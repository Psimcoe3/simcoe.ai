from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from string import Formatter

import yaml


DEFAULT_SYSTEM_PROMPT_LIBRARY_PATH = (
    Path(__file__).resolve().parent.parent / "prompts" / "system_prompt_templates.yaml"
)

SYSTEM_PROMPT_SURFACE_GENERATE_DATA = "generate_data"
SYSTEM_PROMPT_SURFACE_EVALUATION_JUDGE = "evaluation_judge"
SYSTEM_PROMPT_SURFACE_EXPORT_MODELFILE = "export_modelfile"
SYSTEM_PROMPT_SURFACE_AGENT_SHELL = "agent_shell"

KNOWN_SYSTEM_PROMPT_SURFACES = {
    SYSTEM_PROMPT_SURFACE_GENERATE_DATA,
    SYSTEM_PROMPT_SURFACE_EVALUATION_JUDGE,
    SYSTEM_PROMPT_SURFACE_EXPORT_MODELFILE,
    SYSTEM_PROMPT_SURFACE_AGENT_SHELL,
}


def resolve_system_prompt_library_path(path: str | None = None) -> Path:
    if path is None or not str(path).strip():
        return DEFAULT_SYSTEM_PROMPT_LIBRARY_PATH.resolve()

    candidate = Path(path).expanduser()
    if not candidate.is_absolute():
        candidate = Path(__file__).resolve().parent.parent / candidate
    return candidate.resolve()


@lru_cache(maxsize=None)
def _load_library_cached(resolved_library_path: str) -> dict:
    library_path = Path(resolved_library_path)
    try:
        with library_path.open("r", encoding="utf-8") as handle:
            payload = yaml.safe_load(handle)
    except FileNotFoundError as exc:
        raise ValueError(f"System prompt library not found: {library_path}") from exc
    except yaml.YAMLError as exc:
        raise ValueError(f"Could not parse system prompt library '{library_path}': {exc}") from exc

    if not isinstance(payload, dict):
        raise ValueError("System prompt library must contain a top-level mapping")

    templates = payload.get("templates")
    if not isinstance(templates, list) or not templates:
        raise ValueError("System prompt library must define a non-empty templates list")

    template_map: dict[str, dict] = {}
    for index, template in enumerate(templates, start=1):
        if not isinstance(template, dict):
            raise ValueError(f"System prompt template #{index} must be a mapping")

        template_id = template.get("id")
        system_prompt = template.get("system_prompt")
        if not isinstance(template_id, str) or not template_id.strip():
            raise ValueError(f"System prompt template #{index} is missing a non-empty id")
        if not isinstance(system_prompt, str) or not system_prompt.strip():
            raise ValueError(f"System prompt template '{template_id}' is missing system_prompt")
        if template_id in template_map:
            raise ValueError(f"Duplicate system prompt template id: {template_id}")
        template_map[template_id] = template

    return {
        "path": str(library_path),
        "payload": payload,
        "templates": template_map,
    }


def load_system_prompt_library(library_path: str | None = None) -> dict:
    resolved_path = resolve_system_prompt_library_path(library_path)
    return _load_library_cached(str(resolved_path))


def available_system_prompt_template_ids(library_path: str | None = None) -> list[str]:
    library = load_system_prompt_library(library_path)
    return sorted(library["templates"])


def get_system_prompt_template(template_id: str, library_path: str | None = None) -> dict:
    library = load_system_prompt_library(library_path)
    templates = library["templates"]
    try:
        return templates[template_id]
    except KeyError as exc:
        available = ", ".join(sorted(templates))
        raise ValueError(
            f"Unknown system prompt template '{template_id}'. Available templates: {available}"
        ) from exc


def _system_prompt_placeholders(system_prompt: str) -> set[str]:
    placeholders: set[str] = set()
    for _, field_name, _, _ in Formatter().parse(system_prompt):
        if field_name:
            placeholders.add(field_name)
    return placeholders


def _slot_definitions(template: dict) -> dict[str, dict]:
    slot_definitions: dict[str, dict] = {}
    slot_entries = template.get("variable_slots", [])
    if not isinstance(slot_entries, list):
        raise ValueError(f"Template '{template.get('id', 'unknown')}' has invalid variable_slots")

    for slot in slot_entries:
        if not isinstance(slot, dict):
            raise ValueError(
                f"Template '{template.get('id', 'unknown')}' has non-mapping variable slot"
            )
        slot_name = slot.get("name")
        if not isinstance(slot_name, str) or not slot_name.strip():
            raise ValueError(
                f"Template '{template.get('id', 'unknown')}' has a slot without a name"
            )
        slot_definitions[slot_name] = slot
    return slot_definitions


