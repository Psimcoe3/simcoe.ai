# Makefile — orchestrates the fine-tuning pipeline in the correct order.
#
# Usage:
#   make all          # run the full pipeline: check → prepare → train → export → evaluate
#   make quality      # run the CPU-safe quality gate: lint → test
#   make quality-release # quality + lightweight release artifact validation
#   make lint         # run Ruff lint + format checks on core modules
#   make test         # run pure-Python unit tests
#   make check        # validate environment only
#   make prepare      # prepare dataset only
#   make train        # train only (requires prepared data)
#   make train-manifest # backfill a train manifest from existing checkpoints
#   make export       # export only (requires trained adapters)
#   make export-verify # verify existing export artifacts + smoke tests
#   make release-bundle # build a lightweight release-verification bundle from current artifacts
#   make release-verify # validate release manifests/results without rerunning evaluation
#   make gguf         # convert merged model to GGUF and register with Ollama
#   make evaluate     # evaluate only (requires exported model)
#   make stage-archives BATCH=batch_name STAGE_ARCHIVE_NAME='SCHEDULE.zip' # stage selected external archives into a batch
#   make source-registry # snapshot the configured external source root into a registry manifest
#   make source-materialize # copy selected registry assets into repo-managed sources/
#   make stage-organize BATCH=batch_name # rebuild the deduped bucket view for one staged archive batch
#   make stage-import BATCH=batch_name CONFIG=config.electrician.yaml # organize + import one staged archive batch
#   make stage-retire BATCH=batch_name # archive manifests and prune one imported staged batch
#   make retrieval-corpus # build a local retrieval corpus for source-grounded evaluation
#   make golden-benchmark # build the curated golden benchmark from the checked-in spec
#   make generate     # generate synthetic data using Ollama (requires running model)
#   make clean        # remove all generated artifacts
#
# Override the config file:
#   make all CONFIG=my_config.yaml

SHELL  := /bin/bash
PYTHON ?= $(if $(wildcard .venv/bin/python),$(CURDIR)/.venv/bin/python,python3)
CONFIG := config.yaml

# Paths
LLAMA_CPP     := $(HOME)/src/llama.cpp
MERGED_DIR    := models/merged_16bit
GGUF_DIR      := models/gguf
GGUF_F16      := $(GGUF_DIR)/model-f16.gguf
GGUF_Q4       := $(GGUF_DIR)/model-Q4_K_M.gguf
MODELFILE     := $(GGUF_DIR)/Modelfile
OLLAMA        := $(HOME)/.local/bin/ollama
ESTIMATING_NOTES_OUT            ?= data/raw/estimator_ebook_methodology_notes.jsonl
ESTIMATING_NOTES_EXAMPLES_OUT   ?= data/raw/estimator_ebook_methodology_examples.jsonl
ESTIMATING_REFERENCE_OUT        ?= data/raw/estimating_reference.jsonl
ESTIMATING_REFERENCE_EXAMPLES_OUT ?= data/raw/estimating_reference_examples.jsonl
ESTIMATE_INDEX_OUT              ?= data/raw/estimate_index.jsonl
ELECTRICIAN_CORPUS_OUT          ?= data/raw/electrician_reference_examples.jsonl
ELECTRICIAN_CORPUS_SOURCES      ?= data/raw/nccer_examples.jsonl data/raw/njatc_examples.jsonl data/raw/bids_analytics_examples.jsonl $(ESTIMATING_NOTES_EXAMPLES_OUT)
RETRIEVAL_SOURCE   ?= $(ELECTRICIAN_CORPUS_OUT)
RETRIEVAL_OUT      ?= data/retrieval/electrician_reference_corpus.jsonl
RETRIEVAL_MANIFEST ?= data/retrieval/electrician_reference_corpus.manifest.json
GOLDEN_SOURCE      ?= $(RETRIEVAL_SOURCE)
GOLDEN_SPEC        ?= evals/golden_electrician_spec.json
GOLDEN_OUT         ?= evals/golden_electrician.jsonl
GOLDEN_MANIFEST    ?= evals/golden_electrician.manifest.json
STAGE_SOURCE_DIR   ?= /mnt/c/Users/Paul/Downloads
STAGING_ROOT       ?= data/staging/reference_archive_batches
STAGE_ARCHIVED_ROOT ?= $(STAGING_ROOT)/_archived
STAGE_ARCHIVE_NAME ?=
STAGE_ARCHIVE_LIST_FILE ?=
STAGE_ARCHIVES_OVERWRITE ?=
STAGE_LINK_MODE    ?= hardlink
STAGE_IMPORT_RUNTIME_OWNERS ?= retrieval multimodal geometry_rules
STAGE_IMPORT_BUCKET_MANIFEST ?=
STAGE_IMPORT_USE_EXTRACTED ?=
STAGE_IMPORT_INCLUDE_MANUAL_REVIEW ?=
STAGE_IMPORT_SKIP_SHA256 ?=
STAGE_IMPORT_OVERWRITE ?=
STAGE_IMPORT_DRY_RUN ?=
STAGE_RETIRE_ALLOW_WITHOUT_IMPORT ?=
STAGE_RETIRE_KEEP_BATCH ?=
STAGE_RETIRE_OVERWRITE ?=
STAGE_RETIRE_DRY_RUN ?=
STAGE_ARCHIVES_FLAGS = $(strip \
	$(if $(STAGE_ARCHIVE_NAME),--archive "$(STAGE_ARCHIVE_NAME)") \
	$(if $(STAGE_ARCHIVE_LIST_FILE),--archive-list-file "$(STAGE_ARCHIVE_LIST_FILE)") \
	$(if $(STAGE_ARCHIVES_OVERWRITE),--overwrite))
