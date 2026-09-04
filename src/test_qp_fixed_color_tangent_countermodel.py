from qp_fixed_color_tangent_countermodel import (
    anisotropic_tangent_projection_bound,
    fixed_color_tangent_family,
    local_first_carrier_bound,
    near_square_first_carrier_bound,
    near_square_projection_fiber_bound,
)


def test_fixed_colors_have_sqrt_D_distinct_completions() -> None:
    family = fixed_color_tangent_family(m=100_000, h=100)
    assert family.q == 200_000
    assert family.D == 10_000
    assert family.color_determinant == -2 * family.D
    assert len(family.completions) == family.h - 1
    assert len({(item.rows, item.columns) for item in family.completions}) == 99
    assert all(item.distinct_labels == 8 for item in family.completions)
    assert family.normalized_residual_cap < 80.0


def test_family_replays_at_several_scales() -> None:
    for m, h in ((10_000, 20), (1_000_000, 200), (10_000_000, 500)):
        family = fixed_color_tangent_family(m, h)
        assert len(family.completions) == h - 1
        assert abs(family.color_determinant) == 2 * h * h
        assert family.residual_cap <= 80 * family.q * family.D


def test_local_cluster_bound_records_only_the_proved_statement() -> None:
    assert local_first_carrier_bound(0) == 1
    assert local_first_carrier_bound(100) == 101


def test_near_square_projection_fiber_is_on_the_D_scale() -> None:
    # At the active asymptotic proportions H=qD and shell nodes ~q/2,
    # R=sqrt(D) gives O(R) first-corner choices and O(D) total fiber.
    q = 2_000_000
    D = 10_000
    radius = 100
    first = near_square_first_carrier_bound(
        residual_cap=q * D,
        color_lower_bound=q // 3,
        carrier_lower_bound=q // 3,
        carrier_diameter=radius,
    )
    fiber = near_square_projection_fiber_bound(
        residual_cap=q * D,
        color_lower_bound=q // 3,
        carrier_lower_bound=q // 3,
        carrier_diameter=radius,
    )
    assert first <= radius + 2
    assert fiber <= 3 * D


def test_anisotropic_projection_cost_tracks_gap_product() -> None:
    q = 2_000_000
    D = 10_000
    # R*T=D with a long cross-gap and short adjacent displacement.
    fiber = anisotropic_tangent_projection_bound(
        residual_cap=q * D,
        color_lower_bound=q // 3,
        carrier_lower_bound=q // 3,
        cross_gap=1000,
        adjacent_gap=10,
    )
    assert fiber <= 3 * D
