"""Exact algebra and exponent ledgers for nonzero Poisson saddle coalescence.

The phase is

    F(x) = C*(h/x + k/(S-x)) - m*x.

Opposite-sign Fourier frequencies can have a cubic stationary point.  This
module records its exact parametrisation and the dyadic costs used in the
companion audit report; it does not claim the missing collective large-sieve
estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd


Q_POWER_IN_D = Fraction(33, 16)
DELTA_POWER_IN_D = Fraction(-17, 16)
H_POWER_IN_D = Fraction(17, 16)


def exact_integer_cubic_parameters(
    common_factor: int,
    left_cube: int,
    right_cube: int,
    C: int,
    S: int,
    positive_left: bool = True,
) -> tuple[int, int, Fraction, Fraction]:
    """Return ``(h,k,x_star,m_star)`` for a rational cubic caustic.

    Put ``u=d*r^3`` and ``v=d*s^3``.  For ``h=u, k=-v`` the inflection is
    ``x_star=S*r/(r+s)`` and the critical dual value is

        m_star = -C*d*(r+s)^3/S^2.

    Simultaneously changing the signs of ``h,k`` changes the sign of
    ``m_star``.  The returned value need not be integral.
    """

    d, r, s = common_factor, left_cube, right_cube
    if min(d, r, s, C, S) <= 0:
        raise ValueError("all parameters must be positive")
    if gcd(r, s) != 1:
        raise ValueError("the cube parameters must be coprime")
    sign = 1 if positive_left else -1
    h = sign * d * r**3
    k = -sign * d * s**3
    x_star = Fraction(S * r, r + s)
    m_star = Fraction(-sign * C * d * (r + s) ** 3, S**2)
    return h, k, x_star, m_star


def phase_derivative_numerators_at_cubic(
    common_factor: int,
    left_cube: int,
    right_cube: int,
    C: int,
    S: int,
) -> dict[str, Fraction]:
    """Evaluate ``F'``, ``F''`` and ``F'''`` at the positive-left caustic.

    ``m`` is chosen to be the (possibly rational) critical dual value.  The
    first two derivatives vanish and the third never does.
    """

    h, k, x, m = exact_integer_cubic_parameters(
        common_factor, left_cube, right_cube, C, S
    )
    y = Fraction(S) - x
    first = C * (-Fraction(h, 1) / x**2 + Fraction(k, 1) / y**2) - m
    second = 2 * C * (Fraction(h, 1) / x**3 + Fraction(k, 1) / y**3)
    third = 6 * C * (-Fraction(h, 1) / x**4 + Fraction(k, 1) / y**4)
    assert first == 0
    assert second == 0
    assert third != 0
    return {"first": first, "second": second, "third": third}


def is_rational_cubic_pair(u: int, v: int) -> tuple[bool, int, int, int]:
    """Recognise when ``(cuberoot(u)+cuberoot(v))^3`` is rational.

    For positive integers this happens exactly when

        u=d*r^3, v=d*s^3, gcd(r,s)=1.

    The returned tuple is ``(is_pair,d,r,s)``.  Zeros are returned for the
    last three fields when the condition fails.
    """

    if min(u, v) <= 0:
        raise ValueError("u and v must be positive")
    d = gcd(u, v)
    ur, vr = u // d, v // d
    def integer_cube_root(value: int) -> int:
        low, high = 0, 1
        while high**3 <= value:
            high *= 2
        while low + 1 < high:
            middle = (low + high) // 2
            if middle**3 <= value:
                low = middle
            else:
                high = middle
        return low

    r, s = integer_cube_root(ur), integer_cube_root(vr)
    if r**3 == ur and s**3 == vr:
        assert gcd(r, s) == 1
        return True, d, r, s
    return False, 0, 0, 0


@dataclass(frozen=True)
class CenteredCuspCoordinates:
    """Frequency coordinates in the exact symmetric cusp normal form."""

    p: int
    d: int
    ell: int
    constant: int


def centered_cusp_coordinates(h: int, k: int, m: int, Q: int) -> CenteredCuspCoordinates:
    """Return the exact normal-form coordinates for ``C=Q^2,S=2Q``.

    With ``x=Q+y``, ``p=h+k`` and ``d=k-h``, the phase is exactly

        Q*(p-m) + (d-m)*y + (Q*p*y^2+d*y^3)/(Q^2-y^2).

    Thus ``p=0`` kills curvature and ``ell=d-m=0`` reaches the cusp.
    """

    if Q <= 0:
        raise ValueError("Q must be positive")
    p = h + k
    d = k - h
    return CenteredCuspCoordinates(p=p, d=d, ell=d - m, constant=Q * (p - m))


def verify_centered_phase_identity(h: int, k: int, m: int, Q: int, y: int) -> bool:
    """Verify the centered rational phase identity by exact arithmetic."""

    if abs(y) >= Q:
        raise ValueError("require |y|<Q")
    x = Q + y
    phase = Fraction(Q * Q * h, x) + Fraction(Q * Q * k, 2 * Q - x) - m * x
    coords = centered_cusp_coordinates(h, k, m, Q)
    normal = (
        coords.constant
        + coords.ell * y
        + Fraction(Q * coords.p * y * y + coords.d * y**3, Q * Q - y * y)
    )
    return phase == normal


def cubic_dyadic_exponent_ledger() -> dict[str, Fraction]:
    """Return powers of ``D`` for the rigorous absolute saddle stratification.

    At ``|h|,|k|~K`` an opposite-sign integral has one possible Airy mode
    of size ``q^(2/3)K^(-1/3)``.  The other integer dual modes sum to
    ``q^(1/2)K^(1/2)`` for each pair.  Summing the pairs and applying the two
    Selberg coefficients gives the entries below at ``K=H``.
    """

    delta, q, H = DELTA_POWER_IN_D, Q_POWER_IN_D, H_POWER_IN_D
    target = Fraction(1, 2)
    exact_cubic_family = 2 * delta + Fraction(2, 3) * q + Fraction(2, 3) * H
    one_airymode_per_pair = (
        2 * delta + Fraction(2, 3) * q + Fraction(5, 3) * H
    )
    regular_dual_modes = 2 * delta + q / 2 + Fraction(5, 2) * H
    crude_uniform_cubic_for_every_mode = (
        2 * delta + Fraction(2, 3) * q + Fraction(8, 3) * H
    )
    return {
        "target": target,
        "exact_cubic_family": exact_cubic_family,
        "one_airymode_per_pair": one_airymode_per_pair,
        "regular_dual_modes": regular_dual_modes,
        "crude_uniform_cubic_for_every_mode": crude_uniform_cubic_for_every_mode,
        "remaining_regular_gap": regular_dual_modes - target,
    }
