"""Exact fixed-defect graph folds and reduced-cycle certificates.

For a literal carrier--colour mask, group the entries in one carrier row by
the integer product ``n=a*c``.  A fixed defect wedge is then exactly the
shift ``n -> n-h``.  The shift is a partial matching on product states; its
fold through the (at most two, on the prime-power shell) factors of ``n`` is
the fixed-defect colour graph ``K_h``.

This module keeps that fold literal.  It neither completes the product
window nor replaces prime powers by an interval.  It also extracts the exact
additive and multiplicative identities attached to a reduced alternating
cycle of product blocks.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from math import prod, sqrt
from typing import Iterable, Sequence

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix

from qp_finite_carrier_relative_trace import ActualCarrierMatrix


@dataclass(frozen=True)
class DefectBlock:
    """One actual product-state shift inside a common carrier row."""

    carrier_index: int
    source_product: int
    target_product: int
    source_colours: tuple[int, ...]
    target_colours: tuple[int, ...]

    @property
    def defect(self) -> int:
        return self.source_product - self.target_product


def all_fixed_defect_blocks(
    core: ActualCarrierMatrix,
) -> dict[int, tuple[DefectBlock, ...]]:
    """Group every nonzero physical wedge by ``h=ac-a'c'``.

    Colour entries are stored as indices into ``core.values``.  A block is
    listed once for each ordered pair of *product states*, rather than once
    for each of the factor orientations in its rank-one outer product.
    """

    answer: dict[int, list[DefectBlock]] = defaultdict(list)
    values = core.values
    for carrier_index in range(core.dimension):
        lower, upper = core.support.indptr[carrier_index : carrier_index + 2]
        colours = core.support.indices[lower:upper]
        labels = core.labels.data[lower:upper]
        by_product: dict[int, list[int]] = defaultdict(list)
        for colour_index, label in zip(colours, labels):
            product_value = int(values[int(colour_index)]) * int(label)
            by_product[product_value].append(int(colour_index))
        products = tuple(by_product)
        for source_product in products:
            for target_product in products:
                defect = source_product - target_product
                if defect == 0:
                    continue
                answer[defect].append(
                    DefectBlock(
                        carrier_index=carrier_index,
                        source_product=source_product,
                        target_product=target_product,
                        source_colours=tuple(sorted(by_product[source_product])),
                        target_colours=tuple(sorted(by_product[target_product])),
                    )
                )
    return {defect: tuple(blocks) for defect, blocks in answer.items()}


def fixed_defect_matrix(
    dimension: int, blocks: Sequence[DefectBlock]
) -> csr_matrix:
    r"""Return ``K_h=sum u_(b,n-h) u_(b,n)^*`` for unit mask weights."""

    rows: list[int] = []
    columns: list[int] = []
    for block in blocks:
        for target in block.target_colours:
            for source in block.source_colours:
                rows.append(target)
                columns.append(source)
    matrix = coo_matrix(
        (np.ones(len(rows), dtype=np.int64), (rows, columns)),
        shape=(int(dimension), int(dimension)),
    ).tocsr()
    matrix.sum_duplicates()
    return matrix


@dataclass(frozen=True)
class ReducedCycleStep:
    """The two blocks and shared factors in one trace-cycle step."""

    source_block: int
    comparison_block: int
    shared_source_colour: int
    shared_target_colour: int


def find_reduced_alternating_cycle(
    blocks: Sequence[DefectBlock],
) -> tuple[ReducedCycleStep, ...] | None:
    """Find a cycle alternating source-factor and target-factor overlap.

    A trace term of ``(K_h K_h^*)^k`` has blocks ``s_i,t_i`` with ``s_i``
    and ``t_i`` sharing a source factor, while ``t_i`` and ``s_(i+1)`` share
    a target factor.  Reusing the same block at one overlap is excluded; the
    unavoidable internal ``2 by 2`` orientation rectangle is therefore not
    reported as a reduced cycle.
    """

    source_occurrences: dict[int, list[int]] = defaultdict(list)
    target_occurrences: dict[int, list[int]] = defaultdict(list)
    for block_index, block in enumerate(blocks):
        for colour in block.source_colours:
            source_occurrences[colour].append(block_index)
        for colour in block.target_colours:
            target_occurrences[colour].append(block_index)

    source_links: dict[tuple[int, int], int] = {}
    target_links: dict[tuple[int, int], int] = {}
    for colour, indices in source_occurrences.items():
        for first in indices:
            for second in indices:
                if first != second:
                    source_links.setdefault((first, second), colour)
    for colour, indices in target_occurrences.items():
        for first in indices:
            for second in indices:
                if first != second:
                    target_links.setdefault((first, second), colour)

    # transition[s] contains (s_next, t, shared_source, shared_target)
    transitions: dict[int, list[tuple[int, int, int, int]]] = defaultdict(list)
    for (source_block, comparison_block), source_colour in source_links.items():
        for (first, next_block), target_colour in target_links.items():
            if first == comparison_block:
                transitions[source_block].append(
                    (
                        next_block,
                        comparison_block,
                        source_colour,
                        target_colour,
                    )
                )

    colour: dict[int, int] = {}
    stack_nodes: list[int] = []
    stack_edges: list[tuple[int, int, int, int]] = []

    def visit(node: int) -> tuple[ReducedCycleStep, ...] | None:
        colour[node] = 1
        stack_nodes.append(node)
        for transition in transitions.get(node, ()):
            next_node, comparison, shared_source, shared_target = transition
            if colour.get(next_node, 0) == 0:
                stack_edges.append(transition)
                found = visit(next_node)
                if found is not None:
                    return found
                stack_edges.pop()
            elif colour.get(next_node) == 1:
                start = stack_nodes.index(next_node)
                cycle_edges = stack_edges[start:] + [transition]
                cycle_nodes = stack_nodes[start:]
                return tuple(
                    ReducedCycleStep(
                        source_block=cycle_nodes[index],
                        comparison_block=edge[1],
                        shared_source_colour=edge[2],
                        shared_target_colour=edge[3],
                    )
                    for index, edge in enumerate(cycle_edges)
                )
        stack_nodes.pop()
        colour[node] = 2
        return None

    for block_index in range(len(blocks)):
        if colour.get(block_index, 0) == 0:
            found = visit(block_index)
            if found is not None:
                return found
    return None


@dataclass(frozen=True)
class CycleIdentityCertificate:
    length: int
    additive_left_side: int
    multiplicative_left_numerator: int
    multiplicative_left_denominator: int
    multiplicative_label_numerator: int
    multiplicative_label_denominator: int
    maximum_product_gap: int

    @property
    def additive_identity_holds(self) -> bool:
        return self.additive_left_side == 0

    @property
    def multiplicative_identity_holds(self) -> bool:
        return (
            self.multiplicative_left_numerator
            * self.multiplicative_label_denominator
            == self.multiplicative_left_denominator
            * self.multiplicative_label_numerator
        )


def reduced_cycle_identity(
    blocks: Sequence[DefectBlock],
    cycle: Sequence[ReducedCycleStep],
    colour_values: Sequence[int],
) -> CycleIdentityCertificate:
    r"""Evaluate the exact additive and multiplicative cycle identities.

    With ``s_i=(n_i,n_i-h)`` and ``t_i=(m_i,m_i-h)``, put

    ``n_i=x_i alpha_i``, ``m_i=x_i A_i``,
    ``m_i-h=y_i B_i``, ``n_(i+1)-h=y_i beta_(i+1)``.

    Then exactly

    ``sum x_i(alpha_i-A_i)+y_i(B_i-beta_(i+1))=0``

    and

    ``prod(alpha_i B_i)/(A_i beta_i)`` equals
    ``prod(n_i(m_i-h))/(m_i(n_i-h))``.
    """

    if not cycle:
        raise ValueError("a cycle must be nonempty")
    defect = blocks[cycle[0].source_block].defect
    if any(blocks[step.source_block].defect != defect for step in cycle):
        raise ValueError("all source blocks need one fixed defect")
    if any(blocks[step.comparison_block].defect != defect for step in cycle):
        raise ValueError("all comparison blocks need one fixed defect")

    count = len(cycle)
    n_values: list[int] = []
    m_values: list[int] = []
    alpha: list[int] = []
    big_a: list[int] = []
    big_b: list[int] = []
    beta_next: list[int] = []
    additive = 0
    maximum_gap = 0

    for index, step in enumerate(cycle):
        source = blocks[step.source_block]
        comparison = blocks[step.comparison_block]
        following = blocks[cycle[(index + 1) % count].source_block]
        if step.shared_source_colour not in source.source_colours or (
            step.shared_source_colour not in comparison.source_colours
        ):
            raise ValueError("the alleged source colour is not shared")
        if step.shared_target_colour not in comparison.target_colours or (
            step.shared_target_colour not in following.target_colours
        ):
            raise ValueError("the alleged target colour is not shared")
        x_value = int(colour_values[step.shared_source_colour])
        y_value = int(colour_values[step.shared_target_colour])
        n_value = source.source_product
        m_value = comparison.source_product
        if n_value % x_value or m_value % x_value:
            raise ValueError("the alleged source colour does not divide")
        if (m_value - defect) % y_value or (
            following.source_product - defect
        ) % y_value:
            raise ValueError("the alleged target colour does not divide")
        alpha_value = n_value // x_value
        big_a_value = m_value // x_value
        big_b_value = (m_value - defect) // y_value
        beta_value = (following.source_product - defect) // y_value

        n_values.append(n_value)
        m_values.append(m_value)
        alpha.append(alpha_value)
        big_a.append(big_a_value)
        big_b.append(big_b_value)
        beta_next.append(beta_value)
        additive += x_value * (alpha_value - big_a_value)
        additive += y_value * (big_b_value - beta_value)
        maximum_gap = max(maximum_gap, abs(m_value - n_value))

    # beta_next[i] is beta_(i+1); its cyclic product is prod beta_i.
    physical_numerator = prod(
        n_values[index] * (m_values[index] - defect) for index in range(count)
    )
    physical_denominator = prod(
        m_values[index] * (n_values[index] - defect) for index in range(count)
    )
    label_numerator = prod(
        alpha[index] * big_b[index] for index in range(count)
    )
    label_denominator = prod(
        big_a[index] * beta_next[index] for index in range(count)
    )
    return CycleIdentityCertificate(
        length=count,
        additive_left_side=additive,
        multiplicative_left_numerator=physical_numerator,
        multiplicative_left_denominator=physical_denominator,
        multiplicative_label_numerator=label_numerator,
        multiplicative_label_denominator=label_denominator,
        maximum_product_gap=maximum_gap,
    )


def rank_one_block_star(degree: int) -> np.ndarray:
    """Return the canonical star of ``2 by 2`` product-state blocks.

    All blocks share one source factor and have otherwise private source and
    target factors.  Its squared singular norm is exactly ``2*(degree+1)``.
    """

    block_count = int(degree)
    if block_count < 1:
        raise ValueError("degree must be positive")
    # columns: one central factor followed by one private factor per block;
    # rows: two private target factors per block.
    matrix = np.zeros((2 * block_count, block_count + 1), dtype=float)
    for index in range(block_count):
        matrix[2 * index : 2 * index + 2, 0] = 1.0
        matrix[2 * index : 2 * index + 2, index + 1] = 1.0
    return matrix


def rank_one_block_star_norm(degree: int) -> float:
    """Return the exact norm formula for :func:`rank_one_block_star`."""

    block_count = int(degree)
    if block_count < 1:
        raise ValueError("degree must be positive")
    return sqrt(2 * (block_count + 1))
