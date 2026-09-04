"""Information bounds for high primitive directions in the Newton quotient.

This module separates three facts which are easy to conflate:

* an exact stationary frequency at a primitive tangent has size ``p^2``;
* arbitrary supported frequencies still distinguish the tangent in exact
  arithmetic, but only with condition number ``p^2/H``;
* sampled reciprocal packets need the still larger scale ``p^2/(H*N)`` to
  remain separated on a block of length ``N``.

The phase is the physical normalized reciprocal phase

    Phi(t)=h/(4t)+k/(4(1-t))-m*t.

For integer samples we use ``phi(s)=2Q*Phi(t+s/(2Q))``.  Its affine
``m``-term is exactly invisible in the projective integer Newton quotient.
"""

from __future__ import annotations

import cmath
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, sqrt
from typing import Sequence


Frequency = tuple[int, int, int]  # coordinates (-m,h,k)


def parity_reduced_direction(p: int, d: int) -> tuple[int, int, int]:
    """Return ``(chi,a,b)`` for ``t=(p+d)/(2p)=a/(a+b)``."""

    if p <= 0 or d == 0 or abs(d) >= p or gcd(p, abs(d)) != 1:
        raise ValueError("require p>0, 0<|d|<p, and gcd(p,d)=1")
    chi = gcd(p + d, p - d)
    if chi not in (1, 2):
        raise AssertionError("a primitive direction has parity index 1 or 2")
    a, b = (p + d) // chi, (p - d) // chi
    assert gcd(a, b) == 1
    return chi, a, b


def primitive_tangent_normal(p: int, d: int) -> tuple[int, int, int]:
    """Return the primitive tangent vector normal to stationary frequencies.

    In frequency coordinates ``(-m,h,k)``, stationarity is orthogonality to

    ``(chi^2*a^2*b^2, -p^2*b^2, p^2*a^2)``.
    """

    chi, a, b = parity_reduced_direction(p, d)
    normal = (chi * chi * a * a * b * b, -p * p * b * b, p * p * a * a)
    assert gcd(gcd(abs(normal[0]), abs(normal[1])), abs(normal[2])) == 1
    return normal


def stationary_residual(p: int, d: int, frequency: Frequency) -> int:
    """Return zero exactly when ``frequency`` is stationary at the tangent."""

    minus_m, h, k = frequency
    m = -minus_m
    chi, a, b = parity_reduced_direction(p, d)
    return p * p * (a * a * k - b * b * h) - chi * chi * a * a * b * b * m


@dataclass(frozen=True)
class StationarySupportCertificate:
    p: int
    d: int
    parity: int
    a: int
    b: int
    cutoff: int
    universal_lower_bound: int
    only_zero_mode: bool


def stationary_support_certificate(
    p: int, d: int, cutoff: int
) -> StationarySupportCertificate:
    """Certify when the supported stationary lattice contains only zero.

    Every stationary mode has ``p^2|m``.  If ``m=0``, it has
    ``(h,k)=ell*(a^2,b^2)``.  Consequently every nonzero stationary mode has
    sup norm at least ``min(p^2,max(a^2,b^2))>=p^2/4``.
    """

    if cutoff < 0:
        raise ValueError("the cutoff must be nonnegative")
    chi, a, b = parity_reduced_direction(p, d)
    lower = min(p * p, max(a * a, b * b))
    assert 4 * lower >= p * p
    return StationarySupportCertificate(
        p=p,
        d=d,
        parity=chi,
        a=a,
        b=b,
        cutoff=cutoff,
        universal_lower_bound=lower,
        only_zero_mode=cutoff < lower,
    )


def reciprocal_phase(t: Fraction, frequency: Frequency) -> Fraction:
    """Evaluate the normalized reciprocal phase exactly."""

    if not 0 < t < 1:
        raise ValueError("require 0<t<1")
    minus_m, h, k = frequency
    return minus_m * t + Fraction(h, 4) / t + Fraction(k, 4) / (1 - t)


