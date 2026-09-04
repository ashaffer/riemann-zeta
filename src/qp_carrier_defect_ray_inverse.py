"""Exact carrier-preserving defect-ray identities for the QP product mask.

The physical carrier--colour operator has entries supported on actual triples
``(a,b,c)`` satisfying a narrow cubic product window.  Opening its Gram
matrix while retaining the common carrier ``b`` gives the exact integral
defect

``h = a*c-a'*c' = (rho-rho')/(8*b)``.

This module verifies the resulting decomposition without completing the
prime mask or translating the product window.  It also records the finite
Fourier self-duality of the determinant phase, which explains why a circle
major arc pulls back to the same physical defect rays rather than to a
one-variable prime progression.
"""

from __future__ import annotations

import cmath
from collections import defaultdict
from dataclasses import dataclass
from math import gcd, pi
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class MaskedTriple:
    """One weighted physical triple in the cubic product window."""

    a: int
    b: int
    c: int
    weight: complex = 1.0 + 0.0j

    def residual(self, q: int) -> int:
        return 8 * self.a * self.b * self.c - int(q) ** 3


def assert_pair_unique(triples: Sequence[MaskedTriple]) -> None:
    """Raise if any two coordinates support two distinct third coordinates."""

    seen: tuple[dict[tuple[int, int], int], ...] = ({}, {}, {})
    for triple in triples:
        records = (
            ((triple.a, triple.b), triple.c),
            ((triple.a, triple.c), triple.b),
            ((triple.b, triple.c), triple.a),
        )
        for table, (pair, third) in zip(seen, records):
            previous = table.setdefault(pair, third)
            if previous != third:
                raise ValueError("the triple family is not pair-unique")


def validate_product_window(
    triples: Sequence[MaskedTriple], q: int, half_width: int
) -> None:
    """Check pair uniqueness and the literal window ``|8abc-q^3|<=H``."""

    if q <= 0 or half_width < 0:
        raise ValueError("q must be positive and the half-width nonnegative")
    assert_pair_unique(triples)
    for triple in triples:
        if abs(triple.residual(q)) > half_width:
            raise ValueError("a triple lies outside the physical product window")


def carrier_action(
    triples: Sequence[MaskedTriple], color_vector: Mapping[int, complex]
) -> dict[int, complex]:
    """Apply the actual carrier--colour incidence operator to ``z``."""

    answer: dict[int, complex] = defaultdict(complex)
    for triple in triples:
        answer[triple.b] += triple.weight * color_vector.get(triple.c, 0.0)
    return dict(answer)


def centered_carrier_energy(
    triples: Sequence[MaskedTriple],
    color_vector: Mapping[int, complex],
    *,
    carrier_universe: Iterable[int] | None = None,
) -> float:
    """Return ``||P_b Tz||_2^2`` for exact orthogonal mean projection."""

    action = carrier_action(triples, color_vector)
    carriers = tuple(
        dict.fromkeys(
            carrier_universe
            if carrier_universe is not None
            else (triple.b for triple in triples)
        )
    )
    if not carriers:
        return 0.0
    mean = sum(action.get(carrier, 0.0) for carrier in carriers) / len(carriers)
    return float(
        sum(abs(action.get(carrier, 0.0) - mean) ** 2 for carrier in carriers)
    )


def defect_ray_ledger(
    triples: Sequence[MaskedTriple], color_vector: Mapping[int, complex]
) -> dict[str, object]:
    """Decompose ``||Tz||_2^2`` into diagonal and actual defect rays.

    Ordered distinct edges sharing ``b`` contribute to the ray

    ``h=a*c-a'*c'``.

    If ``rho=8abc-q^3`` and ``rho'=8a'bc'-q^3``, then exactly
    ``rho-rho'=8*b*h``.  In particular, no completed or off-window pair is
    inserted by this decomposition.
    """

    by_carrier: dict[int, list[MaskedTriple]] = defaultdict(list)
    color_degree: dict[int, int] = defaultdict(int)
    for triple in triples:
        by_carrier[triple.b].append(triple)
        color_degree[triple.c] += 1

    diagonal = 0.0
    rays: dict[int, complex] = defaultdict(complex)
    for edges in by_carrier.values():
        amplitudes = [
            edge.weight * color_vector.get(edge.c, 0.0) for edge in edges
        ]
        diagonal += sum(abs(amplitude) ** 2 for amplitude in amplitudes)
        for first_index, first in enumerate(edges):
            for second_index, second in enumerate(edges):
                if first_index == second_index:
                    continue
                defect = first.a * first.c - second.a * second.c
                rays[defect] += (
                    amplitudes[first_index]
                    * amplitudes[second_index].conjugate()
                )

    action = carrier_action(triples, color_vector)
    action_energy = float(sum(abs(value) ** 2 for value in action.values()))
    reconstructed = diagonal + sum(rays.values(), 0.0 + 0.0j)
    return {
        "diagonal_energy": diagonal,
        "rays": dict(rays),
        "action_energy": action_energy,
        "reconstructed_energy": reconstructed,
        "maximum_color_degree": max(color_degree.values(), default=0),
    }


