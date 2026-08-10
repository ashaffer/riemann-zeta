import unittest
from fractions import Fraction

from high_order_mellin_center import (
    center_after_shifted_derivatives,
    central_pole_order,
    central_residue_polynomial,
    full_annihilation_repays_target,
    polynomial_derivative,
    remaining_center_degree,
    target_factor_after_shifted_derivatives,
)


class CentralResiduePolynomialTests(unittest.TestCase):
    def test_low_orders(self) -> None:
        self.assertEqual(central_residue_polynomial(0, ()), ())
        self.assertEqual(central_residue_polynomial(1, ()), ())
        self.assertEqual(central_residue_polynomial(2, (2,)), (Fraction(4),))
        # 4! * [r_2 + r_1 L + r_0 L^2/2]
        self.assertEqual(
            central_residue_polynomial(4, (1, 2, 3)),
            (Fraction(72), Fraction(48), Fraction(12)),
        )

    def test_exact_formula_with_rational_taylor_data(self) -> None:
        polynomial = central_residue_polynomial(
            5, (Fraction(1, 2), Fraction(-2, 3), Fraction(5, 7), Fraction(11, 13))
        )
        self.assertEqual(
            polynomial,
            (
                Fraction(1320, 13),
                Fraction(600, 7),
                Fraction(-40),
                Fraction(10),
            ),
        )

    def test_requires_complete_taylor_prefix(self) -> None:
        with self.assertRaises(ValueError):
            central_residue_polynomial(4, (1, 2))
        with self.assertRaises(TypeError):
            central_residue_polynomial(2, (0.5,))


class ShiftedDerivativeTests(unittest.TestCase):
    def test_derivative_exactness(self) -> None:
        polynomial = (Fraction(7), Fraction(-3), Fraction(5), Fraction(2))
        self.assertEqual(
            polynomial_derivative(polynomial),
            (Fraction(-3), Fraction(10), Fraction(6)),
        )
        self.assertEqual(
            polynomial_derivative(polynomial, 2),
            (Fraction(10), Fraction(12)),
        )
        self.assertEqual(polynomial_derivative(polynomial, 4), ())

    def test_full_center_annihilation(self) -> None:
        for order in range(1, 9):
            taylor = tuple(Fraction(index + 1, index + 2) for index in range(order))
            steps = central_pole_order(order)
            self.assertEqual(
                center_after_shifted_derivatives(order, taylor, steps), ()
            )
            self.assertEqual(remaining_center_degree(order, steps), -1)
            if steps > 0:
                self.assertNotEqual(
                    center_after_shifted_derivatives(order, taylor, steps - 1),
                    (),
                )

    def test_target_repayment(self) -> None:
        shifts = (Fraction(1, 11), Fraction(1, 3), Fraction(2, 5), Fraction(7, 4))
        full_annihilation_repays_target(range(1, 10), shifts)
        for order in range(1, 10):
            steps = central_pole_order(order)
            for shift in shifts:
                self.assertEqual(
                    target_factor_after_shifted_derivatives(order, steps, shift),
                    1,
                )

    def test_partial_annihilation_tradeoff(self) -> None:
        order = 6
        shift = Fraction(1, 4)
        self.assertEqual(
            target_factor_after_shifted_derivatives(order, 0, shift),
            Fraction(4**5),
        )
        self.assertEqual(
            target_factor_after_shifted_derivatives(order, 3, shift),
            Fraction(4**2),
        )
        self.assertEqual(
            target_factor_after_shifted_derivatives(order, 5, shift),
            1,
        )
        self.assertEqual(
            target_factor_after_shifted_derivatives(order, 6, shift),
            shift,
        )


class ValidationTests(unittest.TestCase):
    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            central_pole_order(-1)
        with self.assertRaises(ValueError):
            polynomial_derivative((1,), -1)
        with self.assertRaises(ValueError):
            remaining_center_degree(3, -1)
        with self.assertRaises(ValueError):
            target_factor_after_shifted_derivatives(3, 2, 0)
        with self.assertRaises(ValueError):
            full_annihilation_repays_target((), (Fraction(1, 2),))
        with self.assertRaises(ValueError):
            full_annihilation_repays_target((0,), (Fraction(1, 2),))


if __name__ == "__main__":
    unittest.main()
