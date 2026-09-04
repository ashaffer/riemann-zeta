from math import ceil, exp, floor

from qp_four_completion_bezout_token import BezoutTokenChart
from qp_scattered_token_search import full_integer_shell
from qp_self_orbit_adversarial_lab import physical_orbit_tokens
from qp_self_orbit_dynamic_packets import dynamic_packet_decomposition
from qp_self_orbit_small_small_tower import (
    anchor_remainder,
    certify_hard_direction_collapse,
    certify_interline_separation,
    certify_tower_line_count,
    exact_stationary_gradient_gap_lower_bound,
    tower_coordinate_ledger,
    two_direction_identity,
)


def test_two_direction_determinant_identities() -> None:
    anchor = (104_467, 111_006)
    hard = (17, 16)
    directions = ((1, 1), (17, 16), (33, 31), (50, 47))
    for direction in directions:
        first, second = two_direction_identity(anchor, hard, direction)
        assert first[0] == first[1]
        assert second[0] == second[1]


def test_hard_direction_absorbs_every_realized_radius_direction() -> None:
    q, D, radius = 200_000, 371, 20
    anchor = (104_467, 111_006)
    points = physical_orbit_tokens(
        BezoutTokenChart.canonical(*anchor),
        range(-D, D + 1),
        full_integer_shell(q),
    )
    decomposition = dynamic_packet_decomposition(anchor, D, radius, points)
    directions = tuple(
        component.direction
        for component in decomposition.components
        if component.direction is not None
    )
    certificate = certify_hard_direction_collapse(
        anchor, D, radius, (17, 16), directions
    )
    assert certificate.all_parallel
    assert abs(certificate.hard_remainder) == 157
    assert set(directions) == {(17, 16)}


def test_tower_coordinates_line_count_and_macroscopic_gap() -> None:
    q, D, radius = 200_000, 371, 20
    anchor = (104_467, 111_006)
    direction = (17, 16)
    points = physical_orbit_tokens(
        BezoutTokenChart.canonical(*anchor),
        range(-D, D + 1),
        full_integer_shell(q),
    )
    for label, point in points.items():
        ledger = tower_coordinate_ledger(anchor, direction, point)
        assert ledger.label == label
        assert ledger.first_identity[0] == ledger.first_identity[1]
        assert ledger.second_identity[0] == ledger.second_identity[1]

    count = certify_tower_line_count(anchor, D, direction, points)
    # The dynamic decomposition has 49 nontrivial lines and one singleton.
    assert count.line_count == 50
    assert count.line_count <= abs(anchor_remainder(anchor, direction)) == 157

    by_line: dict[int, list[tuple[int, int]]] = {}
    for point in points.values():
        index = direction[0] * point[1] - direction[1] * point[0]
        by_line.setdefault(index, []).append(point)
    first_index, second_index = sorted(by_line)[:2]
    separation = certify_interline_separation(
        anchor,
        D,
        direction,
        by_line[first_index][0],
        by_line[second_index][0],
    )
    assert separation.first_distance * abs(separation.remainder) >= (
        separation.first_numerator_lower_bound
    )
    assert separation.second_distance * abs(separation.remainder) >= (
        separation.second_numerator_lower_bound
    )


def test_stationary_gradient_cells_have_power_separation() -> None:
    q, D, radius = 200_000, 371, 20
    anchor = (104_467, 111_006)
    direction = (17, 16)
    lower = ceil((q / 2) * exp(-0.2))
    upper = floor((q / 2) * exp(0.2))
    K = q // (radius * radius)
    gap = exact_stationary_gradient_gap_lower_bound(
        q, K, lower, upper, anchor, D, direction
    )
    assert gap > 1


def test_content_swap_alias_survives_inside_unique_tower() -> None:
    # Gradient-cell separation is not scalar action separation.  These two
    # distinct ordered U-line pairs have exactly the same physical product.
    anchor = (50_000, 50_007)
    direction = (1, 1)
    first_left = (42_891, 42_885)
    first_right = (57_184, 57_176)
    second_left = (57_188, 57_180)
    second_right = (42_888, 42_882)
    assert anchor_remainder(anchor, direction) == -7
    assert first_left[0] * first_right[1] == second_left[0] * second_right[1]
    first_lines = (
        direction[0] * first_left[1] - direction[1] * first_left[0],
        direction[0] * first_right[1] - direction[1] * first_right[0],
    )
    second_lines = (
        direction[0] * second_left[1] - direction[1] * second_left[0],
        direction[0] * second_right[1] - direction[1] * second_right[0],
    )
    assert first_lines == (-6, -8)
    assert second_lines == (-8, -6)
