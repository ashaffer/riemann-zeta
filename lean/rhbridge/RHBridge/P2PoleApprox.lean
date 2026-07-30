/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2Containment
import RHBridge.PolyEnclosure

/-!
# Finite polynomial enclosures for the p=2 pole coefficients

The positive pole coefficient of each normalized Legendre mode is an integral
against `exp (x/2)`.  This module replaces that exponential by its first
48 Taylor terms and proves a uniform error below `10⁻³⁰` for every
coefficient.  In particular this covers exactly the modes `0,...,47` in the
canonical endpoint.

The Taylor coefficient is expressed through `PolyEnclosure.exactIntegral`.
It is further factored into one explicit normalization square root times a
rational-polynomial core on `[-1,1]`.  The final transfer theorems accept any
generated rational enclosure of that expression.  At the matrix-entry level,
the analytic loss is below `10⁻²⁸`, far inside the stored `10⁻¹²` containment
radius.
-/

namespace RHP2Bridge

open scoped ENNReal InnerProductSpace RealInnerProductSpace

noncomputable def p2PoleTaylorPolynomialCoeff (n : ℕ) : ℝ :=
  PolyEnclosure.exactIntegral
    (LegendreScaled.scaledNormalizedPlainLegendre (7 / 16) n *
      PoleProjection.poleTaylorPolynomial 1 48)
    (-(7 / 16)) (7 / 16)

/-- Rational-polynomial core after rescaling the interval to `[-1,1]` and
factoring out the sole normalization square root. -/
noncomputable def p2PoleTaylorRationalCore (n : ℕ) : ℝ :=
  PolyEnclosure.exactIntegral
    ((PoleProjection.poleTaylorPolynomial 1 48).comp
        (Polynomial.C (7 / 16) * Polynomial.X) *
      LegendreRodrigues.plainLegendre n)
    (-1) 1

