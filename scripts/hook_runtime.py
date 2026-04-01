from __future__ import annotations

import copy

from runtime_contracts import (
    HOOK_ACTION_ANNOTATE,
    HOOK_ACTION_DENY,
    HOOK_ACTION_SET_FIELDS,
    normalize_hook_action,
    normalize_hook_stage,
)


def _get_nested_value(payload: dict, path: str) -> object:
    current: object = payload
    for segment in path.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(segment)
    return current


def _set_nested_value(payload: dict, path: str, value: object) -> None:
    segments = [segment for segment in path.split(".") if segment]
    if not segments:
        return

    current = payload
    for segment in segments[:-1]:
        nested = current.get(segment)
        if not isinstance(nested, dict):
            nested = {}
            current[segment] = nested
        current = nested
    current[segments[-1]] = value


def _matches_expected(actual: object, expected: object) -> bool:
    if isinstance(actual, list):
        if isinstance(expected, list):
            return all(item in actual for item in expected)
        return expected in actual
    if isinstance(expected, list):
        return actual in expected
    return actual == expected


def _rule_matches(rule: dict, payload: dict) -> bool:
    match = rule.get("match")
    if match is None:
        return True
    if not isinstance(match, dict):
        return False

    for field_path, expected in match.items():
        actual = _get_nested_value(payload, str(field_path))
        if not _matches_expected(actual, expected):
            return False
    return True


def apply_hook_stage(cfg: dict, stage: str, payload: dict) -> dict:
    normalized_stage = normalize_hook_stage(stage)
    hooks_cfg = cfg.get("hooks") if isinstance(cfg.get("hooks"), dict) else {}
    rules = hooks_cfg.get("rules") if isinstance(hooks_cfg.get("rules"), list) else []
    if not hooks_cfg or not bool(hooks_cfg.get("enabled", False)) or not rules:
        annotations = dict(payload.get("hook_annotations") or {})
        return {
            "payload": copy.deepcopy(payload),
            "events": [],
            "annotations": annotations,
            "denied": False,
            "deny_reason": None,
        }

    working_payload = copy.deepcopy(payload)
    annotations = dict(working_payload.get("hook_annotations") or {})
    events: list[dict] = []
    deny_reason: str | None = None

    for index, raw_rule in enumerate(rules):
        if not isinstance(raw_rule, dict):
            continue
        if raw_rule.get("enabled") is False:
            continue

        rule_stage = normalize_hook_stage(raw_rule.get("stage"), f"hooks.rules[{index}].stage")
        if rule_stage != normalized_stage:
            continue

        if not _rule_matches(raw_rule, working_payload):
            continue

        action = normalize_hook_action(raw_rule.get("action"), f"hooks.rules[{index}].action")
        rule_name = str(raw_rule.get("name") or f"{normalized_stage}_{index}")
        event = {
            "name": rule_name,
            "stage": normalized_stage,
            "action": action,
            "applied": True,
        }

        if action == HOOK_ACTION_ANNOTATE:
            fields = raw_rule.get("fields") if isinstance(raw_rule.get("fields"), dict) else {}
            for key, value in fields.items():
                annotations[str(key)] = copy.deepcopy(value)
            if annotations:
                working_payload["hook_annotations"] = copy.deepcopy(annotations)
            event["field_count"] = len(fields)
        elif action == HOOK_ACTION_SET_FIELDS:
            fields = raw_rule.get("fields") if isinstance(raw_rule.get("fields"), dict) else {}
            for key, value in fields.items():
                _set_nested_value(working_payload, str(key), copy.deepcopy(value))
            event["field_count"] = len(fields)
        elif action == HOOK_ACTION_DENY:
            deny_reason = str(raw_rule.get("reason") or f"Denied by hook '{rule_name}'")
            event["denied"] = True
            event["reason"] = deny_reason

        events.append(event)
        if deny_reason is not None:
            break

    if annotations:
        working_payload["hook_annotations"] = copy.deepcopy(annotations)
    else:
        working_payload.pop("hook_annotations", None)

    return {
        "payload": working_payload,
        "events": events,
        "annotations": annotations,
        "denied": deny_reason is not None,
        "deny_reason": deny_reason,
    }
