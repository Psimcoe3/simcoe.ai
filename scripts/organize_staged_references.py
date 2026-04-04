"""
Create a non-destructive cleaned view of a staged reference batch by bucketing files,
deduplicating by content hash, and writing manifests for review.
"""

from __future__ import annotations

import argparse
import os
import shutil
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path

from data_contracts import infer_asset_kind, is_drawing_asset
from manifest_utils import current_utc_timestamp, runtime_manifest, sha256_file, write_json_file


DRAWING_EXTRA_PHRASES = (
    "layout",
    "detail",
    "details",
    "diagram",
    "diagrams",
    "riser",
    "risers",
    "legend",
    "legends",
    "section",
    "sections",
    "isometric",
    "sleeve location",
)
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".heic", ".heif"}
VIDEO_EXTENSIONS = {".mov", ".mp4", ".m4v", ".avi", ".mkv", ".wmv"}
AUDIO_EXTENSIONS = {".mp3", ".wav", ".aac", ".m4a", ".flac", ".ogg"}
EMAIL_EXTENSIONS = {".msg", ".eml"}
SPREADSHEET_EXTENSIONS = {".xlsx", ".xls", ".xlsm", ".xlsb", ".ods"}
DELIMITED_EXTENSIONS = {".csv", ".tsv"}
TEXT_DOCUMENT_EXTENSIONS = {".txt", ".md", ".rst"}
STRUCTURED_TEXT_EXTENSIONS = {".json", ".jsonl", ".yaml", ".yml"}
OFFICE_DOCUMENT_EXTENSIONS = {".doc", ".docx"}
IGNORED_FILENAMES = {"thumbs.db", "desktop.ini", ".ds_store"}
IGNORED_DIR_NAMES = {"__macosx"}


@dataclass(frozen=True)
class BucketClassification:
    asset_kind: str
    bucket_family: str
    bucket_subtype: str
    drawing_related: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Clean, dedupe, and bucket a staged reference batch into a non-destructive working view."
        )
    )
    parser.add_argument("--batch-dir", required=True, help="Batch directory created by stage_reference_archives.py")
    parser.add_argument(
        "--out-dir",
        help="Optional explicit output directory. Defaults to <batch-dir>/bucketed.",
    )
    parser.add_argument(
        "--link-mode",
        choices=["hardlink", "symlink", "copy"],
        default="hardlink",
        help="How to materialize unique files into the bucketed view (default: hardlink).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing output directory before organizing.",
    )
    return parser.parse_args()


def _normalized_text(value: str) -> str:
    normalized = value.replace("\\", "/").lower()
    normalized = normalized.replace("_", " ").replace("-", " ").replace("/", " ")
    return " ".join(normalized.split())


def _looks_like_drawing(relative_path: str, asset_kind: str) -> bool:
    if asset_kind == "cad_bim":
        return True
    directory_path = Path(relative_path).parent.as_posix()
    if directory_path != "." and is_drawing_asset(asset_kind, directory_path):
        return True
    if asset_kind not in {"document", "image"}:
        return False
    normalized = _normalized_text(relative_path)
    return any(phrase in normalized for phrase in DRAWING_EXTRA_PHRASES)


