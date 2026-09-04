"""A supported near-zero-dual cloud for the QP completion action.

This module records an exact family of *dual stationary modes*.  It is a
counterexample to an unrestricted assertion that every regular supported
completion-action jet-major-arc ball at correlation threshold ``D^-1/6``
has at most ``D^(1+o(1))`` members.  It is not a family of primal
product-band points, and hence is not a counterexample to a mask-restricted
residual theorem or to the sharp four-cycle bound.

For ``C=Q^2`` and ``S0=2Q``, take coprime opposite-parity ``p,d`` and

    h=(p+d)^2*t,  k=(p-d)^2*(t+1),  m=p^2.

The phase ``F=-m*a+C*h/a+C*k/(S-a)`` is stationary at
``a0=Q*(p+d)/p``.  Its value and first completion derivative are integers,
so both disappear in the physical integer Newton quotient.  The first
visible coordinate is

    Q*J'' = 2*p^3*t*(t+1)/(2*p*t+p+d),

which changes only on the quadratic scale.  A polynomially thick cloud of
such modes therefore defeats a uniform degree cutoff, although a
nonuniform second-derivative Schur sum still controls the cloud.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import ceil, floor, gcd
from typing import Iterable

from qp_stationary_action_jet_rigidity import stationary_action_four_jet


@dataclass(frozen=True)
class NearZeroDualMode:
    """One exact regular member of the canonical near-zero-dual ladder."""

    Q: int
    p: int
    d: int
    t: int
    completion: int
    saddle: Fraction
    complement: Fraction
    h: int
    k: int
    m: int
    action: Fraction
    first: Fraction
    second: Fraction
    third: Fraction
    fourth: Fraction
    tangent_curvature: Fraction

    @property
    def scaled_quadratic_jet(self) -> Fraction:
        """The convenient coordinate ``R=Q*J''``."""

        return self.Q * self.second

    @property
    def tangent_fingerprint(self) -> tuple[int, Fraction]:
        """The ``(chi,K_2)`` part of the lifted tangent fingerprint."""

        return (1, self.tangent_curvature)

    @property
    def maximum_frequency(self) -> int:
        return max(abs(self.h), abs(self.k), abs(self.m))


def canonical_near_zero_dual_mode(Q: int, p: int, d: int, t: int) -> NearZeroDualMode:
    """Construct and exactly verify one canonical supported-mode candidate.

    Requiring ``p`` and ``d`` to have opposite parity makes
    ``gcd(p+d,p-d)=1``.  Positive ``h,k,m`` put the saddle strictly away
    from the endpoint, zero-dual, and fold loci.
    """

    if Q <= 0 or p <= 0 or t <= 0 or not 0 < d < p:
        raise ValueError("require Q,p,t>0 and 0<d<p")
    if gcd(p, d) != 1 or (p - d) % 2 == 0:
        raise ValueError("require coprime opposite-parity p,d")

    completion = 2 * Q
    saddle = Fraction(Q * (p + d), p)
    complement = Fraction(Q * (p - d), p)
    h = (p + d) ** 2 * t
    k = (p - d) ** 2 * (t + 1)
    m = p * p
    record = stationary_action_four_jet(
        Q * Q, completion, saddle, h, k, m
    )

    expected_action = 2 * Q * p * (p * t - d)
    expected_first = -p * p * (t + 1)
    expected_second = Fraction(
        2 * p**3 * t * (t + 1),
        Q * (2 * p * t + p + d),
    )
    assert record["action"] == expected_action
    assert record["first"] == expected_first
    assert record["second"] == expected_second
    assert record["D"] > 0
    tangent_curvature = Fraction(8 * p**4, p * p - d * d)

    return NearZeroDualMode(
        Q=Q,
        p=p,
        d=d,
        t=t,
        completion=completion,
        saddle=saddle,
        complement=complement,
        h=h,
        k=k,
        m=m,
        action=record["action"],
        first=record["first"],
        second=record["second"],
        third=record["third"],
        fourth=record["fourth"],
        tangent_curvature=tangent_curvature,
    )


def mode_is_supported(mode: NearZeroDualMode, cutoff: int) -> bool:
    """Return whether all three integral frequencies lie in the Fejer box."""

    if cutoff <= 0:
        raise ValueError("the cutoff must be positive")
    return mode.maximum_frequency <= cutoff


def enumerate_one_mode_per_tangent(
    Q: int,
    cutoff: int,
    p_min: int,
    p_max: int,
    *,
    target_fraction: int = 16,
) -> tuple[NearZeroDualMode, ...]:
    """Enumerate a compact-collar cloud with one mode per tangent.

    The ladder coordinate is ``t=floor(cutoff/(target_fraction*p^2))``.
    The collar ``p/8<=d<=p/4`` is fixed away from both endpoints.  Invalid
    or unsupported floor effects are simply omitted; in the asymptotic
    range ``p_max^2<=cutoff/64`` none of them matter.
    """

    if min(Q, cutoff, p_min, target_fraction) <= 0 or p_max < p_min:
        raise ValueError("invalid cloud parameters")
    answer: list[NearZeroDualMode] = []
    for p in range(p_min, p_max + 1):
        t = cutoff // (target_fraction * p * p)
        if t <= 0:
            continue
        lower = ceil(p / 8)
        upper = floor(p / 4)
        for d in range(lower, upper + 1):
            if gcd(p, d) != 1 or (p - d) % 2 == 0:
                continue
            mode = canonical_near_zero_dual_mode(Q, p, d, t)
            if mode_is_supported(mode, cutoff):
                answer.append(mode)
    return tuple(answer)


def densest_scaled_quadratic_bin(
    modes: Iterable[NearZeroDualMode], width: Fraction | int
) -> tuple[NearZeroDualMode, ...]:
    """Return a largest half-open ``R=Q*J''`` bin of the given width."""

    width = Fraction(width)
    if width <= 0:
        raise ValueError("the bin width must be positive")
    bins: dict[int, list[NearZeroDualMode]] = {}
    for mode in modes:
        index = floor(mode.scaled_quadratic_jet / width)
        bins.setdefault(index, []).append(mode)
    return tuple(max(bins.values(), key=len, default=[]))


def high_precision_stationary_packet(
    mode: NearZeroDualMode,
    sample_count: int,
    *,
    decimal_digits: int = 60,
) -> tuple[complex, ...]:
    """Evaluate the actual critical-action packet on consecutive integers.

    For positive ``h,k,m`` the stationary equation is strictly increasing
    in the saddle variable, so bisection gives the unique physical branch.
    ``mpmath`` is imported lazily because exact algebra does not need it.
    """

    if sample_count <= 0 or decimal_digits < 30:
        raise ValueError("require a nonempty packet and at least 30 digits")
    import mpmath as mp

    with mp.workdps(decimal_digits):
        C = mp.mpf(mode.Q) ** 2
        values: list[complex] = []
        tiny = mp.power(10, -(decimal_digits - 10))
        for offset in range(sample_count):
            S = mp.mpf(mode.completion + offset)
            lower, upper = S * tiny, S * (1 - tiny)
            for _ in range(4 * decimal_digits):
                saddle = (lower + upper) / 2
                derivative = C * (
                    mp.mpf(mode.k) / (S - saddle) ** 2
                    - mp.mpf(mode.h) / saddle**2
                ) - mode.m
                if derivative > 0:
                    upper = saddle
                else:
                    lower = saddle
            saddle = (lower + upper) / 2
            action = (
                -mode.m * saddle
                + C * mode.h / saddle
                + C * mode.k / (S - saddle)
            )
            residue = action - mp.floor(action)
            value = mp.exp(2j * mp.pi * residue)
            values.append(complex(value) / sample_count**0.5)
    return tuple(values)


def packet_correlation(
    left: tuple[complex, ...], right: tuple[complex, ...]
) -> complex:
    """Return the inner product of two normalized sampled packets."""

    if not left or len(left) != len(right):
        raise ValueError("packets must have the same positive length")
    return sum(x * y.conjugate() for x, y in zip(left, right))


def near_zero_dual_exponent_ledger(epsilon: Fraction = Fraction(1, 96)):
    """Return the exact endpoint exponents for the cloud and its repair."""

    epsilon = Fraction(epsilon)
    if not 0 < epsilon < Fraction(1, 48):
        raise ValueError("require 0<epsilon<1/48")
    Q = Fraction(33, 16)
    H = Fraction(17, 16)
    N = Fraction(11, 16)
    p_floor = Fraction(77, 160)
    p_ceiling = H / 2
    full_saving = Fraction(1, 6)
    closing_saving = Fraction(7, 48)
    full_second_small_edge = 2 * N - 2 * full_saving
    closing_second_small_edge = 2 * N - 2 * closing_saving
    full_unresolved_R = Q - full_second_small_edge
    closing_unresolved_R = Q - closing_second_small_edge
    cloud_bin = 1 + epsilon
    trivial_radius = Q - 2 * N
    schur_inverse_term = Q / 2 - N + H / 2
    schur_direct_term = 3 * H / 2 - Q / 2
    return {
        "Q": Q,
        "H": H,
        "N": N,
        "p_floor": p_floor,
        "p_ceiling": p_ceiling,
        "cloud_tangent_count": H,
        "full_pair_saving": full_saving,
        "closing_pair_saving": closing_saving,
        "full_second_small_edge": full_second_small_edge,
        "closing_second_small_edge": closing_second_small_edge,
        "full_unresolved_R_window": full_unresolved_R,
        "closing_unresolved_R_window": closing_unresolved_R,
        "chosen_cloud_bin": cloud_bin,
        "full_degree_excess": cloud_bin - 1,
        "full_window_slack": full_unresolved_R - cloud_bin,
        "closing_window_deficit": cloud_bin - closing_unresolved_R,
        "closing_cluster_ceiling": Fraction(49, 48),
        "closing_unresolved_margin": Fraction(49, 48) - closing_unresolved_R,
        "trivial_correlation_radius": trivial_radius,
        "nonuniform_schur_inverse_term": schur_inverse_term,
        "nonuniform_schur_direct_term": schur_direct_term,
        "nonuniform_schur_total": max(
            trivial_radius, schur_inverse_term, schur_direct_term
        ),
        "nonuniform_schur_margin_to_D": 1
        - max(trivial_radius, schur_inverse_term, schur_direct_term),
    }
