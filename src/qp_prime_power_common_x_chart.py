"""Exact ledgers for the prime-power common-X parabolic chart.

The arithmetic chart lemma itself is stated in the accompanying report.
These helpers replay its finite congruence and rational-exponent checks;
they do not assert a sharp global four-cycle theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd


Q_EXPONENT = Fraction(33, 16)


def compatible_common_x(
    x: int,
    r1: int,
    r2: int,
    s1: int,
    s2: int,
    eta: int,
    theta: int,
) -> bool:
    """Return whether the two mandatory chart congruences hold."""

    if not r2 or not s2:
        raise ValueError("the active parabolic chart has nonzero components")
    if gcd(abs(r1), abs(r2)) != 1 or gcd(abs(s1), abs(s2)) != 1:
        raise ValueError("r and s must be primitive")
    return (
        (s1 * x - r2 * eta) % abs(s2) == 0
        and (r1 * x + s2 * theta) % abs(r2) == 0
    )


def cross_gcd_divides_x(
    x: int,
    r1: int,
    r2: int,
    s1: int,
    s2: int,
    eta: int,
    theta: int,
) -> bool:
    """Replay ``gcd(r2,s2)|X`` for a compatible primitive chart."""

    if not compatible_common_x(x, r1, r2, s1, s2, eta, theta):
        raise ValueError("x is not on the two-congruence chart")
    return x % gcd(abs(r2), abs(s2)) == 0


@dataclass(frozen=True)
class CommonXExponentLedger:
    """Power-of-D ledger for one flat parabolic singleton block."""

    chart_count: Fraction
    chart_length: Fraction
    color_mass: Fraction
    singleton_trace: Fraction


def common_x_exponent_ledger(
    *,
    e: Fraction,
    t: Fraction,
    r: Fraction,
    s: Fraction,
    mu: Fraction,
    kappa: Fraction,
) -> CommonXExponentLedger:
    """Return the exponents in the actual prime-power chart estimate."""

    chart_count = 2 * r + 2 * s + e + t
    chart_length = min(mu, Q_EXPONENT - r - s)
    color_mass = chart_count + chart_length - 2 * mu
    return CommonXExponentLedger(
        chart_count=chart_count,
        chart_length=chart_length,
        color_mass=color_mass,
        singleton_trace=color_mass + kappa,
    )


def principal_upper_pair(mu: Fraction) -> tuple[Fraction, Fraction]:
    """Return the universal progression-chart and principal exponents.

    The first entry is ``35/8-2*mu`` and the second ``mu-3/4``.
    Their minimum is at most 23/24.
    """

    return Fraction(35, 8) - 2 * mu, mu - Fraction(3, 4)


def nonprincipal_singleton_exponent(mu: Fraction) -> Fraction:
    """Return the mixed-H^2 nonprincipal exponent with kappa=5/16."""

    mass = min(Fraction(1, 2) + mu / 4, Fraction(65, 64) - mu / 4)
    return Fraction(5, 16) + mass
