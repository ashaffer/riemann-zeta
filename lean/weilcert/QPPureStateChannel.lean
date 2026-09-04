/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Algebraic core of the QP pure-state channel formulation

This file certifies the finite Kraus/pair-incidence expansion.  It does not
assert the open arithmetic `S₁ → S₂` norm estimate.
-/

open scoped BigOperators

namespace QPPureStateChannel

variable {Carrier Row Color : Type*}
variable [Fintype Carrier] [Fintype Row] [Fintype Color]

omit [Fintype Row] in
/-- Expanding the row Gram of the weighted carry matrix gives the common
triple sum underlying the pair-incidence operator. -/
theorem kraus_pair_expansion
    (P : Carrier → Row → Color → ℂ) (z : Color → ℂ) (i j : Row) :
    (∑ b, (∑ c, P b i c * z c) *
      starRingEnd ℂ (∑ d, P b j d * z d)) =
    ∑ b, ∑ c, ∑ d,
      (P b i c * starRingEnd ℂ (P b j d)) *
        (z c * starRingEnd ℂ (z d)) := by
  simp only [map_sum, map_mul]
  simp_rw [Finset.sum_mul, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro b _
  apply Finset.sum_congr rfl
  intro c _
  apply Finset.sum_congr rfl
  intro d _
  ring

/-- The critical fourth-trace target has square-root channel scale. -/
theorem fourth_mass_to_channel_scale (D : ℝ) (hD : 0 ≤ D) :
    Real.sqrt D ^ 2 = D := by
  exact Real.sq_sqrt hD

end QPPureStateChannel
