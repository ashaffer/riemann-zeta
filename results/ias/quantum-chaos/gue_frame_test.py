"""gue_frame_test.py — pre-registered GUE rung of the rigidity ladder.

Seat: quantum-chaos (IAS panel round 1). Protocol and predictions pre-registered
in results/ias/SEAT-quantum-chaos.md §5 BEFORE this script was run.

Configuration matches the recorded mechanism experiment (results/RESULTS.md,
model_zeros): L = 2.485, m = 48, dps 50, K = 180 ordinates.
Recorded anchors at this configuration:
  true    2.68972e-10   smooth  2.75124e-10   poisson 2.89509e-12

GUE model: CUE eigenangles (dim 256, Mezzadri QR recipe), sorted, unfolded to
unit density, anchored x_k = u_k - u_1 + 1/2, k = 1..180, mapped through the
same N_smooth^{-1} as the repo's Poisson model. Seeds 1, 2, 3.

Run from repo root:  python3 results/ias/quantum-chaos/gue_frame_test.py
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "..", "src"))
import numpy as np
import mpmath as mp
from model_zeros import smooth_zeros, frame_form
from spectral_margins import spectral_lam_min

L, M, K, DPS = 2.485, 48, 180, 50
mp.mp.dps = DPS


def n_smooth_inverse(x):
    """Solve N_smooth(g) = x, i.e. (g/2pi) ln(g/2pi e) = x - 7/8 (same Newton
    iteration as model_zeros.poisson_zeros)."""
    g = mp.mpf(14)
    target = mp.mpf(x) - mp.mpf('0.875')
    for _ in range(60):
        f = g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) - target
        fp = mp.log(g / (2 * mp.pi)) / (2 * mp.pi)
        step = f / fp
        g = g - step
        if abs(step) < mp.mpf('1e-30'):
            break
    return +g


def cue_unfolded(dim, seed):
    """Sorted unit-density positions of CUE(dim) eigenangles (Mezzadri 2007)."""
    rng = np.random.default_rng(seed)
    A = (rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim)))
    A /= np.sqrt(2.0)
    Q, R = np.linalg.qr(A)
    d = np.diagonal(R)
    Q = Q * (d / np.abs(d))
    theta = np.sort(np.angle(np.linalg.eigvals(Q)))       # in (-pi, pi]
    u = (theta + np.pi) * dim / (2 * np.pi)               # unit mean density
    return u


def gue_zeros(K, seed):
    u = cue_unfolded(256, seed)
    x = u - u[0] + 0.5                                     # anchor x_1 = 1/2
    return [n_smooth_inverse(float(xi)) for xi in x[:K]]


def lam_of(gammas, tag):
    t0 = time.time()
    Q = frame_form(gammas, L, M, dps=DPS)
    lam = spectral_lam_min(Q, nev=1)[0]
    print("%-10s lam_min = %s   ln lam = %+.4f   (%.0f s)"
          % (tag, mp.nstr(lam, 6), float(mp.log(lam)), time.time() - t0),
          flush=True)
    return lam


if __name__ == "__main__":
    print("config: L=%.3f m=%d K=%d dps=%d" % (L, M, K, DPS), flush=True)
    print("recorded anchors: true 2.68972e-10 | smooth 2.75124e-10 | "
          "poisson 2.89509e-12", flush=True)
    # harness validation: recompute the smooth anchor
    lam_sm = lam_of(smooth_zeros(K), "smooth")
    ln_sm = float(mp.log(lam_sm))
    ln_po = float(mp.log(mp.mpf('2.89509e-12')))
    results = []
    for seed in (1, 2, 3):
        gz = gue_zeros(K, seed)
        # discrepancy diagnostic: sup |N_gue - N_smooth| over the block
        # (levels of both sit at x = k - 1/2 mean positions; discrepancy in
        # level index units = max |x_k^gue - (k - 1/2)|)
        u = cue_unfolded(256, seed)
        x = u - u[0] + 0.5
        disc = float(np.max(np.abs(x[:K] - (np.arange(1, K + 1) - 0.5))))
        lam = lam_of(gz, "GUE s%d" % seed)
        results.append((seed, lam, disc))
    print("\n--- summary (Delta = ln lam_GUE - ln lam_smooth, nats) ---",
          flush=True)
    lns = []
    for seed, lam, disc in results:
        ln_g = float(mp.log(lam))
        lns.append(ln_g)
        print("seed %d: lam = %s  Delta = %+0.3f  dist-to-poisson = %0.3f  "
              "sup-discrepancy = %0.2f"
              % (seed, mp.nstr(lam, 6), ln_g - ln_sm, ln_g - ln_po, disc),
              flush=True)
    lns.sort()
    med = lns[1]
    print("median Delta = %+0.3f | ratio |D_smooth|/|D_poisson| = %0.3f | "
          "spread = %0.3f nats"
          % (med - ln_sm,
             abs(med - ln_sm) / abs(med - ln_po),
             lns[-1] - lns[0]), flush=True)
