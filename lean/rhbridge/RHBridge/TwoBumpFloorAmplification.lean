/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Algebraic floor amplification for a two-bump witness

This file isolates the scalar step in a translated two-bump argument.  A bump
of radius `r` and a translate separated by `R` fit in the support window
`a = R / 2 + r`.  If phase choice gives the Rayleigh upper bound

`floor a ≤ (q - crossMagnitude) / normSq`,

then any excess of the cross magnitude over the diagonal energy `q` is a
lower bound for the negative part of the floor.  An exponential cross-term
estimate therefore transfers immediately to an exponential negative-floor
witness.

The file deliberately assumes the analytic cross-term estimate.  It proves
only its reusable algebraic consequence and contains no zeta-specific input.
-/

namespace RHBridge.TwoBumpFloorAmplification

noncomputable section

/-- The negative part of a real number, written without committing clients to
a lattice-group notation. -/
def negativePart (x : ℝ) : ℝ :=
  max (-x) 0

/-- A radius-`r` bump and its translate at separation `R` fit in this centered
support window. -/
def twoBumpSupportRadius (R r : ℝ) : ℝ :=
  R / 2 + r

@[simp]
theorem two_mul_supportRadius_sub_radius (R r : ℝ) :
    2 * (twoBumpSupportRadius R r - r) = R := by
  simp only [twoBumpSupportRadius]
  ring

/-- The basic two-bump amplification inequality.  Once the cross magnitude is
at least the diagonal energy, the normalized excess is visible in the
negative part of the spectral floor at the containing support radius. -/
theorem negativePart_floor_ge_cross_sub_q_div
    (q normSq crossMagnitude R r : ℝ) (floor : ℝ → ℝ)
    (hnormSq : 0 < normSq)
    (hfloor :
      floor (twoBumpSupportRadius R r) ≤ (q - crossMagnitude) / normSq)
    (hcross : q ≤ crossMagnitude) :
    (crossMagnitude - q) / normSq ≤
      negativePart (floor (twoBumpSupportRadius R r)) := by
  have hquotient_nonpos : (q - crossMagnitude) / normSq ≤ 0 :=
    div_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr hcross) hnormSq.le
  have hfloor_nonpos : floor (twoBumpSupportRadius R r) ≤ 0 :=
    hfloor.trans hquotient_nonpos
  rw [negativePart, max_eq_left (neg_nonneg.mpr hfloor_nonpos)]
  calc
    (crossMagnitude - q) / normSq =
        -((q - crossMagnitude) / normSq) := by ring
    _ ≤ -floor (twoBumpSupportRadius R r) := neg_le_neg hfloor

/-- A generic nonnegative lower bound on the cross-term excess transfers to
the negative part of the floor. -/
theorem twoBump_witness_transfer
    (q normSq crossMagnitude witness R r : ℝ) (floor : ℝ → ℝ)
    (hnormSq : 0 < normSq) (hwitness : 0 ≤ witness)
    (hfloor :
      floor (twoBumpSupportRadius R r) ≤ (q - crossMagnitude) / normSq)
    (hcross : q + normSq * witness ≤ crossMagnitude) :
    witness ≤ negativePart (floor (twoBumpSupportRadius R r)) := by
  have hcross_q : q ≤ crossMagnitude := by
    calc
      q ≤ q + normSq * witness :=
        le_add_of_nonneg_right (mul_nonneg hnormSq.le hwitness)
      _ ≤ crossMagnitude := hcross
  calc
    witness ≤ (crossMagnitude - q) / normSq := by
      rw [le_div_iff₀ hnormSq]
      linarith
    _ ≤ negativePart (floor (twoBumpSupportRadius R r)) :=
      negativePart_floor_ge_cross_sub_q_div
        q normSq crossMagnitude R r floor hnormSq hfloor hcross_q

/-- Convenient exponential specialization of `twoBump_witness_transfer`.
Any estimate saying that the cross magnitude exceeds `q` by
`normSq * amplitude * exp(rate * R)` yields the same normalized exponential
lower bound for the negative part of the floor in the window
`R / 2 + r`. -/
theorem twoBump_exponential_witness_transfer
    (q normSq crossMagnitude amplitude rate R r : ℝ) (floor : ℝ → ℝ)
    (hnormSq : 0 < normSq) (hamplitude : 0 ≤ amplitude)
    (hfloor :
      floor (twoBumpSupportRadius R r) ≤ (q - crossMagnitude) / normSq)
    (hcross :
      q + normSq * (amplitude * Real.exp (rate * R)) ≤ crossMagnitude) :
    amplitude * Real.exp (rate * R) ≤
      negativePart (floor (twoBumpSupportRadius R r)) := by
  exact twoBump_witness_transfer
    q normSq crossMagnitude (amplitude * Real.exp (rate * R)) R r floor
    hnormSq (mul_nonneg hamplitude (Real.exp_pos _).le) hfloor hcross

end

end RHBridge.TwoBumpFloorAmplification
