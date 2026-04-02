"""
Shared first-party tool registry for the local simcoe.ai agent shell.
"""

from __future__ import annotations

import copy

from deterministic_tool_utils import build_tool_error, build_tool_request
from estimate_lookup import TOOL_NAME as ESTIMATE_LOOKUP_TOOL_NAME, run_estimate_lookup_request
from hook_runtime import apply_hook_stage
from revit_entity_lookup import (
    TOOL_NAME as REVIT_ENTITY_LOOKUP_TOOL_NAME,
    run_revit_entity_lookup_request,
)
from runtime_contracts import (
    EXECUTION_STATUS_DENIED,
    EXECUTION_STATUS_FAILED,
    EXECUTION_STATUS_SUCCEEDED,
    EXECUTION_SUBJECT_DETERMINISTIC_TOOL,
    HOOK_STAGE_POST_DETERMINISTIC_TOOL,
    HOOK_STAGE_PRE_DETERMINISTIC_TOOL,
    ROUTE_DETERMINISTIC_TOOL,
    build_execution_envelope,
)


TOOL_REGISTRY_SCHEMA_VERSION = 1
TOOL_KIND_DETERMINISTIC = "deterministic_tool"
TOOL_ACCESS_READ_ONLY = "read_only"
TOOL_EXECUTION_SERIAL = "serial"

DEFAULT_AGENT_TOOL_NAME = ESTIMATE_LOOKUP_TOOL_NAME

_TOOL_SPECS = {
    ESTIMATE_LOOKUP_TOOL_NAME: {
        "name": ESTIMATE_LOOKUP_TOOL_NAME,
        "display_name": "Estimate Lookup",
        "description": (
            "Query the deterministic estimate index for grounded installed-cost, "
            "labor, and material records."
        ),
        "kind": TOOL_KIND_DETERMINISTIC,
        "route": ROUTE_DETERMINISTIC_TOOL,
        "runtime_owner": "geometry_rules",
        "access_mode": TOOL_ACCESS_READ_ONLY,
        "execution_mode": TOOL_EXECUTION_SERIAL,
        "aliases": ["estimate", "estimate-lookup"],
        "routing_markers": [],
        "config_section": "deterministic_tools.estimate_lookup",
        "defaults": {
            "index_path": "data/raw/estimate_index.jsonl",
            "default_top_k": 5,
            "max_results": 10,
            "min_score": 2.0,
            "default_quantity": 1.0,
        },
        "execute_fn": run_estimate_lookup_request,
    },
    REVIT_ENTITY_LOOKUP_TOOL_NAME: {
        "name": REVIT_ENTITY_LOOKUP_TOOL_NAME,
        "display_name": "Revit Entity Lookup",
        "description": (
            "Query grounded Revit family/type reference records for entity, family, "
            "type, and catalog metadata."
        ),
        "kind": TOOL_KIND_DETERMINISTIC,
        "route": ROUTE_DETERMINISTIC_TOOL,
        "runtime_owner": "geometry_rules",
        "access_mode": TOOL_ACCESS_READ_ONLY,
        "execution_mode": TOOL_EXECUTION_SERIAL,
        "aliases": ["revit", "revit-lookup", "entity", "entity-lookup"],
        "routing_markers": ["revit", "family type", "family and type", "subcategory"],
        "config_section": "deterministic_tools.revit_entity_lookup",
        "defaults": {
            "index_path": "data/raw/revit_family_index.jsonl",
            "default_top_k": 5,
            "max_results": 10,
            "min_score": 2.0,
        },
        "execute_fn": run_revit_entity_lookup_request,
    },
}


def _normalize_tool_token(value: str) -> str:
    return value.strip().replace("-", "_").lower()


def _tool_config(cfg: dict, tool_name: str) -> dict:
    deterministic_tools = (
        cfg.get("deterministic_tools") if isinstance(cfg.get("deterministic_tools"), dict) else {}
    )
    tool_cfg = deterministic_tools.get(tool_name)
    return tool_cfg if isinstance(tool_cfg, dict) else {}


