# E1 Judgment — P1 phonopy vs MatDiscovery — judge-alpha

- run_id: `e1-p1-phonopy-vs-matdiscovery-judge-alpha-2026-10-15`
- judge: `judge-alpha` (independent; frozen reference = `judge-inputs/p1-phonopy-vs-matdiscovery.json`; host scanned read-only at `/Users/lwm/code/MatDiscovery`)
- date: 2026-10-15
- Isolation note: every classification below is grounded in host files read/grepped during this run. methodology.md §3 (instance record) was returned incidentally by a full-file read before its prohibition was noticed; it was not used as evidence — no classification depends on it.
- Host self-audit scan (F2) performed: `docs/SKILLS-AUDIT-2026-09-24.md`, `docs/SKILL-DESIGN.md` §9 roadmap, `docs/CAPABILITY-SURFACE.md`, AGENTS.md. Only the QHA-α gap was host-admitted (§1.4) and it has been closed on 2026-10-15 (`mat_thermal_expansion`); no other of the 13 reference capabilities maps to an open host-admitted gap, so no source_kind is `host-self-audit`.

## Classifications (13)

| ref_id | class | source_kind | confidence | evidence note |
|---|---|---|---|---|
| fc-assembly | partial | reference-contrast | medium | FC assembly (displacement->forces->produce_force_constants->symmetrize, space-group symmetry) runs INSIDE host workflows: `fieldmat-runners/simple_mattersim_qha_muxi.py:529-539`, `remote_mattersim_runner.py run_phonon:2691-2711` (mattersim PhononWorkflow), `tools/bte-controller/src/bte_controller/core.py:490-504`. But FCs are an embedded intermediate, not a standalone user deliverable on primary routes; fc2/fc3 hdf5 only as optional remote phonon_bte_kappa artifacts. Strict subset -> partial. |
| phonon-dos | equivalent | reference-contrast | high | `mat-phonon` SKILL.md (ga) covers total+projected DOS; phonon task materializes `phonon/total_dos.dat` (default 'dos') + `phonon/projected_dos.csv` (`remote_mattersim_runner.py:494-499,2565-2627`); audit §6.2 verified PDOS produced. Same phonopy DOS/PDOS semantics. |
| band-structure | partial | reference-contrast | medium | `phonon/band.yaml` delivered when 'dispersion' requested (default; artifact spec `remote_mattersim_runner.py:495`; `workflow-phonon-thermal.md:32`), written by upstream PhononWorkflow. But q-path is auto-planned only: `phonon_runtime_plan` exposes supercell/qmesh/amplitude, no BAND path segments; no phonopy-bandplot equivalent. Strict subset of phonopy BAND+bandplot -> partial; deliverable real, so not missing. |
| group-velocity | equivalent | reference-contrast | medium | `phonon/group_velocity.csv` via `run_mesh(with_group_velocities=True)` when requested (`remote_mattersim_runner.py:2536-2541,2631-2690`); documented in mat-phonon SKILL.md + `workflow-phonon-thermal.md:35`. Same mesh-group-velocity semantics as phonopy. |
| thermal-properties-harmonic | equivalent | reference-contrast | high | `phonon/thermal_properties.csv` via phonopy `run_thermal_properties` (tmin/tmax/tstep/cutoff configurable): free_energy/entropy/cv vs T + ZPE (`remote_mattersim_runner.py:2531-2574`). Same F/S/Cv/ZPE semantics as phonopy. |
| mode-gruneisen | partial | reference-contrast | medium | Mode-resolved γ(q,i) exists ONLY on QHA explicit-request path: `gruneisen.csv` when requested_properties includes 'gruneisen' (`simple_mattersim_qha_muxi.py:543-549,583-673,848-856`; qha SKILL.md:33), 3-volume central log-difference on QHA q-mesh. Not on standalone phonon route (grep: gruneisen only in qha muxi/qha skill/`validate-parameters.ts:234`); no standalone CLI/plot. Strict subset -> partial. |
| qha-thermodynamics | partial | reference-contrast | high | qha_simple runs PhonopyQHA per pressure -> `e_v.csv, volume_temperature.csv, gibbs/cp/entropy/enthalpy_at_veq.csv` (+gruneisen.csv on request); α(T) derived locally by `mat_thermal_expansion` (`tools/mat-local-compute/.../thermo.py`; server.py:202-223) from volume_temperature.csv interior points ONLY — qha SKILL.md description states 'interior temperatures only, never the endpoints' and 'no runner-side table'. Strict subset (no endpoint α, no bulk-modulus-vs-T) -> partial. Historical: whole-α gap was host-admitted (SKILLS-AUDIT-2026-09-24 §1.4), closed 2026-10-15. |
| nac-lo-to | missing | reference-contrast | high | Zero nac_params/Born-effective-charge/LO-TO anywhere (grep verified); all phonopy routes build without NAC. Only 'Born' in host = mechanical Born stability (mat-elasticity SKILL.md:29; audit §4.2) — adjacent-but-different. missing stands. |
| electronic-thermal | missing | reference-contrast | high | No electronic DoS/tetrahedron/electronic-thermal anywhere; VASP route parses only TOTEN/scf/relax (`src/vasp-parse.ts`); `thermal-router.md:31` itself tells the agent to ask whether an electronic contribution is required (host has none). |
| irreps-symmetry | missing | reference-contrast | high | Zero irrep/character-table/symmetry-adapted machinery; only symmetry product is a space-group label (`mat_analyze_structure` -> spacegroup_after) — space-group reporting does not subsume mode irreps. |
| mlp-sscha | missing | reference-contrast | medium | Zero sscha; host MLFF (MatterSim) singlepoint/MD adjacent with different input contract (no self-consistent/renormalized-phonon loop) -> missing, not partial. |
| dynamic-structure-factor | missing | reference-contrast | medium | Zero S(q,ω)/inelastic machinery; host static S(q) (`mat_compute_structure_factor` from rdf_rows, `descriptors.py`) is adjacent-but-different -> missing. |
| site-mixture-vca | unknown | reference-contrast | medium | Zero site-mixture/VCA in host; reference evidence is an [Experimental] CLI flag only (confidence low) -> never missing -> unknown. |

