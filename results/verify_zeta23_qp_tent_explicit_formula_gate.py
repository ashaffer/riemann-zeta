#!/usr/bin/env python3
"""Independent replay for the tent/explicit-formula QP exponent ledger."""

from __future__ import annotations

from fractions import Fraction
import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import qp_tent_explicit_formula_gate as gate


def main() -> None:
    width = 0.2
    samples = (0.0, 0.5, 7.0, 31.0, 101.0)
    transform_error = max(
        abs(gate.tent_laplace(-1j * t, width).real - gate.tent_fourier(t, width))
        + abs(gate.tent_laplace(-1j * t, width).imag)
        for t in samples
    )
    assert transform_error < 1e-12
    aperture = Fraction(50, 33)
    target = Fraction(19, 1000)
    grid_exponent = float(aperture + target)
    assert math.isclose(
        grid_exponent, gate.required_positive_grid_exponent(float(target))
    )
    assert gate.KAPPA_MAX < float(target)
    assert not gate.strip_supplies_power(float(target), float(target))
    assert gate.strip_supplies_power(0.020, float(target))
    assert math.isclose(
        gate.convex_mixture_error([0.2, 0.05], [0.25, 0.75]), 0.0875
    )
    assert gate.cosine_product_frequencies(0.2, 0.2) == (0.0, 0.4)
    assert gate.nonlinear_power_escapes_finite_support(0.2, 2)
    assert gate.even_positive_kernel_ratio_lower_bound(0.4, 0.2) == 1.0
    error = 1e-6
    assert math.isclose(gate.promoted_depth_upper_bound(error), error)
    print(
        json.dumps(
            {
                "schema": "verify-zeta23-qp-tent-explicit-formula-gate-v1",
                "status": "PASS",
                "maximum_transform_replay_error": transform_error,
                "aperture_exponent": str(aperture),
                "target_exponent": str(target),
                "safe_grid_constraint_exponent": grid_exponent,
                "strict_strip_width_needed_for_target": True,
                "unconditional_fixed_power_claimed": False,
                "convex_mixing_multiplies_errors": False,
                "nonlinear_amplifier_preserves_actual_frequency_pool": False,
                "positive_definite_kernel_damps_resonant_zero": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
