#!/usr/bin/env python3
"""Exact finite checks for the SR2PF proof-or-counterexample audit.

The companion report contains the asymptotic arguments.  This file only
checks algebraic identities, rational exponent arithmetic, and the explicit
prime fixtures used as falsifiers.  It deliberately does not turn numerical
sampling into evidence for an asymptotic theorem.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import isqrt


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def determinant_3(matrix: list[list[int]]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def cayley_hyperdet(values: dict[tuple[int, int, int], int]) -> int:
    """Cayley's 2 by 2 by 2 hyperdeterminant, exactly over Z."""

    a000 = values[(0, 0, 0)]
    a001 = values[(0, 0, 1)]
    a010 = values[(0, 1, 0)]
    a011 = values[(0, 1, 1)]
    a100 = values[(1, 0, 0)]
    a101 = values[(1, 0, 1)]
    a110 = values[(1, 1, 0)]
    a111 = values[(1, 1, 1)]
    return (
        a000**2 * a111**2
        + a001**2 * a110**2
        + a010**2 * a101**2
        + a100**2 * a011**2
        - 2
        * (
            a000 * a001 * a110 * a111
            + a000 * a010 * a101 * a111
            + a000 * a100 * a011 * a111
            + a001 * a010 * a101 * a110
            + a001 * a100 * a011 * a110
            + a010 * a100 * a011 * a101
        )
        + 4
        * (
            a000 * a011 * a101 * a110
            + a001 * a010 * a100 * a111
        )
    )


def certify_exponents() -> dict[str, Fraction]:
    aperture = Fraction(50, 33)
    physical_error = 1 - aperture
    minor_height = 1 + physical_error
    flattening_determinant = 1 + 2 * physical_error
    projective_sieve = minor_height / 4
    tensor_density = Fraction(179, 10_000)
    balanced_target = tensor_density / 2

    assert physical_error == -Fraction(17, 33)
    assert minor_height == Fraction(16, 33)
    assert flattening_determinant == -Fraction(1, 33)
    assert projective_sieve == Fraction(4, 33)
    assert balanced_target == Fraction(179, 20_000)
    assert balanced_target < projective_sieve

    # The denominator obstruction in the constant-shift secant branch.
    assert 2 * (-physical_error) == Fraction(34, 33) > 1
    return {
        "physical_error": physical_error,
        "minor_height": minor_height,
        "flattening_determinant": flattening_determinant,
        "projective_sieve": projective_sieve,
        "balanced_target": balanced_target,
    }


def certify_schur_plucker_fixture() -> dict[str, object]:
    """Check the exact rank-two Schur-minor factorization on primes."""

    entries = [199 + 210 * index for index in range(9)]
    assert all(is_prime(value) for value in entries)
    matrix = [entries[3 * row : 3 * row + 3] for row in range(3)]
    assert determinant_3(matrix) == 0

    pivot = matrix[0][0]
    schur = [
        [pivot * matrix[i][j] - matrix[i][0] * matrix[0][j] for j in (1, 2)]
        for i in (1, 2)
    ]
    assert all(value != 0 for row in schur for value in row)
    assert schur[0][0] * schur[1][1] == schur[0][1] * schur[1][0]
    return {"matrix": matrix, "schur_minors": schur}


def tangent_prime_fixture() -> tuple[
    dict[tuple[int, int, int], int],
    list[tuple[int, int]],
    list[tuple[int, int]],
]:
    # T_s=sum_j b_j(s_j) prod_{h!=j} a_h(s_h).
    avec = [(1, 1), (4, 4), (1, 3)]
    bvec = [(15, 45), (15, 41), (-16, -19)]
    values: dict[tuple[int, int, int], int] = {}
    for state in product((0, 1), repeat=3):
        total = 0
        for j in range(3):
            term = bvec[j][state[j]]
            for h in range(3):
                if h != j:
                    term *= avec[h][state[h]]
            total += term
        values[state] = total
    return values, avec, bvec


