#!/usr/bin/env python3
"""Finite replay helpers for the Jordan/filter novelty audit.

The analytic theorems live in the accompanying report.  This module only
checks their finite algebraic witnesses:

* causal box filters have multiplier ``(1-exp(-L*s))/s``;
* an alternating exponential sine has large fixed-sign Jordan masses even
  though a block-adaptive sign can choose zero on every block;
* cellwise constant masks approximate the negative mass of a Lipschitz
  piecewise-linear function with error at most ``L*mesh*length/2``;
* multiplier zero order, rather than merely the common zero set, determines
  how much of a source pole survives; and
* increasing endpoint order can insert an exponential attenuation which a
  fixed-filter Landau theorem cannot see.

Nothing here proves an asymptotic prime estimate or a zero-free region.
"""

from __future__ import annotations

import cmath
import math
from collections.abc import Sequence


def causal_box_multiplier(s: complex, length: float = 1.0) -> complex:
    """Return the Laplace multiplier of ``1_[0,length]``.

    The removable value at ``s=0`` is filled continuously.  Its nonzero
    zeros are ``2*pi*i*k/length``, so it has no zeros in ``Re(s)>0``.
    """

    if not math.isfinite(length) or length <= 0.0:
        raise ValueError("length must be finite and positive")
    point = complex(s)
    if point == 0:
        return complex(length)
    return (1.0 - cmath.exp(-length * point)) / point


def exp_sine_unit_masses(theta: float, block: int) -> tuple[float, float]:
    r"""Return the exact positive/negative masses of
    ``exp(theta*t)*sin(pi*t)`` on ``[block,block+1]``.

    Sine has one sign on each open integer block.  Hence precisely one entry
    is zero, while the nonzero mass is

    ``exp(theta*block)*pi*(1+exp(theta))/(theta**2+pi**2)``.
    """

    if not math.isfinite(theta):
        raise ValueError("theta must be finite")
    if type(block) is not int or block < 0:
        raise ValueError("block must be a nonnegative integer")
    mass = (
        math.exp(theta * block)
        * math.pi
        * (1.0 + math.exp(theta))
        / (theta * theta + math.pi * math.pi)
    )
    return (mass, 0.0) if block % 2 == 0 else (0.0, mass)


def alternating_exp_transform(s: complex, theta: float) -> complex:
    r"""Laplace transform of ``(-1)^floor(t) exp(theta*t)``.

    It equals ``tanh((s-theta)/2)/(s-theta)`` with removable value ``1/2``
    at ``s=theta``.  Its nonreal poles lie on ``Re(s)=theta``.
    """

    if not math.isfinite(theta):
        raise ValueError("theta must be finite")
    z = complex(s) - theta
    if z == 0:
        return 0.5 + 0.0j
    return cmath.tanh(z / 2.0) / z


def pole_survival_order(
    source_pole_order: int, multiplier_zero_orders: Sequence[int]
) -> int:
    """Largest pole order retained by a finite filter bank.

    A negative zero order is invalid.  The value is
    ``max(source_pole_order - min(zero_orders), 0)``.  An empty bank retains
    nothing and therefore returns zero.
    """

    if type(source_pole_order) is not int or source_pole_order < 0:
        raise ValueError("source pole order must be a nonnegative integer")
    if any(type(order) is not int or order < 0 for order in multiplier_zero_orders):
        raise ValueError("multiplier zero orders must be nonnegative integers")
    if not multiplier_zero_orders:
        return 0
    return max(source_pole_order - min(multiplier_zero_orders), 0)


def endpoint_flat_log_abs_multiplier(
    order: int, s: complex, *, factorial_normalized: bool = False
) -> float:
    r"""Logarithmic magnitude of the endpoint-flat Mellin multiplier.

    For fixed ``s`` away from its zeros and poles,

    ``H_r(s)=(s-1)*Gamma(s)/Gamma(s+r+2)``.

    The implementation uses a direct logarithmic product, avoiding overflow.
    If ``factorial_normalized`` is true it returns the magnitude after
    multiplication by ``(r+1)!``.
    """

    if type(order) is not int or order < 0:
        raise ValueError("order must be a nonnegative integer")
    point = complex(s)
    if point == 1 or any(point == -index for index in range(order + 2)):
        raise ValueError("evaluation point is a multiplier zero or pole")
    value = math.log(abs(point - 1.0))
    value -= math.fsum(math.log(abs(point + index)) for index in range(order + 2))
    if factorial_normalized:
        value += math.lgamma(order + 2)
    return value


def piecewise_linear_negative_mass(
    nodes: Sequence[float], values: Sequence[float]
) -> float:
    """Integrate the negative part of a piecewise-linear function exactly."""

    _validate_piecewise_linear(nodes, values)
    total = 0.0
    for left, right, a, b in zip(nodes, nodes[1:], values, values[1:]):
        width = right - left
        if a <= 0.0 and b <= 0.0:
            total += -0.5 * (a + b) * width
        elif a < 0.0 < b:
            negative_width = width * (-a) / (b - a)
            total += -0.5 * a * negative_width
        elif b < 0.0 < a:
            negative_width = width * (-b) / (a - b)
            total += -0.5 * b * negative_width
    return total


def grid_mask_negative_proxy(
    nodes: Sequence[float], values: Sequence[float]
) -> float:
    r"""Best negative integral selected by whole-cell ``{0,1}`` masks.

    Each interval between consecutive nodes is one mask cell.  Since the
    function is linear there, its integral is the trapezoid area.
    """

    _validate_piecewise_linear(nodes, values)
    return math.fsum(
        max(-0.5 * (a + b) * (right - left), 0.0)
        for left, right, a, b in zip(nodes, nodes[1:], values, values[1:])
    )


def piecewise_linear_lipschitz(
    nodes: Sequence[float], values: Sequence[float]
) -> float:
    """Return the exact Lipschitz constant of a piecewise-linear function."""

    _validate_piecewise_linear(nodes, values)
    return max(
        abs(b - a) / (right - left)
        for left, right, a, b in zip(nodes, nodes[1:], values, values[1:])
    )


def _validate_piecewise_linear(
    nodes: Sequence[float], values: Sequence[float]
) -> None:
    if len(nodes) != len(values) or len(nodes) < 2:
        raise ValueError("nodes and values must have the same length at least two")
    if any(not math.isfinite(float(item)) for item in (*nodes, *values)):
        raise ValueError("nodes and values must be finite")
    if any(right <= left for left, right in zip(nodes, nodes[1:])):
        raise ValueError("nodes must be strictly increasing")
