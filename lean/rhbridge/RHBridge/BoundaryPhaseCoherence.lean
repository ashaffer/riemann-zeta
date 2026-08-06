/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Boundary phase density as inverse defect-line coherence

For a simple symmetric operator with deficiency indices `(1,1)`, let `K` be
the defect kernel and use `-i` as the reference defect point.  If

`rho(x)^2 = |K(-i,x)|^2 / (K(-i,-i) K(x,x))`,

then the canonically oriented Livšic boundary phase satisfies

`Phi'(x) = 2 / ((1+x^2) rho(x)^2)`.

The operator-theoretic kernel identity is recorded in the accompanying
analytic report.  This file isolates its axiom-free scalar consequences.  In
particular, Cauchy--Schwarz gives only `rho^2 <= 1` and hence the universal
Poisson lower bound.  Linear growth in a support parameter is exactly a
quantitative projective-decorrelation estimate.
-/

namespace RHBridge.BoundaryPhaseCoherence

/-- Squared normalized coherence of two nonzero defect lines. -/
noncomputable def coherenceSq (crossSq referenceSq probeSq : ℝ) : ℝ :=
  crossSq / (referenceSq * probeSq)

/-- Phase density written directly in terms of squared coherence. -/
noncomputable def densityFromCoherence (x rhoSq : ℝ) : ℝ :=
  2 / ((1 + x ^ 2) * rhoSq)

/-- The raw resolvent-Gram form of the phase-density identity. -/
noncomputable def densityFromGram
    (x referenceSq probeSq crossSq : ℝ) : ℝ :=
  2 * referenceSq * probeSq / ((1 + x ^ 2) * crossSq)

/-- Substitution of normalized coherence into the Gram formula. -/
theorem densityFromGram_eq_densityFromCoherence
    {x referenceSq probeSq crossSq : ℝ}
    (href : referenceSq ≠ 0) (hprobe : probeSq ≠ 0) (hcross : crossSq ≠ 0) :
    densityFromGram x referenceSq probeSq crossSq =
      densityFromCoherence x (coherenceSq crossSq referenceSq probeSq) := by
  unfold densityFromGram densityFromCoherence coherenceSq
  have hx : 1 + x ^ 2 ≠ 0 := by positivity
  field_simp

/-- Cauchy--Schwarz coherence gives the universal Poisson-kernel lower bound,
but no growth in an external support parameter. -/
theorem universal_lower_of_coherence_le_one
    {x rhoSq : ℝ} (hrho : 0 < rhoSq) (hle : rhoSq ≤ 1) :
    2 / (1 + x ^ 2) ≤ densityFromCoherence x rhoSq := by
  unfold densityFromCoherence
  have hx : 0 < 1 + x ^ 2 := by positivity
  apply (div_le_div_iff_of_pos_left (by norm_num : (0 : ℝ) < 2) hx
    (mul_pos hx hrho)).mpr
  nlinarith

/-- A `1/(L*(1+x^2))` coherence bound is exactly sufficient for a linear
phase-density lower bound. -/
theorem linear_lower_of_coherence_decay
    {x rhoSq L C : ℝ} (hrho : 0 < rhoSq) (hL : 0 < L) (hC : 0 < C)
    (hdecay : rhoSq ≤ C / (L * (1 + x ^ 2))) :
    2 * L / C ≤ densityFromCoherence x rhoSq := by
  unfold densityFromCoherence
  have hx : 0 < 1 + x ^ 2 := by positivity
  have hden : 0 < (1 + x ^ 2) * rhoSq := mul_pos hx hrho
  rw [div_le_div_iff₀ hC hden]
  have hscaled : L * (1 + x ^ 2) * rhoSq ≤ C := by
    have hpos : 0 < L * (1 + x ^ 2) := mul_pos hL hx
    simpa [mul_assoc, mul_comm, mul_left_comm] using
      (le_div_iff₀ hpos).mp hdecay
  nlinarith

/-- In the standard upper-half-plane Clark normalization, the atom weight
corresponding to the inverse-coherence phase density. -/
noncomputable def clarkWeightFromCoherence (x rhoSq : ℝ) : ℝ :=
  Real.pi * (1 + x ^ 2) * rhoSq

/-- The Clark atom is `2*pi/Phi'`; hence linear phase growth can coexist with
weights that decay like the reciprocal support. -/
theorem clarkWeight_eq_two_pi_div_density
    {x rhoSq : ℝ} (hrho : rhoSq ≠ 0) :
    clarkWeightFromCoherence x rhoSq =
      2 * Real.pi / densityFromCoherence x rhoSq := by
  unfold clarkWeightFromCoherence densityFromCoherence
  have hx : 1 + x ^ 2 ≠ 0 := by positivity
  field_simp

end RHBridge.BoundaryPhaseCoherence
