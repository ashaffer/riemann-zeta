#!/usr/bin/env python3
"""gen_bridge_overlap.py — generate lean/weilcert/BridgeOverlap.lean.

Emits, for every pair k <= j with k + j <= KMAX:

  * evaluation lemmas          aeval_legendre_<n>  (over R, n = 2..KMAX),
  * the universal shifted-overlap polynomial data  Fovl_<k>_<j> : Q[X]
    (exact rational coefficients, from src/certified_spectral.py F_poly),
  * the proved overlap identity
      INT_{-1}^{1-v} P_k(t) P_j(t+v) dt = (Fovl_<k>_<j>).aeval v      (v : R)
    via the fundamental theorem of calculus with an explicit polynomial
    antiderivative A_kj(t, v) generated here (HasDerivAt chains from
    hasDerivAt_pow / HasDerivAt.const_mul / HasDerivAt.add, transported by
    HasDerivAt.congr_deriv).

Cross-checks performed by this generator before emission:
  * F recomputed here from the antiderivative (A(1-v,v) - A(-1,v)) must equal
    src/certified_spectral.py's F_poly(k, j) exactly (Fraction arithmetic).
Cross-checks emitted into the Lean file:
  * shiftedLegendre_cross_check_<n> against mathlib's independent
    Polynomial.shiftedLegendre (P_n(1 - 2x)) at small index.

Usage:  python3 gen_bridge_overlap.py [KMAX]   (default 4)
Writes: lean/weilcert/BridgeOverlap.lean
"""
import sys
import os
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))

from certified_spectral import F_poly, leg, binom  # noqa: E402

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
NMAX = KMAX  # largest single index appearing in pairs

NAMES = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
         6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
         12: "twelve"}


# ----------------------------------------------------------------------
# rendering helpers
# ----------------------------------------------------------------------

def q_lit(c):
    assert c > 0
    if c.denominator == 1:
        return f"({c.numerator} : ℚ)"
    return f"({c.numerator} / {c.denominator} : ℚ)"


def r_lit(c):
    assert c > 0
    if c.denominator == 1:
        return f"({c.numerator} : ℝ)"
    return f"({c.numerator} / {c.denominator} : ℝ)"


def wrap(s, indent, width=86):
    """Break a flat expression string at top-level ' + ' / ' - ' boundaries so
    that no emitted line exceeds `width` columns (linter limit 100)."""
    pieces = []
    depth = 0
    cur = ""
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if depth == 0 and s[i:i + 3] in (" + ", " - ") and cur:
            pieces.append(cur)
            pieces.append(s[i:i + 3])
            cur = ""
            i += 3
            continue
        cur += ch
        i += 1
    pieces.append(cur)
    lines = [pieces[0]]
    eff = indent + len(pieces[0])
    for op, term in zip(pieces[1::2], pieces[2::2]):
        if eff + len(op) + len(term) > width:
            lines[-1] += op.rstrip()
            lines.append(" " * indent + term)
            eff = indent + len(term)
        else:
            lines[-1] += op + term
            eff += len(op) + len(term)
    return "\n".join(lines)


def poly_terms(terms):
    """terms: list of (coeff Fraction, callable mag->string)."""
    out = ""
    first = True
    for c, mono in terms:
        if c == 0:
            continue
        lit = mono(abs(c))
        if first:
            out += ("-" if c < 0 else "") + lit
            first = False
        else:
            out += (" - " if c < 0 else " + ") + lit
    if first:
        out = "0"
    return out


def q_poly(coeffs):
    """ascending Fraction coeffs -> Q[X] expression, C-signs outside."""
    terms = []
    for p, c in enumerate(coeffs):
        if c == 0:
            continue
        if p == 0:
            terms.append((c, lambda m: f"C {q_lit(m)}"))
        else:
            terms.append((c, lambda m, p=p: f"C {q_lit(m)} * X ^ {p}"))
    return poly_terms(terms)


def sign_flags(coeffs):
    """(needs_map_neg, needs_map_sub, needs_map_add) for the q_poly render."""
    nz = [c for c in coeffs if c != 0]
    neg = nz and nz[0] < 0
    sub = any(c < 0 for c in nz[1:])
    add = any(c > 0 for c in nz[1:])
    return neg, sub, add


def r_poly(coeffs, var, descending=False):
    idx = range(len(coeffs) - 1, -1, -1) if descending else range(len(coeffs))
    terms = []
    for p in idx:
        c = coeffs[p]
        if c == 0:
            continue
        if p == 0:
            terms.append((c, lambda m: r_lit(m)))
        else:
            terms.append((c, lambda m, p=p: f"{r_lit(m)} * {var} ^ {p}"))
    return poly_terms(terms)


def bivariate_B(k, j):
    """B[p][q] = coeff of v^p t^q in P_k(t) * P_j(t+v) (exact Fractions),
    mirroring src/certified_spectral.py:F_poly."""
    Pk, Pj = leg(k), leg(j)
    deg_t = k + j
    B = [[Fraction(0)] * (deg_t + 1) for _ in range(j + 1)]
    for i, cj in enumerate(Pj):
        if cj:
            for q in range(i + 1):
                cvq = cj * binom(i, q)
                p = i - q
                for r, ck in enumerate(Pk):
                    if ck:
                        B[p][q + r] += cvq * ck
    return B, deg_t


