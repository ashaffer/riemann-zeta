/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-!
# A triangular-packet cone does not certify a Toeplitz form

This file checks the exact scalar algebra behind the smallest counterexample
to lifting positivity on all modulated interval packets to positivity of the
whole compressed convolution form.

The analytic interpretation is in
`results/TRIANGULAR-PACKET-CONE-NOGO.md`.  No zeta or explicit-formula axiom is
used here.
-/

namespace RHBridge.SelbergPacketConeNoGo

noncomputable section

/-- The real quadratic form of the `3 x 3` Toeplitz matrix with diagonal one,
second off-diagonal `5/4`, and first off-diagonal zero. -/
def toeplitzThreeQuadratic (x₀ x₁ x₂ : ℝ) : ℝ :=
  x₀ ^ 2 + x₁ ^ 2 + x₂ ^ 2 + (5 / 2 : ℝ) * x₀ * x₂

/-- The antisymmetric endpoint vector is a strictly negative direction. -/
theorem toeplitzThreeQuadratic_endpointWitness :
    toeplitzThreeQuadratic 1 0 (-1) = -(1 / 2 : ℝ) := by
  norm_num [toeplitzThreeQuadratic]

/-- The value of the same Toeplitz form on the full modulated box
`(1, exp(i theta), exp(2 i theta))`. -/
def fullPacketValue (θ : ℝ) : ℝ :=
  3 + (5 / 2 : ℝ) * Real.cos (2 * θ)

/-- Every full-width modulated packet retains a uniform positive margin. -/
theorem fullPacketValue_ge_half (θ : ℝ) :
    (1 / 2 : ℝ) ≤ fullPacketValue θ := by
  have hcos : -(1 : ℝ) ≤ Real.cos (2 * θ) := Real.neg_one_le_cos _
  dsimp [fullPacketValue]
  linarith

/-- The continuous rational countermodel's value on an unnormalized
modulated interval of length `ell`.  It corresponds to window length `3/2`,
shift `1`, and shift coefficient `5/4`. -/
def intervalPacketValue (ell phase : ℝ) : ℝ :=
  ell + (5 / 2 : ℝ) * max (ell - 1) 0 * Real.cos phase

/-- Every interval width, position, and modulation in the continuous model
has normalized Rayleigh value at least `1/6`.  Position does not enter the
scalar formula because the kernel is translation invariant on each overlap. -/
theorem intervalPacketValue_ge_sixth
    {ell : ℝ} (hell_pos : 0 < ell) (hell_le : ell ≤ 3 / 2)
    (phase : ℝ) :
    ell / 6 ≤ intervalPacketValue ell phase := by
  by_cases hsmall : ell ≤ 1
  · have hmax : max (ell - 1) 0 = 0 := by
      rw [max_eq_right]
      linarith
    rw [intervalPacketValue, hmax]
    norm_num
    linarith
  · have hsub : 0 ≤ ell - 1 := by linarith
    have hmax : max (ell - 1) 0 = ell - 1 := max_eq_left hsub
    have hcos : -(1 : ℝ) ≤ Real.cos phase := Real.neg_one_le_cos _
    have hscale : 0 ≤ (5 / 2 : ℝ) * (ell - 1) := by positivity
    have hmul := mul_le_mul_of_nonneg_left hcos hscale
    rw [intervalPacketValue, hmax]
    nlinarith

/-- In particular every nonempty modulated interval has strictly positive
form value. -/
theorem intervalPacketValue_pos
    {ell : ℝ} (hell_pos : 0 < ell) (hell_le : ell ≤ 3 / 2)
    (phase : ℝ) :
    0 < intervalPacketValue ell phase := by
  have h := intervalPacketValue_ge_sixth hell_pos hell_le phase
  nlinarith

/-- The two-block antisymmetric direction has normalized Rayleigh quotient
`-1/4` in the continuous countermodel. -/
theorem antisymmetricTwoBlockRayleigh :
    (2 * (1 - (5 / 4 : ℝ))) / 2 = -(1 / 4 : ℝ) := by
  norm_num

/-- Positivity on the symmetric and antisymmetric combinations of two equal-
diagonal vectors is exactly the absolute cross-term bound.  This is the
scalar core of the fixed-box `2 x 2` positivity checkpoint. -/
theorem twoBox_nonnegative_iff_abs_le (q b : ℝ) :
    (0 ≤ q + b ∧ 0 ≤ q - b) ↔ |b| ≤ q := by
  rw [abs_le]
  constructor
  · rintro ⟨hplus, hminus⟩
    constructor <;> linarith
  · rintro ⟨hlower, hupper⟩
    constructor <;> linarith

/-- Once orthogonality has shown that a common reference-norm shift affects
only the common diagonal, the same scalar criterion applies. -/
theorem shiftedTwoBox_nonnegative_iff_abs_le (q b c : ℝ) :
    (0 ≤ q + c + b ∧ 0 ≤ q + c - b) ↔ |b| ≤ q + c := by
  exact twoBox_nonnegative_iff_abs_le (q + c) b

end

end RHBridge.SelbergPacketConeNoGo