STAGE_IMPORT_FLAGS = $(strip \
	$(foreach owner,$(STAGE_IMPORT_RUNTIME_OWNERS),--runtime-owner $(owner)) \
	$(if $(STAGE_IMPORT_BUCKET_MANIFEST),--bucket-manifest "$(STAGE_IMPORT_BUCKET_MANIFEST)") \
	$(if $(STAGE_IMPORT_USE_EXTRACTED),--use-extracted) \
	$(if $(STAGE_IMPORT_INCLUDE_MANUAL_REVIEW),--include-manual-review) \
	$(if $(STAGE_IMPORT_SKIP_SHA256),--skip-sha256) \
	$(if $(STAGE_IMPORT_OVERWRITE),--overwrite) \
	$(if $(STAGE_IMPORT_DRY_RUN),--dry-run))
STAGE_RETIRE_FLAGS = $(strip \
	$(if $(STAGE_ARCHIVED_ROOT),--archived-root "$(STAGE_ARCHIVED_ROOT)") \
	$(if $(STAGE_RETIRE_ALLOW_WITHOUT_IMPORT),--allow-without-import) \
	$(if $(STAGE_RETIRE_KEEP_BATCH),--keep-batch) \
	$(if $(STAGE_RETIRE_OVERWRITE),--overwrite) \
	$(if $(STAGE_RETIRE_DRY_RUN),--dry-run))
QUALITY_PATHS      ?= scripts/agent_command_registry.py scripts/agent_registry.py scripts/agent_shell.py scripts/agent_skill_registry.py scripts/agent_task_manager.py scripts/check_env.py scripts/context_providers.py scripts/deterministic_tool_utils.py scripts/hook_runtime.py scripts/indexed_memory.py scripts/orchestration_inspect.py scripts/prompt_templates.py scripts/request_router.py scripts/retire_staged_reference_batch.py scripts/retrieval_utils.py scripts/revit_entity_lookup.py scripts/runtime_contracts.py scripts/train.py scripts/validate_release_artifacts.py scripts/package_release_bundle.py scripts/workflow_registry.py tests
TEST_PATHS         ?= tests
ARGS               ?=
WORKFLOW           ?=

.PHONY: all quality quality-release release-bundle release-verify lint test check prepare train train-manifest export export-verify gguf evaluate evaluate-quick evaluate-release agent-shell route-request memory-add memory-query memory-import memory-consolidate memory-rebuild-index workflow-list workflow-show workflow-validate workflow-run task-list task-status task-show task-attach task-start-workflow task-start-dream task-start-subagent task-cancel task-resume inspect-hooks inspect-providers inspect-commands inspect-skills inspect-agents inspect-tools inspect-tasks inspect-execution inspect-shell source-registry source-materialize stage-archives stage-organize stage-import stage-retire retrieval-corpus golden-benchmark generate catalog scrape-public pdf-notes ingest-reference-folder merge-examples revit-ingest revit-lookup estimate-index estimate-lookup estimating-reference-examples estimating-canonical electrician-corpus clean help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

