# Makefile — orchestrates the fine-tuning pipeline in the correct order.
#
# Usage:
#   make all          # run the full pipeline: check → prepare → train → export → evaluate
#   make check        # validate environment only
#   make prepare      # prepare dataset only
#   make train        # train only (requires prepared data)
#   make export       # export only (requires trained adapters)
#   make gguf         # convert merged model to GGUF and register with Ollama
#   make evaluate     # evaluate only (requires exported model)
#   make generate     # generate synthetic data using Ollama (requires running model)
#   make clean        # remove all generated artifacts
#
# Override the config file:
#   make all CONFIG=my_config.yaml

SHELL  := /bin/bash
PYTHON := python
CONFIG := config.yaml

# Paths
LLAMA_CPP     := $(HOME)/src/llama.cpp
MERGED_DIR    := models/merged_16bit
GGUF_DIR      := models/gguf
GGUF_F16      := $(GGUF_DIR)/model-f16.gguf
GGUF_Q4       := $(GGUF_DIR)/model-Q4_K_M.gguf
MODELFILE     := $(GGUF_DIR)/Modelfile
OLLAMA        := $(HOME)/.local/bin/ollama

.PHONY: all check prepare train export gguf evaluate generate catalog scrape-public pdf-notes ingest-reference-folder merge-examples revit-ingest estimate-index clean help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

all: check prepare train export gguf evaluate ## Run the full pipeline end-to-end

check: ## Validate environment (Python, CUDA, packages, secrets)
	$(PYTHON) scripts/check_env.py

prepare: ## Prepare JSONL data → processed train/valid splits
	$(PYTHON) scripts/prepare_data.py --config $(CONFIG)

train: ## QLoRA fine-tuning with Unsloth + SFTTrainer
	$(PYTHON) scripts/train.py --config $(CONFIG)

export: ## Merge adapters → 16-bit model
	$(PYTHON) scripts/export.py --config $(CONFIG)

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
	$(PYTHON) scripts/evaluate.py --config $(CONFIG)

generate: ## Generate synthetic training data using Ollama
	$(PYTHON) scripts/generate_data.py --topics topics.yaml \
		--out data/raw/generated.jsonl --count 10
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

pdf-notes: ## Extract short attributed reference notes from a local PDF
	@if [[ -z "$(SOURCE)" ]]; then \
		echo "Usage: make pdf-notes SOURCE=sources/manual.pdf OUT=data/raw/manual_notes.jsonl"; \
		exit 1; \
	fi
	$(PYTHON) scripts/extract_reference_pdf.py \
		--source $(SOURCE) \
		$(if $(SOURCE_NAME),--source-name "$(SOURCE_NAME)",) \
		$(if $(CHUNK_SIZE),--chunk-size $(CHUNK_SIZE),) \
		$(if $(MIN_CHARS),--min-chars $(MIN_CHARS),) \
		$(if $(START_PAGE),--start-page $(START_PAGE),) \
		$(if $(END_PAGE),--end-page $(END_PAGE),) \
		--out $(if $(OUT),$(OUT),data/raw/pdf_reference_notes.jsonl)
	@echo "✅  PDF reference notes extracted"
	@echo "    To turn notes into examples when appropriate:"
	@echo "    $(PYTHON) scripts/build_catalog_data.py --source $(if $(OUT),$(OUT),data/raw/pdf_reference_notes.jsonl) --out data/raw/pdf_reference_examples.jsonl"

ingest-reference-folder: ## Extract mixed local manuals, notes, and code files into JSONL
	@if [[ -z "$(ROOT)" ]]; then \
		echo "Usage: make ingest-reference-folder ROOT=/path/to/folder OUT=data/raw/reference_folder.jsonl"; \
		exit 1; \
	fi
	$(PYTHON) scripts/ingest_reference_folder.py \
		--root "$(ROOT)" \
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

revit-ingest: ## Normalize Revit exports or family directories into reference JSONL
	@if [[ -z "$(SOURCE)" && -z "$(FAMILY_DIR)" ]]; then \
		echo "Usage: make revit-ingest SOURCE=path/to/export.csv OUT=data/raw/revit_family_index.jsonl"; \
		echo "   or: make revit-ingest FAMILY_DIR=/path/to/Revit/Families OUT=data/raw/revit_family_index.jsonl"; \
		exit 1; \
	fi
	$(PYTHON) scripts/revit_ingestion.py \
		$(if $(SOURCE),--source $(SOURCE),) \
		$(if $(FAMILY_DIR),--family-dir $(FAMILY_DIR),) \
		$(if $(INCLUDE_RVT),--include-rvt,) \
		--out $(if $(OUT),$(OUT),data/raw/revit_family_index.jsonl)
	@echo "✅  Revit reference data built for retrieval workflows"

estimate-index: ## Build estimate lookup records, preferring HAR costs over stale crosswalk totals
	@if [[ -z "$(MAPPING)" && -z "$(RSMEANS)" && -z "$(RSMEANS_HAR_DIR)" ]]; then \
		echo "Usage: make estimate-index MAPPING=path/to/stratus_rsmeans_map_FULL.csv OUT=data/raw/estimate_index.jsonl"; \
		echo "   or: make estimate-index RSMEANS_HAR_DIR=/path/to/RSmeans OUT=data/raw/estimate_index.jsonl"; \
		echo "   or: make estimate-index RSMEANS=path/to/corrected_rsmeans.csv OUT=data/raw/estimate_index.jsonl"; \
		exit 1; \
	fi
	$(PYTHON) scripts/build_estimate_index.py \
		$(if $(MAPPING),--mapping $(MAPPING),) \
		$(if $(RSMEANS),--rsmeans $(RSMEANS),) \
		$(if $(RSMEANS_HAR_DIR),--rsmeans-har-dir $(RSMEANS_HAR_DIR),) \
		--out $(if $(OUT),$(OUT),data/raw/estimate_index.jsonl)
	@echo "✅  Estimate index built for live lookup"

clean: ## Remove all generated artifacts (data/processed, models, evals)
	@echo "Removing generated artifacts …"
	rm -rf data/processed
	rm -rf models/adapters models/merged_16bit models/gguf
	rm -rf evals/results.json
	@echo "Done."
