"""Finite falsifier for harmonic spectral-band collar propagation.

The old interval is represented by compactly supported triangular hats.  A
larger, nested uniform grid contributes ``collar`` coordinates.  Those
coordinates are first made L2-orthogonal to the old space, and are then
harmonically lifted with respect to

    h(f) = ||f||_2^2 + (1/2pi) int |fhat(t)|^2 log(1+4t^2)/2 dt.

All form matrices are assembled in x-space with mpmath.  In particular, this
probe has neither a Fourier cutoff nor Simpson quadrature.  It is a finite
diagnostic, not an operator theorem or an RH certificate.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import mpmath as mp

from hp_margins import Omega, hp_form, hp_lam_min, kernel_tail
from weil_core import PRIME_POWERS


def _symmetrize(a: mp.matrix) -> mp.matrix:
    out = mp.matrix(a.rows, a.cols)
    for i in range(a.rows):
        for j in range(a.cols):
            out[i, j] = (a[i, j] + a[j, i]) / 2
    return out


def _submatrix(a: mp.matrix, rows: list[int], cols: list[int]) -> mp.matrix:
    return mp.matrix([[a[i, j] for j in cols] for i in rows])


def _solve_left(a: mp.matrix, b: mp.matrix) -> mp.matrix:
    """Solve AX=B; mpmath's lu_solve handles only vector RHS reliably."""
    ans = mp.matrix(a.rows, b.cols)
    for j in range(b.cols):
        col = mp.lu_solve(a, mp.matrix([b[i, j] for i in range(b.rows)]))
        for i in range(a.rows):
            ans[i, j] = col[i]
    return ans


def wplus_diagonal(k: int, d: mp.mpf) -> mp.mpf:
    """Hat-basis diagonal for multiplier log(1+4t^2)/2.

    Frullani's identity gives

      log(1+4t^2)/2 = int_0^inf exp(-u/2) (1-cos(tu))/u du.

    Fourier inversion then reduces the entry to a compact piecewise-cubic
    integral plus one exponential-integral tail.
    """
    d = mp.mpf(d)
    kd = k * d
    cutoff = (k + 2) * d
    overlap0 = Omega(kd, d)

    def integrand(u: mp.mpf) -> mp.mpf:
        if u == 0:
            return mp.mpf(0)
        shifted = (Omega(kd - u, d) + Omega(kd + u, d)) / 2
        return (overlap0 - shifted) * mp.exp(-u / 2) / u

    points = {mp.mpf(0), cutoff}
    points.update(j * d for j in range(max(k - 2, 0), k + 3))
    ordered = sorted(x for x in points if 0 <= x <= cutoff)
    body = mp.quad(integrand, ordered)
    return body + overlap0 * mp.e1(cutoff / 2)


def unequal_hat_overlap(v: mp.mpf, d1: mp.mpf, d2: mp.mpf) -> mp.mpf:
    """Exact integral of two unit triangular hats separated by ``v``."""
    v, d1, d2 = mp.mpf(v), mp.mpf(d1), mp.mpf(d2)
    lo = max(-d1, v - d2)
    hi = min(d1, v + d2)
    if lo >= hi:
        return mp.mpf(0)
    knots = sorted({lo, hi, mp.mpf(0), v})
    knots = [x for x in knots if lo <= x <= hi]
    root3 = mp.sqrt(3)

    def hat(x: mp.mpf, center: mp.mpf, width: mp.mpf) -> mp.mpf:
        value = 1 - abs(x - center) / width
        return max(mp.mpf(0), value)

    total = mp.mpf(0)
    for left, right in zip(knots, knots[1:]):
        if right <= left:
            continue
        mid = (left + right) / 2
        half = (right - left) / 2
        x1 = mid - half / root3
        x2 = mid + half / root3
        total += half * (
            hat(x1, 0, d1) * hat(x1, v, d2)
            + hat(x2, 0, d1) * hat(x2, v, d2)
        )
    return total


