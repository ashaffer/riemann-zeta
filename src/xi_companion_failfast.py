#!/usr/bin/env python3
"""Certified low-dimensional fail-fast tests for the xi companion.

For

    M(h) = xi(1/2 + h) / xi(1/2) = sum_(n >= 0) a_n h^(2n),

the ``N``-dimensional leading section of the weighted companion in
``results/TRACE-CLASS-XI-COMPANION-GATE.md`` has

    det(I + w K_N) = p_N(w) = sum_(n=0)^N a_n w^n.

This script uses rigorous FLINT/Arb balls to certify:

* the dimension-two section has a nonreal conjugate eigenvalue pair;
* the degree-six Taylor section fails the third Hurwitz determinant.

These finite-section failures do not refute the infinite determinant identity
or RH.  They rule out the proposed leading-section positivity mechanism.
"""

from __future__ import annotations

from flint import acb, acb_series, arb, arb_mat, ctx


def centered_xi_coefficients(maximum_index: int, bits: int) -> list[arb]:
    """Return certified ``a_0, ..., a_maximum_index`` as Arb balls."""

    ctx.threads = 1
    ctx.prec = bits
    ctx.cap = 2 * maximum_index + 2

    h = acb_series([0, 1])
    s = h + acb(arb(1) / 2)
    pi = acb.pi()
    xi = (
        s
        * (s - 1)
        / 2
        * (-s * pi.log() / 2).exp()
        * (s / 2).gamma()
        * s.zeta()
    )
    centered = xi / xi[0]
    return [centered[2 * index].real for index in range(maximum_index + 1)]


def hurwitz_determinants(coefficients: list[arb]) -> list[arb]:
    """Return the leading Hurwitz determinants for ascending coefficients."""

    degree = len(coefficients) - 1
    rows = [
        [
            coefficients[degree - 1 + row - 2 * column]
            if 0 <= degree - 1 + row - 2 * column <= degree
            else arb(0)
            for column in range(degree)
        ]
        for row in range(degree)
    ]
    return [
        arb_mat([row[:size] for row in rows[:size]]).det()
        for size in range(1, degree + 1)
    ]


def main() -> None:
    coefficients = centered_xi_coefficients(maximum_index=6, bits=768)
    a0, a1, a2, a3, a4, a5, a6 = coefficients

    quadratic_discriminant = a1**2 - 4 * a0 * a2
    raw_hankel_minor = a0 * a2 - a1**2
    hurwitz_delta_3 = (
        a3 * a4 * a5
        - a2 * a5**2
        - a3**2 * a6
        + a1 * a5 * a6
    )

    assert quadratic_discriminant < 0
    assert raw_hankel_minor < 0
    assert hurwitz_delta_3 < 0

    hurwitz = hurwitz_determinants(coefficients)
    assert hurwitz[0] > 0
    assert hurwitz[1] > 0
    assert all(determinant < 0 for determinant in hurwitz[2:])

    print(f"a1 = {a1.str(70)}")
    print(f"a2 = {a2.str(70)}")
    print(f"a1^2 - 4*a0*a2 = {quadratic_discriminant.str(70)}")
    print(f"a0*a2 - a1^2 = {raw_hankel_minor.str(70)}")
    print(f"Hurwitz Delta_3(p_6) = {hurwitz_delta_3.str(70)}")
    for index, determinant in enumerate(hurwitz, start=1):
        print(f"Hurwitz Delta_{index}(p_6) = {determinant.str(30)}")


if __name__ == "__main__":
    main()
