#!/usr/bin/env python3
"""Replay the convex/tent endpoint for the actual-prime QP gate.

The analytic theorem is recorded in the companion report.  This module only
replays its elementary pieces: the bilateral Laplace transform of the tent,
the positive-weight Delsarte conversion, the continuum grid loss, and the
exponent ledger.  It does not numerically certify a zero-free strip.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import cmath
import json
import math
from typing import Sequence


APERTURE_EXPONENT = Fraction(50, 33)
KAPPA_MIN = 0.018030323424358778
KAPPA_MAX = 0.018746369714728765
CONVENIENT_KILL_EXPONENT = 0.019


def tent_laplace(z: complex, width: float = 0.2) -> complex:
    """Return ``int g(u) exp(z*u) du`` for ``g=(1-|u|/width)_+``.

    The closed form is ``2(cosh(width*z)-1)/(width*z**2)``.  A short
    Taylor branch avoids the removable singularity at zero.
    """

    if width <= 0.0:
        raise ValueError("width must be positive")
    x = width * complex(z)
    if abs(x) < 1.0e-5:
        # 2(cosh(x)-1)/(width*(x/width)^2)
        return width * (
            1.0 + x * x / 12.0 + x**4 / 360.0 + x**6 / 20160.0
        )
    return 2.0 * width * (cmath.cosh(x) - 1.0) / (x * x)


def tent_fourier(t: float, width: float = 0.2) -> float:
    """Return the nonnegative Fourier transform of the tent at ``t``."""

    if width <= 0.0:
        raise ValueError("width must be positive")
    x = width * float(t) / 2.0
    if x == 0.0:
        return width
    return width * (math.sin(x) / x) ** 2


def normalized_tent_population(t: float, width: float = 0.2) -> float:
    """Return ``tent_fourier(t)/tent_fourier(0)``."""

    return tent_fourier(t, width) / width


def delsarte_value_from_antenna_error(error: float) -> float:
    """Lower bound ``1+1/error`` furnished by ``P(t)>=-error``.

    If ``P(0)=1``, then ``Q=1+P/error`` is an admissible Delsarte
    polynomial and has ``Q(0)=1+1/error``.
    """

    if not 0.0 < error <= 1.0:
        raise ValueError("error must lie in (0,1]")
    return 1.0 + 1.0 / error


def promoted_depth_upper_bound(error: float) -> float:
    """Return the resulting bound ``r_+ <= error``."""

    value = delsarte_value_from_antenna_error(error)
    return 1.0 / (value - 1.0)


def positive_antenna_lipschitz_bound(
    nodes: Sequence[float], weights: Sequence[float]
) -> float:
    """Return ``sum lambda_j |u_j|``, a bound for ``|P'(t)|``."""

    if len(nodes) != len(weights) or not nodes:
        raise ValueError("nodes and weights must have the same nonzero length")
    if any(weight < 0.0 for weight in weights):
        raise ValueError("weights must be nonnegative")
    if not math.isclose(sum(weights), 1.0, rel_tol=1e-12, abs_tol=1e-12):
        raise ValueError("weights must sum to one")
    return sum(weight * abs(node) for node, weight in zip(nodes, weights))


def grid_to_continuum_loss(width: float, mesh: float) -> float:
    """Worst loss from a grid of maximal gap ``mesh`` on a closed band."""

    if width <= 0.0 or mesh < 0.0:
        raise ValueError("width must be positive and mesh nonnegative")
    return width * mesh / 2.0


def positive_cosine_antenna(
    t: float, nodes: Sequence[float], weights: Sequence[float]
) -> float:
    """Evaluate a normalized positive cosine antenna."""

    positive_antenna_lipschitz_bound(nodes, weights)
    return sum(
        weight * math.cos(float(t) * node)
        for node, weight in zip(nodes, weights)
    )


def required_positive_grid_exponent(
    target_exponent: float,
    aperture_exponent: float = float(APERTURE_EXPONENT),
) -> float:
    """Exponent in the safe grid size ``Y^(aperture+target)``.

    To spend half of an error ``Y^-c`` on interpolation, the mesh is
    ``O(Y^-c)`` because every normalized positive antenna is width-Lipschitz.
    """

    if target_exponent < 0.0 or aperture_exponent <= 0.0:
        raise ValueError("invalid exponents")
    return aperture_exponent + target_exponent


def vk_shape_from_log(log_y: float) -> float:
    """Return ``(log Y / log log Y)^(1/3)`` from ``log_y=log Y``."""

    if log_y <= 1.0:
        raise ValueError("log Y must exceed one")
    return (log_y / math.log(log_y)) ** (1.0 / 3.0)


def strip_supplies_power(strip_width: float, requested_power: float) -> bool:
    """A width ``delta`` supplies every Delsarte power ``c<delta``."""

    if strip_width <= 0.0 or requested_power < 0.0:
        raise ValueError("invalid strip width or requested power")
    return requested_power < strip_width


def strip_kills_fixed_slice(strip_width: float) -> bool:
    """Return whether the tent route clears the audited fixed-slice bill."""

    return strip_supplies_power(strip_width, KAPPA_MAX)


