/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2PanelEntry

/-!
# Rational scale-center approximation of the finite `p = 2` pole term

The pole Taylor coefficient contains the same square root as the spherical
component scale, divided by two.  Reusing the 48 checked scale centers avoids
a second generated square-root table.  The resulting product error is far
below the common `10⁻¹⁷` finite-pole budget.
-/

namespace RHP2Bridge

theorem p2PoleSqrt_eq_sphericalScale_div_two (n : ℕ) :
    Real.sqrt ((7 : ℝ) * (2 * n + 1) / 32) =
      p2LegendreSphericalScale n / 2 := by
  let x := Real.sqrt ((7 : ℝ) * (2 * n + 1) / 32)
  let y := p2LegendreSphericalScale n / 2
  have hx0 : 0 ≤ x := Real.sqrt_nonneg _
  have hy0 : 0 ≤ y := by
    dsimp [y]
    exact div_nonneg (p2LegendreSphericalScale_nonneg n) (by norm_num)
  have hx2 : x ^ 2 = (7 : ℝ) * (2 * n + 1) / 32 := by
    dsimp [x]
    rw [Real.sq_sqrt]
    have hn : (0 : ℝ) ≤ (n : ℝ) := by positivity
    positivity
  have hy2 : y ^ 2 = (7 : ℝ) * (2 * n + 1) / 32 := by
    dsimp [y]
    rw [div_pow, p2LegendreSphericalScale_sq]
    push_cast
    ring
  exact (sq_eq_sq₀ hx0 hy0).mp (hx2.trans hy2.symm)

theorem p2PoleTaylorPolynomialCoeff_eq_scale_mul_core (n : ℕ) :
    p2PoleTaylorPolynomialCoeff n =
      (p2LegendreSphericalScale n / 2) *
        p2PoleTaylorRationalCore n := by
  rw [p2PoleTaylorPolynomialCoeff_eq_sqrt_mul_core,
    p2PoleSqrt_eq_sphericalScale_div_two]

theorem abs_p2PoleTaylorRationalCore_le_eight (n : ℕ) :
    |p2PoleTaylorRationalCore n| ≤ 8 := by
  have hc := (abs_p2PoleTaylorPolynomialCoeff_lt_two n).le
  rw [p2PoleTaylorPolynomialCoeff_eq_scale_mul_core, abs_mul,
    abs_of_nonneg (div_nonneg (p2LegendreSphericalScale_nonneg n)
      (by norm_num))] at hc
  have hs := p2LegendreSphericalScale_ge_half n
  have hprod :
      0 ≤ (p2LegendreSphericalScale n / 2 - 1 / 4) *
        |p2PoleTaylorRationalCore n| := by
    apply mul_nonneg
    · linarith
    · exact abs_nonneg _
  nlinarith

noncomputable def p2PoleTaylorCoeffScaleCenter (n : Fin 48) : ℝ :=
  ((p2ScaleCenterQ n.val : ℚ) : ℝ) / 2 *
    p2PoleTaylorRationalCore n.val

theorem abs_p2PoleTaylorCoeff_sub_scaleCenter_le (n : Fin 48) :
    |p2PoleTaylorPolynomialCoeff n.val -
        p2PoleTaylorCoeffScaleCenter n| ≤ 1 / 10 ^ 19 := by
  rw [p2PoleTaylorPolynomialCoeff_eq_scale_mul_core]
  unfold p2PoleTaylorCoeffScaleCenter
  rw [show
      p2LegendreSphericalScale n.val / 2 *
          p2PoleTaylorRationalCore n.val -
        ((p2ScaleCenterQ n.val : ℚ) : ℝ) / 2 *
          p2PoleTaylorRationalCore n.val =
        ((p2LegendreSphericalScale n.val -
          ((p2ScaleCenterQ n.val : ℚ) : ℝ)) / 2) *
            p2PoleTaylorRationalCore n.val by ring,
    abs_mul, abs_div]
  have hs :
      |p2LegendreSphericalScale n.val -
        ((p2ScaleCenterQ n.val : ℚ) : ℝ)| ≤ 1 / 10 ^ 20 := by
    simpa [p2ScaleCenter] using
      (abs_p2LegendreSphericalScale_sub_center_lt n).le
  have hc := abs_p2PoleTaylorRationalCore_le_eight n.val
  rw [abs_of_nonneg (show (0 : ℝ) ≤ 2 by norm_num)]
  calc
    |p2LegendreSphericalScale n.val -
          ((p2ScaleCenterQ n.val : ℚ) : ℝ)| / 2 *
        |p2PoleTaylorRationalCore n.val| ≤
        ((1 / 10 ^ 20 : ℝ) / 2) * 8 := by
      exact mul_le_mul (div_le_div_of_nonneg_right hs (by norm_num)) hc
        (abs_nonneg _) (by positivity)
    _ ≤ 1 / 10 ^ 19 := by norm_num

