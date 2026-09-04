#!/usr/bin/env python3
"""Structural and claim-state checks for the post-synthesis decision path.

This validates routing consistency only.  It does not prove any analytic
estimate, a zero-free strip, or RH.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "results/context/zeta23_post_synthesis_decision_path_v1.json"
REPORT = ROOT / "results/ZETA23-POST-SYNTHESIS-DECISION-PATH-2026-09-02.md"
sys.path.insert(0, str(ROOT / "src"))
from zeta23_proof_tree import load_current_authority_bundle


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    load_current_authority_bundle()
    data = json.loads(CACHE.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    require(data["schema"] == "zeta23_post_synthesis_decision_path_v1", "schema drift")
    global_status = data["global_status"]
    require(global_status["riemann_hypothesis"] == "OPEN", "RH claim drift")
    require(global_status["uniform_zero_free_strip"] == "OPEN", "strip claim drift")
    require(global_status["strip_to_rh_amplifier"] == "ABSENT", "amplifier claim drift")
    require(global_status["universal_completed_zeta_knc"] == "OPEN_RH_EQUIVALENT", "KNC drift")

    stages = data["selected_strip_route"]["stages"]
    require([stage["id"] for stage in stages] == ["S0", "S1", "S2", "S3", "S4"], "stage order drift")
    require(stages[0]["status"] == "COMPLETE_GO_FAILED_BRANCH_SWITCH_FIRED", "S0 verdict drift")
    require(
        stages[1]["status"]
        == "RAW_CANDIDATE_A0_FAILED_BOTH_MECHANISM_CLASSES_UNFORMULATED",
        "S1 candidate disposition drift",
    )
    require(stages[0]["source"].endswith("ADAPTER-INTEGRITY-AUDIT-2026-09-02.md"), "S0 source drift")
    require(stages[2]["red_debts"] == 1, "S2 must be the only planned red analytic debt")
    require(sum(stage["red_debts"] for stage in stages) == 1, "active route contains multiple red debts")
    require(stages[4]["nonclaim"].startswith("Does not imply RH"), "S4 lost RH nonclaim")

    s1 = stages[1]
    require(s1["candidate_limit"] == 2, "S1 bounded-sprint rule drift")
    require(len(s1["candidate_classes"]) == 2, "S1 candidate-class drift")
    require(
        s1["candidate_a0_result"]
        == "FAIL_ADMISSION_TAUTOLOGICAL_C_STAR_ONE_EQUALS_LAMBDA_REEXPANSION",
        "S1-A0 tautology correction drift",
    )
    require(
        s1["candidate_a_structural_class_status"] == "UNFORMULATED_NOT_CLOSED_BY_A0",
        "raw re-expansion improperly closed the structural mechanism class",
    )

    attack = data["selected_strip_route"]["attack_surface"]
    require(attack["status"] == "OPEN_STRIP_EQUIVALENT_ENDPOINT", "endpoint strength drift")
    require("O_full" in attack["formula"] and "=E_Q" in attack["formula"], "R128 equality missing")
    require("0<kappa<=1" in attack["target_scale"], "endpoint exponent domain drift")
    require(
        attack["local_r116_packet"]["status"]
        == "LOCAL_MEMBER_NO_PROVED_ORDER_REFLECTION_ACTUAL_INDEFINITENESS_UNCERTIFIED",
        "R116 packet trust/order-reflection drift",
    )
    require(attack["optional_r123_fixed_window_fork"]["positive_strip_condition"] == "kappa>1/(k+1)", "fixed-k loss drift")
    require(
        attack["optional_r123_fixed_window_fork"]["status"]
        == "EXACT_SCALE_REPLICATION_NOT_A_REDUCTION",
        "R123/R125 rescaled endpoint promoted as a reduction",
    )

    falsifiers = {item["id"] for item in data["mandatory_falsifiers"]}
    for required in ("R178", "R179_SYMMETRIC_QUARTET", "R121", "EARLY_CAUCHY"):
        require(required in falsifiers, f"missing mandatory falsifier: {required}")

    source_paths = data["sources"]
    require(len(source_paths) == len(set(source_paths)), "duplicate source path")
    for source in source_paths:
        require((ROOT / source).exists(), f"missing source: {source}")

    leverage = data["theorem_leverage"]
    require(not any(item["role"] == "DIRECT_STRIP_INPUT" for item in leverage), "unsupported direct theorem bridge")
    require(data["qp_fallback"]["status"] == "CONDITIONAL_ON_S1_STOP", "QP fallback promoted too early")
    require(data["parallel_rh_lane"]["status"] == "OPEN_RH_EQUIVALENT", "RH lane strength drift")
    require(data["debt_policy"]["active_sprint_limit"] == "At most one red debt.", "red-debt limit drift")
    corrections = {item["source"] for item in data["routing_corrections"]}
    require("S0_adapter_audit" in corrections, "S0 correction not propagated")

    lower = report.lower()
    for phrase in (
        "no uniform zero-free strip and no proof of rh",
        "uniform strip --x--> rh",
        "adapter-integrity audit",
        "primitive-only go condition failed",
        "complete-family",
        "reflection-odd",
        "strip-equivalent",
    ):
        require(phrase in lower, f"report lost required guardrail: {phrase}")

    print("PASS: post-synthesis decision path structure and claim-state discipline")
    print("NOTE: this checker records S0's negative verdict; it does not prove S1-S4")


if __name__ == "__main__":
    main()