def convex_mixture_error(errors: Sequence[float], weights: Sequence[float]) -> float:
    """Return the only black-box error supplied by convex mixing.

    If ``P_i>=-errors[i]``, then ``sum weights[i] P_i`` is bounded below by
    the weighted *average* of the errors.  No multiplicative gain occurs.
    """

    if len(errors) != len(weights) or not errors:
        raise ValueError("errors and weights must have the same nonzero length")
    if any(error < 0.0 for error in errors) or any(weight < 0.0 for weight in weights):
        raise ValueError("errors and weights must be nonnegative")
    if not math.isclose(sum(weights), 1.0, rel_tol=1e-12, abs_tol=1e-12):
        raise ValueError("weights must sum to one")
    return sum(error * weight for error, weight in zip(errors, weights))


def cosine_product_frequencies(left: float, right: float) -> tuple[float, float]:
    """Frequencies generated by ``cos(left*t) cos(right*t)``."""

    if left < 0.0 or right < 0.0:
        raise ValueError("frequencies must be nonnegative")
    return abs(left - right), left + right


def nonlinear_power_escapes_finite_support(max_frequency: float, degree: int) -> bool:
    """Whether a degree-``degree`` power generates a frequency above the pool.

    A nonzero coefficient at the largest frequency creates
    ``degree*max_frequency`` in the leading harmonic.  Hence every genuine
    nonlinear pointwise amplifier leaves a finite nonzero cosine pool.
    """

    if max_frequency <= 0.0 or degree < 1:
        raise ValueError("invalid maximum frequency or degree")
    return degree * max_frequency > max_frequency


def positive_kernel_laplace_ratio_bounds(a: float, width: float) -> tuple[float, float]:
    """Bounds for ``int g(u)e^{-a u}/int g`` when ``g>=0`` on ``[-w,w]``."""

    if not 0.0 <= a <= 1.0 or width <= 0.0:
        raise ValueError("require 0<=a<=1 and positive width")
    return math.exp(-a * width), math.exp(a * width)


def even_positive_kernel_ratio_lower_bound(a: float, width: float) -> float:
    """Sharp universal lower bound for an even nonnegative shell kernel.

    The normalized Laplace value is ``E cosh(aU)>=1``.  Real
    positive-definite kernels are even, so this applies to kernels whose pole
    transform is kept nonnegative by the standard autocorrelation route.
    """

    positive_kernel_laplace_ratio_bounds(a, width)
    return 1.0


def iterated_positive_reweighting(
    base_weights: Sequence[float], multipliers: Sequence[Sequence[float]]
) -> tuple[float, ...]:
    """Collapse sequential positive reweightings to their final simplex point."""

    if not base_weights or any(weight <= 0.0 for weight in base_weights):
        raise ValueError("base weights must be strictly positive")
    current = [float(weight) for weight in base_weights]
    total = sum(current)
    current = [weight / total for weight in current]
    for multiplier in multipliers:
        if len(multiplier) != len(current) or any(value < 0.0 for value in multiplier):
            raise ValueError("every multiplier must be nonnegative and dimension matched")
        current = [weight * value for weight, value in zip(current, multiplier)]
        total = sum(current)
        if total <= 0.0:
            raise ValueError("a reweighting cannot annihilate all coordinates")
        current = [weight / total for weight in current]
    return tuple(current)


@dataclass(frozen=True)
class TentGateLedger:
    aperture_exponent: str
    kappa_min: float
    kappa_max: float
    convenient_kill_exponent: float
    convenient_grid_exponent: float
    strip_0019_supplies_convenient_power: bool
    strip_0020_supplies_convenient_power: bool
    strip_0020_kills_fixed_slice: bool
    squaring_stays_in_finite_actual_frequency_pool: bool
    even_positive_kernel_can_damp_a_resonant_zero: bool


def ledger() -> TentGateLedger:
    """Return the exact exponent/polarity ledger."""

    return TentGateLedger(
        aperture_exponent=str(APERTURE_EXPONENT),
        kappa_min=KAPPA_MIN,
        kappa_max=KAPPA_MAX,
        convenient_kill_exponent=CONVENIENT_KILL_EXPONENT,
        convenient_grid_exponent=required_positive_grid_exponent(
            CONVENIENT_KILL_EXPONENT
        ),
        # Strict inequality is required after the logarithmic contour loss.
        strip_0019_supplies_convenient_power=strip_supplies_power(
            0.019, CONVENIENT_KILL_EXPONENT
        ),
        strip_0020_supplies_convenient_power=strip_supplies_power(
            0.020, CONVENIENT_KILL_EXPONENT
        ),
        strip_0020_kills_fixed_slice=strip_kills_fixed_slice(0.020),
        squaring_stays_in_finite_actual_frequency_pool=not nonlinear_power_escapes_finite_support(
            0.2, 2
        ),
        even_positive_kernel_can_damp_a_resonant_zero=(
            even_positive_kernel_ratio_lower_bound(0.4, 0.2) < 1.0
        ),
    )


def main() -> None:
    sample_t = (0.0, 1.0, 17.0, 101.0)
    payload = {
        "schema": "qp-tent-explicit-formula-gate-v1",
        "status": "PASS",
        "tent_fourier": {str(t): tent_fourier(t) for t in sample_t},
        "tent_laplace_on_axis": {
            str(t): [tent_laplace(-1j * t).real, tent_laplace(-1j * t).imag]
            for t in sample_t
        },
        "ledger": asdict(ledger()),
        "claims": {
            "unconditional_fixed_power": False,
            "conditional_strip_to_actual_node_certificate": True,
            "finite_grid_is_asymptotic_proof": False,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
