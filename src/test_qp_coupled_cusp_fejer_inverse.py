from fractions import Fraction

import pytest

from qp_coupled_cusp_fejer_inverse import (
    centered_rational_phase_parts,
    classify_exact_cusp_cubic,
    compact_cusp_exponent_ledger,
    coupled_inverse_exponent_ledger,
    cusp_cubic_from_parameters,
    divisor_mask_contribution_power,
    fejer_coefficient_ledgers,
    hostile_symmetric_cusp_scan,
    hostile_remote_direction_cluster_scan,
    normalized_fejer_coefficients,
    primitive_cusp_lattice_coordinates,
    reciprocal_space_curve_torsion,
    reduced_symmetric_cusp_data,
    shifted_reciprocal_determinant_invariance,
    symmetric_shift_packet_majorant,
    symmetric_cusp_error_cubic,
    shifted_three_reciprocal_content_centres,
    translated_tangent_minor_fixture,
    verify_cusp_regrouping,
)


def test_actual_fejer_coefficients_have_the_required_norms() -> None:
    coefficients = normalized_fejer_coefficients(9, Fraction(3, 2))
    ledger = fejer_coefficient_ledgers(coefficients)
    assert ledger["mean"] == Fraction(1, 6)
    assert ledger["l1"] == ledger["peak"] == Fraction(3, 2)
    assert ledger["l2_squared"] < Fraction(1, 2)


def test_rational_center_normal_form_is_exact() -> None:
    for values in ((10_403, 101, 7, -5, 3, 11), (9_409, 97, -4, 13, -2, -17)):
        parts = centered_rational_phase_parts(*values)
        assert parts["phase"] == parts["constant"] + parts["linear"] + parts["residual"]
    symmetric = centered_rational_phase_parts(101**2, 101, 7, -7, -14, 9)
    assert symmetric["lambda"] == 1
    assert symmetric["p"] == 0
    assert symmetric["linear"] == 0


def test_actual_coefficient_cusp_regrouping() -> None:
    coefficients = {
        key: complex(value)
        for key, value in normalized_fejer_coefficients(7).items()
    }
    left, right = verify_cusp_regrouping(coefficients, A=0.137, t=-0.041)
    assert abs(left - right) < 1.0e-12


def test_integral_error_labels_obey_exact_cusp_cubic() -> None:
    for Q in (17, 101):
        for y in (-7, -1, 0, 3, 11):
            if abs(y) >= Q:
                continue
            for r, s in ((0, 0), (2, 3), (-4, 7), (13, -5)):
                ledger = symmetric_cusp_error_cubic(Q, y, r, s)
                assert Q * ledger["cubic"] == ledger["cubic_rhs"]
                assert y * ledger["rho"] == Q * ledger["kappa"] + ledger["tau"]


def test_singular_cusp_label_is_exactly_the_tangent_packet() -> None:
    for y in range(-12, 13):
        ledger = symmetric_cusp_error_cubic(101, y, 0, 0)
        assert ledger["rho"] == ledger["kappa"] == 0
        assert ledger["e"] == ledger["f"] == -(y * y)
        assert ledger["sigma"] == -2 * y * y
        assert ledger["tau"] == 0


def test_exact_nontangent_cubic_points_have_divisor_parameters() -> None:
    # h*p*(p^2-d^2)=2Q: 2*3*(9-1)=48=2*24.
    for d in (-1, 1):
        rho, kappa = cusp_cubic_from_parameters(Q=24, p=3, d=d, h=2)
        classified = classify_exact_cusp_cubic(24, rho, kappa)
        assert classified["p"] == 3
        assert classified["d"] == d
        assert classified["h"] == 2
        assert classified["physical_y"] == 8 * d
        assert classified["physical"] is True
    assert classify_exact_cusp_cubic(24, 0, 0)["singular"] is True


