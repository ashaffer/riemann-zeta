"""kink_enrichment.py — stress test for the kink-enriched-basis lemma
(PLAN-numerical-analysis.md, Lemma 2; independent numerical-analysis expert run).

QUESTION.  The Legendre ladder at L = 2.485 plunges spectrally to 3.86882e-10
by m = 24, then creeps algebraically to 3.56788e-10 at m = 64 (RESULTS.md,
day-two second session); the repo attributes the creep to interior derivative
kinks of the minimizer at x = +-(a - log p), a = L/4, inherited from the prime
shift operators.  If that local model is right, enriching the m = 24 Legendre
space with a few "snap" functions carrying exactly those corners must restore
the plunge: m = 24 + 4 should land at or below the plain m = 64 value.

PRE-REGISTERED PREDICTIONS (written before the run):
  Model K  (clean corner kinks: phi' jumps at +-(a - log p), rest analytic):
      lam(V2: 24+4) in [3.49, 3.52]e-10  (i.e. at the extrapolated operator
      value, BELOW plain m=64 = 3.5679e-10), and |lam(V3) - lam(V2)| <= 2e-12.
  Model LJ (log-regularized jump: the Euler-Lagrange equation with the
      log-symbol archimedean operator smooths a Heaviside source by 1/log only,
      so no piecewise-polynomial enrichment can restore spectral convergence):
      lam(V2: 24+4) in [3.55, 3.59]e-10 (marginal gain over plain m=24's creep
      position), creep resumes: lam(V3) - lam(V2) creep-sized (>= 3e-12).
  The measured creep exponent (decrement fits beta ~ 1-1.2, docstring of
  src/spectral_margins.py) favors Model LJ; the repo's kink phrasing favors K.
  Either outcome discriminates the local model — that is the point of the run.

VARIANTS (all even-parity block; the ground state is even — validated by V0):
  anchor: repo's spectral_form(2.485, 24) -> expect 3.86882e-10 (RESULTS.md).
  V0: plain even Legendre K=12 (== even block of m=24), own assembler,
      single-piece meshes.  Must reproduce the anchor to ~1e-15 rel.
  V0': same entries out of the ENRICHED (piecewise-mesh) assembly — an
      independent-quadrature cross-check of the piecewise machinery.
  V1: K=12 + corner snaps (|x|-t)_+ at t2 = log2 - a, t3 = log3 - a   (24+2)
  V2: K=12 + corners + quadratic snaps (|x|-t)_+^2 at t2, t3          (24+4)
  V3: K=16 + the same 4 snaps                                         (32+4)
  Diagnostics: Gram spectrum (conditioning), endpoint values phi(a), local
  jump probes at t3, snap coefficients, zero-side partial sum (must be <= lam).

MACHINERY.  Same x-space kernel and conventions as src/spectral_margins.py
(shift constant, kernel_tail, pole, primes n = 2,3), but assembled over
piecewise-polynomial bases: all overlaps S_ij(u) are computed by per-piece
Gauss-Legendre in x (exact: integrands are polynomials on each piece), and the
u-integral of [(G_ij - S_ij(u))/u] * u w(u) is split at every u where the hinge
configuration changes (differences of breakpoints), so the polynomial factor is
exact per piece and the analytic factor u w(u) converges geometrically
(nearest singularity i*pi; all pieces short).  Node counts chosen for exactness
of the polynomial factors (24-pt rules for K=12 products of degree <= 46;
48-pt for K=16).  Assembly dps 50 (+15 working guard), solve dps 40, exactly
like the repo ladder.

EXPECTED (measured 2026-07-26, this machine, single process, 139 s total;
full record in kink_enrichment.log next to this file):
  anchor  repo spectral_form(2.485, 24)      lam = 3.8688156e-10
  V0      plain even K=12 (own assembler)    lam = 3.8688156e-10
          |G - I|_max = 2.7e-51; V0 vs anchor rel diff 2.24e-21
  V0'     enriched-mesh entries, sub-block   cross-quadrature rel diff 2.2e-21
  V1      24+2 corners                       lam = 3.75432393e-10
  V2      24+4 corners+quads                 lam = 3.74025364e-10
  V3      32+4                               lam = 3.57091208e-10
          V3 - V2 = -1.693e-11 (creep-sized); Gram cond 8.0e7
  diag    phi(a) = 5.1264e-05, phi(0) = 1.6718; probe differences at t3
          scale like 2*eps*(-0.94): smooth slope, no visible finite jump
  oracle  2 SUM_40 |phihat(gamma)|^2 = 3.05456e-10 <= lam(V2)  OK
VERDICT: Model K REFUTED (pre-registered K interval [3.49, 3.52]e-10 missed
by 22 sigma-equivalents; V2 lands above even plain m=32).  The creep is NOT a
clean piecewise-polynomial corner: enrichment buys a constant factor
(31% of the m=24 residual, 57% of the m=32 residual vs the 3.50e-10
extrapolation), never a rate.  Consistent with the log-regularized-jump model
(Lemma 1); quantitatively the corner-capture is below even the pre-registered
LJ band [3.55, 3.59]e-10 at m=24.  phi(a) = 5.1e-5 confirms the amplitude
law J_n = (Lambda(n)/sqrt(n))|phi(a)| at the right order (creep-amplitude
arithmetic in the PLAN, Lemma 1(e)).
"""
import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', '..', 'src'))

