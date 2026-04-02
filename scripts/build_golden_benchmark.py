"""
Build a curated electrician golden benchmark from a benchmark spec.
"""

import argparse
import json
import os

from agent_skill_registry import normalize_agent_skill_names
from config_validation import (
    load_config,
    validate_architecture_config,
    validate_managed_sources_config,
    validate_multimodal_config,
    validate_routing_config,
)
from manifest_utils import current_utc_timestamp, sha256_file, write_json_file
from retrieval_utils import parse_reference_response
from runtime_contracts import ROUTE_DETERMINISTIC_TOOL, ROUTE_TEXT, validate_route_contract


def load_json(path: str) -> object:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _optional_string(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    cleaned = value.strip()
    return cleaned or None


def _optional_string_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [cleaned for item in value if isinstance(item, str) and (cleaned := item.strip())]


def _validated_skill_names_from_spec(cfg: dict, spec: dict, *, index: int) -> list[str]:
    skill_names = spec.get("skill_names")
    if skill_names is None:
        return []
    if not isinstance(skill_names, list):
        raise SystemExit(f"Spec entry {index} skill_names must be a list of strings")

    try:
        return normalize_agent_skill_names(cfg, skill_names)
    except ValueError as exc:
        raise SystemExit(f"Spec entry {index} skill_names are invalid: {exc}") from exc


def _resolve_route_fields(
    spec: dict,
    *,
    index: int,
    default_route: str,
    multimodal_enabled: bool,
) -> tuple[str, str]:
    route_value = _optional_string(spec.get("route")) or default_route
    runtime_owner_value = _optional_string(spec.get("runtime_owner"))
    try:
        return validate_route_contract(
            route_value,
            runtime_owner_value,
            multimodal_enabled=multimodal_enabled,
            route_label=f"spec[{index}].route",
            runtime_owner_label=f"spec[{index}].runtime_owner",
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc


def _direct_tool_row_from_spec(
    cfg: dict,
    spec: dict,
    index: int,
    benchmark_id: str,
    category: str,
    *,
    multimodal_enabled: bool,
) -> dict:
    instruction = _optional_string(spec.get("instruction"))
    tool_name = _optional_string(spec.get("tool_name"))
    if instruction is None or tool_name is None:
        raise SystemExit(
            f"Spec entry {index} must define non-empty instruction and tool_name for deterministic tool rows"
        )

    tool_request = spec.get("tool_request")
    tool_expectation = spec.get("tool_expectation")
    if not isinstance(tool_request, dict) or not tool_request:
        raise SystemExit(f"Spec entry {index} must define a non-empty tool_request mapping")
    if not isinstance(tool_expectation, dict) or not tool_expectation:
        raise SystemExit(f"Spec entry {index} must define a non-empty tool_expectation mapping")

    route, runtime_owner = _resolve_route_fields(
        spec,
        index=index,
        default_route=ROUTE_DETERMINISTIC_TOOL,
        multimodal_enabled=multimodal_enabled,
    )
    skill_names = _validated_skill_names_from_spec(cfg, spec, index=index)

    return {
        "benchmark_id": benchmark_id,
        "category": category,
        "route": route,
        "runtime_owner": runtime_owner,
        "skill_names": skill_names,
        "attachment_paths": _optional_string_list(spec.get("attachment_paths")),
        "tool_name": tool_name,
        "tool_request": tool_request,
        "tool_expectation": tool_expectation,
        "source": _optional_string(spec.get("source")),
        "section": _optional_string(spec.get("section")),
        "instruction": instruction,
        "input": spec.get("input") if isinstance(spec.get("input"), str) else None,
        "response": spec.get("response") or spec.get("output"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a curated golden benchmark from a spec file.")
    parser.add_argument("--config", default="config.yaml", help="Config file used to validate route contracts.")
    parser.add_argument("--source", required=True, help="Source example JSONL file.")
    parser.add_argument("--spec", required=True, help="Benchmark spec JSON file.")
    parser.add_argument("--out", required=True, help="Golden benchmark JSONL output path.")
    parser.add_argument("--manifest", required=True, help="Golden benchmark manifest JSON output path.")
    args = parser.parse_args()

    cfg = load_config(args.config)
    validate_architecture_config(cfg)
    validate_routing_config(cfg)
    validate_managed_sources_config(cfg)
    validate_multimodal_config(cfg)
    architecture = cfg.get("architecture") if isinstance(cfg.get("architecture"), dict) else {}
    multimodal_enabled = bool(architecture.get("multimodal_runtime_enabled", False))

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
        category = _optional_string(spec.get("category"))
        benchmark_id = spec.get("benchmark_id") or f"electrician-{index:03d}"
        if category is None:
            raise SystemExit(f"Spec entry {index} must define a non-empty category")

        tool_name = _optional_string(spec.get("tool_name"))
        if tool_name is not None:
            benchmark_rows.append(
                _direct_tool_row_from_spec(
                    cfg,
                    spec,
                    index,
                    benchmark_id,
                    category,
                    multimodal_enabled=multimodal_enabled,
                )
            )
            continue

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

        route, runtime_owner = _resolve_route_fields(
            spec,
            index=index,
            default_route=ROUTE_TEXT,
            multimodal_enabled=multimodal_enabled,
        )
        skill_names = _validated_skill_names_from_spec(cfg, spec, index=index)

        benchmark_rows.append({
            "benchmark_id": benchmark_id,
            "category": category,
            "route": route,
            "runtime_owner": runtime_owner,
            "skill_names": skill_names,
            "attachment_paths": _optional_string_list(spec.get("attachment_paths")),
            "tool_name": None,
            "tool_request": None,
            "tool_expectation": None,
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
    route_counts: dict[str, int] = {}
    for row in benchmark_rows:
        category_counts[row["category"]] = category_counts.get(row["category"], 0) + 1
        route_name = row.get("route") or "text"
        route_counts[route_name] = route_counts.get(route_name, 0) + 1

    manifest = {
        "schema_version": 2,
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
        "routes": route_counts,
        "benchmark_ids": [row["benchmark_id"] for row in benchmark_rows],
    }
    write_json_file(args.manifest, manifest)

    print(f"Built golden benchmark with {len(benchmark_rows)} rows → {args.out}")
    print(f"Manifest written to {args.manifest}")


if __name__ == "__main__":
    main()