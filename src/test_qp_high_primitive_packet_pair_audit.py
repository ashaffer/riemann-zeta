from fractions import Fraction
from math import ceil, gcd

import pytest

from qp_coupled_cusp_fejer_inverse import reduced_symmetric_cusp_data

from qp_high_primitive_packet_pair_audit import (
    additive_representations,
    central_content_remote_closure_exponents,
    central_content_transverse_identity,
    coarse_slope_resolution_exponents,
    dyadic_remote_farey_majorant,
    energy_core_height_exponents,
    exact_tangent_singleton_criterion,
    flat_cyclic_residue_masses,
    local_farey_direction_majorant,
    masked_factorable_completion_form,
    parallel_line_band_bound,
    primitive_symmetric_tangent_steps,
    reflected_c_family_fixed_q_majorant,
    reflected_c_branch_exponents,
    reflected_c_factorization_solutions,
    reflected_cusp_normal_form,
    reflected_h_zero_fixed_q_majorant,
    reflected_k_zero_divisor_identity,
    reflected_k_zero_fixed_q_majorant,
    remote_balanced_offset_reflection_family,
    remote_points_in_symmetric_window,
    remote_reflection_c_family,
    remote_reflection_family,
    remote_reflection_hct_family,
    remote_tangent_parameter_mismatch,
    rho_continuous_approximation_error,
    scaled_cusp_normal_form,
    scaled_cusp_remote_exponents,
    scaled_balanced_axis_factor_data,
    scaled_nonzero_residual_exponents,
    residue_character_parseval,
    symmetric_shifted_fejer_layers,
    symmetric_shifted_layer_envelope,
    thickened_crt_cell_exponents,
    thickened_crt_exponent_ledger,
    weighted_completion_energy,
)


def test_primitive_tangent_step_has_only_the_parity_exception() -> None:
    for p in range(2, 35):
        for d in range(-p + 1, p):
            if gcd(p, abs(d)) != 1:
                continue
            steps = primitive_symmetric_tangent_steps(p, d)
            chi = 4 if p % 2 and d % 2 else 1
            assert steps.parity_divisor == chi
            assert steps.first_step == (p * p - d * d) ** 2 // chi
            assert steps.decreasing_step == p * p * (p - d) ** 2 // chi
            assert steps.increasing_step == p * p * (p + d) ** 2 // chi

    assert primitive_symmetric_tangent_steps(7, 1).first_step == 576
    assert primitive_symmetric_tangent_steps(8, 1).first_step == 3_969
    assert primitive_symmetric_tangent_steps(10, 1).first_step == 9_801
    with pytest.raises(ValueError):
        primitive_symmetric_tangent_steps(9, 3)


def test_energy_core_improves_the_remote_height_floor() -> None:
    ledger = energy_core_height_exponents()
    assert ledger["max_m"] == Fraction(1, 10)
    assert ledger["max_M"] == Fraction(1, 6)
    assert ledger["max_A"] == Fraction(11, 10)
    assert ledger["max_B"] == Fraction(7, 6)
    assert ledger["primitive_p_floor"] == Fraction(43, 144)
    assert ledger["first_step_floor"] == Fraction(43, 36)
    assert ledger["product_curvature_floor"] == Fraction(43, 18)
    assert ledger["first_step_over_sqrt_A"] == Fraction(29, 45)
    assert ledger["curvature_over_A"] == Fraction(58, 45)
    assert ledger["farey_cardinality_closure_max_p"] == Fraction(11, 40)
    assert ledger["farey_to_remote_height_gap"] == Fraction(17, 720)
    assert ledger["balanced_height_zero_count"] == Fraction(23, 96)
    assert ledger["pointwise_p_floor"] == Fraction(13, 48)
    assert ledger["pointwise_first_step_over_sqrt_A"] == Fraction(1, 2)


def test_high_exact_tangent_is_singleton_but_parallel_line_only_constant() -> None:
    # These are the three modest primitive heights in the Q=1009 fixture.
    for p in (7, 8, 10):
        assert exact_tangent_singleton_criterion(p, 1, 29, 29)
        assert parallel_line_band_bound(29, p, 1) <= 3
        assert parallel_line_band_bound(29, p, 1, left_band=False) <= 3


