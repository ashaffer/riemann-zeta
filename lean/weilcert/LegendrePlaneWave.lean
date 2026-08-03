/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import BridgeLegendre
import LegendreTail
import Mathlib.Analysis.Calculus.Deriv.Polynomial
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts

/-!
Reusable integration-by-parts bridge toward the FULLINF F2 plane-wave
coefficient identity.

This module does not identify `Bridge.legendre` or
`LegendreTail.sphericalJIntegralModel` with any library Bessel function.
-/

namespace LegendrePlaneWave

open Complex Polynomial

/-- The Fourier phase with the convention used by FULLINF,
`exp (-i z t)`. -/
noncomputable def fourierPhase (z t : ℝ) : ℂ :=
  Complex.exp ((-((z : ℂ) * Complex.I)) * (t : ℂ))

/-- Derivative of the real-parameter Fourier phase. -/
theorem hasDerivAt_fourierPhase (z t : ℝ) :
    HasDerivAt (fourierPhase z)
      ((-((z : ℂ) * Complex.I)) * fourierPhase z t) t := by
  let c : ℂ := -((z : ℂ) * Complex.I)
  have h := ((hasDerivAt_id (t : ℂ)).const_mul c).cexp.comp_ofReal
  change HasDerivAt (fun y : ℝ ↦ Complex.exp (c * (y : ℂ)))
    (c * Complex.exp (c * (t : ℂ))) t
  simpa [mul_comm] using h

