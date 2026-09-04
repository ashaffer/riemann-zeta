#!/usr/bin/env python3
"""Floating check of the broad-profile Christoffel obstruction.

The theorem in
ZETA23-CHRISTOFFEL-PROFILE-DESIGN-CONCENTRATION-BARRIER-2026-08-13.md
is analytic.  This script only evaluates its exact finite Gram formulas on
the actual prime-power nodes.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.special import j0


WIDTH = 0.2
LOW_EXPONENT = 0.4655
HIGH_EXPONENT = 50.0 / 33.0
DELTA_STAR = 0.0180303234


def prime_powers(limit: int) -> list[int]:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    values: set[int] = set()
    for p in np.flatnonzero(sieve):
        value = int(p)
        while value <= limit:
            values.add(value)
            if value > limit // int(p):
                break
            value *= int(p)
    return sorted(values)


def actual_nodes(y: int) -> np.ndarray:
    lower = y * math.exp(-WIDTH)
    upper = y * math.exp(WIDTH)
    return np.array(
        [
            math.log(n / y)
            for n in prime_powers(math.ceil(upper))
            if lower <= n <= upper
        ],
        dtype=float,
    )


def profile_gram(nodes: np.ndarray, left: float, right: float, kind: str) -> np.ndarray:
    center = 0.5 * (left + right)
    half_width = 0.5 * (right - left)

    def transform(omega: np.ndarray) -> np.ndarray:
        phase = np.exp(1j * center * omega)
        if kind == "uniform":
            # np.sinc(x)=sin(pi*x)/(pi*x).
            return phase * np.sinc(half_width * omega / math.pi)
        if kind == "arcsine":
            return phase * j0(half_width * omega)
        raise ValueError(kind)

    difference = nodes[:, None] - nodes[None, :]
    total = nodes[:, None] + nodes[None, :]
    gram = 0.5 * np.real(transform(difference) + transform(total))
    return 0.5 * (gram + gram.T)


def directional_leverage(
    gram: np.ndarray, q: np.ndarray
) -> tuple[float, float, int]:
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    cutoff = max(1e-13, 1e-11 * float(eigenvalues[-1]))
    retained = eigenvalues > cutoff
    q_coordinates = eigenvectors.T @ q
    unresolved = float(np.linalg.norm(q_coordinates[~retained]))
    leverage = float(np.sum(q_coordinates[retained] ** 2 / eigenvalues[retained]))
    return leverage, unresolved, int(np.sum(retained))


def main() -> None:
    print(f"delta_star={DELTA_STAR:.10f}")
    print(f"uniform_packet_threshold_exponent={2.0 * DELTA_STAR:.10f}")
    print(f"arcsine_packet_threshold_exponent={4.0 * DELTA_STAR:.10f}")
    print(f"full_arcsine_cost_exponent={25.0 / 66.0:.12f}")
    print()
    print("Y M carrier kind leverage sqrt_leverage leverage_over_M unresolved rank")
    for y in (100, 300, 1000, 3000):
        nodes = actual_nodes(y)
        left = y**LOW_EXPONENT
        right = y**HIGH_EXPONENT
        for carrier in (0.0, 7.0):
            q = np.cos(carrier * nodes)
            for kind in ("uniform", "arcsine"):
                gram = profile_gram(nodes, left, right, kind)
                leverage, unresolved, rank = directional_leverage(gram, q)
                print(
                    f"{y} {len(nodes)} {carrier:g} {kind} "
                    f"{leverage:.12g} {math.sqrt(leverage):.12g} "
                    f"{leverage / len(nodes):.12g} {unresolved:.3e} {rank}"
                )


if __name__ == "__main__":
    main()
