"""Unit tests for research/tools/portfolio-model.py (stdlib only)."""

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("portfolio-model.py")
if not MODULE_PATH.exists():
    raise FileNotFoundError(f"missing implementation: {MODULE_PATH}")
spec = importlib.util.spec_from_file_location("portfolio_model", MODULE_PATH)
if spec is None or spec.loader is None:
    raise ImportError(f"cannot load {MODULE_PATH}")
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)

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


def evidence(**overrides):
    base = {key: False for key in EVIDENCE_KEYS}
    base.update(overrides)
    return base


def entry(entry_id, products, **overrides):
    record = {
        "id": entry_id,
        "question": f"question-{entry_id}",
        "products": list(products),
        "preconditions": ["input"],
        "postconditions": ["output"],
        "regime": {"claim": "bulk, harmonic", "tags": ["bulk", "harmonic"]},
        "procedure": f"procedure-{entry_id}",
        "checks": [f"check-{entry_id}"],
        "provenance": [f"source-{entry_id}"],
        "test_contract": {
            "fail_before": f"fails before {entry_id}",
            "pass_after": f"passes after {entry_id}",
            "destroy": f"destroy {entry_id}",
        },
    }
    record.update(overrides)
    return record


def candidate(card_id, relation, action, target_entry=None, **overrides):
    record = {
        "card_id": card_id,
        "relation": relation,
        "relation_evidence": evidence(),
        "action": action,
        "target_entry": target_entry,
        "products": [f"product-{card_id}"],
        "preconditions": ["input"],
        "postconditions": ["output"],
        "regime": {"claim": "bulk", "tags": ["bulk"]},
        "procedure": f"procedure-{card_id}",
        "checks": [f"check-{card_id}"],
        "provenance": [f"source-{card_id}"],
        "has_validity": False,
        "retention_probes": [],
        "probe_effects": {},
        "test_contract": {
            "fail_before": f"fails before {card_id}",
            "pass_after": f"passes after {card_id}",
            "destroy": f"destroy {card_id}",
        },
        "rollback": f"remove {card_id}",
    }
    record.update(overrides)
    return record


def document(entries=None, candidates=None, probes=None, obligations=None,
             lifecycle=None, plan=None, budget=None):
    return {
        "host": {
            "entries": list(entries or []),
            "budget": budget or {
                "context_tokens_before": 100,
                "context_tokens_after": 110,
                "limit": 130,
            },
        },
        "candidates": list(candidates or []),
        "plan": plan or {"accepted": [], "demoted": []},
        "probes": list(probes or []),
        "obligations": list(obligations or []),
        "lifecycle": list(lifecycle or []),
    }


def merge_block(card_id, **overrides):
    block = {
        "witnesses": [
            {
                "unit": f"entry:{card_id}",
                "kind": "W1",
                "evidence": "the candidate repeats the target's product, "
                            "procedure, and regime",
            }
        ],
        "removed_units": [f"entry:{card_id}"],
        "locked_residual": [],
        "coverage": {
            "triggers": [],
            "workflow_edges": [],
            "tool_requirements": [],
            "obligations": [],
            "output_fields": [],
        },
        "recall_probes": ["q-eos-route"],
        "interaction": {"beta": 0.0, "checked": False},
        "evidence_level": "constructive",
        "surface_tokens_before": 100,
        "surface_tokens_after": 80,
    }
    block.update(overrides)
    return block


def probe(qid, owner, kind="route", retained=True, margin=0.5, **overrides):
    record = {
        "qid": qid,
        "text": f"question for {qid}",
        "owner": owner,
        "expected": f"expected for {qid}",
        "kind": kind,
        "retained": retained,
        "margin": margin,
    }
    record.update(overrides)
    return record


