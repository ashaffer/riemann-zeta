import unittest

import mpmath as mp

from suzuki_livsic_calibration import (
    FiniteLivsicModel,
    ShiftCalibration,
    XiLivsicTarget,
    bisect_sign_change,
    calibrate_resolvent_ratio,
    completed_xi,
    exponential_legendre_coefficients,
    reflected_coefficients,
    parity_resolvent_energies,
    resolvent_ratio,
    xi_log_derivative,
)


class SuzukiLivsicCalibrationTest(unittest.TestCase):
    def setUp(self) -> None:
        mp.mp.dps = 60

    def test_xi_normalization_and_log_derivative_constants(self) -> None:
        point = mp.mpf("1.5")
        self.assertAlmostEqual(
            float(mp.re(completed_xi(point))),
            0.5087310387263239580256712366721122,
            places=15,
        )
        target = XiLivsicTarget.compute(dps=60)
        self.assertAlmostEqual(
            float(target.ell),
            0.0461359280604625753594660065422720,
            places=15,
        )
        self.assertAlmostEqual(
            float(target.rho),
            0.996801952032400903528896704787758,
            places=15,
        )
        self.assertLess(
            abs(xi_log_derivative(point) - mp.diff(completed_xi, point) / completed_xi(point)),
            mp.mpf("1e-50"),
        )

    def test_target_zero_and_derivative_sign_at_i(self) -> None:
        target = XiLivsicTarget.compute(dps=60)
        self.assertLess(abs(target.characteristic(mp.j)), mp.mpf("1e-50"))
        numerical = mp.diff(target.characteristic, mp.j)
        self.assertLess(abs(numerical - mp.j * target.rho / 2), mp.mpf("1e-45"))
        self.assertGreater(mp.im(numerical), 0)
        self.assertLess(abs(target.characteristic(0) - 1), mp.mpf("1e-50"))

    def test_high_precision_bisection_on_synthetic_root(self) -> None:
        root = bisect_sign_change(
            lambda value: value**3 - 2,
            mp.mpf(1),
            mp.mpf(2),
            mp.mpf("1e-50"),
        )
        self.assertLess(abs(root - mp.root(2, 3)), mp.mpf("2e-50"))

    def test_synthetic_resolvent_ratio_calibrates_known_shift(self) -> None:
        matrix = mp.matrix([[1, 0], [0, 3]])
        p = mp.matrix([2, 1])
        target = mp.mpf(11) / 13
        self.assertLess(abs(resolvent_ratio(matrix, p, 0) - target), mp.mpf("1e-55"))
        calibration = calibrate_resolvent_ratio(matrix, p, target, dps=60)
        self.assertLess(abs(calibration.sigma), mp.mpf("1e-28"))
        self.assertLess(calibration.rho_residual, mp.mpf("1e-28"))

    def test_exponential_projection_reflection_signs(self) -> None:
        radius = mp.mpf("0.6")
        dimension = 6
        p = exponential_legendre_coefficients(radius, dimension)
        p_minus = reflected_coefficients(p)
        matrix = mp.eye(dimension)
        even_energy, odd_energy = parity_resolvent_energies(matrix, p, 0)
        rho = (even_energy - odd_energy) / (even_energy + odd_energy)
        calibration = ShiftCalibration(
            spectral_floor=mp.mpf(1),
            spectral_ceiling=mp.mpf(1),
            sigma=mp.mpf(0),
            floor_gap=mp.mpf(1),
            condition_estimate=mp.mpf(1),
            rho_target=rho,
            rho_model=rho,
            rho_residual=mp.mpf(0),
            even_energy=even_energy,
            odd_energy=odd_energy,
        )
        model = FiniteLivsicModel(matrix, radius, calibration, dps=60)
        q_plus = model.probe_coefficients(-mp.j)
        q_minus = model.probe_coefficients(mp.j)
        for degree in range(dimension):
            self.assertLess(abs(q_plus[degree] - p[degree]), mp.mpf("1e-50"))
            self.assertLess(
                abs(q_minus[degree] - p_minus[degree]), mp.mpf("1e-50")
            )
        numerical_derivative = mp.diff(model.characteristic, mp.j)
        self.assertLess(
            abs(numerical_derivative - mp.j * rho / 2), mp.mpf("1e-45")
        )
        self.assertGreater(mp.im(numerical_derivative), 0)


if __name__ == "__main__":
    unittest.main()
