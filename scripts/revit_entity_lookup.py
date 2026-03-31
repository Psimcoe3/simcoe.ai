"""
Query Revit/entity grounding records through a deterministic lookup runtime.

Examples:
    python scripts/revit_entity_lookup.py \
        --config config.electrician.yaml \
        --query "Nema 1 Galvanized Screw Cover" \
        --top-k 3

    python scripts/revit_entity_lookup.py \
        --config config.electrician.yaml \
        --record-id revit_family_reference:1234abcd...
"""

from __future__ import annotations

import argparse
import json
import os

from config_validation import load_config, validate_deterministic_tools_config
from deterministic_tool_utils import build_tool_error, build_tool_request, build_tool_response
from manifest_utils import write_json_file
from retrieval_utils import load_jsonl


TOOL_NAME = "revit_entity_lookup"
REVIT_RESULT_FIELDS = (
    "record_type",
    "source_type",
    "source_name",
    "source_path",
    "relative_source_path",
    "file_type",
    "category",
    "subcategory",
    "family_name",
    "type_name",
    "family_and_type",
    "manufacturer",
    "model",
    "part_number",
    "description",
    "material",
    "finish",
    "size",
    "nominal_diameter",
    "overall_length",
    "unit",
    "cost",
    "labor_hours",
    "estimate_id",
    "source_url",
    "source_fields",
)


def _normalize_text(value: object) -> str:
    if value is None:
        return ""
    normalized = []
    for char in str(value).lower():
        normalized.append(char if char.isalnum() else " ")
    return " ".join("".join(normalized).split())


def _tokenize(value: object) -> list[str]:
    tokens: list[str] = []
    for token in _normalize_text(value).split():
        if len(token) >= 2 or token.isdigit():
            tokens.append(token)
    return tokens


def resolve_tool_settings(
    cfg: dict,
    *,
    index_path: str | None = None,
    top_k: int | None = None,
    min_score: float | None = None,
) -> dict:
    validate_deterministic_tools_config(cfg)
    deterministic_tools = (
        cfg.get("deterministic_tools") if isinstance(cfg.get("deterministic_tools"), dict) else {}
    )
    tool_cfg = (
        deterministic_tools.get(TOOL_NAME)
        if isinstance(deterministic_tools.get(TOOL_NAME), dict)
        else {}
    )

    if index_path is None and tool_cfg.get("enabled") is False:
        raise ValueError(
            "deterministic_tools.revit_entity_lookup is disabled in the selected config"
        )

    max_results = int(tool_cfg.get("max_results", 10))
    requested_top_k = top_k if top_k is not None else int(tool_cfg.get("default_top_k", 5))
    return {
        "index_path": index_path
        or tool_cfg.get("index_path")
        or "data/raw/revit_family_index.jsonl",
        "top_k": min(requested_top_k, max_results),
        "max_results": max_results,
        "min_score": float(min_score if min_score is not None else tool_cfg.get("min_score", 2.0)),
    }


def _matches_filter(record: dict, field_name: str, expected: str | None) -> bool:
    if not expected:
        return True
    record_value = _normalize_text(record.get(field_name))
    expected_value = _normalize_text(expected)
    if not expected_value:
        return True
    return expected_value in record_value


