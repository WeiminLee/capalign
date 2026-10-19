# Innovation proposals memo (ACL design lock)

> **Date.** 2026-10-18 (Asia/Shanghai).  
> **Status.** **DECIDED** — user locked Option 1 (2026-10-18): **coverage fork + principled refusal + \(K_H\)/\(t_v\)**.  
> **Purpose.** Algorithm principle + innovation lock *before* further paper-body expansion.  
> **Baseline.** Prior draft claim = λ→I typed introduction (`paper.md` v0.3). Locked claim = refined C1–C3 below.  
> **Rule.** No fabricated experiments. Contribution bullets locked; `paper.md` v0.4.1 expanded around C1–C3 (empirics still TODO).

---

## 1. Current claim weaknesses vs neighbors

### 1.1 One-line baseline claim (what we have)

> Residual of dual-encoded work \(W=(W_p,W_r)\) is typed by product-slot unit \(u\) into unique \(\lambda\); \(\lambda\) selects introduction operator \(I\) on deployed host \(H=(P_H,K_H)\) plus fail-before / destroy-tests; vs wrap-repo / paper-only / write-directly, \(I\) is contractually better on FI / Miss / \(t_v\).

### 1.2 Weaknesses (reviewer attack surface)

| Weakness | Why it hurts | Neighbor that weaponizes it |
|---|---|---|
| **Taxonomy surface-collision** | SciCoQA’s Difference / Paper Omission / Code Omission ≈ our procedure-conflict / obligation-sans-entry / entry-sans-obligation. If C1 is “we also type residuals,” reviewers call it *SciCoQA + edit rules*. | [SciCoQA](https://aclanthology.org/2026.acl-long.1795/) ACL 2026 Main, SAC Highlight |
| **Contract-language collision** | ReproAgent’s *two-channel implementation contract* (paper obligations + repo evidence) sounds like dual encoding. Without a hard “host + refusal + FI” differential, Related Work looks soft. | [ReproAgent](https://arxiv.org/abs/2608.24291) Findings EMNLP 2026 |
| **Theorems assume oracles** | Props. 2–5 need Id, \(\kappa\), Faithful, empty-\(P_H\) start. Without human IRR + Faithful obedience rates, Soundness looks definitional, not scientific. | ARR M5 / M1; [Rating Roulette](https://aclanthology.org/2025.findings-emnlp.1361/) |
| **Validity-gap / \(\kappa\) under-illustrated** | Mini-ref has almost no both-aligned rows; phonopy has validity-gap but no conflict row with gold \(\kappa=1\). Empirically weakest types are the ones that best separate us from SciCoQA. | SciCoQA’s Difference class is their *real* bulk |
| **“Fast / Effective / Testable” brand risk** | Without tables, slogan reads marketing. Call-count / destroy-test must be *definitions*, not vibes. | SA-Bench: executability scaffolds ≠ fidelity |
| **Materials-instance niche** | If narrative stays “materials agent tool,” venue fit weakens vs NLP/agent methodology. | LMR-BENCH / SA-Bench sit in NLP/ML venues |
| **MCP/skill wrap not owned as baseline** | Industry default *is* wrap-repo. If we don’t name MCP attach / SkillFoundry / Trace→skill as \(W_{\mathrm{rap}}\) / write-directly, the FI story feels abstract. | [OWASP MCP](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html); Agentic Skills Top 10 |
| **Detect vs Introduce vs Reproduce triad is clear but thin** | Triad is good framing; innovation must be *what Introduce knows that Detect/Reproduce cannot*. Coverage fork + principled refusal + \(K_H\) are the knowledge, not the triad label. | SA-Bench / LMR / PaperBench / SciReplicate |

### 1.3 What is already strong (do not throw away)

1. **Host is required** — remove \(H\) → claim collapses to SciCoQA. Keep this sentence as Intro load-bearing claim.  
2. **Product-Id merge before typing** — operational antidote to Dude’s granularity asymmetry.  
3. **Counting identities** FI(\(I\))=0; FI/Miss(\(W_{\mathrm{rap}}\))=omission counts; \(t_v\) separates validity — falsifiable *if* Faithful holds.  
4. **Coverage fork** (`qha` vs `band`) — best single figure insight; under-sold as contribution vs “we have λ.”  
5. **Destroy-test** — TestPrism-aligned acceptance for introduction, orthogonal to reproduction scores.

---

## 2. Candidate innovation angles (ranked strongest → weaker)

### Rank 1 — **Coverage fork as primary knowledge claim** (elevate; merge into λ→I)

**One-sentence claim (EN).**  
A dual-encoded work induces two host-coverage measures whose gap sets can be disjoint; any introduction policy that collapses to one face is contractually wrong on FI or Miss.

**Why novel vs neighbors.**  
- SciCoQA: no host → no coverage of \(H\).  
- Dude: grain asymmetry is detection precision/recall; we show *asymmetric host gaps* after product-Id merge.  
- ReproAgent: *merges* paper obligations + repo evidence into one generation contract; we prove that for *introduction into existing \(H\)*, the two faces must remain separable (entry-sans-obligation must not become host products).  
- SA-Bench / LMR / SciReplicate: evaluate generated repo fidelity, not fork on a frozen host surface.  
- MCP wrap: optimizes \(\mathrm{coverage}_{repo}\) by definition.

**Algorithmic principle sketch.**  
1. Independent inventories → product-Id merge → \(\lambda\).  
2. Define \(\mathrm{Obl}=\{p:s=1\}\), \(\mathrm{Ent}=\{p:e=1\}\).  
3. Project gaps: obl-sans-entry → paper-face gap / repo-face absent; entry-sans-obl → reverse.  
4. Theorem-style (already Prop. 3): empty-host wrap-repo FI = \|entry-sans-obl\|, Miss = \|obl-sans-entry\|.  
5. Corollary: if both omission types nonempty, no single-face policy can be FI=0 and Miss=0.

**Insight bought.**  
“Runnable attach” and “paper checklist” are *different instruments*; dual encoding is not two adapters for the same coverage number.

**Risk / cost to validate.**  
**Medium.** Need ≥N works where both omission types appear (phonopy already has both). Report Jaccard of paper-face vs repo-face gap sets; show empty intersection on ≥1 illustrative + ≥k corpus pairs. EΔ is the right experiment — currently TODO.

**Recommendation.** **KEEP + ELEVATE as C1 core.** λ remains the partition engine; fork is the *insight headline*. Do not lead with “six labels.”

---

### Rank 2 — **Principled non-introduction (refusal as success)** (sharpen λ→I)

**One-sentence claim (EN).**  
Correct typed introduction includes *positive refusal*: for entry-sans-obligation and procedure-conflict, success is “\(H\) unchanged + unresolved/excluded record,” not “more products on \(H\).”

**Why novel vs neighbors.**  
- SciCoQA *detects* Paper Omissions; it does not define a host success predicate for *not installing* them.  
- ReproAgent / PaperCoder / SkillFoundry / Trace→skill: generation always tries to realize surfaces.  
- MCP / skill wrap: connect = success. OWASP: connect ≠ least-privilege own.  
- SA-Bench scores whether generated code implements claims — never rewards *not* implementing a repo-only callable as a host obligation.

**Algorithmic principle sketch.**  
\[
I(H,u)=\begin{cases}
H & \lambda\in\{\text{entry-sans-obl},\text{procedure-conflict},\text{incongruent}\}\\
\text{edit }P_H/K_H & \text{otherwise per table}
\end{cases}
\]
Success for refusal types: \(\Delta P_H=\emptyset\) (and no silent side-pick for conflict). Ablation \(\pi\) swapping omission types must flip which units get refused vs written (Prop. 5).

**Insight bought.**  
Agent “capability expansion” literature and industry wrap-all share a wrong stop condition: *more tools* ≠ *better host relative to paper contract*. Refusal is part of Effective, not a failed run.

**Risk / cost to validate.**  
**Low–medium.** Contract counting is free once slots labeled; need human agreement that entry-sans-obl should *not* be host products (annotation guideline + IRR). Show wrap-repo FI on those rows. No need for heavy LLM codegen if reporting contract counters first.

**Recommendation.** **KEEP + MERGE into C2.** Make “refusal” a named subclaim in Intro (currently buried in method table).

---

### Rank 3 — **Validity-gap → \(K_H\) as third residual axis** (under-sold differentiator)

**One-sentence claim (EN).**  
When procedure and entry align but invalidation is one-sided (\(v_p\neq v_r\)), introduction must install a host check \((p,v)\in K_H\); product presence alone (\(p\in P_H\)) is an incomplete success (\(t_v=0\)).

**Why novel vs neighbors.**  
- SciCoQA taxonomy has no dedicated *validity / invalidation* type (Difference ≈ procedure conflict; omissions ≈ missing sides).  
- SA-Bench D1–D4 are numerical/method/protocol/ordering *drift in generated code*, not dual-spec invalidation asymmetry.  
- ReproAgent validation = requirement review + runtime; not “paper says melts near melting point → host must fail on that input.”  
- CodeSpec dual *executable* specs (architecture + behavior) for feature coding — different dual: SE specs, not paper↔repo scientific invalidation.

**Algorithmic principle sketch.**  
λ=validity-gap ⇒ add \(p\) *and* the stated-side invalidation into \(K_H\). Test \(t_v=\mathbf{1}[p\in P_H]\cdot\mathbf{1}[(p,v)\in K_H]\). Prop. 4: wrap-repo and paper-only leave \(t_v=0\) if check was absent. Destroy: delete check → \(t_v=0\).

**Insight bought.**  
Green “delivers product” tests can be scientifically invalid witnesses (AgentRepo: runnable ≠ justified; TestPrism Joint Success ≪ single-ref). Validity is a *residual type*, not a post-hoc lint.

**Risk / cost to validate.**  
**Medium–high.** Need works with explicit one-sided invalidation (phonopy `qha` is the gold example). Writing destroy-tests that actually fail on invalid inputs costs annotation + harness work. Highest *novelty density* per unit of taxonomy expansion.

**Recommendation.** **KEEP as C2 pillar; do not drop.** If page-starved, drop “Fast” branding before dropping \(t_v\).

---

### Rank 4 — **Fail-before + destroy-test as introduction acceptance protocol** (empirical instrument)

**One-sentence claim (EN).**  
Host edits are accepted only under a fail-before / green / destroy-red contract; destroy-still-green rates measure invalid tests, not alignment success (TestPrism Joint Success analogue for introduction).

**Why novel vs neighbors.**  
- Reproduction benches score final repo / claim match; they do not require *pre-edit failure on the same host*.  
- SkillRevise: gate on post-edit tests; weaker on “test must have been red on the *pre-edit* host.”  
- TestPrism diagnoses *test quality*; we reuse the spirit for *introduction witnesses*.  
- SciCoQA has no edit/test loop.

**Algorithmic principle sketch.**  
Freeze tests before patching \(H\). Require: fail(\(H\)) ∧ pass(\(H'\)) ∧ fail(\(H'_{-a}\)) where \(a\) is prescribed bind/steps/check. Report still-green-after-destroy as test-invalid rate.

**Insight bought.**  
Separates Faithful obedience from spurious greens; directly answers ARR concerns about LLM-written checks.

**Risk / cost to validate.**  
**High** for Main-scale tables; **medium** for Findings if done on small frozen slot set with hand-written destroy harness. Depends on Faithful patches (LLM or human).

**Recommendation.** **KEEP as C3 instrument.** Do not claim “more trustworthy” without this number. Optional merge: call it *acceptance protocol*, not a separate “algorithm.”

---

### Rank 5 — **Product-Id merge as Dude operationalization for introduction** (design constraint → claim)

**One-sentence claim (EN).**  
Residual units for introduction must be solicit-able products merged by identity *before* typing; sentence↔function residuals are forbidden inputs to host-gap decisions.

**Why novel vs neighbors.**  
Dude diagnoses over-reporting from granularity asymmetry; SciCoQA operates at QA/sentence grain. We turn the diagnosis into a *hard interface*: no product Id ⇒ no unit ⇒ cannot drive FI/Miss. ViewPoints: unmanaged multi-view inconsistency stays unilateral.

**Algorithmic principle sketch.**  
Independent side inventories → Id merge or keep unilateral (other side zeros) → never invent host gap from unmatched sentence/function pair.

**Insight bought.**  
Detection F1 and introduction safety optimize incompatible grains; raising SciCoQA recall by finer reporting can *increase* wrap-repo FI if those reports become host products.

**Risk / cost to validate.**  
**Medium.** Need IRR on Id decisions + disagreement analysis (partial/missing). Dude already supplies the motivation quote.

**Recommendation.** **MERGE into C1** (fork + product slots). Do not spend a whole contribution bullet unless Id IRR is a headline result.

---

### Drop / demote candidates

| Idea | Verdict | Why |
|---|---|---|
| “Six λ types as taxonomy contribution” alone | **DEMOTE** | Taxonomy ≈ SciCoQA + validity + incongruent; taxonomy is *means*. |
| “Faster than write-directly” as C-level claim | **DEMOTE until Fast table exists** | Definition OK; claim not. |
| “Better detector than SciCoQA” | **DROP** | Wrong battlefield. |
| “SOTA paper→code” | **DROP** | Wrong battlefield. |
| “Eight-step skill instrument” | **DROP from contributions** | Skill behavior ≠ paper claim. |
| Full CodeSpec-style dual executable specs for host | **DROP / out of scope** | Different dual; would explode scope into SE feature coding. |
| Competing with BIV/SkillConsist on package self-audit | **DROP** | Different axis (intra-artifact). |

---

## 3. Locked contribution set (C1–C3) — **DECIDED**

**Refined one-liner (replace §0 identity when locking):**

> Dual encoding forks host coverage; product-typed residual \(\lambda\) selects introduction *and refusal* on deployed \(H\), including validity checks \(K_H\), under a fail-before/destroy acceptance contract that wrap-repo and paper-only violate on FI, Miss, or \(t_v\).

### C1 — Problem reformulation (insight + model)

**EN.** *Coverage-fork residual for dual-encoded scientific work:* independent paper/repo inventories are merged by product identity into units \(u\); the induced paper-face and repo-face host-gap sets can be disjoint; \(\lambda\) is the unique partition of residual (including validity-gap and procedure-conflict).

**Insight.** Dual encoding is not two views of one coverage number; detection taxonomies without \(H\) cannot state this.

### C2 — Method (algorithm)

**EN.** *Typed introduction operator \(I\) with principled refusal:* \(\lambda\) maps to edits of \(H=(P_H,K_H)\) *or* to non-introduction (entry-sans-obligation / procedure-conflict / incongruent). Counting: \(\mathrm{FI}(I)=0\); wrap-repo FI/Miss equal omission-type counts; only \(I\) installs \(t_v=1\) on validity-gap (Props. 2–4). Label permutation \(\pi\) is a non-vacuous ablation (Prop. 5).

**Insight.** Type is causal for *which wrong edit* untyped policies commit; refusal is part of correctness.

### C3 — Evaluation protocol (evidence shape)

**EN.** *Contract acceptance protocol:* against wrap-repo (\(W_{\mathrm{rap}}\) / MCP-attach), paper-only, and write-directly, report Effective (FI, Miss, \(t_v\)), Testable (fail-before → green → destroy-red), and optionally Fast (calls to green). Materials (or any domain with public products + enumerable host) is instance one; \(\lambda\) frozen.

**Insight.** Reproduction fidelity and detection recall are the wrong scalars for host introduction.

### Mapping to current draft

| Current C (paper.md §1.4) | Action |
|---|---|
| Typed residual | **Rewrite toward C1** — lead with fork + product Id; λ as partition, not headline |
| Operator \(I\) | **Rewrite toward C2** — name refusal + \(K_H\) explicitly |
| Contract protocol | **Keep as C3** — demote Fast until measured; keep destroy-test mandatory |

---

## 4. What NOT to claim

| Do not claim | Honest substitute |
|---|---|
| Empirically measured residual rates / multi-work EΔ | “Illustrated on mini-ref & phonopy slots; EΔ TODO” |
| Human IRR κ = … | “Same-model pilot = lower bound; E1′ human IRR TODO” |
| Faster / more accurate / more trustworthy (user study) | Bind to Fast / Effective / Testable definitions only |
| Outperforms SciCoQA on detection | Orthogonal: they detect; we introduce on \(H\) |
| Paper→code SOTA (SA-Bench / LMR / SciReplicate / PaperBench / ReproAgent) | Not a generation/reproduction benchmark |
| “First taxonomy of paper–code mismatch” | SciCoQA already owns detection taxonomy |
| Eight-step cap-align skill loop as contribution | Instrument only |
| LLM judge calibrated | Limitations + Rating Roulette citation |
| MCP/skill wrap is insecure *empirically in our runs* | Position as \(W_{\mathrm{rap}}\) baseline + OWASP connect≠own *design* argument until measured |
| Domain-universal for any chat agent | Three co-conditions (public products, dual process encodings, enumerable host) |

---

## 5. Key URLs

| Work | URL | Use in RW / insight |
|---|---|---|
| SciCoQA (ACL 2026) | https://aclanthology.org/2026.acl-long.1795/ · https://arxiv.org/abs/2601.12910 · https://ukplab.github.io/scicoqa/ | Detect; false assurance; taxonomy collision |
| Dude | https://arxiv.org/abs/2609.03416 | Granularity asymmetry → product-Id constraint |
| SA-Bench | https://arxiv.org/abs/2608.24252 · https://arxiv.org/html/2608.24252 | Semantic drift; exec ≠ fidelity |
| ReproAgent | https://arxiv.org/abs/2608.24291 · https://arxiv.org/html/2608.24291 | Split-spec *generation* contract ≠ host introduction |
| LMR-BENCH | https://aclanthology.org/2025.emnlp-main.314/ · https://arxiv.org/abs/2506.17335 | Masked-repo reproduction |
| SciReplicate-Bench | https://arxiv.org/abs/2504.00255 | Algorithmic reproduction |
| PaperBench | https://arxiv.org/abs/2504.01848 | Repo reproduction rubrics |
| TestPrism | https://arxiv.org/html/2610.12289 | Joint Success → destroy-test analogue |
| Rating Roulette | https://aclanthology.org/2025.findings-emnlp.1361/ | LLM-judge reliability |
| Skill-as-Pseudocode | https://arxiv.org/abs/2605.27955 | Contract+template skills; untyped skill gen neighbor |
| BIV | https://arxiv.org/abs/2605.11770 | Intra-skill audit ≠ host-relative \(W\) |
| SkillConsist | https://arxiv.org/html/2608.07639 | Package self-inconsistency |
| CodeSpec (dual exec. specs) | https://arxiv.org/abs/2607.26777 | Different dual; SE feature coding |
| OWASP MCP Cheat Sheet | https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html | Connect ≠ own; wrap = \(W_{\mathrm{rap}}\) |
| OWASP MCP Top 10 | https://owasp.org/projects/mcp-top-10 | Tool poisoning / scope creep framing |
| OWASP Agentic Skills Top 10 | https://owasp.org/www-project-agentic-skills-top-10/ | Skills layer ≠ MCP connect |
| ViewPoints (TSE 1994) | DOI 10.1109/32.328995 | Multi-view consistency managed, not forced |

Local design authorities: `docs/typed-introduction.md`, `research/introduction-operator.md`, `research/slot-model.md`, `docs/acl-paper-design.md`, `docs/acl-draft/insights-research.md`, `docs/acl-draft/paper.md` (baseline only).

---

## 6. Lock decision — **DECIDED** (2026-10-18)

| Decision | Choice |
|---|---|
| **Status** | **DECIDED** — Option 1 locked by user |
| Lead insight | **Coverage fork** (Rank 1), not “six λ” |
| Method core | **λ→I + principled refusal + \(K_H\)/\(t_v\)** (Ranks 2–3) |
| Evidence shape | **FI / Miss / \(t_v\) + destroy-test** (Rank 4); Fast optional until measured |
| vs SciCoQA | Shared residual labels; **host + introduce/refuse** is the wall |
| vs ReproAgent | Their dual channels *fuse for generation*; ours *keep faces fork for introduction* |
| vs MCP/skill wrap | Name as wrap-repo baseline; least-privilege introduction |
| Contribution docs | Updated: `acl-paper-design.md` §0–§1, `brief.md`, `abstract.md`, this memo, `acl-draft/README.md`; short claim lock on `paper.md` only |
| paper.md body | **v0.4.1 bulk rewrite done** (2026-10-18) around C1–C3; empirics still TODO |
| Experiments before Main | EΔ fork Jaccard → E1′ human Id/λ IRR → E2′ arms on FI/Miss/\(t_v\) + destroy |

**Locked one-liner (EN).** Dual encoding forks host coverage; product-typed residual \(\lambda\) selects introduction *and refusal* on deployed \(H\), including validity checks \(K_H\), under a fail-before/destroy acceptance contract that wrap-repo and paper-only violate on FI, Miss, or \(t_v\).

**Locked one-liner (ZH).** 双编码会在宿主上分叉覆盖；产物类型残差 \(\lambda\) 决定对已部署 \(H\) 的引入*与原则性拒绝*（含有效性检查 \(K_H\)），并用改前必败/破坏测试验收；只接仓库/只抄论文会在 FI、Miss 或 \(t_v\) 上违约。
