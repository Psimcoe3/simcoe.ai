"""
Shared markdown-backed skill registry for the local simcoe.ai agent shell.
"""

from __future__ import annotations

import copy
from pathlib import Path

import yaml

from runtime_contracts import normalize_route


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_REGISTRY_SCHEMA_VERSION = 1


class SkillRegistryError(ValueError):
    pass


def resolve_skill_registry_settings(cfg: dict) -> dict:
    skill_registry = (
        cfg.get("skill_registry") if isinstance(cfg.get("skill_registry"), dict) else {}
    )
    root_dir = str(skill_registry.get("root_dir") or "skills")

    candidate = Path(root_dir).expanduser()
    if not candidate.is_absolute():
        candidate = REPO_ROOT / candidate

    return {
        "enabled": bool(skill_registry.get("enabled", False)),
        "root_dir": str(candidate.resolve()),
        "max_active_skills": int(skill_registry.get("max_active_skills", 2) or 2),
        "max_instruction_chars": int(skill_registry.get("max_instruction_chars", 2400) or 2400),
    }


def _require_non_empty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SkillRegistryError(f"{label} must be a non-empty string")
    return value.strip()


def _require_string_list(value: object, label: str, *, allow_empty: bool = True) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise SkillRegistryError(f"{label} must be a list of strings")
    if not value and not allow_empty:
        raise SkillRegistryError(f"{label} must not be empty")
    return [_require_non_empty_string(item, label) for item in value]


def _require_bool(value: object, label: str) -> bool:
    if not isinstance(value, bool):
        raise SkillRegistryError(f"{label} must be a boolean")
    return value


def _normalize_lookup_token(value: str) -> str:
    return " ".join(value.strip().lower().replace("_", " ").replace("-", " ").split())


def _split_frontmatter(path: Path, content: str) -> tuple[dict, str]:
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        raise SkillRegistryError(f"skill file must start with YAML frontmatter: {path}")

    closing_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        raise SkillRegistryError(f"skill file is missing closing YAML frontmatter fence: {path}")

    frontmatter_text = "\n".join(lines[1:closing_index])
    body = "\n".join(lines[closing_index + 1 :]).strip()
    if not body:
        raise SkillRegistryError(f"skill file must contain non-empty instruction content: {path}")

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as exc:
        raise SkillRegistryError(f"could not parse skill frontmatter '{path}': {exc}") from exc

    if not isinstance(frontmatter, dict):
        raise SkillRegistryError(f"skill frontmatter must be a mapping: {path}")

    return frontmatter, body


def _normalize_route_fit(value: object, label: str) -> list[str]:
    route_fit = _require_string_list(value, label)
    normalized: list[str] = []
    for route_name in route_fit:
        try:
            normalized_route = normalize_route(route_name, label)
        except ValueError as exc:
            raise SkillRegistryError(str(exc)) from exc
        normalized.append(normalized_route)

    if len(set(normalized)) != len(normalized):
        raise SkillRegistryError(f"{label} must not contain duplicates")
    return normalized


def _skill_payload(skill: dict, *, include_instructions: bool) -> dict:
    payload = {
        "schema_version": SKILL_REGISTRY_SCHEMA_VERSION,
        "registry_enabled": bool(skill["registry_enabled"]),
        "name": skill["name"],
        "title": skill["title"],
        "summary": skill["summary"],
        "aliases": copy.deepcopy(skill["aliases"]),
        "tags": copy.deepcopy(skill["tags"]),
        "route_fit": copy.deepcopy(skill["route_fit"]),
        "triggers": copy.deepcopy(skill["triggers"]),
        "use_when": copy.deepcopy(skill["use_when"]),
        "avoid_when": copy.deepcopy(skill["avoid_when"]),
        "always_on": bool(skill["always_on"]),
        "path": skill["path"],
        "relative_path": skill["relative_path"],
        "instruction_chars": int(skill["instruction_chars"]),
    }
    if include_instructions:
        payload["instructions"] = skill["instructions"]
    return payload


