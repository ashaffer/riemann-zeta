from qp_four_cycle_degenerate_plane_covolume import (
    degenerate_plane_covolume_ledger,
)


def test_additive_tangent_plane_covolume() -> None:
    center = 100_000
    first_gap = 7
    second_gap = 11
    # Signed color matrix for
    # (C,C-a;C-b,C-a-b), whose determinant is -a*b.
    signed = (
        center,
        -(center - first_gap),
        -(center - second_gap),
        center - first_gap - second_gap,
    )
    ledger = degenerate_plane_covolume_ledger(
        signed,
        (1, 1),
        (1, 1),
    )
    assert ledger.color_determinant == -77
    assert ledger.row_gap == first_gap
    assert ledger.column_gap == second_gap
    assert ledger.pluecker_content == 1
    assert ledger.wedge_norm_square == 4 * (7 * 7 + 11 * 11)
    assert ledger.saturated_covolume_square_numerator == 680
    assert ledger.null_height_below_covolume


def test_unequal_primitive_directions_and_nontrivial_content() -> None:
    # Start with K'=(0,theta;eta,gamma) in coordinates where e=E11,
    # then use the already nontrivial primitive direction only on one side.
    # Direct example found by solving r^T K s=0.
    signed = (18, -12, -15, 10)  # determinant zero, so perturb consistently.
    # Use a known invertible weighted-additive example instead.
    signed = (2100, -1497, -1393, 993)
    ledger = degenerate_plane_covolume_ledger(
        signed,
        (2, 3),
        (5, 7),
    )
    assert ledger.color_determinant == -21
    assert ledger.row_gap * ledger.column_gap == 21
    assert ledger.pluecker_content == ledger.expected_content
    assert ledger.wedge_norm_square == ledger.expected_wedge_norm_square
    assert ledger.null_height_below_covolume
