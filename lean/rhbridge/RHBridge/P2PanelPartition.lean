/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2PanelComposition

/-!
# The fixed 32-panel partition for the canonical `p = 2` certificate

The generated certificate uses one immutable rational partition of `[0,50]`.
This file checks all geometric side conditions and reduces every local
analytic error to one common rational budget.  It contains no numerical
quadrature: the only finite checks are normalization of explicit rationals.
-/

namespace RHP2Bridge

open scoped BigOperators

/-- Rational endpoints of the canonical positive-half partition. -/
def p2PanelEndpointQ : ℕ → ℚ
  | 0 => 0
  | 1 => 1 / 4
  | 2 => 5 / 16
  | 3 => 3 / 8
  | 4 => 7 / 16
  | 5 => 1 / 2
  | 6 => 5 / 8
  | 7 => 3 / 4
  | 8 => 7 / 8
  | 9 => 1
  | 10 => 5 / 4
  | 11 => 3 / 2
  | 12 => 7 / 4
  | 13 => 2
  | 14 => 5 / 2
  | 15 => 3
  | 16 => 7 / 2
  | 17 => 4
  | 18 => 5
  | 19 => 6
  | 20 => 7
  | 21 => 8
  | 22 => 10
  | 23 => 12
  | 24 => 14
  | 25 => 16
  | 26 => 20
  | 27 => 24
  | 28 => 28
  | 29 => 32
  | 30 => 38
  | 31 => 44
  | 32 => 50
  | _ => 50

/-- Rational center of panel `k`. -/
def p2PanelCenterQ (k : ℕ) : ℚ :=
  (p2PanelEndpointQ k + p2PanelEndpointQ (k + 1)) / 2

/-- Rational half-width of panel `k`. -/
def p2PanelHalfWidthQ (k : ℕ) : ℚ :=
  (p2PanelEndpointQ (k + 1) - p2PanelEndpointQ k) / 2

noncomputable def p2PanelEndpoint (k : ℕ) : ℝ :=
  (p2PanelEndpointQ k : ℝ)

noncomputable def p2PanelCenter (k : ℕ) : ℝ :=
  (p2PanelCenterQ k : ℝ)

noncomputable def p2PanelHalfWidth (k : ℕ) : ℝ :=
  (p2PanelHalfWidthQ k : ℝ)

theorem p2Panel_center_sub_halfWidth (k : Fin 32) :
    p2PanelCenter k.val - p2PanelHalfWidth k.val =
      p2PanelEndpoint k.val := by
  norm_num [p2PanelCenter, p2PanelHalfWidth, p2PanelEndpoint,
    p2PanelCenterQ, p2PanelHalfWidthQ]
  ring

theorem p2Panel_center_add_halfWidth (k : Fin 32) :
    p2PanelCenter k.val + p2PanelHalfWidth k.val =
      p2PanelEndpoint (k.val + 1) := by
  norm_num [p2PanelCenter, p2PanelHalfWidth, p2PanelEndpoint,
    p2PanelCenterQ, p2PanelHalfWidthQ]
  ring

theorem p2PanelHalfWidth_nonneg (k : Fin 32) :
    0 ≤ p2PanelHalfWidth k.val := by
  fin_cases k <;>
    norm_num [p2PanelHalfWidth, p2PanelHalfWidthQ, p2PanelEndpointQ]

theorem p2PanelCenter_nonneg (k : Fin 32) :
    0 ≤ p2PanelCenter k.val := by
  fin_cases k <;>
    norm_num [p2PanelCenter, p2PanelCenterQ, p2PanelEndpointQ]

theorem p2Panel_band (k : Fin 32) :
    |p2PanelCenter k.val| + p2PanelHalfWidth k.val ≤ 50 := by
  fin_cases k <;>
    norm_num [p2PanelCenter, p2PanelHalfWidth,
      p2PanelCenterQ, p2PanelHalfWidthQ, p2PanelEndpointQ]

/-- The quadratic perturbation of every reciprocal denominator stays below
`1/4`; this is stronger than the `< 1` hypothesis used by the panel lemma. -/
theorem p2Panel_prefixRho_le_quarter (k : Fin 32) :
    prefixDenominatorRho 0 (p2PanelCenter k.val)
        (p2PanelHalfWidth k.val) ≤ 1 / 4 := by
  fin_cases k <;>
    norm_num [prefixDenominatorRho, prefixDenominatorBase, prefixA,
      p2PanelCenter, p2PanelHalfWidth, p2PanelCenterQ,
      p2PanelHalfWidthQ, p2PanelEndpointQ, abs_of_nonneg]