def _load_skill_file(path: Path, *, registry_enabled: bool, root_dir: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    frontmatter, instructions = _split_frontmatter(path, content)

    skill_name = _require_non_empty_string(frontmatter.get("id"), f"{path}.id").lower()
    title = _require_non_empty_string(frontmatter.get("title"), f"{path}.title")
    summary = _require_non_empty_string(frontmatter.get("summary"), f"{path}.summary")
    aliases = _require_string_list(frontmatter.get("aliases", []), f"{path}.aliases")
    tags = _require_string_list(frontmatter.get("tags", []), f"{path}.tags")
    triggers = _require_string_list(frontmatter.get("triggers", []), f"{path}.triggers")
    use_when = _require_string_list(frontmatter.get("use_when", []), f"{path}.use_when")
    avoid_when = _require_string_list(frontmatter.get("avoid_when", []), f"{path}.avoid_when")
    route_fit = _normalize_route_fit(frontmatter.get("route_fit", []), f"{path}.route_fit")
    always_on = frontmatter.get("always_on", False)
    if always_on is not False:
        always_on = _require_bool(always_on, f"{path}.always_on")

    return {
        "registry_enabled": registry_enabled,
        "name": skill_name,
        "title": title,
        "summary": summary,
        "aliases": aliases,
        "tags": tags,
        "triggers": triggers,
        "use_when": use_when,
        "avoid_when": avoid_when,
        "route_fit": route_fit,
        "always_on": bool(always_on),
        "path": str(path.resolve()),
        "relative_path": str(path.resolve().relative_to(root_dir.resolve())),
        "instruction_chars": len(instructions),
        "instructions": instructions,
    }


def load_skill_registry(cfg: dict) -> dict:
    settings = resolve_skill_registry_settings(cfg)
    root_dir = Path(settings["root_dir"])
    if not root_dir.is_dir():
        raise SkillRegistryError(f"skill registry directory not found: {root_dir}")

    skills: dict[str, dict] = {}
    lookup: dict[str, str] = {}
    for path in sorted(root_dir.rglob("*.md")):
        if path.name.startswith("."):
            continue

        skill = _load_skill_file(
            path,
            registry_enabled=bool(settings["enabled"]),
            root_dir=root_dir,
        )
        skill_name = skill["name"]
        if skill_name in skills:
            raise SkillRegistryError(f"duplicate skill id '{skill_name}' in {path}")

        skills[skill_name] = skill
        for token in [skill_name, *skill["aliases"]]:
            normalized_token = _normalize_lookup_token(token)
            existing = lookup.get(normalized_token)
            if existing is not None and existing != skill_name:
                raise SkillRegistryError(
                    f"skill alias collision '{token}' between '{existing}' and '{skill_name}'"
                )
            lookup[normalized_token] = skill_name

    return {
        **settings,
        "schema_version": SKILL_REGISTRY_SCHEMA_VERSION,
        "skills": skills,
        "lookup": lookup,
    }


def normalize_agent_skill_name(cfg: dict, value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SkillRegistryError("skill name must be a non-empty string")

    registry = load_skill_registry(cfg)
    normalized_value = _normalize_lookup_token(value)
    resolved = registry["lookup"].get(normalized_value)
    if resolved is not None:
        return resolved

    available = ", ".join(sorted(registry["skills"]))
    raise SkillRegistryError(f"unknown skill '{value}'. Available skills: {available}")


def normalize_agent_skill_names(
    cfg: dict,
    values: list[str] | tuple[str, ...] | None,
    *,
    max_count: int | None = None,
) -> list[str]:
    if values is None:
        return []
    if not isinstance(values, (list, tuple)):
        raise SkillRegistryError("skill names must be provided as a list or tuple")

    normalized: list[str] = []
    seen: set[str] = set()
    for value in values:
        canonical_name = normalize_agent_skill_name(cfg, value)
        if canonical_name in seen:
            continue
        normalized.append(canonical_name)
        seen.add(canonical_name)

    if max_count is not None and len(normalized) > max_count:
        raise SkillRegistryError(f"skill selection exceeds max_active_skills ({max_count})")
    return normalized


def list_agent_skills(cfg: dict) -> list[dict]:
    registry = load_skill_registry(cfg)
    return [
        _skill_payload(registry["skills"][skill_name], include_instructions=False)
        for skill_name in sorted(registry["skills"])
    ]


def list_selected_agent_skills(
    cfg: dict,
    skill_names: list[str] | tuple[str, ...],
    *,
    include_instructions: bool = False,
) -> list[dict]:
    registry = load_skill_registry(cfg)
    normalized_names = normalize_agent_skill_names(cfg, list(skill_names))
    return [
        _skill_payload(registry["skills"][skill_name], include_instructions=include_instructions)
        for skill_name in normalized_names
    ]


def describe_agent_skill(cfg: dict, skill_name: str) -> dict:
    registry = load_skill_registry(cfg)
    canonical_name = normalize_agent_skill_name(cfg, skill_name)
    return _skill_payload(registry["skills"][canonical_name], include_instructions=True)


def match_agent_skills(
    cfg: dict,
    prompt: str,
    *,
    route_name: str | None = None,
    limit: int | None = None,
) -> list[dict]:
    settings = resolve_skill_registry_settings(cfg)
    if not settings["enabled"]:
        return []

    registry = load_skill_registry(cfg)

    normalized_prompt = _normalize_lookup_token(prompt)
    if not normalized_prompt:
        return []

    requested_limit = int(limit or registry["max_active_skills"])
    if requested_limit <= 0:
        return []

    matches: list[dict] = []
    for skill_name in sorted(registry["skills"]):
        skill = registry["skills"][skill_name]
        score = 0
        matched_terms: list[str] = []
        seen_terms: set[str] = set()

        for weight, entries in ((3, skill["triggers"]), (2, skill["aliases"]), (1, skill["tags"])):
            for entry in entries:
                normalized_entry = _normalize_lookup_token(entry)
                if normalized_entry and normalized_entry in normalized_prompt:
                    score += weight
                    if normalized_entry not in seen_terms:
                        matched_terms.append(entry)
                        seen_terms.add(normalized_entry)

        title_token = _normalize_lookup_token(skill["title"])
        if title_token and title_token in normalized_prompt and title_token not in seen_terms:
            score += 1
            matched_terms.append(skill["title"])
            seen_terms.add(title_token)

        name_token = _normalize_lookup_token(skill_name)
        if name_token and name_token in normalized_prompt and name_token not in seen_terms:
            score += 1
            matched_terms.append(skill_name)
            seen_terms.add(name_token)

        if skill["always_on"]:
            score += 1

        if score <= 0:
            continue

        if route_name and route_name in skill["route_fit"]:
            score += 1

        match_payload = _skill_payload(skill, include_instructions=True)
        match_payload["match_score"] = score
        match_payload["matched_terms"] = matched_terms
        matches.append(match_payload)

    matches.sort(key=lambda item: (-int(item["match_score"]), item["name"]))
    return matches[:requested_limit]


def select_agent_skills(
    cfg: dict,
    prompt: str,
    *,
    route_name: str | None = None,
    pinned_skill_names: list[str] | tuple[str, ...] | None = None,
    explicit_skill_names: list[str] | tuple[str, ...] | None = None,
    limit: int | None = None,
) -> list[dict]:
    settings = resolve_skill_registry_settings(cfg)
    if not settings["enabled"] and not explicit_skill_names and not pinned_skill_names:
        return []

    registry = load_skill_registry(cfg)
    requested_limit = int(limit or registry["max_active_skills"])
    if requested_limit <= 0:
        return []

    explicit_names = normalize_agent_skill_names(
        cfg,
        explicit_skill_names,
        max_count=requested_limit,
    )
    pinned_names = normalize_agent_skill_names(
        cfg,
        pinned_skill_names,
        max_count=requested_limit,
    )

    selected: list[dict] = []
    selected_by_name: dict[str, dict] = {}

    def append_skill(
        skill_name: str,
        *,
        selection_source: str,
        match_score: int = 0,
        matched_terms: list[str] | None = None,
    ) -> None:
        existing = selected_by_name.get(skill_name)
        if existing is not None:
            if selection_source not in existing["selection_sources"]:
                existing["selection_sources"].append(selection_source)
            for term in matched_terms or []:
                if term not in existing["matched_terms"]:
                    existing["matched_terms"].append(term)
            existing["match_score"] = max(int(existing["match_score"]), int(match_score))
            return

        if len(selected) >= requested_limit:
            return

        payload = _skill_payload(registry["skills"][skill_name], include_instructions=True)
        payload["selection_sources"] = [selection_source]
        payload["match_score"] = int(match_score)
        payload["matched_terms"] = list(matched_terms or [])
        selected.append(payload)
        selected_by_name[skill_name] = payload

    for skill_name in explicit_names:
        append_skill(skill_name, selection_source="explicit", match_score=requested_limit + 2)

    for skill_name in pinned_names:
        append_skill(skill_name, selection_source="pinned", match_score=requested_limit + 1)

    if registry["enabled"]:
        automatic_matches = match_agent_skills(
            cfg,
            prompt,
            route_name=route_name,
            limit=max(requested_limit, len(registry["skills"])),
        )
        for match in automatic_matches:
            append_skill(
                match["name"],
                selection_source="matched",
                match_score=int(match["match_score"]),
                matched_terms=list(match["matched_terms"]),
            )
            if len(selected) >= requested_limit and match["name"] not in selected_by_name:
                break

    return selected


def render_agent_skill_prompt(cfg: dict, matched_skills: list[dict]) -> str | None:
    if not matched_skills:
        return None

    settings = resolve_skill_registry_settings(cfg)
    remaining_chars = int(settings["max_instruction_chars"])
    if remaining_chars <= 0:
        return None

    sections = [
        "### Active Skills:",
        "Apply the following local skill guidance when it helps answer the request.",
    ]
    for skill in matched_skills:
        if remaining_chars <= 0:
            break

        instructions = str(skill.get("instructions") or "").strip()
        if not instructions:
            continue

        if len(instructions) > remaining_chars:
            clipped_instructions = instructions[: max(0, remaining_chars - 3)].rstrip()
            instructions = clipped_instructions + "..."
        remaining_chars -= len(instructions)

        sections.append(f"#### {skill['title']} ({skill['name']})")
        sections.append(instructions)

    if len(sections) <= 2:
        return None
    return "\n\n".join(sections)
