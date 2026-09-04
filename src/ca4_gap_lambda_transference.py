"""Exact finite algebra for the CA4 gap-to-Lambda transference falsifier.

This module does not model the actual primes.  It verifies the bounded-gap
periodic cell and the two-dimensional Gram obstruction used to show that
absolute continuity alone cannot transfer a fixed natural-weight fourth
moment to adjacent-gap hat weights.
"""

from __future__ import annotations

import cmath
from fractions import Fraction
import json
import math


PERIOD = 18
MOTIF = (0, 1, 2, 3, 4, 5, 6, 8, 16)


def cyclic_gaps() -> tuple[int, ...]:
    """Return the consecutive gaps in one periodic motif cell."""

    return tuple(
        MOTIF[index + 1] - MOTIF[index]
        for index in range(len(MOTIF) - 1)
    ) + (PERIOD - MOTIF[-1] + MOTIF[0],)


def voronoi_weights() -> tuple[Fraction, ...]:
    """Return the constant-profile cyclic Voronoi/trapezoid masses."""

    gaps = cyclic_gaps()
    return tuple(
        Fraction(gaps[index - 1] + gaps[index], 2)
        for index in range(len(gaps))
    )


def density_ratios() -> tuple[Fraction, ...]:
    """Hat probability divided by the uniform natural probability."""

    # Hat mass is w_a/PERIOD and natural mass is 1/len(MOTIF).
    return tuple(
        weight * len(MOTIF) / PERIOD for weight in voronoi_weights()
    )


def natural_structure(harmonic: int) -> complex:
    """Normalized natural cell Fourier coefficient."""

    return sum(
        cmath.exp(2j * math.pi * harmonic * position / PERIOD)
        for position in MOTIF
    ) / len(MOTIF)


def hat_structure(harmonic: int) -> complex:
    """Normalized cyclic-hat cell Fourier coefficient."""

    return sum(
        float(weight)
        * cmath.exp(2j * math.pi * harmonic * position / PERIOD)
        for position, weight in zip(MOTIF, voronoi_weights())
    ) / PERIOD


def exact_zero_certificates() -> dict[str, bool]:
    """Return combinatorial certificates for harmonics 2, 3, and 4."""

    residues_mod_9 = sorted(position % 9 for position in MOTIF)
    counts_mod_6 = tuple(
        sum(position % 6 == residue for position in MOTIF)
        for residue in range(6)
    )
    return {
        # Harmonics 2 and 4 are the sums of all ninth roots, with 4 coprime
        # to 9.  Harmonic 3 has counts (2,1,2,1,2,1); each of the even and
        # odd triples separately sums to zero among the sixth roots.
        "harmonic_2": residues_mod_9 == list(range(9)),
        "harmonic_3": counts_mod_6 == (2, 1, 2, 1, 2, 1),
        "harmonic_4": residues_mod_9 == list(range(9)),
    }


def gram_counterexample(epsilon: Fraction = Fraction(1, 4)) -> dict[str, Fraction]:
    """Evaluate x^T G x and (Dx)^T G (Dx) for the rank-one PSD no-go."""

    if not 0 < epsilon < 1:
        raise ValueError("epsilon must lie in (0,1)")
    # G=[[1,-1],[-1,1]], x=(1,1), Dx=(1+eps,1-eps).
    return {
        "natural_form": Fraction(0),
        "reweighted_form": 4 * epsilon * epsilon,
        "minimum_density": 1 - epsilon,
        "maximum_density": 1 + epsilon,
    }


def audit() -> dict[str, object]:
    """Return the exact/numerical motif and Gram ledger."""

    gaps = cyclic_gaps()
    weights = voronoi_weights()
    ratios = density_ratios()
    zeros = exact_zero_certificates()
    natural_values = {str(k): abs(natural_structure(k)) for k in (2, 3, 4)}
    hat_value = hat_structure(2)
    if gaps != (1, 1, 1, 1, 1, 1, 2, 8, 2):
        raise AssertionError("motif gap serialization changed")
    if sum(weights) != PERIOD:
        raise AssertionError("Voronoi masses do not partition the period")
    if not all(zeros.values()) or max(natural_values.values()) > 2e-15:
        raise AssertionError("natural structure zeros failed")
    if abs(hat_value) < 0.4:
        raise AssertionError("hat alias coefficient unexpectedly vanished")
    if min(ratios) != Fraction(1, 2) or max(ratios) != Fraction(5, 2):
        raise AssertionError("two-sided density bounds changed")
    return {
        "schema": "zeta23.ca4-gap-lambda-transference-falsifier.v1",
        "period": PERIOD,
        "motif": MOTIF,
        "cyclic_gaps": gaps,
        "voronoi_weights": [str(value) for value in weights],
        "density_ratios": [str(value) for value in ratios],
        "density_ratio_bounds": [str(min(ratios)), str(max(ratios))],
        "natural_zero_certificates": zeros,
        "natural_structure_abs": natural_values,
        "hat_harmonic_2": {
            "real": hat_value.real,
            "imag": hat_value.imag,
            "abs": abs(hat_value),
        },
        "rank_one_psd_gram": {
            key: str(value) for key, value in gram_counterexample().items()
        },
        "scope": (
            "exact bounded-gap periodic pseudo-node/linear-algebra falsifier; "
            "not an actual-prime asymptotic and not a refutation of CA4"
        ),
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))
