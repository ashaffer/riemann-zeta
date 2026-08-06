import math
import unittest

import numpy as np

from signed_garding_failfast import completed_symbol, pole_symbol, prime_powers


class SignedGardingFailFastTest(unittest.TestCase):
    def setUp(self):
        self.logs, self.weights = prime_powers(100)

    def test_pole_value_at_zero(self):
        for a in (0.1, 7 / 16, 1.0, 2.0):
            self.assertAlmostEqual(float(pole_symbol(a, 0.0)), 8 * math.sinh(a))

    def test_first_window_contains_only_two(self):
        a = 7 / 16
        active_logs = self.logs[self.logs < 2 * a]
        self.assertEqual(active_logs.size, 1)
        self.assertAlmostEqual(float(active_logs[0]), math.log(2))

    def test_certified_window_symbol_is_not_pointwise_positive(self):
        value = completed_symbol(7 / 16, 0.0, self.logs, self.weights)
        self.assertAlmostEqual(float(value), -2.73971447387, places=10)

    def test_scalar_and_vector_evaluation_agree(self):
        points = np.asarray([0.0, 0.5, 3.0])
        vector = completed_symbol(1.0, points, self.logs, self.weights)
        scalar = np.asarray(
            [completed_symbol(1.0, t, self.logs, self.weights) for t in points]
        )
        np.testing.assert_allclose(vector, scalar, rtol=0, atol=1e-13)


if __name__ == "__main__":
    unittest.main()
