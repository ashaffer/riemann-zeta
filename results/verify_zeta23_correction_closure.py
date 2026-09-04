#!/usr/bin/env python3
"""Replay correction-closure and routing invariants.

This checks exact cross-report statements.  It proves no analytic estimate,
zero-free strip, or RH.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "results/ZETA23-CORRECTION-CLOSURE-AND-FAITHFULNESS-TRILEMMA-2026-09-02.md"
CACHE = ROOT / "results/context/zeta23_correction_closure_v1.json"
sys.path.insert(0, str(ROOT / "src"))
from zeta23_proof_tree import load_current_authority_bundle


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> None:
    load_current_authority_bundle()
    data = json.loads(CACHE.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    require(data["schema"] == "zeta23_correction_closure_v1", "schema drift")
    require(data["global_status"]["uniform_zero_free_strip"] == "OPEN", "strip claim drift")
    require(data["global_status"]["riemann_hypothesis"] == "OPEN", "RH claim drift")
    require(data["corrections"]["r128_global_result"] == "EXACT_EQUALS_ORIGINAL_R71_ENERGY", "R128 drift")
    require(data["corrections"]["r123_r125_status"] == "EXACT_SCALE_REPLICATION_NOT_A_REDUCTION", "R125 drift")
    require(
        data["corrections"]["energy_map"] == "eta=kappa/2 for 0<kappa<=1",
        "energy-map domain drift",
    )
    require(
        data["s1"]["candidate_a0_raw_reexpansion"]
        == "FAIL_ADMISSION_TAUTOLOGICAL_REEXPANSION",
        "S1-A0 drift",
    )
    require(
        data["s1"]["candidate_a_structural_inequality_class"]
        == "UNFORMULATED_NOT_CLOSED",
        "S1 mechanism class was overclosed",
    )
    require(data["r123_conditional_ledger"]["positive_condition"] == "kappa>1/(k+1)", "fixed-k threshold drift")

    cases = {entry["case"]: entry["result"] for entry in data["tested_route_disposition"]}
    require(
        cases["LOCAL_RESTRICTION"]
        == "NO_PROVED_ORDER_REFLECTING_MAP_ACTUAL_INDEFINITENESS_UNCERTIFIED",
        "local case trust drift",
    )
    require(cases["FAITHFUL_RESTORATION"] == "O_FULL_EQUALS_E_Q", "restoration case drift")
    require(cases["FILTERED_FAITHFULNESS"] == "INDEPENDENT_DIRECTION_IS_RESCALED_COMPLETE_FIELD", "filter case drift")
    require(
        data["exhaustiveness_status"]
        == "NOT_PROVED_FOR_COMPOSITIONS_SUBFAMILIES_OR_LINEAR_COMBINATIONS",
        "unproved exhaustion claim revived",
    )

    for source in data["sources"]:
        require((ROOT / source).exists(), f"missing source: {source}")

    r116 = read("results/R116-SIGNED-JOINT-TYPEII-ATTACK.md")
    require("h(c)c^(1-it)" in r116, "outer Mellin phase correction missing")
    require("balanced-packet primitive Mobius correlation" in r116, "R116 local scope missing")

    r121 = read("results/R121-COMPOSITE-CRT-SPARSE-BRIDGE-GATE.md")
    require(
        "balanced squarefree-semiprime packet" in r121
        and "h(c)c^(1-it)" in r121,
        "R121 correction missing",
    )

    r125 = read("results/R125-ADJACENT-FILTER-PRIME-PACKET-BRIDGE-GATE.md")
    require("two adjacent filters on collapsed tail               RANK ONE" in r125, "tail rank drift")
    require(
        "C_(P-1)-C_P=P^(-1/2)tau_(-log P)" in r125,
        "unnormalized adjacent identity drift",
    )
    require(
        "Delta_P=P(C_(P-1)-C_P)" in r125
        and "=P^(1/2)tau_(-log P)" in r125,
        "reciprocal-normalized adjacent identity drift",
    )
    require(
        "raw excess amplitude contributed by a zero" in r125
        and "X^(beta-1/2)P^(1-beta)" in r125
        and "P^(1-beta)/P^(1/2)" in r125,
        "raw versus critical-relative adjacent multiplier drift",
    )

    r128 = read("results/R128-ALL-ARITY-PROPER-CONDUCTOR-GATE.md")
    require("O_full=E_R71" in r128, "complete equality drift")
    require("C=mu*Lambda=-mu log,          C*1=Lambda" in r128, "C*1 identity drift")

    r124 = read("results/R124-ACTUAL-QH-PRIMITIVE-MELLIN-SIGN-GATE.md")
    require("D-rated numerical diagnostic" in r124, "R124 numerical trust label missing")
    r120_flat = " ".join(read(
        "results/R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md"
    ).split())
    require(
        "not a certified negative spectral witness" in r120_flat,
        "R120 inherited an uncertified sign theorem",
    )

    # Exact exponent arithmetic, rather than marker-string checking alone.
    for k in range(1, 65):
        a_k = Fraction(1, 2 * (k + 1))
        threshold = 2 * a_k
        require(threshold == Fraction(1, k + 1), f"threshold algebra failed at k={k}")
        for numerator in range(0, 2 * (k + 1) + 1):
            kappa = Fraction(numerator, 2 * (k + 1))
            sharp_eta = (kappa / 2 - a_k) / (1 - a_k)
            require((sharp_eta > 0) == (kappa > threshold), f"sharp sign map failed at k={k}")

    lower = " ".join(report.lower().split())
    for phrase in (
        "three tested faithfulness dispositions",
        "not an exhaustion theorem",
        "fail admission / tautological",
        "exact scale replication",
        "no uniform zero-free strip",
        "no proof of rh",
    ):
        require(phrase in lower, f"report guardrail missing: {phrase}")

    print("PASS: correction closure and tested-route disposition invariants")
    print("NOTE: no fixed-power estimate, zero-free strip, or RH is proved")


if __name__ == "__main__":
    main()
