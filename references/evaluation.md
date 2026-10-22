# Evaluation — is the alignment valid, and how do we check it?

Two layers. Layer 1 runs on **every run** (a validity gate on the report). Layer 2
is an install-time acceptance test against synthetic fixtures — not benchmark-grade,
but deterministic enough that "the skill works" is checkable by any host.

## Layer 1 — per-run self-check (mandatory, before the report is final)

Before `capability-alignment-report.md` is considered final, run these **18** checks
on it. Any failure is reported in the report's own header (`self_check:` block),
never silently fixed. `not-checkable` is allowed only where the input makes the
check impossible, and it is never a pass.

| # | check | assertion |
|---|---|---|
| 1 | sections | report contains all required sections (`report-contract.md`): surfaces (including `host_sync`, `arms`, `independent_check`, `reference_license`), reference inventory, host inventory, gap table, introduction cards, verification ledger, host-only, neighborhood, unresolved |
| 2 | validated evidence | every `missing` row has ≥1 high/medium evidence entry that came from **validation** (cross-validation step), not the raw comparison — evidence pointers must point at host/reference artifacts (paths/quotes), and the report records the validation command + result (the term searched, the hits, how each was read) |
| 3 | no low-driven missing | no `missing` row's evidence is all `confidence: low`; such gaps are `unknown` |
| 4 | rule citations | every install card cites a placement-rule number from `alignment-rules.md`; every refuse card cites rule 7; a card without a rule is a stub |
| 5 | source kinds | every gap row carries a source kind (`host-self-audit / reference-contrast / domain inference`) |
| 6 | hosts-only tracked | the host-only section exists (even if empty) and reverse gaps are listed there, not dropped |
| 7 | closing statement | report ends with the exact closing sentence from `report-contract.md` |
| 8 | determinism | on **frozen inputs** (fixtures, pinned search-double, no live network) a second pass yields identical gap classes and `lambda` (inventory ordering may differ). A live-network run records `not-checkable`; it may not claim `pass` |
| 9 | neighborhood stratified | Neighborhood section exists (empty on paper/blog). Companion paper is core, not listed as neighborhood. No neighborhood id appears in the core repo gap table. Search-snippet-only neighborhood evidence did not drive `missing`. |
| 10 | host-owned placement | Every install `target` is a host skill/tool/script/extend/runner. None prescribe the reference repo, plugin, hub clone, or MCP as a nested runtime. A host tool that calls a **scientific engine** named by the reference is allowed, and its license is reported. Plumbing items did not appear as `missing`. Refuse cards name no target. |
| 11 | card routing | Each joined product has exactly one card, or an explicit no-card reason. `lambda` matches the slot function in `introduction-card.md`. `ignore` is absent. An `install` card has the five placement fields. A `refuse` card has `placement: null` and names no new skill or tool. An `insufficient-evidence` product has **no** card. |
| 12 | test contract | An `install` card has `fail_before`, `pass_after`, and `destroy`. A `refuse` card has `destroy: n/a` and a `pass_after` that states the host is unchanged. No `confidence: low` span drove an `install`. |
| 13 | slot evidence & fork | Every card slot is `{state, provenance, span, quote}` with `state` one of `1 / 0 / "unknown"`. `state: 1` implies a non-empty verbatim quote; `state: 0` names what was inspected and a valid `why_empty`; `state: "unknown"` has `why_unknown` and an empty quote. Provenance matches the slot (`s`/`v_p` paper, `e`/`v_r` repo, `none` only when the arm does not exist). `kappa: 1` only with both `s` and `e` at `1`. `lambda` recomputed from the states matches the card. `prescribed` / `forbidden_primitives` match the card-label table. The `fork` block is consistent with the two projection tables (`intersection`, `jaccard` recomputed, not hand-written), and is marked `contaminated` when `arms.blind` is false. |
| 14 | verification honesty | The Verification ledger exists and counts every card exactly once. Every card has a `verification` block; beats marked `pass` carry evidence. An `e2e-verified` claim has a build record with date, host commit, commands, and outcomes. No `contract-only` or `failed` card's product is claimed as delivered anywhere in the report. |
| 15 | agent competence | Every `agent-competence` row names a `local_check` with a form (`analytic`/`conservation`/`limit`) and a status (`named`/`demonstrated`), and has **no** card. `named` checks are tallied separately as unrun. No `missing` row carries `host_need: none`. Framework internals (mesh, solver backend, viewer, module tree) do not appear as capabilities. |
| 16 | bridge, not guardrail | Every `install` card names what the agent gets **wrong** without the placement. No card's content is mostly prohibitions. Its `fail_before` is the agent's wrong judgement, not a missing entry point, and its `pass_after` prompt states the user's problem without naming the skill or the entry point. Skill cards carry a positive and a negative routing case; `extend:` cards carry the existing-skill positive case and the must-not-absorb negative case. |
| 17 | unknown handling | No card was produced from a `state: "unknown"` `s` or `e`; such products are `unknown` in the gap table and in Unresolved. No `0` was used for a source that was never inspected. An unreachable paper did not turn into `entry-sans-obligation` or `validity-gap`. |
| 18 | host-need discipline | Every `missing` row has a non-empty `host_need_note`; every `verification` need names the regime, the missing check, and the owning layer; every `agent-competence` row names its local check. No `missing` row has `host_need: none`. |

