import math
import unittest

from mobius_cutoff_recursion_probe import (
    audit_cutoff_step,
    audit_scale_step,
    verify_cutoff_shell_identity,
)
from type2_block_mechanism_probe import _arithmetic_sieve
from ward_nonlocal_covariance_probe import _grouped_tail_coefficients


class MobiusCutoffRecursionProbeTests(unittest.TestCase):
    def test_exact_cutoff_shell_identity(self) -> None:
        check = verify_cutoff_shell_identity(2, 100)
        self.assertLess(check.maximum_error, 2.0e-14)
        self.assertIn(24, check.changed_products)

    def test_small_complete_cutoff_step_is_not_a_contraction(self) -> None:
        audit = audit_cutoff_step()
        self.assertEqual(audit.lower.active_tail_product_values, (24, 25))
        self.assertEqual(audit.upper.active_tail_product_values, (24, 25))
        self.assertAlmostEqual(
            audit.lower.tail_diagonal_raw,
            audit.upper.tail_diagonal_raw,
            places=13,
        )
        self.assertGreater(audit.normalized_raw_ratio, 2.70)
        self.assertGreater(audit.normalized_covariance_ratio, 7.0)
        self.assertLess(audit.raw_contraction_margin, 0.0)
        self.assertLess(audit.normalized_raw_contraction_margin, 0.0)
        self.assertLess(audit.normalized_covariance_contraction_margin, 0.0)
        # The zero mode moves in the opposite direction, so there is no
        # channel-independent ordering either.
        self.assertLess(audit.normalized_zero_mode_ratio, 1.0)
        # With the unevaluated Type-I head, exact Vaughan completion is a
        # cutoff gauge: the completed field is identical on both sides.
        self.assertAlmostEqual(audit.exact_covariance_ratio, 1.0, places=14)
        self.assertAlmostEqual(
            audit.exact_covariance_difference, 0.0, places=14
        )

    def test_active_coefficient_flip_is_invisible_to_the_diagonal(self) -> None:
        mu, _, mangoldt, _ = _arithmetic_sieve(30)
        lower = _grouped_tail_coefficients(2, 30, mu, mangoldt)
        upper = _grouped_tail_coefficients(3, 30, mu, mangoldt)
        self.assertAlmostEqual(lower[24], -math.log(2.0), places=14)
        self.assertAlmostEqual(upper[24], math.log(2.0), places=14)
        self.assertAlmostEqual(lower[25], upper[25], places=14)
        # A simultaneous cutoff move can also create a grouped coefficient
        # from zero, so coefficientwise absolute contraction is false.
        self.assertAlmostEqual(lower[30], 0.0, places=14)
        self.assertAlmostEqual(upper[30], math.log(5.0), places=14)
        self.assertAlmostEqual(
            lower[24] ** 2 + lower[25] ** 2,
            upper[24] ** 2 + upper[25] ** 2,
            places=14,
        )

    def test_same_scale_has_both_cutoff_directions(self) -> None:
        decreasing = audit_cutoff_step(scale=25.0, cutoff=1, step=0.04)
        increasing = audit_cutoff_step(scale=25.0, cutoff=2, step=0.04)
        self.assertLess(decreasing.normalized_raw_ratio, 1.0)
        self.assertGreater(increasing.normalized_raw_ratio, 1.0)

    def test_large_local_amplification(self) -> None:
        audit = audit_cutoff_step(scale=101.0, cutoff=6, step=0.04)
        self.assertGreater(audit.normalized_raw_ratio, 28.0)
        self.assertLess(audit.shell.maximum_error, 2.0e-14)

    def test_higher_order_replication(self) -> None:
        audit = audit_cutoff_step(
            scale=50.0,
            cutoff=4,
            step=0.04,
            input_order=2,
            macro_order=2,
        )
        self.assertGreater(audit.normalized_raw_ratio, 14.0)

    def test_fixed_cutoff_scale_recursion_has_both_directions(self) -> None:
        increasing = audit_scale_step(24.0, 25.0, cutoff=3)
        decreasing = audit_scale_step(26.0, 27.0, cutoff=3)
        self.assertGreater(increasing.normalized_raw_ratio, 2.0)
        self.assertLess(decreasing.normalized_raw_ratio, 0.1)


if __name__ == "__main__":
    unittest.main()
