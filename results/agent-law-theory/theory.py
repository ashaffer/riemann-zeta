"""theory.py — candidate closed forms E[a, N] for -ln lambda_min, and the
exact prolate (time-and-band-limiting) spectrum needed to evaluate the
Landau-Widom / concentration candidate without free constants.

Notation: a = L/4, T* = 2 pi e^{2a} (Nyquist height), staircase
N_{alpha,beta}(T) = alpha (T/2pi) ln(T/(2 pi beta e)) + 7/8, density
rho(t) = N'(t) = (alpha/2pi) ln(t/(2 pi beta)) for t >= 2 pi beta.
Deficit D(T) = (a/pi) T - N(T) (Nyquist count minus zero count), maximal at
T*, vanishing at T_cap = 2 pi beta e^{2a/alpha + 1} (for alpha=beta=1:
T_cap = e T*).

CANDIDATE FUNCTIONALS (each with one overall constant b, except C7):
  C1  E = b * N(T*)                    count below the Nyquist crossing
  C2  E = b * INT_0^{T*} (2a - 2pi rho) dN     per-zero undersampling gap
  C3  E = b * INT_0^{T*} (2a - 2pi rho) dt/2pi  pure area deficit ( = b e^{2a} alpha beta ... )
  C5  E = b * N(T_cap)                 count to deficit closure
  C10 E = b * INT_0^{T*} ln(T*/t) dN   log-weighted toll
  C8  E = 2 pi^2 D(T*) / ln(16 a T*)   Landau-Widom plunge (closed form, no b)
  C7  exact prolate concentration model (numerical, no free constant):
      choose band [0, T]; all zeros <= T are vanished (2#{gamma<=T} linear
      constraints); cost = smallest achievable out-of-band leakage
      1 - lambda_{n}(c) at mode n = 2#{gamma<=T}, c = aT; optimize T.
Integrals are done numerically (mpmath quad) from the first zero upward, so
small-a sign traps of the asymptotic formulas are avoided.
"""
import mpmath as mp
from law_core import sph_jn_list, staircase_zeros


def Nfun(T, a=None, alpha=1, beta=1):
    T = mp.mpf(T)
    tp = 2 * mp.pi
    return mp.mpf(alpha) * T / tp * (mp.log(T / (tp * mp.mpf(beta))) - 1) \
        + mp.mpf('0.875')


def rho(t, alpha=1, beta=1):
    tp = 2 * mp.pi
    return mp.mpf(alpha) / tp * mp.log(mp.mpf(t) / (tp * mp.mpf(beta)))


def Tstar(a, alpha=1, beta=1):
    return 2 * mp.pi * mp.mpf(beta) * mp.e ** (2 * mp.mpf(a) / mp.mpf(alpha))


def Tcap(a, alpha=1, beta=1):
    return 2 * mp.pi * mp.mpf(beta) * mp.e ** (2 * mp.mpf(a) / mp.mpf(alpha) + 1)


def t_first(alpha=1, beta=1):
    """first staircase zero (N = 1/2)"""
    zs = staircase_zeros(1, alpha=str(alpha), beta=str(beta))
    return zs[0]


def _clip0(x):
    return x if x > 0 else mp.mpf(0)


def E_candidates(a, alpha=1, beta=1):
    """dict of candidate exponents WITHOUT the overall constant b
    (except C8 which is absolute)."""
    a = mp.mpf(a)
    Ts = Tstar(a, alpha, beta)
    Tc = Tcap(a, alpha, beta)
    t0 = t_first(alpha, beta)
    out = {}
    out['C1_N(T*)'] = Nfun(Ts, a, alpha, beta)
    out['C5_N(Tcap)'] = Nfun(Tc, a, alpha, beta)
    if Ts > t0:
        out['C2_gap_dN'] = mp.quad(
            lambda t: _clip0(2 * a - 2 * mp.pi * rho(t, alpha, beta))
            * rho(t, alpha, beta), [t0, Ts])
        out['C10_log_dN'] = mp.quad(
            lambda t: mp.log(Ts / t) * rho(t, alpha, beta), [t0, Ts])
    else:
        out['C2_gap_dN'] = mp.mpf(0)
        out['C10_log_dN'] = mp.mpf(0)
    out['C3_area'] = mp.quad(
        lambda t: _clip0(2 * a - 2 * mp.pi * rho(t, alpha, beta))
        / (2 * mp.pi), [2 * mp.pi * mp.mpf(beta) * mp.mpf('1.0001'), Ts]) \
        + mp.mpf(beta)  # t in (0, 2 pi beta): integrand = 2a - 0 ... contributes 2a*2pi*beta/2pi ... see note
    # NOTE on C3 below-2pi-beta piece: rho = 0 there, integrand = 2a,
    # contributing 2a * (2 pi beta) / (2 pi) = 2 a beta.  Add it:
    out['C3_area'] += 2 * a * mp.mpf(beta) - mp.mpf(beta)  # replace crude +beta
    D = a / mp.pi * Ts - Nfun(Ts, a, alpha, beta)
    out['C8_LW'] = 2 * mp.pi ** 2 * D / mp.log(16 * a * Ts)
    return out


# ---------------- exact prolate spectrum ----------------

