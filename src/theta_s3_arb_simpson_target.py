"""High-precision rescaled target scout for the actual theta ``S_3``.

The broad DST scout uses double precision and extrapolates the Laguerre
endpoint.  Near a deep cancellation this can create false signs.  This tool
instead

* evaluates every normalized completed-xi sample with Arb,
* computes the normalized Laguerre endpoint from an exact Arb power series,
* accumulates composite Simpson quadrature in Arb arithmetic.

The resulting ball encloses the *discrete Simpson sum*, not the continuum
quadrature error.  Runs at successively halved mesh widths are therefore a
high-precision falsification check, not an interval proof of ``S_3``.
"""

from __future__ import annotations

import argparse
import json
import math
import time

from flint import acb, acb_series, arb, ctx


def _scaled_transform(t: arb, pi: arb, imaginary_unit: acb) -> arb:
    """Return ``exp(pi*t/8) xi((1-it)/2)/4`` for ``t>=0``."""

    s = (1 - imaginary_unit * t) / 2
    xi = (
        arb("0.5")
        * s
        * (s - 1)
        * ((-s / 2) * pi.log()).exp()
        * (s / 2).gamma()
        * s.zeta()
    )
    return (xi / 4 * (pi * t / 8).exp()).real


def scaled_transform_jet(t: arb, dps: int = 60) -> tuple[arb, arb, arb, arb]:
    """Return normalized ``Z, Z', Z'', Z'^2-Z Z''`` as Arb balls."""

    ctx.dps = dps
    old_cap = ctx.cap
    ctx.cap = max(old_cap, 4)
    try:
        pi = arb.pi()
        imaginary_unit = acb(0, 1)
        variable = acb_series([t, 1], prec=3)
        s = (1 - imaginary_unit * variable) / 2
        xi = (
            arb("0.5")
            * s
            * (s - 1)
            * ((-s / 2) * pi.log()).exp()
            * (s / 2).gamma()
            * s.zeta()
        )
        transformed = xi / 4 * (pi * variable / 8).exp()
        value = transformed[0].real
        first = transformed[1].real
        second = 2 * transformed[2].real
        laguerre = first * first - value * second
        return value, first, second, laguerre
    finally:
        ctx.cap = old_cap


def constant_sine_cubic_tail(p: arb, cutoff: arb, pi: arb) -> arb:
    """Return ``integral_cutoff^infinity sin(p*x)/x^3 dx``."""

    if p == 0:
        return arb(0)
    pw = p * cutoff
    return (
        pw.sin() / (2 * cutoff * cutoff)
        + p * pw.cos() / (2 * cutoff)
        - p * p * (pi / 2 - pw.si()) / 2
    )


def targeted_scaled_s3(
    t_raw: str,
    p_raw: str,
    dx_raw: str,
    margin_raw: str = "60",
    dps: int = 60,
) -> dict[str, object]:
    """Evaluate one normalized ``S_3`` by Arb-node Simpson quadrature."""

    ctx.dps = dps
    t = arb(t_raw)
    p = arb(p_raw)
    dx = arb(dx_raw)
    requested_margin = arb(margin_raw)
    if not (t >= 0 and p >= 0 and dx > 0 and requested_margin > 0):
        raise ValueError("require T,P>=0 and dx,margin>0")

    i_float = float(t / dx)
    i = int(round(i_float))
    if abs(i_float - i) > 1e-10:
        raise ValueError("T must be an integer multiple of dx")

    n = int(math.ceil(float((t + requested_margin) / dx) - 1e-12))
    if n % 2:
        n += 1
    cutoff = arb(n) * dx
    effective_margin = cutoff - t
    extent = i + n

    pi = arb.pi()
    imaginary_unit = acb(0, 1)
    started = time.time()
    transform = [
        _scaled_transform(arb(j) * dx, pi, imaginary_unit)
        for j in range(extent + 1)
    ]
    grid_seconds = time.time() - started
    _, _, _, laguerre = scaled_transform_jet(t, dps=dps)

    simpson_sum = arb(0)
    for j in range(n + 1):
        x = arb(j) * dx
        if j == 0:
            integrand = laguerre * p
        else:
            product_factor = (
                arb(1) if j <= i else (-pi * (x - t) / 4).exp()
            )
            gap = (
                transform[i] * transform[i]
                - product_factor * transform[i + j] * transform[abs(i - j)]
            )
            integrand = gap * (p * x).sin() / (x * x * x)
        weight = 1 if j in (0, n) else (4 if j % 2 else 2)
        simpson_sum += weight * integrand

    integral = dx * simpson_sum / 3
    integral += (
        transform[i]
        * transform[i]
        * constant_sine_cubic_tail(p, cutoff, pi)
    )
    value = laguerre - 2 * integral / pi
    relative = value / laguerre

    return {
        "schema": "zeta23.theta-s3-arb-simpson-target.v1",
        "T": t_raw,
        "P": p_raw,
        "dx": dx_raw,
        "requested_margin": margin_raw,
        "effective_margin": str(effective_margin),
        "cutoff": str(cutoff),
        "transform_nodes": extent + 1,
        "grid_seconds": grid_seconds,
        "scaled_laguerre": str(laguerre),
        "scaled_s3_discrete_simpson": str(value),
        "relative_to_laguerre": str(relative),
        "rigor_scope": (
            "Arb encloses node evaluation and the discrete Simpson sum; "
            "continuum quadrature and omitted product-tail errors are not "
            "enclosed"
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", required=True)
    parser.add_argument("--p", required=True)
    parser.add_argument("--dx", default="0.1")
    parser.add_argument("--margin", default="60")
    parser.add_argument("--dps", type=int, default=60)
    args = parser.parse_args()
    print(
        json.dumps(
            targeted_scaled_s3(
                args.t, args.p, args.dx, args.margin, args.dps
            ),
            indent=2,
        )
    )