class RelationTests(unittest.TestCase):
    def test_relation_consistency_valid(self):
        eos = entry("eos", ["eos-fit"])
        card = candidate(
            "eos-dup", "duplicate", "merge", "eos",
            relation_evidence=evidence(
                same_product=True, same_procedure=True, same_regime=True,
            ),
            products=["eos-fit"], checks=["check-eos"],
        )
        self.assertEqual(pm.check_relation(card, {"eos": eos}), [])

    def test_duplicate_requires_same_procedure_and_regime(self):
        eos = entry("eos", ["eos-fit"])
        no_procedure = candidate(
            "eos-dup", "duplicate", "merge", "eos",
            relation_evidence=evidence(
                same_product=True, same_procedure=False, same_regime=True,
            ),
        )
        no_regime = candidate(
            "eos-dup", "duplicate", "merge", "eos",
            relation_evidence=evidence(
                same_product=True, same_procedure=True, same_regime=False,
            ),
        )
        self.assertTrue(pm.check_relation(no_procedure, {"eos": eos}))
        self.assertTrue(pm.check_relation(no_regime, {"eos": eos}))

    def test_variant_requires_disjoint_regime(self):
        heat = entry("heat-flow", ["lattice-kappa"])
        overlapping = candidate(
            "kappa-slack", "variant", "split", "heat-flow",
            relation_evidence=evidence(
                same_product=True, same_procedure=False, regime_overlap=True,
            ),
        )
        disjoint = candidate(
            "kappa-slack", "variant", "split", "heat-flow",
            relation_evidence=evidence(
                same_product=True, same_procedure=False, regime_overlap=False,
            ),
        )
        self.assertTrue(pm.check_relation(overlapping, {"heat-flow": heat}))
        self.assertEqual(pm.check_relation(disjoint, {"heat-flow": heat}), [])

    def test_hard_conflict_requires_overlap(self):
        heat = entry("heat-flow", ["lattice-kappa"])
        disjoint = candidate(
            "kappa-slack", "hard-conflict", "quarantine", "heat-flow",
            relation_evidence=evidence(
                same_product=True, same_procedure=False, regime_overlap=False,
            ),
        )
        self.assertTrue(pm.check_relation(disjoint, {"heat-flow": heat}))

    def test_description_overlap_is_not_duplicate(self):
        eos = entry("eos", ["eos-fit"], description="equation of state fit")
        adjacent = candidate(
            "qha", "adjacent", "extend", "eos",
            relation_evidence=evidence(question_overlap=True),
            products=["thermal-expansion"],
        )
        self.assertEqual(pm.check_relation(adjacent, {"eos": eos}), [])
        self.assertEqual(pm.check_action(adjacent), [])

        wrong_relation = candidate(
            "qha", "duplicate", "merge", "eos",
            relation_evidence=evidence(question_overlap=True),
            products=["thermal-expansion"],
        )
        self.assertTrue(pm.check_relation(wrong_relation, {"eos": eos}))

        wrong_action = candidate(
            "qha", "adjacent", "merge", "eos",
            relation_evidence=evidence(question_overlap=True),
        )
        self.assertTrue(pm.check_action(wrong_action))


class MergeTests(unittest.TestCase):
    def test_merge_preserves_live_obligations(self):
        eos = entry("eos", ["eos-fit", "eos-elastic"])
        card = candidate(
            "eos-dup", "duplicate", "merge", "eos",
            relation_evidence=evidence(
                same_product=True, same_procedure=True, same_regime=True,
            ),
            products=["eos-fit"], checks=["check-eos"],
            provenance=["source-eos"],
        )
        violations = pm.check_merge(
            card, {"eos": eos}, [{"id": "eos-elastic", "live": True}],
        )
        self.assertTrue(any("eos-elastic" in v or "product" in v for v in violations))

    def test_merge_requires_both_test_contracts(self):
        eos = entry("eos", ["eos-fit"])
        card = candidate(
            "eos-dup", "duplicate", "merge", "eos",
            relation_evidence=evidence(
                same_product=True, same_procedure=True, same_regime=True,
            ),
            products=["eos-fit"], checks=["check-eos"],
            provenance=["source-eos"],
        )
        del card["test_contract"]
        violations = pm.check_merge(card, {"eos": eos}, [])
        self.assertTrue(any("test contract" in v for v in violations))


