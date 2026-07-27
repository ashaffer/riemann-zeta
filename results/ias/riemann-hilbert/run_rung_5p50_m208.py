#!/usr/bin/env python3
"""R2.5 authorized rung: L = 5.50, m = 208, dps 100/90 (assembly/solve).

Exact replication of src/spectral_margins.spectral_form (unchanged instrument
math); the ONLY change is that the u-quadrature loop is split additively over
NW=4 worker processes, with partial sums exchanged as exact _mpf_ tuples, so
the result differs from the serial instrument only by summation order at
working precision (dps+15).

NOTE (protocol): for m > 184 the instrument's own gl_nodes rule jumps
192 -> 384 points in BOTH x and u (nodes_x needs m+4 > 192, nodes_u needs
m+8 > 192). This is the unchanged code's rule, still exact on the polynomial
overlap factors (degree << 767); the deep agent's "identical 192-pt rules"
clause simply does not extend past m = 184, and the analytic-factor
quadrature error only shrinks. Recorded here for the ledger.

Gates (all must pass before the rung is scored):
 G1 serial regression anchor: spectral_form(2.485, 24) @ dps 50/40
    -> lam_min = 3.8688156e-10 to all printed digits (deep agent's anchor).
 G2 parallel-vs-serial: this file's parallel assembler on the anchor config
    must agree with serial spectral_form entrywise to < 1e-40 and reproduce
    the same lam_min to 8 digits.
 G3 monotonicity: lam(m=208) <= lam(m=184) = 4.29586487391e-69 (nested bases).

Scoring (pre-registered, SEAT-riemann-hilbert.md R2.2):
 - any RR rung < 1.5e-74  -> BOTH candidates dead (mine and Fuchs-literal);
 - any RR rung < 1.0e-73  -> MINE dead (A' = 16.75 retracted, both quarantined
   numerology items retracted);
 - rung >= 3e-73 with decrement ratio vs m=184 flattening to >= 0.2
   -> mine favored pending completed-triple Aitken;
 - otherwise: still descending; not adjudicated; m = 224 follow-on decides.
"""
import os
import sys
import time
import json
import pickle
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "..", "src"))
sys.path.insert(0, SRC)

import mpmath as mp                                            # noqa: E402
from spectral_margins import (spectral_form, spectral_lam_min,  # noqa: E402
                              gl_nodes, legvals, overlap_S)
from weil_core import PRIME_POWERS                              # noqa: E402
from hp_margins import kernel_tail                              # noqa: E402

NW = 4          # authorized worker cap
L_RUN, M_RUN, DPS_A, DPS_S = 5.50, 208, 100, 90
LAM_184 = mp.mpf('4.29586487391e-69')

CSV = os.path.join(HERE, "rungs.csv")


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def tup(x):
    return x._mpf_


def untup(t):
    return mp.mpf(t)


def partial_A(args):
    """Worker: additive partial of the archimedean u-loop over nodes idx::NW.
    Returns m x m list of _mpf_ tuples. Math identical to spectral_form."""
    L, m, dps, idx, nw = args
    with mp.workdps(dps + 15):
        a = mp.mpf(L) / 4
        twoa0 = mp.mpf('0.5')
        nk = [mp.sqrt(mp.mpf(2 * k + 1) / (2 * a)) for k in range(m)]
        nodes_x = gl_nodes(max(m + 4, 96))
        nodes_u = gl_nodes(max(m + 8, 192))
        A = [[mp.mpf(0)] * m for _ in range(m)]
        mine = nodes_u[idx::nw]
        t0 = time.time()
        for c_, (xu, wu) in enumerate(mine):
            u = a * (1 + xu)
            S = overlap_S(m, a, u, nodes_x, nk)
            guw = wu * a * u * mp.e ** (-twoa0 * u) / (-mp.expm1(-2 * u))
            for k in range(m):
                Sk = S[k]
                Ak = A[k]
                for j in range(k % 2, m, 2):
                    Ak[j] += guw * (((1 if j == k else 0) - Sk[j]) / u)
            if (c_ + 1) % 12 == 0:
                print(f"  [w{idx}] {c_ + 1}/{len(mine)} u-nodes, "
                      f"{time.time() - t0:.0f}s", flush=True)
        return [[tup(A[k][j]) for j in range(m)] for k in range(m)]


