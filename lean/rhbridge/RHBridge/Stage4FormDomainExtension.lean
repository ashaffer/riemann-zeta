/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage4DominatedResidual

/-!
# Extending the Stage-4 residual from a form core

The load-bearing condition is uniform boundedness of the residual functionals
in the closed form norm.  Density alone is insufficient.
-/

namespace RHP2Bridge.Stage4FormDomainExtension

open Filter Topology

/-- A quantitative dense-core extension theorem for a sequence of continuous
linear residual functionals. -/
theorem tendsto_zero_of_dense_core_of_uniform_operator_norm
    {E : Type*} [SeminormedAddCommGroup E] [NormedSpace ℝ E]
    (L : ℕ → E →L[ℝ] ℂ) (core : Set E) (C : ℝ) (hC : 0 ≤ C)
    (happrox : ∀ (x : E) (ε : ℝ), 0 < ε →
      ∃ y : E, y ∈ core ∧ ‖x - y‖ < ε)
    (hbound : ∀ n, ‖L n‖ ≤ C)
    (hcore : ∀ y ∈ core, Tendsto (fun n ↦ L n y) atTop (𝓝 0))
    (x : E) : Tendsto (fun n ↦ L n x) atTop (𝓝 0) := by
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨y, hy, hxy⟩ := happrox x (ε / (2 * (C + 1))) (by positivity)
  obtain ⟨N, hN⟩ :=
    (Metric.tendsto_atTop.mp (hcore y hy)) (ε / 2) (half_pos hε)
  refine ⟨N, fun n hn ↦ ?_⟩
  have hop : ‖L n (x - y)‖ ≤ C * ‖x - y‖ := by
    calc
      ‖L n (x - y)‖ ≤ ‖L n‖ * ‖x - y‖ := (L n).le_opNorm _
      _ ≤ C * ‖x - y‖ := mul_le_mul_of_nonneg_right (hbound n) (norm_nonneg _)
  have hpert : ‖L n (x - y)‖ < ε / 2 := by
    have hCp : 0 < C + 1 := by linarith
    calc
      ‖L n (x - y)‖ ≤ C * ‖x - y‖ := hop
      _ ≤ (C + 1) * ‖x - y‖ := by
        exact mul_le_mul_of_nonneg_right (by linarith) (norm_nonneg _)
      _ < (C + 1) * (ε / (2 * (C + 1))) :=
        mul_lt_mul_of_pos_left hxy hCp
      _ = ε / 2 := by field_simp
  have hyN : dist (L n y) 0 < ε / 2 := hN n hn
  calc
    dist (L n x) 0 = ‖L n x‖ := by simp [dist_eq_norm]
    _ = ‖L n (x - y) + L n y‖ := by rw [map_sub, sub_add_cancel]
    _ ≤ ‖L n (x - y)‖ + ‖L n y‖ := norm_add_le _ _
    _ < ε / 2 + ε / 2 :=
      add_lt_add hpert (by simpa [dist_zero_right] using hyN)
    _ = ε := by ring

end RHP2Bridge.Stage4FormDomainExtension