def _correlation_breaks(v: mp.mpf, d1: mp.mpf, d2: mp.mpf) -> list[mp.mpf]:
    """Safe u-breakpoints for overlap(v-u) and overlap(v+u)."""
    local1 = (-d1, mp.mpf(0), d1)
    local2 = (-d2, mp.mpf(0), d2)
    separation_knots = {x - y for x in local1 for y in local2}
    cutoff = abs(v) + d1 + d2
    points = {mp.mpf(0), cutoff}
    points.update(abs(v - knot) for knot in separation_knots)
    return sorted(x for x in points if 0 <= x <= cutoff)


def wplus_entry(v: mp.mpf, d1: mp.mpf, d2: mp.mpf) -> mp.mpf:
    """Unequal-hat W_+ entry, cutoff-free in x-space."""
    v, d1, d2 = mp.mpf(v), mp.mpf(d1), mp.mpf(d2)
    overlap0 = unequal_hat_overlap(v, d1, d2)
    cutoff = abs(v) + d1 + d2

    def integrand(u: mp.mpf) -> mp.mpf:
        if u == 0:
            return mp.mpf(0)
        shifted = (
            unequal_hat_overlap(v - u, d1, d2)
            + unequal_hat_overlap(v + u, d1, d2)
        ) / 2
        return (overlap0 - shifted) * mp.exp(-u / 2) / u

    body = mp.quad(integrand, _correlation_breaks(v, d1, d2))
    return body + overlap0 * mp.e1(cutoff / 2)


def arch_entry(
    v: mp.mpf, d1: mp.mpf, d2: mp.mpf, twoa: mp.mpf = mp.mpf("0.5")
) -> mp.mpf:
    """Unequal-hat Re-digamma entry, cutoff-free in x-space."""
    v, d1, d2, twoa = map(mp.mpf, (v, d1, d2, twoa))
    overlap0 = unequal_hat_overlap(v, d1, d2)
    cutoff = abs(v) + d1 + d2

    def integrand(u: mp.mpf) -> mp.mpf:
        if u == 0:
            return mp.mpf(0)
        shifted = (
            unequal_hat_overlap(v - u, d1, d2)
            + unequal_hat_overlap(v + u, d1, d2)
        ) / 2
        return (overlap0 - shifted) * mp.exp(-twoa * u) / (-mp.expm1(-2 * u))

    body = mp.quad(integrand, _correlation_breaks(v, d1, d2))
    return (
        mp.digamma(twoa / 2) * overlap0
        + 2 * body
        + 2 * overlap0 * kernel_tail(cutoff, twoa)
    )


def _pole_transform(center: mp.mpf, width: mp.mpf, sign: int) -> mp.mpf:
    s = mp.mpf(sign) / 2
    return mp.exp(s * center) * (2 * mp.cosh(s * width) - 2) / (s * s * width)


def actual_form_entry(
    ci: mp.mpf,
    di: mp.mpf,
    cj: mp.mpf,
    dj: mp.mpf,
    project_support: mp.mpf,
) -> mp.mpf:
    """Actual zeta Weil-form entry for two arbitrary symmetric hats."""
    separation = cj - ci
    gram = unequal_hat_overlap(separation, di, dj)
    value = arch_entry(separation, di, dj) - mp.log(mp.pi) * gram
    for nn, prime in PRIME_POWERS:
        shift = mp.log(nn)
        if 2 * shift >= project_support:
            continue
        weight = 2 * mp.log(prime) / mp.sqrt(nn)
        shifted = (
            unequal_hat_overlap(separation - shift, di, dj)
            + unequal_hat_overlap(separation + shift, di, dj)
        ) / 2
        value -= weight * shifted
    ppi = _pole_transform(ci, di, +1)
    pmi = _pole_transform(ci, di, -1)
    ppj = _pole_transform(cj, dj, +1)
    pmj = _pole_transform(cj, dj, -1)
    return value + ppi * pmj + pmi * ppj


