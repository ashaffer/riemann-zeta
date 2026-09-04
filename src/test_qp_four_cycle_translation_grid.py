import pytest

from qp_four_cycle_hostile_lab import is_prime
from qp_four_cycle_translation_grid import (
    explicit_distinct_color_integer_witness,
    explicit_distinct_color_four_cycle_audit,
    explicit_prime_modulus_integer_witness,
    translation_grid_entry,
    translation_grid_product_increment,
)


def test_translation_increment_identity_on_asymmetric_corner() -> None:
    n, r, s, ell, t = 101, 8, 7, 3, -5
    a, b, c = translation_grid_entry(n, r, s, ell, t, 1, 0)
    increment = translation_grid_product_increment(n, r, s, ell, t, 1, 0)
    assert a * b * c - (r * n) ** 2 * (s * n) == increment


def test_explicit_prime_modulus_full_integer_witness() -> None:
    audit = explicit_prime_modulus_integer_witness()
    assert is_prime(audit.q)
    assert audit.completions == 305
    assert audit.colors == (
        40_042_793,
        40_042_688,
        40_042_688,
        40_042_583,
    )
    assert audit.color_determinant == -11_025
    assert audit.geometric_degree_cap == pytest.approx(
        243_253.18037892473, rel=2.0e-15
    )
    assert audit.maximum_absolute_frequency == pytest.approx(
        11.969927537022055, rel=2.0e-14
    )
    assert audit.maximum_absolute_eightfold_residual == 21_241_464_599_893
    assert audit.completion_determinant_ratio == pytest.approx(
        13.823560270669066, rel=2.0e-15
    )
    assert audit.completion_sqrt_degree_ratio == pytest.approx(
        0.6184015590322527, rel=2.0e-15
    )


def test_explicit_distinct_color_witness() -> None:
    audit = explicit_distinct_color_integer_witness()
    assert audit.completions == 323
    assert len(set(audit.colors)) == 4
    assert audit.colors == (
        40_042_793,
        40_042_695,
        40_042_688,
        40_042_590,
    )
    assert audit.color_determinant == -10_290
    assert audit.maximum_absolute_frequency == pytest.approx(
        11.967216594202626, rel=2.0e-14
    )
    assert audit.maximum_absolute_eightfold_residual == 21_236_653_844_293
    assert audit.completion_determinant_ratio == pytest.approx(
        13.663418479555305, rel=2.0e-15
    )


def test_translation_grid_does_not_create_a_finite_four_cycle_violation() -> None:
    audit = explicit_distinct_color_four_cycle_audit()
    assert audit.nodes == 447
    assert audit.entries == 1_532
    assert audit.active_colors == 4
    assert audit.smooth_non_degenerate_four_cycle == pytest.approx(
        122.15963796706342, rel=3.0e-13
    )
    assert audit.smooth_fourth_trace == pytest.approx(
        570.463409693488, rel=3.0e-13
    )
    assert audit.unweighted_non_degenerate_four_cycle == pytest.approx(161.5)
    assert audit.unweighted_fourth_trace == pytest.approx(743.75)
    assert (
        audit.smooth_non_degenerate_four_cycle
        < audit.geometric_degree_cap
    )
