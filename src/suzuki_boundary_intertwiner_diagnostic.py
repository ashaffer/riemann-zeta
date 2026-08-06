"""Finite necessary tests for a Suzuki boundary-space intertwiner.

Let ``T_s = A - s I`` be a positive Galerkin metric and let

    d_s(z) = T_s^{-1} P exp(-i z x)

be the projected deficiency vector.  If a unitary map between two energy
spaces intertwines the adjoint derivatives and preserves the spectral
parameter, it must send every line ``C d_a(z)`` to ``C d_b(z)``.  Hence the
normalized Gram kernels of any finite collection of these lines agree up to
a diagonal phase gauge:

    C_b(i,j) = conjugate(q_i) q_j C_a(i,j),    |q_i| = 1.

The magnitudes of the entries and the phases of all Bargmann triples are
therefore invariants.  This module measures those invariants, tunes the one
available target shift on a training set, and evaluates the result on held-out
spectral parameters.  It can also fit a real affine reparameterization
``z_target = alpha*z_reference + beta`` by bounded deterministic grids.  The
affine positive control is the exact spectral scaling induced by interval
dilation.  Assembly uses only ``O(m q + q n + n^2)`` working memory, where
``m`` is the Galerkin dimension, ``q`` the quadrature order, and ``n`` the
number of probes.

This is a necessary-condition diagnostic, not a certified discretization of
the infinite-dimensional adjoint.  A persistent failure rules out the naive
exact unitary, parameter-preserving intertwiner in the tested Galerkin model.
It does not rule out nonunitary embeddings, spectral dilation, or asymptotic
graph/resolvent convergence.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from typing import Sequence

import numpy as np
from numpy.polynomial.legendre import leggauss

from shift_phase_covariance_falsifier import (
    dirichlet_energy_metric,
    hermitian_part,
    orthonormal_dirichlet_sine_values,
    orthonormal_legendre_values,
    scalar_coercive_metric,
)


def parse_probe(value: str) -> complex:
    """Parse a command-line probe, accepting Python's ``j`` notation."""

    try:
        return complex(value.replace("i", "j"))
    except ValueError as error:
        raise argparse.ArgumentTypeError(f"invalid complex probe: {value}") from error


class DeficiencyKernelFamily:
    """Projected resolvent kernels for all scalar shifts of one metric."""

    def __init__(
        self,
        metric: np.ndarray,
        radius: float,
        probes: Sequence[complex],
        quadrature_order: int | None = None,
        basis_kind: str = "legendre",
    ) -> None:
        matrix = hermitian_part(metric)
        if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
            raise ValueError("metric must be square")
        if radius <= 0:
            raise ValueError("radius must be positive")
        probe_array = np.asarray(probes, dtype=complex)
        if probe_array.ndim != 1 or probe_array.size < 2:
            raise ValueError("at least two one-dimensional probes are required")

        dimension = matrix.shape[0]
        order = quadrature_order or max(128, 8 * dimension)
        scaled_nodes, scaled_weights = leggauss(order)
        nodes = radius * scaled_nodes
        weights = radius * scaled_weights
        if basis_kind == "legendre":
            basis = orthonormal_legendre_values(
                dimension, radius, scaled_nodes
            )
        elif basis_kind == "dirichlet-sine":
            basis = orthonormal_dirichlet_sine_values(
                dimension, radius, scaled_nodes
            )
        else:
            raise ValueError("unknown basis kind")

        # Columns are the L2 projections of exp(-i z x).  The exponentials
        # matrix is only order-by-number-of-probes, never a dense z-grid.
        exponentials = np.exp(-1j * np.outer(nodes, probe_array))
        rhs = basis.conj().T @ (weights[:, None] * exponentials)
        eigenvalues, eigenvectors = np.linalg.eigh(matrix)
        self.metric = matrix
        self.radius = float(radius)
        self.probes = probe_array
        self.dimension = dimension
        self.basis_kind = basis_kind
        self.metric_floor = float(eigenvalues[0])
        self.eigenvalues = eigenvalues
        self.nodes = nodes
        self.spectral_projection = (
            eigenvectors.conj().T @ (basis.conj().T * weights[None, :])
        )
        self.rhs_in_eigenbasis = eigenvectors.conj().T @ rhs

    def _rhs(self, probes: Sequence[complex] | None) -> np.ndarray:
        if probes is None:
            return self.rhs_in_eigenbasis
        values = np.asarray(probes, dtype=complex)
        if values.ndim != 1 or values.size < 2:
            raise ValueError("at least two one-dimensional probes are required")
        exponentials = np.exp(-1j * np.outer(self.nodes, values))
        return self.spectral_projection @ exponentials

    def kernel(
        self, shift: float, probes: Sequence[complex] | None = None
    ) -> np.ndarray:
        """Return ``<d(z_i),d(z_j)>_T = <e_i,T^-1 e_j>``."""

        if not shift < self.metric_floor:
            raise ValueError("shift must lie strictly below the metric floor")
        rhs = self._rhs(probes)
        inverse_weights = 1.0 / (self.eigenvalues - shift)
        weighted_rhs = inverse_weights[:, None] * rhs
        kernel = rhs.conj().T @ weighted_rhs
        return hermitian_part(kernel)

    def normalized_kernel(
        self, shift: float, probes: Sequence[complex] | None = None
    ) -> np.ndarray:
        """Return the Gram kernel of the energy-normalized deficiency lines."""

        kernel = self.kernel(shift, probes=probes)
        diagonal = np.real(np.diag(kernel))
        if np.any(diagonal <= 1e-14 * max(1.0, float(np.max(diagonal)))):
            raise FloatingPointError("a projected deficiency vector is too small")
        scale = np.sqrt(diagonal[:, None] * diagonal[None, :])
        normalized = kernel / scale
        np.fill_diagonal(normalized, 1.0)
        return hermitian_part(normalized)


