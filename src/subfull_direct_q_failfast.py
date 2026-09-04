"""Adversarial scan and rigorous negative-dual certificates for direct q.

The floating scan varies the hypothetical reflected-pair depth, its height,
the phase of the critical grid, aperture, endpoint-jet order, and retained
carrier fraction.  A negative value is only a scout result.

For a proposed negative point, :func:`build_rigorous_fixture_forms` rebuilds
the complete finite matrix with FLINT Arb/Acb balls.  Unlike the exploratory
fixture, the proof path does not use a floating orthonormal nullspace.  It
uses

* an exact rational basis of the endpoint-moment kernel;
* one Arb pivot elimination for the selected positive row; and
* a verified interval ``LDL*`` test of

      (mu * theta * kappa - delta) G - K - mu N > 0.

Here ``G`` is the Gram matrix of the nonorthonormal full basis of
``W_m intersect ker(x*)``.  Consequently a successful result proves

      K_ar + mu N <= (mu theta kappa - delta) I

on the entire finite selected-null space, and hence
``q_(theta*kappa)(K_ar) <= -delta``.  The certificate is a theorem about the
specified finite sharp-grid model, not about an unscanned continuum of
parameters and not by itself a zero-free result.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import json
import math
from typing import Any, Iterable, Sequence

import numpy as np
from scipy.linalg import null_space

from carrier_slice_support import carrier_slice_support
from high_height_carrier_slice import (
    archimedean_matrix_sign,
    endpoint_null_basis,
    pole_matrix_sign,
    prime_matrix_sign,
)
from signed_garding_failfast import prime_powers

try:
    from flint import acb, acb_mat, arb, ctx, fmpq, fmpq_mat
except ImportError:  # pragma: no cover - exercised only on missing dependency
    acb = acb_mat = arb = ctx = fmpq = fmpq_mat = None


def _as_fraction(value: int | float | str | Fraction) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, float):
        return Fraction(str(value))
    return Fraction(value)


def selected_rows_with_phase(
    tau: np.ndarray,
    length: float,
    gamma: float,
    alpha: float,
    grid_phase: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Selected real/imaginary rows on a phase-shifted critical grid.

    If ``tau_k=gamma+2*pi*(k+phi)/L``, sign conjugation cancels ``(-1)^k``
    but leaves the factor ``sin(-i*alpha*L/2-pi*phi)``.  Reusing the centered
    formula when ``phi != 0`` would therefore scan the wrong row.
    """
    if alpha <= 0 or alpha >= 0.5:
        raise ValueError("alpha must lie in (0,1/2)")
    z = gamma - 1j * alpha
    common = 2.0 * np.sin(
        length * (z - gamma) / 2.0 - math.pi * grid_phase
    )
    values = common / (z - tau)
    return np.real(values), np.imag(values)


@dataclass(frozen=True)
class FloatingBase:
    height: float
    length: float
    gamma_fraction: float
    gamma: float
    aperture_fraction: float
    grid_phase: float
    indices: np.ndarray
    tau: np.ndarray
    arithmetic: np.ndarray
    active_prime_powers: int


def build_floating_base(
    height: float,
    *,
    gamma_fraction: float,
    aperture_fraction: float,
    grid_phase: float,
) -> FloatingBase:
    """Build the zero-independent arithmetic matrix before conditioning."""
    if height <= 4 or abs(height - round(height)) > 1e-12:
        raise ValueError("the scan currently requires an integer height > 4")
    if not 1.0 < gamma_fraction < 2.0:
        raise ValueError("gamma_fraction must lie in (1,2)")
    if not -0.5 <= grid_phase <= 0.5:
        raise ValueError("grid_phase must lie in [-1/2,1/2]")
    if aperture_fraction <= 0:
        raise ValueError("aperture_fraction must be positive")

    length = math.log(height)
    gamma = gamma_fraction * height
    spacing = 2.0 * math.pi / length
    half_count = int(math.floor(aperture_fraction * height / spacing))
    if half_count < 2:
        raise ValueError("aperture leaves fewer than five grid nodes")
    indices = np.arange(-half_count, half_count + 1, dtype=int)
    tau = gamma + spacing * (indices + grid_phase)
    if tau[0] < height - 1e-12 or tau[-1] > 2.0 * height + 1e-12:
        raise ValueError("phase-shifted grid leaves the dyadic height band")

    logs, weights = prime_powers(int(round(height)))
    arithmetic = (
        archimedean_matrix_sign(tau, length)
        + pole_matrix_sign(tau, indices, length)
        - prime_matrix_sign(tau, length, logs, weights)
    ) / (length * length)
    arithmetic = (arithmetic + arithmetic.conj().T) / 2.0
    return FloatingBase(
        height=height,
        length=length,
        gamma_fraction=gamma_fraction,
        gamma=gamma,
        aperture_fraction=aperture_fraction,
        grid_phase=grid_phase,
        indices=indices,
        tau=tau,
        arithmetic=arithmetic,
        active_prime_powers=int(logs.size),
    )


