"""
Convert structured electrical product catalogs into instruction-tuning examples.

This is the right path when you want the model to know real electrical
construction materials, manufacturers, part numbers, and product specifications.
Instead of relying on synthetic topic prompts alone, feed actual catalog exports
from distributors or manufacturers and generate JSONL rows that match the
training pipeline schema.

Supported source formats:
    - JSONL: one product record per line
    - CSV: one product record per row

Minimum useful fields per record:
    manufacturer, product_name

Recommended fields:
    manufacturer, brand, product_name, category, subcategory, part_number,
    description, applications, standards, materials, finish, voltage,
    amperage, dimensions, trade_size, conductor_material, insulation,
    environment_rating, mounting, spec_sheet_url, source_url

Usage:
    python scripts/build_catalog_data.py \
        --source supplier_export.csv \
        --out data/raw/catalog_examples.jsonl

Then merge into the main dataset after review:
    cat data/raw/catalog_examples.jsonl >> data/raw/dataset.jsonl
"""

import argparse
import csv
import json
import os
import sys
from collections import defaultdict


def _clean_value(value):
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = " ".join(value.strip().split())
        return cleaned or None
    if isinstance(value, (int, float, bool)):
        return str(value)
    if isinstance(value, list):
        parts = [_clean_value(item) for item in value]
        return ", ".join(part for part in parts if part)
    if isinstance(value, dict):
        parts = []
        for key, item in value.items():
            cleaned = _clean_value(item)
            if cleaned:
                parts.append(f"{key}: {cleaned}")
        return "; ".join(parts) or None
    return str(value)


