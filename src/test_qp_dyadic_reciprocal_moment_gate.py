from fractions import Fraction

from qp_dyadic_reciprocal_moment_gate import (
    consecutive_lift_determinant,
    dyadic_moment_loss_ledger,
    hostile_cubic_transition_ledger,
    odd_centre_reduced_phase,
)


def test_odd_centre_next_dyadic_block_remains_coherent() -> None:
    # A scale-exact integer fixture: q is odd, D is of order q^(16/33),
    # M is a fixed small proportion of D, and ell is in the first dyadic
    # interval strictly above q/D^2.  No floating point phase is used.
    q = 2 * 10**33 + 1
    d = 10**16
    m_support = d // 1_000
    ell = 2 * q // d**2
    maximum = max(
        abs(ell * odd_centre_reduced_phase(q, x, y))
        for x in (0, m_support - 1)
        for y in (3 * m_support, 4 * m_support - 1)
    )
    assert maximum < Fraction(1, 100)


def test_consecutive_vectors_are_one_exact_determinant_strip() -> None:
    m = 10**6
    for shift in (0, 1, 17, 999):
        assert consecutive_lift_determinant(m, shift) == -shift


def test_a_sqrt_d_primal_moment_loss_would_improve_the_trace() -> None:
    ledger = dyadic_moment_loss_ledger(Fraction(1, 2))
    assert ledger.l1_loss_exponent_in_degree == Fraction(1, 4)
    assert ledger.slope_block_exponent_in_degree == Fraction(5, 4)
    assert ledger.fourth_trace_exponent_in_degree == Fraction(5, 4)
    assert ledger.improvement_exponent_in_degree == Fraction(1, 16)
    assert ledger.improves_current_uniform_trace


def test_any_primal_moment_loss_below_five_eighths_improves() -> None:
    assert dyadic_moment_loss_ledger(Fraction(5, 8) - Fraction(1, 100)).improves_current_uniform_trace
    assert not dyadic_moment_loss_ledger(Fraction(5, 8)).improves_current_uniform_trace


def test_hostile_transition_misses_by_one_sixteenth_in_p() -> None:
    ledger = hostile_cubic_transition_ledger()
    assert ledger.target_count_exponent_in_p == Fraction(9, 16)
    assert ledger.audited_floor_exponent_in_p == Fraction(5, 8)
    assert ledger.audited_gap_exponent_in_p == Fraction(1, 16)
