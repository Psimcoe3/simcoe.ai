"""
Build a machine-readable source registry from the configured external root.
"""

from __future__ import annotations

import argparse
import os
from collections import Counter
from pathlib import Path

from config_validation import (
    load_config,
    require_directory,
    validate_managed_sources_config,
    validate_source_registry_config,
)
from data_contracts import infer_asset_kind, stable_identifier, suggested_ingestion_contract
from manifest_utils import current_utc_timestamp, file_metadata, write_json_file
from source_registry_utils import (
    resolve_repo_managed_path,
    materialized_manifest_path,
    repo_sync_dir,
    source_registry_namespace,
)



def _normalize_relative_path(relative_path: str) -> str:
    return Path(str(relative_path).replace("\\", "/")).as_posix().lstrip("/")


def build_source_registry_payload_from_assets(
    cfg: dict,
    *,
    config_path: str,
    root: Path,
    scan_root: Path,
    asset_entries: list[dict],
    skip_sha256: bool = False,
) -> dict:
    validate_source_registry_config(cfg)
    validate_managed_sources_config(cfg)

    registry_cfg = cfg.get("source_registry")
    if not isinstance(registry_cfg, dict):
        raise SystemExit("Config must define a source_registry section")
    managed_sources_cfg = cfg.get("managed_sources") if isinstance(cfg.get("managed_sources"), dict) else {}

    root = root.resolve()
    scan_root = scan_root.resolve()
    require_directory(str(root), "Source registry root")
    require_directory(str(scan_root), "Source registry scan root")

    namespace = source_registry_namespace(registry_cfg, str(root))
    repo_sync_root = repo_sync_dir(registry_cfg)

    assets = []
    asset_kind_counts = Counter()
    extension_counts = Counter()
    runtime_owner_counts = Counter()
    pipeline_counts = Counter()
    route_counts = Counter()
    total_bytes = 0

    for asset_entry in asset_entries:
        if not isinstance(asset_entry, dict):
            raise SystemExit("Registry asset entries must be dictionaries")

        path_value = asset_entry.get("path")
        relative_path_value = asset_entry.get("relative_path")
        if not isinstance(path_value, str) or not path_value.strip():
            raise SystemExit("Registry asset entry is missing a source path")
        if not isinstance(relative_path_value, str) or not relative_path_value.strip():
            raise SystemExit("Registry asset entry is missing a relative_path")

        source_path = Path(path_value).resolve()
        if not source_path.is_file():
            raise SystemExit(f"Registry asset path not found: {source_path}")

        relative_path = _normalize_relative_path(relative_path_value)
        asset_kind = str(asset_entry.get("asset_kind") or infer_asset_kind(relative_path))
        suggested = asset_entry.get("suggested_ingestion") if isinstance(asset_entry.get("suggested_ingestion"), dict) else None
        if suggested is None:
            suggested = suggested_ingestion_contract(asset_kind, relative_path)

        metadata = file_metadata(os.fspath(source_path), include_sha256=not skip_sha256)
        total_bytes += metadata["size_bytes"]
        asset_kind_counts[asset_kind] += 1
        extension_counts[source_path.suffix.lower() or "<none>"] += 1
        runtime_owner_counts[str(suggested.get("runtime_owner") or "unassigned")] += 1
        pipeline_counts[str(suggested.get("pipeline") or "unassigned")] += 1
        route_counts[str(suggested.get("route") or "unassigned")] += 1

        asset_record = {
            "registry_id": stable_identifier("source_asset", relative_path),
            "relative_path": relative_path,
            "file_name": source_path.name,
            "extension": source_path.suffix.lower() or None,
            "asset_kind": asset_kind,
            "default_review_state": registry_cfg["default_review_state"],
            "default_data_family": registry_cfg["default_data_family"],
            "default_sft_candidate": False,
            "suggested_ingestion": suggested,
            "repo_managed_path": resolve_repo_managed_path(
                relative_path=relative_path,
                asset_kind=asset_kind,
                suggested_ingestion=suggested,
                namespace=namespace,
                repo_sync_root=repo_sync_root,
                managed_sources_cfg=managed_sources_cfg,
            ),
            **metadata,
        }
        source_note = asset_entry.get("source_note")
        if isinstance(source_note, str) and source_note.strip():
            asset_record["source_note"] = source_note
        assets.append(asset_record)

    return {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "config_path": str(Path(config_path).resolve()),
        "root": str(root),
        "scan_root": str(scan_root),
        "defaults": {
            "review_state": registry_cfg["default_review_state"],
            "data_family": registry_cfg["default_data_family"],
            "allow_auto_sft": False,
        },
        "repo_sync": {
            "namespace": namespace,
            "root": repo_sync_root,
            "materialized_manifest_path": materialized_manifest_path(registry_cfg),
        },
        "summary": {
            "asset_count": len(assets),
            "total_bytes": total_bytes,
            "by_asset_kind": dict(sorted(asset_kind_counts.items())),
            "by_extension": dict(sorted(extension_counts.items())),
            "by_suggested_runtime_owner": dict(sorted(runtime_owner_counts.items())),
            "by_suggested_pipeline": dict(sorted(pipeline_counts.items())),
            "by_suggested_route": dict(sorted(route_counts.items())),
            "sha256_included": not skip_sha256,
        },
        "assets": assets,
    }

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a registry of external source assets")
    parser.add_argument("--config", default="config.yaml", help="Config file with source_registry settings")
    parser.add_argument("--root", help="Override the configured source registry root")
    parser.add_argument("--out", help="Override the configured source registry manifest output path")
    parser.add_argument(
        "--skip_sha256",
        action="store_true",
        help="Skip per-file SHA256 hashing when building the registry",
    )
    return parser.parse_args()


