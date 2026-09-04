"""First-gap cutoffs for the QP parabolic four-cycle sector.

The accompanying report proves that two occupied points on one maximal
parabolic carrier line satisfy two additional first-difference bounds.  The
small routines below keep the exact exponent ledger and replay the integer
identities used in that proof.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class FirstGapReplay:
    """The two exact color-gap increments along one carrier line."""

    top_gap_at_zero: int
    top_gap_at_h: int
    top_gap_increment: int
    expected_top_increment: int
    left_gap_at_zero: int
    left_gap_at_h: int
    left_gap_increment: int
    expected_left_increment: int

    @property
    def identities_hold(self) -> bool:
        return (
            self.top_gap_increment == self.expected_top_increment
            and self.left_gap_increment == self.expected_left_increment
        )


def replay_first_gap_identities(
    *,
    x: int,
    y: int,
    zeta: int,
    a1: int,
    a2: int,
    b1: int,
    b2: int,
    r1: int,
    r2: int,
    s1: int,
    s2: int,
    row_multiplier: int,
    column_multiplier: int,
    separation: int,
) -> FirstGapReplay:
    """Replay the literal first-gap identities.

    The second completion is

    ``a' = a + h*A*r`` and ``b' = b + h*B*s``.

    No product-window approximation is used in this routine; it checks the
    integer algebra before the analytic ``O(D)`` bounds are applied.
    """

    h = separation
    A = row_multiplier
    B = column_multiplier
    a1h = a1 + h * A * r1
    a2h = a2 + h * A * r2
    b1h = b1 + h * B * s1
    b2h = b2 + h * B * s2

    top0 = x * b1 - y * b2
    toph = x * b1h - y * b2h
    left0 = x * a1 - zeta * a2
    lefth = x * a1h - zeta * a2h
    return FirstGapReplay(
        top_gap_at_zero=top0,
        top_gap_at_h=toph,
        top_gap_increment=toph - top0,
        expected_top_increment=h * B * (s1 * x - s2 * y),
        left_gap_at_zero=left0,
        left_gap_at_h=lefth,
        left_gap_increment=lefth - left0,
        expected_left_increment=h * A * (r1 * x - r2 * zeta),
    )


@dataclass(frozen=True)
class CurvatureEndpoint:
    """Exact high-slice optimizer of the first-gap exponent program."""

    eta_height: Fraction
    theta_height: Fraction
    row_height: Fraction
    column_height: Fraction
    gcd_height: Fraction
    row_multiplier_height: Fraction
    column_multiplier_height: Fraction
    occupied_line_height: Fraction
    extra_length_height: Fraction
    relation_mass: Fraction

    @property
    def curvature_exponent(self) -> Fraction:
        return (
            self.relation_mass
            + self.occupied_line_height
            + self.extra_length_height
        )


def first_gap_curvature_endpoint() -> CurvatureEndpoint:
    """Return the equality point giving ``71/64``."""

    return CurvatureEndpoint(
        eta_height=Fraction(1, 2),
        theta_height=Fraction(1, 2),
        row_height=Fraction(25, 64),
        column_height=Fraction(25, 64),
        gcd_height=Fraction(0),
        row_multiplier_height=Fraction(7, 64),
        column_multiplier_height=Fraction(7, 64),
        occupied_line_height=Fraction(7, 32),
        extra_length_height=Fraction(0),
        relation_mass=Fraction(57, 64),
    )


def curvature_dual_rhs() -> Fraction:
    """Return the exact RHS of the high-slice LP dual certificate.

    In the branch ``p=e+2r-g`` and ``kappa=p-17/16``, combine

    * half of ``e+t <= 1``;
    * three quarters of ``j <= a+b``;
    * one quarter of ``j <= e+2r-g-17/16``;
    * half of each one-sided relation-mass bound;
    * five eighths of ``2 ell+a+b+r+s <= 1``; and
    * one quarter of ``ell+b+e+r <= 1``.

    Using ``b-a=r-s``, the left side is
    ``w+j+3 ell/2+5g/4``.  Nonnegativity then bounds the desired
    ``w+j+ell`` by the value returned here.  The opposite branch is the
    transpose.
    """

    return (
        Fraction(1, 2)
        - Fraction(17, 64)
        + Fraction(5, 8)
        + Fraction(1, 4)
    )


def global_trace_exponent() -> Fraction:
    """The new complete trace exponent after sector synthesis."""

    curvature = curvature_dual_rhs()
    broad_and_singleton = Fraction(9, 8)
    return max(curvature, broad_and_singleton)


def carry_operator_exponent() -> Fraction:
    """Fourth root of the global fourth-trace exponent."""

    return global_trace_exponent() / 4


def transferred_transverse_exponent() -> Fraction:
    """Exponent after the established ``D=q^(16/33)`` transfer."""

    return Fraction(1, 2) + carry_operator_exponent() * Fraction(16, 33)

