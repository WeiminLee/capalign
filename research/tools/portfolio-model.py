#!/usr/bin/env python3
"""Static checker for cap-align portfolio admission plans.

This is a research/verification tool, not a skill runner. It reads a declared
JSON portfolio, checks the relation witnesses, action pairs, merge safety,
lifecycle reachability, probes, set-test arithmetic, and budget. It never
executes a probe and never edits a host.

Input shape (see tests/fixtures/mini-library/portfolio-input.json):

    {
      "host": {"entries": [entry], "budget": {...}},
      "candidates": [candidate],
      "plan": {"accepted": [...], "demoted": [...]},
      "probes": [{qid, text, owner, expected, kind, retained, margin}],
      "obligations": [{"id": ..., "live": true}],
      "lifecycle": [{action, target, sources, reason, probes, rollback}]
    }

`margin` is the retained probe's pre-admission margin. It is an input-only
field (the report's set_test carries the same number); candidate probe_effects
is the only source of deltas.
"""

import argparse
import json
import sys
from pathlib import Path

RELATIONS = [
    "covered",
    "partial",
    "duplicate",
    "variant",
    "hard-conflict",
    "subsumes",
    "subsumed",
    "adjacent",
    "unrelated",
]
ACTIONS = [
    "no-op",
    "bind",
    "author",
    "extend",
    "add_validator",
    "merge",
    "demote",
    "upgrade",
    "downgrade",
    "retire",
    "quarantine",
    "refuse",
    "split",
    "new-entry",
]
ALLOWED_ACTIONS = {
    "covered": {"no-op"},
    "partial": {"add_validator", "upgrade", "downgrade", "split"},
    "duplicate": {"merge"},
    "variant": {"split", "demote"},
    "hard-conflict": {"quarantine", "refuse"},
    "subsumes": {"upgrade"},
    "subsumed": {"no-op"},
    "adjacent": {"extend", "new-entry"},
    "unrelated": {"new-entry", "no-op"},
}
EVIDENCE_KEYS = [
    "same_product",
    "same_procedure",
    "same_regime",
    "regime_overlap",
    "regime_subset",
    "checks_missing",
    "question_overlap",
    "products_superset",
    "checks_superset",
    "regime_superset",
    "products_subset",
    "checks_subset",
]
NON_DELIVERING_ACTIONS = {"no-op", "refuse", "quarantine"}
NEW_ROUTABLE_ACTIONS = {"new-entry", "split", "upgrade"}
MERGE_SURFACE_PREFIX = {
    "triggers": "trigger",
    "workflow_edges": "workflow_edge",
    "tool_requirements": "tool_requirement",
    "obligations": "obligation",
    "output_fields": "output_field",
}
MERGE_WITNESS_KINDS = {"W1", "W2", "W3"}
MERGE_EVIDENCE_LEVELS = {"constructive", "model", "statistical"}
W3_FORBIDDEN_MARKERS = ("prohibition", "exemption", "output")
NEGATIVE_INTERACTION = -0.15


