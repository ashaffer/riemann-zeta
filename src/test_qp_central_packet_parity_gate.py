from fractions import Fraction
from itertools import product
import math

import numpy as np

from qp_central_packet_parity_gate import (
    brute_force_minimum_signed_triple_numerator,
    central_packet_parity_certificate,
    doubled_half_integer_distances,
    exact_exponent_ledger,
    verify_reflection_box_leading_terms,
)
from qp_transverse_joint_invariant_lab import (
    FULL_APERTURE,
    continuum_moment_model,
)


def test_project_exponent_ledger_is_exact_and_positive() -> None:
    dimension, loss, gain, net = exact_exponent_ledger(
        aperture_exponent=Fraction(50, 33),
        packet_epsilon=Fraction(0),
        spline_order=2,
    )
    assert dimension == Fraction(1, 2)
    assert loss == Fraction(3, 4)
    assert gain == Fraction(34, 33)
    assert net == Fraction(37, 132) > 0


def test_odd_parity_includes_repetitions_and_all_reflection_corners() -> None:
    N = 100
    nodes = tuple(range(97, 105))
    distances = doubled_half_integer_distances(N, nodes)
    assert all(distance % 2 == 1 for distance in distances)
    assert brute_force_minimum_signed_triple_numerator(distances) == 1
    # This enumerates repeated blocks, all eight cosine sign patterns, and
    # every choice of the upper/lower endpoint in each reflected block.
    assert verify_reflection_box_leading_terms(N, nodes) == 1


def test_exact_taylor_certificate_bounds_actual_signed_log_frequencies() -> None:
    N = 1_000_000
    nodes = (N - 2, N - 1, N, N + 1, N + 2, N + 3)
    certificate = central_packet_parity_certificate(
        N,
        nodes,
        packet_epsilon=Fraction(1, 10),
        spline_order=8,
    )
    assert certificate.maximum_reflection_cluster_size == 2
    assert certificate.interpolation_corner_leading_terms_consistent
    assert certificate.signed_cubic_log_frequency_lower > 0
    assert certificate.net_cubic_decay_exponent > 0

    Y = N + 0.5
    frequencies = [abs(math.log(node / Y)) for node in nodes]
    actual_minimum = min(
        abs(signs[0] * first + signs[1] * second + signs[2] * third)
        for first, second, third in product(frequencies, repeat=3)
        for signs in product((-1, 1), repeat=3)
    )
    assert actual_minimum + 1.0e-15 >= float(
        certificate.signed_cubic_log_frequency_lower
    )


def test_repeated_normalized_reflection_modes_have_stable_gram_and_tiny_cubic() -> None:
    # Floating stress test of the exact divided-difference argument.  The
    # theorem does not depend on this tolerance-based calculation.
    N = 100_000
    Y = N + 0.5
    bandwidth = Y**FULL_APERTURE
    distances = (0.5, 1.5, 2.5)
    nodes = np.array(
        [
            frequency
            for distance in distances
            for frequency in (
                -math.log(1.0 - distance / Y),
                math.log(1.0 + distance / Y),
            )
        ]
    )
    model = continuum_moment_model(
        nodes,
        bandwidth,
        spline_order=8,
        eigenvalue_tolerance=1.0e-16,
    )
    modes: list[np.ndarray] = []
    for index in range(len(distances)):
        left = 2 * index
        right = left + 1
        scaled_gap = bandwidth * abs(nodes[left] - nodes[right])
        mode = np.zeros(len(nodes))
        mode[left] = 1.0 / min(1.0, scaled_gap)
        mode[right] = -mode[left]
        modes.append(mode)

    gram = np.array(
        [[first @ model.covariance @ second for second in modes] for first in modes]
    )
    assert np.min(np.diag(gram)) > 0.1
    assert np.max(np.abs(gram - np.diag(np.diag(gram)))) < 1.0e-6

    maximum_cubic = max(
        abs(
            np.einsum(
                "i,j,k,ijk",
                modes[first],
                modes[second],
                modes[third],
                model.third_central,
                optimize=True,
            )
        )
        for first, second, third in product(range(len(modes)), repeat=3)
    )
    assert maximum_cubic < 1.0e-6
