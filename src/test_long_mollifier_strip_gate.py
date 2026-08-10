import math
import unittest
from fractions import Fraction

from long_mollifier_strip_gate import (
    completed_coefficient_formula,
    divisors,
    exact_long_mollifier_strip_gate,
    first_overlength_band_formula,
    late_divisor_correction,
    logarithmic_mollifier_coefficient,
    long_mollifier_strip_gate,
    mobius,
    sharp_reciprocal_coefficient,
    theta_for_strip_width,
    verify_coefficient_ledger,
    von_mangoldt,
)


class LongMollifierStripGateTests(unittest.TestCase):
    def test_exact_rational_gate(self) -> None:
        exponent, boundary, width = exact_long_mollifier_strip_gate(
            Fraction(5, 4)
        )
        self.assertEqual(exponent, Fraction(9, 4))
        self.assertEqual(boundary, Fraction(9, 10))
        self.assertEqual(width, Fraction(1, 10))
        self.assertEqual(boundary, 1 - width)

    def test_float_gate_and_inverse(self) -> None:
        gate = long_mollifier_strip_gate(1.1)
        self.assertAlmostEqual(gate.natural_moment_exponent, 2.1)
        self.assertAlmostEqual(gate.right_boundary, 21.0 / 22.0)
        self.assertAlmostEqual(gate.strip_width, 1.0 / 22.0)
        self.assertAlmostEqual(
            gate.additive_resolution_exponent_in_y,
            2.0 * gate.strip_width,
        )
        self.assertAlmostEqual(
            theta_for_strip_width(gate.strip_width), gate.theta
        )

    def test_gate_validation(self) -> None:
        for theta in (1.0, 0.0, math.inf, math.nan):
            with self.assertRaises(ValueError):
                long_mollifier_strip_gate(theta)
        for width in (0.0, 0.5, -0.1, math.inf):
            with self.assertRaises(ValueError):
                theta_for_strip_width(width)
        with self.assertRaises(ValueError):
            exact_long_mollifier_strip_gate(Fraction(1, 1))


class ArithmeticFunctionTests(unittest.TestCase):
    def test_divisors_and_mobius(self) -> None:
        self.assertEqual(divisors(1), (1,))
        self.assertEqual(divisors(12), (1, 2, 3, 4, 6, 12))
        expected = {1: 1, 2: -1, 6: 1, 12: 0, 30: -1}
        for n, value in expected.items():
            self.assertEqual(mobius(n), value)

    def test_von_mangoldt(self) -> None:
        self.assertAlmostEqual(von_mangoldt(2), math.log(2))
        self.assertAlmostEqual(von_mangoldt(8), math.log(2))
        self.assertAlmostEqual(von_mangoldt(49), math.log(7))
        self.assertEqual(von_mangoldt(12), 0.0)


class MollifierCoefficientLedgerTests(unittest.TestCase):
    def test_completed_coefficient_identity_on_a_grid(self) -> None:
        residual = verify_coefficient_ledger(
            (2.5, 5.0, 9.25, 17.0), 250
        )
        self.assertLess(residual, 5.0e-13)

    def test_complete_head_is_von_mangoldt(self) -> None:
        for y in (6.0, 11.5, 30.0):
            for n in range(2, math.floor(y) + 1):
                self.assertAlmostEqual(
                    logarithmic_mollifier_coefficient(n, y),
                    von_mangoldt(n) / math.log(y),
                    places=13,
                )
                self.assertAlmostEqual(
                    late_divisor_correction(n, y), 0.0
                )

    def test_first_overlength_band_formula(self) -> None:
        for y in (5.5, 10.0, 17.25):
            for n in range(
                math.floor(y) + 1, math.floor(2.0 * y) + 1
            ):
                if n <= y:
                    continue
                self.assertAlmostEqual(
                    logarithmic_mollifier_coefficient(n, y),
                    first_overlength_band_formula(n, y),
                    places=13,
                )

    def test_sharp_reciprocal_stress_model(self) -> None:
        for cutoff in (2, 5, 11, 25):
            self.assertEqual(
                sharp_reciprocal_coefficient(1, cutoff), 1
            )
            for n in range(2, cutoff + 1):
                self.assertEqual(
                    sharp_reciprocal_coefficient(n, cutoff), 0
                )
            for n in range(cutoff + 1, 2 * cutoff + 1):
                self.assertEqual(
                    sharp_reciprocal_coefficient(n, cutoff),
                    -mobius(n),
                )

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            logarithmic_mollifier_coefficient(0, 2.0)
        with self.assertRaises(ValueError):
            logarithmic_mollifier_coefficient(2, 1.0)
        with self.assertRaises(ValueError):
            completed_coefficient_formula(1, 2.0)
        with self.assertRaises(ValueError):
            first_overlength_band_formula(3, 10.0)
        with self.assertRaises(ValueError):
            sharp_reciprocal_coefficient(2, 0)


if __name__ == "__main__":
    unittest.main()
