import math

import numpy as np

from qp_positive_weight_carrier_probe import (
    _solve_sampled_positive_carrier,
    attained_fixed_length_event,
    canonical_reflected_pairs,
    source_phase_lift_control,
)
from qp_radialization_lab import primes_in_shell


def test_canonical_actual_matching_fixture() -> None:
    primes, signed = primes_in_shell(254.5, 0.2)
    pairs = canonical_reflected_pairs(signed, 254.5)
    assert {(int(primes[i]), int(primes[j])) for i, j in pairs} == {
        (211, 307),
        (239, 271),
    }


def test_attained_event_uses_raw_mass_normalization() -> None:
    signed = np.array([-0.3, -0.2, 0.1, 0.25])
    event = attained_fixed_length_event(
        signed,
        100.5,
        2,
        source_points=31,
        profile="pair",
    )
    nodes = np.abs(signed)
    source_sum = float(
        np.sum(np.cos(nodes[event.start : event.start + event.length] * event.time))
    )
    assert math.isclose(event.depth, -source_sum / event.length, abs_tol=1e-12)
    assert math.isclose(event.mass, -source_sum / 100.0, abs_tol=1e-12)


def test_sampled_positive_carrier_lp_and_unpaired_infeasibility() -> None:
    nodes = np.array([1.0])
    direction = np.array([1.0])
    solution = _solve_sampled_positive_carrier(
        nodes,
        direction,
        np.array([math.pi]),
        (),
        unpaired_only=False,
    )
    assert solution is not None
    weights, rho = solution
    assert np.allclose(weights, [1.0])
    assert math.isclose(rho, 1.0, abs_tol=1e-10)

    paired_nodes = np.array([1.0, 1.0 + 1e-6])
    paired_direction = np.ones(2)
    assert (
        _solve_sampled_positive_carrier(
            paired_nodes,
            paired_direction,
            np.array([math.pi]),
            ((0, 1),),
            unpaired_only=True,
        )
        is None
    )


def test_unpaired_face_cannot_improve_sampled_optimum() -> None:
    nodes = np.array([0.8, 0.80001, 1.3])
    direction = np.array([0.6, 0.6, 1.0])
    times = np.linspace(2.0, 14.0, 41)
    pairs = ((0, 1),)
    full = _solve_sampled_positive_carrier(
        nodes,
        direction,
        times,
        pairs,
        unpaired_only=False,
    )
    unpaired = _solve_sampled_positive_carrier(
        nodes,
        direction,
        times,
        pairs,
        unpaired_only=True,
    )
    assert full is not None and unpaired is not None
    full_weights, full_rho = full
    _, unpaired_rho = unpaired
    assert math.isclose(full_weights[0], full_weights[1], abs_tol=1e-10)
    assert unpaired_rho >= full_rho - 1e-10


def test_source_phase_lift_preserves_coordinatewise_source_values() -> None:
    signed = np.array([-0.19, -0.13, -0.07, 0.06, 0.12, 0.18])
    source_time = 97.0
    lifted = source_phase_lift_control(signed, source_time, seed=42)
    assert np.array_equal(np.signbit(lifted), np.signbit(signed))
    assert np.allclose(
        np.cos(np.abs(lifted) * source_time),
        np.cos(np.abs(signed) * source_time),
        atol=2e-13,
    )
    assert not np.allclose(lifted, signed)
