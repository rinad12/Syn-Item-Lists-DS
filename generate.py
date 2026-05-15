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
# Hierarchical sampling logic
# ---------------------------------------------------------------------------

INTENT_TO_INFRA: dict[str, list[str]] = {
    "Beach vacation": [
        "Resort / Managed environment",
        "Luxury / All-inclusive resort",
        "Marine / Live-aboard boat",
        "Mixed — standard town",
    ],
    "Camping / Backpacking": [
        "None — off-grid / wilderness",
        "Basic — rural / remote village",
        "Temporary field camp",
    ],
    "Business trip": [
        "Urban / Modern — full services",
        "Industrial / Work site",
        "Luxury / All-inclusive resort",
        "Mixed — standard town",
    ],
    "City sightseeing": [
        "Urban / Modern — full services",
        "Mixed — standard town",
        "Luxury / All-inclusive resort",
    ],
    "Hiking / Trekking": [
        "None — off-grid / wilderness",
        "Basic — rural / remote village",
        "Temporary field camp",
        "High-altitude research station",
    ],
    "Ski / Snowboard": [
        "Resort / Managed environment",
        "High-altitude research station",
        "Temporary field camp",
    ],
    "Road trip": [
        "Mixed — standard town",
        "Urban / Modern — full services",
        "Basic — rural / remote village",
        "Developing — inconsistent utilities",
    ],
    "Volunteer mission": [
        "Basic — rural / remote village",
        "Developing — inconsistent utilities",
        "Temporary field camp",
        "None — off-grid / wilderness",
    ],
    "Extreme tourism": [
        "None — off-grid / wilderness",
        "Temporary field camp",
        "High-altitude research station",
        "Underground / Cave system",
        "Marine / Live-aboard boat",
    ],
    "Scientific research expedition": [
        "None — off-grid / wilderness",
        "Temporary field camp",
        "High-altitude research station",
        "Basic — rural / remote village",
    ],
    "Digital nomad relocation": [
        "Urban / Modern — full services",
        "Mixed — standard town",
        "Developing — inconsistent utilities",
    ],
    "Humanitarian aid mission": [
        "Basic — rural / remote village",
        "Developing — inconsistent utilities",
        "Temporary field camp",
        "None — off-grid / wilderness",
    ],
    "Photography expedition": [
        "None — off-grid / wilderness",
        "Temporary field camp",
        "Basic — rural / remote village",
        "Mixed — standard town",
        "High-altitude research station",
    ],
    "Spiritual pilgrimage": [
        "Basic — rural / remote village",
        "Developing — inconsistent utilities",
        "Mixed — standard town",
        "Resort / Managed environment",
    ],
    "Competitive sports event": [
        "Urban / Modern — full services",
        "Resort / Managed environment",
        "Mixed — standard town",
        "Industrial / Work site",
    ],
    "Formal event / Destination wedding": [
        "Luxury / All-inclusive resort",
        "Resort / Managed environment",
        "Urban / Modern — full services",
    ],
    "Medical tourism": [
        "Urban / Modern — full services",
        "Mixed — standard town",
        "Luxury / All-inclusive resort",
    ],
    "Language immersion program": [
        "Urban / Modern — full services",
        "Mixed — standard town",
        "Developing — inconsistent utilities",
    ],
    "Culinary tourism": [
        "Urban / Modern — full services",
        "Mixed — standard town",
        "Luxury / All-inclusive resort",
        "Resort / Managed environment",
    ],
    "Wildlife safari": [
        "None — off-grid / wilderness",
        "Basic — rural / remote village",
        "Temporary field camp",
        "Resort / Managed environment",
    ],
    "Festival attendance": [
        "Mixed — standard town",
        "Urban / Modern — full services",
        "Developing — inconsistent utilities",
        "Temporary field camp",
    ],
    "Academic / Study abroad": [
        "Urban / Modern — full services",
        "Mixed — standard town",
        "Developing — inconsistent utilities",
    ],
}