def evaluate_floating_point(
    base: FloatingBase,
    *,
    alpha: float,
    jet_order: int,
    theta: float,
    iterations: int = 64,
) -> dict[str, Any]:
    """Evaluate one floating direct carrier slice."""
    if not 0 < theta <= 1:
        raise ValueError("theta must lie in (0,1]")
    endpoint = endpoint_null_basis(base.indices, jet_order)
    if endpoint.shape[1] < 2:
        raise ValueError("endpoint jets leave no selected-null direction")
    selected_x, selected_y = selected_rows_with_phase(
        base.tau, base.length, base.gamma, alpha, base.grid_phase
    )
    selected_null = null_space(
        (endpoint.T @ selected_x)[None, :], rcond=1e-12
    )
    inclusion = endpoint @ selected_null
    if inclusion.shape[1] == 0:
        raise ValueError("selected row deletes the endpoint space")

    projected_y = inclusion.T @ selected_y
    carrier = (
        2.0 / (base.length * base.length)
    ) * np.outer(projected_y, projected_y)
    kappa = float(np.linalg.eigvalsh(carrier)[-1])
    if kappa <= 1e-15:
        raise ValueError("carrier is numerically zero")
    arithmetic_slice = inclusion.conj().T @ base.arithmetic @ inclusion
    arithmetic_slice = (arithmetic_slice + arithmetic_slice.conj().T) / 2.0
    support = carrier_slice_support(
        arithmetic_slice, carrier, theta * kappa, iterations=iterations
    )
    return {
        "height_T": base.height,
        "gamma_fraction": base.gamma_fraction,
        "gamma": base.gamma,
        "grid_phase": base.grid_phase,
        "aperture_fraction": base.aperture_fraction,
        "grid_dimension": int(base.indices.size),
        "jet_order": int(jet_order),
        "selected_slice_dimension": int(inclusion.shape[1]),
        "candidate_alpha": alpha,
        "theta": theta,
        "kappa": kappa,
        "eta": theta * kappa,
        "q_eta": support.value,
        "q_eta_over_kappa": support.value / kappa,
        "dual_mu": support.dual_mu,
        "boundary_slice": support.boundary_slice,
        "active_prime_powers": base.active_prime_powers,
    }


