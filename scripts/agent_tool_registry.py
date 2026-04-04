"""
Shared first-party tool registry for the local simcoe.ai agent shell.
"""

from __future__ import annotations

import copy
import re

from agent_registry import normalize_agent_definition_name, resolve_agent_registry_settings
from agent_task_manager import resolve_agent_task_manager_settings, start_subagent_task
from deterministic_tool_utils import build_tool_error, build_tool_request
from estimate_lookup import TOOL_NAME as ESTIMATE_LOOKUP_TOOL_NAME, run_estimate_lookup_request
from hook_runtime import apply_hook_stage
from manifest_utils import current_utc_timestamp
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
TOOL_ACCESS_MUTATING = "mutating"
TOOL_EXECUTION_SERIAL = "serial"

DEFAULT_AGENT_TOOL_NAME = ESTIMATE_LOOKUP_TOOL_NAME
DELEGATE_TO_SUBAGENT_TOOL_NAME = "delegate_to_subagent"
DELEGATE_TOOL_DEFAULT_SOURCE = "agent_shell_delegate"

_DELEGATE_TOOL_PATTERNS = (
    re.compile(
        r"^\s*(?:delegate|assign|route|send|start|launch|run)\s+(?:to\s+)?(?P<agent>[^:]+?)\s*:\s*(?P<task>.+)\s*$",
        re.IGNORECASE,
    ),
    re.compile(
        r"^\s*(?:delegate|assign|route|send)\s+(?:to\s+)?(?P<agent>.+?)\s+to\s+(?P<task>.+)\s*$",
        re.IGNORECASE,
    ),
    re.compile(
        r"^\s*(?:ask|have)\s+(?P<agent>.+?)\s+to\s+(?P<task>.+)\s*$",
        re.IGNORECASE,
    ),
    re.compile(
        r"^\s*(?:subagent|worker)\s+(?P<agent>[^:]+?)\s*:\s*(?P<task>.+)\s*$",
        re.IGNORECASE,
    ),
    re.compile(
        r"^\s*agent\s*[:=]\s*(?P<agent>[^:]+?)\s*[:,-]?\s*(?P<task>.+)\s*$",
        re.IGNORECASE,
    ),
    re.compile(r"^\s*@(?P<agent>[A-Za-z0-9_./ -]+?)\s+(?P<task>.+)\s*$", re.IGNORECASE),
)


def _delegate_tool_enabled(cfg: dict) -> bool:
    agent_registry = resolve_agent_registry_settings(cfg)
    task_manager = resolve_agent_task_manager_settings(cfg)
    if not agent_registry["enabled"] or not task_manager["enabled"]:
        return False

    tool_cfg = _tool_config(cfg, DELEGATE_TO_SUBAGENT_TOOL_NAME)
    return tool_cfg.get("enabled") is not False


def _delegate_tool_attachments(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item.strip() for item in value if isinstance(item, str) and item.strip()]


