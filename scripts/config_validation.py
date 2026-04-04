"""
Shared config and prerequisite validation helpers for pipeline entry points.
"""

import os
from pathlib import Path
import sys

from data_contracts import REVIEW_STATES
from prompt_templates import (
    KNOWN_SYSTEM_PROMPT_SURFACES,
    resolve_system_prompt_library_path,
    validate_system_prompt_template_selection,
)
from runtime_contracts import (
    CONTEXT_PROVIDER_RETRIEVAL,
    FAIL_ROUTE_FALLBACK,
    KNOWN_CONTEXT_PROVIDERS,
    KNOWN_HOOK_ACTIONS,
    KNOWN_HOOK_STAGES,
    KNOWN_ROUTES,
    MULTIMODAL_ROUTES,
    normalize_route,
    normalize_context_provider,
    normalize_route_fallback,
    route_requires_multimodal,
)
import yaml


MEMORY_KINDS = {"operator_note", "verified_fact", "decision", "exception"}
MEMORY_STATUSES = {"active", "stale", "retracted"}
MEMORY_CONTRADICTION_POLICIES = {"mark_stale", "track_only"}
MEMORY_PROVIDERS = {"file"}
AGENT_SHELL_PROVIDERS = {"ollama", "openai"}


def _coerce_path(value: str) -> Path:
    return Path(value).expanduser().resolve()


def fail(message: str) -> None:
    print(f"❌  {message}")
    sys.exit(1)


def load_config(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            cfg = yaml.safe_load(handle)
    except FileNotFoundError:
        fail(f"Config file not found: {path}")
    except yaml.YAMLError as exc:
        fail(f"Could not parse config file '{path}': {exc}")

    if not isinstance(cfg, dict):
        fail("Config file must contain a top-level YAML mapping")
    return cfg


def require_section(cfg: dict, section_name: str) -> dict:
    section = cfg.get(section_name)
    if not isinstance(section, dict):
        fail(f"Missing config section: {section_name}")
    return section


def require_mapping(value: object, label: str) -> dict:
    if not isinstance(value, dict):
        fail(f"{label} must be a mapping")
    return value


def require_keys(section: dict, section_name: str, keys: set[str]) -> None:
    missing_keys = sorted(key for key in keys if key not in section)
    if missing_keys:
        fail(f"Missing config keys in '{section_name}': {', '.join(missing_keys)}")


def require_non_empty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label} must be a non-empty string")
    return value


def require_optional_string(value: object, label: str) -> str | None:
    if value is None:
        return None
    return require_non_empty_string(value, label)


def require_choice(value: object, label: str, choices: set[str]) -> str:
    cleaned = require_non_empty_string(value, label)
    if cleaned not in choices:
        fail(f"{label} must be one of: {', '.join(sorted(choices))}")
    return cleaned


def require_optional_choice(value: object, label: str, choices: set[str]) -> str | None:
    if value is None:
        return None
    return require_choice(value, label, choices)


def require_bool(value: object, label: str) -> bool:
    if not isinstance(value, bool):
        fail(f"{label} must be a boolean")
    return value


def require_optional_bool(value: object, label: str) -> bool | None:
    if value is None:
        return None
    return require_bool(value, label)


