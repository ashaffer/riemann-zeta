"""Fail-fast Pick-matrix scan for the shifted completed-zeta ratio."""
from __future__ import annotations

import argparse

import mpmath as mp
import numpy as np


def xi(s: mp.mpc) -> mp.mpc:
    return (mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2)
            * mp.gamma(s / 2) * mp.zeta(s))


def shifted_ratio(a: float, z: complex) -> mp.mpc:
    return xi(mp.mpf("0.5") + a + 1j * z) / xi(
        mp.mpf("0.5") - a + 1j * z)


def pick_matrix(a: float, points: list[complex]) -> np.ndarray:
    values = [shifted_ratio(a, z) for z in points]
    matrix = np.array([
        [complex((1 - values[i] * mp.conj(values[j]))
                 / (-1j * (points[i] - points[j].conjugate())))
         for j in range(len(points))]
        for i in range(len(points))
    ])
    return (matrix + matrix.conj().T) / 2


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shifts", nargs="+", type=float,
                        default=[0.6, 0.5, 0.4, 0.25, 0.1, 0.05])
    parser.add_argument("--dps", type=int, default=50)
    args = parser.parse_args()
    mp.mp.dps = args.dps

    # Avoid real arguments at the removable gamma/zeta singularities in the
    # elementary xi product formula.
    points = [0.73j, 5 + 0.7j, 10 + 0.7j, 14 + 0.3j,
              14 + 1.1j, 20 + 0.7j, 30 + 0.7j]
    print("a,min_eigenvalue,negative_eigenvalues,max_sample_modulus")
    for a in args.shifts:
        matrix = pick_matrix(a, points)
        eigenvalues = np.linalg.eigvalsh(matrix)
        ratios = [abs(shifted_ratio(a, z)) for z in points]
        print(f"{a:.9g},{eigenvalues[0]:.12e},"
              f"{np.count_nonzero(eigenvalues < -1e-9)},"
              f"{float(max(ratios)):.12e}")


if __name__ == "__main__":
    main()
