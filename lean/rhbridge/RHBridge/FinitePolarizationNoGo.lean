/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Finite positive-polarization gate

Functional-equation duality pairs spectral parameters `rho` and `1 - rho`,
but that pairing is not positive.  This file records the smallest exact
countermodel.  The off-line real pair `1/2 + a, 1/2 - a` preserves the
standard alternating form for every `a`; when `a != 0`, however, no strictly
positive quadratic metric can satisfy the corresponding adjoint law.

The on-line real two-dimensional block is included as a positive control.
These lemmas do not assert anything about the zeta spectrum.  They show why a
positive cup/star metric is genuinely stronger than functional-equation
symmetry and why fitting such a metric after a finite spectrum is known would
be circular in an RH argument.
-/

namespace RHBridge.FinitePolarizationNoGo

open Matrix

/-- A real off-line functional-equation pair `1/2 +- a`. -/
def offLineGenerator (a : ℚ) : Matrix (Fin 2) (Fin 2) ℚ :=
  !![1 / 2 + a, 0; 0, 1 / 2 - a]

/-- The alternating duality pairing.  It is nondegenerate but not positive. -/
def alternatingPairing : Matrix (Fin 2) (Fin 2) ℚ :=
  !![0, 1; -1, 0]

/-- Functional-equation duality holds even for a genuinely off-line pair. -/
theorem offLine_preserves_alternating_duality (a : ℚ) :
    (offLineGenerator a)ᵀ * alternatingPairing +
      alternatingPairing * offLineGenerator a = alternatingPairing := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [offLineGenerator, alternatingPairing, Matrix.mul_apply] <;> ring

/-- Strict positivity of the quadratic form represented by a matrix. -/
def StrictQuadraticPositive (G : Matrix (Fin 2) (Fin 2) ℚ) : Prop :=
  ∀ x : Fin 2 → ℚ, x ≠ 0 → 0 < x ⬝ᵥ G *ᵥ x

/-- For `a != 0`, the positive adjoint equation forces the first diagonal
coefficient of the putative metric to vanish. -/
theorem offLine_adjoint_forces_g00_zero {a : ℚ} (ha : a ≠ 0)
    (G : Matrix (Fin 2) (Fin 2) ℚ)
    (hG : (offLineGenerator a)ᵀ * G + G * offLineGenerator a = G) :
    G 0 0 = 0 := by
  have h00raw := congrArg (fun M : Matrix (Fin 2) (Fin 2) ℚ => M 0 0) hG
  have h00 : (1 / 2 + a) * G 0 0 + G 0 0 * (1 / 2 + a) = G 0 0 := by
    simpa [offLineGenerator, Matrix.mul_apply] using h00raw
  have hprod : a * G 0 0 = 0 := by nlinarith [h00]
  exact (mul_eq_zero.mp hprod).resolve_left ha

/-- The off-line duality block admits no strictly positive metric satisfying
`A^T G + G A = G`. -/
theorem no_positive_adjoint_metric_offLine {a : ℚ} (ha : a ≠ 0) :
    ¬ ∃ G : Matrix (Fin 2) (Fin 2) ℚ,
      (offLineGenerator a)ᵀ * G + G * offLineGenerator a = G ∧
        StrictQuadraticPositive G := by
  rintro ⟨G, hG, hpos⟩
  have hg00 : G 0 0 = 0 := offLine_adjoint_forces_g00_zero ha G hG
  have hone : (![1, 0] : Fin 2 → ℚ) ≠ 0 := by decide
  have := hpos ![1, 0] hone
  simp [dotProduct, Matrix.mulVec, hg00] at this

/-- A critical-line conjugate pair, represented over the reals. -/
def onLineGenerator (gamma : ℚ) : Matrix (Fin 2) (Fin 2) ℚ :=
  !![1 / 2, -gamma; gamma, 1 / 2]

/-- The identity metric satisfies the adjoint law for the on-line block. -/
theorem onLine_identity_adjoint (gamma : ℚ) :
    (onLineGenerator gamma)ᵀ * (1 : Matrix (Fin 2) (Fin 2) ℚ) +
      (1 : Matrix (Fin 2) (Fin 2) ℚ) * onLineGenerator gamma = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [onLineGenerator] <;> ring

/-- The identity metric used by the on-line control is strictly positive. -/
theorem identity_strictQuadraticPositive :
    StrictQuadraticPositive (1 : Matrix (Fin 2) (Fin 2) ℚ) := by
  intro x hx
  simp only [one_mulVec, dotProduct]
  have hcoord : x 0 ≠ 0 ∨ x 1 ≠ 0 := by
    by_contra h
    simp only [not_or, not_not] at h
    apply hx
    funext i
    fin_cases i <;> simp [h.1, h.2]
  simp only [Fin.sum_univ_two]
  rcases hcoord with h0 | h1
  · nlinarith [sq_pos_of_ne_zero h0]
  · nlinarith [sq_pos_of_ne_zero h1]

end RHBridge.FinitePolarizationNoGo
