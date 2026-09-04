#!/usr/bin/env python3
"""Finite identities and exponent ledger for the common-height OD2 gate.

The asymptotic theorem left by the analytic argument is *not* proved here.
This module certifies the exact finite algebra used in the accompanying
report:

* endpoint-trapezoid measures on nested node sets;
* the three-atom update produced by deleting one node;
* telescoping over an arbitrary deletion order;
* diagonal plus signed-shift decomposition of a Fourier square;
* the dimension-two first-return automaton and its dimension-four tensor
  square;
* a periodic nested-refinement countermodel for coefficient-blind OD2.

The countermodel is deliberately not an SPF-rough set or the primes.  It
only identifies which structural facts cannot by themselves prove OD2.
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Iterable


H_MIN = Fraction(8, 33)
EDGE_EXPONENT = Fraction(797, 5000)
KAPPA = Fraction(1_974_048_259, 100_000_000_000)


def trapezoid_measure(points: Iterable[int]) -> dict[int, Fraction]:
    """Endpoint-trapezoid measure on a finite, strictly increasing set."""

    nodes = list(points)
    if len(nodes) < 2 or nodes != sorted(set(nodes)):
        raise ValueError("points must be a strictly increasing finite set")
    mass = {node: Fraction(0) for node in nodes}
    for left, right in zip(nodes, nodes[1:]):
        half = Fraction(right - left, 2)
        mass[left] += half
        mass[right] += half
    return mass


def signed_difference(
    coarse_points: Iterable[int], fine_points: Iterable[int]
) -> dict[int, Fraction]:
    """Return ``nu_coarse - nu_fine`` for nested sets with common ends."""

    coarse = list(coarse_points)
    fine = list(fine_points)
    if not set(coarse).issubset(fine):
        raise ValueError("coarse points must be a subset of fine points")
    if coarse[0] != fine[0] or coarse[-1] != fine[-1]:
        raise ValueError("nested sets must have common endpoints")
    coarse_mass = trapezoid_measure(coarse)
    fine_mass = trapezoid_measure(fine)
    keys = coarse_mass.keys() | fine_mass.keys()
    return {
        node: coarse_mass.get(node, 0) - fine_mass.get(node, 0)
        for node in keys
        if coarse_mass.get(node, 0) != fine_mass.get(node, 0)
    }


def deletion_atom(active_points: Iterable[int], deleted: int) -> dict[int, Fraction]:
    """Exact change ``nu_after - nu_before`` when one interior node is removed.

    If the neighboring distances are ``ell`` and ``r``, the atom is

        (r/2) delta_(x-ell) - ((ell+r)/2) delta_x
            + (ell/2) delta_(x+r).
    """

    active = list(active_points)
    if active != sorted(set(active)) or deleted not in active:
        raise ValueError("deleted must belong to a strictly increasing set")
    index = active.index(deleted)
    if index == 0 or index == len(active) - 1:
        raise ValueError("cannot delete a barrier endpoint")
    left, right = active[index - 1], active[index + 1]
    ell, rdist = deleted - left, right - deleted
    return {
        left: Fraction(rdist, 2),
        deleted: -Fraction(ell + rdist, 2),
        right: Fraction(ell, 2),
    }


def telescope_deletions(
    fine_points: Iterable[int], deletion_order: Iterable[int]
) -> tuple[dict[int, Fraction], list[int]]:
    """Sum deletion atoms and return the resulting coarse set."""

    active = list(fine_points)
    if active != sorted(set(active)):
        raise ValueError("fine points must be strictly increasing")
    total: dict[int, Fraction] = {}
    for deleted in deletion_order:
        atom = deletion_atom(active, deleted)
        for node, value in atom.items():
            total[node] = total.get(node, Fraction(0)) + value
        active.remove(deleted)
    total = {node: value for node, value in total.items() if value}
    return total, active


def affine_moments(coefficients: dict[int, Fraction]) -> tuple[Fraction, Fraction]:
    """Return total mass and first physical moment."""

    return (
        sum(coefficients.values(), Fraction(0)),
        sum((node * value for node, value in coefficients.items()), Fraction(0)),
    )


def fourier_value(
    coefficients: dict[int, Fraction | float | complex], phases: dict[int, complex]
) -> complex:
    """Evaluate a finitely supported coefficient sequence at supplied phases."""

    return sum(complex(value) * phases[node] for node, value in coefficients.items())


def covariance_ledger(
    coefficients: dict[int, Fraction | float | complex], phases: dict[int, complex]
) -> dict[str, complex | float]:
    """Return square, diagonal, off-diagonal, and positive-shift expansion.

    The phases need not form an additive character; this therefore also
    checks the exact logarithmic phase ``exp(i*t*log(n))``.
    """

    nodes = sorted(coefficients)
    value = fourier_value(coefficients, phases)
    diagonal = sum(abs(complex(coefficients[node])) ** 2 for node in nodes)
    off_diagonal = 0j
    positive_shift = 0j
    for left in nodes:
        for right in nodes:
            if left == right:
                continue
            term = (
                complex(coefficients[left])
                * complex(coefficients[right]).conjugate()
                * phases[left]
                * phases[right].conjugate()
            )
            off_diagonal += term
            if right > left:
                positive_shift += term
    return {
        "square": abs(value) ** 2,
        "diagonal": diagonal,
        "off_diagonal": off_diagonal,
        "twice_real_positive_shift": 2.0 * positive_shift.real,
    }


def _mat_vec(matrix: tuple[tuple[int, ...], ...], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def first_return_matrix(bit: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Two-state update for a survivor bit."""

    if bit not in (0, 1):
        raise ValueError("a survivor bit must be zero or one")
    return ((1 - bit, 0), (1, 1))