def _load_source(path: str) -> list[dict]:
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    _, ext = os.path.splitext(path.lower())
    if ext == ".jsonl":
        records = []
        with open(path, "r", encoding="utf-8") as handle:
            for line_number, raw_line in enumerate(handle, start=1):
                stripped = raw_line.strip()
                if not stripped:
                    continue
                try:
                    record = json.loads(stripped)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid JSON on line {line_number}: {exc}") from exc
                if not isinstance(record, dict):
                    raise ValueError(f"Line {line_number} must contain a JSON object")
                records.append(record)
        return records

    if ext == ".csv":
        with open(path, "r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            return list(reader)

    raise ValueError(f"Unsupported source format: {ext}. Use .csv or .jsonl")


def _normalize_record(record: dict) -> dict:
    aliases = {
        "manufacturer": ["manufacturer", "mfr", "maker", "vendor"],
        "brand": ["brand", "series_brand"],
        "product_name": ["product_name", "name", "title", "product", "item_name"],
        "category": ["category", "product_category", "family"],
        "subcategory": ["subcategory", "product_subcategory", "type"],
        "part_number": ["part_number", "sku", "catalog_number", "model", "mpn"],
        "description": ["description", "summary", "details"],
        "applications": ["applications", "application", "uses", "recommended_use"],
        "standards": ["standards", "certifications", "listings", "compliance"],
        "materials": ["materials", "material", "construction"],
        "finish": ["finish", "coating"],
        "voltage": ["voltage", "voltage_rating"],
        "amperage": ["amperage", "amps", "current_rating"],
        "dimensions": ["dimensions", "size", "measurements"],
        "trade_size": ["trade_size", "trade_sizes", "conduit_size"],
        "conductor_material": ["conductor_material", "wire_material", "conductor"],
        "insulation": ["insulation", "insulation_type"],
        "unit_price": ["unit_price", "price", "cost", "list_price", "net_price"],
        "pricing_unit": ["pricing_unit", "uom", "unit_of_measure", "sell_unit"],
        "environment_rating": ["environment_rating", "environment", "nema_rating", "ip_rating"],
        "mounting": ["mounting", "mount", "mounting_type"],
        "spec_sheet_url": ["spec_sheet_url", "datasheet", "spec_url"],
        "source_url": ["source_url", "url", "product_url", "source"],
    }

    normalized = {}
    lowered = {str(key).strip().lower(): value for key, value in record.items()}
    for canonical_key, candidates in aliases.items():
        for candidate in candidates:
            if candidate in lowered:
                cleaned = _clean_value(lowered[candidate])
                if cleaned:
                    normalized[canonical_key] = cleaned
                    break
    return normalized


def _spec_pairs(record: dict) -> list[tuple[str, str]]:
    ordered_fields = [
        ("category", "Category"),
        ("subcategory", "Subcategory"),
        ("materials", "Material"),
        ("finish", "Finish"),
        ("voltage", "Voltage rating"),
        ("amperage", "Current rating"),
        ("trade_size", "Trade size"),
        ("dimensions", "Dimensions"),
        ("conductor_material", "Conductor material"),
        ("insulation", "Insulation"),
        ("unit_price", "Unit price"),
        ("pricing_unit", "Pricing unit"),
        ("environment_rating", "Environment rating"),
        ("mounting", "Mounting"),
        ("standards", "Standards / listings"),
    ]
    pairs = []
    for key, label in ordered_fields:
        value = record.get(key)
        if value:
            pairs.append((label, value))
    return pairs


def _render_spec_summary(record: dict) -> str:
    lines = []
    for label, value in _spec_pairs(record):
        lines.append(f"- {label}: {value}")
    return "\n".join(lines)


def _render_record_summary(record: dict) -> str:
    headline = []
    if record.get("manufacturer"):
        headline.append(record["manufacturer"])
    if record.get("product_name"):
        headline.append(record["product_name"])
    title = " — ".join(headline)

    paragraphs = []
    if title:
        paragraphs.append(title)
    if record.get("part_number"):
        paragraphs.append(f"Part number: {record['part_number']}")
    if record.get("description"):
        paragraphs.append(record["description"])
    if record.get("applications"):
        paragraphs.append(f"Typical applications: {record['applications']}")
    spec_summary = _render_spec_summary(record)
    if spec_summary:
        paragraphs.append("Key specifications:\n" + spec_summary)
    if record.get("spec_sheet_url"):
        paragraphs.append(f"Spec sheet: {record['spec_sheet_url']}")
    if record.get("source_url"):
        paragraphs.append(f"Source: {record['source_url']}")
    return "\n\n".join(paragraphs)


def _render_reference_summary(record: dict) -> str:
    paragraphs = []
    source_name = record.get("source_name") or record.get("manufacturer")
    page_title = record.get("page_title") or record.get("product_name")
    if source_name and page_title:
        paragraphs.append(f"Source: {source_name} — {page_title}")
    elif page_title:
        paragraphs.append(page_title)
    elif source_name:
        paragraphs.append(f"Source: {source_name}")

    if record.get("summary"):
        paragraphs.append(record["summary"])

    key_points = record.get("key_points")
    if isinstance(key_points, str):
        key_points = [point.strip() for point in key_points.split("|") if point.strip()]
    if key_points:
        paragraphs.append("Key points:\n" + "\n".join(f"- {point}" for point in key_points[:8]))

    reference_links = record.get("reference_links")
    if reference_links:
        link_titles = []
        for item in reference_links[:8]:
            if isinstance(item, dict) and item.get("title"):
                link_titles.append(item["title"])
        if link_titles:
            paragraphs.append("Linked references:\n" + "\n".join(f"- {title}" for title in link_titles))

    if record.get("source_url"):
        paragraphs.append(f"Source: {record['source_url']}")

    return "\n\n".join(paragraphs)


def _build_product_examples(record: dict) -> list[dict]:
    manufacturer = record.get("manufacturer")
    product_name = record.get("product_name")
    part_number = record.get("part_number")
    category = record.get("category")

    if not manufacturer or not product_name:
        return []

    product_label = product_name
    if part_number:
        product_label = f"{product_name} ({part_number})"

    summary = _render_record_summary(record)
    examples = [
        {
            "instruction": f"Summarize the electrical construction product {product_label} from {manufacturer}.",
            "response": summary,
        },
        {
            "instruction": f"What should a contractor know about {product_label} from {manufacturer} before submittal or installation?",
            "response": summary,
        },
    ]

    spec_summary = _render_spec_summary(record)
    if spec_summary:
        examples.append(
            {
                "instruction": f"List the key specifications for {product_label} by {manufacturer}.",
                "response": spec_summary,
            }
        )

    if record.get("applications"):
        examples.append(
            {
                "instruction": f"Where is {product_label} by {manufacturer} typically used in electrical construction?",
                "response": record["applications"],
            }
        )

    if record.get("unit_price"):
        pricing_response = f"Unit price: {record['unit_price']}"
        if record.get("pricing_unit"):
            pricing_response += f" per {record['pricing_unit']}"
        examples.append(
            {
                "instruction": f"What pricing data is available for {product_label} from {manufacturer}?",
                "response": pricing_response,
            }
        )

    if category:
        examples.append(
            {
                "instruction": f"Which manufacturer makes the {category.lower()} product named {product_name}?",
                "response": f"{manufacturer} manufactures {product_name}."
                + (f" The catalog or part number is {part_number}." if part_number else ""),
            }
        )

    deduped = []
    seen = set()
    for example in examples:
        key = (example["instruction"], example["response"])
        if key not in seen:
            seen.add(key)
            deduped.append(example)
    return deduped


def _build_manufacturer_examples(records: list[dict]) -> list[dict]:
    grouped = defaultdict(list)
    for record in records:
        manufacturer = record.get("manufacturer")
        if manufacturer:
            grouped[manufacturer].append(record)

    examples = []
    for manufacturer, items in grouped.items():
        categories = sorted({item.get("category") for item in items if item.get("category")})
        product_names = [item.get("product_name") for item in items if item.get("product_name")]
        part_numbers = [item.get("part_number") for item in items if item.get("part_number")]
        response_lines = [f"Manufacturer: {manufacturer}"]
        if categories:
            response_lines.append("Product categories: " + ", ".join(categories))
        if product_names:
            response_lines.append("Representative products: " + ", ".join(product_names[:12]))
        if part_numbers:
            response_lines.append("Representative part numbers: " + ", ".join(part_numbers[:12]))

        examples.append(
            {
                "instruction": f"What electrical construction materials or product lines are represented by {manufacturer}?",
                "response": "\n".join(response_lines),
            }
        )
    return examples


def _build_reference_examples(record: dict) -> list[dict]:
    source_name = record.get("source_name") or record.get("manufacturer")
    page_title = record.get("page_title") or record.get("product_name")
    summary = _render_reference_summary(record)
    if not source_name and not page_title:
        return []

    label = page_title or source_name
    examples = [
        {
            "instruction": f"Summarize the electrical construction reference source {label}.",
            "response": summary,
        }
    ]

    if source_name:
        examples.append(
            {
                "instruction": f"What estimating or industry reference information is available from {source_name}?",
                "response": summary,
            }
        )

    if page_title and source_name:
        examples.append(
            {
                "instruction": f"What should an electrical contractor know from {source_name} page {page_title}?",
                "response": summary,
            }
        )

    deduped = []
    seen = set()
    for example in examples:
        key = (example["instruction"], example["response"])
        if key not in seen:
            seen.add(key)
            deduped.append(example)
    return deduped


def _build_labor_rate_examples(record: dict) -> list[dict]:
    source_name = record.get("source_name")
    page_title = record.get("page_title")
    detail_lines = []
    for key, value in record.items():
        if key in {"kind", "source_name", "page_title", "source_url"}:
            continue
        cleaned = _clean_value(value)
        if cleaned:
            detail_lines.append(f"- {key.replace('_', ' ').title()}: {cleaned}")

    if not detail_lines:
        return []

    response_parts = []
    if source_name:
        response_parts.append(f"Source: {source_name}")
    if page_title:
        response_parts.append(f"Page: {page_title}")
    response_parts.append("Rate details:\n" + "\n".join(detail_lines))
    if record.get("source_url"):
        response_parts.append(f"Source: {record['source_url']}")
    response = "\n\n".join(response_parts)

    label = page_title or source_name or "public labor rate page"
    return [
        {
            "instruction": f"What labor rate information is listed on {label}?",
            "response": response,
        }
    ]


def build_examples(records: list[dict]) -> list[dict]:
    normalized_records = []
    reference_records = []
    code_reference_records = []
    labor_rate_records = []
    for record in records:
        kind = _clean_value(record.get("kind"))
        if kind in {"reference", "labor_reference", "industry_reference"}:
            reference_records.append(record)
            continue
        if kind == "code_reference":
            code_reference_records.append(record)
            continue
        if kind == "labor_rate":
            labor_rate_records.append(record)
            continue

        normalized = _normalize_record(record)
        has_supporting_detail = any(
            normalized.get(field)
            for field in (
                "description",
                "applications",
                "standards",
                "materials",
                "category",
                "subcategory",
                "trade_size",
                "dimensions",
                "voltage",
                "amperage",
                "spec_sheet_url",
            )
        )
        if normalized.get("manufacturer") and normalized.get("product_name") and has_supporting_detail:
            normalized_records.append(normalized)

    examples = []
    for record in normalized_records:
        examples.extend(_build_product_examples(record))
    examples.extend(_build_manufacturer_examples(normalized_records))
    for record in reference_records:
        examples.extend(_build_reference_examples(record))
    for record in code_reference_records:
        examples.extend(_build_reference_examples(record))
    for record in labor_rate_records:
        examples.extend(_build_labor_rate_examples(record))
    return examples


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build instruction-tuning examples from electrical product catalog exports."
    )
    parser.add_argument("--source", required=True, help="Source catalog file (.csv or .jsonl)")
    parser.add_argument("--out", required=True, help="Output JSONL path")
    args = parser.parse_args()

    try:
        source_records = _load_source(args.source)
    except Exception as exc:
        print(f"❌  Could not load source data: {exc}")
        sys.exit(1)

    examples = build_examples(source_records)
    if not examples:
        print(
            "❌  No usable examples were generated. Ensure each source row contains at least "
            "manufacturer and product_name-compatible columns."
        )
        sys.exit(1)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as handle:
        for example in examples:
            handle.write(json.dumps(example, ensure_ascii=False) + "\n")

    print(f"✅  Wrote {len(examples)} training examples to {args.out}")


if __name__ == "__main__":
    main()