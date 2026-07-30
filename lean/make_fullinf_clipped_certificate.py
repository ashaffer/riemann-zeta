"""Generate the kernel-checkable rational interval certificate for the
L = 7/4, m = 48 clipped FULLINF finite block.

The Arb driver constructs the normalized-Legendre matrix as outward balls.
This generator extracts exact decimal enclosures with ``arb.mid_rad_10exp``,
rounds their midpoints to a 10^-18 rational grid, and verifies *exactly* that
every ball lies inside the resulting radius-10^-12 rational interval.

Parity makes the matrix the direct sum of two dense 24 by 24 blocks.  For each
block we form, in exact integers,

  B = 10^18 (midpoint - beta I) - 24 * 10^6 I,
  beta = 227 / 10^7,

compute an exact LDL^T decomposition, integerize it, and verify

  c^2 B = W^T diag(g) W,   Winv W = f I,   g > 0.

The emitted Lean artifact checks those identities with ``decide`` and applies
``CertFramework.cert_window_positive``.  Its conclusion concerns only the
explicit exact rational interval matrices; identification with the analytic
clipped zeta form remains outside Lean.

Usage (from the repository root):

  python3 lean/make_fullinf_clipped_certificate.py
"""

from fractions import Fraction
from math import gcd
import os
import sys
import time

sys.set_int_max_str_digits(3_000_000)

ROOT = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[0]
sys.path.insert(0, os.path.join(ROOT, "src"))

from fullinf_unrestricted_certificate import clipped_matrix


M = 48
BLOCK = 24
DENP = 18
DELTAP = 12
DEN = 10**DENP
DELTA = Fraction(1, 10**DELTAP)
BETA = Fraction(227, 10_000_000)
BETA_SCALED = BETA * DEN
SHIFT = BLOCK * DEN * DELTA
assert BETA_SCALED.denominator == 1
assert SHIFT.denominator == 1
BETA_SCALED = int(BETA_SCALED)
SHIFT = int(SHIFT)


def decimal_scaled(n, exp):
    n = int(n)
    exp = int(exp)
    if exp >= 0:
        return Fraction(n * 10**exp)
    return Fraction(n, 10 ** (-exp))


def arb_interval(x):
    """Exact rational enclosure promised by Arb's public conversion API."""
    mid, rad, exp = x.mid_rad_10exp(50)
    center = decimal_scaled(mid, exp)
    radius = decimal_scaled(rad, exp)
    assert radius >= 0
    return center - radius, center + radius


def round_half_up(q):
    return (2 * q.numerator + q.denominator) // (2 * q.denominator)


def lcm(a, b):
    return a * b // gcd(a, b)