all: check prepare train export gguf evaluate ## Run the full pipeline end-to-end

quality: lint test ## Run the core CPU-safe quality gate

quality-release: quality release-verify ## Run CPU-safe quality checks plus release artifact validation

lint: ## Run Ruff lint and format checks on core modules and tests
	$(PYTHON) -m ruff check --select F $(QUALITY_PATHS)
	$(PYTHON) -m ruff format --check $(QUALITY_PATHS)

test: ## Run pure-Python unit tests
	PYTHONPATH=$(CURDIR)/scripts $(PYTHON) -m pytest $(TEST_PATHS)

check: ## Validate environment (Python, CUDA, packages, secrets)
	$(PYTHON) scripts/check_env.py

prepare: ## Prepare JSONL data → processed train/valid splits
	$(PYTHON) scripts/prepare_data.py --config $(CONFIG)

train: ## QLoRA fine-tuning with Unsloth + SFTTrainer
	$(PYTHON) scripts/train.py --config $(CONFIG)

train-manifest: ## Backfill train manifest from existing adapter/checkpoint artifacts
	$(PYTHON) scripts/train.py --config $(CONFIG) --manifest_only

export: ## Merge adapters → 16-bit model
	$(PYTHON) scripts/export.py --config $(CONFIG)

export-verify: ## Verify existing merged/GGUF artifacts, smoke tests, and export manifest
	$(PYTHON) scripts/export.py --config $(CONFIG) --verify_existing

release-bundle: ## Build a lightweight release-verification bundle from current artifacts
	$(PYTHON) scripts/package_release_bundle.py \
		--config $(CONFIG) \
		--out $(if $(OUT),$(OUT),dist/release-verification-bundle.tar.gz) \
		$(if $(INCLUDE_GGUF),--include-gguf,)

release-verify: ## Validate existing release manifests and results without rerunning evaluation
	$(PYTHON) scripts/validate_release_artifacts.py --config $(CONFIG)

gguf: $(GGUF_Q4) ## Convert to GGUF Q4_K_M and register with Ollama
	@echo "Registering model with Ollama …"
	$(OLLAMA) create simcoe -f $(MODELFILE)
	@echo "✅  Model registered. Run: ollama run simcoe"

$(GGUF_Q4): $(MERGED_DIR)/config.json
	@mkdir -p $(GGUF_DIR)
	$(PYTHON) $(LLAMA_CPP)/convert_hf_to_gguf.py $(MERGED_DIR) \
		--outfile $(GGUF_F16) --outtype f16
	$(LLAMA_CPP)/build/bin/llama-quantize $(GGUF_F16) $(GGUF_Q4) Q4_K_M
	@echo "Cleaning up intermediate F16 GGUF …"
	rm -f $(GGUF_F16)
	@echo "✅  GGUF Q4_K_M ready: $(GGUF_Q4)"

evaluate: ## Score outputs with ROUGE, exact match, and LLM-as-judge
	$(PYTHON) scripts/evaluate.py --config $(CONFIG) $(ARGS)

evaluate-quick: ## Run a faster metrics-only evaluation profile
	$(PYTHON) scripts/evaluate.py --config $(CONFIG) --quick --metrics_only $(ARGS)

evaluate-release: ## Evaluate and fail if configured release thresholds are not met
	$(PYTHON) scripts/evaluate.py --config $(CONFIG) --release $(ARGS)

agent-shell: ## Start the local agent shell (pass one-shot prompts or session args via ARGS)
	$(PYTHON) scripts/agent_shell.py --config $(CONFIG) $(ARGS)

route-request: ## Classify a single request into text/retrieval/tool/drawing routes (pass inputs via ARGS)
	$(PYTHON) scripts/request_router.py --config $(CONFIG) $(ARGS)

memory-add: ## Append a memory event and rebuild the topic/index projections (pass inputs via ARGS)
	$(PYTHON) scripts/indexed_memory.py --config $(CONFIG) add $(ARGS)

memory-query: ## Query the indexed memory store (pass inputs via ARGS)
	$(PYTHON) scripts/indexed_memory.py --config $(CONFIG) query $(ARGS)

