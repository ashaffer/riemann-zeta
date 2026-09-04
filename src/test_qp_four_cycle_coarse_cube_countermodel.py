from qp_four_cycle_coarse_cube_countermodel import (
    block_partial_permutation_trace_bound,
    coarse_cube_countermodel,
)


def test_coarse_affine_blocks_respect_the_degree_ledger() -> None:
    ledger = coarse_cube_countermodel(60)
    assert ledger.shared_color_support <= ledger.critical_side
    assert ledger.maximum_color_degree <= ledger.degree_cap
    assert ledger.maximum_row_degree <= ledger.degree_cap
    assert ledger.local_fourth_trace <= ledger.degree_cap


def test_coarse_recombination_loses_a_power() -> None:
    small = coarse_cube_countermodel(60)
    large = coarse_cube_countermodel(240)
    assert small.nondegenerate_four_cycle_mass > small.degree_cap
    assert large.nondegenerate_four_cycle_mass > large.degree_cap
    # The violation ratio is asymptotic to side/81=sqrt(D)/81.
    assert large.global_to_target_ratio > 3 * small.global_to_target_ratio


def test_positive_block_recombination_lemma_has_no_block_count() -> None:
    assert block_partial_permutation_trace_bound(10_000, 7, 0.5) == 4_375
