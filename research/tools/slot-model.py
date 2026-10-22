#!/usr/bin/env python3
"""slot-model.py — 槽位模型的可执行形式（零依赖，stdlib）。

论文/research 文档里以自然语言定义的四件事，在这里落成代码：
  1. 标签函数 lambda(u)          — introduction-operator.md §2 / typed-introduction.md §6
  2. 宿主投影 project(label, host_has) — slot-model.md §3
  3. 算子模拟 I / W_rap / P_aper / I∘pi — introduction-operator.md §3，验证命题 2-5 的计数
  4. 补丁审计 pi ∈ Adm(lambda)   — introduction-operator.md §4.1（2026-10-19 动作细化）

2026-10-22：槽位由二值改为**三态**（`1 | 0 | "unknown"`），与 skill 的
`references/report-schema.json` 对齐。读不到的来源不再被当成"来源没说"：
`s`/`e` 为 unknown 的行落成 `证据不足`，**不建卡**，差距行记 `unknown`，
且不进误引入 / 漏义务，单列 unresolved。`v` 为 unknown 的行落成
`有效性未评`：可引入，但不写作废检查，`prescribed` 只有 `bind`。

用法：
  python3 slot-model.py <slot.json>                  # 校验槽位 + 标签 + 投影 + 分叉 + 算子模拟
  python3 slot-model.py <slot.json> --empty-host     # 忽略 host_fills，按空宿主模拟
  python3 slot-model.py <slot.json> --audit patch.json  # 审计补丁清单是否属于 Adm(lambda)

patch.json 形如 {"qha": ["impl"], "phonon-dos": ["bind", "check"], ...}

槽位对象（每个槽一格）：
  {"state": 1,         "provenance": "paper", "span": "...", "quote": "..."}
  {"state": 0,         "provenance": "repo",  "span": "...|null", "quote": "", "why_empty": "absent: ..."}
  {"state": "unknown", "provenance": "paper", "span": null, "quote": "", "why_unknown": "unreachable: ..."}
旧记录里的 {"filled": true|false} 仍可读，视作 state 1 / 0。
"""
import json
import re
import sys

UNKNOWN = "unknown"

LABELS = ["不成行", "义务缺入口", "入口缺义务", "做法冲突", "缺有效性",
          "两侧齐", "证据不足", "有效性未评"]
OE, EO, CF, VG, OK, NA, IE, VU = (
    "义务缺入口", "入口缺义务", "做法冲突", "缺有效性", "两侧齐", "不成行",
    "证据不足", "有效性未评",
)

# 与 references/report-schema.json 的 $defs/slotBase 同一套模式。
WHY_EMPTY_RE = re.compile(r"^(absent|no-paper-arm|no-repo-arm)(:.*)?$")
WHY_UNKNOWN_RE = re.compile(r"^(unreachable|not-consulted|unparsable)(:.*)?$")


def read_state(slot, where, problems):
    """读一个槽的 state。三态原样返回；旧记录的 filled 折成 1/0。"""
    if not isinstance(slot, dict):
        problems.append(f"{where}: 槽不是对象")
        return None
    if "state" in slot:
        st = slot["state"]
        if st not in (0, 1, UNKNOWN):
            problems.append(f"{where}: state 必须是 1 / 0 / \"unknown\"，得到 {st!r}")
            return None
    elif "filled" in slot:
        st = 1 if slot["filled"] else 0
    else:
        problems.append(f"{where}: 既无 state 也无 filled")
        return None

    # 逐格良构约束（report-schema.json 的 allOf 三条）。
    if st == 1:
        if not str(slot.get("span") or "").strip():
            problems.append(f"{where}: state=1 必须给 span")
        if not str(slot.get("quote") or "").strip():
            problems.append(f"{where}: state=1 必须给非空 quote")
    elif st == 0:
        we = str(slot.get("why_empty") or "")
        if not we:
            problems.append(f"{where}: state=0 必须给 why_empty")
        elif not WHY_EMPTY_RE.match(we):
            problems.append(
                f"{where}: why_empty 不匹配 ^(absent|no-paper-arm|no-repo-arm)(:.*)?$ — {we[:40]!r}")
    else:
        wu = str(slot.get("why_unknown") or "")
        if not wu:
            problems.append(f"{where}: state=unknown 必须给 why_unknown")
        elif not WHY_UNKNOWN_RE.match(wu):
            problems.append(
                f"{where}: why_unknown 不匹配 ^(unreachable|not-consulted|unparsable)(:.*)?$ — {wu[:40]!r}")
        if str(slot.get("quote") or "").strip():
            problems.append(f"{where}: state=unknown 的 quote 必须为空")
    return st


