from __future__ import annotations

import unittest

from mobius_greedy_dependency_audit import adjacent, audit


class MobiusGreedyDependencyAuditTest(unittest.TestCase):
    def test_exchange_adjacency(self) -> None:
        self.assertTrue(adjacent((3, 7, 23, 41), (3, 7, 491)))
        self.assertTrue(adjacent((3, 7, 17, 29), (3, 5, 7, 11, 17)))
        self.assertFalse(adjacent((3, 7), (3, 11)))
        self.assertFalse(adjacent((3, 5, 7), (3, 5, 11)))

    def test_exact_defect_decomposition(self) -> None:
        result, paths = audit(10_000, 100_000)
        self.assertEqual(result["M_N"], -23)
        self.assertEqual(result["greedy_unmatched"], 23)
        self.assertEqual(result["greedy_deficiency"], 0)
        self.assertEqual(paths, [])
        self.assertTrue(result["decomposition_verified"])

    def test_length_three_certificate(self) -> None:
        result, paths = audit(20_000, 100_000)
        self.assertEqual(result["M_N"], 26)
        self.assertEqual(result["greedy_unmatched"], 28)
        self.assertEqual(result["greedy_deficiency"], 1)
        self.assertEqual(paths, [(19_803, 10_311, 10_353, 19_635)])
        self.assertTrue(result["smaller_side_saturated_after_paths"])
        self.assertEqual(result["residual_after_paths"], 26)

    def test_scan_cap_is_explicit(self) -> None:
        result, paths = audit(20_000, 1)
        self.assertFalse(result["length3_scan_complete"])
        self.assertFalse(result["smaller_side_saturated_after_paths"])
        self.assertEqual(paths, [])


if __name__ == "__main__":
    unittest.main()
