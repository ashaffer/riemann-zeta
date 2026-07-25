"""certified_spectral.py — interval certificates in the spectral (Legendre) basis.

certified_margins.py certifies the HAT-basis ladder; this module certifies the
SPECTRAL ladder of spectral_margins.py — the one that reaches the operator-level
margins — with the same trust base (mpmath.iv enclosures, 220-bit endpoints).

Structure.  Work in the UNNORMALIZED Legendre basis b_k(x) = P_k(x/a), a = L/4
rational: the Gram matrix is exactly diag(2a/(2k+1)) (rational), and the shifted
overlap T_kj(u) = INT b_k(x) b_j(x+u) dx equals a * F_kj(u/a) where

  F_kj(v) = INT_{-1}^{1-v} P_k(t) P_j(t+v) dt

is a UNIVERSAL polynomial in v with exact rational coefficients (degree k+j+1),
computed once in Fraction arithmetic and cached — independent of L.  There are
no hinges (unlike hats), so on [0, 2a]:

  arch_kj = psi(s0) G_kj + 2 INT_0^{2a} H(u) w(u) du + 2 G_kj INT_{2a}^inf w,
  H(u) = G_kj - a F_kj(u/a),  H(0) = 0 exactly,  w(u) = e^{-s0 u}/(1-e^{-2u}).

The kernel splits w = 1/(2u) + g(u): the 1/(2u) part integrates H to an exact
rational (H/u is a polynomial); the g part is SUM_r g_r INT H(u) u^r du against
precomputed rational moments, with the rigorous geometric remainder
|g_r| <= 250/pi^{r+1} (from |c_j| <= 4 e^{(2-s0)pi}/pi^j <= 500/pi^j).  The pole
vectors are 2a i_k(a/2) with i_k the modified spherical Bessel function evaluated
by its ALL-POSITIVE-TERMS series with a rigorous geometric tail; prime terms
evaluate the exact F polynomials at iv.log points.  Parity gives exact zeros for
k+j odd throughout (including the pole).  Lower bound: interval Cholesky of
Q - beta G.  Upper bound: interval Rayleigh quotient of the rationalized spectral
minimizer.  Certifying (Q_un, G_un) certifies the same generalized eigenvalue
that spectral_margins computes in the orthonormal basis.

EXPECTED (measured July 25, 2026, this machine):
  F-polynomial cross-check vs the GL overlap engine: exact agreement (0.0)
  zeta, L = 497/200, spectral m = 24:
      CERTIFIED 3.86870000e-10 < lam_min <= 3.86881560e-10   (18 s)
  zeta, L = 749/250,  spectral m = 48:
      CERTIFIED 4.34600000e-15 < lam_min <= 4.34621580e-15   (86 s)
  zeta, L = 711/200,  spectral m = 40:
      CERTIFIED 1.79970000e-20 < lam_min <= 1.79972291e-20   (33 s)
  (interval-certified positivity of the truncated Weil form at the 1e-10,
   1e-15, and 1e-20 scales — the deep end of the measured f(p) ladder; with
   certified_margins.py the certified ladder spans 3.8e-5 down to 1.8e-20,
   fifteen orders of magnitude.  The certified values are Galerkin minima,
   hence upper bounds on the operator margins of PROGRAM.md 2.15's law.
   Development note: an off-by-one power ladder in the H coefficients was
   caught before any claim by the interval Rayleigh check returning an
   impossible negative upper bound — the layered discipline at work.)
"""
from fractions import Fraction
import mpmath as mp
from mpmath import iv
from weil_core import PRIME_POWERS, kron
from certified_margins import F2iv, g_series, kernel_tail_iv, iv_cholesky_pd

iv.prec = 220

_LEG = [[Fraction(1)], [Fraction(0), Fraction(1)]]


def leg(k):
    """Monomial coefficients of P_k, exact."""
    while len(_LEG) <= k:
        n = len(_LEG) - 1
        Pn, Pm = _LEG[n], _LEG[n - 1]
        new = [Fraction(0)] * (n + 2)
        for i, c in enumerate(Pn):
            new[i + 1] += Fraction(2 * n + 1, n + 1) * c
        for i, c in enumerate(Pm):
            new[i] -= Fraction(n, n + 1) * c
        _LEG.append(new)
    return _LEG[k]


_BINOM = [[1]]


def binom(n, q):
    while len(_BINOM) <= n:
        prev = _BINOM[-1]
        _BINOM.append([1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1])
    return _BINOM[n][q]


_FCACHE = {}