import mpmath as mp                                        # noqa: E402
from spectral_margins import gl_nodes, legvals, spectral_form, \
    spectral_lam_min                                       # noqa: E402
from hp_margins import kernel_tail                         # noqa: E402

LOG = open(os.path.join(_HERE, 'kink_enrichment.log'), 'w')


def say(msg):
    print(msg)
    LOG.write(msg + '\n')
    LOG.flush()


# ---------------------------------------------------------------- basis
class EvenBasis:
    """Even piecewise-polynomial functions on [-a, a]:
    ('leg', k): orthonormal Legendre  sqrt((2k+1)/(2a)) P_k(x/a), k even;
    ('corner', t): (|x|-t)_+ / ||.||;   ('quad', t): (|x|-t)_+^2 / ||.||."""

    def __init__(self, a, leg_idx, snaps):
        self.a = a
        self.leg_idx = list(leg_idx)          # even Legendre degrees used
        self.maxdeg = max(leg_idx) if leg_idx else 0
        self.snaps = []                        # (kind, t, norm)
        for kind, t in snaps:
            if kind == 'corner':
                nrm = mp.sqrt(2 * (a - t) ** 3 / 3)
            else:                              # quad
                nrm = mp.sqrt(2 * (a - t) ** 5 / 5)
            self.snaps.append((kind, t, nrm))
            self.maxdeg = max(self.maxdeg, 2)
        self.N = len(self.leg_idx) + len(self.snaps)
        self.nk = [mp.sqrt(mp.mpf(2 * k + 1) / (2 * a)) for k in leg_idx]
        # positive interior breakpoints (snap kink locations)
        self.bp = sorted({t for _, t, _ in self.snaps})

    def evals(self, x):
        """Values of all N basis functions at x (mpf)."""
        P = legvals(self.maxdeg + 1, x / self.a)
        out = [self.nk[i] * P[k] for i, k in enumerate(self.leg_idx)]
        ax = abs(x)
        for kind, t, nrm in self.snaps:
            v = ax - t
            if v <= 0:
                out.append(mp.mpf(0))
            else:
                out.append((v if kind == 'corner' else v * v) / nrm)
        return out


def _pieces(lo, hi, cuts):
    """Sorted subintervals of [lo, hi] split at the interior cut points."""
    pts = [lo] + sorted(c for c in cuts if lo < c < hi) + [hi]
    return [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)
            if pts[i + 1] > pts[i]]


def S_matrix(B, u, nodes):
    """S_ij(u) = INT_{-a}^{a-u} f_i(x) f_j(x+u) dx (symmetric for even f).
    Piecewise GL in x: split at breakpoints of f_i and shifted ones of f_j."""
    a = B.a
    N = B.N
    S = [[mp.mpf(0)] * N for _ in range(N)]
    if u >= 2 * a:
        return S
    cuts = set()
    for t in B.bp:
        cuts.update((t, -t, t - u, -t - u))
    for lo, hi in _pieces(-a, a - u, cuts):
        c, h = (lo + hi) / 2, (hi - lo) / 2
        for x_, w_ in nodes:
            x = c + h * x_
            wt = w_ * h
            v1 = B.evals(x)
            v2 = B.evals(x + u)
            wv1 = [wt * v for v in v1]
            for i in range(N):
                a1 = wv1[i]
                Si = S[i]
                for j in range(i, N):
                    Si[j] += a1 * v2[j]
    for i in range(N):                    # upper triangle accumulated; mirror
        for j in range(i + 1, N):         # (S is symmetric for even bases)
            S[j][i] = S[i][j]
    return S


