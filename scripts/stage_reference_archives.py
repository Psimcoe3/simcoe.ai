"""
Stage selected external archives into an ignored repo-local batch, preserving both the
original copied archives and extracted contents.
"""

from __future__ import annotations

import argparse
import re
import shutil
import zipfile
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import py7zr

from manifest_utils import current_utc_timestamp, runtime_manifest, write_json_file


REPO_ROOT = Path(__file__).resolve().parents[1]
CHUNK_PATTERN = re.compile(r"^(?P<base>.+)\.chunk\.(?P<part>\d+)$")
COPY_BUFFER_SIZE = 16 * 1024 * 1024


@dataclass(frozen=True)
class ArchiveJob:
    archive_name: str
    archive_kind: str
    source_paths: tuple[Path, ...]
    reconstructed_name: str | None = None

    @property
    def extraction_name(self) -> str:
        return self.reconstructed_name or self.archive_name


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Copy selected archives from an external folder into a repo-local staging batch, "
            "then validate and extract them."
        )
    )
    parser.add_argument(
        "--source-dir",
        default="/mnt/c/Users/Paul/Downloads",
        help="External source directory that currently holds the archives.",
    )
    parser.add_argument(
        "--staging-root",
        default="data/staging/reference_archive_batches",
        help="Repo-relative or absolute root that will hold staging batches.",
    )
    parser.add_argument(
        "--batch-name",
        default=_default_batch_name(),
        help="Name for the staging batch directory.",
    )
    parser.add_argument(
        "--archive",
        action="append",
        default=[],
        help="Archive file name relative to --source-dir. Provide once per selected file.",
    )
    parser.add_argument(
        "--archive-list-file",
        help=(
            "Optional text file with one archive name per line. Blank lines and lines that start "
            "with # are ignored."
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing batch directory with the same name.",
    )
    return parser.parse_args()


def _default_batch_name() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"downloads_reference_import_{timestamp}"


def _resolve_workspace_path(value: str) -> Path:
    path = Path(value).expanduser()
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _archive_names_from_list_file(value: str) -> list[str]:
    list_path = _resolve_workspace_path(value).resolve()
    if not list_path.is_file():
        raise SystemExit(f"Archive list file not found: {list_path}")

    archive_names: list[str] = []
    for raw_line in list_path.read_text(encoding="utf-8-sig").splitlines():
        archive_name = raw_line.strip()
        if not archive_name or archive_name.startswith("#"):
            continue
        archive_names.append(archive_name)
    return archive_names


def _requested_archive_names(args: argparse.Namespace) -> list[str]:
    archive_names = list(args.archive)
    if args.archive_list_file:
        archive_names.extend(_archive_names_from_list_file(args.archive_list_file))

    archive_names = list(dict.fromkeys(archive_names))
    if not archive_names:
        raise SystemExit("Provide at least one --archive value or --archive-list-file")
    return archive_names


def _normalize_permissions(path: Path) -> None:
    path.chmod(0o644)


def _ensure_member_paths_safe(member_names: Iterable[str], destination: Path) -> None:
    destination_root = destination.resolve()
    for member_name in member_names:
        normalized = member_name.replace("\\", "/").lstrip("/")
        target = (destination / normalized).resolve()
        if target != destination_root and destination_root not in target.parents:
            raise ValueError(f"Archive member escapes destination: {member_name}")


def _count_tree(root: Path) -> dict:
    file_count = 0
    dir_count = 0
    total_bytes = 0
    extensions: Counter[str] = Counter()
    for path in sorted(root.rglob("*")):
        if path.is_dir():
            dir_count += 1
            continue
        if not path.is_file():
            continue
        file_count += 1
        total_bytes += path.stat().st_size
        suffix = path.suffix.lower() or "<none>"
        extensions[suffix] += 1
    return {
        "file_count": file_count,
        "directory_count": dir_count,
        "total_bytes": total_bytes,
        "by_extension": dict(sorted(extensions.items())),
    }


def _copy_file(source_path: Path, target_path: Path) -> None:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target_path)
    _normalize_permissions(target_path)


def _copy_chunk_stream(source_path: Path, handle) -> None:
    with source_path.open("rb") as source_handle:
        while True:
            chunk = source_handle.read(COPY_BUFFER_SIZE)
            if not chunk:
                break
            handle.write(chunk)


