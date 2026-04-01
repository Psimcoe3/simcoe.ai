"""
Fast heuristic request router for text, retrieval, deterministic tools, and drawing sheets.
"""

from __future__ import annotations

import argparse
import json

from config_validation import (
    validate_orchestration_config,
    load_config,
    validate_architecture_config,
    validate_deterministic_tools_config,
    validate_multimodal_config,
    validate_retrieval_config,
    validate_routing_config,
)
from data_contracts import infer_asset_kind, is_drawing_asset
from hook_runtime import apply_hook_stage
from runtime_contracts import (
    FAIL_ROUTE_FALLBACK,
    HOOK_STAGE_POST_ROUTE,
    HOOK_STAGE_PRE_ROUTE,
    ROUTE_DETERMINISTIC_TOOL,
    ROUTE_DRAWING_SHEET,
    ROUTE_MIXED,
    ROUTE_RETRIEVAL,
    ROUTE_TEXT,
    default_runtime_owner_for_route,
    normalize_route,
)


DRAWING_QUERY_PHRASES = (
    "drawing",
    "drawings",
    "plan sheet",
    "plan sheets",
    "plan set",
    "plan sets",
    "blueprint",
    "blueprints",
    "floor plan",
    "elevation",
    "panel schedule",
    "single line",
    "one line",
    "schematic",
    "sheet a",
    "sheet e",
)

TOOL_QUERY_PHRASES = (
    "estimate lookup",
    "find the estimate",
    "find estimate",
    "revit entity lookup",
    "find the revit",
    "family type",
    "record id",
    "lookup key",
)

RETRIEVAL_QUERY_PHRASES = (
    "summarize the electrical construction reference source",
    "what should",
    "from the reference",
    "from source",
    "source module",
    "source section",
    "page ",
    "section ",
    "module ",
)


def _normalized_text(value: str | None) -> str:
    if not isinstance(value, str) or not value.strip():
        return ""
    cleaned = value.strip().lower().replace("_", " ").replace("-", " ")
    return " ".join(cleaned.split())


def _contains_phrase(text: str, phrases: tuple[str, ...]) -> bool:
    return any(phrase in text for phrase in phrases)


def _has_enabled_tool(cfg: dict) -> bool:
    deterministic_tools = (
        cfg.get("deterministic_tools") if isinstance(cfg.get("deterministic_tools"), dict) else {}
    )
    return any(
        bool(tool_cfg.get("enabled", False))
        for tool_cfg in deterministic_tools.values()
        if isinstance(tool_cfg, dict)
    )


def _route_available(route: str, cfg: dict) -> bool:
    architecture = cfg.get("architecture") if isinstance(cfg.get("architecture"), dict) else {}
    retrieval_cfg = cfg.get("retrieval") if isinstance(cfg.get("retrieval"), dict) else {}

    if route == ROUTE_TEXT:
        return True
    if route == ROUTE_RETRIEVAL:
        return bool(architecture.get("retrieval_layer_enabled", False)) and bool(
            retrieval_cfg.get("enabled", False)
        )
    if route == ROUTE_DETERMINISTIC_TOOL:
        return _has_enabled_tool(cfg)
    if route == ROUTE_DRAWING_SHEET:
        return bool(architecture.get("multimodal_runtime_enabled", False))
    if route == ROUTE_MIXED:
        return bool(architecture.get("multimodal_runtime_enabled", False)) and (
            bool(architecture.get("retrieval_layer_enabled", False)) or _has_enabled_tool(cfg)
        )
    return False


def _resolve_route(requested_route: str, cfg: dict) -> tuple[str, list[str]]:
    routing_cfg = cfg.get("routing") if isinstance(cfg.get("routing"), dict) else {}
    route_fallbacks = (
        routing_cfg.get("route_fallbacks")
        if isinstance(routing_cfg.get("route_fallbacks"), dict)
        else {}
    )

    visited: set[str] = set()
    fallback_chain: list[str] = []
    current_route = requested_route
    while True:
        if current_route in visited:
            raise ValueError(
                f"Routing fallback cycle detected: {' -> '.join(fallback_chain + [current_route])}"
            )
        visited.add(current_route)
        fallback_chain.append(current_route)

        if _route_available(current_route, cfg):
            return current_route, fallback_chain

        fallback = route_fallbacks.get(current_route, FAIL_ROUTE_FALLBACK)
        if fallback == FAIL_ROUTE_FALLBACK:
            raise ValueError(
                f"Route '{requested_route}' is not available and routing fallback policy is 'fail'"
            )
        current_route = str(fallback)


