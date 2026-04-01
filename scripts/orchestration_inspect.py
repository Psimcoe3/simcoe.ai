from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path

from config_validation import (
    validate_agent_shell_config,
    load_config,
    validate_context_providers_config,
    validate_hooks_config,
)
from context_providers import active_context_provider_names, resolve_context_provider_settings
from manifest_utils import read_json_file
from runtime_contracts import summarize_execution_envelopes


def describe_hooks(cfg: dict) -> dict:
    hooks_cfg = cfg.get("hooks") if isinstance(cfg.get("hooks"), dict) else {}
    rules = hooks_cfg.get("rules") if isinstance(hooks_cfg.get("rules"), list) else []
    stage_counts: dict[str, int] = {}
    action_counts: dict[str, int] = {}
    summarized_rules: list[dict] = []
    for rule in rules:
        if not isinstance(rule, dict):
            continue
        stage = str(rule.get("stage") or "unknown")
        action = str(rule.get("action") or "unknown")
        stage_counts[stage] = stage_counts.get(stage, 0) + 1
        action_counts[action] = action_counts.get(action, 0) + 1
        match = rule.get("match") if isinstance(rule.get("match"), dict) else {}
        fields = rule.get("fields") if isinstance(rule.get("fields"), dict) else {}
        summarized_rules.append(
            {
                "name": rule.get("name"),
                "stage": stage,
                "action": action,
                "enabled": rule.get("enabled", True),
                "match_keys": sorted(match),
                "field_keys": sorted(fields),
            }
        )

    return {
        "enabled": bool(hooks_cfg.get("enabled", False)),
        "rule_count": len(summarized_rules),
        "by_stage": stage_counts,
        "by_action": action_counts,
        "rules": summarized_rules,
    }


def describe_context_providers(cfg: dict) -> dict:
    provider_settings = resolve_context_provider_settings(cfg)
    retrieval_cfg = cfg.get("retrieval") if isinstance(cfg.get("retrieval"), dict) else {}
    memory_cfg = cfg.get("memory") if isinstance(cfg.get("memory"), dict) else {}
    return {
        "order": provider_settings["order"],
        "active": active_context_provider_names(cfg, provider_settings["order"]),
        "max_workers": provider_settings["max_workers"],
        "retrieval_enabled": bool(retrieval_cfg.get("enabled", False)),
        "memory_enabled": bool(memory_cfg.get("enabled", False)),
    }


def _resolve_agent_shell_settings(cfg: dict) -> dict:
    agent_shell = cfg.get("agent_shell") if isinstance(cfg.get("agent_shell"), dict) else {}

    root_dir = Path(str(agent_shell.get("root_dir") or "data/agent_shell")).expanduser()
    if not root_dir.is_absolute():
        root_dir = Path(os.path.abspath(str(root_dir)))

    sessions_dir = Path(str(agent_shell.get("sessions_dir") or root_dir / "sessions")).expanduser()
    if not sessions_dir.is_absolute():
        sessions_dir = Path(os.path.abspath(str(sessions_dir)))

    transcripts_dir = Path(
        str(agent_shell.get("transcripts_dir") or root_dir / "transcripts")
    ).expanduser()
    if not transcripts_dir.is_absolute():
        transcripts_dir = Path(os.path.abspath(str(transcripts_dir)))

    return {
        "enabled": bool(agent_shell.get("enabled", True)),
        "root_dir": str(root_dir),
        "sessions_dir": str(sessions_dir),
        "transcripts_dir": str(transcripts_dir),
    }


def _agent_shell_session_summary_path(settings: dict, session_id: str) -> Path:
    return Path(settings["sessions_dir"]) / f"{session_id}.json"


def _agent_shell_transcript_path(settings: dict, session_id: str) -> Path:
    return Path(settings["transcripts_dir"]) / f"{session_id}.jsonl"


def _read_jsonl_records(path: Path) -> list[dict]:
    if not path.is_file():
        return []

    records: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            records.append(json.loads(stripped))
    return records


