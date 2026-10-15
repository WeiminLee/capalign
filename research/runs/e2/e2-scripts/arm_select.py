#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E2 arm selection — deterministic, zero-bundle (stdlib only).

Arm (a): report-ordered prefix of the gap pool (priority = the pinned alignment
report's stated recommendation order, 1 = highest priority).
Arm (b): the same number k of gaps sampled WITHOUT replacement from the pool,
          seeded (random.Random(seed)) — reproducible across re-runs.
Arm (c): empty selection (no assembly).

Usage:
  python3 arm_select.py --pool POOL.json --k K [--seed SEED] --mode top
  python3 arm_select.py --pool POOL.json --k K [--seed SEED] --mode random
  python3 arm_select.py --pool POOL.json --k K --mode none

POOL.json shape (produced at E2 Phase 2 from the pinned report's
missing/partial recommendations):
  {"gaps": [{"id": "...", "class": "missing|partial",
             "source_kind": "host-self-audit|reference-contrast|domain-inference",
             "priority": 1, ...}]}
`priority` is the report's own recommendation order (1 = fix first).
If a pool entry lacks `priority`, order = list order.
"""
import argparse
import json
import random
import sys


def load_pool(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    gaps = list(data.get("gaps", []))
    if not gaps:
        sys.exit("error: pool has no gaps")
    ids = [g["id"] for g in gaps]
    if len(set(ids)) != len(ids):
        sys.exit("error: pool contains duplicate gap ids")
    return gaps


def ordered_ids(gaps):
    def sort_key(g):
        return (g.get("priority", 999), )
    seen = set()
    out = []
    for g in sorted(gaps, key=sort_key):
        if g["id"] not in seen:
            seen.add(g["id"])
            out.append(g["id"])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pool", required=True)
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--mode", choices=["top", "random", "none"], required=True)
    args = ap.parse_args()

    gaps = load_pool(args.pool)
    n = len(gaps)
    k = min(args.k, n)

    if args.mode == "top":
        selected = ordered_ids(gaps)[:k]
        label = "report-ordered (arm a)"
    elif args.mode == "random":
        rng = random.Random(args.seed)
        selected = rng.sample(ordered_ids(gaps), k)  # randomized order, no replacement
        label = "random (arm b)"
    else:
        selected = []
        label = "none (arm c)"

    manifest = {
        "mode": args.mode,
        "label": label,
        "pool_size": n,
        "k": k,
        "seed": args.seed,
        "selected": selected,
        "unselected": [g["id"] for g in gaps if g["id"] not in selected],
    }
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()