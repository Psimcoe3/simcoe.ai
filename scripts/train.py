from __future__ import annotations

"""
scripts/train.py
────────────────
4-bit QLoRA fine-tuning pipeline using Unsloth + TRL SFTTrainer.

Every hyperparameter is read from config.yaml — nothing is hardcoded.
Inline comments explain *why* each value was chosen, not just what it does.

Usage:
    python scripts/train.py [--config config.yaml]

Prerequisites:
    • Run scripts/check_env.py first to validate the environment.
    • Processed datasets must exist (run scripts/prepare_data.py first).
    • .env must contain HF_TOKEN, WANDB_API_KEY, WANDB_PROJECT.
"""

import argparse
import math
import os
import re
import shutil

from datasets import load_from_disk
from config_validation import load_config, validate_train_config
from dotenv import load_dotenv
from manifest_utils import (
    current_utc_timestamp,
    directory_artifact_manifest,
    read_json_file,
    runtime_manifest,
    safe_git_commit,
    write_json_file,
)


# ── Model + adapter setup ──────────────────────────────────────────────────────

def build_model(cfg: dict):
    """
    Load the base model in 4-bit NF4 precision via Unsloth and attach a
    DoRA + rsLoRA adapter.
    """
    m = cfg["model"]
    l = cfg["lora"]

    # FastLanguageModel patches the HuggingFace model class with Unsloth's
    # optimised CUDA kernels at load time — no code changes required elsewhere.
    from unsloth import FastLanguageModel

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=m["name"],
        max_seq_length=m["max_seq_length"],
        # NF4 uses a 4-bit normal-float data type that matches the distribution
        # of quantised weights much better than int4 / fp4.
        load_in_4bit=m["load_in_4bit"],
        # dtype=None lets Unsloth auto-select bf16 on Ampere+ or fp16 on older
        # GPUs — safest default for the target 16 GB consumer card.
        dtype=m["dtype"],
    )

    model = FastLanguageModel.get_peft_model(
        model,
        # r=16 is the 2026 recommended starting rank: large enough for good
        # task transfer, small enough to fit comfortably in 16 GB VRAM.
        r=l["r"],
        # alpha == r (i.e. effective scale = 1.0) is the rsLoRA guidance.
        # Higher alpha with the same r over-scales gradients and destabilises
        # early training.
        lora_alpha=l["lora_alpha"],
        # Target ALL linear layers in attention AND MLP (not just q/v).
        # Unsloth's own benchmarks show this improves downstream accuracy
        # without meaningful VRAM overhead when using DoRA.
        target_modules=l["target_modules"],
        # lora_dropout=0 is required to enable Unsloth's fused kernel path,
        # which gives the 2× speed-up.  Non-zero dropout falls back to
        # standard PEFT kernels.
        lora_dropout=l["lora_dropout"],
        # bias="none" similarly enables the optimised code path.
        bias=l["bias"],
        # DoRA decomposes the LoRA weight update into magnitude + direction
        # components, empirically improving accuracy by ~3.7 % over standard
        # LoRA on commonsense reasoning benchmarks at no inference cost.
        use_dora=l["use_dora"],
        # rsLoRA re-scales the adapter output by 1/√r rather than 1/r,
        # stabilising gradients when experimenting with higher ranks.
        use_rslora=l["use_rslora"],
        # Unsloth's native gradient checkpointing implementation supports
        # sequences up to 4× the context length of the standard HF
        # implementation — essential for max_seq_length=2048+ on 16 GB VRAM.
        use_gradient_checkpointing="unsloth",
        random_state=cfg["training"]["seed"],
    )

    return model, tokenizer


# ── Tracking initialisation ───────────────────────────────────────────────────────

def _get_tracker(cfg: dict) -> str:
    """
    Return the tracking backend from config.  Defaults to 'tensorboard' for
    fully local, private experiment tracking.  Set privacy.tracking to 'wandb'
    to use Weights & Biases instead (requires WANDB_API_KEY).
    """
    privacy = cfg.get("privacy", {})
    tracker = privacy.get("tracking", "tensorboard")
    if tracker == "wandb":
        try:
            import wandb
            wandb.init(
                project=os.environ.get("WANDB_PROJECT", "simcoe-finetune"),
                config={
                    "model_name": cfg["model"]["name"],
                    "max_seq_length": cfg["model"]["max_seq_length"],
                    "lora_r": cfg["lora"]["r"],
                    "lora_alpha": cfg["lora"]["lora_alpha"],
                    "use_dora": cfg["lora"]["use_dora"],
                    "use_rslora": cfg["lora"]["use_rslora"],
                    **cfg["training"],
                },
                resume="allow",
            )
        except Exception as exc:
            print(f"  ⚠️   W&B init failed ({exc}); falling back to tensorboard.")
            tracker = "tensorboard"
    return tracker