@dataclass(frozen=True)
class ProjectiveKernelResidual:
    probe_count: int
    magnitude_rms: float
    magnitude_max: float
    bargmann_phase_rms: float
    bargmann_phase_max: float
    gauge_residual_rms: float
    gauge_residual_max: float
    gauge_anchor: int


def _off_diagonal_values(matrix: np.ndarray) -> np.ndarray:
    indices = np.triu_indices(matrix.shape[0], 1)
    return matrix[indices]


def _bargmann_phase_errors(
    reference: np.ndarray, target: np.ndarray, tolerance: float = 1e-12
) -> np.ndarray:
    errors: list[float] = []
    count = reference.shape[0]
    for i in range(count):
        for j in range(i + 1, count):
            for k in range(j + 1, count):
                reference_cycle = (
                    reference[i, j] * reference[j, k] * reference[k, i]
                )
                target_cycle = target[i, j] * target[j, k] * target[k, i]
                if (
                    abs(reference_cycle) > tolerance
                    and abs(target_cycle) > tolerance
                ):
                    errors.append(
                        float(np.angle(target_cycle * np.conj(reference_cycle)))
                    )
    return np.asarray(errors, dtype=float)


def _best_gauge_residual(
    reference: np.ndarray, target: np.ndarray, tolerance: float = 1e-12
) -> tuple[float, float, int]:
    count = reference.shape[0]
    off_diagonal = ~np.eye(count, dtype=bool)
    denominator = float(np.linalg.norm(reference[off_diagonal]))
    best = (np.inf, np.inf, -1)
    for anchor in range(count):
        phases = np.ones(count, dtype=complex)
        usable = True
        for j in range(count):
            if j == anchor:
                continue
            product = target[anchor, j] * np.conj(reference[anchor, j])
            if abs(product) <= tolerance:
                usable = False
                break
            phases[j] = product / abs(product)
        if not usable:
            continue
        predicted = np.conj(phases[:, None]) * phases[None, :] * reference
        error = (target - predicted)[off_diagonal]
        relative_rms = float(np.linalg.norm(error) / max(denominator, tolerance))
        maximum = float(np.max(np.abs(error)))
        if relative_rms < best[0]:
            best = (relative_rms, maximum, anchor)
    if best[2] < 0:
        raise FloatingPointError("no nondegenerate phase-gauge anchor exists")
    return best


