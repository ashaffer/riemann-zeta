from fractions import Fraction

from qp_primitive_q3_additive_fiber_gate import (
    active_exponent_ledger,
    additive_fourier_coefficient,
    factored_aligned_window_coefficient,
    postnikov_increment,
    primitive_kernel_by_fibres,
    primitive_kernel_by_unit_frequencies,
    second_fermat_quotient,
    symmetric_aligned_unit_window,
    wild_log_coordinate,
    wild_log_from_second_fermat,
)


def test_aligned_symmetric_window_fourier_factorisation() -> None:
    prime = 7
    blocks = 3
    window = symmetric_aligned_unit_window(prime, blocks)
    for frequency in range(prime**3):
        direct = additive_fourier_coefficient(prime**3, window, frequency)
        factored = factored_aligned_window_coefficient(
            prime, blocks, frequency
        )
        assert abs(direct - factored) < 2e-11


def test_primitive_projection_is_additive_unit_frequency_projection() -> None:
    prime = 5
    window = symmetric_aligned_unit_window(prime, 2)
    for value in range(prime**3):
        by_fibres = primitive_kernel_by_fibres(prime, window, value)
        by_frequencies = primitive_kernel_by_unit_frequencies(
            prime, window, value
        )
        assert abs(by_fibres - by_frequencies) < 2e-11


def test_wild_log_is_additive_and_is_second_fermat_coordinate() -> None:
    prime = 7
    modulus = prime**3
    units = [value for value in range(1, 3 * prime) if value % prime]
    for left in units:
        assert wild_log_coordinate(
            prime, left
        ) == wild_log_from_second_fermat(prime, left)
        for right in units:
            assert wild_log_coordinate(
                prime, left * right % modulus
            ) == (
                wild_log_coordinate(prime, left)
                + wild_log_coordinate(prime, right)
            ) % (prime**2)


def test_postnikov_increment_for_one_q_block() -> None:
    prime = 11
    modulus = prime**2
    for unit in range(1, prime):
        for lift in range(6):
            direct = (
                wild_log_coordinate(prime, unit + prime * lift)
                - wild_log_coordinate(prime, unit)
            ) % modulus
            assert direct == postnikov_increment(prime, unit, lift)


def test_active_exponent_ledger() -> None:
    ledger = active_exponent_ledger()
    assert ledger.degree == Fraction(16, 33)
    assert ledger.residual_length == Fraction(49, 33)
    assert ledger.additive_unit_band_length == Fraction(50, 33)
    assert ledger.additive_fourier_height == Fraction(49, 33)
    assert ledger.normalized_flat_coefficient == Fraction(-50, 33)
    assert ledger.reciprocal_resonance_count == Fraction(17, 33)
    assert ledger.reciprocal_coherent_count == Fraction(1, 33)
    assert ledger.critical_box_size == Fraction(98, 33)
    assert ledger.entropy_deficit == Fraction(1, 33)
