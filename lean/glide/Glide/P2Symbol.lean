/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Glide.GammaUniformQuarter

/-!
# The p=2 clipped zeta symbol

At support `L = 7/4`, only the prime `2` occurs.  This file defines the exact
real frequency symbol used by the FULLINF p=2 certificate and proves its
exterior comparison from the unconditional digamma monotonicity theorem.

No decimal evaluation of digamma is asserted here; the separate
`Glide.DigammaBounds` module proves the directed floor and band enclosures.
-/

open Set

namespace GlideKernel

/-- The amplitude `sqrt(2) * log 2` of the p=2 prime oscillation. -/
noncomputable def p2PrimeAmplitude : ℝ :=
  Real.sqrt 2 * Real.log 2

/-- The exact real zeta multiplier on the p=2 frequency line. -/
noncomputable def p2Omega (r : ℝ) : ℝ :=
  quarterDigammaReal r - Real.log Real.pi -
    p2PrimeAmplitude * Real.cos (r * Real.log 2)

/-- The clipped exterior floor at frequency `S = 50`. -/
noncomputable def p2Alpha : ℝ :=
  quarterDigammaReal 50 - Real.log Real.pi - p2PrimeAmplitude

theorem p2PrimeAmplitude_nonneg : 0 ≤ p2PrimeAmplitude := by
  unfold p2PrimeAmplitude
  positivity

/-- The p=2 symbol is even. -/
theorem p2Omega_neg (r : ℝ) : p2Omega (-r) = p2Omega r := by
  unfold p2Omega
  rw [quarterDigammaReal_neg]
  congr 1
  rw [neg_mul, Real.cos_neg]

/-- The p=2 symbol is continuous. -/
theorem continuous_p2Omega : Continuous p2Omega := by
  unfold p2Omega p2PrimeAmplitude
  have hcos : Continuous (fun r : ℝ ↦ Real.cos (r * Real.log 2)) := by
    simpa [Function.comp_def] using
      Real.continuous_cos.comp (continuous_id.mul continuous_const)
  exact (continuous_quarterDigammaReal.sub continuous_const).sub
    (continuous_const.mul hcos)

/-- Outside `[-50,50]`, the exact symbol is bounded below by the clipped
floor.  Digamma monotonicity controls the archimedean term, while
`cos ≤ 1` controls the prime oscillation. -/
theorem p2Omega_exterior_lower_bound {r : ℝ} (hr : 50 ≤ |r|) :
    p2Alpha ≤ p2Omega r := by
  have hpsi : quarterDigammaReal 50 ≤ quarterDigammaReal r :=
    quarterDigammaReal_exterior_lower_bound (by norm_num) hr
  have hprime :
      p2PrimeAmplitude * Real.cos (r * Real.log 2) ≤ p2PrimeAmplitude := by
    simpa only [mul_one] using
      mul_le_mul_of_nonneg_left (Real.cos_le_one _) p2PrimeAmplitude_nonneg
  unfold p2Alpha p2Omega
  linarith

/-- Equivalent nonnegativity of the clipped symbol defect on the exterior. -/
theorem p2Omega_sub_alpha_nonneg {r : ℝ} (hr : 50 ≤ |r|) :
    0 ≤ p2Omega r - p2Alpha :=
  sub_nonneg.mpr (p2Omega_exterior_lower_bound hr)

end GlideKernel