def test_primitive_cusp_coordinates_retain_both_divisibilities() -> None:
    for Q, y, r, s in ((101, 17, 2, 5), (97, -11, 7, 3), (211, 31, 9, 14)):
        primitive = primitive_cusp_lattice_coordinates(Q, y, r, s)
        assert primitive["tau"] == primitive["g"] * primitive["n"]
        assert primitive["p"] * y - Q * primitive["d"] == primitive["n"]
        assert primitive["cubic"] == primitive["g"] ** 2 * primitive["delta"]
        assert Q * primitive["delta"] == primitive["divided_rhs"]


def test_small_height_family_survives_exact_cubic_and_common_product_deletion() -> None:
    # Q=Y(Y-1), y=Y, r=s=1 gives e=0 and f=-2Y, but both primitive
    # nonmajor labels n and Delta are nonzero.  It is the exact obstruction
    # to calling the remainder a pure AB/Q volume term.
    for Y in (3, 11, 101, 1009):
        Q = Y * (Y - 1)
        primitive = primitive_cusp_lattice_coordinates(Q, Y, 1, 1)
        assert primitive["e"] == 0
        assert primitive["f"] == -2 * Y
        assert primitive["rho"] == 2
        assert primitive["kappa"] == 0
        assert primitive["n"] == Y
        assert primitive["delta"] == 2
        assert primitive["cubic"] == 8


def test_common_vertical_shift_drops_out_of_the_local_determinant() -> None:
    first, second = shifted_reciprocal_determinant_invariance(
        (101, 107, 119), C=10_403, shift=Fraction(7, 19)
    )
    assert first == second


def test_tail_core_split_hits_the_square_root_exponent_exactly() -> None:
    ledger = coupled_inverse_exponent_ledger()
    assert ledger["tail_mask"] == Fraction(1, 4)
    assert ledger["balanced_core"] == Fraction(1, 6)
    assert ledger["divisor_tail"] == Fraction(1, 2)
    assert ledger["local_determinant_error"] == Fraction(-1, 8)
    assert ledger["gram_operator_target"] == Fraction(21, 8)
    assert ledger["fejer_rank_one_norm_squared"] == Fraction(-17, 8)
    assert ledger["quadratic_form_target"] == Fraction(1, 2)
    assert ledger["generic_space_curve_error"] == Fraction(99, 80)
    assert ledger["largest_core_target"] == Fraction(7, 6)
    assert ledger["generic_space_curve_gap"] == Fraction(17, 240)


def test_exact_divisor_closed_mask_frontier() -> None:
    # Worst unbalanced outer endpoint: m=1, M=D^(1/4).
    assert divisor_mask_contribution_power(Fraction(0), Fraction(1, 4)) == Fraction(1, 2)
    # Balanced endpoint: m=M=D^(1/6).
    assert divisor_mask_contribution_power(Fraction(1, 6), Fraction(1, 6)) == Fraction(1, 2)
    # A mask strictly inside u+2v<1/2 is genuinely unclosed by this estimate.
    assert divisor_mask_contribution_power(Fraction(1, 10), Fraction(1, 6)) > Fraction(1, 2)


def test_fixed_sum_reciprocal_curve_has_nonzero_torsion() -> None:
    torsion = reciprocal_space_curve_torsion(
        Fraction(3, 5), Fraction(7, 4), Fraction(2, 3)
    )
    assert torsion > 0
    assert torsion == 12 * Fraction(3, 5) ** 2 * Fraction(7, 4) / (
        Fraction(2, 3) ** 4 * (Fraction(7, 4) - Fraction(2, 3)) ** 4
    )


def test_reduced_cusp_content_factorization_is_exact() -> None:
    for Q, y, r, s in (
        (101, 17, 2, 3),
        (1_009, -144, 24, 18),
        (5_003, 291, 16, 18),
    ):
        data = reduced_symmetric_cusp_data(Q, y, r, s)
        assert data.rho == data.g * data.p
        assert data.kappa == data.g * data.d
        assert data.tau == data.g * data.n
        assert data.p * y - Q * data.d == data.n
        assert data.L == data.g * data.g * data.T