class LifecycleTests(unittest.TestCase):
    def test_retire_live_obligation_rejected(self):
        doc = document(
            entries=[entry("heat-flow", ["lattice-kappa"])],
            obligations=[{"id": "lattice-kappa", "live": True}],
            lifecycle=[{
                "action": "retire", "target": "heat-flow", "sources": [],
                "reason": "old", "probes": [], "rollback": "restore heat-flow",
            }],
        )
        violations = pm.check_lifecycle(doc)
        self.assertTrue(any("lattice-kappa" in v for v in violations))

    def test_retire_unreachable_allowed(self):
        doc = document(
            entries=[entry("qha-old", ["thermal-expansion"])],
            obligations=[{"id": "thermal-expansion", "live": False}],
            probes=[probe("q-qha-old", "qha-old", retained=False)],
            lifecycle=[{
                "action": "retire", "target": "qha-old", "sources": [],
                "reason": "orphan", "probes": [], "rollback": "restore qha-old",
            }],
        )
        self.assertEqual(pm.check_lifecycle(doc), [])

    def test_upgrade_requires_superset(self):
        doc = document(
            entries=[
                entry("eos-old", ["eos-fit"]),
                entry("eos-new", ["eos-fit"]),
            ],
            lifecycle=[{
                "action": "upgrade", "target": "eos-old", "sources": ["eos-new"],
                "reason": "stronger", "probes": [], "rollback": "restore eos-old",
            }],
        )
        violations = pm.check_lifecycle(doc)
        self.assertTrue(any("superset" in v for v in violations))


class SetTestTests(unittest.TestCase):
    def _shadow_doc(self, accepted, demoted):
        heat = entry("heat-flow", ["lattice-kappa"])
        qha = candidate(
            "qha", "adjacent", "new-entry", "heat-flow",
            relation_evidence=evidence(question_overlap=True),
            products=["thermal-expansion"],
            probe_effects={"q-heat-flow-route": -0.2},
        )
        kappa = candidate(
            "kappa-bte-lowT", "partial", "split", "heat-flow",
            relation_evidence=evidence(
                same_product=True, same_procedure=True, regime_subset=False,
            ),
            products=["lattice-kappa"],
            probe_effects={"q-heat-flow-route": -0.2},
        )
        return document(
            entries=[heat], candidates=[qha, kappa],
            probes=[probe("q-heat-flow-route", "heat-flow", margin=0.3)],
            plan={"accepted": accepted, "demoted": demoted},
        )

    def test_joint_shadow_detected(self):
        add_all = self._shadow_doc(["qha", "kappa-bte-lowT"], [])
        self.assertTrue(pm.check_set_test(add_all))

        one_at_a_time = self._shadow_doc(["qha"], [])
        self.assertEqual(pm.check_set_test(one_at_a_time), [])

        gated = self._shadow_doc(["qha", "kappa-bte-lowT"], ["qha"])
        self.assertEqual(pm.check_set_test(gated), [])

    def test_budget_demote(self):
        over = document(
            entries=[entry("eos", ["eos-fit"])],
            candidates=[candidate("qha", "adjacent", "new-entry", "eos",
                                  relation_evidence=evidence(question_overlap=True))],
            budget={
                "context_tokens_before": 100,
                "context_tokens_after": 140,
                "limit": 130,
            },
        )
        self.assertTrue(pm.check_budget(over))
        over["plan"]["demoted"] = ["qha"]
        self.assertEqual(pm.check_budget(over), [])

    def test_card_and_lifecycle_consistent(self):
        card = candidate(
            "qha", "duplicate", "merge", "eos",
            relation_evidence=evidence(
                same_product=True, same_procedure=True, same_regime=True,
            ),
        )
        doc = document(
            entries=[entry("eos", ["eos-fit"])],
            candidates=[card],
            lifecycle=[{
                "action": "upgrade", "target": "qha", "sources": [],
                "reason": "wrong card action", "probes": [], "rollback": "restore",
            }],
        )
        violations = pm.check_lifecycle(doc)
        self.assertTrue(any("qha" in v and "merge" in v for v in violations))


