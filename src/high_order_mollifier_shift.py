#!/usr/bin/env python3
"""Finite ledger for proportional-order logarithmic mollifier weights.

This module proves no zero-free region.  It audits a tempting high-order
variant of the long-mollifier route and records the obstruction that prevents
it from becoming a trivial proof of RH.

Let

    w_{Y,k}(d) = 1_(d<=Y) (log(Y/d)/log(Y))^k

with ``k ~ alpha log(Y)``.  Then:

* fixed coefficients converge to ``d**(-alpha)`` and are dominated by it;
* the mollifier-alone mean-value error has effective support exponent

      chi(alpha) = 1 - 2 alpha + 2 alpha log(2 alpha)

  for ``0 < alpha < 1/2``;
* a *naively isolated* target-zero residue has exponent

      Phi(delta,alpha)
        = delta + alpha(log(alpha/delta)-1).

The adjective "naively" is essential.  The exact high-order Mellin transform
contains ``(w-1)^(-(k+1))``.  If the first-order Bettin--Gonek auxiliary
function is reused, the product acquires a new pole at ``w=1`` of order
``k-1``.  Its polynomial residue must be retained and can cancel the apparent
target carrier.  If one instead modifies the auxiliary function to cancel
that pole, the target carrier is exponentially attenuated.

For ``0 < alpha < 1/2`` there is already an exact exponent repayment:

    2 Phi(1/2,alpha) = chi(alpha).

Thus the elementary mollifier-alone condition ``theta*chi(alpha) <= 1``
forces the largest naive detector exponent in the outer half of the strip to
be at most the threshold needed for contradiction.  High-order tapering does
not, by itself, cross the long-mollifier barrier.
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


def naive_carrier_rate(alpha: float, displacement: float) -> float:
    r"""Exponent of the target residue when the new central pole is omitted.

    This is a useful diagnostic but not a valid isolated lower bound for the
    high-order detector.  The complete Mellin contour also contains the pole
    at ``w=1`` described in the module docstring.
    """

    _require_finite_positive(alpha, "alpha")
    _require_finite_positive(displacement, "displacement")
    return displacement + alpha * (math.log(alpha / displacement) - 1.0)


# Backward-compatible diagnostic name used by the first finite ledger.
carrier_rate = naive_carrier_rate


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

    Its maximum is at ``r=1-2*alpha`` when ``alpha<1/2``.  For
    ``alpha>=1/2`` the maximum moves to ``r=0`` and has exponent zero.
    """

    _require_finite_positive(alpha, "alpha")
    if alpha >= 0.5:
        return 0.0
    return 1.0 - 2.0 * alpha + 2.0 * alpha * math.log(2.0 * alpha)


def maximum_nominal_length_exponent(alpha: float) -> float:
    r"""Mollifier-alone threshold from ``theta*chi(alpha) <= 1``.

    This threshold says nothing by itself about ``zeta * mollifier`` or zero
    detection.  A zero exponent permits arbitrary fixed polynomial length
    only at the mollifier-alone mean-value level.
    """

    exponent = effective_support_exponent(alpha)
    if exponent == 0.0:
        return math.inf
    return 1.0 / exponent


def zero_displacement_boundary(theta: float) -> float:
    """Bettin--Gonek horizontal displacement boundary ``1/(2 theta)``."""

    if not math.isfinite(theta) or theta <= 1.0:
        raise ValueError("theta must be finite and strictly greater than one")
    return 1.0 / (2.0 * theta)


def strip_width_from_nominal_length(theta: float) -> float:
    """Symmetric edge width ``1/2 - 1/(2 theta)``."""

    return 0.5 - zero_displacement_boundary(theta)


def naive_detector_surplus(theta: float, alpha: float, displacement: float) -> float:
    r"""Naive exponent surplus ``2 theta Phi(delta,alpha)-1``.

    A positive value would be needed by the unmodified exponent comparison,
    but it is not sufficient because the central Mellin pole has been omitted.
    """

    if not math.isfinite(theta) or theta <= 1.0:
        raise ValueError("theta must be finite and strictly greater than one")
    return 2.0 * theta * naive_carrier_rate(alpha, displacement) - 1.0


def outer_edge_repayment(alpha: float) -> float:
    r"""Return ``2 Phi(1/2,alpha)-chi(alpha)`` for ``alpha<1/2``.

    The result is zero up to floating-point rounding.  It records the exact
    repayment between effective support and the largest naive carrier in the
    outer half of the critical strip.
    """

    _require_finite_positive(alpha, "alpha")
    if alpha >= 0.5:
        raise ValueError("the repayment identity requires alpha < one half")
    return (
        2.0 * naive_carrier_rate(alpha, 0.5)
        - effective_support_exponent(alpha)
    )


def fully_compensated_carrier_rate(alpha: float, displacement: float) -> float:
    r"""Diagnostic rate after cancelling the central pole in the auxiliary factor.

    Replacing the original ``(w-1)^2/(w+1)^2`` factor by the matching
    ``(w-1)^(k+1)/(w+1)^(k+1)`` removes the pole at ``w=1``.  At ``t=gamma``
    the resulting normalized target residue has the schematic rate

    ``delta + alpha(log(alpha/(2+delta))-1)``.

    This function records that exact exponent ledger; it is not a theorem
    that this particular compensated kernel is optimal.
    """

    _require_finite_positive(alpha, "alpha")
    _require_finite_positive(displacement, "displacement")
    return displacement + alpha * (
        math.log(alpha / (2.0 + displacement)) - 1.0
    )


def central_mellin_pole_order(order: int) -> int:
    """Order of the new pole at ``w=1`` after reusing the first-order kernel."""

    if not isinstance(order, int) or isinstance(order, bool) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    return max(0, order - 1)


def mean_value_alpha_threshold_for_theta(
    theta: float, iterations: int = 160
) -> float:
    r"""Solve ``chi(alpha)=1/theta`` in ``(0,1/2)`` by bisection.

    This is only the mollifier-alone mean-value threshold.  It is not a
    zero-free-strip corridor because of the exact repayment and central pole.
    """

    if not math.isfinite(theta) or theta <= 1.0:
        raise ValueError("theta must be finite and strictly greater than one")
    if not isinstance(iterations, int) or isinstance(iterations, bool) or iterations < 1:
        raise ValueError("iterations must be a positive integer")
    target = 1.0 / theta
    low = 0.0
    high = 0.5
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
    """Minimum of the naive convex carrier rate on a closed interval."""

    _require_finite_positive(alpha, "alpha")
    _require_finite_positive(displacement_min, "displacement_min")
    _require_finite_positive(displacement_max, "displacement_max")
    if displacement_min > displacement_max:
        raise ValueError("displacement_min must not exceed displacement_max")
    minimizer = min(max(alpha, displacement_min), displacement_max)
    return naive_carrier_rate(alpha, minimizer), minimizer


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
    r"""Check ``w_{Y,ceil(alpha log Y)}(d) <= d^{-alpha}`` on a finite grid."""

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
