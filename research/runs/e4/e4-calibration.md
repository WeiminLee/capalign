# E4 calibration — first curve sketch (mini, non-conclusive)

`cal` definition (formal-foundations §5): `cal(l) = P(conf-label = verified |
label = l)` for `l ∈ {high, medium, low}`. These are the label cells measured so
far. **Mini-scale: one populated cell, n=4. This is a curve skeleton, not a
curve.**

## Measured points (run E4-MINI-*, 2026-10-15)

| conf label | host claims (n) | verified (t1) | pass rate | verified (t2) |
|---|---|---|---|---|
| high | 4 | 3 | **0.75** | 0 (0.00, tier saturates) |
| medium | 0 | — | — | — |
| low | 0 | — | — | — |

The single unverified `high` claim: **heat-flow — "produces kappa(T)"**. Its
carrier exists (SKILL.md frontmatter = routing trigger), which is why extractor
confidence is `high`; but its input contract (phonon frequencies from an upstream
capability) has **no producer anywhere on the host** (AUDIT.md + grep confirm no
force-constant / dynamical-matrix / DOS pathway). Extractor confidence measures
*existence of a claim artifact*; verification measures *satisfiable promise* —
exactly the gap E4 exists to measure, visible even here.

Reference-side side-observation (not the cal operator — `cal` is host-side): the
one `low` confidence *reference* item (qha, doc-only claim) fails code
confirmation 1/1, while the 4 `high` reference items are all code-confirmed.
Consistent shape, but it belongs to the reference-inventory calibration, not the
host self-report calibration — kept apart so the definitions stay exact.

## What the sketch does NOT show (degeneracies, stated)

- **Monotonicity unassessable**: no medium/low host claims exist on mini-host; a
  monotone `cal` (high ≥ medium ≥ low pass-rates) needs all three cells on a real
  surface. Mini verdict: "cannot confirm or refute monotonicity".
- **t2 cell is degenerate**: no executables on the host → 0/4 verified at the
  strict witness-test tier → drift saturates at 1.0 and cal at 0.0. Reported
  because the paper must pick a tier and say so.
- **Bias direction**: measured `bias = 0.0` — the fixture cannot produce
  self-vs-external over-claim because both passes read the same artifact tree and
  AUDIT.md pre-admits every gap (clean-by-design). Direction "self ≥ external" is
  **predicted** by assertion D, **not measured** on the mini pair.

## Path to a real curve (next runs)

Per protocol §8, the curve needs, per conf label cell, `n ≥ 5` claims and ≥ 2
claim sources:

- **MatDiscovery (37 skills).** Host claims: backticked tool/artifact mentions in
  SKILL.md description + body (drift-meter extraction semantics, now at capability
  granularity). External surface: code-scraped registry (71 tools + 99 artifacts,
  `build-registry.py`) + human-checked subset. This corpus already yields claim
  sources (`repo-docs`/scenario claims; SKILLS-AUDIT admissions as negative
  reports) → three-label cells are plausible. **Predicted shape to test:**
  `cal(high) ≥ cal(medium) ≥ cal(low)`; if pass rates invert or scatter without
  structure, the external-audit-only boundary (§7.3) applies and gets written into
  the paper.
- **K-Dense scientific-agent-skills.** The "no AUDIT.md" case — the host's only
  self-signal is its own skill text; external = repo file tree + docs resolution.
  This is the corpus most likely to show `bias > 0` (self-promotion with nothing
  honest to lean on).

## Reporting contract for each real-run cell

`cal(l)` row = {n claims, k verified, pass rate, tier, list of `unverified` rows
with fail reasons} — the `unverified` rows are the deliverable (what self-reported
evidence failed validation, and why), not just the aggregate.