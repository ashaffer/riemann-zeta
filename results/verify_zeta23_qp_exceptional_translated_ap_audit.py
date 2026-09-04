#!/usr/bin/env python3
"""Replay the exceptional translated-AP hostile-audit certificates."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_exceptional_translated_ap_audit import (  # noqa: E402
    all_remote_uniform_template,
    first_harmonic_template,
    generic_r0_exponential_term_lower,
    negative_packet_mass_lower,
    positive_harmonic_template,
    singular_r0_certificate,
    two_frequency_kronecker_return,
)


def main() -> None:
    first = [first_harmonic_template(degree) for degree in (2, 3, 5, 8)]
    translated = [
        all_remote_uniform_template(degree)
        for degree in (2, 3, 5, 8)
    ]
    singular = [singular_r0_certificate(delta) for delta in (1e-2, 1e-4, 1e-6)]
    recurrence = two_frequency_kronecker_return(20000)

    for item in first:
        assert item.minimum_probability_weight > 0.0
        assert item.normalized_depth > 0.45
        assert item.interpolation_residual < 1e-10
        assert abs(item.augmented_determinant) > 1e-8
    for item in translated:
        assert item.minimum_weight > 0.0
        assert item.solved_depth > 0.45
        assert item.interpolation_residual < 1e-10
        assert abs(item.augmented_determinant) > 1e-8
    assert singular[-1].directional_cost > 1000.0 * singular[0].directional_cost
    assert singular[-1].positive_depth < singular[0].positive_depth / 1000.0
    assert recurrence.circular_phase_error < 1e-4
    assert recurrence.minimum_weight > 0.0
    assert generic_r0_exponential_term_lower(20) == 2**20
    assert 0.0 < negative_packet_mass_lower(0.1) < 0.1

    print(
        json.dumps(
            {
                "schema": "verify-zeta23-qp-exceptional-translated-ap-audit-v1",
                "first_harmonic_templates": [asdict(item) for item in first],
                "translated_harmonic_templates": [asdict(item) for item in translated],
                "singular_r0": [asdict(item) for item in singular],
                "two_frequency_recurrence": asdict(recurrence),
                "verdict": (
                    "singular r0 cannot promote; positive determinant chambers "
                    "exist and recur, leaving only finite-aperture first return"
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
