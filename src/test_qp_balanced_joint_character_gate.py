from fractions import Fraction

import pytest

from qp_balanced_joint_character_gate import (
    ACTIVE_LEDGER,
    dft_indicator,
    primitive_character_projection,
    unit_frequency_projection,
)


def test_active_rational_ledger() -> None:
    ledger = ACTIVE_LEDGER
    assert ledger.A == Fraction(50, 33)
    assert ledger.residual_exponent == Fraction(49, 33)
    assert ledger.dual_length_exponent == Fraction(50, 33)
    assert ledger.critical_box_q_exponent == Fraction(98, 33)
    assert ledger.critical_box_Q_exponent == Fraction(98, 99)
    assert ledger.entropy_deficit_q_exponent == Fraction(1, 33)
    assert ledger.entropy_deficit_Q_exponent == Fraction(1, 99)
    assert ledger.required_relative_saving_Q_exponent == Fraction(16, 99)
    assert ledger.grouped_u_q_exponent == 2
    assert ledger.grouped_v_q_exponent == Fraction(32, 33)
    assert ledger.grouped_u_q_exponent + ledger.grouped_v_q_exponent == Fraction(
        98, 33
    )


@pytest.mark.parametrize("modulus", [27, 125])
def test_exact_additive_fourier_inversion(modulus: int) -> None:
    residues = {-4, -2, -1, 1, 2, 4}
    residue_set = {r % modulus for r in residues}
    for n in range(modulus):
        expected = 1.0 if n in residue_set else 0.0
        assert dft_indicator(modulus, residues, n) == pytest.approx(
            expected, abs=2e-12
        )


@pytest.mark.parametrize("prime", [3, 5, 7])
def test_primitive_characters_equal_unit_frequency_block(prime: int) -> None:
    residues = [r for r in range(-4, 5) if r and r % prime]
    for n in [1, 2, prime + 1]:
        lhs = primitive_character_projection(prime, residues, n)
        rhs = unit_frequency_projection(prime, residues, n)
        assert lhs == pytest.approx(rhs, abs=5e-11)


def test_main_frequencies_do_not_descend_to_prime_field() -> None:
    # A<2, so K=q^A<q^2.  No nonzero |m|<=K is divisible by q^2.
    assert ACTIVE_LEDGER.dual_length_exponent < 2
    for prime in [101, 1009]:
        # Every positive integer below q^2 is nonzero modulo q^2.
        cutoff = prime**2 - 1
        assert cutoff < prime**2
        assert cutoff % (prime**2) != 0
