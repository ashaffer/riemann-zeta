from fractions import Fraction
from itertools import combinations

from qp_actual_prime_nds import actual_prime_residual_double_star, four_completion_chains
from qp_self_orbit_log_holonomy import (
    guaranteed_zero_cycle_length,
    hostile_nonreturn_triangle,
    phase_remainder_rational_ceiling,
    triangle_row_span_ledger,
)


def test_critical_phase_ceiling_forces_all_cycles_through_length_sixteen() -> None:
    q, D = 100_000, 265
    assert D * D < q
    ceiling = phase_remainder_rational_ceiling(q, D)
    assert ceiling == Fraction(D * D * q, 16 * (q * q - D))
    assert 16 * ceiling < 1
    assert guaranteed_zero_cycle_length(q, D) == 22


def test_hostile_bipartite_c6_collapses_to_zero_holonomy_escape_triangle() -> None:
    triangle = hostile_nonreturn_triangle()
    assert triangle.cycle.forced_zero_by_phase_bound
    assert triangle.cycle.edge_cocycles == (-2_099_874, -350_028, 2_449_902)
    assert triangle.cycle.circulation == 0
    assert triangle.determinants == (-42, -6, 42)
    assert triangle.affine_area == -6
    assert triangle.row_span == 8_341
    assert not triangle.forced_collinear_by_row_span
    assert triangle.opposite_row_functional == (Fraction(1, 2), Fraction(2, 3))


def test_all_triangles_in_the_seven_prime_fixture_are_collinear_packet_seeds() -> None:
    fixture = actual_prime_residual_double_star()
    chains = four_completion_chains(
        fixture.q,
        fixture.D,
        fixture.primes,
        fixture.central.colors,
        residual_only=False,
    )
    vertices: set[tuple[int, int]] = set()
    edges: dict[frozenset[tuple[int, int]], int] = {}
    for chain in chains:
        first = chain.centers
        second = chain.next_colors[::-1]
        vertices.update((first, second))
        key = frozenset((first, second))
        if key in edges:
            assert edges[key] == chain.next_row
        edges[key] = chain.next_row

    ledgers = []
    for v1, v2, v3 in combinations(vertices, 3):
        keys = (
            frozenset((v1, v2)),
            frozenset((v2, v3)),
            frozenset((v3, v1)),
        )
        if all(key in edges for key in keys):
            ledgers.append(
                triangle_row_span_ledger(
                    fixture.q,
                    fixture.D,
                    (v1, v2, v3),
                    tuple(edges[key] for key in keys),
                )
            )

    assert len(vertices) == 5
    assert len(ledgers) == 7
    assert max(ledger.row_span for ledger in ledgers) == 36
    assert all(ledger.cycle.circulation == 0 for ledger in ledgers)
    assert all(ledger.affine_area == 0 for ledger in ledgers)
    assert all(ledger.forced_collinear_by_row_span for ledger in ledgers)
