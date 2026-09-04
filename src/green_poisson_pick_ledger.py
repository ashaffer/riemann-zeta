"""Reproducible constants for the Green--Poisson Pick ledger.

This module only evaluates the elementary one-variable expressions proved in
the accompanying theorem cards.  It is not a zero-free-region computation.
"""

from __future__ import annotations

import math


def green_majorant(v: float) -> float:
    """g(v) = (1/2) log(1 + v^{-2}) for v > 0."""

    if v <= 0.0:
        raise ValueError("v must be positive")
    return 0.5 * math.log1p(1.0 / (v * v))


def poisson_branch_zero(v: float) -> float:
    """The b=0 branch at x=0.9, A=0.5."""

    return 1.8 / (0.81 + v * v)


def poisson_branch_edge(v: float) -> float:
    """The b=A branch at x=0.9, A=0.5."""

    vv = v * v
    return 0.4 / (0.16 + vv) + 1.4 / (1.96 + vv)


def poisson_minorant(v: float) -> float:
    return min(poisson_branch_zero(v), poisson_branch_edge(v))


def kernel_switch() -> float:
    """The exact crossing sqrt((x^2-A^2)/3), x=.9, A=.5."""

    return math.sqrt(0.56 / 3.0)


def positive_root(lam: float = 0.304) -> float:
    """Locate the positive root of g(v)-lam*k(v) after the switch."""

    lo = kernel_switch()
    hi = 4.0

    def residual(v: float) -> float:
        return green_majorant(v) - lam * poisson_minorant(v)

    if residual(lo) <= 0.0 or residual(hi) >= 0.0:
        raise ArithmeticError("root bracket failed")
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if residual(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def _green_primitive(v: float) -> float:
    return 0.5 * v * math.log1p(1.0 / (v * v)) + math.atan(v)


def _zero_primitive(v: float) -> float:
    return 2.0 * math.atan(v / 0.9)


def _edge_primitive(v: float) -> float:
    return math.atan(v / 0.4) + math.atan(v / 1.4)


def positive_part_integral(lam: float = 0.304) -> float:
    """Integral over R of [g-lam*k]_+ using the proved two branches."""

    switch = kernel_switch()
    root = positive_root(lam)
    half = (
        _green_primitive(switch)
        - lam * _zero_primitive(switch)
        + _green_primitive(root)
        - _green_primitive(switch)
        - lam * (_edge_primitive(root) - _edge_primitive(switch))
    )
    return 2.0 * half


def conditional_green_bill(d: float = 0.66, lam: float = 0.304) -> float:
    """Coefficient of L in the one-representative Green bill."""

    return lam / 2.0 + d * positive_part_integral(lam) / (2.0 * math.pi)


def reflected_pair_cap(
    c: float,
    padding: float = 0.003,
    *,
    d: float = 0.66,
    b0: float = 0.49,
    b1: float = 0.49,
) -> float:
    """Right side of the integrated reflected-pair count, divided by L."""

    width = c * math.pi / d
    a_right = 0.5 - b0
    a_left = 0.5 + b1
    angle_sum = sum(
        math.atan((width + padding) / a) + math.atan(padding / a)
        for a in (a_right, a_left)
    )
    return (width + 2.0 * padding) / (2.0 * angle_sum)


def count_compatible_c(padding: float = 0.003) -> float:
    """Solve 2c = reflected_pair_cap(c) by bisection."""

    lo, hi = 0.0, 0.02
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if 2.0 * mid <= reflected_pair_cap(mid, padding):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def binomial_screen_exponent(
    c: float, *, alpha: float = 0.49, d: float = 0.66
) -> float:
    """F(c)=c log(alpha*d/(2*pi*c))."""

    if c <= 0.0:
        return 0.0
    return c * math.log(alpha * d / (2.0 * math.pi * c))

