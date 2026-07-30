"""model_zeros.py — is the envelope law pure density, or arithmetic?

Under RH (and with the usual explicit-formula hypotheses), the truncated Weil
form on test functions supported in [-L/4, L/4] equals
2 SUM_{gamma>0} |phihat(gamma)|^2.  This conditional identity motivates a
numerical frame-model experiment; it is not an unconditional certificate of
the form.  The module replaces numerically computed on-line ordinates by
controlled models with the same leading density:

  true    : numerical gamma_k from mp.zetazero
  smooth  : the Riemann-von Mangoldt staircase, N_smooth(gamma_k) = k - 1/2,
            N_smooth(T) = (T/2pi) ln(T/2pi e) + 7/8 — correct density, zero
            "statistics" (perfectly rigid, no arithmetic)
  poisson0: gamma_k = N_smooth^{-1}(P_k), the historical phase convention
  poisson½: gamma_k = N_smooth^{-1}(P_k - 1/2), phase-matched to the smooth
            staircase (both use one fixed Poisson seed)

Comparing these models probes how much of the finite-section decay is explained
by the leading counting density and how much is sensitive to phase, count
fluctuations, and local gaps.  It cannot by itself identify arithmetic content.
The true-zero model versus the spectral pipeline is also a numerical regression
check of the conditional frame identity.

Build: Q_model = 2 SUM_{gamma <= Gcut} (v_re v_re^T + v_im v_im^T) in the
orthonormal Legendre basis, v_j(gamma) = INT b_j e^{-i gamma x} dx by exact
Gauss-Legendre (the integrand is polynomial x trigonometric; GL at >= m+4
nodes is exact for the polynomial factor and spectrally accurate overall).
Truncating at Gcut only DELETES positive rank-ones: lam_model(Gcut) increases
to the full frame bound as Gcut grows; report the Gcut-escalation.

EXPECTED (remeasured July 27, 2026; m = 48, dps 50):
  validation, L = 2.485, true zeros, Gcut = 180/300/420 (69/138/215 zeros):
    1.10183e-10 -> 2.34606e-10 -> 2.88133e-10, rising toward the spectral-form
    value 3.59571e-10 from below (truncation only deletes positive rank-ones;
    the residual gap is the deleted tail's worth — the frame identity closes).
  at fixed Gcut = 420:                    true | smooth | poisson0 | poisson½
    L = 2.485:  2.88133e-10 | 2.95437e-10 | 3.04282e-12 | 1.89001e-10
    L = 2.996:  3.00206e-15 | 3.45419e-15 | 3.16094e-17 | 3.74208e-15
    L = 3.555:  1.06527e-21 | 1.77483e-22 | 9.58703e-23 | 1.78946e-20
  AUDIT READING (July 27): changing only the Poisson half-step phase changes
  the frame minimum by roughly two orders of magnitude and removes the claimed
  systematic "Poisson cost" at the first two L values.  The original rigidity/
  offset verdict is therefore withdrawn.  The phase-matched multi-seed check
  reported below tests whether the seed-7 comparison is representative.
  The earlier recorded seed-7 rows reproduce exactly when all four sequences
  are capped at K=180, but that cap supplied only 180 of about 215 model points
  below 420.  The values above use every generated point through the cutoff.
  ENSEMBLE AUDIT (July 27; seeds 0..15, phase=-1/2, Gcut=300, m=32):
    seeds 2,3,11 are rejected because their first target lies below the model
    minimum.  Across the 13 accepted seeds, log10(lambda_poisson/lambda_smooth)
    has min/Q1/median/Q3/max
      L=2.485: -7.782/-4.185/-2.904/-0.810/+4.765
      L=2.996: -5.668/-2.585/-1.992/+0.883/+6.291.
    Low/central/high representatives retain essentially the same log-ratios at
    Gcut=420, and the two extremes persist at m=48.  Thus phase matching alone
    does not produce a stable Poisson offset: finite-cutoff count fluctuations
    and extreme gaps dominate.  A sharper rigidity test must also match total
    count/weighted charge.  The accepted-seed summary is conditional because
    rejecting invalid first targets removes about 31% of unconditioned seeds.
  (Echoes the below-GUE small-gap counts of PROGRAM.md 2.1.)
"""
import numpy as np
import mpmath as mp
from spectral_margins import gl_nodes, legvals, spectral_lam_min


