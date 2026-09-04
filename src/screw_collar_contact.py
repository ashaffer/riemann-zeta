#!/usr/bin/env python3
"""Exact arithmetic for two screw-kernel collar countermodels.

The formulas in this module use :class:`fractions.Fraction` throughout.  They
support the analytic audit in
``results/ZETA23-SCREW-COLLAR-POTENTIAL-AND-CONTACT-AUDIT-2026-09-01.md``;
they are not numerical evidence for or against RH.

The first model uses the even C1 compactly supported difference kernel

    k(t) = 1                                      (|t| <= 1),
           1 - 3 r^2 + 2 r^3, r = |t| - 1       (1 <= |t| <= 2),
           0                                      (|t| >= 2).

On the old interval (0,1), its quadratic form is ``|integral f|^2``.  The
mean-zero function

    n(t) = p(t) - p(t-1/2),
    p(t) = t(1/4-t) 1_[0,1/4](t),

is therefore a nullvector.  Pair it with the collar bump

    w_delta(1+t) = t(delta-t) 1_[0,delta](t).

Direct polynomial integration gives ``hostile_cross`` below.  Its nonzero
value for every ``0 < delta <= 1/4`` makes the enlarged two-dimensional form
indefinite.

The second model uses ``g_p(t)=(|t|-2)_+^p`` and the old mean-zero input
``u(t)=t`` on (-1,1).  Its exterior potential is flat to arbitrarily high
finite order while remaining nonzero on every collar.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

Polynomial2 = dict[tuple[int, int], Fraction]


def _as_fraction(value: Fraction | int) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def hostile_cross(delta: Fraction | int) -> Fraction:
    """Return the exact old--collar cross term in the C1 kernel model."""
    d = _as_fraction(delta)
    return -(d**7) * (28 * d**2 - 135 * d + 90) / 60480


def hostile_cross_expanded(delta: Fraction | int) -> Fraction:
    """The independently expanded polynomial form of ``hostile_cross``."""
    d = _as_fraction(delta)
    return -(d**9) / 2160 + (d**8) / 448 - (d**7) / 672


def _multiply(left: Polynomial2, right: Polynomial2) -> Polynomial2:
    answer: Polynomial2 = {}
    for (left_t, left_y), left_coefficient in left.items():
        for (right_t, right_y), right_coefficient in right.items():
            exponent = (left_t + right_t, left_y + right_y)
            answer[exponent] = answer.get(exponent, Fraction(0)) + (
                left_coefficient * right_coefficient
            )
    return {exponent: value for exponent, value in answer.items() if value}


def _t_minus_y_power(power: int) -> Polynomial2:
    return {
        (power - y_power, y_power): Fraction(comb(power, y_power))
        * (-1) ** y_power
        for y_power in range(power + 1)
    }


def hostile_cross_from_integrand(delta: Fraction | int) -> Fraction:
    """Integrate the defining polynomials over ``0 <= y <= t <= delta``.

    The constant part of the kernel pairs to zero with the old mean-zero
    vector.  On the only remaining interaction triangle the integrand is

        y(1/4-y) * t(delta-t) * [-3(t-y)^2+2(t-y)^3].

    This routine expands that integrand and applies the exact monomial rule

        int_0^delta int_0^t t^i y^j dy dt
          = delta^(i+j+2) / ((j+1)(i+j+2)).
    """
    d = _as_fraction(delta)
    old_bump: Polynomial2 = {
        (0, 1): Fraction(1, 4),
        (0, 2): Fraction(-1),
    }
    collar_bump: Polynomial2 = {
        (1, 0): d,
        (2, 0): Fraction(-1),
    }
    transition: Polynomial2 = {}
    for coefficient, power in ((-3, 2), (2, 3)):
        for exponent, value in _t_minus_y_power(power).items():
            transition[exponent] = transition.get(exponent, Fraction(0)) + (
                coefficient * value
            )
    integrand = _multiply(_multiply(old_bump, collar_bump), transition)
    answer = Fraction(0)
    for (t_power, y_power), coefficient in integrand.items():
        answer += coefficient * d ** (t_power + y_power + 2) / (
            (y_power + 1) * (t_power + y_power + 2)
        )
    return answer


def hostile_collar_energy(delta: Fraction | int) -> Fraction:
    """Return q(w_delta,w_delta); the collar sees the constant part of k."""
    d = _as_fraction(delta)
    return d**6 / 36


def hostile_block_determinant(delta: Fraction | int) -> Fraction:
    """Determinant of the old-null/collar 2x2 form block."""
    cross = hostile_cross(delta)
    return -(cross**2)


def shell_potential(power: int, distance: Fraction | int) -> Fraction:
    """Exterior potential at ``x=1+s`` for ``g_p`` and ``u(y)=y``.

    Here ``g_p(t)=(|t|-2)_+^p`` and ``u`` is restricted to ``[-1,1]``.
    For ``0 <= s <= 1``, beta integration yields

        integral_0^s (s-r)^p (r-1) dr
          = s^(p+1) (s-(p+2)) / ((p+1)(p+2)).
    """
    if power < 1:
        raise ValueError("power must be positive")
    s = _as_fraction(distance)
    if not 0 <= s <= 1:
        raise ValueError("the replay formula is restricted to 0 <= s <= 1")
    return s ** (power + 1) * (s - (power + 2)) / (
        (power + 1) * (power + 2)
    )


def shell_collar_charge_squared(
    power: int, width: Fraction | int
) -> Fraction:
    """Exact two-sided L2 squared collar charge for the shell model."""
    if power < 1:
        raise ValueError("power must be positive")
    d = _as_fraction(width)
    if not 0 <= d <= 1:
        raise ValueError("the replay formula is restricted to 0 <= width <= 1")
    p = power
    scale = Fraction(2, (p + 1) ** 2 * (p + 2) ** 2)
    integral = (
        d ** (2 * p + 5) / (2 * p + 5)
        - 2 * (p + 2) * d ** (2 * p + 4) / (2 * p + 4)
        + (p + 2) ** 2 * d ** (2 * p + 3) / (2 * p + 3)
    )
    return scale * integral


def main() -> None:
    for raw_delta in (Fraction(1, 4), Fraction(1, 8), Fraction(1, 32)):
        print(
            f"delta={raw_delta} cross={hostile_cross(raw_delta)} "
            f"collar={hostile_collar_energy(raw_delta)} "
            f"det={hostile_block_determinant(raw_delta)}"
        )


if __name__ == "__main__":
    main()
