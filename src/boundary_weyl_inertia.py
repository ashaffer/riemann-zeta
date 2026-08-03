"""Boundary Weyl/inertia diagnostic for the relative incidence complex.

For the pole-free operator T and moment map M=(exp(x/2),exp(-x/2)), compute
K=M^T T^{-1}M.  Parity changes the boundary coordinates to cosh/sinh and
diagonalizes K.  Haynsworth inertia additivity says that the signature of T on
ker(M^T) is obtained by subtracting the signature of K from that of T.
"""
from __future__ import annotations

import argparse

import mpmath as mp
import numpy as np
from scipy.linalg import null_space

from relative_incidence_gap import moment_vectors
from spectral_margins import spectral_form


def signs(values: np.ndarray, tolerance: float = 1e-12) -> tuple[int, int, int]:
    """Return numbers of negative, zero-sized, and positive eigenvalues."""
    return (int(np.sum(values < -tolerance)),
            int(np.sum(np.abs(values) <= tolerance)),
            int(np.sum(values > tolerance)))


def checkpoint(support: float, dimension: int, dps: int) -> tuple[object, ...]:
    form = np.array(spectral_form(
        support, dimension, dps=dps, zeta_pole=False).tolist(), dtype=float)
    plus, minus = moment_vectors(support, dimension)
    even_moment = (plus + minus) / 2
    odd_moment = (plus - minus) / 2

    solve_even = np.linalg.solve(form, even_moment)
    solve_odd = np.linalg.solve(form, odd_moment)
    k_even = even_moment @ solve_even
    k_odd = odd_moment @ solve_odd
    k_cross = even_moment @ solve_odd

    relative_basis = null_space(np.vstack([plus, minus]))
    relative = relative_basis.T @ form @ relative_basis
    form_eigenvalues = np.linalg.eigvalsh(form)
    relative_eigenvalues = np.linalg.eigvalsh(relative)
    boundary_eigenvalues = np.linalg.eigvalsh(
        np.array([[k_even, k_cross], [k_cross, k_odd]]))

    return (signs(form_eigenvalues), signs(boundary_eigenvalues),
            signs(relative_eigenvalues), form_eigenvalues[0],
            relative_eigenvalues[0], k_even, k_odd, k_cross,
            k_even * k_odd - k_cross * k_cross)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[1.75, 2.485, 2.996, 3.555, 4.04])
    parser.add_argument("--dimensions", nargs="+", type=int,
                        default=[12, 16, 20])
    parser.add_argument("--dps", type=int, default=22)
    args = parser.parse_args()
    mp.mp.dps = args.dps

    print("support,m,inertia_T,inertia_K,inertia_relative,min_T,min_relative,"
          "K_even,K_odd,K_cross,det_K")
    for support in args.supports:
        for dimension in args.dimensions:
            data = checkpoint(support, dimension, args.dps)
            inertias = [f"{n}/{z}/{p}" for n, z, p in data[:3]]
            scalars = [f"{value:.12e}" for value in data[3:]]
            print(f"{support:.9g},{dimension}," +
                  ",".join(inertias + scalars))


if __name__ == "__main__":
    main()
