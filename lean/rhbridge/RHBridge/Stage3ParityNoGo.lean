/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Data.Real.Basic

/-!
# Parity no-go model for the finite determinant route

Reflection commutation and simplicity do not force the lowest eigenvector to
be even.  The missing zeta-specific input is a comparison of the even and odd
spectral blocks.
-/

namespace RHP2Bridge.Stage3ParityNoGo

def reflection (x : ℝ × ℝ) : ℝ × ℝ := (x.1, -x.2)
def groundOperator (x : ℝ × ℝ) : ℝ × ℝ := (x.1, 0)
def oddGround : ℝ × ℝ := (0, 1)
def evenBoundary (x : ℝ × ℝ) : ℝ := x.1

theorem reflection_involution (x : ℝ × ℝ) :
    reflection (reflection x) = x := by
  rcases x with ⟨x, y⟩
  simp [reflection]

theorem operator_commutes_reflection (x : ℝ × ℝ) :
    groundOperator (reflection x) = reflection (groundOperator x) := by
  rcases x with ⟨x, y⟩
  simp [reflection, groundOperator]

theorem oddGround_nonzero : oddGround ≠ 0 := by
  intro h
  have := congrArg Prod.snd h
  simp [oddGround] at this

theorem oddGround_zeroEigenvalue : groundOperator oddGround = 0 := by
  simp [groundOperator, oddGround]

theorem zeroEigenspace_simple (w : ℝ × ℝ)
    (hw : groundOperator w = 0) :
    ∃ c : ℝ, w = c • oddGround := by
  rcases w with ⟨x, y⟩
  have hx : x = 0 := by
    have h := congrArg Prod.fst hw
    simpa [groundOperator] using h
  subst x
  refine ⟨y, ?_⟩
  simp [oddGround]

theorem oddGround_is_odd : reflection oddGround = -oddGround := by
  simp [reflection, oddGround]

theorem evenBoundary_invariant (x : ℝ × ℝ) :
    evenBoundary (reflection x) = evenBoundary x := by
  rfl

theorem evenBoundary_annihilates_oddGround : evenBoundary oddGround = 0 := by
  rfl

/-- Simplicity, reflection invariance, and an even boundary functional are
compatible with an odd simple ground state annihilated by the boundary. -/
theorem simplicity_does_not_force_evenness :
    oddGround ≠ 0 ∧
    groundOperator oddGround = 0 ∧
    (∀ w : ℝ × ℝ, groundOperator w = 0 →
      ∃ c : ℝ, w = c • oddGround) ∧
    reflection oddGround = -oddGround ∧
    evenBoundary oddGround = 0 := by
  exact ⟨oddGround_nonzero, oddGround_zeroEigenvalue,
    zeroEigenspace_simple, oddGround_is_odd,
    evenBoundary_annihilates_oddGround⟩

end RHP2Bridge.Stage3ParityNoGo
