/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.RelativeCrossNecessity

/-!
# Isolating the low-energy old sector

An ordinary `L²` cross estimate closes the Schur determinant on every old
vector whose Weil energy lies above a chosen spectral threshold.  Therefore
only the complementary low-energy sector needs the delicate combined-kernel
cancellation estimate.
-/

namespace RHP2Bridge.LowEnergySector

noncomputable section

def IsLowEnergy (μ energy normSq : ℝ) : Prop := energy ≤ μ * normSq
def IsHighEnergy (μ energy normSq : ℝ) : Prop := μ * normSq ≤ energy

theorem low_or_high (μ energy normSq : ℝ) :
    IsLowEnergy μ energy normSq ∨ IsHighEnergy μ energy normSq :=
  le_total energy (μ * normSq)

/-- On the high-energy old sector, an `L²` cross bound and a collar `L²`
floor imply the required form-relative determinant. -/
theorem cross_sq_le_on_highEnergy
    {oldEnergy collarEnergy cross oldNormSq collarNormSq μ d c : ℝ}
    (hμ : 0 ≤ μ) (hd : 0 ≤ d) (hc : 0 ≤ c)
    (hnOld : 0 ≤ oldNormSq) (hnCollar : 0 ≤ collarNormSq)
    (hOld : IsHighEnergy μ oldEnergy oldNormSq)
    (hCollar : d * collarNormSq ≤ collarEnergy)
    (hCross : |cross| ≤ c * Real.sqrt oldNormSq * Real.sqrt collarNormSq)
    (hconstant : c ^ 2 ≤ μ * d) :
    cross ^ 2 ≤ oldEnergy * collarEnergy := by
  have hsOld : (Real.sqrt oldNormSq) ^ 2 = oldNormSq :=
    Real.sq_sqrt hnOld
  have hsCollar : (Real.sqrt collarNormSq) ^ 2 = collarNormSq :=
    Real.sq_sqrt hnCollar
  have hrhs : 0 ≤ c * Real.sqrt oldNormSq * Real.sqrt collarNormSq := by
    positivity
  calc
    cross ^ 2 = |cross| ^ 2 := by rw [sq_abs]
    _ ≤ (c * Real.sqrt oldNormSq * Real.sqrt collarNormSq) ^ 2 :=
      (sq_le_sq₀ (abs_nonneg cross) hrhs).2 hCross
    _ = c ^ 2 * oldNormSq * collarNormSq := by
      rw [mul_pow, mul_pow, hsOld, hsCollar]
    _ ≤ (μ * d) * oldNormSq * collarNormSq := by
      have h1 := mul_le_mul_of_nonneg_right hconstant hnOld
      have h2 := mul_le_mul_of_nonneg_right h1 hnCollar
      simpa [mul_assoc] using h2
    _ = (μ * oldNormSq) * (d * collarNormSq) := by ring
    _ ≤ oldEnergy * collarEnergy := by
      exact mul_le_mul hOld hCollar
        (mul_nonneg hd hnCollar)
        ((mul_nonneg hμ hnOld).trans hOld)

/-- Exact sector composition: special rigidity is required only below the
threshold; the generic `L²` estimate closes every vector above it. -/
theorem cross_sq_le_of_lowEnergy_rigidity
    {oldEnergy collarEnergy cross oldNormSq collarNormSq μ d c : ℝ}
    (hμ : 0 ≤ μ) (hd : 0 ≤ d) (hc : 0 ≤ c)
    (hnOld : 0 ≤ oldNormSq) (hnCollar : 0 ≤ collarNormSq)
    (hCollar : d * collarNormSq ≤ collarEnergy)
    (hCross : |cross| ≤ c * Real.sqrt oldNormSq * Real.sqrt collarNormSq)
    (hconstant : c ^ 2 ≤ μ * d)
    (hLow : IsLowEnergy μ oldEnergy oldNormSq →
      cross ^ 2 ≤ oldEnergy * collarEnergy) :
    cross ^ 2 ≤ oldEnergy * collarEnergy := by
  rcases low_or_high μ oldEnergy oldNormSq with h | h
  · exact hLow h
  · exact cross_sq_le_on_highEnergy hμ hd hc hnOld hnCollar h hCollar
      hCross hconstant

end

end RHP2Bridge.LowEnergySector
