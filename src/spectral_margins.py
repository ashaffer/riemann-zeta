"""spectral_margins.py — the margin ladder in a spectral (Legendre) basis.

Why this exists (PROGRAM.md 2.14): below ~1e-8 the hat basis, not the arithmetic,
is the binding constraint — the hat-Galerkin value descends like m^{-3.6} toward
the operator margin and cannot reach it at feasible m.  The Weil-form minimizer at
fixed support is analytic, so a spectral Galerkin space converges at a geometric
rate and the ladder can PLATEAU at the true margin, if that margin exceeds the
arithmetic floor.  This is the practical route into the regime the frontier
literature reaches with prolate machinery.

Basis: b_k(x) = sqrt((2k+1)/(2a)) P_k(x/a) on [-a, a], a = L/4.  The Gram matrix
is exactly I (no generalized eigenproblem, perfect conditioning).  By the x -> -x
symmetry, S_kj(u) = 0 for k+j odd and the form block-diagonalizes by parity.

Archimedean term: the same x-space kernel as hp_margins (Gauss digamma identity),
  A = [psi(a0) - log(q/pi... sign per ledger) ...] with
  A_kj = psi(a0) delta_kj + 2 INT_0^{2a} [delta_kj - S_kj(u)] w(u) du
         + 2 delta_kj INT_{2a}^inf w,   w(u) = e^{-2 a0 u}/(1 - e^{-2u}),
where S_kj(u) is the symmetrized shifted overlap INT b_k(x) b_j(x+u) dx — an EXACT
polynomial in u of degree <= k+j+1.  Since S(0) = I, [I - S(u)]/u is a polynomial,
and the u-integrand  [I-S(u)]/u * (u w(u))  is polynomial x analytic: Gauss-
Legendre in u is exact for the polynomial factor and geometrically convergent for
u w(u) (nearest singularity at u = +-i pi).  All overlaps are themselves computed
by Gauss-Legendre in x, exact for polynomial integrands.  No r-truncation, no
Simpson, no hinge bookkeeping.

EXPECTED (measured July 25, 2026, this machine; dps 50 assembly / 40 solve):
  overlap engine unit tests: S_00 err 5.3e-51, S_11 err 0, S_01 (parity) = 0
  L=1.75 ladder m=8/12/16/20/24/28/32/40/48:
    4.13301/3.24836/3.18972/3.17791/3.16043/3.15316/3.15192/3.14680/3.14389e-05
    — below the hat pipeline's reach by m=16 (hats at m=121: 3.399e-05), and
    below the hat-only Richardson bracket [3.18, 3.30]e-05 by m=24: hat-basis
    extrapolation underestimated its own residual.  Still creeping at m=48
    (upper bound 3.1439e-05; tail suggests a limit near 3.12-3.14e-05).
  L=2.485 ladder (the p=3 window, below the hat wall):
    m=12: 7.5308e-08    m=24: 3.86882e-10   m=40: 3.61910e-10
    m=16: 4.4677e-09    m=28: 3.74714e-10   m=48: 3.59571e-10
    m=20: 5.9239e-10    m=32: 3.66564e-10   m=64: 3.56788e-10
    PLUNGE-THEN-CREEP: the spectral basis resolves the analytic bulk by m~24
    (hats needed m=201 to reach 5.6e-09; spectral m=24 is 14x below that),
    then creeps algebraically — the minimizer has interior derivative kinks at
    x = +-(a - log p) inherited from the prime shift operators, so convergence
    is spectral-then-algebraic.  Tail extrapolation (beta ~ 1-1.2 in m^-beta
    fits of the decrements) gives lam_min(operator) ~ 3.49-3.50e-10; the m=64
    value 3.5679e-10 is a hard (Rayleigh-Ritz) upper bound.
    THE SECOND RUNG OF f(p): f(2) ~ 3.13e-05, f(3) ~ 3.5e-10.
  zero-side inequality at (L=2.485, m=48): 2 SUM_{60 zeros} |phihat(gamma)|^2
    = 3.10471e-10 <= Q(phi) = 3.59571e-10 (86% captured) — the spectral
    eigenvalue and the explicit formula agree at the tenth decimal with no
    shared code.
"""
import numpy as np
import mpmath as mp
from mpmath.calculus.quadrature import GaussLegendre
from weil_core import PRIME_POWERS, kron
from hp_margins import kernel_tail

