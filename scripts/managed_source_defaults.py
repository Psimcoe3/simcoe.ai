"""
Helpers for resolving repo-managed source defaults from config.
"""

from __future__ import annotations

from config_validation import load_config, validate_managed_sources_config


def load_managed_source_settings(config_path: str) -> dict:
    cfg = load_config(config_path)
    validate_managed_sources_config(cfg)
    managed_sources = cfg.get("managed_sources")
    return managed_sources if isinstance(managed_sources, dict) else {}


def resolve_managed_source_path(managed_sources: dict, *keys: str) -> str | None:
    for key in keys:
        value = managed_sources.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None
