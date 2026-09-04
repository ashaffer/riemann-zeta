#!/usr/bin/env python3

import unittest

from same_packet_transverse_reserve_probe import build_transverse_fixture


class SamePacketTransverseReserveProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = build_transverse_fixture(32.0, alpha=0.4, eta=0.5)

    def test_scope(self) -> None:
        self.assertFalse(self.fixture["candidate_is_asserted_zero"])
        self.assertIn("floating", self.fixture["scope"])

    def test_dimensions(self) -> None:
        self.assertGreaterEqual(self.fixture["transverse_dimension"], 1)
        self.assertGreater(self.fixture["K_selected"], 0)

    def test_linear_algebra_residuals(self) -> None:
        for value in self.fixture["checks"].values():
            self.assertLess(value, 1e-8)

    def test_channels_are_finite(self) -> None:
        self.assertGreaterEqual(len(self.fixture["channels"]), 1)
        for channel in self.fixture["channels"]:
            self.assertTrue(abs(channel["optimized_reserve_over_eta_K"]) < 1e12)


if __name__ == "__main__":
    unittest.main()
