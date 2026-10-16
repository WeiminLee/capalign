# Skill failures from oh-my-mlip × MatDiscovery (2026-10-16)

Real run. These are method bugs, not instance quirks. Patched into
`SKILL.md` / `inventory-heuristics.md` / `capability-ir.md` / `report-contract.md`.

| # | Failure | What happened | Rule now |
|---|---|---|---|
| F4 | Unbounded host `SKILL.md` scan | `find SKILL.md` on MatDiscovery → **174** files (worktrees, dsh copies). Doctrine skill root is **37**. | §D: read host doctrine first; default-exclude worktrees / node_modules / `.git` / plugin caches. |
| F5 | Homepage+repo as two inputs | Caller gave `oh-my-mlip.org` and the GitHub clone. Skill only started from "a repo". | Phase 0: a homepage URL and a repo path of the same work are one W. Do not search for a homepage already given. |
| F6 | Software-only CITATION forced search | No `preferred-citation`. Old §E said "no paper → search necessary". Query hit unrelated "MLIP" papers. | `type: software` without an article citation ⇒ companion paper absent. At most one identity-gated query; keyword collisions rejected. |
| F7 | Roster exploded into N capabilities / N neighbors | 20 frameworks / 32 models. Granularity bound is ~10–30 **user verbs**, not the catalog. | A registry is one `interface` capability. Driven frameworks are payload, not neighborhood. |
| F8 | Reference-side `skills/` ignored | oh-my-mlip's primary UX is five agent skills. §A only listed CLI/modules/docs. | §A: reference `skills/*/SKILL.md` are capabilities; merge with the same documented verb. |
| F9 | Report path would clobber the host | MatDiscovery already has a phonopy `capability-alignment-report.md`. Skill said "workspace root". | Write in the **caller's cwd** (or `research/runs/<pair>/`). If an existing report has different `surfaces`, namespace the filename. Never overwrite another (H,W). |
