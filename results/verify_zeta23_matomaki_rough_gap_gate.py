#!/usr/bin/env python3
"""Exact exponent ledger for the Matomaki rough-gap second-moment gate.

This script does not certify the imported analytic estimates.  It checks the
rational parameter inequalities used when applying Matomaki's Lemma 5.4 and
the deterministic passage from empty-interval measure to the gap square.
"""

from fractions import Fraction
from math import exp, log


LINEAR_LEVEL = Fraction(1, 3)
BETA_LEVEL = Fraction(1, 1000)
TOTAL_LEVEL = LINEAR_LEVEL + BETA_LEVEL
ROUGH_EXPONENT_MAX = Fraction(4, 25)  # 0.16
INTERVAL_EXPONENT = Fraction(2, 5)  # physical H <= X^(2/5)


def main() -> None:
    # A well-factorable split of the linear weight.  The beta-sieve factor is
    # grouped with the smaller linear factor.
    small = TOTAL_LEVEL / 3
    large = 2 * TOTAL_LEVEL / 3
    linear_complement = LINEAR_LEVEL - large
    assert linear_complement + BETA_LEVEL == small
    assert 0 < small <= large

    # With M<=X^large, N<=X^small, Q<=X^TOTAL_LEVEL, Lemma 5.4
    # has fourth-power bracket exponent 10 TOTAL_LEVEL/3 as long as
    # eta <= 1-5 TOTAL_LEVEL/3.
    eta_star = 1 - 5 * TOTAL_LEVEL / 3
    bracket_exponent = 10 * TOTAL_LEVEL / 3
    correlation_exponent = (
        Fraction(1, 2)
        + INTERVAL_EXPONENT / 2
        + bracket_exponent / 4
    )
    correlation_saving = 1 - correlation_exponent
    assert eta_star == Fraction(797, 1800)
    assert INTERVAL_EXPONENT < eta_star
    assert correlation_saving == Fraction(77, 3600)

    # Check, term by term, which monomials dominate in Lemma 5.4.
    # A=max(HMNQ/X,N)=N.
    hmnq_over_x = (
        INTERVAL_EXPONENT + large + small + TOTAL_LEVEL - 1
    )
    assert hmnq_over_x < small
    a_exp = small
    q_plus_n2 = max(TOTAL_LEVEL, 2 * small)
    first_inner = large + TOTAL_LEVEL + a_exp + q_plus_n2
    second_inner = INTERVAL_EXPONENT + 3 * (large + small) + TOTAL_LEVEL - 1
    assert first_inner == 3 * TOTAL_LEVEL
    assert second_inner < first_inner
    outer_product = a_exp + first_inner
    mq_square = 2 * (large + TOTAL_LEVEL)
    assert outer_product == mq_square == bracket_exponent

    # Lower linear sieve positivity and the Jacobsthal coverage margin.
    s_min = LINEAR_LEVEL / ROUGH_EXPONENT_MAX
    jacobsthal_exponent = 2 * ROUGH_EXPONENT_MAX
    assert s_min == Fraction(25, 12) > 2
    assert jacobsthal_exponent == Fraction(8, 25)
    assert jacobsthal_exponent < INTERVAL_EXPONENT

    # On 2<s<4 the dimension-one lower-sieve function is
    # f(s)=2 e^gamma log(s-1)/s, hence uniformly positive here.
    euler_gamma = 0.5772156649015328606
    f_min = 2 * exp(euler_gamma) * log(float(s_min - 1)) / float(s_min)
    assert f_min > 0.13

    # Algebraic check of the continuous layer-cake identity
    # g^2 = 2 integral_0^g (g-H) dH.
    for gap in (1, 2, 7, 31, 113):
        integral = 2 * Fraction(gap * gap, 2)
        assert integral == gap * gap

    print("Matomaki rough-gap exponent ledger: PASS")
    print(f"linear level d={float(LINEAR_LEVEL):.12f}")
    print(f"beta level e={float(BETA_LEVEL):.12f}")
    print(f"total level L={float(TOTAL_LEVEL):.12f}")
    print(
        "well-factorable exponents "
        f"M={float(large):.12f}, N={float(small):.12f}, Q<={float(TOTAL_LEVEL):.12f}"
    )
    print(f"s_min=d/b_max={float(s_min):.12f}, f(s_min)={f_min:.12f}")
    print(f"raw Lemma 5.4 ceiling eta_*={float(eta_star):.12f}")
    print(
        f"chosen eta={float(INTERVAL_EXPONENT):.12f}, "
        f"correlation saving={float(correlation_saving):.12f}"
    )
    print(
        f"Iwaniec max-gap exponent <=2b={float(jacobsthal_exponent):.12f}, "
        f"coverage margin={float(INTERVAL_EXPONENT-jacobsthal_exponent):.12f}"
    )
    print("consequence: G_2(X;z) << X (log X)^2")


if __name__ == "__main__":
    main()
