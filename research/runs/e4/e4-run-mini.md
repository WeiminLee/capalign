# E4 feasibility run — mini fixtures, two passes (measured)

Run date: 2026-10-15. Host agent: cap-align host (this agent), running the skill
workflow itself. **Mini-scale, non-conclusive** — a feasibility signal, not a
verdict (see protocol §7.4).

## Inputs (frozen)

| input | value |
|---|---|
| reference | `tests/fixtures/mini-ref` (repo, phonon toolkit) |
| host | `tests/fixtures/mini-host` (2 skills + tool registry + AUDIT.md) |
| gold (pass-2 surface source) | `tests/fixtures/gold/mini-ref-vs-mini-host.json` |
| freeze hash (sha256, 10 files: 9 fixtures + gold) | `22cc4d6b848817d85e7ef5170fb2b9da6828909f68385bc9cfd652cb272aa917` |
| run IDs | `E4-MINI-R1-SELF-2026-10-15`, `E4-MINI-R2-GOLD-2026-10-15` |

Frozen reference IR (built once by `inventory_repo`, identical in both passes —
also matches the gold's ref ids):

| id | type | conf | evidence |
|---|---|---|---|
| force-constants | compute | high | `src/mini_ref/cli.py` (`force_constants`) |
| dynamical-matrix | compute | high | `src/mini_ref/cli.py` (`dynamical_matrix`) |
| phonon-dos | compute | high | `src/mini_ref/cli.py` (`dos`) + `docs/band.md` |
| band-structure | workflow | medium | `docs/band.md` (`phon-vib band`) + CLI |
| phonon-thermal-properties | compute | high | `src/mini_ref/cli.py` (`thermal_properties`) |
| qha | workflow | low | `docs/qha.md` only — `qha` module absent from source |

## Pass 1 — self-referential (real commands run)

The host audits itself: `inventory_host §D` over its own tree

```bash
$ find tests/fixtures/mini-host -name "SKILL.md"
tests/fixtures/mini-host/skills/heat-flow/SKILL.md
tests/fixtures/mini-host/skills/eos/SKILL.md

$ cat tests/fixtures/mini-host/tools/tool-registry.json
{"tools": [{"name": "parse-structure", ...}, {"name": "fit-eos", ...}]}

$ cat tests/fixtures/mini-host/AUDIT.md
# mini-host self-audit notes
Known gaps ... (admitted here, not yet built):
- No harmonic heat capacity / specific heat (Cv) or phonon thermal properties
  (free energy F, entropy S, zero-point energy) ...
- No phonon DOS or dispersion.
- No force-constant / dynamical-matrix pathway for any structure.
Open (not gaps, boundaries): lattice thermal conductivity is covered by the
`heat-flow` skill (BTE); equations of state by the `eos` skill.
```

Self-report produced by the scan (positive claims, `conf=high`, direct artifacts):

| claim | carrier | provenance |
|---|---|---|
| heat-flow — lattice thermal conductivity kappa via phonon BTE | `skills/heat-flow/SKILL.md` | skill dir |
| eos — 3rd-order Birch-Murnaghan EOS fit (V0, B0) | `skills/eos/SKILL.md` | skill dir |
| parse-structure — parse POSCAR into structure dict | `tools/tool-registry.json` | tool registry |
| fit-eos — fit 3rd-order BM EOS to E(V) points | `tools/tool-registry.json` | tool registry |

Negative reports (self-admitted absences): phonon-thermal-properties, phonon-dos,
band-structure/dispersion, force-constants, dynamical-matrix.

**Cross-validation** (real `grep -rli` over the host tree):

```
force_const  -> NONE              dynamical -> AUDIT.md only (admission)
dos          -> AUDIT.md only     band      -> NONE
qha          -> NONE              thermal   -> AUDIT.md, skills/heat-flow/SKILL.md
Cv / heat capacity / zero-point / entropy -> AUDIT.md only
kappa        -> skills/heat-flow/SKILL.md
```

Reference-side check: `ls tests/fixtures/mini-ref/src/mini_ref/` → `__init__.py
cli.py` only — the `qha` module claimed by `docs/qha.md` does **not** exist
(low-confidence trap; qha must stay `unknown`).

Pass-1 gap table (strict subsume, codified §D.3 source rules; verbatim in
`fixture-inputs/run1-self-gaps.json`):

| ref_id | class | source_kind | host_id | note |
|---|---|---|---|---|
| force-constants | missing | host-self-audit | — | grep NONE; AUDIT admits no pathway |
| dynamical-matrix | missing | host-self-audit | — | AUDIT admits |
| phonon-dos | missing | host-self-audit | — | AUDIT admits |
| band-structure | missing | host-self-audit | — | AUDIT admits no dispersion |
| phonon-thermal-properties | missing | host-self-audit | heat-flow | heat-flow = BTE lattice kappa, adjacent ≠ subset (strict subsume) |
| qha | unknown | reference-contrast | — | doc-only claim, no code; low evidence must not drive missing |

host-only: `parse-structure, fit-eos, eos`. Layer-1 self-check: 8/8 pass
(determinism re-run reproduced an identical table).

## Pass 2 — gold-fed (real run)

Same frozen reference IR; host surface **supplied** from the gold JSON
(host_only `[parse-structure, fit-eos, eos]`, `host_id` near-miss on
phonon-thermal-properties, externally-verified source kinds). The pass-2 gap table
is the gold table by construction (the gold IS the externally-verified answer):

| ref_id | class | source_kind | host_id |
|---|---|---|---|
| force-constants | missing | reference-contrast | — |
| dynamical-matrix | missing | reference-contrast | — |
| phonon-dos | missing | reference-contrast | — |
| band-structure | missing | reference-contrast | — |
| phonon-thermal-properties | missing | host-self-audit | heat-flow |
| qha | unknown | reference-contrast | — |

Layer-1 self-check: 8/8 pass (determinism re-run identical).

## Verification ledger (both passes share the frozen artifact tree)

| claim | conf | t1 verified | t2 verified | fail reason |
|---|---|---|---|---|
| heat-flow — kappa promise | high | ✗ | ✗ | input contract unsatisfiable: needs phonon frequencies; no host capability produces them (grep/AUDIT) |
| eos — EOS fit | high | ✓ | ✗ | — |
| parse-structure | high | ✓ | ✗ | — |
| fit-eos | high | ✓ | ✗ | — |

Negative reports verified by grep: 5/5 accurate (every admitted absence is truly
absent).

## Results (computed by `e4_calib.py`, stdlib — re-run with)

```bash
python3 e4_calib.py --self fixture-inputs/run1-self-gaps.json \
                    --gold fixture-inputs/run2-gold-gaps.json \
                    --ledger fixture-inputs/verify-ledger.json --out fixture-inputs/metrics.json
```

| quantity | value | label |
|---|---|---|
| drift (t1) self / gold | 0.25 / 0.25 (1 of 4 claims unverified) | measured, mini |
| drift (t2) self / gold | 1.00 / 1.00 (no executable carrier on mini-host) | measured, mini, saturated tier |
| **bias (both tiers)** | **0.00** | measured, mini |
| **cal(t1, high)** | **0.75** (3/4) | measured, mini |
| cal(t2, high) | 0.00 (0/4) | measured, mini, saturated |
| confirmation: conf=low ref item | qha — code absent (reference-side side-observation, not the cal operator) | measured, mini |
| gap agreement — class | 6/6 = 1.00 | measured, mini |
| gap agreement — source_kind | 2/6 = 0.33 | measured, mini |
| gap agreement — host_id | 6/6 = 1.00 | measured, mini |
| negative-report accuracy | 5/5 = 1.00 | measured, mini |
| self-reported evidence entries failing validation | 1 (heat-flow → kappa) | measured, mini |

## Reading (honest, mini-scale)

1. **bias = 0.0 on the fixture — the fixture cannot produce self-bias.** Both
   passes observe the same 4-claim artifact tree, and `AUDIT.md` seeds the honest
   answer (the host already admits every gap). Drift cancels in the difference.
   The only positive claim that fails verification (heat-flow's kappa promise,
   unsatisfiable input dependency) is present in *both* passes, so it cannot move
   bias. The mini corpus is too clean by design: **assertion D's `bias ≥ 0` is
   untestable here**; the protocol's real target is a library with no audit file
   (§8 of the protocol — MatDiscovery 37 skills or K-Dense).
2. **Source-kind agreement 0.33 is the one real, repeatable signal.** Pass 1
   follows the codified §D.3 rule (AUDIT-admitted → host-self-audit) and tags 5
   rows host-self-audit; the gold tags 4 of them reference-contrast. This is the
   known open residue from e1-pilot F2 (judge-2 vs gold), deliberately **not**
   re-adjudicated here (gold + rules are frozen; only `research/runs/e4/` may be
   written). Consequence: on the mini pair, source-kind agreement is confounded by
   a gold-vs-rule residue — must be resolved before the real-library run (gold
   amendment with `log:` entry, or the §D.3 rule text tightened).
3. **Calibration has one populated cell** (`high`, n=4, 0.75). No medium/low
   claims exist on mini-host, so the curve and its monotonicity are unassessable —
   degenerate, not a finding.
4. **Tier discipline matters**: t2 saturates (drift 1.0, cal 0.0) because
   mini-host has no executables. Reported, not hidden — the paper must state which
   tier its headline number uses.
5. Mechanism check: two passes → agreed + disagreed tables, ledger, bias/cal
   bookkeeping, deterministic re-runs — all reproducible with two commands. The
   machinery works; it needs a real library to have something to measure.

## Assets (this directory)

- `e4-protocol.md` — the reproducible protocol (this run instantiates it)
- `e4-calibration.md` — calibration-curve sketch
- `e4_calib.py` — stdlib-only bookkeeper
- `fixture-inputs/run1-self-gaps.json`, `run2-gold-gaps.json`,
  `verify-ledger.json`, `metrics.json` — measured run artifacts