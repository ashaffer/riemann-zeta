#!/usr/bin/env python3
"""Finite ledger for proportional-order logarithmic mollifier weights.

This module proves no zero-free region.  It records the exact tradeoff that
appears when the logarithmic cutoff order grows like ``alpha * log(Y)``:

* fixed coefficients converge to a horizontally shifted reciprocal weight
  ``d**(-alpha)``;
* a formal zero-residue contribution has exponential rate
  ``delta + alpha * (log(alpha / delta) - 1)``;
* this rate is nonnegative and vanishes only at ``delta = alpha``;
* the unweighted mean-value error of the mollifier alone has effective support
  exponent

      chi(alpha) = 1 - 2 alpha + 2 alpha log(2 alpha)

  for ``0 < alpha < 1/2`` and exponent zero for ``alpha >= 1/2``.

The last two items are contour and mean-value ledgers, not a zero-free-strip
proof.  A new high-order analogue of the Bettin--Gonek detector theorem and a
completed bound for ``zeta * mollifier`` would still be required.
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


def effective_support_exponent(alpha: float) -> float:
    r"""Power exponent of ``sum_{d<=Y} w_{Y,k}(d)^2``.

    With ``k ~ alpha log(Y)``, the logarithmic scale ``d=Y^r`` contributes

    ``Y**(r + 2 alpha log(1-r) + o(1))``.

    Its maximum is attained at ``r=1-2*alpha`` when ``alpha<1/2``.  For
    ``alpha>=1/2`` the maximum moves to ``r=0`` and has exponent zero.
    """

    _require_finite_positive(alpha, "alpha")
    if alpha >= 0.5:
        return 0.0
    return 1.0 - 2.0 * alpha + 2.0 * alpha * math.log(2.0 * alpha)


def maximum_nominal_length_exponent(alpha: float) -> float:
    r"""Largest ``theta`` allowed by the mollifier-alone mean-value ledger.

    The elementary mean-value error is at the natural ``T`` scale when
    ``Y=T**theta`` and ``theta * chi(alpha) <= 1``.  A zero exponent permits
    arbitrary fixed polynomial length at this *mollifier-only* level.
    """

    exponent = effective_support_exponent(alpha)
    if exponent == 0.0:
        return math.inf
    return 1.0 / exponent


def strip_width_from_nominal_length(theta: float) -> float:
    """The standard long-mollifier strip width ``(theta-1)/(2 theta)``."""

    if not math.isfinite(theta) or theta <= 1.0:
        raise ValueError("theta must be finite and strictly greater than one")
    return (theta - 1.0) / (2.0 * theta)


def effective_threshold_strip_width(alpha: float) -> float:
    r"""Width at the mollifier-alone threshold ``theta=1/chi(alpha)``.

    For ``0<alpha<1/2`` this equals both

    ``(1-chi(alpha))/2`` and ``alpha * (1-log(2 alpha))``.
    """

    _require_finite_positive(alpha, "alpha")
    if alpha >= 0.5:
        raise ValueError("the finite-threshold formula requires alpha < one half")
    exponent = effective_support_exponent(alpha)
    return (1.0 - exponent) / 2.0


def corridor_margin(theta: float, alpha: float) -> float:
    r"""Return ``1/theta - chi(alpha)``.

    Positivity means that the mollifier alone has a power-saving margin in its
    elementary mean-value error at nominal length ``Y=T**theta``.
    """

    if not math.isfinite(theta) or theta <= 1.0:
        raise ValueError("theta must be finite and strictly greater than one")
    return 1.0 / theta - effective_support_exponent(alpha)


def boundary_carrier_rate(theta: float, alpha: float) -> float:
    """Carrier rate at the standard strip displacement for ``theta``."""

    return carrier_rate(alpha, strip_width_from_nominal_length(theta))


def alpha_threshold_for_theta(theta: float, iterations: int = 160) -> float:
    r"""Solve ``chi(alpha)=1/theta`` inside ``(0,delta_theta)`` by bisection.

    For every fixed ``theta>1``, strict monotonicity of ``chi`` on
    ``(0,1/2)`` and

    ``chi(delta_theta) < 1/theta < lim_{alpha->0+} chi(alpha)=1``

    give a unique threshold.  Choosing ``alpha`` strictly between this value
    and ``delta_theta`` leaves both a mean-value margin and a positive carrier
    rate at the target boundary.
    """

    if not math.isfinite(theta) or theta <= 1.0:
        raise ValueError("theta must be finite and strictly greater than one")
    if not isinstance(iterations, int) or isinstance(iterations, bool) or iterations < 1:
        raise ValueError("iterations must be a positive integer")
    target = 1.0 / theta
    low = 0.0
    high = strip_width_from_nominal_length(theta)
    if effective_support_exponent(high) >= target:
        raise RuntimeError("the theoretical corridor endpoint was not strict")
    for _ in range(iterations):
        midpoint = (low + high) / 2.0
        if effective_support_exponent(midpoint) > target:
            low = midpoint
        else:
            high = midpoint
    return (low + high) / 2.0


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
