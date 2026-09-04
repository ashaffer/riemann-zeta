"""Exact audit ledgers for the exceptional parabolic four-cycle sector.

The routines in this module do not assert the full four-cycle estimate.  They
record two exact checks used in the hostile audit:

* an actual-prime color matrix can obey a short *scaled* additive relation
  without being an ordinary additive rectangle;
* the scalar high/low chart argument balances at ``D**(11/8)``.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import log


Colors = tuple[int, int, int, int]
Pair = tuple[int, int]


def is_prime(value: int) -> bool:
    """Return primality by deterministic trial division (fixture-sized input)."""

    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


@dataclass(frozen=True)
class ActualPrimeScaledRelationLedger:
    q: int
    colors: Colors
    all_colors_prime: bool
    shell_log_radius: float
    weighted_relation_defect: int
    raw_additive_defect: int
    color_determinant: int


def actual_prime_scaled_relation_ledger(
    q: int,
    colors: Colors,
    row_direction: Pair,
    column_direction: Pair,
) -> ActualPrimeScaledRelationLedger:
    """Audit one weighted-additive relation on actual prime colors.

    The signed relation is

    ``r1*s1*c11-r1*s2*c12-r2*s1*c21+r2*s2*c22=0``.

    A zero value does not assert that the colors have carrier completions; it
    only checks the exact color-side obstruction to an equal-slope reduction.
    """

    if q <= 2 or q % 2 == 0:
        raise ValueError("q must be an odd integer greater than two")
    c11, c12, c21, c22 = colors
    r1, r2 = row_direction
    s1, s2 = column_direction
    if 0 in (r1, r2, s1, s2):
        raise ValueError("all direction coordinates must be nonzero")
    center = q / 2
    return ActualPrimeScaledRelationLedger(
        q=q,
        colors=colors,
        all_colors_prime=all(is_prime(color) for color in colors),
        shell_log_radius=max(abs(log(color / center)) for color in colors),
        weighted_relation_defect=(
            r1 * s1 * c11
            - r1 * s2 * c12
            - r2 * s1 * c21
            + r2 * s2 * c22
        ),
        raw_additive_defect=c11 + c22 - c12 - c21,
        color_determinant=c11 * c22 - c12 * c21,
    )


@dataclass(frozen=True)
class ParabolicScalarBarrierLedger:
    split_threshold: Fraction
    relation_height_cutoff: Fraction
    direction_count: Fraction
    fixed_relation_color_mass: Fraction
    chart_length: Fraction
    low_trace: Fraction
    high_trace: Fraction


def parabolic_scalar_barrier_ledger() -> ParabolicScalarBarrierLedger:
    """Return the critical powers in the proved scalar chart argument.

    Exponents are powers of ``D``.  At chart threshold ``M=D**(3/8)``,
    primitive relation height is at most ``D**(1/4)``.  There can be
    ``D**(1/2+o(1))`` such directions, each carrying ``D**(1/2)`` color
    mass and ``D**(3/8)`` completions.  Their product is ``D**(11/8)``.
    """

    threshold = Fraction(3, 8)
    height = 1 - 2 * threshold
    direction_count = 2 * height
    color_mass = Fraction(1, 2)
    chart_length = (1 - height) / 2
    low_trace = 1 + threshold
    high_trace = direction_count + color_mass + chart_length
    return ParabolicScalarBarrierLedger(
        split_threshold=threshold,
        relation_height_cutoff=height,
        direction_count=direction_count,
        fixed_relation_color_mass=color_mass,
        chart_length=chart_length,
        low_trace=low_trace,
        high_trace=high_trace,
    )
