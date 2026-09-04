from qp_four_cycle_affine_patch import (
    affine_patch_ledger,
    coherence_trace_coefficient,
    fixed_direction_merger_ledger,
    linear_grid_identity_ledger,
    parallel_product_band_line_ledger,
    parallel_product_band_point_cap,
    shared_progression_slope_pinning,
    weighted_fourth_trace,
)
from qp_multilevel_translation_grid import multilevel_entry


def _multilevel_edges(m: int, length: int) -> set[tuple[int, int, int]]:
    edges: set[tuple[int, int, int]] = set()
    for h in range(length, 2 * length + 1):
        for ell in range(length, 2 * length + 1):
            if h == ell:
                continue
            for t in range(20 * length, 21 * length + 1):
                for i in (0, 1):
                    for j in (0, 1):
                        edges.add(multilevel_entry(m, h, ell, t, i, j))
    return edges


def test_multilevel_clusters_merge_into_one_affine_patch() -> None:
    length = 8
    m = 10_000_000
    edges = _multilevel_edges(m, length)
    ledger = affine_patch_ledger(edges, (1, 1, 1))
    assert ledger.affine_level == 3 * m
    assert ledger.color_support_size == 3 * length + 1
    assert ledger.maximum_color_matching_size <= 3 * length + 1
    assert ledger.fourth_trace_coefficient <= (3 * length + 1) ** 2


def test_affine_patch_fourth_trace_bound_for_complex_weights() -> None:
    length = 5
    m = 1_000_000
    edges = _multilevel_edges(m, length)
    ledger = affine_patch_ledger(edges, (1, 1, 1))
    colors = sorted({color for _, _, color in edges})
    raw_weights = {
        color: complex((index % 4) - 1.5, (index % 3) - 1)
        for index, color in enumerate(colors)
    }
    norm = sum(abs(value) ** 2 for value in raw_weights.values()) ** 0.5
    weights = {color: value / norm for color, value in raw_weights.items()}
    trace = weighted_fourth_trace(edges, weights)
    assert trace <= ledger.fourth_trace_coefficient + 1e-9


def test_coherence_coefficient_is_matching_size_times_support() -> None:
    assert coherence_trace_coefficient(17, 23) == 391
    assert coherence_trace_coefficient(30, 5) == 25


def test_shared_color_progression_pins_the_slope_product() -> None:
    color = 1_000
    step = 4
    # The two factorizations 8*12=6*16 give different row/column slopes but
    # exactly the same pinned anchor product.
    target = 8 * (8 * color // step) * (12 * color // step) * color
    ledger = shared_progression_slope_pinning(
        target=target,
        residual_half_width=100,
        color_anchor=color,
        color_step=step,
        first_steps=(8, 12),
        second_steps=(6, 16),
    )
    assert ledger.slope_product_difference == 0
    assert ledger.pinning_quantum > ledger.residual_budget


def test_window_thickened_linear_grid_identities_are_exact() -> None:
    ledger = linear_grid_identity_ledger(
        row_base=10_003,
        column_base=9_971,
        color_anchor=10_019,
        row_step=17,
        column_step=19,
        color_step=13,
        length=8,
    )
    assert ledger.row_endpoint_defect == 0
    assert ledger.column_endpoint_defect == 0
    assert ledger.row_curvature_defect == 0
    assert ledger.column_curvature_defect == 0
    assert ledger.anchor_factorization_defect == 0


def test_parallel_product_band_line_allows_missing_parameters() -> None:
    # The line (a,b)=(300+3t,400-4t) is tangent to ab=120000.
    # Deliberately omit parameters: the proof uses occupied spans and does
    # not assume that every intervening lattice point is present.
    points = tuple(
        (300 + 3 * parameter, 400 - 4 * parameter)
        for parameter in (-3, -1, 2, 3)
    )
    ledger = parallel_product_band_line_ledger(
        points,
        product_center=120_000,
        product_half_width=108,
    )
    assert (ledger.primitive_row_step, ledger.primitive_column_step) == (3, 4)
    assert ledger.direction_product == 12
    assert ledger.line_invariant == 2_400
    assert ledger.occupied_points == 4
    assert ledger.invariant_square_defect == 0
    assert ledger.curvature_quantity <= ledger.curvature_upper_bound


def test_parallel_line_point_cap_uses_the_primitive_projection() -> None:
    # A raw projected step (6,-8) has primitive direction (3,-4).
    assert parallel_product_band_point_cap(108, 3, 4) == 12


def test_scale_separation_pins_a_rich_line_invariant() -> None:
    points = (
        (999_999, 1_000_001),
        (1_000_000, 1_000_000),
        (1_000_001, 999_999),
    )
    ledger = parallel_product_band_line_ledger(
        points,
        product_center=10**12,
        product_half_width=100,
    )
    assert ledger.invariant_is_pinned


def test_pinning_can_fail_without_scale_separation() -> None:
    # Both a+b=200 and a+b=201 have three points in the same width-200
    # product band.  This is the finite hostile model excluded by q>>D^2.
    first = parallel_product_band_line_ledger(
        ((99, 101), (100, 100), (101, 99)),
        product_center=10_000,
        product_half_width=100,
    )
    second = parallel_product_band_line_ledger(
        ((99, 102), (100, 101), (101, 100)),
        product_center=10_000,
        product_half_width=100,
    )
    assert first.line_invariant == 200
    assert second.line_invariant == 201
    assert not first.invariant_is_pinned
    assert not second.invariant_is_pinned


def test_fixed_raw_direction_merges_arbitrary_parallel_levels() -> None:
    ledger = fixed_direction_merger_ledger(
        (3, 3, -4, -4),
        product_half_width=108,
    )
    assert ledger.projected_direction_products == (12, 12, 12, 12)
    assert ledger.projected_point_caps == (12, 12, 12, 12)
    assert ledger.color_degree_bound == 48
    assert ledger.fourth_trace_coefficient == 48**2