def _attachment_suggests_drawing(attachments: list[str] | None) -> bool:
    for attachment in attachments or []:
        asset_kind = infer_asset_kind(attachment)
        if is_drawing_asset(asset_kind, attachment):
            return True
    return False


def _finalize_route_decision(decision: dict, latency_budgets: dict) -> dict:
    requested_route = normalize_route(
        decision.get("requested_route") or ROUTE_TEXT,
        "route decision requested_route",
    )
    resolved_route = normalize_route(
        decision.get("resolved_route") or requested_route,
        "route decision resolved_route",
    )
    fallback_chain = decision.get("fallback_chain")
    if isinstance(fallback_chain, list) and fallback_chain:
        normalized_chain = [
            normalize_route(route_name, "route decision fallback_chain")
            for route_name in fallback_chain
        ]
    else:
        normalized_chain = [requested_route]
        if resolved_route != requested_route:
            normalized_chain.append(resolved_route)

    attachments = decision.get("attachments")
    normalized_attachments = []
    if isinstance(attachments, list):
        normalized_attachments = [
            str(attachment).strip()
            for attachment in attachments
            if isinstance(attachment, str) and str(attachment).strip()
        ]

    reasons = decision.get("reasons")
    normalized_reasons = []
    if isinstance(reasons, list):
        normalized_reasons = [
            str(reason).strip()
            for reason in reasons
            if isinstance(reason, str) and str(reason).strip()
        ]

    decision["requested_route"] = requested_route
    decision["resolved_route"] = resolved_route
    decision["runtime_owner"] = default_runtime_owner_for_route(resolved_route)
    decision["latency_budget_ms"] = int(latency_budgets.get(resolved_route, 0) or 0)
    decision["fallback_chain"] = normalized_chain
    decision["fallback_applied"] = resolved_route != requested_route
    decision["attachments"] = normalized_attachments
    decision["reasons"] = normalized_reasons
    return decision


