from qp_four_cycle_parabolic_inverse import (
    plane_section_infinity_ledger,
    translation_grid_plane_directions,
)


def test_translation_grid_section_is_parabolic() -> None:
    first, second = translation_grid_plane_directions(
        (10_000, 10_017),
        (10_000, 10_023),
    )
    ledger = plane_section_infinity_ledger(first, second)
    assert ledger.first_square_coefficient != 0
    assert ledger.second_square_coefficient == 0
    assert ledger.mixed_coefficient == 0
    assert ledger.is_parabolic


def test_generic_plane_section_has_two_points_at_infinity() -> None:
    ledger = plane_section_infinity_ledger(
        (1, 0, 0, 1),
        (0, 1, 1, 0),
    )
    assert ledger.infinity_discriminant != 0
    assert not ledger.is_parabolic

