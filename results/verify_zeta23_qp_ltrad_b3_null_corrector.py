#!/usr/bin/env python3
"""Exact/Arb checks for the LTRAD B3 null-corrector audit.

The script certifies two facts used in the companion report.

1. Genuine ordinary-prime shells contain two disjoint reflected pairs at
   Fourier distance less than ``B^-1``, with ``B=Y^(50/33)``.
2. A single such pair can be exactly source-null at a legal low height while
   retaining a fixed amount of high-band L1 mass per scaled Newton jet.

The analytic inequalities are proved in the report.  Arb is used here only
to certify their hypotheses and the displayed numerical constants; no
sampled quadrature is promoted to a theorem certificate.
"""

from __future__ import annotations

from math import isqrt

from flint import arb, arb_mat, ctx


APERTURE_NUMERATOR = 50
APERTURE_DENOMINATOR = 33
SHELL_WIDTH = arb(1) / 5


def is_prime_by_trial_division(value: int) -> bool:
    """Deterministically prove primality for the modest certificate inputs."""

    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def polynomial_pair(m: int, k: int) -> tuple[int, int, int]:
    """Return the exact odd-k reflected-pair fixture and its parameter r."""

    if m < 2 or k <= 0 or k % 2 == 0:
        raise ValueError("require m >= 2 and positive odd k")
    r = (k * k + 1) // 2
    center = m * m
    return center - k * m + r, center + k * m + r, r


def pair_geometry(m: int, lower: int, upper: int) -> dict[str, arb]:
    """Return Arb enclosures for one reflected prime pair."""

    Y = arb(2 * m * m + 1) / 2
    B = (Y.log() * arb(APERTURE_NUMERATOR) / APERTURE_DENOMINATOR).exp()
    u_lower = (Y / lower).log()
    u_upper = (arb(upper) / Y).log()
    gap = abs(u_lower - u_upper)
    scaled_gap = B * gap
    mean_frequency = (u_lower + u_upper) / 2
    return {
        "Y": Y,
        "B": B,
        "u_lower": u_lower,
        "u_upper": u_upper,
        "scaled_gap": scaled_gap,
        "mean_frequency": mean_frequency,
    }


def certify_fixture(m: int) -> list[dict[str, arb]]:
    """Certify the k=1,3 two-pair polynomial fixture at one center."""

    geometries: list[dict[str, arb]] = []
    twice_Y = 2 * m * m + 1
    four_Y_squared = twice_Y * twice_Y
    for k in (1, 3):
        lower, upper, r = polynomial_pair(m, k)
        assert is_prime_by_trial_division(lower)
        assert is_prime_by_trial_division(upper)
        # This is the exact integer form of
        # p_k q_k - Y^2 = r_k^2 - 1/4.
        assert 4 * lower * upper - four_Y_squared == 4 * r * r - 1

        geometry = pair_geometry(m, lower, upper)
        Y = geometry["Y"]
        width = SHELL_WIDTH
        assert lower > Y * (-width).exp()
        assert lower < Y
        assert upper > Y
        assert upper < Y * width.exp()
        assert geometry["scaled_gap"] > 0
        assert geometry["scaled_gap"] < 1
        assert geometry["mean_frequency"] * geometry["B"] > 64
        geometry["lower"] = arb(lower)
        geometry["upper"] = arb(upper)
        geometry["product_offset"] = arb(4 * r * r - 1) / 4
        geometries.append(geometry)

    center_separation = abs(
        geometries[1]["mean_frequency"]
        - geometries[0]["mean_frequency"]
    )
    assert geometries[0]["B"] * center_separation > 64
    return geometries


def certify_single_pair_source_null() -> dict[str, arb]:
    """Certify the explicit N=3000 source-null one-pair calculation."""

    N = 3000
    Y = arb(2 * N + 1) / 2
    B = (Y.log() * arb(APERTURE_NUMERATOR) / APERTURE_DENOMINATOR).exp()
    lower = 2729
    upper = 3299
    assert is_prime_by_trial_division(lower)
    assert is_prime_by_trial_division(upper)

    u_lower = (Y / lower).log()
    u_upper = (arb(upper) / Y).log()
    mean_frequency = (u_lower + u_upper) / 2
    scaled_gap = B * abs(u_lower - u_upper)
    assert scaled_gap > 0
    assert scaled_gap < 1

    winding = 45
    t0 = 2 * arb.pi() * winding / (u_lower + u_upper)
    assert t0 > arb(N).sqrt()
    assert t0 < N
    # The exact identity is
    # (u_lower+u_upper)t0=2*pi*winding, hence the cosine
    # difference vanishes by cos(a)-cos(b)=-2sin((a+b)/2)sin((a-b)/2).
    source_difference = arb.cos(u_lower * t0) - arb.cos(u_upper * t0)
    assert abs(source_difference) < arb("1e-70")

    # For coefficients (+A,-A), restrict the high band to [B/2,B].
    # The report proves Avg_H |F| / |A| is at least this expression.
    l1_per_raw_amplitude = 2 * arb.sin(scaled_gap / 4) * (
        1 / arb.pi() - 2 / (mean_frequency * B)
    )
    scaled_jet_per_raw_amplitude = 2 * scaled_gap
    l1_per_scaled_jet = l1_per_raw_amplitude / scaled_jet_per_raw_amplitude
    assert l1_per_raw_amplitude > arb("0.0955")
    assert l1_per_scaled_jet > arb("0.079")

    band_length = B - (Y.log() / 100).exp()
    mean_absolute_upper = 2 * (1 / u_lower + 1 / u_upper) / band_length
    positive_sup_per_raw_amplitude = (
        l1_per_raw_amplitude - mean_absolute_upper
    ) / 2
    assert positive_sup_per_raw_amplitude > arb("0.0476")

    return {
        "Y": Y,
        "B": B,
        "lower": arb(lower),
        "upper": arb(upper),
        "scaled_gap": scaled_gap,
        "t0": t0,
        "source_difference": source_difference,
        "l1_per_raw_amplitude": l1_per_raw_amplitude,
        "l1_per_scaled_jet": l1_per_scaled_jet,
        "positive_sup_per_raw_amplitude": positive_sup_per_raw_amplitude,
    }


