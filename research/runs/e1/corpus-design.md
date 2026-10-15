# E1 corpus design — reference-host pairs, kind/domain/host budget

Status: **design proposal, not yet executed**. Seeded by this task (2026-10-15).
Gold drafts for P1 and P2 live next to this file (`draft-gold-01-…json`,
`draft-gold-02-…json`); P3–P6 golds are intentionally not drafted yet per the
task discipline (avoid injecting unvalidated judgments wholesale — each pair's
gold gets the same "draft → judge re-run → promote" cycle as P1/P2).

## 1. Budget the corpus must satisfy (from experiments.md §E1)

- ≥ 6 reference-host pairs.
- Reference kinds: **repo × 3, paper × 2, blog × 1**.
- Domains: **≥ 2** — materials + at least one **neutral** domain (pure
  Python/web/general agent tooling).
- Host side: **multi-host** — MatDiscovery (materials) + at least one neutral
  host.
- Every pair judged by ≥ 2 human + ≥ 2 agent judges; κ per gap class and per
  source kind; pass bar κ ≥ 0.6, confusion report is a deliverable regardless.

Design principles applied (from the task brief): (a) reference-form mix per
kind; (b) domain diversity with a real neutral domain; (c) cost-tiered — the
fixture pairs are token-cheap for judges, the real pairs carry the paper value;
(d) decidability — every pair picked so a judge can actually settle each class
from local artifacts (no network, no licenses).

## 2. The six pairs

