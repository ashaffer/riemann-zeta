"""Exponent replay for the zeta-specific QP reverse-phase reduction."""

from __future__ import annotations

from math import ceil, log


def logarithmic_partition_count(w: float) -> int:
    """Bins of log-width at most w/2 needed to partition [N,2N]."""

    if w <= 0.0:
        raise ValueError("w must be positive")
    return ceil(2.0 * log(2.0) / w)


def phase_discrepancy_exponents(aperture: float, eta: float) -> dict[str, float]:
    """Powers in the Erdos--Turan/second-derivative phase estimate."""

    if not (0.0 < aperture < 2.0):
        raise ValueError("aperture must lie in (0,2)")
    if not (0.0 < eta < 2.0 - aperture):
        raise ValueError("eta must lie in (0,2-aperture)")
    return {
        "truncation": -eta,
        "upper_height": (aperture + eta) / 2.0 - 1.0,
        "lower_height": -0.25,
    }


def negative_mass_from_modulus(relative_modulus: float, w: float = 0.2) -> float:
    """Guaranteed N-normalized negative mass after phase alignment."""

    if relative_modulus < 0.0:
        raise ValueError("relative_modulus must be nonnegative")
    return 3.0 * relative_modulus / (4.0 * logarithmic_partition_count(w))


def singleton_probability_depth() -> float:
    """The defective probability-normalized interval supremum."""

    return 1.0


def singleton_mass_depth(scale: float) -> float:
    """A singleton's contribution with the correct Turan normalization."""

    if scale <= 0.0:
        raise ValueError("scale must be positive")
    return 1.0 / scale


def minimum_atoms_for_mass_event(scale: float, saving: float) -> int:
    """Atomic lower bound forced by E_N^- >= N^-saving."""

    if scale <= 0.0:
        raise ValueError("scale must be positive")
    if not (0.0 < saving < 1.0):
        raise ValueError("saving must lie in (0,1)")
    return ceil(scale ** (1.0 - saving))


def turan_strip_width(saving: float, aperture: float) -> float:
    if saving <= 0.0 or aperture <= 0.0:
        raise ValueError("saving and aperture must be positive")
    return (saving / aperture) ** 2


def turan_half_power_coverage(saving: float, aperture: float) -> float:
    """Limiting longest-scale half-power exponent in the Turan window.

    Coverage by |tau| >= N^(1/2) requires this number to be strictly below
    one.  The sixth root is the beta^(1/6) width in the local criterion at
    the limiting choice beta=saving/aperture.
    """

    if saving <= 0.0 or aperture <= 0.0:
        raise ValueError("saving and aperture must be positive")
    r = (saving / aperture) ** (1.0 / 6.0)
    if r >= 1.0:
        raise ValueError("saving/aperture must be below one")
    return (1.0 + r) / (2.0 * aperture * (1.0 - r))


def reverse_bridge_ledger(
    qp_power: float = 0.019,
    radialization_power: float = 1.0,
    aperture: float = 50.0 / 33.0,
) -> dict[str, float]:
    natural_saving = qp_power * radialization_power
    return {
        "qp_power": qp_power,
        "radialization_power": radialization_power,
        "natural_saving": natural_saving,
        "strip_width": turan_strip_width(natural_saving, aperture),
        "aperture": aperture,
    }


if __name__ == "__main__":
    print(logarithmic_partition_count(0.2))
    print(phase_discrepancy_exponents(50.0 / 33.0, 0.1))
    print(reverse_bridge_ledger())
