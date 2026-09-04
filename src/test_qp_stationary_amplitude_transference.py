from math import isclose

from qp_stationary_amplitude_transference import (
    critical_stationary_transition_ledger,
    cyclic_orbit_sum,
    e,
    fejer_orbit_envelope,
    finite_dft2,
    orbit_distance,
    reconstruct_dft2,
    shifted_eta_fourier_algebra_bound,
    transferred_normal_lattice_sum,
    triangular_fejer_coefficients,
    trigonometric_polynomial,
    weighted_normal_lattice_sum,
)


def test_finite_dft_reconstructs_every_amplitude_entry() -> None:
    size = 7
    amplitude = [
        [
            complex((3 * first + 5 * second + 2) % 11, (first * second - 4) % 9)
            for second in range(size)
        ]
        for first in range(size)
    ]
    fourier = finite_dft2(amplitude)
    for first in range(size):
        for second in range(size):
            assert abs(reconstruct_dft2(fourier, first, second) - amplitude[first][second]) < 2.0e-12


def test_unweighted_normal_lattice_detector_is_cyclic_orbit() -> None:
    coefficients = {-2: 0.3, -1: 0.8, 0: 1.1, 1: -0.4, 2: 0.7}
    alpha, beta = 0.173, -0.291
    modulus, left_step, right_step = 5, 2, 3
    direct = sum(
        first_value * second_value * e(first * alpha + second * beta)
        for first, first_value in coefficients.items()
        for second, second_value in coefficients.items()
        if (second * right_step - first * left_step) % modulus == 0
    )
    orbit = cyclic_orbit_sum(
        coefficients, alpha, beta, modulus, left_step, right_step
    )
    assert abs(direct - orbit) < 2.0e-12


def test_amplitude_weighted_sum_equals_shifted_orbit_superposition() -> None:
    size = 8
    amplitude = [
        [
            1.2
            + 0.25 * e((first + 2 * second) / size)
            - 0.1j * e((3 * first - second) / size)
            for second in range(size)
        ]
        for first in range(size)
    ]
    coefficients = {-3: 0.2, -2: -0.1j, -1: 0.7, 0: 1, 1: 0.4j, 2: -0.3}
    parameters = (0.117, -0.223, 7, 3, 4)
    direct = weighted_normal_lattice_sum(coefficients, amplitude, *parameters)
    transferred = transferred_normal_lattice_sum(coefficients, amplitude, *parameters)
    assert abs(direct - transferred) < 3.0e-12


def test_triangular_polynomial_is_height_one_fejer() -> None:
    order = 19
    coefficients = triangular_fejer_coefficients(order)
    assert isclose(trigonometric_polynomial(coefficients, 0).real, 1.0)
    for theta in (0.031, 0.127, -0.219):
        value = trigonometric_polynomial(coefficients, theta)
        assert abs(value.imag) < 1.0e-12
        assert value.real >= -1.0e-12


def test_shifted_eta_fourier_algebra_bound_controls_transferred_sum() -> None:
    order = 6
    coefficients = triangular_fejer_coefficients(order)
    size = 13
    amplitude = [
        [
            0.8 + 0.2 * e((2 * first + second) / size) + 0.15 * e((-first + 3 * second) / size)
            for second in range(size)
        ]
        for first in range(size)
    ]
    alpha, beta = 0.193, -0.314
    modulus, left_step, right_step = 7, 2, 5
    value = transferred_normal_lattice_sum(
        coefficients,
        amplitude,
        alpha,
        beta,
        modulus,
        left_step,
        right_step,
    )
    bound = shifted_eta_fourier_algebra_bound(
        finite_dft2(amplitude),
        order,
        alpha,
        beta,
        modulus,
        left_step,
        right_step,
    )
    assert abs(value) <= bound + 2.0e-12

    eta = orbit_distance(alpha, beta, modulus, left_step, right_step)
    assert 0 <= eta <= 0.5
    assert 0 < fejer_orbit_envelope(order, eta) <= 1


def test_critical_fold_and_fourier_spread_exponents() -> None:
    ledger = critical_stationary_transition_ledger()
    assert ledger.quadratic_amplitude.numerator == 1
    assert ledger.quadratic_amplitude.denominator == 2
    assert ledger.fold_width.numerator == 1
    assert ledger.fold_width.denominator == 48
    assert ledger.airy_amplitude.numerator == 49
    assert ledger.airy_amplitude.denominator == 48
    assert ledger.fold_amplitude_loss.numerator == 25
    assert ledger.fold_amplitude_loss.denominator == 48
    assert ledger.fold_fourier_spread.numerator == 25
    assert ledger.fold_fourier_spread.denominator == 24
