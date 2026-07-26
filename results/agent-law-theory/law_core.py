"""law_core.py — fast exact frame-form builder for the envelope-law experiments.

Same object as src/model_zeros.frame_form (the truncated frame form
Q = 2 SUM_{gamma <= Gcut} (v_re v_re^T + v_im v_im^T) in the orthonormal
Legendre basis on [-a, a], a = L/4), but the overlap vectors are computed
EXACTLY via spherical Bessel functions instead of Gauss-Legendre quadrature:

  v_k(gamma) = INT_{-a}^{a} b_k(x) e^{-i gamma x} dx
             = sqrt(a(2k+1)/2) * 2 (-i)^k j_k(gamma a),

  b_k(x) = sqrt((2k+1)/(2a)) P_k(x/a),   INT_{-1}^{1} P_k(u) e^{izu} du = 2 i^k j_k(z).

So v_re is supported on even k (sign (-1)^{k/2}) and v_im on odd k
(sign -(-1)^{(k-1)/2}); Q is parity-block-diagonal and we eigensolve the
two (m/2)x(m/2) blocks separately.

j_k(z): the top two orders from mp.besselj(k+1/2, z) (arbitrary precision),
then exact downward recurrence j_{k-1} = (2k+1)/z j_k - j_{k+1} (stable
downward).  Validation against the quadrature builder and against the
EXPECTED numbers of src/model_zeros.py is in validate.py.

Truncation semantics (inherited): deleting gamma > Gcut deletes positive
rank-ones, so every lam_min reported here is a LOWER bound of the
Gcut -> infinity frame bound, increasing in Gcut; and each value is a
Galerkin (Rayleigh-Ritz) minimum over the m-dimensional Legendre space,
i.e. an UPPER bound in m for the same Gcut-truncated operator.
"""
import os
import sys
import time
import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_HERE, "..", "..", "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)


def sph_jn_list(kmax, z, prec_dps):
    """[j_0(z), ..., j_{kmax}(z)] at working precision.  z > 0 mpf."""
    with mp.workdps(prec_dps):
        z = mp.mpf(z)
        if z == 0:
            return [mp.mpf(1) if k == 0 else mp.mpf(0) for k in range(kmax + 1)]
        # top two orders exactly, then downward recurrence
        fac = mp.sqrt(mp.pi / (2 * z))
        jtop = fac * mp.besselj(mp.mpf(2 * kmax + 3) / 2, z)   # j_{kmax+1}
        jtop1 = fac * mp.besselj(mp.mpf(2 * kmax + 1) / 2, z)  # j_{kmax}
        out = [mp.mpf(0)] * (kmax + 1)
        jp1, jk = jtop, jtop1
        out[kmax] = jk
        for k in range(kmax, 0, -1):
            jm1 = (2 * k + 1) / z * jk - jp1
            jp1, jk = jk, jm1
            out[k - 1] = jk
        return out


