from fractions import Fraction

from qp_q3_character_conductor_audit import (
    complete_q_block_decomposition,
    conductor_counts,
    project_character_exponent_ledger,
    residue_count_mod_q,
    symmetric_unit_interval_size,
)


def test_conductor_counts_partition_all_characters() -> None:
    q = 11
    counts = conductor_counts(q)
    assert counts.conductor_one == 1
    assert counts.conductor_q == q - 2
    assert counts.conductor_q_squared == (q - 1) ** 2
    assert counts.conductor_q_cubed == q * (q - 1) ** 2
    assert counts.total == q * q * (q - 1)


def test_symmetric_interval_is_uniform_mod_q_off_zero() -> None:
    q = 11
    degree = 7
    assert symmetric_unit_interval_size(q, degree) == 2 * degree * (q - 1)
    assert all(residue_count_mod_q(q, degree, residue) == 2 * degree for residue in range(1, q))
    assert complete_q_block_decomposition(q, q * degree).boundary_length_per_half == 0
    decomposition = complete_q_block_decomposition(q, q * degree + 4)
    assert decomposition.complete_blocks_per_half == degree
    assert decomposition.boundary_length_per_half == 4


def test_project_exponent_ledger_records_no_improvement() -> None:
    ledger = project_character_exponent_ledger()
    assert ledger.target_exponent_in_q == Fraction(16, 33)
    assert ledger.old_twenty_one_sixteenths_exponent_in_q == Fraction(7, 11)
    assert ledger.hilbert_schmidt_fourth_exponent_in_q == Fraction(32, 33)
    assert ledger.principal_fourth_exponent_in_q == Fraction(-2, 33)
    assert ledger.low_conductor_hs_squared_exponent_in_q == Fraction(-1, 33)
    assert ledger.low_conductor_fourth_exponent_in_q == Fraction(-2, 33)
    assert ledger.residual_length_exponent_in_q == Fraction(49, 33)
    assert ledger.residual_l2_exponent_in_q == Fraction(49, 66)
    assert ledger.burgess_r2_exponent_in_q == Fraction(689, 528)
    assert ledger.burgess_is_worse_than_residual_l2
    assert not ledger.character_method_improves_old_exponent
