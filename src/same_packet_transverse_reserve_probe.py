#!/usr/bin/env python3
"""Actual-coefficient finite Gabor probe for the two-channel reserve gate.

The candidate location is a probe point, not an asserted zeta zero.  The
matrix uses actual von Mangoldt coefficients and the same sharp-grid
completion as ``high_height_carrier_slice``.  Outputs are floating
diagnostics, not interval certificates or zero-free results.
"""

from __future__ import annotations

import argparse
import json
import math
from typing import Any, Iterable

import numpy as np
from scipy.linalg import null_space

from high_height_carrier_slice import (
    archimedean_matrix_sign,
    endpoint_null_basis,
    pole_matrix_sign,
    prime_matrix_sign,
    selected_rows_sign,
)
from same_packet_conditional_covariance_gate import (
    phase_optimized_two_channel_reserve,
)
from signed_garding_failfast import prime_powers


def _rayleigh(matrix: np.ndarray, vector: np.ndarray) -> float:
    return float(np.vdot(vector, matrix @ vector).real)


def _channel_row(
    name: str,
    eta: float,
    carrier: float,
    r: float,
    reserve: np.ndarray,
    e: np.ndarray,
    v: np.ndarray,
) -> dict[str, float | str]:
    c = _rayleigh(reserve, v)
    z = complex(np.vdot(e, reserve @ v))
    optimized, phase = phase_optimized_two_channel_reserve(eta, r, c, z)
    return {
        "channel": name,
        "c_over_K": c / carrier,
        "abs_z_over_K": abs(z) / carrier,
        "optimized_reserve_over_eta_K": optimized / (eta * carrier),
        "maximizing_phase": phase,
    }