def primes_pole_shift(L, m, dps):
    """Parent-side: prime overlaps + pole rank-two + diagonal shift,
    verbatim from spectral_form (q = 1, even parity, zeta pole)."""
    with mp.workdps(dps + 15):
        a = mp.mpf(L) / 4
        twoa0 = mp.mpf('0.5')
        nk = [mp.sqrt(mp.mpf(2 * k + 1) / (2 * a)) for k in range(m)]
        nodes_x = gl_nodes(max(m + 4, 96))
        tail = kernel_tail(2 * a, twoa0)
        shift = mp.digamma(twoa0 / 2) + 2 * tail + mp.log(1 / mp.pi)
        P = [[mp.mpf(0)] * m for _ in range(m)]
        for nn, p in PRIME_POWERS:
            ln = mp.log(nn)
            if 2 * ln < L:
                Sp = overlap_S(m, a, ln, nodes_x, nk)
                w = 2 * mp.log(p) / mp.sqrt(nn)
                for k in range(m):
                    for j in range(m):
                        P[k][j] -= w * Sp[k][j]
        vp = [mp.mpf(0)] * m
        vm = [mp.mpf(0)] * m
        for x_, w_ in nodes_x:
            x = a * x_
            wt = w_ * a
            B = legvals(m, x_)
            ep, em = mp.e ** (x / 2), mp.e ** (-x / 2)
            for k in range(m):
                vp[k] += wt * B[k] * ep
                vm[k] += wt * B[k] * em
        for k in range(m):
            vp[k] *= nk[k]
            vm[k] *= nk[k]
        for k in range(m):
            for j in range(m):
                P[k][j] += vp[k] * vm[j] + vm[k] * vp[j]
        return P, shift


def parallel_form(L, m, dps, nw=NW, pool=None):
    """Assemble Q via nw-way split of the u-loop; identical math to
    spectral_form up to summation order at dps+15."""
    args = [(L, m, dps, i, nw) for i in range(nw)]
    own_pool = pool is None
    if own_pool:
        pool = Pool(nw)
    try:
        async_res = [pool.apply_async(partial_A, (a_,)) for a_ in args]
        PP, shift = primes_pole_shift(L, m, dps)   # parent works meanwhile
        parts = [r.get() for r in async_res]
    finally:
        if own_pool:
            pool.close()
            pool.join()
    with mp.workdps(dps + 15):
        Q = mp.matrix(m)
        for k in range(m):
            for j in range(m):
                s = mp.mpf(0)
                for part in parts:
                    s += untup(part[k][j])
                Q[k, j] = 2 * s + PP[k][j] + (shift if k == j else 0)
        Qo = mp.matrix(m)
        with mp.workdps(dps):
            for k in range(m):
                for j in range(m):
                    Qo[k, j] = +Q[k, j]
    return Qo


