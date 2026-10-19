# Abstract (draft v0.4 — locked C1–C3)

**Aligned with:** `docs/acl-paper-design.md` §0–§1.2 **DECIDED** (2026-10-18);
`docs/acl-draft/innovation-proposals.md`.  
Supersedes v0.3 contribution *wording* (lead was “typed residual / six λ”);
operator \(\lambda\to I\) unchanged. Skill may still stop at recommendations;
manuscript claim is coverage fork + refusal + \(K_H\)/\(t_v\).

Scientific agents and scientific papers arrive on different schedules. A user who
already runs a host agent \(H\) and faces a new dual-encoded work
\(W=(W_{\mathrm{paper}},W_{\mathrm{repo}})\) needs more than a discrepancy
detector: the two faces can induce *disjoint* host-gap sets (coverage fork), so a
policy that collapses to wrap-repo or paper-only is contractually wrong on false
introduction (FI) or missed obligations (Miss). We merge paper and companion-repo
slots by product identity into units \(u\), partition residual by unique
\(\lambda\), and define typed introduction operator \(I\) that maps \(\lambda\)
to edits on \(H=(P_H,K_H)\) *or* to principled non-introduction (entry-sans-
obligation / procedure-conflict / incongruent), installing validity checks into
\(K_H\) when invalidation is one-sided (\(t_v\)). Relative to wrap-repo,
paper-only, and write-directly, counting statements show \(\mathrm{FI}(I)=0\),
wrap-repo FI/Miss equal omission-type counts, and wrap-repo/paper-only leave
\(t_v=0\) on validity-gap units. Acceptance uses fail-before / destroy-tests;
Fast (call count) is reported only when measured. Materials agents are the first
instance domain; the type set is frozen. We do not claim detection SOTA against
SciCoQA, nor paper→code execution SOTA. Multi-work residual measurement, human
IRR, and arm-wise implementation tables remain TODO.

**Keywords:** scientific agents; dual-encoded specifications; coverage fork;
typed introduction; principled refusal; validity checks; fail-before tests;
host-relative coverage.
