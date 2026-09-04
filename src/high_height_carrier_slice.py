"""Actual-coefficient high-height sharp-Gabor carrier-slice fixture.

The arithmetic matrix is assembled without zeta-zero input as

    K_ar = (K_arch + K_pole - K_prime) / L^2

on a critical sharp Fourier grid.  Endpoint jets are imposed by the moment
nullspace W_m.  A *candidate* reflected pair, not asserted to be a zeta zero,
supplies the selected positive row x and negative row y.  The tested space is

    S_sel = W_m intersect ker(x^*),
    N = (2/L^2) (P_S y)(P_S y)^*.

No positive rows from unknown collateral zeros are used.  The primary
diagnostic is the direct constrained arithmetic edge q_eta(K_ar); the
target-subtracted support h_eta(K_ar - K_0) is emitted only to display its
known aligned-baseline contamination.

All prime powers up to X=exp(L) have their actual von Mangoldt weights.  The
archimedean sharp matrix uses closed digamma/trigamma formulas plus an
exponentially convergent tail, and the pole matrix is rank two.  Computations
are floating diagnostics, not interval certificates or zero-free results.
"""
from __future__ import annotations

import argparse
import json
import math
from typing import Any, Dict, Iterable

import numpy as np
from numpy.polynomial.legendre import legvander
from scipy.linalg import null_space
from scipy.special import digamma

from carrier_slice_support import carrier_slice_support
from signed_garding_failfast import prime_powers


def complex_trigamma(z: np.ndarray | complex) -> np.ndarray:
    """Complex trigamma by recurrence and a seven-term asymptotic series."""
    zz = np.asarray(z, dtype=complex)
    recurrence = np.zeros_like(zz)
    for shift in range(14):
        recurrence += 1.0 / (zz + shift) ** 2
    w = zz + 14.0
    answer = 1.0 / w + 1.0 / (2.0 * w * w)
    bernoulli = (1 / 6, -1 / 30, 1 / 42, -1 / 30,
                 5 / 66, -691 / 2730, 7 / 6)
    for index, value in enumerate(bernoulli, start=1):
        answer += value / w ** (2 * index + 1)
    return answer + recurrence


def archimedean_matrix_sign(tau: np.ndarray, length: float) -> np.ndarray:
    """Sign-conjugated sharp matrix of Re psi(1/4+it/2)-log(pi).

    The physical archimedean form has multiplier
    ``Re psi(1/4+it/2)-log(pi)`` with Fourier measure ``dt/(2*pi)``.
    Critical spacing turns its off-diagonal entries into divided differences
    of the truncated sine transform of
    ``exp(-u/2)/(1-exp(-2u))``.  The displayed tail sums restore the exact
    finite-support truncation.
    """
    tau = np.asarray(tau, dtype=float)
    if length <= 0:
        raise ValueError("length must be positive")
    # exp(-(2n+1/2)L) is the only tail scale.  Keep terms until they are far
    # below double precision; at the smallest default L this needs < 12 terms.
    tail_rates: list[float] = []
    index = 0
    while True:
        rate = 2.0 * index + 0.5
        tail_rates.append(rate)
        if math.exp(-rate * length) < 1e-18:
            break
        index += 1
        if index > 10000:
            raise RuntimeError("archimedean tail did not converge")
    rates = np.asarray(tail_rates)[:, None]
    phases = np.exp((-rates + 1j * tau[None, :]) * length)
    denominators = rates - 1j * tau[None, :]

    z = 0.25 + 0.5j * tau
    sine_transform = (
        0.5 * np.imag(digamma(z))
        - np.sum(np.imag(phases / denominators), axis=0)
    )

    delta = tau[:, None] - tau[None, :]
    numerator = sine_transform[:, None] - sine_transform[None, :]
    answer = np.zeros((tau.size, tau.size), dtype=float)
    off_diagonal = ~np.eye(tau.size, dtype=bool)
    answer[off_diagonal] = (
        2.0 * numerator[off_diagonal] / delta[off_diagonal]
    )

    diagonal = (
        length * (np.real(digamma(z)) - math.log(math.pi))
        + 0.5 * np.real(complex_trigamma(z))
        - 2.0 * np.sum(
            np.real(phases / denominators ** 2), axis=0
        )
    )
    np.fill_diagonal(answer, diagonal)
    return (answer + answer.T) / 2.0


def shift_overlap_sign(
    tau: np.ndarray, length: float, shift: float
) -> np.ndarray:
    """Hermitian real-correlation matrix at one positive physical shift."""
    if shift < 0 or shift > length + 1e-12:
        raise ValueError("shift must lie in [0,length]")
    tau = np.asarray(tau, dtype=float)
    delta = tau[:, None] - tau[None, :]
    sine = np.sin(tau * shift)
    numerator = sine[None, :] - sine[:, None]
    answer = np.zeros((tau.size, tau.size), dtype=float)
    off_diagonal = ~np.eye(tau.size, dtype=bool)
    answer[off_diagonal] = (
        numerator[off_diagonal] / delta[off_diagonal]
    )
    np.fill_diagonal(answer, (length - shift) * np.cos(tau * shift))
    return (answer + answer.T) / 2.0