def adversarial_scan(
    *,
    heights: Sequence[float],
    gamma_fractions: Sequence[float],
    grid_phases: Sequence[float],
    aperture_fractions: Sequence[float],
    jet_orders: Sequence[int],
    alphas: Sequence[float],
    thetas: Sequence[float],
    iterations: int = 64,
) -> dict[str, Any]:
    """Run a deterministic Cartesian scan, retaining all valid points."""
    rows: list[dict[str, Any]] = []
    skipped_bases = 0
    skipped_points = 0
    base_count = 0
    for height in heights:
        for gamma_fraction in gamma_fractions:
            for aperture_fraction in aperture_fractions:
                for grid_phase in grid_phases:
                    try:
                        base = build_floating_base(
                            float(height),
                            gamma_fraction=float(gamma_fraction),
                            aperture_fraction=float(aperture_fraction),
                            grid_phase=float(grid_phase),
                        )
                    except ValueError:
                        skipped_bases += 1
                        continue
                    base_count += 1
                    for jet_order in jet_orders:
                        for alpha in alphas:
                            for theta in thetas:
                                try:
                                    row = evaluate_floating_point(
                                        base,
                                        alpha=float(alpha),
                                        jet_order=int(jet_order),
                                        theta=float(theta),
                                        iterations=iterations,
                                    )
                                except ValueError:
                                    skipped_points += 1
                                    continue
                                rows.append(row)
    if not rows:
        raise ValueError("the scan produced no valid carrier slices")
    by_ratio = sorted(rows, key=lambda row: row["q_eta_over_kappa"])
    by_value = sorted(rows, key=lambda row: row["q_eta"])
    theta_minima = []
    for theta in sorted(set(float(value) for value in thetas)):
        candidates = [row for row in rows if row["theta"] == theta]
        if candidates:
            theta_minima.append(min(
                candidates, key=lambda row: row["q_eta_over_kappa"]
            ))
    return {
        "scope": "floating adversarial scan; signs require interval replay",
        "base_count": base_count,
        "skipped_base_count": skipped_bases,
        "point_count": len(rows),
        "skipped_point_count": skipped_points,
        "negative_point_count_at_tolerance_1e-10": sum(
            row["q_eta"] < -1e-10 for row in rows
        ),
        "minimum_by_q_over_kappa": by_ratio[0],
        "minimum_by_absolute_q": by_value[0],
        "ten_smallest_by_q_over_kappa": by_ratio[:10],
        "minimum_by_theta": theta_minima,
    }


# ---- Rigorous Arb/Acb replay -------------------------------------------------


def _require_flint() -> None:
    if arb is None:
        raise RuntimeError("python-flint is required for interval certificates")


def _q(value: int | Fraction) -> Any:
    value = _as_fraction(value)
    return fmpq(value.numerator, value.denominator)


def _arb_q(value: int | Fraction) -> Any:
    return arb(_q(value))


def _exact_endpoint_kernel(indices: Sequence[int], jet_order: int) -> Any:
    """Exact rational basis of ``sum k^r c_k=0``, returned by RREF."""
    dimension = len(indices)
    if jet_order < 0 or jet_order >= dimension:
        raise ValueError("invalid jet order")
    if jet_order == 0:
        return fmpq_mat(dimension, dimension, [
            1 if i == j else 0
            for i in range(dimension) for j in range(dimension)
        ])
    moments = fmpq_mat(jet_order, dimension, [
        int(indices[column]) ** row
        for row in range(jet_order) for column in range(dimension)
    ])
    reduced, rank = moments.rref()
    if rank != jet_order:
        raise RuntimeError("exact endpoint moment matrix lost rank")
    pivots: list[int] = []
    for row in range(rank):
        pivot = next(
            (column for column in range(dimension)
             if reduced[row, column] != 0),
            None,
        )
        if pivot is None:
            raise RuntimeError("RREF row has no pivot")
        pivots.append(pivot)
    free = [column for column in range(dimension) if column not in pivots]
    basis = fmpq_mat(dimension, len(free))
    for out_column, free_column in enumerate(free):
        basis[free_column, out_column] = 1
        for row, pivot in enumerate(pivots):
            basis[pivot, out_column] = -reduced[row, free_column]
    return basis


