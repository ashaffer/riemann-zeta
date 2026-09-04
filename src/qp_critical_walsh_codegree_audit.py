"""Critical flat-bin Walsh tail and transverse codegree identities.

The diffuse weighted-triangle square theorem gives total randomized mass

    R << D * min(1, D/M) * ||z||_2^4

on a factor-two coefficient bin of support ``M``.  Therefore the Walsh
Carleson estimate ``R_H << D/H`` is automatic for ``H <= M/D``.  Above
that threshold the effective Walsh multiplicity is bounded by the literal
common-neighbor codegree.

This module also records two exact identities for a fixed endpoint pair
``x<y``.  A common-neighbor walk consists of a carrier ``v`` and
completions ``a,b`` with residuals

    r=8*x*v*a-q^3,  s=8*y*v*b-q^3.

Writing ``h=y-x``, ``j=a-b``, and ``k=x*a-y*b`` gives

    y*r-x*s = 8*x*y*v*j-h*q^3,
    r-s     = 8*v*k.

Thus every transverse fibre is a carrier-preserving short-product fan.
For two walks, its completion determinant satisfies

    x*(a_i*b_l-a_l*b_i)=k_i*b_l-k_l*b_i.

The identities are exact; they do not by themselves prove the needed
actual-prime codegree bound.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Sequence


@dataclass(frozen=True)
class CriticalWalshExponentLedger:
    support_exponent: Fraction
    refined_randomized_exponent: Fraction
    automatic_carleson_cutoff_exponent: Fraction
    close_row_gap_exponent: Fraction
    close_row_remainder_exponent: Fraction
    close_row_covers_cutoff: bool


def critical_walsh_exponent_ledger(
    support_exponent: Fraction = Fraction(15, 8),
) -> CriticalWalshExponentLedger:
    """Return the exact powers of ``D`` in the flat-bin reduction.

    For ``M=D^mu`` and ``mu>1``, the refined randomized mass is
    ``D^(2-mu)`` and the nonautomatic Walsh multiplicity begins at
    ``H=D^(mu-1)``.  The existing close-row estimate is

    ``codeg(x,y) << (|x-y|+1)D^(1/2)+D^(13/16)``.
    """

    mu = Fraction(support_exponent)
    randomized = Fraction(1) if mu <= 1 else 2 - mu
    cutoff = max(Fraction(0), mu - 1)
    close_gap = cutoff - Fraction(1, 2)
    remainder = Fraction(13, 16)
    return CriticalWalshExponentLedger(
        support_exponent=mu,
        refined_randomized_exponent=randomized,
        automatic_carleson_cutoff_exponent=cutoff,
        close_row_gap_exponent=close_gap,
        close_row_remainder_exponent=remainder,
        close_row_covers_cutoff=(
            close_gap >= 0 and remainder <= cutoff
        ),
    )


@dataclass(frozen=True)
class CommonNeighborWalk:
    carrier: int
    first_completion: int
    second_completion: int


@dataclass(frozen=True)
class TransverseCodegreeLedger:
    q: int
    first_endpoint: int
    second_endpoint: int
    endpoint_gap: int
    walk_count: int
    first_residuals: tuple[int, ...]
    second_residuals: tuple[int, ...]
    defects: tuple[int, ...]
    completion_gaps: tuple[int, ...]
    maximum_residual_identity_error: int
    maximum_product_identity_error: int
    maximum_determinant_identity_error: int
    distinct_defects: int
    completion_determinant_value_count: int
    completion_determinant_energy: int
    determinant_energy_cauchy_lower: Fraction
    nonzero_determinant_value_count: int
    nonzero_determinant_energy: int
    nonzero_determinant_energy_cauchy_lower: Fraction
    most_popular_completion_determinant: int
    most_popular_determinant_multiplicity: int
    product_strip_numerators: tuple[int, ...]


def transverse_common_neighbor_ledger(
    q: int,
    first_endpoint: int,
    second_endpoint: int,
    walks: Sequence[CommonNeighborWalk],
) -> TransverseCodegreeLedger:
    """Evaluate the carrier, defect, and determinant identities exactly."""

    modulus = int(q)
    x = int(first_endpoint)
    y = int(second_endpoint)
    if min(modulus, x, y) <= 0 or x >= y:
        raise ValueError("require q>0 and 0<first_endpoint<second_endpoint")
    materialized = tuple(walks)
    h = y - x
    first_residuals: list[int] = []
    second_residuals: list[int] = []
    defects: list[int] = []
    completion_gaps: list[int] = []
    product_numerators: list[int] = []
    residual_errors: list[int] = []
    product_errors: list[int] = []

    for walk in materialized:
        v = int(walk.carrier)
        a = int(walk.first_completion)
        b = int(walk.second_completion)
        if min(v, a, b) <= 0:
            raise ValueError("walk entries must be positive")
        r = 8 * x * v * a - modulus**3
        s = 8 * y * v * b - modulus**3
        k = x * a - y * b
        j = a - b
        product_numerator = 8 * x * y * v * j - h * modulus**3
        first_residuals.append(r)
        second_residuals.append(s)
        defects.append(k)
        completion_gaps.append(j)
        product_numerators.append(product_numerator)
        residual_errors.append((r - s) - 8 * v * k)
        product_errors.append(product_numerator - (y * r - x * s))

    determinant_counts: Counter[int] = Counter()
    determinant_errors: list[int] = []
    for first in materialized:
        a = int(first.first_completion)
        b = int(first.second_completion)
        k = x * a - y * b
        for second in materialized:
            c = int(second.first_completion)
            d = int(second.second_completion)
            ell = x * c - y * d
            determinant = a * d - c * b
            determinant_counts[determinant] += 1
            determinant_errors.append(x * determinant - (k * d - ell * b))

    walk_count = len(materialized)
    determinant_energy = sum(value * value for value in determinant_counts.values())
    determinant_values = len(determinant_counts)
    cauchy_lower = (
        Fraction(walk_count**4, determinant_values)
        if determinant_values
        else Fraction(0)
    )
    nonzero_counts = {
        determinant: multiplicity
        for determinant, multiplicity in determinant_counts.items()
        if determinant
    }
    nonzero_energy = sum(value * value for value in nonzero_counts.values())
    nonzero_values = len(nonzero_counts)
    nonzero_mass = sum(nonzero_counts.values())
    nonzero_cauchy_lower = (
        Fraction(nonzero_mass**2, nonzero_values)
        if nonzero_values
        else Fraction(0)
    )
    if nonzero_counts:
        popular_determinant, popular_multiplicity = max(
            nonzero_counts.items(), key=lambda item: item[1]
        )
    else:
        popular_determinant, popular_multiplicity = 0, 0
    return TransverseCodegreeLedger(
        q=modulus,
        first_endpoint=x,
        second_endpoint=y,
        endpoint_gap=h,
        walk_count=walk_count,
        first_residuals=tuple(first_residuals),
        second_residuals=tuple(second_residuals),
        defects=tuple(defects),
        completion_gaps=tuple(completion_gaps),
        maximum_residual_identity_error=max(map(abs, residual_errors), default=0),
        maximum_product_identity_error=max(map(abs, product_errors), default=0),
        maximum_determinant_identity_error=max(
            map(abs, determinant_errors), default=0
        ),
        distinct_defects=len(set(defects)),
        completion_determinant_value_count=determinant_values,
        completion_determinant_energy=determinant_energy,
        determinant_energy_cauchy_lower=cauchy_lower,
        nonzero_determinant_value_count=nonzero_values,
        nonzero_determinant_energy=nonzero_energy,
        nonzero_determinant_energy_cauchy_lower=nonzero_cauchy_lower,
        most_popular_completion_determinant=popular_determinant,
        most_popular_determinant_multiplicity=popular_multiplicity,
        product_strip_numerators=tuple(product_numerators),
    )


def constant_determinant_path_step(
    points: Sequence[tuple[int, int]],
) -> tuple[int, int]:
    r"""Recover the exact arithmetic-progression step of a determinant path.

    Assume all coordinates lie in a positive collar of ratio below ``3/2``,
    every point is primitive, and all consecutive oriented determinants are
    one common nonzero integer.  For three consecutive points ``p,q,r``,

    ``det(q,p+r)=0``.

    Primitivity makes ``p+r=lambda*q`` with integral ``lambda``.  The collar
    gives ``1<lambda<3``, hence ``lambda=2``.  The whole path is therefore
    an exact vector arithmetic progression.
    """

    materialized = tuple((int(a), int(b)) for a, b in points)
    if len(materialized) < 2:
        raise ValueError("at least two points are required")
    coordinates = [coordinate for point in materialized for coordinate in point]
    if min(coordinates) <= 0 or 2 * max(coordinates) >= 3 * min(coordinates):
        raise ValueError("points must lie in a positive ratio-<3/2 collar")
    if any(gcd(a, b) != 1 for a, b in materialized):
        raise ValueError("every point must be primitive")

    determinants = tuple(
        a * d - c * b
        for (a, b), (c, d) in zip(materialized, materialized[1:])
    )
    if not determinants[0] or len(set(determinants)) != 1:
        raise ValueError("consecutive oriented determinants must be equal and nonzero")
    step = (
        materialized[1][0] - materialized[0][0],
        materialized[1][1] - materialized[0][1],
    )
    for previous, current, following in zip(
        materialized, materialized[1:], materialized[2:]
    ):
        if (
            previous[0] + following[0] != 2 * current[0]
            or previous[1] + following[1] != 2 * current[1]
        ):
            raise AssertionError("the constant-determinant path is not affine")
    if any(
        point
        != (
            materialized[0][0] + index * step[0],
            materialized[0][1] + index * step[1],
        )
        for index, point in enumerate(materialized)
    ):
        raise AssertionError("the recovered path step is inconsistent")
    return step
