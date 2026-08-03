#!/usr/bin/env python3
"""Arithmetic-side Galerkin test of event-window old/collar cross ratios.

Compact polynomial bumps provide independent old and two-sided collar bases.
The matrix uses the pole term and the Fourier multiplier

  Re psi(1/4+i*pi*xi) - log(pi)
    - sum_active 2 Lambda(n)/sqrt(n) cos(2*pi*log(n)*xi).

No zeta zeros or RH assumptions enter.  Results remain numerical diagnostics;
frequency truncation and quadrature errors are not interval-certified.
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


def interval_basis(left: float, right: float, degree: int, smooth_power: int,
                   quadrature: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return nodes, physical weights, and an L2-orthonormal bump basis."""
    t, wt = leggauss(quadrature)
    half = (right - left) / 2.0
    center = (right + left) / 2.0
    x = center + half * t
    wx = half * wt
    envelope = np.maximum(0.0, 1.0 - t * t) ** smooth_power
    raw = legvander(t, degree - 1) * envelope[:, None]
    gram = raw.T @ (wx[:, None] * raw)
    values, vectors = np.linalg.eigh((gram + gram.T) / 2.0)
    transform = vectors @ np.diag(values ** -0.5) @ vectors.T
    return x, wx, raw @ transform


def combined_basis(a: float, b: float, old_degree: int, collar_degree: int,
                   smooth_power: int, xquad: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    pieces = [
        interval_basis(-a, a, old_degree, smooth_power, xquad),
        interval_basis(-b, -a, collar_degree, smooth_power, xquad),
        interval_basis(a, b, collar_degree, smooth_power, xquad),
    ]
    total_degree = old_degree + 2 * collar_degree
    nodes, weights, blocks = [], [], []
    offset = 0
    for x, wx, local in pieces:
        block = np.zeros((len(x), total_degree))
        block[:, offset:offset + local.shape[1]] = local
        offset += local.shape[1]
        nodes.append(x)
        weights.append(wx)
        blocks.append(block)
    return np.concatenate(nodes), np.concatenate(weights), np.vstack(blocks)


def weil_matrix(a: float, b: float, active: list[tuple[int, float]],
                old_degree: int, collar_degree: int, smooth_power: int,
                xquad: int, xmax: float, dxi: float, chunk: int) -> np.ndarray:
    x, wx, basis = combined_basis(a, b, old_degree, collar_degree,
                                  smooth_power, xquad)
    weighted_basis = wx[:, None] * basis
    dimension = basis.shape[1]
    matrix = np.zeros((dimension, dimension))

    xis = np.arange(-xmax, xmax + dxi / 2.0, dxi)
    integration_weights = np.full(len(xis), dxi)
    integration_weights[[0, -1]] *= 0.5
    for start in range(0, len(xis), chunk):
        xi = xis[start:start + chunk]
        wi = integration_weights[start:start + chunk]
        fourier = np.exp(-2j * math.pi * np.outer(xi, x)) @ weighted_basis
        symbol = np.real(digamma(0.25 + 1j * math.pi * xi)) - math.log(math.pi)
        for n, logp in active:
            symbol -= 2.0 * logp / math.sqrt(n) * np.cos(2.0 * math.pi * math.log(n) * xi)
        matrix += np.real(fourier.conj().T @ ((wi * symbol)[:, None] * fourier))

    pole_plus = (wx * np.exp(x / 2.0)) @ basis
    pole_minus = (wx * np.exp(-x / 2.0)) @ basis
    matrix += np.outer(pole_plus, pole_minus) + np.outer(pole_minus, pole_plus)
    return (matrix + matrix.T) / 2.0


def block_statistics(matrix: np.ndarray, old_degree: int) -> tuple[float, float, float]:
    old = matrix[:old_degree, :old_degree]
    collar = matrix[old_degree:, old_degree:]
    cross = matrix[:old_degree, old_degree:]
    eo, uo = np.linalg.eigh(old)
    ec, uc = np.linalg.eigh(collar)
    if eo[0] <= 0.0 or ec[0] <= 0.0:
        return float(eo[0]), float(ec[0]), math.inf
    normalized = ((uo / np.sqrt(eo)[None, :]).T @ cross @
                  (uc / np.sqrt(ec)[None, :]))
    ratio = float(np.linalg.svd(normalized, compute_uv=False)[0])
    return float(eo[0]), float(ec[0]), ratio


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=float, default=7.0 / 16.0)
    parser.add_argument("--stop", type=float, default=2.0)
    parser.add_argument("--old-degree", type=int, default=8)
    parser.add_argument("--collar-degree", type=int, default=4)
    parser.add_argument("--smooth-power", type=int, default=4)
    parser.add_argument("--xquad", type=int, default=80)
    parser.add_argument("--xmax", type=float, default=160.0)
    parser.add_argument("--dxi", type=float, default=0.04)
    parser.add_argument("--chunk", type=int, default=512)
    parser.add_argument("--output", type=Path, default=Path("results/event-cross-ratios.csv"))
    args = parser.parse_args()

    powers = prime_powers(math.ceil(math.exp(2.0 * args.stop)) + 10)
    thresholds = sorted({math.log(n) / 2.0 for n, _ in powers if math.log(n) / 2.0 > args.start})
    rows = []
    a = args.start
    for b in thresholds:
        if b > args.stop:
            break
        active = [(n, lp) for n, lp in powers if math.log(n) < 2.0 * b - 1e-12]
        matrix = weil_matrix(a, b, active, args.old_degree, args.collar_degree,
                             args.smooth_power, args.xquad, args.xmax,
                             args.dxi, args.chunk)
        old_min, collar_min, ratio = block_statistics(matrix, args.old_degree)
        rows.append({"a": a, "b": b, "width": b - a, "active": len(active),
                     "old_min": old_min, "collar_min": collar_min,
                     "cross_ratio": ratio})
        a = b

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    finite = [row for row in rows if math.isfinite(float(row["cross_ratio"]))]
    worst = max(finite, key=lambda row: float(row["cross_ratio"])) if finite else None
    print(f"events={len(rows)} finite_ratios={len(finite)}")
    print(f"negative_old={sum(float(r['old_min']) <= 0 for r in rows)} "
          f"negative_collar={sum(float(r['collar_min']) <= 0 for r in rows)}")
    if worst:
        print("worst_ratio={cross_ratio:.12g} a={a:.9g} b={b:.9g} width={width:.3g}".format(**worst))
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