theorem p2Panel_prefixRho_lt_one (k : Fin 32) :
    prefixDenominatorRho 0 (p2PanelCenter k.val)
        (p2PanelHalfWidth k.val) < 1 :=
  (p2Panel_prefixRho_le_quarter k).trans_lt (by norm_num)

private theorem quarterPrefixTermError_le_1e18
    (n : ℕ) (c h : ℝ) (hh : 0 ≤ h)
    (hrho : prefixDenominatorRho 0 c h ≤ 1 / 4) :
    quarterPrefixTermError n c h 32 ≤ 1 / 10 ^ 18 := by
  have ha : (1 / 4 : ℝ) ≤ prefixA n := by
    unfold prefixA
    have hn : (0 : ℝ) ≤ (n : ℝ) := by positivity
    linarith
  have ha0 : 0 < prefixA n := lt_of_lt_of_le (by norm_num) ha
  have hD0 : 0 < prefixDenominatorBase n c :=
    prefixDenominatorBase_pos n c
  have hcoef :
      |prefixA n| * |(prefixDenominatorBase n c)⁻¹| ≤ 4 := by
    rw [abs_of_pos ha0, abs_inv, abs_of_pos hD0, ← div_eq_mul_inv]
    apply (div_le_iff₀ hD0).2
    have hDsq : (prefixA n) ^ 2 ≤ prefixDenominatorBase n c := by
      unfold prefixDenominatorBase
      nlinarith [sq_nonneg (c / 2)]
    nlinarith
  have hr0 : 0 ≤ prefixDenominatorRho n c h := by
    unfold prefixDenominatorRho
    positivity
  have hr : prefixDenominatorRho n c h ≤ 1 / 4 :=
    (prefixDenominatorRho_le_zero n c h hh).trans hrho
  have hden : 0 < 1 - prefixDenominatorRho n c h := by
    linarith
  have hpow :
      (prefixDenominatorRho n c h) ^ 32 ≤ (1 / 4 : ℝ) ^ 32 :=
    pow_le_pow_left₀ hr0 hr 32
  have hratio :
      (prefixDenominatorRho n c h) ^ 32 /
          (1 - prefixDenominatorRho n c h) ≤ 1 / (4 * 10 ^ 18) := by
    calc
      (prefixDenominatorRho n c h) ^ 32 /
          (1 - prefixDenominatorRho n c h) ≤
          (1 / 4 : ℝ) ^ 32 /
            (1 - prefixDenominatorRho n c h) := by
        exact div_le_div_of_nonneg_right hpow hden.le
      _ ≤ (1 / 4 : ℝ) ^ 32 / (3 / 4) := by
        apply div_le_div_of_nonneg_left (by positivity) (by norm_num)
        linarith
      _ ≤ 1 / (4 * 10 ^ 18) := by norm_num
  unfold quarterPrefixTermError
  rw [← mul_assoc]
  calc
    |prefixA n| * |(prefixDenominatorBase n c)⁻¹| *
        ((prefixDenominatorRho n c h) ^ 32 /
          (1 - prefixDenominatorRho n c h)) ≤
        4 * (1 / (4 * 10 ^ 18)) := by
      exact mul_le_mul hcoef hratio (by positivity) (by positivity)
    _ = 1 / 10 ^ 18 := by norm_num

/-- A deliberately simple common bound for all 64 reciprocal remainders on
all 32 panels.  The actual worst value is much smaller, but this bound already
leaves more than half of the stored matrix radius unused. -/
theorem p2Panel_prefixError_le (k : Fin 32) :
    quarterDifferenceFinitePrefixError
        (p2PanelCenter k.val) (p2PanelHalfWidth k.val) 32 ≤
      1 / 10 ^ 16 := by
  unfold quarterDifferenceFinitePrefixError
  calc
    (∑ n ∈ Finset.range 64,
        quarterPrefixTermError n (p2PanelCenter k.val)
          (p2PanelHalfWidth k.val) 32) ≤
        ∑ n ∈ Finset.range 64, (1 / 10 ^ 18 : ℝ) := by
      apply Finset.sum_le_sum
      intro n hn
      exact quarterPrefixTermError_le_1e18 n _ _
        (p2PanelHalfWidth_nonneg k) (p2Panel_prefixRho_le_quarter k)
    _ ≤ 1 / 10 ^ 16 := by norm_num

