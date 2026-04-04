from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path

from agent_registry import (
    describe_agent_definition,
    list_agent_definitions,
    resolve_agent_registry_settings,
)
from agent_command_registry import describe_agent_command, list_agent_commands
from agent_skill_registry import (
    describe_agent_skill,
    list_agent_skills,
    resolve_skill_registry_settings,
)
from agent_task_manager import describe_agent_task, list_agent_tasks
from agent_tool_registry import describe_agent_tool, list_agent_tools
from config_validation import (
    validate_agent_registry_config,
    validate_agent_shell_config,
    validate_agent_task_manager_config,
    validate_deterministic_tools_config,
    load_config,
    validate_context_providers_config,
    validate_hooks_config,
    validate_skill_registry_config,
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


def describe_agent_commands(command_name: str | None = None) -> dict:
    if isinstance(command_name, str) and command_name.strip():
        return describe_agent_command(command_name)

    commands = list_agent_commands()
    return {
        "command_count": len(commands),
        "commands": commands,
    }


def describe_agent_skills(cfg: dict, skill_name: str | None = None) -> dict:
    if isinstance(skill_name, str) and skill_name.strip():
        return describe_agent_skill(cfg, skill_name)

    settings = resolve_skill_registry_settings(cfg)
    skills = list_agent_skills(cfg)
    return {
        "enabled": settings["enabled"],
        "root_dir": settings["root_dir"],
        "max_active_skills": settings["max_active_skills"],
        "max_instruction_chars": settings["max_instruction_chars"],
        "skill_count": len(skills),
        "skills": skills,
    }


def describe_agent_agents(cfg: dict, agent_name: str | None = None) -> dict:
    if isinstance(agent_name, str) and agent_name.strip():
        return describe_agent_definition(cfg, agent_name)

    settings = resolve_agent_registry_settings(cfg)
    agents = list_agent_definitions(cfg)
    return {
        "enabled": settings["enabled"],
        "root_dir": settings["root_dir"],
        "agent_count": len(agents),
        "agents": agents,
    }


def describe_agent_tools(cfg: dict, tool_name: str | None = None) -> dict:
    if isinstance(tool_name, str) and tool_name.strip():
        return describe_agent_tool(cfg, tool_name)

    tools = list_agent_tools(cfg)
    return {
        "tool_count": len(tools),
        "enabled_count": sum(1 for tool in tools if tool["enabled"]),
        "tools": tools,
    }


def describe_agent_tasks(
    cfg: dict,
    task_id: str | None = None,
    *,
    tail: int = 20,
    transcript_tail: int | None = None,
) -> dict:
    if isinstance(task_id, str) and task_id.strip():
        return describe_agent_task(cfg, task_id, tail=tail, transcript_tail=transcript_tail)

    return list_agent_tasks(cfg)


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

    history_turn_window = agent_shell.get("history_turn_window")
    if isinstance(history_turn_window, bool) or not isinstance(history_turn_window, int):
        history_turn_window = 6
    elif history_turn_window <= 0:
        history_turn_window = 6

    return {
        "enabled": bool(agent_shell.get("enabled", True)),
        "root_dir": str(root_dir),
        "sessions_dir": str(sessions_dir),
        "transcripts_dir": str(transcripts_dir),
        "history_turn_window": history_turn_window,
    }


def _agent_shell_history_turn_window(settings: dict, summary: dict | None = None) -> int:
    if isinstance(summary, dict):
        value = summary.get("history_turn_window")
        if isinstance(value, int) and not isinstance(value, bool) and value > 0:
            return value
    value = settings.get("history_turn_window")
    if isinstance(value, int) and not isinstance(value, bool) and value > 0:
        return value
    return 6


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
        "skill_names": [
            skill.get("name")
            for skill in turn.get("skills", [])
            if isinstance(skill, dict) and isinstance(skill.get("name"), str)
        ],
        "error": turn.get("error"),
    }


def _agent_shell_history_overview(
    *,
    turn_count: int,
    history_turn_window: int,
    history_summary_text: str | None,
    history_summary_turn_count: int,
) -> dict:
    recent_turn_window = max(1, int(history_turn_window or 0))
    safe_turn_count = max(0, int(turn_count or 0))
    recent_turn_count = min(safe_turn_count, recent_turn_window)
    safe_summary_turn_count = min(
        max(0, int(history_summary_turn_count or 0)),
        max(0, safe_turn_count - recent_turn_count),
    )
    summary_text = history_summary_text.strip() if isinstance(history_summary_text, str) else ""
    return {
        "recent_turn_window": recent_turn_window,
        "recent_turn_count": recent_turn_count,
        "summary_turn_count": safe_summary_turn_count,
        "omitted_turn_count": max(0, safe_turn_count - recent_turn_count - safe_summary_turn_count),
        "has_summary": bool(summary_text),
        "summary_char_count": len(summary_text),
    }


