#!/usr/bin/env python3
"""DG Round-3 analyzer — applies PREREGISTRATION.md estimators verbatim.

Reads env_<tag>.csv + meta_<tag>.json and prints, per configuration:
  lam reproduction, ref/floor, w_E1, w_E2 (A=11.5, band 11.1..11.9),
  node census, x_nodes, S0 tail, y(x) groups, M0/M1 fits + F-test,
  beyond-edge tail exponent.
Cross-config: node-edge shifts, graded-activity ratio G, decision gates.
"""
import json, math, os, sys
import mpmath as mp

OUT = os.path.dirname(os.path.abspath(__file__))

RUNSCSV = {  # reproduction targets (runs.csv, deep-windows agent)
    'L4.50_m160': 7.92448858514e-41,
    'L4.75_m160': 1.86366090828e-47,
    'L4.50_m144': 8.13421925362e-41,
    'L4.75_m144': 2.04044762883e-47,
    'L3.555_m112': 2.12668062431e-22,
    'L3.555_m128': None,           # new rung
    'L2.485_m24': 3.8688156e-10,   # smoke
}


def load(tag):
    meta = json.load(open('%s/meta_%s.json' % (OUT, tag)))
    rows = []
    with open('%s/env_%s.csv' % (OUT, tag)) as f:
        next(f)
        for line in f:
            u, x, lnF = map(float, line.strip().split(','))
            rows.append((u, x, lnF))
    return meta, rows


def envelope_maxima(rows):
    mx = []
    for i in range(1, len(rows) - 1):
        if rows[i][2] > rows[i - 1][2] and rows[i][2] > rows[i + 1][2]:
            mx.append(rows[i])
    return mx


def nodes_list(rows, mxs):
    """Strict local minima with contrast >= 3 nats below mean of adjacent envelope maxima."""
    nds = []
    mus = [m[0] for m in mxs]
    import bisect
    for i in range(1, len(rows) - 1):
        if rows[i][2] < rows[i - 1][2] and rows[i][2] < rows[i + 1][2]:
            u = rows[i][0]
            j = bisect.bisect_left(mus, u)
            if j == 0 or j >= len(mus):
                continue
            envm = 0.5 * (mxs[j - 1][2] + mxs[j][2])
            if envm - rows[i][2] >= 3.0:
                nds.append((u, rows[i][1], rows[i][2], envm - rows[i][2]))
    return nds


def zeta_zeros(kmax=140):
    """True ordinates gamma_1..gamma_kmax, cached to zeros.txt (dps 15)."""
    path = os.path.join(OUT, 'zeros.txt')
    zs = []
    if os.path.exists(path):
        zs = [float(l) for l in open(path) if l.strip()]
    if len(zs) < kmax:
        with mp.workdps(15):
            for k in range(len(zs) + 1, kmax + 1):
                zs.append(float(mp.zetazero(k).imag))
        with open(path, 'w') as f:
            for g in zs:
                f.write('%.10f\n' % g)
    return zs


def dodge_estimators(nds, ell, a):
    """AMENDMENT-1 estimators. nds: nodes (u, x, lnF, contrast), sorted in u.
    Returns (x_dodge, x_spacing, d_list). Alignment vs true zeros; prefix rule."""
    import bisect
    zs = zeta_zeros()
    above = [n for n in nds if n[0] > ell]
    if not above:
        return None, None, []
    d_list = []
    for n in above:
        T = 2 * math.pi * math.exp(n[0])
        j = bisect.bisect_left(zs, T)
        cand = [abs(T - zs[i]) for i in (j - 1, j) if 0 <= i < len(zs)]
        spacing = 2 * math.pi / math.log(T / (2 * math.pi))
        d_list.append((n[1], min(cand) / spacing if cand else float('inf')))
    x_dodge = None
    for x, d in d_list:
        if d <= 0.15:                     # AMENDMENT-1b threshold
            x_dodge = x
        else:
            break
    # spacing cross-check: per-gap nearest-model classification against the
    # ACTUAL nearest-zero gap (low-T zero gaps fluctuate around the smooth mean)
    import bisect as _b
    x_spacing = above[0][1]
    sinc = math.pi / a
    prev_T = 2 * math.pi * math.exp(above[0][0])
    for n in above[1:]:
        T = 2 * math.pi * math.exp(n[0])
        dT = T - prev_T
        def _near(t):
            j = _b.bisect_left(zs, t)
            cand = [zs[i] for i in (j - 1, j) if 0 <= i < len(zs)]
            return min(cand, key=lambda g: abs(g - t)) if cand else None
        g1, g2 = _near(prev_T), _near(T)
        if g1 is None or g2 is None or g1 == g2:
            break
        stair = abs(g2 - g1)
        if abs(dT - stair) <= abs(dT - sinc):
            x_spacing = n[1]
            prev_T = T
        else:
            break
    return x_dodge, x_spacing, d_list


