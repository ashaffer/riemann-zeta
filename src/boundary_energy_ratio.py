"""Stress-test relative boundary no-concentration for the zeta Weil form.

For the hat Galerkin space at support parameter L, form the matrix H(delta)
of L2 mass in the two endpoint slivers of spatial width delta.  The largest
generalized eigenvalue

    max_{c != 0} c^T H(delta)c / c^T Q_L c

is the sharp finite-dimensional boundary-mass/Weil-energy ratio.  Growth in
m or faster growth than the logarithmic boundary scale is evidence against a
support-uniform relative no-concentration estimate.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import numpy as np
import scipy.linalg

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from hp_margins import hp_form


def hat_values(x: np.ndarray, centers: np.ndarray, half_width: float) -> np.ndarray:
    return np.maximum(1.0 - np.abs(x[:, None] - centers[None, :]) / half_width, 0.0)


def boundary_mass_matrix(L: float, m: int, delta: float) -> np.ndarray:
    """Gram matrix on [-a,-a+delta] union [a-delta,a], a=L/4.

    Three-point Gauss--Legendre is exact on each breakpoint interval because
    a product of two piecewise-linear hats is piecewise quadratic.
    """
    a = L / 4.0
    d = (L / 2.0) / (m + 1)
    centers = np.linspace(-a + d, a - d, m)
    delta = min(max(delta, 0.0), a)
    slivers = [(-a, -a + delta), (a - delta, a)]
    nodes, weights = np.polynomial.legendre.leggauss(3)
    H = np.zeros((m, m))
    hat_breaks = np.concatenate((centers - d, centers, centers + d))
    for left, right in slivers:
        breaks = np.unique(np.concatenate(([left, right], hat_breaks)))
        breaks = breaks[(breaks >= left) & (breaks <= right)]
        for lo, hi in zip(breaks[:-1], breaks[1:]):
            if hi <= lo:
                continue
            x = (lo + hi) / 2 + (hi - lo) / 2 * nodes
            V = hat_values(x, centers, d)
            H += (hi - lo) / 2 * (V.T @ (weights[:, None] * V))
    return (H + H.T) / 2


def assemble_weil(L: float, m: int, dps: int) -> tuple[np.ndarray, np.ndarray, float, np.ndarray]:
    Qmp, Gmp = hp_form(L, m, dps=dps)
    Q = np.array(Qmp.tolist(), dtype=float)
    G = np.array(Gmp.tolist(), dtype=float)
    Q = (Q + Q.T) / 2
    eig, vec = scipy.linalg.eigh(Q, G, subset_by_index=[0, 0],
                                 check_finite=False)
    return Q, G, eig[0], vec[:, 0]


def worst_ratio(Q: np.ndarray, G: np.ndarray, ground: np.ndarray,
                L: float, m: int, delta: float) -> tuple[float, float, float]:
    H = boundary_mass_matrix(L, m, delta)
    ratios, vectors = scipy.linalg.eigh(H, Q, check_finite=False)
    ratio = ratios[-1]
    optimizer = vectors[:, -1]
    optimizer /= np.sqrt(optimizer @ G @ optimizer)
    alignment = abs(ground @ G @ optimizer)
    # For H/Q <= C/log(1/delta), this is the smallest required constant C.
    scaled = ratio * np.log(1.0 / delta) if 0 < delta < 1 else np.nan
    return ratio, scaled, alignment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[1.75, 2.0, 2.485, 2.996])
    parser.add_argument("--sizes", nargs="+", type=int, default=[41, 81])
    parser.add_argument("--deltas", nargs="+", type=float,
                        default=[0.1, 0.05, 0.02, 0.01])
    parser.add_argument("--dps", type=int, default=40)
    args = parser.parse_args()

    print("L      m   delta      lambda_min       worst H/Q       required C_log     ground-align")
    for L in args.supports:
        for m in args.sizes:
            Q, G, lam, ground = assemble_weil(L, m, args.dps)
            for delta in args.deltas:
                try:
                    ratio, scaled, alignment = worst_ratio(Q, G, ground, L, m, delta)
                    print(f"{L:5.3f} {m:4d} {delta:7.4f}  {lam:13.5e}  "
                          f"{ratio:13.5e}  {scaled:13.5e}  {alignment:12.5f}")
                except np.linalg.LinAlgError as exc:
                    print(f"{L:5.3f} {m:4d} {delta:7.4f}  FAILED: {exc}")


if __name__ == "__main__":
    main()
