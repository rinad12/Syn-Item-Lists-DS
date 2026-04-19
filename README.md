# Synthetic Packing Lists Dataset

A synthetic dataset of expert-quality packing lists for fine-tuning travel logistics assistants (e.g. Gemma 4). Generated with Google Gemini 2.0 Flash, grounded on 10 hand-curated seed examples.

This dataset was developed using the **Knowledge Distillation** method, where 10 expert scenarios — curated from open web data and professional logistics/survival sources — served as the gold standard seeds for generating an expanded synthetic sample.

## Dataset structure

```
data/
  train.jsonl   # 80% of generated samples
  test.jsonl    # 10%
  val.jsonl     # 10%
```

Each line is a self-contained JSON record:

```json
{
  "intent": "Wildlife safari",
  "duration": 10,
  "infrastructure": "Basic — rural / remote village",
  "climate": "Subtropical (hot humid summer)",
  "risks": ["Vector-borne disease (mosquitoes / ticks)", "High UV exposure"],
  "reasoning": "A 10-day safari in a basic-infrastructure subtropical environment...",
  "packing_list": [
    {
      "category": "Clothing",
      "items": [
        {
          "item": "Long-Sleeved Lightweight Shirt",
          "quantity": 5,
          "formula": "N/2",
          "reason": "Rotation with camp laundry every 2 days; long sleeves are the primary physical barrier against mosquito bites during dawn/dusk game drives."
        }
      ]
    },
    {
      "category": "Health & Hygiene",
      "items": ["..."]
    }
  ]
}
```

### Schema

| Field          | Type                              | Description                                                  |
|----------------|-----------------------------------|--------------------------------------------------------------|
| `intent`       | string                            | Trip purpose (e.g. "Hiking / Trekking", "Business trip")    |
| `duration`     | int                               | Trip length in days                                          |
| `infrastructure` | string                          | Availability of utilities and services at destination        |
| `climate`      | string                            | Climate type at destination                                  |
| `risks`        | list[string]                      | 1–3 active risk factors                                      |
| `reasoning`    | string                            | Model's explanation of how risks/climate shaped the list     |
| `packing_list` | list[PackingCategory]             | Items grouped by category                                    |

**PackingCategory fields:** `category` (str) · `items` (list[PackingItem])

**PackingItem fields:** `item` · `quantity` · `formula` · `reason`

Quantity formulas follow the convention: `N` = one per day, `N+1` = daily + buffer, `N/2` = every-other-day rotation, `Constant` = fixed regardless of duration.

## Setup

Requires [uv](https://github.com/astral-sh/uv) and a Google Gemini API key.

```bash
# Install dependencies
uv sync

# Create .env file
echo "GOOGLE_API_KEY=your_key_here" > .env
```

## Generate

```bash
# Generate 1000 samples (default)
uv run generate.py

# Custom target
uv run generate.py --target 500

# Custom seeds file
uv run generate.py --seeds seed_examples.md --target 1000
```

The script appends to existing `.jsonl` files, so it is safe to stop and resume.

## How it works

1. **Dynamic sampling** — each scenario is randomly drawn: intent from 22 categories, infrastructure from 12 types, climate from 14 types, 1–3 risks from 18 options, duration with weighted tiers (60% short 1–7 days, 30% medium 8–21, 10% long 22–90).
2. **Few-shot grounding** — one of 10 expert-curated seed examples is injected into every prompt as a Gold Standard reference.
3. **Structured output** — Gemini's `response_schema` feature enforces the Pydantic schema on every response; malformed outputs are skipped automatically.
4. **Exponential back-off** — up to 6 retries with jittered delay on API errors.
5. **Stream writing** — each validated sample is appended immediately; no in-memory accumulation.


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
