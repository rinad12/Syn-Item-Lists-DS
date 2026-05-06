# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai>=1.0.0",
#   "pydantic>=2.0.0",
#   "jinja2>=3.1.0",
#   "python-dotenv>=1.0.0",
#   "tqdm>=4.67.0",
# ]
# ///
"""Generate synthetic packing-list dataset using Google Gemini."""

import json
import os
import random
import re
import time
from pathlib import Path
from typing import List

from google import genai
from dotenv import load_dotenv
from jinja2 import Template
from pydantic import BaseModel, ValidationError
from tqdm import tqdm

load_dotenv()

# ---------------------------------------------------------------------------
# Domain lists
# ---------------------------------------------------------------------------

INTENTS = [
    "Beach vacation",
    "Camping / Backpacking",
    "Business trip",
    "City sightseeing",
    "Hiking / Trekking",
    "Ski / Snowboard",
    "Road trip",
    "Volunteer mission",
    "Extreme tourism",
    "Scientific research expedition",
    "Digital nomad relocation",
    "Humanitarian aid mission",
    "Photography expedition",
    "Spiritual pilgrimage",
    "Competitive sports event",
    "Formal event / Destination wedding",
    "Medical tourism",
    "Language immersion program",
    "Culinary tourism",
    "Wildlife safari",
    "Festival attendance",
    "Academic / Study abroad",
]

INFRASTRUCTURES = [
    "None — off-grid / wilderness",
    "Basic — rural / remote village",
    "Developing — inconsistent utilities",
    "Mixed — standard town",
    "Urban / Modern — full services",
    "Industrial / Work site",
    "Resort / Managed environment",
    "Marine / Live-aboard boat",
    "Underground / Cave system",
    "High-altitude research station",
    "Temporary field camp",
    "Luxury / All-inclusive resort",
]

CLIMATES = [
    "Tropical rain (high humidity)",
    "Arid desert (dry heat)",
    "Arctic / Sub-zero cold",
    "High altitude (thin air / intense UV)",
    "Temperate (variable / four seasons)",
    "Mediterranean (dry summer / wet winter)",
    "Maritime (high wind / salt spray)",
    "Monsoonal (seasonal heavy rain)",
    "Subpolar / Tundra",
    "Subtropical (hot humid summer)",
    "Continental (extreme seasonal swings)",
    "Coastal fog / marine layer",
    "Volcanic / geothermal zone",
    "Equatorial rainforest (dense canopy)",
]

RISKS = [
    "High humidity / mold",
    "Dust & sandstorms",
    "Poor water quality",
    "Power instability",
    "Vector-borne disease (mosquitoes / ticks)",
    "High UV exposure",
    "Physical theft / pickpocketing",
    "Civil instability",
    "Extreme wildlife encounters",
    "Air pollution / smog",
    "Seismic activity / earthquakes",
    "Flash floods",
    "Avalanche risk",
    "Jellyfish / marine hazards",
    "Altitude sickness",
    "Frostbite / hypothermia",
    "Food safety / contamination",
    "Communication barriers / no signal",
]

# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------


class PackingItem(BaseModel):
    item: str
    quantity: int
    reason: str


class PackingListResponse(BaseModel):
    items: List[PackingItem]


# ---------------------------------------------------------------------------
# Prompt template
# ---------------------------------------------------------------------------

PROMPT_TEMPLATE = Template(
    """\
Role: Expert Travel Logistics Officer.
Task: Generate a precise, context-aware packing list for the scenario below.

=== SCENARIO ===
- Intent: {{ intent }}
- Duration: {{ duration }} days
- Infrastructure Level: {{ infrastructure }}
- Climate: {{ climate }}
- Risk Factors:
{% for risk in risks %}  * {{ risk }}
{% endfor %}
=== GOLD STANDARD EXAMPLE (follow this quality and reasoning depth) ===
{{ seed_example }}

=== REQUIREMENTS ===
1. ADAPTIVE SCALING — derive quantities from the {{ duration }}-day duration.
2. RISK MITIGATION — include at least one item that directly addresses each
   listed risk factor. Call out the risk by name in the item's reason field.
3. COMPOUND THREATS — if multiple risks overlap, prioritise items that
   address both simultaneously and state so in the reason.
4. INFRASTRUCTURE LOGIC — if infrastructure is off-grid or basic AND
   duration > 7 days, add sustainability items (repair kit, laundry
   solution, extra batteries, water purification).
5. ITEM SCHEMA — every item must have:
   - item: descriptive name (be specific, e.g. "Merino Wool Socks" not "Socks")
   - quantity: integer
   - reason: one short sentence (max 15 words) explaining the WHY
"""
)

# ---------------------------------------------------------------------------
# Seed parser
# ---------------------------------------------------------------------------


