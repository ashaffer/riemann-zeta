import math
import unittest

from qp_signed_kernel_capacity_gate import (
    audit_signed_kernel,
    chebyshev_log_resonant_bound,
    chebyshev_spike_log,
    chebyshev_theta,
    required_chebyshev_order,
    turan_vertical_envelope_floor,
)


class SignedKernelCapacityGateTests(unittest.TestCase):
    def test_exterior_distance_identity(self) -> None:
        for a0, a1 in ((0.01, 0.02), (0.001, 0.1), (0.2, 0.5)):
            xi = (a1 * a1 + a0 * a0) / (a1 * a1 - a0 * a0)
            self.assertAlmostEqual(chebyshev_theta(a0, a1), math.acosh(xi))

    def test_required_order_is_minimal(self) -> None:
        values = dict(log_y=1000.0, target_power=0.019, a0=0.001, a1=0.019, width=0.2)
        order = required_chebyshev_order(**values)
        target = -values["target_power"] * values["log_y"]
        self.assertLessEqual(
            chebyshev_log_resonant_bound(
                order, values["a0"], values["a1"], values["width"]
            ),
            target,
        )
        self.assertGreater(
            chebyshev_log_resonant_bound(
                order - 1, values["a0"], values["a1"], values["width"]
            ),
            target,
        )

    def test_spike_dwarfs_requested_gain(self) -> None:
        audit = audit_signed_kernel(
            log_y=1000.0,
            target_power=0.019,
            a0=0.001,
            a1=0.019,
        )
        self.assertLessEqual(audit.resonant_log_bound, -19.0)
        self.assertGreater(audit.spike_log_value, 1000.0)

    def test_spike_formula_is_finite_and_increases(self) -> None:
        low = chebyshev_spike_log(10, 0.001, 0.019, 0.2)
        high = chebyshev_spike_log(20, 0.001, 0.019, 0.2)
        self.assertTrue(math.isfinite(low))
        self.assertGreater(high, low)

    def test_turan_floor(self) -> None:
        self.assertEqual(turan_vertical_envelope_floor(0.2), 10.0)
        self.assertEqual(turan_vertical_envelope_floor(0.2, 3.0), 30.0)

    def test_input_validation(self) -> None:
        with self.assertRaises(ValueError):
            chebyshev_theta(0.1, 0.1)
        with self.assertRaises(ValueError):
            chebyshev_spike_log(0, 0.01, 0.02, 0.2)


if __name__ == "__main__":
    unittest.main()

