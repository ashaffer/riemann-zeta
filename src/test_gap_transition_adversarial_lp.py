#!/usr/bin/env python3
"""Regression tests for the consecutive-gap adversarial LP."""

from __future__ import annotations

import math
import unittest
from dataclasses import replace
from fractions import Fraction

from gap_transition_adversarial_lp import (
    BlockSpec,
    CauchyClassBound,
    ConstraintSet,
    HeightSelectorBlock,
    MomentBound,
    RationalCell,
    TailBound,
    accessible_stage_frontier,
    atom_support,
    blocks_from_common_selector,
    build_problem,
    cauchy_class_certificates,
    enumerate_common_height_selectors,
    rationalize_feasible_solution,
    required_stage_second_moment_excess,
    solve_projection,
    weighted_endpoint_discrepancy,
)


F = Fraction


class GapTransitionAdversarialLPTest(unittest.TestCase):
    def setUp(self) -> None:
        self.block = BlockSpec("I0", 7, 1, F(1), F(1, 12))
        self.gaps = tuple(range(2, 43, 2))
        self.tail = (TailBound(14, F(2, 5)),)
        self.moments = (MomentBound(2, F(16)), MomentBound(3, F(400)))

    @staticmethod
    def full_flags(**updates: object) -> ConstraintSet:
        values = dict(
            uniform_count_marginals=True,
            physical_gap_congruence=True,
            wheel_admissibility=True,
            uniform_wheel_count_marginals=True,
            gt_tails=True,
            moments=True,
        )
        values.update(updates)
        return ConstraintSet(**values)

    def test_known_constraint_ladder_has_a_coherent_extremizer(self) -> None:
        problem = build_problem(
            (self.block,), self.gaps, flags=self.full_flags(),
            tail_bounds=self.tail, moment_bounds=self.moments,
        )
        solution = solve_projection(problem)
        self.assertTrue(solution.success, solution.status)
        solution = rationalize_feasible_solution(problem, solution)
        self.assertIsNotNone(solution.exact_values)
        # The exact number is not a theorem about primes; the robust fact is
        # that every listed finite constraint leaves a macroscopic mode.
        self.assertGreater(solution.objective_projection, 0.08)
        self.assertGreater(abs(solution.objective_complex), 0.08)
        self.assertGreater(weighted_endpoint_discrepancy(problem, solution)["half_l1"], 0.38)
        for item in atom_support(problem, solution):
            self.assertEqual((item["a"] + item["gap"]) % 7, item["b"])
            self.assertEqual(math.gcd(int(item["wheel_left"]), 30), 1)
            self.assertEqual(math.gcd(int(item["wheel_right"]), 30), 1)

    def test_weighted_uniformity_is_the_exact_missing_condition(self) -> None:
        problem = build_problem(
            (self.block,), self.gaps,
            flags=self.full_flags(weighted_uniform_marginals=True),
            tail_bounds=self.tail, moment_bounds=self.moments,
        )
        solution = solve_projection(problem)
        self.assertTrue(solution.success, solution.status)
        # For prime q=7 and r nonzero, the Ramanujan principal term is -1/6.
        self.assertAlmostEqual(solution.objective_complex.real, -1 / 6, places=10)
        self.assertAlmostEqual(solution.objective_complex.imag, 0.0, places=10)
        diagnostic = weighted_endpoint_discrepancy(problem, solution)
        self.assertLess(diagnostic["half_l1"], 1e-10)
        self.assertAlmostEqual(diagnostic["principal_modulus"], 1 / 6, places=10)

    def test_local_count_moment_cauchy_class_replays(self) -> None:
        stage = CauchyClassBound(
            "seven-multiple", 7, 0, F(1, 84), F(2), mass=F(1, 7)
        )
        problem = build_problem(
            (self.block,), self.gaps,
            flags=self.full_flags(cauchy_classes=True),
            tail_bounds=self.tail,
            moment_bounds=self.moments,
            cauchy_classes=(stage,),
        )
        solution = solve_projection(problem)
        self.assertTrue(solution.success, solution.status)
        certificate = cauchy_class_certificates(problem, solution)[0]
        self.assertAlmostEqual(float(certificate["mass"]), 1 / 7, places=10)
        self.assertLessEqual(
            float(certificate["dft_modulus"]),
            float(certificate["empirical_cauchy_bound"]) + 1e-10,
        )

    def test_endpoint_wheel_admissibility_does_not_bound_second_moment(self) -> None:
        flags = ConstraintSet(
            uniform_count_marginals=True,
            physical_gap_congruence=True,
            wheel_admissibility=True,
            uniform_wheel_count_marginals=True,
        )
        maxima = []
        for top in (42, 84):
            problem = build_problem(
                (self.block,), tuple(range(2, top + 1, 2)), flags=flags
            )
            # The solver accepts any linear diagnostic objective.  Here it
            # maximizes sum g^2*x while preserving count and mass exactly.
            problem = replace(
                problem,
                objective=tuple(complex(atom.gap**2) for atom in problem.atoms),
            )
            solution = solve_projection(problem)
            self.assertTrue(solution.success, solution.status)
            maxima.append(solution.objective_projection)
        self.assertGreater(maxima[1], 1.8 * maxima[0])

    def test_exact_consecutive_wheel_is_stronger_than_endpoint_sieving(self) -> None:
        block = BlockSpec("rough", 11, 3, F(1), F(4, 15))
        flags = ConstraintSet(
            uniform_count_marginals=True,
            physical_gap_congruence=True,
            wheel_admissibility=True,
            consecutive_wheel_survivors=True,
            uniform_wheel_count_marginals=True,
        )
        problem = build_problem((block,), tuple(range(1, 31)), flags=flags, wheel=30)
        solution = solve_projection(problem)
        self.assertTrue(solution.success, solution.status)
        # Consecutive units of the 2*3*5 wheel have gaps only 2,4,6.
        self.assertEqual({atom.gap for atom in problem.atoms}, {2, 4, 6})

    def test_common_height_selector_is_exact(self) -> None:
        selectors = enumerate_common_height_selectors(
            (
                HeightSelectorBlock(
                    "I0", F(1), F(0), (RationalCell(1, 7, F(1, 700)),)
                ),
                HeightSelectorBlock(
                    "I1", F(2), F(0), (RationalCell(2, 7, F(1, 350)),)
                ),
            ),
            F(1, 8),
            F(1, 6),
        )
        self.assertEqual(len(selectors), 1)
        self.assertEqual(selectors[0].height_left, F(99, 700))
        self.assertEqual(selectors[0].height_right, F(101, 700))
        blocks = blocks_from_common_selector(
            selectors[0], ("I0", "I1"), (F(1, 2), F(1, 2)),
            (F(1, 24), F(1, 24)),
        )
        problem = build_problem(
            blocks, self.gaps, flags=self.full_flags(),
            tail_bounds=self.tail, moment_bounds=self.moments,
        )
        solution = solve_projection(problem)
        self.assertTrue(solution.success, solution.status)
        self.assertGreater(solution.objective_projection, 0.09)

    def test_exact_solver_fallback(self) -> None:
        block = BlockSpec("tiny", 2, 1, F(1), F(1))
        problem = build_problem((block,), (1,), flags=ConstraintSet())
        solution = solve_projection(problem, math.pi, force_exact_fallback=True)
        self.assertTrue(solution.success, solution.status)
        self.assertEqual(solution.exact_values, (F(1),))
        self.assertAlmostEqual(solution.objective_projection, 1.0, places=12)

    def test_accessible_stage_frontier_exact_ledger(self) -> None:
        frontier = accessible_stage_frontier(F(799, 5000))
        self.assertEqual(frontier.forced_saving, F(1191, 110000))
        self.assertEqual(frontier.extremal_gap_exponent, F(16387, 110000))
        self.assertLess(frontier.forced_saving, F(90151617, 5_000_000_000))
        self.assertLess(frontier.gap_square_exponent, F(123, 100))
        self.assertLess(frontier.gap_third_exponent, F(1_299_969_230_769, 10**12))
        self.assertEqual(
            required_stage_second_moment_excess(
                F(799, 5000), F(90151617, 5_000_000_000)
            ),
            F(309348383, 2_500_000_000),
        )


if __name__ == "__main__":
    unittest.main()
