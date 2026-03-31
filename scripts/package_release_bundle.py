"""
Build a lightweight release-verification bundle from existing local artifacts.

The bundle is intentionally small. It captures the manifest lineage and the
minimal on-disk files required for `make release-verify` / `make quality-release`
on another machine without rerunning export or evaluation.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import tarfile
import tempfile

from config_validation import (
    load_config,
    validate_release_artifact_config,
)
from manifest_utils import current_utc_timestamp, read_json_file, write_json_file


def _absolute(path: str) -> str:
    return os.path.abspath(path)


def _bundle_root(config_path: str, candidate_paths: list[str]) -> str:
    absolute_paths = [_absolute(config_path), *[_absolute(path) for path in candidate_paths]]
    return os.path.commonpath(absolute_paths)


def _repo_relative_path(path: str, repo_root: str) -> str:
    absolute_path = _absolute(path)
    relative_path = os.path.relpath(absolute_path, repo_root)
    if relative_path.startswith(".."):
        raise ValueError(f"Path is outside the repository root: {absolute_path}")
    return relative_path


def _read_manifest(path: str, label: str) -> dict:
    payload = read_json_file(path)
    if not isinstance(payload, dict):
        raise ValueError(f"{label} must contain a top-level JSON object")
    return payload


def _resolve_release_bundle_plan(cfg: dict, config_path: str, include_gguf: bool) -> dict:
    processed_dir = cfg["data"]["processed_dir"]
    adapter_dir = cfg["training"]["output_dir"]
    merged_dir = cfg["export"]["merged_16bit_dir"]
    modelfile_path = cfg["export"]["ollama_modelfile"]
    results_path = cfg["evaluation"]["results_path"]

    processed_manifest_path = os.path.join(processed_dir, "manifest.json")
    train_manifest_path = os.path.join(adapter_dir, "train_manifest.json")
    export_manifest_path = os.path.join(merged_dir, "export_manifest.json")

    processed_manifest = _read_manifest(processed_manifest_path, "Processed manifest")
    train_manifest = _read_manifest(train_manifest_path, "Training manifest")
    export_manifest = _read_manifest(export_manifest_path, "Export manifest")
    _read_manifest(results_path, "Release evaluation results")

    trainer_outputs = (
        train_manifest.get("outputs") if isinstance(train_manifest.get("outputs"), dict) else {}
    )
    export_outputs = (
        export_manifest.get("outputs") if isinstance(export_manifest.get("outputs"), dict) else {}
    )

    trainer_state_path = trainer_outputs.get("trainer_state_path") or os.path.join(
        adapter_dir, "trainer_state.json"
    )
    gguf_path = export_outputs.get("gguf_path")

    if not isinstance(trainer_state_path, str) or not os.path.isfile(trainer_state_path):
        raise FileNotFoundError(f"Trainer state path not found: {trainer_state_path}")
    if not isinstance(modelfile_path, str) or not os.path.isfile(modelfile_path):
        raise FileNotFoundError(f"Ollama Modelfile not found: {modelfile_path}")
    if gguf_path is not None and not isinstance(gguf_path, str):
        raise ValueError("export_manifest.outputs.gguf_path must be a string or null")
    if isinstance(gguf_path, str) and not os.path.isfile(gguf_path):
        raise FileNotFoundError(f"GGUF artifact not found: {gguf_path}")

    repo_root = _bundle_root(
        config_path,
        [
            processed_manifest_path,
            train_manifest_path,
            export_manifest_path,
            results_path,
            trainer_state_path,
            modelfile_path,
            *([gguf_path] if isinstance(gguf_path, str) else []),
        ],
    )

    file_entries: list[dict] = [
        {
            "path": processed_manifest_path,
            "mode": "copy",
            "reason": "processed_data_manifest",
        },
        {
            "path": train_manifest_path,
            "mode": "copy",
            "reason": "training_manifest",
        },
        {
            "path": trainer_state_path,
            "mode": "copy",
            "reason": "training_state",
        },
        {
            "path": export_manifest_path,
            "mode": "copy",
            "reason": "export_manifest",
        },
        {
            "path": modelfile_path,
            "mode": "copy",
            "reason": "ollama_modelfile",
        },
        {
            "path": results_path,
            "mode": "copy",
            "reason": "release_results",
        },
    ]

    merged_config_path = os.path.join(merged_dir, "config.json")
    if os.path.isfile(merged_config_path):
        file_entries.append(
            {
                "path": merged_config_path,
                "mode": "copy",
                "reason": "merged_model_config",
            }
        )

    if isinstance(gguf_path, str):
        file_entries.append(
            {
                "path": gguf_path,
                "mode": "copy" if include_gguf else "placeholder",
                "reason": "gguf_artifact",
                "original_size_bytes": os.path.getsize(gguf_path),
            }
        )

    directory_entries = [
        {
            "path": processed_manifest.get("outputs", {}).get("train_path")
            or os.path.join(processed_dir, "train"),
            "reason": "processed_train_directory",
        },
        {
            "path": processed_manifest.get("outputs", {}).get("valid_path")
            or os.path.join(processed_dir, "valid"),
            "reason": "processed_valid_directory",
        },
    ]

    normalized_files: list[dict] = []
    for entry in file_entries:
        relative_path = _repo_relative_path(str(entry["path"]), repo_root)
        normalized_files.append(
            {
                **entry,
                "path": _absolute(str(entry["path"])),
                "relative_path": relative_path,
                "size_bytes": os.path.getsize(str(entry["path"]))
                if os.path.isfile(str(entry["path"]))
                else None,
            }
        )

    normalized_directories: list[dict] = []
    for entry in directory_entries:
        path = str(entry["path"])
        if not os.path.isdir(path):
            raise FileNotFoundError(f"Required directory not found: {path}")
        normalized_directories.append(
            {
                **entry,
                "path": _absolute(path),
                "relative_path": _repo_relative_path(path, repo_root),
            }
        )

    return {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "config_path": _absolute(config_path),
        "repo_root": repo_root,
        "include_gguf": include_gguf,
        "bundle_type": "release_verification",
        "manifests": {
            "processed": _absolute(processed_manifest_path),
            "training": _absolute(train_manifest_path),
            "export": _absolute(export_manifest_path),
            "results": _absolute(results_path),
        },
        "files": normalized_files,
        "directories": normalized_directories,
    }


def _write_placeholder(path: str, original_size_bytes: int | None = None) -> None:
    note = "placeholder for lightweight release-verification bundle\n"
    if original_size_bytes is not None:
        note += f"original_size_bytes={original_size_bytes}\n"
    Path(path).write_text(note, encoding="utf-8")


def build_release_bundle(cfg: dict, config_path: str, out_path: str, include_gguf: bool) -> str:
    bundle_plan = _resolve_release_bundle_plan(cfg, config_path, include_gguf)
    absolute_out_path = _absolute(out_path)
    os.makedirs(os.path.dirname(absolute_out_path), exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="release-bundle-") as staging_dir:
        for directory_entry in bundle_plan["directories"]:
            os.makedirs(os.path.join(staging_dir, directory_entry["relative_path"]), exist_ok=True)

        for file_entry in bundle_plan["files"]:
            staged_path = os.path.join(staging_dir, file_entry["relative_path"])
            os.makedirs(os.path.dirname(staged_path), exist_ok=True)
            if file_entry["mode"] == "copy":
                shutil.copy2(file_entry["path"], staged_path)
            else:
                _write_placeholder(staged_path, file_entry.get("original_size_bytes"))

        write_json_file(os.path.join(staging_dir, "release_bundle_manifest.json"), bundle_plan)

        with tarfile.open(absolute_out_path, "w:gz") as archive:
            for current_root, dirnames, filenames in os.walk(staging_dir):
                dirnames.sort()
                filenames.sort()
                relative_root = os.path.relpath(current_root, staging_dir)
                archive_root = "." if relative_root == "." else relative_root
                archive.add(current_root, arcname=archive_root, recursive=False)
                for filename in filenames:
                    path = os.path.join(current_root, filename)
                    archive_name = (
                        filename if relative_root == "." else os.path.join(relative_root, filename)
                    )
                    archive.add(path, arcname=archive_name, recursive=False)

    return absolute_out_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a lightweight release-verification bundle from existing artifacts."
    )
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument(
        "--out",
        default="dist/release-verification-bundle.tar.gz",
        help="Path to the output tar.gz bundle.",
    )
    parser.add_argument(
        "--include-gguf",
        action="store_true",
        help="Copy the real GGUF artifact into the bundle instead of a lightweight placeholder.",
    )
    args = parser.parse_args()

    cfg = load_config(args.config)
    validate_release_artifact_config(cfg)

    bundle_path = build_release_bundle(cfg, args.config, args.out, include_gguf=args.include_gguf)
    print("\n✅  Release verification bundle created.")
    print(f"    Config:  {_absolute(args.config)}")
    print(f"    Bundle:  {bundle_path}")
    print(f"    Mode:    {'full_gguf' if args.include_gguf else 'lightweight'}")
    print()


if __name__ == "__main__":
    main()
