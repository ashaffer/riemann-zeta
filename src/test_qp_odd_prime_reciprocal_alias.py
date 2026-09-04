import pytest

from qp_odd_prime_reciprocal_alias import (
    COLOR_SLOPE,
    ROW_SLOPE,
    alias_entry,
    exact_anchor_is_not_a_prime_power,
    displayed_mass_scales,
    product_increment,
    recentered_alias,
)


def test_exact_recentered_identities() -> None:
    # 15263 is prime and is 2591 modulo 3168.
    alias = recentered_alias(15263)
    assert alias.base_residual == -(3 * alias.q - 1) // 4
    assert alias.slope_defect == 1089
    assert 8 * alias.row_center**2 * alias.color_anchor - alias.q**3 == alias.base_residual
    assert ROW_SLOPE * alias.color_anchor - COLOR_SLOPE * alias.row_center == 1089
    assert exact_anchor_is_not_a_prime_power(alias)


def test_defect_aware_product_formula() -> None:
    alias = recentered_alias(15263)
    for h in (2, 5):
        for ell in (3, 7):
            for translation in (-11, 4, 19):
                for i in (0, 1):
                    for j in (0, 1):
                        a, b, c = alias_entry(alias, h, ell, translation, i, j)
                        predicted = product_increment(alias, i * h, j * ell, translation)
                        assert a * b * c - alias.row_center**2 * alias.color_anchor == predicted


def test_displayed_mass_is_one_translation_factor_below_pair_energy() -> None:
    displayed, pair = displayed_mass_scales(1000, 100)
    assert pair == pytest.approx(999 * displayed)
    # At fan length comparable with the translation length, the deliberately
    # displayed mass is order L^(3/2), whereas the pair energy is L^(5/2).
    # Cross-level rectangles belong to the merged Hankel bound, not this
    # fixed-color ledger.
    displayed2, pair2 = displayed_mass_scales(1000, 1000)
    assert displayed2 < 1000**2
    assert pair2 > 1000**2
