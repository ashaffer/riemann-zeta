#!/usr/bin/env python3
"""Exact finite certificates for the global common-dual prime-beat frame.

For a set of distinct primes ``P`` and every ordered pair ``p != r``, use
all primitive Fourier columns modulo ``p*r`` on an interval of ``H``
integers.  Summing the pairwise Ramanujan Gramians gives an explicit global
frame operator.  Its canonical dual has the coefficient-specific form

    gamma[p,r,theta] = W(theta/(p*r)),

where one common trigonometric polynomial ``W`` is used for every pair.

This module checks the exact algebra and finite reconstruction.  It does not
estimate a zeta sum or prove a zero-free region.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np

from farey_beat_frame_probe import primitive_frame_matrix
from finite_ramanujan_completion_probe import expected_von_mangoldt
from ramanujan_null_gauge_probe import evaluate


@dataclass(frozen=True)
class CommonDualDiagnostic:
    """One exact global-frame reconstruction certificate."""

    length: int
    primes: tuple[int, ...]
    column_count: int
    lower_certificate: int
    smallest_eigenvalue: float
    largest_eigenvalue: float
    reconstruction_error: float
    target_norm_squared: float
    coefficient_norm_squared: float
    dual_energy: float
    ratio_formula_error: float


def _validate(length: int, primes: tuple[int, ...]) -> None:
    if length < 1:
        raise ValueError("length must be positive")
    if len(primes) < 2 or len(set(primes)) != len(primes):
        raise ValueError("at least two distinct primes are required")
    for prime in primes:
        if prime < 2 or any(
            prime % divisor == 0 for divisor in range(2, math.isqrt(prime) + 1)
        ):
            raise ValueError("all bank entries must be prime")
    if min(p * r for p in primes for r in primes if p != r) <= length - 1:
        raise ValueError("every pair product must exceed interval differences")


def global_gram_formula(length: int, primes: tuple[int, ...]) -> np.ndarray:
    """Return the exact ordered-pair global Ramanujan Gramian."""

    _validate(length, primes)
    count = len(primes)
    difference = np.arange(length)[:, None] - np.arange(length)[None, :]
    diagonal_mass = sum(p * r for p in primes for r in primes if p != r)
    gram = diagonal_mass * np.eye(length)
    for prime in primes:
        gram -= (
            2 * (count - 1) * prime * (difference % prime == 0).astype(float)
        )
    gram += count * (count - 1) * np.ones((length, length))
    return gram


def global_frame_bounds(length: int, primes: tuple[int, ...]) -> tuple[int, int]:
    """Return the elementary lower and upper frame certificates."""

    _validate(length, primes)
    count = len(primes)
    diagonal_mass = sum(p * r for p in primes for r in primes if p != r)
    lower = diagonal_mass - 2 * (count - 1) * sum(
        prime * math.ceil(length / prime) for prime in primes
    )
    upper = diagonal_mass + count * (count - 1) * length
    return lower, upper


def explicit_global_frame(
    length: int,
    primes: tuple[int, ...],
    *,
    start: int = 1,
) -> np.ndarray:
    """Concatenate every ordered-pair primitive Fourier frame."""

    _validate(length, primes)
    return np.concatenate(
        [
            primitive_frame_matrix(length, p, r, start=start)
            for p in primes
            for r in primes
            if p != r
        ],
        axis=1,
    )


def prime_centered_target(length: int, *, start: int = 1) -> np.ndarray:
    """Return ``Lambda(n)-1`` on the requested integer interval."""

    return np.asarray(
        [
            evaluate(expected_von_mangoldt(n)) - 1.0
            for n in range(start, start + length)
        ],
        dtype=float,
    )


def analyze_common_dual(
    length: int,
    primes: tuple[int, ...],
    *,
    start: int = 1,
) -> CommonDualDiagnostic:
    """Construct and verify the canonical common-dual expansion."""

    frame = explicit_global_frame(length, primes, start=start)
    gram = global_gram_formula(length, primes)
    target = prime_centered_target(length, start=start)
    dual = np.linalg.solve(gram, target)
    coefficients = frame.conj().T @ dual
    reconstruction = frame @ coefficients
    eigenvalues = np.linalg.eigvalsh(gram)
    lower, _ = global_frame_bounds(length, primes)

    points = np.arange(start, start + length, dtype=float)
    offset = 0
    ratio_error = 0.0
    for p in primes:
        for r in primes:
            if p == r:
                continue
            block_width = (p - 1) * (r - 1)
            residues = np.asarray(
                [theta for theta in range(1, p * r) if math.gcd(theta, p * r) == 1],
                dtype=float,
            )
            expected = np.exp(
                -2j * math.pi * residues[:, None] * points[None, :] / (p * r)
            ) @ dual
            ratio_error = max(
                ratio_error,
                float(
                    np.max(
                        np.abs(coefficients[offset : offset + block_width] - expected)
                    )
                ),
            )
            offset += block_width

    return CommonDualDiagnostic(
        length=length,
        primes=primes,
        column_count=frame.shape[1],
        lower_certificate=lower,
        smallest_eigenvalue=float(eigenvalues[0]),
        largest_eigenvalue=float(eigenvalues[-1]),
        reconstruction_error=float(np.max(np.abs(reconstruction - target))),
        target_norm_squared=float(np.dot(target, target)),
        coefficient_norm_squared=float(np.vdot(coefficients, coefficients).real),
        dual_energy=float(np.dot(target, dual)),
        ratio_formula_error=ratio_error,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--length", type=int, default=16)
    parser.add_argument("--primes", type=int, nargs="+", default=(11, 13, 17))
    args = parser.parse_args()
    result = analyze_common_dual(args.length, tuple(args.primes))
    print(f"column_count={result.column_count}")
    print(f"lower_certificate={result.lower_certificate}")
    print(f"smallest_eigenvalue={result.smallest_eigenvalue:.12g}")
    print(f"largest_eigenvalue={result.largest_eigenvalue:.12g}")
    print(f"reconstruction_error={result.reconstruction_error:.12g}")
    print(f"coefficient_norm_squared={result.coefficient_norm_squared:.12g}")


if __name__ == "__main__":
    main()