INFRA_TO_CLIMATE: dict[str, list[str]] = {
    "None — off-grid / wilderness": [
        "Arctic / Sub-zero cold",
        "High altitude (thin air / intense UV)",
        "Tropical rain (high humidity)",
        "Arid desert (dry heat)",
        "Subpolar / Tundra",
        "Continental (extreme seasonal swings)",
        "Equatorial rainforest (dense canopy)",
        "Monsoonal (seasonal heavy rain)",
    ],
    "Basic — rural / remote village": [
        "Tropical rain (high humidity)",
        "Arid desert (dry heat)",
        "Temperate (variable / four seasons)",
        "Monsoonal (seasonal heavy rain)",
        "Subtropical (hot humid summer)",
        "Continental (extreme seasonal swings)",
        "Equatorial rainforest (dense canopy)",
        "Mediterranean (dry summer / wet winter)",
    ],
    "Developing — inconsistent utilities": [
        "Tropical rain (high humidity)",
        "Arid desert (dry heat)",
        "Temperate (variable / four seasons)",
        "Monsoonal (seasonal heavy rain)",
        "Subtropical (hot humid summer)",
        "Mediterranean (dry summer / wet winter)",
        "Continental (extreme seasonal swings)",
    ],
    "Mixed — standard town": [
        "Temperate (variable / four seasons)",
        "Mediterranean (dry summer / wet winter)",
        "Continental (extreme seasonal swings)",
        "Subtropical (hot humid summer)",
        "Maritime (high wind / salt spray)",
        "Coastal fog / marine layer",
        "Monsoonal (seasonal heavy rain)",
    ],
    "Urban / Modern — full services": [
        "Temperate (variable / four seasons)",
        "Mediterranean (dry summer / wet winter)",
        "Subtropical (hot humid summer)",
        "Continental (extreme seasonal swings)",
        "Maritime (high wind / salt spray)",
        "Coastal fog / marine layer",
        "Arid desert (dry heat)",
        "Tropical rain (high humidity)",
    ],
    "Industrial / Work site": [
        "Arid desert (dry heat)",
        "Arctic / Sub-zero cold",
        "Tropical rain (high humidity)",
        "Continental (extreme seasonal swings)",
        "Temperate (variable / four seasons)",
        "Maritime (high wind / salt spray)",
    ],
    "Resort / Managed environment": [
        "Tropical rain (high humidity)",
        "Mediterranean (dry summer / wet winter)",
        "Subtropical (hot humid summer)",
        "Coastal fog / marine layer",
        "Temperate (variable / four seasons)",
        "Arctic / Sub-zero cold",
        "High altitude (thin air / intense UV)",
    ],
    "Marine / Live-aboard boat": [
        "Tropical rain (high humidity)",
        "Maritime (high wind / salt spray)",
        "Mediterranean (dry summer / wet winter)",
        "Coastal fog / marine layer",
        "Subtropical (hot humid summer)",
        "Equatorial rainforest (dense canopy)",
    ],
    "Underground / Cave system": [
        "Temperate (variable / four seasons)",
        "Tropical rain (high humidity)",
        "High altitude (thin air / intense UV)",
        "Continental (extreme seasonal swings)",
        "Volcanic / geothermal zone",
    ],
    "High-altitude research station": [
        "Arctic / Sub-zero cold",
        "High altitude (thin air / intense UV)",
        "Subpolar / Tundra",
        "Continental (extreme seasonal swings)",
    ],
    "Temporary field camp": [
        "Arctic / Sub-zero cold",
        "Arid desert (dry heat)",
        "Tropical rain (high humidity)",
        "High altitude (thin air / intense UV)",
        "Subpolar / Tundra",
        "Monsoonal (seasonal heavy rain)",
        "Continental (extreme seasonal swings)",
        "Equatorial rainforest (dense canopy)",
    ],
    "Luxury / All-inclusive resort": [
        "Tropical rain (high humidity)",
        "Mediterranean (dry summer / wet winter)",
        "Subtropical (hot humid summer)",
        "Coastal fog / marine layer",
        "Temperate (variable / four seasons)",
    ],
}

