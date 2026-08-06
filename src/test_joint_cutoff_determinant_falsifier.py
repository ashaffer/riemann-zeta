import unittest

from flint import arb

from joint_cutoff_determinant_falsifier import certified_sign_flip


class JointCutoffDeterminantFalsifierTest(unittest.TestCase):
    def test_ramp_evaluated_determinant_changes_sign(self):
        positive, negative = certified_sign_flip()
        self.assertTrue(positive["det"] > 0)
        self.assertTrue(negative["det"] < 0)
        self.assertTrue(positive["det"] > arb("8.7819"))
        self.assertTrue(positive["det"] < arb("8.7820"))
        self.assertTrue(negative["det"] > arb("-3.6337"))
        self.assertTrue(negative["det"] < arb("-3.6336"))

    def test_prime_only_determinant_also_changes_sign(self):
        positive, negative = certified_sign_flip(prime_only=True)
        self.assertTrue(positive["det"] > 0)
        self.assertTrue(negative["det"] < 0)
        self.assertTrue(positive["det"] > arb("6.1632"))
        self.assertTrue(positive["det"] < arb("6.1633"))
        self.assertTrue(negative["det"] > arb("-2.7000"))
        self.assertTrue(negative["det"] < arb("-2.6999"))


if __name__ == "__main__":
    unittest.main()