def _unit_slots(unit, problems):
    """读一行的四个槽 + kappa。返回 (s, e, vp, vr, k)；读不出则 None。"""
    uid = unit.get("id", "?")
    out = {}
    for arm, key, slots in (("paper", "step", ("s",)), ("paper", "validity", ("v_p",)),
                            ("repo", "entry", ("e",)), ("repo", "validity", ("v_r",))):
        rec = unit.get(arm, {}).get(key, {})
        out[slots[0]] = read_state(rec, f"{uid}.{arm}.{key}", problems)
        if isinstance(rec, dict) and "provenance" in rec:
            want = {"paper", "none"} if arm == "paper" else {"repo", "none"}
            if rec["provenance"] not in want:
                problems.append(
                    f"{uid}.{arm}.{key}: provenance={rec['provenance']!r} 不合法，该臂只允许 {sorted(want)}")
    if any(v is None for v in out.values()):
        return None

    k = unit.get("kappa")
    k = bool(k["filled"]) if isinstance(k, dict) else bool(k)
    if k and not (out["s"] == 1 and out["e"] == 1):
        k = False  # 约束：单侧行上的 kappa 先改回 0（typed-introduction.md §6）
    return out["s"], out["e"], out["v_p"], out["v_r"], k


def slots(unit, problems=None):
    """从 unit 记录读出四个三态槽与 kappa。"""
    return _unit_slots(unit, problems if problems is not None else [])


def label(unit, problems=None):
    """lambda 函数。手写 label 与函数不一致时，以函数为准。

    顺序要紧：unknown 先短路，否则 s=1 / e=unknown 会落进两侧齐那一支。

    槽位读不出（畸形）的行不给标签：把它算成任何一支都是编造。记一条问题并返回 None，
    调用方据此让整轮无效 —— 与 skill 的 Layer-1「任一 fail = 整轮无效」同一纪律。
    """
    st = slots(unit, problems)
    if st is None:
        return None
    s, e, vp, vr, k = st
    if s == UNKNOWN or e == UNKNOWN:
        return IE
    if not s and not e:
        return NA
    if s and not e:
        return OE
    if e and not s:
        return EO
    if k:
        return CF
    if vp == UNKNOWN or vr == UNKNOWN:
        return VU
    return VG if vp != vr else OK


def project(lab, host_has):
    """slot-model.md §3 的 project(label, host_has)。CF/不成行/证据不足不进缺口表。"""
    gap = "host-already" if host_has else "gap"
    if lab in (OK, VU):
        both = "covered" if host_has else "gap"
        return both, both
    if lab == OE:
        return gap, "absent"
    if lab == EO:
        return "absent", gap
    if lab == VG:
        v = "host-already" if host_has else "validity-gap"
        return v, v
    if lab == IE:
        return "unknown", "unknown"  # 差距行记 unknown；不建卡
    return "-", "-"


def apply_operator(units, labs, host_has, op, problems=None):
    """在冻住宿主上应用算子，返回 (P', K', records)。空位冻结语义：host_has=True 的产物视为已在 P。"""
    problems = problems if problems is not None else []
    P = {u["id"] for u in units if host_has.get(u["id"])}
    K = set()
    records = []
    eff = dict(labs)
    if op == "I∘pi":  # 打乱消融：对调 OE 与 EO（命题 5）
        eff = {i: {OE: EO, EO: OE}.get(l, l) for i, l in labs.items()}
    for u in units:
        i, lab = u["id"], eff[u["id"]]
        st = slots(u, problems)
        if st is None:
            continue  # 畸形行已记问题；整轮将判为无效
        s, e, vp, vr, k = st
        if op == "W_rap":
            # 只接仓库：e==1 才接。e 为 unknown 接不上（读不到的入口不能包）。
            if e == 1 and i not in P:
                P.add(i)
        elif op == "P_aper":
            # 只抄论文：s==1 才抄。s 为 unknown 抄不出。
            if s == 1 and i not in P:
                P.add(i)
        else:  # I 或 I∘pi
            if lab == OK and i not in P:
                P.add(i)
                if vp == 1 and vr == 1:
                    K.add(i)
            elif lab == OE and i not in P:
                P.add(i)
            elif lab == VG:
                P.add(i)
                K.add(i)
            elif lab == VU:
                P.add(i)  # 有效性未评：可引入，但不写作废检查
            elif lab == CF:
                records.append(i)
            # IE / EO / NA：不改宿主（IE 无卡，EO 拒绝，NA 忽略）
    return P, K, records


