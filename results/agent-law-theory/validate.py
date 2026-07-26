"""validate.py — mandatory validation of the fast builder before any experiment.

V1: entrywise agreement of law_core.frame_blocks (exact Bessel) with
    src/model_zeros.frame_form (quadrature) on a small case.
V2: staircase_zeros(alpha=1,beta=1) == model_zeros.smooth_zeros.
V3: regression against EXPECTED (model_zeros.py, measured July 25 2026):
    L=2.485, m=48, Gcut=420: true 2.68972e-10, smooth 2.75124e-10.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src"))
import mpmath as mp
from law_core import frame_blocks, lam_min_frame, staircase_zeros, true_zeros_cached
from model_zeros import frame_form, smooth_zeros
from spectral_margins import spectral_lam_min

mp.mp.dps = 50

# ---- V1: entrywise, m=8, three frequencies
print("V1: entrywise fast-vs-quadrature, m=8, gammas=[14.1,21.0,25.0], L=2.485")
gs = [mp.mpf('14.134725'), mp.mpf('21.022040'), mp.mpf('25.010858')]
t0 = time.time()
Qq = frame_form(gs, 2.485, 8)
tq = time.time() - t0
t0 = time.time()
Qe, Qo = frame_blocks(gs, 2.485, 8)
tf = time.time() - t0
ke = [0, 2, 4, 6]; ko = [1, 3, 5, 7]
err = mp.mpf(0)
for i, ki in enumerate(ke):
    for j, kj in enumerate(ke):
        err = max(err, abs(Qe[i, j] - Qq[ki, kj]))
for i, ki in enumerate(ko):
    for j, kj in enumerate(ko):
        err = max(err, abs(Qo[i, j] - Qq[ki, kj]))
xpar = max(abs(Qq[i, j]) for i in ke for j in ko)
print("  max |fast - quad| = %s   cross-parity (must ~0) = %s   [quad %.1fs, fast %.2fs]"
      % (mp.nstr(err, 3), mp.nstr(xpar, 3), tq, tf))

# ---- V2: staircase generator vs repo generator
print("V2: staircase(alpha=beta=1) vs model_zeros.smooth_zeros, K=40")
a1 = staircase_zeros(40)
a2 = smooth_zeros(40)
d = max(abs(x - y) for x, y in zip(a1, a2))
print("  max diff = %s" % mp.nstr(d, 3))

# ---- V3: the EXPECTED regression numbers
print("V3: EXPECTED regression, L=2.485, m=48, Gcut=420")
t0 = time.time()
tz = true_zeros_cached(180)
print("  (zeros loaded/computed in %.0fs)" % (time.time() - t0))
gs420 = [g for g in tz if g <= 420]
t0 = time.time()
lam = lam_min_frame(gs420, 2.485, 48, dps=50)[0]
print("  true zeros  (%d): lam = %s  EXPECTED 2.68972e-10  (%.0fs)"
      % (len(gs420), mp.nstr(lam, 6), time.time() - t0))
sm = smooth_zeros(180)
sm420 = [g for g in sm if g <= 420]
t0 = time.time()
lam2 = lam_min_frame(sm420, 2.485, 48, dps=50)[0]
print("  smooth      (%d): lam = %s  EXPECTED 2.75124e-10  (%.0fs)"
      % (len(sm420), mp.nstr(lam2, 6), time.time() - t0))