memory-import: ## Import curated memory rows from JSON, JSONL, or YAML (pass inputs via ARGS)
	$(PYTHON) scripts/indexed_memory.py --config $(CONFIG) import $(ARGS)

memory-consolidate: ## Rebuild topic files from the append-only memory event log
	$(PYTHON) scripts/indexed_memory.py --config $(CONFIG) consolidate

memory-rebuild-index: ## Rebuild the pointer-only memory index from topic records
	$(PYTHON) scripts/indexed_memory.py --config $(CONFIG) rebuild-index

workflow-list: ## List checked-in operator workflows from the registry manifest
	$(PYTHON) scripts/workflow_registry.py --config $(CONFIG) list

workflow-show: ## Show one checked-in operator workflow (set WORKFLOW=name)
	@if [[ -z "$(WORKFLOW)" ]]; then \
		echo "Usage: make workflow-show WORKFLOW=name CONFIG=config.yaml"; \
		exit 1; \
	fi
	$(PYTHON) scripts/workflow_registry.py --config $(CONFIG) show $(WORKFLOW)

workflow-validate: ## Validate the checked-in workflow registry manifest
	$(PYTHON) scripts/workflow_registry.py --config $(CONFIG) validate

workflow-run: ## Run one checked-in operator workflow (set WORKFLOW=name and pass vars via ARGS)
	@if [[ -z "$(WORKFLOW)" ]]; then \
		echo "Usage: make workflow-run WORKFLOW=name CONFIG=config.yaml ARGS='--var key=value'"; \
		exit 1; \
	fi
	$(PYTHON) scripts/workflow_registry.py --config $(CONFIG) run $(WORKFLOW) $(ARGS)

task-list: ## List managed background tasks (pass filters via ARGS)
	$(PYTHON) scripts/agent_task_manager.py --config $(CONFIG) list $(ARGS)

task-status: ## Show a compact managed-task status summary (pass filters via ARGS)
	$(PYTHON) scripts/agent_task_manager.py --config $(CONFIG) status $(ARGS)

task-show: ## Show one managed background task (set TASK_ID=id or pass via ARGS)
	@if [[ -z "$(TASK_ID)" && -z "$(strip $(ARGS))" ]]; then \
		echo "Usage: make task-show TASK_ID=agent-task-123 CONFIG=config.yaml"; \
		exit 1; \
	fi
	$(PYTHON) scripts/agent_task_manager.py --config $(CONFIG) show $(if $(TASK_ID),$(TASK_ID),$(ARGS))

task-attach: ## Reattach to a managed background task log stream (set TASK_ID=id and pass cursor options via ARGS)
	@if [[ -z "$(TASK_ID)" ]]; then \
		echo "Usage: make task-attach TASK_ID=agent-task-123 CONFIG=config.yaml ARGS='--cursor 0 --limit 20'"; \
		exit 1; \
	fi
	$(PYTHON) scripts/agent_task_manager.py --config $(CONFIG) attach $(TASK_ID) $(ARGS)

task-start-workflow: ## Start a checked-in workflow as a managed background task (set WORKFLOW=name)
	@if [[ -z "$(WORKFLOW)" ]]; then \
		echo "Usage: make task-start-workflow WORKFLOW=name CONFIG=config.yaml ARGS='--var key=value'"; \
		exit 1; \
	fi
	$(PYTHON) scripts/agent_task_manager.py --config $(CONFIG) start-workflow $(WORKFLOW) $(ARGS)

task-start-dream: ## Start a managed background dream run
	$(PYTHON) scripts/agent_task_manager.py --config $(CONFIG) start-dream $(ARGS)

task-start-subagent: ## Start a bounded managed background subagent task (pass prompt/options via ARGS)
	$(PYTHON) scripts/agent_task_manager.py --config $(CONFIG) start-subagent $(ARGS)

task-cancel: ## Request cancellation for one managed background task (set TASK_ID=id or pass via ARGS)
	@if [[ -z "$(TASK_ID)" && -z "$(strip $(ARGS))" ]]; then \
		echo "Usage: make task-cancel TASK_ID=agent-task-123 CONFIG=config.yaml"; \
		exit 1; \
	fi
	$(PYTHON) scripts/agent_task_manager.py --config $(CONFIG) cancel $(if $(TASK_ID),$(TASK_ID),$(ARGS))

