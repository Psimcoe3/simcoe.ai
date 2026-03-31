"""
Shared config and prerequisite validation helpers for pipeline entry points.
"""

import os
import sys

from data_contracts import REVIEW_STATES
import yaml


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
    require_choice(
        architecture["primary_runtime"],
        "architecture.primary_runtime",
        {"text", "multimodal"},
    )
    retrieval_layer_enabled = require_bool(
        architecture["retrieval_layer_enabled"],
        "architecture.retrieval_layer_enabled",
    )
    require_bool(
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

    retrieval = cfg.get("retrieval")
    if isinstance(retrieval, dict) and retrieval.get("enabled") and not retrieval_layer_enabled:
        fail("retrieval.enabled cannot be true when architecture.retrieval_layer_enabled is false")


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
        "revit_reference_root",
        "revit_family_dir",
        "structured_root",
    ):
        require_optional_string(managed_sources.get(key), f"managed_sources.{key}")


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


def validate_prepare_data_config(cfg: dict) -> None:
    data = require_section(cfg, "data")
    model = require_section(cfg, "model")

    validate_architecture_config(cfg)
    validate_release_config(cfg)
    validate_retrieval_config(cfg)
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
    validate_release_config(cfg)
    validate_retrieval_config(cfg)
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
    validate_release_config(cfg)
    validate_retrieval_config(cfg)
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
    validate_release_config(cfg)
    validate_retrieval_config(cfg)
    validate_source_registry_config(cfg)
    validate_managed_sources_config(cfg)
    validate_deterministic_tools_config(cfg)