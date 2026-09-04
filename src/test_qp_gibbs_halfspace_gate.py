import math

from qp_gibbs_halfspace_gate import (
    fixed_degree_fourier_scale,
    forced_bad_moment,
    limiting_common_tilt_mean,
    limiting_common_tilt_normalization,
    qp_scaling,
    shifted_square_ledger,
    target_epsilon,
)


def test_halfspace_lock_misses_target_by_factor_two() -> None:
    r = 10_000
    epsilon = target_epsilon(r)
    assert math.isclose(epsilon, 0.005)
    assert math.isclose(forced_bad_moment(r), -2.0 * epsilon)


def test_fixed_degree_fourier_scales() -> None:
    r = 10_000
    assert math.isclose(fixed_degree_fourier_scale(r, 1), 0.01)
    assert math.isclose(fixed_degree_fourier_scale(r, 2), 0.0001)
    assert math.isclose(fixed_degree_fourier_scale(r, 3), 0.000001)


def test_shifted_square_is_uniformly_bounded() -> None:
    first = shifted_square_ledger(100)
    second = shifted_square_ledger(10_000)
    assert first.degree_one_count == 199
    assert first.degree_three_count == 99**2
    assert first.total_bound < 2.01
    assert second.total_bound < 2.001


def test_limiting_common_tilt_never_crosses_support_wall() -> None:
    means = [limiting_common_tilt_mean(value) for value in (0.0, 0.5, 1.0, 2.0, 5.0)]
    assert all(value < -1.0 for value in means)
    assert all(left < right for left, right in zip(means, means[1:]))


def test_limiting_partition_function_is_finite_and_positive() -> None:
    assert math.isclose(limiting_common_tilt_normalization(0.0), 1.0)
    for value in (0.5, 1.0, 2.0, 5.0):
        normalization = limiting_common_tilt_normalization(value)
        assert 0.0 < normalization < 1.0


def test_qp_critical_packet_scaling() -> None:
    ledger = qp_scaling(1000.0, 0.019)
    assert math.isclose(
        ledger["packet_count"], 0.25 / ledger["epsilon"] ** 2, rel_tol=1.0e-12
    )
    assert math.isclose(ledger["fourier_scale"], 2.0 * ledger["epsilon"])
    assert math.isclose(ledger["forced_bad_moment"], -2.0 * ledger["epsilon"])
    assert math.isclose(ledger["packet_exponent"], 0.038)
