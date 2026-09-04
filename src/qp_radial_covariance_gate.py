"""Arithmetic ledger for cross-side collisions in the QP radial gate.

For ``n < Y < m`` the absolute logarithmic frequencies satisfy

    ||log(n/Y)| - |log(m/Y)|| = |log(n*m/Y**2)|.

Thus a collision at Fourier resolution ``kappa / B`` forces the integer
product ``n*m`` into a short interval about ``Y**2``.  The routines below
replay that exact reduction and the exponent ledger used in the accompanying
audit.  They do not assert that LTRAD is proved.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable

import numpy as np


def near_pair_exponent(aperture_exponent: float) -> float:
    """Exponent of the product-window count ``Y**(2-A+o(1))``."""

    return 2.0 - aperture_exponent


def long_event_exponent(depth_exponent: float) -> float:
    """Minimum carrier exponent forced by mass depth ``Y**(-d)``."""

    return 1.0 - depth_exponent


def collision_survival_gap(aperture_exponent: float, depth_exponent: float) -> float:
    """Power gap between a Turan-long carrier and collision endpoints."""

    return aperture_exponent - 1.0 - depth_exponent


def product_window(Y: float, B: float, kappa: float = 1.0) -> tuple[int, int]:
    """Inclusive integer window forced by ``|log(k/Y^2)| <= kappa/B``."""

    if Y <= 0.0 or B <= 0.0 or kappa < 0.0:
        raise ValueError("Y and B must be positive and kappa nonnegative")
    epsilon = kappa / B
    lower = math.ceil(Y * Y * math.exp(-epsilon))
    upper = math.floor(Y * Y * math.exp(epsilon))
    return lower, upper


def divisor_count(number: int) -> int:
    """Return the exact positive-divisor count of ``number``."""

    if number <= 0:
        raise ValueError("number must be positive")
    remaining = number
    count = 1
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            count *= exponent + 1
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        count *= 2
    return count


def all_integer_factor_pair_bound(Y: float, B: float, kappa: float = 1.0) -> int:
    """Upper-bound ordered cross-side pairs by all integer factor pairs.

    Summing ``d(k)`` over the forced product window counts every possible
    ordered factorization ``k=n*m`` and hence dominates any prime-power
    subfamily.
    """

    lower, upper = product_window(Y, B, kappa)
    if upper < lower:
        return 0
    return sum(divisor_count(number) for number in range(lower, upper + 1))


def near_reflection_pairs(
    values: Iterable[int], Y: float, B: float, kappa: float = 1.0
) -> tuple[tuple[int, int], ...]:
    """Enumerate exact cross-side pairs at logarithmic resolution kappa/B."""

    if Y <= 0.0 or B <= 0.0 or kappa < 0.0:
        raise ValueError("invalid collision parameters")
    unique = sorted(set(int(value) for value in values))
    below = [value for value in unique if 0 < value < Y]
    above = [value for value in unique if value > Y]
    tolerance = kappa / B
    pairs: list[tuple[int, int]] = []
    for left in below:
        u_left = math.log(Y / left)
        for right in above:
            u_right = math.log(right / Y)
            if abs(u_left - u_right) <= tolerance:
                pairs.append((left, right))
    return tuple(pairs)


def collision_endpoints(pairs: Iterable[tuple[int, int]]) -> frozenset[int]:
    """Return the set of coordinates touched by collision pairs."""

    return frozenset(value for pair in pairs for value in pair)


def cleaned_negative_sum_lower(original_negative_sum: float, removed_count: int) -> float:
    """Worst-case negative sum after deleting ``removed_count`` unit atoms."""

    if removed_count < 0:
        raise ValueError("removed_count must be nonnegative")
    return original_negative_sum - float(removed_count)


def positive_range_lower(second_moment: float, sup_abs: float, mean_abs: float) -> float:
    """Lower bound for the positive range used in the cluster-frame proof.

    If a real random variable ``F`` obeys ``|F| <= U``, has second moment
    ``Q``, and ``|E F| <= m``, then the range inequality in the report gives

        sup F >= (Q - U*m) / (U - m).

    The formula is useful only when ``U*m < Q`` and ``m < U``; invalid
    inputs are rejected rather than silently producing a negative bound.
    """

    if second_moment <= 0.0 or sup_abs <= 0.0 or mean_abs < 0.0:
        raise ValueError("require Q>0, U>0, and m>=0")
    if mean_abs >= sup_abs or sup_abs * mean_abs >= second_moment:
        raise ValueError("range inequality requires m<U and U*m<Q")
    return (second_moment - sup_abs * mean_abs) / (sup_abs - mean_abs)


def sampled_pair_block_gram(z: float) -> np.ndarray:
    """A finite positive-variance check of the normalized two-cluster block.

    This diagnostic uses four equally weighted points in ``(1/3,2/3)``.
    The second normalized basis function is ``i sin(z*x/2)/z``, with its
    continuous value ``i*x/2`` at zero.
    """

    if not 0.0 <= z <= 1.0:
        raise ValueError("the normalized check expects 0 <= z <= 1")
    points = np.array([0.36, 0.45, 0.55, 0.64], dtype=float)
    first = np.cos(0.5 * z * points).astype(complex)
    if z == 0.0:
        second = 0.5j * points
    else:
        second = 1j * np.sin(0.5 * z * points) / z
    basis = np.vstack([first, second])
    return (basis.conj() @ basis.T) / float(len(points))


def fejer_kernel(order: int, angle: np.ndarray | float) -> np.ndarray:
    """Evaluate ``1+2 sum_(j<m)(1-j/m) cos(j*x)``."""

    if order < 2:
        raise ValueError("order must be at least two")
    angles = np.asarray(angle, dtype=float)
    result = np.ones_like(angles)
    for index in range(1, order):
        result += 2.0 * (1.0 - index / order) * np.cos(index * angles)
    return result


def fejer_transverse_dual(order: int, angle: np.ndarray | float) -> np.ndarray:
    """Evaluate the sharp model dual ``(1-K_m)/(2(m-1))``."""

    return (1.0 - fejer_kernel(order, angle)) / (2.0 * (order - 1))


@dataclass(frozen=True)
class CollisionExponentLedger:
    aperture_exponent: float
    depth_exponent: float
    collision_pair_exponent: float
    collision_endpoint_exponent: float
    long_carrier_exponent: float
    survival_gap: float
    survives: bool


def exponent_ledger(aperture_exponent: float, depth_exponent: float) -> CollisionExponentLedger:
    """Return the asymptotic collision-deletion ledger."""

    collision = near_pair_exponent(aperture_exponent)
    long_carrier = long_event_exponent(depth_exponent)
    gap = collision_survival_gap(aperture_exponent, depth_exponent)
    return CollisionExponentLedger(
        aperture_exponent=aperture_exponent,
        depth_exponent=depth_exponent,
        collision_pair_exponent=collision,
        collision_endpoint_exponent=collision,
        long_carrier_exponent=long_carrier,
        survival_gap=gap,
        survives=gap > 0.0,
    )