class CandidateLifecycleTests(unittest.TestCase):
    def test_upgrade_card_requires_actual_superset(self):
        eos = entry("eos", ["eos-fit"])
        card = candidate(
            "eos-new", "subsumes", "upgrade", "eos",
            relation_evidence=evidence(
                products_superset=True, checks_superset=True,
                regime_superset=True,
            ),
            products=["something-else"],
        )
        violations = pm.check_candidate_lifecycle(card, {"eos": eos}, [])
        self.assertTrue(any("superset" in v for v in violations))

    def test_upgrade_card_requires_target_probes(self):
        eos = entry("eos", ["eos-fit"])
        card = candidate(
            "eos-new", "subsumes", "upgrade", "eos",
            relation_evidence=evidence(
                products_superset=True, checks_superset=True,
                regime_superset=True,
            ),
            products=["eos-fit", "eos-elastic"],
            checks=["check-eos", "check-elastic"],
            retention_probes=[],
        )
        probes = [probe("q-eos-route", "eos", margin=0.5)]
        violations = pm.check_candidate_lifecycle(card, {"eos": eos}, probes)
        self.assertTrue(any("retained probe" in v for v in violations))

    def test_merge_card_requires_target_probes(self):
        eos = entry("eos", ["eos-fit"])
        card = candidate(
            "eos-dup", "duplicate", "merge", "eos",
            relation_evidence=evidence(
                same_product=True, same_procedure=True, same_regime=True,
            ),
            products=["eos-fit"], checks=["check-eos"],
            provenance=["source-eos"], retention_probes=[],
        )
        probes = [probe("q-eos-route", "eos", margin=0.5)]
        violations = pm.check_candidate_lifecycle(card, {"eos": eos}, probes)
        self.assertTrue(any("retained probe" in v for v in violations))


class CandidateProbeTests(unittest.TestCase):
    def test_deliver_probe_is_per_card(self):
        heat = entry("heat-flow", ["lattice-kappa"])
        qha = candidate("qha", "adjacent", "new-entry", "heat-flow",
                        relation_evidence=evidence(question_overlap=True),
                        products=["thermal-expansion"])
        band = candidate("band", "unrelated", "new-entry", None,
                         products=["band-gap"])
        probes = [
            probe("q-qha-route", "qha"),
            probe("q-band-route", "band"),
            probe("q-qha-deliver", "qha", kind="deliver", card_id="qha"),
        ]
        violations = pm.check_probes(document(
            entries=[heat], candidates=[qha, band], probes=probes,
        ))
        self.assertTrue(any("band" in v and "deliver" in v for v in violations))


class LifecycleMergeTests(unittest.TestCase):
    def _merge_doc(self, entries, lifecycle, probes=None):
        return document(entries=entries, probes=probes or [], lifecycle=lifecycle)

    def test_merge_remaps_retained_probes(self):
        a = entry("a", ["x"], checks=["check-a"], provenance=["a"])
        b = entry("b", ["x"], checks=["check-a"], provenance=["b"],
                  procedure="procedure-a")
        doc = self._merge_doc(
            [a, b],
            [
                {"action": "merge", "target": "a", "sources": ["b"],
                 "reason": "duplicate", "probes": ["q-b"], "rollback": "restore b"},
                {"action": "retire", "target": "a", "sources": [],
                 "reason": "now unreachable", "probes": [], "rollback": "restore a"},
            ],
            probes=[probe("q-b", "b", retained=True)],
        )
        violations = pm.check_lifecycle(doc)
        self.assertTrue(any("retained probes" in v and "a" in v for v in violations))

    def test_merge_requires_contracts_and_duplicate_regime(self):
        a = entry("a", ["x"], checks=["check-a"], provenance=["a"])
        b = entry("b", ["x"], checks=["check-a"], provenance=["b"],
                  regime={"claim": "different", "tags": ["other"]})
        del a["test_contract"]
        del b["test_contract"]
        doc = self._merge_doc(
            [a, b],
            [{"action": "merge", "target": "a", "sources": ["b"],
              "reason": "looks alike", "probes": [], "rollback": "restore b"}],
        )
        violations = pm.check_lifecycle(doc)
        self.assertTrue(any("duplicate" in v for v in violations))
        self.assertTrue(any("test contract" in v for v in violations))