def _score_record(query: str, record: dict) -> tuple[float, list[dict]]:
    normalized_query = _normalize_text(query)
    query_tokens = set(_tokenize(query))
    lookup_tokens = {str(token).lower() for token in record.get("lookup_tokens", []) if token}

    score = 0.0
    reasons: list[dict] = []

    overlapping_tokens = sorted(query_tokens & lookup_tokens)
    if overlapping_tokens:
        token_score = float(len(overlapping_tokens) * 3)
        score += token_score
        reasons.append(
            {
                "type": "token_overlap",
                "tokens": overlapping_tokens,
                "weight": token_score,
            }
        )

    weighted_fields = {
        "family_and_type": (16.0, 11.0),
        "family_name": (14.0, 10.0),
        "type_name": (12.0, 9.0),
        "description": (12.0, 8.0),
        "subcategory": (10.0, 7.0),
        "category": (9.0, 6.0),
        "manufacturer": (8.0, 6.0),
        "part_number": (8.0, 6.0),
        "nominal_diameter": (7.0, 5.0),
        "overall_length": (6.0, 4.0),
        "size": (6.0, 4.0),
        "material": (5.0, 3.0),
        "finish": (5.0, 3.0),
    }
    for field_name, (exact_weight, contains_weight) in weighted_fields.items():
        field_value = _normalize_text(record.get(field_name))
        if not field_value:
            continue

        if normalized_query and normalized_query == field_value:
            score += exact_weight
            reasons.append(
                {
                    "type": "exact_field_match",
                    "field": field_name,
                    "weight": exact_weight,
                }
            )
            continue

        if normalized_query and normalized_query in field_value:
            score += contains_weight
            reasons.append(
                {
                    "type": "field_contains_query",
                    "field": field_name,
                    "weight": contains_weight,
                }
            )
            continue

        if field_name != "description" and field_value in normalized_query:
            weight = max(contains_weight - 2.0, 1.0)
            score += weight
            reasons.append(
                {
                    "type": "query_contains_field",
                    "field": field_name,
                    "weight": weight,
                }
            )

    return score, reasons


def _build_result(record: dict, score: float, reasons: list[dict]) -> dict:
    result = {
        "record_id": record.get("record_id"),
        "lookup_key": record.get("lookup_key"),
        "match_score": round(score, 4),
        "match_reasons": reasons,
        "data_contract": record.get("data_contract"),
    }
    for field_name in REVIT_RESULT_FIELDS:
        result[field_name] = record.get(field_name)
    return result


def _lookup_records(
    records: list[dict], request: dict, settings: dict
) -> tuple[list[dict], list[str], dict]:
    warnings: list[str] = []
    filters = request.get("filters") or {}
    filtered_records = [
        record
        for record in records
        if record.get("record_type") == "revit_family_reference"
        and _matches_filter(record, "family_name", filters.get("family_name"))
        and _matches_filter(record, "type_name", filters.get("type_name"))
        and _matches_filter(record, "family_and_type", filters.get("family_and_type"))
        and _matches_filter(record, "category", filters.get("category"))
        and _matches_filter(record, "subcategory", filters.get("subcategory"))
        and _matches_filter(record, "manufacturer", filters.get("manufacturer"))
        and _matches_filter(record, "unit", filters.get("unit"))
        and _matches_filter(record, "source_name", filters.get("source_name"))
    ]

    exact_results: list[dict] = []
    record_id = request.get("record_id")
    lookup_key = request.get("lookup_key")
    if record_id or lookup_key:
        for record in filtered_records:
            if record_id and record.get("record_id") == record_id:
                exact_results.append(
                    _build_result(record, 100.0, [{"type": "record_id_match", "weight": 100.0}])
                )
            elif lookup_key and record.get("lookup_key") == lookup_key:
                exact_results.append(
                    _build_result(record, 95.0, [{"type": "lookup_key_match", "weight": 95.0}])
                )
        if exact_results:
            return (
                exact_results[: request["top_k"]],
                warnings,
                {
                    "candidate_record_count": len(filtered_records),
                    "matched_record_count": len(exact_results),
                },
            )

    query = request.get("query")
    if not query:
        return (
            [],
            warnings,
            {
                "candidate_record_count": len(filtered_records),
                "matched_record_count": 0,
            },
        )

    if not _tokenize(query):
        warnings.append(
            "Query normalized to no lookup tokens; ranking relies on phrase matches only."
        )

    ranked_results: list[tuple[float, dict, list[dict]]] = []
    for record in filtered_records:
        score, reasons = _score_record(query, record)
        if score < settings["min_score"]:
            continue
        ranked_results.append((score, record, reasons))

    ranked_results.sort(
        key=lambda item: (-item[0], item[1].get("record_id") or item[1].get("lookup_key") or ""),
    )
    results = [
        _build_result(record, score, reasons)
        for score, record, reasons in ranked_results[: request["top_k"]]
    ]

    if not results:
        warnings.append("No Revit entity records matched the supplied query and filters.")

    return (
        results,
        warnings,
        {
            "candidate_record_count": len(filtered_records),
            "matched_record_count": len(ranked_results),
        },
    )


