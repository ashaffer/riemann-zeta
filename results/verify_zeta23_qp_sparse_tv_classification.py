#!/usr/bin/env python3
"""Replay the QP sparse/TV classification and transversality certificates."""

from __future__ import annotations

import json
import pathlib
import sys
from dataclasses import asdict

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qp_sparse_tv_classification import (  # noqa: E402
    all_remote_extremal_chamber,
    basis_perturbation_ledger,
    classify_matrix,
    cosine_vandermonde_leading_constant,
    near_optimal_stability_bound,
    normalized_cosine_determinant,
    positive_depth_minimax,
)


def asymptotic_replay(
    nodes: tuple[float, ...], frequencies: tuple[int, ...], tau: float
) -> dict[str, float | list[float] | list[int]]:
    predicted = cosine_vandermonde_leading_constant(nodes, frequencies)
    observed = normalized_cosine_determinant(nodes, frequencies, tau)
    relative_error = abs(observed / predicted - 1.0)
    assert predicted != 0.0
    assert relative_error < 3.0e-3
    return {
        "nodes": list(nodes),
        "frequencies": list(frequencies),
        "tau": tau,
        "predicted_leading_constant": predicted,
        "normalized_determinant": observed,
        "relative_error": relative_error,
    }


def main() -> None:
    determinant_ledgers = {
        "harmonic_minor": asymptotic_replay(
            (0.3, 0.8, 1.4), (1, 3, 6), 0.004
        ),
        "carrier_augmented_minor": asymptotic_replay(
            (0.3, 0.8, 1.4), (0, 3, 6), 0.004
        ),
        "affine_minor": asymptotic_replay(
            (0.0, 0.3, 0.8, 1.4), (1, 2, 4, 7), 0.003
        ),
    }

    phases = np.asarray([0.88, 1.95])
    harmonics = tuple(range(1, 7))
    matrix = np.cos(np.outer(phases, harmonics))
    classification = classify_matrix(matrix, harmonics)
    assert classification.full_spark
    assert classification.signed_minimizing_supports == ((4, 6),)
    assert classification.signed_unique
    assert classification.positive_minimizing_supports == ((4, 5),)
    assert classification.positive_unique
    assert classification.maximum_positive_depth is not None
    minimax_depth = positive_depth_minimax(matrix)
    assert abs(minimax_depth - classification.maximum_positive_depth) < 1.0e-9

    signed_winner = next(
        candidate for candidate in classification.candidates if candidate.signed_unique
    )
    positive_winner = next(
        candidate for candidate in classification.candidates if candidate.positive_unique
    )
    assert signed_winner.signed_dual_slack > 0.05
    assert positive_winner.positive_dual_slack is not None
    assert positive_winner.positive_dual_slack > 0.25

    chambers = [all_remote_extremal_chamber(size) for size in (2, 3, 5)]
    for chamber in chambers:
        chamber_matrix = np.cos(np.outer(chamber.phases, chamber.harmonics))
        replay = classify_matrix(chamber_matrix, chamber.harmonics)
        assert replay.signed_unique and replay.positive_unique
        assert replay.positive_minimizing_supports == (chamber.harmonics,)
        assert replay.maximum_positive_depth is not None
        assert abs(replay.maximum_positive_depth - chamber.depth) < 1.0e-9
        assert chamber.depth > 1.0 / 2.1
        assert chamber.residual < 1.0e-12

    stability = near_optimal_stability_bound(0.003, 0.2, 3.0, 2)
    perturbation = basis_perturbation_ledger(1.0e-5, 10, 4, 2.0, 3.0)
    assert abs(stability.off_support_l1_upper - 0.015) < 1.0e-14
    assert abs(stability.total_l1_distance_upper - 0.105) < 1.0e-14
    assert perturbation.neumann_product < 0.5

    print(
        json.dumps(
            {
                "schema": "verify-zeta23-qp-sparse-tv-classification-v1",
                "status": "PASS",
                "determinant_ledgers": determinant_ledgers,
                "redundant_dictionary": {
                    "signed_support": list(
                        classification.signed_minimizing_supports[0]
                    ),
                    "signed_cost": classification.minimum_signed_cost,
                    "signed_dual_slack": signed_winner.signed_dual_slack,
                    "positive_support": list(
                        classification.positive_minimizing_supports[0]
                    ),
                    "positive_depth": classification.maximum_positive_depth,
                    "positive_minimax_depth": minimax_depth,
                    "positive_dual_slack": positive_winner.positive_dual_slack,
                },
                "all_remote_chambers": [asdict(item) for item in chambers],
                "near_optimal_stability": asdict(stability),
                "phase_perturbation": asdict(perturbation),
                "verdict": (
                    "off a locally finite dilation set, exact optima have "
                    "sharp M-atom support and the positive optimizer is unique"
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