def assemble(L, B, dps=50, nmin_x=24, nmin_u=24):
    """Q, G (mp.matrix) for the truncated Weil form of zeta on basis B.
    Conventions == src/spectral_margins.spectral_form (q=1, even, pole on)."""
    with mp.workdps(dps + 15):
        a = mp.mpf(L) / 4
        assert abs(a - B.a) < mp.mpf(10) ** (-dps)
        N = B.N
        nodes_x = gl_nodes(nmin_x)
        nodes_u = gl_nodes(nmin_u)
        # --- u-mesh: hinge configuration changes at differences of breakpoints
        ext = set(B.bp) | {-t for t in B.bp} | {a, -a}
        ucuts = sorted({abs(b1 - b2) for b1 in ext for b2 in ext
                        if 0 < abs(b1 - b2) < 2 * a})
        G = S_matrix(B, mp.mpf(0), nodes_x)
        A = [[mp.mpf(0)] * N for _ in range(N)]
        for lo, hi in _pieces(mp.mpf(0), 2 * a, ucuts):
            c, h = (lo + hi) / 2, (hi - lo) / 2
            for xu, wu in nodes_u:
                u = c + h * xu
                S = S_matrix(B, u, nodes_x)
                guw = wu * h * u * mp.e ** (-u / 2) / (-mp.expm1(-2 * u))
                for i in range(N):
                    Si, Ai, Gi = S[i], A[i], G[i]
                    for j in range(i, N):
                        Ai[j] += guw * ((Gi[j] - Si[j]) / u)
        shift = mp.digamma(mp.mpf('0.25')) + 2 * kernel_tail(2 * a, mp.mpf('0.5')) \
            + mp.log(1 / mp.pi)
        Q = mp.matrix(N)
        for i in range(N):
            for j in range(i, N):
                Q[i, j] = Q[j, i] = 2 * A[i][j] + shift * G[i][j]
        # --- primes (n = 2, 3 participate at L = 2.485)
        for nn, p in ((2, 2), (3, 3)):
            ln = mp.log(nn)
            if 2 * ln < L:
                Sp = S_matrix(B, ln, nodes_x)
                w = 2 * mp.log(p) / mp.sqrt(nn)
                for i in range(N):
                    for j in range(N):
                        Q[i, j] -= w * Sp[i][j]
        # --- pole: even basis => INT f e^{x/2} = INT f e^{-x/2} =: vp
        vp = [mp.mpf(0)] * N
        for lo, hi in _pieces(-a, a, set(B.bp) | {-t for t in B.bp}):
            c, h = (lo + hi) / 2, (hi - lo) / 2
            for x_, w_ in nodes_x:
                x = c + h * x_
                wt = w_ * h * mp.e ** (x / 2)
                for i, v in enumerate(B.evals(x)):
                    vp[i] += wt * v
        for i in range(N):
            for j in range(N):
                Q[i, j] += 2 * vp[i] * vp[j]
        Gm = mp.matrix(N)
        for i in range(N):
            for j in range(N):
                Gm[i, j] = G[i][j]
        Qo, Go = mp.matrix(N), mp.matrix(N)
        with mp.workdps(dps):
            for i in range(N):
                for j in range(N):
                    Qo[i, j] = +Q[i, j]
                    Go[i, j] = +Gm[i, j]
    return Qo, Go


