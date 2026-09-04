"""Regression tests for the actual-prime transition laboratory."""

from __future__ import annotations

import cmath
import math

from actual_prime_transition_lab import (
    LabConfig,
    _additive_spectrum,
    build_shell,
    run_lab,
    segmented_primes,
    verify_result,
    window_integral,
)


def test_segmented_sieve_known_interval() -> None:
    assert segmented_primes(90, 131, 128) == [
        97,
        101,
        103,
        107,
        109,
        113,
        127,
    ]


def test_tent_window_and_voronoi_partition_are_exact_finite_definitions() -> None:
    config = LabConfig(start=1000, ratio=1.3, q_min=5, q_max=19)
    shell = build_shell(config)
    length = math.log(config.end / config.start)
    expected = length / 2.0
    assert math.isclose(window_integral("tent", 0.0, length, length), expected)
    assert math.isclose(
        sum(node.voronoi_weight for node in shell.nodes),
        expected,
        rel_tol=0.0,
        abs_tol=2e-15,
    )


def test_symmetrized_histogram_matches_direct_edge_sum() -> None:
    config = LabConfig(start=1000, ratio=1.3, q_min=11, q_max=11)
    shell = build_shell(config)
    q = 11
    histogram = [0.0] * q
    for edge in shell.edges:
        histogram[edge.left_prime % q] += edge.left_weight
        histogram[edge.right_prime % q] += edge.right_weight
    spectrum = _additive_spectrum(histogram, q)
    for mode in range(q):
        direct = sum(
            edge.left_weight
            * cmath.exp(2j * math.pi * mode * edge.left_prime / q)
            + edge.right_weight
            * cmath.exp(2j * math.pi * mode * edge.right_prime / q)
            for edge in shell.edges
        )
        # The direct expression reduces large prime phases before summation in
        # a different order, so its double-precision roundoff is slightly
        # larger than the residue-histogram expression.
        assert abs(spectrum[mode] - direct) < 1e-13


def test_pole_sector_is_exactly_gap_divisibility_and_parity_forces_2q() -> None:
    config = LabConfig(
        start=1000,
        ratio=1.3,
        q_min=5,
        q_max=5,
        near_radius=2,
        top_modes=2,
    )
    shell = build_shell(config)
    expected_edges = [edge for edge in shell.edges if edge.gap % 5 == 0]
    assert all(edge.gap % 10 == 0 for edge in expected_edges)
    result = run_lab(config)
    report = result["moduli"][0]
    assert report["transition"]["pole_edge_count"] == len(expected_edges)
    assert math.isclose(
        report["transition"]["pole_mass"],
        sum(edge.mass for edge in expected_edges),
        rel_tol=0.0,
        abs_tol=2e-15,
    )


def test_full_scan_is_deterministic_and_closes_all_finite_identities() -> None:
    config = LabConfig(
        start=1000,
        ratio=1.3,
        q_min=5,
        q_max=19,
        near_radius=2,
        top_modes=3,
        heights=(5000.0,),
        max_height_blocks=12,
        height_detail_blocks=3,
    )
    first = run_lab(config)
    second = run_lab(config)
    assert first["payload_sha256"] == second["payload_sha256"]
    assert first == second
    verify_result(first, recompute=True)
    assert [row["q"] for row in first["moduli"]] == [5, 7, 11, 13, 17, 19]
    assert first["common_height"][0]["nonempty_block_count"] > 0


def test_modes_are_all_scanned_and_near_sector_includes_the_pole_bin() -> None:
    result = run_lab(
        LabConfig(
            start=2000,
            ratio=1.2,
            q_min=7,
            q_max=13,
            near_radius=1,
            top_modes=2,
        )
    )
    for report in result["moduli"]:
        assert report["modes_scanned"] == report["q"] - 1
        for mode in report["top_modes"]:
            pole_bin = mode["phase_increment_sectors"][0]
            assert pole_bin["phase_increment_distance"] == 0
            assert math.isclose(
                pole_bin["mass"],
                report["transition"]["pole_mass"],
                rel_tol=0.0,
                abs_tol=2e-15,
            )


def test_q_rough_presieve_partitions_mass_and_reports_both_baselines() -> None:
    result = run_lab(
        LabConfig(
            start=1000,
            ratio=1.3,
            q_min=5,
            q_max=11,
            top_modes=1,
        )
    )
    for modulus in result["moduli"]:
        q = modulus["q"]
        rough = modulus["q_rough_presieve"]
        assert rough["definition"] == "integers n with no prime factor below q"
        assert rough["checks"]["voronoi_partition_relative_error"] < 2e-15
        assert math.isclose(rough["baselines"]["q_inverse"], 1 / q)
        assert math.isclose(rough["baselines"]["q_inverse_sqrt"], 1 / math.sqrt(q))
        assert rough["rough_gaps"]["second_moment_over_mean_squared"] >= 1.0


def test_q_rough_presieve_can_be_disabled_for_large_external_scans() -> None:
    result = run_lab(
        LabConfig(
            start=1000,
            ratio=1.2,
            q_min=7,
            q_max=7,
            top_modes=1,
            rough_presieve=False,
        )
    )
    assert result["moduli"][0]["q_rough_presieve"] is None


def test_distinguished_gap_four_mode_is_exactly_residue_one() -> None:
    result = run_lab(
        LabConfig(
            start=1000,
            ratio=1.3,
            q_min=11,
            q_max=11,
            near_radius=2,
            top_modes=1,
        )
    )
    row = result["moduli"][0]["distinguished_modes"][0]
    assert row["name"] == "gap_four_residue_one"
    assert 4 * row["mode"] == 12
    # Every literal gap-four edge is contained in the distance-one sector.
    distance_one = row["phase_increment_sectors"][1]
    assert distance_one["edge_count"] >= row["gap_four_edge_count"]
    assert distance_one["mass"] + 2e-15 >= row["gap_four_mass"]


def test_half_mode_captures_fixed_small_gaps_once_q_exceeds_all_gaps() -> None:
    result = run_lab(
        LabConfig(
            start=1000,
            ratio=1.3,
            q_min=29,
            q_max=29,
            near_radius=3,
            top_modes=1,
        )
    )
    assert result["shell"]["maximum_gap"] < 29
    capture = result["moduli"][0]["near_residue"]["fixed_small_gap_capture"]
    assert capture is not None
    assert capture["mode"] == 14
    assert capture["small_gap_cutoff"] == 6
    assert capture["relative_identity_error"] < 2e-15
    wheel = {
        row["wheel_step"]: row
        for row in result["moduli"][0]["near_residue"]["wheel_captures"]
    }
    assert wheel[6]["mode"] * 6 % 29 == 1
    assert wheel[6]["relative_identity_error"] < 2e-15