| # | reference | kind | host | domain | real/synth | cost (judge) | why | expected difficulty |
|---|---|---|---|---|---|---|---|---|
| **P1** | phonopy (repo, `/Users/lwm/code/phonopy`) | repo | MatDiscovery (`plugins/matdiscovery`, 37 skills + 13 local tools + 3 remote submit; doctrine: `docs/CAPABILITY-SURFACE.md`) | materials | real × real | high | Flagship; the documented 19-gap instance (`references/methodology.md` §3, `experiments.md` shared reqs); E1 seed AND E2 arm-(a) source | Largest surface (13-cap reference vs 37-skill host); anchors to reproduce: NAC/electronic-thermal/irreps absent; Grüneisen + group velocity present in host; α partial; host-venv actually ships phonopy 4.8.1 (dependency-fingerprint trap) |
| **P2** | `tests/fixtures/mini-paper.md` | paper | `tests/fixtures/mini-host` (heat-flow + eos skills, 2 tools, AUDIT.md) | materials | synth × synth | lowest | Cheapest; reference inventory **already a verified contract** (`gold/mini-paper.json`); exercises paper-kind extraction + tool/data capabilities + AUDIT source-kind mapping (pilot F2) | data capability (κ product) vs host kappa(T) production → equivalent-vs-adjacent boundary; single-mention (`tetrahedron-integration`) → low/unknown discipline; must-run deps (VASP, phono3py) as hard `tool` caps |
| **P3** | `tests/fixtures/mini-ref` | repo | `tests/fixtures/mini-host` | materials | synth × synth | lowest | **Replication pair** — the verified pilot gold (`gold/mini-ref-vs-mini-host.json`) *is* the E1 seed asset; anchors the κ scale against the recorded pilot record (5/6 class, 2/6 source) | judge contamination — judges must not read `e1-pilot-agreement.md` before running; source-kind split was the pilot's weak spot |
| **P4** | zvec-grep (repo; TypeScript local-first unified search, `docs/` + CLI `zg`) | repo | memmy-agent host (real agent bundle: skills incl. `skill-creator`, memory adapters, session tooling — pick the surface with the host's own convention) | **neutral** (agent search/retrieval vs agent memory/session — both infra, no science lexicon) | real × real | medium–high | Proves cross-domain generality: the whole domain-lexicon adaptation layer swaps (no phonon/DFT families, no materials references) | No domain lexicon exists yet — map = medium-confidence implied families by hand; retrieval/memory semantics adjacency (session vs memory vs tool registry) likely confuses `partial`/`missing`; zvec-grep has 900+ files (inventory reads surface only, judges still must find entry points) — pin the reference to `README.md + docs/ + package CLI` to bound cost |
| **P5** | hindsight paper (arXiv 2512.12818, LLM-application trace evaluation) | paper | same host as P4 | neutral | real × real | medium | Second paper slot; **same host + same domain as P4, only the reference form changes** — isolates the reference-kind variable for κ (`paper` vs `repo` on identical host/domain); hindsight also has a repo, so judges can cross-check claims | Paper-extraction heuristics were only ever exercised on materials papers; neutral-domain methods↔steps decomposition is fresh ground; low-confidence single-mention items expected → unknown-gating pressure |
| **P6** | a materials-domain blog post with a concrete recipe + numbers | blog | MatDiscovery | materials | real × real (fallback: `mini-blog.md` → `mini-host`) | low–medium | Blog slot; blogs are inherently evidence-thin (opinion → `concept`/`low` per alignment-rules §Reference-side heuristics) — forces the `unknown` gate to carry the table | Lowest expected κ subclass: `low`–`unknown` gating is the most judgment-dependent step; blog must be citation-safe (use a permissively-licensed post or the fixture fallback — do NOT scrape copyrighted prose into the corpus); a blog with mostly `unknown` gaps is a *valid* pair, but flag it so judges don't game toward `missing` |

References on disk are read-only inputs (never modified); the host side is only
ever *observed* (skills/tools read, `git status` untouched).

## 3. Host and domain budget — why these hosts

- **MatDiscovery** (P1, P6): the only host with a complete documented doctrine
  (`CAPABILITY-SURFACE.md` §0.1 decision quick-ask — the alignment-rules worked
  example) and the only one with an existing 19-gap instance. It is the
  materials anchor by construction.
- **mini-host** (P2, P3): the pilot's verified host surface; reuses AUDIT.md as
  the self-audit source-kind oracle.
- **memmy-agent** (P4, P5): a *real, local, non-science* agent bundle — it is
  the neutral host. Note on K-Dense (the drift-preliminary / E3 suggestion):
  K-Dense's registry (`research/runs/e3/kdense-registry.json`) is full of
  scientific protocols (clinical-trial templates, CellProfiler logs, assay QC)
  — it is a **science-domain** skill library, so it does NOT satisfy the
  "neutral domain" half of the corpus. Same verdict applies to agapi (JARVIS
  family). A neutral domain must come from genuinely non-scientific tooling.

## 4. Protocol recommendations for the judge fan-out (needs main-agent sign-off)

1. **Fixed reference surface as input.** Judges classify from the gold's
   provided `reference_inventory` (each draft gold ships one), *then may also
   submit their own inventory* for a secondary inventory-agreement number
   (pilot F3 — granularity drift — would otherwise contaminate classification
   κ). Classification agreement and inventory agreement are reported separately.
2. **Per-row confidence** is part of the judgment (each gap row carries one);
   κ is computed over (class, source_kind, confidence∈{…}) cells so the
   confusion report can address "low-confidence mass" directly.
3. **Judge isolation:** judges must not read the pilot agreement record
   (`e1-pilot-agreement.md`) or each other's outputs before their own run;
   the gold files are the target, not the input.
4. **Determinism:** each judge records run id + model + inputs (shared E1
   requirement); a same-input re-run must reproduce their own table.
5. **Dependency-fingerprint rule for every judge** (capability-ir.md #3):
   MatDiscovery's venv *installs* phonopy 4.8.1 (`bte_controller` Requires-Dist
   phonopy) — a host-side *dependency* fingerprint is not a host capability and
   never covers a reference capability.

## 5. What a pair needs to be promotable from draft to verified gold

Covered in `draft-gold-01/02` headers: identical row structure to
`gold/mini-ref-vs-mini-host.json` + the two logged schema extensions
(per-row `confidence`, top-level `equivalent[]` + `reference_inventory[]`),
all adaptations recorded in `log:`. Promotion flow: judges re-run → agreement
≥ pass bar → copy into `tests/fixtures/gold/` with the run record; any class
moved during promotion logs the reason (evaluation.md Layer-2 discipline).

## 6. Open items / risks

- **P1 gap-count mismatch**: the instance is described as 19 gaps, this draft
  derives 9 gap rows on a 13-capability reference. The original 19-gap table
  is not preserved anywhere in capalign; three instance-recorded
  host-admitted items (melting-point runner, collective conductivity, FF
  sanity) have **no phonopy reference capability** on a strict reading — they
  only enter a gap table if the reference inventory is broader than phonopy's
  (e.g. a "vibrational-thermodynamics family" surface). Decision point for the
  main agent: keep the strict phonopy-only reference (this draft) or widen the
  reference to the family-level surface the instance apparently used.
- **P4/P5 host selection**: memmy-agent's surface must be pinned (which modules
  count as the skill/tool registry) by whoever builds that pair's gold; same
  for zvec-grep's entry-point pinning.
- **P6 blog choice** is license-sensitive; fixture fallback (mini-blog →
  mini-host) is the cheap controlled option and already carries a verified
  inventory (`gold/mini-blog.json`).
- **budget**: P1 is the only genuinely expensive pair (13-cap reference vs
  37-skill host). P3 is near-free (all fixtures exist). The knob under token
  pressure is P4/P5: pin the reference surface to `README + docs/ + CLI entry
  points` (as the table notes) to bound judge reading without losing the
  neutral domain. Dropping any repo-form pair breaks the repo×3 count — if one
  must go, replace P3 with a *different* cheap repo pair rather than a net
  removal.
- **One P2 refinement may be needed**: `thermal-conductivity-data` classified
  equivalent (host heat-flow produces kappa(T)); judges may argue data-kind
  capabilities should be `partial` (product provenance differs). Low impact —
  it is a logged draft row, judge-run will settle it.