def test_infinite_remote_reflection_family_has_exact_output_collision() -> None:
    for p, d in ((7, 1), (101, 2), (1_009, 3)):
        fixture = remote_reflection_family(p, d)
        positive, negative = fixture.positive, fixture.negative
        assert positive.n * positive.L * positive.kappa != 0
        assert negative.n * negative.L * negative.kappa != 0
        assert remote_tangent_parameter_mismatch(positive) == Fraction(
            -d, 2 * fixture.Q * p
        )
        assert remote_tangent_parameter_mismatch(negative) == Fraction(
            d, 2 * fixture.Q * p
        )
        first, second = fixture.first_coordinates
        assert first + second == 2 * fixture.Q
        representations = additive_representations((first, second))
        assert representations[2 * fixture.Q] == 2
        # For fixed d and large p, the required O(p) error band lies inside
        # the application width Q^(16/33).  This exact power comparison
        # avoids floating-point roots.
        assert fixture.required_band**33 < fixture.Q**16


def test_q1009_remote_fixture_has_sixfold_reflection_collision() -> None:
    points = remote_points_in_symmetric_window(1_009, 29, 200)
    assert [point.y for point in points] == [-144, -126, -100, 100, 126, 144]
    assert [point.p for point in points] == [7, 8, 10, 10, 8, 7]
    assert [point.d for point in points] == [-1, -1, -1, 1, 1, 1]
    assert all(point.n * point.L * point.kappa != 0 for point in points)

    displacements = [point.y for point in points]
    representations = additive_representations(displacements)
    assert representations[0] == 6
    assert max(representations.values()) == 6
    assert sum(value * value for value in representations.values()) == 90

    for point in points:
        error = rho_continuous_approximation_error(point)
        elementary_bound = Fraction(
            2 * 29 * (point.Q + abs(point.y)),
            point.Q * point.Q - point.y * point.y,
        )
        assert abs(error) <= elementary_bound


def test_farey_sector_bounds_replay_the_exact_loss() -> None:
    assert local_farey_direction_majorant(1_009, 29, 7, 2, 200) == (
        1
        + ceil(Fraction(4 * 7 * 7 * 200, 1_009))
        + ceil(Fraction(16 * 29 * 7, 1_009 * 2))
    )


def test_thickened_crt_ledger_and_pointwise_character_obstruction() -> None:
    ledger = thickened_crt_exponent_ledger()
    assert ledger["sqrt_HB_over_Q"] == Fraction(-91, 96)
    assert ledger["conditional_thickened_total"] == Fraction(7, 96)
    assert ledger["failure_beyond_exact_support_gap"] == Fraction(35, 96)
    assert ledger["exact_weighted_hard_total"] == Fraction(73, 240)
    assert ledger["farey_failure_physical_lower_bound"] == Fraction(173, 96)

    masses = flat_cyclic_residue_masses(35, 6, 25)
    assert len(masses) == 35
    assert set(masses) == {Fraction(1, 35)}
    width = 9
    # The positive pointwise layer sum grows linearly in W.  Its ratio to
    # the hoped-for square-root expression is sqrt(W)=3 here.
    assert sum(masses[:width]) == Fraction(width, 35)
    assert sum(masses[:width]) == 3 * Fraction(3, 35)
    assert dyadic_remote_farey_majorant(29, 7, 2) == (
        4 * 7 * 7 + ceil(Fraction(16 * 29 * 7, 2))
    )


def test_shifted_layers_have_exact_auxiliary_character_parseval() -> None:
    layers = symmetric_shifted_fejer_layers(
        7, 3, 1, Fraction(1, 13), Fraction(2, 17)
    )
    envelope = symmetric_shifted_layer_envelope(7, 3, 1)
    assert len(layers) == primitive_symmetric_tangent_steps(3, 1).first_step
    assert max(abs(value) for value in layers) <= float(envelope) + 1.0e-12
    character_l2, layer_l2 = residue_character_parseval(layers, (0, 1, 4, 7, 9))
    assert abs(character_l2 - layer_l2) < 1.0e-12
    assert layer_l2 <= 5 * float(envelope) ** 2 + 1.0e-12


