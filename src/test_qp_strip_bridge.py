import unittest

from qp_strip_bridge import (
    QP_FIXED_SLICE_KAPPA_MAX,
    centered_continuum_derivative,
    centered_continuum_term,
    fejer_continuum_limit,
    fejer_exact_minimum_frequency,
    fejer_nonzero_cosine,
    fejer_nonzero_nodes_weights,
    matching_zero_mellin_residue,
    pole_mellin_residue,
    positive_coefficient_factor,
    positive_factor_dirichlet_coefficient,
    positive_factor_full_logderivative_coefficient,
    positive_factor_zero_ordinate,
    strip_to_qp_ledger,
    support_factor_logderivative_coefficient,
    support_preserving_factor,
    transferred_turan_strip_width,
)


class QPStripBridgeTests(unittest.TestCase):
    def test_strip_width_above_kappa_closes_fixed_slice(self) -> None:
        delta = 0.02
        c = (delta + QP_FIXED_SLICE_KAPPA_MAX) / 2.0
        ledger = strip_to_qp_ledger(delta, c)
        self.assertTrue(ledger.closes)
        self.assertGreater(c, QP_FIXED_SLICE_KAPPA_MAX)
        self.assertGreater(ledger.contour_reserve, c)

    def test_mellin_decay_handles_lower_aperture(self) -> None:
        ledger = strip_to_qp_ledger(0.03, 0.02)
        self.assertLessEqual(
            ledger.pole_term_exponent, 1.0 - ledger.contour_reserve
        )

    def test_centered_continuum_derivative(self) -> None:
        x = 17.0
        t = 3.25
        step = 1.0e-5
        numerical = (
            centered_continuum_term(x + step, t)
            - centered_continuum_term(x - step, t)
        ) / (2.0 * step)
        self.assertAlmostEqual(numerical, centered_continuum_derivative(x, t), places=8)

    def test_pole_residues_cancel_exactly(self) -> None:
        t = 12.5
        for sign in (-1, 1):
            prime_series_over_s = pole_mellin_residue(t, sign)
            continuum_mellin = pole_mellin_residue(t, sign)
            self.assertEqual(prime_series_over_s, continuum_mellin)

    def test_matching_zero_residue_is_negative(self) -> None:
        self.assertAlmostEqual(matching_zero_mellin_residue(0.8, 2), -2.5)

    def test_support_factor_has_prescribed_conjugate_zeros(self) -> None:
        beta = 0.91
        ordinate = 37.0
        self.assertAlmostEqual(
            abs(support_preserving_factor(beta + 1j * ordinate, beta, ordinate)),
            0.0,
            places=12,
        )
        self.assertAlmostEqual(
            abs(support_preserving_factor(beta - 1j * ordinate, beta, ordinate)),
            0.0,
            places=12,
        )

    def test_support_factor_has_real_conjugate_symmetry(self) -> None:
        beta = 0.87
        ordinate = 9.0
        s = 1.2 + 4.0j
        left = support_preserving_factor(s.conjugate(), beta, ordinate)
        right = support_preserving_factor(s, beta, ordinate).conjugate()
        self.assertAlmostEqual(left.real, right.real, places=13)
        self.assertAlmostEqual(left.imag, right.imag, places=13)

    def test_added_logderivative_coefficients_are_real_and_prime_power_only(self) -> None:
        value = support_factor_logderivative_coefficient(3, 0.9, 7.0)
        self.assertIsInstance(value, float)

    def test_positive_dirichlet_factor_inserts_high_zeros(self) -> None:
        beta = 0.93
        ordinate = positive_factor_zero_ordinate(100, prime=2)
        self.assertAlmostEqual(
            abs(positive_coefficient_factor(beta + 1j * ordinate, beta)),
            0.0,
            places=11,
        )

    def test_positive_factor_preserves_support_and_positive_coefficients(self) -> None:
        beta = 0.8
        for integer in range(1, 30):
            self.assertGreater(
                positive_factor_dirichlet_coefficient(integer, beta), 0.0
            )
        for power in range(1, 12):
            self.assertNotEqual(
                positive_factor_full_logderivative_coefficient(power, beta),
                0.0,
            )

    def test_nonzero_fejer_weights_are_a_probability(self) -> None:
        nodes, weights = fejer_nonzero_nodes_weights(41, 0.2)
        self.assertEqual(len(nodes), 40)
        self.assertTrue(all(0.0 < node <= 0.2 for node in nodes))
        self.assertTrue(all(weight > 0.0 for weight in weights))
        self.assertAlmostEqual(sum(weights), 1.0, places=14)

    def test_fejer_floor_is_exact(self) -> None:
        order = 101
        width = 0.2
        frequency = fejer_exact_minimum_frequency(order, width, zero_index=37)
        self.assertAlmostEqual(
            fejer_nonzero_cosine(frequency, order, width),
            -1.0 / (order - 1),
            places=13,
        )
        for multiplier in (0.0, 0.3, 1.0, 7.0, 21.25):
            self.assertGreaterEqual(
                fejer_nonzero_cosine(multiplier * frequency, order, width)
                + 1.0 / (order - 1),
                -1.0e-13,
            )

    def test_coherent_fejer_certificates_do_not_decay_at_fixed_frequency(self) -> None:
        width = 0.2
        frequency = 1.0
        expected = fejer_continuum_limit(frequency, width)
        self.assertGreater(expected, 0.99)
        self.assertAlmostEqual(
            fejer_nonzero_cosine(frequency, 10001, width),
            expected,
            places=4,
        )

    def test_exact_conditional_turan_width(self) -> None:
        self.assertAlmostEqual(
            transferred_turan_strip_width(0.019, 1.0),
            0.0001572516,
            places=13,
        )


if __name__ == "__main__":
    unittest.main()