theorem abs_p2PoleTaylorCoeffScaleCenter_le_three (n : Fin 48) :
    |p2PoleTaylorCoeffScaleCenter n| ≤ 3 := by
  have ha := (abs_p2PoleTaylorPolynomialCoeff_lt_two n.val).le
  have he := abs_p2PoleTaylorCoeff_sub_scaleCenter_le n
  calc
    |p2PoleTaylorCoeffScaleCenter n| =
        |p2PoleTaylorPolynomialCoeff n.val -
          (p2PoleTaylorPolynomialCoeff n.val -
            p2PoleTaylorCoeffScaleCenter n)| := by ring_nf
    _ ≤ |p2PoleTaylorPolynomialCoeff n.val| +
        |p2PoleTaylorPolynomialCoeff n.val -
          p2PoleTaylorCoeffScaleCenter n| := abs_sub _ _
    _ ≤ 2 + 1 / 10 ^ 19 := add_le_add ha he
    _ ≤ 3 := by norm_num

noncomputable def p2EntryTaylorPoleCenter (e : P2EntryIndex) : ℝ :=
  2 * p2PoleTaylorCoeffScaleCenter
      (p2EntryPoleMode e.block e.col) *
    p2PoleTaylorCoeffScaleCenter
      (p2EntryPoleMode e.block e.row)

theorem abs_p2TaylorPoleContribution_sub_entryCenter_le
    (e : P2EntryIndex) :
    |p2TaylorPoleContribution e - p2EntryTaylorPoleCenter e| ≤
      1 / 10 ^ 17 := by
  let i := p2EntryPoleMode e.block e.col
  let j := p2EntryPoleMode e.block e.row
  let ai := p2PoleTaylorPolynomialCoeff i.val
  let aj := p2PoleTaylorPolynomialCoeff j.val
  let qi := p2PoleTaylorCoeffScaleCenter i
  let qj := p2PoleTaylorCoeffScaleCenter j
  have hei : |ai - qi| ≤ 1 / 10 ^ 19 := by
    exact abs_p2PoleTaylorCoeff_sub_scaleCenter_le i
  have hej : |aj - qj| ≤ 1 / 10 ^ 19 := by
    exact abs_p2PoleTaylorCoeff_sub_scaleCenter_le j
  have haj : |aj| ≤ 2 :=
    (abs_p2PoleTaylorPolynomialCoeff_lt_two j.val).le
  have hqi : |qi| ≤ 3 := abs_p2PoleTaylorCoeffScaleCenter_le_three i
  unfold p2TaylorPoleContribution p2EntryTaylorPoleCenter
  change |2 * ai * aj - 2 * qi * qj| ≤ _
  calc
    |2 * ai * aj - 2 * qi * qj| =
        2 * |(ai - qi) * aj + qi * (aj - qj)| := by
      rw [show 2 * ai * aj - 2 * qi * qj =
        2 * ((ai - qi) * aj + qi * (aj - qj)) by ring, abs_mul]
      norm_num
    _ ≤ 2 * (|ai - qi| * |aj| + |qi| * |aj - qj|) := by
      gcongr
      simpa only [abs_mul] using abs_add_le
        ((ai - qi) * aj) (qi * (aj - qj))
    _ ≤ 2 * ((1 / 10 ^ 19) * 2 + 3 * (1 / 10 ^ 19)) := by
      gcongr
    _ ≤ 1 / 10 ^ 17 := by norm_num

/-- At this point a generated entry has exactly one remaining obligation:
an exact rational comparison of the finite panel/pole center with the stored
matrix center. -/
theorem abs_p2ScalarEntry_sub_storedCenter_le_of_rationalCenter
    (e : P2EntryIndex)
    (hround :
      |p2AlphaCenter * p2EntryDiagonalIndicator e +
          p2InvTwoPiCenter * (2 * p2EntryPanelSum e) +
          p2EntryPoleSign e.block * p2EntryTaylorPoleCenter e -
            p2StoredCenter e| ≤ 1 / 10 ^ 13) :
    |p2ScalarEntry e - p2StoredCenter e| ≤ p2StoredRadius := by
  exact abs_p2ScalarEntry_sub_storedCenter_le_of_panelCertificate
    e (p2EntryTaylorPoleCenter e)
    (abs_p2TaylorPoleContribution_sub_entryCenter_le e) hround

end RHP2Bridge
