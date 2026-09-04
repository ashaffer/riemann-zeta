"""Exact ledgers for the coupled cusp/Fejer inverse reduction.

This module records three pieces used in the companion report:

* the centered rational normal form of the two-inverse phase;
* the concrete triangular Fourier coefficients of a normalized Fejer mask;
* the exact exponent region disposed of by a one-product divisor count.

It is a reduction and inverse theorem, not a proof of the remaining compact
core estimate.
"""

from __future__ import annotations

import cmath
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import ceil, gcd, isqrt
from typing import Mapping


Q_POWER_IN_D = Fraction(33, 16)
H_POWER_IN_D = Fraction(17, 16)
TAIL_MASK_POWER_IN_D = Fraction(1, 4)
BALANCED_CORE_POWER_IN_D = Fraction(1, 6)


@dataclass(frozen=True)
class ReducedSymmetricCuspData:
    """Primitive coordinates for one integral symmetric-cusp point."""

    Q: int
    y: int
    r: int
    s: int
    e: int
    f: int
    rho: int
    kappa: int
    sigma: int
    tau: int
    g: int
    p: int
    d: int
    n: int
    L: int
    T: int


@dataclass(frozen=True)
class SymmetricCuspHostileScan:
    """Finite diagnostic counts for the corrected cusp decomposition."""

    Q: int
    A: int
    B: int
    y_limit: int
    total: int
    common_product: int
    exact_cusp: int
    translated_tangent: int
    remote_minor: int
    minimum_remote_rho: int | None
    minimum_remote_p: int | None


@dataclass(frozen=True)
class RemoteDirectionClusterScan:
    """Multiplicity diagnostics after the proved major-arc deletions."""

    Q: int
    A: int
    B: int
    y_limit: int
    remote_points: int
    distinct_directions: int
    maximum_direction_multiplicity: int
    distinct_denominators: int
    maximum_denominator_multiplicity: int
    distinct_contents: int
    maximum_content_multiplicity: int
    farey_moderate_points: int
    farey_hard_points: int
    farey_target_extension_points: int
    farey_unresolved_points: int


def reduced_symmetric_cusp_data(
    Q: int, y: int, r: int, s: int
) -> ReducedSymmetricCuspData:
    """Return and verify the primitive ``(g,p,d,n,T)`` cusp coordinates.

    For a nonsingular point put ``g=gcd(rho,kappa)``,
    ``rho=g*p``, ``kappa=g*d``, and ``tau=g*n``.  Then

    ``p*y-Q*d=n``

    and the cubic has the exact square-content factorization

    ``L=g^2*T``, ``T=g*p*(p^2-d^2)-2*Q*d^2``.
    """

    raw = symmetric_cusp_error_cubic(Q, y, r, s)
    rho, kappa = raw["rho"], raw["kappa"]
    if rho == 0 and kappa == 0:
        g = p = d = n = T = 0
    else:
        g = gcd(abs(rho), abs(kappa))
        if g == 0:
            raise AssertionError("a nonsingular point must have positive content")
        p, d = rho // g, kappa // g
        assert gcd(p, abs(d)) == 1
        assert raw["tau"] % g == 0
        n = raw["tau"] // g
        assert p * y - Q * d == n
        T = g * p * (p * p - d * d) - 2 * Q * d * d
        assert raw["cubic"] == g * g * T
        assert Q * T == (
            raw["sigma"] * p * p
            + n * d * (g * p + 4 * Q)
            + 2 * n * n
        )
    return ReducedSymmetricCuspData(
        Q=Q,
        y=y,
        r=r,
        s=s,
        e=raw["e"],
        f=raw["f"],
        rho=rho,
        kappa=kappa,
        sigma=raw["sigma"],
        tau=raw["tau"],
        g=g,
        p=p,
        d=d,
        n=n,
        L=raw["cubic"],
        T=T,
    )


