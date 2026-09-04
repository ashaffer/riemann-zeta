"""Replay helpers for the hereditary LTRAD obstruction."""

from __future__ import annotations

from math import floor, log


def triangular_weights(length: int) -> list[float]:
    if length < 1:
        raise ValueError("length must be positive")
    return [
        2.0 * (length + 1 - j) / (length * (length + 1))
        for j in range(1, length + 1)
    ]


def fejer_error_bound(length: int, band_top: float, perturbation: float) -> float:
    if length < 1 or band_top < 0.0 or perturbation < 0.0:
        raise ValueError("invalid Fejer parameters")
    return 1.0 / length + band_top * perturbation


def hereditary_exponent_ledger(
    d: float = 0.019,
    c: float = 0.019,
    eta: float = 0.01,
) -> dict[str, float | bool]:
    hard_exponent = c + eta
    long_interval_exponent = 1.0 - d
    return {
        "d": d,
        "c": c,
        "eta": eta,
        "hard_exponent": hard_exponent,
        "long_interval_exponent": long_interval_exponent,
        "hard_is_negligible": hard_exponent < long_interval_exponent,
        "radial_beats_target": hard_exponent > c,
    }


def finite_scale_ledger(
    scale: float,
    d: float = 0.019,
    c: float = 0.019,
    eta: float = 0.01,
) -> dict[str, int | float]:
    if scale <= 2.0:
        raise ValueError("scale must exceed two")
    exponents = hereditary_exponent_ledger(d=d, c=c, eta=eta)
    if not exponents["hard_is_negligible"]:
        raise ValueError("hard core must be smaller than a threshold interval")
    node_count = floor(scale / log(scale))
    hard_count = floor(scale ** (c + eta))
    threshold_count = floor(scale ** (1.0 - d))
    return {
        "node_count": node_count,
        "hard_count": hard_count,
        "threshold_count": threshold_count,
        "uniform_mass_scale": node_count / scale,
        "radial_upper_scale": 2.0 / max(1, hard_count),
    }


def cluster_hard_core_exponent_ledger(
    aperture: float = 50.0 / 33.0,
    radial_exponent: float = 0.019,
    cluster_exponent: float = 0.019,
) -> dict[str, float | bool]:
    """Replay the exponents in the actual-prime cluster hard-core no-go.

    ``radial_exponent`` is the proposed floor exponent ``c`` in
    ``inf F >= -Y**(-c)``.  ``cluster_exponent`` is the physical diameter
    exponent ``theta``.  In the proof range ``0 < c < 5/4-A/2``, the theorem
    forces

        theta >= (3*A - 2 + 6*c)/11 - o(1).
    """

    if not 1.0 < aperture < 2.0:
        raise ValueError("the cluster theorem requires 1 < aperture < 2")
    maximum_radial_exponent = 1.25 - aperture / 2.0
    if not 0.0 < radial_exponent < maximum_radial_exponent:
        raise ValueError(
            "the cluster theorem requires 0 < radial_exponent < 5/4-A/2"
        )
    if not 0.0 <= cluster_exponent < 0.5:
        raise ValueError("invalid cluster hard-core exponents")
    minimum_cluster_exponent = (
        3.0 * aperture - 2.0 + 6.0 * radial_exponent
    ) / 11.0
    common_antipode_error_exponent = (4.0 * cluster_exponent - 2.0) / 3.0
    energy_sqrt_lower_exponent = 2.0 / 3.0 - 11.0 * cluster_exponent / 6.0
    negative_excursion_lower_exponent = (
        aperture / 2.0 - 1.0 / 3.0 - 11.0 * cluster_exponent / 6.0
    )
    return {
        "aperture": aperture,
        "radial_exponent": radial_exponent,
        "maximum_radial_exponent": maximum_radial_exponent,
        "cluster_exponent": cluster_exponent,
        "minimum_cluster_exponent": minimum_cluster_exponent,
        "common_antipode_error_exponent": common_antipode_error_exponent,
        "energy_sqrt_lower_exponent": energy_sqrt_lower_exponent,
        "negative_excursion_lower_exponent": negative_excursion_lower_exponent,
        "nominal_cluster_is_ruled_out": (
            cluster_exponent < minimum_cluster_exponent
        ),
        "literal_fejer_diameter_exponent": 0.5 + cluster_exponent,
    }


if __name__ == "__main__":
    print(hereditary_exponent_ledger())
    print(finite_scale_ledger(10.0**12))
    print(cluster_hard_core_exponent_ledger())