def laplace_row_sign(
    tau: np.ndarray, indices: np.ndarray, length: float, exponent: float
) -> np.ndarray:
    """Endpoint-sign-conjugated row integral of exp((exponent-itau)t)."""
    rate = exponent - 1j * tau
    raw = 2.0 * np.sinh(rate * length / 2.0) / rate
    signs = np.where(indices % 2 == 0, 1.0, -1.0)
    return signs * raw


def pole_matrix_sign(
    tau: np.ndarray, indices: np.ndarray, length: float
) -> np.ndarray:
    plus = laplace_row_sign(tau, indices, length, 0.5)
    minus = laplace_row_sign(tau, indices, length, -0.5)
    answer = (
        np.outer(np.conj(minus), plus)
        + np.outer(np.conj(plus), minus)
    )
    return (answer + answer.conj().T) / 2.0


def rational_pole_matrix_sign(tau: np.ndarray, length: float) -> np.ndarray:
    """Sharp matrix of ``1/(2*pi*(1/4+t^2))`` in closed form."""
    tau = np.asarray(tau, dtype=float)
    rate = 0.5 - 1j * tau
    exponential = np.exp(-rate * length)
    integral0 = -np.expm1(-rate * length) / rate
    integral1 = (1.0 - exponential * (1.0 + rate * length)) / (rate * rate)
    sine_transform = np.imag(integral0)

    delta = tau[:, None] - tau[None, :]
    numerator = sine_transform[None, :] - sine_transform[:, None]
    answer = np.zeros((tau.size, tau.size), dtype=float)
    off_diagonal = ~np.eye(tau.size, dtype=bool)
    answer[off_diagonal] = (
        2.0 * numerator[off_diagonal] / delta[off_diagonal]
    )
    diagonal = 2.0 * np.real(length * integral0 - integral1)
    np.fill_diagonal(answer, diagonal)
    return (answer + answer.T) / 2.0


def prime_matrix_sign(
    tau: np.ndarray,
    length: float,
    logs: np.ndarray,
    weights: np.ndarray,
) -> np.ndarray:
    """Positive Prime(f) matrix; the completed form subtracts it."""
    answer = np.zeros((tau.size, tau.size), dtype=float)
    for shift, weight in zip(logs, weights):
        if shift < length + 1e-13:
            answer += 2.0 * weight * shift_overlap_sign(tau, length, float(shift))
    return (answer + answer.T) / 2.0


def centered_matrix_actual(
    tau: np.ndarray,
    length: float,
    logs: np.ndarray,
    weights: np.ndarray,
) -> np.ndarray:
    """Exact centered H_E from actual A and D scalar data."""
    phases = np.exp(1j * tau[:, None] * logs[None, :])
    zeta_polynomial = phases @ weights
    s = 0.5 + 1j * tau
    continuum = np.expm1(s * length) / s
    centered = zeta_polynomial - continuum
    a_values = np.imag(centered)

    prime_d = np.cos(tau[:, None] * logs[None, :]) @ (
        weights * (length - logs)
    )
    continuum_d = np.real(
        (np.expm1(s * length) - s * length) / (s * s)
    )
    d_values = prime_d - continuum_d

    delta = tau[:, None] - tau[None, :]
    numerator = a_values[:, None] - a_values[None, :]
    answer = np.zeros((tau.size, tau.size), dtype=float)
    off_diagonal = ~np.eye(tau.size, dtype=bool)
    answer[off_diagonal] = (
        2.0 * numerator[off_diagonal] / delta[off_diagonal]
    )
    np.fill_diagonal(answer, -2.0 * d_values)
    return (answer + answer.T) / 2.0


def endpoint_null_basis(indices: np.ndarray, jet_order: int) -> np.ndarray:
    """Orthonormal basis for the first ``jet_order`` moment nulls."""
    if jet_order < 0 or jet_order >= indices.size:
        raise ValueError("jet_order must lie between 0 and dimension-1")
    if jet_order == 0:
        return np.eye(indices.size)
    scale = max(1.0, float(np.max(np.abs(indices))))
    nodes = indices.astype(float) / scale
    moments = legvander(nodes, jet_order - 1).T
    basis = null_space(moments, rcond=1e-12)
    if basis.shape[1] != indices.size - jet_order:
        raise RuntimeError("endpoint moment matrix lost rank")
    return basis


