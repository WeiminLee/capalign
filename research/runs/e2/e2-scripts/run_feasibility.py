#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""E2 feasibility drive — pipeline smoke, zero-bundle (stdlib only).

What this does (NOT a measurement — a mechanism check of the E2 harness):
  1. generate mini-fixture inputs + golds for 3 tasks derived from the reference
     docs feature surface (mini-ref fixture); gold provenance logged.
  2. build the gap pool from the tracked fixture gold
     (tests/fixtures/gold/mini-ref-vs-mini-host.json) and run the REAL
     arm_select.py in three modes: top (arm-a), seeded random (arm-b), none
     (arm-c).
  3. stage one artifact per selected gap (identical template quality), execute
     each suite task per arm through judge_task.py, print the verdict table.
  4. judge controls: a conforming artifact (pass), a contract-violating
     artifact (fail), determinism re-run — plus suite validation.

Run from research/runs/e2:
  python3 e2-scripts/run_feasibility.py
Writes: e2-assets/fixtures/mini/*, e2-assets/gold/mini/*, e2-assets/gap-pool-mini.json,
        e2-runs/feasibility-<n>/
"""
import json
import math
import os
import shutil
import subprocess
import sys
import time

E2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../runs/e2
CAP_ALIGN = os.path.dirname(os.path.dirname(os.path.dirname(E2)))
GOLD_FIXTURE = os.path.join(CAP_ALIGN, "tests/fixtures/gold/mini-ref-vs-mini-host.json")
FIX_DIR = os.path.join(E2, "e2-assets/fixtures/mini")
GOLD_DIR = os.path.join(E2, "e2-assets/gold/mini")
POOL_PATH = os.path.join(E2, "e2-assets/gap-pool-mini.json")
RUNS_DIR = os.path.join(E2, "e2-runs")
ARM_SELECT = os.path.join(E2, "e2-scripts", "arm_select.py")
JUDGE = os.path.join(E2, "e2-scripts", "judge_task.py")
DERIVE = os.path.join(E2, "e2-scripts", "derive_tasks.py")
PHONOPY_DOC = os.path.join(CAP_ALIGN, "..", "phonopy", "doc")  # symlink-free read root
PHONOPY_DOC = os.path.realpath(PHONOPY_DOC)

# ---------------------------------------------------------------- fixtures --
ROOT2 = math.sqrt(2.0)


def gen_fixtures():
    os.makedirs(FIX_DIR, exist_ok=True)
    fc = [[[[2.0 if a == c else 0.0 for c in range(3)] for _ in range(3)] for _ in range(1)] for a in range(1)]
    # fc[0][0][a][c] = 2.0 on diagonal (k = 2.0, mass = 1.0 -> w = sqrt(2))
    masses = [1.0]
    qpoints = [[0.0, 0.0, 0.0], [0.5, 0.0, 0.0]]
    freqs = [ROOT2, ROOT2, ROOT2]

    files = {
        "band_input.json": {"force_constants": fc, "masses": masses, "qpoints": qpoints},
        "dos_input.json": {"frequencies": freqs, "sigma": 0.05, "fmin": 0.0, "fmax": 3.0, "fpitch": 0.05},
        "thermo_input.json": {"frequencies": freqs, "tmin": 1.0, "tmax": 5.0, "tstep": 0.5},
        "dyn_input.json": {"force_constants": fc, "masses": masses, "qpoints": qpoints},
        "fc_input.json": {
            "atoms": 1,
            "displacements": [[[0.01, 0, 0]], [[0, 0.01, 0]], [[0, 0, 0.01]]],
            "forces": [[[-0.02, 0, 0]], [[0, -0.02, 0]], [[0, 0, -0.02]]],
        },
    }
    for name, data in files.items():
        with open(os.path.join(FIX_DIR, name), "w", encoding="utf-8") as f:
            json.dump(data, f)
    return fc, masses, qpoints, freqs


def gold_band(fc, masses, qpoints):
    k = fc[0][0][0][0]
    w = math.sqrt(abs(k) / masses[0])
    return {"qpoints": qpoints, "frequencies": [[w, w, w] for _ in qpoints]}


def gold_dos(freqs, sigma, fmin, fmax, fpitch):
    # Gaussian-broadened DOS, normalization 1/(sigma*sqrt(2*pi)) — matches doc
    norm = 1.0 / (sigma * math.sqrt(2.0 * math.pi))
    grid, dos = [], []
    x = fmin
    while x <= fmax + 1e-12:
        s = 0.0
        for w in freqs:
            s += math.exp(-((x - w) ** 2) / (2.0 * sigma * sigma)) * norm
        grid.append(x)
        dos.append(s)
        x = round(x + fpitch, 12)
    return {"grid": grid, "dos": dos}


def _F(freqs, T):
    # harmonic free energy, hbar = kB = 1 (fixture convention)
    F = 0.0
    for w in freqs:
        e = math.exp(-w / T)
        F += 0.5 * w + T * math.log(1.0 - e)
    return F


def gold_thermo(freqs, tmin, tmax, tstep, dT=1e-4):
    """Independent gold: F direct, S and Cv by central finite differences of F.
    (Deliberately NOT the analytic S/Cv formulas — the artifact must match a
    differently-derived gold, as the real E2 golds come from the reference.)"""
    temps, Fs, Ss, Cvs = [], [], [], []
    T = tmin
    while T <= tmax + 1e-12:
        F = _F(freqs, T)
        Fp, Fm = _F(freqs, T + dT), _F(freqs, T - dT)
        S = -(Fp - Fm) / (2 * dT)
        Cv = -T * (Fp - 2 * F + Fm) / (dT * dT)
        temps.append(T)
        Fs.append(F)
        Ss.append(S)
        Cvs.append(Cv)
        T = round(T + tstep, 12)
    return {"temperatures": temps, "free_energies": Fs, "entropies": Ss, "heat_capacities": Cvs}


def gen_golds(fc, masses, qpoints, freqs):
    os.makedirs(GOLD_DIR, exist_ok=True)
    golds = {
        "t-mr-01-band-structure": {"band.json": gold_band(fc, masses, qpoints)},
        "t-mr-02-phonon-dos": {"dos.json": gold_dos(freqs, 0.05, 0.0, 3.0, 0.05)},
        "t-mr-03-thermal-properties": {"thermo.json": gold_thermo(freqs, 1.0, 5.0, 0.5)},
    }
    for name, g in golds.items():
        path = os.path.join(GOLD_DIR, name + ".json")
        blob = {
            "_meta": {
                "task": name,
                "generated_by": "e2-scripts/run_feasibility.py (zero-bundle)",
                "provenance": (
                    "mini-tier gold: implemented from the reference docs feature "
                    "surface (docs/band.md + harmonic formulation); F direct, S/Cv by "
                    "central finite difference of F — independent of the staged "
                    "artifacts' analytic formulas. Real-tier golds (E2 full run) come "
                    "from the reference executable, per e2-protocol Phase 6."
                ),
            },
        }
        blob.update(g)  # top-level keys = output filenames (judging contract)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(blob, f, indent=2)
        print(f"  gold {name}: {path}")
    return golds


# ------------------------------------------------------------ task registry --
TASKS = {
    "t-mr-01-band-structure": {
        "ref_capability": "band-structure",
        "input": "band_input.json",
        "output_files": "band.json",
        "gold": "t-mr-01-band-structure",
    },
    "t-mr-02-phonon-dos": {
        "ref_capability": "phonon-dos",
        "input": "dos_input.json",
        "output_files": "dos.json",
        "gold": "t-mr-02-phonon-dos",
    },
    "t-mr-03-thermal-properties": {
        "ref_capability": "phonon-thermal-properties",
        "input": "thermo_input.json",
        "output_files": "thermo.json",
        "gold": "t-mr-03-thermal-properties",
    },
}

# ----------------------------------------------------- artifact templates --
def tpl_band():
    return '''import json, sys, math
inp = json.load(open(sys.argv[1]))
fc, m, qpts = inp["force_constants"], inp["masses"], inp["qpoints"]
k = fc[0][0][0][0]
w = math.sqrt(abs(k) / m[0])
rows = []
for q in qpts:  # 1-atom fixture: 3 modes, each sqrt(2) (k=2, m=1)
    rows.append([w, w, w])
open("band.json", "w").write(json.dumps({"qpoints": qpts, "frequencies": rows}))
print("OK band.json %d qpoints" % len(qpts))
'''


def tpl_dos():
    return '''import json, sys, math
inp = json.load(open(sys.argv[1]))
freqs, sigma = inp["frequencies"], inp["sigma"]
fmin, fmax, fpitch = inp["fmin"], inp["fmax"], inp["fpitch"]
norm = 1.0 / (sigma * math.sqrt(2.0 * math.pi))
grid, dos = [], []
x = fmin
while x <= fmax + 1e-12:
    s = sum(math.exp(-((x - w) ** 2) / (2.0 * sigma * sigma)) * norm for w in freqs)
    grid.append(x); dos.append(s)
    x = round(x + fpitch, 12)
open("dos.json", "w").write(json.dumps({"grid": grid, "dos": dos}))
print("OK dos.json %d points" % len(grid))
'''


def tpl_thermo():
    return '''import json, sys, math
inp = json.load(open(sys.argv[1]))
freqs = inp["frequencies"]
tmin, tmax, tstep = inp["tmin"], inp["tmax"], inp["tstep"]
# harmonic phonon thermal properties, hbar=kB=1 (fixture convention)
def row(T):
    F = S = Cv = 0.0
    for w in freqs:
        x = w / T
        e = math.exp(-x)
        F += 0.5 * w + T * math.log(1.0 - e)          # zero point + T ln(1-e^-x)
        S += (w / T) / (math.exp(x) - 1.0) - math.log(1.0 - e)
        Cv += x * x * math.exp(x) / ((math.exp(x) - 1.0) ** 2)
    return F, S, Cv
temps, Fs, Ss, Cvs = [], [], [], []
T = tmin
while T <= tmax + 1e-12:
    F, S, Cv = row(T)
    temps.append(T); Fs.append(F); Ss.append(S); Cvs.append(Cv)
    T = round(T + tstep, 12)
out = {"temperatures": temps, "free_energies": Fs, "entropies": Ss, "heat_capacities": Cvs}
open("thermo.json", "w").write(json.dumps(out))
print("OK thermo.json %d temperatures" % len(temps))
'''


def tpl_thermo_missing_zp():
    src = tpl_thermo()
    return src.replace("F += 0.5 * w + T * math.log(1.0 - e)", "F += T * math.log(1.0 - e)")


def tpl_force_constants():
    return '''import json, sys
inp = json.load(open(sys.argv[1]))
D, F = inp["displacements"], inp["forces"]
na = inp["atoms"]
fc = [[[[0.0] * 3 for _ in range(3)] for _ in range(na)] for _ in range(na)]
for I in range(len(D)):
    for a in range(na):
        for mu in range(3):
            for b in range(na):
                for nu in range(3):
                    fc[a][b][mu][nu] += D[I][b][nu] * F[I][a][mu]
open("force_constants.json", "w").write(json.dumps({"atoms": na, "force_constants": fc}))
print("OK force_constants.json")
'''


def tpl_dyn():
    return '''import json, sys, math
inp = json.load(open(sys.argv[1]))
fc, m, qpts = inp["force_constants"], inp["masses"], inp["qpoints"]
rows = []
for q in qpts:
    k = fc[0][0][0][0]
    w = math.sqrt(abs(k) / m[0])
    rows.append([w, w, w])
open("dyn.json", "w").write(json.dumps({"qpoints": qpts, "frequencies": rows}))
print("OK dyn.json")
'''


TPL = {
    "band-structure": tpl_band,
    "phonon-dos": tpl_dos,
    "thermal-properties": tpl_thermo,
    "force-constants": tpl_force_constants,
    "dynamical-matrix": tpl_dyn,
}


# -------------------------------------------------------------------- pool --
def build_pool():
    with open(GOLD_FIXTURE, encoding="utf-8") as f:
        gold = json.load(f)
    order = []                      # gold file order (documented order)
    klass, source = {}, {}
    for g in gold["gaps"]:
        if g["class"] == "unknown":
            continue                # unknown never enters the pool (no-low-driven-missing)
        order.append(g["ref_id"])
        klass[g["ref_id"]] = g["class"]
        source[g["ref_id"]] = g["source_kind"]
    # mock report priority judgment (methodology Phase 5, source-informed):
    # host-self-audit first, then reference-contrast in documented order.
    def sort_key(rid):
        return (0 if source[rid] == "host-self-audit" else 1, order.index(rid))
    ranked = sorted(order, key=sort_key)
    pool = {
        "source": "mini fixture gold (tests/fixtures/gold/mini-ref-vs-mini-host.json)",
        "priority_judgment": "host-self-audit > reference-contrast (fix-wrongness "
                             "> honor-promise > extend-surface), then documented order",
        "gaps": [
            {"id": rid, "class": klass[rid], "source_kind": source[rid], "priority": i + 1}
            for i, rid in enumerate(ranked)
        ],
    }
    with open(POOL_PATH, "w", encoding="utf-8") as f:
        json.dump(pool, f, indent=2)
    return pool


def run_arm(mode, seed):
    out = subprocess.run(
        [sys.executable, ARM_SELECT, "--pool", POOL_PATH, "--k", "2",
         "--seed", str(seed), "--mode", mode],
        capture_output=True, text=True, check=True,
    ).stdout
    return json.loads(out)


# ----------------------------------------------------------------- staging --
def stage_artifact(gap_id, cell_dir):
    src = TPL[gap_id]()
    os.makedirs(cell_dir, exist_ok=True)
    runner = os.path.join(cell_dir, gap_id + ".py")
    with open(runner, "w", encoding="utf-8") as f:
        f.write(src)
    return runner


def effort_bytes(cell_dir, runner):
    return os.path.getsize(runner) if os.path.exists(runner) else 0


# ----------------------------------------------------------------- judging --
def judge(task_id, runner, cell_dir, run_id):
    t = TASKS[task_id]
    out = os.path.join(cell_dir, f"verdict-{task_id}.json")
    subprocess.run(
        [sys.executable, JUDGE, "--task", task_id, "--mode", "gold",
         "--runner", runner,
         "--input", os.path.join(FIX_DIR, t["input"]),
         "--gold", os.path.join(GOLD_DIR, t["gold"] + ".json"),
         "--output-files", t["output_files"],
         "--sandbox", cell_dir, "--out", out],
        capture_output=True, text=True, check=True,
    )
    with open(out, encoding="utf-8") as f:
        return json.load(f)


# ------------------------------------------------------------------- main --
def main():
    print("== E2 feasibility (mechanism demo, NOT a measurement) ==")
    print(f"  reference docs root : {PHONOPY_DOC}")
    os.makedirs(RUNS_DIR, exist_ok=True)
    run_id = f"feasibility-{time.strftime('%Y%m%d-%H%M%S')}"
    run_dir = os.path.join(RUNS_DIR, run_id)
    os.makedirs(run_dir, exist_ok=True)

    # 1. fixtures + golds
    print("[1/5] fixtures + golds (zero-bundle)")
    fc, masses, qpts, freqs = gen_fixtures()
    golds = gen_golds(fc, masses, qpts, freqs)

    # 2. pool + arms
    print("[2/5] gap pool + arm selection")
    pool = build_pool()
    print("  pool:", [g["id"] for g in pool["gaps"]],
          "| priority:", pool["priority_judgment"])
    pool_ids = {g["id"] for g in pool["gaps"]}
    absent = [t["ref_capability"] for t in TASKS.values()
              if t["ref_capability"] not in pool_ids]
    if absent:
        sys.exit(f"error: suite tasks reference capabilities not in gap pool: {absent}")
    arms = {
        "arm-a": run_arm("top", 42),
        "arm-b": run_arm("random", 7),
        "arm-c": run_arm("none", 42),
    }
    for name, m in arms.items():
        print(f"  {name} ({m['label']}): k={m['k']} selected={m['selected']}")

    # 3. stage + execute + judge per arm x task
    print("[3/5] stage -> execute -> judge (blind to arm: judge sees task+artifact only)")
    results, effort = {}, {}
    for aname, m in arms.items():
        results[aname], effort[aname] = {}, 0
        for tid, t in TASKS.items():
            cell = os.path.join(run_dir, aname, tid)
            os.makedirs(cell, exist_ok=True)
            if t["ref_capability"] in m["selected"]:
                runner = stage_artifact(t["ref_capability"], cell)
                effort[aname] += effort_bytes(cell, runner)
                verdict = judge(tid, runner, cell, run_id)
                results[aname][tid] = verdict["verdict"]
            else:
                results[aname][tid] = "skip"
    header = ["task"] + list(arms) + ["ref capability"]
    print(f"  {'task':38s} {'arm-a':8s} {'arm-b':8s} {'arm-c':8s} ref-capability")
    for tid, t in TASKS.items():
        print(f"  {tid:38s} {results['arm-a'][tid]:8s} {results['arm-b'][tid]:8s} "
              f"{results['arm-c'][tid]:8s} {t['ref_capability']}")

    # 4. controls + determinism
    print("[4/5] judge controls + determinism (gold-mode)")
    ctl_dir = os.path.join(run_dir, "controls")
    ok = True
    pos = stage_artifact("thermal-properties", ctl_dir)
    v = judge("t-mr-03-thermal-properties", pos, ctl_dir, run_id)
    print(f"  positive control (conforming artifact): {v['verdict']}",
          "PASS" if v["verdict"] == "pass" else "FAIL")
    ok &= v["verdict"] == "pass"
    neg = os.path.join(ctl_dir, "negative-ctl.py")
    with open(neg, "w", encoding="utf-8") as f:
        f.write(tpl_thermo_missing_zp())          # drops the zero-point term
    e1 = os.path.join(ctl_dir, "neg-1.json")
    e2 = os.path.join(ctl_dir, "neg-2.json")
    v1 = judge("t-mr-03-thermal-properties", neg, ctl_dir, run_id)
    v2 = judge("t-mr-03-thermal-properties", neg, ctl_dir, run_id)
    same = (v1["verdict"], v1["reasons"]) == (v2["verdict"], v2["reasons"])
    print(f"  negative control (zero-point term dropped): {v1['verdict']}",
          "PASS" if v1["verdict"] == "fail" else "FAIL")
    print(f"  determinism re-run: verdicts identical = {same}")
    ok &= v1["verdict"] == "fail" and same

    # 5. suite validation
    print("[5/5] task-suite validation")
    sub = subprocess.run(
        [sys.executable, DERIVE, os.path.join(E2, "task-suite.csv"),
         "--ref-doc-root", PHONOPY_DOC],
        capture_output=True, text=True,
    )
    print(" ", sub.stdout.strip() or sub.stderr.strip())
    ok &= sub.returncode == 0

    # aggregate (mechanism demo numbers, n=3 tasks on mini fixtures)
    print("\n== aggregate (DEMO numbers; disproportional to the real E2 scale) ==")
    for aname in arms:
        n_attempt = sum(1 for x in results[aname].values() if x != "skip")
        n_pass = sum(1 for x in results[aname].values() if x == "pass")
        n_skip = sum(1 for x in results[aname].values() if x == "skip")
        print(f"  {aname}: attempted={n_attempt} pass={n_pass} skip={n_skip} "
              f"success-on-attempted={n_pass}/{n_attempt} "
              f"full-suite={n_pass}/{len(TASKS)} effort={effort[aname]}B")
    g_a = sum(1 for x in results["arm-a"].values() if x == "pass") / len(TASKS)
    g_c = sum(1 for x in results["arm-c"].values() if x == "pass") / len(TASKS)
    print(f"  delta full-suite arm-a - arm-c = {g_a - g_c:+.3f} (demo only)")
    print(f"\n  run_id: {run_id}  (artifacts under {run_dir})")
    if not ok:
        sys.exit("controls failed — harness contract broken")
    print("  harness contract OK")


if __name__ == "__main__":
    main()