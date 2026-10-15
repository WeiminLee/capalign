# E1 pilot — inter-rater agreement record (mini-ref vs mini-host)

Date: 2026-10-15. Raters: judge-1 (self-run of skill workflow), judge-2
(isolated independent agent). Gold: `tests/fixtures/gold/mini-ref-vs-mini-host.json`.

## Agreement (6 shared ref capabilities)

| ref capability | judge-1 class/source | judge-2 class/source | gold | agree? |
|---|---|---|---|---|
| force-constants | missing / reference-contrast | missing / **host-self-audit** | missing / reference-contrast | class ✓ · source ✗ |
| dynamical-matrix | missing / reference-contrast | missing / **host-self-audit** | missing / reference-contrast | class ✓ · source ✗ |
| phonon-dos | missing / reference-contrast | missing / **host-self-audit** | missing / reference-contrast | class ✓ · source ✗ |
| band-structure | missing / reference-contrast | missing / **host-self-audit** | missing / reference-contrast | class ✓ · source ✗ |
| phonon-thermal-properties | partial / host-self-audit | **missing** / host-self-audit | **partial** / host-self-audit | **class ✗** · source ✓ |
| qha | unknown / reference-contrast | unknown / reference-contrast | unknown / reference-contrast | ✓ |

Class agreement: 5/6 (0.833) · Source agreement: 2/6 (0.333)

## Findings (design defects surfaced)

### F1 — `partial` semantics contradicted the formal definition
`formal-foundations.md` §2 defines partial as *strict semantic subset* (subsume,
Paolucci-style): host covers a strict subset. Under that definition, `heat-flow`
(BTE lattice kappa) does **not** subsume `phonon-thermal-properties` (Cv/F/S/ZPE) —
they are adjacent, not subset — so the correct class is **missing** (with the
adjacent host capability recorded in a note), not partial. Judge-1 and the gold
wrongly classified it partial under an "adjacent counts as partial" intuition;
judge-2 followed the strict definition.
Action: `alignment-rules.md` §partial clarified to strict-subsume semantics; fixture
gold amended with a `log:` entry.

### F2 — host self-audit mapping was not enforced
judge-1 marked 4 AUDIT-admitted gaps as `reference-contrast` and missed that
AUDIT.md:5-9 explicitly admits them — so the source kind should have been
`host-self-audit` (higher priority). judge-2 got this right. The mapping step
("scan host AUDIT/roadmap text; a gap the host itself admits has source kind
host-self-audit") must be an explicit inventory step, not an afterthought.
Action: `inventory-heuristics.md` §D gains an explicit AUDIT-scan rule; source-kind
selection is driven by it.

### F3 (open, recorded not resolved) — inventory granularity boundary
judge-2 additionally inventoried two meta-level items judge-1 did not: the CLI entry
point (interface) and the dependency fingerprint (data). Per `capability-ir.md`
(semantic units, dependency fingerprint = derivation clue not a standalone
capability), these are boundary cases; recorded for the broader IRR corpus, not
resolved here.

## Running notes
- judge-1 shares authorship with the gold, so "judge-1 vs gold 6/6" carries no
  independence weight; judge-2 is the independent signal.
- F1/F2 each caused exactly one disagreeing judgment; both are now codified, so the
  pilot already bought a rules fix. The κ-rated IRR corpus (E1 formal) proceeds with
  the corrected rules.