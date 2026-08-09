import math
import unittest

from ward_innovation_probe import (
    innovation_check,
    semiprime_diagonal_check,
    verify_ward_identity,
)


class WardInnovationProbeTests(unittest.TestCase):
    def test_ward_identity(self) -> None:
        check = verify_ward_identity(500)
        self.assertLess(check.max_error, 2.0e-12)

    def test_markov_innovation_identity(self) -> None:
        values = [
            math.sin(0.31 * index) + 0.2 * math.cos(0.07 * index)
            for index in range(100)
        ]
        check = innovation_check(values, 0.01, 5, 7)
        self.assertGreaterEqual(check.minimum_gamma, -2.0e-15)
        self.assertLess(check.identity_error, 2.0e-14)
        self.assertAlmostEqual(
            check.raw_energy,
            check.retained_energy + check.innovation_energy,
            places=13,
        )

    def test_semiprime_coefficient_has_right_scale(self) -> None:
        check = semiprime_diagonal_check(100_000, 0.1, 0.4)
        self.assertLess(
            abs(check.measured_coefficient - check.predicted_coefficient),
            0.04,
        )
        self.assertLess(abs(check.decomposition_error), 2.0e-14)
        self.assertGreaterEqual(check.measured_anisotropy, 0.0)


if __name__ == "__main__":
    unittest.main()