def first_return_distance(word: Iterable[int]) -> int:
    """Return the first survivor position, using the exact matrix automaton.

    ``word`` must contain a 1.  Positions start at one.  Further symbols
    after the first 1 leave the accumulated distance unchanged.
    """

    bits = list(word)
    if 1 not in bits:
        raise ValueError("the truncated word must contain a survivor")
    state = (1, 0)  # live prefix product, accumulated empty-prefix count
    for bit in bits:
        state = _mat_vec(first_return_matrix(bit), state)
    return state[1]


def kronecker(
    left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    """Kronecker product of two small integer matrices."""

    return tuple(
        tuple(left[i][j] * right[k][ell] for j in range(len(left[0])) for ell in range(len(right[0])))
        for i in range(len(left))
        for k in range(len(right))
    )


def paired_first_return_product(word_left: Iterable[int], word_right: Iterable[int]) -> int:
    """Compute a product of two first-return distances with bond dimension 4."""

    left_bits, right_bits = list(word_left), list(word_right)
    if len(left_bits) != len(right_bits) or 1 not in left_bits or 1 not in right_bits:
        raise ValueError("paired words need equal length and a survivor in each")
    # Tensor state ordering: P*P, P*S, S*P, S*S.
    state = (1, 0, 0, 0)
    for left_bit, right_bit in zip(left_bits, right_bits):
        state = _mat_vec(
            kronecker(first_return_matrix(left_bit), first_return_matrix(right_bit)),
            state,
        )
    return state[3]


def periodic_refinement(period: int, periods: int, numerator: int = 1) -> dict[str, float | int]:
    """Exact finite nested-node obstruction at an additive carrier.

    Fine nodes are all integers in ``[0, period*periods]`` and coarse nodes
    are the multiples of ``period``.  For a primitive numerator the Fourier
    coefficient of ``nu_coarse-nu_fine`` is exactly the physical length.
    """

    if period < 2 or periods < 1 or math.gcd(numerator, period) != 1:
        raise ValueError("need period >=2, periods >=1, and a primitive numerator")
    length = period * periods
    fine = list(range(length + 1))
    coarse = list(range(0, length + 1, period))
    coefficients = signed_difference(coarse, fine)
    phases = {
        node: cmath.exp(2j * math.pi * numerator * node / period)
        for node in coefficients
    }
    ledger = covariance_ledger(coefficients, phases)
    mass, first_moment = affine_moments(coefficients)
    return {
        "period": period,
        "periods": periods,
        "length": length,
        "mass": int(mass),
        "first_moment": int(first_moment),
        "fourier_abs": abs(fourier_value(coefficients, phases)),
        "square": float(ledger["square"]),
        "diagonal": float(ledger["diagonal"]),
        "off_diagonal": float(complex(ledger["off_diagonal"]).real),
        "shift_discrepancy": abs(
            float(complex(ledger["off_diagonal"]).real)
            - float(ledger["twice_real_positive_shift"])
        ),
    }


def exponent_ledger() -> dict[str, str | float]:
    """Exact power margins at the shallow common-height endpoint."""

    model_exponent = 1 + H_MIN
    target_exponent = 1 + EDGE_EXPONENT
    bridge_frontier = 1 + H_MIN - 4 * KAPPA
    return {
        "h_min": str(H_MIN),
        "edge_exponent": str(EDGE_EXPONENT),
        "generic_nested_model_exponent": str(model_exponent),
        "od2_target_exponent": str(target_exponent),
        "generic_model_miss": str(H_MIN - EDGE_EXPONENT),
        "bridge_frontier": str(bridge_frontier),
        "diagonal_margin_below_bridge": str(bridge_frontier - target_exponent),
    }


def audit() -> dict[str, object]:
    """Run a compact collection of exact finite certificates."""

    fine = [0, 2, 5, 7, 11, 14]
    deletion_order = [5, 11, 7]
    telescoped, coarse = telescope_deletions(fine, deletion_order)
    direct = signed_difference(coarse, fine)
    word_left = [0, 0, 1, 0, 0]
    word_right = [0, 1, 0, 0, 0]
    return {
        "deletion_telescope_exact": telescoped == direct,
        "affine_moments": tuple(str(value) for value in affine_moments(direct)),
        "first_return_left": first_return_distance(word_left),
        "first_return_right": first_return_distance(word_right),
        "tensor_product": paired_first_return_product(word_left, word_right),
        "periodic": periodic_refinement(17, 13, 5),
        "exponents": exponent_ledger(),
    }


if __name__ == "__main__":
    print(audit())
