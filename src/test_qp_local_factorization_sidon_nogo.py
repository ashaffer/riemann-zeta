import unittest
from fractions import Fraction

from qp_local_factorization_sidon_nogo import LocalSidonLedger, active_ledger


class LocalFactorizationSidonNogoTests(unittest.TestCase):
    def test_active_ledger(self) -> None:
        ledger = active_ledger()
        self.assertEqual(ledger.antenna_power, Fraction(1, 50))
        self.assertGreater(ledger.antenna_power, ledger.target_power)
        self.assertEqual(ledger.mean_bias_power, 0)
        self.assertLess(ledger.sidon_union_power, 0)
        self.assertLess(ledger.integer_sidon_union_power, 0)
        self.assertLess(ledger.integer_high_bias_power, ledger.antenna_power)

    def test_support_must_clear_twice_target(self) -> None:
        ledger = LocalSidonLedger(
            aperture=Fraction(50, 33),
            low_endpoint=Fraction(1, 100),
            target_power=Fraction(19, 1000),
            support_power=Fraction(19, 500),
            integrations=4,
        )
        with self.assertRaises(ValueError):
            ledger.verify()

    def test_sidon_union_bound_is_enforced(self) -> None:
        ledger = LocalSidonLedger(
            aperture=Fraction(1, 1),
            low_endpoint=Fraction(1, 100),
            target_power=Fraction(1, 100),
            support_power=Fraction(1, 3),
            integrations=20,
        )
        with self.assertRaises(ValueError):
            ledger.verify()

    def test_bias_bound_is_enforced(self) -> None:
        ledger = LocalSidonLedger(
            aperture=Fraction(50, 33),
            low_endpoint=Fraction(1, 100),
            target_power=Fraction(19, 1000),
            support_power=Fraction(1, 25),
            integrations=1,
        )
        with self.assertRaises(ValueError):
            ledger.verify()

    def test_integer_high_band_bound_is_enforced(self) -> None:
        ledger = LocalSidonLedger(
            aperture=Fraction(19, 10),
            low_endpoint=Fraction(1, 100),
            target_power=Fraction(1, 100),
            support_power=Fraction(1, 10),
            integrations=10,
        )
        ledger.verify()
        with self.assertRaises(ValueError):
            ledger.verify_integer_log_version()


if __name__ == "__main__":
    unittest.main()
