"""Exact diagnostics for the conformal one-cell Pick cusp.

The functions here reproduce identities used in
``ZETA23-CONFORMAL-CUSP-AND-SHALLOW-FAN-PRUNING-2026-08-12.md``.
They are numerical checks, not a proof of the analytic statements.
"""

from __future__ import annotations

import cmath
import math


def contour_h(x: float, d: float, lambda0: float) -> complex:
    """The all-jet contour point for ``-pi < x < pi``."""

    if not (d > 0 and lambda0 > 0 and abs(x) < math.pi):
        raise ValueError("require d, lambda0 > 0 and |x| < pi")
    return (
        -lambda0
        + (2.0 / d) * math.log(math.cos(x / 2.0))
        - 1j * x / d
    )


def cusp_coordinate(h: complex, d: float, lambda0: float) -> complex:
    """Return ``2*exp(d*(h+lambda0)/2)-1``."""

    if not (d > 0 and lambda0 > 0):
        raise ValueError("require d, lambda0 > 0")
    return 2.0 * cmath.exp(d * (complex(h) + lambda0) / 2.0) - 1.0


def half_delay_normalized_margin(
    x: float, depth: float, d: float
) -> float:
    """Normalized phase margin of the half-delay on one phase cell.

    The irrelevant common target factor is removed.  At a node with
    ``h=-depth-i*x/d``, the margin is exactly
    ``exp(d*depth/2)*cos(x/2)``.
    """

    if d <= 0 or depth < 0 or abs(x) > math.pi:
        raise ValueError("require d > 0, depth >= 0 and |x| <= pi")
    return math.exp(d * depth / 2.0) * math.cos(x / 2.0)


def odd_root_fan_max_depth(count: int, d: float, lambda0: float) -> float:
    """Largest scaled depth of the odd root-of-unity contour fan."""

    if count < 1 or count % 2 == 0 or d <= 0 or lambda0 <= 0:
        raise ValueError("count must be positive odd and d, lambda0 positive")
    return lambda0 + (2.0 / d) * math.log(
        1.0 / math.sin(math.pi / (2.0 * count))
    )


def exponential_taylor_tail(radius: float, degree: int) -> float:
    """Elementary upper bound for the complex exponential Taylor tail."""

    if radius < 0 or degree < 0:
        raise ValueError("radius and degree must be nonnegative")
    if radius == 0:
        return 0.0
    log_bound = (
        radius
        + (degree + 1) * math.log(radius)
        - math.lgamma(degree + 2)
    )
    return math.exp(log_bound)


def taylor_degree_for_error(radius: float, tolerance: float) -> int:
    """First degree whose elementary exponential-tail bound meets tolerance."""

    if radius < 0 or not (0 < tolerance < 1):
        raise ValueError("require radius >= 0 and 0 < tolerance < 1")
    degree = 0
    while exponential_taylor_tail(radius, degree) > tolerance:
        degree += 1
    return degree
