"""Finite anisotropic outer-L2 theorem for two error windows.

The theorem proved here is deliberately finite and explicit.  If the
physical outer variable is genuinely Fourier-dual to the reduced error
difference ``(e-f)/g``, Parseval and a fiber count retain the narrower of
the two error windows.  The module also records why an unspecified outer
``L2`` norm, or repeated atoms with the same error labels, does not imply
that gain.
"""

from __future__ import annotations

import cmath
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt, pi
from typing import Mapping, Sequence

from qp_coupled_cusp_fejer_inverse import ReducedSymmetricCuspData


@dataclass(frozen=True)
class DifferenceAtom:
    """One selected atom carrying two integral error labels."""

    left_error: int
    right_error: int
    tag: int = 0


@dataclass(frozen=True)
class DifferenceFiberAudit:
    """Exact fiber data for the reduced error-difference character."""

    narrow_radius: int
    wide_radius: int
    modulus: int
    content: int
    narrow_cardinality: int
    wide_cardinality: int
    selected_atoms: int
    distinct_error_pairs: int
    maximum_fiber: int
    pair_subset_bound: int
    squared_anisotropic_ratio: Fraction


@dataclass(frozen=True)
class UniversalOffContentBlowup:
    """Integral blow-up coordinates for a reduced symmetric cusp point."""

    capital_c: int
    transverse_u: int
    height_h: int
    left_factor: int
    right_factor: int
    reduced_difference: int