def prolate_out_eigs(a, T, m=96, dps=50, nodes=None):
    """Eigenvalues mu_0 <= mu_1 <= ... of B_out = I - A_in on the m-dim
    Legendre space of [-a, a], where A_in = (1/2pi) INT_{-T}^{T} v(r) v(r)^*.
    mu_n -> 1 - lambda_{prolate n} (Galerkin: A_in eigenvalues are lower
    bounds, so mu are upper bounds, decreasing in m).
    Returns sorted list (both parities merged)."""
    with mp.workdps(dps + 10):
        a = mp.mpf(a)
        T = mp.mpf(T)
        # Gauss-Legendre on [0, T] for the r-integral; v_k(r) ~ j_k(ra):
        # oscillation scale aT; use ~ 1.5*aT + 60 nodes
        from law_core import mp as _mp  # same mpmath
        from spectral_margins import gl_nodes
        npts = int(1.5 * float(a * T)) + 60
        if nodes is None:
            nodes = gl_nodes(max(npts, m + 8))
        ck = [mp.sqrt(a * (2 * k + 1) / 2) for k in range(m)]
        ke = list(range(0, m, 2))
        ko = list(range(1, m, 2))
        Ae = [[mp.mpf(0)] * len(ke) for _ in ke]
        Ao = [[mp.mpf(0)] * len(ko) for _ in ko]
        for x_, w_ in nodes:
            r = T * (1 + x_) / 2          # r in [0, T]
            wt = w_ * T / 2 / mp.pi       # (1/2pi) * 2 (both signs) * dr
            j = sph_jn_list(m - 1, r * a, dps + 10)
            ve = [2 * ck[k] * j[k] for k in ke]
            vo = [2 * ck[k] * j[k] for k in ko]
            for i in range(len(ke)):
                for jj in range(i, len(ke)):
                    Ae[i][jj] += wt * ve[i] * ve[jj]
            for i in range(len(ko)):
                for jj in range(i, len(ko)):
                    Ao[i][jj] += wt * vo[i] * vo[jj]
        mus = []
        with mp.workdps(dps):
            for A, idx in ((Ae, ke), (Ao, ko)):
                n = len(idx)
                B = mp.matrix(n)
                for i in range(n):
                    for jj in range(i, n):
                        B[i, jj] = (1 if i == jj else 0) - A[i][jj]
                        B[jj, i] = B[i, jj]
                E = mp.eigsy(B, eigvals_only=True)
                mus.extend([E[i] for i in range(n)])
        mus.sort()
        return mus


def E_C7(a, alpha=1, beta=1, m=96, dps=50, Tmax_fac=1.6, verbose=False):
    """Exact concentration-model exponent: max over T (just below each zero)
    of -ln(1 - lambda_{2k}(aT)) where k = #zeros <= T.
    Scans T -> gamma_{k+1}^- for k = 0, 1, 2, ... until T > Tmax_fac * Tcap.
    Returns (E, T_at_max, k_at_max).  No free constant."""
    zs = staircase_zeros(200, alpha=str(alpha), beta=str(beta),
                         gmax=float(Tmax_fac * Tcap(a, alpha, beta)) + 50)
    best = (mp.mpf('-inf'), None, None)
    for k in range(0, len(zs)):
        T = zs[k] * (1 - mp.mpf('1e-9'))   # just below gamma_{k+1}
        if T > Tmax_fac * Tcap(a, alpha, beta):
            break
        mus = prolate_out_eigs(a, T, m=m, dps=dps)
        n = 2 * k
        if n >= len(mus):
            break
        E = -mp.log(mus[n])
        if verbose:
            print("  C7 scan: k=%d T=%.2f c=%.2f  mu_%d=%s  E=%.3f"
                  % (k, float(T), float(a * T), n, mp.nstr(mus[n], 4),
                     float(E)), flush=True)
        if E > best[0]:
            best = (E, T, k)
    return best


def E_fuchs(a, alpha=1, beta=1, Tmax_fac=1.6):
    """Analytic skeleton of C7 via Fuchs' fixed-n asymptotic
    1 - lambda_n(c) ~ 4 sqrt(pi) 8^n c^{n+1/2} e^{-2c} / n!.
    Same scan structure; returns (E, T, k)."""
    zs = staircase_zeros(200, alpha=str(alpha), beta=str(beta),
                         gmax=float(Tmax_fac * Tcap(a, alpha, beta)) + 50)
    best = (mp.mpf('-inf'), None, None)
    for k in range(0, len(zs)):
        T = zs[k]
        if T > Tmax_fac * Tcap(a, alpha, beta):
            break
        c = mp.mpf(a) * T
        n = 2 * k
        E = 2 * c - (n + mp.mpf('0.5')) * mp.log(c) - n * mp.log(8) \
            + mp.log(mp.factorial(n)) - mp.log(4 * mp.sqrt(mp.pi))
        if E > best[0]:
            best = (E, T, k)
    return best


# ---------------- law refit ----------------

def refit_law(Ls, lnlams):
    """Fit ln lam = A - b e^{L/2}(L/2 + c0): linear in (A, b) at fixed c0;
    scan c0.  Returns (A, b, c0, rms)."""
    import numpy as np
    Ls = np.asarray([float(x) for x in Ls])
    y = np.asarray([float(x) for x in lnlams])
    best = None
    for c0 in np.arange(-2.0, 10.0, 0.01):
        X = np.vstack([np.ones_like(Ls), -np.exp(Ls / 2) * (Ls / 2 + c0)]).T
        coef, res, _, _ = np.linalg.lstsq(X, y, rcond=None)
        pred = X @ coef
        rms = float(np.sqrt(np.mean((pred - y) ** 2)))
        if best is None or rms < best[3]:
            best = (float(coef[0]), float(coef[1]), float(c0), rms)
    return best


if __name__ == "__main__":
    mp.mp.dps = 40
    for L in (2.485, 2.996):
        a = mp.mpf(L) / 4
        cand = E_candidates(a)
        print("L=%.3f  a=%.5f  T*=%.3f  Tcap=%.3f" %
              (L, float(a), float(Tstar(a)), float(Tcap(a))))
        for k, v in cand.items():
            print("   %-12s %10.5f" % (k, float(v)))
