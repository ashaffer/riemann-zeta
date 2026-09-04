"""Finite packet-participation falsifiers using existing QP fixtures.

This verifier deliberately separates two levels.

* ``actual_carrier_packet_profile`` groups the existing actual-prime-power
  ordered-pair incidence graph by its stored carrier.  Each group is a
  weighted partial permutation, hence has operator norm at most one.  This
  is an instance of the abstract full-operator packet lemma, not the open
  A2/A4 affine-packet decomposition of the positive factorial form.
* ``q2_matching_block_profile`` treats each existing short q^2 residual
  block as a symmetric packet of norm two.  Its vertices are single shell
  nodes rather than the ordered-color-pair vertices required by A4.

In both cases the left and right support families coincide and every local
amplitude is constant.  If Delta is the maximum packet participation and
the amplitude is a, Cauchy--Schwarz at a Delta-fold vertex and the choice
lambda_t=a certify the exact optimum

    inf exp(Phi) = (a*Delta)^2.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from itertools import permutations
import json

import numpy as np

from qp_finite_carrier_relative_trace import exact_balanced_degree
from qp_four_cycle_h_graph_lab import (
    build_pair_incidence_graph,
    filtered_pair_incidence_graph,
)
from qp_four_cycle_hostile_lab import FourCycleCore, build_four_cycle_core
from qp_q2_packet_cross_gram_discovery import (
    build_q2_residue_atom_model,
    short_residual_matching_blocks,
)


@dataclass(frozen=True)
class ParticipationProfile:
    fixture: str
    q: int
    degree_parameter: int
    packet_count: int
    incidence_edges: int
    maximum_participation: int
    certified_amplitude: int
    exact_optimum_exp_phi: int
    target_degree_squared: int
    optimum_to_target_ratio: float


def _profile(
    *,
    fixture: str,
    q: int,
    packet_count: int,
    incidence_edges: int,
    maximum_participation: int,
    amplitude: int,
) -> ParticipationProfile:
    degree = exact_balanced_degree(q)
    optimum = (amplitude * maximum_participation) ** 2
    target = degree**2
    return ParticipationProfile(
        fixture=fixture,
        q=q,
        degree_parameter=degree,
        packet_count=packet_count,
        incidence_edges=incidence_edges,
        maximum_participation=maximum_participation,
        certified_amplitude=amplitude,
        exact_optimum_exp_phi=optimum,
        target_degree_squared=target,
        optimum_to_target_ratio=optimum / target,
    )


def actual_carrier_packet_profile(q: int, cutoff: float) -> ParticipationProfile:
    """Certify the carrier-packet abstraction on an actual prime-power core."""

    core = build_four_cycle_core(q, cutoff=cutoff, quadrature_order=32)
    graph = filtered_pair_incidence_graph(
        core,
        build_pair_incidence_graph(core),
        keep="all_five_distinct",
    )
    if graph.carriers is None:
        raise AssertionError("the actual incidence graph lost carrier labels")

    left_supports: dict[int, set[int]] = defaultdict(set)
    right_supports: dict[int, set[int]] = defaultdict(set)
    left_local_indices: dict[int, set[int]] = defaultdict(set)
    right_local_indices: dict[int, set[int]] = defaultdict(set)
    edge_counts: Counter[int] = Counter()
    coordinates = graph.support.tocoo()
    for left_index, right_index in zip(coordinates.row, coordinates.col):
        carrier = int(graph.carriers[int(left_index), int(right_index)])
        left_supports[carrier].add(int(graph.left_pair_codes[int(left_index)]))
        right_supports[carrier].add(int(graph.right_pair_codes[int(right_index)]))
        left_local_indices[carrier].add(int(left_index))
        right_local_indices[carrier].add(int(right_index))
        edge_counts[carrier] += 1

    # A fixed carrier acts by the involution a -> c determined by 8abc.
    # Thus its ordered-pair matrix is a partial permutation in both
    # orientations.  The actual finite support also verifies this directly.
    for carrier, count in edge_counts.items():
        if len(left_local_indices[carrier]) != count:
            raise AssertionError("a carrier packet repeated a left pair")
        if len(right_local_indices[carrier]) != count:
            raise AssertionError("a carrier packet repeated a right pair")

    # Product symmetry makes the two support sets literally equal after the
    # all-five-distinct filter on the audited fixture.
    if set(left_supports) != set(right_supports) or any(
        left_supports[carrier] != right_supports[carrier]
        for carrier in left_supports
    ):
        raise AssertionError("carrier packet supports are not left/right symmetric")

    # Each edge weight is a product of two averages of unit-modulus phases.
    # Hence one is a rigorous amplitude upper bound; this numerical guard
    # only checks that the fixture respects that analytic fact.
    if graph.weighted.nnz and max(abs(graph.weighted.data)) > 1.0 + 1.0e-12:
        raise AssertionError("a carrier packet coefficient exceeded one")

    participation: Counter[int] = Counter()
    for support in left_supports.values():
        participation.update(support)
    delta = max(participation.values(), default=0)
    return _profile(
        fixture=f"actual carrier packets q={q}, U={cutoff:g}",
        q=q,
        packet_count=len(left_supports),
        incidence_edges=int(graph.support.nnz),
        maximum_participation=delta,
        amplitude=1,
    )


def exact_q2_carrier_packet_profile(q: int) -> ParticipationProfile:
    """Certify carrier packets on the exact integer-selected q^2 atoms."""

    model = build_q2_residue_atom_model(q)
    triples = tuple(
        ordered
        for atom in model.selected_atoms
        for ordered in sorted(set(permutations(atom.node_indices)))
    )
    core = FourCycleCore(
        q=q,
        aperture=50.0 / 33.0,
        width=model.width,
        cutoff=1.0,
        values=model.values,
        rows=np.asarray([triple[0] for triple in triples], dtype=np.int32),
        columns=np.asarray([triple[1] for triple in triples], dtype=np.int32),
        colors=np.asarray([triple[2] for triple in triples], dtype=np.int32),
        weights=np.ones(len(triples), dtype=float),
    )
    graph = filtered_pair_incidence_graph(
        core,
        build_pair_incidence_graph(core),
        keep="all_five_distinct",
    )
    if graph.carriers is None:
        raise AssertionError("the exact q^2 incidence graph lost carrier labels")

    left_supports: dict[int, set[int]] = defaultdict(set)
    right_supports: dict[int, set[int]] = defaultdict(set)
    coordinates = graph.support.tocoo()
    for left_index, right_index in zip(coordinates.row, coordinates.col):
        carrier = int(graph.carriers[int(left_index), int(right_index)])
        left_supports[carrier].add(int(graph.left_pair_codes[int(left_index)]))
        right_supports[carrier].add(int(graph.right_pair_codes[int(right_index)]))
    if set(left_supports) != set(right_supports) or any(
        left_supports[carrier] != right_supports[carrier]
        for carrier in left_supports
    ):
        raise AssertionError("exact q^2 carrier supports are not symmetric")

    participation: Counter[int] = Counter()
    for support in left_supports.values():
        participation.update(support)
    delta = max(participation.values(), default=0)
    return _profile(
        fixture=f"exact hard-window q^2 carrier packets q={q}",
        q=q,
        packet_count=len(left_supports),
        incidence_edges=int(graph.support.nnz),
        maximum_participation=delta,
        amplitude=1,
    )


def q2_matching_block_profile(q: int) -> ParticipationProfile:
    """Certify the symmetric norm-two abstraction of q^2 matching blocks."""

    model = build_q2_residue_atom_model(q)
    blocks = short_residual_matching_blocks(model)
    participation: Counter[int] = Counter()
    incidence_edges = 0
    for block in blocks:
        vertices: set[int] = set()
        for atom in block.atoms:
            if not atom.all_nodes_distinct:
                raise AssertionError("the selected q^2 block has a repeated-node atom")
            if vertices.intersection(atom.vertex_set):
                raise AssertionError("the selected q^2 block is not a matching")
            vertices.update(atom.vertex_set)
        participation.update(vertices)
        incidence_edges += len(vertices)

    # A nonempty block is a direct sum of K_3 adjacency matrices, so its
    # operator norm is exactly two and its left/right vertex sets coincide.
    delta = max(participation.values(), default=0)
    return _profile(
        fixture=f"actual q^2 residual matching blocks q={q}",
        q=q,
        packet_count=len(blocks),
        incidence_edges=incidence_edges,
        maximum_participation=delta,
        amplitude=2,
    )


def main() -> None:
    profiles = [
        actual_carrier_packet_profile(25_013, 12.0),
        actual_carrier_packet_profile(25_013, 40.0),
        exact_q2_carrier_packet_profile(4_751),
        exact_q2_carrier_packet_profile(25_013),
        q2_matching_block_profile(151),
        q2_matching_block_profile(4_751),
        q2_matching_block_profile(25_013),
    ]
    print(json.dumps([asdict(profile) for profile in profiles], indent=2))


if __name__ == "__main__":
    main()
