#!/usr/bin/env python3
"""Finite fail-fast checks for approximate positive polarization.

The exact quantity is

    eps(A,G) = ||G^(-1/2) (A^* G + G A - G) G^(-1/2)||_op.

For every eigenvalue ``lambda`` of ``A`` and every positive ``G``,
``eps(A,G) >= abs(2*Re(lambda)-1)``.  The script checks the exact 2-by-2
off-line and pole/Tate controls and runs a small zero-independent semilocal
experiment.

The semilocal metric is the moment Gram matrix of

    |Gamma(1/4+i s/2)|^2 |L_p(1/2+i s)|^2 ds.

It is fixed by gamma and Euler data, not fitted to zeta zeros.  The native
Galerkin scaling generator is built from multiplication by ``s`` and is an
exactly polarized positive control by construction.  Cross-stage columns
use the identity on the fixed monomial coefficient space and test whether the
old generator remains approximately polarized after the one-prime metric
update.  (The exact infinite semilocal Euler-multiplier isomorphism is a
different comparison and transports multiplication exactly.)  The columns
are numerical diagnostics, not interval certificates and not a spectral
realization of the zeta divisor.
"""
from __future__ import annotations

import argparse
from functools import lru_cache

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigvalsh
from scipy.special import loggamma


def gamma_weight(s: float) -> float:
    """Archimedean cyclic density, up to an irrelevant positive scalar."""
    return float(np.exp(2.0 * np.real(loggamma(0.25 + 0.5j * s))))


def local_factor_weight(prime: int, s: float) -> float:
    """The positive one-prime semilocal Euler multiplier."""
    q = prime ** -0.5
    return 1.0 / (1.0 + q * q - 2.0 * q * np.cos(s * np.log(prime)))


def relative_lyapunov_defect(generator: np.ndarray, metric: np.ndarray) -> float:
    """Return the sharp epsilon in the two-sided relative Loewner bound."""
    defect = generator.conj().T @ metric + metric @ generator - metric
    defect = 0.5 * (defect + defect.conj().T)
    generalized = eigvalsh(defect, metric)
    return float(np.max(np.abs(generalized)))


def off_line_generator(alpha: float) -> np.ndarray:
    """The functional-equation pair 1/2 +/- alpha."""
    return np.diag([0.5 + alpha, 0.5 - alpha]).astype(complex)


def pole_tate_generator() -> np.ndarray:
    """The ungraded pole/Tate control with spectral parameters 1 and 0."""
    return np.diag([1.0, 0.0]).astype(complex)


@lru_cache(maxsize=None)
def _moment(prime: int, power: int, cutoff: float) -> float:
    """Moment of the even semilocal density; odd moments vanish exactly."""
    if power % 2:
        return 0.0

    def integrand(s: float) -> float:
        value = (s ** power) * gamma_weight(s)
        if prime:
            value *= local_factor_weight(prime, s)
        return value

    return 2.0 * quad(
        integrand,
        0.0,
        cutoff,
        epsabs=1e-11,
        epsrel=1e-11,
        limit=300,
    )[0]


def semilocal_moment_pair(
    prime: int, dimension: int, cutoff: float
) -> tuple[np.ndarray, np.ndarray]:
    """Return Gram G and first shifted moment H for 1,s,...,s^(d-1)."""
    gram = np.empty((dimension, dimension), dtype=float)
    shifted = np.empty_like(gram)
    for i in range(dimension):
        for j in range(dimension):
            gram[i, j] = _moment(prime, i + j, cutoff)
            shifted[i, j] = _moment(prime, i + j + 1, cutoff)
    return gram, shifted


def scaling_generator(gram: np.ndarray, shifted: np.ndarray) -> np.ndarray:
    """Compression of 1/2+i*s in the monomial coefficient basis."""
    multiplication = np.linalg.solve(gram, shifted)
    return 0.5 * np.eye(gram.shape[0]) + 1j * multiplication


def update_eigenvalues(updated: np.ndarray, base: np.ndarray) -> np.ndarray:
    """Generalized Loewner update spectrum relative to the base metric."""
    return eigvalsh(updated - base, base)


def block_diagonal(*blocks: np.ndarray) -> np.ndarray:
    size = sum(block.shape[0] for block in blocks)
    answer = np.zeros((size, size), dtype=complex)
    cursor = 0
    for block in blocks:
        width = block.shape[0]
        answer[cursor:cursor + width, cursor:cursor + width] = block
        cursor += width
    return answer


def run_semilocal(prime: int, dimension: int, cutoff: float) -> tuple[float, ...]:
    arch_gram, arch_shift = semilocal_moment_pair(0, dimension, cutoff)
    prime_gram, prime_shift = semilocal_moment_pair(prime, dimension, cutoff)
    arch_generator = scaling_generator(arch_gram, arch_shift)
    prime_generator = scaling_generator(prime_gram, prime_shift)

    native_arch = relative_lyapunov_defect(arch_generator, arch_gram)
    native_prime = relative_lyapunov_defect(prime_generator, prime_gram)
    old_generator_new_metric = relative_lyapunov_defect(
        arch_generator, prime_gram
    )
    new_generator_old_metric = relative_lyapunov_defect(
        prime_generator, arch_gram
    )
    update = update_eigenvalues(prime_gram, arch_gram)

    all_generator = block_diagonal(prime_generator, pole_tate_generator())
    all_metric = block_diagonal(prime_gram, np.eye(2))
    all_place = relative_lyapunov_defect(all_generator, all_metric)
    return (
        native_arch,
        native_prime,
        old_generator_new_metric,
        new_generator_old_metric,
        float(update[0]),
        float(update[-1]),
        all_place,
        float(np.linalg.cond(prime_gram)),
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", nargs="+", type=int, default=[2, 3, 5, 7])
    parser.add_argument("--dimensions", nargs="+", type=int, default=[2, 3, 4])
    parser.add_argument("--cutoff", type=float, default=60.0)
    parser.add_argument("--alpha", type=float, default=0.2)
    args = parser.parse_args()

    identity = np.eye(2)
    off_line = relative_lyapunov_defect(
        off_line_generator(args.alpha), identity
    )
    pole = relative_lyapunov_defect(pole_tate_generator(), identity)
    print("analytic_controls_float_evaluation")
    print(
        "off_line_alpha,analytic_lower_bound,identity_metric_defect,"
        "pole_tate_lower_bound,pole_tate_identity_defect"
    )
    print(
        f"{args.alpha:.12g},{2.0 * abs(args.alpha):.12g},"
        f"{off_line:.12g},1,{pole:.12g}"
    )
    print()
    print("semilocal_diagnostics_not_interval_certificates")
    print(
        "prime,dimension,native_arch_defect,native_prime_defect,"
        "arch_generator_in_prime_metric,prime_generator_in_arch_metric,"
        "min_metric_update,max_metric_update,with_pole_tate_defect,"
        "prime_metric_condition"
    )
    for prime in args.primes:
        for dimension in args.dimensions:
            values = run_semilocal(prime, dimension, args.cutoff)
            rendered = ",".join(f"{value:.12e}" for value in values)
            print(f"{prime},{dimension},{rendered}")


if __name__ == "__main__":
    main()
