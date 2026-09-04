"""Algebraic replay for the exact strip-to-QP and support no-go bridges.

The analytic proofs are in the companion report
``results/ZETA23-QP-STRIP-BRIDGE-AND-SUPPORT-NONIMPLICATION-2026-08-15.md``.
This module checks their exponent placement, the centered continuum term,
the finite-Euler-factor countermodels, and the Fejer moving-band model.  It
does not claim a zero-free strip or an unconditional estimate of the actual
Delsarte value.
"""

from __future__ import annotations

from dataclasses import dataclass
import cmath
import math


QP_LOWER_EXPONENT = 0.01
QP_UPPER_EXPONENT = 50.0 / 33.0
QP_FIXED_SLICE_KAPPA_MAX = 0.018746369714728765


@dataclass(frozen=True)
class StripToQPLedger:
    """Exponent ledger for shifting to ``1-delta+eta/2``."""

    strip_width: float
    requested_qp_power: float
    contour_reserve: float
    contour_line: float
    mellin_decay_order: int
    pole_term_exponent: float

    @property
    def closes(self) -> bool:
        return (
            self.strip_width > self.requested_qp_power
            and self.contour_reserve > self.requested_qp_power
            and self.pole_term_exponent <= 1.0 - self.contour_reserve
        )


def strip_to_qp_ledger(
    strip_width: float,
    requested_qp_power: float,
    *,
    lower_height_exponent: float = QP_LOWER_EXPONENT,
) -> StripToQPLedger:
    """Choose explicit contour reserve and Mellin decay for strip -> QP.

    If ``delta > c``, set ``eta=(delta-c)/2``.  The contour error normalized
    by shell mass has exponent ``-(delta-eta)``.  A smooth cutoff's pole term
    is ``Y * t**(-K)``; the returned integer ``K`` makes it no larger than the
    same contour scale for ``t >= Y**a``.
    """

    if not 0.0 < strip_width < 1.0:
        raise ValueError("strip_width must lie in (0, 1)")
    if not 0.0 < requested_qp_power < strip_width:
        raise ValueError("requested_qp_power must lie in (0, strip_width)")
    if lower_height_exponent <= 0.0:
        raise ValueError("lower_height_exponent must be positive")

    eta = (strip_width - requested_qp_power) / 2.0
    reserve = strip_width - eta
    contour_line = 1.0 - strip_width + eta / 2.0
    decay_order = math.ceil(reserve / lower_height_exponent)
    pole_exponent = 1.0 - lower_height_exponent * decay_order
    return StripToQPLedger(
        strip_width=strip_width,
        requested_qp_power=requested_qp_power,
        contour_reserve=reserve,
        contour_line=contour_line,
        mellin_decay_order=decay_order,
        pole_term_exponent=pole_exponent,
    )


def centered_continuum_term(x: float, frequency: float) -> float:
    """Return ``Re(x**(1-it)/(1-it))``."""

    if x <= 0.0:
        raise ValueError("x must be positive")
    z = x ** (1.0 - 1j * frequency) / (1.0 - 1j * frequency)
    return float(z.real)


def centered_continuum_derivative(x: float, frequency: float) -> float:
    """The exact derivative of :func:`centered_continuum_term`."""

    if x <= 0.0:
        raise ValueError("x must be positive")
    return math.cos(frequency * math.log(x))


def matching_zero_mellin_residue(beta: float, multiplicity: int = 1) -> float:
    """Residue after continuum centering at a zero ``beta+i*t``.

    The two conjugate logarithmic derivatives give residue ``-m`` in the
    cosine Dirichlet series.  Partial summation divides it by ``beta``.
    """

    if beta <= 0.0:
        raise ValueError("beta must be positive")
    if multiplicity < 1:
        raise ValueError("multiplicity must be positive")
    return -float(multiplicity) / beta


def pole_mellin_residue(frequency: float, sign: int) -> complex:
    """Residue of both the prime series/s and continuum Mellin term.

    ``sign=+1`` corresponds to the nonreal point ``s=1+i*t`` and
    ``sign=-1`` to ``s=1-i*t``.  Equality of these returned residues is the
    exact pole cancellation in the centered discrepancy.
    """

    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or +1")
    return 1.0 / (2.0 * (1.0 + sign * 1j * frequency))


def support_preserving_factor(
    s: complex, beta: float, ordinate: float, prime: int = 2
) -> complex:
    """Real-conjugate finite Euler factor with zeros at ``beta +/- i*t``.

    The factor is

    ``(1-p**(beta+i*t-s)) * (1-p**(beta-i*t-s))``.

    Multiplying zeta by it changes only logarithmic-derivative coefficients
    at powers of ``p`` and leaves the prime-power frequency support unchanged.
    """

    if not 0.0 < beta < 1.0:
        raise ValueError("beta must lie in (0, 1)")
    if prime < 2 or any(prime % d == 0 for d in range(2, int(math.sqrt(prime)) + 1)):
        raise ValueError("prime must be prime")
    logp = math.log(prime)
    first = 1.0 - cmath.exp((beta + 1j * ordinate - s) * logp)
    second = 1.0 - cmath.exp((beta - 1j * ordinate - s) * logp)
    return first * second


def support_factor_logderivative_coefficient(
    power: int, beta: float, ordinate: float, prime: int = 2
) -> float:
    """Coefficient added to ``-zeta'/zeta`` at ``n=prime**power``.

    It equals ``-2 log(p) p**(k*beta) cos(k*t*log(p))`` and is real.  At every
    integer not a power of ``p`` the added coefficient is exactly zero.
    """

    if power < 1:
        raise ValueError("power must be positive")
    if not 0.0 < beta < 1.0:
        raise ValueError("beta must lie in (0, 1)")
    logp = math.log(prime)
    return -2.0 * logp * prime ** (power * beta) * math.cos(
        power * ordinate * logp
    )