def normalize_agent_tool_name(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("tool name must be a non-empty string")

    cleaned = _normalize_tool_token(value)
    for tool_name, spec in _TOOL_SPECS.items():
        if cleaned == tool_name:
            return tool_name
        aliases = spec.get("aliases") if isinstance(spec.get("aliases"), list) else []
        if cleaned in {_normalize_tool_token(alias) for alias in aliases}:
            return tool_name

    choices = ", ".join(sorted(_TOOL_SPECS))
    raise ValueError(f"unknown tool '{value}'. Available tools: {choices}")


def _resolved_tool_settings(cfg: dict, tool_name: str) -> tuple[bool, dict]:
    spec = _TOOL_SPECS[tool_name]
    tool_cfg = _tool_config(cfg, tool_name)
    enabled = tool_cfg.get("enabled") is not False

    resolved = {}
    for key, default in spec["defaults"].items():
        value = tool_cfg.get(key, default)
        if isinstance(default, bool):
            resolved[key] = bool(value)
        elif isinstance(default, int):
            resolved[key] = int(value)
        elif isinstance(default, float):
            resolved[key] = float(value)
        else:
            resolved[key] = str(value)
    return enabled, resolved


def describe_agent_tool(cfg: dict, tool_name: str) -> dict:
    canonical_name = normalize_agent_tool_name(tool_name)
    spec = _TOOL_SPECS[canonical_name]
    enabled, resolved_settings = _resolved_tool_settings(cfg, canonical_name)

    return {
        "schema_version": TOOL_REGISTRY_SCHEMA_VERSION,
        "name": canonical_name,
        "display_name": spec["display_name"],
        "description": spec["description"],
        "kind": spec["kind"],
        "route": spec["route"],
        "runtime_owner": spec["runtime_owner"],
        "access_mode": spec["access_mode"],
        "execution_mode": spec["execution_mode"],
        "config_section": spec["config_section"],
        "aliases": copy.deepcopy(spec["aliases"]),
        "routing_markers": copy.deepcopy(spec["routing_markers"]),
        "enabled": enabled,
        "resolved_settings": resolved_settings,
    }


def list_agent_tools(cfg: dict, *, include_disabled: bool = True) -> list[dict]:
    tools = [describe_agent_tool(cfg, tool_name) for tool_name in sorted(_TOOL_SPECS)]
    if include_disabled:
        return tools
    return [tool for tool in tools if tool["enabled"]]


def infer_agent_tool_name(prompt: str, explicit_tool_name: str | None = None) -> str:
    if explicit_tool_name is not None:
        return normalize_agent_tool_name(explicit_tool_name)

    normalized_prompt = prompt.lower()
    best_name = DEFAULT_AGENT_TOOL_NAME
    best_score = 0
    for tool_name, spec in _TOOL_SPECS.items():
        markers = spec.get("routing_markers") if isinstance(spec.get("routing_markers"), list) else []
        score = sum(1 for marker in markers if marker in normalized_prompt)
        if score > best_score:
            best_name = tool_name
            best_score = score
    return best_name


def render_agent_tool_response(response: dict) -> str:
    tool_name = str(response.get("tool_name") or TOOL_KIND_DETERMINISTIC)
    if response.get("response_type") == "error":
        message = response.get("error", {}).get("message") or "unknown error"
        return f"{tool_name} failed: {message}"

    results = response.get("results") if isinstance(response.get("results"), list) else []
    lines = [f"{tool_name} returned {len(results)} result(s)."]
    for index, result in enumerate(results[:3], start=1):
        primary_label = (
            result.get("description")
            or result.get("family_and_type")
            or result.get("family_name")
            or result.get("lookup_key")
            or result.get("record_id")
            or "result"
        )
        details: list[str] = []
        if result.get("manufacturer"):
            details.append(str(result["manufacturer"]))
        if result.get("part_number"):
            details.append(f"part={result['part_number']}")
        estimate = result.get("estimate")
        if isinstance(estimate, dict) and estimate.get("installed_total") is not None:
            details.append(f"installed_total={estimate['installed_total']}")
        quantity_rollup = result.get("quantity_rollup")
        if (
            isinstance(quantity_rollup, dict)
            and quantity_rollup.get("supported")
            and isinstance(quantity_rollup.get("totals"), dict)
            and quantity_rollup["totals"].get("installed_total") is not None
        ):
            details.append(
                f"rolled_installed_total={quantity_rollup['totals']['installed_total']}"
            )

        line = f"{index}. {primary_label}"
        if details:
            line += " — " + ", ".join(details)
        lines.append(line)

    warnings = response.get("warnings") if isinstance(response.get("warnings"), list) else []
    if warnings:
        lines.append("Warnings: " + "; ".join(str(item) for item in warnings if str(item).strip()))
    return "\n".join(lines)


def execute_agent_tool(cfg: dict, tool_name: str, request: dict, *, route_name: str) -> dict:
    canonical_name = normalize_agent_tool_name(tool_name)
    tool_metadata = describe_agent_tool(cfg, canonical_name)
    tool_request = copy.deepcopy(request)
    tool_request["tool_name"] = canonical_name

    pre_hook = apply_hook_stage(
        cfg,
        HOOK_STAGE_PRE_DETERMINISTIC_TOOL,
        {
            "route": route_name,
            "tool_name": canonical_name,
            "request": copy.deepcopy(tool_request),
        },
    )
    hook_events = list(pre_hook["events"])
    hook_annotations = dict(pre_hook["annotations"])

    if pre_hook["denied"]:
        denial_message = pre_hook["deny_reason"] or "Deterministic tool denied by hook"
        response = build_tool_error(
            canonical_name,
            request=tool_request,
            message=denial_message,
            code="denied",
        )
        execution_envelope = build_execution_envelope(
            EXECUTION_SUBJECT_DETERMINISTIC_TOOL,
            canonical_name,
            EXECUTION_STATUS_DENIED,
            owner=tool_metadata["runtime_owner"],
            details={
                "request_id": tool_request.get("request_id"),
                "response_type": response.get("response_type"),
                "result_count": 0,
            },
            hook_annotations=hook_annotations,
            hook_events=hook_events,
        )
        return {
            "tool_name": canonical_name,
            "tool_metadata": tool_metadata,
            "request": tool_request,
            "response": response,
            "assistant_response": render_agent_tool_response(response),
            "execution_envelope": execution_envelope,
        }

    hook_payload = pre_hook["payload"]
    if isinstance(hook_payload.get("tool_name"), str):
        canonical_name = normalize_agent_tool_name(hook_payload["tool_name"])
        tool_metadata = describe_agent_tool(cfg, canonical_name)
    if isinstance(hook_payload.get("request"), dict):
        tool_request = hook_payload["request"]
        tool_request["tool_name"] = canonical_name

    if not tool_metadata["enabled"]:
        response = build_tool_error(
            canonical_name,
            request=tool_request,
            message=(
                f"{canonical_name} is disabled in the selected config "
                f"({tool_metadata['config_section']})"
            ),
            code="disabled",
        )
        status = EXECUTION_STATUS_FAILED
    else:
        try:
            response = _TOOL_SPECS[canonical_name]["execute_fn"](cfg, tool_request)

            post_hook = apply_hook_stage(
                cfg,
                HOOK_STAGE_POST_DETERMINISTIC_TOOL,
                {
                    "route": route_name,
                    "tool_name": canonical_name,
                    "request": copy.deepcopy(tool_request),
                    "response": copy.deepcopy(response),
                },
            )
            hook_events.extend(post_hook["events"])
            hook_annotations = dict(post_hook["annotations"])
            if post_hook["denied"]:
                denial_message = post_hook["deny_reason"] or "Deterministic tool denied by hook"
                response = build_tool_error(
                    canonical_name,
                    request=tool_request,
                    message=denial_message,
                    code="denied",
                )
                status = EXECUTION_STATUS_DENIED
            else:
                tool_payload = post_hook["payload"]
                if isinstance(tool_payload.get("tool_name"), str):
                    canonical_name = normalize_agent_tool_name(tool_payload["tool_name"])
                    tool_metadata = describe_agent_tool(cfg, canonical_name)
                if isinstance(tool_payload.get("request"), dict):
                    tool_request = tool_payload["request"]
                    tool_request["tool_name"] = canonical_name
                if isinstance(tool_payload.get("response"), dict):
                    response = tool_payload["response"]
                status = (
                    EXECUTION_STATUS_FAILED
                    if response.get("response_type") == "error"
                    else EXECUTION_STATUS_SUCCEEDED
                )
        except Exception as exc:
            response = build_tool_error(
                canonical_name,
                request=tool_request,
                message=str(exc),
                code="tool_execution_failed",
            )
            status = EXECUTION_STATUS_FAILED

    execution_envelope = build_execution_envelope(
        EXECUTION_SUBJECT_DETERMINISTIC_TOOL,
        canonical_name,
        status,
        owner=str(response.get("runtime_owner") or tool_metadata["runtime_owner"]),
        details={
            "request_id": tool_request.get("request_id"),
            "response_type": response.get("response_type"),
            "result_count": int(response.get("result_count", 0) or 0),
        },
        hook_annotations=hook_annotations,
        hook_events=hook_events,
    )
    return {
        "tool_name": canonical_name,
        "tool_metadata": tool_metadata,
        "request": tool_request,
        "response": response,
        "assistant_response": render_agent_tool_response(response),
        "execution_envelope": execution_envelope,
    }


def execute_inferred_agent_tool(
    cfg: dict,
    prompt: str,
    *,
    route_name: str,
    explicit_tool_name: str | None = None,
) -> dict:
    tool_name = infer_agent_tool_name(prompt, explicit_tool_name=explicit_tool_name)
    request = build_tool_request(tool_name, query=prompt)
    return execute_agent_tool(cfg, tool_name, request, route_name=route_name)