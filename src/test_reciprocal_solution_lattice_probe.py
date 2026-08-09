#!/usr/bin/env python3

import cmath
import math
import unittest

from reciprocal_solution_lattice_probe import (
    axis_indices,
    lattice_solution,
    particular_solution,
    reciprocal_residue,
)


class ReciprocalSolutionLatticeProbeTests(unittest.TestCase):
    def test_affine_parametrization_solves_the_mode_equation(self) -> None:
        theta, m, n = 13, 7, 11
        for ell in range(-10, 11):
            pair = lattice_solution(theta, m, n, ell)
            self.assertEqual(pair.a * n - pair.b * m, theta)

    def test_poisson_shift_is_the_reciprocal_phase(self) -> None:
        theta, m, n, k = 13, 7, 11, 5
        base = particular_solution(theta, m, n)
        direct = cmath.exp(2.0j * math.pi * k * base.a / m)
        residue = reciprocal_residue(theta, m, n, k)
        reciprocal = cmath.exp(2.0j * math.pi * residue / m)
        self.assertLess(abs(direct - reciprocal), 1.0e-12)

    def test_punctured_axes_have_the_expected_divisibility(self) -> None:
        # m divides theta, hence the lattice contains an a=0 point only.
        theta, m, n = 14, 7, 11
        ell_a, ell_b = axis_indices(theta, m, n)
        self.assertIsNotNone(ell_a)
        self.assertIsNone(ell_b)
        pair = lattice_solution(theta, m, n, ell_a or 0)
        self.assertEqual(pair.a, 0)

        # Both divisibilities hold, so both punctures occur.
        theta = m * n
        ell_a, ell_b = axis_indices(theta, m, n)
        self.assertIsNotNone(ell_a)
        self.assertIsNotNone(ell_b)
        self.assertEqual(lattice_solution(theta, m, n, ell_a or 0).a, 0)
        self.assertEqual(lattice_solution(theta, m, n, ell_b or 0).b, 0)

    def test_rejects_noncoprime_moduli(self) -> None:
        with self.assertRaises(ValueError):
            particular_solution(1, 6, 9)


if __name__ == "__main__":
    unittest.main()
