#!/usr/bin/env python3
"""Algebraic probe for the proportional-order B-spline detector bank.

For the fixed-step compact window, set

    alpha_h(s) = (exp(h*s) - 1) / (h*s),
    beta_h(s)  = (1 - exp(-h*s)) / (h*s).

The unnormalized order-k coboundary multiplier factors exactly as

    (alpha_h(s)**k - beta_h(s)**k) / s.

At the proportional scale ``R = k / slope`` this becomes a difference of
two pure k-th powers.  The resulting bases compactify the vertical zero
spectrum.  This module checks that algebra and the elementary exponent
calculus used in ``PROPORTIONAL-ORDER-DETECTOR-BANK-GATE.md``.  It is a
diagnostic, not a zero-free-region computation.
"""

from __future__ import annotations

import argparse
import cmath
import math
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class SpectralNode:
    """A synthetic shifted zero ``s = displacement + i*ordinate``."""

    displacement: float
    ordinate: float

    @property
    def value(self) -> complex:
        return complex(self.displacement, self.ordinate)


def _validate_h(h: float) -> None:
    if not math.isfinite(h) or h <= 0.0:
        raise ValueError("h must be finite and positive")


def _validate_slope(slope: float, h: float) -> None:
    _validate_h(h)
    if not math.isfinite(slope) or slope <= 0.0 or slope * h >= 1.0:
        raise ValueError("slope must satisfy 0 < slope*h < 1")


def _complex_expm1(z: complex) -> complex:
    """Return ``exp(z)-1`` without cancellation for small complex ``z``."""

    if abs(z) >= 1.0e-5:
        return cmath.exp(z) - 1.0
    term = z
    total = z
    for denominator in range(2, 12):
        term *= z / denominator
        total += term
    return total


def alpha_h(s: complex, h: float) -> complex:
    """Return ``(exp(h*s)-1)/(h*s)`` with a stable value at zero."""

    _validate_h(h)
    z = h * complex(s)
    if z == 0.0:
        return 1.0 + 0.0j
    return _complex_expm1(z) / z


def beta_h(s: complex, h: float) -> complex:
    """Return ``(1-exp(-h*s))/(h*s) = exp(-h*s)*alpha_h(s)``."""

    _validate_h(h)
    z = h * complex(s)
    if z == 0.0:
        return 1.0 + 0.0j
    return -_complex_expm1(-z) / z


def factorized_coboundary_multiplier(s: complex, h: float, order: int) -> complex:
    """Return the exact unnormalized compact-window multiplier."""

    _validate_h(h)
    if not isinstance(order, int) or isinstance(order, bool) or order <= 0:
        raise ValueError("order must be a positive integer")
    value = complex(s)
    if value == 0.0:
        return complex(order * h)
    return (alpha_h(value, h) ** order - beta_h(value, h) ** order) / value


def tilted_bases(s: complex, h: float, slope: float) -> tuple[complex, complex]:
    """Return the two bases at ``R=order/slope``."""

    _validate_slope(slope, h)
    value = complex(s)
    carrier = cmath.exp(value / slope)
    return carrier * alpha_h(value, h), carrier * beta_h(value, h)


def tilted_rate(s: complex, h: float, slope: float) -> float:
    """Return the largest logarithmic amplitude per unit log-scale R."""

    _validate_slope(slope, h)
    value = complex(s)
    one_step = max(abs(alpha_h(value, h)), abs(beta_h(value, h)))
    if one_step == 0.0:
        return -math.inf
    return value.real + slope * math.log(one_step)


def raw_bank_rate(nodes: Iterable[SpectralNode], h: float, slope: float) -> float:
    """Return the raw tilted spectral rate of a finite synthetic divisor."""

    rates = [tilted_rate(node.value, h, slope) for node in nodes]
    if not rates:
        raise ValueError("at least one spectral node is required")
    return max(rates)


