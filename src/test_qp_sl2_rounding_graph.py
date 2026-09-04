from qp_sl2_rounding_graph import (
    canonical_anchor,
    carrier_interval,
    first_coordinate_defect,
    hostile_rounding_audit,
    second_defect,
    shell_rounding_graph,
    shell_rounding_point,
)


def test_canonical_complement_and_unique_reconstruction() -> None:
    anchor = canonical_anchor(6089, 5179)
    assert (anchor.u, anchor.v) == (2817, 2396)
    assert anchor.determinant == 1
    point = shell_rounding_point(anchor, 320, 4098, 6112)
    assert point is not None
    assert point.first * anchor.c - point.second * anchor.d == 320


def test_rows_and_partner_colors_use_the_same_rounding_graph() -> None:
    # The actual q=25013 C6 from the project report.  The color pair is
    # (c,d)=(10313,10259), hence g=(d,c).
    anchor = canonical_anchor(10259, 10313)
    row = shell_rounding_point(anchor, -1500, 10000, 16000)
    assert row is not None
    assert (row.quotient, row.first, row.second) == (-1471, 12511, 12577)
    # The partner (c',d')=(12577,12511) has g'=(12511,12577), exactly
    # the same R(-1500) graph point.
    assert row.first == 12511
    assert row.second == 12577


def test_two_forms_of_second_defect_agree() -> None:
    anchor = canonical_anchor(6089, 5179)
    points = shell_rounding_graph(anchor, range(1, 1001), 4098, 6112)
    for first in points[::17]:
        for second in points[::19]:
            assert second_defect(first, second) == first_coordinate_defect(
                anchor, first, second
            )


def test_exact_reciprocal_carrier_interval_on_actual_c6_edge() -> None:
    q = 25013
    anchor = canonical_anchor(10259, 10313)
    row = shell_rounding_point(anchor, -1500, 10000, 16000)
    assert row is not None
    tolerance = 92829387
    interval = carrier_interval(
        target=q**3,
        tolerance=tolerance,
        row=row,
        first_color=10313,
        second_color=10259,
    )
    assert interval.integer_candidates(10000, 16000) == (15161,)
    assert abs(8 * row.first * 15161 * 10313 - q**3) <= tolerance
    assert abs(8 * row.second * 15161 * 10259 - q**3) <= tolerance


def test_scattered_rounding_graph_hostile_audit() -> None:
    audit = hostile_rounding_audit()
    assert audit.point_count == 212
    assert audit.maximum_collinear == 15
    assert audit.maximum_second_defect == 974
    assert audit.minimum_degree_at_cap == audit.point_count

