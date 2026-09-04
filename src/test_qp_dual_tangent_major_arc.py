from fractions import Fraction
from math import gcd

from qp_coupled_cusp_fejer_inverse import normalized_fejer_coefficients
from qp_dual_tangent_major_arc import (
    caustic_frequency_size_gate,
    caustic_phase_height,
    interior_caustic_discriminant,
    normalized_phase_derivatives,
    normalized_fejer_orbit_eta_bound,
    normalized_fejer_grid_maximum,
    rational_tangent_data,
    remote_symmetric_orbit_exponent_ledger,
    special_center_reduced_lambda,
    stationary_affine_heights,
    stationary_coefficient_mass,
    stationary_quartic_value,
    cyclic_tangent_mask_average,
    exact_remote_stationary_sector_exponent_ledger,
    symmetric_error_cusp_identity,
    symmetric_cyclic_fejer_bound,
    symmetric_cyclic_fejer_maximum,
    symmetric_primal_cusp_coordinates,
    symmetric_stationary_alias,
    symmetric_tangent_alias_data,
    tangent_line_meets_integer_lattice,
    tangent_line_intercepts,
    tangent_line_point_and_product_errors,
    tangent_orbit_has_integer_point,
    tangent_orbit_linf_distance,
)


def test_symmetric_tangent_has_full_normal_lattice_and_primitive_caustic() -> None:
    # Here lambda=C/S^2=1/4 and t=1/2.  The primitive tangent direction is
    # the swapped packet (1,-1,1), while (h,k,m)=(1,-1,-2) is the cubic.
    data = rational_tangent_data(1, 4, 1, 1)
    assert data.primitive_direction == (1, -1, 1)
    assert data.stationary_basis[0] == (0, 1, 1)
    assert data.primitive_caustic == (2, 1, -1)

    for frequency in (*data.stationary_basis, data.primitive_caustic):
        assert sum(
            x * y for x, y in zip(frequency, data.primitive_direction)
        ) == 0


def test_caustic_is_exactly_double_but_never_triple_stationary() -> None:
    P, Q, r, s = 2, 5, 2, 3
    data = rational_tangent_data(P, Q, r, s)
    minus_m, h, k = data.primitive_caustic
    m = -minus_m
    t = Fraction(r, r + s)
    derivatives = normalized_phase_derivatives(Fraction(P, Q), h, k, m, t)
    assert derivatives["first"] == 0
    assert derivatives["second"] == 0
    assert derivatives["third"] != 0
    assert stationary_quartic_value(Fraction(P, Q), h, k, m, t) == 0
    assert interior_caustic_discriminant(Fraction(P, Q), h, k, m) == 0


def test_stationary_quartic_discriminant_detects_regular_and_cubic_modes() -> None:
    lam = Fraction(1, 4)
    # At t=1/2, m=k-h.  This mode is regular because h+k is nonzero.
    regular = normalized_phase_derivatives(lam, 1, 2, 1, Fraction(1, 2))
    assert regular["first"] == 0
    assert regular["second"] != 0
    assert interior_caustic_discriminant(lam, 1, 2, 1) != 0

    cubic = normalized_phase_derivatives(lam, 7, -7, -14, Fraction(1, 2))
    assert cubic["first"] == cubic["second"] == 0
    assert cubic["third"] != 0
    assert interior_caustic_discriminant(lam, 7, -7, -14) == 0


def test_affine_height_separates_lattice_packets_from_bare_cubic_saddles() -> None:
    # An odd symmetric packet has no integer common-product centre, but the
    # rational tangent line itself contains the swapped integer packet.
    assert tangent_line_meets_integer_lattice(1, 4, 11, 1, 1)
    point, errors = tangent_line_point_and_product_errors(
        1, 4, 11, 1, 1, Fraction(6)
    )
    assert point == (Fraction(6), Fraction(5), Fraction(6))
    assert errors == (Fraction(-1, 4), Fraction(-1, 4))

    # lambda=1/2, S=5, t=1/3 has an integral-phase primitive cubic, but its
    # full stationary character is nontrivial, so the tangent line misses Z^3.
    assert stationary_affine_heights(1, 2, 5, 1, 2) == (
        Fraction(45, 2),
        Fraction(15),
    )
    assert caustic_phase_height(1, 2, 5, 1, 2) == 0
    assert not tangent_line_meets_integer_lattice(1, 2, 5, 1, 2)