def route_request(
    cfg: dict,
    instruction: str,
    *,
    context: str | None = None,
    source: str | None = None,
    section: str | None = None,
    attachments: list[str] | None = None,
    tool_name: str | None = None,
    explicit_route: str | None = None,
) -> dict:
    routing_cfg = cfg.get("routing") if isinstance(cfg.get("routing"), dict) else {}
    default_route = str(routing_cfg.get("default_route") or ROUTE_TEXT)
    latency_budgets = (
        routing_cfg.get("latency_budgets_ms")
        if isinstance(routing_cfg.get("latency_budgets_ms"), dict)
        else {}
    )

    pre_hook = apply_hook_stage(
        cfg,
        HOOK_STAGE_PRE_ROUTE,
        {
            "instruction": instruction,
            "context": context,
            "source": source,
            "section": section,
            "attachments": list(attachments or []),
            "tool_name": tool_name,
            "explicit_route": explicit_route,
        },
    )
    hook_events = list(pre_hook["events"])
    if pre_hook["denied"]:
        raise ValueError(pre_hook["deny_reason"] or "Request denied by pre_route hook")

    hook_payload = pre_hook["payload"]
    hook_annotations = dict(pre_hook["annotations"])
    instruction = str(hook_payload.get("instruction") or instruction)
    context = (
        hook_payload.get("context") if isinstance(hook_payload.get("context"), str) else context
    )
    source = hook_payload.get("source") if isinstance(hook_payload.get("source"), str) else source
    section = (
        hook_payload.get("section") if isinstance(hook_payload.get("section"), str) else section
    )
    attachments = (
        list(hook_payload.get("attachments"))
        if isinstance(hook_payload.get("attachments"), list)
        else list(attachments or [])
    )
    tool_name = (
        hook_payload.get("tool_name")
        if isinstance(hook_payload.get("tool_name"), str)
        else tool_name
    )
    explicit_route = (
        hook_payload.get("explicit_route")
        if isinstance(hook_payload.get("explicit_route"), str)
        else explicit_route
    )

    normalized_instruction = _normalized_text(instruction)
    normalized_context = _normalized_text(context)
    combined_text = " ".join(
        part for part in (normalized_instruction, normalized_context) if part
    ).strip()

    explicit_tool = isinstance(tool_name, str) and bool(tool_name.strip())
    retrieval_hints = bool(_normalized_text(source) or _normalized_text(section))
    drawing_hints = _contains_phrase(
        combined_text, DRAWING_QUERY_PHRASES
    ) or _attachment_suggests_drawing(attachments)
    tool_hints = explicit_tool or _contains_phrase(combined_text, TOOL_QUERY_PHRASES)
    text_retrieval_hints = retrieval_hints or _contains_phrase(
        combined_text, RETRIEVAL_QUERY_PHRASES
    )

    reasons: list[str] = []
    if explicit_route:
        requested_route = explicit_route
        reasons.append("explicit_route")
    elif drawing_hints and (tool_hints or text_retrieval_hints):
        requested_route = ROUTE_MIXED
        reasons.append("drawing_and_secondary_hints")
    elif drawing_hints:
        requested_route = ROUTE_DRAWING_SHEET
        reasons.append("drawing_hints")
    elif tool_hints:
        requested_route = ROUTE_DETERMINISTIC_TOOL
        reasons.append("deterministic_tool_hints")
    elif text_retrieval_hints:
        requested_route = ROUTE_RETRIEVAL
        reasons.append("retrieval_hints")
    else:
        requested_route = default_route
        reasons.append("routing.default_route")

    resolved_route, fallback_chain = _resolve_route(requested_route, cfg)
    decision = {
        "requested_route": requested_route,
        "resolved_route": resolved_route,
        "runtime_owner": default_runtime_owner_for_route(resolved_route),
        "latency_budget_ms": int(latency_budgets.get(resolved_route, 0) or 0),
        "fallback_chain": fallback_chain,
        "fallback_applied": resolved_route != requested_route,
        "attachments": list(attachments or []),
        "reasons": reasons,
    }
    if hook_annotations:
        decision["hook_annotations"] = hook_annotations

    post_hook = apply_hook_stage(cfg, HOOK_STAGE_POST_ROUTE, decision)
    hook_events.extend(post_hook["events"])
    if post_hook["denied"]:
        raise ValueError(post_hook["deny_reason"] or "Request denied by post_route hook")

    finalized_decision = _finalize_route_decision(post_hook["payload"], latency_budgets)
    if post_hook["annotations"]:
        finalized_decision["hook_annotations"] = dict(post_hook["annotations"])
    else:
        finalized_decision.pop("hook_annotations", None)
    if hook_events:
        finalized_decision["hook_events"] = hook_events
    return finalized_decision


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Route a single request using the configured fast heuristic router."
    )
    parser.add_argument("--config", default="config.yaml", help="Config file with routing settings")
    parser.add_argument("--instruction", required=True, help="Instruction text to classify")
    parser.add_argument("--context", help="Optional input/context text")
    parser.add_argument("--source", help="Optional grounded source hint")
    parser.add_argument("--section", help="Optional grounded section hint")
    parser.add_argument(
        "--attachment",
        action="append",
        default=[],
        help="Optional attachment path. Can be repeated.",
    )
    parser.add_argument("--tool-name", help="Optional explicit deterministic tool name")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = load_config(args.config)
    validate_architecture_config(cfg)
    validate_routing_config(cfg)
    validate_multimodal_config(cfg)
    validate_retrieval_config(cfg)
    validate_orchestration_config(cfg)
    validate_deterministic_tools_config(cfg)

    decision = route_request(
        cfg,
        args.instruction,
        context=args.context,
        source=args.source,
        section=args.section,
        attachments=args.attachment,
        tool_name=args.tool_name,
    )
    print(json.dumps(decision, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
