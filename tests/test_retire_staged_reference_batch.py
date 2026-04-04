from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from retire_staged_reference_batch import retire_batch


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _create_staged_batch(tmp_path: Path, *, with_import_manifest: bool = True) -> tuple[Path, Path]:
    staging_root = tmp_path / "staging"
    batch_dir = staging_root / "batch-one"

    originals_dir = batch_dir / "originals"
    originals_dir.mkdir(parents=True, exist_ok=True)
    (originals_dir / "SCHEDULE.zip").write_bytes(b"archive")

    extracted_file = batch_dir / "extracted" / "docs" / "sheet.pdf"
    extracted_file.parent.mkdir(parents=True, exist_ok=True)
    extracted_file.write_bytes(b"drawing content")

    canonical_file = batch_dir / "bucketed" / "unique" / "documents" / "pdf" / "docs" / "sheet.pdf"
    canonical_file.parent.mkdir(parents=True, exist_ok=True)
    canonical_file.write_bytes(b"drawing content")

    _write_json(
        batch_dir / "manifests" / "stage_manifest.json",
        {
            "schema_version": 1,
            "batch_name": "batch-one",
            "batch_dir": str(batch_dir),
            "extracted_dir": str(batch_dir / "extracted"),
            "summary": {"archive_count": 1, "failed_archives": []},
        },
    )
    _write_json(
        batch_dir / "bucketed" / "manifests" / "bucket_manifest.json",
        {
            "schema_version": 1,
            "batch_dir": str(batch_dir),
            "summary": {"unique_files": 1, "duplicate_files": 0},
        },
    )
    _write_json(
        batch_dir / "bucketed" / "manifests" / "duplicate_groups.json",
        {
            "schema_version": 1,
            "batch_dir": str(batch_dir),
            "duplicate_groups": [],
        },
    )

    if with_import_manifest:
        _write_json(
            batch_dir / "manifests" / "batch_import_manifest.json",
            {
                "schema_version": 1,
                "batch_name": "batch-one",
                "summary": {"selected_count": 1, "copied_count": 1},
            },
        )

    return staging_root, batch_dir


def test_retire_batch_archives_manifests_and_prunes_batch(tmp_path: Path) -> None:
    staging_root, batch_dir = _create_staged_batch(tmp_path)

    result = retire_batch(
        SimpleNamespace(
            staging_root=str(staging_root),
            archived_root=None,
            batch_name="batch-one",
            allow_without_import=False,
            keep_batch=False,
            overwrite=False,
            dry_run=False,
        )
    )

    archived_dir = staging_root / "_archived" / "batch-one"
    retired_manifest = json.loads(
        (archived_dir / "retired_manifest.json").read_text(encoding="utf-8")
    )

    assert not batch_dir.exists()
    assert (archived_dir / "manifests" / "stage_manifest.json").is_file()
    assert (archived_dir / "manifests" / "batch_import_manifest.json").is_file()
    assert (archived_dir / "bucketed" / "manifests" / "bucket_manifest.json").is_file()
    assert retired_manifest["actions"]["source_batch_removed"] is True
    assert retired_manifest["checks"]["import_manifest_present"] is True
    assert retired_manifest["archived_files"] == result["archived_files"]
    assert result["size_estimates"]["estimated_prunable_bytes"] > 0


def test_retire_batch_can_archive_without_pruning_when_requested(tmp_path: Path) -> None:
    staging_root, batch_dir = _create_staged_batch(tmp_path)

    result = retire_batch(
        SimpleNamespace(
            staging_root=str(staging_root),
            archived_root=None,
            batch_name="batch-one",
            allow_without_import=False,
            keep_batch=True,
            overwrite=False,
            dry_run=False,
        )
    )

    archived_dir = staging_root / "_archived" / "batch-one"

    assert batch_dir.exists()
    assert archived_dir.exists()
    assert result["actions"]["source_batch_removed"] is False
    assert (archived_dir / "retired_manifest.json").is_file()


def test_retire_batch_requires_import_manifest_by_default(tmp_path: Path) -> None:
    staging_root, _ = _create_staged_batch(tmp_path, with_import_manifest=False)

    with pytest.raises(SystemExit, match="Import manifest not found"):
        retire_batch(
            SimpleNamespace(
                staging_root=str(staging_root),
                archived_root=None,
                batch_name="batch-one",
                allow_without_import=False,
                keep_batch=False,
                overwrite=False,
                dry_run=True,
            )
        )
