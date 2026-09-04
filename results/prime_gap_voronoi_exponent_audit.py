#!/usr/bin/env python3
"""Replay the rational exponent ledger in the Voronoi prime-gap report."""

from decimal import Decimal, getcontext
from fractions import Fraction


def main() -> None:
    gap_transport = Fraction(77, 100)
    max_gap = Fraction(19, 40)
    tau = Fraction(1, 100)
    sigma = Fraction(751, 1000)
    required = Decimal("0.0180303234")

    terms = (
        gap_transport - tau,
        2 * tau,
        gap_transport - sigma,
    )
    proved = min(terms)
    assert proved == Fraction(19, 1000)
    assert Decimal(proved.numerator) / Decimal(proved.denominator) > required

    print("hybrid terms:", *(str(x) for x in terms))
    print("proved exponent:", proved, "=", float(proved))
    print("required exponent:", required)
    print("margin:", Decimal(proved.numerator) / Decimal(proved.denominator) - required)

    thresholds = []
    for degree in range(6):
        beta = (gap_transport + degree * max_gap) / (degree + 1)
        thresholds.append(beta)
        print(f"degree {degree} Peano threshold: {beta} = {float(beta):.12f}")
    assert all(thresholds[j + 1] < thresholds[j] for j in range(len(thresholds) - 1))
    assert thresholds[0] == gap_transport

    full_aperture = Fraction(50, 33)
    integer_saving = min(sigma / 2, 1 - full_aperture / 2)
    assert integer_saving == Fraction(8, 33)
    print("all-integer worst saving:", integer_saving, "=", float(integer_saving))

    getcontext().prec = 40
    eta = Decimal("0.0180303234")
    beta = Decimal("0.009")
    turan_rhs = eta * (Decimal(1) - beta ** (Decimal(1) / Decimal(6)))
    assert turan_rhs > beta
    print("Turan beta^(1/6):", beta ** (Decimal(1) / Decimal(6)))
    print("Turan eta*(1-beta^(1/6)):", turan_rhs)
    print("Turan strict margin:", turan_rhs - beta)
    print("implied strip delta beta^2:", beta * beta)


if __name__ == "__main__":
    main()
