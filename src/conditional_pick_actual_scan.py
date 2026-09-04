"""Actual completed-matrix scan for the anchored conditional-Pick companion.

This executes the theorem in
``results/ZETA23-PRIME-INDEPENDENT-CONDITIONAL-PICK-COMPANION-2026-08-12.md``
on the finite sharp-grid fixtures.  All matrix signs are ordinary floating
diagnostics; rigorous scalar replay is handled separately with Arb.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from typing import Any, Iterable, Sequence

import numpy as np
from numpy.polynomial.legendre import legvander
from scipy.linalg import null_space

from conditional_pick_companion import (
    anchored_companion,
    phase_optimized_boundary,
)
from high_height_carrier_slice import (
    archimedean_matrix_sign,
    endpoint_null_basis,
    rational_pole_matrix_sign,
)
from subfull_direct_q_failfast import (
    FloatingBase,
    _exact_endpoint_kernel,
    build_floating_base,
    selected_rows_with_phase,
)


@dataclass(frozen=True)
class ConditionalPickGeometry:
    inclusion: np.ndarray
    carrier: np.ndarray
    anchor: np.ndarray
    confluent: np.ndarray
    kappa: float
    theta_star: float


def endpoint_boundary_anchor(
    indices: np.ndarray,
    tau: np.ndarray,
    endpoint: np.ndarray,
    jet_order: int,
) -> np.ndarray:
    """Return the inherited Jacobi boundary vector in endpoint coordinates."""

    if jet_order <= 0:
        raise ValueError("a positive jet order is required for the boundary anchor")
    scale = max(1.0, float(np.max(np.abs(indices))))
    nodes = indices.astype(float) / scale
    polynomial_columns = legvander(nodes, jet_order - 1)
    discarded, _ = np.linalg.qr(polynomial_columns, mode="reduced")
    q_last = discarded[:, jet_order - 1]
    raw = endpoint.conj().T @ (tau * q_last)
    norm = float(np.linalg.norm(raw))
    if norm <= 1.0e-12:
        raise ValueError("endpoint boundary vector is negligible")
    return raw / norm


def selected_depth_derivative(
    tau: np.ndarray,
    length: float,
    gamma: float,
    alpha: float,
    grid_phase: float,
) -> np.ndarray:
    """Derivative in alpha of the selected imaginary row."""

    z = gamma - 1j * alpha
    argument = length * (z - gamma) / 2.0 - math.pi * grid_phase
    common = 2.0 * np.sin(argument)
    derivative_z = (
        length * np.cos(argument) * (z - tau) - common
    ) / (z - tau) ** 2
    return np.imag(-1j * derivative_z)


def build_geometry(
    base: FloatingBase,
    *,
    alpha: float,
    jet_order: int,
) -> ConditionalPickGeometry:
    """Build the carrier, inherited anchor, and confluent tie-breaker."""

    endpoint = endpoint_null_basis(base.indices, jet_order)
    selected_x, selected_y = selected_rows_with_phase(
        base.tau, base.length, base.gamma, alpha, base.grid_phase
    )
    selected_null = null_space(
        (endpoint.T @ selected_x)[None, :], rcond=1.0e-12
    )
    inclusion = endpoint @ selected_null
    if inclusion.shape[1] < 3:
        raise ValueError("selected quotient has dimension below three")

    projected_y = inclusion.conj().T @ selected_y
    carrier_norm = float(np.linalg.norm(projected_y))
    if carrier_norm <= 1.0e-12:
        raise ValueError("carrier is negligible")
    carrier = projected_y / carrier_norm
    kappa = 2.0 * carrier_norm**2 / base.length**2

    endpoint_anchor = endpoint_boundary_anchor(
        base.indices, base.tau, endpoint, jet_order
    )
    projected_anchor = selected_null.conj().T @ endpoint_anchor
    anchor_norm = float(np.linalg.norm(projected_anchor))
    if anchor_norm <= 1.0e-12:
        raise ValueError("inherited anchor vanishes after selected projection")
    anchor = projected_anchor / anchor_norm

    derivative = selected_depth_derivative(
        base.tau,
        base.length,
        base.gamma,
        alpha,
        base.grid_phase,
    )
    confluent = inclusion.conj().T @ derivative
    theta_limit = 1.0 - abs(np.vdot(carrier, anchor)) ** 2
    theta_limit = min(1.0, max(0.0, float(theta_limit.real)))
    return ConditionalPickGeometry(
        inclusion=inclusion,
        carrier=carrier,
        anchor=anchor,
        confluent=confluent,
        kappa=kappa,
        theta_star=theta_limit,
    )


def _orthogonal_complement(vector: np.ndarray) -> np.ndarray:
    row = np.asarray(vector, dtype=complex).conj()[None, :]
    return null_space(row, rcond=1.0e-12)


def evaluate_actual_conditional_pick(
    base: FloatingBase,
    *,
    alpha: float,
    jet_order: int,
    theta: float,
) -> dict[str, Any]:
    """Evaluate the strong anchored law and its minimal one-square version."""

    geometry = build_geometry(base, alpha=alpha, jet_order=jet_order)
    if theta > geometry.theta_star + 1.0e-12:
        raise ValueError("theta exceeds inherited-anchor geometry")

    inclusion = geometry.inclusion
    arithmetic = inclusion.conj().T @ base.arithmetic @ inclusion
    arithmetic = (arithmetic + arithmetic.conj().T) / 2.0
    background_raw = (
        archimedean_matrix_sign(base.tau, base.length)
        + rational_pole_matrix_sign(base.tau, base.length)
    ) / base.length**2
    background = inclusion.conj().T @ background_raw @ inclusion
    background = (background + background.conj().T) / 2.0
    shift = 2.0 * math.pi / base.length
    shifted = arithmetic + shift * np.eye(arithmetic.shape[0])
    background_shifted = background + shift * np.eye(background.shape[0])
    centered = arithmetic - background

    result = anchored_companion(
        geometry.carrier,
        geometry.anchor,
        theta,
        tie_breaker=geometry.confluent,
    )
    state = result.boundary_state
    g_perp = _orthogonal_complement(geometry.anchor)
    anchored_matrix = g_perp.conj().T @ shifted @ g_perp
    anchored_values = np.linalg.eigvalsh(
        (anchored_matrix + anchored_matrix.conj().T) / 2.0
    )

    one_square = float(np.vdot(state, shifted @ state).real)
    background_budget = float(
        np.vdot(state, background_shifted @ state).real
    )
    centered_value = float(np.vdot(state, centered @ state).real)
    unshifted_value = one_square - shift
    boundary = phase_optimized_boundary(
        arithmetic, geometry.carrier, result.companion, theta
    )
    return {
        "height_T": base.height,
        "gamma_fraction": base.gamma_fraction,
        "grid_phase": base.grid_phase,
        "aperture_fraction": base.aperture_fraction,
        "jet_order": int(jet_order),
        "alpha": float(alpha),
        "theta": float(theta),
        "dimension": int(arithmetic.shape[0]),
        "kappa": geometry.kappa,
        "theta_star": geometry.theta_star,
        "anchor_projection_norm": float(
            np.linalg.norm(
                endpoint_null_basis(base.indices, jet_order)
                @ endpoint_boundary_anchor(
                    base.indices,
                    base.tau,
                    endpoint_null_basis(base.indices, jet_order),
                    jet_order,
                )
            )
        ),
        "anchor_residual": result.anchor_residual,
        "plus_one_shift": shift,
        "anchored_cpd_min": float(anchored_values[0]),
        "anchored_cpd_min_over_kappa": float(anchored_values[0] / geometry.kappa),
        "anchored_cpd_negative_eigenvalues": int(np.sum(anchored_values < -1.0e-10)),
        "one_square_shifted": one_square,
        "one_square_shifted_over_kappa": one_square / geometry.kappa,
        "one_square_unshifted": unshifted_value,
        "one_square_unshifted_over_kappa": unshifted_value / geometry.kappa,
        "phase_optimized_boundary": boundary,
        "phase_optimized_boundary_over_kappa": boundary / geometry.kappa,
        "herglotz_background_budget": background_budget,
        "centered_arithmetic_value": centered_value,
        "budget_plus_centered_residual": (
            background_budget + centered_value - one_square
        ),
    }


def scan_actual_conditional_pick(
    *,
    heights: Sequence[float],
    gamma_fractions: Sequence[float],
    grid_phases: Sequence[float],
    aperture_fractions: Sequence[float],
    jet_orders: Sequence[int],
    alphas: Sequence[float],
    theta_fractions: Iterable[float] = (0.5, 0.9, 1.0),
) -> dict[str, Any]:
    """Scan theta as a fraction of each geometry's exact ``theta_star``."""

    rows: list[dict[str, Any]] = []
    skipped = 0
    for height in heights:
        for gamma_fraction in gamma_fractions:
            for aperture in aperture_fractions:
                for phase in grid_phases:
                    try:
                        base = build_floating_base(
                            float(height),
                            gamma_fraction=float(gamma_fraction),
                            aperture_fraction=float(aperture),
                            grid_phase=float(phase),
                        )
                    except ValueError:
                        skipped += 1
                        continue
                    for jet_order in jet_orders:
                        for alpha in alphas:
                            try:
                                geometry = build_geometry(
                                    base, alpha=float(alpha), jet_order=int(jet_order)
                                )
                            except ValueError:
                                skipped += 1
                                continue
                            for fraction in theta_fractions:
                                theta = float(fraction) * geometry.theta_star
                                if theta <= 1.0e-10:
                                    skipped += 1
                                    continue
                                try:
                                    rows.append(evaluate_actual_conditional_pick(
                                        base,
                                        alpha=float(alpha),
                                        jet_order=int(jet_order),
                                        theta=theta,
                                    ))
                                except ValueError:
                                    skipped += 1
    if not rows:
        raise ValueError("scan produced no valid rows")
    return {
        "scope": "floating actual completed anchored-Pick scan",
        "row_count": len(rows),
        "skipped_count": skipped,
        "strong_anchored_cpd_pass_count": sum(
            row["anchored_cpd_min"] >= -1.0e-10 for row in rows
        ),
        "one_square_shifted_pass_count": sum(
            row["one_square_shifted"] >= -1.0e-10 for row in rows
        ),
        "minimum_theta_star": min(rows, key=lambda row: row["theta_star"]),
        "minimum_anchored_cpd_over_kappa": min(
            rows, key=lambda row: row["anchored_cpd_min_over_kappa"]
        ),
        "minimum_one_square_over_kappa": min(
            rows, key=lambda row: row["one_square_shifted_over_kappa"]
        ),
        "minimum_unshifted_one_square_over_kappa": min(
            rows, key=lambda row: row["one_square_unshifted_over_kappa"]
        ),
        "rows": rows,
    }