def parse_seeds(seeds_path: Path) -> list[dict]:
    """Extract JSON blocks from a markdown file of expert examples."""
    text = seeds_path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(.*?)```", text, re.DOTALL)
    seeds: list[dict] = []
    for block in blocks:
        try:
            seeds.append(json.loads(block.strip()))
        except json.JSONDecodeError as exc:
            print(f"[warn] Could not parse seed block: {exc}")
    return seeds


# ---------------------------------------------------------------------------
# Dynamic input sampling
# ---------------------------------------------------------------------------


def sample_duration() -> int:
    """Weighted duration: 60% short (1-7), 30% medium (8-21), 10% long (22-90)."""
    tier = random.choices(["short", "medium", "long"], weights=[60, 30, 10])[0]
    if tier == "short":
        return random.randint(1, 7)
    if tier == "medium":
        return random.randint(8, 21)
    return random.randint(22, 90)


def sample_scenario(seeds: list[dict]) -> dict:
    """Return a dict of randomised scenario inputs plus one seed example."""
    return {
        "intent": random.choice(INTENTS),
        "duration": sample_duration(),
        "infrastructure": random.choice(INFRASTRUCTURES),
        "climate": random.choice(CLIMATES),
        "risks": random.sample(RISKS, k=random.randint(1, 3)),
        "seed_example": json.dumps(random.choice(seeds), indent=2),
    }


# ---------------------------------------------------------------------------
# Exponential back-off
# ---------------------------------------------------------------------------


def call_with_backoff(fn, max_retries: int = 6, base_delay: float = 2.0):
    """Call fn(), retrying with exponential back-off on any exception."""
    for attempt in range(max_retries):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2**attempt) + random.uniform(0, 1)
            print(f"\n[retry {attempt + 1}/{max_retries}] {exc!r} — sleeping {delay:.1f}s")
            time.sleep(delay)


# ---------------------------------------------------------------------------
# Main generation loop
# ---------------------------------------------------------------------------


def main(target: int = 1000, seeds_file: str = "seed_examples.md", model_name: str = "gemini-2.5-flash-lite") -> None:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError("GOOGLE_API_KEY not found in environment / .env file.")

    client = genai.Client(api_key=api_key)
    gen_config = genai.types.GenerateContentConfig(
        temperature=1.0,
        response_mime_type="application/json",
        response_schema=PackingListResponse,
    )

    seeds = parse_seeds(Path(seeds_file))
    if not seeds:
        raise ValueError(f"No seed examples found in {seeds_file!r}.")
    print(f"Loaded {len(seeds)} seed examples from {seeds_file!r}.")

    # Prepare output files
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    split_paths = {
        "train": data_dir / "train.jsonl",
        "test": data_dir / "test.jsonl",
        "val": data_dir / "val.jsonl",
    }
    split_files = {name: path.open("a", encoding="utf-8") for name, path in split_paths.items()}
    split_weights = {"train": 80, "test": 10, "val": 10}

    counts = {"train": 0, "test": 0, "val": 0, "errors": 0}

    try:
        with tqdm(total=target, desc="Generating samples", unit="sample") as pbar:
            while sum(v for k, v in counts.items() if k != "errors") < target:
                scenario = sample_scenario(seeds)
                prompt = PROMPT_TEMPLATE.render(**scenario)

                # Strip seed_example from the record we persist (it's large and redundant)
                scenario_record = {k: v for k, v in scenario.items() if k != "seed_example"}

                try:
                    response = call_with_backoff(
                        lambda p=prompt: client.models.generate_content(
                            model=model_name, contents=p, config=gen_config
                        )
                    )
                    parsed: PackingListResponse = response.parsed or PackingListResponse.model_validate_json(
                        response.text
                    )
                except (ValidationError, Exception) as exc:
                    counts["errors"] += 1
                    tqdm.write(f"[error] Skipping sample: {exc!r}")
                    continue

                record = {
                    "input": scenario_record,
                    "output": [item.model_dump() for item in parsed.items],
                }

                # Choose split
                split = random.choices(
                    list(split_weights.keys()),
                    weights=list(split_weights.values()),
                )[0]
                split_files[split].write(json.dumps(record, ensure_ascii=False) + "\n")
                split_files[split].flush()

                counts[split] += 1
                pbar.update(1)
                pbar.set_postfix(
                    train=counts["train"],
                    test=counts["test"],
                    val=counts["val"],
                    errors=counts["errors"],
                )
    finally:
        for fh in split_files.values():
            fh.close()

    total = counts["train"] + counts["test"] + counts["val"]
    print(
        f"\nDone — {total} samples written "
        f"(train={counts['train']}, test={counts['test']}, val={counts['val']}, "
        f"errors={counts['errors']})"
    )
    for path in split_paths.values():
        if path.exists():
            lines = sum(1 for _ in path.open(encoding="utf-8"))
            print(f"  {path}: {lines} lines")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate synthetic packing-list dataset.")
    parser.add_argument(
        "--target", type=int, default=1000, help="Number of samples to generate (default: 1000)"
    )
    parser.add_argument(
        "--seeds", type=str, default="seed_examples.md", help="Path to seeds markdown file"
    )
    parser.add_argument(
        "--model", type=str, default="gemini-2.5-flash-lite", help="Gemini model name (default: gemini-2.5-flash-lite)"
    )
    args = parser.parse_args()
    main(target=args.target, seeds_file=args.seeds, model_name=args.model)
