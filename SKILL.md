---
name: capability-align
description: 'Use when a materials agent must align materials capabilities of a reference (repo, paper, or blog) onto its own surface and get a gap table plus an introduction card (install placement or refusal) with a test contract. Given a repo, recover its companion paper and a bounded neighborhood (homepage first, web-search only when necessary). Not for running the reference, wrapping it as a nested runtime, executing the test, or implementing the gap. Zero-bundle: host shell/Python only.'
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
- Building/implementing a gap, or executing the card's test (this skill ends at the card).
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

**Blind dual inventory (mandatory when the work has both a paper and a repo
arm).** Inventory the two arms in isolation: finish one side's slot records
(`state` 1 with `span` + verbatim `quote`; `0` with `why_empty`; `unknown` with
`why_unknown`) before opening the other side, and
merge the two sides by product identity only after both are frozen. Reading
both sides in one pass lets the repo's entries ghost-write the paper's missing
steps and flattens the residual this method exists to measure (E1 pilot
contamination lesson). Freeze the paper arm to a file (or a separate isolated
context) before opening the repo arm and record the method in
`surfaces.arms`. If neither is possible, set `blind: false`, cap paper-arm
confidence at `medium`, and mark the fork `contaminated`; it is then not a
measurement.

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
**Pre-flight sync (mandatory when the host is a git worktree with a remote).**
Alignment verdicts are computed against the host surface; a stale surface
produces wrong `host_has` judgments and wrong cards. Before scanning: fetch
and fast-forward the host (`git fetch && git pull --ff-only`). If the pull is
not clean — local uncommitted changes, diverged history, or a merge conflict —
**stop the run and present `git status` to the caller**: stash, commit,
discard, or proceed-dirty is the caller's decision, never the skill's. Record
the outcome (synced commit hash, `not-a-git-repo`, or `paused-user-decision`)
in the report's `surfaces` block. Only after the sync settles is the host
surface frozen for the run.

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
Apply §Alignment boundary before a row becomes `missing`. Alignment is whether
the host's existing question still stands, not whether the reference menu is
copied. A different question, or the same observable through another code or
file, is a boundary unless the host already offers that question. An honest
refusal closes a boundary; labeling the other quantity as this one does not.

Assign each in-bound reference capability a class from `references/alignment-rules.md`
§Gap classification: `equivalent | partial | missing | agent-competence | host-only | unknown`,
and tag it with a source kind: `host-self-audit | reference-contrast | domain
inference` (`methodology.md` Phase 3). Same domain observable on a different
calculator is `equivalent`, not `missing`.

**Ask what the host must own before calling anything missing.** Record
`host_need` (`none|data|contract|runner|verification`), and add a
`host_need_note` whenever it is not `none`. A standard method the agent can
deliver against a standard library, with a **local check** (form +
`named`/`demonstrated` status) and `host_need: none`, is `agent-competence` —
recorded, not a gap, no card. The host is an agent, not a function table; a
library's module list is not a capability inventory (`capability-ir.md`
granularity 9). `missing` requires ≥1 high/medium evidence entry — from
**validated** evidence, not the raw comparison — **and** a `host_need` that is
not `none` **and** a note naming what is missing; for `verification` it names the
regime, the missing check, and the owning layer. Unverifiable gaps are `unknown`,
never `missing`. A `0` slot means the source was inspected and found silent;
`unknown` means it could not be inspected. Plumbing items never appear in the
gap table.

### 6. Card, then placement
A card places a **bridge**: the domain judgement the host agent does not already
have (`references/alignment-rules.md` §What a skill is for). The equation and the
API are not the bridge — a general agent supplies those. Before writing an
`install` card, name what the agent would get **wrong** without it; if the answer
is "nothing, it just needs the command", the content belongs in a validity slot,
not a body. A body that is mostly prohibitions is a guardrail, not a bridge, and
the placement is wrong.
Join the two projections by product (`references/introduction-card.md`). Do
not merge the projection gap tables. Compute `lambda` from this work's slots
only. Do not override it, and do not copy product names, targets, or validity
sentences from another run or from the fixture gold. `ignore` rows are not
cards. All eight labels stay available, including `insufficient-evidence`
(`s` or `e` unknown → **no card**, gap row `unknown`) and
`validity-unassessed` (install with `prescribed: ["bind"]` only, validity stated
as unknown).

For every joined row with `s=e=1`, judge `kappa` as a separate question — are
the two procedures the same computation? `kappa=1` is forbidden unless
`s=e=1`; when the conflict cannot be decided, `kappa=0`. Never invent a
conflict.

Only an `install` card enters the placement questions
(`references/alignment-rules.md` §Placement): axis → tool-vs-script →
new-skill-vs-extend → constraint ownership → never-low-evidence →
**host-owned (rule 6)**. An `agent-competence` row gets **no card**: there is
nothing to place, and minting one is how a library's module list becomes a fake
surface. An `insufficient-evidence` row also gets no card: an unreadable paper
is not a paper that states nothing. Fill `target`, `question`, `input`,
`validity` plus `validity_owner`, and `forbidden`. Apply §Skill boundary and
tool duty: do not put a second scientific argument in an existing skill body,
and do not open a skill for a single-consumer postprocess or a render. The
target is a host skill/tool/script/extend the host would own; it may call an
upstream scientific engine; it must not clone, wrap, or MCP-mount the reference
agent/hub. A `new-question` install card is ranked last. It is a suggestion,
not alignment debt, and not a build order. An `extend:` card carries both
routing cases: the existing skill still routes its original question, and the
neighbouring skill does not absorb the new one.

