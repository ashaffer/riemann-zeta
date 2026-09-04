import math

import pytest

from qp_sidon_support_entropy import (
    centered_log_independence_witness,
    florek_mass_bound,
    local_sidon_entropy_lower,
    log_necessary_interval_length,
    necessary_interval_length,
    normalized_depth_guarantee,
    scale_row,
)


def test_entropy_bound_and_exact_inversion() -> None:
    m = 100
    width = 0.2
    length = 10_000.0
    lower = local_sidon_entropy_lower(m, length, width)
    required = necessary_interval_length(m, width, lower)
    assert 0.0 < lower < math.sqrt(m)
    assert required == pytest.approx(length, rel=1e-12)


def test_necessary_length_increases_when_constant_decreases() -> None:
    assert necessary_interval_length(1000, 0.2, 2.0) > necessary_interval_length(
        1000, 0.2, 4.0
    )
    assert log_necessary_interval_length(100_000, 0.2, 2.0) > 1000.0


def test_florek_displayed_geometric_mass_constant() -> None:
    assert florek_mass_bound(2.0, 0.5) == 1024.0
    assert normalized_depth_guarantee(2.0, 0.5) == 1.0 / 1024.0


def test_two_adic_independence_witness() -> None:
    # A nonzero coefficient sum is caught at the denominator prime 2.
    assert centered_log_independence_witness([1, -2], [3, 5], [2, 1]) == (2, -1)
    # Once the sum vanishes, a distinct odd prime base catches the relation.
    assert centered_log_independence_witness([1, -1], [3, 5], [2, 1]) == (3, 2)
    assert centered_log_independence_witness([0, 0], [3, 5], [2, 1]) is None


def test_qp_scale_proxy_is_far_below_target_interpolation_constant() -> None:
    row = scale_row(10**6)
    assert row.local_constant_lower > row.target_constant
    assert row.log_necessary_length_for_target > math.log(row.band_length)
