# Alignment report — oh-my-mlip vs MatDiscovery

## self_check:
- sections: pass (surfaces, reference inventory, host inventory, gap table, recommendations, host-only, neighborhood, unresolved)
- validated evidence: pass (every `missing` row cites oh-my-mlip paths and a MatDiscovery grep/skill path)
- no-low-driven-missing: pass (no all-low `missing`; companion paper absent rather than inferred)
- rule citations: pass (placement cites alignment-rules §1–§5 and host CAPABILITY-SURFACE.md §0.1)
- source kinds: pass
- host-only tracked: pass (phonon/QHA/BTE/… listed; not dropped)
- closing statement: pass (verbatim)
- determinism: pass (second pass on the same trees produced the same gap ids/classes)
- neighborhood stratified: pass (onthefly-distill and catbench stay in Neighborhood; MACE/SevenNet roster is not neighborhood; no companion paper invented)

## 1. Surfaces
- reference: `/Users/lwm/code/oh-my-mlip` (kind: repo) + official docs `https://oh-my-mlip.org/` (same work; caller supplied both)
- host: `/Users/lwm/code/MatDiscovery` (kind: host)
- generated_at: 2026-10-16
- companion_paper: **not recovered**. `CITATION.cff` is `type: software` with no `preferred-citation` / DOI. One identity-gated search for "oh-my-mlip Jinuk Moon paper" returned unrelated MLIP papers (different authors); all rejected.
- search: not required for homepage (caller + CITATION `url` already had it). Optional paper query used, 0 kept.
- doctrine: **MatDiscovery** `docs/CAPABILITY-SURFACE.md` §0.1 overrides generic placement on conflict.
- host scan bound: `plugins/matdiscovery/skills/` (37 skills) as declared by CAPABILITY-SURFACE / check-skills. Excluded `.claude/worktrees`, `node_modules`, `dsh/.agents` copies (naive `find SKILL.md` would have counted 174 files).

## 2. Reference inventory

### 2.1 Repo + official-docs projection (`layer: core`)

User-reachable verbs from README / docs/howto / `skills/*/SKILL.md` / `oh_my_mlip` API, merged (skill pack ≡ documented howto, not a second roster).

| id | type | conf | evidence |
|---|---|---|---|
| mlip-registry | interface | high | `models.json`; `oh_my_mlip.list_models` / `resolve`; docs/model_status.md. 20 frameworks / 32 variants are **roster of this one capability**, not 20 capabilities. |
| per-env-install | workflow | high | `install.sh`; `skills/setup/SKILL.md`; `scripts/setup_verify.py` (energy+forces on GPU is the oracle) |
| mlip-single-point | compute | high | `oh_my_mlip.run` / `get_calculator`; `skills/run/SKILL.md`; docs/howto/use-a-model.md |
| mlip-relax | compute | high | `skills/run` `--relax`; docs/howto/use-a-model.md |
| calculator-codegen | interface | high | `resolve()` returns interpreter + import + inference lines; docs/reference/api.md |
| catbench-adsorption | workflow | high | `skills/catbench/SKILL.md`; docs/howto/catbench.md; `scripts/catbench_*.py` |
| vasp-to-catbench | workflow | high | docs/howto/vasp-to-catbench.md |
| mlip-finetune | workflow | high | `skills/finetune/SKILL.md`; `scripts/ft_run.py`; docs/howto/finetune.md |
| mlip-distill-nnmtp | workflow | high | `skills/distill/SKILL.md`; docs/howto/distill.md (orchestrates sibling onthefly-distill) |
| gated-hf-weights | tool | medium | docs/gated_models.md; UMA/eSEN need Hugging Face login |
| lockfile-replay | workflow | medium | `envs/locks/`; `OMM_USE_LOCK=1 ./install.sh` |
| mcp-job-server | interface | medium | `oh_my_mlip/mcp_server.py` |

