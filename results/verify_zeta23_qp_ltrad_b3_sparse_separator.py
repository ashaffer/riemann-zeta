#!/usr/bin/env python3
"""Arb checks for the B3 sparse-separator information-gain audit.

The companion report contains the analytic arguments.  This script certifies
the numerical margins in the two-reflected-pair lemma, the exact symmetric
two-pair fixture, the rank-two autocorrelation identities, and the exponent
ledger in the participation/localization arguments.  No sampled grid is used
as a proof of a continuum assertion.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction

from flint import arb, ctx


def certify_two_pair_constants() -> dict[str, arb]:
    """Certify the safe constants in the hard-window two-pair argument."""

    gram = arb("0.02")
    pointwise = arb("2.5").sqrt()
    mean_at_1000 = arb("48.5").sqrt() / 1000

    # Q <= ||F||_infty Avg|F| and
    # Avg|F| <= 2 sup(F) + |Avg F|.
    positive_per_norm = (gram / pointwise - mean_at_1000) / 2
    source_coefficient_norm = arb("8.5").sqrt()
    normalized_positive = positive_per_norm / source_coefficient_norm

    assert positive_per_norm > arb("0.00284")
    assert normalized_positive > arb("0.0009")
    return {
        "gram": gram,
        "pointwise": pointwise,
        "mean_at_1000": mean_at_1000,
        "positive_per_norm": positive_per_norm,
        "source_coefficient_norm": source_coefficient_norm,
        "normalized_positive": normalized_positive,
    }


def certify_symmetric_fixture() -> dict[str, arb]:
    """Certify the exact synthetic two-pair bracket near one half."""

    tau = arb(1) / 500
    a = tau / 4
    w1 = arb.sin(3 * a) / (arb.sin(a) + arb.sin(3 * a))
    w2 = arb.sin(a) / (arb.sin(a) + arb.sin(3 * a))
    c_value = w1 * arb.cos(a) + w2 * arb.cos(3 * a)
    radius = c_value / (2 * arb.cos(2 * a))
    upper = 1 / (2 * arb.cos(2 * a))

    assert w1 > 0
    assert w2 > 0
    assert abs(w1 + w2 - 1) < arb("1e-70")
    assert radius > arb("0.50000006")
    assert radius < arb("0.50000007")
    assert upper > radius
    assert upper < arb("0.50000026")

    # Pair centers are 5*pi/tau and 6*pi/tau; their gap is 500*pi.
    center_gap = arb.pi() / tau
    assert center_gap > 144 * arb.pi()

    # Exact cancellation of the first-pair atoms at s=tau/2,3*tau/2
    # reduces to w1 sin(a)=w2 sin(3a).
    cancellation = w1 * arb.sin(a) - w2 * arb.sin(3 * a)
    assert abs(cancellation) < arb("1e-70")

    omega1 = 5 * arb.pi() / tau
    omega2 = 6 * arb.pi() / tau
    nodes = (
        omega1 - arb(1) / 2,
        omega1 + arb(1) / 2,
        omega2 - arb(1) / 2,
        omega2 + arb(1) / 2,
    )
    source_d = arb.cos(tau / 2)
    source = [arb.cos(node * tau) + source_d for node in nodes]
    s1 = tau / 2
    s2 = 3 * tau / 2
    coordinate_residuals = [
        w1 * arb.cos(node * s1)
        + w2 * arb.cos(node * s2)
        + radius * source_value
        for node, source_value in zip(nodes, source)
    ]
    assert all(abs(value) < arb("1e-70") for value in coordinate_residuals)

    upper_coefficient = -1 / (4 * source_d)
    upper_source_dot = upper_coefficient * (source[2] + source[3])
    assert abs(upper_source_dot + 1) < arb("1e-70")

    return {
        "tau": tau,
        "w1": w1,
        "w2": w2,
        "radius": radius,
        "upper": upper,
        "center_gap": center_gap,
        "cancellation": cancellation,
        "max_coordinate_residual": max(map(abs, coordinate_residuals)),
        "upper_source_dot": upper_source_dot,
    }


def certify_exponent_ledger() -> dict[str, arb]:
    """Check the smoothing and target exponents used in the report."""

    aperture = arb(50) / 33
    y_over_b_exponent = 1 - aperture
    smoothing_order = 2
    mean_absorption_exponent = 1 + smoothing_order * y_over_b_exponent
    target = arb("0.0179")
    hard_core_diameter = (3 * aperture - 2 + 6 * arb("0.019")) / 11
    target_hard_core_diameter = (3 * aperture - 2 + 6 * target) / 11
    local_energy_transition = (2 - aperture) / 2
    hard_core_gap = local_energy_transition - hard_core_diameter
    target_hard_core_gap = local_energy_transition - target_hard_core_diameter
    critical_floor = arb(2) / 99

    assert abs(mean_absorption_exponent + arb(1) / 33) < arb("1e-70")
    assert target > 0
    assert hard_core_diameter > arb("0.2417")
    assert hard_core_diameter < arb("0.2418")
    assert abs(local_energy_transition - arb(8) / 33) < arb("1e-70")
    assert hard_core_gap > arb("0.00065")
    assert hard_core_gap < arb("0.00066")
    assert target_hard_core_gap > arb("0.00125")
    assert target_hard_core_gap < arb("0.00126")
    assert critical_floor > arb("0.0202")
    assert critical_floor < arb("0.0203")
    return {
        "aperture": aperture,
        "y_over_b_exponent": y_over_b_exponent,
        "mean_absorption_exponent": mean_absorption_exponent,
        "target": target,
        "hard_core_diameter": hard_core_diameter,
        "target_hard_core_diameter": target_hard_core_diameter,
        "local_energy_transition": local_energy_transition,
        "hard_core_gap": hard_core_gap,
        "target_hard_core_gap": target_hard_core_gap,
        "critical_floor": critical_floor,
    }


def certify_rank_two_autocorrelation(n: int = 37) -> dict[str, object]:
    """Check the exact rank-two generalized-Fejer sharpness family."""

    if n < 2:
        raise ValueError("n must be at least two")
    q_step = 4 * n
    base = [i + q_step * j for i in range(n) for j in range(n)]
    multiplicities = Counter(a - b for a in base for b in base)
    m = n * n

    assert len(base) == m
    assert multiplicities[0] == m
    assert len(multiplicities) - 1 == (2 * n - 1) ** 2 - 1
    assert all(multiplicities[d] == multiplicities[-d] for d in multiplicities)

    positive_differences = [d for d in multiplicities if d > 0]
    active_nodes = len(positive_differences)
    assert active_nodes == 2 * n * (n - 1)
    assert sum(multiplicities[d] for d in positive_differences) == m * (m - 1) // 2

    square_sum_positive = sum(
        multiplicities[d] ** 2 for d in positive_differences
    )
    t_value = (2 * n**3 + n) // 3
    assert 2 * square_sum_positive == t_value**2 - m**2

    s1 = Fraction(1, 2)
    energy = Fraction(square_sum_positive, m * m * (m - 1) ** 2)
    participation = s1 * s1 / energy
    support_upper = Fraction(1, 2 * (m - 1))
    sharpness_product = participation * support_upper

    assert participation > m
    assert participation < Fraction(9 * m, 8)
    assert Fraction(1, 2) < sharpness_product < Fraction(3, 5)
    return {
        "n": n,
        "m": m,
        "q_step": q_step,
        "active_nodes": active_nodes,
        "s1": s1,
        "energy": energy,
        "participation": participation,
        "support_upper": support_upper,
        "sharpness_product": sharpness_product,
    }


def certify_quarter_adversary() -> dict[str, object]:
    """Certify the quarter maximum and a common-z source normalization."""

    # F(x)=1/6-x/3-x^2/3 for x=cos(2*pi*s/tau).
    critical_x = Fraction(-1, 2)
    critical_value = (
        Fraction(1, 6)
        - critical_x / 3
        - critical_x * critical_x / 3
    )
    left_value = Fraction(1, 6) + Fraction(1, 3) - Fraction(1, 3)
    right_value = Fraction(1, 6) - Fraction(1, 3) - Fraction(1, 3)
    assert critical_value == Fraction(1, 4)
    assert critical_value > left_value
    assert critical_value > right_value

    tau = arb(1) / 1_000_000
    z_value = arb(7) / 10
    source_factor = arb.cos(z_value * tau / 2)
    normalization_scale = 2 / (1 + source_factor)
    p1 = -normalization_scale / 3
    p2 = -normalization_scale / 6
    source_dot = (p1 + p2) * (1 + source_factor)
    perturbed_upper = normalization_scale / 4
    assert 2 * arb.pi() / tau > 144 * arb.pi()
    assert 2 * arb.pi() / tau > 1000
    assert abs(source_dot + 1) < arb("1e-70")
    assert perturbed_upper > arb(1) / 4
    assert perturbed_upper < arb("0.2500000000001")
    return {
        "critical_x": critical_x,
        "maximum": critical_value,
        "source_dot": source_dot,
        "perturbed_upper": perturbed_upper,
    }


def main() -> None:
    ctx.dps = 80
    two_pair = certify_two_pair_constants()
    fixture = certify_symmetric_fixture()
    ledger = certify_exponent_ledger()
    rank_two = certify_rank_two_autocorrelation()
    quarter = certify_quarter_adversary()

    print("two-pair positive return per coefficient norm:",
          two_pair["positive_per_norm"])
    print("source-normalized two-pair return:",
          two_pair["normalized_positive"])
    print("symmetric fixture lower radius:", fixture["radius"])
    print("symmetric fixture upper radius:", fixture["upper"])
    print("mean-absorption exponent:", ledger["mean_absorption_exponent"])
    print("short-carrier diameter threshold:", ledger["hard_core_diameter"])
    print("localized-energy/hard-core exponent gap:", ledger["hard_core_gap"])
    print("rank-two active nodes:", rank_two["active_nodes"])
    print("rank-two effective participation:",
          float(rank_two["participation"]))
    print("rank-two h upper times participation:",
          float(rank_two["sharpness_product"]))
    print("disjoint-event two-pair upper adversary:",
          float(quarter["maximum"]))
    print("all sparse-separator certificates passed")


if __name__ == "__main__":
    main()
