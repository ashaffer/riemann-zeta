/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.FixedWindowStripReduction

/-!
# Long-mollifier exponent savings imply symmetric zero-free strips

This file formalizes only the elementary exponent arithmetic behind the
averaged long-mollifier criterion. It neither assumes nor proves the open
mollified second-moment estimate.
-/

namespace RHP2Bridge.LongMollifierStripReduction

open GuinandWeilFormula

noncomputable section

/-- Natural exponent of the cutoff-averaged moment when the mollifier has
length `T^theta`. -/
def naturalMomentExponent (theta : ℝ) : ℝ := theta + 1

/-- Right boundary supplied by the averaged mollifier criterion at exponent
`theta + 1`: `(theta + 1) / (2 * theta)`. -/
def rightBoundary (theta : ℝ) : ℝ :=
  (theta + 1) / (2 * theta)

/-- Symmetric strip width corresponding to the right boundary. -/
def stripWidth (theta : ℝ) : ℝ :=
  (theta - 1) / (2 * theta)

/-- Mollifier exponent needed to target a prescribed symmetric strip width. -/
def thetaForStripWidth (eta : ℝ) : ℝ :=
  1 / (1 - 2 * eta)

/-- Every nontrivial zero obeys a specified right-real-part bound. -/
def RightZeroBound (boundary : ℝ) : Prop :=
  ∀ rho : NontrivialZetaZero, rho.val.re ≤ boundary

/-- Abstract real-part reflection closure of the nontrivial zero set. The
functional equation supplies this property analytically; it is kept explicit
here so that this arithmetic module imports no zero-free conclusion. -/
def RealPartReflectionClosed : Prop :=
  ∀ rho : NontrivialZetaZero,
    ∃ reflected : NontrivialZetaZero,
      reflected.val.re = 1 - rho.val.re

theorem rightBoundary_eq_one_sub_stripWidth
    {theta : ℝ} (htheta : theta ≠ 0) :
    rightBoundary theta = 1 - stripWidth theta := by
  unfold rightBoundary stripWidth
  field_simp [htheta]
  ring

theorem rightBoundary_eq_half_add_reciprocal
    {theta : ℝ} (htheta : theta ≠ 0) :
    rightBoundary theta = 1 / 2 + 1 / (2 * theta) := by
  unfold rightBoundary
  field_simp [htheta]
  ring

theorem stripWidth_eq_half_sub_reciprocal
    {theta : ℝ} (htheta : theta ≠ 0) :
    stripWidth theta = 1 / 2 - 1 / (2 * theta) := by
  unfold stripWidth
  field_simp [htheta]
  ring

theorem stripWidth_pos {theta : ℝ} (htheta : 1 < theta) :
    0 < stripWidth theta := by
  unfold stripWidth
  exact div_pos (sub_pos.mpr htheta)
    (mul_pos (by norm_num) (lt_trans zero_lt_one htheta))

theorem stripWidth_lt_half {theta : ℝ} (htheta : 1 < theta) :
    stripWidth theta < 1 / 2 := by
  have htheta_pos : 0 < theta := lt_trans zero_lt_one htheta
  rw [stripWidth_eq_half_sub_reciprocal (ne_of_gt htheta_pos)]
  have hreciprocal : 0 < 1 / (2 * theta) := by
    exact one_div_pos.mpr (mul_pos (by norm_num) htheta_pos)
  linarith

theorem rightBoundary_gt_half {theta : ℝ} (htheta : 1 < theta) :
    1 / 2 < rightBoundary theta := by
  have htheta_pos : 0 < theta := lt_trans zero_lt_one htheta
  rw [rightBoundary_eq_half_add_reciprocal (ne_of_gt htheta_pos)]
  have hreciprocal : 0 < 1 / (2 * theta) := by
    exact one_div_pos.mpr (mul_pos (by norm_num) htheta_pos)
  linarith

theorem rightBoundary_lt_one {theta : ℝ} (htheta : 1 < theta) :
    rightBoundary theta < 1 := by
  rw [rightBoundary_eq_one_sub_stripWidth
    (ne_of_gt (lt_trans zero_lt_one htheta))]
  linarith [stripWidth_pos htheta]

