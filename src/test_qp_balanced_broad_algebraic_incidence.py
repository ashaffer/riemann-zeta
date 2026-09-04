from fractions import Fraction
from itertools import combinations

from qp_balanced_broad_algebraic_incidence import (
    affine_rank,
    alternating_residual_sum,
    balanced_incidence_fibration_ledger,
    broad_twisted_cubic,
    carrier_product,
    color_cross_ratio,
    completion_residuals,
    determinant2,
    every_four_affinely_independent,
    residual_cross_ratio,
    same_color_secant_determinant,
    signed_color_level,
)


def test_exact_additive_and_multiplicative_residual_fiber() -> None:
    q = 101
    center = q**3
    colors = (64, 71, 73, 81)
    product = carrier_product((97, 103), (89, 107))
    residuals = completion_residuals(center, colors, product)

    assert alternating_residual_sum(residuals) == 8 * signed_color_level(
        colors, product
    )
    assert residual_cross_ratio(center, residuals) == color_cross_ratio(colors)
    assert color_cross_ratio(colors) == Fraction(64 * 81, 71 * 73)


def test_balanced_linear_incidence_term_is_the_whole_obstruction() -> None:
    ledger = balanced_incidence_fibration_ledger()
    assert ledger.total_color_exponent == Fraction(73, 16)
    assert ledger.slice_cap_exponent == Fraction(5, 16)
    assert ledger.trivial_incidence_exponent == Fraction(78, 16)
    assert ledger.target_incidence_exponent == Fraction(76, 16)
    assert ledger.mandatory_linear_term_exponent == Fraction(78, 16)
    assert ledger.missing_saving_exponent == Fraction(1, 8)
    assert ledger.endpoint_color_interval_exponent == Fraction(-17, 16)


def test_twisted_cubic_stays_on_one_nonzero_level() -> None:
    # K=((64,-71),(-73,81)) has determinant one and positive adjugate.
    colors = (64, 71, 73, 81)
    constant = 200
    parameters = tuple(range(1, 11))
    products = broad_twisted_cubic(colors, constant, parameters)

    assert 64 * 81 - 71 * 73 == 1
    assert all(determinant2(product) == 0 for product in products)
    assert all(
        signed_color_level(colors, product) == constant for product in products
    )


def test_twisted_cubic_is_ruling_free_and_not_a_plane_packet() -> None:
    colors = (64, 71, 73, 81)
    products = broad_twisted_cubic(colors, 200, range(1, 11))

    for first, second in combinations(products, 2):
        assert same_color_secant_determinant(first, second) != 0
    assert affine_rank(products) == 3
    assert every_four_affinely_independent(products)
