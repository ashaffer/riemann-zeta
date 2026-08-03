"""Compare the relative incidence Ritz gap with its exact degree threshold.

On the two-moment subspace the incidence energy is E=Q+D||f||^2.  Therefore
the best Galerkin Poincare ratio is 1+lambda_relative/D.  Values approaching
one quantify why any generic inequality with uniform multiplicative slack is
structurally impossible.
"""
from __future__ import annotations

import argparse

import mpmath as mp
import numpy as np
from scipy.linalg import null_space

from relative_incidence_gap import moment_vectors
from spectral_margins import spectral_form
from weil_core import PRIME_POWERS


def degree_deficit(support: float) -> mp.mpf:
    value = -(mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi))
    for n, prime in PRIME_POWERS:
        if 2 * mp.log(n) < support:
            value += 2 * mp.log(prime) / mp.sqrt(n)
    return value


def constrained_component_values(
        support: float, dimension: int, dps: int) -> tuple[float, ...]:
    """Return the joint gap and the separately minimized incidence floors.

    The pole-free Weil matrix is ``Q=E_infty+E_prime-D I``.  Adding the
    corresponding scalar degrees to the archimedean and prime pieces recovers
    their nonnegative translation-defect energies.  Comparing the minimum of
    their sum with the sum of their separate minima measures the phase-sensitive
    transversality that ordinary tensorization discards.
    """
    total_q = np.array(spectral_form(
        support, dimension, dps=dps, include_primes=True,
        zeta_pole=False).tolist(), dtype=float)
    arch_q = np.array(spectral_form(
        support, dimension, dps=dps, include_primes=False,
        zeta_pole=False).tolist(), dtype=float)
    plus, minus = moment_vectors(support, dimension)
    relative_basis = null_space(np.vstack([plus, minus]))

    degree = float(degree_deficit(support))
    arch_degree = float(-(mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi)))
    prime_degree = degree - arch_degree
    identity = np.eye(dimension)

    def floor(matrix: np.ndarray) -> float:
        compressed = relative_basis.T @ matrix @ relative_basis
        return float(np.linalg.eigvalsh(compressed)[0])

    relative_gap = floor(total_q)
    arch_floor = floor(arch_q + arch_degree * identity)
    prime_floor = floor(total_q - arch_q + prime_degree * identity)
    joint_floor = relative_gap + degree
    separate_floor = arch_floor + prime_floor
    synergy = joint_floor - separate_floor
    return (degree, relative_gap, arch_floor, prime_floor,
            separate_floor - degree, synergy)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[1.75, 2.485, 2.996, 3.555, 4.04])
    parser.add_argument("--dimension", type=int, default=20)
    parser.add_argument("--dps", type=int, default=22)
    args = parser.parse_args()
    mp.mp.dps = args.dps

    print("support,dimension,degree,relative_gap,ratio_excess,"
          "arch_floor,prime_floor,separate_floor_minus_degree,synergy")
    for support in args.supports:
        (degree, gap, arch_floor, prime_floor,
         separate_deficit, synergy) = constrained_component_values(
             support, args.dimension, args.dps)
        print(f"{support:.9g},{args.dimension},{degree:.12e},"
              f"{gap:.12e},{gap / degree:.12e},{arch_floor:.12e},"
              f"{prime_floor:.12e},{separate_deficit:.12e},"
              f"{synergy:.12e}")


if __name__ == "__main__":
    main()