task-resume: ## Resume a failed, cancelled, or pending managed background task (set TASK_ID=id or pass via ARGS)
	@if [[ -z "$(TASK_ID)" && -z "$(strip $(ARGS))" ]]; then \
		echo "Usage: make task-resume TASK_ID=agent-task-123 CONFIG=config.yaml"; \
		exit 1; \
	fi
	$(PYTHON) scripts/agent_task_manager.py --config $(CONFIG) resume $(if $(TASK_ID),$(TASK_ID),$(ARGS))

inspect-hooks: ## Inspect configured hooks for the selected config
	$(PYTHON) scripts/orchestration_inspect.py --config $(CONFIG) hooks

inspect-providers: ## Inspect configured context providers for the selected config
	$(PYTHON) scripts/orchestration_inspect.py --config $(CONFIG) providers

inspect-commands: ## Inspect local agent shell command metadata (pass --command-name via ARGS for one command)
	$(PYTHON) scripts/orchestration_inspect.py --config $(CONFIG) commands $(ARGS)

inspect-skills: ## Inspect local markdown skill metadata (pass --skill-name via ARGS for one skill)
	$(PYTHON) scripts/orchestration_inspect.py --config $(CONFIG) skills $(ARGS)

inspect-agents: ## Inspect local markdown agent metadata (pass --agent-name via ARGS for one agent)
	$(PYTHON) scripts/orchestration_inspect.py --config $(CONFIG) agents $(ARGS)

inspect-tools: ## Inspect local agent tool metadata (pass --tool-name via ARGS for one tool)
	$(PYTHON) scripts/orchestration_inspect.py --config $(CONFIG) tools $(ARGS)

inspect-tasks: ## Inspect managed background tasks (pass --task-id via ARGS for one task)
	$(PYTHON) scripts/orchestration_inspect.py --config $(CONFIG) tasks $(ARGS)

inspect-execution: ## Inspect saved execution summary from evaluation results (pass --results via ARGS if needed)
	$(PYTHON) scripts/orchestration_inspect.py --config $(CONFIG) execution $(ARGS)

inspect-shell: ## Inspect saved local agent shell sessions (pass --session-id via ARGS for detail)
	$(PYTHON) scripts/orchestration_inspect.py --config $(CONFIG) shell $(ARGS)

source-registry: ## Build a registry manifest for the configured external source root
	$(PYTHON) scripts/build_source_registry.py --config $(CONFIG)

source-materialize: ## Copy selected registry assets into repo-managed sources/ (pass selectors via ARGS)
	$(PYTHON) scripts/materialize_sources.py --config $(CONFIG) $(ARGS)

stage-archives: ## Stage selected external archives into a repo-local batch (set BATCH=name and STAGE_ARCHIVE_NAME or STAGE_ARCHIVE_LIST_FILE)
	@if [[ -z "$(BATCH)" ]]; then \
		echo "Usage: make stage-archives BATCH=batch-name STAGE_ARCHIVE_NAME='SCHEDULE.zip' STAGE_ARCHIVES_OVERWRITE=1"; \
		echo "   or: make stage-archives BATCH=batch-name STAGE_ARCHIVE_LIST_FILE=path/to/archive_selection.txt"; \
		exit 1; \
	fi
	@if [[ -z "$(STAGE_ARCHIVE_NAME)" && -z "$(STAGE_ARCHIVE_LIST_FILE)" ]]; then \
		echo "Provide STAGE_ARCHIVE_NAME='file.zip' or STAGE_ARCHIVE_LIST_FILE=path/to/archive_selection.txt"; \
		exit 1; \
	fi
	$(PYTHON) scripts/stage_reference_archives.py \
		--source-dir "$(STAGE_SOURCE_DIR)" \
		--staging-root "$(STAGING_ROOT)" \
		--batch-name "$(BATCH)" $(STAGE_ARCHIVES_FLAGS)

stage-organize: ## Refresh the deduped bucketed review view for one staged archive batch (set BATCH=name)
	@if [[ -z "$(BATCH)" ]]; then \
		echo "Usage: make stage-organize BATCH=batch-name STAGING_ROOT=data/staging/reference_archive_batches"; \
		exit 1; \
	fi
	$(PYTHON) scripts/organize_staged_references.py \
		--batch-dir "$(STAGING_ROOT)/$(BATCH)" \
		--link-mode $(STAGE_LINK_MODE) \
		--overwrite

