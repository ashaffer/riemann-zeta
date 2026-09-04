import math
import inspect

import numpy as np

from qp_radialization_lab import (
    directional_interval_scan,
    fixed_log_partition_scan,
    maximum_subarray,
    prime_powers_in_shell,
    primes_in_shell,
    ratio_to_power,
    run_instance,
    singleton_resonances,
    solve_finite_antipode,
    solve_finite_antipode_dual,
)


def test_maximum_subarray_with_minimum_length() -> None:
    values = np.array([3.0, -10.0, 4.0, 5.0, -2.0])
    assert maximum_subarray(values, 1) == (9.0, 2, 4)
    assert maximum_subarray(values, 3) == (7.0, 2, 5)
    unavailable = maximum_subarray(values, 6)
    assert unavailable[0] == -math.inf


def test_actual_shell_nodes_are_nonzero() -> None:
    values, nodes = prime_powers_in_shell(100.5, 0.2)
    primes, logs = primes_in_shell(100.5, 0.2)
    assert len(values) >= len(primes) > 0
    assert np.all(nodes > 0.0)
    assert np.all(np.abs(logs) > 0.0)


def test_finite_antipode_primal_dual_fixture() -> None:
    # One coordinate and the legal phase pi give the exact depth one.
    nodes = np.array([1.0])
    times = np.array([math.pi, 2.0 * math.pi])
    primal = solve_finite_antipode(nodes, times)
    dual = solve_finite_antipode_dual(nodes, times)
    assert primal.success and dual.success
    assert abs(primal.depth - 1.0) < 1e-10
    assert abs(dual.level - 1.0) < 1e-10


def test_singleton_floor_is_mass_normalized() -> None:
    logs = np.array([0.1, 0.13])
    count = singleton_resonances(logs, 10.0, 1000.0)
    assert count == 2
    N = 100
    assert 1.0 / N == 0.01


def test_power_ratio() -> None:
    assert ratio_to_power(0.25, 0.5, 2.0) == 1.0
    assert ratio_to_power(0.25, 0.0, 2.0) is None


def test_strip_threshold_is_the_default_and_can_be_unavailable() -> None:
    assert inspect.signature(run_instance).parameters["long_d"].default == 0.019
    primes = np.array([97, 101, 103])
    logs = np.log(primes / 100.5)
    value = directional_interval_scan(
        primes, logs, 100.0, 10.0, 100.0, minimum_count=4
    )
    assert not value.available
    assert value.curvature == 0.0


def test_fixed_log_cells_are_a_subset_of_arbitrary_intervals() -> None:
    primes = np.array([83, 89, 97, 101, 103, 107, 109, 113, 127])
    logs = np.log(primes / 100.5)
    arbitrary = directional_interval_scan(
        primes, logs, 100.0, 10.0, 200.0, minimum_count=1, phase_step=0.2
    )
    cells = fixed_log_partition_scan(
        primes,
        logs,
        100.0,
        10.0,
        200.0,
        shell_width=0.25,
        cell_log_width=0.1,
        phase_step=0.2,
    )
    assert cells.nonempty_cell_count <= cells.cell_count
    assert cells.lower <= arbitrary.upper_guard + 1e-10
    assert cells.upper_guard >= cells.lower


def test_small_actual_prime_instance_has_both_radius_bands() -> None:
    result = run_instance(
        40,
        antipode_phase_step=0.2,
        directional_phase_step=0.15,
        max_exchange_iterations=3,
    )
    high = result["antipode_high_band"]
    full = result["antipode_full_band"]
    assert high["lower"] <= high["upper_guard"]
    assert full["lower"] <= full["upper_guard"]
    assert full["lower"] + 1e-8 >= high["lower"]
    assert len(high["support_times"]) == high["support_size"]
    assert not result["direction_long_interval"]["available"]