def test_pure_minor_volume_term_has_an_exact_translated_tangent_counterexample() -> None:
    with pytest.raises(ValueError, match="y>=4"):
        translated_tangent_minor_fixture(3)
    Y = 10**12
    Q, A, B, data = translated_tangent_minor_fixture(Y)
    assert Q == Y * (Y - 1)
    assert data.n != 0 and data.L != 0
    assert data.r == data.s == 1 and data.d == 0
    assert abs(data.e) <= A and abs(data.f) <= B
    assert A * B < Q

    ledger = compact_cusp_exponent_ledger()
    assert ledger["counterexample_mM2_in_D"] == Fraction(1, 16)
    assert ledger["counterexample_volume_in_D"] == Fraction(-1, 32)
    assert ledger["counterexample_volume_in_Q"] == Fraction(-1, 66)
    assert ledger["energy_max_A_in_D"] == Fraction(11, 10)
    assert ledger["energy_max_B_in_D"] == Fraction(7, 6)
    assert ledger["energy_remote_p_floor_in_D"] == Fraction(43, 144)
    assert ledger["energy_B4over3_over_Q_in_D"] == Fraction(-73, 144)
    assert ledger["energy_A_over_Q2over3_in_D"] == Fraction(-11, 40)
    assert ledger["energy_p2_over_sqrtA_in_D"] == Fraction(11, 120)


def test_secondary_symmetric_shift_packet_fits_square_root_budget() -> None:
    Q, A, B = 100_003, 266, 2_128
    # This is well inside the sufficient compact-core inequality.
    assert B**8 <= A**3 * Q**4
    ceiling = symmetric_shift_packet_majorant(Q, A, B)
    actual = 0
    for y in range(-Q // 2, Q // 2 + 1):
        for t in range(1, 20):
            e = t * (Q + y) - y * y
            f = t * (Q - y) - y * y
            actual += abs(e) <= A and abs(f) <= B
    assert actual <= ceiling


def test_hostile_scan_keeps_only_high_primitive_remote_points() -> None:
    scan = hostile_symmetric_cusp_scan(20_011, 122, 488, y_limit=8_000)
    assert scan.total == (
        scan.common_product
        + scan.exact_cusp
        + scan.translated_tangent
        + scan.remote_minor
    )
    assert scan.remote_minor > 0
    assert scan.minimum_remote_rho is not None
    assert scan.minimum_remote_p is not None
    # This finite threshold is only a consistency check for the asymptotic
    # power-height lemma, not its proof.
    assert scan.minimum_remote_p >= 7


def test_remote_cluster_scan_sees_no_repeated_primitive_direction() -> None:
    scan = hostile_remote_direction_cluster_scan(20_011, 122, 488, y_limit=8_000)
    assert scan.remote_points == 12
    assert scan.distinct_directions == scan.remote_points
    assert scan.maximum_direction_multiplicity == 1
    assert scan.maximum_denominator_multiplicity == 2
    assert scan.farey_moderate_points + scan.farey_hard_points == scan.remote_points
    assert scan.farey_moderate_points == 0
    assert (
        scan.farey_moderate_points
        + scan.farey_target_extension_points
        + scan.farey_unresolved_points
        == scan.remote_points
    )
    assert scan.farey_target_extension_points == 0
    assert scan.farey_unresolved_points == scan.remote_points

    # Denominator-only grouping is genuinely coarser: this energy-core
    # fixture has three different directions with p=55.
    denominator_cluster = hostile_remote_direction_cluster_scan(
        5_000, 63, 100, y_limit=2_000
    )
    assert denominator_cluster.maximum_direction_multiplicity == 1
    assert denominator_cluster.maximum_denominator_multiplicity == 3


def test_hard_content_centre_is_an_exact_shifted_three_reciprocal() -> None:
    values = shifted_three_reciprocal_content_centres(5_000, 55, 9, -10)
    assert values["unshifted"] == values["reciprocal"]
    assert values["shifted"] - values["unshifted"] == values["perturbation"]
    # This is the p=55,d=9 hostile point; the shifted centre is close to
    # its integral content g=5, while the nonzero n-shift is still visible.
    assert abs(values["shifted"] - 5) < Fraction(1, 2_000)
    assert values["perturbation"] != 0
