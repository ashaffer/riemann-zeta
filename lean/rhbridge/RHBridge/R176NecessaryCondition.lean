/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Necessary coefficient conditions for the R176 contour target

The proposed complementary-boundary estimate has a nonnegative left-hand
side. Therefore its claimed negative saving cannot exceed the positive
right-arc contribution. This file records that elementary obstruction without
assuming any zeta-specific analytic estimate.
-/

namespace RHP2Bridge.R176NecessaryCondition

/-- If a nonnegative quantity is bounded by
`q * gain * logH - c * q * logH`, with positive `q` and `logH`, then the
claimed saving coefficient cannot exceed `gain`. -/
theorem savingCoefficient_le_gain
    {q gain c logH lhs : ℝ}
    (hq : 0 < q) (hlogH : 0 < logH) (hlhs : 0 ≤ lhs)
    (hbound : lhs ≤ q * gain * logH - c * q * logH) :
    c ≤ gain := by
  have hrearrange :
      q * gain * logH - c * q * logH =
        (q * logH) * (gain - c) := by
    ring
  rw [hrearrange] at hbound
  have hnonneg : 0 ≤ (q * logH) * (gain - c) :=
    le_trans hlhs hbound
  have hscale : 0 < q * logH := mul_pos hq hlogH
  by_contra hnot
  have hnegative : gain - c < 0 := by linarith
  have : (q * logH) * (gain - c) < 0 :=
    mul_neg_of_pos_of_neg hscale hnegative
  linarith

/-- Applied to the exact R176 right-arc gain, the target estimate forces
`c ≤ aR * omega`. -/
theorem savingCoefficient_le_rightArcWeight
    {q aR omega c logH lhs : ℝ}
    (hq : 0 < q) (hlogH : 0 < logH) (hlhs : 0 ≤ lhs)
    (hbound :
      lhs ≤ q * (aR * omega) * logH - c * q * logH) :
    c ≤ aR * omega :=
  savingCoefficient_le_gain hq hlogH hlhs hbound

/-- If only an unsigned split estimate loses a factor two in the positive
right-arc term, the strongest immediate necessary conclusion is correspondingly
weaker: `c ≤ 2 * aR * omega`. -/
theorem savingCoefficient_le_two_mul_rightArcWeight
    {q aR omega c logH lhs : ℝ}
    (hq : 0 < q) (hlogH : 0 < logH) (hlhs : 0 ≤ lhs)
    (hbound :
      lhs ≤ q * (2 * aR * omega) * logH - c * q * logH) :
    c ≤ 2 * aR * omega :=
  savingCoefficient_le_gain hq hlogH hlhs hbound

/-- No fixed positive saving coefficient can satisfy the necessary condition
along a contour family whose right-arc weight can become arbitrarily small. -/
theorem savingCoefficient_nonpos_of_arbitrarilySmallGain
    {ι : Type*} {gain : ι → ℝ} {c : ℝ}
    (hsmall : ∀ ε : ℝ, 0 < ε → ∃ i : ι, gain i < ε)
    (hnecessary : ∀ i : ι, c ≤ gain i) :
    c ≤ 0 := by
  by_contra hnot
  have hc : 0 < c := lt_of_not_ge hnot
  obtain ⟨i, hi⟩ := hsmall c hc
  linarith [hnecessary i]

end RHP2Bridge.R176NecessaryCondition
