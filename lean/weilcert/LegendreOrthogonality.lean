/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import LegendreRodrigues

/-!
Orthogonality of the analysis-facing Legendre family against lower-degree
polynomials, derived directly from Rodrigues' formula.
-/

namespace LegendreOrthogonality

open Polynomial

/-- Real interval inner product of two polynomial evaluations. -/
noncomputable def polynomialPairIntegral
    (p q : ℝ[X]) (a b : ℝ) : ℝ :=
  ∫ t in a..b, p.eval t * q.eval t

/-- One integration-by-parts step for two real polynomials. -/
theorem polynomialPairIntegral_derivative
    (p q : ℝ[X]) (a b : ℝ) :
    polynomialPairIntegral p.derivative q a b =
      p.eval b * q.eval b - p.eval a * q.eval a -
        polynomialPairIntegral p q.derivative a b := by
  have h := intervalIntegral.integral_mul_deriv_eq_deriv_mul
    (a := a) (b := b)
    (u := fun t : ℝ ↦ q.eval t)
    (u' := fun t : ℝ ↦ q.derivative.eval t)
    (v := fun t : ℝ ↦ p.eval t)
    (v' := fun t : ℝ ↦ p.derivative.eval t)
    (fun t _ ↦ q.hasDerivAt t)
    (fun t _ ↦ p.hasDerivAt t)
    (by
      apply Continuous.intervalIntegrable
      exact continuous_iff_continuousAt.mpr fun t ↦
        (q.derivative.hasDerivAt t).continuousAt)
    (by
      apply Continuous.intervalIntegrable
      exact continuous_iff_continuousAt.mpr fun t ↦
        (p.derivative.hasDerivAt t).continuousAt)
  simpa [polynomialPairIntegral, mul_comm] using h

/-- Symmetry of the polynomial interval inner product. -/
theorem polynomialPairIntegral_comm
    (p q : ℝ[X]) (a b : ℝ) :
    polynomialPairIntegral p q a b =
      polynomialPairIntegral q p a b := by
  apply intervalIntegral.integral_congr
  intro t _
  ring

/-- Pull a constant polynomial factor through the first argument. -/
theorem polynomialPairIntegral_C_mul_left
    (c : ℝ) (p q : ℝ[X]) (a b : ℝ) :
    polynomialPairIntegral (C c * p) q a b =
      c * polynomialPairIntegral p q a b := by
  rw [polynomialPairIntegral, polynomialPairIntegral]
  calc
    (∫ t in a..b, (C c * p).eval t * q.eval t) =
        ∫ t in a..b, c * (p.eval t * q.eval t) := by
          apply intervalIntegral.integral_congr
          intro t _
          simp only [eval_mul, eval_C]
          ring
    _ = _ := by rw [intervalIntegral.integral_const_mul]

/-- Pull a constant polynomial factor through the second argument. -/
theorem polynomialPairIntegral_C_mul_right
    (c : ℝ) (p q : ℝ[X]) (a b : ℝ) :
    polynomialPairIntegral p (C c * q) a b =
      c * polynomialPairIntegral p q a b := by
  rw [polynomialPairIntegral_comm,
    polynomialPairIntegral_C_mul_left,
    polynomialPairIntegral_comm]

/-- Repeated polynomial integration by parts.  If the first `n` endpoint
jets of `p` vanish, moving `n` derivatives from `p` to `q` contributes the
sign `(-1)^n`. -/
theorem polynomialPairIntegral_iterate_derivative_of_boundary_zero
    (p q : ℝ[X]) (a b : ℝ) (n : ℕ)
    (hboundary : ∀ j < n,
      ((Polynomial.derivative^[j]) p).eval a = 0 ∧
        ((Polynomial.derivative^[j]) p).eval b = 0) :
    polynomialPairIntegral
        ((Polynomial.derivative^[n]) p) q a b =
      (-1 : ℝ) ^ n *
        polynomialPairIntegral p
          ((Polynomial.derivative^[n]) q) a b := by
  induction n generalizing q with
  | zero => simp
  | succ n ih =>
      have hends := hboundary n (Nat.lt_succ_self n)
      have hsmall : ∀ j < n,
          ((Polynomial.derivative^[j]) p).eval a = 0 ∧
            ((Polynomial.derivative^[j]) p).eval b = 0 := by
        intro j hj
        exact hboundary j (hj.trans (Nat.lt_succ_self n))
      rw [Function.iterate_succ_apply',
        polynomialPairIntegral_derivative, hends.1, hends.2]
      simp only [zero_mul, sub_zero, zero_sub]
      rw [ih q.derivative hsmall, Function.iterate_succ_apply, pow_succ]
      ring

/-- Every polynomial of degree below `n` is orthogonal to the `n`th
Rodrigues derivative. -/
theorem rodriguesWeight_iterate_derivative_orthogonal_of_natDegree_lt
    (n : ℕ) (q : ℝ[X]) (hq : q.natDegree < n) :
    polynomialPairIntegral
      ((Polynomial.derivative^[n])
        (LegendrePlaneWave.rodriguesWeight n)) q (-1) 1 = 0 := by
  rw [polynomialPairIntegral_iterate_derivative_of_boundary_zero
    (p := LegendrePlaneWave.rodriguesWeight n) (q := q)
    (a := (-1 : ℝ)) (b := 1) (n := n)]
  · rw [Polynomial.iterate_derivative_eq_zero hq]
    simp [polynomialPairIntegral]
  · intro j hj
    exact ⟨
      LegendrePlaneWave.eval_iterate_derivative_rodriguesWeight_neg_one hj,
      LegendrePlaneWave.eval_iterate_derivative_rodriguesWeight_one hj⟩

/-- Mapping the shifted family from integers to reals preserves its degree. -/
@[simp] theorem natDegree_shiftedLegendreReal (n : ℕ) :
    (LegendreRodrigues.shiftedLegendreReal n).natDegree = n := by
  rw [LegendreRodrigues.shiftedLegendreReal,
    Polynomial.natDegree_map_eq_of_injective Int.cast_injective,
    Polynomial.natDegree_shiftedLegendre]

/-- The transformed shifted-Legendre family has its expected degree. -/
@[simp] theorem natDegree_plainLegendre (n : ℕ) :
    (LegendreRodrigues.plainLegendre n).natDegree = n := by
  have haffine :
      (C (-(1 / 2 : ℝ)) * X + C (1 / 2 : ℝ)).natDegree = 1 := by
    rw [Polynomial.natDegree_eq_one]
    exact ⟨-(1 / 2 : ℝ), by norm_num, 1 / 2, rfl⟩
  rw [LegendreRodrigues.plainLegendre, Polynomial.natDegree_comp,
    natDegree_shiftedLegendreReal, haffine, Nat.mul_one]

/-- Leading coefficient of the real shifted family. -/
theorem leadingCoeff_shiftedLegendreReal (n : ℕ) :
    (LegendreRodrigues.shiftedLegendreReal n).leadingCoeff =
      (-1 : ℝ) ^ n * (n.centralBinom : ℝ) := by
  rw [Polynomial.leadingCoeff, natDegree_shiftedLegendreReal,
    LegendreRodrigues.shiftedLegendreReal, Polynomial.coeff_map,
    Polynomial.coeff_shiftedLegendre]
  simp only [Nat.choose_self, Nat.cast_one, mul_one,
    Nat.centralBinom_eq_two_mul_choose]
  rw [show n + n = 2 * n by omega]
  simp

/-- Classical leading coefficient `binomial(2n,n)/2^n` of the unshifted
family. -/
theorem leadingCoeff_plainLegendre (n : ℕ) :
    (LegendreRodrigues.plainLegendre n).leadingCoeff =
      (n.centralBinom : ℝ) / 2 ^ n := by
  have hqnat :
      (C (-(1 / 2 : ℝ)) * X + C (1 / 2 : ℝ)).natDegree = 1 := by
    rw [Polynomial.natDegree_eq_one]
    exact ⟨-(1 / 2 : ℝ), by norm_num, 1 / 2, rfl⟩
  have hqlead :
      (C (-(1 / 2 : ℝ)) * X + C (1 / 2 : ℝ)).leadingCoeff =
        -(1 / 2 : ℝ) := by
    rw [Polynomial.leadingCoeff, hqnat]
    simp
  have hqne :
      (C (-(1 / 2 : ℝ)) * X + C (1 / 2 : ℝ)).natDegree ≠ 0 := by
    rw [hqnat]
    norm_num
  rw [LegendreRodrigues.plainLegendre,
    Polynomial.leadingCoeff_comp hqne,
    leadingCoeff_shiftedLegendreReal,
    natDegree_shiftedLegendreReal, hqlead]
  have hsign : (-1 : ℝ) ^ n * (-1 : ℝ) ^ n = 1 := by
    rw [← mul_pow]
    norm_num
  rw [show (-(1 / 2 : ℝ)) ^ n =
      (-1 : ℝ) ^ n * (1 / 2 : ℝ) ^ n by
        rw [show -(1 / 2 : ℝ) = (-1) * (1 / 2) by ring, mul_pow]]
  rw [mul_assoc, mul_left_comm (n.centralBinom : ℝ), ← mul_assoc,
    hsign, one_mul]
  rw [one_div, inv_pow, div_eq_mul_inv]

/-- The `n`th derivative of `Pₙ` is its top coefficient times `n!`. -/
theorem iterate_derivative_plainLegendre_self (n : ℕ) :
    (Polynomial.derivative^[n])
        (LegendreRodrigues.plainLegendre n) =
      C ((n.factorial : ℝ) *
        ((n.centralBinom : ℝ) / 2 ^ n)) := by
  have hdeg := Polynomial.natDegree_iterate_derivative
    (LegendreRodrigues.plainLegendre n) n
  rw [natDegree_plainLegendre, Nat.sub_self] at hdeg
  rw [Polynomial.eq_C_of_natDegree_le_zero hdeg]
  congr 1
  rw [Polynomial.coeff_iterate_derivative, zero_add,
    Nat.descFactorial_self, nsmul_eq_mul]
  rw [show (LegendreRodrigues.plainLegendre n).coeff n =
      (LegendreRodrigues.plainLegendre n).leadingCoeff by
        rw [Polynomial.leadingCoeff, natDegree_plainLegendre],
    leadingCoeff_plainLegendre]

/-- An `n`th derivative at the top degree is the constant `n!` times the
top coefficient. -/
theorem iterate_derivative_eq_C_factorial_mul_coeff_of_natDegree_le
    (p : ℝ[X]) (n : ℕ) (hdeg : p.natDegree ≤ n) :
    (Polynomial.derivative^[n]) p =
      C ((n.factorial : ℝ) * p.coeff n) := by
  rw [Polynomial.eq_C_of_natDegree_le_zero
    ((Polynomial.natDegree_iterate_derivative p n).trans
      (Nat.sub_eq_zero_of_le hdeg).le)]
  congr 1
  rw [Polynomial.coeff_iterate_derivative, Nat.zero_add,
    Nat.descFactorial_self]
  simp [nsmul_eq_mul]

/-- Degree of the Rodrigues weight. -/
@[simp] theorem natDegree_rodriguesWeight (n : ℕ) :
    (LegendrePlaneWave.rodriguesWeight n).natDegree = 2 * n := by
  have hi : (1 - X ^ 2 : ℝ[X]) = -(X ^ 2 - 1) := by ring
  have hinner : (X ^ 2 - 1 : ℝ[X]).natDegree = 2 := by
    simpa only [Polynomial.C_1] using
      (Polynomial.natDegree_X_pow_sub_C (R := ℝ) (n := 2) (r := 1))
  rw [LegendrePlaneWave.rodriguesWeight, hi, Polynomial.natDegree_pow,
    Polynomial.natDegree_neg, hinner]
  omega

/-- Top coefficient of the Rodrigues weight. -/
theorem leadingCoeff_rodriguesWeight (n : ℕ) :
    (LegendrePlaneWave.rodriguesWeight n).leadingCoeff =
      (-1 : ℝ) ^ n := by
  have hi : (1 - X ^ 2 : ℝ[X]) = -(X ^ 2 - 1) := by ring
  rw [LegendrePlaneWave.rodriguesWeight, hi,
    Polynomial.leadingCoeff_pow, Polynomial.leadingCoeff_neg,
    Polynomial.leadingCoeff_X_pow_sub_one]
  norm_num

theorem coeff_rodriguesWeight_top (n : ℕ) :
    (LegendrePlaneWave.rodriguesWeight n).coeff (2 * n) =
      (-1 : ℝ) ^ n := by
  rw [← natDegree_rodriguesWeight n]
  exact leadingCoeff_rodriguesWeight n

/-- Differentiating the degree-`2n` weight `2n` times retains only its top
coefficient. -/
theorem iterate_derivative_twice_rodriguesWeight (n : ℕ) :
    (Polynomial.derivative^[2 * n])
        (LegendrePlaneWave.rodriguesWeight n) =
      C (((2 * n).factorial : ℝ) * (-1 : ℝ) ^ n) := by
  rw [iterate_derivative_eq_C_factorial_mul_coeff_of_natDegree_le]
  · rw [coeff_rodriguesWeight_top]
  · exact (natDegree_rodriguesWeight n).le

theorem factorial_two_mul_eq_pow_mul_factorial_mul_doubleFactorial
    (n : ℕ) :
    (2 * n).factorial =
      (2 ^ n * n.factorial) * Nat.doubleFactorial (2 * n - 1) := by
  cases n with
  | zero => norm_num
  | succ n =>
      rw [show 2 * (n + 1) = (2 * n + 1) + 1 by omega,
        Nat.factorial_eq_mul_doubleFactorial,
        show 2 * n + 1 + 1 = 2 * (n + 1) by omega,
        Nat.doubleFactorial_two_mul]
      congr 1

/-- Equivalent double-factorial form of the top derivative of `Pₙ`. -/
theorem iterate_derivative_plainLegendre_eq_doubleFactorial (n : ℕ) :
    (Polynomial.derivative^[n])
        (LegendreRodrigues.plainLegendre n) =
      C (Nat.doubleFactorial (2 * n - 1) : ℝ) := by
  have h := congrArg (Polynomial.derivative^[n])
    (LegendreRodrigues.rodrigues_plainLegendre n)
  rw [Polynomial.iterate_derivative_C_mul,
    Polynomial.iterate_derivative_C_mul,
    ← Function.iterate_add_apply,
    show n + n = 2 * n by omega,
    iterate_derivative_twice_rodriguesWeight] at h
  have hfact :=
    factorial_two_mul_eq_pow_mul_factorial_mul_doubleFactorial n
  norm_num only [Polynomial.C_mul] at h
  apply (mul_left_cancel₀
    (show C (((2 : ℝ) ^ n) * (n.factorial : ℝ)) ≠ 0 by
      simpa using (Polynomial.C_ne_zero.mpr
        (mul_ne_zero (pow_ne_zero n (by norm_num : (2 : ℝ) ≠ 0))
          (by positivity : (n.factorial : ℝ) ≠ 0)))))
  rw [Polynomial.C_mul, h]
  have hfactR : ((2 * n).factorial : ℝ) =
      ((2 : ℝ) ^ n * (n.factorial : ℝ)) *
        (Nat.doubleFactorial (2 * n - 1) : ℝ) := by
    exact_mod_cast hfact
  rw [hfactR]
  simp only [Polynomial.C_mul]
  have hsign : (-1 : ℝ) ^ n * (-1 : ℝ) ^ n = 1 := by
    rw [← mul_pow]
    norm_num
  have hsignC :
      C ((-1 : ℝ) ^ n) * C ((-1 : ℝ) ^ n) = 1 := by
    rw [← Polynomial.C_mul, hsign]
    simp
  calc
    C ((-1 : ℝ) ^ n) *
        (C ((2 : ℝ) ^ n) * C (n.factorial : ℝ) *
          C (Nat.doubleFactorial (2 * n - 1) : ℝ) *
          C ((-1 : ℝ) ^ n)) =
      (C ((-1 : ℝ) ^ n) * C ((-1 : ℝ) ^ n)) *
        (C ((2 : ℝ) ^ n) * C (n.factorial : ℝ) *
          C (Nat.doubleFactorial (2 * n - 1) : ℝ)) := by ring
    _ = _ := by rw [hsignC]; simp

/-- Pairing the Rodrigues weight with a constant is the previously computed
weight integral times that constant. -/
theorem polynomialPairIntegral_rodriguesWeight_C
    (n : ℕ) (c : ℝ) :
    polynomialPairIntegral
        (LegendrePlaneWave.rodriguesWeight n) (C c) (-1) 1 =
      c * LegendreTail.weightIntegral n := by
  rw [polynomialPairIntegral, LegendreTail.weightIntegral]
  calc
    (∫ t in (-1 : ℝ)..1,
        (LegendrePlaneWave.rodriguesWeight n).eval t * (C c).eval t) =
      ∫ t in (-1 : ℝ)..1, c * (1 - t ^ 2) ^ n := by
        apply intervalIntegral.integral_congr
        intro t _
        simp [LegendrePlaneWave.rodriguesWeight]
        ring
    _ = _ := by rw [intervalIntegral.integral_const_mul]

/-- Norm identity before simplifying the elementary factorial expression. -/
theorem plainLegendre_norm_scaled (n : ℕ) :
    ((2 : ℝ) ^ n * (n.factorial : ℝ)) *
        polynomialPairIntegral
          (LegendreRodrigues.plainLegendre n)
          (LegendreRodrigues.plainLegendre n) (-1) 1 =
      ((n.factorial : ℝ) *
        ((n.centralBinom : ℝ) / 2 ^ n)) *
          LegendreTail.weightIntegral n := by
  let P : ℝ[X] := LegendreRodrigues.plainLegendre n
  let W : ℝ[X] := LegendrePlaneWave.rodriguesWeight n
  have hpoly := congrArg
    (fun p : ℝ[X] ↦ polynomialPairIntegral p P (-1) 1)
    (LegendreRodrigues.rodrigues_plainLegendre n)
  rw [polynomialPairIntegral_C_mul_left,
    polynomialPairIntegral_C_mul_left] at hpoly
  have hibp :=
    polynomialPairIntegral_iterate_derivative_of_boundary_zero
      W P (-1) 1 n (by
        intro j hj
        exact ⟨
          LegendrePlaneWave.eval_iterate_derivative_rodriguesWeight_neg_one hj,
          LegendrePlaneWave.eval_iterate_derivative_rodriguesWeight_one hj⟩)
  have hsign : (-1 : ℝ) ^ n * (-1 : ℝ) ^ n = 1 := by
    rw [← mul_pow]
    norm_num
  change ((2 : ℝ) ^ n * (n.factorial : ℝ)) *
      polynomialPairIntegral P P (-1) 1 = _
  calc
    ((2 : ℝ) ^ n * (n.factorial : ℝ)) *
        polynomialPairIntegral P P (-1) 1 =
      (-1 : ℝ) ^ n *
        polynomialPairIntegral
          ((Polynomial.derivative^[n]) W) P (-1) 1 := hpoly
    _ = (-1 : ℝ) ^ n *
        ((-1 : ℝ) ^ n *
          polynomialPairIntegral W
            ((Polynomial.derivative^[n]) P) (-1) 1) := by rw [hibp]
    _ = _ := by
      rw [show (Polynomial.derivative^[n]) P =
          C ((n.factorial : ℝ) *
            ((n.centralBinom : ℝ) / 2 ^ n)) by
            simpa [P] using iterate_derivative_plainLegendre_self n,
        show polynomialPairIntegral W
            (C ((n.factorial : ℝ) *
              ((n.centralBinom : ℝ) / 2 ^ n))) (-1) 1 =
            ((n.factorial : ℝ) *
              ((n.centralBinom : ℝ) / 2 ^ n)) *
                LegendreTail.weightIntegral n by
          simpa [W] using polynomialPairIntegral_rodriguesWeight_C n
            ((n.factorial : ℝ) *
              ((n.centralBinom : ℝ) / 2 ^ n)),
        ← mul_assoc, hsign, one_mul]

/-- The double-factorial and weight-integral factors simplify to the
classical Legendre normalization. -/
theorem doubleFactorial_mul_weightIntegral_eq (n : ℕ) :
    (Nat.doubleFactorial (2 * n - 1) : ℝ) *
        LegendreTail.weightIntegral n =
      ((2 : ℝ) ^ n * (n.factorial : ℝ)) *
        (2 / (2 * (n : ℝ) + 1)) := by
  rw [LegendreTail.weightIntegral_eq]
  have hrec : Nat.doubleFactorial (2 * n + 1) =
      (2 * n + 1) * Nat.doubleFactorial (2 * n - 1) := by
    simpa only using Nat.doubleFactorial_add_one (2 * n)
  have hrecR : (Nat.doubleFactorial (2 * n + 1) : ℝ) =
      (2 * (n : ℝ) + 1) *
        (Nat.doubleFactorial (2 * n - 1) : ℝ) := by
    exact_mod_cast hrec
  rw [hrecR, pow_succ]
  have hdf :
      (Nat.doubleFactorial (2 * n - 1) : ℝ) ≠ 0 := by positivity
  have hn : 2 * (n : ℝ) + 1 ≠ 0 := by positivity
  field_simp

/-- Exact diagonal norm of the all-degree Legendre family. -/
theorem plainLegendre_pair_self (n : ℕ) :
    polynomialPairIntegral
        (LegendreRodrigues.plainLegendre n)
        (LegendreRodrigues.plainLegendre n) (-1) 1 =
      2 / (2 * (n : ℝ) + 1) := by
  let P : ℝ[X] := LegendreRodrigues.plainLegendre n
  let W : ℝ[X] := LegendrePlaneWave.rodriguesWeight n
  let A : ℝ := (2 : ℝ) ^ n * (n.factorial : ℝ)
  let d : ℝ := Nat.doubleFactorial (2 * n - 1)
  have hrod := congrArg
    (fun p : ℝ[X] ↦ polynomialPairIntegral p P (-1) 1)
    (LegendreRodrigues.rodrigues_plainLegendre n)
  have hibp :
      polynomialPairIntegral
          ((Polynomial.derivative^[n]) W) P (-1) 1 =
        (-1 : ℝ) ^ n *
          polynomialPairIntegral W
            ((Polynomial.derivative^[n]) P) (-1) 1 := by
    apply polynomialPairIntegral_iterate_derivative_of_boundary_zero
    intro j hj
    exact ⟨
      LegendrePlaneWave.eval_iterate_derivative_rodriguesWeight_neg_one hj,
      LegendrePlaneWave.eval_iterate_derivative_rodriguesWeight_one hj⟩
  have hderiv : (Polynomial.derivative^[n]) P = C d := by
    simpa [P, d] using
      iterate_derivative_plainLegendre_eq_doubleFactorial n
  rw [polynomialPairIntegral_C_mul_left,
    polynomialPairIntegral_C_mul_left] at hrod
  change A * polynomialPairIntegral P P (-1) 1 =
    (-1 : ℝ) ^ n *
      polynomialPairIntegral
        ((Polynomial.derivative^[n]) W) P (-1) 1 at hrod
  rw [hibp, hderiv,
    show polynomialPairIntegral W (C d) (-1) 1 =
        d * LegendreTail.weightIntegral n by
      simpa [W, d] using
        polynomialPairIntegral_rodriguesWeight_C n d] at hrod
  have hsign : (-1 : ℝ) ^ n * (-1 : ℝ) ^ n = 1 := by
    rw [← mul_pow]
    norm_num
  rw [← mul_assoc, hsign, one_mul] at hrod
  have hnumeric : d * LegendreTail.weightIntegral n =
      A * (2 / (2 * (n : ℝ) + 1)) := by
    simpa [A, d] using doubleFactorial_mul_weightIntegral_eq n
  rw [hnumeric] at hrod
  have hA : A ≠ 0 := by
    dsimp [A]
    positivity
  apply mul_left_cancel₀ hA
  exact hrod

/-- Integral form of the exact squared norm. -/
theorem plainLegendre_norm_sq (n : ℕ) :
    (∫ x in (-1 : ℝ)..1,
      (LegendreRodrigues.plainLegendre n).eval x ^ 2) =
      2 / (2 * (n : ℝ) + 1) := by
  simpa [polynomialPairIntegral, pow_two] using
    plainLegendre_pair_self n

/-- `plainLegendre n` is orthogonal to every polynomial of degree below
`n`.  This is the triangular form of Legendre orthogonality. -/
theorem plainLegendre_orthogonal_of_natDegree_lt
    (n : ℕ) (q : ℝ[X]) (hq : q.natDegree < n) :
    polynomialPairIntegral
      (LegendreRodrigues.plainLegendre n) q (-1) 1 = 0 := by
  have hpoly := congrArg
    (fun p : ℝ[X] ↦ polynomialPairIntegral p q (-1) 1)
    (LegendreRodrigues.rodrigues_plainLegendre n)
  rw [polynomialPairIntegral_C_mul_left,
    polynomialPairIntegral_C_mul_left,
    rodriguesWeight_iterate_derivative_orthogonal_of_natDegree_lt n q hq,
    mul_zero] at hpoly
  have hscale : (2 : ℝ) ^ n * (n.factorial : ℝ) ≠ 0 := by positivity
  exact (mul_eq_zero.mp hpoly).resolve_left hscale

/-- Pairwise orthogonality for distinct members of the all-degree family. -/
theorem plainLegendre_pairwise_orthogonal
    {m n : ℕ} (hmn : m ≠ n) :
    polynomialPairIntegral
      (LegendreRodrigues.plainLegendre m)
      (LegendreRodrigues.plainLegendre n) (-1) 1 = 0 := by
  rcases lt_or_gt_of_ne hmn with hlt | hgt
  · rw [polynomialPairIntegral_comm]
    exact plainLegendre_orthogonal_of_natDegree_lt n
      (LegendreRodrigues.plainLegendre m) (by simpa using hlt)
  · exact plainLegendre_orthogonal_of_natDegree_lt m
      (LegendreRodrigues.plainLegendre n) (by simpa using hgt)

/-! ## Orthonormal normalization -/

/-- Unit-normalized Legendre polynomial for the unweighted interval
`[-1,1]`. -/
noncomputable def normalizedPlainLegendre (n : ℕ) : ℝ[X] :=
  C (Real.sqrt ((2 * (n : ℝ) + 1) / 2)) *
    LegendreRodrigues.plainLegendre n

theorem normalizedPlainLegendre_pair_self (n : ℕ) :
    polynomialPairIntegral
        (normalizedPlainLegendre n)
        (normalizedPlainLegendre n) (-1) 1 = 1 := by
  rw [normalizedPlainLegendre,
    polynomialPairIntegral_C_mul_left,
    polynomialPairIntegral_C_mul_right,
    plainLegendre_pair_self]
  have hnonneg : 0 ≤ (2 * (n : ℝ) + 1) / 2 := by positivity
  rw [← mul_assoc, ← pow_two, Real.sq_sqrt hnonneg]
  field_simp

theorem normalizedPlainLegendre_pairwise_orthogonal
    {m n : ℕ} (hmn : m ≠ n) :
    polynomialPairIntegral
        (normalizedPlainLegendre m)
        (normalizedPlainLegendre n) (-1) 1 = 0 := by
  rw [normalizedPlainLegendre, normalizedPlainLegendre,
    polynomialPairIntegral_C_mul_left,
    polynomialPairIntegral_C_mul_right,
    plainLegendre_pairwise_orthogonal hmn,
    mul_zero, mul_zero]

/-- Kronecker-delta form of orthonormality. -/
theorem normalizedPlainLegendre_orthonormal (m n : ℕ) :
    polynomialPairIntegral
        (normalizedPlainLegendre m)
        (normalizedPlainLegendre n) (-1) 1 =
      if m = n then 1 else 0 := by
  split_ifs with h
  · subst n
    exact normalizedPlainLegendre_pair_self m
  · exact normalizedPlainLegendre_pairwise_orthogonal h

end LegendreOrthogonality
