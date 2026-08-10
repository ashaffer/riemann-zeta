#!/usr/bin/env python3
"""Exact finite algebra for the central pole of a high-order mollifier.

This module proves no zero-free region.  It records the residue polynomial
created when an order-``k`` logarithmic mollifier is paired with the original
first-order Mellin auxiliary factor.

Write ``z = w - 1`` and let

    R(1+z) = sum_{j>=0} r_j z^j

be the analytic factor left after separating the central denominator.  The
central part of the contour integrand is

    k! * x * exp(z log x) * R(1+z) / z^(k-1).

For ``k>=2`` its residue at ``z=0`` is

    x * k! * sum_{j=0}^{k-2}
        r_j * (log x)^(k-2-j) / (k-2-j)!.

Hence it is ``x`` times a polynomial of degree at most ``k-2``.  The operator
``D_L - 1``, with ``L=log x``, differentiates that polynomial after removing
the factor ``x``.  Applying it ``k-1`` times annihilates the complete central
residue.  On a target carrier

    exp(w0 L) / (w0-1)^(k-1),

however, the same operator contributes ``(w0-1)^(k-1)`` and cancels the
entire apparent high-order amplification.
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Iterable, Sequence


RationalLike = int | Fraction


def _fraction(value: RationalLike) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("coefficients must be integers or Fraction values")
    return Fraction(value)


def central_pole_order(order: int) -> int:
    """Return the order ``max(k-1,0)`` of the new central pole."""

    if not isinstance(order, int) or isinstance(order, bool) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    return max(0, order - 1)


def central_residue_polynomial(
    order: int, taylor_coefficients: Sequence[RationalLike]
) -> tuple[Fraction, ...]:
    """Return ascending coefficients of the exact central residue polynomial.

    ``taylor_coefficients[j]`` is ``r_j`` in
    ``R(1+z)=sum_j r_j z^j``.  The returned tuple ``c`` represents

    ``x * sum_m c[m] * (log x)^m``.

    Only ``r_0,...,r_(k-2)`` enter.  For ``k<=1`` the reused first-order
    kernel creates no central pole, and the zero polynomial is returned.
    """

    if not isinstance(order, int) or isinstance(order, bool) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    if order <= 1:
        return ()
    required = order - 1
    if len(taylor_coefficients) < required:
        raise ValueError(
            f"order {order} requires at least {required} Taylor coefficients"
        )
    coefficients = tuple(_fraction(value) for value in taylor_coefficients)
    scale = math.factorial(order)
    result: list[Fraction] = []
    for power in range(order - 1):
        taylor_index = order - 2 - power
        result.append(
            Fraction(scale, math.factorial(power)) * coefficients[taylor_index]
        )
    return tuple(result)


def polynomial_derivative(
    coefficients: Sequence[RationalLike], steps: int = 1
) -> tuple[Fraction, ...]:
    """Differentiate an ascending-coefficient polynomial exactly."""

    if not isinstance(steps, int) or isinstance(steps, bool) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    result = tuple(_fraction(value) for value in coefficients)
    for _ in range(steps):
        result = tuple(
            Fraction(power) * result[power]
            for power in range(1, len(result))
        )
        if not result:
            return ()
    return result


def center_after_shifted_derivatives(
    order: int,
    taylor_coefficients: Sequence[RationalLike],
    steps: int,
) -> tuple[Fraction, ...]:
    r"""Polynomial left after applying ``(D_L-1)^steps`` to the center.

    Since ``(D_L-1)(exp(L)P(L))=exp(L)P'(L)``, this is simply the exact
    derivative of the residue polynomial.
    """

    return polynomial_derivative(
        central_residue_polynomial(order, taylor_coefficients), steps
    )


def remaining_center_degree(order: int, steps: int) -> int:
    """Maximum remaining polynomial degree, using ``-1`` for the zero center."""

    if not isinstance(order, int) or isinstance(order, bool) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    if not isinstance(steps, int) or isinstance(steps, bool) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    return max(-1, order - 2 - steps)


def target_factor_after_shifted_derivatives(
    order: int, steps: int, spectral_shift: RationalLike
) -> Fraction:
    r"""Target factor after ``steps`` applications of ``D_L-1``.

    The initially isolated high-order target contains
    ``spectral_shift**(-(k-1))``.  Every shifted derivative multiplies it by
    ``spectral_shift``.  Full center annihilation at ``steps=k-1`` therefore
    leaves factor one exactly.
    """

    if not isinstance(order, int) or isinstance(order, bool) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    if not isinstance(steps, int) or isinstance(steps, bool) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    shift = _fraction(spectral_shift)
    if shift == 0:
        raise ValueError("spectral_shift must be nonzero")
    exponent = steps - central_pole_order(order)
    if exponent >= 0:
        return shift**exponent
    return Fraction(1, 1) / (shift ** (-exponent))


def full_annihilation_repays_target(
    orders: Iterable[int], spectral_shifts: Iterable[RationalLike]
) -> None:
    """Assert the exact repayment identity on a finite rational grid."""

    saw_case = False
    for order in orders:
        if not isinstance(order, int) or isinstance(order, bool) or order < 1:
            raise ValueError("orders must contain positive integers")
        for spectral_shift in spectral_shifts:
            saw_case = True
            factor = target_factor_after_shifted_derivatives(
                order, central_pole_order(order), spectral_shift
            )
            if factor != 1:
                raise AssertionError(
                    "full center annihilation failed to repay target factor: "
                    f"k={order}, shift={spectral_shift}, factor={factor}"
                )
    if not saw_case:
        raise ValueError("the verification grid was empty")