class MetricAndBudgetTests(unittest.TestCase):
    def test_ghost_demotion_does_not_satisfy_budget(self):
        doc = document(
            entries=[entry("eos", ["eos-fit"])],
            budget={"context_tokens_before": 130,
                    "context_tokens_after": 140, "limit": 130},
            plan={"accepted": [], "demoted": ["ghost"]},
        )
        self.assertTrue(any("ghost" in v for v in pm.check_budget(doc)))

    def test_metrics_use_documented_definitions(self):
        old = entry("qha-old", ["thermal-expansion"])
        heat = entry("heat-flow", ["lattice-kappa"])
        qha = candidate("qha", "adjacent", "new-entry", "heat-flow",
                        relation_evidence=evidence(question_overlap=True),
                        products=["thermal-expansion"])
        doc = document(
            entries=[old, heat], candidates=[qha],
            probes=[
                probe("q-old", "qha-old", retained=False),
                probe("q-heat", "heat-flow"),
            ],
            obligations=[
                {"id": "thermal-expansion", "live": False},
                {"id": "lattice-kappa", "live": True},
            ],
            plan={"accepted": ["qha"], "demoted": ["qha"]},
        )
        metrics = pm._metrics(doc)
        self.assertEqual(metrics["orphan_count"], 1)
        self.assertEqual(metrics["portfolio_coverage"], 1.0)