stage-import: ## Refresh the bucketed view and import one staged archive batch into repo-managed sources/ (set BATCH=name)
	@if [[ -z "$(BATCH)" ]]; then \
		echo "Usage: make stage-import BATCH=batch-name CONFIG=config.electrician.yaml"; \
		exit 1; \
	fi
	$(PYTHON) scripts/organize_staged_references.py \
		--batch-dir "$(STAGING_ROOT)/$(BATCH)" \
		--link-mode $(STAGE_LINK_MODE) \
		--overwrite
	$(PYTHON) scripts/import_staged_reference_batch.py \
		--config $(CONFIG) \
		--staging-root "$(STAGING_ROOT)" \
		--batch-name "$(BATCH)" $(STAGE_IMPORT_FLAGS)

stage-retire: ## Archive manifests for one staged batch and prune it after import (set BATCH=name)
	@if [[ -z "$(BATCH)" ]]; then \
		echo "Usage: make stage-retire BATCH=batch-name STAGE_RETIRE_DRY_RUN=1"; \
		echo "   add STAGE_RETIRE_KEEP_BATCH=1 to archive manifests without deleting the source batch"; \
		exit 1; \
	fi
	$(PYTHON) scripts/retire_staged_reference_batch.py \
		--staging-root "$(STAGING_ROOT)" \
		--batch-name "$(BATCH)" $(STAGE_RETIRE_FLAGS)

retrieval-corpus: ## Build a deduplicated retrieval corpus from source-grounded examples
	$(PYTHON) scripts/build_retrieval_corpus.py \
		--source $(RETRIEVAL_SOURCE) \
		--out $(RETRIEVAL_OUT) \
		--manifest $(RETRIEVAL_MANIFEST)

golden-benchmark: ## Build the curated golden benchmark from the checked-in spec
	$(PYTHON) scripts/build_golden_benchmark.py \
		--config $(CONFIG) \
		--source $(GOLDEN_SOURCE) \
		--spec $(GOLDEN_SPEC) \
		--out $(GOLDEN_OUT) \
		--manifest $(GOLDEN_MANIFEST)

generate: ## Generate synthetic training data using Ollama (pass overrides via ARGS)
	$(PYTHON) scripts/generate_data.py --config $(CONFIG) --topics topics.yaml \
		--out data/raw/generated.jsonl --count 10 $(ARGS)
	@echo "✅  Generated data saved to data/raw/generated.jsonl"
	@echo "    To merge: cat data/raw/generated.jsonl >> data/raw/dataset.jsonl"

catalog: ## Build training data from a real manufacturer/distributor catalog export
	@if [[ -z "$(SOURCE)" ]]; then \
		echo "Usage: make catalog SOURCE=path/to/catalog.csv OUT=data/raw/catalog_examples.jsonl"; \
		exit 1; \
	fi
	$(PYTHON) scripts/build_catalog_data.py --source $(SOURCE) \
		--out $(if $(OUT),$(OUT),data/raw/catalog_examples.jsonl)
	@echo "✅  Catalog-derived data built. Review it before merging into data/raw/dataset.jsonl"

scrape-public: ## Scrape public manufacturer/spec pages and public labor-rate pages
	$(PYTHON) scripts/scrape_public_data.py --sources sources/public_sources.yaml \
		--out data/raw/public_scrape.jsonl
	@echo "✅  Public web data scraped to data/raw/public_scrape.jsonl"
	@echo "    To turn product, wage, and reference records into training examples:"
	@echo "    $(PYTHON) scripts/build_catalog_data.py --source data/raw/public_scrape.jsonl --out data/raw/public_catalog_examples.jsonl"

