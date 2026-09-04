import numpy as np
import pytest

from qp_finite_carrier_relative_trace import build_actual_carrier_matrix
from qp_fixed_defect_graph_cycles import (
    ReducedCycleStep,
    all_fixed_defect_blocks,
    find_reduced_alternating_cycle,
    fixed_defect_matrix,
    rank_one_block_star,
    rank_one_block_star_norm,
    reduced_cycle_identity,
)


def test_literal_fixed_defect_fold_reconstructs_every_oriented_wedge() -> None:
    core = build_actual_carrier_matrix(25_013)
    rays = all_fixed_defect_blocks(core)
    assert set(rays) == {-36, 36}
    for defect, blocks in rays.items():
        matrix = fixed_defect_matrix(core.dimension, blocks)
        assert matrix.nnz == 4
        assert matrix.sum() == 4
        assert np.max(matrix.data) == 1
        assert fixed_defect_matrix(core.dimension, rays[-defect]).toarray() == pytest.approx(
            matrix.toarray().T
        )


def test_full_integer_reduced_cycle_obeys_both_exact_identities() -> None:
    # The integer shell supplies a deliberately non-prime diagnostic in
    # which reduced alternating cycles really occur.  The identities do not
    # use primality and retain every literal product-window block.
    core = build_actual_carrier_matrix(1_013, kind="integers")
    rays = all_fixed_defect_blocks(core)
    found = None
    for blocks in rays.values():
        cycle = find_reduced_alternating_cycle(blocks)
        if cycle is not None:
            found = (blocks, cycle)
            break
    assert found is not None
    blocks, cycle = found
    certificate = reduced_cycle_identity(blocks, cycle, core.values)
    assert certificate.length >= 1
    assert certificate.additive_identity_holds
    assert certificate.multiplicative_identity_holds


def test_actual_prime_fixed_defect_quotients_have_no_reduced_cycle_at_q100003() -> None:
    core = build_actual_carrier_matrix(100_003)
    rays = all_fixed_defect_blocks(core)
    assert len(rays) == 52
    assert all(find_reduced_alternating_cycle(blocks) is None for blocks in rays.values())
    assert max(len(blocks) for blocks in rays.values()) == 6


def test_wider_literal_all_prime_mask_has_a_nontrivial_reduced_cycle() -> None:
    # This uses a deliberately wider finite cutoff.  It is not an active-scale
    # counterexample; it proves that primality plus the exact product mask does
    # not turn the reduced-cycle identities into formal contradictions.
    q = 100_003
    half_degree = 20_000
    core = build_actual_carrier_matrix(q, degree_parameter=half_degree)
    blocks = all_fixed_defect_blocks(core)[4_242]
    by_source_product = {
        block.source_product: index for index, block in enumerate(blocks)
    }
    colour_index = {
        int(value): index for index, value in enumerate(core.values)
    }
    cycle = (
        ReducedCycleStep(
            source_block=by_source_product[2_951_930_173],
            comparison_block=by_source_product[2_636_424_521],
            shared_source_colour=colour_index[60_257],
            shared_target_colour=colour_index[58_979],
        ),
        ReducedCycleStep(
            source_block=by_source_product[2_493_695_341],
            comparison_block=by_source_product[2_542_072_123],
            shared_source_colour=colour_index[44_059],
            shared_target_colour=colour_index[55_763],
        ),
    )
    certificate = reduced_cycle_identity(blocks, cycle, core.values)
    assert certificate.additive_identity_holds
    assert certificate.multiplicative_identity_holds
    for step in cycle:
        for block_index in (step.source_block, step.comparison_block):
            block = blocks[block_index]
            carrier = int(core.values[block.carrier_index])
            assert abs(8 * carrier * block.source_product - q**3) <= q * half_degree
            assert abs(8 * carrier * block.target_product - q**3) <= q * half_degree


@pytest.mark.parametrize("degree", [1, 2, 7, 31])
def test_product_block_star_has_the_exact_sqrt_degree_norm(degree: int) -> None:
    matrix = rank_one_block_star(degree)
    observed = np.linalg.svd(matrix, compute_uv=False)[0]
    assert observed == pytest.approx(rank_one_block_star_norm(degree))
