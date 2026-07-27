#!/usr/bin/env python3
"""R2.6 authorized follow-on rung: L = 5.50, m = 224, dps 100/90.

Identical protocol to run_rung_5p50_m208.py (unchanged instrument math;
4-way additive split of the u-quadrature; exact _mpf_-tuple exchange).
Gates: G1 serial anchor; G2 parallel-vs-serial on anchor config;
G3 monotonicity lam(224) <= lam(208) = 4.21478011593e-71.

Scoring: the pre-registered R2.6 ratchet policy (SEAT-riemann-hilbert.md),
r := lam(224)/lam(208):
  lam < 1.5e-74                    -> BOTH-DEAD
  lam < 1.0e-73                    -> MINE-DEAD (retractions execute)
  lam >= 1.0e-73 and 0.15<=r<=0.6  -> FLATTENING-ONSET: m=240 + Aitken endgame
  1.0e-73 <= lam <= 3e-73, r<0.15  -> MINE-DISFAVORED pending m=240
  lam > 3e-73 and r < 0.15         -> STILL-PLUNGING: m=240 then HARD STOP
"""
import os
import sys
import time
import json
import pickle

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "..", "src"))
sys.path.insert(0, SRC)

import mpmath as mp                                             # noqa: E402
from spectral_margins import spectral_form, spectral_lam_min    # noqa: E402
from run_rung_5p50_m208 import parallel_form, log               # noqa: E402

L_RUN, M_RUN, DPS_A, DPS_S = 5.50, 224, 100, 90
LAM_208 = mp.mpf('4.21478011593e-71')
CSV = os.path.join(HERE, "rungs.csv")


def main():
    t_start = time.time()
    log(f"rung runner start: L={L_RUN} m={M_RUN} dps={DPS_A}/{DPS_S} NW=4")

    # G1 serial anchor
    t0 = time.time()
    Qa = spectral_form(2.485, 24, dps=50)
    lam_a = spectral_lam_min(Qa, nev=1, dps=40)[0]
    s = mp.nstr(lam_a, 8)
    log(f"G1 serial anchor lam = {s} ({time.time() - t0:.1f}s)")
    if s != '3.8688156e-10':
        log("G1 FAIL - aborting");  sys.exit(1)
    log("G1 PASS")

    # G2 parallel assembler vs serial on anchor config
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

    # the rung
    log("assembly start (384-pt GL rule; ~40-55 min at 4 workers)")
    t0 = time.time()
    Q = parallel_form(L_RUN, M_RUN, DPS_A)
    t1 = time.time()
    log(f"assembly done in {t1 - t0:.1f}s; checkpointing Q")
    with open(os.path.join(HERE, "Q_5p50_m224.pkl"), "wb") as f:
        pickle.dump([[Q[k, j]._mpf_ for j in range(M_RUN)]
                     for k in range(M_RUN)], f)
    lams = spectral_lam_min(Q, nev=3, dps=DPS_S)
    t2 = time.time()
    lam = lams[0]
    log(f"lam_min = {mp.nstr(lam, 12)} (bottom 3: "
        f"{[mp.nstr(x, 8) for x in lams]}); solve {t2 - t1:.1f}s")

    # G3 + ratchet scoring
    mono = lam <= LAM_208
    log(f"G3 monotonicity lam(224) <= lam(208): {'PASS' if mono else 'FAIL'}")
    r = lam / LAM_208
    log10lam = mp.log(lam, 10)
    log(f"log10 lam = {mp.nstr(log10lam, 6)}; r = lam(224)/lam(208) = "
        f"{mp.nstr(r, 4)}")
    if lam < mp.mpf('1.5e-74'):
        verdict = "BOTH-DEAD"
    elif lam < mp.mpf('1.0e-73'):
        verdict = "MINE-DEAD (retractions execute: A'=16.75 + both quarantined items)"
    elif r >= mp.mpf('0.15') and r <= mp.mpf('0.6'):
        verdict = "FLATTENING-ONSET (m=240 + completed-triple Aitken = endgame)"
    elif lam <= mp.mpf('3e-73'):
        verdict = "MINE-DISFAVORED pending m=240 (plunging inside my limit band)"
    else:
        verdict = "STILL-PLUNGING (m=240 authorized, then HARD STOP)"
    log(f"VERDICT vs R2.6 ratchet policy: {verdict}")

    stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(CSV, "a") as f:
        f.write(f"{L_RUN},{M_RUN},{DPS_A},{DPS_S},{mp.nstr(lam, 12)},"
                f"{t1 - t0:.1f},{t2 - t1:.1f},{t2 - t0:.1f},{stamp},"
                f"r2-ratchet-4w\n")
    with open(os.path.join(HERE, "rung_5p50_m224.json"), "w") as f:
        json.dump(dict(L=L_RUN, m=M_RUN, dps=[DPS_A, DPS_S],
                       lam_min=mp.nstr(lam, 12),
                       bottom3=[mp.nstr(x, 10) for x in lams],
                       log10lam=float(log10lam),
                       ratio_to_m208=float(r),
                       gates=dict(G1="PASS", G2="PASS",
                                  G3="PASS" if mono else "FAIL"),
                       verdict=verdict,
                       assembly_s=round(t1 - t0, 1),
                       solve_s=round(t2 - t1, 1),
                       total_s=round(time.time() - t_start, 1),
                       workers=4, finished_utc=stamp), f, indent=1)
    log(f"done; total wall {time.time() - t_start:.1f}s")


if __name__ == "__main__":
    main()
