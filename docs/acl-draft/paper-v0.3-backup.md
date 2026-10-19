# Typed Introduction of Dual-Encoded Scientific Work into Deployed Agents

> **CLAIM LOCK (DECIDED 2026-10-18) — contribution bullets only; body below is v0.3 baseline, not yet retargeted.**
>
> **One-liner.** Dual encoding forks host coverage; product-typed \(\lambda\) selects introduction *and refusal* on \(H=(P_H,K_H)\), including \(K_H\)/\(t_v\), under fail-before/destroy acceptance that wrap-repo / paper-only violate on FI, Miss, or \(t_v\).
>
> | # | EN | ZH |
> |---|---|---|
> | **C1** | Coverage-fork residual: product-Id merge; paper-face vs repo-face host gaps can be disjoint; \(\lambda\) partitions residual. | 双编码分叉宿主覆盖；产物身份合并后面向可不相交。 |
> | **C2** | Typed \(I\) with principled refusal + \(K_H\): refuse entry-sans-obl / conflict / incongruent; install \(t_v\) on validity-gap. | \(\lambda\) 决定编辑与原则性拒绝；有效性缺口装 \(K_H\)。 |
> | **C3** | Contract acceptance: Effective (FI, Miss, \(t_v\)) + Testable (fail-before→destroy); Fast optional until measured. | FI/Miss/\(t_v\)+破坏测试验收；不跟检测/复现抢榜。 |
>
> Authority: [`../acl-paper-design.md`](../acl-paper-design.md) §0–§1.2; [`innovation-proposals.md`](innovation-proposals.md). **No fabricated empirics.**

**Working title (ACL long / Findings).**  
*Coverage Fork and Typed Introduction: Residual Labels Select Host Edits, Refusal, and Validity Checks*

**Status.** Draft **v0.3 body** + **v0.4 claim lock** (2026-10-18, Asia/Shanghai). Body not bulk-rewritten; contributions locked to C1–C3. See `CHANGELOG-v0.3.md`, `innovation-proposals.md`.  
**Claim scope.** [`../acl-paper-design.md`](../acl-paper-design.md) §0–§1.2 (DECIDED) and §1.3 — no fabricated empirics; unrun cells `TODO`.  
**Figure X.** [`../figures/typed-introduction/cap-align-typed-introduction.pdf`](../figures/typed-introduction/cap-align-typed-introduction.pdf)  
**Formal proofs.** [`../../research/introduction-operator.md`](../../research/introduction-operator.md) (Props. 1–5). Design authority: [`../typed-introduction.md`](../typed-introduction.md).

---

## Abstract

A user who already runs a host agent \(H\) and faces a dual-encoded work \(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\) needs more than a discrepancy detector: justified *host edits* and tests that must fail *before* those edits. We cast paper–repo residual as a typed unit \(u=(p,s,e,v_{\mathrm{p}},v_{\mathrm{r}},\kappa)\) with unique label \(\lambda\), and define introduction operator \(I\) mapping \(\lambda\) to edits on \(H=(P_H,K_H)\) plus a fail-before / destroy-test contract. Counting statements show \(I\) introduces no false products (\(\mathrm{FI}=0\)); wrap-repo’s FI and Miss equal the counts of entry-sans-obligation and obligation-sans-entry; wrap-repo and paper-only leave \(t_v=0\) on validity-gap units. Fast / Effective / Testable mean call count, those counters, and destroy-tests. Materials agents are the first instance; the type set is frozen. We do not claim detection SOTA (SciCoQA) or paper→code SOTA. Multi-work EΔ, human IRR, and arm tables remain `TODO`.

**Keywords:** scientific agents; dual-encoded specs; paper–repo residual; typed introduction; fail-before tests; host-relative coverage.

---

## 1. Introduction

### 1.1 Problem

