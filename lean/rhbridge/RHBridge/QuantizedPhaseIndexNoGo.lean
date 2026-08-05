/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.FunProp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Finite quantized-phase gate

This file records the algebraic core of the fail-fast audit for a quantized
completed phase.  A functional-equation quartet has a strictly positive
factor on the real centered line, so ordinary real-line phase cannot see it.
Its exact expansion is the algebraic input to the normalized compact-open
estimate when the quartet is moved to large height.

At a finite prime, the functional-equation-normalized Euler phase is already
null-homotopic: scaling its disk radius to zero gives a path of nonvanishing
unit phases.  The lemmas below prove the nonvanishing and unit-norm facts
needed for that contraction.  They do not claim a topological classification
of every possible global zeta index.
-/

namespace RHBridge.QuantizedPhaseIndexNoGo

open scoped ComplexConjugate

/-- The centered even polynomial whose roots are `+-gamma +- i delta`. -/
def quartetFactor (gamma delta x : ℚ) : ℚ :=
  ((x - gamma) ^ 2 + delta ^ 2) * ((x + gamma) ^ 2 + delta ^ 2)

/-- Exact expansion used in the compact-open remote-quartet estimate. -/
theorem quartetFactor_expansion (gamma delta x : ℚ) :
    quartetFactor gamma delta x =
      (gamma ^ 2 + delta ^ 2) ^ 2 +
        2 * (delta ^ 2 - gamma ^ 2) * x ^ 2 + x ^ 4 := by
  simp only [quartetFactor]
  ring

/-- Functional-equation reflection makes the quartet factor even. -/
theorem quartetFactor_even (gamma delta x : ℚ) :
    quartetFactor gamma delta (-x) = quartetFactor gamma delta x := by
  simp only [quartetFactor]
  ring

/-- A genuine quartet is strictly positive on the real centered line. -/
theorem quartetFactor_pos {gamma delta x : ℚ} (hdelta : delta ≠ 0) :
    0 < quartetFactor gamma delta x := by
  have hd : 0 < delta ^ 2 := sq_pos_of_ne_zero hdelta
  have hleft : 0 < (x - gamma) ^ 2 + delta ^ 2 :=
    add_pos_of_nonneg_of_pos (sq_nonneg _) hd
  have hright : 0 < (x + gamma) ^ 2 + delta ^ 2 :=
    add_pos_of_nonneg_of_pos (sq_nonneg _) hd
  exact mul_pos hleft hright

/-- Multiplying real critical-line data by a genuine quartet changes no sign. -/
theorem mul_quartet_nonneg_iff {gamma delta x value : ℚ}
    (hdelta : delta ≠ 0) :
    0 ≤ value * quartetFactor gamma delta x ↔ 0 ≤ value := by
  have hq : 0 < quartetFactor gamma delta x := quartetFactor_pos hdelta
  constructor
  · intro hproduct
    by_contra hvalue
    have hv : value < 0 := lt_of_not_ge hvalue
    exact (not_lt_of_ge hproduct) (mul_neg_of_neg_of_pos hv hq)
  · intro hvalue
    exact mul_nonneg hvalue hq.le

/-- The normalized local Euler phase on one prime-circle coordinate. -/
noncomputable def localEulerPhase (r : ℝ) (z : ℂ) : ℂ :=
  (1 - (r : ℂ) * conj z) / (1 - (r : ℂ) * z)

/-- Radial contraction of a local Euler loop to the constant loop one. -/
noncomputable def localEulerHomotopy (r t : ℝ) (z : ℂ) : ℂ :=
  localEulerPhase (t * r) z

/-- The radial contraction starts at the constant phase one. -/
theorem localEulerHomotopy_zero (r : ℝ) (z : ℂ) :
    localEulerHomotopy r 0 z = 1 := by
  simp [localEulerHomotopy, localEulerPhase]

/-- At time one the radial contraction is the original local Euler phase. -/
@[simp] theorem localEulerHomotopy_one (r : ℝ) (z : ℂ) :
    localEulerHomotopy r 1 z = localEulerPhase r z := by
  simp [localEulerHomotopy]

/-- A disk Euler denominator stays nonzero throughout the radial contraction. -/
theorem localEulerDenominator_ne_zero {r t : ℝ} {z : ℂ}
    (hr : |r| < 1) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) (hz : ‖z‖ = 1) :
    (1 : ℂ) - ((t * r : ℝ) : ℂ) * z ≠ 0 := by
  have har : 0 ≤ |r| := abs_nonneg r
  have hmul : 0 ≤ (1 - t) * |r| :=
    mul_nonneg (sub_nonneg.mpr ht1) har
  have habs : |t * r| < 1 := by
    rw [abs_mul, abs_of_nonneg ht0]
    nlinarith
  have hnorm : ‖(((t * r : ℝ) : ℂ) * z)‖ < 1 := by
    rw [norm_mul, Complex.norm_real, hz, mul_one]
    exact habs
  intro hzero
  have heq : (((t * r : ℝ) : ℂ) * z) = 1 :=
    (sub_eq_zero.mp hzero).symm
  rw [heq, norm_one] at hnorm
  exact (lt_irrefl 1) hnorm

/-- Every stage of the finite-prime radial contraction has unit norm. -/
theorem localEulerHomotopy_norm_eq_one {r t : ℝ} {z : ℂ}
    (hr : |r| < 1) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) (hz : ‖z‖ = 1) :
    ‖localEulerHomotopy r t z‖ = 1 := by
  have hden := localEulerDenominator_ne_zero hr ht0 ht1 hz
  have hconj :
      (1 : ℂ) - ((t * r : ℝ) : ℂ) * conj z =
        conj ((1 : ℂ) - ((t * r : ℝ) : ℂ) * z) := by
    simp
  rw [localEulerHomotopy, localEulerPhase, norm_div, hconj,
    Complex.norm_conj]
  exact div_self (norm_ne_zero_iff.mpr hden)

/-- The local radial homotopy remains in the nonzero complex numbers. -/
theorem localEulerHomotopy_ne_zero {r t : ℝ} {z : ℂ}
    (hr : |r| < 1) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) (hz : ‖z‖ = 1) :
    localEulerHomotopy r t z ≠ 0 := by
  apply norm_ne_zero_iff.mp
  rw [localEulerHomotopy_norm_eq_one hr ht0 ht1 hz]
  exact one_ne_zero

/-- The radial formula is an actual continuous homotopy on the prime circle. -/
theorem localEulerHomotopy_continuousOn {r : ℝ} (hr : |r| < 1) :
    ContinuousOn
      (fun x : ℝ × ℂ => localEulerHomotopy r x.1 x.2)
      (Set.Icc (0 : ℝ) 1 ×ˢ Metric.sphere (0 : ℂ) 1) := by
  apply ContinuousOn.div
  · fun_prop [localEulerHomotopy, localEulerPhase]
  · fun_prop [localEulerHomotopy, localEulerPhase]
  · intro x hx
    apply localEulerDenominator_ne_zero hr hx.1.1 hx.1.2
    simpa [Metric.mem_sphere] using hx.2

end RHBridge.QuantizedPhaseIndexNoGo
