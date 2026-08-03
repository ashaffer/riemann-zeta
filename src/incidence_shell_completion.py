"""Nested-support block completion diagnostic for the relative Weil form.

At two successive supports ``L0 < L1`` this script uses a genuinely nested
hat space: old hats live in ``[-L0/4,L0/4]`` and independent hats live in the
two new collars.  It imposes the two Weil moment conditions and decomposes the
new relative space orthogonally as

    embedded old relative space  +  moment-corrected collar.

Prime autocorrelations are integrated exactly (piecewise quadratic Gauss
quadrature), so a newly activated prime shell restricts to exactly its scalar
degree on the embedded old space.  Only the archimedean matrix uses a finite
Fourier cutoff.

Two related completion tests are reported.

1. For the propagated old Weil ground vector, eliminate the collar by the
   exact Schur correction.  The remaining defect is positive exactly when
   that old line can be completed without producing a negative vector.
2. Propagate the canonical old contractive dual-frame column through the
   shell isometry.  If the old/collar edge blocks are

       B_old = (A, sqrt(Delta) V),   B_collar = (F, G),

   put ``P=F* C``, ``Q=G* V``, ``r=sqrt(Delta/D_old)`` and
   ``alpha=sqrt(D_old/D_new)``.  The unsatisfied cross-dual equation is

       Y = alpha (P + r Q),

   while the complementary shell-return map is ``T=Q-rP``.  The script tests
   the necessary right-inverse floor ``T T* >= D_new I`` for this ansatz and
   compares the least solution of ``T Z=Y`` with the propagated contraction
   slack.

   It also tests two larger but still non-exhaustive collar channels.  The
   fresh shell innovation is

       R_fresh = G*G - Q Q*,

   and the natural return-plus-fresh capacity is

       T (I+r^2 C*C)^-1 T* + R_fresh.

   Failure of the first floor rejects the shell-return ansatz itself.  Failure
   of the fresh or combined floors rejects those sufficient collar-only cycle
   families, but not arbitrary cycles in the full kernel of the old edge map.

   Finally the script adds the old-edge innovation

       R_old = F*F - F*A (A*A)^-1 A*F.

   The three orthogonal capacities ``R_old``, ``R_fresh``, and the coupled
   return capacity sum to the full incidence Schur complement.  More
   importantly, ``R_old+R_fresh`` is a proper structured subspace.  The script
   forms its actual dual frame: correct the old residual by ``-Z R^-1 Y`` and
   use ``sqrt(D_new) Z R^-1`` as the collar right inverse.  Its reported
   contraction slack is a genuine sufficient finite-dimensional test, not
   merely a capacity floor.

   For a canonical old column it also evaluates the amplified threshold

       H = D_new [I + L* S0 (S0-D_new I)^-1 L],
       L = S0^-1 B_U* B_W.

   The full-kernel comparison against ``H`` is exactly the Weil Schur
   condition.  Comparisons for old-only, shell-only, return-only, and their
   proper sums are noncircular sufficient tests of those structured cycle
   subspaces.

None of these tests proves positivity on the new collar.  The final
``canonical_margin`` is included as an algebraic control: it is

    lambda_min(Q) / (D + lambda_min(Q)),

the contraction margin of the full canonical dual frame, and hence is exactly
equivalent to positivity of the same finite Weil matrix.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import mpmath as mp
import numpy as np
from scipy.linalg import eigvalsh as generalized_eigvalsh
from scipy.linalg import eigh as generalized_eigh
from scipy.linalg import null_space

from incidence_poincare_ratio import degree_deficit
from weil_core import PRIME_POWERS, cdig


@dataclass(frozen=True)
class CompletionDiagnostic:
    old_support: float
    new_support: float
    old_relative_dimension: int
    collar_relative_dimension: int
    shell_isometry_error: float
    old_gap: float
    collar_gap: float
    full_gap: float
    full_ground_old_mass: float
    primal_cross_ratio: float
    primal_defect: float
    completed_rayleigh: float
    full_schur_minimum: float
    propagated_slack: float
    cross_dual_residual: float
    return_cancellation_factor: float
    return_rank: int
    return_stable_rank: float
    return_map_rank: int
    return_floor_ratio: float
    return_solve_residual: float
    return_correction_norm: float
    return_correction_slack_ratio: float
    fresh_shell_rank: int
    fresh_shell_floor_ratio: float
    old_fresh_rank: int
    old_fresh_floor_ratio: float
    two_fresh_floor_ratio: float
    two_fresh_completion_slack: float
    old_fresh_return_floor_ratio: float
    combined_cycle_rank: int
    combined_cycle_floor_ratio: float
    full_kernel_rank: int
    full_kernel_floor_ratio: float
    full_kernel_completion_slack: float
    full_kernel_to_canonical_ratio: float
    full_kernel_schur_error: float
    amplified_return_ratio: float
    amplified_shell_ratio: float
    amplified_old_ratio: float
    amplified_return_shell_ratio: float
    amplified_old_return_ratio: float
    amplified_old_shell_ratio: float
    amplified_old_shell_second_ratio: float
    amplified_old_shell_worst_parity: float
    amplified_old_shell_second_parity: float
    amplified_old_shell_negative_count: int
    amplified_old_shell_negative_even_count: int
    amplified_old_shell_negative_odd_count: int
    amplified_old_shell_near_count: int
    return_on_worst_mode: float
    return_to_worst_deficit: float
    return_cross_negative: float
    amplified_full_ratio: float
    amplified_old_shell_excess_to_canonical: float
    minimal_correction: float
    corrected_slack: float
    propagated_kernel_cost: float
    fixed_column_extension_slack: float
    canonical_margin: float


def hat_group(left: float, right: float,
              degree: int) -> tuple[np.ndarray, np.ndarray]:
    half_width = (right - left) / (degree + 1)
    centers = np.linspace(left + half_width, right - half_width, degree)
    return centers, np.full(degree, half_width)


def block_gram(degrees: list[int], half_widths: list[float]) -> np.ndarray:
    """The exact L2 Gram matrix of disjoint equal-width hat groups."""
    total = sum(degrees)
    gram = np.zeros((total, total))
    offset = 0
    for degree, width in zip(degrees, half_widths):
        for i in range(degree):
            gram[offset + i, offset + i] = 2 * width / 3
            if i + 1 < degree:
                gram[offset + i, offset + i + 1] = width / 6
                gram[offset + i + 1, offset + i] = width / 6
        offset += degree
    return gram


def hat_value(x: float, center: float, half_width: float) -> float:
    return max(0.0, 1.0 - abs(x - center) / half_width)


def shifted_hat_overlap(center_i: float, width_i: float,
                        center_j: float, width_j: float,
                        shift: float) -> float:
    """Return integral b_i(x)b_j(x+shift) dx exactly to float precision."""
    breakpoints = sorted({
        center_i - width_i, center_i, center_i + width_i,
        center_j - shift - width_j, center_j - shift,
        center_j - shift + width_j,
    })
    node = 1 / math.sqrt(3)
    value = 0.0
    for left, right in zip(breakpoints[:-1], breakpoints[1:]):
        if right <= left:
            continue
        midpoint = (left + right) / 2
        radius = (right - left) / 2
        for sign in (-1, 1):
            x = midpoint + sign * radius * node
            value += radius * hat_value(x, center_i, width_i) * hat_value(
                x + shift, center_j, width_j)
    return value


def prime_matrix(centers: np.ndarray, widths: np.ndarray,
                 support: float) -> np.ndarray:
    """Exact positive autocorrelation matrix subtracted in the Weil form."""
    dimension = len(centers)
    matrix = np.zeros((dimension, dimension))
    for n, prime in PRIME_POWERS:
        shift = math.log(n)
        if 2 * shift >= support:
            continue
        translate = np.empty((dimension, dimension))
        for i in range(dimension):
            for j in range(dimension):
                translate[i, j] = shifted_hat_overlap(
                    centers[i], widths[i], centers[j], widths[j], shift)
        weight = 2 * math.log(prime) / math.sqrt(n)
        matrix += weight * (translate + translate.T) / 2
    return matrix


def archimedean_matrix(centers: np.ndarray, widths: np.ndarray,
                       gram: np.ndarray, cutoff: float,
                       intervals: int, chunk: int) -> np.ndarray:
    """Fourier-cutoff archimedean-minus-log(pi) matrix."""
    if intervals % 2:
        intervals += 1
    frequencies = np.linspace(1e-9, cutoff, intervals + 1)
    step = frequencies[1] - frequencies[0]
    weights = np.ones(intervals + 1)
    weights[1:-1:2] = 4
    weights[2:-1:2] = 2
    weights *= step / 3
    multiplier = cdig(0.25 + 0.5j * frequencies).real * weights

    matrix = np.zeros_like(gram)
    for start in range(0, len(frequencies), chunk):
        frequency = frequencies[start:start + chunk, None]
        scaled = frequency * widths[None, :] / 2
        sinc = np.where(np.abs(scaled) < 1e-12, 1.0,
                        np.sin(scaled) / scaled)
        transform = (widths[None, :] * sinc ** 2
                     * np.exp(-1j * frequency * centers[None, :]))
        local_weight = multiplier[start:start + chunk, None]
        matrix += np.real(transform.conj().T @ (local_weight * transform))
    return matrix / math.pi - math.log(math.pi) * gram


def pole_vectors(centers: np.ndarray,
                 widths: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    exponent = 0.5
    factor = ((2 * np.cosh(exponent * widths) - 2)
              / (exponent * exponent * widths))
    return (np.exp(exponent * centers) * factor,
            np.exp(-exponent * centers) * factor)


def relative_decomposition(gram: np.ndarray, plus: np.ndarray,
                           minus: np.ndarray,
                           old_degree: int) -> tuple[np.ndarray, int]:
    """Whiten L2, then return [old relative | corrected collar]."""
    whitening = np.linalg.inv(np.linalg.cholesky(gram).T)
    plus_orthonormal = whitening.T @ plus
    minus_orthonormal = whitening.T @ minus
    full_relative = null_space(np.vstack([
        plus_orthonormal, minus_orthonormal]))

    old_relative_local = null_space(np.vstack([
        plus_orthonormal[:old_degree],
        minus_orthonormal[:old_degree],
    ]))
    old_relative = np.zeros((len(plus), old_degree - 2))
    old_relative[:old_degree] = old_relative_local
    collar_coordinates = null_space(old_relative.T @ full_relative)
    corrected_collar = full_relative @ collar_coordinates
    decomposition = np.column_stack([old_relative, corrected_collar])
    return whitening @ decomposition, old_relative.shape[1]


def _least_eigenvalue(matrix: np.ndarray) -> float:
    return float(np.linalg.eigvalsh((matrix + matrix.T) / 2)[0])


def diagnose_pair(old_support: float, new_support: float,
                  old_degree: int, collar_degree: int,
                  cutoff: float, intervals: int,
                  chunk: int) -> CompletionDiagnostic:
    old_radius = old_support / 4
    new_radius = new_support / 4
    old_centers, old_widths = hat_group(
        -old_radius, old_radius, old_degree)
    left_centers, left_widths = hat_group(
        -new_radius, -old_radius, collar_degree)
    right_centers, right_widths = hat_group(
        old_radius, new_radius, collar_degree)
    centers = np.concatenate([old_centers, left_centers, right_centers])
    widths = np.concatenate([old_widths, left_widths, right_widths])
    dimension = len(centers)

    gram = block_gram(
        [old_degree, collar_degree, collar_degree],
        [old_widths[0], left_widths[0], right_widths[0]])
    plus, minus = pole_vectors(centers, widths)
    coordinates, old_relative_dimension = relative_decomposition(
        gram, plus, minus, old_degree)
    relative_dimension = dimension - 2
    collar_relative_dimension = relative_dimension - old_relative_dimension

    archimedean = archimedean_matrix(
        centers, widths, gram, cutoff, intervals, chunk)
    pole = np.outer(plus, minus) + np.outer(minus, plus)
    old_prime = prime_matrix(centers, widths, old_support)
    new_prime = prime_matrix(centers, widths, new_support)
    old_places_form = coordinates.T @ (
        archimedean + pole - old_prime) @ coordinates
    new_form = coordinates.T @ (
        archimedean + pole - new_prime) @ coordinates

    old_degree_scalar = float(degree_deficit(old_support))
    new_degree_scalar = float(degree_deficit(new_support))
    shell_degree = new_degree_scalar - old_degree_scalar
    identity = np.eye(relative_dimension)
    old_places_gradient = old_places_form + old_degree_scalar * identity
    shell_gradient = (new_form - old_places_form
                      + shell_degree * identity)
    full_gradient = new_form + new_degree_scalar * identity

    old_slice = slice(0, old_relative_dimension)
    collar_slice = slice(old_relative_dimension, relative_dimension)
    shell_old = shell_gradient[old_slice, old_slice]
    shell_isometry_error = float(np.linalg.norm(
        shell_old - shell_degree * np.eye(old_relative_dimension), ord=2))

    old_block = new_form[old_slice, old_slice]
    cross_block = new_form[old_slice, collar_slice]
    collar_block = new_form[collar_slice, collar_slice]
    old_values, old_vectors = np.linalg.eigh(old_block)
    old_ground = old_vectors[:, 0]
    old_gap = float(old_values[0])
    collar_gap = _least_eigenvalue(collar_block)
    full_values, full_vectors = np.linalg.eigh(new_form)
    full_gap = float(full_values[0])
    full_ground_old_mass = float(np.linalg.norm(
        full_vectors[:old_relative_dimension, 0]) ** 2)

    if collar_gap <= 0:
        primal_cross_ratio = math.inf
        primal_defect = -math.inf
        completed_rayleigh = -math.inf
        full_schur_minimum = -math.inf
    else:
        cross_residual = cross_block.T @ old_ground
        correction = np.linalg.solve(collar_block, cross_residual)
        cross_gain = float(cross_residual @ correction)
        primal_cross_ratio = cross_gain / old_gap
        primal_defect = old_gap - cross_gain
        completed_rayleigh = primal_defect / (1 + float(correction @ correction))
        schur = old_block - cross_block @ np.linalg.solve(
            collar_block, cross_block.T)
        full_schur_minimum = _least_eigenvalue(schur)

    # Propagated canonical old dual column.  All formulas below use only Gram
    # matrices, and are invariant under a unitary change of incidence edges.
    old_gradient = old_places_gradient[old_slice, old_slice]
    shell_old_gram = shell_gradient[old_slice, old_slice]
    propagated_gram = (
        old_degree_scalar ** 2 / new_degree_scalar
        * np.linalg.inv(old_gradient)
        + shell_old_gram / new_degree_scalar)
    propagated_slack = _least_eigenvalue(
        np.eye(old_relative_dimension) - propagated_gram)

    residual = (
        old_degree_scalar
        * old_places_gradient[collar_slice, old_slice]
        @ np.linalg.inv(old_gradient)
        + shell_gradient[collar_slice, old_slice]
    ) / math.sqrt(new_degree_scalar)
    cross_dual_residual = float(np.linalg.norm(residual, ord=2))

    # Exact shell-return gate.  Write the old-place and shell edge blocks as
    # (A,sqrt(shell_degree)V) on old states and (F,G) on collar states.
    # For the canonical old dual C, only the pairings
    # P=F*C and Q=G*V are needed; they are determined by the Gram blocks.
    # The propagated cross residual is alpha(P+rQ), while Q-rP is the
    # complementary return map which would have to repair it.
    old_cross = old_places_gradient[collar_slice, old_slice]
    shell_cross = shell_gradient[collar_slice, old_slice]
    edge_p = (math.sqrt(old_degree_scalar) * old_cross
              @ np.linalg.inv(old_gradient))
    edge_q = shell_cross / math.sqrt(shell_degree)
    shell_ratio = math.sqrt(shell_degree / old_degree_scalar)
    propagation_scale = math.sqrt(old_degree_scalar / new_degree_scalar)
    return_sum = edge_p + shell_ratio * edge_q
    return_map = edge_q - shell_ratio * edge_p
    return_cancellation_factor = float(
        np.linalg.norm(return_sum, ord=2)
        / (np.linalg.norm(edge_p, ord=2)
           + shell_ratio * np.linalg.norm(edge_q, ord=2)))
    sum_singular_values = np.linalg.svd(return_sum, compute_uv=False)
    sum_rank_tolerance = (max(return_sum.shape) * np.finfo(float).eps
                          * sum_singular_values[0])
    return_rank = int(np.sum(sum_singular_values > sum_rank_tolerance))
    return_stable_rank = float(
        np.sum(sum_singular_values ** 2) / sum_singular_values[0] ** 2)
    singular_values = np.linalg.svd(return_map, compute_uv=False)
    rank_tolerance = (max(return_map.shape) * np.finfo(float).eps
                      * singular_values[0])
    return_map_rank = int(np.sum(singular_values > rank_tolerance))
    return_floor = (
        float(singular_values[-1] ** 2)
        if return_map.shape[0] <= return_map.shape[1] else 0.0)
    return_floor_ratio = return_floor / new_degree_scalar
    return_y = propagation_scale * return_sum
    return_correction = np.linalg.pinv(
        return_map, rcond=max(return_map.shape) * np.finfo(float).eps
    ) @ return_y
    return_solve_residual = float(
        np.linalg.norm(return_map @ return_correction - return_y, ord=2)
        / max(np.linalg.norm(return_y, ord=2), np.finfo(float).tiny))
    return_correction_norm = float(np.linalg.norm(
        return_correction, ord=2))
    return_correction_slack_ratio = (
        return_correction_norm ** 2 / propagated_slack
        if propagated_slack > 0 else math.inf)

    # Orthogonal innovation left in the new shell after removing the part
    # already paired with the old-shell isometry V.  Positivity is automatic;
    # a fresh-shell-only sufficient construction would need this innovation
    # to dominate the new degree on the entire collar.
    fresh_shell = (shell_gradient[collar_slice, collar_slice]
                   - edge_q @ edge_q.T)
    fresh_shell = (fresh_shell + fresh_shell.T) / 2
    fresh_values = np.linalg.eigvalsh(fresh_shell)
    fresh_tolerance = (max(fresh_shell.shape) * np.finfo(float).eps
                       * max(1.0, abs(fresh_values[-1])))
    fresh_shell_rank = int(np.sum(fresh_values > fresh_tolerance))
    fresh_shell_floor_ratio = max(0.0, float(fresh_values[0])) / new_degree_scalar

    # The corresponding innovation already present in the old-place edge
    # space is the part of F orthogonal to range(A).  It is the Schur
    # complement of the old-place incidence Gram matrix.
    old_fresh = (
        old_places_gradient[collar_slice, collar_slice]
        - old_cross @ np.linalg.solve(old_gradient, old_cross.T))
    old_fresh = (old_fresh + old_fresh.T) / 2
    old_fresh_values = np.linalg.eigvalsh(old_fresh)
    old_fresh_tolerance = (
        max(old_fresh.shape) * np.finfo(float).eps
        * max(1.0, abs(old_fresh_values[-1])))
    old_fresh_rank = int(np.sum(old_fresh_values > old_fresh_tolerance))
    old_fresh_floor_ratio = max(
        0.0, float(old_fresh_values[0])) / new_degree_scalar

    old_dual_gram = old_degree_scalar * np.linalg.inv(old_gradient)
    cycle_metric = (np.eye(old_relative_dimension)
                    + shell_ratio ** 2 * old_dual_gram)
    return_capacity = return_map @ np.linalg.solve(
        cycle_metric, return_map.T)
    two_fresh = old_fresh + fresh_shell
    old_fresh_return = old_fresh + return_capacity
    combined_cycle = return_capacity + fresh_shell
    full_kernel_capacity = old_fresh + combined_cycle
    two_fresh_floor_ratio = max(
        0.0, _least_eigenvalue(two_fresh)) / new_degree_scalar
    old_fresh_return_floor_ratio = max(
        0.0, _least_eigenvalue(old_fresh_return)) / new_degree_scalar
    combined_cycle = (combined_cycle + combined_cycle.T) / 2
    combined_values = np.linalg.eigvalsh(combined_cycle)
    combined_tolerance = (max(combined_cycle.shape) * np.finfo(float).eps
                          * max(1.0, abs(combined_values[-1])))
    combined_cycle_rank = int(np.sum(combined_values > combined_tolerance))
    combined_cycle_floor_ratio = max(
        0.0, float(combined_values[0])) / new_degree_scalar

    full_kernel_values = np.linalg.eigvalsh(
        (full_kernel_capacity + full_kernel_capacity.T) / 2)
    full_kernel_tolerance = (
        max(full_kernel_capacity.shape) * np.finfo(float).eps
        * max(1.0, abs(full_kernel_values[-1])))
    full_kernel_rank = int(np.sum(
        full_kernel_values > full_kernel_tolerance))
    full_kernel_floor_ratio = max(
        0.0, float(full_kernel_values[0])) / new_degree_scalar

    def structured_completion_slack(capacity: np.ndarray) -> float:
        """Contraction slack for correction/right inverse using this cycle Gram."""
        inverse_residual = np.linalg.solve(capacity, residual)
        inverse_identity = np.linalg.inv(capacity)
        structured_gram = np.block([
            [propagated_gram + residual.T @ inverse_residual,
             -math.sqrt(new_degree_scalar)
             * residual.T @ inverse_identity],
            [-math.sqrt(new_degree_scalar)
             * inverse_identity @ residual,
             new_degree_scalar * inverse_identity],
        ])
        return _least_eigenvalue(
            np.eye(relative_dimension) - structured_gram)

    two_fresh_completion_slack = structured_completion_slack(two_fresh)

    # Orthogonal decomposition check: old-fresh + shell-fresh + coupled
    # return must equal the Gram of the projection of B_W into ker(B_U*),
    # i.e. the incidence Schur complement computed below.

    full_old = full_gradient[old_slice, old_slice]
    full_cross = full_gradient[old_slice, collar_slice]
    full_collar = full_gradient[collar_slice, collar_slice]
    incidence_schur = full_collar - full_cross.T @ np.linalg.solve(
        full_old, full_cross)
    full_kernel_schur_error = float(np.linalg.norm(
        full_kernel_capacity - incidence_schur, ord=2))

    # Exact amplified collar threshold.  The full-kernel inequality
    # G_full >= H is algebraically the Schur condition for the Weil matrix;
    # replacing G_full by a proper cycle subspace is a genuinely sufficient
    # structured criterion.
    old_weil_inverse = np.linalg.inv(old_block)
    leakage = np.linalg.solve(full_old, full_cross)
    amplified_threshold = new_degree_scalar * (
        np.eye(collar_relative_dimension)
        + leakage.T @ full_old @ old_weil_inverse @ leakage)

    def amplified_ratio(capacity: np.ndarray) -> float:
        return float(generalized_eigvalsh(
            (capacity + capacity.T) / 2,
            (amplified_threshold + amplified_threshold.T) / 2,
            subset_by_index=[0, 0])[0])

    amplified_return_ratio = amplified_ratio(return_capacity)
    amplified_shell_ratio = amplified_ratio(fresh_shell)
    amplified_old_ratio = amplified_ratio(old_fresh)
    amplified_return_shell_ratio = amplified_ratio(combined_cycle)
    amplified_old_return_ratio = amplified_ratio(old_fresh_return)
    amplified_old_shell_values, amplified_old_shell_vectors = generalized_eigh(
        (two_fresh + two_fresh.T) / 2,
        (amplified_threshold + amplified_threshold.T) / 2)
    amplified_old_shell_ratio = float(amplified_old_shell_values[0])
    amplified_old_shell_second_ratio = float(amplified_old_shell_values[1])
    reflection_indices = np.concatenate([
        np.arange(old_degree - 1, -1, -1),
        old_degree + collar_degree
        + np.arange(collar_degree - 1, -1, -1),
        old_degree + np.arange(collar_degree - 1, -1, -1),
    ])

    collar_coordinates = coordinates[:, collar_slice]
    collar_reflection = (
        collar_coordinates.T @ gram
        @ collar_coordinates[reflection_indices, :])
    reflected_modes = collar_reflection @ amplified_old_shell_vectors
    mode_norms = np.sum(amplified_old_shell_vectors ** 2, axis=0)
    amplified_old_shell_parities = np.sum(
        amplified_old_shell_vectors * reflected_modes, axis=0) / mode_norms
    amplified_old_shell_worst_parity = float(
        amplified_old_shell_parities[0])
    amplified_old_shell_second_parity = float(
        amplified_old_shell_parities[1])
    amplified_old_shell_negative_count = int(np.sum(
        amplified_old_shell_values < 1 - 1e-10))
    negative_parities = amplified_old_shell_parities[
        :amplified_old_shell_negative_count]
    amplified_old_shell_negative_even_count = int(np.sum(
        negative_parities > 0.5))
    amplified_old_shell_negative_odd_count = int(np.sum(
        negative_parities < -0.5))
    amplified_old_shell_near_count = int(np.sum(
        amplified_old_shell_values < 1.01))
    worst_mode = amplified_old_shell_vectors[:, 0]
    return_on_worst_mode = float(
        worst_mode @ return_capacity @ worst_mode)
    worst_deficit = max(0.0, 1 - amplified_old_shell_ratio)
    return_to_worst_deficit = (
        return_on_worst_mode / worst_deficit
        if worst_deficit > 0 else math.nan)
    if amplified_old_shell_negative_count:
        negative_vectors = amplified_old_shell_vectors[
            :, :amplified_old_shell_negative_count]
        positive_vectors = amplified_old_shell_vectors[
            :, amplified_old_shell_negative_count:]
        return_cross_negative = float(np.linalg.norm(
            negative_vectors.T @ return_capacity @ positive_vectors,
            ord=2))
    else:
        return_cross_negative = 0.0
    amplified_full_ratio = amplified_ratio(full_kernel_capacity)
    inverse_schur_residual = np.linalg.solve(incidence_schur, residual)
    correction_gram = residual.T @ inverse_schur_residual
    minimal_correction = math.sqrt(max(
        0.0, float(np.linalg.eigvalsh(correction_gram)[-1])))

    propagated_to_orthogonal_collar = (
        residual.T
        - math.sqrt(new_degree_scalar)
        * np.linalg.solve(full_old, full_cross))
    corrected_gram = (
        propagated_gram
        - propagated_to_orthogonal_collar @ inverse_schur_residual
        - residual.T @ np.linalg.solve(
            incidence_schur, propagated_to_orthogonal_collar.T)
        + correction_gram)
    corrected_slack = _least_eigenvalue(
        np.eye(old_relative_dimension) - corrected_gram)

    # For the full kernel, unlike the two fresh innovation spaces, the coupled
    # return channel is not orthogonal to the propagated column.  Retain those
    # cross terms explicitly.  This is the exact dual-frame completion which
    # preserves the propagated old column.
    incidence_schur_inverse = np.linalg.inv(incidence_schur)
    full_completion_cross = (
        math.sqrt(new_degree_scalar)
        * (propagated_to_orthogonal_collar - residual.T)
        @ incidence_schur_inverse)
    full_completion_gram = np.block([
        [corrected_gram, full_completion_cross],
        [full_completion_cross.T,
         new_degree_scalar * incidence_schur_inverse],
    ])
    full_kernel_completion_slack = _least_eigenvalue(
        np.eye(relative_dimension) - full_completion_gram)

    # Once the corrected old column satisfies the full dual equation, its
    # difference from the canonical solution lies in ker(B*).  This kernel
    # component is genuine extra contraction cost.  The optimal completion of
    # the remaining columns keeps their kernel components zero, so the matrix
    # below gives the best possible full contraction which preserves this
    # particular propagated/corrected old column.
    full_gradient_inverse = np.linalg.inv(full_gradient)
    canonical_old_gram = (
        new_degree_scalar
        * full_gradient_inverse[old_slice, old_slice])
    propagated_kernel_gram = (
        corrected_gram - canonical_old_gram)
    propagated_kernel_gram = (
        propagated_kernel_gram + propagated_kernel_gram.T) / 2
    propagated_kernel_cost = math.sqrt(max(
        0.0, float(np.linalg.eigvalsh(propagated_kernel_gram)[-1])))
    embedded_kernel_gram = np.zeros_like(full_gradient)
    embedded_kernel_gram[old_slice, old_slice] = propagated_kernel_gram
    fixed_column_extension_slack = _least_eigenvalue(
        np.eye(relative_dimension)
        - new_degree_scalar * full_gradient_inverse
        - embedded_kernel_gram)

    canonical_margin = full_gap / (new_degree_scalar + full_gap)
    full_kernel_to_canonical_ratio = (
        full_kernel_completion_slack / canonical_margin
        if canonical_margin != 0 else math.nan)
    amplified_old_shell_excess_to_canonical = (
        (amplified_old_shell_ratio - 1) / canonical_margin
        if canonical_margin != 0 else math.nan)
    return CompletionDiagnostic(
        old_support=old_support,
        new_support=new_support,
        old_relative_dimension=old_relative_dimension,
        collar_relative_dimension=collar_relative_dimension,
        shell_isometry_error=shell_isometry_error,
        old_gap=old_gap,
        collar_gap=collar_gap,
        full_gap=full_gap,
        full_ground_old_mass=full_ground_old_mass,
        primal_cross_ratio=primal_cross_ratio,
        primal_defect=primal_defect,
        completed_rayleigh=completed_rayleigh,
        full_schur_minimum=full_schur_minimum,
        propagated_slack=propagated_slack,
        cross_dual_residual=cross_dual_residual,
        return_cancellation_factor=return_cancellation_factor,
        return_rank=return_rank,
        return_stable_rank=return_stable_rank,
        return_map_rank=return_map_rank,
        return_floor_ratio=return_floor_ratio,
        return_solve_residual=return_solve_residual,
        return_correction_norm=return_correction_norm,
        return_correction_slack_ratio=return_correction_slack_ratio,
        fresh_shell_rank=fresh_shell_rank,
        fresh_shell_floor_ratio=fresh_shell_floor_ratio,
        old_fresh_rank=old_fresh_rank,
        old_fresh_floor_ratio=old_fresh_floor_ratio,
        two_fresh_floor_ratio=two_fresh_floor_ratio,
        two_fresh_completion_slack=two_fresh_completion_slack,
        old_fresh_return_floor_ratio=old_fresh_return_floor_ratio,
        combined_cycle_rank=combined_cycle_rank,
        combined_cycle_floor_ratio=combined_cycle_floor_ratio,
        full_kernel_rank=full_kernel_rank,
        full_kernel_floor_ratio=full_kernel_floor_ratio,
        full_kernel_completion_slack=full_kernel_completion_slack,
        full_kernel_to_canonical_ratio=full_kernel_to_canonical_ratio,
        full_kernel_schur_error=full_kernel_schur_error,
        amplified_return_ratio=amplified_return_ratio,
        amplified_shell_ratio=amplified_shell_ratio,
        amplified_old_ratio=amplified_old_ratio,
        amplified_return_shell_ratio=amplified_return_shell_ratio,
        amplified_old_return_ratio=amplified_old_return_ratio,
        amplified_old_shell_ratio=amplified_old_shell_ratio,
        amplified_old_shell_second_ratio=(
            amplified_old_shell_second_ratio),
        amplified_old_shell_worst_parity=(
            amplified_old_shell_worst_parity),
        amplified_old_shell_second_parity=(
            amplified_old_shell_second_parity),
        amplified_old_shell_negative_count=(
            amplified_old_shell_negative_count),
        amplified_old_shell_negative_even_count=(
            amplified_old_shell_negative_even_count),
        amplified_old_shell_negative_odd_count=(
            amplified_old_shell_negative_odd_count),
        amplified_old_shell_near_count=amplified_old_shell_near_count,
        return_on_worst_mode=return_on_worst_mode,
        return_to_worst_deficit=return_to_worst_deficit,
        return_cross_negative=return_cross_negative,
        amplified_full_ratio=amplified_full_ratio,
        amplified_old_shell_excess_to_canonical=(
            amplified_old_shell_excess_to_canonical),
        minimal_correction=minimal_correction,
        corrected_slack=corrected_slack,
        propagated_kernel_cost=propagated_kernel_cost,
        fixed_column_extension_slack=fixed_column_extension_slack,
        canonical_margin=canonical_margin,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[1.75, 2.485, 2.996, 3.555, 4.04])
    parser.add_argument("--old-degree", type=int, default=31)
    parser.add_argument("--collar-degree", type=int, default=10)
    parser.add_argument("--arch-cutoff", type=float, default=1200.0)
    parser.add_argument("--arch-intervals", type=int, default=120000)
    parser.add_argument("--chunk", type=int, default=2000)
    args = parser.parse_args()
    mp.mp.dps = 30

    fields = list(CompletionDiagnostic.__dataclass_fields__)
    print(",".join(fields))
    for old_support, new_support in zip(args.supports[:-1], args.supports[1:]):
        result = diagnose_pair(
            old_support, new_support, args.old_degree,
            args.collar_degree, args.arch_cutoff,
            args.arch_intervals, args.chunk)
        values = []
        for field in fields:
            value = getattr(result, field)
            if isinstance(value, int):
                values.append(str(value))
            else:
                values.append(f"{value:.12e}")
        print(",".join(values), flush=True)


if __name__ == "__main__":
    main()
