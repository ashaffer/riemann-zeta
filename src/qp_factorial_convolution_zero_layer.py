"""Exact zero-layer obstruction to the broad factorial-convolution route.

For a hard product window put

    I_c = {n > 0 : |8*c*n-q**3| <= H}.

The direct four-cycle matrix only samples ``n=a*b`` with both factors in
the shell.  A tempting majorant extends ``f(n)=z_c`` to every integer in
the disjoint union of the ``I_c`` and bounds its off-diagonal
multiplicative energy.  This module records an exact full-integer
counterexample to that stronger estimate.

Choose coprime ``u<v`` and two nearby scales ``g,h``.  The four colors

    u*g, v*g, v*h, u*h

have equal opposite products.  For

    A in J_g = {A : |8*u*v*g*A-q**3| <= H},
    B in J_h = {B : |8*u*v*h*B-q**3| <= H},

the four supported integers satisfy

    (v*A)*(u*B) = (u*A)*(v*B).

Both ``J`` intervals have order ``H/q`` elements when ``g,h`` are of
order ``q``.  At ``H=q*D`` this gives order ``D**2`` factorial
off-diagonal collisions on four fixed colors.  The construction lies in
the equal-color-product (determinant zero) layer and is fully compatible
with the residual rigidity condition ``2*H**2<q**3``.

This is a diagnostic for the proposed *majorant*.  Most of its integers
need not factor into two shell nodes, so it is not a counterexample to the
original direct four-cycle bound.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


def _ceil_div(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


@dataclass(frozen=True)
class IntegerInterval:
    """A closed interval of integers."""

    lower: int
    upper: int

    @property
    def count(self) -> int:
        return max(0, self.upper - self.lower + 1)

    def intersection_count(self, other: "IntegerInterval") -> int:
        return max(0, min(self.upper, other.upper) - max(self.lower, other.lower) + 1)


def multiplier_interval(q: int, residual_half_width: int, multiplier: int) -> IntegerInterval:
    """Return ``{A>0: |8*multiplier*A-q**3|<=H}`` exactly."""

    if q <= 0 or residual_half_width < 0 or multiplier <= 0:
        raise ValueError("q and multiplier must be positive and H nonnegative")
    target = q**3
    denominator = 8 * multiplier
    lower = max(1, _ceil_div(target - residual_half_width, denominator))
    upper = (target + residual_half_width) // denominator
    return IntegerInterval(lower=lower, upper=upper)


def in_product_window(q: int, residual_half_width: int, color: int, value: int) -> bool:
    """Test membership in the exact hard interval ``I_color``."""

    return value > 0 and abs(8 * color * value - q**3) <= residual_half_width


def equal_product_residual_rigidity(
    q: int,
    residuals: tuple[int, int, int, int],
) -> bool:
    """Replay the equal-color-product residual multiset lemma.

    The input order is ``(r1,r2,r3,r4)``.  If

    ``(Q+r1)(Q+r2)=(Q+r3)(Q+r4)`` and ``2*H**2<Q``, where
    ``H=max |ri|``, then the two residual pairs agree as multisets.

    The function raises when either hypothesis is absent and returns the
    asserted multiset equality otherwise.
    """

    if q <= 0:
        raise ValueError("q must be positive")
    r1, r2, r3, r4 = residuals
    target = q**3
    height = max(abs(value) for value in residuals)
    if 2 * height * height >= target:
        raise ValueError("the sub-square-root residual hypothesis fails")
    if (target + r1) * (target + r2) != (target + r3) * (target + r4):
        raise ValueError("the two residual products are unequal")
    return sorted((r1, r2)) == sorted((r3, r4))


@dataclass(frozen=True)
class ProportionalDilateObstruction:
    """Exact ledger for the determinant-zero factorial block."""

    q: int
    residual_half_width: int
    u: int
    v: int
    g: int
    h: int
    colors: tuple[int, int, int, int]
    first_multipliers: IntegerInterval
    second_multipliers: IntegerInterval
    off_diagonal_parameter_pairs: int

    @property
    def color_determinant(self) -> int:
        c1, c2, c3, c4 = self.colors
        return c1 * c2 - c3 * c4

    @property
    def flat_unit_vector_energy_lower_bound(self) -> float:
        """Contribution for weight ``1/2`` on each of four colors."""

        return self.off_diagonal_parameter_pairs / 16.0

    def collision(self, first: int, second: int) -> tuple[int, int, int, int]:
        """Return ``(v*A,u*B,u*A,v*B)`` after exact validation."""

        if not self.first_multipliers.lower <= first <= self.first_multipliers.upper:
            raise ValueError("first multiplier lies outside J_g")
        if not self.second_multipliers.lower <= second <= self.second_multipliers.upper:
            raise ValueError("second multiplier lies outside J_h")
        values = (self.v * first, self.u * second, self.u * first, self.v * second)
        for color, value in zip(self.colors, values, strict=True):
            if not in_product_window(self.q, self.residual_half_width, color, value):
                raise AssertionError("constructed value missed its product window")
        if values[0] * values[1] != values[2] * values[3]:
            raise AssertionError("constructed products differ")
        return values


def proportional_dilate_obstruction(
    q: int,
    residual_half_width: int,
    *,
    u: int,
    v: int,
    g: int,
    h: int,
) -> ProportionalDilateObstruction:
    """Build the exact four-color obstruction.

    The caller controls shell placement.  We require coprime ``u<v``,
    distinct positive ``g,h``, and four distinct colors.  The colors are
    ordered to match the collision tuple:

    ``(u*g, v*h, v*g, u*h)``.
    """

    if min(q, u, v, g, h) <= 0 or residual_half_width < 0:
        raise ValueError("all scales must be positive and H nonnegative")
    if not u < v or math.gcd(u, v) != 1:
        raise ValueError("u<v must be coprime")
    if g == h:
        raise ValueError("g and h must be distinct")
    colors = (u * g, v * h, v * g, u * h)
    if len(set(colors)) != 4:
        raise ValueError("the four colors must be distinct")
    first = multiplier_interval(q, residual_half_width, u * v * g)
    second = multiplier_interval(q, residual_half_width, u * v * h)
    overlap = first.intersection_count(second)
    off_diagonal = first.count * second.count - overlap
    answer = ProportionalDilateObstruction(
        q=q,
        residual_half_width=residual_half_width,
        u=u,
        v=v,
        g=g,
        h=h,
        colors=colors,
        first_multipliers=first,
        second_multipliers=second,
        off_diagonal_parameter_pairs=off_diagonal,
    )
    if answer.color_determinant != 0:
        raise AssertionError("the opposite color products should agree")
    return answer


def consecutive_shell_scales(
    q: int,
    width: float,
    *,
    u: int,
    v: int,
) -> tuple[int, int]:
    """Choose consecutive ``g,h`` putting ``u*g,v*g,u*h,v*h`` in the shell.

    Such scales exist for all sufficiently large ``q`` whenever
    ``log(v/u)<2*width``.  Floating point is used only to choose this finite
    diagnostic fixture; exact shell membership is checked before return.
    """

    if q <= 0 or width <= 0 or min(u, v) <= 0:
        raise ValueError("invalid shell parameters")
    if not u < v or math.gcd(u, v) != 1:
        raise ValueError("u<v must be coprime")
    if math.log(v / u) >= 2 * width:
        raise ValueError("the fixed ratio does not fit in the shell")
    shell_lower = 0.5 * q * math.exp(-width)
    shell_upper = 0.5 * q * math.exp(width)
    lower_scale = math.ceil(shell_lower / u)
    upper_scale = math.floor(shell_upper / v)
    for g in range(lower_scale, upper_scale):
        h = g + 1
        colors = (u * g, v * g, u * h, v * h)
        if len(set(colors)) == 4 and all(shell_lower < c < shell_upper for c in colors):
            return g, h
    raise ValueError("q is too small to contain two suitable consecutive scales")
