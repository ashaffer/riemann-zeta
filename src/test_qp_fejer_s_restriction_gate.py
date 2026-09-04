from fractions import Fraction
from math import isclose

from qp_fejer_s_restriction_gate import (
    convolution,
    convolution_energy,
    critical_restriction_exponents,
    interval_self_energy,
    norm_squared,
    normalized_fejer_value,
    packet_pair_overlap,
    packet_square_function_upper_bound,
    rank_one_overlap,
    restriction_fejer_term_exponents,
    weighted_young_mask_exponent,
)


def test_fejer_riesz_tensor_identity() -> None:
    order = 37
    theta_one = 0.007
    theta_two = -0.011
    overlap = rank_one_overlap(order, theta_one, theta_two, scale=1.7)
    expected = normalized_fejer_value(order, theta_one, 1.7)
    expected *= normalized_fejer_value(order, theta_two, 1.7)
    assert isclose(abs(overlap) ** 2, expected, rel_tol=1.0e-12, abs_tol=1.0e-12)


def test_central_mask_vectors_remain_coherent_after_arbitrary_deletion() -> None:
    order = 101
    for numerator in range(-20, 21):
        theta = numerator / (100.0 * order)
        assert normalized_fejer_value(order, theta) > 0.85


def test_completion_sum_is_exact_additive_convolution() -> None:
    left = {3: 2 - 1j, 8: -0.5 + 2j}
    right = {4: 1 + 3j, 9: -2j}
    result = convolution(left, right)
    assert result[7] == left[3] * right[4]
    assert result[12] == left[3] * right[9] + left[8] * right[4]
    assert result[17] == left[8] * right[9]
    assert isclose(convolution_energy(left, right), norm_squared(result))


def test_tangent_interval_saturates_square_root_restriction_scale() -> None:
    for length in (1, 2, 7, 40):
        raw = interval_self_energy(length)
        normalized = interval_self_energy(length, normalized=True)
        assert raw == Fraction(2 * length**3 + length, 3)
        assert normalized == Fraction(2 * length, 3) + Fraction(1, 3 * length)
        assert normalized <= length
        assert normalized >= Fraction(2 * length, 3)


def test_packet_pair_bounded_overlap_square_function() -> None:
    left_packets = [
        {0: 1 + 1j, 1: 2 - 1j},
        {10: -1j, 11: 0.5},
    ]
    right_packets = [
        {30: 1, 31: -2},
        {50: 2j, 51: 1},
    ]
    overlap = packet_pair_overlap(
        [tuple(packet) for packet in left_packets],
        [tuple(packet) for packet in right_packets],
    )
    assert overlap == 1
    total_left = {key: value for packet in left_packets for key, value in packet.items()}
    total_right = {key: value for packet in right_packets for key, value in packet.items()}
    assert convolution_energy(total_left, total_right) <= packet_square_function_upper_bound(
        left_packets, right_packets
    ) + 1.0e-12


def test_energy_core_and_fejer_exponent_ledger() -> None:
    ledger = critical_restriction_exponents()
    assert ledger.q == Fraction(33, 16)
    assert ledger.reciprocal_bandwidth == Fraction(17, 16)
    assert ledger.pointwise_balanced_core == Fraction(1, 6)
    assert ledger.energy_balanced_core == Fraction(1, 10)
    assert ledger.energy_unbalanced_core == Fraction(1, 6)
    assert ledger.fejer_convolution_norm == Fraction(5, 4)
    assert ledger.fejer_energy == Fraction(5, 2)
    assert ledger.exceptional_sum_count == Fraction(7, 4)

    # Trivial Young closes exactly when m^2 M^3 >= D^(1/2).
    assert weighted_young_mask_exponent(Fraction(1, 10), Fraction(1, 10)) == Fraction(5, 2)
    assert weighted_young_mask_exponent(Fraction(0), Fraction(1, 6)) == Fraction(5, 2)

    norm, weight, total = restriction_fejer_term_exponents(
        Fraction(1, 10), Fraction(1, 8)
    )
    assert norm + weight == total
    assert total == Fraction(5, 4) - Fraction(5, 4) * Fraction(1, 10) - Fraction(3, 2) * Fraction(1, 8)
