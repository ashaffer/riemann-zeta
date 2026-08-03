/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.CanonicalZeroMode

/-!
# The shift obstruction in the finite-interval canonical route

Suzuki's finite-interval Hilbert norm is obtained from a shifted form
`Q(v) - lambda * ||v||^2`, with `lambda` below the bottom of the Weil
operator.  Therefore a null vector of `Q` is not a null vector of the shifted
Hilbert norm when `lambda < 0`.  This elementary fact prevents identifying a
Weil zero mode with the zero spectral parameter of the differentiation
operator without an additional intertwining theorem.
-/

namespace RHP2Bridge.CanonicalShiftObstruction

/-- Abstract scalar model of Suzuki's shifted form norm. -/
def shiftedEnergy (weilEnergy lambda l2NormSq : ℝ) : ℝ :=
  weilEnergy - lambda * l2NormSq

/-- A nonzero Weil null mode has strictly positive shifted energy for every
negative shift.  Thus the shift embeds rather than kills the null mode. -/
theorem shiftedEnergy_pos_of_weil_zero
    {weilEnergy lambda l2NormSq : ℝ}
    (hzero : weilEnergy = 0)
    (hlambda : lambda < 0)
    (hl2 : 0 < l2NormSq) :
    0 < shiftedEnergy weilEnergy lambda l2NormSq := by
  unfold shiftedEnergy
  rw [hzero, zero_sub]
  exact neg_pos.mpr (mul_neg_of_neg_of_pos hlambda hl2)

/-- At shift zero the shifted norm sees exactly the original degeneracy, so
it is not a Hilbert norm in the presence of a nonzero Weil null mode. -/
theorem shiftedEnergy_zero_shift
    (weilEnergy l2NormSq : ℝ) :
    shiftedEnergy weilEnergy 0 l2NormSq = weilEnergy := by
  simp [shiftedEnergy]

/-- The two desired properties conflict in the scalar zero-mode model:
negative shifting makes the null mode non-null, while leaving it null forces
the shift to be zero. -/
theorem shift_eq_zero_of_null_preserved
    {lambda l2NormSq : ℝ}
    (hl2 : l2NormSq ≠ 0)
    (hpreserved : shiftedEnergy 0 lambda l2NormSq = 0) :
    lambda = 0 := by
  unfold shiftedEnergy at hpreserved
  have hmul : lambda * l2NormSq = 0 := by
    linarith
  exact (mul_eq_zero.mp hmul).resolve_right hl2

end RHP2Bridge.CanonicalShiftObstruction
