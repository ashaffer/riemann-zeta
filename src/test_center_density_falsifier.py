import pytest

from center_density_falsifier import deterministic_fixture


def test_modulation_is_visible_to_counts_but_removed_by_cell_weights() -> None:
    metrics = deterministic_fixture()
    # The normalized counting measure sees the prescribed -kappa/2 mode.
    assert metrics.unweighted_source_real == pytest.approx(-0.1, abs=2e-4)
    # Voronoi lengths reconstruct Lebesgue measure, whose selected mode is 0.
    assert abs(metrics.voronoi_source_real) < 2e-4


def test_odd_half_grid_retains_a_unit_bragg_peak() -> None:
    metrics = deterministic_fixture()
    assert metrics.bragg_modulus > 1 - 1e-12
    assert metrics.snap_displacement < 4e-7
    assert metrics.maximum_gap < 2e-4
