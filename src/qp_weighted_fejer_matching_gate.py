"""Exact matching obstruction to an absolute weighted-Fejer covariance bound.

The module records the scalar formulas from
``results/ZETA23-QP-WEIGHTED-FEJER-MATCHING-GATE-2026-08-15.md``.
It does not claim an obstruction for the natural von Mangoldt measure.  It
shows that stable normalization, negative packet means, small scalar
difference moments, and actual-node support do not imply an *absolute*
bound for the quadratic covariance.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class MatchingLedger:
    """Closed-form moment ledger for the two-square matching model."""

    delta: float
    m: int
    b: float
    base_normalization: float
    difference_moment: float
    candidate_normalization: float
    covariance_at_matching_shift: float


@dataclass(frozen=True)
class SubcriticalAPLedger:
    """Exact one-sided covariance ledger for a subcritical AP packet."""

    delta: float
    length: int
    b: float
    base_normalization: float
    maximum_difference_moment: float
    additive_energy: int
    endpoint_triple_count: int
    tail_second_moment: float
    candidate_normalization: float
    endpoint_covariance: float


def matching_ledger(delta: float, m: int, alpha: float | None = None) -> MatchingLedger:
    """Return the exact ledger.

    ``m`` is the number of matched pairs and the packet count is ``2*m``.
    The positive base density is

    ``|1-b U(1+W)|^2 + b^2 |U(1-W)|^2``.

    Its normalization is ``1+4*m*b^2``.  The smaller quadratic root is
    chosen so that every packet moment equals ``-delta``.  The candidate
    square has coefficient ``alpha`` at every packet; by default
    ``alpha=delta``.
    """

    if not (0.0 < delta < 1.0):
        raise ValueError("delta must lie in (0,1)")
    if m < 1:
        raise ValueError("m must be positive")
    discriminant = 1.0 - 16.0 * m * delta * delta
    if discriminant <= 0.0:
        raise ValueError("the construction requires 16*m*delta^2 < 1")
    b = (1.0 - sqrt(discriminant)) / (8.0 * m * delta)
    z0 = 1.0 + 4.0 * m * b * b
    rho = 4.0 * b * b / z0
    if alpha is None:
        alpha = delta

    # D=U(1+W) has E D=-2m delta and
    # E|D|^2=2m+2m(m-1)rho.
    z_candidate = (
        1.0
        - 4.0 * m * alpha * delta
        + alpha * alpha * (2.0 * m + 2.0 * m * (m - 1) * rho)
    )

    # At the matching shift d, Phi(d)=0.  There are m exact zero
    # resonances and m(m-1) translated Sidon-difference resonances.
    covariance = alpha * alpha * (m + m * (m - 1) * rho)
    return MatchingLedger(
        delta=delta,
        m=m,
        b=b,
        base_normalization=z0,
        difference_moment=rho,
        candidate_normalization=z_candidate,
        covariance_at_matching_shift=covariance,
    )


def golomb_pair_frequencies(m: int) -> tuple[list[int], int]:
    """Return an explicit Sidon/Golomb set ``A`` and a matching shift ``d``.

    All frequencies are ``O(m^4)``.  The large offsets make the Fourier
    support sets used in the exact moment calculation disjoint.
    """

    if m < 2:
        raise ValueError("m must be at least two")
    q = 10 * m**3
    offset = 100 * m**4
    a = [offset + q * j + j * j for j in range(1, m + 1)]
    d = 30 * m**4
    return a, d


def subcritical_ap_ledger(
    delta: float, length: int, alpha: float | None = None
) -> SubcriticalAPLedger:
    """Return the exact AP ledger for the density ``|1-bD|^2``.

    Here ``D=sum_{j<length} exp(-i(t0+j*d)u)`` and ``t0`` is separated from
    every AP difference.  The base density makes every packet mean
    ``-delta``.  At the endpoint query ``t0``, the quadratic covariance is
    negative once the additive triple count dominates the tail second
    moment.
    """

    if not (0.0 < delta < 1.0):
        raise ValueError("delta must lie in (0,1)")
    if length < 2:
        raise ValueError("length must be at least two")
    discriminant = 1.0 - 4.0 * length * delta * delta
    if discriminant <= 0.0:
        raise ValueError("the construction requires 4*length*delta^2 < 1")
    b = (1.0 - sqrt(discriminant)) / (2.0 * length * delta)
    z0 = 1.0 + length * b * b
    max_difference = b * b * (length - 1) / z0
    energy = (2 * length**3 + length) // 3
    triple_count = length * (length + 1) // 2
    second_moment = (length + b * b * energy) / z0
    if alpha is None:
        alpha = delta
    z_candidate = 1.0 - 2.0 * alpha * length * delta + alpha * alpha * second_moment
    covariance = alpha * alpha * delta * (second_moment - triple_count)
    return SubcriticalAPLedger(
        delta=delta,
        length=length,
        b=b,
        base_normalization=z0,
        maximum_difference_moment=max_difference,
        additive_energy=energy,
        endpoint_triple_count=triple_count,
        tail_second_moment=second_moment,
        candidate_normalization=z_candidate,
        endpoint_covariance=covariance,
    )


def oriented_differences_are_unique(values: list[int]) -> bool:
    """Check uniqueness of nonzero oriented differences."""

    seen: set[int] = set()
    for i, left in enumerate(values):
        for j, right in enumerate(values):
            if i == j:
                continue
            difference = left - right
            if difference in seen:
                return False
            seen.add(difference)
    return True


def exponent_ledger(c: float = 0.019) -> dict[str, float]:
    """Return aperture and actual-prime mesh transfer exponents.

    Packet count has exponent ``2c`` and the explicit frequencies have
    exponent ``8c``.  Nearest-node transfer through the BHP logarithmic mesh
    ``Y^(-19/40)`` costs ``K*h`` for characters and ``R^2*K*h`` for the
    quadratic covariance integrand.
    """

    return {
        "packet_count": 2.0 * c,
        "frequency_top": 8.0 * c,
        "character_transfer_error": 8.0 * c - 19.0 / 40.0,
        "quadratic_transfer_error": 12.0 * c - 19.0 / 40.0,
        "delta_squared": -2.0 * c,
        "project_aperture_top": 50.0 / 33.0,
    }


if __name__ == "__main__":
    # A scale-free replay with kappa=(2m)delta^2 close to 1/16.
    example_delta = 1.0e-3
    example_m = int((1.0 / 32.0) / (example_delta * example_delta))
    print(matching_ledger(example_delta, example_m))
    print(subcritical_ap_ledger(example_delta, 1000))
    print(exponent_ledger())
