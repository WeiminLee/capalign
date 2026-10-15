# E2 runtime — harness skeleton + feasibility record

Two parts: (1) the harness skeleton each arm executes through, (2) the actual
feasibility run on the mini fixture (recorded, reproducible). Everything below
marked **executed** has a real output; everything marked **planned** is
protocol, not yet run. No fabricated numbers.

## 1. Harness skeleton

File layout (all under `research/runs/e2/`):

```
e2-scripts/
  arm_select.py       arm selection: top (a) / seeded random (b) / none (c)
  derive_pool.py      pinned report JSON -> gap pool (Phase 2)
  derive_tasks.py     task-suite.csv structural validation (gates the suite)
  run_feasibility.py  mini-fixture pipeline drive (this record)
  judge_task.py       judgment contract: gold | cmd; verdict pass|fail|skip
e2-assets/            snapshots, pinned report copy, gap pool, fixtures, golds
e2-runs/<run-id>/     one self-contained directory per execution
```

How each arm executes (reusing the skill workflow — no custom harness):

| arm | assembly input | selection | staged artifact | judge |
|---|---|---|---|---|
| **a** | the pinned alignment report (SKILL.md workflow output, Layer-1 green) | top-k by the report's stated recommendation order (`arm_select.py --mode top`) | gap-close unit shaped by the host doctrine (CAPABILITY-SURFACE.md: `SKILL.md` frontmatter + body, or script with `--describe`) | blind, gold/cmd/judge |
| **b** | the same gap pool | k without replacement, seeded RNG (`--mode random --seed <recorded>`) | same template quality, same budget | blind, gold/cmd/judge |
| **c** | — | none (`--mode none`) | no artifacts staged | `skip` verdicts |

Execution loop (per arm): for each task in the suite → if the task's ref
capability is in the arm's selection, run the staged artifact in a sandbox cell
with the task's fixture input, judge it; else record `skip`. The judge never
sees the arm label.

Sandbox contract (`judge_task.py`): subprocess, cwd = fresh cell dir, timeout
(default 30 s), captured stdout/stderr; gold mode deep-compares produced files
vs gold (numeric tolerance 1e-6 rel+abs, non-numeric equality); cmd mode checks
exit 0 + pattern; missing runner → `skip`.

## 2. Feasibility run (executed 2026-10-15, run id `feasibility-20261015-185033`)

Scope: the **mini fixture** (`tests/fixtures/mini-ref` reference surface,
fixture gold `mini-ref-vs-mini-host.json`), 3 tasks, zero-bundle stdlib
python3. Purpose: validate the judging pipeline and arm plumbing — **not a
measurement** (the numbers are mechanism checks).

Command:
```bash
cd research/runs/e2 && python3 e2-scripts/run_feasibility.py
```

### 2.1 Recorded output (verbatim, abridged)

```
[1/5] fixtures + golds (zero-bundle)
  gold t-mr-01-band-structure: .../e2-assets/gold/mini/t-mr-01-band-structure.json
  gold t-mr-02-phonon-dos: .../e2-assets/gold/mini/t-mr-02-phonon-dos.json
  gold t-mr-03-thermal-properties: .../e2-assets/gold/mini/t-mr-03-thermal-properties.json
[2/5] gap pool + arm selection
  pool: ['force-constants', 'dynamical-matrix', 'phonon-dos', 'band-structure', 'phonon-thermal-properties']
  arm-a (report-ordered (arm a)): k=2 selected=['force-constants', 'dynamical-matrix']
  arm-b (random (arm b)):         k=2 selected=['phonon-dos', 'dynamical-matrix']
  arm-c (none (arm c)):           k=2 selected=[]
[3/5] stage -> execute -> judge (blind to arm)
  task                             arm-a  arm-b  arm-c  ref-capability
  t-mr-01-band-structure           skip   skip   skip   band-structure
  t-mr-02-phonon-dos               skip   pass   skip   phonon-dos
  t-mr-03-thermal-properties       skip   skip   skip   phonon-thermal-properties
[4/5] judge controls + determinism
  positive control (conforming artifact): pass   PASS
  negative control (zero-point term dropped): fail PASS
  determinism re-run: verdicts identical = True
[5/5] task-suite validation
  suite OK: 32 rows total, 29 real-tier (judge-needed 6/29 = 21%), 3 mini-tier
== aggregate (DEMO numbers; disproportional to the real E2 scale) ==
  arm-a: attempted=0 pass=0 skip=3 effort=0B
  arm-b: attempted=1 pass=1 skip=2 effort=528B
  arm-c: attempted=0 pass=0 skip=3 effort=0B
  delta full-suite arm-a - arm-c = +0.000 (demo only)
  harness contract OK
```

