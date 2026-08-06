/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Exact Frostman normalization of a Cayley transform

This file records the elementary identity needed to normalize the proposed
zeta characteristic at `z=i` without accumulating sign or Mobius-transform
errors.  If `Theta=(1-L)/(1+L)` and `alpha=(1-ell)/(1+ell)`, then

`(Theta-alpha)/(1-alpha*Theta) = (ell-L)/(ell+L)`.

The result is purely field algebra.  It makes no assertion that either side
is Schur, inner, holomorphic on a half-plane, or associated with a positive
kernel; those zeta-specific properties are RH-strength statements.
-/

namespace RHBridge.FrostmanCayleyNormalization

noncomputable section

/-- Cayley transform used for the logarithmic derivative. -/
def cayley (L : ℂ) : ℂ :=
  (1 - L) / (1 + L)

/-- Disk automorphism sending `alpha` to zero. -/
def frostman (alpha theta : ℂ) : ℂ :=
  (theta - alpha) / (1 - alpha * theta)

/-- The composed Cayley--Frostman normalization reduces to one fractional
linear expression. -/
theorem frostman_cayley_eq
    (ell L : ℂ) (hell : 1 + ell ≠ 0) (hL : 1 + L ≠ 0)
    (hsum : ell + L ≠ 0) :
    frostman (cayley ell) (cayley L) = (ell - L) / (ell + L) := by
  have hdeneq :
      1 - ((1 - ell) / (1 + ell)) * ((1 - L) / (1 + L)) =
        2 * (ell + L) / ((1 + ell) * (1 + L)) := by
    field_simp [hell, hL]
    ring
  have hfrost :
      1 - ((1 - ell) / (1 + ell)) * ((1 - L) / (1 + L)) ≠ 0 := by
    rw [hdeneq]
    exact div_ne_zero (mul_ne_zero (by norm_num) hsum) (mul_ne_zero hell hL)
  unfold frostman cayley
  rw [hdeneq]
  field_simp [hell, hL, hsum]
  ring

/-- Name for the reduced normalized target. -/
def normalizedTarget (ell L : ℂ) : ℂ :=
  (ell - L) / (ell + L)

@[simp]
theorem normalizedTarget_self (ell : ℂ) :
    normalizedTarget ell ell = 0 := by
  simp [normalizedTarget]

@[simp]
theorem normalizedTarget_zero (ell : ℂ) (hell : ell ≠ 0) :
    normalizedTarget ell 0 = 1 := by
  simp [normalizedTarget, hell]

/-- Oddness of the input logarithmic derivative becomes reciprocal symmetry
of the normalized target. -/
theorem normalizedTarget_neg_eq_inv
    (ell L : ℂ) :
    normalizedTarget ell (-L) = (normalizedTarget ell L)⁻¹ := by
  simp [normalizedTarget, inv_div, sub_eq_add_neg]

end

end RHBridge.FrostmanCayleyNormalization
