#!/usr/bin/env python3
"""Galerkin test of the low-frequency pole/archimedean/event form.

The basis is the first N orthonormal Legendre functions on [-a,a].  For a
prime-power activation n at a = log(n)/2, the tested matrix is

  pole + integral_{|xi|<=cutoff}
    [A(xi) - 2 Lambda(n)/sqrt(n) cos(2 pi log(n) xi)] F_i conj(F_j) dxi.

Negative eigenvalues are rigorous counterexamples only after interval-error
certification; here they are diagnostic witnesses for the proposed mechanism.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from scipy.special import digamma
from sympy import primerange


def prime_powers(limit: int) -> list[tuple[int, float]]:
    values: dict[int, float] = {}
    for p in primerange(2, limit + 1):
        q = p
        while q <= limit:
            values[q] = math.log(p)
            if q > limit // p:
                break
            q *= p
    return sorted(values.items())


def event_matrix(n: int, logp: float, degree: int, cutoff: float,
                 xquad: int, fquad: int) -> np.ndarray:
    a = math.log(n) / 2.0
    tx, wx = leggauss(xquad)
    x = a * tx
    physical_weights = a * wx
    basis = legvander(tx, degree - 1)
    basis *= np.sqrt((2.0 * np.arange(degree) + 1.0) / (2.0 * a))

    tf, wf = leggauss(fquad)
    xi = cutoff * tf
    frequency_weights = cutoff * wf
    phase = np.exp(-2j * math.pi * np.outer(xi, x))
    fourier = phase @ (physical_weights[:, None] * basis)

    arch = np.real(digamma(0.25 + 1j * math.pi * xi)) - math.log(math.pi)
    amplitude = 2.0 * logp / math.sqrt(n)
    symbol = arch - amplitude * np.cos(2.0 * math.pi * math.log(n) * xi)
    weighted = frequency_weights * symbol
    band = np.real(fourier.conj().T @ (weighted[:, None] * fourier))

    pole_plus = (physical_weights * np.exp(x / 2.0)) @ basis
    pole_minus = (physical_weights * np.exp(-x / 2.0)) @ basis
    pole = np.outer(pole_plus, pole_minus) + np.outer(pole_minus, pole_plus)
    matrix = pole + band
    return (matrix + matrix.T) / 2.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stop", type=float, default=4.0,
                        help="maximum support threshold log(n)/2")
    parser.add_argument("--degree", type=int, default=20)
    parser.add_argument("--cutoff", type=float, default=5.0)
    parser.add_argument("--xquad", type=int, default=120)
    parser.add_argument("--fquad", type=int, default=180)
    parser.add_argument("--output", type=Path,
                        default=Path("results/low-frequency-events.csv"))
    parser.add_argument("--witness", type=Path,
                        default=Path("results/low-frequency-worst-witness.npz"))
    args = parser.parse_args()

    events = prime_powers(math.ceil(math.exp(2.0 * args.stop)))
    rows: list[dict[str, float | int]] = []
    worst: tuple[float, int, float, np.ndarray] | None = None
    for n, logp in events:
        a = math.log(n) / 2.0
        if a > args.stop:
            continue
        matrix = event_matrix(n, logp, args.degree, args.cutoff,
                              args.xquad, args.fquad)
        values, vectors = np.linalg.eigh(matrix)
        lam = float(values[0])
        rows.append({"n": n, "a": a, "amplitude": 2.0 * logp / math.sqrt(n),
                     "lambda_min": lam})
        if worst is None or lam < worst[0]:
            worst = (lam, n, a, vectors[:, 0])

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["n", "a", "amplitude", "lambda_min"])
        writer.writeheader()
        writer.writerows(rows)
    assert worst is not None
    np.savez(args.witness, lambda_min=worst[0], n=worst[1], a=worst[2],
             coefficients=worst[3], degree=args.degree, cutoff=args.cutoff)
    negative = sum(float(row["lambda_min"]) < 0.0 for row in rows)
    print(f"events={len(rows)} negative={negative}")
    print(f"worst_lambda={worst[0]:.12g} n={worst[1]} a={worst[2]:.12g}")
    print(f"csv={args.output} witness={args.witness}")


if __name__ == "__main__":
    main()
