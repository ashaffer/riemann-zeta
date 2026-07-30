/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Glide.DigammaSeries

/-!
# Locally uniform convergence of Euler's Gamma approximants

This file upgrades mathlib's pointwise theorem `Complex.GammaSeq_tendsto_Gamma`
to locally uniform convergence on the positive-real half-plane.  The proof uses
Euler's integral representation and dominated convergence along the product
filter `atTop ×ˢ 𝓝 z`.  A two-exponent majorant controls the integrand uniformly
near both zero and infinity.
-/

open Filter MeasureTheory Set
open scoped Topology

namespace GlideKernel

private noncomputable def approxGammaKernel (n : ℕ) (z : ℂ) (x : ℝ) : ℂ :=
  indicator (Ioc 0 (n : ℝ))
    (fun x : ℝ => ((1 - x / n) ^ n : ℝ) * (x : ℂ) ^ (z - 1)) x

private lemma integrable_approxGammaKernel (n : ℕ) {z : ℂ} (hz : 0 < z.re) :
    Integrable (approxGammaKernel n z) (volume.restrict (Ioi 0)) := by
  change Integrable
    (indicator (Ioc 0 (n : ℝ))
      (fun x : ℝ => ((1 - x / n) ^ n : ℝ) * (x : ℂ) ^ (z - 1)))
    (volume.restrict (Ioi 0))
  rw [integrable_indicator_iff (measurableSet_Ioc : MeasurableSet (Ioc (_ : ℝ) _)),
    IntegrableOn, Measure.restrict_restrict_of_subset Ioc_subset_Ioi_self, ← IntegrableOn,
    ← intervalIntegrable_iff_integrableOn_Ioc_of_le (by positivity : (0 : ℝ) ≤ n)]
  apply IntervalIntegrable.continuousOn_mul
  · refine intervalIntegral.intervalIntegrable_cpow' ?_
    rwa [Complex.sub_re, Complex.one_re, ← zero_sub, sub_lt_sub_iff_right]
  · fun_prop

private lemma integral_approxGammaKernel (n : ℕ) (z : ℂ) :
    ∫ x, approxGammaKernel n z x ∂volume.restrict (Ioi 0) =
      ∫ x : ℝ in 0..n, ((1 - x / n) ^ n : ℝ) * (x : ℂ) ^ (z - 1) := by
  change (∫ x : ℝ in Ioi 0, indicator (Ioc 0 (n : ℝ))
    (fun x : ℝ => ((1 - x / n) ^ n : ℝ) * (x : ℂ) ^ (z - 1)) x) = _
  rw [MeasureTheory.integral_indicator (measurableSet_Ioc : MeasurableSet (Ioc (_ : ℝ) _)),
    intervalIntegral.integral_of_le (by positivity : 0 ≤ (n : ℝ)),
    Measure.restrict_restrict_of_subset Ioc_subset_Ioi_self]

private noncomputable def gammaMajorant (a b : ℝ) : ℝ → ℝ :=
  (fun x : ℝ => Real.exp (-x) * x ^ (a - 1)) +
    (fun x : ℝ => Real.exp (-x) * x ^ (b - 1))

