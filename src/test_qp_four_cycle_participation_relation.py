from fractions import Fraction

from qp_four_cycle_participation_relation import (
    capped_hyperbola_block_is_valid,
    direct_sum_product_band_barrier,
    primitive_rank_one_directions,
)


def test_capped_hyperbola_dyadic_inequality_exhaustively() -> None:
    for product_limit in range(1, 80):
        for participation in range(1, 80):
            for first_length in range(1, product_limit + 1):
                for second_length in range(1, product_limit // first_length + 1):
                    assert capped_hyperbola_block_is_valid(
                        first_length,
                        second_length,
                        product_limit,
                        participation,
                    )


def test_primitive_rank_one_direction_count_has_quadratic_log_scale() -> None:
    counts = [len(primitive_rank_one_directions(height)) for height in range(1, 7)]
    assert counts == [16, 48, 112, 192, 320, 448]
    # A deliberately generous finite reflection of O(R^2 log(2R)).
    for height, count in enumerate(counts, start=1):
        assert count <= 20 * height * height * (height.bit_length() + 1)


def test_direct_sum_product_band_barrier_is_exact() -> None:
    ledger = direct_sum_product_band_barrier(block_side=9, block_count=11)
    assert ledger.coordinate_count == 99
    assert ledger.product_limit == 81
    assert ledger.input_norm_squared == 1
    assert ledger.input_fourth_power_sum == Fraction(1, 99)
    assert ledger.bilinear_value == 9
    assert ledger.bilinear_value == ledger.square_root_product_limit
