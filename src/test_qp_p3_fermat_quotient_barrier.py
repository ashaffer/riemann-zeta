from fractions import Fraction

from qp_p3_fermat_quotient_barrier import (
    best_formal_burgess_saving,
    best_licensed_classical_burgess_saving,
    coarse_q2_detector,
    formal_burgess_saving,
    kerr_2019_p3_exponent,
    optimistic_p3_burgess_deficit,
    primitive_character_count,
    ratio_conductor_counts,
    ratio_conductor_from_parameters,
    target_p_saving,
    taylor_block_mixed_saving,
)


def test_ratio_conductor_counts_partition_all_primitive_partners():
    for p in (3, 5, 7, 11, 17):
        counts = ratio_conductor_counts(p)
        assert counts.total == primitive_character_count(p)
        assert counts.p3 == p * (p - 2) * (p - 1)
        assert counts.p2 == (p - 1) ** 2


def test_ratio_conductor_parameter_classification():
    p = 11
    assert ratio_conductor_from_parameters(p, 3, 1) == p**3
    assert ratio_conductor_from_parameters(p, 3, p) == p**2
    assert ratio_conductor_from_parameters(p, 3, 0) == p
    assert ratio_conductor_from_parameters(p, 0, 0) == 1


def test_formal_and_licensed_burgess_ledgers_are_distinct_at_p3():
    assert best_formal_burgess_saving(3, 50) == (6, Fraction(1, 48))
    assert best_licensed_classical_burgess_saving(3, 50) == (3, Fraction(0))
    assert best_formal_burgess_saving(2, 50) == (2, Fraction(1, 8))


def test_target_and_optimistic_deficit():
    assert target_p_saving() == Fraction(2, 33)
    assert optimistic_p3_burgess_deficit() == Fraction(7, 176)
    assert formal_burgess_saving(3, 6) == Fraction(1, 48)


def test_kerr_cubefull_specialization_is_trivial():
    for r in range(2, 30):
        assert kerr_2019_p3_exponent(r) > 1


def test_known_taylor_block_ledger_stays_below_target():
    # These are the best small-degree choices; increasing the degree worsens
    # the VMVT-weight cost in this ledger.
    assert taylor_block_mixed_saving(2, 10) == Fraction(1, 105)
    assert taylor_block_mixed_saving(3, 12) == Fraction(1, 72)
    assert taylor_block_mixed_saving(3, 12) < target_p_saving()


def test_coarse_q2_detector_is_exact_inside_its_support():
    p, h = 101, 777
    p2 = p * p
    for rho in range(-(p2 // 3) + 1, p2 // 3):
        assert coarse_q2_detector(rho, p, h) == (abs(rho) <= h)


def test_coarse_q2_detector_rejects_neighboring_lifts():
    p, h = 101, 777
    assert not coarse_q2_detector(p * p + 3, p, h)
    assert not coarse_q2_detector(-p * p - 3, p, h)