def metrics(units, labs, P0, P, K, problems=None):
    """FI / Miss / t_v / unresolved。CF 故意不加入，从 Miss 单列；IE 单列 unresolved。"""
    problems = problems if problems is not None else []
    fi, miss, unresolved = [], [], []
    for u in units:
        i, lab = u["id"], labs[u["id"]]
        st = slots(u, problems)
        if st is None or lab is None:
            continue  # 畸形行已记问题；整轮将判为无效
        s = st[0]
        if lab == IE:
            unresolved.append(i)
            continue  # 读不到来源的行既不算误引入，也不算漏义务
        if i in P - P0 and s == 0:
            fi.append(i)
        if s == 1 and i not in P0 and i not in P and lab != CF:
            miss.append(i)
    tv = {u["id"]: int(u["id"] in P and u["id"] in K)
          for u in units if labs[u["id"]] == VG}
    return sorted(fi), sorted(miss), tv, sorted(unresolved)


# ---- Adm(lambda) 补丁审计（introduction-operator.md §4.1）----

PRESCRIBED = {OK: "bind", OE: "impl", VG: "check", CF: "record", VU: "bind", IE: "none", NA: "none"}


def audit(units, labs, patch, problems=None):
    """检查补丁清单 pi 是否属于 Adm(lambda(u))。返回违规列表。"""
    problems = problems if problems is not None else []
    out = []
    for u in units:
        i, lab = u["id"], labs[u["id"]]
        st = slots(u, problems)
        if st is None or lab is None:
            continue  # 畸形行已记问题；无标签可审
        s, e, vp, vr, k = st
        acts = set(patch.get(i, []))
        unknown = acts - {"bind", "impl", "check", "record", "nop"}
        if unknown:
            out.append(f"{i}: 未知原子动作 {sorted(unknown)}")
        if lab in (EO, NA, IE):
            if acts & {"bind", "impl"}:
                out.append(f"{i}: {lab} 禁止 bind/impl，补丁含 {sorted(acts)}")
            if lab == IE and "check" in acts:
                out.append(f"{i}: 证据不足不得写作废检查（有效性无从判断）")
        elif lab == CF:
            if "record" not in acts:
                out.append(f"{i}: 做法冲突缺少 record")
            if acts & {"bind", "impl"}:
                out.append(f"{i}: 做法冲突私自选边（含 bind/impl）")
        elif lab == OK:
            if "bind" not in acts:
                out.append(f"{i}: 两侧齐缺少 bind（丢掉入口自己重写是违规）")
            if "impl" in acts:
                out.append(f"{i}: 两侧齐禁止 impl（应绑现成入口）")
            if vp == 1 and vr == 1 and "check" not in acts:
                out.append(f"{i}: 两侧都写了作废条件，缺少 check")
        elif lab == OE:
            if "impl" not in acts:
                out.append(f"{i}: 义务缺入口缺少 impl（按论文实现）")
            if "bind" in acts:
                out.append(f"{i}: 义务缺入口禁止 bind（伪造仓库入口）")
        elif lab == VG:
            if "bind" not in acts or "check" not in acts:
                out.append(f"{i}: 缺有效性要求 bind + check，补丁含 {sorted(acts)}")
        elif lab == VU:
            if "bind" not in acts:
                out.append(f"{i}: 有效性未评要求 bind，补丁含 {sorted(acts)}")
            if "check" in acts:
                out.append(f"{i}: 有效性未评不得写作废检查（该侧未评）")
            if "impl" in acts:
                out.append(f"{i}: 有效性未评禁止 impl")
    return out


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
    problems = []
    labs = {u["id"]: label(u, problems) for u in units}
    ok = True

    # 0. 槽位良构（三态 / why_empty / why_unknown / provenance / quote）
    if problems:
        print("== 槽位良构 ==")
        for p in problems:
            print(f"  ✗ {p}")
        ok = False

    # 1. 校验手写标签
    print("== 标签校验（lambda 函数 vs 手写 label）==")
    for u in units:
        hand = u.get("label")
        lab = labs[u["id"]]
        if lab is None:
            print(f"  {u['id']:<18} ✗ 槽位畸形，无标签（见上）")
            ok = False
            continue
        mark = ""
        if hand is not None and hand != lab:
            mark = f"  ✗ 手写={hand}"
            ok = False
        print(f"  {u['id']:<18} {lab}{mark}")

    # 2. 宿主投影与分叉
    host_has = {}
    if not empty_host:
        host_has = {f["unit_id"]: bool(f["host_has"]) for f in data.get("host_fills", [])}
    print("\n== 宿主投影 ==")
    paper_gaps, repo_gaps = [], []
    for u in units:
        i = u["id"]
        if labs[i] is None:
            print(f"  {i:<18} paper={'—':<13} repo=—（畸形，跳过）")
            continue
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
    ie_rows = sorted(i for i, l in labs.items() if l == IE)
    if ie_rows:
        print(f"  证据不足（不进缺口表，不建卡）: {ie_rows}")

    # 3. 算子模拟：验证命题 2-5 的计数（typed-introduction.md §11 的理论值）
    print("\n== 算子模拟（I / W_rap / P_aper / I∘pi）==")
    P0 = {i for i, h in host_has.items() if h}
    sim = {}
    print(f"  {'operator':<8} {'FI':<4} {'Miss':<5} {'unres':<6} {'t_v':<22} records")
    for op in ["I", "W_rap", "P_aper", "I∘pi"]:
        P, K, records = apply_operator(units, labs, host_has, op, problems)
        fi, miss, tv, unres = metrics(units, labs, P0, P, K, problems)
        sim[op] = (P, K, fi, miss, tv, unres)
        print(f"  {op:<8} {len(fi):<4} {len(miss):<5} {len(unres):<6} {str(tv):<22} {records}")
        if fi:
            print(f"           FI 明细: {fi}")
        if miss:
            print(f"           Miss 明细: {miss}")
        if unres:
            print(f"           未决明细: {unres}")
    # 命题检查
    P_I, K_I, fi_I, miss_I, _, _ = sim["I"]
    _, _, fi_W, miss_W, _, _ = sim["W_rap"]
    n_eo = sum(1 for l in labs.values() if l == EO)
    n_oe = sum(1 for l in labs.values() if l == OE)
    n_ie = sum(1 for l in labs.values() if l == IE)
    p2 = len(fi_I) == 0
    p3 = len(fi_W) == n_eo and len(miss_W) == n_oe
    p4 = all(i in K_I for i, l in labs.items() if l == VG)
    print(f"\n  命题 2 (FI(I)=0): {p2}")
    print(f"  命题 3 (FI(W_rap)=|EO|={n_eo}, Miss(W_rap)=|OE|={n_oe}): {p3}"
          + (f"  [含 {n_ie} 行证据不足；未决既不算误引入也不算漏义务]" if n_ie else ""))
    print(f"  命题 4 (VG 单元上 I 使 t_v=1): {p4}")
    ok = ok and p2 and p3 and p4

    # 4. 补丁审计
    if audit_path:
        patch = json.load(open(audit_path))
        print("\n== 补丁审计（pi ∈ Adm(lambda)）==")
        bad = audit(units, labs, patch, problems)
        if bad:
            for p in bad:
                print(f"  ✗ {p}")
            ok = False
        else:
            print("  全部通过")
        for i, l in labs.items():
            if l in PRESCRIBED:
                act = PRESCRIBED[l]
                if act == "none":
                    print(f"  {i}: 无规定动作（{l} 不建卡，无 destroy 检查）")
                else:
                    print(f"  {i}: 规定动作 = {act}（destroy 检查：移除后测试必须变红）")

    if problems:
        ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())