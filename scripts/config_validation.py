"""
Shared config and prerequisite validation helpers for pipeline entry points.
"""

import os
import sys

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


def require_bool(value: object, label: str) -> bool:
    if not isinstance(value, bool):
        fail(f"{label} must be a boolean")
    return value


def require_positive_int(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        fail(f"{label} must be a positive integer")
    return value


def require_positive_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
        fail(f"{label} must be a positive number")
    return float(value)


def require_number_in_range(value: object, label: str, low: float, high: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not low < value < high:
        fail(f"{label} must be a number between {low} and {high}")
    return float(value)


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


def require_environment_variables(variable_names: list[str]) -> None:
    missing = [name for name in variable_names if not os.environ.get(name)]
    if missing:
        fail(
            "Missing required environment variables: "
            f"{', '.join(missing)}. Copy .env.example to .env and fill in the values."
        )


def validate_prepare_data_config(cfg: dict) -> None:
    data = require_section(cfg, "data")
    model = require_section(cfg, "model")

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

    require_keys(model, "model", {"name", "max_seq_length", "load_in_4bit", "dtype"})
    require_keys(lora, "lora", {"r", "lora_alpha", "lora_dropout", "bias", "target_modules", "use_dora", "use_rslora"})
    require_keys(training, "training", {"output_dir", "per_device_train_batch_size", "gradient_accumulation_steps", "num_train_epochs", "learning_rate", "lr_scheduler_type", "warmup_ratio", "bf16", "fp16", "logging_steps", "save_steps", "save_total_limit", "seed"})
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
    require_number_in_range(training["warmup_ratio"], "training.warmup_ratio", 0, 1)
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