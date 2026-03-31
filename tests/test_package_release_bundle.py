from __future__ import annotations

import json
from pathlib import Path
import tarfile

from package_release_bundle import build_release_bundle


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _base_config(tmp_path: Path) -> tuple[dict, str]:
    raw_path = tmp_path / "data" / "raw.jsonl"
    processed_dir = tmp_path / "data" / "processed"
    train_dir = processed_dir / "train"
    valid_dir = processed_dir / "valid"
    adapter_dir = tmp_path / "models" / "adapters"
    merged_dir = tmp_path / "models" / "merged_16bit"
    gguf_dir = tmp_path / "models" / "gguf"
    modelfile_path = gguf_dir / "Modelfile"
    gguf_path = gguf_dir / "model-Q4_K_M.gguf"
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
            "kind": "processed_validation",
            "path": str(valid_dir.resolve()),
        },
    }
    _write_json(results_path, results)

    config_path.write_text(json.dumps(config, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return config, str(config_path)


def test_build_release_bundle_creates_expected_archive_entries(tmp_path) -> None:
    config, config_path = _base_config(tmp_path)
    bundle_path = tmp_path / "dist" / "release-verification-bundle.tar.gz"

    build_release_bundle(config, config_path, str(bundle_path), include_gguf=False)

    assert bundle_path.is_file()
    with tarfile.open(bundle_path, "r:gz") as archive:
        names = set(archive.getnames())
        assert "release_bundle_manifest.json" in names
        assert "data/processed/manifest.json" in names
        assert "data/processed/train" in names
        assert "data/processed/valid" in names
        assert "models/adapters/train_manifest.json" in names
        assert "models/adapters/trainer_state.json" in names
        assert "models/merged_16bit/export_manifest.json" in names
        assert "models/gguf/Modelfile" in names
        assert "models/gguf/model-Q4_K_M.gguf" in names
        assert "evals/results.json" in names

        bundle_manifest = json.load(archive.extractfile("release_bundle_manifest.json"))
        gguf_entries = [
            entry
            for entry in bundle_manifest["files"]
            if entry["relative_path"] == "models/gguf/model-Q4_K_M.gguf"
        ]
        assert len(gguf_entries) == 1
        assert gguf_entries[0]["mode"] == "placeholder"
