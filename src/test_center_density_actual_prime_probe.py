import math

import numpy as np

from center_density_actual_prime_probe import (
    _group_difference,
    _phase_masks,
    floating_retained_hat,
    top_band_scout,
)
from qp_radialization_lab import primes_up_to


def test_phase_mask_and_group_difference() -> None:
    centers = np.exp(np.linspace(0.0, 2 * math.pi, 1001))
    taus = np.array([1.0])
    source = np.array([1.0 + 0.0j])
    masks, normalized = _phase_masks(centers, taus, source, 0.75)
    assert abs(float(np.mean(masks[0])) - math.acos(0.75) / math.pi) < 0.002
    metric = normalized[0]
    difference = _group_difference(masks, metric)
    assert difference.shape == (1,)
    assert difference[0] < 0.0


def test_actual_retained_hat_is_a_probability() -> None:
    center = 8000.5
    primes = np.asarray(
        primes_up_to(math.ceil(center * math.exp(0.2))),
        dtype=np.int64,
    )
    vector = floating_retained_hat(center, primes)
    assert len(vector.primes) == len(vector.nodes) == len(vector.weights)
    assert vector.kept_edge_count > 0
    assert np.all(vector.weights > 0.0)
    np.testing.assert_allclose(np.sum(vector.weights), 1.0, atol=2e-15)


def test_top_band_scout_has_consistent_ledger() -> None:
    center = 8000.5
    primes = np.asarray(
        primes_up_to(math.ceil(center * math.exp(0.2))),
        dtype=np.int64,
    )
    vector = floating_retained_hat(center, primes)
    strata = (np.arange(64, dtype=float) + 0.5) / 64
    scout = top_band_scout(vector, center, strata)
    assert scout["mean_fourth"] >= 0.0
    assert scout["top_integral"] > 0.0
    assert scout["diagonal_density"] > 0.0
    assert scout["diagonal_ratio"] == (
        scout["mean_fourth"] / scout["diagonal_density"]
    )
