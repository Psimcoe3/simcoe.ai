"""
scripts/evaluate.py
───────────────────
Post-training evaluation pipeline.

Runs inference on the held-out validation set and scores outputs using:
  1.  ROUGE-1 / ROUGE-2 / ROUGE-L  (standard automatic metrics)
  2.  Exact match  (case-insensitive string equality after normalisation)
  3.  LLM-as-judge  (stub — enable by setting evaluation.judge_model in config.yaml)

Results are written to evals/results.json.

Usage:
    python scripts/evaluate.py [--config config.yaml]

Prerequisites:
    • A merged 16-bit model must exist at models/merged_16bit/
      (or update evaluation to point at the adapter directory).
    • Processed validation data must exist at data/processed/valid/.
"""

import argparse
import copy
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import re
import shutil
import subprocess
import string
import time

try:
    import torch
except ImportError:
    torch = None

from config_validation import load_config, validate_evaluate_config
from datasets import load_from_disk
from deterministic_tool_utils import build_tool_request
from estimate_lookup import TOOL_NAME as ESTIMATE_LOOKUP_TOOL_NAME, run_estimate_lookup_request
from manifest_utils import current_utc_timestamp, read_json_file, write_json_file
import requests
from revit_entity_lookup import TOOL_NAME as REVIT_ENTITY_LOOKUP_TOOL_NAME, run_revit_entity_lookup_request
from retrieval_utils import (
    build_retrieval_augmented_prompt,
    extract_instruction_text,
    format_retrieved_context,
    load_jsonl,
    retrieve_documents,
)
from runtime_contracts import (
    ROUTE_DETERMINISTIC_TOOL,
    ROUTE_MIXED,
    ROUTE_RETRIEVAL,
    ROUTE_TEXT,
    validate_route_contract,
)
from tokenizer_utils import load_tokenizer_with_compat
from transformers import AutoModelForCausalLM, GenerationConfig, pipeline

try:
    from rouge_score import rouge_scorer
    _scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
except ImportError:
    _scorer = None


SUPPORTED_TEXT_GENERATION_ROUTES = {ROUTE_TEXT, ROUTE_RETRIEVAL}
SUPPORTED_EVALUATION_ROUTES = SUPPORTED_TEXT_GENERATION_ROUTES | {ROUTE_DETERMINISTIC_TOOL}
UNIMPLEMENTED_EVALUATION_ROUTES = {ROUTE_MIXED, "drawing_sheet"}


# ── Text normalisation ────────────────────────────────────────────────────────

