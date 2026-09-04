"""A coarse-cube countermodel to trace recombination from local planes alone."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CoarseCubeCountermodelLedger:
    critical_side: int
    degree_cap: int
    coarse_blocks: int
    internal_block_side: int
    shared_color_support: int
    maximum_color_degree: int
    maximum_row_degree: int
    local_fourth_trace: float
    global_fourth_trace: float
    nondegenerate_four_cycle_mass: float
    global_to_target_ratio: float


def block_partial_permutation_trace_bound(
    global_color_degree: int,
    local_color_degree: int,
    color_block_l2_mass: float,
) -> float:
    """Recombine row/column-disjoint coarse blocks without a block-count loss.

    If ``F_p^2`` is the weighted Frobenius mass of block ``p``, then
    ``sum_p S4(p)^4 <= max_p(F_p^2) sum_p(F_p^2)``.  Local color degree
    bounds the first factor, while global color degree bounds the second.
    """

    if global_color_degree < 0 or local_color_degree < 0:
        raise ValueError("degree bounds must be nonnegative")
    if color_block_l2_mass < 0:
        raise ValueError("the color-block mass must be nonnegative")
    return (
        global_color_degree
        * local_color_degree
        * color_block_l2_mass**4
    )


def coarse_cube_countermodel(side: int) -> CoarseCubeCountermodelLedger:
    """Return the exact repeated affine-cube ledger.

    There are ``side`` row/column-disjoint blocks.  Each is an ``ell`` by
    ``ell`` additive Hankel matrix colored by ``i+j``; all blocks reuse the
    same ``2*ell-1`` colors.  Flat unit weights make each block constant.
    """

    if side < 6:
        raise ValueError("the critical side must be at least six")
    ell = side // 3
    colors = 2 * ell - 1
    blocks = side
    degree_cap = side * side
    maximum_color_degree = blocks * ell
    maximum_row_degree = ell
    # Every entry has size colors^(-1/2), so the unique nonzero singular
    # value of one ell-by-ell block is ell/sqrt(colors).
    local_trace = ell**4 / colors**2
    global_trace = blocks * local_trace
    nondegenerate = blocks * (ell * (ell - 1)) ** 2 / colors**2
    return CoarseCubeCountermodelLedger(
        critical_side=side,
        degree_cap=degree_cap,
        coarse_blocks=blocks,
        internal_block_side=ell,
        shared_color_support=colors,
        maximum_color_degree=maximum_color_degree,
        maximum_row_degree=maximum_row_degree,
        local_fourth_trace=local_trace,
        global_fourth_trace=global_trace,
        nondegenerate_four_cycle_mass=nondegenerate,
        global_to_target_ratio=nondegenerate / degree_cap,
    )
