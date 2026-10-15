# E1 Judgment — P2 mini-paper-vs-mini-host (judge-beta)

- run_id: `e1-p2-mini-paper-vs-mini-host-judge-beta-2026-10-15`
- judge: `judge-beta`
- reference surface: `research/runs/e1/judge-inputs/p2-mini-paper-vs-mini-host.json` (reference_inventory reproduced verbatim; 9 capabilities)
- host surface scanned (read-only): `tests/fixtures/mini-host` — skills: `heat-flow`, `eos`; tools: `parse-structure`, `fit-eos`; `AUDIT.md` self-audit. Host surface is fully enumerated (4 files), no other skill dirs, tool registries, or scripts exist.
- doctrine used: `references/alignment-rules.md` + `references/capability-ir.md` (granularity boundary) + `inventory-heuristics.md` §D (incl. mandatory AUDIT-scan) + `methodology.md` §0–§2, §4. Host has no capability doctrine of its own that would override the generic rules.

## Classifications (9 rows)

| ref_id | class | source_kind | confidence | note (host evidence) |
|---|---|---|---|---|
| finite-displacement-phonons | missing | host-self-audit | medium | No host path builds phonons from displacements; heat-flow `skills/heat-flow/SKILL.md:8` requires phonon frequencies "from an upstream capability" that no host component provides; AUDIT.md:8-9 admits no FC/dynmat pathway and no DOS. Displacement/VASP front-end only implicitly admitted → medium. |
| force-constant-assembly | missing | host-self-audit | high | AUDIT.md:9 "No force-constant / dynamical-matrix pathway for any structure"; no FC assembly in skills/ or tools/. |
| vasp-calculator | missing | reference-contrast | high | Host has no DFT surface: tools = parse-structure + fit-eos only; no forces producer anywhere; AUDIT.md silent on DFT. |
| dynamical-matrix-diagonalization | missing | host-self-audit | high | AUDIT.md:9 explicit admission; no dynmat build/diagonalization in host. |
| phonon-dos | missing | host-self-audit | high | AUDIT.md:8 "No phonon DOS or dispersion"; heat-flow consumes frequencies, produces none. |
| heat-capacity | missing | host-self-audit | high | AUDIT.md:5-7 admits no Cv/F/S/ZPE. heat-flow solves BTE for lattice kappa only — adjacent-but-different, does not subsume Cv → missing with near-miss heat-flow (strict-subset semantics). |
| phono3py-bte | equivalent | not-a-gap | high | heat-flow `skills/heat-flow/SKILL.md:8` "Solve the phonon BTE for lattice thermal conductivity … produces kappa(T)"; AUDIT.md:12 confirms BTE lattice-kappa boundary. Missing upstream frequency producer is a separate pipeline gap, not a solver gap. |
| thermal-conductivity-data | equivalent | not-a-gap | high | heat-flow produces kappa(T); reference kappa data differs only in provenance (published vs host-produced), not capability. |
| tetrahedron-integration | unknown | not-a-gap | high | Reference evidence is a single low-confidence mention; low never drives missing (no-low-driven-missing). |

Counts: **9 rows — missing 6, equivalent 2, partial 0, unknown 1, host-only 0.**

## Trap response (each trap_asserted addressed explicitly)

1. **Dependency fingerprints ≠ capabilities / must-run deps are still classified** — handled: VASP is classified `missing` (verified: no DFT surface in host); phono3py-BTE is classified via its solver capability semantic and found `equivalent` (heat-flow covers phonon-BTE lattice kappa). Tool-kind capabilities are not treated as automatic gaps — phono3py-bte is the counterexample.
2. **Reference-data vs host-produced-data is provenance, not capability** — verified: kappa product (Table 1 + raw data) vs heat-flow's `produces kappa(T)` → `equivalent`. Partial is declined for this row precisely because there is no host deliverable the reference data capability represents that the host cannot produce.
3. **AUDIT admissions force source_kind host-self-audit (F2 rule)** — applied: rows force-constant-assembly, dynamical-matrix-diagonalization, phonon-dos, heat-capacity all tagged `source_kind: host-self-audit` (AUDIT.md:5-9), NOT reference-contrast; the AUDIT scan ran before classification.
4. **Adjacent-but-different is MISSING, not partial (strict subsume)** — applied: lattice-kappa heat-flow vs reference heat-capacity (Cv/F/S/ZPE): heat-flow never covers Cv, so the strict-subset test fails and the row is `missing` with heat-flow recorded as the near-miss. The reference workflow row finite-displacement-phonons follows the same logic (heat-flow is downstream of it, not a subset).
5. **No-low-driven-missing** — applied: tetrahedron-integration (single mention, low) is `unknown`, never `missing`.

## Host-only (informational, per methodology §4.4)

- `eos` skill + `fit-eos` tool — Birch-Murnaghan E(V) fit → V0/B0: no reference counterpart in mini-paper inventory.
- `parse-structure` tool — POSCAR → structure dict: no reference counterpart.

## Sources NOT consulted (methodology §4.3)

- Host failure statistics / user-question logs (none exist in the fixture).
- Anything under `tests/fixtures/gold/`, `tests/fixtures/runs/`, `research/runs/e1/draft-gold-*.json`, `research/runs/e4/`, `references/methodology.md` §3, or other judges' outputs — excluded by isolation contract.
- The reference mini-paper itself was not read; per the pair contract the frozen reference input (judge-inputs file) is the only reference surface.