def classify_relative_path(relative_path: str) -> BucketClassification:
    suffix = Path(relative_path).suffix.lower()
    asset_kind = infer_asset_kind(relative_path)
    if suffix in IMAGE_EXTENSIONS and asset_kind == "other":
        asset_kind = "image"
    elif suffix in SPREADSHEET_EXTENSIONS and asset_kind == "other":
        asset_kind = "tabular"

    drawing_related = _looks_like_drawing(relative_path, asset_kind)

    if drawing_related:
        if asset_kind == "cad_bim":
            return BucketClassification(asset_kind=asset_kind, bucket_family="drawings", bucket_subtype="cad_bim", drawing_related=True)
        if suffix in IMAGE_EXTENSIONS:
            return BucketClassification(asset_kind=asset_kind, bucket_family="drawings", bucket_subtype="image", drawing_related=True)
        if suffix == ".pdf":
            return BucketClassification(asset_kind=asset_kind, bucket_family="drawings", bucket_subtype="pdf", drawing_related=True)
        if suffix in OFFICE_DOCUMENT_EXTENSIONS:
            return BucketClassification(asset_kind=asset_kind, bucket_family="drawings", bucket_subtype="office", drawing_related=True)
        return BucketClassification(asset_kind=asset_kind, bucket_family="drawings", bucket_subtype="document", drawing_related=True)

    if suffix in EMAIL_EXTENSIONS:
        return BucketClassification(asset_kind=asset_kind, bucket_family="documents", bucket_subtype="email_message", drawing_related=False)
    if asset_kind == "document":
        if suffix == ".pdf":
            subtype = "pdf"
        elif suffix in OFFICE_DOCUMENT_EXTENSIONS:
            subtype = "office"
        elif suffix in TEXT_DOCUMENT_EXTENSIONS:
            subtype = "text"
        elif suffix in STRUCTURED_TEXT_EXTENSIONS:
            subtype = "structured_text"
        else:
            subtype = "document"
        return BucketClassification(asset_kind=asset_kind, bucket_family="documents", bucket_subtype=subtype, drawing_related=False)
    if asset_kind == "code":
        return BucketClassification(asset_kind=asset_kind, bucket_family="documents", bucket_subtype="code", drawing_related=False)
    if asset_kind == "tabular":
        subtype = "delimited" if suffix in DELIMITED_EXTENSIONS else "spreadsheet"
        return BucketClassification(asset_kind=asset_kind, bucket_family="tabular", bucket_subtype=subtype, drawing_related=False)
    if suffix in IMAGE_EXTENSIONS:
        return BucketClassification(asset_kind="image", bucket_family="media", bucket_subtype="image", drawing_related=False)
    if suffix in VIDEO_EXTENSIONS:
        return BucketClassification(asset_kind=asset_kind, bucket_family="media", bucket_subtype="video", drawing_related=False)
    if suffix in AUDIO_EXTENSIONS:
        return BucketClassification(asset_kind=asset_kind, bucket_family="media", bucket_subtype="audio", drawing_related=False)
    return BucketClassification(asset_kind=asset_kind, bucket_family="other", bucket_subtype="other", drawing_related=False)


def _iter_candidate_files(extracted_root: Path):
    for path in sorted(extracted_root.rglob("*")):
        if not path.is_file():
            continue
        lowered_parts = {part.lower() for part in path.relative_to(extracted_root).parts[:-1]}
        if lowered_parts & IGNORED_DIR_NAMES:
            continue
        if path.name.lower() in IGNORED_FILENAMES:
            continue
        yield path


def _materialize_unique_file(source_path: Path, target_path: Path, link_mode: str) -> str:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    if link_mode == "hardlink":
        try:
            os.link(source_path, target_path)
            return "hardlink"
        except OSError:
            shutil.copy2(source_path, target_path)
            return "copy_fallback"
    if link_mode == "symlink":
        try:
            os.symlink(source_path, target_path)
            return "symlink"
        except OSError:
            shutil.copy2(source_path, target_path)
            return "copy_fallback"
    shutil.copy2(source_path, target_path)
    return "copy"


