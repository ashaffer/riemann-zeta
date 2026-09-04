"""Exact ledgers for the dense-defect continued-fraction energy gate.

The companion report proves the lattice and Freiman statements.  This file
keeps the critical rational exponents and the finite determinant divisibility
check executable; it does not claim the open reciprocal-energy theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class DenseDefectLedger:
    q_in_degree: Fraction
    fan_threshold: Fraction
    energy_threshold: Fraction
    adjacent_gap: Fraction
    popular_chords: Fraction
    inverse_step_endpoint: Fraction
    wrap_count: Fraction
    branch_length: Fraction
    branch_occupancy: Fraction
    cf_chord_scale: Fraction
    density_forced_chord_scale: Fraction
    density_to_cf_gap: Fraction
    carrier_alphabet_deficit: Fraction
    packet_determinant_scale: Fraction
    packet_determinant_margin: Fraction
    packet_step_scale: Fraction
    reciprocal_three_ap_scale: Fraction
    reciprocal_three_ap_forbidden_gap: Fraction
    mixed_difference_product_cutoff: Fraction
    narrow_rectangle_energy_bound: Fraction
    narrow_to_target_margin: Fraction


def dense_defect_ledger() -> DenseDefectLedger:
    """Return the exact powers of ``D`` in the critical dense-defect audit."""

    q = Fraction(33, 16)
    fan = Fraction(7, 8)
    inverse = Fraction(73, 64)
    packet_determinant = Fraction(3, 2)
    return DenseDefectLedger(
        q_in_degree=q,
        fan_threshold=fan,
        energy_threshold=4 * fan - 1,
        adjacent_gap=1 - fan,
        popular_chords=2 * fan - 1,
        inverse_step_endpoint=inverse,
        wrap_count=inverse + 1 - q,
        branch_length=q - inverse,
        branch_occupancy=fan - (inverse + 1 - q),
        cf_chord_scale=q - 1,
        density_forced_chord_scale=q - fan,
        density_to_cf_gap=(q - fan) - (q - 1),
        carrier_alphabet_deficit=inverse - (2 * fan - 1),
        packet_determinant_scale=packet_determinant,
        packet_determinant_margin=q - packet_determinant,
        packet_step_scale=Fraction(1, 2),
        reciprocal_three_ap_scale=q / 2,
        reciprocal_three_ap_forbidden_gap=q / 2 - Fraction(1, 2),
        mixed_difference_product_cutoff=q,
        narrow_rectangle_energy_bound=Fraction(2),
        narrow_to_target_margin=4 * fan - 1 - Fraction(2),
    )


def reciprocal_second_difference(
    carrier_constant: Fraction,
    first_completion: int,
    completion_step: int,
) -> Fraction:
    """Return the exact second difference of ``C/a`` on a completion 3-AP.

    This replays the rational identity in equation (4.9) of the companion
    report, before the ``O(D/q)`` rounding errors from the three carriers.
    """

    a = first_completion
    s = completion_step
    if min(a, a + s, a + 2 * s) <= 0:
        raise ValueError("all three completion coordinates must be positive")
    direct = (
        carrier_constant / a
        - 2 * carrier_constant / (a + s)
        + carrier_constant / (a + 2 * s)
    )
    factored = (
        2
        * carrier_constant
        * s
        * s
        / (a * (a + s) * (a + 2 * s))
    )
    if direct != factored:
        raise AssertionError("reciprocal second-difference identity failed")
    return direct


def reciprocal_mixed_difference(
    carrier_constant: Fraction,
    first_completion: int,
    first_step: int,
    second_step: int,
) -> Fraction:
    """Return the exact mixed difference of ``C/a`` on a rectangle.

    The four coordinates are ``a``, ``a+r``, ``a+s``, and ``a+r+s``.
    This is the rational identity underlying the broad-rectangle reduction.
    """

    a = first_completion
    r = first_step
    s = second_step
    coordinates = (a, a + r, a + s, a + r + s)
    if min(coordinates) <= 0:
        raise ValueError("all four completion coordinates must be positive")
    direct = (
        carrier_constant / a
        + carrier_constant / (a + r + s)
        - carrier_constant / (a + r)
        - carrier_constant / (a + s)
    )
    factored = (
        carrier_constant
        * r
        * s
        * (2 * a + r + s)
        / (a * (a + r) * (a + s) * (a + r + s))
    )
    if direct != factored:
        raise AssertionError("reciprocal mixed-difference identity failed")
    return direct


def completion_lattice_determinant(
    x: int,
    y: int,
    first: tuple[int, int],
    second: tuple[int, int],
) -> tuple[int, int]:
    """Return the determinant and its quotient by ``y``.

    A completion vector ``(d,s)`` belongs to the defect lattice precisely
    when ``x*s == d (mod y)``.  The determinant of two such vectors is a
    multiple of ``y``.
    """

    if not 0 < x < y:
        raise ValueError("expected positive ordered endpoints")
    d1, s1 = first
    d2, s2 = second
    if (x * s1 - d1) % y or (x * s2 - d2) % y:
        raise ValueError("a vector is not in the completion lattice")
    determinant = d1 * s2 - d2 * s1
    if determinant % y:
        raise AssertionError("completion-lattice determinant lost divisibility")
    return determinant, determinant // y


def low_rectangle_forces_collinearity(
    y: int,
    first: tuple[int, int],
    second: tuple[int, int],
    defect_radius: int,
    completion_radius: int,
) -> bool:
    """Check the numerical part of the one-low-rectangle lemma.

    The caller is responsible for checking lattice membership.  If the
    vectors fit in the stated rectangle and ``2*R*S<y``, a determinant that
    is a multiple of ``y`` must vanish.
    """

    if min(y, defect_radius, completion_radius) <= 0:
        raise ValueError("all scales must be positive")
    if 2 * defect_radius * completion_radius >= y:
        raise ValueError("the rectangle is not below the determinant quantum")
    for defect, completion in (first, second):
        if abs(defect) > defect_radius or abs(completion) > completion_radius:
            raise ValueError("a vector lies outside the supplied rectangle")
    return first[0] * second[1] == second[0] * first[1]
