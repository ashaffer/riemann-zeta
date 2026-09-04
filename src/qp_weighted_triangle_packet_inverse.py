"""Exact tangent obstruction and the packet-safe unconditionality target.

The residual matching decomposition gives a sharp Rademacher fourth moment,
but a direct comparison with the all-plus operator cannot hold in the
full-integer product-window model.  This module records the elementary
Hankel fixture witnessing the loss, using exact rational arithmetic.

The fixture is deliberately a *method obstruction*: its nodes are integers,
not necessarily prime powers.  It identifies the coherent component that an
actual-mask inverse theorem has to extract before applying square-function
unconditionality to the remainder.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class TangentUnconditionalityLedger:
    """Exact fourth moments for the flat ``L x L`` tangent packet."""

    order: int
    center: int
    q: int
    degree_parameter: int
    color_count: int
    all_plus_fourth: Fraction
    rademacher_fourth: Fraction
    unconditionality_ratio: Fraction
    maximum_residual: int
    product_window_holds: bool
    labels_are_proper: bool
    alternating_label_rectangles: int


def _quadratic_label(order: int, row: int, column: int) -> int:
    """The exact width-``q`` residual label once the center is large.

    With ``y=2L+j`` and

    ``F(i,y)=i^2+i*y+y^2``, ``r/q=-4F-4*i*y*(i+y)/m``.

    The center assumption in :func:`tangent_unconditionality_ledger` makes
    the second term lie in ``(-1,0]``.  Thus ``floor(r/q)`` is the value
    returned here.
    """

    y = 2 * order + column
    form = row * row + row * y + y * y
    return -4 * form - int(row > 0)


def tangent_unconditionality_ledger(
    order: int, center: int | None = None
) -> TangentUnconditionalityLedger:
    r"""Certify the polynomial gap between all-plus and random block signs.

    Put

    ``a_i=m+i``, ``b_j=m+2L+j``, ``c_ij=m-2L-i-j``, ``q=2m``.

    Give the ``2L-1`` color nodes the flat coefficient
    ``(2L-1)^(-1/2)`` and every other node coefficient zero.  The carry
    matrix is the symmetric dilation of the constant ``L x L`` Hankel
    matrix.  Consequently

    ``||A||_S4^4 = 2 L^4/(2L-1)^2``.

    Width-``q`` residual labels form a proper matrix coloring with no
    alternating two-label rectangle.  Rademacher averaging therefore leaves
    only row/column backtracking and equals ``2 L^2/(2L-1)``.  Their ratio is
    ``L^2/(2L-1) ~ L/2 ~ sqrt(D)``.
    """

    length = int(order)
    if length < 2:
        raise ValueError("order must be at least two")
    # This makes 0 < 4*i*y*(i+y)/m < 1 for every i>0 in the packet.
    minimum_center = 64 * length**3
    midpoint = minimum_center + 1 if center is None else int(center)
    if midpoint <= minimum_center:
        raise ValueError("center must exceed 64*order^3")

    q = 2 * midpoint
    degree = 100 * length * length
    target = q**3
    maximum_residual = 0
    labels: dict[tuple[int, int], int] = {}
    for i in range(length):
        for j in range(length):
            a = midpoint + i
            b = midpoint + 2 * length + j
            c = midpoint - 2 * length - i - j
            residual = 8 * a * b * c - target
            maximum_residual = max(maximum_residual, abs(residual))
            exact_label = residual // q
            predicted_label = _quadratic_label(length, i, j)
            if exact_label != predicted_label:
                raise AssertionError("the exact residual label formula failed")
            labels[i, j] = exact_label

    proper = True
    for i in range(length):
        proper &= len({labels[i, j] for j in range(length)}) == length
    for j in range(length):
        proper &= len({labels[i, j] for i in range(length)}) == length

    alternating = 0
    for i in range(length):
        for ip in range(i + 1, length):
            for j in range(length):
                for jp in range(j + 1, length):
                    if (
                        labels[i, j] == labels[ip, jp]
                        and labels[ip, j] == labels[i, jp]
                    ) or (
                        labels[i, j] == labels[ip, j]
                        and labels[i, jp] == labels[ip, jp]
                    ):
                        alternating += 1

    colors = 2 * length - 1
    all_plus = Fraction(2 * length**4, colors**2)
    randomized = Fraction(2 * length**2, colors)
    return TangentUnconditionalityLedger(
        order=length,
        center=midpoint,
        q=q,
        degree_parameter=degree,
        color_count=colors,
        all_plus_fourth=all_plus,
        rademacher_fourth=randomized,
        unconditionality_ratio=all_plus / randomized,
        maximum_residual=maximum_residual,
        product_window_holds=maximum_residual <= q * degree,
        labels_are_proper=proper,
        alternating_label_rectangles=alternating,
    )


def packet_safe_inverse_target() -> str:
    """Return the precise logical replacement for raw unconditionality."""

    return (
        "extract affine/Hankel packets with a Carleson packing bound; "
        "prove residual-block S4 unconditionality only on the remainder"
    )
