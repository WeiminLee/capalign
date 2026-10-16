---
name: capability-align
description: 'Use when a materials agent must align materials capabilities of a reference (repo, paper, or blog) onto its own surface and get a gap table plus host-owned placement. Given a repo, recover its companion paper and a bounded neighborhood (homepage first, web-search only when necessary). Not for running the reference, wrapping it as a nested runtime, or implementing the gap. Zero-bundle: host shell/Python only.'
---

# capability-align

Canonical, framework-agnostic skill: last the host agent align its own capability
surface to a reference (repo / paper / blog). Installable in any framework that
loads `SKILL.md` + `references/` (Claude Code / Agent Skills / DeepSeek Harness /
Cursor / .agents). No framework API and no bundled scripts are used — the agent
runs the inventory commands with the host's own shell / Python.

## Intent
The object is **materials capabilities** of a given work \(W\), relative to the
host \(H\). Core layer: what a materials simulation can compute (observables and
simulation workflows). Outer bound: materials-agent methods a domain scientist
would name (benchmark a potential, fine-tune it on their chemistry, distill it
for production). Generic agent packaging is out of scope. Alignment means the
**host owns** the missing verbs on its own skill/tool/runner surface after the
reference agent is gone — not a clone, plugin, or MCP of \(W\) nested inside
\(H\). Rules: `references/alignment-rules.md` §Scope and §Placement 6.

## When to use
- A repo is pointed at (a simulation/DFT/ML tool, or a materials agent/hub): "what materials capabilities do I lack, and where do they land on my surface"; recover the companion paper and a bounded related neighborhood so the spec is not repo-only.
- A homepage/docs URL is pointed at, alone or **with** its GitHub clone: they are one work (official-docs + repo), not two references.
- A paper is pointed at: which of its methods/workflows should the host own?
- A blog/writeup is pointed at: audit its claims/recipes against the host surface.

## When not to use
- Running the reference tool (that is the reference's own scope).
- Building/implementing a gap (this skill ends at the recommendation).
- Nesting the reference as a runtime ("wrap this clone / add its plugin / call its MCP").
- Auditing generic agent plumbing (plugin marketplace, extra MCP, lockfiles, env bootstrap, codegen) as if they were materials gaps.
- Generic summarization without capability-surface framing.
- Unbounded literature review: neighborhood recovery is budgeted and identity-gated, not a related-work crawl.

## Workflow (follow in order)

### 1. Inventory the reference
Run the heuristics in `references/inventory-heuristics.md` §A/B/C for the given
reference kind. Apply §Scope (`alignment-rules.md`): keep materials-sim and
materials-agent methods; drop generic agent plumbing; merge the same observable
on a different calculator into one `compute`. Produce the reference capability
list in the IR schema (`references/capability-ir.md`), including the type
vocabulary and the `confidence` tag on every item.

When the given reference is a **repo**, a **homepage**, or **both**, then run
§E `recover_reference` before step 2: local seeds → homepage (skip search if
the caller already gave it) → web-search **only when necessary** (budget ≤3
queries, ≤5 neighborhood items). A software-only `CITATION.cff` does not force
a paper search. Split **core** \(W=\) given repo + companion paper/official
docs from **neighborhood** \(N=\) identity-gated siblings / cited methods /
declared-related. Registry rosters are one capability, not N neighbors.
Inventory the companion paper with §B when one exists; neighborhood items get
a lightweight inventory (`layer: neighborhood`, confidence ≤ medium). Live
network is never required for a valid run; missing fetch/search is
`unresolved`, not a failed run. Paper/blog inputs skip §E (empty Neighborhood
section).

### 2. Inventory the host agent
Run §D of the heuristics: **scope first** (host doctrine skill/tool root;
exclude worktrees / `node_modules`), then auto-scan skill dirs / `SKILL.md`s /
tool registries; ask the caller for whatever the scan cannot close. Produce
the host capability list in the same IR, with provenance recorded for each
item. If naive `SKILL.md` count and doctrine root disagree by >2×, use the
doctrine root.

### 3. Normalize
Apply the IR normalization rules (`capability-ir.md` §Normalization): semantic
units, stable ids, collapse duplicates, keep `low` items tagged, merge same
observable / drop plumbing (granularity 4 and 8).

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
inference` (`methodology.md` Phase 3). Same domain observable on a different
calculator is `equivalent`, not `missing`. `missing` requires ≥1 high/medium
evidence entry — from **validated** evidence, not the raw comparison — and never
from `low` entries; unverifiable gaps are `unknown`. Plumbing items never
appear in the gap table.

### 6. Recommend
For every `missing` / `partial` gap, apply the placement decision
(`references/alignment-rules.md` §Placement): axis → tool-vs-script →
new-skill-vs-extend → constraint ownership → never-low-evidence →
**host-owned (rule 6)**. A recommendation names a host skill/tool/script/extend
the host would own; it may call an upstream scientific engine; it must not
clone, wrap, or MCP-mount the reference agent/hub. Order the recommendations
with the stated priority judgment (`methodology.md` Phase 5: fix-wrongness >
honor-promise > extend-surface; source-kind informs priority), and cite the
rule number each satisfies. The recommendation is a placement suggestion, not a
build order.

### 7. Report & self-check
Write `capability-alignment-report.md` (and `capability-alignment.json` IR)
per `references/report-contract.md` — required sections, validity rules, and the
closing statement verbatim. Before declaring the report final, run Layer-1
self-check (`references/evaluation.md` §Layer 1): the report must open with the
`self_check:` block, all 10 checks green, or the run is not valid and must be
reworked.

## Outputs & validity
- Authoritative artifacts: `capability-alignment-report.md` + `capability-alignment.json`
  in the **caller's cwd**, or `research/runs/<ref>-vs-<host>/` when running inside
  this repo. If a report already exists whose `surfaces.reference` is a different
  \(W\), namespace the filename (do not overwrite another pair — MatDiscovery
  already carried a phonopy report).
- Every report line traces to an inventory entry; no fabricated capability names.
- Placement recommendations cite the decision rule; a recommendation without a
  rule is a stub. A recommendation that keeps the reference repo/plugin/MCP as
  the host runtime is invalid (rule 6).
- `low`-confidence reference entries never drive a `missing` verdict.
- Neighborhood capabilities whose only evidence is a search snippet are `low`
  and never drive `missing`.
- Companion paper belongs in core; neighborhood rows stay in the Neighborhood
  section of the report.
- The host's own capability-surface convention overrides these rules where they
  conflict.

## References
- [Methodology — generic method; the phonopy ↔ MatDiscovery run is its validating instance](references/methodology.md)
- [Evaluation — per-run self-check + fixture acceptance tests](references/evaluation.md)
- [Inventory heuristics](references/inventory-heuristics.md)
- [Capability IR](references/capability-ir.md)
- [Alignment & placement rules](references/alignment-rules.md)
- [Report contract](references/report-contract.md)