Deployed scientific agents and published paper+repo works arrive on different schedules. Holding \(H\) and a new \(W\), the practitioner’s first question is not “does this paper match its own code?” (detection) nor “can an agent regenerate the code?” (reproduction), but:

> Which products of \(W\) does \(H\) already deliver, which residual *types* justify an edit, and which test must fail *before* that edit?

A gap table answers only coverage. A discrepancy detector answers a different paper. Neither says *what to change* when paper and repo disagree.

### 1.2 Claim vs SciCoQA (and vs reproduction)

**SciCoQA** (ACL 2026 Main) detects conflicts between a paper and *its own* code at sentence/claim grain, and reports recall of *real* discrepancies (best \(\approx 46.7\%\); Paper Omissions hardest). Their taxonomy (Difference / Paper Omission / Code Omission) roughly aligns with our procedure-conflict / obligation-sans-entry / entry-sans-obligation. **Shared surface: residual labels. Differential: we require a deployed host \(H\), and \(\lambda\) selects an introduction operator \(I\) with fail-before tests.** Remove \(H\) and the claim collapses to detection—we refuse that collapse.

**Reproduction / generation** (SA-Bench, LMR-BENCH, SciReplicate, ReproAgent, PaperBench, AutoMat, SkillFoundry-style wrap) ask whether agents can write or run code from papers. Our endpoint is an *edit contract* on an existing host surface, scored by FI / Miss / \(t_v\), not execution accuracy.

| Family | Input | Output | Success |
|---|---|---|---|
| Detect | Paper + own code | Discrepancy labels | Recall / F1 |
| Reproduce | Paper (± repo) | Code / run / claim match | Fidelity / exec. |
| **Introduce (ours)** | \(W\) + **host** \(H\) | \(I(H,\lambda)\) + fail-before | FI, Miss, \(t_v\); Fast; Testable |

### 1.3 Insights (why type is causal, not catalog)

Dual encoding is not two adapters. On one \(H\), \(\mathrm{coverage}(H,W_{\mathrm{paper}})\) and \(\mathrm{coverage}(H,W_{\mathrm{repo}})\) can fork: obligation-sans-entry gaps only on the paper face; entry-sans-obligation only on the repo face (Figure X(b); `qha` vs `band`). Wrapping every entry **installs products the paper never obligated** and **misses products the paper obligated but the repo never exposed**. Type causes wrong edits.

Three community takeaways:

1. **Detection recall \(\neq\) introduction safety.** Low SciCoQA recall yields *false assurance* (missed real conflicts). Untyped wrapping yields *false introduction* (FI). Dude shows naïve dual-detection raises recall but tanks precision via *granularity asymmetry*—sentence↔function alignment invents gaps no product identity supports. Both failures are silent and orthogonal.
2. **Runnable / used \(\neq\) host-covered.** SA-Bench: semantic drift persists under executability scaffolds (mean SAU \(\approx 0.221\)). Materials-side notes converge: code execution \(\neq\) reliable scientific execution; skill *usage* \(\neq\) capability gain; stop conditions must bind obligations, not “it compiled.” Nearest host skills (`eos` \(\neq\) QHA) must not flip `host_has`.
3. **Green tests can be invalid.** TestPrism: Joint Success (\(\approx 28\%\)) ≪ single-reference success (\(\approx 60\%\)). Our destroy-test is the introduction analogue—if deleting the prescribed bind/steps/check leaves the suite green, it was never a validity witness. Rating Roulette: LLM-judge scores can be self-inconsistent; E1′ therefore requires human IRR.

### 1.4 Contributions

> **Authoritative C1–C3:** see claim lock at top of this file and [`../acl-paper-design.md`](../acl-paper-design.md) §1.2. Bullets below retargeted to the DECIDED lock (no other body expansion).

