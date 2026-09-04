#!/usr/bin/env python3
"""Exact exponent audit for the prime-Voronoi rational-alias gate."""

from fractions import Fraction


def main() -> None:
    aperture = Fraction(50, 33)
    gap_square_exponent = Fraction(123, 100)
    denominator_exponent = Fraction(1, 10)
    conservative_c = Fraction(19, 1000)
    delta_star = Fraction(180303234, 10_000_000_000)

    # sqrt(R)*sqrt(sum g^2)/Y with R=(t/Y)Q^2.
    boundary_base = Fraction(3, 2) - gap_square_exponent / 2
    assert boundary_base == Fraction(177, 200)

    length_saving = 1 - aperture / 2 - denominator_exponent
    boundary_saving = boundary_base - aperture / 2 - denominator_exponent
    alias_base = boundary_base - aperture / 2
    maximal_r_at_delta_star = alias_base - delta_star

    assert length_saving == Fraction(47, 330)
    assert alias_base == Fraction(841, 6600)
    assert boundary_saving == Fraction(181, 6600)
    assert boundary_saving > conservative_c > delta_star

    print(f"aperture A                 = {aperture} = {float(aperture):.12f}")
    print(
        "mean-square gap exponent  = "
        f"{gap_square_exponent} = {float(gap_square_exponent):.12f}"
    )
    print(
        "denominator exponent r    = "
        f"{denominator_exponent} = {float(denominator_exponent):.12f}"
    )
    print(
        "geometric-length saving   = "
        f"{length_saving} = {float(length_saving):.12f}"
    )
    print(
        "boundary-gap saving       = "
        f"{boundary_saving} = {float(boundary_saving):.12f}"
    )
    print(
        "room over c=.019          = "
        f"{float(boundary_saving - conservative_c):.12f}"
    )
    print(
        "room over delta_*         = "
        f"{float(boundary_saving - delta_star):.12f}"
    )
    print(
        "largest r at delta_*      = "
        f"{maximal_r_at_delta_star} = {float(maximal_r_at_delta_star):.12f}"
    )
    print("PASS: q <= Y^(1/10) rational aliases are below the target scale")


if __name__ == "__main__":
    main()
