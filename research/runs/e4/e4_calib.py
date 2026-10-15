#!/usr/bin/env python3
"""E4 calibration/bias bookkeeping — zero-dependency (stdlib only).

Reads the two E4 run gap tables (self-referential and gold-fed) plus the
capability-level verification ledger produced in the same run, and computes the
E4 headline numbers from research/formal-foundations.md \u00a75:

  drift(H)  = |Claim(H) \u2212 Verified(H)| / |Claim(H)|         (declared but unproven)
  bias      = drift(H_self-reported) \u2212 drift(H_externally-verified)
  cal(l)    = P(conf-label = verified | label = l)
  agreement = gap-table agreement (class / source kind) between the two runs

Tiers: t1 = claim-resolution (carrier artifact + satisfiable input contract),
t2 = strict witness-test (formal-foundations definition).

This script is a measurement ledger, not an alignment run: the gap tables and
the verification ledger are produced by the skill workflow itself (SKILL.md
steps 1\u20137), exactly as documented in e4-run-mini.md.

Usage:
  python3 e4_calib.py \
    --self run1-self-gaps.json \
    --gold run2-gold-gaps.json \
    --ledger verify-ledger.json \
    [--out metrics.json]
"""

from __future__ import annotations

import argparse
import json
import pathlib


LEDGER_KEY = {"t1_claim_resolution": "t1", "t2_witness_test": "t2"}


def drift(claims: list, tier: str) -> dict:
    total = len(claims)
    verified = sum(1 for c in claims if bool(c.get(f"verified_{LEDGER_KEY[tier]}", 0)))
    return {
        "claims": total,
        "verified": verified,
        "unverified": total - verified,
        "drift": (total - verified) / total if total else None,
    }


def cal_by_label(claims: list, tier: str) -> dict:
    by_label: dict[str, list] = {}
    for c in claims:
        by_label.setdefault(c["conf_label"], []).append(c)
    out = {}
    for label, items in sorted(by_label.items()):
        mn = sum(1 for c in items if bool(c.get(f"verified_{LEDGER_KEY[tier]}", 0)))
        out[label] = {"n": len(items), "verified": mn, "pass_rate": mn / len(items)}
    return out


def agreement(a: list, b: list, field: str) -> dict:
    pairs = [(x.get(field), y.get(field)) for x, y in zip(a, b)]
    same = sum(1 for p, q in pairs if p == q)
    return {"compared": len(pairs), "agree": same, "agreement": same / len(pairs)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self", type=pathlib.Path, required=True)
    ap.add_argument("--gold", type=pathlib.Path, required=True)
    ap.add_argument("--ledger", type=pathlib.Path, required=True)
    ap.add_argument("--out", type=pathlib.Path, default=None)
    args = ap.parse_args()

    run1 = json.loads(args.self.read_text(encoding="utf-8"))
    run2 = json.loads(args.gold.read_text(encoding="utf-8"))
    ledger = json.loads(args.ledger.read_text(encoding="utf-8"))

    claims = ledger["positive_claims"]
    tiers = ["t1_claim_resolution", "t2_witness_test"]

    result = {
        "runs": {"self": run1["run_id"], "gold": run2["run_id"]},
        "drift": {
            tier: {
                "self": drift(claims, tier),
                "gold": drift(claims, tier),  # same frozen artifact tree by construction
            }
            for tier in tiers
        },
        "bias": {tier: None for tier in tiers},
        "cal": {tier: cal_by_label(claims, tier) for tier in tiers},
        "gap_agreement": {
            "class": agreement(run1["gaps"], run2["gaps"], "class"),
            "source_kind": agreement(run1["gaps"], run2["gaps"], "source_kind"),
            "host_id": agreement(run1["gaps"], run2["gaps"], "host_id"),
        },
        "negative_reports": {
            "total": ledger["negative_reports"]["total"],
            "accurate": ledger["negative_reports"]["accurate"],
            "accuracy": ledger["negative_reports"]["accurate"] / ledger["negative_reports"]["total"],
        },
        "unverified_self_reported": [
            {"id": c["id"], "claim": c["claim"], "conf_label": c["conf_label"],
             "evidence": c["carrier"], "tier1_verdict": bool(c.get("verified_t1", 0)),
             "tier2_verdict": bool(c.get("verified_t2", 0)),
             "fail_reason": c["fail_reason"]}
            for c in claims
            if not bool(c.get("verified_t1", 0))
        ],
        "ledger_rows": [
            {"id": c["id"], "claim": c["claim"], "conf_label": c["conf_label"],
             "verified_t1": bool(c.get("verified_t1", 0)),
             "verified_t2": bool(c.get("verified_t2", 0))}
            for c in claims
        ],
        "conf_labels_present": ledger["conf_labels_present"],
        "caveats": "mini-scale, non-conclusive: n=4 host claims, single conf label, fixture seeds honest AUDIT admissions; no claim-source diversity",
    }
    for tier in tiers:
        d1 = result["drift"][tier]["self"]["drift"]
        d2 = result["drift"][tier]["gold"]["drift"]
        if d1 is not None and d2 is not None:
            result["bias"][tier] = d1 - d2

    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"saved: {args.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())