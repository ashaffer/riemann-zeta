"""Finite phase-jet Bessel and inverse-cluster ledgers.

The analytic theorem recorded by this module is a theorem about vectors on a
*finite integer interval*.  There is no auxiliary continuous Fourier
variable.  Oscillation is measured by forward differences of the sampled
phase, modulo the lattice of integer-valued Newton polynomials

    sum_r m_r * binom(n-n0, r),  m_r in Z.

That quotient is essential: adding such a polynomial does not change a
single sampled exponential.  In particular, the integral affine wrap labels
in the QP stationary calculation are aliases, not separated characters.

The module supplies exact exponent ledgers for the first-, second-, and
third-difference van der Corput tests and finite numerical helpers for the
TT* / Schur inverse statement.  The proof of the derivative tests and of the
inverse theorem is given in the companion report.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence

import numpy as np


def forward_difference(values: Sequence[float | Fraction], order: int = 1):
    """Return the exact forward difference of the requested order."""

    if order < 0:
        raise ValueError("order must be nonnegative")
    answer = tuple(values)
    for _ in range(order):
        answer = tuple(answer[index + 1] - answer[index] for index in range(len(answer) - 1))
    return answer


def integer_binomial(argument: int, order: int) -> int:
    """Return ``binom(argument, order)`` for any integral argument.

    The falling-factorial definition is integral also when ``argument`` is
    negative.  It is the natural basis for integer-valued polynomial aliases.
    """

    if order < 0:
        raise ValueError("order must be nonnegative")
    numerator = 1
    for offset in range(order):
        numerator *= argument - offset
    return numerator // math.factorial(order)


def integer_newton_polynomial(
    index: int, coefficients: Sequence[int], *, origin: int = 0
) -> int:
    """Evaluate an integer-valued Newton polynomial on the integer lattice."""

    return sum(
        coefficient * integer_binomial(index - origin, order)
        for order, coefficient in enumerate(coefficients)
    )


def quotient_by_integer_newton_phase(
    phases: Sequence[float | Fraction],
    coefficients: Sequence[int],
    *,
    origin: int = 0,
) -> tuple[float | Fraction, ...]:
    """Subtract an invisible integer-valued phase from sampled phases."""

    return tuple(
        phase - integer_newton_polynomial(index, coefficients, origin=origin)
        for index, phase in enumerate(phases)
    )


def sampled_exponential(phases: Sequence[float | Fraction]) -> tuple[complex, ...]:
    """Return ``e(phase)`` at the supplied integer samples."""

    return tuple(
        cmath.exp(2j * cmath.pi * float(phase - math.floor(phase)))
        for phase in phases
    )


def normalized_packet(
    phases: Sequence[float | Fraction], amplitudes: Sequence[complex] | None = None
) -> tuple[complex, ...]:
    """Return an energy-normalized finite oscillatory packet."""

    if not phases:
        raise ValueError("a packet needs at least one sample")
    if amplitudes is None:
        amplitudes = (1.0,) * len(phases)
    if len(amplitudes) != len(phases):
        raise ValueError("phase and amplitude lengths differ")
    raw = tuple(
        complex(amplitude)
        * cmath.exp(2j * cmath.pi * float(phase - math.floor(phase)))
        for amplitude, phase in zip(amplitudes, phases)
    )
    norm = math.sqrt(sum(abs(value) ** 2 for value in raw))
    if norm == 0:
        raise ValueError("the amplitude cannot vanish identically")
    return tuple(value / norm for value in raw)


def packet_gram(packets: Sequence[Sequence[complex]]) -> np.ndarray:
    """Return the Gram matrix of finite sampled packets."""

    if not packets:
        return np.zeros((0, 0), dtype=np.complex128)
    width = len(packets[0])
    if width == 0 or any(len(packet) != width for packet in packets):
        raise ValueError("packets must be nonempty and have a common length")
    matrix = np.asarray(packets, dtype=np.complex128)
    return matrix @ matrix.conjugate().T


def abel_variation(coefficients: Sequence[complex]) -> float:
    """Variation norm in finite Abel summation.

    If every partial sum of ``z_n`` is at most ``M``, then

        |sum b_n z_n| <= abel_variation(b) * M.

    A flat normalized cross-amplitude ``b_n=1/N`` has variation ``1/N``.
    """

    if not coefficients:
        return 0.0
    return abs(coefficients[-1]) + sum(
        abs(coefficients[index + 1] - coefficients[index])
        for index in range(len(coefficients) - 1)
    )


@dataclass(frozen=True)
class JetSchurAudit:
    packet_count: int
    sample_count: int
    maximum_near_degree: int
    epsilon: float
    maximum_off_near_correlation: float
    schur_bessel_squared_bound: float
    actual_bessel_squared: float


def jet_schur_audit(
    packets: Sequence[Sequence[complex]],
    near_pairs: Iterable[tuple[int, int]],
    epsilon: float,
    *,
    tolerance: float = 1.0e-10,
) -> JetSchurAudit:
    """Verify the finite TT* cluster hypothesis and return its Schur bound.

    ``near_pairs`` is the phase-jet major-arc graph.  Every off-graph Gram
    entry must have magnitude at most ``epsilon``.  The theorem then gives

        ||T||^2 <= 1 + Delta + epsilon*(K-1-Delta),

    where ``Delta`` is the maximum near degree.  Packets are required to be
    normalized; arbitrary synthesis coefficients are covered by the operator
    norm of the Gram matrix.
    """

    if not 0 <= epsilon <= 1:
        raise ValueError("epsilon must lie in [0,1]")
    gram = packet_gram(packets)
    count = gram.shape[0]
    if count == 0:
        return JetSchurAudit(0, 0, 0, epsilon, 0.0, 0.0, 0.0)
    if np.max(np.abs(np.diag(gram) - 1.0)) > tolerance:
        raise ValueError("all packets must be energy-normalized")
    adjacency = [set() for _ in range(count)]
    for first, second in near_pairs:
        if first == second or not (0 <= first < count and 0 <= second < count):
            raise ValueError("near pairs must be distinct valid packet indices")
        adjacency[first].add(second)
        adjacency[second].add(first)
    maximum_off = 0.0
    for first in range(count):
        for second in range(first + 1, count):
            if second not in adjacency[first]:
                maximum_off = max(maximum_off, float(abs(gram[first, second])))
    if maximum_off > epsilon + tolerance:
        raise ValueError("an off-near Gram entry exceeds epsilon")
    degree = max(map(len, adjacency), default=0)
    bound = 1 + degree + epsilon * (count - 1 - degree)
    actual = float(np.linalg.eigvalsh(gram)[-1].real)
    return JetSchurAudit(
        packet_count=count,
        sample_count=gram.shape[0] and len(packets[0]),
        maximum_near_degree=degree,
        epsilon=epsilon,
        maximum_off_near_correlation=maximum_off,
        schur_bessel_squared_bound=bound,
        actual_bessel_squared=actual,
    )


def inverse_near_degree_floor(
    bessel_squared: Fraction, packet_count: int, epsilon: Fraction
) -> int:
    """Minimum near degree forced by a measured Bessel quotient.

    This is the integral form of

        Delta >= (L-1-epsilon*(K-1))/(1-epsilon).

    It is stronger than discarding the ``-epsilon*Delta`` term.
    """

    bessel_squared, epsilon = Fraction(bessel_squared), Fraction(epsilon)
    if packet_count < 0 or not 0 <= epsilon < 1:
        raise ValueError("require K>=0 and 0<=epsilon<1")
    if packet_count == 0:
        return 0
    lower = (bessel_squared - 1 - epsilon * (packet_count - 1)) / (1 - epsilon)
    return max(0, min(packet_count - 1, math.ceil(lower)))


def derivative_test_saving_exponent(
    order: int, block_exponent: Fraction, derivative_decay_exponent: Fraction
) -> Fraction:
    """Power saving in a normalized discrete derivative-test envelope.

    Write ``N=D^n`` and ``lambda=D^(-t)``.  Ignoring absolute constants, the
    normalized envelopes are

        r=1: D^(-n+t),
        r=2: D^(-t/2) + D^(-n+t/2),
        r=3: D^(-t/6) + D^(-n/2+t/6).

    The return value is the smaller saving exponent among the displayed
    terms.  A nonpositive value means that the derivative test gives no power
    cancellation at that scale.
    """

    n, t = Fraction(block_exponent), Fraction(derivative_decay_exponent)
    if n <= 0 or t < 0:
        raise ValueError("require a positive block exponent and t>=0")
    if order == 1:
        return n - t
    if order == 2:
        return min(t / 2, n - t / 2)
    if order == 3:
        return min(t / 6, n / 2 - t / 6)
    raise ValueError("only derivative orders 1, 2, and 3 are implemented")


def derivative_test_decay_window(
    order: int, block_exponent: Fraction, required_saving: Fraction
) -> tuple[Fraction, Fraction]:
    """Return all ``t`` for which the derivative test saves ``D^-saving``."""

    n, saving = Fraction(block_exponent), Fraction(required_saving)
    if n <= 0 or saving < 0:
        raise ValueError("require n>0 and saving>=0")
    if order == 1:
        lower, upper = Fraction(), n - saving
    elif order == 2:
        lower, upper = 2 * saving, 2 * n - 2 * saving
    elif order == 3:
        lower, upper = 6 * saving, 3 * n - 6 * saving
    else:
        raise ValueError("only derivative orders 1, 2, and 3 are implemented")
    if upper < lower:
        raise ValueError("the requested saving exceeds this test's optimum")
    return lower, upper


@dataclass(frozen=True)
class EndpointPhaseJetLedger:
    block_length: Fraction
    wide_packet_count: Fraction
    narrow_bessel_squared_target: Fraction
    full_pair_correlation_saving: Fraction
    closing_operator_saving: Fraction
    closing_pair_correlation_saving: Fraction
    closing_cluster_ceiling: Fraction
    optimal_cubic_pair_saving: Fraction
    cubic_margin_for_full_gain: Fraction
    cubic_margin_for_closing_gain: Fraction
    full_first_window: tuple[Fraction, Fraction]
    full_second_window: tuple[Fraction, Fraction]
    full_third_window: tuple[Fraction, Fraction]
    closing_third_window: tuple[Fraction, Fraction]


def endpoint_phase_jet_ledger() -> EndpointPhaseJetLedger:
    """Return the exact ``D``-power ledger at the worst anisotropic cell."""

    block = Fraction(11, 16)  # q^(1/3), q=D^(33/16)
    wide = Fraction(7, 6)     # B=D^(7/6)
    narrow = Fraction(1)      # A=D
    full_pair = wide - narrow  # epsilon=A/B=D^(-1/6)
    closing_operator = Fraction(7, 96)
    closing_pair = 2 * closing_operator
    closing_cluster = wide - closing_pair
    cubic = block / 4
    return EndpointPhaseJetLedger(
        block_length=block,
        wide_packet_count=wide,
        narrow_bessel_squared_target=narrow,
        full_pair_correlation_saving=full_pair,
        closing_operator_saving=closing_operator,
        closing_pair_correlation_saving=closing_pair,
        closing_cluster_ceiling=closing_cluster,
        optimal_cubic_pair_saving=cubic,
        cubic_margin_for_full_gain=cubic - full_pair,
        cubic_margin_for_closing_gain=cubic - closing_pair,
        full_first_window=derivative_test_decay_window(1, block, full_pair),
        full_second_window=derivative_test_decay_window(2, block, full_pair),
        full_third_window=derivative_test_decay_window(3, block, full_pair),
        closing_third_window=derivative_test_decay_window(3, block, closing_pair),
    )


def integer_affine_alias_packets(packet_count: int, sample_count: int):
    """Return the exact hostile family ``e(j*n)=1`` on integer samples."""

    if packet_count <= 0 or sample_count <= 0:
        raise ValueError("packet and sample counts must be positive")
    return tuple(
        normalized_packet(tuple(Fraction(label * sample) for sample in range(sample_count)))
        for label in range(packet_count)
    )


@dataclass(frozen=True)
class StationaryActionJet:
    """Exact first three derivatives of one stationary completion action."""

    center: Fraction
    completion: Fraction
    saddle: Fraction
    left_frequency: Fraction
    right_frequency: Fraction
    poisson_frequency: Fraction
    left_scaled_frequency: Fraction
    right_scaled_frequency: Fraction
    curvature_numerator: Fraction
    first: Fraction
    second: Fraction
    third: Fraction
    fourth: Fraction


def stationary_action_jet(
    center: Fraction,
    completion: Fraction,
    saddle: Fraction,
    left_frequency: Fraction,
    right_frequency: Fraction,
    poisson_frequency: Fraction,
) -> StationaryActionJet:
    r"""Return the exact physical-``S`` jet of a stationary action.

    For

    ``F(a,S)=C*(h/a+k/(S-a))-m*a``

    assume ``F_a=0`` at the supplied interior saddle.  Put

    ``u=C*h/a^2``, ``v=C*k/(S-a)^2``, and ``w=u*(S-a)+v*a``.

    Nondegeneracy is ``w!=0``.  If ``A(S)=F(a(S),S)`` is the local stationary
    action, exact implicit differentiation gives

    ``A'=-v``, ``A''=2uv/w``, and
    ``A'''=-6uv*(u^2*(S-a)+v^2*a)/w^3``.
    """

    C, S, a, h, k, m = map(
        Fraction,
        (center, completion, saddle, left_frequency, right_frequency, poisson_frequency),
    )
    if C == 0 or not 0 < a < S:
        raise ValueError("require a nonzero center and an interior saddle")
    b = S - a
    u = C * h / (a * a)
    v = C * k / (b * b)
    if v - u != m:
        raise ValueError("the supplied point is not stationary")
    w = u * b + v * a
    if w == 0:
        raise ValueError("the supplied stationary point is a cubic fold")
    first = -v
    second = 2 * u * v / w
    third = -6 * u * v * (u * u * b + v * v * a) / (w**3)
    tangent = a / S
    saddle_speed = v * a / w
    shape = -S * third / (3 * second)
    transport = (
        saddle_speed * (1 - saddle_speed) / (tangent * (1 - tangent))
    )
    fourth = 3 * second * (4 * shape * shape - 5 * transport * (shape - 1)) / (S * S)
    return StationaryActionJet(
        center=C,
        completion=S,
        saddle=a,
        left_frequency=h,
        right_frequency=k,
        poisson_frequency=m,
        left_scaled_frequency=u,
        right_scaled_frequency=v,
        curvature_numerator=w,
        first=first,
        second=second,
        third=third,
        fourth=fourth,
    )


def recover_stationary_action_from_three_jet(
    center: Fraction,
    completion: Fraction,
    first: Fraction,
    second: Fraction,
    third: Fraction,
) -> StationaryActionJet:
    r"""Recover a regular nonzero-dual saddle from ``(A',A'',A''')``.

    This is the exact injectivity theorem behind the phase-jet proposal.
    It applies off the singular loci ``h*k*m=0`` and off the cubic fold.
    The zero-dual locus ``m=0`` is genuinely noninjective: reflected tangent
    decompositions can have the same stationary action for every ``S``.
    """

    C, S, p1, p2, p3 = map(Fraction, (center, completion, first, second, third))
    if C == 0 or p1 == 0 or p2 == 0:
        raise ValueError("the one-inverse or zero-curvature locus is singular")
    v = -p1
    ratio = -2 * v * p3 / (3 * p2 * p2)
    if ratio == 1:
        raise ValueError("the zero-dual stationary-action jet is noninjective")
    u = (v - p2 * S / 2) / (ratio - 1)
    if u == 0 or u == v:
        raise ValueError("the one-inverse or zero-dual locus is singular")
    w = 2 * u * v / p2
    a = (w - u * S) / (v - u)
    if not 0 < a < S:
        raise ValueError("the recovered jet has no interior saddle")
    b = S - a
    h = u * a * a / C
    k = v * b * b / C
    m = v - u
    recovered = stationary_action_jet(C, S, a, h, k, m)
    if (recovered.first, recovered.second, recovered.third) != (p1, p2, p3):
        raise ArithmeticError("three-jet reconstruction failed")
    return recovered


@dataclass(frozen=True)
class QuotientCurvatureJetInvariants:
    """Affine-Newton-quotient invariants from ``(A'',A''',A'''')``."""

    shape: Fraction
    transport: Fraction
    transverse_square: Fraction
    mixed_invariant: Fraction
    centered: bool
    tangent_x_squared: Fraction
    speed_y_squared_if_centered: Fraction | None
    speed_over_tangent: Fraction | None


def quotient_curvature_jet_invariants(
    completion: Fraction,
    second: Fraction,
    third: Fraction,
    fourth: Fraction,
) -> QuotientCurvatureJetInvariants:
    r"""Recover the stationary shape up to exact left-right reflection.

    Put ``t=a/S``, ``alpha=a'(S)``, ``x=2t-1``, and ``y=2alpha-1``.  The
    affine-quotient curvature jet obeys

    ``A=-S*q3/(3*q2)=1+(alpha-t)^2/(t*(1-t))`` and

    ``B=S^2*q4/(3*q2)=4*A^2-5*R*(A-1)``,

    where ``R=alpha*(1-alpha)/(t*(1-t))``.  For nonzero Poisson frequency,
    ``w=A-1>0``.  With ``L=1-R-w``, one has

    ``x^2=L^2/(L^2+4w)`` and ``y/x=(L+2w)/L``.

    Thus ``(t,alpha)`` is determined up to ``(t,alpha)->(1-t,1-alpha)``.
    When ``L=0`` the nonzero-dual branch is central: ``x=0`` and ``y^2=w``.
    """

    S, q2, q3, q4 = map(Fraction, (completion, second, third, fourth))
    if S <= 0 or q2 == 0:
        raise ValueError("require a positive completion and nonzero curvature jet")
    shape = -S * q3 / (3 * q2)
    transverse = shape - 1
    if transverse <= 0:
        raise ValueError("the zero-dual or nonphysical curvature shape is singular")
    scaled_fourth = S * S * q4 / (3 * q2)
    transport = (4 * shape * shape - scaled_fourth) / (5 * transverse)
    mixed = 1 - transport - transverse
    if mixed == 0:
        return QuotientCurvatureJetInvariants(
            shape=shape,
            transport=transport,
            transverse_square=transverse,
            mixed_invariant=mixed,
            centered=True,
            tangent_x_squared=Fraction(),
            speed_y_squared_if_centered=transverse,
            speed_over_tangent=None,
        )
    x_squared = mixed * mixed / (mixed * mixed + 4 * transverse)
    return QuotientCurvatureJetInvariants(
        shape=shape,
        transport=transport,
        transverse_square=transverse,
        mixed_invariant=mixed,
        centered=False,
        tangent_x_squared=x_squared,
        speed_y_squared_if_centered=None,
        speed_over_tangent=(mixed + 2 * transverse) / mixed,
    )
