"""Exact exponent and conductor ledgers for the primitive-p^3 shell gate.

The routines in this module are deliberately elementary.  They certify the
finite combinatorics and rational exponent calculations used in the companion
report; they do not claim a new character-sum estimate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class RatioConductorCounts:
    """Numbers of primitive-character partners in each ratio conductor."""

    p3: int
    p2: int
    p: int
    principal: int

    @property
    def total(self) -> int:
        return self.p3 + self.p2 + self.p + self.principal


def primitive_character_count(p: int) -> int:
    """Number of primitive Dirichlet characters modulo p^3, p odd prime."""

    if p < 3:
        raise ValueError("p must be an odd prime")
    return p * (p - 1) ** 2


def ratio_conductor_counts(p: int) -> RatioConductorCounts:
    """Count partners psi for fixed primitive chi, classified by cond(bar chi psi).

    Write a character as (alpha,beta), with alpha modulo p-1 and beta modulo
    p^2.  Primitivity means p does not divide beta.  A beta difference which
    is a unit, a nonzero multiple of p, or zero gives conductor p^3, p^2, or
    at most p respectively.
    """

    if p < 3:
        raise ValueError("p must be an odd prime")
    return RatioConductorCounts(
        p3=p * (p - 2) * (p - 1),
        p2=(p - 1) ** 2,
        p=p - 2,
        principal=1,
    )


def ratio_conductor_from_parameters(
    p: int,
    alpha_difference: int,
    beta_difference: int,
) -> int:
    """Return 1, p, p^2, or p^3 for a character-parameter difference."""

    a = alpha_difference % (p - 1)
    b = beta_difference % (p * p)
    if b % p:
        return p**3
    if b:
        return p**2
    if a:
        return p
    return 1


def formal_burgess_saving(modulus_p_exponent: int, r: int) -> Fraction:
    """Formal p-saving at interval length p in the usual Burgess formula.

    For modulus p^k and N=p, the displayed Burgess expression has exponent

        1 - 1/r + k(r+1)/(4r^2) = 1 - saving.

    This function only computes the expression.  For a cubefull modulus such
    as p^3, the classical theorem does *not* license arbitrary r.
    """

    if r < 1:
        raise ValueError("r must be positive")
    k = modulus_p_exponent
    return Fraction(1, r) - Fraction(k * (r + 1), 4 * r * r)


def classical_burgess_r_is_licensed(modulus_p_exponent: int, r: int) -> bool:
    """Classical Burgess range: all r for cubefree p^k (k<=2), else r<=3."""

    return modulus_p_exponent <= 2 or r <= 3


def best_formal_burgess_saving(modulus_p_exponent: int, r_max: int = 100) -> tuple[int, Fraction]:
    """Optimize the formal (not necessarily licensed) saving over 1<=r<=r_max."""

    values = [(r, formal_burgess_saving(modulus_p_exponent, r)) for r in range(1, r_max + 1)]
    return max(values, key=lambda item: item[1])


def best_licensed_classical_burgess_saving(
    modulus_p_exponent: int,
    r_max: int = 100,
) -> tuple[int, Fraction]:
    """Optimize only over the classical theorem's licensed r-values."""

    values = [
        (r, formal_burgess_saving(modulus_p_exponent, r))
        for r in range(1, r_max + 1)
        if classical_burgess_r_is_licensed(modulus_p_exponent, r)
    ]
    return max(values, key=lambda item: item[1])


def target_p_saving() -> Fraction:
    """D^(1/8) at D=p^(16/33), expressed as a p-exponent."""

    return Fraction(2, 33)


def optimistic_p3_burgess_deficit() -> Fraction:
    """Target 2/33 minus the unlicensed formal r=6 saving 1/48."""

    return target_p_saving() - formal_burgess_saving(3, 6)


def kerr_2019_p3_exponent(r: int) -> Fraction:
    """p-exponent after specializing Kerr's cubefull-part bound to q=p^3,N=p.

    Kerr's bound is

      N^(1-1/r) q^((r+1)/(4r^2)+o(1))
      c^((r-1)/(4r^2)-1/(32r^3)),

    and the cubefull part is c=q=p^3 here.
    """

    if r < 2:
        raise ValueError("r must be at least two")
    return Fraction(1, 1) + Fraction(1, 2 * r) - Fraction(3, 32 * r**3)


def taylor_block_mixed_saving(d: int, r: int) -> Fraction:
    """Optimistic p-saving from a degree-d Taylor block in the q=p^2 scheme.

    For Mellin frequency |t|~p, a degree-d Taylor expansion of t log n is
    uniformly accurate on blocks H=p^(d/(d+1)).  In modulus Q=p^2 units this
    is H=Q^(1/4+kappa), kappa=(d-1)/(4(d+1)).  The one-dimensional mixed
    Burgess/VMVT ledger with M=d(d+1)/2 gives Q-saving

      [4*kappa*(r-M)-1]/[4*r*(r-M)].

    The returned value is twice this, hence the p-saving.  Applicability of a
    prime-power mixed theorem is an additional hypothesis; this is an
    optimistic numerical ceiling, not a proved estimate for the QP mask.
    """

    if d < 1:
        raise ValueError("d must be positive")
    m = Fraction(d * (d + 1), 2)
    if r <= m:
        raise ValueError("r must exceed the VMVT weight")
    kappa = Fraction(d - 1, 4 * (d + 1))
    delta_q = (4 * kappa * (r - m) - 1) / (4 * r * (r - m))
    return 2 * delta_q


def coarse_q2_detector(rho: int, p: int, h: int) -> bool:
    """Hard-cutoff version of the exact coarse-q^2 detector.

    The smooth report identity uses a bump supported on |rho|<p^2/3 and equal
    to one on |rho|<=p^2/4.  This Boolean version tests the support implication:
    in that coarse window, the residue condition rho mod p^2 in [-h,h] is
    equivalent to |rho|<=h.
    """

    if not 0 <= h < p * p // 4:
        raise ValueError("h must be below p^2/4")
    if 3 * abs(rho) >= p * p:
        return False
    residue = rho % (p * p)
    centered = residue if residue <= p * p // 2 else residue - p * p
    return abs(centered) <= h

