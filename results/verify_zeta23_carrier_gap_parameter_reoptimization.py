#!/usr/bin/env python3
"""Replay the coupled carrier/gap exponent reoptimization.

This checker only verifies elementary identities and high-precision numerical
inequalities.  It does not reprove the Bellotti--Wong or Gafni--Tao inputs.
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 80

A_BW = mp.mpf("0.10076")
GP_LAMBDA = mp.mpf("0.304")
GP_INTEGRAL_UPPER = mp.mpf("1.39")


def R(y: mp.mpf) -> mp.mpf:
    return (
        y * mp.log(1 + y ** -2) + 2 * mp.atan(y)
    ) / mp.pi


def E1(alpha: mp.mpf, d: mp.mpf, a: mp.mpf = A_BW) -> mp.mpf:
    y = mp.pi * a / (alpha * (2 * d - 1))
    return alpha * (d - mp.mpf("0.5")) * (1 - R(y))


def kappa(alpha: mp.mpf, d: mp.mpf, a: mp.mpf = A_BW) -> mp.mpf:
    return E1(alpha, d, a) / d


def s_gt(theta: mp.mpf) -> mp.mpf:
    return (45 * theta - 6) / 65


def continuous_frontier(alpha: mp.mpf, d: mp.mpf) -> dict[str, mp.mpf]:
    kap = kappa(alpha, d)
    aperture = 1 / d
    theta = mp.mpf(2) / 15 + mp.mpf(13) * kap / 9
    beta = (
        2 - aperture - theta - kap
    ) / 2
    main_saving = 1 - aperture / 2 - beta
    pole_saving = s_gt(beta)
    return {
        "E1": E1(alpha, d),
        "kappa": kap,
        "aperture": aperture,
        "theta": theta,
        "beta": beta,
        "main_saving": main_saving,
        "pole_saving": pole_saving,
        "pole_margin": pole_saving - kap,
        "peano_limit": 1 - theta,
    }


def gp_bill(d: mp.mpf) -> mp.mpf:
    return GP_LAMBDA / 2 + d * GP_INTEGRAL_UPPER / (2 * mp.pi)


def require_gt(left: mp.mpf, right: mp.mpf, name: str) -> None:
    if not left > right:
        raise AssertionError(f"{name}: {left!s} <= {right!s}")


def require_lt(left: mp.mpf, right: mp.mpf, name: str) -> None:
    if not left < right:
        raise AssertionError(f"{name}: {left!s} >= {right!s}")


def close(left: mp.mpf, right: mp.mpf, tolerance: str = "1e-45") -> None:
    if abs(left - right) > mp.mpf(tolerance):
        raise AssertionError(f"{left!s} != {right!s}")


def main() -> None:
    # The original calibration and its exact aperture conversion.
    old_alpha = mp.mpf(49) / 100
    old_d = mp.mpf(33) / 50
    old = continuous_frontier(old_alpha, old_d)
    close(old["aperture"], mp.mpf(50) / 33)
    close(old["E1"], mp.mpf("0.011900013460076803182602071856126"), "1e-30")
    close(old["kappa"], mp.mpf("0.0180303234243587927009122300851"), "1e-30")

    # If alpha is artificially restricted to [0.49,0.5), the best point is
    # only a limiting point because d<2/3 is strict.  It still misses.
    old_endpoint = continuous_frontier(old_alpha, mp.mpf(2) / 3)
    close(
        old_endpoint["pole_margin"],
        mp.mpf("-0.0010346017624994050160909777538975907573"),
        "1e-39",
    )
    require_lt(old_endpoint["pole_margin"], 0, "old-band limiting margin")

    # Algebraic identity: pole margin is positive exactly when beta>theta,
    # equivalently kappa < 3/10-3/(16d).
    for alpha, d in (
        (mp.mpf("0.49"), mp.mpf("0.66")),
        (mp.mpf("0.48"), mp.mpf("0.666")),
        (mp.mpf("0.47"), mp.mpf("0.665")),
    ):
        row = continuous_frontier(alpha, d)
        kcrit = mp.mpf(3) / 10 - mp.mpf(3) / (16 * d)
        close(
            row["pole_margin"],
            mp.mpf(9) / 13 * (row["beta"] - row["theta"]),
        )
        close(
            row["pole_margin"],
            mp.mpf(24) / 13 * (kcrit - row["kappa"]),
        )

    # The unique limiting alpha where the corridor just closes at d=2/3.
    target_kappa = mp.mpf(3) / 160
    alpha_star = mp.findroot(
        lambda alpha: kappa(alpha, mp.mpf(2) / 3) - target_kappa,
        (mp.mpf("0.48"), mp.mpf("0.485")),
    )
    close(
        alpha_star,
        mp.mpf("0.48255967768667502639190860375113245523"),
        "1e-38",
    )
    close(kappa(alpha_star, mp.mpf(2) / 3), target_kappa)

    # A robust, wholly interior rational calibration for the single slice
    # alpha=0.47.  It is not a uniform certificate on [0.47,0.5).
    alpha = mp.mpf(47) / 100
    d = mp.mpf(133) / 200
    theta = mp.mpf(397) / 2500       # 0.1588
    beta = mp.mpf(799) / 5000        # 0.1598
    row = continuous_frontier(alpha, d)
    kap = row["kappa"]

    require_gt(d, mp.mpf("0.5"), "packet lower d")
    require_lt(d, mp.mpf(2) / 3, "strict packet upper d")
    require_gt(alpha, mp.mpf(3) / 8, "legacy packet depth floor")
    require_lt(alpha, mp.mpf("0.5"), "critical-strip depth")
    close(row["aperture"], mp.mpf(200) / 133)

    raw_carrier = alpha * d
    green_reserve = raw_carrier - gp_bill(d)
    require_gt(green_reserve, row["E1"], "Green reserve covers E1")
    require_gt(raw_carrier, A_BW / 2, "legacy raw carrier")
    require_gt(
        alpha * d * d,
        2 * A_BW,
        "legacy compact-tail sufficient inequality",
    )

    tail_saving = s_gt(theta)
    collar_saving = 2 - row["aperture"] - 2 * beta - theta
    main_saving = 1 - row["aperture"] / 2 - beta
    pole_saving = s_gt(beta)
    peano_endpoint = (2 + tail_saving - 2 * theta - kap) / 2

    require_gt(theta, mp.mpf(2) / 15, "GT local-branch lower end")
    require_lt(theta, mp.mpf(353) / 1445, "GT local-branch upper end")
    require_gt(tail_saving, kap, "long-gap tail")
    require_gt(collar_saving, kap, "short half-cell collar")
    require_gt(main_saving, kap, "main inverse-image mass")
    require_gt(pole_saving, kap, "same-residue pole tail")
    require_gt(beta, theta, "all one-gap denominators covered")
    require_gt(peano_endpoint, mp.mpf("0.8412"), "Peano transition")

    # Multi-gap curvature denominators remain much larger than the cover.
    curvature_denominator_exponent = 1 - row["aperture"] / 2
    require_gt(
        curvature_denominator_exponent,
        beta,
        "multi-gap curvature window remains",
    )

    # Quantifier audit.  Promotion over a band uses the minimum kappa, but a
    # uniform dual kill must beat the supremum, attained as alpha tends to
    # 1/2.  The explicit tail/collar/pole savings all miss that supremum.
    alpha_top = mp.mpf("0.5")
    top = continuous_frontier(alpha_top, d)
    kappa_min = kap
    kappa_max = top["kappa"]
    require_gt(kappa_max, kappa_min, "kill uses top-depth kappa")
    close(
        kappa_max,
        mp.mpf("0.01974048258294210222651618399200661031595"),
        "1e-40",
    )
    require_lt(tail_saving, kappa_max, "tail misses uniform kill")
    require_lt(collar_saving, kappa_max, "collar misses uniform kill")
    require_lt(pole_saving, kappa_max, "pole misses uniform kill")
    require_lt(top["pole_margin"], 0, "top-depth slice remains open")
    close(
        top["pole_margin"],
        mp.mpf("-0.00312991347874562770794659300317241187305"),
        "1e-40",
    )

    top_green_reserve = alpha_top * d - gp_bill(d)
    require_gt(
        top_green_reserve,
        top["E1"],
        "top-depth Green reserve covers E1",
    )

    # Polarity audit.  The lower endpoint is the conservative promotion
    # budget, not the budget for a dual no-go uniform over the whole band.
    deep_kappa = kappa(mp.mpf("0.5"), d)
    kcrit = mp.mpf(3) / 10 - mp.mpf(3) / (16 * d)
    require_gt(deep_kappa, kcrit, "deep candidate survives pole frontier")

    optimized_pole_crossing = mp.findroot(
        lambda candidate_alpha: kappa(candidate_alpha, d) - kcrit,
        (mp.mpf("0.47"), mp.mpf("0.48")),
    )
    close(
        optimized_pole_crossing,
        mp.mpf("0.47721728945766112540731098986322746037"),
        "1e-38",
    )

    fixed_tail_crossing = mp.findroot(
        lambda candidate_alpha: kappa(candidate_alpha, d) - tail_saving,
        (alpha, mp.mpf("0.475")),
    )
    close(
        fixed_tail_crossing,
        mp.mpf("0.471505596359095574339559573763512757"),
        "1e-36",
    )

    print("PASS carrier-gap parameter reoptimization")
    print(f"old restricted limiting deficit={mp.nstr(-old_endpoint['pole_margin'], 16)}")
    print(f"critical alpha at d->2/3={mp.nstr(alpha_star, 18)}")
    print(f"explicit alpha={mp.nstr(alpha, 8)} d={mp.nstr(d, 8)}")
    print(f"aperture={mp.nstr(row['aperture'], 16)}")
    print(f"E1={mp.nstr(row['E1'], 16)} kappa={mp.nstr(kap, 16)}")
    print(f"theta={mp.nstr(theta, 10)} beta={mp.nstr(beta, 10)}")
    print(f"tail margin={mp.nstr(tail_saving-kap, 16)}")
    print(f"collar margin={mp.nstr(collar_saving-kap, 16)}")
    print(f"pole margin={mp.nstr(pole_saving-kap, 16)}")
    print(f"Peano endpoint={mp.nstr(peano_endpoint, 16)}")
    print(f"Green reserve minus E1={mp.nstr(green_reserve-row['E1'], 16)}")
    print(f"uniform-band kappa_max={mp.nstr(kappa_max, 16)}")
    print(f"tail minus kappa_max={mp.nstr(tail_saving-kappa_max, 16)}")
    print(f"collar minus kappa_max={mp.nstr(collar_saving-kappa_max, 16)}")
    print(f"pole minus kappa_max={mp.nstr(pole_saving-kappa_max, 16)}")
    print(
        "top-depth Green reserve minus E1="
        f"{mp.nstr(top_green_reserve-top['E1'], 16)}"
    )
    print(f"deep-band kappa at alpha->1/2={mp.nstr(deep_kappa, 16)}")
    print(f"fixed-cutoff tail crossing alpha={mp.nstr(fixed_tail_crossing, 16)}")
    print(
        "optimized pole crossing at fixed d="
        f"{mp.nstr(optimized_pole_crossing, 16)}"
    )
    print(
        "remaining multi-gap denominator exponent="
        f"{mp.nstr(curvature_denominator_exponent, 16)}"
    )


if __name__ == "__main__":
    main()
