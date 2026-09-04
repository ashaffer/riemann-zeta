"""Finite Fourier transference for weighted stationary normal-lattice sums.

Everything in this module is a finite identity or exponent ledger.  The
stationary-amplitude estimates discussed in the companion report are not
asserted here as a completed large-sieve theorem.
"""

from __future__ import annotations

from cmath import exp
from dataclasses import dataclass
from fractions import Fraction
from math import pi
from typing import Mapping, Sequence


ComplexCoefficients = Mapping[int, complex]


def e(theta: float) -> complex:
    """Return ``exp(2*pi*i*theta)``."""

    return exp(2j * pi * theta)


def torus_distance(theta: float) -> float:
    """Distance from ``theta`` to the nearest integer."""

    return abs(theta - round(theta))


def trigonometric_polynomial(coefficients: ComplexCoefficients, theta: float) -> complex:
    """Evaluate ``sum_h c_h e(h theta)``."""

    return sum(value * e(index * theta) for index, value in coefficients.items())


def triangular_fejer_coefficients(order: int) -> dict[int, float]:
    """Fourier coefficients of the height-one normalized Fejer kernel."""

    if order <= 0:
        raise ValueError("order must be positive")
    return {
        index: (1.0 / order) * (1.0 - abs(index) / order)
        for index in range(-order + 1, order)
    }


def cyclic_orbit_sum(
    coefficients: ComplexCoefficients,
    alpha: float,
    beta: float,
    modulus: int,
    left_step: int,
    right_step: int,
) -> complex:
    """Return the cyclic orbit in the normal-lattice detector identity."""

    if modulus <= 0:
        raise ValueError("modulus must be positive")
    total = 0j
    for orbit in range(modulus):
        total += trigonometric_polynomial(
            coefficients, alpha - orbit * left_step / modulus
        ) * trigonometric_polynomial(
            coefficients, beta + orbit * right_step / modulus
        )
    return total / modulus


def orbit_distance(
    alpha: float,
    beta: float,
    modulus: int,
    left_step: int,
    right_step: int,
) -> float:
    """Minimum simultaneous affine-height distance along the cyclic orbit."""

    if modulus <= 0:
        raise ValueError("modulus must be positive")
    return min(
        max(
            torus_distance(alpha - orbit * left_step / modulus),
            torus_distance(beta + orbit * right_step / modulus),
        )
        for orbit in range(modulus)
    )


def fejer_orbit_envelope(order: int, eta: float) -> float:
    """The exact elementary envelope ``min(1,(4 N^2 eta^2)^-1)``."""

    if order <= 0:
        raise ValueError("order must be positive")
    if eta <= 0:
        return 1.0
    return min(1.0, 1.0 / (4.0 * order * order * eta * eta))


def finite_dft2(amplitude: Sequence[Sequence[complex]]) -> tuple[tuple[complex, ...], ...]:
    """Normalized two-dimensional DFT on a square finite torus."""

    size = len(amplitude)
    if size == 0 or any(len(row) != size for row in amplitude):
        raise ValueError("amplitude must be a nonempty square matrix")
    scale = 1.0 / (size * size)
    return tuple(
        tuple(
            scale
            * sum(
                amplitude[first][second]
                * e(-(dual_first * first + dual_second * second) / size)
                for first in range(size)
                for second in range(size)
            )
            for dual_second in range(size)
        )
        for dual_first in range(size)
    )


def reconstruct_dft2(
    fourier_coefficients: Sequence[Sequence[complex]], first: int, second: int
) -> complex:
    """Reconstruct one value from the normalized finite DFT."""

    size = len(fourier_coefficients)
    if size == 0 or any(len(row) != size for row in fourier_coefficients):
        raise ValueError("coefficients must be a nonempty square matrix")
    return sum(
        fourier_coefficients[dual_first][dual_second]
        * e((dual_first * first + dual_second * second) / size)
        for dual_first in range(size)
        for dual_second in range(size)
    )


def weighted_normal_lattice_sum(
    coefficients: ComplexCoefficients,
    amplitude: Sequence[Sequence[complex]],
    alpha: float,
    beta: float,
    congruence_modulus: int,
    left_step: int,
    right_step: int,
) -> complex:
    """Direct amplitude-weighted normal-lattice sum.

    The amplitude is read periodically on its finite torus.  Coefficient
    indices themselves remain ordinary integers in the congruence.
    """

    size = len(amplitude)
    if size == 0 or any(len(row) != size for row in amplitude):
        raise ValueError("amplitude must be a nonempty square matrix")
    if congruence_modulus <= 0:
        raise ValueError("congruence modulus must be positive")
    return sum(
        first_value
        * second_value
        * amplitude[first % size][second % size]
        * e(first * alpha + second * beta)
        for first, first_value in coefficients.items()
        for second, second_value in coefficients.items()
        if (second * right_step - first * left_step) % congruence_modulus == 0
    )


def transferred_normal_lattice_sum(
    coefficients: ComplexCoefficients,
    amplitude: Sequence[Sequence[complex]],
    alpha: float,
    beta: float,
    congruence_modulus: int,
    left_step: int,
    right_step: int,
) -> complex:
    """The exact DFT superposition of shifted cyclic orbit sums."""

    fourier = finite_dft2(amplitude)
    size = len(fourier)
    return sum(
        fourier[dual_first][dual_second]
        * cyclic_orbit_sum(
            coefficients,
            alpha + dual_first / size,
            beta + dual_second / size,
            congruence_modulus,
            left_step,
            right_step,
        )
        for dual_first in range(size)
        for dual_second in range(size)
    )


def shifted_eta_fourier_algebra_bound(
    fourier_coefficients: Sequence[Sequence[complex]],
    order: int,
    alpha: float,
    beta: float,
    congruence_modulus: int,
    left_step: int,
    right_step: int,
) -> float:
    """Weighted Fourier-algebra bound using every shifted orbit distance."""

    size = len(fourier_coefficients)
    if size == 0 or any(len(row) != size for row in fourier_coefficients):
        raise ValueError("coefficients must be a nonempty square matrix")
    return float(
        sum(
            abs(fourier_coefficients[dual_first][dual_second])
            * fejer_orbit_envelope(
                order,
                orbit_distance(
                    alpha + dual_first / size,
                    beta + dual_second / size,
                    congruence_modulus,
                    left_step,
                    right_step,
                ),
            )
            for dual_first in range(size)
            for dual_second in range(size)
        )
    )


@dataclass(frozen=True)
class StationaryTransitionLedger:
    q: Fraction
    top_frequency: Fraction
    quadratic_amplitude: Fraction
    fold_width: Fraction
    airy_amplitude: Fraction
    target: Fraction
    fold_amplitude_loss: Fraction
    fold_fourier_spread: Fraction


def critical_stationary_transition_ledger() -> StationaryTransitionLedger:
    """Return critical powers of ``D`` for ``K=H=q/D``."""

    q = Fraction(33, 16)
    top = Fraction(17, 16)
    fold_width = (2 * top - q) / 3
    airy = 2 * q / 3 - top / 3
    target = Fraction(1, 2)
    return StationaryTransitionLedger(
        q=q,
        top_frequency=top,
        quadratic_amplitude=(q - top) / 2,
        fold_width=fold_width,
        airy_amplitude=airy,
        target=target,
        fold_amplitude_loss=airy - target,
        fold_fourier_spread=top - fold_width,
    )
