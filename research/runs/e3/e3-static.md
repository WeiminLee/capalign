# E3 study 1 — static cross-library drift check (assertion C, first pass)

Scope of this file: the **static** half of E3 study 1 — does promise-drift sort
by *source* (description vs body) and is the *level* predictable/explainable
across host libraries? Evidence: the MatDiscovery pilot
(`../drift-preliminary.md`, already measured) + a fresh static measurement of
the K-Dense public skill library (`kdense-drift.json`,
`kdense-drift-summary.md`). n = 2 libraries: a **sample of one contrast**, not
a distribution. Assertion C's "predictable from cheap surface features" part is
NOT tested here (that needs ≥ 3 libraries + held-out scoring).

## 1. Corpus and structure (new host: K-Dense)

Repo `https://github.com/k-dense-ai/scientific-agent-skills` (commit `a1043ef`,
shallow clone, read-only). Open Agent Skills standard library: 177 skills,
`skills/<name>/SKILL.md` + optional `references/` (176 skills), `scripts/` (121
skills, 518 scripts), `assets/` (43). Structural facts that matter for the
measurement:

1. **No MatDiscovery-style registry exists.** No `@mcp.tool()` defs, no runner
   tuple/constant file, no per-skill artifact manifest. Tool registration is
   implicit: a script exists in `scripts/` or it doesn't.
2. **Tests live at repo level, not per skill**: `tests/<name>/test_scripts.py`
   + fixtures — K-Dense's real witness-test infrastructure (the analog of our
   `confl ≥ medium ∧ witness test` tier, but we do NOT execute it here; see §2).