def smooth_zeros(K):
    """First K solutions of N_smooth(g) = k - 1/2."""
    out = []
    g = mp.mpf(14)
    for k in range(1, K + 1):
        target = k - mp.mpf('0.5') - mp.mpf('0.875')
        for _ in range(60):
            f = g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) - target
            fp = mp.log(g / (2 * mp.pi)) / (2 * mp.pi)
            step = f / fp
            g = g - step
            if abs(step) < mp.mpf('1e-30'):
                break
        out.append(+g)
        g = g + 2 * mp.pi / mp.log(g / (2 * mp.pi))
    return out


def poisson_zeros(K, seed=7, phase=0):
    """Push unit-rate Poisson arrivals through N_smooth(gamma)=P_k+phase.

    The historical experiment used ``phase=0``.  ``phase=-0.5`` aligns the
    mean kth arrival with ``smooth_zeros`` but can put the first target below
    the minimum of the smooth counting model for some seeds; such a seed is
    rejected explicitly rather than silently selecting a wrong Newton branch.
    """
    rng = np.random.default_rng(seed)
    arrivals = np.cumsum(rng.exponential(1.0, K))
    out = []
    g = mp.mpf(14)
    min_count = -mp.mpf('0.125')  # N_smooth has its minimum at gamma = 2*pi
    for x in arrivals:
        count_target = mp.mpf(float(x)) + mp.mpf(phase)
        if count_target < min_count:
            raise ValueError("Poisson phase puts a target below min N_smooth")
        target = count_target - mp.mpf('0.875')
        for _ in range(60):
            f = g / (2 * mp.pi) * mp.log(g / (2 * mp.pi * mp.e)) - target
            fp = mp.log(g / (2 * mp.pi)) / (2 * mp.pi)
            step = f / fp
            g = g - step
            if abs(step) < mp.mpf('1e-30'):
                break
        out.append(+g)
    return out


def smooth_count(T):
    """Leading Riemann--von Mangoldt staircase used by the model."""
    T = mp.mpf(T)
    return T / (2 * mp.pi) * mp.log(T / (2 * mp.pi * mp.e)) + mp.mpf('0.875')


def smooth_zeros_to_cutoff(Gcut):
    """All rigid-staircase nodes whose model ordinate is at most ``Gcut``."""
    Gcut = mp.mpf(Gcut)
    K = max(0, int(mp.floor(smooth_count(Gcut) + mp.mpf('0.5'))))
    return [g for g in smooth_zeros(K) if g <= Gcut]


def poisson_zeros_to_cutoff(Gcut, seed=7, phase=0):
    """All seeded Poisson-model nodes through ``Gcut``.

    Generate one arrival beyond the cutoff before inversion.  This avoids the
    historical bug in which ``K=180`` silently capped a nominal ``Gcut=420``
    experiment even though the model count there is about 215.
    """
    ncut = float(smooth_count(Gcut))
    phase_float = float(phase)
    rng = np.random.default_rng(seed)
    arrival = 0.0
    K = 0
    while True:
        arrival += float(rng.exponential())
        if arrival + phase_float > ncut:
            break
        K += 1
    return [g for g in poisson_zeros(K, seed=seed, phase=phase) if g <= Gcut]


def true_zeros_to_cutoff(Gcut):
    """Numerical on-line zeta ordinates returned by mpmath through ``Gcut``."""
    Gcut = mp.mpf(Gcut)
    out = []
    k = 1
    while True:
        gamma = mp.zetazero(k).imag
        if gamma > Gcut:
            return out
        out.append(gamma)
        k += 1


