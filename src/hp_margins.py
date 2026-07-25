"""hp_margins.py — the margin ladder in extended precision (M1's first rung).

The float pipeline (weil_core.build_form) computes the archimedean matrix by
Simpson quadrature in r on [0, 3000] — the piece whose 1.5% trapezoid error once
faked a disproof of RH (PROGRAM.md 2.6), and whose residual error floor is what
2.8 could not see below.  This module removes that error source exactly.

The x-space kernel.  Gauss: psi(z) = INT_0^inf [e^{-t}/t - e^{-zt}/(1-e^{-t})] dt.
For z = a + ir/2 (a = 1/4 zeta/even chi, 3/4 odd chi), averaging +-r:

  Re psi(a + ir/2) - psi(a) = INT_0^inf e^{-at} (1 - cos(rt/2)) / (1 - e^{-t}) dt,

a NONNEGATIVE integrand (identity verified against mpmath digamma to 1e-17).
Multiply by h(r) = |phihat(r)|^2, integrate (1/2pi) INT dr (Fubini is clean), and
use (1/2pi) INT h(r) cos(ru) dr = psi_phi(u), the autocorrelation of phi:

  (1/2pi) INT h(r) Re psi(a + ir/2) dr
      = psi(a) psi_phi(0) + 2 INT_0^inf [psi_phi(0) - psi_phi(u)]
                                        e^{-2au} / (1 - e^{-2u}) du.

For the hat basis, psi_phi is the exact piecewise cubic hat_overlap, compactly
supported: each archimedean matrix entry is a SHORT 1D integral of an exact
polynomial against a smooth explicit kernel — no r-truncation, no Simpson grid.
The matrix is Toeplitz (centers are equally spaced), so only m distinct
diagonals a(k) are ever computed.  Everything else in the form (Gram, pole,
prime overlaps) is exact closed form evaluated in mpmath.  The generalized
eigenproblem is solved in mpmath (bidiagonal Cholesky of the tridiagonal Gram,
then eigsy), so the entire chain runs at 25+ digits: what remains one-sided is
only Rayleigh-Ritz (computed lam_min is an upper bound on the operator's).

EXPECTED (measured July 25, 2026, this machine; dps 40 assembly / 30 solve):
  validation, L=1.75 m=41:
    max |A_hp - A_simpson| entrywise = 4.08e-07 (the float pipeline's true
      arch-matrix error, dominated by the R=3000 truncation) -- yet lam_min
      moves by < 1e-9: the truncation error is high-frequency Toeplitz and
      nearly orthogonal to the smooth minimizers.
    lam_min hp = 3.77497984e-05  vs float 3.77498877e-05: the float bias is a
      stable +0.7-0.9e-09 at every (L, m) tested -- the float ladder's error
      budget, now measured rather than guessed.
    zero-side inequality: 2 SUM_{first 60 zeros} |phihat(gamma)|^2
      = 3.6207e-05 <= Q(phi) = 3.7750e-05  (captures 96%; deficit is the
      gamma^-4 hat tail, not error)
  p=2 window, hp ladder at L=1.75, m = 41/61/81/101/121:
    3.77498/3.59685/3.50265/3.44205/3.39895e-05.  (A Richardson fit of these
    hat values alone suggested a basis limit of 3.18-3.30e-05; the spectral
    basis of spectral_margins.py later got BELOW that bracket — 3.1439e-05 at
    m=48 and still descending — so hat-only extrapolation underestimates the
    remaining basis error.  Use the spectral ladder for operator limits.)
  the p=3-window question (L=2.485, mid-window; 2.8 could not resolve):
    m = 41:  1.39741e-06     m = 121: 3.45007e-08
    m = 61:  4.13636e-07     m = 161: 1.24514e-08
    m = 81:  1.52570e-07     m = 201: 5.57117e-09
    m = 101: 6.71035e-08
    float minus hp is a STABLE +7e-10 at every m: the float ladder was real
    Galerkin data, not a quadrature floor -- but it keeps descending like
    m^{-3.6} (alpha stable 3.6 +/- 0.1 over the last four rungs) with no
    plateau above 5.6e-09.  Verdict on 2.8: the "shared
    resolution floor" was neither float noise nor a flat envelope; it is a
    genuine shared basis transient.  The true interior margins for p >= 3
    sit below hat-basis reach; the prolate basis is the next instrument.
  threshold approach (p=3 boundary, m=81): lam_min at d = distance-to-threshold
    0.100/0.050/0.025/0.007/0.002 = 4.070/2.541/2.057/1.744/1.712e-07; the
    small-d flattening IS the m=81 basis floor (the L=2.19 m-ladder crosses
    it: 1.436/0.382/0.175e-06 at m=41/61/81, still descending).  Raw kappa
    0.49-0.68 by rung choice; floor-subtracted kappa ~ 1.3-1.5.  The float-era
    kappa ~ 0.4 was mostly floor.
"""
import numpy as np
import mpmath as mp
from weil_core import PRIME_POWERS, kron


