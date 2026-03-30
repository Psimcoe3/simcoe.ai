# Source Notes

This folder can hold both public source configuration and user-supplied local reference material.

## Local Source Authority

- Local source material in this repo or in user-provided reference folders may be used for retrieval, note extraction, and reviewed training-example generation when explicitly authorized by the user.
- `2026_national_electrical_estimator_ebook.pdf` is present as a local estimating source and can be summarized into attributed notes or distilled examples.
- Prefer summarized, attributed records over raw bulk page dumps even when full local use is authorized.

## Managed Copies

- External files should not stay as ad hoc dependencies once they are selected for real use in this repo.
- Use `scripts/build_source_registry.py` to inventory the external root, then `scripts/materialize_sources.py` to copy selected assets into `sources/managed/<namespace>/<runtime_owner>/<asset_kind>/...`.
- Preserve downstream processing against the repo-managed copy so retrieval, training, and review workflows remain reproducible even if the original external folder changes.

## Current Estimating References

- Public article: Bids Analytics, "How To Estimate Electrical Construction Costs: A Contractor's Blueprint"
  - Useful for workflow guidance: document review, scope definition, quantity takeoff, labor adjustments, indirect costs, contingency, and estimate verification.
- Local ebook: `2026_national_electrical_estimator_ebook.pdf`
  - Verified locally as a 553-page PDF generated in 2025 for the 2026 edition.
  - Early pages show it is organized as a trade estimating manual with section-level cost tables beginning with conduit and fittings.

## Recommended Use In This Repo

- Keep price/labor lookups in external reference data such as RSMeans-derived indices.
- Use public articles and local manuals to improve retrieval context, estimating checklists, and explanation quality.
- If you want to operationalize local PDFs, add a dedicated extraction/summarization step that produces short, attributed notes rather than raw page dumps.