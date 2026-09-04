from qp_actual_masked_cycle_high_trace_barrier import (
    actual_masked_four_cycle,
    alternating_cycle_ledger,
    critical_component_count,
    projective_plane_trace_ledger,
)


def test_actual_masked_cycle_is_prime_and_inside_the_sharp_window() -> None:
    ledger = actual_masked_four_cycle()
    assert ledger.all_nodes_prime
    assert ledger.all_nodes_in_shell
    assert ledger.q_exceeds_d_squared
    assert ledger.maximum_absolute_residual < ledger.integer_window_lower_bound


def test_actual_cycle_has_a_nonzero_small_alternating_determinant() -> None:
    ledger = actual_masked_four_cycle()
    assert ledger.alternating_label_determinant == -158
    assert 0 < abs(ledger.alternating_label_determinant) < ledger.d_integer_lower_bound


def test_cycle_cross_multiplication_is_exact_but_labels_do_not_balance() -> None:
    ledger = actual_masked_four_cycle()
    edge_00, edge_01, edge_10, edge_11 = ledger.edges
    cycle = alternating_cycle_ledger(
        ledger.q,
        (edge_00.label, edge_11.label),
        (edge_01.label, edge_10.label),
        (edge_00.residual, edge_11.residual),
        (edge_01.residual, edge_10.residual),
    )
    assert cycle.cross_multiplication_defect == 0
    assert cycle.unprimed_label_product - cycle.primed_label_product == -158
    assert cycle.residual_sum_difference != 0


def test_projective_plane_components_have_spectral_excess_without_rectangles() -> None:
    ledger = projective_plane_trace_ledger(7, components=3)
    assert ledger.vertices_per_side_per_component == 57
    assert ledger.degree == 8
    assert ledger.four_cycle_count == 0
    assert ledger.centred_component_singular_value == ledger.degree
    assert ledger.centred_component_singular_value > ledger.square_root_degree
    assert ledger.maximum_label_degree == ledger.degree
    assert ledger.unique_edge_label_count == ledger.total_edges


def test_critical_component_count_has_the_right_scale() -> None:
    assert critical_component_count(1) == 1
    assert critical_component_count(2**16) == 2
