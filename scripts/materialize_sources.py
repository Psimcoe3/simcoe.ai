"""
Copy selected external registry assets into repo-managed source storage.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from config_validation import load_config, require_file, validate_source_registry_config
from manifest_utils import current_utc_timestamp, read_json_file, write_json_file
from source_registry_utils import (
    managed_relative_path,
    materialized_manifest_path,
    repo_sync_dir,
    source_registry_namespace,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy selected external source assets into the repo-managed sources tree."
    )
    parser.add_argument("--config", default="config.yaml", help="Config file with source_registry settings")
    parser.add_argument("--registry", help="Override the registry manifest path")
    parser.add_argument("--repo-dir", help="Override the repo-managed source root")
    parser.add_argument("--out-manifest", help="Override the materialization manifest output path")
    parser.add_argument(
        "--registry-id",
        action="append",
        default=[],
        help="Select a specific registry asset id. Can be provided multiple times.",
    )
    parser.add_argument(
        "--relative-path",
        action="append",
        default=[],
        help="Select a specific source-relative path. Can be provided multiple times.",
    )
    parser.add_argument(
        "--path-prefix",
        action="append",
        default=[],
        help="Select all assets under a relative path prefix. Can be provided multiple times.",
    )
    parser.add_argument(
        "--asset-kind",
        action="append",
        default=[],
        help="Optional filter on asset_kind after primary selection.",
    )
    parser.add_argument(
        "--runtime-owner",
        action="append",
        default=[],
        help="Optional filter on suggested_ingestion.runtime_owner after primary selection.",
    )
    parser.add_argument(
        "--pipeline",
        action="append",
        default=[],
        help="Optional filter on suggested_ingestion.pipeline after primary selection.",
    )
    parser.add_argument(
        "--copy-all",
        action="store_true",
        help="Copy all assets from the registry manifest.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite repo-managed files that already exist.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Resolve and report copy destinations without copying files.",
    )
    return parser.parse_args()


def _normalize_path(value: str) -> str:
    return str(Path(value.replace("\\", "/")).as_posix()).strip("/")


def _matches_primary(asset: dict, args: argparse.Namespace) -> bool:
    if args.copy_all:
        return True

    relative_path = _normalize_path(str(asset.get("relative_path") or ""))
    if args.registry_id and asset.get("registry_id") in set(args.registry_id):
        return True
    if args.relative_path and relative_path in {_normalize_path(value) for value in args.relative_path}:
        return True

    for prefix in args.path_prefix:
        normalized_prefix = _normalize_path(prefix)
        if relative_path == normalized_prefix or relative_path.startswith(f"{normalized_prefix}/"):
            return True
    return False


def _matches_filters(asset: dict, args: argparse.Namespace) -> bool:
    suggested = asset.get("suggested_ingestion") if isinstance(asset.get("suggested_ingestion"), dict) else {}

    if args.asset_kind and asset.get("asset_kind") not in set(args.asset_kind):
        return False
    if args.runtime_owner and suggested.get("runtime_owner") not in set(args.runtime_owner):
        return False
    if args.pipeline and suggested.get("pipeline") not in set(args.pipeline):
        return False
    return True


def selected_assets(assets: list[dict], args: argparse.Namespace) -> list[dict]:
    selected = [asset for asset in assets if _matches_primary(asset, args) and _matches_filters(asset, args)]
    return sorted(selected, key=lambda item: str(item.get("relative_path") or ""))


def target_path_for_asset(asset: dict, repo_root: Path, repo_dir: str, namespace: str) -> Path:
    suggested = asset.get("suggested_ingestion") if isinstance(asset.get("suggested_ingestion"), dict) else {}
    relative_target = managed_relative_path(
        str(asset.get("relative_path") or ""),
        str(asset.get("asset_kind") or "other"),
        suggested.get("runtime_owner") if isinstance(suggested, dict) else None,
        namespace,
    )
    return repo_root / repo_dir / relative_target


def source_path_for_asset(asset: dict, registry_root: Path) -> Path:
    explicit_path = asset.get("path")
    if isinstance(explicit_path, str) and explicit_path.strip():
        return Path(explicit_path)
    return registry_root / str(asset.get("relative_path") or "")


def main() -> int:
    args = parse_args()
    cfg = load_config(args.config)
    validate_source_registry_config(cfg)

    source_registry = cfg.get("source_registry")
    if not isinstance(source_registry, dict):
        raise SystemExit("Config must define a source_registry section")

    registry_path = args.registry or source_registry["manifest_path"]
    require_file(registry_path, "Source registry manifest")
    registry = read_json_file(registry_path)

    assets = registry.get("assets")
    if not isinstance(assets, list):
        raise SystemExit("Registry manifest is missing an assets array")

    if not (args.copy_all or args.registry_id or args.relative_path or args.path_prefix):
        raise SystemExit(
            "Choose assets with --registry-id, --relative-path, --path-prefix, or use --copy-all"
        )

    registry_root = Path(str(registry.get("root") or source_registry["root"]))
    repo_dir = args.repo_dir or repo_sync_dir(source_registry)
    out_manifest = args.out_manifest or materialized_manifest_path(source_registry)
    namespace = source_registry_namespace(source_registry, str(registry_root))

    chosen_assets = selected_assets(assets, args)
    if not chosen_assets:
        raise SystemExit("No registry assets matched the provided selectors")

    copied = 0
    already_present = 0
    errors = []
    materialized_assets = []

    for asset in chosen_assets:
        source_path = source_path_for_asset(asset, registry_root)
        target_path = target_path_for_asset(asset, REPO_ROOT, repo_dir, namespace)
        relative_target_path = target_path.relative_to(REPO_ROOT).as_posix()

        status = "dry_run"
        if not source_path.is_file():
            status = "missing_source"
            errors.append(f"Missing source file: {source_path}")
        elif target_path.exists() and not args.overwrite:
            status = "already_present"
            already_present += 1
        elif not args.dry_run:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, target_path)
            status = "copied"
            copied += 1

        materialized_assets.append(
            {
                "registry_id": asset.get("registry_id"),
                "relative_path": asset.get("relative_path"),
                "asset_kind": asset.get("asset_kind"),
                "source_path": str(source_path),
                "repo_managed_path": relative_target_path,
                "status": status,
                "suggested_ingestion": asset.get("suggested_ingestion"),
                "size_bytes": asset.get("size_bytes"),
                "sha256": asset.get("sha256"),
            }
        )

    manifest = {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "config_path": str((REPO_ROOT / args.config).resolve()) if not Path(args.config).is_absolute() else str(Path(args.config).resolve()),
        "registry_manifest_path": str(Path(registry_path).resolve()),
        "registry_root": str(registry_root.resolve()),
        "repo_sync": {
            "namespace": namespace,
            "root": repo_dir,
        },
        "selection": {
            "copy_all": args.copy_all,
            "registry_ids": args.registry_id,
            "relative_paths": args.relative_path,
            "path_prefixes": args.path_prefix,
            "asset_kinds": args.asset_kind,
            "runtime_owners": args.runtime_owner,
            "pipelines": args.pipeline,
            "overwrite": args.overwrite,
            "dry_run": args.dry_run,
        },
        "summary": {
            "selected_count": len(chosen_assets),
            "copied_count": copied,
            "already_present_count": already_present,
            "error_count": len(errors),
        },
        "assets": materialized_assets,
        "errors": errors,
    }
    write_json_file(out_manifest, manifest)

    if errors:
        raise SystemExit(
            f"Materialization wrote manifest to {out_manifest} but found {len(errors)} missing source files"
        )

    print(f"Selected {len(chosen_assets)} registry assets")
    print(f"Manifest written to {out_manifest}")
    if args.dry_run:
        print("Dry run complete; no files were copied")
    else:
        print(f"Copied {copied} files into {repo_dir}")
        if already_present:
            print(f"Skipped {already_present} files already present in the repo")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
