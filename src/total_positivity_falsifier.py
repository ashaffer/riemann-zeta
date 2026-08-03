"""Falsify total positivity of finite hat-Galerkin Weil Green matrices.

This is only a diagnostic: failure of a minor rules out this particular
ordered-basis total-positivity route, while success would not prove a
continuum theorem.
"""
from __future__ import annotations

import argparse
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from hp_margins import hp_form


def audit(L: float, m: int, dps: int) -> tuple[float, float, tuple[int, int], float, tuple[int, int]]:
    Qmp, _ = hp_form(L, m, dps=dps)
    Q = np.array(Qmp.tolist(), dtype=float)
    Q = (Q + Q.T) / 2
    least_eigenvalue = float(np.linalg.eigvalsh(Q)[0])
    green = np.linalg.inv(Q)
    entry_location = tuple(map(int, np.unravel_index(np.argmin(green), green.shape)))
    least_entry = float(green[entry_location])
    least_minor = float("inf")
    minor_location = (0, 0)
    for i in range(m - 1):
        for j in range(m - 1):
            minor = float(np.linalg.det(green[np.ix_([i, i + 1], [j, j + 1])]))
            if minor < least_minor:
                least_minor = minor
                minor_location = (i, j)
    return least_eigenvalue, least_entry, entry_location, least_minor, minor_location


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float, default=[1.75, 2.0, 2.485, 2.996])
    parser.add_argument("--sizes", nargs="+", type=int, default=[21, 41])
    parser.add_argument("--dps", type=int, default=35)
    args = parser.parse_args()
    print("L      m   lambda_min(Q)  min Green entry (i,j)       min adjacent minor (i,j)")
    for L in args.supports:
        for m in args.sizes:
            eig, entry, eloc, minor, mloc = audit(L, m, args.dps)
            print(f"{L:5.3f} {m:3d} {eig:14.6e} {entry:16.6e} {eloc!s:>9} "
                  f"{minor:20.6e} {mloc!s:>9}")


if __name__ == "__main__":
    main()
