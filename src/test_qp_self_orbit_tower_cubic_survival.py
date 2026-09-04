from fractions import Fraction
from math import ceil, exp, floor

from qp_self_orbit_tower_cubic_survival import (
    actual_prime_tower_replay,
    aligned_cubic_beta,
    aligned_near_cube_residual,
    balanced_rectangle_certificate,
    balanced_rectangle_ranges,
    canonical_tower_cubic_fixture,
    embedded_reciprocal_phase,
    tower_label,
    tower_point,
)


def test_critical_tower_fixture_is_primitive_and_scale_exact() -> None:
    fixture = canonical_tower_cubic_fixture(2)
    assert fixture.fan_scale == 2**8
    assert fixture.long_scale == 2**25
    assert fixture.q == 2 * 2**33
    assert fixture.degree == 2**16
    assert fixture.top_frequency == 2 * 2**17
    assert fixture.packet_radius_squared == fixture.degree
    assert fixture.packet_remainder == fixture.fan_scale
    assert fixture.reflected_anchor == (
        fixture.fan_scale * fixture.long_scale - 1,
        fixture.fan_scale * (fixture.long_scale + 1) - 1,
    )


def test_balanced_unimodular_rectangle_lies_in_one_full_self_orbit() -> None:
    fixture = canonical_tower_cubic_fixture(2)
    certificate = balanced_rectangle_certificate(fixture)
    assert certificate.labels_are_injective
    assert certificate.all_labels_within_degree
    assert certificate.lies_in_algebraic_nine_tenths_eleven_tenths_shell
    assert certificate.point_count == certificate.m_count * certificate.n_count

    shell_lower = ceil((fixture.q / 2.0) * exp(-0.2))
    shell_upper = floor((fixture.q / 2.0) * exp(0.2))
    assert shell_lower <= certificate.minimum_coordinate
    assert certificate.maximum_coordinate <= shell_upper

    m_values, n_values = balanced_rectangle_ranges(fixture)
    samples = (
        (m_values.start, n_values.start),
        (m_values.stop - 1, n_values.stop - 1),
        ((m_values.start + m_values.stop) // 2, n_values.start),
    )
    for m, n in samples:
        b, B = tower_point(fixture, m, n)
        c, C = fixture.anchor
        assert c * b - C * B == tower_label(fixture, m, n)


def test_orbit_kernel_is_exactly_the_aligned_completed_strip_kernel() -> None:
    fixture = canonical_tower_cubic_fixture(2)
    m_values, n_values = balanced_rectangle_ranges(fixture)
    first = (m_values.start + 3, n_values.start + 5)
    second = (m_values.stop - 7, n_values.stop - 11)
    orbit_phase, completed_phase = embedded_reciprocal_phase(
        fixture, first, second
    )
    assert orbit_phase == completed_phase


def test_aligned_cubic_frequency_and_cleared_residual_are_exact() -> None:
    fixture = canonical_tower_cubic_fixture(2)
    u = fixture.fan_scale
    direct, aligned = aligned_cubic_beta(fixture, u)
    assert direct == aligned
    assert aligned == 1 + Fraction(1, fixture.long_scale)

    a = fixture.top_frequency // 4
    b = round(a * direct)
    residual = aligned_near_cube_residual(fixture, a, b, u)
    assert residual.phase_error == residual.normalized_residual
    # The S/R-1 perturbation is at the natural Fejer width 1/F.
    assert abs(a * (aligned - 1)) <= 1 / fixture.fan_scale


def test_finite_actual_prime_anchor_replays_the_same_aligned_tower() -> None:
    replay = actual_prime_tower_replay()
    assert replay.anchor == (8_000_000_221, 8_000_000_011)
    assert replay.fan_scale == 210
    assert replay.long_scale == 38_095_238
    assert replay.euclidean_remainder == 31
    assert replay.reflected_anchor == (
        replay.fan_scale * replay.long_direction[0]
        - replay.euclidean_remainder * replay.short_complement[0],
        replay.fan_scale * replay.long_direction[1]
        - replay.euclidean_remainder * replay.short_complement[1],
    )
    assert replay.labels_are_injective
    assert replay.maximum_absolute_label < replay.degree
    assert replay.lies_in_nine_tenths_eleven_tenths_shell
    assert replay.point_count == len(replay.m_values) * len(replay.n_values)
