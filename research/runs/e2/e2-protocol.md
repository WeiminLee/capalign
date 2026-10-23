# E2 — before/after: does report-driven assembly beat the baselines?

Status: **protocol v0.1 (executable skeleton) — harness feasibility ran on the
mini fixture; the full experiment is not yet run.** Instance parameters below
are the first (materials) instance; the phases are host/reference-agnostic so a
neutral-domain instance swaps only the parameter table.

- Assertion under test: **B** (`formal-foundations.md` §3) — coverage@reference
  predicts task success on a suite derived from the reference; gains plateau at
  `coverage* < 1`. E2 operationalizes "acting on the alignment report" and
  compares it against two baselines.
- Experiment spec: `research/experiments.md` §E2 (three arms, effort equalized,
  success + gain-per-effort, SoK +16.2pp anchor).
- Method: `SKILL.md` workflow (steps 1–9; this protocol was written when it was 1–7) — the experiment is a **first-class
  user of the artifact**, not a custom harness.

---

## 1. Instance parameters

| parameter | value (this instance) | generic role |
|---|---|---|
| host library | `MatDiscovery` (`/Users/lwm/code/MatDiscovery`, **read-only**) — 37 skills in `plugins/matdiscovery/skills/`, 13 `local_compute` tools, 3 remote submit tools, doctrine in `docs/CAPABILITY-SURFACE.md` | the surface being assembled |
| host commit pin | `ce3574fbd40f2c5ca0b90c2226a65257410e54b5` — **note**: HEAD moved from `01c025b1a` to `ce3574fb` during E2 prototyping (external commit, untouched by E2); the run sheet re-pins at every Phase 1, so use the Phase-1 snapshot, not this §1 value | determinism |
| reference | `phonopy` (`/Users/lwm/code/phonopy`, **read-only**), kind = repo, docs feature surface in `doc/` | the surface tasks derive from |
| reference commit pin | `e66b62d2689b699190606c14a172ebec4dbd86b0` | determinism |
| alignment report | pinned artifact consumed by arm (a) — see Phase 2 | arm-(a) input |
| task suite | `task-suite.md` / `task-suite.csv` (this directory), derived from the reference docs surface | measurement instrument |
| effort budget | k = number of assembled gap-close artifacts; **k = 5 default** (must be `<` pool size so the arms do not trivially cover the same set; see §5) | equalization axis |
| zero-bundle | only host shell + `python3` (stdlib); no `pip install`, no network | discipline |

Neutral-domain extension slot: replace the parameter table (host path, reference
path + kind, doc root, doctrine pointer) and re-run the same phases. Nothing in
Phases 0–7 names a material domain except the *instance* inventory step, which
reads the domain lexicon from the adaptation layer (`references/methodology.md`
§2), per the method's layer discipline.

## 2. Constraints & ethics of measurement (read first)

1. **MatDiscovery is read-only for E2.** It holds a large amount of uncommitted
   work; we only read its tree (`plugins/matdiscovery/skills`,
   `docs/CAPABILITY-SURFACE.md`, `AGENTS.md`, `git rev-parse HEAD`). No
   `git checkout/rm/reset/stash`, no writes.
2. Because the host cannot be written, **assembly is staged**: arm artifacts are
   self-contained, sandbox-executable gap-close units built into the E2 scratch
   tree (`e2-assets/`, `e2-runs/`), shaped by the host's own doctrine
   (CAPABILITY-SURFACE.md §0.1: skill = frontmatter `name/description/metadata`
   + method body; tool-type gaps = script with `--describe`). This is an
   **emulation boundary**, declared here so the paper can word its claims
   precisely (see §10).
3. Zero-bundle and no network: all execution is fixture-local stdlib python3.
4. Honesty rule: this directory keeps "executed/verified" and
   "protocol/planned" apart; no fabricated numbers.

## 3. Artifacts & reproducibility run sheet

Everything lands under `research/runs/e2/`:

```
e2-protocol.md          this file
task-suite.md/.csv      the suite (reference-surface derived)
e2-scripts/             arm_select.py / judge_task.py / derive_tasks.py / run_feasibility.py
e2-assets/              snapshots, pinned report copy, gap pool, fixtures, golds
e2-runs/<run-id>/       one directory per execution, self-contained
```

