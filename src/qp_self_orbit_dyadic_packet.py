"""Exact ledgers for the self-orbit dyadic reciprocal packet reduction.

This module does not prove the open dyadic reciprocal large-sieve estimate.
It records the exact finite identities which make that estimate the right
target and the new local fact that every natural-scale self-orbit cluster is
an affine packet.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd, sqrt
from typing import Iterable

Point = tuple[int, int]


def determinant(first: Point, second: Point) -> int:
    """Return the oriented determinant of two integer vectors."""

    return first[0] * second[1] - first[1] * second[0]


def affine_area(first: Point, second: Point, third: Point) -> int:
    """Return twice the oriented affine area of three lattice points."""

    return determinant(
        (second[0] - first[0], second[1] - first[1]),
        (third[0] - first[0], third[1] - first[1]),
    )


def orbit_label(anchor: Point, point: Point) -> int:
    """The determinant label ``c*b-C*B`` of a physical orbit point."""

    c, C = anchor
    b, B = point
    return c * b - C * B


def label_area_identity(
    anchor: Point, first: Point, second: Point, third: Point
) -> tuple[int, int]:
    """Return the two exactly equal sides of the local affine identity.

    If ``t_i=c*b_i-C*B_i``, then

    ``C*area = (t_2-t_1)(b_3-b_1)-(b_2-b_1)(t_3-t_1)``.
    """

    _, C = anchor
    t1, t2, t3 = (orbit_label(anchor, point) for point in (first, second, third))
    b1, b2, b3 = first[0], second[0], third[0]
    left = C * affine_area(first, second, third)
    right = (t2 - t1) * (b3 - b1) - (b2 - b1) * (t3 - t1)
    return left, right


@dataclass(frozen=True)
class LocalAffinePacketCertificate:
    anchor: Point
    degree: int
    radius: int
    point_count: int
    maximum_label: int
    first_coordinate_diameter: int
    area_numerator_bound: int
    anchor_denominator: int
    all_collinear: bool


def certify_local_affine_packet(
    anchor: Point,
    points: Iterable[Point],
    degree: int,
    radius: int,
) -> LocalAffinePacketCertificate:
    """Certify that one natural-scale orbit cell is exactly affine.

    The hypotheses are deliberately checkable and integral: every label has
    absolute value at most ``degree``, the first-coordinate diameter is at
    most ``radius``, and ``4*degree*radius < |C|``.  The label-area identity
    then puts the integral affine area strictly between ``-1`` and ``1``.
    """

    selected = tuple(points)
    if degree < 0 or radius < 0:
        raise ValueError("degree and radius must be nonnegative")
    if not selected:
        diameter = 0
        maximum_label = 0
    else:
        first_coordinates = [point[0] for point in selected]
        diameter = max(first_coordinates) - min(first_coordinates)
        maximum_label = max(abs(orbit_label(anchor, point)) for point in selected)
    if maximum_label > degree:
        raise ValueError("a point lies outside the determinant-label window")
    if diameter > radius:
        raise ValueError("the points do not lie in one first-coordinate cell")
    _, C = anchor
    numerator_bound = 4 * degree * radius
    if numerator_bound >= abs(C):
        raise ValueError("the integral-area inequality is not strict")

    all_collinear = True
    for triple in combinations(selected, 3):
        left, right = label_area_identity(anchor, *triple)
        if left != right:
            raise AssertionError("the exact label-area identity failed")
        # The sharper data-dependent inequality is useful in finite tests;
        # the displayed 4*D*R bound is the uniform theorem.
        if abs(right) > numerator_bound:
            raise AssertionError("the uniform label-area bound failed")
        if left % C != 0 or abs(left) >= abs(C):
            raise AssertionError("integral-area divisibility failed")
        all_collinear &= affine_area(*triple) == 0
    if not all_collinear:
        raise AssertionError("the strict integral-area hypotheses force collinearity")
    return LocalAffinePacketCertificate(
        anchor=anchor,
        degree=degree,
        radius=radius,
        point_count=len(selected),
        maximum_label=maximum_label,
        first_coordinate_diameter=diameter,
        area_numerator_bound=numerator_bound,
        anchor_denominator=abs(C),
        all_collinear=all_collinear,
    )


@dataclass(frozen=True)
class CloseDirectionCertificate:
    primitive_direction: Point
    multiplicity: int
    label_step: int
    legendre_numerator: int
    legendre_denominator: int
    satisfies_legendre: bool


def close_direction_certificate(
    anchor: Point, first: Point, second: Point
) -> CloseDirectionCertificate:
    """Check the continued-fraction criterion for a close orbit direction.

    Orient the difference so its first coordinate is positive and write it
    as ``g*(p,P)`` with a primitive direction.  The determinant-label step is
    ``r=c*p-C*P``.  For positive ``c,p,P``, the exact inequality
    ``2*|r|*P<c`` is Legendre's criterion for ``p/P`` to be a convergent of
    ``C/c``.
    """

    dx, dy = second[0] - first[0], second[1] - first[1]
    if dx == 0 and dy == 0:
        raise ValueError("the two points must be distinct")
    if dx < 0:
        dx, dy = -dx, -dy
    multiplicity = gcd(abs(dx), abs(dy))
    p, P = dx // multiplicity, dy // multiplicity
    c, C = anchor
    label_step = c * p - C * P
    valid_signs = c > 0 and p > 0 and P > 0
    return CloseDirectionCertificate(
        primitive_direction=(p, P),
        multiplicity=multiplicity,
        label_step=label_step,
        legendre_numerator=2 * abs(label_step) * abs(P),
        legendre_denominator=abs(c),
        satisfies_legendre=valid_signs and 2 * abs(label_step) * P < c,
    )


def cross_determinant_from_labels(
    anchor: Point, first: Point, second: Point
) -> tuple[int, int]:
    """Return the equal sides of ``C*det=(t_1*b_2-t_2*b_1)``."""

    _, C = anchor
    t1 = orbit_label(anchor, first)
    t2 = orbit_label(anchor, second)
    return C * determinant(first, second), t1 * second[0] - t2 * first[0]


def tower_coordinate_identities(
    anchor: Point, direction: Point, point: Point
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return the exact index-``r`` tower coordinate identities.

    With ``r=c*p-C*P``, orbit label ``t=c*b-C*B``, and transverse line
    index ``s=p*B-P*b``, one has

    ``r*b=p*t+C*s`` and ``r*B=P*t+c*s``.
    """

    c, C = anchor
    p, P = direction
    b, B = point
    r = c * p - C * P
    t = c * b - C * B
    s = p * B - P * b
    return (r * b, p * t + C * s), (r * B, P * t + c * s)


