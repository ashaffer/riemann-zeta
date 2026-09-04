import math

import numpy as np

from qp_four_cycle_hostile_lab import (
    BlockedLatinInvariants,
    FourCycleCore,
    blocked_latin_invariants,
    centered_fourier_amplitude,
    dephasing_error,
    exact_prime_rectangle_fixture,
    is_prime,
    rectangle_value_and_gradient,
)


def test_blocked_latin_separates_trace_from_operator_target() -> None:
    data: BlockedLatinInvariants = blocked_latin_invariants(25)
    degree_cap = 25**2
    assert data.color_degree == degree_cap
    assert data.frobenius_sq == degree_cap
    assert data.operator_norm == degree_cap ** 0.25
    assert data.fourth_trace == 25**3
    assert data.nondegenerate_four_cycle == 25 * 24**2
    assert data.nondegenerate_four_cycle > 20 * degree_cap


def test_centered_transform_is_positive_on_inner_core_and_dephases() -> None:
    frequencies = np.linspace(-12.0, 12.0, 49)
    amplitudes = centered_fourier_amplitude(frequencies, quadrature_order=192)
    assert np.min(amplitudes) > 0.7
    assert dephasing_error(7.25) < 2.0e-15


def small_core() -> FourCycleCore:
    # Matrix entries are z_0, z_1 / z_1, z_0.  Its sole geometric rectangle
    # has the alternating two-color pattern.
    return FourCycleCore(
        q=5,
        aperture=1.5,
        width=0.2,
        cutoff=1.0,
        values=np.array([2, 3], dtype=np.int64),
        rows=np.array([0, 0, 1, 1], dtype=np.int32),
        columns=np.array([0, 1, 0, 1], dtype=np.int32),
        colors=np.array([0, 1, 1, 0], dtype=np.int32),
        weights=np.ones(4),
    )


def test_rectangle_identity_on_two_by_two_core() -> None:
    core = small_core()
    vector = np.array([0.6, 0.8])
    value, trace, _ = rectangle_value_and_gradient(core, vector)
    matrix = np.array([[0.6, 0.8], [0.8, 0.6]])
    gram = matrix.T @ matrix
    expected_trace = float(np.trace(gram @ gram))
    expected_q = 4.0 * (0.6 * 0.8) ** 2
    assert math.isclose(trace, expected_trace, rel_tol=1.0e-13)
    assert math.isclose(value, expected_q, rel_tol=1.0e-13)


def test_rectangle_gradient_matches_finite_difference() -> None:
    core = small_core()
    vector = np.array([0.6, 0.8])
    _, _, gradient = rectangle_value_and_gradient(core, vector)
    assert gradient is not None
    step = 1.0e-6
    for coordinate in range(2):
        direction = np.zeros(2)
        direction[coordinate] = step
        plus, _, _ = rectangle_value_and_gradient(
            core, vector + direction, with_gradient=False
        )
        minus, _, _ = rectangle_value_and_gradient(
            core, vector - direction, with_gradient=False
        )
        finite_difference = (plus - minus) / (2.0 * step)
        assert math.isclose(
            gradient[coordinate], finite_difference, rel_tol=2.0e-9, abs_tol=2.0e-9
        )


def test_exact_prime_rectangle_has_constant_determinant() -> None:
    fixture = exact_prime_rectangle_fixture()
    entries = (
        *fixture.rows,
        *fixture.columns,
        fixture.colors[0][0],
        fixture.colors[0][1],
        fixture.colors[1][0],
        fixture.colors[1][1],
    )
    assert all(is_prime(value) for value in entries)
    center = fixture.q / 2.0
    assert all(abs(math.log(value / center)) < 0.2 for value in entries)
    assert fixture.color_determinant == 6
    assert max(abs(value) for value in fixture.frequencies) < 0.7
