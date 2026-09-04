#!/usr/bin/env python3
"""Rigorous Arb certificate at the first post-Chuk support event.

The physical half-window is

    a_5 = log(5) / 2.

At this exact endpoint, the ``p=5`` translation is equal to the support
diameter.  Its autocorrelation is therefore zero, so the completed-zeta Weil
form has the same active source terms ``2,3,4`` as Chuk's ``a=0.8`` window.

This driver reuses the independently audited common-node machinery in
``chuk_l08_arb_certificate`` with a stronger clipping configuration:

    cutoff T = 250, exterior floor alpha = 73/100,
    Legendre degrees 0,...,299, 80 Gauss nodes per unit panel.

It proves a ``6e-18`` finite-head floor and transfers a ``5e-18`` floor to
the infinite Legendre complement.  Thus, for every complex function in the
logarithmic form domain supported in ``[-a_5,a_5]``,

    Q(f) >= 5e-18 ||f||_2^2,

with strict inequality for nonzero ``f``.

Combined with Suzuki's unconditional continuity theorem for the localized
ground value, this certifies positivity on an existential nonempty interval
past the p=5 activation.  Continuity supplies no effective interval width,
so this is not a cofinal or all-support propagation theorem.
"""

from __future__ import annotations

import argparse
from time import time

from flint import acb, arb, ctx, fmpq

import chuk_l08_arb_certificate as base


def Q(n: int, d: int = 1) -> fmpq:
    return fmpq(n, d)


def A(x) -> arb:
    return arb(x)


CUTOFF = 250
ALPHA = Q(73, 100)
DEFAULT_DEGREE = 300
DEFAULT_ORDER = 80
DEFAULT_PRECISION = 640
CROSS_CHECK_PRECISION = 384
HEAD_SHIFT = Q(6, 10**18)
FULL_SHIFT = Q(5, 10**18)
GLIDE_LOG_DENOMINATOR = 10**22


def configure_base() -> arb:
    """Install the exact endpoint parameters in the shared audited engine."""
    log5 = A(5).log()
    base.CUTOFF = CUTOFF
    base.ALPHA = ALPHA
    base.A_HALF_WIDTH = log5 / 2
    return log5


def endpoint_and_envelope_checks(log5: arb) -> dict[str, arb]:
    """Check the exact event mask and every multiplier constant used below."""
    support = 2 * A(base.A_HALF_WIDTH)
    if not (support - log5).contains(0):
        raise ArithmeticError("2*a_5 does not enclose log(5)")
    base.require_lt(A(2).log(), support, "log(2) < log(5)")
    base.require_lt(A(3).log(), support, "log(3) < log(5)")
    base.require_lt(A(4).log(), support, "log(4) < log(5)")
    base.require_gt(A(7).log(), support, "log(7) > log(5)")

    beta_star = (
        (A(CUTOFF) / (2 * base.PI)).log()
        - Q(1, CUTOFF)
        - base.PRIME_MASS
    )
    base.require_gt(beta_star, ALPHA, "beta_*(250) > 73/100")

    # The same recurrence-plus-Binet estimates as the a=0.8 driver, now at
    # T=250.  The first bound is also the multiplier constant used by the
    # infinite head/tail transfer.
    radius = (A(Q(5, 4)) ** 2 + A(Q(CUTOFF, 2)) ** 2).sqrt()
    psi_real_band_bound = (
        radius.log() + base.PI / 2 + Q(2, 5) + Q(4, 75) + 4
    )
    real_multiplier_bound = (
        psi_real_band_bound + base.PI.log() + base.PRIME_MASS + A(ALPHA)
    )
    base.require_lt(
        real_multiplier_bound,
        Q(16),
        "|Omega-alpha| on [0,250]",
    )

    real_extent = A(CUTOFF) + (A(5).sqrt() - 2) / 4
    complex_radius = (
        A(Q(11, 8)) ** 2 + (real_extent / 2) ** 2
    ).sqrt()
    psi_ellipse_bound = (
        complex_radius.log()
        + base.PI / 2
        + Q(4, 9)
        + Q(16, 243)
        + 8
    )
    comb_ellipse_bound = (
        base.PRIME_MASS * (A(4).log() / 4).cosh()
    )
    ellipse_multiplier_bound = (
        psi_ellipse_bound
        + base.PI.log()
        + comb_ellipse_bound
        + A(ALPHA)
    )
    base.require_lt(
        ellipse_multiplier_bound,
        Q(21),
        "|Omega-alpha| on the Bernstein ellipses",
    )
    return {
        "half_width": A(base.A_HALF_WIDTH),
        "support_diameter": support,
        "beta_star": beta_star,
        "real_multiplier_bound": real_multiplier_bound,
        "ellipse_multiplier_bound": ellipse_multiplier_bound,
    }