def compare_projective_kernels(
    reference: np.ndarray, target: np.ndarray
) -> ProjectiveKernelResidual:
    """Compare two normalized kernels modulo independent line phases."""

    reference = hermitian_part(reference)
    target = hermitian_part(target)
    if reference.shape != target.shape or reference.ndim != 2:
        raise ValueError("normalized kernels must have the same square shape")
    if reference.shape[0] < 2:
        raise ValueError("at least two probes are required")

    magnitude_error = _off_diagonal_values(
        np.abs(target) - np.abs(reference)
    )
    phase_error = _bargmann_phase_errors(reference, target)
    gauge_rms, gauge_max, anchor = _best_gauge_residual(reference, target)
    return ProjectiveKernelResidual(
        probe_count=reference.shape[0],
        magnitude_rms=float(np.sqrt(np.mean(magnitude_error**2))),
        magnitude_max=float(np.max(np.abs(magnitude_error))),
        bargmann_phase_rms=(
            float(np.sqrt(np.mean(phase_error**2))) if phase_error.size else 0.0
        ),
        bargmann_phase_max=(
            float(np.max(np.abs(phase_error))) if phase_error.size else 0.0
        ),
        gauge_residual_rms=gauge_rms,
        gauge_residual_max=gauge_max,
        gauge_anchor=anchor,
    )


@dataclass(frozen=True)
class TunedIntertwinerDiagnostic:
    reference_shift: float
    target_shift: float
    objective: float
    train: ProjectiveKernelResidual
    holdout: ProjectiveKernelResidual
    full: ProjectiveKernelResidual


@dataclass(frozen=True)
class AffineIntertwinerDiagnostic:
    """Result of a bounded real-affine spectral-parameter fit."""

    reference_shift: float
    target_shift: float
    alpha: float
    beta: float
    objective: float
    optimum_on_boundary: bool
    train: ProjectiveKernelResidual
    holdout: ProjectiveKernelResidual
    full: ProjectiveKernelResidual


def evaluate_shift_pair(
    reference: DeficiencyKernelFamily,
    target: DeficiencyKernelFamily,
    reference_shift: float,
    target_shift: float,
    train_indices: Sequence[int],
    holdout_indices: Sequence[int],
) -> TunedIntertwinerDiagnostic:
    """Evaluate one fixed pair of shifts without fitting either parameter."""

    if reference.probes.shape != target.probes.shape or not np.allclose(
        reference.probes, target.probes
    ):
        raise ValueError("reference and target must use identical probes")
    train = np.asarray(train_indices, dtype=int)
    holdout = np.asarray(holdout_indices, dtype=int)
    reference_kernel = reference.normalized_kernel(reference_shift)
    target_kernel = target.normalized_kernel(target_shift)
    return TunedIntertwinerDiagnostic(
        reference_shift=float(reference_shift),
        target_shift=float(target_shift),
        objective=float("nan"),
        train=compare_projective_kernels(
            reference_kernel[np.ix_(train, train)],
            target_kernel[np.ix_(train, train)],
        ),
        holdout=compare_projective_kernels(
            reference_kernel[np.ix_(holdout, holdout)],
            target_kernel[np.ix_(holdout, holdout)],
        ),
        full=compare_projective_kernels(reference_kernel, target_kernel),
    )


def evaluate_affine_pair(
    reference: DeficiencyKernelFamily,
    target: DeficiencyKernelFamily,
    reference_shift: float,
    target_shift: float,
    alpha: float,
    beta: float,
    train_indices: Sequence[int],
    holdout_indices: Sequence[int],
) -> AffineIntertwinerDiagnostic:
    """Evaluate ``z_target = alpha*z_reference + beta`` at fixed shifts."""

    if alpha <= 0:
        raise ValueError("the affine scale alpha must be positive")
    train = np.asarray(train_indices, dtype=int)
    holdout = np.asarray(holdout_indices, dtype=int)
    reference_kernel = reference.normalized_kernel(reference_shift)
    mapped_probes = alpha * reference.probes + beta
    target_kernel = target.normalized_kernel(target_shift, probes=mapped_probes)
    train_residual = compare_projective_kernels(
        reference_kernel[np.ix_(train, train)],
        target_kernel[np.ix_(train, train)],
    )
    return AffineIntertwinerDiagnostic(
        reference_shift=float(reference_shift),
        target_shift=float(target_shift),
        alpha=float(alpha),
        beta=float(beta),
        objective=train_residual.gauge_residual_rms,
        optimum_on_boundary=False,
        train=train_residual,
        holdout=compare_projective_kernels(
            reference_kernel[np.ix_(holdout, holdout)],
            target_kernel[np.ix_(holdout, holdout)],
        ),
        full=compare_projective_kernels(reference_kernel, target_kernel),
    )


