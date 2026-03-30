"""
Build a curated electrician golden benchmark from a benchmark spec.
"""

import argparse
import json
import os

from manifest_utils import current_utc_timestamp, sha256_file, write_json_file
from retrieval_utils import parse_reference_response


def load_json(path: str) -> object:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a curated golden benchmark from a spec file.")
    parser.add_argument("--source", required=True, help="Source example JSONL file.")
    parser.add_argument("--spec", required=True, help="Benchmark spec JSON file.")
    parser.add_argument("--out", required=True, help="Golden benchmark JSONL output path.")
    parser.add_argument("--manifest", required=True, help="Golden benchmark manifest JSON output path.")
    args = parser.parse_args()

    spec_rows = load_json(args.spec)
    if not isinstance(spec_rows, list) or not spec_rows:
        raise SystemExit("Benchmark spec must be a non-empty JSON array")

    with open(args.source, "r", encoding="utf-8") as handle:
        source_rows = [json.loads(line) for line in handle if line.strip()]

    benchmark_rows: list[dict] = []
    for index, spec in enumerate(spec_rows, start=1):
        if not isinstance(spec, dict):
            raise SystemExit(f"Spec entry {index} must be a JSON object")

        instruction = spec.get("instruction")
        source_match = spec.get("source")
        category = spec.get("category")
        benchmark_id = spec.get("benchmark_id") or f"electrician-{index:03d}"
        if not all(isinstance(value, str) and value.strip() for value in (instruction, source_match, category)):
            raise SystemExit(f"Spec entry {index} must define non-empty instruction, source, and category")

        matched_row = None
        matched_source = None
        matched_section = None
        for row in source_rows:
            if row.get("instruction") != instruction:
                continue

            parsed = parse_reference_response(row.get("response") or row.get("output") or "")
            source_name = parsed.get("source") or ""
            if source_match not in source_name:
                continue

            matched_row = row
            matched_source = source_name
            matched_section = parsed.get("section")
            break

        if matched_row is None:
            raise SystemExit(
                f"Could not find benchmark row for instruction='{instruction}' source='{source_match}'"
            )

        benchmark_rows.append({
            "benchmark_id": benchmark_id,
            "category": category,
            "source": matched_source,
            "section": matched_section,
            "instruction": matched_row.get("instruction"),
            "input": matched_row.get("input"),
            "response": matched_row.get("response") or matched_row.get("output"),
        })

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as handle:
        for row in benchmark_rows:
            handle.write(json.dumps(row, ensure_ascii=False))
            handle.write("\n")

    category_counts: dict[str, int] = {}
    for row in benchmark_rows:
        category_counts[row["category"]] = category_counts.get(row["category"], 0) + 1

    manifest = {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "source": {
            "path": os.path.abspath(args.source),
            "sha256": sha256_file(args.source),
        },
        "spec": {
            "path": os.path.abspath(args.spec),
            "sha256": sha256_file(args.spec),
        },
        "output": {
            "path": os.path.abspath(args.out),
            "count": len(benchmark_rows),
        },
        "categories": category_counts,
        "benchmark_ids": [row["benchmark_id"] for row in benchmark_rows],
    }
    write_json_file(args.manifest, manifest)

    print(f"Built golden benchmark with {len(benchmark_rows)} rows → {args.out}")
    print(f"Manifest written to {args.manifest}")


if __name__ == "__main__":
    main()