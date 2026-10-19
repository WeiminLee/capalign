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
   documented user commands + **reference-side `skills/*/SKILL.md`** when the
   repo ships an agent skill pack. Merge a skill with the CLI/docs verb it
   wraps (oh-my-mlip `skills/run` ≡ `oh_my_mlip.run` ≡ howto/use-a-model — one
   capability, several evidence pointers). **One user-reachable verb per
   capability; nothing finer.** A registry/roster of N models or frameworks is
   **one** domain-agent `interface` at most, not N capabilities (F7; a 20-model
   hub → one selection interface). Hub install of that roster is plumbing, not
   a verb.
2. **Dependency fingerprint** — read the manifest dependencies; map the
   domain-relevant ones to implied capability families (e.g., a phonon code may
   imply force-constants / dynamical-matrix / DOS / thermal-properties; a DFT
   code may imply SCF / relax / band-structure / response). A named method is
   not an implied family unless this work states it. Mark an implication
   `confidence: medium` unless confirmed in docs/code (`high`).
3. **Docs feature surface** — when `docs/` exists, list feature pages; each page
   that documents a user-facing capability adds one capability (evidence
   `doc: <path>`) unless it duplicates an entry surface item. Pages that only
   declare related projects, citations, or see-also lists are **§E seeds**, not
   capabilities.
4. **Tests as sanity** — test file names reflect capability boundaries; use them
   only to confirm an inventory item exists, never to invent one.
5. **Exclude** — vendored deps, build artifacts, examples (unless they are the
   documented capability), CI config, and **generic agent plumbing** (plugin
   marketplace, extra MCP server, lockfile replay, per-env bootstrap, token
   login, calculator codegen). Plumbing is not a capability
   (`capability-ir.md` granularity 4; `alignment-rules.md` §Scope).
6. **Same observable, one compute** — energy / forces / relax / MD with a
   different calculator merge into one `compute`. Hub install of a model
   roster is plumbing. Domain-agent verbs (benchmark protocol, fine-tune,
   distill) stay separate `workflow`s (granularity 6 and 8).

## B. Paper inventory (`inventory_paper`)

0. **Blindness (mandatory on dual-encoded works).** Run this pass without having
   read the repo arm in the same pass; finish every slot's `span`/`quote` here
   before §A output is consulted. Merge by product identity happens only after
   both arms are frozen (SKILL.md step 1).

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

0a. **Sync before scope (mandatory when git + remote exist).**
   ```bash
   git -C <host> remote -v 2>/dev/null || echo not-a-git-repo
   git -C <host> fetch && git -C <host> pull --ff-only
   git -C <host> status --porcelain; git -C <host> rev-parse HEAD
   ```
   Non-fast-forward, uncommitted changes, or any conflict → **stop**, show the
   caller the status, and wait for their decision (stash / commit / discard /
   proceed-dirty). Never auto-stash, auto-merge, or auto-resolve. Record the
   synced commit hash (or `not-a-git-repo` / `paused-user-decision`) for the
   report; the frozen host list is taken from this synced state.

0. **Scope the tree before scanning (F4).** Read the host doctrine if present
   (`CAPABILITY-SURFACE.md`, `AGENTS.md`, `ARCHITECTURE.md`): the declared
   skill root and tool root **are** the inventory surface. Default-exclude
   `node_modules`, `.git`, `.venv`, `vendor`, `dist`, `.claude/worktrees`,
   `*.worktrees`, plugin caches. A naive `find -name SKILL.md` on MatDiscovery
   counted 174 files; the doctrine root `plugins/matdiscovery/skills/` has 37.
   If doctrine and naive scan disagree by >2×, **stop and use the doctrine
   root** — do not classify on the inflated set.

