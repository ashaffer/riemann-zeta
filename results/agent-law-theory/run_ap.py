"""run_ap.py — RUN 2: arithmetic-progression frequencies (constant density).

gamma_k = s0 (k + 1/2), k = 0..; both signs enter through |phihat|^2.
Exact theory for the INFINITE system on [-a, a], a = L/4 (anti-periodization
/ Poisson summation, derived in the report):
  - s0 <  pi/a (oversampled): TIGHT frame, lam_inf = 2 pi / s0 exactly.
  - s0 >  pi/a (undersampled): lam_inf = 0 exactly (anti-periodization
    kernel: phi supported on two edge slivers of width s = 2a - 2pi/s0,
    equal up to sign pattern).  Any positive Galerkin value is then a pure
    basis artifact and must DECREASE in m without floor.
This is the constant-density calibration: it shows the per-zero suppression
cost of a strictly sub-Nyquist block is ZERO in the operator limit, i.e. the
zeta margin is entirely a variable-density (chirp) effect.
"""
import mpmath as mp
from law_core import ap_zeros
from runs import record

mp.mp.dps = 50
OUT = "ap.jsonl"

# L = 2.485: pi/a = 5.05674 ; L = 2.996: pi/a = 4.19467
GRID = [
    (2.485, [3.2, 4.0, 4.6, 4.9, 5.0567, 5.2, 5.5, 6.0, 7.0]),
    (2.996, [3.5, 4.0, 4.1947, 4.4, 5.0]),
]

for L, s0s in GRID:
    a = mp.mpf(L) / 4
    nyq = mp.pi / a
    for s0 in s0s:
        for (m, gcut) in ((32, 420), (48, 420), (64, 420), (48, 840), (64, 840)):
            gs = ap_zeros(s0, gcut)
            record(OUT, "ap", gs, L, m, dps=50,
                   extra={"Gcut": gcut, "s0": float(s0),
                          "s0_over_nyq": float(mp.mpf(s0) / nyq),
                          "pred_inf": (float(2 * mp.pi / mp.mpf(s0))
                                       if mp.mpf(s0) < nyq else 0.0)})
print("RUN 2 done", flush=True)
