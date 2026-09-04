"""Exact budget ledger and finite witness for CA4 mask transference.

The asymptotic argument is proved in the accompanying report.  This module
checks the exact exponent obstruction and replays the already frozen HT-HAT
centers.  It constructs the edge-truncated nodal-hat vector, compares its
discrete variation with the natural von Mangoldt shell vector, and evaluates
the scalar CA4 transfer budget.  No finite output is promoted to an
asymptotic claim.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import json
import math

from flint import arb
import numpy as np

from prime_log_hat_tail import (
    TILT,
    WIDTH,
    build_prime_hat_vector,
    fraction_arb,
    integrate_hat_segment,
)


THETA = Fraction(163, 1000)
Q = Fraction(2787, 3250)
CA4_THETA = THETA
CA4_L2_SAVING = Q
CA4_LOSS = Fraction(1, 10)
TARGET = Fraction(19, 1000)
NATURAL_L2_SAVING = Fraction(1)
SEMIPRIME_L2_BUDGET_EXPONENT = Q - Fraction(1, 20)
FROZEN_CENTERS = (
    Fraction(1025, 2),
    Fraction(2049, 2),
    Fraction(4097, 2),
    Fraction(8193, 2),
)


def energy_inflation(q: Fraction = CA4_L2_SAVING) -> Fraction:
    """Exponent in S2(lambda)/S2(natural), up to Y^o(1)."""

    return NATURAL_L2_SAVING - q


def natural_diagonal_budget(
    q: Fraction = CA4_L2_SAVING,
    loss: Fraction = CA4_LOSS,
) -> Fraction:
    """Allowed fourth-moment inflation above the natural diagonal."""

    return 2 * energy_inflation(q) + loss


def sup_multiplier_budget(
    q: Fraction = CA4_L2_SAVING,
    loss: Fraction = CA4_LOSS,
) -> Fraction:
    """Largest beta for which even a fictitious Y^(4 beta) bound fits."""

    return natural_diagonal_budget(q, loss) / 4


def l2_tail_mass_exponent(
    beta: Fraction,
    q: Fraction = CA4_L2_SAVING,
) -> Fraction:
    """Saving in the high-ratio mass supplied by S2(lambda) alone."""

    return beta + q - 1


MASS_O1_THRESHOLD = energy_inflation()
MASS_TARGET_THRESHOLD = energy_inflation() + TARGET
SUP_BUDGET_THRESHOLD = sup_multiplier_budget()
FULL_SUP_DEFICIT = 4 * CA4_THETA - natural_diagonal_budget()
O1_TRUNCATION_DEFICIT = MASS_O1_THRESHOLD - SUP_BUDGET_THRESHOLD
TARGET_TRUNCATION_DEFICIT = MASS_TARGET_THRESHOLD - SUP_BUDGET_THRESHOLD


def l2_truncation_can_fit_sup_budget() -> bool:
    """Whether L2 control yields a mass-retaining cutoff inside the budget."""

    return MASS_O1_THRESHOLD < SUP_BUDGET_THRESHOLD


def discrete_variation(weights: np.ndarray) -> float:
    """Internal first-difference variation."""

    values = np.asarray(weights, dtype=float)
    if values.ndim != 1 or len(values) < 2:
        raise ValueError("weights must be a one-dimensional nontrivial vector")
    return float(np.sum(np.abs(np.diff(values))))


def difference_witness(weights: np.ndarray) -> np.ndarray:
    """Return b=D^T sign(D weights), so b.weights=TV(weights)."""

    values = np.asarray(weights, dtype=float)
    signs = np.sign(np.diff(values))
    witness = np.zeros_like(values)
    witness[:-1] -= signs
    witness[1:] += signs
    return witness


def natural_shell_weights(primes: tuple[int, ...]) -> np.ndarray:
    """Normalized Alpoge--Furman prime weights Lambda(p)/sqrt(p)."""

    values = np.array([math.log(prime) / math.sqrt(prime) for prime in primes])
    return values / float(np.sum(values))


def retained_hat_weights(center: Fraction) -> tuple[tuple[int, ...], np.ndarray]:
    """Build the exact prescribed edge-truncated hat vector, then normalize."""

    prime_hat = build_prime_hat_vector(center, precision_bits=192)
    primes = prime_hat.primes
    nodes = prime_hat.vector.nodes
    cutoff = float(center) ** float(THETA)
    width = fraction_arb(WIDTH)
    alpha = fraction_arb(TILT)
    raw = [arb(0) for _ in primes]

    for index, (left, right) in enumerate(zip(nodes, nodes[1:])):
        if primes[index + 1] - primes[index] > cutoff:
            continue
        delta = right - left
        raw[index] += integrate_hat_segment(
            left,
            right,
            right / delta,
            -1 / delta,
            width,
            alpha,
        )
        raw[index + 1] += integrate_hat_segment(
            left,
            right,
            -left / delta,
            1 / delta,
            width,
            alpha,
        )

    mass = sum(raw, arb(0))
    if not mass.lower() > 0:
        raise ArithmeticError("the frozen shell has no retained edge mass")
    weights = np.array([float((value / mass).mid()) for value in raw])
    weights /= float(np.sum(weights))
    return primes, weights


@dataclass(frozen=True)
class FrozenAudit:
    center: float
    prime_count: int
    retained_support: int
    cutoff: float
    hat_variation: float
    natural_variation: float
    hat_natural_l1: float
    witness_identity_error: float
    witness_sup_norm: float
    ca4_scalar_budget: float
    mixed_atom_witness_floor: float
    floor_to_budget_ratio: float


def audit_center(center: Fraction) -> FrozenAudit:
    primes, hat = retained_hat_weights(center)
    natural = natural_shell_weights(primes)
    witness = difference_witness(hat)
    variation = discrete_variation(hat)
    budget = float(center) ** (-float(SEMIPRIME_L2_BUDGET_EXPONENT))
    witness_floor = variation * variation
    return FrozenAudit(
        center=float(center),
        prime_count=len(primes),
        retained_support=int(np.count_nonzero(hat > 0)),
        cutoff=float(center) ** float(THETA),
        hat_variation=variation,
        natural_variation=discrete_variation(natural),
        hat_natural_l1=float(np.sum(np.abs(hat - natural))),
        witness_identity_error=abs(float(witness @ hat) - variation),
        witness_sup_norm=float(np.max(np.abs(witness))),
        ca4_scalar_budget=budget,
        mixed_atom_witness_floor=witness_floor,
        floor_to_budget_ratio=witness_floor / budget,
    )


def exponent_ledger() -> dict[str, str | bool]:
    """Return the exact fractions used by the scalar transfer test."""

    return {
        "theta": f"{THETA.numerator}/{THETA.denominator}",
        "q": f"{Q.numerator}/{Q.denominator}",
        "semiprime_l2_budget_exponent": (
            f"{SEMIPRIME_L2_BUDGET_EXPONENT.numerator}/"
            f"{SEMIPRIME_L2_BUDGET_EXPONENT.denominator}"
        ),
        "natural_diagonal_fourth_moment_budget": str(
            natural_diagonal_budget()
        ),
        "largest_sup_multiplier_beta_that_fits": str(
            SUP_BUDGET_THRESHOLD
        ),
        "beta_needed_for_o1_discarded_mass": str(MASS_O1_THRESHOLD),
        "beta_needed_for_Y_minus_019_discarded_mass": str(
            MASS_TARGET_THRESHOLD
        ),
        "full_retained_gap_sup_deficit": str(FULL_SUP_DEFICIT),
        "l2_truncation_can_fit_sup_budget": l2_truncation_can_fit_sup_budget(),
    }


def main() -> None:
    payload = {
        "scope": "finite replay at the four preregistered HT-HAT centers only",
        "asymptotic_claim": False,
        "exponents": exponent_ledger(),
        "audits": [asdict(audit_center(center)) for center in FROZEN_CENTERS],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
