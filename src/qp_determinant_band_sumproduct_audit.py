"""Exact checks for the QP determinant-band positive tensor.

There are two complementary facts.

* On the whole fixed-width prime shell, flat weights force determinant-band
  mass of order ``D / log(q)^2``.  Thus the positive tensor cannot admit a
  uniform fixed-power saving over ``D``.
* If all active colors lie in one integer interval ``[X,X+L]`` with
  ``D + L^2 < X``, the determinant condition forces an additive
  parallelogram.  Its determinant factors as a product of the two gaps, and
  dyadic autocorrelation gives a square-root ``D`` bound.

The analytic inequalities are proved in the accompanying report.  This
module records the exact identities, finite collision counts, and exponent
ledger used to hostile-audit them.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import ceil, floor, log2, sqrt
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class DeterminantBandExponentLedger:
    """Project-scale exponents for the two determinant-band regimes."""

    d_exponent_in_q: Fraction
    full_shell_r43_exponent_in_d: Fraction
    global_flat_prime_lower_exponent_in_d: Fraction
    localized_upper_exponent_in_d: Fraction
    flat_support_at_most_d_upper_exponent_in_d: Fraction
    conditional_modular_energy_upper_exponent_in_d: Fraction
    localized_four_cycle_trace_exponent_in_d: Fraction
    localized_d_prime_span_squared_exponent_in_q: Fraction
    localized_span_condition_has_power_margin: bool
    uniform_positive_power_saving_is_possible: bool


@dataclass(frozen=True)
class UniformFiveFourthsLedger:
    """Exact D-power synthesis for the uniform five-fourths theorem."""

    support_crossover: Fraction
    flat_character_mass_at_crossover: Fraction
    broad_pointwise_cap: Fraction
    small_bin_trace: Fraction
    diffuse_trace_at_crossover: Fraction
    parabolic_trace: Fraction
    uniform_trace: Fraction
    uniform_operator: Fraction
    previous_uniform_trace: Fraction
    trace_gain: Fraction
    transverse_exponent: Fraction


def uniform_five_fourths_ledger() -> UniformFiveFourthsLedger:
    """Return the exact crossover ledger behind the uniform improvement.

    For a factor-two coefficient bin of size ``M=D^mu``, the character
    determinant mass is ``D^(1/2+mu/4)`` (the principal term is smaller at
    the crossover).  Multiplication by the broad completion cap ``D^(5/16)``
    meets the diffuse trace ``D^(3-mu)`` at ``mu=7/4``.  Both equal
    ``D^(5/4)`` there, which also matches the proved parabolic theorem.
    """

    crossover = Fraction(7, 4)
    character_mass = Fraction(1, 2) + crossover / 4
    broad_cap = Fraction(5, 16)
    small_trace = character_mass + broad_cap
    diffuse_trace = 3 - crossover
    uniform_trace = Fraction(5, 4)
    previous = Fraction(21, 16)
    return UniformFiveFourthsLedger(
        support_crossover=crossover,
        flat_character_mass_at_crossover=character_mass,
        broad_pointwise_cap=broad_cap,
        small_bin_trace=small_trace,
        diffuse_trace_at_crossover=diffuse_trace,
        parabolic_trace=uniform_trace,
        uniform_trace=uniform_trace,
        uniform_operator=uniform_trace / 4,
        previous_uniform_trace=previous,
        trace_gain=previous - uniform_trace,
        transverse_exponent=Fraction(1, 2) + Fraction(16, 33) * (uniform_trace / 4),
    )


def determinant_band_exponent_ledger() -> DeterminantBandExponentLedger:
    """Return the exact power ledger at ``D=q^(16/33)``.

    Logarithms are suppressed.  The whole prime shell has cardinality
    ``q^(1+o(1))=D^(33/16+o(1))`` and gives a lower bound
    ``D^(1-o(1))``.  A block of ``D`` consecutive-scale primes has span
    ``D q^o(1)``; its squared span is ``q^(32/33+o(1))=o(q)``, so the local
    square-root theorem applies and gives ``D^(1/2)``.
    """

    return DeterminantBandExponentLedger(
        d_exponent_in_q=Fraction(16, 33),
        full_shell_r43_exponent_in_d=Fraction(33, 16),
        global_flat_prime_lower_exponent_in_d=Fraction(1),
        localized_upper_exponent_in_d=Fraction(1, 2),
        flat_support_at_most_d_upper_exponent_in_d=Fraction(3, 4),
        conditional_modular_energy_upper_exponent_in_d=Fraction(1, 2),
        localized_four_cycle_trace_exponent_in_d=Fraction(1),
        localized_d_prime_span_squared_exponent_in_q=Fraction(32, 33),
        localized_span_condition_has_power_margin=True,
        uniform_positive_power_saving_is_possible=False,
    )


def flat_support_character_bound_exponent() -> Fraction:
    """Return the unconditional endpoint exponent ``3/4`` in powers of D.

    For a flat set of ``M<=D`` actual shell prime powers, multiplicative
    character orthogonality gives

    ``N_D(A)/M^2 << M^(1/4) D^(1/2) q^o(1) + MD/q``.

    The first term is at most ``D^(3/4+o(1))`` and the second is subunit at
    ``D=q^(16/33)``.
    """

    return Fraction(3, 4)


def flat_support_character_profile_exponent(mu: Fraction) -> Fraction:
    """Return ``min(mu, 1/2+mu/4)`` for ``M=D^mu<=D``.

    The first entry is the three-coordinate matching bound ``W<=M``; the
    second is the character/fourth-moment estimate.  The negligible
    principal term ``MD/q`` is omitted from this D-power profile.
    """

    if mu < 0 or mu > 1:
        raise ValueError("the flat-support exponent must lie in [0,1]")
    return min(mu, Fraction(1, 2) + mu / 4)


def modular_energy_promotion_exponent(energy_exponent_in_m: Fraction) -> Fraction:
    """Return the endpoint D-exponent supplied by a modular-energy bound.

    If every relevant modulus has multiplicative energy
    ``E_x(A)<=M^energy_exponent_in_m q^o(1)``, the character argument gives

    ``N_D(A)/M^2 << D^(1/2) M^((energy_exponent_in_m-1)/4)``

    at ``M=D``.  Thus the trivial energy exponent three gives ``3/4``,
    while the desired near-diagonal exponent two gives ``1/2``.
    """

    if energy_exponent_in_m < 2 or energy_exponent_in_m > 3:
        raise ValueError("the modular-energy exponent must lie in [2,3]")
    return Fraction(1, 2) + (energy_exponent_in_m - 2) / 4


def determinant(a: int, b: int, c: int, d: int) -> int:
    """Return ``a*d-b*c``."""

    return a * d - b * c


def local_additive_balance_is_forced(
    a: int,
    b: int,
    c: int,
    d: int,
    *,
    interval_left: int,
    interval_length: int,
    band: int,
) -> bool:
    """Check the exact local implication ``|ad-bc|<=band => a+d=b+c``.

    The implication is certified only under ``band+interval_length^2 < X``
    for ``X=interval_left``.  All four inputs must lie in ``[X,X+L]``.
    """

    if interval_left <= 0 or interval_length < 0 or band < 0:
        raise ValueError("invalid interval or determinant band")
    if band + interval_length**2 >= interval_left:
        raise ValueError("the local additive-balance hypothesis is absent")
    if any(
        value < interval_left or value > interval_left + interval_length
        for value in (a, b, c, d)
    ):
        raise ValueError("a coordinate lies outside the local interval")
    if abs(determinant(a, b, c, d)) > band:
        return True
    return a + d == b + c


def parallelogram_determinant_factorization(a: int, b: int, c: int, d: int) -> bool:
    """Check ``ad-bc=-(a-b)(a-c)`` when ``a+d=b+c``."""

    if a + d != b + c:
        raise ValueError("the four integers do not form an additive parallelogram")
    return determinant(a, b, c, d) == -(a - b) * (a - c)


def weighted_determinant_band_mass(
    coordinates: Sequence[int],
    weights: Sequence[float],
    band: int,
    *,
    nonzero: bool = False,
    all_distinct: bool = False,
) -> float:
    """Enumerate the positive determinant-band quartic on a finite fixture."""

    if len(coordinates) != len(weights):
        raise ValueError("coordinates and weights have different lengths")
    if band < 0:
        raise ValueError("the determinant band is negative")
    total = 0.0
    for i, a in enumerate(coordinates):
        for j, b in enumerate(coordinates):
            for k, c in enumerate(coordinates):
                for ell, d in enumerate(coordinates):
                    det = determinant(a, b, c, d)
                    if abs(det) > band or (nonzero and det == 0):
                        continue
                    if all_distinct and len({a, b, c, d}) != 4:
                        continue
                    total += abs(weights[i] * weights[j] * weights[k] * weights[ell])
    return total


def weighted_hyperbolic_parallelogram_mass(
    weights: Mapping[int, float], band: int, *, nonzero: bool = True
) -> float:
    """Enumerate the local gap form after extending the weights by zero.

    This returns

    ``sum_{a,h,k: |h*k|<=band} u[a]u[a-h]u[a-k]u[a-h-k]``.
    """

    if band < 0:
        raise ValueError("the determinant band is negative")
    if not weights:
        return 0.0
    support = tuple(weights)
    max_gap = max(support) - min(support)
    total = 0.0
    for a in support:
        for h in range(-max_gap, max_gap + 1):
            if nonzero and h == 0:
                continue
            for k in range(-max_gap, max_gap + 1):
                if nonzero and k == 0:
                    continue
                if abs(h * k) > band:
                    continue
                total += (
                    abs(weights.get(a, 0.0))
                    * abs(weights.get(a - h, 0.0))
                    * abs(weights.get(a - k, 0.0))
                    * abs(weights.get(a - h - k, 0.0))
                )
    return total


def dyadic_minimum_sum(band: int) -> int:
    """Return ``sum min(2^i,2^j)`` over ``i,j>=0, 2^(i+j)<=band``.

    The proof of the local theorem bounds each dyadic gap block by a fixed
    constant times this minimum.  This ledger sum is ``O(sqrt(band))``.
    """

    if band < 1:
        return 0
    top = floor(log2(band))
    return sum(
        min(2**i, 2**j)
        for i in range(top + 1)
        for j in range(top + 1)
        if i + j <= top
    )


def dyadic_minimum_sum_ratio(band: int) -> float:
    """Normalize the dyadic ledger by ``sqrt(band)``."""

    if band < 1:
        return 0.0
    return dyadic_minimum_sum(band) / sqrt(band)


def slope_bin_collision_lower_bound(
    number_of_nodes: int, number_of_bins: int, *, cross_repeat_allowance: int = 2
) -> int:
    """Cauchy lower bound for all-distinct nonzero slope collisions.

    There are ``N=M(M-1)`` reduced ordered slopes.  Cauchy gives at least
    ``ceil(N^2/J)-N`` ordered collisions of two distinct slopes in ``J``
    bins.  In the prime fixture, same-position coordinate repeats cannot be
    nonzero in a sub-``q`` determinant band, while each of the two cross
    repeats costs at most ``M^2``.  The returned value applies this safe
    subtraction and truncates at zero.
    """

    if number_of_nodes < 0 or number_of_bins <= 0 or cross_repeat_allowance < 0:
        raise ValueError("invalid collision parameters")
    m = number_of_nodes
    slopes = m * (m - 1)
    collisions = ceil(slopes * slopes / number_of_bins) - slopes
    return max(0, collisions - cross_repeat_allowance * m * m)


def all_distinct_tangent_packet_count(length: int) -> int:
    """Count a robust all-distinct subpacket in a consecutive integer block.

    Take ``a`` in the upper quarter of ``{0,...,length-1}`` and distinct
    positive gaps ``h,k<=length/8``.  Then ``a,a-h,a-k,a-h-k`` are all in
    the block and are pairwise distinct.  The count is cubic in ``length``.
    """

    if length < 1:
        return 0
    gap_cap = length // 8
    anchor_count = max(0, length - 2 * gap_cap)
    ordered_distinct_gaps = gap_cap * max(0, gap_cap - 1)
    return anchor_count * ordered_distinct_gaps
