# Insights research notes (→ `paper.md` v0.3 (also informed v0.2))

**Date.** 2026-10-18 (Asia/Shanghai).  
**Purpose.** Bibliography + how each source informed ACL-grade insight paragraphs in `paper.md`.  
**Rule.** No invented experimental numbers; AgentRepo borrowings are paraphrased with local paths.

---

## A. Web / ACL–EMNLP neighbors (what they claim → our differential)

| Source | Their claimed insight | How we used it in the draft | Citation |
|---|---|---|---|
| **SciCoQA** | Best LLMs detect only ~46.7% of *real* paper–code discrepancies; Paper Omissions hardest; low recall → *false assurance* | Intro §1.3 takeaway #1; RW §2.1; Discussion 5.1–5.2: detection ≠ introduction | https://aclanthology.org/2026.acl-long.1795/ · arXiv:2601.12910 |
| **Dude** | Single-agent is one-sided; naïve dual-detection raises recall but tanks precision via *granularity asymmetry* (over-interpretation / over-reporting) | Product-slot design constraint; refuse sentence→host-gap inflation; Table 1 row | arXiv:2609.03416 (EMNLP 2026 Main) · https://arxiv.org/html/2609.03416v1 |
| **SA-Bench** | *Semantic drift*; mean SAU ~0.221; scaffolds for executability give limited scientific fidelity; agents attempt then mismatch/stub | Executability ≠ coverage; generation-side twin of coverage fork | arXiv:2608.24252 · https://arxiv.org/html/2608.24252 |
| **ReproAgent** | Specs are *split* (explicit paper obligations vs implicit repo conventions); persist both channels in a generation contract | Sibling “contract” language; Table 1: generation contract ≠ host introduction | arXiv:2608.24291 (Findings EMNLP 2026) |
| **LMR-BENCH** | Paper reproduction with masked functions; incomplete paper understanding & brittle cross-file reasoning dominate failures | RW: reproduce ≠ introduce | https://aclanthology.org/2025.emnlp-main.314/ |
| **SciReplicate-Bench** | Missing/inconsistent algorithm descriptions block reproduction; dual Paper/Code agents | RW neighbor only | arXiv:2504.00255 |
| **PaperBench** | Agents write code but fail integration / execution / result match; early stopping | RW: generation difficulty ≠ host edit contract | arXiv:2504.01848 · ICML 2025 |
| **Rating Roulette** | LLM judges show low *intra-rater* reliability; report Krippendorff’s α, not accuracy alone | §3.6 + Limitations: LLM-judge pilots are lower bounds; E1′ needs human IRR | https://aclanthology.org/2025.findings-emnlp.1361/ |
| **TestPrism** | Single-reference test success (~60%) ≫ Joint Success (~28%); suites must fail initial, accept all valid, reject all invalid | Destroy-test = introduction analogue of Joint Success; §3.6 / Discussion 5.3 | arXiv:2610.12289 |
| **ViewPoints (SE)** | Multi-view requirements may overlap/complement/contradict; consistency is *managed*, not forced | Why product slots: unilateral rows; κ=0 when undecidable | Nuseibeh et al., IEEE TSE 1994 · DOI 10.1109/32.328995 |
| **OWASP MCP** | Tool poisoning, rug pulls, confused deputy; connect ≠ least-privilege capability ownership | MCP-wrap = \(W_{\mathrm{rap}}\) baseline, not \(I\); failure-mode table | https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html |

---

## B. AgentRepo local deep-read (paths → transferable insights)

Inventory focus: `/Users/lwm/workspace/AgentRepo/20_Research/Claims/`, `Topics/Agent-Eval.md`, AI4S / materials notes. PDFs under `Papers/` and `20_Research/Papers/` were used via existing analyzed notes (not re-copied verbatim).

