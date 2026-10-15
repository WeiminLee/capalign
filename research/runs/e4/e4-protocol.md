# E4 protocol — self-referential vs gold-fed alignment (two-pass, input-frozen)

Status: protocol v0.1 (2026-10-15). Instantiated on the mini fixtures — see
`e4-run-mini.md` (measured) and `e4-calibration.md` (curve sketch). Runs through
the **skill's own workflow** (`SKILL.md` steps 1–7), zero-bundle: host shell +
`python3` stdlib only. Nothing in this protocol touches the gold fixtures or the
rule files in `references/`.

---

## 1. Purpose and formal objects

E4 (experiments.md §E4) tests **assertion D** (formal-foundations.md §5): an agent
auditing its own capability surface shows `bias ≥ 0` (self-reports over-claim), yet
the bias is stable per source and correctable; `cal` (verification hit-rate per
confidence label) is monotone in `confl`. If the self-report is *uncalibratable*
(bias varies without recoverable structure), the closed-loop governance claim
weakens to **external-audit-only** — we state that boundary up front and run E4 to
find which regime we are in.

Three measured objects, all defined on a **frozen input** (same reference, same host
artifact tree, same reference IR in both passes):

| quantity | definition | where |
|---|---|---|
| `drift(H)` | `|Claim(H) − Verified(H)| / |Claim(H)|` (declared but unproven) | formal-foundations §4 |
| `bias` | `drift(H_self-reported) − drift(H_externally-verified)` | formal-foundations §5 |
| `cal(l)` | `P(conf-label = verified | label = l)` for `l ∈ {high, medium, low}` | formal-foundations §5 |
| gap-table agreement | class and source-kind agreement between pass-1 and pass-2 gap tables | experiments.md §E4 |

`Claim(H)` = the capabilities the host or its documents declare (positive claims:
"this host can do X"). Admitted absences ("I do not have X") are **negative
reports** — kept in a separate ledger, not counted as claims, and validated
separately. `Verified(H)` is tiered (rising strictness):

- **t1, claim-resolution** — a declared capability has (a) a carrier artifact on
  the host and (b) a satisfiable input contract from the host's own surface.
- **t2, witness-test** — `confl ≥ medium` **and** a reproducible execution
  (fixture gold / `--describe` / determinism re-run) proving the capability
  performs (formal-foundations §3 `Prov(h)`).

Both tiers are computed; the paper's headline uses the tier matched to the corpus
(t2 on real libraries with runners, t1 where no executable carrier exists).

## 2. Input freeze

Both passes consume **byte-identical** inputs:

- reference = `tests/fixtures/mini-ref` (the phonon toolkit), host =
  `tests/fixtures/mini-host` (2 skills + tool registry + AUDIT.md) — **or** the same
  pair at a pinned commit for the real-library extension (§8).
- Reference IR is built **once** by `inventory_repo` (§3 step 1) and frozen: both
  passes start from that exact capability table, never re-derived.
- Freeze hash (sha256 over the 10 fixture input files, incl. the gold JSON) —
  recorded in `e4-run-mini.md` §inputs: `22cc4d6b…aa917`. A re-run whose hash
  differs is a different input and is logged as such.

## 3. Pass 1 — self-referential (trigger, zero-bundle)

The host agent audits **itself**. Trigger = the skill workflow exactly as in
production; there is no E4-specific harness:

```
1. inventory_repo:    reference = tests/fixtures/mini-ref
2. inventory_host:    host = tests/fixtures/mini-host   # §D auto-scan: the host
                       # reads its OWN skills/, tool registry, AUDIT.md — the
                       # self-report (skills + tools + self-admitted gaps)
   # §D.3 self-audit scan is MANDATORY and drives source kind:
   #   a gap the host's own AUDIT.md admits  -> source_kind = host-self-audit
3. Normalize            (capability-ir.md §Normalization)
4. Cross-validate       (grep the host tree for every candidate term; §4 below)
5. Classify & source-tag (alignment-rules.md §Gap classification, strict subsume)
6. Recommend            (rule-cited placement for every missing/partial)
7. Report + Layer-1 self-check (8/8 green, incl. determinism re-run)
```

Cross-validation commands (real, run in `e4-run-mini.md`):

```bash
find host -type f | sort
for t in "force_const" "dynamical" "dos" "band" "qha" "thermal" "Cv" "heat capacity" "kappa" "zero-point" "entropy"; do
  grep -rli "$t" tests/fixtures/mini-host || echo "NONE: $t"
done
ls tests/fixtures/mini-ref/src/mini_ref/     # qha module must NOT exist
```

Every candidate `missing`/`partial` needs validated evidence (paths/quotes from
host + reference artifacts), never the comparison table alone
(`methodology.md` §2, `SKILL.md` step 4). The pass-1 gap table is recorded
verbatim as `fixture-inputs/run1-self-gaps.json`.

## 4. Pass 2 — gold-fed (trigger)

Second alignment on the **same frozen reference IR**, with the host surface
**supplied externally** instead of self-scanned:

```
1. inventory_repo:    reference = tests/fixtures/mini-ref    (same frozen IR)
2. inventory_host:    surface = tests/fixtures/gold/mini-ref-vs-mini-host.json
                      host-side information (host_only list, host_id near-misses,
                      externally-verified source kinds) — the agent receives the
                      host surface, it does not scan itself
3. Normalize / 4. Cross-validate / 5. Classify / 6. Recommend / 7. Report
   — identical steps; the host-surface source is the ONLY independent variable
```

