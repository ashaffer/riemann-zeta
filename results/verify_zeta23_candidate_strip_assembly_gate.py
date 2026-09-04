#!/usr/bin/env python3
"""Replay the exact constants and polarity of the strip assembly audit."""

from fractions import Fraction
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from candidate_strip_assembly_gate import (  # noqa: E402
    MAX_COUNTERFACTUAL_OD2_X_BILL,
    MAX_COUNTERFACTUAL_OD2_Y_BILL,
    OD2_EPSILON_FRONTIER,
    RESIDUAL_GP_BUDGET_AFTER_COUNTERFACTUAL_OD2,
    ZF_DELTA,
    audit,
    stated_gp_od2_ga2_package_proves_strip,
)


def main() -> None:
    assert ZF_DELTA == Fraction(1, 100)
    assert OD2_EPSILON_FRONTIER == Fraction(
        3_351_407_453, 3_300_000_000_000
    )
    assert MAX_COUNTERFACTUAL_OD2_Y_BILL == Fraction(13_699, 660_000)
    assert MAX_COUNTERFACTUAL_OD2_X_BILL == Fraction(13_699, 1_000_000)
    assert RESIDUAL_GP_BUDGET_AFTER_COUNTERFACTUAL_OD2 == Fraction(
        2_338_451, 200_000_000
    )
    assert RESIDUAL_GP_BUDGET_AFTER_COUNTERFACTUAL_OD2 > 0
    assert not stated_gp_od2_ga2_package_proves_strip()
    print("candidate-centred strip assembly gate: PASS")
    for key, value in audit().items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