`docs/model_licenses.md` and per-framework recipe pages are evidence for `mlip-registry` / `per-env-install`, not extra capabilities.

### 2.2 Paper projection
Empty. Software citation only.

## 3. Host inventory (MatDiscovery, scoped)

Skill root `plugins/matdiscovery/skills/` (doctrine). Tools under `tools/` (alame, bte-controller, fieldmat-mcp-server, mat-local-compute, structure-modeling, …). GPU energy/relax path is **remote FieldMat / MatterSim**, not a local multi-MLIP hub.

| id | type | provenance |
|---|---|---|
| mat-singlepoint-energy | skill | FieldMat force-field single-point (energy, forces, stress) |
| mat-relax-analysis | skill | FieldMat relaxation |
| mat-active-learning | skill | ALAME loop: MD sample → VASP label → FieldMat finetune (Ti prior-bank) |
| mat-vasp-calculation | skill | platform VASP service |
| mat-nve-md / nvt-heating / npt-compression | skill | FieldMat MD |
| mat-phonon, mat-qha-thermal-expansion, mat-lattice-thermal-conductivity, … | skill | phonon / QHA / BTE family |
| fieldmat-mcp-server | tool | transport to FieldMat |
| mat-local-compute | tool | local structure/energy checks |

Self-audit (`docs/SKILLS-AUDIT-2026-09-24.md`): contract drift, QHA α(T) under-delivery, force-equivariance plan-only. **Does not admit** a missing multi-MLIP hub — MLIP-registry gaps are `reference-contrast`.

## 4. Cross-validation

Host grep (`plugins/matdiscovery/skills`, `docs/CAPABILITY-SURFACE.md`, `tools/`):

- `oh_my_mlip` / `list_models` / `install.sh` / `models.json`: no hits in the skill/tool surface → registry + per-env-install confirmed missing
- MatterSim / FieldMat: host **does** run energy and relax, but on one remote force field, not on an arbitrary registry model → single-point / relax are **adjacent-but-different**, class `missing` with host_id noted (strict subsume: FieldMat ⊄ "any of 20 MLIPs")
- `mat-active-learning` is ALAME/FieldMat finetune, not `ft_run.py` driving each framework's trainer → adjacent-but-different, missing
- `mat-vasp-calculation` is DFT, not CatBench dataset conversion → catbench / vasp-to-catbench missing
- catbench / onthefly-distill / NN-MTP / LAMMPS pair_nnmtp: no skill/tool → missing
- `fieldmat-mcp-server` is a different MCP (FieldMat tasks), not `oh_my_mlip.mcp_server` → missing with near-miss note

Naive host scan (maxdepth-4 `SKILL.md`) hit **174** files including `.claude/worktrees`. Using doctrine skill root: **37**. The unbounded scan is a method bug; this run used the bound.

## 5. Gap table — core, repo/docs projection

| ref_id | class | source_kind | host_id | evidence |
|---|---|---|---|---|
| mlip-registry | missing | reference-contrast | — | `models.json` + `list_models`; host has no multi-framework roster |
| per-env-install | missing | reference-contrast | — | `install.sh` + `setup_verify.py`; host does not build per-framework conda envs |
| mlip-single-point | missing | reference-contrast | mat-singlepoint-energy | FieldMat/MatterSim single-point does not subsume `oh_my_mlip.run(model=…)` |
| mlip-relax | missing | reference-contrast | mat-relax-analysis | FieldMat relax ≠ relax-with-chosen-registry-model |
| calculator-codegen | missing | reference-contrast | — | no `resolve()` codegen |
| catbench-adsorption | missing | reference-contrast | — | no CatBench pipeline (benchmark case JSON strings are not the tool) |
| vasp-to-catbench | missing | reference-contrast | mat-vasp-calculation | VASP skill exists; CatBench dataset conversion does not |
| mlip-finetune | missing | reference-contrast | mat-active-learning | ALAME ≠ per-framework `ft_run.py` |
| mlip-distill-nnmtp | missing | reference-contrast | — | no NN-MTP / LAMMPS student path |
| gated-hf-weights | missing | reference-contrast | — | no UMA/eSEN HF gating flow |
| lockfile-replay | missing | reference-contrast | — | no `envs/locks` replay |
| mcp-job-server | missing | reference-contrast | fieldmat-mcp-server | different MCP contract |

