from qp_tangent_plucker_inverse import (
    add_scaled,
    anchored_codegree_ledger,
    affine_double_star,
    affine_arm_fiber_certificate,
    antipodal_degenerate_fiber,
    bilinear,
    determinant,
    determinant_sensitive_bound_gap,
    frobenius,
    outer,
    plucker_ledger,
    physical_affine_transition_grid,
    rank_one_double_star_energy,
    rank_one_double_star_ledger,
    residual_secant_model,
    ruling_certificate,
    secant_midpoint_certificate,
    shared_edge_arm_ledger,
    shared_edge_cross_certificate,
    tangent_carriers,
    tangent_colors,
    tangent_secant,
    tagged_parabola_projection_ledger,
    three_term_ruling_certificate,
)


def test_bilinear_plucker_and_equal_level_cross_factor() -> None:
    matrix = (19, -17, -13, 11)
    first_row = (23, 29)
    second_row = (41, 43)
    first_column = (31, 37)
    second_column = (47, 53)
    ledger = plucker_ledger(
        matrix, first_row, second_row, first_column, second_column
    )
    assert ledger.plucker_left == ledger.plucker_right
    assert ledger.energy_determinant == -(
        ledger.row_determinant * ledger.column_determinant
    )

    # The tangent family supplies a nontrivial equal-level instance.
    tangent_matrix, _ = tangent_colors(100_000, 100)
    row, column = tangent_carriers(100_000, 100, 7)
    other_row, other_column = tangent_carriers(100_000, 100, 43)
    equal = plucker_ledger(
        tangent_matrix, row, other_row, column, other_column
    )
    assert equal.first_level == equal.second_level
    assert equal.full_conic_parameter == (
        equal.first_level**2
        + equal.color_determinant * equal.energy_determinant
    )
    assert equal.full_conic_parameter != 0


def test_three_term_fixed_det_progression_forces_tangent_ruling() -> None:
    # Use the physical tangent witness rather than a hand-picked singular
    # matrix, so all three ruling conditions are exercised simultaneously.
    matrix, energy, direction = tangent_secant(100_000, 100, 7, 13)
    middle = add_scaled(energy, direction, 1)
    last = add_scaled(energy, direction, 2)
    certificate = three_term_ruling_certificate(
        matrix, energy, middle, last
    )
    assert certificate.is_tangent_ruling
    assert determinant(direction) == 0
    assert frobenius(matrix, direction) == 0


def test_tangent_family_has_constant_level_and_ruling_direction() -> None:
    m = 1_000_000
    h = 200
    matrix, colors = tangent_colors(m, h)
    assert determinant(matrix) == -2 * h * h
    levels = []
    for parameter in (1, 2, 17, 101, 199):
        row, column = tangent_carriers(m, h, parameter)
        levels.append(bilinear(matrix, row, column))
    assert len(set(levels)) == 1
    assert levels[0] == -2 * h * h * (m + 3 * h)
    assert colors == (m, m - 2 * h, m - h, m - 3 * h)

    _, energy, direction = tangent_secant(m, h, 17, 31)
    certificate = ruling_certificate(matrix, energy, direction)
    assert certificate.is_tangent_ruling
    assert determinant(energy) == 2 * h * h * 31 * 31


def test_determinant_sensitive_completion_cap_is_false_on_tangent_witness() -> None:
    D, multiplicity, gap = determinant_sensitive_bound_gap(500)
    assert D == 250_000
    assert multiplicity == 499
    # sqrt(D/|k|)=1/sqrt(2), so the failure grows linearly in h.
    assert gap > 700


def test_fixed_det_residual_model_survives_every_tangent_ruling() -> None:
    model = residual_secant_model(80, common_level=10_000, color_scale=7)
    assert model.color_determinant == 1
    assert len(model.secants) == 80
    assert len(set(model.secants)) == 80
    assert all(determinant(item) == 1 for item in model.secants)
    assert all(frobenius(model.matrix, item) == 0 for item in model.secants)
    assert all(determinant(item) == 0 for item in model.first_rank_one_endpoints)
    assert all(determinant(item) == 0 for item in model.second_rank_one_endpoints)
    assert all(
        frobenius(model.matrix, item) == model.common_level
        for item in model.first_rank_one_endpoints
    )
    assert all(
        frobenius(model.matrix, item) == model.common_level
        for item in model.second_rank_one_endpoints
    )
    for index, first in enumerate(model.secants):
        for second in model.secants[index + 1 :]:
            chord = tuple(y - x for x, y in zip(first, second))
            assert determinant(chord) != 0


