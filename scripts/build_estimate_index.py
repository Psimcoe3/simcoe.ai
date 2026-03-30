"""
Build a lookup-ready estimate index from RSMeans or crosswalk exports.

The goal is to keep volatile price and labor data outside model weights. This
script turns RSMeans-style CSV or JSONL records into JSONL lookup records keyed
by normalized family, category, manufacturer, and description tokens.

Examples:
    python scripts/build_estimate_index.py \
        --mapping /mnt/c/Users/Paul/RSmeans/stratus_rsmeans_map_FULL.csv \
    --rsmeans-har-dir /mnt/c/Users/Paul/RSmeans \
        --out data/raw/estimate_index.jsonl
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import urlparse

from data_contracts import build_data_contract, stable_identifier


ESTIMATE_FIELDS = (
    "description",
    "unit",
    "crew",
    "daily_output",
    "labor_hours",
    "bare_materials",
    "bare_labor",
    "bare_equipment",
    "bare_total",
    "installed_total",
    "hourly_operational_cost",
    "rent_per_day",
    "rent_per_week",
    "rent_per_month",
)


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
    return str(value)


def _normalise_key(key: str) -> str:
    return "".join(ch.lower() for ch in str(key).strip() if ch.isalnum())


def _lookup_value(record: dict, aliases: list[str]):
    normalised = {_normalise_key(key): value for key, value in record.items()}
    for alias in aliases:
        value = normalised.get(_normalise_key(alias))
        cleaned = _clean_value(value)
        if cleaned:
            return cleaned
    return None


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


def _iter_rsmeans_har_rows(input_dir: str):
    base_path = Path(input_dir)
    if not base_path.exists():
        raise FileNotFoundError(input_dir)

    row_number = 0
    for path in sorted(base_path.rglob("*.har")):
        with path.open("r", encoding="utf-8") as handle:
            har = json.load(handle)
        for entry in har.get("log", {}).get("entries", []):
            request = entry.get("request", {})
            response = entry.get("response", {})
            if "rsmeansonline" not in urlparse(request.get("url", "")).netloc:
                continue
            text = response.get("content", {}).get("text", "")
            if not text:
                continue
            try:
                payload = json.loads(text)
            except json.JSONDecodeError:
                continue
            objects = [payload] if isinstance(payload, dict) else [item for item in payload if isinstance(item, dict)]
            for obj in objects:
                for row in obj.get("rows", []):
                    cells = row.get("cell")
                    if isinstance(cells, list):
                        row_number += 1
                        yield str(path), row_number, cells


def _parse_number(value: str | None):
    if value is None:
        return None
    cleaned = value.replace(",", "").replace("$", "").replace("%", "").strip()
    if not cleaned:
        return None
    try:
        return float(cleaned)
    except ValueError:
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


def _normalise_description(value: str | None) -> str | None:
    cleaned = _clean_value(value)
    if not cleaned:
        return None

    normalized = []
    for char in cleaned.lower():
        normalized.append(char if char.isalnum() else " ")
    return " ".join("".join(normalized).split()) or None


def _build_lookup_key(record: dict) -> str:
    parts = []
    for key in ("category", "family_name", "manufacturer", "part_number", "description"):
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


def _attach_estimate_contract(record: dict) -> dict:
    record["record_id"] = stable_identifier(
        "estimate_lookup",
        record.get("lookup_key") or record.get("description"),
        record.get("source_name"),
        record.get("source_row"),
    )
    record["data_contract"] = build_data_contract(
        data_family="estimate_lookup_records",
        runtime_owner="geometry_rules",
        routing_hint="deterministic_tool_input",
    )
    return record


def _normalize_mapping_record(record: dict, source_name: str, row_number: int) -> dict | None:
    family_name = _lookup_value(
        record,
        [
            "family_name",
            "family",
            "family name",
            "templateName",
            "eVolve_Description",
            "STRATUS_Part_BOMDescription",
        ],
    )
    category = _lookup_value(record, ["category", "family category", "cadType", "Category"])
    manufacturer = _lookup_value(record, ["manufacturer", "Manufacturer", "brand"])
    part_number = _lookup_value(
        record,
        ["part_number", "Catalog Number", "Model", "STRATUS_Part_BOMProductCode"],
    )
    description = _lookup_value(
        record,
        [
            "RSMeans__MatchedDescription",
            "RSMeans__Description",
            "description",
            "Description",
            "Product Description",
        ],
    )
    unit = _lookup_value(record, ["RSMeans__Unit", "Unit", "unit"])
    crew = _lookup_value(record, ["RSMeans__Crew", "Crew"])

    labor_hours = _parse_number(_lookup_value(record, ["RSMeans__LaborHours", "LaborHours"]))
    bare_materials = _parse_number(_lookup_value(record, ["RSMeans__BareMaterials", "BareMaterials"]))
    bare_labor = _parse_number(_lookup_value(record, ["RSMeans__BareLabor", "BareLabor"]))
    bare_equipment = _parse_number(
        _lookup_value(record, ["RSMeans__BareEquipment", "BareEquipment"])
    )
    bare_total = _parse_number(_lookup_value(record, ["RSMeans__BareTotal", "BareTotal"]))
    total_op = _parse_number(_lookup_value(record, ["RSMeans__TotalOP", "TotalOP"]))
    daily_output = _parse_number(_lookup_value(record, ["RSMeans__DailyOutput", "DailyOutput"]))

    has_estimate_values = any(
        value is not None
        for value in (labor_hours, bare_materials, bare_labor, bare_equipment, bare_total, total_op)
    )
    if not has_estimate_values and not description:
        return None

    normalized = {
        "record_type": "estimate_lookup",
        "source_name": source_name,
        "source_row": row_number,
        "family_name": family_name,
        "category": category,
        "manufacturer": manufacturer,
        "part_number": part_number,
        "description": description,
        "unit": unit,
        "crew": crew,
        "daily_output": daily_output,
        "labor_hours": labor_hours,
        "bare_materials": bare_materials,
        "bare_labor": bare_labor,
        "bare_equipment": bare_equipment,
        "bare_total": bare_total,
        "installed_total": total_op,
        "lookup_tokens": _tokenize(category, family_name, manufacturer, part_number, description),
    }
    normalized["lookup_key"] = _build_lookup_key(normalized)
    return _attach_estimate_contract(normalized)


def _estimate_record_score(record: dict) -> int:
    return sum(record.get(field) is not None for field in ESTIMATE_FIELDS)


def _index_estimates_by_description(records: list[dict]) -> dict[str, dict]:
    indexed = {}
    for record in records:
        key = _normalise_description(record.get("description"))
        if not key:
            continue
        existing = indexed.get(key)
        if existing is None or _estimate_record_score(record) > _estimate_record_score(existing):
            indexed[key] = record
    return indexed


def _enrich_mapping_records(mapping_records: list[dict], estimate_records: list[dict]) -> tuple[list[dict], int]:
    estimates_by_description = _index_estimates_by_description(estimate_records)
    enriched_records = []
    enriched_count = 0

    for record in mapping_records:
        description_key = _normalise_description(record.get("description"))
        matched_estimate = estimates_by_description.get(description_key)
        if matched_estimate is None:
            enriched_records.append(record)
            continue

        enriched = dict(record)
        for field in ESTIMATE_FIELDS:
            enriched[field] = matched_estimate.get(field)
        enriched["estimate_source_name"] = matched_estimate.get("source_name")
        enriched["estimate_source_row"] = matched_estimate.get("source_row")
        enriched["estimate_merge_strategy"] = "description_exact_normalized"
        enriched["lookup_tokens"] = _tokenize(
            enriched.get("category"),
            enriched.get("family_name"),
            enriched.get("manufacturer"),
            enriched.get("part_number"),
            enriched.get("description"),
        )
        enriched["lookup_key"] = _build_lookup_key(enriched)
        enriched_records.append(enriched)
        enriched_count += 1

    return enriched_records, enriched_count


def _normalize_rsmeans_record(record: dict, source_name: str, row_number: int) -> dict | None:
    description = _lookup_value(record, ["Description", "description"])
    if not description:
        return None

    unit = _lookup_value(record, ["Unit", "unit"])
    crew = _lookup_value(record, ["Crew", "crew"])
    daily_output = _parse_number(_lookup_value(record, ["DailyOutput", "daily_output"]))
    labor_hours = _parse_number(_lookup_value(record, ["LaborHours", "labor_hours"]))
    bare_materials = _parse_number(_lookup_value(record, ["BareMaterials", "bare_materials"]))
    bare_labor = _parse_number(_lookup_value(record, ["BareLabor", "bare_labor"]))
    bare_equipment = _parse_number(_lookup_value(record, ["BareEquipment", "bare_equipment"]))
    bare_total = _parse_number(_lookup_value(record, ["BareTotal", "bare_total"]))
    total_op = _parse_number(_lookup_value(record, ["TotalOP", "total_op"]))

    normalized = {
        "record_type": "estimate_lookup",
        "source_name": source_name,
        "source_row": row_number,
        "description": description,
        "unit": unit,
        "crew": crew,
        "daily_output": daily_output,
        "labor_hours": labor_hours,
        "bare_materials": bare_materials,
        "bare_labor": bare_labor,
        "bare_equipment": bare_equipment,
        "bare_total": bare_total,
        "installed_total": total_op,
        "lookup_tokens": _tokenize(description, unit, crew),
    }
    normalized["lookup_key"] = _build_lookup_key(normalized)
    return _attach_estimate_contract(normalized)


def _normalize_rsmeans_har_row(cells: list, source_name: str, row_number: int) -> dict | None:
    def cell(index: int):
        if index >= len(cells):
            return None
        return cells[index]

    description = _clean_value(cell(7))
    if not description:
        return None

    unit = _clean_value(cell(8))
    crew = _clean_value(cell(9))
    daily_output = _parse_number(_clean_value(cell(10)))
    labor_hours = _parse_number(_clean_value(cell(12)))
    bare_materials = _parse_number(_clean_value(cell(14)))
    bare_total = _parse_number(_clean_value(cell(21)))
    bare_equipment = _parse_number(_clean_value(cell(29)))
    bare_labor = _parse_number(_clean_value(cell(30)))
    hourly_operational_cost = _parse_number(_clean_value(cell(33)))
    rent_per_day = _parse_number(_clean_value(cell(34)))
    rent_per_week = _parse_number(_clean_value(cell(35)))
    rent_per_month = _parse_number(_clean_value(cell(36)))

    normalized = {
        "record_type": "estimate_lookup",
        "source_name": source_name,
        "source_row": row_number,
        "description": description,
        "unit": unit,
        "crew": crew,
        "daily_output": daily_output,
        "labor_hours": labor_hours,
        "bare_materials": bare_materials,
        "bare_labor": bare_labor,
        "bare_equipment": bare_equipment,
        "bare_total": bare_total,
        "installed_total": None,
        "hourly_operational_cost": hourly_operational_cost,
        "rent_per_day": rent_per_day,
        "rent_per_week": rent_per_week,
        "rent_per_month": rent_per_month,
        "lookup_tokens": _tokenize(description, unit, crew),
    }
    normalized["lookup_key"] = _build_lookup_key(normalized)
    return _attach_estimate_contract(normalized)


def _looks_like_code_series(values: list[float | None]) -> bool:
    present = [value for value in values if value is not None]
    if not present:
        return False
    huge = sum(abs(value) >= 1_000_000 for value in present)
    return huge / len(present) >= 0.9


def _validate_rsmeans_csv_records(records: list[dict], source_name: str) -> None:
    sample = records[: min(len(records), 500)]
    materials = [_parse_number(_lookup_value(record, ["BareMaterials", "bare_materials"])) for record in sample]
    totals = [_parse_number(_lookup_value(record, ["BareTotal", "bare_total"])) for record in sample]
    total_op = [_parse_number(_lookup_value(record, ["TotalOP", "total_op"])) for record in sample]

    if _looks_like_code_series(materials) and _looks_like_code_series(totals) and not any(value is not None for value in total_op):
        raise ValueError(
            f"{source_name} looks misparsed: BareMaterials and BareTotal contain identifier-like values rather than costs. "
            "Use --rsmeans-har-dir with the raw HAR files or regenerate the CSV with corrected indices."
        )


def _write_jsonl(records: list[dict], out_path: str) -> None:
    output_path = Path(out_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=True) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build an estimate lookup index")
    parser.add_argument("--mapping", action="append", default=[], help="Crosswalk CSV or JSONL input")
    parser.add_argument("--rsmeans", action="append", default=[], help="RSMeans CSV or JSONL input")
    parser.add_argument(
        "--rsmeans-har-dir",
        action="append",
        default=[],
        help="Directory containing raw RSMeans HAR files to parse directly",
    )
    parser.add_argument("--out", required=True, help="Output JSONL path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.mapping and not args.rsmeans and not args.rsmeans_har_dir:
        raise SystemExit("Provide at least one --mapping, --rsmeans, or --rsmeans-har-dir input")

    mapping_records = []
    rsmeans_records = []
    har_records = []

    for mapping_path in args.mapping:
        loaded_records = _load_source(mapping_path)
        normalized_count = 0
        for row_number, record in enumerate(loaded_records, start=1):
            normalized = _normalize_mapping_record(record, mapping_path, row_number)
            if normalized:
                mapping_records.append(normalized)
                normalized_count += 1
        print(f"Loaded {normalized_count} estimate mapping records from {mapping_path}")

    for rsmeans_path in args.rsmeans:
        loaded_records = _load_source(rsmeans_path)
        _validate_rsmeans_csv_records(loaded_records, rsmeans_path)
        normalized_count = 0
        for row_number, record in enumerate(loaded_records, start=1):
            normalized = _normalize_rsmeans_record(record, rsmeans_path, row_number)
            if normalized:
                rsmeans_records.append(normalized)
                normalized_count += 1
        print(f"Loaded {normalized_count} RSMeans records from {rsmeans_path}")

    for har_dir in args.rsmeans_har_dir:
        normalized_count = 0
        for source_name, row_number, cells in _iter_rsmeans_har_rows(har_dir):
            normalized = _normalize_rsmeans_har_row(cells, source_name, row_number)
            if normalized:
                har_records.append(normalized)
                normalized_count += 1
        print(f"Loaded {normalized_count} RSMeans HAR records from {har_dir}")

    estimate_records = rsmeans_records + har_records
    if mapping_records and estimate_records:
        mapping_records, enriched_count = _enrich_mapping_records(mapping_records, estimate_records)
        print(
            "Enriched "
            f"{enriched_count} mapping records with trusted estimate fields from RSMeans/HAR inputs"
        )

    records = mapping_records + rsmeans_records + har_records

    deduped = {}
    for record in records:
        dedup_key = record.get("lookup_key") or f"{record.get('source_name')}|{record.get('source_row')}"
        existing = deduped.get(dedup_key)
        if existing is None:
            deduped[dedup_key] = record
            continue
        existing_score = sum(value is not None for value in existing.values())
        candidate_score = sum(value is not None for value in record.values())
        if candidate_score > existing_score:
            deduped[dedup_key] = record

    final_records = list(deduped.values())
    _write_jsonl(final_records, args.out)
    print(f"Wrote {len(final_records)} estimate lookup records to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())