def dyadic_orders(log_scale: float, maximum_slope: float, h: float) -> tuple[int, ...]:
    """Return distinct positive orders ``floor(maximum_slope*R/2**j)``."""

    _validate_slope(maximum_slope, h)
    if not math.isfinite(log_scale) or log_scale <= 0.0:
        raise ValueError("log_scale must be finite and positive")
    orders: list[int] = []
    index = 0
    while True:
        order = math.floor(maximum_slope * log_scale / (2.0**index))
        if order < 1:
            break
        if not orders or order != orders[-1]:
            orders.append(order)
        index += 1
    return tuple(orders)


def vk_shell_scale(slope: float) -> float:
    """Return the VK optimizer ``y ~ slope^(-3/5) log(1/slope)^(-1/5)``."""

    if not math.isfinite(slope) or not 0.0 < slope < 1.0:
        raise ValueError("slope must lie in (0,1)")
    logarithm = math.log(math.e / slope)
    return slope ** (-3.0 / 5.0) * logarithm ** (-1.0 / 5.0)


def vk_tilted_saving(slope: float) -> float:
    """Return the corresponding rate scale ``slope*y``."""

    return slope * vk_shell_scale(slope)


def retreated_cutoff_theta(
    log_scale: float,
    order: int,
    a_zero: float,
    retreat: float,
) -> float:
    """Return ``a_zero/order + retreat*order/log_scale`` from Theorem 7.1."""

    if not math.isfinite(log_scale) or log_scale <= 0.0:
        raise ValueError("log_scale must be finite and positive")
    if not isinstance(order, int) or isinstance(order, bool) or order <= 0:
        raise ValueError("order must be a positive integer")
    if not 0.5 < a_zero < 1.0:
        raise ValueError("a_zero must lie in (1/2,1)")
    if not math.isfinite(retreat) or retreat <= 0.0:
        raise ValueError("retreat must be finite and positive")
    return a_zero / order + retreat * order / log_scale


def retreated_support_margin(
    log_scale: float,
    order: int,
    h: float,
    a_zero: float,
    retreat: float,
) -> float:
    """Return ``theta*R-h*k``; nonnegative means the support gate holds."""

    _validate_h(h)
    theta = retreated_cutoff_theta(log_scale, order, a_zero, retreat)
    return theta * log_scale - h * order


def retreated_uv_error_exponent(
    log_scale: float,
    order: int,
    a_zero: float,
    retreat: float,
    euler_constant: float,
) -> float:
    """Return the displayed dominant exponent before lower-order terms."""

    if not math.isfinite(euler_constant) or euler_constant < 0.0:
        raise ValueError("euler_constant must be finite and nonnegative")
    theta = retreated_cutoff_theta(log_scale, order, a_zero, retreat)
    return (
        euler_constant * order * order
        + (0.5 - (order + 1) * theta) * log_scale
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h", type=float, default=0.1)
    parser.add_argument("--slope", type=float, default=0.02)
    parser.add_argument("--order", type=int, default=20)
    parser.add_argument("--delta", type=float, default=0.1)
    parser.add_argument("--gamma", type=float, default=14.134725141734695)
    args = parser.parse_args()

    node = complex(args.delta, args.gamma)
    z_value, w_value = tilted_bases(node, args.h, args.slope)
    multiplier = factorized_coboundary_multiplier(node, args.h, args.order)
    direct = cmath.exp(node * args.order / args.slope) * multiplier
    powers = (z_value**args.order - w_value**args.order) / node

    print(f"alpha={alpha_h(node, args.h)!r}")
    print(f"beta={beta_h(node, args.h)!r}")
    print(f"z={z_value!r} |z|={abs(z_value):.12g}")
    print(f"w={w_value!r} |w|={abs(w_value):.12g}")
    print(f"tilted_rate={tilted_rate(node, args.h, args.slope):.12g}")
    print(f"factorization_error={abs(direct-powers):.12g}")
    print(f"vk_shell_scale={vk_shell_scale(args.slope):.12g}")
    print(f"vk_tilted_saving={vk_tilted_saving(args.slope):.12g}")


if __name__ == "__main__":
    main()