def tune_affine_reparameterization(
    reference: DeficiencyKernelFamily,
    target: DeficiencyKernelFamily,
    reference_shift: float,
    target_shift: float,
    alpha_min: float,
    alpha_max: float,
    beta_min: float,
    beta_max: float,
    train_indices: Sequence[int],
    holdout_indices: Sequence[int],
    grid_size: int = 33,
    refinement_levels: int = 3,
) -> AffineIntertwinerDiagnostic:
    """Fit a bounded real-affine spectral map by deterministic grid refinement.

    This deliberately avoids a local nonlinear optimizer: the phase-gauge
    objective is only piecewise smooth.  ``optimum_on_boundary`` warns that the
    supplied search box did not contain a resolved interior minimum.
    """

    if not 0 < alpha_min < alpha_max:
        raise ValueError("alpha bounds must be positive and increasing")
    if not beta_min < beta_max:
        raise ValueError("beta bounds must be increasing")
    if grid_size < 5 or refinement_levels < 1:
        raise ValueError("the affine grid is too small")
    train = np.asarray(train_indices, dtype=int)
    holdout = np.asarray(holdout_indices, dtype=int)
    if train.size < 3 or holdout.size < 2:
        raise ValueError("use at least three training and two holdout probes")
    if np.intersect1d(train, holdout).size:
        raise ValueError("training and holdout indices must be disjoint")

    reference_full = reference.normalized_kernel(reference_shift)
    reference_train = reference_full[np.ix_(train, train)]
    train_probes = reference.probes[train]

    def objective(alpha: float, beta: float) -> float:
        mapped = alpha * train_probes + beta
        target_train = target.normalized_kernel(target_shift, probes=mapped)
        return compare_projective_kernels(
            reference_train, target_train
        ).gauge_residual_rms

    original_bounds = (alpha_min, alpha_max, beta_min, beta_max)
    best_alpha = (alpha_min + alpha_max) / 2.0
    best_beta = (beta_min + beta_max) / 2.0
    best_value = np.inf
    for _ in range(refinement_levels):
        alphas = np.linspace(alpha_min, alpha_max, grid_size)
        betas = np.linspace(beta_min, beta_max, grid_size)
        level_best = (np.inf, best_alpha, best_beta, 0, 0)
        for alpha_index, alpha in enumerate(alphas):
            for beta_index, beta in enumerate(betas):
                value = objective(float(alpha), float(beta))
                if value < level_best[0]:
                    level_best = (
                        value,
                        float(alpha),
                        float(beta),
                        alpha_index,
                        beta_index,
                    )
        best_value, best_alpha, best_beta, _, _ = level_best
        alpha_step = float(alphas[1] - alphas[0])
        beta_step = float(betas[1] - betas[0])
        alpha_min = max(original_bounds[0], best_alpha - alpha_step)
        alpha_max = min(original_bounds[1], best_alpha + alpha_step)
        beta_min = max(original_bounds[2], best_beta - beta_step)
        beta_max = min(original_bounds[3], best_beta + beta_step)

    alpha_span = original_bounds[1] - original_bounds[0]
    beta_span = original_bounds[3] - original_bounds[2]
    boundary_tolerance = 1e-8
    on_boundary = (
        best_alpha - original_bounds[0] <= boundary_tolerance * alpha_span
        or original_bounds[1] - best_alpha <= boundary_tolerance * alpha_span
        or best_beta - original_bounds[2] <= boundary_tolerance * beta_span
        or original_bounds[3] - best_beta <= boundary_tolerance * beta_span
    )
    mapped_full = best_alpha * reference.probes + best_beta
    target_full = target.normalized_kernel(target_shift, probes=mapped_full)
    return AffineIntertwinerDiagnostic(
        reference_shift=float(reference_shift),
        target_shift=float(target_shift),
        alpha=best_alpha,
        beta=best_beta,
        objective=float(best_value),
        optimum_on_boundary=on_boundary,
        train=compare_projective_kernels(
            reference_train, target_full[np.ix_(train, train)]
        ),
        holdout=compare_projective_kernels(
            reference_full[np.ix_(holdout, holdout)],
            target_full[np.ix_(holdout, holdout)],
        ),
        full=compare_projective_kernels(reference_full, target_full),
    )


