import numpy as np

from qp_two_star_interval_peeling_barrier import (
    carrier_degrees,
    cyclic_second_determinants,
    factorial_row_count,
    integer_tangent_packet,
    latin_two_star_fixture,
    pair_incidence_matrix,
    pair_multiplicities,
    row_pair_interval_loads,
    triangular_tangent_two_star,
    two_star_count,
)


def test_latin_fixture_has_all_three_pair_uniqueness_properties() -> None:
    fixture = latin_two_star_fixture(groups=3, degree=5, interval_count=19)
    for counter in pair_multiplicities(fixture.triples).values():
        assert max(counter.values()) == 1


def test_every_short_row_pair_cell_is_sparse() -> None:
    fixture = latin_two_star_fixture(groups=3, degree=5, interval_count=19)
    assert max(row_pair_interval_loads(fixture).values()) == 1


def test_two_star_and_factorial_counts_saturate_formulas() -> None:
    groups = 3
    degree = 5
    fixture = latin_two_star_fixture(groups, degree, interval_count=19)
    support = groups * degree
    assert set(carrier_degrees(fixture).values()) == {degree}
    assert two_star_count(fixture) == support * degree * (degree - 1)

    matrix = pair_incidence_matrix(fixture)
    assert np.all(matrix.sum(axis=0) == degree)
    assert np.all(matrix.sum(axis=1) == degree)
    assert round(np.linalg.norm(matrix, ord=2), 10) == degree
    assert factorial_row_count(matrix) == support * degree * (degree - 1) ** 2


def test_triangular_tangent_formula() -> None:
    length = 7
    multiplicities = list(range(1, length + 1)) + list(
        range(length - 1, 0, -1)
    )
    direct = sum(value * (value + 1) for value in multiplicities)
    assert direct == triangular_tangent_two_star(length)


def test_full_integer_tangent_packet_obeys_product_window() -> None:
    center = 100_000
    length = 7
    q = 2 * center
    width = 100 * length**2
    triples = integer_tangent_packet(center, length)
    assert all(abs(8 * a * b * c - q**3) <= q * width for a, b, c in triples)
    colors_by_carrier: dict[int, set[int]] = {}
    for _, carrier, color in triples:
        colors_by_carrier.setdefault(carrier, set()).add(color)
    direct = sum(len(colors) * (len(colors) - 1) for colors in colors_by_carrier.values())
    assert direct == triangular_tangent_two_star(length)


def test_cyclic_second_determinants_detect_nonconstant_cycle() -> None:
    assert cyclic_second_determinants((101, 103, 107, 109)) == (
        198,
        -222,
        -1074,
        1026,
    )
