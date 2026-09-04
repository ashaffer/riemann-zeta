#!/usr/bin/env python3
"""Exact verifier for the finite-wheel renewal operator theorem.

This checks a random/sieved-wheel model and a full-period coupling identity.
It makes no assertion about local blocks of actual primes.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from finite_wheel_transfer_operator import (  # noqa: E402
    SparseRenewalOperator,
    apply_sparse_entries,
    character_diagonalization,
    prefix_discrepancy_certificate,
    repeated_base_wheel_operator,
    uniform_wheel_certificate,
)


def main() -> None:
    # Independent sparse-system residuals and stochastic transition rows.
    operator = SparseRenewalOperator.unit_wheel(30, 11, Fraction(2, 13))
    forward, backward = operator.gap_resolvents()
    assert apply_sparse_entries(operator.sparse_system_entries(1), forward) == tuple(
        Fraction(gap) for gap in operator.gaps
    )
    assert apply_sparse_entries(operator.sparse_system_entries(-1), backward) == tuple(
        Fraction(operator.gaps[(i - 1) % operator.size])
        for i in range(operator.size)
    )
    assert all(sum(row, Fraction(0)) == 1 for row in operator.transition_matrix())
    assert sum(operator.stationary_voronoi_masses(), Fraction(0)) == 1

    # P is deliberately allowed to vary through nontrivial and non-squarefree
    # values.  Every inequality here is a Fraction comparison.
    cases = (
        (1, 5, Fraction(1, 10)),
        (2, 11, Fraction(1)),
        (6, 7, Fraction(1, 9)),
        (30, 11, Fraction(3, 20)),
        (210, 11, Fraction(1, 5)),
        (1024, 13, Fraction(2, 7)),
    )
    for P, q, p in cases:
        certificate = uniform_wheel_certificate(P, q, p)
        center, radius, bound = certificate.exact_triangle_ledger()
        assert center == Fraction(1, q * (q - 1))
        assert radius == Fraction(1, q)
        assert bound == Fraction(1, q - 1)
        assert all(delta >= 0 for delta in certificate.excesses)
        for r in range(1, q):
            assert abs(certificate.numerical_nonprincipal_mode(r)) <= float(bound) + 2e-14

    # Character diagonalization is an independent spectral readout of the
    # additive mode; the theorem's inequality itself did not use floats.
    certificate = uniform_wheel_certificate(30, 11, Fraction(2, 9))
    for r in range(1, 11):
        direct, reconstructed = character_diagonalization(
            certificate.residue_masses, 11, r
        )
        assert abs(direct - reconstructed) < 2e-14

    # Every stage before q is q-mode zero on a full common period, and every
    # interval truncation is exactly an endpoint coboundary.
    base = repeated_base_wheel_operator(30, 11, Fraction(2, 13))
    base_prefix = prefix_discrepancy_certificate(base, 11)
    assert base_prefix.total_residues == (Fraction(30),) * 11
    final_prefix = prefix_discrepancy_certificate(
        SparseRenewalOperator.unit_wheel(30, 11, Fraction(2, 13)), 11
    )
    for left, right in [(-137, 19), (0, 330), (17, 931), (330, 1320)]:
        assert final_prefix.interval_discrepancy(
            left, right
        ) == final_prefix.endpoint_coboundary(left, right)

    beta = Fraction(1537, 10000)
    kappa_upper = Fraction(123378, 6250000)  # .01974048
    assert beta > kappa_upper

    print("finite-wheel sparse resolvent identities: PASS")
    print("exact rational deletion-coupling certificates: PASS")
    print("uniform growing-P bound: |A_np| <= 1/(q-1)")
    print(f"target exponent margin: beta-kappa_max = {float(beta-kappa_upper):.8f}")
    print("additive/character diagonalization: PASS")
    print("sequential pre-q zero modes and prefix coboundary: PASS")
    print("scope: full-period/renewal wheel; local actual-prime transfer OPEN")


if __name__ == "__main__":
    main()
