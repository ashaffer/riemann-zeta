"""Fail-fast spectral-angle tests for the completed incidence decomposition.

The continuum and prime incidence energies are positive separately, but their
separate constrained floors do not reach the exact degree threshold.  This
script tests two genuinely phase-sensitive lower bounds:

* the optimal two-band Friedrichs-angle certificate;
* a multilevel spectral minorant retaining the first k modes of both pieces.

The second bound converges to the full Galerkin matrix as k approaches the
dimension.  Requiring nearly every mode is evidence against a useful
low-dimensional transversality theorem, not a proof about the operator.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass

import mpmath as mp
import numpy as np
from scipy.linalg import null_space

from incidence_poincare_ratio import degree_deficit
from relative_incidence_gap import moment_vectors
from spectral_margins import spectral_form


@dataclass(frozen=True)
class AngleDiagnostic:
    support: float
    relative_dimension: int
    degree: float
    joint_gap: float
    component_deficit: float
    best_two_band_reserve: float
    first_multilevel_certificate: int | None


def constrained_components(
        support: float, dimension: int, dps: int
) -> tuple[float, np.ndarray, np.ndarray]:
    """Return D and the continuum/prime energies on the moment kernel."""
    total_q = np.array(spectral_form(
        support, dimension, dps=dps, include_primes=True,
        zeta_pole=False).tolist(), dtype=float)
    arch_q = np.array(spectral_form(
        support, dimension, dps=dps, include_primes=False,
        zeta_pole=False).tolist(), dtype=float)
    plus, minus = moment_vectors(support, dimension)
    relative_basis = null_space(np.vstack([plus, minus]))

    degree = float(degree_deficit(support))
    arch_degree = float(-mp.digamma(mp.mpf("0.25")) + mp.log(mp.pi))
    prime_degree = degree - arch_degree
    identity = np.eye(dimension)
    continuum = relative_basis.T @ (
        arch_q + arch_degree * identity) @ relative_basis
    prime = relative_basis.T @ (
        total_q - arch_q + prime_degree * identity) @ relative_basis
    return degree, continuum, prime


def weighted_angle_reserve(s: float, t: float, cosine: float) -> float:
    """Sharp lower bound for s(I-P)+t(I-Q) from ||PQ|| <= cosine."""
    discriminant = (s - t) ** 2 + 4 * s * t * cosine ** 2
    return (s + t - np.sqrt(max(0.0, discriminant))) / 2


def diagnose(support: float, dimension: int, dps: int) -> AngleDiagnostic:
    degree, continuum, prime = constrained_components(
        support, dimension, dps)
    wa, va = np.linalg.eigh(continuum)
    wb, vb = np.linalg.eigh(prime)
    joint_gap = float(np.linalg.eigvalsh(continuum + prime)[0] - degree)
    deficit = degree - float(wa[0] + wb[0])
    relative_dimension = len(wa)

    best_reserve = 0.0
    for ka in range(1, relative_dimension):
        s = float(wa[ka] - wa[0])
        if s <= 0:
            continue
        for kb in range(1, relative_dimension):
            t = float(wb[kb] - wb[0])
            if t <= 0:
                continue
            cosine = float(np.linalg.svd(
                va[:, :ka].T @ vb[:, :kb], compute_uv=False)[0])
            best_reserve = max(
                best_reserve, weighted_angle_reserve(s, t, cosine))

    first_certificate = None
    for k in range(1, relative_dimension):
        continuum_minorant = va @ np.diag(np.r_[
            wa[:k], np.repeat(wa[k], relative_dimension - k)]) @ va.T
        prime_minorant = vb @ np.diag(np.r_[
            wb[:k], np.repeat(wb[k], relative_dimension - k)]) @ vb.T
        lower_bound = float(np.linalg.eigvalsh(
            continuum_minorant + prime_minorant)[0])
        if lower_bound >= degree:
            first_certificate = k
            break

    return AngleDiagnostic(
        support=support,
        relative_dimension=relative_dimension,
        degree=degree,
        joint_gap=joint_gap,
        component_deficit=deficit,
        best_two_band_reserve=best_reserve,
        first_multilevel_certificate=first_certificate,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--supports", nargs="+", type=float,
                        default=[1.75, 2.485, 2.996, 3.555, 4.04])
    parser.add_argument("--dimension", type=int, default=12)
    parser.add_argument("--dps", type=int, default=20)
    args = parser.parse_args()
    mp.mp.dps = args.dps

    print("support,dimension,relative_dimension,degree,joint_gap,"
          "component_deficit,best_two_band_reserve,"
          "first_multilevel_certificate")
    for support in args.supports:
        result = diagnose(support, args.dimension, args.dps)
        first = ("none" if result.first_multilevel_certificate is None
                 else str(result.first_multilevel_certificate))
        print(f"{support:.9g},{args.dimension},{result.relative_dimension},"
              f"{result.degree:.12e},{result.joint_gap:.12e},"
              f"{result.component_deficit:.12e},"
              f"{result.best_two_band_reserve:.12e},{first}")


if __name__ == "__main__":
    main()
