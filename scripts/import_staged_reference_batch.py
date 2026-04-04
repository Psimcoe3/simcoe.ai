"""
Build a source registry and materialize actionable assets from a staged archive batch.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from build_source_registry import (
    build_source_registry_payload,
    build_source_registry_payload_from_assets,
)
from config_validation import (
    load_config,
    validate_managed_sources_config,
    validate_source_registry_config,
)
from manifest_utils import current_utc_timestamp, read_json_file, write_json_file
from materialize_sources import materialize_registry_assets


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ACTIONABLE_RUNTIME_OWNERS = ["retrieval", "multimodal", "geometry_rules"]
DEFAULT_BUCKET_MANIFEST = Path("bucketed") / "manifests" / "bucket_manifest.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Turn a staged archive batch into a registry manifest and materialize actionable assets "
            "into the repo-managed source tree."
        )
    )
    parser.add_argument("--config", default="config.electrician.yaml", help="Config file with source and managed-source settings")
    parser.add_argument(
        "--staging-root",
        default="data/staging/reference_archive_batches",
        help="Repo-relative or absolute root that holds staged batches",
    )
    parser.add_argument("--batch-name", required=True, help="Name of the staged batch directory")
    parser.add_argument(
        "--bucket-manifest",
        help=(
            "Optional organizer bucket manifest to use as the canonical import view. "
            "Defaults to <batch-dir>/bucketed/manifests/bucket_manifest.json when present."
        ),
    )
    parser.add_argument(
        "--use-extracted",
        action="store_true",
        help="Ignore any organizer bucket manifest and build the registry directly from the extracted tree.",
    )
    parser.add_argument("--skip-sha256", action="store_true", help="Skip per-file SHA256 hashing when building the registry")
    parser.add_argument("--runtime-owner", action="append", default=[], help="Runtime owners to materialize. Can be repeated.")
    parser.add_argument("--include-manual-review", action="store_true", help="Also materialize manual-review assets")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite already materialized files")
    parser.add_argument("--dry-run", action="store_true", help="Build manifests and selections without copying files")
    return parser.parse_args()


def _resolve_workspace_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def _runtime_owners_from_args(args: argparse.Namespace) -> list[str]:
    runtime_owners = list(args.runtime_owner)
    if not runtime_owners:
        runtime_owners = list(DEFAULT_ACTIONABLE_RUNTIME_OWNERS)
    if args.include_manual_review and "manual_review" not in runtime_owners:
        runtime_owners.append("manual_review")
    return runtime_owners


def _resolve_bucket_manifest_path(args: argparse.Namespace, batch_dir: Path) -> Path | None:
    if args.use_extracted:
        return None

    if args.bucket_manifest:
        bucket_manifest_path = _resolve_workspace_path(args.bucket_manifest).resolve()
        if not bucket_manifest_path.is_file():
            raise SystemExit(f"Bucket manifest not found: {bucket_manifest_path}")
        return bucket_manifest_path

    default_bucket_manifest = (batch_dir / DEFAULT_BUCKET_MANIFEST).resolve()
    if default_bucket_manifest.is_file():
        return default_bucket_manifest
    return None


def _bucket_manifest_asset_entries(bucket_manifest: dict) -> list[dict]:
    entries = bucket_manifest.get("entries")
    if not isinstance(entries, list):
        raise SystemExit("Bucket manifest is missing an entries array")

    asset_entries: list[dict] = []
    for entry in entries:
        if not isinstance(entry, dict) or entry.get("status") != "unique":
            continue

        relative_source_path = entry.get("relative_source_path")
        canonical_bucket_path = entry.get("canonical_bucket_path") or entry.get("bucket_path")
        if not isinstance(relative_source_path, str) or not relative_source_path.strip():
            raise SystemExit("Bucket manifest unique entry is missing relative_source_path")
        if not isinstance(canonical_bucket_path, str) or not canonical_bucket_path.strip():
            raise SystemExit("Bucket manifest unique entry is missing canonical_bucket_path")

        asset_entries.append(
            {
                "path": canonical_bucket_path,
                "relative_path": relative_source_path,
                "asset_kind": entry.get("asset_kind"),
                "source_note": "bucketed_canonical_view",
            }
        )

    if not asset_entries:
        raise SystemExit("Bucket manifest did not contain any unique canonical assets")
    return asset_entries


def main() -> int:
    args = parse_args()
    if args.use_extracted and args.bucket_manifest:
        raise SystemExit("--use-extracted cannot be combined with --bucket-manifest")

    cfg = load_config(args.config)
    validate_source_registry_config(cfg)
    validate_managed_sources_config(cfg)

    staging_root = _resolve_workspace_path(args.staging_root)
    batch_dir = staging_root / args.batch_name
    if not batch_dir.is_dir():
        raise SystemExit(f"Staged batch directory not found: {batch_dir}")

    manifests_dir = batch_dir / "manifests"
    stage_manifest_path = manifests_dir / "stage_manifest.json"
    if not stage_manifest_path.is_file():
        raise SystemExit(f"Stage manifest not found: {stage_manifest_path}")
    stage_manifest = read_json_file(str(stage_manifest_path))

    failed_archives = stage_manifest.get("summary", {}).get("failed_archives")
    if isinstance(failed_archives, list) and failed_archives:
        raise SystemExit(
            "Cannot import a staged batch with failed archives: " + ", ".join(str(item) for item in failed_archives)
        )

    extracted_dir = Path(str(stage_manifest.get("extracted_dir") or "")).resolve()
    if not extracted_dir.is_dir():
        raise SystemExit(f"Extracted directory not found: {extracted_dir}")

    bucket_manifest_path = _resolve_bucket_manifest_path(args, batch_dir)

    runtime_owners = _runtime_owners_from_args(args)
    registry_manifest_path = manifests_dir / "source_registry.json"
    materialized_manifest_path = manifests_dir / "materialized_sources.json"
    import_manifest_path = manifests_dir / "batch_import_manifest.json"

    source_view = {
        "mode": "extracted",
        "root": str(extracted_dir),
        "scan_root": str(extracted_dir),
        "bucket_manifest_path": None,
    }
    if bucket_manifest_path is not None:
        bucket_manifest = read_json_file(str(bucket_manifest_path))
        unique_root = Path(str(bucket_manifest.get("unique_root") or "")).resolve()
        if not unique_root.is_dir():
            raise SystemExit(f"Bucket unique root not found: {unique_root}")

        logical_root = Path(str(bucket_manifest.get("extracted_root") or extracted_dir)).resolve()
        if not logical_root.is_dir():
            raise SystemExit(f"Bucket logical root not found: {logical_root}")

        registry_payload = build_source_registry_payload_from_assets(
            cfg,
            config_path=args.config,
            root=logical_root,
            scan_root=unique_root,
            asset_entries=_bucket_manifest_asset_entries(bucket_manifest),
            skip_sha256=args.skip_sha256,
        )
        source_view = {
            "mode": "bucketed",
            "root": str(logical_root),
            "scan_root": str(unique_root),
            "bucket_manifest_path": str(bucket_manifest_path.resolve()),
        }
    else:
        registry_payload = build_source_registry_payload(
            cfg,
            config_path=args.config,
            scan_root=extracted_dir,
            skip_sha256=args.skip_sha256,
        )
    write_json_file(str(registry_manifest_path), registry_payload)

    materialized_manifest = materialize_registry_assets(
        cfg=cfg,
        config_path=args.config,
        registry=registry_payload,
        registry_path=str(registry_manifest_path),
        out_manifest_override=str(materialized_manifest_path),
        runtime_owners=runtime_owners,
        copy_all=True,
        overwrite=args.overwrite,
        dry_run=args.dry_run,
    )

    import_manifest = {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "config_path": str(Path(args.config).resolve()),
        "batch_name": args.batch_name,
        "batch_dir": str(batch_dir.resolve()),
        "stage_manifest_path": str(stage_manifest_path.resolve()),
        "registry_manifest_path": str(registry_manifest_path.resolve()),
        "materialized_manifest_path": str(materialized_manifest_path.resolve()),
        "selection": {
            "runtime_owners": runtime_owners,
            "overwrite": args.overwrite,
            "dry_run": args.dry_run,
            "skip_sha256": args.skip_sha256,
        },
        "source_view": source_view,
        "stage_summary": stage_manifest.get("summary"),
        "registry_summary": registry_payload.get("summary"),
        "materialization_summary": materialized_manifest.get("summary"),
    }
    write_json_file(str(import_manifest_path), import_manifest)

    print(f"Built staged-batch registry: {registry_manifest_path}")
    print(f"Materialization manifest: {materialized_manifest_path}")
    print(f"Import manifest: {import_manifest_path}")
    print(f"Registry source view: {source_view['mode']} ({source_view['scan_root']})")
    print(
        "Selected runtime owners: "
        + ", ".join(runtime_owners)
        + f" | assets={registry_payload['summary']['asset_count']}"
        + f" | selected={materialized_manifest['summary']['selected_count']}"
        + f" | copied={materialized_manifest['summary']['copied_count']}"
    )
    if args.dry_run:
        print("Dry run complete; no files were copied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())