def _normalize_template_variables(template: dict, variables: dict | None) -> dict[str, str]:
    if variables is None:
        variables = {}
    if not isinstance(variables, dict):
        raise ValueError("Template variables must be a mapping")

    normalized: dict[str, str] = {}
    for key, value in variables.items():
        if not isinstance(key, str) or not key.strip():
            raise ValueError("Template variable names must be non-empty strings")
        if value is None:
            continue
        if isinstance(value, (dict, list, tuple, set)):
            raise ValueError(f"Template variable '{key}' must be a scalar value")
        normalized[key] = str(value).strip()

    slot_definitions = _slot_definitions(template)
    for slot_name, slot in slot_definitions.items():
        default_value = slot.get("default")
        if slot_name not in normalized and default_value is not None:
            normalized[slot_name] = str(default_value).strip()

    system_prompt = str(template["system_prompt"])
    placeholders = _system_prompt_placeholders(system_prompt)
    required_slots = {
        slot_name
        for slot_name, slot in slot_definitions.items()
        if bool(slot.get("required", False))
    }
    for placeholder in placeholders:
        slot = slot_definitions.get(placeholder)
        if slot is None or slot.get("default") is None:
            required_slots.add(placeholder)

    missing = sorted(slot_name for slot_name in required_slots if not normalized.get(slot_name))
    if missing:
        raise ValueError(
            f"Template '{template['id']}' is missing required variables: {', '.join(missing)}"
        )

    return normalized


def validate_system_prompt_template_selection(
    template_id: str,
    *,
    variables: dict | None = None,
    library_path: str | None = None,
) -> dict:
    template = get_system_prompt_template(template_id, library_path)
    normalized_variables = _normalize_template_variables(template, variables)
    return {
        "template": template,
        "variables": normalized_variables,
        "library_path": str(resolve_system_prompt_library_path(library_path)),
    }


def render_system_prompt_template(
    template_id: str,
    *,
    variables: dict | None = None,
    library_path: str | None = None,
) -> str:
    selection = validate_system_prompt_template_selection(
        template_id,
        variables=variables,
        library_path=library_path,
    )
    template = selection["template"]
    normalized_variables = selection["variables"]
    try:
        return str(template["system_prompt"]).format_map(normalized_variables)
    except KeyError as exc:
        missing_key = str(exc).strip("'")
        raise ValueError(
            f"Template '{template_id}' is missing required variable '{missing_key}'"
        ) from exc


def resolve_configured_system_prompt(
    cfg: dict,
    surface: str,
    fallback_prompt: str,
) -> tuple[str, dict]:
    if surface not in KNOWN_SYSTEM_PROMPT_SURFACES:
        choices = ", ".join(sorted(KNOWN_SYSTEM_PROMPT_SURFACES))
        raise ValueError(f"Unknown system prompt surface '{surface}'. Expected one of: {choices}")

    default_library_path = str(resolve_system_prompt_library_path())
    metadata = {
        "surface": surface,
        "configured": False,
        "source": "default",
        "template_id": None,
        "variables": {},
        "library_path": default_library_path,
    }

    system_prompts = cfg.get("system_prompts")
    if not isinstance(system_prompts, dict):
        return fallback_prompt, metadata

    library_path_value = system_prompts.get("library_path")
    resolved_library_path = str(resolve_system_prompt_library_path(library_path_value))
    metadata["library_path"] = resolved_library_path

    surface_cfg = system_prompts.get(surface)
    if not isinstance(surface_cfg, dict):
        return fallback_prompt, metadata

    template_id = surface_cfg.get("template_id")
    if not isinstance(template_id, str) or not template_id.strip():
        return fallback_prompt, metadata

    variables = (
        surface_cfg.get("variables") if isinstance(surface_cfg.get("variables"), dict) else {}
    )
    selection = validate_system_prompt_template_selection(
        template_id.strip(),
        variables=variables,
        library_path=resolved_library_path,
    )
    rendered_prompt = str(selection["template"]["system_prompt"]).format_map(selection["variables"])
    metadata.update(
        {
            "configured": True,
            "source": "template",
            "template_id": template_id.strip(),
            "variables": selection["variables"],
        }
    )
    return rendered_prompt, metadata
