/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Tactic

/-!
# Rigidity of the metric shift under canonical support nesting

Whenever an unshifted quadratic form and its reference norm are unchanged by
an embedding, the corresponding shifted energy changes by exactly
`(sigmaOld - sigmaNew) * ||f||²`.  On any nonzero old vector, exact
preservation of shifted energy therefore forces the two shifts to agree.

This file deliberately states the result as axiom-free scalar algebra.  It can
be instantiated with
`ActivationCancellation.weilForm_nestedSupport_eq` and
`NestedSupport.norm_nestedSupport`.  Keeping those heavy analytic imports out
of this small module also prevents the general form API from pulling the fixed
P2 certificate into every downstream build.
-/

namespace RHBridge.NestedShiftRigidity

/-- Scalar shifted energy.  This is intentionally independent of any one
realization of the underlying quadratic form. -/
def shiftedEnergy (energy sigma normSq : ℝ) : ℝ :=
  energy - sigma * normSq

/-- If the unshifted energy and norm-squared are fixed, changing the scalar
shift has this exact effect. -/
theorem shiftedEnergy_sub_shiftedEnergy
    (energy normSq sigmaOld sigmaNew : ℝ) :
    shiftedEnergy energy sigmaNew normSq -
        shiftedEnergy energy sigmaOld normSq =
      (sigmaOld - sigmaNew) * normSq := by
  unfold shiftedEnergy
  ring

/-- Fixing the metric shift at `-1/4` adds exactly one quarter of the
reference norm-squared to the unshifted energy. -/
theorem quarterNegativeShift_eq (energy normSq : ℝ) :
    shiftedEnergy energy (-(1 / 4 : ℝ)) normSq =
      energy + (1 / 4 : ℝ) * normSq := by
  unfold shiftedEnergy
  ring

/-- Any nonnegative unshifted form becomes `1/4`-coercive after the fixed
negative shift `-1/4`. -/
theorem quarterNegativeShift_coercive_of_nonnegative
    {energy normSq : ℝ} (henergy : 0 ≤ energy) :
    (1 / 4 : ℝ) * normSq ≤
      shiftedEnergy energy (-(1 / 4 : ℝ)) normSq := by
  rw [quarterNegativeShift_eq]
  linarith

/-- A pre-existing lower bound `delta` gains exactly `1/4` under the fixed
negative shift.  This is the scalar form of the certified-window safety
argument used by the Suzuki diagnostic. -/
theorem quarterNegativeShift_coercive_of_lowerBound
    {energy normSq delta : ℝ} (hlower : delta * normSq ≤ energy) :
    (delta + 1 / 4) * normSq ≤
      shiftedEnergy energy (-(1 / 4 : ℝ)) normSq := by
  rw [quarterNegativeShift_eq]
  nlinarith

/-- A nonnegative spectral floor makes `-1/4` a strictly admissible shift. -/
theorem quarterNegativeShift_lt_floor_of_nonnegative
    {floor : ℝ} (hfloor : 0 ≤ floor) :
    -(1 / 4 : ℝ) < floor := by
  linarith

/-- A nonzero norm-squared makes exact preservation of a shifted energy rigid
in the shift parameter. -/
theorem shift_eq_of_shiftedEnergy_eq
    {energy normSq sigmaOld sigmaNew : ℝ} (hnorm : normSq ≠ 0)
    (hpreserved :
      shiftedEnergy energy sigmaNew normSq =
        shiftedEnergy energy sigmaOld normSq) :
    sigmaNew = sigmaOld := by
  have hzero : (sigmaOld - sigmaNew) * normSq = 0 := by
    rw [← shiftedEnergy_sub_shiftedEnergy]
    exact sub_eq_zero.mpr hpreserved
  have : sigmaOld - sigmaNew = 0 :=
    (mul_eq_zero.mp hzero).resolve_right hnorm
  linarith

/-- General embedding form of the compatibility identity.  The hypotheses say
that both the unshifted energy and norm-squared of the old vector are exactly
preserved. -/
theorem shiftedEnergy_sub_of_invariants
    {energyOld energyNew normOldSq normNewSq sigmaOld sigmaNew : ℝ}
    (henergy : energyNew = energyOld) (hnorm : normNewSq = normOldSq) :
    shiftedEnergy energyNew sigmaNew normNewSq -
        shiftedEnergy energyOld sigmaOld normOldSq =
      (sigmaOld - sigmaNew) * normOldSq := by
  rw [henergy, hnorm]
  exact shiftedEnergy_sub_shiftedEnergy _ _ _ _

/-- If an embedding preserves unshifted energy, norm-squared, and shifted
energy on one vector of nonzero norm, then its two shift parameters agree. -/
theorem shift_eq_of_preserved_invariants
    {energyOld energyNew normOldSq normNewSq sigmaOld sigmaNew : ℝ}
    (henergy : energyNew = energyOld) (hnorm : normNewSq = normOldSq)
    (hnonzero : normOldSq ≠ 0)
    (hpreserved :
      shiftedEnergy energyNew sigmaNew normNewSq =
        shiftedEnergy energyOld sigmaOld normOldSq) :
    sigmaNew = sigmaOld := by
  rw [henergy, hnorm] at hpreserved
  exact shift_eq_of_shiftedEnergy_eq hnonzero hpreserved

end RHBridge.NestedShiftRigidity