def certify_scaled_tangent_fixture() -> dict[str, object]:
    """Primality does not by itself remove tangent diagonal scalings."""

    values, avec, bvec = tangent_prime_fixture()
    expected = [11, 149, 37, 227, 131, 509, 157, 587]
    assert list(values.values()) == expected
    assert len(set(expected)) == 8
    assert all(is_prime(value) for value in expected)
    assert cayley_hyperdet(values) == 0

    # It is not an unscaled additive cube.
    mixed_additive_difference = (
        values[(0, 0, 0)]
        + values[(1, 0, 1)]
        - values[(0, 0, 1)]
        - values[(1, 0, 0)]
    )
    assert mixed_additive_difference == 240

    # Normalize it as p_S=p_0 x_S (1+sum_{j in S} g_j).
    p0 = values[(0, 0, 0)]
    base_additive = sum(
        Fraction(bvec[j][0], avec[j][0]) for j in range(3)
    )
    x = [Fraction(avec[j][1], avec[j][0]) for j in range(3)]
    g = []
    for j in range(3):
        increment = (
            Fraction(bvec[j][1], avec[j][1])
            - Fraction(bvec[j][0], avec[j][0])
        )
        g.append(increment / base_additive)
    assert len(set(g)) == 3 and all(value != 0 for value in g)

    for state, prime in values.items():
        scale = Fraction(1)
        additive = Fraction(1)
        for j, bit in enumerate(state):
            if bit:
                scale *= x[j]
                additive += g[j]
        assert p0 * scale * additive == prime

    # Check -Delta_ij/(p_i p_j)=a_i a_j, the height-recovery identity.
    for i in range(3):
        for j in range(i + 1, 3):
            state_i = tuple(1 if k == i else 0 for k in range(3))
            state_j = tuple(1 if k == j else 0 for k in range(3))
            state_ij = tuple(1 if k in (i, j) else 0 for k in range(3))
            delta = p0 * values[state_ij] - values[state_i] * values[state_j]
            ai = g[i] / (1 + g[i])
            aj = g[j] / (1 + g[j])
            assert -Fraction(delta, values[state_i] * values[state_j]) == ai * aj

    return {
        "values": expected,
        "mixed_additive_difference": mixed_additive_difference,
        "x": x,
        "g": g,
    }


def honest_secant_values(
    avec: list[tuple[int, int]], bvec: list[tuple[int, int]]
) -> dict[tuple[int, ...], int]:
    values: dict[tuple[int, ...], int] = {}
    for state in product((0, 1), repeat=len(avec)):
        first = 1
        second = 1
        for j, bit in enumerate(state):
            first *= avec[j][bit]
            second *= bvec[j][bit]
        values[state] = first + second
    return values


def certify_honest_secant_norm_orbit() -> dict[str, object]:
    """Check the fixed-norm identity and determinant cocycle used in Section 7."""

    # A genuinely two-sided 2 x 2 x 2 tensor of eight distinct primes.
    prime_a = [(16, 2), (11, 19), (13, 19)]
    prime_b = [(21, 17), (15, 23), (15, 5)]
    prime_values = honest_secant_values(prime_a, prime_b)
    expected = [7013, 4919, 11197, 8191, 4111, 1693, 6359, 2677]
    assert list(prime_values.values()) == expected
    assert len(set(expected)) == 8
    assert all(is_prime(value) for value in expected)
    hyperdet = cayley_hyperdet(prime_values)  # type: ignore[arg-type]
    assert hyperdet != 0

    def face_minor(i: int, j: int) -> int:
        states: dict[tuple[int, int], tuple[int, int, int]] = {}
        for x, y in product((0, 1), repeat=2):
            state = [0, 0, 0]
            state[i] = x
            state[j] = y
            states[(x, y)] = tuple(state)
        return (
            prime_values[states[(0, 0)]] * prime_values[states[(1, 1)]]
            - prime_values[states[(0, 1)]] * prime_values[states[(1, 0)]]
        )

    d12 = face_minor(0, 1)
    d13 = face_minor(0, 2)
    d23 = face_minor(1, 2)
    base_norm = 1
    for j in range(3):
        base_norm *= prime_a[j][0] * prime_b[j][0]
    assert Fraction(d12 * d13 * d23, hyperdet) == base_norm

    # A fourth mode checks D_S/D_empty=N_S/N_empty exactly.
    avec = prime_a + [(17, 19)]
    bvec = prime_b + [(47, 53)]
    values = honest_secant_values(avec, bvec)

    def background_minor(bit: int) -> int:
        def value(x: int, y: int) -> int:
            return values[(x, y, 0, bit)]

        return value(0, 0) * value(1, 1) - value(0, 1) * value(1, 0)

    delta0 = background_minor(0)
    delta1 = background_minor(1)
    q = Fraction(avec[3][1] * bvec[3][1], avec[3][0] * bvec[3][0])
    assert Fraction(delta1, delta0) == q

    norm0 = base_norm * avec[3][0] * bvec[3][0]
    norm1 = base_norm * avec[3][1] * bvec[3][1]
    assert Fraction(norm1, norm0) == Fraction(delta1, delta0)

    return {
        "values": expected,
        "hyperdeterminant": hyperdet,
        "base_norm": base_norm,
        "cocycle": q,
    }


def certify_all() -> None:
    exponents = certify_exponents()
    schur = certify_schur_plucker_fixture()
    tangent = certify_scaled_tangent_fixture()
    secant = certify_honest_secant_norm_orbit()
    print("minor-height exponent:", exponents["minor_height"])
    print("projective-sieve exponent:", exponents["projective_sieve"])
    print("clean balanced target exponent:", exponents["balanced_target"])
    print("Schur-minor fixture:", schur["schur_minors"])
    print("scaled tangent prime fixture:", tangent["values"])
    print("honest secant prime fixture:", secant["values"])
    print("honest secant norm cocycle:", secant["cocycle"])
    print("all SR2PF finite certificates passed")


if __name__ == "__main__":
    certify_all()