def F_poly(k, j):
    """Exact Fraction coefficients (in v) of INT_{-1}^{1-v} P_k(t) P_j(t+v) dt,
    valid for v in [0, 2].  Requires nothing of parity; cached; F_kj = F_jk for
    k+j even (the only case used)."""
    if k > j:
        k, j = j, k
    if (k, j) in _FCACHE:
        return _FCACHE[(k, j)]
    Pk, Pj = leg(k), leg(j)
    # B[p][q] = coeff of v^p t^q in P_j(t+v) P_k(t)
    deg_t = k + j
    B = [[Fraction(0)] * (deg_t + 1) for _ in range(j + 1)]
    for i, cj in enumerate(Pj):
        if cj:
            for q in range(i + 1):
                cvq = cj * binom(i, q)          # v^{i-q} t^q
                p = i - q
                for r, ck in enumerate(Pk):
                    if ck:
                        B[p][q + r] += cvq * ck
    # integrate t over [-1, 1-v]
    F = [Fraction(0)] * (k + j + 2)
    for p in range(j + 1):
        row = B[p]
        for q in range(deg_t + 1):
            c = row[q]
            if not c:
                continue
            c1 = c / (q + 1)
            # + (1-v)^{q+1} term
            for s in range(q + 2):
                F[p + s] += c1 * binom(q + 1, s) * (-1) ** s
            # - (-1)^{q+1} term
            F[p] -= c1 * (-1) ** (q + 1)
    while len(F) > 1 and F[-1] == 0:
        F.pop()
    _FCACHE[(k, j)] = F
    return F


def ik_iv(k, z):
    """Modified spherical Bessel i_k(z), z a positive Fraction, via the
    all-positive series i_k = SUM_s z^{k+2s} / (2^s s! (2k+2s+1)!!), with a
    rigorous geometric tail."""
    ziv = F2iv(z)
    dfac = Fraction(1)
    for t in range(1, 2 * k + 2, 2):
        dfac *= t
    term = ziv ** k / F2iv(dfac)
    tot = term
    s = 0
    while True:
        s += 1
        term = term * ziv * ziv / F2iv(2 * s * (2 * k + 2 * s + 1))
        tot += term
        ratio = ziv * ziv / F2iv(2 * (s + 1) * (2 * k + 2 * s + 3))
        if float(term.b) < 1e-70:
            return tot + iv.mpf([0, 1]) * term * ratio / (1 - ratio)


