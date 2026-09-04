#!/usr/bin/env python3
"""Standalone verifier for the OD2 tensor-trace/low-slope theorem card."""

from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from od2_tensor_trace_gate import (  # noqa: E402
    EDGE_EXPONENT,
    H_MAX,
    H_MIN,
    SELECTOR_BETA,
    SELECTOR_CAP,
    TRUNCATED_CUBE_SAVING,
    audit,
    low_slope_exponent,
    selector_wedge,
)


def main() -> None:
    data = audit()
    jordan = data["paired_jordan"]
    assert jordan["state"] == (1, 19, 19, 361)
    assert jordan["nilpotent_square_nonzero"]
    assert jordan["nilpotent_cube_zero"]
    assert data["affine_difference"] == (0.0, 0.0)
    assert data["monomial"]["aggregate_with_Y"] == "Y*G"

    wedge = selector_wedge()
    eta_min = low_slope_exponent(H_MIN)
    eta_max = low_slope_exponent(H_MAX)
    h_cap = (
        4 * SELECTOR_CAP
        - 3 * EDGE_EXPONENT
        + TRUNCATED_CUBE_SAVING
    )
    assert eta_min == Fraction(150703, 858000)
    assert eta_max == Fraction(135181, 520000)
    assert eta_min > SELECTOR_BETA
    assert h_cap == Fraction(460197, 864500)
    assert H_MIN < h_cap < H_MAX
    assert wedge["wedge_reaches_h_max"] is False

    print("OD2 tensor-trace finite algebra: PASS")
    print(f"low-slope exponent at h_min={eta_min} ({float(eta_min):.12f})")
    print(f"largest h with capped selector wedge={h_cap} ({float(h_cap):.12f})")
    print("rational residual-slope replacement: REJECTED (net H loss)")
    print("actual SPF OD2 outside the low-integer-slope sector: OPEN")


if __name__ == "__main__":
    main()
