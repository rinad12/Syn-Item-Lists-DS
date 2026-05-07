"""Convert old flat JSONL format to new input/output format."""

import json
from pathlib import Path

INPUT_KEYS = {"intent", "duration", "infrastructure", "climate", "risks"}

def convert_record(old: dict) -> dict:
    items = []
    for category in old.get("packing_list", []):
        for item in category.get("items", []):
            items.append({
                "item": item["item"],
                "quantity": item["quantity"],
                "reason": item["reason"],
            })
    return {
        "input": {k: old[k] for k in INPUT_KEYS if k in old},
        "output": items,
    }

for split in ("train", "test", "val"):
    path = Path("data") / f"{split}.jsonl"
    if not path.exists():
        continue
    lines = path.read_text(encoding="utf-8").splitlines()
    converted = []
    skipped = 0
    for line in lines:
        if not line.strip():
            continue
        record = json.loads(line)
        if "input" in record:
            converted.append(line)
            continue
        try:
            converted.append(json.dumps(convert_record(record), ensure_ascii=False))
        except Exception as e:
            print(f"[warn] skipping record: {e}")
            skipped += 1
    path.write_text("\n".join(converted) + "\n", encoding="utf-8")
    print(f"{split}.jsonl: {len(converted)} records converted, {skipped} skipped")
