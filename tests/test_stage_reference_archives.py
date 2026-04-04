from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path

import pytest

from stage_reference_archives import _requested_archive_names, stage_archives


def _write_zip(path: Path, members: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, mode="w") as archive:
        for member_name, content in members.items():
            archive.writestr(member_name, content)


def test_requested_archive_names_accepts_list_file_and_deduplicates(tmp_path: Path) -> None:
    archive_list_path = tmp_path / "archive_selection.txt"
    archive_list_path.write_text(
        "\n".join(
            [
                "# selected downloads batch",
                "listed.zip",
                "extra.7z",
                "listed.zip",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    args = argparse.Namespace(
        archive=["inline.zip", "listed.zip", "inline.zip"],
        archive_list_file=str(archive_list_path),
    )

    assert _requested_archive_names(args) == ["inline.zip", "listed.zip", "extra.7z"]


def test_requested_archive_names_requires_archive_input() -> None:
    args = argparse.Namespace(archive=[], archive_list_file=None)

    with pytest.raises(
        SystemExit, match="Provide at least one --archive value or --archive-list-file"
    ):
        _requested_archive_names(args)


def test_stage_archives_accepts_archive_list_file(tmp_path: Path) -> None:
    source_dir = tmp_path / "downloads"
    staging_root = tmp_path / "staging"
    archive_name = "SCHEDULE.zip"
    _write_zip(source_dir / archive_name, {"sheets/panel_schedule.txt": "lighting schedule"})

    archive_list_path = tmp_path / "archive_selection.txt"
    archive_list_path.write_text(f"# smoke test\n{archive_name}\n", encoding="utf-8")

    args = argparse.Namespace(
        source_dir=str(source_dir),
        staging_root=str(staging_root),
        batch_name="smoke-test",
        archive=[],
        archive_list_file=str(archive_list_path),
        overwrite=False,
    )

    batch_dir, manifest_path, entries = stage_archives(args)

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert batch_dir == staging_root / "smoke-test"
    assert manifest["summary"]["archive_count"] == 1
    assert entries[0]["archive_name"] == archive_name
    assert entries[0]["status"] == "extracted"
    assert (batch_dir / "originals" / archive_name).is_file()
    assert (batch_dir / "extracted" / archive_name / "sheets" / "panel_schedule.txt").read_text(
        encoding="utf-8"
    ) == "lighting schedule"