def translated_tangent_minor_fixture(y: int) -> tuple[int, int, int, ReducedSymmetricCuspData]:
    """Return the exact ``r=s=1`` counterexample to a pure volume term.

    Put ``Q=y*(y-1)``.  Then ``e=0``, ``f=-2y``, while both reduced
    minor-arc invariants are nonzero: ``n=y`` and ``L=8``.  Taking
    ``A=ceil(Q^(16/33))`` and ``B=2y`` places the example in the Fejer
    compact core, but ``A*B/Q=Q^(-1/66+o(1))``.  Thus a proposed bound
    containing only ``A*B/Q`` (with no additive term) is false.
    """

    if y < 4:
        raise ValueError("require y>=4")
    Q = y * (y - 1)
    A = ceil(Q ** (16.0 / 33.0))
    B = 2 * y
    data = reduced_symmetric_cusp_data(Q, y, 1, 1)
    assert data.e == 0 and data.f == -B
    assert (data.g, data.p, data.d, data.n, data.L, data.T) == (
        2,
        1,
        0,
        y,
        8,
        2,
    )
    assert A <= B < Q
    return Q, A, B, data


def shifted_three_reciprocal_content_centres(
    Q: int, p: int, d: int, n: int
) -> dict[str, Fraction]:
    """Return the unshifted and exact ``n``-shifted cusp-content centres.

    The unshifted centre has the exact three-reciprocal form

    ``2Q*d^2/[p*(p^2-d^2)] = Q/(p-d)+Q/(p+d)-2Q/p``.

    Substituting ``y=(Qd+n)/p`` into the narrow first product band gives
    the shifted centre recorded below.  Its difference from the unshifted
    value is retained exactly; dropping it is not justified in the remote
    gate.
    """

    if Q <= 0 or p <= 0 or abs(d) >= p or gcd(p, abs(d)) != 1:
        raise ValueError("require Q,p>0, |d|<p, and gcd(p,d)=1")
    if Q * (p + d) + n == 0:
        raise ValueError("shifted denominator cannot vanish")
    unshifted = Fraction(2 * Q * d * d, p * (p * p - d * d))
    reciprocal = Fraction(Q, p - d) + Fraction(Q, p + d) - Fraction(2 * Q, p)
    shifted = Fraction(
        2 * (Q * d + n) ** 2,
        p * (p - d) * (Q * (p + d) + n),
    )
    perturbation = Fraction(
        2 * n * (Q * d * (2 * p + d) + n * (p + d)),
        p * (p * p - d * d) * (Q * (p + d) + n),
    )
    assert unshifted == reciprocal
    assert shifted - unshifted == perturbation
    return {
        "unshifted": unshifted,
        "reciprocal": reciprocal,
        "shifted": shifted,
        "perturbation": perturbation,
    }


def narrow_shift_square_count_majorant(Q: int, A: int, R: int) -> int:
    """Elementary majorant for points with ``0<=r<=R``.

    From ``e=r*(Q+y)-y^2`` one has

    ``|(2y-r)^2-(r^2+4Qr)|<=4A``.

    Summing the square-spacing bound over ``1<=r<=R`` gives

    ``O(sqrt(A)+R+A*sqrt(R/Q))``.

    This function returns a concrete ceiling with a deliberately generous
    absolute constant; the report records the asymptotic lemma.
    """

    if min(Q, A) <= 0 or R < 0 or A * 2 > Q:
        raise ValueError("require Q,A>0, R>=0, and 2A<=Q")
    return 8 * (
        1
        + isqrt(A)
        + R
        + ceil(A * (R / Q) ** 0.5)
    )


def symmetric_shift_packet_majorant(Q: int, A: int, B: int) -> int:
    """Concrete ceiling for the positive-shift packet ``r=s=t>0``.

    The omitted singular shift ``t=0`` is the common-product packet and
    contributes ``O(sqrt(A))`` separately.  For ``t>0`` the two bands imply

    ``t*|y|<=B`` and ``|y^2-tQ|<=B``.

    Hence ``t<<B^(2/3)Q^(-1/3)`` and square spacing gives

    ``#(t,y)<<1+B^(2/3)Q^(-1/3)+B^(4/3)Q^(-2/3)``.

    In the compact Fejer core, ``B<=A^(3/8)*sqrt(Q)``, so this is
    ``O(1+sqrt(A))``.
    """

    if min(Q, A, B) <= 0 or A > B or B * 4 > Q:
        raise ValueError("require 0<A<=B<=Q/4")
    first = ceil(B ** (2.0 / 3.0) / Q ** (1.0 / 3.0))
    second = ceil(B ** (4.0 / 3.0) / Q ** (2.0 / 3.0))
    return 16 * (1 + first + second)