def run_revit_entity_lookup_request(
    cfg: dict,
    request: dict,
    *,
    index_path: str | None = None,
    min_score: float | None = None,
) -> dict:
    settings = resolve_tool_settings(
        cfg,
        index_path=index_path,
        top_k=request.get("top_k"),
        min_score=min_score,
    )

    normalized_request = dict(request)
    normalized_request["filters"] = (
        request.get("filters") if isinstance(request.get("filters"), dict) else {}
    )
    normalized_request["top_k"] = settings["top_k"]

    records = load_jsonl(settings["index_path"])
    results, warnings, provenance = _lookup_records(records, normalized_request, settings)
    return build_tool_response(
        TOOL_NAME,
        request=normalized_request,
        results=results,
        index_path=settings["index_path"],
        warnings=warnings,
        provenance={
            "record_count": len(records),
            **provenance,
        },
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Query deterministic Revit/entity lookup records.")
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--index", default=None, help="Override the Revit index path.")
    parser.add_argument("--query", default=None, help="Natural-language Revit/entity lookup query.")
    parser.add_argument("--record-id", default=None, help="Exact record_id lookup.")
    parser.add_argument("--lookup-key", default=None, help="Exact lookup_key lookup.")
    parser.add_argument("--family-name", default=None)
    parser.add_argument("--type-name", default=None)
    parser.add_argument("--family-and-type", default=None)
    parser.add_argument("--category", default=None)
    parser.add_argument("--subcategory", default=None)
    parser.add_argument("--manufacturer", default=None)
    parser.add_argument("--unit", default=None)
    parser.add_argument("--source-name", default=None)
    parser.add_argument("--top-k", type=int, default=None)
    parser.add_argument("--min-score", type=float, default=None)
    parser.add_argument("--out", default=None, help="Write the JSON response to this path.")
    args = parser.parse_args()

    if not args.query and not args.record_id and not args.lookup_key:
        parser.error("provide at least one of --query, --record-id, or --lookup-key")
    if args.top_k is not None and args.top_k <= 0:
        parser.error("--top-k must be greater than zero")
    if args.min_score is not None and args.min_score < 0:
        parser.error("--min-score must be zero or greater")
    return args


def main() -> None:
    args = parse_args()
    cfg = load_config(args.config)
    filters = {
        "family_name": args.family_name,
        "type_name": args.type_name,
        "family_and_type": args.family_and_type,
        "category": args.category,
        "subcategory": args.subcategory,
        "manufacturer": args.manufacturer,
        "unit": args.unit,
        "source_name": args.source_name,
    }
    request = build_tool_request(
        TOOL_NAME,
        query=args.query,
        record_id=args.record_id,
        lookup_key=args.lookup_key,
        filters=filters,
        top_k=args.top_k,
    )

    try:
        response = run_revit_entity_lookup_request(
            cfg,
            request,
            index_path=args.index,
            min_score=args.min_score,
        )
    except Exception as exc:
        response = build_tool_error(
            TOOL_NAME,
            request=request,
            message=str(exc),
            code="revit_entity_lookup_failed",
        )
        if args.out:
            write_json_file(args.out, response)
        else:
            print(json.dumps(response, indent=2, sort_keys=True))
        raise SystemExit(1) from exc

    if args.out:
        write_json_file(args.out, response)
        print(f"Wrote Revit lookup response to {os.path.abspath(args.out)}")
        return

    print(json.dumps(response, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
