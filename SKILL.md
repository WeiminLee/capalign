---
name: capability-align
description: 'Use when a materials agent must audit and align its own capability surface against a reference — a code repository, a paper, or a blog/writeup — and get a gap table plus placement recommendations. Input: repo path / paper / blog text. Output: capability inventories, gap classification, per-gap placement suggestions. Not for running the reference tool itself, and not for implementing the gap. Zero-bundle: runs with the host shell/Python, nothing pre-installed.'
---

# capability-align

Canonical, framework-agnostic skill: last the host agent align its own capability
surface to a reference (repo / paper / blog). Installable in any framework that
loads `SKILL.md` + `references/` (Claude Code / Agent Skills / DeepSeek Harness /
Cursor / .agents). No framework API and no bundled scripts are used — the agent
runs the inventory commands with the host's own shell / Python.

## When to use
- A repo is pointed at (a simulation/DFT/ML tool): "what can it do / what am I missing / should I wrap it".
- A paper is pointed at: which of its methods/workflows should I expose?
- A blog/writeup is pointed at: audit its claims/recipes against my surface.

## When not to use
- Running the reference tool (that is the reference's own scope).
- Building/implementing a gap (this skill ends at the recommendation).
- Generic summarization without capability-surface framing.

## Workflow (follow in order)

### 1. Inventory the reference
Run the heuristics in `references/inventory-heuristics.md` §A/B/C for the given
reference kind. Produce the reference capability list in the IR schema
(`references/capability-ir.md`), including the type vocabulary and the
`confidence` tag on every item.

### 2. Inventory the host agent
Run §D of the heuristics: auto-scan skill dirs / `SKILL.md`s / tool registries;
ask the caller for whatever the scan cannot close. Produce the host capability
list in the same IR, with provenance recorded for each item.

### 3. Normalize
Apply the IR normalization rules (`capability-ir.md` §Normalization): semantic
units, stable ids, collapse duplicates, keep `low` items tagged.

### 4. Cross-validate suspected gaps
Before classifying anything, validate every candidate `missing` / `partial`
against the host (and, cheaply, the reference): grep the capability terms in the
host code, read the artifact spec, check the runner output. Never classify from
the comparison table alone — the first instance produced false candidates this
way (see `methodology.md` §2/§3). Record the validation evidence per candidate.

### 5. Classify & source-tag
Assign each reference capability a class from `references/alignment-rules.md`
§Gap classification: `equivalent | partial | missing | host-only | unknown`, and
tag it with a source kind: `host self-audit | reference-contrast | domain
inference` (`methodology.md` Phase 3). `missing` requires ≥1 high/medium evidence
entry — from **validated** evidence, not the raw comparison — and never from
`low` entries; unverifiable gaps are `unknown`.

### 6. Recommend
For every `missing` / `partial` gap, apply the placement decision
(`references/alignment-rules.md` §Placement): axis → tool-vs-script →
new-skill-vs-extend → constraint ownership → never-low-evidence. Order the
recommendations with the stated priority judgment (`methodology.md` Phase 5:
fix-wrongness > honor-promise > extend-surface; source-kind informs priority),
and cite the rule number each satisfies. The recommendation is a placement
suggestion, not a build order.

### 7. Report & self-check
Write `capability-alignment-report.md` (and `capability-alignment.json` IR)
per `references/report-contract.md` — required sections, validity rules, and the
closing statement verbatim. Before declaring the report final, run Layer-1
self-check (`references/evaluation.md` §Layer 1): the report must open with the
`self_check:` block, all checks green, or the run is not valid and must be reworked.

## Outputs & validity
- Authoritative artifacts: `capability-alignment-report.md` + `capability-alignment.json`
  at the workspace root.
- Every report line traces to an inventory entry; no fabricated capability names.
- Placement recommendations cite the decision rule; a recommendation without a
  rule is a stub.
- `low`-confidence reference entries never drive a `missing` verdict.
- The host's own capability-surface convention overrides these rules where they
  conflict.

## References
- [Methodology — generic method; the phonopy ↔ MatDiscovery run is its validating instance](references/methodology.md)
- [Evaluation — per-run self-check + fixture acceptance tests](references/evaluation.md)
- [Inventory heuristics](references/inventory-heuristics.md)
- [Capability IR](references/capability-ir.md)
- [Alignment & placement rules](references/alignment-rules.md)
- [Report contract](references/report-contract.md)