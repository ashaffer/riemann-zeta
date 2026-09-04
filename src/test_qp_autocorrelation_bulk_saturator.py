from fractions import Fraction

from qp_autocorrelation_bulk_saturator import (
    aligned_physical_bulk_ledger,
    bulk_autocorrelation_ledger,
    additive_autocorrelation,
    kloosterman_square_function,
    normalized_separated_autocorrelation,
    primitive_square_function_lower_bound,
    product_convolution,
    separated_support,
)


def test_separated_support_uses_two_nonzero_dyadic_intervals() -> None:
    assert separated_support(8) == (8, 9, 15, 16)


def test_bulk_energy_is_macroscopic_and_normalized() -> None:
    ledger = bulk_autocorrelation_ledger(8)
    assert ledger.fan_norm_squared == 1
    assert ledger.tensor_input_norm_squared == 1
    assert ledger.lower_band_left == 96
    assert ledger.lower_band_right == 192
    assert ledger.normalized_bulk_energy_lower_bound == Fraction(8 * 8, 8192)
    assert ledger.normalized_total_mass == 16


def test_actual_autocorrelation_exceeds_the_symbolic_bulk_lower_bound() -> None:
    length = 8
    coefficients = normalized_separated_autocorrelation(length)
    bulk_energy = sum(
        abs(value) ** 2
        for delta, value in coefficients.items()
        if Fraction(3 * length * length, 2) < delta <= 3 * length * length
    )
    assert bulk_energy >= float(
        bulk_autocorrelation_ledger(length).normalized_bulk_energy_lower_bound
    )


def test_aligned_physical_pullback_is_broad_and_macroscopic() -> None:
    length = 16
    ledger = aligned_physical_bulk_ledger(length)
    assert ledger.row_support_size == 4
    assert ledger.color_support_size == 8
    assert ledger.designated_quadruples == 64
    assert ledger.normalized_bulk_energy_lower_bound == Fraction(1, 128)
    assert ledger.normalized_total_mass == 32
    assert ledger.raw_determinant_lower_bound == 192
    assert ledger.raw_determinant_upper_bound == 384


def test_aligned_congruences_and_determinant_pullback_are_exact() -> None:
    length = 16
    row_frequencies = tuple(
        frequency
        for frequency in separated_support(length)
        if frequency % 2 == 0
    )
    color_frequencies = separated_support(length)
    row_step = 101
    color_step = row_step + 1
    modulus = row_step + 2
    row_bezout = row_step - 1
    color_bezout = row_step

    for frequency in row_frequencies:
        physical_fan = -frequency // 2
        assert (row_bezout * physical_fan * modulus - frequency) % row_step == 0
    for frequency in color_frequencies:
        physical_fan = -frequency
        assert (
            color_bezout * physical_fan * modulus - frequency
        ) % color_step == 0

    high_row = max(row_frequencies)
    high_color = max(color_frequencies)
    low_row = min(row_frequencies)
    low_color = min(color_frequencies)
    delta = high_row * high_color - low_row * low_color
    row_high, row_low = -high_row // 2, -low_row // 2
    color_high, color_low = -high_color, -low_color
    fan_determinant = row_high * color_high - row_low * color_low
    assert delta == 2 * fan_determinant
    assert fan_determinant != 0


def test_aligned_packet_actual_bulk_energy_exceeds_ledger() -> None:
    length = 16
    row_support = tuple(
        frequency
        for frequency in separated_support(length)
        if frequency % 2 == 0
    )
    color_support = separated_support(length)
    row_value = len(row_support) ** -0.5
    color_value = len(color_support) ** -0.5
    coefficients = additive_autocorrelation(
        product_convolution(
            {frequency: row_value for frequency in row_support},
            {frequency: color_value for frequency in color_support},
        )
    )
    bulk_energy = sum(
        abs(value) ** 2
        for delta, value in coefficients.items()
        if Fraction(3 * length * length, 2) < delta <= 3 * length * length
    )
    assert bulk_energy >= float(
        aligned_physical_bulk_ledger(length).normalized_bulk_energy_lower_bound
    )


def test_prime_kloosterman_square_function_is_exact_parseval() -> None:
    coefficients = normalized_separated_autocorrelation(8)
    left, right = kloosterman_square_function(coefficients, 401, multiplier=7)
    assert abs(left - right) < 1e-9


def test_primitive_square_function_retains_a_power_for_large_modulus() -> None:
    length = 8
    lower = primitive_square_function_lower_bound(length, 65537)
    expected = Fraction(length * length, 8192) - Fraction(length**4, 16 * 65537)
    assert lower == expected
    assert lower > 0
