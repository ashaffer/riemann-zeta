import math

from qp_four_cycle_gap_projection import (
    CarrierGapSector,
    asymptotic_gap_scales,
    gap_projection_fiber_bounds,
)
from qp_four_cycle_hostile_lab import FULL_APERTURE, exact_prime_rectangle_fixture


def test_exact_fiber_envelopes_have_the_three_expected_pairings() -> None:
    q = 2_000_000
    D = 10_000
    sector = CarrierGapSector(
        row_gap=10,
        column_gap=17,
        cross_gaps=((1_000, 1_013), (1_007, 1_020)),
    )
    bounds = gap_projection_fiber_bounds(
        residual_cap=q * D,
        color_lower_bound=q // 3,
        carrier_lower_bound=q // 3,
        sector=sector,
    )
    assert len(bounds.coefficient_squares) == 3
    assert all(value > 0 for value in bounds.coefficient_squares)
    # The horizontal projection uses the shorter same-row displacement.
    assert max(bounds.horizontal) < 3 * (2 * sector.row_gap + 1) * 1_021


def test_anisotropic_tangent_sector_is_recovered() -> None:
    # r11<=R and the row displacement is T.  Triangle inequality gives
    # r21<=R+T, so the horizontal coefficient is O(RT).
    R = 1_000
    T = 10
    D = R * T
    sector = CarrierGapSector(
        row_gap=T,
        column_gap=1_500,
        cross_gaps=((R, 2_000), (R + T, 2_010)),
    )
    scales = asymptotic_gap_scales(sector)
    assert scales.horizontal_square <= (2 * D) ** 2
    assert scales.covered_at_scale(D, constant=2)


def test_near_square_sector_is_on_the_D_scale() -> None:
    R = 100
    D = R * R
    sector = CarrierGapSector(
        row_gap=R,
        column_gap=R,
        cross_gaps=((R, R), (R, R)),
    )
    assert asymptotic_gap_scales(sector).covered_at_scale(D, constant=2)


def test_actual_prime_fixture_survives_every_gap_projection() -> None:
    fixture = exact_prime_rectangle_fixture()
    sector = CarrierGapSector.from_carriers(fixture.rows, fixture.columns)
    scales = asymptotic_gap_scales(sector)
    project_D = math.ceil(
        12.0 * fixture.q**2 / (fixture.q / 2.0) ** FULL_APERTURE
    )

    assert sector.row_gap == 1_464
    assert sector.column_gap == 516
    assert sector.cross_gaps == ((7_000, 7_516), (5_536, 6_052))
    assert not scales.covered_at_scale(project_D, constant=64)
    assert scales.best > 2_900_000
    assert project_D == 6_512
