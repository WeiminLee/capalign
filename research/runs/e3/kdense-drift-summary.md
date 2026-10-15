# K-Dense drift measurement — E3 study 1 static part

Run date: 2026-10-15 · corpus: https://github.com/k-dense-ai/scientific-agent-skills
(commit `a1043ef`, shallow clone, read-only) · tool: `research/tools/drift-meter.py` (unmodified)
· crafted registry: `e3/kdense-registry.json` (builder `e3/build-kdense-registry.py`).

Reproduce:

```bash
python3 e3/build-kdense-registry.py /tmp/kdense --out e3/kdense-registry.json          # 121 artifact names from 55 scripts
python3 ../tools/drift-meter.py /tmp/kdense/skills --out e3/kdense-drift-noregistry.json --table   # fabricated-tier baseline
python3 ../tools/drift-meter.py /tmp/kdense/skills --registry e3/kdense-registry.json --out e3/kdense-drift.json --table  # full run
```

## Scope decision (口径)

K-Dense has **no MatDiscovery-style registry** (no `@mcp.tool()` defs / runner-tuple constants).
Its verification surface is structural: `scripts/*.py` products, shipped files under the skill dir,
plus the repo-level witness-test suite `tests/<skill-name>/`. Per the E3 instruction we ran **both**
modes and report them side by side:

- **no-registry run** — measures the *fabricated* tier (registry-independent) + the shipped-file-only
  verified tier. This is the only tier statistically comparable across libraries.
- **crafted-registry run** — a temporary verification surface (NOT a gold standard): artifact filename
  literals scraped from each skill's own `scripts/*.py` (the K-Dense analog of MatDiscovery's
  fieldmat-runners registry), each entry carrying its source script in `_provenance`.
- **Tool tier is structurally empty**: drift-meter's claim grammar only extracts MatDiscovery-named
  tools (`mcp__*` / `fieldmat_*` / `mat_*`). K-Dense claims packages/CLIs/scripts instead, so K-Dense
  contributes **0 tool claims** — the cross-library comparison is therefore artifact-tier +
  fabricated-tier only. This is a measurement-interface caveat, not a statement about K-Dense's tools.

## Aggregate

| metric | no-registry run | crafted-registry run |
|---|---|---|
| skills | 177 | 177 |
| claims (dedup per skill) | 178 | 178 |
| description-layer claims | 0 | 0 |
| body-layer claims | 178 | 178 |
| verified | 75 (shipped-file only) | **124 (69.7%)** |
| **drift (declared, no verified carrier)** | 103 (57.9%) | **54 (30.3%)** |
| **fabricated (no evidence at all)** | **0 (0.0%)** | **0 (0.0%)** |

- Claim distribution is heavy-tailed: 50/177 skills have ≥ 1 claim (max: depmap 18, clinical-reports
  15); 127 skills yield 0 claims under this grammar (their promises are prose/package names the
  artifact+tool grammar cannot see — the same interface reason the tool tier is empty).
- Only one skill (`bgpt-paper-search`) lacks `references/` or `scripts/`; it has no claims, so the
  fabricated tier is 0 for every measured claim.

## Verified attribution (registry run, 124 verified)

| verified via | count |
|---|---|
| scripts-product registry only | 49 |
| shipped file in skill dir only | 73 |
| both | 2 |

