import unittest

from r124_actual_qh_primitive_mellin_probe import primitive_mellin_audit


class ActualQhPrimitiveMellinProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = primitive_mellin_audit(
            ratio_nodes=1001,
            tau_maximum=30.0,
            tau_count=121,
            localizer_order=8,
        )

    def test_integer_ratio_is_positive_gram_value(self) -> None:
        self.assertGreater(self.audit.phi_at_one, 0.0)
        self.assertLess(self.audit.integer_gram_error, 2.0e-10)

    def test_full_shell_multiplier_has_both_signs(self) -> None:
        self.assertGreater(self.audit.lambda_at_zero, 1.0e-3)
        self.assertGreater(self.audit.maximum_lambda, 1.0e-2)
        self.assertLess(self.audit.minimum_lambda, -1.0e-2)
        self.assertTrue(self.audit.sign_change_intervals)

    def test_positive_definite_necessary_condition_fails(self) -> None:
        self.assertGreater(self.audit.maximum_kernel_modulus_ratio, 2.0)


if __name__ == "__main__":
    unittest.main()