def explicit_glide_instantiation(log5: arb) -> dict[str, arb]:
    """Instantiate THEOREMS.md's effective support-continuity estimate.

    The project support variable is ``L=4a``.  We take
    ``ell_0=L_5=2 log(5)``, ``ell_1=4`` and
    ``0 < h <= exp(-10^22)``.  The cited theorem then loses at most
    ``C_glide / 10^22`` from the endpoint ground value.
    """
    ell0 = 2 * log5
    ell1 = A(4)
    kappa0 = acb(Q(1, 4)).digamma().real - base.PI.log()
    c_pole = 4 * (ell1 / 4).sinh()
    c_prime = 2 * ell1 * (ell1 / 4).exp()
    c_lambda = (
        4 * (ell0 / 4).sinh()
        + kappa0
        + 8
        + (2 / base.PI) * (1 + 64 / (ell0 * ell0)).log()
        + 2
        + 2 * ell0 * (ell0 / 4).exp()
    )
    c_b = c_lambda + 1 + c_pole + c_prime + Q(269, 50)
    c_c = 2 + 4 * c_b
    c_pole_prime = (ell1 / 4).exp() * (ell1 + ell1 * ell1 / 4)
    c_glide = (
        (16 + c_pole_prime) / ell0
        + c_prime * c_c
        + (1 + (ell1 / 2).exp()) * ell1 * c_c
    )
    loss = c_glide / GLIDE_LOG_DENOMINATOR
    residual_floor = A(FULL_SHIFT) - loss
    base.require_lt(c_glide, Q(12662), "C_glide")
    base.require_gt(
        residual_floor,
        Q(3733, 10**21),
        "post-p=5 propagated floor",
    )
    return {
        "ell0": ell0,
        "c_lambda": c_lambda,
        "c_b": c_b,
        "c_c": c_c,
        "c_glide": c_glide,
        "glide_loss": loss,
        "post_event_floor": residual_floor,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--degree", type=int, default=DEFAULT_DEGREE)
    parser.add_argument("--order", type=int, default=DEFAULT_ORDER)
    parser.add_argument("--precision", type=int, default=DEFAULT_PRECISION)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument(
        "--cross-check",
        action="store_true",
        help="independently replay representative entries with acb.integral",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.precision < DEFAULT_PRECISION:
        raise ValueError("the endpoint head proof requires at least 640 bits")
    if args.order < 32:
        raise ValueError("quadrature order is implausibly small")
    ctx.prec = args.precision
    ctx.threads = args.threads
    log5 = configure_base()
    if not A(args.degree) > A(base.A_HALF_WIDTH) * CUTOFF:
        raise ValueError("degree must exceed a_5*T for the tail bound")

    checks = endpoint_and_envelope_checks(log5)
    for key, value in checks.items():
        print(key, value.str(30, radius=True), flush=True)
    print("prime mass", base.PRIME_MASS.str(30, radius=True), flush=True)
    entry_error = base.quadrature_entry_error(args.order)
    print("quadrature entry error", entry_error.str(18, radius=True), flush=True)

    started = time()
    blocks, _ = base.assemble_parity_blocks(
        args.degree,
        args.order,
        verbose=not args.quiet,
    )
    print(f"assembly seconds {time() - started:.2f}", flush=True)
    print(
        "parity block dimensions",
        blocks[0].nrows(),
        blocks[1].nrows(),
        flush=True,
    )
    print(
        "quadrature operator error bounds",
        (blocks[0].nrows() * entry_error).str(18, radius=True),
        (blocks[1].nrows() * entry_error).str(18, radius=True),
        flush=True,
    )
    for parity, block in enumerate(blocks):
        radius, row, column = base.maximum_entry_radius(block)
        print(
            ("even" if parity == 0 else "odd"),
            "maximum final entry radius",
            radius.str(18, radius=True),
            "at",
            row,
            column,
            flush=True,
        )
    if args.cross_check:
        # The adaptive route targets 2^-150 accuracy and is independent of
        # the 640-bit preconditioned head solve.  Running it at 384 bits keeps
        # this diagnostic replay practical while its balls are still far
        # narrower than the common-node enclosures they must overlap.
        working_precision = ctx.prec
        ctx.prec = CROSS_CHECK_PRECISION
        try:
            print(
                "adaptive cross-check precision",
                CROSS_CHECK_PRECISION,
                flush=True,
            )
            base.adaptive_cross_check(blocks, args.degree)
        finally:
            ctx.prec = working_precision

    base.certify_head(blocks, HEAD_SHIFT)
    transfer = base.full_space_transfer(
        args.degree,
        HEAD_SHIFT,
        FULL_SHIFT,
    )
    for key, value in transfer.items():
        print(key, A(value).str(25, radius=True), flush=True)
    glide = explicit_glide_instantiation(log5)
    for key, value in glide.items():
        print(key, A(value).str(25, radius=True), flush=True)
    print(
        "ARBITRARY-PRECISION BALL CERTIFIED: at a=log(5)/2, "
        "Q(f) >= 5e-18 ||f||_2^2 on the logarithmic form domain, "
        "with strict inequality for every nonzero f",
        flush=True,
    )
    print(
        "EFFECTIVE FIRST-EVENT PROPAGATION CERTIFIED: for every "
        "0 < h <= exp(-10^22) in project-L units, "
        "lambda(2 log(5)+h) > 3.733e-18",
        flush=True,
    )


if __name__ == "__main__":
    main()
