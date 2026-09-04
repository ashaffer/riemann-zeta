import math

import numpy as np
from scipy.optimize import brentq

from qp_remote_sparse_core import (
    lattice_points_per_radius_one_packet,
    negative_peak_weight,
    phase_box_haar_log_volume,
    sign_persistence_certificate,
    sparse_core_bound,
)


def explicit_remote_chamber(size: int) -> tuple[np.ndarray, np.ndarray]:
    top = 2 * size - 1
    harmonics = np.arange(size, 2 * size, dtype=int)
    epsilon = 0.05 / size

    def polynomial(theta: float) -> float:
        return (
            0.5
            + epsilon * float(np.sum(np.cos(harmonics[:-1] * theta)))
            + math.cos(top * theta)
        )

    centers = (2.0 * math.pi / 3.0 + 2.0 * math.pi * np.arange(size)) / top
    radius = math.pi / (12.0 * top)
    phases = np.asarray(
        [brentq(polynomial, center - radius, center + radius) for center in centers]
    )
    return phases, harmonics


def test_sparse_core_constants() -> None:
    assert math.isclose(negative_peak_weight(0.2), 1.0 / 9.0)
    assert lattice_points_per_radius_one_packet(1.0) == 3
    assert lattice_points_per_radius_one_packet(1.1) == 2
    bound = sparse_core_bound(0.2, packet_count=25, step=1.0)
    assert bound.exceptional_harmonic_count == 75
    assert math.isclose(bound.largest_weight_lower, 1.0 / 675.0)


def test_remote_chamber_has_certified_open_phase_box() -> None:
    phases, harmonics = explicit_remote_chamber(8)
    certificate = sign_persistence_certificate(phases, harmonics)
    assert certificate.depth > 0.47
    assert certificate.minimum_negative_coefficient > 0.0
    assert certificate.phase_radius > 0.0
    assert certificate.perturbed_depth_lower > 0.45

    perturbation = np.linspace(-0.9, 0.9, len(phases)) * certificate.phase_radius
    shifted = phases + perturbation
    matrix = np.cos(np.outer(shifted, harmonics))
    coefficients = np.linalg.solve(matrix, np.ones(len(phases)))
    assert np.max(coefficients) < 0.0
    assert -1.0 / np.sum(coefficients) >= certificate.perturbed_depth_lower


def test_phase_box_volume_is_exponential_in_dimension() -> None:
    radius = 10.0**-3
    assert math.isclose(phase_box_haar_log_volume(radius, 10), 10 * math.log(radius / math.pi))

