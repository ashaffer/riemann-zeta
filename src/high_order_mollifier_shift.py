#!/usr/bin/env python3
"""Finite ledger for proportional-order logarithmic mollifier weights.

This module proves no zero-free region.  It records the exact tradeoff that
appears when the logarithmic cutoff order grows like ``alpha * log(Y)``:

* fixed coefficients converge to a horizontally shifted reciprocal weight
  ``d**(-alpha)``;
* a formal zero-residue contribution has exponential rate
  ``delta + alpha * (log(alpha / delta) - 1)``;
* this rate is nonnegative and vanishes only at ``delta = alpha``.

The last item is a contour-ledger statement, not a lower bound: in the
absolute-convergence regime the remaining contour must cancel the isolated
residue at the same exponential scale.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class ProportionalOrderLedger:
    """Parameters for a logarithmic cutoff of order about ``alpha log(Y)``."""

    scale: float
    alpha: float
    order: int
    order_over_log_scale: float
    shifted_real_part: float


def _require_finite_positive(value: float, name: str) -> None:
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and strictly positive")


def proportional_order(scale: float, alpha: float) -> ProportionalOrderLedger:
    """Choose ``k = ceil(alpha * log(scale))`` for ``scale > 1``."""

    if not math.isfinite(scale) or scale <= 1.0:
        raise ValueError("scale must be finite and strictly greater than one")
    _require_finite_positive(alpha, "alpha")
    logarithm = math.log(scale)
    order = max(1, math.ceil(alpha * logarithm))
    return ProportionalOrderLedger(
        scale=scale,
        alpha=alpha,
        order=order,
        order_over_log_scale=order / logarithm,
        shifted_real_part=0.5 + alpha,
    )


def logarithmic_cutoff_weight(scale: float, divisor: int, order: int) -> float:
    r"""Return ``1_(d<=Y) (log(Y/d)/log(Y))^k``.

    ``order=0`` is allowed and gives the sharp cutoff weight on ``d<=Y``.
    """

    if not math.isfinite(scale) or scale <= 1.0:
        raise ValueError("scale must be finite and strictly greater than one")
    if not isinstance(divisor, int) or isinstance(divisor, bool) or divisor < 1:
        raise ValueError("divisor must be a positive integer")
    if not isinstance(order, int) or isinstance(order, bool) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    if divisor > scale:
        return 0.0
    base = math.log(scale / divisor) / math.log(scale)
    # Guard tiny negative roundoff at the terminal point.
    if base < 0.0 and base > -64.0 * math.ulp(1.0):
        base = 0.0
    if not 0.0 <= base <= 1.0 + 64.0 * math.ulp(1.0):
        raise RuntimeError("cutoff base left its exact interval [0,1]")
    return max(0.0, min(1.0, base)) ** order


def shifted_reciprocal_weight(divisor: int, alpha: float) -> float:
    """The coefficientwise proportional-order limit ``d**(-alpha)``."""

    if not isinstance(divisor, int) or isinstance(divisor, bool) or divisor < 1:
        raise ValueError("divisor must be a positive integer")
    _require_finite_positive(alpha, "alpha")
    return divisor ** (-alpha)


def proportional_weight(scale: float, divisor: int, alpha: float) -> float:
    """Cutoff weight with ``k = ceil(alpha log(scale))``."""

    ledger = proportional_order(scale, alpha)
    return logarithmic_cutoff_weight(scale, divisor, ledger.order)


def carrier_rate(alpha: float, displacement: float) -> float:
    r"""Formal exponential rate of the isolated Mellin residue.

    For ``k ~ alpha log(Y)`` and a positive horizontal displacement ``delta``,
    Stirling's formula gives

    ``Phi(delta,alpha) = delta + alpha(log(alpha/delta)-1)``.
    """

    _require_finite_positive(alpha, "alpha")
    _require_finite_positive(displacement, "displacement")
    return displacement + alpha * (math.log(alpha / displacement) - 1.0)


def scaled_entropy_rate(alpha: float, displacement: float) -> float:
    """Equivalent stable form ``alpha * (x - 1 - log x)``."""

    _require_finite_positive(alpha, "alpha")
    _require_finite_positive(displacement, "displacement")
    ratio = displacement / alpha
    return alpha * (ratio - 1.0 - math.log(ratio))


def minimum_carrier_rate_on_interval(
    alpha: float, displacement_min: float, displacement_max: float = 0.5
) -> tuple[float, float]:
    """Return ``(minimum rate, minimizing displacement)`` on a closed interval.

    The convex rate has its unique global minimum at ``delta=alpha``.
    """

    _require_finite_positive(alpha, "alpha")
    _require_finite_positive(displacement_min, "displacement_min")
    _require_finite_positive(displacement_max, "displacement_max")
    if displacement_min > displacement_max:
        raise ValueError("displacement_min must not exceed displacement_max")
    minimizer = min(max(alpha, displacement_min), displacement_max)
    return carrier_rate(alpha, minimizer), minimizer


def terminal_power_exponent(alpha: float, relative_log_position: float) -> float:
    r"""Power exponent of a coefficient at ``d=Y^r``.

    For ``0 <= r < 1`` and ``k ~ alpha log(Y)``, the weight is
    ``Y**(alpha * log(1-r) + o(1))``.  The returned exponent is nonpositive.
    """

    _require_finite_positive(alpha, "alpha")
    if (
        not math.isfinite(relative_log_position)
        or relative_log_position < 0.0
        or relative_log_position >= 1.0
    ):
        raise ValueError("relative_log_position must lie in [0,1)")
    return alpha * math.log1p(-relative_log_position)


def verify_weight_domination(
    scales: Iterable[float], alphas: Iterable[float], divisor_cap: int
) -> float:
    r"""Check ``w_{Y,ceil(alpha log Y)}(d) <= d^{-alpha}`` on a finite grid.

    Returns the largest signed excess, which should be nonpositive up to
    floating-point roundoff.
    """

    if (
        not isinstance(divisor_cap, int)
        or isinstance(divisor_cap, bool)
        or divisor_cap < 1
    ):
        raise ValueError("divisor_cap must be a positive integer")
    largest_excess = -math.inf
    for scale in scales:
        if not math.isfinite(scale) or scale <= 1.0:
            raise ValueError("every scale must be finite and greater than one")
        for alpha in alphas:
            _require_finite_positive(alpha, "alpha")
            for divisor in range(1, min(divisor_cap, math.floor(scale)) + 1):
                excess = (
                    proportional_weight(scale, divisor, alpha)
                    - shifted_reciprocal_weight(divisor, alpha)
                )
                largest_excess = max(largest_excess, excess)
                if excess > 2.0e-14:
                    raise AssertionError(
                        "proportional cutoff exceeded shifted reciprocal "
                        f"at Y={scale}, alpha={alpha}, d={divisor}: {excess}"
                    )
    if largest_excess == -math.inf:
        raise ValueError("the verification grid was empty")
    return largest_excess


def fixed_divisor_convergence(
    divisor: int, alpha: float, scales: Iterable[float]
) -> tuple[float, ...]:
    """Return absolute errors against ``d**(-alpha)`` along supplied scales."""

    target = shifted_reciprocal_weight(divisor, alpha)
    errors: list[float] = []
    for scale in scales:
        if scale < divisor:
            raise ValueError("every scale must be at least the divisor")
        errors.append(abs(proportional_weight(scale, divisor, alpha) - target))
    return tuple(errors)