def test_cell_polytope_replays_low_and_high_crt_boundaries() -> None:
    low = thickened_crt_cell_exponents(
        Fraction(), Fraction(1, 7), Fraction(), Fraction(1, 2),
        square_root_layers=True,
    )
    assert low["low_crt"] is True
    assert low["final"] == Fraction(1, 14) - Fraction(1, 96)
    assert low["closed"] is True

    boundary = Fraction(253, 384)
    high = thickened_crt_cell_exponents(
        Fraction(), Fraction(), Fraction(), boundary,
        square_root_layers=True,
    )
    assert high["low_crt"] is False
    assert high["final"] == Fraction(1, 2)
    assert high["closed"] is True
    beyond = thickened_crt_cell_exponents(
        Fraction(), Fraction(), Fraction(), boundary + Fraction(1, 1000),
        square_root_layers=True,
    )
    assert beyond["closed"] is False

    pointwise = thickened_crt_cell_exponents(
        Fraction(), Fraction(1, 10), Fraction(1, 5), Fraction(3, 5),
        square_root_layers=False,
    )
    assert pointwise["final"] == (
        Fraction(11, 2) * Fraction(3, 5)
        - Fraction(1, 2) * Fraction(1, 5)
        + Fraction(1, 10)
        - Fraction(205, 96)
    )

    failure = thickened_crt_cell_exponents(
        Fraction(), Fraction(1, 10), Fraction(), Fraction(1),
        square_root_layers=True,
    )
    assert failure["region"] == "farey_failure"
    assert failure["direction"] == Fraction(49, 32)  # sqrt(QGP), not P^2
    assert failure["final"] == -Fraction(7, 96) + 2 + Fraction(1, 20)
    assert failure["final"] > Fraction(173, 96)


def test_integer_c_reflection_family_and_divisor_enumeration() -> None:
    for c in (-3, -1, 0, 2, 5):
        fixture = remote_reflection_c_family(7, 1, c)
        assert fixture.c == c
        assert fixture.positive.n == -c
        assert fixture.negative.n == c
        assert fixture.positive.T == fixture.negative.T == -2 * c
        assert fixture.positive.L == fixture.negative.L == -8 * c
        assert fixture.positive.e == c * 6
        assert fixture.positive.f == c * 8
        assert fixture.first_coordinates[0] + fixture.first_coordinates[1] == 2 * fixture.Q

    fixture = remote_reflection_c_family(7, 1, 2)
    solutions = reflected_c_factorization_solutions(fixture.Q, 5)
    assert (2, 7, 1) in solutions
    for c, p, d in solutions:
        assert fixture.Q - c == p * (p - d) * (p + d)

    branch = reflected_c_branch_exponents(Fraction(), Fraction(), Fraction(11, 16))
    assert branch["paired_c_count"] == Fraction(5, 16)
    assert branch["sqrt_A_target"] == Fraction(1, 2)
    assert branch["paired_margin"] == Fraction(3, 16)
    assert branch["paired_closure_ceiling_pi"] == Fraction(3, 4)

    wider = (
        remote_reflection_hct_family(10, 1, h=1, c=19, t=1),
        remote_reflection_hct_family(8, 1, h=2, c=1, t=0),
        remote_reflection_hct_family(7, 1, h=3, c=1, t=0),
    )
    assert [(item.Q, item.positive.y) for item in wider] == [
        (1_009, 100),
        (1_009, 126),
        (1_009, 144),
    ]
    assert [(item.positive.e, item.positive.f) for item in wider] == [
        (-19, -1),
        (14, 18),
        (18, 24),
    ]


