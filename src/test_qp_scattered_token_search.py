from qp_scattered_token_search import (
    actual_prime_parallel_fixture,
    broad_scattered_fixture,
    integer_parallel_fixture,
    one_orbit_middle_ledger,
    orbit_reflection_ledger,
    physical_center_digital_strip,
)
from qp_four_completion_bezout_token import BezoutTokenChart


def test_integer_rich_root_is_one_parallel_token_chart() -> None:
    audit = integer_parallel_fixture()
    assert audit.D == 371
    assert audit.root_degree == 18
    assert audit.maximum_neighbor_degree == 18
    assert audit.neighbourhood_degree_sum == 271
    assert audit.center_line_mass == 271
    assert audit.center_line == (1, -1, -1)
    assert audit.endpoint_line_mass == 271
    assert audit.endpoint_line == (1, -1, 1)
    assert audit.parallel_carriers


def test_broad_root_has_only_two_paths_off_its_best_center_line() -> None:
    audit = broad_scattered_fixture()
    assert audit.neighbourhood_degree_sum == 7
    assert audit.root_degree == 4
    assert audit.nonreturn_paths == 3
    assert audit.center_line_mass == 5


def test_larger_actual_prime_shell_is_also_one_parallel_chart() -> None:
    audit = actual_prime_parallel_fixture()
    assert audit.q == 10_604_226
    assert audit.D == 2548
    assert audit.node_count == 137_783
    assert audit.root_degree == 4
    assert audit.maximum_neighbor_degree == 3
    assert audit.neighbourhood_degree_sum == 10
    assert audit.nonreturn_paths == 6
    assert audit.center_line_mass == 10
    assert audit.center_line == (1, -6, -6)
    assert audit.endpoint_line_mass == 10
    assert audit.endpoint_line == (1, -6, 6)
    assert audit.parallel_carriers


def test_endpoint_tokens_are_the_reflected_center_orbit() -> None:
    chart = BezoutTokenChart.canonical(108_551, 111_297)
    reflection = orbit_reflection_ledger(chart, h=77, n_at_minus_h=-26)
    assert reflection.center_token_at_minus_h == (-77, -26)
    assert reflection.endpoint_token_at_h == (77, 26)
    assert reflection.endpoint_at_h == tuple(reversed(reflection.center_at_minus_h))

    middle = one_orbit_middle_ledger(
        chart, center_token=(-162, -54), reflected_source_token=(-77, -26)
    )
    assert middle.endpoint_token == (77, 26)
    assert middle.endpoint == tuple(reversed(middle.reflected_source_center))
    assert middle.left_product == middle.center[0] * middle.endpoint[0]
    assert middle.right_product == middle.center[1] * middle.endpoint[1]


def test_width_one_digital_strip_still_has_many_exact_directions() -> None:
    audit = physical_center_digital_strip(
        200_000, 371, (92_519, 87_756)
    )
    assert len(audit.points) == 289
    assert audit.distinct_difference_directions == 344
    assert audit.maximum_affine_line_size == 18
    assert audit.affine_line_cover_lower_bound == 17
    assert audit.maximizing_line == (1, -3, -10)
