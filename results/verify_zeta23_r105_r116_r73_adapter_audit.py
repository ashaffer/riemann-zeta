#!/usr/bin/env python3
"""Replay structural invariants for the R105--R116--R73 adapter audit.

This checks claim state, exact routing metadata, and that the cited local
reports still contain the scope statements on which the audit relies.  It
does not prove the analytic inputs, a zero-free strip, or RH.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "results/ZETA23-R105-R116-R73-ADAPTER-INTEGRITY-AUDIT-2026-09-02.md"
CACHE = ROOT / "results/context/zeta23_r105_r116_r73_adapter_audit_v1.json"
sys.path.insert(0, str(ROOT / "src"))
from zeta23_proof_tree import load_current_authority_bundle


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> None:
    load_current_authority_bundle()
    data = json.loads(CACHE.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    require(data["schema"] == "zeta23_r105_r116_r73_adapter_audit_v1", "schema drift")
    require(data["global_status"]["riemann_hypothesis"] == "OPEN", "RH claim drift")
    require(data["global_status"]["uniform_zero_free_strip"] == "OPEN", "strip claim drift")

    verdict = data["s0_verdict"]
    require(verdict["primitive_only_go_condition"] == "FAIL", "S0 verdict drift")
    require(verdict["r116_balanced_semiprime_theorem"] == "VALID_IN_SCOPE", "R116 scope drift")
    require(verdict["r128_all_class_adapter"] == "EXACT_EQUALS_ORIGINAL_ENDPOINT", "R128 drift")
    require(verdict["branch_switch"] == "FIRED", "branch switch not recorded")

    chain = {item["source"]: item["status"] for item in data["dependency_chain"]}
    require(chain["R116"] == "LOCAL_RESTRICTION_NOT_GLOBAL_EQUIVALENCE", "R116 promoted globally")
    require(
        chain["R120_R124"]
        == "NO_PROVED_ORDER_REFLECTING_MAP_ACTUAL_INDEFINITENESS_UNCERTIFIED",
        "primitive trust/order-reflection drift",
    )
    require(chain["R128"] == "EXACT_AND_EQUAL_TO_ORIGINAL_QH_ENERGY", "complete dual drift")
    require(
        chain["R125"] == "RANK_ONE_ON_TAIL_FAITHFUL_DIRECTION_IS_RESCALED_COMPLETE_FIELD",
        "R125 scale-replication correction drift",
    )
    require(chain["R180"] == "EXPONENT_EQUIVALENCE", "fixed-window calibration drift")

    maps = data["exponent_maps"]
    require(
        maps["complete_energy"]["conclusion"] == "eta=kappa/2 for 0<kappa<=1",
        "complete exponent map/domain drift",
    )
    filtered = maps["r123_fixed_window_collapsed"]
    require(filtered["cofactor_exponent_a_k"] == "1/(2*(k+1))", "fixed-k cofactor drift")
    require(filtered["positive_strip_condition"] == "kappa>1/(k+1)", "filtered reserve drift")
    require(
        filtered["research_status_after_r125"] == "EXACT_SCALE_REPLICATION_NOT_A_REDUCTION",
        "R123/R125 fork incorrectly promoted",
    )

    for source in data["sources"]:
        require((ROOT / source).exists(), f"missing source: {source}")

    r116 = read("results/R116-SIGNED-JOINT-TYPEII-ATTACK.md")
    require("c=p r" in r116 and "p,r asymp sqrt(c)" in r116, "R116 semiprime scope vanished")
    require("permission to delete the nonsquarefree tail" in r116, "R116 nonsquarefree warning vanished")
    require("h(c)c^(1-it)" in r116, "R116 outer Mellin phase correction vanished")

    r120 = read("results/R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md")
    require(
        "primitive quadratic form" in r120
        and "HERMITIAN / POSITIVITY UNPROVED" in r120,
        "R120 sign-trust warning vanished",
    )
    require("must not be extended to every many-prime modulus" in r120, "R120 global-scope warning vanished")

    r128 = read("results/R128-ALL-ARITY-PROPER-CONDUCTOR-GATE.md")
    require("O_full=E_R71" in r128, "R128 endpoint identity vanished")
    require("complete all-class remainder               ZERO" in r128, "R128 conductor cancellation vanished")

    r125 = read("results/R125-ADJACENT-FILTER-PRIME-PACKET-BRIDGE-GATE.md")
    require("two adjacent filters on collapsed tail               RANK ONE" in r125, "R125 tail rank drift")
    require("original canonical cofactor sequence at the smaller scale" in r125, "R125 rescaling drift")

    fixed = read("results/FIXED-WINDOW-REDUCTION-INDEPENDENT-AUDIT-2026-08-30.md")
    require("theta_k=1/2-1/[4(k+1)]" in fixed, "fixed-window cutoff drift")

    lower = " ".join(report.lower().split())
    for phrase in (
        "primitive-only go condition failed",
        "exact, but equals endpoint",
        "before cauchy--schwarz or absolute values",
        "no uniform zero-free strip",
        "no proof of rh",
    ):
        require(phrase in lower, f"audit lost guardrail: {phrase}")

    print("PASS: R105--R116--R73 adapter audit invariants")
    print("NOTE: S0 fails only for the primitive-only adapter; this checker proves no strip or RH")


if __name__ == "__main__":
    main()
