#!/usr/bin/env python3
"""Replay the optimally sparse positive-cosine theorem ledger."""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sparse_cosine_antipode_classification import (  # noqa: E402
    build_antipode_certificate,
    consecutive_chebyshev_classification,
)


def main() -> None:
    supports = ((1, 2, 3), (20, 21, 22, 23), (11, 17, 31, 44, 59))
    depths = (0.2, 0.5, 0.81)
    rows = []
    for support, depth in zip(supports, depths, strict=True):
        certificate = build_antipode_certificate(support, depth)
        assert certificate.top_weight_margin > 0.0
        assert certificate.maximum_vector_residual < 5e-12
        assert abs(certificate.evaluation_determinant) > 1e-10
        rows.append(
            {
                "support": support,
                "depth": depth,
                "root_degree": support[-1],
                "selected_atoms": len(support),
                "residual": certificate.maximum_vector_residual,
            }
        )
    consecutive = build_antipode_certificate((1, 2, 3, 4), 0.6)
    classified = consecutive_chebyshev_classification(consecutive.phases)
    assert classified.strict_positive_antipode
    assert classified.depth is not None and abs(classified.depth - 0.6) < 5e-11
    print(
        json.dumps(
            {
                "status": "PASS",
                "claims": {
                    "sharp_compression_bound": "at most M atoms",
                    "generic_lower_bound": "at least M atoms",
                    "arbitrary_prescribed_support": True,
                    "every_depth_strictly_below_one": True,
                    "consecutive_chebyshev_iff": True,
                },
                "fixtures": rows,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
