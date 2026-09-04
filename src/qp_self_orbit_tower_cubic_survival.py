"""A canonical self-orbit containing the hostile balanced HSM chart.

This module records an exact algebraic family.  It does not prove that the
hostile shifted-cube transition has too many solutions, and it does not
disprove the dyadic reciprocal large sieve.  Its narrower purpose is to
show that canonical-tower integrality does not remove that transition: the
aligned unimodular chart used in its derivation occurs literally inside one
complete integer self-orbit at the critical exponents.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd


Pair = tuple[int, int]


def det(left: Pair, right: Pair) -> int:
    """Return the oriented determinant of two integer vectors."""

    return left[0] * right[1] - left[1] * right[0]


@dataclass(frozen=True)
class CanonicalTowerCubicFixture:
    """Critical-scale parameters for the embedded aligned chart."""

    base: int
    fan_scale: int
    long_scale: int
    q: int
    degree: int
    top_frequency: int
    packet_radius_squared: int
    long_direction: Pair
    short_complement: Pair
    short_packet_direction: Pair
    reflected_anchor: Pair
    anchor: Pair
    packet_remainder: int


def canonical_tower_cubic_fixture(base: int) -> CanonicalTowerCubicFixture:
    r"""Build the exact critical family.

    Put

    ``F=N^8, R=N^25, q=2FR, D=F^2``.

    With ``d=(R,R+1)`` and ``e=(-1,-1)``, one has ``det(d,e)=1`` and

    ``(C,c)=F*d+e=(FR-1,F(R+1)-1)``.

    Thus the primitive anchor is ``(c,C)``.  Its short packet direction is
    ``(1,1)=-e`` and its determinant remainder is exactly ``F``.  Moreover
    ``q/D`` is integral and its natural packet radius has square ``D``.
    """

    N = int(base)
    if N < 2 or N % 2:
        raise ValueError("the base must be an even integer at least two")
    F = N**8
    R = N**25
    q = 2 * F * R
    D = F * F
    d = (R, R + 1)
    e = (-1, -1)
    reflected = (F * R - 1, F * (R + 1) - 1)
    C, c = reflected
    anchor = (c, C)
    short = (1, 1)
    if det(d, e) != 1:
        raise AssertionError("the aligned long/short chart is not unimodular")
    if (F * d[0] + e[0], F * d[1] + e[1]) != reflected:
        raise AssertionError("the reflected anchor decomposition failed")
    if gcd(c, C) != 1:
        raise AssertionError("the canonical anchor is not primitive")
    remainder = c * short[0] - C * short[1]
    if remainder != F:
        raise AssertionError("the short tower remainder is not the fan scale")
    top_frequency = q // D
    if top_frequency * D != q:
        raise AssertionError("the top dyadic frequency is not integral")
    return CanonicalTowerCubicFixture(
        base=N,
        fan_scale=F,
        long_scale=R,
        q=q,
        degree=D,
        top_frequency=top_frequency,
        packet_radius_squared=q // top_frequency,
        long_direction=d,
        short_complement=e,
        short_packet_direction=short,
        reflected_anchor=reflected,
        anchor=anchor,
        packet_remainder=remainder,
    )


def _is_prime_below_2_64(value: int) -> bool:
    """Deterministic Miller--Rabin primality test for ``value < 2^64``."""

    n = int(value)
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if n % prime == 0:
            return n == prime
    odd_part = n - 1
    exponent = 0
    while odd_part % 2 == 0:
        exponent += 1
        odd_part //= 2
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % n == 0:
            continue
        residue = pow(base, odd_part, n)
        if residue in (1, n - 1):
            continue
        for _ in range(exponent - 1):
            residue = residue * residue % n
            if residue == n - 1:
                break
        else:
            return False
    return True


@dataclass(frozen=True)
class ActualPrimeTowerReplay:
    """One finite replay with both anchor coordinates prime."""

    q: int
    degree: int
    fan_scale: int
    long_scale: int
    euclidean_remainder: int
    anchor: Pair
    reflected_anchor: Pair
    long_direction: Pair
    short_complement: Pair
    m_values: range
    n_values: range
    point_count: int
    maximum_absolute_label: int
    labels_are_injective: bool
    lies_in_nine_tenths_eleven_tenths_shell: bool


def actual_prime_tower_replay() -> ActualPrimeTowerReplay:
    r"""Return a finite prime-anchor instance of the same aligned tower.

    The exact data are

    ``C=8000000011, c=8000000221, c-C=210`` and
    ``C=210*38095238+31``.

    Both ``C`` and ``c`` are prime.  In the basis
    ``d=(38095238,38095239)``, ``e=(-1,-1)`` one has

    ``(C,c)=210*d-31*e``

    and the orbit label of ``z=m*d+n*e`` is ``-210*n-31*m``.  The returned
    rectangle is a constant-size balanced all-one subchart.  This is a
    finite compatibility replay only; it is not an asymptotic theorem about
    prime pairs with a prescribed growing gap.
    """

    C = 8_000_000_011
    c = 8_000_000_221
    fan = c - C
    long_scale, remainder = divmod(C, fan)
    d = (long_scale, long_scale + 1)
    e = (-1, -1)
    if not (_is_prime_below_2_64(C) and _is_prime_below_2_64(c)):
        raise AssertionError("the advertised anchor coordinates are not prime")
    if (
        fan * d[0] - remainder * e[0],
        fan * d[1] - remainder * e[1],
    ) != (C, c):
        raise AssertionError("the prime replay tower decomposition failed")
    if det(d, e) != 1:
        raise AssertionError("the prime replay chart is not unimodular")

    # Center the shell at fan*d, only 31 below the prime reflected anchor.
    q = 2 * fan * long_scale
    degree = fan * fan
    m_values = range(190, 231)
    n_values = range(-100, 101)
    labels: set[int] = set()
    maximum_label = 0
    minimum_coordinate: int | None = None
    maximum_coordinate: int | None = None
    for m in m_values:
        for n in n_values:
            b = long_scale * m - n
            B = (long_scale + 1) * m - n
            label = c * b - C * B
            expected = -fan * n - remainder * m
            if label != expected:
                raise AssertionError("the prime replay label identity failed")
            if label in labels:
                raise AssertionError("the prime replay label map is not injective")
            labels.add(label)
            maximum_label = max(maximum_label, abs(label))
            local_min, local_max = min(b, B), max(b, B)
            minimum_coordinate = (
                local_min
                if minimum_coordinate is None
                else min(minimum_coordinate, local_min)
            )
            maximum_coordinate = (
                local_max
                if maximum_coordinate is None
                else max(maximum_coordinate, local_max)
            )
    if minimum_coordinate is None or maximum_coordinate is None:
        raise AssertionError("the prime replay rectangle is empty")
    shell_ok = (
        10 * minimum_coordinate > 9 * (q // 2)
        and 10 * maximum_coordinate < 11 * (q // 2)
    )
    if maximum_label > degree:
        raise AssertionError("the prime replay leaves the short label interval")
    return ActualPrimeTowerReplay(
        q=q,
        degree=degree,
        fan_scale=fan,
        long_scale=long_scale,
        euclidean_remainder=remainder,
        anchor=(c, C),
        reflected_anchor=(C, c),
        long_direction=d,
        short_complement=e,
        m_values=m_values,
        n_values=n_values,
        point_count=len(labels),
        maximum_absolute_label=maximum_label,
        labels_are_injective=len(labels) == len(m_values) * len(n_values),
        lies_in_nine_tenths_eleven_tenths_shell=shell_ok,
    )


def tower_point(fixture: CanonicalTowerCubicFixture, m: int, n: int) -> Pair:
    r"""Return ``z=m*(R,R+1)+n*(-1,-1)``."""

    R = fixture.long_scale
    return R * int(m) - int(n), (R + 1) * int(m) - int(n)


def tower_label(fixture: CanonicalTowerCubicFixture, m: int, n: int) -> int:
    r"""Return and verify the exact self-orbit label ``t=m-F*n``."""

    b, B = tower_point(fixture, m, n)
    c, C = fixture.anchor
    direct = c * b - C * B
    expected = int(m) - fixture.fan_scale * int(n)
    if direct != expected:
        raise AssertionError("the canonical tower label identity failed")
    return direct


def balanced_rectangle_ranges(
    fixture: CanonicalTowerCubicFixture,
) -> tuple[range, range]:
    """Return two intervals of lengths comparable to the fan scale.

    The first interval has length ``F/8< F``.  Consequently the map
    ``(m,n) -> m-F*n`` is injective on the returned rectangle.  For the
    supplied critical family every point also lies in the standard
    ``exp(+-0.2)`` shell and has label of magnitude below ``D``; those
    inequalities are checked by :func:`balanced_rectangle_certificate`.
    """

    F = fixture.fan_scale
    if F % 8:
        raise ValueError("the fan scale must be divisible by eight")
    return range(15 * F // 16, 17 * F // 16), range(F // 4, 3 * F // 4)


@dataclass(frozen=True)
class BalancedRectangleCertificate:
    m_count: int
    n_count: int
    point_count: int
    labels_are_injective: bool
    maximum_absolute_label: int
    all_labels_within_degree: bool
    minimum_coordinate: int
    maximum_coordinate: int
    algebraic_shell_lower_numerator: int
    algebraic_shell_upper_numerator: int
    lies_in_algebraic_nine_tenths_eleven_tenths_shell: bool


def balanced_rectangle_certificate(
    fixture: CanonicalTowerCubicFixture,
) -> BalancedRectangleCertificate:
    """Certify the all-one balanced rectangle without floating point.

    We use the slightly narrower algebraic shell

    ``(9/10)*(q/2) < b,B < (11/10)*(q/2)``.

    For ``R>=32`` this is contained in the project's
    ``exp(+-0.2)`` shell (the latter numerical containment is tested in the
    regression test).  The algebraic inequalities and label injectivity are
    exact.
    """

    F, R, q, D = (
        fixture.fan_scale,
        fixture.long_scale,
        fixture.q,
        fixture.degree,
    )
    m_values, n_values = balanced_rectangle_ranges(fixture)
    labels: set[int] = set()
    minimum_coordinate: int | None = None
    maximum_coordinate: int | None = None
    maximum_label = 0
    for m in m_values:
        for n in n_values:
            point = tower_point(fixture, m, n)
            label = tower_label(fixture, m, n)
            if label in labels:
                raise AssertionError("two rectangle points have the same orbit label")
            labels.add(label)
            maximum_label = max(maximum_label, abs(label))
            local_min = min(point)
            local_max = max(point)
            minimum_coordinate = (
                local_min
                if minimum_coordinate is None
                else min(minimum_coordinate, local_min)
            )
            maximum_coordinate = (
                local_max
                if maximum_coordinate is None
                else max(maximum_coordinate, local_max)
            )
    if minimum_coordinate is None or maximum_coordinate is None:
        raise AssertionError("the balanced rectangle unexpectedly became empty")

    lower_ok = 10 * minimum_coordinate > 9 * (q // 2)
    upper_ok = 10 * maximum_coordinate < 11 * (q // 2)
    return BalancedRectangleCertificate(
        m_count=len(m_values),
        n_count=len(n_values),
        point_count=len(labels),
        labels_are_injective=len(labels) == len(m_values) * len(n_values),
        maximum_absolute_label=maximum_label,
        all_labels_within_degree=maximum_label <= D,
        minimum_coordinate=minimum_coordinate,
        maximum_coordinate=maximum_coordinate,
        algebraic_shell_lower_numerator=10 * minimum_coordinate - 9 * (q // 2),
        algebraic_shell_upper_numerator=11 * (q // 2)
        - 10 * maximum_coordinate,
        lies_in_algebraic_nine_tenths_eleven_tenths_shell=lower_ok and upper_ok,
    )


def embedded_reciprocal_phase(
    fixture: CanonicalTowerCubicFixture,
    first: tuple[int, int],
    second: tuple[int, int],
) -> tuple[Fraction, Fraction]:
    r"""Return the identical orbit and balanced completed-strip phases.

    If ``first=(m,n)`` and ``second=(m',n')``, the physical factors are

    ``b=R*m-n`` and ``B'=(R+1)*m'-n'``.

    This is exactly the completed-strip chart with
    ``(R,S)=(R,R+1)`` and complementary coefficients ``U=V=-1``.
    """

    m, n = map(int, first)
    mp, np = map(int, second)
    first_point = tower_point(fixture, m, n)
    second_point = tower_point(fixture, mp, np)
    orbit_phase = Fraction(
        fixture.q**3, 8 * first_point[0] * second_point[1]
    )
    R = fixture.long_scale
    completed_phase = Fraction(
        fixture.q**3,
        8 * (R * m - n) * ((R + 1) * mp - np),
    )
    if orbit_phase != completed_phase:
        raise AssertionError("the embedded HSM phase identity failed")
    return orbit_phase, completed_phase


def aligned_cubic_beta(
    fixture: CanonicalTowerCubicFixture, input_value: int
) -> tuple[Fraction, Fraction]:
    r"""Return the two identical formulas for the diagonal cubic frequency.

    For the aligned chart the frequency is

    ``beta_u=8*R^2*(R+1)*u^3/q^3
            =((R+1)/R)*(u/F)^3``.

    Thus the canonical tower gives exactly the ``S=R+1`` model used in the
    hostile Fejer-diagonal audit.
    """

    u = int(input_value)
    if u <= 0:
        raise ValueError("the cubic input must be positive")
    F, R, q = fixture.fan_scale, fixture.long_scale, fixture.q
    direct = Fraction(8 * R * R * (R + 1) * u**3, q**3)
    aligned = Fraction(R + 1, R) * Fraction(u, F) ** 3
    if direct != aligned:
        raise AssertionError("the aligned cubic frequency identity failed")
    return direct, aligned


@dataclass(frozen=True)
class AlignedNearCubeResidual:
    multiplier: int
    nearest_integer: int
    input_value: int
    residual: int
    phase_error: Fraction
    normalized_residual: Fraction


def aligned_near_cube_residual(
    fixture: CanonicalTowerCubicFixture,
    multiplier: int,
    nearest_integer: int,
    input_value: int,
) -> AlignedNearCubeResidual:
    r"""Clear denominators in one tower-compatible cubic approximation.

    Exactly,

    ``a*beta_u-b = [a*(R+1)*u^3-b*R*F^3]/(R*F^3)``.

    No extra divisibility has been inserted: this is the standard aligned
    near-cube numerator itself.
    """

    a, b, u = int(multiplier), int(nearest_integer), int(input_value)
    if min(a, u) <= 0:
        raise ValueError("the multiplier and cubic input must be positive")
    F, R = fixture.fan_scale, fixture.long_scale
    beta, _ = aligned_cubic_beta(fixture, u)
    residual = a * (R + 1) * u**3 - b * R * F**3
    direct = a * beta - b
    normalized = Fraction(residual, R * F**3)
    if direct != normalized:
        raise AssertionError("the aligned near-cube clearing identity failed")
    return AlignedNearCubeResidual(
        multiplier=a,
        nearest_integer=b,
        input_value=u,
        residual=residual,
        phase_error=direct,
        normalized_residual=normalized,
    )