def mixed_extension_forms(
    old_degree: int,
    collar_degree: int,
    delta: mp.mpf,
    event_prime: int,
    dps: int,
):
    """Old uniform hats plus independently refined, disjoint collar hats.

    The collar hats are the standard interior-node basis on each open outer
    interval.  They vanish at the old boundary, which is only a pointwise
    restriction and is harmless for this finite conforming diagnostic in the
    logarithmic form domain.
    """
    with mp.workdps(dps + 15):
        lold = 2 * mp.log(event_prime)
        lnew = lold + mp.mpf(delta)
        old_radius = lold / 4
        old_width = lold / (2 * (old_degree + 1))
        old_centers = [
            -old_radius + (i + 1) * old_width for i in range(old_degree)
        ]
        physical_collar = mp.mpf(delta) / 4
        collar_width = physical_collar / (collar_degree + 1)
        left = [
            -old_radius - (j + 1) * collar_width for j in range(collar_degree)
        ]
        right = [
            old_radius + (j + 1) * collar_width for j in range(collar_degree)
        ]
        collar_centers = left + right
        collar_widths = [collar_width] * len(collar_centers)

        qold, gold = hp_form(lold, old_degree, dps=dps + 5)
        hold = reference_form(lold, old_degree, dps=dps + 5)
        total = old_degree + len(collar_centers)
        q = mp.matrix(total)
        g = mp.matrix(total)
        h = mp.matrix(total)
        for i in range(old_degree):
            for j in range(old_degree):
                q[i, j], g[i, j], h[i, j] = qold[i, j], gold[i, j], hold[i, j]

        centers = old_centers + collar_centers
        widths = [old_width] * old_degree + collar_widths
        for i in range(total):
            start = max(i, old_degree) if i < old_degree else i
            for j in range(start, total):
                sep = centers[j] - centers[i]
                gij = unequal_hat_overlap(sep, widths[i], widths[j])
                hij = gij + wplus_entry(sep, widths[i], widths[j])
                qij = actual_form_entry(
                    centers[i], widths[i], centers[j], widths[j], lnew
                )
                q[i, j] = q[j, i] = qij
                g[i, j] = g[j, i] = gij
                h[i, j] = h[j, i] = hij
        return q, g, h, lold, lnew


def reference_form(L: mp.mpf, m: int, dps: int) -> mp.matrix:
    """Assemble h=G+W_+ for the same uniform full-grid hats as hp_form."""
    with mp.workdps(dps + 15):
        d = mp.mpf(L) / (2 * (m + 1))
        diagonal = [Omega(k * d, d) + wplus_diagonal(k, d) for k in range(m)]
        h = mp.matrix(m)
        for i in range(m):
            for j in range(m):
                h[i, j] = diagonal[abs(i - j)]
        out = mp.matrix(m)
        with mp.workdps(dps):
            for i in range(m):
                for j in range(m):
                    out[i, j] = +h[i, j]
    return out


def _block(a: mp.matrix, old: list[int], collar: list[int]):
    return (
        _submatrix(a, old, old),
        _submatrix(a, old, collar),
        _submatrix(a, collar, collar),
    )


def l2_orthogonalized_blocks(
    q: mp.matrix, h: mp.matrix, g: mp.matrix, old: list[int], collar: list[int]
):
    """Congruence for Psi -> Psi-Phi Go^{-1}Goc, returned by form."""
    go, goc, gcc = _block(g, old, collar)
    correction = _solve_left(go, goc)

    def corrected(a: mp.matrix):
        aa, x, dd = _block(a, old, collar)
        xo = x - aa * correction
        do = dd - x.T * correction - correction.T * x + correction.T * aa * correction
        return _symmetrize(aa), xo, _symmetrize(do)

    aq, xq, dq = corrected(q)
    hh, yh, zh = corrected(h)
    gg, crossg, gc = corrected(g)
    return {
        "Q": (aq, xq, dq),
        "H": (hh, yh, zh),
        "G": (gg, crossg, gc),
        "l2_correction": correction,
        "raw_Goc": goc,
    }


