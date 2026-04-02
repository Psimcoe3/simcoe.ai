"""
Shared route/runtime contract helpers for text, retrieval, tools, and multimodal sidecars.
"""

from __future__ import annotations

import copy

from data_contracts import RUNTIME_OWNERS


ROUTE_TEXT = "text"
ROUTE_RETRIEVAL = "retrieval"
ROUTE_DETERMINISTIC_TOOL = "deterministic_tool"
ROUTE_DRAWING_SHEET = "drawing_sheet"
ROUTE_MIXED = "mixed"

CONTEXT_PROVIDER_MEMORY = "memory"
CONTEXT_PROVIDER_RETRIEVAL = "retrieval"

HOOK_STAGE_PRE_ROUTE = "pre_route"
HOOK_STAGE_POST_ROUTE = "post_route"
HOOK_STAGE_PRE_CONTEXT_PROVIDER = "pre_context_provider"
HOOK_STAGE_POST_CONTEXT_PROVIDER = "post_context_provider"
HOOK_STAGE_PRE_DETERMINISTIC_TOOL = "pre_deterministic_tool"
HOOK_STAGE_POST_DETERMINISTIC_TOOL = "post_deterministic_tool"

HOOK_ACTION_ANNOTATE = "annotate"
HOOK_ACTION_DENY = "deny"
HOOK_ACTION_SET_FIELDS = "set_fields"

EXECUTION_ENVELOPE_SCHEMA_VERSION = 1
EXECUTION_SUBJECT_ROUTE = "route"
EXECUTION_SUBJECT_CONTEXT_PROVIDER = "context_provider"
EXECUTION_SUBJECT_DETERMINISTIC_TOOL = "deterministic_tool"
EXECUTION_SUBJECT_TASK = "task"

EXECUTION_STATUS_SUCCEEDED = "succeeded"
EXECUTION_STATUS_FAILED = "failed"
EXECUTION_STATUS_SKIPPED = "skipped"
EXECUTION_STATUS_DENIED = "denied"

TASK_KIND_WORKFLOW = "workflow"
TASK_KIND_DREAM = "dream"
TASK_KIND_SUBAGENT = "subagent"

TASK_STATUS_PENDING = "pending"
TASK_STATUS_RUNNING = "running"
TASK_STATUS_COMPLETED = "completed"
TASK_STATUS_FAILED = "failed"
TASK_STATUS_CANCELLED = "cancelled"

KNOWN_ROUTES = {
    ROUTE_TEXT,
    ROUTE_RETRIEVAL,
    ROUTE_DETERMINISTIC_TOOL,
    ROUTE_DRAWING_SHEET,
    ROUTE_MIXED,
}
KNOWN_CONTEXT_PROVIDERS = {
    CONTEXT_PROVIDER_MEMORY,
    CONTEXT_PROVIDER_RETRIEVAL,
}
KNOWN_HOOK_STAGES = {
    HOOK_STAGE_PRE_ROUTE,
    HOOK_STAGE_POST_ROUTE,
    HOOK_STAGE_PRE_CONTEXT_PROVIDER,
    HOOK_STAGE_POST_CONTEXT_PROVIDER,
    HOOK_STAGE_PRE_DETERMINISTIC_TOOL,
    HOOK_STAGE_POST_DETERMINISTIC_TOOL,
}
KNOWN_HOOK_ACTIONS = {
    HOOK_ACTION_ANNOTATE,
    HOOK_ACTION_DENY,
    HOOK_ACTION_SET_FIELDS,
}
KNOWN_EXECUTION_SUBJECTS = {
    EXECUTION_SUBJECT_ROUTE,
    EXECUTION_SUBJECT_CONTEXT_PROVIDER,
    EXECUTION_SUBJECT_DETERMINISTIC_TOOL,
    EXECUTION_SUBJECT_TASK,
}
KNOWN_EXECUTION_STATUSES = {
    EXECUTION_STATUS_SUCCEEDED,
    EXECUTION_STATUS_FAILED,
    EXECUTION_STATUS_SKIPPED,
    EXECUTION_STATUS_DENIED,
}
KNOWN_TASK_KINDS = {
    TASK_KIND_WORKFLOW,
    TASK_KIND_DREAM,
    TASK_KIND_SUBAGENT,
}
KNOWN_TASK_STATUSES = {
    TASK_STATUS_PENDING,
    TASK_STATUS_RUNNING,
    TASK_STATUS_COMPLETED,
    TASK_STATUS_FAILED,
    TASK_STATUS_CANCELLED,
}
MULTIMODAL_ROUTES = {ROUTE_DRAWING_SHEET, ROUTE_MIXED}
FAIL_ROUTE_FALLBACK = "fail"