def compact_cusp_exponent_ledger() -> dict[str, Fraction]:
    """Powers behind the corrected cusp major/minor decomposition."""

    return {
        "Q_in_D": Fraction(33, 16),
        "counterexample_A_in_D": Fraction(1),
        "counterexample_B_in_D": Fraction(33, 32),
        "counterexample_mM2_in_D": Fraction(1, 16),
        "counterexample_volume_in_D": Fraction(-1, 32),
        "counterexample_volume_in_Q": Fraction(-1, 66),
        "max_A_in_D": Fraction(7, 6),
        "max_B_in_D": Fraction(5, 4),
        "remote_r_floor_in_D": Fraction(1, 2),
        "remote_y_floor_in_D": Fraction(41, 32),
        "remote_primitive_p_floor_in_D": Fraction(13, 48),
        "energy_max_m_in_D": Fraction(1, 10),
        "energy_max_M_in_D": Fraction(1, 6),
        "energy_max_A_in_D": Fraction(11, 10),
        "energy_max_B_in_D": Fraction(7, 6),
        "energy_remote_p_floor_in_D": Fraction(43, 144),
        "energy_B4over3_over_Q_in_D": Fraction(-73, 144),
        "energy_A_over_Q2over3_in_D": Fraction(-11, 40),
        "energy_p2_over_sqrtA_in_D": Fraction(11, 120),
        "energy_p4_over_H_in_D": Fraction(19, 144),
    }


def hostile_symmetric_cusp_scan(
    Q: int, A: int, B: int, y_limit: int | None = None
) -> SymmetricCuspHostileScan:
    """Exhaust a finite symmetric product window using exact integers.

    The output is diagnostic only.  Categories are disjoint and ordered as
    common product (``n=0``), exact cusp (``L=0``), translated tangent
    (``kappa=0``), and the surviving remote minor sector.
    """

    if min(Q, A, B) <= 0 or A > B or 2 * B >= Q:
        raise ValueError("require 0<A<=B<Q/2")
    if y_limit is None:
        y_limit = Q // 3
    if y_limit < 0 or y_limit * 2 >= Q:
        raise ValueError("require 0<=y_limit<Q/2")

    categories = {
        "common_product": 0,
        "exact_cusp": 0,
        "translated_tangent": 0,
        "remote_minor": 0,
    }
    remote_rho: list[int] = []
    remote_p: list[int] = []

    def candidates(numerator: int, denominator: int, width: int) -> tuple[int, ...]:
        lower = numerator // denominator
        return tuple(
            value
            for value in (lower, lower + 1)
            if abs(value * denominator - numerator) <= width
        )

    for y in range(-y_limit, y_limit + 1):
        square = y * y
        for r in candidates(square, Q + y, A):
            for s in candidates(square, Q - y, B):
                data = reduced_symmetric_cusp_data(Q, y, r, s)
                if data.n == 0:
                    categories["common_product"] += 1
                elif data.L == 0:
                    categories["exact_cusp"] += 1
                elif data.kappa == 0:
                    categories["translated_tangent"] += 1
                else:
                    categories["remote_minor"] += 1
                    remote_rho.append(data.rho)
                    remote_p.append(data.p)
    total = sum(categories.values())
    return SymmetricCuspHostileScan(
        Q=Q,
        A=A,
        B=B,
        y_limit=y_limit,
        total=total,
        common_product=categories["common_product"],
        exact_cusp=categories["exact_cusp"],
        translated_tangent=categories["translated_tangent"],
        remote_minor=categories["remote_minor"],
        minimum_remote_rho=min(remote_rho, default=None),
        minimum_remote_p=min(remote_p, default=None),
    )