Determinism: every run records run id, host/ref commit pins, model if an agent
was used, seeds, and the pinned report hash; same-input re-run must reproduce
the verdicts (Layer-1 check #8, `references/evaluation.md`).

---

## 4. Phases

### Phase 0 — Environment & determinism (1 command, check once)

```bash
python3 --version        # >= 3.9, stdlib only
python3 -c "import math,json,subprocess"    # nothing else required
```

### Phase 1 — Snapshots (read-only, pinned)

```bash
HOST=/Users/lwm/code/MatDiscovery
REF=/Users/lwm/code/phonopy
git -C "$HOST" rev-parse HEAD > e2-assets/host-commit.txt
git -C "$REF"  rev-parse HEAD > e2-assets/ref-commit.txt
# host surface = skills + tools + doctrine (inventory-heuristics.md §D)
find "$HOST/plugins/matdiscovery/skills" -maxdepth 1 -type d | sort > e2-assets/host-skills.txt
("$HOST/plugins/matdiscovery/skills" contains 37 skill dirs; audit-count asserted)
# reference docs feature surface (inventory-heuristics.md §A.3)
find "$REF/doc" -maxdepth 1 \( -name "*.md" -o -name "*.rst" \) ! -name conf.py | sort > e2-assets/ref-doc-index.txt
```

### Phase 2 — Alignment report (the input arm (a) acts on)

Run the cap-align workflow (SKILL.md steps 1–9; written when it was 1–7) on reference = phonopy repo,
host = MatDiscovery surface *or* pin the existing case-study record
(`references/methodology.md` §3 records the first instance: 19 gaps, 3 false
catches; the full record lives outside this repo and its location is pinned
here when it is copied in). The report used by E2 MUST:

- be in one fixed file pair `e2-assets/report/capability-alignment-report.md` + `.json`,
  hashed (`shasum -a 256`) into `e2-assets/report/SHA256SUMS`;
- pass **Layer-1 self-check** (all 8 checks green, `references/evaluation.md`);
- state its **recommendation order** explicitly (methodology Phase 5 judgment:
  fix-wrongness > honor-promise > extend-surface, source-kind informed).

From the report, derive the **gap pool** — the `missing`/`partial`
recommendations that cite a rule and carry validated evidence:

```bash
python3 e2-scripts/derive_pool.py \
  --report e2-assets/report/capability-alignment.json \
  --out e2-assets/gap-pool.json   # {gaps:[{id,class,source_kind,priority}]}
```

(`derive_pool.py` implements the extraction: contains only `missing`/`partial`;
`unknown` class rows are excluded, and a `missing` row whose input lacks an
explicit evidence field is kept but flagged in the pool's `warnings` list — the
strict evidence check is the pinned report's Layer-1 #2 gate, already green.)

**Fix-and-pin discipline**: the report is *the same fixed file* for every arm
and every re-run; arms never regenerate it.

### Phase 3 — Task suite derivation (from the reference docs surface)

Rule of non-circularity (this is a correctness property of E2, not a style
rule): **the suite derives from the reference docs feature surface only** —
`task-suite.md` §Derivation. The alignment report's gap labels are attached to
tasks *after* derivation (join on reference capability id) and used only for
stratified analysis. If the report influenced which tasks were sampled, arm (a)
would be favored by construction.

```bash
# 1. enumerate the reference docs feature surface (the derivation input)
find "$REF/doc" -maxdepth 1 \( -name "*.md" -o -name "*.rst" \) ! -name conf.py | sort
# 2. per inventory-heuristics.md §A.3: each feature page documenting a user-facing
#    capability contributes 1..N capabilities; each capability contributes 1..N tasks
#    following the task template in task-suite.md §Derivation (id, input, expected
#    output, judging method).
# 3. register every task in task-suite.csv at the E2 root (single table of truth)
# 4. validate the suite contract:
python3 e2-scripts/derive_tasks.py task-suite.csv --ref-doc-root "$REF/doc"
#    contract: >= 20 real-tier rows; every row traceable to an existing doc page;
#    judge method in {gold, cmd, judge}; primary-judge share < 30%
```

Suite shape obligations (encode what makes E2 fair):

- the suite spans the **whole reference surface** (equivalent + partial +
  missing + unknown cells as derivable), not only the gaps — otherwise "no
  assembly" (arm c) has nothing it can pass and the baseline is vacuous;
- each task states a decidable expected output and one judging method;
- gold files are logged (Layer 2 rule: any adaptation is recorded in the gold's
  `log:` array, never silent).

### Phase 4 — Arms (effort equalization is the confounder control)

Let `G` = gap pool, `k` = effort budget (default 5, fixed for the run), pool
size `|G|` ~ reference-dependent; require `1 ≤ k < |G|` so the arms are not
forced to select the same set.

```bash
# arm (a) — report-ordered: top-k recommendations in the pinned report's order
python3 e2-scripts/arm_select.py --pool e2-assets/gap-pool.json --k 5 --mode top
# arm (b) — random: k without replacement, seeded RNG (seed recorded in run sheet)
python3 e2-scripts/arm_select.py --pool e2-assets/gap-pool.json --k 5 --seed 42 --mode random
# arm (c) — control: no assembly
python3 e2-scripts/arm_select.py --pool e2-assets/gap-pool.json --k 5 --mode none
```

Each selected gap is **staged** as a gap-close artifact in the E2 scratch tree,
shaped by the host doctrine (see §2.2):

- skill-type gap → `SKILL.md` (frontmatter `name/description/metadata` + method
  body + `## Calls`/`## Assembly & inspection` blocks where the host requires,
  per CAPABILITY-SURFACE.md §10.2);
- tool-type gap → python script with a `--describe` self-declaration
  (CAPABILITY-SURFACE.md §5.1);
- the artifact must run in the sandbox with stdlib python3 and fixture inputs
  (the same discipline as the real host's offline minimal cases, §5.2).

Effort accounting (reported per arm, never just asserted equal):

- `effort_tokens(arm)` = Σ byte-count + estimated tokens of staged artifacts
  (`wc -c`), and, when the assembler is an agent, agent steps from the trace;
- equalization: same `k`, same artifact template quality per arm (in the
  feasibility demo: byte-identical templates), recorded, not assumed.

### Phase 5 — Execution (sandbox runner contract)

Each cell (arm × task) is executed by the judge's runner (blind to arm):

```bash
python3 e2-scripts/judge_task.py --task <task-id> --mode gold \
  --runner <staged-artifact> --input <fixture-input> \
  --gold <gold-file> --output-files <declared outputs> \
  --sandbox <cell-dir> --out <cell-dir>/verdict.json
```

Runner contract (all stdlib, no network): subprocess with timeout (default
30 s), cwd = fresh cell dir, captured stdout/stderr, exit code, produced files
checked against the task's declared outputs. A cell with no staged artifact
(arm c, and arm a/b on suite cells outside their selection) is recorded as
`skip` — the three-way verdict vocabulary is `pass | fail | skip`.

### Phase 6 — Judging (three methods, blind, deterministic)

| method | applies to | mechanism |
|---|---|---|
| `gold` | deterministic numeric outputs | deep compare of produced files vs gold file, numeric tolerance (default `1e-6`, both rel and abs); gold provenance logged |
| `cmd` | interface/format tasks | exit 0 + documented regex/URL pattern on stdout or a named output |
| `judge` | outputs needing domain interpretation | rubric in `task-suite.md`; the judge receives only the evidence bundle (task, produced files, rubric) — **arm labels never reach the judge** |

Blindness: `judge_task.py` consumes only `(task, runner, input, gold)`; the
caller (run driver) routes the arm without labeling it. Judge-share cap: ≤ 30%
of real-tier tasks primary-judge; those additionally get a dual-judge pass and
an inter-judge agreement note (folded into the E2 report; `e2-runtime.md`
records the current state: 6/29 = 21%).

Determinism: re-run one seeded arm once; verdicts must be identical
(Layer-1 #8). Confirmed for the mini pipeline in `e2-runtime.md` §Feasibility.

### Phase 7 — Metrics & hypothesis test

For each arm and for the full suite (skips counted as fails for the headline
metric, separately reported as coverage):

- `success(arm) = #pass / #tasks`; `Δ_arm = success(arm) − success(c)`;
- `gain-per-effort(arm) = Δ_arm / effort_tokens(arm)` (both reported);
- `coverage@reference` before/after per arm (adequacy-gated: a task pass is the
  witness test; `formal-foundations.md` §3) — the mechanism metric;
- comparison: `Δ_a` vs `Δ_b` and both vs `0`; effect magnitude read against the
  SoK anchor (+16.2pp over self-generated skills, `experiments.md` §E2);
- plateau check (Assertion B shape): regress success on coverage@ref across
  arms; report the shape rather than forcing a fit.

Report artifact: `e2-runs/<run-id>/summary.md` + `aggregate.json` with every
verdict, effort line, and seed — enough to recompute the table.

---

## 5. Confounder control (explicit ledger)

| confounder | control |
|---|---|
| effort differs between arms | same k; per-gap artifact budget; effort measured and reported (tokens + steps) |
| suite not comparable across arms | suite fixed once (Phase 3); per-arm coverage (= #cells attempted) reported as a covariate; headline metric on the full suite |
| report order leaks into the suite | non-circularity rule (Phase 3); gap labels attached after derivation |
| judging knows the arm | blind judge inputs (Phase 6); judge share capped |
| order effects in execution | task order fixed; run twice (reproducibility) |
| assembler skill differences | same assemblage template quality per arm; agent traces recorded when an agent assembles |
| host drift during the run | snapshot + commit pins (Phase 1); re-run determinism check |

The feasibility run surfaced one real design lesson already: **arm selection
and suite coverage interact** — a report-ordered top-k may buy gaps that the
suite does not sample (demo: arm-a selected 0/3 suite cells). E2 therefore
reports `success-on-attempted` AND full-suite success, and the paper must word
the claim per-arm ("on the cells it staged" vs "on the full reference surface").

## 6. Validity gates

1. Layer-1 self-check green on the pinned report (8/8).
2. Suite contract green (`derive_tasks.py` non-zero exits are a gate).
3. Gold logging: any gold amendment records a `log:` entry, per Layer 2.
4. Determinism: seeded re-run reproduces the verdict table.
5. The pin-hash of the report is part of the run id.

## 7. Limitations (declared, not hidden)

- **Emulation boundary**: E2 grades staged gap-close artifacts in a sandbox; it
  does NOT re-execute the live MatDiscovery routing (offline, no GPU/credentials).
  The claim the paper can make from E2 is stated accordingly (§2.2). End-to-end
  live-host validation is follow-up work, not silently conflated.
- Mini-fixture feasibility numbers are mechanism checks, not measurements.
- Reference golds: where phonopy itself is not installed, golds are computed
  from the reference's documented equations on fixtures (mini tier did this and
  logged provenance); the full run should generate golds from a reference
  executable installation and log that provenance too.
- Full experiment still to run: phases 1–7 on the real pair
  (MatDiscovery × phonopy) with an agent assembling arm (a).

## 8. Script inventory

| script | role | verified |
|---|---|---|
| `e2-scripts/arm_select.py` | deterministic arm selection (top/random/none, seeded) | yes — demo pool, seeds 7/9/42 reproducible |
| `e2-scripts/judge_task.py` | judgment contract (gold/cmd; skip) | yes — controls pass/fail + determinism |
| `e2-scripts/derive_tasks.py` | suite structural validation | yes — 32 rows OK |
| `e2-scripts/run_feasibility.py` | mini-fixture pipeline drive | yes — `feasibility-20261015-184554` |
| `e2-scripts/derive_pool.py` | report JSON → gap pool (Phase 2) | yes — logic exercised on the mini fixture gold via the same extraction in `run_feasibility.py`; CLI run against the real report pending |

## 9. Next step (the full E2 run)

1. Pin the real phonopy↔MatDiscovery report into `e2-assets/report/` (or
   regenerate it through the skill workflow and Layer-1-check it).
2. `derive_pool.py` from the pinned report JSON.
3. Execute Phases 1–7 with an agent assembler (arm a and b), recording traces.
4. Generate real-tier golds from a reference executable install (logged).
5. Aggregate, check the plateau shape, write `summary.md`.

Protocol written 2026-10-15, first instance pinned to the parameters in §1.