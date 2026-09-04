import math

import pytest

from qp_ltrad_hereditary_gate import (
    cluster_hard_core_exponent_ledger,
    fejer_error_bound,
    finite_scale_ledger,
    hereditary_exponent_ledger,
    triangular_weights,
)


def test_triangular_weights_are_a_probability() -> None:
    weights = triangular_weights(20)
    assert sum(weights) == pytest.approx(1.0)
    assert all(weight > 0.0 for weight in weights)


def test_fejer_floor_on_a_replay_grid() -> None:
    length = 20
    weights = triangular_weights(length)
    for k in range(2001):
        x = 2.0 * math.pi * k / 2000.0
        value = sum(
            weight * math.cos((j + 1) * x) for j, weight in enumerate(weights)
        )
        assert value >= -1.0 / length - 1e-12


def test_fejer_perturbation_budget() -> None:
    length = 100
    band_top = 10.0**6
    perturbation = 1.0 / (length * band_top)
    assert fejer_error_bound(length, band_top, perturbation) == pytest.approx(
        2.0 / length
    )


def test_project_exponents_separate_hard_core_and_long_interval() -> None:
    ledger = hereditary_exponent_ledger()
    assert ledger["hard_is_negligible"] is True
    assert ledger["radial_beats_target"] is True
    assert ledger["hard_exponent"] == pytest.approx(0.029)
    assert ledger["long_interval_exponent"] == pytest.approx(0.981)


def test_finite_scale_has_prime_density_size() -> None:
    # The comparison N^(1-d) < N/log N is asymptotic and turns on late at
    # the small project exponent d=.019.
    scale = 10.0**200
    ledger = finite_scale_ledger(scale)
    assert ledger["node_count"] == math.floor(scale / math.log(scale))
    assert ledger["hard_count"] < ledger["threshold_count"] < ledger["node_count"]
    assert ledger["uniform_mass_scale"] > scale ** (-0.019)


def test_bad_exponent_choice_is_rejected() -> None:
    with pytest.raises(ValueError):
        finite_scale_ledger(10.0**6, d=0.2, c=0.7, eta=0.2)


def test_project_cluster_hard_core_exponent_ledger() -> None:
    ledger = cluster_hard_core_exponent_ledger()
    expected = 28.0 / 121.0 + 6.0 * 0.019 / 11.0
    assert ledger["minimum_cluster_exponent"] == pytest.approx(expected)
    assert ledger["minimum_cluster_exponent"] == pytest.approx(0.2417685950413223)
    assert ledger["nominal_cluster_is_ruled_out"] is True
    assert ledger["literal_fejer_diameter_exponent"] == pytest.approx(0.519)

    # At the threshold, the lower-excursion exponent is exactly -c.
    boundary = cluster_hard_core_exponent_ledger(
        cluster_exponent=ledger["minimum_cluster_exponent"]
    )
    assert boundary["negative_excursion_lower_exponent"] == pytest.approx(-0.019)


def test_cluster_hard_core_ledger_checks_theorem_range() -> None:
    with pytest.raises(ValueError):
        cluster_hard_core_exponent_ledger(aperture=1.0)
    with pytest.raises(ValueError):
        cluster_hard_core_exponent_ledger(radial_exponent=0.0)
    with pytest.raises(ValueError):
        cluster_hard_core_exponent_ledger(
            aperture=1.9,
            radial_exponent=0.31,
        )
    with pytest.raises(ValueError):
        cluster_hard_core_exponent_ledger(cluster_exponent=0.5)
