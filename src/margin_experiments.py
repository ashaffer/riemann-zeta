"""margin_experiments.py — the zeta-form margin ladder and its structure theory.

All experiments use weil_core.build_form (conventions certified by oracle.py).

EXPECTED (July 26, 2026; float pipeline, Rayleigh-Ritz one-sided):
  margin sweep (m = 41): positivity holds through every prime-power threshold;
    deficits without the newest prime: -0.41/-0.40/-0.61/-0.59/-0.18 for
    windows of 2/3/4(=2^2)/5/7; rescues restore to ~1e-6.
  basis escalation: mid-window L = 1.75 margin CONVERGES 3.775 -> 3.442e-5
    (m = 41 -> 101); near-threshold margins COLLAPSE under refinement
    (L = 2.19: 1.44e-6 -> 1.18e-7).  Interior real, thresholds zero-slack.
  mechanism law: dLambda ~ -2 Lambda(p) chi(p) p^{-1/2} psi_min(log p); 8/8 sign
    predictions correct across q = 1,3,5,7,11.
  pole flip (zeta, L = 1.70): psi_min(log 2) = +0.106 pole-free -> -0.200 with pole;
    prime 2 flips from drain (-0.126) to rescuer (+0.131).
  safety factor rescue/deficit: 2.39, 1.45, 1.27, 1.05, 1.06, 1.03 at
    L = 1.55..3.20 — decays to 1 (zero slack inside the mechanism).
  cascade: #eigenvalues < 1e-2 grows 1,2,2,3,5,7 over the same L range; principal
    angle between bottom-3 blocks of landscape vs full form jumps ~20 -> 90 deg
    at L ~ 2.4 (the changing of the guard).
  keyhole (L = 3.2, m = 61): bottom vector's |F(r)| suppressed 200-5000x at the
    seven zeta zeros in band; nodes at 14.135, 21.020, 25.010, 30.410, 32.910,
    37.515 vs true 14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862.
"""
import numpy as np
from weil_core import build_form, lam_min_of, arch_weights, hat_overlap, hatFT


def margin_sweep(L_grid, m=41, prime_sets=(set(), {2}, {2, 3}, {2, 3, 5}, {2, 3, 5, 7})):
    """lam_min for variants including only the listed primes (zeta form).
    Implemented by building the full P and re-adding excluded primes' pieces is
    equivalent; here we rebuild per variant for clarity."""
    rg, WW = arch_weights('even')
    rows = []
    for L in L_grid:
        Qfull, G, ex = build_form(L, m, rg=rg, WW=WW)      # all primes
        Qnop, _, _ = build_form(L, m, include_primes=False, rg=rg, WW=WW)
        row = []
        from weil_core import PRIME_POWERS
        for V in prime_sets:
            P = np.zeros_like(Qnop)
            for nn, p in PRIME_POWERS:
                if p in V and 2*np.log(nn) < L:
                    Ps = hat_overlap(ex['Dm'] + np.log(nn), ex['d'])
                    P += 2*np.log(p)/np.sqrt(nn)*(Ps + Ps.T)/2
            row.append(lam_min_of(Qnop - P, G))
        rows.append((L, row))
    return rows


def mechanism_test(L, m, q, D, parity, p, with_pole=None):
    """First-order law test: predicted vs exact effect of adding prime p to the
    pole+archimedean landscape at (q, parity).  For zeta pass q=1, parity='even'."""
    rg, WW = arch_weights(parity)
    Q0, G, ex = build_form(L, m, D=D, q=q, parity=parity, include_primes=False,
                           rg=rg, WW=WW)
    Lc = np.linalg.cholesky(G); Li = np.linalg.inv(Lc)
    w0, U0 = np.linalg.eigh(Li @ Q0 @ Li.T)
    c = np.linalg.solve(Lc.T, U0[:, 0])            # G-normalized landscape minimizer
    from weil_core import kron
    PM = np.zeros_like(Q0)
    nn = p
    while 2*np.log(nn) < L + 0.4:
        ch = 1 if q == 1 else kron(D, nn)
        if ch:
            Ps = hat_overlap(ex['Dm'] + np.log(nn), ex['d'])
            PM += 2*np.log(p)*ch/np.sqrt(nn)*(Ps + Ps.T)/2
        nn *= p
    Ps2 = hat_overlap(ex['Dm'] + np.log(p), ex['d'])
    psi_min = c @ ((Ps2 + Ps2.T)/2) @ c
    dpred = -(c @ PM @ c)
    dexact = lam_min_of(Q0 - PM, G) - w0[0]
    return {'lam0': w0[0], 'psi_min': psi_min, 'dpred': dpred, 'dexact': dexact,
            'sign_match': np.sign(dpred) == np.sign(dexact)}


def cascade_and_keyhole(L=3.2, m=61, zeros=None, r_grid=None):
    """Bottom spectrum of the full zeta form and the node structure of its
    near-null vectors.  If `zeros` (true gamma_i) supplied, reports suppression
    |F(gamma_i)| / median|F| — forced small by lam_min + the certified identity;
    their LOCATION at the true gammas is the full-pipeline validation."""
    Q, G, ex = build_form(L, m)
    Lc = np.linalg.cholesky(G); Li = np.linalg.inv(Lc)
    w, U = np.linalg.eigh(Li @ Q @ Li.T)
    if r_grid is None:
        r_grid = np.arange(2.0, 45.0, 0.005)
    E = hatFT(r_grid, ex['xc'], ex['d'])
    report = {'eigs': w[:7], 'vectors': []}
    for k in range(3):
        c = np.linalg.solve(Lc.T, U[:, k])
        F = np.abs(E @ c)
        med = np.median(F)
        mins = sorted(r_grid[i] for i in range(1, len(r_grid)-1)
                      if F[i] < F[i-1] and F[i] < F[i+1] and F[i] < 0.12*med)
        entry = {'lam': w[k], 'nodes': mins[:9]}
        if zeros is not None:
            entry['suppression'] = [float(np.abs(E[np.argmin(np.abs(r_grid-g))] @ c)/med)
                                    for g in zeros]
        report['vectors'].append(entry)
    return report


if __name__ == "__main__":
    import mpmath as mp
    mp.mp.dps = 16
    gams = [float(mp.zetazero(k).imag) for k in range(1, 8)]
    rep = cascade_and_keyhole(zeros=gams)
    print("bottom eigenvalues:", " ".join("%.1e" % v for v in rep['eigs'][:5]))
    v = rep['vectors'][0]
    print("vector 1 suppression at zeros:", " ".join("%.4f" % s for s in v['suppression']))
    print("nodes:", ", ".join("%.3f" % x for x in v['nodes']))
    print("true :", ", ".join("%.4f" % g for g in gams))
    r = mechanism_test(1.70, 41, 1, 1, 'even', 2)
    print("pole flip check: psi_min(log2)=%+.3f dExact=%+.3e (EXPECTED -0.200, +0.131)"
          % (r['psi_min'], r['dexact']))
