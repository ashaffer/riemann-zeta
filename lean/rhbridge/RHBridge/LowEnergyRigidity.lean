/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.LowEnergySector

/-!
# The boundary-rigidity obstruction

Small old diagonal energy alone cannot control the off-diagonal boundary
trace, even for a symmetric two-block quadratic form.  This file records the
counterexample and identifies the exact additional statement required of the
combined zeta kernel.
-/

namespace RHP2Bridge.LowEnergyRigidity

noncomputable section

/-- The observed three-way boundary residual: pole plus archimedean minus
prime. -/
def traceResidual (pole arch prime : ℝ) : ℝ := pole + arch - prime

/-- Low old energy alone permits an arbitrarily prescribed combined boundary
trace.  Here the old energy is zero and the norm square is one. -/
theorem small_energy_alone_does_not_force_traceCancellation
    {μ K : ℝ} (hμ : 0 ≤ μ) :
    LowEnergySector.IsLowEnergy μ 0 1 ∧
      traceResidual K 0 0 = K := by
  constructor
  · unfold LowEnergySector.IsLowEnergy
    simpa using hμ
  · simp [traceResidual]

/-- A concrete symmetric block quadratic with zero old diagonal and arbitrary
boundary residual.  At `t = -sign C` it is negative when `C ≠ 0`, showing why
some genuinely mixed positivity/continuation input is indispensable. -/
theorem zero_old_energy_large_trace_forces_negative_direction
    {C D : ℝ} (hC : C ≠ 0) (hD : 0 ≤ D) :
    ∃ t : ℝ, 0 + 2 * t * C + t ^ 2 * D < 0 := by
  refine ⟨-C / (D + 1), ?_⟩
  have hden : 0 < D + 1 := by linarith
  have hdenne : D + 1 ≠ 0 := ne_of_gt hden
  rw [show 0 + 2 * (-C / (D + 1)) * C +
      (-C / (D + 1)) ^ 2 * D =
      -(C ^ 2 * (D + 2)) / (D + 1) ^ 2 by field_simp [hdenne] <;> ring]
  exact div_neg_of_neg_of_pos
    (neg_neg_of_pos (mul_pos (sq_pos_of_ne_zero hC) (by linarith)))
    (sq_pos_of_pos hden)

/-- For fixed old and collar vectors, boundary rigidity is exactly mixed-plane
positivity.  This is the zeta-specific identity that a genuine proof must
establish; it cannot be inferred from the size of the old diagonal alone. -/
theorem boundaryRigidity_iff_mixedPlaneNonnegative
    {oldEnergy collarEnergy pole arch prime : ℝ}
    (hOld : 0 ≤ oldEnergy) (hCollar : 0 ≤ collarEnergy) :
    (traceResidual pole arch prime) ^ 2 ≤ oldEnergy * collarEnergy ↔
      RelativeCrossNecessity.MixedPlaneNonnegative oldEnergy
        (traceResidual pole arch prime) collarEnergy := by
  exact (RelativeCrossNecessity.mixedPlaneNonnegative_iff
    hOld hCollar).symm

end

end RHP2Bridge.LowEnergyRigidity
