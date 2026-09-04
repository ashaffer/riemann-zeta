from fractions import Fraction
from math import gcd

from qp_coupled_cusp_fejer_inverse import reduced_symmetric_cusp_data
from qp_residual_phase_jet_collision import (
    content_is_unique_in_narrow_left_band,
    enumerate_transverse_non_square_residuals,
    non_square_n_one_residual_family,
    phase_lift_exponent_ledger,
    reconstruct_reduced_data_from_fingerprint,
    reflected_point,
    reflection_jet_identity,
    residual_frequency_support_ledger,
    residual_jet_collision_audit,
    residual_phase_jet,
)


def test_exact_regular_and_cubic_action_defects() -> None:
    point = reduced_symmetric_cusp_data(349, 74, 13, 20)
    jet = residual_phase_jet(point)
    assert (point.g, point.p, point.d, point.n) == (1, 33, 7, -1)
    assert jet.parity_divisor == 2
    assert jet.regular_action_defect == Fraction(349, 232650)
    assert jet.caustic_action_defect == Fraction(1, 116325)
    assert (
        jet.caustic_action_defect
        / (jet.parity_divisor * jet.regular_action_defect)
        == Fraction(-point.n, point.Q)
    )
    assert jet.regular_tangent_curvature == Fraction(1185921, 520)


def test_oriented_fingerprint_reconstructs_primitive_data() -> None:
    for point in (
        reduced_symmetric_cusp_data(349, 74, 13, 20),
        reduced_symmetric_cusp_data(349, -74, 20, 13),
        non_square_n_one_residual_family(2, 3),
        non_square_n_one_residual_family(5, 8),
    ):
        jet = residual_phase_jet(point)
        recovered = reconstruct_reduced_data_from_fingerprint(
            point.Q,
            jet.parity_divisor,
            jet.regular_tangent_curvature,
            jet.regular_action_defect,
            jet.caustic_action_defect,
        )
        assert recovered == {
            "p": point.p,
            "d": point.d,
            "y": point.y,
            "n": point.n,
            "ell": point.p * point.p - point.d * point.d,
        }


def test_reflection_is_the_exact_unoriented_collision() -> None:
    point = non_square_n_one_residual_family(4, 7)
    reflected = reflected_point(point)
    left, right = residual_phase_jet(point), residual_phase_jet(reflected)
    assert left.unoriented_fingerprint == right.unoriented_fingerprint
    assert left.oriented_fingerprint != right.oriented_fingerprint
    assert all(reflection_jet_identity(point).values())
    assert (reflected.y, reflected.r, reflected.s) == (
        -point.y,
        point.s,
        point.r,
    )


def test_infinite_family_stays_off_every_closed_chart() -> None:
    for multiplier in range(2, 7):
        for d in range(3, 10):
            point = non_square_n_one_residual_family(multiplier, d)
            jet = residual_phase_jet(point)
            assert point.g % (point.d * point.d) != 0
            assert jet.scaled_v == 0
            assert jet.scaled_z == 2 * d
            assert jet.scaled_residual == 4 * d * d
            assert jet.scaled_z != 0 and jet.scaled_residual != 0


def test_q349_action_only_near_collision_is_split_by_curvature() -> None:
    first = residual_phase_jet(reduced_symmetric_cusp_data(349, 74, 13, 20))
    second = residual_phase_jet(reduced_symmetric_cusp_data(349, 102, 23, 42))
    assert (first.point.n, second.point.n) == (-1, -1)
    gap = abs(first.caustic_action_defect - second.caustic_action_defect)
    # This is far below even the coarse reciprocal scale 1/Q, so a scalar
    # action character does not separate the packets.  Curvature does.
    assert gap < Fraction(1, 349)
    assert first.regular_tangent_curvature != second.regular_tangent_curvature
    assert first.unoriented_fingerprint != second.unoriented_fingerprint


def test_q349_finite_residual_scan_has_only_reflection_collisions() -> None:
    points = enumerate_transverse_non_square_residuals(349, 43, 43)
    audit = residual_jet_collision_audit(points)
    assert audit.point_count == 12
    assert audit.reflection_orbit_count == 6
    assert audit.maximum_cubic_character_multiplicity == 2
    assert audit.nonreflection_cubic_character_collisions == 0
    assert audit.maximum_unoriented_fingerprint_multiplicity == 2
    assert audit.nonreflection_full_jet_collisions == 0


def test_narrow_band_makes_content_unique() -> None:
    point = non_square_n_one_residual_family(3, 5)
    assert content_is_unique_in_narrow_left_band(
        point.Q, point.y, point.p, point.d, abs(point.e)
    )


def test_tangent_curvature_is_injective_on_primitive_directions() -> None:
    seen: dict[tuple[int, Fraction], tuple[int, int]] = {}
    for p in range(2, 90):
        for d in range(1, p):
            if gcd(p, d) != 1:
                continue
            parity = gcd(p + d, p - d)
            curvature = Fraction(8 * p**4, parity**2 * (p * p - d * d))
            key = parity, curvature
            assert key not in seen
            seen[key] = (p, d)


def test_action_wrap_and_frequency_support_ledgers() -> None:
    lifts = phase_lift_exponent_ledger()
    assert lifts["quadratic_wrap_count"] == Fraction(13, 48)
    assert lifts["cubic_action_size"] == Fraction(-5, 8)
    assert lifts["wrap_count_margin"] == Fraction(11, 48)

    support = residual_frequency_support_ledger()
    assert support["regular_support_margin_at_floor"] == Fraction(1, 10)
    assert support["regular_residual_strip_width"] == Fraction(1, 20)
    assert support["cubic_support_deficit_at_floor"] == Fraction(61, 160)