_NODES = {}


def gl_nodes(npoints_min):
    """Cached Gauss-Legendre nodes on [-1, 1] with >= npoints_min points.
    mpmath's rule at degree d has 3*2^(d-1) points; exact for degree 2K-1."""
    deg = 1
    while 3 * 2 ** (deg - 1) < npoints_min:
        deg += 1
    key = (deg, mp.mp.prec)
    if key not in _NODES:
        _NODES[key] = GaussLegendre(mp.mp).calc_nodes(deg, mp.mp.prec)
    return _NODES[key]


def legvals(m, t):
    """P_0..P_{m-1}(t) by recurrence (t an mpf)."""
    P = [mp.mpf(1)]
    if m > 1:
        P.append(t)
    for k in range(1, m - 1):
        P.append(((2 * k + 1) * t * P[k] - k * P[k - 1]) / (k + 1))
    return P


def overlap_S(m, a, u, nodes, nk):
    """Symmetrized shifted overlap S_kj(u) = (T_kj + T_jk)/2 with
    T_kj = INT_{-a}^{a-u} b_k(x) b_j(x+u) dx, orthonormal b.  Parity:
    S_kj = 0 for k+j odd (enforced exactly).  Returns list-of-lists (mp)."""
    lo, hi = -a, a - u
    S = [[mp.mpf(0)] * m for _ in range(m)]
    if hi <= lo:
        return S
    c, h = (lo + hi) / 2, (hi - lo) / 2
    for x_, w_ in nodes:
        x = c + h * x_
        wt = w_ * h
        B1 = legvals(m, x / a)
        B2 = legvals(m, (x + u) / a)
        for k in range(m):
            bk = wt * B1[k]
            row = S[k]
            for j in range(k % 2, m, 2):        # k+j even only
                row[j] += bk * B2[j]
    for k in range(m):
        for j in range(k % 2, m, 2):
            S[k][j] *= nk[k] * nk[j]
    # symmetrize (T and T^T agree up to quadrature ordering; average anyway)
    for k in range(m):
        for j in range(k):
            if (k + j) % 2 == 0:
                s = (S[k][j] + S[j][k]) / 2
                S[k][j] = s
                S[j][k] = s
    return S


def spectral_form(L, m, dps=50, include_primes=True, zeta_pole=True,
                  q=1, D=1, parity='even', prime_set=None, nx=None, nu=None):
    """The truncated Weil form in the orthonormal Legendre basis: returns Q
    (mp.matrix, Gram = I).  q = 1, parity 'even', zeta_pole=True is zeta;
    q > 1 with D the Kronecker discriminant is the chi-twisted, pole-free form."""
    with mp.workdps(dps + 15):
        a = mp.mpf(L) / 4
        twoa0 = mp.mpf('0.5') if parity == 'even' else mp.mpf('1.5')
        nk = [mp.sqrt(mp.mpf(2 * k + 1) / (2 * a)) for k in range(m)]
        nodes_x = gl_nodes(max(m + 4, 96))
        nodes_u = gl_nodes(max(m + 8, 192))
        A = [[mp.mpf(0)] * m for _ in range(m)]
        for xu, wu in nodes_u:                       # u = a(1 + xu) in [0, 2a]
            u = a * (1 + xu)
            S = overlap_S(m, a, u, nodes_x, nk)
            guw = wu * a * u * mp.e ** (-twoa0 * u) / (-mp.expm1(-2 * u))
            for k in range(m):
                Sk = S[k]
                Ak = A[k]
                for j in range(k % 2, m, 2):
                    Ak[j] += guw * (((1 if j == k else 0) - Sk[j]) / u)
        tail = kernel_tail(2 * a, twoa0)
        shift = mp.digamma(twoa0 / 2) + 2 * tail + mp.log(mp.mpf(q) / mp.pi)
        Q = mp.matrix(m)
        for k in range(m):
            for j in range(m):
                Q[k, j] = 2 * A[k][j] + (shift if k == j else 0)
        if include_primes:
            for nn, p in PRIME_POWERS:
                ln = mp.log(nn)
                if 2 * ln < L:
                    if prime_set is not None and p not in prime_set:
                        continue
                    c = 1 if q == 1 else kron(D, nn)
                    if not c:
                        continue
                    Sp = overlap_S(m, a, ln, nodes_x, nk)
                    w = 2 * mp.log(p) * c / mp.sqrt(nn)
                    for k in range(m):
                        for j in range(m):
                            Q[k, j] -= w * Sp[k][j]
        if zeta_pole and q == 1:
            vp = [mp.mpf(0)] * m
            vm = [mp.mpf(0)] * m
            for x_, w_ in nodes_x:
                x = a * x_
                wt = w_ * a
                B = legvals(m, x_)
                ep, em = mp.e ** (x / 2), mp.e ** (-x / 2)
                for k in range(m):
                    vp[k] += wt * B[k] * ep
                    vm[k] += wt * B[k] * em
            for k in range(m):
                vp[k] *= nk[k]
                vm[k] *= nk[k]
            for k in range(m):
                for j in range(m):
                    Q[k, j] += vp[k] * vm[j] + vm[k] * vp[j]
        Qo = mp.matrix(m)
        with mp.workdps(dps):
            for k in range(m):
                for j in range(m):
                    Qo[k, j] = +Q[k, j]
    return Qo


