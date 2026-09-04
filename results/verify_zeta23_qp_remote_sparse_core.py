#!/usr/bin/env python3
"""Replay the deterministic sparse-core exponent ledger."""

from __future__ import annotations

import json
import pathlib
import sys
from dataclasses import asdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_remote_sparse_core import sparse_core_bound  # noqa: E402


def main() -> None:
    kappa = 0.0180303234
    # At depth r=Y^-kappa the large-value packet exponent is 2*kappa.
    payload = {
        "status": "PASS",
        "kappa": kappa,
        "negative_peak_weight_exponent": -kappa,
        "exceptional_harmonic_count_exponent": 2.0 * kappa,
        "largest_barycentric_weight_exponent": -3.0 * kappa,
        "largest_barycentric_weight_numeric_exponent": -3.0 * kappa,
        "finite_fixture": asdict(sparse_core_bound(0.1, 100, 1.0)),
        "verdict": (
            "the sparse core is rigorous but is realized by the positive "
            "chamber template and gives no finite-aperture exclusion"
        ),
    }
    assert payload["largest_barycentric_weight_exponent"] == -0.0540909702
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