The pass-2 gap table is the externally-verified verdict; on the fixtures it is the
gold table by construction. Recorded as `fixture-inputs/run2-gold-gaps.json`.

## 5. Measurement step (post-align, still zero-bundle)

After both passes, build the capability-level **verification ledger** (positive
claims with `conf` label, carrier, t1/t2 verdict, fail reason; negative reports
checked by grep) and compute the numbers with the stdlib-only bookkeeper:

```bash
python3 e4_calib.py --self fixture-inputs/run1-self-gaps.json \
                    --gold fixture-inputs/run2-gold-gaps.json \
                    --ledger fixture-inputs/verify-ledger.json \
                    --out fixture-inputs/metrics.json
```

(`e4_calib.py` is a measurement ledger, **not** an alignment instrument — it adds
nothing to the skill's runtime; the two gap tables and the ledger come from the
workflow itself.)

## 6. Formulas landed (with worked examples)

**Measured on the mini fixtures (real run 2026-10-15 — mini-scale, non-conclusive):**

```
Claim(self) = Claim(gold) = {heat-flow, eos, parse-structure, fit-eos},  n = 4
Verified(t1) = {eos, parse-structure, fit-eos}                            v = 3
drift(t1) = |4 − 3| / 4 = 0.25                     (self) and 0.25 (gold)
bias(t1)  = 0.25 − 0.25 = 0.0
cal(t1, high) = P(verified | high) = 3/4 = 0.75    (heat-flow fails: its kappa
                                          promise needs phonon frequencies the
                                          host cannot produce)
t2: Verified = ∅ (no executable artifact on mini-host) -> drift = 4/4 = 1.0 in
    both passes; bias = 0.0 (tier saturates; stated, not hidden)
gap agreement: class 6/6 (1.0), source_kind 2/6 (0.33) — see e4-run-mini.md §results
negative reports (admitted absences): 5/5 accurate
```

**Synthetic example (illustrative arithmetic only — NOT a measurement; a 10-claim
host as a real-library run could look like):**

```
Host declares 10 capabilities, source log: 6 from skill docs, 4 from tool registry.
Pass 2 (external) validates 8/10            -> drift(gold) = 0.20
Pass 1 (self)  claims 12 (2 self-promoted, no artifacts)
                                             -> drift(self) = (12−8)/12 ≈ 0.333
bias = +0.133  (positive: over-claim direction assertion D predicts)
cal: high 5/5 = 1.00, medium 2/3 ≈ 0.67, low 0/2 = 0.00   (monotone in confl ✓)
per-source: skill-docs drift 2/6 ≈ 0.33 > registry 0/4 = 0.0  (source structure ✓)
```

## 7. Verdict criteria (run-level, per corpus)

For each run pair, in order:

1. **Validity gates first**: both passes green on Layer-1 (8/8), determinism
   re-run identical (Layer-1 #8). A red gate invalidates the pair, no verdict is
   drawn.
2. **Bias branch** — `bias ≥ 0`: assertion D's over-claim direction holds on this
   corpus. `bias < 0` (self-reports *under*-claim) or `bias ≈ 0` with no
   detectable effect: the over-claim hypothesis is not supported here; say so.
3. **Calibration branch** — `cal` monotone in `confl` (non-increasing pass-rate as
   labels weaken) **and** per-source drift shows recoverable structure:
   assertion D holds → self-audit usable with per-source correction.
   `cal` non-monotone **or** bias varying without structure: **external-audit-only
   boundary** — closed-loop governance requires the external carrier; written into
   the paper, not papered over.
4. **Sample-size guard** — a verdict needs label cells with `n ≥ 5` claims each
   and ≥ 2 source kinds; below that the run is "feasibility signal", not a
   verdict. The mini run below is exactly that: a feasibility signal.

## 8. Extension to real libraries (the protocol's real target)

The mini fixtures seed the mechanism, not the numbers. Next run pairs, cheapest
first:

| pair | pass 1 (self) | pass 2 (external) | why |
|---|---|---|---|
| **MatDiscovery, 37 skills** | agent runs `inventory_host §D` over its own `plugins/matdiscovery/skills`; self-reported claims + `SKILLS-AUDIT` admissions | host surface = code-scraped registry (`research/tools/build-registry.py`, 71 tools + 99 artifacts) + human-checked subset; drift via `drift-meter` semantics at capability level | existing drift corpus, mixed claim sources (paper-methods / repo-docs / scenario skills) → per-source calibration cells |
| **K-Dense scientific-agent-skills** | agent self-scans the freshly cloned skills | external = repo docs + file tree resolution (no self-admission artifact to lean on) | the predictable over-claim case: no AUDIT.md, so pass 1 has nothing honest to seed |

Determinism re-run per pair (Layer-1 #8), freeze hash recorded, and every number
tagged with its tier (t1/t2) and its label cell sizes.

## 9. Standing discipline (inherited + E4-specific)

- Zero-bundle, skill workflow only; no edits to `tests/fixtures/gold/` or
  `references/`; no commits; MatDiscovery read-only.
- E4-specific honesty: (a) every number carries "measured" or "synthetic example";
  (b) saturated tiers are reported, not suppressed; (c) a pass-2 table is the gold
  table *only because* the gold is the externally-verified answer — on real pairs
  nothing gives the answer away, and pass 2 stands alone.