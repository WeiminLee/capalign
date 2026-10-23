# cap-align acceptance tests

Synthetic fixtures + gold answers. Not benchmark-grade — a smoke + trap battery that
proves the aligner detects what it is designed to detect. No test framework, no
runner: the tests run **through the skill's own workflow**, exactly as in production
(this is the zero-bundle contract). Layer-1 self-check rules live in
`references/evaluation.md`; the JSON contract is `references/report-schema.json`.

## Fixtures

| fixture | traps asserted |
|---|---|
| `mini-ref/` (phonon toolkit) | doc-claim-without-code → repo-arm `unknown` not `missing`; adjacent thermal capability (host `heat-flow`) → repo-arm `missing` with a host note, not `partial`; that repo entry's introduction card is `refuse`; host-self-audit source kind; CITATION companion paper is core; neighborhood identity gate |
| `mini-ref-unreachable/` (paper claimed, not retrievable) | the tri-state trap: `s = unknown` is not `0`; the product is `insufficient-evidence` with **no card**, not `entry-sans-obligation`/`refuse` and not `validity-gap`/`install`; Unresolved records `why_unknown: unreachable` |
| `mini-host/` (2 skills + registry + AUDIT.md) | provenance scanning; `host-self-audit` tagging |
| `mini-paper.md` | single-mention → `low`; hard software deps → `tool`; published data → `data` |
| `mini-blog.md` | named command → `tool`; recipe → `workflow` medium; bare opinion → `concept` low |
| `mini-library/` | all nine fusion relations; duplicate vs variant vs hard-conflict; same procedure/different regime → `partial`; description overlap is not duplication; merge preserves both test contracts and carries the fail-closed evidence block (witness ladder, hard surface coverage, locked residual, recall gate, interaction gate, never-inflate); two individually safe cards jointly shadow `heat-flow` |
| `mini-retire/` | upgrade superset; retire an unreachable entry is allowed; retiring the live last deliverer of `lattice-kappa` is rejected |
| `runs/2026-10-16-e-neighborhood/` | **historical** worked example (written under 9 Layer-1 checks, pre-`arms` / pre-tri-state); not current gold. `runs/judge-1/` is an older pilot, also not gold. |

## How to run (host agent, instruction-driven)

```
1. inventory_repo:    reference = tests/fixtures/mini-ref, host = tests/fixtures/mini-host
   (includes recover_reference §E; use neighborhood-search-double.json, no live network)
1b. unreachable:      reference = tests/fixtures/mini-ref-unreachable, host = tests/fixtures/mini-host
   (no local paper; the double returns nothing — expect no cards)
2. inventory_paper:   reference = tests/fixtures/mini-paper.md (host surface may be omitted; single-inventory)
3. inventory_blog:    reference = tests/fixtures/mini-blog.md
4. align mini-ref vs mini-host
5. compare outputs to gold/*.json, entry by entry
   — repo-arm gaps: gold/mini-ref-vs-mini-host.json
   — unreachable-paper gaps/cards: gold/mini-unreachable-vs-mini-host.json
   — companion paper inventory: gold/mini-companion-paper.json
   — paper-arm gaps: gold/mini-paper-projection-vs-mini-host.json
   — neighborhood keep/reject: gold/mini-neighborhood.json
   — introduction cards: gold/mini-introduction-cards.json
   — portfolio plans: mini-library/gold/portfolio-plan.json, mini-retire/gold/portfolio-plan.json
   worked example (historical): tests/fixtures/runs/2026-10-16-e-neighborhood/
```

Portfolio tool (research check, not a bundled skill runner):

```bash
python3 research/tools/portfolio-model.py tests/fixtures/mini-library/portfolio-input.json --json
python3 research/tools/portfolio-model.py tests/fixtures/mini-library/portfolio-input-gated.json --json
python3 research/tools/portfolio-model.py tests/fixtures/mini-retire/portfolio-input.json --json
```

Expected: the add-all input exits 1 with the joint-shadow violation; the gated
input exits 0; the retire input exits 1 with the bad-retire violation while the
good lifecycle actions pass.

Compare rules: `class` and `source_kind` must match gold exactly; `host_id` where
gold names one; the `traps_asserted` list must all hold; slot `state`/`provenance`
must match. A mismatch is either a method regression (fix the skill) or a deliberate
rule change — the latter requires a `log:` entry in the gold file (what changed, why,
when).

Pass = zero unlogged mismatches on all fixtures plus the neighborhood /
companion-paper / unreachable-paper / introduction-card / portfolio-plan golds,
zero violations on the gold-valid portfolio plans, the named violations on the
bad plans, and Layer-1 self-check green on the mini-ref runs (**21 checks**,
including unknown handling, host-need discipline, extend routing, slot evidence &
fork, and the three portfolio checks).

## When to run

- after installing the skill into a new host (one-time acceptance);
- after any change to SKILL.md / references (regression check);
- before declaring an alignment result trustworthy.