pdf-notes: ## Extract short attributed reference notes from a local PDF or configured managed default
	$(PYTHON) scripts/extract_reference_pdf.py \
		--config $(CONFIG) \
		$(if $(SOURCE),--source $(SOURCE),) \
		$(if $(MANAGED_KEY),--managed-key $(MANAGED_KEY),) \
		$(if $(SOURCE_NAME),--source-name "$(SOURCE_NAME)",) \
		$(if $(CHUNK_SIZE),--chunk-size $(CHUNK_SIZE),) \
		$(if $(MIN_CHARS),--min-chars $(MIN_CHARS),) \
		$(if $(START_PAGE),--start-page $(START_PAGE),) \
		$(if $(END_PAGE),--end-page $(END_PAGE),) \
		--out $(if $(OUT),$(OUT),data/raw/pdf_reference_notes.jsonl)
	@echo "✅  PDF reference notes extracted"
	@echo "    To turn notes into examples when appropriate:"
	@echo "    $(PYTHON) scripts/build_catalog_data.py --source $(if $(OUT),$(OUT),data/raw/pdf_reference_notes.jsonl) --out data/raw/pdf_reference_examples.jsonl"

ingest-reference-folder: ## Extract mixed local manuals, notes, and code files into JSONL from a managed default or explicit root
	$(PYTHON) scripts/ingest_reference_folder.py \
		--config $(CONFIG) \
		$(if $(ROOT),--root "$(ROOT)",) \
		$(if $(MANAGED_KEY),--managed-key $(MANAGED_KEY),) \
		$(if $(SOURCE_NAME),--source-name "$(SOURCE_NAME)",) \
		$(if $(TEXT_CHUNK_LINES),--text-chunk-lines $(TEXT_CHUNK_LINES),) \
		$(if $(PDF_CHUNK_SIZE),--pdf-chunk-size $(PDF_CHUNK_SIZE),) \
		$(if $(PDF_MIN_CHARS),--pdf-min-chars $(PDF_MIN_CHARS),) \
		--out $(if $(OUT),$(OUT),data/raw/reference_folder.jsonl)
	@echo "✅  Local reference folder ingested"
	@echo "    To build reviewed examples from the output:"
	@echo "    $(PYTHON) scripts/build_catalog_data.py --source $(if $(OUT),$(OUT),data/raw/reference_folder.jsonl) --out data/raw/reference_folder_examples.jsonl"

merge-examples: ## Merge multiple example JSONL files into one deduplicated corpus
	@if [[ -z "$(SOURCES)" ]]; then \
		echo "Usage: make merge-examples SOURCES='file1.jsonl file2.jsonl' OUT=data/raw/merged_examples.jsonl"; \
		exit 1; \
	fi
	$(PYTHON) scripts/merge_example_sets.py \
		$(foreach src,$(SOURCES),--source "$(src)") \
		--out $(if $(OUT),$(OUT),data/raw/merged_examples.jsonl)
	@echo "✅  Example sets merged"

revit-ingest: ## Normalize Revit exports or family directories into reference JSONL, using managed defaults when configured
	$(PYTHON) scripts/revit_ingestion.py \
		--config $(CONFIG) \
		$(if $(MANAGED_KEY),--managed-key $(MANAGED_KEY),) \
		$(if $(SOURCE),--source "$(SOURCE)",) \
		$(if $(FAMILY_DIR),--family-dir "$(FAMILY_DIR)",) \
		$(if $(INCLUDE_RVT),--include-rvt,) \
		--out $(if $(OUT),$(OUT),data/raw/revit_family_index.jsonl)
	@echo "✅  Revit reference data built for retrieval and deterministic lookup workflows"

revit-lookup: ## Query the deterministic Revit/entity lookup runtime
	$(PYTHON) scripts/revit_entity_lookup.py \
		--config $(CONFIG) \
		$(if $(INDEX),--index $(INDEX),) \
		$(if $(QUERY),--query "$(QUERY)",) \
		$(if $(RECORD_ID),--record-id $(RECORD_ID),) \
		$(if $(LOOKUP_KEY),--lookup-key $(LOOKUP_KEY),) \
		$(if $(FAMILY_NAME),--family-name "$(FAMILY_NAME)",) \
		$(if $(TYPE_NAME),--type-name "$(TYPE_NAME)",) \
		$(if $(FAMILY_AND_TYPE),--family-and-type "$(FAMILY_AND_TYPE)",) \
		$(if $(CATEGORY),--category "$(CATEGORY)",) \
		$(if $(SUBCATEGORY),--subcategory "$(SUBCATEGORY)",) \
		$(if $(MANUFACTURER),--manufacturer "$(MANUFACTURER)",) \
		$(if $(UNIT),--unit "$(UNIT)",) \
		$(if $(SOURCE_NAME),--source-name "$(SOURCE_NAME)",) \
		$(if $(TOP_K),--top-k $(TOP_K),) \
		$(if $(MIN_SCORE),--min-score $(MIN_SCORE),) \
		$(if $(OUT),--out $(OUT),)

