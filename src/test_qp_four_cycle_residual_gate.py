import math

import pytest

from qp_four_cycle_hostile_lab import exact_prime_rectangle_fixture
from qp_four_cycle_residual_gate import (
    active_exponent_ledger,
    cross_product_identity_sides,
    cross_conic_factorization_sides,
    cross_conic_identity_sides,
    cross_conic_ledger,
    cycle_ledger,
    determinant_identity_sides,
    is_pairwise_coprime_prime_power_shell,
    local_shift_degree_bound,
    prime_power_base,
    residual_sum_pinning_bound,
    residual_sum_pinning_error,
    shift_factorization_sides,
    shift_identity_sides,
    short_product_pairing,
    tangent_identity_sides,
    tangent_modes,
    weighted_determinant_layer,
    weighted_determinant_layer_bound,
)


def fixture_data():
    fixture = exact_prime_rectangle_fixture()
    return fixture, cycle_ledger(
        fixture.q, fixture.rows, fixture.columns, fixture.colors
    )


def test_exact_prime_fixture_replays_all_residual_identities() -> None:
    fixture, ledger = fixture_data()
    assert ledger.residuals == fixture.residuals
    assert ledger.color_determinant == 6
    assert determinant_identity_sides(ledger)[0] == determinant_identity_sides(ledger)[1]
    assert cross_product_identity_sides(ledger, fixture.colors)[0] == (
        cross_product_identity_sides(ledger, fixture.colors)[1]
    )
    assert all(left == right for left, right in shift_identity_sides(
        ledger, fixture.rows, fixture.columns
    ))
    assert all(left == right for left, right in shift_factorization_sides(
        ledger, fixture.rows, fixture.columns, fixture.colors
    ))
    assert ledger.alternating_sum == 1_208_688
    assert ledger.bilinear_level == 151_086
    assert ledger.row_shifts == (-10, -16)
    assert ledger.column_shifts == (42, 36)

    conic = cross_conic_ledger(fixture.rows, fixture.columns, fixture.colors)
    assert all(
        left == right
        for left, right in cross_conic_identity_sides(
            conic, fixture.colors, ledger.bilinear_level
        )
    )
    (c11, _), (_, c22) = fixture.colors
    s, t = conic.diagonal_products
    assert cross_conic_factorization_sides(
        c11,
        c22,
        conic.cross_color_product,
        s,
        t,
        ledger.bilinear_level,
        conic.cross_difference,
    )[0] == cross_conic_factorization_sides(
        c11,
        c22,
        conic.cross_color_product,
        s,
        t,
        ledger.bilinear_level,
        conic.cross_difference,
    )[1]


def test_residual_sum_is_pinned_to_the_color_rational() -> None:
    fixture, ledger = fixture_data()
    error = residual_sum_pinning_error(ledger, fixture.colors)
    (_, c12), (c21, _) = fixture.colors
    cap = max(abs(value) for value in ledger.residuals)
    bound = residual_sum_pinning_bound(
        cap, abs(ledger.color_determinant), fixture.q**3, c12 * c21
    )
    assert abs(error) <= bound
    assert abs(error) < 0.04
    assert round(ledger.color_determinant * fixture.q**3 / (c12 * c21)) == (
        ledger.alternating_sum
    )


def test_exact_tangent_is_a_row_or_column_swap_mode() -> None:
    column_rows = (5, 7)
    column_columns = (11, 13)
    column_colors = ((17, 7), (19, 5))
    column = cycle_ledger(23, column_rows, column_columns, column_colors)
    assert tangent_modes(column) == ("column_swap",)
    assert column.color_determinant == column.column_shifts[0] == -48
    assert column.bilinear_level == column_columns[0] * column.color_determinant
    assert tangent_identity_sides(
        column, column_rows, column_columns, column_colors
    ) == (0, 0)

    row_rows = (5, 7)
    row_columns = (11, 13)
    row_colors = ((17, 19), (13, 11))
    row = cycle_ledger(23, row_rows, row_columns, row_colors)
    assert tangent_modes(row) == ("row_swap",)
    assert row.color_determinant == row.row_shifts[0] == -60
    assert row.bilinear_level == row_rows[0] * row.color_determinant
    assert tangent_identity_sides(row, row_rows, row_columns, row_colors) == (0, 0)

    fixture, generic = fixture_data()
    assert tangent_modes(generic) == ()
    assert tangent_identity_sides(
        generic, fixture.rows, fixture.columns, fixture.colors
    )[0] != 0


def test_short_zero_cross_ratio_forces_row_or_column_pairing() -> None:
    modulus = 10_000
    assert short_product_pairing(modulus, (3, 3, -2, -2)) == ("rows",)
    assert short_product_pairing(modulus, (3, -2, 3, -2)) == ("columns",)
    assert short_product_pairing(modulus, (1, 1, 1, 1)) == ("rows", "columns")
    with pytest.raises(ValueError):
        short_product_pairing(modulus, (3, 2, 1, 0))


def test_narrow_prime_power_shell_is_pairwise_coprime() -> None:
    assert prime_power_base(2**9) == 2
    assert prime_power_base(17**2) == 17
    assert prime_power_base(12) is None
    assert is_pairwise_coprime_prime_power_shell((101, 103, 107, 11**2))
    assert not is_pairwise_coprime_prime_power_shell((2**8, 2**9, 257))


def test_weighted_fixed_determinant_layer_obeys_divisor_bound() -> None:
    values = (5, 7, 11, 13)
    weights = {5: 0.5, 7: -0.25j, 11: 0.75, 13: -0.3}
    for determinant in (-4, -2, 0, 2, 4):
        actual = weighted_determinant_layer(values, weights, determinant)
        bound = weighted_determinant_layer_bound(values, weights, determinant)
        assert actual <= bound + 1.0e-12


def test_active_scale_is_below_both_square_root_thresholds() -> None:
    ledger = active_exponent_ledger()
    assert ledger["D"] == (16, 33)
    assert ledger["D_over_sqrt_q"] == (-1, 66)
    assert ledger["D_squared_over_q"] == (-1, 33)
    assert ledger["sqrt_D"] == (8, 33)
    assert math.isclose(16 / 33 - 1 / 2, -1 / 66)


def test_local_shift_count_records_only_the_proved_linear_bound() -> None:
    assert local_shift_degree_bound(4_099, 100) == 21
    assert local_shift_degree_bound(399, 100) == 1
    with pytest.raises(ValueError):
        local_shift_degree_bound(-1, 100)
