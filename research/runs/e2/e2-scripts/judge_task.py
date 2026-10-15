#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E2 task judge — deterministic, zero-bundle (stdlib only).

Implements the task-suite judging contract (task-suite.md §Judgement):

  mode gold : exit code 0 + declared output files exist + every output file
              deep-compares against the task gold file (numeric tolerance
              atol/tol, non-numeric equality).
  mode cmd  : exit code 0 + the given regex matches (stdout, or a named
              output file).
  no runner : verdict `skip` (arm-c control: no staged artifact).

Blindness discipline: the judge consumes ONLY (task, runner, input, gold) — it
never sees an arm label. The caller routes arm artifacts to --runner.

Usage:
  python3 judge_task.py --task t-id --mode gold --runner A.py \
      --input in.json --gold gold.json --output-files band.json \
      --out verdict.json [--tolerance 1e-6] [--timeout 30]
  python3 judge_task.py --task t-id --mode cmd --runner A.py \
      --input in.json --cmd-pattern '^OK .*' --out verdict.json
"""
import argparse
import collections
import json
import math
import os
import re
import subprocess
import sys
import tempfile


def _num_close(a, b, tol):
    return math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol)


def deep_close(a, b, tol, path="$"):
    """Structural equality; numbers compared with tolerances. Returns (ok, diff)."""
    if isinstance(a, bool) or isinstance(b, bool):
        if type(a) is type(b) and a == b:
            return True, ""
        return False, f"{path}: bool mismatch {a!r} vs {b!r}"
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if _num_close(a, b, tol):
            return True, ""
        return False, f"{path}: {a!r} vs {b!r} (out of tol {tol})"
    if isinstance(a, str) and isinstance(b, str):
        if a == b:
            return True, ""
        return False, f"{path}: string mismatch {a!r} vs {b!r}"
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False, f"{path}: list length {len(a)} vs {len(b)}"
        for i, (x, y) in enumerate(zip(a, b)):
            ok, d = deep_close(x, y, tol, f"{path}[{i}]")
            if not ok:
                return False, d
        return True, ""
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a) != set(b):
            return False, f"{path}: key sets differ {sorted(a)} vs {sorted(b)}"
        for k in a:
            ok, d = deep_close(a[k], b[k], tol, f"{path}.{k}")
            if not ok:
                return False, d
        return True, ""
    if a == b:
        return True, ""
    return False, f"{path}: {a!r} vs {b!r}"


def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def sandbox_run(runner, task_input, sandbox, timeout):
    """Run [python3 runner task_input] with cwd=sandbox. Returns (exit, out, err)."""
    proc = subprocess.run(
        [sys.executable, os.path.abspath(runner), os.path.abspath(task_input)],
        cwd=sandbox,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return proc.returncode, proc.stdout, proc.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--mode", choices=["gold", "cmd"], required=True)
    ap.add_argument("--runner", required=True)
    ap.add_argument("--input", required=True)
    ap.add_argument("--gold")
    ap.add_argument("--output-files", default="")
    ap.add_argument("--cmd-pattern")
    ap.add_argument("--tolerance", type=float, default=1e-6)
    ap.add_argument("--timeout", type=int, default=30)
    ap.add_argument("--out", required=True)
    ap.add_argument("--sandbox", default="")
    args = ap.parse_args()

    base = {
        "task": args.task,
        "mode": args.mode,
        "verdict": "skip",
        "reasons": [],
    }

    if not os.path.exists(args.runner):
        base["reasons"].append("no runner (artifact absent) -> skip")
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(base, f, indent=2)
        print(json.dumps(base, ensure_ascii=False))
        return 0

    if args.sandbox:
        os.makedirs(args.sandbox, exist_ok=True)
        sandbox = args.sandbox
    else:
        sandbox = tempfile.mkdtemp(prefix=f"e2-{args.task}-")

    try:
        exit_code, stdout, stderr = sandbox_run(args.runner, args.input, sandbox, args.timeout)
    except subprocess.TimeoutExpired:
        base["verdict"] = "fail"
        base["reasons"].append(f"timeout > {args.timeout}s")
        _write(base, stdout="", stderr="", exit_code=None, args=args)
        return 0

    base["exit_code"] = exit_code
    base["stdout_tail"] = stdout[-2000:]

    if exit_code != 0:
        base["verdict"] = "fail"
        base["reasons"].append(f"non-zero exit {exit_code}")

    if args.mode == "cmd":
        pattern = args.cmd_pattern or "OK"
        if base["verdict"] == "skip" and not base.get("reasons"):
            base["verdict"] = "pass" if re.search(pattern, stdout) else "fail"
            base["reasons"].append(
                f"cmd-pattern {pattern!r} {'matched' if base['verdict'] == 'pass' else 'not found'}"
            )
        else:
            if re.search(pattern, stdout):
                base["reasons"].append(f"cmd-pattern {pattern!r} matched")
            else:
                base["verdict"] = "fail"
                base["reasons"].append(f"cmd-pattern {pattern!r} not found in stdout")
    else:  # gold
        expected = [x for x in args.output_files.split(",") if x]
        missing = [x for x in expected if not os.path.exists(os.path.join(sandbox, x))]
        if missing:
            base["verdict"] = "fail"
            base["reasons"].append(f"missing output file(s): {missing}")
        else:
            try:
                if args.gold:
                    gold = read_json(args.gold) if os.path.exists(args.gold) else json.loads(args.gold)
                else:
                    gold = None
            except Exception as e:  # noqa: BLE001
                base["verdict"] = "fail"
                base["reasons"].append(f"gold unreadable: {e}")
                _write(base, stdout=stdout, stderr=stderr, exit_code=exit_code, args=args)
                return 0
            all_pass = base["verdict"] != "fail"
            for name in expected:
                try:
                    produced = read_json(os.path.join(sandbox, name))
                except Exception as e:  # noqa: BLE001
                    all_pass = False
                    base["reasons"].append(f"{name}: unparsable ({e})")
                    continue
                ok, diff = deep_close(produced, gold[name], args.tolerance)
                if not ok:
                    all_pass = False
                    base["reasons"].append(f"{name}: gold mismatch — {diff}")
            if all_pass:
                base["verdict"] = "pass"
                base["reasons"].append(f"gold compare OK ({len(expected)} file(s))")

    _write(base, stdout=stdout, stderr=stderr, exit_code=exit_code, args=args)
    return 0


def _write(base, stdout, stderr, exit_code, args):
    base["exit_code"] = exit_code if exit_code is not None else base.get("exit_code")
    if stderr:
        base["stderr_tail"] = stderr[-800:]
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(base, f, indent=2)
    print(json.dumps(base, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())