def _summarize_agent_shell_turn(turn: dict) -> dict:
    return {
        "turn_id": turn.get("turn_id"),
        "turn_index": turn.get("turn_index"),
        "route": turn.get("route"),
        "runtime_owner": turn.get("runtime_owner"),
        "user_prompt": turn.get("user", {}).get("prompt"),
        "assistant_response": turn.get("assistant", {}).get("response"),
        "error": turn.get("error"),
    }


def _append_execution_envelopes_from_execution_block(
    execution: dict, envelopes: list[dict]
) -> None:
    route = execution.get("route")
    if isinstance(route, dict):
        envelopes.append(copy.deepcopy(route))

    context_providers = execution.get("context_providers")
    if isinstance(context_providers, list):
        for provider in context_providers:
            if isinstance(provider, dict):
                envelopes.append(copy.deepcopy(provider))

    deterministic_tool = execution.get("deterministic_tool")
    if isinstance(deterministic_tool, dict):
        envelopes.append(copy.deepcopy(deterministic_tool))


def describe_agent_shell_sessions(cfg: dict) -> dict:
    settings = _resolve_agent_shell_settings(cfg)
    session_dir = Path(settings["sessions_dir"])
    sessions: list[dict] = []
    errors: list[dict] = []

    if session_dir.is_dir():
        for summary_path in session_dir.glob("*.json"):
            try:
                summary = read_json_file(str(summary_path))
                if not isinstance(summary, dict):
                    raise ValueError("session summary must contain a top-level JSON object")
            except ValueError as exc:
                errors.append(
                    {
                        "session_summary_path": str(summary_path.resolve()),
                        "error": str(exc),
                    }
                )
                continue

            sessions.append(
                {
                    "session_id": str(summary.get("session_id") or summary_path.stem),
                    "session_summary_path": str(summary_path.resolve()),
                    "created_at": summary.get("created_at"),
                    "updated_at": summary.get("updated_at"),
                    "provider": summary.get("provider"),
                    "model": summary.get("model"),
                    "turn_count": int(summary.get("turn_count", 0) or 0),
                    "last_route": summary.get("last_route"),
                    "last_runtime_owner": summary.get("last_runtime_owner"),
                    "route_counts": copy.deepcopy(summary.get("route_counts") or {}),
                }
            )

    sessions.sort(
        key=lambda item: (
            str(item.get("updated_at") or ""),
            str(item.get("session_id") or ""),
        ),
        reverse=True,
    )

    payload = {
        **settings,
        "session_count": len(sessions),
        "sessions": sessions,
    }
    if errors:
        payload["errors"] = errors
    return payload


def describe_agent_shell_session(cfg: dict, session_id: str, *, tail: int = 5) -> dict:
    if tail < 0:
        raise ValueError("tail must be zero or greater")

    settings = _resolve_agent_shell_settings(cfg)
    summary_path = _agent_shell_session_summary_path(settings, session_id)
    if not summary_path.is_file():
        raise ValueError(f"agent shell session not found: {session_id}")

    summary = read_json_file(str(summary_path))
    if not isinstance(summary, dict):
        raise ValueError("session summary must contain a top-level JSON object")

    transcript_path = summary.get("transcript_path")
    if isinstance(transcript_path, str) and transcript_path.strip():
        resolved_transcript_path = Path(transcript_path).expanduser()
        if not resolved_transcript_path.is_absolute():
            resolved_transcript_path = Path(os.path.abspath(str(resolved_transcript_path)))
    else:
        resolved_transcript_path = _agent_shell_transcript_path(settings, session_id)

    turns = _read_jsonl_records(resolved_transcript_path)
    recent_turns = [_summarize_agent_shell_turn(turn) for turn in turns[-max(0, tail) :]]

    envelopes: list[dict] = []
    schema_version = None
    for turn in turns:
        execution = turn.get("execution")
        if not isinstance(execution, dict):
            continue
        if schema_version is None and isinstance(execution.get("schema_version"), int):
            schema_version = execution["schema_version"]
        _append_execution_envelopes_from_execution_block(execution, envelopes)

    return {
        **settings,
        "session_summary_path": str(summary_path.resolve()),
        "transcript_path": str(resolved_transcript_path.resolve()),
        "session": summary,
        "recent_turns": recent_turns,
        "execution": {
            "source": "reconstructed_from_agent_shell_transcript",
            "schema_version": schema_version,
            "summary": summarize_execution_envelopes(envelopes),
        },
    }