def exact_certificate(center, name):
    """Certificate for center - beta I with a 24*delta safety shift."""
    n = len(center)
    shifted = [row[:] for row in center]
    for i in range(n):
        shifted[i][i] -= BETA_SCALED
    bmat = [row[:] for row in shifted]
    for i in range(n):
        bmat[i][i] -= SHIFT

    work = [[Fraction(v) for v in row] for row in bmat]
    lower = [[Fraction(i == j) for j in range(n)] for i in range(n)]
    pivots = [Fraction(0)] * n
    for k in range(n):
        pivots[k] = work[k][k]
        if pivots[k] <= 0:
            raise ArithmeticError(f"{name}: nonpositive exact pivot {k}: {pivots[k]}")
        for i in range(k + 1, n):
            lower[i][k] = work[i][k] / pivots[k]
        for i in range(k + 1, n):
            for j in range(k + 1, i + 1):
                work[i][j] -= lower[i][k] * lower[j][k] * pivots[k]
                work[j][i] = work[i][j]

    lower_inv = [[Fraction(i == j) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i):
            lower_inv[i][j] = -sum(
                lower[i][k] * lower_inv[k][j] for k in range(j, i)
            )

    row_den = [1] * n
    for k in range(n):
        for i in range(n):
            row_den[k] = lcm(row_den[k], lower[i][k].denominator)
    common = 1
    for k in range(n):
        common = lcm(common, row_den[k])
        common = lcm(common, pivots[k].denominator)

    wmat = [
        [int(row_den[k] * lower[i][k]) for i in range(n)]
        for k in range(n)
    ]
    gvec = []
    for k in range(n):
        value = pivots[k] * common * common / (row_den[k] * row_den[k])
        assert value.denominator == 1 and value > 0
        gvec.append(int(value))

    for i in range(n):
        for j in range(n):
            lhs = common * common * bmat[i][j]
            rhs = sum(wmat[k][i] * gvec[k] * wmat[k][j] for k in range(n))
            assert lhs == rhs, (name, "congruence", i, j)

    inverse_scale = 1
    for i in range(n):
        for k in range(n):
            inverse_scale = lcm(
                inverse_scale, (lower_inv[k][i] / row_den[k]).denominator
            )
    winv = []
    for i in range(n):
        row = []
        for k in range(n):
            value = inverse_scale * lower_inv[k][i] / row_den[k]
            assert value.denominator == 1
            row.append(int(value))
        winv.append(row)
    for i in range(n):
        for j in range(n):
            value = sum(winv[i][k] * wmat[k][j] for k in range(n))
            assert value == (inverse_scale if i == j else 0), (name, "inverse", i, j)

    return shifted, wmat, winv, gvec, common, inverse_scale, pivots


def digits(x):
    return len(str(abs(int(x)))) if x else 1


def emit_fun2(name, values):
    lines = [f"def {name} : Nat → Nat → Int"]
    for i, row in enumerate(values):
        for j, value in enumerate(row):
            lines.append(f"  | {i}, {j} => {value}")
    lines.append("  | _, _ => 0")
    return "\n".join(lines)


def emit_fun1(name, values):
    lines = [f"def {name} : Nat → Int"]
    for i, value in enumerate(values):
        lines.append(f"  | {i} => {value}")
    lines.append("  | _ => 0")
    return "\n".join(lines)


def emit_block(prefix, cert):
    shifted, wmat, winv, gvec, common, inverse_scale, _ = cert
    cap = prefix.capitalize()
    data = "\n\n".join(
        [
            emit_fun2(prefix + "AFun", shifted),
            emit_fun2(prefix + "WFun", wmat),
            emit_fun2(prefix + "WiFun", winv),
            emit_fun1(prefix + "GFun", gvec),
            f"def {prefix}CInt : Int := {common}",
            f"def {prefix}FInt : Int := {inverse_scale}",
        ]
    )
    return f"""{data}

def {prefix}AInt : Matrix (Fin 24) (Fin 24) ℤ :=
  Matrix.of fun i j => {prefix}AFun i.val j.val

def {prefix}WInt : Matrix (Fin 24) (Fin 24) ℤ :=
  Matrix.of fun i j => {prefix}WFun i.val j.val

def {prefix}WiInt : Matrix (Fin 24) (Fin 24) ℤ :=
  Matrix.of fun i j => {prefix}WiFun i.val j.val

def {prefix}GInt : Fin 24 → ℤ := fun k => {prefix}GFun k.val

def {prefix}BInt : Matrix (Fin 24) (Fin 24) ℤ :=
  Matrix.of fun i j => {prefix}AInt i j - if i = j then shiftInt else 0

def {prefix}AQ : Matrix (Fin 24) (Fin 24) ℚ :=
  Matrix.of fun i j => ({prefix}AInt i j : ℚ)

def {prefix}WQ : Matrix (Fin 24) (Fin 24) ℚ :=
  Matrix.of fun i j => ({prefix}WInt i j : ℚ)

def {prefix}WiQ : Matrix (Fin 24) (Fin 24) ℚ :=
  Matrix.of fun i j => ({prefix}WiInt i j : ℚ)

def {prefix}GQ : Fin 24 → ℚ := fun k => ({prefix}GInt k : ℚ)

/-- Center of the exact rational interval for the {prefix} parity block.
The stored integer matrix is shifted by `beta`; this definition restores the
unshifted clipped-matrix center. -/
def {prefix}Mid : Matrix (Fin 24) (Fin 24) ℚ :=
  Matrix.of fun i j => {prefix}AQ i j / scale + if i = j then beta else 0

def {prefix}Lower : Matrix (Fin 24) (Fin 24) ℚ :=
  Matrix.of fun i j => {prefix}Mid i j - delta

def {prefix}Upper : Matrix (Fin 24) (Fin 24) ℚ :=
  Matrix.of fun i j => {prefix}Mid i j + delta

set_option maxHeartbeats 200000000 in
lemma {prefix}KeyInt : ∀ i j : Fin 24,
    {prefix}CInt ^ 2 * {prefix}BInt i j =
      ∑ k, {prefix}WInt k i * {prefix}GInt k * {prefix}WInt k j := by decide

set_option maxHeartbeats 200000000 in
lemma {prefix}WinvInt : ∀ i j : Fin 24,
    (∑ k, {prefix}WiInt i k * {prefix}WInt k j) =
      if i = j then {prefix}FInt else 0 := by decide

set_option maxHeartbeats 200000000 in
lemma {prefix}GPos : ∀ k, 0 < {prefix}GInt k := by decide

lemma {prefix}CPos : (0 : ℤ) < {prefix}CInt := by decide

lemma {prefix}FPos : (0 : ℤ) < {prefix}FInt := by decide

lemma {prefix}KeyQ (i j : Fin 24) :
    ({prefix}CInt : ℚ) ^ 2 *
        ({prefix}AQ i j - if i = j then (shiftInt : ℚ) else 0) =
      ∑ k, {prefix}WQ k i * {prefix}GQ k * {prefix}WQ k j := by
  have h := {prefix}KeyInt i j
  have hq : (({prefix}CInt ^ 2 * {prefix}BInt i j : ℤ) : ℚ) =
      ((∑ k, {prefix}WInt k i * {prefix}GInt k * {prefix}WInt k j : ℤ) : ℚ) := by
    exact_mod_cast h
  push_cast at hq
  simpa [{prefix}BInt, {prefix}AQ, {prefix}WQ, {prefix}GQ] using hq

lemma {prefix}WinvQ (i j : Fin 24) :
    (∑ k, {prefix}WiQ i k * {prefix}WQ k j) =
      if i = j then ({prefix}FInt : ℚ) else 0 := by
  have h := {prefix}WinvInt i j
  have hq := congrArg (fun z : ℤ => (z : ℚ)) h
  push_cast at hq
  simpa [{prefix}WiQ, {prefix}WQ] using hq

/-- Every exact rational matrix in the stored {prefix}-block interval has
quadratic form strictly above `beta = 2.27e-5` on nonzero vectors. -/
theorem {prefix}IntervalLowerBound (M : Matrix (Fin 24) (Fin 24) ℚ)
    (hM : ∀ i j, {prefix}Lower i j ≤ M i j ∧ M i j ≤ {prefix}Upper i j)
    (x : Fin 24 → ℚ) (hx : x ≠ 0) :
    beta * (x ⬝ᵥ x) < x ⬝ᵥ M *ᵥ x := by
  let N : Matrix (Fin 24) (Fin 24) ℚ := M - beta • 1
  have hclose : ∀ i j, |N i j - {prefix}AQ i j / scale| ≤ delta := by
    intro i j
    have bounds := hM i j
    have habs : |M i j - {prefix}Mid i j| ≤ delta := by
      rw [abs_le]
      constructor
      · have hlo := bounds.1
        simp only [{prefix}Lower, Matrix.of_apply] at hlo
        linarith
      · have hhi := bounds.2
        simp only [{prefix}Upper, Matrix.of_apply] at hhi
        linarith
    have heq : N i j - {prefix}AQ i j / scale = M i j - {prefix}Mid i j := by
      simp only [N, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul,
        {prefix}Mid, Matrix.of_apply]
      by_cases hij : i = j
      · subst j
        simp
        ring
      · simp [Matrix.one_apply_ne hij, hij]
    rwa [heq]
  have hpos : 0 < x ⬝ᵥ N *ᵥ x := by
    refine CertFramework.cert_window_positive {prefix}AQ {prefix}WQ {prefix}WiQ
      {prefix}GQ ({prefix}CInt : ℚ) ({prefix}FInt : ℚ) (shiftInt : ℚ)
      scale delta {prefix}KeyQ {prefix}WinvQ ?_ ?_ ?_ ?_ ?_ ?_ N hclose hx
    · intro k
      unfold {prefix}GQ
      exact_mod_cast {prefix}GPos k
    · exact_mod_cast {prefix}CPos.ne'
    · exact_mod_cast {prefix}FPos.ne'
    · norm_num [scale]
    · norm_num [delta]
    · norm_num [scale, delta, shiftInt]
  have hrewrite : x ⬝ᵥ N *ᵥ x = x ⬝ᵥ M *ᵥ x - beta * (x ⬝ᵥ x) := by
    simp only [N, sub_mulVec, smul_mulVec, one_mulVec, dotProduct_sub,
      dotProduct_smul, smul_eq_mul]
  rw [hrewrite] at hpos
  exact sub_pos.mp hpos
"""


def emit_file(even_cert, odd_cert, max_error):
    return f"""/-
FullInfClipped48: kernel-checked finite clipped-block interval theorem.

This file contains exact rational interval data for the normalized Legendre
matrix produced by the L=7/4, S=50, m=48 Arb clipped-symbol driver.  Parity
splits it into two 24-dimensional blocks.  The generator proved externally,
using Arb's documented outward decimal conversion, that every source ball is
contained in the displayed midpoint ± delta interval; its largest exact
center-to-endpoint error was {float(max_error):.3e} < delta/100.

The theorem in this file is deliberately narrower than the analytic FULLINF
claim: it proves positivity for every *exact rational matrix* in these stored
intervals.  It does not identify an analytic integral with the interval data.
All LDL congruences and inverse identities below are checked by the Lean kernel
with `decide`; no native_decide or trusted numeric oracle is used.

Generated by lean/make_fullinf_clipped_certificate.py.
-/
import Mathlib
import CertFramework

namespace FullInfClipped48

open Matrix Finset

set_option linter.style.longLine false
set_option linter.style.setOption false
set_option linter.style.maxHeartbeats false
set_option maxHeartbeats 200000000
set_option maxRecDepth 8192

noncomputable section

def beta : ℚ := 227 / 10 ^ 7
def scale : ℚ := 10 ^ 18
def delta : ℚ := 1 / 10 ^ 12
def shiftInt : ℤ := 24000000

{emit_block("even", even_cert)}

{emit_block("odd", odd_cert)}

/-- The kernel-checked 48-dimensional direct-sum statement for the exact
rational clipped-block interval data. -/
theorem clipped48IntervalLowerBound
    (Me Mo : Matrix (Fin 24) (Fin 24) ℚ)
    (he : ∀ i j, evenLower i j ≤ Me i j ∧ Me i j ≤ evenUpper i j)
    (ho : ∀ i j, oddLower i j ≤ Mo i j ∧ Mo i j ≤ oddUpper i j)
    (xe xo : Fin 24 → ℚ) (hx : (xe, xo) ≠ (0, 0)) :
    beta * (xe ⬝ᵥ xe + xo ⬝ᵥ xo) <
      xe ⬝ᵥ Me *ᵥ xe + xo ⬝ᵥ Mo *ᵥ xo := by
  by_cases hxe : xe = 0
  · have hxo : xo ≠ 0 := by
      intro hxo
      exact hx (Prod.ext hxe hxo)
    have hodd := oddIntervalLowerBound Mo ho xo hxo
    simpa [hxe] using hodd
  · have heven := evenIntervalLowerBound Me he xe hxe
    have hodd : beta * (xo ⬝ᵥ xo) ≤ xo ⬝ᵥ Mo *ᵥ xo := by
      by_cases hxo : xo = 0
      · simp [hxo]
      · exact (oddIntervalLowerBound Mo ho xo hxo).le
    linarith

end

end FullInfClipped48
"""


def main():
    started = time.time()
    matrix = clipped_matrix(verbose=True)
    centers = {"even": [[0] * BLOCK for _ in range(BLOCK)],
               "odd": [[0] * BLOCK for _ in range(BLOCK)]}
    max_error = Fraction(0)
    for parity, name in [(0, "even"), (1, "odd")]:
        for i in range(BLOCK):
            for j in range(BLOCK):
                lo, hi = arb_interval(matrix[2 * i + parity][2 * j + parity])
                midpoint = (lo + hi) / 2
                rounded = round_half_up(midpoint * DEN)
                center = Fraction(rounded, DEN)
                error = max(abs(center - lo), abs(hi - center))
                if error > max_error:
                    max_error = error
                if error >= DELTA / 100:
                    raise ArithmeticError(
                        f"{name}[{i},{j}] enclosure error {float(error):.3e} too large"
                    )
                centers[name][i][j] = rounded
    for name in centers:
        for i in range(BLOCK):
            for j in range(BLOCK):
                assert centers[name][i][j] == centers[name][j][i]

    print(f"matrix balls converted; max exact interval error {float(max_error):.3e}")
    even_cert = exact_certificate(centers["even"], "even")
    odd_cert = exact_certificate(centers["odd"], "odd")
    for name, cert in [("even", even_cert), ("odd", odd_cert)]:
        shifted, wmat, winv, gvec, common, inverse_scale, pivots = cert
        print(
            f"{name}: exact pivots positive; min={float(min(pivots)):.3e}; "
            f"digits A/W/Winv/g/c/f="
            f"{max(digits(v) for row in shifted for v in row)}/"
            f"{max(digits(v) for row in wmat for v in row)}/"
            f"{max(digits(v) for row in winv for v in row)}/"
            f"{max(digits(v) for v in gvec)}/{digits(common)}/{digits(inverse_scale)}"
        )
    output = emit_file(even_cert, odd_cert, max_error)
    target = os.path.join(ROOT, "lean", "weilcert", "FullInfClipped48.lean")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(output)
    print(f"wrote {target} ({len(output) / 1e6:.2f} MB) in {time.time()-started:.1f}s")


if __name__ == "__main__":
    main()
