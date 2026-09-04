#!/usr/bin/env python3
from fractions import Fraction
import sys

sys.path.insert(0, "src")

from common_height_l2_bridge import (
    KAPPA,
    audit,
    block_covariance_identity,
    delta_frontier_from_l2,
    diagonal_l2_exponent,
    maximum_closing_l2_exponent,
)


def main() -> None:
    result = audit()
    assert result["strictly_positive"] is True
    assert delta_frontier_from_l2() == Fraction(2, 33) - Fraction(1_974_048_259, 100_000_000_000)
    assert maximum_closing_l2_exponent() == Fraction(1) + Fraction(8, 33) - 4 * KAPPA
    assert diagonal_l2_exponent() == Fraction(1) + Fraction(797, 5000)
    assert delta_frontier_from_l2(diagonal_l2_exponent()) > Fraction(1, 1000)
    direct, expanded = block_covariance_identity([[1 + 1j, 2 - 3j], [4j, -2]])
    assert abs(direct - expanded) < 1e-12
    print("common-height L2-to-CH4 bridge: PASS")
    print(result)


if __name__ == "__main__":
    main()
