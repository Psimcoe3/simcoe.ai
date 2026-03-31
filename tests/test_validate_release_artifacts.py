from __future__ import annotations

import json
from pathlib import Path
import shutil

from validate_release_artifacts import validate_release_artifacts


def _write_json(path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _base_config(tmp_path) -> tuple[dict, dict, str]:
    raw_path = tmp_path / "data" / "raw.jsonl"
    processed_dir = tmp_path / "data" / "processed"
    train_dir = processed_dir / "train"
    valid_dir = processed_dir / "valid"
    adapter_dir = tmp_path / "models" / "adapters"
    merged_dir = tmp_path / "models" / "merged_16bit"
    gguf_dir = tmp_path / "models" / "gguf"
    modelfile_path = gguf_dir / "Modelfile"
    gguf_path = gguf_dir / "model-Q4_K_M.gguf"
    benchmark_path = tmp_path / "evals" / "golden.jsonl"
    results_path = tmp_path / "evals" / "results.json"

    train_dir.mkdir(parents=True)
    valid_dir.mkdir(parents=True)
    adapter_dir.mkdir(parents=True)
    merged_dir.mkdir(parents=True)
    gguf_dir.mkdir(parents=True)
    results_path.parent.mkdir(parents=True)

    raw_path.write_text('{"instruction":"a","response":"b"}\n', encoding="utf-8")
    trainer_state_path = adapter_dir / "trainer_state.json"
    trainer_state_path.write_text("{}\n", encoding="utf-8")
    (merged_dir / "config.json").write_text("{}\n", encoding="utf-8")
    modelfile_path.write_text("FROM ./model-Q4_K_M.gguf\n", encoding="utf-8")
    gguf_path.write_text("gguf\n", encoding="utf-8")
    benchmark_path.write_text('{"prompt":"q","response":"a"}\n', encoding="utf-8")

    config_path = tmp_path / "config.test.yaml"
    config = {
        "model": {
            "name": "test-model",
            "max_seq_length": 2048,
            "load_in_4bit": True,
            "dtype": None,
        },
        "lora": {
            "r": 16,
            "lora_alpha": 16,
            "lora_dropout": 0,
            "bias": "none",
            "target_modules": ["q_proj"],
            "use_dora": False,
            "use_rslora": True,
        },
        "training": {
            "output_dir": str(adapter_dir),
            "per_device_train_batch_size": 1,
            "gradient_accumulation_steps": 1,
            "num_train_epochs": 1,
            "learning_rate": 0.0002,
            "lr_scheduler_type": "cosine",
            "warmup_steps": 1,
            "bf16": True,
            "fp16": False,
            "logging_steps": 1,
            "save_steps": 1,
            "save_total_limit": 1,
            "seed": 3407,
        },
        "data": {
            "raw_path": str(raw_path),
            "processed_dir": str(processed_dir),
            "validation_split": 0.1,
            "random_state": 3407,
        },
        "export": {
            "merged_16bit_dir": str(merged_dir),
            "gguf_dir": str(gguf_dir),
            "gguf_quantisation": "q4_k_m",
            "ollama_modelfile": str(modelfile_path),
        },
        "evaluation": {
            "results_path": str(results_path),
            "golden_benchmark_path": str(benchmark_path),
            "judge_model": "simcoe",
            "num_examples": 10,
            "quick_num_examples": 2,
            "max_new_tokens": 32,
            "quick_max_new_tokens": 16,
            "inference_batch_size": 1,
            "judge_concurrency": 1,
        },
        "release": {
            "fail_on_threshold_breach": False,
            "require_merged_smoke_test": True,
            "require_gguf_smoke_test": True,
            "full_min_rouge1": 0.2,
            "full_min_rouge2": 0.1,
            "full_min_rougeL": 0.1,
            "full_min_exact_match": 0.0,
            "min_avg_judge_score": 3.5,
        },
    }

    processed_manifest = {
        "schema_version": 1,
        "generated_at": "2026-03-31T01:00:00+00:00",
        "config_path": str(config_path.resolve()),
        "source": {
            "raw_path": str(raw_path.resolve()),
            "sha256": "raw-sha",
            "size_bytes": 32,
        },
        "counts": {
            "raw_rows": 2,
            "formatted_rows": 2,
            "unique_text_rows": 2,
            "duplicate_text_rows": 0,
            "train_rows": 1,
            "valid_rows": 1,
        },
        "dataset_fingerprints": {
            "raw": "raw-fp",
            "formatted": "formatted-fp",
            "train": "train-fp",
            "valid": "valid-fp",
        },
        "outputs": {
            "processed_dir": str(processed_dir.resolve()),
            "train_path": str(train_dir.resolve()),
            "valid_path": str(valid_dir.resolve()),
        },
        "processing": {
            "model_name": "test-model",
            "max_seq_length": 2048,
            "validation_split": 0.1,
            "random_state": 3407,
        },
    }
    _write_json(processed_dir / "manifest.json", processed_manifest)

    train_manifest = {
        "schema_version": 1,
        "generated_at": "2026-03-31T02:00:00+00:00",
        "config_path": str(config_path.resolve()),
        "data": {
            "processed_dir": str(processed_dir.resolve()),
            "train_rows": 1,
            "valid_rows": 1,
            "processed_manifest": processed_manifest,
        },
        "outputs": {
            "adapter_dir": str(adapter_dir.resolve()),
            "trainer_state_path": str(trainer_state_path.resolve()),
            "trainer_state_source_path": str(trainer_state_path.resolve()),
            "artifacts": [],
        },
    }
    _write_json(adapter_dir / "train_manifest.json", train_manifest)

    export_manifest = {
        "schema_version": 1,
        "generated_at": "2026-03-31T03:00:00+00:00",
        "config_path": str(config_path.resolve()),
        "training_manifest": train_manifest,
        "outputs": {
            "merged_dir": str(merged_dir.resolve()),
            "gguf_dir": str(gguf_dir.resolve()),
            "gguf_path": str(gguf_path.resolve()),
            "merged_artifacts": [],
            "gguf_artifacts": [],
        },
        "smoke_tests": {
            "merged": {"required": True, "passed": True},
            "gguf": {"required": True, "passed": True},
        },
    }
    _write_json(merged_dir / "export_manifest.json", export_manifest)

    results = {
        "generated_at": "2026-03-31T04:00:00+00:00",
        "mode": "full",
        "settings": {
            "release_mode": True,
            "fail_on_threshold_breach": True,
        },
        "data_manifest": {
            "path": str((processed_dir / "manifest.json").resolve()),
            "schema_version": 1,
            "generated_at": processed_manifest["generated_at"],
            "source": processed_manifest["source"],
            "counts": processed_manifest["counts"],
            "dataset_fingerprints": processed_manifest["dataset_fingerprints"],
        },
        "release_gate": {
            "configured": True,
            "passed": True,
            "failure_count": 0,
            "failed_checks": [],
            "checks": [
                {"name": "rouge1", "passed": True},
                {"name": "rouge2", "passed": True},
                {"name": "rougeL", "passed": True},
                {"name": "exact_match", "passed": True},
                {"name": "avg_judge_score", "passed": True},
            ],
        },
        "evaluation_source": {
            "kind": "golden_benchmark",
            "path": str(benchmark_path.resolve()),
        },
    }
    _write_json(results_path, results)

    config_path.write_text(json.dumps(config, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return config, processed_manifest, str(config_path)


def _copy_tree(source_root: Path, destination_root: Path, relative_path: str) -> None:
    source_path = source_root / relative_path
    destination_path = destination_root / relative_path
    if source_path.is_dir():
        shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
        return
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, destination_path)


def _relocated_config(relocated_root: Path) -> tuple[dict, str]:
    config_path = relocated_root / "config.test.yaml"
    config = {
        "model": {
            "name": "test-model",
            "max_seq_length": 2048,
            "load_in_4bit": True,
            "dtype": None,
        },
        "lora": {
            "r": 16,
            "lora_alpha": 16,
            "lora_dropout": 0,
            "bias": "none",
            "target_modules": ["q_proj"],
            "use_dora": False,
            "use_rslora": True,
        },
        "training": {
            "output_dir": str((relocated_root / "models" / "adapters").resolve()),
            "per_device_train_batch_size": 1,
            "gradient_accumulation_steps": 1,
            "num_train_epochs": 1,
            "learning_rate": 0.0002,
            "lr_scheduler_type": "cosine",
            "warmup_steps": 1,
            "bf16": True,
            "fp16": False,
            "logging_steps": 1,
            "save_steps": 1,
            "save_total_limit": 1,
            "seed": 3407,
        },
        "data": {
            "raw_path": str((relocated_root / "data" / "raw.jsonl").resolve()),
            "processed_dir": str((relocated_root / "data" / "processed").resolve()),
            "validation_split": 0.1,
            "random_state": 3407,
        },
        "export": {
            "merged_16bit_dir": str((relocated_root / "models" / "merged_16bit").resolve()),
            "gguf_dir": str((relocated_root / "models" / "gguf").resolve()),
            "gguf_quantisation": "q4_k_m",
            "ollama_modelfile": str((relocated_root / "models" / "gguf" / "Modelfile").resolve()),
        },
        "evaluation": {
            "results_path": str((relocated_root / "evals" / "results.json").resolve()),
            "golden_benchmark_path": str((relocated_root / "evals" / "golden.jsonl").resolve()),
            "judge_model": "simcoe",
            "num_examples": 10,
            "quick_num_examples": 2,
            "max_new_tokens": 32,
            "quick_max_new_tokens": 16,
            "inference_batch_size": 1,
            "judge_concurrency": 1,
        },
        "release": {
            "fail_on_threshold_breach": False,
            "require_merged_smoke_test": True,
            "require_gguf_smoke_test": True,
            "full_min_rouge1": 0.2,
            "full_min_rouge2": 0.1,
            "full_min_rougeL": 0.1,
            "full_min_exact_match": 0.0,
            "min_avg_judge_score": 3.5,
        },
    }
    config_path.write_text(json.dumps(config, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return config, str(config_path)


def test_validate_release_artifacts_passes_for_consistent_lineage(tmp_path) -> None:
    config, _, config_path = _base_config(tmp_path)

    errors = validate_release_artifacts(config, config_path)

    assert errors == []


def test_validate_release_artifacts_fails_for_stale_results(tmp_path) -> None:
    config, _, config_path = _base_config(tmp_path)
    results_path = tmp_path / "evals" / "results.json"
    results = json.loads(results_path.read_text(encoding="utf-8"))
    results["generated_at"] = "2026-03-31T02:30:00+00:00"
    _write_json(results_path, results)

    errors = validate_release_artifacts(config, config_path)

    assert "release results are older than the export manifest" in errors


def test_validate_release_artifacts_accepts_relocated_bundle_paths(
    tmp_path,
    monkeypatch,
) -> None:
    original_root = tmp_path / "original"
    original_root.mkdir()
    _base_config(original_root)

    relocated_root = tmp_path / "relocated"
    relocated_root.mkdir()
    for relative_path in (
        "data/raw.jsonl",
        "data/processed",
        "models/adapters",
        "models/merged_16bit",
        "models/gguf",
        "evals/results.json",
        "evals/golden.jsonl",
    ):
        _copy_tree(original_root, relocated_root, relative_path)

    bundle_manifest = {
        "schema_version": 1,
        "repo_root": str(original_root.resolve()),
    }
    _write_json(relocated_root / "release_bundle_manifest.json", bundle_manifest)

    relocated_config, relocated_config_path = _relocated_config(relocated_root)

    monkeypatch.chdir(relocated_root)
    errors = validate_release_artifacts(relocated_config, relocated_config_path)

    assert errors == []
