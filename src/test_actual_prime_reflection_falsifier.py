import unittest

from flint import arb

from actual_prime_reflection_falsifier import certified_actual_prime_reflection


class ActualPrimeReflectionFalsifierTest(unittest.TestCase):
    def test_actual_prime_reflection_is_strictly_negative(self):
        values = certified_actual_prime_reflection()
        self.assertTrue(values["reflection"] < 0)
        self.assertTrue(values["reflection"] > arb("-0.22436"))
        self.assertTrue(values["reflection"] < arb("-0.22434"))
        self.assertTrue(values["prime_prime"] > 0)
        self.assertTrue(values["prime_background"] < 0)
        self.assertTrue(values["baseline_baseline"] > 0)
        self.assertTrue(values["prime_diagonal"] > 0)
        self.assertTrue(values["reflection_without_prime_diagonal"] < 0)


if __name__ == "__main__":
    unittest.main()