def generalized_extreme(b: mp.matrix, s: mp.matrix, which: str) -> mp.mpf:
    """Extreme generalized eigenvalue of symmetric (B,S), S positive."""
    if b.rows == 0:
        return mp.mpf(0)
    chol = mp.cholesky(_symmetrize(s))
    left = _solve_left(chol, _symmetrize(b))
    whitened = _solve_left(chol, left.T).T
    eigvals = mp.eigsy(_symmetrize(whitened), eigvals_only=True)
    values = [eigvals[i] for i in range(eigvals.rows)]
    if which == "max":
        return max(values)
    if which == "min":
        return min(values)
    raise ValueError("which must be 'min' or 'max'")


def _max_abs(a: mp.matrix) -> mp.mpf:
    if not a.rows or not a.cols:
        return mp.mpf(0)
    return max(abs(a[i, j]) for i in range(a.rows) for j in range(a.cols))


def _columns(vectors: list[list[mp.mpf]]) -> mp.matrix:
    if not vectors:
        return mp.matrix(0, 0)
    rows = len(vectors[0])
    ans = mp.matrix(rows, len(vectors))
    for j, vec in enumerate(vectors):
        for i, value in enumerate(vec):
            ans[i, j] = value
    return ans


def _band_rho(
    u: mp.matrix, xtilde: mp.matrix, s: mp.matrix, indices: Iterable[int]
) -> mp.mpf:
    ids = list(indices)
    if not ids:
        return mp.mpf(0)
    ub = _submatrix(u, list(range(u.rows)), ids)
    f = ub.T * xtilde
    return generalized_extreme(f.T * f, s, "max")


def _mpstr(x: mp.mpf, digits: int = 18) -> str:
    return mp.nstr(x, digits, min_fixed=0, max_fixed=0)


