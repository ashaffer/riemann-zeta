from fractions import Fraction
from math import sqrt

import pytest

from qp_anisotropic_outer_l2 import (
    DifferenceAtom,
    anisotropic_endpoint_ledger,
    collapsed_outer_energy,
    difference_fiber_audit,
    exact_outer_l2_upper_bound,
    forced_narrow_zero_factor,
    forced_narrow_zero_factor_fixed_q_majorant,
    fourier_difference_energy,
    full_error_rectangle,
    grouped_difference_energy,
    residual_three_count_exponent_ledger,
    universal_off_content_blowup,
)
from qp_coupled_cusp_fejer_inverse import reduced_symmetric_cusp_data


def test_no_wrap_pair_fiber_retains_the_narrow_window() -> None:
    audit = difference_fiber_audit(2, 7, 31)
    assert audit.narrow_cardinality == 5
    assert audit.wide_cardinality == 15
    assert audit.maximum_fiber == 5
    assert audit.maximum_fiber == audit.pair_subset_bound
    assert audit.squared_anisotropic_ratio == Fraction(1, 3)


def test_difference_character_parseval_and_sharp_fiber_bound() -> None:
    atoms = (
        DifferenceAtom(-2, 1),
        DifferenceAtom(-1, -1),
        DifferenceAtom(0, 3),
        DifferenceAtom(1, 1),
        DifferenceAtom(2, 5),
    )
    coefficients = (1 + 2j, -3j, 2 - 1j, -1 + 4j, 3 + 1j)
    direct = fourier_difference_energy(atoms, coefficients, 31)
    grouped = grouped_difference_energy(atoms, coefficients, 31)
    upper = exact_outer_l2_upper_bound(atoms, coefficients, 31)
    assert abs(direct - grouped) < 1.0e-10
    assert grouped <= upper + 1.0e-12

    diagonal = tuple(DifferenceAtom(e, e) for e in range(-2, 3))
    flat = tuple(1 / sqrt(5) for _ in diagonal)
    assert abs(grouped_difference_energy(diagonal, flat, 31) - 5) < 1.0e-12
    assert abs(exact_outer_l2_upper_bound(diagonal, flat, 31) - 5) < 1.0e-12


def test_arbitrary_selected_pair_subset_keeps_the_same_bound() -> None:
    rectangle = full_error_rectangle(3, 9)
    selected = tuple(
        atom
        for index, atom in enumerate(rectangle)
        if (3 * atom.left_error + 5 * atom.right_error + index) % 4
    )
    audit = difference_fiber_audit(3, 9, 41, atoms=selected)
    assert audit.distinct_error_pairs == audit.selected_atoms
    assert audit.maximum_fiber <= 7


def test_collapsed_outer_phase_and_repeated_atoms_are_exact_obstructions() -> None:
    rectangle = full_error_rectangle(2, 7)
    flat = tuple(1 / sqrt(len(rectangle)) for _ in rectangle)
    # If all nominal characters are the same outer vector, the energy is
    # |rectangle|=5*15, rather than at most the narrow fiber constant 5.
    assert abs(collapsed_outer_energy(flat) - 75) < 1.0e-12
    assert collapsed_outer_energy(flat) > 5 * sum(abs(x) ** 2 for x in flat)

    copies = tuple(DifferenceAtom(0, 0, tag) for tag in range(8))
    copied_flat = tuple(1 / sqrt(8) for _ in copies)
    audit = difference_fiber_audit(2, 7, 31, atoms=copies)
    assert audit.maximum_fiber == 8 > audit.pair_subset_bound
    assert abs(grouped_difference_energy(copies, copied_flat, 31) - 8) < 1.0e-12


def test_wrap_is_rejected_and_endpoint_gain_would_close_numerically() -> None:
    with pytest.raises(ValueError, match="wraps"):
        difference_fiber_audit(2, 7, 18)
    ledger = anisotropic_endpoint_ledger()
    assert ledger["sqrt_narrow_over_wide_gain"] == -Fraction(1, 12)
    assert ledger["no_wrap_total_after_gain"] == Fraction(47, 96)
    assert ledger["closing_margin"] == Fraction(1, 96)