CLIMATE_TO_RISKS: dict[str, list[str]] = {
    "Tropical rain (high humidity)": [
        "High humidity / mold",
        "Vector-borne disease (mosquitoes / ticks)",
        "Poor water quality",
        "Flash floods",
        "Food safety / contamination",
        "High UV exposure",
        "Communication barriers / no signal",
    ],
    "Arid desert (dry heat)": [
        "Dust & sandstorms",
        "High UV exposure",
        "Poor water quality",
        "Extreme wildlife encounters",
        "Communication barriers / no signal",
        "Food safety / contamination",
    ],
    "Arctic / Sub-zero cold": [
        "Frostbite / hypothermia",
        "Avalanche risk",
        "Communication barriers / no signal",
        "Power instability",
        "Flash floods",
    ],
    "High altitude (thin air / intense UV)": [
        "Altitude sickness",
        "High UV exposure",
        "Frostbite / hypothermia",
        "Avalanche risk",
        "Communication barriers / no signal",
        "Power instability",
    ],
    "Temperate (variable / four seasons)": [
        "Physical theft / pickpocketing",
        "Flash floods",
        "Food safety / contamination",
        "Air pollution / smog",
        "Vector-borne disease (mosquitoes / ticks)",
        "Civil instability",
    ],
    "Mediterranean (dry summer / wet winter)": [
        "High UV exposure",
        "Physical theft / pickpocketing",
        "Food safety / contamination",
        "Seismic activity / earthquakes",
        "Civil instability",
        "Air pollution / smog",
    ],
    "Maritime (high wind / salt spray)": [
        "Jellyfish / marine hazards",
        "Flash floods",
        "Communication barriers / no signal",
        "High UV exposure",
        "Power instability",
    ],
    "Monsoonal (seasonal heavy rain)": [
        "Flash floods",
        "High humidity / mold",
        "Vector-borne disease (mosquitoes / ticks)",
        "Poor water quality",
        "Power instability",
        "Food safety / contamination",
        "Communication barriers / no signal",
    ],
    "Subpolar / Tundra": [
        "Frostbite / hypothermia",
        "Communication barriers / no signal",
        "Power instability",
        "Extreme wildlife encounters",
        "Flash floods",
    ],
    "Subtropical (hot humid summer)": [
        "High humidity / mold",
        "Vector-borne disease (mosquitoes / ticks)",
        "High UV exposure",
        "Flash floods",
        "Food safety / contamination",
        "Air pollution / smog",
        "Seismic activity / earthquakes",
    ],
    "Continental (extreme seasonal swings)": [
        "Frostbite / hypothermia",
        "Flash floods",
        "Civil instability",
        "Air pollution / smog",
        "Power instability",
        "Food safety / contamination",
    ],
    "Coastal fog / marine layer": [
        "Jellyfish / marine hazards",
        "High humidity / mold",
        "Flash floods",
        "Physical theft / pickpocketing",
        "Communication barriers / no signal",
    ],
    "Volcanic / geothermal zone": [
        "Seismic activity / earthquakes",
        "Air pollution / smog",
        "High UV exposure",
        "Communication barriers / no signal",
        "Extreme wildlife encounters",
    ],
    "Equatorial rainforest (dense canopy)": [
        "High humidity / mold",
        "Vector-borne disease (mosquitoes / ticks)",
        "Poor water quality",
        "Extreme wildlife encounters",
        "Flash floods",
        "Communication barriers / no signal",
        "Food safety / contamination",
    ],
}

# Per-intent duration ranges; intents absent here use the weighted fallback.
INTENT_DURATION_RANGES: dict[str, tuple[int, int]] = {
    "Digital nomad relocation":           (14, 90),
    "Academic / Study abroad":            (14, 90),
    "Language immersion program":         (14, 90),
    "Business trip":                      (1,  5),
    "Formal event / Destination wedding": (1,  5),
    "Hiking / Trekking":                  (5,  21),
    "Camping / Backpacking":              (5,  21),
    "Volunteer mission":                  (5,  21),
    "Humanitarian aid mission":           (5,  21),
    "Ski / Snowboard":                    (3,  14),
    "Scientific research expedition":     (7,  30),
    "Photography expedition":             (7,  30),
    "Wildlife safari":                    (7,  30),
}

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
5. CONCISE OUTPUT — Do not exceed {{ max_items }} total items. Prioritise the
   most critical gear for survival, professional needs, and risk mitigation.
   Avoid filler items.