def f_expr(B, deg_t, j, tvar="t"):
    terms = []
    for q in range(deg_t + 1):
        for p in range(j + 1):
            c = B[p][q]
            if c == 0:
                continue
            def mono(m, p=p, q=q):
                s = r_lit(m)
                if p > 0:
                    s += f" * v ^ {p}"
                if q > 0:
                    s += f" * {tvar} ^ {q}"
                return s
            terms.append((c, mono))
    return poly_terms(terms)


def a_coeff_exprs(B, deg_t, j):
    out = []
    for q in range(deg_t + 1):
        aq = [B[p][q] / (q + 1) for p in range(j + 1)]
        if all(c == 0 for c in aq):
            continue
        out.append((q, r_poly(aq, "v"), aq))
    return out


def F_from_A(acoeffs, j, deg_t):
    F = [Fraction(0)] * (deg_t + 2 + j)
    for q, _s, aq in acoeffs:
        for p, c in enumerate(aq):
            if c == 0:
                continue
            for s in range(q + 2):
                F[p + s] += c * binom(q + 1, s) * (-1) ** s
            F[p] -= c * (-1) ** (q + 1)
    while len(F) > 1 and F[-1] == 0:
        F.pop()
    return F


# ----------------------------------------------------------------------
# lemma generators
# ----------------------------------------------------------------------

def gen_aeval_legendre(n):
    coeffs = leg(n)
    rhs = wrap(r_poly(coeffs, "x", descending=True), 8)
    deps = [f"aeval_legendre_{NAMES[m]}" for m in (n - 1, n - 2) if m >= 2]
    dep_str = f" [{', '.join(deps)}]" if deps else ""
    return f"""lemma aeval_legendre_{NAMES[n]} (x : ℝ) :
    aeval x (legendre {n})
      = {rhs} := by
  nth_rewrite 1 [show ({n} : ℕ) = {n - 2} + 2 from rfl]
  rw [aeval_legendre_add_two]
  norm_num{dep_str}
  ring
"""


def gen_pair(k, j):
    B, deg_t = bivariate_B(k, j)
    fx = f_expr(B, deg_t, j)
    acoeffs = a_coeff_exprs(B, deg_t, j)
    F_mine = F_from_A(acoeffs, j, deg_t)
    F_ref = list(F_poly(k, j))
    assert F_mine == F_ref + [Fraction(0)] * (len(F_mine) - len(F_ref)), \
        f"F mismatch at ({k},{j})"
    neg, sub, add = sign_flags(F_ref)
    maps = (["map_add"] if add else []) + (["map_sub"] if sub else []) \
        + (["map_neg"] if neg else []) + ["map_mul", "map_pow"]
    A_fun = (" +\n          ").join(
        f"({wrap(s, 12)}) * x ^ {q + 1}" for q, s, _ in acoeffs)
    chain = None
    for q, s, _ in acoeffs:
        piece = (f"((hasDerivAt_pow {q + 1} t).const_mul\n"
                 f"        ({wrap(s, 10)}))")
        chain = piece if chain is None else f"({chain}.add\n      {piece})"
    ev = [f"aeval_legendre_{NAMES[k]}"]
    if j != k:
        ev.append(f"aeval_legendre_{NAMES[j]}")
    fxh = wrap(fx, 8)
    fdef = f"""/-- `F_{{{k}{j}}}`: exact rational data from `src/certified_spectral.py`,
`F_poly({k}, {j})`. -/
noncomputable def Fovl_{k}_{j} : ℚ[X] :=
  {wrap(q_poly(F_ref), 4)}
"""
    thm = f"""-- The generated FTC proof elaborates explicit polynomial identities of
-- degree {k + j + 1}; the default elaboration budget is exceeded past
-- k + j = 8, so raise it locally (kernel checking is unaffected).
set_option maxHeartbeats 1600000 in
/-- Overlap identity `∫_{{-1}}^{{1-v}} P_{k}(t) P_{j}(t+v) dt = F_{{{k}{j}}}(v)`. -/
theorem overlap_{k}_{j} (v : ℝ) :
    (∫ t in (-1 : ℝ)..(1 - v), aeval t (legendre {k}) * aeval (t + v) (legendre {j}))
      = aeval v Fovl_{k}_{j} := by
  have hi : ∀ t : ℝ, aeval t (legendre {k}) * aeval (t + v) (legendre {j})
      = {fxh} := by
    intro t
    simp only [{', '.join(ev)}]
    ring
  simp only [hi]
  have hd : ∀ t ∈ Set.uIcc (-1 : ℝ) (1 - v),
      HasDerivAt
        (fun x : ℝ =>
          {A_fun})
        ({wrap(fx, 10)}) t := by
    intro t _
    exact HasDerivAt.congr_deriv
      {chain}
      (by push_cast; ring)
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hd
    (((by fun_prop : Continuous fun t : ℝ =>
        {wrap(fx, 10)})).intervalIntegrable _ _)]
  simp only [Fovl_{k}_{j}, {', '.join(maps)}, aeval_C, aeval_X, eq_ratCast]
  push_cast
  ring
"""
    return fdef + "\n" + thm