# ── Trainer ────────────────────────────────────────────────────────────────────

def build_trainer(
    model,
    tokenizer,
    train_dataset,
    eval_dataset,
    cfg: dict,
    tracker: str,
) -> "SFTTrainer":
    from trl import SFTConfig, SFTTrainer

    t = cfg["training"]
    m = cfg["model"]

    examples_per_step = (
        t["per_device_train_batch_size"] * t["gradient_accumulation_steps"]
    )
    steps_per_epoch = max(1, math.ceil(len(train_dataset) / examples_per_step))
    total_training_steps = max(1, math.ceil(steps_per_epoch * t["num_train_epochs"]))

    if t.get("warmup_steps") is not None:
        warmup_steps = t["warmup_steps"]
    else:
        warmup_ratio = t.get("warmup_ratio", 0)
        warmup_steps = max(1, math.ceil(total_training_steps * warmup_ratio))

    training_args = SFTConfig(
        output_dir=t["output_dir"],
        per_device_train_batch_size=t["per_device_train_batch_size"],
        # Gradient accumulation makes the effective batch 4 × 4 = 16.
        # Larger effective batches improve gradient estimates and allow a
        # higher learning rate without divergence.
        gradient_accumulation_steps=t["gradient_accumulation_steps"],
        num_train_epochs=t["num_train_epochs"],
        # 2e-4 is the standard QLoRA learning rate from the original QLoRA
        # paper (Dettmers et al. 2023) and still works well with DoRA.
        learning_rate=t["learning_rate"],
        # Cosine schedule decays smoothly to near-zero, reducing the risk of
        # overshooting the optimum at the end of training.
        lr_scheduler_type=t["lr_scheduler_type"],
        # Warm up for a small number of optimizer steps at the start of
        # training. Prefer an explicit warmup_steps config; fall back to a
        # ratio of total training steps for older configs.
        warmup_steps=warmup_steps,
        # bf16 has a wider dynamic range than fp16, reducing overflow/underflow
        # on Ampere+ GPUs.  fp16 is left False to avoid mixed precision issues.
        bf16=t["bf16"],
        fp16=t["fp16"],
        logging_steps=t["logging_steps"],
        save_steps=t["save_steps"],
        save_total_limit=t["save_total_limit"],
        seed=t["seed"],
        # Tracking backend — 'tensorboard' is fully local, no account needed.
        report_to=tracker,
        # Pack short examples together to fill the context window and reduce
        # padding waste — standard practice for instruction fine-tuning.
        dataset_text_field="text",
        max_length=m["max_seq_length"],
        dataset_num_proc=2,
    )

    trainer = SFTTrainer(
        model=model,
        processing_class=tokenizer,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        args=training_args,
    )

    return trainer


def _tracker_name(cfg: dict) -> str:
    privacy = cfg.get("privacy", {})
    return privacy.get("tracking", "tensorboard")


def load_processed_manifest(processed_dir: str) -> dict | None:
    manifest_path = os.path.join(processed_dir, "manifest.json")
    if not os.path.isfile(manifest_path):
        return None
    try:
        return read_json_file(manifest_path)
    except Exception as exc:
        return {
            "path": os.path.abspath(manifest_path),
            "error": str(exc),
        }


def summarise_trainer_state(trainer: SFTTrainer) -> dict:
    state = trainer.state
    log_history = state.log_history or []
    final_log = log_history[-1] if log_history else None

    return {
        "epoch": state.epoch,
        "global_step": state.global_step,
        "max_steps": state.max_steps,
        "num_train_epochs": state.num_train_epochs,
        "best_metric": state.best_metric,
        "best_model_checkpoint": state.best_model_checkpoint,
        "final_log": final_log,
    }


def summarise_trainer_state_dict(state: dict) -> dict:
    log_history = state.get("log_history") or []
    final_log = log_history[-1] if log_history else None
    return {
        "epoch": state.get("epoch"),
        "global_step": state.get("global_step"),
        "max_steps": state.get("max_steps"),
        "num_train_epochs": state.get("num_train_epochs"),
        "best_metric": state.get("best_metric"),
        "best_model_checkpoint": state.get("best_model_checkpoint"),
        "final_log": final_log,
    }


CHECKPOINT_PATTERN = re.compile(r"^checkpoint-(\d+)$")