def _normalise(text: str) -> str:
    """Lower-case, strip punctuation and extra whitespace."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ── Inference ─────────────────────────────────────────────────────────────────

def extract_prompt(text: str) -> str:
    """
    Strip the expected '### Response:' section from a formatted example so
    we can feed only the instruction part to the model and evaluate its output.
    """
    # Split at the response marker and return everything before it
    parts = text.split("### Response:")
    if len(parts) >= 2:
        return parts[0] + "### Response:"
    return text


def extract_reference(text: str) -> str:
    """Return the reference response (everything after '### Response:')."""
    parts = text.split("### Response:")
    if len(parts) >= 2:
        return parts[1].strip()
    return ""


def build_prompt(instruction: str, context: str | None = None) -> str:
    instruction = instruction.strip()
    context = (context or "").strip()
    if context:
        return (
            f"### Instruction:\n{instruction}\n\n"
            f"### Input:\n{context}\n\n"
            f"### Response:"
        )
    return f"### Instruction:\n{instruction}\n\n### Response:"


def build_example_from_text(text: str) -> dict:
    return {
        "prompt": extract_prompt(text),
        "reference": extract_reference(text),
        "category": None,
        "benchmark_id": None,
        "source": None,
        "section": None,
        "route": "text",
        "runtime_owner": "text",
        "tool_name": None,
        "tool_request": None,
        "tool_expectation": None,
    }


def build_example_from_benchmark_row(row: dict, multimodal_enabled: bool) -> dict:
    instruction = str(row.get("instruction", "")).strip()
    context = row.get("input")
    reference = str(row.get("response") or row.get("output") or "").strip()
    benchmark_id = str(row.get("benchmark_id") or "benchmark_row").strip() or "benchmark_row"
    try:
        route, runtime_owner = validate_route_contract(
            row.get("route") or ROUTE_TEXT,
            row.get("runtime_owner"),
            multimodal_enabled=multimodal_enabled,
            route_label=f"benchmark[{benchmark_id}].route",
            runtime_owner_label=f"benchmark[{benchmark_id}].runtime_owner",
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    return {
        "prompt": build_prompt(instruction, context if isinstance(context, str) else None),
        "reference": reference,
        "category": row.get("category"),
        "benchmark_id": row.get("benchmark_id"),
        "source": row.get("source"),
        "section": row.get("section"),
        "route": route,
        "runtime_owner": runtime_owner,
        "tool_name": row.get("tool_name"),
        "tool_request": row.get("tool_request") if isinstance(row.get("tool_request"), dict) else None,
        "tool_expectation": row.get("tool_expectation") if isinstance(row.get("tool_expectation"), dict) else None,
    }


def load_evaluation_examples(cfg: dict, settings: dict) -> tuple[list[dict], dict]:
    benchmark_path = cfg["evaluation"].get("golden_benchmark_path")
    architecture = cfg.get("architecture") if isinstance(cfg.get("architecture"), dict) else {}
    multimodal_enabled = bool(architecture.get("multimodal_runtime_enabled", False))
    if settings["mode"] != "quick" and benchmark_path:
        benchmark_rows = load_jsonl(benchmark_path)
        example_count = min(settings["num_examples"], len(benchmark_rows))
        selected_rows = benchmark_rows[:example_count]
        examples = [build_example_from_benchmark_row(row, multimodal_enabled) for row in selected_rows]
        return examples, {
            "kind": "golden_benchmark",
            "path": os.path.abspath(benchmark_path),
            "available_rows": len(benchmark_rows),
            "selected_rows": example_count,
        }

    valid_dir = os.path.join(cfg["data"]["processed_dir"], "valid")
    valid_ds = load_from_disk(valid_dir)
    example_count = min(settings["num_examples"], len(valid_ds))
    rows = list(valid_ds.select(range(example_count)))
    examples = [build_example_from_text(row["text"]) for row in rows]
    return examples, {
        "kind": "processed_validation",
        "path": os.path.abspath(valid_dir),
        "available_rows": len(valid_ds),
        "selected_rows": example_count,
    }


def prepare_prompts_with_retrieval(examples: list[dict], cfg: dict, settings: dict) -> tuple[list[str], dict]:
    retrieval_cfg = cfg.get("retrieval") if isinstance(cfg.get("retrieval"), dict) else None
    route_forces_retrieval = any(_route_name(example) == ROUTE_RETRIEVAL for example in examples)
    requested_retrieval = bool(settings["use_retrieval"] or route_forces_retrieval)

    if not retrieval_cfg:
        if requested_retrieval:
            raise SystemExit("Evaluation examples require retrieval, but config.retrieval is not defined")
        return [example["prompt"] for example in examples], {"enabled": False, "used": False}

    retrieval_enabled = bool(retrieval_cfg.get("enabled", False))
    if not retrieval_enabled:
        if requested_retrieval:
            raise SystemExit("Evaluation examples require retrieval, but retrieval.enabled is false")
        return [example["prompt"] for example in examples], {"enabled": False, "used": False}

    if not requested_retrieval:
        return [example["prompt"] for example in examples], {
            "enabled": True,
            "used": False,
            "forced_by_routes": False,
        }

    corpus_path = retrieval_cfg["corpus_path"]
    corpus = load_jsonl(corpus_path)
    top_k = int(retrieval_cfg.get("top_k", 3))
    max_context_chars = int(retrieval_cfg.get("max_context_chars", 1600))
    min_score = float(retrieval_cfg.get("min_score", 1.0))

    prompts: list[str] = []
    traces: list[dict] = []
    retrieval_usage_count = 0
    for example in examples:
        query = extract_instruction_text(example["prompt"])
        should_retrieve = bool(settings["use_retrieval"] or _route_name(example) == ROUTE_RETRIEVAL)
        trace = {
            "route": _route_name(example),
            "query": query,
            "preferred_source": example.get("source"),
            "preferred_section": example.get("section"),
            "used": should_retrieve,
            "results": [],
        }

        if should_retrieve:
            retrieved = retrieve_documents(
                query,
                corpus,
                top_k=top_k,
                min_score=min_score,
                preferred_source=example.get("source"),
                preferred_section=example.get("section"),
            )
            retrieved_context = format_retrieved_context(retrieved, max_context_chars=max_context_chars)
            prompts.append(build_retrieval_augmented_prompt(example["prompt"], retrieved_context))
            trace["results"] = [
                {
                    "id": item.get("id"),
                    "source": item.get("source"),
                    "section": item.get("section"),
                    "score": item.get("score"),
                }
                for item in retrieved
            ]
            retrieval_usage_count += 1
        else:
            prompts.append(example["prompt"])

        traces.append(trace)

    return prompts, {
        "enabled": True,
        "used": retrieval_usage_count > 0,
        "forced_by_routes": route_forces_retrieval,
        "corpus_path": os.path.abspath(corpus_path),
        "corpus_size": len(corpus),
        "top_k": top_k,
        "max_context_chars": max_context_chars,
        "min_score": min_score,
        "retrieval_example_count": retrieval_usage_count,
        "per_example": traces,
    }


def _chunked(items: list[str], chunk_size: int):
    for start in range(0, len(items), chunk_size):
        yield start, items[start:start + chunk_size]


def _clear_cuda_cache() -> None:
    if torch is not None and torch.cuda.is_available():
        torch.cuda.empty_cache()


def _extract_prediction(generated_text: str) -> str:
    parts = generated_text.split("### Response:")
    return parts[-1].strip() if len(parts) >= 2 else generated_text.strip()


def _is_recoverable_cuda_error(exc: RuntimeError) -> bool:
    message = str(exc).lower()
    return any(
        marker in message
        for marker in (
            "out of memory",
            "cuda error",
            "cublas",
            "device-side assert",
        )
    )


def _resolve_int_setting(value: object, default: int) -> int:
    if isinstance(value, int) and value > 0:
        return value
    return default


def _resolve_float_setting(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _round_metric(value: float | None) -> float | None:
    if value is None:
        return None
    return round(float(value), 4)


def _route_name(example: dict) -> str:
    route = example.get("route")
    if isinstance(route, str) and route.strip():
        return route.strip().lower()
    return "text"


def _is_deterministic_tool_example(example: dict) -> bool:
    return _route_name(example) == ROUTE_DETERMINISTIC_TOOL or bool(example.get("tool_name"))


def _is_grounded_example(example: dict) -> bool:
    if _is_deterministic_tool_example(example):
        return False
    return any(
        isinstance(example.get(field_name), str) and example.get(field_name).strip()
        for field_name in ("source", "section")
    )


def _ensure_supported_evaluation_routes(examples: list[dict]) -> None:
    unsupported_routes = sorted(
        {_route_name(example) for example in examples if _route_name(example) not in SUPPORTED_EVALUATION_ROUTES}
    )
    if not unsupported_routes:
        return

    raise SystemExit(
        "Evaluation does not yet implement these routes: "
        f"{', '.join(unsupported_routes)}. "
        "Keep architecture.multimodal_runtime_enabled=false for now or add the multimodal sidecar runtime first."
    )


def _format_release_actual(actual: object) -> str:
    if isinstance(actual, dict):
        return json.dumps(actual, sort_keys=True)
    if isinstance(actual, list):
        return json.dumps(actual)
    return str(actual)


def build_generation_config(gen_pipeline, max_new_tokens: int, pad_token_id: int) -> GenerationConfig:
    base_generation_config = getattr(gen_pipeline.model, "generation_config", None)
    if base_generation_config is None:
        generation_config = GenerationConfig()
    else:
        generation_config = copy.deepcopy(base_generation_config)

    generation_config.max_new_tokens = max_new_tokens
    generation_config.do_sample = False
    generation_config.pad_token_id = pad_token_id
    generation_config.eos_token_id = gen_pipeline.tokenizer.eos_token_id
    generation_config.max_length = None

    if hasattr(generation_config, "temperature"):
        generation_config.temperature = None
    if hasattr(generation_config, "top_p"):
        generation_config.top_p = None

    return generation_config


def resolve_evaluation_settings(cfg: dict, args: argparse.Namespace) -> dict:
    evaluation_cfg = cfg["evaluation"]
    release_cfg = cfg.get("release", {}) if isinstance(cfg.get("release"), dict) else {}
    retrieval_cfg = cfg.get("retrieval", {}) if isinstance(cfg.get("retrieval"), dict) else {}
    release_mode = bool(args.release)

    full_num_examples = _resolve_int_setting(evaluation_cfg.get("num_examples"), 100)
    quick_num_examples = _resolve_int_setting(
        evaluation_cfg.get("quick_num_examples"),
        min(20, full_num_examples),
    )
    full_max_new_tokens = _resolve_int_setting(evaluation_cfg.get("max_new_tokens"), 256)
    quick_max_new_tokens = _resolve_int_setting(
        evaluation_cfg.get("quick_max_new_tokens"),
        min(128, full_max_new_tokens),
    )
    inference_batch_size = _resolve_int_setting(
        evaluation_cfg.get("inference_batch_size"),
        1,
    )
    judge_concurrency = _resolve_int_setting(
        evaluation_cfg.get("judge_concurrency"),
        1,
    )

    return {
        "mode": "full" if release_mode else ("quick" if args.quick else "full"),
        "release_mode": release_mode,
        "num_examples": args.num_examples or (
            quick_num_examples if args.quick else full_num_examples
        ),
        "max_new_tokens": args.max_new_tokens or (
            quick_max_new_tokens if args.quick else full_max_new_tokens
        ),
        "inference_batch_size": args.batch_size or inference_batch_size,
        "judge_concurrency": args.judge_concurrency or judge_concurrency,
        "judge_model": None if args.metrics_only else evaluation_cfg.get("judge_model"),
        "metrics_only": args.metrics_only,
        "fail_on_threshold_breach": (
            release_mode
            or
            args.fail_on_thresholds
            or bool(release_cfg.get("fail_on_threshold_breach", False))
        ),
        "use_retrieval": (
            args.use_retrieval
            or (
                bool(retrieval_cfg.get("enabled", False))
                and not args.quick
                and (
                    bool(retrieval_cfg.get("use_in_full_evaluation", False))
                    or (
                        release_mode
                        and bool(release_cfg.get("require_retrieval_for_grounded_benchmark", False))
                    )
                )
            )
        ),
    }


def load_processed_manifest(processed_dir: str) -> dict | None:
    manifest_path = os.path.join(processed_dir, "manifest.json")
    if not os.path.isfile(manifest_path):
        return None

    try:
        manifest = read_json_file(manifest_path)
    except Exception as exc:
        return {
            "path": os.path.abspath(manifest_path),
            "exists": True,
            "error": str(exc),
        }

    return {
        "path": os.path.abspath(manifest_path),
        "exists": True,
        "schema_version": manifest.get("schema_version"),
        "generated_at": manifest.get("generated_at"),
        "source": manifest.get("source"),
        "counts": manifest.get("counts"),
        "dataset_fingerprints": manifest.get("dataset_fingerprints"),
    }


def build_release_gate(
    cfg: dict,
    mode: str,
    rouge_scores: dict,
    exact_match: float | None,
    judge_scores: list[dict],
    per_category_metrics: dict | None = None,
    examples: list[dict] | None = None,
    retrieval_info: dict | None = None,
) -> dict:
    release_cfg = cfg.get("release")
    if not isinstance(release_cfg, dict):
        return {
            "configured": False,
            "mode": mode,
            "passed": None,
            "checks": [],
            "failure_count": 0,
            "failed_checks": [],
        }

    checks: list[dict] = []
    mode_prefix = "quick" if mode == "quick" else "full"

    def add_metric_check(name: str, threshold_key: str, actual_value: float | None) -> None:
        threshold = _resolve_float_setting(release_cfg.get(threshold_key))
        if threshold is None:
            return

        if actual_value is None:
            checks.append(
                {
                    "name": name,
                    "threshold": threshold,
                    "actual": None,
                    "passed": False,
                    "status": "missing",
                }
            )
            return

        checks.append(
            {
                "name": name,
                "threshold": threshold,
                "actual": _round_metric(actual_value),
                "passed": actual_value >= threshold,
                "status": "evaluated",
            }
        )

    add_metric_check("rouge1", f"{mode_prefix}_min_rouge1", rouge_scores.get("rouge1"))
    add_metric_check("rouge2", f"{mode_prefix}_min_rouge2", rouge_scores.get("rouge2"))
    add_metric_check("rougeL", f"{mode_prefix}_min_rougeL", rouge_scores.get("rougeL"))
    add_metric_check("exact_match", f"{mode_prefix}_min_exact_match", exact_match)

    judge_threshold = _resolve_float_setting(release_cfg.get("min_avg_judge_score"))
    text_examples_present = any(not _is_deterministic_tool_example(example) for example in (examples or []))
    if judge_threshold is not None:
        numeric_judge_scores = [
            float(item["score"])
            for item in judge_scores
            if isinstance(item.get("score"), (int, float))
        ]
        if numeric_judge_scores:
            average_judge_score = sum(numeric_judge_scores) / len(numeric_judge_scores)
            checks.append(
                {
                    "name": "avg_judge_score",
                    "threshold": judge_threshold,
                    "actual": _round_metric(average_judge_score),
                    "passed": average_judge_score >= judge_threshold,
                    "status": "evaluated",
                }
            )
        else:
            checks.append(
                {
                    "name": "avg_judge_score",
                    "threshold": judge_threshold,
                    "actual": None,
                    "passed": not text_examples_present,
                    "status": "missing" if text_examples_present else "skipped",
                    "reason": (
                        "judge scores unavailable"
                        if text_examples_present
                        else "no text-generation examples selected"
                    ),
                }
            )

    if bool(release_cfg.get("require_retrieval_for_grounded_benchmark", False)):
        grounded_examples = [example for example in (examples or []) if _is_grounded_example(example)]
        if not grounded_examples:
            checks.append(
                {
                    "name": "grounded_benchmark_retrieval",
                    "threshold": "enabled_and_used",
                    "actual": {"grounded_examples": 0},
                    "passed": True,
                    "status": "skipped",
                    "reason": "no grounded benchmark rows selected",
                }
            )
        else:
            retrieval_enabled = bool(retrieval_info.get("enabled")) if isinstance(retrieval_info, dict) else False
            retrieval_used = bool(retrieval_info.get("used")) if isinstance(retrieval_info, dict) else False
            checks.append(
                {
                    "name": "grounded_benchmark_retrieval",
                    "threshold": "enabled_and_used",
                    "actual": {
                        "grounded_examples": len(grounded_examples),
                        "retrieval_enabled": retrieval_enabled,
                        "retrieval_used": retrieval_used,
                    },
                    "passed": retrieval_used,
                    "status": "evaluated" if retrieval_enabled else "missing",
                }
            )

    category_thresholds = release_cfg.get("category_thresholds")
    if isinstance(category_thresholds, dict):
        for category_name, thresholds in category_thresholds.items():
            category_metrics = (per_category_metrics or {}).get(category_name)
            if category_metrics is None:
                checks.append(
                    {
                        "name": f"category:{category_name}",
                        "threshold": "configured",
                        "actual": None,
                        "passed": False,
                        "status": "missing",
                    }
                )
                continue

            metric_map = {
                "min_rouge1": category_metrics.get("rouge", {}).get("rouge1"),
                "min_rouge2": category_metrics.get("rouge", {}).get("rouge2"),
                "min_rougeL": category_metrics.get("rouge", {}).get("rougeL"),
                "min_exact_match": category_metrics.get("exact_match"),
                "min_avg_judge_score": category_metrics.get("avg_judge_score"),
                "min_tool_success_rate": category_metrics.get("tool_success_rate"),
                "min_avg_tool_match_score": category_metrics.get("avg_tool_match_score"),
            }
            for threshold_key, actual in metric_map.items():
                threshold = _resolve_float_setting(thresholds.get(threshold_key))
                if threshold is None:
                    continue

                checks.append(
                    {
                        "name": f"category:{category_name}:{threshold_key}",
                        "threshold": threshold,
                        "actual": _round_metric(actual),
                        "passed": actual is not None and actual >= threshold,
                        "status": "evaluated" if actual is not None else "missing",
                    }
                )

    blocking_checks = [check for check in checks if check["status"] != "skipped"]
    failed_checks = [check for check in blocking_checks if not check["passed"]]
    if not checks:
        passed = None
    else:
        passed = all(check["passed"] for check in blocking_checks)

    return {
        "configured": bool(checks),
        "mode": mode,
        "passed": passed,
        "checks": checks,
        "failure_count": len(failed_checks),
        "failed_checks": failed_checks,
    }


def run_inference(
    gen_pipeline,
    prompts: list[str],
    batch_size: int,
    max_new_tokens: int = 256,
) -> tuple[list[str], dict]:
    predictions = []
    total = len(prompts)
    requested_batch_size = max(1, batch_size)
    current_batch_size = max(1, requested_batch_size)
    oom_retries = 0
    start_time = time.perf_counter()
    start_index = 0

    if hasattr(gen_pipeline.tokenizer, "pad_token_id") and gen_pipeline.tokenizer.pad_token_id is not None:
        pad_token_id = gen_pipeline.tokenizer.pad_token_id
    else:
        pad_token_id = gen_pipeline.tokenizer.eos_token_id
    generation_config = build_generation_config(gen_pipeline, max_new_tokens, pad_token_id)

    while start_index < total:
        try:
            prompt_batch = prompts[start_index:start_index + current_batch_size]
            batch_start = time.perf_counter()
            outputs = gen_pipeline(
                prompt_batch,
                batch_size=current_batch_size,
                generation_config=generation_config,
            )
            for out in outputs:
                generated = out[0]["generated_text"]
                predictions.append(_extract_prediction(generated))

            start_index += len(prompt_batch)
            batch_elapsed = time.perf_counter() - batch_start
            overall_elapsed = max(time.perf_counter() - start_time, 1e-6)
            print(
                "    Inference "
                f"{start_index}/{total} examples "
                f"(batch_size={current_batch_size}, "
                f"{batch_elapsed:.1f}s batch, "
                f"{start_index / overall_elapsed:.2f} ex/s)"
            )
        except RuntimeError as exc:
            if not _is_recoverable_cuda_error(exc) or current_batch_size == 1:
                raise

            oom_retries += 1
            next_batch_size = max(1, current_batch_size // 2)
            print(
                "    ⚠️   CUDA generation failure; retrying with "
                f"batch_size={next_batch_size}."
            )
            current_batch_size = next_batch_size
            _clear_cuda_cache()

    total_elapsed = time.perf_counter() - start_time
    return predictions, {
        "requested_batch_size": requested_batch_size,
        "final_batch_size": current_batch_size,
        "oom_retries": oom_retries,
        "examples_per_second": round(total / max(total_elapsed, 1e-6), 4),
    }


# ── Scoring ───────────────────────────────────────────────────────────────────

def score_rouge(predictions: list[str], references: list[str]) -> dict:
    if _scorer is None:
        print("  ⚠️   rouge-score library not available; skipping ROUGE.")
        return {}
    aggregated = {"rouge1": [], "rouge2": [], "rougeL": []}
    for pred, ref in zip(predictions, references):
        scores = _scorer.score(ref, pred)
        for key in aggregated:
            aggregated[key].append(scores[key].fmeasure)
    return {k: round(sum(v) / len(v), 4) for k, v in aggregated.items() if v}


def score_exact_match(predictions: list[str], references: list[str]) -> float:
    """Case-insensitive exact match after normalisation."""
    matches = sum(
        _normalise(p) == _normalise(r)
        for p, r in zip(predictions, references)
    )
    return round(matches / len(predictions), 4) if predictions else 0.0


def score_by_category(
    predictions: list[str],
    references: list[str],
    examples: list[dict],
    judge_scores: list[dict],
) -> dict:
    grouped_indexes: dict[str, list[int]] = {}
    for index, example in enumerate(examples):
        if _is_deterministic_tool_example(example):
            continue
        category = example.get("category")
        if not isinstance(category, str) or not category.strip():
            continue
        grouped_indexes.setdefault(category, []).append(index)

    category_metrics: dict[str, dict] = {}
    for category, indexes in grouped_indexes.items():
        category_predictions = [predictions[index] for index in indexes]
        category_references = [references[index] for index in indexes]
        category_judge_scores = [judge_scores[index] for index in indexes]
        numeric_judge_scores = [
            float(item["score"])
            for item in category_judge_scores
            if isinstance(item.get("score"), (int, float))
        ]

        category_metrics[category] = {
            "count": len(indexes),
            "rouge": score_rouge(category_predictions, category_references),
            "exact_match": score_exact_match(category_predictions, category_references),
            "avg_judge_score": _round_metric(
                sum(numeric_judge_scores) / len(numeric_judge_scores)
            ) if numeric_judge_scores else None,
        }

    return category_metrics


def _compare_expected_fields(
    expected: object,
    actual: object,
    path: str,
    checks: list[dict],
    tolerance: float = 1e-4,
) -> None:
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            checks.append(
                {
                    "path": path,
                    "expected": expected,
                    "actual": actual,
                    "passed": False,
                }
            )
            return

        for key, value in expected.items():
            next_path = f"{path}.{key}" if path else str(key)
            _compare_expected_fields(value, actual.get(key), next_path, checks, tolerance=tolerance)
        return

    if isinstance(expected, bool):
        passed = isinstance(actual, bool) and actual is expected
    elif isinstance(expected, (int, float)) and not isinstance(expected, bool):
        passed = (
            isinstance(actual, (int, float))
            and abs(float(actual) - float(expected)) <= tolerance
        )
    else:
        passed = actual == expected

    checks.append(
        {
            "path": path,
            "expected": expected,
            "actual": actual,
            "passed": passed,
        }
    )


def execute_deterministic_tool_example(cfg: dict, example: dict) -> dict:
    tool_name = example.get("tool_name")
    tool_request = example.get("tool_request") if isinstance(example.get("tool_request"), dict) else {}
    tool_expectation = (
        example.get("tool_expectation") if isinstance(example.get("tool_expectation"), dict) else {}
    )

    request = build_tool_request(
        str(tool_name),
        query=tool_request.get("query"),
        record_id=tool_request.get("record_id"),
        lookup_key=tool_request.get("lookup_key"),
        filters=tool_request.get("filters"),
        top_k=tool_request.get("top_k"),
        quantity=tool_request.get("quantity"),
    )

    checks: list[dict] = []
    try:
        if tool_name == ESTIMATE_LOOKUP_TOOL_NAME:
            response = run_estimate_lookup_request(
                cfg,
                request,
                index_path=tool_request.get("index_path"),
                min_score=tool_request.get("min_score"),
            )
        elif tool_name == REVIT_ENTITY_LOOKUP_TOOL_NAME:
            response = run_revit_entity_lookup_request(
                cfg,
                request,
                index_path=tool_request.get("index_path"),
                min_score=tool_request.get("min_score"),
            )
        else:
            return {
                "route": _route_name(example),
                "tool_name": tool_name,
                "passed": False,
                "match_score": 0.0,
                "passed_checks": 0,
                "total_checks": 1,
                "checks": [
                    {
                        "path": "tool_name",
                        "expected": [ESTIMATE_LOOKUP_TOOL_NAME, REVIT_ENTITY_LOOKUP_TOOL_NAME],
                        "actual": tool_name,
                        "passed": False,
                    }
                ],
                "error": f"Unsupported deterministic tool: {tool_name}",
                "response": None,
            }

        minimum_results = tool_expectation.get("result_count_at_least")
        if minimum_results is not None:
            actual_result_count = int(response.get("result_count", 0))
            checks.append(
                {
                    "path": "result_count_at_least",
                    "expected": minimum_results,
                    "actual": actual_result_count,
                    "passed": actual_result_count >= int(minimum_results),
                }
            )

        top_result_expectation = tool_expectation.get("top_result")
        if top_result_expectation is not None:
            top_result = response.get("results", [None])[0] if response.get("results") else None
            _compare_expected_fields(top_result_expectation, top_result, "top_result", checks)
    except Exception as exc:
        return {
            "route": _route_name(example),
            "tool_name": tool_name,
            "passed": False,
            "match_score": 0.0,
            "passed_checks": 0,
            "total_checks": 1,
            "checks": [
                {
                    "path": "tool_execution",
                    "expected": "success",
                    "actual": str(exc),
                    "passed": False,
                }
            ],
            "error": str(exc),
            "response": None,
        }

    total_checks = len(checks)
    passed_checks = sum(1 for check in checks if check["passed"])
    if total_checks:
        passed = passed_checks == total_checks
        match_score = round(passed_checks / total_checks, 4)
    else:
        passed = bool(response.get("result_count", 0))
        match_score = 1.0 if passed else 0.0

    return {
        "route": _route_name(example),
        "tool_name": tool_name,
        "passed": passed,
        "match_score": match_score,
        "passed_checks": passed_checks,
        "total_checks": total_checks,
        "checks": checks,
        "response": response,
        "warnings": response.get("warnings", []),
    }


def score_deterministic_tools_by_category(route_results: list[dict | None], examples: list[dict]) -> dict:
    grouped: dict[str, list[dict]] = {}
    for index, example in enumerate(examples):
        route_result = route_results[index]
        if route_result is None:
            continue
        category = example.get("category")
        if not isinstance(category, str) or not category.strip():
            continue
        grouped.setdefault(category, []).append(route_result)

    category_metrics: dict[str, dict] = {}
    for category, results in grouped.items():
        match_scores = [float(item.get("match_score", 0.0)) for item in results]
        passed = [item for item in results if item.get("passed")]
        tool_names = sorted({str(item.get("tool_name")) for item in results if item.get("tool_name")})
        category_metrics[category] = {
            "count": len(results),
            "route": "deterministic_tool",
            "tool_names": tool_names,
            "tool_success_rate": round(len(passed) / len(results), 4),
            "avg_tool_match_score": _round_metric(sum(match_scores) / len(match_scores)),
        }

    return category_metrics


def summarise_deterministic_tool_results(route_results: list[dict | None]) -> dict:
    filtered_results = [item for item in route_results if item is not None]
    if not filtered_results:
        return {
            "count": 0,
            "passed": 0,
            "tool_success_rate": None,
            "avg_tool_match_score": None,
            "tool_names": [],
        }

    match_scores = [float(item.get("match_score", 0.0)) for item in filtered_results]
    return {
        "count": len(filtered_results),
        "passed": sum(1 for item in filtered_results if item.get("passed")),
        "tool_success_rate": round(
            sum(1 for item in filtered_results if item.get("passed")) / len(filtered_results),
            4,
        ),
        "avg_tool_match_score": _round_metric(sum(match_scores) / len(match_scores)),
        "tool_names": sorted(
            {str(item.get("tool_name")) for item in filtered_results if item.get("tool_name")}
        ),
    }


# ── LLM-as-judge ───────────────────────────────────────────────────────────────

_JUDGE_SYSTEM_PROMPT = (
    "You are an expert evaluator. You will be given an instruction, a reference "
    "answer, and a model-generated response. Rate the response on a scale of 1-5 "
    "using these criteria:\n"
    "  5 = Excellent: accurate, complete, and well-structured\n"
    "  4 = Good: mostly accurate with minor omissions\n"
    "  3 = Acceptable: partially correct but missing key information\n"
    "  2 = Poor: significant errors or omissions\n"
    "  1 = Unacceptable: wrong, incoherent, or irrelevant\n\n"
    "Respond with ONLY a JSON object: {\"score\": <int 1-5>, \"rationale\": \"<brief explanation>\"}"
)


def _build_judge_message(prompt: str, prediction: str, reference: str) -> str:
    return (
        f"### Instruction\n{prompt}\n\n"
        f"### Reference Answer\n{reference}\n\n"
        f"### Model Response\n{prediction}\n\n"
        "Rate the model response. Return JSON only."
    )


def _ollama_binary() -> str | None:
    return shutil.which("ollama") or os.path.expanduser("~/.local/bin/ollama")


def _wait_for_ollama_server(timeout_sec: float = 30.0) -> None:
    deadline = time.time() + timeout_sec
    last_error: Exception | None = None

    while time.time() < deadline:
        try:
            response = requests.get("http://127.0.0.1:11434/api/tags", timeout=5)
            response.raise_for_status()
            return
        except requests.RequestException as exc:
            last_error = exc
            time.sleep(0.5)

    if last_error is not None:
        raise last_error
    raise RuntimeError("Timed out waiting for Ollama server")


def _ensure_ollama_server() -> subprocess.Popen | None:
    try:
        _wait_for_ollama_server(timeout_sec=1.0)
        return None
    except requests.RequestException:
        pass

    ollama = _ollama_binary()
    if not ollama or not os.path.exists(ollama):
        raise FileNotFoundError("Ollama binary not found")

    server_process = subprocess.Popen(
        [ollama, "serve"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        _wait_for_ollama_server(timeout_sec=30.0)
    except Exception:
        server_process.terminate()
        try:
            server_process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            server_process.kill()
            server_process.wait(timeout=10)
        raise

    return server_process


def _stop_server_process(server_process: subprocess.Popen | None) -> None:
    if server_process is None:
        return

    server_process.terminate()
    try:
        server_process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        server_process.kill()
        server_process.wait(timeout=10)


def _get_judge_client_factory(judge_model: str):
    try:
        from openai import OpenAI
    except ImportError:
        print("  ⚠️   openai package not installed; skipping LLM-as-judge.")
        return None, None

    if judge_model.startswith("openai/"):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("  ⚠️   OPENAI_API_KEY not set; skipping LLM-as-judge.")
            return None, None

        model_name = judge_model.removeprefix("openai/")

        def create_client():
            return OpenAI(api_key=api_key)
    else:
        model_name = judge_model

        def create_client():
            return OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

    return create_client, model_name


def _score_single_judgement(
    create_client,
    model_name: str,
    prompt: str,
    prediction: str,
    reference: str,
) -> dict:
    try:
        client = create_client()
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": _JUDGE_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": _build_judge_message(prompt, prediction, reference),
                },
            ],
            temperature=0.0,
            max_tokens=256,
        )
        raw = response.choices[0].message.content.strip()
        json_match = re.search(r'\{[^}]+\}', raw)
        parsed = json.loads(json_match.group() if json_match else raw)
        score = int(parsed.get("score", 0))
        rationale = str(parsed.get("rationale", ""))
        if not 1 <= score <= 5:
            raise ValueError(f"score {score} out of range")
        return {"score": score, "rationale": rationale}
    except Exception as exc:
        return {"score": None, "rationale": f"judge error: {exc}"}


def llm_judge(
    judge_model: str | None,
    prompts: list[str],
    predictions: list[str],
    references: list[str],
    concurrency: int = 1,
) -> list[dict]:
    """
    Score each prediction using a local Ollama model or OpenAI-compatible judge.

    Set evaluation.judge_model in config.yaml to:
      - An Ollama model name (e.g. "simcoe") for fully local judging.
      - "openai/<model>" (e.g. "openai/gpt-4o") to use the OpenAI API.
      - null to disable.
    """
    if judge_model is None:
        return [
            {"score": None, "rationale": "LLM-as-judge not configured"}
            for _ in predictions
        ]

    server_process = None
    if not judge_model.startswith("openai/"):
        try:
            server_process = _ensure_ollama_server()
        except Exception as exc:
            return [
                {"score": None, "rationale": f"judge backend unavailable: {exc}"}
                for _ in predictions
            ]

    try:
        create_client, model_name = _get_judge_client_factory(judge_model)
        if create_client is None:
            return [
                {"score": None, "rationale": "judge backend unavailable"}
                for _ in predictions
            ]

        results: list[dict] = []
        total = len(predictions)
        if concurrency <= 1 or total <= 1:
            for i, (prompt, pred, ref) in enumerate(zip(prompts, predictions, references)):
                results.append(_score_single_judgement(create_client, model_name, prompt, pred, ref))
                if (i + 1) % 10 == 0 or (i + 1) == total:
                    print(f"    Judged {i + 1}/{total} examples …")
            return results

        results = [None] * total
        max_workers = min(concurrency, total)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_index = {
                executor.submit(
                    _score_single_judgement,
                    create_client,
                    model_name,
                    prompts[i],
                    predictions[i],
                    references[i],
                ): i
                for i in range(total)
            }
            completed = 0
            for future in as_completed(future_to_index):
                index = future_to_index[future]
                try:
                    results[index] = future.result()
                except Exception as exc:
                    results[index] = {"score": None, "rationale": f"judge error: {exc}"}
                completed += 1
                if completed % 10 == 0 or completed == total:
                    print(f"    Judged {completed}/{total} examples …")

        return results
    finally:
        _stop_server_process(server_process)


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the fine-tuned model.")
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument(
        "--num_examples",
        type=int,
        default=None,
        help="Number of validation examples to evaluate. Defaults to the config profile.",
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=None,
        help="Override evaluation.inference_batch_size for generation.",
    )
    parser.add_argument(
        "--max_new_tokens",
        type=int,
        default=None,
        help="Override evaluation.max_new_tokens for generation.",
    )
    parser.add_argument(
        "--judge_concurrency",
        type=int,
        default=None,
        help="Override evaluation.judge_concurrency for LLM-as-judge requests.",
    )
    parser.add_argument(
        "--metrics_only",
        action="store_true",
        help="Skip LLM-as-judge scoring and compute automatic metrics only.",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Use quick evaluation defaults from the config.",
    )
    parser.add_argument(
        "--release",
        action="store_true",
        help="Run the full release profile and fail closed on release gate misses.",
    )
    parser.add_argument(
        "--use_retrieval",
        action="store_true",
        help="Augment prompts with retrieved context when retrieval is configured.",
    )
    parser.add_argument(
        "--fail_on_thresholds",
        action="store_true",
        help="Exit non-zero when configured release thresholds are not met.",
    )
    args = parser.parse_args()

    if args.release and args.quick:
        parser.error("--release cannot be combined with --quick")

    cfg = load_config(args.config)
    settings = resolve_evaluation_settings(cfg, args)
    validate_evaluate_config(cfg, settings["num_examples"])

    model_dir = cfg["export"]["merged_16bit_dir"]
    results_path = cfg["evaluation"]["results_path"]
    judge_model = settings["judge_model"]
    max_seq_length = cfg["model"]["max_seq_length"]
    total_start = time.perf_counter()
    processed_manifest = load_processed_manifest(cfg["data"]["processed_dir"])

    print(
        "\n⚙️   Evaluation settings: "
        f"mode={settings['mode']}, "
        f"release_mode={settings['release_mode']}, "
        f"num_examples={settings['num_examples']}, "
        f"batch_size={settings['inference_batch_size']}, "
        f"max_new_tokens={settings['max_new_tokens']}, "
        f"judge_concurrency={settings['judge_concurrency']}, "
        f"use_retrieval={settings['use_retrieval']}, "
        f"metrics_only={settings['metrics_only']}, "
        f"fail_on_threshold_breach={settings['fail_on_threshold_breach']}"
    )

    if processed_manifest is None:
        print("  ⚠️   Processed dataset manifest not found. Re-run prepare_data to capture lineage metadata.")
    elif processed_manifest.get("error"):
        print(f"  ⚠️   Could not read processed dataset manifest ({processed_manifest['error']}).")
    else:
        manifest_path = processed_manifest["path"]
        print(f"  📄  Loaded processed dataset manifest: {manifest_path}")

    # ── Load evaluation data ──────────────────────────────────────────────────
    examples, evaluation_source = load_evaluation_examples(cfg, settings)
    _ensure_supported_evaluation_routes(examples)
    print(f"\n📂  Loading evaluation rows from: {evaluation_source['path']}")
    print(f"    Dataset kind: {evaluation_source['kind']}")
    print(f"    Evaluating on {len(examples)} examples.")

    references = [example["reference"] for example in examples]
    prompts: list[str | None] = [example["prompt"] for example in examples]
    predictions: list[str | None] = [None] * len(examples)
    judge_scores: list[dict] = [
        {"score": None, "rationale": "not evaluated for this route"}
        for _ in examples
    ]
    route_results: list[dict | None] = [None] * len(examples)
    retrieval_traces: list[dict | None] = [None] * len(examples)

    text_indexes = [index for index, example in enumerate(examples) if not _is_deterministic_tool_example(example)]
    tool_indexes = [index for index, example in enumerate(examples) if _is_deterministic_tool_example(example)]

    model_load_seconds = 0.0
    inference_seconds = 0.0
    inference_stats = {
        "evaluated_examples": 0,
        "requested_batch_size": settings["inference_batch_size"],
        "final_batch_size": settings["inference_batch_size"],
        "oom_retries": 0,
        "examples_per_second": 0.0,
    }
    judge_seconds = 0.0
    retrieval_info = {"enabled": False, "used": False}
    rouge_scores: dict = {}
    em_score: float | None = None

    if text_indexes:
        print(f"\n🔍  Loading merged model from: {model_dir}")
        model_load_start = time.perf_counter()
        tokenizer = load_tokenizer_with_compat(model_dir)
        if tokenizer.pad_token_id is None and tokenizer.eos_token_id is not None:
            tokenizer.pad_token_id = tokenizer.eos_token_id
        model = AutoModelForCausalLM.from_pretrained(
            model_dir,
            device_map="auto",
            torch_dtype="auto",
            trust_remote_code=True,
        )
        gen_pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
        )
        model_load_seconds = time.perf_counter() - model_load_start
        print(f"    Model ready in {model_load_seconds:.1f}s")

        text_examples = [examples[index] for index in text_indexes]
        text_references = [references[index] for index in text_indexes]
        text_prompts, retrieval_info = prepare_prompts_with_retrieval(text_examples, cfg, settings)
        if retrieval_info.get("used"):
            text_retrieval = retrieval_info.get("per_example", [None] * len(text_examples))
        else:
            text_retrieval = [None] * len(text_examples)

        for local_index, example_index in enumerate(text_indexes):
            prompts[example_index] = text_prompts[local_index]
            retrieval_traces[example_index] = text_retrieval[local_index]

        print("\n🤖  Running inference …")
        inference_start = time.perf_counter()
        text_predictions, inference_stats = run_inference(
            gen_pipeline,
            text_prompts,
            batch_size=settings["inference_batch_size"],
            max_new_tokens=settings["max_new_tokens"],
        )
        inference_seconds = time.perf_counter() - inference_start
        inference_stats["evaluated_examples"] = len(text_indexes)

        for local_index, example_index in enumerate(text_indexes):
            predictions[example_index] = text_predictions[local_index]

        print("\n📊  Computing automatic metrics …")
        rouge_scores = score_rouge(text_predictions, text_references)
        em_score = score_exact_match(text_predictions, text_references)
        print(f"    ROUGE:        {rouge_scores}")
        print(f"    Exact match:  {em_score:.4f}")

        if judge_model is None:
            print("\n🧑‍⚖️  Skipping LLM-as-judge evaluation.")
            text_judge_scores = [
                {"score": None, "rationale": "LLM-as-judge not configured"}
                for _ in text_predictions
            ]
        else:
            print("\n🧑‍⚖️  Running LLM-as-judge evaluation …")
            judge_start = time.perf_counter()
            text_judge_scores = llm_judge(
                judge_model,
                text_prompts,
                text_predictions,
                text_references,
                concurrency=settings["judge_concurrency"],
            )
            judge_seconds = time.perf_counter() - judge_start

        for local_index, example_index in enumerate(text_indexes):
            judge_scores[example_index] = text_judge_scores[local_index]
    else:
        print("\n🤖  No text-generation benchmark rows selected; skipping model inference.")

    if tool_indexes:
        print("\n🧰  Running deterministic tool evaluation …")
        for example_index in tool_indexes:
            route_result = execute_deterministic_tool_example(cfg, examples[example_index])
            route_results[example_index] = route_result
            response = route_result.get("response") if isinstance(route_result, dict) else None
            top_result = response.get("results", [None])[0] if isinstance(response, dict) and response.get("results") else None
            if top_result is not None:
                predictions[example_index] = json.dumps(top_result, sort_keys=True)

    per_category_metrics = score_by_category(predictions, references, examples, judge_scores)
    per_category_metrics.update(score_deterministic_tools_by_category(route_results, examples))
    deterministic_tool_metrics = summarise_deterministic_tool_results(route_results)

    release_gate = build_release_gate(
        cfg,
        settings["mode"],
        rouge_scores,
        em_score,
        judge_scores,
        per_category_metrics=per_category_metrics,
        examples=examples,
        retrieval_info=retrieval_info,
    )

    if release_gate["configured"]:
        print(
            "\n🚦  Release gate: "
            f"{'PASS' if release_gate['passed'] else 'FAIL'}"
        )
        for check in release_gate["failed_checks"][:5]:
            print(
                "    - "
                f"{check['name']}: actual={_format_release_actual(check['actual'])} "
                f"threshold={check['threshold']}"
            )
        if release_gate["failure_count"] > 5:
            print(f"    ... {release_gate['failure_count'] - 5} more blocking checks")

    # ── Save results ──────────────────────────────────────────────────────────
    results = {
        "generated_at": current_utc_timestamp(),
        "num_examples": len(examples),
        "mode": settings["mode"],
        "metrics": {
            "rouge": rouge_scores,
            "exact_match": em_score,
            "deterministic_tools": deterministic_tool_metrics,
        },
        "judge_model": judge_model,
        "settings": {
            "max_seq_length": max_seq_length,
            "max_new_tokens": settings["max_new_tokens"],
            "inference_batch_size": settings["inference_batch_size"],
            "judge_concurrency": settings["judge_concurrency"],
            "use_retrieval": settings["use_retrieval"],
            "metrics_only": settings["metrics_only"],
            "release_mode": settings["release_mode"],
            "fail_on_threshold_breach": settings["fail_on_threshold_breach"],
        },
        "evaluation_source": evaluation_source,
        "retrieval": retrieval_info,
        "data_manifest": processed_manifest,
        "release_gate": release_gate,
        "timings_sec": {
            "model_load": round(model_load_seconds, 4),
            "inference": round(inference_seconds, 4),
            "judge": round(judge_seconds, 4),
            "total": round(time.perf_counter() - total_start, 4),
        },
        "inference_stats": inference_stats,
        "per_category_metrics": per_category_metrics,
        "per_example": [
            {
                "prompt": prompts[i],
                "reference": references[i],
                "prediction": predictions[i],
                "judge": judge_scores[i],
                "category": examples[i].get("category"),
                "benchmark_id": examples[i].get("benchmark_id"),
                "route": _route_name(examples[i]),
                "runtime_owner": examples[i].get("runtime_owner"),
                "tool_name": examples[i].get("tool_name"),
                "tool_request": examples[i].get("tool_request"),
                "tool_expectation": examples[i].get("tool_expectation"),
                "route_evaluation": route_results[i],
                "source": examples[i].get("source"),
                "section": examples[i].get("section"),
                "retrieval": retrieval_traces[i],
            }
            for i in range(len(examples))
        ],
    }

    write_json_file(results_path, results)

    print(f"\n💾  Results saved to: {results_path}")

    if (
        release_gate["configured"]
        and settings["fail_on_threshold_breach"]
        and release_gate["passed"] is False
    ):
        print("\n❌  Evaluation failed configured release thresholds.\n")
        raise SystemExit(2)

    print("\n✅  Evaluation complete.\n")


if __name__ == "__main__":
    main()