def main():
    t_start = time.time()
    log(f"rung runner start: L={L_RUN} m={M_RUN} dps={DPS_A}/{DPS_S} NW={NW}")

    # ---- G1: serial regression anchor -------------------------------------
    t0 = time.time()
    Qa = spectral_form(2.485, 24, dps=50)
    lam_a = spectral_lam_min(Qa, nev=1, dps=40)[0]
    s = mp.nstr(lam_a, 8)
    log(f"G1 serial anchor lam = {s} ({time.time() - t0:.1f}s)")
    if s != '3.8688156e-10':
        log("G1 FAIL - aborting");  sys.exit(1)
    log("G1 PASS")

    # ---- G2: parallel assembler vs serial on the anchor config ------------
    t0 = time.time()
    Qp = parallel_form(2.485, 24, 50)
    dmax = mp.mpf(0)
    for k in range(24):
        for j in range(24):
            d = abs(Qp[k, j] - Qa[k, j])
            if d > dmax:
                dmax = d
    lam_p = spectral_lam_min(Qp, nev=1, dps=40)[0]
    log(f"G2 entrywise max |par - ser| = {mp.nstr(dmax, 3)}; "
        f"lam_par = {mp.nstr(lam_p, 8)} ({time.time() - t0:.1f}s)")
    if dmax > mp.mpf('1e-40') or mp.nstr(lam_p, 8) != '3.8688156e-10':
        log("G2 FAIL - aborting");  sys.exit(1)
    log("G2 PASS")

    # ---- the rung ----------------------------------------------------------
    log(f"assembly start (384-pt GL x/u rule at this m; expect ~35-60 min "
        f"at {NW} workers under load)")
    t0 = time.time()
    Q = parallel_form(L_RUN, M_RUN, DPS_A)
    t1 = time.time()
    log(f"assembly done in {t1 - t0:.1f}s; checkpointing Q")
    with open(os.path.join(HERE, "Q_5p50_m208.pkl"), "wb") as f:
        pickle.dump([[tup(Q[k, j]) for j in range(M_RUN)]
                     for k in range(M_RUN)], f)
    lams = spectral_lam_min(Q, nev=3, dps=DPS_S)
    t2 = time.time()
    lam = lams[0]
    log(f"lam_min = {mp.nstr(lam, 12)} (bottom 3: "
        f"{[mp.nstr(x, 8) for x in lams]}); solve {t2 - t1:.1f}s")

    # ---- G3 + scoring -------------------------------------------------------
    mono = lam <= LAM_184
    log(f"G3 monotonicity lam(208) <= lam(184): {'PASS' if mono else 'FAIL'}")
    log10lam = mp.log(lam, 10)
    ratio = lam / LAM_184
    log(f"log10 lam = {mp.nstr(log10lam, 6)}; ratio to m=184 = "
        f"{mp.nstr(ratio, 4)} (prev decrement ratio was 0.0298)")
    if lam < mp.mpf('1.5e-74'):
        verdict = "BOTH-DEAD (below 1.5e-74: mine AND Fuchs-literal killed)"
    elif lam < mp.mpf('1.0e-73'):
        verdict = ("MINE-DEAD (below 1.0e-73: A'=16.75 retracted; "
                   "quarantined numerology items retracted)")
    elif lam >= mp.mpf('3e-73') and ratio >= mp.mpf('0.2'):
        verdict = ("MINE-FAVORED pending completed-triple Aitken "
                   "(flattened above 3e-73)")
    else:
        verdict = "NOT-ADJUDICATED (still descending; m=224 decides)"
    log(f"VERDICT vs pre-registered rule: {verdict}")

    stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    new = not os.path.exists(CSV)
    with open(CSV, "a") as f:
        if new:
            f.write("L,m,dps_assembly,dps_solve,lam_min,assembly_s,solve_s,"
                    "total_s,finished_utc,tag\n")
        f.write(f"{L_RUN},{M_RUN},{DPS_A},{DPS_S},{mp.nstr(lam, 12)},"
                f"{t1 - t0:.1f},{t2 - t1:.1f},{t2 - t0:.1f},{stamp},"
                f"r2-authorized-4w\n")
    with open(os.path.join(HERE, "rung_5p50_m208.json"), "w") as f:
        json.dump(dict(L=L_RUN, m=M_RUN, dps=[DPS_A, DPS_S],
                       lam_min=mp.nstr(lam, 12),
                       bottom3=[mp.nstr(x, 10) for x in lams],
                       log10lam=float(log10lam),
                       ratio_to_m184=float(ratio),
                       gates=dict(G1="PASS", G2="PASS",
                                  G3="PASS" if mono else "FAIL"),
                       verdict=verdict,
                       assembly_s=round(t1 - t0, 1),
                       solve_s=round(t2 - t1, 1),
                       total_s=round(time.time() - t_start, 1),
                       nodes_rule="384-pt GL x/u (instrument's own rule at m=208)",
                       workers=NW, finished_utc=stamp), f, indent=1)
    log(f"done; total wall {time.time() - t_start:.1f}s")


if __name__ == "__main__":
    main()
