# Inventory heuristics (reference & host)

Zero-bundle, instruction-level rules. The agent runs these with the host's own
shell / Python — nothing is pre-installed. Output of each pass is the capability
IR (see `capability-ir.md`).

---

## A. Repo inventory (`inventory_repo`)

1. **Entry surface** — run with the host shell, e.g.:
   ```bash
   ls <repo>; cat <repo>/pyproject.toml 2>/dev/null || cat <repo>/package.json 2>/dev/null
   grep -rn "^\[project.scripts\]\|console_scripts\|\[bin\]\|bin/" <repo> --include="*.toml" --include="*.json" -l 2>/dev/null
   find <repo> -maxdepth 2 -name "*.py" -path "*/src/*" | head; find <repo> -maxdepth 2 -type d -not -path "*/node_modules*" -not -path "*/.git*"
   ```
   Capability boundaries = package top-level modules + CLI entry points +
   documented user commands. **One CLI/tool per capability; nothing finer.**
2. **Dependency fingerprint** — read the manifest dependencies; map the
   domain-relevant ones to implied capability families (e.g., a phonon code →
   force-constants / dynamical-matrix / DOS / thermal-properties / QHA families;
   a DFT code → SCF / relax / band-structure / response families). Mark these
   `confidence: medium` unless confirmed in docs/code (`high`).
3. **Docs feature surface** — when `docs/` exists, list feature pages; each page
   that documents a user-facing capability adds one capability (evidence
   `doc: <path>`) unless it duplicates an entry surface item.
4. **Tests as sanity** — test file names reflect capability boundaries; use them
   only to confirm an inventory item exists, never to invent one.
5. **Exclude** — vendored deps, build artifacts, examples (unless they are the
   documented capability), CI config.

## B. Paper inventory (`inventory_paper`)

1. **Methods → Steps** — decompose the Methods section into steps; a step that
   computes something → `compute`; that orchestrates steps → `workflow`;
   that the authors say must be run (software, solver, dataset) → `tool`/`data`.
2. **Contribution claims** — each claim implies a capability: a new algorithm →
   `compute`; a protocol → `workflow`; an approximation/theory → `concept`.
3. **Products** — tables/figures/datasets named in Results are `data` capabilities
   only if they are reusable artifacts (a reference dataset, a benchmark
   protocol), not a single figure.
4. **Dependencies** — named software/versions are hard `tool` capabilities
   (evidence `method|results quote`).
5. **Confidence** — direct method statements = `high`; inferences from the
   abstract/intro = `medium`; from a single passing mention = `low` (flagged).

## C. Blog / writeup inventory (`inventory_blog`)

1. Extract claims and recipes; every capability needs a **quote** as evidence.
2. A named command / tool / package → `tool`; a step-by-step recipe → `workflow`;
   a factual benchmark number → `data`; an opinion or "X is better than Y"
   without procedure → `concept` at `confidence: low`.
3. **Do not** inflate: recommendations/advertising copy that names no procedure
   is `concept`/`low` at most, and often not a capability at all.

## D. Host-agent inventory (`inventory_host`)

1. **Auto-scan** (in order, until gaps close; all read-only):
   ```bash
   # skill dirs (common framework roots)
   find . -maxdepth 3 -type d \( -name ".agents" -o -name "skills" -o -name ".dsh" \) -not -path "*/node_modules*" 2>/dev/null
   find . -maxdepth 4 -name "SKILL.md" -not -path "*/node_modules*" 2>/dev/null
   # tool registries / named entry points
   ls tools/ 2>/dev/null; grep -rln "defineTool\|@mcp.tool\|name: '" --include="*.ts" --include="*.py" . 2>/dev/null | head -20
   ```
   For each found `SKILL.md`: frontmatter `name` + `description` (= the routing
   trigger) → capability of type `skill`, evidence `skill: <path>`.
   For each tool definition: the registered tool name + one-line purpose →
   capability of type `tool`, evidence `tool: <path>`, provenance recorded.
3. **Host self-audit scan (mandatory, drives source kind).** Look for a host-side
   audit/roadmap/known-gaps artifact (e.g. `AUDIT.md`, `docs/*-audit*`,
   `SKILLS-*.md`, issues/roadmap text): a capability the host itself admits lacking
   **must** be tagged `source_kind: host-self-audit` (highest priority) — the
   reference merely confirms what the host already owes. This is an inventory step,
   not an afterthought: run it before classification and let it override the
   default `reference-contrast` for every admitted gap. (E1 pilot F2: judge-1
   missed 4 AUDIT-admitted gaps and mis-tagged them reference-contrast; judge-2
   followed this rule.)
4. **Ask-fallback** — a gap that scanning cannot close (proprietary host,
   credentials-only surface, registry without source) is asked of the caller in
   plain text; the caller's reply is ingested as the authoritative host IR
   (`confidence: high`, evidence `caller-supplied`).
3. **Host-only marker** — every host capability records where it came from
   (skill dir / tool registry / scripts / caller), so placement recommendations
   can point at a concrete host location.