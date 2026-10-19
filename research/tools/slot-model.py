#!/usr/bin/env python3
"""slot-model.py — 槽位模型的可执行形式（零依赖，stdlib）。

论文/research 文档里以自然语言定义的四件事，在这里落成代码：
  1. 标签函数 lambda(u)          — introduction-operator.md §2 / typed-introduction.md §6
  2. 宿主投影 project(label, host_has) — slot-model.md §3
  3. 算子模拟 I / W_rap / P_aper / I∘pi — introduction-operator.md §3，验证命题 2-5 的计数
  4. 补丁审计 pi ∈ Adm(lambda)   — introduction-operator.md §4.1（2026-10-19 动作细化）

用法：
  python3 slot-model.py <slot.json>                  # 校验标签 + 投影 + 分叉 + 算子模拟
  python3 slot-model.py <slot.json> --empty-host     # 忽略 host_fills，按空宿主模拟
  python3 slot-model.py <slot.json> --audit patch.json  # 审计补丁清单是否属于 Adm(lambda)

patch.json 形如 {"qha": ["impl"], "phonon-dos": ["bind", "check"], ...}
"""
import json
import sys

LABELS = ["不成行", "义务缺入口", "入口缺义务", "做法冲突", "缺有效性", "两侧齐"]
OE, EO, CF, VG, OK, NA = "义务缺入口", "入口缺义务", "做法冲突", "缺有效性", "两侧齐", "不成行"


def slots(unit):
    """从 unit 记录读出五个布尔槽。kappa 缺省为 0；良构约束：kappa=1 只在 s=e=1 时合法。"""
    s = bool(unit["paper"]["step"]["filled"])
    e = bool(unit["repo"]["entry"]["filled"])
    vp = bool(unit["paper"]["validity"]["filled"])
    vr = bool(unit["repo"]["validity"]["filled"])
    k = unit.get("kappa")
    k = bool(k["filled"]) if isinstance(k, dict) else bool(k)
    if k and not (s and e):
        k = False  # 约束：单侧行上的 kappa 先改回 0（typed-introduction.md §6）
    return s, e, vp, vr, k


def label(unit):
    """lambda 函数。手写 label 与函数不一致时，以函数为准。"""
    s, e, vp, vr, k = slots(unit)
    if not s and not e:
        return NA
    if s and not e:
        return OE
    if e and not s:
        return EO
    if k:
        return CF
    return VG if vp != vr else OK


def project(lab, host_has):
    """slot-model.md §3 的 project(label, host_has)。CF/不成行不进缺口表。"""
    gap = "host-already" if host_has else "gap"
    if lab == OK:
        both = "covered" if host_has else "gap"
        return both, both
    if lab == OE:
        return gap, "absent"
    if lab == EO:
        return "absent", gap
    if lab == VG:
        v = "host-already" if host_has else "validity-gap"
        return v, v
    return "-", "-"


def apply_operator(units, labs, host_has, op):
    """在冻住宿主上应用算子，返回 (P', K', records)。空位冻结语义：host_has=True 的产物视为已在 P。"""
    P = {u["id"] for u in units if host_has.get(u["id"])}
    K = set()
    records = []
    eff = dict(labs)
    if op == "I∘pi":  # 打乱消融：对调 OE 与 EO（命题 5）
        eff = {i: {OE: EO, EO: OE}.get(l, l) for i, l in labs.items()}
    for u in units:
        i, lab = u["id"], eff[u["id"]]
        s, e, vp, vr, k = slots(u)
        if op == "W_rap":
            if e and i not in P:
                P.add(i)
        elif op == "P_aper":
            if s and i not in P:
                P.add(i)
        else:  # I 或 I∘pi
            if lab == OK and i not in P:
                P.add(i)
                if vp and vr:
                    K.add(i)
            elif lab == OE and i not in P:
                P.add(i)
            elif lab == VG:
                P.add(i)
                K.add(i)
            elif lab == CF:
                records.append(i)
    return P, K, records


def metrics(units, labs, P0, P, K):
    """FI / Miss / t_v。CF 故意不加入，从 Miss 单列。"""
    fi = sorted(u["id"] for u in units if u["id"] in P - P0 and not slots(u)[0])
    miss = sorted(
        u["id"] for u in units
        if slots(u)[0] and u["id"] not in P0 and u["id"] not in P and labs[u["id"]] != CF
    )
    tv = {u["id"]: int(u["id"] in P and u["id"] in K) for u in units if labs[u["id"]] == VG}
    return fi, miss, tv


# ---- Adm(lambda) 补丁审计（introduction-operator.md §4.1）----

PRESCRIBED = {OK: "bind", OE: "impl", VG: "check", CF: "record"}


