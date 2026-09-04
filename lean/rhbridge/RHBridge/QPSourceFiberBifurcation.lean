/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Data.Rat.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Finite algebra for the QP/Turan source-fiber bifurcation

This file formalizes the exact finite-dimensional statements used in the
September 3 audit:

* a legal negative source annihilates its shifted source direction;
* a positive antenna has two different dual normalizations, one for the
  direct radial problem and one for the sufficient transverse source fiber;
* a shallow antenna floor transfers to both dual upper bounds; and
* the relevant exponent identities and strict gaps are exact rationals.

The diffuse real-node construction, replacement by actual prime logarithms,
DPA, LTRAD on actual primes, a zero-free strip, and RH are not formalized or
proved here.
-/

namespace RHBridge.QPSourceFiberBifurcation

noncomputable section

open scoped BigOperators

section FinitePairing

variable {ι : Type*} [Fintype ι]

/-- The real finite pairing used by the convex dual problems. -/
def pairing (x a : ι → ℝ) : ℝ := ∑ i, x i * a i

/-- Total coefficient mass, equivalently pairing with the all-ones vector. -/
def mass (x : ι → ℝ) : ℝ := ∑ i, x i

/-- The shifted event direction `v=a(t₀)+Dq`. -/
def sourceDirection (a : ι → ℝ) (D : ℝ) (i : ι) : ℝ := a i + D

