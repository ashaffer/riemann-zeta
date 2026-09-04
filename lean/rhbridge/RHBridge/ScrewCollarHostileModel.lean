/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.LowEnergyRigidity

/-!
# Exact scalar certificate for the screw-collar hostile model

The analytic construction and its exact polynomial integration are recorded
in the companion report.  This module kernel-checks the sign and the resulting
two-dimensional indefiniteness for every `0 < delta <= 1/4`.
-/

namespace RHP2Bridge.ScrewCollarHostileModel

noncomputable section

/-- Exact old--collar cross term of the even C1 convolution countermodel. -/
def hostileCross (delta : ℝ) : ℝ :=
  -(delta ^ 7 * (28 * delta ^ 2 - 135 * delta + 90)) / 60480

/-- The collar diagonal in the same model. -/
def hostileCollarEnergy (delta : ℝ) : ℝ := delta ^ 6 / 36

/-- The remaining polynomial factor is strictly positive throughout the
collar range used by the construction. -/
theorem hostile_factor_pos {delta : ℝ}
    (hdelta : 0 < delta) (hupper : delta <= 1 / 4) :
    0 < 28 * delta ^ 2 - 135 * delta + 90 := by
  nlinarith [sq_nonneg delta]

/-- Every nontrivial arbitrarily thin collar carries a strictly negative
cross term in the explicit model. -/
theorem hostileCross_neg {delta : ℝ}
    (hdelta : 0 < delta) (hupper : delta <= 1 / 4) :
    hostileCross delta < 0 := by
  have hpow : 0 < delta ^ 7 := pow_pos hdelta 7
  have hfactor := hostile_factor_pos hdelta hupper
  have hnum : 0 < delta ^ 7 * (28 * delta ^ 2 - 135 * delta + 90) :=
    mul_pos hpow hfactor
  have hden : (0 : ℝ) < 60480 := by norm_num
  unfold hostileCross
  exact div_neg_of_neg_of_pos (neg_neg_of_pos hnum) hden

theorem hostileCollarEnergy_nonneg {delta : ℝ} :
    0 <= hostileCollarEnergy delta := by
  unfold hostileCollarEnergy
  positivity

/-- A zero old diagonal plus this nonzero collar charge has a negative mixed
direction.  Thus positivity cannot right-extend on generic kernel structure. -/
theorem hostile_model_has_negative_direction {delta : ℝ}
    (hdelta : 0 < delta) (hupper : delta <= 1 / 4) :
    ∃ t : ℝ,
      0 + 2 * t * hostileCross delta +
        t ^ 2 * hostileCollarEnergy delta < 0 := by
  exact LowEnergyRigidity.zero_old_energy_large_trace_forces_negative_direction
    (ne_of_lt (hostileCross_neg hdelta hupper))
    hostileCollarEnergy_nonneg

end

end RHP2Bridge.ScrewCollarHostileModel
