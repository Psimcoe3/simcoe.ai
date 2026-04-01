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
import shlex
from typing import Callable
import uuid

from dotenv import load_dotenv

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
from deterministic_tool_utils import build_tool_error, build_tool_request
from estimate_lookup import (
    TOOL_NAME as ESTIMATE_LOOKUP_TOOL_NAME,
    run_estimate_lookup_request,
)
from hook_runtime import apply_hook_stage
from manifest_utils import current_utc_timestamp, read_json_file, write_json_file
from orchestration_inspect import describe_context_providers
from prompt_templates import (
    SYSTEM_PROMPT_SURFACE_AGENT_SHELL,
    resolve_configured_system_prompt,
)
from request_router import route_request
from retrieval_utils import build_context_augmented_prompt
from revit_entity_lookup import (
    TOOL_NAME as REVIT_ENTITY_LOOKUP_TOOL_NAME,
    run_revit_entity_lookup_request,
)
from runtime_contracts import (
    CONTEXT_PROVIDER_MEMORY,
    CONTEXT_PROVIDER_RETRIEVAL,
    EXECUTION_STATUS_DENIED,
    EXECUTION_STATUS_FAILED,
    EXECUTION_STATUS_SUCCEEDED,
    EXECUTION_SUBJECT_DETERMINISTIC_TOOL,
    HOOK_STAGE_POST_DETERMINISTIC_TOOL,
    HOOK_STAGE_PRE_DETERMINISTIC_TOOL,
    ROUTE_DETERMINISTIC_TOOL,
    ROUTE_RETRIEVAL,
    ROUTE_TEXT,
    build_execution_envelope,
    summarize_execution_envelopes,
)
from workflow_registry import WorkflowRegistryError, get_workflow, list_workflows


load_dotenv()

SESSION_SCHEMA_VERSION = 1
TURN_SCHEMA_VERSION = 1
SUPPORTED_MODEL_ROUTES = {ROUTE_TEXT, ROUTE_RETRIEVAL}
SUPPORTED_TOOL_NAMES = {ESTIMATE_LOOKUP_TOOL_NAME, REVIT_ENTITY_LOOKUP_TOOL_NAME}

_SYSTEM_PROMPT = """\
You are a grounded local operator assistant for simcoe.ai.
Use memory hints, retrieved context, and deterministic tool output as primary evidence when they are provided.
If the answer depends on information you were not given, say what is missing instead of inventing it.
Keep answers concise, actionable, and explicit about assumptions.
"""

HELP_TEXT = """Available commands:
/help
/exit
/quit
/session
/route <instruction>
/providers
/workflow list
/workflow show <name>

Enter a normal prompt to run the routed shell flow.
Use --session-id from the CLI to resume a saved session.
""".strip()


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
            transcript_path = _session_transcript_path(settings, session_id)
            transcript_path.parent.mkdir(parents=True, exist_ok=True)
            transcript_path.touch(exist_ok=True)
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


def _history_messages_from_turns(turns: list[dict], history_turn_window: int) -> list[dict]:
    messages: list[dict] = []
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


def _infer_deterministic_tool_name(prompt: str, explicit_tool_name: str | None = None) -> str:
    if explicit_tool_name in SUPPORTED_TOOL_NAMES:
        return str(explicit_tool_name)

    normalized_prompt = prompt.lower()
    revit_markers = ("revit", "family type", "family and type", "subcategory")
    if any(marker in normalized_prompt for marker in revit_markers):
        return REVIT_ENTITY_LOOKUP_TOOL_NAME
    return ESTIMATE_LOOKUP_TOOL_NAME


