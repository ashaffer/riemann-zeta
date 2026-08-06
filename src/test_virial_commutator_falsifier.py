import unittest

import numpy as np

from virial_commutator_falsifier import (
    adapted_virial_commutator,
    diagnose_matrix,
    legendre_position_matrix,
)


class VirialCommutatorTests(unittest.TestCase):
    def test_position_matrix_is_symmetric_and_parity_switching(self) -> None:
        position = legendre_position_matrix(3.27, 8)
        np.testing.assert_allclose(position, position.T)
        for row in range(8):
            for column in range(8):
                if (row + column) % 2 == 0:
                    self.assertEqual(position[row, column], 0.0)

    def test_finite_commutator_has_zero_trace_and_eigenstate_diagonal(self) -> None:
        weil = np.array(
            [[2.0, 0.3, 0.0], [0.3, 1.0, -0.2], [0.0, -0.2, 0.5]]
        )
        position = legendre_position_matrix(1.75, 3)
        _, _, commutator = adapted_virial_commutator(weil, position)
        self.assertAlmostEqual(float(np.trace(commutator).real), 0.0, places=13)
        _, eigenvectors = np.linalg.eigh(weil)
        diagonal = np.diag(eigenvectors.T @ commutator @ eigenvectors)
        np.testing.assert_allclose(diagonal, 0.0, atol=1e-13)

    def test_nonpositive_matrix_marks_whitening_undefined(self) -> None:
        result = diagnose_matrix(1.75, np.diag([-1.0, 2.0]))
        self.assertTrue(np.isinf(result.kappa_critical))

    def test_positive_whitening_finds_repair_threshold(self) -> None:
        weil = np.array(
            [[2.0, 0.3, 0.0], [0.3, 1.0, -0.2], [0.0, -0.2, 0.5]]
        )
        result = diagnose_matrix(1.75, weil)
        position = legendre_position_matrix(1.75, 3)
        _, _, commutator = adapted_virial_commutator(weil, position)
        repaired = commutator + result.kappa_critical * weil
        self.assertGreaterEqual(np.linalg.eigvalsh(repaired)[0], -1e-12)
        if result.kappa_critical > 1e-6:
            under_repaired = (
                commutator + (result.kappa_critical - 1e-6) * weil
            )
            self.assertLess(np.linalg.eigvalsh(under_repaired)[0], 0.0)

    def test_two_state_leakage_has_compensating_sign(self) -> None:
        operator = np.array([[0.0, 1.0], [1.0, 0.0]])
        generator = 0.5 * np.array([[0.0, -1.0], [1.0, 0.0]])
        commutator = operator @ generator - generator @ operator
        np.testing.assert_allclose(commutator, np.diag([1.0, -1.0]))


if __name__ == "__main__":
    unittest.main()
