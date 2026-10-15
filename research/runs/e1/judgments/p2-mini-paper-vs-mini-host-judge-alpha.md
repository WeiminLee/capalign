# E1 Judge — P2 mini-paper vs mini-host — judge-alpha

- run_id: `e1-p2-mini-paper-vs-mini-host-judge-alpha-2026-10-15`
- judge: `judge-alpha`
- reference: `tests/fixtures/mini-paper.md` (inventory as given in judge-inputs, 9 rows)
- host: `tests/fixtures/mini-host` (skills: heat-flow, eos; tools: parse-structure, fit-eos; AUDIT.md)
- inputs used (isolation discipline): judge-inputs/p2 file + references/alignment-rules.md + capability-ir.md + inventory-heuristics.md §D + methodology.md §0–§2, §4. **Not read:** any tests/fixtures/gold|runs file, draft-gold-*.json, research/runs/e4/, methodology.md §3, other judges' outputs.

## Classifications (9/9 rows)

| ref_id | class | source_kind | confidence | evidence note |
|---|---|---|---|---|
| finite-displacement-phonons | missing | host-self-audit | high | No part of the displacement→forces→FC→dynmat→DOS→Cv chain in host; AUDIT.md:5-9 self-admits FC/dynmat, DOS, Cv all absent; heat-flow/SKILL.md:8 requires frequencies "from an upstream capability" |
| force-constant-assembly | missing | host-self-audit | high | AUDIT.md:9 "No force-constant / dynamical-matrix pathway for any structure" — direct admission |
| vasp-calculator | missing | reference-contrast | high | Host has no DFT surface at all (scan: only parse-structure/fit-eos tools, heat-flow/eos skills); AUDIT silent on DFT → not self-audit |
| dynamical-matrix-diagonalization | missing | host-self-audit | high | AUDIT.md:9 "No force-constant / dynamical-matrix pathway for any structure" — direct admission |
| phonon-dos | missing | host-self-audit | high | AUDIT.md:8 "No phonon DOS or dispersion" — direct admission |
| heat-capacity | missing | host-self-audit | high | AUDIT.md:5-7 admits no Cv / F / S / ZPE; heat-flow (lattice kappa) is adjacent-but-different, not strict subset → missing with near-miss recorded |
| phono3py-bte | equivalent | reference-contrast | high | heat-flow/SKILL.md solves phonon BTE → kappa(T), same semantics as phono3py RTA solver; running the specific solver (dependency fingerprint) is not the capability |
| thermal-conductivity-data | equivalent | reference-contrast | high | heat-flow produces kappa(T) on demand; published-vs-produced is provenance, not capability difference; no deliverable host cannot produce |
| tetrahedron-integration | unknown | reference-contrast | low | Single mention, inventory confidence low → never missing (no-low-driven-missing); host silent, cannot cross-validate |

## Trap responses (traps_asserted from judge-inputs)

1. **Dependency fingerprint ≠ capability (VASP / phono3py are must-run deps).** vasp-calculator classified missing — but on real absence: host has no DFT/electronic-structure surface anywhere (verified by full fixture scan), not merely "didn't install VASP". phono3py-bte classified **equivalent** — host heat-flow skill implements the BTE-solving semantics the dep provides; not a tool-kind auto-gap.
2. **Data provenance (Table 1 kappa + raw data) vs host-produced kappa(T).** Classified **equivalent**: heat-flow produces kappa(T) on demand; provenance (published pre-computed vs on-demand) is not a capability difference. To claim partial one must name a deliverable the host cannot produce — none identified.
3. **AUDIT.md admissions (FC / dynmat / DOS / Cv).** Rows force-constant-assembly, dynamical-matrix-diagonalization, phonon-dos, heat-capacity, and the finite-displacement workflow are tagged **host-self-audit** (F2 rule), anchored line-by-line to AUDIT.md. vasp-calculator is NOT self-audit (AUDIT never mentions a DFT/electronic-structure engine) → reference-contrast.
4. **Adjacent heat-flow (lattice kappa) vs reference heat-capacity (Cv/F/S/ZPE).** heat-capacity = **missing**, with the heat-flow near-miss recorded in the note — not partial: heat-flow covers kappa(T), a different physical quantity; it does not strictly subsume Cv/F/S/ZPE (strict-subsume, pilot F1). Similarly the BTE/DOS/frequency side of heat-flow does not subsume the phonon-DOS computation.
5. **tetrahedron-integration single-mention/low.** **unknown** at low confidence — no-low-driven-missing (capability-ir.md #6, alignment-rules "Never" rule). Not upgraded to missing even though the host has no DOS machinery at all: the reference-side evidence itself is too weak.

## Host-only (informational, per methodology §4.4 — not in JSON, which contains only ref_ids)

- `eos` skill + `fit-eos` tool (Birch-Murnaghan E-V fit → V0/B0): no reference counterpart.
- `parse-structure` tool (POSCAR → structure dict): no reference counterpart.

## Hardest rows (2-3)

1. **phono3py-bte (equivalent, high)** — hardest because a `tool`-typed reference (a named solver, phono3py RTA) is being mapped onto a host `skill` that never mentions phono3py. The whole call hinges on capability-vs-dependency semantics: the host has zero phonon-frequency machinery, so if one reads "phono3py" as "solving the BTE", heat-flow covers it; if one reads it as "must run phono3py output", it looks missing. Trap 1 explicitly resolves it to equivalent, and the semantics argument (BTE solve → kappa) held: a user asking "compute lattice thermal conductivity" is served by heat-flow. Confidence high, but this is the row most likely to split judges.
2. **finite-displacement-phonons (missing, host-self-audit, high)** — the workflow row is the aggregation of four separately-admitted gaps. AUDIT.md never names the workflow as a whole ("finite displacement"), so tagging it host-self-audit required the judgment that the workflow cannot exist once its constitutive steps (displacements/forces → FC → dynmat → DOS → Cv) are each admitted absent — plus heat-flow's explicit dependency on upstream frequencies. A stricter reading might tag it reference-contrast; I chose self-audit because the host already owes the entire chain.
3. **tetrahedron-integration (unknown, low)** — deceptively tempting to mark missing: the host demonstrably has no DOS machinery, and a domain expert knows tetrahedron integration is a DOS-construction subtask. But the reference-side evidence is a single passing mention at low confidence, and the rules forbid low-driven-missing twice over (IR #6, alignment-rules Never). The discipline of not letting my domain knowledge upgrade an evidence-weak row is why it stays unknown.

## Summary counts

- Classified: 9 rows (all reference_inventory ref_ids).
- class: equivalent 2 | partial 0 | missing 6 | unknown 1
- source_kind: host-self-audit 5 (finite-displacement-phonons, force-constant-assembly, dynamical-matrix-diagonalization, phonon-dos, heat-capacity); reference-contrast 4 (vasp-calculator, phono3py-bte, thermal-conductivity-data, tetrahedron-integration); domain-inference 0.