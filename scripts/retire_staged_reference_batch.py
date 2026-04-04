"""
Archive the machine-readable manifests for one staged reference batch and optionally
remove the larger staged assets after import succeeds.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from manifest_utils import current_utc_timestamp, read_json_file, write_json_file


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARCHIVED_DIRNAME = "_archived"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Copy the audit manifests for a staged reference batch into an archived location "
            "and optionally prune the original staged batch directory."
        )
    )
    parser.add_argument(
        "--staging-root",
        default="data/staging/reference_archive_batches",
        help="Repo-relative or absolute root that holds staged batches.",
    )
    parser.add_argument(
        "--archived-root",
        help=(
            "Repo-relative or absolute root that will hold archived batch manifests. "
            "Defaults to <staging-root>/_archived."
        ),
    )
    parser.add_argument("--batch-name", required=True, help="Name of the staged batch directory.")
    parser.add_argument(
        "--allow-without-import",
        action="store_true",
        help="Allow archiving a batch even when manifests/batch_import_manifest.json is missing.",
    )
    parser.add_argument(
        "--keep-batch",
        action="store_true",
        help="Keep the original staged batch directory after archiving its manifests.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing archived manifest directory for the same batch.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the archive-and-prune plan without writing or deleting files.",
    )
    return parser.parse_args()


def _resolve_workspace_path(value: str) -> Path:
    path = Path(value).expanduser()
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _directory_stats(root: Path) -> dict:
    if not root.exists():
        return {
            "exists": False,
            "directory_count": 0,
            "file_count": 0,
            "total_bytes": 0,
        }

    directory_count = 0
    file_count = 0
    total_bytes = 0
    for path in sorted(root.rglob("*")):
        if path.is_dir():
            directory_count += 1
            continue
        if not path.is_file():
            continue
        file_count += 1
        total_bytes += path.stat().st_size

    return {
        "exists": True,
        "directory_count": directory_count,
        "file_count": file_count,
        "total_bytes": total_bytes,
    }


def _planned_archive_files(source_dir: Path, destination_prefix: Path) -> list[str]:
    if not source_dir.is_dir():
        return []

    planned_files: list[str] = []
    for source_path in sorted(source_dir.rglob("*")):
        if not source_path.is_file():
            continue
        planned_files.append((destination_prefix / source_path.relative_to(source_dir)).as_posix())
    return planned_files


def _copy_tree(source_dir: Path, destination_dir: Path, destination_prefix: Path) -> list[str]:
    copied_files: list[str] = []
    if not source_dir.is_dir():
        return copied_files

    for source_path in sorted(source_dir.rglob("*")):
        if not source_path.is_file():
            continue
        relative_path = source_path.relative_to(source_dir)
        target_path = destination_dir / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)
        copied_files.append((destination_prefix / relative_path).as_posix())
    return copied_files


def _manifest_snapshot(path: Path) -> dict | None:
    if not path.is_file():
        return None

    payload = read_json_file(str(path))
    summary = payload.get("summary")
    if not isinstance(summary, dict):
        summary = None
    return {
        "path": str(path.resolve()),
        "schema_version": payload.get("schema_version"),
        "summary": summary,
    }


def _remove_path(path: Path) -> None:
    if not path.exists():
        return
    if path.is_dir():
        shutil.rmtree(path)
        return
    path.unlink()


def _validate_archive_location(batch_dir: Path, archived_dir: Path) -> None:
    batch_resolved = batch_dir.resolve()
    archived_resolved = archived_dir.resolve()
    if batch_resolved == archived_resolved or batch_resolved in archived_resolved.parents:
        raise SystemExit(
            "Archived manifest directory must be outside the staged batch directory being retired"
        )


def retire_batch(args: argparse.Namespace) -> dict:
    staging_root = _resolve_workspace_path(args.staging_root)
    batch_dir = (staging_root / args.batch_name).resolve()
    if not batch_dir.is_dir():
        raise SystemExit(f"Staged batch directory not found: {batch_dir}")

    archived_root = (
        _resolve_workspace_path(args.archived_root)
        if args.archived_root
        else (staging_root / DEFAULT_ARCHIVED_DIRNAME)
    ).resolve()
    archived_dir = (archived_root / args.batch_name).resolve()
    _validate_archive_location(batch_dir, archived_dir)

    manifests_dir = batch_dir / "manifests"
    bucketed_manifests_dir = batch_dir / "bucketed" / "manifests"
    stage_manifest_path = manifests_dir / "stage_manifest.json"
    import_manifest_path = manifests_dir / "batch_import_manifest.json"
    bucket_manifest_path = bucketed_manifests_dir / "bucket_manifest.json"
    duplicate_manifest_path = bucketed_manifests_dir / "duplicate_groups.json"

    if not stage_manifest_path.is_file():
        raise SystemExit(f"Stage manifest not found: {stage_manifest_path}")
    if not import_manifest_path.is_file() and not args.allow_without_import:
        raise SystemExit(
            "Import manifest not found; rerun after stage-import or pass --allow-without-import"
        )

    archived_files = [
        *_planned_archive_files(manifests_dir, Path("manifests")),
        *_planned_archive_files(bucketed_manifests_dir, Path("bucketed") / "manifests"),
        "retired_manifest.json",
    ]
    size_estimates = {
        "batch": _directory_stats(batch_dir),
        "originals": _directory_stats(batch_dir / "originals"),
        "extracted": _directory_stats(batch_dir / "extracted"),
        "bucketed_unique": _directory_stats(batch_dir / "bucketed" / "unique"),
        "manifests": _directory_stats(manifests_dir),
        "bucketed_manifests": _directory_stats(bucketed_manifests_dir),
    }
    size_estimates["estimated_prunable_bytes"] = (
        size_estimates["originals"]["total_bytes"]
        + size_estimates["extracted"]["total_bytes"]
        + size_estimates["bucketed_unique"]["total_bytes"]
    )

    payload = {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "batch_name": args.batch_name,
        "batch_dir": str(batch_dir),
        "archived_dir": str(archived_dir),
        "checks": {
            "stage_manifest_present": True,
            "import_manifest_present": import_manifest_path.is_file(),
            "allow_without_import": bool(args.allow_without_import),
        },
        "actions": {
            "dry_run": bool(args.dry_run),
            "overwrite_archive": bool(args.overwrite),
            "keep_batch": bool(args.keep_batch),
            "source_batch_removed": not args.dry_run and not args.keep_batch,
        },
        "archived_files": archived_files,
        "size_estimates": size_estimates,
        "snapshots": {
            "stage_manifest": _manifest_snapshot(stage_manifest_path),
            "import_manifest": _manifest_snapshot(import_manifest_path),
            "bucket_manifest": _manifest_snapshot(bucket_manifest_path),
            "duplicate_groups_manifest": _manifest_snapshot(duplicate_manifest_path),
        },
    }

    if args.dry_run:
        return payload

    if archived_dir.exists():
        if not args.overwrite:
            raise SystemExit(
                f"Archived manifest directory already exists: {archived_dir}; pass --overwrite to replace it"
            )
        _remove_path(archived_dir)

    copied_files = []
    copied_files.extend(_copy_tree(manifests_dir, archived_dir / "manifests", Path("manifests")))
    copied_files.extend(
        _copy_tree(
            bucketed_manifests_dir,
            archived_dir / "bucketed" / "manifests",
            Path("bucketed") / "manifests",
        )
    )
    copied_files.append("retired_manifest.json")
    payload["archived_files"] = copied_files
    write_json_file(str(archived_dir / "retired_manifest.json"), payload)

    if not args.keep_batch:
        shutil.rmtree(batch_dir)

    return payload


def main() -> int:
    payload = retire_batch(parse_args())
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