A `refuse` card cites rule 7 and stops. `placement` is null. Success is that
the host stays unchanged. Do not invent a skill for a repo entry the paper
never obligates, and do not pick a side of a procedure conflict.

On every card, write the test contract from `introduction-card.md`. Do not
execute it. Order install cards with the stated priority judgment
(`methodology.md` Phase 5: fix-wrongness > honor-promise > extend-surface).

### 7. Portfolio admission
Run this step whenever at least one card is `install`. Freeze the host portfolio
(entries, descriptions, declared products/checks/regimes, route probes, budget).
For each install card, classify its relation to every existing entry using
`references/portfolio-admission.md` §Relation taxonomy; choose the lifecycle
action from the relation→action table; declare the retention probes before
looking at any outcome; then run the set test in the report (not on the host).
A card that passes row-level λ but breaks a retained probe is not admissible.
On failure, try `merge` with the nearest true duplicate, then `demote` out of the
default router; if neither works, defer admission (no lifecycle action for this
card, recorded in Unresolved). Never silently accept the break. A `merge` must
carry the fail-closed evidence block in `references/portfolio-admission.md` §6:
one witness per removed unit (W1/W2/W3), hard surface coverage or verbatim locked
residual, both sides' recall probes, the negative-interaction gate, and the
never-inflate check. No witness means no merge, regardless of similarity. A hard
conflict (`hard-conflict`) is recorded and quarantined; do not pick a side. This
step emits a plan only. It does not edit, merge, install, or execute.

### 8. Report
Write `capability-alignment-report.md` (and `capability-alignment.json` IR)
per `references/report-contract.md` — required sections, validity rules, and the
closing statement verbatim. When at least one card is `install`, the report
includes the Portfolio section: host entries, relations and actions, probes, set
test, lifecycle plan, budget delta, and rollback.

### 9. Self-check
Before declaring the report final, run Layer-1 self-check
(`references/evaluation.md` §Layer 1): the report must open with the
`self_check:` block, all **21** checks green, or the run is not valid and must
be reworked. Checks 19–21 are mandatory when at least one card is `install`; a
run with only refusals still emits an empty `portfolio` block. Then run the
independent re-check on the frozen artifacts (schema, slot recompute, card
routing); if no isolated context is available, record
`independent_check: not-available` and do not present the self-check as
verification.

## Outputs & validity
- Authoritative artifacts: `capability-alignment-report.md` + `capability-alignment.json`
  in the **caller's cwd**, or `research/runs/<ref>-vs-<host>/` when running inside
  this repo. If a report already exists whose `surfaces.reference` is a different
  \(W\), namespace the filename (do not overwrite another pair — MatDiscovery
  already carried a phonopy report).
- Every report line traces to an inventory entry; no fabricated capability names.
- Slots are tri-state: `1` (stated, with quote), `0` (inspected, silent, with
  `why_empty`), `unknown` (not inspected, with `why_unknown`). `unknown` never
  drives an install or a refuse card; it produces an `unknown` gap row and an
  Unresolved entry.
- A capability the agent can deliver with a standard library and a `local_check`
  (form + `named`/`demonstrated` status) is `agent-competence`, not a gap and not
  a card. `named` checks are tallied as unrun. Framework internals are not
  capabilities.
- `missing` carries `host_need_note`; a `verification` need names the regime, the
  missing check, and the owning layer.
- Install cards cite a placement rule; refuse cards cite rule 7. A card
  without a rule is a stub. A card that keeps the reference repo/plugin/MCP as
  the host runtime is invalid (rule 6).
- `extend:` cards carry both routing cases (existing question still routed; the
  neighbour does not absorb the new one).
- `low`-confidence reference entries never drive a `missing` verdict or an
  `install` card.
- Neighborhood capabilities whose only evidence is a search snippet are `low`
  and never drive `missing`.
- Companion paper belongs in core; neighborhood rows stay in the Neighborhood
  section of the report.
- The host's own capability-surface convention overrides these rules where they
  conflict.

## References
- [Quick decisions — the eight decisions a live run needs, in order](references/quick-decisions.md)
- [Methodology — generic method; the phonopy ↔ MatDiscovery run is its validating instance](references/methodology.md)
- [Evaluation — per-run self-check + fixture acceptance tests](references/evaluation.md)
- [Inventory heuristics](references/inventory-heuristics.md)
- [Capability IR](references/capability-ir.md)
- [Alignment & placement rules](references/alignment-rules.md)
- [Introduction card — lambda, install or refuse, test contract](references/introduction-card.md)
- [Portfolio admission — fusion relations, probes, set test, lifecycle plan](references/portfolio-admission.md)
- [Report contract](references/report-contract.md)
- [Report JSON schema](references/report-schema.json)
