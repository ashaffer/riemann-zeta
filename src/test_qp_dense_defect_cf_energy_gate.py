from fractions import Fraction

import pytest

from qp_dense_defect_cf_energy_gate import (
    completion_lattice_determinant,
    dense_defect_ledger,
    low_rectangle_forces_collinearity,
    reciprocal_mixed_difference,
    reciprocal_second_difference,
)


def test_critical_dense_defect_exponents() -> None:
    ledger = dense_defect_ledger()
    assert ledger.energy_threshold == Fraction(5, 2)
    assert ledger.adjacent_gap == Fraction(1, 8)
    assert ledger.popular_chords == Fraction(3, 4)
    assert ledger.wrap_count == Fraction(5, 64)
    assert ledger.branch_length == Fraction(59, 64)
    assert ledger.branch_occupancy == Fraction(51, 64)
    assert ledger.cf_chord_scale == Fraction(17, 16)
    assert ledger.density_forced_chord_scale == Fraction(19, 16)
    assert ledger.density_to_cf_gap == Fraction(1, 8)
    assert ledger.carrier_alphabet_deficit == Fraction(25, 64)
    assert ledger.packet_determinant_margin == Fraction(9, 16)
    assert ledger.packet_step_scale == Fraction(1, 2)
    assert ledger.reciprocal_three_ap_scale == Fraction(33, 32)
    assert ledger.reciprocal_three_ap_forbidden_gap == Fraction(17, 32)
    assert ledger.mixed_difference_product_cutoff == Fraction(33, 16)
    assert ledger.narrow_rectangle_energy_bound == Fraction(2)
    assert ledger.narrow_to_target_margin == Fraction(1, 2)


def test_reciprocal_three_ap_second_difference_identity() -> None:
    value = reciprocal_second_difference(Fraction(11_000), 100, 3)
    assert value == Fraction(2 * 11_000 * 9, 100 * 103 * 106)


def test_reciprocal_rectangle_mixed_difference_identity() -> None:
    value = reciprocal_mixed_difference(Fraction(13_000), 100, 3, 7)
    expected = Fraction(
        13_000 * 3 * 7 * (200 + 3 + 7),
        100 * 103 * 107 * 110,
    )
    assert value == expected


def test_completion_lattice_determinant_is_a_host_multiple() -> None:
    # x=5, y=13 and x^{-1}=8 (mod 13).  Both vectors are multiples of
    # the primitive low ray (1,8), so their determinant vanishes.
    determinant, quotient = completion_lattice_determinant(
        5, 13, (1, 8), (2, 16)
    )
    assert determinant == quotient == 0
    assert low_rectangle_forces_collinearity(101, (1, 8), (2, 16), 2, 16)


def test_noncollinear_lattice_vectors_need_one_host_quantum() -> None:
    # (1,8) and (3,11) both lie in the x=5, y=13 lattice, and their
    # determinant is -13.  They therefore cannot fit in a rectangle whose
    # determinant ceiling is strictly below 13.
    determinant, quotient = completion_lattice_determinant(
        5, 13, (1, 8), (3, 11)
    )
    assert determinant == -13
    assert quotient == -1
    with pytest.raises(ValueError, match="determinant quantum"):
        low_rectangle_forces_collinearity(13, (1, 8), (3, 11), 3, 11)
