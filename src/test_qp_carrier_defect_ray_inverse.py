import math

import pytest

from qp_carrier_defect_ray_inverse import (
    coherent_ray_certificate,
    defect_ray_ledger,
    determinant_fourier_prediction,
    determinant_fourier_sum,
    prime_rectangle_wedge_fixture,
    ramanujan_sum,
)


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def test_all_prime_fixture_is_literal_pair_unique_product_mask() -> None:
    q, half_width, triples = prime_rectangle_wedge_fixture()
    nodes = {coordinate for triple in triples for coordinate in (triple.a, triple.b, triple.c)}
    assert len(nodes) == 8
    assert all(_is_prime(node) for node in nodes)
    assert tuple(triple.residual(q) for triple in triples) == (
        17_066_235,
        18_768_395,
        7_565_163,
        10_476_011,
    )
    assert max(abs(triple.residual(q)) for triple in triples) <= half_width


def test_common_carrier_gram_decomposes_exactly_into_physical_defect_rays() -> None:
    _, _, triples = prime_rectangle_wedge_fixture()
    c11, c12, c21, c22 = 26_003, 25_537, 24_329, 23_893
    vector = {c11: 1.0, c12: -1.0, c21: 1.0, c22: -1.0}
    ledger = defect_ray_ledger(triples, vector)
    rays = ledger["rays"]
    assert set(rays) == {-42, 42, -36, 36}
    assert rays[42] == pytest.approx(1.0)
    assert rays[-42] == pytest.approx(1.0)
    assert rays[36] == pytest.approx(1.0)
    assert rays[-36] == pytest.approx(1.0)
    assert ledger["diagonal_energy"] == pytest.approx(4.0)
    assert ledger["action_energy"] == pytest.approx(8.0)
    assert ledger["reconstructed_energy"] == pytest.approx(8.0)


def test_exact_centering_preserves_the_actual_ray_certificate() -> None:
    q, half_width, triples = prime_rectangle_wedge_fixture()
    vector = {26_003: 1.0, 25_537: -1.0, 24_329: 1.0, 23_893: -1.0}
    certificate = coherent_ray_certificate(triples, vector, q, half_width)
    # The input and output both have mean zero on this exact fixture.
    assert certificate["centered_energy"] == pytest.approx(8.0)
    assert certificate["forced_nonzero_ray_total"] == pytest.approx(4.0)
    assert certificate["largest_observed_paired_ray"] == pytest.approx(2.0)
    assert certificate["largest_observed_paired_ray"] >= certificate[
        "forced_single_ray_lower_bound"
    ]


@pytest.mark.parametrize(
    "modulus,numerator,frequencies",
    [(5, 2, (1, 2, 3, 4)), (7, 3, (2, 5, 1, 6))],
)
def test_determinant_phase_is_exactly_fourier_self_dual(
    modulus: int, numerator: int, frequencies: tuple[int, int, int, int]
) -> None:
    assert determinant_fourier_sum(
        modulus, numerator, frequencies
    ) == pytest.approx(
        determinant_fourier_prediction(modulus, numerator, frequencies)
    )


def test_rational_arc_average_groups_the_same_defect_rays() -> None:
    _, _, triples = prime_rectangle_wedge_fixture()
    vector = {26_003: 1.0, 25_537: -1.0, 24_329: 1.0, 23_893: -1.0}
    rays = defect_ray_ledger(triples, vector)["rays"]
    modulus = 5
    direct = sum(
        sum(
            value
            * __import__("cmath").exp(
                2j * __import__("math").pi * numerator * defect / modulus
            )
            for defect, value in rays.items()
        )
        for numerator in range(modulus)
        if math.gcd(numerator, modulus) == 1
    )
    grouped = sum(
        value * ramanujan_sum(modulus, defect)
        for defect, value in rays.items()
    )
    assert direct == pytest.approx(grouped)
