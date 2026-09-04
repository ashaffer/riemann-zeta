import mpmath as mp
from fractions import Fraction

from harmonic_schur_collar_probe import (
    actual_form_entry,
    analyze_mixed_collar,
    analyze_nested_collar,
    arch_entry,
    generalized_extreme,
    reference_form,
    unequal_hat_overlap,
    wplus_entry,
    wplus_diagonal,
)
from hp_margins import Omega, arch_diagonal, hp_form


def test_wplus_reference_is_positive_on_small_grid():
    with mp.workdps(35):
        h = reference_form(mp.mpf("1.7"), 7, dps=30)
        vals = mp.eigsy(h, eigvals_only=True)
        assert min(vals[i] for i in range(vals.rows)) > 0
        assert wplus_diagonal(0, mp.mpf("0.2")) > 0


def test_unequal_kernel_reduces_to_toeplitz_kernel():
    with mp.workdps(35):
        d = mp.mpf("0.17")
        for k in range(5):
            v = k * d
            assert abs(unequal_hat_overlap(v, d, d) - Omega(v, d)) < mp.mpf("1e-30")
            assert abs(wplus_entry(v, d, d) - wplus_diagonal(k, d)) < mp.mpf("1e-28")
            assert abs(arch_entry(v, d, d) - arch_diagonal(k, d, mp.mpf("0.5"))) < mp.mpf("1e-28")


def test_arbitrary_hat_actual_entry_matches_uniform_assembler():
    with mp.workdps(35):
        length = mp.mpf("1.75")
        degree = 5
        width = length / (2 * (degree + 1))
        radius = length / 4
        centers = [-radius + (i + 1) * width for i in range(degree)]
        q, _ = hp_form(length, degree, dps=32)
        for i, j in ((0, 0), (0, 3), (2, 4)):
            got = actual_form_entry(
                centers[i], width, centers[j], width, length
            )
            assert abs(got - q[i, j]) < mp.mpf("1e-27")


def test_generalized_extreme_diagonal_case():
    with mp.workdps(40):
        b = mp.matrix([[2, 0], [0, 9]])
        s = mp.matrix([[1, 0], [0, 3]])
        assert abs(generalized_extreme(b, s, "min") - 2) < mp.mpf("1e-25")
        assert abs(generalized_extreme(b, s, "max") - 3) < mp.mpf("1e-25")


def test_nested_probe_algebraic_identities():
    row = analyze_nested_collar(7, 1, dps=35, event_prime=5)
    checks = row["checks"]
    for key, value in checks.items():
        assert value is not None, key
        assert abs(mp.mpf(value)) < mp.mpf("1e-25"), (key, value)
    assert not row["nonpositive_old_modes"]
    assert mp.mpf(row["actual_schur_min_over_S"]) > 0


def test_mixed_probe_algebraic_identities():
    row = analyze_mixed_collar(7, 1, "0.12", dps=32, event_prime=5)
    assert row["geometry"] == "literal_disjoint_collar_hats"
    for key, value in row["checks"].items():
        assert value is not None, key
        assert abs(mp.mpf(value)) < mp.mpf("1e-22"), (key, value)


def test_abstract_direct_response_does_not_imply_band_allocation():
    # delta=e^{-m}, G=diag(1,eta), h=I, A=lambda, D=1 and
    # B^2=lambda*eta/2.  The enlarged Q is positive and its direct inverse
    # response has the desired 1/log rate, while the proposed extra
    # (m+1)^-2 allocation diverges.  Fractions make this an exact check.
    for band in (4, 12, 30):
        lam = Fraction(1, 2**band)
        eta = Fraction(1, band + 1)
        b_squared = lam * eta / 2
        assert lam - b_squared > 0  # det [[lam,b],[b,1]]
        direct_response = b_squared / lam
        assert (band + 1) * direct_response == Fraction(1, 2)
        weighted_band_rho = (band + 1) ** 2 * 2**band * b_squared
        assert weighted_band_rho == Fraction(band + 1, 2)


def test_abstract_sliver_capacity_does_not_control_harmonic_tail():
    # G=diag(1,eta), Href=[[3,3],[3,5]] has K=1 and S=2.
    # Href-G is positive, and Gc/S tends to zero, but J*GJ/S tends to 1/2.
    for scale in (4, 12, 30):
        eta = Fraction(1, scale + 1)
        assert 2 * (5 - eta) - 9 > 0  # determinant of Href-G
        raw_collar_ratio = eta / 2
        harmonic_ratio = (1 + eta) / 2
        assert raw_collar_ratio < Fraction(1, scale)
        assert harmonic_ratio > Fraction(1, 2)
