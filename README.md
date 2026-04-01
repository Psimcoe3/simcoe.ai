# simcoe.ai — Local LLM Fine-Tuning Pipeline

A production-ready 4-bit QLoRA fine-tuning pipeline for 7B/8B language models,
designed to run on a single NVIDIA GPU (16 GB VRAM) inside WSL2 on Windows.

Built on a **March 2026 validated stack**: Unsloth optimised kernels, rsLoRA
adapters with optional DoRA support, local TensorBoard tracking by default,
GGUF export for Ollama inference, deterministic lookup runtimes, and
release-gated evaluation.

---

## Table of Contents

1. [Quickstart](#quickstart)
2. [Project Structure](#project-structure)
3. [Environment Setup — WSL2 & CUDA 12.4](#environment-setup--wsl2--cuda-124)
4. [Configuration](#configuration)
5. [Pipeline Walkthrough](#pipeline-walkthrough)
6. [Inference Workflows](#inference-workflows)
7. [Developer Workflow](#developer-workflow)
8. [Prompt Engineering Library](#prompt-engineering-library)
9. [What Else Would I Do Next?](#what-else-would-i-do-next)
10. [LoRA vs QLoRA vs Full Fine-Tuning](#lora-vs-qlora-vs-full-fine-tuning)

---

## Quickstart

```bash
# 1. Clone and enter the repo
git clone https://github.com/Psimcoe3/simcoe.ai.git
cd simcoe.ai

# 2. Create a virtual environment (Python 3.11+; 3.12.3 validated)
python3 -m venv .venv
source .venv/bin/activate

# 3. Install the validated CUDA 12.4 dependency stack
pip install -r requirements.txt

# 4. Optional integrations (.env is only needed for external services)
cp .env.example .env
# Fill only the keys you plan to use:
# - HF_TOKEN for gated model downloads
# - WANDB_* if you switch privacy.tracking to wandb
# - OPENAI_API_KEY for openai/* judging or generation

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
├── pyproject.toml         # Ruff + pytest configuration
├── requirements-dev.txt   # CPU-safe dev/test tooling
├── .pre-commit-config.yaml # Local quality hooks
├── topics.yaml            # Topic definitions for synthetic data generation
├── prompts/
│   ├── README.md          # System prompt playbook for internal prompt engineers
│   └── system_prompt_templates.yaml # Guidance-first template catalog
├── .env.example           # Secret template (copy to .env, never commit .env)
├── requirements.txt       # Pinned working versions for Python 3.12 / CUDA 12.4
├── .github/
│   └── workflows/
│       └── quality.yml    # CI quality gate for lint + tests
│
├── data/
│   ├── raw/               # Place your dataset.jsonl here (seed dataset included)
│   └── processed/         # Train/validation Arrow datasets (auto-generated)
│   └── registry/          # Source registry manifests for external roots (auto-generated)
│
├── models/
│   ├── adapters/          # Saved LoRA / DoRA adapter weights
│   ├── merged_16bit/      # Merged model in bfloat16 (for vLLM)
│   └── gguf/              # Q4_K_M GGUF + Ollama Modelfile
│
├── scripts/
│   ├── agent_shell.py     # Local interactive shell backed by routing, context providers, and deterministic tools
│   ├── check_env.py       # Pre-flight validator
│   ├── build_estimate_index.py # Build lookup-ready RSMeans estimate records
│   ├── build_catalog_data.py # Turn structured product/reference data into training rows
│   ├── build_source_registry.py # Snapshot external source roots into a review-safe registry manifest
│   ├── config_validation.py # Shared config/prerequisite validation
│   ├── data_contracts.py  # Stable IDs and review-safe data-family metadata
│   ├── deterministic_tool_utils.py # Stable request/response envelopes for lookup runtimes
│   ├── indexed_memory.py  # Pointer-only memory index + topic/event storage + query CLI
│   ├── generate_data.py   # Synthetic data generation via Ollama or OpenAI-compatible APIs
│   ├── prepare_data.py    # JSONL → formatted + split dataset
│   ├── revit_entity_lookup.py # Deterministic Revit/entity lookup runtime
│   ├── revit_ingestion.py # Normalize Revit exports or family files for retrieval and lookup
│   ├── train.py           # QLoRA training with Unsloth + SFTTrainer
│   ├── export.py          # Merge adapters → 16-bit + GGUF
│   └── evaluate.py        # ROUGE / exact match / LLM-as-judge
│
├── evals/
│   └── results.json       # Evaluation output (auto-generated)
│
├── tests/                 # Pure-Python unit tests for retrieval and deterministic tools
│
└── logs/                  # W&B local artefacts (gitignored)
```

---

## Environment Setup — WSL2 & CUDA 12.4

### Prerequisites

- Windows 11 with WSL2 enabled
- Ubuntu 22.04 LTS (recommended) in WSL2
- NVIDIA GPU with 16 GB VRAM (RTX 3090 / 4080 / 4090 / A4000 or better)
- NVIDIA drivers ≥ 550 on the Windows host (CUDA 12.4 is surfaced into WSL2 automatically)

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

### Step 2 — Python 3.12 (3.11+ supported)

```bash
sudo apt-get install -y python3.12 python3.12-venv python3.12-dev
python3.12 -m venv .venv
source .venv/bin/activate
```

### Step 3 — Install the validated stack

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

`requirements.txt` already pins the working `cu124` PyTorch wheels, `unsloth==2026.3.17`, and the verified compatibility fix `torchao==0.12.0`.

If you need a different CUDA build, update the three `cu124` PyTorch pins in `requirements.txt` to the matching wheel set before installing.

### Step 4 — Optional integrations

```bash
cp .env.example .env
# Fill only the integrations you need:
# - HF_TOKEN for gated model downloads
# - WANDB_* if privacy.tracking=wandb
# - OPENAI_API_KEY for openai/* judging or generation
```

For the fully local path in this repo, `.env` is optional: TensorBoard tracking, local Ollama judging, and local Ollama generation all work without external credentials.

### Step 5 — Validate

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
| `evaluation` | `judge_model`, `results_path`, `inference_batch_size`, `max_new_tokens` |
| `release` | `fail_on_threshold_breach`, quick/full thresholds, category thresholds, smoke-test requirements |
| `retrieval` | `enabled`, corpus path, benchmark-time retrieval settings |
| `memory` | `enabled`, file-backed memory paths, pointer-index limits, and skeptical retrieval settings |
| `agent_shell` | local shell provider/model, session persistence paths, output budget, and text-route context policy |
| `architecture` | primary runtime, retrieval requirement, multimodal/geometry feature flags |
| `source_registry` | external source root, registry manifest path, review-safe defaults |
| `managed_sources` | repo-owned mirror paths used as defaults by PDF, folder-ingest, and estimate-index workflows |

---

## Pipeline Walkthrough

### 1. Prepare data (`scripts/prepare_data.py`)

- Loads a JSONL file where each line is `{"instruction": "...", "input": "...", "response": "..."}`.
- Enforces a strict raw schema: `instruction` must be a non-empty string, `input` must be a string when present, and each row must provide a non-empty `response` or `output`.
- Rejects conflicting `response` and `output` values, invalid `metadata` or `tags` fields, and chat-style rows such as `messages` or `conversations` that have not been converted yet.
- Formats into an Alpaca-style instruction template.
- Splits 90 % / 10 % (train / validation) using `random_state=3407`.
- Validates that no example exceeds `max_seq_length` tokens and drops over-length examples.
- Saves Arrow datasets to `data/processed/`.
- Writes `manifest.json` in the processed dataset directory with source hash, row counts, token-length summaries, and dataset fingerprints.

### 2. Train (`scripts/train.py`)

- Fails early if processed datasets are missing or required config fields are invalid.
- Treats `.env` as optional. External credentials are only needed when you deliberately opt into gated model downloads, W&B tracking, or OpenAI-backed workflows.
- Loads the base model in 4-bit NF4 via Unsloth's `FastLanguageModel`.
- Applies the configured adapter strategy. The checked-in configs currently enable rsLoRA and keep DoRA off because merged export remains more reliable without the magnitude-vector path.
- Initialises local TensorBoard tracking by default and only switches to Weights & Biases when `privacy.tracking: wandb` is configured.
- Trains with `SFTTrainer` (cosine LR schedule, warmup 5 %, bfloat16).
- Saves LoRA adapters to `models/adapters/`.
- Writes `train_manifest.json` with config, runtime, processed-data lineage, trainer state, and adapter checksums.
- Supports `--manifest_only` to backfill `train_manifest.json` from an existing adapter directory and latest checkpoint without re-running training.

### 3. Export (`scripts/export.py`)

- Fails early if adapter artifacts are missing or export-related config values are invalid.
- Merges adapters into the base model at bfloat16 precision (→ `models/merged_16bit/`).
- Quantises to Q4_K_M GGUF (→ `models/gguf/`).
- Writes an Ollama `Modelfile` for one-command registration.
- Supports `--verify_existing` so you can validate already-exported artifacts without re-running the merge.
- Starts a local Ollama daemon automatically for GGUF smoke tests when the binary is installed but the server is not already running.
- Can run required merged-model and GGUF smoke tests from the `release` section.
- Writes `export_manifest.json` with artifact checksums, runtime metadata, and smoke-test results.

### 4. Evaluate (`scripts/evaluate.py`)

- Fails early if the merged model, processed validation set, configured benchmark, or evaluation config is missing.
- Loads the merged model and runs batched inference with timing and progress output.
- Scores outputs with ROUGE-1/2/L and exact match.
- Supports LLM-as-judge scoring via a local Ollama model or an OpenAI-compatible backend.
   Set `evaluation.judge_model: simcoe` for local Ollama or `evaluation.judge_model: openai/<model>` for the remote path.
   `OPENAI_API_KEY` is only needed for the remote path.
- Auto-starts a local Ollama daemon for judge requests when needed and shuts it down afterward if evaluation launched it.
- Rates each response 1–5 with a structured rationale. Set `judge_model: null` to disable.
- Supports quick and full evaluation profiles via config plus CLI overrides for example count, batch size, and generation length.
- Uses `evaluation.golden_benchmark_path` for full-mode benchmark runs when configured.
- Can inject retrieved context from a local corpus when `retrieval.enabled` and `retrieval.use_in_full_evaluation` are set.
- Can also inject local indexed-memory hints when `memory.enabled` is true. Memory stays separate from the retrieval corpus: the always-loaded file is a pointer-only index, while full topic records are loaded on demand and filtered skeptically.
- Retrieval and memory context assembly now runs through a named context-provider registry. Provider ordering is config-driven via `context_providers.order`, and evaluation traces serialize provider-level results separately from the flattened retrieval and memory fields kept for compatibility.
- Retrieval and memory context assembly still prefetches in parallel during evaluation, and memory queries read the maintained pointer index rather than rebuilding it on every lookup.
- Route decisions, context providers, and deterministic-tool execution now expose optional pre/post hook stages. Hooks are local config rules for audit, deny, annotate, or field rewrites; they are disabled by default.
- Evaluation outputs now also carry structured execution envelopes: a top-level `execution.summary` plus per-example `execution` blocks that normalize route, context-provider, and deterministic-tool traces without removing the older compatibility fields.
- Supports mixed-route golden benchmarks where some rows are evaluated through deterministic tools instead of text generation.
- Reports deterministic-tool success and match-score metrics separately so text and tool regressions are visible independently.

### 5. Memory workflows (`scripts/indexed_memory.py`)

- Memory is local operational state, not training data and not release lineage.
- The store has three layers: `events.jsonl` as an append-only log, `topics/*.json` as materialized topic records, and `MEMORY.json` as a pointer-only index that never stores full topic content.
- `memory.provider` is explicit even though the current backend is only `file`; that keeps evaluation and CLI call sites stable if a local SQLite or other backend is added later.
- Memory now participates in the same context-provider registry as retrieval, so prompt assembly stays extensible without baking new provider branches into `scripts/evaluate.py`.
- Query results are skeptical by default: stale, retracted, contradicted, below-threshold, and unverified topics are excluded and returned with explicit reasons.
- Consolidation tracks superseded and contradicted observations, and evaluation traces now carry a stable `memory_request_id` so memory hits can be audited per benchmark row.
- Curated imports are supported from JSON, JSONL, and YAML. Imported rows must be explicit operator knowledge, not derivable scratch state.
- Operator commands:

```bash
make memory-add CONFIG=config.electrician.yaml ARGS='--topic "Grounding guidance" --summary "Prefer verified grounding notes" --content "Use verified NCCER grounding guidance before falling back to generic notes." --kind verified_fact --tag grounding'

make memory-query CONFIG=config.electrician.yaml ARGS='--query "grounding guidance"'

make memory-import CONFIG=config.electrician.yaml ARGS='--source-file data/raw/curated_memory.jsonl --source-label operator_seed'

make memory-consolidate CONFIG=config.electrician.yaml

make workflow-list CONFIG=config.electrician.yaml

make workflow-show CONFIG=config.electrician.yaml WORKFLOW=memory-seed

make workflow-run CONFIG=config.electrician.yaml WORKFLOW=memory-seed ARGS='--var source_file=data/raw/curated_memory.jsonl --dry-run'

make inspect-hooks CONFIG=config.electrician.yaml

make inspect-providers CONFIG=config.electrician.yaml

make inspect-execution CONFIG=config.electrician.yaml

make inspect-shell CONFIG=config.yaml
make inspect-shell CONFIG=config.yaml ARGS='--session-id agent-shell-123456789abc --tail 3'
```
- Emits release-gate results from the optional `release` section, including per-category threshold checks, and can fail non-zero when thresholds are breached.
- Saves results to `evals/results.json`.

### 5A. Workflow Registry And Inspection

- `workflows/registry.yaml` is a checked-in local workflow manifest for repeatable operator jobs such as memory seeding, retrieval corpus refresh, benchmark refresh, and release verification.
- `scripts/workflow_registry.py` can list, validate, show, dry-run, and execute those workflows using the current Python environment and selected config.
- `scripts/orchestration_inspect.py` exposes operator inspection views for hook rules, provider ordering, saved execution summaries from evaluation results, and persisted local agent shell sessions.
- These surfaces are intentionally local and config-driven. They are not a plugin marketplace and do not fetch remote tools or instructions.

### 5. Build Retrieval And Benchmark Assets

- `scripts/build_retrieval_corpus.py` builds a deduplicated local retrieval corpus plus a manifest with source distribution and dedupe counts.
- `scripts/build_golden_benchmark.py` builds a reproducible benchmark JSONL from the checked-in spec and source corpus.
- The golden benchmark spec can now mix source-matched text rows with direct deterministic-tool rows. Tool rows declare `route: deterministic_tool`, `tool_name`, `tool_request`, and `tool_expectation` in the spec.
- These assets are intended for source-heavy domains where release quality depends on grounded retrieval, not just memorized phrasing.

### 6. Source Registry And Review Contracts

- `scripts/build_source_registry.py` snapshots the configured external root into a machine-readable registry manifest with stable asset IDs, file hashes, and ingestion recommendations.
- Registry entries now include a suggested repo-managed destination path so selected external assets can be mirrored into this repo in a predictable layout.
- `scripts/materialize_sources.py` copies selected registry assets into `sources/managed/<namespace>/<runtime_owner>/<asset_kind>/...` and writes a materialization manifest.
- `scripts/ingest_reference_folder.py`, `scripts/revit_ingestion.py`, and `scripts/build_estimate_index.py` now stamp output records with `record_id` and a `data_contract` block.
- Contract-marked non-SFT records default to `review_state: review_required` and `sft_candidate: false`.
- `scripts/build_catalog_data.py` refuses to promote contract-marked unreviewed records into training examples unless `--allow_contract_override` is passed deliberately.
- Operational rule: once an external file is targeted for actual use, materialize it into the repo first and run downstream ingestion from the repo-managed copy instead of the external path.

---

## Makefile

The Makefile orchestrates the pipeline in the correct order:

```bash
make all          # check → prepare → train → export → evaluate
make quality      # lint + tests for the core CPU-safe modules
make quality-release # quality + lightweight release artifact verification
make lint         # Ruff lint + format check on core modules and tests
make test         # pure-Python unit tests
make check        # validate environment only
make prepare      # prepare dataset only
make train        # fine-tune (requires prepared data)
make train-manifest # backfill train lineage from existing checkpoints
make export       # export (requires trained adapters)
make export-verify # verify existing exports and smoke tests
make release-bundle # package a lightweight release-verification bundle
make release-verify # validate release manifests/results without rerunning evaluation
make evaluate     # evaluate (requires exported model)
make evaluate-quick # faster metrics-only evaluation
make evaluate-release # fail if configured release thresholds are missed
make agent-shell  # start the local routed shell or run a one-shot prompt
make workflow-list # list checked-in operator workflows
make workflow-show WORKFLOW=memory-seed # inspect one workflow
make workflow-validate # validate the checked-in workflow manifest
make workflow-run WORKFLOW=memory-seed ARGS='--var source_file=data/raw/curated_memory.jsonl --dry-run' # run or preview one workflow
make inspect-hooks # inspect configured hook rules
make inspect-providers # inspect configured provider ordering and active providers
make inspect-execution # inspect saved execution summary from evaluation results
make source-registry # build the configured external source registry manifest
make source-materialize # copy selected external assets into sources/managed/
make retrieval-corpus # build the local retrieval corpus
make golden-benchmark # build the curated golden benchmark
make pdf-notes    # extract short attributed notes from a local PDF
make ingest-reference-folder # ingest a mixed local docs/code folder into JSONL
make merge-examples # merge reviewed example JSONLs into one corpus
make revit-ingest # normalize Revit exports or family files into retrieval data
make revit-lookup # query the deterministic Revit/entity lookup runtime
make estimate-index # build RSMeans-based price/labor lookup data
make estimate-lookup # query the deterministic estimate lookup runtime
make clean        # remove all generated artifacts
make help         # show all targets
```

Override the config file: `make all CONFIG=my_config.yaml`

For the electrician workflow, the release-oriented sequence is typically:

```bash
make source-registry CONFIG=config.electrician.yaml
make source-materialize CONFIG=config.electrician.yaml ARGS='--registry-id source_asset:...'
make retrieval-corpus
make golden-benchmark
make train-manifest CONFIG=config.electrician.yaml
make export-verify CONFIG=config.electrician.yaml
make evaluate-release CONFIG=config.electrician.yaml
make release-bundle CONFIG=config.electrician.yaml OUT=.github/release-bundles/electrician-release-verification-bundle.tar.gz
make release-verify CONFIG=config.electrician.yaml
```

`make evaluate-release` now runs an explicit release profile. That profile fails closed when judge thresholds are configured but no judge scores are available, and it can enforce retrieval usage for grounded benchmark rows when `release.require_retrieval_for_grounded_benchmark: true` is set.

`make release-verify` is the lightweight follow-up check. It only reads the processed data manifest, training manifest, export manifest, and saved release results to confirm the lineage chain is coherent and the last saved release gate passed. It does not rerun training, export, smoke tests, or model evaluation.

`make release-bundle` packages the minimal artifact set needed for that lightweight verification on another machine. By default it keeps the bundle small by replacing the GGUF binary with a placeholder file at the same repo-relative path; pass `INCLUDE_GGUF=1` if you want the real GGUF copied into the bundle. `dist/` is ignored, so write the bundle under `.github/release-bundles/` when you want the release-candidate workflow to run from a pushed commit.

For local operator workflows and inspection:

```bash
make workflow-list CONFIG=config.electrician.yaml
make workflow-show CONFIG=config.electrician.yaml WORKFLOW=retrieval-refresh
make workflow-run CONFIG=config.electrician.yaml WORKFLOW=benchmark-refresh ARGS='--dry-run'
make inspect-hooks CONFIG=config.electrician.yaml
make inspect-providers CONFIG=config.electrician.yaml
make inspect-execution CONFIG=config.electrician.yaml
```

The repo now also includes a GitHub Actions workflow, [.github/workflows/release-candidate-verify.yml](.github/workflows/release-candidate-verify.yml), which restores a checked-in bundle or downloads one from a URL and then runs `make quality-release` against it. The repo-backed flow is:

```bash
make release-bundle CONFIG=config.electrician.yaml OUT=.github/release-bundles/electrician-release-verification-bundle.tar.gz
sha256sum .github/release-bundles/electrician-release-verification-bundle.tar.gz > .github/release-bundles/electrician-release-verification-bundle.tar.gz.sha256
git add .github/release-bundles/electrician-release-verification-bundle.tar.gz .github/release-bundles/electrician-release-verification-bundle.tar.gz.sha256
git commit -m "Refresh electrician release candidate bundle"
git push origin main
```

Pushing that bundle to `main` triggers `release-candidate-verify` automatically.

If you do not want the bundle in git, the workflow also supports an external tarball URL. Upload the bundle somewhere GitHub Actions can fetch, then run `release-candidate-verify` manually with:

- `config_path=config.electrician.yaml`
- `artifact_bundle_url=<https URL to the tar.gz>` or leave it empty to use `artifact_bundle_path`
- `artifact_bundle_path=.github/release-bundles/electrician-release-verification-bundle.tar.gz`
- `artifact_bundle_sha256=<optional checksum>`

---

## Inference Workflows

### 1. Use the merged 16-bit export directly with Transformers

This path uses the existing runtime dependencies already pinned in `requirements.txt`:

```bash
PYTHONPATH=scripts python - <<'PY'
from tokenizer_utils import load_tokenizer_with_compat
from transformers import AutoModelForCausalLM, pipeline

model_dir = "models/merged_16bit"
tokenizer = load_tokenizer_with_compat(model_dir)
if tokenizer.pad_token_id is None and tokenizer.eos_token_id is not None:
   tokenizer.pad_token_id = tokenizer.eos_token_id

model = AutoModelForCausalLM.from_pretrained(
   model_dir,
   device_map="auto",
   torch_dtype="auto",
   trust_remote_code=True,
)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
prompt = "### Instruction:\nExplain why grounding and bonding matter in electrical work.\n\n### Response:"
result = pipe(prompt, max_new_tokens=128, do_sample=False)[0]["generated_text"]
print(result.split("### Response:", 1)[-1].strip())
PY
```

The same `models/merged_16bit` directory is also suitable for a separate vLLM serving stack if that runtime is part of your deployment environment.

### 2. Register the GGUF export with Ollama

```bash
ollama serve
ollama create simcoe -f models/gguf/Modelfile
ollama run simcoe
```

`scripts/export.py` writes the `Modelfile` automatically and prints the same registration commands after export. If you only want to re-run smoke tests against existing artifacts, use `make export-verify`.

### 3. Use the local agent shell

The repo now includes `scripts/agent_shell.py`, a local operator-facing shell that reuses the existing fast router, context-provider registry, deterministic lookup runtimes, workflow registry, and prompt-template system.

Start an interactive session:

```bash
make agent-shell CONFIG=config.yaml
```

Run a single routed prompt and exit:

```bash
make agent-shell CONFIG=config.yaml ARGS='--prompt "Find the estimate lookup for EMT conduit."'
```

Resume or inspect a saved session:

```bash
make agent-shell CONFIG=config.yaml ARGS='--session-id agent-shell-123456789abc'
make agent-shell CONFIG=config.yaml ARGS='--show-session --session-id agent-shell-123456789abc'
make inspect-shell CONFIG=config.yaml
make inspect-shell CONFIG=config.yaml ARGS='--session-id agent-shell-123456789abc --tail 3'
```

Shell sessions persist under `agent_shell.root_dir` and keep a JSON session summary plus a JSONL transcript per session. Inside the shell, `/help` shows the initial command surface: `/session`, `/route`, `/providers`, and `/workflow list|show`.

---

## Developer Workflow

Install the lightweight developer toolchain, enable pre-commit hooks, and run the same CPU-safe quality gate used in CI:

```bash
pip install -r requirements-dev.txt
pre-commit install
make quality
```

The quality gate intentionally stays off the GPU-heavy training stack. It covers the deterministic lookup and retrieval core with Ruff plus pytest, while full training/export/evaluation remain manual or release-job workflows.

If a machine already has release artifacts on disk, use `make quality-release CONFIG=config.electrician.yaml` to combine the CPU-safe quality gate with lightweight release artifact validation.

---

## Prompt Engineering Library

The repo now includes a guidance-first prompt engineering library under `prompts/`.
It is aimed at internal prompt engineers who want reusable system prompt patterns
that match the current runtime rather than accidentally conflicting with it.

- `prompts/system_prompt_templates.yaml` catalogs reusable system prompts with purpose, use and avoid conditions, variable slots, anti-patterns, and expected failure modes.
- `prompts/README.md` explains the conditioning levers behind those templates and maps them to the repo's current prompt stack.
- `system_prompts.*` in the checked-in configs now lets runtime surfaces select template ids for synthetic generation, judge scoring, and the exported Ollama `SYSTEM` block.

Use the library when you need to control stable model behavior such as:

- domain scope
- evidence discipline
- insufficient-context behavior
- standards and compliance framing

Do not use the library as a substitute for retrieval or deterministic tools.
Facts that change over time, source text that needs attribution, and lookup-owned
values such as prices or entity metadata should stay outside the system prompt.

The current runtime stack is still the source of truth:

1. Optional system prompt from chat-completions or the Ollama `SYSTEM` block.
2. `### Instruction:` content.
3. Optional `### Input:` content.
4. Optional `### Memory Hints:`.
5. Optional `### Retrieved Context:`.
6. `### Response:` generation boundary.

The checked-in configs currently point those runtime surfaces at behavior-equivalent
template ids, so the library is active without changing the existing prompt intent.
You can swap to stronger grounding templates later by changing `system_prompts.*`
and supplying any required variables.

---

## Revit Estimation Workflow

The Revit estimation path in this repo is retrieval-first.

- Revit families, schedule exports, and Stratus-style metadata are normalized into reference records.
- RSMeans or crosswalk data is normalized into lookup-ready estimate records.
- The model can explain the matched item and estimate context, but current price and labor stay in external lookup data instead of model weights.

### 1. Build Revit family references

Use a structured export when you have one:

```bash
python scripts/revit_ingestion.py \
   --source /path/to/revit_schedule_export.csv \
   --out data/raw/revit_family_index.jsonl
```

Or bootstrap a reference catalog directly from a family directory:

```bash
python scripts/revit_ingestion.py \
   --family-dir /mnt/c/Users/Paul/Revit/Families \
   --out data/raw/revit_family_index.jsonl
```

Equivalent Make target:

```bash
make revit-ingest FAMILY_DIR=/mnt/c/Users/Paul/Revit/Families OUT=data/raw/revit_family_index.jsonl
```

You can also build a deterministic lookup index from a structured managed export, which is the recommended path for benchmark-quality entity resolution:

```bash
make revit-ingest \
   CONFIG=config.electrician.yaml \
   SOURCE="sources/managed/electricalai_docs/manual_review/tabular/csv model info/eV_FamilyInstanceList(2).xlsx - Itemized List - Final Export.csv" \
   OUT=data/raw/revit_family_index.jsonl
```

Once the index exists, query it through the deterministic Revit/entity runtime:

```bash
python scripts/revit_entity_lookup.py \
   --config config.electrician.yaml \
   --query "Nema 1 Galvanized Screw Cover" \
   --top-k 3
```

Equivalent Make target:

```bash
make revit-lookup \
   CONFIG=config.electrician.yaml \
   QUERY="Nema 1 Galvanized Screw Cover" \
   TOP_K=3
```

This returns a deterministic JSON envelope with normalized Revit family/type metadata, source provenance, and retained source fields from the structured export when available.

### 2. Build the estimate index

Normalize crosswalk and RSMeans records into lookup entries. When `managed_sources.estimating_har_dir` is configured, the repo-managed HAR mirror becomes the default input:

```bash
python scripts/build_estimate_index.py \
   --config config.electrician.yaml \
   --out data/raw/estimate_index.jsonl
```

The checked-in `rsmeans_parsed.csv` path may be misaligned if it was generated with the old fixed column map. The estimate builder now rejects obviously code-shifted CSVs and prefers parsing the raw HAR files directly.

When both `--mapping` and `--rsmeans-har-dir` are provided, the builder keeps the family/category/manufacturer metadata from the crosswalk file but replaces estimate fields with the trusted HAR-derived values whenever the RSMeans description matches.

Equivalent Make target:

```bash
make estimate-index CONFIG=config.electrician.yaml OUT=data/raw/estimate_index.jsonl
```

If you want to enrich the managed HAR data with a crosswalk file, pass it explicitly:

```bash
make estimate-index CONFIG=config.electrician.yaml \
   MAPPING=/path/to/stratus_rsmeans_map_FULL.csv \
   OUT=data/raw/estimate_index.jsonl
```

### 2b. Query the estimate index deterministically

Once the index exists, query it through the deterministic lookup runtime instead of treating it as a passive JSONL artifact:

```bash
python scripts/estimate_lookup.py \
   --config config.electrician.yaml \
   --query "3/4 EMT conduit" \
   --quantity 120
```

Equivalent Make target:

```bash
make estimate-lookup \
   CONFIG=config.electrician.yaml \
   QUERY="3/4 EMT conduit" \
   QUANTITY=120 \
   TOP_K=3
```

The response is a deterministic JSON envelope with a stable request ID, matched estimate records, source provenance, and quantity rollups when the unit is safe to scale.

### 3. Keep training and retrieval separate

Keep volatile fields like material pricing, labor hours, and installed totals in retrieval data. Use training data for:

- family identification language
- estimate explanation and assumptions
- output formatting
- interpretation of category, type, and assembly context

Use `scripts/build_catalog_data.py` only after reviewing whether a structured source should become training examples or stay as reference data.

Raw external-root assets should first be registered with:

```bash
make source-registry CONFIG=config.electrician.yaml
```

When a registered asset is actually selected for use, mirror it into the repo before ingestion:

```bash
make source-materialize CONFIG=config.electrician.yaml \
   ARGS='--registry data/registry/electricalai_docs_registry.json --path-prefix estimating'
```

That command copies matching files into `sources/managed/electricalai_docs/...` and records the copy set in `data/registry/materialized_sources.json`.

When records carry a `data_contract` block, `build_catalog_data.py` will block automatic SFT conversion unless the record is explicitly marked reviewed/approved and `sft_candidate: true`.

---

## Synthetic Data Generation

`scripts/generate_data.py` uses a local Ollama model by default and can switch
to an OpenAI-compatible backend when you pass an `openai/<model>` name.

```bash
# Generate 20 examples per topic with the local Ollama model named "simcoe"
python scripts/generate_data.py --topics topics.yaml --out data/raw/generated.jsonl --count 20

# Use a remote OpenAI-compatible model instead
python scripts/generate_data.py --topics topics.yaml --out data/raw/generated.jsonl --count 20 --model openai/gpt-4o

# Merge into the main dataset
cat data/raw/generated.jsonl >> data/raw/dataset.jsonl
```

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
California DIR prevailing wage pages, Electrical Contractor Magazine, and
electrical estimating workflow references from Bids Analytics.

Local manuals or ebooks placed in [sources/README.md](sources/README.md) should stay reference-only unless their licensing has been reviewed for broader dataset use.

### Extract reference notes from local PDFs

Use a dedicated PDF-to-notes step for local manuals and estimator books:

```bash
python scripts/extract_reference_pdf.py \
   --config config.electrician.yaml \
   --start-page 4 \
   --out data/raw/estimator_ebook_methodology_notes.jsonl
```

Equivalent Make target:

```bash
make pdf-notes \
   CONFIG=config.electrician.yaml \
   START_PAGE=4 \
   OUT=data/raw/estimator_ebook_methodology_notes.jsonl
```

This step creates short, attributed reference-note records with page ranges and summaries. It is intended for retrieval context and reviewed methodology examples, not raw page dumping. The canonical managed-estimating target writes to `data/raw/estimator_ebook_methodology_notes.jsonl`.

### Ingest a local reference folder

Use a mixed-folder ingestion step when a local tree contains manuals, notes, and code-like files:

```bash
python scripts/ingest_reference_folder.py \
   --config config.electrician.yaml \
   --out data/raw/electrical_material_reference.jsonl
```

Equivalent Make target:

```bash
make ingest-reference-folder \
   CONFIG=config.electrician.yaml \
   OUT=data/raw/electrical_material_reference.jsonl
```

With the electrician config, that defaults to the repo-managed folder at `sources/managed/electricalai_docs/retrieval/document/estimating` unless you pass `ROOT=...` explicitly. To ingest a different managed family, pass `MANAGED_KEY=drawings_reference_root`, `MANAGED_KEY=code_training_reference_root`, or another configured key.

This step recursively scans the folder and emits:

- PDF-derived reference notes for manuals and code books
- text reference notes for `.txt`, `.md`, `.yaml`, and `.json` files
- code reference records for source files such as `.py`, `.cs`, `.js`, and `.ts`

The output can be reviewed directly for retrieval use. If those records are explicitly approved for SFT, you can convert them with `make estimating-reference-examples ALLOW_CONTRACT_OVERRIDE=1`, but the default corpus build keeps them retrieval-only.

Managed source mirrors under `sources/managed/` now use Git LFS for large binary and document formats so the repo stays pushable to GitHub. Run `git lfs install` on machines that will materialize or clone those assets.

### Merge reviewed example sets

When you have multiple approved example files, merge and deduplicate them into a single corpus:

```bash
make merge-examples \
   SOURCES="data/raw/nccer_examples.jsonl data/raw/njatc_examples.jsonl data/raw/bids_analytics_examples.jsonl data/raw/estimator_ebook_methodology_examples.jsonl" \
   OUT=data/raw/electrician_reference_examples.jsonl
```

This is the easiest path for building a larger electrician-focused dataset from multiple reviewed source families before running `scripts/prepare_data.py`.

To rebuild the canonical electrician corpus from repo-managed estimating sources in one step:

```bash
make electrician-corpus CONFIG=config.electrician.yaml
```

That target refreshes:

- `data/raw/estimator_ebook_methodology_notes.jsonl`
- `data/raw/estimator_ebook_methodology_examples.jsonl`
- `data/raw/estimating_reference.jsonl`
- `data/raw/estimate_index.jsonl`
- `data/raw/electrician_reference_examples.jsonl`

The managed folder ingest stays retrieval-only by default because its `data_contract` metadata is not approved for SFT promotion. If you explicitly review and approve those records, run:

```bash
make estimating-reference-examples CONFIG=config.electrician.yaml ALLOW_CONTRACT_OVERRIDE=1
```
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

1. ~~**Add CI smoke checks**~~ ✅ Done — PRs now run a CPU-safe quality gate with Ruff and pytest.
2. ~~**Ship a tiny example dataset**~~ ✅ Done — 32-example seed dataset at `data/raw/dataset.jsonl`.
3. ~~**Replace the LLM-as-judge stub**~~ ✅ Done — real OpenAI-based judge in `scripts/evaluate.py`.
4. ~~**Add config validation**~~ ✅ Done — shared `scripts/config_validation.py` used by all pipeline scripts.
5. ~~**Document inference workflows**~~ ✅ Done — merged-model and Ollama serving paths are documented above.
6. **Add a nightly GPU-backed release job** that runs `make evaluate-release CONFIG=config.electrician.yaml` against current artifacts.
7. **Check in a tiny retrieval fixture set** so corpus builders and benchmark builders can be tested end to end on CPU.
8. **Scale the dataset** using `scripts/generate_data.py` to reach 500–2000+
   reviewed examples before production fine-tuning.

---

## LoRA vs QLoRA vs Full Fine-Tuning

| Method | VRAM | Speed | When to use |
|--------|------|-------|-------------|
| **Full fine-tuning** | 80 GB+ (for 7B) | Slowest | You have a large high-quality dataset and multi-GPU hardware; you need maximum task performance |
| **LoRA** | ~24 GB (for 7B in fp16) | Fast | You have a moderate dataset and a 24 GB GPU; you want better accuracy than QLoRA without the quantisation noise |
| **QLoRA (4-bit)** | ~10–14 GB (for 7B/8B) | Fast | You have a 16 GB consumer GPU; dataset is small-to-medium; this is the default for most hobbyist and SME use-cases |

**Rule of thumb for this project (16 GB VRAM):**

- Default to **QLoRA** (4-bit NF4 + rsLoRA as configured).
- If quality is insufficient after 3 epochs and your dataset is large (>50 K examples), consider renting a 24 GB GPU and switching to plain **LoRA** by setting `load_in_4bit: false` in `config.yaml`.
- **Full fine-tuning** is out of scope for single-GPU consumer hardware unless you use a very small model (≤ 3B parameters).

### Why DoRA over standard LoRA?

DoRA (Weight-Decomposed Low-Rank Adaptation) decomposes the weight update into
magnitude and direction components.  It has been shown to improve average
accuracy by **~3.7 %** over standard LoRA on commonsense reasoning benchmarks
with **no additional inference cost** — the adapter is merged before deployment.
The checked-in configs currently leave `use_dora: false` because merged export
is still more reliable on the validated live stack without the magnitude-vector
path.

### Why rsLoRA?

Rank-Stabilized LoRA re-scales the adapter output by `1/√r` instead of `1/r`.
This keeps gradient magnitudes stable across different rank values, making
hyperparameter sweeps over `r` less sensitive and reducing the risk of training
instability at higher ranks.

---

## License

MIT
