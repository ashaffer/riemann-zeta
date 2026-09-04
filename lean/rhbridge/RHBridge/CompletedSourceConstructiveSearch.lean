/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Finite algebra for the constructive completed-source search

This file kernel-checks only the elementary algebra behind the audit:

* finite Neumann/source words have an exact geometric remainder;
* the remainder is the full charge at the contact value `K = -1`;
* a regular convolution parametrix acts as the identity on a zero of its
  annihilator symbol; and
* the paired four-root Cauchy kernel has Suzuki's rational closed form; and
* a three-coordinate model can obey both an annihilator equation and a zero
  old compression while retaining nonzero old-to-exterior charge.

It does not formalize the completed-zeta operator, the analytic
mean-periodic convolution, kernel-null charge, a zero-free strip, or RH.
-/

namespace RHBridge.CompletedSourceConstructiveSearch

noncomputable section

/-- The first `m` terms of the formal inverse of `1 + k`. -/
def finiteSourceSum : Nat → ℝ → ℝ
  | 0, _ => 0
  | m + 1, k => finiteSourceSum m k + (-k) ^ m

/-- Exact finite geometric division, including its terminal remainder. -/
theorem finiteSourceSum_division (m : Nat) (k : ℝ) :
    finiteSourceSum m k * (1 + k) + (-k) ^ m = 1 := by
  induction m with
  | zero => simp [finiteSourceSum]
  | succ m ih =>
      rw [finiteSourceSum]
      rw [add_mul, pow_succ]
      nlinarith

/-- Scalar form of `Gamma = T_m A + Gamma (-K)^m`. -/
theorem finite_source_word_exact
    (m : Nat) (k gamma : ℝ) :
    gamma =
      (gamma * finiteSourceSum m k) * (1 + k) + gamma * (-k) ^ m := by
  have h := finiteSourceSum_division m k
  calc
    gamma = gamma * 1 := by ring
    _ = gamma * (finiteSourceSum m k * (1 + k) + (-k) ^ m) := by rw [h]
    _ = (gamma * finiteSourceSum m k) * (1 + k) + gamma * (-k) ^ m := by ring

/-- At a contact, every finite source-word remainder is the original charge. -/
theorem finite_source_contact_remainder
    (m : Nat) (gamma : ℝ) :
    gamma * (-(-1 : ℝ)) ^ m = gamma := by
  simp

/-- More generally, no regular scalar polynomial value changes the residual
at the contact spectral point. -/
theorem regular_polynomial_contact_residual
    (p gamma : ℝ) :
    gamma * (1 - (1 + (-1 : ℝ)) * p) = gamma := by
  ring

/-- A regular multiplier parametrix has residual one at every zero of the
annihilator symbol. -/
theorem regular_parametrix_residual_at_zero
    (parametrix symbol : ℂ) (hsymbol : symbol = 0) :
    1 - parametrix * symbol = 1 := by
  rw [hsymbol, mul_zero, sub_zero]

/-- Pairing the Cauchy channels at the fourth roots `1`, `-1`, `i`, `-i`
gives the rational derivative of the Lerch channel.  The two nonreal terms
have already been combined as `2*q/(q^2+1)`.  This is the finite algebraic
identity only; the Lerch-series differentiation is not formalized here. -/
theorem four_cauchy_pairing
    (q : ℝ) (hminus : q - 1 ≠ 0) (hplus : q + 1 ≠ 0) :
    1 / (q - 1) + 1 / (q + 1) + 2 * q / (q ^ 2 + 1) =
      4 * q ^ 3 / (q ^ 4 - 1) := by
  have himag : q ^ 2 + 1 ≠ 0 := by
    nlinarith [sq_nonneg q]
  have hfactor : q ^ 4 - 1 = (q - 1) * (q + 1) * (q ^ 2 + 1) := by
    ring
  have hfour : q ^ 4 - 1 ≠ 0 := by
    rw [hfactor]
    exact mul_ne_zero (mul_ne_zero hminus hplus) himag
  field_simp [hminus, hplus, himag, hfour]
  <;> ring

section AnnihilatorCountermodel

/-- A symmetric source map whose first and third rows agree. -/
def sourceMap (v : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![v 1, v 0 + v 2, v 1]

/-- Projection onto the first (old) coordinate. -/
def oldProjection (v : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![v 0, 0, 0]

/-- Projection onto the two exterior coordinates. -/
def exteriorProjection (v : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![0, v 1, v 2]

/-- Orthogonal projection onto the line spanned by `(1,0,-1)`. -/
def annihilatorMap (v : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![(v 0 - v 2) / 2, 0, (v 2 - v 0) / 2]

/-- The source is annihilated after postcomposition. -/
theorem annihilator_source_zero (v : Fin 3 → ℝ) :
    annihilatorMap (sourceMap v) = 0 := by
  funext i
  fin_cases i <;> simp [annihilatorMap, sourceMap]

/-- Its old-to-old compression is also zero. -/
theorem old_source_old_zero (v : Fin 3 → ℝ) :
    oldProjection (sourceMap (oldProjection v)) = 0 := by
  funext i
  fin_cases i <;> simp [oldProjection, sourceMap]

/-- The first old basis vector nevertheless has a nonzero exterior charge. -/
theorem annihilator_equation_does_not_kill_charge :
    exteriorProjection
        (sourceMap (oldProjection ![(1 : ℝ), 0, 0])) =
      ![(0 : ℝ), 1, 0] := by
  ext i
  fin_cases i <;> simp [exteriorProjection, sourceMap, oldProjection]

end AnnihilatorCountermodel

end

end RHBridge.CompletedSourceConstructiveSearch