def test_tangent_product_errors_are_exactly_quadratic() -> None:
    point, errors = tangent_line_point_and_product_errors(
        3, 7, 35, 2, 3, Fraction(17, 1)
    )
    a, v, w = point
    center = Fraction(14)
    complement = Fraction(21)
    C = Fraction(3 * 35**2, 7)
    assert a == 17
    assert errors == (
        -C * (a - center) ** 2 / center**2,
        -C * (a - center) ** 2 / complement**2,
    )
    assert a * v - C == errors[0]
    assert (35 - a) * w - C == errors[1]


def test_special_center_denominator_and_caustic_frequency_gate_are_exact() -> None:
    lam = special_center_reduced_lambda(30, 25, 21)
    assert lam == Fraction(30**3, 8 * 25 * 21**2)
    multiplier, largest = caustic_frequency_size_gate(
        lam.denominator, 2, 3
    )
    assert multiplier == lam.denominator // __import__("math").gcd(
        lam.denominator, 5**3
    )
    assert largest == multiplier * 3**3
    # Since (r+s)^3 <= 8*max(r,s)^3, largest<=H always forces Q<=8H.
    assert lam.denominator <= 8 * largest


def test_primal_carrier_cusp_is_the_exact_dual_cusp_coordinate_pair() -> None:
    coordinates = symmetric_primal_cusp_coordinates(101, 7)
    assert coordinates["rho"] == 2 * coordinates["A"]
    assert coordinates["kappa"] == 2 * coordinates["t"]
    assert coordinates["rho"] ** 3 == coordinates["kappa"] ** 2 * (
        coordinates["rho"] + 202
    )


def test_affine_height_criterion_matches_exhaustive_small_tangent_lines() -> None:
    for P in range(1, 5):
        for denominator in range(1, 6):
            if gcd(P, denominator) != 1:
                continue
            for S in range(3, 9):
                for r, s in ((1, 1), (1, 2), (2, 1), (2, 3), (3, 2)):
                    data = rational_tangent_data(P, denominator, r, s)
                    period = data.primitive_direction[0]
                    brute = False
                    for a in range(period):
                        point, _ = tangent_line_point_and_product_errors(
                            P, denominator, S, r, s, Fraction(a)
                        )
                        if all(coordinate.denominator == 1 for coordinate in point):
                            brute = True
                            break
                    assert tangent_line_meets_integer_lattice(
                        P, denominator, S, r, s
                    ) == brute


def test_error_deformed_primal_cusp_retains_the_dual_divisibility_coordinate() -> None:
    for y, left_shift, right_shift in ((7, 2, -3), (-11, 5, 4), (0, 1, 1)):
        data = symmetric_error_cusp_identity(
            101, y, left_shift, right_shift
        )
        assert data["left"] == data["right"]
        assert data["tau"] == y * data["rho"] - 101 * data["kappa"]


def test_stationary_normal_lattice_regroups_as_a_cyclic_fejer_orbit() -> None:
    coefficients = normalized_fejer_coefficients(7)
    for parameters in ((1, 4, 11, 1, 1), (1, 2, 5, 1, 2), (3, 7, 13, 2, 3)):
        alpha, beta, direction = tangent_line_intercepts(*parameters)
        direct = stationary_coefficient_mass(
            coefficients, direction, alpha, beta
        )
        cyclic = cyclic_tangent_mask_average(
            coefficients, direction, alpha, beta
        )
        assert abs(direct - cyclic) < 1.0e-11


def test_cyclic_orbit_packet_criterion_matches_full_affine_height() -> None:
    for parameters in ((1, 4, 11, 1, 1), (1, 2, 5, 1, 2), (3, 7, 13, 2, 3)):
        alpha, beta, direction = tangent_line_intercepts(*parameters)
        assert tangent_orbit_has_integer_point(direction, alpha, beta) == (
            tangent_line_meets_integer_lattice(*parameters)
        )


def test_cyclic_fejer_average_obeys_the_exact_eta_envelope() -> None:
    order = 31
    coefficients = normalized_fejer_coefficients(order)
    for parameters in ((1, 4, 11, 1, 1), (1, 2, 5, 1, 2), (3, 7, 13, 2, 3)):
        alpha, beta, direction = tangent_line_intercepts(*parameters)
        eta = tangent_orbit_linf_distance(direction, alpha, beta)
        average = cyclic_tangent_mask_average(
            coefficients, direction, alpha, beta
        )
        envelope = normalized_fejer_orbit_eta_bound(order, eta)
        assert abs(average.imag) < 1.0e-12
        assert average.real <= float(envelope) + 1.0e-12
        assert (eta == 0) == tangent_line_meets_integer_lattice(*parameters)