/-- One complex integration-by-parts step for a real polynomial against the
Fourier phase.  This is the reusable analytic step needed to turn a Rodrigues
formula into a plane-wave coefficient identity. -/
theorem integral_derivative_mul_fourierPhase
    (p : ℝ[X]) (z a b : ℝ) :
    (∫ t in a..b,
        ((p.derivative.eval t : ℝ) : ℂ) * fourierPhase z t) =
      ((p.eval b : ℝ) : ℂ) * fourierPhase z b -
        ((p.eval a : ℝ) : ℂ) * fourierPhase z a +
          ((z : ℂ) * Complex.I) *
            (∫ t in a..b,
              ((p.eval t : ℝ) : ℂ) * fourierPhase z t) := by
  let u : ℝ → ℂ := fourierPhase z
  let u' : ℝ → ℂ := fun t ↦ (-((z : ℂ) * Complex.I)) * u t
  let v : ℝ → ℂ := fun t ↦ ((p.eval t : ℝ) : ℂ)
  let v' : ℝ → ℂ := fun t ↦ ((p.derivative.eval t : ℝ) : ℂ)
  have hu (t : ℝ) : HasDerivAt u (u' t) t := by
    simpa [u, u'] using hasDerivAt_fourierPhase z t
  have hv (t : ℝ) : HasDerivAt v (v' t) t := by
    simpa [v, v'] using (p.hasDerivAt t).ofReal_comp
  have hu_cont : Continuous u :=
    continuous_iff_continuousAt.mpr fun t ↦ (hu t).continuousAt
  have hparts := intervalIntegral.integral_mul_deriv_eq_deriv_mul
    (a := a) (b := b) (u := u) (u' := u') (v := v) (v' := v')
    (fun t _ ↦ hu t) (fun t _ ↦ hv t)
    (by
      apply Continuous.intervalIntegrable
      exact continuous_const.mul hu_cont)
    (by
      apply Continuous.intervalIntegrable
      exact continuous_iff_continuousAt.mpr fun t ↦
        ((p.derivative.hasDerivAt t).ofReal_comp).continuousAt)
  dsimp [u, u', v, v'] at hparts
  have hconst :
      (∫ t in a..b,
        (-((z : ℂ) * Complex.I)) * fourierPhase z t *
          ((p.eval t : ℝ) : ℂ)) =
        (-((z : ℂ) * Complex.I)) *
          (∫ t in a..b,
            fourierPhase z t * ((p.eval t : ℝ) : ℂ)) := by
    calc
      _ = ∫ t in a..b,
          (-((z : ℂ) * Complex.I)) *
            (fourierPhase z t * ((p.eval t : ℝ) : ℂ)) := by
              apply intervalIntegral.integral_congr
              intro t _
              ring
      _ = _ := by rw [intervalIntegral.integral_const_mul]
  rw [hconst] at hparts
  simpa [mul_assoc, mul_comm, mul_left_comm] using hparts

/-- Fourier integral of a real polynomial, viewed as complex-valued. -/
noncomputable def polyFourierIntegral (p : ℝ[X]) (z a b : ℝ) : ℂ :=
  ∫ t in a..b, ((p.eval t : ℝ) : ℂ) * fourierPhase z t

/-- Pull a real polynomial scalar through the complex Fourier integral. -/
theorem polyFourierIntegral_C_mul (c : ℝ) (p : ℝ[X]) (z a b : ℝ) :
    polyFourierIntegral (C c * p) z a b =
      (c : ℂ) * polyFourierIntegral p z a b := by
  rw [polyFourierIntegral, polyFourierIntegral]
  calc
    (∫ t in a..b,
        ((((C c * p).eval t : ℝ) : ℂ) * fourierPhase z t)) =
        ∫ t in a..b,
          (c : ℂ) * (((p.eval t : ℝ) : ℂ) * fourierPhase z t) := by
            apply intervalIntegral.integral_congr
            intro t _
            simp only [eval_mul, eval_C, Complex.ofReal_mul]
            ring
    _ = _ := by rw [intervalIntegral.integral_const_mul]

/-- One-step recurrence in compact polynomial-Fourier notation. -/
theorem polyFourierIntegral_derivative (p : ℝ[X]) (z a b : ℝ) :
    polyFourierIntegral p.derivative z a b =
      ((p.eval b : ℝ) : ℂ) * fourierPhase z b -
        ((p.eval a : ℝ) : ℂ) * fourierPhase z a +
          ((z : ℂ) * Complex.I) * polyFourierIntegral p z a b := by
  simpa [polyFourierIntegral] using
    integral_derivative_mul_fourierPhase p z a b

/-- Repeated integration by parts.  If every derivative below order `n`
vanishes at both endpoints, moving `n` derivatives from a polynomial onto
`exp (-i z t)` multiplies its Fourier integral by `(i z)^n`. -/
theorem polyFourierIntegral_iterate_derivative_of_boundary_zero
    (p : ℝ[X]) (z a b : ℝ) (n : ℕ)
    (hboundary : ∀ j < n,
      ((Polynomial.derivative^[j]) p).eval a = 0 ∧
        ((Polynomial.derivative^[j]) p).eval b = 0) :
    polyFourierIntegral ((Polynomial.derivative^[n]) p) z a b =
      (((z : ℂ) * Complex.I) ^ n) * polyFourierIntegral p z a b := by
  induction n with
  | zero => simp
  | succ n ih =>
      have hends := hboundary n (Nat.lt_succ_self n)
      have hsmall : ∀ j < n,
          ((Polynomial.derivative^[j]) p).eval a = 0 ∧
            ((Polynomial.derivative^[j]) p).eval b = 0 := by
        intro j hj
        exact hboundary j (hj.trans (Nat.lt_succ_self n))
      rw [Function.iterate_succ_apply', polyFourierIntegral_derivative,
        hends.1, hends.2]
      simp only [Complex.ofReal_zero, zero_mul, sub_zero, zero_add]
      rw [ih hsmall, pow_succ]
      ring

/-! ## The Rodrigues weight has the required endpoint zeros -/

/-- Polynomial `(1-X²)^n` occurring in the unshifted Rodrigues formula. -/
noncomputable def rodriguesWeight (n : ℕ) : ℝ[X] :=
  (1 - X ^ 2) ^ n

theorem X_sub_one_pow_dvd_rodriguesWeight (n : ℕ) :
    (X - C (1 : ℝ)) ^ n ∣ rodriguesWeight n := by
  refine ⟨(-1 : ℝ[X]) ^ n * (X + C (1 : ℝ)) ^ n, ?_⟩
  symm
  calc
    (X - C (1 : ℝ)) ^ n *
          ((-1 : ℝ[X]) ^ n * (X + C (1 : ℝ)) ^ n) =
        ((X - C (1 : ℝ)) *
          ((-1 : ℝ[X]) * (X + C (1 : ℝ)))) ^ n := by
            rw [mul_pow, mul_pow]
    _ = rodriguesWeight n := by
      congr 1
      norm_num
      ring

theorem X_add_one_pow_dvd_rodriguesWeight (n : ℕ) :
    (X - C (-1 : ℝ)) ^ n ∣ rodriguesWeight n := by
  refine ⟨(-1 : ℝ[X]) ^ n * (X - C (1 : ℝ)) ^ n, ?_⟩
  symm
  calc
    (X - C (-1 : ℝ)) ^ n *
          ((-1 : ℝ[X]) ^ n * (X - C (1 : ℝ)) ^ n) =
        ((X - C (-1 : ℝ)) *
          ((-1 : ℝ[X]) * (X - C (1 : ℝ)))) ^ n := by
            rw [mul_pow, mul_pow]
    _ = rodriguesWeight n := by
      congr 1
      norm_num
      ring

/-- Every derivative of `(1-X²)^n` below order `n` vanishes at `1`. -/
theorem eval_iterate_derivative_rodriguesWeight_one
    {n j : ℕ} (hj : j < n) :
    ((Polynomial.derivative^[j]) (rodriguesWeight n)).eval 1 = 0 := by
  have hdvd := Polynomial.pow_sub_dvd_iterate_derivative_of_pow_dvd j
    (X_sub_one_pow_dvd_rodriguesWeight n)
  obtain ⟨q, hq⟩ := hdvd
  rw [hq, eval_mul, eval_pow, eval_sub, eval_X, eval_C, sub_self,
    zero_pow (Nat.sub_ne_zero_of_lt hj), zero_mul]

/-- Every derivative of `(1-X²)^n` below order `n` vanishes at `-1`. -/
theorem eval_iterate_derivative_rodriguesWeight_neg_one
    {n j : ℕ} (hj : j < n) :
    ((Polynomial.derivative^[j]) (rodriguesWeight n)).eval (-1) = 0 := by
  have hdvd := Polynomial.pow_sub_dvd_iterate_derivative_of_pow_dvd j
    (X_add_one_pow_dvd_rodriguesWeight n)
  obtain ⟨q, hq⟩ := hdvd
  rw [hq, eval_mul, eval_pow, eval_sub, eval_X, eval_C, sub_self,
    zero_pow (Nat.sub_ne_zero_of_lt hj), zero_mul]

/-- The fully iterated integration-by-parts identity for the Rodrigues weight. -/
theorem rodriguesWeight_iterate_derivative_fourier (n : ℕ) (z : ℝ) :
    polyFourierIntegral
        ((Polynomial.derivative^[n]) (rodriguesWeight n)) z (-1) 1 =
      (((z : ℂ) * Complex.I) ^ n) *
        polyFourierIntegral (rodriguesWeight n) z (-1) 1 := by
  apply polyFourierIntegral_iterate_derivative_of_boundary_zero
  intro j hj
  exact ⟨eval_iterate_derivative_rodriguesWeight_neg_one hj,
    eval_iterate_derivative_rodriguesWeight_one hj⟩

/-! ## Matching the two Fourier-phase conventions -/

/-- The Rodrigues weight is even. -/
@[simp] theorem eval_rodriguesWeight_neg (n : ℕ) (t : ℝ) :
    (rodriguesWeight n).eval (-t) = (1 - t ^ 2) ^ n := by
  simp [rodriguesWeight]

/-- Any even real polynomial has identical positive- and negative-phase
Fourier integrals on `[-1,1]`. -/
theorem polyFourierIntegral_eq_positive_phase_of_even
    (p : ℝ[X]) (z : ℝ) (heven : ∀ t : ℝ, p.eval (-t) = p.eval t) :
    polyFourierIntegral p z (-1) 1 =
      ∫ t in (-1 : ℝ)..1,
        Complex.exp ((z * t : ℝ) * Complex.I) *
          ((p.eval t : ℝ) : ℂ) := by
  let f : ℝ → ℂ := fun t ↦
    Complex.exp ((z * t : ℝ) * Complex.I) *
      ((p.eval t : ℝ) : ℂ)
  have hsub := intervalIntegral.integral_comp_neg
    (a := (-1 : ℝ)) (b := 1) f
  simp only [neg_neg] at hsub
  rw [polyFourierIntegral, ← hsub]
  apply intervalIntegral.integral_congr
  intro t _
  simp only [f, fourierPhase]
  rw [heven]
  push_cast
  ring_nf

/-- On the symmetric interval, evenness of the Rodrigues weight converts the
FULLINF phase `exp (-i z t)` to the positive phase used in
`sphericalJIntegralModel`. -/
theorem polyFourierIntegral_rodriguesWeight_eq_positive_phase
    (n : ℕ) (z : ℝ) :
    polyFourierIntegral (rodriguesWeight n) z (-1) 1 =
      ∫ t in (-1 : ℝ)..1,
        Complex.exp ((z * t : ℝ) * Complex.I) *
          (((1 - t ^ 2) ^ n : ℝ) : ℂ) := by
  simpa [rodriguesWeight] using
    (polyFourierIntegral_eq_positive_phase_of_even
      (rodriguesWeight n) z (fun t ↦ by simp [rodriguesWeight]))

/-- Direct bridge from the local spherical-Bessel integral model to the
Fourier integral of the Rodrigues weight. -/
theorem sphericalJIntegralModel_eq_mul_polyFourierIntegral
    (n : ℕ) (z : ℝ) :
    LegendreTail.sphericalJIntegralModel n z =
      ((z ^ n / (2 ^ (n + 1) * (n.factorial : ℝ)) : ℝ) : ℂ) *
        polyFourierIntegral (rodriguesWeight n) z (-1) 1 := by
  rw [LegendreTail.sphericalJIntegralModel,
    polyFourierIntegral_rodriguesWeight_eq_positive_phase]

end LegendrePlaneWave
