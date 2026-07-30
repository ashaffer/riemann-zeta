/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2DigammaTail
import RHBridge.PolyEnclosure

/-!
# Centered polynomial enclosures for the p=2 finite digamma prefix

The first 64 terms of the rational digamma-difference series are the finite
prefix in `quarterDifferenceApprox r K 64`.  On a centered panel
`r = c+x`, each variable denominator is factored exactly as
`D₀ * (1+q(x))`, where `q` is quadratic.  A finite geometric reciprocal
therefore produces an explicit polynomial and a rational error expression.

The perturbation radius is largest at `n=0`, so a generated certificate
needs only one panel-side condition.  No floating-point evaluation occurs in
these proofs.
-/

namespace RHP2Bridge

open scoped BigOperators
open Polynomial

noncomputable def prefixA (n : ℕ) : ℝ := (n : ℝ) + 1 / 4

theorem quarterDifferenceTerm_fifty_eq (r : ℝ) (n : ℕ) :
    GlideKernel.quarterDifferenceTerm r 50 n =
      prefixA n / ((prefixA n) ^ 2 + 625) -
        prefixA n * (((prefixA n) ^ 2 + (r / 2) ^ 2)⁻¹) := by
  unfold GlideKernel.quarterDifferenceTerm prefixA
  norm_num [div_eq_mul_inv]

noncomputable def prefixDenominatorBase (n : ℕ) (c : ℝ) : ℝ :=
  (prefixA n) ^ 2 + (c / 2) ^ 2

noncomputable def prefixDenominatorPerturbation (n : ℕ) (c : ℝ) : ℝ[X] :=
  C (c / (2 * prefixDenominatorBase n c)) * X +
    C (1 / (4 * prefixDenominatorBase n c)) * X ^ 2

noncomputable def prefixDenominatorRho (n : ℕ) (c h : ℝ) : ℝ :=
  |c / (2 * prefixDenominatorBase n c)| * h +
    |1 / (4 * prefixDenominatorBase n c)| * h ^ 2

theorem prefixDenominatorBase_pos (n : ℕ) (c : ℝ) :
    0 < prefixDenominatorBase n c := by
  unfold prefixDenominatorBase prefixA
  positivity

