"""FB-T1: boundary trace and structured tails of the spectral Galerkin argmin.

Pre-registration: PREREGISTRATION-FBT1.md (same directory). Run from repo root:
    python3 results/ias/free-boundary/fbt1_trace_tails.py
One worker, minutes-scale. Output: fbt1_output.txt (tee'd by the caller).
"""
import sys, time, json
sys.path.insert(0, '/home/ubuntu/Projects/Riemann-Zeta/src')
import numpy as np
import mpmath as mp
from scipy.special import spherical_jn
from spectral_margins import spectral_form, spectral_lam_min

L = mp.mpf(7) / 4
A = float(L) / 4.0                      # a = 0.4375
WINDOWS = [500.0, 1000.0, 2000.0, 3000.0]
NPER = 12                               # periods of sin^2(ra) per window
NPTS = 3000                             # grid points per window


def phihat_num(c, m, r):
    """phi-hat(r) = sum_k c_k nu_k 2a (-i)^k j_k(ra); float, vectorized in r."""
    nu = np.sqrt((2 * np.arange(m) + 1) / (2 * A))
    z = r * A
    out = np.zeros_like(r, dtype=complex)
    for k in range(m):
        if abs(c[k]) < 1e-30:
            continue
        out += c[k] * nu[k] * 2 * A * (-1j) ** k * spherical_jn(k, z)
    return out


def linhat(c0, c1, r):
    """transform of (c0 + c1 x) 1_[-a,a]."""
    s, co = np.sin(r * A), np.cos(r * A)
    base = 2 * s / r
    xpart = 1j * (2 * A * co / r - 2 * s / r ** 2)   # int x e^{-irx}
    return c0 * base + c1 * xpart


def window_stats(fh, r, power):
    return np.mean(r ** power * np.abs(fh) ** 2)


def tail_mass(hatfun, R, Rmax=6000.0, n=140000):
    r = np.linspace(R, Rmax, n)
    v = np.abs(hatfun(r)) ** 2
    integral = np.trapz(v, r)
    # remainder beyond Rmax from the measured local mean of r^2|f|^2
    tail_const = np.mean(r[-4000:] ** 2 * v[-4000:])
    rem = tail_const / Rmax
    return (2.0 / (2 * np.pi)) * (integral + rem)


results = {}
for m in (32, 48, 64):
    t0 = time.time()
    Q = spectral_form(L, m, dps=35)
    lams, vecs = spectral_lam_min(Q, nev=1, dps=28, vectors=True)
    lam = float(lams[0])
    c = np.array([float(x) for x in vecs[0]])
    # traces
    nu = np.sqrt((2 * np.arange(m) + 1) / (2 * A))
    signs = (-1.0) ** np.arange(m)
    dP1 = np.arange(m) * (np.arange(m) + 1) / 2.0          # P_k'(1)
    t_a = float(np.sum(c * nu))                             # phi(a)
    t_ma = float(np.sum(c * nu * signs))                    # phi(-a)
    dp_a = float(np.sum(c * nu * dP1)) / A                  # phi'(a^-)
    dp_ma = float(np.sum(c * nu * dP1 * (-signs))) / A      # phi'(-a^+), P_k'(-1)=(-1)^{k-1}dP1
    c0, c1 = (t_a + t_ma) / 2.0, (t_a - t_ma) / (2 * A)
    pp_a, pp_ma = dp_a - c1, dp_ma - c1                     # psi'(+-a)
    odd_frac = float(np.linalg.norm(c[1::2]) / np.linalg.norm(c))

    ph = lambda r: phihat_num(c, m, r)
    ps = lambda r: phihat_num(c, m, r) - linhat(c0, c1, r)

    row = dict(lam=lam, t_a=t_a, t_ma=t_ma, dp_a=dp_a, dp_ma=dp_ma,
               odd_frac=odd_frac, windows={})
    per = np.pi / A
    means_phi, means_psi = [], []
    for r0 in WINDOWS:
        r = np.linspace(r0, r0 + NPER * per, NPTS)
        fh, gh = ph(r), ps(r)
        h_phi = window_stats(fh, r, 2) / (t_a ** 2 + t_ma ** 2)
        h_psi = window_stats(gh, r, 4) / (pp_a ** 2 + pp_ma ** 2)
        row['windows'][r0] = dict(h_phi=h_phi, h_psi=h_psi,
                                  m2=window_stats(fh, r, 0),
                                  m2psi=window_stats(gh, r, 0))
        means_phi.append(window_stats(fh, r, 0))
        means_psi.append(window_stats(gh, r, 0))
    # log-log slopes across window centers
    lr = np.log(np.array(WINDOWS) + NPER * per / 2)
    row['slope_phi'] = float(np.polyfit(lr, np.log(means_phi), 1)[0])
    row['slope_psi'] = float(np.polyfit(lr, np.log(means_psi), 1)[0])
    row['tau_phi_287'] = tail_mass(ph, 287.0)
    row['tau_psi_287'] = tail_mass(ps, 287.0)
    row['tau_phi_1000'] = tail_mass(ph, 1000.0)
    row['tau_psi_1000'] = tail_mass(ps, 1000.0)
    row['secs'] = time.time() - t0
    results[m] = row
    print(f"m={m}  lam={lam:.6e}  t(a)={t_a:+.6f}  t(-a)={t_ma:+.6f}  "
          f"odd_frac={odd_frac:.2e}  ({row['secs']:.0f}s)")
    print(f"   phi'(a)={dp_a:+.4f}  psi'(a)={pp_a:+.4f}  "
          f"slope_phi={row['slope_phi']:+.3f}  slope_psi={row['slope_psi']:+.3f}")
    for r0 in WINDOWS:
        w = row['windows'][r0]
        print(f"   r~{int(r0)}: h_phi={w['h_phi']:.3f}  h_psi={w['h_psi']:.3f}")
    print(f"   tau_phi(287)={row['tau_phi_287']:.3e}  tau_psi(287)={row['tau_psi_287']:.3e}  "
          f"ratio={row['tau_psi_287']/row['tau_phi_287']:.2e}")
    print(f"   tau_phi(1000)={row['tau_phi_1000']:.3e}  tau_psi(1000)={row['tau_psi_1000']:.3e}")
    sys.stdout.flush()

t32, t48, t64 = (results[m]['t_a'] for m in (32, 48, 64))
print(f"\nP4 trace drift: q1=t48/t32={t48/t32:.4f}  q2=t64/t48={t64/t48:.4f} "
      f"(H_const ~1.00; H_log 0.90/0.93)")
with open('/home/ubuntu/Projects/Riemann-Zeta/results/ias/free-boundary/fbt1_results.json', 'w') as f:
    json.dump({str(k): v for k, v in results.items()}, f, indent=1, default=float)
print("done")