def test_universal_blowup_and_exact_low_height_zero_factor() -> None:
    # p=7,d=1,g=2, with the narrow one-band cancellation e=-1.
    point = reduced_symmetric_cusp_data(351, 49, 6, 8)
    blowup = universal_off_content_blowup(point)
    assert (
        blowup.capital_c,
        blowup.transverse_u,
        blowup.height_h,
        blowup.left_factor,
        blowup.right_factor,
    ) == (30, 2, 2, 0, 4)
    forced = forced_narrow_zero_factor(point, 1)
    assert forced["z"] == 1
    assert forced["gate_denominator"] == 12
    assert forced["gate_numerator_majorant"] == 8
    assert forced["p_divisor_target"] == 350
    assert forced["p_plus_d_divisor_target"] == 352
    assert 350 % 7 == 0 and 352 % 8 == 0
    with pytest.raises(ValueError, match="gate"):
        forced_narrow_zero_factor(point, 2)


def test_fixed_completion_sum_does_not_fourier_separate_reduced_difference() -> None:
    first = reduced_symmetric_cusp_data(1009, -144, 24, 18)
    second = reduced_symmetric_cusp_data(1009, -100, 11, 9)
    assert first.n == 1 and second.n == 9
    # Both belong to the same physical completion level S=2Q.
    assert 2 * first.Q == 2 * second.Q == 2018
    assert universal_off_content_blowup(first).reduced_difference == 1
    assert universal_off_content_blowup(second).reduced_difference == 9


def test_zero_factor_shifted_divisor_sum_is_a_valid_finite_majorant() -> None:
    majorant = forced_narrow_zero_factor_fixed_q_majorant(351, 1)
    # The actual fixture injects into z=1, p|350, p+d|352.
    assert majorant >= 1


def test_residual_three_count_polytope_has_exact_closing_cells() -> None:
    # At the AP^2/Q=1 and d~1 corner, both the cubic and fixed-factor
    # counts lie below sqrt(A).
    corner = residual_three_count_exponent_ledger(
        Fraction(), Fraction(), Fraction(15, 32), Fraction(17, 32)
    )
    assert corner["farey_exponent"] == Fraction(17, 32)
    assert corner["cubic_exponent"] == Fraction(15, 32)
    assert corner["fixed_factor_exponent"] == Fraction(15, 32)
    assert corner["target"] == Fraction(1, 2)
    assert corner["closed"] is True
    assert corner["union_test"] is True

    # A cell where only the Farey count reaches the target.
    farey = residual_three_count_exponent_ledger(
        Fraction(1, 24),
        Fraction(1, 24),
        Fraction(51, 96),
        Fraction(49, 96),
    )
    assert farey["best_mechanism"] == "farey"
    assert farey["farey_exponent"] == Fraction(49, 96)
    assert farey["target"] == Fraction(50, 96)
    assert farey["closed"] is True

    cubic = residual_three_count_exponent_ledger(
        Fraction(), Fraction(), Fraction(127, 256), Fraction(17, 32)
    )
    assert cubic["best_mechanism"] == "cubic"
    assert cubic["cubic_exponent"] == Fraction(127, 256)
    assert cubic["farey_exponent"] > Fraction(1, 2)
    assert cubic["fixed_factor_exponent"] > Fraction(1, 2)

    fixed = residual_three_count_exponent_ledger(
        Fraction(), Fraction(1, 10), Fraction(23, 48), Fraction(17, 32)
    )
    assert fixed["best_mechanism"] == "fixed_factor"
    assert fixed["fixed_factor_exponent"] == Fraction(31, 64)
    assert fixed["farey_exponent"] > Fraction(1, 2)
    assert fixed["cubic_exponent"] > Fraction(1, 2)

    # Raising gamma past all three ceilings leaves a genuine residual cell.
    failed = residual_three_count_exponent_ledger(
        Fraction(), Fraction(1, 7), Fraction(), Fraction(43, 48)
    )
    assert failed["closed"] is False
    assert failed["union_test"] is False
    assert min(
        failed["farey_exponent"],
        failed["cubic_exponent"],
        failed["fixed_factor_exponent"],
    ) > Fraction(1, 2)
