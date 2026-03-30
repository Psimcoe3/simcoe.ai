"""
Shared helpers for writing machine-readable pipeline manifests.
"""

import hashlib
import json
import os
from datetime import datetime, timezone


def current_utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: str, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def summarise_numeric(values: list[int | float]) -> dict | None:
    if not values:
        return None

    total = sum(values)
    return {
        "count": len(values),
        "min": min(values),
        "max": max(values),
        "mean": round(total / len(values), 4),
    }


def read_json_file(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json_file(path: str, payload: dict) -> None:
    parent_dir = os.path.dirname(path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")