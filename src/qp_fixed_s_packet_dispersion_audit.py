"""Exact checks for the fixed-S packet-or-dispersion gate.

For a fixed integer centre ``N`` and fixed completion sum ``a+b=S``, write

    a*v = N+e,   b*w = N+f.

The off-resonant normal form is a complementary shifted-divisor problem.
If ``g=gcd(a,b)``, ``a=g*A``, and ``b=g*B``, then ``A+B=S/g`` and
``gcd(A,B)=1``.  Moreover ``A`` divides ``(N+e)/g`` and ``B`` divides
``(N+f)/g``.  When ``e != f``, necessarily ``g | (e-f)``.

This module also stores a small exact physical fixture showing that a
constant multiple of ``sqrt(D)`` scattered carrier sums need not create a
three-point affine packet or even a three-term progression.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd


@dataclass(frozen=True)
class FixedSumRepresentation:
    a: int
    b: int
    v: int
    w: int

    @property
    def S(self) -> int:
        return self.a + self.b

    @property
    def U(self) -> int:
        return self.v + self.w

    def products(self) -> tuple[int, int]:
        return self.a * self.v, self.b * self.w

    def errors(self, center: int) -> tuple[int, int]:
        n, m = self.products()
        return n - center, m - center


@dataclass(frozen=True)
class ComplementaryDivisorData:
    """The exact gcd/complementary-divisor coordinates of one pair."""

    g: int
    T: int
    A: int
    B: int
    n_reduced: int
    m_reduced: int
    e: int
    f: int


def complementary_divisor_data(
    rep: FixedSumRepresentation, center: int
) -> ComplementaryDivisorData:
    """Return and verify the exact shifted-divisor normal form."""

    n, m = rep.products()
    e, f = n - center, m - center
    g = gcd(rep.a, rep.b)
    assert rep.S % g == n % g == m % g == 0
    A, B, T = rep.a // g, rep.b // g, rep.S // g
    n_reduced, m_reduced = n // g, m // g
    assert gcd(A, B) == 1
    assert A + B == T
    assert n_reduced % A == 0
    assert m_reduced % B == 0
    if e != f:
        assert (e - f) % g == 0
    return ComplementaryDivisorData(
        g, T, A, B, n_reduced, m_reduced, e, f
    )


def reconstruct_complementary_divisor(
    data: ComplementaryDivisorData, center: int
) -> FixedSumRepresentation:
    """Reconstruct the unique representation from valid normal-form data."""

    assert data.A + data.B == data.T
    assert gcd(data.A, data.B) == 1
    assert data.n_reduced % data.A == 0
    assert data.m_reduced % data.B == 0
    rep = FixedSumRepresentation(
        data.g * data.A,
        data.g * data.B,
        data.n_reduced // data.A,
        data.m_reduced // data.B,
    )
    assert rep.errors(center) == (data.e, data.f)
    assert gcd(rep.a, rep.b) == data.g
    return rep


def exact_fixed_sum_identities(
    rep: FixedSumRepresentation, center: int
) -> tuple[int, Fraction, Fraction]:
    """Return the exact product and centred identities.

    The first returned value is zero by

        a*b*U = center*S + b*e + a*f.

    The two fractions are the equal sides of

        S*U/4-center-(U/S)h^2 = (e+f)/2-(e-f)h/S,

    where ``h=(a-b)/2``.  Fractions retain the parity cases exactly.
    """

    e, f = rep.errors(center)
    product_residual = (
        rep.a * rep.b * rep.U
        - center * rep.S
        - rep.b * e
        - rep.a * f
    )
    h = Fraction(rep.a - rep.b, 2)
    left = (
        Fraction(rep.S * rep.U, 4)
        - center
        - Fraction(rep.U, rep.S) * h * h
    )
    right = Fraction(e + f, 2) - Fraction(e - f, rep.S) * h
    assert product_residual == 0
    assert left == right
    return product_residual, left, right


def has_nontrivial_three_ap(values: set[int] | list[int]) -> bool:
    vals = set(values)
    for middle in vals:
        for left in vals:
            if left < middle and 2 * middle - left in vals:
                return True
    return False


def has_collinear_triple(points: set[tuple[int, int]]) -> bool:
    ordered = sorted(points)
    for p, q, r in combinations(ordered, 3):
        if (q[1] - p[1]) * (r[0] - p[0]) == (
            r[1] - p[1]
        ) * (q[0] - p[0]):
            return True
    return False


def off_resonant_counterfixture() -> tuple[
    int, int, int, int, tuple[FixedSumRepresentation, ...]
]:
    """Return an exact eight-level, packet-free physical fixture.

    Parameters are ``q=800, D=26, S=2027, N=986978`` and all four
    coordinates lie in ``[q,2q]``.  The eight displayed representatives
    are unordered; adjoining their swaps gives sixteen ordered points and
    carrier-sum multiplicity exactly two on every level.
    """

    q, D, S, center = 800, 26, 2027, 986_978
    reps = (
        FixedSumRepresentation(807, 1220, 1223, 809),
        FixedSumRepresentation(835, 1192, 1182, 828),
        FixedSumRepresentation(859, 1168, 1149, 845),
        FixedSumRepresentation(882, 1145, 1119, 862),
        FixedSumRepresentation(886, 1141, 1114, 865),
        FixedSumRepresentation(908, 1119, 1087, 882),
        FixedSumRepresentation(940, 1087, 1050, 908),
        FixedSumRepresentation(987, 1040, 1000, 949),
    )
    for rep in reps:
        assert rep.S == S
        assert all(q <= z <= 2 * q for z in (rep.a, rep.b, rep.v, rep.w))
        e, f = rep.errors(center)
        assert max(abs(e), abs(f)) <= D
        assert e != f
    return q, D, S, center, reps


def counterfixture_point_set() -> set[tuple[int, int]]:
    """Return both endpoints ``(a,v),(b,w)`` of the counterfixture."""

    _, _, _, _, reps = off_resonant_counterfixture()
    return {
        point
        for rep in reps
        for point in ((rep.a, rep.v), (rep.b, rep.w))
    }


def prime_power_base(value: int) -> int | None:
    """Return the prime base when ``value`` is a prime power.

    The routine is deliberately elementary: it is only an exact replay aid
    for the finite ledgers in this module.
    """

    if value < 2:
        return None
    divisor = 2
    while divisor * divisor <= value and value % divisor:
        divisor = 3 if divisor == 2 else divisor + 2
    if divisor * divisor > value:
        return value
    remainder = value
    while remainder % divisor == 0:
        remainder //= divisor
    return divisor if remainder == 1 else None


def narrow_prime_power_bases(values: tuple[int, ...]) -> tuple[int, ...]:
    """Verify a ratio-``<2`` prime-power shell and return its bases.

    Two different powers of one prime have ratio at least two.  Therefore
    the returned bases are distinct whenever the input values are distinct.
    """

    if not values or min(values) <= 0 or max(values) >= 2 * min(values):
        raise ValueError("require a nonempty positive shell of ratio <2")
    bases = tuple(prime_power_base(value) for value in values)
    if any(base is None for base in bases):
        raise ValueError("every shell value must be a prime power")
    for i, value in enumerate(values):
        for other in values[i + 1 :]:
            if value != other and gcd(value, other) != 1:
                raise AssertionError("distinct shell nodes must be coprime")
    return tuple(int(base) for base in bases)


def shell_factor_orientations(
    product: int, shell: tuple[int, ...]
) -> tuple[tuple[int, int], ...]:
    """Return the ordered shell factorizations of one exact product.

    On a narrow prime-power shell there are at most two: unique
    factorization determines the unordered pair, and only its orientation
    remains free.
    """

    narrow_prime_power_bases(shell)
    shell_set = set(shell)
    answer = tuple(
        (factor, product // factor)
        for factor in shell
        if product % factor == 0 and product // factor in shell_set
    )
    assert len(answer) <= 2
    return answer


@dataclass(frozen=True)
class ActualPrimePowerDefectData:
    """The rigid arithmetic attached to one actual-shell representation."""

    n: int
    m: int
    X: int
    first_residual: int
    second_residual: int
    product_gcd: int
    defect_gcd: int
    residual_gcd: int


def actual_prime_power_defect_data(
    rep: FixedSumRepresentation, q: int, color: int
) -> ActualPrimePowerDefectData:
    """Verify the actual-mask rigidity and the exact project residual gcd.

    All five physical nodes must lie in one ratio-``<2`` prime-power shell.
    If ``0<|a*v-b*w|<min(shell)``, the two product-factor multisets are
    disjoint.  Hence the products and the defect are pairwise coprime, and

    ``gcd(q^3+r, q^3+s)=8*color``

    for ``r=8*color*a*v-q^3`` and ``s=8*color*b*w-q^3``.
    """

    nodes = (color, rep.a, rep.b, rep.v, rep.w)
    narrow_prime_power_bases(nodes)
    n, m = rep.products()
    X = n - m
    first_residual = 8 * color * n - q**3
    second_residual = 8 * color * m - q**3
    if X == 0:
        assert (
            (rep.a == rep.b and rep.v == rep.w)
            or (rep.a == rep.w and rep.v == rep.b)
        )
    elif abs(X) < min(nodes):
        assert {rep.a, rep.v}.isdisjoint({rep.b, rep.w})
        assert gcd(n, m) == 1
        assert gcd(abs(X), n * m) == 1
        assert gcd(rep.a, rep.b) == 1
    residual_gcd = gcd(q**3 + first_residual, q**3 + second_residual)
    assert residual_gcd == 8 * color * gcd(n, m)
    return ActualPrimePowerDefectData(
        n=n,
        m=m,
        X=X,
        first_residual=first_residual,
        second_residual=second_residual,
        product_gcd=gcd(n, m),
        defect_gcd=gcd(abs(X), n * m),
        residual_gcd=residual_gcd,
    )


def exact_center_prime_fixtures() -> tuple[
    tuple[int, int, int, tuple[FixedSumRepresentation, ...]], ...
]:
    """Return exact all-prime fixtures at ``C=q^3/(8*color)``.

    The first fixture is the smallest clean nonzero-defect example used in
    the audit.  The second has two genuinely different nonzero carrier sums
    for one fixed completion sum.  The window test is kept integral by
    multiplying by ``8*color``.
    """

    fixtures = (
        (
            211,
            13,
            113,
            (FixedSumRepresentation(97, 101, 107, 103),),
        ),
        (
            4_951,
            62,
            2_557,
            (
                FixedSumRepresentation(2_399, 2_617, 2_473, 2_267),
                FixedSumRepresentation(2_473, 2_543, 2_399, 2_333),
            ),
        ),
    )
    for q, width, color, reps in fixtures:
        sums = {rep.S for rep in reps}
        assert len(sums) == 1
        for rep in reps:
            data = actual_prime_power_defect_data(rep, q, color)
            assert data.X != 0
            assert abs(data.first_residual) <= 8 * color * width
            assert abs(data.second_residual) <= 8 * color * width
    return fixtures
