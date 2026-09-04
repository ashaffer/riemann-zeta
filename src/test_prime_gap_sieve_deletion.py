#!/usr/bin/env python3
"""Regression tests for the exact sieve-deletion calculus."""

from __future__ import annotations

import cmath
import math

from prime_gap_sieve_deletion import (
    circular_pre_q_wheel_stage,
    decompose,
    log_tent_mode,
    one_hole_q_wheel_coefficient,
    rational_mode,
)


def test_one_hole_wheel_formula_matches_direct_circular_trapezoid() -> None:
    for q, a in [(11, 3), (19, 5), (43, 11)]:
        residues = list(range(1, q))
        direct = 0j
        for index, left in enumerate(residues):
            right = residues[(index + 1) % len(residues)]
            lifted_right = right if index + 1 < len(residues) else right + q
            gap = lifted_right - left
            direct += 0.5 * gap * (
                cmath.exp(2j * math.pi * a * left / q)
                + cmath.exp(2j * math.pi * a * right / q)
            )
        direct /= q
        assert abs(direct - one_hole_q_wheel_coefficient(a, q)) < 2e-14


def test_rational_stage_before_at_after_is_exact_on_multiple_shells() -> None:
    for lo, hi in [(1009, 4999), (10_007, 19_997)]:
        for q in (11, 19, 43):
            a = (q + 1) // 4
            result = decompose(lo, hi, rational_mode(a, q))
            diagnostic = result.rational_stage_diagnostic(q, a, neighbor_stages=2)
            checks = diagnostic["telescoping_checks"]
            assert checks["before_at_after_error"] < 2e-9
            assert checks["tail_from_cumulative_at_error"] < 2e-9
            assert math.isclose(diagnostic["benchmarks"]["q_inverse"], 1 / q)
            assert len(diagnostic["neighbor_stages"]) <= 5


def test_q_stage_is_real_dominant_for_a_complete_large_fixture() -> None:
    # This is a deterministic finite observation, not an asymptotic claim.
    for q in (11, 19, 43):
        a = (q + 1) // 4
        result = decompose(100_003, 199_999, rational_mode(a, q))
        stage = result.rational_stage_diagnostic(q, a)["stage_q_contribution"]
        assert stage["real_sign"] == -1
        assert abs(stage["real"]) > 20 * abs(stage["imag"])


def test_complete_pre_q_wheel_stage_is_real_and_predicts_long_shell() -> None:
    expected = {
        11: -0.11687480550763536,
        19: -0.06710677778852056,
    }
    for q, value in expected.items():
        a = (q + 1) // 4
        wheel = circular_pre_q_wheel_stage(a, q)
        assert abs(wheel["normalized_stage"][0] - value) < 2e-15
        assert wheel["reflection_imaginary_error"] < 2e-15
        assert wheel["real_formula_error"] < 2e-15

        finite = decompose(100_003, 199_999, rational_mode(a, q))
        finite_stage = finite.stages[q] / finite.length
        # Boundary truncation is visible, but a shell containing many small
        # wheel periods already tracks the exact circular constant.
        assert abs(finite_stage.real - value) < 3e-4


def main() -> None:
    rational = decompose(101, 997, rational_mode(4, 17))
    assert rational.identity_error < 1e-9
    assert rational.prime_count == 143
    assert sum(rational.deleted_by_stage.values()) == (997 - 101 + 1) - 143

    # The identity is algebraic and must also hold for a nonperiodic log phase.
    log_mode = log_tent_mode(math.sqrt(10_007 * 12_007), 0.2, 0.49, 321.5)
    logarithmic = decompose(10_007, 12_007, log_mode)
    assert logarithmic.identity_error < 1e-8

    # A direct arbitrary complex polynomial mode catches sign/Jacobian errors.
    polynomial = decompose(
        211,
        521,
        lambda value: complex(value % 7, value % 11) * cmath.exp(0.013j * value),
    )
    assert polynomial.identity_error < 1e-8
    print(
        "PASS sieve-deletion identity",
        f"rational_stages={len(rational.stages)}",
        f"log_stages={len(logarithmic.stages)}",
    )


if __name__ == "__main__":
    main()