def reciprocal_chart_difference(
    q: int, first: Point, second: Point
) -> tuple[Fraction, Fraction]:
    """Return the exact two-chart difference and its determinant formula."""

    b, B = first
    d, D = second
    if 0 in (b, B, d, D):
        raise ZeroDivisionError("reciprocal chart coordinates must be nonzero")
    Q = Fraction(q**3, 8)
    direct = Q / (b * D) - Q / (B * d)
    formula = -Q * determinant(first, second) / (b * D * B * d)
    return direct, formula


def cleared_reciprocal_collision(
    Q: Fraction, first_product: int, second_product: int, shift: int
) -> tuple[Fraction, Fraction]:
    """Clear denominators in one reciprocal collision exactly."""

    if first_product == 0 or second_product == 0:
        raise ZeroDivisionError("products must be nonzero")
    direct = Q / first_product - Q / second_product - shift
    residual = (
        Q * (second_product - first_product)
        - shift * first_product * second_product
    ) / (first_product * second_product)
    return direct, residual


@dataclass(frozen=True)
class DyadicPacketExponentLedger:
    degree: Fraction
    low_frequency: Fraction
    top_frequency: Fraction
    largest_packet_radius: Fraction
    smallest_packet_radius: Fraction
    affine_integrality_margin: Fraction
    low_mode_l1: Fraction
    one_block_l1: Fraction
    selberg_output: Fraction


def critical_dyadic_packet_ledger() -> DyadicPacketExponentLedger:
    """Return the exact q-exponents at ``D=q^(16/33)``."""

    degree = Fraction(16, 33)
    low = 1 - 2 * degree
    top = 1 - degree
    largest_radius = (1 - low) / 2
    smallest_radius = (1 - top) / 2
    return DyadicPacketExponentLedger(
        degree=degree,
        low_frequency=low,
        top_frequency=top,
        largest_packet_radius=largest_radius,
        smallest_packet_radius=smallest_radius,
        affine_integrality_margin=1 - degree - largest_radius,
        low_mode_l1=low + 2 * degree,
        one_block_l1=Fraction(1),
        selberg_output=(degree - 1) + 1,
    )


def drpls_block_l1_bound(q: float, frequency: float) -> float:
    """Cauchy's exact numerical output from ``M(K)<=q^2/K``."""

    if q <= 0 or frequency <= 0:
        raise ValueError("q and frequency must be positive")
    return sqrt(frequency) * sqrt(q * q / frequency)


@dataclass(frozen=True)
class TowerEasySectorLedger:
    packet_radius: float
    maximum_block_size: float
    crude_packet_square_bound: float
    drpls_target: float
    remainder_threshold: float
    direction_threshold: float
    closes_by_remainder: bool
    closes_by_direction_size: bool


def tower_easy_sector_ledger(
    q: float,
    degree: float,
    frequency: float,
    determinant_step: float,
    direction_size: float,
) -> TowerEasySectorLedger:
    """Audit the trivial packet-square sector for one CF tower family.

    Ignoring harmless endpoint constants, a diameter-``R`` block has at
    most ``M=min(2D/|r|,R/||U||)`` points.  Since the total orbit size is
    ``O(D)``, its packet-square contribution is at most ``K(MD)^2``.  This
    is below ``q^2/K`` if ``M<=R^2/D``.  The two displayed threshold tests
    are sufficient ways this happens.
    """

    if min(q, degree, frequency, abs(determinant_step), direction_size) <= 0:
        raise ValueError("all scales and the two direction parameters must be nonzero")
    radius = sqrt(q / frequency)
    maximum_block = min(
        2 * degree / abs(determinant_step), radius / direction_size
    )
    crude = frequency * (maximum_block * degree) ** 2
    target = q * q / frequency
    remainder_threshold = 2 * degree * degree / (radius * radius)
    direction_threshold = degree / radius
    return TowerEasySectorLedger(
        packet_radius=radius,
        maximum_block_size=maximum_block,
        crude_packet_square_bound=crude,
        drpls_target=target,
        remainder_threshold=remainder_threshold,
        direction_threshold=direction_threshold,
        closes_by_remainder=abs(determinant_step) >= remainder_threshold,
        closes_by_direction_size=direction_size >= direction_threshold,
    )
