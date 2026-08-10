import unittest
from fractions import Fraction

from kloosterman_strip_gate import (
    blomer_pascadi_term_exponents,
    conditional_strip_gate,
    critical_blomer_pascadi_gate,
    remainder_exponent_in_t,
    remainder_surplus,
    target_exponent_in_t,
    theorem_saving_at_length,
    trivial_bilinear_exponent,
)


class BlomerPascadiExponentTests(unittest.TestCase):
    def test_critical_term_exponents(self) -> None:
        exponents = blomer_pascadi_term_exponents(Fraction(1, 2))
        self.assertEqual(exponents[0], Fraction(31, 32))
        self.assertEqual(exponents[1], Fraction(31, 32))
        self.assertEqual(exponents[2], Fraction(17, 18))
        self.assertEqual(trivial_bilinear_exponent(Fraction(1, 2)), 1)
        self.assertEqual(theorem_saving_at_length(Fraction(1, 2)), Fraction(1, 32))

    def test_saving_is_nonnegative(self) -> None:
        for numerator in range(0, 33):
            saving = theorem_saving_at_length(Fraction(numerator, 32))
            self.assertGreaterEqual(saving, 0)


class ConditionalStripGateTests(unittest.TestCase):
    def test_critical_gate(self) -> None:
        gate = critical_blomer_pascadi_gate()
        self.assertEqual(gate.saving, Fraction(1, 32))
        self.assertEqual(gate.maximum_theta, Fraction(32, 31))
        self.assertEqual(gate.strip_width, Fraction(1, 64))
        self.assertEqual(gate.right_zero_boundary, Fraction(63, 64))
        self.assertEqual(gate.natural_moment_exponent, Fraction(63, 31))

    def test_exact_exponent_balance(self) -> None:
        saving = Fraction(1, 32)
        theta = Fraction(32, 31)
        self.assertEqual(
            remainder_exponent_in_t(theta, saving),
            target_exponent_in_t(theta),
        )
        self.assertEqual(remainder_surplus(theta, saving), 0)
        self.assertLess(remainder_surplus(Fraction(1), saving), 0)
        self.assertGreater(remainder_surplus(Fraction(33, 32), saving), 0)

    def test_general_width_is_half_saving(self) -> None:
        for saving in (Fraction(1, 100), Fraction(1, 32), Fraction(1, 12), Fraction(1, 4)):
            gate = conditional_strip_gate(saving)
            self.assertEqual(gate.maximum_theta, 1 / (1 - saving))
            self.assertEqual(gate.strip_width, saving / 2)
            self.assertEqual(gate.right_zero_boundary, 1 - saving / 2)
            self.assertEqual(remainder_surplus(gate.maximum_theta, saving), 0)


class ValidationTests(unittest.TestCase):
    def test_validation(self) -> None:
        with self.assertRaises(TypeError):
            conditional_strip_gate(0.1)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            conditional_strip_gate(Fraction(0))
        with self.assertRaises(ValueError):
            conditional_strip_gate(Fraction(1))
        with self.assertRaises(ValueError):
            theorem_saving_at_length(Fraction(-1, 4))
        with self.assertRaises(ValueError):
            remainder_exponent_in_t(Fraction(0), Fraction(1, 32))


if __name__ == "__main__":
    unittest.main()