estimate-index: ## Build estimate lookup records, preferring managed HAR defaults when available
	$(PYTHON) scripts/build_estimate_index.py \
		--config $(CONFIG) \
		$(if $(MANAGED_KEY),--managed-key $(MANAGED_KEY),) \
		$(if $(MAPPING),--mapping $(MAPPING),) \
		$(if $(RSMEANS),--rsmeans $(RSMEANS),) \
		$(if $(RSMEANS_HAR_DIR),--rsmeans-har-dir $(RSMEANS_HAR_DIR),) \
		--out $(if $(OUT),$(OUT),data/raw/estimate_index.jsonl)
	@echo "✅  Estimate index built for live lookup"

estimate-lookup: ## Query the deterministic estimate lookup runtime
	$(PYTHON) scripts/estimate_lookup.py \
		--config $(CONFIG) \
		$(if $(INDEX),--index $(INDEX),) \
		$(if $(QUERY),--query "$(QUERY)",) \
		$(if $(RECORD_ID),--record-id $(RECORD_ID),) \
		$(if $(LOOKUP_KEY),--lookup-key $(LOOKUP_KEY),) \
		$(if $(FAMILY_NAME),--family-name "$(FAMILY_NAME)",) \
		$(if $(CATEGORY),--category "$(CATEGORY)",) \
		$(if $(MANUFACTURER),--manufacturer "$(MANUFACTURER)",) \
		$(if $(UNIT),--unit "$(UNIT)",) \
		$(if $(SOURCE_NAME),--source-name "$(SOURCE_NAME)",) \
		$(if $(TOP_K),--top-k $(TOP_K),) \
		$(if $(MIN_SCORE),--min-score $(MIN_SCORE),) \
		$(if $(QUANTITY),--quantity $(QUANTITY),) \
		$(if $(OUT),--out $(OUT),)

estimating-reference-examples: ## Convert managed estimating reference records into examples only after explicit training approval
	$(PYTHON) scripts/build_catalog_data.py --source $(ESTIMATING_REFERENCE_OUT) \
		$(if $(ALLOW_CONTRACT_OVERRIDE),--allow_contract_override,) \
		--out $(ESTIMATING_REFERENCE_EXAMPLES_OUT)
	@echo "✅  Managed estimating reference examples built at $(ESTIMATING_REFERENCE_EXAMPLES_OUT)"

estimating-canonical: ## Rebuild the managed estimating notes, examples, and estimate index with repo-managed defaults
	$(MAKE) pdf-notes CONFIG=$(CONFIG) OUT=$(ESTIMATING_NOTES_OUT)
	$(PYTHON) scripts/build_catalog_data.py --source $(ESTIMATING_NOTES_OUT) \
		--out $(ESTIMATING_NOTES_EXAMPLES_OUT)
	$(MAKE) ingest-reference-folder CONFIG=$(CONFIG) MANAGED_KEY=estimating_reference_root OUT=$(ESTIMATING_REFERENCE_OUT)
	$(MAKE) estimate-index CONFIG=$(CONFIG) OUT=$(ESTIMATE_INDEX_OUT)
	@echo "✅  Canonical managed estimating artifacts refreshed"

electrician-corpus: estimating-canonical ## Rebuild the canonical electrician corpus with managed estimating examples
	$(MAKE) merge-examples SOURCES="$(ELECTRICIAN_CORPUS_SOURCES)" OUT=$(ELECTRICIAN_CORPUS_OUT)
	@echo "✅  Canonical electrician corpus refreshed at $(ELECTRICIAN_CORPUS_OUT)"

clean: ## Remove all generated artifacts (data/processed, models, evals)
	@echo "Removing generated artifacts …"
	rm -rf data/processed
	rm -rf models/adapters models/merged_16bit models/gguf
	rm -rf evals/results.json
	rm -rf .pytest_cache .ruff_cache
	@echo "Done."
