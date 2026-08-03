/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import IntervalFourierL2
import Mathlib.Analysis.Real.Pi.Leibniz

/-!
# The normalized `L = 7/4` Legendre band ledger

This file applies the general band-integrated Legendre estimate at
`(a,b,m) = (7/16,50,48)` and checks the exact rational bound
`rho < 81 / 10^23` in the Lean kernel.  The normalization is explicitly
`dz / (2*pi)`; no appeal to a numerical value of `pi` or to a trusted
floating-point evaluator is made.

The elementary lower bound `3.14 < pi` is obtained from a finite lower
partial sum of the kernel-checked Leibniz series.
-/

namespace FullInfLegendreLedger

open scoped ENNReal InnerProductSpace

/-- A rational lower bound on `pi`, proved from the Leibniz series. -/
theorem pi_gt_314 : (157 : ℝ) / 50 < Real.pi := by
  have hanti : Antitone (fun i : ℕ ↦ (2 * (i : ℝ) + 1)⁻¹) := by
    intro i j hij
    apply inv_anti₀
    · positivity
    · have hijR : (i : ℝ) ≤ j := by exact_mod_cast hij
      linarith
  have hlower := hanti.alternating_series_le_tendsto
    Real.tendsto_sum_pi_div_four 700
  have hsum : (157 : ℝ) / 200 <
      ∑ i ∈ Finset.range (2 * 700),
        (-1 : ℝ) ^ i * (1 / (2 * i + 1)) := by
    norm_num [Finset.sum_range_succ]
  linarith

/-- The endpoint geometric ratio at `(a,b,m) = (7/16,50,48)`. -/
theorem p2_geometric_ratio_lt_one :
    (((7 : ℝ) / 16 * 50) ^ 2 /
      ((2 * (48 : ℝ) + 1) * (2 * (48 : ℝ) + 3))) < 1 := by
  norm_num

/-- Exact kernel-checked version of the `rho < 8.1e-22` endpoint ledger. -/
theorem p2_normalizedBandLeakageMajorant_lt :
    LegendrePlaneWaveBand.fourierNormalizedBandLeakageMajorant
        (7 / 16) 50 48 <
      (81 : ℝ) / 10 ^ 23 := by
  have hpi : (157 : ℝ) / 50 < Real.pi := pi_gt_314
  have hfactor :
      2 * ((7 : ℝ) / 16) * 50 / Real.pi < 4375 / 314 := by
    apply (div_lt_iff₀ Real.pi_pos).2
    nlinarith
  have htailpos :
      0 < LegendreTail.doubleFactorialMajorant
          (((7 : ℝ) / 16) * 50) 48 /
        (1 - (((7 : ℝ) / 16) * 50) ^ 2 /
          ((2 * (48 : ℝ) + 1) * (2 * (48 : ℝ) + 3))) := by
    have hq := p2_geometric_ratio_lt_one
    unfold LegendreTail.doubleFactorialMajorant
    positivity
  unfold LegendrePlaneWaveBand.fourierNormalizedBandLeakageMajorant
    LegendrePlaneWaveBand.bandLeakageMajorant
  change
    (50 / Real.pi) *
      (2 * ((7 : ℝ) / 16) *
        (LegendreTail.doubleFactorialMajorant
            (((7 : ℝ) / 16) * 50) 48 /
          (1 - (((7 : ℝ) / 16) * 50) ^ 2 /
            ((2 * (48 : ℝ) + 1) * (2 * (48 : ℝ) + 3))))) <
      (81 : ℝ) / 10 ^ 23
  rw [show
    (50 / Real.pi) *
        (2 * ((7 : ℝ) / 16) *
          (LegendreTail.doubleFactorialMajorant
              (((7 : ℝ) / 16) * 50) 48 /
            (1 - (((7 : ℝ) / 16) * 50) ^ 2 /
              ((2 * (48 : ℝ) + 1) * (2 * (48 : ℝ) + 3))))) =
    (2 * ((7 : ℝ) / 16) * 50 / Real.pi) *
      (LegendreTail.doubleFactorialMajorant
          (((7 : ℝ) / 16) * 50) 48 /
        (1 - (((7 : ℝ) / 16) * 50) ^ 2 /
          ((2 * (48 : ℝ) + 1) * (2 * (48 : ℝ) + 3)))) by ring]
  calc
    _ < (4375 / 314 : ℝ) *
        (LegendreTail.doubleFactorialMajorant
            (((7 : ℝ) / 16) * 50) 48 /
          (1 - (((7 : ℝ) / 16) * 50) ^ 2 /
            ((2 * (48 : ℝ) + 1) * (2 * (48 : ℝ) + 3)))) :=
      mul_lt_mul_of_pos_right hfactor htailpos
    _ < (81 : ℝ) / 10 ^ 23 := by
      unfold LegendreTail.doubleFactorialMajorant
      norm_num [Nat.doubleFactorial]