def analyze_nested_collar(
    old_degree: int,
    collar_degree: int,
    dps: int = 50,
    event_prime: int = 5,
    _assembled=None,
) -> dict:
    """Run one spectral-band diagnostic at L=2 log(event_prime).

    ``_assembled`` is an internal hook used by :func:`analyze_mixed_collar`;
    callers should normally leave it unset.
    """
    if old_degree < 3 or collar_degree < 1:
        raise ValueError("old_degree >= 3 and collar_degree >= 1 are required")
    with mp.workdps(dps + 15):
        if _assembled is None:
            geometry = "nested_uniform_galerkin_complement"
            lold = 2 * mp.log(event_prime)
            total = old_degree + 2 * collar_degree
            # This makes the central old hats exactly the old uniform grid.
            lnew = lold * mp.mpf(total + 1) / (old_degree + 1)
            qfull, gfull = hp_form(lnew, total, dps=dps + 5)
            hfull = reference_form(lnew, total, dps=dps + 5)
            old = list(range(collar_degree, collar_degree + old_degree))
            collar = list(range(collar_degree)) + list(
                range(collar_degree + old_degree, total)
            )
        else:
            qfull, gfull, hfull, lold, lnew, old, collar, geometry = _assembled
            total = qfull.rows
        delta = lnew - lold
        old_mesh = lold / (2 * (old_degree + 1))
        if geometry == "literal_disjoint_collar_hats":
            collar_mesh = delta / (4 * (collar_degree + 1))
        else:
            collar_mesh = old_mesh
        mesh_ratio = old_mesh / collar_mesh
        blocks = l2_orthogonalized_blocks(qfull, hfull, gfull, old, collar)
        a, x, dmat = blocks["Q"]
        h, y, z = blocks["H"]
        go, goc_after, gc = blocks["G"]

        k = _solve_left(h, y)
        s = _symmetrize(z - y.T * k)
        xtilde = x - a * k
        dtilde = _symmetrize(
            dmat - x.T * k - k.T * x + k.T * a * k
        )

        raa = a - h
        ray = x - y
        raz = dmat - z
        cross_residual = ray - raa * k
        j_residual = raz - ray.T * k - k.T * ray + k.T * raa * k

        lambdas, vectors = hp_lam_min(
            a, go, nev=old_degree, dps=dps, vectors=True
        )
        u = _columns(vectors)
        f = u.T * xtilde
        response = mp.matrix(s.rows)
        for j, lam in enumerate(lambdas):
            if lam <= 0:
                response = None
                break
            row = mp.matrix([[f[j, col] for col in range(f.cols)]])
            response += row.T * row / lam

        high_ids: list[int] = []
        bands: dict[int, list[int]] = {}
        nonpositive: list[int] = []
        for idx, lam in enumerate(lambdas):
            if lam <= 0:
                nonpositive.append(idx)
            elif lam > 1:
                high_ids.append(idx)
            else:
                band = int(mp.floor(-mp.log(lam, 2)))
                bands.setdefault(band, []).append(idx)

        rho_high = _band_rho(u, xtilde, s, high_ids)
        band_rows = []
        carleson_raw = rho_high
        response_bound = rho_high
        for band in sorted(bands):
            rho = _band_rho(u, xtilde, s, bands[band])
            scaled = (band + 1) ** 2 * mp.power(2, band) * rho
            carleson_raw = max(carleson_raw, scaled)
            response_bound += mp.power(2, band + 1) * rho
            band_rows.append(
                {
                    "band": band,
                    "count": len(bands[band]),
                    "lambda_min": _mpstr(min(lambdas[i] for i in bands[band])),
                    "lambda_max": _mpstr(max(lambdas[i] for i in bands[band])),
                    "rho": _mpstr(rho),
                    "weighted_rho": _mpstr(scaled),
                }
            )

        nu = generalized_extreme(dtilde, s, "min")
        diagonal_loss = max(mp.mpf(0), 1 - nu)
        raw_epsilon = max(diagonal_loss, carleson_raw)
        log_factor = mp.log(mp.e / delta)
        k_num = log_factor * raw_epsilon
        ref_numerator = k.T * go * k + gc
        k_ref = log_factor * generalized_extreme(ref_numerator, s, "max")

        actual_response = None
        schur_min = None
        inverse_identity_error = None
        k_direct_response = None
        ward_ratio = None
        if response is not None:
            actual_response = generalized_extreme(response, s, "max")
            schur_min = generalized_extreme(dtilde - response, s, "min")
            direct = xtilde.T * _solve_left(a, xtilde)
            inverse_identity_error = _max_abs(direct - response)
            k_direct_response = log_factor * actual_response
            ward_ratio = generalized_extreme(response, ref_numerator, "max")

        sufficient_schur_margin = nu - response_bound
        result = {
            "status": "FINITE_DIAGNOSTIC_ONLY",
            "event_prime": event_prime,
            "geometry": geometry,
            "old_project_support": _mpstr(lold),
            "new_project_support": _mpstr(lnew),
            "delta_project_support": _mpstr(delta),
            "old_degree": old_degree,
            "collar_degree_each_side": collar_degree,
            "total_degree": total,
            "dps": dps,
            "old_hat_halfwidth": _mpstr(old_mesh),
            "collar_hat_halfwidth": _mpstr(collar_mesh),
            "old_to_collar_mesh_ratio": _mpstr(mesh_ratio),
            "old_lambda_min": _mpstr(min(lambdas)),
            "old_lambda_max": _mpstr(max(lambdas)),
            "nonpositive_old_modes": nonpositive,
            "nu_Dtilde_over_S": _mpstr(nu),
            "diagonal_loss": _mpstr(diagonal_loss),
            "rho_high": _mpstr(rho_high),
            "carleson_raw_epsilon": _mpstr(carleson_raw),
            "raw_epsilon": _mpstr(raw_epsilon),
            "log_factor": _mpstr(log_factor),
            "K_num": _mpstr(k_num),
            "K_ref": _mpstr(k_ref),
            "K_diagonal": _mpstr(log_factor * diagonal_loss),
            "K_direct_response": (
                None if k_direct_response is None else _mpstr(k_direct_response)
            ),
            "boundary_Ward_ratio": (
                None if ward_ratio is None else _mpstr(ward_ratio)
            ),
            "scalar_Kresponse_over_Kref": (
                None
                if k_direct_response is None or k_ref == 0
                else _mpstr(k_direct_response / k_ref)
            ),
            "dyadic_bands": band_rows,
            "spectral_response_bound_over_S": _mpstr(response_bound),
            "sufficient_schur_margin_over_S": _mpstr(sufficient_schur_margin),
            "actual_response_over_S": (
                None if actual_response is None else _mpstr(actual_response)
            ),
            "actual_schur_min_over_S": (
                None if schur_min is None else _mpstr(schur_min)
            ),
            "checks": {
                "L2_cross_after_orthogonalization_max_abs": _mpstr(
                    _max_abs(goc_after)
                ),
                "harmonic_cross_after_lift_max_abs": _mpstr(_max_abs(y - h * k)),
                "residual_cross_identity_max_abs": _mpstr(
                    _max_abs(xtilde - cross_residual)
                ),
                "residual_diagonal_identity_max_abs": _mpstr(
                    _max_abs(dtilde - (s + j_residual))
                ),
                "inverse_spectral_identity_max_abs": (
                    None
                    if inverse_identity_error is None
                    else _mpstr(inverse_identity_error)
                ),
            },
        }
    return result


