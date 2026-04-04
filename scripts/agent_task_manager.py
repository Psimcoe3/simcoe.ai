"""
Managed background task runner for workflow, dream, and subagent jobs.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import uuid

from agent_registry import resolve_agent_definition_task_defaults
from agent_skill_registry import normalize_agent_skill_names
from config_validation import (
    load_config,
    validate_agent_task_manager_config,
    validate_dream_config,
    validate_workflow_registry_config,
)
from indexed_memory import run_memory_dream
from manifest_utils import current_utc_timestamp, read_json_file, write_json_file
from runtime_contracts import (
    TASK_KIND_DREAM,
    TASK_KIND_SUBAGENT,
    TASK_KIND_WORKFLOW,
    TASK_STATUS_CANCELLED,
    TASK_STATUS_COMPLETED,
    TASK_STATUS_FAILED,
    TASK_STATUS_PENDING,
    TASK_STATUS_RUNNING,
    ROUTE_DETERMINISTIC_TOOL,
    ROUTE_RETRIEVAL,
    ROUTE_TEXT,
    normalize_task_kind,
    normalize_task_status,
    normalize_route,
    summarize_execution_envelopes,
)
from request_router import route_request
from workflow_registry import WorkflowRegistryError, render_workflow_steps, run_workflow


REPO_ROOT = Path(__file__).resolve().parents[1]
TASK_MANAGER_SCHEMA_VERSION = 1
ACTIVE_TASK_STATUSES = frozenset({TASK_STATUS_PENDING, TASK_STATUS_RUNNING})
RESUMABLE_TASK_STATUSES = frozenset(
    {TASK_STATUS_PENDING, TASK_STATUS_FAILED, TASK_STATUS_CANCELLED}
)
DEFAULT_TASK_RECENT_LIMIT = 5
DEFAULT_ATTACH_LINE_LIMIT = 20
DEFAULT_SUBAGENT_ALLOWED_ROUTES = (ROUTE_TEXT, ROUTE_RETRIEVAL)
MAX_SUBAGENT_DELEGATION_BRIEFING_CHARS = 4000
SUBAGENT_TASK_ALLOWED_ROUTES = {
    ROUTE_TEXT,
    ROUTE_RETRIEVAL,
    ROUTE_DETERMINISTIC_TOOL,
}
TASK_TRANSCRIPT_RECORD_SUBAGENT_TURN = "subagent_turn"
TASK_TRANSCRIPT_RECORD_TASK_EVENT = "task_event"
TASK_TRANSCRIPT_EVENT_STARTED = "task_started"
TASK_TRANSCRIPT_EVENT_COMPLETED = "task_completed"
TASK_TRANSCRIPT_EVENT_FAILED = "task_failed"
TASK_TRANSCRIPT_EVENT_CANCELLED = "task_cancelled"


class TaskManagerError(ValueError):
    pass


class TaskCancelledError(RuntimeError):
    pass


def resolve_agent_task_manager_settings(cfg: dict) -> dict:
    agent_task_manager = (
        cfg.get("agent_task_manager") if isinstance(cfg.get("agent_task_manager"), dict) else {}
    )
    root_dir = str(agent_task_manager.get("root_dir") or "data/agent_tasks")
    return {
        "enabled": bool(agent_task_manager.get("enabled", True)),
        "root_dir": _resolve_repo_path(root_dir),
        "tasks_dir": _resolve_repo_path(
            str(agent_task_manager.get("tasks_dir") or f"{root_dir}/tasks")
        ),
        "logs_dir": _resolve_repo_path(
            str(agent_task_manager.get("logs_dir") or f"{root_dir}/logs")
        ),
        "transcripts_dir": _resolve_repo_path(
            str(agent_task_manager.get("transcripts_dir") or f"{root_dir}/transcripts")
        ),
    }


def _resolve_repo_path(path: str) -> str:
    candidate = Path(path).expanduser()
    if candidate.is_absolute():
        return str(candidate.resolve())
    return str((REPO_ROOT / candidate).resolve())


def ensure_agent_task_manager_layout(settings: dict) -> None:
    Path(settings["root_dir"]).mkdir(parents=True, exist_ok=True)
    Path(settings["tasks_dir"]).mkdir(parents=True, exist_ok=True)
    Path(settings["logs_dir"]).mkdir(parents=True, exist_ok=True)
    Path(settings["transcripts_dir"]).mkdir(parents=True, exist_ok=True)


def _task_summary_path(settings: dict, task_id: str) -> Path:
    return Path(settings["tasks_dir"]) / f"{task_id}.json"


def _task_log_path(settings: dict, task_id: str) -> Path:
    return Path(settings["logs_dir"]) / f"{task_id}.log"


def _task_transcript_path(settings: dict, task_id: str) -> Path:
    return Path(settings["transcripts_dir"]) / f"{task_id}.jsonl"


def _task_list_payload(summary: dict) -> dict:
    metadata = _task_metadata(summary)
    child_task_ids = _task_child_task_ids(summary)
    return {
        "task_id": summary["task_id"],
        "kind": summary["kind"],
        "name": summary["name"],
        "status": summary["status"],
        "active": _task_is_active(summary),
        "restartable": _task_is_resumable(summary),
        "created_at": summary.get("created_at"),
        "updated_at": summary.get("updated_at"),
        "started_at": summary.get("started_at"),
        "completed_at": summary.get("completed_at"),
        "exit_code": summary.get("exit_code"),
        "pid": summary.get("pid"),
        "source": summary.get("source"),
        "parent_task_id": _task_parent_task_id(summary),
        "child_task_count": len(child_task_ids),
        "last_child_task_id": _task_last_child_task_id(summary),
        "agent_definition_name": metadata.get("agent_definition_name"),
        "cancel_requested_at": summary.get("cancel_requested_at"),
        "resumed_by_task_id": summary.get("resumed_by_task_id"),
        "resumed_from_task_id": metadata.get("resumed_from_task_id"),
    }


def _read_task_summary(settings: dict, task_id: str) -> dict:
    summary_path = _task_summary_path(settings, task_id)
    if not summary_path.is_file():
        raise TaskManagerError(f"task not found: {task_id}")

    payload = read_json_file(str(summary_path))
    if not isinstance(payload, dict):
        raise TaskManagerError(f"task summary must contain a top-level object: {summary_path}")
    return payload


def _write_task_summary(settings: dict, summary: dict) -> dict:
    updated_summary = copy.deepcopy(summary)
    updated_summary["updated_at"] = current_utc_timestamp()
    write_json_file(str(_task_summary_path(settings, updated_summary["task_id"])), updated_summary)
    return updated_summary


def _task_summary(
    settings: dict,
    *,
    task_id: str,
    kind: str,
    name: str,
    config_path: str,
    source: str,
    metadata: dict | None = None,
) -> dict:
    created_at = current_utc_timestamp()
    summary_path = _task_summary_path(settings, task_id)
    log_path = _task_log_path(settings, task_id)
    transcript_path = _task_transcript_path(settings, task_id)
    return {
        "schema_version": TASK_MANAGER_SCHEMA_VERSION,
        "task_id": task_id,
        "kind": normalize_task_kind(kind),
        "name": name,
        "status": TASK_STATUS_PENDING,
        "created_at": created_at,
        "updated_at": created_at,
        "config_path": os.path.abspath(config_path),
        "summary_path": str(summary_path.resolve()),
        "log_path": str(log_path.resolve()),
        "transcript_path": str(transcript_path.resolve()),
        "pid": None,
        "source": source,
        "metadata": copy.deepcopy(metadata or {}),
        "result": None,
        "error": None,
        "exit_code": None,
        "started_at": None,
        "completed_at": None,
        "cancel_requested_at": None,
    }


def _task_metadata(summary: dict) -> dict:
    metadata = summary.get("metadata")
    return copy.deepcopy(metadata) if isinstance(metadata, dict) else {}


def _task_parent_task_id(summary: dict) -> str | None:
    parent_task_id = _task_metadata(summary).get("parent_task_id")
    if not isinstance(parent_task_id, str) or not parent_task_id.strip():
        return None
    return parent_task_id.strip()


def _task_child_task_ids(summary: dict) -> list[str]:
    child_task_ids = _task_metadata(summary).get("child_task_ids")
    if not isinstance(child_task_ids, list):
        return []

    cleaned: list[str] = []
    seen: set[str] = set()
    for item in child_task_ids:
        if not isinstance(item, str) or not item.strip():
            continue
        candidate = item.strip()
        if candidate in seen:
            continue
        cleaned.append(candidate)
        seen.add(candidate)
    return cleaned


def _task_last_child_task_id(summary: dict) -> str | None:
    last_child_task_id = summary.get("last_child_task_id")
    if isinstance(last_child_task_id, str) and last_child_task_id.strip():
        return last_child_task_id.strip()

    child_task_ids = _task_child_task_ids(summary)
    return child_task_ids[-1] if child_task_ids else None


def _task_detail_payload(summary: dict, *, process_running: bool | None = None) -> dict:
    child_task_ids = _task_child_task_ids(summary)
    payload = copy.deepcopy(summary)
    payload["active"] = _task_is_active(summary)
    payload["restartable"] = _task_is_resumable(summary)
    payload["process_running"] = (
        _task_process_running(summary) if process_running is None else process_running
    )
    payload["parent_task_id"] = _task_parent_task_id(summary)
    payload["child_task_count"] = len(child_task_ids)
    payload["child_task_ids"] = child_task_ids
    payload["last_child_task_id"] = _task_last_child_task_id(summary)
    subagent_context = _subagent_task_context(summary)
    if subagent_context is not None:
        payload["subagent_context"] = subagent_context
    return payload


def _resolved_task_transcript_path(settings: dict, summary: dict) -> Path:
    transcript_path = summary.get("transcript_path")
    if isinstance(transcript_path, str) and transcript_path.strip():
        resolved_path = Path(transcript_path).expanduser()
        if not resolved_path.is_absolute():
            resolved_path = Path(os.path.abspath(str(resolved_path)))
        return resolved_path
    return _task_transcript_path(settings, str(summary.get("task_id") or ""))


def _read_task_jsonl_records(path: Path) -> list[dict]:
    if not path.is_file():
        return []

    records: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            records.append(json.loads(stripped))
    return records


def _task_transcript_record_type(record: dict) -> str:
    record_type = record.get("record_type")
    if isinstance(record_type, str) and record_type.strip():
        return record_type.strip()
    if isinstance(record.get("turn_id"), str) and record.get("turn_id").strip():
        return TASK_TRANSCRIPT_RECORD_SUBAGENT_TURN
    return TASK_TRANSCRIPT_RECORD_TASK_EVENT


def _task_transcript_base_event(summary: dict, *, event_type: str) -> dict:
    return {
        "record_type": TASK_TRANSCRIPT_RECORD_TASK_EVENT,
        "event_type": event_type,
        "recorded_at": current_utc_timestamp(),
        "task_id": summary.get("task_id"),
        "task_kind": summary.get("kind"),
        "task_name": summary.get("name"),
        "task_status": summary.get("status"),
        "source": summary.get("source"),
    }


def _workflow_task_transcript_event(summary: dict, *, event_type: str) -> dict:
    metadata = _task_metadata(summary)
    result = summary.get("result") if isinstance(summary.get("result"), dict) else None
    workflow_name = (
        str(metadata.get("workflow")).strip()
        if isinstance(metadata.get("workflow"), str) and str(metadata.get("workflow")).strip()
        else str(summary.get("name") or "workflow")
    )
    record = _task_transcript_base_event(summary, event_type=event_type)
    record.update(
        {
            "workflow": workflow_name,
            "description": (
                result.get("description")
                if isinstance(result, dict) and isinstance(result.get("description"), str)
                else metadata.get("description")
            ),
            "step_count": (
                int(result.get("step_count", 0) or 0)
                if isinstance(result, dict)
                else int(metadata.get("step_count", 0) or 0)
            ),
            "tags": (
                copy.deepcopy(result.get("tags", []))
                if isinstance(result, dict)
                else copy.deepcopy(metadata.get("tags", []))
            ),
            "variables": (
                copy.deepcopy(result.get("variables", {}))
                if isinstance(result, dict)
                else copy.deepcopy(metadata.get("variables", {}))
            ),
        }
    )
    if isinstance(result, dict):
        record["executed_steps"] = int(result.get("executed_steps", 0) or 0)
        record["dream"] = copy.deepcopy(result.get("dream", {}))
        record["result"] = _workflow_result_summary(result)
    if isinstance(summary.get("error"), str) and str(summary.get("error")).strip():
        record["error"] = str(summary.get("error")).strip()
    exit_code = summary.get("exit_code")
    if isinstance(exit_code, int) and not isinstance(exit_code, bool):
        record["exit_code"] = exit_code
    return record


def _dream_task_transcript_event(summary: dict, *, event_type: str) -> dict:
    metadata = _task_metadata(summary)
    result = summary.get("result") if isinstance(summary.get("result"), dict) else None
    record = _task_transcript_base_event(summary, event_type=event_type)
    record["dream_enabled"] = bool(metadata.get("dream_enabled", False))
    if isinstance(result, dict):
        record["dream_status"] = result.get("status")
        record["result"] = copy.deepcopy(result)
    if isinstance(summary.get("error"), str) and str(summary.get("error")).strip():
        record["error"] = str(summary.get("error")).strip()
    exit_code = summary.get("exit_code")
    if isinstance(exit_code, int) and not isinstance(exit_code, bool):
        record["exit_code"] = exit_code
    return record


def _task_transcript_event(summary: dict, *, event_type: str) -> dict | None:
    try:
        task_kind = normalize_task_kind(summary.get("kind"), "task kind")
    except ValueError:
        return None

    if task_kind == TASK_KIND_WORKFLOW:
        return _workflow_task_transcript_event(summary, event_type=event_type)
    if task_kind == TASK_KIND_DREAM:
        return _dream_task_transcript_event(summary, event_type=event_type)
    return None


def _task_transcript_event_type(task_status: object) -> str:
    normalized_status = normalize_task_status(task_status, "task status")
    if normalized_status == TASK_STATUS_COMPLETED:
        return TASK_TRANSCRIPT_EVENT_COMPLETED
    if normalized_status == TASK_STATUS_FAILED:
        return TASK_TRANSCRIPT_EVENT_FAILED
    if normalized_status == TASK_STATUS_CANCELLED:
        return TASK_TRANSCRIPT_EVENT_CANCELLED
    return TASK_TRANSCRIPT_EVENT_STARTED


def _summarize_task_transcript_turn(turn: dict) -> dict:
    return {
        "turn_id": turn.get("turn_id"),
        "turn_index": turn.get("turn_index"),
        "route": turn.get("route"),
        "runtime_owner": turn.get("runtime_owner"),
        "user_prompt": turn.get("user", {}).get("prompt"),
        "assistant_response": turn.get("assistant", {}).get("response"),
        "skill_names": [
            skill.get("name")
            for skill in turn.get("skills", [])
            if isinstance(skill, dict) and isinstance(skill.get("name"), str)
        ],
        "tool_name": (
            turn.get("tool", {}).get("name") if isinstance(turn.get("tool"), dict) else None
        ),
        "error": turn.get("error"),
    }


def _summarize_task_transcript_event(record: dict) -> dict:
    result = record.get("result") if isinstance(record.get("result"), dict) else {}
    dream = record.get("dream") if isinstance(record.get("dream"), dict) else {}
    result_dream = result.get("dream") if isinstance(result.get("dream"), dict) else {}
    return {
        "event_type": record.get("event_type"),
        "recorded_at": record.get("recorded_at"),
        "task_kind": record.get("task_kind"),
        "task_status": record.get("task_status"),
        "workflow": record.get("workflow") or result.get("workflow"),
        "executed_steps": record.get("executed_steps") or result.get("executed_steps"),
        "step_count": record.get("step_count") or result.get("step_count"),
        "dream_status": (
            record.get("dream_status")
            or dream.get("status")
            or result.get("status")
            or result_dream.get("status")
        ),
        "error": record.get("error"),
        "exit_code": record.get("exit_code"),
    }


def _append_task_execution_envelopes_from_turn(turn: dict, envelopes: list[dict]) -> int | None:
    execution = turn.get("execution") if isinstance(turn.get("execution"), dict) else None
    if execution is None:
        return None

    schema_version = (
        execution.get("schema_version")
        if isinstance(execution.get("schema_version"), int)
        else None
    )
    route = execution.get("route")
    if isinstance(route, dict):
        envelopes.append(copy.deepcopy(route))

    context_providers = execution.get("context_providers")
    if isinstance(context_providers, list):
        for provider in context_providers:
            if isinstance(provider, dict):
                envelopes.append(copy.deepcopy(provider))

    deterministic_tool = execution.get("deterministic_tool")
    if isinstance(deterministic_tool, dict):
        envelopes.append(copy.deepcopy(deterministic_tool))
    return schema_version


def _append_task_transcript_record(settings: dict, summary: dict, record: dict) -> None:
    transcript_path = _resolved_task_transcript_path(settings, summary)
    transcript_path.parent.mkdir(parents=True, exist_ok=True)
    with transcript_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(copy.deepcopy(record), sort_keys=True) + "\n")


def _task_transcript_payload(settings: dict, summary: dict, *, tail: int) -> dict | None:
    try:
        task_kind = normalize_task_kind(summary.get("kind"), "task kind")
    except ValueError:
        task_kind = None

    transcript_path = _resolved_task_transcript_path(settings, summary)
    if not transcript_path.is_file():
        return None

    records = _read_task_jsonl_records(transcript_path)
    if not records:
        return None

    if task_kind == TASK_KIND_SUBAGENT:
        turns = [
            record
            for record in records
            if _task_transcript_record_type(record) == TASK_TRANSCRIPT_RECORD_SUBAGENT_TURN
        ]
        recent_turns = [_summarize_task_transcript_turn(turn) for turn in turns[-max(0, tail) :]]
        envelopes: list[dict] = []
        schema_version = None
        for turn in turns:
            turn_schema_version = _append_task_execution_envelopes_from_turn(turn, envelopes)
            if schema_version is None and turn_schema_version is not None:
                schema_version = turn_schema_version

        return {
            "transcript_path": str(transcript_path.resolve()),
            "record_count": len(records),
            "turn_count": len(turns),
            "recent_turns": recent_turns,
            "last_turn": copy.deepcopy(turns[-1]) if turns else None,
            "execution": {
                "source": "reconstructed_from_task_transcript",
                "schema_version": schema_version,
                "summary": summarize_execution_envelopes(envelopes),
            },
        }

    events = [
        record
        for record in records
        if _task_transcript_record_type(record) == TASK_TRANSCRIPT_RECORD_TASK_EVENT
    ]
    if not events:
        return None

    return {
        "transcript_path": str(transcript_path.resolve()),
        "record_count": len(records),
        "event_count": len(events),
        "recent_events": [
            _summarize_task_transcript_event(record) for record in events[-max(0, tail) :]
        ],
        "last_event": copy.deepcopy(events[-1]) if events else None,
    }


def _write_task_transcript_turn(settings: dict, summary: dict, turn_payload: dict) -> None:
    record = copy.deepcopy(turn_payload)
    record.setdefault("record_type", TASK_TRANSCRIPT_RECORD_SUBAGENT_TURN)
    _append_task_transcript_record(settings, summary, record)


def _task_is_active(summary: dict) -> bool:
    try:
        return normalize_task_status(summary.get("status")) in ACTIVE_TASK_STATUSES
    except ValueError:
        return False


def _task_is_resumable(summary: dict) -> bool:
    try:
        return normalize_task_status(summary.get("status")) in RESUMABLE_TASK_STATUSES
    except ValueError:
        return False


def _task_resume_depth(summary: dict) -> int:
    value = _task_metadata(summary).get("resume_depth")
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        return 0
    return value


def _task_variables(summary: dict) -> dict[str, str]:
    variables = _task_metadata(summary).get("variables")
    if not isinstance(variables, dict):
        return {}

    normalized: dict[str, str] = {}
    for key, value in variables.items():
        if not isinstance(key, str) or not key.strip() or value is None:
            continue
        normalized[key.strip()] = str(value)
    return normalized


def _task_log_lines(log_path: Path) -> list[str]:
    if not log_path.is_file():
        return []
    return log_path.read_text(encoding="utf-8").splitlines()


def _task_process_running(summary: dict) -> bool:
    pid = summary.get("pid")
    if isinstance(pid, bool) or not isinstance(pid, int) or pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _normalized_subagent_attachments(value: object) -> list[str]:
    if not isinstance(value, list):
        return []

    attachments: list[str] = []
    seen: set[str] = set()
    for item in value:
        if not isinstance(item, str) or not item.strip():
            continue
        candidate = item.strip()
        if candidate in seen:
            continue
        attachments.append(candidate)
        seen.add(candidate)
    return attachments


def _normalize_subagent_allowed_routes(
    allowed_routes: list[str] | tuple[str, ...] | None,
    *,
    explicit_tool_name: str | None,
) -> list[str]:
    raw_routes = list(allowed_routes) if allowed_routes is not None else []
    if not raw_routes:
        raw_routes = (
            [ROUTE_DETERMINISTIC_TOOL]
            if explicit_tool_name
            else list(DEFAULT_SUBAGENT_ALLOWED_ROUTES)
        )

    normalized: list[str] = []
    seen: set[str] = set()
    for route_name in raw_routes:
        normalized_route = normalize_route(route_name, "subagent allowed route")
        if normalized_route not in SUBAGENT_TASK_ALLOWED_ROUTES:
            choices = ", ".join(sorted(SUBAGENT_TASK_ALLOWED_ROUTES))
            raise TaskManagerError(f"subagent allowed routes must be limited to: {choices}")
        if normalized_route == ROUTE_DETERMINISTIC_TOOL and not explicit_tool_name:
            raise TaskManagerError(
                "subagent deterministic_tool route requires an explicit tool name"
            )
        if normalized_route in seen:
            continue
        normalized.append(normalized_route)
        seen.add(normalized_route)
    return normalized


def _normalize_subagent_prompt(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise TaskManagerError("subagent prompt must be a non-empty string")
    return value.strip()


def _normalize_subagent_instructions(value: object) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise TaskManagerError("subagent instructions must be a string when present")
    cleaned = value.strip()
    return cleaned or None


def _normalize_subagent_delegation_briefing(value: object) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise TaskManagerError("subagent delegation briefing must be a string when present")
    cleaned = value.strip()
    if not cleaned:
        return None
    if len(cleaned) <= MAX_SUBAGENT_DELEGATION_BRIEFING_CHARS:
        return cleaned

    truncated = cleaned[:MAX_SUBAGENT_DELEGATION_BRIEFING_CHARS].rstrip()
    return f"{truncated}\n\n[delegation briefing truncated]"


def _compose_subagent_execution_prompt(
    prompt: str,
    *,
    agent_instructions: str | None,
    delegation_briefing: str | None,
) -> str:
    sections: list[str] = []
    if agent_instructions:
        sections.append(f"### Agent Instructions:\n{agent_instructions}")
    if delegation_briefing:
        sections.append(f"### Delegation Briefing:\n{delegation_briefing}")
    if not sections:
        return prompt
    sections.append(f"### Assigned Task:\n{prompt}")
    return "\n\n".join(sections)


def _build_subagent_delegation_briefing(summary: dict) -> str | None:
    metadata = _task_metadata(summary)
    sections: list[str] = []
    overview: list[str] = []

    task_id = summary.get("task_id")
    if isinstance(task_id, str) and task_id.strip():
        overview.append(f"Parent task id: {task_id.strip()}")

    parent_worker = metadata.get("agent_name") or summary.get("name")
    if isinstance(parent_worker, str) and parent_worker.strip():
        overview.append(f"Parent worker: {parent_worker.strip()}")

    parent_agent_definition = metadata.get("agent_definition_name")
    if isinstance(parent_agent_definition, str) and parent_agent_definition.strip():
        overview.append(f"Parent agent definition: {parent_agent_definition.strip()}")

    request_source = metadata.get("request_source") or summary.get("source")
    if isinstance(request_source, str) and request_source.strip():
        overview.append(f"Parent request source: {request_source.strip()}")

    section = metadata.get("section")
    if isinstance(section, str) and section.strip():
        overview.append(f"Parent section: {section.strip()}")

    attachments = _normalized_subagent_attachments(metadata.get("attachments"))
    if attachments:
        overview.append(f"Parent attachments: {', '.join(attachments)}")

    if overview:
        sections.append("\n".join(overview))

    inherited_briefing = _normalize_subagent_delegation_briefing(
        metadata.get("delegation_briefing")
    )
    if inherited_briefing:
        sections.append(f"Inherited delegation context:\n{inherited_briefing}")

    parent_prompt = metadata.get("prompt")
    if isinstance(parent_prompt, str) and parent_prompt.strip():
        sections.append(f"Parent assigned task:\n{parent_prompt.strip()}")

    if not sections:
        return None
    return _normalize_subagent_delegation_briefing("\n\n".join(sections))


def _subagent_task_metadata(
    cfg: dict,
    *,
    prompt: str,
    task_source: str,
    request_source: str | None,
    section: str | None,
    attachments: list[str] | None,
    explicit_skill_names: list[str] | tuple[str, ...] | None,
    explicit_tool_name: str | None,
    parent_task_id: str | None,
    delegation_briefing: str | None,
    agent_name: str | None,
    agent_definition_name: str | None,
    agent_instructions: str | None,
    allowed_routes: list[str] | tuple[str, ...] | None,
) -> dict:
    normalized_prompt = _normalize_subagent_prompt(prompt)
    normalized_skills = (
        normalize_agent_skill_names(cfg, explicit_skill_names) if explicit_skill_names else []
    )
    normalized_attachments = _normalized_subagent_attachments(attachments)
    normalized_tool_name = (
        str(explicit_tool_name).strip()
        if isinstance(explicit_tool_name, str) and explicit_tool_name.strip()
        else None
    )
    normalized_section = (
        str(section).strip() if isinstance(section, str) and section.strip() else None
    )
    normalized_parent_task_id = (
        str(parent_task_id).strip()
        if isinstance(parent_task_id, str) and parent_task_id.strip()
        else None
    )
    normalized_agent_name = (
        str(agent_name).strip() if isinstance(agent_name, str) and agent_name.strip() else None
    )
    normalized_agent_definition_name = (
        str(agent_definition_name).strip()
        if isinstance(agent_definition_name, str) and agent_definition_name.strip()
        else None
    )
    normalized_agent_instructions = _normalize_subagent_instructions(agent_instructions)
    normalized_delegation_briefing = _normalize_subagent_delegation_briefing(delegation_briefing)
    normalized_allowed_routes = _normalize_subagent_allowed_routes(
        allowed_routes,
        explicit_tool_name=normalized_tool_name,
    )
    return {
        "prompt": normalized_prompt,
        "request_source": (
            str(request_source).strip()
            if isinstance(request_source, str) and str(request_source).strip()
            else task_source
        ),
        "section": normalized_section,
        "attachments": normalized_attachments,
        "explicit_skill_names": normalized_skills,
        "explicit_tool_name": normalized_tool_name,
        "allowed_routes": normalized_allowed_routes,
        "parent_task_id": normalized_parent_task_id,
        "delegation_briefing": normalized_delegation_briefing,
        "agent_name": normalized_agent_name,
        "agent_definition_name": normalized_agent_definition_name,
        "agent_instructions": normalized_agent_instructions,
        "max_turns": 1,
    }


def _subagent_result_summary(turn_payload: dict) -> dict:
    tool_payload = turn_payload.get("tool") if isinstance(turn_payload.get("tool"), dict) else None
    return {
        "turn_id": turn_payload.get("turn_id"),
        "route": turn_payload.get("route"),
        "runtime_owner": turn_payload.get("runtime_owner"),
        "assistant_response": turn_payload.get("assistant", {}).get("response"),
        "assistant_source": turn_payload.get("assistant", {}).get("source"),
        "error": turn_payload.get("error"),
        "selected_skill_names": [
            skill.get("name")
            for skill in turn_payload.get("skills", [])
            if isinstance(skill, dict) and isinstance(skill.get("name"), str)
        ],
        "tool_name": tool_payload.get("name") if tool_payload else None,
        "tool_request": copy.deepcopy(tool_payload.get("request")) if tool_payload else None,
        "execution_summary": copy.deepcopy(turn_payload.get("execution", {}).get("summary") or {}),
    }


def _normalized_task_string(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    cleaned = value.strip()
    return cleaned or None


def _normalized_task_string_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []

    cleaned: list[str] = []
    seen: set[str] = set()
    for item in value:
        candidate = _normalized_task_string(item)
        if candidate is None or candidate in seen:
            continue
        cleaned.append(candidate)
        seen.add(candidate)
    return cleaned


def _subagent_task_context(summary: dict) -> dict | None:
    try:
        if normalize_task_kind(summary.get("kind"), "task kind") != TASK_KIND_SUBAGENT:
            return None
    except ValueError:
        return None

    metadata = _task_metadata(summary)
    prompt = _normalized_task_string(metadata.get("prompt"))
    agent_instructions = _normalized_task_string(metadata.get("agent_instructions"))
    delegation_briefing = _normalized_task_string(metadata.get("delegation_briefing"))
    explicit_tool_name = _normalized_task_string(metadata.get("explicit_tool_name"))
    explicit_skill_names = _normalized_task_string_list(metadata.get("explicit_skill_names"))
    attachments = _normalized_subagent_attachments(metadata.get("attachments"))
    try:
        allowed_routes = _normalize_subagent_allowed_routes(
            metadata.get("allowed_routes"),
            explicit_tool_name=explicit_tool_name,
        )
    except ValueError:
        allowed_routes = _normalized_task_string_list(metadata.get("allowed_routes"))

    prompt_sections: list[str] = []
    if agent_instructions:
        prompt_sections.append("agent_instructions")
    if delegation_briefing:
        prompt_sections.append("delegation_briefing")
    if prompt:
        prompt_sections.append("assigned_task")

    return {
        "has_prior_history": False,
        "history_message_count": 0,
        "prompt_sections": prompt_sections,
        "prompt_section_count": len(prompt_sections),
        "prompt_char_count": len(prompt or ""),
        "has_agent_instructions": bool(agent_instructions),
        "agent_instructions_char_count": len(agent_instructions or ""),
        "has_delegation_briefing": bool(delegation_briefing),
        "delegation_briefing_char_count": len(delegation_briefing or ""),
        "attachment_count": len(attachments),
        "explicit_skill_names": explicit_skill_names,
        "explicit_tool_name": explicit_tool_name,
        "allowed_routes": allowed_routes,
    }


def _validate_parent_task_link(settings: dict, parent_task_id: str | None) -> dict | None:
    if parent_task_id is None:
        return None
    return _read_task_summary(settings, parent_task_id)


def _record_child_task_link(settings: dict, parent_task_id: str | None, child_task_id: str) -> None:
    if parent_task_id is None:
        return

    parent_summary = _read_task_summary(settings, parent_task_id)
    metadata = _task_metadata(parent_summary)
    child_task_ids = (
        metadata.get("child_task_ids") if isinstance(metadata.get("child_task_ids"), list) else []
    )
    normalized_child_task_ids = [
        task_id for task_id in child_task_ids if isinstance(task_id, str) and task_id.strip()
    ]
    if child_task_id not in normalized_child_task_ids:
        normalized_child_task_ids.append(child_task_id)
    metadata["child_task_ids"] = normalized_child_task_ids
    parent_summary["metadata"] = metadata
    parent_summary["last_child_task_id"] = child_task_id
    _write_task_summary(settings, parent_summary)


def _task_counts(task_summaries: list[dict]) -> tuple[dict[str, int], dict[str, int]]:
    by_status: dict[str, int] = {}
    by_kind: dict[str, int] = {}
    for task in task_summaries:
        status = str(task.get("status") or "unknown")
        kind = str(task.get("kind") or "unknown")
        by_status[status] = by_status.get(status, 0) + 1
        by_kind[kind] = by_kind.get(kind, 0) + 1
    return by_status, by_kind


def _task_lineage_summary(task_summaries: list[dict]) -> dict:
    root_task_count = 0
    child_task_count = 0
    parent_task_count = 0

    for task in task_summaries:
        if _task_parent_task_id(task) is None:
            root_task_count += 1
        else:
            child_task_count += 1
        if _task_child_task_ids(task):
            parent_task_count += 1

    return {
        "root_task_count": root_task_count,
        "child_task_count": child_task_count,
        "parent_task_count": parent_task_count,
    }


def list_agent_tasks(
    cfg: dict,
    *,
    task_kind: str | None = None,
    task_status: str | None = None,
    task_source: str | None = None,
) -> dict:
    settings = resolve_agent_task_manager_settings(cfg)
    ensure_agent_task_manager_layout(settings)

    normalized_kind = normalize_task_kind(task_kind) if task_kind else None
    normalized_status = normalize_task_status(task_status) if task_status else None
    normalized_source = None
    if task_source is not None:
        if not isinstance(task_source, str) or not task_source.strip():
            raise TaskManagerError("task source must be a non-empty string")
        normalized_source = task_source.strip()

    tasks: list[dict] = []
    errors: list[dict] = []
    for summary_path in Path(settings["tasks_dir"]).glob("*.json"):
        try:
            summary = read_json_file(str(summary_path))
            if not isinstance(summary, dict):
                raise TaskManagerError("task summary must contain a top-level object")
        except Exception as exc:
            errors.append(
                {
                    "task_summary_path": str(summary_path.resolve()),
                    "error": str(exc),
                }
            )
            continue

        if normalized_kind and summary.get("kind") != normalized_kind:
            continue
        if normalized_status and summary.get("status") != normalized_status:
            continue
        if normalized_source and str(summary.get("source") or "") != normalized_source:
            continue
        tasks.append(summary)

    tasks.sort(
        key=lambda item: (
            str(item.get("updated_at") or ""),
            str(item.get("task_id") or ""),
        ),
        reverse=True,
    )
    by_status, by_kind = _task_counts(tasks)
    lineage = _task_lineage_summary(tasks)
    active_task_count = sum(1 for task in tasks if _task_is_active(task))
    restartable_task_count = sum(1 for task in tasks if _task_is_resumable(task))
    payload = {
        **settings,
        "filters": {
            "kind": normalized_kind,
            "status": normalized_status,
            "source": normalized_source,
        },
        "task_count": len(tasks),
        "active_task_count": active_task_count,
        "restartable_task_count": restartable_task_count,
        "by_status": by_status,
        "by_kind": by_kind,
        "lineage": lineage,
        "tasks": [_task_list_payload(task) for task in tasks],
    }
    if errors:
        payload["errors"] = errors
    return payload


def describe_agent_task(
    cfg: dict,
    task_id: str,
    *,
    tail: int = 20,
    transcript_tail: int | None = None,
) -> dict:
    if tail < 0:
        raise TaskManagerError("tail must be zero or greater")
    if transcript_tail is not None and transcript_tail < 0:
        raise TaskManagerError("transcript_tail must be zero or greater")

    settings = resolve_agent_task_manager_settings(cfg)
    summary = _read_task_summary(settings, task_id)
    log_path = Path(str(summary.get("log_path") or _task_log_path(settings, task_id))).expanduser()
    if not log_path.is_absolute():
        log_path = Path(os.path.abspath(str(log_path)))

    log_lines = _task_log_lines(log_path)

    task_payload = _task_detail_payload(summary)
    transcript_payload = _task_transcript_payload(
        settings,
        summary,
        tail=tail if transcript_tail is None else transcript_tail,
    )
    if transcript_payload is not None:
        task_payload["transcript_path"] = transcript_payload["transcript_path"]

    payload = {
        **settings,
        "task": task_payload,
        "log_path": str(log_path.resolve()),
        "log_line_count": len(log_lines),
        "log_tail": log_lines[-tail:] if tail else [],
    }
    if transcript_payload is not None:
        payload["transcript"] = transcript_payload
    return payload


def attach_agent_task(
    cfg: dict,
    task_id: str,
    *,
    cursor: int = 0,
    limit: int = DEFAULT_ATTACH_LINE_LIMIT,
) -> dict:
    if isinstance(cursor, bool) or not isinstance(cursor, int) or cursor < 0:
        raise TaskManagerError("attach cursor must be zero or greater")
    if isinstance(limit, bool) or not isinstance(limit, int) or limit <= 0:
        raise TaskManagerError("attach limit must be a positive integer")

    settings = resolve_agent_task_manager_settings(cfg)
    summary = _read_task_summary(settings, task_id)
    log_path = Path(str(summary.get("log_path") or _task_log_path(settings, task_id))).expanduser()
    if not log_path.is_absolute():
        log_path = Path(os.path.abspath(str(log_path)))
    log_lines = _task_log_lines(log_path)
    safe_cursor = min(cursor, len(log_lines))
    attached_lines = log_lines[safe_cursor : safe_cursor + limit]
    process_running = _task_process_running(summary)
    task_payload = _task_detail_payload(summary, process_running=process_running)

    return {
        **settings,
        "task": task_payload,
        "log_path": str(log_path.resolve()),
        "cursor": cursor,
        "next_cursor": safe_cursor + len(attached_lines),
        "log_line_count": len(log_lines),
        "process_running": process_running,
        "stream_complete": (safe_cursor + len(attached_lines)) >= len(log_lines)
        and not process_running,
        "attached_lines": attached_lines,
    }


def summarize_agent_tasks(
    cfg: dict,
    *,
    task_kind: str | None = None,
    task_status: str | None = None,
    task_source: str | None = None,
    recent_limit: int = DEFAULT_TASK_RECENT_LIMIT,
) -> dict:
    if isinstance(recent_limit, bool) or not isinstance(recent_limit, int) or recent_limit <= 0:
        raise TaskManagerError("recent_limit must be a positive integer")

    listing = list_agent_tasks(
        cfg,
        task_kind=task_kind,
        task_status=task_status,
        task_source=task_source,
    )
    tasks = listing["tasks"]
    active_tasks = [task for task in tasks if task.get("active")]
    restartable_tasks = [task for task in tasks if task.get("restartable")]
    tasks_with_children = [task for task in tasks if int(task.get("child_task_count", 0) or 0) > 0]
    lineage = copy.deepcopy(listing.get("lineage") or {})
    lineage["tasks_with_children"] = copy.deepcopy(tasks_with_children[:recent_limit])
    return {
        "enabled": listing["enabled"],
        "root_dir": listing["root_dir"],
        "tasks_dir": listing["tasks_dir"],
        "logs_dir": listing["logs_dir"],
        "transcripts_dir": listing["transcripts_dir"],
        "filters": copy.deepcopy(listing["filters"]),
        "task_count": listing["task_count"],
        "active_task_count": listing["active_task_count"],
        "restartable_task_count": listing["restartable_task_count"],
        "by_status": copy.deepcopy(listing["by_status"]),
        "by_kind": copy.deepcopy(listing["by_kind"]),
        "lineage": lineage,
        "recent_limit": recent_limit,
        "recent_tasks": copy.deepcopy(tasks[:recent_limit]),
        "active_tasks": copy.deepcopy(active_tasks[:recent_limit]),
        "restartable_tasks": copy.deepcopy(restartable_tasks[:recent_limit]),
        **({"errors": copy.deepcopy(listing["errors"])} if "errors" in listing else {}),
    }


def start_subagent_task(
    cfg: dict,
    config_path: str,
    prompt: str,
    *,
    agent_definition_name: str | None = None,
    agent_instructions: str | None = None,
    source: str = "operator",
    request_source: str | None = None,
    section: str | None = None,
    attachments: list[str] | None = None,
    explicit_skill_names: list[str] | tuple[str, ...] | None = None,
    explicit_tool_name: str | None = None,
    parent_task_id: str | None = None,
    delegation_briefing: str | None = None,
    agent_name: str | None = None,
    allowed_routes: list[str] | tuple[str, ...] | None = None,
    task_metadata: dict | None = None,
) -> dict:
    settings = resolve_agent_task_manager_settings(cfg)
    ensure_agent_task_manager_layout(settings)

    _validate_parent_task_link(settings, parent_task_id)

    resolved_agent_definition_name = None
    resolved_agent_instructions = _normalize_subagent_instructions(agent_instructions)
    resolved_section = section
    resolved_explicit_skill_names = list(explicit_skill_names or [])
    resolved_explicit_tool_name = explicit_tool_name
    resolved_agent_name = agent_name
    resolved_allowed_routes = list(allowed_routes or [])

    if isinstance(agent_definition_name, str) and agent_definition_name.strip():
        if resolved_agent_instructions is None:
            agent_defaults = resolve_agent_definition_task_defaults(cfg, agent_definition_name)
            resolved_agent_definition_name = agent_defaults["agent_definition_name"]
            resolved_agent_instructions = agent_defaults["instructions"]
            if resolved_section is None:
                resolved_section = agent_defaults["section"]
            resolved_explicit_skill_names = [
                *agent_defaults["explicit_skill_names"],
                *resolved_explicit_skill_names,
            ]
            if resolved_explicit_tool_name is None:
                resolved_explicit_tool_name = agent_defaults["explicit_tool_name"]
            if not resolved_allowed_routes:
                resolved_allowed_routes = list(agent_defaults["allowed_routes"])
            if resolved_agent_name is None:
                resolved_agent_name = agent_defaults["title"]
        else:
            resolved_agent_definition_name = str(agent_definition_name).strip()

    metadata = _subagent_task_metadata(
        cfg,
        prompt=prompt,
        task_source=source,
        request_source=request_source,
        section=resolved_section,
        attachments=attachments,
        explicit_skill_names=resolved_explicit_skill_names,
        explicit_tool_name=resolved_explicit_tool_name,
        parent_task_id=parent_task_id,
        delegation_briefing=delegation_briefing,
        agent_name=resolved_agent_name,
        agent_definition_name=resolved_agent_definition_name,
        agent_instructions=resolved_agent_instructions,
        allowed_routes=resolved_allowed_routes,
    )
    if isinstance(task_metadata, dict):
        metadata.update(copy.deepcopy(task_metadata))

    task_id = f"agent-task-{uuid.uuid4().hex[:12]}"
    task_name = metadata.get("agent_name") or "subagent"
    summary = _task_summary(
        settings,
        task_id=task_id,
        kind=TASK_KIND_SUBAGENT,
        name=str(task_name),
        config_path=config_path,
        source=source,
        metadata=metadata,
    )
    summary = _write_task_summary(settings, summary)
    started_summary = _start_task_process(
        settings,
        summary,
        _worker_command(
            config_path,
            task_id=task_id,
            kind=TASK_KIND_SUBAGENT,
        ),
    )
    _record_child_task_link(settings, metadata.get("parent_task_id"), started_summary["task_id"])
    return started_summary


def parse_task_vars(values: list[str]) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for item in values:
        if "=" not in item:
            raise TaskManagerError(f"task variable '{item}' must use KEY=VALUE format")
        key, value = item.split("=", 1)
        if not key.strip():
            raise TaskManagerError("task variable name must be a non-empty string")
        parsed[key.strip()] = value
    return parsed


def _worker_command(
    config_path: str,
    *,
    task_id: str,
    kind: str,
    workflow_name: str | None = None,
    extra_vars: dict[str, str] | None = None,
) -> list[str]:
    command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--config",
        os.path.abspath(config_path),
        "worker",
        "--task-id",
        task_id,
        "--kind",
        normalize_task_kind(kind),
    ]
    if workflow_name is not None:
        command.extend(["--workflow", workflow_name])
    for key, value in sorted((extra_vars or {}).items()):
        command.extend(["--var", f"{key}={value}"])
    return command


def _start_task_process(settings: dict, summary: dict, command: list[str]) -> dict:
    log_path = Path(summary["log_path"])
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as log_handle:
        process = subprocess.Popen(
            command,
            cwd=str(REPO_ROOT),
            env=os.environ.copy(),
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )

    updated_summary = copy.deepcopy(summary)
    updated_summary["status"] = TASK_STATUS_RUNNING
    updated_summary["pid"] = process.pid
    updated_summary["started_at"] = updated_summary.get("started_at") or current_utc_timestamp()
    updated_summary["command"] = command
    return _write_task_summary(settings, updated_summary)


def start_workflow_task(
    cfg: dict,
    config_path: str,
    workflow_name: str,
    extra_vars: dict[str, str] | None = None,
    *,
    source: str = "operator",
    task_metadata: dict | None = None,
) -> dict:
    settings = resolve_agent_task_manager_settings(cfg)
    ensure_agent_task_manager_layout(settings)

    rendered = render_workflow_steps(cfg, config_path, workflow_name, extra_vars)
    task_id = f"agent-task-{uuid.uuid4().hex[:12]}"
    metadata = {
        "workflow": rendered["workflow"],
        "description": rendered["description"],
        "required_vars": list(rendered["required_vars"]),
        "defaults": copy.deepcopy(rendered["defaults"]),
        "tags": list(rendered["tags"]),
        "variables": copy.deepcopy(rendered["variables"]),
        "step_count": len(rendered["steps"]),
    }
    if isinstance(task_metadata, dict):
        metadata.update(copy.deepcopy(task_metadata))

    summary = _task_summary(
        settings,
        task_id=task_id,
        kind=TASK_KIND_WORKFLOW,
        name=rendered["workflow"],
        config_path=config_path,
        source=source,
        metadata=metadata,
    )
    summary = _write_task_summary(settings, summary)
    return _start_task_process(
        settings,
        summary,
        _worker_command(
            config_path,
            task_id=task_id,
            kind=TASK_KIND_WORKFLOW,
            workflow_name=rendered["workflow"],
            extra_vars=extra_vars,
        ),
    )


def start_dream_task(
    cfg: dict,
    config_path: str,
    *,
    source: str = "operator",
    task_metadata: dict | None = None,
) -> dict:
    settings = resolve_agent_task_manager_settings(cfg)
    ensure_agent_task_manager_layout(settings)

    task_id = f"agent-task-{uuid.uuid4().hex[:12]}"
    metadata = {
        "dream_enabled": bool(
            isinstance(cfg.get("dream"), dict) and cfg["dream"].get("enabled", False)
        )
    }
    if isinstance(task_metadata, dict):
        metadata.update(copy.deepcopy(task_metadata))

    summary = _task_summary(
        settings,
        task_id=task_id,
        kind=TASK_KIND_DREAM,
        name="dream",
        config_path=config_path,
        source=source,
        metadata=metadata,
    )
    summary = _write_task_summary(settings, summary)
    return _start_task_process(
        settings,
        summary,
        _worker_command(
            config_path,
            task_id=task_id,
            kind=TASK_KIND_DREAM,
        ),
    )


def _run_subagent_turn(cfg: dict, summary: dict) -> dict:
    from agent_shell import (
        build_completion_fn,
        resolve_agent_shell_settings,
        resolve_agent_shell_system_prompt,
        run_agent_turn,
    )

    metadata = _task_metadata(summary)
    prompt = _normalize_subagent_prompt(metadata.get("prompt"))
    agent_instructions = _normalize_subagent_instructions(metadata.get("agent_instructions"))
    delegation_briefing = _normalize_subagent_delegation_briefing(
        metadata.get("delegation_briefing")
    )
    explicit_tool_name = metadata.get("explicit_tool_name")
    allowed_routes = _normalize_subagent_allowed_routes(
        metadata.get("allowed_routes"),
        explicit_tool_name=explicit_tool_name,
    )
    section = metadata.get("section") if isinstance(metadata.get("section"), str) else None
    attachments = _normalized_subagent_attachments(metadata.get("attachments"))
    route_decision = route_request(
        cfg,
        prompt,
        source=str(metadata.get("request_source") or summary.get("source") or "subagent"),
        section=section,
        attachments=attachments,
        tool_name=explicit_tool_name,
    )
    resolved_route = normalize_route(route_decision.get("resolved_route"), "subagent route")
    if resolved_route not in set(allowed_routes):
        choices = ", ".join(allowed_routes)
        raise TaskManagerError(
            f"subagent task route '{resolved_route}' is not allowed; allowed routes: {choices}"
        )

    settings = resolve_agent_shell_settings(cfg)
    system_prompt, _ = resolve_agent_shell_system_prompt(cfg)
    completion_fn = build_completion_fn(settings)
    execution_prompt = _compose_subagent_execution_prompt(
        prompt,
        agent_instructions=agent_instructions,
        delegation_briefing=delegation_briefing,
    )
    parent_task_id = (
        str(summary.get("task_id")).strip()
        if isinstance(summary.get("task_id"), str) and str(summary.get("task_id")).strip()
        else None
    )
    child_delegation_briefing = _build_subagent_delegation_briefing(summary)
    return run_agent_turn(
        cfg,
        settings,
        execution_prompt,
        config_path=str(summary.get("config_path") or "config.yaml"),
        system_prompt=system_prompt,
        history_messages=[],
        source=str(metadata.get("request_source") or summary.get("source") or "subagent"),
        section=section,
        attachments=attachments,
        explicit_tool_name=explicit_tool_name,
        parent_task_id=parent_task_id,
        delegation_briefing=child_delegation_briefing,
        explicit_skill_names=list(metadata.get("explicit_skill_names") or []),
        pinned_skill_names=[],
        completion_fn=completion_fn,
        turn_index=0,
    )


def resume_agent_task(
    cfg: dict,
    task_id: str,
    *,
    source: str = "operator_resume",
) -> dict:
    settings = resolve_agent_task_manager_settings(cfg)
    summary = _read_task_summary(settings, task_id)
    status = normalize_task_status(summary.get("status"), "task status")
    if status not in RESUMABLE_TASK_STATUSES:
        raise TaskManagerError(f"task '{task_id}' is not resumable because it is {status}")

    kind = normalize_task_kind(summary.get("kind"), "task kind")
    metadata = _task_metadata(summary)
    resume_metadata = {
        "resumed_from_task_id": task_id,
        "resumed_from_status": status,
        "resumed_from_kind": kind,
        "resume_depth": _task_resume_depth(summary) + 1,
    }
    config_path = str(summary.get("config_path") or "config.yaml")
    if kind == TASK_KIND_WORKFLOW:
        validate_workflow_registry_config(cfg)
        workflow_name = str(metadata.get("workflow") or summary.get("name") or "").strip()
        if not workflow_name:
            raise TaskManagerError(f"task '{task_id}' does not record a workflow name")
        resumed_summary = start_workflow_task(
            cfg,
            config_path,
            workflow_name,
            _task_variables(summary),
            source=source,
            task_metadata=resume_metadata,
        )
    elif kind == TASK_KIND_DREAM:
        validate_dream_config(cfg)
        resumed_summary = start_dream_task(
            cfg,
            config_path,
            source=source,
            task_metadata=resume_metadata,
        )
    elif kind == TASK_KIND_SUBAGENT:
        resumed_summary = start_subagent_task(
            cfg,
            config_path,
            _normalize_subagent_prompt(metadata.get("prompt")),
            agent_definition_name=(
                str(metadata.get("agent_definition_name"))
                if isinstance(metadata.get("agent_definition_name"), str)
                and str(metadata.get("agent_definition_name")).strip()
                else None
            ),
            agent_instructions=_normalize_subagent_instructions(metadata.get("agent_instructions")),
            source=source,
            request_source=(
                str(metadata.get("request_source"))
                if isinstance(metadata.get("request_source"), str)
                and str(metadata.get("request_source")).strip()
                else None
            ),
            section=metadata.get("section") if isinstance(metadata.get("section"), str) else None,
            attachments=_normalized_subagent_attachments(metadata.get("attachments")),
            explicit_skill_names=list(metadata.get("explicit_skill_names") or []),
            explicit_tool_name=(
                str(metadata.get("explicit_tool_name"))
                if isinstance(metadata.get("explicit_tool_name"), str)
                and str(metadata.get("explicit_tool_name")).strip()
                else None
            ),
            parent_task_id=(
                str(metadata.get("parent_task_id"))
                if isinstance(metadata.get("parent_task_id"), str)
                and str(metadata.get("parent_task_id")).strip()
                else None
            ),
            delegation_briefing=_normalize_subagent_delegation_briefing(
                metadata.get("delegation_briefing")
            ),
            agent_name=(
                str(metadata.get("agent_name"))
                if isinstance(metadata.get("agent_name"), str)
                and str(metadata.get("agent_name")).strip()
                else None
            ),
            allowed_routes=list(metadata.get("allowed_routes") or []),
            task_metadata=resume_metadata,
        )
    else:
        raise TaskManagerError(f"unsupported task kind for resume: {kind}")

    updated_summary = copy.deepcopy(summary)
    updated_summary["resumed_at"] = current_utc_timestamp()
    updated_summary["resumed_by_task_id"] = resumed_summary["task_id"]
    updated_summary["resume_count"] = int(summary.get("resume_count", 0) or 0) + 1
    _write_task_summary(settings, updated_summary)
    return resumed_summary


def cancel_agent_task(cfg: dict, task_id: str) -> dict:
    settings = resolve_agent_task_manager_settings(cfg)
    summary = _read_task_summary(settings, task_id)
    status = normalize_task_status(summary.get("status"), "task status")
    if status not in {TASK_STATUS_PENDING, TASK_STATUS_RUNNING}:
        raise TaskManagerError(
            f"task '{task_id}' is not cancellable because it is already {status}"
        )

    pid = summary.get("pid")
    if isinstance(pid, bool) or not isinstance(pid, int) or pid <= 0:
        raise TaskManagerError(f"task '{task_id}' does not have a live process id")

    try:
        os.killpg(os.getpgid(pid), signal.SIGTERM)
    except ProcessLookupError as exc:
        raise TaskManagerError(f"task '{task_id}' process is no longer running") from exc

    updated_summary = copy.deepcopy(summary)
    updated_summary["cancel_requested_at"] = current_utc_timestamp()
    return _write_task_summary(settings, updated_summary)


def _workflow_result_summary(result: dict) -> dict:
    return {
        "workflow": result.get("workflow"),
        "description": result.get("description"),
        "executed_steps": int(result.get("executed_steps", 0) or 0),
        "step_count": len(result.get("steps", [])) if isinstance(result.get("steps"), list) else 0,
        "tags": copy.deepcopy(result.get("tags", [])),
        "variables": copy.deepcopy(result.get("variables", {})),
        "dream": copy.deepcopy(result.get("dream", {})),
    }


def _log_task_event(message: str, payload: dict | None = None) -> None:
    print(message)
    if isinstance(payload, dict):
        print(json.dumps(payload, indent=2, sort_keys=False))


def run_task_worker(
    cfg: dict,
    *,
    task_id: str,
    kind: str,
    workflow_name: str | None = None,
    extra_vars: dict[str, str] | None = None,
) -> dict:
    settings = resolve_agent_task_manager_settings(cfg)
    summary = _read_task_summary(settings, task_id)
    cancel_state = {"requested": False, "signal": None}
    normalized_kind: str | None = None

    def _handle_cancel(signum, _frame) -> None:
        cancel_state["requested"] = True
        cancel_state["signal"] = signum
        raise TaskCancelledError(f"task cancelled by signal {signum}")

    previous_sigterm = signal.signal(signal.SIGTERM, _handle_cancel)
    previous_sigint = signal.signal(signal.SIGINT, _handle_cancel)

    updated_summary = copy.deepcopy(summary)
    updated_summary["status"] = TASK_STATUS_RUNNING
    updated_summary["pid"] = os.getpid()
    updated_summary["started_at"] = updated_summary.get("started_at") or current_utc_timestamp()
    updated_summary = _write_task_summary(settings, updated_summary)

    try:
        normalized_kind = normalize_task_kind(kind)
        if normalized_kind in {TASK_KIND_WORKFLOW, TASK_KIND_DREAM}:
            transcript_event = _task_transcript_event(
                updated_summary,
                event_type=TASK_TRANSCRIPT_EVENT_STARTED,
            )
            if transcript_event is not None:
                _append_task_transcript_record(settings, updated_summary, transcript_event)
        if normalized_kind == TASK_KIND_WORKFLOW:
            if not isinstance(workflow_name, str) or not workflow_name.strip():
                raise TaskManagerError("workflow task requires a workflow name")
            result = run_workflow(
                cfg,
                updated_summary["config_path"],
                workflow_name,
                extra_vars,
            )
            updated_summary["result"] = _workflow_result_summary(result)
        elif normalized_kind == TASK_KIND_DREAM:
            updated_summary["result"] = copy.deepcopy(run_memory_dream(cfg))
        elif normalized_kind == TASK_KIND_SUBAGENT:
            _log_task_event("subagent task started", {"task_id": task_id})
            turn_payload = _run_subagent_turn(cfg, updated_summary)
            _write_task_transcript_turn(settings, updated_summary, turn_payload)
            updated_summary["result"] = _subagent_result_summary(turn_payload)
            _log_task_event(
                "subagent task completed",
                {
                    "task_id": task_id,
                    "route": turn_payload.get("route"),
                    "runtime_owner": turn_payload.get("runtime_owner"),
                    "assistant_response": turn_payload.get("assistant", {}).get("response"),
                },
            )
        else:
            raise TaskManagerError(f"unsupported task kind: {normalized_kind}")

        updated_summary["status"] = TASK_STATUS_COMPLETED
        updated_summary["exit_code"] = 0
        updated_summary["error"] = None
    except TaskCancelledError as exc:
        updated_summary["status"] = TASK_STATUS_CANCELLED
        updated_summary["exit_code"] = 128 + int(cancel_state["signal"] or signal.SIGTERM)
        updated_summary["error"] = str(exc)
    except subprocess.CalledProcessError as exc:
        if cancel_state["requested"]:
            updated_summary["status"] = TASK_STATUS_CANCELLED
            updated_summary["exit_code"] = 128 + int(cancel_state["signal"] or signal.SIGTERM)
            updated_summary["error"] = f"task cancelled by signal {cancel_state['signal']}"
        else:
            updated_summary["status"] = TASK_STATUS_FAILED
            updated_summary["exit_code"] = int(exc.returncode)
            updated_summary["error"] = str(exc)
    except Exception as exc:
        updated_summary["status"] = TASK_STATUS_FAILED
        updated_summary["exit_code"] = 1
        updated_summary["error"] = str(exc)
    finally:
        try:
            updated_summary["completed_at"] = current_utc_timestamp()
            updated_summary["pid"] = os.getpid()
            if normalized_kind in {TASK_KIND_WORKFLOW, TASK_KIND_DREAM}:
                transcript_event = _task_transcript_event(
                    updated_summary,
                    event_type=_task_transcript_event_type(updated_summary.get("status")),
                )
                if transcript_event is not None:
                    _append_task_transcript_record(settings, updated_summary, transcript_event)
            updated_summary = _write_task_summary(settings, updated_summary)
        finally:
            signal.signal(signal.SIGTERM, previous_sigterm)
            signal.signal(signal.SIGINT, previous_sigint)

    return updated_summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manage local background tasks for simcoe.ai.")
    parser.add_argument("--config", default="config.yaml", help="Config file to use")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List saved tasks")
    list_parser.add_argument("--kind", help="Optional task kind filter")
    list_parser.add_argument("--status", help="Optional task status filter")
    list_parser.add_argument("--source", help="Optional task source filter")

    status_parser = subparsers.add_parser("status", help="Show a compact task status summary")
    status_parser.add_argument("--kind", help="Optional task kind filter")
    status_parser.add_argument("--status", help="Optional task status filter")
    status_parser.add_argument("--source", help="Optional task source filter")
    status_parser.add_argument(
        "--recent-limit",
        type=int,
        default=DEFAULT_TASK_RECENT_LIMIT,
        help="How many recent tasks to include in summary lists.",
    )

    attach_parser = subparsers.add_parser(
        "attach",
        help="Reattach to an existing task by reading new log lines from a cursor",
    )
    attach_parser.add_argument("task_id", help="Task id to attach to")
    attach_parser.add_argument(
        "--cursor",
        type=int,
        default=0,
        help="Zero-based log cursor to resume from.",
    )
    attach_parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_ATTACH_LINE_LIMIT,
        help="Maximum number of log lines to return.",
    )

    show_parser = subparsers.add_parser("show", help="Show one task summary and recent logs")
    show_parser.add_argument("task_id", help="Task id to inspect")
    show_parser.add_argument("--tail", type=int, default=20, help="Recent log lines to include")
    show_parser.add_argument(
        "--transcript-tail",
        type=int,
        help="Recent structured transcript records to include. Defaults to --tail.",
    )

    start_workflow_parser = subparsers.add_parser(
        "start-workflow",
        help="Start a checked-in workflow as a background task",
    )
    start_workflow_parser.add_argument("workflow", help="Workflow name to run")
    start_workflow_parser.add_argument(
        "--var",
        action="append",
        default=[],
        help="Workflow variable assignment in KEY=VALUE form. Can be repeated.",
    )
    start_workflow_parser.add_argument(
        "--source",
        default="operator",
        help="Task source label recorded in the task summary.",
    )

    start_dream_parser = subparsers.add_parser(
        "start-dream",
        help="Start a background dream-memory consolidation task",
    )
    start_dream_parser.add_argument(
        "--source",
        default="operator",
        help="Task source label recorded in the task summary.",
    )

    start_subagent_parser = subparsers.add_parser(
        "start-subagent",
        help="Start a bounded background subagent task",
    )
    start_subagent_parser.add_argument(
        "--agent",
        help="Optional local agent definition id or alias.",
    )
    start_subagent_parser.add_argument(
        "--prompt",
        required=True,
        help="Prompt for the background subagent worker.",
    )
    start_subagent_parser.add_argument(
        "--source",
        default="operator_subagent",
        help="Task source label recorded in the task summary.",
    )
    start_subagent_parser.add_argument("--section", help="Optional section hint for routing.")
    start_subagent_parser.add_argument(
        "--attachment",
        action="append",
        default=[],
        help="Optional attachment path. Can be repeated.",
    )
    start_subagent_parser.add_argument(
        "--skill",
        action="append",
        default=[],
        help="Optional local skill id or alias. Can be repeated.",
    )
    start_subagent_parser.add_argument(
        "--tool-name",
        help="Optional explicit deterministic tool restriction.",
    )
    start_subagent_parser.add_argument(
        "--parent-task-id",
        help="Optional parent task id for explicit child linkage.",
    )
    start_subagent_parser.add_argument(
        "--briefing",
        help="Optional delegation briefing passed into the subagent prompt.",
    )
    start_subagent_parser.add_argument(
        "--agent-name",
        help="Optional friendly display name for the subagent task.",
    )
    start_subagent_parser.add_argument(
        "--allow-route",
        action="append",
        default=[],
        help="Optional allowed route override. Can be repeated.",
    )

    cancel_parser = subparsers.add_parser("cancel", help="Request cancellation for one task")
    cancel_parser.add_argument("task_id", help="Task id to cancel")

    resume_parser = subparsers.add_parser(
        "resume", help="Resume a failed, cancelled, or pending task"
    )
    resume_parser.add_argument("task_id", help="Task id to resume")
    resume_parser.add_argument(
        "--source",
        default="operator_resume",
        help="Task source label recorded in the resumed task summary.",
    )

    worker_parser = subparsers.add_parser("worker", help=argparse.SUPPRESS)
    worker_parser.add_argument("--task-id", required=True)
    worker_parser.add_argument("--kind", required=True)
    worker_parser.add_argument("--workflow")
    worker_parser.add_argument("--var", action="append", default=[])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = load_config(args.config)

    try:
        if args.command == "list":
            validate_agent_task_manager_config(cfg)
            payload = list_agent_tasks(
                cfg,
                task_kind=args.kind,
                task_status=args.status,
                task_source=args.source,
            )
            print(__import__("json").dumps(payload, indent=2, sort_keys=False))
            return 0
        if args.command == "status":
            validate_agent_task_manager_config(cfg)
            payload = summarize_agent_tasks(
                cfg,
                task_kind=args.kind,
                task_status=args.status,
                task_source=args.source,
                recent_limit=args.recent_limit,
            )
            print(__import__("json").dumps(payload, indent=2, sort_keys=False))
            return 0
        if args.command == "attach":
            validate_agent_task_manager_config(cfg)
            payload = attach_agent_task(
                cfg,
                args.task_id,
                cursor=args.cursor,
                limit=args.limit,
            )
            print(__import__("json").dumps(payload, indent=2, sort_keys=False))
            return 0
        if args.command == "show":
            validate_agent_task_manager_config(cfg)
            payload = describe_agent_task(
                cfg,
                args.task_id,
                tail=args.tail,
                transcript_tail=args.transcript_tail,
            )
            print(__import__("json").dumps(payload, indent=2, sort_keys=False))
            return 0
        if args.command == "start-workflow":
            validate_agent_task_manager_config(cfg)
            validate_workflow_registry_config(cfg)
            payload = start_workflow_task(
                cfg,
                args.config,
                args.workflow,
                parse_task_vars(args.var),
                source=args.source,
            )
            print(__import__("json").dumps(payload, indent=2, sort_keys=False))
            return 0
        if args.command == "start-dream":
            validate_agent_task_manager_config(cfg)
            validate_dream_config(cfg)
            payload = start_dream_task(cfg, args.config, source=args.source)
            print(__import__("json").dumps(payload, indent=2, sort_keys=False))
            return 0
        if args.command == "start-subagent":
            validate_agent_task_manager_config(cfg)
            payload = start_subagent_task(
                cfg,
                args.config,
                args.prompt,
                agent_definition_name=args.agent,
                source=args.source,
                section=args.section,
                attachments=args.attachment,
                explicit_skill_names=args.skill,
                explicit_tool_name=args.tool_name,
                parent_task_id=args.parent_task_id,
                delegation_briefing=args.briefing,
                agent_name=args.agent_name,
                allowed_routes=args.allow_route,
            )
            print(__import__("json").dumps(payload, indent=2, sort_keys=False))
            return 0
        if args.command == "cancel":
            validate_agent_task_manager_config(cfg)
            payload = cancel_agent_task(cfg, args.task_id)
            print(__import__("json").dumps(payload, indent=2, sort_keys=False))
            return 0
        if args.command == "resume":
            validate_agent_task_manager_config(cfg)
            payload = resume_agent_task(cfg, args.task_id, source=args.source)
            print(__import__("json").dumps(payload, indent=2, sort_keys=False))
            return 0
        if args.command == "worker":
            payload = run_task_worker(
                cfg,
                task_id=args.task_id,
                kind=args.kind,
                workflow_name=args.workflow,
                extra_vars=parse_task_vars(args.var),
            )
            return (
                0
                if payload.get("status") == TASK_STATUS_COMPLETED
                else int(payload.get("exit_code") or 1)
            )
        raise TaskManagerError(f"unsupported command: {args.command}")
    except (TaskManagerError, WorkflowRegistryError, ValueError) as exc:
        print(f"❌  {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