def frame_blocks(gammas, L, m, dps=50):
    """Even/odd parity blocks (Qe, Qo) of the frame form
    Q = 2 SUM_gamma (v_re v_re^T + v_im v_im^T), orthonormal Legendre basis.
    Returns (Qe, Qo) as mp.matrix at dps."""
    wd = dps + 10
    with mp.workdps(wd):
        a = mp.mpf(L) / 4
        ck = [mp.sqrt(a * (2 * k + 1) / 2) for k in range(m)]
        ke = list(range(0, m, 2))
        ko = list(range(1, m, 2))
        ne, no = len(ke), len(ko)
        Qe = [[mp.mpf(0)] * ne for _ in range(ne)]
        Qo = [[mp.mpf(0)] * no for _ in range(no)]
        for g in gammas:
            z = mp.mpf(g) * a
            j = sph_jn_list(m - 1, z, wd)
            # v_re[k] = 2 c_k (-1)^{k/2} j_k   (k even)
            # v_im[k] = -2 c_k (-1)^{(k-1)/2} j_k (k odd); signs cancel in v v^T
            ve = [2 * ck[k] * j[k] * (1 if (k // 2) % 2 == 0 else -1) for k in ke]
            vo = [2 * ck[k] * j[k] * (1 if ((k - 1) // 2) % 2 == 0 else -1) for k in ko]
            for i in range(ne):
                vei = 2 * ve[i]
                row = Qe[i]
                for jj in range(i, ne):
                    row[jj] += vei * ve[jj]
            for i in range(no):
                voi = 2 * vo[i]
                row = Qo[i]
                for jj in range(i, no):
                    row[jj] += voi * vo[jj]
        Me = mp.matrix(ne)
        Mo = mp.matrix(no)
        with mp.workdps(dps):
            for i in range(ne):
                for jj in range(i, ne):
                    Me[i, jj] = +Qe[i][jj]
                    Me[jj, i] = Me[i, jj]
            for i in range(no):
                for jj in range(i, no):
                    Mo[i, jj] = +Qo[i][jj]
                    Mo[jj, i] = Mo[i, jj]
    return Me, Mo


def lam_min_frame(gammas, L, m, dps=50, solve_dps=None, nev=1):
    """Smallest nev eigenvalues (across both parity blocks) of the truncated
    frame form.  Returns sorted list of mpf."""
    solve_dps = solve_dps or dps
    Qe, Qo = frame_blocks(gammas, L, m, dps=dps)
    lams = []
    with mp.workdps(solve_dps):
        for Q in (Qe, Qo):
            E = mp.eigsy(Q, eigvals_only=True)
            lams.extend([E[i] for i in range(Q.rows)])
    lams.sort()
    return lams[:nev]


# ---------------- model zero sequences ----------------

def staircase_zeros(K, alpha='1', beta='1', dps=50, gmax=None):
    """First K solutions of N_{alpha,beta}(g) = k - 1/2 with
    N_{a,b}(T) = alpha (T/2pi) ln(T/(2 pi beta e)) + 7/8.
    alpha=beta=1 reproduces model_zeros.smooth_zeros.  If gmax is given,
    stop at the first zero exceeding gmax (returns fewer than K)."""
    with mp.workdps(dps):
        al = mp.mpf(alpha)
        be = mp.mpf(beta)
        tp = 2 * mp.pi
        out = []
        g = tp * be * mp.e * mp.mpf('1.05')  # start just above density zero
        for k in range(1, K + 1):
            target = k - mp.mpf('0.5') - mp.mpf('0.875')
            for _ in range(80):
                lg = mp.log(g / (tp * be))
                f = al * g / tp * (lg - 1) - target
                fp = al * lg / tp
                if fp <= 0:
                    g = tp * be * mp.e
                    continue
                step = f / fp
                gn = g - step
                if gn <= tp * be:          # keep above the density zero
                    gn = (g + tp * be) / 2
                g = gn
                if abs(step) < mp.mpf('1e-30'):
                    break
            out.append(+g)
            if gmax is not None and g > gmax:
                break
            g = g + tp / (al * mp.log(g / (tp * be)))
        return out


def ap_zeros(s0, gcut, offset='0.5'):
    """Arithmetic progression gamma_k = s0 (k + offset), k = 0, 1, ...,
    up to gcut."""
    s0 = mp.mpf(s0)
    off = mp.mpf(offset)
    out = []
    k = 0
    while True:
        g = s0 * (k + off)
        if g > gcut:
            break
        out.append(g)
        k += 1
    return out


def true_zeros_cached(K, path=os.path.join(_HERE, "data", "zeta_zeros.txt"),
                      dps=40):
    """First K zeta-zero ordinates, cached to disk at 40 digits."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    have = []
    if os.path.exists(path):
        with open(path) as f:
            have = [line.strip() for line in f if line.strip()]
    if len(have) < K:
        with mp.workdps(dps + 10):
            for k in range(len(have) + 1, K + 1):
                have.append(mp.nstr(mp.zetazero(k).imag, dps))
        with open(path, "w") as f:
            f.write("\n".join(have) + "\n")
    return [mp.mpf(s) for s in have[:K]]


if __name__ == "__main__":
    mp.mp.dps = 50
    t0 = time.time()
    zs = staircase_zeros(12)
    print("staircase alpha=beta=1 first zeros:",
          [mp.nstr(z, 8) for z in zs[:5]], "(%.1fs)" % (time.time() - t0))