| Local path | Paraphrased claim we borrowed | Where it landed |
|---|---|---|
| `20_Research/Claims/代码执行不等于可靠科学执行.md` | Adding code execution can *hurt* materials reasoning; runnable code ≠ correct scientific procedure | §3.6; Discussion 5.3 |
| `20_Research/Claims/可执行性不是物理建模Agent的停止条件.md` | Stop condition = obligation ledger + evidence binding, not “compiles/simulates” (Pufibara) | §3.6; fail-before framing |
| `20_Research/Claims/使用率不是技能收益的代理指标.md` | Skill usage rate can anti-correlate with gains (SkillFlow) | §1.3 takeaway #2; nearest≠covered |
| `20_Research/Claims/Harness外部可验证性空白.md` | External verifiability largely absent in production harnesses | Discussion 5.3 (destroy-tests as local verifiability) |
| `20_Research/Claims/动态能力扩张是突破静态工具集天花板的关键杠杆.md` | Capability expansion helps when typed obligations are missing—but must be selected, not wrap-all | Discussion 5.2 |
| `20_Research/Claims/Benchmark任务留出下agent配置信号不可迁移.md` | Benchmark pass ≠ generalization to unseen tasks | Soft caution in Limitations mindset (not a new experiment claim) |
| `20_Research/Topics/Agent-Eval.md` → AutoMat note | from-paper near-zero success vs from-artifact; “numbers match, claim unverified” | Discussion 5.1 |
| `20_Research/Topics/Agent-Eval.md` → Skill-Use / Skill Coverage | Trigger/compliance/boundary; coverage adequacy ≠ host coverage of external \(W\) | Table 1 Skill Coverage row kept; nearest≠covered |
| `20_Research/Papers/AI4S_Agent/How_Do_Agents_Fail_on_AutoResearch.md` | Missing metacognitive loop (check outputs against findings) | Soft framing for Faithful/obedience reporting—not copied numbers |
| `Trace2Skill-调研总结.md` / AgentSkill cluster | Trace→skill compilation is *untyped generation* of skills | RW: SkillFoundry/Repo-To-Skill-style as write-directly neighbor |

**Not borrowed as contributions:** AgentRepo harness-evolution scores, SkillFlow point deltas, OmniMatBench CAL numbers—those stay in AgentRepo; we only take *methodological slogans* that reinforce typed introduction without claiming their empirics.

---

## C. Insight upgrades actually written into `paper.md`

1. **§1.3** — three community takeaways (false assurance vs false introduction; executability/usage proxies; destroy-tests ↔ TestPrism Joint Success).  
2. **§2.1 + Table 1** — SciCoQA/Dude precision–recall tension; SA-Bench semantic drift; ReproAgent split-spec; new rows for ReproAgent / TestPrism / ViewPoints.  
3. **§3.1 Why product slots** — Paper Omission ↔ over-reporting; ViewPoints multi-view analogy.  
4. **§3.3** — coverage fork as mechanism; MCP-wrap worsens FI/Miss; OWASP connect≠own.  
5. **§3.6** — TestPrism + Rating Roulette + AgentRepo runnable≠justified.  
6. **§5.1–5.3 + failure table** — three instruments; typed expansion vs wrap-all; external verifiability; MCP / usage / LLM-judge failure modes.  
7. **Appendix B** — link to this notes file; checklist item for citations.

---

## D. Still TODO (do not pretend done)

- EΔ / E1′ human IRR / E2′ arm tables (no numbers invented).  
- Optional: thinner single-column Figure X.  
- Optional: Related Work paragraph citing AutoMat / Pufibara by arXiv once venue IDs are frozen in the .bib.

---

## E. Search / fetch log (high level)

- WebSearch + WebFetch: SciCoQA anthology/HTML, Dude HTML, SA-Bench HTML, ReproAgent HTML, PaperBench HTML, LMR-BENCH, Rating Roulette, TestPrism, MCP OWASP, ViewPoints DOI.  
- Machine `57de027e-…`: recursive inventory of `/Users/lwm/workspace/AgentRepo` (Papers/, 20_Research/Claims/, Topics/Agent-Eval.md, AI4S_Agent notes).


---

## F. v0.3 weave (post-compress)

Items that were notes-only or thin in v0.2 and are now explicit in `paper.md`:

- AutoMat “claim unverified” → §1.2 / §5.1  
- Trace→skill as untyped baseline → RW table  
- SciReplicate in reproduce cluster → §2  
- Faithful ↔ metacognitive obedience (AutoResearch notes) → §3.4  
- Benchmark non-transfer → §4 + Limitations (8)  
- SciCoQA collapse-if-no-\(H\) sentence → §1.2
