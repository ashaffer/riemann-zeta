"""Exact arithmetic for the signed-shell Chebyshev/capacity gate.

The mathematical statements audited by this module are recorded in
``results/ZETA23-QP-SIGNED-KERNEL-CAPACITY-GATE-2026-08-15.md``.  This file
only evaluates the closed-form constants occurring there; it does not use
floating-point experiments as a substitute for any positivity statement.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


def _positive(name: str, value: float) -> float:
    value = float(value)
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and positive")
    return value


def log_cosh(value: float) -> float:
    """Return ``log(cosh(value))`` without overflowing."""

    size = abs(float(value))
    return size + math.log1p(math.exp(-2.0 * size)) - math.log(2.0)


def chebyshev_theta(a0: float, a1: float) -> float:
    """Exterior Green distance for ``[a0^2,a1^2]`` seen from zero.

    It is both ``acosh((a1^2+a0^2)/(a1^2-a0^2))`` and
    ``log((a1+a0)/(a1-a0))``.  The logarithmic formula is more stable when
    ``a0/a1`` is small.
    """

    a0 = _positive("a0", a0)
    a1 = _positive("a1", a1)
    if not a0 < a1:
        raise ValueError("a0 must be smaller than a1")
    return math.log((a1 + a0) / (a1 - a0))


def chebyshev_log_resonant_bound(
    order: int, a0: float, a1: float, width: float
) -> float:
    """Log of the proved bound for ``|F_m(-a)|``, uniformly in the interval.

    The exact bound is ``exp(width*a1) / cosh(order*theta)^2``.
    """

    if not isinstance(order, int) or isinstance(order, bool) or order < 1:
        raise ValueError("order must be a positive integer")
    width = _positive("width", width)
    theta = chebyshev_theta(a0, a1)
    return width * float(a1) - 2.0 * log_cosh(order * theta)


def required_chebyshev_order(
    log_y: float,
    target_power: float,
    a0: float,
    a1: float,
    width: float,
) -> int:
    """Least integer order certified to give ``|F_m(-a)| <= Y^-target``."""

    log_y = _positive("log_y", log_y)
    target_power = _positive("target_power", target_power)
    width = _positive("width", width)
    theta = chebyshev_theta(a0, a1)
    target = 0.5 * (target_power * log_y + width * a1)

    # acosh(exp(target)) = target + log(1 + sqrt(1-exp(-2 target))).
    inverse = target + math.log1p(math.sqrt(max(0.0, 1.0 - math.exp(-2.0 * target))))
    order = max(1, math.ceil(inverse / theta))
    while chebyshev_log_resonant_bound(order, a0, a1, width) > -target_power * log_y:
        order += 1
    while (
        order > 1
        and chebyshev_log_resonant_bound(order - 1, a0, a1, width)
        <= -target_power * log_y
    ):
        order -= 1
    return order


def chebyshev_spike_log(order: int, a0: float, a1: float, width: float) -> float:
    """Exact log transform value at the audited imaginary-axis spike.

    Put ``K=4*order+4`` and ``t*=pi*K/(2*width)``.  For the squared
    Chebyshev multiplier times the K-fold box spline, this returns

      log F_m(i t*)
       = 2(log T_m(eta)-log T_m(xi)) + K log(2/pi).
    """

    if not isinstance(order, int) or isinstance(order, bool) or order < 1:
        raise ValueError("order must be a positive integer")
    a0 = _positive("a0", a0)
    a1 = _positive("a1", a1)
    width = _positive("width", width)
    if not a0 < a1:
        raise ValueError("a0 must be smaller than a1")

    spline_order = 4 * order + 4
    spike = math.pi * spline_order / (2.0 * width)
    delta = a1 * a1 - a0 * a0
    xi = (a1 * a1 + a0 * a0) / delta
    eta = (2.0 * spike * spike + a1 * a1 + a0 * a0) / delta
    return (
        2.0
        * (
            log_cosh(order * math.acosh(eta))
            - log_cosh(order * math.acosh(xi))
        )
        + spline_order * math.log(2.0 / math.pi)
    )


def turan_vertical_envelope_floor(width: float, eta: float = 1.0) -> float:
    """Universal floor ``2*eta/width`` from the Turan/inversion theorem."""

    width = _positive("width", width)
    eta = _positive("eta", eta)
    return 2.0 * eta / width


@dataclass(frozen=True)
class SignedKernelAudit:
    log_y: float
    target_power: float
    a0: float
    a1: float
    width: float
    order: int
    resonant_log_bound: float
    spike_log_value: float
    vertical_envelope_floor: float


def audit_signed_kernel(
    log_y: float,
    target_power: float,
    a0: float,
    a1: float,
    width: float = 0.2,
) -> SignedKernelAudit:
    """Assemble the exact closed-form audit for one parameter choice."""

    order = required_chebyshev_order(log_y, target_power, a0, a1, width)
    return SignedKernelAudit(
        log_y=float(log_y),
        target_power=float(target_power),
        a0=float(a0),
        a1=float(a1),
        width=float(width),
        order=order,
        resonant_log_bound=chebyshev_log_resonant_bound(
            order, a0, a1, width
        ),
        spike_log_value=chebyshev_spike_log(order, a0, a1, width),
        vertical_envelope_floor=turan_vertical_envelope_floor(width),
    )

