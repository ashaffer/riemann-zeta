"""Fail-fast test for metric-shift versus boundary-phase covariance.

Suzuki's finite-window construction uses the positive metric

    T_s = A - s I,                 s < inf spec(A),

and deficiency vectors determined by ``T_s v_+ = exp(x)`` and
``T_s v_- = exp(-x)``.  Its characteristic function has the form

    W_s(theta, z)
      = (z-i) int v_+(x) exp(i z x) dx
        + exp(i theta) (z+i) int v_-(x) exp(i z x) dx.

For real ``z`` define the required boundary phasor

    E_s(z) = -(z-i) I_+(z) / ((z+i) I_-(z)).

Then ``z`` is a zero of ``W_s(theta, .)`` exactly when
``E_s(z) = exp(i theta)``.  Consequently one target phase makes every selected
reference zero ``z_j`` a target zero only if all values ``E_t(z_j)`` agree
(and this condition is also sufficient for that one-sided inclusion).
Equality of complete zero sets additionally requires that the target have no
extra zeros.  This module measures the decisive necessary obstruction
directly.

The default experiment includes three deliberately distinct models:

* a scalar metric, where covariance is exact (positive control);
* the genuine Dirichlet energy ``int (|u'|^2 + alpha |u|^2)``;
* optionally, the repository's completed-Weil Legendre Galerkin matrix.

The last item is a Galerkin shadow of Suzuki's construction, not a certified
discretization of the unbounded self-adjoint extensions.  A failure there
does not refute the infinite-dimensional expectation; it rules out only the
naive claim that Hilbert-space isomorphism alone forces a constant phase
remapping in this finite model.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander


_TWO_PI = 2.0 * np.pi


def bisect_sign_change(
    function: Callable[[float], float],
    left: float,
    right: float,
    f_left: float,
    f_right: float,
    tolerance: float = 1e-14,
    max_iterations: int = 100,
) -> float:
    """Locate a bracketed real root without an optional SciPy dependency."""

    if f_left == 0.0:
        return float(left)
    if f_right == 0.0:
        return float(right)
    if f_left * f_right > 0.0:
        raise ValueError("root endpoints must bracket a sign change")
    for _ in range(max_iterations):
        midpoint = (left + right) / 2.0
        f_midpoint = float(function(midpoint))
        if f_midpoint == 0.0 or right - left <= 2.0 * tolerance:
            return float(midpoint)
        if f_left * f_midpoint < 0.0:
            right = midpoint
            f_right = f_midpoint
        else:
            left = midpoint
            f_left = f_midpoint
    return float((left + right) / 2.0)


def hermitian_part(matrix: np.ndarray) -> np.ndarray:
    """Remove floating-point skew-Hermitian noise."""

    matrix = np.asarray(matrix, dtype=complex)
    return (matrix + matrix.conj().T) / 2.0


def scalar_coercive_metric(dimension: int, value: float = 5.0) -> np.ndarray:
    """Return the scalar positive metric used as an exact covariance control."""

    if dimension < 2:
        raise ValueError("dimension must be at least two")
    if value <= 0:
        raise ValueError("value must be positive")
    return value * np.eye(dimension)


def diagonal_coercive_metric(dimension: int) -> np.ndarray:
    """A transparent algebraic anisotropic metric in the Legendre basis.

    The normalized Legendre mode of degree ``k`` has energy
    ``2 + (k+1)^2``.  Thus the model is coercive with lower bound three and
    has an explicitly non-scalar spectral profile.
    """

    if dimension < 2:
        raise ValueError("dimension must be at least two")
    degrees = np.arange(dimension, dtype=float)
    return np.diag(2.0 + (degrees + 1.0) ** 2)


def dirichlet_energy_metric(
    dimension: int, radius: float, mass: float = 1.0
) -> np.ndarray:
    """Galerkin matrix of ``int(|u'|^2 + mass |u|^2)`` on ``H_0^1``.

    In the orthonormal Dirichlet sine basis on ``[-radius, radius]`` the
    eigenvalues are ``(n*pi/(2*radius))^2 + mass``, ``n >= 1``.  This is a
    bona fide coercive continuum energy.  The operator ``i d/dx`` is symmetric
    on its compactly supported interior core for the induced inner product.
    """

    if dimension < 2:
        raise ValueError("dimension must be at least two")
    if radius <= 0:
        raise ValueError("radius must be positive")
    if mass <= 0:
        raise ValueError("mass must be positive")
    modes = np.arange(1, dimension + 1, dtype=float)
    eigenvalues = (modes * np.pi / (2.0 * radius)) ** 2 + mass
    return np.diag(eigenvalues)


def orthonormal_legendre_values(
    dimension: int, radius: float, scaled_nodes: np.ndarray
) -> np.ndarray:
    """Evaluate the orthonormal Legendre basis on ``[-radius, radius]``."""

    if radius <= 0:
        raise ValueError("radius must be positive")
    values = legvander(np.asarray(scaled_nodes, dtype=float), dimension - 1)
    scales = np.sqrt((2.0 * np.arange(dimension) + 1.0) / (2.0 * radius))
    return values * scales


def orthonormal_dirichlet_sine_values(
    dimension: int, radius: float, scaled_nodes: np.ndarray
) -> np.ndarray:
    """Evaluate the orthonormal Dirichlet sine basis on the interval."""

    if radius <= 0:
        raise ValueError("radius must be positive")
    nodes = radius * np.asarray(scaled_nodes, dtype=float)
    modes = np.arange(1, dimension + 1, dtype=float)
    angles = np.outer((nodes + radius) / (2.0 * radius), modes * np.pi)
    return np.sin(angles) / np.sqrt(radius)


class ShiftedCharacteristic:
    """Finite Galerkin realization of Suzuki's shifted characteristic data."""

    def __init__(
        self,
        metric: np.ndarray,
        radius: float,
        shift: float,
        quadrature_order: int | None = None,
        basis_kind: str = "legendre",
    ) -> None:
        metric = hermitian_part(metric)
        if metric.ndim != 2 or metric.shape[0] != metric.shape[1]:
            raise ValueError("metric must be square")
        if radius <= 0:
            raise ValueError("radius must be positive")
        dimension = metric.shape[0]
        minimum = float(np.linalg.eigvalsh(metric)[0])
        if not shift < minimum:
            raise ValueError("shift must lie strictly below the metric floor")

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
        rhs_plus = basis.conj().T @ (weights * np.exp(nodes))
        rhs_minus = basis.conj().T @ (weights * np.exp(-nodes))
        shifted_metric = metric - shift * np.eye(dimension)

        self.metric = metric
        self.radius = float(radius)
        self.shift = float(shift)
        self.dimension = dimension
        self.basis_kind = basis_kind
        self.metric_floor = minimum
        self.nodes = nodes
        self.weights = weights
        self.basis = basis
        self.v_plus_coefficients = np.linalg.solve(
            shifted_metric, rhs_plus
        )
        self.v_minus_coefficients = np.linalg.solve(
            shifted_metric, rhs_minus
        )
        self.v_plus_shift_derivative_coefficients = np.linalg.solve(
            shifted_metric, self.v_plus_coefficients
        )
        self.v_minus_shift_derivative_coefficients = np.linalg.solve(
            shifted_metric, self.v_minus_coefficients
        )
        self.weighted_v_plus = weights * (
            basis @ self.v_plus_coefficients
        )
        self.weighted_v_minus = weights * (
            basis @ self.v_minus_coefficients
        )
        self.weighted_v_plus_shift_derivative = weights * (
            basis @ self.v_plus_shift_derivative_coefficients
        )
        self.weighted_v_minus_shift_derivative = weights * (
            basis @ self.v_minus_shift_derivative_coefficients
        )

    def fourier_integrals(
        self, z: float | complex | np.ndarray, chunk_size: int = 512
    ) -> tuple[np.ndarray, np.ndarray]:
        """Return ``(I_+(z), I_-(z))`` in bounded-memory chunks."""

        values = np.asarray(z, dtype=complex)
        shape = values.shape
        flat = values.reshape(-1)
        plus = np.empty(flat.size, dtype=complex)
        minus = np.empty(flat.size, dtype=complex)
        for start in range(0, flat.size, chunk_size):
            stop = min(start + chunk_size, flat.size)
            exponentials = np.exp(
                1j * np.outer(flat[start:stop], self.nodes)
            )
            plus[start:stop] = exponentials @ self.weighted_v_plus
            minus[start:stop] = exponentials @ self.weighted_v_minus
        return plus.reshape(shape), minus.reshape(shape)

    def phase_velocity(self, z: float | np.ndarray) -> np.ndarray:
        """Derivative of ``arg E_s(z)`` with respect to the metric shift.

        Since ``d(T_s^{-1})/ds = T_s^{-2}``, logarithmic
        differentiation gives

        ``d log(E_s)/ds = I_+' / I_+ - I_-' / I_-``.

        A differentiable constant phase remapping can preserve several fixed
        zeros only if this imaginary part has the same value at every zero.
        """

        values = np.asarray(z, dtype=float)
        shape = values.shape
        flat = values.reshape(-1)
        plus, minus = self.fourier_integrals(values)
        plus_derivative = np.empty(flat.size, dtype=complex)
        minus_derivative = np.empty(flat.size, dtype=complex)
        chunk_size = 512
        for start in range(0, flat.size, chunk_size):
            stop = min(start + chunk_size, flat.size)
            exponentials = np.exp(
                1j * np.outer(flat[start:stop], self.nodes)
            )
            plus_derivative[start:stop] = (
                exponentials @ self.weighted_v_plus_shift_derivative
            )
            minus_derivative[start:stop] = (
                exponentials @ self.weighted_v_minus_shift_derivative
            )
        plus_derivative = plus_derivative.reshape(shape)
        minus_derivative = minus_derivative.reshape(shape)
        if np.any(np.abs(plus) < 1e-14) or np.any(np.abs(minus) < 1e-14):
            raise FloatingPointError("phase velocity denominator is too small")
        return np.imag(
            plus_derivative / plus - minus_derivative / minus
        )

    def boundary_phasor(
        self, z: float | np.ndarray, normalize: bool = True
    ) -> np.ndarray:
        """Return the boundary phase required to make real ``z`` a zero."""

        values = np.asarray(z, dtype=float)
        plus, minus = self.fourier_integrals(values)
        numerator = -(values - 1j) * plus
        denominator = (values + 1j) * minus
        if np.any(np.abs(denominator) < 1e-14):
            raise FloatingPointError("boundary phasor denominator is too small")
        phasor = numerator / denominator
        if normalize:
            modulus = np.abs(phasor)
            if np.any(modulus < 1e-14):
                raise FloatingPointError("boundary phasor is too small")
            if np.any(np.abs(modulus - 1.0) > 1e-8):
                raise ValueError(
                    "unit boundary phasors require reflection-symmetric data"
                )
            phasor = phasor / modulus
        return phasor

    def characteristic(
        self, z: float | complex | np.ndarray, phase: float
    ) -> np.ndarray:
        """Evaluate the finite shifted characteristic function."""

        values = np.asarray(z, dtype=complex)
        plus, minus = self.fourier_integrals(values)
        return (
            (values - 1j) * plus
            + np.exp(1j * phase) * (values + 1j) * minus
        )

    def normalized_characteristic_residual(
        self, z: float | np.ndarray, phase: float
    ) -> np.ndarray:
        """Evaluate ``|W|/(|first summand|+|second summand|)``."""

        values = np.asarray(z, dtype=float)
        plus, minus = self.fourier_integrals(values)
        first = (values - 1j) * plus
        second = np.exp(1j * phase) * (values + 1j) * minus
        scale = np.abs(first) + np.abs(second)
        if np.any(scale < 1e-14):
            raise FloatingPointError("characteristic normalization is too small")
        return np.abs(first + second) / scale

    def real_zeros(
        self,
        phase: float,
        z_min: float,
        z_max: float,
        samples: int = 12001,
    ) -> np.ndarray:
        """Locate real zeros from the exact boundary-phase condition.

        For unit phasors, ``imag(E exp(-i phase))`` vanishes both at the
        desired phase and at its antipode.  The positive-real-part check keeps
        only the actual characteristic zeros.
        """

        if not z_min < z_max:
            raise ValueError("z_min must be smaller than z_max")
        if samples < 3:
            raise ValueError("samples must be at least three")
        grid = np.linspace(z_min, z_max, samples)
        rotation = np.exp(-1j * phase)
        rotated = self.boundary_phasor(grid) * rotation
        sine = np.imag(rotated)
        roots: list[float] = []

        def equation(value: float) -> float:
            return float(
                np.imag(self.boundary_phasor(value) * rotation)
            )

        for index in range(samples - 1):
            left, right = grid[index], grid[index + 1]
            f_left, f_right = sine[index], sine[index + 1]
            candidate: float | None = None
            if abs(f_left) < 1e-12:
                candidate = float(left)
            elif f_left * f_right < 0:
                candidate = bisect_sign_change(
                    equation, left, right, f_left, f_right
                )
            if candidate is None:
                continue
            aligned = self.boundary_phasor(candidate) * rotation
            if np.real(aligned) < 0.9:
                continue
            if not roots or abs(candidate - roots[-1]) > 1e-7:
                roots.append(candidate)

        if abs(sine[-1]) < 1e-12:
            aligned = self.boundary_phasor(grid[-1]) * rotation
            if np.real(aligned) > 0.9:
                roots.append(float(grid[-1]))
        return np.asarray(roots, dtype=float)


@dataclass(frozen=True)
class PhaseAlignmentDiagnostic:
    model: str
    dimension: int
    radius: float
    shift_reference: float
    shift_target: float
    reference_phase: float
    root_count: int
    best_target_phase: float
    required_phase_chord_diameter: float
    phase_velocity_range: float
    phase_velocity_std: float
    rms_normalized_residual: float
    max_normalized_residual: float
    nearest_root_rms: float
    nearest_root_max: float
    reference_root_min: float
    reference_root_max: float


def _principal_phase(value: complex) -> float:
    return float(np.mod(np.angle(value), _TWO_PI))


def diagnose_phase_alignment(
    model: str,
    reference: ShiftedCharacteristic,
    target: ShiftedCharacteristic,
    phase: float,
    z_min: float = -24.0,
    z_max: float = 24.0,
    samples: int = 12001,
    root_limit: int = 11,
) -> PhaseAlignmentDiagnostic:
    """Fit one target phase and measure its unavoidable root residual."""

    if reference.dimension != target.dimension:
        raise ValueError("reference and target dimensions must agree")
    roots = reference.real_zeros(phase, z_min, z_max, samples=samples)
    if roots.size < 2:
        raise RuntimeError("the reference window contains too few roots")
    if root_limit > 0 and roots.size > root_limit:
        order = np.argsort(np.abs(roots))[:root_limit]
        roots = np.sort(roots[order])

    required = target.boundary_phasor(roots)
    velocities = reference.phase_velocity(roots)
    mean_phasor = np.mean(required)
    if abs(mean_phasor) < 1e-14:
        best_phasor = 1.0 + 0.0j
    else:
        best_phasor = mean_phasor / abs(mean_phasor)
    best_phase = _principal_phase(best_phasor)
    pairwise = np.abs(required[:, None] - required[None, :])
    chord_diameter = float(np.max(pairwise))
    residuals = target.normalized_characteristic_residual(
        roots, best_phase
    )

    target_roots = target.real_zeros(
        best_phase, z_min, z_max, samples=samples
    )
    if target_roots.size == 0:
        nearest = np.full(roots.shape, np.inf)
    else:
        nearest = np.min(
            np.abs(roots[:, None] - target_roots[None, :]), axis=1
        )

    return PhaseAlignmentDiagnostic(
        model=model,
        dimension=reference.dimension,
        radius=reference.radius,
        shift_reference=reference.shift,
        shift_target=target.shift,
        reference_phase=float(phase),
        root_count=int(roots.size),
        best_target_phase=best_phase,
        required_phase_chord_diameter=chord_diameter,
        phase_velocity_range=float(np.max(velocities) - np.min(velocities)),
        phase_velocity_std=float(np.std(velocities)),
        rms_normalized_residual=float(np.sqrt(np.mean(residuals**2))),
        max_normalized_residual=float(np.max(residuals)),
        nearest_root_rms=float(np.sqrt(np.mean(nearest**2))),
        nearest_root_max=float(np.max(nearest)),
        reference_root_min=float(np.min(roots)),
        reference_root_max=float(np.max(roots)),
    )


def _format(diagnostic: PhaseAlignmentDiagnostic) -> str:
    values: Iterable[str] = (
        diagnostic.model,
        str(diagnostic.dimension),
        f"{diagnostic.radius:.12g}",
        f"{diagnostic.shift_reference:.12g}",
        f"{diagnostic.shift_target:.12g}",
        f"{diagnostic.reference_phase:.12g}",
        str(diagnostic.root_count),
        f"{diagnostic.best_target_phase:.12e}",
        f"{diagnostic.required_phase_chord_diameter:.12e}",
        f"{diagnostic.phase_velocity_range:.12e}",
        f"{diagnostic.phase_velocity_std:.12e}",
        f"{diagnostic.rms_normalized_residual:.12e}",
        f"{diagnostic.max_normalized_residual:.12e}",
        f"{diagnostic.nearest_root_rms:.12e}",
        f"{diagnostic.nearest_root_max:.12e}",
        f"{diagnostic.reference_root_min:.12e}",
        f"{diagnostic.reference_root_max:.12e}",
    )
    return ",".join(values)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dimension", type=int, default=8)
    parser.add_argument("--radius", type=float, default=0.75)
    parser.add_argument("--phase", type=float, default=0.37)
    parser.add_argument("--z-min", type=float, default=-24.0)
    parser.add_argument("--z-max", type=float, default=24.0)
    parser.add_argument("--samples", type=int, default=12001)
    parser.add_argument("--root-limit", type=int, default=11)
    parser.add_argument(
        "--include-completed",
        action="store_true",
        help="also assemble the repository's completed-Weil Galerkin metric",
    )
    parser.add_argument("--support", type=float, default=1.75)
    parser.add_argument("--dps", type=int, default=35)
    parser.add_argument("--completed-reference-shift", type=float, default=0.0)
    parser.add_argument(
        "--completed-safe-reference-shift", type=float, default=-0.05
    )
    parser.add_argument("--completed-target-shift", type=float, default=-0.25)
    args = parser.parse_args()

    header = (
        "model,dimension,radius,shift_reference,shift_target,reference_phase,"
        "root_count,best_target_phase,required_phase_chord_diameter,"
        "phase_velocity_range,phase_velocity_std,"
        "rms_normalized_residual,max_normalized_residual,nearest_root_rms,"
        "nearest_root_max,reference_root_min,reference_root_max"
    )
    print(header)

    scalar = scalar_coercive_metric(args.dimension)
    scalar_reference = ShiftedCharacteristic(scalar, args.radius, 0.0)
    scalar_target = ShiftedCharacteristic(scalar, args.radius, -1.0)
    print(
        _format(
            diagnose_phase_alignment(
                "scalar-control",
                scalar_reference,
                scalar_target,
                args.phase,
                args.z_min,
                args.z_max,
                args.samples,
                args.root_limit,
            )
        ),
        flush=True,
    )

    dirichlet = dirichlet_energy_metric(args.dimension, args.radius)
    dirichlet_reference = ShiftedCharacteristic(
        dirichlet, args.radius, 0.0, basis_kind="dirichlet-sine"
    )
    dirichlet_target = ShiftedCharacteristic(
        dirichlet, args.radius, -1.0, basis_kind="dirichlet-sine"
    )
    print(
        _format(
            diagnose_phase_alignment(
                "dirichlet-energy",
                dirichlet_reference,
                dirichlet_target,
                args.phase,
                args.z_min,
                args.z_max,
                args.samples,
                args.root_limit,
            )
        ),
        flush=True,
    )

    if args.include_completed:
        # Imported lazily so unit tests and the default scout stay lightweight.
        from spectral_margins import spectral_form

        completed = np.asarray(
            spectral_form(
                args.support, args.dimension, dps=args.dps
            ).tolist(),
            dtype=float,
        )
        completed_radius = args.support / 4.0
        completed_reference = ShiftedCharacteristic(
            completed, completed_radius, args.completed_reference_shift
        )
        completed_target = ShiftedCharacteristic(
            completed, completed_radius, args.completed_target_shift
        )
        print(
            _format(
                diagnose_phase_alignment(
                    f"completed-Weil-L{args.support:g}",
                    completed_reference,
                    completed_target,
                    args.phase,
                    args.z_min,
                    args.z_max,
                    args.samples,
                    args.root_limit,
                )
            ),
            flush=True,
        )
        if (
            args.completed_safe_reference_shift
            != args.completed_reference_shift
        ):
            completed_safe_reference = ShiftedCharacteristic(
                completed,
                completed_radius,
                args.completed_safe_reference_shift,
            )
            print(
                _format(
                    diagnose_phase_alignment(
                        f"completed-Weil-safe-L{args.support:g}",
                        completed_safe_reference,
                        completed_target,
                        args.phase,
                        args.z_min,
                        args.z_max,
                        args.samples,
                        args.root_limit,
                    )
                ),
                flush=True,
            )


if __name__ == "__main__":
    main()