Layer-1 failures mean the run is **not valid**, not "mostly done".

### Independent re-check

A second pass by a separately invoked context or agent (no access to the first
pass's reasoning, only its frozen artifacts) re-runs the mechanical subset:
schema validation (`references/report-schema.json`), the slot/lambda recompute,
the card-class routing, the `host_need` evidence, and the unknown handling. When
the host cannot isolate a context, record `independent_check: not-available` and
do not present the self-check as verification.

## Layer 2 — install-time acceptance tests (synthetic fixtures)

Purpose: prove the method detects the traps it is designed for, on inputs small
enough to have a hand-computed gold answer. Not benchmark-grade: the fixtures are a
smoke + trap battery, run once per install (or per skill update), adjudicated by a
human/agent against the gold.

### Fixture set (`tests/fixtures/`)

| fixture | what it is | what it traps |
|---|---|---|
| `mini-ref/` | a tiny phonon/vibrational-analysis package (force constants, dynamical matrix, DOS, thermal CLI; docs claim QHA, code has no QHA; CITATION + related + search-double) | dependency-fingerprint families; docs-claim-without-code → `low`; the "adjacent-but-different" trap (see below); companion-paper recovery; neighborhood identity gate; wrapping a scientific-engine CLI is allowed (rule 6 engine case) |
| `mini-ref-unreachable/` | the same shape but the companion paper is claimed and unreachable (no local copy; the search double returns nothing) | the tri-state trap: `s` is `unknown`, not `0`; the row is `insufficient-evidence` with no card, not `entry-sans-obligation`/`refuse` and not `validity-gap`/`install` |
| `mini-host/` | a tiny host surface: two skills (`heat-flow`, `eos`), two tools, plus an audit note admitting a missing heat-capacity capability | host-self-audit source kind; `partial` vs `missing` adjacency (heat-flow ⊄ thermal-properties) |
| `mini-paper.md` | a condensed paper excerpt: explicit method steps, one software dependency (ASE), one reusable dataset, one single-mention term | methods→steps decomposition; hard `tool`/`data` extraction; single-mention → `low` |
| `mini-blog.md` | a how-to post: one named command, one step-by-step recipe, one opinion | recipe→`workflow`, command→`tool`, bare opinion→`concept` `low` |

### Gold answers (`tests/fixtures/gold/…json`)

Each fixture pair has `gold-<ref>-vs-<host>.json` with the expected gap table
(class + source kind per ref capability), the expected card decisions (including
**no card** for `insufficient-evidence`), and expected host-only set. Gold is the
hand-computed answer at the time the fixture was written; it may be amended when a
placement rule legitimately changes — amendments are recorded in the gold file's
`log:` array (what changed, why, when).

### How to run (zero-bundle)

1. Point the skill at the fixture: reference = `tests/fixtures/mini-ref` (or
   `mini-ref-unreachable`), paper/blog files, host = `tests/fixtures/mini-host` —
   or provide the host surface file directly (`inventory_host [surface.json]`).
   Repo runs must execute §E against `neighborhood-search-double.json` (no live
   network).
2. Run the alignment workflow (SKILL.md steps 1–7) normally.
3. Compare the produced gap table to the gold file, entry by entry. Also compare
   companion-paper inventory to `gold/mini-companion-paper.json`, paper-arm gaps
   to `gold/mini-paper-projection-vs-mini-host.json`, neighborhood keep/reject to
   `gold/mini-neighborhood.json`, and introduction cards to
   `gold/mini-introduction-cards.json` (`lambda`, `action`, `placement`, `test`,
   and the absence of cards for `insufficient-evidence`). Worked example:
   `tests/fixtures/runs/2026-10-16-e-neighborhood/` (historical, written under 9
   Layer-1 checks; not current gold).
4. Differences that are **new** (not in the gold `log:`) are failures to be
   adjudicated: either a method regression (fix the skill) or a legitimate rule
   change (amend gold with a `log:` entry).
5. Paper and blog fixtures are single-inventory checks: compare the produced
   capability inventory against `gold-paper.json` / `gold-blog.json`
   (ids, types, confidence).

Pass criteria: zero unlogged mismatches on all fixtures plus the neighborhood /
companion-paper / unreachable-paper / introduction-card golds, and Layer-1 green
on the mini-ref runs (all 18 checks, including unknown handling, host-need
discipline, extend routing, and the bridge-not-guardrail check).

### What this deliberately does NOT do

- No unit-test framework, no CI wiring, no bundled runner — the skill stays
  zero-bundle; the tests run through the skill's own instruction-driven workflow,
  which is exactly what the skill will do in production.
- No benchmark-grade scoring (no rubrics, no pass-rate thresholds over real repos).
- The phonopy ↔ MatDiscovery run stays a reference *instance* in `methodology.md` —
  deliberately **not** a test fixture, so the tests never depend on the one example
  the method is not bound to.
