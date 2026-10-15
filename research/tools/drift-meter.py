#!/usr/bin/env python3
"""Drift meter v0 — claimed vs verified capability surface, per skill.

Research tool for E1/E3 (promise-drift measurement). Zero-dependency (stdlib);
lives in research/tools/ deliberately — NOT part of the skill's runtime (the
skill stays zero-bundle; this is the measurement harness the paper's empirics run).

What it does per SKILL.md:
  1. Parse frontmatter name/description.
  2. Extract claimed tools  (backticked ``mcp__*`` / ``fieldmat_*`` / ``mat_*_`` / tool names)
     and claimed artifact filenames (backticked .json/.csv/.vasp/.traj/.log/.yaml/.xyz),
     split by source: description vs body. Negated sentences (do not / never /
     not available / no local tool / not produced) are excluded.
  3. Verify against a host registry (--registry JSON: {tools: [...], artifacts: [...]}):
       tool/artifact present in registry  -> verified
       absent from registry, no negation  -> drift (declared but unproven)
       absent and the claim sits in a line with no evidence pointer and no
       references/scripts link in the skill -> fabricated (no evidence at all)
  4. Emit per-skill rows + aggregate: drift by source, fabricated share.

Output: JSON to stdout (or --out file) plus a human table on stderr when --table.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

TOOL_RE = re.compile(r"`((?:mcp__[\w.]+|fieldmat_\w+|mat_[\w.]+))`")
ARTIFACT_RE = re.compile(r"`([\w./-]+\.(?:json|csv|vasp|traj|log|yaml|xyz))`")
NEGATION = (
    "do not",
    "never",
    "not available",
    "no local tool",
    "not produced",
    "no registered tool",
    "cannot be invoked",
    "does not",
    "not supported",
    "no longer",
    "not currently",
    "doesn't",
    "not exist",
)


def is_negated(line: str) -> bool:
    low = line.lower()
    return any(phrase in low for phrase in NEGATION)


def extract_frontmatter(text: str) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    end = next((i for i, l in enumerate(lines[1:], 1) if l.strip() == "---"), None)
    if end is None:
        return {}, text
    fm: dict = {}
    for l in lines[1:end]:
        if ":" in l:
            k, _, v = l.partition(":")
            fm[k.strip()] = v.strip().strip("'\"")
    return fm, "\n".join(lines[end + 1 :])


def claims_from(text: str) -> dict:
    tools: dict[str, str] = {}
    artifacts: dict[str, str] = {}
    for lineno, line in enumerate(text.splitlines(), 1):
        if is_negated(line):
            continue
        for m in TOOL_RE.finditer(line):
            tools.setdefault(m.group(1), f"L{lineno}")
        for m in ARTIFACT_RE.finditer(line):
            artifacts.setdefault(m.group(1), f"L{lineno}")
    return {"tools": tools, "artifacts": artifacts, "lines": len(text.splitlines())}


def skill_has_evidence(skill_dir: pathlib.Path, body: str) -> bool:
    has_resources = (skill_dir / "references").is_dir() or (skill_dir / "scripts").is_dir()
    links_ref = "references/" in body or "scripts/" in body
    return has_resources or links_ref


def normalize_claim(claim: str) -> list[str]:
    """mcp__server__tool claims must match either the full name or the bare tool."""
    m = re.fullmatch(r"mcp__(\w+)__(.+)", claim)
    if m:
        return [claim, m.group(2)]
    return [claim]


def scan(skills_root: pathlib.Path, registry: dict | None) -> dict:
    registry_tools = set(registry.get("tools", [])) if registry else set()
    registry_artifacts = set(registry.get("artifacts", [])) if registry else set()
    skills: list[dict] = []
    agg = {"skills": 0, "claims": 0, "verified": 0, "drift": 0, "fabricated": 0,
           "drift_by_source": {"description": {"claims": 0, "verified": 0},
                               "body": {"claims": 0, "verified": 0}}}
    for skill_md in sorted(skills_root.rglob("SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        fm, body = extract_frontmatter(text)
        name = fm.get("name", skill_md.parent.name)
        body_claims = claims_from(body)
        desc_claims = claims_from(fm.get("description", ""))
        combined: dict[str, dict[str, str]] = {"tools": {}, "artifacts": {}}
        for kind in ("tools", "artifacts"):
            merged = dict(desc_claims[kind])
            merged.update(body_claims[kind])
            combined[kind] = merged
        evidence = skill_has_evidence(skill_md.parent, body)
        local_names = {p.name for p in skill_md.parent.rglob("*") if p.is_file()}

        def is_verified(claim: str) -> bool:
            if any(c in registry_tools or c in registry_artifacts
                   for c in normalize_claim(claim)):
                return True
            return claim.split("/")[-1] in local_names  # file present in this skill dir

        all_claims = list(combined["tools"]) + list(combined["artifacts"])
        verified_claims = [c for c in all_claims if is_verified(c)]
        drift_items = [c for c in all_claims if not is_verified(c)]
        fabricated_items = [c for c in drift_items if not evidence]
        per = {
            "name": name,
            "path": str(skill_md),
            "claims": len(all_claims),
            "verified": len(verified_claims),
            "drift": len(drift_items),
            "fabricated": len(fabricated_items),
            "drift_items": drift_items,
            "fabricated_items": fabricated_items,
            "has_evidence": evidence,
        }
        skills.append(per)
        # aggregates
        agg["skills"] += 1
        agg["claims"] += per["claims"]
        agg["verified"] += per["verified"]
        agg["drift"] += per["drift"]
        agg["fabricated"] += per["fabricated"]
        for src, claims in (("description", desc_claims), ("body", body_claims)):
            s = agg["drift_by_source"][src]
            s["claims"] += len(claims["tools"]) + len(claims["artifacts"])
            s["verified"] += sum(
                1 for c in list(claims["tools"]) + list(claims["artifacts"])
                if is_verified(c)
            )
    return {"summary": agg, "skills": skills, "registry_loaded": registry is not None}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("skills_dir", type=pathlib.Path)
    ap.add_argument("--registry", type=pathlib.Path, default=None,
                    help='JSON {"tools": [...], "artifacts": [...]}')
    ap.add_argument("--out", type=pathlib.Path, default=None)
    ap.add_argument("--table", action="store_true")
    args = ap.parse_args()

    registry = None
    if args.registry:
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
    result = scan(args.skills_dir, registry)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"saved: {args.out}")
    else:
        print(text)
    if args.table:
        s = result["summary"]
        drift_rate = s["drift"] / s["claims"] if s["claims"] else 0.0
        fab_rate = s["fabricated"] / s["claims"] if s["claims"] else 0.0
        print(f"\nskills={s['skills']} claims={s['claims']} verified={s['verified']} "
              f"drift={s['drift']} ({drift_rate:.1%}) fabricated={s['fabricated']} ({fab_rate:.1%})",
              file=sys.stderr)
        for src, d in s["drift_by_source"].items():
            r = d["verified"] / d["claims"] if d["claims"] else 1.0
            print(f"  {src:<12} claims={d['claims']} verified={d['verified']} verify_rate={r:.1%}",
                  file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())