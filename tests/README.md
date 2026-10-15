# capalign acceptance tests

Synthetic fixtures + gold answers. Not benchmark-grade — a smoke + trap battery that
proves the aligner detects what it is designed to detect. No test framework, no
runner: the tests run **through the skill's own workflow**, exactly as in production
(this is the zero-bundle contract). Layer-1 self-check rules live in
`references/evaluation.md`.

## Fixtures

| fixture | traps asserted |
|---|---|
| `mini-ref/` (phonon toolkit) | doc-claim-without-code → `unknown` not `missing`; adjacent thermal capability (host `heat-flow`) → `partial` with host link; host self-audit source kind |
| `mini-host/` (2 skills + registry + AUDIT.md) | provenance scanning; `host self-audit` tagging |
| `mini-paper.md` | single-mention → `low`; hard software deps → `tool`; published data → `data` |
| `mini-blog.md` | named command → `tool`; recipe → `workflow` medium; bare opinion → `concept` low |

## How to run (host agent, instruction-driven)

```
1. inventory_repo:    reference = tests/fixtures/mini-ref, host = tests/fixtures/mini-host
2. inventory_paper:   reference = tests/fixtures/mini-paper.md (host surface may be omitted; single-inventory)
3. inventory_blog:    reference = tests/fixtures/mini-blog.md
4. align mini-ref vs mini-host
5. compare outputs to gold/*.json, entry by entry
```

Compare rules: `class` and `source_kind` must match gold exactly; `host_id` where
gold names one; the `traps_asserted` list must all hold. A mismatch is either a
method regression (fix the skill) or a deliberate rule change — the latter requires
a `log:` entry in the gold file (what changed, why, when).

Pass = zero unlogged mismatches on all four fixtures, and Layor-1 self-check green
on the mini-ref run.

## When to run

- after installing the skill into a new host (one-time acceptance);
- after any change to SKILL.md / references (regression check);
- before declaring an alignment result trustworthy.