def build_transverse_fixture(
    height: float,
    *,
    alpha: float = 0.4,
    aperture_fraction: float = 0.2,
    jet_order: int | None = None,
    eta: float = 0.5,
) -> dict[str, Any]:
    if height <= 4:
        raise ValueError("height must exceed four")
    if not 0 < eta < 1:
        raise ValueError("eta must lie strictly between zero and one")

    length = math.log(height)
    center = 1.5 * height
    spacing = 2.0 * math.pi / length
    half_count = int(math.floor(aperture_fraction * height / spacing))
    if half_count < 2:
        raise ValueError("aperture leaves too few critical-grid nodes")
    indices = np.arange(-half_count, half_count + 1, dtype=int)
    tau = center + spacing * indices
    if jet_order is None:
        jet_order = max(3, int(math.ceil(math.log(height))))
    if jet_order + 3 > indices.size:
        raise ValueError("fixture leaves no transverse selected-null channel")

    logs, weights = prime_powers(int(math.floor(math.exp(length) + 1e-10)))
    active = logs <= length + 1e-13
    logs = logs[active]
    weights = weights[active]

    arithmetic_raw = (
        archimedean_matrix_sign(tau, length)
        + pole_matrix_sign(tau, indices, length)
        - prime_matrix_sign(tau, length, logs, weights)
    )
    arithmetic_raw = (arithmetic_raw + arithmetic_raw.conj().T) / 2

    endpoint = endpoint_null_basis(indices, jet_order)
    selected_x, selected_y = selected_rows_sign(tau, center, length, alpha)
    x_endpoint = endpoint.T @ selected_x
    inclusion = endpoint @ null_space(x_endpoint[None, :], rcond=1e-12)
    if inclusion.shape[1] < 2:
        raise RuntimeError("selected-positive null space has no transverse channel")

    normalization = length * length
    projected_y = inclusion.T @ selected_y
    carrier = (2.0 / normalization) * np.outer(projected_y, projected_y)
    carrier_size = float(np.linalg.eigvalsh(carrier)[-1])
    if carrier_size <= 1e-14:
        raise RuntimeError("selected carrier was numerically deleted")
    e = projected_y.astype(complex) / np.linalg.norm(projected_y)

    arithmetic = inclusion.conj().T @ (arithmetic_raw / normalization) @ inclusion
    arithmetic = (arithmetic + arithmetic.conj().T) / 2
    reserve = arithmetic + carrier
    reserve = (reserve + reserve.conj().T) / 2
    r = _rayleigh(reserve, e)

    transverse_basis = null_space(e.conj()[None, :], rcond=1e-12)
    transverse = transverse_basis.conj().T @ reserve @ transverse_basis
    transverse = (transverse + transverse.conj().T) / 2
    eigenvalues, eigenvectors = np.linalg.eigh(transverse)

    schur_coordinates = transverse_basis.conj().T @ reserve @ e
    schur_residual = float(np.linalg.norm(schur_coordinates))
    channels: list[dict[str, float | str]] = []
    if schur_residual > 1e-14:
        v_cross = transverse_basis @ (schur_coordinates / schur_residual)
        channels.append(
            _channel_row(
                "conditional_schur_residual",
                eta,
                carrier_size,
                r,
                reserve,
                e,
                v_cross,
            )
        )

    v_positive = transverse_basis @ eigenvectors[:, -1]
    channels.append(
        _channel_row(
            "top_transverse_eigenvector",
            eta,
            carrier_size,
            r,
            reserve,
            e,
            v_positive,
        )
    )

    checks = {
        "endpoint_null_residual": float(
            np.linalg.norm(
                endpoint.conj().T @ endpoint - np.eye(endpoint.shape[1]),
                ord=2,
            )
        ),
        "selected_positive_null_residual": float(np.linalg.norm(selected_x @ inclusion)),
        "carrier_direction_residual": float(
            np.linalg.norm(carrier @ e - carrier_size * e)
        ),
        "transverse_orthogonality_residual": float(
            np.linalg.norm(e.conj() @ transverse_basis)
        ),
        "reserve_hermitian_residual": float(
            np.linalg.norm(reserve - reserve.conj().T, ord=2)
        ),
    }

    return {
        "scope": "floating actual-Lambda probe; candidate is not asserted to be a zero",
        "height_T": height,
        "candidate_gamma": center,
        "candidate_alpha": alpha,
        "candidate_is_asserted_zero": False,
        "L": length,
        "grid_dimension": int(indices.size),
        "selected_null_dimension": int(inclusion.shape[1]),
        "transverse_dimension": int(transverse_basis.shape[1]),
        "jet_order": int(jet_order),
        "active_prime_powers": int(logs.size),
        "eta": eta,
        "K_selected": carrier_size,
        "r_over_K": r / carrier_size,
        "conditional_schur_residual_over_K": schur_residual / carrier_size,
        "transverse_lambda_min_over_K": float(eigenvalues[0] / carrier_size),
        "transverse_lambda_max_over_K": float(eigenvalues[-1] / carrier_size),
        "channels": channels,
        "checks": checks,
    }


def run_sequence(heights: Iterable[float], **kwargs: Any) -> list[dict[str, Any]]:
    return [build_transverse_fixture(float(height), **kwargs) for height in heights]


def _parse_heights(value: str) -> list[float]:
    return [float(item) for item in value.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--heights", default="32,64,128,256")
    parser.add_argument("--alpha", type=float, default=0.4)
    parser.add_argument("--aperture-fraction", type=float, default=0.2)
    parser.add_argument("--jet-order", type=int)
    parser.add_argument("--eta", type=float, default=0.5)
    parser.add_argument("--output")
    args = parser.parse_args()
    payload = run_sequence(
        _parse_heights(args.heights),
        alpha=args.alpha,
        aperture_fraction=args.aperture_fraction,
        jet_order=args.jet_order,
        eta=args.eta,
    )
    encoded = json.dumps(payload, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(encoded + "\n")
    else:
        print(encoded)


if __name__ == "__main__":
    main()