def _golden_section_minimize(
    function, left: float, right: float, iterations: int = 48
) -> tuple[float, float]:
    ratio = (np.sqrt(5.0) - 1.0) / 2.0
    x_left = right - ratio * (right - left)
    x_right = left + ratio * (right - left)
    f_left = float(function(x_left))
    f_right = float(function(x_right))
    for _ in range(iterations):
        if f_left <= f_right:
            right, x_right, f_right = x_right, x_left, f_left
            x_left = right - ratio * (right - left)
            f_left = float(function(x_left))
        else:
            left, x_left, f_left = x_left, x_right, f_right
            x_right = left + ratio * (right - left)
            f_right = float(function(x_right))
    if f_left <= f_right:
        return float(x_left), f_left
    return float(x_right), f_right


def tune_target_shift(
    reference: DeficiencyKernelFamily,
    target: DeficiencyKernelFamily,
    reference_shift: float,
    shift_min: float,
    shift_max: float,
    train_indices: Sequence[int],
    holdout_indices: Sequence[int],
    grid_size: int = 257,
) -> TunedIntertwinerDiagnostic:
    """Tune one shift on training probes and report held-out invariants."""

    if reference.probes.shape != target.probes.shape or not np.allclose(
        reference.probes, target.probes
    ):
        raise ValueError("reference and target must use identical probes")
    if not shift_min < shift_max < target.metric_floor:
        raise ValueError("the target shift interval must lie below its metric floor")
    train = np.asarray(train_indices, dtype=int)
    holdout = np.asarray(holdout_indices, dtype=int)
    if train.size < 3 or holdout.size < 2:
        raise ValueError("use at least three training and two holdout probes")
    if np.intersect1d(train, holdout).size:
        raise ValueError("training and holdout indices must be disjoint")
    count = reference.probes.size
    if (
        np.any(train < 0)
        or np.any(train >= count)
        or np.any(holdout < 0)
        or np.any(holdout >= count)
    ):
        raise IndexError("a probe index is out of range")

    reference_full = reference.normalized_kernel(reference_shift)
    reference_train = reference_full[np.ix_(train, train)]

    def objective(shift: float) -> float:
        target_kernel = target.normalized_kernel(shift)
        target_train = target_kernel[np.ix_(train, train)]
        return compare_projective_kernels(
            reference_train, target_train
        ).gauge_residual_rms

    grid = np.linspace(shift_min, shift_max, grid_size)
    values = np.asarray([objective(float(shift)) for shift in grid])
    best_index = int(np.argmin(values))
    candidates = [(float(grid[best_index]), float(values[best_index]))]
    # The best-gauge objective is continuous away from degenerate correlations
    # but need not be globally unimodal.  Refine every grid-local minimum and
    # retain the best value including the original grid samples.
    for index in range(1, grid.size - 1):
        if values[index] <= values[index - 1] and values[index] <= values[index + 1]:
            candidates.append(
                _golden_section_minimize(
                    objective, float(grid[index - 1]), float(grid[index + 1])
                )
            )
    target_shift, best_value = min(candidates, key=lambda candidate: candidate[1])

    target_full = target.normalized_kernel(target_shift)
    train_residual = compare_projective_kernels(
        reference_train, target_full[np.ix_(train, train)]
    )
    holdout_residual = compare_projective_kernels(
        reference_full[np.ix_(holdout, holdout)],
        target_full[np.ix_(holdout, holdout)],
    )
    return TunedIntertwinerDiagnostic(
        reference_shift=float(reference_shift),
        target_shift=target_shift,
        objective=best_value,
        train=train_residual,
        holdout=holdout_residual,
        full=compare_projective_kernels(reference_full, target_full),
    )


