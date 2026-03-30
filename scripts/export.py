"""
scripts/export.py
─────────────────
Merge LoRA adapters into the base model and export in two formats:

  1.  16-bit merged weights → for vLLM / HuggingFace serving.
  2.  Q4_K_M GGUF → for Ollama / llama.cpp local inference.
      A Modelfile is also generated so the model can be registered with Ollama
      in a single command.

Usage:
    python scripts/export.py [--config config.yaml]

Prerequisites:
    • LoRA adapters must exist at models/adapters/ (run scripts/train.py first).
    • Unsloth must be installed.
"""

import argparse
import os
import subprocess
import sys

from config_validation import load_config, validate_export_config
from unsloth import FastLanguageModel


# ── Load model + adapters ─────────────────────────────────────────────────────

def load_finetuned(cfg: dict):
    """
    Re-load the base model and reattach the saved LoRA adapters.
    We load in 4-bit here to keep VRAM usage low; the merge step will
    up-cast to 16-bit automatically when saving.
    """
    m = cfg["model"]
    adapter_dir = cfg["training"]["output_dir"]

    print(f"  Loading base model: {m['name']}")
    print(f"  Attaching adapters: {adapter_dir}")

    model, tokenizer = FastLanguageModel.from_pretrained(
        # Pass the adapter directory as model_name — Unsloth reads the base
        # model identifier from adapter_config.json inside that directory and
        # loads both the base weights and the adapter in one call.
        model_name=adapter_dir,
        max_seq_length=m["max_seq_length"],
        load_in_4bit=m["load_in_4bit"],
        dtype=m["dtype"],
    )
    return model, tokenizer


# ── 16-bit merged export ──────────────────────────────────────────────────────

def export_merged_16bit(model, tokenizer, out_dir: str) -> None:
    """
    Merge adapter weights into the base model and save in bfloat16.
    This format is ready for vLLM serving with --dtype bfloat16.
    """
    os.makedirs(out_dir, exist_ok=True)
    print(f"\n  Merging and saving 16-bit model → {out_dir}")
    model.save_pretrained_merged(
        out_dir,
        tokenizer,
        save_method="merged_16bit",
    )
    print(f"  ✅  16-bit merged model saved to: {out_dir}")


# ── GGUF export ───────────────────────────────────────────────────────────────

def _find_gguf_files(gguf_dir: str) -> list[str]:
    if not os.path.isdir(gguf_dir):
        return []
    return sorted(
        os.path.join(gguf_dir, filename)
        for filename in os.listdir(gguf_dir)
        if filename.endswith(".gguf")
    )


def _export_gguf_with_llama_cpp(merged_dir: str, gguf_dir: str, quantisation: str) -> str:
    llama_cpp_dir = os.environ.get(
        "LLAMA_CPP_DIR",
        os.path.expanduser("~/src/llama.cpp"),
    )
    convert_script = os.path.join(llama_cpp_dir, "convert_hf_to_gguf.py")
    quantize_bin = os.path.join(llama_cpp_dir, "build", "bin", "llama-quantize")

    if not os.path.isfile(convert_script) or not os.path.isfile(quantize_bin):
        raise FileNotFoundError(
            "llama.cpp conversion tools not found. Set LLAMA_CPP_DIR or install "
            "convert_hf_to_gguf.py and llama-quantize."
        )

    os.makedirs(gguf_dir, exist_ok=True)
    f16_path = os.path.join(gguf_dir, "model-f16.gguf")
    quantized_path = os.path.join(gguf_dir, f"model-{quantisation.upper()}.gguf")

    print("  Falling back to llama.cpp conversion …")
    subprocess.run(
        [
            sys.executable,
            convert_script,
            merged_dir,
            "--outfile",
            f16_path,
            "--outtype",
            "f16",
        ],
        check=True,
    )
    subprocess.run(
        [quantize_bin, f16_path, quantized_path, quantisation.upper()],
        check=True,
    )

    if os.path.isfile(f16_path):
        os.remove(f16_path)

    return quantized_path