def selected_rows_sign(
    tau: np.ndarray, center: float, length: float, alpha: float
) -> tuple[np.ndarray, np.ndarray]:
    """Raw real/imaginary selected-pair rows in sign-conjugated coordinates."""
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    z = center - 1j * alpha
    common = 2.0 * np.sin(length * (z - center) / 2.0)
    values = common / (z - tau)
    return np.real(values), np.imag(values)


def _matrix_extrema(matrix: np.ndarray) -> tuple[float, float]:
    values = np.linalg.eigvalsh((matrix + matrix.conj().T) / 2.0)
    return float(values[0]), float(values[-1])


def build_fixture(
    height: float,
    *,
    alpha: float = 0.4,
    aperture_fraction: float = 0.2,
    jet_order: int | None = None,
) -> Dict[str, Any]:
    """Build one zero-independent actual-coefficient high-height fixture."""
    if height <= 4:
        raise ValueError("height must exceed 4")
    length = math.log(height)
    x_cutoff = int(math.floor(math.exp(length) + 1e-10))
    center = 1.5 * height
    spacing = 2.0 * math.pi / length
    half_count = int(math.floor(aperture_fraction * height / spacing))
    if half_count < 2:
        raise ValueError("aperture leaves too few critical-grid nodes")
    indices = np.arange(-half_count, half_count + 1, dtype=int)
    tau = center + spacing * indices
    if tau[0] < height or tau[-1] > 2.0 * height:
        raise RuntimeError("critical grid left the requested dyadic band")
    dimension = indices.size
    if jet_order is None:
        jet_order = max(3, int(math.ceil(math.log(height))))
    if jet_order + 2 > dimension:
        raise ValueError("endpoint and selected rows leave no carrier space")

    all_logs, all_weights = prime_powers(x_cutoff)
    active = all_logs <= length + 1e-13
    logs = all_logs[active]
    weights = all_weights[active]

    arch = archimedean_matrix_sign(tau, length)
    pole = pole_matrix_sign(tau, indices, length)
    prime = prime_matrix_sign(tau, length, logs, weights)
    arithmetic_raw = arch + pole - prime
    arithmetic_raw = (arithmetic_raw + arithmetic_raw.conj().T) / 2.0

    # Independent completion check: H_ar = H_E + H_mu + H_0.  H_E is built
    # from the centered actual A,D data, while H_0 is built directly from the
    # Fourier transform of the positive rational density.
    centered = centered_matrix_actual(tau, length, logs, weights)
    rational = rational_pole_matrix_sign(tau, length)
    background = arch + rational
    completion_residual = float(
        np.linalg.norm(arithmetic_raw - (centered + background), ord=2)
    )

    endpoint = endpoint_null_basis(indices, jet_order)
    selected_x, selected_y = selected_rows_sign(tau, center, length, alpha)
    x_endpoint = endpoint.T @ selected_x
    selected_null = null_space(x_endpoint[None, :], rcond=1e-12)
    inclusion = endpoint @ selected_null
    if inclusion.shape[1] == 0:
        raise RuntimeError("selected positive row deleted the whole endpoint space")
    projected_y = inclusion.T @ selected_y

    normalization = length * length
    carrier = (2.0 / normalization) * np.outer(projected_y, projected_y)
    kappa = float(2.0 * np.vdot(projected_y, projected_y).real / normalization)
    if kappa <= 1e-14:
        raise RuntimeError("selected carrier was numerically deleted")
    carrier_direction = projected_y / np.linalg.norm(projected_y)

    selected_full = (2.0 / normalization) * (
        np.outer(selected_x, selected_x) - np.outer(selected_y, selected_y)
    )
    selected_slice = inclusion.T @ selected_full @ inclusion
    selected_identity_error = float(
        np.linalg.norm(selected_slice + carrier, ord=2)
    )

    arithmetic = arithmetic_raw / normalization
    arithmetic_slice = inclusion.conj().T @ arithmetic @ inclusion
    arithmetic_slice = (arithmetic_slice + arithmetic_slice.conj().T) / 2.0
    target_subtracted = arithmetic_slice + carrier

    components = {
        "arch": inclusion.conj().T @ (arch / normalization) @ inclusion,
        "pole": inclusion.conj().T @ (pole / normalization) @ inclusion,
        "minus_prime": inclusion.conj().T @ (-prime / normalization) @ inclusion,
        "centered": inclusion.conj().T @ (centered / normalization) @ inclusion,
        "background": inclusion.conj().T @ (background / normalization) @ inclusion,
    }
    top_component_values = {
        name: float(np.vdot(carrier_direction, matrix @ carrier_direction).real)
        for name, matrix in components.items()
    }

    fractions = (0.5, 0.9, 1.0)
    slice_rows: list[dict[str, float]] = []
    baseline_lower_margins: list[float] = []
    baseline_upper_margins: list[float] = []
    for fraction in fractions:
        eta = fraction * kappa
        direct = carrier_slice_support(
            arithmetic_slice, carrier, eta, iterations=64
        )
        subtracted = carrier_slice_support(
            target_subtracted, carrier, eta, iterations=64
        )
        slice_rows.append({
            "theta": fraction,
            "eta": eta,
            "q_eta_direct_arithmetic": direct.value,
            "q_eta_over_kappa": direct.value / kappa,
            "h_eta_target_subtracted": subtracted.value,
            "h_eta_over_kappa": subtracted.value / kappa,
            "baseline_gap_h_minus_q": subtracted.value - direct.value,
        })
        # For R_full=K_ar+N, the exact baseline theorem gives
        # q_eta+eta <= h_eta <= q_eta+kappa.
        baseline_lower_margins.append(
            subtracted.value - direct.value - eta
        )
        baseline_upper_margins.append(
            direct.value + kappa - subtracted.value
        )

    full_carrier_arithmetic = float(
        np.vdot(carrier_direction, arithmetic_slice @ carrier_direction).real
    )
    full_carrier_row = slice_rows[-1]

    endpoint_nodes = indices.astype(float) / max(1.0, float(half_count))
    endpoint_moments = legvander(endpoint_nodes, jet_order - 1).T
    endpoint_error = float(np.linalg.norm(endpoint_moments @ endpoint, ord=2))
    selected_null_error = float(np.linalg.norm(selected_x @ inclusion))
    rational_min, rational_max = _matrix_extrema(rational / normalization)
    arithmetic_min, arithmetic_max = _matrix_extrema(arithmetic_slice)
    background_min, background_max = _matrix_extrema(background / normalization)

    infinite_carrier = math.sinh(alpha * length) / (alpha * length) - 1.0
    return {
        "scope": "floating target-conditioned, zero-independent arithmetic fixture",
        "height_T": height,
        "X_exp_L": math.exp(length),
        "L": length,
        "candidate_gamma": center,
        "candidate_alpha": alpha,
        "candidate_is_asserted_zero": False,
        "grid_dimension": int(dimension),
        "grid_tau_min": float(tau[0]),
        "grid_tau_max": float(tau[-1]),
        "jet_order": int(jet_order),
        "endpoint_dimension": int(endpoint.shape[1]),
        "selected_slice_dimension": int(inclusion.shape[1]),
        "active_prime_powers": int(logs.size),
        "actual_von_mangoldt_mass": float(np.sum(weights)),
        "kappa_selected": kappa,
        "kappa_infinite_sharp_lattice": infinite_carrier,
        "carrier_retention_ratio": kappa / infinite_carrier,
        "arithmetic_slice_lambda_min": arithmetic_min,
        "arithmetic_slice_lambda_max": arithmetic_max,
        "rational_matrix_lambda_min": rational_min,
        "rational_matrix_lambda_max": rational_max,
        "background_lambda_min": background_min,
        "background_lambda_max": background_max,
        "top_carrier_components": top_component_values,
        "q_and_baseline_diagnostics": slice_rows,
        "checks": {
            "endpoint_moment_residual": endpoint_error,
            "selected_positive_row_residual": selected_null_error,
            "selected_pair_equals_minus_N_residual": selected_identity_error,
            "completed_centered_decomposition_residual": completion_residual,
            "carrier_lambda_max_residual": abs(
                float(np.linalg.eigvalsh(carrier)[-1]) - kappa
            ),
            "full_carrier_q_identity_residual": abs(
                full_carrier_row["q_eta_direct_arithmetic"]
                - full_carrier_arithmetic
            ),
            "full_carrier_baseline_identity_residual": abs(
                full_carrier_row["h_eta_target_subtracted"]
                - full_carrier_row["q_eta_direct_arithmetic"]
                - kappa
            ),
            "baseline_sandwich_min_lower_margin": min(
                baseline_lower_margins
            ),
            "baseline_sandwich_min_upper_margin": min(
                baseline_upper_margins
            ),
        },
    }


def run_sequence(heights: Iterable[float], **kwargs: Any) -> list[Dict[str, Any]]:
    return [build_fixture(float(height), **kwargs) for height in heights]


def _parse_heights(value: str) -> list[float]:
    return [float(item) for item in value.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--heights", default="32,64,128,256,512")
    parser.add_argument("--alpha", type=float, default=0.4)
    parser.add_argument("--aperture-fraction", type=float, default=0.2)
    parser.add_argument("--jet-order", type=int)
    args = parser.parse_args()
    payload = run_sequence(
        _parse_heights(args.heights),
        alpha=args.alpha,
        aperture_fraction=args.aperture_fraction,
        jet_order=args.jet_order,
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
