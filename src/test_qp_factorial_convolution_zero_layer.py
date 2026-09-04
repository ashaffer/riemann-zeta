from qp_factorial_convolution_zero_layer import (
    consecutive_shell_scales,
    equal_product_residual_rigidity,
    proportional_dilate_obstruction,
)


def test_equal_product_residual_rigidity() -> None:
    q = 1_000_003
    residuals = (12_345, -54_321, -54_321, 12_345)
    assert equal_product_residual_rigidity(q, residuals)


def test_proportional_dilate_block_is_exact_and_quadratic() -> None:
    q = 1_000_003
    degree = 200
    height = q * degree
    g, h = consecutive_shell_scales(q, 0.2, u=5, v=6)
    ledger = proportional_dilate_obstruction(
        q,
        height,
        u=5,
        v=6,
        g=g,
        h=h,
    )

    assert ledger.color_determinant == 0
    assert len(set(ledger.colors)) == 4
    assert ledger.first_multipliers.count >= 10
    assert ledger.second_multipliers.count >= 10
    assert ledger.off_diagonal_parameter_pairs >= 90
    assert ledger.flat_unit_vector_energy_lower_bound >= 90 / 16

    first = ledger.first_multipliers.lower
    second = ledger.second_multipliers.upper
    values = ledger.collision(first, second)
    assert values[0] * values[1] == values[2] * values[3]

    residual_first = 8 * 5 * 6 * g * first - q**3
    residual_second = 8 * 5 * 6 * h * second - q**3
    assert equal_product_residual_rigidity(
        q,
        (residual_first, residual_second, residual_first, residual_second),
    )
