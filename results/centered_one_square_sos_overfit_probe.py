#!/usr/bin/env python3
"""Prime-separable SOS stress test for the centered one-square gate.

For a centered real odd carrier, the von Mangoldt contribution is a sum of
one-variable trigonometric polynomials, one for each prime.  This probe
compares the actual common-height phase with the stronger relaxation in
which every prime phase is chosen independently.  The latter is exactly the
best bound available to a prime-separable Fejer/SOS certificate.

All output is floating diagnostic data, not an interval certificate.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from high_height_carrier_slice import (
    archimedean_matrix_sign,
    endpoint_null_basis,
    pole_matrix_sign,
    shift_overlap_sign,
)


def prime_power_atoms(limit: int) -> list[tuple[int, int, float, float]]:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for prime in range(2, math.isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = False
    atoms: list[tuple[int, int, float, float]] = []
    for prime_value in np.flatnonzero(sieve):
        prime = int(prime_value)
        log_prime = math.log(prime)
        power = prime
        exponent = 1
        while power <= limit:
            atoms.append(
                (prime, exponent, math.log(power), log_prime / math.sqrt(power))
            )
            if power > limit // prime:
                break
            power *= prime
            exponent += 1
    return atoms


def analyze(
    cutoff: int,
    alpha: float,
    aperture: float,
    jet_order: int,
    gamma_ratio: float,
    phase_samples: int,
) -> dict[str, float | int]:
    length = math.log(cutoff)
    spacing = 2.0 * math.pi / length
    half_count = int(math.floor(aperture * cutoff / spacing))
    indices = np.arange(-half_count, half_count + 1, dtype=int)
    base_tau = spacing * indices
    q = alpha / spacing

    raw_carrier = indices / (indices * indices + q * q)
    endpoint = endpoint_null_basis(indices, jet_order)
    carrier = endpoint @ (endpoint.T @ raw_carrier)
    carrier /= np.linalg.norm(carrier)

    coefficients: dict[int, list[tuple[int, float, float]]] = {}
    for prime, exponent, log_power, weight in prime_power_atoms(cutoff):
        overlap = shift_overlap_sign(base_tau, length, log_power)
        coefficient = -2.0 * weight * float(
            carrier @ overlap @ carrier
        ) / (length * length)
        coefficients.setdefault(prime, []).append(
            (exponent, coefficient, log_power)
        )

    theta = np.linspace(0.0, 2.0 * math.pi, phase_samples, endpoint=False)
    independent_minimum = 0.0
    independent_maximum = 0.0
    actual_prime = 0.0
    gamma = gamma_ratio * cutoff
    for polynomial in coefficients.values():
        values = np.zeros_like(theta)
        for exponent, coefficient, log_power in polynomial:
            values += coefficient * np.cos(exponent * theta)
            actual_prime += coefficient * math.cos(gamma * log_power)
        independent_minimum += float(np.min(values))
        independent_maximum += float(np.max(values))

    tau = gamma + base_tau
    background_matrix = (
        archimedean_matrix_sign(tau, length)
        + pole_matrix_sign(tau, indices, length)
    ) / (length * length)
    shifted_background = float(
        np.vdot(carrier, background_matrix @ carrier).real
    ) + 2.0 * math.pi / length

    return {
        "cutoff": cutoff,
        "dimension": int(indices.size),
        "prime_count": len(coefficients),
        "shifted_background": shifted_background,
        "actual_prime_contribution": actual_prime,
        "actual_shifted_square": shifted_background + actual_prime,
        "independent_prime_phase_minimum": independent_minimum,
        "independent_prime_phase_maximum": independent_maximum,
        "prime_separable_sos_lower": shifted_background + independent_minimum,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoffs", nargs="+", type=int, default=[32, 48, 64, 96, 128, 256, 512])
    parser.add_argument("--alpha", type=float, default=0.49)
    parser.add_argument("--aperture", type=float, default=0.2)
    parser.add_argument("--jet-order", type=int, default=2)
    parser.add_argument("--gamma-ratio", type=float, default=1.5)
    parser.add_argument("--phase-samples", type=int, default=65536)
    args = parser.parse_args()
    for cutoff in args.cutoffs:
        print(
            analyze(
                cutoff,
                args.alpha,
                args.aperture,
                args.jet_order,
                args.gamma_ratio,
                args.phase_samples,
            )
        )


if __name__ == "__main__":
    main()