/-- The decisive exponent comparison. For positive `theta`, asking for a
zero-free line strictly to the right of the conditional boundary is exactly
asking that the detector exponent `2 * sigma * theta` exceed the natural
moment exponent `theta + 1`. -/
theorem rightBoundary_lt_iff_exponent_gap
    {theta sigma : ℝ} (htheta : 0 < theta) :
    rightBoundary theta < sigma ↔
      naturalMomentExponent theta < 2 * sigma * theta := by
  change (theta + 1) / (2 * theta) < sigma ↔
    theta + 1 < 2 * sigma * theta
  have hdenominator : 0 < 2 * theta :=
    mul_pos (by norm_num) htheta
  constructor
  · intro h
    have hcross := (div_lt_iff₀ hdenominator).mp h
    nlinarith
  · intro h
    apply (div_lt_iff₀ hdenominator).mpr
    nlinarith

theorem exponent_gap_pos
    {theta sigma : ℝ} (htheta : 0 < theta)
    (hsigma : rightBoundary theta < sigma) :
    0 < 2 * sigma * theta - naturalMomentExponent theta := by
  have hgap :=
    (rightBoundary_lt_iff_exponent_gap htheta).mp hsigma
  linarith

theorem thetaForStripWidth_gt_one
    {eta : ℝ} (heta_pos : 0 < eta) (heta_half : eta < 1 / 2) :
    1 < thetaForStripWidth eta := by
  unfold thetaForStripWidth
  have hdenominator : 0 < 1 - 2 * eta := by linarith
  apply (lt_div_iff₀ hdenominator).mpr
  linarith

theorem stripWidth_thetaForStripWidth
    {eta : ℝ} (heta_pos : 0 < eta) (heta_half : eta < 1 / 2) :
    stripWidth (thetaForStripWidth eta) = eta := by
  have hdenominator : 1 - 2 * eta ≠ 0 := by
    exact ne_of_gt (by linarith)
  unfold stripWidth thetaForStripWidth
  field_simp [hdenominator]
  ring

theorem rightBoundary_thetaForStripWidth
    {eta : ℝ} (heta_pos : 0 < eta) (heta_half : eta < 1 / 2) :
    rightBoundary (thetaForStripWidth eta) = 1 - eta := by
  rw [rightBoundary_eq_one_sub_stripWidth]
  · rw [stripWidth_thetaForStripWidth heta_pos heta_half]
  · unfold thetaForStripWidth
    exact one_div_ne_zero (by linarith)

/-- A right-half-plane zero bound plus real-part reflection gives the complete
symmetric strip. This is the precise logical use of the functional equation. -/
theorem closedStrip_of_longMollifierRightBound
    {theta : ℝ} (htheta : theta ≠ 0)
    (hright : RightZeroBound (rightBoundary theta))
    (hreflect : RealPartReflectionClosed) :
    FixedWindowStripReduction.NontrivialZerosInClosedStrip
      (stripWidth theta) := by
  intro rho
  have hupper := hright rho
  obtain ⟨reflected, hreflected⟩ := hreflect rho
  have hreflectedUpper := hright reflected
  rw [hreflected,
    rightBoundary_eq_one_sub_stripWidth htheta] at hreflectedUpper
  constructor
  · linarith
  · simpa [rightBoundary_eq_one_sub_stripWidth htheta] using hupper

/-- Equivalent displacement formulation of the same symmetric strip. -/
theorem closedStrip_of_longMollifierDisplacement
    {theta : ℝ} (htheta : 1 < theta)
    (hdisp : FixedWindowStripReduction.HorizontalDisplacementAtMost
      (1 / (2 * theta))) :
    FixedWindowStripReduction.NontrivialZerosInClosedStrip
      (stripWidth theta) := by
  apply FixedWindowStripReduction.closedStrip_of_displacementAtMost hdisp
  have htheta_ne : theta ≠ 0 :=
    ne_of_gt (lt_trans zero_lt_one htheta)
  rw [stripWidth_eq_half_sub_reciprocal htheta_ne]
  ring_nf

end

end RHP2Bridge.LongMollifierStripReduction
