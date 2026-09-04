import math

from qp_ltrad_full_numeric_audit import (
    diagnose_pair,
    finite_ltrad_frontier,
    pnt_shell_count_crossover_log10,
)


def test_finite_frontier_separates_the_natural_wedge() -> None:
    frontier = finite_ltrad_frontier(
        1000,
        126,
        0.0308950,
        0.0309129,
        0.169408,
        0.169703,
    )
    assert 0.503 < frontier.premise_d_definite < 0.504
    assert 0.256 < frontier.conclusion_failure_c_definite < 0.257
    assert not frontier.definite_violation_rectangle_meets_c_gt_d
    assert 1.9 < frontier.effective_E_as_power_of_R < 2.1
    assert 1.958 < frontier.effective_E_as_power_of_R_lower < 1.959
    assert 1.960 < frontier.effective_E_as_power_of_R_upper < 1.961
    assert (
        frontier.effective_E_as_power_of_R_lower
        <= frontier.effective_E_as_power_of_R
        <= frontier.effective_E_as_power_of_R_upper
    )


def test_requested_pair_is_count_vacuous_at_small_scale() -> None:
    diagnostic = diagnose_pair(
        1000,
        126,
        0.0308950,
        0.0309129,
        0.169408,
        0.169703,
        c_rad=0.0189,
        d_dir=0.001,
    )
    assert diagnostic.premise_status == "fails"
    assert diagnostic.conclusion_status == "fails"
    assert diagnostic.implication_status == "premise-impossible-by-count-at-this-center"


def test_finite_constant_one_violation_is_detected() -> None:
    diagnostic = diagnose_pair(
        1000,
        126,
        0.0308950,
        0.0309129,
        0.169408,
        0.169703,
        c_rad=0.20,
        d_dir=0.60,
    )
    assert diagnostic.premise_status == "holds"
    assert diagnostic.conclusion_status == "fails"
    assert diagnostic.implication_status == "finite-constant-one-violation"


def test_pnt_crossover_calibration() -> None:
    width = 0.2
    maximal_center_ratio = 2.0 * math.exp(width)
    log10_n = pnt_shell_count_crossover_log10(
        0.019,
        shell_width=width,
        center_ratio=maximal_center_ratio,
    )
    assert 130.8 < log10_n < 131.1

    benchmark_log10_n = pnt_shell_count_crossover_log10(
        0.001,
        shell_width=width,
        center_ratio=maximal_center_ratio,
    )
    assert 3967.8 < benchmark_log10_n < 3968.2
