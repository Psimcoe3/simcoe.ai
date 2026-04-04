"""
Shared markdown-backed agent registry for local simcoe.ai subagents.
"""

from __future__ import annotations

import copy
from pathlib import Path

import yaml

from agent_skill_registry import normalize_agent_skill_names
from runtime_contracts import ROUTE_DETERMINISTIC_TOOL, normalize_route


REPO_ROOT = Path(__file__).resolve().parents[1]
AGENT_REGISTRY_SCHEMA_VERSION = 1


class AgentRegistryError(ValueError):
    pass


def resolve_agent_registry_settings(cfg: dict) -> dict:
    agent_registry = (
        cfg.get("agent_registry") if isinstance(cfg.get("agent_registry"), dict) else {}
    )
    root_dir = str(agent_registry.get("root_dir") or "agents")

    candidate = Path(root_dir).expanduser()
    if not candidate.is_absolute():
        candidate = REPO_ROOT / candidate

    return {
        "enabled": bool(agent_registry.get("enabled", False)),
        "root_dir": str(candidate.resolve()),
    }


def _require_non_empty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise AgentRegistryError(f"{label} must be a non-empty string")
    return value.strip()


def _require_optional_string(value: object, label: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise AgentRegistryError(f"{label} must be a string when present")
    cleaned = value.strip()
    return cleaned or None


def _require_string_list(value: object, label: str, *, allow_empty: bool = True) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise AgentRegistryError(f"{label} must be a list of strings")
    if not value and not allow_empty:
        raise AgentRegistryError(f"{label} must not be empty")
    return [_require_non_empty_string(item, label) for item in value]


def _normalize_lookup_token(value: str) -> str:
    return " ".join(value.strip().lower().replace("_", " ").replace("-", " ").split())


def _split_frontmatter(path: Path, content: str) -> tuple[dict, str]:
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        raise AgentRegistryError(f"agent file must start with YAML frontmatter: {path}")

    closing_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        raise AgentRegistryError(f"agent file is missing closing YAML frontmatter fence: {path}")

    frontmatter_text = "\n".join(lines[1:closing_index])
    body = "\n".join(lines[closing_index + 1 :]).strip()
    if not body:
        raise AgentRegistryError(f"agent file must contain non-empty instruction content: {path}")

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        raise AgentRegistryError(f"could not parse agent frontmatter '{path}': {exc}") from exc

    if not isinstance(frontmatter, dict):
        raise AgentRegistryError(f"agent frontmatter must be a mapping: {path}")

    return frontmatter, body


def _normalize_allowed_routes(
    value: object,
    label: str,
    *,
    explicit_tool_name: str | None,
) -> list[str]:
    allowed_routes = _require_string_list(value, label)
    normalized: list[str] = []
    for route_name in allowed_routes:
        try:
            normalized_route = normalize_route(route_name, label)
        except ValueError as exc:
            raise AgentRegistryError(str(exc)) from exc
        if normalized_route == ROUTE_DETERMINISTIC_TOOL and not explicit_tool_name:
            raise AgentRegistryError(f"{label} cannot include deterministic_tool without tool_name")
        normalized.append(normalized_route)

    if len(set(normalized)) != len(normalized):
        raise AgentRegistryError(f"{label} must not contain duplicates")
    return normalized


def _agent_payload(agent: dict, *, include_instructions: bool) -> dict:
    payload = {
        "schema_version": AGENT_REGISTRY_SCHEMA_VERSION,
        "registry_enabled": bool(agent["registry_enabled"]),
        "name": agent["name"],
        "title": agent["title"],
        "summary": agent["summary"],
        "aliases": copy.deepcopy(agent["aliases"]),
        "skill_names": copy.deepcopy(agent["skill_names"]),
        "allowed_routes": copy.deepcopy(agent["allowed_routes"]),
        "tool_name": agent["tool_name"],
        "section": agent["section"],
        "use_when": copy.deepcopy(agent["use_when"]),
        "avoid_when": copy.deepcopy(agent["avoid_when"]),
        "path": agent["path"],
        "relative_path": agent["relative_path"],
        "instruction_chars": int(agent["instruction_chars"]),
    }
    if include_instructions:
        payload["instructions"] = agent["instructions"]
    return payload


def _load_agent_file(path: Path, *, registry_enabled: bool, root_dir: Path, cfg: dict) -> dict:
    content = path.read_text(encoding="utf-8")
    frontmatter, instructions = _split_frontmatter(path, content)

    agent_name = _require_non_empty_string(frontmatter.get("id"), f"{path}.id").lower()
    title = _require_non_empty_string(frontmatter.get("title"), f"{path}.title")
    summary = _require_non_empty_string(frontmatter.get("summary"), f"{path}.summary")
    aliases = _require_string_list(frontmatter.get("aliases", []), f"{path}.aliases")
    skill_names_raw = _require_string_list(
        frontmatter.get("skill_names", []), f"{path}.skill_names"
    )
    tool_name = _require_optional_string(frontmatter.get("tool_name"), f"{path}.tool_name")
    section = _require_optional_string(frontmatter.get("section"), f"{path}.section")
    use_when = _require_string_list(frontmatter.get("use_when", []), f"{path}.use_when")
    avoid_when = _require_string_list(frontmatter.get("avoid_when", []), f"{path}.avoid_when")
    allowed_routes = _normalize_allowed_routes(
        frontmatter.get("allowed_routes", []),
        f"{path}.allowed_routes",
        explicit_tool_name=tool_name,
    )

    return {
        "registry_enabled": registry_enabled,
        "name": agent_name,
        "title": title,
        "summary": summary,
        "aliases": aliases,
        "skill_names": normalize_agent_skill_names(cfg, skill_names_raw) if skill_names_raw else [],
        "allowed_routes": allowed_routes,
        "tool_name": tool_name,
        "section": section,
        "use_when": use_when,
        "avoid_when": avoid_when,
        "path": str(path.resolve()),
        "relative_path": str(path.resolve().relative_to(root_dir.resolve())),
        "instruction_chars": len(instructions),
        "instructions": instructions,
    }


def load_agent_registry(cfg: dict) -> dict:
    settings = resolve_agent_registry_settings(cfg)
    root_dir = Path(settings["root_dir"])
    if not root_dir.is_dir():
        raise AgentRegistryError(f"agent registry directory not found: {root_dir}")

    agents: dict[str, dict] = {}
    lookup: dict[str, str] = {}
    for path in sorted(root_dir.rglob("*.md")):
        if path.name.startswith("."):
            continue

        agent = _load_agent_file(
            path,
            registry_enabled=bool(settings["enabled"]),
            root_dir=root_dir,
            cfg=cfg,
        )
        agent_name = agent["name"]
        if agent_name in agents:
            raise AgentRegistryError(f"duplicate agent id '{agent_name}' in {path}")

        agents[agent_name] = agent
        for token in [agent_name, *agent["aliases"]]:
            normalized_token = _normalize_lookup_token(token)
            existing = lookup.get(normalized_token)
            if existing is not None and existing != agent_name:
                raise AgentRegistryError(
                    f"agent alias collision '{token}' between '{existing}' and '{agent_name}'"
                )
            lookup[normalized_token] = agent_name

    return {
        **settings,
        "schema_version": AGENT_REGISTRY_SCHEMA_VERSION,
        "agents": agents,
        "lookup": lookup,
    }


def normalize_agent_definition_name(cfg: dict, value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise AgentRegistryError("agent definition name must be a non-empty string")

    registry = load_agent_registry(cfg)
    normalized_value = _normalize_lookup_token(value)
    resolved = registry["lookup"].get(normalized_value)
    if resolved is not None:
        return resolved

    available = ", ".join(sorted(registry["agents"]))
    raise AgentRegistryError(f"unknown agent '{value}'. Available agents: {available}")


def list_agent_definitions(cfg: dict) -> list[dict]:
    registry = load_agent_registry(cfg)
    return [
        _agent_payload(registry["agents"][agent_name], include_instructions=False)
        for agent_name in sorted(registry["agents"])
    ]


def describe_agent_definition(cfg: dict, agent_definition_name: str) -> dict:
    registry = load_agent_registry(cfg)
    canonical_name = normalize_agent_definition_name(cfg, agent_definition_name)
    return _agent_payload(registry["agents"][canonical_name], include_instructions=True)


def resolve_agent_definition_task_defaults(cfg: dict, agent_definition_name: str) -> dict:
    agent = describe_agent_definition(cfg, agent_definition_name)
    return {
        "agent_definition_name": agent["name"],
        "title": agent["title"],
        "instructions": agent["instructions"],
        "section": agent["section"],
        "explicit_skill_names": copy.deepcopy(agent["skill_names"]),
        "explicit_tool_name": agent["tool_name"],
        "allowed_routes": copy.deepcopy(agent["allowed_routes"]),
    }
