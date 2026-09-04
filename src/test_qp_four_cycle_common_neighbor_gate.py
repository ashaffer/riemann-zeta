from qp_four_cycle_common_neighbor_gate import (
    forced_resonance,
    gcd_reduce_colors,
    residual_difference,
    resonant_product_interval_length,
    resonant_product_residual,
)


def test_exact_residual_difference_identity() -> None:
    result = residual_difference(
        q=101,
        first_row=44,
        second_row=55,
        column=57,
        first_color=55,
        second_color=44,
    )
    assert result.identity_error == 0
    assert result.cross_integer == 0


def test_gcd_reduction_detects_small_denominator_resonance() -> None:
    result = gcd_reduce_colors(44, 55, 65, 52)
    assert result.gcd == 11
    assert result.first_reduced_row == 4
    assert result.second_reduced_row == 5
    assert result.resonant
    assert result.resonance_parameter == 13


def test_large_gcd_forces_resonance() -> None:
    assert forced_resonance(
        row_gcd=100,
        residual_bound=10_000.0,
        minimum_column=30,
    )
    assert not forced_resonance(
        row_gcd=50,
        residual_bound=10_000.0,
        minimum_column=30,
    )


def test_resonant_rows_have_identical_cubic_residual() -> None:
    residual = resonant_product_residual(
        q=101,
        row_gcd=11,
        first_reduced_row=4,
        second_reduced_row=5,
        column=57,
        resonance_parameter=13,
    )
    assert residual == 8 * 44 * 57 * 65 - 101**3
    assert residual == 8 * 55 * 57 * 52 - 101**3


def test_resonant_product_interval_length() -> None:
    # |8*4*5*11*b*h-q^3|<=8800 gives a full b*h interval of length 10.
    assert (
        resonant_product_interval_length(
            residual_bound=8_800,
            row_gcd=11,
            first_reduced_row=4,
            second_reduced_row=5,
        )
        == 10.0
    )
