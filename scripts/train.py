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
import os

import wandb
import yaml
from datasets import load_from_disk
from dotenv import load_dotenv
from trl import SFTTrainer, SFTConfig
from unsloth import FastLanguageModel


# ── Config loading ─────────────────────────────────────────────────────────────

def load_config(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


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


# ── W&B initialisation ─────────────────────────────────────────────────────────

def init_wandb(cfg: dict) -> None:
    """
    Initialise Weights & Biases before the trainer is created so that all
    hyperparameters, system metrics, and training curves are captured from
    the very first step.
    """
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
        # Resume the same run if a checkpoint exists — useful for multi-day
        # training jobs or recovering from an OOM crash.
        resume="allow",
    )


# ── Trainer ────────────────────────────────────────────────────────────────────

def build_trainer(
    model,
    tokenizer,
    train_dataset,
    eval_dataset,
    cfg: dict,
) -> SFTTrainer:
    t = cfg["training"]
    m = cfg["model"]

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
        # 5 % warmup prevents gradient explosion in the first few steps when
        # the adapter weights are still far from their converged values.
        warmup_ratio=t["warmup_ratio"],
        # bf16 has a wider dynamic range than fp16, reducing overflow/underflow
        # on Ampere+ GPUs.  fp16 is left False to avoid mixed precision issues.
        bf16=t["bf16"],
        fp16=t["fp16"],
        logging_steps=t["logging_steps"],
        save_steps=t["save_steps"],
        save_total_limit=t["save_total_limit"],
        seed=t["seed"],
        # W&B integration — logs loss, learning rate, and grad norm automatically
        # when wandb has been initialised before this point.
        report_to="wandb",
        # Pack short examples together to fill the context window and reduce
        # padding waste — standard practice for instruction fine-tuning.
        dataset_text_field="text",
        max_seq_length=m["max_seq_length"],
        dataset_num_proc=2,
    )

    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        args=training_args,
    )

    return trainer


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    # Load secrets from .env (HF_TOKEN, WANDB_API_KEY, WANDB_PROJECT)
    load_dotenv()

    parser = argparse.ArgumentParser(description="QLoRA fine-tuning with Unsloth.")
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)

    # Initialise W&B before the trainer so all config is captured
    init_wandb(cfg)

    print(f"\n🚀  Loading model: {cfg['model']['name']}")
    model, tokenizer = build_model(cfg)

    processed_dir = cfg["data"]["processed_dir"]
    print(f"\n📂  Loading processed datasets from: {processed_dir}")
    train_dataset = load_from_disk(os.path.join(processed_dir, "train"))
    eval_dataset = load_from_disk(os.path.join(processed_dir, "valid"))
    print(f"    Train: {len(train_dataset)} examples")
    print(f"    Valid: {len(eval_dataset)} examples")

    print("\n🏋️  Building trainer …")
    trainer = build_trainer(model, tokenizer, train_dataset, eval_dataset, cfg)

    print("\n🏋️  Starting training …")
    trainer.train()

    # Save LoRA adapters (not the full merged model — see scripts/export.py)
    adapter_dir = cfg["training"]["output_dir"]
    os.makedirs(adapter_dir, exist_ok=True)
    print(f"\n💾  Saving LoRA adapters to: {adapter_dir}")
    model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)

    wandb.finish()
    print("\n✅  Training complete.\n")


if __name__ == "__main__":
    main()
