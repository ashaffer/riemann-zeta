"""Finite actual-node laboratory for calibrated leverage and negative skew.

For a calibrated residual ``v=a(t0)+D*1`` and a fixed compactly supported
time law, this module studies the scale-invariant quantity

    J_v(y) = L_v(y) * (1 + Gamma_-(y)),

where

    L_v(y) = [-y.v]_+ / sqrt(Var(F_y)),
    Gamma_-(y) = max(0, -E[Z_y**3] / Var(F_y)**(3/2)).

The time law is an explicit compact B-spline probability supported in
``[B/3, 2B/3]``.  Its characteristic function is closed form, so means,
covariances, and third moments are continuum quantities rather than sampled
time-grid moments.  The nonlinear maximization and all cosine arithmetic are
floating point.  Reported maxima are candidate lower bounds for ``sup_y J``;
they are diagnostics, not theorem certificates.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import math
from typing import Any

import numpy as np
from qp_radialization_lab import (
    directional_interval_scan,
    prime_powers_in_shell,
    primes_up_to,
    primes_in_shell,
)
from qp_transverse_sharpness_lab import first_odd_resonance


FULL_APERTURE = 50.0 / 33.0


def _sinc(value: np.ndarray | float) -> np.ndarray:
    """Return ``sin(value)/value`` with a stable value at zero."""

    values = np.asarray(value, dtype=float)
    return np.sinc(values / np.pi)


def spline_cosine_transform(
    frequency: np.ndarray | float, bandwidth: float, order: int = 8
) -> np.ndarray:
    """Cosine transform of the compact B-spline time probability.

    The random time is

        B/2 + U_1 + ... + U_order,

    with independent ``U_j`` uniform on
    ``[-B/(6*order), B/(6*order)]``.  Hence its support is exactly
    ``[B/3, 2B/3]``.
    """

    if bandwidth <= 0.0:
        raise ValueError("bandwidth must be positive")
    if order < 1:
        raise ValueError("order must be positive")
    omega = np.asarray(frequency, dtype=float)
    phase = 0.5 * bandwidth * omega
    local = bandwidth * omega / (6.0 * order)
    return np.cos(phase) * _sinc(local) ** order


@dataclass(frozen=True)
class ContinuumMomentModel:
    nodes: np.ndarray
    bandwidth: float
    spline_order: int
    mean: np.ndarray
    covariance: np.ndarray
    third_central: np.ndarray
    minimum_eigenvalue: float
    maximum_eigenvalue: float
    retained_rank: int
    symmetry_error: float


def continuum_moment_model(
    nodes: np.ndarray,
    bandwidth: float,
    *,
    spline_order: int = 8,
    eigenvalue_tolerance: float = 1.0e-12,
) -> ContinuumMomentModel:
    """Build exact-transform first, second, and third cosine moments."""

    u = np.asarray(nodes, dtype=float)
    if u.ndim != 1 or len(u) == 0 or np.any(u <= 0.0):
        raise ValueError("nodes must be a nonempty vector of positive values")

    transform = lambda omega: spline_cosine_transform(omega, bandwidth, spline_order)
    mean = transform(u)
    raw_second = 0.5 * (
        transform(u[:, None] - u[None, :])
        + transform(u[:, None] + u[None, :])
    )
    covariance = raw_second - np.outer(mean, mean)
    covariance = 0.5 * (covariance + covariance.T)

    count = len(u)
    third = np.empty((count, count, count), dtype=float)
    uj = u[:, None]
    uk = u[None, :]
    mean_outer = mean[:, None] * mean[None, :]
    for index, ui in enumerate(u):
        raw_third = 0.25 * (
            transform(ui + uj + uk)
            + transform(ui + uj - uk)
            + transform(ui - uj + uk)
            + transform(-ui + uj + uk)
        )
        centered = raw_third - mean[index] * raw_second
        centered -= mean[:, None] * raw_second[index, :][None, :]
        centered -= raw_second[index, :][:, None] * mean[None, :]
        centered += 2.0 * mean[index] * mean_outer
        third[index] = centered

    # Average the six permutations.  Analytically they agree; this removes
    # only floating evaluation asymmetry before nonlinear optimization.
    permutations = (
        third,
        third.transpose(0, 2, 1),
        third.transpose(1, 0, 2),
        third.transpose(1, 2, 0),
        third.transpose(2, 0, 1),
        third.transpose(2, 1, 0),
    )
    symmetry_error = max(float(np.max(np.abs(third - item))) for item in permutations)
    third = sum(permutations) / 6.0

    eigenvalues = np.linalg.eigvalsh(covariance)
    maximum = float(eigenvalues[-1])
    threshold = eigenvalue_tolerance * maximum
    retained = int(np.sum(eigenvalues > threshold))
    if retained == 0:
        raise np.linalg.LinAlgError("the continuum covariance has no retained range")
    return ContinuumMomentModel(
        nodes=u,
        bandwidth=float(bandwidth),
        spline_order=spline_order,
        mean=mean,
        covariance=covariance,
        third_central=third,
        minimum_eigenvalue=float(eigenvalues[-retained]),
        maximum_eigenvalue=maximum,
        retained_rank=retained,
        symmetry_error=symmetry_error,
    )


@dataclass(frozen=True)
class JointInvariantCandidate:
    value: float
    leverage: float
    negative_skew: float
    standardized_third: float
    variance: float
    residual_pairing: float
    leverage_upper: float
    crude_global_upper_guard: float
    projected_gradient_relative: float
    optimizer_success: bool
    optimizer_message: str
    starts: int
    coefficients: np.ndarray
    whitened_vector: np.ndarray


@dataclass(frozen=True)
class CubicSpectralDiagnostic:
    """Floating lower/upper bracket for the whitened signed cubic norm."""

    negative_skew_candidate: float
    matricization_upper: float
    relative_stationarity_residual: float
    converged: bool
    starts: int
    whitened_vector: np.ndarray
    coefficients: np.ndarray


@dataclass(frozen=True)
class ShortRightWindowSkewDiagnostic:
    """Exact-transform skew of the proposed short right-prime packet."""

    N: int
    Y: float
    bandwidth: float
    window_length: float
    prime_count: int
    variance: float
    central_third: float
    negative_skew: float
    absolute_standardized_third: float
    packet_scale_quarter_power: float
    half_integer_transform_epsilon: float
    covariance_lower_bound: float
    rigorous_absolute_skew_upper: float


def _third_contraction(tensor: np.ndarray, vector: np.ndarray) -> tuple[float, np.ndarray]:
    """Return ``T[y,y,y]`` and ``T[y,y,.]``."""

    contracted = np.einsum("ijk,j,k->i", tensor, vector, vector, optimize=True)
    return float(np.dot(vector, contracted)), contracted


def _segmented_primes(left: int, right: int) -> np.ndarray:
    """Return primes in the inclusive integer interval ``[left,right]``."""

    if right < left or right < 2:
        return np.empty(0, dtype=np.int64)
    left = max(2, int(left))
    right = int(right)
    mask = np.ones(right - left + 1, dtype=bool)
    for prime_raw in primes_up_to(math.isqrt(right)):
        prime = int(prime_raw)
        first = max(prime * prime, ((left + prime - 1) // prime) * prime)
        if first <= right:
            mask[first - left :: prime] = False
    return np.arange(left, right + 1, dtype=np.int64)[mask]


def short_right_window_skew_diagnostic(
    N: int,
    *,
    full_aperture: float = FULL_APERTURE,
    spline_order: int = 8,
) -> ShortRightWindowSkewDiagnostic:
    """Test the uniform negative packet on ``Y<p<=Y+Y/sqrt(B)``.

    Here ``Y=N+1/2`` and the coefficients are all ``-1`` (normalization is
    immaterial).  In addition to exact-transform floating moments, this
    returns a rigorous analytic bound for this packet whenever the reported
    covariance lower bound is positive.

    Indeed, writing ``p=Y+h`` makes every ``h`` a half-integer.  Every signed
    sum of three such ``h`` is again a nonzero half-integer.  On the stated
    window the logarithmic Taylor errors total at most ``3/(2B)``, so for
    ``B>=6Y`` every signed triple log frequency is at least ``1/(4Y)``.
    The order-q spline transform is consequently at most
    ``epsilon=(24*q*Y/B)^q`` in absolute value.  Gershgorin and the centered
    third-moment formula then give the bound returned below.
    """

    if N < 2:
        raise ValueError("N must be at least two")
    Y = N + 0.5
    bandwidth = Y**full_aperture
    length = Y / math.sqrt(bandwidth)
    primes = _segmented_primes(math.floor(Y) + 1, math.floor(Y + length))
    if len(primes) == 0:
        raise ValueError("the short right window contains no primes")
    nodes = np.log(primes.astype(float) / Y)
    model = continuum_moment_model(
        nodes, bandwidth, spline_order=spline_order
    )
    coefficients = -np.ones(len(primes), dtype=float)
    variance = float(coefficients @ model.covariance @ coefficients)
    third = float(
        np.einsum(
            "i,j,k,ijk",
            coefficients,
            coefficients,
            coefficients,
            model.third_central,
            optimize=True,
        )
    )
    standardized = third / variance**1.5

    if bandwidth < 6.0 * Y:
        epsilon = 1.0
    else:
        epsilon = min(
            1.0, (24.0 * spline_order * Y / bandwidth) ** spline_order
        )
    covariance_lower = 0.5 - len(primes) * (epsilon + epsilon * epsilon)
    if covariance_lower > 0.0:
        analytic_upper = (
            (4.0 * epsilon + 2.0 * epsilon**3)
            * len(primes) ** 1.5
            / covariance_lower**1.5
        )
    else:
        analytic_upper = math.inf
    delta = 1.0 + Y * Y / bandwidth
    return ShortRightWindowSkewDiagnostic(
        N=N,
        Y=Y,
        bandwidth=bandwidth,
        window_length=length,
        prime_count=len(primes),
        variance=variance,
        central_third=third,
        negative_skew=max(0.0, -standardized),
        absolute_standardized_third=abs(standardized),
        packet_scale_quarter_power=delta**0.25,
        half_integer_transform_epsilon=epsilon,
        covariance_lower_bound=covariance_lower,
        rigorous_absolute_skew_upper=analytic_upper,
    )


def cubic_spectral_diagnostic(
    model: ContinuumMomentModel,
    *,
    starts: int = 16,
    seed: int = 0,
    maximum_iterations: int = 500,
    eigenvalue_tolerance: float = 1.0e-12,
) -> CubicSpectralDiagnostic:
    """Optimize negative skew and compute a global matricization upper.

    If ``T~`` is the covariance-whitened central third tensor, then

        max_(||x||=1) |T~[x,x,x]| <= ||T~_(1)||_(2->2).

    The left side is attacked by multi-start sphere ascent.  The right side
    is a global bound for the floating moment model, not interval arithmetic.
    """

    eigenvalues, eigenvectors = np.linalg.eigh(model.covariance)
    keep = eigenvalues > eigenvalue_tolerance * float(eigenvalues[-1])
    whitening = eigenvectors[:, keep] / np.sqrt(eigenvalues[keep])[None, :]
    rank = whitening.shape[1]

    def data(x: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
        y = whitening @ x
        third, contracted = _third_contraction(model.third_central, y)
        gradient = -3.0 * (whitening.T @ contracted)
        return -third, gradient, y

    def refine(x0: np.ndarray) -> tuple[np.ndarray, float, bool]:
        x = np.asarray(x0, dtype=float)
        x /= np.linalg.norm(x)
        if data(x)[0] < 0.0:
            x = -x
        angle_hint = 0.25
        converged = False
        for _ in range(maximum_iterations):
            value, gradient, _ = data(x)
            projected = gradient - float(np.dot(gradient, x)) * x
            norm = float(np.linalg.norm(projected))
            if norm <= 2.0e-8 * max(1.0, abs(value)):
                converged = True
                break
            direction = projected / norm
            angle = min(0.5, angle_hint)
            accepted = False
            while angle >= 1.0e-12:
                trial = math.cos(angle) * x + math.sin(angle) * direction
                trial_value = data(trial)[0]
                if trial_value >= value + 1.0e-4 * angle * norm:
                    x = trial
                    angle_hint = min(0.5, 1.5 * angle)
                    accepted = True
                    break
                angle *= 0.5
            if not accepted:
                converged = norm <= 2.0e-6 * max(1.0, abs(value))
                break
        return x, data(x)[0], converged

    rng = np.random.default_rng(seed)
    best_x: np.ndarray | None = None
    best_value = -math.inf
    best_converged = False
    for _ in range(max(1, starts)):
        x0 = rng.normal(size=rank)
        # A few tensor-power steps provide eigenvector-informed seeds before
        # the guarded Riemannian ascent.
        x0 /= np.linalg.norm(x0)
        for _ in range(12):
            _, gradient, _ = data(x0)
            if np.linalg.norm(gradient) == 0.0:
                break
            x0 = gradient / np.linalg.norm(gradient)
            if data(x0)[0] < 0.0:
                x0 = -x0
        x, value, converged = refine(x0)
        if value > best_value:
            best_x = x
            best_value = value
            best_converged = converged
    assert best_x is not None
    _, gradient, coefficients = data(best_x)
    projected = gradient - float(np.dot(gradient, best_x)) * best_x
    residual = float(np.linalg.norm(projected) / max(1.0, abs(best_value)))

    whitened_tensor = np.einsum(
        "ijk,ia,jb,kc->abc",
        model.third_central,
        whitening,
        whitening,
        whitening,
        optimize="optimal",
    )
    matricization = whitened_tensor.reshape(rank, rank * rank)
    upper = float(np.linalg.svd(matricization, compute_uv=False)[0])
    return CubicSpectralDiagnostic(
        negative_skew_candidate=best_value,
        matricization_upper=upper,
        relative_stationarity_residual=residual,
        converged=best_converged,
        starts=max(1, starts),
        whitened_vector=best_x,
        coefficients=coefficients,
    )


def optimize_joint_invariant(
    model: ContinuumMomentModel,
    residual: np.ndarray,
    *,
    starts: int = 12,
    seed: int = 0,
    maximum_iterations: int = 500,
    eigenvalue_tolerance: float = 1.0e-12,
    whitened_seed_vectors: list[np.ndarray] | None = None,
) -> JointInvariantCandidate:
    """Multi-start sphere optimization of ``J_v``.

    The covariance is whitened, so every optimization vector has variance
    one.  Since the problem is nonconvex, the returned value is a candidate
    lower bound for the true supremum.
    """

    v = np.asarray(residual, dtype=float)
    if v.shape != model.nodes.shape:
        raise ValueError("residual and nodes must have equal shape")
    eigenvalues, eigenvectors = np.linalg.eigh(model.covariance)
    threshold = eigenvalue_tolerance * float(eigenvalues[-1])
    keep = eigenvalues > threshold
    if not np.any(keep):
        raise np.linalg.LinAlgError("covariance whitening retained no directions")
    whitening = eigenvectors[:, keep] / np.sqrt(eigenvalues[keep])[None, :]
    calibrated = whitening.T @ v
    leverage_upper = float(np.linalg.norm(calibrated))
    if leverage_upper == 0.0:
        raise ValueError("residual vanishes on the covariance range")

    tensor = model.third_central

    def data(x: np.ndarray) -> tuple[float, np.ndarray, float, float, float, np.ndarray]:
        y = whitening @ x
        third, contracted = _third_contraction(tensor, y)
        third_gradient = 3.0 * (whitening.T @ contracted)
        leverage = -float(np.dot(calibrated, x))
        negative_skew = max(0.0, -third)
        value = max(0.0, leverage) * (1.0 + negative_skew)
        if leverage <= 0.0:
            gradient = np.zeros_like(x)
        elif third < 0.0:
            gradient = -calibrated * (1.0 + negative_skew) - leverage * third_gradient
        else:
            gradient = -calibrated
        return value, gradient, leverage, third, negative_skew, y

    def objective(x: np.ndarray) -> float:
        return -data(x)[0]

    def objective_gradient(x: np.ndarray) -> np.ndarray:
        return -data(x)[1]

    rng = np.random.default_rng(seed)
    leverage_start = -calibrated / leverage_upper
    initial: list[np.ndarray] = [leverage_start]
    if whitened_seed_vectors is not None:
        for supplied in whitened_seed_vectors:
            supplied_array = np.asarray(supplied, dtype=float)
            if supplied_array.shape != calibrated.shape or np.linalg.norm(supplied_array) == 0.0:
                raise ValueError("a supplied whitened seed has the wrong shape")
            supplied_array = supplied_array / np.linalg.norm(supplied_array)
            if np.dot(calibrated, supplied_array) > 0.0:
                supplied_array = -supplied_array
            initial.append(supplied_array)
    scales = (0.15, 0.4, 0.8, 1.5)
    while len(initial) < max(1, starts):
        scale = scales[(len(initial) - 1) % len(scales)]
        trial = leverage_start + scale * rng.normal(size=len(calibrated))
        trial /= np.linalg.norm(trial)
        if np.dot(calibrated, trial) > 0.0:
            trial = -trial
        initial.append(trial)

    best_x: np.ndarray | None = None
    best_value = -math.inf
    best_converged = False
    best_iterations = 0

    def refine_on_sphere(x0: np.ndarray) -> tuple[np.ndarray, float, bool, int]:
        """Projected-gradient ascent with an Armijo great-circle search."""

        x = np.asarray(x0, dtype=float)
        x /= np.linalg.norm(x)
        if np.dot(calibrated, x) > 0.0:
            x = -x
        value = data(x)[0]
        angle_hint = 0.25
        converged = False
        for iteration in range(1, maximum_iterations + 1):
            value, gradient, *_ = data(x)
            projected = gradient - float(np.dot(gradient, x)) * x
            norm = float(np.linalg.norm(projected))
            if norm <= 2.0e-8 * max(1.0, abs(value)):
                converged = True
                break
            direction = projected / norm
            angle = min(0.5, angle_hint)
            accepted = False
            while angle >= 1.0e-12:
                trial = math.cos(angle) * x + math.sin(angle) * direction
                trial_value = data(trial)[0]
                if trial_value >= value + 1.0e-4 * angle * norm:
                    x = trial
                    value = trial_value
                    angle_hint = min(0.5, 1.5 * angle)
                    accepted = True
                    break
                angle *= 0.5
            if not accepted:
                converged = norm <= 2.0e-6 * max(1.0, abs(value))
                break
        return x, value, converged, iteration

    for x0 in initial:
        refined, candidate_value, converged, iterations = refine_on_sphere(x0)
        if candidate_value > best_value:
            best_value = candidate_value
            best_x = refined
            best_converged = converged
            best_iterations = iterations

    assert best_x is not None
    x = best_x
    value, gradient, leverage, third, negative_skew, y = data(x)
    projected = gradient - float(np.dot(gradient, x)) * x
    projected_relative = float(np.linalg.norm(projected) / max(1.0, abs(value)))

    # For Var=1, |E Z^3| <= ||Z||_infinity.  Cauchy and the smallest
    # covariance eigenvalue give a completely continuum (but very loose)
    # global skew guard.
    skew_guard = (
        (1.0 + float(np.max(np.abs(model.mean))))
        * math.sqrt(len(v) / model.minimum_eigenvalue)
    )
    global_guard = leverage_upper * (1.0 + skew_guard)
    return JointInvariantCandidate(
        value=value,
        leverage=leverage,
        negative_skew=negative_skew,
        standardized_third=third,
        variance=float(y @ model.covariance @ y),
        residual_pairing=float(np.dot(y, v)),
        leverage_upper=leverage_upper,
        crude_global_upper_guard=global_guard,
        projected_gradient_relative=projected_relative,
        optimizer_success=best_converged,
        optimizer_message=(
            f"projected-gradient {'converged' if best_converged else 'stopped'} "
            f"after {best_iterations} iterations"
        ),
        starts=len(initial),
        coefficients=y,
        whitened_vector=x,
    )


def stationary_identity_residual(
    model: ContinuumMomentModel,
    residual: np.ndarray,
    candidate: JointInvariantCandidate,
    *,
    eigenvalue_tolerance: float = 1.0e-12,
) -> float:
    """Relative residual of the exact active-negative-skew Euler equation."""

    eigenvalues, eigenvectors = np.linalg.eigh(model.covariance)
    keep = eigenvalues > eigenvalue_tolerance * float(eigenvalues[-1])
    whitening = eigenvectors[:, keep] / np.sqrt(eigenvalues[keep])[None, :]
    a = whitening.T @ np.asarray(residual, dtype=float)
    x = candidate.whitened_vector
    y = candidate.coefficients
    third, contracted = _third_contraction(model.third_central, y)
    txx = whitening.T @ contracted
    leverage = -float(np.dot(a, x))
    g = max(0.0, -third)
    if third >= 0.0:
        lhs = -a
        multiplier = leverage
    else:
        lhs = -(1.0 + g) * a - 3.0 * leverage * txx
        multiplier = leverage * (1.0 + 4.0 * g)
    residual_vector = lhs - multiplier * x
    return float(np.linalg.norm(residual_vector) / max(1.0, np.linalg.norm(lhs)))


def near_reflection_endpoints(
    signed_nodes: np.ndarray, bandwidth: float, *, kappa: float = 8.0
) -> tuple[list[tuple[int, int]], set[int]]:
    """Find opposite-side absolute-log pairs within ``kappa/B``."""

    signed = np.asarray(signed_nodes, dtype=float)
    lower = np.flatnonzero(signed < 0.0)
    upper = np.flatnonzero(signed > 0.0)
    upper_order = upper[np.argsort(np.abs(signed[upper]))]
    upper_values = np.abs(signed[upper_order])
    pairs: list[tuple[int, int]] = []
    endpoints: set[int] = set()
    tolerance = kappa / bandwidth
    for left_index in lower:
        value = abs(float(signed[left_index]))
        location = int(np.searchsorted(upper_values, value))
        choices = [position for position in (location - 1, location) if 0 <= position < len(upper_values)]
        if not choices:
            continue
        best = min(choices, key=lambda position: abs(float(upper_values[position]) - value))
        right_index = int(upper_order[best])
        if abs(float(upper_values[best]) - value) <= tolerance and right_index not in endpoints:
            pairs.append((int(left_index), right_index))
            endpoints.add(int(left_index))
            endpoints.add(right_index)
    return pairs, endpoints


def coefficient_packet_statistics(
    coefficients: np.ndarray,
    signed_nodes: np.ndarray,
    bandwidth: float,
    *,
    reflection_kappa: float = 8.0,
) -> dict[str, float | int]:
    """Scale-invariant coefficient and ``B^-1`` product-packet diagnostics."""

    y = np.asarray(coefficients, dtype=float)
    signed = np.asarray(signed_nodes, dtype=float)
    squares = y * y
    total_square = float(np.sum(squares))
    absolute = np.abs(y)
    effective_support = float(np.sum(absolute) ** 2 / total_square)
    ordered = np.sort(squares)[::-1]
    cumulative = np.cumsum(ordered) / total_square
    top50 = int(np.searchsorted(cumulative, 0.5) + 1)
    top90 = int(np.searchsorted(cumulative, 0.9) + 1)

    pairs, endpoints = near_reflection_endpoints(
        signed, bandwidth, kappa=reflection_kappa
    )
    endpoint_share = (
        float(np.sum(squares[list(endpoints)]) / total_square) if endpoints else 0.0
    )

    pair_frequencies = (signed[:, None] + signed[None, :]).ravel()
    pair_coefficients = (y[:, None] * y[None, :]).ravel()
    bins = np.floor(bandwidth * pair_frequencies).astype(np.int64)
    _, inverse = np.unique(bins, return_inverse=True)
    signed_mass = np.bincount(inverse, weights=pair_coefficients)
    absolute_mass = np.bincount(inverse, weights=np.abs(pair_coefficients))
    total_absolute_mass = float(np.sum(absolute_mass))
    cancellation_ratio = float(np.sum(np.abs(signed_mass)) / total_absolute_mass)
    packet_effective_count = float(
        total_absolute_mass**2 / np.sum(absolute_mass * absolute_mass)
    )
    largest_packet_share = float(np.max(absolute_mass) / total_absolute_mass)
    return {
        "coefficient_effective_support": effective_support,
        "top50_l2_coordinates": top50,
        "top90_l2_coordinates": top90,
        "positive_coefficient_fraction": float(np.mean(y > 0.0)),
        "coefficient_sum_over_l1": float(np.sum(y) / np.sum(absolute)),
        "near_reflection_pair_count": len(pairs),
        "near_reflection_endpoint_l2_share": endpoint_share,
        "product_packet_count": len(absolute_mass),
        "product_packet_effective_count": packet_effective_count,
        "largest_product_packet_l1_share": largest_packet_share,
        "signed_product_packet_cancellation_ratio": cancellation_ratio,
    }


def _residual_instances(
    N: int,
    powers: np.ndarray,
    nodes: np.ndarray,
    *,
    width: float,
    phase_step: float,
) -> dict[str, dict[str, float | np.ndarray | int]]:
    Y = N + 0.5
    primes, prime_logs = primes_in_shell(Y, width)
    high_left = N**0.5
    high_right = N**1.5

    eligible: list[tuple[float, int, float]] = []
    for prime, signed_log in zip(primes, prime_logs, strict=True):
        node_index = int(np.flatnonzero(powers == int(prime))[0])
        try:
            time = first_odd_resonance(float(nodes[node_index]), high_left, high_right)
        except ValueError:
            continue
        eligible.append((abs(float(signed_log)), int(prime), time))
    if not eligible:
        raise ValueError("no legal singleton resonance")
    _, singleton_prime, singleton_time = min(eligible)
    singleton_index = int(np.flatnonzero(powers == singleton_prime)[0])
    singleton_calibration = np.zeros(len(nodes), dtype=float)
    singleton_calibration[singleton_index] = 1.0

    broad = directional_interval_scan(
        primes,
        prime_logs,
        float(N),
        high_left,
        high_right,
        minimum_count=1,
        phase_step=phase_step,
    )
    broad_mask = (primes >= broad.left_prime) & (primes <= broad.right_prime)
    broad_depth = -float(np.mean(np.cos(prime_logs[broad_mask] * broad.time)))
    broad_calibration = np.zeros(len(nodes), dtype=float)
    for prime in primes[broad_mask]:
        broad_calibration[int(np.flatnonzero(powers == int(prime))[0])] = 1.0 / float(
            np.sum(broad_mask)
        )
    return {
        "singleton": {
            "time": singleton_time,
            "depth": 1.0,
            "prime": singleton_prime,
            "residual": np.cos(nodes * singleton_time) + 1.0,
            "calibration": singleton_calibration,
        },
        "broad": {
            "time": broad.time,
            "depth": broad_depth,
            "prime_count": int(np.sum(broad_mask)),
            "left_prime": broad.left_prime,
            "right_prime": broad.right_prime,
            "residual": np.cos(nodes * broad.time) + broad_depth,
            "calibration": broad_calibration,
        },
    }


def run_joint_invariant_instance(
    N: int,
    *,
    width: float = 0.2,
    full_aperture: float = FULL_APERTURE,
    spline_order: int = 8,
    starts: int = 12,
    phase_step: float = 0.12,
    seed: int = 0,
) -> dict[str, Any]:
    """Run singleton and broad actual-node joint-invariant diagnostics."""

    Y = N + 0.5
    powers, nodes = prime_powers_in_shell(Y, width)
    signed_nodes = np.log(powers.astype(float) / Y)
    bandwidth = Y**full_aperture
    model = continuum_moment_model(nodes, bandwidth, spline_order=spline_order)
    skew_spectral = cubic_spectral_diagnostic(
        model,
        starts=max(8, starts),
        seed=seed + 7919 * N,
    )
    residuals = _residual_instances(
        N, powers, nodes, width=width, phase_step=phase_step
    )
    delta = 1.0 + Y * Y / bandwidth
    rows: dict[str, Any] = {}
    for offset, (name, metadata) in enumerate(residuals.items()):
        candidate = optimize_joint_invariant(
            model,
            np.asarray(metadata["residual"]),
            starts=starts,
            seed=seed + 1009 * N + offset,
            whitened_seed_vectors=[
                skew_spectral.whitened_vector,
                -skew_spectral.whitened_vector,
            ],
        )
        packet = coefficient_packet_statistics(
            candidate.coefficients, signed_nodes, bandwidth
        )
        residual = np.asarray(metadata["residual"])
        calibration = np.asarray(metadata["calibration"])
        coefficients = candidate.coefficients
        carrier_alignment = min(
            1.0, max(0.0, candidate.leverage / candidate.leverage_upper)
        )
        payload = {
            key: value
            for key, value in metadata.items()
            if key not in {"residual", "calibration"}
        }
        payload.update(
            {
                "J_candidate": candidate.value,
                "leverage": candidate.leverage,
                "negative_skew": candidate.negative_skew,
                "standardized_third": candidate.standardized_third,
                "leverage_upper": candidate.leverage_upper,
                "whitened_carrier_alignment": carrier_alignment,
                "whitened_carrier_variance_share": carrier_alignment**2,
                "whitened_calibrated_null_variance_share": 1.0 - carrier_alignment**2,
                "calibration_dot_residual_replay": float(np.dot(calibration, residual)),
                "coefficient_calibration_cosine": float(
                    np.dot(coefficients, calibration)
                    / (np.linalg.norm(coefficients) * np.linalg.norm(calibration))
                ),
                "J_over_sqrt_M": candidate.value / math.sqrt(len(nodes)),
                "J_over_41_66_proxy": (
                    candidate.value / (math.sqrt(len(nodes)) * delta**0.25)
                ),
                "J_over_49_66_proxy": candidate.value / math.sqrt(len(nodes) * delta),
                "negative_skew_over_packet_quarter": (
                    candidate.negative_skew / delta**0.25
                ),
                "negative_skew_over_sqrt_packet": candidate.negative_skew / math.sqrt(delta),
                "variance_replay": candidate.variance,
                "residual_pairing_replay": candidate.residual_pairing,
                "negative_pairing_constraint_satisfied": bool(
                    candidate.residual_pairing < 0.0
                ),
                "stationary_identity_relative_residual": stationary_identity_residual(
                    model, residual, candidate
                ),
                "optimizer_success": candidate.optimizer_success,
                "optimizer_message": candidate.optimizer_message,
                "optimizer_starts": candidate.starts,
                "crude_continuum_global_upper_guard": candidate.crude_global_upper_guard,
                "floating_matricization_global_J_upper": (
                    candidate.leverage_upper
                    * (1.0 + skew_spectral.matricization_upper)
                ),
                "J_over_floating_matricization_global_upper": (
                    candidate.value
                    / (
                        candidate.leverage_upper
                        * (1.0 + skew_spectral.matricization_upper)
                    )
                ),
                "floating_global_upper_over_sqrt_M": (
                    candidate.leverage_upper
                    * (1.0 + skew_spectral.matricization_upper)
                    / math.sqrt(len(nodes))
                ),
                "floating_global_upper_over_41_66_proxy": (
                    candidate.leverage_upper
                    * (1.0 + skew_spectral.matricization_upper)
                    / (math.sqrt(len(nodes)) * delta**0.25)
                ),
                "floating_global_upper_over_49_66_proxy": (
                    candidate.leverage_upper
                    * (1.0 + skew_spectral.matricization_upper)
                    / math.sqrt(len(nodes) * delta)
                ),
                **packet,
            }
        )
        rows[name] = payload
    return {
        "N": N,
        "Y": Y,
        "node_count": len(nodes),
        "bandwidth": bandwidth,
        "aperture_exponent": full_aperture,
        "packet_scale": delta,
        "sqrt_packet_scale": math.sqrt(delta),
        "packet_scale_quarter_power": delta**0.25,
        "spline_order": spline_order,
        "time_support": [bandwidth / 3.0, 2.0 * bandwidth / 3.0],
        "covariance_minimum_eigenvalue": model.minimum_eigenvalue,
        "covariance_maximum_eigenvalue": model.maximum_eigenvalue,
        "covariance_retained_rank": model.retained_rank,
        "third_tensor_symmetry_error": model.symmetry_error,
        "negative_skew_spectral_candidate": (
            skew_spectral.negative_skew_candidate
        ),
        "negative_skew_matricization_upper": skew_spectral.matricization_upper,
        "negative_skew_spectral_candidate_over_upper": (
            skew_spectral.negative_skew_candidate
            / skew_spectral.matricization_upper
        ),
        "negative_skew_matricization_upper_over_sqrt_packet": (
            skew_spectral.matricization_upper / math.sqrt(delta)
        ),
        "negative_skew_matricization_upper_over_packet_quarter": (
            skew_spectral.matricization_upper / delta**0.25
        ),
        "negative_skew_spectral_candidate_over_packet_quarter": (
            skew_spectral.negative_skew_candidate / delta**0.25
        ),
        "negative_skew_spectral_relative_stationarity_residual": (
            skew_spectral.relative_stationarity_residual
        ),
        "negative_skew_spectral_optimizer_converged": skew_spectral.converged,
        "negative_skew_spectral_optimizer_starts": skew_spectral.starts,
        "continuum_moments_from_exact_characteristic_function": True,
        "floating_nonlinear_candidates_only": True,
        "residuals": rows,
    }


def scaling_fit(results: list[dict[str, Any]], residual_name: str) -> dict[str, float]:
    """Least-squares log slopes for a named residual family."""

    if len(results) < 2:
        item = results[0]["residuals"][residual_name]
        return {
            "slope_vs_Y": math.nan,
            "intercept_vs_Y": math.nan,
            "slope_vs_M": math.nan,
            "intercept_vs_M": math.nan,
            "slope_of_J_over_sqrt_M_vs_Y": math.nan,
            "slope_of_J_over_41_66_proxy_vs_Y": math.nan,
            "slope_of_J_over_49_66_proxy_vs_Y": math.nan,
            "median_J_over_sqrt_M": float(item["J_over_sqrt_M"]),
            "median_J_over_41_66_proxy": float(item["J_over_41_66_proxy"]),
            "median_J_over_49_66_proxy": float(item["J_over_49_66_proxy"]),
        }
    log_y = np.log([row["Y"] for row in results])
    log_m = np.log([row["node_count"] for row in results])
    log_j = np.log([row["residuals"][residual_name]["J_candidate"] for row in results])
    log_sqrt_m = 0.5 * log_m
    log_quarter_proxy = np.log(
        [
            math.sqrt(row["node_count"]) * row["packet_scale"] ** 0.25
            for row in results
        ]
    )
    log_proxy = np.log(
        [
            math.sqrt(row["node_count"] * row["packet_scale"])
            for row in results
        ]
    )
    slope_y, intercept_y = np.polyfit(log_y, log_j, 1)
    slope_m, intercept_m = np.polyfit(log_m, log_j, 1)
    normalized_slope_y, _ = np.polyfit(log_y, log_j - log_sqrt_m, 1)
    quarter_proxy_slope_y, _ = np.polyfit(
        log_y, log_j - log_quarter_proxy, 1
    )
    proxy_slope_y, _ = np.polyfit(log_y, log_j - log_proxy, 1)
    ratios_sqrt = np.exp(log_j - log_sqrt_m)
    ratios_quarter_proxy = np.exp(log_j - log_quarter_proxy)
    ratios_proxy = np.exp(log_j - log_proxy)
    return {
        "slope_vs_Y": float(slope_y),
        "intercept_vs_Y": float(intercept_y),
        "slope_vs_M": float(slope_m),
        "intercept_vs_M": float(intercept_m),
        "slope_of_J_over_sqrt_M_vs_Y": float(normalized_slope_y),
        "slope_of_J_over_41_66_proxy_vs_Y": float(quarter_proxy_slope_y),
        "slope_of_J_over_49_66_proxy_vs_Y": float(proxy_slope_y),
        "median_J_over_sqrt_M": float(np.median(ratios_sqrt)),
        "median_J_over_41_66_proxy": float(np.median(ratios_quarter_proxy)),
        "median_J_over_49_66_proxy": float(np.median(ratios_proxy)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--N", type=int, nargs="+", default=[70, 200, 600, 1000, 1800])
    parser.add_argument("--starts", type=int, default=12)
    parser.add_argument("--phase-step", type=float, default=0.12)
    parser.add_argument("--spline-order", type=int, default=8)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument(
        "--short-window-N",
        type=int,
        nargs="*",
        default=[],
        help="also test uniform negative packets on Y<p<=Y+Y/sqrt(B)",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    results = [
        run_joint_invariant_instance(
            value,
            starts=args.starts,
            phase_step=args.phase_step,
            spline_order=args.spline_order,
            seed=args.seed,
        )
        for value in args.N
    ]
    scaling: dict[str, Any] = {
        "all_scales": {
            name: scaling_fit(results, name) for name in ("singleton", "broad")
        }
    }
    if len(results) >= 4:
        scaling["excluding_smallest"] = {
            name: scaling_fit(results[1:], name) for name in ("singleton", "broad")
        }
    if len(results) >= 5:
        scaling["last_four"] = {
            name: scaling_fit(results[-4:], name) for name in ("singleton", "broad")
        }
    payload = {
        "schema": "zeta23.qp-transverse-joint-invariant-lab.v1",
        "scope": "floating nonlinear candidates; exact-transform continuum moments",
        "rows": results,
        "scaling": scaling,
        "short_right_window_packets": [
            asdict(
                short_right_window_skew_diagnostic(
                    value,
                    spline_order=args.spline_order,
                )
            )
            for value in args.short_window_N
        ],
    }
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return
    for row in results:
        for name in ("singleton", "broad"):
            item = row["residuals"][name]
            print(
                f"N={row['N']:5d} M={row['node_count']:4d} {name:9s} "
                f"J={item['J_candidate']:10.5f} L={item['leverage']:9.5f} "
                f"G-={item['negative_skew']:8.5f} "
                f"J/sqrtM={item['J_over_sqrt_M']:8.5f} "
                f"J/41={item['J_over_41_66_proxy']:8.5f} "
                f"J/proxy={item['J_over_49_66_proxy']:8.5f} "
                f"eff={item['coefficient_effective_support']:7.2f} "
                f"refl={item['near_reflection_endpoint_l2_share']:7.3f} "
                f"stat={item['stationary_identity_relative_residual']:.2e}"
            )
    for item in payload["short_right_window_packets"]:
        print(
            f"short-window N={item['N']:13d} K={item['prime_count']:4d} "
            f"Gamma_abs={item['absolute_standardized_third']:.5e} "
            f"Delta^1/4={item['packet_scale_quarter_power']:.5f} "
            f"rigorous-upper={item['rigorous_absolute_skew_upper']:.5e}"
        )
    print(json.dumps(scaling, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
