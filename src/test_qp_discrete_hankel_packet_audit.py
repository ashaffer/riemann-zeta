import math

import numpy as np
import pytest

from qp_discrete_hankel_packet_audit import (
    color_layer,
    high_denominator_packet_ledger,
    parabolic_sidon_cayley_matrix,
    schatten_fourth_power,
    sidon_cayley_obstruction_ledger,
    shift_height_coordinates,
    tangent_hankel_matrix,
    tangent_packet_hilbert_schmidt_bound,
    tangent_product_increment,
)


def test_shift_height_map_is_unimodular_and_has_the_prescribed_shift() -> None:
    for r, s, e, h in ((7, 5, 3, 101), (17, 19, -4, 73), (101, 98, 9, 11)):
        coordinates = shift_height_coordinates(r, s, e, h)
        assert coordinates.determinant == -1
        assert coordinates.cross_shift == e
        assert (
            coordinates.second_product_coefficient
            - coordinates.first_product_coefficient
            == e
        )


def test_nonzero_shift_range_has_a_subunit_product_interval_at_project_scale() -> None:
    q = 10**12 + 39
    degree = int(q ** (16 / 33))
    threshold = math.ceil(q / degree)
    ledger = high_denominator_packet_ledger(q, degree, threshold)
    assert ledger.nonzero_shift_possible
    assert ledger.subunit_product_interval
    assert ledger.product_interval_length_bound <= degree * degree / q
    # Up to endpoint roundings, the shift-height rectangle has area D.
    assert ledger.candidate_area_bound <= 3 * degree


def test_exact_tangent_product_identity_and_literal_window() -> None:
    order = 24
    center = 10**7
    degree = 100 * order * order
    for i in range(order):
        for j0 in range(order):
            j = 2 * order + j0
            a = center + i
            b = center + j
            c = center - i - j
            increment = tangent_product_increment(center, i, j)
            assert a * b * c - center**3 == increment
            assert abs(8 * increment) < (2 * center) * degree


def test_flat_tangent_packet_is_coherent_and_saturates_order_squared() -> None:
    order = 31
    weights = np.ones(2 * order - 1) / math.sqrt(2 * order - 1)
    matrix = tangent_hankel_matrix(weights, order)
    expected = order**4 / (2 * order - 1) ** 2
    assert schatten_fourth_power(matrix) == pytest.approx(expected)
    assert expected >= order * order / 4


def test_whole_packet_closes_by_hilbert_schmidt_for_arbitrary_weights() -> None:
    rng = np.random.default_rng(20260822)
    order = 27
    weights = rng.normal(size=2 * order - 1) + 1j * rng.normal(
        size=2 * order - 1
    )
    matrix = tangent_hankel_matrix(weights, order)
    assert schatten_fourth_power(matrix) <= (
        tangent_packet_hilbert_schmidt_bound(weights, order) * (1 + 1e-12)
    )


def test_color_layers_have_no_cotlar_decay_inside_the_packet() -> None:
    order = 25
    central = range(order - 1, order + 5)
    layers = {index: color_layer(order, index) for index in central}
    for first in central:
        for second in central:
            product = layers[first] @ layers[second].T
            assert np.linalg.norm(product, ord=2) == pytest.approx(1.0)


def test_parabolic_cayley_layers_are_matchings_with_sidon_codegrees() -> None:
    prime = 7
    matrix = parabolic_sidon_cayley_matrix(prime)
    assert np.all(matrix.sum(axis=0) == prime)
    assert np.all(matrix.sum(axis=1) == prime)
    gram = matrix @ matrix.T
    assert np.all(np.diag(gram) == prime)
    off_diagonal = gram[~np.eye(prime * prime, dtype=bool)]
    assert np.max(off_diagonal) == 1


def test_sidon_cayley_graph_has_the_full_tensor_zero_mode_loss() -> None:
    prime = 7
    matrix = parabolic_sidon_cayley_matrix(prime)
    # z is constant 1/sqrt(p), hence u=z tensor z is constant 1/p.
    tensor = np.full(prime * prime, 1 / prime)
    assert np.vdot(tensor, tensor).real == pytest.approx(1.0)
    assert np.vdot(matrix @ tensor, matrix @ tensor).real == pytest.approx(prime**2)
    ledger = sidon_cayley_obstruction_ledger(prime)
    assert ledger.maximum_distinct_row_codegree == 1
    assert ledger.tensor_zero_mode_energy == prime**2
    assert ledger.violation_factor == prime