def certify_universal_pair_constants() -> dict[str, arb]:
    """Certify the safe constants in the analytic one-/two-pair lemmas."""

    one_pair_terminal = arb.sin(arb(1) / 2) * (
        2 / arb.pi() - arb(1) / 4
    )
    one_pair_full = one_pair_terminal / 2
    two_pair_terminal = 11 / (48 * arb(2).sqrt()) - (
        3 * arb(2).sqrt() / 4
    ) * (1 - 2 * arb.sin(arb(1) / 2))
    two_pair_full = two_pair_terminal / 2
    assert one_pair_terminal > arb("0.1853")
    assert one_pair_full > arb("0.0926")
    assert two_pair_terminal > arb("0.1184")
    assert two_pair_full > arb("0.0592")
    return {
        "one_pair_terminal": one_pair_terminal,
        "one_pair_full": one_pair_full,
        "two_pair_terminal": two_pair_terminal,
        "two_pair_full": two_pair_full,
    }


def certify_three_pair_no_separator() -> dict[str, object]:
    """Certify one six-node dual measure excluding a local separator.

    If the returned positive weights are denoted by ``w_k``, the solved
    identities are

        sum_k w_k cos(omega_i s_k) = -r v_i,   sum_k w_k = 1.

    Therefore every ``y`` with ``y dot v = -1`` has

        sum_k w_k F_y(s_k) = r,

    and hence ``sup_s F_y(s) >= r``.  This is a certificate for this one
    synthetic fixture, not a general B3 theorem.
    """

    tau = arb(1) / 500
    phases = [arb.pi() - arb(2) / 5, arb.pi() + arb(2) / 5, arb(7) / 10]
    nodes: list[arb] = []
    for index, phase in enumerate(phases):
        center = (phase + 2 * arb.pi() * (2 * index + 1)) / tau
        nodes.extend((center - arb(1) / 2, center + arb(1) / 2))

    assert nodes[2] - nodes[1] > 144 * arb.pi()
    assert nodes[4] - nodes[3] > 144 * arb.pi()

    D = -sum((arb.cos(node * tau) for node in nodes[:4]), arb(0)) / 4
    source = [arb.cos(node * tau) + D for node in nodes]
    grid_indices = (21, 237, 791, 899, 1007, 1068)
    points = [
        arb(1) / 100_000
        + arb(index) * (1 - arb(1) / 100_000) / 11_999
        for index in grid_indices
    ]
    assert all(point > 0 and point < 1 for point in points)
    assert D > 0 and D < 1

    rows = [
        [arb.cos(node * point) for point in points] + [source_value]
        for node, source_value in zip(nodes, source)
    ]
    rows.append([arb(1)] * len(points) + [arb(0)])
    matrix = arb_mat(rows)
    right_hand_side = arb_mat(7, 1, [arb(0)] * 6 + [arb(1)])
    solution = matrix.solve(right_hand_side)
    weights = [solution[index, 0] for index in range(6)]
    radius = solution[6, 0]
    determinant = matrix.det()

    assert determinant > arb("0.0000736")
    assert all(weight > 0 for weight in weights)
    assert radius > arb("0.5928")
    residual = matrix * solution - right_hand_side
    assert all(abs(residual[index, 0]) < arb("1e-65") for index in range(7))
    return {
        "tau": tau,
        "D": D,
        "determinant": determinant,
        "weights": weights,
        "radius": radius,
    }


def main() -> None:
    ctx.dps = 80
    constants = certify_universal_pair_constants()
    source_null = certify_single_pair_source_null()
    no_separator = certify_three_pair_no_separator()
    fixtures = {
        3339: certify_fixture(3339),
        1_002_924: certify_fixture(1_002_924),
    }

    print("universal lower-bound constants")
    for name, value in constants.items():
        print(f"  {name}={value}")
    print("single actual-pair source-null witness")
    for name, value in source_null.items():
        print(f"  {name}={value}")
    print("exact two-pair ordinary-prime fixtures")
    for m, pairs in fixtures.items():
        print(f"  m={m}, Y={pairs[0]['Y']}")
        for pair in pairs:
            print(
                "    "
                f"({pair['lower']}, {pair['upper']}), "
                f"product_offset={pair['product_offset']}, "
                f"B_gap={pair['scaled_gap']}"
            )
    print("three-pair separator-qualified control")
    for name, value in no_separator.items():
        print(f"  {name}={value}")
    print("all exact and Arb checks: PASS")


if __name__ == "__main__":
    main()
