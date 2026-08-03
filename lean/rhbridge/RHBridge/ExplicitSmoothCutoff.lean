/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.SmoothCutoff
import RHBridge.SmoothCompactSupportData

/-!
# Smooth-cutoff wrappers for compactly supported Weil test data

The reusable cutoff construction and its quantitative derivative estimates are
in `RHBridge.SmoothCutoff`; the representative data type is in the small
`RHBridge.SmoothCompactSupportData` module.  This file contains only the
decomposition wrappers and has no dependency on the explicit formula or the
zeta-zero theory.
-/

namespace RHP2Bridge.ExplicitSmoothCutoff

noncomputable section

open GuinandWeilFormula

/-- The part of `φ` selected by the quantitative inner cutoff. -/
def explicitOldSmoothData {b : ℝ} (φ : SmoothCompactSupportData b)
    (r a : ℝ) (_hr : 0 < r) (hra : r < a) :
    SmoothCompactSupportData a where
  toFun x := explicitCutoff r a x * φ x
  smooth := explicitCutoff_smooth.mul φ.smooth
  support_subset := by
    intro x hx
    have hcut : explicitCutoff r a x ≠ 0 :=
      Function.support_mul_subset_left _ _ hx
    constructor
    · by_contra hxa
      exact hcut (explicitCutoff_eq_zero_of_le_neg hra (le_of_not_ge hxa))
    · by_contra hxa
      exact hcut (explicitCutoff_eq_zero_of_pos hra (le_of_not_ge hxa))

/-- The complementary collar part of `φ`. -/
def explicitCollarSmoothData {b : ℝ} (φ : SmoothCompactSupportData b)
    (r a : ℝ) (_hr : 0 < r) (_hra : r < a) :
    SmoothCompactSupportData b where
  toFun x := (1 - explicitCutoff r a x) * φ x
  smooth := (contDiff_const.sub explicitCutoff_smooth).mul φ.smooth
  support_subset := by
    intro x hx
    exact φ.support_subset (Function.support_mul_subset_right _ _ hx)

/-- The inner and collar parts reconstruct the original test function. -/
theorem explicitOld_add_collar {b : ℝ} (φ : SmoothCompactSupportData b)
    (r a : ℝ) (hr : 0 < r) (hra : r < a) (x : ℝ) :
    explicitOldSmoothData φ r a hr hra x +
        explicitCollarSmoothData φ r a hr hra x = φ x := by
  simp only [explicitOldSmoothData, explicitCollarSmoothData]
  ring

end

end RHP2Bridge.ExplicitSmoothCutoff