def diagnostic_row(
    model: str,
    reference_support: float,
    target_support: float,
    dimension: int,
    diagnostic: TunedIntertwinerDiagnostic,
) -> dict[str, str | int | float]:
    """Flatten the diagnostic into a stable CSV row."""

    return {
        "model": model,
        "reference_support": reference_support,
        "target_support": target_support,
        "dimension": dimension,
        "reference_shift": diagnostic.reference_shift,
        "target_shift": diagnostic.target_shift,
        "train_gauge_rms": diagnostic.train.gauge_residual_rms,
        "train_magnitude_max": diagnostic.train.magnitude_max,
        "train_bargmann_phase_max": diagnostic.train.bargmann_phase_max,
        "holdout_gauge_rms": diagnostic.holdout.gauge_residual_rms,
        "holdout_magnitude_max": diagnostic.holdout.magnitude_max,
        "holdout_bargmann_phase_max": diagnostic.holdout.bargmann_phase_max,
        "full_gauge_rms": diagnostic.full.gauge_residual_rms,
        "full_magnitude_max": diagnostic.full.magnitude_max,
        "full_bargmann_phase_max": diagnostic.full.bargmann_phase_max,
        "affine_alpha": "",
        "affine_beta": "",
        "affine_optimum_on_boundary": "",
    }


