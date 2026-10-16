# Evaluation — is the alignment valid, and how do we check it?

Two layers. Layer 1 runs on **every run** (a validity gate on the report). Layer 2
is an install-time acceptance test against synthetic fixtures — not benchmark-grade,
but deterministic enough that "the skill works" is checkable by any host.

## Layer 1 — per-run self-check (mandatory, before the report is final)

Before `capability-alignment-report.md` is considered final, run these checks on it.
Any failure is reported in the report's own header (`self_check:` block), never
silently fixed.

| # | check | assertion |
|---|---|---|
| 1 | sections | report contains all required sections (see `report-contract.md`): surfaces, reference inventory, host inventory, gap table, recommendations, host-only, neighborhood, unresolved |
| 2 | validated evidence | every `missing` row has ≥1 high/medium evidence entry that came from **validation** (cross-validation step), not the raw comparison — assert by the evidence pointers pointing at host/reference artifacts (paths/quotes), not at "comparison" |
| 3 | no low-driven missing | no `missing` row's evidence is all `confidence: low`; such gaps are `unknown` |
| 4 | rule citations | every recommendation cites a placement-rule number from `alignment-rules.md`; a recommendation without a rule is a stub |
| 5 | source kinds | every gap row carries a source kind (`host self-audit / reference-contrast / domain inference`) |
| 6 | hosts-only tracked | the host-only section exists (even if empty) and reverse gaps are listed there, not dropped |
| 7 | closing statement | report ends with the exact closing sentence from `report-contract.md` |
| 8 | determinism | re-run the alignment on the same inputs once; gap table must come out identical (inventory ordering may differ, classification may not) |
| 9 | neighborhood stratified | Neighborhood section exists (empty on paper/blog). Companion paper is core, not listed as neighborhood. No neighborhood id appears in the core repo gap table. Search-snippet-only neighborhood evidence did not drive `missing`. |
| 10 | host-owned placement | Every recommendation is a host skill/tool/script/extend/skip. None prescribe the reference repo, plugin, hub clone, or MCP as a nested runtime. A host tool that calls a **scientific engine** named by the reference is allowed. Plumbing items did not appear as `missing`. |

Layer-1 failures mean the run is **not valid**, not "mostly done".

## Layer 2 — install-time acceptance tests (synthetic fixtures)

Purpose: prove the method detects the traps it is designed for, on inputs small
enough to have a hand-computed gold answer. Not benchmark-grade: the fixtures are a
smoke + trap battery, run once per install (or per skill update), adjudicated by a
human/agent against the gold.

### Fixture set (`tests/fixtures/`)
| fixture | what it is | what it traps |
|---|---|---|
| `mini-ref/` | a tiny phonon/vibrational-analysis package (force constants, dynamical matrix, DOS, thermal CLI; docs claim QHA, code has no QHA; CITATION + related + search-double) | dependency-fingerprint families; docs-claim-without-code → `low`; the "adjacent-but-different" trap (see below); companion-paper recovery; neighborhood identity gate; wrapping a scientific-engine CLI is allowed (rule 6 engine case) |
| `mini-host/` | a tiny host surface: two skills (`heat-flow`, `eos`), two tools, plus an audit note admitting a missing heat-capacity capability | host self-audit source kind; `partial` vs `missing` adjacency (heat-flow ⊄ thermal-properties) |
| `mini-paper.md` | a condensed paper excerpt: explicit method steps, one software dependency (ASE), one reusable dataset, one single-mention term | methods→steps decomposition; hard `tool`/`data` extraction; single-mention → `low` |
| `mini-blog.md` | a how-to post: one named command, one step-by-step recipe, one opinion | recipe→`workflow`, command→`tool`, bare opinion→`concept` `low` |

### Gold answers (`tests/fixtures/gold/…json`)
Each fixture pair has `gold-<ref>-vs-<host>.json` with the expected gap table
(class + source kind per ref capability) and expected host-only set. Gold is the
hand-computed answer at the time the fixture was written; it may be amended when a
placement rule legitimately changes — amendments are recorded in the gold file's
`log:` array (what changed, why, when).

### How to run (zero-bundle)
1. Point the skill at the fixture: reference = `tests/fixtures/mini-ref` (and the
   paper/blog files), host = `tests/fixtures/mini-host` — or provide the host
   surface file directly (`inventory_host [surface.json]`). Repo runs must execute
   §E against `neighborhood-search-double.json` (no live network).
2. Run the alignment workflow (SKILL.md steps 1–7) normally.
3. Compare the produced gap table to the gold file, entry by entry. Also compare
   companion-paper inventory to `gold/mini-companion-paper.json`, paper-arm gaps
   to `gold/mini-paper-projection-vs-mini-host.json`, and neighborhood
   keep/reject to `gold/mini-neighborhood.json`. Worked example:
   `tests/fixtures/runs/2026-10-16-e-neighborhood/`.
4. Differences that are **new** (not in the gold `log:`) are failures to be
   adjudicated: either a method regression (fix the skill) or a legitimate rule
   change (amend gold with a `log:` entry).
5. Paper and blog fixtures are single-inventory checks: compare the produced
   capability inventory against `gold-paper.json` / `gold-blog.json`
   (ids, types, confidence).

Pass criteria: zero unlogged mismatches on all four fixtures **plus**
`gold/mini-neighborhood.json` and `gold/mini-companion-paper.json`; Layer-1
self-check green on the mini-ref run (10 checks, including neighborhood
stratified and host-owned placement).

### What this deliberately does NOT do
- No unit-test framework, no CI wiring, no bundled runner — the skill stays
  zero-bundle; the tests run through the skill's own instruction-driven workflow,
  which is exactly what the skill will do in production.
- No benchmark-grade scoring (no rubrics, no pass-rate thresholds over real repos).
- The phonopy ↔ MatDiscovery run stays a reference *instance* in `methodology.md` —
  deliberately **not** a test fixture, so the tests never depend on the one example
  the method is not bound to.