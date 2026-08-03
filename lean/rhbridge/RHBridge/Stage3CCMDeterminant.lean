/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage3DeterminantLimit

/-!
# Connes--Consani--Moscovici determinant target

This is the exact two-parameter interface suggested by the finite-dimensional
spectral-triple construction.  It keeps finite-level real-zero input separate
from the open cofinal determinant convergence.
-/

namespace RHP2Bridge.Stage3CCMDeterminant

open Filter Complex Stage3DeterminantLimit

/-- One finite-window regularized characteristic function.  In the CCM
construction these fields are obtained from simplicity and evenness of the
lowest truncated Weil eigenvector and self-adjointness of the rank-one
perturbation. -/
structure FiniteWindowCharacteristic where
  support : ℝ
  cutoff : ℕ
  support_gt_one : 1 < support
  characteristic : ℂ → ℂ
  entire : Differentiable ℂ characteristic
  realZeros : AllZerosReal characteristic

/-- A zero-free entire normalization does not alter the spectral zero set. -/
structure ZeroFreeNormalization where
  factor : ℂ → ℂ
  entire : Differentiable ℂ factor
  neverZero : ∀ z, factor z ≠ 0

def normalizedCharacteristic
    (window : FiniteWindowCharacteristic)
    (normalization : ZeroFreeNormalization) : ℂ → ℂ :=
  fun z ↦ normalization.factor z * window.characteristic z

theorem normalizedCharacteristic_entire
    (window : FiniteWindowCharacteristic)
    (normalization : ZeroFreeNormalization) :
    Differentiable ℂ (normalizedCharacteristic window normalization) := by
  exact normalization.entire.mul window.entire

theorem normalizedCharacteristic_realZeros
    (window : FiniteWindowCharacteristic)
    (normalization : ZeroFreeNormalization) :
    AllZerosReal (normalizedCharacteristic window normalization) := by
  intro z hz
  have hchar : window.characteristic z = 0 := by
    rcases mul_eq_zero.mp hz with hfactor | hchar
    · exact False.elim (normalization.neverZero z hfactor)
    · exact hchar
  exact window.realZeros z hchar

/-- The concrete open convergence package: both truncation parameters are
cofinal, normalization is zero-free, and the normalized determinants converge
compact-locally directly to completed xi. -/
structure CCMDeterminantXiLimit where
  window : ℕ → FiniteWindowCharacteristic
  normalization : ℕ → ZeroFreeNormalization
  support_cofinal : Tendsto (fun n ↦ (window n).support) atTop atTop
  cutoff_cofinal : Tendsto (fun n ↦ (window n).cutoff) atTop atTop
  locallyUniform : TendstoLocallyUniformly
    (fun n ↦ normalizedCharacteristic (window n) (normalization n))
    criticalXi atTop

/-- The CCM convergence package instantiates the abstract Hurwitz bridge. -/
def CCMDeterminantXiLimit.toRealZeroEntireApproximation
    (h : CCMDeterminantXiLimit) :
    RealZeroEntireApproximation criticalXi where
  approximant n := normalizedCharacteristic (h.window n) (h.normalization n)
  approximant_entire n := normalizedCharacteristic_entire _ _
  approximant_realZeros n := normalizedCharacteristic_realZeros _ _
  locallyUniform := h.locallyUniform
  target_nonzero := criticalXi_nonzero

theorem riemannHypothesis_of_CCMDeterminantXiLimit
    (h : CCMDeterminantXiLimit) : RiemannHypothesis :=
  riemannHypothesis_of_realZeroEntireApproximation
    h.toRealZeroEntireApproximation

end RHP2Bridge.Stage3CCMDeterminant