theorem prefixDenominatorRho_eq (n : ℕ) (c h : ℝ) :
    prefixDenominatorRho n c h =
      (|c| / 2 * h + (1 / 4 : ℝ) * h ^ 2) /
        prefixDenominatorBase n c := by
  have hD := prefixDenominatorBase_pos n c
  unfold prefixDenominatorRho
  simp only [abs_div, abs_mul, abs_one, abs_of_pos hD]
  norm_num
  field_simp [hD.ne']

theorem prefixDenominatorBase_zero_le (n : ℕ) (c : ℝ) :
    prefixDenominatorBase 0 c ≤ prefixDenominatorBase n c := by
  unfold prefixDenominatorBase prefixA
  have hn : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
  have ha : (1 / 4 : ℝ) ≤ (n : ℝ) + 1 / 4 := by linarith
  gcongr
  positivity

theorem prefixDenominatorRho_le_zero
    (n : ℕ) (c h : ℝ) (_hh : 0 ≤ h) :
    prefixDenominatorRho n c h ≤ prefixDenominatorRho 0 c h := by
  rw [prefixDenominatorRho_eq, prefixDenominatorRho_eq]
  have hnum : 0 ≤ |c| / 2 * h + (1 / 4 : ℝ) * h ^ 2 := by positivity
  exact div_le_div₀ hnum le_rfl (prefixDenominatorBase_pos 0 c)
    (prefixDenominatorBase_zero_le n c)

theorem prefixDenominator_factor (n : ℕ) (c x : ℝ) :
    prefixDenominatorBase n c *
        (1 + (prefixDenominatorPerturbation n c).eval x) =
      (prefixA n) ^ 2 + ((c + x) / 2) ^ 2 := by
  have hD := (prefixDenominatorBase_pos n c).ne'
  unfold prefixDenominatorPerturbation
  simp only [eval_add, eval_mul, eval_C, eval_X, eval_pow]
  field_simp [hD]
  unfold prefixDenominatorBase
  ring

theorem prefixDenominatorPerturbation_polyBound
    (n : ℕ) (c h : ℝ) (_hh : 0 ≤ h) :
    PolyEnclosure.PolyBound h (prefixDenominatorPerturbation n c)
      (prefixDenominatorRho n c h) := by
  intro x hx
  unfold prefixDenominatorPerturbation prefixDenominatorRho
  simp only [eval_add, eval_mul, eval_C, eval_X, eval_pow]
  calc
    |c / (2 * prefixDenominatorBase n c) * x +
        1 / (4 * prefixDenominatorBase n c) * x ^ 2| ≤
      |c / (2 * prefixDenominatorBase n c) * x| +
        |1 / (4 * prefixDenominatorBase n c) * x ^ 2| := abs_add_le _ _
    _ = |c / (2 * prefixDenominatorBase n c)| * |x| +
        |1 / (4 * prefixDenominatorBase n c)| * |x| ^ 2 := by
      rw [abs_mul, abs_mul, abs_pow]
    _ ≤ |c / (2 * prefixDenominatorBase n c)| * h +
        |1 / (4 * prefixDenominatorBase n c)| * h ^ 2 := by
      gcongr

noncomputable def quarterPrefixTermPolynomial (n : ℕ) (c : ℝ) (M : ℕ) : ℝ[X] :=
  C (prefixA n / ((prefixA n) ^ 2 + 625)) -
    C (prefixA n) *
      (C (prefixDenominatorBase n c)⁻¹ *
        PolyEnclosure.geometricReciprocal
          (prefixDenominatorPerturbation n c) M)

noncomputable def quarterPrefixTermError (n : ℕ) (c h : ℝ) (M : ℕ) : ℝ :=
  |prefixA n| *
    (|(prefixDenominatorBase n c)⁻¹| *
      ((prefixDenominatorRho n c h) ^ M /
        (1 - prefixDenominatorRho n c h)))

theorem quarterDifferenceTerm_centeredEncloses
    (n : ℕ) (c h : ℝ) (M : ℕ) (hh : 0 ≤ h)
    (hrho : prefixDenominatorRho n c h < 1) :
    PolyEnclosure.CenteredEncloses c h
      (fun r => GlideKernel.quarterDifferenceTerm r 50 n)
      (quarterPrefixTermPolynomial n c M)
      (quarterPrefixTermError n c h M) := by
  let D := prefixDenominatorBase n c
  let q := prefixDenominatorPerturbation n c
  let rho := prefixDenominatorRho n c h
  have hD : D ≠ 0 := (prefixDenominatorBase_pos n c).ne'
  have hrho0 : 0 ≤ rho := by
    dsimp [rho, prefixDenominatorRho]
    positivity
  have hq : PolyEnclosure.PolyBound h q rho :=
    prefixDenominatorPerturbation_polyBound n c h hh
  have hrec0 := PolyEnclosure.centeredEncloses_scaledGeometricReciprocal
    c h rho D q M hD hrho0 hrho hq
  have hrec : PolyEnclosure.CenteredEncloses c h
      (fun r => ((prefixA n) ^ 2 + (r / 2) ^ 2)⁻¹)
      (C D⁻¹ * PolyEnclosure.geometricReciprocal q M)
      (|D⁻¹| * (rho ^ M / (1 - rho))) := by
    intro x hx
    have ht := hrec0 x hx
    simp only [add_sub_cancel_left] at ht
    rw [prefixDenominator_factor n c x] at ht
    exact ht
  have hconst : PolyEnclosure.CenteredEncloses c h
      (fun _ => prefixA n / ((prefixA n) ^ 2 + 625))
      (C (prefixA n / ((prefixA n) ^ 2 + 625))) 0 := by
    intro x hx
    simp
  have hterm := hconst.sub (hrec.const_mul (prefixA n))
  simpa [quarterPrefixTermPolynomial, quarterPrefixTermError,
    quarterDifferenceTerm_fifty_eq, prefixA, D, q, rho,
    div_eq_mul_inv, abs_inv] using hterm

noncomputable def quarterDifferenceFinitePrefix (r : ℝ) : ℝ :=
  ∑ n ∈ Finset.range 64, GlideKernel.quarterDifferenceTerm r 50 n

noncomputable def quarterDifferenceFinitePrefixPolynomial
    (c : ℝ) (M : ℕ) : ℝ[X] :=
  ∑ n ∈ Finset.range 64, quarterPrefixTermPolynomial n c M

noncomputable def quarterDifferenceFinitePrefixError
    (c h : ℝ) (M : ℕ) : ℝ :=
  ∑ n ∈ Finset.range 64, quarterPrefixTermError n c h M

theorem quarterDifferenceApprox_sixtyFour_eq
    (r : ℝ) (K : ℕ) :
    quarterDifferenceApprox r K 64 =
      quarterDifferenceFinitePrefix r +
        quarterTailPolynomial r K 64 := by
  rfl

theorem quarterDifferenceFinitePrefix_centeredEncloses
    (c h : ℝ) (M : ℕ) (hh : 0 ≤ h)
    (hrho : ∀ n ∈ Finset.range 64,
      prefixDenominatorRho n c h < 1) :
    PolyEnclosure.CenteredEncloses c h quarterDifferenceFinitePrefix
      (quarterDifferenceFinitePrefixPolynomial c M)
      (quarterDifferenceFinitePrefixError c h M) := by
  intro x hx
  unfold quarterDifferenceFinitePrefix quarterDifferenceFinitePrefixPolynomial
  rw [eval_finsetSum, ← Finset.sum_sub_distrib]
  calc
    |∑ n ∈ Finset.range 64,
        (GlideKernel.quarterDifferenceTerm (c + x) 50 n -
          (quarterPrefixTermPolynomial n c M).eval x)| ≤
      ∑ n ∈ Finset.range 64,
        |GlideKernel.quarterDifferenceTerm (c + x) 50 n -
          (quarterPrefixTermPolynomial n c M).eval x| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ n ∈ Finset.range 64, quarterPrefixTermError n c h M := by
      apply Finset.sum_le_sum
      intro n hn
      exact quarterDifferenceTerm_centeredEncloses n c h M hh (hrho n hn) x hx
    _ = quarterDifferenceFinitePrefixError c h M := rfl

theorem quarterDifferenceFinitePrefix_centeredEncloses_of_rho_zero
    (c h : ℝ) (M : ℕ) (hh : 0 ≤ h)
    (hrho : prefixDenominatorRho 0 c h < 1) :
    PolyEnclosure.CenteredEncloses c h quarterDifferenceFinitePrefix
      (quarterDifferenceFinitePrefixPolynomial c M)
      (quarterDifferenceFinitePrefixError c h M) := by
  apply quarterDifferenceFinitePrefix_centeredEncloses c h M hh
  intro n hn
  exact (prefixDenominatorRho_le_zero n c h hh).trans_lt hrho

end RHP2Bridge
