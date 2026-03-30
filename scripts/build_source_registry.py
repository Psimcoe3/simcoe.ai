"""
Build a machine-readable source registry from the configured external root.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from config_validation import (
    load_config,
    require_directory,
    validate_source_registry_config,
)
from data_contracts import infer_asset_kind, stable_identifier, suggested_ingestion_contract
from manifest_utils import current_utc_timestamp, file_metadata, write_json_file
from source_registry_utils import (
    managed_relative_path,
    materialized_manifest_path,
    repo_sync_dir,
    source_registry_namespace,
)


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


def main() -> int:
    args = parse_args()
    cfg = load_config(args.config)
    validate_source_registry_config(cfg)

    registry_cfg = cfg.get("source_registry")
    if not isinstance(registry_cfg, dict):
        raise SystemExit("Config must define a source_registry section")

    configured_root = Path(registry_cfg["root"])
    scan_root = Path(args.root or registry_cfg["root"])
    out_path = args.out or registry_cfg["manifest_path"]
    require_directory(str(scan_root), "Source registry root")

    relative_base = scan_root.resolve()
    if args.root:
        configured_root_resolved = configured_root.resolve()
        if relative_base.is_relative_to(configured_root_resolved):
            relative_base = configured_root_resolved

    namespace = source_registry_namespace(registry_cfg, str(relative_base))
    repo_sync_root = repo_sync_dir(registry_cfg)

    assets = []
    asset_kind_counts = Counter()
    extension_counts = Counter()
    total_bytes = 0

    for path in sorted(scan_root.rglob("*")):
        if not path.is_file():
            continue

        relative_path = path.resolve().relative_to(relative_base)
        asset_kind = infer_asset_kind(str(path))
        suggested = suggested_ingestion_contract(asset_kind)
        metadata = file_metadata(str(path), include_sha256=not args.skip_sha256)
        total_bytes += metadata["size_bytes"]
        asset_kind_counts[asset_kind] += 1
        extension_counts[path.suffix.lower() or "<none>"] += 1

        assets.append(
            {
                "registry_id": stable_identifier("source_asset", str(relative_path)),
                "relative_path": str(relative_path),
                "file_name": path.name,
                "extension": path.suffix.lower() or None,
                "asset_kind": asset_kind,
                "default_review_state": registry_cfg["default_review_state"],
                "default_data_family": registry_cfg["default_data_family"],
                "default_sft_candidate": False,
                "suggested_ingestion": suggested,
                "repo_managed_path": str(
                    Path(repo_sync_root)
                    / managed_relative_path(
                        str(relative_path),
                        asset_kind,
                        suggested.get("runtime_owner"),
                        namespace,
                    )
                ),
                **metadata,
            }
        )

    payload = {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "config_path": str(Path(args.config).resolve()),
        "root": str(relative_base),
        "scan_root": str(scan_root.resolve()),
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
            "sha256_included": not args.skip_sha256,
        },
        "assets": assets,
    }
    write_json_file(out_path, payload)
    print(f"Wrote {len(assets)} registered source assets to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())