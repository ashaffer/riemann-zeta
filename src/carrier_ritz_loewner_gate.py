"""Low-dimensional Ritz witnesses for a rank-one carrier slice.

For a Hermitian completed-arithmetic matrix ``K`` and

    N = kappa * a a^*,  ||a|| = 1,

the direct carrier edge is the maximum of ``<z,Kz>`` over unit vectors with
``|<a,z>|^2 >= theta``.  This module evaluates the exact restriction to
``span(a,w)`` and constructs two canonical, zero-independent companion
directions:

* ``P_(a perp) B a`` for a completed background matrix ``B``;
* ``P_(a perp) J a`` for the compressed Jacobi/coordinate operator ``J``;
* the projected target-depth derivative of the selected evaluation row.

It also exposes the prime-adaptive Lanczos direction ``P_(a perp) K a``.
That direction is useful diagnostically, but its scalar entries contain
quadratic and cubic moments of the arithmetic matrix and therefore are not
a linear completed-prime reduction.

The routines are finite-dimensional floating diagnostics.  The exact
formula implemented by :func:`two_dimensional_carrier_ritz` is proved in the
companion theorem card under ``results/``.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import argparse
import json
import math
from typing import Any, Iterable

import numpy as np
from scipy.linalg import null_space

from carrier_slice_support import carrier_slice_support
from high_height_carrier_slice import (
    archimedean_matrix_sign,
    endpoint_null_basis,
    pole_matrix_sign,
    prime_matrix_sign,
    rational_pole_matrix_sign,
    selected_rows_sign,
)
from signed_garding_failfast import prime_powers


@dataclass(frozen=True)
class TwoDimensionalRitzResult:
    """Exact carrier-constrained maximum on ``span(a,w)``."""

    value: float
    boundary_value: float
    unconstrained_top_value: float
    unconstrained_top_carrier_mass: float
    carrier_diagonal: float
    complement_diagonal: float
    coupling_modulus: float
    boundary_active: bool


def _hermitian(matrix: np.ndarray) -> np.ndarray:
    answer = np.asarray(matrix, dtype=complex)
    if answer.ndim != 2 or answer.shape[0] != answer.shape[1]:
        raise ValueError("matrix must be square")
    scale = max(1.0, float(np.linalg.norm(answer, ord=2)))
    if np.linalg.norm(answer - answer.conj().T, ord=2) > 1e-10 * scale:
        raise ValueError("matrix must be Hermitian")
    return (answer + answer.conj().T) / 2.0


def _unit(vector: np.ndarray, *, tolerance: float = 1e-12) -> np.ndarray:
    answer = np.asarray(vector, dtype=complex).reshape(-1)
    norm = float(np.linalg.norm(answer))
    if norm <= tolerance:
        raise ValueError("vector has negligible norm")
    return answer / norm


def orthogonal_companion(
    carrier_direction: np.ndarray,
    proposed_direction: np.ndarray,
    *,
    tolerance: float = 1e-12,
) -> np.ndarray:
    """Normalize the component of ``proposed_direction`` orthogonal to ``a``."""
    a = _unit(carrier_direction, tolerance=tolerance)
    proposed = np.asarray(proposed_direction, dtype=complex).reshape(-1)
    if proposed.shape != a.shape:
        raise ValueError("direction shapes differ")
    perpendicular = proposed - a * np.vdot(a, proposed)
    return _unit(perpendicular, tolerance=tolerance)


def canonical_companion(
    operator: np.ndarray, carrier_direction: np.ndarray
) -> np.ndarray:
    """Return ``P_(a perp) operator*a`` as a unit vector."""
    matrix = _hermitian(operator)
    a = _unit(carrier_direction)
    if matrix.shape[0] != a.size:
        raise ValueError("operator and carrier dimensions differ")
    return orthogonal_companion(a, matrix @ a)


def two_dimensional_ritz_from_entries(
    carrier_diagonal: float,
    complement_diagonal: float,
    coupling_modulus: float,
    theta: float,
) -> TwoDimensionalRitzResult:
    """Evaluate the exact constrained maximum of a Hermitian ``2 x 2`` block.

    The phase of the complement vector is chosen so that the off-diagonal
    contribution is positive.  ``theta`` is the required squared carrier
    overlap, not the carrier expectation ``theta*kappa``.
    """
    if theta < 0.0 or theta > 1.0:
        raise ValueError("theta must lie in [0,1]")
    r = float(carrier_diagonal)
    d = float(complement_diagonal)
    c = float(coupling_modulus)
    if c < -1e-14:
        raise ValueError("coupling modulus must be nonnegative")
    c = max(0.0, c)

    root = math.hypot(r - d, 2.0 * c)
    top = 0.5 * (r + d + root)
    boundary = (
        theta * r
        + (1.0 - theta) * d
        + 2.0 * math.sqrt(theta * (1.0 - theta)) * c
    )

    if root <= 1e-15 * max(1.0, abs(r), abs(d), c):
        # The block is scalar, so a top eigenvector with any carrier mass is
        # available and every feasible Rayleigh quotient equals r.
        top_mass = theta
        value = r
        boundary_active = False
    else:
        top_mass = 0.5 * (1.0 + (r - d) / root)
        if top_mass + 1e-14 >= theta:
            value = top
            boundary_active = False
        else:
            value = boundary
            boundary_active = True

    return TwoDimensionalRitzResult(
        value=float(value),
        boundary_value=float(boundary),
        unconstrained_top_value=float(top),
        unconstrained_top_carrier_mass=float(top_mass),
        carrier_diagonal=r,
        complement_diagonal=d,
        coupling_modulus=c,
        boundary_active=boundary_active,
    )


def two_dimensional_carrier_ritz(
    matrix: np.ndarray,
    carrier_direction: np.ndarray,
    complement_direction: np.ndarray,
    theta: float,
) -> TwoDimensionalRitzResult:
    """Exact carrier edge after restriction to ``span(a,w)``."""
    operator = _hermitian(matrix)
    a = _unit(carrier_direction)
    w = orthogonal_companion(a, complement_direction)
    if operator.shape[0] != a.size:
        raise ValueError("matrix and vector dimensions differ")
    r = float(np.vdot(a, operator @ a).real)
    d = float(np.vdot(w, operator @ w).real)
    c = float(abs(np.vdot(w, operator @ a)))
    return two_dimensional_ritz_from_entries(r, d, c, theta)


def lanczos_moments(
    matrix: np.ndarray, carrier_direction: np.ndarray
) -> dict[str, float]:
    """Return the exact first-step Lanczos identities through ``<a,K^3a>``."""
    operator = _hermitian(matrix)
    a = _unit(carrier_direction)
    ka = operator @ a
    k2a = operator @ ka
    m1 = float(np.vdot(a, ka).real)
    m2 = float(np.vdot(a, k2a).real)
    m3 = float(np.vdot(ka, k2a).real)
    variance = max(0.0, m2 - m1 * m1)
    if variance <= 1e-24 * max(1.0, m2 * m2):
        return {
            "m1": m1,
            "m2": m2,
            "m3": m3,
            "coupling_squared": variance,
            "complement_diagonal": math.nan,
        }
    complement = (m3 - 2.0 * m1 * m2 + m1 ** 3) / variance
    return {
        "m1": m1,
        "m2": m2,
        "m3": m3,
        "coupling_squared": variance,
        "complement_diagonal": float(complement),
    }


def _orthonormal_extension(
    carrier_direction: np.ndarray, candidates: Iterable[np.ndarray]
) -> np.ndarray:
    columns = [_unit(carrier_direction)]
    for candidate in candidates:
        vector = np.asarray(candidate, dtype=complex).reshape(-1).copy()
        for column in columns:
            vector -= column * np.vdot(column, vector)
        norm = float(np.linalg.norm(vector))
        if norm > 1e-10:
            columns.append(vector / norm)
    return np.column_stack(columns)


def _actual_fixture_operators(
    height: float,
    *,
    alpha: float,
    aperture_fraction: float,
    jet_order: int | None,
) -> dict[str, Any]:
    """Assemble the operators needed for the focused Ritz diagnostic."""
    if height <= 4:
        raise ValueError("height must exceed 4")
    length = math.log(height)
    center = 1.5 * height
    spacing = 2.0 * math.pi / length
    half_count = int(math.floor(aperture_fraction * height / spacing))
    if half_count < 2:
        raise ValueError("aperture leaves too few critical-grid nodes")
    indices = np.arange(-half_count, half_count + 1, dtype=int)
    tau = center + spacing * indices
    if jet_order is None:
        jet_order = max(3, int(math.ceil(length)))
    if jet_order + 2 > indices.size:
        raise ValueError("endpoint and selected rows leave no carrier space")

    logs, weights = prime_powers(int(math.floor(math.exp(length) + 1e-10)))
    active = logs <= length + 1e-13
    logs, weights = logs[active], weights[active]
    arch = archimedean_matrix_sign(tau, length)
    pole = pole_matrix_sign(tau, indices, length)
    prime = prime_matrix_sign(tau, length, logs, weights)
    rational = rational_pole_matrix_sign(tau, length)

    endpoint = endpoint_null_basis(indices, jet_order)
    selected_x, selected_y = selected_rows_sign(tau, center, length, alpha)
    z = center - 1j * alpha
    denominator = z - tau
    numerator = 2.0 * np.sin(length * (z - center) / 2.0)
    derivative_z = (
        length * np.cos(length * (z - center) / 2.0) * denominator
        - numerator
    ) / denominator ** 2
    selected_y_alpha = np.imag(-1j * derivative_z)
    x_endpoint = endpoint.T @ selected_x
    selected_null = null_space(x_endpoint[None, :], rcond=1e-12)
    inclusion = endpoint @ selected_null
    projected_y = inclusion.T @ selected_y
    a = _unit(projected_y)

    normalization = length * length
    kappa = float(2.0 * np.vdot(projected_y, projected_y).real / normalization)
    arithmetic = inclusion.conj().T @ (
        (arch + pole - prime) / normalization
    ) @ inclusion
    background = inclusion.conj().T @ (
        (arch + rational) / normalization
    ) @ inclusion
    coordinate = inclusion.conj().T @ np.diag(tau) @ inclusion
    return {
        "K": _hermitian(arithmetic),
        "B": _hermitian(background),
        "J": _hermitian(coordinate),
        "a": a,
        "confluent_alpha_raw": inclusion.T @ selected_y_alpha,
        "kappa": kappa,
        "dimension": int(inclusion.shape[1]),
        "jet_order": int(jet_order),
        "L": length,
    }


def actual_fixture_ritz(
    height: float,
    *,
    alpha: float = 0.4,
    aperture_fraction: float = 0.2,
    jet_order: int | None = None,
    theta_values: Iterable[float] = (0.5, 0.9),
) -> dict[str, Any]:
    """Compare canonical 2D/3D Ritz witnesses with the full carrier edge."""
    data = _actual_fixture_operators(
        height,
        alpha=alpha,
        aperture_fraction=aperture_fraction,
        jet_order=jet_order,
    )
    matrix, background, coordinate = data["K"], data["B"], data["J"]
    a, kappa = data["a"], data["kappa"]

    raw_directions: dict[str, np.ndarray] = {}
    for name, operator in (
        ("background", background),
        ("jacobi", coordinate),
        ("arithmetic_lanczos", matrix),
    ):
        try:
            raw_directions[name] = canonical_companion(operator, a)
        except ValueError:
            continue
    try:
        raw_directions["confluent_alpha"] = orthogonal_companion(
            a, data["confluent_alpha_raw"]
        )
    except ValueError:
        pass

    geometric_basis = _orthonormal_extension(
        a,
        [
            raw_directions[name]
            for name in ("background", "confluent_alpha")
            if name in raw_directions
        ],
    )
    compressed_geometric = geometric_basis.conj().T @ matrix @ geometric_basis
    carrier_geometric = np.zeros_like(compressed_geometric)
    carrier_geometric[0, 0] = kappa

    rows: list[dict[str, Any]] = []
    for theta in theta_values:
        theta = float(theta)
        if theta < 0.0 or theta > 1.0:
            raise ValueError("theta values must lie in [0,1]")
        full = carrier_slice_support(matrix, kappa * np.outer(a, a.conj()),
                                     theta * kappa, iterations=80)
        geometric = carrier_slice_support(
            compressed_geometric,
            carrier_geometric,
            theta * kappa,
            iterations=80,
        )
        direction_results = {
            name: asdict(two_dimensional_carrier_ritz(matrix, a, direction,
                                                      theta))
            for name, direction in raw_directions.items()
        }
        rows.append({
            "theta": theta,
            "full_q": full.value,
            "full_q_over_kappa": full.value / kappa,
            "geometric_ritz_dimension": int(geometric_basis.shape[1]),
            "geometric_ritz_q": geometric.value,
            "geometric_ritz_q_over_kappa": geometric.value / kappa,
            "two_dimensional": direction_results,
        })

    return {
        "scope": "floating low-dimensional actual-prime Ritz diagnostic",
        "height_T": float(height),
        "alpha": float(alpha),
        "L": data["L"],
        "selected_slice_dimension": data["dimension"],
        "jet_order": data["jet_order"],
        "kappa": kappa,
        "carrier_diagonal": float(np.vdot(a, matrix @ a).real),
        "lanczos_moments": lanczos_moments(matrix, a),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--heights", default="64,128,256,512")
    parser.add_argument("--alpha", type=float, default=0.4)
    parser.add_argument("--aperture-fraction", type=float, default=0.2)
    parser.add_argument("--jet-order", type=int)
    parser.add_argument("--theta", default="0.5,0.9")
    args = parser.parse_args()
    heights = [float(value) for value in args.heights.split(",")]
    theta_values = [float(value) for value in args.theta.split(",")]
    payload = [
        actual_fixture_ritz(
            height,
            alpha=args.alpha,
            aperture_fraction=args.aperture_fraction,
            jet_order=args.jet_order,
            theta_values=theta_values,
        )
        for height in heights
    ]
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
