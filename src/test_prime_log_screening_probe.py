import math
import unittest

from prime_log_screening_probe import (
    Atom,
    analyze_block,
    decompose_energy,
    pole_coefficient,
)


class PrimeLogScreeningProbeTests(unittest.TestCase):
    def test_pole_coefficient_is_triangle_integral(self) -> None:
        ell = 0.8
        steps = 200_000
        spacing = 2.0 * ell / steps
        midpoint_sum = 0.0
        for index in range(steps):
            value = -ell + (index + 0.5) * spacing
            midpoint_sum += (1.0 - abs(value) / ell) * math.exp(value / 2.0)
        self.assertAlmostEqual(
            spacing * midpoint_sum, pole_coefficient(ell), places=10
        )

    def test_one_atom_full_hat_has_known_diagonal(self) -> None:
        atom = Atom(3.0, 2.5)
        ell = 0.7
        result = decompose_energy([atom], 3.0 - ell, 3.0 + ell, ell)
        self.assertAlmostEqual(
            result.atom_diagonal, atom.weight**2 * 2.0 * ell / 3.0, places=12
        )
        self.assertAlmostEqual(result.atom_off_diagonal, 0.0, places=12)

    def test_atom_off_diagonal_is_nonnegative(self) -> None:
        atoms = [Atom(2.0, 1.0), Atom(2.2, 0.7), Atom(3.0, 0.4)]
        result = decompose_energy(atoms, 1.0, 4.0, 0.8)
        self.assertGreaterEqual(result.atom_off_diagonal, -1.0e-12)

    def test_core_boundary_additivity(self) -> None:
        result = analyze_block(4.0, 5.0, 0.2)
        for name in (
            "atom_diagonal",
            "atom_off_diagonal",
            "atom_continuum",
            "continuum_square",
            "energy",
        ):
            self.assertAlmostEqual(
                getattr(result.total, name),
                getattr(result.core, name) + getattr(result.boundary, name),
                places=9,
            )


if __name__ == "__main__":
    unittest.main()
