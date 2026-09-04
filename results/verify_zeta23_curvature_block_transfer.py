#!/usr/bin/env python3
"""Exact exponent checks for the curvature-block transfer/no-go report."""

from fractions import Fraction


KAPPA = Fraction(90151617, 5_000_000_000)
BETA = Fraction(1537, 10_000)
THETA = Fraction(797, 5_000)
B = Fraction(39, 250)
A = 1 - B
H = (1 + B) / 2
TRANSITION_H_MAX = Fraction(5797, 10_000)


def main() -> None:
    c_gt = Fraction(9, 13) * (B - Fraction(2, 15))
    vaughan = BETA / 2
    prefix_exp = 1 - vaughan
    type_ii_fiber = TRANSITION_H_MAX - Fraction(1, 2)
    square_exp = 1 + B - KAPPA
    long_count_exp = 1 - B - KAPPA

    assert BETA < B < THETA
    assert A == Fraction(211, 250)
    assert Fraction(4203, 5000) < A < 1
    assert H == Fraction(289, 500)
    assert Fraction(1, 2) <= H <= TRANSITION_H_MAX
    assert B < H

    assert c_gt == Fraction(51, 3250)
    assert c_gt < KAPPA
    assert KAPPA - c_gt > Fraction(2, 1000)

    assert vaughan == Fraction(1537, 20_000)
    assert prefix_exp == Fraction(18463, 20_000)
    assert prefix_exp - TRANSITION_H_MAX == Fraction(6869, 20_000)
    assert type_ii_fiber == Fraction(797, 10_000)
    assert type_ii_fiber < BETA

    assert square_exp < Fraction(123, 100)
    assert 2 * B > KAPPA
    assert long_count_exp > 0

    # N_L*Y^b/Y = Y^-kappa.
    assert long_count_exp + B - 1 == -KAPPA

    print("curvature-block transfer audit: PASS")
    print(f"companion t exponent={float(A):.10f}")
    print(f"block H exponent={float(H):.10f}")
    print(f"one-period gap exponent={float(B):.10f}")
    print(f"GT saving at gap scale={float(c_gt):.10f}")
    print(f"target kappa={float(KAPPA):.10f}")
    print(f"Vaughan global saving={float(vaughan):.10f}")
    print(f"prefix-vs-longest-block loss={float(prefix_exp-TRANSITION_H_MAX):.10f}")
    print(f"balanced Type-II fiber exponent={float(type_ii_fiber):.10f}")
    print(f"countermodel gap-square exponent={float(square_exp):.10f}")


if __name__ == "__main__":
    main()