theorem pairing_scale_left (c : ℝ) (x a : ι → ℝ) :
    pairing (fun i => c * x i) a = c * pairing x a := by
  simp only [pairing, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  ring

theorem mass_scale (c : ℝ) (x : ι → ℝ) :
    mass (fun i => c * x i) = c * mass x := by
  simp [mass, Finset.mul_sum]

theorem pairing_sourceDirection (x a : ι → ℝ) (D : ℝ) :
    pairing x (sourceDirection a D) = pairing x a + D * mass x := by
  simp only [pairing, sourceDirection, mass, mul_add, Finset.sum_add_distrib]
  congr 1
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  ring

/-- The event probability is null on `a(t₀)+Dq` when its source response is
exactly `-D`. -/
theorem legalSource_annihilates_direction
    (lam a : ι → ℝ) (D : ℝ)
    (hmass : mass lam = 1) (hsource : pairing lam a = -D) :
    pairing lam (sourceDirection a D) = 0 := by
  rw [pairing_sourceDirection, hsource, hmass]
  ring

/-- Direct radial dual associated with a probability antenna. -/
def radialDual (alpha : ι → ℝ) (i : ι) : ℝ := -alpha i

theorem radialDual_mass
    (alpha : ι → ℝ) (hmass : mass alpha = 1) :
    mass (radialDual alpha) = -1 := by
  change (∑ i, -alpha i) = -1
  rw [Finset.sum_neg_distrib]
  change -(mass alpha) = -1
  rw [hmass]

theorem radialDual_pairing (alpha a : ι → ℝ) :
    pairing (radialDual alpha) a = -pairing alpha a := by
  simp [pairing, radialDual, ← Finset.sum_neg_distrib]

/-- A lower floor for a positive antenna is an upper support bound for its
direct radial dual. -/
theorem radialDual_response_le
    (alpha a : ι → ℝ) (delta : ℝ)
    (hfloor : -delta ≤ pairing alpha a) :
    pairing (radialDual alpha) a ≤ delta := by
  rw [radialDual_pairing]
  linarith

/-- Denominator for the projective source-fiber normalization. -/
def sourceDenominator (alpha a : ι → ℝ) (D : ℝ) : ℝ :=
  D + pairing alpha a

/-- Adaptive separator `y=-alpha/(D+alpha.a(t₀))`. -/
def normalizedSeparator (alpha a : ι → ℝ) (D : ℝ) (i : ι) : ℝ :=
  (-1 / sourceDenominator alpha a D) * alpha i

theorem normalizedSeparator_pairing
    (alpha a atom : ι → ℝ) (D : ℝ) :
    pairing (normalizedSeparator alpha a D) atom =
      (-1 / sourceDenominator alpha a D) * pairing alpha atom := by
  exact pairing_scale_left _ _ _

/-- Probability normalization makes the projective separator pair to `-1`
with the shifted source direction. -/
theorem normalizedSeparator_pairs_sourceDirection
    (alpha a : ι → ℝ) (D : ℝ)
    (hmass : mass alpha = 1)
    (hden : sourceDenominator alpha a D ≠ 0) :
    pairing (normalizedSeparator alpha a D)
      (sourceDirection a D) = -1 := by
  rw [normalizedSeparator_pairing, pairing_sourceDirection, hmass]
  rw [mul_one]
  have hsum : pairing alpha a + D = sourceDenominator alpha a D := by
    simp [sourceDenominator, add_comm]
  rw [hsum]
  field_simp

/-- A shallow antenna floor gives the corresponding projective upper bound
on every high-band atom. -/
theorem normalizedSeparator_response_le
    (alpha sourceAtom atom : ι → ℝ) (D delta : ℝ)
    (hden : 0 < sourceDenominator alpha sourceAtom D)
    (hfloor : -delta ≤ pairing alpha atom) :
    pairing (normalizedSeparator alpha sourceAtom D) atom ≤
      delta / sourceDenominator alpha sourceAtom D := by
  rw [normalizedSeparator_pairing]
  have heq :
      (-1 / sourceDenominator alpha sourceAtom D) * pairing alpha atom =
        -pairing alpha atom / sourceDenominator alpha sourceAtom D := by
    ring
  rw [heq]
  exact (div_le_div_iff_of_pos_right hden).2 (by linarith)

end FinitePairing

section ConvexRadialUpperBound

variable {ι τ : Type*} [Fintype ι] [Fintype τ]

/-- Pairing commutes with a finite linear combination of atoms. -/
theorem pairing_linearCombination
    (z : ι → ℝ) (beta : τ → ℝ) (atom : τ → ι → ℝ) :
    pairing z (fun i => ∑ t, beta t * atom t i) =
      ∑ t, beta t * pairing z (atom t) := by
  simp only [pairing, Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro t _
  apply Finset.sum_congr rfl
  intro i _
  ring

/-- Finite convex duality: a mass `-1` dual whose response to every atom is
at most `delta` bounds any represented negative radial point by `delta`.
This is the direct radial statement, not the `v`-fiber statement. -/
theorem radialPoint_le_of_dual
    (z : ι → ℝ) (beta : τ → ℝ) (atom : τ → ι → ℝ)
    (r delta : ℝ)
    (hzmass : mass z = -1)
    (hbeta_nonneg : ∀ t, 0 ≤ beta t)
    (hbeta_mass : ∑ t, beta t = 1)
    (hrep : ∀ i, (∑ t, beta t * atom t i) = -r)
    (hresponse : ∀ t, pairing z (atom t) ≤ delta) :
    r ≤ delta := by
  have hpair :
      pairing z (fun i => ∑ t, beta t * atom t i) = r := by
    have hfun : (fun i => ∑ t, beta t * atom t i) = (fun _ => -r) :=
      funext hrep
    rw [hfun]
    simp only [pairing]
    calc
      (∑ i, z i * -r) = -r * ∑ i, z i := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro i _
        ring
      _ = r := by change -r * mass z = r; rw [hzmass]; ring
  rw [pairing_linearCombination] at hpair
  rw [← hpair]
  calc
    (∑ t, beta t * pairing z (atom t)) ≤ ∑ t, beta t * delta := by
      apply Finset.sum_le_sum
      intro t _
      exact mul_le_mul_of_nonneg_left (hresponse t) (hbeta_nonneg t)
    _ = delta := by rw [← Finset.sum_mul, hbeta_mass, one_mul]

end ConvexRadialUpperBound

section ExponentLedger

theorem source_plus_transverse_eq_radial :
    (1 : ℚ) / 1000 + 179 / 10000 = 189 / 10000 := by
  norm_num

theorem diffuse_minus_source_eq_badFiber :
    (1 : ℚ) / 2 - 1 / 1000 = 499 / 1000 := by
  norm_num

theorem diffuse_below_dpa_scale : (19 : ℚ) / 1000 < 1 / 2 := by
  norm_num

theorem diffuse_below_directRadialTarget : (189 : ℚ) / 10000 < 1 / 2 := by
  norm_num

theorem badFiber_below_transverseTarget :
    (179 : ℚ) / 10000 < 499 / 1000 := by
  norm_num

end ExponentLedger

end

end RHBridge.QPSourceFiberBifurcation