private lemma gammaMajorant_integrable {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    Integrable (gammaMajorant a b) (volume.restrict (Ioi 0)) := by
  exact (Real.GammaIntegral_convergent ha).add (Real.GammaIntegral_convergent hb)

private lemma cpow_norm_le_two_exponent_majorant {a b x : ℝ} {z : ℂ}
    (hx : 0 < x) (haz : a ≤ z.re) (hzb : z.re ≤ b) :
    ‖(x : ℂ) ^ (z - 1)‖ ≤ x ^ (a - 1) + x ^ (b - 1) := by
  rw [Complex.norm_cpow_eq_rpow_re_of_pos hx, Complex.sub_re, Complex.one_re]
  rcases le_total x 1 with hx1 | h1x
  · exact le_add_of_le_of_nonneg
      (Real.rpow_le_rpow_of_exponent_ge hx hx1 (sub_le_sub_right haz 1))
      (Real.rpow_nonneg hx.le (b - 1))
  · exact le_add_of_nonneg_of_le (Real.rpow_nonneg hx.le (a - 1))
      (Real.rpow_le_rpow_of_exponent_le h1x (sub_le_sub_right hzb 1))

private lemma approxGammaKernel_norm_le_majorant {a b x : ℝ} {n : ℕ} {z : ℂ}
    (hn : n ≠ 0) (hx : 0 < x) (haz : a ≤ z.re) (hzb : z.re ≤ b) :
    ‖approxGammaKernel n z x‖ ≤ gammaMajorant a b x := by
  rcases lt_or_ge (n : ℝ) x with hxn | hxn
  · rw [approxGammaKernel, indicator_of_notMem (notMem_Ioc_of_gt hxn), norm_zero]
    simp only [gammaMajorant, Pi.add_apply]
    positivity
  · rw [approxGammaKernel, indicator_of_mem (mem_Ioc.mpr ⟨hx, hxn⟩), norm_mul,
      Complex.norm_of_nonneg
        (pow_nonneg (sub_nonneg.mpr <| div_le_one_of_le₀ hxn <| by positivity) _)]
    calc
      (1 - x / (n : ℝ)) ^ n * ‖(x : ℂ) ^ (z - 1)‖
          ≤ Real.exp (-x) * ‖(x : ℂ) ^ (z - 1)‖ := by
            gcongr
            exact Real.one_sub_div_pow_le_exp_neg hxn
      _ ≤ gammaMajorant a b x := by
            rw [gammaMajorant, Pi.add_apply, ← mul_add]
            gcongr
            exact cpow_norm_le_two_exponent_majorant hx haz hzb

private theorem gammaSeq_joint_tendsto_at {s : ℂ} (hs : 0 < s.re) :
    Tendsto (fun p : ℕ × ℂ => Complex.GammaSeq p.2 p.1)
      (atTop ×ˢ 𝓝 s) (𝓝 (Complex.Gamma s)) := by
  let a : ℝ := s.re / 2
  let b : ℝ := s.re + 1
  have ha : 0 < a := by dsimp [a]; positivity
  have hb : 0 < b := by dsimp [b]; linarith
  have hsab : a < s.re ∧ s.re < b := by dsimp [a, b]; constructor <;> linarith
  have hwindow : ∀ᶠ z : ℂ in 𝓝 s, a ≤ z.re ∧ z.re ≤ b := by
    have hopen : {z : ℂ | a < z.re ∧ z.re < b} ∈ 𝓝 s := by
      exact (isOpen_lt continuous_const Complex.continuous_re).inter
        (isOpen_lt Complex.continuous_re continuous_const) |>.mem_nhds hsab
    filter_upwards [hopen] with z hz
    exact ⟨hz.1.le, hz.2.le⟩
  have hzpos : ∀ᶠ z : ℂ in 𝓝 s, 0 < z.re := by
    filter_upwards [hwindow] with z hz
    exact ha.trans_le hz.1
  have hmeas : ∀ᶠ p : ℕ × ℂ in atTop ×ˢ 𝓝 s,
      AEStronglyMeasurable (approxGammaKernel p.1 p.2)
        (volume.restrict (Ioi 0)) := by
    filter_upwards [tendsto_snd.eventually hzpos] with p hp
    exact (integrable_approxGammaKernel p.1 hp).aestronglyMeasurable
  have hbound : ∀ᶠ p : ℕ × ℂ in atTop ×ˢ 𝓝 s,
      ∀ᵐ x ∂volume.restrict (Ioi 0),
        ‖approxGammaKernel p.1 p.2 x‖ ≤ gammaMajorant a b x := by
    filter_upwards [tendsto_fst.eventually (eventually_ne_atTop 0),
      tendsto_snd.eventually hwindow] with p hn hz
    rw [ae_restrict_iff' measurableSet_Ioi]
    filter_upwards with x hx
    exact approxGammaKernel_norm_le_majorant hn hx hz.1 hz.2
  have hlim : ∀ᵐ x ∂volume.restrict (Ioi 0),
      Tendsto (fun p : ℕ × ℂ => approxGammaKernel p.1 p.2 x)
        (atTop ×ˢ 𝓝 s)
        (𝓝 (↑(Real.exp (-x)) * (x : ℂ) ^ (s - 1))) := by
    rw [ae_restrict_iff' measurableSet_Ioi]
    filter_upwards with x hx
    have hxevent : ∀ᶠ p : ℕ × ℂ in atTop ×ˢ 𝓝 s, x ≤ (p.1 : ℝ) := by
      exact tendsto_fst.eventually (eventually_ge_atTop ⌈x⌉₊) |>.mono fun p hp => by
        rwa [Nat.ceil_le] at hp
    have hpow : Tendsto (fun p : ℕ × ℂ => ((1 - x / p.1) ^ p.1 : ℝ))
        (atTop ×ˢ 𝓝 s) (𝓝 (Real.exp (-x))) := by
      refine (Real.tendsto_one_add_div_pow_exp (-x)).comp tendsto_fst |>.congr' ?_
      filter_upwards [tendsto_fst.eventually (eventually_ne_atTop 0)] with p hn
      dsimp only [Function.comp_apply]
      congr 1
      ring
    have hcpow : Tendsto (fun p : ℕ × ℂ => (x : ℂ) ^ (p.2 - 1))
        (atTop ×ˢ 𝓝 s) (𝓝 ((x : ℂ) ^ (s - 1))) := by
      exact (continuousAt_const_cpow (Complex.ofReal_ne_zero.mpr hx.ne')).tendsto.comp
        (tendsto_snd.sub tendsto_const_nhds)
    refine (Complex.continuous_ofReal.tendsto _ |>.comp hpow).mul hcpow |>.congr' ?_
    filter_upwards [hxevent] with p hp
    change (↑((1 - x / (p.1 : ℝ)) ^ p.1) : ℂ) * (x : ℂ) ^ (p.2 - 1) =
      approxGammaKernel p.1 p.2 x
    have hmem : x ∈ Ioc 0 (p.1 : ℝ) := ⟨hx, hp⟩
    rw [approxGammaKernel, indicator_of_mem hmem]
  have hint := tendsto_integral_filter_of_dominated_convergence
    (μ := volume.restrict (Ioi 0))
    (gammaMajorant a b)
    hmeas hbound (gammaMajorant_integrable ha hb) hlim
  have hint' : Tendsto
      (fun p : ℕ × ℂ => ∫ x, approxGammaKernel p.1 p.2 x ∂volume.restrict (Ioi 0))
      (atTop ×ˢ 𝓝 s) (𝓝 (Complex.Gamma s)) := by
    rw [Complex.Gamma_eq_integral hs]
    exact hint
  apply hint'.congr'
  filter_upwards [tendsto_fst.eventually (eventually_ne_atTop 0),
    tendsto_snd.eventually hzpos] with p hn hz
  rw [integral_approxGammaKernel]
  exact (Complex.GammaSeq_eq_approx_Gamma_integral hz hn).symm

/-- Euler's approximants converge locally uniformly to `Gamma` on `Re z > 0`. -/
theorem gammaSeq_tendstoLocallyUniformlyOn :
    TendstoLocallyUniformlyOn
      (fun n z => Complex.GammaSeq z n) Complex.Gamma atTop positiveRealHalfPlane := by
  rw [isOpen_positiveRealHalfPlane.tendstoLocallyUniformlyOn_iff_forall_tendsto]
  intro s hs
  apply tendsto_uniformity_iff_dist_tendsto_zero.2
  have hsre : 0 < s.re := hs
  have hsne : ∀ n : ℕ, s ≠ -(n : ℂ) := by
    intro n h
    have hre := congrArg Complex.re h
    have hre' : s.re = -(n : ℝ) := by simpa using hre
    have hn : 0 ≤ (n : ℝ) := Nat.cast_nonneg n
    linarith
  have hGamma : Tendsto (fun p : ℕ × ℂ => Complex.Gamma p.2)
      (atTop ×ˢ 𝓝 s) (𝓝 (Complex.Gamma s)) := by
    exact (Complex.continuousAt_Gamma s hsne).tendsto.comp tendsto_snd
  have hSeq := gammaSeq_joint_tendsto_at hsre
  simpa using hGamma.dist hSeq

/-- The standard trigamma series is the complex derivative of `digamma` on
the positive-real half-plane. -/
theorem hasDerivAt_digamma_trigammaSeries {z : ℂ} (hz : 0 < z.re) :
    HasDerivAt Complex.digamma (trigammaSeries z) z :=
  hasDerivAt_digamma_of_gammaSeq_locallyUniform
    gammaSeq_tendstoLocallyUniformlyOn hz

/-- The derivative formula needed on the quarter-line, with no remaining
analytic premise. -/
theorem hasDerivAt_quarterDigammaReal (r : ℝ) :
    HasDerivAt quarterDigammaReal (quarterTrigammaSlope r) r :=
  hasDerivAt_quarterDigammaReal_of_gammaSeq_locallyUniform
    gammaSeq_tendstoLocallyUniformlyOn r

/-- The quarter-line real part of digamma is strictly increasing on the
nonnegative half-line. -/
theorem quarterDigammaReal_strictMonoOn :
    StrictMonoOn quarterDigammaReal (Ici 0) :=
  quarterDigammaReal_strictMonoOn_of_gammaSeq_locallyUniform
    gammaSeq_tendstoLocallyUniformlyOn

/-- The unconditional exterior comparison used by the F7 argument. -/
theorem quarterDigammaReal_exterior_lower_bound {S r : ℝ}
    (hS : 0 ≤ S) (hr : S ≤ |r|) :
    quarterDigammaReal S ≤ quarterDigammaReal r :=
  quarterDigammaReal_exterior_lower_bound_of_gammaSeq_locallyUniform
    gammaSeq_tendstoLocallyUniformlyOn hS hr

end GlideKernel