## Counts

- total classified: 13 (all ref_ids in the frozen reference_inventory)
- equivalent: 3 (phonon-dos, group-velocity, thermal-properties-harmonic)
- partial: 4 (fc-assembly, band-structure, mode-gruneisen, qha-thermodynamics)
- missing: 5 (nac-lo-to, electronic-thermal, irreps-symmetry, mlp-sscha, dynamic-structure-factor)
- unknown: 1 (site-mixture-vca)

## Traps addressed (each asserted trap explicitly checked against host evidence)

1. **Dependency fingerprint ≠ capability** — phonopy 4.8.1/phono3py 4.8.2 are `.venv` installs (`tools/bte-controller` Requires-Dist). No classification rests on the install: fc-assembly partial rests on the actual runner computation paths (qha muxi 529-539, bte-controller 490-504); dos/band/gv/thermal rest on the phonon task contract (artifact spec + skill); nac-lo-to stays missing even though phonopy supports NAC upstream (host surface never exposes it).
2. **Born mechanical ≠ Born effective charges** — verified: all host 'Born' hits are stiffness-tensor eigenvalue checks (mat-elasticity SKILL.md:29 'all eigenvalues of the stiffness tensor are positive'; audit §4.2). nac-lo-to = missing.
3. **mode-gruneisen** — read `write_mode_gruneisen` semantics: it IS mode-resolved γ(q,i) (log ω vs log V central difference) but only on the QHA explicit-request path with a 3-volume window; 'existed in the host' not over-applied to equivalent → partial (strict subset), as the instance kill is a subset, not a superset.
4. **qha α** — verified: `mat_thermal_expansion` (2026-10-15) interior-points-only (qha SKILL.md description verbatim); interior-only derivation keeps it a strict subset → partial, not equivalent.
5. **sscha/MLP** — zero sscha; MatterSim FF singlepoint/MD adjacent (different input contract) → missing, not partial.
6. **static vs dynamic S(q)** — host `mat_compute_structure_factor` is static (sinc transform of rdf_rows); does not subsume dynamic S(q,ω) → missing.
7. **site-mixture VCA** — experimental CLI-only reference evidence (low) → unknown, never missing.
8. **irreps** — space-group reporting (`mat_analyze_structure` spacegroup_after, used by mat-relax-analysis) does not subsume mode irreps/character tables → missing.

## Hardest calls (judge's own view)

1. **band-structure (partial vs equivalent)** — the host genuinely delivers `band.yaml` (dispersion is a default-requested property), but the q-path is auto-planned by the upstream PhononWorkflow with no user BAND control and no plot CLI. Choosing partial requires treating path-selection as part of the capability semantics rather than a parameter detail; choosing equivalent requires treating 'dispersion along some path' as the whole semantic. I chose partial (strict-subset reading), medium confidence — the same logic the model applies to mode-gruneisen (path/route restriction ⇒ strict subset).
2. **fc-assembly (partial vs missing)** — the assembly computation is demonstrably performed (phonopy calls in three routes) but its only standalone deliverables are optional fc2/fc3 hdf5 on the remote BTE path (helper not vendored, unverifiable locally). If 'user-reachable deliverable' is read strictly, missing is defensible; I chose partial because the computation is real, symmetry-reduced, and BTE-scoped FC artifacts exist — a strict subset, medium confidence.
3. **mode-gruneisen vs qha-thermodynamics source-kind split** — both depend on the same QHA machinery; keeping mode-gruneisen partial (explicit-request-only, coarse 3-volume difference, no plot) while qha-thermodynamics is the broader workflow required careful separation so the two notes don't contradict (mode-gruneisen's narrowness is the reason it is not equivalent; qha's interior-only α + no bulk-modulus-vs-T is why it is not equivalent).

## Sources consulted (host, read-only)

- docs/: CAPABILITY-SURFACE.md, SKILLS-AUDIT-2026-09-24.md, SKILL-DESIGN.md (§6-§9), AGENTS.md (working memory)
- plugins/matdiscovery/: skills mat-phonon (+references), mat-qha-thermal-expansion, mat-lattice-thermal-conductivity, mat-vasp-calculation, bte-thermal-conductivity-scenario; src/: direct-tools.ts, fieldmat-config.ts, tasks.ts, vasp-parse.ts, vasp-tools.ts; fieldmat-runners/: remote_mattersim_runner.py, simple_mattersim_qha_muxi.py
- tools/: mat-local-compute (server.py, descriptors.py, thermo.py, transport.py), bte-controller (core.py)
- NOT consulted (prohibited / out of scope): tests/fixtures/gold, tests/fixtures/runs, research/runs/e1/draft-gold-*.json, research/runs/e4, other judgments, methodology.md §3 (beyond the accidental full-file read noted above).