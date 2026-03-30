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
import shutil
import subprocess
import sys
import time

from config_validation import load_config, validate_export_config
from manifest_utils import (
    current_utc_timestamp,
    directory_artifact_manifest,
    read_json_file,
    runtime_manifest,
    safe_git_commit,
    write_json_file,
)
import requests


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

    from unsloth import FastLanguageModel

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


def load_training_manifest(adapter_dir: str) -> dict | None:
    manifest_path = os.path.join(adapter_dir, "train_manifest.json")
    if not os.path.isfile(manifest_path):
        return None
    try:
        return read_json_file(manifest_path)
    except Exception as exc:
        return {
            "path": os.path.abspath(manifest_path),
            "error": str(exc),
        }


def resolve_smoke_test_settings(cfg: dict) -> dict:
    release = cfg.get("release", {}) if isinstance(cfg.get("release"), dict) else {}
    prompt = release.get(
        "smoke_test_prompt",
        "In one sentence, explain why grounding and bonding matter in electrical work.",
    )
    max_new_tokens = int(release.get("smoke_test_max_new_tokens", 48))
    min_response_chars = int(release.get("smoke_test_min_response_chars", 40))
    model_name = release.get("ollama_model_name", "simcoe-smoke")
    return {
        "prompt": prompt,
        "max_new_tokens": max_new_tokens,
        "min_response_chars": min_response_chars,
        "require_merged_smoke_test": bool(release.get("require_merged_smoke_test", False)),
        "require_gguf_smoke_test": bool(release.get("require_gguf_smoke_test", False)),
        "ollama_model_name": model_name,
    }


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


def _build_generation_config(tokenizer, max_new_tokens: int):
    from transformers import GenerationConfig

    generation_config = GenerationConfig()
    generation_config.max_new_tokens = max_new_tokens
    generation_config.do_sample = False
    generation_config.pad_token_id = tokenizer.pad_token_id or tokenizer.eos_token_id
    generation_config.eos_token_id = tokenizer.eos_token_id
    generation_config.max_length = None
    generation_config.temperature = None
    generation_config.top_p = None
    return generation_config


def _run_merged_smoke_test(merged_dir: str, prompt: str, max_new_tokens: int) -> str:
    from tokenizer_utils import load_tokenizer_with_compat
    from transformers import AutoModelForCausalLM, pipeline

    tokenizer = load_tokenizer_with_compat(merged_dir)
    if tokenizer.pad_token_id is None and tokenizer.eos_token_id is not None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    model = AutoModelForCausalLM.from_pretrained(
        merged_dir,
        device_map="auto",
        torch_dtype="auto",
        trust_remote_code=True,
    )
    gen_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
    generation_config = _build_generation_config(tokenizer, max_new_tokens)
    formatted_prompt = f"### Instruction:\n{prompt}\n\n### Response:"
    output = gen_pipeline([formatted_prompt], generation_config=generation_config, batch_size=1)
    generated_text = output[0][0]["generated_text"]
    parts = generated_text.split("### Response:")
    return parts[-1].strip() if len(parts) >= 2 else generated_text.strip()


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


def _run_gguf_smoke_test(
    modelfile_path: str,
    model_name: str,
    prompt: str,
    max_new_tokens: int,
) -> str:
    ollama = _ollama_binary()
    if not ollama or not os.path.exists(ollama):
        raise FileNotFoundError("Ollama binary not found")

    server_process = _ensure_ollama_server()

    subprocess.run([ollama, "create", model_name, "-f", modelfile_path], check=True)
    try:
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": model_name,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": max_new_tokens,
                    "temperature": 0,
                },
            },
            timeout=300,
        )
        response.raise_for_status()
        payload = response.json()
        return str(payload.get("response", "")).strip()
    finally:
        subprocess.run([ollama, "rm", model_name], check=False)
        if server_process is not None:
            server_process.terminate()
            try:
                server_process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                server_process.kill()
                server_process.wait(timeout=10)


def _assert_smoke_response(response: str, min_response_chars: int, label: str) -> None:
    if not response.strip():
        raise RuntimeError(f"{label} smoke test produced an empty response")
    if len(response.strip()) < min_response_chars:
        raise RuntimeError(
            f"{label} smoke test response too short ({len(response.strip())} chars < {min_response_chars})"
        )