def test_three_equal_determinants_alone_do_not_force_level_orthogonality() -> None:
    matrix = (1, 0, 0, 1)
    base = (0, 1, -1, 0)
    direction = (1, 0, 0, 0)
    certificate = ruling_certificate(matrix, base, direction)
    assert len(set(certificate.sampled_determinants)) == 1
    assert certificate.direction_determinant == 0
    assert certificate.determinant_polar == 0
    assert certificate.direction_level == 1
    assert not certificate.is_tangent_ruling


def test_product_difference_used_by_plucker_is_literal() -> None:
    row = (3, 5)
    column = (7, 11)
    other_row = (13, 17)
    other_column = (19, 23)
    first = outer(row, column)
    second = outer(other_row, other_column)
    energy = tuple(x - y for x, y in zip(first, second))
    assert determinant(energy) == -(
        (row[0] * other_row[1] - row[1] * other_row[0])
        * (
            column[0] * other_column[1]
            - column[1] * other_column[0]
        )
    )


def test_secant_midpoint_binary_norm_reduction() -> None:
    model = residual_secant_model(12, common_level=1000, color_scale=5)
    base = model.secants[2]
    translated = model.secants[9]
    displacement = tuple(y - x for x, y in zip(base, translated))
    certificate = secant_midpoint_certificate(
        model.matrix, base, displacement  # type: ignore[arg-type]
    )
    assert certificate.determinant_level == 1
    assert certificate.displacement_determinant == -(9 - 2) ** 2
    assert certificate.midpoint_determinant == 4 + (9 - 2) ** 2
    assert certificate.midpoint_level == 0
    assert certificate.midpoint_displacement_polar == 0


def test_full_rank_antipodal_exception_is_a_tangent_line_fiber() -> None:
    points = []
    for parameter in range(-10, 11):
        matrix, base, displacement = antipodal_degenerate_fiber(parameter)
        points.append(base)
        assert determinant(base) == 1
        assert determinant(add_scaled(base, displacement, 1)) == 1
        assert determinant(displacement) == 4
        certificate = secant_midpoint_certificate(matrix, base, displacement)
        assert certificate.expected_midpoint_determinant == 0
    direction = tuple(y - x for x, y in zip(points[0], points[1]))
    assert determinant(direction) == 0
    assert frobenius(matrix, direction) == 0


def test_six_physical_products_force_every_cross_neighbor_determinant() -> None:
    grid = physical_affine_transition_grid(8)
    by_edge = {
        (centers, colors): row for centers, colors, row in grid.witnesses
    }
    center_vertices = sorted({centers for centers, _, _ in grid.witnesses})
    color_vertices = sorted({colors for _, colors, _ in grid.witnesses})
    base_centers = center_vertices[0]
    base_colors = color_vertices[0]
    left_colors = color_vertices[-1]
    right_centers = center_vertices[-1]
    certificate = shared_edge_cross_certificate(
        grid.q,
        grid.D_window,
        base_row=by_edge[base_centers, base_colors],
        first_center=base_centers[0],
        second_center=base_centers[1],
        first_color=base_colors[0],
        second_color=base_colors[1],
        left_row=by_edge[base_centers, left_colors],
        left_first_color=left_colors[0],
        left_second_color=left_colors[1],
        right_row=by_edge[right_centers, base_colors],
        right_first_center=right_centers[0],
        right_second_center=right_centers[1],
    )
    expected = (
        left_colors[0] * right_centers[0]
        - left_colors[1] * right_centers[1]
    )
    assert certificate.cross_determinant == expected
    assert abs(expected) <= grid.maximum_transition_determinant
    assert certificate.identity_left == certificate.identity_right
    assert abs(expected) <= certificate.cross_determinant_upper_bound
    assert certificate.cross_determinant_upper_bound <= 2 * grid.D_window