/-- The full normalized band-energy consequence at the `L = 7/4` endpoint.
This is the displayed F2 inequality with a rational `rho`; identifying the
coefficient with a chosen global Fourier transform and applying Plancherel
remain separate normalization steps. -/
theorem p2_normalized_planeWaveBandEnergy_le
    (w : LegendreScaledL2.IntervalL2 (7 / 16))
    (hw : w ∈
      (LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48)ᗮ) :
    LegendrePlaneWaveBand.fourierNormalizedPlaneWaveBandEnergy
        (7 / 16) w 50 ≤
      (81 / 10 ^ 23 : ℝ) * ‖w‖ ^ 2 := by
  have hband := LegendrePlaneWaveBand.fourierNormalizedPlaneWave_bandEnergy_le
    (7 / 16) (by norm_num) 50 (by norm_num) 48 w hw
      p2_geometric_ratio_lt_one
  calc
    LegendrePlaneWaveBand.fourierNormalizedPlaneWaveBandEnergy
        (7 / 16) w 50 ≤
        ‖w‖ ^ 2 *
          LegendrePlaneWaveBand.fourierNormalizedBandLeakageMajorant
            (7 / 16) 50 48 := hband
    _ ≤ ‖w‖ ^ 2 * (81 / 10 ^ 23 : ℝ) :=
      mul_le_mul_of_nonneg_left p2_normalizedBandLeakageMajorant_lt.le
        (sq_nonneg ‖w‖)
    _ = (81 / 10 ^ 23 : ℝ) * ‖w‖ ^ 2 := by ring

/-- The endpoint F2 statement for the genuine complex Bochner Fourier
coefficient on `[-7/16,7/16]`, integrated over `[-50,50]` with density
`dz/(2*pi)`. -/
theorem p2_normalizedIntervalFourierBandEnergy_le
    (w : LegendreScaledL2.IntervalL2 (7 / 16))
    (hw : w ∈
      (LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48)ᗮ) :
    IntervalFourierL2.normalizedIntervalFourierBandEnergy
        (7 / 16) w 50 ≤
      (81 / 10 ^ 23 : ℝ) * ‖w‖ ^ 2 := by
  have hband :=
    IntervalFourierL2.normalizedIntervalFourierBandEnergy_le_of_mem_orthogonal
      (7 / 16) (by norm_num) 50 (by norm_num) 48 w hw
        p2_geometric_ratio_lt_one
  calc
    IntervalFourierL2.normalizedIntervalFourierBandEnergy
        (7 / 16) w 50 ≤
        ‖w‖ ^ 2 *
          LegendrePlaneWaveBand.fourierNormalizedBandLeakageMajorant
            (7 / 16) 50 48 := hband
    _ ≤ ‖w‖ ^ 2 * (81 / 10 ^ 23 : ℝ) :=
      mul_le_mul_of_nonneg_left p2_normalizedBandLeakageMajorant_lt.le
        (sq_nonneg ‖w‖)
    _ = (81 / 10 ^ 23 : ℝ) * ‖w‖ ^ 2 := by ring

/-! ## Pole Taylor-competitor ledger -/

/-- The elementary degree-47 Taylor remainder majorant used for each of the
two pole vectors at `a = 7/16`. -/
noncomputable def p2PoleTaylorMajorant : ℝ :=
  Real.sqrt (7 / 8) * Real.exp (7 / 32) *
    (7 / 32) ^ 48 / Nat.factorial 48

/-- A tight rational upper bound on the only exponential occurring in the
pole ledger.  Subdivision into 64 equal pieces and
`exp x ≤ 1/(1-x)` keeps the proof wholly exact. -/
theorem exp_seven_div_32_lt :
    Real.exp (7 / 32) < (249 : ℝ) / 200 := by
  let x : ℝ := 7 / (32 * 64)
  have hx0 : 0 ≤ x := by norm_num [x]
  have hx1 : x < 1 := by norm_num [x]
  have hsmall := Real.exp_bound_div_one_sub_of_interval hx0 hx1
  have hpow : Real.exp x ^ 64 ≤ (1 / (1 - x)) ^ 64 := by
    exact pow_le_pow_left₀ (Real.exp_nonneg x) hsmall 64
  rw [← Real.exp_nat_mul] at hpow
  norm_num [x] at hpow
  exact hpow.trans_lt (by norm_num)

/-- Exact kernel-checked version of the per-sign pole residual ledger
`delta < 1.95e-93`.  The separate analytic Taylor-remainder-to-projection
argument is not asserted by this scalar theorem. -/
theorem p2PoleTaylorMajorant_lt :
    p2PoleTaylorMajorant < (195 : ℝ) / 10 ^ 95 := by
  have hsqrt : Real.sqrt (7 / 8) < (1871 : ℝ) / 2000 := by
    rw [Real.sqrt_lt] <;> norm_num
  have hexp := exp_seven_div_32_lt
  unfold p2PoleTaylorMajorant
  calc
    Real.sqrt (7 / 8) * Real.exp (7 / 32) *
          (7 / 32) ^ 48 / Nat.factorial 48 <
        ((1871 : ℝ) / 2000) * ((249 : ℝ) / 200) *
          (7 / 32) ^ 48 / Nat.factorial 48 := by
      gcongr
    _ < (195 : ℝ) / 10 ^ 95 := by
      norm_num [Nat.factorial]

end FullInfLegendreLedger
