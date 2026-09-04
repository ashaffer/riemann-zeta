#!/usr/bin/env python3
"""Independent compact verifier for the common-height OD2 gate report."""

from fractions import Fraction
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from common_height_od2_gate import (  # noqa: E402
    EDGE_EXPONENT,
    H_MIN,
    KAPPA,
    audit,
)


def main() -> None:
    data = audit()
    assert data["deletion_telescope_exact"]
    assert data["affine_moments"] == ("0", "0")
    assert data["first_return_left"] == 3
    assert data["first_return_right"] == 2
    assert data["tensor_product"] == 6

    periodic = data["periodic"]
    length = periodic["length"]
    assert abs(periodic["fourier_abs"] - length) < 1e-8
    assert abs(periodic["square"] - length**2) < 1e-7
    assert periodic["mass"] == 0 and periodic["first_moment"] == 0
    assert periodic["off_diagonal"] > 0
    assert periodic["shift_discrepancy"] < 1e-6

    miss = H_MIN - EDGE_EXPONENT
    margin = H_MIN - 4 * KAPPA - EDGE_EXPONENT
    assert miss == Fraction(13699, 165000)
    assert miss > 0
    assert margin > 0

    print("common-height OD2 finite identities: PASS")
    print(f"nested-node structural miss={miss} ({float(miss):.12f})")
    print(f"diagonal-to-bridge margin={margin} ({float(margin):.12f})")
    print("actual SPF/common-height OD2 theorem: NOT ASSERTED")


if __name__ == "__main__":
    main()
