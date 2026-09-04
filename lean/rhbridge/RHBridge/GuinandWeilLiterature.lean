/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.GuinandWeilFormula
import Glide.CompactSupportFourierLaplace

/-!
# Classical literature inputs for the Guinand--Weil formula

This module deliberately isolates results taken from the classical analytic
number-theory literature rather than reproving their full analytic machinery
inside Mathlib.  Importing this module therefore changes the trust boundary
through the two explicit-formula declarations below.  The elementary
Paley--Wiener prerequisite is proved from the project's compact-support
Fourier--Laplace library and introduces no project axiom.

The literature inputs are unconditional.  In particular, they assume neither
RH nor positivity of the Weil form.

The smooth explicit formula goes back to Guinand and Weil.  Standard modern
statements allow compactly supported piecewise `C²` tests, so the globally
smooth class below is a strict subclass.  The second input is its closure in
the logarithmic quadratic-form norm; this is the natural domain dictated by
the logarithmically growing archimedean multiplier.
-/

namespace RHP2Bridge.GuinandWeilLiterature

open scoped Topology

noncomputable section

open GuinandWeilFormula GeneralZetaWeilForm

/-- Paley--Wiener consequence: a compactly supported smooth function has an
entire bilateral Laplace transform. -/
theorem smooth_bilateralLaplace_entire {a : ℝ}
    (φ : SmoothCompactSupportData a) :
    Differentiable ℂ φ.bilateralLaplace := by
  let b : ℝ := |a| + 1
  let ψ : ℝ → ℂ := fun x ↦ (φ x : ℂ)
  have hb : 0 < b := by
    dsimp [b]
    positivity
  have hab : a ≤ b := by
    dsimp [b]
    linarith [le_abs_self a]
  have hsupport : Set.Icc (-a) a ⊆ Set.Icc (-b) b := by
    intro x hx
    exact ⟨(neg_le_neg hab).trans hx.1, hx.2.trans hab⟩
  have hψi : MeasureTheory.IntegrableOn ψ (Set.Icc (-b) b) :=
    (Complex.continuous_ofReal.comp φ.smooth.continuous).integrableOn_Icc
  have htransform : Differentiable ℂ
      (CompactSupportFourierLaplace.transform ψ b) :=
    CompactSupportFourierLaplace.differentiable_transform hb hψi
  have hcomp : Differentiable ℂ (fun s : ℂ ↦
      CompactSupportFourierLaplace.transform ψ b (Complex.I * s)) :=
    htransform.comp ((differentiable_const _).mul differentiable_id)
  have heq : φ.bilateralLaplace = fun s : ℂ ↦
      CompactSupportFourierLaplace.transform ψ b (Complex.I * s) := by
    funext s
    unfold SmoothCompactSupportData.bilateralLaplace
      CompactSupportFourierLaplace.transform
    have hzero : ∀ x, x ∉ Set.Icc (-b) b →
        ψ x * Complex.exp (-(Complex.I * (Complex.I * s) * (x : ℂ))) = 0 := by
      intro x hx
      have hφzero : φ x = 0 := by
        apply Function.notMem_support.mp
        intro hxφ
        exact hx (hsupport (φ.support_subset hxφ))
      simp [ψ, hφzero]
    rw [MeasureTheory.setIntegral_eq_integral_of_forall_compl_eq_zero hzero]
    apply MeasureTheory.integral_congr_ae
    filter_upwards [] with x
    change Complex.exp (s * (x : ℂ)) * (φ x : ℂ) =
      (φ x : ℂ) * Complex.exp (-(Complex.I * (Complex.I * s) * (x : ℂ)))
    have hexponent : -(Complex.I * (Complex.I * s) * (x : ℂ)) =
        s * (x : ℂ) := by
      rw [← mul_assoc Complex.I Complex.I s, Complex.I_mul_I]
      ring
    rw [hexponent]
    ring
  rw [heq]
  exact hcomp

/-- The normalization-matched smooth Guinand--Weil explicit formula.  This
contains no assertion about the real parts of zeta zeros. -/
axiom smooth_guinandWeil_formula {a : ℝ}
    (φ : SmoothCompactSupportData a) :
    Holds a φ.toTestSpace

/-- Correct low-regularity closure of the explicit formula.  The zero sum is
understood by symmetric exhaustion through closed disks, not as an
unconditionally convergent scalar series. -/
axiom logarithmicDomain_guinandWeil_formula {a : ℝ}
    (f : LogarithmicFormDomain a) :
    DiskHolds a f.val

theorem smooth_zero_sum_eq_weilForm {a : ℝ}
    (φ : SmoothCompactSupportData a) :
    (∑' ρ : NontrivialZetaZero, zeroSummand a φ.toTestSpace ρ) =
      weilForm a φ.toTestSpace :=
  (smooth_guinandWeil_formula φ).2

theorem logarithmic_zero_disk_limit_eq_weilForm {a : ℝ}
    (f : LogarithmicFormDomain a) :
    Filter.Tendsto (fun R : ℝ ↦ zeroSumInDisk R a f.val) Filter.atTop
      (𝓝 (logarithmicWeilForm a f : ℂ)) := by
  simpa [DiskHolds, logarithmicWeilForm] using
    logarithmicDomain_guinandWeil_formula f

end

end RHP2Bridge.GuinandWeilLiterature
