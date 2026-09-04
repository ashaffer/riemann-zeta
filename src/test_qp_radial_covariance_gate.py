import math

import numpy as np

from qp_radial_covariance_gate import (
    all_integer_factor_pair_bound,
    cleaned_negative_sum_lower,
    collision_endpoints,
    divisor_count,
    exponent_ledger,
    fejer_transverse_dual,
    near_reflection_pairs,
    product_window,
    positive_range_lower,
    sampled_pair_block_gram,
)


def test_project_exponent_ledger_has_large_survival_gap() -> None:
    ledger = exponent_ledger(50.0 / 33.0, 0.019)
    assert math.isclose(ledger.collision_pair_exponent, 16.0 / 33.0)
    assert math.isclose(ledger.long_carrier_exponent, 0.981)
    assert ledger.survival_gap > 0.496
    assert ledger.survives


def test_product_window_contains_every_enumerated_pair() -> None:
    Y = 20.5
    B = 35.0
    kappa = 2.0
    values = list(range(12, 32))
    lower, upper = product_window(Y, B, kappa)
    for left, right in near_reflection_pairs(values, Y, B, kappa):
        assert lower <= left * right <= upper


def test_integer_factor_bound_dominates_selected_pairs() -> None:
    Y = 30.5
    B = 55.0
    kappa = 3.0
    values = list(range(16, 50))
    pairs = near_reflection_pairs(values, Y, B, kappa)
    assert len(pairs) <= all_integer_factor_pair_bound(Y, B, kappa)


def test_divisor_count_and_endpoints() -> None:
    assert divisor_count(1) == 1
    assert divisor_count(36) == 9
    assert collision_endpoints(((2, 15), (3, 10), (2, 21))) == {2, 3, 10, 15, 21}


def test_cleaned_event_worst_case_cost() -> None:
    assert cleaned_negative_sum_lower(1000.0, 17) == 983.0


def test_one_sided_range_inequality_replays_half_moment_margin() -> None:
    # U*m=Q/4 leaves strictly more than the Q/(2U) used in the proof.
    Q = 2.0
    U = 4.0
    m = Q / (4.0 * U)
    assert positive_range_lower(Q, U, m) > Q / (2.0 * U)


def test_normalized_pair_block_stays_positive_at_collision() -> None:
    minima = []
    for z in np.linspace(0.0, 1.0, 101):
        eigenvalues = np.linalg.eigvalsh(sampled_pair_block_gram(float(z)))
        minima.append(float(eigenvalues[0]))
    assert min(minima) > 0.001


def test_fejer_transverse_model_has_one_over_dimension_ceiling() -> None:
    order = 37
    angles = np.linspace(0.0, 2.0 * math.pi, 5001)
    values = fejer_transverse_dual(order, angles)
    assert math.isclose(float(values[0]), -0.5, abs_tol=1e-12)
    assert float(np.max(values)) <= 1.0 / (2.0 * (order - 1)) + 1e-12