def hostile_remote_direction_cluster_scan(
    Q: int, A: int, B: int, y_limit: int | None = None
) -> RemoteDirectionClusterScan:
    """Group strict remote points by primitive direction, denominator, and content.

    This is a finite diagnostic, not an asymptotic proof.  The strict remote
    proxy deletes ``n=0``, ``L=0``, and ``kappa=0`` and also requires
    ``rho^3>Q`` and ``r^2>A``.  The Farey split is the exact integer test
    ``g*p^5<=Q`` used by the moderate-height lemma in the companion report.
    """

    if min(Q, A, B) <= 0 or A > B or 2 * B >= Q:
        raise ValueError("require 0<A<=B<Q/2")
    if y_limit is None:
        y_limit = Q // 3
    if y_limit < 0 or y_limit * 2 >= Q:
        raise ValueError("require 0<=y_limit<Q/2")

    directions: Counter[tuple[int, int]] = Counter()
    denominators: Counter[int] = Counter()
    contents: Counter[int] = Counter()
    moderate = 0
    hard = 0
    target_extension = 0
    unresolved = 0

    def candidates(numerator: int, denominator: int, width: int) -> tuple[int, ...]:
        lower = numerator // denominator
        return tuple(
            value
            for value in (lower, lower + 1)
            if abs(value * denominator - numerator) <= width
        )

    for y in range(-y_limit, y_limit + 1):
        square = y * y
        for r in candidates(square, Q + y, A):
            for s in candidates(square, Q - y, B):
                data = reduced_symmetric_cusp_data(Q, y, r, s)
                if (
                    data.n == 0
                    or data.L == 0
                    or data.kappa == 0
                    or data.rho**3 <= Q
                    or data.r * data.r <= A
                ):
                    continue
                directions[(data.p, data.d)] += 1
                denominators[data.p] += 1
                contents[data.g] += 1
                if data.g * data.p**5 <= Q:
                    moderate += 1
                else:
                    hard += 1
                    if data.g * data.p**5 * Q <= (Q + A * B) ** 2:
                        target_extension += 1
                    else:
                        unresolved += 1

    count = sum(directions.values())
    return RemoteDirectionClusterScan(
        Q=Q,
        A=A,
        B=B,
        y_limit=y_limit,
        remote_points=count,
        distinct_directions=len(directions),
        maximum_direction_multiplicity=max(directions.values(), default=0),
        distinct_denominators=len(denominators),
        maximum_denominator_multiplicity=max(denominators.values(), default=0),
        distinct_contents=len(contents),
        maximum_content_multiplicity=max(contents.values(), default=0),
        farey_moderate_points=moderate,
        farey_hard_points=hard,
        farey_target_extension_points=target_extension,
        farey_unresolved_points=unresolved,
    )


def normalized_fejer_coefficients(
    order: int, scale: Fraction = Fraction(1)
) -> dict[int, Fraction]:
    """Fourier coefficients of ``scale*F_order/order``.

    Here ``F_N(theta)=N^(-1)|sum_(j<N)e(j theta)|^2`` has height ``N``.
    Therefore ``F_N/N`` has height one, mean ``1/N``, triangular
    coefficients, and squared reciprocal-distance decay.
    """

    if order <= 0 or scale <= 0:
        raise ValueError("order and scale must be positive")
    return {
        h: scale * Fraction(order - abs(h), order * order)
        for h in range(-order + 1, order)
    }


def fejer_coefficient_ledgers(
    coefficients: Mapping[int, Fraction],
) -> dict[str, Fraction]:
    """Return exact ``l1``, squared ``l2``, mean, and peak ledgers."""

    if not coefficients:
        raise ValueError("coefficients cannot be empty")
    mean = coefficients.get(0, Fraction(0))
    l1 = sum(abs(value) for value in coefficients.values())
    l2_squared = sum(value * value for value in coefficients.values())
    peak = sum(coefficients.values())
    return {"mean": mean, "l1": l1, "l2_squared": l2_squared, "peak": peak}


