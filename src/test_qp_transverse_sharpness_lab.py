import math

import numpy as np

from qp_transverse_sharpness_lab import (
    calibrated_residual,
    first_odd_resonance,
    run_transverse_instance,
    solve_finite_transverse_dual,
    solve_finite_transverse_primal,
)


def test_one_coordinate_transverse_primal_dual() -> None:
    nodes = np.array([1.0])
    times = np.array([math.pi, 2.0 * math.pi])
    # t0=pi, D=1 gives v=0 in one coordinate, so use v=1 instead.
    residual = np.array([1.0])
    primal = solve_finite_transverse_primal(nodes, times, residual)
    dual = solve_finite_transverse_dual(nodes, times, residual)
    assert primal.success and dual.success
    assert abs(primal.depth - 1.0) < 1e-10
    assert abs(dual.level - 1.0) < 1e-10


def test_first_odd_resonance() -> None:
    time = first_odd_resonance(0.1, 100.0, 1000.0)
    quotient = time * 0.1 / math.pi
    assert 100.0 <= time <= 1000.0
    assert abs(quotient - round(quotient)) < 1e-12
    assert int(round(quotient)) % 2 == 1


def test_calibrated_residual_zeroes_singleton_coordinate() -> None:
    nodes = np.array([0.1, 0.2])
    time = math.pi / 0.1
    residual = calibrated_residual(nodes, time, 1.0)
    assert abs(residual[0]) < 1e-12


def test_small_actual_instance_brackets_both_events() -> None:
    result = run_transverse_instance(
        40,
        phase_step=0.2,
        max_exchange_iterations=3,
    )
    for event in (result["singleton"], result["broad_interval"]):
        bracket = event["bracket"]
        assert bracket["lower"] <= bracket["upper_guard"]
        assert bracket["dual_equality_residual"] < 1e-6
    assert result["singleton"]["depth"] == 1.0
    assert result["broad_interval"]["probability_depth"] > 0.0
