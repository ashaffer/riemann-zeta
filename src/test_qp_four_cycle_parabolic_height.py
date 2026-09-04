from fractions import Fraction

from qp_four_cycle_parabolic_height import (
    binary_determinant_discriminant,
    choose_nondegenerate_slice_plane,
    degenerate_plane_direction,
    eleven_thirty_seconds_exponents,
    four_elevenths_exponents,
    generalized_tangent_entry,
    height_split_exponents,
    middle_slice_exponents,
    scaled_additivity_ledger,
    twenty_three_sixty_fourths_exponents,
)


def test_unequal_slope_chart_is_scaled_but_not_raw_additive() -> None:
    scale = 100_003
    entries = {
        (i, j): generalized_tangent_entry(scale, 0, i, j)
        for i in (0, 1)
        for j in (0, 1)
    }
    colors = (
        entries[(0, 0)].color,
        entries[(0, 1)].color,
        entries[(1, 0)].color,
        entries[(1, 1)].color,
    )
    ledger = scaled_additivity_ledger(colors, (6, 5), (5, 5))
    assert ledger.raw_additive_defect == -5
    assert ledger.scaled_additive_defect == 0
    assert ledger.first_step == 750
    assert ledger.second_step == 250
    assert ledger.color_determinant == -250
    assert ledger.slope_product == 750
    assert ledger.scaled_determinant == -187_500


def test_generalized_tangent_product_identity() -> None:
    scale = 100_003
    parameter = 137
    row_offsets = (0, 2)
    column_offsets = (1, 7)
    for row_index in (0, 1):
        for column_index in (0, 1):
            entry = generalized_tangent_entry(
                scale,
                parameter,
                row_index,
                column_index,
            )
            first = row_offsets[row_index] + parameter
            second = column_offsets[column_index] - parameter
            total = first + second
            expected_defect = 125 * (
                scale * (first * second - total * total)
                - total * first * second
            )
            assert entry.product_defect == expected_defect
            assert entry.target == 125 * scale**3


def test_height_split_exponent_balance() -> None:
    threshold, trace, operator = height_split_exponents()
    assert threshold == Fraction(3, 8)
    assert trace == Fraction(11, 8)
    assert operator == Fraction(11, 32)
    assert 1 + threshold == Fraction(5, 2) - 3 * threshold


def test_degenerate_binary_plane_recovers_rank_one_direction() -> None:
    # det(x*V+y*W)=-(x+y)^2, with repeated direction V-W=E_11.
    first = (0, 1, 1, 0)
    second = (-1, 1, 1, 0)
    ledger = degenerate_plane_direction(first, second)
    assert ledger.discriminant == 0
    assert ledger.root_coordinates == (1, -1)
    assert ledger.direction == (1, 0, 0, 0)
    assert ledger.direction_determinant == 0


def test_constant_shear_finds_nondegenerate_binary_slice() -> None:
    # Traceless matrices carry det=-x^2-yz.  The plane at t=0 is
    # degenerate, while adding V3 once makes its discriminant nonzero.
    first = (1, 0, 0, -1)
    second = (0, 1, 0, 0)
    third = (0, 0, 1, 0)
    assert binary_determinant_discriminant(first, second) == 0
    choice = choose_nondegenerate_slice_plane(first, second, third)
    assert choice.shear == 1
    assert choice.sheared_second == (0, 1, 1, 0)
    assert choice.binary_discriminant != 0


def test_middle_and_four_elevenths_exponents() -> None:
    gap, nondegenerate, degenerate = middle_slice_exponents()
    assert gap == Fraction(5, 176)
    assert nondegenerate == Fraction(181, 176)
    assert degenerate == Fraction(247, 176)
    cutoff, trace, operator = four_elevenths_exponents()
    assert cutoff == Fraction(1, 11)
    assert trace == Fraction(16, 11)
    assert operator == Fraction(4, 11)
    transverse = Fraction(1, 2) + operator * Fraction(16, 33)
    assert transverse == Fraction(491, 726)


def test_twenty_three_sixty_fourths_balance() -> None:
    cutoff, slice_loss, trace, operator = (
        twenty_three_sixty_fourths_exponents()
    )
    assert cutoff == Fraction(9, 8)
    assert slice_loss == Fraction(1, 16)
    assert trace == Fraction(23, 16)
    assert operator == Fraction(23, 64)
    transverse = Fraction(1, 2) + operator * Fraction(16, 33)
    assert transverse == Fraction(89, 132)


def test_eleven_thirty_seconds_balance() -> None:
    product_cutoff, lambda2_cutoff, completion, trace, operator = (
        eleven_thirty_seconds_exponents()
    )
    assert product_cutoff == Fraction(17, 16)
    assert lambda2_cutoff == Fraction(5, 8)
    assert completion == Fraction(3, 8)
    assert trace == Fraction(11, 8)
    assert operator == Fraction(11, 32)
    transverse = Fraction(1, 2) + operator * Fraction(16, 33)
    assert transverse == Fraction(2, 3)
