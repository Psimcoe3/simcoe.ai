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

import yaml
from datasets import load_from_disk
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

try:
    import evaluate as hf_evaluate
    _rouge = hf_evaluate.load("rouge")
except Exception:
    _rouge = None


# ── Config ────────────────────────────────────────────────────────────────────

def load_config(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


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
    if _rouge is None:
        print("  ⚠️   evaluate library not available; skipping ROUGE.")
        return {}
    scores = _rouge.compute(predictions=predictions, references=references)
    return {k: round(v, 4) for k, v in scores.items()}


def score_exact_match(predictions: list[str], references: list[str]) -> float:
    """Case-insensitive exact match after normalisation."""
    matches = sum(
        _normalise(p) == _normalise(r)
        for p, r in zip(predictions, references)
    )
    return round(matches / len(predictions), 4) if predictions else 0.0


# ── LLM-as-judge (stub) ───────────────────────────────────────────────────────

def llm_judge_stub(
    judge_model: str | None,
    prompts: list[str],
    predictions: list[str],
    references: list[str],
) -> list[dict]:
    """
    Stub for LLM-as-judge evaluation.

    When judge_model is set in config.yaml, this function should:
      1. Construct a scoring prompt that presents the instruction, reference
         response, and model output to a capable judge model.
      2. Parse a numeric score (e.g. 1–5) and a brief rationale from the
         judge's response.
      3. Return a list of per-example dicts with 'score' and 'rationale' keys.

    For now it returns placeholder values.  Replace the body of this function
    with a real implementation using the OpenAI / Anthropic SDK or a local
    vLLM-served judge model.

    Example scoring prompt template:
        "Rate the following response on a scale of 1–5 for correctness and
         helpfulness.
         Instruction: {instruction}
         Reference: {reference}
         Response: {response}
         Score:"
    """
    if judge_model is None:
        return [{"score": None, "rationale": "LLM-as-judge not configured"} for _ in predictions]

    # TODO: implement real judge logic here
    # Example with OpenAI:
    #   from openai import OpenAI
    #   client = OpenAI()
    #   for prompt, pred, ref in zip(prompts, predictions, references):
    #       resp = client.chat.completions.create(...)
    #       ...
    print(f"  ⚠️   LLM-as-judge stub called with judge_model='{judge_model}'.  "
          "Returning placeholder scores.")
    return [{"score": None, "rationale": "stub — not yet implemented"} for _ in predictions]


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
    judge_scores = llm_judge_stub(judge_model, prompts, predictions, references)

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
