"""
Local interactive agent shell built on the existing simcoe.ai routing,
context-provider, hook, deterministic-tool, and prompt-template surfaces.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path
from typing import Callable
import uuid

from dotenv import load_dotenv

from agent_command_registry import execute_agent_command
from agent_skill_registry import render_agent_skill_prompt, select_agent_skills
from agent_tool_registry import execute_inferred_agent_tool
from config_validation import (
    load_config,
    validate_agent_shell_config,
    validate_architecture_config,
    validate_deterministic_tools_config,
    validate_orchestration_config,
    validate_retrieval_config,
    validate_routing_config,
    validate_system_prompts_config,
)
from context_providers import build_context_provider_registry
from manifest_utils import current_utc_timestamp, read_json_file, write_json_file
from orchestration_inspect import describe_context_providers
from prompt_templates import (
    SYSTEM_PROMPT_SURFACE_AGENT_SHELL,
    resolve_configured_system_prompt,
)
from request_router import route_request
from retrieval_utils import build_context_augmented_prompt
from runtime_contracts import (
    CONTEXT_PROVIDER_MEMORY,
    CONTEXT_PROVIDER_RETRIEVAL,
    ROUTE_DETERMINISTIC_TOOL,
    ROUTE_RETRIEVAL,
    ROUTE_TEXT,
    summarize_execution_envelopes,
)


load_dotenv()

SESSION_SCHEMA_VERSION = 1
TURN_SCHEMA_VERSION = 1
SUPPORTED_MODEL_ROUTES = {ROUTE_TEXT, ROUTE_RETRIEVAL}
DEFAULT_SESSION_HISTORY_TURN_WINDOW = 6
SESSION_HISTORY_SUMMARY_MAX_CHARS = 2000
SESSION_HISTORY_SUMMARY_LINE_PROMPT_CHARS = 96
SESSION_HISTORY_SUMMARY_LINE_RESPONSE_CHARS = 144

_SYSTEM_PROMPT = """\
You are a grounded local operator assistant for simcoe.ai.
Use memory hints, retrieved context, and deterministic tool output as primary evidence when they are provided.
If the answer depends on information you were not given, say what is missing instead of inventing it.
Keep answers concise, actionable, and explicit about assumptions.
"""


def resolve_agent_shell_settings(cfg: dict) -> dict:
    agent_shell = cfg.get("agent_shell") if isinstance(cfg.get("agent_shell"), dict) else {}

    root_dir = str(agent_shell.get("root_dir") or "data/agent_shell")
    return {
        "enabled": bool(agent_shell.get("enabled", True)),
        "provider": str(agent_shell.get("provider") or "ollama"),
        "model": str(agent_shell.get("model") or "simcoe"),
        "root_dir": root_dir,
        "sessions_dir": str(agent_shell.get("sessions_dir") or f"{root_dir}/sessions"),
        "transcripts_dir": str(agent_shell.get("transcripts_dir") or f"{root_dir}/transcripts"),
        "max_turns": int(agent_shell.get("max_turns", 40) or 40),
        "temperature": float(agent_shell.get("temperature", 0.2) or 0.2),
        "max_output_tokens": int(agent_shell.get("max_output_tokens", 512) or 512),
        "history_turn_window": _normalized_session_history_turn_window(
            agent_shell.get("history_turn_window")
        ),
        "ollama_base_url": str(agent_shell.get("ollama_base_url") or "http://localhost:11434/v1"),
        "openai_api_key_env": str(agent_shell.get("openai_api_key_env") or "OPENAI_API_KEY"),
        "include_memory_in_text_routes": bool(
            agent_shell.get("include_memory_in_text_routes", False)
        ),
        "include_retrieval_in_text_routes": bool(
            agent_shell.get("include_retrieval_in_text_routes", False)
        ),
        "persist_context_sections": bool(agent_shell.get("persist_context_sections", True)),
    }


def resolve_agent_shell_system_prompt(cfg: dict) -> tuple[str, dict]:
    return resolve_configured_system_prompt(
        cfg,
        SYSTEM_PROMPT_SURFACE_AGENT_SHELL,
        _SYSTEM_PROMPT.rstrip("\n"),
    )


def _session_summary_path(settings: dict, session_id: str) -> Path:
    return Path(settings["sessions_dir"]) / f"{session_id}.json"


def _session_transcript_path(settings: dict, session_id: str) -> Path:
    return Path(settings["transcripts_dir"]) / f"{session_id}.jsonl"


def _normalized_session_skill_names(value: object) -> list[str]:
    if not isinstance(value, list):
        return []

    cleaned: list[str] = []
    seen: set[str] = set()
    for item in value:
        if not isinstance(item, str) or not item.strip():
            continue
        candidate = item.strip()
        if candidate in seen:
            continue
        cleaned.append(candidate)
        seen.add(candidate)
    return cleaned


def _normalized_session_history_summary_text(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    cleaned = value.strip()
    return cleaned or None


def _normalized_session_history_summary_turn_count(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        return 0
    return value


def _normalized_session_history_turn_window(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        return DEFAULT_SESSION_HISTORY_TURN_WINDOW
    return value


def _resolved_session_history_turn_window(
    settings: dict | None = None,
    session_summary: dict | None = None,
) -> int:
    if isinstance(session_summary, dict):
        value = session_summary.get("history_turn_window")
        if isinstance(value, int) and not isinstance(value, bool) and value > 0:
            return value
    if isinstance(settings, dict):
        value = settings.get("history_turn_window")
        if isinstance(value, int) and not isinstance(value, bool) and value > 0:
            return value
    return DEFAULT_SESSION_HISTORY_TURN_WINDOW


def _compact_session_history_text(value: object, *, max_chars: int) -> str | None:
    if not isinstance(value, str):
        return None
    cleaned = " ".join(value.strip().split())
    if not cleaned:
        return None
    if len(cleaned) <= max_chars:
        return cleaned
    return cleaned[: max_chars - 3].rstrip() + "..."


def _session_history_summary_line(turn: dict) -> str | None:
    prompt = _compact_session_history_text(
        turn.get("user", {}).get("prompt") if isinstance(turn.get("user"), dict) else None,
        max_chars=SESSION_HISTORY_SUMMARY_LINE_PROMPT_CHARS,
    )
    response = _compact_session_history_text(
        turn.get("assistant", {}).get("response")
        if isinstance(turn.get("assistant"), dict)
        else None,
        max_chars=SESSION_HISTORY_SUMMARY_LINE_RESPONSE_CHARS,
    )
    route = str(turn.get("route") or "unknown").strip() or "unknown"
    if prompt and response:
        return f"- [{route}] User: {prompt} | Assistant: {response}"
    if prompt:
        return f"- [{route}] User: {prompt}"
    if response:
        return f"- [{route}] Assistant: {response}"
    return None


def _build_session_history_summary(
    turns: list[dict],
    *,
    history_turn_window: int = DEFAULT_SESSION_HISTORY_TURN_WINDOW,
    max_chars: int = SESSION_HISTORY_SUMMARY_MAX_CHARS,
) -> tuple[str | None, int]:
    safe_window = max(1, history_turn_window)
    if len(turns) <= safe_window:
        return None, 0

    older_turns = turns[:-safe_window]
    selected_lines: list[str] = []
    selected_turn_count = 0
    for turn in reversed(older_turns):
        line = _session_history_summary_line(turn)
        if line is None:
            continue
        candidate_lines = list(reversed([line, *selected_lines]))
        candidate_text = "\n".join(candidate_lines)
        if len(candidate_text) > max_chars:
            break
        selected_lines.insert(0, line)
        selected_turn_count += 1

    if not selected_lines:
        return None, 0
    return "\n".join(selected_lines), selected_turn_count


def _apply_session_history_summary(summary: dict, turns: list[dict]) -> tuple[dict, bool]:
    normalized = copy.deepcopy(summary)
    updated = False
    history_turn_window = _resolved_session_history_turn_window(session_summary=normalized)
    if normalized.get("history_turn_window") != history_turn_window:
        normalized["history_turn_window"] = history_turn_window
        updated = True
    summary_text, summary_turn_count = _build_session_history_summary(
        turns,
        history_turn_window=history_turn_window,
    )
    normalized_summary_text = _normalized_session_history_summary_text(summary_text)
    normalized_summary_turn_count = _normalized_session_history_summary_turn_count(
        summary_turn_count
    )

    if normalized.get("history_summary_text") != normalized_summary_text:
        normalized["history_summary_text"] = normalized_summary_text
        updated = True
    if normalized.get("history_summary_turn_count") != normalized_summary_turn_count:
        normalized["history_summary_turn_count"] = normalized_summary_turn_count
        updated = True
    return normalized, updated


def _normalize_session_summary(summary: dict) -> tuple[dict, bool]:
    normalized = copy.deepcopy(summary)
    updated = False
    for field_name in ("pinned_skills", "next_turn_skills", "last_skill_names"):
        cleaned = _normalized_session_skill_names(normalized.get(field_name))
        if normalized.get(field_name) != cleaned:
            normalized[field_name] = cleaned
            updated = True
    history_summary_text = _normalized_session_history_summary_text(
        normalized.get("history_summary_text")
    )
    if normalized.get("history_summary_text") != history_summary_text:
        normalized["history_summary_text"] = history_summary_text
        updated = True
    history_summary_turn_count = _normalized_session_history_summary_turn_count(
        normalized.get("history_summary_turn_count")
    )
    if normalized.get("history_summary_turn_count") != history_summary_turn_count:
        normalized["history_summary_turn_count"] = history_summary_turn_count
        updated = True
    history_turn_window = _normalized_session_history_turn_window(
        normalized.get("history_turn_window")
    )
    if normalized.get("history_turn_window") != history_turn_window:
        normalized["history_turn_window"] = history_turn_window
        updated = True
    return normalized, updated


def persist_session_summary(settings: dict, session_summary: dict) -> dict:
    normalized_summary, _ = _normalize_session_summary(session_summary)
    write_json_file(
        str(_session_summary_path(settings, normalized_summary["session_id"])),
        normalized_summary,
    )
    return normalized_summary


def update_session_skill_selection(
    settings: dict,
    session_summary: dict,
    pinned_skill_names: list[str] | None,
    next_turn_skill_names: list[str] | None,
) -> dict:
    updated_summary = copy.deepcopy(session_summary)
    if pinned_skill_names is not None:
        updated_summary["pinned_skills"] = _normalized_session_skill_names(pinned_skill_names)
    if next_turn_skill_names is not None:
        updated_summary["next_turn_skills"] = _normalized_session_skill_names(next_turn_skill_names)
    updated_summary["updated_at"] = current_utc_timestamp()
    return persist_session_summary(settings, updated_summary)


def ensure_agent_shell_layout(settings: dict) -> None:
    Path(settings["root_dir"]).mkdir(parents=True, exist_ok=True)
    Path(settings["sessions_dir"]).mkdir(parents=True, exist_ok=True)
    Path(settings["transcripts_dir"]).mkdir(parents=True, exist_ok=True)


def initialize_session(
    settings: dict,
    *,
    config_path: str,
    system_prompt_metadata: dict,
    session_id: str | None = None,
) -> dict:
    ensure_agent_shell_layout(settings)

    if session_id:
        summary_path = _session_summary_path(settings, session_id)
        if summary_path.is_file():
            summary = read_json_file(str(summary_path))
            summary, summary_updated = _normalize_session_summary(summary)
            resolved_history_turn_window = _resolved_session_history_turn_window(
                settings,
                summary,
            )
            if summary.get("history_turn_window") != resolved_history_turn_window:
                summary["history_turn_window"] = resolved_history_turn_window
                summary_updated = True
            transcript_path = _session_transcript_path(settings, session_id)
            transcript_path.parent.mkdir(parents=True, exist_ok=True)
            transcript_path.touch(exist_ok=True)
            turns = read_session_turns(settings, session_id)
            summary, history_updated = _apply_session_history_summary(summary, turns)
            if summary_updated:
                persist_session_summary(settings, summary)
            elif history_updated:
                persist_session_summary(settings, summary)
            return summary

    resolved_session_id = session_id or f"agent-shell-{uuid.uuid4().hex[:12]}"
    created_at = current_utc_timestamp()
    transcript_path = _session_transcript_path(settings, resolved_session_id)
    transcript_path.parent.mkdir(parents=True, exist_ok=True)
    transcript_path.touch(exist_ok=True)

    summary = {
        "schema_version": SESSION_SCHEMA_VERSION,
        "session_id": resolved_session_id,
        "created_at": created_at,
        "updated_at": created_at,
        "config_path": os.path.abspath(config_path),
        "provider": settings["provider"],
        "model": settings["model"],
        "transcript_path": str(transcript_path.resolve()),
        "turn_count": 0,
        "route_counts": {},
        "last_turn_id": None,
        "last_route": None,
        "last_runtime_owner": None,
        "last_prompt": None,
        "pinned_skills": [],
        "next_turn_skills": [],
        "last_skill_names": [],
        "history_summary_text": None,
        "history_summary_turn_count": 0,
        "history_turn_window": _resolved_session_history_turn_window(settings),
        "system_prompt_metadata": copy.deepcopy(system_prompt_metadata),
    }
    write_json_file(str(_session_summary_path(settings, resolved_session_id)), summary)
    return summary


def read_session_turns(settings: dict, session_id: str) -> list[dict]:
    transcript_path = _session_transcript_path(settings, session_id)
    if not transcript_path.is_file():
        return []

    turns: list[dict] = []
    with transcript_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            turns.append(json.loads(stripped))
    return turns


def _history_messages_from_turns(
    turns: list[dict],
    history_turn_window: int,
    *,
    session_history_summary_text: str | None = None,
) -> list[dict]:
    messages: list[dict] = []
    if isinstance(session_history_summary_text, str) and session_history_summary_text.strip():
        messages.append(
            {
                "role": "system",
                "content": (
                    f"### Earlier Session Summary:\n{session_history_summary_text.strip()}"
                ),
            }
        )
    for turn in turns[-max(1, history_turn_window) :]:
        user_prompt = (
            turn.get("user", {}).get("prompt") if isinstance(turn.get("user"), dict) else None
        )
        assistant_response = (
            turn.get("assistant", {}).get("response")
            if isinstance(turn.get("assistant"), dict)
            else None
        )
        if isinstance(user_prompt, str) and user_prompt.strip():
            messages.append({"role": "user", "content": user_prompt})
        if isinstance(assistant_response, str) and assistant_response.strip():
            messages.append({"role": "assistant", "content": assistant_response})
    return messages


def build_session_history_messages(
    settings: dict, session_summary: dict, turns: list[dict]
) -> list[dict]:
    return _history_messages_from_turns(
        turns,
        _resolved_session_history_turn_window(settings, session_summary),
        session_history_summary_text=_normalized_session_history_summary_text(
            session_summary.get("history_summary_text")
        ),
    )


def _describe_session_history(summary: dict, turns: list[dict]) -> dict:
    total_turn_count = len(turns)
    history_turn_window = _resolved_session_history_turn_window(session_summary=summary)
    recent_turn_count = min(total_turn_count, history_turn_window)
    summary_turn_count = min(
        _normalized_session_history_summary_turn_count(summary.get("history_summary_turn_count")),
        max(0, total_turn_count - recent_turn_count),
    )
    summary_text = _normalized_session_history_summary_text(summary.get("history_summary_text"))
    history_messages = _history_messages_from_turns(
        turns,
        history_turn_window,
        session_history_summary_text=summary_text,
    )
    return {
        "recent_turn_window": history_turn_window,
        "total_turn_count": total_turn_count,
        "recent_turn_count": recent_turn_count,
        "summary_turn_count": summary_turn_count,
        "omitted_turn_count": max(0, total_turn_count - recent_turn_count - summary_turn_count),
        "has_summary": bool(summary_text),
        "summary_char_count": len(summary_text or ""),
        "message_count": len(history_messages),
    }


def build_instruction_prompt(instruction: str) -> str:
    return f"### Instruction:\n{instruction.strip()}\n\n### Response:"


def _provider_enabled_for_route(provider_name: str, route_name: str, settings: dict) -> bool:
    if route_name == ROUTE_RETRIEVAL:
        return provider_name in {CONTEXT_PROVIDER_MEMORY, CONTEXT_PROVIDER_RETRIEVAL}
    if route_name == ROUTE_TEXT:
        if provider_name == CONTEXT_PROVIDER_MEMORY:
            return bool(settings["include_memory_in_text_routes"])
        if provider_name == CONTEXT_PROVIDER_RETRIEVAL:
            return bool(settings["include_retrieval_in_text_routes"])
    return False


def collect_context_for_turn(
    cfg: dict,
    settings: dict,
    prompt: str,
    *,
    route_name: str,
    source: str | None = None,
    section: str | None = None,
    turn_index: int = 0,
    providers: list[dict] | None = None,
    provider_metadata: dict | None = None,
) -> tuple[list[tuple[str, str]], list[dict], dict]:
    if providers is None or provider_metadata is None:
        providers, provider_metadata = build_context_provider_registry(cfg)

    context_sections: list[tuple[str, str]] = []
    traces: list[dict] = []
    selected_provider_names: list[str] = []
    example = {
        "benchmark_id": f"agent_shell_turn_{turn_index}",
        "source": source,
        "section": section,
    }

    for provider in providers:
        provider_name = str(provider.get("name") or "").strip().lower()
        if not _provider_enabled_for_route(provider_name, route_name, settings):
            continue

        provider_result = provider["query_fn"](example, prompt, turn_index)
        provider_trace = copy.deepcopy(provider_result["trace"])
        traces.append(provider_trace)
        selected_provider_names.append(provider_name)
        if provider_result["context"].strip():
            context_sections.append((provider_result["section_title"], provider_result["context"]))

    metadata = {
        **copy.deepcopy(provider_metadata),
        "selected": selected_provider_names,
    }
    return context_sections, traces, metadata


def create_model_client(settings: dict):
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("openai package not installed. Run: pip install openai") from exc

    if settings["provider"] == "openai":
        api_key = os.environ.get(settings["openai_api_key_env"])
        if not api_key:
            raise RuntimeError(
                f"Environment variable '{settings['openai_api_key_env']}' is required for agent_shell.provider=openai"
            )
        return OpenAI(api_key=api_key)

    return OpenAI(base_url=settings["ollama_base_url"], api_key="ollama")


def run_chat_completion(settings: dict, messages: list[dict], client) -> str:
    response = client.chat.completions.create(
        model=settings["model"],
        messages=messages,
        temperature=float(settings["temperature"]),
        max_tokens=int(settings["max_output_tokens"]),
    )
    content = response.choices[0].message.content
    if not isinstance(content, str) or not content.strip():
        return "Model returned an empty response."
    return content.strip()


def build_completion_fn(settings: dict) -> Callable[[list[dict]], str]:
    client = None

    def complete(messages: list[dict]) -> str:
        nonlocal client
        if client is None:
            client = create_model_client(settings)
        return run_chat_completion(settings, messages, client)

    return complete


def execute_deterministic_tool_turn(
    cfg: dict,
    prompt: str,
    *,
    route_name: str,
    explicit_tool_name: str | None = None,
    config_path: str | None = None,
    source: str | None = None,
    section: str | None = None,
    attachments: list[str] | None = None,
    parent_task_id: str | None = None,
    delegation_briefing: str | None = None,
) -> dict:
    return execute_inferred_agent_tool(
        cfg,
        prompt,
        route_name=route_name,
        explicit_tool_name=explicit_tool_name,
        config_path=config_path,
        source=source,
        section=section,
        attachments=attachments,
        parent_task_id=parent_task_id,
        delegation_briefing=delegation_briefing,
    )


def run_agent_turn(
    cfg: dict,
    settings: dict,
    prompt: str,
    *,
    config_path: str | None = None,
    system_prompt: str,
    history_messages: list[dict] | None = None,
    source: str | None = None,
    section: str | None = None,
    attachments: list[str] | None = None,
    explicit_tool_name: str | None = None,
    parent_task_id: str | None = None,
    delegation_briefing: str | None = None,
    explicit_skill_names: list[str] | None = None,
    pinned_skill_names: list[str] | None = None,
    completion_fn: Callable[[list[dict]], str] | None = None,
    turn_index: int = 0,
    providers: list[dict] | None = None,
    provider_metadata: dict | None = None,
) -> dict:
    normalized_prompt = prompt.strip()
    turn_id = f"turn_{uuid.uuid4().hex[:12]}"
    generated_at = current_utc_timestamp()

    if turn_index >= int(settings["max_turns"]):
        error_message = f"Session limit of {settings['max_turns']} turns reached."
        return {
            "schema_version": TURN_SCHEMA_VERSION,
            "turn_id": turn_id,
            "turn_index": turn_index,
            "generated_at": generated_at,
            "route": None,
            "runtime_owner": None,
            "user": {
                "prompt": normalized_prompt,
                "source": source,
                "section": section,
                "attachments": list(attachments or []),
            },
            "assistant": {
                "response": error_message,
                "source": "error",
                "provider": None,
                "model": None,
            },
            "error": error_message,
            "route_decision": None,
            "context_sections": [],
            "provider_traces": [],
            "skills": [],
            "skill_prompt": None,
            "tool": None,
            "execution": {
                "schema_version": 1,
                "route": None,
                "context_providers": [],
                "deterministic_tool": None,
                "summary": summarize_execution_envelopes([]),
            },
        }

    route_decision: dict | None = None
    context_sections: list[tuple[str, str]] = []
    provider_traces: list[dict] = []
    matched_skills: list[dict] = []
    skill_prompt: str | None = None
    tool_result: dict | None = None
    prompt_with_context: str | None = None
    error: str | None = None

    try:
        route_decision = route_request(
            cfg,
            normalized_prompt,
            source=source,
            section=section,
            attachments=list(attachments or []),
            tool_name=explicit_tool_name,
        )
        route_name = route_decision["resolved_route"]

        if route_name == ROUTE_DETERMINISTIC_TOOL:
            tool_result = execute_deterministic_tool_turn(
                cfg,
                normalized_prompt,
                route_name=route_name,
                explicit_tool_name=explicit_tool_name,
                config_path=config_path,
                source=source,
                section=section,
                attachments=list(attachments or []),
                parent_task_id=parent_task_id,
                delegation_briefing=delegation_briefing,
            )
            assistant_response = tool_result["assistant_response"]
            assistant_source = "deterministic_tool"
            assistant_provider = None
            assistant_model = None
        elif route_name in SUPPORTED_MODEL_ROUTES:
            context_sections, provider_traces, _ = collect_context_for_turn(
                cfg,
                settings,
                normalized_prompt,
                route_name=route_name,
                source=source,
                section=section,
                turn_index=turn_index,
                providers=providers,
                provider_metadata=provider_metadata,
            )
            matched_skills = select_agent_skills(
                cfg,
                normalized_prompt,
                route_name=route_name,
                explicit_skill_names=explicit_skill_names,
                pinned_skill_names=pinned_skill_names,
            )
            instruction_prompt = build_instruction_prompt(normalized_prompt)
            skill_prompt = render_agent_skill_prompt(cfg, matched_skills)
            if skill_prompt:
                instruction_prompt = f"{skill_prompt}\n\n{instruction_prompt}"
            prompt_with_context = build_context_augmented_prompt(
                instruction_prompt,
                context_sections=context_sections,
            )
            complete = completion_fn or build_completion_fn(settings)
            messages = [{"role": "system", "content": system_prompt}]
            messages.extend(copy.deepcopy(history_messages or []))
            messages.append({"role": "user", "content": prompt_with_context})
            assistant_response = str(complete(messages) or "").strip()
            if not assistant_response:
                assistant_response = "Model returned an empty response."
            assistant_source = "model"
            assistant_provider = settings["provider"]
            assistant_model = settings["model"]
        else:
            error = f"Route '{route_name}' is not implemented in the local agent shell yet."
            assistant_response = error
            assistant_source = "error"
            assistant_provider = None
            assistant_model = None
    except Exception as exc:
        error = str(exc)
        assistant_response = f"Agent shell error: {error}"
        assistant_source = "error"
        assistant_provider = None
        assistant_model = None

    execution_envelopes: list[dict] = []
    route_envelope = None
    if isinstance(route_decision, dict) and isinstance(
        route_decision.get("execution_envelope"), dict
    ):
        route_envelope = copy.deepcopy(route_decision["execution_envelope"])
        execution_envelopes.append(route_envelope)
    provider_envelopes = [
        copy.deepcopy(trace["execution_envelope"])
        for trace in provider_traces
        if isinstance(trace, dict) and isinstance(trace.get("execution_envelope"), dict)
    ]
    execution_envelopes.extend(provider_envelopes)
    deterministic_tool_envelope = None
    if isinstance(tool_result, dict) and isinstance(tool_result.get("execution_envelope"), dict):
        deterministic_tool_envelope = copy.deepcopy(tool_result["execution_envelope"])
        execution_envelopes.append(deterministic_tool_envelope)

    serialized_context_sections = [
        {"title": title, "content": content} for title, content in context_sections
    ]

    return {
        "schema_version": TURN_SCHEMA_VERSION,
        "turn_id": turn_id,
        "turn_index": turn_index,
        "generated_at": generated_at,
        "route": route_decision.get("resolved_route") if isinstance(route_decision, dict) else None,
        "runtime_owner": route_decision.get("runtime_owner")
        if isinstance(route_decision, dict)
        else None,
        "user": {
            "prompt": normalized_prompt,
            "source": source,
            "section": section,
            "attachments": list(attachments or []),
        },
        "assistant": {
            "response": assistant_response,
            "source": assistant_source,
            "provider": assistant_provider,
            "model": assistant_model,
        },
        "error": error,
        "route_decision": copy.deepcopy(route_decision),
        "prompt_with_context": prompt_with_context,
        "context_sections": serialized_context_sections,
        "provider_traces": copy.deepcopy(provider_traces),
        "skills": [
            {
                "name": skill["name"],
                "title": skill["title"],
                "summary": skill["summary"],
                "path": skill["path"],
                "relative_path": skill["relative_path"],
                "match_score": skill["match_score"],
                "matched_terms": copy.deepcopy(skill["matched_terms"]),
                "selection_sources": copy.deepcopy(skill["selection_sources"]),
            }
            for skill in matched_skills
        ],
        "skill_prompt": skill_prompt,
        "tool": (
            {
                "name": tool_result["tool_name"],
                "request": copy.deepcopy(tool_result["request"]),
                "response": copy.deepcopy(tool_result["response"]),
            }
            if isinstance(tool_result, dict)
            else None
        ),
        "execution": {
            "schema_version": 1,
            "route": route_envelope,
            "context_providers": provider_envelopes,
            "deterministic_tool": deterministic_tool_envelope,
            "summary": summarize_execution_envelopes(execution_envelopes),
        },
    }


def record_turn(
    settings: dict,
    session_summary: dict,
    turn_payload: dict,
    *,
    system_prompt_metadata: dict,
    clear_next_turn_skills: bool = False,
) -> dict:
    transcript_path = _session_transcript_path(settings, session_summary["session_id"])
    transcript_path.parent.mkdir(parents=True, exist_ok=True)

    persisted_turn = copy.deepcopy(turn_payload)
    if not settings["persist_context_sections"]:
        persisted_turn["context_sections"] = []
        persisted_turn["prompt_with_context"] = None

    with transcript_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(persisted_turn, sort_keys=True) + "\n")

    updated_summary = copy.deepcopy(session_summary)
    updated_summary["updated_at"] = current_utc_timestamp()
    updated_summary["turn_count"] = int(updated_summary.get("turn_count", 0)) + 1
    updated_summary["last_turn_id"] = turn_payload.get("turn_id")
    updated_summary["last_route"] = turn_payload.get("route")
    updated_summary["last_runtime_owner"] = turn_payload.get("runtime_owner")
    updated_summary["last_prompt"] = turn_payload.get("user", {}).get("prompt")
    updated_summary["last_skill_names"] = [
        skill.get("name")
        for skill in turn_payload.get("skills", [])
        if isinstance(skill, dict) and isinstance(skill.get("name"), str)
    ]
    updated_summary["system_prompt_metadata"] = copy.deepcopy(system_prompt_metadata)
    updated_summary["pinned_skills"] = _normalized_session_skill_names(
        updated_summary.get("pinned_skills")
    )
    updated_summary["history_turn_window"] = _resolved_session_history_turn_window(settings)
    if clear_next_turn_skills:
        updated_summary["next_turn_skills"] = []
    else:
        updated_summary["next_turn_skills"] = _normalized_session_skill_names(
            updated_summary.get("next_turn_skills")
        )

    route_counts = dict(updated_summary.get("route_counts") or {})
    route_name = turn_payload.get("route")
    if isinstance(route_name, str) and route_name.strip():
        route_counts[route_name] = int(route_counts.get(route_name, 0)) + 1
    updated_summary["route_counts"] = route_counts

    turns = read_session_turns(settings, session_summary["session_id"])
    updated_summary, _ = _apply_session_history_summary(updated_summary, turns)

    write_json_file(
        str(_session_summary_path(settings, session_summary["session_id"])),
        updated_summary,
    )
    return updated_summary


def describe_agent_shell_session(settings: dict, session_id: str, *, tail: int = 5) -> dict:
    summary_path = _session_summary_path(settings, session_id)
    if not summary_path.is_file():
        raise ValueError(f"Session not found: {session_id}")

    summary = read_json_file(str(summary_path))
    turns = read_session_turns(settings, session_id)
    summary, _ = _apply_session_history_summary(summary, turns)
    history = _describe_session_history(summary, turns)
    recent_turns = []
    for turn in turns[-max(0, tail) :]:
        recent_turns.append(
            {
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
                "error": turn.get("error"),
            }
        )

    return {
        "session": summary,
        "history": history,
        "recent_turns": recent_turns,
    }


def handle_shell_command(
    cfg: dict,
    settings: dict,
    session_summary: dict,
    raw_prompt: str,
) -> dict | None:
    return execute_agent_command(
        cfg,
        settings,
        session_summary,
        raw_prompt,
        describe_session_fn=describe_agent_shell_session,
        describe_context_providers_fn=describe_context_providers,
        update_session_skills_fn=update_session_skill_selection,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Start or inspect the local simcoe.ai agent shell."
    )
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument(
        "--session-id",
        help="Resume an existing session or pin a specific session id for a new one.",
    )
    parser.add_argument("--prompt", help="Run a single prompt non-interactively and exit.")
    parser.add_argument("--source", help="Optional source hint for routing and retrieval.")
    parser.add_argument("--section", help="Optional section hint for routing and retrieval.")
    parser.add_argument(
        "--attachment",
        action="append",
        default=[],
        help="Optional attachment path. Can be repeated.",
    )
    parser.add_argument(
        "--tool-name",
        help="Optional explicit deterministic tool name override.",
    )
    parser.add_argument(
        "--skill",
        action="append",
        default=[],
        help="Optional explicit local skill id or alias. Can be repeated for one-shot prompts.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the full turn payload as JSON for a non-interactive prompt.",
    )
    parser.add_argument(
        "--show-session",
        action="store_true",
        help="Print the saved session summary and recent turns, then exit.",
    )
    parser.add_argument(
        "--tail",
        type=int,
        default=5,
        help="Number of recent turns to include with --show-session.",
    )
    args = parser.parse_args()

    if args.show_session and not args.session_id:
        parser.error("--show-session requires --session-id")
    if args.tail < 0:
        parser.error("--tail must be zero or greater")
    if args.show_session and args.prompt:
        parser.error("--show-session cannot be combined with --prompt")

    return args


def main() -> int:
    args = parse_args()
    cfg = load_config(args.config)
    validate_architecture_config(cfg)
    validate_routing_config(cfg)
    validate_retrieval_config(cfg)
    validate_deterministic_tools_config(cfg)
    validate_orchestration_config(cfg)
    validate_system_prompts_config(cfg)
    validate_agent_shell_config(cfg)

    settings = resolve_agent_shell_settings(cfg)
    if not settings["enabled"]:
        print("❌  agent_shell.enabled is false in the selected config")
        return 1

    system_prompt, system_prompt_metadata = resolve_agent_shell_system_prompt(cfg)

    if args.show_session:
        try:
            payload = describe_agent_shell_session(
                settings,
                args.session_id,
                tail=args.tail,
            )
        except ValueError as exc:
            print(f"❌  {exc}")
            return 1
        print(json.dumps(payload, indent=2, sort_keys=False))
        return 0

    session_summary = initialize_session(
        settings,
        config_path=args.config,
        system_prompt_metadata=system_prompt_metadata,
        session_id=args.session_id,
    )
    providers, provider_metadata = build_context_provider_registry(cfg)
    complete = build_completion_fn(settings)

    if args.prompt:
        pending_next_turn_skills = _normalized_session_skill_names(
            session_summary.get("next_turn_skills")
        )
        session_turns = read_session_turns(settings, session_summary["session_id"])
        session_summary, _ = _apply_session_history_summary(session_summary, session_turns)
        history_messages = build_session_history_messages(
            settings,
            session_summary,
            session_turns,
        )
        turn_payload = run_agent_turn(
            cfg,
            settings,
            args.prompt,
            config_path=str(session_summary.get("config_path") or args.config),
            system_prompt=system_prompt,
            history_messages=history_messages,
            source=args.source,
            section=args.section,
            attachments=args.attachment,
            explicit_tool_name=args.tool_name,
            explicit_skill_names=list(args.skill) + pending_next_turn_skills,
            pinned_skill_names=_normalized_session_skill_names(
                session_summary.get("pinned_skills")
            ),
            completion_fn=complete,
            turn_index=int(session_summary.get("turn_count", 0)),
            providers=providers,
            provider_metadata=provider_metadata,
        )
        record_turn(
            settings,
            session_summary,
            turn_payload,
            system_prompt_metadata=system_prompt_metadata,
            clear_next_turn_skills=bool(pending_next_turn_skills),
        )

        if args.json:
            print(json.dumps(turn_payload, indent=2, sort_keys=False))
        else:
            print(turn_payload["assistant"]["response"])
        return 1 if turn_payload.get("error") else 0

    if int(session_summary.get("turn_count", 0)) >= int(settings["max_turns"]):
        print(
            f"Session '{session_summary['session_id']}' already reached the configured max_turns ({settings['max_turns']})."
        )
        return 1

    print(
        f"simcoe.ai agent shell session {session_summary['session_id']}\n"
        "Type /help for commands. Type /exit to quit."
    )
    while int(session_summary.get("turn_count", 0)) < int(settings["max_turns"]):
        try:
            prompt = input(f"agent[{session_summary['session_id'][:8]}]> ").strip()
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print("\nInterrupted. Use /exit to leave the shell.")
            continue

        if not prompt:
            continue

        command_result = handle_shell_command(cfg, settings, session_summary, prompt)
        if command_result is not None:
            if isinstance(command_result.get("session_summary"), dict):
                session_summary = command_result["session_summary"]
            print(command_result["response"])
            if command_result.get("exit"):
                break
            continue

        pending_next_turn_skills = _normalized_session_skill_names(
            session_summary.get("next_turn_skills")
        )
        session_turns = read_session_turns(settings, session_summary["session_id"])
        session_summary, _ = _apply_session_history_summary(session_summary, session_turns)
        history_messages = build_session_history_messages(
            settings,
            session_summary,
            session_turns,
        )
        turn_payload = run_agent_turn(
            cfg,
            settings,
            prompt,
            config_path=str(session_summary.get("config_path") or args.config),
            system_prompt=system_prompt,
            history_messages=history_messages,
            explicit_skill_names=pending_next_turn_skills,
            pinned_skill_names=_normalized_session_skill_names(
                session_summary.get("pinned_skills")
            ),
            completion_fn=complete,
            turn_index=int(session_summary.get("turn_count", 0)),
            providers=providers,
            provider_metadata=provider_metadata,
        )
        session_summary = record_turn(
            settings,
            session_summary,
            turn_payload,
            system_prompt_metadata=system_prompt_metadata,
            clear_next_turn_skills=bool(pending_next_turn_skills),
        )
        print(turn_payload["assistant"]["response"])

    if int(session_summary.get("turn_count", 0)) >= int(settings["max_turns"]):
        print(f"Session limit reached ({settings['max_turns']} turns).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
