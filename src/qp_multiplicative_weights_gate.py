"""Finite algebra for the QP multiplicative-weights/Bessel gate.

The companion report proves exact potential identities and isolates the
missing all-order actual-prime estimate.  This module replays only the
elementary quantitative ledger.  It does not prove QP or a zero-free strip.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


KAPPA_MIN = 0.018030323424358778
KAPPA_MAX = 0.018746369714728765


def _normal_cdf(x: float) -> float:
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def i0_series(x: float, *, tolerance: float = 1.0e-16) -> float:
    """Evaluate ``I_0(x)`` by its positive power series."""

    if tolerance <= 0.0:
        raise ValueError("tolerance must be positive")
    term = 1.0
    total = 1.0
    k = 0
    quarter_x_squared = 0.25 * x * x
    while True:
        k += 1
        term *= quarter_x_squared / (k * k)
        total += term
        if term <= tolerance * total:
            return total
        if k > 10_000:
            raise ArithmeticError("I_0 series did not converge")


def bessel_coefficient_mass(step: float, iterations: int) -> float:
    """Return ``(exp(step)/I_0(step))**iterations``."""

    if step < 0.0 or iterations < 0:
        raise ValueError("step and iterations must be nonnegative")
    return math.exp(iterations * (step - math.log(i0_series(step))))


def orthant_witness_upper_bound(
    epsilon: float, step: float, iterations: int, minimum_base_mass: float
) -> float:
    """Upper bound in the continued-violation formula (1.10)."""

    if epsilon <= 0.0 or step <= 0.0 or iterations < 1:
        raise ValueError("epsilon, step, and iterations must be positive")
    if not 0.0 < minimum_base_mass <= 1.0:
        raise ValueError("minimum_base_mass must lie in (0,1]")
    entropy_tax = math.log(1.0 / minimum_base_mass) / (step * iterations)
    return -epsilon + 0.5 * step + entropy_tax


def sufficient_dichotomy_iterations(epsilon: float, minimum_base_mass: float) -> int:
    """Iterations making the ``step=epsilon/2`` witness at most ``-epsilon/2``."""

    if epsilon <= 0.0:
        raise ValueError("epsilon must be positive")
    if not 0.0 < minimum_base_mass <= 1.0:
        raise ValueError("minimum_base_mass must lie in (0,1]")
    return math.ceil(8.0 * math.log(1.0 / minimum_base_mass) / epsilon**2)


POISSON_TAIL_EXPONENT = 4.0 * (math.log(4.0) - 1.0)


@dataclass(frozen=True)
class ScalarBesselFloor:
    normalized_lower_bound: float
    coefficient_mass: float
    scalar_error: float
    poisson_tail_error: float
    effective_order: float


def scalar_bessel_floor(delta: float, step: float, iterations: int) -> ScalarBesselFloor:
    """Replay the lower bound (4.5).

    It assumes the scalar characteristic-function floor ``Phi(v)>=-delta``
    through combination height ``4*step*iterations*B``.
    """

    if not 0.0 <= delta <= 1.0:
        raise ValueError("delta must lie in [0,1]")
    if step <= 0.0 or iterations < 1:
        raise ValueError("step and iterations must be positive")
    effective_order = step * iterations
    mass = bessel_coefficient_mass(step, iterations)
    scalar_error = delta * (mass - 1.0)
    tail_error = math.exp(-POISSON_TAIL_EXPONENT * effective_order)
    return ScalarBesselFloor(
        normalized_lower_bound=1.0 - scalar_error - tail_error,
        coefficient_mass=mass,
        scalar_error=scalar_error,
        poisson_tail_error=tail_error,
        effective_order=effective_order,
    )


def i0_normalized_halfspace_limit(a: float) -> float:
    """Limit in report formula (6.6) for the conditioned torus model."""

    if a < 0.0:
        raise ValueError("a must be nonnegative")
    return _normal_cdf(-math.sqrt(2.0) - a / math.sqrt(2.0)) / _normal_cdf(
        -math.sqrt(2.0)
    )


def exponent_gap() -> float:
    """Return the strict gap between the KILL and PROMOTE ledgers."""

    return KAPPA_MAX - KAPPA_MIN

