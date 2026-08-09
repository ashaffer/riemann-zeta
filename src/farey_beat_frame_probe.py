#!/usr/bin/env python3
"""Finite checks for the R83 primitive Farey-beat frame.

For two distinct primes ``p,r`` with ``pr > H``, the primitive exponentials
``e(theta*n/(pr))`` form a stable frame on any interval of ``H`` integers
when ``p,r`` are chosen near ``2*sqrt(H)``.  CRT writes every such exponential
as the beat of denominator-``p`` and denominator-``r`` frequencies.

The frame reconstructs arbitrary vectors, so this probe certifies a change
of coordinates rather than a cancellation estimate or zero-free region.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass, field

import numpy as np

from finite_ramanujan_completion_probe import expected_von_mangoldt
from ramanujan_null_gauge_probe import evaluate


@dataclass(frozen=True)
class BeatFrameResult:
    """Numerical certificate for one finite primitive beat frame."""

    length: int
    prime_p: int
    prime_r: int
    modulus: int
    lower_certificate: int
    smallest_eigenvalue: float
    largest_eigenvalue: float
    reconstruction_error: float
    target_norm_squared: float
    coefficient_norm_squared: float
    coefficients: np.ndarray = field(repr=False, compare=False)


@dataclass(frozen=True)
class BeatTensorDiagnostic:
    """Schatten diagnostics for the canonical prime-derived beat matrix."""

    length: int
    matrix_rank: int
    frobenius_norm: float
    nuclear_norm: float
    nuclear_to_frobenius: float


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, math.isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def two_primes_near_twice_sqrt(length: int) -> tuple[int, int]:
    """Return the first two primes at least ``2*sqrt(length)``."""

    if length < 2:
        raise ValueError("length must be at least two")
    candidate = max(2, math.ceil(2.0 * math.sqrt(length)))
    answer: list[int] = []
    while len(answer) < 2:
        if _is_prime(candidate):
            answer.append(candidate)
        candidate += 1
    return answer[0], answer[1]


def primitive_residues(modulus: int) -> tuple[int, ...]:
    """Return the units modulo ``modulus`` in their standard range."""

    if modulus < 2:
        raise ValueError("modulus must be at least two")
    return tuple(
        residue
        for residue in range(1, modulus)
        if math.gcd(residue, modulus) == 1
    )


def crt_beat(theta: int, prime_p: int, prime_r: int) -> tuple[int, int]:
    """Return ``a,b`` with ``theta = a*r-b*p (mod p*r)``."""

    modulus = prime_p * prime_r
    if prime_p == prime_r or not _is_prime(prime_p) or not _is_prime(prime_r):
        raise ValueError("prime_p and prime_r must be distinct primes")
    if math.gcd(theta, modulus) != 1:
        raise ValueError("theta must be a unit modulo p*r")
    a = (theta * pow(prime_r, -1, prime_p)) % prime_p
    b = (-theta * pow(prime_p, -1, prime_r)) % prime_r
    return a, b


def primitive_frame_matrix(
    length: int,
    prime_p: int,
    prime_r: int,
    *,
    start: int = 1,
) -> np.ndarray:
    """Return ``A[n,theta]=e(theta*n/(p*r))`` on a finite interval."""

    if length < 1 or start < 0:
        raise ValueError("length must be positive and start nonnegative")
    modulus = prime_p * prime_r
    points = np.arange(start, start + length, dtype=float)
    residues = np.asarray(primitive_residues(modulus), dtype=float)
    return np.exp(2j * math.pi * points[:, None] * residues[None, :] / modulus)


def exact_gram_formula(length: int, prime_p: int, prime_r: int) -> np.ndarray:
    """Return the exact integer matrix ``c_(p*r)(n-m)`` on length ``H``."""

    if length < 1 or prime_p * prime_r <= length - 1:
        raise ValueError("require p*r larger than every nonzero interval difference")
    difference = np.arange(length)[:, None] - np.arange(length)[None, :]
    return (
        prime_p * prime_r * (difference == 0)
        - prime_p * (difference % prime_p == 0)
        - prime_r * (difference % prime_r == 0)
        + 1
    ).astype(float)


def lower_frame_certificate(length: int, prime_p: int, prime_r: int) -> int:
    """Return the elementary lower frame bound ``kappa``."""

    return (
        prime_p * prime_r
        - prime_p * math.ceil(length / prime_p)
        - prime_r * math.ceil(length / prime_r)
    )


def prime_centered_target(length: int) -> np.ndarray:
    """Return ``Lambda(n)-1`` for ``1 <= n <= length``."""

    return np.asarray(
        [evaluate(expected_von_mangoldt(n)) - 1.0 for n in range(1, length + 1)],
        dtype=float,
    )


def analyze_frame(length: int) -> BeatFrameResult:
    """Build the canonical minimum-norm expansion of ``Lambda-1``."""

    prime_p, prime_r = two_primes_near_twice_sqrt(length)
    modulus = prime_p * prime_r
    frame = primitive_frame_matrix(length, prime_p, prime_r)
    gram = exact_gram_formula(length, prime_p, prime_r)
    target = prime_centered_target(length)
    dual = np.linalg.solve(gram, target)
    coefficients = frame.conj().T @ dual
    reconstruction = frame @ coefficients
    eigenvalues = np.linalg.eigvalsh(gram)
    return BeatFrameResult(
        length=length,
        prime_p=prime_p,
        prime_r=prime_r,
        modulus=modulus,
        lower_certificate=lower_frame_certificate(length, prime_p, prime_r),
        smallest_eigenvalue=float(eigenvalues[0]),
        largest_eigenvalue=float(eigenvalues[-1]),
        reconstruction_error=float(np.max(np.abs(reconstruction - target))),
        target_norm_squared=float(np.dot(target, target)),
        coefficient_norm_squared=float(np.vdot(coefficients, coefficients).real),
        coefficients=coefficients,
    )


def coefficient_matrix(result: BeatFrameResult) -> np.ndarray:
    """Reshape the canonical unit-indexed coefficients into CRT beat indices."""

    matrix = np.zeros((result.prime_p - 1, result.prime_r - 1), dtype=complex)
    for coefficient, theta in zip(
        result.coefficients,
        primitive_residues(result.modulus),
        strict=True,
    ):
        a, b = crt_beat(theta, result.prime_p, result.prime_r)
        matrix[a - 1, b - 1] = coefficient
    return matrix


def tensor_diagnostic(length: int) -> BeatTensorDiagnostic:
    """Return nuclear-versus-Frobenius data for the actual ``Lambda-1`` frame."""

    result = analyze_frame(length)
    singular_values = np.linalg.svd(coefficient_matrix(result), compute_uv=False)
    frobenius = float(np.linalg.norm(singular_values))
    nuclear = float(np.sum(singular_values))
    tolerance = singular_values[0] * 1.0e-10
    rank = int(np.count_nonzero(singular_values > tolerance))
    return BeatTensorDiagnostic(
        length=length,
        matrix_rank=rank,
        frobenius_norm=frobenius,
        nuclear_norm=nuclear,
        nuclear_to_frobenius=nuclear / frobenius,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--length", type=int, default=32)
    args = parser.parse_args()
    result = analyze_frame(args.length)
    tensor = tensor_diagnostic(args.length)
    print(f"p={result.prime_p}")
    print(f"r={result.prime_r}")
    print(f"modulus={result.modulus}")
    print(f"lower_certificate={result.lower_certificate}")
    print(f"smallest_eigenvalue={result.smallest_eigenvalue:.12g}")
    print(f"largest_eigenvalue={result.largest_eigenvalue:.12g}")
    print(f"reconstruction_error={result.reconstruction_error:.3g}")
    print(f"coefficient_norm_squared={result.coefficient_norm_squared:.12g}")
    print(f"beat_matrix_rank={tensor.matrix_rank}")
    print(f"nuclear_to_frobenius={tensor.nuclear_to_frobenius:.12g}")


if __name__ == "__main__":
    main()
