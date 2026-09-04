from qp_four_cycle_multidirection_relation import (
    unequal_capped_hyperbola_block_is_valid,
    restricted_type_interpolation_is_valid,
)


def test_unequal_capped_hyperbola_blocks_exhaustively() -> None:
    for product_limit in range(1, 45):
        for first_cap in range(1, 24):
            for second_cap in range(1, 24):
                for first_length in range(1, product_limit + 1):
                    for second_length in range(
                        1, product_limit // first_length + 1
                    ):
                        assert unequal_capped_hyperbola_block_is_valid(
                            first_length,
                            second_length,
                            product_limit,
                            first_cap,
                            second_cap,
                        )


def test_restricted_type_interpolation_exhaustively() -> None:
    for determinant_width in range(1, 28):
        for height in range(1, 10):
            for n1 in range(1, 9):
                for n2 in range(n1, 10):
                    for n3 in range(n2, 11):
                        for n4 in range(n3, 12):
                            assert restricted_type_interpolation_is_valid(
                                (n1, n2, n3, n4),
                                height,
                                determinant_width,
                            )


def test_interpolation_is_permutation_invariant() -> None:
    supports = (2, 11, 5, 7)
    assert restricted_type_interpolation_is_valid(supports, 3, 17)
    assert restricted_type_interpolation_is_valid(
        tuple(reversed(supports)), 3, 17
    )

