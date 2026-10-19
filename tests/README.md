# cap-align acceptance tests

Synthetic fixtures + gold answers. Not benchmark-grade — a smoke + trap battery that
proves the aligner detects what it is designed to detect. No test framework, no
runner: the tests run **through the skill's own workflow**, exactly as in production
(this is the zero-bundle contract). Layer-1 self-check rules live in
`references/evaluation.md`.

## Fixtures

| fixture | traps asserted |
|---|---|
| `mini-ref/` (phonon toolkit) | doc-claim-without-code → repo-arm `unknown` not `missing`; adjacent thermal capability (host `heat-flow`) → repo-arm `missing` with a host note, not `partial`; that repo entry's introduction card is `refuse`; host self-audit source kind; CITATION companion paper is core; neighborhood identity gate |
| `mini-host/` (2 skills + registry + AUDIT.md) | provenance scanning; `host self-audit` tagging |
| `mini-paper.md` | single-mention → `low`; hard software deps → `tool`; published data → `data` |
| `mini-blog.md` | named command → `tool`; recipe → `workflow` medium; bare opinion → `concept` low |
| `runs/2026-10-16-e-neighborhood/` | worked example of a valid post-§E report (two projections, neighborhood stratified). Written under 9 Layer-1 checks; current Layer-1 is 10 (adds host-owned placement). `runs/judge-1/` is a historical E1 pilot and is not the current gold. |

## How to run (host agent, instruction-driven)

```
1. inventory_repo:    reference = tests/fixtures/mini-ref, host = tests/fixtures/mini-host
   (includes recover_reference §E; use neighborhood-search-double.json, no live network)
2. inventory_paper:   reference = tests/fixtures/mini-paper.md (host surface may be omitted; single-inventory)
3. inventory_blog:    reference = tests/fixtures/mini-blog.md
4. align mini-ref vs mini-host
5. compare outputs to gold/*.json, entry by entry
   — repo-arm gaps: gold/mini-ref-vs-mini-host.json
   — companion paper inventory: gold/mini-companion-paper.json
   — paper-arm gaps: gold/mini-paper-projection-vs-mini-host.json
   — neighborhood keep/reject: gold/mini-neighborhood.json
   — introduction cards: gold/mini-introduction-cards.json
   worked example: tests/fixtures/runs/2026-10-16-e-neighborhood/
```

Compare rules: `class` and `source_kind` must match gold exactly; `host_id` where
gold names one; the `traps_asserted` list must all hold. A mismatch is either a
method regression (fix the skill) or a deliberate rule change — the latter requires
a `log:` entry in the gold file (what changed, why, when).

Pass = zero unlogged mismatches on all four fixtures plus the neighborhood /
companion-paper golds and `gold/mini-introduction-cards.json`, and Layer-1
self-check green on the mini-ref run (14 checks, including neighborhood
stratified, host-owned placement, card routing, test contract, and slot
evidence & fork).
Projection `class` values stay on their own gold files.

## When to run

- after installing the skill into a new host (one-time acceptance);
- after any change to SKILL.md / references (regression check);
- before declaring an alignment result trustworthy.