theorem p2PoleTaylorPolynomialCoeff_eq_sqrt_mul_core (n : ℕ) :
    p2PoleTaylorPolynomialCoeff n =
      Real.sqrt ((7 : ℝ) * (2 * n + 1) / 32) *
        p2PoleTaylorRationalCore n := by
  let a : ℝ := 7 / 16
  let b : ℝ := (2 * (n : ℝ) + 1) / 2
  let T : Polynomial ℝ := PoleProjection.poleTaylorPolynomial 1 48
  let P : Polynomial ℝ := LegendreRodrigues.plainLegendre n
  let f : ℝ → ℝ := fun x =>
    (LegendreScaled.scaledNormalizedPlainLegendre a n).eval x * T.eval x
  have ha : a ≠ 0 := by norm_num [a]
  have ha0 : 0 ≤ a := by norm_num [a]
  have hchange := intervalIntegral.integral_comp_mul_left f ha
    (a := (-1 : ℝ)) (b := 1)
  have hrescale : (∫ x in -a..a, f x) = a * ∫ t in (-1 : ℝ)..1, f (a * t) := by
    have hchange' :
        (∫ t in (-1 : ℝ)..1, f (a * t)) =
          a⁻¹ * ∫ x in -a..a, f x := by
      simpa using hchange
    rw [hchange']
    field_simp
  have hintegrand (t : ℝ) :
      f (a * t) =
        (Real.sqrt a)⁻¹ * Real.sqrt b *
          ((T.comp (Polynomial.C a * Polynomial.X) * P).eval t) := by
    dsimp [f, T, P]
    rw [LegendreScaled.eval_scaledNormalizedPlainLegendre]
    rw [show a * t / a = t by field_simp]
    unfold LegendreOrthogonality.normalizedPlainLegendre
    simp only [Polynomial.eval_mul, Polynomial.eval_C, Polynomial.eval_comp,
      Polynomial.eval_X]
    dsimp [b]
    ring
  have hint :
      (∫ t in (-1 : ℝ)..1, f (a * t)) =
        ((Real.sqrt a)⁻¹ * Real.sqrt b) *
          ∫ t in (-1 : ℝ)..1,
            (T.comp (Polynomial.C a * Polynomial.X) * P).eval t := by
    rw [← intervalIntegral.integral_const_mul]
    apply intervalIntegral.integral_congr
    intro t ht
    exact hintegrand t
  have hscale :
      a * ((Real.sqrt a)⁻¹ * Real.sqrt b) = Real.sqrt (a * b) := by
    rw [Real.sqrt_mul ha0]
    have hsqrt : Real.sqrt a ≠ 0 := (Real.sqrt_pos.2 (by norm_num [a])).ne'
    field_simp
    rw [Real.sq_sqrt ha0]
  unfold p2PoleTaylorPolynomialCoeff p2PoleTaylorRationalCore
  rw [← PolyEnclosure.integral_eval_eq_exactIntegral,
    ← PolyEnclosure.integral_eval_eq_exactIntegral]
  calc
    (∫ x in -(7 / 16)..7 / 16,
        (LegendreScaled.scaledNormalizedPlainLegendre (7 / 16) n *
          PoleProjection.poleTaylorPolynomial 1 48).eval x) =
        ∫ x in -a..a, f x := by
      apply intervalIntegral.integral_congr
      intro x hx
      dsimp [a, f, T]
      rw [Polynomial.eval_mul]
    _ = a * ∫ t in (-1 : ℝ)..1, f (a * t) := hrescale
    _ = a * (((Real.sqrt a)⁻¹ * Real.sqrt b) *
        ∫ t in (-1 : ℝ)..1,
          (T.comp (Polynomial.C a * Polynomial.X) * P).eval t) := by
      rw [hint]
    _ = Real.sqrt (a * b) *
        ∫ t in (-1 : ℝ)..1,
          (T.comp (Polynomial.C a * Polynomial.X) * P).eval t := by
      rw [← mul_assoc, hscale]
    _ = Real.sqrt ((7 : ℝ) * (2 * n + 1) / 32) *
        ∫ x in (-1 : ℝ)..1,
          ((PoleProjection.poleTaylorPolynomial 1 48).comp
              (Polynomial.C (7 / 16) * Polynomial.X) *
            LegendreRodrigues.plainLegendre n).eval x := by
      have hab : a * b = (7 : ℝ) * (2 * n + 1) / 32 := by
        dsimp [a, b]
        ring
      rw [hab]

theorem p2PoleTaylorPolynomialCoeff_eq_inner (n : ℕ) :
    p2PoleTaylorPolynomialCoeff n =
      inner ℝ (p2LegendreBasis n)
        (LegendreScaledL2.polynomialToL2 (7 / 16)
          (PoleProjection.poleTaylorPolynomial 1 48)) := by
  change p2PoleTaylorPolynomialCoeff n =
    inner ℝ
      (LegendreScaledL2.polynomialToL2 (7 / 16)
        (LegendreScaled.scaledNormalizedPlainLegendre (7 / 16) n))
      (LegendreScaledL2.polynomialToL2 (7 / 16)
        (PoleProjection.poleTaylorPolynomial 1 48))
  rw [LegendreScaledL2.inner_polynomialToL2 (7 / 16) (by norm_num)]
  unfold p2PoleTaylorPolynomialCoeff
  rw [← PolyEnclosure.integral_eval_eq_exactIntegral]
  unfold LegendreOrthogonality.polynomialPairIntegral
  apply intervalIntegral.integral_congr
  intro x hx
  change Polynomial.eval x
      (LegendreScaled.scaledNormalizedPlainLegendre (7 / 16) n *
        PoleProjection.poleTaylorPolynomial 1 48) = _
  rw [Polynomial.eval_mul]

theorem p2_polePlus_sub_taylor_norm_lt :
    ‖PoleProjection.polePlusL2 (7 / 16) -
        LegendreScaledL2.polynomialToL2 (7 / 16)
          (PoleProjection.poleTaylorPolynomial 1 48)‖ <
      (1 : ℝ) / 10 ^ 30 := by
  have hsq := PoleProjection.norm_poleL2_sub_taylor_sq_le
    (7 / 16) (by norm_num) (by norm_num) 1 (by norm_num) 48 (by norm_num)
  have hnorm : 0 ≤ ‖PoleProjection.poleL2 (7 / 16) 1 -
      LegendreScaledL2.polynomialToL2 (7 / 16)
        (PoleProjection.poleTaylorPolynomial 1 48)‖ := norm_nonneg _
  have hrat :
      (2 : ℝ) * (7 / 16) *
          ((7 / 16 / 2) ^ 48 *
            ((49 : ℝ) / (Nat.factorial 48 * 48 : ℝ))) ^ 2 <
        ((1 : ℝ) / 10 ^ 30) ^ 2 := by
    norm_num [Nat.factorial]
  unfold PoleProjection.polePlusL2
  nlinarith

theorem p2PoleCoeff_sub_taylorPolynomialCoeff_abs_lt (n : ℕ) :
    |p2PoleCoeff n - p2PoleTaylorPolynomialCoeff n| <
      (1 : ℝ) / 10 ^ 30 := by
  rw [p2PoleTaylorPolynomialCoeff_eq_inner]
  unfold p2PoleCoeff
  rw [← inner_sub_right]
  have hcs := abs_real_inner_le_norm
    (p2LegendreBasis n)
    (PoleProjection.polePlusL2 (7 / 16) -
      LegendreScaledL2.polynomialToL2 (7 / 16)
        (PoleProjection.poleTaylorPolynomial 1 48))
  have hnormBasis : ‖p2LegendreBasis n‖ = 1 :=
    (LegendreScaledL2.scaledNormalizedLegendreL2_orthonormal
      (7 / 16) (by norm_num)).norm_eq_one n
  rw [hnormBasis, one_mul] at hcs
  exact hcs.trans_lt p2_polePlus_sub_taylor_norm_lt

/-- A generated rational enclosure of the finite polynomial coefficient
transfers to the actual exponential coefficient with only `10^-30` loss. -/
theorem p2PoleCoeff_sub_rational_abs_lt_of_taylor_enclosure
    (n : Fin 48) (q e : ℝ)
    (hfinite : |p2PoleTaylorPolynomialCoeff n.val - q| ≤ e) :
    |p2PoleCoeff n.val - q| <
      (1 : ℝ) / 10 ^ 30 + e := by
  rw [show p2PoleCoeff n.val - q =
      (p2PoleCoeff n.val - p2PoleTaylorPolynomialCoeff n.val) +
        (p2PoleTaylorPolynomialCoeff n.val - q) by ring]
  exact (abs_add_le _ _).trans_lt
    (add_lt_add_of_lt_of_le
      (p2PoleCoeff_sub_taylorPolynomialCoeff_abs_lt n.val) hfinite)

theorem abs_p2PoleCoeff_le_one (n : ℕ) :
    |p2PoleCoeff n| ≤ 1 := by
  unfold p2PoleCoeff
  calc
    |inner ℝ (p2LegendreBasis n)
        (PoleProjection.polePlusL2 (7 / 16))| ≤
        ‖p2LegendreBasis n‖ *
          ‖PoleProjection.polePlusL2 (7 / 16)‖ :=
      abs_real_inner_le_norm _ _
    _ ≤ 1 := by
      rw [(LegendreScaledL2.scaledNormalizedLegendreL2_orthonormal
        (7 / 16) (by norm_num)).norm_eq_one n, one_mul]
      exact PoleProjection.p2_polePlusL2_norm_le_one

theorem abs_p2PoleTaylorPolynomialCoeff_lt_two (n : ℕ) :
    |p2PoleTaylorPolynomialCoeff n| < 2 := by
  have herr := p2PoleCoeff_sub_taylorPolynomialCoeff_abs_lt n
  have hc := abs_p2PoleCoeff_le_one n
  calc
    |p2PoleTaylorPolynomialCoeff n| =
        |p2PoleCoeff n -
          (p2PoleCoeff n - p2PoleTaylorPolynomialCoeff n)| := by ring_nf
    _ ≤ |p2PoleCoeff n| +
        |p2PoleCoeff n - p2PoleTaylorPolynomialCoeff n| :=
      abs_sub _ _
    _ < 1 + (1 : ℝ) / 10 ^ 30 := add_lt_add_of_le_of_lt hc herr
    _ < 2 := by norm_num

theorem p2PoleEntry_sub_taylorPolynomialEntry_abs_lt (i j : Fin 48) :
    |2 * p2PoleCoeff i.val * p2PoleCoeff j.val -
        2 * p2PoleTaylorPolynomialCoeff i.val *
          p2PoleTaylorPolynomialCoeff j.val| <
      (1 : ℝ) / 10 ^ 28 := by
  let ci := p2PoleCoeff i.val
  let cj := p2PoleCoeff j.val
  let ai := p2PoleTaylorPolynomialCoeff i.val
  let aj := p2PoleTaylorPolynomialCoeff j.val
  have hei : |ci - ai| ≤ (1 : ℝ) / 10 ^ 30 :=
    (p2PoleCoeff_sub_taylorPolynomialCoeff_abs_lt i.val).le
  have hej : |cj - aj| ≤ (1 : ℝ) / 10 ^ 30 :=
    (p2PoleCoeff_sub_taylorPolynomialCoeff_abs_lt j.val).le
  have hcj : |cj| ≤ 1 := abs_p2PoleCoeff_le_one j.val
  have hai : |ai| ≤ 2 := (abs_p2PoleTaylorPolynomialCoeff_lt_two i.val).le
  change |2 * ci * cj - 2 * ai * aj| < _
  rw [show 2 * ci * cj - 2 * ai * aj =
      2 * ((ci - ai) * cj + ai * (cj - aj)) by ring]
  calc
    |2 * ((ci - ai) * cj + ai * (cj - aj))| =
        2 * |(ci - ai) * cj + ai * (cj - aj)| := by norm_num
    _ ≤ 2 * (|(ci - ai) * cj| + |ai * (cj - aj)|) := by
      gcongr
      exact abs_add_le _ _
    _ = 2 * (|ci - ai| * |cj| + |ai| * |cj - aj|) := by
      rw [abs_mul, abs_mul]
    _ ≤ 2 * (((1 : ℝ) / 10 ^ 30) * 1 +
        2 * ((1 : ℝ) / 10 ^ 30)) := by gcongr
    _ < (1 : ℝ) / 10 ^ 28 := by norm_num

/-- Entry-level transfer: after checking only the finite polynomial product,
the true rank-two pole entry loses less than `10^-28`. -/
theorem p2PoleEntry_sub_rational_abs_lt_of_taylor_enclosure
    (i j : Fin 48) (q e : ℝ)
    (hfinite :
      |2 * p2PoleTaylorPolynomialCoeff i.val *
          p2PoleTaylorPolynomialCoeff j.val - q| ≤ e) :
    |2 * p2PoleCoeff i.val * p2PoleCoeff j.val - q| <
      (1 : ℝ) / 10 ^ 28 + e := by
  rw [show 2 * p2PoleCoeff i.val * p2PoleCoeff j.val - q =
      (2 * p2PoleCoeff i.val * p2PoleCoeff j.val -
        2 * p2PoleTaylorPolynomialCoeff i.val *
          p2PoleTaylorPolynomialCoeff j.val) +
      (2 * p2PoleTaylorPolynomialCoeff i.val *
        p2PoleTaylorPolynomialCoeff j.val - q) by ring]
  exact (abs_add_le _ _).trans_lt
    (add_lt_add_of_lt_of_le
      (p2PoleEntry_sub_taylorPolynomialEntry_abs_lt i j) hfinite)

end RHP2Bridge
