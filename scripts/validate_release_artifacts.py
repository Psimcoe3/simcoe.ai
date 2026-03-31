"""
Validate release manifests and artifacts without rerunning model evaluation.

This script checks the existing lineage chain:
  processed manifest -> training manifest -> export manifest -> release results

It is intentionally lightweight. It only reads config, manifests, and existing
artifact paths. It does not rerun training, export, smoke tests, or evaluation.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import os

from config_validation import (
    load_config,
    validate_evaluate_config,
    validate_export_config,
    validate_prepare_data_config,
    validate_release_config,
    validate_train_config,
)
from manifest_utils import read_json_file


PROCESSED_MANIFEST_FIELDS = (
    "schema_version",
    "generated_at",
    "source",
    "counts",
    "dataset_fingerprints",
)


def _absolute(path: str) -> str:
    return os.path.abspath(path)


def _read_json_object(path: str, label: str, errors: list[str]) -> dict | None:
    if not os.path.isfile(path):
        errors.append(f"{label} not found: {path}")
        return None

    try:
        payload = read_json_file(path)
    except Exception as exc:
        errors.append(f"{label} could not be read: {exc}")
        return None

    if not isinstance(payload, dict):
        errors.append(f"{label} must contain a top-level JSON object")
        return None
    return payload


def _expect_mapping(value: object, label: str, errors: list[str]) -> dict | None:
    if not isinstance(value, dict):
        errors.append(f"{label} must be a JSON object")
        return None
    return value


def _expect_file(path: str | None, label: str, errors: list[str]) -> None:
    if not isinstance(path, str) or not path.strip():
        errors.append(f"{label} must be a non-empty file path")
        return
    if not os.path.isfile(path):
        errors.append(f"{label} not found: {path}")


def _expect_directory(path: str | None, label: str, errors: list[str]) -> None:
    if not isinstance(path, str) or not path.strip():
        errors.append(f"{label} must be a non-empty directory path")
        return
    if not os.path.isdir(path):
        errors.append(f"{label} not found: {path}")


def _parse_timestamp(value: object, label: str, errors: list[str]) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a non-empty ISO timestamp")
        return None
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        errors.append(f"{label} is not a valid ISO timestamp: {value}")
        return None


def _compare_processed_lineage(
    actual: dict | None,
    expected: dict,
    label: str,
    errors: list[str],
) -> None:
    if not isinstance(actual, dict):
        errors.append(f"{label} is missing or invalid")
        return

    mismatched_fields = [
        field_name
        for field_name in PROCESSED_MANIFEST_FIELDS
        if actual.get(field_name) != expected.get(field_name)
    ]
    if mismatched_fields:
        errors.append(
            f"{label} does not match the current processed manifest fields: "
            f"{', '.join(mismatched_fields)}"
        )


def _check_release_gate_coverage(results: dict, release_cfg: dict, errors: list[str]) -> None:
    release_gate = _expect_mapping(results.get("release_gate"), "results.release_gate", errors)
    if release_gate is None:
        return

    checks = release_gate.get("checks")
    if not isinstance(checks, list):
        errors.append("results.release_gate.checks must be a list")
        return

    check_map = {
        check.get("name"): check
        for check in checks
        if isinstance(check, dict) and isinstance(check.get("name"), str)
    }

    mode = str(results.get("mode") or "full").strip().lower() or "full"
    mode_prefix = "quick" if mode == "quick" else "full"
    for metric_name, threshold_key in (
        ("rouge1", f"{mode_prefix}_min_rouge1"),
        ("rouge2", f"{mode_prefix}_min_rouge2"),
        ("rougeL", f"{mode_prefix}_min_rougeL"),
        ("exact_match", f"{mode_prefix}_min_exact_match"),
    ):
        if release_cfg.get(threshold_key) is None:
            continue
        check = check_map.get(metric_name)
        if not isinstance(check, dict):
            errors.append(f"results.release_gate is missing the '{metric_name}' release check")
            continue
        if check.get("passed") is not True:
            errors.append(f"results.release_gate check '{metric_name}' did not pass")

    if release_cfg.get("min_avg_judge_score") is not None:
        check = check_map.get("avg_judge_score")
        if not isinstance(check, dict):
            errors.append("results.release_gate is missing the 'avg_judge_score' release check")
        elif check.get("passed") is not True:
            errors.append("results.release_gate check 'avg_judge_score' did not pass")

    if bool(release_cfg.get("require_retrieval_for_grounded_benchmark")):
        check = check_map.get("grounded_benchmark_retrieval")
        if not isinstance(check, dict):
            errors.append(
                "results.release_gate is missing the 'grounded_benchmark_retrieval' release check"
            )
        elif check.get("passed") is not True:
            errors.append("results.release_gate check 'grounded_benchmark_retrieval' did not pass")

    category_thresholds = release_cfg.get("category_thresholds")
    if not isinstance(category_thresholds, dict):
        return

    for category_name, thresholds in category_thresholds.items():
        if not isinstance(thresholds, dict):
            continue
        for threshold_key, threshold_value in thresholds.items():
            if threshold_value is None:
                continue
            check_name = f"category:{category_name}:{threshold_key}"
            check = check_map.get(check_name)
            if not isinstance(check, dict):
                errors.append(f"results.release_gate is missing the '{check_name}' release check")
                continue
            if check.get("passed") is not True:
                errors.append(f"results.release_gate check '{check_name}' did not pass")


def validate_release_artifacts(cfg: dict, config_path: str) -> list[str]:
    errors: list[str] = []

    processed_dir = cfg["data"]["processed_dir"]
    adapter_dir = cfg["training"]["output_dir"]
    merged_dir = cfg["export"]["merged_16bit_dir"]
    gguf_dir = cfg["export"]["gguf_dir"]
    modelfile_path = cfg["export"]["ollama_modelfile"]
    results_path = cfg["evaluation"]["results_path"]
    benchmark_path = cfg["evaluation"].get("golden_benchmark_path")
    release_cfg = cfg.get("release") if isinstance(cfg.get("release"), dict) else None

    if release_cfg is None:
        errors.append("config.release must be defined for release artifact validation")
        return errors

    processed_manifest_path = os.path.join(processed_dir, "manifest.json")
    processed_manifest = _read_json_object(
        processed_manifest_path,
        "Processed data manifest",
        errors,
    )
    if processed_manifest is not None:
        outputs = _expect_mapping(
            processed_manifest.get("outputs"), "processed_manifest.outputs", errors
        )
        counts = _expect_mapping(
            processed_manifest.get("counts"), "processed_manifest.counts", errors
        )
        if outputs is not None:
            if outputs.get("processed_dir") != _absolute(processed_dir):
                errors.append(
                    "processed_manifest.outputs.processed_dir does not match config.data.processed_dir"
                )
            _expect_directory(
                outputs.get("train_path"), "processed_manifest.outputs.train_path", errors
            )
            _expect_directory(
                outputs.get("valid_path"), "processed_manifest.outputs.valid_path", errors
            )
        if counts is not None:
            train_rows = counts.get("train_rows")
            valid_rows = counts.get("valid_rows")
            if not isinstance(train_rows, int) or train_rows <= 0:
                errors.append("processed_manifest.counts.train_rows must be a positive integer")
            if not isinstance(valid_rows, int) or valid_rows <= 0:
                errors.append("processed_manifest.counts.valid_rows must be a positive integer")

    train_manifest_path = os.path.join(adapter_dir, "train_manifest.json")
    train_manifest = _read_json_object(train_manifest_path, "Training manifest", errors)
    train_generated_at: datetime | None = None
    if train_manifest is not None:
        train_generated_at = _parse_timestamp(
            train_manifest.get("generated_at"),
            "train_manifest.generated_at",
            errors,
        )
        if train_manifest.get("config_path") != _absolute(config_path):
            errors.append("train_manifest.config_path does not match the selected config")
        data_block = _expect_mapping(train_manifest.get("data"), "train_manifest.data", errors)
        outputs = _expect_mapping(train_manifest.get("outputs"), "train_manifest.outputs", errors)
        if data_block is not None:
            if data_block.get("processed_dir") != _absolute(processed_dir):
                errors.append(
                    "train_manifest.data.processed_dir does not match config.data.processed_dir"
                )
            if processed_manifest is not None:
                _compare_processed_lineage(
                    data_block.get("processed_manifest"),
                    processed_manifest,
                    "train_manifest.data.processed_manifest",
                    errors,
                )
        if outputs is not None:
            if outputs.get("adapter_dir") != _absolute(adapter_dir):
                errors.append(
                    "train_manifest.outputs.adapter_dir does not match config.training.output_dir"
                )
            _expect_file(
                outputs.get("trainer_state_path"),
                "train_manifest.outputs.trainer_state_path",
                errors,
            )

    export_manifest_path = os.path.join(merged_dir, "export_manifest.json")
    export_manifest = _read_json_object(export_manifest_path, "Export manifest", errors)
    export_generated_at: datetime | None = None
    if export_manifest is not None:
        export_generated_at = _parse_timestamp(
            export_manifest.get("generated_at"),
            "export_manifest.generated_at",
            errors,
        )
        if export_manifest.get("config_path") != _absolute(config_path):
            errors.append("export_manifest.config_path does not match the selected config")
        outputs = _expect_mapping(export_manifest.get("outputs"), "export_manifest.outputs", errors)
        smoke_tests = _expect_mapping(
            export_manifest.get("smoke_tests"), "export_manifest.smoke_tests", errors
        )
        embedded_training_manifest = _expect_mapping(
            export_manifest.get("training_manifest"),
            "export_manifest.training_manifest",
            errors,
        )
        if outputs is not None:
            if outputs.get("merged_dir") != _absolute(merged_dir):
                errors.append(
                    "export_manifest.outputs.merged_dir does not match config.export.merged_16bit_dir"
                )
            if outputs.get("gguf_dir") != _absolute(gguf_dir):
                errors.append(
                    "export_manifest.outputs.gguf_dir does not match config.export.gguf_dir"
                )
            _expect_directory(
                outputs.get("merged_dir"), "export_manifest.outputs.merged_dir", errors
            )
            _expect_directory(outputs.get("gguf_dir"), "export_manifest.outputs.gguf_dir", errors)
            gguf_path = outputs.get("gguf_path")
            if gguf_path is not None:
                _expect_file(gguf_path, "export_manifest.outputs.gguf_path", errors)
        _expect_file(_absolute(modelfile_path), "config.export.ollama_modelfile", errors)

        if embedded_training_manifest is not None:
            embedded_data = _expect_mapping(
                embedded_training_manifest.get("data"),
                "export_manifest.training_manifest.data",
                errors,
            )
            if embedded_data is not None and processed_manifest is not None:
                _compare_processed_lineage(
                    embedded_data.get("processed_manifest"),
                    processed_manifest,
                    "export_manifest.training_manifest.data.processed_manifest",
                    errors,
                )

        if smoke_tests is not None:
            if bool(release_cfg.get("require_merged_smoke_test")):
                merged_smoke = _expect_mapping(
                    smoke_tests.get("merged"), "export_manifest.smoke_tests.merged", errors
                )
                if merged_smoke is not None and merged_smoke.get("passed") is not True:
                    errors.append(
                        "export manifest shows a failed or missing merged-model smoke test"
                    )
            if bool(release_cfg.get("require_gguf_smoke_test")):
                gguf_smoke = _expect_mapping(
                    smoke_tests.get("gguf"), "export_manifest.smoke_tests.gguf", errors
                )
                if gguf_smoke is not None and gguf_smoke.get("passed") is not True:
                    errors.append("export manifest shows a failed or missing GGUF smoke test")

    results = _read_json_object(results_path, "Release evaluation results", errors)
    results_generated_at: datetime | None = None
    if results is not None:
        results_generated_at = _parse_timestamp(
            results.get("generated_at"), "results.generated_at", errors
        )
        settings = _expect_mapping(results.get("settings"), "results.settings", errors)
        if settings is not None:
            if settings.get("release_mode") is not True:
                errors.append(
                    "results.settings.release_mode must be true for release artifact validation"
                )
            if settings.get("fail_on_threshold_breach") is not True:
                errors.append(
                    "results.settings.fail_on_threshold_breach must be true for release artifact validation"
                )

        release_gate = _expect_mapping(results.get("release_gate"), "results.release_gate", errors)
        if release_gate is not None:
            if release_gate.get("configured") is not True:
                errors.append("results.release_gate.configured must be true")
            if release_gate.get("passed") is not True:
                errors.append("results.release_gate did not pass")
            failed_checks = release_gate.get("failed_checks")
            if isinstance(failed_checks, list) and failed_checks:
                errors.append("results.release_gate.failed_checks is not empty")

        data_manifest = _expect_mapping(
            results.get("data_manifest"), "results.data_manifest", errors
        )
        if data_manifest is not None and processed_manifest is not None:
            if data_manifest.get("path") != _absolute(processed_manifest_path):
                errors.append(
                    "results.data_manifest.path does not point at the current processed manifest"
                )
            _compare_processed_lineage(
                data_manifest, processed_manifest, "results.data_manifest", errors
            )

        evaluation_source = _expect_mapping(
            results.get("evaluation_source"), "results.evaluation_source", errors
        )
        if benchmark_path and evaluation_source is not None:
            if evaluation_source.get("kind") != "golden_benchmark":
                errors.append(
                    "results.evaluation_source.kind must be 'golden_benchmark' when a benchmark is configured"
                )
            if evaluation_source.get("path") != _absolute(benchmark_path):
                errors.append(
                    "results.evaluation_source.path does not match config.evaluation.golden_benchmark_path"
                )

        _check_release_gate_coverage(results, release_cfg, errors)

    processed_generated_at = (
        _parse_timestamp(
            processed_manifest.get("generated_at"), "processed_manifest.generated_at", errors
        )
        if processed_manifest is not None
        else None
    )
    if (
        processed_generated_at
        and train_generated_at
        and train_generated_at < processed_generated_at
    ):
        errors.append("training manifest is older than the processed data manifest")
    if train_generated_at and export_generated_at and export_generated_at < train_generated_at:
        errors.append("export manifest is older than the training manifest")
    if export_generated_at and results_generated_at and results_generated_at < export_generated_at:
        errors.append("release results are older than the export manifest")

    return errors


def _resolve_validation_num_examples(cfg: dict) -> int:
    evaluation = cfg.get("evaluation") if isinstance(cfg.get("evaluation"), dict) else {}
    configured = evaluation.get("quick_num_examples") or evaluation.get("num_examples") or 1
    if isinstance(configured, int) and configured > 0:
        return configured
    return 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate release manifests and existing artifacts without rerunning evaluation."
    )
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)
    validate_prepare_data_config(cfg)
    validate_train_config(cfg)
    validate_export_config(cfg)
    validate_release_config(cfg)
    validate_evaluate_config(cfg, _resolve_validation_num_examples(cfg))

    errors = validate_release_artifacts(cfg, args.config)
    if errors:
        print("\n❌  Release artifact validation failed.")
        for error in errors:
            print(f"    - {error}")
        print()
        raise SystemExit(1)

    print("\n✅  Release artifacts validated.")
    print(f"    Config:   {_absolute(args.config)}")
    print(f"    Data:     {_absolute(os.path.join(cfg['data']['processed_dir'], 'manifest.json'))}")
    print(
        f"    Train:    {_absolute(os.path.join(cfg['training']['output_dir'], 'train_manifest.json'))}"
    )
    print(
        f"    Export:   {_absolute(os.path.join(cfg['export']['merged_16bit_dir'], 'export_manifest.json'))}"
    )
    print(f"    Results:  {_absolute(cfg['evaluation']['results_path'])}")
    print()


if __name__ == "__main__":
    main()
