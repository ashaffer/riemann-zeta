/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.InnerProductSpace.l2Space

/-!
Generic Parseval and tail identities for a countable Hilbert basis.
-/

namespace HilbertBasisTail

open scoped ENNReal

variable {ι 𝕜 E : Type*} [RCLike 𝕜]
variable [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]

/-- Parseval's identity in nonnegative real squared-modulus form. -/
theorem hasSum_sq_norm_inner (b : HilbertBasis ι 𝕜 E) (x : E) :
    HasSum (fun i ↦ ‖inner 𝕜 (b i) x‖ ^ 2) (‖x‖ ^ 2) := by
  have h := lp.hasSum_norm (p := (2 : ℝ≥0∞)) (by norm_num) (b.repr x)
  simpa [HilbertBasis.repr_apply_apply] using h

/-- Parseval's identity as a `tsum`. -/
theorem tsum_sq_norm_inner (b : HilbertBasis ι 𝕜 E) (x : E) :
    ∑' i, ‖inner 𝕜 (b i) x‖ ^ 2 = ‖x‖ ^ 2 :=
  (hasSum_sq_norm_inner b x).tsum_eq

/-- The coefficient energy after the first `m` basis vectors equals total
energy minus the first `m` coefficient energies. -/
theorem tsum_nat_add_sq_norm_inner_eq_sub_sum
    (b : HilbertBasis ℕ 𝕜 E) (x : E) (m : ℕ) :
    ∑' n : ℕ, ‖inner 𝕜 (b (m + n)) x‖ ^ 2 =
      ‖x‖ ^ 2 - ∑ k ∈ Finset.range m, ‖inner 𝕜 (b k) x‖ ^ 2 := by
  let energy : ℕ → ℝ := fun k ↦ ‖inner 𝕜 (b k) x‖ ^ 2
  have hsum : Summable energy := (hasSum_sq_norm_inner b x).summable
  have hsplit := hsum.sum_add_tsum_nat_add m
  have htotal : ∑' k : ℕ, energy k = ‖x‖ ^ 2 :=
    (hasSum_sq_norm_inner b x).tsum_eq
  rw [htotal] at hsplit
  have hsplit' :
      (∑ k ∈ Finset.range m, energy k) +
          (∑' n : ℕ, energy (m + n)) = ‖x‖ ^ 2 := by
    simpa [Nat.add_comm] using hsplit
  change ∑' n : ℕ, energy (m + n) =
    ‖x‖ ^ 2 - ∑ k ∈ Finset.range m, energy k
  linarith

/-- A coefficient-tail estimate immediately bounds the corresponding
finite-section Parseval residual. -/
theorem norm_sq_sub_sum_le_of_tsum_tail_le
    (b : HilbertBasis ℕ 𝕜 E) (x : E) (m : ℕ) (C : ℝ)
    (hC : (∑' n : ℕ, ‖inner 𝕜 (b (m + n)) x‖ ^ 2) ≤ C) :
    ‖x‖ ^ 2 - ∑ k ∈ Finset.range m, ‖inner 𝕜 (b k) x‖ ^ 2 ≤ C := by
  rw [← tsum_nat_add_sq_norm_inner_eq_sub_sum b x m]
  exact hC

/-- Every finite-section Parseval residual is nonnegative. -/
theorem norm_sq_sub_sum_nonneg
    (b : HilbertBasis ℕ 𝕜 E) (x : E) (m : ℕ) :
    0 ≤ ‖x‖ ^ 2 -
      ∑ k ∈ Finset.range m, ‖inner 𝕜 (b k) x‖ ^ 2 := by
  rw [← tsum_nat_add_sq_norm_inner_eq_sub_sum b x m]
  exact tsum_nonneg fun _ ↦ sq_nonneg _

end HilbertBasisTail