def certified_spectral_form(L, m, q=1, D=1, parity='even', N=400):
    """Q (iv, unnormalized Legendre basis) and G (list of rational diagonal
    entries) for the truncated Weil form at rational L."""
    L = Fraction(L)
    a = L / 4
    two_a = 2 * a
    s_num, s_den = (1, 2) if parity == 'even' else (3, 2)
    g, _ = g_series(N, s_num, s_den)
    # kernel moments  M_s = INT_0^{2a} u^s G_N(u) du,  s = 1 .. 2m+2  (exact)
    smax = 2 * m + 2
    pow2a = [Fraction(1)]
    for _ in range(smax + N + 3):
        pow2a.append(pow2a[-1] * two_a)
    Mom = [Fraction(0)] * (smax + 1)
    for s in range(1, smax + 1):
        acc = Fraction(0)
        for r in range(N + 1):
            acc += g[r] * pow2a[s + r + 1] / (s + r + 1)
        Mom[s] = acc
    # rigorous series remainder scale: |g(u) - G_N(u)| <= rN on [0, 2a]
    ratio = F2iv(two_a) / iv.pi
    rN = F2iv(250) / iv.pi * ratio ** (N + 1) / (1 - ratio)
    psi0 = -iv.euler - 3 * iv.log(iv.mpf(2)) + (iv.pi / 2 if parity == 'odd' else -iv.pi / 2)
    tail = kernel_tail_iv(two_a, s_num, s_den)
    lq = iv.log(iv.mpf(q)) - iv.log(iv.pi)
    G = [two_a / (2 * k + 1) for k in range(m)]
    # prime data
    pr = []
    for nn, p in PRIME_POWERS:
        c = 1 if q == 1 else kron(D, nn)
        if c and mp.log(nn) < float(L) / 2:
            w = 2 * iv.log(iv.mpf(p)) * c / iv.sqrt(iv.mpf(nn))
            pr.append((iv.log(iv.mpf(nn)) / F2iv(a), w))
    Q = [[iv.mpf(0)] * m for _ in range(m)]
    for k in range(m):
        for j in range(k, m):
            if (k + j) % 2:
                continue
            F = F_poly(k, j)
            Gkj = G[k] if k == j else Fraction(0)
            # H coefficients: h_p = -f_p a^{1-p}, p >= 1  (h_0 = 0 exactly)
            h = [Fraction(0)] * len(F)
            ap = Fraction(1)                        # a^{1-p} = a^0 at p = 1
            for p in range(1, len(F)):
                h[p] = -F[p] * ap
                ap /= a
            I1 = sum(h[p] * pow2a[p] / p for p in range(1, len(h))) / 2
            I2 = sum(h[p] * Mom[p] for p in range(1, len(h)))
            Hb = sum(abs(h[p]) * pow2a[p + 1] / (p + 1) for p in range(1, len(h)))
            ent = psi0 * F2iv(Gkj) + 2 * (F2iv(I1) + F2iv(I2)) \
                + iv.mpf([-1, 1]) * 2 * rN * F2iv(Hb) + 2 * F2iv(Gkj) * tail \
                + lq * F2iv(Gkj)
            # primes
            for v0, w in pr:
                Fv = iv.mpf(0)
                for c in reversed(F):
                    Fv = Fv * v0 + F2iv(c)
                ent = ent - w * F2iv(a) * Fv
            Q[k][j] = ent
            Q[j][k] = ent
    if q == 1:
        vp = [2 * F2iv(a) * ik_iv(k, a / 2) for k in range(m)]
        for k in range(m):
            for j in range(m):
                if (k + j) % 2 == 0:
                    sgn = (-1) ** j + (-1) ** k          # = +-2
                    Q[k][j] = Q[k][j] + vp[k] * vp[j] * (sgn // 1)
    return Q, G


def certify_spectral(L, m, beta, q=1, D=1, parity='even', ray_vec=None, N=400):
    L = Fraction(L)
    beta = Fraction(beta)
    Q, G = certified_spectral_form(L, m, q=q, D=D, parity=parity, N=N)
    M = [[Q[i][j] - (F2iv(beta * G[i]) if i == j else 0) for j in range(m)]
         for i in range(m)]
    ok = iv_cholesky_pd(M)
    ub = None
    if ray_vec is not None:
        c = [F2iv(Fraction(x).limit_denominator(10 ** 12)) for x in ray_vec]
        num = iv.mpf(0)
        den = iv.mpf(0)
        for i in range(m):
            for j in range(m):
                num += c[i] * Q[i][j] * c[j]
            den += c[i] * c[i] * F2iv(G[i])
        ub = num / den
    return ok, ub


if __name__ == "__main__":
    import time
    from spectral_margins import spectral_form, spectral_lam_min
    # cross-check: exact F polynomial vs the GL overlap engine (orthonormal S)
    mp.mp.dps = 50
    a_ = mp.mpf('0.6')
    from spectral_margins import overlap_S, gl_nodes
    nk = [mp.sqrt(mp.mpf(2 * kk + 1) / (2 * a_)) for kk in range(8)]
    S = overlap_S(8, a_, mp.mpf('0.3'), gl_nodes(96), nk)
    for (kk, jj) in ((2, 4), (5, 5), (0, 6)):
        F = F_poly(kk, jj)
        v = mp.mpf('0.3') / a_
        Fv = mp.mpf(0)
        for c in reversed(F):
            Fv = Fv * v + mp.mpf(c.numerator) / c.denominator
        pred = float(nk[kk] * nk[jj] * a_ * Fv)
        print("F cross-check (k,j)=(%d,%d): |exact - GL| = %.1e"
              % (kk, jj, abs(pred - float(S[kk][jj]))))
    # certificates at the deep end of the ladder
    cases = [
        ("zeta L=497/200 m=24", Fraction(497, 200), 24, Fraction(38687, 10 ** 14)),
        ("zeta L=749/250 m=48", Fraction(749, 250), 48, Fraction(4346, 10 ** 18)),
        ("zeta L=711/200 m=40", Fraction(711, 200), 40, Fraction(17997, 10 ** 24)),
    ]
    for tag, Lc, m_, beta in cases:
        t0 = time.time()
        Qs = spectral_form(float(Lc), m_)
        lams, vecs = spectral_lam_min(Qs, nev=1, vectors=True)
        aa = float(Lc) / 4
        ray = [float(vecs[0][kk]) * (float(mp.sqrt((2 * kk + 1) / (2 * aa))))
               for kk in range(m_)]
        ok, ub = certify_spectral(Lc, m_, beta, ray_vec=ray)
        print("%s: CERTIFIED %.8e < lam_min <= %.8e : %s  (%.0f s)"
              % (tag, float(beta), float(ub.b), ok, time.time() - t0))