def _reconstruct_chunked_archive(source_parts: tuple[Path, ...], target_path: Path) -> None:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with target_path.open("wb") as target_handle:
        for source_part in source_parts:
            _copy_chunk_stream(source_part, target_handle)
    _normalize_permissions(target_path)


def _extract_zip(archive_path: Path, destination: Path) -> tuple[dict, list[str]]:
    with zipfile.ZipFile(archive_path) as archive:
        member_names = archive.namelist()
        _ensure_member_paths_safe(member_names, destination)
        bad_member = archive.testzip()
        if bad_member is not None:
            raise zipfile.BadZipFile(f"CRC failure in member {bad_member}")
        archive.extractall(destination)
    return {"pack_crc_ok": True, "bad_member": None, "member_count": len(member_names)}, member_names


def _extract_7z(archive_path: Path, destination: Path) -> tuple[dict, list[str]]:
    with py7zr.SevenZipFile(archive_path, mode="r") as archive:
        member_names = archive.getnames()
        _ensure_member_paths_safe(member_names, destination)
        pack_crc_ok = archive.test()
    with py7zr.SevenZipFile(archive_path, mode="r") as archive:
        bad_member = archive.testzip()
    if pack_crc_ok is False:
        raise ValueError(f"Pack CRC validation failed for {archive_path.name}")
    if bad_member is not None:
        raise ValueError(f"CRC failure in member {bad_member}")
    with py7zr.SevenZipFile(archive_path, mode="r") as archive:
        archive.extractall(path=destination)
    return {
        "pack_crc_ok": pack_crc_ok,
        "bad_member": bad_member,
        "member_count": len(member_names),
    }, member_names


def _extract_archive(archive_path: Path, archive_kind: str, destination: Path) -> tuple[dict, dict]:
    destination.mkdir(parents=True, exist_ok=True)
    if archive_kind in {"zip", "chunked_zip"}:
        integrity, _ = _extract_zip(archive_path, destination)
    elif archive_kind == "7z":
        integrity, _ = _extract_7z(archive_path, destination)
    else:
        raise ValueError(f"Unsupported archive kind: {archive_kind}")
    return integrity, _count_tree(destination)


def _group_jobs(source_dir: Path, archive_names: list[str]) -> list[ArchiveJob]:
    regular_paths: list[Path] = []
    chunk_groups: dict[str, list[tuple[int, Path]]] = {}
    for archive_name in archive_names:
        source_path = source_dir / archive_name
        if not source_path.is_file():
            raise FileNotFoundError(f"Source archive not found: {source_path}")
        match = CHUNK_PATTERN.match(source_path.name)
        if match is None:
            regular_paths.append(source_path)
            continue
        base_name = match.group("base")
        chunk_groups.setdefault(base_name, []).append((int(match.group("part")), source_path))

    jobs: list[ArchiveJob] = []
    for source_path in sorted(regular_paths):
        suffix = source_path.suffix.lower()
        if suffix not in {".7z", ".zip"}:
            raise ValueError(f"Unsupported archive type for {source_path.name}")
        jobs.append(
            ArchiveJob(
                archive_name=source_path.name,
                archive_kind="7z" if suffix == ".7z" else "zip",
                source_paths=(source_path,),
            )
        )

    for base_name in sorted(chunk_groups):
        parts = sorted(chunk_groups[base_name], key=lambda item: item[0])
        if parts[0][0] != 1:
            raise ValueError(f"Chunk sequence for {base_name} must start at part 1")
        expected_parts = list(range(parts[0][0], parts[0][0] + len(parts)))
        actual_parts = [part_number for part_number, _ in parts]
        if actual_parts != expected_parts:
            raise ValueError(
                f"Chunk sequence for {base_name} is incomplete: {actual_parts} != {expected_parts}"
            )
        jobs.append(
            ArchiveJob(
                archive_name=base_name,
                archive_kind="chunked_zip",
                source_paths=tuple(path for _, path in parts),
                reconstructed_name=base_name,
            )
        )

    return sorted(jobs, key=lambda item: item.archive_name.lower())


