/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Optimality of the local prime-edge polarization

The arithmetic term attached to a logarithmic translation contains a negative
cross term.  Completing it to the square `(u - v)^2` costs one diagonal copy
at each endpoint.  The lemmas below record that this cost is optimal among all
real Gram representations: positivity alone forces the total diagonal cost to
be at least twice the desired cross coefficient.

This is an abstract obstruction, not an RH assumption.  It isolates why a
place-by-place sum-of-squares decomposition cannot repair a negative completed
residual by choosing a more elaborate local Gram space.
-/

namespace RHBridge.PrimeEdgePolarization

/-- The exact difference-square polarization of one negative cross term. -/
theorem differenceSquare_identity (w x y : ℝ) :
    w * (x - y) ^ 2 = w * x ^ 2 + w * y ^ 2 - 2 * w * x * y := by
  ring

/-- Any two Gram vectors pay at least twice their (nonnegative) cross mass. -/
theorem gram_diagonal_cost {E : Type*} [SeminormedAddCommGroup E]
    [InnerProductSpace ℝ E] (u v : E) (w : ℝ)
    (huv : @inner ℝ E _ u v = w) :
    2 * w ≤ ‖u‖ ^ 2 + ‖v‖ ^ 2 := by
  have hnonneg : 0 ≤ ‖u - v‖ ^ 2 := sq_nonneg ‖u - v‖
  rw [norm_sub_sq_real, huv] at hnonneg
  linarith

/-- Scalar version used for a single rank-one square.

If `a*b=w`, the square `(a*x-b*y)^2` has the requested cross coefficient,
but its two diagonal coefficients necessarily sum to at least `2*w`.
-/
theorem rankOne_diagonal_cost {a b w : ℝ} (hab : a * b = w) :
    2 * w ≤ a ^ 2 + b ^ 2 := by
  nlinarith [sq_nonneg (a - b)]

/-- The lower bound is sharp: equal endpoint weights attain it. -/
theorem rankOne_cost_sharp (c : ℝ) :
    2 * c ^ 2 = c ^ 2 + c ^ 2 := by
  ring

end RHBridge.PrimeEdgePolarization
