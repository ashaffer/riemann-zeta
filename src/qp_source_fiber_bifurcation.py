#!/usr/bin/env python3
"""Exact finite algebra for the QP/Turan source-fiber bifurcation.

This module isolates what a legal negative source event forces and how any
positive shallow antenna produces an adaptive bad source-fiber separator.
It checks finite identities and exponent bookkeeping only.  It does not
replace pseudo-nodes by actual primes or prove DPA, LTRAD, a zero-free strip,
or RH.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import argparse
import json
import math
from typing import Sequence

import numpy as np


SOURCE_DEPTH_EXPONENT = Fraction(1, 1000)
TRANSVERSE_TARGET_EXPONENT = Fraction(179, 10_000)
RADIAL_TARGET_EXPONENT = Fraction(189, 10_000)
DPA_TARGET_EXPONENT = Fraction(19, 1000)
DIFFUSE_ANTENNA_ERROR_EXPONENT = Fraction(1, 2)
DIFFUSE_SOURCE_FIBER_EXPONENT = (
    DIFFUSE_ANTENNA_ERROR_EXPONENT - SOURCE_DEPTH_EXPONENT
)


def _vector(values: Sequence[float], *, name: str) -> np.ndarray:
    result = np.asarray(values, dtype=float)
    if result.ndim != 1 or result.size == 0:
        raise ValueError(f"{name} must be a nonempty vector")
    return result


def source_direction(source_atom: Sequence[float], depth: float) -> np.ndarray:
    """Return ``v=a(t0)+Dq`` for the all-ones radial direction ``q``."""

    atom = _vector(source_atom, name="source_atom")
    if depth <= 0.0:
        raise ValueError("depth must be positive")
    return atom + depth


def normalized_separator(
    antenna: Sequence[float], source_atom: Sequence[float], depth: float
) -> tuple[np.ndarray, float]:
    """Return ``y=-alpha/A`` and ``A=D+alpha.a(t0)``.

    A positive denominator is the exact and only feasibility condition for
    this normalization.
    """

    alpha = _vector(antenna, name="antenna")
    atom = _vector(source_atom, name="source_atom")
    if alpha.shape != atom.shape:
        raise ValueError("antenna/source dimension mismatch")
    denominator = float(depth + np.dot(alpha, atom))
    if denominator <= 0.0:
        raise ValueError("source-fiber denominator must be positive")
    return -alpha / denominator, denominator


def radial_dual(antenna: Sequence[float]) -> np.ndarray:
    """Return the direct radial dual ``z=-alpha``.

    When ``alpha`` is a probability vector, ``z.q=-1``.  If every antenna
    response is at least ``-delta``, every dual response is at most ``delta``
    and convex duality bounds the direct radial inradius by ``delta``.  This
    is distinct from the normalized ``v``-fiber separator above.
    """

    return -_vector(antenna, name="antenna")


@dataclass(frozen=True)
class SourceFiberCertificate:
    """Numerical residuals for the exact source/fiber normalization."""

    source_mass: float
    source_response: float
    source_null_residual: float
    antenna_mass: float
    denominator: float
    separator_pairing: float
    separator_pairing_residual: float
    antenna_negative_depth: float
    q_dual_level: float
    v_dual_level: float
    projective_identity_residual: float


def certify_source_fiber(
    *,
    source_probability: Sequence[float],
    antenna_probability: Sequence[float],
    source_atom: Sequence[float],
    high_band_atoms: Sequence[Sequence[float]],
    depth: float,
) -> SourceFiberCertificate:
    """Check the legal-source null relation and adaptive separator identity.

    Rows of ``high_band_atoms`` are cosine atoms ``a(t)``.  When the two
    coefficient vectors are probabilities and the source response is ``-D``,
    the exact identities are

    ``lambda.v=0``, ``y.v=-1``, and ``h(y)=a(alpha)/A``.
    """

    lam = _vector(source_probability, name="source_probability")
    alpha = _vector(antenna_probability, name="antenna_probability")
    atom0 = _vector(source_atom, name="source_atom")
    atoms = np.asarray(high_band_atoms, dtype=float)
    if lam.shape != alpha.shape or alpha.shape != atom0.shape:
        raise ValueError("source-fiber vector dimension mismatch")
    if atoms.ndim != 2 or atoms.shape[1] != alpha.size or atoms.shape[0] == 0:
        raise ValueError("high_band_atoms has the wrong shape")

    direction = source_direction(atom0, depth)
    separator, denominator = normalized_separator(alpha, atom0, depth)
    source_response = float(np.dot(lam, atom0))
    source_null = float(np.dot(lam, direction))
    separator_pairing = float(np.dot(separator, direction))
    antenna_values = atoms @ alpha
    separator_values = atoms @ separator
    antenna_depth = float(-np.min(antenna_values))
    q_dual = float(np.max(atoms @ radial_dual(alpha)))
    v_dual = float(np.max(separator_values))
    return SourceFiberCertificate(
        source_mass=float(np.sum(lam)),
        source_response=source_response,
        source_null_residual=abs(source_null),
        antenna_mass=float(np.sum(alpha)),
        denominator=denominator,
        separator_pairing=separator_pairing,
        separator_pairing_residual=abs(separator_pairing + 1.0),
        antenna_negative_depth=antenna_depth,
        q_dual_level=q_dual,
        v_dual_level=v_dual,
        projective_identity_residual=abs(
            v_dual - antenna_depth / denominator
        ),
    )


def fejer_probability_weights(order: int) -> np.ndarray:
    """Triangular probability weights on frequencies ``1,...,order-1``."""

    if order < 2:
        raise ValueError("order must be at least two")
    indices = np.arange(1, order, dtype=float)
    weights = 2.0 * (order - indices) / (order * (order - 1))
    if abs(float(np.sum(weights)) - 1.0) > 1e-14:
        raise ArithmeticError("Fejer weights failed to normalize")
    return weights


def fejer_probability_transform(order: int, theta: float) -> float:
    """Return the triangular cosine transform ``(K_m(theta)-1)/(m-1)``."""

    weights = fejer_probability_weights(order)
    indices = np.arange(1, order, dtype=float)
    return float(np.dot(weights, np.cos(indices * theta)))


def fejer_closed_form(order: int, theta: float) -> float:
    """Evaluate the same transform through the Fejer-kernel square."""

    if order < 2:
        raise ValueError("order must be at least two")
    geometric = sum(np.exp(1j * j * theta) for j in range(order))
    kernel = abs(geometric) ** 2 / order
    return float((kernel - 1.0) / (order - 1))


@dataclass(frozen=True)
class FejerFiberReplay:
    order: int
    depth: float
    source_null_residual: float
    separator_pairing_residual: float
    exact_floor: float
    computed_fiber_level: float
    fiber_level_residual: float


def fejer_source_fiber_replay(order: int = 101, depth: float = 0.2) -> FejerFiberReplay:
    """Replay an exact Fejer bad fiber with a disjoint source coordinate."""

    if not 0.0 < depth < 1.0:
        raise ValueError("depth must lie in (0,1)")
    alpha_active = fejer_probability_weights(order)
    alpha = np.r_[alpha_active, 0.0]
    lam = np.r_[np.zeros(order - 1), 1.0]
    # At t0 the active Fejer phases equal one.  The disjoint source coordinate
    # is chosen to have cosine response -D.
    atom0 = np.r_[np.ones(order - 1), -depth]
    theta_star = 2.0 * math.pi / order
    atom_star = np.r_[
        np.cos(np.arange(1, order, dtype=float) * theta_star),
        0.0,
    ]
    certificate = certify_source_fiber(
        source_probability=lam,
        antenna_probability=alpha,
        source_atom=atom0,
        high_band_atoms=np.vstack([atom_star]),
        depth=depth,
    )
    expected = 1.0 / ((1.0 + depth) * (order - 1))
    return FejerFiberReplay(
        order=order,
        depth=depth,
        source_null_residual=certificate.source_null_residual,
        separator_pairing_residual=certificate.separator_pairing_residual,
        exact_floor=expected,
        computed_fiber_level=certificate.v_dual_level,
        fiber_level_residual=abs(certificate.v_dual_level - expected),
    )


def exponent_ledger() -> dict[str, str | bool]:
    """Return the exact asymptotic ledger of the diffuse pseudo-node model."""

    mixed_radial = SOURCE_DEPTH_EXPONENT + TRANSVERSE_TARGET_EXPONENT
    return {
        "source_depth": str(SOURCE_DEPTH_EXPONENT),
        "transverse_target": str(TRANSVERSE_TARGET_EXPONENT),
        "mixed_radial_target": str(mixed_radial),
        "recorded_radial_target": str(RADIAL_TARGET_EXPONENT),
        "dpa_target": str(DPA_TARGET_EXPONENT),
        "diffuse_antenna_error": str(DIFFUSE_ANTENNA_ERROR_EXPONENT),
        "diffuse_bad_fiber": str(DIFFUSE_SOURCE_FIBER_EXPONENT),
        "mixing_identity": mixed_radial == RADIAL_TARGET_EXPONENT,
        "pseudo_q_radius_below_dpa_upper_scale": (
            DIFFUSE_ANTENNA_ERROR_EXPONENT > DPA_TARGET_EXPONENT
        ),
        "pseudo_q_radius_violates_direct_ltrad_scale": (
            DIFFUSE_ANTENNA_ERROR_EXPONENT > RADIAL_TARGET_EXPONENT
        ),
        "pseudo_v_radius_violates_transverse_scale": (
            DIFFUSE_SOURCE_FIBER_EXPONENT > TRANSVERSE_TARGET_EXPONENT
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=101)
    parser.add_argument("--depth", type=float, default=0.2)
    args = parser.parse_args()
    print(
        json.dumps(
            {
                "fejer_fiber": asdict(
                    fejer_source_fiber_replay(args.order, args.depth)
                ),
                "exponents": exponent_ledger(),
                "scope": (
                    "FINITE_ALGEBRA_AND_PSEUDONODE_LEDGER_ONLY_"
                    "NO_ACTUAL_PRIME_DPA_LTRAD_STRIP_OR_RH_PROOF"
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