def export_gguf(
    model,
    tokenizer,
    merged_dir: str,
    gguf_dir: str,
    quantisation: str,
) -> str:
    """
    Export the merged model as a GGUF file using the specified quantisation
    level.  Q4_K_M offers an excellent size / quality trade-off for Ollama
    and llama.cpp inference on consumer hardware.

    Returns the path to the generated GGUF file.
    """
    os.makedirs(gguf_dir, exist_ok=True)
    print(f"\n  Exporting GGUF ({quantisation.upper()}) → {gguf_dir}")
    try:
        model.save_pretrained_gguf(
            gguf_dir,
            tokenizer,
            quantization_method=quantisation,
        )
    except Exception as exc:
        print(f"  ⚠️   Unsloth GGUF export failed ({exc})")
        gguf_path = _export_gguf_with_llama_cpp(merged_dir, gguf_dir, quantisation)
        print(f"  ✅  GGUF file saved to: {gguf_path}")
        return gguf_path

    gguf_files = _find_gguf_files(gguf_dir)
    if gguf_files:
        print(f"  ✅  GGUF file saved to: {gguf_files[0]}")
        return gguf_files[0]

    print("  ⚠️   Unsloth GGUF export produced no .gguf file in the target directory.")
    gguf_path = _export_gguf_with_llama_cpp(merged_dir, gguf_dir, quantisation)
    print(f"  ✅  GGUF file saved to: {gguf_path}")
    return gguf_path


# ── Ollama Modelfile generation ───────────────────────────────────────────────

def generate_modelfile(gguf_path: str, modelfile_path: str, cfg: dict) -> None:
    """
    Write an Ollama Modelfile that points to the exported GGUF.

    Register the model with Ollama:
        ollama create simcoe -f models/gguf/Modelfile

    Then run inference:
        ollama run simcoe "Your prompt here"
    """
    if not os.path.isfile(gguf_path):
        raise FileNotFoundError(f"GGUF file not found: {gguf_path}")

    model_name = cfg["model"]["name"].split("/")[-1]
    max_seq_length = cfg["model"]["max_seq_length"]

    modelfile_content = (
        f"# Modelfile generated by scripts/export.py\n"
        f"# Register with: ollama create {model_name} -f {modelfile_path}\n\n"
        f"FROM {os.path.abspath(gguf_path)}\n\n"
        f"PARAMETER num_ctx {max_seq_length}\n"
        f"PARAMETER stop \"### Instruction:\"\n"
        f"PARAMETER stop \"### Response:\"\n\n"
        f"TEMPLATE \"\"\"\n"
        f"{{{{ if .System }}}}### System:\n{{{{ .System }}}}\n\n{{{{ end }}}}"
        f"### Instruction:\n{{{{ .Prompt }}}}\n\n"
        f"### Response:\n{{{{ .Response }}}}\"\"\"\n\n"
        f"SYSTEM \"\"\"\n"
        f"You are a helpful AI assistant fine-tuned on domain-specific data.\n"
        f"\"\"\"\n"
    )

    os.makedirs(os.path.dirname(modelfile_path), exist_ok=True)
    with open(modelfile_path, "w") as f:
        f.write(modelfile_content)

    print(f"\n  ✅  Ollama Modelfile written to: {modelfile_path}")
    print(f"  To register: ollama create {model_name} -f {modelfile_path}")
    print(f"  To run:      ollama run {model_name}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Merge and export the fine-tuned model.")
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)
    validate_export_config(cfg)
    exp = cfg["export"]

    print("\n🔧  Loading fine-tuned model and adapters …")
    model, tokenizer = load_finetuned(cfg)

    # ── 16-bit merged export (for vLLM) ───────────────────────────────────────
    merged_dir = exp["merged_16bit_dir"]
    export_merged_16bit(model, tokenizer, merged_dir)

    # ── GGUF export (for Ollama / llama.cpp) ──────────────────────────────────
    try:
        gguf_path = export_gguf(
            model,
            tokenizer,
            merged_dir,
            exp["gguf_dir"],
            exp["gguf_quantisation"],
        )
    except Exception as exc:
        print(f"\n  ⚠️   GGUF export failed: {exc}")
        print("  The 16-bit merged model is still available for inference.")
        print("  To retry GGUF export later, install llama.cpp and re-run this script.")
        gguf_path = None

    # ── Ollama Modelfile ───────────────────────────────────────────────────────
    if gguf_path:
        generate_modelfile(gguf_path, exp["ollama_modelfile"], cfg)

    print("\n✅  Export complete.\n")


if __name__ == "__main__":
    main()
