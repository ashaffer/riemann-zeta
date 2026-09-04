"""Dynamic affine packets inside one short Bezout self-orbit.

The Fourier scale ``K`` naturally sees physical differences of radius
``R=sqrt(q/K)``.  This module records an exact feature special to the
self-orbit: when ``D*R=o(q)``, every connected ``R``-cluster is one affine
line, and its primitive direction is a continued-fraction convergent of the
anchor slope.

These statements retain arbitrary subsets of the orbit, including the
actual prime-power mask.  They do not prove orthogonality between different
parallel translates and therefore do not prove the dyadic reciprocal large
sieve.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Mapping, Sequence


Pair = tuple[int, int]


def det(left: Pair, right: Pair) -> int:
    return left[0] * right[1] - left[1] * right[0]


def primitive_direction(first: Pair, second: Pair) -> Pair:
    """Return the primitive direction, oriented to have positive second entry."""

    dx, dy = second[0] - first[0], second[1] - first[1]
    content = gcd(abs(dx), abs(dy))
    if not content:
        raise ValueError("two distinct points are required")
    dx, dy = dx // content, dy // content
    if dy < 0 or (dy == 0 and dx < 0):
        dx, dy = -dx, -dy
    return dx, dy


def rational_convergents(numerator: int, denominator: int) -> tuple[Fraction, ...]:
    """Return all principal continued-fraction convergents of ``n/d``."""

    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError("the rational slope must be positive")
    a_values: list[int] = []
    n, d = numerator, denominator
    while d:
        a_values.append(n // d)
        n, d = d, n % d
    p_before, p_previous = 0, 1
    q_before, q_previous = 1, 0
    answer: list[Fraction] = []
    for a in a_values:
        p = a * p_previous + p_before
        q = a * q_previous + q_before
        answer.append(Fraction(p, q))
        p_before, p_previous = p_previous, p
        q_before, q_previous = q_previous, q
    return tuple(answer)


@dataclass(frozen=True)
class OrbitAreaLedger:
    anchor: Pair
    labels: tuple[int, int, int]
    points: tuple[Pair, Pair, Pair]
    affine_area: int
    scaled_area: int
    label_coordinate_expression: int


def orbit_area_ledger(
    anchor: Pair,
    labels: Sequence[int],
    points: Sequence[Pair],
) -> OrbitAreaLedger:
    r"""Verify the exact self-orbit affine-area identity.

    For ``t_i=c*b_i-C*B_i`` one has

    ``C det(v2-v1,v3-v1)
       =(t2-t1)(b3-b1)-(b2-b1)(t3-t1)``.
    """

    if len(labels) != 3 or len(points) != 3:
        raise ValueError("exactly three labelled points are required")
    c, C = map(int, anchor)
    ts = tuple(map(int, labels))
    vs = tuple((int(point[0]), int(point[1])) for point in points)
    for t, (b, B) in zip(ts, vs, strict=True):
        if c * b - C * B != t:
            raise ValueError("a point has the wrong self-orbit label")
    v1, v2, v3 = vs
    t1, t2, t3 = ts
    area = det(
        (v2[0] - v1[0], v2[1] - v1[1]),
        (v3[0] - v1[0], v3[1] - v1[1]),
    )
    expression = (t2 - t1) * (v3[0] - v1[0]) - (
        v2[0] - v1[0]
    ) * (t3 - t1)
    if C * area != expression:
        raise AssertionError("the orbit affine-area identity failed")
    return OrbitAreaLedger(
        anchor=(c, C),
        labels=(t1, t2, t3),
        points=(v1, v2, v3),
        affine_area=area,
        scaled_area=C * area,
        label_coordinate_expression=expression,
    )


@dataclass(frozen=True)
class DynamicAffineComponent:
    labels: tuple[int, ...]
    points: tuple[Pair, ...]
    direction: Pair | None
    anchor_determinant_step: int | None
    direction_is_principal_convergent: bool
    label_capacity: int | None


@dataclass(frozen=True)
class DynamicPacketDecomposition:
    anchor: Pair
    D: int
    radius: int
    point_count: int
    component_count: int
    nontrivial_component_count: int
    distinct_nontrivial_directions: tuple[Pair, ...]
    convergent_count: int
    components: tuple[DynamicAffineComponent, ...]


def dynamic_packet_decomposition(
    anchor: Pair,
    D: int,
    radius: int,
    labelled_points: Mapping[int, Pair],
) -> DynamicPacketDecomposition:
    r"""Decompose the radius graph into exact affine CF packets.

    Two points are adjacent when their sup-norm distance is at most ``R``.
    A two-edge path has first-coordinate diameter at most ``2R``.  The area
    identity then gives ``|C*area|<=8DR``.  The strict hypothesis below makes
    every such triple collinear, so collinearity propagates through an entire
    connected component.

    If ``g(p,P)`` is a close difference in primitive direction ``(p,P)``,
    then ``g(cp-CP)`` is its label difference.  Under ``4DR<c`` Legendre's
    criterion makes ``p/P`` a principal convergent of ``C/c``.  The stronger
    component hypothesis ``8DR<min(c,C)`` implies both estimates.
    """

    c, C = map(int, anchor)
    D, radius = int(D), int(radius)
    if D < 0 or radius <= 0 or 8 * D * radius >= min(c, C):
        raise ValueError("require 8*D*radius < min(anchor)")
    points = {int(t): (int(v[0]), int(v[1])) for t, v in labelled_points.items()}
    for t, (b, B) in points.items():
        if abs(t) > D or c * b - C * B != t:
            raise ValueError("the input is not contained in the short self-orbit")

    labels = tuple(sorted(points))
    adjacency: dict[int, list[int]] = {t: [] for t in labels}
    for index, t in enumerate(labels):
        v = points[t]
        for s in labels[:index]:
            w = points[s]
            if max(abs(v[0] - w[0]), abs(v[1] - w[1])) <= radius:
                adjacency[t].append(s)
                adjacency[s].append(t)

    convergents = frozenset(rational_convergents(C, c))
    seen: set[int] = set()
    components: list[DynamicAffineComponent] = []
    directions: set[Pair] = set()
    for root in labels:
        if root in seen:
            continue
        stack = [root]
        seen.add(root)
        component_labels: list[int] = []
        while stack:
            t = stack.pop()
            component_labels.append(t)
            for neighbour in adjacency[t]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        component_labels.sort(key=lambda t: points[t])
        component_points = tuple(points[t] for t in component_labels)
        if len(component_points) == 1:
            component = DynamicAffineComponent(
                labels=tuple(component_labels),
                points=component_points,
                direction=None,
                anchor_determinant_step=None,
                direction_is_principal_convergent=False,
                label_capacity=None,
            )
            components.append(component)
            continue

        direction = primitive_direction(component_points[0], component_points[1])
        p, P = direction
        if P == 0:
            raise AssertionError("a short self-orbit component became horizontal")
        for point in component_points[2:]:
            if det(
                (
                    component_points[1][0] - component_points[0][0],
                    component_points[1][1] - component_points[0][1],
                ),
                (
                    point[0] - component_points[0][0],
                    point[1] - component_points[0][1],
                ),
            ):
                raise AssertionError("a dynamic component was not affine-collinear")
        determinant_step = c * p - C * P
        if not determinant_step:
            raise AssertionError("a short component was parallel to the anchor ray")
        slope = Fraction(p, P)
        is_convergent = slope in convergents
        if not is_convergent:
            raise AssertionError("a short direction failed Legendre's criterion")
        capacity = 1 + (2 * D) // abs(determinant_step)
        if len(component_points) > capacity:
            raise AssertionError("the label-step packet capacity failed")
        directions.add(direction)
        components.append(
            DynamicAffineComponent(
                labels=tuple(component_labels),
                points=component_points,
                direction=direction,
                anchor_determinant_step=determinant_step,
                direction_is_principal_convergent=True,
                label_capacity=capacity,
            )
        )

    components.sort(key=lambda component: component.points[0])
    return DynamicPacketDecomposition(
        anchor=(c, C),
        D=D,
        radius=radius,
        point_count=len(points),
        component_count=len(components),
        nontrivial_component_count=sum(
            component.direction is not None for component in components
        ),
        distinct_nontrivial_directions=tuple(sorted(directions)),
        convergent_count=len(convergents),
        components=tuple(components),
    )


@dataclass(frozen=True)
class ReciprocalLaneHessian:
    q: int
    first_coordinate: int
    second_coordinate: int
    first_step: int
    second_step: int
    phase: Fraction
    first_derivative: Fraction
    second_derivative: Fraction
    first_pure_second_derivative: Fraction
    second_pure_second_derivative: Fraction
    mixed_second_derivative: Fraction
    hessian_determinant: Fraction


def reciprocal_lane_hessian(
    q: int,
    first_coordinate: int,
    second_coordinate: int,
    first_step: int,
    second_step: int,
) -> ReciprocalLaneHessian:
    r"""Return exact derivatives of ``Q/[(b+pr)(B+Ps)]`` at the origin."""

    q = int(q)
    b, B = int(first_coordinate), int(second_coordinate)
    p, P = int(first_step), int(second_step)
    if min(q, b, B) <= 0 or not p or not P:
        raise ValueError("positive coordinates and nonzero lane steps are required")
    Q = Fraction(q**3, 8)
    phase = Q / (b * B)
    d_r = -Q * p / (b * b * B)
    d_s = -Q * P / (b * B * B)
    d_rr = 2 * Q * p * p / (b**3 * B)
    d_ss = 2 * Q * P * P / (b * B**3)
    d_rs = Q * p * P / (b * b * B * B)
    determinant = d_rr * d_ss - d_rs * d_rs
    expected = 3 * Q * Q * p * p * P * P / (b**4 * B**4)
    if determinant != expected:
        raise AssertionError("the reciprocal phase Hessian determinant failed")
    return ReciprocalLaneHessian(
        q=q,
        first_coordinate=b,
        second_coordinate=B,
        first_step=p,
        second_step=P,
        phase=phase,
        first_derivative=d_r,
        second_derivative=d_s,
        first_pure_second_derivative=d_rr,
        second_pure_second_derivative=d_ss,
        mixed_second_derivative=d_rs,
        hessian_determinant=determinant,
    )