def gen_eig_bottom(Q, G, nev=2, dps=40, vectors=False):
    """Bottom generalized eigenpairs of (Q, G) via Cholesky + eigsy."""
    with mp.workdps(dps):
        N = Q.rows
        Lc = mp.cholesky(G)
        # M = Lc^{-1} Q Lc^{-T}
        Y = mp.matrix(N)
        for j in range(N):                       # solve Lc Y = Q (columns)
            for i in range(N):
                s = Q[i, j]
                for k in range(i):
                    s -= Lc[i, k] * Y[k, j]
                Y[i, j] = s / Lc[i, i]
        M = mp.matrix(N)
        for j in range(N):                       # solve Lc M^T = Y^T
            for i in range(N):
                s = Y[j, i]
                for k in range(i):
                    s -= Lc[i, k] * M[k, j]
                M[i, j] = s / Lc[i, i]
        for i in range(N):
            for j in range(i):
                s = (M[i, j] + M[j, i]) / 2
                M[i, j] = M[j, i] = s
        E, V = mp.eigsy(M)
        order = sorted(range(N), key=lambda i: E[i])
        lams = [E[i] for i in order[:nev]]
        if not vectors:
            return lams
        vecs = []
        for idx in order[:nev]:
            y = [V[i, idx] for i in range(N)]
            c = [mp.mpf(0)] * N
            for i in range(N - 1, -1, -1):       # solve Lc^T c = y
                s = y[i]
                for k in range(i + 1, N):
                    s -= Lc[k, i] * c[k]
                c[i] = s / Lc[i, i]
            vecs.append(c)
        return lams, vecs


def sub_eig(Q, G, idx, nev=2, dps=40, vectors=False):
    """Eigen of the principal submatrix on the index list idx."""
    n = len(idx)
    Qs, Gs = mp.matrix(n), mp.matrix(n)
    for a_, i in enumerate(idx):
        for b_, j in enumerate(idx):
            Qs[a_, b_] = Q[i, j]
            Gs[a_, b_] = G[i, j]
    return gen_eig_bottom(Qs, Gs, nev=nev, dps=dps, vectors=vectors)


def phi_eval(B, coeffs, x):
    return mp.fsum(c * v for c, v in zip(coeffs, B.evals(x)))


def zero_side_partial(B, coeffs, n_zeros=40, dps=25, nmin=96):
    """2 SUM_{k<=n_zeros} phihat(gamma_k)^2 (phi even => phihat real).
    A partial sum of squares: must be <= Q(phi)."""
    with mp.workdps(dps):
        a = B.a
        nodes = gl_nodes(nmin)
        cuts = set(B.bp) | {-t for t in B.bp}
        tot = mp.mpf(0)
        for kz in range(1, n_zeros + 1):
            g = mp.zetazero(kz).imag
            re = mp.mpf(0)
            for lo, hi in _pieces(-a, a, cuts):
                c, h = (lo + hi) / 2, (hi - lo) / 2
                for x_, w_ in nodes:
                    x = c + h * x_
                    re += w_ * h * phi_eval(B, coeffs, x) * mp.cos(g * x)
            tot += re * re
        return 2 * tot