1. **C1 — Coverage-fork residual:** merge by product identity into \(u\); paper-face vs repo-face host-gap sets can be disjoint; unique \(\lambda\) partitions residual (incl. validity-gap, procedure-conflict)—host-facing, not a sentence–function detector; lead with *fork*, not “six labels.”
2. **C2 — Operator \(I\) with principled refusal + \(K_H\):** \(\lambda\) selects edits on \(H=(P_H,K_H)\) *or* non-introduction (entry-sans-obligation / procedure-conflict / incongruent); install \(t_v\) on validity-gap. Counting: \(\mathrm{FI}(I)=0\); wrap-repo FI/Miss = omission counts; wrap-repo/paper-only give \(t_v=0\) on validity-gap; \(\pi\) non-vacuous.
3. **C3 — Contract acceptance:** vs wrap-repo / paper-only / write-directly—Effective (FI, Miss, \(t_v\)) + Testable (fail-before→destroy); Fast only when measured. Type set frozen; materials is instance one.

**Not claimed:** multi-work residual rates (`TODO` EΔ); human IRR (`TODO` E1′); user-study “faster/more accurate”; SciCoQA detection SOTA; paper→code SOTA; “six λ taxonomy” as the contribution; eight-step instrument loops.

---

## 2. Related Work

Neighbors by *scientific question*. Full bibliography notes: [`insights-research.md`](insights-research.md), [`../../research/related-work.md`](../../research/related-work.md).

**Detect.** SciCoQA (ACL 2026; arXiv:2601.12910): paper↔own-code discrepancies; missed conflicts → false assurance. Dude (EMNLP 2026; arXiv:2609.03416): granularity asymmetry; dual-detection can raise recall while destroying precision. We adopt both as *design constraints*: merge by product Id **before** typing; refuse sentence-level host gaps; entry-sans-obligation must not become host products. We do **not** list “better detector” as a contribution.

**Reproduce / generate.** SA-Bench (semantic drift; arXiv:2608.24252); LMR-BENCH, SciReplicate-Bench, PaperBench (incomplete understanding, brittle integration); ReproAgent (Findings EMNLP 2026; arXiv:2608.24291) persists *split* specs (paper obligations + repo conventions) for *generation*. AutoMat-style claim reproduction can match scalars while leaving the scientific claim unverified. Untyped skill compilation (SkillFoundry / Trace→skill / Repo-To-Skill) is our write-directly / wrap neighbor. Endpoint differs: edit contract on **existing** \(H\), not a new artifact.

**Intra-artifact audit.** BIV / SkillConsist / DCI / Skill Coverage compare a package or trajectory to *itself*. Shared words (“drift,” “coverage”) must not collapse axes: ours is incoming \(W\) vs deployed \(H\).

**SE / systems cousins.** ViewPoints (Nuseibeh et al., 1994): multi-view specs may contradict; consistency is *managed*, not forced—motivates unilateral rows and \(\kappa=0\) when undecidable. TestPrism / mutation testing: reject invalid implementations—motivates destroy-tests. OWASP MCP: connect \(\neq\) least-privilege ownership—MCP-wrap is \(W_{\mathrm{rap}}\), not \(I\).

| Work | Their Q | Diff vs us |
|---|---|---|
| SciCoQA | Detect paper–own-code | Host required; \(\lambda\to I\) + fail-before |
| Dude | Raise detection F1 | Product-Id merge; refuse grain-invented gaps |
| SA-Bench / LMR / SciReplicate / PaperBench / ReproAgent | Generate / reproduce | Not a generation bench; FI/Miss/\(t_v\) |
| SkillFoundry / Trace→skill | Compile → new skills | Untyped gen. = baseline; gaps relative to *this* \(H\) |
| BIV / Skill Coverage | Package / trajectory vs self | Incoming \(W\) vs deployed \(H\) |
| ViewPoints / TestPrism / OWASP MCP | Multi-view; suite validity; tool connect | Design constraints for Id, destroy-tests, wrap≠\(I\) |

---

## 3. Method