def test_frequency_resolution_is_coarser_than_a_physical_packet() -> None:
    ledger = coarse_slope_resolution_exponents(Fraction(1, 10))
    assert ledger["packets_per_frequency_chart"] == Fraction(9, 20)
    assert ledger["physical_resolution_denominator"] == Fraction(121, 160)
    assert ledger["frequency_denominator_ceiling"] == Fraction(17, 32)
    assert ledger["denominator_gap"] == Fraction(9, 40)


def test_fixed_q_c_branch_has_the_cubic_gap_majorant() -> None:
    fixture = remote_reflection_c_family(7, 1, 2)
    assert fixture.Q == 338 and fixture.required_band == 16
    # The majorant counts both reflected signs d=+-1.
    assert reflected_c_family_fixed_q_majorant(fixture.Q, fixture.required_band) == 2


def test_balanced_offset_is_a_hostile_non_small_c_reflection_branch() -> None:
    fixture = remote_balanced_offset_reflection_family(101, 3)
    point = fixture.positive
    normal = reflected_cusp_normal_form(point)
    assert fixture.c == 606
    assert (normal["c"], normal["u"], normal["content_defect"]) == (606, 3, 0)
    assert normal["balanced_height"] == 0
    assert normal["left_residual"] == -3
    assert normal["right_residual"] == 3
    assert normal["quadratic_residual"] == -9
    assert point.n * point.L * point.kappa != 0
    assert remote_tangent_parameter_mismatch(point) == Fraction(-3, 2 * fixture.Q)
    assert fixture.first_coordinates[0] + fixture.first_coordinates[1] == 2 * fixture.Q
    # The physical bands cost O(p*t), while the small-c criterion costs
    # |c|*p=2*p^2*t and therefore misses this family by a factor ~p.
    assert fixture.required_band == 309
    assert abs(fixture.c) * point.p > 100 * fixture.required_band
    assert fixture.required_band**33 < fixture.Q**16
    assert reflected_h_zero_fixed_q_majorant(fixture.Q, fixture.required_band) >= 2


def test_next_quadratic_residual_detects_one_band_cancellation() -> None:
    # p=7,d=1,u=1,c=2p+d gives h=d*u and therefore k=0.
    point = reduced_symmetric_cusp_data(351, 49, 6, 8)
    normal = reflected_cusp_normal_form(point)
    assert (normal["c"], normal["u"], normal["balanced_height"]) == (15, 1, 1)
    assert normal["left_residual"] == 0
    assert normal["right_residual"] == 2
    assert normal["quadratic_residual"] == 0
    assert point.e == -1
    assert point.f == 15


def test_k_zero_branches_have_the_fixed_d_divisor_identity() -> None:
    # h=d*u: Q=7*(7^2-1)+(2*7+1)*1=351.
    plus = reflected_k_zero_divisor_identity(351, 7, 1, 1, 1)
    assert plus == {
        "branch": 1,
        "c": 15,
        "mu": 2,
        "x": 15,
        "target": 2805,
        "cofactor": 187,
    }

    # h=-d*u: Q=7*(7^2-1)+(2*7-1)*1=349.
    minus = reflected_k_zero_divisor_identity(349, 7, 1, 1, -1)
    assert minus == {
        "branch": -1,
        "c": 13,
        "mu": 2,
        "x": 13,
        "target": 2795,
        "cofactor": 215,
    }


def test_k_zero_divisor_identity_checks_the_requested_branch() -> None:
    with pytest.raises(ValueError, match="not on the requested"):
        reflected_k_zero_divisor_identity(351, 7, 1, 1, -1)
    assert (351 - 1) % 7 == 0
    # For A=1 the two signs and u=+-1 sample Q-1 and Q+1 twice;
    # both 350 and 352 have twelve positive divisors.
    assert reflected_k_zero_fixed_q_majorant(351, 1) == 144