def spectral_lam_min(Q, nev=3, dps=40, vectors=False):
    with mp.workdps(dps):
        E, V = mp.eigsy(Q)
        order = sorted(range(Q.rows), key=lambda i: E[i])
        lams = [E[i] for i in order[:nev]]
        if not vectors:
            return lams
        return lams, [[V[i, idx] for i in range(Q.rows)] for idx in order[:nev]]


def zero_side_partial_spectral(L, m, coeffs, n_zeros=80, dps=25):
    """2 SUM |phihat(gamma)|^2 for phi = sum c_k b_k; a partial sum of squares,
    must be <= Q(phi) = lam for the unit minimizer."""
    with mp.workdps(dps):
        a = mp.mpf(L) / 4
        nk = [mp.sqrt(mp.mpf(2 * k + 1) / (2 * a)) for k in range(m)]
        nodes = gl_nodes(max(m + 4, 96))
        tot = mp.mpf(0)
        for kz in range(1, n_zeros + 1):
            g = mp.zetazero(kz).imag
            re = mp.mpf(0)
            im = mp.mpf(0)
            for x_, w_ in nodes:
                x = a * x_
                wt = w_ * a
                B = legvals(m, x_)
                phi = mp.fsum(coeffs[k] * nk[k] * B[k] for k in range(m))
                re += wt * phi * mp.cos(g * x)
                im -= wt * phi * mp.sin(g * x)
            tot += re * re + im * im
        return 2 * tot


if __name__ == "__main__":
    import time
    mp.mp.dps = 50
    # --- unit tests: closed-form overlaps
    a = mp.mpf('0.5')
    nk = [mp.sqrt(mp.mpf(2 * k + 1) / (2 * a)) for k in range(4)]
    nodes = gl_nodes(96)
    u = mp.mpf('0.3')
    S = overlap_S(4, a, u, nodes, nk)
    exact00 = 1 - u / (2 * a)
    tau = u / a          # T_11 = ((1-tau)^3 + 1)/2 + (3/4) tau^2 (tau - 2)
    exact11 = ((1 - tau) ** 3 + 1) / 2 + mp.mpf(3) / 4 * tau * tau * (tau - 2)
    print("S_00 err %.1e   S_11 err %.1e   S_01 (must be 0) %.1e"
          % (abs(S[0][0] - exact00), abs(S[1][1] - exact11), abs(S[0][1])))
    # --- ladders
    for L, ms in ((1.75, (8, 12, 16, 20, 24)), (2.485, (12, 16, 20, 24, 28, 32))):
        print("L = %.3f spectral ladder:" % L)
        for m_ in ms:
            t0 = time.time()
            Q = spectral_form(L, m_)
            lam = spectral_lam_min(Q, nev=1)[0]
            print("  m=%2d  lam_min = %s   (%.0f s)"
                  % (m_, mp.nstr(lam, 9), time.time() - t0))
