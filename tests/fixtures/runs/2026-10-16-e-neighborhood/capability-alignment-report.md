# Alignment report — mini-ref vs mini-host (recover_reference §E)

## self_check:
- sections: pass (surfaces, reference inventory, host inventory, gap table, recommendations, host-only, neighborhood, unresolved)
- validated evidence: pass (every `missing` row cites a module/doc/AUDIT path, not the comparison table)
- no-low-driven-missing: pass (repo-arm `qha` is `unknown`; neighborhood `mini-3ph` is `unknown`; neither drives `missing`)
- rule citations: pass (each recommendation cites alignment-rules §1–§5)
- source kinds: pass (every gap row tagged)
- host-only tracked: pass (parse-structure, fit-eos, eos)
- closing statement: pass (verbatim)
- determinism: pass (second pass on the same fixtures produced an identical gap table)
- neighborhood stratified: pass (companion paper is core; neighborhood ids absent from the core repo gap table; search-snippet-only evidence did not drive `missing`)

## 1. Surfaces
- reference: `tests/fixtures/mini-ref` (kind: repo, layer: core)
- host: `tests/fixtures/mini-host` (kind: host; 2 skills + tool registry + AUDIT.md)
- generated_at: 2026-10-16
- companion_paper: recovered — `CITATION.cff` DOI `10.1234/mini-ref.2015`, local text `papers/qha-mini-ref-2015.md` (relation: companion-paper, layer: core)
- search: necessary (README names `mini-3ph` with no URL); source = `neighborhood-search-double.json` (fixture; live network not used); queries ≤ 3, neighborhood kept ≤ 5
- doctrine: generic alignment-rules (mini-host has no CAPABILITY-SURFACE.md)

## 2. Reference inventory

### 2.1 Repo projection (`layer: core`, `source_kind: repo`)

| id | type | conf | evidence |
|---|---|---|---|
| force-constants | compute | high | `src/mini_ref/cli.py` `force_constants` |
| dynamical-matrix | compute | high | `cli.py` `dynamical_matrix` |
| phonon-dos | compute | high | `cli.py` `dos` + `docs/band.md` |
| band-structure | workflow | medium | `docs/band.md` (`phon-vib band`) + CLI entry |
| phonon-thermal-properties | compute | high | `cli.py` `thermal_properties` (F / S / Cv) |
| qha | workflow | **low** | `docs/qha.md` only — no `qha` module in source |

`docs/related.md` is a §E seed, not a capability. numpy/spglib are dependency fingerprints, not capabilities.

### 2.2 Paper projection (`layer: core`, `relation: companion-paper`)

| id | type | conf | evidence |
|---|---|---|---|
| qha-protocol | workflow | high | Methods: Helmholtz F on a volume grid, then minimize F(V,T) |
| thermal-expansion | compute | high | Methods: minimizing F(V,T) gives thermal expansion |
| harmonic-validity | concept | high | Validity: harmonic approximation must hold; imaginary modes invalidate QHA |
| mini-ref-package | tool | high | Software: implemented in the mini-ref package |

C3: repo-arm `qha` stays **low / unknown**; paper-arm `qha-protocol` is **high**. Not merged.

## 3. Host inventory

| id | type | provenance |
|---|---|---|
| heat-flow | skill | `skills/heat-flow/SKILL.md` — BTE lattice κ |
| eos | skill | `skills/eos/SKILL.md` — Birch-Murnaghan E(V) |
| parse-structure | tool | `tools/tool-registry.json` |
| fit-eos | tool | `tools/tool-registry.json` |

Host self-audit (`AUDIT.md`): admits no harmonic Cv / F / S / ZPE, no phonon DOS or dispersion, no force-constant / dynamical-matrix pathway.

## 4. Cross-validation of suspected gaps

Host-tree grep (capability terms) before classify:

- force-constants / dynamical-matrix: no FC or D(q) module or tool; AUDIT.md names the absence → confirmed missing, source host-self-audit
- phonon-dos / band-structure: no DOS or dispersion; AUDIT.md names both → confirmed missing, host-self-audit
- phonon-thermal-properties: host `heat-flow` produces lattice κ (BTE), not Cv/F/S/ZPE; AUDIT.md admits no heat capacity → adjacent-but-different, **missing** (strict subsume), host_id noted
- qha (repo): docs-only, no `qha` module → evidence low → **unknown**, not missing
- qha-protocol (paper): Methods statement is high; host has no QHA workflow (AUDIT does not name QHA) → missing, reference-contrast
- thermal-expansion (paper): host `eos` fits E(V), not α(T) from F(V,T) → adjacent-but-different, missing
- harmonic-validity: concept; host has no validity-condition skill → missing, recommend skip
- mini-ref-package: host does not wrap the companion CLI; overlaps repo-arm tools
- mini-thermal-kit (neighborhood): mentioning sentence is “BTE companion”; host `heat-flow` covers BTE lattice κ → equivalent on that lightweight capability
- mini-3ph (neighborhood): README mention + search-double title; **no neighbor-owned README/docs** → cannot drive missing → unknown

