"""Galerkin diagnostic for the codimension-two relative Weil complex.

The two moment constraints are orthogonality to exp(x/2) and exp(-x/2).
They annihilate the rank-(1,1) pole form.  This script projects the independently
assembled pole-free archimedean-minus-prime matrix onto that moment kernel and
reports its smallest Ritz values.
"""
from __future__ import annotations

import argparse

import mpmath as mp
import numpy as np
from scipy.linalg import null_space

from spectral_margins import gl_nodes, legvals, spectral_form


def moment_vectors(support: float, dimension: int) -> tuple[np.ndarray, np.ndarray]:
    """Legendre coordinates of exp(+x/2) and exp(-x/2)."""
    a = mp.mpf(support) / 4
    normalizers = [mp.sqrt(mp.mpf(2 * k + 1) / (2 * a))
                   for k in range(dimension)]
    nodes = gl_nodes(max(dimension + 4, 96))
    plus = np.zeros(dimension)
    minus = np.zeros(dimension)
    for node, weight in nodes:
        x = a * node
        scaled_weight = weight * a
        values = legvals(dimension, node)
        for k in range(dimension):
            common = scaled_weight * values[k] * normalizers[k]
            plus[k] += float(common * mp.exp(x / 2))
            minus[k] += float(common * mp.exp(-x / 2))
    return plus, minus


def relative_ritz_values(support: float, dimension: int, dps: int) -> np.ndarray:
    """Ritz spectrum after imposing both exact moment constraints."""
    form = np.array(spectral_form(
        support, dimension, dps=dps, zeta_pole=False).tolist(), dtype=float)
    plus, minus = moment_vectors(support, dimension)
    relative_basis = null_space(np.vstack([plus, minus]))
    return np.linalg.eigvalsh(relative_basis.T @ form @ relative_basis)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[1.75, 2.485, 2.996, 3.555, 4.04])
    parser.add_argument("--dimension", type=int, default=20)
    parser.add_argument("--dps", type=int, default=25)
    args = parser.parse_args()

    mp.mp.dps = args.dps
    print("support,dimension,min_relative,next_relative")
    for support in args.supports:
        values = relative_ritz_values(support, args.dimension, args.dps)
        print(f"{support:.9g},{args.dimension},"
              f"{values[0]:.12e},{values[1]:.12e}")


if __name__ == "__main__":
    main()