def test_k_zero_minus_branch_includes_the_asymmetric_second_root() -> None:
    # The wide square can be much larger than the narrow band: here
    # u=-2*r=-12 makes e=0 while f=-u^2=-144.  The fixed-d identity still
    # captures the point, which is why the scalar proof cannot simply assume
    # |u|<=sqrt(A) on both signs.
    point = reduced_symmetric_cusp_data(180, 36, 6, 8)
    normal = reflected_cusp_normal_form(point)
    assert (normal["c"], normal["u"], normal["balanced_height"]) == (-156, -12, 12)
    assert normal["balanced_height"] == -point.d * normal["u"]
    assert (point.e, point.f) == (0, -144)
    identity = reflected_k_zero_divisor_identity(180, 7, 1, -12, -1)
    assert (identity["target"], identity["x"], identity["cofactor"]) == (
        1443,
        13,
        111,
    )


def test_central_content_transverse_identity_is_exact_off_the_major_axes() -> None:
    point = reduced_symmetric_cusp_data(343, 40, 6, 8)
    normal = reflected_cusp_normal_form(point)
    assert normal["content_defect"] == 0
    assert normal["quadratic_residual"] != 0
    identity = central_content_transverse_identity(point)
    assert identity == {
        "u": -8,
        "sigma": 1522,
        "left": Fraction(-320),
        "right": Fraction(-320),
    }


def test_central_content_remote_closure_has_a_one_over_48_margin() -> None:
    ledger = central_content_remote_closure_exponents()
    assert ledger["count"] == Fraction(23, 48)
    assert ledger["saving"] == Fraction(1, 48)
    assert ledger["high_offset_ratio"] == Fraction(-5, 48)


def test_scaled_cusp_normal_form_absorbs_noncentral_content_exactly() -> None:
    # This is the scale lambda=3 balanced branch with shifted offset t=2.
    # Its raw content defect is 4 and contributes 2*ell^2=4608 in the old
    # normal form, yet the physical errors remain only -40 and 44.
    fixture = remote_reflection_hct_family(7, 1, h=3, c=28, t=2)
    point = fixture.positive
    normal = scaled_cusp_normal_form(point)
    assert (point.e, point.f) == (-40, 44)
    assert normal["content_defect"] == 4
    assert normal["scale"] == 3
    assert normal["shifted_c"] == 28
    assert normal["shifted_u"] == 2
    assert (normal["T"], normal["v"], normal["z"]) == (-56, 4, 0)
    assert (normal["left_error"], normal["right_error"]) == (-144, 192)
    assert normal["quadratic_residual"] == -16


def test_scaled_cusp_offset_has_energy_core_margins() -> None:
    ledger = scaled_cusp_remote_exponents()
    assert ledger["offset"] == Fraction(23, 48)
    assert ledger["sqrt_A_margin"] == Fraction(1, 48)
    assert ledger["sqrt_B_margin"] == Fraction(5, 48)


def test_scaled_cusp_one_band_axes_have_the_claimed_signs() -> None:
    # h_lambda=+u_lambda gives z=-d*v and puts -u_lambda^2 in e.
    left = remote_reflection_hct_family(7, 1, h=3, c=15, t=1).positive
    left_normal = scaled_cusp_normal_form(left)
    assert (left.e, left.f) == (-1, 47)
    assert (left_normal["v"], left_normal["z"]) == (2, -2)
    assert left_normal["left_residual"] == 0

    # h_lambda=-u_lambda gives z=+d*v and puts -u_lambda^2 in f.
    right = remote_reflection_hct_family(7, 1, h=3, c=13, t=1).positive
    right_normal = scaled_cusp_normal_form(right)
    assert (right.e, right.f) == (-37, -1)
    assert (right_normal["v"], right_normal["z"]) == (2, 2)
    assert right_normal["right_residual"] == 0

    # The asymmetric second root can make e=0 while the square sits in the
    # wide f-band.  Its eta=0 divisor targets are nevertheless exact.
    bad = remote_reflection_hct_family(7, 1, h=3, c=-468, t=-36).positive
    bad_normal = scaled_cusp_normal_form(bad)
    assert (bad.Q, bad.y, bad.e, bad.f) == (540, 108, 0, -1296)
    assert (bad_normal["v"], bad_normal["z"]) == (-72, -72)
    shift = bad_normal["v"] // (2 * bad.d)
    eta = -shift - bad.g * (bad.p - bad.d)
    assert (shift, eta) == (-36, 0)
    assert 2 * (bad.Q + eta) % (bad.p - bad.d) == 0
    assert 2 * (bad.Q + 3 * eta) % (bad.p - 2 * bad.d) == 0