def test_physical_affine_biclique_and_cycle_free_double_star() -> None:
    grid = physical_affine_transition_grid(12)
    assert len(grid.edges) == 12**2
    assert grid.maximum_product_residual <= grid.q * grid.D_window
    assert grid.maximum_transition_determinant < grid.D_window
    central = grid.edges[0]
    full = shared_edge_arm_ledger(grid.edges, central)
    assert full.left_degree == full.right_degree == 12
    assert full.edge_degree_product == 12**2
    assert full.completed_noncentral_arm_pairs == 11**2

    anchored = anchored_codegree_ledger(grid.edges, central[1])
    assert anchored.partner_count == 12
    assert anchored.maximum_codegree == 12
    assert anchored.first_moment == 12**2
    assert anchored.second_moment == 12**3
    assert anchored.determinant_layers_are_distinct

    star_edges = affine_double_star(grid)
    star = shared_edge_arm_ledger(star_edges, central)
    assert len(star_edges) == 2 * 12 - 1
    assert star.left_degree == star.right_degree == 12
    assert star.edge_degree_product == 12**2
    assert star.noncentral_arm_pairs == 11**2
    assert star.completed_noncentral_arm_pairs == 0


def test_rank_one_double_star_separates_rdp_from_weighted_energy() -> None:
    D = 300
    left_degree = right_degree = D // 3
    ledger = rank_one_double_star_ledger(left_degree, right_degree)
    assert ledger.maximum_left_codegree == 1
    assert ledger.maximum_right_codegree == 1
    assert ledger.central_degree_product == 10_000 > D
    assert ledger.maximum_neighbor_degree_sum == 199 <= D

    coefficients = tuple(
        complex((index % 7) - 3, (index % 5) - 2)
        for index in range(2 * left_degree)
    )
    energy = rank_one_double_star_energy(
        coefficients, left_degree, right_degree
    )
    norm_squared = sum(abs(value) ** 2 for value in coefficients)
    # Two elementary AM-GM/Cauchy bounds give E <=R/4 ||z||^4.
    assert energy <= right_degree * norm_squared**2 / 4 + 1e-8


def test_tagged_parabola_projection_destroys_the_zero_tag_gain() -> None:
    D = 100
    ledger = tagged_parabola_projection_ledger(D, 10)
    assert ledger.total_points == 1_000
    # The product of two parabolas has diagonal-scale additive energy.
    assert ledger.tagged_additive_energy < 4 * ledger.total_points**2
    # Nevertheless its K-rich zero-tag slice violates the desired D*K tail.
    assert ledger.zero_tag_off_diagonal_mass == 9_000 > D * 10
    # Dropping the tag creates all cross-tag pairs and loses exactly P.
    assert ledger.projected_off_diagonal_mass == 900_000
    assert ledger.projection_multiplicity_loss == D


def test_one_affine_arm_reduces_rdp_to_parallel_fiber_occupancy() -> None:
    grid = physical_affine_transition_grid(12)
    center_vertices = sorted({centers for centers, _, _ in grid.witnesses})
    color_vertices = sorted({colors for _, colors, _ in grid.witnesses})
    certificate = affine_arm_fiber_certificate(color_vertices, center_vertices)
    assert certificate.packet_length == 12
    assert certificate.opposite_population == 12
    # The extremal affine grid puts the whole opposite packet in one induced
    # direction fiber.  This is exactly the ruling/packet that must be merged.
    assert certificate.maximum_fiber_occupancy == 12
    assert certificate.degree_product == 12**2

    # A synthetic transverse selection with at most one point per direction
    # token illustrates the closed R=1 sector of the exact lemma.
    affine = tuple((10_000 + t, 10_001 + t) for t in range(20))
    transverse = tuple((20_000 + t, 20_003 + 2 * t) for t in range(8))
    transverse_certificate = affine_arm_fiber_certificate(affine, transverse)
    assert transverse_certificate.maximum_fiber_occupancy == 1
    assert transverse_certificate.degree_product <= (
        transverse_certificate.degree_product_ceiling
    )
