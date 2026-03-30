"""
Merge multiple example JSONL files into one deduplicated training corpus.

Usage:
    python scripts/merge_example_sets.py \
        --source data/raw/nccer_examples.jsonl \
        --source data/raw/njatc_examples.jsonl \
        --out data/raw/electrician_reference_examples.jsonl
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def _load_records(path: str) -> list[dict]:
    source_path = Path(path)
    if not source_path.exists():
        raise FileNotFoundError(path)

    records = []
    with source_path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            stripped = raw_line.strip()
            if not stripped:
                continue
            try:
                record = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number} in {path}: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"Line {line_number} in {path} must be a JSON object")
            records.append(record)
    return records


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Merge example JSONL files into one deduplicated corpus")
    parser.add_argument("--source", action="append", required=True, help="Input JSONL example file")
    parser.add_argument("--out", required=True, help="Output JSONL path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    merged = []
    seen = set()

    for source in args.source:
        for record in _load_records(source):
            key = (
                str(record.get("instruction", "")).strip(),
                str(record.get("input", "")).strip(),
                str(record.get("response", record.get("output", ""))).strip(),
            )
            if key in seen:
                continue
            seen.add(key)
            merged.append(record)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        for record in merged:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Wrote {len(merged)} deduplicated examples to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())