# ---------------------------------------------------------------- run
if __name__ == '__main__':
    T0 = time.time()
    mp.mp.dps = 50
    L = 2.485
    a = mp.mpf(L) / 4
    t2 = mp.log(2) - a          # 0.0718971...  (= |a - log 2|)
    t3 = mp.log(3) - a          # 0.4773623...  (= |a - log 3|)
    say('kink_enrichment run, L = %.3f, a = %s' % (L, mp.nstr(a, 8)))
    say('kink locations t2 = %s, t3 = %s' % (mp.nstr(t2, 8), mp.nstr(t3, 8)))
    say('pre-registered: Model K  -> lam(V2) in [3.49, 3.52]e-10')
    say('                Model LJ -> lam(V2) in [3.55, 3.59]e-10')
    say('repo reference values: m=24 3.86882e-10 | m=32 3.66564e-10 | '
        'm=48 3.59571e-10 | m=64 3.56788e-10 | extrap 3.49-3.50e-10')

    # anchor: the repo's own ladder point
    t0 = time.time()
    Qr = spectral_form(L, 24)
    lam_anchor = spectral_lam_min(Qr, nev=1)[0]
    say('[anchor] repo spectral_form(2.485, 24): lam = %s  (%.0f s)'
        % (mp.nstr(lam_anchor, 9), time.time() - t0))

    # V0: plain even block K=12, own assembler (single-piece meshes)
    t0 = time.time()
    B0 = EvenBasis(a, range(0, 24, 2), [])
    Q0, G0 = assemble(L, B0)
    lam0 = gen_eig_bottom(Q0, G0, nev=1)[0]
    off = max(abs(G0[i, j] - (1 if i == j else 0))
              for i in range(B0.N) for j in range(B0.N))
    say('[V0] plain even K=12: lam = %s  |G - I|_max = %.1e  (%.0f s)'
        % (mp.nstr(lam0, 9), float(off), time.time() - t0))
    say('     V0 vs anchor rel diff = %.2e'
        % float(abs(lam0 - lam_anchor) / lam_anchor))

    # enriched assembly: K=12 + 4 snaps (V0', V1, V2 all from this matrix)
    t0 = time.time()
    snaps = [('corner', t2), ('corner', t3), ('quad', t2), ('quad', t3)]
    B2 = EvenBasis(a, range(0, 24, 2), snaps)
    Q2, G2 = assemble(L, B2)
    say('[assembly] enriched 12+4 done (%.0f s)' % (time.time() - t0))
    lam0p = sub_eig(Q2, G2, list(range(12)), nev=1)[0]
    say("[V0'] same entries from piecewise mesh: lam = %s  (cross-quadrature "
        'rel diff vs V0 = %.1e)' % (mp.nstr(lam0p, 9),
                                    float(abs(lam0p - lam0) / lam0)))
    lam1 = sub_eig(Q2, G2, list(range(14)), nev=1)[0]
    say('[V1] 24+2 corners: lam = %s' % mp.nstr(lam1, 9))
    (lam2s, vecs2) = sub_eig(Q2, G2, list(range(16)), nev=2, vectors=True)
    lam2 = lam2s[0]
    say('[V2] 24+4 (corners+quads): lam = %s   lam_2 = %s'
        % (mp.nstr(lam2, 9), mp.nstr(lam2s[1], 3)))
    with mp.workdps(40):
        eG = mp.eigsy(G2, eigvals_only=True)
        say('     Gram spectrum: min %.2e  max %.2e  (cond %.1e)'
            % (float(min(eG)), float(max(eG)), float(max(eG) / min(eG))))

    # diagnostics on the V2 minimizer
    c2 = vecs2[0]
    nrm = mp.sqrt(mp.fsum(c2[i] * mp.fsum(G2[i, j] * c2[j]
                  for j in range(B2.N)) for i in range(B2.N)))
    c2 = [c / nrm for c in c2]
    say('[diag] snap coefficients (unit-G-norm minimizer): '
        'corner(t2) %.3e  corner(t3) %.3e  quad(t2) %.3e  quad(t3) %.3e'
        % tuple(float(c2[12 + k]) for k in range(4)))
    say('[diag] endpoint and probe values: phi(a) = %.4e   phi(0) = %.4e'
        % (float(phi_eval(B2, c2, a)), float(phi_eval(B2, c2, mp.mpf(0)))))
    for eps in ('0.05', '0.02', '0.01'):
        e_ = mp.mpf(eps)
        dphi = phi_eval(B2, c2, t3 + e_) - phi_eval(B2, c2, t3 - e_)
        say('       phi(t3+%s) - phi(t3-%s) = %.4e' % (eps, eps, float(dphi)))
    t0 = time.time()
    zs = zero_side_partial(B2, c2, n_zeros=40)
    say('[oracle] 2 SUM_40 |phihat(gamma)|^2 = %s <= lam(V2) = %s : %s  (%.0f s)'
        % (mp.nstr(zs, 6), mp.nstr(lam2, 6),
           'OK' if zs <= lam2 else 'VIOLATION', time.time() - t0))

    # V3: K=16 + same snaps, if within budget
    if time.time() - T0 < 480:
        t0 = time.time()
        B3 = EvenBasis(a, range(0, 32, 2), snaps)
        Q3, G3 = assemble(L, B3, nmin_x=48, nmin_u=32)
        lam3 = gen_eig_bottom(Q3, G3, nev=1)[0]
        say('[V3] 32+4: lam = %s  (%.0f s)' % (mp.nstr(lam3, 9),
                                               time.time() - t0))
        say('     V3 - V2 = %.3e  (Model K: |.| <= 2e-12; LJ: creep-sized)'
            % float(lam3 - lam2))
    say('verdict inputs: plain m=64 = 3.56788e-10; extrapolated operator '
        'value 3.49-3.50e-10')
    say('total %.0f s' % (time.time() - T0))
    LOG.close()
