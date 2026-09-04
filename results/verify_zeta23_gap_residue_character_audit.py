#!/usr/bin/env python3
"""Arithmetic and finite-model checks for the gap residue/character audit."""

from __future__ import annotations

import cmath
from fractions import Fraction


BETA = Fraction(1537, 10000)
THETA = Fraction(797, 5000)
KAPPA_DECIMAL = Fraction(180303234, 10_000_000_000)


def e_q(x: int, q: int) -> complex:
    return cmath.exp(2j * cmath.pi * x / q)


def check_exponents() -> None:
    rms_saving = BETA - THETA / 2
    bad_count = THETA + 2 * KAPPA_DECIMAL
    b_star = Fraction(2, 15) + Fraction(13, 9) * KAPPA_DECIMAL
    c_beta = Fraction(9, 13) * (BETA - Fraction(2, 15))

    assert rms_saving == Fraction(74, 1000)
    assert c_beta == Fraction(141, 10000)
    assert BETA < b_star < THETA
    assert bad_count > BETA
    assert Fraction(1, 1) + THETA - KAPPA_DECIMAL < Fraction(123, 100)

    print(f"large-sieve RMS saving={float(rms_saving):.12f}")
    print(f"bad-fraction exponent={float(bad_count):.12f}")
    print(f"c(beta)={float(c_beta):.12f}")
    print(f"b_star={float(b_star):.12f}")


def check_finite_countermodel() -> None:
    # A small exact residue-cycle instance.  The asymptotic construction uses
    # d~log Y, q~Y^b, and K~Y^kappa/d; only its algebra is checked here.
    q = 1009
    d = 7
    k_cycles = 11

    residues = [(k * d) % q for k in range(1, q)]
    assert len(set(residues)) == q - 1
    assert 0 not in residues

    counts = {a: 0 for a in range(1, q)}
    for _ in range(k_cycles):
        for a in residues:
            counts[a] += 1
    assert set(counts.values()) == {k_cycles}

    # One base cycle: d-edges except for the final 2d edge skipping zero.
    base = 0j
    for idx, a in enumerate(residues):
        b = residues[(idx + 1) % len(residues)]
        gap = 2 * d if idx == len(residues) - 1 else d
        base += gap * (e_q(a, q) + e_q(b, q)) / 2

    base_formula = -d + d * cmath.cos(2 * cmath.pi * d / q)
    assert abs(base - base_formula) < 1e-9

    # Lengthen d -> 2d by q.  Endpoint residues and all visit counts stay put.
    long_increment = q * (e_q(d, q) + e_q(2 * d, q)) / 2
    super_dft = k_cycles * base + long_increment
    super_mass = k_cycles * q * d + q
    exact_ratio = abs(super_dft) / super_mass
    expected_scale = 1 / (k_cycles * d)

    assert abs(long_increment) > 0.99 * q
    assert exact_ratio > 0.8 * expected_scale
    assert exact_ratio < 1.2 * expected_scale

    # Every nontrivial character on the cyclic unit group sums to zero over a
    # complete residue cycle.  Check this directly using a primitive root.
    primitive_root = 11
    assert len({pow(primitive_root, j, q) for j in range(q - 1)}) == q - 1
    for frequency in (1, 2, 17, 503):
        char_sum = sum(
            cmath.exp(2j * cmath.pi * frequency * j / (q - 1))
            for j in range(q - 1)
        )
        assert abs(char_sum) < 1e-9

    print(f"finite model normalized DFT={exact_ratio:.12f}")
    print(f"finite model predicted scale={expected_scale:.12f}")


def main() -> None:
    check_exponents()
    check_finite_countermodel()
    print("gap residue/character audit: PASS")


if __name__ == "__main__":
    main()