def test_symmetric_tangent_direction_has_only_the_parity_index_exception() -> None:
    # r,s both odd: n is even, g=4, and R=r^2*s^2.
    even_sum = symmetric_tangent_alias_data(3, 1)
    assert even_sum.direction == (9, -4, 36)
    assert even_sum.parity_index == 1
    # Opposite parity: n is odd, g=1, R=4*r^2*s^2.
    odd_sum = symmetric_tangent_alias_data(2, 1)
    assert odd_sum.direction == (16, -9, 36)
    assert odd_sum.parity_index == 4


def test_symmetric_alias_rule_matches_the_raw_stationary_congruence() -> None:
    for r, s in ((3, 1), (2, 1), (3, 2), (5, 3)):
        direction = symmetric_tangent_alias_data(r, s).direction
        R, minus_left_step, right_step = direction
        for h in range(-30, 31):
            for k in range(-30, 31):
                raw = (k * right_step + h * minus_left_step) % R == 0
                recognized, _, _, m = symmetric_stationary_alias(h, k, r, s)
                assert recognized == raw
                if recognized:
                    assert m * R == k * right_step + h * minus_left_step


def test_fejer_grid_maximum_has_exact_residue_class_formula() -> None:
    assert normalized_fejer_grid_maximum(7, 10) == Fraction(1, 7)
    assert normalized_fejer_grid_maximum(10, 3) == Fraction(34, 100)
    for order in range(2, 30):
        for modulus in range(1, 20):
            maximum = normalized_fejer_grid_maximum(order, modulus)
            if modulus >= order:
                assert maximum == Fraction(1, order)
            else:
                assert maximum <= Fraction(1, modulus) + Fraction(
                    modulus, 4 * order * order
                )


def test_symmetric_cyclic_orbit_obeys_product_grid_bound_in_both_parities() -> None:
    order = 23
    coefficients = normalized_fejer_coefficients(order)
    for r, s, S in ((3, 1, 17), (2, 1, 17), (3, 2, 19), (5, 3, 23)):
        alpha, beta, direction = tangent_line_intercepts(1, 4, S, r, s)
        average = cyclic_tangent_mask_average(
            coefficients, direction, alpha, beta
        )
        bound = symmetric_cyclic_fejer_bound(order, r, s)
        assert abs(average.imag) < 1.0e-12
        assert average.real <= float(bound) + 1.0e-11


def test_remote_primitive_floor_gives_more_than_one_full_H_gain() -> None:
    ledger = remote_symmetric_orbit_exponent_ledger()
    assert ledger["primitive_p_floor"] == Fraction(13, 48)
    assert ledger["p_fourth_power_floor"] == Fraction(13, 12)
    assert ledger["H"] == Fraction(17, 16)
    assert ledger["excess_over_H"] == Fraction(1, 48)
    assert ledger["cyclic_mass_ceiling"] == Fraction(-13, 12)


def test_symmetric_orbit_maximum_is_exact_including_index_four_aliases() -> None:
    order = 29
    coefficients = normalized_fejer_coefficients(order)
    for r, s in ((3, 1), (2, 1), (3, 2), (5, 3)):
        direction = symmetric_tangent_alias_data(r, s).direction
        actual = cyclic_tangent_mask_average(
            coefficients, direction, Fraction(), Fraction()
        )
        exact = symmetric_cyclic_fejer_maximum(order, r, s)
        ceiling = symmetric_cyclic_fejer_bound(order, r, s)
        assert abs(actual.imag) < 1.0e-12
        assert abs(actual.real - float(exact)) < 1.0e-12
        assert exact <= ceiling


def test_all_exact_remote_directions_fit_below_the_square_root_target() -> None:
    ledger = exact_remote_stationary_sector_exponent_ledger()
    assert ledger["Airy_before_direction_sum"] == Fraction(49, 48)
    assert ledger["direction_sum_saving"] == Fraction(13, 24)
    assert ledger["exact_remote_sector"] == Fraction(23, 48)
    assert ledger["target"] == Fraction(1, 2)
    assert ledger["slack_below_target"] == Fraction(1, 48)