3. **Output artifacts are never shipped** in skill dirs (AGENTS.md: "A skill
   directory ships only what an agent loads … generated artifacts stay out") —
   so the meter's shipped-file fallback cannot verify output promises, exactly
   like MatDiscovery's agent-assembled outputs.
4. **Publishing discipline is enforced** (AGENTS.md + CI: `references/` almost
   mandatory, scripts need test suites) — this matters for the fabricated tier.

## 2. 口径 decision (and why)

Per the E3 instruction we faced the registry-rather question head-on and chose
**(c) run both, report both, with the crafted registry as an explicitly
temporary verification surface**.

- **(b) no-registry mode** is kept as the primary *comparable* tier: the
  **fabricated** class is registration-independent by definition (`drift` ∧ `E(c)
  = ∅` where `E` is the references/scripts evidence test) and the shipped-file
  verified tier is mechanical. Without it we could not speak across libraries at
  all.
- **(a) a lightweight crafted registry** was needed because no-registry mode
  systematically *undercounts* verified: with no registry, verified shrinks to
  "filename shipped in the skill dir", but K-Dense policy keeps outputs out of
  skill dirs — 103/178 claims (57.9%) would read as drift and the 100%-verified
  body layer of MatDiscovery would be unrepresentable. The crafted registry
  restores a verification surface: artifact filename literals scraped **from the
  skill's own `scripts/*.py`** — the K-Dense analog of MatDiscovery's
  fieldmat-runners scrape (`build-registry.py`). Every entry records its source
  script in `_provenance` (auditable), builder: `e3/build-kdense-registry.py`.

  The crafted registry is **not** a gold standard: it has literal-scrape blind
  spots (measured: 31 `f"{...}.csv/json"` dynamic-write sites in scripts; e.g.
  pybamm writes `tight-tolerance.csv`/`refined-mesh.csv` via `f"{{name}}.csv"`,
  which no literal scrape can resolve). Consequences are stated as bounds, not
  fudged away: drift=54 is an upper bound; the no-carrier-found floor is
  40/178 = 22.5%.

- **Honest limitation, stated not hidden**: without a registry the **verified**
  layer is unmeasurable, and we did not fake one from the repo's tests. K-Dense's
  `tests/` suite is the *strongest* verification carrier it has (executable
  witness tests), but we did not execute it and did not promote test presence to
  "verified" — we keep it as a separate *carrier* class (`in tests/<name>/`) so
  the paper can later decide whether tests ≥ witness. Also: drift-meter's claim
  grammar only extracts MatDiscovery-named **tools** (`mcp__*`/`fieldmat_*`/
  `mat_*`), so K-Dense's tool/package promises contribute **0 tool claims**; the
  verified comparison is artifact-tier + fabricated-tier only. This is a
  measurement-interface mismatch, recorded here so the paper does not read
  "K-Dense has no tools" into it.

## 3. Numbers

Full per-skill table and run inputs: `kdense-drift-summary.md`. Headline:

| metric | MatDiscovery (37 skills) | K-Dense (177 skills) |
|---|---|---|
| claims | 134 (tool+artifact) | 178 (artifact only; tools = 0 by grammar) |
| claims / skill | 3.62 | 1.01 (50/177 skills have ≥ 1 claim) |
| verified | 119 (88.8%) | 124 (69.7%) |
| **drift** | **15 (11.2%)** | **54 (30.3%)** |
| **fabricated** | **3 (2.2%)** | **0 (0.0%)** |
| drift by source | body 14/15; description 1/1 verified | body 54/54 (description = 0 claims) |
| verification surface | code-scraped 71 tools + 99 artifacts | crafted 121 artifacts (+shipped files) |

Verified attribution (K-Dense): 49 registry-only, 73 shipped-file-only, 2 both.
Drift decomposition (mechanical, reproducible): URL-cited 1 · literal in
`tests/<name>/` 13 · residual 40. Residual includes depmap's 17
portal-download-file names (the skill's stated job is retrieving them), 6
waypoint-bio training-run/HF-config names, 4 cantera sweep outputs, 2 pybamm
`f`-string outputs, 11 singles.

## 4. Assertion C, initial cross-library reading

**Source ordering (description vs body).** Both libraries show the same
ordering — drift concentrates in the **body**; the description layer is clean or
empty: MatDiscovery 1/1 verified (100%), K-Dense 0 claims by construction
(descriptions are trigger-phrase prose with no backticked artifact/tool names
under this grammar). Direction of the starting hypothesis
(`paper-methods > blog-recipes > repo-docs` per-source ordering) is consistent
with: repo-docs-style prose (both libraries' bodies) carry the drift; neither
library's description layer contributes measurable drift. Ordering holds;
**levels are not comparable** because K-Dense's description layer is
empty-by-grammar, not measured-clean — flagged, not claimed.

**Level explainability (drift 30.3% vs 11.2%).** The difference is *explained by
structure*, and that is the meaningful Assertion-C evidence at n=2:

1. **Claim-type composition differs.** MatDiscovery's claims are mostly
   host-owned artifact promises (`mcp__` tools + runner products); its 15 drift
   items are self-authored output files with no runner carrier. K-Dense's claims
   are dominated by *references to external data resources* the grammar counts
   as promises (DepMap portal files ×17, PrimeKG, Cantera's bundled `h2o2.yaml`,
   `gpt2-*.yaml` host configs, `/v1/openapi.json`) — no host registry can or
   should verify an external resource name. Doc-referencing libraries inflate
   naive drift; the drift is in the *measurement's claim grammar*, not the host.
2. **Verification-surface coverage differs.** MatDiscovery's runners are
   literal-laden → registry resolves them; K-Dense scripts build names
   dynamically (f-strings) → the crafted registry under-resolves. Measured
   rather than guessed (§2).
3. **The fabricated tier — the registry-independent one — tells the cleanest
   story: 0 (0.0%) vs 3 (2.2%).** K-Dense's CI/AGENTS.md discipline
   (references/ for nearly all skills, scripts mandatory-tested) eliminates the
   "no evidence at all" class *by construction*; MatDiscovery's fabricated items
   came from agent-assembled scenario skills with no evidence surface. This is a
   direct, comparable observation: **fabrication is controllable by
   library-level publication discipline**, evidence for the governance-loop
   claim (Assertion D/E direction) and for drift being a *structural*, not
   random, quantity.

**What we can and cannot say.** Can say: drift is not random noise in either
library — it decomposes into identifiable cause classes (un-carried output
promises in MatDiscovery; external-resource references + dynamic-name outputs +
test-unwitnessed artifacts in K-Dense), and the by-source ordering (body ≫
description) is stable across the two hosts. Cannot say: anything about *rates*
being predictable from cheap surface features — the interface (claim grammar +
verification surface) is host-bound, n=2 cannot estimate a distribution, and
neither run exercises held-out prediction.

## 5. Limitations (honest)

- **n = 2 libraries** — one contrast pair, not a distribution; any
  generalization (e.g. "marketplace libraries have drift ≈ 30%") is out of
  scope until a 3rd host (candidates: another skill marketplace e.g.
  skills marketplaces in `$CWD/benchmark`-adjacent repos, or
  `AntOmniEvo`/`AlloyEvo` skill trees with registries) is measured plus held-out
  feature prediction (AUROC per assertion C).
- **Host-bound claim grammar.** Tool tier empty for K-Dense; description tier
  empty-by-grammar for K-Dense. A host-agnostic claim extractor (generic
  backtick token classifier + external-reference detector) is prerequisite
  before the cross-library table can be fair — this is the same E1-style IRR
  work the pilot called for.
- **Crafted registry is temporary and imperfect**: literal-scrape over/under
  coverage (f-string gap measured: 31 write sites), no execution of K-Dense's
  `tests/`, no human-adjudicated gold on any skill. `fabricated` stays a lower
  bound (same rule as pilot).
- **depmap-vs-manual boundary** in the drift inventory is mechanical
  (URL/test-literal anchors) + a documented manual annotation, not IRR gold.
- K-Dense is assets-light in our terms (43/177 have assets/) and its skills are
  mostly single-script; MatDiscovery skills are richer (references/scripts).
  Claim-per-skill 1.01 vs 3.62 therefore also reflects skill granularity, not
  just grammar.

## 6. Next steps

1. Third host with a *native* registry (tool surface comparable to
   MatDiscovery) — makes the verified tier cross-comparable for the first time.
2. Host-agnostic claim grammar (generic token extraction + external-reference
   exclusion) + IRR sample on both libraries.
3. Feature prediction trial per assertion C once ≥ 3 libraries: evidence
   density, claim-type mix, references/scripts presence, update recency vs
   drift/fabricated — held-out, AUROC ≥ threshold.
4. Optionally: promote K-Dense `tests/<name>/` presence to a *carrier* class in
   the meter output (not to "verified") so the paper can test tests-as-witness
   assumptions without executing them.