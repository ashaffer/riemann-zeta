#!/usr/bin/env python3
"""Replay the transition LP and the exact q-stage exponent frontier.

This verifies finite rational constraints and exponent arithmetic.  It does
not assert that an LP extremizer is an actual-prime configuration.
"""

from __future__ import annotations

import math
import sys
from dataclasses import replace
from fractions import Fraction
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from gap_transition_adversarial_lp import (  # noqa: E402
    BlockSpec,
    ConstraintSet,
    MomentBound,
    TailBound,
    accessible_stage_frontier,
    atom_support,
    build_problem,
    gt_tail_saving,
    rationalize_feasible_solution,
    required_stage_second_moment_excess,
    solve_projection,
    weighted_endpoint_discrepancy,
)


F = Fraction
BETA = F(799, 5000)
THETA = F(397, 2500)
KAPPA_SLICE = F(17_522_268_449_743_408, 10**18)
KAPPA_BAND_MAX = F(197_404_825_829_421, 10**16)


def exact_exponent_ledger() -> None:
    frontier = accessible_stage_frontier(BETA)
    assert frontier.extremal_gap_exponent == F(16387, 110000)
    assert frontier.forced_saving == F(1191, 110000)
    assert frontier.forced_saving == gt_tail_saving(frontier.extremal_gap_exponent)
    assert frontier.forced_saving < KAPPA_SLICE < KAPPA_BAND_MAX

    # One-scale adversary: N_q=Y^(1-beta) gaps of size Y^h_star.
    assert frontier.gap_square_exponent == F(31299, 27500)
    assert frontier.gap_square_exponent < F(123, 100)
    assert frontier.gap_third_exponent == F(141583, 110000)
    truncated_m3_cap = 1 + 2 * THETA - gt_tail_saving(THETA)
    assert truncated_m3_cap == F(42249, 32500)
    assert frontier.gap_third_exponent < truncated_m3_cap
    assert F(2, 15) < frontier.extremal_gap_exponent < THETA < BETA

    # Accessible alternatives: max gap and known S2 do not close.  The
    # proposed new rough S2=Y^(1+o(1)) would close an individual q-stage.
    assert BETA - THETA == F(1, 1000) < frontier.forced_saving
    known_s2_saving = (BETA - F(23, 100)) / 2
    assert known_s2_saving == -F(351, 10000)
    optional_rough_s2_saving = BETA / 2
    assert optional_rough_s2_saving == F(799, 10000) > KAPPA_BAND_MAX
    slice_rho = required_stage_second_moment_excess(BETA, KAPPA_SLICE)
    band_rho = required_stage_second_moment_excess(BETA, KAPPA_BAND_MAX)
    assert slice_rho == F(3_898_608_221_891_037, 31_250_000_000_000_000)
    assert band_rho == F(601_595_174_170_579, 5_000_000_000_000_000)
    assert 0 < band_rho < slice_rho < F(23, 100)

    # Count+GT can close only above these denominator exponents.
    slice_crossing = F(2, 15) + F(22, 9) * KAPPA_SLICE
    band_crossing = F(2, 15) + F(22, 9) * KAPPA_BAND_MAX
    assert BETA < slice_crossing < band_crossing


def finite_rational_extremizer() -> tuple[float, float, int, int]:
    block = BlockSpec("I0", 7, 1, F(1), F(1, 12))
    gaps = tuple(range(2, 43, 2))
    flags = ConstraintSet(
        uniform_count_marginals=True,
        physical_gap_congruence=True,
        wheel_admissibility=True,
        uniform_wheel_count_marginals=True,
        gt_tails=True,
        moments=True,
    )
    problem = build_problem(
        (block,), gaps, flags=flags,
        tail_bounds=(TailBound(14, F(2, 5)),),
        moment_bounds=(MomentBound(2, F(16)), MomentBound(3, F(400))),
    )
    numerical = solve_projection(problem)
    assert numerical.success
    solution = rationalize_feasible_solution(problem, numerical)
    assert solution.exact_values is not None
    # Rigorous interval replay of the real selected DFT.  All LP weights are
    # exact Fractions and pi is introduced as an interval constant.
    mp.iv.dps = 60
    interval_projection = mp.iv.mpf(0)
    for index, atom in enumerate(problem.atoms):
        weight = solution.exact_values[index]
        if not weight:
            continue
        exact_weight = mp.iv.mpf(weight.numerator) / weight.denominator
        left = mp.iv.cos(2 * mp.iv.pi * atom.a / 7)
        right = mp.iv.cos(2 * mp.iv.pi * atom.b / 7)
        interval_projection += atom.gap * exact_weight * (left + right) / 2
    certified_lower = float(interval_projection.a)
    assert certified_lower > 0.08
    discrepancy = weighted_endpoint_discrepancy(problem, solution)
    assert discrepancy["half_l1"] > 0.38
    support = atom_support(problem, solution)
    assert support
    assert all((int(item["a"]) + int(item["gap"])) % 7 == item["b"] for item in support)
    assert all(math.gcd(int(item["wheel_left"]), 30) == 1 for item in support)
    assert all(math.gcd(int(item["wheel_right"]), 30) == 1 for item in support)
    return (
        certified_lower,
        discrepancy["half_l1"],
        len(support),
        max(value.denominator for value in solution.exact_values),
    )


def endpoint_wheel_moment_failure() -> tuple[float, float]:
    block = BlockSpec("I0", 7, 1, F(1), F(1, 12))
    flags = ConstraintSet(
        uniform_count_marginals=True,
        physical_gap_congruence=True,
        wheel_admissibility=True,
        uniform_wheel_count_marginals=True,
    )
    maxima = []
    for top in (42, 84):
        problem = build_problem(
            (block,), tuple(range(2, top + 1, 2)), flags=flags
        )
        moment_problem = replace(
            problem,
            objective=tuple(complex(atom.gap**2) for atom in problem.atoms),
        )
        solution = solve_projection(moment_problem)
        assert solution.success
        maxima.append(solution.objective_projection)
    assert maxima[1] > 1.8 * maxima[0]
    return maxima[0], maxima[1]


def main() -> None:
    exact_exponent_ledger()
    projection, discrepancy, support_size, denominator = finite_rational_extremizer()
    moment_42, moment_84 = endpoint_wheel_moment_failure()
    frontier = accessible_stage_frontier(BETA)
    print("PASS gap-transition adversarial LP")
    print(f"accessible_stage_saving={float(frontier.forced_saving):.12f}")
    print(f"extremal_gap_exponent={float(frontier.extremal_gap_exponent):.12f}")
    print(f"slice_deficit={float(KAPPA_SLICE-frontier.forced_saving):.12f}")
    print(f"band_deficit={float(KAPPA_BAND_MAX-frontier.forced_saving):.12f}")
    print(f"optional_rough_S2_saving={float(BETA/2):.12f}")
    print(f"required_rho_slice<{float(required_stage_second_moment_excess(BETA,KAPPA_SLICE)):.12f}")
    print(f"required_rho_band<{float(required_stage_second_moment_excess(BETA,KAPPA_BAND_MAX)):.12f}")
    print(f"finite_exact_projection={projection:.12f}")
    print(f"finite_weighted_half_l1={discrepancy:.12f}")
    print(f"finite_support={support_size} max_denominator={denominator}")
    print(f"endpoint_wheel_max_S2(top=42)={moment_42:.12f}")
    print(f"endpoint_wheel_max_S2(top=84)={moment_84:.12f}")


if __name__ == "__main__":
    main()
