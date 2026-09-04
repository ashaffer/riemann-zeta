#!/usr/bin/env python3
"""Exact normalization ledger for the global compact Pick deep-fan gate.

The optimization routines are reproducible floating diagnostics.  The formulas
they evaluate (Poisson load, complex Lagrange rate, and conditional jet budget)
are the theorem-grade part of the accompanying audit card.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from scipy.optimize import brentq, minimize_scalar


ALPHA = 0.49
DENSITY = 0.66
RAW_CARRIER = ALPHA * DENSITY
GREEN_LAMBDA = 0.304
ROUNDED_POSITIVE_PART = 1.39
ROUNDED_GREEN_BILL = (
    GREEN_LAMBDA / 2
    + DENSITY * ROUNDED_POSITIVE_PART / (2 * math.pi)
)
PICK_SURCHARGE = RAW_CARRIER - ROUNDED_GREEN_BILL
CARRIER_DEPTH_FLOOR = ALPHA * DENSITY


def pair_poisson_kernel(b: float, ordinate: float = 0.0) -> float:
    """Reflected-pair kernel on the limiting line Re(s)=1.

    Centered coordinates have x=1/2.  The pair depths are +/-b.
    """

    if not (0 <= b < 0.5):
        raise ValueError("require 0 <= b < 1/2")
    v2 = ordinate * ordinate
    return (0.5 - b) / ((0.5 - b) ** 2 + v2) + (0.5 + b) / (
        (0.5 + b) ** 2 + v2
    )


def centered_screen_poisson_load(
    half_width_twice: float, b: float, d: float = DENSITY
) -> float:
    """Leading L-normalized pointwise load of two interlaced chains.

    ``half_width_twice`` is the full physical ordinate width H.  Each chain
    has spacing pi/(d L), and the two chains interlace, so their combined
    density is 2 d L/pi.  The maximum is at the interval center.
    """

    H = float(half_width_twice)
    if H < 0 or not (0 <= b < 0.5) or d <= 0:
        raise ValueError("invalid screen parameters")
    a_right = 0.5 - b
    a_left = 0.5 + b
    return (4 * d / math.pi) * (
        math.atan(H / (2 * a_right)) + math.atan(H / (2 * a_left))
    )


def pointwise_screen_c_cap(b: float, d: float = DENSITY) -> float:
    """Largest K/L=c allowed by the pointwise L/2 Poisson budget."""

    if not (0 <= b < 0.5) or d <= 0:
        raise ValueError("invalid screen parameters")
    root = brentq(
        lambda H: centered_screen_poisson_load(H, b, d) - 0.5,
        1e-15,
        10.0,
        xtol=1e-14,
        rtol=1e-14,
    )
    return d * root / math.pi


def complex_lagrange_rate(y: float) -> float:
    r"""Limit 1+integral_0^1 log|1/2+i*y-x| dx.

    This is the exponential interpolation factor missed if a depth-shifted
    binomial chain is treated as though its target remained on the chain.
    """

    if y < 0:
        raise ValueError("y must be nonnegative")
    if y == 0:
        return -math.log(2.0)
    return 0.5 * math.log(0.25 + y * y) + 2 * y * math.atan(1 / (2 * y))


def centered_binomial_attenuation(
    b: float,
    c: float,
    *,
    alpha: float = ALPHA,
    d: float = DENSITY,
) -> float:
    """Forced attenuation exponent for the centered two-chain screen.

    The formula includes Taylor remainder, the factor 2^K from positive
    binomial dependence, and complex Lagrange continuation back to alpha.
    """

    if not (0 < b <= alpha < 0.5) or c <= 0 or d <= 0:
        raise ValueError("invalid binomial parameters")
    eta = alpha - b
    H = math.pi * c / d
    radius = math.hypot(eta, H / 2)
    y = eta / H
    if radius >= alpha:
        return float("-inf")
    return c * (
        math.log(alpha / (2 * radius)) - complex_lagrange_rate(y)
    )


@dataclass(frozen=True)
class ScreenOptimum:
    b: float
    c: float
    c_cap: float
    attenuation: float
    poisson_load: float


def optimize_centered_screen() -> ScreenOptimum:
    """Numerically maximize the audited screen exponent over the live band."""

    def best_at_b(b: float) -> tuple[float, float, float]:
        cap = pointwise_screen_c_cap(b)
        result = minimize_scalar(
            lambda c: -centered_binomial_attenuation(b, c),
            bounds=(1e-10, cap),
            method="bounded",
            options={"xatol": 1e-13},
        )
        return -float(result.fun), float(result.x), cap

    outer = minimize_scalar(
        lambda b: -best_at_b(float(b))[0],
        bounds=(CARRIER_DEPTH_FLOOR, ALPHA - 1e-10),
        method="bounded",
        options={"xatol": 1e-12},
    )
    b = float(outer.x)
    exponent, c, cap = best_at_b(b)
    H = math.pi * c / DENSITY
    return ScreenOptimum(
        b=b,
        c=c,
        c_cap=cap,
        attenuation=exponent,
        poisson_load=centered_screen_poisson_load(H, b),
    )


def four_rows_per_jet_danger(b: float, alpha: float = ALPHA) -> float:
    r"""Conditional exponent if a uniform 4r-row growing fixture existed.

    The pointwise budget permits at most L/(2K_b) rows.  Four rows per
    complex jet order would permit r/L=1/(8K_b), and r Schur steps from b
    to alpha would cost log((alpha+b)/(alpha-b)) per order.

    This is a danger envelope, not an existence theorem for such fixtures.
    """

    if not (0 < b < alpha < 0.5):
        raise ValueError("require 0 < b < alpha < 1/2")
    kernel = pair_poisson_kernel(b)
    return math.log((alpha + b) / (alpha - b)) / (8 * kernel)


@dataclass(frozen=True)
class JetDanger:
    b: float
    exponent: float
    excess_over_surcharge: float


def optimize_four_row_jet_danger() -> JetDanger:
    result = minimize_scalar(
        lambda b: -four_rows_per_jet_danger(float(b)),
        bounds=(CARRIER_DEPTH_FLOOR, ALPHA - 1e-10),
        method="bounded",
        options={"xatol": 1e-14},
    )
    b = float(result.x)
    exponent = -float(result.fun)
    return JetDanger(b, exponent, exponent - PICK_SURCHARGE)


def self_check() -> dict[str, object]:
    screen = optimize_centered_screen()
    danger = optimize_four_row_jet_danger()
    assert math.isclose(RAW_CARRIER, 0.3234, rel_tol=0, abs_tol=1e-15)
    assert ROUNDED_GREEN_BILL < 0.298008745
    assert math.isclose(PICK_SURCHARGE, 0.0253912552075, rel_tol=2e-12)
    assert screen.attenuation < PICK_SURCHARGE
    assert screen.poisson_load <= 0.5 + 2e-7
    assert danger.exponent > PICK_SURCHARGE
    return {
        "rounded_green_bill": ROUNDED_GREEN_BILL,
        "pick_surcharge": PICK_SURCHARGE,
        "screen": screen.__dict__,
        "conditional_four_row_jet_danger": danger.__dict__,
        "gp_closed": False,
    }


if __name__ == "__main__":
    print(self_check())
