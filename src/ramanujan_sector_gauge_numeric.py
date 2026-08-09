#!/usr/bin/env python3
"""Finite-torus proxy for sector-aware Ramanujan null-gauge optimization.

This module is deliberately a numerical falsifier, not an R71 estimate.  On
``1 <= n <= Y`` it uses the exact synthesis matrix

    S[n, q] = c_q(n),                 1 <= q <= 2Y,

and restricts coefficient changes to ``S x = Lambda`` with ``x_1 = 1``.
Thus every computed change is an actual finite Ramanujan null gauge and the
displayed integer-lattice coefficient remains the completed one.

Each Ramanujan sum is expanded into one representative of every primitive
residue ``a/q`` on the finite torus.  Farey frequencies are grouped into
shift-averaged bins.  The sum of the within-bin Gram matrices is a positive
semidefinite proxy for the determinant-zero, dual-zero, and near-axis
sectors.  Its complement is called ``off_axis``.  This is *not* the exact
continuous Poisson ``j=0`` decomposition: integer aliases have been collapsed
and a frequency-resolution bin is standing in for the Wright sector cut.

The smooth shell kernel is positive semidefinite, so the proxy can safely be
used to reject proposed coefficient-norm shortcuts.  Favorable output cannot
by itself certify a zero-free region.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass, field

import numpy as np
from scipy.linalg import null_space

from finite_ramanujan_completion_probe import (
    expected_von_mangoldt,
    mobius_sieve,
    ramanujan_sum,
)
from ramanujan_null_gauge_probe import (
    evaluate,
    gauged_coefficients,
    inverse_totient_weights,
)


@dataclass(frozen=True)
class SectorGaugeProxy:
    """Matrices defining one deterministic finite sector proxy."""

    active_limit: int
    cutoff: int
    bin_count: int
    shift_count: int
    mode_reconstruction_error: float
    synthesis: np.ndarray = field(repr=False, compare=False)
    target: np.ndarray = field(repr=False, compare=False)
    baseline: np.ndarray = field(repr=False, compare=False)
    kernel: np.ndarray = field(repr=False, compare=False)
    ledger_weights: np.ndarray = field(repr=False, compare=False)
    full: np.ndarray = field(repr=False, compare=False)
    bad: np.ndarray = field(repr=False, compare=False)
    theta_zero: np.ndarray = field(repr=False, compare=False)
    axes: np.ndarray = field(repr=False, compare=False)
    near_zero: np.ndarray = field(repr=False, compare=False)
    off_axis: np.ndarray = field(repr=False, compare=False)

    def energy(self, matrix: np.ndarray, coefficients: np.ndarray) -> float:
        """Return the real quadratic energy of ``coefficients``."""

        vector = np.asarray(coefficients, dtype=float)
        if vector.shape != (self.cutoff,):
            raise ValueError("coefficient vector has the wrong length")
        return float(vector @ matrix @ vector)

    @property
    def baseline_ledger(self) -> float:
        """Return ``sum_q phi(q)|x_q|^2`` for the exact prime-cloud gauge."""

        return float(np.dot(self.ledger_weights, self.baseline**2))


@dataclass(frozen=True)
class PenalizedGauge:
    """One point on the bad-sector/ledger quadratic tradeoff."""

    relative_penalty: float
    absolute_penalty: float
    constraint_residual: float
    ledger: float
    full_energy: float
    bad_energy: float
    theta_zero_energy: float
    axes_energy: float
    near_zero_energy: float
    off_axis_energy: float
    coefficients: np.ndarray = field(repr=False, compare=False)


def _totients(limit: int) -> np.ndarray:
    values = np.arange(limit + 1, dtype=int)
    for prime in range(2, limit + 1):
        if values[prime] != prime:
            continue
        values[prime::prime] -= values[prime::prime] // prime
    return values


def _target_values(active_limit: int) -> np.ndarray:
    answer = np.zeros(active_limit, dtype=float)
    for n in range(1, active_limit + 1):
        answer[n - 1] = evaluate(expected_von_mangoldt(n))
    return answer


def smooth_shell_kernel(active_limit: int) -> np.ndarray:
    """Return the normalized positive Gaussian shell kernel used by the proxy."""

    if active_limit < 4:
        raise ValueError("active_limit must be at least four")
    points = np.arange(1, active_limit + 1, dtype=float)
    center = 0.68 * active_limit
    shell_width = 0.22 * active_limit
    correlation_width = max(1.0, 0.06 * active_limit)
    weights = np.exp(-0.5 * ((points - center) / shell_width) ** 2)
    difference = points[:, None] - points[None, :]
    return (
        np.sqrt(weights[:, None] * weights[None, :])
        * np.exp(-0.5 * (difference / correlation_width) ** 2)
        / (math.sqrt(2.0 * math.pi) * correlation_width)
    )


def build_sector_proxy(
    active_limit: int,
    *,
    bin_count: int | None = None,
    shift_count: int = 4,
) -> SectorGaugeProxy:
    """Build the exact-null, finite-torus sector proxy at cutoff ``2Y``."""

    if active_limit < 4:
        raise ValueError("active_limit must be at least four")
    if shift_count < 1:
        raise ValueError("shift_count must be positive")
    cutoff = 2 * active_limit
    bins = active_limit if bin_count is None else bin_count
    if bins < 2:
        raise ValueError("bin_count must be at least two")

    points = np.arange(1, active_limit + 1, dtype=float)
    mobius = mobius_sieve(cutoff)
    synthesis = np.asarray(
        [
            [ramanujan_sum(q, n, mobius) for q in range(1, cutoff + 1)]
            for n in range(1, active_limit + 1)
        ],
        dtype=float,
    )
    target = _target_values(active_limit)
    baseline = np.asarray(
        [evaluate(vector) for vector in gauged_coefficients(active_limit)[1:]],
        dtype=float,
    )
    kernel = smooth_shell_kernel(active_limit)

    # A mode is (zero-based denominator index, torus frequency, values).
    modes: list[tuple[int, float, np.ndarray]] = [
        (0, 0.0, np.ones(active_limit, dtype=complex))
    ]
    for q in range(2, cutoff + 1):
        for numerator in range(1, q):
            if math.gcd(numerator, q) != 1:
                continue
            frequency = numerator / q
            values = np.exp(2j * math.pi * frequency * points)
            modes.append((q - 1, frequency, values))

    theta_zero = np.zeros((cutoff, cutoff), dtype=float)
    for q_index, _, values in modes:
        theta_zero[q_index, q_index] += float(
            np.real(values.conj() @ kernel @ values)
        )

    bad = np.zeros((cutoff, cutoff), dtype=float)
    first_mode_synthesis: np.ndarray | None = None
    for shift_index in range(shift_count):
        shift = (shift_index + 0.5) / shift_count
        binned = np.zeros((bins, active_limit, cutoff), dtype=complex)
        for q_index, frequency, values in modes:
            index = int(math.floor(frequency * bins + shift)) % bins
            binned[index, :, q_index] += values
        if first_mode_synthesis is None:
            first_mode_synthesis = np.sum(binned, axis=0)
        for block in binned:
            bad += np.real(block.conj().T @ kernel @ block) / shift_count

    assert first_mode_synthesis is not None
    reconstruction_error = float(
        np.max(np.abs(first_mode_synthesis - synthesis))
    )
    full = synthesis.T @ kernel @ synthesis

    # The q=1 self-pair is already in theta_zero.  ``axes`` holds only its
    # cross terms, making bad = theta_zero + axes + near_zero exact.
    axes = np.zeros_like(bad)
    axes[0, 1:] = bad[0, 1:]
    axes[1:, 0] = bad[1:, 0]
    near_zero = bad - theta_zero - axes
    off_axis = full - bad
    ledger_weights = _totients(cutoff)[1:].astype(float)

    return SectorGaugeProxy(
        active_limit=active_limit,
        cutoff=cutoff,
        bin_count=bins,
        shift_count=shift_count,
        mode_reconstruction_error=reconstruction_error,
        synthesis=synthesis,
        target=target,
        baseline=baseline,
        kernel=kernel,
        ledger_weights=ledger_weights,
        full=full,
        bad=bad,
        theta_zero=theta_zero,
        axes=axes,
        near_zero=near_zero,
        off_axis=off_axis,
    )


def prime_cloud_null_vector(proxy: SectorGaugeProxy) -> np.ndarray:
    """Return the exact vector ``c_1 + sum_p w_p c_p = 0`` on the shell."""

    vector = np.zeros(proxy.cutoff, dtype=float)
    vector[0] = 1.0
    for prime, weight in inverse_totient_weights(proxy.active_limit).items():
        vector[prime - 1] = float(weight)
    return vector


def penalized_gauge(
    proxy: SectorGaugeProxy,
    relative_penalty: float,
) -> PenalizedGauge:
    """Minimize ``bad + penalty * ledger`` on the exact completed null orbit."""

    if relative_penalty < 0.0 or not math.isfinite(relative_penalty):
        raise ValueError("relative_penalty must be finite and nonnegative")
    q_one = np.zeros(proxy.cutoff, dtype=float)
    q_one[0] = 1.0
    constraints = np.vstack((proxy.synthesis, q_one))
    right_hand_side = np.concatenate((proxy.target, np.asarray([1.0])))
    null_basis = null_space(constraints, rcond=1.0e-11)

    scale = float(np.trace(proxy.bad) / np.sum(proxy.ledger_weights))
    absolute_penalty = relative_penalty * scale
    hessian = proxy.bad + absolute_penalty * np.diag(proxy.ledger_weights)
    reduced = null_basis.T @ hessian @ null_basis
    forcing = -null_basis.T @ hessian @ proxy.baseline
    adjustment = np.linalg.lstsq(reduced, forcing, rcond=1.0e-11)[0]
    coefficients = proxy.baseline + null_basis @ adjustment
    residual = float(
        np.max(np.abs(constraints @ coefficients - right_hand_side))
    )

    return PenalizedGauge(
        relative_penalty=relative_penalty,
        absolute_penalty=absolute_penalty,
        constraint_residual=residual,
        ledger=float(np.dot(proxy.ledger_weights, coefficients**2)),
        full_energy=proxy.energy(proxy.full, coefficients),
        bad_energy=proxy.energy(proxy.bad, coefficients),
        theta_zero_energy=proxy.energy(proxy.theta_zero, coefficients),
        axes_energy=proxy.energy(proxy.axes, coefficients),
        near_zero_energy=proxy.energy(proxy.near_zero, coefficients),
        off_axis_energy=proxy.energy(proxy.off_axis, coefficients),
        coefficients=coefficients,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--active-limit", type=int, default=24)
    parser.add_argument("--shift-count", type=int, default=4)
    parser.add_argument("--relative-penalty", type=float, default=0.01)
    args = parser.parse_args()

    proxy = build_sector_proxy(
        args.active_limit,
        shift_count=args.shift_count,
    )
    candidate = penalized_gauge(proxy, args.relative_penalty)
    null_vector = prime_cloud_null_vector(proxy)
    print(f"mode_reconstruction_error={proxy.mode_reconstruction_error:.3g}")
    print(f"minimum_bad_eigenvalue={np.linalg.eigvalsh(proxy.bad)[0]:.12g}")
    print(f"prime_cloud_null_residual={np.max(np.abs(proxy.synthesis @ null_vector)):.3g}")
    print(f"baseline_ledger={proxy.baseline_ledger:.12g}")
    print(f"candidate_ledger={candidate.ledger:.12g}")
    print(f"candidate_bad_energy={candidate.bad_energy:.12g}")
    print(f"candidate_off_axis_energy={candidate.off_axis_energy:.12g}")


if __name__ == "__main__":
    main()
