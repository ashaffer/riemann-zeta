from collections import Counter
from math import gcd, sqrt

from qp_fixed_s_packet_dispersion_audit import (
    actual_prime_power_defect_data,
    complementary_divisor_data,
    counterfixture_point_set,
    exact_center_prime_fixtures,
    exact_fixed_sum_identities,
    has_collinear_triple,
    has_nontrivial_three_ap,
    narrow_prime_power_bases,
    off_resonant_counterfixture,
    prime_power_base,
    reconstruct_complementary_divisor,
    shell_factor_orientations,
)


def test_exact_off_resonant_counterfixture() -> None:
    q, D, S, center, reps = off_resonant_counterfixture()
    assert (q, D, S, center) == (800, 26, 2027, 986_978)
    assert len(reps) == 8 > sqrt(D)

    carrier_sums = [rep.U for rep in reps]
    assert len(set(carrier_sums)) == len(reps)
    assert not has_nontrivial_three_ap(carrier_sums)

    points = counterfixture_point_set()
    assert len(points) == 16
    assert not has_nontrivial_three_ap({a for a, _ in points})
    assert not has_collinear_triple(points)


def test_fixture_has_no_hidden_gcd_or_error_label_packet() -> None:
    _, _, _, center, reps = off_resonant_counterfixture()
    labels = []
    for rep in reps:
        e, f = rep.errors(center)
        labels.append((e - f, e + f))
        assert gcd(rep.a, rep.b) == 1
    assert len(set(labels)) == len(labels)
    assert all(x != 0 for x, _ in labels)


def test_complementary_divisor_normal_form_and_identities() -> None:
    _, _, _, center, reps = off_resonant_counterfixture()
    for rep in reps:
        data = complementary_divisor_data(rep, center)
        assert data.g == 1
        assert data.A + data.B == data.T
        assert data.n_reduced % data.A == 0
        assert data.m_reduced % data.B == 0
        assert (data.e - data.f) % data.g == 0
        assert reconstruct_complementary_divisor(data, center) == rep
        residual, left, right = exact_fixed_sum_identities(rep, center)
        assert residual == 0
        assert left == right


def test_swaps_give_only_two_points_per_scattered_level() -> None:
    _, _, _, _, reps = off_resonant_counterfixture()
    ordered = list(reps) + [
        type(rep)(rep.b, rep.a, rep.w, rep.v) for rep in reps
    ]
    multiplicity = Counter(rep.U for rep in ordered)
    assert set(multiplicity.values()) == {2}


def test_narrow_prime_power_shell_is_coprime_and_product_sidon() -> None:
    shell = (97, 101, 103, 107, 113, 121, 125, 128)
    assert narrow_prime_power_bases(shell) == (
        97,
        101,
        103,
        107,
        113,
        11,
        5,
        2,
    )
    assert prime_power_base(343) == 7
    assert prime_power_base(45) is None
    assert shell_factor_orientations(97 * 107, shell) == (
        (97, 107),
        (107, 97),
    )
    assert shell_factor_orientations(121 * 121, shell) == ((121, 121),)


def test_actual_center_all_prime_nonzero_defect_fixtures() -> None:
    small, two_level = exact_center_prime_fixtures()
    q, width, color, reps = small
    assert (q, width, color) == (211, 13, 113)
    assert reps[0].S == 198
    data = actual_prime_power_defect_data(reps[0], q, color)
    assert data.X == -24
    assert data.product_gcd == data.defect_gcd == 1
    assert data.residual_gcd == 8 * color

    q, width, color, reps = two_level
    assert (q, width, color) == (4_951, 62, 2_557)
    assert {rep.S for rep in reps} == {5_016}
    assert {rep.U for rep in reps} == {4_740, 4_732}
    assert {rep.products()[0] - rep.products()[1] for rep in reps} == {
        -12,
        -92,
    }
