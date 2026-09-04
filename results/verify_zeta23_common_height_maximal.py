#!/usr/bin/env python3
"""Exact exponent audit for the common-height maximal-incidence fail-fast gate."""

from fractions import Fraction as F


KAPPA = F(90_151_617, 5_000_000_000)
BETA = F(1537, 10_000)
THETA = F(797, 5000)
B = F(39, 250)
A = 1 - B
H = 1 - A / 2
TRANSITION = F(4203, 5000)
APERTURE = F(50, 33)


def dec(x: F) -> str:
    return f"{float(x):.10f}"


def main() -> None:
    assert BETA < B < THETA < H
    assert A == F(211, 250)
    assert H == F(289, 500)
    assert TRANSITION < A < 1 < APERTURE
    assert 1 - A == B  # one full logarithmic turn has physical gap Y^b

    # Blockwise large-sieve allowance relative to K=Y^(a/2) blocks.
    ls_excess = THETA + 2 * KAPPA
    assert ls_excess == F(977_303_234, 5_000_000_000)
    assert ls_excess > 0

    # The high-q formula agrees at 2r=h and then increases.
    transition_r = H / 2
    high_q_relative = 2 * transition_r + THETA - 1 + A / 2 + 2 * KAPPA
    assert high_q_relative == ls_excess

    # Common-height rational-cell radii.
    bottom_cell_width = A / 2 - BETA
    smallest_cell_width = A / 2 - H
    assert bottom_cell_width == F(2683, 10_000)
    assert smallest_cell_width == -B
    # alpha=Y^-b is farther from 0 than the q=1 cell width Y^-h,
    # and below every positive rational with q<=Y^beta.
    assert B < H
    assert BETA < B

    # Model counts and gap ledgers.
    long_gap_count = 1 - B - KAPPA
    gaps_per_block = long_gap_count - A / 2
    gap_square = 1 + B - KAPPA
    gap_third = 1 + 2 * B - KAPPA
    cached_third = F(84_549, 65_000)
    assert long_gap_count > 0
    assert gaps_per_block > 0
    assert gap_square < F(123, 100)
    assert gap_third < cached_third
    assert gaps_per_block == H - B - KAPPA

    # Nearest-odd-integer rounding shifts phase by t/Y=Y^-b.
    phase_rounding = A - 1
    assert phase_rounding == -B

    # Long-gap error terms: smooth amplitude gives Delta^2, while integer
    # rounding gives the larger Y^-1 error per selected gap.  Both are o of
    # the coherent Y^-kappa main term.
    smooth_long_error = B - 1 - KAPPA
    rounding_long_error = -B - KAPPA
    assert smooth_long_error < -KAPPA
    assert rounding_long_error < -KAPPA

    # Per-block target and comparator errors.
    local_target = H - 1 - KAPPA
    local_small_peano = H - 1 - 2 * B
    local_half_cell = H - 2
    local_continuum = -A
    assert local_small_peano < local_target
    assert local_half_cell < local_target
    assert local_continuum < local_target

    # Rational replacement costs (H/Y)/q and is below the local target for
    # every retained q>Y^beta.
    local_rational_error = H - 1 - BETA
    assert local_rational_error < local_target

    c_gt = F(9, 13) * (B - F(2, 15))
    assert c_gt == F(51, 3250)
    assert c_gt < KAPPA
    # The Gafni--Tao saving is increasing in gamma, so this endpoint check
    # controls every 2/15 <= gamma <= b.
    assert F(9, 13) > 0

    # Coefficient square sum and integer-product fourth moment.
    s2_exponent = B - 1 - KAPPA
    assert s2_exponent < THETA - 1
    fourth_moment = 2 * B - 2 * KAPPA
    bad_length = fourth_moment + 4 * KAPPA
    assert bad_length == 2 * B + 2 * KAPPA

    # Diffuse-vector exceptional ledgers still permit at least one peak.
    diffuse_bad_length = 4 * KAPPA
    diffuse_components = F(9, 2) * KAPPA
    assert diffuse_bad_length > 0
    assert diffuse_components > 0

    print("common-height maximal-incidence ledger: PASS")
    print(f"large-sieve excess over one bad/block = {dec(ls_excess)}")
    print(f"bottom rational-cell height radius exponent = {dec(bottom_cell_width)}")
    print(f"smallest rational-cell height radius exponent = {dec(smallest_cell_width)}")
    print(f"long-gap count exponent = {dec(long_gap_count)}")
    print(f"long gaps per curvature block exponent = {dec(gaps_per_block)}")
    print(f"gap-square exponent = {dec(gap_square)}")
    print(f"gap-third exponent = {dec(gap_third)}")
    print(f"endpoint phase-rounding exponent = {dec(phase_rounding)}")
    print(f"long-gap smooth-error exponent = {dec(smooth_long_error)}")
    print(f"long-gap rounding-error exponent = {dec(rounding_long_error)}")
    print(f"local target exponent = {dec(local_target)}")
    print(f"local small-mesh Peano exponent = {dec(local_small_peano)}")
    print(f"local rational-replacement exponent = {dec(local_rational_error)}")
    print(f"Gafni--Tao saving at b = {dec(c_gt)}")
    print(f"coefficient S2 exponent = {dec(s2_exponent)}")
    print(f"integer-product fourth-moment exponent = {dec(fourth_moment)}")
    print(f"model bad-length allowance exponent = {dec(bad_length)}")
    print(f"diffuse bad-length exponent = {dec(diffuse_bad_length)}")
    print(f"diffuse component-count exponent = {dec(diffuse_components)}")


if __name__ == "__main__":
    main()
