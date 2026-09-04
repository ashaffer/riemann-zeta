from qp_four_cycle_covolume_moment_barrier import (
    critical_covolume_moment_witness,
)
from qp_four_cycle_degenerate_plane_covolume import (
    degenerate_plane_covolume_ledger,
)


def test_exact_critical_covolume_moment_obstruction() -> None:
    witness = critical_covolume_moment_witness(16)
    x, y, z, w = witness.colors
    assert witness.relation_defect == 0
    assert witness.color_determinant == -witness.column_gap
    assert witness.distinct_colors
    assert x > y > z > w > 0
    assert witness.below_determinant_budget
    assert witness.below_low_plane_cutoff
    assert witness.equal_weight_moment_exceeds_d

    # All four colors lie very near the nominal center q/2.
    center = witness.ambient_scale // 2
    assert max(abs(color - center) for color in witness.colors) * 100 < center


def test_covolume_formula_agrees_with_plane_ledger() -> None:
    witness = critical_covolume_moment_witness(17)
    x, y, z, w = witness.colors
    ledger = degenerate_plane_covolume_ledger(
        (x, -y, -z, w),
        witness.row_direction,
        witness.column_direction,
    )
    assert ledger.row_gap == witness.row_gap
    assert ledger.column_gap == witness.column_gap
    assert ledger.saturated_covolume_square_numerator == witness.covolume_square
    assert ledger.color_determinant == witness.color_determinant


def test_asymptotic_exponents_are_on_the_claimed_scales() -> None:
    witness = critical_covolume_moment_witness(19)
    n = witness.scale
    d = witness.determinant_budget
    # h=(N^2+1)^2 is D^(1/4) up to a bounded factor.
    assert n**4 < witness.null_height < 2 * n**4
    assert d == n**16
    # P is asymptotic to 2N^17: above D=N^16 but below q/D=4N^17.
    assert (n**17) ** 2 < witness.covolume_square
    assert witness.covolume_square < (4 * n**17) ** 2