Figure X: dual encoding → typed unit → host projection → \(I\) + fail-before, vs \(W_{\mathrm{rap}}\) / \(P_{\mathrm{aper}}\) on FI, Miss, \(t_v\). Proofs in `research/introduction-operator.md`; design in `docs/typed-introduction.md`.

### 3.1 Dual encoding and product slots

\(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\) when public product names exist, both encodings describe one procedure, and the host surface is enumerable. Materials is instance one; \(\lambda\) does not name phonons.

Unit = one solicit-able product \(p\) (not file/function/sentence):
\[
u=(p,\; s,\; e,\; v_{\mathrm{p}},\; v_{\mathrm{r}},\; \kappa),
\]
with \(s\)/\(e\) = paper procedure / repo entry (citeable loci); \(v_{\mathrm{p}},v_{\mathrm{r}}\) = explicit invalidation; \(\kappa=1\) only if both sides have procedures that are *not* the same computation (requires \(s=e=1\)). Inventories are **independent**; merge by product identity (**Id**). Uncertain Id → no merge; uncertain \(\kappa\) → 0.

**Why product slots.** Sentence–function detectors optimize textual-conflict recall. Introduction needs a grain a host can *own*: add \(p\) to \(P_H\), install \((p,v)\) in \(K_H\), or refuse. Dude’s grain mismatch and SciCoQA’s Paper Omission hardness share a root—code exposes many callables papers need not obligate—so treating every entry as obligation inflates FI under wrap-repo. Product slots refuse that inflation *before* \(\lambda\). ViewPoints: manage inconsistency; unilateral rows stay unilateral until Id is decided.

### 3.2 Type \(\lambda\) (partition)

\[
\lambda(u)=\begin{cases}
\text{incongruent} & s=e=0 \\
\text{obligation-sans-entry} & s=1,\; e=0 \\
\text{entry-sans-obligation} & s=0,\; e=1 \\
\text{procedure-conflict} & s=e=\kappa=1 \\
\text{validity-gap} & s=e=1,\;\kappa=0,\; v_{\mathrm{p}}\neq v_{\mathrm{r}} \\
\text{both-aligned} & s=e=1,\;\kappa=0,\; v_{\mathrm{p}}=v_{\mathrm{r}}.
\end{cases}
\]

**Prop. 1.** Exactly one label per well-formed unit (case on \((s,e)\), then \(\kappa\), then validity). Incongruent units ignored. Without \(\kappa\), conflicts would mislabel as both-aligned and wrongly bind into \(H\).

### 3.3 Coverage fork (insight)

\(\mathrm{Obl}(W)=\{p\mid s=1\}\), \(\mathrm{Ent}(W)=\{p\mid e=1\}\). Projection assigns paper-face / repo-face statuses without editing \(H\). Obligation-sans-entry is `gap` on paper and `absent` on repo; entry-sans-obligation reverses. Hence \(\mathrm{coverage}_{\mathrm{paper}}\) need not equal \(\mathrm{coverage}_{\mathrm{repo}}\). Wrapping every entry improves repo coverage while **hurting** Effective on the paper contract. Mini-ref / phonopy: `qha` and `band` share **no** common missing ids across faces (Figure X(b)). Nearest \(\neq\) covered.

**Mechanism.** Dual encoding is a coverage fork (ReproAgent’s split-spec twin on the generation side; SA-Bench’s drift twin under exec. scaffolds). **MCP-wrapping the companion repo optimizes \(\mathrm{coverage}_{\mathrm{repo}}\) and can strictly worsen FI/Miss whenever omission types are present.** OWASP: connect \(\neq\) own under least privilege.

### 3.4 Operator \(I\) and baselines