class MergeEvidenceTests(unittest.TestCase):
    def _card(self, **overrides):
        return candidate(
            "eos-dup", "duplicate", "merge", "eos",
            relation_evidence=evidence(
                same_product=True, same_procedure=True, same_regime=True,
            ),
            products=["eos-fit"], checks=["check-eos"],
            provenance=["source-eos"], retention_probes=["q-eos-route"],
            merge=merge_block("eos-dup", **overrides),
        )

    def _check(self, card, eos=None, probes=None):
        eos = eos or entry("eos", ["eos-fit"], checks=["check-eos"],
                           provenance=["source-eos"])
        probes = probes if probes is not None else [
            probe("q-eos-route", "eos", margin=0.5),
        ]
        return pm.check_merge_evidence(card, {"eos": eos}, probes)

    def test_valid_merge_evidence_passes(self):
        self.assertEqual(self._check(self._card()), [])

    def test_every_removed_unit_needs_exactly_one_witness(self):
        no_witness = self._card(
            witnesses=[],
            removed_units=["entry:eos-dup"],
        )
        violations = self._check(no_witness)
        self.assertTrue(any("entry:eos-dup" in v and "witness" in v
                            for v in violations))

        duplicates = self._card(
            witnesses=[
                {"unit": "entry:eos-dup", "kind": "W1", "evidence": "same"},
                {"unit": "entry:eos-dup", "kind": "W2", "evidence": "again"},
            ],
        )
        self.assertTrue(any("more than one witness" in v
                            for v in self._check(duplicates)))

    def test_w3_cannot_delete_prohibition_or_output(self):
        eos = entry("eos", ["eos-fit"], surface={
            "output_fields": ["warn-before-fit"],
            "obligations": ["never-fit-outside-regime"],
        })
        card = self._card(
            witnesses=[
                {"unit": "entry:eos-dup", "kind": "W1", "evidence": "same"},
                {"unit": "output_field:warn-before-fit", "kind": "W3",
                 "evidence": "checker says it follows"},
                {"unit": "obligation:never-fit-outside-regime", "kind": "W3",
                 "evidence": "checker says it follows"},
            ],
            removed_units=[
                "entry:eos-dup",
                "output_field:warn-before-fit",
                "obligation:never-fit-outside-regime",
            ],
        )
        violations = self._check(card, eos=eos)
        self.assertTrue(any("W3" in v and "warn-before-fit" in v
                            for v in violations))
        self.assertTrue(any("W3" in v and "never-fit-outside-regime" in v
                            for v in violations))

    def test_merge_cannot_silently_drop_a_surface_unit(self):
        eos = entry("eos", ["eos-fit"], surface={
            "triggers": ["eos"],
            "workflow_edges": ["eos->check"],
        })
        card = self._card()
        card["surface"] = {
            "triggers": ["eos-dup"],
            "workflow_edges": ["eos-dup->check"],
        }
        violations = self._check(card, eos=eos)
        self.assertTrue(any("silently drops" in v and "trigger:eos" in v
                            for v in violations))
        self.assertTrue(any("workflow_edge:eos->check" in v
                            for v in violations))

    def test_unknown_surface_class_is_rejected(self):
        eos = entry("eos", ["eos-fit"], surface={
            "trigger": ["eos"],
        })
        violations = self._check(self._card(), eos=eos)
        self.assertTrue(any("surface class" in v and "trigger" in v
                            for v in violations))

        coverage = {
            "triggers": [], "workflow_edges": [], "tool_requirements": [],
            "obligations": [], "output_fields": [], "trigger": ["eos"],
        }
        bad_coverage = self._card(coverage=coverage)
        self.assertTrue(any("coverage class" in v and "trigger" in v
                            for v in self._check(bad_coverage)))

    def test_locked_residual_must_be_preserved_verbatim(self):
        eos = entry("eos", ["eos-fit"], surface={
            "triggers": ["eos"],
        })
        card = self._card(
            locked_residual=[{"unit": "trigger:eos", "reason": "unparsable"}],
        )
        violations = self._check(card, eos=eos)
        self.assertTrue(any("verbatim" in v for v in violations))

        fixed = self._card(
            locked_residual=[{
                "unit": "trigger:eos",
                "reason": "unparsable",
                "verbatim": "eos",
            }],
        )
        self.assertEqual(self._check(fixed, eos=eos), [])

    def test_source_entry_removal_is_itself_a_covered_unit(self):
        card = self._card(
            witnesses=[],
            removed_units=[],
        )
        violations = self._check(card)
        self.assertTrue(any("entry:eos-dup" in v for v in violations))

    def test_recall_gate_requires_both_sides_and_no_failure(self):
        missing = self._card(recall_probes=[])
        violations = self._check(missing)
        self.assertTrue(any("q-eos-route" in v for v in violations))

        failed = self._check(
            self._card(),
            probes=[probe("q-eos-route", "eos", passed=False)],
        )
        self.assertTrue(any("recall probe" in v and "failed" in v
                            for v in failed))

    def test_recall_gate_includes_the_candidates_own_probe(self):
        probes = [
            probe("q-eos-route", "eos", margin=0.5),
            probe("q-eos-dup-deliver", "eos", kind="deliver",
                  card_id="eos-dup", margin=0.5),
        ]
        violations = self._check(self._card(), probes=probes)
        self.assertTrue(any("q-eos-dup-deliver" in v for v in violations))

    def test_negative_interaction_requires_extended_check(self):
        unguarded = self._card(
            interaction={"beta": -0.2, "checked": False},
        )
        self.assertTrue(any("interaction" in v and "extended" in v
                            for v in self._check(unguarded)))

        guarded = self._card(
            interaction={"beta": -0.2, "checked": True,
                         "evidence": "interaction regression suite passed"},
        )
        self.assertEqual(self._check(guarded), [])

    def test_merge_never_inflates_surface(self):
        card = self._card(surface_tokens_before=100,
                          surface_tokens_after=120)
        self.assertTrue(any("inflates" in v for v in self._check(card)))

    def test_statistical_level_requires_randomized_evidence(self):
        unsupported = self._card(evidence_level="statistical")
        self.assertTrue(any("statistical" in v and "randomized" in v
                            for v in self._check(unsupported)))

        supported = self._card(
            evidence_level="statistical",
            causal_evidence={"design": "randomized", "n_trials": 40},
        )
        self.assertEqual(self._check(supported), [])


if __name__ == "__main__":
    unittest.main()
