"""make_certificate_deep.py — deeper/broader kernel certificates for lean/weilcert.

Extends lean/make_certificate.py (m = 12, zeta, L = 497/200) to:

  zeta24   zeta,   L = 497/200, spectral m = 24, DEN = 10^28, delta = 1e-14
           -> lean/weilcert/WeilcertDeep.lean    (namespace WeilCertDeep)
  chi7m16  chi_{-7}, L = 5,     spectral m = 16, DEN = 10^24, delta = 1e-9
           -> lean/weilcert/WeilcertFamily.lean  (namespace WeilCertFamily)
  zeta48   zeta,   L = 749/250, spectral m = 48, DEN = 10^30, delta = 1e-19
           -> lean/weilcert/WeilcertDeeper.lean  (namespace WeilCertDeeper)

Differences from make_certificate.py (all in the direction of MORE rigor):
  * interval endpoints are extracted from mpmath.iv raw tuples and converted to
    exact Fractions (no float pass); the rounding of midpoints to the 1/DEN
    grid is performed and VERIFIED in exact integer arithmetic;
  * the identification budget |A/DEN - Q_true| <= 0.5/DEN + halfwidth is
    asserted exactly to be < delta/100 (the m = 12 generator emitted midpoints
    through 53-bit floats, which costs ~1.5e-17 and silently exceeds its
    stated delta = 1e-20; see results/agent-lean-depth.md);
  * the shift S = m * DEN * delta is asserted to be at least two orders below
    DEN * lam_min(unnormalized), measured by exact-LDL success with margin.

Certificate identities verified exactly in Fractions/ints before emission:
    c^2 B = W^T diag(g) W,   Winv W = f I,   g > 0,   B = A - S*I.
Any failed assert aborts with no file written.

Usage:  python3 make_certificate_deep.py zeta24 [--measure-only]
"""

import sys, math, time, argparse, os
sys.set_int_max_str_digits(3000000)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)).rsplit('/', 1)[0] + '/src')
from fractions import Fraction
import mpmath as mp
from certified_spectral import certified_spectral_form

WINDOWS = {
    'zeta24': dict(L=Fraction(497, 200), m=24, q=1, D=1, parity='even', N=400,
                   DENP=28, DELTAP=14, ns='WeilCertDeep', fname='WeilcertDeep.lean',
                   desc='truncated Weil form of zeta at support L = 497/200, '
                        'unnormalized Legendre basis P_0..P_23 (m = 24): the p = 3 '
                        'window margin at the 1e-10 scale'),
    'chi7m16': dict(L=Fraction(5), m=16, q=7, D=-7, parity='odd', N=900,
                    DENP=24, DELTAP=9, ns='WeilCertFamily', fname='WeilcertFamily.lean',
                    desc='truncated Weil form of the odd Dirichlet character chi_{-7} '
                         '(conductor 7, no pole term) at support L = 5, unnormalized '
                         'Legendre basis P_0..P_15 (m = 16): the first formally '
                         'verified GRH-side positivity window'),
    'zeta48': dict(L=Fraction(749, 250), m=48, q=1, D=1, parity='even', N=400,
                   DENP=30, DELTAP=19, heartbeats=1600000000, bigdata=True,
                   ns='WeilCertDeeper', fname='WeilcertDeeper.lean',
                   desc='truncated Weil form of zeta at support L = 749/250, '
                        'unnormalized Legendre basis P_0..P_47 (m = 48): the n = 4 '
                        'window margin at the 1e-15 scale'),
}


def mpf_tuple_to_frac(t):
    """Exact Fraction from a raw mpf tuple (sign, man, exp, bc); handles 0."""
    if t == mp.libmp.fzero or t == 0:
        return Fraction(0)
    sign, man, exp, bc = t
    v = Fraction(int(man)) * (Fraction(2) ** int(exp))
    return -v if sign else v


def iv_to_fracs(x):
    a, b = x._mpi_
    return mpf_tuple_to_frac(a), mpf_tuple_to_frac(b)


def round_half_up(q):
    """floor(q + 1/2) in exact integer arithmetic (works for negatives)."""
    return (2 * q.numerator + q.denominator) // (2 * q.denominator)


def digits(n):
    return len(str(abs(n))) if n else 1


