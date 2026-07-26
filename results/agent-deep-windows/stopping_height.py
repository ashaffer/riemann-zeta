"""stopping_height.py — scalar readouts of the C4/w(L) protocol
(PLAN-differential-geometry.md, Round 2 (c)) on the deep-windows ladders,
plus the HA Round-2 T1' two-horizon consistency test.

w_E2 (action matching, the protocol's PRIMARY estimator): solve
    T* (e^w (w-1) + 1) = E_m + A,   T* = 2 pi e^{L/2},  E_m = -ln lam_m,
with A = 11.5 and sensitivity band A in {11.1, 11.9} (protocol values).
Convergence gate (Step 5.1): |w_E2(m_top) - w_E2(m_prev)| <= 0.01.
Level test (Step 5.2): converged w_E2 >= 1.26 at L=4.75 AND 5.00 => B_abrupt;
w_E2 in [1.20, 1.25] => level-non-discriminating (drift vs smooth cap);
<= 1.18 => pipeline suspect.
T1' (PLAN-harmonic-analysis.md Round 2): every stopping height must lie
STRICTLY inside (e T*, e^2 T*), i.e. w in (1, 2); margins reported.
The SHAPE test (Step 5.3) needs the minimizer vectors' envelope — not
computable from eigenvalues; see the report.
"""
import csv
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
W_INF = 1.278464542761074   # root of e^w (w-1) = 1  <=>  slope cap 4 pi


def w_of(lam, L, A=11.5):
    E = -math.log(lam)
    rhs = (E + A) / (2 * math.pi * math.exp(L / 2)) - 1
    lo, hi = 0.0, 5.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if math.exp(mid) * (mid - 1) < rhs:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def load_ladders():
    lad = {}
    for fn in ("priors.csv", "runs.csv"):
        p = os.path.join(HERE, fn)
        if not os.path.exists(p):
            continue
        with open(p) as f:
            for r in csv.DictReader(f):
                lad.setdefault(float(r["L"]), []).append(
                    (int(r["m"]), float(r["lam_min"])))
    for L in lad:
        lad[L] = sorted(set(lad[L]))
    return lad


if __name__ == "__main__":
    lad = load_ladders()
    print("w_inf = %.6f (e^w(w-1)=1 <=> slope cap 4pi); horizons w=1 (eT*), "
          "w=2 (e^2 T*)" % W_INF)
    print("%-6s %-4s %-11s %-8s %-17s %-10s %-7s %s" % (
        "L", "m", "lam", "w_E2", "A-band", "gate", "T1'lo", "T1'hi"))
    for L in sorted(lad):
        rows = lad[L]
        for i, (m, lam) in enumerate(rows):
            w = w_of(lam, L)
            wlo, whi = w_of(lam, L, 11.1), w_of(lam, L, 11.9)
            gate = ""
            if i == len(rows) - 1 and len(rows) >= 2:
                dw = abs(w - w_of(rows[-2][1], L))
                gate = "PASS" if dw <= 0.01 else "FAIL(%.3f)" % dw
            print("%-6.3f %-4d %-11.3e %-8.4f [%.4f,%.4f]  %-10s %+.3f  %+.3f"
                  % (L, m, lam, w, wlo, whi, gate, w - 1, 2 - w))
