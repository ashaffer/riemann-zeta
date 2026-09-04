"""Integer-shell tangent family for fixed-color carry completions.

The family is an exact obstruction to a geometry-only ``D/|k|`` completion
bound.  It deliberately uses the full integer shell and an even formal
parameter ``q=2m``; it is not an actual-prime-power counterexample.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class TangentCompletion:
    parameter: int
    rows: tuple[int, int]
    columns: tuple[int, int]
    residuals: tuple[int, int, int, int]
    distinct_labels: int


@dataclass(frozen=True)
class FixedColorTangentFamily:
    m: int
    h: int
    q: int
    D: int
    colors: tuple[tuple[int, int], tuple[int, int]]
    color_determinant: int
    completions: tuple[TangentCompletion, ...]
    residual_cap: int

    @property
    def normalized_residual_cap(self) -> float:
        return self.residual_cap / (self.q * self.D)


def carry_residual(q: int, a: int, b: int, c: int) -> int:
    return 8 * a * b * c - q**3


def fixed_color_tangent_family(m: int, h: int) -> FixedColorTangentFamily:
    """Return the ``h-1``-point integer tangent orbit.

    Put ``D=h^2`` and ``q=2m``.  The fixed colors are

    ``[[m,m-2h],[m-h,m-3h]]``.

    For ``1<=s<h``, the carriers are

    ``a=(m+h+s,m+2h+s)``, ``b=(m-h-s,m+h-s)``.

    Their first-order deviations cancel at every corner, leaving residuals
    of size ``O(m h^2)``.  All eight displayed labels are distinct.
    """

    if h < 2:
        raise ValueError("h must be at least two")
    if m <= 20 * h:
        raise ValueError("m must be larger than the tangent offsets")
    q = 2 * m
    D = h * h
    colors = ((m, m - 2 * h), (m - h, m - 3 * h))
    determinant = colors[0][0] * colors[1][1] - colors[0][1] * colors[1][0]
    completions: list[TangentCompletion] = []
    cap = 0
    for s in range(1, h):
        rows = (m + h + s, m + 2 * h + s)
        columns = (m - h - s, m + h - s)
        c11, c12 = colors[0]
        c21, c22 = colors[1]
        residuals = (
            carry_residual(q, rows[0], columns[0], c11),
            carry_residual(q, rows[0], columns[1], c12),
            carry_residual(q, rows[1], columns[0], c21),
            carry_residual(q, rows[1], columns[1], c22),
        )
        labels = (*rows, *columns, c11, c12, c21, c22)
        cap = max(cap, *(abs(value) for value in residuals))
        completions.append(
            TangentCompletion(
                parameter=s,
                rows=rows,
                columns=columns,
                residuals=residuals,
                distinct_labels=len(set(labels)),
            )
        )
    family = FixedColorTangentFamily(
        m=m,
        h=h,
        q=q,
        D=D,
        colors=colors,
        color_determinant=determinant,
        completions=tuple(completions),
        residual_cap=cap,
    )
    if determinant != -2 * D:
        raise AssertionError("the fixed color determinant is not -2D")
    if any(item.distinct_labels != 8 for item in completions):
        raise AssertionError("a tangent completion has a repeated label")
    # The elementary expansion in the report gives a uniform constant 80
    # once m>20h; retain a fail-closed exact check here.
    if cap > 80 * q * D:
        raise AssertionError("the tangent residual escaped its O(qD) window")
    return family


def local_first_carrier_bound(interval_length: int) -> int:
    """Maximum completions once ``a1`` is confined to an integer interval.

    In a pair-unique carry window, fixing ``a1`` and the four colors fixes
    ``b1``, then ``a2`` and ``b2``.  Thus an interval containing at most
    ``interval_length+1`` integers contains at most that many completions.
    This records the rigorous local ``sqrt(D)`` mechanism, not a global
    clustering theorem.
    """

    if interval_length < 0:
        raise ValueError("interval length must be nonnegative")
    return interval_length + 1


def _ceiling_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def near_square_first_carrier_bound(
    residual_cap: int,
    color_lower_bound: int,
    carrier_lower_bound: int,
    carrier_diameter: int,
) -> int:
    """Exact coarse count for a near-square corner's first carrier.

    If ``|8abc-Q|<=residual_cap`` and ``|a-b|<=R``, put
    ``X=Q/(8c)`` and ``u=(a+b)/2``.  Then

    ``|u^2-X| <= residual_cap/(8c)+R^2/4``.

    Since ``u`` is at least the carrier lower bound, both ``a`` and ``b``
    lie in an interval of length at most

    ``R+2*(residual_cap/(8c)+R^2/4)/carrier_lower_bound``

    around ``sqrt(X)``.  This routine returns the resulting integer count,
    using only lower bounds for ``b`` and ``c``.
    """

    if min(
        residual_cap,
        color_lower_bound,
        carrier_lower_bound,
        carrier_diameter,
    ) < 0:
        raise ValueError("bounds must be nonnegative")
    if color_lower_bound == 0 or carrier_lower_bound == 0:
        raise ValueError("shell lower bounds must be positive")
    radius_error = Fraction(residual_cap, 8 * color_lower_bound) + Fraction(
        carrier_diameter**2, 4
    )
    length = Fraction(carrier_diameter, 1) + 2 * radius_error / carrier_lower_bound
    return _ceiling_fraction(length) + 1


def near_square_projection_fiber_bound(
    residual_cap: int,
    color_lower_bound: int,
    carrier_lower_bound: int,
    carrier_diameter: int,
) -> int:
    """Fiber envelope for either horizontal color-pair projection.

    Once the near-square corner's first carrier is selected, pair uniqueness
    fixes both carriers in that row.  The second-row carrier has at most
    ``2R+1`` integer choices, after which pair uniqueness fixes both remaining
    colors.  The same bound holds for the bottom color-pair projection.
    """

    first = near_square_first_carrier_bound(
        residual_cap,
        color_lower_bound,
        carrier_lower_bound,
        carrier_diameter,
    )
    return first * (2 * carrier_diameter + 1)


def anisotropic_tangent_projection_bound(
    residual_cap: int,
    color_lower_bound: int,
    carrier_lower_bound: int,
    cross_gap: int,
    adjacent_gap: int,
) -> int:
    """Maximum of the two color-pair fiber envelopes in Theorem 3.2.

    The forward corner has cross-gap ``R``.  At the reverse corner the
    triangle inequality gives cross-gap ``R+T``.  Each projection then has
    at most the near-square first-corner count times ``2T+1`` choices.
    """

    if adjacent_gap > cross_gap:
        raise ValueError("the anisotropic theorem requires T<=R")
    forward = near_square_first_carrier_bound(
        residual_cap, color_lower_bound, carrier_lower_bound, cross_gap
    )
    reverse = near_square_first_carrier_bound(
        residual_cap,
        color_lower_bound,
        carrier_lower_bound,
        cross_gap + adjacent_gap,
    )
    return max(forward, reverse) * (2 * adjacent_gap + 1)
