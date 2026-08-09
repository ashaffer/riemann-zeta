#!/usr/bin/env python3

import unittest

from luroth_global_alias_probe import (
    defect_carrier_partial,
    dual_defect,
    dual_finite_part,
    exact_alias_prefactor,
    exact_dual_value,
    scaled_dual_alias,
    stationary_prefactor,
)


class LurothGlobalAliasProbeTests(unittest.TestCase):
    def test_dual_defects_telescope_to_finite_part(self) -> None:
        for cutoff in (1, 2, 17, 101):
            s = 0.83 + 9.0j
            self.assertLess(
                abs(defect_carrier_partial(cutoff, s) - dual_finite_part(cutoff, s)),
                2e-13,
            )

    def test_euler_corrected_finite_part_approaches_dual_zeta(self) -> None:
        cutoff = 200_000
        s = 0.7 + 7.0j
        observed = dual_finite_part(cutoff, s) - 0.5 * cutoff ** (s - 1)
        self.assertLess(abs(observed - exact_dual_value(s)), 3e-6)

    def test_exact_gamma_prefactor_matches_stationary_phase(self) -> None:
        s = 0.9 + 10_000.0j
        exact = exact_alias_prefactor(s)
        predicted = stationary_prefactor(s)
        self.assertLess(abs(exact - predicted) / abs(exact), 4e-4)

    def test_dual_defects_have_real_negative_sign(self) -> None:
        for s in (0.1, 0.5, 0.9):
            for index in (1, 2, 10, 100):
                value = dual_defect(index, s)
                self.assertAlmostEqual(value.imag, 0.0)
                self.assertLess(value.real, 0.0)

    def test_dual_alias_has_unit_response(self) -> None:
        observed = scaled_dual_alias(index=2, sigma=0.9, height=100_000.0)
        self.assertLess(abs(observed - 1), 2e-3)

    def test_global_alias_identity(self) -> None:
        import mpmath as mp

        s = 0.77 + 13.0j
        left = (s - 1) * complex(mp.zeta(s)) / (s * (s + 1))
        right = exact_alias_prefactor(s) * exact_dual_value(s)
        self.assertLess(abs(left - right), 2e-13)


if __name__ == "__main__":
    unittest.main()