def load_portfolio(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _failures(prefix, missing):
    return [f"{prefix}: missing {name}" for name in missing]


def _products(record):
    return set(record.get("products", []) or [])


def _checks(record):
    return set(record.get("checks", []) or [])


def _provenance(record):
    return set(record.get("provenance", []) or [])


def _regime_tags(record):
    regime = record.get("regime") or {}
    return set(regime.get("tags", []) or [])


def _candidate_as_entry(card):
    return {
        "id": card.get("card_id"),
        "products": list(card.get("products", [])),
        "checks": list(card.get("checks", [])),
        "provenance": list(card.get("provenance", [])),
        "regime": card.get("regime") or {"claim": "", "tags": []},
        "test_contract": card.get("test_contract"),
    }


def validate_portfolio(doc):
    violations = []
    if not isinstance(doc, dict):
        return ["document must be a JSON object"]
    for key in ("host", "candidates", "plan", "probes", "obligations", "lifecycle"):
        if key not in doc:
            violations.append(f"document: missing {key}")
    host = doc.get("host")
    if not isinstance(host, dict):
        violations.append("host: must be an object")
        host = {}
    if not isinstance(host.get("entries"), list):
        violations.append("host.entries: must be an array")
    budget = host.get("budget")
    if not isinstance(budget, dict):
        violations.append("host.budget: must be an object")
    else:
        for key in (
            "context_tokens_before",
            "context_tokens_after",
            "limit",
        ):
            if key not in budget:
                violations.append(f"host.budget: missing {key}")
    for index, card in enumerate(doc.get("candidates", []) or []):
        if not isinstance(card, dict):
            violations.append(f"candidate[{index}]: must be an object")
            continue
        for key in ("card_id", "relation", "relation_evidence", "action"):
            if key not in card:
                violations.append(f"candidate[{index}]: missing {key}")
    return violations


def check_relation(candidate, entries):
    violations = []
    card_id = candidate.get("card_id", "?")
    relation = candidate.get("relation")
    evidence = candidate.get("relation_evidence") or {}
    if relation not in RELATIONS:
        violations.append(f"{card_id}: unknown relation {relation!r}")
        return violations
    missing = [key for key in EVIDENCE_KEYS if key not in evidence]
    if missing:
        violations.extend(_failures(f"{card_id}: relation_evidence", missing))
        return violations
    for key in EVIDENCE_KEYS:
        if not isinstance(evidence.get(key), bool):
            violations.append(f"{card_id}: relation_evidence.{key} must be boolean")

    target = candidate.get("target_entry")
    target_entry = entries.get(target) if target else None
    if target is not None and target not in entries:
        violations.append(f"{card_id}: target_entry {target!r} does not exist")
    if relation in {
        "covered", "partial", "duplicate", "variant", "hard-conflict",
        "subsumes", "subsumed",
    } and target_entry is None:
        violations.append(f"{card_id}: relation {relation} requires a target entry")

    def flag(key):
        return evidence.get(key) is True

    predicates = {
        "covered": flag("same_product") and flag("same_procedure")
        and flag("regime_subset") and not flag("checks_missing"),
        "partial": flag("same_product") and flag("same_procedure")
        and (not flag("same_regime") or flag("checks_missing")),
        "duplicate": flag("same_product") and flag("same_procedure")
        and flag("same_regime") and not flag("checks_missing"),
        "variant": flag("same_product") and not flag("same_procedure")
        and not flag("regime_overlap"),
        "hard-conflict": flag("same_product") and not flag("same_procedure")
        and flag("regime_overlap"),
        "subsumes": flag("products_superset") and flag("checks_superset")
        and flag("regime_superset"),
        "subsumed": flag("products_subset") and flag("checks_subset")
        and flag("regime_subset"),
        "adjacent": not flag("same_product") and flag("question_overlap"),
        "unrelated": not flag("same_product") and not flag("question_overlap"),
    }
    if not predicates[relation]:
        violations.append(
            f"{card_id}: declared relation {relation} does not match its witnesses"
        )
    return violations


def check_action(candidate):
    violations = []
    card_id = candidate.get("card_id", "?")
    relation = candidate.get("relation")
    action = candidate.get("action")
    if action not in ACTIONS:
        violations.append(f"{card_id}: unknown action {action!r}")
        return violations
    allowed = ALLOWED_ACTIONS.get(relation, set())
    if action not in allowed:
        violations.append(
            f"{card_id}: action {action} is not allowed for relation {relation}"
        )
    if action == "merge" and relation != "duplicate":
        violations.append(f"{card_id}: merge is only allowed for duplicate")
    if action == "merge" and not candidate.get("target_entry"):
        violations.append(f"{card_id}: merge requires a target_entry")
    return violations


def check_merge(candidate, entries, obligations):
    if candidate.get("action") != "merge":
        return []
    violations = []
    card_id = candidate.get("card_id", "?")
    if candidate.get("relation") != "duplicate":
        violations.append(f"{card_id}: merge requires relation duplicate")
    target_id = candidate.get("target_entry")
    target = entries.get(target_id) if target_id else None
    if target is None:
        violations.append(f"{card_id}: merge target {target_id!r} does not exist")
        return violations

    candidate_products = _products(candidate)
    candidate_checks = _checks(candidate)
    target_products = _products(target)
    target_checks = _checks(target)
    lost_products = target_products - candidate_products
    lost_checks = target_checks - candidate_checks
    if lost_products:
        violations.append(
            f"{card_id}: merge loses target product(s): {sorted(lost_products)}"
        )
    if lost_checks:
        violations.append(
            f"{card_id}: merge loses target check(s): {sorted(lost_checks)}"
        )
    lost_provenance = _provenance(target) - _provenance(candidate)
    if lost_provenance:
        violations.append(
            f"{card_id}: merge loses target provenance: {sorted(lost_provenance)}"
        )
    if not candidate.get("test_contract"):
        violations.append(f"{card_id}: merge requires the candidate test contract")
    if not target.get("test_contract"):
        violations.append(f"{card_id}: merge requires the target test contract")

    remaining = [
        record for entry_id, record in entries.items() if entry_id != target_id
    ]
    remaining.append(_candidate_as_entry(candidate))
    for obligation in obligations:
        if not obligation.get("live"):
            continue
        obligation_id = obligation.get("id")
        if obligation_id not in target_products:
            continue
        if not any(obligation_id in _products(record) for record in remaining):
            violations.append(
                f"{card_id}: merge leaves live obligation {obligation_id} "
                "without a deliverer"
            )
    return violations


def _surface_units(record):
    surface = record.get("surface")
    if not isinstance(surface, dict):
        return set()
    units = set()
    for key, prefix in MERGE_SURFACE_PREFIX.items():
        items = surface.get(key) or []
        if not isinstance(items, list):
            continue
        for item in items:
            if isinstance(item, str) and item:
                units.add(f"{prefix}:{item}")
    return units


def _is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _w3_forbidden(unit):
    """W3 is too weak for obligations and output/prohibition markers."""
    prefix = unit.split(":", 1)[0]
    if prefix in {"obligation", "output_field"}:
        return True
    lowered = unit.lower()
    return any(marker in lowered for marker in W3_FORBIDDEN_MARKERS)


def check_merge_evidence(candidate, entries, probes):
    """Check the fail-closed evidence attached to a card-level merge.

    Merge is a structural claim: every removed unit needs one witness, every
    unit that cannot be witnessed is preserved in the locked residual, both
    sides' retained probes are replayed before commit, and no merge may claim a
    measured causal benefit without randomized evidence. The down side of a
    merge is unbounded, so an absent or malformed block is itself a violation.
    """
    if candidate.get("action") != "merge":
        return []
    card_id = candidate.get("card_id", "?")
    block = candidate.get("merge")
    if not isinstance(block, dict):
        return [f"{card_id}: merge requires a merge evidence block"]

    violations = []
    rollback = candidate.get("rollback")
    if not isinstance(rollback, str) or not rollback.strip():
        violations.append(f"{card_id}: merge requires rollback instructions")

    witnesses = block.get("witnesses")
    removed = block.get("removed_units")
    if not isinstance(witnesses, list):
        violations.append(f"{card_id}: merge.witnesses must be an array")
        witnesses = []
    if not isinstance(removed, list):
        violations.append(f"{card_id}: merge.removed_units must be an array")
        removed = []
    removed_units = {unit for unit in removed if isinstance(unit, str) and unit}
    source_unit = f"entry:{card_id}"
    if source_unit not in removed_units:
        violations.append(
            f"{card_id}: merge must account for removing {source_unit}"
        )

    seen = {}
    for index, witness in enumerate(witnesses):
        if not isinstance(witness, dict):
            violations.append(
                f"{card_id}: merge.witnesses[{index}] must be an object"
            )
            continue
        unit = witness.get("unit")
        kind = witness.get("kind")
        evidence = witness.get("evidence")
        if not isinstance(unit, str) or not unit:
            violations.append(
                f"{card_id}: merge.witnesses[{index}] has no unit"
            )
            continue
        if kind not in MERGE_WITNESS_KINDS:
            violations.append(f"{card_id}: {unit} has unknown witness kind {kind!r}")
        if not isinstance(evidence, str) or not evidence.strip():
            violations.append(f"{card_id}: {unit} has an empty witness")
        if unit in seen:
            violations.append(
                f"{card_id}: {unit} has more than one witness"
            )
        seen[unit] = kind
        if kind == "W3" and _w3_forbidden(unit):
            violations.append(
                f"{card_id}: W3 cannot delete {unit}; it is an obligation or "
                "output unit, or carries a prohibition/exemption marker"
            )
    for unit in sorted(removed_units - set(seen)):
        violations.append(f"{card_id}: removed unit {unit} has no witness")
    for unit in sorted(set(seen) - removed_units):
        violations.append(
            f"{card_id}: witness unit {unit} is not declared as removed"
        )

    locked = block.get("locked_residual")
    if not isinstance(locked, list):
        violations.append(f"{card_id}: merge.locked_residual must be an array")
        locked = []
    locked_units = set()
    for index, record in enumerate(locked):
        if not isinstance(record, dict):
            violations.append(
                f"{card_id}: merge.locked_residual[{index}] must be an object"
            )
            continue
        unit = record.get("unit")
        reason = record.get("reason")
        verbatim = record.get("verbatim")
        if not isinstance(unit, str) or not unit:
            violations.append(
                f"{card_id}: merge.locked_residual[{index}] has no unit"
            )
            continue
        if not isinstance(reason, str) or not reason.strip():
            violations.append(f"{card_id}: locked residual {unit} has no reason")
        if not isinstance(verbatim, str) or not verbatim.strip():
            violations.append(
                f"{card_id}: locked residual {unit} is not preserved verbatim"
            )
        if unit in removed_units:
            violations.append(
                f"{card_id}: {unit} cannot be both removed and locked"
            )
        locked_units.add(unit)

    target_id = candidate.get("target_entry")
    target = entries.get(target_id) or {}
    for label, record in (("target", target), ("candidate", candidate)):
        surface = record.get("surface")
        if not isinstance(surface, dict):
            continue
        unknown = sorted(set(surface) - set(MERGE_SURFACE_PREFIX))
        if unknown:
            violations.append(
                f"{card_id}: unknown surface class(es) on {label}: {unknown}"
            )

    coverage = block.get("coverage")
    if not isinstance(coverage, dict):
        violations.append(f"{card_id}: merge.coverage must be an object")
        coverage = {}
    else:
        unknown = sorted(set(coverage) - set(MERGE_SURFACE_PREFIX))
        if unknown:
            violations.append(
                f"{card_id}: unknown coverage class(es): {unknown}"
            )
    coverage_units = set()
    for key, prefix in MERGE_SURFACE_PREFIX.items():
        items = coverage.get(key) or []
        if not isinstance(items, list):
            violations.append(f"{card_id}: merge.coverage.{key} must be an array")
            continue
        for item in items:
            if isinstance(item, str) and item:
                coverage_units.add(f"{prefix}:{item}")

    required = _surface_units(target) | _surface_units(candidate)
    dropped = required - removed_units - locked_units - coverage_units
    if dropped:
        violations.append(
            f"{card_id}: merge silently drops surface unit(s): {sorted(dropped)}"
        )
    inflated = coverage_units - required
    if inflated:
        violations.append(
            f"{card_id}: merge coverage declares unit(s) absent from both sides: "
            f"{sorted(inflated)}"
        )

    recall = block.get("recall_probes")
    if not isinstance(recall, list):
        violations.append(f"{card_id}: merge.recall_probes must be an array")
        recall = []
    if not recall:
        violations.append(f"{card_id}: merge recall gate requires a probe")
    target_probes = _retained_probe_ids(target_id, probes) if target_id else set()
    candidate_probes = set(candidate.get("retention_probes") or [])
    own_probes = {
        record.get("qid")
        for record in probes
        if isinstance(record, dict)
        and record.get("card_id") == card_id
        and record.get("kind") in {"deliver", "validity"}
        and record.get("retained")
    }
    missing_recall = (
        target_probes | candidate_probes | own_probes
    ) - set(recall)
    if missing_recall:
        violations.append(
            f"{card_id}: merge recall gate omits retained probe(s): "
            f"{sorted(missing_recall)}"
        )
    by_qid = {
        record.get("qid"): record
        for record in probes
        if isinstance(record, dict)
    }
    for qid in recall:
        if not isinstance(qid, str) or not qid:
            violations.append(f"{card_id}: recall probe id must be a string")
            continue
        record = by_qid.get(qid)
        if record is None:
            violations.append(f"{card_id}: recall probe {qid} is not declared")
        elif record.get("passed") is False:
            violations.append(f"{card_id}: recall probe {qid} failed")

    interaction = block.get("interaction")
    beta = None
    if not isinstance(interaction, dict):
        violations.append(f"{card_id}: merge.interaction must be an object")
    else:
        beta = interaction.get("beta")
        if not _is_number(beta):
            violations.append(f"{card_id}: merge.interaction.beta must be a number")
    if _is_number(beta) and beta < NEGATIVE_INTERACTION:
        if interaction.get("checked") is not True:
            violations.append(
                f"{card_id}: interaction beta {beta:g} below "
                f"{NEGATIVE_INTERACTION:g} requires an extended regression check"
            )
        elif not str(interaction.get("evidence") or "").strip():
            violations.append(
                f"{card_id}: extended interaction check has no evidence"
            )

    level = block.get("evidence_level")
    if level not in MERGE_EVIDENCE_LEVELS:
        violations.append(
            f"{card_id}: merge.evidence_level must be one of "
            f"{sorted(MERGE_EVIDENCE_LEVELS)}"
        )
    elif level == "statistical":
        causal = block.get("causal_evidence")
        if not isinstance(causal, dict):
            causal = {}
        trials = causal.get("n_trials")
        if causal.get("design") != "randomized" or not (
            isinstance(trials, int) and not isinstance(trials, bool) and trials > 0
        ):
            violations.append(
                f"{card_id}: statistical merge requires randomized evidence "
                "with n_trials > 0"
            )

    before = block.get("surface_tokens_before")
    after = block.get("surface_tokens_after")
    if not _is_number(before) or not _is_number(after):
        violations.append(
            f"{card_id}: merge surface token counts must be numbers"
        )
    elif after > before:
        violations.append(
            f"{card_id}: merge inflates surface tokens: {before:g} -> {after:g}"
        )
    return violations


def _retained_probe_ids(owner, probes):
    return {
        record.get("qid")
        for record in probes
        if record.get("owner") == owner
        and record.get("retained")
        and record.get("card_id") in (None, owner)
    }


def check_candidate_lifecycle(candidate, entries, probes):
    """Check the card-level upgrade/merge claims that mutate an existing entry.

    The relation witnesses are declared, but a mutation still has to be true of
    the actual entry records: an upgrade source must be a real product/check/
    regime superset, and a merge/upgrade must carry the target's retained probes.
    """
    violations = []
    card_id = candidate.get("card_id", "?")
    action = candidate.get("action")
    target_id = candidate.get("target_entry")
    if action not in {"merge", "upgrade"} or not target_id:
        return violations
    target = entries.get(target_id)
    if target is None:
        return violations

    target_probes = _retained_probe_ids(target_id, probes)
    declared = set(candidate.get("retention_probes", []) or [])
    missing = target_probes - declared
    if missing:
        violations.append(
            f"{card_id}: {action} must carry the target's retained probes: "
            f"{sorted(missing)}"
        )

    if action == "upgrade":
        if not _products(target) <= _products(candidate):
            violations.append(
                f"{card_id}: upgrade source does not deliver a superset of "
                f"{target_id}'s products"
            )
        if not _checks(target) <= _checks(candidate):
            violations.append(
                f"{card_id}: upgrade source does not carry a superset of "
                f"{target_id}'s checks"
            )
        if not _regime_tags(target) <= _regime_tags(candidate):
            violations.append(
                f"{card_id}: upgrade source does not cover a superset of "
                f"{target_id}'s regime"
            )
        if not candidate.get("test_contract"):
            violations.append(f"{card_id}: upgrade requires the source test contract")
        if not target.get("test_contract"):
            violations.append(f"{card_id}: upgrade requires the target test contract")
    return violations


def _format_shadow(qid, margin, contributions, score):
    parts = [f"{margin:g}"]
    for _, delta in contributions:
        sign = "+" if delta >= 0 else "-"
        parts.append(f"{sign} {abs(delta):g}")
    return f"joint shadow on {qid}: {' '.join(parts)} = {score:g}"


def _set_test_result(doc):
    violations = []
    probes = doc.get("probes", []) or []
    candidates = doc.get("candidates", []) or []
    plan = doc.get("plan", {}) or {}
    accepted = set(plan.get("accepted", []) or [])
    demoted = set(plan.get("demoted", []) or [])
    by_id = {card.get("card_id"): card for card in candidates}

    retained_results = []
    for record in probes:
        if not record.get("retained"):
            continue
        qid = record.get("qid", "?")
        margin = float(record.get("margin", 0.0))
        contributions = []
        for card_id in accepted:
            if card_id in demoted:
                continue
            card = by_id.get(card_id)
            if not card:
                continue
            delta = (card.get("probe_effects") or {}).get(qid)
            if delta:
                contributions.append({"card_id": card_id, "delta": float(delta)})
        score = margin + sum(item["delta"] for item in contributions)
        passed = score >= 0
        retained_results.append({
            "qid": qid,
            "owner": record.get("owner"),
            "margin": margin,
            "contributions": contributions,
            "score": round(score, 6),
            "passed": passed,
        })
        if not passed:
            violations.append(
                _format_shadow(
                    qid, margin,
                    [(item["card_id"], item["delta"]) for item in contributions],
                    score,
                )
            )

    new_results = []
    for card in candidates:
        action = card.get("action")
        if action in NON_DELIVERING_ACTIONS:
            continue
        owner = card.get("card_id") if action in NEW_ROUTABLE_ACTIONS else (
            card.get("target_entry") or card.get("card_id")
        )
        deliver = next(
            (
                record for record in probes
                if record.get("kind") == "deliver"
                and record.get("owner") == owner
                and record.get("card_id") == card.get("card_id")
            ),
            None,
        )
        if deliver is None:
            continue
        passed = deliver.get("passed", True) is not False
        new_results.append({
            "qid": deliver.get("qid"),
            "owner": owner,
            "card_id": card.get("card_id"),
            "passed": passed,
        })
        if not passed:
            violations.append(f"new probe failed: {deliver.get('qid')}")

    conflicts = list(doc.get("conflicts", []) or [])
    for card in candidates:
        if card.get("relation") != "hard-conflict":
            continue
        pair = (card.get("card_id"), card.get("target_entry"))
        if not any(
            {item.get("a"), item.get("b")} == set(pair)
            for item in conflicts
        ):
            conflicts.append({
                "a": pair[0],
                "b": pair[1],
                "kind": "procedure",
                "evidence": "declared hard-conflict",
            })

    budget = (doc.get("host") or {}).get("budget") or {}
    after = budget.get("context_tokens_after", 0)
    limit = budget.get("limit", 0)
    for card_id in demoted:
        if card_id not in by_id:
            violations.append(
                f"demoted id {card_id!r} is not a candidate; it cannot reduce the "
                "default surface"
            )
    over_budget = after > limit
    budget_passed = not over_budget or bool(demoted)
    if not budget_passed:
        violations.append(
            f"over budget: {after} > {limit} and no entry is demoted"
        )

    passed = not violations
    if passed:
        reason = "all retained probes pass; budget within limit"
    else:
        reason = "; ".join(violations)
    return {
        "retained_probes": retained_results,
        "new_probes": new_results,
        "conflicts": conflicts,
        "budget": {
            "context_tokens_before": budget.get("context_tokens_before", 0),
            "context_tokens_after": after,
            "limit": limit,
            "demoted": sorted(demoted),
        },
        "passed": passed,
        "reason": reason,
    }, violations


def check_set_test(doc):
    _, violations = _set_test_result(doc)
    return violations


def check_budget(doc):
    violations = []
    budget = (doc.get("host") or {}).get("budget") or {}
    after = budget.get("context_tokens_after", 0)
    limit = budget.get("limit", 0)
    demoted = (doc.get("plan") or {}).get("demoted", []) or []
    candidate_ids = {
        card.get("card_id") for card in (doc.get("candidates", []) or [])
    }
    for card_id in demoted:
        if card_id not in candidate_ids:
            violations.append(
                f"demoted id {card_id!r} is not a candidate; it cannot reduce the "
                "default surface"
            )
    if after > limit and not demoted:
        violations.append(
            f"over budget: {after} > {limit} and no entry is demoted"
        )
    return violations


def check_probes(doc):
    violations = []
    host_entries = (doc.get("host") or {}).get("entries", []) or []
    candidates = doc.get("candidates", []) or []
    probes = doc.get("probes", []) or []
    owner_ids = {record.get("id") for record in host_entries}
    owner_ids.update(card.get("card_id") for card in candidates)

    qids = set()
    for index, record in enumerate(probes):
        prefix = f"probe[{index}]"
        for key in ("qid", "text", "owner", "expected", "kind", "retained"):
            if key not in record:
                violations.append(f"{prefix}: missing {key}")
        qid = record.get("qid")
        if qid in qids:
            violations.append(f"{prefix}: duplicate qid {qid}")
        qids.add(qid)
        if record.get("kind") not in {"route", "deliver", "validity"}:
            violations.append(f"{prefix}: invalid kind {record.get('kind')!r}")
        if record.get("owner") not in owner_ids:
            violations.append(f"{prefix}: unknown owner {record.get('owner')!r}")
        if not record.get("text"):
            violations.append(f"{prefix}: text must be non-empty")
        if not record.get("expected"):
            violations.append(f"{prefix}: expected must be non-empty")

    candidate_ids = {card.get("card_id") for card in candidates}
    for index, record in enumerate(probes):
        card_id = record.get("card_id")
        if card_id is not None and card_id not in candidate_ids:
            violations.append(
                f"probe[{index}]: card_id {card_id!r} is not a candidate"
            )

    def has(kind, owner, card_id=None):
        for record in probes:
            if record.get("kind") != kind or record.get("owner") != owner:
                continue
            if card_id is None or record.get("card_id") == card_id:
                return True
        return False

    for record in host_entries:
        entry_id = record.get("id")
        if not has("route", entry_id):
            violations.append(f"{entry_id}: missing route probe")

    for card in candidates:
        card_id = card.get("card_id")
        action = card.get("action")
        if action in NEW_ROUTABLE_ACTIONS and not has("route", card_id):
            violations.append(f"{card_id}: missing route probe for a new entry")
        if action in NON_DELIVERING_ACTIONS:
            continue
        owner = card_id if action in NEW_ROUTABLE_ACTIONS else (
            card.get("target_entry") or card_id
        )
        if not has("deliver", owner, card_id):
            violations.append(
                f"{card_id}: missing deliver probe owned by {owner} and card_id {card_id}"
            )
        if card.get("has_validity") and not has("validity", owner, card_id):
            violations.append(
                f"{card_id}: missing validity probe owned by {owner} and card_id {card_id}"
            )

    for card in candidates:
        card_id = card.get("card_id")
        for qid in card.get("retention_probes", []) or []:
            if qid not in qids:
                violations.append(
                    f"{card_id}: retention probe {qid} is not declared"
                )
                continue
            record = next(item for item in probes if item.get("qid") == qid)
            if not record.get("retained"):
                violations.append(
                    f"{card_id}: retention probe {qid} is not retained"
                )
    return violations


def check_lifecycle(doc):
    violations = []
    entries = {
        record.get("id"): dict(record)
        for record in ((doc.get("host") or {}).get("entries", []) or [])
    }
    candidates = doc.get("candidates", []) or []
    candidate_by_id = {card.get("card_id"): card for card in candidates}
    for card in candidates:
        card_id = card.get("card_id")
        if card.get("action") in NON_DELIVERING_ACTIONS:
            continue
        if card_id and card_id not in entries:
            entries[card_id] = _candidate_as_entry(card)

    probes = doc.get("probes", []) or []
    probe_owner = {record.get("qid"): record.get("owner") for record in probes}
    probe_retained = {
        record.get("qid"): bool(record.get("retained")) for record in probes
    }
    obligations = doc.get("obligations", []) or []
    live_ids = {
        obligation.get("id")
        for obligation in obligations
        if obligation.get("live")
    }

    for index, item in enumerate(doc.get("lifecycle", []) or []):
        prefix = f"lifecycle[{index}]"
        for key in ("action", "target", "sources", "reason", "probes", "rollback"):
            if key not in item:
                violations.append(f"{prefix}: missing {key}")
        action = item.get("action")
        target = item.get("target")
        sources = item.get("sources", []) or []
        if action not in ACTIONS:
            violations.append(f"{prefix}: unknown action {action!r}")
            continue
        if not item.get("reason"):
            violations.append(f"{prefix}: reason must be non-empty")
        if not item.get("rollback"):
            violations.append(f"{prefix}: rollback must be non-empty")
        for qid in item.get("probes", []) or []:
            if qid not in probe_owner:
                violations.append(f"{prefix}: probe {qid!r} is not declared")

        for card_id in [target] + list(sources):
            card = candidate_by_id.get(card_id)
            if card and card.get("action") != action:
                violations.append(
                    f"{card_id}: lifecycle action {action} does not match "
                    f"card action {card.get('action')}"
                )

        if action == "retire":
            if target not in entries:
                violations.append(f"{prefix}: retire target {target!r} does not exist")
                continue
            delivered = _products(entries[target]) & live_ids
            if delivered:
                violations.append(
                    f"{target} still delivers live obligation "
                    f"{sorted(delivered)[0]}; retire requires no live obligation"
                )
            retained_owned = [
                qid for qid, owner in probe_owner.items()
                if owner == target and probe_retained.get(qid)
            ]
            if retained_owned:
                violations.append(
                    f"{target}: cannot retire while retained probes depend on it: "
                    f"{sorted(retained_owned)}"
                )
            del entries[target]
        elif action == "upgrade":
            if target not in entries:
                violations.append(f"{prefix}: upgrade target {target!r} does not exist")
                continue
            if not sources:
                violations.append(f"{prefix}: upgrade requires a source")
                continue
            if len(sources) > 1:
                violations.append(
                    f"{prefix}: upgrade takes exactly one source, got {sources}"
                )
                continue
            source = sources[0]
            if source not in entries:
                violations.append(f"{prefix}: upgrade source {source!r} does not exist")
                continue
            if not entries[target].get("test_contract"):
                violations.append(
                    f"{target}: upgrade requires the target test contract"
                )
            if not entries[source].get("test_contract"):
                violations.append(
                    f"{source}: upgrade requires the source test contract"
                )
            if not _products(entries[target]) <= _products(entries[source]):
                violations.append(
                    f"{source}: upgrade source does not deliver a superset of "
                    f"{target}'s products"
                )
            if not _checks(entries[target]) <= _checks(entries[source]):
                violations.append(
                    f"{source}: upgrade source does not carry a superset of "
                    f"{target}'s checks"
                )
            if not _regime_tags(entries[target]) <= _regime_tags(entries[source]):
                violations.append(
                    f"{source}: upgrade source does not cover a superset of "
                    f"{target}'s regime"
                )
            for qid, owner in list(probe_owner.items()):
                if owner == target and probe_retained.get(qid):
                    probe_owner[qid] = source
            del entries[target]
        elif action == "merge":
            if target not in entries:
                violations.append(f"{prefix}: merge target {target!r} does not exist")
                continue
            if not sources:
                violations.append(f"{prefix}: merge requires at least one source")
                continue
            for source in sources:
                if source not in entries:
                    violations.append(f"{prefix}: merge source {source!r} does not exist")
                    continue
                for entry_id in (target, source):
                    if not entries[entry_id].get("test_contract"):
                        violations.append(
                            f"{entry_id}: merge requires a test contract"
                        )
                same_entry = (
                    _products(entries[target]) == _products(entries[source])
                    and entries[target].get("procedure")
                    == entries[source].get("procedure")
                    and _regime_tags(entries[target]) == _regime_tags(entries[source])
                )
                if not same_entry:
                    violations.append(
                        f"{source}: merge source is not a duplicate of {target} "
                        "(products, procedure, and regime must match)"
                    )
                    continue
                for qid, owner in list(probe_owner.items()):
                    if owner == source and probe_retained.get(qid):
                        probe_owner[qid] = target
                entries[target]["products"] = sorted(
                    _products(entries[target]) | _products(entries[source])
                )
                entries[target]["checks"] = sorted(
                    _checks(entries[target]) | _checks(entries[source])
                )
                entries[target]["provenance"] = sorted(
                    _provenance(entries[target]) | _provenance(entries[source])
                )
                merged_tags = _regime_tags(entries[target]) & _regime_tags(entries[source])
                regime = dict(entries[target].get("regime") or {})
                regime["tags"] = sorted(merged_tags)
                entries[target]["regime"] = regime
                if source != target:
                    del entries[source]
        elif action == "demote":
            if target not in entries:
                violations.append(f"{prefix}: demote target {target!r} does not exist")
        elif action == "split":
            for source in sources:
                if source not in entries:
                    violations.append(f"{prefix}: split source {source!r} does not exist")
        elif action == "new-entry":
            if target and target not in entries:
                violations.append(f"{prefix}: new-entry target {target!r} does not exist")

    for obligation_id in live_ids:
        if not any(
            obligation_id in _products(record) for record in entries.values()
        ):
            violations.append(
                f"live obligation {obligation_id} has no deliverer after the "
                "lifecycle plan"
            )
    return violations


def _metrics(doc):
    host_entries = (doc.get("host") or {}).get("entries", []) or []
    candidates = doc.get("candidates", []) or []
    probes = doc.get("probes", []) or []
    plan = doc.get("plan", {}) or {}
    accepted = set(plan.get("accepted", []) or [])
    obligations = doc.get("obligations", []) or []

    retained_owners = {
        record.get("owner") for record in probes if record.get("retained")
    }
    entries = {
        record.get("id"): record for record in host_entries
    }
    for card in candidates:
        card_id = card.get("card_id")
        if card_id in accepted:
            entries[card_id] = _candidate_as_entry(card)
    live = [item for item in obligations if item.get("live")]
    live_ids = {item.get("id") for item in live}
    if live:
        covered = sum(
            1 for item in live
            if any(item.get("id") in _products(record) for record in entries.values())
        )
        coverage = round(covered / len(live), 4)
    else:
        coverage = 1.0
    return {
        "entry_count": len(host_entries),
        "duplicate_count": sum(
            1 for card in candidates if card.get("relation") == "duplicate"
        ),
        "hard_conflict_count": sum(
            1 for card in candidates if card.get("relation") == "hard-conflict"
        ),
        "orphan_count": sum(
            1 for record in host_entries
            if not (_products(record) & live_ids)
            and record.get("id") not in retained_owners
        ),
        "portfolio_coverage": coverage,
    }


def run(doc):
    violations = []
    violations.extend(validate_portfolio(doc))
    entries = {
        record.get("id"): record
        for record in ((doc.get("host") or {}).get("entries", []) or [])
    }
    candidates = doc.get("candidates", []) or []
    obligations = doc.get("obligations", []) or []
    probes = doc.get("probes", []) or []
    for card in candidates:
        violations.extend(check_relation(card, entries))
        violations.extend(check_action(card))
        violations.extend(check_merge(card, entries, obligations))
        violations.extend(check_merge_evidence(card, entries, probes))
        violations.extend(check_candidate_lifecycle(card, entries, probes))
    violations.extend(check_lifecycle(doc))
    violations.extend(check_probes(doc))
    set_test, set_test_violations = _set_test_result(doc)
    violations.extend(set_test_violations)

    plan = [
        {
            "card_id": card.get("card_id"),
            "relation": card.get("relation"),
            "action": card.get("action"),
            "target_entry": card.get("target_entry"),
        }
        for card in candidates
    ]
    plan.sort(key=lambda item: (str(item.get("action")), str(item.get("card_id"))))
    return {
        "violations": violations,
        "plan": plan,
        "metrics": _metrics(doc),
        "set_test": set_test,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check a cap-align portfolio admission plan (static, no execution)."
    )
    parser.add_argument("input", type=Path, help="portfolio-input.json")
    parser.add_argument("--json", action="store_true", help="print JSON")
    args = parser.parse_args(argv)

    doc = load_portfolio(args.input)
    result = run(doc)
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        if result["violations"]:
            for violation in result["violations"]:
                print(f"VIOLATION: {violation}")
        else:
            print("ok: no violations")
        print(
            "metrics: "
            + json.dumps(result["metrics"], sort_keys=True)
        )
    return 0 if not result["violations"] else 1


if __name__ == "__main__":
    sys.exit(main())