def find_latest_checkpoint(adapter_dir: str) -> str | None:
    candidates: list[tuple[int, str]] = []
    for entry in os.listdir(adapter_dir):
        match = CHECKPOINT_PATTERN.match(entry)
        if not match:
            continue
        checkpoint_path = os.path.join(adapter_dir, entry)
        if os.path.isdir(checkpoint_path):
            candidates.append((int(match.group(1)), checkpoint_path))

    if not candidates:
        return None

    candidates.sort(key=lambda item: item[0])
    return candidates[-1][1]


def load_existing_trainer_state(adapter_dir: str) -> tuple[dict | None, str | None]:
    trainer_state_path = os.path.join(adapter_dir, "trainer_state.json")
    if os.path.isfile(trainer_state_path):
        return read_json_file(trainer_state_path), trainer_state_path

    latest_checkpoint = find_latest_checkpoint(adapter_dir)
    if latest_checkpoint is None:
        return None, None

    checkpoint_state_path = os.path.join(latest_checkpoint, "trainer_state.json")
    if not os.path.isfile(checkpoint_state_path):
        return None, None

    return read_json_file(checkpoint_state_path), checkpoint_state_path


def reconstruct_train_metrics(trainer_state: dict) -> dict:
    final_log = summarise_trainer_state_dict(trainer_state).get("final_log") or {}
    return {
        "reconstructed_from_existing_artifacts": True,
        "epoch": trainer_state.get("epoch"),
        "global_step": trainer_state.get("global_step"),
        "max_steps": trainer_state.get("max_steps"),
        "num_train_epochs": trainer_state.get("num_train_epochs"),
        "final_logged_loss": final_log.get("loss"),
        "final_logged_learning_rate": final_log.get("learning_rate"),
        "total_flos": trainer_state.get("total_flos"),
    }


def resolve_dataset_counts(processed_dir: str) -> tuple[int, int]:
    processed_manifest = load_processed_manifest(processed_dir)
    counts = processed_manifest.get("counts") if isinstance(processed_manifest, dict) else None
    if isinstance(counts, dict):
        train_rows = counts.get("train_rows")
        valid_rows = counts.get("valid_rows")
        if isinstance(train_rows, int) and isinstance(valid_rows, int):
            return train_rows, valid_rows

    train_dataset = load_from_disk(os.path.join(processed_dir, "train"))
    eval_dataset = load_from_disk(os.path.join(processed_dir, "valid"))
    return len(train_dataset), len(eval_dataset)


def build_training_manifest(
    cfg: dict,
    config_path: str,
    tracker: str,
    processed_dir: str,
    adapter_dir: str,
    train_rows: int,
    valid_rows: int,
    train_metrics: dict,
    trainer_state_summary: dict,
    trainer_state_path: str,
    manifest_mode: str,
    trainer_state_source_path: str | None = None,
) -> dict:
    processed_manifest = load_processed_manifest(processed_dir)

    return {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "git_commit": safe_git_commit(os.getcwd()),
        "config_path": os.path.abspath(config_path),
        "manifest_mode": manifest_mode,
        "tracker": tracker,
        "model": cfg["model"],
        "lora": cfg["lora"],
        "training": cfg["training"],
        "data": {
            "processed_dir": os.path.abspath(processed_dir),
            "train_rows": train_rows,
            "valid_rows": valid_rows,
            "processed_manifest": processed_manifest,
        },
        "runtime": runtime_manifest(
            [
                "torch",
                "transformers",
                "datasets",
                "trl",
                "peft",
                "accelerate",
                "unsloth",
            ]
        ),
        "train_metrics": train_metrics,
        "trainer_state": trainer_state_summary,
        "outputs": {
            "adapter_dir": os.path.abspath(adapter_dir),
            "trainer_state_path": os.path.abspath(trainer_state_path),
            "trainer_state_source_path": (
                os.path.abspath(trainer_state_source_path)
                if trainer_state_source_path
                else os.path.abspath(trainer_state_path)
            ),
            "artifacts": directory_artifact_manifest(adapter_dir),
        },
    }


def write_training_manifest(
    cfg: dict,
    config_path: str,
    tracker: str,
    processed_dir: str,
    adapter_dir: str,
    train_dataset,
    eval_dataset,
    trainer: SFTTrainer,
    train_metrics: dict,
) -> str:
    manifest_path = os.path.join(adapter_dir, "train_manifest.json")
    trainer_state_path = os.path.join(adapter_dir, "trainer_state.json")
    trainer.state.save_to_json(trainer_state_path)

    manifest = build_training_manifest(
        cfg,
        config_path,
        tracker,
        processed_dir,
        adapter_dir,
        len(train_dataset),
        len(eval_dataset),
        train_metrics,
        summarise_trainer_state(trainer),
        trainer_state_path,
        manifest_mode="post_train",
    )
    write_json_file(manifest_path, manifest)
    return manifest_path


