# Prompt Engineering Library

This directory is a guidance-first library for internal prompt engineers.
It is designed to help condition models in ways that fit the current repo
instead of fighting its prompt stack.

The catalog lives in [system_prompt_templates.yaml](system_prompt_templates.yaml).
The library now has two roles:

- human guidance for prompt engineers
- optional runtime template selection through config `system_prompts.*`

The checked-in configs use behavior-equivalent template ids for the existing
generation, judge, and Ollama export system prompts, while broader conditioning
templates remain available for future runtime use.

## What This Repo Already Does

The current prompt stack has a fixed shape:

1. Optional system prompt from a chat client or the Ollama `Modelfile` `SYSTEM` block.
2. `### Instruction:` content created by the training and evaluation helpers.
3. Optional `### Input:` content when a raw example includes extra context.
4. Optional `### Memory Hints:` inserted before the answer marker.
5. Optional `### Retrieved Context:` inserted after memory hints and before the answer marker.
6. `### Response:` where generation starts.

That stack is defined by the current repo surfaces:

- [../scripts/prepare_data.py](../scripts/prepare_data.py) formats training rows into `### Instruction` and `### Response` text.
- [../scripts/evaluate.py](../scripts/evaluate.py) builds inference prompts and judge messages.
- [../scripts/retrieval_utils.py](../scripts/retrieval_utils.py) inserts memory and retrieval context ahead of `### Response:`.
- [../scripts/generate_data.py](../scripts/generate_data.py) shows how system prompts are already used for synthetic data generation.
- [../scripts/export.py](../scripts/export.py) writes the Ollama `SYSTEM` block and runtime `TEMPLATE`.

The system prompt library is meant to sit above those mechanics.

## Runtime Selection

Runtime selection is optional and config-driven:

```yaml
system_prompts:
	library_path: "prompts/system_prompt_templates.yaml"
	generate_data:
		template_id: "synthetic-data-generator"
	evaluation_judge:
		template_id: "evaluation-rubric-judge"
	export_modelfile:
		template_id: "runtime-helpful-assistant"
```

Each surface can also pass `variables` when the chosen template requires them.
For example, `grounded-domain-baseline` requires `domain`, while
`runtime-helpful-assistant` does not require any variables.

## What A System Prompt Should Control

Use the system prompt for stable behavior:

- Role and domain perimeter.
- Evidence discipline.
- Uncertainty and fallback behavior.
- Output expectations that should persist across many tasks.

Do not use the system prompt for volatile facts:

- Code sections that may change by edition.
- Prices, labor rates, or vendor-specific data.
- Retrieved source text that should remain attributable.
- Tool outputs that should stay deterministic.

If a fact can change independently of the model, it belongs in retrieval, memory,
or a deterministic tool instead of a long-lived system prompt.

## Conditioning Levers

### 1. Role Before Tone

Start by constraining the model's operating boundary.
"You are a domain-focused assistant for NEC code interpretation" is stronger than
stacking style words like helpful, clear, concise, or friendly.

Why it matters:

- Scope framing reduces off-domain drift.
- It gives the model a basis for deciding when not to answer from priors.
- It lets prompt engineers swap domains without rewriting every instruction.

### 2. Evidence Policy Before Eloquence

Tell the model what evidence can ground an answer.
For this repo, that usually means one of four things:

- The user instruction alone.
- The user instruction plus `### Input:`.
- Memory hints inserted by indexed memory.
- Retrieved context inserted by the retrieval layer.

If the prompt engineer does not define how those sources should be treated, the
model tends to blend them with background priors. That is usually where fluent
hallucinations start.

### 3. Explicit Uncertainty Behavior

Generic warnings like "be careful" do not condition the model well.
Useful uncertainty behavior is concrete:

- Name the kinds of missing input that should stop a definitive answer.
- Tell the model whether to ask a clarifying question or provide a bounded partial answer.
- Require it to separate supported claims from assumptions when the distinction matters.

### 4. Output Contract Only When It Helps

Use formatting constraints sparingly.
This repo already relies on `### Response:` as the completion boundary, so a
system prompt should not demand an incompatible outer wrapper.

Good output contracts:

- Summarize in 3-5 bullets.
- Cite source name and section when present.
- Separate supported findings from assumptions.

Weak output contracts:

- Long JSON schemas for tasks that are really explanatory.
- Stylistic instructions that drown out the user request.
- Requesting exact citations when no source text is available.

### 5. Route Fit

Conditioning should match the route.

- `text`: Use broad role and fallback guidance.
- `retrieval`: Add strong evidence discipline and insufficiency handling.
- `deterministic_tool`: Use prompts that hand off cleanly when a lookup should own the answer.
- Judge or evaluation flows: Use a scoring rubric, not a domain-expert persona.

One prompt template should not try to optimize all routes at once.

## How To Use The Catalog

Each template entry in [system_prompt_templates.yaml](system_prompt_templates.yaml)
contains:

- `purpose`: what the template is trying to condition.
- `use_when` and `avoid_when`: where the template fits or breaks.
- `conditioning_insights`: why the template is written that way.
- `variable_slots`: the parts a prompt engineer is expected to change.
- `anti_patterns`: the most common ways to weaken the template.
- `expected_failure_modes`: what to watch for in evaluation.
- `system_prompt`: the reusable base text.

Treat `variable_slots` as the adaptation seam. If you find yourself rewriting the
whole template for each domain, the template is probably too brittle.

## Recommended Workflow For Prompt Engineers

1. Pick the route first.
2. Choose the narrowest template that matches the risk profile.
3. Fill variable slots with operational language, not marketing language.
4. Check whether the answer should rely on retrieval or a deterministic tool.
5. Verify that the system prompt does not conflict with `### Response:` formatting.
6. Evaluate failure modes before promoting the template.

For example, if a task should answer only from retrieved sources, start from the
source-constrained template instead of weakening the grounded baseline with extra
warnings. That usually produces cleaner behavior and clearer evaluation results.

## Review Checklist

Use this checklist before adopting or revising a template:

- Does the template define scope more clearly than it defines tone?
- Does it explain what evidence the model may rely on?
- Does it tell the model what to do when evidence is missing?
- Does it avoid embedding facts that belong in retrieval or tool output?
- Does it preserve compatibility with the repo's `### Instruction` and `### Response` format?
- Does it name a likely failure mode so evaluation can confirm or reject the design?

## Non-Goals In The First Pass

This library does not yet:

- Auto-select templates by route or domain without config.
- Add a full prompt-version experiment tracker across every artifact.
- Replace retrieval or deterministic tool outputs with system prompt steering.

Those are possible follow-up integrations once the library proves useful as a
human-authored design surface.