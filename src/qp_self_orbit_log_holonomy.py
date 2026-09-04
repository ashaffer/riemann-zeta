"""Log-phase holonomy for the rounded symmetric self-orbit kernel.

For an oriented hard edge ``i -> j`` with carrier ``x``, put

    w_ij = x * det(v_i, v_j),
    F_i  = (q**3 / 8) * log(b_i / B_i).

The two cubic windows make ``w_ij`` an integer approximation to
``F_i-F_j`` with error ``O(D**2/q)``.  This module records the exact integer
identities and rational error ceilings used by the accompanying report.  It
does not claim the total-edge theorem or the sharp four-cycle bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence


Pair = tuple[int, int]


def det(left: Pair, right: Pair) -> int:
    """Return the oriented two-dimensional determinant."""

    return left[0] * right[1] - left[1] * right[0]


def phase_remainder_rational_ceiling(q: int, D: int) -> Fraction:
    r"""Return ``D^2/[16q(1-D/q^2)]`` exactly.

    If ``|u|,|v|<=a=D/q^2`` and ``phi(s)=log(1+s)-s``, then

    ``|phi(u)-phi(v)| <= -log(1-a)-a <= a^2/(2(1-a))``.

    Multiplication by ``q^3/8`` gives the returned ceiling.  The factor 16
    uses the range of ``phi`` on ``[-a,a]``; applying the triangle inequality
    to two separate Taylor remainders would unnecessarily lose a factor two.
    """

    q, D = int(q), int(D)
    if q <= 0 or D < 0 or D >= q * q:
        raise ValueError("require q>0 and 0<=D<q^2")
    return Fraction(D * D * q, 16 * (q * q - D))


def guaranteed_zero_cycle_length(q: int, D: int) -> int:
    """Largest length forced flat by the uniform rational phase ceiling."""

    ceiling = phase_remainder_rational_ceiling(q, D)
    if not ceiling:
        return 10**18
    return (ceiling.denominator - 1) // ceiling.numerator


@dataclass(frozen=True)
class HardEdgePhaseLedger:
    q: int
    D: int
    first: Pair
    second: Pair
    row: int
    first_residual: int
    second_residual: int
    determinant: int
    integer_cocycle: int
    phase_remainder_ceiling: Fraction


def hard_edge_phase_ledger(
    q: int, D: int, first: Pair, second: Pair, row: int
) -> HardEdgePhaseLedger:
    """Verify one literal hard edge and its exact determinant cocycle.

    The residual difference identity is

    ``(8*x*b_i*B_j-q^3)-(8*x*B_i*b_j-q^3)=8*w_ij``.

    Together with the analytic range estimate documented in
    :func:`phase_remainder_rational_ceiling`, this proves

    ``|(F_i-F_j)-w_ij| <= phase_remainder_ceiling``.
    """

    b_i, B_i = map(int, first)
    b_j, B_j = map(int, second)
    q, D, row = int(q), int(D), int(row)
    residual_a = 8 * row * b_i * B_j - q**3
    residual_b = 8 * row * B_i * b_j - q**3
    if max(abs(residual_a), abs(residual_b)) > q * D:
        raise ValueError("the supplied transition is not a hard edge")
    kappa = det((b_i, B_i), (b_j, B_j))
    cocycle = row * kappa
    if residual_a - residual_b != 8 * cocycle:
        raise AssertionError("the edge residual/cocycle identity failed")
    return HardEdgePhaseLedger(
        q=q,
        D=D,
        first=(b_i, B_i),
        second=(b_j, B_j),
        row=row,
        first_residual=residual_a,
        second_residual=residual_b,
        determinant=kappa,
        integer_cocycle=cocycle,
        phase_remainder_ceiling=phase_remainder_rational_ceiling(q, D),
    )


@dataclass(frozen=True)
class CycleHolonomyLedger:
    q: int
    D: int
    vertices: tuple[Pair, ...]
    rows: tuple[int, ...]
    edge_cocycles: tuple[int, ...]
    circulation: int
    phase_remainder_ceiling: Fraction
    forced_zero_by_phase_bound: bool


def cycle_holonomy_ledger(
    q: int, D: int, vertices: Sequence[Pair], rows: Sequence[int]
) -> CycleHolonomyLedger:
    """Audit an oriented hard cycle and apply the subunit phase theorem."""

    points = tuple((int(point[0]), int(point[1])) for point in vertices)
    carriers = tuple(map(int, rows))
    if len(points) < 3 or len(points) != len(carriers):
        raise ValueError("a cycle needs equally many vertices and edge rows")
    edges = tuple(
        hard_edge_phase_ledger(
            q, D, points[index], points[(index + 1) % len(points)], carriers[index]
        )
        for index in range(len(points))
    )
    cocycles = tuple(edge.integer_cocycle for edge in edges)
    circulation = sum(cocycles)
    ceiling = phase_remainder_rational_ceiling(q, D)
    forced = len(points) * ceiling < 1
    if forced and circulation:
        raise AssertionError("subunit log-phase circulation was a nonzero integer")
    return CycleHolonomyLedger(
        q=int(q),
        D=int(D),
        vertices=points,
        rows=carriers,
        edge_cocycles=cocycles,
        circulation=circulation,
        phase_remainder_ceiling=ceiling,
        forced_zero_by_phase_bound=forced,
    )


@dataclass(frozen=True)
class TriangleRowSpanLedger:
    cycle: CycleHolonomyLedger
    determinants: tuple[int, int, int]
    affine_area: int
    row_span: int
    median_row: int
    maximum_determinant: int
    area_left_side: int
    row_span_right_side: int
    forced_collinear_by_row_span: bool
    opposite_row_functional: tuple[Fraction, Fraction]


def triangle_row_span_ledger(
    q: int, D: int, vertices: Sequence[Pair], rows: Sequence[int]
) -> TriangleRowSpanLedger:
    r"""Verify the exact zero-holonomy triangle/row-span dichotomy.

    Rows are ordered as ``(x_12,x_23,x_31)``.  If their circulation is zero,
    then

    ``det(v_2-v_1,v_3-v_1)=kappa_12+kappa_23+kappa_31``

    and choosing the median carrier ``x_*`` gives

    ``x_* |area| <= (max x-min x) max|kappa|``.

    Thus a row span whose right side is strictly smaller than ``x_*`` forces
    the integral affine area to vanish.  Zero holonomy is also exactly the
    vanishing of the determinant with rows

    ``(b_1,B_1,x_23),(b_2,B_2,x_31),(b_3,B_3,x_12)``;

    the returned rational functional ``L`` satisfies
    ``(x_23,x_31,x_12)=(L(v_1),L(v_2),L(v_3))``.
    """

    if len(vertices) != 3 or len(rows) != 3:
        raise ValueError("exactly three vertices and three rows are required")
    cycle = cycle_holonomy_ledger(q, D, vertices, rows)
    if cycle.circulation:
        raise ValueError("the triangle does not have zero determinant holonomy")
    v1, v2, v3 = cycle.vertices
    kappas = (det(v1, v2), det(v2, v3), det(v3, v1))
    area = det(
        (v2[0] - v1[0], v2[1] - v1[1]),
        (v3[0] - v1[0], v3[1] - v1[1]),
    )
    if area != sum(kappas):
        raise AssertionError("the triangle affine-area identity failed")
    median = sorted(cycle.rows)[1]
    span = max(cycle.rows) - min(cycle.rows)
    maximum_kappa = max(map(abs, kappas))
    left_side = median * abs(area)
    right_side = span * maximum_kappa
    if left_side > right_side:
        raise AssertionError("the median-row affine-area inequality failed")
    forced_collinear = right_side < median
    if forced_collinear and area:
        raise AssertionError("a subunit integral affine area did not vanish")

    # Opposite rows at v1,v2,v3 are x23,x31,x12 respectively.
    opposite = (cycle.rows[1], cycle.rows[2], cycle.rows[0])
    denominator = det(v1, v2)
    if not denominator:
        raise ValueError("the first two triangle directions must be nonparallel")
    alpha = Fraction(opposite[0] * v2[1] - v1[1] * opposite[1], denominator)
    beta = Fraction(v1[0] * opposite[1] - opposite[0] * v2[0], denominator)
    if tuple(alpha * b + beta * B for b, B in cycle.vertices) != opposite:
        raise AssertionError("the opposite-edge row functional failed")

    return TriangleRowSpanLedger(
        cycle=cycle,
        determinants=kappas,
        affine_area=area,
        row_span=span,
        median_row=median,
        maximum_determinant=maximum_kappa,
        area_left_side=left_side,
        row_span_right_side=right_side,
        forced_collinear_by_row_span=forced_collinear,
        opposite_row_functional=(alpha, beta),
    )


def hostile_nonreturn_triangle() -> TriangleRowSpanLedger:
    """Return the critical full-integer row-separated escape triangle."""

    return triangle_row_span_ledger(
        100_000,
        265,
        ((50_008, 50_001), (50_002, 49_995), (42_858, 42_852)),
        (49_997, 58_338, 58_331),
    )
