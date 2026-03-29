"""
scripts/check_env.py
────────────────────
Pre-flight environment validator.  Run this before attempting any training to
surface version mismatches early — the single most common cause of silent
failures in a WSL2 / CUDA 12.x stack.

Usage:
    python scripts/check_env.py
"""

import sys
import importlib


# ── Helpers ───────────────────────────────────────────────────────────────────

def _pass(msg: str) -> None:
    print(f"  ✅  {msg}")


def _fail(msg: str) -> None:
    print(f"  ❌  {msg}")


def _warn(msg: str) -> None:
    print(f"  ⚠️   {msg}")


def _section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")


# ── Checks ────────────────────────────────────────────────────────────────────

def check_python() -> bool:
    major, minor = sys.version_info[:2]
    ok = major == 3 and minor >= 11
    msg = f"Python {major}.{minor} (need 3.11+)"
    _pass(msg) if ok else _fail(msg)
    return ok


def check_torch() -> bool:
    try:
        import torch
        ok = True
        _pass(f"PyTorch {torch.__version__}")
    except ImportError:
        _fail("PyTorch not installed")
        return False

    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        vram_gb = torch.cuda.get_device_properties(0).total_memory / 1e9
        _pass(f"CUDA available  —  {gpu_name}  ({vram_gb:.1f} GB VRAM)")

        # Warn if VRAM is below 12 GB — QLoRA on an 8B model is tight below that.
        if vram_gb < 12:
            _warn(
                f"Only {vram_gb:.1f} GB VRAM detected.  "
                "QLoRA on an 8B model requires ~12 GB minimum."
            )
        elif vram_gb < 16:
            _warn(
                f"{vram_gb:.1f} GB VRAM — should be sufficient for 4-bit QLoRA "
                "with batch_size=4, but monitor usage carefully."
            )

        # CUDA version
        cuda_ver = torch.version.cuda or "unknown"
        if cuda_ver.startswith("12"):
            _pass(f"CUDA {cuda_ver}")
        else:
            _warn(
                f"CUDA {cuda_ver} detected — this project targets CUDA 12.x.  "
                "Dependency versions may need adjustment."
            )
    else:
        _fail(
            "CUDA is NOT available.  "
            "Training will fall back to CPU and be extremely slow."
        )
        ok = False

    return ok


def check_package(pkg_name: str, import_name: str | None = None) -> bool:
    """Return True if the package can be imported."""
    import_name = import_name or pkg_name
    try:
        mod = importlib.import_module(import_name)
        version = getattr(mod, "__version__", "unknown")
        _pass(f"{pkg_name} {version}")
        return True
    except ImportError as exc:
        _fail(f"{pkg_name} not installed — {exc}")
        return False


def check_bitsandbytes() -> bool:
    try:
        import bitsandbytes as bnb
        _pass(f"bitsandbytes {bnb.__version__}")

        # Quick functional check — bnb raises at import time on CUDA mismatch,
        # but an explicit cuda_setup check is more informative.
        try:
            from bitsandbytes.cuda_setup.main import get_cuda_lib_handle  # noqa: F401
        except Exception:
            pass  # older bnb versions don't expose this; skip silently

        return True
    except ImportError as exc:
        _fail(f"bitsandbytes not installed — {exc}")
        return False
    except Exception as exc:
        _warn(f"bitsandbytes installed but CUDA setup may be broken: {exc}")
        return False


def check_unsloth() -> bool:
    try:
        import unsloth  # noqa: F401
        version = getattr(unsloth, "__version__", "unknown")
        _pass(f"unsloth {version}")
        return True
    except ImportError as exc:
        _fail(f"unsloth not installed — {exc}")
        _warn(
            "Install with:  "
            "pip install unsloth[colab-new] @ https://github.com/unslothai/unsloth"
        )
        return False
    except Exception as exc:
        _warn(f"unsloth installed but raised an error on import: {exc}")
        return False


def check_env_vars() -> bool:
    import os
    ok = True
    # These are optional — the pipeline runs fully locally without any of them.
    for var, note in [
        ("HF_TOKEN", "needed only for gated HF models — Unsloth models are ungated"),
        ("WANDB_API_KEY", "needed only if privacy.tracking is set to 'wandb'"),
        ("WANDB_PROJECT", "needed only if privacy.tracking is set to 'wandb'"),
    ]:
        if os.environ.get(var):
            _pass(f"{var} is set")
        else:
            _warn(f"{var} not set — {note}")
            ok = False
    return ok


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    # Load .env if present
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    results: list[bool] = []

    _section("Python version")
    results.append(check_python())

    _section("PyTorch & CUDA")
    results.append(check_torch())

    _section("Hugging Face stack")
    for pkg, imp in [
        ("transformers", None),
        ("datasets", None),
        ("peft", None),
        ("trl", None),
        ("accelerate", None),
        ("huggingface_hub", None),
    ]:
        results.append(check_package(pkg, imp))

    _section("Quantisation")
    results.append(check_bitsandbytes())

    _section("Unsloth")
    results.append(check_unsloth())

    _section("Experiment tracking & evaluation")
    for pkg in ("wandb", "evaluate", "deepeval"):
        results.append(check_package(pkg))

    _section("Environment variables (.env)")
    check_env_vars()  # warnings only — don't count as hard failure

    print("\n" + "═" * 60)
    failures = results.count(False)
    if failures == 0:
        print("  🎉  All checks passed — environment looks good!")
    else:
        print(f"  ⚠️   {failures} check(s) failed — resolve the issues above before training.")
    print("═" * 60 + "\n")

    sys.exit(0 if failures == 0 else 1)


if __name__ == "__main__":
    main()