noncomputable def p2PanelDefectErrorBound : ℝ := 21 / 10 ^ 15
noncomputable def p2PanelComponentErrorBound : ℝ := 2 / 10 ^ 18
noncomputable def p2PanelPairErrorBound : ℝ := 5 / 10 ^ 18
noncomputable def p2PanelIntegrandErrorBound : ℝ := 22 / 10 ^ 15
noncomputable def p2PositiveHalfBandErrorBound : ℝ := 11 / 10 ^ 13

theorem p2Panel_defectError_le (k : Fin 32) :
    p2DefectPanelError (p2PanelCenter k.val)
        (p2PanelHalfWidth k.val) 32 ≤ p2PanelDefectErrorBound := by
  unfold p2DefectPanelError p2PanelDefectErrorBound
  linarith [p2Panel_prefixError_le k]

theorem abs_p2SelectedScaleCenterQ_le_ten
    (kind : P2SelectedKind) (k : Fin 24) :
    |(p2SelectedScaleCenterQ kind k : ℝ)| ≤ 10 := by
  cases kind <;> fin_cases k <;>
    norm_num [p2SelectedScaleCenterQ, p2SelectedDegree, p2ScaleCenterQ]

theorem p2Panel_componentError_le
    (kind : P2SelectedKind) (k : Fin 24) :
    p2SelectedComponent100ScaleCenterError kind k ≤
      p2PanelComponentErrorBound := by
  have hq := abs_p2SelectedScaleCenterQ_le_ten kind k
  unfold p2SelectedComponent100ScaleCenterError
    p2SelectedComponent100PanelError p2SelectedSphericalPanelError
    p2Spherical100Error p2PanelComponentErrorBound
  norm_num at hq ⊢
  nlinarith

private theorem p2Panel_pairError_le
    (kind : P2SelectedKind) (i j : Fin 24) :
    panelPairError
        (p2SelectedComponent100ScaleCenterError kind j)
        (p2SelectedComponent100ScaleCenterError kind i)
        (1 + p2SelectedComponent100ScaleCenterError kind j)
        (1 + p2SelectedComponent100ScaleCenterError kind i) ≤
      p2PanelPairErrorBound := by
  have hi := p2Panel_componentError_le kind i
  have hj := p2Panel_componentError_le kind j
  have hi0 := p2SelectedComponent100ScaleCenterError_nonneg kind i
  have hj0 := p2SelectedComponent100ScaleCenterError_nonneg kind j
  have hC0 : 0 ≤ p2PanelComponentErrorBound := by
    norm_num [p2PanelComponentErrorBound]
  unfold panelPairError p2PanelPairErrorBound
  calc
    _ ≤ p2PanelComponentErrorBound * p2PanelComponentErrorBound +
        p2PanelComponentErrorBound * (1 + p2PanelComponentErrorBound) +
        (1 + p2PanelComponentErrorBound) * p2PanelComponentErrorBound := by
      apply add_le_add
      · apply add_le_add
        · exact mul_le_mul hj hi hi0 hC0
        · exact mul_le_mul hj (add_le_add_right hi 1)
            (by positivity) hC0
      · exact mul_le_mul (add_le_add_right hj 1) hi hi0 (by positivity)
    _ ≤ 5 / 10 ^ 18 := by
      norm_num [p2PanelComponentErrorBound]

theorem p2Panel_integrandError_le
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) :
    p2ScaleCenteredPanelIntegrandError kind i j
        (p2PanelCenter k.val) (p2PanelHalfWidth k.val) 32 ≤
      p2PanelIntegrandErrorBound := by
  let ed := p2DefectPanelError (p2PanelCenter k.val)
    (p2PanelHalfWidth k.val) 32
  let ei := p2SelectedComponent100ScaleCenterError kind i
  let ej := p2SelectedComponent100ScaleCenterError kind j
  have hed := p2Panel_defectError_le k
  have hei := p2Panel_componentError_le kind i
  have hej := p2Panel_componentError_le kind j
  have hed0 := p2DefectPanelError_nonneg
    (p2PanelCenter k.val) (p2PanelHalfWidth k.val) 32
    (p2PanelHalfWidth_nonneg k) (p2Panel_band k)
    (p2Panel_prefixRho_lt_one k)
  have hei0 := p2SelectedComponent100ScaleCenterError_nonneg kind i
  have hej0 := p2SelectedComponent100ScaleCenterError_nonneg kind j
  have hpair := p2Panel_pairError_le kind i j
  have hpair0 : 0 ≤ panelPairError ej ei (1 + ej) (1 + ei) := by
    dsimp [ei, ej]
    unfold panelPairError
    positivity
  have hD0 : 0 ≤ p2PanelDefectErrorBound := by
    norm_num [p2PanelDefectErrorBound]
  have hC0 : 0 ≤ p2PanelComponentErrorBound := by
    norm_num [p2PanelComponentErrorBound]
  have hP0 : 0 ≤ p2PanelPairErrorBound := by
    norm_num [p2PanelPairErrorBound]
  unfold p2ScaleCenteredPanelIntegrandError
    p2CanonicalPanelIntegrandError panelTripleError
  change ed * panelPairError ej ei (1 + ej) (1 + ei) +
      ed * ((1 + ej) * (1 + ei)) +
      (7447 / 1000 + ed) * panelPairError ej ei (1 + ej) (1 + ei) ≤ _
  calc
    _ ≤ p2PanelDefectErrorBound * p2PanelPairErrorBound +
        p2PanelDefectErrorBound *
          ((1 + p2PanelComponentErrorBound) *
            (1 + p2PanelComponentErrorBound)) +
        (7447 / 1000 + p2PanelDefectErrorBound) *
          p2PanelPairErrorBound := by
      gcongr
    _ ≤ p2PanelIntegrandErrorBound := by
      norm_num [p2PanelDefectErrorBound, p2PanelComponentErrorBound,
        p2PanelPairErrorBound, p2PanelIntegrandErrorBound]

