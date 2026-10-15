# Alignment report — E1 pilot, judge 1 (self-run of the skill's workflow)

## self_check:
- sections: pass (all 7 present)
- validated evidence: pass (every `missing` row cites a specific module/doc path)
- no-low-driven-missing: pass (qha classified `unknown`, evidence low)
- rule citations: pass (recommendations cite alignment-rules §1–§5)
- source kinds: pass (every gap row tagged)
- host-only tracked: pass
- closing statement: pass
- determinism: pending (run twice; single run recorded here)

## 1. Surfaces
- reference: `tests/fixtures/mini-ref` (kind: repo)
- host: `tests/fixtures/mini-host` (kind: host, 2 skills + tool registry + AUDIT.md)
- generated_at: 2026-10-15

## 2. Reference inventory (mini-ref)

| id | type | conf | evidence |
|---|---|---|---|
| force-constants | compute | high | `src/mini_ref/cli.py` (force_constants module) |
| dynamical-matrix | compute | high | `cli.py` (dynamical_matrix module) |
| phonon-dos | compute | high | `cli.py` (dos module) + docs/band.md |
| band-structure | workflow | medium | docs/band.md (`phon-vib band`) + CLI entry |
| phonon-thermal-properties | compute | high | `cli.py` (thermal_properties module) |
| qha | workflow | low | docs/qha.md only — no `qha` module in source |

Dependency fingerprint: numpy/spglib present; does NOT independently imply a
phonon capability family without module evidence (fingerprint alone = medium at most).

## 3. Host inventory (mini-host)
- skills: heat-flow (lattice kappa via BTE), eos (Birch-Murnaghan fit)
- tools (tool-registry.json): parse-structure, fit-eos
- AUDIT.md self-audit: explicitly admits — no harmonic heat capacity / Cv / F/S/ZPE,
  no phonon DOS or dispersion, no force-constant / dynamical-matrix pathway

## 4. Cross-validation of suspected gaps
For each candidate gap, searched the host tree for an existing partial path:

- force-constants: host grep → no FC module, no tool → confirmed missing
- dynamical-matrix: host has nothing diagonalizing D(q) → confirmed missing
- phonon-dos: host has no DOS → confirmed missing
- band-structure: host has no dispersion → confirmed missing
- phonon-thermal-properties: host has heat-flow, but scrutined: heat-flow's output is
  lattice kappa (BTE), not Cv/F/S/ZPE; AUDIT.md explicitly admits no heat capacity →
  **partial, not missing** (host covers adjacent-but-different territory)
- qha: only docs claim in the reference, no code → evidence low → **unknown**,
  NOT missing (no-low-driven-missing)

## 5. Classification & source tagging
| ref_id | class | source | evidence |
|---|---|---|---|
| force-constants | missing | reference-contrast | module evidence, validated empty in host |
| dynamical-matrix | missing | reference-contrast | same |
| phonon-dos | missing | reference-contrast | module + doc |
| band-structure | missing | reference-contrast | doc + CLI |
| phonon-thermal-properties | partial | host-self-audit | AUDIT.md admits exactly this absence; host_id=heat-flow (adjacent, not covering) |
| qha | unknown | reference-contrast | low evidence only |

host-only: parse-structure, fit-eos, eos (no reference counterpart) — informational.

## 6. Recommendations
- force-constants / dynamical-matrix / phonon-dos / band-structure:
  placement = new tool (or host's own skill `scripts/` if single-consumer);
  rule §1 (axis: deterministic computation → tool/script), §2 (change-count),
  §3 (input contract differs from existing skills → new tool).
- phonon-thermal-properties (partial): extend or add host capability to cover Cv/F/S/ZPE;
  rule §3 (adjacent problem class, different output contract from heat-flow).
- qha: mark unknown / re-inventory when the reference ships actual code.

## 7. Closing statement
Recommendations are placement suggestions; building them is a decision for the host
agent and its human. Unverified capabilities were never treated as missing.