ROUTE_DEFAULT_RUNTIME_OWNER = {
    ROUTE_TEXT: "text",
    ROUTE_RETRIEVAL: "retrieval",
    ROUTE_DETERMINISTIC_TOOL: "geometry_rules",
    ROUTE_DRAWING_SHEET: "multimodal",
    ROUTE_MIXED: "multimodal",
}

ROUTE_RUNTIME_OWNERS = {
    ROUTE_TEXT: {"text"},
    ROUTE_RETRIEVAL: {"retrieval", "text"},
    ROUTE_DETERMINISTIC_TOOL: {"geometry_rules"},
    ROUTE_DRAWING_SHEET: {"multimodal"},
    ROUTE_MIXED: {"multimodal"},
}


def normalize_route(value: object, label: str = "route") -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")

    route = value.strip().lower()
    if route not in KNOWN_ROUTES:
        choices = ", ".join(sorted(KNOWN_ROUTES))
        raise ValueError(f"{label} must be one of: {choices}")
    return route


def normalize_context_provider(value: object, label: str = "context provider") -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")

    provider = value.strip().lower()
    if provider not in KNOWN_CONTEXT_PROVIDERS:
        choices = ", ".join(sorted(KNOWN_CONTEXT_PROVIDERS))
        raise ValueError(f"{label} must be one of: {choices}")
    return provider


def normalize_hook_stage(value: object, label: str = "hook stage") -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")

    stage = value.strip().lower()
    if stage not in KNOWN_HOOK_STAGES:
        choices = ", ".join(sorted(KNOWN_HOOK_STAGES))
        raise ValueError(f"{label} must be one of: {choices}")
    return stage


def normalize_hook_action(value: object, label: str = "hook action") -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")

    action = value.strip().lower()
    if action not in KNOWN_HOOK_ACTIONS:
        choices = ", ".join(sorted(KNOWN_HOOK_ACTIONS))
        raise ValueError(f"{label} must be one of: {choices}")
    return action


def normalize_execution_subject(value: object, label: str = "execution subject") -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")

    subject = value.strip().lower()
    if subject not in KNOWN_EXECUTION_SUBJECTS:
        choices = ", ".join(sorted(KNOWN_EXECUTION_SUBJECTS))
        raise ValueError(f"{label} must be one of: {choices}")
    return subject


def normalize_execution_status(value: object, label: str = "execution status") -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")

    status = value.strip().lower()
    if status not in KNOWN_EXECUTION_STATUSES:
        choices = ", ".join(sorted(KNOWN_EXECUTION_STATUSES))
        raise ValueError(f"{label} must be one of: {choices}")
    return status


def normalize_task_kind(value: object, label: str = "task kind") -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")

    task_kind = value.strip().lower()
    if task_kind not in KNOWN_TASK_KINDS:
        choices = ", ".join(sorted(KNOWN_TASK_KINDS))
        raise ValueError(f"{label} must be one of: {choices}")
    return task_kind


def normalize_task_status(value: object, label: str = "task status") -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")

    task_status = value.strip().lower()
    if task_status not in KNOWN_TASK_STATUSES:
        choices = ", ".join(sorted(KNOWN_TASK_STATUSES))
        raise ValueError(f"{label} must be one of: {choices}")
    return task_status


