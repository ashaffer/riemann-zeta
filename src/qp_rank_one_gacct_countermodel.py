"""Exact abstract countermodel separating GACCT from the rank-one target.

Let ``s`` be prime.  Rows are points of ``F_s^4`` and columns are its affine
hyperplanes.  Two hyperplanes with distinct projective normals meet in
``s^2`` points, while distinct parallel hyperplanes are disjoint.

Assign every hyperplane column its own disjoint ordered pair of colors.  The
cardinal high-codegree tail is then of order ``s^4`` at multiplicity
``K=s^2``, although every pure pair vector ``conj(z) tensor z`` has energy at
most ``D/4`` for ``D=s^4``.  This is an abstract incidence construction, not
an actual QP hard-window counterexample.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Sequence


Vector4 = tuple[int, int, int, int]
Hyperplane = tuple[Vector4, int]


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def projective_normals(prime: int) -> tuple[Vector4, ...]:
    """Return the canonical points of ``P^3(F_prime)``.

    The first nonzero coordinate is normalized to one.
    """

    if not _is_prime(prime):
        raise ValueError("the finite-field order must be prime")
    normals: set[Vector4] = set()
    for vector in product(range(prime), repeat=4):
        if vector == (0, 0, 0, 0):
            continue
        first = next(coordinate for coordinate in vector if coordinate)
        inverse = pow(first, -1, prime)
        normals.add(tuple((inverse * coordinate) % prime for coordinate in vector))
    return tuple(sorted(normals))


def affine_hyperplane_supports(
    prime: int,
) -> tuple[tuple[Vector4, ...], tuple[Hyperplane, ...], tuple[frozenset[int], ...]]:
    """Enumerate points, affine hyperplanes, and their exact supports."""

    normals = projective_normals(prime)
    points = tuple(product(range(prime), repeat=4))
    hyperplanes = tuple((normal, level) for normal in normals for level in range(prime))
    supports: list[frozenset[int]] = []
    for normal, level in hyperplanes:
        supports.append(
            frozenset(
                index
                for index, point in enumerate(points)
                if sum(a * b for a, b in zip(normal, point)) % prime == level
            )
        )
    return points, hyperplanes, tuple(supports)


@dataclass(frozen=True)
class RankOneGACCTCountermodelLedger:
    field_order: int
    row_count: int
    projective_normal_count: int
    column_count: int
    column_degree: int
    dyadic_multiplicity: int
    target_D: int
    gacct_allowance: int
    high_partner_count: int
    gacct_failure_factor: Fraction
    normalized_rank_one_energy_upper: Fraction
    normalized_hc_weight_upper: Fraction


def rank_one_gacct_countermodel_ledger(
    prime: int, *, verify_intersections: bool = True
) -> RankOneGACCTCountermodelLedger:
    """Return and optionally replay the finite-field countermodel ledger."""

    normals = projective_normals(prime)
    normal_count = prime**3 + prime**2 + prime + 1
    if len(normals) != normal_count:
        raise AssertionError("the projective-normal count failed")
    row_count = prime**4
    column_count = prime * normal_count
    column_degree = prime**3
    multiplicity = prime**2
    high_partners = column_count - prime
    if verify_intersections:
        _points, hyperplanes, supports = affine_hyperplane_supports(prime)
        if len(hyperplanes) != column_count:
            raise AssertionError("the affine-hyperplane count failed")
        if any(len(support) != column_degree for support in supports):
            raise AssertionError("an affine hyperplane has the wrong size")
        for first in range(column_count):
            first_normal, _first_level = hyperplanes[first]
            for second in range(first + 1, column_count):
                second_normal, _second_level = hyperplanes[second]
                intersection = len(supports[first] & supports[second])
                expected = 0 if first_normal == second_normal else multiplicity
                if intersection != expected:
                    raise AssertionError("the hyperplane codegree law failed")
    allowance = row_count // multiplicity
    return RankOneGACCTCountermodelLedger(
        field_order=prime,
        row_count=row_count,
        projective_normal_count=normal_count,
        column_count=column_count,
        column_degree=column_degree,
        dyadic_multiplicity=multiplicity,
        target_D=row_count,
        gacct_allowance=allowance,
        high_partner_count=high_partners,
        gacct_failure_factor=Fraction(high_partners, allowance),
        normalized_rank_one_energy_upper=Fraction(row_count, 4),
        normalized_hc_weight_upper=Fraction(1, 4),
    )


@dataclass(frozen=True)
class RankOneMassLedger:
    color_norm_squared: float
    selected_pair_l1: float
    exact_incidence_energy: float
    dyadic_hc_weight: float
    energy_upper: float
    hc_upper: float


def rank_one_masses(
    prime: int,
    left_colors: Sequence[complex],
    right_colors: Sequence[complex],
) -> RankOneMassLedger:
    """Evaluate the exact incidence energy and the ``K=s^2`` HC layer.

    Entry ``i`` represents the disjoint ordered color pair
    ``(left_colors[i], right_colors[i])``.  The full color norm is the sum of
    the squared moduli of all these disjoint labels.
    """

    points, hyperplanes, supports = affine_hyperplane_supports(prime)
    if len(left_colors) != len(hyperplanes) or len(right_colors) != len(hyperplanes):
        raise ValueError("one disjoint color pair is required per hyperplane")
    pair_values = tuple(
        complex(left).conjugate() * complex(right)
        for left, right in zip(left_colors, right_colors)
    )
    pair_magnitudes = tuple(abs(value) for value in pair_values)
    color_norm = sum(abs(value) ** 2 for value in left_colors) + sum(
        abs(value) ** 2 for value in right_colors
    )
    selected_l1 = sum(pair_magnitudes)
    row_sums = [0j for _point in points]
    for value, support in zip(pair_values, supports):
        for point_index in support:
            row_sums[point_index] += value
    energy = sum(abs(value) ** 2 for value in row_sums)
    hc_weight = 0.0
    for first, ((normal, _level), first_weight) in enumerate(
        zip(hyperplanes, pair_magnitudes)
    ):
        for second, ((other_normal, _other_level), second_weight) in enumerate(
            zip(hyperplanes, pair_magnitudes)
        ):
            if first != second and normal != other_normal:
                hc_weight += first_weight * second_weight
    energy_upper = prime**4 * color_norm**2 / 4
    hc_upper = color_norm**2 / 4
    if selected_l1 > color_norm / 2 + 1e-12:
        raise AssertionError("disjoint-pair AM-GM failed")
    if energy > energy_upper + 1e-9 * max(1.0, energy_upper):
        raise AssertionError("the rank-one energy bound failed")
    if hc_weight > hc_upper + 1e-9 * max(1.0, hc_upper):
        raise AssertionError("the rank-one HC bound failed")
    return RankOneMassLedger(
        color_norm_squared=float(color_norm),
        selected_pair_l1=float(selected_l1),
        exact_incidence_energy=float(energy),
        dyadic_hc_weight=float(hc_weight),
        energy_upper=float(energy_upper),
        hc_upper=float(hc_upper),
    )
