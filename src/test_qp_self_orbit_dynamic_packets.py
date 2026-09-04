from collections import Counter
from math import isqrt

from qp_four_completion_bezout_token import BezoutTokenChart
from qp_scattered_token_search import full_integer_shell
from qp_self_orbit_adversarial_lab import (
    multilevel_self_orbit_packet,
    physical_orbit_tokens,
)
from qp_self_orbit_dynamic_packets import (
    dynamic_packet_decomposition,
    orbit_area_ledger,
    rational_convergents,
    reciprocal_lane_hessian,
)


def test_orbit_area_identity_allows_full_label_span() -> None:
    q, D = 200_000, 371
    anchor = (106_319, 106_348)
    points = physical_orbit_tokens(
        BezoutTokenChart.canonical(*anchor),
        range(-D, D + 1),
        full_integer_shell(q),
    )
    labels = (-367, 0, 368)
    ledger = orbit_area_ledger(anchor, labels, tuple(points[t] for t in labels))
    assert max(labels) - min(labels) == 735
    assert ledger.scaled_area == ledger.label_coordinate_expression


def test_dynamic_scale_has_many_translates_but_one_convergent_direction() -> None:
    q, D, radius = 200_000, 371, 20
    fixtures = {
        (106_319, 106_348): ((1, 1), Counter({26: 6, 25: 5})),
        (104_467, 111_006): ((17, 16), Counter({5: 36, 4: 13})),
        (118_951, 95_146): ((4, 5), Counter({10: 11, 11: 1})),
    }
    nodes = full_integer_shell(q)
    for anchor, (direction, sizes) in fixtures.items():
        points = physical_orbit_tokens(
            BezoutTokenChart.canonical(*anchor), range(-D, D + 1), nodes
        )
        audit = dynamic_packet_decomposition(anchor, D, radius, points)
        nontrivial = [
            component for component in audit.components if component.direction is not None
        ]
        assert audit.distinct_nontrivial_directions == (direction,)
        assert Counter(len(component.points) for component in nontrivial) == sizes
        assert all(component.direction_is_principal_convergent for component in nontrivial)
        assert all(
            len(component.points) <= component.label_capacity
            for component in nontrivial
        )
        assert direction[0] / direction[1] in {
            float(value) for value in rational_convergents(anchor[1], anchor[0])
        }


def test_fixed_anchor_multilevel_slice_is_one_dynamic_packet_not_many_translates() -> None:
    m, length, step = 100_000_000_000, 10, 11
    packet = multilevel_self_orbit_packet(m=m, length=length, step=step)
    chart = BezoutTokenChart.canonical(*packet.anchor)
    points: dict[int, tuple[int, int]] = {}
    for translation in range(20 * length, 21 * length + 1):
        point = (m + translation, m + step + translation)
        points[chart.center_to_token(point)[0]] = point
    source_points = [(m - step, m)] + [
        (m - step - level, m - level)
        for level in range(length, 2 * length + 1)
        if level != step
    ]
    for point in source_points:
        points[chart.center_to_token(point)[0]] = point
    radius = 500
    assert isqrt(packet.D) < radius
    audit = dynamic_packet_decomposition(packet.anchor, packet.D, radius, points)
    assert audit.point_count == 22
    assert audit.component_count == audit.nontrivial_component_count == 1
    assert audit.components[0].direction == (1, 1)


def test_reciprocal_lane_hessian_is_strictly_curved_off_coordinate_rulings() -> None:
    ledger = reciprocal_lane_hessian(200_000, 100_003, 99_997, 17, 16)
    assert ledger.hessian_determinant > 0
    assert ledger.mixed_second_derivative > 0
