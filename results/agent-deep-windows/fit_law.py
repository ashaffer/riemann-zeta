"""fit_law.py — refit of the envelope law  ln lam = A - b e^{L/2} (L/2 + c0)
over the old five windows plus the new deep rungs, tail extrapolation of the
per-L basis ladders, residual analysis, and the 13-window forecast.

The law is linear in (A, beta1, beta2) with X1 = (L/2) e^{L/2}, X2 = e^{L/2}:
    ln lam = A + beta1 X1 + beta2 X2,   b = -beta1,  c0 = beta2 / beta1.
Every lam used is a Rayleigh-Ritz UPPER bound (one-sided bias: true values can
only be lower, so measured points can only sit ABOVE the true envelope).

Reads priors.csv (recorded values from results/RESULTS.md) and runs.csv (this
agent's runs); writes fit_report.txt next to itself and prints it.
"""
import csv
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path, src):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path) as f:
        for r in csv.DictReader(f):
            rows.append(dict(L=float(r["L"]), m=int(r["m"]),
                             lam=float(r["lam_min"]), src=src,
                             tag=r.get("source", r.get("tag", ""))))
    return rows


def lstsq3(pts):
    """Least squares for ln lam = A + b1*X1 + b2*X2 (normal equations, 3x3)."""
    rows = [(1.0, (p["L"] / 2) * math.exp(p["L"] / 2), math.exp(p["L"] / 2),
             math.log(p["lam"])) for p in pts]
    n = 3
    M = [[sum(r[i] * r[j] for r in rows) for j in range(n)] for i in range(n)]
    v = [sum(r[i] * r[3] for r in rows) for i in range(n)]
    # Gaussian elimination with partial pivoting
    for c in range(n):
        piv = max(range(c, n), key=lambda i: abs(M[i][c]))
        M[c], M[piv] = M[piv], M[c]
        v[c], v[piv] = v[piv], v[c]
        for i in range(c + 1, n):
            f = M[i][c] / M[c][c]
            for j in range(c, n):
                M[i][j] -= f * M[c][j]
            v[i] -= f * v[c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (v[i] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    A, b1, b2 = x
    return dict(A=A, b=-b1, c0=b2 / b1, beta=(A, b1, b2))


def law_ln(A, b, c0, L):
    return A - b * math.exp(L / 2) * (L / 2 + c0)


def residuals(fit, pts):
    return [(p, math.log(p["lam"]) - law_ln(fit["A"], fit["b"], fit["c0"], p["L"]))
            for p in pts]


def aitken(seq):
    """Aitken delta^2 limit estimate for an equal-step monotone ladder."""
    l1, l2, l3 = seq[-3:]
    d1, d2 = l1 - l2, l2 - l3
    if d1 <= d2 or d2 <= 0:
        return None, None
    r = d2 / d1
    return l3 - d2 * r / (1 - r), r


CANON = (10.2, 1.755, 4.0)   # the recorded law of RESULTS.md / ENVELOPE.md
FOURPI = 4 * math.pi         # universal Fuchs/prolate decay rate per e^{L/2}


def lstsq_general(rows):
    """rows = (x1..xk, y); returns least-squares coefficients."""
    n = len(rows[0]) - 1
    M = [[sum(r[i] * r[j] for r in rows) for j in range(n)] for i in range(n)]
    v = [sum(r[i] * r[n] for r in rows) for i in range(n)]
    for c in range(n):
        piv = max(range(c, n), key=lambda i: abs(M[i][c]))
        M[c], M[piv] = M[piv], M[c]
        v[c], v[piv] = v[piv], v[c]
        for i in range(c + 1, n):
            f = M[i][c] / M[c][c]
            for j in range(c, n):
                M[i][j] -= f * M[c][j]
            v[i] -= f * v[c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (v[i] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x


def fit_fuchs(pts, fix_b=None):
    """Fuchs-form fit  ln lam = A' - b' e^{L/2} + p (L/2).
    If fix_b is given, b' is held fixed (fit A', p only)."""
    if fix_b is None:
        rows = [(1.0, -math.exp(p["L"] / 2), p["L"] / 2, math.log(p["lam"]))
                for p in pts]
        A, b, pw = lstsq_general(rows)
        return dict(A=A, b=b, p=pw)
    rows = [(1.0, p["L"] / 2,
             math.log(p["lam"]) + fix_b * math.exp(p["L"] / 2)) for p in pts]
    A, pw = lstsq_general(rows)
    return dict(A=A, b=fix_b, p=pw)


def fuchs_ln(f, L):
    return f["A"] - f["b"] * math.exp(L / 2) + f["p"] * (L / 2)


def algebraic_limit(ms, lams, beta):
    """Fit lam(m) = lam_inf + C m^-beta through the last two points."""
    m2, m3 = ms[-2], ms[-1]
    l2, l3 = lams[-2], lams[-1]
    C = (l2 - l3) / (m2 ** -beta - m3 ** -beta)
    return l3 - C * m3 ** -beta


def mln(m):
    return m * math.log(m)


def creep_limit(ms, lams):
    """Numerical-analysis expert's Lemma 1 creep model:
    lam(m) = lam_inf + C/(m ln m), C calibrated on the LAST decrement.
    When the ladder is still in the geometric plunge (ratio << the
    (m ln m)^-1 model's own ratio ~0.72-0.75 for our steps), the last
    decrement exceeds the true creep decrement, so C is overestimated and
    this extrapolation is a conservative LOWER estimate of lam_inf.
    Returns (lam_inf_est, C, next_decrement_prediction)."""
    m2, m3 = ms[-2], ms[-1]
    l2, l3 = lams[-2], lams[-1]
    C = (l2 - l3) / (1 / mln(m2) - 1 / mln(m3))
    m4 = m3 + (m3 - m2)
    return (l3 - C / mln(m3), C, C * (1 / mln(m3) - 1 / mln(m4)))


def main():
    priors = load(os.path.join(HERE, "priors.csv"), "prior")
    runs = load(os.path.join(HERE, "runs.csv"), "new")
    allpts = priors + runs
    out = []

    def emit(s=""):
        out.append(s)
        print(s)

    # ---- deepest-m upper bound per L, and per-L ladders
    byL = {}
    for p in allpts:
        byL.setdefault(p["L"], []).append(p)
    for L in byL:
        byL[L].sort(key=lambda p: p["m"])
    deepest = {L: byL[L][-1] for L in byL}

    emit("== per-L ladders (all values Rayleigh-Ritz upper bounds) ==")
    extrap = {}
    for L in sorted(byL):
        lad = byL[L]
        emit("L = %.3f : " % L + "   ".join(
            "m=%d %.6e%s" % (p["m"], p["lam"], "*" if p["src"] == "new" else "")
            for p in lad))
        mono = all(lad[i]["lam"] > lad[i + 1]["lam"] for i in range(len(lad) - 1))
        if len(lad) > 1:
            emit("           monotone decreasing in m: %s" % ("PASS" if mono else "FAIL <-- BUG"))
        if len(lad) >= 3 and mono:
            ms = [p["m"] for p in lad[-3:]]
            ls = [p["lam"] for p in lad[-3:]]
            if ms[1] - ms[0] == ms[2] - ms[1]:
                # creep model applies to any monotone equal-step triple
                cl0, cC0, cd0 = creep_limit(ms, ls)
                extrap.setdefault(L, {})["creep"] = cl0
                extrap[L]["creep_next_d"] = cd0
                lim, r = aitken(ls)
                if lim is None:
                    emit("           tail: decrements NON-monotone (staircase) "
                         "- Aitken invalid; hard UB %.3e; creep-model lim %.3e"
                         % (ls[-1], cl0))
                if lim is not None:
                    a10 = algebraic_limit(ms, ls, 1.0)
                    a12 = algebraic_limit(ms, ls, 1.2)
                    phase = ("PLUNGE (geometric, Aitken reliable)" if r < 0.55
                             else "creep (algebraic tail, Aitken optimistic)")
                    extrap[L] = dict(aitken=lim, ratio=r)
                    txt = "           tail: step ratio %.3f [%s]\n" % (r, phase)
                    txt += "                 Aitken lim %.3e" % lim
                    if a10 > 0 and r > 0.3:      # algebraic model consistent
                        extrap[L]["alg10"] = a10
                        extrap[L]["alg12"] = a12
                        txt += (" | m^-1.0 lim %.3e | m^-1.2 lim %.3e"
                                % (a10, a12))
                    else:
                        txt += (" | algebraic-tail model inconsistent with "
                                "ratio (plunge): bracket = [Aitken, lam(m_max)]")
                    emit(txt)
                    # expert creep model (Lemma 1): lam_inf, calibrated C, and
                    # the (m ln m)^-1 model's own decrement ratio for these steps
                    cl, cC, cd = creep_limit(ms, ls)
                    rmodel = ((1 / mln(ms[1]) - 1 / mln(ms[2]))
                              / (1 / mln(ms[0]) - 1 / mln(ms[1])))
                    extrap[L]["creep"] = cl
                    extrap[L]["creep_next_d"] = cd
                    emit("                 creep-model (mlnm) lim %.3e "
                         "[model ratio %.3f vs measured %.3f%s]"
                         % (cl, rmodel, r,
                            "; plunge-dominated: C overestimated, lim is a "
                            "conservative floor" if r < 0.5 * rmodel else ""))
            if len(lad) >= 4:
                ms4 = [p["m"] for p in lad[-4:]]
                ls4 = [p["lam"] for p in lad[-4:]]
                if ms4[1] - ms4[0] == ms4[2] - ms4[1] == ms4[3] - ms4[2]:
                    # model discrimination: predict lam(m4) from first triple
                    limg, rg = aitken(ls4[:3])
                    if limg is not None:
                        dg = (ls4[1] - ls4[2]) * rg
                        clim, cc, cdn = creep_limit(ms4[:3], ls4[:3])
                        emit("           4-pt MODEL TEST at m=%d: measured %.4e | "
                             "geometric predicts %.4e | creep-model predicts %.4e"
                             % (ms4[3], ls4[3], ls4[2] - dg, ls4[2] - cdn))
            if len(lad) >= 4 and lad[-4]["m"] == ms[0] - (ms[2] - ms[1]):
                lim2, r2 = aitken([p["lam"] for p in lad[-4:-1]])
                if lim2 is not None and L in extrap:
                    emit("           4-pt check: previous-triple Aitken %.3e "
                         "(vs %.3e; agreement gauges extrapolation trust)"
                         % (lim2, extrap[L]["aitken"]))
                    extrap[L]["aitken_prev"] = lim2
    emit()

    # ---- fits
    solid = [deepest[L] for L in sorted(deepest) if L <= 4.03]
    four = [p for p in solid if p["L"] < 4.0]
    all_deepest = [deepest[L] for L in sorted(deepest)]
    no_deepest = [p for p in all_deepest if p["L"] <= 4.51]

    fits = [
        ("F0 four original fit windows (1.75..3.555)", four),
        ("F1 five solid windows (1.75..4.025)", solid),
        ("F2 ALL windows, deepest-m upper bounds", all_deepest),
        ("F3 all except deepest points (L<=4.50)", no_deepest),
    ]
    # F4: replace upper bounds by tail limits where available.  For the two
    # shallowest windows the recorded RESULTS.md tail estimates from richer
    # m-ladders are used (m=8..48 at L=1.75 -> ~3.13e-5; m=12..64 at
    # L=2.485 -> ~3.49-3.50e-10); elsewhere this session's Aitken limits.
    recorded_limits = {1.750: 3.13e-5, 2.485: 3.495e-10}
    subst = []
    for L in sorted(deepest):
        p = dict(deepest[L])
        if L in extrap:
            p = dict(p)
            p["lam"] = extrap[L]["aitken"]
            p["tag"] = "aitken-extrapolated"
        elif L in recorded_limits:
            p = dict(p)
            p["lam"] = recorded_limits[L]
            p["tag"] = "recorded-RESULTS.md-limit"
        subst.append(p)
    fits.append(("F4 ALL windows, tail-extrapolated limits where available", subst))
    # F6: the numerical-analysis expert's reading — creep-model limits
    creep_pts = []
    for L in sorted(deepest):
        p = dict(deepest[L])
        if L in extrap and "creep" in extrap[L] and extrap[L]["creep"] > 0:
            p["lam"] = extrap[L]["creep"]
            p["tag"] = "creep-model-extrapolated"
        elif L in recorded_limits:
            p["lam"] = recorded_limits[L]
            p["tag"] = "recorded-RESULTS.md-limit"
        creep_pts.append(p)
    fits.append(("F6 ALL windows, expert creep-model (mlnm) limits", creep_pts))
    # F1b: solid windows only, best-limit values (the clean baseline law)
    f1b_pts = [p for p in subst if p["L"] <= 4.03]
    fits.append(("F1b solid windows (1.75..4.025), best-limit values", f1b_pts))

    results = {}
    for name, pts in fits:
        f = lstsq3(pts)
        results[name] = (f, pts)
        emit("== %s ==" % name)
        emit("   A = %+.4f   b = %.5f   c0 = %+.4f" % (f["A"], f["b"], f["c0"]))
        emit("   residuals r = ln lam_obs - ln lam_fit (positive = point above law):")
        for p, r in residuals(f, pts):
            emit("     L=%.3f  m=%3d  lam=%.4e  r=%+.4f  (%.1f%% in lam)"
                 % (p["L"], p["m"], p["lam"], r, 100 * (math.exp(r) - 1)))
        emit()

    # ---- the bend question: laws evaluated at the deep rungs
    f1 = results["F1b solid windows (1.75..4.025), best-limit values"][0]
    for lawname, (A_, b_, c_) in (
            ("canonical law (10.2, 1.755, 4.0)", CANON),
            ("solid-window best-limit refit F1b", (f1["A"], f1["b"], f1["c0"]))):
        emit("== deep rungs against the %s ==" % lawname)
        emit("   (r > 0: measured/extrapolated point ABOVE the law)")
        for L in sorted(deepest):
            if L < 4.1:
                continue
            pred = law_ln(A_, b_, c_, L)
            ub = math.log(deepest[L]["lam"])
            line = ("   L=%.3f  pred %.2e | deepest-m (m=%d) ub %.2e "
                    "r_ub %+.3f" % (L, math.exp(pred), deepest[L]["m"],
                                    deepest[L]["lam"], ub - pred))
            if L in extrap:
                cands = [extrap[L][k] for k in
                         ("aitken", "alg10", "alg12", "creep")
                         if k in extrap[L] and extrap[L][k] > 0]
                lo, hi = min(cands), max(cands)
                line += (" | lim[geo %.2e / creep %s] r [%+.2f, %+.2f]" % (
                    extrap[L]["aitken"],
                    ("%.2e" % extrap[L]["creep"]) if "creep" in extrap[L]
                    and extrap[L]["creep"] > 0 else "n/a",
                    math.log(lo) - pred, math.log(hi) - pred))
            emit(line)
        emit()

    # ---- Fuchs-form fits on the deep windows (extrapolated limits preferred)
    deep_pts = []
    excluded = []
    for L in sorted(deepest):
        if L < 4.2:
            continue
        p = dict(deepest[L])
        if L in extrap:
            p["lam"] = extrap[L]["aitken"]
            p["tag"] = "aitken"
            deep_pts.append(p)
        else:
            excluded.append(p)
    fuchs_fits = {}
    if len(deep_pts) >= 3:
        emit("== Fuchs-form fits  ln lam = A' - b' e^{L/2} + p (L/2)  on deep windows ==")
        emit("   points (extrapolated limits ONLY): " + ", ".join(
            "L=%.2f %.3e" % (p["L"], p["lam"]) for p in deep_pts))
        if excluded:
            emit("   excluded (unconverged raw UB): " + ", ".join(
                "L=%.2f %.3e(m=%d)" % (p["L"], p["lam"], p["m"])
                for p in excluded))
        ff = fit_fuchs(deep_pts)
        fuchs_fits["free"] = ff
        emit("   free fit:   A' = %+.3f   b' = %.4f  (4pi = %.4f; ratio %.4f)   p = %.3f"
             % (ff["A"], ff["b"], FOURPI, ff["b"] / FOURPI, ff["p"]))
        # 2-param: p fixed at Fuchs n=4 value 4.5, fit (A', b') — the clean
        # slope test (subtract 4.5(L/2) from ln lam, fit linear in c)
        rows = [(1.0, -math.exp(p["L"] / 2),
                 math.log(p["lam"]) - 4.5 * (p["L"] / 2)) for p in deep_pts]
        Ap, bp = lstsq_general(rows)
        fuchs_fits["fixp45"] = dict(A=Ap, b=bp, p=4.5)
        emit("   p=4.5 fit:  A' = %+.3f   b' = %.4f  (b'/4pi = %.4f)"
             % (Ap, bp, bp / FOURPI))
        f4 = fit_fuchs(deep_pts, fix_b=FOURPI)
        fuchs_fits["fix4pi"] = f4
        emit("   b'=4pi fit: A' = %+.3f   p = %.3f  (Fuchs n=4 predicts p = 4.5)"
             % (f4["A"], f4["p"]))
        for name, f in (("free", ff), ("fixp45", fuchs_fits["fixp45"]),
                        ("fix4pi", f4)):
            emit("   residuals (%s):" % name)
            for p in deep_pts:
                r = math.log(p["lam"]) - fuchs_ln(f, p["L"])
                emit("     L=%.3f  r=%+.4f (%.1f%%)" % (p["L"], r,
                                                        100 * (math.exp(r) - 1)))
        # pairwise slope estimates with the Fuchs n=4 prefactor power fixed:
        # b'_pair = [4.5 d(L/2) - d(ln lam)] / d(e^{L/2})
        emit("   pairwise slopes (p = 4.5 fixed), to compare with 4pi = %.4f:"
             % FOURPI)
        for pa, pb in zip(deep_pts, deep_pts[1:]):
            dc = math.exp(pb["L"] / 2) - math.exp(pa["L"] / 2)
            dln = math.log(pb["lam"]) - math.log(pa["lam"])
            dl2 = (pb["L"] - pa["L"]) / 2
            emit("     L %.2f -> %.2f :  b'_pair = %.4f  (b'/4pi = %.4f)"
                 % (pa["L"], pb["L"], (4.5 * dl2 - dln) / dc,
                    (4.5 * dl2 - dln) / dc / FOURPI))
        # crossover of canonical-law local slope 1.755(L/2+5) with 4pi
        Lx = 2 * (FOURPI / 1.755 - 5)
        emit("   canonical-law local slope 1.755(L/2+5) crosses 4pi at L = %.3f"
             % Lx)
        emit()

    # ---- forecast for the 13-window
    emit("== forecast, 13-window (L in [5.13, 5.50], thresholds 2ln13=5.130 / 2ln16=5.545) ==")
    for name in ("F1 five solid windows (1.75..4.025)",
                 "F2 ALL windows, deepest-m upper bounds",
                 "F4 ALL windows, tail-extrapolated limits where available"):
        f = results[name][0]
        preds = ["L=%.2f: %.2e" % (L, math.exp(law_ln(f["A"], f["b"], f["c0"], L)))
                 for L in (5.13, 5.20, 5.30, 5.40, 5.50)]
        emit("   %s:" % name)
        emit("     " + "   ".join(preds))
    for name, f in fuchs_fits.items():
        preds = ["L=%.2f: %.2e" % (L, math.exp(fuchs_ln(f, L)))
                 for L in (5.13, 5.20, 5.30, 5.40, 5.50)]
        emit("   Fuchs-form deep fit (%s):" % name)
        emit("     " + "   ".join(preds))
    emit()
    # comparator (prior-art 7.1/7.2 anchors: c=11 -> 1e-49, c=100 -> 1e-530,
    # slope 4pi nats per unit c = e^{L/2}, log-correction from the two anchors)
    emit("== Connes/Groskin comparator (calibrated on the 7.1/7.2 anchors) ==")
    lge = math.log10(math.e)
    beta = (530.0 - 49.0 - (100 - 11) * FOURPI * lge) / math.log10(100 / 11)
    gam = 49.0 - FOURPI * lge * 11 - beta * math.log10(11)
    emit("   log10 lam = -(%.4f c %+.3f log10 c %+.3f),  c = e^{L/2}"
         % (FOURPI * lge, beta, gam))
    for L in (4.796, 5.00, 5.13, 5.30, 5.50, 5.545):
        c = math.exp(L / 2)
        emit("   L=%.3f (c=%6.3f): comparator 1e%+.1f" %
             (L, c, -(FOURPI * lge * c + beta * math.log10(c) + gam)))
    with open(os.path.join(HERE, "fit_report.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
