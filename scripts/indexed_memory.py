"""
File-backed indexed memory with a pointer-only index, on-demand topic files,
and an append-only event log.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
from typing import Protocol

import yaml

from config_validation import load_config, validate_dream_config, validate_memory_config
from data_contracts import stable_identifier
from manifest_utils import current_utc_timestamp, read_json_file, write_json_file
from retrieval_utils import score_document


MEMORY_SCHEMA_VERSION = 1
DREAM_SCHEMA_VERSION = 1
MEMORY_KINDS = {"operator_note", "verified_fact", "decision", "exception"}
MEMORY_STATUSES = {"active", "stale", "retracted"}
MEMORY_VERIFICATION_STATUSES = {"verified", "unverified", "disputed"}
MEMORY_CONTRADICTION_POLICIES = {"mark_stale", "track_only"}
MEMORY_PROVIDERS = {"file"}


def _memory_cfg(cfg: dict) -> dict:
    section = cfg.get("memory") if isinstance(cfg.get("memory"), dict) else {}
    return {
        "enabled": bool(section.get("enabled", False)),
        "provider": str(section.get("provider") or "file"),
        "root_dir": str(section.get("root_dir") or "data/memory"),
        "index_path": str(section.get("index_path") or "data/memory/MEMORY.json"),
        "topics_dir": str(section.get("topics_dir") or "data/memory/topics"),
        "events_path": str(section.get("events_path") or "data/memory/events.jsonl"),
        "default_top_k": int(section.get("default_top_k", 3) or 3),
        "topic_candidate_limit": int(section.get("topic_candidate_limit", 8) or 8),
        "max_context_chars": int(section.get("max_context_chars", 1200) or 1200),
        "max_index_entries": int(section.get("max_index_entries", 64) or 64),
        "max_summary_chars": int(section.get("max_summary_chars", 160) or 160),
        "max_supporting_observations": int(section.get("max_supporting_observations", 3) or 3),
        "max_trace_results": int(section.get("max_trace_results", 3) or 3),
        "max_trace_excluded": int(section.get("max_trace_excluded", 3) or 3),
        "min_score": float(section.get("min_score", 2) or 2),
        "require_verification": bool(section.get("require_verification", True)),
        "contradiction_policy": str(section.get("contradiction_policy") or "mark_stale"),
        "exclude_contradicted_topics": bool(section.get("exclude_contradicted_topics", True)),
        "import_max_records": int(section.get("import_max_records", 250) or 250),
        "allowed_kinds": list(section.get("allowed_kinds") or sorted(MEMORY_KINDS)),
        "exclude_statuses": list(section.get("exclude_statuses") or ["stale", "retracted"]),
        "consolidation_min_events": int(section.get("consolidation_min_events", 8) or 8),
    }


def _dream_cfg(cfg: dict) -> dict:
    section = cfg.get("dream") if isinstance(cfg.get("dream"), dict) else {}
    memory_root = Path(_memory_cfg(cfg)["root_dir"])
    root_dir = Path(str(section.get("root_dir") or (memory_root / "dream")))
    return {
        "enabled": bool(section.get("enabled", False)),
        "root_dir": str(root_dir),
        "state_path": str(Path(str(section.get("state_path") or (root_dir / "state.json")))),
        "lock_path": str(Path(str(section.get("lock_path") or (root_dir / "consolidation.lock")))),
        "log_dir": str(Path(str(section.get("log_dir") or (root_dir / "daily_logs")))),
        "minimum_hours_between_runs": int(section.get("minimum_hours_between_runs", 24) or 24),
        "minimum_sessions_between_runs": int(section.get("minimum_sessions_between_runs", 5) or 5),
        "lock_timeout_seconds": int(section.get("lock_timeout_seconds", 900) or 900),
        "max_recent_logs": int(section.get("max_recent_logs", 200) or 200),
        "max_persistable_entries_per_run": int(
            section.get("max_persistable_entries_per_run", 32) or 32
        ),
        "brief_summary_chars": int(section.get("brief_summary_chars", 160) or 160),
    }


def _ensure_layout(settings: dict) -> None:
    root_dir = Path(settings["root_dir"])
    topics_dir = Path(settings["topics_dir"])
    index_path = Path(settings["index_path"])
    events_path = Path(settings["events_path"])

    root_dir.mkdir(parents=True, exist_ok=True)
    topics_dir.mkdir(parents=True, exist_ok=True)
    index_path.parent.mkdir(parents=True, exist_ok=True)
    events_path.parent.mkdir(parents=True, exist_ok=True)

    if not events_path.exists():
        events_path.write_text("", encoding="utf-8")

    if not index_path.exists():
        write_json_file(
            str(index_path),
            {
                "schema_version": MEMORY_SCHEMA_VERSION,
                "generated_at": current_utc_timestamp(),
                "topic_count": 0,
                "topics": [],
            },
        )


def _coerce_datetime(value: object) -> datetime | None:
    if isinstance(value, datetime):
        dt = value
    elif isinstance(value, str) and value.strip():
        try:
            dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        except ValueError:
            return None
    else:
        return None

    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _coerce_now(value: object | None = None) -> datetime:
    if value is None:
        return datetime.now(timezone.utc)
    dt = _coerce_datetime(value)
    if dt is None:
        raise ValueError("Dream timestamps must be ISO-8601 strings or timezone-aware datetimes")
    return dt


def _datetime_to_timestamp(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat()


def _default_dream_state() -> dict:
    timestamp = current_utc_timestamp()
    return {
        "schema_version": DREAM_SCHEMA_VERSION,
        "generated_at": timestamp,
        "updated_at": timestamp,
        "dream_count": 0,
        "session_count": 0,
        "last_session_at": None,
        "last_session_id": None,
        "last_dream_at": None,
        "last_dream_session_count": 0,
        "last_processed_log_at": None,
        "last_processed_log_entry_id": None,
        "last_run": None,
    }


def _ensure_dream_layout(settings: dict) -> None:
    root_dir = Path(settings["root_dir"])
    state_path = Path(settings["state_path"])
    lock_path = Path(settings["lock_path"])
    log_dir = Path(settings["log_dir"])

    root_dir.mkdir(parents=True, exist_ok=True)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    if not state_path.exists():
        write_json_file(str(state_path), _default_dream_state())


def _load_dream_state(settings: dict) -> dict:
    _ensure_dream_layout(settings)
    state_path = Path(settings["state_path"])
    try:
        payload = read_json_file(str(state_path))
    except (FileNotFoundError, json.JSONDecodeError):
        payload = _default_dream_state()
        write_json_file(str(state_path), payload)

    if not isinstance(payload, dict):
        payload = _default_dream_state()
        write_json_file(str(state_path), payload)
    return payload


def _write_dream_state(settings: dict, state: dict) -> dict:
    payload = _default_dream_state()
    payload.update(state)
    payload["schema_version"] = DREAM_SCHEMA_VERSION
    payload.setdefault("generated_at", current_utc_timestamp())
    payload["updated_at"] = current_utc_timestamp()
    write_json_file(settings["state_path"], payload)
    return payload


def _dream_log_path(settings: dict, generated_at: str) -> Path:
    generated_dt = _coerce_datetime(generated_at) or datetime.now(timezone.utc)
    return Path(settings["log_dir"]) / f"{generated_dt.strftime('%Y-%m-%d')}.jsonl"


def _append_dream_log_row(settings: dict, payload: dict) -> None:
    _ensure_dream_layout(settings)
    log_path = _dream_log_path(settings, str(payload["generated_at"]))
    with open(log_path, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True) + "\n")


def _load_dream_log_entries(
    settings: dict,
    *,
    since_generated_at: str | None = None,
    since_entry_id: str | None = None,
) -> list[dict]:
    _ensure_dream_layout(settings)
    since_dt = _coerce_datetime(since_generated_at)
    cleaned_since_entry_id = (
        since_entry_id.strip()
        if isinstance(since_entry_id, str) and since_entry_id.strip()
        else None
    )
    entries: list[dict] = []

    for log_path in sorted(Path(settings["log_dir"]).glob("*.jsonl")):
        with open(log_path, "r", encoding="utf-8") as handle:
            for line in handle:
                stripped = line.strip()
                if not stripped:
                    continue
                payload = json.loads(stripped)
                if not isinstance(payload, dict):
                    continue
                generated_dt = _coerce_datetime(payload.get("generated_at"))
                entry_id = str(payload.get("entry_id") or "")
                if since_dt is not None and generated_dt is not None:
                    if generated_dt < since_dt:
                        continue
                    if (
                        generated_dt == since_dt
                        and cleaned_since_entry_id is not None
                        and entry_id <= cleaned_since_entry_id
                    ):
                        continue
                elif since_dt is not None and generated_dt is None:
                    continue
                payload["log_path"] = str(log_path.resolve())
                entries.append(payload)

    entries.sort(
        key=lambda item: (str(item.get("generated_at") or ""), str(item.get("entry_id") or ""))
    )
    return entries


def _normalize_persist_memory_entry(settings: dict, log_entry: dict) -> dict | None:
    persist_memory = log_entry.get("persist_memory")
    if not isinstance(persist_memory, dict):
        return None
    if bool(persist_memory.get("derivable", False)):
        return None

    topic = str(persist_memory.get("topic") or "").strip()
    content = str(persist_memory.get("content") or persist_memory.get("body") or "").strip()
    if not topic or not content:
        return None

    summary = str(persist_memory.get("summary") or log_entry.get("summary") or "").strip()
    if not summary:
        summary = _truncate(content, settings["brief_summary_chars"])

    source = str(
        persist_memory.get("source")
        or f"dream_log:{str(log_entry.get('source') or 'unknown').strip() or 'unknown'}"
    ).strip()
    return {
        "topic": topic,
        "summary": summary,
        "content": content,
        "kind": str(persist_memory.get("kind") or "operator_note"),
        "status": str(persist_memory.get("status") or "active"),
        "verification_status": str(persist_memory.get("verification_status") or "unverified"),
        "source": source,
        "tags": persist_memory.get("tags") or [],
        "supersedes": persist_memory.get("supersedes"),
        "contradicts": persist_memory.get("contradicts"),
        "generated_at": str(
            persist_memory.get("generated_at")
            or log_entry.get("generated_at")
            or current_utc_timestamp()
        ),
    }


def _load_dream_lock_info(settings: dict, now: datetime) -> dict:
    _ensure_dream_layout(settings)
    lock_path = Path(settings["lock_path"])
    payload: dict | None = None
    if lock_path.exists():
        try:
            payload = read_json_file(str(lock_path))
        except (FileNotFoundError, json.JSONDecodeError):
            payload = {"schema_version": DREAM_SCHEMA_VERSION}

    acquired_at = (
        _coerce_datetime(payload.get("acquired_at")) if isinstance(payload, dict) else None
    )
    age_seconds = None
    stale = False
    if lock_path.exists():
        if acquired_at is None:
            stale = True
        else:
            age_seconds = max((now - acquired_at).total_seconds(), 0.0)
            stale = age_seconds >= float(settings["lock_timeout_seconds"])

    return {
        "path": str(lock_path.resolve()),
        "exists": lock_path.exists(),
        "active": lock_path.exists() and not stale,
        "stale": stale,
        "age_seconds": round(age_seconds, 4) if age_seconds is not None else None,
        "timeout_seconds": int(settings["lock_timeout_seconds"]),
        "payload": payload,
    }


def _acquire_dream_lock(settings: dict, now: datetime) -> dict:
    _ensure_dream_layout(settings)
    lock_info = _load_dream_lock_info(settings, now)
    lock_path = Path(settings["lock_path"])
    if lock_info["stale"] and lock_path.exists():
        lock_path.unlink(missing_ok=True)
    elif lock_info["active"]:
        raise RuntimeError("dream lock is already held")

    payload = {
        "schema_version": DREAM_SCHEMA_VERSION,
        "acquired_at": _datetime_to_timestamp(now),
        "pid": os.getpid(),
    }
    try:
        with open(lock_path, "x", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
    except FileExistsError as exc:
        raise RuntimeError("dream lock is already held") from exc
    return payload


def _release_dream_lock(settings: dict) -> None:
    Path(settings["lock_path"]).unlink(missing_ok=True)


def _normalized_text(value: str | None) -> str:
    if not isinstance(value, str) or not value.strip():
        return ""
    return " ".join(value.strip().lower().split())


def _clean_string_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        cleaned = value.strip()
        return [cleaned] if cleaned else []
    if not isinstance(value, list):
        return []
    return sorted({str(item).strip() for item in value if str(item).strip()})


def _topic_id(topic: str) -> str:
    return stable_identifier("memory_topic", _normalized_text(topic))


def _truncate(text: str, limit: int) -> str:
    cleaned = " ".join((text or "").split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: max(limit - 3, 1)].rstrip() + "..."


def _normalize_event_links(value: object) -> list[str]:
    return _clean_string_list(value)


def _load_events(settings: dict) -> list[dict]:
    _ensure_layout(settings)
    events: list[dict] = []
    with open(settings["events_path"], "r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                events.append(json.loads(stripped))
    return sorted(events, key=lambda item: item.get("generated_at", ""))


def _append_events(settings: dict, events: list[dict]) -> None:
    if not events:
        return
    _ensure_layout(settings)
    with open(settings["events_path"], "a", encoding="utf-8") as handle:
        for event in events:
            handle.write(json.dumps(event, sort_keys=True) + "\n")


def _validate_entry_shape(
    settings: dict,
    *,
    topic: str,
    content: str,
    kind: str,
    status: str,
    verification_status: str,
) -> None:
    if not topic.strip():
        raise ValueError("Memory topic must be a non-empty string")
    if not content.strip():
        raise ValueError("Memory content must be a non-empty string")
    if kind not in set(settings["allowed_kinds"]):
        raise ValueError(f"Unsupported memory kind: {kind}")
    if status not in MEMORY_STATUSES:
        raise ValueError(f"Unsupported memory status: {status}")
    if verification_status not in MEMORY_VERIFICATION_STATUSES:
        raise ValueError(f"Unsupported verification status: {verification_status}")


def _build_memory_event(
    settings: dict,
    *,
    topic: str,
    summary: str,
    content: str,
    kind: str = "operator_note",
    status: str = "active",
    verification_status: str = "verified",
    source: str | None = "manual",
    tags: object = None,
    supersedes: str | None = None,
    contradicts: object = None,
    generated_at: str | None = None,
) -> dict:
    _validate_entry_shape(
        settings,
        topic=topic,
        content=content,
        kind=kind,
        status=status,
        verification_status=verification_status,
    )
    cleaned_topic = " ".join(topic.split())
    cleaned_content = content.strip()
    cleaned_summary = " ".join(summary.split()) or _truncate(
        cleaned_content,
        settings["max_summary_chars"],
    )
    cleaned_tags = _clean_string_list(tags)
    cleaned_supersedes = (
        supersedes.strip() if isinstance(supersedes, str) and supersedes.strip() else None
    )
    cleaned_contradicts = [
        event_id
        for event_id in _normalize_event_links(contradicts)
        if event_id != cleaned_supersedes
    ]
    cleaned_generated_at = (
        generated_at.strip()
        if isinstance(generated_at, str) and generated_at.strip()
        else current_utc_timestamp()
    )
    cleaned_source = source.strip() if isinstance(source, str) and source.strip() else None
    topic_id = _topic_id(cleaned_topic)
    event_id = stable_identifier(
        "memory_event",
        topic_id,
        kind,
        status,
        verification_status,
        cleaned_summary,
        cleaned_content,
        json.dumps(cleaned_tags, sort_keys=True),
        cleaned_supersedes or "",
        json.dumps(cleaned_contradicts, sort_keys=True),
        cleaned_source or "",
        cleaned_generated_at,
    )

    return {
        "schema_version": MEMORY_SCHEMA_VERSION,
        "event_id": event_id,
        "topic_id": topic_id,
        "topic": cleaned_topic,
        "kind": kind,
        "status": status,
        "verification_status": verification_status,
        "summary": cleaned_summary,
        "content": cleaned_content,
        "tags": cleaned_tags,
        "source": cleaned_source,
        "supersedes": cleaned_supersedes,
        "contradicts": cleaned_contradicts,
        "generated_at": cleaned_generated_at,
    }


def _observation_payload(event: dict) -> dict:
    return {
        "event_id": event["event_id"],
        "kind": event["kind"],
        "status": event["status"],
        "verification_status": event["verification_status"],
        "summary": event["summary"],
        "content": event["content"],
        "tags": list(event.get("tags") or []),
        "source": event.get("source"),
        "generated_at": event["generated_at"],
        "supersedes": event.get("supersedes"),
        "contradicts": _normalize_event_links(event.get("contradicts")),
        "contradicted_by": _normalize_event_links(event.get("contradicted_by")),
    }


def _mark_contradiction(
    target: dict,
    *,
    contradicting_event_id: str,
    policy: str,
) -> None:
    contradicted_by = set(_normalize_event_links(target.get("contradicted_by")))
    contradicted_by.add(contradicting_event_id)
    target["contradicted_by"] = sorted(contradicted_by)
    if policy == "mark_stale" and target.get("status") == "active":
        target["status"] = "stale"
        target["stale_reason"] = "contradicted"


def _dedupe_observations(observations: list[dict]) -> tuple[list[dict], int]:
    deduped: dict[tuple[object, ...], dict] = {}
    duplicates_removed = 0

    for observation in observations:
        key = (
            observation.get("kind") or "",
            observation.get("status") or "",
            observation.get("verification_status") or "",
            _normalized_text(observation.get("summary")),
            _normalized_text(observation.get("content")),
            tuple(_normalize_event_links(observation.get("contradicts"))),
            tuple(_normalize_event_links(observation.get("contradicted_by"))),
        )
        if key in deduped:
            duplicates_removed += 1
            existing = deduped[key]
            duplicate_count = int(existing.get("duplicate_count", 1)) + int(
                observation.get("duplicate_count", 1)
            )
            merged_event_ids = set(existing.get("merged_event_ids") or [existing["event_id"]])
            merged_event_ids.update(
                observation.get("merged_event_ids") or [observation["event_id"]]
            )
            if observation.get("generated_at", "") >= existing.get("generated_at", ""):
                observation["duplicate_count"] = duplicate_count
                observation["merged_event_ids"] = sorted(merged_event_ids)
                deduped[key] = observation
            else:
                existing["duplicate_count"] = duplicate_count
                existing["merged_event_ids"] = sorted(merged_event_ids)
            continue

        observation["duplicate_count"] = int(observation.get("duplicate_count", 1))
        observation["merged_event_ids"] = sorted(
            set(observation.get("merged_event_ids") or [observation["event_id"]])
        )
        deduped[key] = observation

    return sorted(
        deduped.values(),
        key=lambda item: item.get("generated_at", ""),
        reverse=True,
    ), duplicates_removed


def _observation_rank(observation: dict) -> tuple[int, int, int, int, str]:
    return (
        1
        if observation.get("status") == "active"
        and observation.get("verification_status") == "verified"
        else 0,
        1 if observation.get("status") == "active" else 0,
        1 if observation.get("verification_status") == "verified" else 0,
        1 if not observation.get("contradicted_by") else 0,
        str(observation.get("generated_at") or ""),
    )


def _topic_summary(
    observations: list[dict], max_summary_chars: int
) -> tuple[str, str, str, str | None]:
    if not observations:
        return "", "unverified", "stale", None

    chosen = sorted(observations, key=_observation_rank, reverse=True)[0]
    summary = chosen.get("summary") or chosen.get("content") or ""
    return (
        _truncate(summary, max_summary_chars),
        str(chosen.get("verification_status") or "unverified"),
        str(chosen.get("status") or "active"),
        chosen.get("event_id"),
    )


def _topic_record_from_events(
    settings: dict, topic_id: str, events: list[dict]
) -> tuple[dict, int]:
    observations: list[dict] = []
    observations_by_id: dict[str, dict] = {}
    contradiction_pairs: set[tuple[str, str]] = set()
    unresolved_contradictions: set[str] = set()
    for event in sorted(events, key=lambda item: item.get("generated_at", "")):
        observation = _observation_payload(event)
        observations.append(observation)
        observations_by_id[observation["event_id"]] = observation

        target_ids = _normalize_event_links(observation.get("contradicts"))
        if isinstance(observation.get("supersedes"), str) and observation["supersedes"]:
            target_ids.append(observation["supersedes"])

        resolved_targets: list[str] = []
        for target_id in sorted(set(target_ids)):
            target = observations_by_id.get(target_id)
            if target is None:
                unresolved_contradictions.add(target_id)
                continue
            resolved_targets.append(target_id)
            contradiction_pairs.add((target_id, observation["event_id"]))
            _mark_contradiction(
                target,
                contradicting_event_id=observation["event_id"],
                policy=settings["contradiction_policy"],
            )

        observation["contradicts"] = resolved_targets

    observations, duplicates_removed = _dedupe_observations(observations)
    topic_name = str(events[-1].get("topic") or topic_id)
    summary, verification_status, topic_status, summary_event_id = _topic_summary(
        observations,
        settings["max_summary_chars"],
    )
    tags = sorted(
        {
            tag.strip()
            for observation in observations
            for tag in observation.get("tags") or []
            if isinstance(tag, str) and tag.strip()
        }
    )
    contradicted_event_ids = sorted(
        {
            event_id
            for observation in observations
            for event_id in _normalize_event_links(observation.get("contradicted_by"))
        }
    )
    active_observation_count = sum(
        1 for observation in observations if observation.get("status") == "active"
    )
    active_verified_observation_count = sum(
        1
        for observation in observations
        if observation.get("status") == "active"
        and observation.get("verification_status") == "verified"
    )
    topic_path = Path(settings["topics_dir"]) / f"{topic_id}.json"
    topic_record = {
        "schema_version": MEMORY_SCHEMA_VERSION,
        "topic_id": topic_id,
        "topic": topic_name,
        "summary": summary,
        "summary_event_id": summary_event_id,
        "status": topic_status,
        "verification_status": verification_status,
        "tags": tags,
        "last_updated": observations[0].get("generated_at")
        if observations
        else current_utc_timestamp(),
        "observation_count": len(observations),
        "active_observation_count": active_observation_count,
        "active_verified_observation_count": active_verified_observation_count,
        "has_contradictions": bool(contradiction_pairs or contradicted_event_ids),
        "contradiction_count": len(contradiction_pairs),
        "contradicted_event_ids": contradicted_event_ids,
        "unresolved_contradictions": sorted(unresolved_contradictions),
        "observations": observations,
        "path": str(topic_path.resolve()),
    }
    return topic_record, duplicates_removed


def _write_topic_record(settings: dict, topic_record: dict) -> None:
    topic_path = Path(settings["topics_dir"]) / f"{topic_record['topic_id']}.json"
    write_json_file(str(topic_path), topic_record)


def _load_index_payload(settings: dict) -> dict:
    _ensure_layout(settings)
    index_path = Path(settings["index_path"])
    if not index_path.exists():
        return _rebuild_memory_index(settings)

    payload = read_json_file(str(index_path))
    if not isinstance(payload, dict) or not isinstance(payload.get("topics"), list):
        return _rebuild_memory_index(settings)
    return payload


def _rebuild_memory_index(settings: dict) -> dict:
    _ensure_layout(settings)

    topics: list[dict] = []
    topics_dir = Path(settings["topics_dir"])
    for topic_path in sorted(topics_dir.glob("*.json")):
        topic_record = read_json_file(str(topic_path))
        topics.append(
            {
                "topic_id": topic_record.get("topic_id"),
                "topic": topic_record.get("topic"),
                "summary": _truncate(
                    str(topic_record.get("summary") or ""),
                    settings["max_summary_chars"],
                ),
                "summary_event_id": topic_record.get("summary_event_id"),
                "status": topic_record.get("status"),
                "verification_status": topic_record.get("verification_status"),
                "tags": list(topic_record.get("tags") or []),
                "last_updated": topic_record.get("last_updated"),
                "observation_count": topic_record.get("observation_count", 0),
                "active_verified_observation_count": topic_record.get(
                    "active_verified_observation_count", 0
                ),
                "has_contradictions": bool(topic_record.get("has_contradictions", False)),
                "contradiction_count": int(topic_record.get("contradiction_count", 0) or 0),
                "unresolved_contradictions": list(
                    topic_record.get("unresolved_contradictions") or []
                ),
                "path": str(topic_path.resolve()),
            }
        )

    topics.sort(key=lambda item: item.get("last_updated", ""), reverse=True)
    payload = {
        "schema_version": MEMORY_SCHEMA_VERSION,
        "generated_at": current_utc_timestamp(),
        "provider": settings["provider"],
        "topic_count": len(topics),
        "topics": topics[: settings["max_index_entries"]],
    }
    write_json_file(settings["index_path"], payload)
    return payload


def _consolidate_memory(settings: dict) -> dict:
    _ensure_layout(settings)
    events = _load_events(settings)

    events_by_topic: dict[str, list[dict]] = {}
    for event in events:
        topic_id = str(event.get("topic_id") or "")
        if topic_id:
            events_by_topic.setdefault(topic_id, []).append(event)

    topics_dir = Path(settings["topics_dir"])
    existing_paths = {path.name for path in topics_dir.glob("*.json")}
    retained_paths: set[str] = set()
    duplicates_removed = 0
    contradiction_count = 0

    for topic_id, topic_events in sorted(events_by_topic.items()):
        topic_record, topic_duplicates = _topic_record_from_events(settings, topic_id, topic_events)
        duplicates_removed += topic_duplicates
        contradiction_count += int(topic_record.get("contradiction_count", 0) or 0)
        _write_topic_record(settings, topic_record)
        retained_paths.add(f"{topic_id}.json")

    for filename in existing_paths - retained_paths:
        (topics_dir / filename).unlink(missing_ok=True)

    index_payload = _rebuild_memory_index(settings)
    return {
        "schema_version": MEMORY_SCHEMA_VERSION,
        "generated_at": current_utc_timestamp(),
        "provider": settings["provider"],
        "event_count": len(events),
        "topic_count": len(events_by_topic),
        "duplicates_removed": duplicates_removed,
        "contradiction_count": contradiction_count,
        "index_topic_count": index_payload["topic_count"],
    }


def _record_memory_entries(settings: dict, entries: list[dict]) -> list[dict]:
    events = [
        _build_memory_event(
            settings,
            topic=str(entry.get("topic") or ""),
            summary=str(entry.get("summary") or ""),
            content=str(entry.get("content") or ""),
            kind=str(entry.get("kind") or "operator_note"),
            status=str(entry.get("status") or "active"),
            verification_status=str(entry.get("verification_status") or "verified"),
            source=entry.get("source"),
            tags=entry.get("tags"),
            supersedes=entry.get("supersedes"),
            contradicts=entry.get("contradicts"),
            generated_at=entry.get("generated_at"),
        )
        for entry in entries
    ]
    _append_events(settings, events)
    _consolidate_memory(settings)
    return events


def record_memory_entry(
    cfg: dict,
    *,
    topic: str,
    summary: str,
    content: str,
    kind: str = "operator_note",
    status: str = "active",
    verification_status: str = "verified",
    source: str | None = "manual",
    tags: list[str] | None = None,
    supersedes: str | None = None,
    contradicts: list[str] | None = None,
) -> dict:
    return record_memory_entries(
        cfg,
        [
            {
                "topic": topic,
                "summary": summary,
                "content": content,
                "kind": kind,
                "status": status,
                "verification_status": verification_status,
                "source": source,
                "tags": tags or [],
                "supersedes": supersedes,
                "contradicts": contradicts or [],
            }
        ],
    )[0]


def _read_import_rows(source_path: str) -> list[dict]:
    path = Path(source_path)
    suffix = path.suffix.lower()

    if suffix == ".jsonl":
        rows: list[dict] = []
        with open(path, "r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                stripped = line.strip()
                if not stripped:
                    continue
                payload = json.loads(stripped)
                if not isinstance(payload, dict):
                    raise ValueError(
                        f"memory import row {line_number} in {source_path} must be an object"
                    )
                rows.append(payload)
        return rows

    with open(path, "r", encoding="utf-8") as handle:
        if suffix in {".yaml", ".yml"}:
            payload = yaml.safe_load(handle)
        else:
            payload = json.load(handle)

    if payload is None:
        return []
    if isinstance(payload, dict) and isinstance(payload.get("entries"), list):
        rows = payload["entries"]
    elif isinstance(payload, list):
        rows = payload
    elif isinstance(payload, dict):
        rows = [payload]
    else:
        raise ValueError(f"Unsupported memory import payload in {source_path}")

    normalized_rows: list[dict] = []
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise ValueError(f"memory import row {index} in {source_path} must be an object")
        normalized_rows.append(row)
    return normalized_rows


def _import_memory_entries(
    settings: dict,
    source_path: str,
    *,
    source_label: str | None = None,
) -> dict:
    rows = _read_import_rows(source_path)
    if len(rows) > settings["import_max_records"]:
        raise ValueError(
            f"memory import exceeds memory.import_max_records={settings['import_max_records']}"
        )

    path = Path(source_path)
    batch_source = (
        source_label.strip()
        if isinstance(source_label, str) and source_label.strip()
        else str(path.resolve())
    )
    batch_id = stable_identifier(
        "memory_import",
        batch_source,
        len(rows),
        current_utc_timestamp(),
    )
    entries: list[dict] = []
    topic_ids: set[str] = set()

    for index, row in enumerate(rows, start=1):
        if bool(row.get("derivable", False)):
            raise ValueError(
                f"memory import row {index} in {source_path} is marked derivable and cannot be persisted"
            )

        topic = str(row.get("topic") or "").strip()
        content = str(row.get("content") or row.get("body") or "").strip()
        summary = str(row.get("summary") or "").strip() or _truncate(
            content,
            settings["max_summary_chars"],
        )
        entry = {
            "topic": topic,
            "summary": summary,
            "content": content,
            "kind": str(row.get("kind") or "operator_note"),
            "status": str(row.get("status") or "active"),
            "verification_status": str(
                row.get("verification_status") or row.get("verification-status") or "verified"
            ),
            "source": str(row.get("source") or batch_source),
            "tags": row.get("tags") if row.get("tags") is not None else row.get("tag"),
            "supersedes": row.get("supersedes"),
            "contradicts": row.get("contradicts"),
            "generated_at": row.get("generated_at") or row.get("generated-at"),
        }
        topic_ids.add(_topic_id(topic))
        entries.append(entry)

    events = _record_memory_entries(settings, entries)
    return {
        "schema_version": MEMORY_SCHEMA_VERSION,
        "batch_id": batch_id,
        "generated_at": current_utc_timestamp(),
        "provider": settings["provider"],
        "source_path": str(path.resolve()),
        "source_label": batch_source,
        "imported_count": len(events),
        "topic_count": len(topic_ids),
        "event_ids": [event["event_id"] for event in events],
    }


def _score_index_entry(query: str, entry: dict) -> float:
    return score_document(
        query,
        {
            "source": entry.get("topic", ""),
            "section": " ".join(entry.get("tags") or []),
            "content": entry.get("summary", ""),
        },
    )


def _score_topic_record(query: str, topic_record: dict) -> float:
    content_parts = [str(topic_record.get("summary") or "")]
    for observation in topic_record.get("observations") or []:
        content_parts.append(str(observation.get("summary") or ""))
        content_parts.append(str(observation.get("content") or ""))

    return score_document(
        query,
        {
            "source": topic_record.get("topic", ""),
            "section": " ".join(topic_record.get("tags") or []),
            "content": "\n".join(part for part in content_parts if part),
        },
    )


def _query_memory(
    settings: dict,
    query: str,
    *,
    top_k: int | None = None,
    min_score: float | None = None,
    require_verification: bool | None = None,
    request_id: str | None = None,
    trace_result_limit: int | None = None,
    trace_excluded_limit: int | None = None,
    supporting_observation_limit: int | None = None,
) -> dict:
    _ensure_layout(settings)
    index_payload = _load_index_payload(settings)

    candidate_limit = settings["topic_candidate_limit"]
    selected_top_k = top_k if isinstance(top_k, int) and top_k > 0 else settings["default_top_k"]
    selected_min_score = float(min_score if min_score is not None else settings["min_score"])
    require_verified = (
        bool(require_verification)
        if require_verification is not None
        else bool(settings["require_verification"])
    )
    excluded_statuses = set(settings["exclude_statuses"])
    selected_request_id = (
        request_id.strip()
        if isinstance(request_id, str) and request_id.strip()
        else stable_identifier(
            "memory_query",
            query,
            selected_top_k,
            selected_min_score,
            require_verified,
        )
    )
    result_trace_limit = (
        trace_result_limit
        if isinstance(trace_result_limit, int) and trace_result_limit > 0
        else settings["max_trace_results"]
    )
    excluded_trace_limit = (
        trace_excluded_limit
        if isinstance(trace_excluded_limit, int) and trace_excluded_limit > 0
        else settings["max_trace_excluded"]
    )
    support_limit = (
        supporting_observation_limit
        if isinstance(supporting_observation_limit, int) and supporting_observation_limit > 0
        else settings["max_supporting_observations"]
    )

    ranked_index = []
    for entry in index_payload.get("topics") or []:
        score = _score_index_entry(query, entry)
        if score > 0:
            ranked_index.append({**entry, "index_score": round(score, 4)})

    ranked_index.sort(key=lambda item: (-item["index_score"], item.get("topic_id", "")))
    accepted: list[dict] = []
    excluded: list[dict] = []
    for entry in ranked_index[:candidate_limit]:
        topic_record = read_json_file(str(entry["path"]))
        score = round(_score_topic_record(query, topic_record), 4)
        supporting_observations = [
            {
                "event_id": observation.get("event_id"),
                "summary": observation.get("summary"),
                "status": observation.get("status"),
                "verification_status": observation.get("verification_status"),
                "generated_at": observation.get("generated_at"),
                "contradicted_by": observation.get("contradicted_by", []),
            }
            for observation in (topic_record.get("observations") or [])[:support_limit]
        ]
        lineage = {
            "request_id": selected_request_id,
            "topic_id": topic_record.get("topic_id"),
            "summary_event_id": topic_record.get("summary_event_id"),
            "supporting_event_ids": [
                observation.get("event_id") for observation in supporting_observations
            ],
        }
        reasons: list[str] = []

        if topic_record.get("status") in excluded_statuses:
            reasons.append(str(topic_record.get("status")))
        if require_verified and topic_record.get("verification_status") != "verified":
            reasons.append("unverified")
        if (
            settings["exclude_contradicted_topics"]
            and topic_record.get("has_contradictions")
            and int(topic_record.get("active_verified_observation_count", 0) or 0) < 1
        ):
            reasons.append("contradicted")
        if score < selected_min_score:
            reasons.append("below_threshold")

        result = {
            "topic_id": topic_record.get("topic_id"),
            "topic": topic_record.get("topic"),
            "summary": topic_record.get("summary"),
            "status": topic_record.get("status"),
            "verification_status": topic_record.get("verification_status"),
            "tags": list(topic_record.get("tags") or []),
            "last_updated": topic_record.get("last_updated"),
            "observation_count": topic_record.get("observation_count", 0),
            "active_verified_observation_count": topic_record.get(
                "active_verified_observation_count", 0
            ),
            "has_contradictions": bool(topic_record.get("has_contradictions", False)),
            "contradiction_count": int(topic_record.get("contradiction_count", 0) or 0),
            "score": score,
            "topic_path": topic_record.get("path"),
            "lineage": lineage,
            "supporting_observations": supporting_observations,
        }
        if reasons:
            result["exclusion_reasons"] = reasons
            excluded.append(result)
            continue

        accepted.append(result)

    accepted.sort(key=lambda item: (-item["score"], item.get("topic_id", "")))
    excluded.sort(key=lambda item: (-item["score"], item.get("topic_id", "")))
    results = accepted[:selected_top_k]
    return {
        "schema_version": MEMORY_SCHEMA_VERSION,
        "generated_at": current_utc_timestamp(),
        "provider": settings["provider"],
        "query": query,
        "request_id": selected_request_id,
        "used": bool(results),
        "result_count": len(results),
        "accepted_candidate_count": len(accepted),
        "excluded_candidate_count": len(excluded),
        "results": results,
        "trace_results": results[:result_trace_limit],
        "excluded": excluded[:excluded_trace_limit],
        "index_path": str(Path(settings["index_path"]).resolve()),
        "events_path": str(Path(settings["events_path"]).resolve()),
        "topic_count": index_payload.get("topic_count", 0),
        "top_k": selected_top_k,
        "min_score": selected_min_score,
        "require_verification": require_verified,
    }


class MemoryProvider(Protocol):
    def rebuild_index(self) -> dict: ...

    def consolidate(self) -> dict: ...

    def record_entries(self, entries: list[dict]) -> list[dict]: ...

    def import_entries(
        self,
        source_path: str,
        *,
        source_label: str | None = None,
    ) -> dict: ...

    def query(
        self,
        query: str,
        *,
        top_k: int | None = None,
        min_score: float | None = None,
        require_verification: bool | None = None,
        request_id: str | None = None,
        trace_result_limit: int | None = None,
        trace_excluded_limit: int | None = None,
        supporting_observation_limit: int | None = None,
    ) -> dict: ...


class FileMemoryProvider:
    def __init__(self, settings: dict) -> None:
        self.settings = settings

    def rebuild_index(self) -> dict:
        return _rebuild_memory_index(self.settings)

    def consolidate(self) -> dict:
        return _consolidate_memory(self.settings)

    def record_entries(self, entries: list[dict]) -> list[dict]:
        return _record_memory_entries(self.settings, entries)

    def import_entries(
        self,
        source_path: str,
        *,
        source_label: str | None = None,
    ) -> dict:
        return _import_memory_entries(
            self.settings,
            source_path,
            source_label=source_label,
        )

    def query(
        self,
        query: str,
        *,
        top_k: int | None = None,
        min_score: float | None = None,
        require_verification: bool | None = None,
        request_id: str | None = None,
        trace_result_limit: int | None = None,
        trace_excluded_limit: int | None = None,
        supporting_observation_limit: int | None = None,
    ) -> dict:
        return _query_memory(
            self.settings,
            query,
            top_k=top_k,
            min_score=min_score,
            require_verification=require_verification,
            request_id=request_id,
            trace_result_limit=trace_result_limit,
            trace_excluded_limit=trace_excluded_limit,
            supporting_observation_limit=supporting_observation_limit,
        )


MEMORY_PROVIDER_FACTORIES = {
    "file": FileMemoryProvider,
}


def _get_memory_provider(cfg: dict) -> MemoryProvider:
    settings = _memory_cfg(cfg)
    provider_name = settings["provider"]
    factory = MEMORY_PROVIDER_FACTORIES.get(provider_name)
    if factory is None:
        raise ValueError(f"Unsupported memory provider: {provider_name}")
    return factory(settings)


def rebuild_memory_index(cfg: dict) -> dict:
    return _get_memory_provider(cfg).rebuild_index()


def consolidate_memory(cfg: dict) -> dict:
    return _get_memory_provider(cfg).consolidate()


def record_memory_entries(cfg: dict, entries: list[dict]) -> list[dict]:
    return _get_memory_provider(cfg).record_entries(entries)


def import_memory_entries(
    cfg: dict,
    source_path: str,
    *,
    source_label: str | None = None,
) -> dict:
    return _get_memory_provider(cfg).import_entries(
        source_path,
        source_label=source_label,
    )


def query_memory(
    cfg: dict,
    query: str,
    *,
    top_k: int | None = None,
    min_score: float | None = None,
    require_verification: bool | None = None,
    request_id: str | None = None,
    trace_result_limit: int | None = None,
    trace_excluded_limit: int | None = None,
    supporting_observation_limit: int | None = None,
) -> dict:
    return _get_memory_provider(cfg).query(
        query,
        top_k=top_k,
        min_score=min_score,
        require_verification=require_verification,
        request_id=request_id,
        trace_result_limit=trace_result_limit,
        trace_excluded_limit=trace_excluded_limit,
        supporting_observation_limit=supporting_observation_limit,
    )


def append_dream_log_entry(
    cfg: dict,
    *,
    category: str,
    summary: str,
    details: str | None = None,
    source: str = "manual",
    session_id: str | None = None,
    request_id: str | None = None,
    metadata: dict | None = None,
    persist_memory: dict | None = None,
    generated_at: str | datetime | None = None,
) -> dict:
    settings = _dream_cfg(cfg)
    timestamp = _datetime_to_timestamp(_coerce_now(generated_at))
    cleaned_category = " ".join(category.split())
    if not cleaned_category:
        raise ValueError("Dream log category must be a non-empty string")

    cleaned_summary = " ".join(summary.split())
    cleaned_details = str(details or "").strip()
    if not cleaned_summary:
        cleaned_summary = _truncate(
            cleaned_details or cleaned_category, settings["brief_summary_chars"]
        )

    cleaned_source = " ".join(source.split()) or "manual"
    payload = {
        "schema_version": DREAM_SCHEMA_VERSION,
        "entry_id": stable_identifier(
            "dream_log",
            cleaned_category,
            cleaned_source,
            cleaned_summary,
            cleaned_details,
            session_id or "",
            request_id or "",
            timestamp,
        ),
        "generated_at": timestamp,
        "category": cleaned_category,
        "source": cleaned_source,
        "summary": _truncate(cleaned_summary, settings["brief_summary_chars"]),
        "details": cleaned_details,
        "session_id": session_id,
        "request_id": request_id,
    }
    if isinstance(metadata, dict) and metadata:
        payload["metadata"] = dict(metadata)
    if isinstance(persist_memory, dict) and persist_memory:
        payload["persist_memory"] = dict(persist_memory)

    _append_dream_log_row(settings, payload)
    return payload


def record_dream_session(
    cfg: dict,
    *,
    source: str,
    summary: str | None = None,
    details: str | None = None,
    metadata: dict | None = None,
    generated_at: str | datetime | None = None,
) -> dict:
    settings = _dream_cfg(cfg)
    state = _load_dream_state(settings)
    timestamp = _datetime_to_timestamp(_coerce_now(generated_at))
    next_session_count = int(state.get("session_count", 0) or 0) + 1
    cleaned_source = " ".join(source.split()) or "session"
    session_id = stable_identifier(
        "dream_session",
        cleaned_source,
        next_session_count,
        timestamp,
    )
    log_entry = append_dream_log_entry(
        cfg,
        category="session",
        summary=summary or f"{cleaned_source} session {next_session_count}",
        details=details,
        source=cleaned_source,
        session_id=session_id,
        metadata=metadata,
        generated_at=timestamp,
    )
    state["session_count"] = next_session_count
    state["last_session_at"] = timestamp
    state["last_session_id"] = session_id
    state = _write_dream_state(settings, state)
    return {
        "schema_version": DREAM_SCHEMA_VERSION,
        "enabled": settings["enabled"],
        "recorded": True,
        "session_id": session_id,
        "session_count": next_session_count,
        "state_path": str(Path(settings["state_path"]).resolve()),
        "log_entry": log_entry,
        "state": state,
    }


def assess_memory_dream(cfg: dict, *, now: str | datetime | None = None) -> dict:
    settings = _dream_cfg(cfg)
    state = _load_dream_state(settings)
    now_dt = _coerce_now(now)
    last_dream_dt = _coerce_datetime(state.get("last_dream_at"))
    lock_info = _load_dream_lock_info(settings, now_dt)
    pending_logs = _load_dream_log_entries(
        settings,
        since_generated_at=state.get("last_processed_log_at"),
        since_entry_id=state.get("last_processed_log_entry_id"),
    )
    recent_logs = pending_logs[-settings["max_recent_logs"] :]
    session_count = int(state.get("session_count", 0) or 0)
    sessions_since_last_dream = max(
        0,
        session_count - int(state.get("last_dream_session_count", 0) or 0),
    )
    hours_since_last_dream = None
    time_gate_passed = last_dream_dt is None
    if last_dream_dt is not None:
        hours_since_last_dream = max((now_dt - last_dream_dt).total_seconds() / 3600.0, 0.0)
        time_gate_passed = hours_since_last_dream >= float(settings["minimum_hours_between_runs"])

    session_gate_passed = sessions_since_last_dream >= int(
        settings["minimum_sessions_between_runs"]
    )
    lock_gate_passed = not bool(lock_info["active"])
    pending_persistable_count = sum(
        1 for entry in recent_logs if _normalize_persist_memory_entry(settings, entry) is not None
    )
    eligible = (
        bool(settings["enabled"]) and time_gate_passed and session_gate_passed and lock_gate_passed
    )
    status = "eligible" if eligible else "waiting"
    if not settings["enabled"]:
        status = "disabled"

    return {
        "schema_version": DREAM_SCHEMA_VERSION,
        "generated_at": _datetime_to_timestamp(now_dt),
        "enabled": settings["enabled"],
        "eligible": eligible,
        "status": status,
        "state_path": str(Path(settings["state_path"]).resolve()),
        "log_dir": str(Path(settings["log_dir"]).resolve()),
        "state": {
            "dream_count": int(state.get("dream_count", 0) or 0),
            "session_count": session_count,
            "last_session_at": state.get("last_session_at"),
            "last_session_id": state.get("last_session_id"),
            "last_dream_at": state.get("last_dream_at"),
            "last_dream_session_count": int(state.get("last_dream_session_count", 0) or 0),
            "last_processed_log_at": state.get("last_processed_log_at"),
            "last_processed_log_entry_id": state.get("last_processed_log_entry_id"),
        },
        "gates": {
            "time": {
                "passed": time_gate_passed,
                "minimum_hours_between_runs": int(settings["minimum_hours_between_runs"]),
                "hours_since_last_dream": round(hours_since_last_dream, 4)
                if hours_since_last_dream is not None
                else None,
            },
            "session": {
                "passed": session_gate_passed,
                "minimum_sessions_between_runs": int(settings["minimum_sessions_between_runs"]),
                "sessions_since_last_dream": sessions_since_last_dream,
            },
            "lock": {
                "passed": lock_gate_passed,
                **lock_info,
            },
        },
        "pending_log_count": len(pending_logs),
        "pending_persistable_log_count": pending_persistable_count,
        "recent_log_categories": sorted(
            {str(entry.get("category") or "") for entry in recent_logs if entry.get("category")}
        ),
    }


def run_memory_dream(
    cfg: dict,
    *,
    force: bool = False,
    now: str | datetime | None = None,
) -> dict:
    settings = _dream_cfg(cfg)
    assessment = assess_memory_dream(cfg, now=now)
    if not force and not assessment["eligible"]:
        return {
            "schema_version": DREAM_SCHEMA_VERSION,
            "generated_at": assessment["generated_at"],
            "enabled": settings["enabled"],
            "status": "skipped",
            "forced": force,
            "reason": "dream gates not satisfied",
            "assessment": assessment,
        }

    now_dt = _coerce_now(now)
    try:
        _acquire_dream_lock(settings, now_dt)
    except RuntimeError as exc:
        return {
            "schema_version": DREAM_SCHEMA_VERSION,
            "generated_at": _datetime_to_timestamp(now_dt),
            "enabled": settings["enabled"],
            "status": "locked",
            "forced": force,
            "reason": str(exc),
            "assessment": assess_memory_dream(cfg, now=now_dt),
        }

    try:
        state = _load_dream_state(settings)
        memory_settings = _memory_cfg(cfg)
        index_before = _load_index_payload(memory_settings)
        events_before = _load_events(memory_settings)
        pending_logs = _load_dream_log_entries(
            settings,
            since_generated_at=state.get("last_processed_log_at"),
            since_entry_id=state.get("last_processed_log_entry_id"),
        )
        logs_to_process = pending_logs[: settings["max_recent_logs"]]

        persistable_entries: list[dict] = []
        skipped_persistable_entry_ids: list[str] = []
        for log_entry in logs_to_process:
            normalized_entry = _normalize_persist_memory_entry(settings, log_entry)
            if normalized_entry is None:
                continue
            if len(persistable_entries) >= settings["max_persistable_entries_per_run"]:
                skipped_persistable_entry_ids.append(str(log_entry.get("entry_id") or ""))
                continue
            persistable_entries.append(normalized_entry)

        imported_events: list[dict] = []
        if persistable_entries:
            imported_events = record_memory_entries(cfg, persistable_entries)

        consolidation = consolidate_memory(cfg)
        index_after = _load_index_payload(memory_settings)
        events_after = _load_events(memory_settings)
        last_processed_log_at = state.get("last_processed_log_at")
        last_processed_log_entry_id = state.get("last_processed_log_entry_id")
        if logs_to_process:
            last_processed_log_at = logs_to_process[-1].get("generated_at")
            last_processed_log_entry_id = logs_to_process[-1].get("entry_id")

        updated_state = _write_dream_state(
            settings,
            {
                **state,
                "dream_count": int(state.get("dream_count", 0) or 0) + 1,
                "last_dream_at": _datetime_to_timestamp(now_dt),
                "last_dream_session_count": int(state.get("session_count", 0) or 0),
                "last_processed_log_at": last_processed_log_at,
                "last_processed_log_entry_id": last_processed_log_entry_id,
                "last_run": {
                    "generated_at": _datetime_to_timestamp(now_dt),
                    "forced": force,
                    "processed_log_count": len(logs_to_process),
                    "persisted_memory_count": len(imported_events),
                    "skipped_persistable_entry_count": len(skipped_persistable_entry_ids),
                },
            },
        )

        return {
            "schema_version": DREAM_SCHEMA_VERSION,
            "generated_at": _datetime_to_timestamp(now_dt),
            "enabled": settings["enabled"],
            "status": "succeeded",
            "forced": force,
            "assessment": assessment,
            "phases": {
                "orient": {
                    "memory_event_count": len(events_before),
                    "memory_topic_count": int(index_before.get("topic_count", 0) or 0),
                    "current_session_count": int(state.get("session_count", 0) or 0),
                    "memory_index_path": str(Path(memory_settings["index_path"]).resolve()),
                },
                "gather_recent_signal": {
                    "pending_log_count": len(pending_logs),
                    "processed_log_count": len(logs_to_process),
                    "persistable_log_count": len(persistable_entries),
                    "recent_categories": sorted(
                        {
                            str(log_entry.get("category") or "")
                            for log_entry in logs_to_process
                            if log_entry.get("category")
                        }
                    ),
                },
                "consolidate": {
                    "persisted_memory_count": len(imported_events),
                    "imported_event_ids": [event["event_id"] for event in imported_events],
                    "skipped_persistable_entry_ids": [
                        entry_id for entry_id in skipped_persistable_entry_ids if entry_id
                    ],
                },
                "prune_and_index": {
                    **consolidation,
                    "memory_event_count_after": len(events_after),
                    "memory_topic_count_after": int(index_after.get("topic_count", 0) or 0),
                },
            },
            "state": {
                "dream_count": int(updated_state.get("dream_count", 0) or 0),
                "last_dream_at": updated_state.get("last_dream_at"),
                "last_dream_session_count": int(
                    updated_state.get("last_dream_session_count", 0) or 0
                ),
                "last_processed_log_at": updated_state.get("last_processed_log_at"),
                "last_processed_log_entry_id": updated_state.get("last_processed_log_entry_id"),
            },
        }
    finally:
        _release_dream_lock(settings)


def format_memory_context(results: list[dict], max_context_chars: int) -> str:
    chunks: list[str] = []
    current_length = 0
    for index, item in enumerate(results, start=1):
        support_lines = [
            f"- {observation.get('summary')}"
            for observation in item.get("supporting_observations") or []
            if observation.get("summary")
        ]
        chunk = (
            f"[Memory {index}] Topic: {item.get('topic') or 'Unknown'}\n"
            f"Status: {item.get('status') or 'Unknown'}\n"
            f"Verification: {item.get('verification_status') or 'Unknown'}\n"
            f"Summary: {item.get('summary') or ''}"
        ).strip()
        if support_lines:
            chunk = f"{chunk}\nSupport:\n" + "\n".join(support_lines)

        proposed_length = current_length + len(chunk) + (2 if chunks else 0)
        if chunks and proposed_length > max_context_chars:
            break
        chunks.append(chunk)
        current_length = proposed_length

    return "\n\n".join(chunks)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manage the local indexed memory store.")
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Config file with memory settings",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser(
        "add", help="Append a memory event and rebuild the topic/index views"
    )
    add_parser.add_argument("--topic", required=True, help="Topic title for the memory entry")
    add_parser.add_argument(
        "--summary", required=True, help="Short summary stored in the topic/index views"
    )
    add_parser.add_argument(
        "--content", required=True, help="Full observation content stored in the topic record"
    )
    add_parser.add_argument("--kind", default="operator_note", help="Memory kind")
    add_parser.add_argument("--status", default="active", help="Memory status")
    add_parser.add_argument("--verification-status", default="verified", help="Verification state")
    add_parser.add_argument(
        "--source", default="manual", help="Operator or process that authored the note"
    )
    add_parser.add_argument(
        "--tag", action="append", default=[], help="Optional tag. Can be repeated."
    )
    add_parser.add_argument("--supersedes", help="Optional event_id that this note supersedes")
    add_parser.add_argument(
        "--contradicts",
        action="append",
        default=[],
        help="Optional event_id that this note contradicts. Can be repeated.",
    )

    query_parser = subparsers.add_parser("query", help="Query the memory index and topic records")
    query_parser.add_argument("--query", required=True, help="Query string")
    query_parser.add_argument("--top-k", type=int, help="Maximum accepted results")
    query_parser.add_argument("--min-score", type=float, help="Minimum score threshold")
    query_parser.add_argument(
        "--allow-unverified", action="store_true", help="Include unverified topics"
    )
    query_parser.add_argument("--request-id", help="Optional external request ID")

    import_parser = subparsers.add_parser(
        "import", help="Import curated memory rows from JSON, JSONL, or YAML"
    )
    import_parser.add_argument("--source-file", required=True, help="Path to the import file")
    import_parser.add_argument(
        "--source-label", help="Optional source label stored on imported rows"
    )

    dream_log_parser = subparsers.add_parser(
        "dream-log", help="Append an entry to the dream daily log"
    )
    dream_log_parser.add_argument("--category", required=True, help="Dream log category")
    dream_log_parser.add_argument("--summary", required=True, help="Brief dream log summary")
    dream_log_parser.add_argument("--details", help="Optional dream log details")
    dream_log_parser.add_argument("--source", default="manual", help="Log source label")
    dream_log_parser.add_argument("--session-id", help="Optional session identifier")
    dream_log_parser.add_argument("--request-id", help="Optional request identifier")
    dream_log_parser.add_argument("--persist-topic", help="Optional memory topic to persist")
    dream_log_parser.add_argument(
        "--persist-summary",
        help="Optional memory summary for a persistable dream log entry",
    )
    dream_log_parser.add_argument(
        "--persist-content",
        help="Optional memory content for a persistable dream log entry",
    )
    dream_log_parser.add_argument(
        "--persist-kind",
        default="operator_note",
        help="Optional memory kind for a persistable dream log entry",
    )
    dream_log_parser.add_argument(
        "--persist-status",
        default="active",
        help="Optional memory status for a persistable dream log entry",
    )
    dream_log_parser.add_argument(
        "--persist-verification-status",
        default="unverified",
        help="Optional memory verification state for a persistable dream log entry",
    )
    dream_log_parser.add_argument(
        "--persist-tag",
        action="append",
        default=[],
        help="Optional memory tag for a persistable dream log entry. Can be repeated.",
    )

    dream_session_parser = subparsers.add_parser(
        "dream-session", help="Record a session for dream gating"
    )
    dream_session_parser.add_argument(
        "--source",
        default="manual",
        help="Session source label",
    )
    dream_session_parser.add_argument("--summary", help="Optional brief session summary")
    dream_session_parser.add_argument("--details", help="Optional session details")

    dream_run_parser = subparsers.add_parser(
        "dream-run", help="Run a dream consolidation pass when gates allow it"
    )
    dream_run_parser.add_argument(
        "--force",
        action="store_true",
        help="Bypass dream eligibility gates for the current run",
    )

    subparsers.add_parser("dream-status", help="Inspect current dream eligibility and state")

    subparsers.add_parser(
        "consolidate", help="Rebuild topic files from the append-only memory event log"
    )
    subparsers.add_parser(
        "rebuild-index", help="Rebuild the pointer-only memory index from topic records"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = load_config(args.config)
    validate_memory_config(cfg)
    validate_dream_config(cfg)

    if args.command == "add":
        payload = record_memory_entry(
            cfg,
            topic=args.topic,
            summary=args.summary,
            content=args.content,
            kind=args.kind,
            status=args.status,
            verification_status=args.verification_status,
            source=args.source,
            tags=args.tag,
            supersedes=args.supersedes,
            contradicts=args.contradicts,
        )
    elif args.command == "query":
        payload = query_memory(
            cfg,
            args.query,
            top_k=args.top_k,
            min_score=args.min_score,
            require_verification=not args.allow_unverified,
            request_id=args.request_id,
        )
    elif args.command == "import":
        payload = import_memory_entries(
            cfg,
            args.source_file,
            source_label=args.source_label,
        )
    elif args.command == "dream-log":
        persist_memory = None
        if args.persist_topic or args.persist_summary or args.persist_content or args.persist_tag:
            persist_memory = {
                "topic": args.persist_topic,
                "summary": args.persist_summary,
                "content": args.persist_content,
                "kind": args.persist_kind,
                "status": args.persist_status,
                "verification_status": args.persist_verification_status,
                "tags": args.persist_tag,
            }
        payload = append_dream_log_entry(
            cfg,
            category=args.category,
            summary=args.summary,
            details=args.details,
            source=args.source,
            session_id=args.session_id,
            request_id=args.request_id,
            persist_memory=persist_memory,
        )
    elif args.command == "dream-session":
        payload = record_dream_session(
            cfg,
            source=args.source,
            summary=args.summary,
            details=args.details,
        )
    elif args.command == "dream-run":
        payload = run_memory_dream(cfg, force=args.force)
    elif args.command == "dream-status":
        payload = assess_memory_dream(cfg)
    elif args.command == "consolidate":
        payload = consolidate_memory(cfg)
    else:
        payload = rebuild_memory_index(cfg)

    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
