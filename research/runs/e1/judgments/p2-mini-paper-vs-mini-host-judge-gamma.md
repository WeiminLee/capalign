# E1 judge record — P2 mini-paper ↔ mini-host (judge-gamma)

- run_id: `e1-p2-mini-paper-vs-mini-host-judge-gamma-2026-10-15`
- judge: `judge-gamma`
- pair: `p2-mini-paper-vs-mini-host`
- frozen reference surface: `research/runs/e1/judge-inputs/p2-mini-paper-vs-mini-host.json` (its `reference_inventory`, 9 rows)
- host scanned (read-only): `tests/fixtures/mini-host` — `AUDIT.md`, `skills/heat-flow/SKILL.md`, `skills/eos/SKILL.md`, `tools/tool-registry.json` (2 tools: `parse-structure`, `fit-eos`)
- date: 2026-10-15

No host file was written; only `ls`/`grep`/`Read` used on the host surface.

## Classifications (9 rows)

| ref_id | class | source_kind | confidence | note |
|---|---|---|---|---|
| finite-displacement-phonons | missing | host-self-audit | high | No displacements→FC→dynmat→DOS→Cv pipeline; heat-flow only *consumes* phonon frequencies "from an upstream capability" (`skills/heat-flow/SKILL.md:9`); AUDIT.md admits the pathway step-by-step (:5–9). |
| force-constant-assembly | missing | host-self-audit | high | No FC computation anywhere; AUDIT.md:9 "No force-constant / dynamical-matrix pathway for any structure." |
| vasp-calculator | missing | reference-contrast | high | No DFT/forces surface: grep vasp\|ase\|dft = 0 hits; tools are only parse-structure/fit-eos. AUDIT does not admit a VASP/DFT gap → reference-contrast, not host-self-audit. |
| dynamical-matrix-diagonalization | missing | host-self-audit | high | No dynmat in host; AUDIT.md:9 admits the FC/dynmat pathway gap. |
| phonon-dos | missing | host-self-audit | high | No DOS/dispersion; AUDIT.md:8 "No phonon DOS or dispersion." |
| heat-capacity | missing | host-self-audit | high | AUDIT.md:5–7 explicitly admits no Cv/F/S/ZPE. Near-miss: heat-flow lattice kappa is adjacent-but-different, does not subsume Cv → missing, not partial. |
| phono3py-bte | equivalent | reference-contrast * | high | heat-flow is itself the BTE solver unit ("lattice thermal conductivity kappa from the phonon Boltzmann transport equation", `skills/heat-flow/SKILL.md:3,8`); phono3py identity is implementation plating. |
| thermal-conductivity-data | equivalent | reference-contrast * | high | heat-flow produces kappa(T) (`.md:9`); published-vs-produced is provenance, not capability; no host-impossible deliverable shown. Upstream-frequency gap charged to pipeline rows, not this row. |
| tetrahedron-integration | unknown | reference-contrast * | low | Single low-confidence mention; low-only evidence never drives missing; semantics uncharacterizable. Host "tetrahedron" grep = 0 hits is informational only. |

\* `source_kind` convention: the three source kinds are defined for *gaps* (`alignment-rules.md` §Gap source kinds). For non-gap rows (`equivalent`, `unknown`) I record the nominal value `reference-contrast` (classification stems from comparing both surfaces; no host self-audit statement bears on these rows). Flagged here so inter-judge κ comparisons know the convention.

## Trap responses (all 5 addressed explicitly)

1. **Must-run deps are hard tool caps; VASP missing, phono3py-BTE equivalent; tool caps ≠ auto gaps.** — Confirmed by grep: VASP row has no host counterpart (zero DFT/forces surface) → `missing` (reference-contrast). phono3py-BTE → `equivalent` via heat-flow (the skill *is* a BTE-solver capability; solver name is plating). No row was classified on fingerprint alone; each tool-kind row was matched to an actual host surface element.
2. **Kappa data: provenance ≠ capability → equivalent; partial requires a host-impossible deliverable.** — Confirmed: heat-flow's stated output is kappa(T); the reference's published Table 1 + raw data is the same semantic unit. No deliverable of the reference data row that heat-flow cannot produce *given upstream frequencies*; the missing-frequencies shortfall is the pipeline gap, charged there.
3. **AUDIT.md admissions → host-self-audit, not reference-contrast.** — Confirmed: force-constant-assembly, dynamical-matrix-diagonalization, phonon-dos, heat-capacity each map to an explicit AUDIT.md line; finite-displacement-phonons is tagged host-self-audit by composition (every step of the workflow is audit-admitted). vasp-calculator kept reference-contrast because the AUDIT does not mention VASP/DFT.
4. **heat-flow (lattice kappa) vs heat-capacity (Cv/F/S/ZPE) = adjacent-but-different → missing with near-miss, not partial.** — Confirmed: strict-subset test fails (lattice kappa does not subsume harmonic Cv/free energy/entropy/ZPE); heat-flow named as the near-miss in the note.
5. **tetrahedron-integration is single-mention/low → unknown, never missing.** — Confirmed: class `unknown`, confidence `low`; the "no-low-driven-missing" discipline applied.

## Classes summary

- total: **9**
- equivalent: **2** (phono3py-bte, thermal-conductivity-data)
- partial: **0**
- missing: **6** (finite-displacement-phonons, force-constant-assembly, vasp-calculator, dynamical-matrix-diagonalization, phonon-dos, heat-capacity)
- unknown: **1** (tetrahedron-integration)
- source_kind: host-self-audit ×5, reference-contrast ×4 (3 nominal for non-gaps)

## Sources deliberately NOT consulted (standing discipline, methodology §4.3)

- `tests/fixtures/gold/**` (incl. gold/mini-ref-vs-mini-host.json) and `tests/fixtures/runs/**` — forbidden by protocol
- `research/runs/e1/draft-gold-*.json` and `research/runs/e4/**` — forbidden by protocol
- `references/methodology.md` §3 (instance answer record) — forbidden by protocol
- other judges' outputs — forbidden by protocol
- the reference paper `tests/fixtures/mini-paper.md` itself — the frozen reference surface for this run is the judge-input file only; reference evidence was taken verbatim from its `reference_inventory`

## Hardest rows (2–3)

1. **phono3py-bte** (equivalent vs missing): the reference names a specific solver, the host names none and needs upstream frequencies. The call hinged on whether the semantic unit is "solve the phonon BTE → kappa" (host covers it; solver name is plating) or "phono3py the specific tool" (host lacks it). Resolved via `capability-ir.md` granularity rule 3 + the skill's own BTE routing trigger.
2. **thermal-conductivity-data** (equivalent vs partial): published *dataset product* vs a *generator* that cannot run end-to-end today (missing upstream frequencies). The tension is provenance-≠-capability versus "host can't actually reproduce this dataset now". I ruled equivalence and charged the upstream shortfall to the pipeline rows; a judge weighting current runnability could argue partial — but per the trap rule, partial requires a deliverable the host cannot produce, and kappa(T) data is produceable once the (charged elsewhere) pipeline exists.
3. **finite-displacement-phonons** (workflow granularity + source kind): it is not a single audit-admitted item; whether it is "just the sum of its missing steps" or a distinct orchestration capability, and whether its source tag follows the admitted steps (host-self-audit) or the reference contrast work (reference-contrast), is the likeliest inter-judge divergence on this pair.