def wE2(lam, L, A=11.5):
    ell = L / 2.0
    Tst = 2 * math.pi * math.exp(ell)
    E = -math.log(lam)
    rhs = (E + A) / Tst - 1.0
    w = mp.findroot(lambda W: mp.e ** W * (W - 1) - rhs, 1.2)
    return float(w)


def twoA(x, L):
    ell = L / 2.0
    Tst = 2 * math.pi * math.exp(ell)
    return Tst * (math.exp(x) * (x - 1) + 1)


def fpval(F, d1, d2):
    if F <= 0:
        return 1.0
    x = d2 / (d2 + d1 * F)
    return float(mp.betainc(d2 / 2.0, d1 / 2.0, 0, x, regularized=True))


def analyze(tag, verbose=True):
    meta, rows = load(tag)
    L = float(meta['L'])
    m = meta['m']
    ell = L / 2.0
    lam = float(mp.mpf(meta['lam'][0]))
    res = {'tag': tag, 'L': L, 'm': m, 'lam': lam}

    # C1 gate pieces
    target = RUNSCSV.get(tag)
    res['lam_dev'] = abs(lam / target - 1) if target else None
    res['gap21'] = float(mp.mpf(meta['lam_ratio_21']))
    res['norm_c'] = float(mp.mpf(meta['norm_c']))
    res['tail16'] = float(mp.mpf(meta['tail16']))

    mxs = envelope_maxima(rows)
    ref = max(r[2] for r in rows if abs(r[0] - ell) <= 0.1)
    emax = [(u, x, lnF - ref) for (u, x, lnF) in mxs]
    # floor and w_E1 on the envelope-maxima series (Round-2 definition)
    above = [e for e in emax if e[0] >= ell]
    floor = min(e[2] for e in above)
    res['ref'] = ref
    res['floor'] = floor
    wE1 = None
    for e in above:
        if e[2] <= floor + 1.0:
            wE1 = e[1]
            break
    res['w_E1'] = wE1
    res['w_E2'] = wE2(lam, L)
    res['w_E2_band'] = (wE2(lam, L, 11.1), wE2(lam, L, 11.9))

    nds = nodes_list(rows, mxs)
    nda = [n for n in nds if n[0] > ell]
    res['x_lastnode'] = max(n[1] for n in nda) if nda else None   # degenerate; record only
    res['n_nodes_above'] = len(nda)
    res['n_nodes_total'] = len(nds)
    a_half = L / 4.0
    xd, xs_, dlist = dodge_estimators(nds, ell, a_half)
    res['x_dodge'] = xd
    res['x_spacing'] = xs_
    res['d_list'] = dlist
    res['x_nodes'] = xd   # AMENDMENT-1: all downstream rules use x_dodge

    # y(x) groups
    sel = [e for e in emax if e[2] > floor + 2.0 and e[1] >= 0.20]
    groups = []
    for i in range(0, len(sel) - 4, 5):
        g = sel[i:i + 5]
        span = g[-1][0] - g[0][0]
        if span > 0.12:
            continue
        n = len(g)
        su = sum(p[0] for p in g); se = sum(p[2] for p in g)
        suu = sum(p[0] * p[0] for p in g); sue = sum(p[0] * p[2] for p in g)
        det = n * suu - su * su
        if det == 0:
            continue
        slope = (n * sue - su * se) / det
        uc = su / n
        y = -slope / (2 * math.pi * math.exp(uc))
        groups.append((uc - ell, y))
    res['groups_all'] = groups

    xcap = (res['x_nodes'] - 0.05) if res['x_nodes'] else None
    fitg = [g for g in groups if xcap is None or g[0] <= xcap]
    res['n_fit'] = len(fitg)
    if len(fitg) >= 4:
        sxx = sum(x * x for x, y in fitg)
        sxy = sum(x * y for x, y in fitg)
        b0 = sxy / sxx
        rss0 = sum((y - b0 * x) ** 2 for x, y in fitg)
        res['beta0'] = b0
        res['rss0'] = rss0
        # M1: continuous 2-segment through origin
        best = None
        xs = sorted(x for x, y in fitg)
        for k in range(3, len(fitg) - 2):
            xb = xs[k]
            # design: f1 = min(x, xb), f2 = max(0, x - xb)
            a11 = a12 = a22 = r1 = r2 = 0.0
            for x, y in fitg:
                f1 = min(x, xb); f2 = max(0.0, x - xb)
                a11 += f1 * f1; a12 += f1 * f2; a22 += f2 * f2
                r1 += f1 * y; r2 += f2 * y
            det = a11 * a22 - a12 * a12
            if abs(det) < 1e-30:
                continue
            c1 = (a22 * r1 - a12 * r2) / det
            c2 = (a11 * r2 - a12 * r1) / det
            rss = sum((y - c1 * min(x, xb) - c2 * max(0.0, x - xb)) ** 2
                      for x, y in fitg)
            if best is None or rss < best[0]:
                best = (rss, xb, c1, c2)
        if best:
            rss1, xb, c1, c2 = best
            n = len(fitg)
            F = ((rss0 - rss1) / 2.0) / (rss1 / (n - 3)) if rss1 > 0 else float('inf')
            res['break'] = dict(x_b=xb, beta_pre=c1, beta_post=c2,
                                F=F, p=fpval(F, 2, n - 3))
    # beyond-edge tail exponent on grid lnF vs u
    if res['x_nodes']:
        seg = [(u, lnF) for (u, x, lnF) in rows
               if res['x_nodes'] + 0.10 <= x <= res['x_nodes'] + 0.35]
        if len(seg) > 10:
            n = len(seg)
            su = sum(s[0] for s in seg); se = sum(s[1] for s in seg)
            suu = sum(s[0] ** 2 for s in seg); sue = sum(s[0] * s[1] for s in seg)
            res['p_tail'] = -(n * sue - su * se) / (n * suu - su * su)

    if verbose:
        print("== %s ==" % tag)
        print(" lam = %.6e   dev vs runs.csv = %s   gap21 = %.3g  tail16 = %.2e"
              % (lam, ("%.2e" % res['lam_dev']) if res['lam_dev'] is not None else "n/a",
                 res['gap21'], res['tail16']))
        print(" ref = %.3f  floor(rel) = %.2f   w_E1 = %s   w_E2 = %.4f  [%.4f, %.4f]"
              % (ref, floor, ("%.3f" % wE1) if wE1 else "n/a",
                 res['w_E2'], res['w_E2_band'][1], res['w_E2_band'][0]))
        print(" nodes above T*: %d (last raw node x = %s)"
              % (res['n_nodes_above'],
                 ("%.3f" % res['x_lastnode']) if res['x_lastnode'] else "n/a"))
        print(" x_dodge = %s   x_spacing = %s   (agreement flag: %s)"
              % (("%.4f" % res['x_dodge']) if res['x_dodge'] else "n/a",
                 ("%.4f" % res['x_spacing']) if res['x_spacing'] else "n/a",
                 "OK" if (res['x_dodge'] and res['x_spacing'] and
                          abs(res['x_dodge'] - res['x_spacing']) <= 0.08)
                 else "DISAGREE"))
        if res['d_list']:
            head = "  ".join("%.2f:%.2f" % (x, d) for x, d in res['d_list'][:14])
            print(" node alignment d (x:d) = %s%s"
                  % (head, " ..." if len(res['d_list']) > 14 else ""))
        if 'beta0' in res:
            print(" y(x) fit zone: n = %d groups (x <= %.3f)   beta0 = %.4f"
                  % (res['n_fit'], xcap, res['beta0']))
            if 'break' in res:
                b = res['break']
                print("   break: x_b = %.3f  slopes %.3f -> %.3f   F = %.2f  p = %.4g"
                      % (b['x_b'], b['beta_pre'], b['beta_post'], b['F'], b['p']))
        if 'p_tail' in res:
            print(" beyond-edge tail exponent p_tail = %.1f" % res['p_tail'])
        print()
    return res


