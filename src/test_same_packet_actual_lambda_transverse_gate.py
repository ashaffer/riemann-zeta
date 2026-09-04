#!/usr/bin/env python3

import math
import unittest

import numpy as np

from high_height_carrier_slice import prime_matrix_sign
from same_packet_actual_lambda_transverse_gate import (
    actual_lambda_cross_coefficient,
    actual_lambda_schur_vector,
    gram_energy,
    isolation_log_ratio,
    transverse_data,
    two_channel_best,
)
from signed_garding_failfast import prime_powers


class ActualLambdaTransverseGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.length = math.log(32.0)
        self.tau = 48.0 + (2.0 * math.pi / self.length) * np.arange(-2, 3)
        logs, weights = prime_powers(32)
        active = logs <= self.length + 1e-13
        self.logs = logs[active]
        self.weights = weights[active]
        rng = np.random.default_rng(20260813)
        synthesis = rng.normal(size=(self.tau.size, self.tau.size - 1))
        self.inclusion = np.linalg.qr(synthesis)[0]
        raw = rng.normal(size=(self.tau.size, self.tau.size))
        self.background = (raw + raw.T) / 2.0
        quotient_dimension = self.inclusion.shape[1]
        e = rng.normal(size=quotient_dimension) + 1j * rng.normal(
            size=quotient_dimension
        )
        self.e = e / np.linalg.norm(e)
        v = rng.normal(size=quotient_dimension) + 1j * rng.normal(
            size=quotient_dimension
        )
        v -= self.e * np.vdot(self.e, v)
        self.v = v / np.linalg.norm(v)

    def test_exact_actual_lambda_cross_coefficient(self) -> None:
        prime = prime_matrix_sign(
            self.tau, self.length, self.logs, self.weights
        )
        reserve = (
            self.inclusion.conj().T
            @ (self.background - prime)
            @ self.inclusion
            / (self.length * self.length)
        )
        direct = np.vdot(self.e, reserve @ self.v)
        expanded = actual_lambda_cross_coefficient(
            self.tau,
            self.length,
            self.logs,
            self.weights,
            self.inclusion,
            self.e,
            self.v,
            self.background,
        )
        self.assertAlmostEqual(direct.real, expanded.real, places=11)
        self.assertAlmostEqual(direct.imag, expanded.imag, places=11)

    def test_vector_and_full_gram_expansions(self) -> None:
        total, background, columns = actual_lambda_schur_vector(
            self.tau,
            self.length,
            self.logs,
            self.weights,
            self.inclusion,
            self.e,
            self.background,
        )
        self.assertAlmostEqual(
            float(np.vdot(total, total).real),
            gram_energy(background, columns),
            places=10,
        )

    def test_transverse_invariants_ignore_aligned_carrier(self) -> None:
        rng = np.random.default_rng(17)
        raw = rng.normal(size=(5, 5)) + 1j * rng.normal(size=(5, 5))
        reserve = (raw + raw.conj().T) / 2.0
        e = rng.normal(size=5) + 1j * rng.normal(size=5)
        e /= np.linalg.norm(e)
        first = transverse_data(reserve, e)
        second = transverse_data(reserve + 7.0 * np.outer(e, e.conj()), e)
        self.assertAlmostEqual(first.schur_residual, second.schur_residual, places=11)
        self.assertAlmostEqual(
            first.transverse_lambda_max,
            second.transverse_lambda_max,
            places=11,
        )

    def test_isolation_gap_beats_every_fixed_log_power(self) -> None:
        values = [
            isolation_log_ratio(log_x, 0.3234, 0.3034, 8.0)
            for log_x in (1e4, 2e4, 4e4)
        ]
        self.assertGreater(values[0], values[1])
        self.assertGreater(values[1], values[2])
        self.assertLess(values[-1], -100.0)

    def test_phase_is_exact(self) -> None:
        z = 3.0 + 4.0j
        value, phase = two_channel_best(0.4, -2.0, 1.0, z)
        grid = np.linspace(-math.pi, math.pi, 100001)
        samples = (
            0.4 * -2.0
            + 0.6 * 1.0
            + 2.0 * math.sqrt(0.24) * np.real(np.exp(1j * grid) * z)
        )
        self.assertAlmostEqual(value, float(np.max(samples)), places=8)
        self.assertAlmostEqual(
            np.real(np.exp(1j * phase) * z), abs(z), places=12
        )


if __name__ == "__main__":
    unittest.main()
