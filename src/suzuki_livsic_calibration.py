"""High-precision finite-Galerkin calibration of a Suzuki Livsic function.

The analytic target is fixed by

    xi(s) = 1/2 s(s-1) pi^(-s/2) Gamma(s/2) zeta(s),
    L(s)  = xi'(s) / xi(s),
    ell   = L(3/2),
    S_xi(z) = (ell - L(1/2-i z)) / (ell + L(1/2-i z)).

At ``z=i``, ``S_xi(i)=0`` and

    S_xi'(i) = (i/2) rho_xi,       rho_xi = L'(3/2)/L(3/2).

For a completed-Weil Galerkin matrix ``Q`` on ``[-a,a]``, put
``R_sigma=(Q-sigma I)^-1`` and let ``p`` be the Legendre coefficient vector
of ``exp(x)``.  Reflection gives ``pminus[k]=(-1)^k p[k]``.  We calibrate the
single shift by

    rho_a(sigma) = (pminus^T R_sigma p)/(p^T R_sigma p) = rho_xi.

The finite analytic model is

    S_a(z) = (i-z)/(i+z) * I_plus(z)/I_minus(z),
    I_plus(z)  = q(z)^T R_sigma p,
    I_minus(z) = q(z)^T R_sigma pminus,

where ``q(z)`` is the coefficient vector of ``exp(i z x)``.  Thus the
calibration matches the derivative at ``i`` with the stated sign.

This is a finite-Galerkin diagnostic.  Agreement at finitely many probes does
not establish a graph/resolvent limit.  In particular, Schur-class or kernel
positivity of the completed-xi target is RH-equivalent and is explicitly not
inferred here.  The weak imaginary-axis probes are reported separately from
the stronger real and off-axis tests because much of their agreement is a
universal normalized-Cayley effect.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from typing import Callable, Sequence

import mpmath as mp

from spectral_margins import gl_nodes, legvals, spectral_form


def completed_xi(s: complex | mp.mpc | mp.mpf) -> mp.mpc:
    """The completed Riemann xi function with the normalization under test."""

    value = mp.mpc(s)
    return (
        mp.mpf("0.5")
        * value
        * (value - 1)
        * mp.power(mp.pi, -value / 2)
        * mp.gamma(value / 2)
        * mp.zeta(value)
    )


def xi_log_derivative(s: complex | mp.mpc | mp.mpf) -> mp.mpc:
    """Return ``xi'/xi`` using its factored logarithmic derivative."""

    value = mp.mpc(s)
    zeta_value = mp.zeta(value)
    zeta_derivative = mp.diff(mp.zeta, value)
    return (
        1 / value
        + 1 / (value - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(value / 2) / 2
        + zeta_derivative / zeta_value
    )


@dataclass(frozen=True)
class XiLivsicTarget:
    ell: mp.mpf
    rho: mp.mpf
    derivative_at_i: mp.mpc

    @classmethod
    def compute(cls, dps: int = 60) -> "XiLivsicTarget":
        with mp.workdps(dps):
            point = mp.mpf("1.5")
            ell = mp.re(xi_log_derivative(point))
            derivative = mp.re(mp.diff(xi_log_derivative, point))
            rho = derivative / ell
            return cls(+ell, +rho, +(mp.j * rho / 2))

    def characteristic(self, z: complex | mp.mpc | mp.mpf) -> mp.mpc:
        value = mp.mpc(z)
        logarithmic_derivative = xi_log_derivative(
            mp.mpf("0.5") - mp.j * value
        )
        return (self.ell - logarithmic_derivative) / (
            self.ell + logarithmic_derivative
        )


def bisect_sign_change(
    function: Callable[[mp.mpf], mp.mpf],
    left: mp.mpf,
    right: mp.mpf,
    tolerance: mp.mpf,
    max_iterations: int = 300,
) -> mp.mpf:
    """High-precision bisection for a continuous sign-changing function."""

    left = mp.mpf(left)
    right = mp.mpf(right)
    f_left = mp.mpf(function(left))
    f_right = mp.mpf(function(right))
    if f_left == 0:
        return left
    if f_right == 0:
        return right
    if f_left * f_right > 0:
        raise ValueError("root endpoints must bracket a sign change")
    for _ in range(max_iterations):
        midpoint = (left + right) / 2
        f_midpoint = mp.mpf(function(midpoint))
        if f_midpoint == 0 or right - left <= 2 * tolerance:
            return midpoint
        if f_left * f_midpoint < 0:
            right = midpoint
            f_right = f_midpoint
        else:
            left = midpoint
            f_left = f_midpoint
    raise RuntimeError("bisection did not reach the requested tolerance")


def exponential_legendre_coefficients(a: mp.mpf, dimension: int) -> mp.matrix:
    """Exact Legendre coefficients of ``exp(x)`` on ``[-a,a]``."""

    return mp.matrix(
        [
            mp.sqrt(mp.pi * (2 * degree + 1))
            * mp.besseli(mp.mpf(degree) + mp.mpf("0.5"), a)
            for degree in range(dimension)
        ]
    )


def reflected_coefficients(vector: mp.matrix) -> mp.matrix:
    """Apply interval reflection in the Legendre basis."""

    return mp.matrix([(-1) ** degree * vector[degree] for degree in range(vector.rows)])


def _principal_submatrix(matrix: mp.matrix, indices: Sequence[int]) -> mp.matrix:
    size = len(indices)
    block = mp.matrix(size, size)
    for row, source_row in enumerate(indices):
        for column, source_column in enumerate(indices):
            block[row, column] = matrix[source_row, source_column]
    return block


def _subvector(vector: mp.matrix, indices: Sequence[int]) -> mp.matrix:
    return mp.matrix([vector[index] for index in indices])


def _bilinear_dot(left: mp.matrix, right: mp.matrix) -> mp.mpc:
    return mp.fsum(left[index] * right[index] for index in range(left.rows))


def parity_resolvent_energies(
    matrix: mp.matrix, p: mp.matrix, shift: mp.mpf
) -> tuple[mp.mpf, mp.mpf]:
    """Return the even and odd contributions to ``p^T(Q-shift I)^-1p``."""

    energies: list[mp.mpf] = []
    for parity in (0, 1):
        indices = list(range(parity, matrix.rows, 2))
        block = _principal_submatrix(matrix, indices)
        vector = _subvector(p, indices)
        shifted = block - shift * mp.eye(block.rows)
        solution = mp.lu_solve(shifted, vector)
        energies.append(mp.re(_bilinear_dot(vector, solution)))
    return energies[0], energies[1]


def resolvent_ratio(matrix: mp.matrix, p: mp.matrix, shift: mp.mpf) -> mp.mpf:
    """Compute ``rho_a`` through the numerically stable parity decomposition."""

    even_energy, odd_energy = parity_resolvent_energies(matrix, p, shift)
    return (even_energy - odd_energy) / (even_energy + odd_energy)


@dataclass(frozen=True)
class ShiftCalibration:
    spectral_floor: mp.mpf
    spectral_ceiling: mp.mpf
    sigma: mp.mpf
    floor_gap: mp.mpf
    condition_estimate: mp.mpf
    rho_target: mp.mpf
    rho_model: mp.mpf
    rho_residual: mp.mpf
    even_energy: mp.mpf
    odd_energy: mp.mpf


def calibrate_resolvent_ratio(
    matrix: mp.matrix,
    p: mp.matrix,
    rho_target: mp.mpf,
    dps: int = 60,
) -> ShiftCalibration:
    """Calibrate ``sigma`` below the Galerkin floor in logarithmic gap scale."""

    with mp.workdps(dps + 15):
        eigenvalues, _ = mp.eigsy(matrix)
        spectral_floor = eigenvalues[0]
        spectral_ceiling = eigenvalues[eigenvalues.rows - 1]
        scale = max(mp.mpf(1), abs(spectral_floor), abs(spectral_ceiling))
        gap_low = scale * mp.power(10, -max(25, dps // 2))
        gap_high = scale

        def error_at_log_gap(log_gap: mp.mpf) -> mp.mpf:
            gap = mp.exp(log_gap)
            return resolvent_ratio(matrix, p, spectral_floor - gap) - rho_target

        log_low = mp.log(gap_low)
        log_high = mp.log(gap_high)
        low_value = error_at_log_gap(log_low)
        high_value = error_at_log_gap(log_high)
        expansions = 0
        while low_value * high_value > 0 and expansions < 20:
            gap_high *= 10
            log_high = mp.log(gap_high)
            high_value = error_at_log_gap(log_high)
            expansions += 1
        if low_value * high_value > 0:
            raise RuntimeError("the target resolvent ratio is not bracketed below the floor")

        log_gap = bisect_sign_change(
            error_at_log_gap,
            log_low,
            log_high,
            tolerance=mp.power(10, -min(30, dps // 2)),
        )
        floor_gap = mp.exp(log_gap)
        sigma = spectral_floor - floor_gap
        even_energy, odd_energy = parity_resolvent_energies(matrix, p, sigma)
        rho_model = (even_energy - odd_energy) / (even_energy + odd_energy)
        condition_estimate = (spectral_ceiling - sigma) / floor_gap
        return ShiftCalibration(
            spectral_floor=+spectral_floor,
            spectral_ceiling=+spectral_ceiling,
            sigma=+sigma,
            floor_gap=+floor_gap,
            condition_estimate=+condition_estimate,
            rho_target=+rho_target,
            rho_model=+rho_model,
            rho_residual=+abs(rho_model - rho_target),
            even_energy=+even_energy,
            odd_energy=+odd_energy,
        )


class FiniteLivsicModel:
    """Analytic finite-Galerkin Livsic function at one calibrated shift."""

    def __init__(
        self,
        matrix: mp.matrix,
        radius: mp.mpf,
        calibration: ShiftCalibration,
        dps: int = 60,
    ) -> None:
        self.matrix = matrix
        self.radius = mp.mpf(radius)
        self.calibration = calibration
        self.dimension = matrix.rows
        self.dps = dps
        with mp.workdps(dps + 15):
            self.p_plus = exponential_legendre_coefficients(
                self.radius, self.dimension
            )
            self.p_minus = reflected_coefficients(self.p_plus)
            shifted = matrix - calibration.sigma * mp.eye(matrix.rows)
            self.resolvent_p_plus = mp.lu_solve(shifted, self.p_plus)
            self.resolvent_p_minus = mp.lu_solve(shifted, self.p_minus)

            nodes = gl_nodes(max(self.dimension + 4, 96))
            self.nodes: list[mp.mpf] = []
            self.projection_rows: list[list[mp.mpf]] = [
                [] for _ in range(self.dimension)
            ]
            normalizations = [
                mp.sqrt(mp.mpf(2 * degree + 1) / (2 * self.radius))
                for degree in range(self.dimension)
            ]
            for scaled_node, weight in nodes:
                x = self.radius * scaled_node
                values = legvals(self.dimension, scaled_node)
                self.nodes.append(+x)
                for degree in range(self.dimension):
                    self.projection_rows[degree].append(
                        +(weight * self.radius * normalizations[degree] * values[degree])
                    )

    def probe_coefficients(self, z: complex | mp.mpc | mp.mpf) -> mp.matrix:
        """Legendre coefficients of ``exp(i z x)`` by high-order quadrature."""

        value = mp.mpc(z)
        exponentials = [mp.exp(mp.j * value * x) for x in self.nodes]
        return mp.matrix(
            [
                mp.fsum(
                    weight * exponential
                    for weight, exponential in zip(row, exponentials)
                )
                for row in self.projection_rows
            ]
        )

    def characteristic(self, z: complex | mp.mpc | mp.mpf) -> mp.mpc:
        value = mp.mpc(z)
        if value == -mp.j:
            raise ZeroDivisionError("the normalized Livsic function has a pole at -i")
        q = self.probe_coefficients(value)
        integral_plus = _bilinear_dot(q, self.resolvent_p_plus)
        integral_minus = _bilinear_dot(q, self.resolvent_p_minus)
        return (
            (mp.j - value)
            / (mp.j + value)
            * integral_plus
            / integral_minus
        )

    @property
    def derivative_at_i(self) -> mp.mpc:
        return mp.j * self.calibration.rho_model / 2


@dataclass(frozen=True)
class ProbeError:
    label: str
    z: mp.mpc
    model: mp.mpc
    target: mp.mpc
    absolute_error: mp.mpf


@dataclass(frozen=True)
class LivsicCalibrationReport:
    support: float
    dimension: int
    calibration: ShiftCalibration
    derivative_error: mp.mpf
    weak: tuple[ProbeError, ...]
    off_axis: tuple[ProbeError, ...]
    real_rms_error: mp.mpf
    real_max_error: mp.mpf
    real_max_z: mp.mpf
    real_probe_count: int


def compare_probe(
    label: str,
    z: complex | mp.mpc | mp.mpf,
    model: FiniteLivsicModel,
    target: XiLivsicTarget,
) -> ProbeError:
    value = mp.mpc(z)
    model_value = model.characteristic(value)
    target_value = target.characteristic(value)
    return ProbeError(
        label,
        value,
        model_value,
        target_value,
        abs(model_value - target_value),
    )


def build_report(
    support: float,
    dimension: int,
    dps: int,
    target: XiLivsicTarget,
    real_probes: Sequence[mp.mpf],
) -> LivsicCalibrationReport:
    """Assemble, calibrate, and test one completed-Weil Galerkin model."""

    with mp.workdps(dps + 15):
        matrix = spectral_form(support, dimension, dps=dps)
        radius = mp.mpf(str(support)) / 4
        p = exponential_legendre_coefficients(radius, dimension)
        calibration = calibrate_resolvent_ratio(
            matrix, p, target.rho, dps=dps
        )
        model = FiniteLivsicModel(matrix, radius, calibration, dps=dps)
        weak = tuple(
            compare_probe(label, z, model, target)
            for label, z in (("i/4", mp.j / 4), ("2i", 2 * mp.j))
        )
        off_axis = tuple(
            compare_probe(label, z, model, target)
            for label, z in (
                ("14+.5i", 14 + mp.j / 2),
                ("14+2i", 14 + 2 * mp.j),
                ("10+10i", 10 + 10 * mp.j),
            )
        )
        real_errors = [
            compare_probe(f"real-{z}", z, model, target) for z in real_probes
        ]
        maximum = max(real_errors, key=lambda error: error.absolute_error)
        rms = mp.sqrt(
            mp.fsum(error.absolute_error**2 for error in real_errors)
            / len(real_errors)
        )
        return LivsicCalibrationReport(
            support=float(support),
            dimension=dimension,
            calibration=calibration,
            derivative_error=+abs(model.derivative_at_i - target.derivative_at_i),
            weak=weak,
            off_axis=off_axis,
            real_rms_error=+rms,
            real_max_error=+maximum.absolute_error,
            real_max_z=+mp.re(maximum.z),
            real_probe_count=len(real_errors),
        )


def _number(value: mp.mpf | mp.mpc, digits: int = 16) -> str:
    return mp.nstr(value, digits)


def report_row(report: LivsicCalibrationReport) -> dict[str, object]:
    calibration = report.calibration
    weak = {probe.label: probe for probe in report.weak}
    off_axis = {probe.label: probe for probe in report.off_axis}
    return {
        "support": report.support,
        "dimension": report.dimension,
        "spectral_floor": _number(calibration.spectral_floor),
        "sigma": _number(calibration.sigma),
        "floor_gap": _number(calibration.floor_gap),
        "condition_estimate": _number(calibration.condition_estimate),
        "rho_model": _number(calibration.rho_model),
        "rho_residual": _number(calibration.rho_residual),
        "train_derivative_error": _number(report.derivative_error),
        "weak_i_over_4_error": _number(weak["i/4"].absolute_error),
        "weak_2i_error": _number(weak["2i"].absolute_error),
        "strong_14_half_i_error": _number(off_axis["14+.5i"].absolute_error),
        "strong_14_2i_error": _number(off_axis["14+2i"].absolute_error),
        "strong_10_10i_error": _number(off_axis["10+10i"].absolute_error),
        "strong_real_rms_error": _number(report.real_rms_error),
        "strong_real_max_error": _number(report.real_max_error),
        "strong_real_max_z": _number(report.real_max_z),
        "real_probe_count": report.real_probe_count,
        "schur_kernel_status": "RH-equivalent-not-tested",
        "model_status": "finite-Galerkin-diagnostic",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--supports", type=float, nargs="+", default=[1.75, 2.485, 2.996])
    parser.add_argument("--dimensions", type=int, nargs="+", default=[8, 10, 12])
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--real-min", type=float, default=1.0)
    parser.add_argument("--real-max", type=float, default=30.0)
    parser.add_argument("--real-step", type=float, default=1.0)
    args = parser.parse_args()
    if args.dps < 40:
        parser.error("use at least 40 decimal digits near the calibrated floor")
    if not 0 < args.real_step or not args.real_min <= args.real_max:
        parser.error("invalid real-probe grid")

    with mp.workdps(args.dps + 15):
        target = XiLivsicTarget.compute(dps=args.dps)
        count = int(mp.floor((args.real_max - args.real_min) / args.real_step)) + 1
        real_probes = [
            mp.mpf(str(args.real_min)) + index * mp.mpf(str(args.real_step))
            for index in range(count)
        ]

        fieldnames: list[str] | None = None
        writer: csv.DictWriter | None = None
        for support in args.supports:
            for dimension in args.dimensions:
                row = report_row(
                    build_report(support, dimension, args.dps, target, real_probes)
                )
                if writer is None:
                    fieldnames = list(row.keys())
                    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
                    writer.writeheader()
                writer.writerow(row)
                sys.stdout.flush()


if __name__ == "__main__":
    main()
