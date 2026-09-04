from qp_four_cycle_critical_cube import (
    critical_cube_ledger,
    product_linearization,
)


def test_exact_product_linearization_identity() -> None:
    difference, linear, remainder = product_linearization(
        (10_003, 9_991, 10_019),
        (10_010, 9_980, 10_024),
    )
    assert difference == linear + remainder


def test_translation_patch_is_affine_rank_two_in_critical_cube() -> None:
    m = 10**8
    side = 40
    points = {
        (m + x, m + y, m - x - y)
        for x in range(0, 9)
        for y in range(0, 9)
    }
    maximum_residual = max(
        abs(8 * a * b * c - 8 * m**3) for a, b, c in points
    )
    ledger = critical_cube_ledger(
        points,
        target=8 * m**3,
        residual_half_width=maximum_residual,
        cube_side=side,
    )
    assert ledger.affine_rank == 2
    assert ledger.maximum_difference_determinant == 0


def test_cramer_bound_is_below_gradient_at_asymptotic_margin() -> None:
    # This synthetic scale has R^4/q small, the exact asymptotic condition
    # used in the theorem.  The points themselves are the rank-two patch
    # above; the assertion replays the decisive size comparison.
    m = 10**12
    side = 20
    points = {
        (m + x, m + y, m - x - y)
        for x in range(0, 5)
        for y in range(0, 5)
    }
    maximum_residual = max(
        abs(8 * a * b * c - 8 * m**3) for a, b, c in points
    )
    ledger = critical_cube_ledger(
        points,
        target=8 * m**3,
        residual_half_width=maximum_residual,
        cube_side=side,
    )
    assert ledger.cramer_upper_bound < ledger.gradient_minimum