6. ITEM SCHEMA — every item must have:
   - item: descriptive name (be specific, e.g. "Merino Wool Socks" not "Socks")
   - quantity: integer
   - reason: one short sentence (max 10 words) explaining the WHY
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
# Sampling functions
# ---------------------------------------------------------------------------


def sample_duration(intent: str) -> int:
    """Return a duration in days appropriate for the given intent."""
    if intent in INTENT_DURATION_RANGES:
        lo, hi = INTENT_DURATION_RANGES[intent]
        return random.randint(lo, hi)
    tier = random.choices(["short", "medium", "long"], weights=[60, 30, 10])[0]
    if tier == "short":
        return random.randint(1, 7)
    if tier == "medium":
        return random.randint(8, 21)
    return random.randint(22, 90)


_INTENT_ITEM_MODIFIER: dict[str, int] = {
    "Business trip": -3,
    "Formal event / Destination wedding": -2,
    "Camping / Backpacking": 3,
    "Hiking / Trekking": 2,
    "Humanitarian aid mission": 2,
    "Scientific research expedition": 3,
    "Photography expedition": 2,
}


def calculate_max_items(intent: str, duration: int, risks: list[str]) -> int:
    """Return a max item count ceiling for the prompt."""
    if duration <= 3:
        base = random.randint(5, 8)
    elif duration <= 10:
        base = random.randint(10, 15)
    else:
        base = random.randint(15, 25)
    modifier = _INTENT_ITEM_MODIFIER.get(intent, 0)
    base = max(base + modifier, 5)
    return max(base, len(risks) + 3)


def sample_scenario(
    seeds: list[dict],
    intent: str,
    used_combos: set[tuple[str, str, str]] | None = None,
    require_unseen: bool = False,
) -> tuple[dict, tuple[str, str, str]]:
    """
    Top-down hierarchical sampling: intent → infra → climate → risks.

    If require_unseen=True, makes a best-effort attempt to return a
    (intent, infra, climate) combo not present in used_combos.
    Falls back gracefully if all combos are exhausted.
    """
    used_combos = used_combos or set()
    infra_candidates = INTENT_TO_INFRA.get(intent) or INFRASTRUCTURES

    max_attempts = max(len(infra_candidates) * 3, 10)
    infra = random.choice(infra_candidates)
    climate_candidates = INFRA_TO_CLIMATE.get(infra) or CLIMATES
    climate = random.choice(climate_candidates)
    combo = (intent, infra, climate)

    if require_unseen and combo in used_combos:
        for _ in range(max_attempts - 1):
            infra = random.choice(infra_candidates)
            climate_candidates = INFRA_TO_CLIMATE.get(infra) or CLIMATES
            climate = random.choice(climate_candidates)
            combo = (intent, infra, climate)
            if combo not in used_combos:
                break
        else:
            tqdm.write(f"[warn] intent '{intent}': no unseen combo found after {max_attempts} attempts — using seen combo")

    risk_pool = CLIMATE_TO_RISKS.get(climate) or RISKS
    k = random.randint(1, min(3, len(risk_pool)))
    risks = random.sample(risk_pool, k=k)

    duration = sample_duration(intent)
    scenario = {
        "intent": intent,
        "duration": duration,
        "infrastructure": infra,
        "climate": climate,
        "risks": risks,
        "seed_example": json.dumps(random.choice(seeds), indent=2),
        "max_items": calculate_max_items(intent, duration, risks),
    }
    return scenario, combo


def compute_intent_counts(target_train: int) -> dict[str, int]:
    """Distribute target_train samples equally across all intents."""
    n = len(INTENTS)
    base = target_train // n
    remainder = target_train % n
    counts = {intent: base for intent in INTENTS}
    for intent in INTENTS[:remainder]:
        counts[intent] += 1
    return counts


# ---------------------------------------------------------------------------
# LLM call helper
# ---------------------------------------------------------------------------


