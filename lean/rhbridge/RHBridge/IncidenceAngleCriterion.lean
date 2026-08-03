/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Angle reserves and contractive dual frames

The completed incidence differential has a manifestly nonnegative energy, but
the relative Weil form subtracts a positive scalar degree.  This file records
two abstract ways in which genuinely phase-sensitive information can close
that deficit.

The first combines separate component floors with an additional angle reserve.
The second shows that a contractive dual frame for the incidence differential
implies the sharp Poincare bound.  It also records the elementary zero-frequency
obstruction: a translation-invariant pointwise Gram multiplier cannot factor a
generator after subtraction of a positive scalar degree.
-/

namespace RHP2Bridge.IncidenceAngleCriterion

open scoped RealInnerProductSpace

/-- Separate component floors close the target once their phase-sensitive
reserves supply the remaining scalar deficit. -/
theorem angleReserve_closes {X : Type*}
    (normSq continuumEnergy primeEnergy continuumReserve primeReserve : X → ℝ)
    {continuumFloor primeFloor angleReserve degree : ℝ}
    (hnorm : ∀ x, 0 ≤ normSq x)
    (hcontinuum : ∀ x,
      continuumFloor * normSq x + continuumReserve x ≤ continuumEnergy x)
    (hprime : ∀ x,
      primeFloor * normSq x + primeReserve x ≤ primeEnergy x)
    (hangle : ∀ x,
      angleReserve * normSq x ≤ continuumReserve x + primeReserve x)
    (hthreshold : degree ≤ continuumFloor + primeFloor + angleReserve) :
    ∀ x, degree * normSq x ≤ continuumEnergy x + primeEnergy x := by
  intro x
  have hscaled := mul_le_mul_of_nonneg_right hthreshold (hnorm x)
  nlinarith [hcontinuum x, hprime x, hangle x]

/-- A normalized translation-invariant generator vanishes at zero frequency,
so subtracting a positive degree makes its zero-frequency symbol negative. -/
theorem shiftedGenerator_negative_at_zero (generator : ℝ → ℝ) {degree : ℝ}
    (hzero : generator 0 = 0) (hdegree : 0 < degree) :
    generator 0 - degree < 0 := by
  rw [hzero]
  linarith

/-- Consequently the shifted symbol cannot itself be a pointwise nonnegative
Gram multiplier.  Any successful factorization must use compact support and
the relative moment constraints rather than act translation-invariantly on the
ambient line. -/
theorem no_pointwise_nonnegative_shift (generator : ℝ → ℝ) {degree : ℝ}
    (hzero : generator 0 = 0) (hdegree : 0 < degree) :
    ¬(∀ frequency, 0 ≤ generator frequency - degree) := by
  intro hnonneg
  have hzeroNonneg := hnonneg 0
  have hnegative := shiftedGenerator_negative_at_zero generator hzero hdegree
  linarith

/-- A contractive dual frame gives the sharp incidence lower bound.  In the
intended application `B` is the completed incidence differential, `C` is an
arithmetic dual frame, and `d^2` is the exact scalar degree deficit. -/
theorem energy_ge_sq_of_contractive_dual
    {H E : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (B C : H →ₗ[ℝ] E) {d : ℝ} (hd : 0 ≤ d)
    (hdual : ∀ x,
      inner ℝ (B x) (C x) = d * inner ℝ x x)
    (hcontractive : ∀ x, ‖C x‖ ≤ ‖x‖) :
    ∀ x, d ^ 2 * ‖x‖ ^ 2 ≤ ‖B x‖ ^ 2 := by
  intro x
  have hcs := abs_real_inner_le_norm (B x) (C x)
  rw [hdual x, real_inner_self_eq_norm_sq,
    abs_of_nonneg (mul_nonneg hd (sq_nonneg ‖x‖))] at hcs
  have hproduct : d * ‖x‖ ^ 2 ≤ ‖B x‖ * ‖x‖ :=
    hcs.trans (mul_le_mul_of_nonneg_left (hcontractive x) (norm_nonneg (B x)))
  by_cases hx : ‖x‖ = 0
  · simp [hx]
  · have hxpos : 0 < ‖x‖ := lt_of_le_of_ne (norm_nonneg x) (Ne.symm hx)
    have hlinear : d * ‖x‖ ≤ ‖B x‖ := by
      apply le_of_mul_le_mul_right _ hxpos
      calc
        (d * ‖x‖) * ‖x‖ = d * ‖x‖ ^ 2 := by ring
        _ ≤ ‖B x‖ * ‖x‖ := hproduct
    nlinarith [norm_nonneg (B x)]

end RHP2Bridge.IncidenceAngleCriterion