def _prime_power_integers(limit: int) -> list[tuple[int, int]]:
    """Return exact ``(n,p)`` pairs for prime powers ``n=p^a <= limit``."""
    sieve = [True] * (limit + 1)
    if limit >= 0:
        sieve[0] = False
    if limit >= 1:
        sieve[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
    answer: list[tuple[int, int]] = []
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        n = p
        while n <= limit:
            answer.append((n, p))
            if n > limit // p:
                break
            n *= p
    return sorted(answer)


def _symmetric_error(radius: Any) -> Any:
    return arb(0, radius.upper())


def _arch_interval(tau: Sequence[Any], length: Any, bits: int) -> Any:
    """Rigorous archimedean sharp matrix, including a geometric tail."""
    pi = arb.pi()
    sine_transform: list[Any] = []
    diagonal_tail_bounds: list[Any] = []
    target = 2.0 ** (-max(32, bits - 16))
    for frequency in tau:
        z = acb(_arb_q(Fraction(1, 4)), frequency / 2)
        value = z.digamma().imag / 2
        diagonal_sum = arb(0)
        index = 0
        while True:
            rate = arb(2 * index) + _arb_q(Fraction(1, 2))
            phase = (acb(-rate, frequency) * length).exp()
            denominator = acb(rate, -frequency)
            value -= (phase / denominator).imag
            diagonal_sum += (phase / (denominator * denominator)).real
            next_rate = rate + 2
            geometric = 1 - (-2 * length).exp()
            tail1 = (-next_rate * length).exp() / (next_rate * geometric)
            tail2 = (-next_rate * length).exp() / (
                next_rate * next_rate * geometric
            )
            if float(tail1.upper()) < target:
                value += _symmetric_error(tail1)
                diagonal_sum += _symmetric_error(tail2)
                diagonal_tail_bounds.append(diagonal_sum)
                break
            index += 1
            if index > 10000:
                raise RuntimeError("rigorous archimedean tail did not converge")
        sine_transform.append(value)

    dimension = len(tau)
    answer = acb_mat(dimension, dimension)
    for i in range(dimension):
        z = acb(_arb_q(Fraction(1, 4)), tau[i] / 2)
        # diagonal_tail_bounds stores the enclosed finite sum plus tail.
        diagonal = (
            length * (z.digamma().real - pi.log())
            + z.polygamma(1).real / 2
            - 2 * diagonal_tail_bounds[i]
        )
        answer[i, i] = acb(diagonal)
        for j in range(i + 1, dimension):
            entry = 2 * (sine_transform[i] - sine_transform[j]) / (
                tau[i] - tau[j]
            )
            answer[i, j] = acb(entry)
            answer[j, i] = acb(entry)
    return answer


def _pole_interval(
    tau: Sequence[Any], indices: Sequence[int], length: Any
) -> Any:
    rows: dict[Fraction, list[Any]] = {}
    for exponent in (Fraction(1, 2), Fraction(-1, 2)):
        vector = []
        for frequency, index in zip(tau, indices):
            rate = acb(_arb_q(exponent), -frequency)
            value = 2 * (rate * length / 2).sinh() / rate
            vector.append(value if index % 2 == 0 else -value)
        rows[exponent] = vector
    plus = rows[Fraction(1, 2)]
    minus = rows[Fraction(-1, 2)]
    dimension = len(tau)
    raw = acb_mat(dimension, dimension)
    for i in range(dimension):
        for j in range(dimension):
            raw[i, j] = (
                minus[i].conjugate() * plus[j]
                + plus[i].conjugate() * minus[j]
            )
    # Explicit Hermitian symmetrization retains the exact matrix and narrows
    # small independent evaluation asymmetries.
    return (raw + raw.transpose().conjugate()) / 2


def _prime_interval(tau: Sequence[Any], length: Any, limit: int) -> Any:
    dimension = len(tau)
    answer = acb_mat(dimension, dimension)
    for n, p in _prime_power_integers(limit):
        shift = arb(n).log()
        weight = arb(p).log() / arb(n).sqrt()
        for i in range(dimension):
            diagonal = (length - shift) * (tau[i] * shift).cos()
            answer[i, i] += 2 * weight * diagonal
            for j in range(i + 1, dimension):
                entry = (
                    (tau[j] * shift).sin() - (tau[i] * shift).sin()
                ) / (tau[i] - tau[j])
                entry *= 2 * weight
                answer[i, j] += entry
                answer[j, i] += entry
    return answer


def _selected_interval_rows(
    tau: Sequence[Any],
    length: Any,
    gamma: Any,
    alpha: Fraction,
    phase: Fraction,
) -> tuple[list[Any], list[Any]]:
    alpha_ball = _arb_q(alpha)
    phase_ball = _arb_q(phase)
    z = acb(gamma, -alpha_ball)
    common = 2 * acb(-arb.pi() * phase_ball, -alpha_ball * length / 2).sin()
    values = [common / (z - frequency) for frequency in tau]
    return [value.real for value in values], [value.imag for value in values]


def _acb_exact_basis(matrix: Any) -> Any:
    return acb_mat(matrix.nrows(), matrix.ncols(), [
        acb(arb(matrix[i, j]))
        for i in range(matrix.nrows()) for j in range(matrix.ncols())
    ])


def _selected_null_basis(
    endpoint: Any, selected_x: Sequence[Any]
) -> tuple[Any, int, Any]:
    """Full interval basis after one exact selected-row pivot elimination."""
    e_basis = _acb_exact_basis(endpoint)
    endpoint_dimension = endpoint.ncols()
    row: list[Any] = []
    for column in range(endpoint_dimension):
        value = arb(0)
        for i in range(endpoint.nrows()):
            value += selected_x[i] * arb(endpoint[i, column])
        row.append(value)
    candidates = [
        (float(abs(value).lower()), column)
        for column, value in enumerate(row)
        if not value.contains(0)
    ]
    if not candidates:
        raise RuntimeError("no selected-row pivot is separated from zero")
    pivot = max(candidates)[1]
    free = [column for column in range(endpoint_dimension) if column != pivot]
    elimination = acb_mat(endpoint_dimension, len(free))
    for output, column in enumerate(free):
        elimination[column, output] = 1
        elimination[pivot, output] = -row[column] / row[pivot]
    basis = e_basis * elimination
    # An interval zero check: exact x*B is zero by construction.  Dependency
    # inflation may widen the balls, but every residual must still contain 0.
    max_radius = arb(0)
    for column in range(basis.ncols()):
        residual = acb(0)
        for i in range(basis.nrows()):
            residual += selected_x[i] * basis[i, column]
        if not residual.contains(0):
            raise RuntimeError("selected-null interval basis lost exact zero")
        max_radius = max(max_radius, abs(residual).upper())
    return basis, pivot, max_radius


@dataclass(frozen=True)
class RigorousFixtureForms:
    gram: Any
    arithmetic_form: Any
    carrier_form: Any
    carrier_vector: Any
    kappa: Any
    dimension: int
    grid_dimension: int
    pivot: int
    selected_null_residual_radius: Any
    parameters: dict[str, Any]


def build_rigorous_fixture_forms(
    height: int,
    *,
    gamma_fraction: int | str | Fraction,
    aperture_fraction: int | str | Fraction,
    grid_phase: int | str | Fraction,
    alpha: int | str | Fraction,
    jet_order: int,
    bits: int = 160,
) -> RigorousFixtureForms:
    """Rebuild the full conditioned finite model with Arb/Acb enclosures."""
    _require_flint()
    if height <= 4:
        raise ValueError("height must exceed 4")
    gamma_fraction_q = _as_fraction(gamma_fraction)
    aperture_q = _as_fraction(aperture_fraction)
    phase_q = _as_fraction(grid_phase)
    alpha_q = _as_fraction(alpha)
    if not Fraction(1) < gamma_fraction_q < Fraction(2):
        raise ValueError("gamma_fraction must lie in (1,2)")
    if not Fraction(-1, 2) <= phase_q <= Fraction(1, 2):
        raise ValueError("phase must lie in [-1/2,1/2]")
    if not Fraction(0) < alpha_q < Fraction(1, 2):
        raise ValueError("alpha must lie in (0,1/2)")

    previous_precision = ctx.prec
    ctx.prec = bits
    try:
        length = arb(height).log()
        spacing = 2 * arb.pi() / length
        # The integer aperture decision is made exactly from the same rational
        # decimal input used by the scout.  Its floor is then checked by Arb.
        approximate_half = math.floor(
            float(aperture_q) * height
            / (2 * math.pi / math.log(height))
        )
        half_count = int(approximate_half)
        if half_count < 2:
            raise ValueError("aperture leaves fewer than five grid nodes")
        exact_cut = _arb_q(aperture_q) * height / spacing
        if not (exact_cut > half_count and exact_cut < half_count + 1):
            raise RuntimeError("interval aperture floor is not certified")
        indices = list(range(-half_count, half_count + 1))
        gamma = _arb_q(gamma_fraction_q) * height
        tau = [
            gamma + spacing * _arb_q(Fraction(index) + phase_q)
            for index in indices
        ]
        if not tau[0] > height or not tau[-1] < 2 * height:
            raise ValueError("phase-shifted grid is not strictly inside band")

        arch = _arch_interval(tau, length, bits)
        pole = _pole_interval(tau, indices, length)
        prime = _prime_interval(tau, length, height)
        arithmetic = (arch + pole - prime) / (length * length)
        arithmetic = (
            arithmetic + arithmetic.transpose().conjugate()
        ) / 2

        selected_x, selected_y = _selected_interval_rows(
            tau, length, gamma, alpha_q, phase_q
        )
        endpoint = _exact_endpoint_kernel(indices, jet_order)
        if endpoint.ncols() < 2:
            raise ValueError("endpoint jets leave no selected-null direction")
        basis, pivot, null_radius = _selected_null_basis(
            endpoint, selected_x
        )
        adjoint = basis.transpose().conjugate()
        gram = adjoint * basis
        arithmetic_form = adjoint * arithmetic * basis
        y_column = acb_mat(len(indices), 1, [acb(value) for value in selected_y])
        projected_y = adjoint * y_column
        carrier_form = (
            projected_y * projected_y.transpose().conjugate()
        ) * (2 / (length * length))

        solved = gram.solve(projected_y)
        carrier_scalar = (
            projected_y.transpose().conjugate() * solved
        )[0, 0]
        if not carrier_scalar.imag.contains(0):
            raise RuntimeError("carrier scalar lost Hermitian reality")
        kappa = 2 * carrier_scalar.real / (length * length)
        if not kappa.lower() > 0:
            raise RuntimeError("carrier kappa is not separated from zero")
        return RigorousFixtureForms(
            gram=gram,
            arithmetic_form=arithmetic_form,
            carrier_form=carrier_form,
            carrier_vector=projected_y,
            kappa=kappa,
            dimension=basis.ncols(),
            grid_dimension=len(indices),
            pivot=pivot,
            selected_null_residual_radius=null_radius,
            parameters={
                "height_T": height,
                "gamma_fraction": str(gamma_fraction_q),
                "aperture_fraction": str(aperture_q),
                "grid_phase": str(phase_q),
                "alpha": str(alpha_q),
                "jet_order": jet_order,
                "bits": bits,
            },
        )
    finally:
        ctx.prec = previous_precision


def interval_hermitian_ldl_positive(matrix: Any) -> dict[str, Any]:
    """Certify strict positivity with a no-pivot interval ``LDL*`` factor."""
    _require_flint()
    if matrix.nrows() != matrix.ncols():
        raise ValueError("matrix must be square")
    dimension = matrix.nrows()
    lower = [[acb(0) for _ in range(dimension)] for _ in range(dimension)]
    pivots: list[Any] = []
    for j in range(dimension):
        diagonal = matrix[j, j]
        for k in range(j):
            diagonal -= lower[j][k] * pivots[k] * lower[j][k].conjugate()
        if not diagonal.imag.contains(0):
            return {
                "certified_positive": False,
                "failure": "diagonal interval excludes Hermitian reality",
                "failed_pivot": j,
            }
        pivot = diagonal.real
        pivots.append(pivot)
        if not pivot.lower() > 0:
            return {
                "certified_positive": False,
                "failure": "interval LDL pivot is not strictly positive",
                "failed_pivot": j,
                "pivot_interval": _arb_bounds(pivot),
                "certified_pivot_lower_bounds": [
                    float(value.lower()) for value in pivots[:-1]
                ],
            }
        lower[j][j] = 1
        for i in range(j + 1, dimension):
            value = matrix[i, j]
            for k in range(j):
                value -= lower[i][k] * pivots[k] * lower[j][k].conjugate()
            lower[i][j] = value / pivot
    return {
        "certified_positive": True,
        "minimum_ldl_pivot_lower_bound": min(
            float(value.lower()) for value in pivots
        ),
        "pivot_lower_bounds": [float(value.lower()) for value in pivots],
    }


def _arb_bounds(value: Any) -> list[float]:
    return [float(value.lower()), float(value.upper())]


def certify_negative_dual(
    forms: RigorousFixtureForms,
    *,
    theta: int | str | Fraction,
    mu: int | str | Fraction,
    delta: int | str | Fraction,
    arithmetic_shift: int | str | Fraction = 0,
) -> dict[str, Any]:
    """Certify one rational dual witness.

    ``arithmetic_shift`` replaces ``K`` by ``K-shift*I`` and exists only for
    calibration tests.  A research certificate must use the default zero.
    """
    _require_flint()
    theta_q = _as_fraction(theta)
    mu_q = _as_fraction(mu)
    delta_q = _as_fraction(delta)
    shift_q = _as_fraction(arithmetic_shift)
    if not Fraction(0) < theta_q <= Fraction(1):
        raise ValueError("theta must lie in (0,1]")
    if mu_q < 0 or delta_q <= 0 or shift_q < 0:
        raise ValueError("require mu>=0, delta>0, shift>=0")

    previous_precision = ctx.prec
    ctx.prec = int(forms.parameters["bits"])
    try:
        theta_ball = _arb_q(theta_q)
        mu_ball = _arb_q(mu_q)
        delta_ball = _arb_q(delta_q)
        shift_ball = _arb_q(shift_q)
        # Positive definiteness of this form is exactly the claimed Loewner
        # inequality in the nonorthonormal selected-null basis.
        positive_form = (
            (mu_ball * theta_ball * forms.kappa - delta_ball + shift_ball)
            * forms.gram
            - forms.arithmetic_form
            - mu_ball * forms.carrier_form
        )
        positive_form = (
            positive_form + positive_form.transpose().conjugate()
        ) / 2
        ldl = interval_hermitian_ldl_positive(positive_form)
    finally:
        ctx.prec = previous_precision
    certified = bool(ldl["certified_positive"])
    return {
        "scope": (
            "rigorous finite direct-q certificate"
            if shift_q == 0
            else "rigorous shifted calibration; not an arithmetic sign claim"
        ),
        "certified_negative_dual": certified,
        "theta": str(theta_q),
        "mu": str(mu_q),
        "delta": str(delta_q),
        "arithmetic_shift": str(shift_q),
        "conclusion": (
            f"q_(theta*kappa)(K_ar) <= -{delta_q}"
            if certified and shift_q == 0
            else (
                f"q_(theta*kappa)(K_ar-{shift_q}I) <= -{delta_q}"
                if certified else "no certified conclusion"
            )
        ),
        "kappa_interval": _arb_bounds(forms.kappa),
        "dimension": forms.dimension,
        "grid_dimension": forms.grid_dimension,
        "parameters": forms.parameters,
        "ldl": ldl,
    }


def certify_full_carrier_sign(forms: RigorousFixtureForms) -> dict[str, Any]:
    """Enclose the exact ``q_kappa`` Rayleigh scalar of the rank-one carrier.

    This directly encloses one finite boundary slice.  If its lower endpoint
    is positive, feasible-set monotonicity also proves positivity of every
    ``theta<1`` slice for this same fixed matrix.  It does not enclose those
    sub-full values or certify a neighboring parameter or asymptotic family.
    """
    _require_flint()
    previous_precision = ctx.prec
    ctx.prec = int(forms.parameters["bits"])
    try:
        direction = forms.gram.solve(forms.carrier_vector)
        adjoint = direction.transpose().conjugate()
        denominator_ball = (adjoint * forms.gram * direction)[0, 0]
        numerator_ball = (adjoint * forms.arithmetic_form * direction)[0, 0]
        if (not denominator_ball.imag.contains(0)
                or not numerator_ball.imag.contains(0)):
            raise RuntimeError("full-carrier Rayleigh scalar lost reality")
        denominator = denominator_ball.real
        if not denominator.lower() > 0:
            raise RuntimeError("full-carrier Rayleigh denominator is not positive")
        value = numerator_ball.real / denominator
        sign = (
            "strictly_positive" if value.lower() > 0 else
            "strictly_negative" if value.upper() < 0 else
            "unresolved"
        )
        return {
            "scope": "one rigorous finite full-carrier boundary slice",
            "q_kappa_interval": _arb_bounds(value),
            "q_kappa_sign": sign,
            "kappa_interval": _arb_bounds(forms.kappa),
            "dimension": forms.dimension,
            "grid_dimension": forms.grid_dimension,
            "parameters": forms.parameters,
            "uniform_or_subfull_conclusion": False,
        }
    finally:
        ctx.prec = previous_precision


def certify_rational_carrier_state(
    forms: RigorousFixtureForms,
    coefficients: Sequence[tuple[int | str | Fraction, int | str | Fraction]],
    *,
    required_theta: int | str | Fraction,
) -> dict[str, Any]:
    """Certify one explicit rational complex state in the rigorous basis.

    ``coefficients`` are ``(real, imaginary)`` pairs in the nonorthonormal
    selected-null basis used by :func:`build_rigorous_fixture_forms`.  A
    positive lower Rayleigh endpoint and a carrier fraction above
    ``required_theta`` prove one finite arithmetic-admission witness.  This
    does not certify how the rational vector was selected or any neighboring
    parameter value.
    """

    _require_flint()
    theta_q = _as_fraction(required_theta)
    if not Fraction(0) < theta_q <= Fraction(1):
        raise ValueError("required_theta must lie in (0,1]")
    if len(coefficients) != forms.dimension:
        raise ValueError("coefficient dimension differs from fixture")

    previous_precision = ctx.prec
    ctx.prec = int(forms.parameters["bits"])
    try:
        vector = acb_mat(forms.dimension, 1, [
            acb(_arb_q(_as_fraction(real)), _arb_q(_as_fraction(imag)))
            for real, imag in coefficients
        ])
        adjoint = vector.transpose().conjugate()
        denominator_ball = (adjoint * forms.gram * vector)[0, 0]
        arithmetic_ball = (adjoint * forms.arithmetic_form * vector)[0, 0]
        carrier_ball = (adjoint * forms.carrier_form * vector)[0, 0]
        for name, value in (
            ("denominator", denominator_ball),
            ("arithmetic", arithmetic_ball),
            ("carrier", carrier_ball),
        ):
            if not value.imag.contains(0):
                raise RuntimeError(f"{name} scalar lost Hermitian reality")
        denominator = denominator_ball.real
        if not denominator.lower() > 0:
            raise RuntimeError("state norm is not separated from zero")
        value = arithmetic_ball.real / denominator
        fraction = carrier_ball.real / (denominator * forms.kappa)
        carrier_certified = fraction.lower() >= float(theta_q)
        positive_certified = value.lower() > 0
        return {
            "scope": "one rigorous rational carrier-rich arithmetic state",
            "required_theta": str(theta_q),
            "carrier_fraction_interval": _arb_bounds(fraction),
            "rayleigh_interval": _arb_bounds(value),
            "certified_required_carrier": bool(carrier_certified),
            "certified_strictly_positive": bool(positive_certified),
            "certified_arithmetic_admission": bool(
                carrier_certified and positive_certified
            ),
            "kappa_interval": _arb_bounds(forms.kappa),
            "dimension": forms.dimension,
            "grid_dimension": forms.grid_dimension,
            "parameters": forms.parameters,
        }
    finally:
        ctx.prec = previous_precision


def _csv_floats(value: str) -> list[float]:
    return [float(item) for item in value.split(",") if item.strip()]


def _csv_ints(value: str) -> list[int]:
    return [int(item) for item in value.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--heights", default="16,32,64,128")
    parser.add_argument("--gamma-fractions", default="1.25,1.5,1.75")
    parser.add_argument("--grid-phases", default="-0.49,0,0.49")
    parser.add_argument("--apertures", default="0.1,0.2,0.32")
    parser.add_argument("--jet-orders", default="0,1,3,5")
    parser.add_argument("--alphas", default="0.1,0.25,0.4,0.499")
    parser.add_argument("--thetas", default="0.5,0.9,0.99,1")
    parser.add_argument("--iterations", type=int, default=64)
    args = parser.parse_args()
    result = adversarial_scan(
        heights=_csv_floats(args.heights),
        gamma_fractions=_csv_floats(args.gamma_fractions),
        grid_phases=_csv_floats(args.grid_phases),
        aperture_fractions=_csv_floats(args.apertures),
        jet_orders=_csv_ints(args.jet_orders),
        alphas=_csv_floats(args.alphas),
        thetas=_csv_floats(args.thetas),
        iterations=args.iterations,
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
