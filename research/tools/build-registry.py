#!/usr/bin/env python3
"""Build a host capability registry from a code tree (drift-meter input).

Zero-dependency. Scans a MatDiscovery-style repo for the verification surface:
  - tools:      `@mcp.tool()` defs in tools/*/src, `name: '...'` in
                plugins/*/src/*-tools.ts, fieldmat_* literals, mcp__server__tool
                literals in plugins/matdiscovery/src
  - artifacts:  filename literals (*.json/csv/vasp/traj/log/yaml) in
                plugins/matdiscovery/fieldmat-runners/*.py

Usage:
  python3 build-registry.py <repo-root> [--out registry.json]
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re


def scrape(root: pathlib.Path) -> dict:
    tools: set[str] = set()
    artifacts: set[str] = set()

    for p in root.joinpath("tools").rglob("*.py"):
        if "src" not in p.parts or "site-packages" in str(p):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        tools.update(re.findall(r"@mcp\.tool\(\)\s*\ndef\s+(\w+)\(", text))

    for p in root.joinpath("plugins/matdiscovery/src").rglob("*-tools.ts"):
        text = p.read_text(encoding="utf-8", errors="ignore")
        tools.update(re.findall(r"name:\s*'([a-z_]+)'", text))

    for p in root.joinpath("plugins/matdiscovery/src").glob("*.ts"):
        text = p.read_text(encoding="utf-8", errors="ignore")
        tools.update(re.findall(r"'(fieldmat_\w+)'", text))
        tools.update(m.strip("'") for m in re.findall(r"'mcp__[\w.]+__[\w.]+'", text))

    for p in root.joinpath("plugins/matdiscovery/fieldmat-runners").glob("*.py"):
        text = p.read_text(encoding="utf-8", errors="ignore")
        artifacts.update(
            re.findall(r"[\"']([\w./-]+\.(?:json|csv|vasp|traj|log|yaml))[\"']", text)
        )

    tools = {t for t in tools if not t.startswith(("__", "test_"))}
    return {"tools": sorted(tools), "artifacts": sorted(artifacts)}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("repo_root", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path, default=None)
    args = ap.parse_args()
    reg = scrape(args.repo_root)
    text = json.dumps(reg, ensure_ascii=False, indent=1)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"saved: {args.out} (tools={len(reg['tools'])}, artifacts={len(reg['artifacts'])})")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())