def _agent_shell_history_message_count_for_window(
    turns: list[dict],
    *,
    history_turn_window: int,
    has_summary: bool,
) -> int:
    count = 1 if has_summary else 0
    for turn in turns[-max(1, history_turn_window) :]:
        user_prompt = (
            turn.get("user", {}).get("prompt") if isinstance(turn.get("user"), dict) else None
        )
        assistant_response = (
            turn.get("assistant", {}).get("response")
            if isinstance(turn.get("assistant"), dict)
            else None
        )
        if isinstance(user_prompt, str) and user_prompt.strip():
            count += 1
        if isinstance(assistant_response, str) and assistant_response.strip():
            count += 1
    return count


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

            history_turn_window = _agent_shell_history_turn_window(settings, summary)
            history_overview = _agent_shell_history_overview(
                turn_count=int(summary.get("turn_count", 0) or 0),
                history_turn_window=history_turn_window,
                history_summary_text=(
                    summary.get("history_summary_text")
                    if isinstance(summary.get("history_summary_text"), str)
                    else None
                ),
                history_summary_turn_count=int(summary.get("history_summary_turn_count", 0) or 0),
            )

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
                    "last_skill_names": copy.deepcopy(summary.get("last_skill_names") or []),
                    "pinned_skills": copy.deepcopy(summary.get("pinned_skills") or []),
                    "next_turn_skills": copy.deepcopy(summary.get("next_turn_skills") or []),
                    "history_summary_turn_count": int(
                        summary.get("history_summary_turn_count", 0) or 0
                    ),
                    "has_history_summary": bool(summary.get("history_summary_text")),
                    "history_recent_turn_window": history_overview["recent_turn_window"],
                    "history_recent_turn_count": history_overview["recent_turn_count"],
                    "history_omitted_turn_count": history_overview["omitted_turn_count"],
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
    history_turn_window = _agent_shell_history_turn_window(settings, summary)
    history = _agent_shell_history_overview(
        turn_count=len(turns),
        history_turn_window=history_turn_window,
        history_summary_text=(
            summary.get("history_summary_text")
            if isinstance(summary.get("history_summary_text"), str)
            else None
        ),
        history_summary_turn_count=int(summary.get("history_summary_turn_count", 0) or 0),
    )
    history["message_count"] = _agent_shell_history_message_count_for_window(
        turns,
        history_turn_window=history_turn_window,
        has_summary=bool(history["has_summary"]),
    )

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
        "history": history,
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
            "Inspect hook, provider, command, skill, agent, tool, task, execution, and agent shell session surfaces "
            "from config and saved artifacts."
        )
    )
    parser.add_argument("--config", default="config.yaml", help="Config file to inspect")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("hooks", help="Inspect configured hook rules")
    subparsers.add_parser("providers", help="Inspect configured context providers")
    commands_parser = subparsers.add_parser(
        "commands",
        help="Inspect local agent shell command metadata",
    )
    commands_parser.add_argument(
        "--command-name",
        help="Optional command name to inspect. Omit to list the local command registry.",
    )
    skills_parser = subparsers.add_parser(
        "skills",
        help="Inspect local markdown skill metadata",
    )
    skills_parser.add_argument(
        "--skill-name",
        help="Optional skill name to inspect. Omit to list the local skill registry.",
    )
    tools_parser = subparsers.add_parser("tools", help="Inspect configured local agent tools")
    tools_parser.add_argument(
        "--tool-name",
        help="Optional tool name to inspect. Omit to list the local tool registry.",
    )
    tasks_parser = subparsers.add_parser("tasks", help="Inspect managed background tasks")
    tasks_parser.add_argument(
        "--task-id",
        help="Optional task id to inspect. Omit to list saved tasks.",
    )
    tasks_parser.add_argument(
        "--tail",
        type=int,
        default=20,
        help="Recent log lines to include when inspecting one saved task.",
    )
    tasks_parser.add_argument(
        "--transcript-tail",
        type=int,
        help="Recent structured transcript records to include. Defaults to --tail.",
    )
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
    agents_parser = subparsers.add_parser("agents", help="Inspect local named agent definitions")
    agents_parser.add_argument(
        "--agent-name",
        help="Optional agent definition name to inspect. Omit to list the local agent registry.",
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
        elif args.command == "commands":
            payload = describe_agent_commands(args.command_name)
        elif args.command == "skills":
            validate_skill_registry_config(cfg)
            payload = describe_agent_skills(cfg, args.skill_name)
        elif args.command == "agents":
            validate_agent_registry_config(cfg)
            payload = describe_agent_agents(cfg, args.agent_name)
        elif args.command == "tools":
            validate_deterministic_tools_config(cfg)
            payload = describe_agent_tools(cfg, args.tool_name)
        elif args.command == "tasks":
            validate_agent_task_manager_config(cfg)
            payload = describe_agent_tasks(
                cfg,
                args.task_id,
                tail=args.tail,
                transcript_tail=args.transcript_tail,
            )
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