def require_positive_int(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        fail(f"{label} must be a positive integer")
    return value


def require_optional_positive_int(value: object, label: str) -> int | None:
    if value is None:
        return None
    return require_positive_int(value, label)


def require_positive_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
        fail(f"{label} must be a positive number")
    return float(value)


def require_number_in_range(value: object, label: str, low: float, high: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not low < value < high:
        fail(f"{label} must be a number between {low} and {high}")
    return float(value)


def require_number_in_closed_range(value: object, label: str, low: float, high: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not low <= value <= high:
        fail(f"{label} must be a number between {low} and {high}, inclusive")
    return float(value)


def require_optional_number_in_closed_range(
    value: object,
    label: str,
    low: float,
    high: float,
) -> float | None:
    if value is None:
        return None
    return require_number_in_closed_range(value, label, low, high)


def require_non_negative_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
        fail(f"{label} must be a non-negative number")
    return float(value)


def require_string_list(value: object, label: str) -> list[str]:
    if not isinstance(value, list) or not value:
        fail(f"{label} must be a non-empty list of strings")

    cleaned: list[str] = []
    for item in value:
        cleaned.append(require_non_empty_string(item, label))
    return cleaned


def require_directory(path: str, label: str) -> None:
    if not os.path.isdir(path):
        fail(f"{label} not found: {path}")


def require_file(path: str, label: str) -> None:
    if not os.path.isfile(path):
        fail(f"{label} not found: {path}")


def require_environment_variables(variable_names: list[str]) -> None:
    missing = [name for name in variable_names if not os.environ.get(name)]
    if missing:
        fail(
            "Missing required environment variables: "
            f"{', '.join(missing)}. Copy .env.example to .env and fill in the values."
        )


def _require_optional_scalar(value: object, label: str) -> object:
    if value is None:
        return None
    if isinstance(value, (str, int, float, bool)):
        if isinstance(value, str) and not value.strip():
            fail(f"{label} must not be an empty string")
        return value
    fail(f"{label} must be a scalar value when present")


def _resolved_path_for_comparison(path: str) -> Path:
    return Path(path).expanduser().resolve()


def _paths_overlap(first_path: str, second_path: str) -> bool:
    first = _resolved_path_for_comparison(first_path)
    second = _resolved_path_for_comparison(second_path)
    return first == second or first in second.parents or second in first.parents


def _path_is_within(root_path: str, candidate_path: str) -> bool:
    root = _resolved_path_for_comparison(root_path)
    candidate = _resolved_path_for_comparison(candidate_path)
    return candidate == root or root in candidate.parents


def validate_architecture_config(cfg: dict) -> None:
    architecture = cfg.get("architecture")
    if architecture is None:
        return

    if not isinstance(architecture, dict):
        fail("architecture must be a mapping when present")

    require_keys(
        architecture,
        "architecture",
        {
            "system_type",
            "primary_runtime",
            "multimodal_runtime_enabled",
            "retrieval_layer_enabled",
            "geometry_rules_enabled",
            "grounded_answers_require_retrieval",
        },
    )

    require_non_empty_string(architecture["system_type"], "architecture.system_type")
    primary_runtime = require_choice(
        architecture["primary_runtime"],
        "architecture.primary_runtime",
        {"text", "multimodal"},
    )
    retrieval_layer_enabled = require_bool(
        architecture["retrieval_layer_enabled"],
        "architecture.retrieval_layer_enabled",
    )
    multimodal_runtime_enabled = require_bool(
        architecture["multimodal_runtime_enabled"],
        "architecture.multimodal_runtime_enabled",
    )
    require_bool(
        architecture["geometry_rules_enabled"],
        "architecture.geometry_rules_enabled",
    )
    grounded_answers_require_retrieval = require_bool(
        architecture["grounded_answers_require_retrieval"],
        "architecture.grounded_answers_require_retrieval",
    )
    if grounded_answers_require_retrieval and not retrieval_layer_enabled:
        fail(
            "architecture.grounded_answers_require_retrieval cannot be true when "
            "architecture.retrieval_layer_enabled is false"
        )
    if primary_runtime == "multimodal" and not multimodal_runtime_enabled:
        fail(
            "architecture.primary_runtime cannot be 'multimodal' when "
            "architecture.multimodal_runtime_enabled is false"
        )

    retrieval = cfg.get("retrieval")
    if isinstance(retrieval, dict) and retrieval.get("enabled") and not retrieval_layer_enabled:
        fail("retrieval.enabled cannot be true when architecture.retrieval_layer_enabled is false")


def validate_system_prompts_config(cfg: dict) -> None:
    system_prompts = cfg.get("system_prompts")
    if system_prompts is None:
        return

    if not isinstance(system_prompts, dict):
        fail("system_prompts must be a mapping when present")

    library_path_value = require_optional_string(
        system_prompts.get("library_path"),
        "system_prompts.library_path",
    )
    resolved_library_path: str | None = None
    if library_path_value is not None:
        resolved_library_path = str(resolve_system_prompt_library_path(library_path_value))
        require_file(resolved_library_path, "System prompt library")

    unknown_keys = sorted(
        key
        for key in system_prompts
        if key not in KNOWN_SYSTEM_PROMPT_SURFACES and key != "library_path"
    )
    if unknown_keys:
        fail(
            "system_prompts contains unsupported keys: "
            f"{', '.join(unknown_keys)}"
        )

    for surface in sorted(KNOWN_SYSTEM_PROMPT_SURFACES):
        surface_cfg = system_prompts.get(surface)
        if surface_cfg is None:
            continue
        if not isinstance(surface_cfg, dict):
            fail(f"system_prompts.{surface} must be a mapping when present")

        template_id = require_optional_string(
            surface_cfg.get("template_id"),
            f"system_prompts.{surface}.template_id",
        )
        variables = surface_cfg.get("variables")
        if variables is not None:
            require_mapping(variables, f"system_prompts.{surface}.variables")
            for variable_name, variable_value in variables.items():
                if not isinstance(variable_name, str) or not variable_name.strip():
                    fail(
                        f"system_prompts.{surface}.variables keys must be non-empty strings"
                    )
                _require_optional_scalar(
                    variable_value,
                    f"system_prompts.{surface}.variables.{variable_name}",
                )

        if template_id is None:
            continue

        try:
            validate_system_prompt_template_selection(
                template_id,
                variables=variables if isinstance(variables, dict) else None,
                library_path=resolved_library_path or library_path_value,
            )
        except ValueError as exc:
            fail(f"system_prompts.{surface} is invalid: {exc}")


def validate_routing_config(cfg: dict) -> None:
    routing = cfg.get("routing")
    if routing is None:
        return

    if not isinstance(routing, dict):
        fail("routing must be a mapping when present")

    require_keys(
        routing,
        "routing",
        {"default_route", "route_fallbacks", "latency_budgets_ms"},
    )

    architecture = cfg.get("architecture") if isinstance(cfg.get("architecture"), dict) else {}
    multimodal_enabled = bool(architecture.get("multimodal_runtime_enabled", False))

    try:
        default_route = normalize_route(routing["default_route"], "routing.default_route")
    except ValueError as exc:
        fail(str(exc))

    if route_requires_multimodal(default_route) and not multimodal_enabled:
        fail(
            "routing.default_route cannot require the multimodal runtime when "
            "architecture.multimodal_runtime_enabled is false"
        )

    route_fallbacks = require_mapping(routing["route_fallbacks"], "routing.route_fallbacks")
    fallback_keys = set(route_fallbacks.keys())
    missing_fallbacks = sorted(KNOWN_ROUTES - fallback_keys)
    extra_fallbacks = sorted(fallback_keys - KNOWN_ROUTES)
    if missing_fallbacks:
        fail(
            "routing.route_fallbacks is missing routes: "
            f"{', '.join(missing_fallbacks)}"
        )
    if extra_fallbacks:
        fail(
            "routing.route_fallbacks contains unsupported routes: "
            f"{', '.join(extra_fallbacks)}"
        )

    for route_name in sorted(KNOWN_ROUTES):
        try:
            fallback = normalize_route_fallback(
                route_fallbacks.get(route_name),
                f"routing.route_fallbacks.{route_name}",
            )
        except ValueError as exc:
            fail(str(exc))

        if fallback != FAIL_ROUTE_FALLBACK and fallback == route_name:
            fail(f"routing.route_fallbacks.{route_name} cannot point to itself")
        if fallback != FAIL_ROUTE_FALLBACK and route_requires_multimodal(fallback) and not multimodal_enabled:
            fail(
                f"routing.route_fallbacks.{route_name} cannot target '{fallback}' when "
                "architecture.multimodal_runtime_enabled is false"
            )

    latency_budgets = require_mapping(routing["latency_budgets_ms"], "routing.latency_budgets_ms")
    budget_keys = set(latency_budgets.keys())
    missing_budgets = sorted(KNOWN_ROUTES - budget_keys)
    extra_budgets = sorted(budget_keys - KNOWN_ROUTES)
    if missing_budgets:
        fail(
            "routing.latency_budgets_ms is missing routes: "
            f"{', '.join(missing_budgets)}"
        )
    if extra_budgets:
        fail(
            "routing.latency_budgets_ms contains unsupported routes: "
            f"{', '.join(extra_budgets)}"
        )

    for route_name in sorted(KNOWN_ROUTES):
        require_positive_int(
            latency_budgets.get(route_name),
            f"routing.latency_budgets_ms.{route_name}",
        )


def validate_multimodal_config(cfg: dict) -> None:
    architecture = cfg.get("architecture") if isinstance(cfg.get("architecture"), dict) else {}
    multimodal_enabled = bool(architecture.get("multimodal_runtime_enabled", False))
    multimodal = cfg.get("multimodal")

    if multimodal is None:
        if multimodal_enabled:
            fail(
                "multimodal config is required when architecture.multimodal_runtime_enabled is true"
            )
        return

    if not isinstance(multimodal, dict):
        fail("multimodal must be a mapping when present")

    require_keys(
        multimodal,
        "multimodal",
        {
            "enabled_routes",
            "drawing_asset_root",
            "observation_mode",
            "ocr_enabled",
            "max_pages_per_document",
            "max_images_per_request",
            "max_observation_chars",
        },
    )

    enabled_routes = require_string_list(multimodal["enabled_routes"], "multimodal.enabled_routes")
    normalized_routes: list[str] = []
    for route_name in enabled_routes:
        try:
            normalized_route = normalize_route(route_name, "multimodal.enabled_routes")
        except ValueError as exc:
            fail(str(exc))
        if normalized_route not in MULTIMODAL_ROUTES:
            choices = ", ".join(sorted(MULTIMODAL_ROUTES))
            fail(f"multimodal.enabled_routes entries must be one of: {choices}")
        normalized_routes.append(normalized_route)
    if len(set(normalized_routes)) != len(normalized_routes):
        fail("multimodal.enabled_routes must not contain duplicate routes")

    drawing_asset_root = require_non_empty_string(
        multimodal["drawing_asset_root"],
        "multimodal.drawing_asset_root",
    )
    require_choice(
        multimodal["observation_mode"],
        "multimodal.observation_mode",
        {"ocr_text", "ocr_plus_layout"},
    )
    require_bool(multimodal["ocr_enabled"], "multimodal.ocr_enabled")
    require_positive_int(
        multimodal["max_pages_per_document"],
        "multimodal.max_pages_per_document",
    )
    require_positive_int(
        multimodal["max_images_per_request"],
        "multimodal.max_images_per_request",
    )
    require_positive_int(
        multimodal["max_observation_chars"],
        "multimodal.max_observation_chars",
    )
    model_name = require_optional_string(multimodal.get("model_name"), "multimodal.model_name")
    require_optional_string(multimodal.get("processor_name"), "multimodal.processor_name")

    if multimodal_enabled and model_name is None:
        fail(
            "multimodal.model_name is required when architecture.multimodal_runtime_enabled is true"
        )

    managed_sources = cfg.get("managed_sources") if isinstance(cfg.get("managed_sources"), dict) else None
    if managed_sources is None:
        if multimodal_enabled:
            fail(
                "managed_sources is required when architecture.multimodal_runtime_enabled is true"
            )
        return

    drawings_multimodal_root = require_optional_string(
        managed_sources.get("drawings_multimodal_root"),
        "managed_sources.drawings_multimodal_root",
    )
    drawings_reference_root = require_optional_string(
        managed_sources.get("drawings_reference_root"),
        "managed_sources.drawings_reference_root",
    )

    if drawings_multimodal_root is None:
        if multimodal_enabled:
            fail(
                "managed_sources.drawings_multimodal_root is required when "
                "architecture.multimodal_runtime_enabled is true"
            )
        return

    if drawings_reference_root is not None and _paths_overlap(drawings_reference_root, drawings_multimodal_root):
        fail(
            "managed_sources.drawings_reference_root and managed_sources.drawings_multimodal_root "
            "must be separate, non-overlapping paths"
        )

    if _resolved_path_for_comparison(drawings_multimodal_root) != _resolved_path_for_comparison(drawing_asset_root):
        fail(
            "multimodal.drawing_asset_root must match managed_sources.drawings_multimodal_root"
        )


def validate_source_registry_config(cfg: dict) -> None:
    source_registry = cfg.get("source_registry")
    if source_registry is None:
        return

    if not isinstance(source_registry, dict):
        fail("source_registry must be a mapping when present")

    require_keys(
        source_registry,
        "source_registry",
        {"root", "manifest_path", "default_review_state", "default_data_family", "allow_auto_sft"},
    )
    require_non_empty_string(source_registry["root"], "source_registry.root")
    require_non_empty_string(source_registry["manifest_path"], "source_registry.manifest_path")
    require_choice(
        source_registry["default_review_state"],
        "source_registry.default_review_state",
        REVIEW_STATES,
    )
    require_non_empty_string(
        source_registry["default_data_family"],
        "source_registry.default_data_family",
    )
    allow_auto_sft = require_bool(
        source_registry["allow_auto_sft"],
        "source_registry.allow_auto_sft",
    )
    if allow_auto_sft:
        fail(
            "source_registry.allow_auto_sft must remain false; external sources cannot enter SFT automatically"
        )

    require_optional_string(source_registry.get("repo_namespace"), "source_registry.repo_namespace")
    require_optional_string(source_registry.get("repo_sync_dir"), "source_registry.repo_sync_dir")
    require_optional_string(
        source_registry.get("materialized_manifest_path"),
        "source_registry.materialized_manifest_path",
    )


def validate_managed_sources_config(cfg: dict) -> None:
    managed_sources = cfg.get("managed_sources")
    if managed_sources is None:
        return

    if not isinstance(managed_sources, dict):
        fail("managed_sources must be a mapping when present")

    for key in (
        "root",
        "reference_root",
        "estimating_reference_root",
        "estimating_pdf",
        "estimating_har_dir",
        "code_training_reference_root",
        "drawings_reference_root",
        "drawings_multimodal_root",
        "revit_reference_root",
        "revit_family_dir",
        "structured_root",
    ):
        require_optional_string(managed_sources.get(key), f"managed_sources.{key}")

    drawings_reference_root = require_optional_string(
        managed_sources.get("drawings_reference_root"),
        "managed_sources.drawings_reference_root",
    )
    drawings_multimodal_root = require_optional_string(
        managed_sources.get("drawings_multimodal_root"),
        "managed_sources.drawings_multimodal_root",
    )
    if (
        drawings_reference_root is not None
        and drawings_multimodal_root is not None
        and _paths_overlap(drawings_reference_root, drawings_multimodal_root)
    ):
        fail(
            "managed_sources.drawings_reference_root and managed_sources.drawings_multimodal_root "
            "must be separate, non-overlapping paths"
        )


def validate_deterministic_tools_config(cfg: dict) -> None:
    deterministic_tools = cfg.get("deterministic_tools")
    if deterministic_tools is None:
        return

    if not isinstance(deterministic_tools, dict):
        fail("deterministic_tools must be a mapping when present")

    for tool_name, tool_cfg in deterministic_tools.items():
        if not isinstance(tool_name, str) or not tool_name.strip():
            fail("deterministic_tools keys must be non-empty strings")

        tool_settings = require_mapping(tool_cfg, f"deterministic_tools.{tool_name}")
        require_optional_bool(
            tool_settings.get("enabled"),
            f"deterministic_tools.{tool_name}.enabled",
        )
        require_optional_string(
            tool_settings.get("index_path"),
            f"deterministic_tools.{tool_name}.index_path",
        )
        require_optional_positive_int(
            tool_settings.get("default_top_k"),
            f"deterministic_tools.{tool_name}.default_top_k",
        )
        require_optional_positive_int(
            tool_settings.get("max_results"),
            f"deterministic_tools.{tool_name}.max_results",
        )
        require_optional_number_in_closed_range(
            tool_settings.get("min_score"),
            f"deterministic_tools.{tool_name}.min_score",
            0,
            1_000_000,
        )
        default_quantity = tool_settings.get("default_quantity")
        if default_quantity is not None:
            require_positive_number(
                default_quantity,
                f"deterministic_tools.{tool_name}.default_quantity",
            )


def validate_release_config(cfg: dict) -> None:
    release = cfg.get("release")
    if release is None:
        return

    if not isinstance(release, dict):
        fail("release must be a mapping when present")

    require_optional_bool(
        release.get("fail_on_threshold_breach"),
        "release.fail_on_threshold_breach",
    )
    require_optional_bool(
        release.get("require_retrieval_for_grounded_benchmark"),
        "release.require_retrieval_for_grounded_benchmark",
    )

    for key in (
        "quick_min_rouge1",
        "quick_min_rouge2",
        "quick_min_rougeL",
        "quick_min_exact_match",
        "full_min_rouge1",
        "full_min_rouge2",
        "full_min_rougeL",
        "full_min_exact_match",
    ):
        require_optional_number_in_closed_range(release.get(key), f"release.{key}", 0, 1)

    require_optional_number_in_closed_range(
        release.get("min_avg_judge_score"),
        "release.min_avg_judge_score",
        1,
        5,
    )
    require_optional_bool(
        release.get("require_merged_smoke_test"),
        "release.require_merged_smoke_test",
    )
    require_optional_bool(
        release.get("require_gguf_smoke_test"),
        "release.require_gguf_smoke_test",
    )
    require_optional_string(release.get("smoke_test_prompt"), "release.smoke_test_prompt")
    require_optional_positive_int(
        release.get("smoke_test_max_new_tokens"),
        "release.smoke_test_max_new_tokens",
    )
    require_optional_positive_int(
        release.get("smoke_test_min_response_chars"),
        "release.smoke_test_min_response_chars",
    )
    require_optional_string(
        release.get("ollama_model_name"),
        "release.ollama_model_name",
    )

    if bool(release.get("require_retrieval_for_grounded_benchmark")):
        retrieval = cfg.get("retrieval")
        if not isinstance(retrieval, dict) or not bool(retrieval.get("enabled", False)):
            fail(
                "release.require_retrieval_for_grounded_benchmark cannot be true when "
                "retrieval.enabled is not true"
            )

    category_thresholds = release.get("category_thresholds")
    if category_thresholds is None:
        return

    threshold_map = require_mapping(category_thresholds, "release.category_thresholds")
    for category_name, category_threshold in threshold_map.items():
        if not isinstance(category_name, str) or not category_name.strip():
            fail("release.category_thresholds keys must be non-empty strings")

        thresholds = require_mapping(
            category_threshold,
            f"release.category_thresholds.{category_name}",
        )

        for key in ("min_rouge1", "min_rouge2", "min_rougeL", "min_exact_match"):
            require_optional_number_in_closed_range(
                thresholds.get(key),
                f"release.category_thresholds.{category_name}.{key}",
                0,
                1,
            )

        require_optional_number_in_closed_range(
            thresholds.get("min_tool_success_rate"),
            f"release.category_thresholds.{category_name}.min_tool_success_rate",
            0,
            1,
        )
        require_optional_number_in_closed_range(
            thresholds.get("min_avg_tool_match_score"),
            f"release.category_thresholds.{category_name}.min_avg_tool_match_score",
            0,
            1,
        )

        require_optional_number_in_closed_range(
            thresholds.get("min_avg_judge_score"),
            f"release.category_thresholds.{category_name}.min_avg_judge_score",
            1,
            5,
        )


def validate_retrieval_config(cfg: dict) -> None:
    retrieval = cfg.get("retrieval")
    if retrieval is None:
        return

    if not isinstance(retrieval, dict):
        fail("retrieval must be a mapping when present")

    enabled = require_optional_bool(retrieval.get("enabled"), "retrieval.enabled")
    corpus_path = require_optional_string(retrieval.get("corpus_path"), "retrieval.corpus_path")
    manifest_path = require_optional_string(retrieval.get("manifest_path"), "retrieval.manifest_path")
    require_optional_positive_int(retrieval.get("top_k"), "retrieval.top_k")
    require_optional_positive_int(
        retrieval.get("max_context_chars"),
        "retrieval.max_context_chars",
    )
    require_optional_number_in_closed_range(
        retrieval.get("min_score"),
        "retrieval.min_score",
        0,
        1_000_000,
    )
    require_optional_bool(
        retrieval.get("use_in_full_evaluation"),
        "retrieval.use_in_full_evaluation",
    )

    if enabled:
        if corpus_path is None:
            fail("retrieval.corpus_path is required when retrieval.enabled is true")
        require_file(corpus_path, "Retrieval corpus file")
        if manifest_path is not None:
            require_file(manifest_path, "Retrieval manifest file")


def validate_memory_config(cfg: dict) -> None:
    memory = cfg.get("memory")
    if memory is None:
        return

    if not isinstance(memory, dict):
        fail("memory must be a mapping when present")

    require_keys(
        memory,
        "memory",
        {
            "enabled",
            "provider",
            "root_dir",
            "index_path",
            "topics_dir",
            "events_path",
            "default_top_k",
            "topic_candidate_limit",
            "max_context_chars",
            "max_index_entries",
            "max_summary_chars",
            "max_supporting_observations",
            "max_trace_results",
            "max_trace_excluded",
            "min_score",
            "require_verification",
            "contradiction_policy",
            "exclude_contradicted_topics",
            "import_max_records",
            "allowed_kinds",
            "exclude_statuses",
            "consolidation_min_events",
        },
    )

    require_bool(memory["enabled"], "memory.enabled")
    require_choice(memory["provider"], "memory.provider", MEMORY_PROVIDERS)
    require_non_empty_string(memory["root_dir"], "memory.root_dir")
    require_non_empty_string(memory["index_path"], "memory.index_path")
    require_non_empty_string(memory["topics_dir"], "memory.topics_dir")
    require_non_empty_string(memory["events_path"], "memory.events_path")
    default_top_k = require_positive_int(memory["default_top_k"], "memory.default_top_k")
    topic_candidate_limit = require_positive_int(
        memory["topic_candidate_limit"],
        "memory.topic_candidate_limit",
    )
    max_context_chars = require_positive_int(
        memory["max_context_chars"],
        "memory.max_context_chars",
    )
    max_index_entries = require_positive_int(
        memory["max_index_entries"],
        "memory.max_index_entries",
    )
    max_summary_chars = require_positive_int(
        memory["max_summary_chars"],
        "memory.max_summary_chars",
    )
    max_supporting_observations = require_positive_int(
        memory["max_supporting_observations"],
        "memory.max_supporting_observations",
    )
    max_trace_results = require_positive_int(
        memory["max_trace_results"],
        "memory.max_trace_results",
    )
    max_trace_excluded = require_positive_int(
        memory["max_trace_excluded"],
        "memory.max_trace_excluded",
    )
    require_number_in_closed_range(
        memory["min_score"],
        "memory.min_score",
        0,
        1_000_000,
    )
    require_bool(memory["require_verification"], "memory.require_verification")
    contradiction_policy = require_choice(
        memory["contradiction_policy"],
        "memory.contradiction_policy",
        MEMORY_CONTRADICTION_POLICIES,
    )
    exclude_contradicted_topics = require_bool(
        memory["exclude_contradicted_topics"],
        "memory.exclude_contradicted_topics",
    )
    import_max_records = require_positive_int(
        memory["import_max_records"],
        "memory.import_max_records",
    )
    allowed_kinds = require_string_list(memory["allowed_kinds"], "memory.allowed_kinds")
    exclude_statuses = require_string_list(memory["exclude_statuses"], "memory.exclude_statuses")
    require_positive_int(
        memory["consolidation_min_events"],
        "memory.consolidation_min_events",
    )

    unknown_kinds = sorted(set(allowed_kinds) - MEMORY_KINDS)
    if unknown_kinds:
        fail(
            "memory.allowed_kinds contains unsupported values: "
            f"{', '.join(unknown_kinds)}"
        )

    unknown_statuses = sorted(set(exclude_statuses) - MEMORY_STATUSES)
    if unknown_statuses:
        fail(
            "memory.exclude_statuses contains unsupported values: "
            f"{', '.join(unknown_statuses)}"
        )

    if default_top_k > topic_candidate_limit:
        fail("memory.default_top_k cannot exceed memory.topic_candidate_limit")
    if default_top_k > max_index_entries:
        fail("memory.default_top_k cannot exceed memory.max_index_entries")
    if max_summary_chars > max_context_chars:
        fail("memory.max_summary_chars cannot exceed memory.max_context_chars")
    if max_supporting_observations > max_trace_results:
        fail("memory.max_supporting_observations cannot exceed memory.max_trace_results")
    if max_trace_results > topic_candidate_limit:
        fail("memory.max_trace_results cannot exceed memory.topic_candidate_limit")
    if max_trace_excluded > max_index_entries:
        fail("memory.max_trace_excluded cannot exceed memory.max_index_entries")
    if contradiction_policy == "track_only" and not exclude_contradicted_topics:
        fail(
            "memory.exclude_contradicted_topics must be true when memory.contradiction_policy is 'track_only'"
        )
    if import_max_records < default_top_k:
        fail("memory.import_max_records cannot be smaller than memory.default_top_k")


def validate_dream_config(cfg: dict) -> None:
    dream = cfg.get("dream")
    if dream is None:
        return

    if not isinstance(dream, dict):
        fail("dream must be a mapping when present")

    require_keys(
        dream,
        "dream",
        {
            "enabled",
            "root_dir",
            "state_path",
            "lock_path",
            "log_dir",
            "minimum_hours_between_runs",
            "minimum_sessions_between_runs",
            "lock_timeout_seconds",
            "max_recent_logs",
            "max_persistable_entries_per_run",
            "brief_summary_chars",
        },
    )

    enabled = require_bool(dream["enabled"], "dream.enabled")
    root_dir = require_non_empty_string(dream["root_dir"], "dream.root_dir")
    state_path = require_non_empty_string(dream["state_path"], "dream.state_path")
    lock_path = require_non_empty_string(dream["lock_path"], "dream.lock_path")
    log_dir = require_non_empty_string(dream["log_dir"], "dream.log_dir")
    minimum_hours_between_runs = require_positive_int(
        dream["minimum_hours_between_runs"],
        "dream.minimum_hours_between_runs",
    )
    minimum_sessions_between_runs = require_positive_int(
        dream["minimum_sessions_between_runs"],
        "dream.minimum_sessions_between_runs",
    )
    lock_timeout_seconds = require_positive_int(
        dream["lock_timeout_seconds"],
        "dream.lock_timeout_seconds",
    )
    max_recent_logs = require_positive_int(dream["max_recent_logs"], "dream.max_recent_logs")
    max_persistable_entries_per_run = require_positive_int(
        dream["max_persistable_entries_per_run"],
        "dream.max_persistable_entries_per_run",
    )
    brief_summary_chars = require_positive_int(
        dream["brief_summary_chars"],
        "dream.brief_summary_chars",
    )

    root_path = _coerce_path(root_dir)
    state_resolved = _coerce_path(state_path)
    lock_resolved = _coerce_path(lock_path)
    log_resolved = _coerce_path(log_dir)

    if state_resolved == lock_resolved:
        fail("dream.state_path and dream.lock_path must be different files")
    if log_resolved == state_resolved.parent or log_resolved == lock_resolved.parent:
        fail("dream.log_dir must be separate from the directories holding dream state and lock files")
    if not str(state_resolved).startswith(str(root_path)):
        fail("dream.state_path must live under dream.root_dir")
    if not str(lock_resolved).startswith(str(root_path)):
        fail("dream.lock_path must live under dream.root_dir")
    if not str(log_resolved).startswith(str(root_path)):
        fail("dream.log_dir must live under dream.root_dir")
    if max_persistable_entries_per_run > max_recent_logs:
        fail(
            "dream.max_persistable_entries_per_run cannot exceed dream.max_recent_logs"
        )
    if lock_timeout_seconds < 60:
        fail("dream.lock_timeout_seconds must be at least 60 seconds")
    if brief_summary_chars > 1_000:
        fail("dream.brief_summary_chars must be 1000 characters or less")

    if enabled:
        memory = cfg.get("memory")
        if not isinstance(memory, dict):
            fail("dream.enabled requires a memory config section")
        if not bool(memory.get("enabled", False)):
            fail("dream.enabled requires memory.enabled to be true")


def validate_context_providers_config(cfg: dict) -> None:
    context_providers = cfg.get("context_providers")
    if context_providers is None:
        return

    if not isinstance(context_providers, dict):
        fail("context_providers must be a mapping when present")

    require_keys(
        context_providers,
        "context_providers",
        {"order", "max_workers"},
    )

    order = require_string_list(context_providers["order"], "context_providers.order")
    normalized_order = [
        normalize_context_provider(provider, "context_providers.order") for provider in order
    ]
    if len(normalized_order) != len(set(normalized_order)):
        fail("context_providers.order must not contain duplicate providers")
    if CONTEXT_PROVIDER_RETRIEVAL not in normalized_order:
        fail("context_providers.order must include 'retrieval'")

    unknown_providers = sorted(set(normalized_order) - KNOWN_CONTEXT_PROVIDERS)
    if unknown_providers:
        fail(
            "context_providers.order contains unsupported values: "
            f"{', '.join(unknown_providers)}"
        )

    require_positive_int(context_providers["max_workers"], "context_providers.max_workers")


def validate_hooks_config(cfg: dict) -> None:
    hooks = cfg.get("hooks")
    if hooks is None:
        return

    if not isinstance(hooks, dict):
        fail("hooks must be a mapping when present")

    require_keys(hooks, "hooks", {"enabled", "rules"})
    require_bool(hooks["enabled"], "hooks.enabled")

    rules = hooks.get("rules")
    if not isinstance(rules, list):
        fail("hooks.rules must be a list")

    for index, rule in enumerate(rules):
        if not isinstance(rule, dict):
            fail(f"hooks.rules[{index}] must be a mapping")

        require_keys(rule, f"hooks.rules[{index}]", {"name", "stage", "action"})
        require_non_empty_string(rule["name"], f"hooks.rules[{index}].name")
        require_choice(rule["stage"], f"hooks.rules[{index}].stage", KNOWN_HOOK_STAGES)
        action = require_choice(rule["action"], f"hooks.rules[{index}].action", KNOWN_HOOK_ACTIONS)
        require_optional_bool(rule.get("enabled"), f"hooks.rules[{index}].enabled")

        match = rule.get("match")
        if match is not None:
            require_mapping(match, f"hooks.rules[{index}].match")

        reason = rule.get("reason")
        if reason is not None:
            require_optional_string(reason, f"hooks.rules[{index}].reason")

        fields = rule.get("fields")
        if action in {"annotate", "set_fields"}:
            resolved_fields = require_mapping(fields, f"hooks.rules[{index}].fields")
            if not resolved_fields:
                fail(f"hooks.rules[{index}].fields must not be empty")
        elif fields is not None:
            fail(f"hooks.rules[{index}].fields is only valid for annotate or set_fields hooks")


def validate_workflow_registry_config(cfg: dict) -> None:
    workflow_registry = cfg.get("workflow_registry")
    if workflow_registry is None:
        return

    if not isinstance(workflow_registry, dict):
        fail("workflow_registry must be a mapping when present")

    require_keys(workflow_registry, "workflow_registry", {"enabled", "manifest_path"})
    require_bool(workflow_registry["enabled"], "workflow_registry.enabled")
    manifest_path = require_non_empty_string(
        workflow_registry["manifest_path"],
        "workflow_registry.manifest_path",
    )
    require_file(manifest_path, "Workflow registry manifest")


def validate_skill_registry_config(cfg: dict) -> None:
    skill_registry = cfg.get("skill_registry")
    if skill_registry is None:
        return

    if not isinstance(skill_registry, dict):
        fail("skill_registry must be a mapping when present")

    require_keys(
        skill_registry,
        "skill_registry",
        {"enabled", "root_dir", "max_active_skills", "max_instruction_chars"},
    )
    require_bool(skill_registry["enabled"], "skill_registry.enabled")
    root_dir = require_non_empty_string(skill_registry["root_dir"], "skill_registry.root_dir")
    require_positive_int(
        skill_registry["max_active_skills"],
        "skill_registry.max_active_skills",
    )
    require_positive_int(
        skill_registry["max_instruction_chars"],
        "skill_registry.max_instruction_chars",
    )
    require_directory(root_dir, "Skill registry directory")


def validate_agent_registry_config(cfg: dict) -> None:
    agent_registry = cfg.get("agent_registry")
    if agent_registry is None:
        return

    if not isinstance(agent_registry, dict):
        fail("agent_registry must be a mapping when present")

    require_keys(agent_registry, "agent_registry", {"enabled", "root_dir"})
    require_bool(agent_registry["enabled"], "agent_registry.enabled")
    root_dir = require_non_empty_string(agent_registry["root_dir"], "agent_registry.root_dir")
    require_directory(root_dir, "Agent registry directory")


def validate_agent_task_manager_config(cfg: dict) -> None:
    agent_task_manager = cfg.get("agent_task_manager")
    if agent_task_manager is None:
        return

    if not isinstance(agent_task_manager, dict):
        fail("agent_task_manager must be a mapping when present")

    require_keys(
        agent_task_manager,
        "agent_task_manager",
        {"enabled", "root_dir", "tasks_dir", "logs_dir", "transcripts_dir"},
    )

    require_bool(agent_task_manager["enabled"], "agent_task_manager.enabled")
    root_dir = require_non_empty_string(
        agent_task_manager["root_dir"],
        "agent_task_manager.root_dir",
    )
    tasks_dir = require_non_empty_string(
        agent_task_manager["tasks_dir"],
        "agent_task_manager.tasks_dir",
    )
    logs_dir = require_non_empty_string(
        agent_task_manager["logs_dir"],
        "agent_task_manager.logs_dir",
    )
    transcripts_dir = require_non_empty_string(
        agent_task_manager["transcripts_dir"],
        "agent_task_manager.transcripts_dir",
    )

    if tasks_dir == logs_dir:
        fail("agent_task_manager.tasks_dir and agent_task_manager.logs_dir must be different")
    if tasks_dir == transcripts_dir:
        fail("agent_task_manager.tasks_dir and agent_task_manager.transcripts_dir must be different")
    if logs_dir == transcripts_dir:
        fail("agent_task_manager.logs_dir and agent_task_manager.transcripts_dir must be different")
    if not _path_is_within(root_dir, tasks_dir):
        fail("agent_task_manager.tasks_dir must live under agent_task_manager.root_dir")
    if not _path_is_within(root_dir, logs_dir):
        fail("agent_task_manager.logs_dir must live under agent_task_manager.root_dir")
    if not _path_is_within(root_dir, transcripts_dir):
        fail("agent_task_manager.transcripts_dir must live under agent_task_manager.root_dir")


def validate_agent_shell_config(cfg: dict) -> None:
    agent_shell = cfg.get("agent_shell")
    if agent_shell is None:
        return

    if not isinstance(agent_shell, dict):
        fail("agent_shell must be a mapping when present")

    require_keys(
        agent_shell,
        "agent_shell",
        {
            "enabled",
            "provider",
            "model",
            "root_dir",
            "sessions_dir",
            "transcripts_dir",
            "max_turns",
            "temperature",
            "max_output_tokens",
            "history_turn_window",
            "ollama_base_url",
            "openai_api_key_env",
            "include_memory_in_text_routes",
            "include_retrieval_in_text_routes",
            "persist_context_sections",
        },
    )

    require_bool(agent_shell["enabled"], "agent_shell.enabled")
    require_choice(agent_shell["provider"], "agent_shell.provider", AGENT_SHELL_PROVIDERS)
    require_non_empty_string(agent_shell["model"], "agent_shell.model")
    root_dir = require_non_empty_string(agent_shell["root_dir"], "agent_shell.root_dir")
    sessions_dir = require_non_empty_string(
        agent_shell["sessions_dir"],
        "agent_shell.sessions_dir",
    )
    transcripts_dir = require_non_empty_string(
        agent_shell["transcripts_dir"],
        "agent_shell.transcripts_dir",
    )
    require_positive_int(agent_shell["max_turns"], "agent_shell.max_turns")
    require_number_in_closed_range(
        agent_shell["temperature"],
        "agent_shell.temperature",
        0,
        2,
    )
    require_positive_int(
        agent_shell["max_output_tokens"],
        "agent_shell.max_output_tokens",
    )
    require_positive_int(
        agent_shell["history_turn_window"],
        "agent_shell.history_turn_window",
    )
    require_non_empty_string(
        agent_shell["ollama_base_url"],
        "agent_shell.ollama_base_url",
    )
    require_non_empty_string(
        agent_shell["openai_api_key_env"],
        "agent_shell.openai_api_key_env",
    )
    include_memory_in_text_routes = require_bool(
        agent_shell["include_memory_in_text_routes"],
        "agent_shell.include_memory_in_text_routes",
    )
    include_retrieval_in_text_routes = require_bool(
        agent_shell["include_retrieval_in_text_routes"],
        "agent_shell.include_retrieval_in_text_routes",
    )
    require_bool(
        agent_shell["persist_context_sections"],
        "agent_shell.persist_context_sections",
    )

    if sessions_dir == transcripts_dir:
        fail("agent_shell.sessions_dir and agent_shell.transcripts_dir must be different")
    if not _path_is_within(root_dir, sessions_dir):
        fail("agent_shell.sessions_dir must live under agent_shell.root_dir")
    if not _path_is_within(root_dir, transcripts_dir):
        fail("agent_shell.transcripts_dir must live under agent_shell.root_dir")

    memory = cfg.get("memory") if isinstance(cfg.get("memory"), dict) else {}
    if include_memory_in_text_routes and not bool(memory.get("enabled", False)):
        fail(
            "agent_shell.include_memory_in_text_routes requires memory.enabled to be true"
        )

    retrieval = cfg.get("retrieval") if isinstance(cfg.get("retrieval"), dict) else {}
    if include_retrieval_in_text_routes and not bool(retrieval.get("enabled", False)):
        fail(
            "agent_shell.include_retrieval_in_text_routes requires retrieval.enabled to be true"
        )


def validate_orchestration_config(cfg: dict) -> None:
    validate_memory_config(cfg)
    validate_dream_config(cfg)
    validate_context_providers_config(cfg)
    validate_hooks_config(cfg)
    validate_workflow_registry_config(cfg)
    validate_skill_registry_config(cfg)
    validate_agent_registry_config(cfg)
    validate_agent_task_manager_config(cfg)
    validate_agent_shell_config(cfg)


def validate_prepare_data_config(cfg: dict) -> None:
    data = require_section(cfg, "data")
    model = require_section(cfg, "model")

    validate_architecture_config(cfg)
    validate_routing_config(cfg)
    validate_multimodal_config(cfg)
    validate_release_config(cfg)
    validate_retrieval_config(cfg)
    validate_orchestration_config(cfg)
    validate_system_prompts_config(cfg)
    validate_source_registry_config(cfg)
    validate_managed_sources_config(cfg)
    validate_deterministic_tools_config(cfg)

    require_keys(data, "data", {"raw_path", "processed_dir", "validation_split", "random_state"})
    require_keys(model, "model", {"max_seq_length", "name"})

    require_non_empty_string(data["raw_path"], "data.raw_path")
    require_non_empty_string(data["processed_dir"], "data.processed_dir")
    require_number_in_range(data["validation_split"], "data.validation_split", 0, 1)
    require_positive_int(data["random_state"], "data.random_state")
    require_positive_int(model["max_seq_length"], "model.max_seq_length")
    require_non_empty_string(model["name"], "model.name")


def validate_train_config(cfg: dict) -> None:
    model = require_section(cfg, "model")
    lora = require_section(cfg, "lora")
    training = require_section(cfg, "training")
    data = require_section(cfg, "data")

    validate_architecture_config(cfg)
    validate_routing_config(cfg)
    validate_multimodal_config(cfg)
    validate_release_config(cfg)
    validate_retrieval_config(cfg)
    validate_orchestration_config(cfg)
    validate_system_prompts_config(cfg)
    validate_source_registry_config(cfg)
    validate_managed_sources_config(cfg)
    validate_deterministic_tools_config(cfg)

    require_keys(model, "model", {"name", "max_seq_length", "load_in_4bit", "dtype"})
    require_keys(lora, "lora", {"r", "lora_alpha", "lora_dropout", "bias", "target_modules", "use_dora", "use_rslora"})
    require_keys(training, "training", {"output_dir", "per_device_train_batch_size", "gradient_accumulation_steps", "num_train_epochs", "learning_rate", "lr_scheduler_type", "bf16", "fp16", "logging_steps", "save_steps", "save_total_limit", "seed"})
    require_keys(data, "data", {"processed_dir"})

    require_non_empty_string(model["name"], "model.name")
    require_positive_int(model["max_seq_length"], "model.max_seq_length")
    require_bool(model["load_in_4bit"], "model.load_in_4bit")
    require_optional_string(model["dtype"], "model.dtype")

    require_positive_int(lora["r"], "lora.r")
    require_positive_number(lora["lora_alpha"], "lora.lora_alpha")
    require_non_negative_number(lora["lora_dropout"], "lora.lora_dropout")
    require_non_empty_string(lora["bias"], "lora.bias")
    require_string_list(lora["target_modules"], "lora.target_modules")
    require_bool(lora["use_dora"], "lora.use_dora")
    require_bool(lora["use_rslora"], "lora.use_rslora")

    require_non_empty_string(training["output_dir"], "training.output_dir")
    require_positive_int(training["per_device_train_batch_size"], "training.per_device_train_batch_size")
    require_positive_int(training["gradient_accumulation_steps"], "training.gradient_accumulation_steps")
    require_positive_number(training["num_train_epochs"], "training.num_train_epochs")
    require_positive_number(training["learning_rate"], "training.learning_rate")
    require_non_empty_string(training["lr_scheduler_type"], "training.lr_scheduler_type")
    warmup_steps = require_optional_positive_int(training.get("warmup_steps"), "training.warmup_steps")
    warmup_ratio = training.get("warmup_ratio")
    if warmup_steps is None:
        if warmup_ratio is None:
            fail("training must define either warmup_steps or warmup_ratio")
        require_number_in_range(warmup_ratio, "training.warmup_ratio", 0, 1)
    elif warmup_ratio is not None:
        require_number_in_range(warmup_ratio, "training.warmup_ratio", 0, 1)
    require_bool(training["bf16"], "training.bf16")
    require_bool(training["fp16"], "training.fp16")
    if training["bf16"] and training["fp16"]:
        fail("training.bf16 and training.fp16 cannot both be true")
    require_positive_int(training["logging_steps"], "training.logging_steps")
    require_positive_int(training["save_steps"], "training.save_steps")
    require_positive_int(training["save_total_limit"], "training.save_total_limit")
    require_positive_int(training["seed"], "training.seed")

    processed_dir = require_non_empty_string(data["processed_dir"], "data.processed_dir")
    require_directory(os.path.join(processed_dir, "train"), "Processed train dataset directory")
    require_directory(os.path.join(processed_dir, "valid"), "Processed validation dataset directory")


def validate_export_config(cfg: dict) -> None:
    model = require_section(cfg, "model")
    training = require_section(cfg, "training")
    export = require_section(cfg, "export")

    validate_architecture_config(cfg)
    validate_routing_config(cfg)
    validate_multimodal_config(cfg)
    validate_release_config(cfg)
    validate_retrieval_config(cfg)
    validate_orchestration_config(cfg)
    validate_system_prompts_config(cfg)
    validate_source_registry_config(cfg)
    validate_managed_sources_config(cfg)
    validate_deterministic_tools_config(cfg)

    require_keys(model, "model", {"name", "max_seq_length", "load_in_4bit", "dtype"})
    require_keys(training, "training", {"output_dir"})
    require_keys(export, "export", {"merged_16bit_dir", "gguf_dir", "gguf_quantisation", "ollama_modelfile"})

    require_non_empty_string(model["name"], "model.name")
    require_positive_int(model["max_seq_length"], "model.max_seq_length")
    require_bool(model["load_in_4bit"], "model.load_in_4bit")
    require_optional_string(model["dtype"], "model.dtype")

    adapter_dir = require_non_empty_string(training["output_dir"], "training.output_dir")
    require_directory(adapter_dir, "Adapter directory")

    require_non_empty_string(export["merged_16bit_dir"], "export.merged_16bit_dir")
    require_non_empty_string(export["gguf_dir"], "export.gguf_dir")
    require_non_empty_string(export["gguf_quantisation"], "export.gguf_quantisation")
    require_non_empty_string(export["ollama_modelfile"], "export.ollama_modelfile")


def validate_evaluate_config(cfg: dict, num_examples: int) -> None:
    model = require_section(cfg, "model")
    data = require_section(cfg, "data")
    export = require_section(cfg, "export")
    evaluation = require_section(cfg, "evaluation")

    require_keys(model, "model", {"max_seq_length"})
    require_keys(data, "data", {"processed_dir"})
    require_keys(export, "export", {"merged_16bit_dir"})
    require_keys(evaluation, "evaluation", {"results_path", "judge_model"})

    require_positive_int(model["max_seq_length"], "model.max_seq_length")
    require_positive_int(num_examples, "--num_examples")

    processed_dir = require_non_empty_string(data["processed_dir"], "data.processed_dir")
    require_directory(os.path.join(processed_dir, "valid"), "Processed validation dataset directory")

    merged_dir = require_non_empty_string(export["merged_16bit_dir"], "export.merged_16bit_dir")
    require_directory(merged_dir, "Merged model directory")

    require_non_empty_string(evaluation["results_path"], "evaluation.results_path")
    require_optional_string(evaluation["judge_model"], "evaluation.judge_model")
    benchmark_path = require_optional_string(
        evaluation.get("golden_benchmark_path"),
        "evaluation.golden_benchmark_path",
    )
    if benchmark_path is not None:
        require_file(benchmark_path, "Golden benchmark file")

    configured_num_examples = require_optional_positive_int(
        evaluation.get("num_examples"),
        "evaluation.num_examples",
    )
    quick_num_examples = require_optional_positive_int(
        evaluation.get("quick_num_examples"),
        "evaluation.quick_num_examples",
    )
    max_new_tokens = require_optional_positive_int(
        evaluation.get("max_new_tokens"),
        "evaluation.max_new_tokens",
    )
    quick_max_new_tokens = require_optional_positive_int(
        evaluation.get("quick_max_new_tokens"),
        "evaluation.quick_max_new_tokens",
    )
    inference_batch_size = require_optional_positive_int(
        evaluation.get("inference_batch_size"),
        "evaluation.inference_batch_size",
    )
    judge_concurrency = require_optional_positive_int(
        evaluation.get("judge_concurrency"),
        "evaluation.judge_concurrency",
    )

    if configured_num_examples is not None and quick_num_examples is not None:
        if quick_num_examples > configured_num_examples:
            fail("evaluation.quick_num_examples cannot exceed evaluation.num_examples")

    if max_new_tokens is not None and quick_max_new_tokens is not None:
        if quick_max_new_tokens > max_new_tokens:
            fail("evaluation.quick_max_new_tokens cannot exceed evaluation.max_new_tokens")

    if inference_batch_size is not None and inference_batch_size < 1:
        fail("evaluation.inference_batch_size must be a positive integer")

    if judge_concurrency is not None and judge_concurrency < 1:
        fail("evaluation.judge_concurrency must be a positive integer")

    validate_architecture_config(cfg)
    validate_routing_config(cfg)
    validate_multimodal_config(cfg)
    validate_release_config(cfg)
    validate_retrieval_config(cfg)
    validate_orchestration_config(cfg)
    validate_system_prompts_config(cfg)
    validate_source_registry_config(cfg)
    validate_managed_sources_config(cfg)


def validate_release_artifact_config(cfg: dict) -> None:
    data = require_section(cfg, "data")
    training = require_section(cfg, "training")
    export = require_section(cfg, "export")
    evaluation = require_section(cfg, "evaluation")

    validate_architecture_config(cfg)
    validate_routing_config(cfg)
    validate_multimodal_config(cfg)
    validate_release_config(cfg)
    validate_orchestration_config(cfg)
    validate_system_prompts_config(cfg)
    validate_source_registry_config(cfg)
    validate_managed_sources_config(cfg)

    require_keys(data, "data", {"processed_dir"})
    require_keys(training, "training", {"output_dir"})
    require_keys(
        export,
        "export",
        {"merged_16bit_dir", "gguf_dir", "gguf_quantisation", "ollama_modelfile"},
    )
    require_keys(
        evaluation,
        "evaluation",
        {"results_path", "judge_model"},
    )

    require_non_empty_string(data["processed_dir"], "data.processed_dir")
    require_non_empty_string(training["output_dir"], "training.output_dir")
    require_non_empty_string(export["merged_16bit_dir"], "export.merged_16bit_dir")
    require_non_empty_string(export["gguf_dir"], "export.gguf_dir")
    require_non_empty_string(export["gguf_quantisation"], "export.gguf_quantisation")
    require_non_empty_string(export["ollama_modelfile"], "export.ollama_modelfile")
    require_non_empty_string(evaluation["results_path"], "evaluation.results_path")
    require_optional_string(evaluation["judge_model"], "evaluation.judge_model")
    require_optional_string(
        evaluation.get("golden_benchmark_path"),
        "evaluation.golden_benchmark_path",
    )

    configured_num_examples = require_optional_positive_int(
        evaluation.get("num_examples"),
        "evaluation.num_examples",
    )
    quick_num_examples = require_optional_positive_int(
        evaluation.get("quick_num_examples"),
        "evaluation.quick_num_examples",
    )
    max_new_tokens = require_optional_positive_int(
        evaluation.get("max_new_tokens"),
        "evaluation.max_new_tokens",
    )
    quick_max_new_tokens = require_optional_positive_int(
        evaluation.get("quick_max_new_tokens"),
        "evaluation.quick_max_new_tokens",
    )
    inference_batch_size = require_optional_positive_int(
        evaluation.get("inference_batch_size"),
        "evaluation.inference_batch_size",
    )
    judge_concurrency = require_optional_positive_int(
        evaluation.get("judge_concurrency"),
        "evaluation.judge_concurrency",
    )

    if configured_num_examples is not None and quick_num_examples is not None:
        if quick_num_examples > configured_num_examples:
            fail("evaluation.quick_num_examples cannot exceed evaluation.num_examples")

    if max_new_tokens is not None and quick_max_new_tokens is not None:
        if quick_max_new_tokens > max_new_tokens:
            fail("evaluation.quick_max_new_tokens cannot exceed evaluation.max_new_tokens")

    if inference_batch_size is not None and inference_batch_size < 1:
        fail("evaluation.inference_batch_size must be a positive integer")

    if judge_concurrency is not None and judge_concurrency < 1:
        fail("evaluation.judge_concurrency must be a positive integer")
    validate_orchestration_config(cfg)
    validate_system_prompts_config(cfg)
    validate_deterministic_tools_config(cfg)