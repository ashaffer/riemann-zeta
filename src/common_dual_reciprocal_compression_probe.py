#!/usr/bin/env python3
"""Exact finite probe for the common-dual reciprocal-phase compression.

Let ``A`` concatenate the ordered-pair primitive frames

    A[n,(p,r,theta)] = e(theta*n/(p*r)),  p != r,

and put ``S=A A*``.  The canonical coefficients of a target ``v`` are
``gamma=A* S^(-1) v``.  For an integer shift ``j`` the reciprocal rotation is

    R_j[p,r,theta] = e(-j*theta*inverse(p mod r)/r).

If ``theta=a*r-b*p`` modulo ``p*r``, then this rotation is ``e(j*b/r)``.
Consequently it is the factor which changes the slow beat into the native
complex phase, with no cosine replacement.

The isometry ``U=A* S^(-1/2)`` compresses the rotation to

    C_j = U* R_j U.

This module checks that compression and the exact shifted-Ramanujan kernel.
It also keeps apart two quantities which must not be conflated:

* the canonical phase slice ``A(R_j-I)gamma``;
* the full native residual ``A R_j d-v``, where
  ``d[p,r,theta]=(log(p)/p)(log(r)/r)``.

In the whitened ``S^(-1)`` geometry their exact decomposition is

    S^(-1/2)(A R_j d-v)
      = U* R_j(d-gamma) + (C_j-I)S^(-1/2)v.

The calculations are finite algebraic diagnostics.  They are not an
asymptotic estimate or evidence for a zero-free region.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np

from common_dual_prime_beat_probe import (
    explicit_global_frame,
    global_gram_formula,
    prime_centered_target,
)
from farey_beat_frame_probe import crt_beat, primitive_residues


@dataclass(frozen=True)
class ReciprocalCompressionDiagnostic:
    """One exact common-dual/native reciprocal compression audit."""

    length: int
    primes: tuple[int, ...]
    start: int
    shift: int
    column_count: int
    isometry_error: float
    shifted_kernel_error: float
    native_shifted_formula_error: float
    compression_formula_error: float
    reciprocal_orientation_error: float
    reconstruction_error: float
    compression_operator_norm: float
    compression_smallest_singular_value: float
    compression_defect_operator_norm: float
    compression_defect_smallest_singular_value: float
    canonical_euclidean_defect_ratio: float
    canonical_whitened_defect_ratio: float
    coefficient_phase_defect: float
    coefficient_phase_identity_error: float
    compression_dissipation_identity_error: float
    schur_leakage_identity_error: float
    adversarial_largest_whitened_ratio: float
    adversarial_smallest_whitened_ratio: float
    native_euclidean_residual_ratio: float
    native_whitened_residual_ratio: float
    native_synthesis_whitened_ratio: float
    native_target_whitened_correlation: float
    native_contact_triangle_ratio: float
    mismatch_whitened_ratio: float
    canonical_term_whitened_ratio: float
    signed_triangle_ratio: float
    mismatch_canonical_correlation: float
    full_decomposition_error: float


def ordered_column_metadata(
    primes: tuple[int, ...],
) -> tuple[tuple[int, int, int], ...]:
    """Return metadata in exactly the column order used by the global frame."""

    return tuple(
        (p, r, theta)
        for p in primes
        for r in primes
        if p != r
        for theta in primitive_residues(p * r)
    )


def reciprocal_rotation(
    primes: tuple[int, ...], shift: int
) -> np.ndarray:
    """Return the diagonal of ``R_j`` in global-frame column order."""

    return np.asarray(
        [
            np.exp(-2j * math.pi * shift * theta * pow(p, -1, r) / r)
            for p, r, theta in ordered_column_metadata(primes)
        ],
        dtype=complex,
    )


def native_rank_one_coefficients(primes: tuple[int, ...]) -> np.ndarray:
    """Return ``d[p,r,theta]=(log p/p)(log r/r)`` in column order."""

    weights = {prime: math.log(prime) / prime for prime in primes}
    return np.asarray(
        [weights[p] * weights[r] for p, r, _ in ordered_column_metadata(primes)],
        dtype=complex,
    )


def complete_shift_period(primes: tuple[int, ...]) -> int:
    """Return a common period for every reciprocal rotation in the bank."""

    if len(primes) == 0:
        raise ValueError("at least one prime is required")
    return math.lcm(*primes)


def native_prime_point_ceiling(primes: tuple[int, ...]) -> float:
    """Return the uniform native synthesis ceiling at prime target points.

    Put ``h_p=log(p)/p``.  If ``n`` is prime and exceeds every bank prime,
    then ``c_p(n)=-1`` and, for every shift ``j``,

    ``sum_(p!=r) h_p h_r c_p(n)c_r(n-j)
       <= (sum_p h_p)^2-sum_p h_p^2``.

    Divisibilities ``r | n-j`` only decrease the left side.  This elementary
    one-sided obstruction is useful because ``Lambda(n)-1`` is of order
    ``log n`` at the same points.
    """

    if len(primes) < 2:
        raise ValueError("at least two primes are required")
    weights = np.asarray([math.log(prime) / prime for prime in primes])
    return float(np.sum(weights) ** 2 - np.dot(weights, weights))


def _ramanujan_two_primes(value: np.ndarray, p: int, r: int) -> np.ndarray:
    """Evaluate ``c_(p*r)`` for two distinct primes entrywise."""

    return (
        p * (value % p == 0).astype(float) - 1.0
    ) * (
        r * (value % r == 0).astype(float) - 1.0
    )


def _ramanujan_prime(value: np.ndarray, prime: int) -> np.ndarray:
    """Evaluate ``c_prime`` entrywise."""

    return prime * (value % prime == 0).astype(float) - 1.0


def shifted_ramanujan_kernel(
    length: int,
    primes: tuple[int, ...],
    shift: int,
    *,
    start: int = 1,
) -> np.ndarray:
    """Return the exact kernel ``A R_j A*`` by Ramanujan sums.

    The translation ``p*inverse(p mod r)`` is zero modulo ``p`` and one
    modulo ``r``.  The ``start`` argument is retained to mirror the explicit
    frame API; only point differences occur in the kernel.
    """

    if length < 1:
        raise ValueError("length must be positive")
    points = np.arange(start, start + length, dtype=np.int64)
    difference = points[:, None] - points[None, :]
    kernel = np.zeros((length, length), dtype=float)
    for p in primes:
        for r in primes:
            if p == r:
                continue
            translation = shift * p * pow(p, -1, r)
            kernel += _ramanujan_two_primes(
                difference - translation, p, r
            )
    return kernel


def native_shifted_type2_vector(
    length: int,
    primes: tuple[int, ...],
    shift: int,
    *,
    start: int = 1,
) -> np.ndarray:
    """Return the exact native synthesis ``A R_j d`` in physical space.

    Since ``p*inverse(p mod r)`` is zero modulo ``p`` and one modulo ``r``,

    ``c_(p*r)(n-j*p*inverse(p mod r)) = c_p(n)c_r(n-j)``.

    Thus this is exactly the ordered, unequal-prime square-root Type-II
    product with ``h_p=log(p)/p``.
    """

    if length < 1:
        raise ValueError("length must be positive")
    points = np.arange(start, start + length, dtype=np.int64)
    weights = {prime: math.log(prime) / prime for prime in primes}
    values = {
        prime: _ramanujan_prime(points, prime) for prime in primes
    }
    shifted_values = {
        prime: _ramanujan_prime(points - shift, prime) for prime in primes
    }
    answer = np.zeros(length, dtype=float)
    for p in primes:
        for r in primes:
            if p != r:
                answer += (
                    weights[p]
                    * weights[r]
                    * values[p]
                    * shifted_values[r]
                )
    return answer


def _inverse_square_root(matrix: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    if eigenvalues[0] <= 0.0:
        raise np.linalg.LinAlgError("the global frame operator is not positive")
    return (eigenvectors / np.sqrt(eigenvalues)) @ eigenvectors.conj().T


def _safe_ratio(numerator: float, denominator: float) -> float:
    if denominator == 0.0:
        return 0.0 if numerator == 0.0 else math.inf
    return numerator / denominator


def analyze_reciprocal_compression(
    length: int,
    primes: tuple[int, ...],
    *,
    start: int = 1,
    shift: int = 1,
    target: np.ndarray | None = None,
) -> ReciprocalCompressionDiagnostic:
    """Construct and audit the exact canonical and full native residuals."""

    frame = explicit_global_frame(length, primes, start=start)
    gram = global_gram_formula(length, primes)
    if target is None:
        vector = prime_centered_target(length, start=start).astype(complex)
    else:
        vector = np.asarray(target, dtype=complex)
        if vector.shape != (length,):
            raise ValueError("target must have shape (length,)")
        if not np.all(np.isfinite(vector)):
            raise ValueError("target must be finite")

    rotation = reciprocal_rotation(primes, shift)
    if len(rotation) != frame.shape[1]:
        raise RuntimeError("column metadata does not match the explicit frame")

    inverse_sqrt = _inverse_square_root(gram)
    isometry = frame.conj().T @ inverse_sqrt
    identity = np.eye(length)
    isometry_error = float(
        np.max(np.abs(isometry.conj().T @ isometry - identity))
    )

    direct_kernel = (frame * rotation[np.newaxis, :]) @ frame.conj().T
    formula_kernel = shifted_ramanujan_kernel(
        length, primes, shift, start=start
    )
    shifted_kernel_error = float(np.max(np.abs(direct_kernel - formula_kernel)))

    compression = isometry.conj().T @ (rotation[:, None] * isometry)
    compressed_formula = inverse_sqrt @ formula_kernel @ inverse_sqrt
    compression_formula_error = float(
        np.max(np.abs(compression - compressed_formula))
    )

    orientation_error = 0.0
    for (p, r, theta), phase in zip(
        ordered_column_metadata(primes), rotation
    ):
        _, numerator_r = crt_beat(theta, p, r)
        expected = np.exp(2j * math.pi * shift * numerator_r / r)
        orientation_error = max(orientation_error, float(abs(phase - expected)))

    gram_inverse_vector = np.linalg.solve(gram, vector)
    gamma = frame.conj().T @ gram_inverse_vector
    reconstruction = frame @ gamma
    reconstruction_error = float(np.max(np.abs(reconstruction - vector)))

    canonical_defect = frame @ ((rotation - 1.0) * gamma)
    vector_norm = float(np.linalg.norm(vector))
    canonical_euclidean_ratio = _safe_ratio(
        float(np.linalg.norm(canonical_defect)), vector_norm
    )

    whitened_vector = inverse_sqrt @ vector
    canonical_whitened = (compression - identity) @ whitened_vector
    whitened_vector_norm = float(np.linalg.norm(whitened_vector))
    canonical_whitened_ratio = _safe_ratio(
        float(np.linalg.norm(canonical_whitened)), whitened_vector_norm
    )

    gamma_norm_squared = float(np.vdot(gamma, gamma).real)
    rotated_coefficient_defect = (rotation - 1.0) * gamma
    coefficient_phase_defect = _safe_ratio(
        float(np.vdot(rotated_coefficient_defect, rotated_coefficient_defect).real),
        2.0 * gamma_norm_squared,
    )
    phase_inner = np.vdot(gamma, rotation * gamma)
    phase_identity = (
        0.0
        if gamma_norm_squared == 0.0
        else 1.0 - phase_inner.real / gamma_norm_squared
    )
    coefficient_phase_identity_error = float(
        abs(coefficient_phase_defect - phase_identity)
    )
    compression_pairing = np.vdot(
        whitened_vector,
        (compression - identity) @ whitened_vector,
    ).real
    compression_dissipation_identity_error = float(
        abs(
            compression_pairing
            + 0.5
            * np.vdot(
                rotated_coefficient_defect,
                rotated_coefficient_defect,
            ).real
        )
    )
    # ``I-C* C=U*R*(I-UU*)R U``.  Form the scalar version on the
    # canonical target without materializing the coefficient-space
    # projection ``UU*``.
    rotated_gamma = rotation * gamma
    projected_rotated_gamma = isometry.conj().T @ rotated_gamma
    null_leakage_norm_squared = (
        np.vdot(rotated_gamma, rotated_gamma).real
        - np.vdot(
            projected_rotated_gamma,
            projected_rotated_gamma,
        ).real
    )
    schur_leakage_identity_error = float(
        abs(
            np.vdot(rotated_coefficient_defect, rotated_coefficient_defect).real
            - null_leakage_norm_squared
            - np.vdot(canonical_whitened, canonical_whitened).real
        )
    )

    compression_singular = np.linalg.svd(compression, compute_uv=False)
    defect_operator = compression - identity
    defect_singular = np.linalg.svd(defect_operator, compute_uv=False)

    native = native_rank_one_coefficients(primes)
    direct_native_synthesis = frame @ (rotation * native)
    shifted_native_synthesis = native_shifted_type2_vector(
        length, primes, shift, start=start
    )
    native_shifted_formula_error = float(
        np.max(np.abs(direct_native_synthesis - shifted_native_synthesis))
    )
    full_residual = direct_native_synthesis - vector
    native_euclidean_ratio = _safe_ratio(
        float(np.linalg.norm(full_residual)), vector_norm
    )
    full_whitened = inverse_sqrt @ full_residual
    native_whitened_ratio = _safe_ratio(
        float(np.linalg.norm(full_whitened)), whitened_vector_norm
    )
    native_synthesis_whitened = inverse_sqrt @ direct_native_synthesis
    native_synthesis_norm = float(np.linalg.norm(native_synthesis_whitened))
    native_synthesis_ratio = _safe_ratio(
        native_synthesis_norm, whitened_vector_norm
    )
    native_target_correlation = _safe_ratio(
        float(np.vdot(native_synthesis_whitened, whitened_vector).real),
        native_synthesis_norm * whitened_vector_norm,
    )
    native_contact_triangle_ratio = _safe_ratio(
        float(np.linalg.norm(full_whitened)),
        native_synthesis_norm + whitened_vector_norm,
    )

    mismatch_whitened = isometry.conj().T @ (rotation * (native - gamma))
    canonical_term = canonical_whitened
    mismatch_norm = float(np.linalg.norm(mismatch_whitened))
    canonical_term_norm = float(np.linalg.norm(canonical_term))
    full_norm = float(np.linalg.norm(full_whitened))
    mismatch_ratio = _safe_ratio(mismatch_norm, whitened_vector_norm)
    canonical_term_ratio = _safe_ratio(
        canonical_term_norm, whitened_vector_norm
    )
    signed_triangle_ratio = _safe_ratio(
        full_norm, mismatch_norm + canonical_term_norm
    )
    mismatch_canonical_correlation = _safe_ratio(
        float(np.vdot(mismatch_whitened, canonical_term).real),
        mismatch_norm * canonical_term_norm,
    )
    full_decomposition_error = float(
        np.max(np.abs(full_whitened - mismatch_whitened - canonical_term))
    )

    return ReciprocalCompressionDiagnostic(
        length=length,
        primes=primes,
        start=start,
        shift=shift,
        column_count=frame.shape[1],
        isometry_error=isometry_error,
        shifted_kernel_error=shifted_kernel_error,
        native_shifted_formula_error=native_shifted_formula_error,
        compression_formula_error=compression_formula_error,
        reciprocal_orientation_error=orientation_error,
        reconstruction_error=reconstruction_error,
        compression_operator_norm=float(compression_singular[0]),
        compression_smallest_singular_value=float(compression_singular[-1]),
        compression_defect_operator_norm=float(defect_singular[0]),
        compression_defect_smallest_singular_value=float(defect_singular[-1]),
        canonical_euclidean_defect_ratio=canonical_euclidean_ratio,
        canonical_whitened_defect_ratio=canonical_whitened_ratio,
        coefficient_phase_defect=coefficient_phase_defect,
        coefficient_phase_identity_error=coefficient_phase_identity_error,
        compression_dissipation_identity_error=(
            compression_dissipation_identity_error
        ),
        schur_leakage_identity_error=schur_leakage_identity_error,
        adversarial_largest_whitened_ratio=float(defect_singular[0]),
        adversarial_smallest_whitened_ratio=float(defect_singular[-1]),
        native_euclidean_residual_ratio=native_euclidean_ratio,
        native_whitened_residual_ratio=native_whitened_ratio,
        native_synthesis_whitened_ratio=native_synthesis_ratio,
        native_target_whitened_correlation=native_target_correlation,
        native_contact_triangle_ratio=native_contact_triangle_ratio,
        mismatch_whitened_ratio=mismatch_ratio,
        canonical_term_whitened_ratio=canonical_term_ratio,
        signed_triangle_ratio=signed_triangle_ratio,
        mismatch_canonical_correlation=mismatch_canonical_correlation,
        full_decomposition_error=full_decomposition_error,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--length", type=int, default=16)
    parser.add_argument("--primes", type=int, nargs="+", default=(7, 11, 13))
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--shift", type=int, default=1)
    args = parser.parse_args()
    result = analyze_reciprocal_compression(
        args.length,
        tuple(args.primes),
        start=args.start,
        shift=args.shift,
    )
    for field_name in result.__dataclass_fields__:
        print(f"{field_name}={getattr(result, field_name)}")


if __name__ == "__main__":
    main()
