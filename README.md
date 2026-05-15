# Synthetic Packing Lists Dataset

A synthetic dataset of expert-quality packing lists for fine-tuning travel logistics assistants. Generated with Google Gemini, grounded on 10 hand-curated seed examples via knowledge distillation.

**Dataset on Hugging Face:** [rinad12/Syn-Item-Lists](https://huggingface.co/datasets/rinad12/Syn-Item-Lists)

## Dataset structure

```
data/
  train.jsonl   # 80%
  test.jsonl    # 10%
  val.jsonl     # 10%
```

Each line is a JSON record with an `input` context and a flat `output` list:

```json
{
  "input": {
    "intent": "Wildlife safari",
    "duration": 10,
    "infrastructure": "Basic — rural / remote village",
    "climate": "Subtropical (hot humid summer)",
    "risks": ["Vector-borne disease (mosquitoes / ticks)", "High UV exposure"],
    "max_items": 13
  },
  "output": [
    {
      "item": "Long-Sleeved Lightweight Shirt",
      "quantity": 5,
      "reason": "Barrier against mosquitoes at dawn/dusk drives."
    },
    {
      "item": "DEET Insect Repellent",
      "quantity": 2,
      "reason": "Essential protection against vector-borne disease."
    }
  ]
}
```

### Schema

**input**

| Field | Type | Description |
|---|---|---|
| `intent` | string | Trip purpose (e.g. "Hiking / Trekking", "Wildlife safari") |
| `duration` | int | Trip length in days |
| `infrastructure` | string | Availability of utilities and services at destination |
| `climate` | string | Climate type at destination |
| `risks` | list[string] | 1–3 active risk factors |
| `max_items` | int | Upper bound on list length passed to the model |

**output** — list of items

| Field | Type | Description |
|---|---|---|
| `item` | string | Specific item name (e.g. "Merino Wool Socks", not "Socks") |
| `quantity` | int | Number of units to pack |
| `reason` | string | Why this item is needed (max 10 words) |

## Setup

Requires [uv](https://github.com/astral-sh/uv) and a Google Gemini API key.

```bash
uv sync
echo "GOOGLE_API_KEY=your_key_here" > .env
```

## Generate

```bash
# Generate 1000 samples (default) — overwrites existing data files
uv run generate.py

# Custom options
uv run generate.py --target 500 --seeds seed_examples.md --model gemini-2.5-flash-lite

# Append to existing files instead of overwriting
uv run generate.py --target 500 --append
```

### Flags

| Flag | Default | Description |
|---|---|---|
| `--target N` | `1000` | Total number of samples to generate |
| `--seeds PATH` | `seed_examples.md` | Path to the seed examples markdown file |
| `--model NAME` | `gemini-2.5-flash-lite` | Gemini model to use for generation |
| `--append` | off | Append to existing `.jsonl` files instead of overwriting them |

By default the script **overwrites** `data/train.jsonl`, `data/val.jsonl`, and `data/test.jsonl`. Pass `--append` to extend an existing dataset without losing prior samples.

## How it works

1. **Hierarchical sampling** — scenarios are constructed top-down: intent → infrastructure → climate → risks. Each intent maps to a curated set of plausible infrastructure types; each infrastructure type maps to realistic climates; each climate maps to a risk pool. This prevents nonsensical combinations (e.g. a beach resort in Arctic tundra).
2. **Intent-aware duration** — trip length is drawn from per-intent ranges (e.g. Business trip: 1–5 days; Camping: 5–21 days; Digital nomad: 14–90 days) rather than a single global distribution.
3. **Balanced train split** — the 80% train set is built from a shuffled intent queue so every intent gets equal representation regardless of total sample count.
4. **Seen/unseen val & test isolation** — the val and test sets are each 50% combinations already seen in train and 50% novel (intent × infra × climate) combinations, giving a clean measure of generalisation.
5. **Dynamic list length cap** — `max_items` is calculated per scenario from duration tier (1–3 d → 5–8, 4–10 d → 10–15, 11+ d → 15–25), an intent modifier (e.g. Business trip −3, Camping +3), and a risk floor of `len(risks) + 3`. It is injected into the prompt as a hard constraint.
6. **Few-shot grounding** — one of 10 expert-curated seed examples is injected into every prompt as a gold standard reference.
7. **Structured output** — Gemini's `response_schema` enforces the Pydantic schema on every response; malformed outputs are skipped automatically.
8. **Exponential back-off** — up to 6 retries with jittered delay on API errors.
9. **Stream writing** — each validated sample is appended immediately; no in-memory accumulation.

## Project structure

```
.
├── generate.py          # Generation script (PEP 723 inline metadata)
├── seed_examples.md     # 10 hand-curated expert packing list examples
├── pyproject.toml
├── uv.lock
├── .env                 # GOOGLE_API_KEY (not committed)
└── data/
    ├── train.jsonl
    ├── test.jsonl
    └── val.jsonl
```

## License

Apache 2.0
