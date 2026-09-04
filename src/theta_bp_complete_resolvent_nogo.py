"""Exact Green-kernel audit for the complete theta ``B_P`` operator.

After Fourier transformation in ``w``, the polar-subtracted identity

    Phi((w+d)/2) Phi((w-d)/2) = L C(w,d) / 256

contains the constant-coefficient operator

    L_T = D_d^4 + 2 (T^2 - 1) D_d^2 + (T^2 + 1)^2.

Its Fourier symbol is strictly positive, but its *unique* decaying
translation-invariant inverse is not positivity preserving on the
pointwise cone unless ``T=0``.  (The inverse remains a positive-definite
convolution kernel in the Hilbert-space sense.)
This module records the exact inverse and reproducible numerical checks.

The result is a scoped no-go for a positive scalar inverse-resolvent proof.
It is not a counterexample to positive definiteness of the actual ``B_P``.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import argparse
import json
import math
from typing import Iterable


def completion_symbol(t: float, frequency: float) -> float:
    """Return the Fourier symbol of the completed ``d`` operator."""

    return (1.0 + (frequency + t) ** 2) * (
        1.0 + (frequency - t) ** 2
    )


def expanded_completion_symbol(t: float, frequency: float) -> float:
    """Return the same symbol in expanded fourth-order form."""

    return (
        frequency**4
        + 2.0 * (1.0 - t * t) * frequency**2
        + (1.0 + t * t) ** 2
    )


def complete_green(t: float, displacement: float) -> float:
    """The unique decaying convolution inverse of the completed operator.

    The formula is continuous at ``t=0``.  It uses ``abs(displacement)``
    because the kernel is even in both variables.
    """

    q = abs(float(t))
    x = abs(float(displacement))
    if q == 0.0:
        return 0.25 * (1.0 + x) * math.exp(-x)
    return (
        math.exp(-x)
        * (math.cos(q * x) + math.sin(q * x) / q)
        / (4.0 * (1.0 + q * q))
    )


def first_zero(t: float) -> float:
    """Return the first positive zero of ``complete_green(t, .)``."""

    q = abs(float(t))
    if q == 0.0:
        return math.inf
    return (math.pi / 2.0 + math.atan(1.0 / q)) / q


def negative_witness(t: float) -> tuple[float, float]:
    """Return the universal explicit negative witness ``d=pi/abs(t)``."""

    q = abs(float(t))
    if q == 0.0:
        raise ValueError("the zero-frequency Green kernel is positive")
    displacement = math.pi / q
    # Evaluating the simplified exact expression avoids trigonometric
    # roundoff in sin(pi).
    value = -math.exp(-displacement) / (4.0 * (1.0 + q * q))
    return displacement, value


def green_total_mass(t: float) -> float:
    """Return ``integral_R G_T = 1 / symbol(T, 0)``."""

    q = float(t)
    return 1.0 / (1.0 + q * q) ** 2


@dataclass(frozen=True)
class ResolventRow:
    t: float
    origin: float
    first_zero: float
    witness_d: float
    witness_value: float
    total_mass: float
    symbol_minimum_lower_bound: float


def resolvent_row(t: float) -> ResolventRow:
    """Build one transparent certificate row."""

    q = abs(float(t))
    if q == 0.0:
        return ResolventRow(
            t=float(t),
            origin=complete_green(t, 0.0),
            first_zero=math.inf,
            witness_d=math.inf,
            witness_value=0.0,
            total_mass=green_total_mass(t),
            symbol_minimum_lower_bound=1.0,
        )
    witness_d, witness_value = negative_witness(t)
    return ResolventRow(
        t=float(t),
        origin=complete_green(t, 0.0),
        first_zero=first_zero(t),
        witness_d=witness_d,
        witness_value=witness_value,
        total_mass=green_total_mass(t),
        # Each factor in the factored symbol is at least one.
        symbol_minimum_lower_bound=1.0,
    )


def build_report(t_values: Iterable[float]) -> dict[str, object]:
    """Return a JSON-serializable report for selected frequencies."""

    rows = [resolvent_row(value) for value in t_values]
    return {
        "schema": "zeta23.theta-bp-complete-resolvent-nogo.v1",
        "operator": "D^4 + 2(T^2-1)D^2 + (T^2+1)^2",
        "symbol": "[1+(lambda+T)^2][1+(lambda-T)^2]",
        "green": (
            "exp(-|d|)[cos(T|d|)+sin(T|d|)/T]"
            "/[4(1+T^2)]"
        ),
        "zero_frequency_green": "(1+|d|)exp(-|d|)/4",
        "universal_negative_witness": "d=pi/|T| for every T != 0",
        "scope": (
            "rules out a nonnegative scalar translation-invariant inverse "
            "resolvent; does not decide B_P positive definiteness"
        ),
        "rows": [asdict(row) for row in rows],
    }


def _parse_values(raw: str) -> list[float]:
    values = [float(part.strip()) for part in raw.split(",") if part.strip()]
    if not values:
        raise ValueError("at least one T value is required")
    return values


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--t-values", default="0,0.5,1,2,10")
    args = parser.parse_args()
    print(json.dumps(build_report(_parse_values(args.t_values)), indent=2))