def render_deterministic_tool_response(response: dict) -> str:
    tool_name = str(response.get("tool_name") or "deterministic_tool")
    if response.get("response_type") == "error":
        message = response.get("error", {}).get("message") or "unknown error"
        return f"{tool_name} failed: {message}"

    results = response.get("results") if isinstance(response.get("results"), list) else []
    lines = [f"{tool_name} returned {len(results)} result(s)."]
    for index, result in enumerate(results[:3], start=1):
        primary_label = (
            result.get("description")
            or result.get("family_and_type")
            or result.get("family_name")
            or result.get("lookup_key")
            or result.get("record_id")
            or "result"
        )
        details: list[str] = []
        if result.get("manufacturer"):
            details.append(str(result["manufacturer"]))
        if result.get("part_number"):
            details.append(f"part={result['part_number']}")
        estimate = result.get("estimate")
        if isinstance(estimate, dict) and estimate.get("installed_total") is not None:
            details.append(f"installed_total={estimate['installed_total']}")
        quantity_rollup = result.get("quantity_rollup")
        if (
            isinstance(quantity_rollup, dict)
            and quantity_rollup.get("supported")
            and isinstance(quantity_rollup.get("totals"), dict)
            and quantity_rollup["totals"].get("installed_total") is not None
        ):
            details.append(f"rolled_installed_total={quantity_rollup['totals']['installed_total']}")

        line = f"{index}. {primary_label}"
        if details:
            line += " — " + ", ".join(details)
        lines.append(line)

    warnings = response.get("warnings") if isinstance(response.get("warnings"), list) else []
    if warnings:
        lines.append("Warnings: " + "; ".join(str(item) for item in warnings if str(item).strip()))
    return "\n".join(lines)


def execute_deterministic_tool_turn(
    cfg: dict,
    prompt: str,
    *,
    route_name: str,
    explicit_tool_name: str | None = None,
) -> dict:
    tool_name = _infer_deterministic_tool_name(prompt, explicit_tool_name=explicit_tool_name)
    request = build_tool_request(tool_name, query=prompt)

    pre_hook = apply_hook_stage(
        cfg,
        HOOK_STAGE_PRE_DETERMINISTIC_TOOL,
        {
            "route": route_name,
            "tool_name": tool_name,
            "request": copy.deepcopy(request),
        },
    )
    hook_events = list(pre_hook["events"])
    hook_annotations = dict(pre_hook["annotations"])

    if pre_hook["denied"]:
        denial_message = pre_hook["deny_reason"] or "Deterministic tool denied by hook"
        response = build_tool_error(
            tool_name, request=request, message=denial_message, code="denied"
        )
        execution_envelope = build_execution_envelope(
            EXECUTION_SUBJECT_DETERMINISTIC_TOOL,
            tool_name,
            EXECUTION_STATUS_DENIED,
            owner="geometry_rules",
            details={
                "request_id": request.get("request_id"),
                "response_type": response.get("response_type"),
                "result_count": 0,
            },
            hook_annotations=hook_annotations,
            hook_events=hook_events,
        )
        return {
            "tool_name": tool_name,
            "request": request,
            "response": response,
            "assistant_response": render_deterministic_tool_response(response),
            "execution_envelope": execution_envelope,
        }

    hook_payload = pre_hook["payload"]
    if isinstance(hook_payload.get("tool_name"), str):
        tool_name = hook_payload["tool_name"]
    if isinstance(hook_payload.get("request"), dict):
        request = hook_payload["request"]

    try:
        if tool_name == ESTIMATE_LOOKUP_TOOL_NAME:
            response = run_estimate_lookup_request(cfg, request)
        elif tool_name == REVIT_ENTITY_LOOKUP_TOOL_NAME:
            response = run_revit_entity_lookup_request(cfg, request)
        else:
            raise ValueError(f"Unsupported deterministic tool: {tool_name}")

        post_hook = apply_hook_stage(
            cfg,
            HOOK_STAGE_POST_DETERMINISTIC_TOOL,
            {
                "route": route_name,
                "tool_name": tool_name,
                "request": copy.deepcopy(request),
                "response": copy.deepcopy(response),
            },
        )
        hook_events.extend(post_hook["events"])
        hook_annotations = dict(post_hook["annotations"])
        if post_hook["denied"]:
            denial_message = post_hook["deny_reason"] or "Deterministic tool denied by hook"
            response = build_tool_error(
                tool_name, request=request, message=denial_message, code="denied"
            )
            status = EXECUTION_STATUS_DENIED
        else:
            tool_payload = post_hook["payload"]
            if isinstance(tool_payload.get("tool_name"), str):
                tool_name = tool_payload["tool_name"]
            if isinstance(tool_payload.get("request"), dict):
                request = tool_payload["request"]
            if isinstance(tool_payload.get("response"), dict):
                response = tool_payload["response"]
            status = (
                EXECUTION_STATUS_FAILED
                if response.get("response_type") == "error"
                else EXECUTION_STATUS_SUCCEEDED
            )
    except Exception as exc:
        response = build_tool_error(
            tool_name,
            request=request,
            message=str(exc),
            code="tool_execution_failed",
        )
        status = EXECUTION_STATUS_FAILED

    execution_envelope = build_execution_envelope(
        EXECUTION_SUBJECT_DETERMINISTIC_TOOL,
        tool_name,
        status,
        owner=str(response.get("runtime_owner") or "geometry_rules"),
        details={
            "request_id": request.get("request_id"),
            "response_type": response.get("response_type"),
            "result_count": int(response.get("result_count", 0) or 0),
        },
        hook_annotations=hook_annotations,
        hook_events=hook_events,
    )
    return {
        "tool_name": tool_name,
        "request": request,
        "response": response,
        "assistant_response": render_deterministic_tool_response(response),
        "execution_envelope": execution_envelope,
    }