| \(\lambda\) | Edit | Fail-before / destroy |
|---|---|---|
| both-aligned | Bind entry; install shared validity if stated | \(p\notin P_H\to p\in P_H\); unbind → red |
| obligation-sans-entry | Host-owned procedure from paper; **no** forged entry | \(p\in P_H\) without fake entry; remove steps → red |
| entry-sans-obligation | **No** edit | Paper tests must not require \(p\) |
| validity-gap | Bind **and** install invalidation check | \(t_v:0\to1\); remove check → 0 |
| procedure-conflict | No silent side-pick; unresolved record | \(P_H\) unchanged |
| incongruent | Ignore | — |

Baselines: \(W_{\mathrm{rap}}\) (every \(e=1\), never \(K_H\)); \(P_{\mathrm{aper}}\) (every \(s=1\), no bind/check); write-directly (no \(\lambda\)); ablation \(\pi\) swaps the two omission types then applies \(I\).

**Faithful.** Theorems assume patches realize the table. We do not prove an LLM writes them—report green-rate **and** destroy still-green (invalid tests \(\neq\) alignment success). Metacognitive “check outputs against findings” failures in AutoResearch-style loops are the obedience risk Faithful names, not a separate benchmark claim.

### 3.5 Why \(\lambda\) selects the edit

Detection says residual *exists*. Typed introduction says *which wrong edit* an untyped policy commits:

- **Prop. 2.** \(I\) adds only \(s=1\) products \(\Rightarrow \mathrm{FI}(I)=0\) (empty start, Faithful).
- **Prop. 3.** \(\mathrm{FI}(W_{\mathrm{rap}})=|\{u:\text{entry-sans-obligation}\}|\), \(\mathrm{Miss}(W_{\mathrm{rap}})=|\{u:\text{obligation-sans-entry}\}|\) (empty start).
- **Prop. 4.** On validity-gap, \(t_v=1\) under \(I\); \(t_v=0\) under \(W_{\mathrm{rap}}\) and \(P_{\mathrm{aper}}\) if check was absent.
- **Prop. 5.** If \(\pi\) swaps omission types and \(\ge 1\) such unit exists, some \(H\) and tests separate \(I\) from \(I\circ\pi\) (non-vacuous ablation).

**Knowledge claim.** SciCoQA-style labels become *edit selectors* with falsifiable counting identities. FI, Miss, and missing validity are separable errors—orthogonal to detection recall and reproduction accuracy.

*Illustrative* empty-host counts on filled phonopy / mini-ref slots (**not** multi-paper EΔ): \(I\): FI\(=0\); \(W_{\mathrm{rap}}\): FI\(=2\) (`band`, `group-velocity`), Miss\(=1\) (`lattice-kappa`); validity-gap rows get \(t_v=1\) only under \(I\). Full EΔ `TODO`.

### 3.6 Fast / Effective / Testable

| Name | Definition |
|---|---|
| FI | Added to \(P_H\) with \(s=0\) |
| Miss | \(s=1\), initially absent, operator did not add (conflicts listed separately) |
| \(t_v\) | Product present **and** invalidation installed |
| **Fast** | Model calls (opt. human edits) until fail-before holds and post-edit passes |
| **Effective** | Per-\(\lambda\) FI, Miss, \(t_v\) (+ deltas) |
| **Testable** | Fail-before ∧ pass-after ∧ fail-on-delete; report still-green-after-delete |

Trustworthiness is destroy-test rate, not “the model said it matches.” Speed is call count to the *same* green contract vs write-directly. Task win-rate without destroy-tests understates invalid suites; call count without FI/Miss understates wrong installs.

---

## 4. Experiments (protocol; results mostly TODO)

Separate **contract counts** (Props. 2–3; decidable from labels + Faithful \(I\)) from **implementation obedience**.

| ID | Question | Status | Floor |
|---|---|---|---|
| **EΔ** | Residual non-empty and \(\lambda\)-typed on same \(W\) | **TODO** (phonopy/mini = illustrations) | ≥1 real pair; independent dual inventories |
| **E1′** | Human IRR on Id / \(\lambda\) / projection | Same-model pilot only; **human TODO** | ≥2 annotators; \(\kappa\) + raw agreement |
| **E2′** | \(I\) vs \(W_{\mathrm{rap}}\) vs \(P_{\mathrm{aper}}\) vs write-directly (+ \(\pi\)) | Typed arms **TODO** | Same labeled units; FI/Miss/\(t_v\) by \(\lambda\) |
| **Fast / Testable** | Calls to green; destroy still-green | **TODO** | Matched tasks; report invalid-test rate |

