from fractions import Fraction
from math import gcd

from qp_high_p_newton_information import (
    adjacent_primitive_tangents,
    aligned_packet_correlation,
    harmonic_torus_resolution,
    high_p_information_exponents,
    parity_reduced_direction,
    primitive_tangent_normal,
    projective_newton_signature,
    sampled_reciprocal_phase,
    stationary_residual,
    stationary_support_certificate,
    torus_distance,
)
from qp_residual_phase_jet_collision import non_square_n_one_residual_family


def test_primitive_normal_and_p_squared_divisibility() -> None:
    p, d = 11, 3
    chi, a, b = parity_reduced_direction(p, d)
    normal = primitive_tangent_normal(p, d)
    assert gcd(gcd(abs(normal[0]), abs(normal[1])), abs(normal[2])) == 1
    # The canonical zero-dual mode is stationary.
    assert stationary_residual(p, d, (0, a * a, b * b)) == 0
    # Every enumerated stationary mode has p^2|m.
    for minus_m in range(-2 * p * p, 2 * p * p + 1):
        for h in range(-20, 21):
            for k in range(-20, 21):
                if stationary_residual(p, d, (minus_m, h, k)) == 0:
                    assert (-minus_m) % (p * p) == 0
    assert chi in (1, 2)


def test_universal_high_p_support_gap_and_parity_constant() -> None:
    certificate = stationary_support_certificate(p=11, d=2, cutoff=25)
    assert 11 * 11 > 4 * 25
    assert certificate.only_zero_mode

    # Merely p^2>H is not enough with parity chi=2: (a^2,b^2) can fit.
    plateau = stationary_support_certificate(p=9, d=1, cutoff=25)
    assert 9 * 9 > 25
    assert not plateau.only_zero_mode
    assert (plateau.a, plateau.b) == (5, 4)
    assert stationary_residual(9, 1, (0, 25, 16)) == 0


def test_affine_m_is_exactly_invisible_in_newton_quotient() -> None:
    Q = 101
    t = Fraction(11, 20)
    base = projective_newton_signature(Q, t, (0, 7, -3))
    shifted = projective_newton_signature(Q, t, (-17, 7, -3))
    assert base == shifted


def test_adjacent_direction_gap_and_supported_signature_closeness() -> None:
    Q, p, H = 10007, 101, 20
    left, right, gap = adjacent_primitive_tangents(p)
    assert gap == Fraction(1, p * (p + 2))
    maximum = Fraction()
    # Exhaust a small supported box; m is omitted because it is invisible.
    for h in range(-H, H + 1):
        for k in range(-H, H + 1):
            left_jet = projective_newton_signature(Q, left, (0, h, k))
            right_jet = projective_newton_signature(Q, right, (0, h, k))
            for x, y in zip(left_jet, right_jet):
                maximum = max(maximum, torus_distance(x, y))
    # The observed scale is H/p^2, up to an absolute collar constant.
    assert maximum < Fraction(100 * H, p * p)


def test_genuine_residual_family_contains_farey_scale_neighbors() -> None:
    multiplier, d = 3, 20
    first = non_square_n_one_residual_family(multiplier, d)
    second = non_square_n_one_residual_family(multiplier, d + 1)
    t_first = Fraction(first.p + first.d, 2 * first.p)
    t_second = Fraction(second.p + second.d, 2 * second.p)
    assert abs(t_first - t_second) == Fraction(1, 2 * first.p * second.p)
    for point in (first, second):
        assert point.n == 1
        assert point.g % (point.d * point.d) != 0


def test_full_sampled_packets_become_coherent() -> None:
    Q, p, H, N = 20011, 401, 7, 30
    left, right, _ = adjacent_primitive_tangents(p)
    for frequency in ((0, H, 0), (0, 0, H), (-H, H, -H)):
        left_phases = sampled_reciprocal_phase(Q, left, frequency, N)
        right_phases = sampled_reciprocal_phase(Q, right, frequency, N)
        assert aligned_packet_correlation(left_phases, right_phases) > 0.99


def test_information_threshold_ledger() -> None:
    powers = high_p_information_exponents()
    assert powers["stationary_support_edge"] == Fraction(17, 32)
    assert powers["newton_coefficient_eta_alias"] == Fraction(29, 48)
    assert powers["phase_jet_certificate_alias"] == Fraction(77, 96)
    assert powers["sampled_packet_coherence"] == Fraction(7, 8)
    assert powers["sampled_phase_eta_alias"] == Fraction(91, 96)
    assert powers["fixed_Q_eta_signature_cluster"] == Fraction(41, 48)
    assert powers["physical_slope_rounding_cluster"] == Fraction(329, 480)


def test_full_harmonic_signature_resolves_base_torus_gap() -> None:
    noise, harmonics = Fraction(1, 100), 20
    gap = Fraction(1, 2500)
    assert harmonic_torus_resolution(gap, harmonics, noise) == noise / harmonics

    # A gap visible to an intermediate harmonic is correctly rejected.
    try:
        harmonic_torus_resolution(Fraction(1, 40), harmonics, noise)
    except ValueError:
        pass
    else:
        raise AssertionError("a resolved harmonic gap was accepted as an alias")
