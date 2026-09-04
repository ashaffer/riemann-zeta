import math

import numpy as np

from qp_kmt_cluster_square_gate import (
    asymptotic_ledger,
    fixed_sum_sign_moments,
    forced_block_size,
    forced_tail_energy_fraction,
    local_positive_radius,
    maximum_separated_points,
    mixture_ledger,
    termwise_covariance_certificate,
)


def test_block_cauchy_for_random_mixture() -> None:
    rng = np.random.default_rng(20260814)
    x = rng.normal(size=9) + 1j * rng.normal(size=9)
    y = np.zeros((9, 31), dtype=complex)
    for row in range(9):
        columns = rng.choice(31, size=5, replace=False)
        y[row, columns] = rng.normal(size=5) + 1j * rng.normal(size=5)
    ledger = mixture_ledger(x, y)
    assert ledger.maximum_tail_support == 5
    assert ledger.carrier_l1 <= ledger.cauchy_upper * (1.0 + 1.0e-12)


def test_critical_rank_forces_macroscopic_block() -> None:
    epsilon = 1.0 / 100.0
    packet_count = 10_000
    assert math.isclose(packet_count, epsilon**-2)
    # With D <= 2 Z and half of each lift assigned to the linear channel,
    # the exact bound is L >= R/4.
    lower = forced_block_size(
        packet_count,
        epsilon,
        linear_fraction=0.5,
        normalization_ratio=2.0,
    )
    assert math.isclose(lower, packet_count / 4.0)


def test_termwise_kmt_floor_grows_at_critical_rank() -> None:
    epsilon = 1.0 / 100.0
    r = int(epsilon**-2)
    block = r // 4
    tail_fraction = forced_tail_energy_fraction(
        r,
        epsilon,
        block,
        linear_fraction=0.5,
        normalization_ratio=2.0,
    )
    assert math.isclose(tail_fraction, 0.5)
    eta = 0.01
    certificate = termwise_covariance_certificate(eta, block, tail_fraction)
    assert certificate > 10.0
    assert certificate > epsilon


def test_local_merge_has_constant_capacity() -> None:
    radius = local_positive_radius(0.2, 0.5)
    assert math.isclose(radius, 5.0 * math.pi / 3.0)
    assert maximum_separated_points(2.0 * radius) == 11


def test_fixed_sum_model_is_locally_good_but_globally_locked() -> None:
    r, mean, off = fixed_sum_sign_moments(100, depth=2)
    assert r == 10_000
    assert math.isclose(mean, -0.02)
    assert math.isclose(off, 3.0 / 9999.0)
    variance = 1.0 - mean * mean
    assert variance > 0.999
    # The average of the R coordinates is pointwise -2/sqrt(R).
    assert math.isclose(mean, -2.0 / math.sqrt(r))


def test_asymptotic_floor_loses_to_every_fixed_power() -> None:
    first = asymptotic_ledger(1.0e3)
    second = asymptotic_ledger(2.0e3)
    assert second["eta_times_rank"] > first["eta_times_rank"]
    assert second["eta_over_epsilon"] > first["eta_over_epsilon"]
