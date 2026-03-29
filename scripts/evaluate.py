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
import json
import os
import re
import string

from config_validation import load_config, validate_evaluate_config
from datasets import load_from_disk
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

try:
    from rouge_score import rouge_scorer
    _scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
except ImportError:
    _scorer = None


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


def run_inference(
    gen_pipeline,
    examples: list[dict],
    max_new_tokens: int = 256,
) -> list[str]:
    prompts = [extract_prompt(ex["text"]) for ex in examples]
    outputs = gen_pipeline(
        prompts,
        max_new_tokens=max_new_tokens,
        do_sample=False,
        temperature=1.0,
        pad_token_id=gen_pipeline.tokenizer.eos_token_id,
    )
    predictions = []
    for out in outputs:
        # The pipeline returns the full sequence; strip the prompt prefix.
        generated = out[0]["generated_text"]
        # Extract text after '### Response:'
        parts = generated.split("### Response:")
        pred = parts[-1].strip() if len(parts) >= 2 else generated.strip()
        predictions.append(pred)
    return predictions


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


def llm_judge(
    judge_model: str | None,
    prompts: list[str],
    predictions: list[str],
    references: list[str],
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

    use_openai = judge_model.startswith("openai/")

    if use_openai:
        try:
            from openai import OpenAI
        except ImportError:
            print("  ⚠️   openai package not installed; skipping LLM-as-judge.")
            return [{"score": None, "rationale": "openai package not installed"} for _ in predictions]

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("  ⚠️   OPENAI_API_KEY not set; skipping LLM-as-judge.")
            return [{"score": None, "rationale": "OPENAI_API_KEY not set"} for _ in predictions]

        client = OpenAI(api_key=api_key)
        model_name = judge_model.removeprefix("openai/")
    else:
        # Use Ollama via its OpenAI-compatible API
        try:
            from openai import OpenAI
        except ImportError:
            print("  ⚠️   openai package not installed; skipping LLM-as-judge.")
            return [{"score": None, "rationale": "openai package not installed"} for _ in predictions]

        client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        model_name = judge_model

    results: list[dict] = []
    for i, (prompt, pred, ref) in enumerate(zip(prompts, predictions, references)):
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": _JUDGE_SYSTEM_PROMPT},
                    {"role": "user", "content": _build_judge_message(prompt, pred, ref)},
                ],
                temperature=0.0,
                max_tokens=256,
            )
            raw = response.choices[0].message.content.strip()
            # Try to extract JSON from the response
            json_match = re.search(r'\{[^}]+\}', raw)
            if json_match:
                parsed = json.loads(json_match.group())
            else:
                parsed = json.loads(raw)
            score = int(parsed.get("score", 0))
            rationale = str(parsed.get("rationale", ""))
            if not 1 <= score <= 5:
                raise ValueError(f"score {score} out of range")
            results.append({"score": score, "rationale": rationale})
        except Exception as exc:
            results.append({"score": None, "rationale": f"judge error: {exc}"})

        if (i + 1) % 10 == 0:
            print(f"    Judged {i + 1}/{len(predictions)} examples …")

    return results


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the fine-tuned model.")
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument(
        "--num_examples",
        type=int,
        default=100,
        help="Number of validation examples to evaluate (default: 100).",
    )
    args = parser.parse_args()

    cfg = load_config(args.config)
    validate_evaluate_config(cfg, args.num_examples)

    model_dir = cfg["export"]["merged_16bit_dir"]
    valid_dir = os.path.join(cfg["data"]["processed_dir"], "valid")
    results_path = cfg["evaluation"]["results_path"]
    judge_model = cfg["evaluation"].get("judge_model")
    max_seq_length = cfg["model"]["max_seq_length"]

    # ── Load model ────────────────────────────────────────────────────────────
    print(f"\n🔍  Loading merged model from: {model_dir}")
    tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_dir,
        device_map="auto",
        trust_remote_code=True,
    )
    gen_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=max_seq_length,
    )

    # ── Load validation data ──────────────────────────────────────────────────
    print(f"\n📂  Loading validation set from: {valid_dir}")
    valid_ds = load_from_disk(valid_dir)
    examples = list(valid_ds)[:args.num_examples]
    print(f"    Evaluating on {len(examples)} examples.")

    references = [extract_reference(ex["text"]) for ex in examples]
    prompts = [extract_prompt(ex["text"]) for ex in examples]

    # ── Run inference ─────────────────────────────────────────────────────────
    print("\n🤖  Running inference …")
    predictions = run_inference(gen_pipeline, examples)

    # ── Automatic metrics ─────────────────────────────────────────────────────
    print("\n📊  Computing automatic metrics …")
    rouge_scores = score_rouge(predictions, references)
    em_score = score_exact_match(predictions, references)

    print(f"    ROUGE:        {rouge_scores}")
    print(f"    Exact match:  {em_score:.4f}")

    # ── LLM-as-judge ─────────────────────────────────────────────────────────
    print("\n🧑‍⚖️  Running LLM-as-judge evaluation …")
    judge_scores = llm_judge(judge_model, prompts, predictions, references)

    # ── Save results ──────────────────────────────────────────────────────────
    results = {
        "num_examples": len(examples),
        "metrics": {
            "rouge": rouge_scores,
            "exact_match": em_score,
        },
        "judge_model": judge_model,
        "per_example": [
            {
                "prompt": prompts[i],
                "reference": references[i],
                "prediction": predictions[i],
                "judge": judge_scores[i],
            }
            for i in range(len(examples))
        ],
    }

    os.makedirs(os.path.dirname(results_path), exist_ok=True)
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n💾  Results saved to: {results_path}")
    print("\n✅  Evaluation complete.\n")


if __name__ == "__main__":
    main()
