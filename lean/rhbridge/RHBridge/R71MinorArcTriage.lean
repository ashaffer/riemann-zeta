/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Algebraic guards for the R71 minor-arc triage

This file checks the finite exponent and recombination algebra used after the
analytic Fourier localizations.  In units of `X^(1/100)`, the requested
`eta = 1/100` complete-energy exponent is `98`, while the two controlled
localization errors have exponents `97` (Mellin difference) and `96`
(additive principal-band cross term).

The signed completion architecture and the qualitative principal-band
obstruction have local predecessors.  The R187 delta guarded here is the
frozen affine-center algebra, the explicit order-four exponent ledger, and
the signed-recombination safeguards; no novelty claim is encoded in Lean.

It does **not** formalize Fourier inversion, Young's convolution inequality,
Plancherel, compact Gevrey cutoffs, B-spline Fourier decay, the elementary
divisor bound, the exact Vaughan identity, cofactor Poisson summation, any
dispersion or Kloosterman theorem, a fixed-power R71 estimate, a zero-free
strip, the four-cycle bound, or RH.
-/

namespace RHBridge.R71MinorArcTriage

/-- The frozen strip width is one hundredth. -/
def eta : ℚ := 1 / 100

/-- The corresponding complete-energy exponent is `1 - 2 eta = 49/50`. -/
theorem targetExponent : (1 : ℚ) - 2 * eta = 49 / 50 := by
  norm_num [eta]

/-- Four integrations of the additive tail at aperture `X^(-1+eta)` leave
the cross-term exponent `1 - 4 eta = 24/25`. -/
theorem additiveCrossExponent : (1 : ℚ) - 4 * eta = 24 / 25 := by
  norm_num [eta]

/-- Squaring the order-four additive tail gives exponent
`1 - 8 eta = 23/25`. -/
theorem additiveTailEnergyExponent : (1 : ℚ) - 8 * eta = 23 / 25 := by
  norm_num [eta]

/-- The deliberately weaker far-difference ledger still lies strictly below
the target exponent. -/
theorem farDifferenceExponent_lt_target :
    (97 : ℚ) / 100 < 49 / 50 := by
  norm_num

/-- The additive principal-band error lies strictly below the target too. -/
theorem additiveCrossExponent_lt_target :
    (24 : ℚ) / 25 < 49 / 50 := by
  norm_num

/-- Exact affine-center moment matching.  If `B J₀ = beta/N` and
`A J₀ - B J₁ = alpha/N`, then integrating `A + B log t` against the scaled
window reproduces the affine center coefficients. -/
theorem affineCenter_moment_match
    (alpha beta norm J₀ J₁ : ℝ) (hnorm : norm ≠ 0) (hJ₀ : J₀ ≠ 0) :
    let B := beta / (norm * J₀)
    let A := alpha / (norm * J₀) + beta * J₁ / (norm * J₀ ^ 2)
    B * J₀ = beta / norm ∧ A * J₀ - B * J₁ = alpha / norm := by
  dsimp
  constructor <;> (field_simp [hnorm, hJ₀] <;> ring)

/-- A near contribution at exponent `98` plus an absolutely controlled far
contribution at exponent `97` has the target exponent, up to the harmless
constant two.  The variable `scale` represents `X^(1/100)`. -/
theorem completedBound_of_near_far
    (scale near far total : ℝ)
    (hscale : 1 ≤ scale)
    (hsplit : total = near + far)
    (hnear : near ≤ scale ^ 98)
    (hfar : |far| ≤ scale ^ 97) :
    total ≤ 2 * scale ^ 98 := by
  have hfar' : far ≤ scale ^ 97 := le_trans (le_abs_self far) hfar
  have hpow : scale ^ 97 ≤ scale ^ 98 := by
    calc
      scale ^ 97 = scale ^ 97 * 1 := by ring
      _ ≤ scale ^ 97 * scale :=
        mul_le_mul_of_nonneg_left hscale (by positivity)
      _ = scale ^ 98 := by ring
  rw [hsplit]
  linarith

/-- Conversely, a bound for the completed total controls the near form once
the signed far error is controlled.  No positivity of the far term is used. -/
theorem nearBound_of_completed_far
    (scale near far total : ℝ)
    (hscale : 1 ≤ scale)
    (hsplit : total = near + far)
    (htotal : total ≤ scale ^ 98)
    (hfar : |far| ≤ scale ^ 97) :
    near ≤ 2 * scale ^ 98 := by
  have hminus : -far ≤ scale ^ 97 :=
    le_trans (neg_le_abs far) hfar
  have hpow : scale ^ 97 ≤ scale ^ 98 := by
    calc
      scale ^ 97 = scale ^ 97 * 1 := by ring
      _ ≤ scale ^ 97 * scale :=
        mul_le_mul_of_nonneg_left hscale (by positivity)
      _ = scale ^ 98 := by ring
  linarith

/-- Two plateau extensions of the same completed total give near pieces that
differ by at most the sum of their far-error budgets. -/
theorem nearExtension_difference
    (near₁ far₁ near₂ far₂ total budget : ℝ)
    (hsplit₁ : total = near₁ + far₁)
    (hsplit₂ : total = near₂ + far₂)
    (hfar₁ : |far₁| ≤ budget)
    (hfar₂ : |far₂| ≤ budget) :
    |near₁ - near₂| ≤ 2 * budget := by
  have heq : near₁ - near₂ = far₂ - far₁ := by linarith
  rw [heq]
  calc
    |far₂ - far₁| ≤ |far₂| + |far₁| := abs_sub far₂ far₁
    _ ≤ budget + budget := add_le_add hfar₂ hfar₁
    _ = 2 * budget := by ring

/-- A hard band split need not be positive: this exact scalar model has
positive total and near terms but a negative far term. -/
theorem signedFar_counterexample :
    ∃ total near far : ℚ,
      total = near + far ∧ 0 < total ∧ 0 < near ∧ far < 0 := by
  refine ⟨1, 2, -1, ?_⟩
  norm_num

/-- Pointwise packet smallness has no aggregation content by itself: `n`
packets of size `1/n` sum to one. -/
theorem pointwiseSmall_does_not_aggregate (n : ℕ) (hn : 0 < n) :
    ∑ _j ∈ Finset.range n, (1 / (n : ℚ)) = 1 := by
  simp [hn.ne']

end RHBridge.R71MinorArcTriage
