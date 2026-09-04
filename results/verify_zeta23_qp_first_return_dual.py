#!/usr/bin/env python3
"""Independent replay of the QP first-return dual exponent and finite algebra."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_first_return_dual import (  # noqa: E402
    carrier_loss_exponent,
    cosine_atoms,
    exponent_ledger,
    projected_gram_correction,
    projection_leverage,
    remote_incommensurate_fixture,
)


ledger = exponent_ledger()
assert math.isclose(ledger.kappa_min, 0.018030323424358778, abs_tol=2e-15)
assert math.isclose(ledger.kappa_max, 0.018746369714728765, abs_tol=2e-15)
assert carrier_loss_exponent(0.49) < carrier_loss_exponent(0.5) < 0.019
cached_reoptimized_kappa_max = carrier_loss_exponent(0.5, 0.665)
legal_d_kappa_supremum = carrier_loss_exponent(0.5, 2.0 / 3.0)
assert math.isclose(cached_reoptimized_kappa_max, 0.019740482582942102, abs_tol=2e-15)
assert math.isclose(legal_d_kappa_supremum, 0.020075148161991937, abs_tol=2e-15)
assert 0.019 < cached_reoptimized_kappa_max < legal_d_kappa_supremum

beta = Fraction(19, 125)
theta = Fraction(161, 1000)
target = Fraction(19, 1000)
aperture = Fraction(50, 33)
assert (45 * theta - 6) / 65 - target == Fraction(1, 6500)
assert 2 - aperture - 2 * beta - theta - target == Fraction(7, 8250)
assert 1 - aperture / 2 - beta - target == Fraction(2357, 33000)

# Replay the complete rational Table-1 envelope, not just its binding branch.
gap_audit_path = ROOT / "results" / "verify_zeta23_high_denominator_gap_tail.py"
gap_audit_spec = importlib.util.spec_from_file_location("gap_tail_audit", gap_audit_path)
assert gap_audit_spec is not None and gap_audit_spec.loader is not None
gap_audit = importlib.util.module_from_spec(gap_audit_spec)
gap_audit_spec.loader.exec_module(gap_audit)
table_minimum = gap_audit.audit_theta(theta, (45 * theta - 6) / 65)
assert table_minimum == (Fraction(249, 13000), "Guth--Maynard", Fraction(7, 10))

nodes = np.asarray([0.07, 0.13, 0.21, 0.29, 0.37])
centers = cosine_atoms(nodes, [19.0, 37.0, 53.0])
base = -np.ones(len(nodes)) / len(nodes)
targets = np.asarray([0.01, -0.02, 0.03])
corrected = projected_gram_correction(base, centers, targets)
assert corrected.maximum_center_residual < 2e-12
assert abs(corrected.carrier_change) < 2e-12
queries = cosine_atoms(nodes, [19.0, 29.0, 37.0, 43.0, 53.0])
leverage = projection_leverage(centers, queries)
assert np.all(leverage >= -1e-11)
assert np.all(leverage <= 1.0 + 1e-10)
assert math.isclose(float(leverage[0]), 1.0, abs_tol=2e-11)
assert math.isclose(float(leverage[2]), 1.0, abs_tol=2e-11)
assert math.isclose(float(leverage[4]), 1.0, abs_tol=2e-11)

fixture = remote_incommensurate_fixture(node_count=6, harmonic_offset=9)
assert fixture.minimum_weight > 0.0
assert fixture.perturbed_depth > 0.49
assert fixture.interpolation_residual < 2e-12
assert fixture.first_frequency > 0.0
assert fixture.last_frequency > fixture.first_frequency

print(
    json.dumps(
        {
            "schema": "verify-zeta23-qp-first-return-dual-v1",
            "status": "PASS",
            "kappa_min": ledger.kappa_min,
            "kappa_max": ledger.kappa_max,
            "cached_d_0.665_kappa_max": cached_reoptimized_kappa_max,
            "legal_d_supremal_kappa_max": legal_d_kappa_supremum,
            "uniform_kill_target": ledger.proposed_kill,
            "full_cache_target_scope": "FAIL: .019 is fixed-d=.66 only",
            "auxiliary_margins": {
                "long_gap": ledger.long_gap_margin,
                "short_collar": ledger.short_collar_margin,
                "inverse_image": ledger.inverse_image_margin,
            },
            "gram_center_residual": corrected.maximum_center_residual,
            "maximum_projection_leverage": float(np.max(leverage)),
            "incommensurate_fixture_depth": fixture.perturbed_depth,
            "scope": (
                "finite identities and exponent arithmetic only; the missing "
                "actual-prime off-packet leverage/retained-tail theorem is not asserted"
            ),
        },
        indent=2,
        sort_keys=True,
    )
)
