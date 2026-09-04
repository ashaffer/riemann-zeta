"""Finite checks for the signed-discrepancy affine-carrier gate.

The mathematical report proves the exact statements.  This module keeps the
normalizations and the elementary finite identities replayable.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np


@dataclass(frozen=True)
class GridAudit:
    mesh: float
    grid_points: int
    derivative_bound: float


def continuum_grid_audit(
    *,
    lower: float,
    upper: float,
    shell_width: float,
    coefficient_l1: float,
    carrier: float,
    epsilon: float,
) -> GridAudit:
    """Grid sufficient for passing a half-epsilon bound to the continuum.

    If ``F(t)=sum c_j cos(t u_j)``, ``|u_j|<=shell_width``, then
    ``|F'|<=shell_width*||c||_1``.  A grid with the returned mesh, including
    both endpoints, turns ``F>=-epsilon*carrier/2`` on the grid into
    ``F>=-epsilon*carrier`` on the interval.
    """

    if not 0.0 <= lower < upper:
        raise ValueError("require 0 <= lower < upper")
    if shell_width <= 0.0 or coefficient_l1 <= 0.0:
        raise ValueError("width and l1 norm must be positive")
    if carrier <= 0.0 or epsilon <= 0.0:
        raise ValueError("carrier and epsilon must be positive")
    derivative = shell_width * coefficient_l1
    mesh = epsilon * carrier / (2.0 * derivative)
    points = 1 + math.ceil((upper - lower) / mesh)
    return GridAudit(mesh=mesh, grid_points=points, derivative_bound=derivative)


def cosine_values(coefficients: np.ndarray, nodes: np.ndarray, times: np.ndarray) -> np.ndarray:
    coefficients = np.asarray(coefficients, dtype=float)
    nodes = np.asarray(nodes, dtype=float)
    times = np.asarray(times, dtype=float)
    if coefficients.ndim != 1 or nodes.ndim != 1 or coefficients.size != nodes.size:
        raise ValueError("coefficients and nodes must be matching vectors")
    return np.cos(np.outer(times, nodes)) @ coefficients


def rounding_seed_lower_bound(
    rounded_lower: np.ndarray,
    spectral_error: float,
) -> np.ndarray:
    """Worst lower bound for a seed after subtracting rounding error."""

    if spectral_error < 0.0:
        raise ValueError("spectral error must be nonnegative")
    return np.asarray(rounded_lower, dtype=float) - spectral_error


def required_sign_carrier(discrepancy: float, epsilon: float) -> float:
    """Carrier needed to normalize absolute discrepancy to ``epsilon``."""

    if discrepancy < 0.0 or epsilon <= 0.0:
        raise ValueError("invalid discrepancy or epsilon")
    return discrepancy / epsilon


def conditional_sign_mean(atom: np.ndarray, carrier: int) -> float:
    """Exact E[sum sigma_j atom_j | sum sigma_j = carrier]."""

    atom = np.asarray(atom, dtype=float)
    if atom.ndim != 1 or atom.size == 0:
        raise ValueError("atom must be a nonempty vector")
    if abs(carrier) > atom.size or (carrier - atom.size) % 2:
        raise ValueError("carrier is not attainable by a sign vector")
    return float(carrier * np.mean(atom))


def half_grid_nodes(indices: np.ndarray, aperture: float) -> np.ndarray:
    """Nodes whose cosine values at ``aperture`` are all exactly minus one."""

    indices = np.asarray(indices, dtype=int)
    if indices.ndim != 1 or aperture <= 0.0:
        raise ValueError("invalid indices or aperture")
    return (2.0 * indices + 1.0) * math.pi / aperture


def half_grid_normalized_value(coefficients: np.ndarray, nodes: np.ndarray, aperture: float) -> float:
    """Evaluate the normalized signed antenna at a half-grid aperture."""

    coefficients = np.asarray(coefficients, dtype=float)
    carrier = float(np.sum(coefficients))
    if carrier == 0.0:
        raise ValueError("zero carrier")
    return float(cosine_values(coefficients, nodes, np.array([aperture]))[0] / carrier)


def perturbed_half_grid_error_bound(
    *, phase_perturbation: float, normalized_total_variation: float
) -> float:
    """Bound ``|F(B)/S+1|`` for a perturbed odd-half-period grid.

    The phase perturbations are bounded in modulus by ``phase_perturbation``.
    The inequality ``1-cos x <= x^2/2`` gives the result.
    """

    if phase_perturbation < 0.0 or normalized_total_variation < 0.0:
        raise ValueError("bounds must be nonnegative")
    return 0.5 * phase_perturbation**2 * normalized_total_variation


def finite_symmetric_discrepancy(matrix: np.ndarray) -> float:
    """Compute min ||A^T y||_infinity subject to ``sum(y)=1``.

    ``matrix`` has node rows and sampled-frequency columns.  This is only a
    finite replay of the continuous symmetric problem.
    """

    from scipy.optimize import linprog

    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("matrix must be nonempty")
    m, r = matrix.shape
    # Variables are y_1,...,y_m,d with +/- A^T y <= d.
    objective = np.r_[np.zeros(m), 1.0]
    upper = np.vstack(
        (
            np.c_[matrix.T, -np.ones(r)],
            np.c_[-matrix.T, -np.ones(r)],
        )
    )
    result = linprog(
        objective,
        A_ub=upper,
        b_ub=np.zeros(2 * r),
        A_eq=np.r_[np.ones(m), 0.0][None, :],
        b_eq=np.array([1.0]),
        bounds=[(None, None)] * m + [(0.0, None)],
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    return float(result.x[-1])


def finite_signed_synthesis_cost(matrix: np.ndarray) -> float:
    """Compute min ||z||_1 subject to ``A z = q`` for a finite dictionary."""

    from scipy.optimize import linprog

    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("matrix must be nonempty")
    m, r = matrix.shape
    # z=z+ - z-.
    objective = np.ones(2 * r)
    result = linprog(
        objective,
        A_eq=np.c_[matrix, -matrix],
        b_eq=np.ones(m),
        bounds=[(0.0, None)] * (2 * r),
        method="highs",
    )
    if not result.success:
        return math.inf
    return float(result.fun)


def verify_finite_polar_identity(matrix: np.ndarray, tolerance: float = 1e-8) -> bool:
    """Check ``symmetric discrepancy * signed synthesis cost = 1``."""

    discrepancy = finite_symmetric_discrepancy(matrix)
    cost = finite_signed_synthesis_cost(matrix)
    return math.isfinite(cost) and abs(discrepancy * cost - 1.0) <= tolerance


if __name__ == "__main__":
    sample = np.array(
        [
            [1.0, 0.2, -0.4, 0.7],
            [0.1, 1.0, 0.5, -0.2],
            [-0.3, 0.4, 1.0, 0.1],
        ]
    )
    if not verify_finite_polar_identity(sample):
        raise SystemExit("finite polar identity failed")
    print("signed discrepancy affine-carrier gate: verified")
