#!/usr/bin/env python3
"""Finite checks for the R178 divisor-commutator and prime Hodge identities."""

from __future__ import annotations

import math

import numpy as np


def mobius(n: int) -> int:
    value = 1
    p = 2
    while p * p <= n:
        if n % p:
            p += 1
            continue
        n //= p
        value = -value
        if n % p == 0:
            return 0
        while n % p == 0:
            n //= p
        p += 1
    if n > 1:
        value = -value
    return value


def divisor_matrices(limit: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    zeta = np.zeros((limit, limit), dtype=float)
    moebius = np.zeros_like(zeta)
    for n in range(1, limit + 1):
        for d in range(1, n + 1):
            if n % d == 0:
                zeta[n - 1, d - 1] = 1.0
                moebius[n - 1, d - 1] = mobius(n // d)
    grading = np.diag([math.log(n) for n in range(1, limit + 1)])
    return zeta, moebius, grading


def main() -> None:
    limit = 30
    zeta, moebius, grading = divisor_matrices(limit)
    identity_error = np.max(np.abs(zeta @ moebius - np.eye(limit)))

    commutator = moebius @ grading - grading @ moebius
    expected = np.zeros_like(commutator)
    for n in range(1, limit + 1):
        for d in range(1, n + 1):
            if n % d == 0:
                q = n // d
                expected[n - 1, d - 1] = -mobius(q) * math.log(q)
    commutator_error = np.max(np.abs(commutator - expected))

    primes = np.array([5.0, 7.0, 11.0, 13.0])
    logs = np.log(primes)
    ones = np.ones(len(primes))
    raw = 2.0 * np.diag(logs) - np.outer(logs, ones) - np.outer(ones, logs)
    projection = np.eye(len(primes)) - np.outer(ones, ones) / len(primes)
    projected_error = np.max(
        np.abs(projection @ raw @ projection - 2.0 * projection @ np.diag(logs) @ projection)
    )
    inertia = np.linalg.eigvalsh(raw)

    weights = 1.0 / primes
    weighted = np.diag(weights) @ raw @ np.diag(weights)
    rng = np.random.default_rng(178)
    vector = rng.normal(size=len(primes))
    weighted_mean = np.dot(weights, vector) / np.dot(weights, weights)
    vector -= weighted_mean * weights
    weighted_energy = float(vector @ weighted @ vector)
    diagonal_energy = float(2.0 * np.sum(logs * (weights * vector) ** 2))

    r = 11
    k = 3
    phases = []
    for x in range(1, r):
        inverse = pow(x, -1, r)
        phases.append(np.exp(-2j * np.pi * k * inverse / r))
    ramanujan_mean_error = abs(np.mean(phases) + 1.0 / (r - 1))

    print(f"divisor inverse error:       {identity_error:.3e}")
    print(f"commutator identity error:   {commutator_error:.3e}")
    print(f"projected Hodge error:       {projected_error:.3e}")
    print(f"prime-block eigenvalues:     {inertia}")
    print(f"weighted energy error:       {abs(weighted_energy-diagonal_energy):.3e}")
    print(f"Ramanujan mean error:        {ramanujan_mean_error:.3e}")


if __name__ == "__main__":
    main()