## 5b. Gap table — paper projection
Empty (no companion paper).

## 6. Recommendations

Priority: host-self-audit items in SKILLS-AUDIT (QHA α(T), force-equivariance) are **out of this W** — they stay on the host's own backlog. For this W, all gaps are reference-contrast.

Host doctrine §0.1: independent routing trigger → **new skill**; deterministic compute consumed by several skills → **tool**. Do **not** mint one skill per MLIP framework.

1. **mat-mlip-hub** (new skill) wrapping an oh-my-mlip clone: roster, install, single-point, relax, `resolve()` codegen. Rule §1 (skill = way to do MLIP work), §3 (new routing: "install MACE / run UMA"). Install/verify stay scripts of that skill or a small tool; do not become 20 tools.
2. **catbench-adsorption** (new skill) + keep CatBench inside the hub envs. Rule §1, §3 (independent trigger: adsorption leaderboard). Do not extend `mat-vasp-calculation`.
3. **vasp-to-catbench**: extend the catbench skill (`references/`), not a third skill. Rule §3 (same toolbox, adjacent).
4. **mlip-finetune** (new skill). Do not extend `mat-active-learning` (different trainer, different input contract). Rule §3.
5. **mlip-distill-nnmtp**: **new skill** that *calls* onthefly-distill (GPL-2.0 sibling; do not vendor). Rule §1, §3. License is a product decision — report, do not decide.
6. gated-hf-weights / lockfile-replay: pages under the hub skill `references/`, not new skills. Rule §3.
7. mcp-job-server: **skip** unless the host wants a second MCP; FieldMat MCP already occupies the transport axis. Rule §1 (plugin/server axis already filled).

## 7. Host-only (informational)

Phonon / QHA / BTE / EOS / melting / convex-hull / NEB / structure-modeling / alloy-design — MatDiscovery property surface with no oh-my-mlip counterpart. FieldMat MD ensembles likewise. Not gaps in W.

## 8. Neighborhood

**Kept** (identity-gated; roster frameworks MACE/SevenNet/… **rejected** as neighborhood)

| id | relation | class | host_id | evidence |
|---|---|---|---|---|
| onthefly-distill | sibling | missing | — | README + docs/howto/distill.md; neighbor README fetched (NN-MTP AL loop, LAMMPS `pair_nnmtp`). Host has no counterpart. |
| catbench | sibling | missing | — | `https://github.com/JinukMoon/catbench`; ships in every oh-my-mlip env; same author. Core already has `catbench-adsorption`; this row is the standalone package. |

**Rejected**

| id | reason |
|---|---|
| MACE, SevenNet, NequIP, … (20 frameworks) | registry payload, not related works of W |
| arXiv 2610.09644 MLIP knowledge graph | keyword collision; authors ≠ Moon |
| instadeepai/mlip, CV papers titled MLIP | keyword collision |

Companion paper is core-absent, not a neighborhood miss.

## 9. Unresolved
- Companion paper: none published under this CITATION; do not invent one
- CatBench standalone repo not cloned; neighborhood inventory is README/docs of oh-my-mlip plus GitHub name
- Host FieldMat MatterSim version vs oh-my-mlip MatterSim-v1-5M: not verified (would need a live runner); left as the adjacent note on single-point/relax
- Naive 174-skill scan discarded; if doctrine files were absent the run would have been invalid — that is now a hard scoping rule

Recommendations are placement suggestions; building them is a decision for the host agent and its human. Unverified capabilities were never treated as missing.
