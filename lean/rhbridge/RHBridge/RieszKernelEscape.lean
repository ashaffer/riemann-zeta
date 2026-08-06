/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.Real.Sqrt
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Scalar geometry of nested Riesz-kernel escape

Suppose a consistent bounded functional on a smaller Hilbert space has Riesz
vector `vSmall`, while its restriction to a larger nested space has Riesz
vector `vLarge`.  Orthogonal projection sends `vLarge` to `vSmall`.  If their
squared norms are `small` and `large`, the squared mass retained by the old
space is `small / large`, the normalized coherence is its square root, and
the complementary projection mass is `1 - small / large`.

This file checks those scalar consequences and the elementary Riesz lower
bound used by the Suzuki defect-escape argument.  The analytic inputs--the
Riesz projection identity, translation invariance, density of the nested
union, and weak convergence--are stated and proved in the companion report;
they are deliberately not hidden behind Lean axioms here.
-/

namespace RHBridge.RieszKernelEscape

noncomputable section

/-- Fraction of the larger Riesz vector's squared norm retained by projection
onto the smaller nested space. -/
def projectionMass (small large : ℝ) : ℝ :=
  small / large

/-- Coherence of the two normalized Riesz vectors under the projection
identity. -/
def normalizedCoherence (small large : ℝ) : ℝ :=
  Real.sqrt (projectionMass small large)

/-- Squared norm fraction outside the old nested space. -/
def projectionTailFraction (small large : ℝ) : ℝ :=
  1 - projectionMass small large

/-- Minimum squared distance after aligning the phases of two normalized
vectors whose coherence is `normalizedCoherence`. -/
def normalizedDistanceSq (small large : ℝ) : ℝ :=
  2 * (1 - normalizedCoherence small large)

/-- Riesz/Cauchy lower bound produced by a vector of energy `energy`, absolute
functional value `pairing`, and multiplicative translation amplification
`amplification`. -/
def rieszNormSqLowerBound
    (pairing energy amplification : ℝ) : ℝ :=
  amplification ^ 2 * pairing ^ 2 / energy

theorem projectionMass_nonneg
    {small large : ℝ} (hsmall : 0 ≤ small) (hlarge : 0 < large) :
    0 ≤ projectionMass small large := by
  exact div_nonneg hsmall hlarge.le

theorem projectionMass_le_one
    {small large : ℝ} (hlarge : 0 < large) (hnested : small ≤ large) :
    projectionMass small large ≤ 1 := by
  unfold projectionMass
  rw [div_le_one hlarge]
  exact hnested

/-- The square of normalized coherence is exactly the retained projection
mass. -/
theorem normalizedCoherence_sq
    {small large : ℝ} (hsmall : 0 ≤ small) (hlarge : 0 < large) :
    normalizedCoherence small large ^ 2 = projectionMass small large := by
  unfold normalizedCoherence
  exact Real.sq_sqrt (projectionMass_nonneg hsmall hlarge)

theorem normalizedCoherence_nonneg (small large : ℝ) :
    0 ≤ normalizedCoherence small large := by
  exact Real.sqrt_nonneg _

theorem normalizedCoherence_le_one
    {small large : ℝ} (hsmall : 0 ≤ small) (hlarge : 0 < large)
    (hnested : small ≤ large) :
    normalizedCoherence small large ≤ 1 := by
  have hsq := normalizedCoherence_sq hsmall hlarge
  have hmass := projectionMass_le_one hlarge hnested
  have hnonneg := normalizedCoherence_nonneg small large
  nlinarith

theorem projectionTailFraction_nonneg
    {small large : ℝ} (hlarge : 0 < large) (hnested : small ≤ large) :
    0 ≤ projectionTailFraction small large := by
  unfold projectionTailFraction
  linarith [projectionMass_le_one hlarge hnested]

/-- A strict increase in Riesz norm forces a positive projection tail and
coherence strictly below one. -/
theorem projectionTailFraction_pos
    {small large : ℝ} (hlarge : 0 < large) (hstrict : small < large) :
    0 < projectionTailFraction small large := by
  unfold projectionTailFraction projectionMass
  rw [sub_pos, div_lt_one hlarge]
  exact hstrict

theorem normalizedCoherence_lt_one
    {small large : ℝ} (hsmall : 0 ≤ small) (hlarge : 0 < large)
    (hstrict : small < large) :
    normalizedCoherence small large < 1 := by
  have hsq := normalizedCoherence_sq hsmall hlarge
  have hmass : projectionMass small large < 1 := by
    unfold projectionMass
    rw [div_lt_one hlarge]
    exact hstrict
  have hnonneg := normalizedCoherence_nonneg small large
  nlinarith

theorem normalizedDistanceSq_nonneg
    {small large : ℝ} (hsmall : 0 ≤ small) (hlarge : 0 < large)
    (hnested : small ≤ large) :
    0 ≤ normalizedDistanceSq small large := by
  unfold normalizedDistanceSq
  have := normalizedCoherence_le_one hsmall hlarge hnested
  linarith

/-- The translated Riesz lower bound is positive whenever all three inputs
are positive. -/
theorem rieszNormSqLowerBound_pos
    {pairing energy amplification : ℝ}
    (hpairing : 0 < pairing) (henergy : 0 < energy)
    (hamplification : 0 < amplification) :
    0 < rieszNormSqLowerBound pairing energy amplification := by
  unfold rieszNormSqLowerBound
  positivity

/-- Multiplying the functional value by `amplification` multiplies its
squared Riesz lower bound by `amplification^2`. -/
theorem rieszNormSqLowerBound_eq_amplified
    (pairing energy amplification : ℝ) :
    rieszNormSqLowerBound pairing energy amplification =
      amplification ^ 2 * rieszNormSqLowerBound pairing energy 1 := by
  unfold rieszNormSqLowerBound
  ring

end

end RHBridge.RieszKernelEscape
