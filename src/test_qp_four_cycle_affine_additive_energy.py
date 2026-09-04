from qp_four_cycle_affine_additive_energy import (
    affine_additive_energy_ledger,
    interval_additive_energy,
)


def test_long_unequal_slope_chart_embeds_in_aff_times_add() -> None:
    # The long active integer chart from the scaled-additivity theorem.
    center = 97  # 1 mod 6
    rows = ((6 * center, 6), (5 * (center + 2), 5))
    columns = ((5 * (center + 1), -5), (5 * (center + 7), -5))
    colors = (
        25 * (center - 1) // 6,
        25 * (center - 7) // 6,
        5 * (center - 3),
        5 * (center - 9),
    )
    ledger = affine_additive_energy_ledger(rows, columns, colors)
    assert ledger.affine_identity
    assert ledger.additive_identity
    d11, d12, d21, d22 = ledger.tags
    assert d11 + d22 == d12 + d21


def test_affine_identity_does_not_need_the_color_relation() -> None:
    rows = ((11, 2), (17, 3))
    columns = ((23, -5), (29, 7))
    ledger = affine_additive_energy_ledger(rows, columns, (1, 2, 4, 8))
    assert ledger.affine_identity
    assert not ledger.additive_identity


def test_one_affine_fibre_has_cubic_tag_energy() -> None:
    for length in (1, 2, 7, 31):
        brute_force = sum(
            1
            for a in range(1, length + 1)
            for b in range(1, length + 1)
            for c in range(1, length + 1)
            for d in range(1, length + 1)
            if b - a == d - c
        )
        assert interval_additive_energy(length) == brute_force
    length = 100
    assert interval_additive_energy(length) > length**3 // 2
    assert interval_additive_energy(length) < length**3