def _collect_execution_envelopes(results_payload: dict) -> list[dict]:
    per_example = results_payload.get("per_example")
    if not isinstance(per_example, list):
        return []

    envelopes: list[dict] = []
    for item in per_example:
        if not isinstance(item, dict):
            continue
        execution = item.get("execution")
        if not isinstance(execution, dict):
            continue

        _append_execution_envelopes_from_execution_block(execution, envelopes)

    return envelopes


def summarize_execution_results(results_payload: dict) -> dict:
    execution = results_payload.get("execution")
    if isinstance(execution, dict) and isinstance(execution.get("summary"), dict):
        return {
            "source": "top_level_execution_summary",
            "schema_version": execution.get("schema_version"),
            "summary": copy.deepcopy(execution["summary"]),
        }

    envelopes = _collect_execution_envelopes(results_payload)
    return {
        "source": "reconstructed_from_per_example",
        "schema_version": None,
        "summary": summarize_execution_envelopes(envelopes),
    }


def describe_execution_results(cfg: dict, results_path: str | None = None) -> dict:
    configured_path = results_path
    if configured_path is None:
        evaluation_cfg = cfg.get("evaluation") if isinstance(cfg.get("evaluation"), dict) else {}
        configured_path = evaluation_cfg.get("results_path")
    if not isinstance(configured_path, str) or not configured_path.strip():
        raise ValueError("results path is required")

    resolved_path = os.path.abspath(configured_path)
    if not os.path.isfile(resolved_path):
        raise ValueError(f"results file not found: {resolved_path}")

    payload = read_json_file(resolved_path)
    if not isinstance(payload, dict):
        raise ValueError("results file must contain a top-level JSON object")

    summary = summarize_execution_results(payload)
    return {
        "results_path": resolved_path,
        **summary,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Inspect hook, provider, execution, and agent shell session surfaces "
            "from config and saved artifacts."
        )
    )
    parser.add_argument("--config", default="config.yaml", help="Config file to inspect")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("hooks", help="Inspect configured hook rules")
    subparsers.add_parser("providers", help="Inspect configured context providers")
    execution_parser = subparsers.add_parser("execution", help="Inspect saved execution summaries")
    execution_parser.add_argument(
        "--results",
        help="Optional explicit results JSON path. Defaults to evaluation.results_path from config.",
    )
    shell_parser = subparsers.add_parser(
        "shell",
        help="Inspect saved local agent shell sessions",
    )
    shell_parser.add_argument(
        "--session-id",
        help="Optional session id to inspect. Omit to list saved shell sessions.",
    )
    shell_parser.add_argument(
        "--tail",
        type=int,
        default=5,
        help="Recent turns to include when inspecting one saved shell session.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = load_config(args.config)

    try:
        if args.command == "hooks":
            validate_hooks_config(cfg)
            payload = describe_hooks(cfg)
        elif args.command == "providers":
            validate_context_providers_config(cfg)
            payload = describe_context_providers(cfg)
        elif args.command == "execution":
            payload = describe_execution_results(cfg, args.results)
        elif args.command == "shell":
            validate_agent_shell_config(cfg)
            if args.session_id:
                payload = describe_agent_shell_session(cfg, args.session_id, tail=args.tail)
            else:
                payload = describe_agent_shell_sessions(cfg)
        else:
            raise ValueError(f"unsupported command: {args.command}")
    except ValueError as exc:
        print(f"❌  {exc}")
        return 1

    print(json.dumps(payload, indent=2, sort_keys=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
