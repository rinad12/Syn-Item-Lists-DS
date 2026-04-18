# Synthetic Packing Lists Dataset

A dataset of synthetic packing lists generated for various trip types, destinations, durations, and traveler profiles. Intended for fine-tuning or evaluating language models on list-generation tasks.

## Dataset

`data/dataset.jsonl` — one JSON object per line. Each record represents a single packing list generation task:

```json
{
  "prompt": "Create a packing list for a 7-day beach vacation in Thailand for a solo traveler.",
  "completion": "..."
}
```

## Setup

Requires [uv](https://github.com/astral-sh/uv).

```bash
uv sync
```

## Generate

```bash
uv run generate.py
```

By default generates 100 examples and writes them to `data/dataset.jsonl`. Use `--count` to change the number:

```bash
uv run generate.py --count 500
```

## Schema

| Field        | Type   | Description                                      |
|--------------|--------|--------------------------------------------------|
| `prompt`     | string | User instruction describing the trip             |
| `completion` | string | Packing list as a markdown-formatted string      |
| `metadata`   | object | Trip type, destination, duration, traveler count |

## License

Apache 2.0