def _delegate_tool_briefing(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    cleaned = value.strip()
    return cleaned or None


def _delegate_tool_candidate_queries(query: str) -> list[str]:
    candidates = [query]
    for marker in ("### Assigned Task:", "Assigned Task:"):
        if marker not in query:
            continue
        candidate = query.rsplit(marker, 1)[-1].strip()
        if candidate and candidate not in candidates:
            candidates.append(candidate)
    return candidates


def _resolve_delegate_target(cfg: dict, request: dict) -> tuple[str, str]:
    filters = request.get("filters") if isinstance(request.get("filters"), dict) else {}
    query = request.get("query") if isinstance(request.get("query"), str) else None
    cleaned_query = query.strip() if isinstance(query, str) and query.strip() else None

    explicit_agent = None
    for filter_name in ("agent", "agent_definition_name"):
        candidate = filters.get(filter_name)
        if isinstance(candidate, str) and candidate.strip():
            explicit_agent = candidate.strip()
            break

    if explicit_agent is not None:
        if cleaned_query is None:
            raise ValueError(
                "delegate_to_subagent requires request.query when filters.agent is used"
            )
        candidate_queries = _delegate_tool_candidate_queries(cleaned_query)
        delegated_prompt = next(
            (candidate for candidate in candidate_queries[1:] if candidate.strip()),
            cleaned_query,
        )
        return normalize_agent_definition_name(cfg, explicit_agent), delegated_prompt

    if cleaned_query is None:
        raise ValueError("delegate_to_subagent requires a non-empty query")

    for candidate_query in _delegate_tool_candidate_queries(cleaned_query):
        for pattern in _DELEGATE_TOOL_PATTERNS:
            match = pattern.match(candidate_query)
            if match is None:
                continue
            agent_candidate = match.group("agent").strip().strip('"\'')
            delegated_prompt = match.group("task").strip()
            if not agent_candidate or not delegated_prompt:
                continue
            return normalize_agent_definition_name(cfg, agent_candidate), delegated_prompt

    raise ValueError(
        "delegate_to_subagent requires an agent name plus task text. "
        "Use patterns like 'delegate to estimate-reviewer: review the answer' or "
        "'ask estimate-reviewer to review the answer'."
    )


def _delegate_task_payload(summary: dict) -> dict:
    metadata = summary.get("metadata") if isinstance(summary.get("metadata"), dict) else {}
    return {
        "task_id": summary.get("task_id"),
        "kind": summary.get("kind"),
        "name": summary.get("name"),
        "status": summary.get("status"),
        "source": summary.get("source"),
        "summary_path": summary.get("summary_path"),
        "log_path": summary.get("log_path"),
        "parent_task_id": metadata.get("parent_task_id"),
        "agent_definition_name": metadata.get("agent_definition_name"),
    }


def _build_delegate_tool_response(request: dict, started_summary: dict) -> dict:
    task_payload = _delegate_task_payload(started_summary)
    return {
        "schema_version": 1,
        "tool_name": DELEGATE_TO_SUBAGENT_TOOL_NAME,
        "runtime_owner": "text",
        "response_type": "task_result",
        "generated_at": current_utc_timestamp(),
        "request": copy.deepcopy(request),
        "result_count": 1,
        "results": [task_payload],
        "task": task_payload,
        "warnings": [],
        "provenance": {
            "config_path": str(started_summary.get("config_path") or request.get("config_path") or "config.yaml"),
        },
    }


def _run_delegate_to_subagent_request(cfg: dict, request: dict) -> dict:
    if not _delegate_tool_enabled(cfg):
        raise ValueError("delegate_to_subagent requires agent_registry.enabled and agent_task_manager.enabled")

    config_path = request.get("config_path") if isinstance(request.get("config_path"), str) else None
    agent_definition_name, delegated_prompt = _resolve_delegate_target(cfg, request)
    filters = request.get("filters") if isinstance(request.get("filters"), dict) else {}
    request_source = filters.get("source") if isinstance(filters.get("source"), str) else None
    raw_parent_task_id = filters.get("parent_task_id")
    parent_task_id = (
        raw_parent_task_id.strip()
        if isinstance(raw_parent_task_id, str) and raw_parent_task_id.strip()
        else None
    )
    delegation_briefing = _delegate_tool_briefing(filters.get("delegation_briefing"))
    section = filters.get("section") if isinstance(filters.get("section"), str) else None
    attachments = _delegate_tool_attachments(filters.get("attachments"))

    started_summary = start_subagent_task(
        cfg,
        config_path or "config.yaml",
        delegated_prompt,
        agent_definition_name=agent_definition_name,
        source=DELEGATE_TOOL_DEFAULT_SOURCE,
        request_source=request_source,
        section=section,
        attachments=attachments,
        parent_task_id=parent_task_id,
        delegation_briefing=delegation_briefing,
    )
    return _build_delegate_tool_response(request, started_summary)

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
    DELEGATE_TO_SUBAGENT_TOOL_NAME: {
        "name": DELEGATE_TO_SUBAGENT_TOOL_NAME,
        "display_name": "Delegate To Subagent",
        "description": (
            "Start a bounded background subagent task from a named local agent definition "
            "and return the new task id for follow-up."
        ),
        "kind": TOOL_KIND_DETERMINISTIC,
        "route": ROUTE_DETERMINISTIC_TOOL,
        "runtime_owner": "text",
        "access_mode": TOOL_ACCESS_MUTATING,
        "execution_mode": TOOL_EXECUTION_SERIAL,
        "aliases": ["delegate", "subagent", "delegate-subagent"],
        "routing_markers": ["delegate to", "start subagent", "launch subagent", "subagent"],
        "config_section": "deterministic_tools.delegate_to_subagent",
        "defaults": {},
        "execute_fn": _run_delegate_to_subagent_request,
    },
}

_TOOL_ORDER = (
    ESTIMATE_LOOKUP_TOOL_NAME,
    REVIT_ENTITY_LOOKUP_TOOL_NAME,
    DELEGATE_TO_SUBAGENT_TOOL_NAME,
)


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
    if tool_name == DELEGATE_TO_SUBAGENT_TOOL_NAME:
        enabled = enabled and _delegate_tool_enabled(cfg)

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
    tools = [describe_agent_tool(cfg, tool_name) for tool_name in _TOOL_ORDER]
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

    if response.get("response_type") == "task_result":
        task = response.get("task") if isinstance(response.get("task"), dict) else None
        if task is None:
            results = response.get("results") if isinstance(response.get("results"), list) else []
            task = results[0] if results and isinstance(results[0], dict) else {}
        task_id = task.get("task_id") or "unknown-task"
        kind = task.get("kind") or "task"
        agent_definition_name = task.get("agent_definition_name")
        message = f"{tool_name} started {kind} task {task_id}"
        if isinstance(agent_definition_name, str) and agent_definition_name.strip():
            message += f" using agent {agent_definition_name}"
        message += f". Use /tasks show {task_id} or /tasks attach {task_id}."
        return message

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
    config_path: str | None = None,
    source: str | None = None,
    section: str | None = None,
    attachments: list[str] | None = None,
    parent_task_id: str | None = None,
    delegation_briefing: str | None = None,
) -> dict:
    tool_name = infer_agent_tool_name(prompt, explicit_tool_name=explicit_tool_name)
    filters: dict[str, object] = {}
    if isinstance(source, str) and source.strip():
        filters["source"] = source.strip()
    if isinstance(section, str) and section.strip():
        filters["section"] = section.strip()
    if isinstance(attachments, list) and attachments:
        filters["attachments"] = [
            item.strip() for item in attachments if isinstance(item, str) and item.strip()
        ]
    if isinstance(parent_task_id, str) and parent_task_id.strip():
        filters["parent_task_id"] = parent_task_id.strip()
    if isinstance(delegation_briefing, str) and delegation_briefing.strip():
        filters["delegation_briefing"] = delegation_briefing.strip()
    request = build_tool_request(tool_name, query=prompt, filters=filters or None)
    if isinstance(config_path, str) and config_path.strip():
        request["config_path"] = config_path.strip()
    return execute_agent_tool(cfg, tool_name, request, route_name=route_name)