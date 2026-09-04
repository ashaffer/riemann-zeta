"""Exact Bezout-token normal form for the anchored four-completion gate.

This module is deliberately an algebraic audit, not a proof of the open
neighbourhood-degree-sum estimate.  For a primitive anchor ``(c, C)`` choose
``u, v`` with ``c*u-C*v=1``.  A centre pair and a partner pair then have the
unique token forms

    b = u*delta-C*n,       B = v*delta-c*n,
    d = -v*h+c*m,          E = -u*h+C*m.

The middle determinant is ``delta*m-n*h`` and the product sum is represented
by a symmetric integral matrix of determinant minus one.  The resulting Gram
identities factor back into the original coordinate products.  In particular
they expose a useful normal form, but do not create an additional completion
condition or an ``O(D)`` occupied-cell theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


Pair = tuple[int, int]
Token = tuple[int, int]
Matrix2 = tuple[tuple[int, int], tuple[int, int]]


def _extended_gcd(first: int, second: int) -> tuple[int, int, int]:
    """Return ``(g, x, y)`` with ``first*x+second*y=g>0``."""

    old_r, r = abs(first), abs(second)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    x = old_s if first >= 0 else -old_s
    y = old_t if second >= 0 else -old_t
    return old_r, x, y


@dataclass(frozen=True)
class BezoutFourCompletionChart:
    """The unimodular token chart based at one primitive anchor."""

    c: int
    C: int
    u: int
    v: int
    K: Matrix2

    @classmethod
    def from_anchor(cls, anchor: Pair) -> "BezoutFourCompletionChart":
        c, C = map(int, anchor)
        if c <= 0 or C <= 0 or gcd(c, C) != 1:
            raise ValueError("the anchor must be a positive primitive pair")
        common, u, coefficient_of_C = _extended_gcd(c, C)
        if common != 1:
            raise AssertionError("extended gcd did not return a Bezout pair")
        v = -coefficient_of_C
        if c * u - C * v != 1:
            raise AssertionError("the oriented Bezout identity failed")
        mixed = c * u + C * v
        K = ((-2 * u * v, mixed), (mixed, -2 * c * C))
        if K[0][0] * K[1][1] - K[0][1] * K[1][0] != -1:
            raise AssertionError("the token Gram matrix is not unimodular")
        return cls(c=c, C=C, u=u, v=v, K=K)

    def center_token(self, center: Pair) -> Token:
        """Return the unique ``(delta,n)`` token of ``(b,B)``."""

        b, B = map(int, center)
        delta = self.c * b - self.C * B
        numerator = self.u * delta - b
        if numerator % self.C:
            raise AssertionError("the centre token is not integral")
        n = numerator // self.C
        if (self.u * delta - self.C * n, self.v * delta - self.c * n) != (b, B):
            raise AssertionError("centre reconstruction failed")
        return delta, n

    def partner_token(self, partner: Pair) -> Token:
        """Return the unique ``(h,m)`` token of ``(d,E)``."""

        d, E = map(int, partner)
        h = self.C * d - self.c * E
        numerator = d + self.v * h
        if numerator % self.c:
            raise AssertionError("the partner token is not integral")
        m = numerator // self.c
        if (-self.v * h + self.c * m, -self.u * h + self.C * m) != (d, E):
            raise AssertionError("partner reconstruction failed")
        return h, m

    @staticmethod
    def determinant(first: Token, second: Token) -> int:
        return first[0] * second[1] - first[1] * second[0]

    def pairing(self, first: Token, second: Token) -> int:
        """Return ``first^T K second``."""

        x, y = first
        z, w = second
        return (
            x * (self.K[0][0] * z + self.K[0][1] * w)
            + y * (self.K[1][0] * z + self.K[1][1] * w)
        )

    def audit_pair(self, center: Pair, partner: Pair) -> "TokenPairLedger":
        """Verify all determinant, Gram, and factorisation identities."""

        b, B = center
        d, E = partner
        P = self.center_token(center)
        Q = self.partner_token(partner)
        Q0 = (0, 1)
        delta, _ = P
        h, _ = Q
        kappa = self.determinant(P, Q)
        S0 = self.pairing(P, Q0)
        S = self.pairing(P, Q)
        L = self.C * d + self.c * E

        expected = {
            "delta": self.c * b - self.C * B,
            "h": self.C * d - self.c * E,
            "kappa": b * d - B * E,
            "S0": b * self.c + B * self.C,
            "S": b * d + B * E,
        }
        observed = {
            "delta": delta,
            "h": h,
            "kappa": kappa,
            "S0": S0,
            "S": S,
        }
        if observed != expected:
            raise AssertionError("a physical invariant disagrees with its token form")

        if 2 * self.c * self.C * S != S0 * L + delta * h:
            raise AssertionError("the first Lorentz multiplication identity failed")
        if 2 * self.c * self.C * kappa != S0 * h + delta * L:
            raise AssertionError("the second Lorentz multiplication identity failed")
        if (S0 + delta) * (L + h) != 2 * self.c * self.C * (S + kappa):
            raise AssertionError("the positive factorisation failed")
        if (S0 - delta) * (L - h) != 2 * self.c * self.C * (S - kappa):
            raise AssertionError("the negative factorisation failed")
        if S * S - kappa * kappa != 4 * b * B * d * E:
            raise AssertionError("the middle Gram identity failed")

        return TokenPairLedger(
            center_token=P,
            partner_token=Q,
            delta=delta,
            h=h,
            middle_determinant=kappa,
            anchor_sum=S0,
            partner_sum=L,
            middle_sum=S,
        )


@dataclass(frozen=True)
class TokenPairLedger:
    center_token: Token
    partner_token: Token
    delta: int
    h: int
    middle_determinant: int
    anchor_sum: int
    partner_sum: int
    middle_sum: int


@dataclass(frozen=True)
class HardDiamond:
    first_residual: int
    second_residual: int
    diamond_value: int
    bound: int

    @property
    def holds(self) -> bool:
        return self.diamond_value <= self.bound


def hard_diamond(q: int, D: int, row: int, product_sum: int, determinant: int) -> HardDiamond:
    """Audit the exact equivalence of two hard windows and one diamond.

    If ``product_sum=uv+UV`` and ``determinant=uv-UV``, the two residuals
    are ``4*row*(sum+det)-q^3`` and ``4*row*(sum-det)-q^3``.  The maximum of
    their absolute values is exactly

        ``abs(4*row*sum-q^3)+4*row*abs(det)``.
    """

    first = 4 * row * (product_sum + determinant) - q**3
    second = 4 * row * (product_sum - determinant) - q**3
    diamond = abs(4 * row * product_sum - q**3) + 4 * row * abs(determinant)
    if diamond != max(abs(first), abs(second)):
        raise AssertionError("the hard-diamond equivalence failed")
    return HardDiamond(first, second, diamond, q * D)


@dataclass(frozen=True)
class PrimeNonzeroMixedRemainder:
    q: int
    D: int
    anchor: Pair
    center: Pair
    partner: Pair
    base_row: int
    next_row: int
    chart: BezoutFourCompletionChart
    ledger: TokenPairLedger
    base_diamond: HardDiamond
    next_diamond: HardDiamond


def prime_nonzero_mixed_remainder_fixture() -> PrimeNonzeroMixedRemainder:
    """A literal all-prime chain with ``delta*h != 0`` and ``D^2<q``.

    This is the central/same-centre arm of the seven-prime fixture already
    certified in ``QPActualPrimeNDS.lean``.  It rules out interpreting the
    small term ``delta*h`` in the Lorentz identity as an integer which must
    vanish merely because it is smaller than the large modulus ``2*c*C``.
    """

    m = 2_934_091
    q = 2 * m
    D = 1_912
    anchor = (m + 18, m + 12)
    center = (m, m + 6)
    partner = (m + 12, m + 6)
    base_row = m - 18
    next_row = m - 12
    chart = BezoutFourCompletionChart.from_anchor(anchor)
    ledger = chart.audit_pair(center, partner)
    base = hard_diamond(q, D, base_row, ledger.anchor_sum, ledger.delta)
    nxt = hard_diamond(
        q, D, next_row, ledger.middle_sum, ledger.middle_determinant
    )
    if not (base.holds and nxt.holds):
        raise AssertionError("the prime fixture left a hard diamond")
    if ledger.delta * ledger.h == 0 or D * D >= q:
        raise AssertionError("the mixed-remainder no-go was not realized")
    return PrimeNonzeroMixedRemainder(
        q=q,
        D=D,
        anchor=anchor,
        center=center,
        partner=partner,
        base_row=base_row,
        next_row=next_row,
        chart=chart,
        ledger=ledger,
        base_diamond=base,
        next_diamond=nxt,
    )
