from collections import Counter

from qp_four_cycle_norm_graph_countermodel import (
    norm_graph_neighbors,
    norm_graph_resource_ledger,
    norm_graph_vertices,
)


def test_exact_norm_graph_resource_and_four_cycle_ledger() -> None:
    ledger = norm_graph_resource_ledger(7)
    assert ledger.vertices_per_side == 294
    assert ledger.vertex_degree == ledger.colors == 48
    assert ledger.color_degree == ledger.degree_cap == 294
    assert ledger.generic_rank_one_mass_lower_bound == 7**3 * 4
    assert ledger.generic_mass_to_degree_cap > 4


def test_concrete_norm_graph_has_the_claimed_pair_codegrees_and_colors() -> None:
    prime = 7
    vertices = norm_graph_vertices(prime)
    neighborhoods = {
        vertex: norm_graph_neighbors(prime, vertex) for vertex in vertices
    }
    assert all(len(table) == prime * prime - 1 for table in neighborhoods.values())

    # The canonical extension-field color is proper on both sides and every
    # color is a perfect matching.
    color_counts: Counter[tuple[int, int]] = Counter()
    right_color_pairs: set[tuple[object, tuple[int, int]]] = set()
    for table in neighborhoods.values():
        assert len(set(table.values())) == prime * prime - 1
        for right, color in table.items():
            color_counts[color] += 1
            key = (right, color)
            assert key not in right_color_pairs
            right_color_pairs.add(key)
    assert set(color_counts.values()) == {len(vertices)}

    # If the extension coordinates agree the codegree is zero.  Otherwise it
    # is q when the scalar coordinates agree and q+1 when they differ.
    codegrees: Counter[int] = Counter()
    four_cycles = 0
    for index, left in enumerate(vertices):
        left_neighbors = neighborhoods[left].keys()
        for right in vertices[index + 1 :]:
            common = len(left_neighbors & neighborhoods[right].keys())
            codegrees[common] += 1
            four_cycles += common * (common - 1) // 2
            if left[0] == right[0]:
                assert common == 0
            elif left[1] == right[1]:
                assert common == prime
            else:
                assert common == prime + 1
    assert set(codegrees) == {0, prime, prime + 1}
    assert four_cycles == norm_graph_resource_ledger(prime).unordered_four_cycles

