from fractions import Fraction

from qp_two_star_bdh_selberg_inverse import (
    critical_bdh_ledger,
    latin_selberg_l1,
    selberg_inverse_ledger,
)


def test_critical_bdh_terms_are_below_m_squared() -> None:
    ledger = critical_bdh_ledger()
    assert ledger.diagonal_ratio == Fraction(-7, 8)
    assert ledger.principal_ratio == Fraction(-1, 16)


def test_small_power_selberg_failure_is_centered_sparse() -> None:
    epsilon = Fraction(1, 100)
    ledger = selberg_inverse_ledger(epsilon)
    assert ledger.frequency_length == Fraction(17, 16)
    assert ledger.term_count == 2
    assert ledger.normalized_average_coefficient == -1 + epsilon
    assert ledger.relative_centered_excess == -Fraction(15, 16) + 2 * epsilon
    assert ledger.relative_centered_excess < 0


def test_latin_model_has_prescribed_aligned_l1_mass() -> None:
    q, d, block = 2**20, 2**8, 2**5
    assert latin_selberg_l1(q, d, block) == (q // d) * block**2