1. **Auto-scan** (in order, until gaps close; all read-only; already scoped):
   ```bash
   # skill dirs (common framework roots) — exclude worktrees and package stores
   find . -maxdepth 3 -type d \( -name ".agents" -o -name "skills" -o -name ".dsh" \) \
     -not -path "*/node_modules*" -not -path "*/.git*" -not -path "*worktrees*" 2>/dev/null
   find . -maxdepth 4 -name "SKILL.md" \
     -not -path "*/node_modules*" -not -path "*worktrees*" -not -path "*/.git*" 2>/dev/null
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

---

## E. Companion encodings & neighborhood (`recover_reference`)

The caller may hand a **repo path**, a **homepage/docs URL**, or **both**. They
are encodings of one work \(W\), not two references (F5). If both are given,
treat homepage as `official-docs` on the core repo projection and **do not**
search for a homepage. If only a homepage is given, recover the repo from
CITATION / GitHub link on that page, then continue as a repo run.

When the given reference is a **repo** (or a homepage that resolved to one),
the local tree is only \(W_{\mathrm{repo}}\). Recover the rest of the work, then
a bounded neighborhood, **before** classifying gaps. This step observes the
reference; it does not look at the host.

Paper/blog inputs skip this section (report an empty Neighborhood). Reverse
recovery (paper → companion repo) is allowed by the same identity gate when the
paper names a code URL; it is not required on paper-only runs.

Live network is **never required** for a valid run. Homepage fetch and web-search
are best-effort using whatever fetch/search the **host agent already has**. No
search client is bundled. If they are unavailable, record `unresolved` and
continue with the local core.

### E.1 Two strata (do not mix)

| stratum | what it is | gap table |
|---|---|---|
| **core** \(W\) | the given repo + its own companion paper / official docs / CITATION | \(\mathrm{Gap}(H,W)\); C1 / C3 live here. Paper arm and repo arm stay separate projections. |
| **neighborhood** \(N\) | related papers, sibling packages, declared related tools | a second table; items tagged `layer: neighborhood` |

Neighborhood rows must not appear in the core repo gap table. The companion
paper is core, never neighborhood.

### E.2 Pipeline (in order, stop early)

**1. Seed extract (local, no network).** Read, if present:

- `CITATION.cff` preferred-citation (DOI, title, authors)
- `pyproject.toml` / `package.json` / `setup.cfg` `[project.urls]` (Homepage, Documentation, Repository)
- top-level `README*` see-also / related / "please cite" links
- `docs/` pages that declare related projects
- local `papers/` / `paper/` / `*.pdf` excerpts
- named-but-unlinked entities ("Companion solver: mini-3ph")

Each seed is a candidate with a provisional `relation`.

**2. Homepage fetch (if a Homepage/Documentation URL exists and the host can fetch).**
Parse publication lists, related-projects, documentation index. Add candidates.
Skip live fetch when the host is `example.invalid` / `localhost`, or when the
repo contains `neighborhood-search-double.json` (fixture mode).

**3. Web-search only when necessary.** Necessary iff, after (1)–(2):

- a seed is named but has no URL, **or**
- Homepage/Documentation URL exists but fetch failed and local docs do not substitute, **or**
- the work **claims a paper** (README "please cite the paper", docs/publications) that is still unresolved.

Not necessary when the caller already gave the homepage, or when
`CITATION.cff` is `type: software` with **no** `preferred-citation` article/DOI
and no docs claim a paper — companion paper is then **absent**, not missing-to-search
(F6). At most **one** optional identity-gated query for a software-only citation;
keyword collisions (other papers titled "MLIP") are rejected.

Not necessary when local + homepage already closed the companion paper and
every named seed has a URL or a local docs declaration.

Budget: **≤ 3 queries**, **≤ 5 neighborhood items kept**. Queries resolve named
seeds or the companion paper; at most **one** propose query of the form
`"{package} related packages OR companion code"` (same identity gate).

If `neighborhood-search-double.json` sits at the repo root, use it as the frozen
search response and do **not** hit the network (fixture contract). If search is
necessary, no double exists, and the host has no search: leave those seeds in
`unresolved` with reason `search-required-offline`. Do not invent packages.

**4. Identity / relation gate.** Keep a candidate only if it has a `relation`
from this closed set **and** the match is evidenced:

| relation | keep when |
|---|---|
| `companion-paper` | DOI, title, or authors match `CITATION.cff` / "please cite"; or local `papers/` is that article |
| `official-docs` | Homepage / Documentation URL of the same project |
| `sibling` | named by the core README/docs as a related package, **or** search hit for a named-unlinked seed whose authors overlap CITATION authors and whose kind is software/paper |
| `cited-method` | the repo cites it as its method paper |
| `declared-related` | listed on the homepage or `docs/` as a related project |

Reject: listicles / roundups / "top N tools"; hits that share only domain
keywords; anything without DOI / author overlap / declared name; **roster
payload** of a registry (the N models a hub *drives* are not neighborhood
works — F7). Rejected candidates are listed with a one-line reason, not
inventoried.

**5. Inventory.**

- Companion paper (kept, `layer: core`): run §B on local text if present; if
  only a DOI/URL was recovered, fetch the abstract/HTML **once** when the host
  can, else inventory the citation record at `confidence: medium` and put the
  full text in `unresolved`.
- Official docs site: treat feature pages as §A.3 evidence on the **repo**
  projection; do not duplicate them as neighborhood.
- Each kept neighborhood item: **lightweight** — title/abstract/README one-pager
  if cheap (one fetch), otherwise the mentioning sentence in the core repo.
  Do not clone the neighbor. All neighborhood capabilities start at
  `confidence: medium` at most; a search snippet with no neighbor document is
  `low`.

### E.3 Evidence gate (neighborhood)

- `low` (search snippet only) never drives `missing` — class is `unknown`.
- Neighborhood `missing` requires ≥1 high/medium evidence entry **from the
  neighbor's own abstract/README/docs**, then the same validation-before-classify
  rule as core.
- Neighborhood source kind is `reference-contrast` unless the host audit already
  admits the gap (`host-self-audit`).

### E.4 Determinism

Same repo, same seeds, same budget, same search-double (or the same three
queries on a live host) → the same `(core, kept, rejected)` triple. Live search
ranking may vary; the identity gate, not the rank, decides membership. Fixture
runs pin the double and must match `tests/fixtures/gold/mini-neighborhood.json`.