def defect_height_bound(q: int, half_width: int, minimum_carrier: int) -> int:
    """Return the exact integer bound from ``|rho-rho'|<=2H``."""

    if q <= 0 or half_width < 0 or minimum_carrier <= 0:
        raise ValueError("invalid physical scales")
    # 8*b*|h| <= 2*H.
    return half_width // (4 * minimum_carrier)


def coherent_ray_certificate(
    triples: Sequence[MaskedTriple],
    color_vector: Mapping[int, complex],
    q: int,
    half_width: int,
    *,
    carrier_universe: Iterable[int] | None = None,
) -> dict[str, object]:
    """Return the quantitative mask-preserving coherent-ray certificate.

    Since orthogonal centering can only lower the carrier energy, the sum of
    the nonzero paired rays is at least

    ``||P_b Tz||^2-diagonal-|zero ray|``.

    There are at most ``H/(4*b_min)`` positive defects.  Hence one actual
    ray pair has at least the displayed excess divided by that number.
    """

    if not triples:
        raise ValueError("the certificate needs at least one actual triple")
    validate_product_window(triples, q, half_width)
    ledger = defect_ray_ledger(triples, color_vector)
    rays = ledger["rays"]
    assert isinstance(rays, dict)
    centered_energy = centered_carrier_energy(
        triples, color_vector, carrier_universe=carrier_universe
    )
    zero_ray = rays.get(0, 0.0 + 0.0j)
    positive_defects = sorted({abs(defect) for defect in rays if defect})
    paired_ray_energy = {
        defect: (rays.get(defect, 0.0) + rays.get(-defect, 0.0)).real
        for defect in positive_defects
    }
    height_bound = defect_height_bound(
        q, half_width, min(triple.b for triple in triples)
    )
    forced_total = max(
        0.0,
        centered_energy
        - float(ledger["diagonal_energy"])
        - abs(zero_ray),
    )
    forced_single_ray = forced_total / max(1, height_bound)
    return {
        **ledger,
        "centered_energy": centered_energy,
        "zero_ray": zero_ray,
        "paired_ray_energy": paired_ray_energy,
        "height_bound": height_bound,
        "forced_nonzero_ray_total": forced_total,
        "forced_single_ray_lower_bound": forced_single_ray,
        "largest_observed_paired_ray": max(
            paired_ray_energy.values(), default=0.0
        ),
    }


def additive_character(value: int, modulus: int) -> complex:
    return cmath.exp(2j * pi * (int(value) % int(modulus)) / int(modulus))


def determinant_fourier_sum(
    modulus: int,
    numerator: int,
    frequencies: tuple[int, int, int, int],
) -> complex:
    """Brute-force the Fourier transform of ``e_r(a det)`` on ``M_2``."""

    r = int(modulus)
    a = int(numerator)
    if r <= 1 or gcd(a, r) != 1:
        raise ValueError("numerator must be a unit modulo a nontrivial modulus")
    u, v, up, vp = map(int, frequencies)
    return sum(
        additive_character(
            a * (x * y - xp * yp) + u * x + v * y + up * xp + vp * yp,
            r,
        )
        for x in range(r)
        for y in range(r)
        for xp in range(r)
        for yp in range(r)
    )


def determinant_fourier_prediction(
    modulus: int,
    numerator: int,
    frequencies: tuple[int, int, int, int],
) -> complex:
    """Return the exact self-dual determinant Fourier transform."""

    r = int(modulus)
    a = int(numerator)
    if r <= 1 or gcd(a, r) != 1:
        raise ValueError("numerator must be a unit modulo a nontrivial modulus")
    u, v, up, vp = map(int, frequencies)
    inverse = pow(a, -1, r)
    return r * r * additive_character(inverse * (up * vp - u * v), r)


def ramanujan_sum(modulus: int, value: int) -> complex:
    """Return ``sum_(a mod r)^* e_r(a*value)`` exactly."""

    r = int(modulus)
    if r <= 0:
        raise ValueError("modulus must be positive")
    return sum(
        additive_character(a * int(value), r)
        for a in range(r)
        if gcd(a, r) == 1
    )


def prime_rectangle_wedge_fixture() -> tuple[int, int, tuple[MaskedTriple, ...]]:
    """Return the all-eight-distinct prime rectangle at ``q=50021``.

    The four triples lie in a literal product window of half-width twenty
    million.  Opening by common carrier produces the two nonzero physical
    defect magnitudes 42 and 36.
    """

    q = 50_021
    half_width = 20_000_000
    a1, a2 = 21_277, 22_741
    b1, b2 = 28_277, 28_793
    c11, c12, c21, c22 = 26_003, 25_537, 24_329, 23_893
    triples = (
        MaskedTriple(a1, b1, c11),
        MaskedTriple(a1, b2, c12),
        MaskedTriple(a2, b1, c21),
        MaskedTriple(a2, b2, c22),
    )
    validate_product_window(triples, q, half_width)
    return q, half_width, triples
