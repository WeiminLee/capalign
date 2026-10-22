# Quick decisions — the card for a live run

Read this first; it is the whole method in the order a run needs it. The detailed
rules are in the reference files named at each line.

1. **What counts as one capability?** A procedure a user runs — not a module, a
   class, a CLI subcommand, a mesh/solver/viewer, or a config file. A library is
   inventoried as workflows; its modules are evidence pointers. A roster of N
   models is one `interface`. Target ~10–30 capabilities for a typical repo; much
   more means over-splitting, much less means over-collapsing.
   (`capability-ir.md` §Granularity boundary.)

2. **What must the host own?** Ask before calling anything `missing`:
   `data` / `contract` / `runner` / `verification`, or `none`. `none` plus a
   `local_check` (form: analytic / conservation / limit; status: named /
   demonstrated) is `agent-competence` — no card. Every non-`none` need carries a
   note; `verification` names the regime, the missing check, and the owning layer
   (gate / runner / skill-body). (`alignment-rules.md` §Agent competence,
   §Host-need evidence.)

3. **What did the source actually say?** Slots are tri-state:
   `1` = stated (quote required), `0` = inspected and silent (`why_empty`),
   `unknown` = could not inspect (`why_unknown`). `s`/`v_p` come from the paper,
   `e`/`v_r` from the repo; `none` only when the arm does not exist. Unknown is
   never 0. (`introduction-card.md` §What opens a row.)

4. **Which label?**
   `s=e=0` → ignore · `s=1,e=0` → install · `s=0,e=1` → refuse ·
   `s=e=κ=1` → refuse (conflict) · `s=e=1,v_p≠v_r` → install (validity gap) ·
   `s=e=1,v_p=v_r` → install · `s`/`e` unknown → **no card, row `unknown`** ·
   `s=e=1`, a `v` unknown → install with `bind` only (`validity-unassessed`).
   (`introduction-card.md` §Label.)

5. **Where does it land?** Axis (skill / tool / script / runner) → tool vs script
   (shared consumer or gate/render/audit) → extend vs new skill (same input
   contract + adjacent problem class ⇒ extend, three lines + one reference page;
   independent trigger or different contract ⇒ new skill) → constraint owner →
   host-owned (rule 6: never clone/wrap/MCP the reference agent/hub; calling an
   upstream scientific engine is allowed, report its license).
   (`alignment-rules.md` §Placement.)

6. **What proves the card?** Three beats: `fail_before` = the agent's wrong
   judgement without the skill (not a missing entry point); `pass_after` = right
   on a prompt that does not name the skill or entry point; `destroy` = remove
   the prescribed primitive named by the card and the test turns red. Skill cards and extend cards
   also need routing cases (positive + must-not-absorb negative).
   (`introduction-card.md` §Test contract.)

7. **What must never be skipped?** Unknown handling, host-need evidence, the
   tri-state slot recompute, the fork recompute, verification honesty, and the
   independent re-check. All 18 checks are in `evaluation.md`; validity rules and
   the JSON shape are in `report-contract.md` / `report-schema.json`.