## 5. Gap table — core, repo projection

| ref_id | class | source_kind | host_id | evidence |
|---|---|---|---|---|
| force-constants | missing | host-self-audit | — | `cli.py` `force_constants`; AUDIT.md admits no FC pathway |
| dynamical-matrix | missing | host-self-audit | — | `cli.py` `dynamical_matrix`; AUDIT.md admits no D(q) pathway |
| phonon-dos | missing | host-self-audit | — | `cli.py` `dos` + `docs/band.md`; AUDIT.md admits no phonon DOS |
| band-structure | missing | host-self-audit | — | `docs/band.md` + `phon-vib band`; AUDIT.md admits no dispersion |
| phonon-thermal-properties | missing | host-self-audit | heat-flow | adjacent-but-different: BTE κ does not subsume Cv/F/S/ZPE; AUDIT.md admits no heat capacity |
| qha | unknown | reference-contrast | — | `docs/qha.md` only, no code; low evidence |

## 5b. Gap table — core, paper projection

| ref_id | class | source_kind | host_id | evidence |
|---|---|---|---|---|
| qha-protocol | missing | reference-contrast | — | Methods F(V,T) protocol; host has no QHA workflow |
| thermal-expansion | missing | reference-contrast | eos | eos fits E(V), not α(T) from F(V,T) |
| harmonic-validity | missing | reference-contrast | — | paper validity condition; no host counterpart |
| mini-ref-package | missing | reference-contrast | — | companion package; host has no wrapper (same placement family as repo-arm tools) |

Paper-arm rows are **not** copied into the repo-arm table.

## 6. Recommendations

Priority: host-self-audit (repo-arm) before reference-contrast (paper-arm).

- force-constants, dynamical-matrix, phonon-dos: **new tool**. Rule §1 (deterministic compute → tool/script), §2 (several consumers would share FC/D(q)/DOS), §3 (input contract differs from heat-flow / eos).
- band-structure: **new tool** (dispersion from D(q)). Rule §1, §3.
- phonon-thermal-properties: **new tool** for Cv/F/S/ZPE — do not extend heat-flow (different output contract). Rule §1, §3.
- qha (repo): no placement. Rule §5 (never recommend on all-low evidence).
- qha-protocol (paper): **new skill** (independent routing trigger: QHA workflow). Rule §1, §3.
- thermal-expansion: **new tool**; do not extend eos (E(V) ≠ α(T)). Rule §1, §3.
- harmonic-validity: **skip**. Rule §4 (never-mechanical scientific judgment; this skill does not decide scientific soundness).
- mini-ref-package: **new tool** wrapping the companion CLI — same family as the repo-arm tools above, not a second stack. Rule §1, §3.

## 7. Host-only

| id | note |
|---|---|
| parse-structure | tool; no reference counterpart |
| fit-eos | tool; no reference counterpart |
| eos | skill; no reference counterpart on the repo arm (paper-arm records it as a near-miss on thermal-expansion) |

`heat-flow` is not host-only: it is the adjacent host_id on phonon-thermal-properties and the match for neighborhood `mini-thermal-kit`.

## 8. Neighborhood

Search used: yes (necessary — `mini-3ph` named, no URL). Source: `tests/fixtures/mini-ref/neighborhood-search-double.json`. Live network: no.

**Kept**

| id | relation | conf | lightweight cap | class | host_id | evidence |
|---|---|---|---|---|---|---|
| mini-thermal-kit | sibling | medium | BTE companion | equivalent | heat-flow | `docs/related.md`; README see-also. Neighbor not cloned. |
| mini-3ph | sibling | medium (item) / low (snippet) | anharmonic solver | unknown | — | README named-unlinked; search-double same author Ada Fixture. No neighbor-owned docs → cannot `missing`. |

**Rejected**

| id | reason |
|---|---|
| top-10-phonon-codes-2024 | keyword-only listicle; no DOI / author / declared-related match |

Companion paper `qha-mini-ref-2015` is **core**, not listed here.

**Unresolved neighborhood seeds:** none (search double resolved `mini-3ph`).

## 9. Unresolved

- repo-arm `qha`: docs-claim-without-code; re-inventory if the reference ships a `qha` module
- neighborhood `mini-3ph`: neighbor-owned README/docs not fetched; class stays `unknown`
- homepage `https://example.invalid/mini-ref`: fixture host, fetch skipped; local `docs/` substituted

Recommendations are placement suggestions; building them is a decision for the host agent and its human. Unverified capabilities were never treated as missing.