def test_scaled_cusp_recenter_handles_a_hostile_generic_noncentral_point() -> None:
    # This exact point appeared in the complete Q=5003, B=50 scan.  In the
    # old lambda=1 coordinates its offset is -369409430, while its correctly
    # scaled offset is only 10/343.
    point = reduced_symmetric_cusp_data(5003, 1570, 375, 718)
    assert (point.g, point.p, point.d, point.e, point.f) == (
        1,
        1093,
        343,
        -25,
        -6,
    )
    old = reflected_cusp_normal_form(point)
    assert old["u"] == -369409430
    scaled = scaled_cusp_normal_form(point)
    assert scaled["shifted_u"] == Fraction(10, 343)
    assert (scaled["T"], scaled["v"], scaled["z"]) == (-34894, 20, 8826)
    assert scaled["quadratic_residual"] != 0


def test_scaled_balanced_axis_has_the_two_fixed_q_divisor_forms() -> None:
    positive = remote_reflection_hct_family(7, 1, h=3, c=28, t=2).positive
    data = scaled_balanced_axis_factor_data(positive)
    assert data == {
        "M": 296,
        "a": 6,
        "w": 4,
        "left_target": 2064,
        "right_target": 2080,
    }

    # Exact asymmetric second-root cancellation: e=0 while f=-756.
    bad = remote_reflection_hct_family(7, 1, h=3, c=-252, t=-18).positive
    assert (bad.Q, bad.y, bad.e, bad.f) == (756, 126, 0, -756)
    bad_data = scaled_balanced_axis_factor_data(bad)
    assert bad_data == {
        "M": 216,
        "a": 6,
        "w": -36,
        "left_target": 1584,
        "right_target": 1440,
        "t": 36,
        "eta": 0,
        "bad_target": 1512,
    }


def test_scaled_nonzero_residual_forces_high_primitive_height() -> None:
    ledger = scaled_nonzero_residual_exponents()
    assert ledger["primitive_floor"] == Fraction(77, 160)
    assert ledger["primitive_floor"] > ledger["central_remote_floor"]


def test_factorable_post_peel_mask_is_dominated_by_absolute_energy() -> None:
    left_locations = (10, 12, 17)
    right_locations = (3, 5, 10)
    left_weights = (1 + 2j, -3j, 2 - 1j)
    right_weights = (2j, 1 - 1j, -2 + 3j)

    full_mask: dict[tuple[int, int, int, int], complex] = {}
    selected_mask: dict[tuple[int, int, int, int], complex] = {}
    for i, a in enumerate(left_locations):
        for j, b in enumerate(right_locations):
            for k, c in enumerate(left_locations):
                for ell, d in enumerate(right_locations):
                    if a + b != c + d:
                        continue
                    key = (i, j, k, ell)
                    full_mask[key] = 1
                    if (i + 2 * j + 3 * k + ell) % 3:
                        selected_mask[key] = (3 + 4j) / 5

    full_form = masked_factorable_completion_form(
        left_locations,
        left_weights,
        right_locations,
        right_weights,
        full_mask,
    )
    complex_energy = weighted_completion_energy(
        left_locations,
        left_weights,
        right_locations,
        right_weights,
    )
    assert abs(full_form.real - complex_energy) < 1.0e-10
    assert abs(full_form.imag) < 1.0e-10

    selected_form = masked_factorable_completion_form(
        left_locations,
        left_weights,
        right_locations,
        right_weights,
        selected_mask,
    )
    absolute_energy = weighted_completion_energy(
        left_locations,
        left_weights,
        right_locations,
        right_weights,
        absolute_weights=True,
    )
    assert abs(selected_form) <= absolute_energy + 1.0e-10

    with pytest.raises(ValueError, match="completion equality"):
        masked_factorable_completion_form(
            left_locations,
            left_weights,
            right_locations,
            right_weights,
            {(0, 0, 0, 1): 1},
        )