Registry coverage: 121 artifact names from 55 scripts (of 518 repo scripts). The registry converts
49 claims from drift→verified over the no-registry baseline (e.g. `report.json` /
`phase-equilibria.csv`, which pycalphad's `equilibrate.py` literally writes).

## Drift inventory (54 items; all in the body layer)

Mechanical subclassification (rules in e3-static.md §口径):

| class | count | items |
|---|---|---|
| URL-cited (same line as http/download/fetch) | 1 | genomic-intelligence `/v1/openapi.json` |
| carrier literal in `tests/<name>/` | 13 | e.g. bulk-rnaseq `metadata.csv`, cantera `baseline.csv`, liteparse `paper.pdf.json`, nwb-conversion `.validation.json`, relsa `relsa_scores.csv`, timesfm `.metadata.json`, tellurium `baseline.csv`, pybamm `curve.csv` … |
| residual (no URL line, no test literal) | 40 | depmap portal files (17), waypoint-bio (6), cantera `finer/tighter/longer_horizon` outputs (4), pybamm `tight-tolerance.csv`/`refined-mesh.csv` (2), plus 11 single items |

Residual detail — 40 items, by skill: depmap 17 · waypoint-bio 6 · cantera 4 · pybamm 2 ·
bids/cellprofiler/deepspot-m/lab-hardware-cad/liteparse/mageck/nextflow/paperclip/pi-agent/primekg/
scientific-schematics 1 each. Manual annotation (indicative, not IRR gold): the depmap 17 are
**DepMap portal download-file names** (the skill's stated purpose is retrieving them; docs say "Use
DepMap Downloads … download current data"); waypoint-bio's 2 `gpt2-*.yaml` are host-package shipped
configs; primekg's `kg*.csv` are downloaded PrimeKG graph files; cantera's `h2o2.yaml` is "Cantera's
bundled" mechanism — i.e. most residual items are **references to external data resources the grammar
counts as claims**, not fabricated host promises.

Registry blind spot, measured: 31 `f"Ellipsis.csv/json"` f-string write sites across scripts (e.g.
pybamm writes `curve.csv`/`tight-tolerance.csv`/`refined-mesh.csv` via `f"{name}.csv"` `name ∈
{'curve','tight-tolerance','refined-mesh'}`) — literal scraping cannot resolve dynamic names, so the
crafted registry under-verifies. drift=54 is therefore an **upper bound** on genuine unverifiable
promises; the no-carrier-found floor is 40/178 = 22.5%.

## Per-skill table (177 skills; claims/verified/drift/fabricated/evidence)

| skill | claims | verified | drift | fab | evid. |
|---|---|---|---|---|---|
| 13c-metabolic-flux | 1 | 1 | 0 | 0 | yes |
| adaptyv | 0 | 0 | 0 | 0 | yes |
| aeon | 0 | 0 | 0 | 0 | yes |
| alphagenome | 0 | 0 | 0 | 0 | yes |
| analytical-method-validation | 0 | 0 | 0 | 0 | yes |
| anndata | 0 | 0 | 0 | 0 | yes |
| arbor | 0 | 0 | 0 | 0 | yes |
| arboreto | 0 | 0 | 0 | 0 | yes |
| astropy | 0 | 0 | 0 | 0 | yes |
| autoskill | 2 | 2 | 0 | 0 | yes |
| benchling-integration | 0 | 0 | 0 | 0 | yes |
| bgpt-paper-search | 0 | 0 | 0 | 0 | no |
| bids | 2 | 0 | 2 | 0 | yes |
| biopython | 0 | 0 | 0 | 0 | yes |
| bioservices | 0 | 0 | 0 | 0 | yes |
| bulk-rnaseq | 4 | 3 | 1 | 0 | yes |
| cantera | 7 | 2 | 5 | 0 | yes |
| cellprofiler | 5 | 4 | 1 | 0 | yes |
| cellxgene-census | 0 | 0 | 0 | 0 | yes |
| cirq | 0 | 0 | 0 | 0 | yes |
| citation-management | 0 | 0 | 0 | 0 | yes |
| clinical-decision-support | 7 | 7 | 0 | 0 | yes |
| clinical-reports | 15 | 15 | 0 | 0 | yes |
| cobrapy | 0 | 0 | 0 | 0 | yes |
| consciousness-council | 0 | 0 | 0 | 0 | yes |
| dask | 0 | 0 | 0 | 0 | yes |
| database-lookup | 0 | 0 | 0 | 0 | yes |
| datalad | 0 | 0 | 0 | 0 | yes |
| datamol | 0 | 0 | 0 | 0 | yes |
| deepchem | 0 | 0 | 0 | 0 | yes |
| deepspot-m | 1 | 0 | 1 | 0 | yes |
| deeptools | 0 | 0 | 0 | 0 | yes |
| depmap | 18 | 0 | 18 | 0 | yes |
| dhdna-profiler | 0 | 0 | 0 | 0 | yes |
| diffdock | 0 | 0 | 0 | 0 | yes |
| dnanexus-integration | 1 | 0 | 1 | 0 | yes |
| esm | 0 | 0 | 0 | 0 | yes |
| etetoolkit | 0 | 0 | 0 | 0 | yes |
| exa-search | 0 | 0 | 0 | 0 | yes |
| experimental-design | 0 | 0 | 0 | 0 | yes |
| exploratory-data-analysis | 0 | 0 | 0 | 0 | yes |
| fictiv | 0 | 0 | 0 | 0 | yes |
| flowio | 0 | 0 | 0 | 0 | yes |
| flowkit | 2 | 2 | 0 | 0 | yes |
| fluidsim | 0 | 0 | 0 | 0 | yes |
| folklore-variant-evidence | 0 | 0 | 0 | 0 | yes |
| generate-image | 0 | 0 | 0 | 0 | yes |
| geniml | 1 | 1 | 0 | 0 | yes |
| genomic-coordinates | 0 | 0 | 0 | 0 | yes |
| genomic-intelligence | 1 | 0 | 1 | 0 | yes |
| geomaster | 0 | 0 | 0 | 0 | yes |
| geopandas | 0 | 0 | 0 | 0 | yes |
| get-available-resources | 0 | 0 | 0 | 0 | yes |
| gget | 0 | 0 | 0 | 0 | yes |
| ginkgo-cloud-lab | 0 | 0 | 0 | 0 | yes |
| glycoengineering | 0 | 0 | 0 | 0 | yes |
| gtars | 0 | 0 | 0 | 0 | yes |
| histolab | 0 | 0 | 0 | 0 | yes |
| hugging-science | 0 | 0 | 0 | 0 | yes |
| hypogenic | 1 | 1 | 0 | 0 | yes |
| hypothesis-generation | 7 | 7 | 0 | 0 | yes |
| imaging-data-commons | 0 | 0 | 0 | 0 | yes |
| infographics | 0 | 0 | 0 | 0 | yes |
| iso-standards-readiness | 9 | 9 | 0 | 0 | yes |
| lab-hardware-cad | 1 | 0 | 1 | 0 | yes |
| labarchive-integration | 0 | 0 | 0 | 0 | yes |
| lamindb | 0 | 0 | 0 | 0 | yes |
| latchbio-integration | 0 | 0 | 0 | 0 | yes |
| latex-posters | 0 | 0 | 0 | 0 | yes |
| liteparse | 2 | 0 | 2 | 0 | yes |
| literature-review | 0 | 0 | 0 | 0 | yes |
| mageck | 1 | 0 | 1 | 0 | yes |
| marine-carbonate-chemistry | 3 | 2 | 1 | 0 | yes |
| markdown-mermaid-writing | 0 | 0 | 0 | 0 | yes |
| market-research-reports | 1 | 1 | 0 | 0 | yes |
| markitdown | 0 | 0 | 0 | 0 | yes |
| matchms | 0 | 0 | 0 | 0 | yes |
| matlab | 0 | 0 | 0 | 0 | yes |
| matplotlib | 0 | 0 | 0 | 0 | yes |
| medchem | 0 | 0 | 0 | 0 | yes |
| modal | 0 | 0 | 0 | 0 | yes |
| molecular-dynamics | 0 | 0 | 0 | 0 | yes |
| molfeat | 0 | 0 | 0 | 0 | yes |
| ncats-arax | 2 | 2 | 0 | 0 | yes |
| networkx | 0 | 0 | 0 | 0 | yes |
| neurokit2 | 0 | 0 | 0 | 0 | yes |
| neuropixels-analysis | 0 | 0 | 0 | 0 | yes |
| nextflow | 1 | 0 | 1 | 0 | yes |
| nmrglue | 3 | 3 | 0 | 0 | yes |
| nwb-conversion | 1 | 0 | 1 | 0 | yes |
| omero-integration | 0 | 0 | 0 | 0 | yes |
| onekgpd | 0 | 0 | 0 | 0 | yes |
| ontology-term-resolution | 0 | 0 | 0 | 0 | yes |
| open-notebook | 1 | 1 | 0 | 0 | yes |
| openpiv | 0 | 0 | 0 | 0 | yes |
| opentrons-integration | 0 | 0 | 0 | 0 | yes |
| optimize-for-gpu | 0 | 0 | 0 | 0 | yes |
| pacsomatic | 0 | 0 | 0 | 0 | yes |
| paper-lookup | 0 | 0 | 0 | 0 | yes |
| paperclip | 1 | 0 | 1 | 0 | yes |
| paperzilla | 0 | 0 | 0 | 0 | yes |
| parallel-web | 0 | 0 | 0 | 0 | yes |
| pathml | 0 | 0 | 0 | 0 | yes |
| pathogen-variant-surveillance | 0 | 0 | 0 | 0 | yes |
| pathway-enrichment | 0 | 0 | 0 | 0 | yes |
| peer-review | 5 | 5 | 0 | 0 | yes |
| pennylane | 0 | 0 | 0 | 0 | yes |
| phylogenetics | 0 | 0 | 0 | 0 | yes |
| pi-agent | 1 | 0 | 1 | 0 | yes |
| pkpd-modeling | 0 | 0 | 0 | 0 | yes |
| polars | 0 | 0 | 0 | 0 | yes |
| polars-bio | 0 | 0 | 0 | 0 | yes |
| pptx-posters | 1 | 1 | 0 | 0 | yes |
| primekg | 3 | 1 | 2 | 0 | yes |
| primer-design | 0 | 0 | 0 | 0 | yes |
| protocolsio-integration | 1 | 1 | 0 | 0 | yes |
| pufferlib | 0 | 0 | 0 | 0 | yes |
| pybamm | 6 | 3 | 3 | 0 | yes |
| pycalphad | 2 | 2 | 0 | 0 | yes |
| pydeseq2 | 5 | 5 | 0 | 0 | yes |
| pydicom | 0 | 0 | 0 | 0 | yes |
| pyhealth | 0 | 0 | 0 | 0 | yes |
| pylabrobot | 1 | 1 | 0 | 0 | yes |
| pymatgen | 0 | 0 | 0 | 0 | yes |
| pymc | 0 | 0 | 0 | 0 | yes |
| pymoo | 0 | 0 | 0 | 0 | yes |
| pyopenms | 0 | 0 | 0 | 0 | yes |
| pysam | 0 | 0 | 0 | 0 | yes |
| pytdc | 0 | 0 | 0 | 0 | yes |
| pytorch-lightning | 0 | 0 | 0 | 0 | yes |
| pyzotero | 0 | 0 | 0 | 0 | yes |
| qiime2-amplicon | 3 | 3 | 0 | 0 | yes |
| qiskit | 0 | 0 | 0 | 0 | yes |
| qutip | 0 | 0 | 0 | 0 | yes |
| rdkit | 0 | 0 | 0 | 0 | yes |
| relion | 0 | 0 | 0 | 0 | yes |
| relsa-severity-assessment | 2 | 1 | 1 | 0 | yes |
| research-grants | 0 | 0 | 0 | 0 | yes |
| research-lookup | 8 | 8 | 0 | 0 | yes |
| rowan | 0 | 0 | 0 | 0 | yes |
| scanpy | 3 | 3 | 0 | 0 | yes |
| scholar-evaluation | 5 | 5 | 0 | 0 | yes |
| scientific-brainstorming | 0 | 0 | 0 | 0 | yes |
| scientific-critical-thinking | 0 | 0 | 0 | 0 | yes |
| scientific-schematics | 1 | 0 | 1 | 0 | yes |
| scientific-slides | 0 | 0 | 0 | 0 | yes |
| scientific-visualization | 1 | 1 | 0 | 0 | yes |
| scientific-writing | 10 | 10 | 0 | 0 | yes |
| scikit-bio | 0 | 0 | 0 | 0 | yes |
| scikit-learn | 0 | 0 | 0 | 0 | yes |
| scikit-survival | 0 | 0 | 0 | 0 | yes |
| scvelo | 0 | 0 | 0 | 0 | yes |
| scvi-tools | 0 | 0 | 0 | 0 | yes |
| seaborn | 0 | 0 | 0 | 0 | yes |
| shap | 4 | 4 | 0 | 0 | yes |
| simpy | 0 | 0 | 0 | 0 | yes |
| stable-baselines3 | 0 | 0 | 0 | 0 | yes |
| statistical-analysis | 0 | 0 | 0 | 0 | yes |
| statistical-power | 0 | 0 | 0 | 0 | yes |
| statsmodels | 0 | 0 | 0 | 0 | yes |
| sympy | 0 | 0 | 0 | 0 | yes |
| tamarind | 0 | 0 | 0 | 0 | yes |
| tellurium | 2 | 1 | 1 | 0 | yes |
| tiledbvcf | 0 | 0 | 0 | 0 | yes |
| timesfm-forecasting | 1 | 0 | 1 | 0 | yes |
| torch-geometric | 0 | 0 | 0 | 0 | yes |
| torchdrug | 0 | 0 | 0 | 0 | yes |
| transformers | 0 | 0 | 0 | 0 | yes |
| treatment-plans | 6 | 6 | 0 | 0 | yes |
| umap-learn | 0 | 0 | 0 | 0 | yes |
| uncertainty-and-units | 0 | 0 | 0 | 0 | yes |
| usfiscaldata | 0 | 0 | 0 | 0 | yes |
| vaex | 0 | 0 | 0 | 0 | yes |
| venue-templates | 0 | 0 | 0 | 0 | yes |
| waypoint-bio | 6 | 0 | 6 | 0 | yes |
| what-if-oracle | 0 | 0 | 0 | 0 | yes |
| zarr-python | 0 | 0 | 0 | 0 | yes |

## Cross-library comparison (MatDiscovery pilot from `drift-preliminary.md`)

| metric | MatDiscovery (37 skills) | K-Dense (177 skills) |
|---|---|---|
| claims (tool+artifact) | 134 | 178 |
| claims / skill | 3.62 | 1.01 |
| verified | 119 (88.8%) | 124 (69.7%) |
| **drift** | **15 (11.2%)** | **54 (30.3%)** |
| **fabricated** | **3 (2.2%)** | **0 (0.0%)** |
| description-layer verified | 100% (1/1) | n/a (0 claims) |
| body-layer verified | 88.8% | 69.7% |
| registry surface | code-scraped: 71 tools + 99 artifacts (runner products) | crafted (temporary): 121 artifacts, tools n/a |
| tool-tier claims in drift count | yes (all verified) | 0 claims by grammar |
| drift composition | agent/tool-written output artifacts with no runner carrier (15/15) | external-resource references + dynamic-name outputs + test-unwitnessed artifacts |

**Reading the comparison is only valid artifact-tier + fabricated-tier** (see caveats); on that
footing: K-Dense's fabricated tier is zero *by construction* (its AGENTS.md mandates
references/ for every skill and repo-level tests for scripts), while MatDiscovery's 3 fabricated
items came from agent-assembled skills with no evidence surface. Drift rate differs 30.3% vs 11.2%
but is not a like-for-like rate: K-Dense's claim set is dominated by doc-referenced external data
names that no host registry can (or should) verify, and its verification surface misses dynamic
output naming.

## Caveats

- Crafted registry is a *temporary verification surface* with literal-scrape blind spots (f-strings,
  variable-built names, `Path/join` chains) — over- and under-coverage both possible; provenance per
  entry is recorded for audit.
- Claim grammar is MatDiscovery-bound; K-Dense tool/package claims are invisible ⇒ claim counts and
  rates are not directly cross-comparable; only the fabricated tier and the artifact tier are.
- Two-library comparison is a sample of one, not a distribution (see e3-static.md).
- `fabricated` uses "skill has references/ or scripts/ or links" as the evidence test (identical rule
  to the MatDiscovery pilot) — a lower bound on fabrication.
