#!/usr/bin/env python3
"""Build a K-Dense verification registry for drift-meter (E3 study 1 static part).

K-Dense has NO MatDiscovery-style registry (no @mcp.tool() defs, no runner-
tuple constants file). Its genuine verification surface is structural:
  - `scripts/*.py`  — executable helpers; **filename literals inside them are
    the analog of MatDiscovery's fieldmat-runners artifact registry**
    (e.g. pycalphad's equilibrate.py writes "report.json" and
    "phase-equilibria.csv", exactly the names SKILL.md claims).
  - shipped files under the skill dir (assets/ templates, scripts/, references/)
    — NOT registered here; drift-meter already resolves those via its
    file-present-in-skill-dir fallback.

This script registers only the scripts-product surface, with per-entry
provenance (which script each name was scraped from) so the crafted registry
is auditable. Tools tier is intentionally empty: K-Dense tool claims are
package/CLI/script names that drift-meter's MatDiscovery-bound TOOL_RE
(mcp__* / fieldmat_* / mat_*) does not extract — documented in e3-static.md
as a measurement-interface mismatch, not as "K-Dense has no tools".

Zero-dependency (stdlib only). Usage:
  python3 build-kdense-registry.py <kdense-repo> --out kdense-registry.json
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re

# Same artifact extension set drift-meter counts claims on, so the registry
# can only verify claims the meter can see.
LITERAL_RE = re.compile(r"[\"']([\w./-]+\.(?:json|csv|vasp|traj|log|yaml|xyz))[\"']")


def is_external(name: str) -> bool:
    """URL-ish or clearly non-local literals are not host products."""
    return "://" in name or name.startswith("http")


def scrape(root: pathlib.Path) -> dict:
    artifacts: set[str] = set()
    provenance: dict[str, list[str]] = {}
    for script in sorted(root.joinpath("skills").glob("*/scripts/**/*.py")):
        # same isolation rules the repo applies: skip vendored/test scaffolding
        if "tests" in script.parts or "site-packages" in script.parts:
            continue
        text = script.read_text(encoding="utf-8", errors="ignore")
        for m in LITERAL_RE.finditer(text):
            name = m.group(1)
            if is_external(name):
                continue
            # strip a leading "./" so "phase-equilibria.csv" matches claims
            rel = name[2:] if name.startswith("./") else name
            if not rel or rel.startswith("."):
                continue  # ".metadata.json"-style globals excluded, dotfile noise
            artifacts.add(rel)
            provenance.setdefault(rel, []).append(str(script))
    return {"tools": [], "artifacts": sorted(artifacts), "_provenance": provenance}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("kdense_repo", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path, default=None)
    args = ap.parse_args()
    reg = scrape(args.kdense_repo)
    text = json.dumps(reg, ensure_ascii=False, indent=1)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"saved: {args.out} (tools={len(reg['tools'])}, "
              f"artifacts={len(reg['artifacts'])}, "
              f"provenance_sources={len(set(s for v in reg['_provenance'].values() for s in v))})")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())