import math
import unittest

from high_order_mellin_residue import (
    central_residue_polynomial_coefficients,
    central_simple_pole_residue,
    completed_simple_pole_residue,
    completed_tail_formula,
    evaluate_polynomial,
    predicted_completed_principal_rate,
    principal_pole_ledger,
    real_target_survival_fraction,
    target_simple_pole_residue,
    target_survival_fraction,
    truncated_exponential,
)
from high_order_mollifier_shift import naive_carrier_rate


class ExactResidueIdentityTests(unittest.TestCase):
    def test_truncated_exponential(self) -> None:
        self.assertEqual(truncated_exponential(3.0, -1), 0.0j)
        self.assertEqual(truncated_exponential(3.0, 0), 1.0 + 0.0j)
        self.assertAlmostEqual(truncated_exponential(2.0, 2).real, 5.0)

    def test_target_plus_center_equals_taylor_remainder(self) -> None:
        for order in range(1, 10):
            for log_scale in (0.7, 2.0, 5.5):
                for pole_offset in (0.2, 0.7, 0.25 + 0.4j, -0.3 + 0.8j):
                    direct = completed_simple_pole_residue(
                        order, log_scale, pole_offset
                    )
                    tail = completed_tail_formula(order, log_scale, pole_offset)
                    self.assertAlmostEqual(direct.real, tail.real, places=10)
                    self.assertAlmostEqual(direct.imag, tail.imag, places=10)

    def test_polynomial_coefficients(self) -> None:
        for order in range(1, 9):
            for pole_offset in (0.3, 0.2 + 0.5j):
                coefficients = central_residue_polynomial_coefficients(
                    order, pole_offset
                )
                self.assertEqual(len(coefficients), max(0, order - 1))
                for log_scale in (0.5, 2.0, 4.0):
                    self.assertAlmostEqual(
                        evaluate_polynomial(coefficients, log_scale).real,
                        central_simple_pole_residue(
                            order, log_scale, pole_offset
                        ).real,
                        places=12,
                    )
                    self.assertAlmostEqual(
                        evaluate_polynomial(coefficients, log_scale).imag,
                        central_simple_pole_residue(
                            order, log_scale, pole_offset
                        ).imag,
                        places=12,
                    )

    def test_survival_fraction_identity(self) -> None:
        for order in range(1, 9):
            for log_scale in (1.0, 4.0):
                for pole_offset in (0.2, 0.5 + 0.3j):
                    target = target_simple_pole_residue(
                        order, log_scale, pole_offset
                    )
                    completed = completed_simple_pole_residue(
                        order, log_scale, pole_offset
                    )
                    fraction = target_survival_fraction(
                        order, log_scale, pole_offset
                    )
                    self.assertAlmostEqual(
                        (completed / target).real, fraction.real, places=11
                    )
                    self.assertAlmostEqual(
                        (completed / target).imag, fraction.imag, places=11
                    )

    def test_ledger(self) -> None:
        ledger = principal_pole_ledger(5, 3.0, 0.4 + 0.2j)
        self.assertAlmostEqual(
            (ledger.target_residue + ledger.central_residue).real,
            ledger.completed_residue.real,
        )
        self.assertAlmostEqual(
            (ledger.completed_residue / ledger.target_residue).imag,
            ledger.target_survival_fraction.imag,
        )


class PoissonTransitionTests(unittest.TestCase):
    def test_fraction_lies_in_unit_interval(self) -> None:
        for order in range(1, 50):
            for log_scale in (1.0, 5.0, 20.0):
                for displacement in (0.02, 0.1, 0.4):
                    fraction = real_target_survival_fraction(
                        order, log_scale, displacement
                    )
                    self.assertGreaterEqual(fraction, 0.0)
                    self.assertLessEqual(fraction, 1.0)

    def test_below_and_above_proportional_order_transition(self) -> None:
        log_scale = 100.0
        alpha = 0.2
        order = math.ceil(alpha * log_scale)
        below = real_target_survival_fraction(order, log_scale, 0.1)
        at_transition = real_target_survival_fraction(order, log_scale, alpha)
        above = real_target_survival_fraction(order, log_scale, 0.4)
        self.assertLess(below, 1.0e-3)
        self.assertGreater(at_transition, 0.4)
        self.assertLess(at_transition, 0.7)
        self.assertGreater(above, 0.999)

    def test_large_alpha_resolves_absolute_convergence_paradox(self) -> None:
        log_scale = 100.0
        alpha = 0.8
        order = math.ceil(alpha * log_scale)
        for displacement in (0.02, 0.1, 0.25, 0.49):
            self.assertLess(
                real_target_survival_fraction(order, log_scale, displacement),
                1.0e-6,
            )
            self.assertEqual(
                predicted_completed_principal_rate(alpha, displacement), 0.0
            )

    def test_predicted_rate_switch(self) -> None:
        alpha = 0.1
        self.assertEqual(predicted_completed_principal_rate(alpha, 0.05), 0.0)
        self.assertEqual(predicted_completed_principal_rate(alpha, 0.1), 0.0)
        self.assertAlmostEqual(
            predicted_completed_principal_rate(alpha, 0.3),
            naive_carrier_rate(alpha, 0.3),
        )
        self.assertGreater(predicted_completed_principal_rate(alpha, 0.3), 0.0)


class ValidationTests(unittest.TestCase):
    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            truncated_exponential(1.0, -2)
        with self.assertRaises(ValueError):
            target_simple_pole_residue(0, 1.0, 0.2)
        with self.assertRaises(ValueError):
            target_simple_pole_residue(2, 0.0, 0.2)
        with self.assertRaises(ValueError):
            target_simple_pole_residue(2, 1.0, 0.0)
        with self.assertRaises(ValueError):
            real_target_survival_fraction(2, 1.0, 0.0)
        with self.assertRaises(ValueError):
            predicted_completed_principal_rate(0.0, 0.1)
        with self.assertRaises(ValueError):
            predicted_completed_principal_rate(0.1, 0.0)


if __name__ == "__main__":
    unittest.main()
