from qp_four_cycle_rational_tangent import (
    integer_band_components,
    tangent_component_point_bound,
    tangent_patch_fourth_trace_coefficient,
)


def test_tangent_component_bound_is_sharp_up_to_endpoints() -> None:
    # (m+t)(m-t)=m^2-t^2, so the component has 2h+1 points when E=h^2.
    h = 100
    components = integer_band_components(
        a0=1_000_000,
        b0=1_000_000,
        row_step=1,
        column_step=1,
        product_center=1_000_000**2,
        product_half_width=h * h,
        first_parameter=-2 * h,
        last_parameter=2 * h,
    )
    assert len(components) == 1
    assert len(components[0]) == 2 * h + 1
    assert len(components[0]) <= tangent_component_point_bound(h * h, 1, 1)


def test_steeper_primitive_direction_improves_the_budget() -> None:
    D = 10_000
    additive = tangent_patch_fourth_trace_coefficient(D, 1, 1)
    steep = tangent_patch_fourth_trace_coefficient(D, 5, 7)
    assert steep < additive
    assert steep < 16 * D // 35 + 500


def test_every_bruteforce_component_obeys_the_envelope() -> None:
    for r, s in ((1, 2), (2, 3), (3, 5), (7, 4)):
        for center_shift in (-300, -50, 0, 80, 500):
            components = integer_band_components(
                a0=10_000,
                b0=9_000,
                row_step=r,
                column_step=s,
                product_center=90_000_000 + center_shift,
                product_half_width=200,
                first_parameter=-100,
                last_parameter=100,
            )
            bound = tangent_component_point_bound(200, r, s)
            assert all(len(component) <= bound for component in components)
