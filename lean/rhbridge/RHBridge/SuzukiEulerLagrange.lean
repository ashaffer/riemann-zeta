/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.LowEnergyRigidity
import RHBridge.SuzukiPrimeRamp

/-!
# Weak Euler--Lagrange equation and the Suzuki boundary residual

This file polarizes the unconditional Suzuki identity and separates the weak
old-sector eigen-equation from its collar residual.  The residual is nonlocal:
the prime ramps have interior kink lines and therefore do not reduce to
endpoint evaluation.
-/

namespace RHP2Bridge.SuzukiEulerLagrange

open GeneralZetaWeilForm GuinandWeilFormula

noncomputable section

/-- Pointwise addition on the explicit smooth core. -/
def smoothDataAdd {a : ℝ} (φ ψ : SmoothCompactSupportData a) :
    SmoothCompactSupportData a where
  toFun x := φ x + ψ x
  smooth := φ.smooth.add ψ.smooth
  support_subset := by
    intro x hx
    by_contra hxI
    have hφ : φ x = 0 := by
      by_contra h
      exact hxI (φ.support_subset h)
    have hψ : ψ x = 0 := by
      by_contra h
      exact hxI (ψ.support_subset h)
    exact hx (by simp [hφ, hψ])

@[simp] theorem smoothDataAdd_apply {a x : ℝ}
    (φ ψ : SmoothCompactSupportData a) :
    smoothDataAdd φ ψ x = φ x + ψ x := rfl

theorem smoothDataToTestSpace_add {a : ℝ}
    (φ ψ : SmoothCompactSupportData a) :
    (smoothDataAdd φ ψ).toTestSpace = φ.toTestSpace + ψ.toTestSpace := by
  have hmaps : (smoothDataAdd φ ψ).intervalContinuousMap =
      φ.intervalContinuousMap + ψ.intervalContinuousMap := by
    ext x
    rfl
  unfold SmoothCompactSupportData.toTestSpace
  rw [hmaps]
  exact (ContinuousMap.toLp 2 (LegendreScaledL2.intervalMeasure a) ℝ).map_add
    φ.intervalContinuousMap ψ.intervalContinuousMap

/-- Polarization of Suzuki's diagonal derivative-kernel form.  This avoids
assuming a separate bilinearity theorem for its iterated integral. -/
def polarizedScrewCross {a : ℝ}
    (φ ψ : SmoothCompactSupportData a) : ℝ :=
  (SuzukiScrewLiterature.screwKernelForm
      (smoothDataAdd φ ψ)
      (smoothDataAdd φ ψ) -
    SuzukiScrewLiterature.screwKernelForm φ φ -
    SuzukiScrewLiterature.screwKernelForm ψ ψ) / 2

/-- The polarized Suzuki kernel is exactly the arithmetic Weil cross term,
including pole, archimedean, and prime-ramp cancellation. -/
theorem polarizedScrewCross_eq_weilCross {a : ℝ}
    (φ ψ : SmoothCompactSupportData a) :
    polarizedScrewCross φ ψ =
      SupportDecomposition.weilCross a φ.toTestSpace ψ.toTestSpace := by
  unfold polarizedScrewCross SupportDecomposition.weilCross
  rw [SuzukiScrewLiterature.screwKernelForm_eq_weilForm,
    SuzukiScrewLiterature.screwKernelForm_eq_weilForm,
    SuzukiScrewLiterature.screwKernelForm_eq_weilForm,
    smoothDataToTestSpace_add]

/-- Smooth variations whose support remains in the old interval `[-a,a]`
while they are represented in the larger window `[-b,b]`. -/
def IsOldVariation (a : ℝ) {b : ℝ}
    (ψ : SmoothCompactSupportData b) : Prop :=
  Function.support ψ.toFun ⊆ LegendreScaledL2.Interval a

/-- Weak localized Euler--Lagrange equation for a candidate eigenfunction.
It controls every old-supported variation and deliberately says nothing yet
about collar variations. -/
def IsWeakOldEigenpair (a b eig : ℝ)
    (φ : SmoothCompactSupportData b) : Prop :=
  IsOldVariation a φ ∧
    ∀ ψ : SmoothCompactSupportData b, IsOldVariation a ψ →
      polarizedScrewCross φ ψ =
        eig * inner ℝ φ.toTestSpace ψ.toTestSpace

/-- The Euler--Lagrange residual against an arbitrary larger-window test. -/
def boundaryResidual {b eig : ℝ} (φ ψ : SmoothCompactSupportData b) : ℝ :=
  polarizedScrewCross φ ψ -
    eig * inner ℝ φ.toTestSpace ψ.toTestSpace

/-- The weak equation annihilates the residual on all old variations. -/
theorem boundaryResidual_eq_zero_of_oldVariation
    {a b eig : ℝ} {φ ψ : SmoothCompactSupportData b}
    (heigen : IsWeakOldEigenpair a b eig φ)
    (hψ : IsOldVariation a ψ) :
    boundaryResidual (eig := eig) φ ψ = 0 := by
  unfold boundaryResidual
  rw [heigen.2 ψ hψ]
  ring

/-- Against an `L²`-orthogonal collar variation, the residual is exactly the
combined arithmetic boundary trace. -/
theorem boundaryResidual_eq_weilCross_of_orthogonal
    {b eig : ℝ} {φ ψ : SmoothCompactSupportData b}
    (horth : inner ℝ φ.toTestSpace ψ.toTestSpace = 0) :
    boundaryResidual (eig := eig) φ ψ =
      SupportDecomposition.weilCross b φ.toTestSpace ψ.toTestSpace := by
  unfold boundaryResidual
  rw [horth, mul_zero, sub_zero, polarizedScrewCross_eq_weilCross]

end


end RHP2Bridge.SuzukiEulerLagrange
