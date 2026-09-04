from qp_pair_cell_discriminant import (
    ProductBandPoint,
    assert_refined_divisor_bounds,
    refined_divisor_majorant,
    refined_pair_cells,
    scan_pair_cells,
    shell_points,
    tangent_block_ledger,
    verify_discriminant_identities,
)


def test_all_discriminant_identities_on_a_physical_shell() -> None:
    q, band, center = 200, 12, 76_156
    points = shell_points(q, band, center)
    assert points
    for first in points:
        for second in points:
            verify_discriminant_identities(first, second, center)


def test_fixed_sum_error_and_carrier_cell_has_divisor_majorant() -> None:
    q, band, center = 200, 12, 76_156
    points = shell_points(q, band, center)
    assert_refined_divisor_bounds(points, center)
    for (completion_sum, error_sum, carrier_sum), multiplicity in refined_pair_cells(
        points
    ).items():
        majorant = refined_divisor_majorant(
            completion_sum, error_sum, carrier_sum, center
        )
        if majorant is not None:
            assert multiplicity <= majorant


def test_zero_residual_exception_is_a_single_diagonal_pair() -> None:
    center = 10_000
    point = ProductBandPoint(100, 100, 0)
    cells = refined_pair_cells([point])
    assert cells[(200, 0, 200)] == 1
    assert refined_divisor_majorant(200, 0, 200, center) is None
    assert_refined_divisor_bounds([point], center)


def test_scan_keeps_projected_and_refined_multiplicity_distinct() -> None:
    ledger = scan_pair_cells(q=200, band=12, center=76_156)
    assert ledger["points"] > 1
    assert ledger["maximum_projected_cell"] >= ledger["maximum_refined_cell"]
    assert ledger["maximum_carrier_sums_per_cell"] >= 1


def test_sqrt_band_blocking_does_not_follow_from_exact_cell_codegree() -> None:
    band = 10_000
    ledger = tangent_block_ledger(root=100_000, band=band)
    assert ledger["maximum_exact_cell"] == 2
    assert ledger["central_block_cell"] > band ** (1 / 4)
    assert ledger["maximum_direction_product_in_central_block"] <= ledger["block_width"] // 2
    assert ledger["maximum_direction_product_in_central_block"] < 100_000
