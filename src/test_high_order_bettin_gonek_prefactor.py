import cmath
import unittest

from high_order_bettin_gonek_prefactor import (
    bettin_gonek_prefactor,
    central_full_prefactor_residue,
    completed_factor_taylor_coefficients,
    completed_full_prefactor_residue,
    evaluate_taylor,
    full_prefactor_ledger,
    full_prefactor_taylor_remainder,
    prefactor_taylor_coefficients,
    target_full_prefactor_residue,
)


class PrefactorSeriesTests(unittest.TestCase):
    def test_prefactor_taylor_series(self) -> None:
        for height in (0.0, 1.5, 14.134725):
            coefficients = prefactor_taylor_coefficients(height, 12)
            for value in (1.0e-4, -2.0e-4 + 1.0e-4j):
                approximation = evaluate_taylor(coefficients, value)
                exact = bettin_gonek_prefactor(value, height)
                self.assertTrue(
                    cmath.isclose(
                        approximation, exact, rel_tol=1.0e-12, abs_tol=1.0e-12
                    )
                )

    def test_completed_factor_taylor_series(self) -> None:
        log_scale = 3.0
        height = 7.0
        coefficients = completed_factor_taylor_coefficients(
            log_scale, height, 14
        )
        for value in (1.0e-4, -1.0e-4 + 2.0e-4j):
            approximation = evaluate_taylor(coefficients, value)
            exact = cmath.exp(log_scale * value) * bettin_gonek_prefactor(
                value, height
            )
            self.assertTrue(
                cmath.isclose(
                    approximation, exact, rel_tol=1.0e-12, abs_tol=1.0e-12
                )
            )


class FullResidueIdentityTests(unittest.TestCase):
    def test_target_plus_center_equals_full_taylor_remainder(self) -> None:
        for order in range(1, 10):
            for log_scale in (0.8, 2.0, 5.0):
                for height in (0.0, 3.0, 14.134725):
                    for target_offset in (0.15, 0.4, 0.2 + 0.3j):
                        direct = completed_full_prefactor_residue(
                            order, log_scale, height, target_offset
                        )
                        remainder = full_prefactor_taylor_remainder(
                            order, log_scale, height, target_offset
                        )
                        self.assertTrue(
                            cmath.isclose(
                                direct,
                                remainder,
                                rel_tol=2.0e-9,
                                abs_tol=2.0e-9,
                            ),
                            msg=(
                                f"k={order}, L={log_scale}, t={height}, "
                                f"z0={target_offset}"
                            ),
                        )

    def test_order_one_has_no_central_residue(self) -> None:
        for height in (0.0, 4.0):
            for target_offset in (0.2, 0.3 + 0.1j):
                self.assertEqual(
                    central_full_prefactor_residue(
                        1, 2.0, height, target_offset
                    ),
                    0.0j,
                )
                self.assertTrue(
                    cmath.isclose(
                        completed_full_prefactor_residue(
                            1, 2.0, height, target_offset
                        ),
                        target_full_prefactor_residue(
                            1, 2.0, height, target_offset
                        ),
                    )
                )

    def test_ledger(self) -> None:
        ledger = full_prefactor_ledger(7, 4.0, 14.134725, 0.25)
        self.assertTrue(
            cmath.isclose(
                ledger.target_residue + ledger.central_residue,
                ledger.completed_residue,
            )
        )
        self.assertTrue(
            cmath.isclose(
                ledger.completed_residue / ledger.target_residue,
                ledger.completed_over_target,
            )
        )


class ValidationTests(unittest.TestCase):
    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            prefactor_taylor_coefficients(0.0, -1)
        with self.assertRaises(ValueError):
            completed_factor_taylor_coefficients(0.0, 0.0, 2)
        with self.assertRaises(ValueError):
            target_full_prefactor_residue(0, 1.0, 0.0, 0.2)
        with self.assertRaises(ValueError):
            target_full_prefactor_residue(2, 0.0, 0.0, 0.2)
        with self.assertRaises(ValueError):
            target_full_prefactor_residue(2, 1.0, 0.0, 0.0)


if __name__ == "__main__":
    unittest.main()