Legacy same-model IRR may appear in appendix as instrument pilot—not human IRR, not typed Effective.

**Placeholders (do not invent).** Residual mix (EΔ), human IRR (E1′), and arm table (E2′) remain empty except the *illustrative* empty-host phonopy row: \(I\) FI/Miss \(=0/0\), \(t_v=1\) on validity-gap; \(W_{\mathrm{rap}}\) FI/Miss \(=2/1\), \(t_v=0\); \(P_{\mathrm{aper}}\) \(t_v=0\); \(I\circ\pi\) FI/Miss \(=2/1\). Report contract-expected vs realized columns when Faithful may fail. Benchmark pass on fixed tasks does not transfer to unseen introduction settings—another reason E2′ must use held-out works.

---

## 5. Discussion

### 5.1 Three instruments

Detect, reproduce, and introduce answer incompatible targets. Competing on SciCoQA recall or SA-Bench / PaperBench scores is a **category error**: a perfect detector still does not choose host edits; a perfect reproducer may wrap entry-sans-obligation products into \(H\); scalar match can leave the claim unverified. **Community takeaway:** peers need three instruments—(i) discrepancy detectors, (ii) reproduction / semantic-alignment benches, (iii) typed introduction contracts for *already-deployed* hosts. Collapsing (iii) into (i)/(ii) recreates wrap-repo’s FI/Miss identities.

### 5.2 Residual as cause of wrong edits

The fork \(\mathrm{coverage}_{\mathrm{paper}}\neq\mathrm{coverage}_{\mathrm{repo}}\) is the mechanism behind Prop. 3. Toolchains that “just MCP-wrap the companion repo” inherit wrap-repo FI/Miss whenever omission types exist—a systems insight independent of materials jargon. Dude + SciCoQA Paper Omission jointly explain why wrap looks attractive (concrete callables) and why it is unsafe (many callables are not obligations; many obligations lack entries). Dynamic capability expansion can still be right when the *typed* obligation is missing—but expansion must be selected by \(\lambda\), not by entry presence.

### 5.3 Destroy-tests and honest Fast

Fail-before + destroy-tests operationalize trust for LLM patches. Green-only metrics conflate lucky tests with correct installs (TestPrism). Destroy-tests are a local form of the broader *external verifiability* gap in agent harnesses. Always report still-green-after-delete; treat LLM-judge-only green as non-claims until human IRR (Rating Roulette). Fast is defined only vs write-directly on the **same** fail-before suite—otherwise “faster alignment” is process theater.

### 5.4 Failure modes

| Failure | Breaks | Honest handling |
|---|---|---|
| **Id fails** | Invented/split products | No merge; no cross-row residual |
| **\(\kappa\) undecidable** | Conflict vs aligned | \(\kappa=0\); never invent conflict |
| **nearest as covered** | False `host_has` | Log nearest; \(\mathrm{host\_has}=\bot\) |
| **Faithful breaks** | Theorem antecedents | Report obedience; do not cite Prop. 2 as empirical FI\(=0\) |
| **Cross-reading inventories** | Erased residual | Separate passes (write-directly cheats this) |
| **Open-ended chat \(P_H\)** | Non-enumerable surface | Out of scope until freezable |
| **MCP wrap as \(I\)** | FI; privilege confusion | Wrap \(=W_{\mathrm{rap}}\); pin manifests |
| **Usage / nearest as coverage** | False `host_has` | Require product Id; usage \(\neq\) gain |
| **LLM-judge-only Effective** | Self-inconsistent labels | Human IRR; report \(\alpha\) |
| **Judge contamination** | Inflated agreement | Line-bounded reads; disclose |

