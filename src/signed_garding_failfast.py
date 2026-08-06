#!/usr/bin/env python3
"""Low-memory diagnostics for the signed zeta Gårding checkpoint.

For functions supported in ``[-a,a]`` the Weil form is the Paley--Wiener
compression of the multiplier

    Omega_a(t) = Re psi(1/4+it/2) - log(pi)
                 - 2 sum_{log n < 2a} Lambda(n)/sqrt(n) cos(t log n)
                 + 4 int_0^(2a) cosh(u/2) cos(tu) du.

The final term is the *plus-signed* zeta-pole contribution.  This program scans
Omega and Omega-c*log(1+t^2) in small frequency chunks.  A sampled minimum is
only a falsifier/diagnostic: positivity of the Weil form concerns the
compression to PW_a and does not imply pointwise positivity of Omega.
"""

from __future__ import annotations

import argparse
import math
from collections.abc import Iterable

import numpy as np
from scipy.special import digamma


def prime_powers(limit: int) -> tuple[np.ndarray, np.ndarray]:
    """Return log(n) and Lambda(n)/sqrt(n) for prime powers n <= limit."""
    if limit < 2:
        return np.empty(0), np.empty(0)
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    sieve[4::2] = False
    stop = math.isqrt(limit)
    for p in range(3, stop + 1, 2):
        if sieve[p]:
            sieve[p * p :: 2 * p] = False

    logs: list[float] = []
    weights: list[float] = []
    for p in np.flatnonzero(sieve):
        logp = math.log(int(p))
        n = int(p)
        while n <= limit:
            logs.append(math.log(n))
            weights.append(logp / math.sqrt(n))
            if n > limit // int(p):
                break
            n *= int(p)
    order = np.argsort(logs)
    return np.asarray(logs)[order], np.asarray(weights)[order]


def pole_symbol(a: float, t: np.ndarray | float) -> np.ndarray:
    """Fourier multiplier of the rank-two zeta-pole form."""
    tt = np.asarray(t, dtype=float)
    numerator = (
        0.5 * math.sinh(a) * np.cos(2 * a * tt)
        + tt * math.cosh(a) * np.sin(2 * a * tt)
    )
    return 4 * numerator / (tt * tt + 0.25)


def completed_symbol(
    a: float,
    t: np.ndarray | float,
    all_logs: np.ndarray,
    all_weights: np.ndarray,
) -> np.ndarray:
    """Evaluate the exact finite-window completed multiplier."""
    tt = np.atleast_1d(np.asarray(t, dtype=float))
    active = all_logs < 2 * a
    logs = all_logs[active]
    weights = all_weights[active]
    prime = np.zeros_like(tt)
    if logs.size:
        prime = 2 * (np.cos(tt[:, None] * logs[None, :]) @ weights)
    arch = np.real(digamma(0.25 + 0.5j * tt)) - math.log(math.pi)
    answer = arch - prime + pole_symbol(a, tt)
    return answer if np.ndim(t) else answer[0]


def chunked_minimum(
    a: float,
    frequencies: np.ndarray,
    coefficients: Iterable[float],
    logs: np.ndarray,
    weights: np.ndarray,
    chunk: int,
) -> dict[float, tuple[float, float]]:
    """Return sampled minima (value, argmin) for Omega-c log(1+t^2)."""
    result = {float(c): (math.inf, math.nan) for c in coefficients}
    for start in range(0, frequencies.size, chunk):
        tt = frequencies[start : start + chunk]
        omega = completed_symbol(a, tt, logs, weights)
        energy = np.log1p(tt * tt)
        for coefficient in result:
            values = omega - coefficient * energy
            index = int(np.argmin(values))
            if values[index] < result[coefficient][0]:
                result[coefficient] = (float(values[index]), float(tt[index]))
    return result


def parse_csv_floats(value: str) -> list[float]:
    return [float(item) for item in value.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", default="0.4375,1,2,3,4,5")
    parser.add_argument("--coefficients", default="0,0.1,0.25,0.5")
    parser.add_argument("--tmax", type=float, default=250.0)
    parser.add_argument("--step", type=float, default=0.005)
    parser.add_argument("--chunk", type=int, default=128)
    args = parser.parse_args()

    supports = parse_csv_floats(args.supports)
    coefficients = parse_csv_floats(args.coefficients)
    limit = math.ceil(math.exp(2 * max(supports)))
    logs, weights = prime_powers(limit)
    frequencies = np.arange(0.0, args.tmax + args.step / 2, args.step)

    print("a,active_prime_powers,prime_mass,pole_at_zero,omega_at_zero," +
          ",".join(f"min_c{c:g},argmin_c{c:g}" for c in coefficients))
    for a in supports:
        active = logs < 2 * a
        prime_mass = 2 * float(np.sum(weights[active]))
        omega_zero = float(completed_symbol(a, 0.0, logs, weights))
        minima = chunked_minimum(
            a, frequencies, coefficients, logs, weights, args.chunk
        )
        fields: list[str] = [
            f"{a:.12g}",
            str(int(np.sum(active))),
            f"{prime_mass:.12g}",
            f"{float(pole_symbol(a, 0.0)):.12g}",
            f"{omega_zero:.12g}",
        ]
        for coefficient in coefficients:
            value, argmin = minima[coefficient]
            fields.extend((f"{value:.12g}", f"{argmin:.12g}"))
        print(",".join(fields))


if __name__ == "__main__":
    main()
