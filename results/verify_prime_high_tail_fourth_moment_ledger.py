#!/usr/bin/env python3
"""Replay the exact exponent and prime-product energy ledger.

This is deliberately dependency-free.  It verifies the rational inequalities
used in the accompanying theorem card and checks the ordered prime-product
convolution identity with exact Fractions.
"""

from fractions import Fraction


def product_energy(weights: dict[int, Fraction]) -> Fraction:
    conv: dict[int, Fraction] = {}
    for p, a in weights.items():
        for q, b in weights.items():
            conv[p * q] = conv.get(p * q, Fraction(0)) + a * b
    return sum((value * value for value in conv.values()), Fraction(0))


def main() -> None:
    delta_star = Fraction(119000134, 6_600_000_000)  # 0.018030323333...
    c = Fraction(19, 1000)
    tau = Fraction(1, 100)
    cell_exponent = Fraction(3, 100)
    aperture = Fraction(50, 33)

    assert c > delta_star
    assert 2 * tau > c
    assert cell_exponent - tau > c
    assert aperture < 2

    bad_length = 4 * c
    derivative_cover = 5 * c
    peak_components = Fraction(9, 2) * c
    second_moment_loss = aperture - 1
    fourth_conductor_loss = 2 - aperture

    assert bad_length == Fraction(19, 250)  # .076
    assert peak_components == Fraction(171, 2000)  # .0855
    assert derivative_cover == Fraction(19, 200)  # .095
    assert second_moment_loss == Fraction(17, 33)
    assert fourth_conductor_loss == Fraction(16, 33)

    weights = {
        2: Fraction(1, 7),
        3: Fraction(2, 7),
        5: Fraction(-1, 7),
        7: Fraction(5, 7),
    }
    s2 = sum((a * a for a in weights.values()), Fraction(0))
    s4 = sum((a**4 for a in weights.values()), Fraction(0))
    energy = product_energy(weights)
    expected = 2 * s2 * s2 - s4
    assert energy == expected
    assert energy <= 2 * s2 * s2

    print(f"delta_star_proxy={float(delta_star):.12f}")
    print(f"test_exponent={float(c):.12f}")
    print(f"low_error_exponent={float(cell_exponent - tau):.12f}")
    print(f"target_tail_exponent={float(2 * tau):.12f}")
    print(f"bad_set_length_exponent={float(bad_length):.12f}")
    print(f"large_peak_component_exponent={float(peak_components):.12f}")
    print(f"derivative_grid_exponent={float(derivative_cover):.12f}")
    print(f"aperture={float(aperture):.12f}")
    print(f"second_moment_length_loss={float(second_moment_loss):.12f}")
    print(f"fourth_moment_conductor_gap={float(fourth_conductor_loss):.12f}")
    print(f"product_energy={energy} identity_rhs={expected}")
    print("status=PASS")


if __name__ == "__main__":
    main()
