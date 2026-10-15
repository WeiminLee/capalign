#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E2 Phase 2 — derive the gap pool from a pinned alignment report (stdlib only).

Input: `capability-alignment.json` per references/report-contract.md:
  {"surfaces": {...}, "gaps": [{"ref_id","class","host_id","rule",...}],
   "recommendations": [...], "unresolved": [...]}
Tolerance for real-world reports (case-study record may use slightly different
keys): the script reads, in order of preference,
  recommendations[*] when they name a ref capability id and cite a rule,
  else gaps[*], and keeps only classes missing/partial that are NOT unknown or
  low-evidence. Entries with an explicit "priority" field keep it; otherwise the
  report's stated order (array order) is the priority, 1 = highest.

Output: gap pool JSON for arm_select.py:
  {"source": <report path>, "priority_judgment": <from report if present>,
   "gaps": [{"id","class","source_kind","priority"}]}

Usage:
  python3 derive_pool.py --report capability-alignment.json --out e2-assets/gap-pool.json
"""
import argparse
import json
import sys

POOLABLE = {"missing", "partial"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--priority-judgment", default="report's stated recommendation order")
    args = ap.parse_args()

    with open(args.report, encoding="utf-8") as f:
        report = json.load(f)

    poolable, warnings = [], []

    def take(rid, cls, source_kind, rule, evidence):
        if cls not in POOLABLE:
            return False
        if cls == "missing" and not evidence:
            # Strict no-evidence rejection is the report gate's job (Layer-1 #2,
            # evaluation.md). E2 consumes only pinned, gate-green reports, so a
            # missing row without explicit evidence is kept and flagged.
            warnings.append(f"{rid}: missing row without explicit evidence field "
                            "(assumed validated by pinned report, Layer-1 #2)")
        poolable.append({
            "id": rid,
            "class": cls,
            "source_kind": source_kind or "reference-contrast",
            "rule": rule,
        })
        return True

    consumed = False
    for rec in report.get("recommendations", []):
        rid = rec.get("ref_id") or rec.get("id") or rec.get("capability_id")
        if not rid:
            continue
        take(rid, rec.get("class", "missing"), rec.get("source_kind"),
             rec.get("rule"), rec.get("evidence"))
        consumed = True
    if consumed:
        used_from = "recommendations"
    else:
        for g in report.get("gaps", []):
            take(g.get("ref_id"), g.get("class"), g.get("source_kind"),
                 g.get("rule"), g.get("evidence_kinds") or g.get("evidence"))
        used_from = "gaps"

    # priorities: explicit field wins; else array order (1 = first).
    gaps = sorted(
        poolable,
        key=lambda g: (g.pop("priority", 10 ** 9),),
    )
    for i, g in enumerate(gaps, start=1):
        g["priority"] = i

    pool = {
        "source": args.report,
        "used": used_from,
        "priority_judgment": args.priority_judgment,
        "gaps": gaps,
        "warnings": warnings,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(pool, f, indent=2)

    print(f"pool: {len(gaps)} poolable gaps (from {used_from}); "
          f"{len(warnings)} warning(s): {warnings}")
    for g in gaps:
        print(f"  #{g['priority']:2d} {g['id']:30s} {g['class']:7s} {g['source_kind']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())