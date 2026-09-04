"""Finite hostile tests for the two-sided residual-lattice argument.

The routines here deliberately separate three different statements:

* the two one-sided covolume/line-occupancy bounds;
* the exact matched bilinear level;
* a congruence-level modular-parabola model.

The last two are not interchangeable.  In particular, lifting a modular
bilinear level to least integer representatives normally splits it into
many exact integer levels.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt
from random import Random
from typing import Iterable, Sequence


Point = tuple[int, int]
MatchedPoint = tuple[Point, Point]


@dataclass(frozen=True)
class TwoSidedLineCap:
    """The conjunction, not the product, of the two lattice caps."""

    lattice_determinant: int
    row_area: int
    carrier_area: int
    row_cap: int
    carrier_cap: int
    combined_cap: int


def _safe_square_root_ratio(area: int, determinant: int) -> int:
    quotient = (area + determinant - 1) // determinant
    root = isqrt(quotient)
    return root if root * root == quotient else root + 1


def two_sided_line_cap(
    lattice_determinant: int,
    row_widths: tuple[int, int],
    carrier_widths: tuple[int, int],
    maximum_line_occupancy: int = 2,
) -> TwoSidedLineCap:
    """Return a safe constant version of the two one-sided estimates.

    The mathematical scale is

        m << T * min(1+sqrt(EF/|k|), 1+sqrt(GH/|k|)).

    The factor four only absorbs the elementary Minkowski and boundary
    constants.  There is no multiplication of the two estimates: the same
    matched set is being bounded twice.
    """

    determinant = abs(int(lattice_determinant))
    if determinant == 0:
        raise ValueError("the lattice determinant must be nonzero")
    if maximum_line_occupancy < 1:
        raise ValueError("line occupancy must be positive")
    widths = (*row_widths, *carrier_widths)
    if any(width < 0 for width in widths):
        raise ValueError("rectangle widths must be nonnegative")
    row_area = row_widths[0] * row_widths[1]
    carrier_area = carrier_widths[0] * carrier_widths[1]
    row_cap = maximum_line_occupancy * (
        1 + 4 * _safe_square_root_ratio(row_area, determinant)
    )
    carrier_cap = maximum_line_occupancy * (
        1 + 4 * _safe_square_root_ratio(carrier_area, determinant)
    )
    return TwoSidedLineCap(
        lattice_determinant=determinant,
        row_area=row_area,
        carrier_area=carrier_area,
        row_cap=row_cap,
        carrier_cap=carrier_cap,
        combined_cap=min(row_cap, carrier_cap),
    )


@dataclass(frozen=True)
class TwoSidedExponentCap:
    """Power-scale version of the conjunction of the two caps."""

    row_exponent: Fraction
    carrier_exponent: Fraction
    combined_exponent: Fraction


def two_sided_exponent_cap(
    determinant: Fraction,
    row_widths: tuple[Fraction, Fraction],
    carrier_widths: tuple[Fraction, Fraction],
) -> TwoSidedExponentCap:
    row = max(Fraction(0), (sum(row_widths) - determinant) / 2)
    carrier = max(Fraction(0), (sum(carrier_widths) - determinant) / 2)
    return TwoSidedExponentCap(row, carrier, min(row, carrier))


def affine_determinant(first: Point, second: Point, third: Point) -> int:
    """Twice the signed area of three integer points."""

    return (second[0] - first[0]) * (third[1] - first[1]) - (
        second[1] - first[1]
    ) * (third[0] - first[0])


def has_no_three_collinear(points: Sequence[Point]) -> bool:
    if len(set(points)) != len(points):
        return False
    return all(
        affine_determinant(*triple) != 0
        for triple in combinations(points, 3)
    )


def modular_parabola_zero_level(prime: int) -> tuple[MatchedPoint, ...]:
    """A square-box, two-sided no-three-line matching at exact level zero.

    For ``y_t=t^2 mod p``, take ``r_t=(t,y_t)`` and rotate it to
    ``s_t=(-y_t,t)``.  Their ordinary dot product is exactly zero even for
    the least integer lifts.  Reduction modulo ``p`` proves that either
    projection has no three collinear points.
    """

    if prime < 2:
        raise ValueError("the modulus must be at least two")
    return tuple(
        ((parameter, parameter * parameter % prime),
         (-(parameter * parameter % prime), parameter))
        for parameter in range(prime)
    )


def modular_inverse_parabola(prime: int) -> tuple[MatchedPoint, ...]:
    """A nonzero *congruence*-level matching on two finite-field conics.

    With ``u=t^{-1} mod p``, the two projections are ``(t,t^2)`` and
    ``(u,u^2)`` modulo ``p`` and their dot product is ``2 mod p``.  The
    returned least integer lifts generally do not have one common exact
    dot product; that fragmentation is an important fail-fast check.
    """

    if prime < 3:
        raise ValueError("use an odd prime modulus")
    output: list[MatchedPoint] = []
    for parameter in range(1, prime):
        inverse = pow(parameter, -1, prime)
        output.append(
            (
                (parameter, parameter * parameter % prime),
                (inverse, inverse * inverse % prime),
            )
        )
    return tuple(output)


def exact_dot_levels(matching: Iterable[MatchedPoint]) -> Counter[int]:
    return Counter(
        row[0] * carrier[0] + row[1] * carrier[1]
        for row, carrier in matching
    )


def exact_parabola_matching(parameter: int) -> MatchedPoint:
    """An arbitrarily long exact nonzero-level, line-sparse matching."""

    value = int(parameter)
    return (
        (value, value * value + 1),
        (value * value - value + 1, 1 - value),
    )


def _centered_bezout_partner(first: int, second: int) -> Point:
    """A box-sized partner with ``first*u+second*v=1``.

    ``first`` and ``second`` must be positive and coprime.  Translating the
    centered Bezout solution once by ``(second,-first)`` makes the partner
    have size comparable with the input while retaining exact dot level one.
    """

    if first <= 0 or second <= 1 or gcd(first, second) != 1:
        raise ValueError("positive coprime inputs are required")
    first_coordinate = pow(first, -1, second)
    if 2 * first_coordinate > second:
        first_coordinate -= second
    second_coordinate = (1 - first * first_coordinate) // second
    partner = (
        first_coordinate + second,
        second_coordinate - first,
    )
    assert first * partner[0] + second * partner[1] == 1
    return partner


def exact_bezout_square_pool(order: int) -> tuple[MatchedPoint, ...]:
    """Return the ``asymp order^2`` exact-level pool used in the proof.

    Rows range over primitive points in ``[N,2N]^2``.  Their partners lie
    in an absolute ``O(N)`` square, have exact dot product one, and every
    carrier point has only ``O(1)`` preimages.  A standard random deletion
    argument extracts ``Omega(N/sqrt(log N))`` pairs in simultaneous
    no-three-line position.
    """

    if order < 2:
        raise ValueError("order must be at least two")
    output: list[MatchedPoint] = []
    for first in range(order, 2 * order + 1):
        for second in range(order, 2 * order + 1):
            if gcd(first, second) == 1:
                output.append(
                    ((first, second), _centered_bezout_partner(first, second))
                )
    return tuple(output)


def _normalized_line(first: Point, second: Point) -> tuple[int, int, int]:
    if first == second:
        raise ValueError("a line needs two distinct points")
    a_coefficient = second[1] - first[1]
    b_coefficient = first[0] - second[0]
    c_coefficient = -(
        a_coefficient * first[0] + b_coefficient * first[1]
    )
    content = gcd(
        gcd(abs(a_coefficient), abs(b_coefficient)), abs(c_coefficient)
    )
    if content:
        a_coefficient //= content
        b_coefficient //= content
        c_coefficient //= content
    if a_coefficient < 0 or (
        a_coefficient == 0 and b_coefficient < 0
    ):
        a_coefficient *= -1
        b_coefficient *= -1
        c_coefficient *= -1
    return a_coefficient, b_coefficient, c_coefficient


def greedy_two_sided_general_position(
    matching: Sequence[MatchedPoint], seed: int = 0
) -> tuple[MatchedPoint, ...]:
    """Greedy finite diagnostic; the theorem itself uses random deletion."""

    indices = list(range(len(matching)))
    Random(seed).shuffle(indices)
    chosen: list[MatchedPoint] = []
    row_lines: set[tuple[int, int, int]] = set()
    carrier_lines: set[tuple[int, int, int]] = set()
    rows: set[Point] = set()
    carriers: set[Point] = set()
    for index in indices:
        row, carrier = matching[index]
        if row in rows or carrier in carriers:
            continue
        if any(a * row[0] + b * row[1] + c == 0 for a, b, c in row_lines):
            continue
        if any(
            a * carrier[0] + b * carrier[1] + c == 0
            for a, b, c in carrier_lines
        ):
            continue
        for old_row, old_carrier in chosen:
            row_lines.add(_normalized_line(old_row, row))
            carrier_lines.add(_normalized_line(old_carrier, carrier))
        chosen.append((row, carrier))
        rows.add(row)
        carriers.add(carrier)
    return tuple(chosen)