def _reduced_label(atom: DifferenceAtom, content: int, modulus: int) -> int:
    difference = atom.left_error - atom.right_error
    if difference % content:
        raise ValueError("the error difference must be divisible by content")
    return (difference // content) % modulus


def full_error_rectangle(
    narrow_radius: int, wide_radius: int, content: int = 1
) -> tuple[DifferenceAtom, ...]:
    """Return the admissible error pairs in two centered windows."""

    if narrow_radius < 0 or wide_radius < narrow_radius or content <= 0:
        raise ValueError("require 0<=narrow_radius<=wide_radius and content>0")
    return tuple(
        DifferenceAtom(e, f)
        for e in range(-narrow_radius, narrow_radius + 1)
        for f in range(-wide_radius, wide_radius + 1)
        if (e - f) % content == 0
    )


def difference_fiber_audit(
    narrow_radius: int,
    wide_radius: int,
    modulus: int,
    *,
    content: int = 1,
    atoms: Sequence[DifferenceAtom] | None = None,
) -> DifferenceFiberAudit:
    """Audit the exact fibers and the mask-only anisotropic norm gain.

    The no-alias condition

    ``content*modulus > 2*(narrow_radius+wide_radius)``

    makes congruence of reduced differences equivalent to equality in the
    represented range.  For a genuine subset of error *pairs*, each fiber
    then contains at most ``2*narrow_radius+1`` atoms: once the narrow error
    is chosen, the wide error is forced.

    Repeated tagged atoms are permitted so that the exact multiplicity loss
    is visible.  In that case ``maximum_fiber`` remains the valid bound, but
    the mask-only ``pair_subset_bound`` need not hold.
    """

    if narrow_radius < 0 or wide_radius < narrow_radius or content <= 0:
        raise ValueError("require 0<=narrow_radius<=wide_radius and content>0")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    if content * modulus <= 2 * (narrow_radius + wide_radius):
        raise ValueError("the reduced difference wraps modulo the outer torus")
    chosen = (
        full_error_rectangle(narrow_radius, wide_radius, content)
        if atoms is None
        else tuple(atoms)
    )
    for atom in chosen:
        if abs(atom.left_error) > narrow_radius or abs(atom.right_error) > wide_radius:
            raise ValueError("an atom lies outside the stated error windows")
    fibers = Counter(_reduced_label(atom, content, modulus) for atom in chosen)
    narrow_cardinality = 2 * narrow_radius + 1
    wide_cardinality = 2 * wide_radius + 1
    return DifferenceFiberAudit(
        narrow_radius=narrow_radius,
        wide_radius=wide_radius,
        modulus=modulus,
        content=content,
        narrow_cardinality=narrow_cardinality,
        wide_cardinality=wide_cardinality,
        selected_atoms=len(chosen),
        distinct_error_pairs=len({(a.left_error, a.right_error) for a in chosen}),
        maximum_fiber=max(fibers.values(), default=0),
        pair_subset_bound=narrow_cardinality,
        squared_anisotropic_ratio=Fraction(narrow_cardinality, wide_cardinality),
    )


def grouped_difference_energy(
    atoms: Sequence[DifferenceAtom],
    coefficients: Sequence[complex],
    modulus: int,
    *,
    content: int = 1,
) -> float:
    """Return the Parseval-side energy grouped by reduced difference."""

    if len(atoms) != len(coefficients):
        raise ValueError("atoms and coefficients must have the same length")
    grouped: dict[int, complex] = defaultdict(complex)
    for atom, coefficient in zip(atoms, coefficients):
        grouped[_reduced_label(atom, content, modulus)] += coefficient
    return sum(abs(value) ** 2 for value in grouped.values())


def fourier_difference_energy(
    atoms: Sequence[DifferenceAtom],
    coefficients: Sequence[complex],
    modulus: int,
    *,
    content: int = 1,
) -> float:
    """Return the normalized outer-torus L2 energy by direct DFT."""

    if modulus <= 0 or len(atoms) != len(coefficients):
        raise ValueError("require a positive modulus and matching sequences")
    labels = [_reduced_label(atom, content, modulus) for atom in atoms]
    total = 0.0
    for outer in range(modulus):
        value = sum(
            coefficient * cmath.exp(2j * pi * outer * label / modulus)
            for label, coefficient in zip(labels, coefficients)
        )
        total += abs(value) ** 2
    return total / modulus


def exact_outer_l2_upper_bound(
    atoms: Sequence[DifferenceAtom],
    coefficients: Sequence[complex],
    modulus: int,
    *,
    content: int = 1,
) -> float:
    """Return ``max_fiber * ||coefficients||_2^2``.

    Parseval followed by Cauchy on each fiber proves that this bounds both
    energy functions above.  The constant is sharp for unrestricted scalar
    coefficients supported on a largest fiber.
    """

    if len(atoms) != len(coefficients):
        raise ValueError("atoms and coefficients must have the same length")
    fibers = Counter(_reduced_label(atom, content, modulus) for atom in atoms)
    maximum = max(fibers.values(), default=0)
    return maximum * sum(abs(value) ** 2 for value in coefficients)


def collapsed_outer_energy(coefficients: Sequence[complex]) -> float:
    """Energy when every nominal difference character collapses to one mode."""

    return abs(sum(coefficients)) ** 2


def anisotropic_endpoint_ledger() -> Mapping[str, Fraction]:
    """Return the endpoint exponent gain and the resulting no-wrap total."""

    narrow = Fraction(1)
    wide = Fraction(7, 6)
    gain = (narrow - wide) / 2
    no_wrap_total = Fraction(55, 96)
    return {
        "narrow_error_width": narrow,
        "wide_error_width": wide,
        "sqrt_narrow_over_wide_gain": gain,
        "no_wrap_total_before_gain": no_wrap_total,
        "no_wrap_total_after_gain": no_wrap_total + gain,
        "square_root_target": Fraction(1, 2),
        "closing_margin": Fraction(1, 2) - (no_wrap_total + gain),
    }


def universal_off_content_blowup(
    point: ReducedSymmetricCuspData,
) -> UniversalOffContentBlowup:
    """Return and verify the universal ``(C,U,H)`` blow-up identities.

    With ``ell=p^2-d^2``, put

    ``C=2*d^2*Q-g*p*ell``, ``U=2*d*y-g*ell``, and ``H=C-2*p*U``.

    Then, exactly,

    ``4*d^2*e=g*(p-d)*(H-d*U)-U^2``,
    ``4*d^2*f=g*(p+d)*(H+d*U)-U^2``, and
    ``2*d*n=-(H+p*U)``.
    """

    if point.d == 0 or point.p <= abs(point.d):
        raise ValueError("require a nonsingular noncentral primitive direction")
    Q, y, g, p, d = point.Q, point.y, point.g, point.p, point.d
    ell = p * p - d * d
    capital_c = 2 * d * d * Q - g * p * ell
    transverse_u = 2 * d * y - g * ell
    height_h = capital_c - 2 * p * transverse_u
    left_factor = height_h - d * transverse_u
    right_factor = height_h + d * transverse_u
    assert 4 * d * d * point.e == g * (p - d) * left_factor - transverse_u**2
    assert 4 * d * d * point.f == g * (p + d) * right_factor - transverse_u**2
    assert 2 * d * point.n == -(height_h + p * transverse_u)
    assert point.e - point.f == g * point.n
    return UniversalOffContentBlowup(
        capital_c=capital_c,
        transverse_u=transverse_u,
        height_h=height_h,
        left_factor=left_factor,
        right_factor=right_factor,
        reduced_difference=point.n,
    )


def forced_narrow_zero_factor(
    point: ReducedSymmetricCuspData, narrow_band: int
) -> Mapping[str, int]:
    """Force ``H-dU=0`` under the exact integral low-height gate.

    The sufficient condition is

    ``g*(p-d)>4*d^2*narrow_band+U^2``.

    If it holds and ``|e|<=narrow_band``, integrality forces the left factor
    to vanish.  Then ``U=2*d*z`` for an integer ``z``, and

    ``e=-z^2``, ``n=-(p+d)z``,
    ``p | Q-z``, and ``p+d | Q+z``.
    """

    if narrow_band < 0 or abs(point.e) > narrow_band:
        raise ValueError("the point must obey the stated narrow error band")
    blowup = universal_off_content_blowup(point)
    d, p, g = point.d, point.p, point.g
    threshold = 4 * d * d * narrow_band + blowup.transverse_u**2
    if g * (p - d) <= threshold:
        raise ValueError("the exact low-height gate does not hold")
    assert blowup.left_factor == 0
    z_fraction = Fraction(blowup.transverse_u, 2 * d)
    assert z_fraction * z_fraction == -point.e
    if z_fraction.denominator != 1:
        raise AssertionError("a rational number with integral square is integral")
    z = z_fraction.numerator
    assert point.e == -z * z
    assert point.n == -(p + d) * z
    assert (point.Q - z) % p == 0
    assert (point.Q + z) % (p + d) == 0
    return {
        "z": z,
        "left_factor": blowup.left_factor,
        "p_divisor_target": point.Q - z,
        "p_plus_d_divisor_target": point.Q + z,
        "gate_denominator": g * (p - d),
        "gate_numerator_majorant": threshold,
    }


def _positive_divisor_count(value: int) -> int:
    if value <= 0:
        raise ValueError("the divisor target must be positive")
    total = 0
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor == 0:
            total += 1 if divisor * divisor == value else 2
    return total


def forced_narrow_zero_factor_fixed_q_majorant(Q: int, narrow_band: int) -> int:
    """Return the shifted-divisor majorant for the forced zero-factor branch.

    For every ``|z|<=sqrt(narrow_band)``, the preceding theorem injects a
    point into a choice of divisors

    ``p | Q-z`` and ``p+d | Q+z``.

    The returned sum is therefore an exact finite upper bound before the
    primitive, collar, positivity, and reconstruction constraints are
    imposed.  Standard divisor estimates make it
    ``O(sqrt(narrow_band)*Q^o(1))`` when ``sqrt(narrow_band)=o(Q)``.
    """

    if Q <= 1 or narrow_band < 0 or isqrt(narrow_band) >= Q:
        raise ValueError("require Q>1 and 0<=sqrt(narrow_band)<Q")
    return sum(
        _positive_divisor_count(Q - z) * _positive_divisor_count(Q + z)
        for z in range(-isqrt(narrow_band), isqrt(narrow_band) + 1)
    )


def residual_three_count_exponent_ledger(
    u: Fraction,
    v: Fraction,
    gamma: Fraction,
    primitive_pi: Fraction,
) -> Mapping[str, Fraction | bool | str]:
    """Optimize three scalar counts in the residual ``A*P^2/Q>=1`` range.

    Write

    ``A=D^(1+u)``, ``B=D^(1+v)``, ``G=D^gamma``, and ``P=D^primitive_pi``.

    The three supplied counts are

    ``sqrt(G*P^5/Q)``, ``B*G*P^2/Q``, and
    ``G*sqrt(G*P^3/Q)*(1+A*P^2/Q)``.

    In an occupied residual cell, all displayed power factors are at least
    one.  The function returns their exact exponents, their minimum, and the
    equivalent union of half-spaces for closing at ``sqrt(A)``.
    """

    u, v, gamma, primitive_pi = map(Fraction, (u, v, gamma, primitive_pi))
    q = Fraction(33, 16)
    if min(u, v, gamma, primitive_pi) < 0 or u > v or 2 * u + 3 * v >= Fraction(1, 2):
        raise ValueError("require 0<=u<=v and 2u+3v<1/2")
    if u + 2 * primitive_pi < Fraction(17, 16):
        raise ValueError("the cell is below the residual A*P^2/Q threshold")
    if gamma + 3 * primitive_pi < q:
        raise ValueError("the dyadic physical height d would be below one")
    if gamma + primitive_pi > q:
        raise ValueError("the dyadic physical height would exceed P")

    farey = (gamma + 5 * primitive_pi - q) / 2
    cubic = v + gamma + 2 * primitive_pi - Fraction(17, 16)
    fixed_factor = (
        gamma
        + (gamma + 3 * primitive_pi - q) / 2
        + u
        + 2 * primitive_pi
        - Fraction(17, 16)
    )
    assert min(farey, cubic, fixed_factor) >= 0
    target = (1 + u) / 2
    thresholds = {
        "farey": Fraction(49, 16) + u - 5 * primitive_pi,
        "cubic": Fraction(25, 16) + u / 2 - v - 2 * primitive_pi,
        "fixed_factor": Fraction(83, 48) - u / 3 - 7 * primitive_pi / 3,
    }
    counts = {"farey": farey, "cubic": cubic, "fixed_factor": fixed_factor}
    best_name = min(counts, key=counts.get)
    best = counts[best_name]
    union_threshold = max(thresholds.values())
    return {
        "farey_exponent": farey,
        "cubic_exponent": cubic,
        "fixed_factor_exponent": fixed_factor,
        "target": target,
        "best_exponent": best,
        "best_mechanism": best_name,
        "closed": best <= target,
        "margin": target - best,
        "farey_gamma_ceiling": thresholds["farey"],
        "cubic_gamma_ceiling": thresholds["cubic"],
        "fixed_factor_gamma_ceiling": thresholds["fixed_factor"],
        "union_gamma_ceiling": union_threshold,
        "union_test": gamma <= union_threshold,
    }