def positive_coefficient_factor(
    s: complex, beta: float, prime: int = 2
) -> complex:
    """Finite Dirichlet factor ``1 + p**(beta-s)``.

    Multiplication by this factor keeps all ordinary Dirichlet coefficients
    positive and inserts zeros on ``Re(s)=beta``.  Its logarithmic derivative
    changes coefficients only at powers of ``p``.
    """

    if not 0.0 < beta < 1.0:
        raise ValueError("beta must lie in (0, 1)")
    if prime < 2 or any(prime % d == 0 for d in range(2, int(math.sqrt(prime)) + 1)):
        raise ValueError("prime must be prime")
    return 1.0 + cmath.exp((beta - s) * math.log(prime))


def positive_factor_zero_ordinate(index: int, prime: int = 2) -> float:
    """A positive zero ordinate of ``1 + p**(beta-s)``.

    The returned ordinate is ``(2*index+1)*pi/log(p)``.
    """

    if index < 0:
        raise ValueError("index must be nonnegative")
    return (2 * index + 1) * math.pi / math.log(prime)


def positive_factor_full_logderivative_coefficient(
    power: int, beta: float, prime: int = 2
) -> float:
    """Full coefficient of ``-F'/F`` at ``p**power``.

    Here ``F(s)=zeta(s)*(1+p**(beta-s))``.  The coefficient is
    ``log(p)*(1+(-1)**(power-1)*p**(power*beta))`` and never vanishes for
    ``0<beta<1``.
    """

    if power < 1:
        raise ValueError("power must be positive")
    if not 0.0 < beta < 1.0:
        raise ValueError("beta must lie in (0, 1)")
    return math.log(prime) * (
        1.0 + (-1.0) ** (power - 1) * prime ** (power * beta)
    )


def positive_factor_dirichlet_coefficient(
    integer: int, beta: float, prime: int = 2
) -> float:
    """Ordinary Dirichlet coefficient of ``zeta(s)*(1+p**(beta-s))``."""

    if integer < 1:
        raise ValueError("integer must be positive")
    if not 0.0 < beta < 1.0:
        raise ValueError("beta must lie in (0, 1)")
    return 1.0 + (prime ** beta if integer % prime == 0 else 0.0)


def fejer_nonzero_nodes_weights(
    order: int, width: float
) -> tuple[tuple[float, ...], tuple[float, ...]]:
    """Return the nonzero-node Fejer QP model.

    There are ``order-1`` nodes ``j*width/(order-1)`` and positive weights
    ``2*(order-j)/(order*(order-1))``.  Their cosine polynomial is bounded
    below by ``-1/(order-1)`` on the whole real line.
    """

    if order < 2:
        raise ValueError("order must be at least two")
    if width <= 0.0:
        raise ValueError("width must be positive")
    nodes = tuple(j * width / (order - 1) for j in range(1, order))
    weights = tuple(
        2.0 * (order - j) / (order * (order - 1))
        for j in range(1, order)
    )
    return nodes, weights


def normalized_fejer_kernel(phase: float, order: int) -> float:
    """Return ``|sum_(r<order) exp(i*r*phase)|^2/order^2``."""

    if order < 2:
        raise ValueError("order must be at least two")
    geometric_sum = sum(cmath.exp(1j * r * phase) for r in range(order))
    return abs(geometric_sum) ** 2 / order**2


def fejer_nonzero_cosine(frequency: float, order: int, width: float) -> float:
    """Evaluate the positive nonzero-node certificate.

    The exact identity is ``(order*F_order(phase)-1)/(order-1)``, where
    ``phase=width*frequency/(order-1)`` and ``F_order`` is nonnegative.
    """

    if width <= 0.0:
        raise ValueError("width must be positive")
    phase = width * frequency / (order - 1)
    return (
        order * normalized_fejer_kernel(phase, order) - 1.0
    ) / (order - 1)


def fejer_exact_minimum_frequency(
    order: int, width: float, zero_index: int = 1
) -> float:
    """Return a frequency where the certificate equals ``-1/(order-1)``."""

    if order < 2:
        raise ValueError("order must be at least two")
    if width <= 0.0:
        raise ValueError("width must be positive")
    if zero_index < 1 or zero_index % order == 0:
        raise ValueError("zero_index must be positive and not divisible by order")
    return 2.0 * math.pi * zero_index * (order - 1) / (order * width)


def fejer_continuum_limit(frequency: float, width: float) -> float:
    """Fixed-frequency limit of the nonzero-node Fejer certificates."""

    if width <= 0.0:
        raise ValueError("width must be positive")
    argument = width * frequency / 2.0
    if argument == 0.0:
        return 1.0
    return (math.sin(argument) / argument) ** 2


def transferred_turan_strip_width(
    qp_power: float,
    comparison_exponent: float,
    *,
    upper_aperture_exponent: float = QP_UPPER_EXPONENT,
) -> float:
    """Strip width delivered by a hypothetical QP-to-prime comparison.

    If the comparison turns ``r_+ <= Y**(-c)`` into a natural prime modulus
    saving of power ``comparison_exponent*c``, Turan gives the high-height
    width ``(comparison_exponent*c/A)**2``.
    """

    if qp_power <= 0.0:
        raise ValueError("qp_power must be positive")
    if comparison_exponent <= 0.0:
        raise ValueError("comparison_exponent must be positive")
    if upper_aperture_exponent <= 0.0:
        raise ValueError("upper_aperture_exponent must be positive")
    return (comparison_exponent * qp_power / upper_aperture_exponent) ** 2