# ---------------------------------------------------------------- primitives
def Omega(v, d):
    """Exact hat autocorrelation INT hat(x) hat(x+v) dx, unit hats half-width d."""
    t = abs(mp.mpf(v)) / d
    if t >= 2:
        return mp.mpf(0)
    if t >= 1:
        return d * (2 - t) ** 3 / 6
    return d * (mp.mpf(2) / 3 - t * t + t ** 3 / 2)


def kernel_tail(U, twoa):
    """INT_U^inf e^{-twoa*u}/(1 - e^{-2u}) du = SUM_n e^{-(2n+twoa)U}/(2n+twoa)."""
    tot, n = mp.mpf(0), 0
    while True:
        c = 2 * n + twoa
        term = mp.e ** (-c * U) / c
        tot += term
        if term < mp.mpf(10) ** (-mp.mp.dps - 5):
            return tot
        n += 1


def arch_diagonal(k, d, twoa):
    """a(k) = (1/2pi) INT |phihat_i phihat_j| Re psi(a+ir/2) dr for |i-j| = k,
    via the x-space kernel; twoa = 2a (1/2 for zeta/even, 3/2 for odd)."""
    kd = k * d
    U0 = (k + 2) * d
    Om0 = Omega(kd, d)

    def integrand(u):
        br = Om0 - (Omega(kd - u, d) + Omega(kd + u, d)) / 2
        return br * mp.e ** (-twoa * u) / (-mp.expm1(-2 * u))

    pts = sorted({j * d for j in range(max(k - 2, 0), k + 3)} | {mp.mpf(0), U0})
    pts = [p for p in pts if 0 <= p <= U0]
    body = mp.quad(integrand, pts)
    return mp.digamma(twoa / 2) * Om0 + 2 * body + 2 * Om0 * kernel_tail(U0, twoa)


# ---------------------------------------------------------------- assembly
def hp_form(L, m, parity='even', dps=40, include_primes=True, zeta_pole=True,
            q=1, D=1, prime_set=None):
    """Assemble the truncated Weil form in the hat basis entirely in mpmath.
    Returns (Q, G) as mp.matrix at dps digits.  Conventions == weil_core.
    q = 1 is zeta (pole on); q > 1 with Kronecker discriminant D is the
    chi-twisted pole-free form (use parity='odd' for D < 0).  prime_set
    restricts to the listed underlying primes (None = all below e^{L/2})."""
    with mp.workdps(dps + 20):
        ell = mp.mpf(L) / 2
        d = ell / (m + 1)
        twoa = mp.mpf('0.5') if parity == 'even' else mp.mpf('1.5')
        arch = [arch_diagonal(k, d, twoa) for k in range(m)]
        gram = [Omega(k * d, d) for k in range(m)]
        prime = [mp.mpf(0)] * m
        if include_primes:
            for nn, p in PRIME_POWERS:
                ln = mp.log(nn)
                if 2 * ln < L:
                    if prime_set is not None and p not in prime_set:
                        continue
                    c = 1 if q == 1 else kron(D, nn)
                    if not c:
                        continue
                    w = 2 * mp.log(p) * c / mp.sqrt(nn)
                    for k in range(m):
                        prime[k] += w * (Omega(k * d + ln, d) + Omega(k * d - ln, d)) / 2
        lp = mp.log(mp.pi) - mp.log(q)              # subtracted below: +log(q/pi)*G
        diag = [arch[k] - lp * gram[k] - prime[k] for k in range(m)]
        xc = [-ell / 2 + (i + 1) * d for i in range(m)]
        Q = mp.matrix(m)
        G = mp.matrix(m)
        for i in range(m):
            for j in range(m):
                Q[i, j] = diag[abs(i - j)]
                G[i, j] = gram[abs(i - j)]
        if zeta_pole and q == 1:
            s = mp.mpf('0.5')
            cs = (2 * mp.cosh(s * d) - 2) / (s * s * d)
            hp_ = [mp.e ** (s * x) * cs for x in xc]
            hm_ = [mp.e ** (-s * x) * cs for x in xc]
            for i in range(m):
                for j in range(m):
                    Q[i, j] += hp_[i] * hm_[j] + hm_[i] * hp_[j]
        Qo = mp.matrix(m)
        Go = mp.matrix(m)
        with mp.workdps(dps):
            for i in range(m):
                for j in range(m):
                    Qo[i, j] = +Q[i, j]
                    Go[i, j] = +G[i, j]
    return Qo, Go


