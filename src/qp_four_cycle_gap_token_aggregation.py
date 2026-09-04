"""Finite ledgers for parabolic gap-token aggregation.

The analytic theorem is proved in the accompanying report.  This module
 checks the exact finite mechanisms used there: thin-strip overlap, divisor
 lifting, occupied-line multipliers, and the normalized-GCD reduction of a
 primitive line slope.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd


def thin_strip_certificate(
    direction_height: int,
    determinant_width: int,
    shell_scale: int,
) -> bool:
    """Return the strict area condition ``H*D/q < 1``.

    Up to an absolute shell constant, this is the area of the symmetric
    body containing all primitive slope vectors attached to a fixed color
    pair and one dyadic factor-size block.
    """

    if min(direction_height, determinant_width, shell_scale) < 1:
        raise ValueError("all scales must be positive")
    return direction_height * determinant_width < shell_scale


def primitive_lifts_of_gap(
    gap: int,
    factor_radius: int,
) -> list[tuple[int, int, int]]:
    """Enumerate ``(r1,r2,eta)`` with ``r2*eta=gap``.

    The vector ``(r1,r2)`` is primitive, both coordinates are nonzero, and
    its sup norm is at most ``factor_radius``.  The theorem uses the bound
    ``O(R*tau(gap))`` for this list.
    """

    if gap == 0:
        raise ValueError("the nonzero-determinant sector has nonzero gaps")
    if factor_radius < 1:
        raise ValueError("factor_radius must be positive")
    lifts: list[tuple[int, int, int]] = []
    for r2 in range(-factor_radius, factor_radius + 1):
        if r2 == 0 or gap % r2:
            continue
        eta = gap // r2
        for r1 in range(-factor_radius, factor_radius + 1):
            if r1 == 0 or gcd(abs(r1), abs(r2)) != 1:
                continue
            lifts.append((r1, r2, eta))
    return lifts


def signed_divisor_count(value: int) -> int:
    """Count nonzero signed divisors of ``value`` exactly."""

    if value == 0:
        raise ValueError("value must be nonzero")
    n = abs(value)
    positive = sum(1 for divisor in range(1, n + 1) if n % divisor == 0)
    return 2 * positive


def divisor_lift_bound_is_valid(gap: int, factor_radius: int) -> bool:
    """Check the elementary ``2 R`` choices per signed divisor bound."""

    lifts = primitive_lifts_of_gap(gap, factor_radius)
    return len(lifts) <= 2 * factor_radius * signed_divisor_count(gap)


@dataclass(frozen=True)
class OccupiedParabolicLineLedger:
    """Canonical data for one primitive carrier line.

    In unimodular coordinates the signed color matrix is
    ``((0, theta), (eta, gamma))`` and the two carriers have coordinates
    ``(u, alpha)`` and ``(v, beta)``.  Constancy of the common level fixes
    the primitive longitudinal direction ``(A, B)``.
    """

    determinant: int
    common_level: int
    transverse_gcd: int
    row_multiplier: int
    column_multiplier: int
    quadratic_multiplier: int

    @property
    def primitive_direction(self) -> bool:
        return gcd(abs(self.row_multiplier), abs(self.column_multiplier)) == 1

    @property
    def transverse_scale_divides_level_discriminant(self) -> bool:
        return (self.determinant * self.common_level) % self.transverse_gcd == 0


def occupied_parabolic_line_ledger(
    *,
    eta: int,
    theta: int,
    gamma: int,
    u: int,
    alpha: int,
    v: int,
    beta: int,
) -> OccupiedParabolicLineLedger:
    """Return the exact primitive-multiplier ledger for one carrier line.

    The zero transverse-coordinate cases are excluded in the active
    all-distinct chart.  Signs of the two multipliers are retained.
    """

    if eta == 0 or theta == 0 or alpha == 0 or beta == 0:
        raise ValueError("eta, theta, alpha, and beta must be nonzero")
    eta_alpha = eta * alpha
    theta_beta = theta * beta
    transverse_gcd = gcd(abs(eta_alpha), abs(theta_beta))
    row_multiplier = eta_alpha // transverse_gcd
    column_multiplier = -theta_beta // transverse_gcd
    common_level = theta * u * beta + eta * alpha * v + gamma * alpha * beta
    determinant = -eta * theta
    ledger = OccupiedParabolicLineLedger(
        determinant=determinant,
        common_level=common_level,
        transverse_gcd=transverse_gcd,
        row_multiplier=row_multiplier,
        column_multiplier=column_multiplier,
        quadratic_multiplier=row_multiplier * column_multiplier,
    )
    if not ledger.primitive_direction:
        raise AssertionError("the canonical carrier direction is not primitive")
    if not ledger.transverse_scale_divides_level_discriminant:
        raise AssertionError("the transverse scale failed to divide kL")
    return ledger


@dataclass(frozen=True)
class NormalizedGCDLineLedger:
    """Reduced wedge ratios and their normalized-GCD line weight.

    Absolute values are used because the finitely many sign blocks are
    separated in the analytic argument.  If

    ``(eta,beta)=t*(q,p)`` and ``(theta,alpha)=u*(s,r)``

    with both displayed pairs primitive, then the common factors ``t,u``
    cancel from ``1/sqrt(|A*B|)``.
    """

    eta_beta_content: int
    theta_alpha_content: int
    eta_reduced: int
    beta_reduced: int
    theta_reduced: int
    alpha_reduced: int
    reduced_cross_gcd: int
    row_multiplier: int
    column_multiplier: int
    inverse_quadratic_multiplier: Fraction

    @property
    def rich_fixed_direction_threshold(self) -> int:
        """Three points are needed for fixed-direction intercept pinning."""

        return 3


def normalized_gcd_line_ledger(
    *,
    eta: int,
    theta: int,
    alpha: int,
    beta: int,
) -> NormalizedGCDLineLedger:
    """Return the exact normalized-GCD reduction of ``|A*B|^-1``.

    The returned rational number is ``1/|A*B|``, the square of the analytic
    normalized-GCD kernel.  Keeping the square makes this finite replay
    exact and avoids floating-point square roots.
    """

    if eta == 0 or theta == 0 or alpha == 0 or beta == 0:
        raise ValueError("eta, theta, alpha, and beta must be nonzero")

    eta_beta_content = gcd(abs(eta), abs(beta))
    theta_alpha_content = gcd(abs(theta), abs(alpha))
    eta_reduced = abs(eta) // eta_beta_content
    beta_reduced = abs(beta) // eta_beta_content
    theta_reduced = abs(theta) // theta_alpha_content
    alpha_reduced = abs(alpha) // theta_alpha_content
    left_integer = eta_reduced * alpha_reduced
    right_integer = theta_reduced * beta_reduced
    reduced_cross_gcd = gcd(left_integer, right_integer)
    row_multiplier = left_integer // reduced_cross_gcd
    column_multiplier = right_integer // reduced_cross_gcd
    inverse_quadratic_multiplier = Fraction(
        reduced_cross_gcd**2,
        left_integer * right_integer,
    )

    actual_transverse_gcd = gcd(abs(eta * alpha), abs(theta * beta))
    if actual_transverse_gcd != (
        eta_beta_content * theta_alpha_content * reduced_cross_gcd
    ):
        raise AssertionError("the transverse content did not factor")
    if gcd(row_multiplier, column_multiplier) != 1:
        raise AssertionError("the reduced line direction is not primitive")
    if inverse_quadratic_multiplier != Fraction(
        1, row_multiplier * column_multiplier
    ):
        raise AssertionError("the normalized-GCD weight is inconsistent")

    return NormalizedGCDLineLedger(
        eta_beta_content=eta_beta_content,
        theta_alpha_content=theta_alpha_content,
        eta_reduced=eta_reduced,
        beta_reduced=beta_reduced,
        theta_reduced=theta_reduced,
        alpha_reduced=alpha_reduced,
        reduced_cross_gcd=reduced_cross_gcd,
        row_multiplier=row_multiplier,
        column_multiplier=column_multiplier,
        inverse_quadratic_multiplier=inverse_quadratic_multiplier,
    )


def fixed_direction_merger_applies(occupied_parameter_count: int) -> bool:
    """Return whether the proved rich fixed-direction merger applies.

    Two-point lines are deliberately left out: they are isolated secant
    chords and retain the varying-``E`` correlation.
    """

    if occupied_parameter_count < 0:
        raise ValueError("occupied_parameter_count must be nonnegative")
    return occupied_parameter_count >= 3


def occupied_line_inverse_sqrt_sum(line_count: int) -> float:
    """Return ``sum_{n<=J} n^(-1/2)`` for the occupied-line ledger."""

    if line_count < 0:
        raise ValueError("line_count must be nonnegative")
    return sum(index**-0.5 for index in range(1, line_count + 1))


def occupied_line_square_root_bound_is_valid(line_count: int) -> bool:
    """Check the elementary ordering bound ``sum n^-1/2 <=2 sqrt(J)``."""

    if line_count < 0:
        raise ValueError("line_count must be nonnegative")
    if line_count == 0:
        return True
    return occupied_line_inverse_sqrt_sum(line_count) <= 2 * line_count**0.5


@dataclass(frozen=True)
class RefinedParabolicExponentLedger:
    """Exact exponent ledger for one determinant-content block.

    The variables encode

    ``R=D^r, S=D^s, E=D^e, T=D^t, G=D^g``.

    Here ``G`` is the dyadic size of ``gcd(eta, theta)``.  Its inverse
    occurs both in the exact plane covolume and in the refined color-mass
    estimate ``sqrt(E*T*R*S)/G``.
    """

    plane_covolume: Fraction
    slice_multiplicity: Fraction
    relation_mass: Fraction
    singleton_contribution: Fraction
    curvature_contribution: Fraction

    @property
    def scoped_bounds_hold(self) -> bool:
        return (
            self.singleton_contribution <= Fraction(5, 4)
            and self.curvature_contribution <= Fraction(37, 32)
        )


def refined_parabolic_exponent_ledger(
    *,
    row_height: Fraction,
    column_height: Fraction,
    eta_height: Fraction,
    theta_height: Fraction,
    gcd_height: Fraction,
) -> RefinedParabolicExponentLedger:
    """Return the exact LP ledger behind the scoped ``D^(5/4)`` theorem.

    All inputs are exponents to base ``D``.  Invalid points outside the
    feasible minima polytope raise ``ValueError``.
    """

    r = Fraction(row_height)
    s = Fraction(column_height)
    e = Fraction(eta_height)
    t = Fraction(theta_height)
    g = Fraction(gcd_height)
    if min(r, s, e, t, g) < 0:
        raise ValueError("all dyadic exponents must be nonnegative")
    if r + s > 1 or e + t > 1:
        raise ValueError("direction height or determinant exceeds D")
    if g > min(e, t):
        raise ValueError("the gcd scale cannot exceed either factor")

    plane_covolume = max(e + 2 * r, t + 2 * s) - g
    if plane_covolume > Fraction(11, 8):
        raise ValueError("the first-two-minima product exceeds q^(2/3)")
    slice_multiplicity = max(
        Fraction(0), plane_covolume - Fraction(17, 16)
    )
    relation_mass = (e + t + r + s) / 2 - g
    singleton = slice_multiplicity + relation_mass
    curvature = (
        1 + slice_multiplicity + e + t
    ) / 2 - g
    ledger = RefinedParabolicExponentLedger(
        plane_covolume=plane_covolume,
        slice_multiplicity=slice_multiplicity,
        relation_mass=relation_mass,
        singleton_contribution=singleton,
        curvature_contribution=curvature,
    )
    if not ledger.scoped_bounds_hold:
        raise AssertionError("the refined parabolic exponent LP failed")
    return ledger
