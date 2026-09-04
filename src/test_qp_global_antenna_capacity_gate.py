import math

import pytest

from qp_global_antenna_capacity_gate import (
    affine_peak_bound,
    distinct_prime_factor_count,
    global_peak_bound_for_half_integer,
    shell_contains_at_most_one_power,
    verify,
)


def test_replay() -> None:
    verify()


def test_factor_count_and_half_integer_bound() -> None:
    assert distinct_prime_factor_count(1) == 0
    assert distinct_prime_factor_count(2 * 3 * 5 * 7) == 4
    assert global_peak_bound_for_half_integer(7) == 7


def test_narrow_shell_ratio() -> None:
    assert shell_contains_at_most_one_power(2, 0.2)
    assert not shell_contains_at_most_one_power(2, math.log(2) / 2)


def test_affine_endpoint_maximum() -> None:
    assert affine_peak_bound(0, 1.0) == 2.0
    assert affine_peak_bound(3, 0.0) == 7.0
    assert affine_peak_bound(3, 1.0) == 2.0


def test_input_guards() -> None:
    with pytest.raises(ValueError):
        distinct_prime_factor_count(0)
    with pytest.raises(ValueError):
        global_peak_bound_for_half_integer(0)
    with pytest.raises(ValueError):
        affine_peak_bound(1, 1.1)