theorem p2Panel_totalWidth :
    ∑ k ∈ Finset.range 32, 2 * p2PanelHalfWidth k = 50 := by
  norm_num [p2PanelHalfWidth, p2PanelHalfWidthQ, p2PanelEndpointQ,
    Finset.sum_range_succ]

theorem abs_p2SelectedBandIntegrand_le
    (kind : P2SelectedKind) (i j : ℕ) {r : ℝ} (hr : |r| ≤ 50) :
    |p2SelectedBandIntegrand kind i j r| ≤ 7447 / 1000 := by
  have hd := GlideKernel.p2Omega_sub_alpha_abs_le hr
  have hi := abs_p2SelectedComponent_le_one kind i r
  have hj := abs_p2SelectedComponent_le_one kind j r
  unfold p2SelectedBandIntegrand
  rw [abs_mul, abs_mul]
  calc
    |GlideKernel.p2Omega r - GlideKernel.p2Alpha| *
        (|p2SelectedComponent kind j r| *
          |p2SelectedComponent kind i r|) ≤
        (7447 / 1000) * (1 * 1) := by
      exact mul_le_mul hd (mul_le_mul hj hi (abs_nonneg _) (by norm_num))
        (mul_nonneg (abs_nonneg _) (abs_nonneg _)) (by norm_num)
    _ = 7447 / 1000 := by ring

theorem abs_integral_p2SelectedBandIntegrand_le
    (kind : P2SelectedKind) (i j : ℕ) :
    |∫ r in (0 : ℝ)..50, p2SelectedBandIntegrand kind i j r| ≤
      7447 / 20 := by
  have h := intervalIntegral.norm_integral_le_of_norm_le_const
    (f := p2SelectedBandIntegrand kind i j)
    (C := (7447 : ℝ) / 1000) (a := (0 : ℝ)) (b := 50) (by
      intro r hr
      rw [Real.norm_eq_abs]
      apply abs_p2SelectedBandIntegrand_le
      rw [Set.uIoc_of_le (by norm_num)] at hr
      rw [abs_of_nonneg hr.1.le]
      exact hr.2)
  rw [Real.norm_eq_abs] at h
  convert h using 1 <;> norm_num

