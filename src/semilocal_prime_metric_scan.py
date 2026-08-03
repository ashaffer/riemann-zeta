"""Test Loewner ordering of one-prime semilocal moment metrics.

The archimedean cyclic measure is proportional to
|Gamma(1/4+i s/2)|^2 ds.  Adjoining p multiplies it by
|L_p(1/2+i s)|^2.  We assemble even-monomial Gram matrices and report the
generalized eigenvalues of G_p-G_infinity relative to G_infinity.
"""
from __future__ import annotations

import argparse

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigvalsh
from scipy.special import loggamma


def gamma_weight(s: float) -> float:
    return float(np.exp(2 * np.real(loggamma(0.25 + 0.5j * s))))


def local_factor_weight(prime: int, s: float) -> float:
    q = prime ** -0.5
    return 1 / (1 + q * q - 2 * q * np.cos(s * np.log(prime)))


def even_moment_grams(prime: int, dimension: int) -> tuple[np.ndarray, np.ndarray]:
    arch = np.zeros((dimension, dimension))
    updated = np.zeros_like(arch)
    for i in range(dimension):
        for j in range(i, dimension):
            power = 2 * (i + j)

            def base_integrand(s: float) -> float:
                return (s ** power) * gamma_weight(s)

            def updated_integrand(s: float) -> float:
                return base_integrand(s) * local_factor_weight(prime, s)

            base = 2 * quad(base_integrand, 0, 60, epsabs=1e-11,
                            epsrel=1e-11, limit=300)[0]
            new = 2 * quad(updated_integrand, 0, 60, epsabs=1e-11,
                           epsrel=1e-11, limit=300)[0]
            arch[i, j] = arch[j, i] = base
            updated[i, j] = updated[j, i] = new
    return arch, updated


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", nargs="+", type=int, default=[2, 3, 5, 7])
    parser.add_argument("--dimensions", nargs="+", type=int, default=[2, 3, 4])
    args = parser.parse_args()

    print("prime,dimension,min_update,max_update")
    for prime in args.primes:
        for dimension in args.dimensions:
            arch, updated = even_moment_grams(prime, dimension)
            eigenvalues = eigvalsh(updated - arch, arch)
            print(f"{prime},{dimension},{eigenvalues[0]:.12e},"
                  f"{eigenvalues[-1]:.12e}")


if __name__ == "__main__":
    main()