def audit(units, labs, patch):
    """检查补丁清单 pi 是否属于 Adm(lambda(u))。返回违规列表。"""
    problems = []
    for u in units:
        i, lab = u["id"], labs[u["id"]]
        s, e, vp, vr, k = slots(u)
        acts = set(patch.get(i, []))
        unknown = acts - {"bind", "impl", "check", "record", "nop"}
        if unknown:
            problems.append(f"{i}: 未知原子动作 {sorted(unknown)}")
        if lab in (EO, NA):
            if acts & {"bind", "impl"}:
                problems.append(f"{i}: {lab} 禁止 bind/impl，补丁含 {sorted(acts)}")
        elif lab == CF:
            if "record" not in acts:
                problems.append(f"{i}: 做法冲突缺少 record")
            if acts & {"bind", "impl"}:
                problems.append(f"{i}: 做法冲突私自选边（含 bind/impl）")
        elif lab == OK:
            if "bind" not in acts:
                problems.append(f"{i}: 两侧齐缺少 bind（丢掉入口自己重写是违规）")
            if "impl" in acts:
                problems.append(f"{i}: 两侧齐禁止 impl（应绑现成入口）")
            if vp and vr and "check" not in acts:
                problems.append(f"{i}: 两侧都写了作废条件，缺少 check")
        elif lab == OE:
            if "impl" not in acts:
                problems.append(f"{i}: 义务缺入口缺少 impl（按论文实现）")
            if "bind" in acts:
                problems.append(f"{i}: 义务缺入口禁止 bind（伪造仓库入口）")
        elif lab == VG:
            if "bind" not in acts or "check" not in acts:
                problems.append(f"{i}: 缺有效性要求 bind + check，补丁含 {sorted(acts)}")
    return problems


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    path = args[0]
    empty_host = "--empty-host" in args
    audit_path = args[args.index("--audit") + 1] if "--audit" in args else None

    data = json.load(open(path))
    units = [u for u in data["units"]]
    labs = {u["id"]: label(u) for u in units}
    ok = True

    # 1. 校验手写标签
    print("== 标签校验（lambda 函数 vs 手写 label）==")
    for u in units:
        hand = u.get("label")
        mark = ""
        if hand is not None and hand != labs[u["id"]]:
            mark = f"  ✗ 手写={hand}"
            ok = False
        print(f"  {u['id']:<18} {labs[u['id']]}{mark}")

    # 2. 宿主投影与分叉
    host_has = {}
    if not empty_host:
        host_has = {f["unit_id"]: bool(f["host_has"]) for f in data.get("host_fills", [])}
    print("\n== 宿主投影 ==")
    paper_gaps, repo_gaps = [], []
    for u in units:
        i = u["id"]
        pp, rp = project(labs[i], host_has.get(i, False))
        print(f"  {i:<18} paper={pp:<13} repo={rp}")
        if pp == "gap":
            paper_gaps.append(i)
        if rp == "gap":
            repo_gaps.append(i)
    inter = sorted(set(paper_gaps) & set(repo_gaps))
    union = sorted(set(paper_gaps) | set(repo_gaps))
    jac = len(inter) / len(union) if union else 1.0
    print(f"  paper_gaps={paper_gaps}")
    print(f"  repo_gaps ={repo_gaps}")
    print(f"  交集={inter}  Jaccard={jac:.3f}")
    rec = data.get("fork")
    if rec:
        match = rec["paper_gaps"] == paper_gaps and rec["repo_gaps"] == repo_gaps
        print(f"  与记录 fork 一致: {match}")
        ok = ok and match

    # 3. 算子模拟：验证命题 2-5 的计数（typed-introduction.md §11 的理论值）
    print("\n== 算子模拟（I / W_rap / P_aper / I∘pi）==")
    P0 = {i for i, h in host_has.items() if h}
    print(f"  {'operator':<8} {'FI':<4} {'Miss':<5} {'t_v':<22} records")
    for op in ["I", "W_rap", "P_aper", "I∘pi"]:
        P, K, records = apply_operator(units, labs, host_has, op)
        fi, miss, tv = metrics(units, labs, P0, P, K)
        print(f"  {op:<8} {len(fi):<4} {len(miss):<5} {str(tv):<22} {records}")
        if fi:
            print(f"           FI 明细: {fi}")
        if miss:
            print(f"           Miss 明细: {miss}")
    # 命题检查
    P_I, K_I, _ = apply_operator(units, labs, host_has, "I")
    fi_I, miss_I, _ = metrics(units, labs, P0, P_I, K_I)
    P_W, _, _ = apply_operator(units, labs, host_has, "W_rap")
    fi_W, miss_W, _ = metrics(units, labs, P0, P_W, set())
    n_eo = sum(1 for l in labs.values() if l == EO)
    n_oe = sum(1 for l in labs.values() if l == OE)
    p2 = len(fi_I) == 0
    p3 = len(fi_W) == n_eo and len(miss_W) == n_oe
    p4 = all(i in K_I for i, l in labs.items() if l == VG)
    print(f"\n  命题 2 (FI(I)=0): {p2}")
    print(f"  命题 3 (FI(W_rap)=|EO|={n_eo}, Miss(W_rap)=|OE|={n_oe}): {p3}")
    print(f"  命题 4 (VG 单元上 I 使 t_v=1): {p4}")
    ok = ok and p2 and p3 and p4

    # 4. 补丁审计
    if audit_path:
        patch = json.load(open(audit_path))
        print("\n== 补丁审计（pi ∈ Adm(lambda)）==")
        problems = audit(units, labs, patch)
        if problems:
            for p in problems:
                print(f"  ✗ {p}")
            ok = False
        else:
            print("  全部通过")
        for i, l in labs.items():
            if l in PRESCRIBED:
                print(f"  {i}: 规定动作 = {PRESCRIBED[l]}（destroy 检查：移除后测试必须变红）")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