# ---------------------------------------------------------------- eigensolve
def hp_lam_min(Q, G, nev=3, dps=30, vectors=False):
    """Smallest nev generalized eigenvalues of (Q, G) in mpmath.
    G is tridiagonal: Cholesky is bidiagonal, solves are O(m^2)."""
    with mp.workdps(dps):
        m = Q.rows
        l0 = [mp.sqrt(G[0, 0])]
        l1 = []
        for i in range(1, m):
            l1.append(G[i, i - 1] / l0[-1])
            l0.append(mp.sqrt(G[i, i] - l1[-1] ** 2))

        def linv(B):
            R = mp.matrix(m)
            for j in range(m):
                R[0, j] = B[0, j] / l0[0]
                for i in range(1, m):
                    R[i, j] = (B[i, j] - l1[i - 1] * R[i - 1, j]) / l0[i]
            return R

        M = linv(linv(Q).T)
        for i in range(m):
            for j in range(i):
                s = (M[i, j] + M[j, i]) / 2
                M[i, j] = s
                M[j, i] = s
        E, V = mp.eigsy(M)
        order = sorted(range(m), key=lambda i: E[i])
        lams = [E[i] for i in order[:nev]]
        if not vectors:
            return lams
        vecs = []
        for idx in order[:nev]:
            u = [V[i, idx] for i in range(m)]
            c = [mp.mpf(0)] * m
            c[m - 1] = u[m - 1] / l0[m - 1]
            for i in range(m - 2, -1, -1):
                c[i] = (u[i] - l1[i] * c[i + 1]) / l0[i]
            vecs.append(c)
        return lams, vecs


# ---------------------------------------------------------------- validation
def float_arch_matrix(L, m):
    """The float pipeline's archimedean matrix (Simpson, R=3000), for comparison."""
    from weil_core import arch_weights, hatFT
    rg, WW = arch_weights('even')
    ell = L / 2
    d = ell / (m + 1)
    xc = np.linspace(-ell / 2 + d, ell / 2 - d, m)
    A = np.zeros((m, m))
    step = 40000
    for i in range(0, len(rg), step):
        E = hatFT(rg[i:i + step], xc, d)
        A += ((E * WW[i:i + step][:, None]).conj().T @ E).real
    return A / np.pi


def hp_arch_matrix_float(L, m, dps=40):
    """The kernel-path archimedean matrix, rounded to float, for comparison."""
    with mp.workdps(dps + 20):
        ell = mp.mpf(L) / 2
        d = ell / (m + 1)
        a = [arch_diagonal(k, d, mp.mpf('0.5')) for k in range(m)]
    A = np.empty((m, m))
    for i in range(m):
        for j in range(m):
            A[i, j] = float(a[abs(i - j)])
    return A


def zero_side_partial(L, m, c_vec, n_zeros=60):
    """2 SUM_{k<=n_zeros} |phihat(gamma_k)|^2 for the (G-normalized) vector c.
    A PARTIAL sum of squares: must be <= Q(phi); the deficit is the gamma^-4
    tail of the hat transform, not an error."""
    from weil_core import hatFT
    ell = L / 2
    d = ell / (m + 1)
    xc = np.linspace(-ell / 2 + d, ell / 2 - d, m)
    gams = np.array([float(mp.zetazero(k).imag) for k in range(1, n_zeros + 1)])
    F = hatFT(gams, xc, d) @ np.asarray(c_vec, float)
    return 2 * float((np.abs(F) ** 2).sum())


if __name__ == "__main__":
    import time
    mp.mp.dps = 20
    print("validation at L=1.75, m=41 (the converged p=2-window anchor)")
    t0 = time.time()
    Af = float_arch_matrix(1.75, 41)
    Ah = hp_arch_matrix_float(1.75, 41)
    print("  max |A_simpson - A_kernel| = %.2e   (float pipeline's true arch error)"
          % np.abs(Af - Ah).max())
    Q, G = hp_form(1.75, 41)
    lams, vecs = hp_lam_min(Q, G, nev=1, vectors=True)
    print("  lam_min hp = %s   (float pipeline: 3.77498877e-05)" % mp.nstr(lams[0], 9))
    zs = zero_side_partial(1.75, 41, [float(x) for x in vecs[0]])
    print("  zero-side partial (60 zeros) = %.4e <= Q(phi) = %.4e : %s"
          % (zs, float(lams[0]), "OK" if zs <= float(lams[0]) else "VIOLATION"))
    print("  (%.0f s)" % (time.time() - t0))
    print("the p=3-window question (L=2.485): EXPECTED in module docstring")
    for m_ in (41, 61):
        Q, G = hp_form(2.485, m_)
        lam = hp_lam_min(Q, G, nev=1)[0]
        print("  m=%3d  lam_min = %s" % (m_, mp.nstr(lam, 6)))