def rationalized_boundary_coordinates(
    base: FloatingBase,
    *,
    alpha: float,
    jet_order: int,
    theta: float,
    max_denominator: int = 10**9,
) -> dict[str, Any]:
    """Approximate the boundary--confluent state in the rigorous RREF basis."""

    geometry = build_geometry(base, alpha=alpha, jet_order=jet_order)
    result = anchored_companion(
        geometry.carrier,
        geometry.anchor,
        theta,
        tie_breaker=geometry.confluent,
    )
    physical_state = geometry.inclusion @ result.boundary_state

    endpoint_exact = _exact_endpoint_kernel(
        [int(value) for value in base.indices], jet_order
    )
    endpoint = np.array([
        [float(endpoint_exact[i, j]) for j in range(endpoint_exact.ncols())]
        for i in range(endpoint_exact.nrows())
    ])
    selected_x, _ = selected_rows_with_phase(
        base.tau, base.length, base.gamma, alpha, base.grid_phase
    )
    row = selected_x @ endpoint
    pivot = int(np.argmax(np.abs(row)))
    free = [column for column in range(endpoint.shape[1]) if column != pivot]
    elimination = np.zeros((endpoint.shape[1], len(free)), dtype=float)
    for output, column in enumerate(free):
        elimination[column, output] = 1.0
        elimination[pivot, output] = -row[column] / row[pivot]
    basis = endpoint @ elimination
    coordinates, *_ = np.linalg.lstsq(basis, physical_state, rcond=None)
    residual = float(np.linalg.norm(basis @ coordinates - physical_state))
    rational = [
        (
            Fraction(float(value.real)).limit_denominator(max_denominator),
            Fraction(float(value.imag)).limit_denominator(max_denominator),
        )
        for value in coordinates
    ]
    rational_complex = np.array([
        complex(float(real), float(imaginary)) for real, imaginary in rational
    ])
    rational_residual = float(
        np.linalg.norm(basis @ rational_complex - physical_state)
    )
    return {
        "coefficients": rational,
        "pivot": pivot,
        "floating_basis_residual": residual,
        "rationalized_physical_residual": rational_residual,
        "anchor_residual": result.anchor_residual,
        "theta_star": geometry.theta_star,
    }
