"""
Shared command registry for the local simcoe.ai agent shell.
"""

from __future__ import annotations

import json
import shlex
from typing import Callable

from agent_registry import (
    describe_agent_definition,
    list_agent_definitions,
    resolve_agent_registry_settings,
)
from agent_skill_registry import (
    describe_agent_skill,
    list_agent_skills,
    list_selected_agent_skills,
    normalize_agent_skill_names,
    resolve_skill_registry_settings,
)
from agent_task_manager import (
    TaskManagerError,
    attach_agent_task,
    cancel_agent_task,
    describe_agent_task,
    list_agent_tasks,
    parse_task_vars,
    resume_agent_task,
    start_subagent_task,
    start_dream_task,
    start_workflow_task,
    summarize_agent_tasks,
)
from agent_tool_registry import describe_agent_tool, list_agent_tools
from request_router import route_request
from workflow_registry import WorkflowRegistryError, get_workflow, list_workflows


COMMAND_REGISTRY_SCHEMA_VERSION = 1
COMMAND_KIND_SHELL = "shell_command"
COMMAND_ACCESS_READ_ONLY = "read_only"
COMMAND_ACCESS_SESSION_WRITE = "session_write"

_COMMAND_ORDER = (
    "help",
    "exit",
    "session",
    "commands",
    "skills",
    "agents",
    "tools",
    "providers",
    "route",
    "workflow",
    "tasks",
)

_COMMAND_SPECS = {
    "help": {
        "name": "help",
        "display_name": "Help",
        "description": "Show the current shell command surface and usage hints.",
        "aliases": [],
        "category": "core",
        "usage_examples": ["/help"],
    },
    "exit": {
        "name": "exit",
        "display_name": "Exit",
        "description": "Exit the local agent shell session.",
        "aliases": ["quit"],
        "category": "core",
        "usage_examples": ["/exit", "/quit"],
    },
    "session": {
        "name": "session",
        "display_name": "Session",
        "description": "Inspect the current persisted shell session and recent turns.",
        "aliases": [],
        "category": "inspection",
        "usage_examples": ["/session"],
    },
    "commands": {
        "name": "commands",
        "display_name": "Commands",
        "description": "List shell command metadata or inspect one command definition.",
        "aliases": [],
        "category": "inspection",
        "usage_examples": ["/commands", "/commands list", "/commands show <name>"],
    },
    "skills": {
        "name": "skills",
        "display_name": "Skills",
        "description": "List local markdown skill metadata or inspect one loaded skill.",
        "aliases": [],
        "category": "inspection",
        "access_mode": COMMAND_ACCESS_SESSION_WRITE,
        "usage_examples": [
            "/skills",
            "/skills active",
            "/skills show <name>",
            "/skills pin <name> [<name> ...]",
            "/skills unpin <name> [<name> ...]",
            "/skills use <name> [<name> ...]",
            "/skills clear",
        ],
    },
    "agents": {
        "name": "agents",
        "display_name": "Agents",
        "description": "List local markdown subagent definitions or inspect one named agent.",
        "aliases": [],
        "category": "inspection",
        "access_mode": COMMAND_ACCESS_READ_ONLY,
        "usage_examples": ["/agents", "/agents list", "/agents show <name>"],
    },
    "tools": {
        "name": "tools",
        "display_name": "Tools",
        "description": "List local agent tool metadata or inspect one registered tool.",
        "aliases": [],
        "category": "inspection",
        "access_mode": COMMAND_ACCESS_READ_ONLY,
        "usage_examples": ["/tools", "/tools list", "/tools show <name>"],
    },
    "providers": {
        "name": "providers",
        "display_name": "Providers",
        "description": "Inspect the configured context-provider ordering and activation state.",
        "aliases": [],
        "category": "inspection",
        "access_mode": COMMAND_ACCESS_READ_ONLY,
        "usage_examples": ["/providers"],
    },
    "route": {
        "name": "route",
        "display_name": "Route",
        "description": "Preview the router decision for an instruction without running a turn.",
        "aliases": [],
        "category": "routing",
        "access_mode": COMMAND_ACCESS_READ_ONLY,
        "usage_examples": ["/route <instruction>"],
    },
    "workflow": {
        "name": "workflow",
        "display_name": "Workflow",
        "description": "List checked-in workflows or inspect one workflow definition.",
        "aliases": [],
        "category": "workflow",
        "access_mode": COMMAND_ACCESS_READ_ONLY,
        "usage_examples": ["/workflow list", "/workflow show <name>"],
    },
    "tasks": {
        "name": "tasks",
        "display_name": "Tasks",
        "description": "List, inspect, attach, start, cancel, and resume managed background tasks.",
        "aliases": [],
        "category": "tasks",
        "access_mode": COMMAND_ACCESS_SESSION_WRITE,
        "usage_examples": [
            "/tasks",
            "/tasks status",
            "/tasks list --status running",
            "/tasks show <task-id>",
            "/tasks show <task-id> --tail 10 --transcript-tail 2",
            "/tasks attach <task-id>",
            "/tasks start workflow <name>",
            "/tasks start workflow <name> --var key=value",
            "/tasks start dream",
            '/tasks start subagent --prompt "Summarize the source section."',
            '/tasks start subagent --prompt "Review the answer." --briefing "Check NEC grounding references first."',
            "/tasks cancel <task-id>",
            "/tasks resume <task-id>",
        ],
    },
}

