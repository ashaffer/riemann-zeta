"""Exact arithmetic for the fixed-level and two-anchor QP identities."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class CompletionInvariant:
    e: int
    f: int
    ell: int
    level: int
    level_identity_error: int
    second_ell: int
    gap_identity_error: int


@dataclass(frozen=True)
class PairResultant:
    row_determinant: int
    carrier_determinant: int
    forward_mixed_level: int
    reverse_mixed_level: int
    identity_error: int


@dataclass(frozen=True)
class PartnerLevelSpacing:
    """Exact rational spacing data for two color-only level centers."""

    first_center: Fraction
    second_center: Fraction
    partner_determinant: int
    spacing_identity_error: Fraction
    first_rounded_level: int
    second_rounded_level: int


def completion_invariant(
    anchor: tuple[int, int],
    partner: tuple[int, int],
    row: tuple[int, int],
    carriers: tuple[int, int],
) -> CompletionInvariant:
    """Return ``e,f,ell,L`` and check ``cL=ABk-e ell`` exactly."""

    c, d = anchor
    cp, dp = partner
    a, capital_a = row
    b, capital_b = carriers
    k = c * dp - cp * d
    e = a * c - capital_a * d
    f = a * cp - capital_a * dp
    ell = cp * capital_b - c * b
    second_ell = dp * capital_b - d * b
    level = b * e - capital_b * f
    error = c * level - (capital_a * capital_b * k - e * ell)
    gap_error = level - (capital_a * second_ell - a * ell)
    return CompletionInvariant(e, f, ell, level, error, second_ell, gap_error)


def pair_resultant(
    anchor: tuple[int, int],
    partner: tuple[int, int],
    first_row: tuple[int, int],
    second_row: tuple[int, int],
    first_carriers: tuple[int, int],
    second_carriers: tuple[int, int],
) -> PairResultant:
    """Check ``X_ij X_ji=L_i L_j-k*delta*t`` exactly."""

    c, d = anchor
    cp, dp = partner
    first = completion_invariant(anchor, partner, first_row, first_carriers)
    second = completion_invariant(anchor, partner, second_row, second_carriers)
    a_i, capital_a_i = first_row
    a_j, capital_a_j = second_row
    b_i, capital_b_i = first_carriers
    b_j, capital_b_j = second_carriers
    delta = a_i * capital_a_j - capital_a_i * a_j
    t = b_i * capital_b_j - capital_b_i * b_j
    forward = b_i * second.e - capital_b_i * second.f
    reverse = b_j * first.e - capital_b_j * first.f
    k = c * dp - cp * d
    error = forward * reverse - (first.level * second.level - k * delta * t)
    return PairResultant(delta, t, forward, reverse, error)


def carrier_rectangle_minor(
    first_partner: tuple[int, int],
    second_partner: tuple[int, int],
) -> int:
    """Determinant of a two-row by two-partner carrier rectangle."""

    first_top, first_bottom = first_partner
    second_top, second_bottom = second_partner
    return first_top * second_bottom - second_top * first_bottom


def nearest_integer(value: Fraction) -> int:
    """Round a rational to the nearest integer, resolving ties upward."""

    value = Fraction(value)
    return (2 * value.numerator + value.denominator) // (2 * value.denominator)


def partner_level_center(
    q: int,
    anchor: tuple[int, int],
    partner: tuple[int, int],
) -> Fraction:
    """Return the color-only center ``q^3 k/(8 c d')`` exactly."""

    if q <= 0:
        raise ValueError("q must be positive")
    c, d = anchor
    cp, dp = partner
    if min(c, d, cp, dp) <= 0:
        raise ValueError("color coordinates must be positive")
    k = c * dp - cp * d
    return Fraction(q**3 * k, 8 * c * dp)


def partner_level_spacing(
    q: int,
    anchor: tuple[int, int],
    first_partner: tuple[int, int],
    second_partner: tuple[int, int],
) -> PartnerLevelSpacing:
    """Replay the exact spacing identity for two color-only levels.

    If the partners are ``r=(c_r,d_r)`` and ``s=(c_s,d_s)``, then

    ``X_r-X_s=q^3*d*(c_s*d_r-c_r*d_s)/(8*c*d_r*d_s)``.
    """

    c, d = anchor
    cr, dr = first_partner
    cs, ds = second_partner
    first_center = partner_level_center(q, anchor, first_partner)
    second_center = partner_level_center(q, anchor, second_partner)
    determinant = cs * dr - cr * ds
    claimed_spacing = Fraction(q**3 * d * determinant, 8 * c * dr * ds)
    error = first_center - second_center - claimed_spacing
    return PartnerLevelSpacing(
        first_center=first_center,
        second_center=second_center,
        partner_determinant=determinant,
        spacing_identity_error=error,
        first_rounded_level=nearest_integer(first_center),
        second_rounded_level=nearest_integer(second_center),
    )
