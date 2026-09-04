import cmath
import math
from collections import Counter
from fractions import Fraction

from qp_canonical_self_orbit_drpls_lab import (
    adjacent_anchor,
    balanced_tower_rectangle_audit,
    canonical_integer_orbit,
    dyadic_moment_from_profile,
    exact_radius_packets,
    frequency_square_profile,
    scan_active_dyadic_range,
    small_small_sector_audit,
)
from qp_balanced_tower_alias_gram import (
    balanced_tower_alias_gram_audit,
    critical_balanced_radius,
    decode_packet_pair,
    transpose_hinge_correlation_audit,
)


def test_adjacent_orbit_has_the_exact_interval_formula() -> None:
    q, D = 20_000, 121
    anchor = adjacent_anchor(q)
    orbit = canonical_integer_orbit(q, D, anchor)
    m = q // 2
    assert len(orbit) == 2 * D + 1
    assert all(orbit[t] == (m + 1 - t, m - t) for t in range(-D, D + 1))


def test_exact_phase_residue_profile_matches_fraction_brute_force() -> None:
    q, D, K = 400, 4, 3
    anchor = adjacent_anchor(q)
    orbit = canonical_integer_orbit(q, D, anchor)
    profile = frequency_square_profile(q, D, anchor, 2 * K, points=orbit)
    Q = Fraction(q**3, 8)
    ordered = tuple(orbit[label] for label in sorted(orbit))
    for h in range(1, 2 * K + 1):
        brute = sum(
            cmath.exp(2j * math.pi * float((h * Q / (left[0] * right[1])) % 1))
            for left in ordered
            for right in ordered
        )
        assert math.isclose(profile.squares[h], abs(brute) ** 2, rel_tol=2e-13)


def test_alias_ledger_and_all_integral_K_scan_are_consistent() -> None:
    q, D = 2_000, 39
    scan = scan_active_dyadic_range(q, D, adjacent_anchor(q))
    audit = dyadic_moment_from_profile(scan.profile, scan.worst.K)
    assert audit == scan.worst
    assert audit.exact_alias_mass >= audit.equal_product_alias_mass
    assert audit.exact_alias_mass >= audit.strict_diagonal_mass
    assert math.isclose(
        audit.normalized_mass,
        audit.normalized_exact_alias + audit.normalized_signed_nonalias,
        rel_tol=2e-15,
        abs_tol=2e-15,
    )


def test_adjacent_orbit_is_entirely_in_the_constant_one_small_small_sector() -> None:
    q, D, K = 20_000, 121, 165
    anchor = adjacent_anchor(q)
    orbit = canonical_integer_orbit(q, D, anchor)
    packets = exact_radius_packets(q, D, K, anchor, orbit)
    assert len(packets) == 1
    assert packets[0].direction == (1, 1)
    assert packets[0].remainder == -1
    assert packets[0].small_small

    audit = small_small_sector_audit(q, D, anchor, K, points=orbit)
    profile = frequency_square_profile(q, D, anchor, 2 * K, points=orbit)
    full = dyadic_moment_from_profile(profile, K)
    assert audit.small_small_point_count == 2 * D + 1
    assert audit.small_small_block_count == 21
    assert math.isclose(audit.restricted_mass, full.mass, rel_tol=3e-14)
    assert audit.packet_square_mass > 0


def test_long_double_reproduces_double_after_exact_range_reduction() -> None:
    q, D = 5_000, 62
    K = q // D
    anchor = adjacent_anchor(q)
    double = frequency_square_profile(q, D, anchor, 2 * K)
    extended = frequency_square_profile(q, D, anchor, 2 * K, method="clongdouble")
    first = dyadic_moment_from_profile(double, K)
    second = dyadic_moment_from_profile(extended, K)
    assert abs(first.normalized_mass - second.normalized_mass) < 1e-11


def test_balanced_tower_contains_exact_lane_by_n_rectangle() -> None:
    audit = balanced_tower_rectangle_audit(F=12, R=2_358)
    assert audit.q == 56_592
    assert audit.D == 144
    assert audit.anchor == (28_307, 28_295)
    assert audit.all_orbit_points_have_tower_coordinates
    assert audit.rectangle_is_contained
    assert len(audit.lane_parameters) == 5
    assert audit.rectangle_point_count == 60


def test_critical_balanced_radius_is_the_exact_ceiling() -> None:
    for F in (2, 6, 12, 44):
        R = critical_balanced_radius(F)
        assert (R - 1) ** 8 < F**25 <= R**8


def test_balanced_tower_exact_alias_quotient_has_consistent_ledger() -> None:
    audit = balanced_tower_alias_gram_audit(F=6)
    assert audit.R == 271
    assert audit.K == audit.R // audit.F == 45
    assert audit.point_count == 18
    assert audit.ordered_packet_pair_count == 9
    global_aliases: Counter[Fraction] = Counter()
    packet_aliases: Counter[tuple[int, Fraction]] = Counter()
    lanes = audit.lane_parameters
    quotient_pairs = tuple(
        (left, right)
        for left in range(len(lanes))
        for right in range(left, len(lanes))
    )
    quotient_lookup = {
        lane_pair: quotient_id
        for quotient_id, lane_pair in enumerate(quotient_pairs)
    }
    quotient_aliases: Counter[tuple[int, Fraction]] = Counter()
    for left_id, left_lane in enumerate(lanes):
        for n in range(audit.F):
            first = left_lane * audit.R - n
            for right_id, right_lane in enumerate(lanes):
                for n_prime in range(audit.F):
                    second = right_lane * (audit.R + 1) - n_prime
                    denominator = 8 * first * second
                    phase = Fraction(audit.q**3 % denominator, denominator)
                    global_aliases[phase] += 1
                    packet_aliases[(left_id * len(lanes) + right_id, phase)] += 1
                    unordered_pair = min(left_id, right_id), max(left_id, right_id)
                    quotient_aliases[(quotient_lookup[unordered_pair], phase)] += 1
    brute_cross_alias_mass = audit.K * (
        sum(count * count for count in global_aliases.values())
        - sum(count * count for count in packet_aliases.values())
    )
    assert audit.exact_cross_packet_alias_mass == brute_cross_alias_mass == 270
    brute_quotient_alias_mass = audit.K * (
        sum(count * count for count in global_aliases.values())
        - sum(count * count for count in quotient_aliases.values())
    )
    quotient = audit.transpose_quotient
    assert quotient.column_count == len(lanes) * (len(lanes) + 1) // 2
    assert quotient.exact_cross_alias_mass == brute_quotient_alias_mass == 0
    assert math.isclose(
        audit.total_mass,
        quotient.packet_diagonal_mass
        + quotient.exact_cross_alias_mass
        + quotient.signed_nonalias_cross_mass,
        rel_tol=2e-15,
    )
    assert audit.maximum_phase_alias_class_size == 2
    assert math.isclose(
        audit.total_mass,
        audit.packet_pair_diagonal_mass
        + audit.exact_cross_packet_alias_mass
        + audit.signed_nonalias_cross_mass,
        rel_tol=2e-15,
    )
    assert decode_packet_pair(7, len(audit.lane_parameters)) == (2, 1)


def test_transpose_hinge_has_no_exact_alias_but_persistent_correlation() -> None:
    audit = transpose_hinge_correlation_audit(24, (21, 24, 28))
    assert audit.K == 856
    assert audit.exact_cross_alias_mass == 0
    assert math.isclose(
        audit.alias_removed_absolute_correlation,
        0.281831270038,
        rel_tol=2e-11,
    )