for _command_name in ("help", "exit", "session", "commands"):
    _COMMAND_SPECS[_command_name]["access_mode"] = COMMAND_ACCESS_READ_ONLY


def normalize_agent_command_name(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("command name must be a non-empty string")

    cleaned = value.strip().lstrip("/").lower()
    for command_name in _COMMAND_ORDER:
        spec = _COMMAND_SPECS[command_name]
        if cleaned == command_name:
            return command_name
        aliases = spec.get("aliases") if isinstance(spec.get("aliases"), list) else []
        if cleaned in {str(alias).strip().lower() for alias in aliases}:
            return command_name

    choices = ", ".join(f"/{name}" for name in _COMMAND_ORDER)
    raise ValueError(f"unknown command '{value}'. Available commands: {choices}")


def describe_agent_command(command_name: str) -> dict:
    canonical_name = normalize_agent_command_name(command_name)
    spec = _COMMAND_SPECS[canonical_name]
    return {
        "schema_version": COMMAND_REGISTRY_SCHEMA_VERSION,
        "name": canonical_name,
        "display_name": spec["display_name"],
        "description": spec["description"],
        "kind": COMMAND_KIND_SHELL,
        "access_mode": spec["access_mode"],
        "category": spec["category"],
        "aliases": list(spec["aliases"]),
        "usage_examples": list(spec["usage_examples"]),
    }


def list_agent_commands() -> list[dict]:
    return [describe_agent_command(command_name) for command_name in _COMMAND_ORDER]


def render_agent_command_help() -> str:
    lines = ["Available commands:"]
    for command in list_agent_commands():
        for usage in command["usage_examples"]:
            lines.append(usage)
    lines.extend(
        [
            "",
            "Enter a normal prompt to run the routed shell flow.",
            "Use --session-id from the CLI to resume a saved session.",
        ]
    )
    return "\n".join(lines)


def _list_commands_payload() -> dict:
    commands = list_agent_commands()
    return {
        "command_count": len(commands),
        "commands": commands,
    }


def _session_skill_names(session_summary: dict, field_name: str) -> list[str]:
    raw_value = session_summary.get(field_name)
    if not isinstance(raw_value, list):
        return []

    cleaned: list[str] = []
    seen: set[str] = set()
    for item in raw_value:
        if not isinstance(item, str) or not item.strip():
            continue
        candidate = item.strip()
        if candidate in seen:
            continue
        cleaned.append(candidate)
        seen.add(candidate)
    return cleaned


def _render_active_skills_payload(cfg: dict, session_summary: dict) -> dict:
    settings_payload = resolve_skill_registry_settings(cfg)
    pinned_skill_names = _session_skill_names(session_summary, "pinned_skills")
    next_turn_skill_names = _session_skill_names(session_summary, "next_turn_skills")
    return {
        "enabled": settings_payload["enabled"],
        "root_dir": settings_payload["root_dir"],
        "max_active_skills": settings_payload["max_active_skills"],
        "max_instruction_chars": settings_payload["max_instruction_chars"],
        "session_id": session_summary.get("session_id"),
        "pinned_skill_names": pinned_skill_names,
        "next_turn_skill_names": next_turn_skill_names,
        "pinned_skills": list_selected_agent_skills(cfg, pinned_skill_names),
        "next_turn_skills": list_selected_agent_skills(cfg, next_turn_skill_names),
    }


def _parse_task_list_options(option_args: list[str]) -> dict[str, str | None]:
    parsed: dict[str, str | None] = {
        "kind": None,
        "status": None,
        "source": None,
    }
    index = 0
    while index < len(option_args):
        if index + 1 >= len(option_args):
            raise ValueError(
                "Usage: /tasks list [--kind <kind>] [--status <status>] [--source <source>]"
            )
        flag = option_args[index].lower()
        value = option_args[index + 1]
        if flag == "--kind":
            parsed["kind"] = value
        elif flag == "--status":
            parsed["status"] = value
        elif flag == "--source":
            parsed["source"] = value
        else:
            raise ValueError(
                "Usage: /tasks list [--kind <kind>] [--status <status>] [--source <source>]"
            )
        index += 2
    return parsed


def _parse_task_status_options(option_args: list[str]) -> dict[str, str | int | None]:
    parsed: dict[str, str | int | None] = {
        "kind": None,
        "status": None,
        "source": None,
        "recent_limit": 5,
    }
    index = 0
    while index < len(option_args):
        if index + 1 >= len(option_args):
            raise ValueError(
                "Usage: /tasks status [--kind <kind>] [--status <status>] [--source <source>] [--recent-limit <count>]"
            )
        flag = option_args[index].lower()
        value = option_args[index + 1]
        if flag == "--kind":
            parsed["kind"] = value
        elif flag == "--status":
            parsed["status"] = value
        elif flag == "--source":
            parsed["source"] = value
        elif flag == "--recent-limit":
            try:
                parsed["recent_limit"] = int(value)
            except ValueError as exc:
                raise ValueError("/tasks status --recent-limit must be an integer") from exc
        else:
            raise ValueError(
                "Usage: /tasks status [--kind <kind>] [--status <status>] [--source <source>] [--recent-limit <count>]"
            )
        index += 2
    return parsed


def _parse_task_attach_options(option_args: list[str]) -> dict[str, int]:
    parsed = {
        "cursor": 0,
        "limit": 20,
    }
    index = 0
    while index < len(option_args):
        if index + 1 >= len(option_args):
            raise ValueError("Usage: /tasks attach <task-id> [--cursor <cursor>] [--limit <count>]")
        flag = option_args[index].lower()
        value = option_args[index + 1]
        if flag == "--cursor":
            try:
                parsed["cursor"] = int(value)
            except ValueError as exc:
                raise ValueError("/tasks attach --cursor must be an integer") from exc
        elif flag == "--limit":
            try:
                parsed["limit"] = int(value)
            except ValueError as exc:
                raise ValueError("/tasks attach --limit must be an integer") from exc
        else:
            raise ValueError("Usage: /tasks attach <task-id> [--cursor <cursor>] [--limit <count>]")
        index += 2
    return parsed


def _parse_task_show_options(option_args: list[str]) -> dict[str, int | None]:
    parsed: dict[str, int | None] = {
        "tail": 20,
        "transcript_tail": None,
    }
    index = 0
    while index < len(option_args):
        if index + 1 >= len(option_args):
            raise ValueError(
                "Usage: /tasks show <task-id> [--tail <count>] [--transcript-tail <count>]"
            )
        flag = option_args[index].lower()
        value = option_args[index + 1]
        if flag == "--tail":
            try:
                parsed["tail"] = int(value)
            except ValueError as exc:
                raise ValueError("/tasks show --tail must be an integer") from exc
        elif flag == "--transcript-tail":
            try:
                parsed["transcript_tail"] = int(value)
            except ValueError as exc:
                raise ValueError("/tasks show --transcript-tail must be an integer") from exc
        else:
            raise ValueError(
                "Usage: /tasks show <task-id> [--tail <count>] [--transcript-tail <count>]"
            )
        index += 2
    return parsed


def _parse_task_subagent_options(option_args: list[str]) -> dict[str, object]:
    parsed: dict[str, object] = {
        "agent_definition_name": None,
        "prompt": None,
        "source": "agent_shell_subagent",
        "section": None,
        "attachments": [],
        "skill_names": [],
        "tool_name": None,
        "parent_task_id": None,
        "delegation_briefing": None,
        "agent_name": None,
        "allowed_routes": [],
    }
    index = 0
    while index < len(option_args):
        if index + 1 >= len(option_args):
            raise ValueError(
                "Usage: /tasks start subagent --prompt <prompt> [--agent <name>] [--source <source>] [--section <section>] [--attachment <path>] [--skill <name>] [--tool-name <tool>] [--parent-task-id <task-id>] [--briefing <text>] [--agent-name <name>] [--allow-route <route>]"
            )
        flag = option_args[index].lower()
        value = option_args[index + 1]
        if flag == "--agent":
            parsed["agent_definition_name"] = value
        elif flag == "--prompt":
            parsed["prompt"] = value
        elif flag == "--source":
            parsed["source"] = value
        elif flag == "--section":
            parsed["section"] = value
        elif flag == "--attachment":
            parsed["attachments"].append(value)
        elif flag == "--skill":
            parsed["skill_names"].append(value)
        elif flag == "--tool-name":
            parsed["tool_name"] = value
        elif flag == "--parent-task-id":
            parsed["parent_task_id"] = value
        elif flag == "--briefing":
            parsed["delegation_briefing"] = value
        elif flag == "--agent-name":
            parsed["agent_name"] = value
        elif flag == "--allow-route":
            parsed["allowed_routes"].append(value)
        else:
            raise ValueError(
                "Usage: /tasks start subagent --prompt <prompt> [--agent <name>] [--source <source>] [--section <section>] [--attachment <path>] [--skill <name>] [--tool-name <tool>] [--parent-task-id <task-id>] [--briefing <text>] [--agent-name <name>] [--allow-route <route>]"
            )
        index += 2

    if not isinstance(parsed["prompt"], str) or not str(parsed["prompt"]).strip():
        raise ValueError(
            "Usage: /tasks start subagent --prompt <prompt> [--agent <name>] [--source <source>] [--section <section>] [--attachment <path>] [--skill <name>] [--tool-name <tool>] [--parent-task-id <task-id>] [--briefing <text>] [--agent-name <name>] [--allow-route <route>]"
        )
    return parsed


def execute_agent_command(
    cfg: dict,
    settings: dict,
    session_summary: dict,
    raw_prompt: str,
    *,
    describe_session_fn: Callable[[dict, str], dict],
    describe_context_providers_fn: Callable[[dict], dict],
    update_session_skills_fn: Callable[[dict, dict, list[str] | None, list[str] | None], dict]
    | None = None,
) -> dict | None:
    if not raw_prompt.startswith("/"):
        return None

    try:
        parts = shlex.split(raw_prompt)
    except ValueError as exc:
        return {"exit": False, "response": f"Command parse error: {exc}"}

    if not parts:
        return {"exit": False, "response": render_agent_command_help()}

    try:
        command = normalize_agent_command_name(parts[0])
    except ValueError:
        return {
            "exit": False,
            "response": f"Unknown command '{parts[0].lower()}'. Use /help.",
        }

    if command == "exit":
        return {"exit": True, "response": "Exiting agent shell."}
    if command == "help":
        return {"exit": False, "response": render_agent_command_help()}
    if command == "session":
        payload = describe_session_fn(settings, session_summary["session_id"])
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "commands":
        if len(parts) == 1 or (len(parts) >= 2 and parts[1].lower() == "list"):
            payload = _list_commands_payload()
        elif len(parts) >= 3 and parts[1].lower() == "show":
            try:
                payload = describe_agent_command(parts[2])
            except ValueError as exc:
                return {"exit": False, "response": str(exc)}
        else:
            return {
                "exit": False,
                "response": "Usage: /commands | /commands list | /commands show <name>",
            }
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "skills":
        try:
            if len(parts) == 1 or (len(parts) >= 2 and parts[1].lower() == "list"):
                settings_payload = resolve_skill_registry_settings(cfg)
                skills = list_agent_skills(cfg)
                payload = {
                    "enabled": settings_payload["enabled"],
                    "root_dir": settings_payload["root_dir"],
                    "max_active_skills": settings_payload["max_active_skills"],
                    "max_instruction_chars": settings_payload["max_instruction_chars"],
                    "skill_count": len(skills),
                    "pinned_skill_names": _session_skill_names(session_summary, "pinned_skills"),
                    "next_turn_skill_names": _session_skill_names(
                        session_summary,
                        "next_turn_skills",
                    ),
                    "skills": skills,
                }
            elif len(parts) >= 2 and parts[1].lower() == "active":
                payload = _render_active_skills_payload(cfg, session_summary)
            elif len(parts) >= 3 and parts[1].lower() == "show":
                payload = describe_agent_skill(cfg, parts[2])
            elif len(parts) >= 3 and parts[1].lower() == "pin":
                if update_session_skills_fn is None:
                    return {
                        "exit": False,
                        "response": "Skill pinning is unavailable in this shell context.",
                    }
                settings_payload = resolve_skill_registry_settings(cfg)
                requested_names = normalize_agent_skill_names(cfg, parts[2:])
                combined_names = _session_skill_names(session_summary, "pinned_skills")
                for skill_name in requested_names:
                    if skill_name not in combined_names:
                        combined_names.append(skill_name)
                if len(combined_names) > int(settings_payload["max_active_skills"]):
                    return {
                        "exit": False,
                        "response": (
                            "Pinned skills exceed max_active_skills "
                            f"({settings_payload['max_active_skills']})."
                        ),
                    }
                updated_summary = update_session_skills_fn(
                    settings,
                    session_summary,
                    combined_names,
                    None,
                )
                payload = _render_active_skills_payload(cfg, updated_summary)
                return {
                    "exit": False,
                    "response": json.dumps(payload, indent=2, sort_keys=False),
                    "session_summary": updated_summary,
                }
            elif len(parts) >= 3 and parts[1].lower() == "unpin":
                if update_session_skills_fn is None:
                    return {
                        "exit": False,
                        "response": "Skill pinning is unavailable in this shell context.",
                    }
                requested_names = set(normalize_agent_skill_names(cfg, parts[2:]))
                remaining_names = [
                    skill_name
                    for skill_name in _session_skill_names(session_summary, "pinned_skills")
                    if skill_name not in requested_names
                ]
                updated_summary = update_session_skills_fn(
                    settings,
                    session_summary,
                    remaining_names,
                    None,
                )
                payload = _render_active_skills_payload(cfg, updated_summary)
                return {
                    "exit": False,
                    "response": json.dumps(payload, indent=2, sort_keys=False),
                    "session_summary": updated_summary,
                }
            elif len(parts) >= 3 and parts[1].lower() == "use":
                if update_session_skills_fn is None:
                    return {
                        "exit": False,
                        "response": "One-turn skill selection is unavailable in this shell context.",
                    }
                settings_payload = resolve_skill_registry_settings(cfg)
                requested_names = normalize_agent_skill_names(
                    cfg,
                    parts[2:],
                    max_count=int(settings_payload["max_active_skills"]),
                )
                updated_summary = update_session_skills_fn(
                    settings,
                    session_summary,
                    None,
                    requested_names,
                )
                payload = _render_active_skills_payload(cfg, updated_summary)
                return {
                    "exit": False,
                    "response": json.dumps(payload, indent=2, sort_keys=False),
                    "session_summary": updated_summary,
                }
            elif len(parts) >= 2 and parts[1].lower() == "clear":
                if update_session_skills_fn is None:
                    return {
                        "exit": False,
                        "response": "Skill state clearing is unavailable in this shell context.",
                    }
                updated_summary = update_session_skills_fn(settings, session_summary, [], [])
                payload = _render_active_skills_payload(cfg, updated_summary)
                return {
                    "exit": False,
                    "response": json.dumps(payload, indent=2, sort_keys=False),
                    "session_summary": updated_summary,
                }
            else:
                return {
                    "exit": False,
                    "response": (
                        "Usage: /skills | /skills list | /skills active | /skills show <name> "
                        "| /skills pin <name> [<name> ...] | /skills unpin <name> [<name> ...] "
                        "| /skills use <name> [<name> ...] | /skills clear"
                    ),
                }
        except ValueError as exc:
            return {"exit": False, "response": str(exc)}
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "agents":
        try:
            if len(parts) == 1 or (len(parts) >= 2 and parts[1].lower() == "list"):
                settings_payload = resolve_agent_registry_settings(cfg)
                agents = list_agent_definitions(cfg)
                payload = {
                    "enabled": settings_payload["enabled"],
                    "root_dir": settings_payload["root_dir"],
                    "agent_count": len(agents),
                    "agents": agents,
                }
            elif len(parts) >= 3 and parts[1].lower() == "show":
                payload = describe_agent_definition(cfg, parts[2])
            else:
                return {
                    "exit": False,
                    "response": "Usage: /agents | /agents list | /agents show <name>",
                }
        except ValueError as exc:
            return {"exit": False, "response": str(exc)}
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "tools":
        if len(parts) == 1 or (len(parts) >= 2 and parts[1].lower() == "list"):
            tools = list_agent_tools(cfg)
            payload = {
                "tool_count": len(tools),
                "enabled_count": sum(1 for tool in tools if tool["enabled"]),
                "tools": tools,
            }
        elif len(parts) >= 3 and parts[1].lower() == "show":
            try:
                payload = describe_agent_tool(cfg, parts[2])
            except ValueError as exc:
                return {"exit": False, "response": str(exc)}
        else:
            return {"exit": False, "response": "Usage: /tools | /tools list | /tools show <name>"}
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "providers":
        payload = describe_context_providers_fn(cfg)
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "route":
        if len(parts) < 2:
            return {"exit": False, "response": "Usage: /route <instruction>"}
        instruction = raw_prompt.split(None, 1)[1]
        try:
            payload = route_request(cfg, instruction)
        except ValueError as exc:
            return {"exit": False, "response": f"Routing error: {exc}"}
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "workflow":
        if len(parts) < 2:
            return {
                "exit": False,
                "response": "Usage: /workflow list | /workflow show <name>",
            }
        subcommand = parts[1].lower()
        try:
            if subcommand == "list":
                payload = list_workflows(cfg)
            elif subcommand == "show" and len(parts) >= 3:
                payload = get_workflow(cfg, parts[2])
            else:
                return {
                    "exit": False,
                    "response": "Usage: /workflow list | /workflow show <name>",
                }
        except WorkflowRegistryError as exc:
            return {"exit": False, "response": str(exc)}
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "tasks":
        config_path = (
            str(session_summary.get("config_path") or "config.yaml")
            if isinstance(session_summary, dict)
            else "config.yaml"
        )
        try:
            if len(parts) == 1:
                payload = list_agent_tasks(cfg)
            elif len(parts) >= 2 and parts[1].lower() == "list":
                options = _parse_task_list_options(parts[2:])
                payload = list_agent_tasks(
                    cfg,
                    task_kind=options["kind"],
                    task_status=options["status"],
                    task_source=options["source"],
                )
            elif len(parts) >= 2 and parts[1].lower() == "status":
                options = _parse_task_status_options(parts[2:])
                payload = summarize_agent_tasks(
                    cfg,
                    task_kind=options["kind"],
                    task_status=options["status"],
                    task_source=options["source"],
                    recent_limit=int(options["recent_limit"] or 5),
                )
            elif len(parts) >= 3 and parts[1].lower() == "show":
                options = _parse_task_show_options(parts[3:])
                payload = describe_agent_task(
                    cfg,
                    parts[2],
                    tail=int(options["tail"] or 20),
                    transcript_tail=options["transcript_tail"],
                )
            elif len(parts) >= 3 and parts[1].lower() == "attach":
                options = _parse_task_attach_options(parts[3:])
                payload = attach_agent_task(
                    cfg,
                    parts[2],
                    cursor=int(options["cursor"]),
                    limit=int(options["limit"]),
                )
            elif len(parts) >= 3 and parts[1].lower() == "start":
                task_kind = parts[2].lower()
                if task_kind == "workflow":
                    if len(parts) < 4:
                        return {
                            "exit": False,
                            "response": ("Usage: /tasks start workflow <name> [--var key=value]"),
                        }
                    workflow_name = parts[3]
                    extra_args = parts[4:]
                    if len(extra_args) % 2 != 0 or any(
                        extra_args[index] != "--var" for index in range(0, len(extra_args), 2)
                    ):
                        return {
                            "exit": False,
                            "response": ("Usage: /tasks start workflow <name> [--var key=value]"),
                        }
                    payload = start_workflow_task(
                        cfg,
                        config_path,
                        workflow_name,
                        parse_task_vars(extra_args[1::2]),
                        source="agent_shell",
                    )
                elif task_kind == "dream" and len(parts) == 3:
                    payload = start_dream_task(
                        cfg,
                        config_path,
                        source="agent_shell",
                    )
                elif task_kind == "subagent":
                    options = _parse_task_subagent_options(parts[3:])
                    payload = start_subagent_task(
                        cfg,
                        config_path,
                        str(options["prompt"]),
                        agent_definition_name=(
                            str(options["agent_definition_name"])
                            if isinstance(options["agent_definition_name"], str)
                            and str(options["agent_definition_name"]).strip()
                            else None
                        ),
                        source=str(options["source"]),
                        section=(
                            str(options["section"])
                            if isinstance(options["section"], str)
                            and str(options["section"]).strip()
                            else None
                        ),
                        attachments=list(options["attachments"]),
                        explicit_skill_names=list(options["skill_names"]),
                        explicit_tool_name=(
                            str(options["tool_name"])
                            if isinstance(options["tool_name"], str)
                            and str(options["tool_name"]).strip()
                            else None
                        ),
                        parent_task_id=(
                            str(options["parent_task_id"])
                            if isinstance(options["parent_task_id"], str)
                            and str(options["parent_task_id"]).strip()
                            else None
                        ),
                        delegation_briefing=(
                            str(options["delegation_briefing"])
                            if isinstance(options["delegation_briefing"], str)
                            and str(options["delegation_briefing"]).strip()
                            else None
                        ),
                        agent_name=(
                            str(options["agent_name"])
                            if isinstance(options["agent_name"], str)
                            and str(options["agent_name"]).strip()
                            else None
                        ),
                        allowed_routes=list(options["allowed_routes"]),
                    )
                else:
                    return {
                        "exit": False,
                        "response": (
                            "Usage: /tasks start workflow <name> [--var key=value] "
                            "| /tasks start dream "
                            "| /tasks start subagent --prompt <prompt> [--agent <name>] [--source <source>] [--section <section>] [--attachment <path>] [--skill <name>] [--tool-name <tool>] [--parent-task-id <task-id>] [--agent-name <name>] [--allow-route <route>]"
                        ),
                    }
            elif len(parts) >= 3 and parts[1].lower() == "cancel":
                payload = cancel_agent_task(cfg, parts[2])
            elif len(parts) >= 3 and parts[1].lower() == "resume":
                payload = resume_agent_task(cfg, parts[2], source="agent_shell_resume")
            else:
                return {
                    "exit": False,
                    "response": (
                        "Usage: /tasks | /tasks list [--kind <kind>] [--status <status>] [--source <source>] "
                        "| /tasks status [--kind <kind>] [--status <status>] [--source <source>] [--recent-limit <count>] "
                        "| /tasks show <task-id> [--tail <count>] [--transcript-tail <count>] "
                        "| /tasks attach <task-id> [--cursor <cursor>] [--limit <count>] "
                        "| /tasks start workflow <name> [--var key=value] "
                        "| /tasks start dream "
                        "| /tasks start subagent --prompt <prompt> [--agent <name>] [--source <source>] [--section <section>] [--attachment <path>] [--skill <name>] [--tool-name <tool>] [--parent-task-id <task-id>] [--agent-name <name>] [--allow-route <route>] "
                        "| /tasks cancel <task-id> | /tasks resume <task-id>"
                    ),
                }
        except (TaskManagerError, WorkflowRegistryError, ValueError) as exc:
            return {"exit": False, "response": str(exc)}
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}

    return {"exit": False, "response": f"Unknown command '/{command}'. Use /help."}