def run_agent_turn(
    cfg: dict,
    settings: dict,
    prompt: str,
    *,
    system_prompt: str,
    history_messages: list[dict] | None = None,
    source: str | None = None,
    section: str | None = None,
    attachments: list[str] | None = None,
    explicit_tool_name: str | None = None,
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
            prompt_with_context = build_context_augmented_prompt(
                build_instruction_prompt(normalized_prompt),
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
    updated_summary["system_prompt_metadata"] = copy.deepcopy(system_prompt_metadata)

    route_counts = dict(updated_summary.get("route_counts") or {})
    route_name = turn_payload.get("route")
    if isinstance(route_name, str) and route_name.strip():
        route_counts[route_name] = int(route_counts.get(route_name, 0)) + 1
    updated_summary["route_counts"] = route_counts

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
                "error": turn.get("error"),
            }
        )

    return {
        "session": summary,
        "recent_turns": recent_turns,
    }


def handle_shell_command(
    cfg: dict,
    settings: dict,
    session_summary: dict,
    raw_prompt: str,
) -> dict | None:
    if not raw_prompt.startswith("/"):
        return None

    try:
        parts = shlex.split(raw_prompt)
    except ValueError as exc:
        return {"exit": False, "response": f"Command parse error: {exc}"}

    if not parts:
        return {"exit": False, "response": HELP_TEXT}

    command = parts[0].lower()
    if command in {"/exit", "/quit"}:
        return {"exit": True, "response": "Exiting agent shell."}
    if command == "/help":
        return {"exit": False, "response": HELP_TEXT}
    if command == "/session":
        payload = describe_agent_shell_session(settings, session_summary["session_id"], tail=3)
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "/providers":
        payload = describe_context_providers(cfg)
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "/route":
        if len(parts) < 2:
            return {"exit": False, "response": "Usage: /route <instruction>"}
        instruction = raw_prompt.split(None, 1)[1]
        try:
            payload = route_request(cfg, instruction)
        except ValueError as exc:
            return {"exit": False, "response": f"Routing error: {exc}"}
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}
    if command == "/workflow":
        if len(parts) < 2:
            return {"exit": False, "response": "Usage: /workflow list | /workflow show <name>"}
        subcommand = parts[1].lower()
        try:
            if subcommand == "list":
                payload = list_workflows(cfg)
            elif subcommand == "show" and len(parts) >= 3:
                payload = get_workflow(cfg, parts[2])
            else:
                return {
                    "exit": False,
                    "response": "Usage: /workflow list | /workflow show <name>",
                }
        except WorkflowRegistryError as exc:
            return {"exit": False, "response": str(exc)}
        return {"exit": False, "response": json.dumps(payload, indent=2, sort_keys=False)}

    return {"exit": False, "response": f"Unknown command '{command}'. Use /help."}


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
        history_messages = _history_messages_from_turns(
            read_session_turns(settings, session_summary["session_id"]),
            int(settings["max_turns"]),
        )
        turn_payload = run_agent_turn(
            cfg,
            settings,
            args.prompt,
            system_prompt=system_prompt,
            history_messages=history_messages,
            source=args.source,
            section=args.section,
            attachments=args.attachment,
            explicit_tool_name=args.tool_name,
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
            print(command_result["response"])
            if command_result.get("exit"):
                break
            continue

        history_messages = _history_messages_from_turns(
            read_session_turns(settings, session_summary["session_id"]),
            int(settings["max_turns"]),
        )
        turn_payload = run_agent_turn(
            cfg,
            settings,
            prompt,
            system_prompt=system_prompt,
            history_messages=history_messages,
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
        )
        print(turn_payload["assistant"]["response"])

    if int(session_summary.get("turn_count", 0)) >= int(settings["max_turns"]):
        print(f"Session limit reached ({settings['max_turns']} turns).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
