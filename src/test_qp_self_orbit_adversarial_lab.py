from qp_actual_prime_nds import exact_balanced_degree, in_hard_window
from qp_scattered_token_search import (
    RootedTokenScanner,
    broad_scattered_fixture,
    full_integer_shell,
    full_prime_power_shell,
)
from qp_self_orbit_adversarial_lab import (
    central_integer_kernel_fixture,
    first_scattered_prime_c6,
    interval_run_count,
    multilevel_self_orbit_packet,
    rooted_adjacency,
    rooted_vertex_points,
    scattered_prime_c8,
    short_self_orbit_kernel,
)


def test_entire_short_kernel_is_linear_sized_on_rich_and_broad_fixtures() -> None:
    rich = central_integer_kernel_fixture()
    assert rich.D == 371
    assert rich.physical_token_count == 743
    assert rich.incident_vertex_count == 144
    assert rich.directed_edge_count == 432
    assert rich.maximum_degree == rich.anchor_degree == 18
    assert rich.anchor_neighbour_degree_sum == 271
    assert rich.maximum_incident_affine_line_size == 144

    q = 200_000
    D = exact_balanced_degree(q)
    nodes = full_integer_shell(q)
    expected = {
        (108_551, 111_297): (256, 10, 16, 7, 3),
        (92_519, 87_756): (289, 25, 32, 1, 4),
        (116_417, 118_578): (245, 22, 26, 5, 3),
    }
    for gamma, values in expected.items():
        audit = short_self_orbit_kernel(q, D, nodes, gamma)
        assert (
            audit.physical_token_count,
            audit.incident_vertex_count,
            audit.directed_edge_count,
            audit.anchor_neighbour_degree_sum,
            audit.maximum_incident_affine_line_size,
        ) == values


def test_entire_actual_prime_kernel_is_tiny_in_the_large_fixture() -> None:
    q = 10_604_226
    audit = short_self_orbit_kernel(
        q,
        exact_balanced_degree(q),
        full_prime_power_shell(q),
        (5_302_109, 5_302_103),
    )
    assert audit.D == 2548
    assert audit.node_count == 137_783
    assert audit.physical_token_count == 14
    assert audit.incident_vertex_count == 5
    assert audit.directed_edge_count == 14
    assert audit.anchor_degree == 4
    assert audit.anchor_neighbour_degree_sum == 10
    assert audit.maximum_incident_affine_line_size == 5


def test_ordered_monge_and_two_interval_guesses_have_exact_counterexamples() -> None:
    broad = rooted_adjacency(broad_scattered_fixture())
    assert broad == {
        -162: frozenset((-77, 0)),
        -150: frozenset((0,)),
        -135: frozenset((-235, 0)),
        -77: frozenset((-162, 0)),
    }
    entry = lambda row, column: int(column in broad.get(row, ()))
    # Violates the Monge <= orientation.
    assert entry(-162, -77) + entry(-150, 0) > (
        entry(-162, 0) + entry(-150, -77)
    )
    # Violates the reverse (anti-Monge) orientation.
    assert entry(-162, -235) + entry(-150, -77) < (
        entry(-162, -77) + entry(-150, -235)
    )

    q = 3500
    t_audit = RootedTokenScanner(
        q, exact_balanced_degree(q), full_integer_shell(q)
    ).root_audit((1681, 1689))
    t_adjacency = rooted_adjacency(t_audit)
    t_order = sorted(rooted_vertex_points(t_audit))
    assert t_adjacency[1] == frozenset((0, 8, 16))
    assert t_order == [0, 1, 8, 10, 16]
    assert interval_run_count(t_adjacency[1], t_order) == 3

    q = 200_000
    b_audit = RootedTokenScanner(
        q, exact_balanced_degree(q), full_integer_shell(q)
    ).root_audit((116_417, 118_578))
    b_adjacency = rooted_adjacency(b_audit)
    points = rooted_vertex_points(b_audit)
    b_order = sorted(points, key=lambda label: points[label][0])
    assert b_order == [-85, 143, -185, -179, -222, 0]
    assert interval_run_count(b_adjacency[-179], b_order) == 3


def test_multilevel_tangent_slice_is_a_linear_sized_self_orbit_packet() -> None:
    packet = multilevel_self_orbit_packet()
    assert packet.q == 40_000_000
    assert packet.D == 204_800
    assert packet.anchor == (20_000_000, 19_999_989)
    assert len(packet.center_labels) == len(packet.source_labels) == 11
    assert packet.undirected_biclique_edges == 121
    assert packet.directed_edge_lower_bound == 242
    assert packet.maximum_product_residual < packet.q * packet.D


def test_scattered_prime_cycles_are_exact_but_far_outside_critical_D() -> None:
    c6 = first_scattered_prime_c6()
    assert len(c6.points) == 6
    assert c6.maximum_product_residual == 208_700_629
    assert c6.minimum_literal_D == 8344
    assert c6.critical_D == 135
    assert c6.distinct_edge_directions == 6
    assert abs(c6.maximum_smooth_frequency - 21.518440849497075) < 1.0e-12
    assert c6.all_displayed_values_distinct
    assert c6.all_displayed_values_prime
    assert c6.no_three_points_collinear
    assert all(
        in_hard_window(c6.q, c6.minimum_literal_D, triple)
        for pair in c6.edge_triples
        for triple in pair
    )
    assert any(
        not in_hard_window(c6.q, c6.minimum_literal_D - 1, triple)
        for pair in c6.edge_triples
        for triple in pair
    )

    c8 = scattered_prime_c8()
    assert len(c8.points) == 8
    assert c8.maximum_product_residual == 349_280_171
    assert c8.minimum_literal_D == 13_964
    assert c8.critical_D == 135
    assert c8.distinct_edge_directions == 8
    assert c8.all_displayed_values_distinct
    assert c8.all_displayed_values_prime
    assert c8.no_three_points_collinear