def affine_diagnostic_row(
    model: str,
    reference_support: float,
    target_support: float,
    dimension: int,
    diagnostic: AffineIntertwinerDiagnostic,
) -> dict[str, str | int | float | bool]:
    """Flatten an affine diagnostic into the common CSV schema."""

    return {
        "model": model,
        "reference_support": reference_support,
        "target_support": target_support,
        "dimension": dimension,
        "reference_shift": diagnostic.reference_shift,
        "target_shift": diagnostic.target_shift,
        "train_gauge_rms": diagnostic.train.gauge_residual_rms,
        "train_magnitude_max": diagnostic.train.magnitude_max,
        "train_bargmann_phase_max": diagnostic.train.bargmann_phase_max,
        "holdout_gauge_rms": diagnostic.holdout.gauge_residual_rms,
        "holdout_magnitude_max": diagnostic.holdout.magnitude_max,
        "holdout_bargmann_phase_max": diagnostic.holdout.bargmann_phase_max,
        "full_gauge_rms": diagnostic.full.gauge_residual_rms,
        "full_magnitude_max": diagnostic.full.magnitude_max,
        "full_bargmann_phase_max": diagnostic.full.bargmann_phase_max,
        "affine_alpha": diagnostic.alpha,
        "affine_beta": diagnostic.beta,
        "affine_optimum_on_boundary": diagnostic.optimum_on_boundary,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--supports", type=float, nargs="+", default=[1.75, 2.485, 2.996]
    )
    parser.add_argument("--dimensions", type=int, nargs="+", default=[8])
    parser.add_argument("--dps", type=int, default=30)
    parser.add_argument(
        "--reference-shifts", type=float, nargs="+", default=[-0.05, -0.25]
    )
    parser.add_argument("--shift-min", type=float, default=-2.0)
    parser.add_argument("--shift-max", type=float, default=-0.001)
    parser.add_argument(
        "--fit-affine",
        action="store_true",
        help="fit z_target = alpha*z_reference + beta at each common shift",
    )
    parser.add_argument("--alpha-min", type=float, default=0.4)
    parser.add_argument("--alpha-max", type=float, default=1.2)
    parser.add_argument("--beta-min", type=float, default=-4.0)
    parser.add_argument("--beta-max", type=float, default=4.0)
    parser.add_argument("--affine-grid-size", type=int, default=33)
    parser.add_argument("--affine-refinements", type=int, default=3)
    parser.add_argument(
        "--probes",
        type=parse_probe,
        nargs="+",
        default=[-7.0, -3.0, 0.0, 3.0, 7.0, 11.0, 1j, -1j],
    )
    args = parser.parse_args()
    if len(args.supports) < 2:
        parser.error("at least two nested supports are required")
    if len(args.probes) < 7:
        parser.error("use at least seven probes for train/holdout separation")

    # Alternate training and holdout probes so both sets span the z-range.
    train = np.arange(0, len(args.probes), 2)
    holdout = np.arange(1, len(args.probes), 2)
    if train.size < 3 or holdout.size < 2:
        parser.error("the probe split is too small")

    fieldnames = [
        "model",
        "reference_support",
        "target_support",
        "dimension",
        "reference_shift",
        "target_shift",
        "train_gauge_rms",
        "train_magnitude_max",
        "train_bargmann_phase_max",
        "holdout_gauge_rms",
        "holdout_magnitude_max",
        "holdout_bargmann_phase_max",
        "full_gauge_rms",
        "full_magnitude_max",
        "full_bargmann_phase_max",
        "affine_alpha",
        "affine_beta",
        "affine_optimum_on_boundary",
    ]
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    writer.writeheader()

    # Exact positive control: a scalar metric changes only by an overall
    # resolvent factor, which disappears after projective normalization.
    control_dimension = max(args.dimensions)
    control_radius = 0.75
    scalar = DeficiencyKernelFamily(
        scalar_coercive_metric(control_dimension),
        control_radius,
        args.probes,
    )
    writer.writerow(
        diagnostic_row(
            "scalar-positive-control",
            2.0 * control_radius,
            2.0 * control_radius,
            control_dimension,
            evaluate_shift_pair(scalar, scalar, 0.0, -1.0, train, holdout),
        )
    )

    if args.fit_affine:
        dilation_reference_radius = 0.55
        dilation_target_radius = 0.9
        dilation_reference = DeficiencyKernelFamily(
            scalar_coercive_metric(control_dimension),
            dilation_reference_radius,
            args.probes,
        )
        dilation_target = DeficiencyKernelFamily(
            scalar_coercive_metric(control_dimension),
            dilation_target_radius,
            args.probes,
        )
        writer.writerow(
            affine_diagnostic_row(
                "scalar-affine-dilation-control",
                2.0 * dilation_reference_radius,
                2.0 * dilation_target_radius,
                control_dimension,
                evaluate_affine_pair(
                    dilation_reference,
                    dilation_target,
                    0.0,
                    0.0,
                    dilation_reference_radius / dilation_target_radius,
                    0.0,
                    train,
                    holdout,
                ),
            )
        )

    # Genuine continuum negative control: changing the shift reweights the
    # Dirichlet eigenmodes unequally, so the projective kernel drifts.
    dirichlet = DeficiencyKernelFamily(
        dirichlet_energy_metric(control_dimension, control_radius),
        control_radius,
        args.probes,
        basis_kind="dirichlet-sine",
    )
    writer.writerow(
        diagnostic_row(
            "dirichlet-negative-control",
            2.0 * control_radius,
            2.0 * control_radius,
            control_dimension,
            evaluate_shift_pair(
                dirichlet, dirichlet, 0.0, -1.0, train, holdout
            ),
        )
    )

    # Imported lazily: completed-Weil assembly is the expensive part.
    from spectral_margins import spectral_form

    for dimension in args.dimensions:
        families: list[DeficiencyKernelFamily] = []
        for support in args.supports:
            metric = np.asarray(
                spectral_form(support, dimension, dps=args.dps).tolist(),
                dtype=float,
            )
            families.append(
                DeficiencyKernelFamily(
                    metric, support / 4.0, args.probes, basis_kind="legendre"
                )
            )
        reference = families[0]
        for reference_shift in args.reference_shifts:
            if not reference_shift < reference.metric_floor:
                parser.error(
                    f"reference shift {reference_shift} is not below the "
                    f"metric floor {reference.metric_floor} at dimension {dimension}"
                )
            for target_support, target in zip(args.supports[1:], families[1:]):
                # Exact nesting prefers a common shift.  Report that canonical
                # comparison before allowing a separately tuned target shift.
                common = evaluate_shift_pair(
                    reference,
                    target,
                    reference_shift,
                    reference_shift,
                    train,
                    holdout,
                )
                writer.writerow(
                    diagnostic_row(
                        "completed-Weil-common-shift",
                        args.supports[0],
                        target_support,
                        dimension,
                        common,
                    )
                )
                if args.fit_affine:
                    affine = tune_affine_reparameterization(
                        reference,
                        target,
                        reference_shift,
                        reference_shift,
                        args.alpha_min,
                        args.alpha_max,
                        args.beta_min,
                        args.beta_max,
                        train,
                        holdout,
                        grid_size=args.affine_grid_size,
                        refinement_levels=args.affine_refinements,
                    )
                    writer.writerow(
                        affine_diagnostic_row(
                            "completed-Weil-affine-common-shift",
                            args.supports[0],
                            target_support,
                            dimension,
                            affine,
                        )
                    )
                diagnostic = tune_target_shift(
                    reference,
                    target,
                    reference_shift,
                    args.shift_min,
                    args.shift_max,
                    train,
                    holdout,
                )
                writer.writerow(
                    diagnostic_row(
                        "completed-Weil-tuned-shift",
                        args.supports[0],
                        target_support,
                        dimension,
                        diagnostic,
                    )
                )


if __name__ == "__main__":
    main()