/-- Uniform analytic enclosure of a selected positive-half band integral by
the sum of its 32 exact rational-polynomial panel integrals. -/
theorem integral_p2SelectedBandIntegrand_sub_panelSum_le
    (kind : P2SelectedKind) (i j : Fin 24) :
    |(∫ r in (0 : ℝ)..50, p2SelectedBandIntegrand kind i.val j.val r) -
        ∑ k ∈ Finset.range 32,
          PolyEnclosure.exactIntegral
            (p2ScaleCenteredPanelIntegrandPolynomial kind i j
              (p2PanelCenter k) 32)
            (-p2PanelHalfWidth k) (p2PanelHalfWidth k)| ≤
      p2PositiveHalfBandErrorBound := by
  have hagg := PolyEnclosure.integral_partition_sub_sum_exactIntegral_le
    (p2SelectedBandIntegrand kind i.val j.val)
    p2PanelEndpoint p2PanelCenter p2PanelHalfWidth
    (fun k => p2ScaleCenteredPanelIntegrandError kind i j
      (p2PanelCenter k) (p2PanelHalfWidth k) 32)
    (fun k => p2ScaleCenteredPanelIntegrandPolynomial kind i j
      (p2PanelCenter k) 32)
    32 (continuous_p2SelectedBandIntegrand kind i.val j.val)
    (by
      intro k hk
      exact p2PanelHalfWidth_nonneg ⟨k, Finset.mem_range.mp hk⟩)
    (by
      intro k hk
      let k' : Fin 32 := ⟨k, Finset.mem_range.mp hk⟩
      exact ⟨p2Panel_center_sub_halfWidth k',
        p2Panel_center_add_halfWidth k'⟩)
    (by
      intro k hk
      let k' : Fin 32 := ⟨k, Finset.mem_range.mp hk⟩
      exact p2ScaleCenteredPanelIntegrand_centeredEncloses
        kind i j (p2PanelCenter k) (p2PanelHalfWidth k) 32
        (p2PanelHalfWidth_nonneg k') (p2Panel_band k')
        (p2Panel_prefixRho_lt_one k'))
  have hagg' :
      |(∫ r in (0 : ℝ)..50,
          p2SelectedBandIntegrand kind i.val j.val r) -
          ∑ k ∈ Finset.range 32,
            PolyEnclosure.exactIntegral
              (p2ScaleCenteredPanelIntegrandPolynomial kind i j
                (p2PanelCenter k) 32)
              (-p2PanelHalfWidth k) (p2PanelHalfWidth k)| ≤
        ∑ k ∈ Finset.range 32,
          2 * p2PanelHalfWidth k *
            p2ScaleCenteredPanelIntegrandError kind i j
              (p2PanelCenter k) (p2PanelHalfWidth k) 32 := by
    simpa [p2PanelEndpoint, p2PanelEndpointQ] using hagg
  calc
    _ ≤ ∑ k ∈ Finset.range 32,
        2 * p2PanelHalfWidth k *
          p2ScaleCenteredPanelIntegrandError kind i j
            (p2PanelCenter k) (p2PanelHalfWidth k) 32 := hagg'
    _ ≤ ∑ k ∈ Finset.range 32,
        2 * p2PanelHalfWidth k * p2PanelIntegrandErrorBound := by
      apply Finset.sum_le_sum
      intro k hk
      let k' : Fin 32 := ⟨k, Finset.mem_range.mp hk⟩
      have herr := p2Panel_integrandError_le kind i j k'
      have hwidth := p2PanelHalfWidth_nonneg k'
      simpa [k'] using mul_le_mul_of_nonneg_left herr
        (mul_nonneg (show (0 : ℝ) ≤ 2 by norm_num) hwidth)
    _ = p2PositiveHalfBandErrorBound := by
      rw [← Finset.sum_mul, p2Panel_totalWidth]
      norm_num [p2PanelIntegrandErrorBound,
        p2PositiveHalfBandErrorBound]

/-- The exact rational-polynomial panel sum has a small universal magnitude
bound, so the normalization-constant error never needs a generated bound. -/
theorem abs_p2SelectedBandPanelSum_le
    (kind : P2SelectedKind) (i j : Fin 24) :
    |∑ k ∈ Finset.range 32,
        PolyEnclosure.exactIntegral
          (p2ScaleCenteredPanelIntegrandPolynomial kind i j
            (p2PanelCenter k) 32)
          (-p2PanelHalfWidth k) (p2PanelHalfWidth k)| ≤ 373 := by
  let I : ℝ :=
    ∫ r in (0 : ℝ)..50, p2SelectedBandIntegrand kind i.val j.val r
  let R : ℝ :=
    ∑ k ∈ Finset.range 32,
      PolyEnclosure.exactIntegral
        (p2ScaleCenteredPanelIntegrandPolynomial kind i j
          (p2PanelCenter k) 32)
        (-p2PanelHalfWidth k) (p2PanelHalfWidth k)
  have hI : |I| ≤ 7447 / 20 := by
    exact abs_integral_p2SelectedBandIntegrand_le kind i.val j.val
  have hIR : |I - R| ≤ p2PositiveHalfBandErrorBound := by
    exact integral_p2SelectedBandIntegrand_sub_panelSum_le kind i j
  change |R| ≤ 373
  calc
    |R| = |I - (I - R)| := by ring_nf
    _ ≤ |I| + |I - R| := abs_sub _ _
    _ ≤ 7447 / 20 + p2PositiveHalfBandErrorBound := add_le_add hI hIR
    _ ≤ 373 := by norm_num [p2PositiveHalfBandErrorBound]

end RHP2Bridge