def centered_rational_phase_parts(
    C: int, Q: int, h: int, k: int, m: int, y: int
) -> dict[str, Fraction]:
    """Return the exact centered phase and cusp normal-form pieces.

    Put ``S=2Q``, ``x=Q+y``, ``lambda=C/Q^2``, ``p=h+k`` and ``d=k-h``.
    Then

        C(h/(Q+y)+k/(Q-y))-m(Q+y)

    equals

        Q(lambda*p-m) + (lambda*d-m)y
        + lambda*(Q*p*y^2+d*y^3)/(Q^2-y^2).

    No integrality assumption on ``lambda`` is made.
    """

    if min(C, Q) <= 0 or abs(y) >= Q:
        raise ValueError("require C,Q>0 and |y|<Q")
    lam = Fraction(C, Q * Q)
    p, d = h + k, k - h
    phase = Fraction(C * h, Q + y) + Fraction(C * k, Q - y) - m * (Q + y)
    constant = Q * (lam * p - m)
    linear = (lam * d - m) * y
    residual = lam * Fraction(Q * p * y * y + d * y**3, Q * Q - y * y)
    assert phase == constant + linear + residual
    return {
        "lambda": lam,
        "p": Fraction(p),
        "d": Fraction(d),
        "phase": phase,
        "constant": constant,
        "linear": linear,
        "residual": residual,
    }


def symmetric_cusp_error_cubic(
    Q: int, y: int, r: int, s: int
) -> dict[str, int]:
    """Return the exact integral cusp identities for two product errors.

    At the extremal centre ``C=Q^2, S=2Q`` write

        a=Q+y,       v=Q-y+r,
        S-a=Q-y,     w=Q+y+s.

    Thus the product errors are

        e=(Q+y)v-Q^2=r(Q+y)-y^2,
        f=(Q-y)w-Q^2=s(Q-y)-y^2.

    Put ``rho=r+s``, ``kappa=s-r``, ``sigma=e+f`` and
    ``tau=e-f``.  Direct elimination of ``y`` gives

        y*rho = Q*kappa + tau,
        Q*rho-y*kappa = 2*y^2+sigma,
        Q*(rho^3-kappa^2*(rho+2Q))
          = sigma*rho^2 + tau*kappa*(rho+4Q) + 2*tau^2.

    The last formula identifies the exact arithmetic major-arc cubic; it
    retains the two anisotropic errors rather than replacing them by their
    maximum.
    """

    if Q <= 0 or abs(y) >= Q:
        raise ValueError("require Q>0 and |y|<Q")
    e = r * (Q + y) - y * y
    f = s * (Q - y) - y * y
    rho, kappa = r + s, s - r
    sigma, tau = e + f, e - f
    cubic = rho**3 - kappa * kappa * (rho + 2 * Q)
    cubic_rhs = sigma * rho * rho + tau * kappa * (rho + 4 * Q) + 2 * tau * tau
    assert y * rho == Q * kappa + tau
    assert Q * rho - y * kappa == 2 * y * y + sigma
    assert Q * cubic == cubic_rhs
    return {
        "e": e,
        "f": f,
        "rho": rho,
        "kappa": kappa,
        "sigma": sigma,
        "tau": tau,
        "cubic": cubic,
        "cubic_rhs": cubic_rhs,
    }


def classify_exact_cusp_cubic(Q: int, rho: int, kappa: int) -> dict[str, int | bool | Fraction]:
    """Classify a nonnegative integral point on the exact cusp cubic.

    For ``rho^3=kappa^2(rho+2Q)`` the origin is the singular solution.
    Every solution with ``rho>0`` has the unique form

        rho=h*d^2*p,       kappa=h*d^3,
        gcd(p,d)=1,        h*p*(p^2-d^2)=2Q.

    Conversely these conditions produce a point on the cubic.  A point
    comes from an integral physical displacement ``y`` only if
    ``y=Q*d/p`` is integral.  The factor equation makes clear that exact
    non-tangent major arcs have only divisor-many parameter choices.
    """

    if Q <= 0 or rho < 0:
        raise ValueError("require Q>0 and rho>=0")
    if rho**3 != kappa * kappa * (rho + 2 * Q):
        raise ValueError("the supplied point is not on the exact cusp cubic")
    if rho == 0:
        assert kappa == 0
        return {"singular": True, "rho": 0, "kappa": 0}
    if kappa == 0:
        raise AssertionError("a positive-rho cusp point cannot have kappa=0")

    common = gcd(rho, abs(kappa))
    p, d = rho // common, kappa // common
    assert gcd(p, abs(d)) == 1
    assert common % (d * d) == 0
    h = common // (d * d)
    assert h * p * (p * p - d * d) == 2 * Q
    physical_y = Fraction(Q * d, p)
    return {
        "singular": False,
        "p": p,
        "d": d,
        "h": h,
        "rho": rho,
        "kappa": kappa,
        "physical_y": physical_y,
        "physical": physical_y.denominator == 1 and abs(physical_y) < Q,
    }


