# Promise drift — preliminary measurement (MatDiscovery, 37 skills)

First run of the drift meter (assertion C seed). Honest numbers with the v0
measurement caveats spelled out — this is a pilot, not the paper's table.

## Method (drift-meter v0)

- Corpus: MatDiscovery `plugins/matdiscovery/skills` (37 SKILL.md).
- Claims: backticked tool names (`mcp__*` / `fieldmat_*` / `mat_*_*`) and artifact
  filenames (`.json/.csv/.vasp/.traj/.log/.yaml/.xyz`) in description + body,
  negated sentences excluded (do not / never / no registered tool / not produced…).
- Verification surface (registry, from `build-registry.py` over the MatDiscovery
  code tree): 71 tool names (`@mcp.tool()` defs, TS `name:` literals, fieldmat/mcp
  literals) + 99 artifact filenames (fieldmat-runners literals) + **files present
  in the skill's own directory** (examples/ etc.).
- Classes: verified = claim resolves in the registry or locally; drift = declared
  but unverified; fabricated = drift with no evidence directory/link at all.

## Result

| metric | value |
|---|---|
| skills | 37 |
| claims | 134 |
| verified | 119 |
| **drift (declared, unverified)** | **15 (11.2%)** |
| **fabricated (no evidence at all)** | **3 (2.2%)** |
| description-layer claims verified | 100% (1/1) |
| body-layer claims verified | 88.8% |

## Drift inventory (all 8 skills; every item is an **agent-assembled or tool-written
artifact with no runner/registry carrier**)

| skill | drift | items |
|---|---|---|
| alloy-design-scenario | 3 | ranked.json, run.json, final_ranked.json (fabricated; no references/scripts) |
| mat-soft-mode / mat-soft-mode-scan | 2+2 | mode_vector.json, selected_soft_mode.json, soft_mode_summary.json |
| mat-dynamic-stability | 2 | dynamic_stability_2d_summary.json, report.json |
| mat-md-trajectory-descriptor | 3 | trajectory_descriptor_summary.json, trajectory_manifest.json, analysis/md_quality.json |
| mat-melting-point | 1 | melting_point_summary.json |
| mat-qha-thermal-expansion | 1 | thermal_expansion.json (local tool output, not a runner product) |
| mat-relax-analysis | 1 | structure_summary.json (host TS persistence hook, not in runner registry) |

## Reading (what the pilot already shows)

1. **The drift is not random — it has one cause class.** 15/15 items are
   agent-assembled or host-tool-written artifacts. The *verification carrier* for
   these (a runner spec or a host-side artifact registry) does not exist in
   MatDiscovery, exactly as SKILLS-AUDIT described qualitatively; this is that
   debt, measured. Fabricated tier is 3 (2.2%) — alloy scenario's self-authored
   files with no evidence at all.
2. **Description layer is clean (100%).** Routing triggers are not the drift
   source; body-produced artifact promises are. Drift-by-source decomposition
   (assertion C) already separates.
3. Cross-check vs. known baselines: the 4 `bte_controller` tool mentions are now
   verified (registry gains them in v1); the earlier observe-mode
   check-skill-artifacts misses (89) overlap this drift set but are a different
   unit (runner-tuple membership vs claim resolution) — noted for the paper.

## Caveats (v0, must not be over-read)

- Registry is code-scraped; a host-side artifact registry (TS constants like
  FORMATION_ENERGY_FILENAME) is **not** yet in the verification surface — 2 of the
  15 items (structure_summary.json, thermal_expansion.json) are known to have an
  actual producer outside the runner; including the host surface is v1.
- Negation exclusion is lexical; the paper's measurement must add human-adjudicated
  gold on a sample to bound extraction error itself (E1-style IRR for the meter).
- `fabricated` uses "skill has references/ or scripts/" as the evidence test; it is
  a lower bound on fabrication.

## Next (E3 path)

- v1 registry: add host-side artifact constants + TS persistence hooks.
- Extend corpus: public skill libraries (K-Dense scientific-agent-skills, skill
  marketplaces) — drift distribution across libraries is the E3 table.
- Predictors (assertion C): evidence density, description length, update recency,
  skill tier (atomic/expert/scenario), claims count → AUROC on held-out skills.