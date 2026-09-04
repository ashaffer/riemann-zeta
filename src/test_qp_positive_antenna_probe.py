import math

import numpy as np

from qp_positive_antenna_probe import (
    _solve_sampled_positive_antenna,
    compare_positive_antenna_cones,
)


def test_coordinate_cap_is_enforced_and_detects_empty_simplex() -> None:
    nodes = np.array([0.7, 1.1, 1.6])
    times = np.linspace(1.0, 17.0, 51)
    solution = _solve_sampled_positive_antenna(
        nodes,
        times,
        coordinate_cap=0.4,
    )
    assert solution is not None
    assert math.isclose(float(np.sum(solution.weights)), 1.0, abs_tol=2e-9)
    assert float(np.max(solution.weights)) <= 0.4 + 2e-9
    assert math.isclose(solution.dual_weight_sum, 1.0, abs_tol=2e-8)
    assert solution.complementarity_residual <= 2e-8

    assert (
        _solve_sampled_positive_antenna(
            nodes,
            times,
            coordinate_cap=0.3,
        )
        is None
    )


def test_nested_cones_have_ordered_levels_on_a_common_pool() -> None:
    nodes = np.array([0.31, 0.3102, 0.77, 1.19, 1.61])
    times = np.linspace(2.0, 81.0, 251)
    pairs = ((0, 1),)
    unrestricted = _solve_sampled_positive_antenna(nodes, times)
    carrier = _solve_sampled_positive_antenna(nodes, times, pairs)
    capped = _solve_sampled_positive_antenna(
        nodes,
        times,
        pairs,
        coordinate_cap=0.3,
    )
    assert unrestricted is not None and carrier is not None and capped is not None
    assert unrestricted.level <= carrier.level + 2e-9
    assert carrier.level <= capped.level + 2e-9
    assert math.isclose(carrier.weights[0], carrier.weights[1], abs_tol=2e-9)
    assert math.isclose(capped.weights[0], capped.weights[1], abs_tol=2e-9)
    assert float(np.max(capped.weights)) <= 0.3 + 2e-9


def test_joint_exchange_retains_order_and_reports_cap() -> None:
    nodes = np.array([0.05, 0.05005, 0.09, 0.13, 0.18])
    center = 80.5
    cap_constant = 5.0
    cap = cap_constant * math.log(center) / center
    brackets = compare_positive_antenna_cones(
        nodes,
        center,
        ((0, 1),),
        cap_constant=cap_constant,
        initial_points=81,
        validation_phase_step=0.5,
        max_iterations=2,
    )
    unrestricted = brackets["unrestricted_positive"]
    carrier = brackets["carrier_positive"]
    capped = brackets["carrier_capped_positive"]
    assert unrestricted.feasible and carrier.feasible and capped.feasible
    assert unrestricted.pool_size == carrier.pool_size == capped.pool_size
    assert unrestricted.lower <= carrier.lower + 2e-8
    assert carrier.lower <= capped.lower + 2e-8
    assert capped.max_coordinate <= cap + 2e-8
    assert capped.cap_violation <= 2e-8
    assert carrier.pair_residual <= 2e-8
    assert capped.pair_residual <= 2e-8
    assert unrestricted.lower <= unrestricted.upper_guard + 2e-8
    assert carrier.lower <= carrier.upper_guard + 2e-8
    assert capped.lower <= capped.upper_guard + 2e-8
