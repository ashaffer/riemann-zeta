#!/usr/bin/env python3
"""Standalone exact replay of the rough-gap lower-sieve exponent ledger."""

from fractions import Fraction
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from rough_gap_lower_sieve_frontier import (  # noqa: E402
    LowerSieveParameters,
    required_excess,
    rough_gap_moment_certificate,
)


def main() -> None:
    p = LowerSieveParameters()
    c = rough_gap_moment_certificate(p)
    assert p.main_term_power_margin == Fraction(103, 7500)
    assert p.linear_sieve_ratio == Fraction(5000, 2397) > 2
    assert p.jacobsthal_gap_cutoff == Fraction(799, 2500)
    assert p.type_ii_poisson_range == Fraction(797, 1800)
    assert c.type_ii.shifted_product == Fraction(-22, 1875)
    assert c.type_ii.inner_first == Fraction(1003, 1000)
    assert c.type_ii.inner_second == Fraction(4927, 7500)
    assert c.type_ii.convolution == Fraction(84457, 90000)
    assert c.final_gap_square == 1
    assert c.excess == 0

    hostile_kappa = Fraction(19740482582942, 10**15)
    needed = required_excess(Fraction(799, 5000), hostile_kappa)
    assert c.excess < needed

    print("rough-gap lower-sieve exact exponent ledger: PASS")
    print(f"linear_sieve_ratio={p.linear_sieve_ratio} ({float(p.linear_sieve_ratio):.12f})")
    print(f"main_term_power_margin={p.main_term_power_margin} ({float(p.main_term_power_margin):.12f})")
    print(f"G2_exponent={c.final_gap_square} ({float(c.final_gap_square):.12f})")
    print(f"rho={c.excess} ({float(c.excess):.12f})")
    print(f"required_rho<{float(needed):.12f}")
    print(f"margin={float(needed-c.excess):.12f}")


if __name__ == "__main__":
    main()
