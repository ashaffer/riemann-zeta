from __future__ import annotations

import unittest

from fgf4_selected_q_dispersion import (
    buchstab_bilinear_audit,
    buchstab_sector_cauchy_audit,
    endpoint_parity_countermodel,
    selected_dispersion_audit,
)


class SelectedQDispersionTests(unittest.TestCase):
    def assertComplexClose(
        self, left: complex, right: complex, places: int = 7
    ) -> None:
        self.assertAlmostEqual(left.real, right.real, places=places)
        self.assertAlmostEqual(left.imag, right.imag, places=places)

    def test_selected_twist_and_dispersion_identities(self) -> None:
        row = selected_dispersion_audit(100003, 101005, 1003)
        self.assertGreater(row.pair_count, 0)
        self.assertComplexClose(row.twisted_sum, -1j * row.additive_sum)
        self.assertAlmostEqual(
            row.selected_square_from_differences.real,
            abs(row.additive_sum) ** 2,
            places=7,
        )
        self.assertAlmostEqual(
            row.selected_square_from_differences.imag, 0.0, places=7
        )
        self.assertEqual(row.centered_variance, row.centered_variance_from_q_shifts)
        self.assertAlmostEqual(
            row.parseval_second_lhs, row.parseval_second_rhs, places=6
        )
        self.assertAlmostEqual(
            row.parseval_fourth_lhs, row.parseval_fourth_rhs, places=4
        )

    def test_endpoint_has_only_literal_diagonal(self) -> None:
        # The interval diameter is strictly below q, so two distinct endpoints
        # cannot occupy the same residue modulo q.
        row = selected_dispersion_audit(100003, 101005, 1003)
        self.assertEqual(row.positive_q_shift_pairs, 0)
        expected = row.pair_count - row.pair_count * row.pair_count / row.modulus
        self.assertAlmostEqual(float(row.centered_variance), expected)

    def test_exact_buchstab_bilinearization(self) -> None:
        row = buchstab_bilinear_audit(10003, 14003, 83, 7)
        self.assertGreater(row.subtraction_rows, 0)
        self.assertComplexClose(row.direct, row.rough_term - row.subtraction_term)
        self.assertComplexClose(row.subtraction_term, row.transformed_bilinear_term)

    def test_buchstab_cauchy_zero_mode(self) -> None:
        row = buchstab_sector_cauchy_audit(10003, 40003, 83, 7, 7, 200)
        self.assertGreater(row.outer_rows, 0)
        self.assertGreater(row.diagonal_zero_mode, 0)
        self.assertComplexClose(
            complex(row.cauchy_energy), row.expanded_energy, places=6
        )
        self.assertLessEqual(
            abs(row.direct_form) ** 2,
            row.outer_rows * row.cauchy_energy + 1e-7,
        )

    def test_locally_admissible_endpoint_countermodel(self) -> None:
        row = endpoint_parity_countermodel(100003, 1003)
        self.assertGreater(row.support_size, 0)
        self.assertLess(row.arc_width_radians, 3.141592653589793 / 2)
        self.assertGreaterEqual(
            abs(row.twisted_sum) + 1e-9, row.geometric_lower_bound
        )
        self.assertGreater(row.geometric_lower_bound, row.support_size / 2)


if __name__ == "__main__":
    unittest.main()