def sampled_reciprocal_phase(
    Q: int, t: Fraction, frequency: Frequency, sample_count: int
) -> tuple[Fraction, ...]:
    """Return ``2Q*Phi(t+s/(2Q))`` on an integer block."""

    if Q <= 0 or sample_count <= 0:
        raise ValueError("require Q>0 and a nonempty sample block")
    answer = []
    for sample in range(sample_count):
        shifted = t + Fraction(sample, 2 * Q)
        if not 0 < shifted < 1:
            raise ValueError("the sampled block leaves the reciprocal collar")
        answer.append(2 * Q * reciprocal_phase(shifted, frequency))
    return tuple(answer)


def forward_difference(values: Sequence[Fraction], order: int) -> tuple[Fraction, ...]:
    """Return an exact forward difference."""

    if order < 0:
        raise ValueError("order must be nonnegative")
    answer = tuple(values)
    for _ in range(order):
        answer = tuple(answer[index + 1] - answer[index] for index in range(len(answer) - 1))
    return answer


def projective_newton_signature(
    Q: int, t: Fraction, frequency: Frequency, order: int = 3
) -> tuple[Fraction, ...]:
    """Return Newton coefficients of orders 1 through ``order`` modulo one.

    The constant coefficient is omitted because a global phase does not
    affect an absolute Gram entry.  The returned representatives lie in
    ``[0,1)``.
    """

    if order < 1:
        raise ValueError("require order>=1")
    values = sampled_reciprocal_phase(Q, t, frequency, order + 1)
    signature = []
    for degree in range(1, order + 1):
        coefficient = forward_difference(values, degree)[0]
        signature.append(coefficient - coefficient.numerator // coefficient.denominator)
    return tuple(signature)


def torus_distance(left: Fraction, right: Fraction) -> Fraction:
    """Return distance in ``R/Z`` between two rational values."""

    delta = left - right
    residue = delta - delta.numerator // delta.denominator
    return min(residue, 1 - residue)


def harmonic_torus_resolution(
    base_gap: Fraction, harmonic_count: int, noise: Fraction
) -> Fraction:
    """Resolve a torus gap from all of its first ``harmonic_count`` multiples.

    If ``||j*x||_T<=noise<1/4`` for every ``1<=j<=L``, then necessarily
    ``||x||_T<=noise/L``.  This elementary lemma is the vector-valued gain
    supplied by the full supported Fejer frequency interval.
    """

    if harmonic_count <= 0 or not 0 <= noise < Fraction(1, 4):
        raise ValueError("require L>0 and 0<=noise<1/4")
    zero = Fraction()
    distance = torus_distance(base_gap, zero)
    for multiplier in range(1, harmonic_count + 1):
        if torus_distance(multiplier * base_gap, zero) > noise:
            raise ValueError("the harmonic near-alias hypothesis fails")
    bound = noise / harmonic_count
    if distance > bound:
        raise AssertionError("harmonic torus resolution lemma failed")
    return bound


def adjacent_primitive_tangents(p: int) -> tuple[Fraction, Fraction, Fraction]:
    """Return an explicit pair at Farey-scale distance ``1/[p(p+2)]``.

    For odd ``p``, these are the directions ``(p,1)`` and ``(p+2,1)``.
    """

    if p < 3 or p % 2 == 0:
        raise ValueError("require an odd p>=3")
    left = Fraction(p + 1, 2 * p)
    right = Fraction(p + 3, 2 * (p + 2))
    gap = abs(left - right)
    assert gap == Fraction(1, p * (p + 2))
    return left, right, gap


def newton_jet_lipschitz_bound(
    cutoff: int,
    tangent_gap: Fraction,
    *,
    collar: Fraction = Fraction(1, 4),
) -> Fraction:
    """A uniform bound for each supported first-through-third jet gap.

    The first Newton coefficient dominates.  On
    ``collar<=t,t'<=1-collar``, repeated finite-difference integration gives

    ``dist_T(Delta^r phi_t,Delta^r phi_t')
       <= C_r*H*|t-t'|*(2Q)^(1-r)``.

    This helper returns the valid common bound ``C*H*|t-t'|`` with a simple
    explicit constant large enough for orders one through three.
    """

    if cutoff < 0 or not 0 < collar < Fraction(1, 2):
        raise ValueError("invalid cutoff or collar")
    # max_{2<=j<=4} j!/(2*collar^(j+1)) bounds the two reciprocal terms.
    constants = [
        Fraction(2, 1) / collar**3,
        Fraction(6, 2) / collar**4,
        Fraction(24, 2) / collar**5,
    ]
    return max(constants) * cutoff * abs(tangent_gap)


def sampled_projective_phase_bound(
    cutoff: int,
    sample_count: int,
    tangent_gap: Fraction,
    *,
    collar: Fraction = Fraction(1, 4),
) -> Fraction:
    """Bound the aligned phase gap on a full sampled block.

    After subtracting the value at sample zero, the affine ``m`` term
    cancels exactly.  The mean-value theorem gives

    ``max_s |(phi_t(s)-phi_t(0))-(phi_t'(s)-phi_t'(0))|
       <= C*H*N*|t-t'|``.
    """

    if sample_count <= 0:
        raise ValueError("sample_count must be positive")
    second_derivative_constant = Fraction(1, 1) / collar**3
    return second_derivative_constant * cutoff * sample_count * abs(tangent_gap)


def aligned_packet_correlation(
    left_phases: Sequence[Fraction], right_phases: Sequence[Fraction]
) -> float:
    """Return absolute correlation after the irrelevant constant alignment."""

    if not left_phases or len(left_phases) != len(right_phases):
        raise ValueError("phase blocks must have the same positive length")
    offset = left_phases[0] - right_phases[0]
    total = 0j
    for left, right in zip(left_phases, right_phases):
        delta = left - right - offset
        total += cmath.exp(2j * cmath.pi * float(delta))
    return abs(total) / len(left_phases)


def high_p_information_exponents() -> dict[str, Fraction]:
    """Return the four distinct high-``p`` resolution thresholds."""

    H = Fraction(17, 16)
    eta_decay = Fraction(7, 48)
    block = Fraction(11, 16)
    stationary = H / 2
    newton_noise_alias = (H + eta_decay) / 2
    first_test_minimum = block - eta_decay
    certificate_alias = (H + first_test_minimum) / 2
    packet_coherence = (H + block) / 2
    sampled_eta_alias = (H + block + eta_decay) / 2
    fixed_q_noise_cell = Fraction(33, 16) - H - eta_decay
    residual_floor = Fraction(77, 160)
    slope_rounding_cell = Fraction(7, 6) - residual_floor
    assert stationary == Fraction(17, 32)
    assert newton_noise_alias == Fraction(29, 48)
    assert first_test_minimum == Fraction(13, 24)
    assert certificate_alias == Fraction(77, 96)
    assert packet_coherence == Fraction(7, 8)
    assert sampled_eta_alias == Fraction(91, 96)
    assert fixed_q_noise_cell == Fraction(41, 48)
    assert slope_rounding_cell == Fraction(329, 480)
    return {
        "H": H,
        "eta_decay": eta_decay,
        "block": block,
        "stationary_support_edge": stationary,
        "newton_coefficient_eta_alias": newton_noise_alias,
        "first_test_minimum_decay": first_test_minimum,
        "phase_jet_certificate_alias": certificate_alias,
        "sampled_packet_coherence": packet_coherence,
        "sampled_phase_eta_alias": sampled_eta_alias,
        "fixed_Q_eta_signature_cluster": fixed_q_noise_cell,
        "physical_slope_rounding_cluster": slope_rounding_cell,
    }


def asymptotic_correlation_lower_bound(phase_radius: float) -> float:
    """Elementary lower bound when all aligned phases lie in a short arc."""

    if not 0 <= phase_radius <= 0.25:
        raise ValueError("require a phase radius in [0,1/4]")
    return max(0.0, 1.0 - 2.0 * (cmath.pi.real**2) * phase_radius**2)
