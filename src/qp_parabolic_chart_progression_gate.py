"""Exact common-X progression bounds for parabolic QP color charts.

The routines here replay the elementary congruences behind the chart
occupancy cutoff.  They also retain the exponent ledger at the primitive
high-completion face.  No analytic prime-tuple estimate is asserted.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, lcm


D_TO_Q = Fraction(33, 16)


def chart_colors(
    *,
    x: int,
    r1: int,
    r2: int,
    s1: int,
    s2: int,
    eta: int,
    theta: int,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Return ``(x,y,zeta,w)`` in the exact common-X chart.

    Fractions are kept so failed integrality remains visible.
    """

    if r2 == 0 or s2 == 0:
        raise ValueError("the active chart has nonzero second coordinates")
    y = Fraction(s1 * x - r2 * eta, s2)
    zeta = Fraction(r1 * x + s2 * theta, r2)
    w = Fraction(r1 * y + s1 * theta, r2)
    return Fraction(x), y, zeta, w


def common_x_modulus(*, r1: int, r2: int, s1: int, s2: int) -> int:
    """Return the modulus of the simultaneous common-X congruences.

    For primitive ``r`` and ``s``, integrality of ``y`` and ``zeta`` puts
    ``X`` in one residue class modulo ``|s2|`` and ``|r2|`` respectively.
    """

    if gcd(abs(r1), abs(r2)) != 1 or gcd(abs(s1), abs(s2)) != 1:
        raise ValueError("r and s must be primitive")
    if r2 == 0 or s2 == 0:
        raise ValueError("the active chart has nonzero second coordinates")
    return lcm(abs(r2), abs(s2))


def common_component_divisor(*, r2: int, s2: int) -> int:
    """The divisor forced into every integral common-X value."""

    if r2 == 0 or s2 == 0:
        raise ValueError("the active chart has nonzero second coordinates")
    return gcd(abs(r2), abs(s2))


def affine_steps(*, r1: int, r2: int, s1: int, s2: int) -> tuple[int, int, int, int]:
    """Steps of ``(x,y,zeta,w)`` when ``gcd(r2,s2)=1``.

    Taking ``X=X0+n*r2*s2`` gives the four displayed steps, up to a common
    sign fixed by orientation.
    """

    if gcd(abs(r2), abs(s2)) != 1:
        raise ValueError("the product-modulus formula requires coprime components")
    return r2 * s2, s1 * r2, r1 * s2, r1 * s1


@dataclass(frozen=True)
class PrimitiveFaceLedger:
    """Exponent ledger for the relocated primitive singleton face."""

    eta: Fraction = Fraction(1, 2)
    theta: Fraction = Fraction(1, 2)
    row: Fraction = Fraction(7, 16)
    column: Fraction = Fraction(7, 16)
    gcd_height: Fraction = Fraction(0)
    occupied_lines: Fraction = Fraction(5, 16)
    principal_support: Fraction = Fraction(15, 8)
    nonprincipal_support: Fraction = Fraction(33, 32)

    @property
    def chart_count(self) -> Fraction:
        return (
            2 * self.row
            + 2 * self.column
            + self.eta
            + self.theta
            - self.gcd_height
        )

    @property
    def unrestricted_x_length(self) -> Fraction:
        return D_TO_Q - max(self.row, self.column)

    @property
    def actual_x_length(self) -> Fraction:
        return D_TO_Q - self.row - self.column

    def flat_trace(self, *, actual_prime_powers: bool) -> Fraction:
        """Raw flat-bin trace exponent at the principal support."""

        length = self.actual_x_length if actual_prime_powers else self.unrestricted_x_length
        return (
            self.chart_count
            + length
            + self.occupied_lines
            - 2 * self.principal_support
        )

    @property
    def required_principal_matrix_count(self) -> Fraction:
        """Number exponent needed to saturate ``M*D/q`` globally."""

        return 3 * self.principal_support + 1 - D_TO_Q

    @property
    def unrestricted_matrix_count(self) -> Fraction:
        return self.chart_count + self.unrestricted_x_length

    @property
    def actual_matrix_count(self) -> Fraction:
        return self.chart_count + self.actual_x_length

    @property
    def nonprincipal_mass(self) -> Fraction:
        mu = self.nonprincipal_support
        return min(Fraction(1, 2) + mu / 4, Fraction(65, 64) - mu / 4)

    @property
    def nonprincipal_trace(self) -> Fraction:
        return self.nonprincipal_mass + self.occupied_lines


def flat_chart_trace_exponent(
    *,
    row: Fraction,
    column: Fraction,
    eta: Fraction,
    theta: Fraction,
    gcd_height: Fraction,
    occupied_lines: Fraction,
    support: Fraction,
    actual_prime_powers: bool = True,
) -> Fraction:
    """Return the chart-count/flat-weight singleton exponent.

    A chart has weight at most ``min(M^-1, L*M^-2)``.  Here
    ``L<=q/(RS)`` on actual prime powers and ``L<=q/max(R,S)`` without the
    prime-power divisor argument.
    """

    chart_count = 2 * row + 2 * column + eta + theta - gcd_height
    if actual_prime_powers:
        length = D_TO_Q - row - column
    else:
        length = D_TO_Q - max(row, column)
    return (
        chart_count
        + occupied_lines
        - support
        + min(Fraction(0), length - support)
    )
