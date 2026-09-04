#!/usr/bin/env python3
"""Exact endpoint-flat Riesz ramps used by the one-sided Landau audit.

For an integer endpoint order ``r >= 0``, put

    w_r(y) = ((r + 2)y - 1)(1 - y)^r / (r + 1)!,  0 <= y <= 1.

Its Mellin transform is

    integral_0^1 w_r(y)y^(s-1)dy
      = (s - 1) / (s(s+1)...(s+r+1)).

Thus ``r=0`` is the R95/R96 ramp ``2y-1`` and every ``r>=1`` is an
endpoint-flat positive smoothing of it.  The routines below replay the exact
algebra and finite actual-prime formulas.  They do not assert an asymptotic
one-sided estimate or a zero-free region.
"""

from __future__ import annotations

import math
from fractions import Fraction
from typing import Literal, Sequence


Rational = int | Fraction


def _order(value: int) -> int:
    if type(value) is not int or value < 0:
        raise ValueError("endpoint order must be a nonnegative integer")
    return value


def endpoint_flat_beta_coefficients(order: int) -> tuple[Fraction, ...]:
    """Return the coefficients of ``w_r(y)=sum_j c_j y^j`` exactly."""

    order = _order(order)
    return tuple(
        Fraction((-1) ** (index + 1) * (index + 1),
                 math.factorial(index) * math.factorial(order + 1 - index))
        for index in range(order + 2)
    )


def endpoint_flat_beta_weight_exact(order: int, ratio: Rational) -> Fraction:
    """Evaluate the beta ramp exactly at a rational ``0 <= ratio <= 1``."""

    order = _order(order)
    y = Fraction(ratio)
    if not 0 <= y <= 1:
        raise ValueError("ratio must lie in [0, 1]")
    return Fraction((order + 2) * y - 1) * (1 - y) ** order / math.factorial(
        order + 1
    )


def endpoint_flat_beta_weight(order: int, ratio: float) -> float:
    """Evaluate the beta ramp in floating-point arithmetic."""

    order = _order(order)
    if not math.isfinite(ratio) or not 0.0 <= ratio <= 1.0:
        raise ValueError("ratio must be finite and lie in [0, 1]")
    return (
        ((order + 2) * ratio - 1)
        * (1 - ratio) ** order
        / math.factorial(order + 1)
    )


def endpoint_flat_beta_mellin_target(order: int, s: Rational) -> Fraction:
    """Evaluate ``(s-1)/(s(s+1)...(s+r+1))`` exactly."""

    order = _order(order)
    point = Fraction(s)
    denominator = math.prod(
        (point + index for index in range(order + 2)), start=Fraction(1)
    )
    return (point - 1) / denominator


def endpoint_flat_beta_continuum(order: int, x: float) -> float:
    """Return the exactly cancelled continuum contribution."""

    order = _order(order)
    if not math.isfinite(x) or x < 1.0:
        raise ValueError("x must be finite and at least one")
    return (1.0 - 1.0 / x) ** (order + 1) / math.factorial(order + 1)


def endpoint_flat_beta_ramp(
    order: int, x: float, mangoldt: Sequence[float]
) -> float:
    """Evaluate the centered endpoint-flat von Mangoldt ramp at ``x``."""

    order = _order(order)
    if not math.isfinite(x) or x < 1.0:
        raise ValueError("x must be finite and at least one")
    maximum = math.floor(x)
    if maximum >= len(mangoldt):
        raise ValueError("mangoldt table is too short")
    prime_part = math.fsum(
        mangoldt[integer] * endpoint_flat_beta_weight(order, integer / x)
        for integer in range(2, maximum + 1)
        if mangoldt[integer]
    )
    return prime_part - endpoint_flat_beta_continuum(order, x)


def endpoint_flat_riesz_error(
    order: int, x: float, mangoldt: Sequence[float]
) -> float:
    r"""Evaluate the normalized Riesz error whose derivative is the ramp.

    The exact identity away from no special point (the cutoff weight already
    vanishes at entry) is

        B_r(x) = x^2 C_r'(x)/(r+1)!,

    where

        C_r(x) = x^-1 sum Lambda(n)(1-n/x)^(r+1)
                 - (1-x^-1)^(r+2)/(r+2).
    """

    order = _order(order)
    if not math.isfinite(x) or x < 1.0:
        raise ValueError("x must be finite and at least one")
    maximum = math.floor(x)
    if maximum >= len(mangoldt):
        raise ValueError("mangoldt table is too short")
    riesz_sum = math.fsum(
        mangoldt[integer] * (1.0 - integer / x) ** (order + 1)
        for integer in range(2, maximum + 1)
        if mangoldt[integer]
    )
    return riesz_sum / x - (1.0 - 1.0 / x) ** (order + 2) / (order + 2)


def endpoint_flat_riesz_derivative_numerator(
    order: int, x: float, mangoldt: Sequence[float]
) -> float:
    """Return ``x^2 C_r'(x)``, replaying the Riesz derivative identity."""

    return math.factorial(_order(order) + 1) * endpoint_flat_beta_ramp(
        order, x, mangoldt
    )


def fixed_orientation_bad_mass(
    values: Sequence[float],
    weights: Sequence[float] | None = None,
    *,
    orientation: Literal[-1, 1] = 1,
) -> float:
    """Return the discrete Jordan mass opposing one fixed orientation.

    ``orientation=1`` measures the negative part and ``orientation=-1`` the
    positive part.  The orientation is deliberately fixed for the complete
    sample; choosing it separately from block to block is not Landau-valid.
    """

    if orientation not in (-1, 1):
        raise ValueError("orientation must be -1 or 1")
    if weights is None:
        weights = (1.0,) * len(values)
    if len(values) != len(weights):
        raise ValueError("values and weights must have equal length")
    if any(weight < 0 or not math.isfinite(weight) for weight in weights):
        raise ValueError("weights must be finite and nonnegative")
    return math.fsum(
        weight * max(-orientation * value, 0.0)
        for value, weight in zip(values, weights, strict=True)
    )

