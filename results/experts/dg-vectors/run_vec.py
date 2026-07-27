#!/usr/bin/env python3
"""DG Round-3 vector extraction worker.

Usage: python3 run_vec.py IDX
Assembles the truncated Weil form via src/spectral_margins.spectral_form
(unmodified), solves for the bottom eigenpairs (mp.eigsy via spectral_lam_min,
vectors=True), saves the minimizer vector, and evaluates the transform envelope
ln|phihat(T)| on the pre-registered grid. Outputs per config:
  vec_<tag>.txt   minimizer coefficients (50 sig digits per line)
  env_<tag>.csv   u, x=u-ell, lnF (floats)
  meta_<tag>.json lambdas, timings, norms, tail diagnostics
"""
import sys, os, json, time

sys.path.insert(0, '/home/ubuntu/Projects/Riemann-Zeta/src')
OUT = '/home/ubuntu/Projects/Riemann-Zeta/results/experts/dg-vectors'

import mpmath as mp

# (L, m, dps_asm, dps_solve, dps_eval)
CONFIGS = [
    ('4.50',  160, 75, 65, 50),   # 0 primary deep
    ('4.75',  160, 75, 65, 50),   # 1 primary deep
    ('4.50',  144, 75, 65, 50),   # 2 m-stability rung
    ('4.75',  144, 75, 65, 50),   # 3 m-stability rung
    ('3.555', 112, 50, 40, 40),   # 4 null control
    ('3.555', 128, 50, 40, 40),   # 5 control m-rung
    ('2.485',  24, 50, 40, 40),   # 6 smoke test (not a decision input)
]


def main(idx):
    Ls, m, dpsa, dpss, dpse = CONFIGS[idx]
    L = float(Ls)
    tag = "L%s_m%d" % (Ls, m)
    log = open("%s/logs/%s.log" % (OUT, tag), 'w', buffering=1)
    log.write("start %s  dps %d/%d/%d\n" % (time.strftime('%FT%TZ', time.gmtime()), dpsa, dpss, dpse))

    mp.mp.dps = dpsa
    import spectral_margins as sm

    t0 = time.time()
    Q = sm.spectral_form(L, m, dps=dpsa)
    t_asm = time.time() - t0
    log.write("assembled in %.1f s\n" % t_asm)

    t0 = time.time()
    lams, vecs = sm.spectral_lam_min(Q, nev=3, dps=dpss, vectors=True)
    t_solve = time.time() - t0
    log.write("solved in %.1f s  lam1 = %s\n" % (t_solve, mp.nstr(lams[0], 12)))

    c = vecs[0]
    with open("%s/vec_%s.txt" % (OUT, tag), 'w') as f:
        for x in c:
            f.write(mp.nstr(x, 50) + "\n")

    with mp.workdps(dpss):
        nrm = mp.sqrt(mp.fsum(ck * ck for ck in c))
        tail = mp.fsum(c[k] * c[k] for k in range(max(0, m - 16), m))

    # ---- envelope on the pre-registered grid ----
    t0 = time.time()
    with mp.workdps(dpse):
        a = mp.mpf(Ls) / 4
        ell = mp.mpf(Ls) / 2
        nodes = sm.gl_nodes(768)
        nk = [mp.sqrt(mp.mpf(2 * k + 1) / (2 * a)) for k in range(m)]
        xs, wts, phis = [], [], []
        for x_, w_ in nodes:
            B = sm.legvals(m, x_)
            phi = mp.fsum(c[k] * nk[k] * B[k] for k in range(m))
            xs.append(a * x_)
            wts.append(w_ * a)
            phis.append(phi)
        wphi = [wts[i] * phis[i] for i in range(len(xs))]
        npts = 1600
        lo = ell - mp.mpf('0.15')
        span = mp.mpf('1.60')
        rows = []
        for i in range(npts):
            u = lo + span * i / (npts - 1)
            T = 2 * mp.pi * mp.e ** u
            re = mp.fsum(wphi[j] * mp.cos(T * xs[j]) for j in range(len(xs)))
            im = mp.fsum(wphi[j] * mp.sin(T * xs[j]) for j in range(len(xs)))
            mag2 = re * re + im * im
            lnF = mp.log(mag2) / 2 if mag2 > 0 else mp.mpf(-9999)
            rows.append((float(u), float(u - ell), float(lnF)))
            if i % 200 == 0:
                log.write("  env %d/%d\n" % (i, npts))
    t_env = time.time() - t0

    with open("%s/env_%s.csv" % (OUT, tag), 'w') as f:
        f.write("u,x,lnF\n")
        for r in rows:
            f.write("%.10f,%.10f,%.10f\n" % r)

    meta = dict(tag=tag, L=Ls, m=m, dps=[dpsa, dpss, dpse],
                lam=[mp.nstr(l, 12) for l in lams],
                lam_ratio_21=mp.nstr(lams[1] / lams[0], 6),
                norm_c=mp.nstr(nrm, 12), tail16=mp.nstr(tail, 6),
                t_asm=round(t_asm, 1), t_solve=round(t_solve, 1),
                t_env=round(t_env, 1),
                finished=time.strftime('%FT%TZ', time.gmtime()))
    with open("%s/meta_%s.json" % (OUT, tag), 'w') as f:
        json.dump(meta, f, indent=1)
    log.write("done %s\n" % meta['finished'])
    log.close()


if __name__ == '__main__':
    main(int(sys.argv[1]))
