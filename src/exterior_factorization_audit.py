"""Exact fixtures for the exterior-factorization falsifier.

The operator question is whether a bounded old block ``A`` and collar charge
``C`` admit ``C = T A``.  The routines below deliberately use only rational
arithmetic.  They separate four logically different facts:

* the old and collar diagonal blocks can be positive while a nullvector is
  charged (the enlarged block is then necessarily indefinite);
* a positive enlarged block gives a square-root/Schur factorization, but a
  family of linear factors through ``A`` can have unbounded norm;
* a positive infinite-dimensional block need not give even a closable
  factor through ``A`` when ``ran A`` is not closed; and
* an equality on a merely dense core can be faked by a nonclosable operator
  while the actual kernel is charged.

These are abstract proof-class tests.  They make no assertion about the
completed-zeta operator, a zero-free strip, or RH.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import json


Q = Fraction


@dataclass(frozen=True)
class SameOldBlockLedger:
    """Two extensions with identical positive diagonal blocks."""

    old_positive_value: Q
    old_null_value: Q
    collar_value: Q
    uncharged_null_charge: Q
    charged_null_charge: Q
    charged_null_collar_determinant: Q
    charged_negative_direction_value: Q


def same_old_block_different_charge() -> SameOldBlockLedger:
    """Return the exact ``diag(1, 0)`` old-block comparison.

    The charged extension has block matrix, in coordinates
    ``(positive old, null old, collar)``,

        [[1, 0, 0], [0, 0, 1], [0, 1, 1]].

    On the null/collar vector ``(1, -1)`` its value is ``-1``.  The
    uncharged extension replaces both cross entries by zero and is PSD.
    """

    null_charge = Q(1)
    collar = Q(1)
    negative_value = 2 * null_charge * Q(1) * Q(-1) + collar
    return SameOldBlockLedger(
        old_positive_value=Q(1),
        old_null_value=Q(0),
        collar_value=collar,
        uncharged_null_charge=Q(0),
        charged_null_charge=null_charge,
        charged_null_collar_determinant=-null_charge * null_charge,
        charged_negative_direction_value=negative_value,
    )


@dataclass(frozen=True)
class ScalarContactLedger:
    epsilon: Q
    old_block: Q
    charge: Q
    collar_block: Q
    determinant: Q
    schur_square_root_identity_defect: Q
    unique_nonzero_factor_norm: Q | None


def scalar_contact(epsilon: Q | int) -> ScalarContactLedger:
    """Audit ``[[eps^2, eps], [eps, 1]]`` exactly.

    It is the Gram matrix of ``(eps, 1)``.  For ``eps != 0`` the only scalar
    factor in ``C = T A`` has size ``1/|eps|``.  At contact ``eps = 0`` the
    charge vanishes exactly.
    """

    eps = Q(epsilon)
    old = eps * eps
    charge = eps
    collar = Q(1)
    # At eps = 0 the equation is 0 = T*0, so factors exist but are not
    # unique.  ``None`` records the absence of the unique nonzero formula;
    # it must not be read as nonexistence of a factor at the limiting block.
    factor = None if eps == 0 else abs(charge / old)
    return ScalarContactLedger(
        epsilon=eps,
        old_block=old,
        charge=charge,
        collar_block=collar,
        determinant=old * collar - charge * charge,
        schur_square_root_identity_defect=charge * charge - old,
        unique_nonzero_factor_norm=factor,
    )


def uniform_factor_blowup(epsilons: tuple[Q, ...]) -> tuple[Q | None, ...]:
    """Return the exact reduced factor norms in the scalar contact family."""

    return tuple(
        scalar_contact(eps).unique_nonzero_factor_norm for eps in epsilons
    )


@dataclass(frozen=True)
class NonclosedRangeLedger:
    block_start: int
    block_length: int
    input_norm_squared: Q
    quotient_output: Q
    finite_schur_completion_defect: Q
    charge_preimage_square_sum: int


def nonclosable_psd_sequence(block_start: int, block_length: int) -> NonclosedRangeLedger:
    """Give an exact graph sequence for a PSD nonclosed-range example.

    On ``ell^2`` take ``A e_n=4^-n e_n`` and
    ``C x=sum 4^-n x_n``.  With the rational collar diagonal
    ``D=sum_(n>=1) 4^-n=1/3``, the full form is

        sum 4^-n |x_n+t|^2 >= 0.

    Nevertheless ``C*1=(4^-n)`` is not in ``ran A``: its only formal
    preimage is the non-square-summable constant sequence.  The induced
    quotient map is ``T_0 z=sum z_n``.  The returned finite-support vector
    has ``block_length`` entries equal to ``1/block_length``; its norm tends
    to zero while ``T_0 z=1``, proving that ``T_0`` is not closable.
    """

    if block_start < 1:
        raise ValueError("block_start must be positive")
    if block_length < 1:
        raise ValueError("block_length must be positive")
    length = Q(block_length)
    z_value = Q(1, block_length)
    norm_squared = length * z_value * z_value

    # Every finite compression has D=sum(c_n^2/a_n)=sum 4^-n, so its exact
    # generalized Schur complement is zero.  This checks full-block
    # positivity without printing an irrelevant enormous rational value.
    schur_defect = sum(
        Q(1, 4**n) - Q(1, 4**n) ** 2 / Q(1, 4**n)
        for n in range(block_start, block_start + block_length)
    )
    return NonclosedRangeLedger(
        block_start=block_start,
        block_length=block_length,
        input_norm_squared=norm_squared,
        quotient_output=length * z_value,
        finite_schur_completion_defect=schur_defect,
        charge_preimage_square_sum=block_length,
    )


@dataclass(frozen=True)
class ClosedUnboundedLedger:
    coordinate: int
    a_value: Q
    c_value: Q
    schur_defect: Q
    factor_ratio: Q


def closed_unbounded_coordinate(coordinate: int) -> ClosedUnboundedLedger:
    """Audit the PSD model ``A=diag(4^-n)``, ``C=A^(1/2)``.

    The full block ``[[A,C],[C,I]]`` is PSD, while its canonical factor
    through ``A`` is the closed unbounded diagonal operator
    ``T e_n=2^n e_n``.
    """

    if coordinate < 1:
        raise ValueError("coordinate must be positive")
    n = coordinate
    a_value = Q(1, 4**n)
    c_value = Q(1, 2**n)
    return ClosedUnboundedLedger(
        coordinate=n,
        a_value=a_value,
        c_value=c_value,
        schur_defect=c_value * c_value - a_value,
        factor_ratio=c_value / a_value,
    )


@dataclass(frozen=True)
class DenseCoreLedger:
    averaging_length: int
    distance_to_charged_null_squared: Q
    a_image_norm_squared: Q
    core_charge: Q
    actual_null_charge: Q


def dense_core_false_positive(averaging_length: int) -> DenseCoreLedger:
    """Return the sequence witnessing a fake dense-core factorization.

    Let ``X=C + ell^2``, ``A(alpha,z)=(0,z)``, and ``C(alpha,z)=alpha``.
    On the dense graph core ``D={(sum z_n,z): z in c00}``, define
    ``T(0,z)=sum z_n``.  Then ``C=T A`` on ``D``.  For the vector with
    ``averaging_length`` entries ``1/averaging_length``, the graph point
    tends to the charged nullvector ``(1,0)``, while ``A`` tends to zero and
    the core charge stays one.  Thus ``T`` is nonclosable and the identity
    says nothing about the actual kernel.
    """

    if averaging_length < 1:
        raise ValueError("averaging_length must be positive")
    norm_squared = Q(1, averaging_length)
    return DenseCoreLedger(
        averaging_length=averaging_length,
        distance_to_charged_null_squared=norm_squared,
        a_image_norm_squared=norm_squared,
        core_charge=Q(1),
        actual_null_charge=Q(1),
    )


def _jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    return value


def audit_ledger() -> dict[str, object]:
    """Return a compact exact replay ledger."""

    epsilons = (Q(1, 2), Q(1, 4), Q(1, 8), Q(0))
    return {
        "scope": "ABSTRACT_PROOF_CLASS_ONLY",
        "same_old_block": asdict(same_old_block_different_charge()),
        "scalar_contacts": [asdict(scalar_contact(eps)) for eps in epsilons],
        "uniform_factor_norms": uniform_factor_blowup(epsilons),
        "nonclosable_psd": asdict(nonclosable_psd_sequence(10, 100)),
        "closed_unbounded": asdict(closed_unbounded_coordinate(20)),
        "dense_core_false_positive": asdict(dense_core_false_positive(100)),
        "claims_rh_or_strip": False,
    }


def main() -> None:
    print(json.dumps(_jsonable(audit_ledger()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