def organize_batch(batch_dir: Path, out_dir: Path, *, link_mode: str, overwrite: bool) -> tuple[Path, Path, Path]:
    extracted_root = batch_dir / "extracted"
    if not extracted_root.is_dir():
        raise SystemExit(f"Extracted root not found: {extracted_root}")

    if out_dir.exists():
        if not overwrite:
            raise SystemExit(f"Output directory already exists: {out_dir}")
        shutil.rmtree(out_dir)

    unique_root = out_dir / "unique"
    manifests_root = out_dir / "manifests"
    manifests_root.mkdir(parents=True, exist_ok=True)

    hash_to_canonical: dict[str, dict] = {}
    entries: list[dict] = []
    duplicate_groups: dict[str, list[dict]] = defaultdict(list)
    family_unique_counts: Counter[str] = Counter()
    family_duplicate_counts: Counter[str] = Counter()
    subtype_unique_counts: Counter[str] = Counter()
    subtype_duplicate_counts: Counter[str] = Counter()
    materialization_modes: Counter[str] = Counter()
    total_bytes = 0
    unique_bytes = 0

    for source_path in _iter_candidate_files(extracted_root):
        relative_source_path = source_path.relative_to(extracted_root).as_posix()
        classification = classify_relative_path(relative_source_path)
        digest = sha256_file(str(source_path))
        size_bytes = source_path.stat().st_size
        total_bytes += size_bytes
        bucket_key = f"{classification.bucket_family}/{classification.bucket_subtype}"
        bucket_relative_path = Path(classification.bucket_family) / classification.bucket_subtype / Path(relative_source_path)
        bucket_path = unique_root / bucket_relative_path

        canonical = hash_to_canonical.get(digest)
        if canonical is None:
            materialized_as = _materialize_unique_file(source_path, bucket_path, link_mode)
            materialization_modes[materialized_as] += 1
            unique_bytes += size_bytes
            family_unique_counts[classification.bucket_family] += 1
            subtype_unique_counts[bucket_key] += 1
            canonical = {
                "sha256": digest,
                "source_path": str(source_path),
                "relative_source_path": relative_source_path,
                "bucket_family": classification.bucket_family,
                "bucket_subtype": classification.bucket_subtype,
                "bucket_path": str(bucket_path),
                "size_bytes": size_bytes,
            }
            hash_to_canonical[digest] = canonical
            entry_status = "unique"
        else:
            family_duplicate_counts[classification.bucket_family] += 1
            subtype_duplicate_counts[bucket_key] += 1
            duplicate_groups[digest].append(
                {
                    "source_path": str(source_path),
                    "relative_source_path": relative_source_path,
                    "bucket_family": classification.bucket_family,
                    "bucket_subtype": classification.bucket_subtype,
                    "size_bytes": size_bytes,
                }
            )
            entry_status = "duplicate"

        entry = {
            "source_path": str(source_path),
            "relative_source_path": relative_source_path,
            "file_name": source_path.name,
            "size_bytes": size_bytes,
            "extension": source_path.suffix.lower() or None,
            "sha256": digest,
            "status": entry_status,
            **asdict(classification),
            "bucket_key": bucket_key,
            "bucket_relative_path": str(bucket_relative_path),
            "bucket_path": str(bucket_path) if entry_status == "unique" else None,
            "canonical_relative_source_path": canonical["relative_source_path"],
            "canonical_bucket_path": canonical["bucket_path"],
        }
        entries.append(entry)

    duplicate_payload = {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "batch_dir": str(batch_dir),
        "output_dir": str(out_dir),
        "duplicate_groups": [
            {
                "sha256": digest,
                "canonical": hash_to_canonical[digest],
                "duplicates": sorted(group, key=lambda item: item["relative_source_path"]),
            }
            for digest, group in sorted(duplicate_groups.items())
        ],
    }
    duplicate_manifest_path = manifests_root / "duplicate_groups.json"
    write_json_file(str(duplicate_manifest_path), duplicate_payload)

    summary = {
        "scanned_files": len(entries),
        "total_bytes": total_bytes,
        "unique_files": sum(1 for entry in entries if entry["status"] == "unique"),
        "unique_bytes": unique_bytes,
        "duplicate_files": sum(1 for entry in entries if entry["status"] == "duplicate"),
        "duplicate_groups": len(duplicate_groups),
        "by_family": {
            family: {
                "unique_files": family_unique_counts[family],
                "duplicate_files": family_duplicate_counts[family],
            }
            for family in sorted(
                set(family_unique_counts.keys())
                | set(family_duplicate_counts.keys())
                | {entry["bucket_family"] for entry in entries}
            )
        },
        "by_bucket": {
            bucket_key: {
                "unique_files": subtype_unique_counts[bucket_key],
                "duplicate_files": subtype_duplicate_counts[bucket_key],
            }
            for bucket_key in sorted(
                set(subtype_unique_counts.keys())
                | set(subtype_duplicate_counts.keys())
                | {entry["bucket_key"] for entry in entries}
            )
        },
        "materialization_modes": dict(sorted(materialization_modes.items())),
    }
    manifest = {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "batch_dir": str(batch_dir),
        "extracted_root": str(extracted_root),
        "output_dir": str(out_dir),
        "unique_root": str(unique_root),
        "link_mode_requested": link_mode,
        "runtime": runtime_manifest(),
        "summary": summary,
        "entries": sorted(entries, key=lambda item: item["relative_source_path"]),
    }
    manifest_path = manifests_root / "bucket_manifest.json"
    write_json_file(str(manifest_path), manifest)
    return manifest_path, duplicate_manifest_path, unique_root


def main() -> int:
    args = parse_args()
    batch_dir = Path(args.batch_dir).expanduser().resolve()
    if not batch_dir.is_dir():
        raise SystemExit(f"Batch directory not found: {batch_dir}")
    out_dir = Path(args.out_dir).expanduser().resolve() if args.out_dir else batch_dir / "bucketed"
    manifest_path, duplicate_manifest_path, unique_root = organize_batch(
        batch_dir,
        out_dir,
        link_mode=args.link_mode,
        overwrite=args.overwrite,
    )
    print(f"Wrote bucket manifest to {manifest_path}")
    print(f"Wrote duplicate groups to {duplicate_manifest_path}")
    print(f"Unique bucketed view available at {unique_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())