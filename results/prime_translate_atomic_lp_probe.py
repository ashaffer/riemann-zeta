#!/usr/bin/env python3
"""Finite Wiener-ball probe for the prime-translate nulling criterion.

This is exploratory evidence only.  On a logarithmic window around ``Y`` it
maximizes a Laplace moment of a real cosine polynomial subject to exact zeros
at every active prime-power logarithm and an l1 coefficient budget.  The
cosine restriction is much smaller than the admissible complex polarized
space, so a small optimum is not a no-go theorem.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import linprog


def prime_powers(limit: int) -> list[int]:
    """Return all n <= limit with von Mangoldt weight nonzero."""
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = False
    out: set[int] = set()
    for p in np.flatnonzero(sieve):
        q = int(p)
        while q <= limit:
            out.add(q)
            if q > limit // int(p):
                break
            q *= int(p)
    return sorted(out)


def solve_one(Y: float, width: float, alpha: float, bandwidth_ratio: float) -> dict:
    logY = math.log(Y)
    lower = Y * math.exp(-width)
    upper = Y * math.exp(width)
    nodes = [math.log(n / Y) for n in prime_powers(math.ceil(upper)) if lower <= n <= upper]

    bandwidth = bandwidth_ratio * Y
    max_mode = max(1, int(math.floor(bandwidth * logY / (2.0 * math.pi))))
    omega = 2.0 * math.pi * np.arange(max_mode + 1) / logY
    sample = np.cos(np.outer(nodes, omega))

    # The moment is against a fixed triangular cross-lobe weight.  For
    # s=alpha+i*freq,
    #
    #   integral_(-w)^w (1-|u|/w)e^(s*u)du
    #     = 2*(cosh(s*w)-1)/(w*s^2).
    #
    # Using the closed form avoids an increasingly ill-conditioned
    # oscillatory quadrature as the mode cutoff grows.
    def moment(freq: float) -> float:
        s = complex(alpha, freq)
        if abs(s) < 1e-14:
            return width
        return float((2.0 * (np.cosh(s * width) - 1.0) / (width * s * s)).real)

    target = np.array([moment(float(freq)) for freq in omega])
    # h=h_plus-h_minus, h_±>=0.  This is exactly ||h||_1<=1 for real h.
    objective = np.concatenate([-target, target])
    equality = np.concatenate([sample, -sample], axis=1)
    inequality = np.ones((1, 2 * len(target)))
    result = linprog(
        objective,
        A_ub=inequality,
        b_ub=np.array([1.0]),
        A_eq=equality,
        b_eq=np.zeros(len(nodes)),
        bounds=(0.0, None),
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    optimum = -float(result.fun)

    # Dual identity:
    #   sup{<target,h>: sample*h=0, ||h||_1<=1}
    #     = inf_y ||target-sample^T*y||_infinity.
    # Solving it separately is a useful conditioning check on the primal.
    dual_objective = np.zeros(len(nodes) + 1)
    dual_objective[-1] = 1.0
    dual_upper = np.block(
        [
            [sample.T, -np.ones((len(target), 1))],
            [-sample.T, -np.ones((len(target), 1))],
        ]
    )
    dual_rhs = np.concatenate([target, -target])
    dual = linprog(
        dual_objective,
        A_ub=dual_upper,
        b_ub=dual_rhs,
        bounds=[(None, None)] * len(nodes) + [(0.0, None)],
        method="highs",
    )
    if not dual.success:
        raise RuntimeError(dual.message)
    dual_optimum = float(dual.fun)
    unconstrained = float(np.max(np.abs(target)))
    residual = float(np.max(np.abs(equality @ result.x))) if nodes else 0.0
    return {
        "Y": Y,
        "nodes": len(nodes),
        "modes": len(target),
        "bandwidth": bandwidth,
        "optimum": optimum,
        "dual_optimum": dual_optimum,
        "duality_gap": abs(optimum - dual_optimum),
        "unconstrained": unconstrained,
        "ratio": optimum / unconstrained,
        "max_zero_residual": residual,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--Y", type=float, nargs="+", default=[100, 300, 1000, 3000])
    parser.add_argument("--width", type=float, default=0.2)
    parser.add_argument("--alpha", type=float, default=0.2)
    parser.add_argument("--bandwidth-ratio", type=float, default=0.5)
    args = parser.parse_args()
    for Y in args.Y:
        print(solve_one(Y, args.width, args.alpha, args.bandwidth_ratio))


if __name__ == "__main__":
    main()
