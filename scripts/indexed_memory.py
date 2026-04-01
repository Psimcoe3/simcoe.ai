"""
File-backed indexed memory with a pointer-only index, on-demand topic files,
and an append-only event log.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from config_validation import load_config, validate_memory_config
from data_contracts import stable_identifier
from manifest_utils import current_utc_timestamp, read_json_file, write_json_file
from retrieval_utils import score_document


MEMORY_SCHEMA_VERSION = 1
MEMORY_KINDS = {"operator_note", "verified_fact", "decision", "exception"}
MEMORY_STATUSES = {"active", "stale", "retracted"}
MEMORY_VERIFICATION_STATUSES = {"verified", "unverified", "disputed"}
MEMORY_CONTRADICTION_POLICIES = {"mark_stale", "track_only"}


def _memory_cfg(cfg: dict) -> dict:
    section = cfg.get("memory") if isinstance(cfg.get("memory"), dict) else {}
    return {
        "enabled": bool(section.get("enabled", False)),
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


def rebuild_memory_index(cfg: dict) -> dict:
    settings = _memory_cfg(cfg)
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
        "topic_count": len(topics),
        "topics": topics[: settings["max_index_entries"]],
    }
    write_json_file(settings["index_path"], payload)
    return payload


def consolidate_memory(cfg: dict) -> dict:
    settings = _memory_cfg(cfg)
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

    index_payload = rebuild_memory_index(cfg)
    return {
        "schema_version": MEMORY_SCHEMA_VERSION,
        "generated_at": current_utc_timestamp(),
        "event_count": len(events),
        "topic_count": len(events_by_topic),
        "duplicates_removed": duplicates_removed,
        "contradiction_count": contradiction_count,
        "index_topic_count": index_payload["topic_count"],
    }


def record_memory_entries(cfg: dict, entries: list[dict]) -> list[dict]:
    settings = _memory_cfg(cfg)
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
    consolidate_memory(cfg)
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


def import_memory_entries(
    cfg: dict,
    source_path: str,
    *,
    source_label: str | None = None,
) -> dict:
    settings = _memory_cfg(cfg)
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

    events = record_memory_entries(cfg, entries)
    return {
        "schema_version": MEMORY_SCHEMA_VERSION,
        "batch_id": batch_id,
        "generated_at": current_utc_timestamp(),
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
    settings = _memory_cfg(cfg)
    _ensure_layout(settings)
    index_payload = rebuild_memory_index(cfg)

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
    elif args.command == "consolidate":
        payload = consolidate_memory(cfg)
    else:
        payload = rebuild_memory_index(cfg)

    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