def gen_shifted_check(n):
    if n == 0:
        simp_line = "  simp"
    elif n == 1:
        simp_line = "  simp [Finset.sum_range_succ, Nat.choose]"
    else:
        simp_line = (f"  simp [Finset.sum_range_succ, Nat.choose, map_ofNat, "
                     f"aeval_legendre_{NAMES[n]}]")
    tail = "" if n < 1 else "\n  ring"
    return f"""lemma shiftedLegendre_cross_check_{NAMES[n]} (x : ℝ) :
    aeval x (Polynomial.shiftedLegendre {n}) = aeval (1 - 2 * x) (legendre {n}) := by
  rw [Polynomial.shiftedLegendre]
{simp_line}{tail}
"""


# ----------------------------------------------------------------------
# file assembly
# ----------------------------------------------------------------------

pairs = [(k, j) for k in range(NMAX + 1) for j in range(k, NMAX + 1)
         if k + j <= KMAX]

parts = [f"""/-
BridgeOverlap (GENERATED by lean/gen_bridge_overlap.py — regenerate, do not
hand-edit): the universal shifted-overlap polynomials of the Bridge
Proposition (THEOREMS.md) and their proved integral identities

  ∫ t in (-1)..(1-v), P_k(t) * P_j(t+v) dt  =  F_kj(v)     (all v : ℝ)

for k ≤ j, k + j ≤ {KMAX}.  The rational data Fovl_k_j is generated by
src/certified_spectral.py's F_poly (exact Fractions); the identities are
proved by the fundamental theorem of calculus with explicit polynomial
antiderivatives, entirely inside Lean — no numerics, no `native_decide`.

`overlap_scaled` converts any such identity to the form actually used by the
truncated Weil form at scale a = L/4: with b_k(x) = P_k(x/a),

  ∫ x in (-a)..(a-u), b_k(x) b_j(x+u) dx = a * F_kj(u/a).

Cross-checks: `shiftedLegendre_cross_check_*` verify against mathlib's
independent `Polynomial.shiftedLegendre` (P_n(1-2x)) at small index.
-/
import BridgeLegendre

namespace Bridge

open Polynomial

/-! ## Evaluation lemmas over ℝ -/

@[simp] lemma aeval_legendre_zero (x : ℝ) : aeval x (legendre 0) = 1 := by
  simp

@[simp] lemma aeval_legendre_one (x : ℝ) : aeval x (legendre 1) = x := by
  simp
"""]

for n in range(2, NMAX + 1):
    parts.append(gen_aeval_legendre(n))

parts.append(
    "/-! ## Cross-check against mathlib's `Polynomial.shiftedLegendre` -/\n")
for n in range(0, min(NMAX, 4) + 1):
    parts.append(gen_shifted_check(n))

parts.append("/-! ## The overlap polynomials and their integral identities -/\n")
for (k, j) in pairs:
    parts.append(gen_pair(k, j))

parts.append("""/-! ## The scaled form used by the truncated Weil form -/

/-- Change of scale: any proved reference-interval overlap identity yields the
overlap of the Weil-form basis `b_k(x) = P_k(x/a)` on `[-a, a]`:
`∫ b_k(x) b_j(x+u) dx = a * F_kj(u/a)`.  (`a = L/4` in the ledger.) -/
theorem overlap_scaled {k j : ℕ} {F : ℚ[X]}
    (hF : ∀ v : ℝ, (∫ t in (-1 : ℝ)..(1 - v),
        aeval t (legendre k) * aeval (t + v) (legendre j)) = aeval v F)
    {a : ℝ} (ha : 0 < a) (u : ℝ) :
    (∫ x in (-a)..(a - u),
        aeval (x / a) (legendre k) * aeval ((x + u) / a) (legendre j))
      = a * aeval (u / a) F := by
  have hsplit : ∀ x : ℝ,
      aeval (x / a) (legendre k) * aeval ((x + u) / a) (legendre j)
        = aeval (x / a) (legendre k) * aeval (x / a + u / a) (legendre j) := by
    intro x; rw [add_div]
  simp only [hsplit]
  have h2 := intervalIntegral.integral_comp_div
    (a := -a) (b := a - u) (c := a)
    (f := fun t => aeval t (legendre k) * aeval (t + u / a) (legendre j))
    ha.ne'
  rw [h2, neg_div, div_self ha.ne', sub_div, div_self ha.ne', hF (u / a),
    smul_eq_mul]
""")

parts.append("end Bridge\n")

out = os.path.join(HERE, "weilcert", "BridgeOverlap.lean")
with open(out, "w") as fh:
    fh.write("\n".join(parts))
print(f"wrote {out}: {len(pairs)} pairs (KMAX = {KMAX}), "
      f"aeval lemmas up to n = {NMAX}")
for (k, j) in pairs:
    print(f"  overlap_{k}_{j}: F deg {len(F_poly(k, j)) - 1}")
