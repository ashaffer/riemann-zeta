# Copyright (c) 2026 Riemann-Zeta project contributors.
# Released under Apache 2.0 license as described in the repository LICENSE.
"""Generate the kernel-checked finite prime-5 rescue certificate.

The analytic side uses ``src/certified_spectral.py`` at

    L = 327/100,  m = 12,

in the unnormalised Legendre basis.  The full matrix contains every active
prime power.  In this support window the only active term not belonging to
the prime places {2, 3} is n = 5, so the old matrix is recovered by adding
back the p=5 overlap term.

The generated Lean file deliberately does *not* trust that analytic
identification.  It stores exact rational midpoints and proves:

* an exact integer LDL congruence for the full midpoint minus a safety shift;
* positivity for every real matrix in the displayed full interval;
* negativity of the old midpoint on one exact integer witness;
* positivity of the midpoint event correction on that witness; and
* the corresponding robust statements for arbitrary full/old real matrices
  in the displayed intervals.

Containment of the analytic matrices in those intervals remains an explicit
external hypothesis of the final Lean theorem.

Run from the repository root:

    python3 lean/make_prime5_rescue_certificate.py
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
import os
import sys
import time

import mpmath as mp
from mpmath import iv
import numpy as np


sys.set_int_max_str_digits(3_000_000)

ROOT = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[0]
sys.path.insert(0, os.path.join(ROOT, "src"))

from certified_spectral import F2iv, F_poly, certified_spectral_form


L = Fraction(327, 100)
M = 12
DEN = 10**24
DELTA = Fraction(1, 10**20)
SHIFT = M * DEN * DELTA
assert SHIFT.denominator == 1
SHIFT = int(SHIFT)


def lcm(a: int, b: int) -> int:
    a, b = int(a), int(b)
    return a * b // gcd(a, b)


def mpf_fraction(value) -> Fraction:
    """Convert an mpmath binary endpoint to an exact Fraction."""
    sign, mantissa, exponent, _ = mp.mpf(value)._mpf_
    result = Fraction(mantissa)
    if exponent >= 0:
        result *= 2**exponent
    else:
        result /= 2 ** (-exponent)
    return -result if sign else result


def interval_bounds(value) -> tuple[Fraction, Fraction]:
    return mpf_fraction(value.a), mpf_fraction(value.b)


def round_half_up(value: Fraction) -> int:
    return int((2 * value.numerator + value.denominator) // (2 * value.denominator))


def rounded_centers(matrix, name: str) -> tuple[list[list[int]], Fraction]:
    centers = [[0] * M for _ in range(M)]
    max_error = Fraction(0)
    for i in range(M):
        for j in range(M):
            lo, hi = interval_bounds(matrix[i][j])
            midpoint = (lo + hi) / 2
            rounded = round_half_up(midpoint * DEN)
            center = Fraction(rounded, DEN)
            error = max(abs(center - lo), abs(hi - center))
            max_error = max(max_error, error)
            if error > DELTA:
                raise ArithmeticError(
                    f"{name}[{i},{j}] interval misses midpoint +/- delta: {error}"
                )
            centers[i][j] = rounded
    for i in range(M):
        for j in range(M):
            if centers[i][j] != centers[j][i]:
                raise ArithmeticError(f"{name} rounded midpoint is not symmetric")
    return centers, max_error


def exact_ldl_certificate(center: list[list[int]]):
    """Certify center - SHIFT*I by an exact integer LDL congruence."""
    bmat = [row[:] for row in center]
    for i in range(M):
        bmat[i][i] -= SHIFT

    work = [[Fraction(value) for value in row] for row in bmat]
    lower = [[Fraction(i == j) for j in range(M)] for i in range(M)]
    pivots = [Fraction(0)] * M
    for k in range(M):
        pivots[k] = work[k][k]
        if pivots[k] <= 0:
            raise ArithmeticError(f"nonpositive exact LDL pivot {k}: {pivots[k]}")
        for i in range(k + 1, M):
            lower[i][k] = work[i][k] / pivots[k]
        for i in range(k + 1, M):
            for j in range(k + 1, i + 1):
                work[i][j] -= lower[i][k] * lower[j][k] * pivots[k]
                work[j][i] = work[i][j]

    lower_inv = [[Fraction(i == j) for j in range(M)] for i in range(M)]
    for i in range(M):
        for j in range(i):
            lower_inv[i][j] = -sum(
                lower[i][k] * lower_inv[k][j] for k in range(j, i)
            )

    row_den = [1] * M
    for k in range(M):
        for i in range(M):
            row_den[k] = lcm(row_den[k], lower[i][k].denominator)
    common = 1
    for k in range(M):
        common = lcm(common, row_den[k])
        common = lcm(common, pivots[k].denominator)

    wmat = [
        [int(row_den[k] * lower[i][k]) for i in range(M)]
        for k in range(M)
    ]
    gvec = []
    for k in range(M):
        value = pivots[k] * common * common / row_den[k] ** 2
        if value.denominator != 1 or value <= 0:
            raise ArithmeticError("failed to integerise a positive LDL pivot")
        gvec.append(int(value))

    for i in range(M):
        for j in range(M):
            lhs = common * common * bmat[i][j]
            rhs = sum(wmat[k][i] * gvec[k] * wmat[k][j] for k in range(M))
            if lhs != rhs:
                raise ArithmeticError(("congruence", i, j))

    inverse_scale = 1
    for i in range(M):
        for k in range(M):
            inverse_scale = lcm(
                inverse_scale, (lower_inv[k][i] / row_den[k]).denominator
            )
    winv = []
    for i in range(M):
        row = []
        for k in range(M):
            value = inverse_scale * lower_inv[k][i] / row_den[k]
            if value.denominator != 1:
                raise ArithmeticError("failed to integerise inverse witness")
            row.append(int(value))
        winv.append(row)
    for i in range(M):
        for j in range(M):
            value = sum(winv[i][k] * wmat[k][j] for k in range(M))
            if value != (inverse_scale if i == j else 0):
                raise ArithmeticError(("inverse", i, j))

    return wmat, winv, gvec, common, inverse_scale, pivots


def quad(matrix: list[list[int]], vector: list[int]) -> int:
    return sum(
        vector[i] * matrix[i][j] * vector[j]
        for i in range(M)
        for j in range(M)
    )


def integer_witness(old_center: list[list[int]]) -> list[int]:
    old_float = np.array(old_center, dtype=float) / float(DEN)
    values, vectors = np.linalg.eigh(old_float)
    vector = vectors[:, np.argmin(values)]
    # The negative mode is odd.  Enforce exact parity before rationalisation.
    witness = [0 if k % 2 == 0 else int(np.rint(10**12 * vector[k])) for k in range(M)]
    divisor = 0
    for value in witness:
        divisor = gcd(divisor, abs(value))
    if divisor > 1:
        witness = [value // divisor for value in witness]
    if not any(witness):
        raise ArithmeticError("zero witness")
    return witness


def digits(value: int) -> int:
    return len(str(abs(int(value)))) if value else 1


def emit_fun2(name: str, values: list[list[int]]) -> str:
    lines = [f"def {name} : Nat → Nat → Int"]
    for i, row in enumerate(values):
        for j, value in enumerate(row):
            lines.append(f"  | {i}, {j} => {value}")
    lines.append("  | _, _ => 0")
    return "\n".join(lines)


def emit_fun1(name: str, values: list[int]) -> str:
    lines = [f"def {name} : Nat → Int"]
    for i, value in enumerate(values):
        lines.append(f"  | {i} => {value}")
    lines.append("  | _ => 0")
    return "\n".join(lines)


def emit_lean(
    full_center,
    old_center,
    cert,
    witness,
    full_quad,
    old_quad,
    witness_norm,
    full_error,
    old_error,
):
    wmat, winv, gvec, common, inverse_scale, _ = cert
    event_quad = full_quad - old_quad
    first_nonzero = next(i for i, value in enumerate(witness) if value)
    first_value = witness[first_nonzero]
    data = "\n\n".join(
        [
            emit_fun2("fullAFun", full_center),
            emit_fun2("oldAFun", old_center),
            emit_fun2("fullWFun", wmat),
            emit_fun2("fullWiFun", winv),
            emit_fun1("fullGFun", gvec),
            emit_fun1("witnessFun", witness),
        ]
    )
    return f'''/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/

/-
Prime5Rescue12: kernel-checked finite matrix rescue at L = 327/100, m = 12.

The generated exact data prove a finite matrix statement only.  The source
interval computation externally found maximum center errors

  full: {float(full_error):.3e},  old {{2,3}}: {float(old_error):.3e},

both below delta = 1e-20.  Lean does not assume that computation: the final
theorem accepts containment of arbitrary real matrices in the stored
midpoint-plus/minus-delta intervals as explicit hypotheses.

All integer congruence, inverse, positivity, and witness identities are checked
by the Lean kernel using `decide`.  No statement about the infinite-dimensional
Weil operator, RH, or analytic interval containment is made here.

Generated by lean/make_prime5_rescue_certificate.py.
-/
import Mathlib
import CertFramework

namespace Prime5Rescue12

open Matrix Finset

set_option linter.style.longLine false
set_option linter.style.setOption false
set_option linter.style.maxHeartbeats false
set_option maxHeartbeats 200000000
set_option maxRecDepth 8192

noncomputable section

def scaleInt : Int := {DEN}
def shiftInt : Int := {SHIFT}
def deltaReal : ℝ := 1 / 10 ^ 20
def scaleReal : ℝ := 10 ^ 24

{data}

def fullAInt : Matrix (Fin 12) (Fin 12) ℤ :=
  Matrix.of fun i j => fullAFun i.val j.val

def oldAInt : Matrix (Fin 12) (Fin 12) ℤ :=
  Matrix.of fun i j => oldAFun i.val j.val

def fullWInt : Matrix (Fin 12) (Fin 12) ℤ :=
  Matrix.of fun i j => fullWFun i.val j.val

def fullWiInt : Matrix (Fin 12) (Fin 12) ℤ :=
  Matrix.of fun i j => fullWiFun i.val j.val

def fullGInt : Fin 12 → ℤ := fun k => fullGFun k.val

def fullBInt : Matrix (Fin 12) (Fin 12) ℤ :=
  Matrix.of fun i j => fullAInt i j - if i = j then shiftInt else 0

def witnessInt : Fin 12 → ℤ := fun k => witnessFun k.val

def fullCInt : Int := {common}
def fullFInt : Int := {inverse_scale}
def oldQuadInt : Int := {old_quad}
def fullQuadInt : Int := {full_quad}
def eventQuadInt : Int := {event_quad}
def witnessNormInt : Int := {witness_norm}

set_option maxHeartbeats 200000000 in
lemma fullKeyInt : ∀ i j : Fin 12,
    fullCInt ^ 2 * fullBInt i j =
      ∑ k, fullWInt k i * fullGInt k * fullWInt k j := by decide

set_option maxHeartbeats 200000000 in
lemma fullWinvInt : ∀ i j : Fin 12,
    (∑ k, fullWiInt i k * fullWInt k j) =
      if i = j then fullFInt else 0 := by decide

lemma fullGPosInt : ∀ k, 0 < fullGInt k := by decide
lemma fullCPosInt : (0 : ℤ) < fullCInt := by decide
lemma fullFPosInt : (0 : ℤ) < fullFInt := by decide

lemma oldWitnessIntIdentity :
    witnessInt ⬝ᵥ oldAInt *ᵥ witnessInt = oldQuadInt := by decide

lemma fullWitnessIntIdentity :
    witnessInt ⬝ᵥ fullAInt *ᵥ witnessInt = fullQuadInt := by decide

lemma witnessNormIntIdentity :
    witnessInt ⬝ᵥ witnessInt = witnessNormInt := by decide

lemma oldQuadInt_negative : oldQuadInt < 0 := by decide
lemma eventQuadInt_positive : 0 < eventQuadInt := by decide
lemma fullQuadInt_positive : 0 < fullQuadInt := by decide

def fullAReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => (fullAInt i j : ℝ)

def oldAReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => (oldAInt i j : ℝ)

def fullWReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => (fullWInt i j : ℝ)

def fullWiReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => (fullWiInt i j : ℝ)

def fullGReal : Fin 12 → ℝ := fun k => (fullGInt k : ℝ)

def witnessReal : Fin 12 → ℝ := fun k => (witnessInt k : ℝ)

def fullMidReal : Matrix (Fin 12) (Fin 12) ℝ :=
  (scaleReal)⁻¹ • fullAReal

def oldMidReal : Matrix (Fin 12) (Fin 12) ℝ :=
  (scaleReal)⁻¹ • oldAReal

def eventMidReal : Matrix (Fin 12) (Fin 12) ℝ :=
  fullMidReal - oldMidReal

def fullLowerReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => fullMidReal i j - deltaReal

def fullUpperReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => fullMidReal i j + deltaReal

def oldLowerReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => oldMidReal i j - deltaReal

def oldUpperReal : Matrix (Fin 12) (Fin 12) ℝ :=
  Matrix.of fun i j => oldMidReal i j + deltaReal

lemma fullKeyReal (i j : Fin 12) :
    (fullCInt : ℝ) ^ 2 *
        (fullAReal i j - if i = j then (shiftInt : ℝ) else 0) =
      ∑ k, fullWReal k i * fullGReal k * fullWReal k j := by
  have h := congrArg (fun z : ℤ => (z : ℝ)) (fullKeyInt i j)
  push_cast at h
  by_cases hij : i = j
  · subst j
    simpa [fullBInt, fullAReal, fullWReal, fullGReal] using h
  · simpa [fullBInt, fullAReal, fullWReal, fullGReal, hij] using h

lemma fullWinvReal (i j : Fin 12) :
    (∑ k, fullWiReal i k * fullWReal k j) =
      if i = j then (fullFInt : ℝ) else 0 := by
  have h := congrArg (fun z : ℤ => (z : ℝ)) (fullWinvInt i j)
  push_cast at h
  by_cases hij : i = j
  · subst j
    simpa [fullWiReal, fullWReal] using h
  · simpa [fullWiReal, fullWReal, hij] using h

lemma fullGPosReal : ∀ k, 0 < fullGReal k := by
  intro k
  unfold fullGReal
  exact_mod_cast fullGPosInt k

lemma boundsToAbs
    (M C : Matrix (Fin 12) (Fin 12) ℝ)
    (h : ∀ i j, C i j - deltaReal ≤ M i j ∧
      M i j ≤ C i j + deltaReal) :
    ∀ i j, |M i j - C i j| ≤ deltaReal := by
  intro i j
  rw [abs_le]
  constructor <;> linarith [h i j]

/-- Every real matrix in the stored full interval is strictly positive.
Analytic containment in this interval is intentionally a hypothesis. -/
theorem fullIntervalPositiveReal (M : Matrix (Fin 12) (Fin 12) ℝ)
    (hM : ∀ i j,
      fullLowerReal i j ≤ M i j ∧ M i j ≤ fullUpperReal i j)
    (x : Fin 12 → ℝ) (hx : x ≠ 0) :
    0 < x ⬝ᵥ M *ᵥ x := by
  have hclose : ∀ i j, |M i j - fullMidReal i j| ≤ deltaReal := by
    apply boundsToAbs M fullMidReal
    intro i j
    simpa [fullLowerReal, fullUpperReal] using hM i j
  refine CertFramework.cert_window_positive fullAReal fullWReal fullWiReal
    fullGReal (fullCInt : ℝ) (fullFInt : ℝ) (shiftInt : ℝ)
    scaleReal deltaReal fullKeyReal fullWinvReal fullGPosReal ?_ ?_ ?_ ?_ ?_
    M ?_ hx
  · exact_mod_cast fullCPosInt.ne'
  · exact_mod_cast fullFPosInt.ne'
  · norm_num [scaleReal]
  · norm_num [deltaReal]
  · norm_num [scaleReal, deltaReal, shiftInt]
  · intro i j
    have h := hclose i j
    have hmid : fullMidReal i j = fullAReal i j / scaleReal := by
      simp [fullMidReal, scaleReal, div_eq_mul_inv, mul_comm]
    rwa [hmid] at h

lemma oldWitnessARealIdentity :
    witnessReal ⬝ᵥ oldAReal *ᵥ witnessReal = (oldQuadInt : ℝ) := by
  have h := oldWitnessIntIdentity
  simp only [witnessReal, oldAReal, Matrix.of_apply, dotProduct, Matrix.mulVec] at h ⊢
  exact_mod_cast h

lemma fullWitnessARealIdentity :
    witnessReal ⬝ᵥ fullAReal *ᵥ witnessReal = (fullQuadInt : ℝ) := by
  have h := fullWitnessIntIdentity
  simp only [witnessReal, fullAReal, Matrix.of_apply, dotProduct, Matrix.mulVec] at h ⊢
  exact_mod_cast h

lemma witnessNormRealIdentity :
    witnessReal ⬝ᵥ witnessReal = (witnessNormInt : ℝ) := by
  have h := witnessNormIntIdentity
  simp only [witnessReal, dotProduct] at h ⊢
  exact_mod_cast h

lemma witnessReal_ne_zero : witnessReal ≠ 0 := by
  intro h
  have hc := congrFun h (⟨{first_nonzero}, by decide⟩ : Fin 12)
  norm_num [witnessReal, witnessInt, witnessFun] at hc

lemma oldMidWitnessValue :
    witnessReal ⬝ᵥ oldMidReal *ᵥ witnessReal =
      (oldQuadInt : ℝ) / scaleReal := by
  simp only [oldMidReal, smul_mulVec, dotProduct_smul, smul_eq_mul]
  rw [oldWitnessARealIdentity]
  simp [div_eq_mul_inv, mul_comm]

lemma fullMidWitnessValue :
    witnessReal ⬝ᵥ fullMidReal *ᵥ witnessReal =
      (fullQuadInt : ℝ) / scaleReal := by
  simp only [fullMidReal, smul_mulVec, dotProduct_smul, smul_eq_mul]
  rw [fullWitnessARealIdentity]
  simp [div_eq_mul_inv, mul_comm]

/-- Exact rational midpoint witness: the old {{2,3}} midpoint is negative. -/
theorem oldMidWitnessNegative :
    witnessReal ⬝ᵥ oldMidReal *ᵥ witnessReal < 0 := by
  rw [oldMidWitnessValue]
  norm_num [oldQuadInt, scaleReal]

/-- Exact rational midpoint witness: the p=5 event correction is positive. -/
theorem eventMidWitnessPositive :
    0 < witnessReal ⬝ᵥ eventMidReal *ᵥ witnessReal := by
  simp only [eventMidReal, sub_mulVec, dotProduct_sub]
  rw [fullMidWitnessValue, oldMidWitnessValue]
  norm_num [fullQuadInt, oldQuadInt, scaleReal]

lemma oldPerturbationNegative (Old : Matrix (Fin 12) (Fin 12) ℝ)
    (hOld : ∀ i j,
      oldLowerReal i j ≤ Old i j ∧ Old i j ≤ oldUpperReal i j) :
    witnessReal ⬝ᵥ Old *ᵥ witnessReal < 0 := by
  have hclose : ∀ i j, |Old i j - oldMidReal i j| ≤ deltaReal := by
    apply boundsToAbs Old oldMidReal
    intro i j
    simpa [oldLowerReal, oldUpperReal] using hOld i j
  let E : Matrix (Fin 12) (Fin 12) ℝ := Old - oldMidReal
  have hE : ∀ i j, |E i j| ≤ deltaReal := by
    intro i j
    simpa [E, Matrix.sub_apply] using hclose i j
  have herr := CertFramework.pert_bound E deltaReal (by norm_num [deltaReal])
    hE witnessReal
  have hupp : witnessReal ⬝ᵥ E *ᵥ witnessReal ≤
      12 * deltaReal * (witnessReal ⬝ᵥ witnessReal) :=
    (le_abs_self _).trans herr
  have hsplit : witnessReal ⬝ᵥ Old *ᵥ witnessReal =
      witnessReal ⬝ᵥ oldMidReal *ᵥ witnessReal +
        witnessReal ⬝ᵥ E *ᵥ witnessReal := by
    have hmat : Old = oldMidReal + E := by
      ext i j
      simp [E]
    rw [hmat, add_mulVec, dotProduct_add]
  rw [hsplit, oldMidWitnessValue, witnessNormRealIdentity] at *
  have hbudget :
      (oldQuadInt : ℝ) / scaleReal +
          12 * deltaReal * (witnessNormInt : ℝ) < 0 := by
    norm_num [oldQuadInt, witnessNormInt, scaleReal, deltaReal]
  linarith

lemma eventPerturbationPositive
    (Full Old : Matrix (Fin 12) (Fin 12) ℝ)
    (hFull : ∀ i j,
      fullLowerReal i j ≤ Full i j ∧ Full i j ≤ fullUpperReal i j)
    (hOld : ∀ i j,
      oldLowerReal i j ≤ Old i j ∧ Old i j ≤ oldUpperReal i j) :
    0 < witnessReal ⬝ᵥ (Full - Old) *ᵥ witnessReal := by
  have hf : ∀ i j, |Full i j - fullMidReal i j| ≤ deltaReal := by
    apply boundsToAbs Full fullMidReal
    intro i j
    simpa [fullLowerReal, fullUpperReal] using hFull i j
  have ho : ∀ i j, |Old i j - oldMidReal i j| ≤ deltaReal := by
    apply boundsToAbs Old oldMidReal
    intro i j
    simpa [oldLowerReal, oldUpperReal] using hOld i j
  let E : Matrix (Fin 12) (Fin 12) ℝ := (Full - Old) - eventMidReal
  have hE : ∀ i j, |E i j| ≤ 2 * deltaReal := by
    intro i j
    have hrewrite : E i j =
        (Full i j - fullMidReal i j) - (Old i j - oldMidReal i j) := by
      simp [E, eventMidReal, Matrix.sub_apply]
      ring
    rw [hrewrite]
    exact (abs_sub _ _).trans (by linarith [hf i j, ho i j])
  have herr := CertFramework.pert_bound E (2 * deltaReal)
    (by norm_num [deltaReal]) hE witnessReal
  have hlow : -(12 * (2 * deltaReal) *
      (witnessReal ⬝ᵥ witnessReal)) ≤
      witnessReal ⬝ᵥ E *ᵥ witnessReal := neg_le_of_abs_le herr
  have hsplit : witnessReal ⬝ᵥ (Full - Old) *ᵥ witnessReal =
      witnessReal ⬝ᵥ eventMidReal *ᵥ witnessReal +
        witnessReal ⬝ᵥ E *ᵥ witnessReal := by
    have hmat : Full - Old = eventMidReal + E := by
      ext i j
      simp [E]
    rw [hmat, add_mulVec, dotProduct_add]
  have hevent : witnessReal ⬝ᵥ eventMidReal *ᵥ witnessReal =
      ((fullQuadInt : ℝ) - oldQuadInt) / scaleReal := by
    simp only [eventMidReal, sub_mulVec, dotProduct_sub]
    rw [fullMidWitnessValue, oldMidWitnessValue]
    ring
  rw [hsplit, hevent, witnessNormRealIdentity] at *
  have hbudget : 0 <
      ((fullQuadInt : ℝ) - oldQuadInt) / scaleReal -
        12 * (2 * deltaReal) * (witnessNormInt : ℝ) := by
    norm_num [fullQuadInt, oldQuadInt, witnessNormInt, scaleReal, deltaReal]
  linarith

/-- Standalone finite rescue interface.  The two interval-containment
hypotheses are the entire analytic trust boundary. -/
theorem finitePrime5Rescue
    (Full Old : Matrix (Fin 12) (Fin 12) ℝ)
    (hFull : ∀ i j,
      fullLowerReal i j ≤ Full i j ∧ Full i j ≤ fullUpperReal i j)
    (hOld : ∀ i j,
      oldLowerReal i j ≤ Old i j ∧ Old i j ≤ oldUpperReal i j) :
    (∀ x : Fin 12 → ℝ, x ≠ 0 → 0 < x ⬝ᵥ Full *ᵥ x) ∧
      witnessReal ⬝ᵥ Old *ᵥ witnessReal < 0 ∧
      0 < witnessReal ⬝ᵥ (Full - Old) *ᵥ witnessReal := by
  refine ⟨?_, oldPerturbationNegative Old hOld,
    eventPerturbationPositive Full Old hFull hOld⟩
  intro x hx
  exact fullIntervalPositiveReal Full hFull x hx

end

end Prime5Rescue12
'''


def main() -> None:
    started = time.time()
    full_interval, _ = certified_spectral_form(L, M, N=320)
    a = L / 4
    old_interval = [[full_interval[i][j] for j in range(M)] for i in range(M)]
    v5 = iv.log(iv.mpf(5)) / F2iv(a)
    w5 = 2 * iv.log(iv.mpf(5)) / iv.sqrt(iv.mpf(5))
    for i in range(M):
        for j in range(M):
            if (i + j) % 2:
                continue
            value = iv.mpf(0)
            for coefficient in reversed(F_poly(i, j)):
                value = value * v5 + F2iv(coefficient)
            old_interval[i][j] = full_interval[i][j] + w5 * F2iv(a) * value

    full_center, full_error = rounded_centers(full_interval, "full")
    old_center, old_error = rounded_centers(old_interval, "old")
    cert = exact_ldl_certificate(full_center)
    witness = integer_witness(old_center)
    old_quad = quad(old_center, witness)
    full_quad = quad(full_center, witness)
    witness_norm = sum(value * value for value in witness)
    event_quad = full_quad - old_quad

    if not old_quad < 0 < full_quad or event_quad <= 0:
        raise ArithmeticError("witness does not exhibit the finite rescue")
    if Fraction(old_quad, DEN) + M * DELTA * witness_norm >= 0:
        raise ArithmeticError("old witness lacks interval-negative reserve")
    if Fraction(event_quad, DEN) - 2 * M * DELTA * witness_norm <= 0:
        raise ArithmeticError("event witness lacks interval-positive reserve")

    wmat, winv, gvec, common, inverse_scale, pivots = cert
    print(
        f"interval centers: full error={float(full_error):.3e}, "
        f"old error={float(old_error):.3e}"
    )
    print(
        f"full exact LDL: min pivot/scale={float(min(pivots) / DEN):.3e}; "
        f"digits A/W/Winv/g/c/f="
        f"{max(digits(v) for row in full_center for v in row)}/"
        f"{max(digits(v) for row in wmat for v in row)}/"
        f"{max(digits(v) for row in winv for v in row)}/"
        f"{max(digits(v) for v in gvec)}/{digits(common)}/{digits(inverse_scale)}"
    )
    print(
        f"witness: old={float(Fraction(old_quad, DEN * witness_norm)):.12e}, "
        f"event={float(Fraction(event_quad, DEN * witness_norm)):.12e}, "
        f"full={float(Fraction(full_quad, DEN * witness_norm)):.12e}"
    )

    output = emit_lean(
        full_center,
        old_center,
        cert,
        witness,
        full_quad,
        old_quad,
        witness_norm,
        full_error,
        old_error,
    )
    target = os.path.join(ROOT, "lean", "weilcert", "Prime5Rescue12.lean")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(output)
    print(f"wrote {target} ({len(output) / 1e6:.2f} MB) in {time.time()-started:.1f}s")


if __name__ == "__main__":
    main()
