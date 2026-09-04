"""Lossless Bezout-token coordinates for the QP four-completion gate.

Fix a primitive ordered endpoint ``gamma=(c,C)`` and choose ``u,v`` with

    c*u - C*v = 1.

The two unimodular maps in this module send a centre pair ``(b,B)`` and an
endpoint pair ``(d,E)`` to tokens ``P=(delta,n)`` and ``R=(h,m)``.  In these
coordinates the middle transition determinant is exactly ``det(P,R)`` and
the sum of its two coordinate products is one fixed determinant-minus-one
bilinear form.  Thus the two physical hard windows become one exact diamond.

Nothing here completes an actual mask to a box.  The maps are bijections of
``Z^2`` and the hard-window predicate is checked before and after the lift.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


Pair = tuple[int, int]


def det(left: Pair, right: Pair) -> int:
    """Return the oriented two-dimensional determinant."""

    return left[0] * right[1] - left[1] * right[0]


@dataclass(frozen=True)
class BezoutTokenChart:
    """One primitive fixed-endpoint token chart."""

    c: int
    C: int
    u: int
    v: int

    @classmethod
    def canonical(cls, c: int, C: int) -> "BezoutTokenChart":
        """Choose the representative ``0 <= u < C`` of ``c*u=1 (mod C)``."""

        if c <= 0 or C <= 1 or gcd(c, C) != 1:
            raise ValueError("the endpoint coordinates must be positive and primitive")
        u = pow(c, -1, C)
        v = (c * u - 1) // C
        return cls(c=c, C=C, u=u, v=v)

    def __post_init__(self) -> None:
        if self.c * self.u - self.C * self.v != 1:
            raise ValueError("the supplied coefficients are not Bezout coefficients")

    @property
    def form_matrix(self) -> tuple[Pair, Pair]:
        """The symmetric determinant-minus-one form for product sums."""

        cross = self.c * self.u + self.C * self.v
        return ((-2 * self.u * self.v, cross), (cross, -2 * self.c * self.C))

    @property
    def form_determinant(self) -> int:
        matrix = self.form_matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    def center_to_token(self, center: Pair) -> Pair:
        """Lift ``(b,B)`` to ``P=(c*b-C*B, n)`` without multiplicity."""

        b, B = center
        delta = self.c * b - self.C * B
        numerator = self.u * delta - b
        if numerator % self.C:
            raise AssertionError("the centre lift lost integrality")
        n = numerator // self.C
        token = (delta, n)
        if self.token_to_center(token) != center:
            raise AssertionError("the centre token map is not inverse")
        return token

    def token_to_center(self, token: Pair) -> Pair:
        delta, n = token
        return self.u * delta - self.C * n, self.v * delta - self.c * n

    def endpoint_to_token(self, endpoint: Pair) -> Pair:
        """Lift ``(d,E)`` to ``R=(C*d-c*E, m)`` without multiplicity."""

        d, E = endpoint
        h = self.C * d - self.c * E
        numerator = E + self.u * h
        if numerator % self.C:
            raise AssertionError("the endpoint lift lost integrality")
        m = numerator // self.C
        token = (h, m)
        if self.token_to_endpoint(token) != endpoint:
            raise AssertionError("the endpoint token map is not inverse")
        return token

    def token_to_endpoint(self, token: Pair) -> Pair:
        h, m = token
        return -self.v * h + self.c * m, -self.u * h + self.C * m

    def bilinear(self, left: Pair, right: Pair) -> int:
        """Evaluate the product-sum form ``left^T K right``."""

        matrix = self.form_matrix
        return (
            left[0] * (matrix[0][0] * right[0] + matrix[0][1] * right[1])
            + left[1] * (matrix[1][0] * right[0] + matrix[1][1] * right[1])
        )

    def gram_ledger(self, center: Pair, endpoint: Pair) -> "TokenGramLedger":
        """Verify the determinant-minus-one Gram/Pluecker identity.

        In physical coordinates the identity is only

            (bd+BE)^2 - 4*b*B*d*E = (bd-BE)^2.

        Recording both forms makes clear that it is lossless but does not
        create a new divisor constraint after either physical leg is projected
        away.
        """

        left = self.center_to_token(center)
        right = self.endpoint_to_token(endpoint)
        cross = self.bilinear(left, right)
        left_norm = self.bilinear(left, left)
        right_norm = self.bilinear(right, right)
        area = det(left, right)
        if left_norm != -2 * center[0] * center[1]:
            raise AssertionError("the left token norm is not the physical product")
        if right_norm != -2 * endpoint[0] * endpoint[1]:
            raise AssertionError("the right token norm is not the physical product")
        if cross * cross - left_norm * right_norm != area * area:
            raise AssertionError("the token Gram identity failed")
        return TokenGramLedger(
            center_token=left,
            endpoint_token=right,
            cross=cross,
            left_norm=left_norm,
            right_norm=right_norm,
            area=area,
        )

    def transition_ledger(self, center: Pair, endpoint: Pair) -> "TokenTransitionLedger":
        left = self.center_to_token(center)
        right = self.endpoint_to_token(endpoint)
        physical_difference = center[0] * endpoint[0] - center[1] * endpoint[1]
        physical_sum = center[0] * endpoint[0] + center[1] * endpoint[1]
        token_difference = det(left, right)
        token_sum = self.bilinear(left, right)
        if physical_difference != token_difference or physical_sum != token_sum:
            raise AssertionError("the token transition identities failed")
        return TokenTransitionLedger(
            center=center,
            endpoint=endpoint,
            center_token=left,
            endpoint_token=right,
            physical_difference=physical_difference,
            token_difference=token_difference,
            physical_sum=physical_sum,
            token_sum=token_sum,
        )


@dataclass(frozen=True)
class TokenTransitionLedger:
    center: Pair
    endpoint: Pair
    center_token: Pair
    endpoint_token: Pair
    physical_difference: int
    token_difference: int
    physical_sum: int
    token_sum: int


@dataclass(frozen=True)
class TokenGramLedger:
    center_token: Pair
    endpoint_token: Pair
    cross: int
    left_norm: int
    right_norm: int
    area: int


def hard_pair_residuals(q: int, row: int, center: Pair, endpoint: Pair) -> Pair:
    """Return the two literal cubic residuals for one transition edge."""

    target = q**3
    return (
        8 * row * center[0] * endpoint[0] - target,
        8 * row * center[1] * endpoint[1] - target,
    )


def hard_pair_diamond(q: int, row: int, product_sum: int, product_difference: int) -> int:
    """Return the exact maximum of the two hard-window residual magnitudes.

    The equality used is ``max(|X|,|Y|)=|(X+Y)/2|+|(X-Y)/2|``.
    """

    return abs(4 * row * product_sum - q**3) + 4 * row * abs(product_difference)


def verify_hard_pair_diamond(
    q: int, D: int, row: int, chart: BezoutTokenChart, center: Pair, endpoint: Pair
) -> bool:
    """Check exact equivalence of the two physical windows and token diamond."""

    ledger = chart.transition_ledger(center, endpoint)
    residuals = hard_pair_residuals(q, row, center, endpoint)
    diamond = hard_pair_diamond(
        q, row, ledger.token_sum, ledger.token_difference
    )
    if max(map(abs, residuals)) != diamond:
        raise AssertionError("the physical and token hard-window heights differ")
    return (max(map(abs, residuals)) <= q * D) == (diamond <= q * D)


def principal_adjacent_relaxation(middle: int, length: int) -> tuple[
    BezoutTokenChart, tuple[Pair, ...], tuple[Pair, ...]
]:
    """Return the sharp ``D^2`` determinant-only relaxation.

    For ``gamma=(M,M+1)`` the tokens are

        P_r=(r,r-1),       R_s=(s,s+1),

    and every cross determinant equals ``r+s``.  The corresponding physical
    vectors stay in a narrow integer shell, but no row/product mask is asserted.
    """

    if middle <= 2 * length + 2 or length < 1:
        raise ValueError("the physical relaxation must stay positive")
    chart = BezoutTokenChart.canonical(middle, middle + 1)
    centers = tuple((middle + 1 - r, middle - r) for r in range(1, length + 1))
    endpoints = tuple((middle + s, middle + 1 + s) for s in range(1, length + 1))
    for index, center in enumerate(centers, 1):
        if chart.center_to_token(center) != (index, index - 1):
            raise AssertionError("unexpected principal centre token")
    for index, endpoint in enumerate(endpoints, 1):
        if chart.endpoint_to_token(endpoint) != (index, index + 1):
            raise AssertionError("unexpected principal endpoint token")
    return chart, centers, endpoints


def principal_middle_product_residual(middle: int, r: int, s: int) -> tuple[int, int]:
    """Return the affine row and exact unscaled first-product residual.

    Put ``A=r-1``.  For the principal vectors

        b=M-A, d=M+s, x=M+A-s,

    one has

        x*b*d-M^3 = -M*(A^2-A*s+s^2)+A*s*(s-A).
    """

    A = r - 1
    row = middle + A - s
    residual = row * (middle - A) * (middle + s) - middle**3
    closed = -middle * (A * A - A * s + s * s) + A * s * (s - A)
    if residual != closed:
        raise AssertionError("the principal quadratic residual identity failed")
    return row, residual


def principal_survivor_bound(D: int) -> int:
    """A coarse ``O(D)`` lattice bound for the exact principal hard chart.

    Under ``M >= 16*D^2``, any principal pair with ``1<=r,s<=D`` which has
    an integer row in the first physical hard window must obey

        (r-1)^2-(r-1)*s+s^2 <= 5D/16.

    This routine returns the number of nonnegative lattice pairs satisfying
    that necessary ellipse condition.
    """

    if D < 1:
        return 0
    return sum(
        1
        for A in range(D)
        for s in range(1, D + 1)
        if 16 * (A * A - A * s + s * s) <= 5 * D
    )
