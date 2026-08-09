#!/usr/bin/env python3
"""Fail-fast audit for direct two-shift bounds on the completed R71 field.

The underlying calculation is the cutoff-complete B-spline/Vaughan model in
``ward_nonlocal_covariance_probe``.  This module states, and tests without
sector deletion, four simple estimates one might try before attacking a
genuine two-shift correlation theorem.  Write ``D`` for the grouped-tail
diagonal and ``G`` for every unequal-product and explicit-center term.

1. **Signed screening:** ``G <= 0``.
2. **Leading-one Gram control:** ``abs(G) <= D`` (hence ``E <= 2D``).
3. **Terminal two-shift control:** the same two inequalities for the
   Markov covariance kernel.
4. **Low-frequency control:** for the normalized block Fourier coefficient,
   ``Ghat(t) <= 0`` or ``abs(Ghat(t)) <= Dhat(t)`` on a low band.

For terminal order one the raw expectation is exactly the normalized R71
energy on ``[log(X)-h,log(X)]``.  Its retained zero mode is the Fourier mode
``t=0``.  Thus a strict failure at zero also persists on a nonempty frequency
interval by continuity.

These leading-constant/sign claims are useful finite gates, but they are not
the full analytic target.  Their failure does not exclude a bound with a
polylogarithmic or more general ``exp(o(log X))`` loss, a long-block average,
or a growing-order theorem.  Such an estimate remains the direct P4/R71
problem.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

from ward_nonlocal_covariance_probe import (
    NonlocalCovarianceAudit,
    audit_nonlocal_covariance,
)


@dataclass(frozen=True)
class DirectTwoShiftAudit:
    base: NonlocalCovarianceAudit
    raw_signed_margin: float
    raw_leading_one_margin: float
    covariance_signed_margin: float
    covariance_leading_one_margin: float
    zero_mode_signed_margin: float
    zero_mode_leading_one_margin: float
    low_band_signed_margin: float
    low_band_leading_one_margin: float
    raw_unequal_signed_margin: float
    raw_center_signed_margin: float


def direct_two_shift_audit(
    scale: float = 59.0,
    cutoff: int = 4,
    step: float = 0.04,
    input_order: int = 1,
    macro_order: int = 1,
    gaussian_order: int = 16,
    low_frequencies: tuple[float, ...] = (0.0, 0.25, 0.5, 1.0),
) -> DirectTwoShiftAudit:
    """Test all candidate inequalities on one complete finite model.

    Every margin is nonnegative when the corresponding proposed inequality
    holds.  The default is the smallest configuration found in the stated
    integer/grid scan with a central semiprime and simultaneous strict
    failure of all signed and leading-one bounds; no claim of exhaustive
    minimality over continuous parameters is made.
    """

    base = audit_nonlocal_covariance(
        scale,
        cutoff,
        step,
        input_order,
        macro_order,
        gaussian_order=gaussian_order,
        spectral_frequencies=low_frequencies,
    )
    raw_g = base.raw_nonlocal_remainder
    covariance_g = base.global_covariance_remainder
    zero_g = base.retained_nonlocal_remainder
    low_signed = min(-value for value in base.spectral_remainder)
    low_leading = min(
        diagonal - abs(remainder)
        for diagonal, remainder in zip(
            base.spectral_diagonal, base.spectral_remainder
        )
    )
    return DirectTwoShiftAudit(
        base,
        -raw_g,
        base.tail_diagonal_raw - abs(raw_g),
        -covariance_g,
        base.tail_diagonal_covariance - abs(covariance_g),
        -zero_g,
        base.tail_diagonal_retained - abs(zero_g),
        low_signed,
        low_leading,
        -base.raw_unequal_product,
        -base.raw_center_completion,
    )


def scan_small_admissible_models(
    maximum_scale: int = 80,
    steps: tuple[float, ...] = (
        0.02,
        0.03,
        0.04,
        0.05,
        0.06,
        0.08,
        0.10,
        0.12,
    ),
) -> list[DirectTwoShiftAudit]:
    """Return simultaneous counterexamples in a documented finite grid.

    The cutoff is ``floor(X^(3/8))`` and the fixed-order support condition is
    enforced.  Results are ordered by ``X`` and then ``h``.
    """

    if maximum_scale < 8:
        raise ValueError("maximum_scale must be at least eight")
    answers: list[DirectTwoShiftAudit] = []
    for scale in range(8, maximum_scale + 1):
        cutoff = max(1, math.floor(scale ** (3.0 / 8.0)))
        for step in steps:
            if cutoff * cutoff > scale * math.exp(-step):
                continue
            audit = direct_two_shift_audit(
                float(scale),
                cutoff,
                step,
                gaussian_order=8,
            )
            base = audit.base
            if (
                base.active_tail_products < 2
                or not base.active_central_semiprimes
            ):
                continue
            decisive = (
                audit.raw_signed_margin,
                audit.raw_leading_one_margin,
                audit.covariance_signed_margin,
                audit.covariance_leading_one_margin,
                audit.zero_mode_signed_margin,
                audit.zero_mode_leading_one_margin,
                audit.low_band_signed_margin,
                audit.low_band_leading_one_margin,
            )
            if all(value < 0.0 for value in decisive):
                answers.append(audit)
    return answers


def _ratio(remainder: float, diagonal: float) -> float:
    return remainder / diagonal if diagonal else math.nan


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", type=float, default=59.0)
    parser.add_argument("--cutoff", type=int, default=4)
    parser.add_argument("--step", type=float, default=0.04)
    parser.add_argument("--input-order", type=int, default=1)
    parser.add_argument("--macro-order", type=int, default=1)
    parser.add_argument("--gaussian-order", type=int, default=16)
    parser.add_argument("--scan-to", type=int)
    args = parser.parse_args()
    if args.scan_to is not None:
        results = scan_small_admissible_models(args.scan_to)
        for result in results:
            base = result.base
            print(
                f"X={base.scale:g} Y={base.cutoff} h={base.step:g} "
                f"products={base.active_tail_product_values} "
                f"pq={base.active_central_semiprime_values}"
            )
        print(f"simultaneous counterexamples: {len(results)}")
        return

    audit = direct_two_shift_audit(
        args.scale,
        args.cutoff,
        args.step,
        args.input_order,
        args.macro_order,
        args.gaussian_order,
    )
    base = audit.base
    print(
        f"X={base.scale:g} Y={base.cutoff} h={base.step:g} "
        f"j={base.input_order} m={base.macro_order}"
    )
    print(
        f"products={base.active_tail_product_values} "
        f"central_pq={base.active_central_semiprime_values}"
    )
    print(
        "G/D ratios: "
        f"raw={_ratio(base.raw_nonlocal_remainder, base.tail_diagonal_raw):+.9g} "
        f"cov={_ratio(base.global_covariance_remainder, base.tail_diagonal_covariance):+.9g} "
        f"zero={_ratio(base.retained_nonlocal_remainder, base.tail_diagonal_retained):+.9g}"
    )
    print(
        "raw decomposition: "
        f"D={base.tail_diagonal_raw:.12g} "
        f"unequal={base.raw_unequal_product:+.12g} "
        f"center={base.raw_center_completion:+.12g} "
        f"E={base.raw_energy:.12g}"
    )
    print(
        "low-band Ghat/Dhat: "
        + ", ".join(
            f"{frequency:g}:{_ratio(remainder, diagonal):+.9g}"
            for frequency, diagonal, remainder in zip(
                base.spectral_frequencies,
                base.spectral_diagonal,
                base.spectral_remainder,
            )
        )
    )


if __name__ == "__main__":
    main()