def _generate_record(
    client: genai.Client,
    gen_config: genai.types.GenerateContentConfig,
    model_name: str,
    scenario: dict,
) -> dict:
    """Render prompt, call LLM with backoff, parse and return the JSONL record dict."""
    prompt = PROMPT_TEMPLATE.render(**scenario)
    scenario_record = {k: v for k, v in scenario.items() if k != "seed_example"}

    response = call_with_backoff(
        lambda p=prompt: client.models.generate_content(
            model=model_name, contents=p, config=gen_config
        )
    )
    parsed: PackingListResponse = response.parsed or PackingListResponse.model_validate_json(
        response.text
    )
    return {
        "input": scenario_record,
        "output": [item.model_dump() for item in parsed.items],
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


def main(target: int = 1000, seeds_file: str = "seed_examples.md", model_name: str = "gemini-2.5-flash-lite", append: bool = False) -> None:
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

    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    split_paths = {
        "train": data_dir / "train.jsonl",
        "test": data_dir / "test.jsonl",
        "val": data_dir / "val.jsonl",
    }
    file_mode = "a" if append else "w"
    split_files = {name: path.open(file_mode, encoding="utf-8") for name, path in split_paths.items()}

    counts = {"train": 0, "test": 0, "val": 0, "errors": 0}

    target_train = int(target * 0.80)
    target_val   = int(target * 0.10)
    target_test  = target - target_train - target_val

    # Build a shuffled intent queue with equal per-intent representation.
    intent_counts = compute_intent_counts(target_train)
    intent_queue: list[str] = []
    for intent, n in intent_counts.items():
        intent_queue.extend([intent] * n)
    random.shuffle(intent_queue)

    # train_combinations starts empty each run; cross-run isolation is not
    # guaranteed when --append is used across multiple generation sessions.
    train_combinations: set[tuple[str, str, str]] = set()

    try:
        with tqdm(total=target, desc="Generating samples", unit="sample") as pbar:

            # ── Phase 1: TRAIN ────────────────────────────────────────────
            queue_idx = 0
            while counts["train"] < target_train:
                if queue_idx < len(intent_queue):
                    intent = intent_queue[queue_idx]
                    queue_idx += 1
                else:
                    intent = random.choice(INTENTS)

                scenario, combo = sample_scenario(seeds, intent)

                try:
                    record = _generate_record(client, gen_config, model_name, scenario)
                except (ValidationError, Exception) as exc:
                    counts["errors"] += 1
                    tqdm.write(f"[error] Skipping sample: {exc!r}")
                    continue

                split_files["train"].write(json.dumps(record, ensure_ascii=False) + "\n")
                split_files["train"].flush()
                train_combinations.add(combo)
                counts["train"] += 1
                pbar.update(1)
                pbar.set_postfix(
                    train=counts["train"],
                    test=counts["test"],
                    val=counts["val"],
                    errors=counts["errors"],
                )

            # ── Phase 2: VAL + TEST ───────────────────────────────────────
            for split_name, split_target in [("val", target_val), ("test", target_test)]:
                generated_in_split = 0
                seen_target   = round(split_target * 0.5)
                unseen_target = split_target - seen_target
                seen_count    = 0
                unseen_count  = 0

                while generated_in_split < split_target:
                    need_unseen = unseen_count < unseen_target
                    intent = random.choice(INTENTS)

                    scenario, combo = sample_scenario(
                        seeds,
                        intent,
                        used_combos=train_combinations,
                        require_unseen=need_unseen,
                    )
                    is_unseen = combo not in train_combinations

                    try:
                        record = _generate_record(client, gen_config, model_name, scenario)
                    except (ValidationError, Exception) as exc:
                        counts["errors"] += 1
                        tqdm.write(f"[error] Skipping sample: {exc!r}")
                        continue

                    split_files[split_name].write(json.dumps(record, ensure_ascii=False) + "\n")
                    split_files[split_name].flush()

                    if is_unseen:
                        unseen_count += 1
                    else:
                        seen_count += 1

                    counts[split_name] += 1
                    generated_in_split += 1
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
    parser.add_argument(
        "--append", action="store_true", help="Append to existing data files instead of overwriting"
    )
    args = parser.parse_args()
    main(target=args.target, seeds_file=args.seeds, model_name=args.model, append=args.append)