def backfill_training_manifest(cfg: dict, config_path: str, tracker: str) -> str:
    processed_dir = cfg["data"]["processed_dir"]
    adapter_dir = cfg["training"]["output_dir"]
    manifest_path = os.path.join(adapter_dir, "train_manifest.json")
    trainer_state, trainer_state_source_path = load_existing_trainer_state(adapter_dir)

    if trainer_state is None or trainer_state_source_path is None:
        raise FileNotFoundError(
            f"No trainer_state.json found in {adapter_dir} or its checkpoint-* subdirectories"
        )

    canonical_trainer_state_path = os.path.join(adapter_dir, "trainer_state.json")
    if os.path.abspath(trainer_state_source_path) != os.path.abspath(canonical_trainer_state_path):
        shutil.copyfile(trainer_state_source_path, canonical_trainer_state_path)

    train_rows, valid_rows = resolve_dataset_counts(processed_dir)
    manifest = build_training_manifest(
        cfg,
        config_path,
        tracker,
        processed_dir,
        adapter_dir,
        train_rows,
        valid_rows,
        reconstruct_train_metrics(trainer_state),
        summarise_trainer_state_dict(trainer_state),
        canonical_trainer_state_path,
        manifest_mode="backfill_existing_artifacts",
        trainer_state_source_path=trainer_state_source_path,
    )
    write_json_file(manifest_path, manifest)
    return manifest_path


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    # Load .env if present (optional — no external secrets required)
    load_dotenv()

    # ── Privacy: block all telemetry before any library import side-effects ──
    os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
    os.environ["DO_NOT_TRACK"] = "1"
    os.environ["WANDB_DISABLED"] = "true"
    os.environ["DISABLE_TELEMETRY"] = "YES"
    os.environ.setdefault("TENSORBOARD_LOGGING_DIR", "logs")

    parser = argparse.ArgumentParser(description="QLoRA fine-tuning with Unsloth.")
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument(
        "--manifest_only",
        action="store_true",
        help="Backfill train_manifest.json from existing adapter and checkpoint artifacts without running training.",
    )
    args = parser.parse_args()

    cfg = load_config(args.config)
    validate_train_config(cfg)

    if args.manifest_only:
        tracker = _tracker_name(cfg)
        manifest_path = backfill_training_manifest(cfg, args.config, tracker)
        print(f"\n🧾  Training manifest written to: {manifest_path}\n")
        return

    # Initialise tracking (TensorBoard by default — fully local)
    tracker = _get_tracker(cfg)
    print(f"\n📊  Tracking: {tracker}")

    print(f"\n🚀  Loading model: {cfg['model']['name']}")
    model, tokenizer = build_model(cfg)

    processed_dir = cfg["data"]["processed_dir"]
    print(f"\n📂  Loading processed datasets from: {processed_dir}")
    train_dataset = load_from_disk(os.path.join(processed_dir, "train"))
    eval_dataset = load_from_disk(os.path.join(processed_dir, "valid"))
    print(f"    Train: {len(train_dataset)} examples")
    print(f"    Valid: {len(eval_dataset)} examples")

    print("\n🏋️  Building trainer …")
    trainer = build_trainer(model, tokenizer, train_dataset, eval_dataset, cfg, tracker)

    print("\n🏋️  Starting training …")
    train_result = trainer.train()

    # Save LoRA adapters (not the full merged model — see scripts/export.py)
    adapter_dir = cfg["training"]["output_dir"]
    os.makedirs(adapter_dir, exist_ok=True)
    print(f"\n💾  Saving LoRA adapters to: {adapter_dir}")
    model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)

    manifest_path = write_training_manifest(
        cfg,
        args.config,
        tracker,
        processed_dir,
        adapter_dir,
        train_dataset,
        eval_dataset,
        trainer,
        train_result.metrics,
    )
    print(f"    Training manifest → {manifest_path}")

    if tracker == "wandb":
        try:
            import wandb
            wandb.finish()
        except Exception:
            pass

    print("\n✅  Training complete.\n")
    if tracker == "tensorboard":
        print("    View training curves:  tensorboard --logdir logs/\n")


if __name__ == "__main__":
    main()