def cusp_cubic_from_parameters(Q: int, p: int, d: int, h: int) -> tuple[int, int]:
    """Construct the exact cusp point from its coprime divisor parameters."""

    if Q <= 0 or p <= 0 or h <= 0 or d == 0 or gcd(p, abs(d)) != 1:
        raise ValueError("require Q,p,h>0, d!=0, and gcd(p,d)=1")
    if h * p * (p * p - d * d) != 2 * Q:
        raise ValueError("parameters do not satisfy h*p*(p^2-d^2)=2Q")
    rho, kappa = h * d * d * p, h * d**3
    assert rho**3 == kappa * kappa * (rho + 2 * Q)
    return rho, kappa


def primitive_cusp_lattice_coordinates(
    Q: int, y: int, r: int, s: int
) -> dict[str, int]:
    """Put a noncentral error-labelled cusp point in primitive coordinates.

    If ``g=gcd(rho,kappa)``, ``rho=g*p`` and ``kappa=g*d``, the two exact
    divisibilities which an approximate-major-arc argument must preserve are

        tau=g*n,                 p*y-Q*d=n,
        cubic=g^2*Delta,
        Delta=g*p*(p^2-d^2)-2*Q*d^2.

    In particular, discarding ``tau`` or ``g`` loses genuine arithmetic
    information.  The routine also checks the divided error-cubic identity.
    """

    ledger = symmetric_cusp_error_cubic(Q, y, r, s)
    rho, kappa = ledger["rho"], ledger["kappa"]
    if rho == 0 and kappa == 0:
        raise ValueError("the singular cusp origin has no primitive direction")
    g = gcd(abs(rho), abs(kappa))
    if g == 0:
        raise ValueError("a noncentral point must have a nonzero gcd scale")
    p, d = rho // g, kappa // g
    tau = ledger["tau"]
    assert tau % g == 0
    n = tau // g
    assert p * y - Q * d == n
    delta = g * p * (p * p - d * d) - 2 * Q * d * d
    assert ledger["cubic"] == g * g * delta
    sigma = ledger["sigma"]
    divided_rhs = sigma * p * p + n * d * (g * p + 4 * Q) + 2 * n * n
    assert Q * delta == divided_rhs
    return {
        **ledger,
        "g": g,
        "p": p,
        "d": d,
        "n": n,
        "delta": delta,
        "divided_rhs": divided_rhs,
    }


def cusp_autocorrelation(
    coefficients: Mapping[int, complex], p: int, t: float
) -> complex:
    """Return ``B_p(t)=sum_h c_h c_(p-h)e((p-2h)t)``."""

    total = 0j
    for h, left in coefficients.items():
        right = coefficients.get(p - h)
        if right is not None:
            total += complex(left) * complex(right) * cmath.exp(
                2j * cmath.pi * (p - 2 * h) * t
            )
    return total


def verify_cusp_regrouping(
    coefficients: Mapping[int, complex], A: float, t: float
) -> tuple[complex, complex]:
    """Evaluate both sides of the exact actual-coefficient regrouping.

    The identity is

        P(A-t)P(A+t)=sum_p B_p(t)e(pA),

    where ``P(theta)=sum_h c_h e(h theta)``.
    """

    def polynomial(theta: float) -> complex:
        return sum(
            complex(value) * cmath.exp(2j * cmath.pi * h * theta)
            for h, value in coefficients.items()
        )

    left = polynomial(A - t) * polynomial(A + t)
    support = tuple(coefficients)
    p_min, p_max = 2 * min(support), 2 * max(support)
    right = sum(
        cusp_autocorrelation(coefficients, p, t)
        * cmath.exp(2j * cmath.pi * p * A)
        for p in range(p_min, p_max + 1)
    )
    return left, right


