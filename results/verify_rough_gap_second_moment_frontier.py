#!/usr/bin/env python3
"""Exact parameter audit for the polynomial rough-gap second moment.

This is an exponent checker, not a formalization of the imported sieve and
Kloosterman estimates.  It replays every monomial in Matomaki's Lemma 5.4,
checks the fixed-level corollary, and derives the 3/16 frontier of the
balanced two-factor parameter scheme.
"""

from fractions import Fraction as F


def lemma_54_ledger(d: F, e: F, eta: F, nu: F = F(0)) -> dict[str, F]:
    """Return exponents in the exact fourth-power bracket of Lemma 5.4.

    The linear level D=X^d is split at R=X^(2(d+e)/3).  The beta factor
    E=X^e is grouped with D/R.  ``nu`` is a conservative enlargement of
    both factor supports; the proof takes nu arbitrarily small relative to
    the fixed endpoint margin.
    """

    level = d + e
    m = 2 * level / 3 + nu
    n = level / 3 + nu
    q = level

    hmnq_over_x = eta + m + n + q - 1
    a = max(hmnq_over_x, n)  # HMNQ/X + N
    q_plus_n_squared = max(q, 2 * n)
    inner_first = m + q + a + q_plus_n_squared
    inner_second = eta + 3 * (m + n) + q - 1
    outer_product = a + max(inner_first, inner_second)
    mq_squared = 2 * (m + q)
    bracket = max(mq_squared, outer_product)
    correlation = F(1, 2) + eta / 2 + bracket / 4

    return {
        "d": d,
        "e": e,
        "L": level,
        "eta": eta,
        "m": m,
        "n": n,
        "q": q,
        "HMNQ/X": hmnq_over_x,
        "A": a,
        "Q+N^2": q_plus_n_squared,
        "inner_first": inner_first,
        "inner_second": inner_second,
        "outer_product": outer_product,
        "MQ_squared": mq_squared,
        "bracket": bracket,
        "correlation": correlation,
        "saving": 1 - correlation,
    }


def check_balanced_closed_form(d: F, e: F, eta: F) -> None:
    """Check the closed form in its stated dominance chamber."""

    row = lemma_54_ledger(d, e, eta)
    level = d + e
    assert eta + 5 * level / 3 <= 1
    assert d + level <= 1
    assert row["A"] == level / 3
    assert row["Q+N^2"] == level
    assert row["inner_first"] == 3 * level
    assert row["inner_second"] <= row["inner_first"]
    assert row["outer_product"] == 10 * level / 3
    assert row["MQ_squared"] == 10 * level / 3
    assert row["bracket"] == 10 * level / 3
    assert row["correlation"] == F(1, 2) + eta / 2 + 5 * level / 6


def check_fixed_level_corollary() -> None:
    d = F(1, 3)
    e = F(1, 1000)
    eta = d
    check_balanced_closed_form(d, e, eta)
    row = lemma_54_ledger(d, e, eta)

    assert row["saving"] == F(197, 3600)

    # The original project band ends at b=.16.  It is strictly inside the
    # fixed-D b<1/6 range and its Jacobsthal exponent is covered by eta=1/3.
    b_band = F(4, 25)
    assert d / b_band == F(25, 12) > 2
    assert 2 * b_band < eta

    # Representative point in the uniform clean corollary
    # X^eps <= z <= X^(1/6-eps).
    margin = F(1, 100)
    b_clean = F(1, 6) - margin
    assert d > 2 * b_clean
    assert eta > 2 * b_clean


def check_moving_level_family() -> None:
    # Exact identities are checked at several rational endpoint margins.
    for eps in (F(1, 10000), F(1, 1000), F(1, 100), F(1, 20)):
        d = F(3, 8) - eps
        e = min(F(1, 1000), eps / 10)
        eta = d
        b = F(3, 16) - eps

        assert d - 2 * b == eps
        assert eta - 2 * b == eps
        assert d / b > 2
        assert eta > 2 * b
        assert e <= eps / 10

        check_balanced_closed_form(d, e, eta)
        row = lemma_54_ledger(d, e, eta)
        expected_saving = 4 * eps / 3 - 5 * e / 6
        assert row["saving"] == expected_saving
        assert expected_saving >= 5 * eps / 4

        # Explicitly leave room for factor-support slack.  This is much
        # smaller than needed and is only a robustness test.
        slack_row = lemma_54_ledger(d, e, eta, eps / 1000)
        assert slack_row["saving"] > 0


def check_optimizer() -> None:
    # With e tending to zero, the three strict constraints are
    #   2b<d, 2b<eta, eta+5d/3<1.
    # Hence 2b < min(d, 1-5d/3).  The two affine branches meet exactly at
    # d=3/8, giving b=3/16.  Check both the intersection and globality.
    d_star = F(3, 8)
    b_star = F(3, 16)
    assert d_star == 1 - 5 * d_star / 3
    assert b_star == d_star / 2

    for denominator in (97, 1000, 4096):
        for numerator in range(1, denominator):
            d = F(numerator, denominator)
            feasible_b = min(d, 1 - 5 * d / 3) / 2
            assert feasible_b <= b_star

    # Conversely, every b<3/16 is feasible after choosing d, eta close
    # enough to 3/8 and then taking e>0 sufficiently small.
    for gap in (F(1, 10000), F(1, 1000), F(1, 100)):
        eps = gap
        d = d_star - eps
        e = eps / 10
        eta = d
        b = b_star - eps
        assert 2 * b < min(d, eta)
        assert eta + 5 * (d + e) / 3 < 1


def check_layer_cake() -> None:
    # 2 int_0^g (g-H)dH = g^2.
    for gap in (1, 2, 7, 31, 113):
        integral = 2 * (F(gap * gap) - F(gap * gap, 2))
        assert integral == gap * gap


def main() -> None:
    check_fixed_level_corollary()
    check_moving_level_family()
    check_optimizer()
    check_layer_cake()

    fixed = lemma_54_ledger(F(1, 3), F(1, 1000), F(1, 3))
    print("rough-gap second-moment frontier audit: PASS")
    print(f"fixed-D saving={fixed['saving']} ({float(fixed['saving']):.12f})")
    print("fixed-D corollary: b < 1/6")
    print("optimized balanced frontier: b < 3/16")
    print("analytic sieve/Kloosterman inputs: cited, not certified by this script")


if __name__ == "__main__":
    main()