def frame_form(gammas, L, m, dps=50):
    """Q = 2 SUM_gamma |<phi, e^{i gamma .}>|^2 in the orthonormal Legendre
    basis; returns mp.matrix.  Rank 2*len(gammas): use len >= m/2."""
    with mp.workdps(dps + 10):
        a = mp.mpf(L) / 4
        nk = [mp.sqrt(mp.mpf(2 * k + 1) / (2 * a)) for k in range(m)]
        gmax = max(float(g) for g in gammas)
        # nodes must resolve the oscillation e^{i gamma a x}: phase up to a*gmax
        nodes = gl_nodes(max(m + 4, 96, int(float(a) * gmax / 1.6) + 48))
        B = []
        W = []
        for x_, w_ in nodes:
            P = legvals(m, x_)
            B.append([nk[k] * P[k] for k in range(m)])
            W.append(w_ * a)
        Q = mp.matrix(m)
        for g in gammas:
            vre = [mp.mpf(0)] * m
            vim = [mp.mpf(0)] * m
            for t, (x_, _) in enumerate(nodes):
                arg = g * a * x_
                c = W[t] * mp.cos(arg)
                s = -W[t] * mp.sin(arg)
                Bt = B[t]
                for k in range(m):
                    vre[k] += c * Bt[k]
                    vim[k] += s * Bt[k]
            for k in range(m):
                for j in range(k, m):
                    inc = 2 * (vre[k] * vre[j] + vim[k] * vim[j])
                    Q[k, j] += inc
                    if j > k:
                        Q[j, k] += inc
        Qo = mp.matrix(m)
        with mp.workdps(dps):
            for k in range(m):
                for j in range(m):
                    Qo[k, j] = +Q[k, j]
    return Qo


def poisson_frame_ensemble(seeds, Ls, Gcut=300, m=32, dps=40, phase=-0.5):
    """Evaluate a reproducible seeded Poisson ensemble against the rigid model.

    Returns ``(smooth_values, rows, rejected)``, where each row is
    ``(seed, point_count, {L: lambda_m})``.  For ``phase=-0.5`` some first
    arrivals lie below the minimum of the asymptotic counting staircase; those
    seeds are reported in ``rejected`` rather than silently conditioned away.
    Consequently, summaries of ``rows`` describe the accepted-seed ensemble,
    not an unconditional Poisson law.
    """
    Ls = tuple(Ls)
    smooth = smooth_zeros_to_cutoff(Gcut)
    smooth_values = {
        L: spectral_lam_min(frame_form(smooth, L, m, dps=dps), nev=1)[0]
        for L in Ls
    }
    rows = []
    rejected = []
    for seed in seeds:
        try:
            gammas = poisson_zeros_to_cutoff(
                Gcut, seed=int(seed), phase=phase
            )
        except ValueError as exc:
            rejected.append((int(seed), str(exc)))
            continue
        values = {
            L: spectral_lam_min(frame_form(gammas, L, m, dps=dps), nev=1)[0]
            for L in Ls
        }
        rows.append((int(seed), len(gammas), values))
    return smooth_values, rows, rejected


if __name__ == "__main__":
    import time
    mp.mp.dps = 50
    m = 48
    max_cut = 420.0
    all_true = true_zeros_to_cutoff(max_cut)
    all_sm = smooth_zeros_to_cutoff(max_cut)
    all_po = poisson_zeros_to_cutoff(max_cut)
    all_po_match = poisson_zeros_to_cutoff(max_cut, phase=-0.5)
    # Gcut escalation on the validation case: frame(true) must rise toward the
    # spectral-form value 3.59571e-10 from below
    for Gcut in (180.0, 300.0, 420.0):
        gs = [g for g in all_true if g <= Gcut]
        Q = frame_form(gs, 2.485, m)
        lam = spectral_lam_min(Q, nev=1)[0]
        print("validation L=2.485 true zeros Gcut=%.0f (%d zeros): %s  (form: 3.59571e-10)"
              % (Gcut, len(gs), mp.nstr(lam, 6)), flush=True)
    Gcut = 420.0
    for L in (2.485, 2.996, 3.555):
        row = []
        for tag, allg in (("true", all_true), ("smooth", all_sm),
                          ("poisson0", all_po), ("poisson_half", all_po_match)):
            gs = [g for g in allg if g <= Gcut]
            t0 = time.time()
            Q = frame_form(gs, L, m)
            lam = spectral_lam_min(Q, nev=1)[0]
            row.append("%s %s (%.0fs)" % (tag, mp.nstr(lam, 6), time.time() - t0))
        print("L=%.3f: " % L + " | ".join(row), flush=True)
