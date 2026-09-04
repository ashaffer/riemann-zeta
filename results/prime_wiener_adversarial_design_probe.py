#!/usr/bin/env python3
"""Check the Chebyshev/Wiener adversarial-design identity on actual nodes.

This is an exploratory finite cosine restriction, not an asymptotic bound
for the full complex extremal E_Y.  It independently checks that the LP
extremizer supplies an optimal weighted least-squares design whose Schur
complement is E_cos^2.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import linprog


def prime_powers(limit: int) -> list[int]:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    values: set[int] = set()
    for p in np.flatnonzero(sieve):
        q = int(p)
        while q <= limit:
            values.add(q)
            if q > limit // int(p):
                break
            q *= int(p)
    return sorted(values)


def instance(Y: float, width: float, alpha: float, bandwidth_ratio: float):
    log_y = math.log(Y)
    lower, upper = Y * math.exp(-width), Y * math.exp(width)
    nodes = [
        math.log(n / Y)
        for n in prime_powers(math.ceil(upper))
        if lower <= n <= upper
    ]
    bandwidth = bandwidth_ratio * Y
    max_mode = max(1, int(math.floor(bandwidth * log_y / (2.0 * math.pi))))
    omega = 2.0 * math.pi * np.arange(max_mode + 1) / log_y
    V = np.cos(np.outer(nodes, omega))

    def moment(freq: float) -> float:
        s = complex(alpha, freq)
        if abs(s) < 1e-14:
            return width
        return float((2.0 * (np.cosh(s * width) - 1.0) / (width * s * s)).real)

    b = np.array([moment(float(freq)) for freq in omega])
    return nodes, omega, V, b


def solve(Y: float, width: float, alpha: float, bandwidth_ratio: float) -> dict:
    nodes, omega, V, b = instance(Y, width, alpha, bandwidth_ratio)
    d = len(b)

    # Primal: maximize b.h subject to Vh=0 and ||h||_1<=1.
    primal = linprog(
        np.concatenate([-b, b]),
        A_ub=np.ones((1, 2 * d)),
        b_ub=np.array([1.0]),
        A_eq=np.concatenate([V, -V], axis=1),
        b_eq=np.zeros(len(nodes)),
        bounds=(0.0, None),
        method="highs",
    )
    if not primal.success:
        raise RuntimeError(primal.message)
    h = primal.x[:d] - primal.x[d:]
    E = -float(primal.fun)

    # Dual Chebyshev approximation: min_y ||b-V^T y||_infinity.
    dual = linprog(
        np.r_[np.zeros(len(nodes)), 1.0],
        A_ub=np.block(
            [[V.T, -np.ones((d, 1))], [-V.T, -np.ones((d, 1))]]
        ),
        b_ub=np.r_[b, -b],
        bounds=[(None, None)] * len(nodes) + [(0.0, None)],
        method="highs",
    )
    if not dual.success:
        raise RuntimeError(dual.message)
    y = dual.x[:-1]
    residual = b - V.T @ y

    # Complementarity turns the primal mass into an adversarial design.
    mass = float(np.sum(np.abs(h)))
    w = np.abs(h) / mass
    sqrt_w = np.sqrt(w)
    Xw = sqrt_w[:, None] * V.T
    bw = sqrt_w * b
    y_wls, *_ = np.linalg.lstsq(Xw, bw, rcond=None)
    r_wls = b - V.T @ y_wls
    design_value = float(np.dot(w, r_wls * r_wls))
    normal_residual = float(np.max(np.abs(V @ (w * r_wls)))) if nodes else 0.0

    support = np.flatnonzero(w > 1e-9)
    equioscillation_error = (
        float(np.max(np.abs(np.abs(residual[support]) - E))) if len(support) else 0.0
    )
    return {
        "Y": Y,
        "nodes": len(nodes),
        "modes": len(omega),
        "E_cos": E,
        "dual_E": float(dual.fun),
        "sqrt_design_schur": math.sqrt(max(design_value, 0.0)),
        "design_support": len(support),
        "support_bound_M_plus_1": len(nodes) + 1,
        "normal_equation_residual": normal_residual,
        "equioscillation_error": equioscillation_error,
        "prime_null_residual": float(np.max(np.abs(V @ h))) if nodes else 0.0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--Y", nargs="+", type=float, default=[50, 100, 200, 300])
    parser.add_argument("--width", type=float, default=0.2)
    parser.add_argument("--alpha", type=float, default=0.49)
    parser.add_argument("--bandwidth-ratio", type=float, default=2.0)
    args = parser.parse_args()
    for Y in args.Y:
        print(solve(Y, args.width, args.alpha, args.bandwidth_ratio))


if __name__ == "__main__":
    main()
