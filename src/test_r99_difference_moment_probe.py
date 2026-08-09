import unittest

import mpmath as mp

from r99_difference_moment_probe import (
    LOG_TWO,
    alias_laplace,
    alias_weight,
    cubic_gap_coefficients,
    difference_localizer_bound,
    difference_moment,
    evaluate_polynomial,
    laplace_polynomial,
    normalized_first_moment,
    separator_coefficients,
    smallest_localizing_rayleigh,
    stationary_phase_envelope,
)


class DifferenceMomentProbeTests(unittest.TestCase):
    def test_closed_moment_matches_quadrature(self) -> None:
        mp.mp.dps = 50
        observed = difference_moment(1.3, 0.4, 4, vanishing_order=1)
        expected = mp.quad(
            lambda x: x**5 * mp.exp(-1.3 * x) * (1 - mp.exp(-0.4 * x)),
            [0, mp.inf],
        )
        self.assertLess(abs(observed - expected), mp.mpf("1e-40"))

    def test_degree_one_support_obstruction(self) -> None:
        mean = normalized_first_moment(60, 1)
        self.assertAlmostEqual(float(mean), 1 / 60 + 1 / 61, places=14)
        self.assertLess(mean, LOG_TWO)

    def test_localizer_crosses_the_prime_log_floor(self) -> None:
        values = [
            smallest_localizing_rayleigh(1, 1, degree).rayleigh
            for degree in range(7)
        ]
        self.assertTrue(all(right < left for left, right in zip(values, values[1:])))
        self.assertGreater(values[5], LOG_TWO)
        self.assertLess(values[6], LOG_TWO)

    def test_comparison_bound_is_honest_when_finite(self) -> None:
        degree = 40
        observed = smallest_localizing_rayleigh(
            1, 1, degree, dps=150
        ).rayleigh
        bound = difference_localizer_bound(1, 1, degree)
        self.assertTrue(mp.isfinite(bound))
        self.assertLess(observed, bound)
        self.assertLess(bound, LOG_TWO)

    def test_separator_is_prime_support_positive_and_reverses_order(self) -> None:
        certificate = smallest_localizing_rayleigh(1, 1, 6)
        coefficients = separator_coefficients(certificate)
        self.assertEqual(coefficients[0], 0)
        for integer in (2, 3, 4, 5, 7, 8, 9, 11, 16, 25):
            self.assertGreaterEqual(
                evaluate_polynomial(coefficients, mp.log(integer)),
                -mp.mpf("1e-55"),
            )
        pole = mp.re(laplace_polynomial(coefficients, 1))
        target = mp.re(laplace_polynomial(coefficients, 2))
        self.assertLess(pole, target)
        # This localizing separator alone has the wrong target sign; R99's
        # two-bump theorem is needed for a useful positive target response.
        self.assertLess(target, 0)

    def test_r90_cubic_has_positive_target_and_order_reversal(self) -> None:
        coefficients = cubic_gap_coefficients(mp.mpf(1) / 30, mp.mpf(13) / 20)
        pole = mp.re(laplace_polynomial(coefficients, 60))
        target = mp.re(laplace_polynomial(coefficients, 61))
        self.assertGreater(pole, 0)
        self.assertGreater(target, pole)

    def test_alias_is_zero_on_integer_logs_but_has_nonzero_transform(self) -> None:
        mp.mp.dps = 60
        for integer in (2, 3, 4, 5, 8, 9, 25, 101):
            self.assertLess(abs(alias_weight(mp.log(integer))), mp.mpf("1e-55"))
        self.assertGreater(abs(alias_laplace(3)), mp.mpf("1e-4"))

    def test_alias_stationary_phase_envelope(self) -> None:
        mp.mp.dps = 50
        height = mp.mpf(100)
        for sigma in (mp.mpf("0.25"), mp.mpf("2")):
            observed = abs(alias_laplace(sigma + 1j * height))
            predicted = stationary_phase_envelope(sigma, height)
            self.assertLess(abs(observed / predicted - 1), mp.mpf("0.08"))

    def test_input_validation(self) -> None:
        with self.assertRaises(ValueError):
            difference_moment(0, 1, 2)
        with self.assertRaises(ValueError):
            difference_moment(1, -1, 2)
        with self.assertRaises(ValueError):
            difference_moment(1, 1, True)
        with self.assertRaises(ValueError):
            alias_laplace(1j)
        with self.assertRaises(ValueError):
            cubic_gap_coefficients(0.5, 0.4)


if __name__ == "__main__":
    unittest.main()
