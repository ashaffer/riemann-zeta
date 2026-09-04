from fractions import Fraction

import pytest

from qp_balanced_cross_tensor_barrier import (
    BalancedCrossTensorLedger,
    active_ledger,
    nonprincipal_parseval_floor,
    normalized_fibre_pair_bound,
    normalized_principal_fibre_pair_bound,
)


def test_active_exponent_ledger() -> None:
    ledger = active_ledger()
    assert ledger.row_exponent == Fraction(16, 33)
    assert ledger.residual_exponent == Fraction(49, 33)
    assert ledger.schur_tensor_exponent == Fraction(8, 33)
    assert ledger.full_transverse_exponent == Fraction(49, 66)
    assert ledger.q2_parseval_character_floor == Fraction(49, 66)
    assert ledger.character_to_schur_gap == Fraction(1, 2)
    assert ledger.formal_principal_tensor_exponent == Fraction(31, 132)
    assert ledger.formal_principal_transverse_exponent == Fraction(97, 132)
    assert ledger.formal_principal_saving == Fraction(1, 132)


def test_raw_restricted_bound_is_sharp_at_critical_sizes() -> None:
    row_length = 64.0
    value = normalized_fibre_pair_bound(
        row_length, row_length, row_length, row_length
    )
    assert value == pytest.approx(row_length**0.5)


def test_raw_restricted_bound_never_exceeds_schur_constant() -> None:
    row_length = 16.0
    for first in (1.0, 4.0, 16.0, 64.0, 256.0):
        for second in (1.0, 4.0, 16.0, 64.0, 256.0):
            for third in (1.0, 4.0, 16.0, 64.0, 256.0):
                assert normalized_fibre_pair_bound(
                    first, second, third, row_length
                ) <= row_length**0.5 + 1e-12


def test_principal_only_critical_sizes() -> None:
    # The global optimum is attained when all three set sizes are sqrt(q).
    row_length = 16.0
    modulus_root = 256.0
    critical_size = modulus_root**0.5
    value = normalized_principal_fibre_pair_bound(
        critical_size,
        critical_size,
        critical_size,
        row_length,
        modulus_root,
    )
    assert value == pytest.approx(row_length / modulus_root**0.25)


def test_nonprincipal_parseval_floor() -> None:
    phi = 10_000
    length = 400
    floor = nonprincipal_parseval_floor(length, phi)
    assert floor**2 == pytest.approx(length * (phi - length) / (phi - 1))
    assert floor > (0.95 * length) ** 0.5


def test_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        BalancedCrossTensorLedger(Fraction(3, 2))
    with pytest.raises(ValueError):
        normalized_fibre_pair_bound(0.0, 1.0, 1.0, 1.0)
    with pytest.raises(ValueError):
        nonprincipal_parseval_floor(10, 10)
