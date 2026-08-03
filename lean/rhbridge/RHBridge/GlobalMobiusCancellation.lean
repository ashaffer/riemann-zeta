/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import Mathlib.Analysis.InnerProductSpace.Basic

/-!
# Global Möbius cancellation and its positivity gate

Möbius inversion is the exact nonlocal incidence operation which removes the
disconnected cross-prime terms from the logarithmic derivative.  It produces
the von Mangoldt function, but naturally as a mixed pairing.  The elementary
lemmas below record why a nonzero pure mixed pairing cannot itself be a
positive quadratic form.
-/

namespace RHBridge.GlobalMobiusCancellation

open ArithmeticFunction
open scoped ArithmeticFunction

/-- The global divisor-incidence cancellation is exactly the von Mangoldt
function.  In coefficients this says
`sum_{d | n} mu(d) log(n / d) = Lambda(n)`. -/
theorem moebiusLog_eq_vonMangoldt :
    (ArithmeticFunction.moebius : ArithmeticFunction ℝ) *
      ArithmeticFunction.log = ArithmeticFunction.vonMangoldt := by
  exact ArithmeticFunction.moebius_mul_log_eq_vonMangoldt

/-- A mixed Hilbert pairing is a polarization (difference) of three squares. -/
theorem mixedPairing_polarization {E : Type*} [SeminormedAddCommGroup E]
    [InnerProductSpace ℝ E] (u v : E) :
    2 * @inner ℝ E _ u v = ‖u + v‖ ^ 2 - ‖u‖ ^ 2 - ‖v‖ ^ 2 := by
  rw [norm_add_sq_real]
  ring

/-- A nonzero pure off-diagonal block has a negative direction: changing the
sign of one channel reverses the mixed quadratic form. -/
theorem mixedPairing_has_negative_direction {E : Type*}
    [SeminormedAddCommGroup E] [InnerProductSpace ℝ E] {u v : E}
    (hcross : @inner ℝ E _ u v ≠ 0) :
    2 * @inner ℝ E _ u v < 0 ∨
      2 * @inner ℝ E _ u (-v) < 0 := by
  rw [inner_neg_right]
  rcases lt_or_gt_of_ne hcross with hneg | hpos
  · exact Or.inl (mul_neg_of_pos_of_neg (by norm_num) hneg)
  · exact Or.inr (by nlinarith)

/-- Consequently, universal nonnegativity of a pure mixed block forces its
cross coefficient to vanish. -/
theorem mixedPairing_nonnegative_for_both_signs_forces_zero {E : Type*}
    [SeminormedAddCommGroup E] [InnerProductSpace ℝ E] (u v : E)
    (hplus : 0 ≤ 2 * @inner ℝ E _ u v)
    (hminus : 0 ≤ 2 * @inner ℝ E _ u (-v)) :
    @inner ℝ E _ u v = 0 := by
  rw [inner_neg_right] at hminus
  nlinarith

end RHBridge.GlobalMobiusCancellation