def build_execution_envelope(
    subject_type: object,
    subject_name: object,
    status: object,
    *,
    owner: object | None = None,
    details: dict | None = None,
    hook_annotations: dict | None = None,
    hook_events: list[dict] | None = None,
) -> dict:
    if not isinstance(subject_name, str) or not subject_name.strip():
        raise ValueError("execution subject_name must be a non-empty string")

    envelope = {
        "schema_version": EXECUTION_ENVELOPE_SCHEMA_VERSION,
        "subject_type": normalize_execution_subject(subject_type),
        "subject_name": subject_name.strip().lower(),
        "status": normalize_execution_status(status),
    }
    if owner is not None:
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("execution owner must be a non-empty string when present")
        envelope["owner"] = owner.strip().lower()
    if details:
        envelope["details"] = copy.deepcopy(details)
    if hook_annotations:
        envelope["hook_annotations"] = copy.deepcopy(hook_annotations)
    if hook_events:
        envelope["hook_events"] = copy.deepcopy(hook_events)
    return envelope


def summarize_execution_envelopes(envelopes: list[dict | None]) -> dict:
    summary = {
        "total": 0,
        "by_status": {},
        "by_subject_type": {},
        "by_subject": {},
        "by_owner": {},
    }

    for envelope in envelopes:
        if not isinstance(envelope, dict):
            continue

        subject_type = envelope.get("subject_type")
        subject_name = envelope.get("subject_name")
        status = envelope.get("status")
        owner = envelope.get("owner")
        if (
            not isinstance(subject_type, str)
            or not isinstance(subject_name, str)
            or not isinstance(status, str)
        ):
            continue

        summary["total"] += 1
        summary["by_status"][status] = summary["by_status"].get(status, 0) + 1
        summary["by_subject_type"][subject_type] = (
            summary["by_subject_type"].get(subject_type, 0) + 1
        )
        subject_key = f"{subject_type}:{subject_name}"
        summary["by_subject"][subject_key] = summary["by_subject"].get(subject_key, 0) + 1
        if isinstance(owner, str) and owner.strip():
            summary["by_owner"][owner] = summary["by_owner"].get(owner, 0) + 1

    return summary


def normalize_route_fallback(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")

    cleaned = value.strip().lower()
    if cleaned == FAIL_ROUTE_FALLBACK:
        return cleaned
    return normalize_route(cleaned, label)


def route_requires_multimodal(route: str) -> bool:
    return route in MULTIMODAL_ROUTES


def default_runtime_owner_for_route(route: str) -> str:
    return ROUTE_DEFAULT_RUNTIME_OWNER[route]


def validate_route_contract(
    route_value: object,
    runtime_owner_value: object,
    *,
    multimodal_enabled: bool,
    route_label: str = "route",
    runtime_owner_label: str = "runtime_owner",
) -> tuple[str, str]:
    route = normalize_route(route_value, route_label)
    if route_requires_multimodal(route) and not multimodal_enabled:
        raise ValueError(
            f"{route_label}='{route}' requires architecture.multimodal_runtime_enabled=true"
        )

    if runtime_owner_value is None:
        runtime_owner = default_runtime_owner_for_route(route)
    else:
        if not isinstance(runtime_owner_value, str) or not runtime_owner_value.strip():
            raise ValueError(f"{runtime_owner_label} must be a non-empty string when present")
        runtime_owner = runtime_owner_value.strip().lower()

    if runtime_owner not in RUNTIME_OWNERS:
        choices = ", ".join(sorted(RUNTIME_OWNERS))
        raise ValueError(f"{runtime_owner_label} must be one of: {choices}")

    allowed_runtime_owners = ROUTE_RUNTIME_OWNERS[route]
    if runtime_owner not in allowed_runtime_owners:
        choices = ", ".join(sorted(allowed_runtime_owners))
        raise ValueError(
            f"{runtime_owner_label}='{runtime_owner}' is invalid for {route_label}='{route}'; "
            f"allowed values: {choices}"
        )

    return route, runtime_owner
