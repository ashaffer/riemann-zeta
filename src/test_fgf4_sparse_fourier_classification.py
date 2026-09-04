from __future__ import annotations

import itertools
import math
import unittest

from fgf4_sparse_fourier_classification import (
    degree_sensitive_energy_floor,
    energy_rigidity,
    exhaustive_support_maximum,
    fourier_energy,
    galois_energy_orbit,
    is_selected_interval,
    local_sparse_model,
    phase_arc_stability,
    selected_progression_discrepancy,
    sharp_support_extremum,
)


class FGF4SparseFourierClassificationTests(unittest.TestCase):
    def test_sharp_support_extremum_and_equality(self) -> None:
        for q in (7, 11):
            for size in range(1, q):
                maximum, number = exhaustive_support_maximum(q, size, 3)
                self.assertAlmostEqual(maximum, sharp_support_extremum(q, size))
                self.assertEqual(number, q)
                for subset in itertools.combinations(range(q), size):
                    value = abs(
                        sum(
                            complex(
                                math.cos(2 * math.pi * 3 * row / q),
                                math.sin(2 * math.pi * 3 * row / q),
                            )
                            for row in subset
                        )
                    )
                    if abs(value - maximum) < 1e-9:
                        self.assertTrue(is_selected_interval(subset, q, 3))

    def test_energy_rigidity_and_quantization(self) -> None:
        for values in ((0, 1, 3), (0, 1, 4), (0, 2, 5, 7)):
            q = 11
            row = energy_rigidity(values, q)
            direct_excess = sum(
                (count - row.lambda_off_diagonal) ** 2
                for count in row.correlation[1:]
            )
            self.assertEqual(row.excess, direct_excess)
            self.assertGreaterEqual(row.quantized_gap, 0)
            self.assertEqual(row.quantized_gap % 2, 0)

    def test_difference_set_is_exact_energy_minimizer(self) -> None:
        # The quadratic residues modulo 7 form a (7,3,1) difference set.
        row = energy_rigidity((1, 2, 4), 7)
        self.assertTrue(row.is_difference_set)
        self.assertTrue(row.is_almost_difference_set)
        self.assertEqual(row.excess, 0)
        orbit = galois_energy_orbit((1, 2, 4), 7, 1)
        self.assertEqual(orbit.degree, 1)
        self.assertAlmostEqual(orbit.selected_energy, float(orbit.mu_fourier))

    def test_galois_degree_trace_and_generic_simplicity(self) -> None:
        # gcd(10,3*2)=2, so every three-subset modulo 11 has stabilizer {+-1}.
        values = (0, 1, 4)
        row = galois_energy_orbit(values, 11, 3)
        self.assertEqual(row.cardinality_gcd, 2)
        self.assertEqual(row.stabilizer, (1, 10))
        self.assertEqual(row.degree, 5)
        self.assertEqual(row.trace, 12)
        self.assertEqual(len(row.level_cosets), 5)
        self.assertTrue(all(len(coset) == 2 for coset in row.level_cosets))
        self.assertLess(row.selected_energy, float(row.trace_bound) + 1e-10)

        energies = [fourier_energy(values, 11, frequency) for frequency in range(1, 11)]
        for left in range(1, 11):
            for right in range(1, 11):
                equal = abs(energies[left - 1] - energies[right - 1]) < 1e-8
                self.assertEqual(equal, right in (left, (-left) % 11))

    def test_degree_sensitive_energy_penalty(self) -> None:
        values = (0, 1, 4)
        rigidity = energy_rigidity(values, 11)
        orbit = galois_energy_orbit(values, 11, 1)
        lower = degree_sensitive_energy_floor(rigidity, orbit)
        self.assertGreaterEqual(float(rigidity.centered_energy) + 1e-10, lower)

    def test_selected_coefficient_forces_a_progression_race(self) -> None:
        row = selected_progression_discrepancy((0, 1, 4), 11, 3)
        self.assertGreater(row.discrepancy, 0)
        self.assertLessEqual(row.selected_modulus, 4 * float(row.discrepancy) + 1e-9)
        # For FGF4, 4 is the inverse of a=(q+1)/4 modulo q.
        self.assertEqual(pow((11 + 1) // 4, -1, 11), 4)

    def test_near_extremizer_phase_arc_stability(self) -> None:
        row = phase_arc_stability((0, 1, 2), 101, 1, 0.2)
        self.assertEqual(row.outliers, 0)
        self.assertLessEqual(row.outliers, row.outlier_upper_bound + 1e-9)

    def test_local_sparse_model_is_exact_and_locally_admissible(self) -> None:
        row = local_sparse_model(10007, 101)
        self.assertAlmostEqual(abs(row.selected_sum), row.geometric_modulus, places=8)
        self.assertEqual(len(set(value % row.q for value in row.values)), row.size)
        self.assertTrue(all(value % 12 == 1 for value in row.values))
        self.assertTrue(all(math.gcd(value * (value + 4), 6) == 1 for value in row.values))
        self.assertGreater(row.geometric_modulus, 0.99 * row.size)


if __name__ == "__main__":
    unittest.main()
