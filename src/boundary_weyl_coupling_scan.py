"""Fail-fast perturbation test for the boundary-Weyl inertia mechanism.

Scale the entire prime adjacency by r while leaving the archimedean operator
fixed.  If Poisson/parity alone protected the boundary signature mechanism,
the one-negative-direction chamber would persist structurally.  Crossings near
r=1 show instead that its orientation depends on the exact arithmetic balance.
"""
from __future__ import annotations

import argparse

import numpy as np
from scipy.linalg import null_space

from relative_incidence_gap import moment_vectors
from spectral_margins import spectral_form


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--support", type=float, default=2.485)
    parser.add_argument("--dimension", type=int, default=24)
    parser.add_argument("--dps", type=int, default=25)
    parser.add_argument("--couplings", nargs="+", type=float,
                        default=[0.999, 0.9995, 0.9999, 1.0,
                                 1.0001, 1.0005, 1.001])
    args = parser.parse_args()

    arch = np.array(spectral_form(
        args.support, args.dimension, dps=args.dps, zeta_pole=False,
        include_primes=False).tolist(), dtype=float)
    arithmetic = np.array(spectral_form(
        args.support, args.dimension, dps=args.dps,
        zeta_pole=False).tolist(), dtype=float)
    prime_adjacency = arch - arithmetic

    plus, minus = moment_vectors(args.support, args.dimension)
    even_moment = (plus + minus) / 2
    odd_moment = (plus - minus) / 2
    relative_basis = null_space(np.vstack([plus, minus]))

    print("coupling,negative_index,min_relative,K_even,K_odd")
    for coupling in args.couplings:
        operator = arch - coupling * prime_adjacency
        eigenvalues = np.linalg.eigvalsh(operator)
        relative = relative_basis.T @ operator @ relative_basis
        relative_minimum = np.linalg.eigvalsh(relative)[0]
        k_even = even_moment @ np.linalg.solve(operator, even_moment)
        k_odd = odd_moment @ np.linalg.solve(operator, odd_moment)
        negative_index = int(np.sum(eigenvalues < -1e-10))
        print(f"{coupling:.12g},{negative_index},{relative_minimum:.12e},"
              f"{k_even:.12e},{k_odd:.12e}")


if __name__ == "__main__":
    main()