def build_source_registry_payload(
    cfg: dict,
    *,
    config_path: str,
    scan_root: Path,
    skip_sha256: bool = False,
) -> dict:
    registry_cfg = cfg.get("source_registry")
    if not isinstance(registry_cfg, dict):
        raise SystemExit("Config must define a source_registry section")

    configured_root = Path(registry_cfg["root"])
    scan_root = scan_root.resolve()
    require_directory(str(scan_root), "Source registry root")

    relative_base = scan_root
    configured_root_resolved = configured_root.resolve()
    if scan_root.is_relative_to(configured_root_resolved):
        relative_base = configured_root_resolved

    relative_base_str = os.fspath(relative_base)
    scan_root_str = os.fspath(scan_root)
    asset_entries: list[dict] = []

    for current_root, dirnames, filenames in os.walk(scan_root_str):
        dirnames.sort()
        filenames.sort()

        for filename in filenames:
            path_str = os.path.join(current_root, filename)
            relative_path = os.path.relpath(path_str, relative_base_str)
            asset_entries.append(
                {
                    "path": path_str,
                    "relative_path": relative_path,
                }
            )

    return build_source_registry_payload_from_assets(
        cfg,
        config_path=config_path,
        root=relative_base,
        scan_root=scan_root,
        asset_entries=asset_entries,
        skip_sha256=skip_sha256,
    )


def main() -> int:
    args = parse_args()
    cfg = load_config(args.config)
    registry_cfg = cfg.get("source_registry")
    if not isinstance(registry_cfg, dict):
        raise SystemExit("Config must define a source_registry section")
    scan_root = Path(args.root or registry_cfg["root"])
    out_path = args.out or registry_cfg["manifest_path"]
    payload = build_source_registry_payload(
        cfg,
        config_path=args.config,
        scan_root=scan_root,
        skip_sha256=args.skip_sha256,
    )
    write_json_file(out_path, payload)
    print(f"Wrote {payload['summary']['asset_count']} registered source assets to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())