Arm-selection determinism (executed, two consecutive calls):
```
seed 7 random -> ['phonon-dos', 'dynamical-matrix']   (identical on re-run)
seed 9 random -> ['band-structure', 'phonon-dos']
seed 42 top   -> ['force-constants', 'dynamical-matrix']
```

### 2.2 What the feasibility proved

1. **Judging pipeline discriminates.** Positive control (conforming artifact)
   → `pass`; negative control (same artifact with the zero-point term removed,
   a real physical bug) → `fail` with a gold diff reason
   (`$.free_energies[0]: -0.836 vs 1.286 out of tol`); arm-c cells → `skip`.
   The gold is deliberately *not* a re-implementation (S/Cv from central
   finite differences of F vs the artifact's analytic formulas) — the pipeline
   would catch an analytic-formula bug.
2. **Determinism.** Same inputs re-run → identical verdicts & reasons.
3. **Arm plumbing.** pool → `arm_select` (top/random/none) → staging (host-doctrine
   shaped, effort metered in bytes) → sandbox judge → aggregate.
4. **Suite contract gate.** `derive_tasks.py` passes (≥20 real rows, all doc
   paths exist under `phonopy/doc`, judge share 21% < 30%).
5. **Cmd-mode judging path** (executed separately): a conforming artifact
   matching `^OK ` → `pass`; a non-conforming one (missing the `OK` prefix)
   → `fail`. Both `gold` and `cmd` verdict paths are now exercised.

### 2.3 Design findings recorded (fed into the protocol)

- **Arm selection × suite coverage is a real confounder.** In the demo,
  report-ordered top-k (`force-constants`, `dynamical-matrix`) staged artifacts
  that covered 0 of the 3 suite cells, while the seeded random arm covered 1.
  E2 therefore reports BOTH `success-on-attempted` and full-suite success, and
  requires the suite to span the whole reference surface (protocol §5; the
  mini pool is uniformly host-self-audit since the fixture gold's F2
  amendment, so the demo's "priority" collapses to documented order — another
  reason it is a mechanism check, not a comparison).
- **Naming discipline.** Task `ref_capability` must use the reference surface's
  capability ids (`phonon-thermal-properties`, not `thermal-properties`) so the
  join between pool and suite is total. A runtime assertion now fails the demo
  if a task references a capability outside the pool.
- **Verdict vocabulary.** `skip` is a real state (no artifact), not an error;
  the judge defaults to `skip` only when the runner is absent (previous bug:
  it leaked into gold-mismatch cases — fixed so a mismatch always yields `fail`).

### 2.4 Dev-time fixes (recorded for traceability)

| bug | fix | checked |
|---|---|---|
| gold file path double extension (`t.*.json` + `.json`) | registry stores basename without extension | re-run green |
| gold-mode mismatch left verdict at `skip` | verdict forced to `fail` on mismatch | negative control |
| `task-suite.csv` unquoted comma fields → ragged rows | regenerated via `csv` writer | validator |
| pool/suite id mismatch (`thermal-properties` vs `phonon-thermal-properties`) | `ref_capability` = reference surface ids + runtime assertion | re-run green |

## 3. Full E2 run — not yet run (blocks, in order)

1. **Pinned real report**: the phonopy↔MatDiscovery record (methodology §3,
   19 gaps) is referenced but its file location is not yet copied into
   `e2-assets/report/`; until then arm-(a) has no authority. (The mini report
   is the fixture gold, used only for plumbing.)
2. **Assembler with agency**: arm (a)/(b) artifacts in the full run are
   produced by an agent reading the report (skills workflow); that requires an
   agent run + trace, not available in this zero-bundle feasibility.
3. **Real-tier golds**: `r-*` gold files marked `k8: pending` need a reference
   executable install (or documented-equation golds, logged).
4. **Coverage-parity strategy** (protocol §5) tuned on the real pool before
   budgets are fixed.

Status summary: pipeline verified on mini fixtures; **full experiment not run
— protocol ready**.

## 4. Re-run instructions

```bash
# full pipeline smoke (3 mini tasks, ~1 s, stdlib only)
cd research/runs/e2
python3 e2-scripts/run_feasibility.py
# suite gate
python3 e2-scripts/derive_tasks.py task-suite.csv --ref-doc-root /Users/lwm/code/phonopy/doc
# arm selection alone
python3 e2-scripts/arm_select.py --pool e2-assets/gap-pool-mini.json --k 2 --seed 7 --mode random
# pool from a report JSON (real run input)
python3 e2-scripts/derive_pool.py --report e2-assets/report/capability-alignment.json --out e2-assets/gap-pool.json
```