def shifted_reciprocal_determinant_invariance(
    abscissae: tuple[int, int, int], C: int, shift: Fraction
) -> tuple[Fraction, Fraction]:
    """Verify that a common vertical shift does not change the determinant.

    The two returned determinants are for rows ``(1,a,C/a)`` and
    ``(1,a,C/a-shift)``.  This is the algebra behind translated-mask local
    packet rigidity.
    """

    a1, a2, a3 = abscissae
    if min(a1, a2, a3, C) <= 0 or len(set(abscissae)) != 3:
        raise ValueError("positive distinct abscissae and C are required")

    def determinant(values: tuple[Fraction, Fraction, Fraction]) -> Fraction:
        v1, v2, v3 = values
        return (a2 - a1) * (v3 - v1) - (a3 - a1) * (v2 - v1)

    reciprocal = tuple(Fraction(C, a) for a in abscissae)
    shifted = tuple(value - shift for value in reciprocal)
    first = determinant(reciprocal)
    second = determinant(shifted)
    assert first == second
    return first, second


def divisor_mask_contribution_power(
    smaller_mask_power: Fraction, larger_mask_power: Fraction
) -> Fraction:
    """Power of ``D`` in one weighted dyadic mask.

    If ``m=D^u`` and ``M=D^v`` with ``0<=u<=v``, the one-coordinate
    divisor estimate and the two squared Fejer weights give

        D*m/(m^2*M^2) = D^(1-u-2v).

    The mask is therefore already at the square-root target precisely when
    ``u+2v>=1/2``.
    """

    if smaller_mask_power < 0 or larger_mask_power < smaller_mask_power:
        raise ValueError("require 0 <= smaller_mask_power <= larger_mask_power")
    return Fraction(1) - smaller_mask_power - 2 * larger_mask_power


def reciprocal_space_curve_torsion(
    c: Fraction, s: Fraction, t: Fraction
) -> Fraction:
    """Wronskian determinant for ``(t,c/t,c/(s-t))``.

    The determinant of the first three derivative vectors is

        12*c^2*s/(t^4*(s-t)^4),

    so the normalized fixed-sum reciprocal curve has nonzero torsion on a
    positive shell.  This verifies that generic space-curve lattice-point
    theorems are formally applicable; their error exponent is nevertheless
    too large for the compact-core target.
    """

    if c <= 0 or s <= 0 or t <= 0 or t >= s:
        raise ValueError("require c,s>0 and 0<t<s")
    return 12 * c * c * s / (t**4 * (s - t) ** 4)


def coupled_inverse_exponent_ledger() -> dict[str, Fraction]:
    """Return the exact critical powers in the Fejer tail/core split."""

    q, H, alpha = Q_POWER_IN_D, H_POWER_IN_D, TAIL_MASK_POWER_IN_D
    balanced = BALANCED_CORE_POWER_IN_D
    target = Fraction(1, 2)
    # If max(U,V)>=D^alpha, the narrower one-product divisor count gives
    # D/max(U,V)^2 after the Fejer weights.
    divisor_tail = Fraction(1) - 2 * alpha
    # In the core U,V<=D^alpha, the q^(1/3)-arc determinant error is
    # D*U*q^(-2/3).
    local_determinant_error = Fraction(1) + alpha - Fraction(2, 3) * q
    # Huang's generic fixed-denominator space-curve error q^(3/5), compared
    # with the largest possible desired mask bound in u+2v<1/2.
    generic_space_curve_error = Fraction(3, 5) * q
    largest_core_target = Fraction(7, 6)
    gram_target = 2 * H + target
    fejer_rank_one_norm_squared = -2 * H
    return {
        "q": q,
        "H": H,
        "tail_mask": alpha,
        "balanced_core": balanced,
        "target": target,
        "divisor_tail": divisor_tail,
        "local_determinant_error": local_determinant_error,
        "generic_space_curve_error": generic_space_curve_error,
        "largest_core_target": largest_core_target,
        "generic_space_curve_gap": generic_space_curve_error - largest_core_target,
        "gram_operator_target": gram_target,
        "fejer_rank_one_norm_squared": fejer_rank_one_norm_squared,
        "quadratic_form_target": gram_target + fejer_rank_one_norm_squared,
    }
