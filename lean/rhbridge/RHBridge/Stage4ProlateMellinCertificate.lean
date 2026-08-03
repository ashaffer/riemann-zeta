/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage4FullDomainResidual
import RHBridge.ZetaZeroFreeRegionLiterature

/-!
# From prolate tail control to the global CCM zero bound

The certificate records the output of weighted prolate interpolation, Poisson
summation, and one Mellin integration by parts before inserting any fact about
the location of zeta zeros.
-/

namespace RHP2Bridge.Stage4ProlateMellinCertificate

open Filter Topology GeneralZetaWeilForm GuinandWeilFormula
open Stage4FullDomainResidual ZetaZeroFreeRegionLiterature

structure ProlateMellinTailCertificate {a : ℕ → ℝ}
    (f : (n : ℕ) → LogarithmicFormDomain (a n)) where
  leakageRate : ℕ → ℝ
  leakageRate_nonneg : ∀ n, 0 ≤ leakageRate n
  leakageRate_tendsto_zero : Tendsto leakageRate atTop (𝓝 0)
  transform_at_zero_le : ∀ n (ρ : NontrivialZetaZero),
    ‖bilateralLaplace (a n) (f n).val (ρ.val - 1 / 2)‖ +
      ‖bilateralLaplace (a n) (f n).val (1 / 2 - ρ.val)‖ ≤
    leakageRate n * (centeredEdgeDistance ρ)⁻¹ /
      (1 + |ρ.val.im|)

/-- The RH-free zero-free region converts the strip-edge loss in the prolate
tail certificate into the global logarithmic majorant consumed by Stage 4. -/
theorem hasCCMGlobalZeroBound
    {a : ℕ → ℝ} {f : (n : ℕ) → LogarithmicFormDomain (a n)}
    (P : ProlateMellinTailCertificate f) :
    ∃ rate : ℕ → ℝ, HasCCMGlobalZeroBound f rate := by
  obtain ⟨C, hC, hzf⟩ := exists_recip_centeredEdgeDistance_le_log
  let rate : ℕ → ℝ := fun n ↦ C * P.leakageRate n
  refine ⟨rate, ?_, ?_, ?_⟩
  · intro n
    exact mul_nonneg hC (P.leakageRate_nonneg n)
  · simpa [rate] using P.leakageRate_tendsto_zero.const_mul C
  · intro n ρ
    have hden : 0 < 1 + |ρ.val.im| := by positivity
    calc
      ‖bilateralLaplace (a n) (f n).val (ρ.val - 1 / 2)‖ +
          ‖bilateralLaplace (a n) (f n).val (1 / 2 - ρ.val)‖ ≤
          P.leakageRate n * (centeredEdgeDistance ρ)⁻¹ /
            (1 + |ρ.val.im|) := P.transform_at_zero_le n ρ
      _ ≤ P.leakageRate n *
          (C * Real.log (2 + |ρ.val.im|)) /
            (1 + |ρ.val.im|) := by
        exact div_le_div_of_nonneg_right
          (mul_le_mul_of_nonneg_left (hzf ρ) (P.leakageRate_nonneg n))
          hden.le
      _ = rate n * (Real.log (2 + |ρ.val.im|) /
          (1 + |ρ.val.im|)) := by
        dsimp [rate]
        field_simp

end RHP2Bridge.Stage4ProlateMellinCertificate