def _build_manifest(
    *,
    batch_name: str,
    source_dir: Path,
    batch_dir: Path,
    entries: list[dict],
) -> dict:
    copied_bytes = 0
    extracted_bytes = 0
    extracted_files = 0
    failed_archives: list[str] = []
    for entry in entries:
        copied_bytes += int(entry.get("copied_bytes") or 0)
        extraction_summary = entry.get("extraction_summary") if isinstance(entry.get("extraction_summary"), dict) else {}
        extracted_bytes += int(extraction_summary.get("total_bytes") or 0)
        extracted_files += int(extraction_summary.get("file_count") or 0)
        if entry.get("status") != "extracted":
            failed_archives.append(str(entry.get("archive_name") or "<unknown>"))

    return {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "batch_name": batch_name,
        "source_dir": str(source_dir),
        "batch_dir": str(batch_dir),
        "originals_dir": str(batch_dir / "originals"),
        "extracted_dir": str(batch_dir / "extracted"),
        "runtime": runtime_manifest(["py7zr"]),
        "summary": {
            "archive_count": len(entries),
            "copied_bytes": copied_bytes,
            "extracted_bytes": extracted_bytes,
            "extracted_file_count": extracted_files,
            "failed_archives": failed_archives,
        },
        "entries": entries,
    }


def stage_archives(args: argparse.Namespace) -> tuple[Path, Path, list[dict]]:
    source_dir = Path(args.source_dir).expanduser().resolve()
    if not source_dir.is_dir():
        raise SystemExit(f"Source directory does not exist: {source_dir}")

    staging_root = _resolve_workspace_path(args.staging_root)
    batch_dir = staging_root / args.batch_name
    originals_dir = batch_dir / "originals"
    extracted_dir = batch_dir / "extracted"
    manifests_dir = batch_dir / "manifests"
    manifest_path = manifests_dir / "stage_manifest.json"

    if batch_dir.exists():
        if not args.overwrite:
            raise SystemExit(f"Batch directory already exists: {batch_dir}")
        shutil.rmtree(batch_dir)

    manifests_dir.mkdir(parents=True, exist_ok=True)
    jobs = _group_jobs(source_dir, _requested_archive_names(args))
    entries: list[dict] = []

    for index, job in enumerate(jobs, start=1):
        print(f"[{index}/{len(jobs)}] staging {job.archive_name}")
        copied_source_paths: list[Path] = []
        copied_bytes = 0
        for source_path in job.source_paths:
            copied_target_path = originals_dir / source_path.name
            _copy_file(source_path, copied_target_path)
            copied_source_paths.append(copied_target_path)
            copied_bytes += copied_target_path.stat().st_size

        archive_path = copied_source_paths[0]
        reconstructed_path: Path | None = None
        if job.archive_kind == "chunked_zip":
            reconstructed_path = originals_dir / job.reconstructed_name
            _reconstruct_chunked_archive(tuple(copied_source_paths), reconstructed_path)
            archive_path = reconstructed_path

        extraction_target = extracted_dir / job.extraction_name
        status = "extracted"
        error_message: str | None = None
        integrity: dict | None = None
        extraction_summary: dict | None = None

        try:
            integrity, extraction_summary = _extract_archive(archive_path, job.archive_kind, extraction_target)
        except Exception as exc:  # pragma: no cover - operational logging path
            status = "failed"
            error_message = str(exc)

        entry = {
            "archive_name": job.archive_name,
            "archive_kind": job.archive_kind,
            "status": status,
            "source_paths": [str(path) for path in job.source_paths],
            "copied_source_paths": [str(path) for path in copied_source_paths],
            "archive_path": str(archive_path),
            "reconstructed_archive_path": str(reconstructed_path) if reconstructed_path else None,
            "copied_bytes": copied_bytes,
            "extraction_dir": str(extraction_target),
            "integrity": integrity,
            "extraction_summary": extraction_summary,
            "error": error_message,
        }
        entries.append(entry)
        write_json_file(
            str(manifest_path),
            _build_manifest(
                batch_name=args.batch_name,
                source_dir=source_dir,
                batch_dir=batch_dir,
                entries=entries,
            ),
        )

        if status != "extracted":
            print(f"  failed: {error_message}")
        else:
            file_count = extraction_summary["file_count"] if extraction_summary is not None else 0
            print(f"  extracted {file_count} files into {extraction_target}")

    return batch_dir, manifest_path, entries


def main() -> int:
    args = parse_args()
    batch_dir, manifest_path, entries = stage_archives(args)
    print(f"Wrote staging manifest to {manifest_path}")
    failed_entries = [entry for entry in entries if entry.get("status") != "extracted"]
    if failed_entries:
        print(f"Completed with {len(failed_entries)} failed archive(s)")
        return 1
    print(f"Completed staging batch at {batch_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())