### 5.5 Domain scope

Require co-holding of public product names, dual encodings of one process, and enumerable host surface. Computational materials is instance one; other domains that satisfy the trio are transfer checks **with \(\lambda\) frozen**—not a license for arbitrary chat agents.

---

## 6. Limitations

(1) Multi-work EΔ beyond illustrative slots incomplete. (2) Existing agreement is same-model pilot, not human IRR. (3) Counting theorems assume Faithful patches—report green-rate and destroy failures. (4) Scope requires product names + dual encoding + enumerable \(H\). (5) No competition on SciCoQA recall or paper→code accuracy. (6) Intra-package drift is context, not headline. (7) Pilot contamination risk → line-bounded protocol. (8) Fixed-task benchmark signals need not transfer to unseen introduction works.

---

## 7. Ethics statement (draft)

Public scientific papers/repos; no personal data. Risks: over-trust without destroy-tests; silent side-pick on procedure-conflict; dual-use wrapping—mitigated by host-owned capability (no nesting a reference agent as runtime). Annotator studies (`TODO`) use public texts and disclose agreement protocols. Slot schemas, guides, and EΔ/E1′/E2′ scripts to be released when runs complete.

---

## 8. Conclusion

We reframed paper–repo residual from a detection target into a **typed introduction contract**: \(\lambda\) selects edits on \(H\) and fail-before tests; wrap-repo and paper-only admit countable FI, Miss, and \(t_v\) failures that \(I\) avoids under Faithful realization. Remaining work is measurement—human IRR, multi-work EΔ, obedience tables—not further taxonomy. Detection and reproduction remain valuable and orthogonal; introduction is the missing third.

---

## Appendix A. Figure X caption

> **Figure X.** Typed introduction for dual-encoded scientific work. (a) Paper and repo slots merge by product identity into \(u\), labeled by unique \(\lambda\). (b) Same \(\lambda\) projects differently on paper vs repo faces—`qha` and `band` share no common missing ids. (c–d) \(I\) maps \(\lambda\) to edits on \(H=(P_H,K_H)\) and fail-before tests; vs \(W_{\mathrm{rap}}\) / \(P_{\mathrm{aper}}\), contractually better on FI, Miss, \(t_v\); Fast / Effective / Testable = call count, those counters, destroy-tests.

## Appendix B. Document map

| Path | Role |
|---|---|
| This file | ACL English draft **v0.3** (compressed + insight-sharpened) |
| [`CHANGELOG-v0.3.md`](CHANGELOG-v0.3.md) | What was cut / woven |
| [`insights-research.md`](insights-research.md) | Bibliography → insight map |
| [`../acl-paper-design.md`](../acl-paper-design.md) | Writing pack / claim scope |
| [`../typed-introduction.md`](../typed-introduction.md) | Design authority |
| [`../../research/introduction-operator.md`](../../research/introduction-operator.md) | Operator proofs |
| [`paper-v0.2-backup.md`](paper-v0.2-backup.md) | Pre-compress snapshot |

## Appendix C. Checklist

- [x] Contributions = typed residual / \(I\) / contract protocol
- [x] RW opens detect vs introduce (SciCoQA); no “better detector”
- [x] Figure X caption has no fake rates
- [x] Experiments mark TODO; illustrative counts labeled non-claim
- [x] Limitations: EΔ, IRR, Faithful, scope, neighbors, transfer
- [x] No eight-step / lattice / intra-package drift as contributions
- [x] Six insight threads retained (fork; product slots; \(\lambda\to I\); failure modes; three instruments; Fast/Effective/Testable)
- [x] Unused research woven: AutoMat claim-unverified; Trace→skill as untyped baseline; Faithful↔metacognitive obedience; benchmark non-transfer; SciReplicate in reproduce cluster
