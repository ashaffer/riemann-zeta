from fractions import Fraction

import pytest

from qp_prime_center_burgess_cubic_gate import (
    PrimeCenterBurgessLedger,
    active_ledger,
    cubic_endpoint_ratio,
    multiplicative_character_spectrum,
    normalized_incidence_bounds,
    product_residue_count,
    restricted_weak_constant,
)


def test_active_all_prime_burgess_ledger() -> None:
    ledger = active_ledger()
    assert ledger.residual_exponent == Fraction(16, 33)
    assert ledger.old_skew_exponent == Fraction(8, 33)
    assert ledger.burgess_character_exponent == Fraction(227, 528)
    assert ledger.burgess_skew_exponent == Fraction(227, 1056)
    assert ledger.burgess_transverse_exponent == Fraction(755, 1056)
    assert ledger.burgess_saving == Fraction(29, 1056)


def test_density_one_ledger_is_stronger() -> None:
    ledger = active_ledger()
    assert ledger.density_one_skew_exponent == Fraction(97, 528)
    assert ledger.density_one_transverse_exponent == Fraction(361, 528)
    assert ledger.density_one_transverse_exponent < ledger.burgess_transverse_exponent


def test_principal_and_nonprincipal_interpolation() -> None:
    principal, nonprincipal = normalized_incidence_bounds(
        a_size=20,
        b_size=80,
        c_size=10,
        residual_length=4.0,
        modulus=101.0,
        character_maximum=9.0,
    )
    assert principal <= 4.0 / 101.0**0.5
    assert nonprincipal <= 3.0
    assert principal + nonprincipal <= restricted_weak_constant(4.0, 101.0, 9.0)


def test_cubic_endpoint_bound() -> None:
    assert cubic_endpoint_ratio(0.0) == pytest.approx(1.0)
    for skew_floor in (0.0, 1.0, 3.0, 100.0):
        assert cubic_endpoint_ratio(-skew_floor) >= 1.0 / (skew_floor + 1.0)


def test_small_prime_character_expansion_bound() -> None:
    prime = 11
    first = (1, 2, 4, 7)
    second = (1, 3, 5)
    residues = (1, 2, 10)
    count = product_residue_count(first, second, residues, prime)
    spectrum_r = multiplicative_character_spectrum(residues, prime)
    spectrum_a = multiplicative_character_spectrum(first, prime)
    spectrum_b = multiplicative_character_spectrum(second, prime)
    reconstructed = sum(
        spectrum_r[k].conjugate() * spectrum_a[k] * spectrum_b[k]
        for k in range(prime - 1)
    ) / (prime - 1)
    assert reconstructed.real == pytest.approx(count)
    assert reconstructed.imag == pytest.approx(0.0, abs=1e-10)


def test_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        PrimeCenterBurgessLedger(Fraction(3, 2))
    with pytest.raises(ValueError):
        restricted_weak_constant(1.0, 0.0, 1.0)
    with pytest.raises(ValueError):
        normalized_incidence_bounds(0, 1, 1, 1.0, 11.0, 1.0)
