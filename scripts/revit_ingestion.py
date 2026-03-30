"""
Normalize Revit-derived family references into JSONL records for retrieval.

This script does not parse .rfa binaries directly. Instead, it supports two
practical inputs that already exist in the user's environment:

1. Structured CSV or JSONL exports from Revit, pyRevit, Dynamo, Stratus, or
   schedule exports.
2. Recursive file scans of family directories to bootstrap a reference catalog
   from .rfa filenames when richer metadata is not available yet.

The output is reference data for lookup and indexing. It is not training data.

Examples:
    python scripts/revit_ingestion.py \
        --family-dir /mnt/c/Users/Paul/Revit/Families \
        --out data/raw/revit_family_index.jsonl

    python scripts/revit_ingestion.py \
        --source /mnt/c/Users/Paul/RSmeans/get_part_template_responses.csv \
        --source data/raw/revit_schedule_export.jsonl \
        --out data/raw/revit_family_index.jsonl
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
from pathlib import Path

from data_contracts import build_data_contract, stable_identifier


SCAN_EXTENSIONS = {".rfa"}
OPTIONAL_SCAN_EXTENSIONS = {".rvt"}
MAX_EXTRA_FIELDS = 40


def _clean_value(value):
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = " ".join(value.strip().split())
        return cleaned or None
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        parts = [_clean_value(item) for item in value]
        return ", ".join(part for part in parts if part) or None
    if isinstance(value, dict):
        parts = []
        for key, item in value.items():
            cleaned = _clean_value(item)
            if cleaned:
                parts.append(f"{key}: {cleaned}")
        return "; ".join(parts) or None
    return str(value)


def _normalise_key(key: str) -> str:
    return "".join(ch.lower() for ch in str(key).strip() if ch.isalnum())


def _safe_parse_literal(value):
    if not isinstance(value, str):
        return value
    stripped = value.strip()
    if not stripped:
        return None
    if stripped[0] not in "[{(":
        return value
    try:
        return ast.literal_eval(stripped)
    except (ValueError, SyntaxError):
        return value


def _load_source(path: str) -> list[dict]:
    source_path = Path(path)
    if not source_path.exists():
        raise FileNotFoundError(path)

    extension = source_path.suffix.lower()
    if extension == ".jsonl":
        records = []
        with source_path.open("r", encoding="utf-8") as handle:
            for line_number, raw_line in enumerate(handle, start=1):
                stripped = raw_line.strip()
                if not stripped:
                    continue
                try:
                    record = json.loads(stripped)
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Invalid JSON on line {line_number} in {path}: {exc}"
                    ) from exc
                if not isinstance(record, dict):
                    raise ValueError(f"Line {line_number} in {path} must be a JSON object")
                records.append(record)
        return records

    if extension == ".csv":
        with source_path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))

    raise ValueError(f"Unsupported source format for {path}: {extension}")


def _lookup_value(record: dict, aliases: list[str]):
    normalised = {_normalise_key(key): value for key, value in record.items()}
    for alias in aliases:
        value = normalised.get(_normalise_key(alias))
        if value is None:
            continue
        parsed = _safe_parse_literal(value)
        cleaned = _clean_value(parsed)
        if cleaned:
            return cleaned
    return None


def _tokenize(*values: str | None) -> list[str]:
    tokens = set()
    for value in values:
        if not value:
            continue
        normalized = []
        for char in value.lower():
            normalized.append(char if char.isalnum() else " ")
        for token in "".join(normalized).split():
            if len(token) >= 2:
                tokens.add(token)
    return sorted(tokens)


def _build_lookup_key(record: dict) -> str:
    parts = []
    for key in ("category", "family_name", "type_name", "manufacturer", "part_number"):
        value = record.get(key)
        if value:
            parts.append(value.lower())
    normalized = []
    for char in "|".join(parts):
        normalized.append(char if char.isalnum() else "-")
    joined = "".join(normalized)
    while "--" in joined:
        joined = joined.replace("--", "-")
    return joined.strip("-")


def _attach_spatial_contract(record: dict) -> dict:
    record["record_id"] = stable_identifier(
        "revit_family_reference",
        record.get("lookup_key") or record.get("family_and_type") or record.get("family_name"),
        record.get("source_path") or record.get("source_name"),
    )
    record["data_contract"] = build_data_contract(
        data_family="spatial_grounding_records",
        runtime_owner="geometry_rules",
        routing_hint="deterministic_tool_input",
    )
    return record


def _collect_extra_fields(record: dict, consumed_aliases: set[str]) -> dict:
    extras = {}
    for key, value in record.items():
        if _normalise_key(key) in consumed_aliases:
            continue
        cleaned = _clean_value(_safe_parse_literal(value))
        if cleaned:
            extras[str(key)] = cleaned
        if len(extras) >= MAX_EXTRA_FIELDS:
            break
    return extras


def _normalize_export_record(record: dict, source_name: str) -> dict | None:
    alias_map = {
        "family_name": [
            "family_name",
            "family",
            "family name",
            "templateName",
            "product family",
            "name",
        ],
        "type_name": ["type_name", "type", "type name", "subcategory"],
        "family_and_type": ["family and type", "family_and_type"],
        "category": ["category", "family category", "product category", "cadType"],
        "manufacturer": ["manufacturer", "manufacturer name", "brand", "vendor"],
        "model": ["model", "model number", "catalog number"],
        "part_number": ["part_number", "part number", "item number", "stratus item number"],
        "description": [
            "description",
            "evolve_description",
            "technical description",
            "summary",
            "propertiesToInclude",
        ],
        "material": ["material", "material main", "body material"],
        "finish": ["finish", "coating"],
        "size": ["size", "trade size", "nominal diameter"],
        "unit": ["unit", "unitofmeasure", "pricing_unit"],
        "cost": ["cost", "total cost", "replacementcost"],
        "labor_hours": ["labor hours", "installation hours", "time to install"],
        "estimate_id": ["evolve_estimateid", "estimateid", "estimate_id"],
        "source_url": ["url", "source_url", "product url", "source"],
    }

    normalized = {
        "record_type": "revit_family_reference",
        "source_type": "structured_export",
        "source_name": source_name,
    }

    consumed_aliases = set()
    for canonical_key, aliases in alias_map.items():
        value = _lookup_value(record, aliases)
        if value:
            normalized[canonical_key] = value
        consumed_aliases.update(_normalise_key(alias) for alias in aliases)

    if not normalized.get("family_name") and normalized.get("family_and_type"):
        normalized["family_name"] = normalized["family_and_type"]

    if not normalized.get("family_and_type"):
        parts = [normalized.get("family_name"), normalized.get("type_name")]
        joined = " : ".join(part for part in parts if part)
        if joined:
            normalized["family_and_type"] = joined

    if not any(normalized.get(key) for key in ("family_name", "family_and_type", "description")):
        return None

    normalized["lookup_tokens"] = _tokenize(
        normalized.get("category"),
        normalized.get("family_name"),
        normalized.get("type_name"),
        normalized.get("manufacturer"),
        normalized.get("part_number"),
        normalized.get("description"),
    )
    normalized["lookup_key"] = _build_lookup_key(normalized)
    extras = _collect_extra_fields(record, consumed_aliases)
    if extras:
        normalized["source_fields"] = extras
    return _attach_spatial_contract(normalized)


def _scan_family_dir(path: str, include_rvt: bool) -> list[dict]:
    base_path = Path(path)
    if not base_path.exists():
        raise FileNotFoundError(path)

    allowed_extensions = set(SCAN_EXTENSIONS)
    if include_rvt:
        allowed_extensions.update(OPTIONAL_SCAN_EXTENSIONS)

    records = []
    for file_path in sorted(base_path.rglob("*")):
        if not file_path.is_file():
            continue
        if file_path.suffix.lower() not in allowed_extensions:
            continue

        relative_path = file_path.relative_to(base_path)
        category = relative_path.parts[0] if len(relative_path.parts) > 1 else None
        family_name = file_path.stem
        records.append(
            _attach_spatial_contract(
                {
                "record_type": "revit_family_reference",
                "source_type": "family_directory_scan",
                "source_name": str(base_path),
                "source_path": str(file_path),
                "relative_source_path": str(relative_path),
                "file_type": file_path.suffix.lower().lstrip("."),
                "category": category,
                "family_name": family_name,
                "family_and_type": family_name,
                "lookup_tokens": _tokenize(category, family_name, file_path.suffix.lower()),
                "lookup_key": _build_lookup_key(
                    {"category": category, "family_name": family_name}
                ),
                }
            )
        )
    return records


def _write_jsonl(records: list[dict], out_path: str) -> None:
    output_path = Path(out_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=True) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize Revit-derived reference data")
    parser.add_argument("--source", action="append", default=[], help="CSV or JSONL export to ingest")
    parser.add_argument(
        "--family-dir",
        action="append",
        default=[],
        help="Directory to recursively scan for .rfa family files",
    )
    parser.add_argument(
        "--include-rvt",
        action="store_true",
        help="Include .rvt model files when scanning family directories",
    )
    parser.add_argument("--out", required=True, help="Output JSONL path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.source and not args.family_dir:
        raise SystemExit("Provide at least one --source or --family-dir input")

    records = []

    for source in args.source:
        loaded_records = _load_source(source)
        normalized_count = 0
        for record in loaded_records:
            normalized = _normalize_export_record(record, source)
            if normalized:
                records.append(normalized)
                normalized_count += 1
        print(f"Loaded {normalized_count} normalized Revit records from {source}")

    for family_dir in args.family_dir:
        scanned_records = _scan_family_dir(family_dir, include_rvt=args.include_rvt)
        records.extend(scanned_records)
        print(f"Scanned {len(scanned_records)} family references from {family_dir}")

    deduped = {}
    for record in records:
        key = record.get("lookup_key") or json.dumps(record, sort_keys=True)
        source_path = record.get("source_path") or record.get("source_name")
        deduped[f"{key}|{source_path}"] = record

    final_records = list(deduped.values())
    _write_jsonl(final_records, args.out)
    print(f"Wrote {len(final_records)} Revit reference records to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())