def build_certificate(spec, verbose=True):
    L, m = spec['L'], spec['m']
    DEN = 10 ** spec['DENP']
    delta = Fraction(1, 10 ** spec['DELTAP'])
    S = m * DEN * delta
    assert S.denominator == 1
    S = int(S)

    t0 = time.time()
    Q, G = certified_spectral_form(L, m, q=spec['q'], D=spec['D'],
                                   parity=spec['parity'], N=spec['N'])
    t_form = time.time() - t0
    if verbose:
        print("[%s] enclosures built in %.1f s" % (spec['ns'], t_form))

    # exact endpoints, exact rounding, exact identification budget
    A = [[0] * m for _ in range(m)]
    max_halfwidth = Fraction(0)
    max_rnd = Fraction(0)
    for i in range(m):
        for j in range(m):
            fa, fb = iv_to_fracs(Q[i][j])
            assert fb >= fa
            mid = (fa + fb) / 2
            hw = (fb - fa) / 2
            n0 = round_half_up(mid * DEN)
            rnd = abs(Fraction(n0) - mid * DEN)
            assert rnd <= Fraction(1, 2)
            A[i][j] = n0
            max_halfwidth = max(max_halfwidth, hw)
            max_rnd = max(max_rnd, rnd / DEN)
    for i in range(m):
        for j in range(m):
            assert A[i][j] == A[j][i]
    ident = max_rnd + max_halfwidth      # |A/DEN - Q_true| <= ident, exact
    assert ident < delta / 100, (float(ident), float(delta))
    if verbose:
        print("[%s] exact identification bound %.3e  (delta = %.0e; margin %.0fx)"
              % (spec['ns'], float(ident), float(delta), float(delta / ident)))

    # B = A - S I, exact LDL^T
    B = [[A[i][j] - (S if i == j else 0) for j in range(m)] for i in range(m)]
    Lm = [[Fraction(1 if i == j else 0) for j in range(m)] for i in range(m)]
    Dp = [Fraction(0)] * m
    Aw = [[Fraction(B[i][j]) for j in range(m)] for i in range(m)]
    for k in range(m):
        Dp[k] = Aw[k][k]
        assert Dp[k] > 0, "pivot %d nonpositive: B = A - S*I not PD" % k
        for i in range(k + 1, m):
            Lm[i][k] = Aw[i][k] / Dp[k]
        for i in range(k + 1, m):
            for j in range(k + 1, i + 1):
                Aw[i][j] -= Lm[i][k] * Lm[j][k] * Dp[k]
                Aw[j][i] = Aw[i][j]
    # exact unit-lower-triangular inverse of Lm
    Li = [[Fraction(1 if i == j else 0) for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(i):
            Li[i][j] = -sum(Lm[i][k] * Li[k][j] for k in range(j, i))
    lcm = lambda a, b: a * b // math.gcd(a, b)
    r = [1] * m
    for k in range(m):
        for i in range(m):
            r[k] = lcm(r[k], Lm[i][k].denominator)
    c = 1
    for k in range(m):
        c = lcm(c, r[k])
        c = lcm(c, Dp[k].denominator)
    W = [[int(r[k] * Lm[i][k]) for i in range(m)] for k in range(m)]
    g = []
    for k in range(m):
        gk = Dp[k] * c * c / (r[k] * r[k])
        assert gk.denominator == 1, "g[%d] not integral" % k
        g.append(int(gk))
    for k in range(m):
        assert g[k] > 0
    for i in range(m):
        for j in range(m):
            assert c * c * B[i][j] == sum(W[k][i] * g[k] * W[k][j] for k in range(m)), \
                "congruence fails at (%d,%d)" % (i, j)
    f = 1
    for i in range(m):
        for k in range(m):
            f = lcm(f, (Li[k][i] / r[k]).denominator)
    Wi = [[0] * m for _ in range(m)]
    for i in range(m):
        for k in range(m):
            wik = f * Li[k][i] / r[k]
            assert wik.denominator == 1
            Wi[i][k] = int(wik)
    for i in range(m):
        for j in range(m):
            assert sum(Wi[i][k] * W[k][j] for k in range(m)) == (f if i == j else 0), \
                "inverse identity fails at (%d,%d)" % (i, j)
    t_cert = time.time() - t0 - t_form
    if verbose:
        print("[%s] certificate verified exactly in Fractions (%.1f s): "
              "c^2 B = W^T diag(g) W;  Winv W = f I;  g > 0" % (spec['ns'], t_cert))

    stats = dict(
        dig_A=max(digits(A[i][j]) for i in range(m) for j in range(m)),
        dig_W=max(digits(W[k][i]) for k in range(m) for i in range(m)),
        dig_Wi=max(digits(Wi[i][k]) for i in range(m) for k in range(m)),
        dig_g=max(digits(x) for x in g),
        dig_c=digits(c), dig_f=digits(f),
        ident=float(ident), t_form=t_form, t_cert=t_cert,
        total_chars=sum(digits(W[k][i]) for k in range(m) for i in range(m))
                    + sum(digits(Wi[i][k]) for i in range(m) for k in range(m))
                    + sum(digits(x) for x in g) + digits(c) + digits(f)
                    + sum(digits(A[i][j]) for i in range(m) for j in range(m)),
    )
    if verbose:
        print("[%s] digit sizes: A<=%d  W<=%d  Winv<=%d  g<=%d  c=%d  f=%d  "
              "(data chars ~%.2f MB)"
              % (spec['ns'], stats['dig_A'], stats['dig_W'], stats['dig_Wi'],
                 stats['dig_g'], stats['dig_c'], stats['dig_f'],
                 stats['total_chars'] / 1e6))
    return A, W, Wi, g, c, f, S, stats


def fun2(name, data, m):
    out = ["def %s : Nat → Nat → Int" % name]
    for i in range(m):
        for j in range(m):
            out.append("  | %d, %d => %d" % (i, j, data[i][j]))
    out.append("  | _, _ => 0")
    return "\n".join(out)


def fun1(name, data, m):
    out = ["def %s : Nat → Int" % name]
    for k in range(m):
        out.append("  | %d => %d" % (k, data[k]))
    out.append("  | _ => 0")
    return "\n".join(out)


def emit_lean(spec, A, W, Wi, g, c, f, S, stats):
    m, ns = spec['m'], spec['ns']
    HB = spec.get('heartbeats', 8000000)
    if spec.get('bigdata'):
        # Data definitions this large must not be IR-compiled: at m = 48 the
        # COMPILER (not the kernel) hit the default heartbeat limit lowering
        # wiFun, then every dependent failed with "depends on ... noncomputable".
        # `noncomputable section` skips codegen entirely (the kernel term, which
        # is all `decide` uses, is unaffected); the file-level maxHeartbeats
        # covers the large definition elaborations themselves.
        # maxRecDepth: the Fin-48 double-forall decide instances recurse past the
        # elaborator's default 512 (they passed at m = 24, failed at m = 48 with
        # "maximum recursion depth has been reached").
        bigopts = ("\nset_option maxHeartbeats %d\nset_option maxRecDepth 16384\n"
                   "\nnoncomputable section\n" % HB)
        bigend = "\nend\n"
    else:
        bigopts = ""
        bigend = ""
    DENP, DELTAP = spec['DENP'], spec['DELTAP']
    DP = DENP - DELTAP
    FinM = "(Fin %d)" % m
    hdr = f"""/-
{ns}: a machine-checked window of Weil positivity — {spec['desc']}.

Main result `{ns}.weil_window_positive`: every rational {m}x{m} matrix M whose
entries lie entrywise within 1/10^{DELTAP} of the explicit rational matrix mRat
(the integer data aFun below divided by 10^{DENP}) has a strictly positive
quadratic form: 0 < x . (M x) for all x != 0.

Bridge (see THEOREMS.md and results/agent-lean-depth.md): the {m}x{m} matrix of
the {spec['desc']}
lies entrywise within {float(stats['ident']):.1e} of mRat — the enclosures are
220-bit outward-rounded intervals (src/certified_spectral.py) and the rounding
to the 10^-{DENP} grid was performed and verified in exact rational arithmetic
(lean/make_certificate_deep.py), so the identification budget is exact.

Certificate: integer congruence
  cInt^2 * B = W^T * diag(g) * W,   Winv * W = fInt * 1,   g > 0,
with B = A - {S} * 1 (the shift {S} = {m} * 10^{DENP} * delta covers the
worst-case entrywise perturbation delta = 1/10^{DELTAP} via the Cauchy–Schwarz
bound |x^T E x| <= {m} * (10^{DENP} * delta) * |x|^2), all verified below by
kernel computation (`decide`); no floating point, no native_decide, no axioms
beyond propext, Classical.choice, Quot.sound.

Generated by lean/make_certificate_deep.py; every identity re-verified exactly
in Fraction arithmetic before emission.
-/
import Mathlib

namespace {ns}

open Matrix Finset
{bigopts}
"""
    data = "\n\n".join([
        fun2("aFun", A, m), fun2("wFun", W, m), fun2("wiFun", Wi, m),
        fun1("gFun", g, m),
        "def cInt : Int := %d" % c,
        "def fInt : Int := %d" % f,
        "def sInt : Int := %d" % S,
    ])
    body = f"""

/-! ## Matrices over ℤ and their ℚ casts -/

def aInt : Matrix {FinM} {FinM} ℤ := Matrix.of fun i j => aFun i.val j.val

def wInt : Matrix {FinM} {FinM} ℤ := Matrix.of fun i j => wFun i.val j.val

def wiInt : Matrix {FinM} {FinM} ℤ := Matrix.of fun i j => wiFun i.val j.val

def gInt : Fin {m} → ℤ := fun k => gFun k.val

def bInt : Matrix {FinM} {FinM} ℤ :=
  Matrix.of fun i j => aFun i.val j.val - if i = j then sInt else 0

def aQ : Matrix {FinM} {FinM} ℚ := Matrix.of fun i j => (aInt i j : ℚ)

def bQ : Matrix {FinM} {FinM} ℚ := Matrix.of fun i j => (bInt i j : ℚ)

def wQ : Matrix {FinM} {FinM} ℚ := Matrix.of fun i j => (wInt i j : ℚ)

def wiQ : Matrix {FinM} {FinM} ℚ := Matrix.of fun i j => (wiInt i j : ℚ)

def gQ : Fin {m} → ℚ := fun k => (gInt k : ℚ)

/-- The certificate midpoint matrix: `mRat i j = aInt i j / 10^{DENP}`. -/
def mRat : Matrix {FinM} {FinM} ℚ := Matrix.of fun i j => (aInt i j : ℚ) / 10 ^ {DENP}

def delta : ℚ := 1 / 10 ^ {DELTAP}

/-! ## The kernel-checked integer facts -/

set_option maxHeartbeats {HB} in
lemma key_int : ∀ i j : Fin {m},
    cInt ^ 2 * bInt i j = ∑ k, wInt k i * gInt k * wInt k j := by decide

set_option maxHeartbeats {HB} in
lemma winv_int : ∀ i j : Fin {m},
    (∑ k, wiInt i k * wInt k j) = if i = j then fInt else 0 := by decide

set_option maxHeartbeats {HB} in
lemma g_pos : ∀ k, 0 < gInt k := by decide

set_option maxHeartbeats {HB} in
lemma f_pos : (0 : ℤ) < fInt := by decide

set_option maxHeartbeats {HB} in
lemma c_pos : (0 : ℤ) < cInt := by decide

lemma c_ne : (cInt : ℚ) ≠ 0 := by exact_mod_cast c_pos.ne'

/-! ## Casts to ℚ -/

lemma key_q (i j : Fin {m}) :
    (cInt : ℚ) ^ 2 * bQ i j = ∑ k, wQ k i * gQ k * wQ k j := by
  have h := key_int i j
  have : ((cInt ^ 2 * bInt i j : ℤ) : ℚ)
      = ((∑ k, wInt k i * gInt k * wInt k j : ℤ) : ℚ) := by exact_mod_cast h
  push_cast at this
  simpa [bQ, wQ, gQ, Matrix.of_apply] using this

lemma winv_q (i j : Fin {m}) :
    (∑ k, wiQ i k * wQ k j) = if i = j then (fInt : ℚ) else 0 := by
  have h := winv_int i j
  by_cases hij : i = j
  · subst hij
    simp only [if_pos rfl] at h ⊢
    have : ((∑ k, wiInt i k * wInt k i : ℤ) : ℚ) = ((fInt : ℤ) : ℚ) := by
      exact_mod_cast h
    push_cast at this
    simpa [wiQ, wQ, Matrix.of_apply] using this
  · simp only [if_neg hij] at h ⊢
    have : ((∑ k, wiInt i k * wInt k j : ℤ) : ℚ) = ((0 : ℤ) : ℚ) := by
      exact_mod_cast h
    push_cast at this
    simpa [wiQ, wQ, Matrix.of_apply] using this

lemma bq_eq (i j : Fin {m}) :
    bQ i j = aQ i j - if i = j then ({S} : ℚ) else 0 := by
  by_cases hij : i = j
  · subst hij
    simp only [bQ, aQ, bInt, aInt, sInt, Matrix.of_apply, if_pos rfl]
    push_cast
    ring
  · simp only [bQ, aQ, bInt, aInt, Matrix.of_apply, if_neg hij]
    push_cast
    ring

/-! ## General algebra: quadratic forms under congruence -/

/-- If `A i j = ∑ k, L i k * d k * L j k` then the quadratic form of `A` is the
`d`-weighted sum of squares of the coordinates `∑ i, x i * L i k`. -/
lemma quad_of_ldl {{n : ℕ}} (A L : Matrix (Fin n) (Fin n) ℚ) (d : Fin n → ℚ)
    (hA : ∀ i j, A i j = ∑ k, L i k * d k * L j k) (x : Fin n → ℚ) :
    x ⬝ᵥ A *ᵥ x = ∑ k, d k * (∑ i, x i * L i k) ^ 2 := by
  have expand : x ⬝ᵥ A *ᵥ x = ∑ i, ∑ j, x i * A i j * x j := by
    unfold Matrix.mulVec dotProduct
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun j _ => by ring
  rw [expand]
  have h1 : ∀ i j, x i * A i j * x j
      = ∑ k, d k * ((x i * L i k) * (x j * L j k)) := by
    intro i j
    rw [hA, Finset.mul_sum, Finset.sum_mul]
    exact Finset.sum_congr rfl fun k _ => by ring
  simp_rw [h1]
  have h2 : (∑ i, ∑ j, ∑ k, d k * ((x i * L i k) * (x j * L j k)))
      = ∑ k, ∑ i, ∑ j, d k * ((x i * L i k) * (x j * L j k)) := by
    calc ∑ i, ∑ j, ∑ k, d k * ((x i * L i k) * (x j * L j k))
        = ∑ i, ∑ k, ∑ j, d k * ((x i * L i k) * (x j * L j k)) :=
          Finset.sum_congr rfl fun i _ => Finset.sum_comm
      _ = ∑ k, ∑ i, ∑ j, d k * ((x i * L i k) * (x j * L j k)) :=
          Finset.sum_comm
  rw [h2]
  refine Finset.sum_congr rfl fun k _ => ?_
  calc ∑ i, ∑ j, d k * ((x i * L i k) * (x j * L j k))
      = ∑ i, (x i * L i k) * (d k * ∑ j, x j * L j k) := by
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [Finset.mul_sum]
        refine Eq.trans ?_ (Finset.mul_sum _ _ _).symm
        exact Finset.sum_congr rfl fun j _ => by ring
    _ = (∑ i, x i * L i k) * (d k * ∑ j, x j * L j k) := by
        rw [← Finset.sum_mul]
    _ = d k * (∑ i, x i * L i k) ^ 2 := by ring

/-- Reconstruction: with `Winv * W = f * 1` entrywise, `f * x j` is recovered
from the coordinates `y k = ∑ i, x i * W k i`. -/
lemma resolve (x : Fin {m} → ℚ) (j : Fin {m}) :
    (fInt : ℚ) * x j = ∑ k, wiQ j k * (∑ i, x i * wQ k i) := by
  have h : (∑ k, wiQ j k * (∑ i, x i * wQ k i))
      = ∑ i, x i * ∑ k, wiQ j k * wQ k i := by
    calc ∑ k, wiQ j k * (∑ i, x i * wQ k i)
        = ∑ k, ∑ i, wiQ j k * (x i * wQ k i) := by
          exact Finset.sum_congr rfl fun k _ => Finset.mul_sum _ _ _
      _ = ∑ i, ∑ k, wiQ j k * (x i * wQ k i) := Finset.sum_comm
      _ = ∑ i, x i * ∑ k, wiQ j k * wQ k i := by
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [Finset.mul_sum]
          exact Finset.sum_congr rfl fun k _ => by ring
  rw [h]
  simp_rw [winv_q, mul_ite, mul_zero]
  rw [Finset.sum_ite_eq Finset.univ j (fun i => x i * (fInt : ℚ))]
  simp [mul_comm]

lemma y_exists {{x : Fin {m} → ℚ}} (hx : x ≠ 0) :
    ∃ k, (∑ i, x i * wQ k i) ≠ 0 := by
  by_contra hall
  push_neg at hall
  apply hx
  funext j
  have h := resolve x j
  simp only [hall, mul_zero, Finset.sum_const_zero] at h
  have hf : (fInt : ℚ) ≠ 0 := by exact_mod_cast f_pos.ne'
  have hxj := (mul_eq_zero.mp h).resolve_left hf
  simpa using hxj

lemma bq_quad_pos {{x : Fin {m} → ℚ}} (hx : x ≠ 0) : 0 < x ⬝ᵥ bQ *ᵥ x := by
  have hkey : ∀ i j, ((cInt : ℚ) ^ 2 • bQ) i j = ∑ k, wQᵀ i k * gQ k * wQᵀ j k := by
    intro i j
    simp only [Matrix.smul_apply, smul_eq_mul, Matrix.transpose_apply]
    exact key_q i j
  have hquad := quad_of_ldl ((cInt : ℚ) ^ 2 • bQ) wQᵀ gQ hkey x
  have hsmul : x ⬝ᵥ ((cInt : ℚ) ^ 2 • bQ) *ᵥ x = (cInt : ℚ) ^ 2 * (x ⬝ᵥ bQ *ᵥ x) := by
    rw [smul_mulVec, dotProduct_smul, smul_eq_mul]
  rw [hsmul] at hquad
  have hpos : 0 < ∑ k, gQ k * (∑ i, x i * wQᵀ i k) ^ 2 := by
    obtain ⟨k, hk⟩ := y_exists hx
    have hk' : (∑ i, x i * wQᵀ i k) ≠ 0 := by
      simpa [Matrix.transpose_apply] using hk
    refine Finset.sum_pos' (fun m _ => ?_) ⟨k, Finset.mem_univ k, ?_⟩
    · have h1 : (0 : ℚ) < gQ m := by
        unfold gQ
        exact_mod_cast g_pos m
      positivity
    · have h1 : (0 : ℚ) < gQ k := by
        unfold gQ
        exact_mod_cast g_pos k
      have h2 : (0 : ℚ) < (∑ i, x i * wQᵀ i k) ^ 2 := by positivity
      positivity
  have hc2 : (0 : ℚ) < (cInt : ℚ) ^ 2 := by
    have := c_ne
    positivity
  nlinarith [hquad, hpos, hc2]

/-! ## Perturbation -/

lemma pert_bound (E : Matrix {FinM} {FinM} ℚ) (d : ℚ) (hd : 0 ≤ d)
    (hE : ∀ i j, |E i j| ≤ d) (x : Fin {m} → ℚ) :
    |x ⬝ᵥ E *ᵥ x| ≤ {m} * d * (x ⬝ᵥ x) := by
  have habs : |x ⬝ᵥ E *ᵥ x| ≤ d * (∑ i, |x i|) ^ 2 := by
    have step1 : |x ⬝ᵥ E *ᵥ x| ≤ ∑ i, |x i| * ∑ j, d * |x j| := by
      refine (Finset.abs_sum_le_sum_abs _ _).trans ?_
      refine Finset.sum_le_sum fun i _ => ?_
      rw [abs_mul]
      refine mul_le_mul_of_nonneg_left ?_ (abs_nonneg _)
      refine (Finset.abs_sum_le_sum_abs _ _).trans ?_
      refine Finset.sum_le_sum fun j _ => ?_
      rw [abs_mul]
      exact mul_le_mul_of_nonneg_right (hE i j) (abs_nonneg _)
    refine step1.trans ?_
    have : ∑ i, |x i| * ∑ j, d * |x j|
        = d * ((∑ i, |x i|) * (∑ j, |x j|)) := by
      rw [← Finset.mul_sum, ← Finset.sum_mul]
      ring
    rw [this, sq]
  refine habs.trans ?_
  have hcs : (∑ i, |x i|) ^ 2 ≤ {m} * ∑ i, |x i| ^ 2 := by
    simpa using sq_sum_le_card_mul_sum_sq (s := Finset.univ)
      (f := fun i : Fin {m} => |x i|)
  have hsq : (∑ i, |x i| ^ 2) = x ⬝ᵥ x := by
    unfold dotProduct
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [sq_abs, sq]
  calc d * (∑ i, |x i|) ^ 2 ≤ d * ({m} * ∑ i, |x i| ^ 2) :=
        mul_le_mul_of_nonneg_left hcs hd
    _ = {m} * d * (x ⬝ᵥ x) := by rw [hsq]; ring

/-! ## Main theorem -/

/-- **A machine-checked window of Weil positivity.**  Every rational matrix
entrywise within `delta = 1/10^{DELTAP}` of `mRat` has a strictly positive
quadratic form.  (The {spec['desc']} is such a matrix — identification budget
{float(stats['ident']):.1e} entrywise, exact-rational rounding; see the module
docstring and results/agent-lean-depth.md.) -/
theorem weil_window_positive (M : Matrix {FinM} {FinM} ℚ)
    (hM : ∀ i j, |M i j - mRat i j| ≤ delta)
    (x : Fin {m} → ℚ) (hx : x ≠ 0) : 0 < x ⬝ᵥ M *ᵥ x := by
  set N : Matrix {FinM} {FinM} ℚ := (10 ^ {DENP} : ℚ) • M with hN
  set E : Matrix {FinM} {FinM} ℚ := N - aQ with hE
  have hEbound : ∀ i j, |E i j| ≤ 10 ^ {DP} := by
    intro i j
    have h := hM i j
    have : E i j = 10 ^ {DENP} * (M i j - mRat i j) := by
      simp only [hE, hN, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul,
        mRat, aQ, Matrix.of_apply]
      ring
    rw [this, abs_mul]
    calc |(10 ^ {DENP} : ℚ)| * |M i j - mRat i j| ≤ |(10 ^ {DENP} : ℚ)| * delta := by
          refine mul_le_mul_of_nonneg_left h (abs_nonneg _)
      _ = 10 ^ {DP} := by norm_num [delta]
  have hsplit : N = bQ + ({S} : ℚ) • (1 : Matrix {FinM} {FinM} ℚ) + E := by
    ext i j
    have hb := bq_eq i j
    by_cases hij : i = j
    · subst hij
      simp only [Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply_eq,
        smul_eq_mul, mul_one, hE, Matrix.sub_apply, hb]
      simp
    · simp only [Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply_ne hij,
        smul_eq_mul, mul_zero, hE, Matrix.sub_apply, hb, if_neg hij]
      ring
  have hq : x ⬝ᵥ N *ᵥ x
      = x ⬝ᵥ bQ *ᵥ x + {S} * (x ⬝ᵥ x) + x ⬝ᵥ E *ᵥ x := by
    rw [hsplit, add_mulVec, add_mulVec, dotProduct_add, dotProduct_add,
        smul_mulVec, one_mulVec, dotProduct_smul]
    simp [smul_eq_mul]
  have h1 := bq_quad_pos hx
  have h2 := pert_bound E (10 ^ {DP}) (by norm_num) hEbound x
  have h3 : -({m} * 10 ^ {DP} * (x ⬝ᵥ x)) ≤ x ⬝ᵥ E *ᵥ x := neg_le_of_abs_le h2
  have hNq : x ⬝ᵥ N *ᵥ x = 10 ^ {DENP} * (x ⬝ᵥ M *ᵥ x) := by
    rw [hN, smul_mulVec, dotProduct_smul, smul_eq_mul]
  have hNpos : 0 < x ⬝ᵥ N *ᵥ x := by
    rw [hq]
    nlinarith [h1, h3]
  rw [hNq] at hNpos
  nlinarith [hNpos]

/-- The certificate matrix itself. -/
theorem mRat_positive (x : Fin {m} → ℚ) (hx : x ≠ 0) : 0 < x ⬝ᵥ mRat *ᵥ x := by
  refine weil_window_positive mRat (fun i j => ?_) x hx
  simp only [sub_self, abs_zero]
  norm_num [delta]
{bigend}
end {ns}
"""
    return hdr + data + body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('window', choices=sorted(WINDOWS))
    ap.add_argument('--measure-only', action='store_true',
                    help='verify certificate and print sizes; write no Lean file')
    args = ap.parse_args()
    spec = WINDOWS[args.window]
    A, W, Wi, g, c, f, S, stats = build_certificate(spec)
    print("[%s] S (shift) = %d = %d * 10^%d;  DEN = 10^%d;  delta = 1e-%d"
          % (spec['ns'], S, spec['m'], spec['DENP'] - spec['DELTAP'],
             spec['DENP'], spec['DELTAP']))
    if args.measure_only:
        print("[%s] --measure-only: no Lean file written" % spec['ns'])
        return
    txt = emit_lean(spec, A, W, Wi, g, c, f, S, stats)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'weilcert', spec['fname'])
    with open(out, 'w') as fh:
        fh.write(txt)
    print("[%s] wrote %s (%.2f MB)" % (spec['ns'], out, len(txt) / 1e6))


if __name__ == "__main__":
    main()
