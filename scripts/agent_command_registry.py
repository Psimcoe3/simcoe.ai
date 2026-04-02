"""
Shared command registry for the local simcoe.ai agent shell.
"""

from __future__ import annotations

import json
import shlex
from typing import Callable

from agent_skill_registry import (
    describe_agent_skill,
    list_agent_skills,
    list_selected_agent_skills,
    normalize_agent_skill_names,
    resolve_skill_registry_settings,
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
    "tools",
    "providers",
    "route",
    "workflow",
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

    return {"exit": False, "response": f"Unknown command '/{command}'. Use /help."}
