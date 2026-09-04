import math

import mpmath as mp
import numpy as np

from semilocal_hankel_poisson_gate import (
    finite_trace_defect,
    fourier_hardy_projection,
    hankel_from_negative_coefficients,
    origin_polar_hankel_sequence,
    ratio_logarithmic_derivative,
    reference_multiplier,
    reference_phase,
    relative_sonin_ward_countermodel,
    rho_infinity,
    rho_prime,
    semilocal_origin_pole_order,
    semilocal_ratio,
    semilocal_weil_multiplier,
    smooth_quasi_inner_ward_countermodel,
)


def test_exact_local_factor_normalization_and_unimodularity() -> None:
    with mp.workdps(70):
        for t in (mp.mpf("0"), mp.mpf("0.3"), mp.mpf("2.75"), mp.mpf("11")):
            assert abs(abs(rho_infinity(t)) - 1) < mp.mpf("1e-65")
            for prime in (2, 3, 5):
                assert abs(abs(rho_prime(prime, t)) - 1) < mp.mpf("1e-65")
            value = semilocal_ratio(t)
            assert abs(abs(value) - 1) < mp.mpf("1e-64")
            derivative = ratio_logarithmic_derivative(t)
            expected = semilocal_weil_multiplier(t)
            assert abs(mp.im(derivative)) < mp.mpf("1e-62")
            assert abs(mp.re(derivative) - expected) < mp.mpf("1e-61")


def test_reciprocal_orientation_reverses_the_complete_source() -> None:
    with mp.workdps(60):
        t = mp.mpf("1.375")
        u = semilocal_ratio(t)
        reciprocal_derivative = mp.diff(lambda x: 1 / semilocal_ratio(x), t)
        reciprocal_source = -1j * mp.conj(1 / u) * reciprocal_derivative
        assert abs(reciprocal_source + semilocal_weil_multiplier(t)) < mp.mpf(
            "1e-51"
        )


def test_reference_phase_has_the_repository_reference_multiplier() -> None:
    with mp.workdps(60):
        for t in (mp.mpf("0"), mp.mpf("0.25"), mp.mpf("4")):
            assert abs(mp.diff(reference_phase, t) - reference_multiplier(t)) < mp.mpf(
                "1e-52"
            )


def test_every_exact_finite_cyclic_collocation_erases_the_trace_anomaly() -> None:
    rng = np.random.default_rng(20260901)
    for order in (9, 17, 32):
        projection = fourier_hardy_projection(order)
        phases = rng.normal(size=order)
        unitary = np.diag(np.exp(1j * phases))
        test = np.diag(rng.normal(size=order) + 1j * rng.normal(size=order))
        value = finite_trace_defect(projection, unitary, test)
        assert abs(value) < 2.0e-12
        defect = projection - unitary.conj().T @ projection @ unitary
        assert np.linalg.norm(np.diag(defect), ord=np.inf) < 2.0e-15


def test_semilocal_origin_polar_rank_is_four_not_the_zeta_pole_rank_two() -> None:
    order = semilocal_origin_pole_order((2, 3, 5))
    assert order == 4
    coefficients = origin_polar_hankel_sequence(order, 48)
    hankel = hankel_from_negative_coefficients(coefficients, 18)
    singular_values = np.linalg.svd(hankel, compute_uv=False)
    assert np.count_nonzero(singular_values > 1.0e-10) == order
    assert singular_values[order] < 1.0e-12


def test_smooth_quasi_inner_structure_does_not_give_a_uniform_ward_bound() -> None:
    coarse = smooth_quasi_inner_ward_countermodel(1.0e-3)
    fine = smooth_quasi_inner_ward_countermodel(1.0e-9)
    assert coarse.old_q_floor > 0
    assert fine.old_q_floor > 0
    assert math.isclose(coarse.ward_ratio, 250.0)
    assert math.isclose(fine.ward_ratio, 2.5e8)
    assert fine.enlarged_determinant < 0
    assert math.isclose(fine.ward_ratio / coarse.ward_ratio, 1.0e6)


def test_two_moments_and_h_harmonicity_do_not_remove_the_sonin_obstruction() -> None:
    coarse = relative_sonin_ward_countermodel(1.0e-2)
    fine = relative_sonin_ward_countermodel(1.0e-7)
    assert math.isclose(coarse.rotation_weight + coarse.sonin_weight, 1.0)
    assert math.isclose(fine.rotation_weight + fine.sonin_weight, 1.0)
    assert math.isclose(coarse.old_q_floor, 1.0e-4)
    assert math.isclose(fine.old_q_floor, 1.0e-14)
    assert math.isclose(coarse.ward_ratio, (1 + 1.0e-4) * 99.0)
    assert fine.ward_ratio > 9.999998e6
