from __future__ import annotations

import json
from pathlib import Path

from import_staged_reference_batch import main as import_staged_batch_main


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_test_config(config_path: Path, tmp_path: Path, managed_root: Path) -> None:
    config_path.write_text(
        "\n".join(
            [
                "source_registry:",
                f'  root: "{tmp_path.as_posix()}"',
                f'  manifest_path: "{(tmp_path / "registry.json").as_posix()}"',
                '  default_review_state: "review_required"',
                '  default_data_family: "reference_unassigned"',
                "  allow_auto_sft: false",
                '  repo_namespace: "electricalai_docs"',
                f'  repo_sync_dir: "{managed_root.as_posix()}"',
                f'  materialized_manifest_path: "{(tmp_path / "materialized.json").as_posix()}"',
                "managed_sources:",
                f'  root: "{managed_root.as_posix()}"',
                f'  reference_root: "{(managed_root / "retrieval" / "document").as_posix()}"',
                f'  estimating_reference_root: "{(managed_root / "retrieval" / "document" / "estimating").as_posix()}"',
                f'  estimating_pdf: "{(managed_root / "retrieval" / "document" / "estimating" / "book.pdf").as_posix()}"',
                f'  estimating_har_dir: "{(managed_root / "manual_review" / "other" / "estimating").as_posix()}"',
                f'  code_training_reference_root: "{(managed_root / "retrieval" / "document" / "code").as_posix()}"',
                f'  drawings_reference_root: "{(managed_root / "retrieval" / "document" / "Drawings").as_posix()}"',
                f'  drawings_multimodal_root: "{(managed_root / "multimodal" / "image" / "Drawings").as_posix()}"',
                f'  revit_reference_root: "{(managed_root / "retrieval" / "document" / "Revit").as_posix()}"',
                f'  revit_family_dir: "{(managed_root / "geometry_rules" / "cad_bim" / "Revit").as_posix()}"',
                f'  structured_root: "{(managed_root / "manual_review" / "tabular").as_posix()}"',
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def test_import_staged_reference_batch_builds_registry_and_materializes_actionable_assets(
    monkeypatch,
    tmp_path: Path,
) -> None:
    staging_root = tmp_path / "staging"
    batch_dir = staging_root / "batch-one"
    extracted_dir = batch_dir / "extracted"
    manifests_dir = batch_dir / "manifests"

    drawing_pdf = extracted_dir / "docs" / "Drawings" / "E101.pdf"
    drawing_pdf.parent.mkdir(parents=True, exist_ok=True)
    drawing_pdf.write_text("drawing", encoding="utf-8")

    bulletin_pdf = extracted_dir / "docs" / "Technical-Bulletins" / "TB_E03_Lighting_Standards.pdf"
    bulletin_pdf.parent.mkdir(parents=True, exist_ok=True)
    bulletin_pdf.write_text("bulletin", encoding="utf-8")

    site_photo = extracted_dir / "photos" / "IMG_001.jpg"
    site_photo.parent.mkdir(parents=True, exist_ok=True)
    site_photo.write_text("photo", encoding="utf-8")

    _write_json(
        manifests_dir / "stage_manifest.json",
        {
            "schema_version": 1,
            "batch_name": "batch-one",
            "batch_dir": str(batch_dir),
            "extracted_dir": str(extracted_dir),
            "summary": {
                "archive_count": 1,
                "failed_archives": [],
            },
        },
    )

    managed_root = tmp_path / "managed"
    config_path = tmp_path / "config.test.yaml"
    _write_test_config(config_path, tmp_path, managed_root)

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        "sys.argv",
        [
            "import_staged_reference_batch.py",
            "--config",
            str(config_path),
            "--staging-root",
            str(staging_root),
            "--batch-name",
            "batch-one",
            "--skip-sha256",
        ],
    )

    exit_code = import_staged_batch_main()
    assert exit_code == 0

    registry_manifest = json.loads(
        (manifests_dir / "source_registry.json").read_text(encoding="utf-8")
    )
    materialized_manifest = json.loads(
        (manifests_dir / "materialized_sources.json").read_text(encoding="utf-8")
    )
    import_manifest = json.loads(
        (manifests_dir / "batch_import_manifest.json").read_text(encoding="utf-8")
    )

    assert registry_manifest["summary"]["asset_count"] == 3
    assert registry_manifest["summary"]["by_suggested_runtime_owner"]["manual_review"] == 1
    assert registry_manifest["summary"]["by_suggested_runtime_owner"]["multimodal"] == 1
    assert registry_manifest["summary"]["by_suggested_runtime_owner"]["retrieval"] == 1
    assert materialized_manifest["summary"]["selected_count"] == 2
    assert materialized_manifest["summary"]["copied_count"] == 2

    copied_targets = {
        Path(asset["repo_managed_path"]).name for asset in materialized_manifest["assets"]
    }
    assert "TB_E03_Lighting_Standards.pdf" in copied_targets
    assert "E101.pdf" in copied_targets
    assert "IMG_001.jpg" not in copied_targets
    assert import_manifest["source_view"]["mode"] == "extracted"
    assert import_manifest["source_view"]["bucket_manifest_path"] is None


def test_import_staged_reference_batch_prefers_bucketed_canonical_view_when_present(
    monkeypatch,
    tmp_path: Path,
) -> None:
    staging_root = tmp_path / "staging"
    batch_dir = staging_root / "batch-one"
    extracted_dir = batch_dir / "extracted"
    manifests_dir = batch_dir / "manifests"

    drawing_pdf = extracted_dir / "docs" / "Drawings" / "E101.pdf"
    drawing_pdf.parent.mkdir(parents=True, exist_ok=True)
    drawing_pdf.write_text("drawing", encoding="utf-8")

    duplicate_drawing = extracted_dir / "docs_copy" / "Drawings" / "E101-copy.pdf"
    duplicate_drawing.parent.mkdir(parents=True, exist_ok=True)
    duplicate_drawing.write_text("drawing", encoding="utf-8")

    bulletin_pdf = extracted_dir / "docs" / "Technical-Bulletins" / "TB_E03_Lighting_Standards.pdf"
    bulletin_pdf.parent.mkdir(parents=True, exist_ok=True)
    bulletin_pdf.write_text("bulletin", encoding="utf-8")

    bucketed_unique_root = batch_dir / "bucketed" / "unique"
    canonical_drawing = bucketed_unique_root / "drawings" / "pdf" / "docs" / "Drawings" / "E101.pdf"
    canonical_drawing.parent.mkdir(parents=True, exist_ok=True)
    canonical_drawing.write_text("drawing", encoding="utf-8")

    canonical_bulletin = (
        bucketed_unique_root
        / "documents"
        / "pdf"
        / "docs"
        / "Technical-Bulletins"
        / "TB_E03_Lighting_Standards.pdf"
    )
    canonical_bulletin.parent.mkdir(parents=True, exist_ok=True)
    canonical_bulletin.write_text("bulletin", encoding="utf-8")

    _write_json(
        manifests_dir / "stage_manifest.json",
        {
            "schema_version": 1,
            "batch_name": "batch-one",
            "batch_dir": str(batch_dir),
            "extracted_dir": str(extracted_dir),
            "summary": {
                "archive_count": 1,
                "failed_archives": [],
            },
        },
    )
    _write_json(
        batch_dir / "bucketed" / "manifests" / "bucket_manifest.json",
        {
            "schema_version": 1,
            "batch_dir": str(batch_dir),
            "extracted_root": str(extracted_dir),
            "output_dir": str(batch_dir / "bucketed"),
            "unique_root": str(bucketed_unique_root),
            "summary": {
                "scanned_files": 3,
                "unique_files": 2,
                "duplicate_files": 1,
                "duplicate_groups": 1,
            },
            "entries": [
                {
                    "status": "unique",
                    "relative_source_path": "docs/Drawings/E101.pdf",
                    "asset_kind": "document",
                    "canonical_bucket_path": str(canonical_drawing),
                    "bucket_path": str(canonical_drawing),
                },
                {
                    "status": "duplicate",
                    "relative_source_path": "docs_copy/Drawings/E101-copy.pdf",
                    "asset_kind": "document",
                    "canonical_bucket_path": str(canonical_drawing),
                    "bucket_path": None,
                },
                {
                    "status": "unique",
                    "relative_source_path": "docs/Technical-Bulletins/TB_E03_Lighting_Standards.pdf",
                    "asset_kind": "document",
                    "canonical_bucket_path": str(canonical_bulletin),
                    "bucket_path": str(canonical_bulletin),
                },
            ],
        },
    )

    managed_root = tmp_path / "managed"
    config_path = tmp_path / "config.test.yaml"
    _write_test_config(config_path, tmp_path, managed_root)

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        "sys.argv",
        [
            "import_staged_reference_batch.py",
            "--config",
            str(config_path),
            "--staging-root",
            str(staging_root),
            "--batch-name",
            "batch-one",
            "--skip-sha256",
        ],
    )

    exit_code = import_staged_batch_main()
    assert exit_code == 0

    registry_manifest = json.loads(
        (manifests_dir / "source_registry.json").read_text(encoding="utf-8")
    )
    materialized_manifest = json.loads(
        (manifests_dir / "materialized_sources.json").read_text(encoding="utf-8")
    )
    import_manifest = json.loads(
        (manifests_dir / "batch_import_manifest.json").read_text(encoding="utf-8")
    )

    assert registry_manifest["summary"]["asset_count"] == 2
    assert {asset["relative_path"] for asset in registry_manifest["assets"]} == {
        "docs/Drawings/E101.pdf",
        "docs/Technical-Bulletins/TB_E03_Lighting_Standards.pdf",
    }
    assert registry_manifest["summary"]["by_suggested_runtime_owner"]["multimodal"] == 1
    assert registry_manifest["summary"]["by_suggested_runtime_owner"]["retrieval"] == 1

    copied_targets = {
        Path(asset["repo_managed_path"]).name for asset in materialized_manifest["assets"]
    }
    assert copied_targets == {"E101.pdf", "TB_E03_Lighting_Standards.pdf"}
    assert import_manifest["source_view"]["mode"] == "bucketed"
    assert Path(import_manifest["source_view"]["scan_root"]) == bucketed_unique_root
    assert (
        Path(import_manifest["source_view"]["bucket_manifest_path"]).name == "bucket_manifest.json"
    )
