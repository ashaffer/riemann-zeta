from fractions import Fraction

from qp_affine_four_completion_hessian import (
    StationaryAffineProduct,
    actual_prime_stationary_integrality_obstruction,
    count_affine_determinant_strip,
    classify_two_leg_directions,
    parallel_affine_strip_elementary_ceiling,
    parallel_token_direction_ledger,
    stationary_lattice_point_ceiling,
    verify_transverse_affine_strip_bound,
)


def test_general_stationary_cubic_and_hessian() -> None:
    chart = StationaryAffineProduct(1000, 1000, 1000, -2, 3)
    assert chart.integral_row_law
    assert chart.row_r_step == 2
    assert chart.row_s_step == -3
    assert chart.hessian_determinant == 3 * 1000**2 * 2**2 * 3**2
    for r, s in ((0, 0), (2, 3), (-4, 1), (5, -2)):
        chart.exact_residual_from_base(r, s)


def test_principal_quadratic_is_the_signed_hexagonal_norm() -> None:
    middle = 10_000
    # b=M-A and d=M+s, so the normalized variables have opposite signs.
    chart = StationaryAffineProduct(middle, middle, middle, -1, 1)
    r, s = 7, 5
    A, B = chart.normalized_displacements(r, s)
    assert A * A + A * B + B * B == Fraction(r * r - r * s + s * s, middle**2)


def test_stationary_window_implies_an_ellipse_and_O_D_count() -> None:
    q = 20_000
    D = 160
    middle = q // 2
    target = middle**3
    tolerance = q * D // 8
    chart = StationaryAffineProduct(middle, middle, middle, -2, 3)
    survivors = 0
    for r in range(-D, D + 1):
        for s in range(-D, D + 1):
            if abs(chart.normalized_displacements(r, s)[0]) + abs(
                chart.normalized_displacements(r, s)[1]
            ) > Fraction(1, 4):
                continue
            residual = chart.exact_residual_from_base(r, s)
            if abs(residual) <= tolerance:
                survivors += 1
                chart.necessary_displacement_bound(
                    r,
                    s,
                    base_residual_bound=tolerance,
                    cell_residual_bound=tolerance,
                    target=target,
                )
    assert survivors <= stationary_lattice_point_ceiling(q, D, chart)
    assert survivors <= 20 * D


def test_simultaneous_degeneracy_is_only_coordinate_tangent() -> None:
    first = classify_two_leg_directions((1, 0), (0, 1))
    assert first.simultaneous_degeneracy
    assert first.coordinate_tangent_ruling
    assert first.signed_tangent

    # Full signed tangency is strictly weaker than Hessian degeneracy.
    second = classify_two_leg_directions((1, 1), (1, 1))
    assert second.signed_tangent
    assert not second.first_hessian_degenerate
    assert not second.second_hessian_degenerate
    assert not second.simultaneous_degeneracy


def test_actual_coprime_rows_block_exact_stationary_integrality() -> None:
    assert actual_prime_stationary_integrality_obstruction(101, 103, 2)
    chart = StationaryAffineProduct(101, 103, 107, 2, 3)
    assert not chart.integral_row_law


def test_every_transverse_affine_token_chart_has_a_harmonic_strip_bound() -> None:
    D = 90
    r_values = range(-D, D + 1)
    s_values = range(-D, D + 1)
    count, ceiling = verify_transverse_affine_strip_bound(
        17, -11, 7, 3, r_values, s_values, D
    )
    assert count <= ceiling
    assert ceiling < 30 * D * (1 + D.bit_length())


def test_parallel_small_slope_regime_really_escapes_the_strip_alone() -> None:
    D = 80
    rs = range(D)
    # The constant determinant zero chart retains the complete D by D block.
    count = count_affine_determinant_strip(0, 0, 0, 0, rs, rs, D)
    assert count == D * D
    assert parallel_affine_strip_elementary_ceiling(D, D, D, 0, 0) == D * D

    # A large affine slope restores an O(D) line-strip bound.
    assert parallel_affine_strip_elementary_ceiling(D, D, D, D, 1) <= 3 * D


def test_parallel_tokens_split_into_curved_and_coordinate_null_rulings() -> None:
    # For (c,C)=(11,13), one has 11*6-13*5=1.
    curved = parallel_token_direction_ledger(11, 13, 6, 5, (1, 0), (-2, 0))
    assert curved.token_area == 0
    assert curved.first_product_cross == curved.second_product_cross
    assert curved.first_product_cross != 0
    assert curved.token_norm != 0
    assert not curved.coordinate_null_ruling

    # Solve u*e-C*n=0 to make the centre direction a coordinate axis.
    null = parallel_token_direction_ledger(11, 13, 6, 5, (13, 6), (26, 12))
    assert null.token_area == 0
    assert null.token_norm == 0
    assert null.coordinate_null_ruling
