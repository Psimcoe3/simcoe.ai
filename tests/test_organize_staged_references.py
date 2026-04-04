from __future__ import annotations

import json
from pathlib import Path

from data_contracts import infer_asset_kind
from organize_staged_references import classify_relative_path, organize_batch


def test_infer_asset_kind_recognizes_heic_and_xlsm() -> None:
    assert infer_asset_kind("photo.heic") == "image"
    assert infer_asset_kind("sheet.xlsm") == "tabular"


def test_classify_relative_path_routes_layout_pdf_to_drawings() -> None:
    classification = classify_relative_path(
        "E107_L7_LAYOUT_REV01/Down Temp Power Sleeve Location.pdf"
    )

    assert classification.bucket_family == "drawings"
    assert classification.bucket_subtype == "pdf"
    assert classification.drawing_related is True


def test_classify_relative_path_keeps_generic_plan_document_out_of_drawings() -> None:
    classification = classify_relative_path(
        "001 - DOCUMENTS.7z/01 - CONTRACT DOCUMENTS/Site Safety Plan.pdf"
    )

    assert classification.bucket_family == "documents"
    assert classification.bucket_subtype == "pdf"
    assert classification.drawing_related is False


def test_organize_batch_dedupes_and_buckets_files(tmp_path: Path) -> None:
    batch_dir = tmp_path / "batch"
    extracted = batch_dir / "extracted"

    duplicate_a = extracted / "documents" / "alpha.pdf"
    duplicate_a.parent.mkdir(parents=True, exist_ok=True)
    duplicate_a.write_bytes(b"same-pdf-content")

    duplicate_b = extracted / "documents_copy" / "alpha-copy.pdf"
    duplicate_b.parent.mkdir(parents=True, exist_ok=True)
    duplicate_b.write_bytes(b"same-pdf-content")

    drawing_pdf = extracted / "E107_LAYOUT" / "plan set.pdf"
    drawing_pdf.parent.mkdir(parents=True, exist_ok=True)
    drawing_pdf.write_bytes(b"drawing-pdf")

    image_file = extracted / "photos" / "field.heic"
    image_file.parent.mkdir(parents=True, exist_ok=True)
    image_file.write_bytes(b"image")

    spreadsheet = extracted / "schedules" / "panel_schedule.xlsm"
    spreadsheet.parent.mkdir(parents=True, exist_ok=True)
    spreadsheet.write_bytes(b"spreadsheet")

    email = extracted / "mail" / "daily.msg"
    email.parent.mkdir(parents=True, exist_ok=True)
    email.write_bytes(b"email-message")

    manifest_path, duplicate_manifest_path, unique_root = organize_batch(
        batch_dir,
        batch_dir / "bucketed",
        link_mode="hardlink",
        overwrite=False,
    )

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    duplicates = json.loads(duplicate_manifest_path.read_text(encoding="utf-8"))

    assert manifest["summary"]["scanned_files"] == 6
    assert manifest["summary"]["unique_files"] == 5
    assert manifest["summary"]["duplicate_files"] == 1
    assert manifest["summary"]["duplicate_groups"] == 1

    assert (unique_root / "documents" / "pdf" / "documents" / "alpha.pdf").exists()
    assert (unique_root / "drawings" / "pdf" / "E107_LAYOUT" / "plan set.pdf").exists()
    assert (unique_root / "media" / "image" / "photos" / "field.heic").exists()
    assert (unique_root / "tabular" / "spreadsheet" / "schedules" / "panel_schedule.xlsm").exists()
    assert (unique_root / "documents" / "email_message" / "mail" / "daily.msg").exists()

    assert len(duplicates["duplicate_groups"]) == 1
    duplicate_group = duplicates["duplicate_groups"][0]
    assert duplicate_group["canonical"]["relative_source_path"] == "documents/alpha.pdf"
    assert (
        duplicate_group["duplicates"][0]["relative_source_path"] == "documents_copy/alpha-copy.pdf"
    )

    bucketed_pdf = unique_root / "documents" / "pdf" / "documents" / "alpha.pdf"
    assert bucketed_pdf.stat().st_ino == duplicate_a.stat().st_ino
