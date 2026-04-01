"""
Shared route/runtime contract helpers for text, retrieval, tools, and multimodal sidecars.
"""

from __future__ import annotations

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
