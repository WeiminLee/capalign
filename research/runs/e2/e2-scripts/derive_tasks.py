#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structurally validates and registers the E2 task suite (task-suite.md).

One table of truth: `task-suite.csv` (6 columns, header row). This script
enforces the suite contract from e2-protocol.md Phase 3:

  * unique kebab-case ids; tier in {mini, real}
  * every row carries a non-empty expected-output and a judge method
  * judge method in {gold, cmd, judge}
  * real tier: >= 20 rows; doc_path exists (evidence the task derives from the
    reference docs feature surface); < 30% of rows are primary `judge`
  * mini tier: input_path and gold exist now (pipeline smoke tier)

Usage:
  python3 derive_tasks.py e2-assets/task-suite.csv [--ref-doc-root /Users/lwm/code/phonopy/doc]
Exit 0 when the suite is valid; non-zero prints the violated rules.
"""
import argparse
import csv
import os
import re
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    ap.add_argument("--ref-doc-root", default="")
    args = ap.parse_args()

    errors = []
    rows = []
    with open(args.csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            r = {k.strip(): (v.strip() if v else "") for k, v in r.items()}
            rows.append(r)

    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        dup = sorted({i for i in ids if ids.count(i) > 1})
        errors.append(f"duplicate ids: {dup}")
    for r in rows:
        ident = r.get("id", "")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]{2,}", ident):
            errors.append(f"{ident}: id not kebab-case slug")
        if r.get("tier") not in ("mini", "real"):
            errors.append(f"{ident}: tier must be mini|real, got {r.get('tier')}")
        if r.get("judge_method") not in ("gold", "cmd", "judge"):
            errors.append(f"{ident}: judge_method must be gold|cmd|judge, got {r.get('judge_method')}")
        if not r.get("expected_output"):
            errors.append(f"{ident}: empty expected_output (not decidable)")
        if r.get("tier") == "mini":
            if not r.get("input_path") or not os.path.exists(r.get("input_path", "")):
                errors.append(f"{ident}: mini tier input_path must exist now, got {r.get('input_path')}")
            for g in (r.get("gold_path", "") or "").split(";"):
                if g and not os.path.exists(g):
                    errors.append(f"{ident}: mini gold_path missing: {g}")

    real = [r for r in rows if r.get("tier") == "real"]
    if len(real) < 20:
        errors.append(f"real tier has {len(real)} rows; need >= 20")

    if args.ref_doc_root:
        for r in real:
            p = r.get("doc_path", "")
            if not p:
                errors.append(f"{r.get('id')}: real tier doc_path missing")
                continue
            if not os.path.exists(os.path.join(args.ref_doc_root, p)):
                errors.append(f"{r.get('id')}: doc_path not found under ref docs: {p}")

    judge_rows = [r for r in real if r.get("judge_method") == "judge"]
    share = len(judge_rows) / len(real) if real else 0.0
    if share >= 0.30:
        errors.append(
            f"real tier judge-needed share {share:.2f} >= 0.30 "
            f"({len(judge_rows)}/{len(real)}); the protocol caps primary-judge rows at 30%"
        )

    if errors:
        print("suite INVALID")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(
        f"suite OK: {len(rows)} rows total, {len(real)} real-tier "
        f"(judge-needed {len(judge_rows)}/{len(real)} = {share:.0%}), "
        f"{len([r for r in rows if r.get('tier')=='mini'])} mini-tier"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())