def run_smoke_tests(cfg: dict, merged_dir: str, gguf_path: str | None, modelfile_path: str) -> dict:
    settings = resolve_smoke_test_settings(cfg)
    results: dict[str, dict] = {}

    if settings["require_merged_smoke_test"]:
        start = time.perf_counter()
        merged_response = _run_merged_smoke_test(
            merged_dir,
            settings["prompt"],
            settings["max_new_tokens"],
        )
        _assert_smoke_response(
            merged_response,
            settings["min_response_chars"],
            "Merged model",
        )
        results["merged"] = {
            "required": True,
            "passed": True,
            "response_preview": merged_response[:240],
            "elapsed_sec": round(time.perf_counter() - start, 4),
        }
    else:
        results["merged"] = {
            "required": False,
            "passed": None,
            "status": "skipped",
        }

    if settings["require_gguf_smoke_test"]:
        if gguf_path is None or not os.path.isfile(gguf_path):
            raise FileNotFoundError("GGUF smoke test required but no GGUF artifact is available")

        start = time.perf_counter()
        gguf_response = _run_gguf_smoke_test(
            modelfile_path,
            settings["ollama_model_name"],
            settings["prompt"],
            settings["max_new_tokens"],
        )
        _assert_smoke_response(
            gguf_response,
            settings["min_response_chars"],
            "GGUF model",
        )
        results["gguf"] = {
            "required": True,
            "passed": True,
            "response_preview": gguf_response[:240],
            "elapsed_sec": round(time.perf_counter() - start, 4),
            "model_name": settings["ollama_model_name"],
        }
    else:
        results["gguf"] = {
            "required": False,
            "passed": None,
            "status": "skipped",
        }

    return results


def write_export_manifest(
    cfg: dict,
    config_path: str,
    merged_dir: str,
    gguf_dir: str,
    gguf_path: str | None,
    smoke_tests: dict,
    timings: dict,
) -> str:
    adapter_dir = cfg["training"]["output_dir"]
    manifest_path = os.path.join(merged_dir, "export_manifest.json")
    manifest = {
        "schema_version": 1,
        "generated_at": current_utc_timestamp(),
        "git_commit": safe_git_commit(os.getcwd()),
        "config_path": os.path.abspath(config_path),
        "training_manifest": load_training_manifest(adapter_dir),
        "runtime": runtime_manifest(["torch", "transformers", "requests", "unsloth"]),
        "model": cfg["model"],
        "export": cfg["export"],
        "outputs": {
            "merged_dir": os.path.abspath(merged_dir),
            "gguf_dir": os.path.abspath(gguf_dir),
            "gguf_path": os.path.abspath(gguf_path) if gguf_path else None,
            "merged_artifacts": directory_artifact_manifest(merged_dir),
            "gguf_artifacts": directory_artifact_manifest(gguf_dir),
        },
        "smoke_tests": smoke_tests,
        "timings_sec": timings,
    }
    write_json_file(manifest_path, manifest)
    return manifest_path


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
    parser.add_argument(
        "--verify_existing",
        action="store_true",
        help="Skip export and only validate existing merged/GGUF artifacts, manifests, and smoke tests.",
    )
    args = parser.parse_args()

    cfg = load_config(args.config)
    validate_export_config(cfg)
    exp = cfg["export"]
    timings: dict[str, float] = {}

    # ── 16-bit merged export (for vLLM) ───────────────────────────────────────
    merged_dir = exp["merged_16bit_dir"]
    gguf_path: str | None = None

    if not args.verify_existing:
        print("\n🔧  Loading fine-tuned model and adapters …")
        load_start = time.perf_counter()
        model, tokenizer = load_finetuned(cfg)
        timings["load_finetuned"] = round(time.perf_counter() - load_start, 4)

        merge_start = time.perf_counter()
        export_merged_16bit(model, tokenizer, merged_dir)
        timings["export_merged_16bit"] = round(time.perf_counter() - merge_start, 4)

        # ── GGUF export (for Ollama / llama.cpp) ──────────────────────────────────
        try:
            gguf_start = time.perf_counter()
            gguf_path = export_gguf(
                model,
                tokenizer,
                merged_dir,
                exp["gguf_dir"],
                exp["gguf_quantisation"],
            )
            timings["export_gguf"] = round(time.perf_counter() - gguf_start, 4)
        except Exception as exc:
            print(f"\n  ⚠️   GGUF export failed: {exc}")
            print("  The 16-bit merged model is still available for inference.")
            print("  To retry GGUF export later, install llama.cpp and re-run this script.")
            gguf_path = None
    else:
        print("\n🔎  Verifying existing export artifacts …")
        gguf_files = _find_gguf_files(exp["gguf_dir"])
        gguf_path = gguf_files[0] if gguf_files else None

    # ── Ollama Modelfile ───────────────────────────────────────────────────────
    if gguf_path:
        generate_modelfile(gguf_path, exp["ollama_modelfile"], cfg)

    smoke_start = time.perf_counter()
    smoke_tests = run_smoke_tests(
        cfg,
        merged_dir,
        gguf_path,
        exp["ollama_modelfile"],
    )
    timings["smoke_tests"] = round(time.perf_counter() - smoke_start, 4)

    manifest_path = write_export_manifest(
        cfg,
        args.config,
        merged_dir,
        exp["gguf_dir"],
        gguf_path,
        smoke_tests,
        timings,
    )
    print(f"  Export manifest → {manifest_path}")

    print("\n✅  Export complete.\n")


if __name__ == "__main__":
    main()
