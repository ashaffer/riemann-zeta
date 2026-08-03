"""Test quartet-product phases of finite-element Weil ground states.

Horizontal displacements are hypothetical; known zeta zeros used here are on
the critical line.  This asks whether parity and ground-state shape alone
force the reflected product to be nonnegative.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import mpmath as mp
import numpy as np
import scipy.linalg

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from hp_margins import hp_form


def hat_laplace(s: complex, centers: np.ndarray, width: float) -> np.ndarray:
    return np.exp(s * centers) * 2 * (np.cosh(s * width) - 1) / (s * s * width)


def ground_state(L: float, m: int, dps: int):
    Qmp, Gmp = hp_form(L, m, dps=dps)
    Q = np.array(Qmp.tolist(), dtype=float)
    G = np.array(Gmp.tolist(), dtype=float)
    eigenvalue, vectors = scipy.linalg.eigh((Q + Q.T) / 2, (G + G.T) / 2,
                                            subset_by_index=[0, 0])
    half_support = L / 4
    width = (L / 2) / (m + 1)
    centers = np.linspace(-half_support + width, half_support - width, m)
    return float(eigenvalue[0]), vectors[:, 0], centers, width


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float, default=[1.75, 2.485, 2.996])
    parser.add_argument("--size", type=int, default=41)
    parser.add_argument("--zeros", type=int, default=20)
    parser.add_argument("--deltas", nargs="+", type=float, default=[0.05, 0.2, 0.35, 0.49])
    parser.add_argument("--dps", type=int, default=35)
    args = parser.parse_args()
    ordinates = [float(mp.im(mp.zetazero(k))) for k in range(1, args.zeros + 1)]
    print("L,lambda_min,negative,total,worst_phase,worst_delta,worst_gamma")
    for L in args.supports:
        eigenvalue, coeffs, centers, width = ground_state(L, args.size, args.dps)
        values = []
        for delta in args.deltas:
            for gamma in ordinates:
                alpha = delta + 1j * gamma
                fp = coeffs @ hat_laplace(alpha, centers, width)
                fm = coeffs @ hat_laplace(-alpha, centers, width)
                values.append(((fp * fm).real, delta, gamma))
        worst = min(values)
        negative = sum(value < 0 for value, _, _ in values)
        print(f"{L:.6g},{eigenvalue:.10e},{negative},{len(values)},"
              f"{worst[0]:.10e},{worst[1]:.6g},{worst[2]:.10g}")


if __name__ == "__main__":
    main()