def cross(tags):
    R = {t: analyze(t) for t in tags}
    print("==== cross-config (pre-registered discriminators) ====")
    for L, t160, t144 in (('4.50', 'L4.50_m160', 'L4.50_m144'),
                          ('4.75', 'L4.75_m160', 'L4.75_m144')):
        if t160 in R and t144 in R and R[t160]['x_nodes'] and R[t144]['x_nodes']:
            a, b = R[t160], R[t144]
            dx = a['x_nodes'] - b['x_nodes']
            d2A = twoA(a['x_nodes'], float(L)) - twoA(b['x_nodes'], float(L))
            dln = math.log(b['lam']) - math.log(a['lam'])
            G = dln / d2A if d2A != 0 else float('nan')
            print(" L=%s: x_nodes 144->160: %.4f -> %.4f (shift %.4f; tracking=0.105)"
                  % (L, b['x_nodes'], a['x_nodes'], dx))
            print("        dln lam = %.5f   d2A(x_nodes) = %.3f   G = %.4f" % (dln, d2A, G))
    if 'L3.555_m112' in R and 'L3.555_m128' in R:
        a, b = R['L3.555_m128'], R['L3.555_m112']
        if a['x_nodes'] and b['x_nodes']:
            print(" control 3.555: x_nodes 112->128: %.4f -> %.4f (shift %.4f; tracking=0.134)"
                  % (b['x_nodes'], a['x_nodes'], a['x_nodes'] - b['x_nodes']))


if __name__ == '__main__':
    tags = sys.argv[1:]
    if not tags:
        tags = [f[4:-5] for f in sorted(os.listdir(OUT))
                if f.startswith('meta_') and f.endswith('.json')]
    if len(tags) == 1:
        analyze(tags[0])
    else:
        cross(tags)
