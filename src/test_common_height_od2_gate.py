#!/usr/bin/env python3

import cmath
import math
import unittest
from fractions import Fraction

from common_height_od2_gate import (
    EDGE_EXPONENT,
    H_MIN,
    affine_moments,
    covariance_ledger,
    deletion_atom,
    exponent_ledger,
    first_return_distance,
    paired_first_return_product,
    periodic_refinement,
    signed_difference,
    telescope_deletions,
    trapezoid_measure,
)


class CommonHeightOD2GateTests(unittest.TestCase):
    def test_trapezoid_mass_and_first_moment(self) -> None:
        points = [1, 4, 9, 13]
        mass = trapezoid_measure(points)
        self.assertEqual(sum(mass.values()), 12)
        self.assertEqual(sum(n * value for n, value in mass.items()), Fraction(13**2 - 1, 2))

    def test_single_deletion_atom(self) -> None:
        active = [0, 3, 8]
        self.assertEqual(
            deletion_atom(active, 3),
            {0: Fraction(5, 2), 3: -4, 8: Fraction(3, 2)},
        )

    def test_deletion_telescope(self) -> None:
        fine = [0, 2, 5, 7, 11, 14]
        total, coarse = telescope_deletions(fine, [5, 11, 7])
        self.assertEqual(coarse, [0, 2, 14])
        self.assertEqual(total, signed_difference(coarse, fine))

    def test_affine_exactness(self) -> None:
        difference = signed_difference([0, 5, 12], list(range(13)))
        self.assertEqual(affine_moments(difference), (0, 0))

    def test_general_log_shift_identity(self) -> None:
        coefficients = {11: Fraction(3, 2), 13: -2, 18: Fraction(1, 2)}
        height = 37.25
        phases = {n: cmath.exp(1j * height * math.log(n)) for n in coefficients}
        ledger = covariance_ledger(coefficients, phases)
        self.assertAlmostEqual(
            float(ledger["square"]),
            float(ledger["diagonal"]) + complex(ledger["off_diagonal"]).real,
            places=10,
        )
        self.assertAlmostEqual(
            complex(ledger["off_diagonal"]).real,
            float(ledger["twice_real_positive_shift"]),
            places=10,
        )

    def test_first_return_automaton(self) -> None:
        self.assertEqual(first_return_distance([0, 0, 1, 0]), 3)
        self.assertEqual(first_return_distance([1, 0, 0]), 1)

    def test_tensor_automaton(self) -> None:
        left = [0, 0, 1, 0]
        right = [0, 1, 0, 0]
        self.assertEqual(paired_first_return_product(left, right), 6)

    def test_periodic_nested_obstruction(self) -> None:
        result = periodic_refinement(17, 13, 5)
        length = result["length"]
        self.assertAlmostEqual(result["fourier_abs"], length, places=9)
        self.assertAlmostEqual(result["square"], length * length, places=7)
        self.assertEqual(result["mass"], 0)
        self.assertEqual(result["first_moment"], 0)
        self.assertLess(result["shift_discrepancy"], 1e-6)

    def test_exponent_miss_is_strict(self) -> None:
        self.assertGreater(H_MIN, EDGE_EXPONENT)
        ledger = exponent_ledger()
        self.assertEqual(ledger["generic_model_miss"], str(H_MIN - EDGE_EXPONENT))


if __name__ == "__main__":
    unittest.main()
