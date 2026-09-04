/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Exact finite ledgers for the QP self-orbit total kernel

This file certifies two algebraic reductions used in the total-kernel audit:

* a rooted neighbourhood-degree sum is bounded by the total directed edge
  mass of a zero-one kernel;
* cross-products telescope around any finite cyclic permutation.

It makes no assertion about the open reciprocal-product large sieve or the
sharp four-cycle estimate.
-/

open scoped BigOperators

namespace QPSelfOrbitTotalKernel

variable {Vertex : Type*} [Fintype Vertex]

/-- A root-selected degree sum is at most the total directed edge mass.
Symmetry is not needed for this finite implication. -/
theorem rooted_degree_sum_le_total
    (X : Vertex → Vertex → ℕ) (root : Vertex)
    (hX : ∀ i j, X i j ≤ 1) :
    (∑ t, X root t * ∑ j, X t j) ≤ ∑ t, ∑ j, X t j := by
  apply Finset.sum_le_sum
  intro t _
  calc
    X root t * (∑ j, X t j) ≤ 1 * (∑ j, X t j) := by
      gcongr
      exact hX root t
    _ = ∑ j, X t j := one_mul _

/-- Reindexing either coordinate by the same finite permutation preserves
the product of cross-products.  A cyclic successor is the application used
for the self-orbit holonomy ledger. -/
theorem permuted_cross_product_telescopes
    {R : Type*} [CommMonoid R]
    (next : Equiv.Perm Vertex) (x b B : Vertex → R) :
  (∏ i, x i * b i * B (next i)) =
      ∏ i, x i * B i * b (next i) := by
  simp_rw [Finset.prod_mul_distrib]
  have hB : (∏ i, B (next i)) = ∏ i, B i := next.bijective.prod_comp B
  have hb : (∏ i, b (next i)) = ∏ i, b i := next.bijective.prod_comp b
  rw [hB, hb]
  ac_rfl

/-- Exact product identity behind cycle holonomy.  The hypotheses are the
two oriented cross-product residual definitions; no small-error estimate is
formalized here. -/
theorem cycle_error_products_telescope
    (next : Equiv.Perm Vertex)
    (Q : ℤ) (e f x b B : Vertex → ℤ)
    (he : ∀ i, Q + e i = (8 * x i) * b i * B (next i))
    (hf : ∀ i, Q + f i = (8 * x i) * B i * b (next i)) :
    (∏ i, (Q + e i)) = ∏ i, (Q + f i) := by
  calc
    (∏ i, (Q + e i)) = ∏ i, (8 * x i) * b i * B (next i) := by
      apply Finset.prod_congr rfl
      intro i _
      exact he i
    _ = ∏ i, (8 * x i) * B i * b (next i) :=
      permuted_cross_product_telescopes next (fun i ↦ 8 * x i) b B
    _ = ∏ i, (Q + f i) := by
      apply Finset.prod_congr rfl
      intro i _
      exact (hf i).symm

end QPSelfOrbitTotalKernel
