from qp_multilevel_translation_grid import (
    RESIDUAL_SCALE,
    audit_multilevel_translation_grid,
    multilevel_entry,
    multilevel_product_increment,
)


def test_exact_first_order_cancellation_identity() -> None:
    m = 10**9
    h, ell, t = 17, 23, 211
    for i in (0, 1):
        for j in (0, 1):
            a, b, c = multilevel_entry(m, h, ell, t, i, j)
            assert a * b * c - m**3 == multilevel_product_increment(
                m, i * h, j * ell, t
            )


def test_multilevel_grid_has_polynomial_reuse_but_D_weighted_mass() -> None:
    ledger = audit_multilevel_translation_grid(m=20_000_000, length=10)
    assert ledger.degree_scale == RESIDUAL_SCALE * 100
    assert ledger.patches == 110
    assert ledger.completions_per_patch == 11
    assert ledger.maximum_color_patch_reuse == ledger.patches
    assert ledger.color_support_size == 3 * ledger.length + 1
    # The exact ratio tends to 1/(9*RESIDUAL_SCALE), so the normalized
    # pair energy is genuinely of order D even though its fixed constant is
    # small because we chose a generous literal product-window cutoff.
    assert ledger.flat_weighted_offdiagonal_mass > ledger.degree_scale / 20_000
    assert ledger.flat_weighted_offdiagonal_mass < ledger.degree_scale / 10_000
    expected_spiked_mass = (
        ledger.length ** 0.5 * (ledger.length + 1) ** 2 / 16
    )
    assert ledger.spiked_weighted_offdiagonal_mass == expected_spiked_mass
    # The spiked mass is Theta(L^(5/2))=Theta(D^(5/4)), whereas the flat
    # mass is only Theta(D).
    assert (
        ledger.spiked_weighted_offdiagonal_mass
        / ledger.flat_weighted_offdiagonal_mass
        > 0.5 * ledger.length ** 0.5
    )
    assert ledger.normalized_residual_cap < 1
