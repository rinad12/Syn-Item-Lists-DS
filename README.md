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
    "risks": ["Vector-borne disease (mosquitoes / ticks)", "High UV exposure"]
  },
  "output": [
    {
      "item": "Long-Sleeved Lightweight Shirt",
      "quantity": 5,
      "reason": "Primary barrier against mosquitoes at dawn/dusk drives."
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

**output** — list of items

| Field | Type | Description |
|---|---|---|
| `item` | string | Specific item name (e.g. "Merino Wool Socks", not "Socks") |
| `quantity` | int | Number of units to pack |
| `reason` | string | Why this item is needed, referencing the scenario context |

## Setup

Requires [uv](https://github.com/astral-sh/uv) and a Google Gemini API key.

```bash
uv sync
echo "GOOGLE_API_KEY=your_key_here" > .env
```

## Generate

```bash
# Generate 1000 samples (default)
uv run generate.py

# Custom options
uv run generate.py --target 500 --seeds seed_examples.md --model gemini-2.5-flash-lite
```

The script appends to existing `.jsonl` files, so it is safe to stop and resume.

## How it works

1. **Dynamic sampling** — each scenario is randomly drawn: intent from 22 categories, infrastructure from 12 types, climate from 14 types, 1–3 risks from 18 options, duration with weighted tiers (60% short 1–7 days, 30% medium 8–21, 10% long 22–90).
2. **Few-shot grounding** — one of 10 expert-curated seed examples is injected into every prompt as a gold standard reference.
3. **Structured output** — Gemini's `response_schema` enforces the Pydantic schema on every response; malformed outputs are skipped automatically.
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