def analyze_mixed_collar(
    old_degree: int,
    collar_degree: int,
    delta: mp.mpf | str | float,
    dps: int = 50,
    event_prime: int = 5,
) -> dict:
    """Probe a fixed old grid with independently shrinking/refined collars."""
    with mp.workdps(dps + 15):
        delta_mp = mp.mpf(str(delta))
        if delta_mp <= 0:
            raise ValueError("delta must be positive")
        q, g, h, lold, lnew = mixed_extension_forms(
            old_degree, collar_degree, delta_mp, event_prime, dps
        )
    old = list(range(old_degree))
    collar = list(range(old_degree, q.rows))
    assembled = (
        q,
        g,
        h,
        lold,
        lnew,
        old,
        collar,
        "literal_disjoint_collar_hats",
    )
    return analyze_nested_collar(
        old_degree,
        collar_degree,
        dps=dps,
        event_prime=event_prime,
        _assembled=assembled,
    )


def run_scan(
    pairs: list[tuple[int, int]], dps: int, event_prime: int = 5
) -> dict:
    rows = [
        analyze_nested_collar(m, c, dps=dps, event_prime=event_prime)
        for m, c in pairs
    ]
    return {
        "schema": "zeta23.harmonic_schur_collar_probe.v1",
        "interpretation": (
            "Finite conforming evidence only. Aggregate Schur, reference, and "
            "response statistics must be tested under matched old/collar refinement; "
            "the formerly proposed bandwise HSBCR allocation is not inferred."
        ),
        "rows": rows,
    }


def run_mixed_scan(
    old_degree: int,
    collar_degree: int,
    deltas: list[str],
    dps: int,
    event_prime: int = 5,
) -> dict:
    rows = [
        analyze_mixed_collar(
            old_degree, collar_degree, delta, dps=dps, event_prime=event_prime
        )
        for delta in deltas
    ]
    return {
        "schema": "zeta23.harmonic_schur_collar_probe.v1",
        "interpretation": (
            "Finite conforming evidence only. Mixed mode decouples collar width "
            "from old/collar Galerkin resolution."
        ),
        "rows": rows,
    }


def _pairs(text: str) -> list[tuple[int, int]]:
    ans = []
    for item in text.split(","):
        left, right = item.split(":")
        ans.append((int(left), int(right)))
    return ans


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pairs", default="12:1,20:1,28:1")
    parser.add_argument("--mode", choices=("nested", "mixed"), default="nested")
    parser.add_argument("--old-degree", type=int, default=20)
    parser.add_argument("--collar-degree", type=int, default=2)
    parser.add_argument("--deltas", default="0.2,0.1,0.05")
    parser.add_argument("--dps", type=int, default=45)
    parser.add_argument("--event-prime", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.mode == "nested":
        payload = run_scan(_pairs(args.pairs), args.dps, args.event_prime)
    else:
        payload = run_mixed_scan(
            args.old_degree,
            args.collar_degree,
            args.deltas.split(","),
            args.dps,
            args.event_prime,
        )
    rendered = json.dumps(payload, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
