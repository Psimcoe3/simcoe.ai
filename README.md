# simcoe.ai — Local LLM Fine-Tuning Pipeline

A production-ready 4-bit QLoRA fine-tuning pipeline for 7B/8B language models,
designed to run on a single NVIDIA GPU (16 GB VRAM) inside WSL2 on Windows.

Built on **2026 best practices**: Unsloth optimised kernels, DoRA + rsLoRA
adapters, Weights & Biases experiment tracking, GGUF export for Ollama inference,
and fully automated evaluation.

---

## Table of Contents

1. [Quickstart](#quickstart)
2. [Project Structure](#project-structure)
3. [Environment Setup — WSL2 & CUDA 12.x](#environment-setup--wsl2--cuda-12x)
4. [Configuration](#configuration)
5. [Pipeline Walkthrough](#pipeline-walkthrough)
6. [What Else Would I Do Next?](#what-else-would-i-do-next)
7. [LoRA vs QLoRA vs Full Fine-Tuning](#lora-vs-qlora-vs-full-fine-tuning)

---

## Quickstart

```bash
# 1. Clone and enter the repo
git clone https://github.com/Psimcoe3/simcoe.ai.git
cd simcoe.ai

# 2. Create a virtual environment (Python 3.11+)
python3.11 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies (GPU-specific Unsloth wheel — see Environment Setup)
pip install -r requirements.txt

# 4. Configure secrets
cp .env.example .env
# Edit .env and add HF_TOKEN, WANDB_API_KEY, WANDB_PROJECT, OPENAI_API_KEY

# 5. Validate the environment
python scripts/check_env.py

# 6. Prepare your data  (JSONL file → data/raw/dataset.jsonl)
python scripts/prepare_data.py

# 7. Fine-tune
python scripts/train.py

# 8. Export (16-bit for vLLM + GGUF for Ollama)
python scripts/export.py

# 9. Evaluate
python scripts/evaluate.py
```

Or run the entire pipeline in one command:

```bash
make all
```

---

## Project Structure

```
simcoe.ai/
├── config.yaml            # All hyperparameters — nothing hardcoded in scripts
├── Makefile               # Pipeline orchestration (make all, make train, etc.)
├── topics.yaml            # Topic definitions for synthetic data generation
├── .env.example           # Secret template (copy to .env, never commit .env)
├── requirements.txt       # Pinned dependency versions for CUDA 12.x
│
├── data/
│   ├── raw/               # Place your dataset.jsonl here (seed dataset included)
│   └── processed/         # Train/validation Arrow datasets (auto-generated)
│
├── models/
│   ├── adapters/          # Saved LoRA / DoRA adapter weights
│   ├── merged_16bit/      # Merged model in bfloat16 (for vLLM)
│   └── gguf/              # Q4_K_M GGUF + Ollama Modelfile
│
├── scripts/
│   ├── check_env.py       # Pre-flight validator
│   ├── config_validation.py # Shared config/prerequisite validation
│   ├── generate_data.py   # Synthetic data generation via OpenAI API
│   ├── prepare_data.py    # JSONL → formatted + split dataset
│   ├── train.py           # QLoRA training with Unsloth + SFTTrainer
│   ├── export.py          # Merge adapters → 16-bit + GGUF
│   └── evaluate.py        # ROUGE / exact match / LLM-as-judge
│
├── evals/
│   └── results.json       # Evaluation output (auto-generated)
│
└── logs/                  # W&B local artefacts (gitignored)
```

---

## Environment Setup — WSL2 & CUDA 12.x

### Prerequisites

- Windows 11 with WSL2 enabled
- Ubuntu 22.04 LTS (recommended) in WSL2
- NVIDIA GPU with 16 GB VRAM (RTX 3090 / 4080 / 4090 / A4000 or better)
- NVIDIA drivers ≥ 535 on the Windows host (CUDA 12.x is surfaced into WSL2 automatically)

### Step 1 — Verify CUDA in WSL2

```bash
nvidia-smi          # should show your GPU and CUDA 12.x
nvcc --version      # should show CUDA 12.x
```

If `nvidia-smi` works but `nvcc` is missing:

```bash
sudo apt-get install -y cuda-toolkit-12-4
echo 'export PATH=/usr/local/cuda-12.4/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Step 2 — Python 3.11

```bash
sudo apt-get install -y python3.11 python3.11-venv python3.11-dev
```

### Step 3 — PyTorch with CUDA 12

```bash
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==0.20.1 \
    --index-url https://download.pytorch.org/whl/cu124
```

### Step 4 — Unsloth (GPU-specific wheel)

Unsloth publishes pre-built wheels for each CUDA/Torch combination.
Replace `cu124` with your actual CUDA version (e.g. `cu121`, `cu124`).

```bash
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
# OR use the PyPI wheel:
pip install unsloth==2024.12.4
```

> **Tip:** If you get a `bitsandbytes` CUDA error on WSL2, reinstall with:
> `pip install bitsandbytes==0.45.0 --prefer-binary`

### Step 5 — Remaining dependencies

```bash
pip install -r requirements.txt
```

### Step 6 — Configure secrets

```bash
cp .env.example .env
# Open .env and fill in HF_TOKEN, WANDB_API_KEY, WANDB_PROJECT
```

### Step 7 — Validate

```bash
python scripts/check_env.py
```

---

## Configuration

All hyperparameters live in **`config.yaml`** at the project root.
Edit that file instead of touching the scripts.

Key sections:

| Section | Key settings |
|---------|-------------|
| `model` | `name`, `max_seq_length`, `load_in_4bit` |
| `lora`  | `r`, `lora_alpha`, `target_modules`, `use_dora`, `use_rslora` |
| `training` | `learning_rate`, `num_train_epochs`, `per_device_train_batch_size` |
| `data`  | `raw_path`, `validation_split`, `random_state` |
| `export` | `gguf_quantisation`, output directories |
| `evaluation` | `judge_model`, `results_path` |

---

## Pipeline Walkthrough

### 1. Prepare data (`scripts/prepare_data.py`)

- Loads a JSONL file where each line is `{"instruction": "...", "input": "...", "response": "..."}`.
- Fails early on invalid JSON, blank lines, missing `instruction`, or missing `response`/`output` fields.
- Formats into an Alpaca-style instruction template.
- Splits 90 % / 10 % (train / validation) using `random_state=3407`.
- Validates that no example exceeds `max_seq_length` tokens and drops over-length examples.
- Saves Arrow datasets to `data/processed/`.

### 2. Train (`scripts/train.py`)

- Fails early if processed datasets are missing, required config fields are invalid, or `HF_TOKEN` / `WANDB_API_KEY` / `WANDB_PROJECT` are unset.
- Loads the base model in 4-bit NF4 via Unsloth's `FastLanguageModel`.
- Applies a DoRA + rsLoRA adapter with `r=16, lora_alpha=16` targeting all linear layers.
- Initialises Weights & Biases for loss, learning rate, and gradient norm tracking.
- Trains with `SFTTrainer` (cosine LR schedule, warmup 5 %, bfloat16).
- Saves LoRA adapters to `models/adapters/`.

### 3. Export (`scripts/export.py`)

- Fails early if adapter artifacts are missing or export-related config values are invalid.
- Merges adapters into the base model at bfloat16 precision (→ `models/merged_16bit/`).
- Quantises to Q4_K_M GGUF (→ `models/gguf/`).
- Writes an Ollama `Modelfile` for one-command registration.

### 4. Evaluate (`scripts/evaluate.py`)

- Fails early if the merged model, processed validation set, or evaluation config is missing.
- Loads the merged model and runs inference on the validation set.
- Scores outputs with ROUGE-1/2/L and exact match.
- LLM-as-judge scoring via OpenAI API (set `evaluation.judge_model` in `config.yaml`; requires `OPENAI_API_KEY`).
  Rates each response 1–5 with a structured rationale.
  Set `judge_model: null` to disable.
- Saves results to `evals/results.json`.

---

## Makefile

The Makefile orchestrates the pipeline in the correct order:

```bash
make all          # check → prepare → train → export → evaluate
make check        # validate environment only
make prepare      # prepare dataset only
make train        # fine-tune (requires prepared data)
make export       # export (requires trained adapters)
make evaluate     # evaluate (requires exported model)
make clean        # remove all generated artifacts
make help         # show all targets
```

Override the config file: `make all CONFIG=my_config.yaml`

---

## Synthetic Data Generation

`scripts/generate_data.py` uses an OpenAI-compatible API to generate training
examples from topic descriptions.

```bash
# Generate 20 examples per topic
python scripts/generate_data.py --topics topics.yaml --out data/raw/generated.jsonl --count 20

# Merge into the main dataset
cat data/raw/generated.jsonl >> data/raw/dataset.jsonl

## Public Source Ingestion

The repo also supports collecting public manufacturer, wage, and industry
reference pages before converting them into training examples.

```bash
# Scrape configured public sources
make scrape-public

# Convert scraped records into JSONL training examples
python scripts/build_catalog_data.py \
   --source data/raw/public_scrape.jsonl \
   --out data/raw/public_catalog_examples.jsonl
```

Current source coverage in [sources/public_sources.yaml](sources/public_sources.yaml)
includes material manufacturers such as ABB, nVent HOFFMAN, Atkore, Leviton,
Hubbell, and Legrand, plus public reference sources such as BLS OEWS,
California DIR prevailing wage pages, and Electrical Contractor Magazine.
```

Edit `topics.yaml` to define your domains. The included topics cover:
- NEC Code (general requirements + special occupancies)
- Massachusetts amendments (527 CMR)
- Electrical theory and apprentice training
- Software design patterns
- Software architecture and DevOps

### Seed Dataset

A 32-example seed dataset is included at `data/raw/dataset.jsonl` covering all
four target domains. Use it to verify the pipeline end-to-end before scaling up
with `generate_data.py`.

---

## What Else Would I Do Next?

If I were taking this project beyond the initial pipeline, the next high-leverage
improvements would be:

1. **Add CI smoke checks** so every PR validates YAML parsing, script imports,
   and basic CLI help output before changes are merged.
2. ~~**Ship a tiny example dataset**~~ ✅ Done — 32-example seed dataset at `data/raw/dataset.jsonl`.
3. ~~**Replace the LLM-as-judge stub**~~ ✅ Done — real OpenAI-based judge in `scripts/evaluate.py`.
4. ~~**Add config validation**~~ ✅ Done — shared `scripts/config_validation.py` used by all pipeline scripts.
5. **Document inference workflows** for both Hugging Face/vLLM and Ollama so
   users can move from export to local serving without guessing the next step.
6. **Scale the dataset** using `scripts/generate_data.py` to reach 500–2000+
   examples before production fine-tuning.

---

## LoRA vs QLoRA vs Full Fine-Tuning

| Method | VRAM | Speed | When to use |
|--------|------|-------|-------------|
| **Full fine-tuning** | 80 GB+ (for 7B) | Slowest | You have a large high-quality dataset and multi-GPU hardware; you need maximum task performance |
| **LoRA** | ~24 GB (for 7B in fp16) | Fast | You have a moderate dataset and a 24 GB GPU; you want better accuracy than QLoRA without the quantisation noise |
| **QLoRA (4-bit)** | ~10–14 GB (for 7B/8B) | Fast | You have a 16 GB consumer GPU; dataset is small-to-medium; this is the default for most hobbyist and SME use-cases |

**Rule of thumb for this project (16 GB VRAM):**

- Default to **QLoRA** (4-bit NF4 + DoRA + rsLoRA as configured).
- If quality is insufficient after 3 epochs and your dataset is large (>50 K examples), consider renting a 24 GB GPU and switching to plain **LoRA** by setting `load_in_4bit: false` in `config.yaml`.
- **Full fine-tuning** is out of scope for single-GPU consumer hardware unless you use a very small model (≤ 3B parameters).

### Why DoRA over standard LoRA?

DoRA (Weight-Decomposed Low-Rank Adaptation) decomposes the weight update into
magnitude and direction components.  It has been shown to improve average
accuracy by **~3.7 %** over standard LoRA on commonsense reasoning benchmarks
with **no additional inference cost** — the adapter is merged before deployment.

### Why rsLoRA?

Rank-Stabilized LoRA re-scales the adapter output by `1/√r` instead of `1/r`.
This keeps gradient magnitudes stable across different rank values, making
hyperparameter sweeps over `r` less sensitive and reducing the risk of training
instability at higher ranks.

---

## License

MIT
