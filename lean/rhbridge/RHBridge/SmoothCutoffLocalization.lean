/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.SmoothSupportPropagation
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension

/-!
# Smooth cutoff localization on logarithmic support windows

This file constructs the domain-safe old/collar split on the explicit smooth
core.  Mathlib's canonical bump equals one on `[-r,r]`, vanishes outside
`(-a,a)`, and takes values in `[0,1]`.  Multiplying a smooth test function by
this bump gives an old piece at support `a`; multiplying by its complement
gives a collar piece at the original support `b`.

The construction is exact.  Quantitative derivative bounds for Mathlib's
abstract bump base are not currently part of its API, so no transition-width
estimate is asserted here.
-/

namespace RHP2Bridge.SmoothCutoffLocalization

noncomputable section

open GuinandWeilFormula

/-- Canonical smooth cutoff: one on the closed radius-`r` ball and supported
in the open radius-`a` ball. -/
def supportCutoff (r a : ℝ) (hr : 0 < r) (hra : r < a) :
    ContDiffBump (0 : ℝ) :=
  ⟨r, a, hr, hra⟩

theorem supportCutoff_smooth (r a : ℝ) (hr : 0 < r) (hra : r < a) :
    ContDiff ℝ (⊤ : ℕ∞) (supportCutoff r a hr hra) :=
  (supportCutoff r a hr hra).contDiff

theorem supportCutoff_eq_one {r a x : ℝ} (hr : 0 < r) (hra : r < a)
    (hx : |x| ≤ r) : supportCutoff r a hr hra x = 1 := by
  apply (supportCutoff r a hr hra).one_of_mem_closedBall
  simpa [supportCutoff, Real.dist_eq] using hx

theorem supportCutoff_eq_zero {r a x : ℝ} (hr : 0 < r) (hra : r < a)
    (hx : a ≤ |x|) : supportCutoff r a hr hra x = 0 := by
  apply (supportCutoff r a hr hra).zero_of_le_dist
  simpa [supportCutoff, Real.dist_eq] using hx

theorem supportCutoff_mem_Icc (r a x : ℝ) (hr : 0 < r) (hra : r < a) :
    supportCutoff r a hr hra x ∈ Set.Icc (0 : ℝ) 1 :=
  ⟨(supportCutoff r a hr hra).nonneg,
    (supportCutoff r a hr hra).le_one⟩

/-- The smoothly localized old piece, now genuinely supported in `[-a,a]`. -/
def oldSmoothData {b : ℝ} (φ : SmoothCompactSupportData b)
    (r a : ℝ) (hr : 0 < r) (hra : r < a) :
    SmoothCompactSupportData a where
  toFun x := supportCutoff r a hr hra x * φ x
  smooth := (supportCutoff_smooth r a hr hra).mul φ.smooth
  support_subset := by
    intro x hx
    have hcut : supportCutoff r a hr hra x ≠ 0 :=
      Function.support_mul_subset_left _ _ hx
    have hxa : |x| < a := by
      have hm : x ∈ Function.support (supportCutoff r a hr hra) := hcut
      rw [ContDiffBump.support_eq] at hm
      simpa [supportCutoff, Metric.mem_ball, Real.dist_eq] using hm
    exact ⟨neg_le_of_abs_le hxa.le, le_of_abs_le hxa.le⟩

/-- The complementary smooth collar piece, retaining the original support. -/
def collarSmoothData {b : ℝ} (φ : SmoothCompactSupportData b)
    (r a : ℝ) (hr : 0 < r) (hra : r < a) :
    SmoothCompactSupportData b where
  toFun x := (1 - supportCutoff r a hr hra x) * φ x
  smooth := (contDiff_const.sub (supportCutoff_smooth r a hr hra)).mul φ.smooth
  support_subset := by
    intro x hx
    exact φ.support_subset (Function.support_mul_subset_right _ _ hx)

/-- The smooth old and collar representatives sum pointwise to the original
test function; no limiting or almost-everywhere qualification is needed. -/
theorem oldSmoothData_add_collarSmoothData {b : ℝ}
    (φ : SmoothCompactSupportData b) (r a : ℝ)
    (hr : 0 < r) (hra : r < a) (x : ℝ) :
    oldSmoothData φ r a hr hra x + collarSmoothData φ r a hr hra x = φ x := by
  simp only [oldSmoothData, collarSmoothData]
  ring

/-- Width of the transition collar.  Future quantitative estimates must
control the cutoff derivatives in terms of this positive number. -/
def transitionWidth (r a : ℝ) : ℝ := a - r

theorem transitionWidth_pos {r a : ℝ} (hra : r < a) :
    0 < transitionWidth r a := sub_pos.mpr hra

end

end RHP2Bridge.SmoothCutoffLocalization
