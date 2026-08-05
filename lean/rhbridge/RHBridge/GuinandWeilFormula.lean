/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.GeneralZetaWeilForm
import RHBridge.ComplexResidue
import RHBridge.SmoothCompactSupportData
import Mathlib.NumberTheory.LSeries.ZetaZeros
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Complex.Exponential
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap
import Mathlib.Analysis.Fourier.FourierTransformDeriv
import Mathlib.Analysis.SpecialFunctions.Gamma.Digamma
import Mathlib.Analysis.Calculus.ParametricIntegral

/-!
# The zero side of the Guinand--Weil formula

This file gives an axiom-free formal statement of the missing explicit-formula
bridge.  Zeta zeros are counted with analytic multiplicity and exhausted by
closed disks.  The theorem asserting convergence and equality with the
arithmetic Weil form is recorded as a proposition, not assumed as an axiom.
-/

namespace RHP2Bridge.GuinandWeilFormula

open Filter
open scoped ENNReal InnerProductSpace RealInnerProductSpace Topology ArithmeticFunction
  ComplexConjugate

noncomputable section

/-- Zeros in the open critical strip; trivial zeros and the pole are excluded. -/
def NontrivialZetaZero :=
  {ρ : ℂ // riemannZeta ρ = 0 ∧ 0 < ρ.re ∧ ρ.re < 1}

/-- Analytic multiplicity of a nontrivial zeta zero. -/
def zeroMultiplicity (ρ : NontrivialZetaZero) : ℕ :=
  analyticOrderNatAt (𝕜 := ℂ) riemannZeta ρ.val

theorem analyticAt_riemannZeta_nontrivialZero (ρ : NontrivialZetaZero) :
    AnalyticAt ℂ riemannZeta ρ.val := by
  apply analyticOn_riemannZeta ρ.val
  simp only [Set.mem_compl_iff, Set.mem_singleton_iff]
  intro h
  have := congrArg Complex.re h
  norm_num at this
  linarith [ρ.property.2.2]

theorem eventually_riemannZeta_ne_zero_nhdsNE
    (ρ : NontrivialZetaZero) :
    ∀ᶠ z in 𝓝[≠] ρ.val, riemannZeta z ≠ 0 := by
  obtain ⟨U, hU, hUzero⟩ :=
    nhds_inter_eq_singleton_of_mem_discrete
      isDiscrete_riemannZetaZeros ρ.property.1
  have hU' : U ∈ 𝓝[≠] ρ.val := nhdsWithin_le_nhds hU
  filter_upwards [hU', self_mem_nhdsWithin] with z hz hzρ
  intro hzero
  have hzmem : z ∈ U ∩ riemannZetaZeros :=
    ⟨hz, hzero⟩
  have : z = ρ.val := by
    simpa [hUzero] using hzmem
  exact hzρ this

theorem analyticOrderAt_riemannZeta_ne_top (ρ : NontrivialZetaZero) :
    analyticOrderAt riemannZeta ρ.val ≠ ⊤ := by
  intro htop
  have hzero : ∀ᶠ z in 𝓝[≠] ρ.val, riemannZeta z = 0 :=
    (analyticOrderAt_eq_top.mp htop).filter_mono nhdsWithin_le_nhds
  exact Filter.Eventually.exists
    (hzero.and (eventually_riemannZeta_ne_zero_nhdsNE ρ)) |>.elim
      (fun _ h ↦ h.2 h.1)

theorem zeroMultiplicity_pos (ρ : NontrivialZetaZero) :
    0 < zeroMultiplicity ρ := by
  have hfinite := analyticOrderAt_riemannZeta_ne_top ρ
  have horder : analyticOrderAt riemannZeta ρ.val ≠ 0 :=
    analyticOrderAt_ne_zero.mpr
      ⟨analyticAt_riemannZeta_nontrivialZero ρ, ρ.property.1⟩
  apply Nat.pos_of_ne_zero
  intro hzero
  change analyticOrderNatAt riemannZeta ρ.val = 0 at hzero
  apply horder
  rw [← Nat.cast_analyticOrderNatAt hfinite]
  simp [hzero]

/-- Local analytic factorization of zeta at a nontrivial zero, with the
exponent equal to the multiplicity used in the zero sum. -/
theorem exists_local_zeta_factorization (ρ : NontrivialZetaZero) :
    ∃ g : ℂ → ℂ, AnalyticAt ℂ g ρ.val ∧ g ρ.val ≠ 0 ∧
      ∀ᶠ z in 𝓝 ρ.val,
        riemannZeta z = (z - ρ.val) ^ zeroMultiplicity ρ * g z := by
  exact ((analyticAt_riemannZeta_nontrivialZero ρ).analyticOrderNatAt_eq_iff
    (analyticOrderAt_riemannZeta_ne_top ρ)).mp rfl

/-- On a punctured neighborhood of a nontrivial zero, the logarithmic
derivative of zeta is its multiplicity-weighted simple pole plus a holomorphic
logarithmic derivative.  Thus the residue coefficient is exactly the analytic
multiplicity used in the zero sum. -/
theorem eventually_logDeriv_riemannZeta_eq_principalPart_add
    (ρ : NontrivialZetaZero) :
    ∃ g : ℂ → ℂ, AnalyticAt ℂ g ρ.val ∧ g ρ.val ≠ 0 ∧
      ∀ᶠ z in 𝓝[≠] ρ.val,
        logDeriv riemannZeta z =
          zeroMultiplicity ρ / (z - ρ.val) + logDeriv g z := by
  obtain ⟨g, hga, hg0, hfac⟩ := exists_local_zeta_factorization ρ
  refine ⟨g, hga, hg0, ?_⟩
  let p : ℂ → ℂ := fun z ↦ (z - ρ.val) ^ zeroMultiplicity ρ
  have hfacNE : riemannZeta =ᶠ[𝓝[≠] ρ.val] fun z ↦ p z * g z :=
    hfac.filter_mono nhdsWithin_le_nhds
  have hderiv := hfacNE.nhdsNE_deriv
  have hgNE : ∀ᶠ z in 𝓝[≠] ρ.val, g z ≠ 0 :=
    (hga.continuousAt.eventually_ne hg0).filter_mono nhdsWithin_le_nhds
  have hgaNE : ∀ᶠ z in 𝓝[≠] ρ.val, AnalyticAt ℂ g z :=
    hga.eventually_analyticAt.filter_mono nhdsWithin_le_nhds
  filter_upwards [hfacNE, hderiv, hgNE, hgaNE, self_mem_nhdsWithin]
    with z hzeta hder hg hgAnalytic hzρ
  have hzρ' : z ≠ ρ.val := by simpa using hzρ
  have hp : p z ≠ 0 := pow_ne_zero _ (sub_ne_zero.mpr hzρ')
  have hdp : DifferentiableAt ℂ p z := by
    dsimp [p]
    fun_prop
  have hlogeq : logDeriv riemannZeta z =
      logDeriv (fun w ↦ p w * g w) z := by
    unfold logDeriv
    simp only [Pi.div_apply]
    rw [hder, hzeta]
  rw [hlogeq, logDeriv_mul z hp hg hdp hgAnalytic.differentiableAt]
  congr 1
  dsimp [p]
  rw [logDeriv_fun_pow (by fun_prop)]
  simp [logDeriv_apply, div_eq_mul_inv]

/-- Bilateral Laplace transform of the compactly supported test vector. -/
def bilateralLaplace (a : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) : ℂ :=
  ∫ x : ℝ, IntervalZeroExtension.zeroExtension a f x *
    Complex.exp (s * x)

/-- Oppositely exponentially weighted zero extensions used on a vertical
line `re s = 1/2 + b`. -/
def weightedZeroExtensionFn (a b : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) (x : ℝ) : ℂ :=
  Real.exp (b * x) * IntervalZeroExtension.zeroExtensionFn a f x

/-- Representative-level bilateral transform, convenient for pointwise
Fourier calculations. -/
def bilateralLaplaceFn (a : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) : ℂ :=
  ∫ x : ℝ, IntervalZeroExtension.zeroExtensionFn a f x *
    Complex.exp (s * x)

/-- The representative-level bilateral Laplace integrand is integrable for
every compactly supported interval `L²` vector. -/
theorem integrable_bilateralLaplaceFn_integrand
    (a : ℝ) (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) :
    MeasureTheory.Integrable (fun x : ℝ ↦
      IntervalZeroExtension.zeroExtensionFn a f x *
        Complex.exp (s * x)) := by
  let C : ℝ := Real.exp (‖s‖ * |a|)
  have hmajorant : MeasureTheory.Integrable (fun x : ℝ ↦
      C * ‖IntervalZeroExtension.zeroExtensionFn a f x‖) := by
    exact (MeasureTheory.memLp_one_iff_integrable.mp
      (IntervalZeroExtension.zeroExtensionFn_memLp_one a f)).norm.const_mul C
  apply hmajorant.mono'
  · exact (IntervalZeroExtension.zeroExtensionFn_memLp a f).1.mul
      (Complex.continuous_exp.comp
        (continuous_const.mul Complex.continuous_ofReal)).aestronglyMeasurable
  · filter_upwards [] with x
    rw [norm_mul]
    by_cases hx : x ∈ LegendreScaledL2.Interval a
    · have hxa : |x| ≤ |a| := by
        rcases hx with ⟨hx₁, hx₂⟩
        have ha : 0 ≤ a := by linarith
        rw [abs_of_nonneg ha, abs_le]
        exact ⟨by linarith, hx₂⟩
      have hsx : ‖s * (x : ℂ)‖ ≤ ‖s‖ * |a| := by
        rw [norm_mul, Complex.norm_real, Real.norm_eq_abs]
        exact mul_le_mul_of_nonneg_left hxa (norm_nonneg s)
      have hexp : ‖Complex.exp (s * x)‖ ≤ C := by
        exact (Complex.norm_exp_le_exp_norm _).trans
          (Real.exp_le_exp.mpr hsx)
      simpa [mul_comm] using mul_le_mul_of_nonneg_left hexp
        (norm_nonneg (IntervalZeroExtension.zeroExtensionFn a f x))
    · rw [IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem a f hx]
      simp

/-- The quotient-representative bilateral Laplace integrand is integrable. -/
theorem integrable_bilateralLaplace_integrand
    (a : ℝ) (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) :
    MeasureTheory.Integrable (fun x : ℝ ↦
      (IntervalZeroExtension.zeroExtension a f : ℝ → ℂ) x *
        Complex.exp (s * x)) := by
  apply (integrable_bilateralLaplaceFn_integrand a f s).congr
  filter_upwards [IntervalZeroExtension.coeFn_zeroExtension a f] with x hx
  rw [hx]

/-- The bilateral Laplace transform is additive on the interval test space. -/
theorem bilateralLaplace_add
    (a : ℝ) (f g : GeneralZetaWeilForm.TestSpace a) (s : ℂ) :
    bilateralLaplace a (f + g) s =
      bilateralLaplace a f s + bilateralLaplace a g s := by
  unfold bilateralLaplace
  have hcoe :
      (IntervalZeroExtension.zeroExtension a (f + g) : ℝ → ℂ) =ᵐ[
        MeasureTheory.volume]
        fun x ↦ (IntervalZeroExtension.zeroExtension a f : ℝ → ℂ) x +
          (IntervalZeroExtension.zeroExtension a g : ℝ → ℂ) x := by
    rw [IntervalZeroExtension.zeroExtension_add]
    exact MeasureTheory.Lp.coeFn_add _ _
  calc
    (∫ x : ℝ, (IntervalZeroExtension.zeroExtension a (f + g) : ℝ → ℂ) x *
        Complex.exp (s * x)) =
      ∫ x : ℝ, ((IntervalZeroExtension.zeroExtension a f : ℝ → ℂ) x *
          Complex.exp (s * x) +
        (IntervalZeroExtension.zeroExtension a g : ℝ → ℂ) x *
          Complex.exp (s * x)) := by
            apply MeasureTheory.integral_congr_ae
            filter_upwards [hcoe] with x hx
            rw [hx]
            ring
    _ = _ := MeasureTheory.integral_add
      (integrable_bilateralLaplace_integrand a f s)
      (integrable_bilateralLaplace_integrand a g s)

/-- The bilateral Laplace transform is homogeneous for real scalars. -/
theorem bilateralLaplace_smul
    (a c : ℝ) (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) :
    bilateralLaplace a (c • f) s = c * bilateralLaplace a f s := by
  unfold bilateralLaplace
  have hcoe :
      (IntervalZeroExtension.zeroExtension a (c • f) : ℝ → ℂ) =ᵐ[
        MeasureTheory.volume]
        fun x ↦ c • (IntervalZeroExtension.zeroExtension a f : ℝ → ℂ) x := by
    rw [IntervalZeroExtension.zeroExtension_smul]
    exact MeasureTheory.Lp.coeFn_smul c _
  calc
    (∫ x : ℝ, (IntervalZeroExtension.zeroExtension a (c • f) : ℝ → ℂ) x *
        Complex.exp (s * x)) =
      ∫ x : ℝ, c * ((IntervalZeroExtension.zeroExtension a f : ℝ → ℂ) x *
        Complex.exp (s * x)) := by
          apply MeasureTheory.integral_congr_ae
          filter_upwards [hcoe] with x hx
          rw [hx, Complex.real_smul]
          ring
    _ = _ := by rw [MeasureTheory.integral_const_mul]

/-- Representative-level centered transform.  This is the product that
occurs on the vertical contour after applying cross-Plancherel. -/
def centeredTestTransformFn (a : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) : ℂ :=
  bilateralLaplaceFn a f (s - 1 / 2) *
    bilateralLaplaceFn a f (1 / 2 - s)

theorem conj_zeroExtensionFn (a x : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) :
    conj (IntervalZeroExtension.zeroExtensionFn a f x) =
      IntervalZeroExtension.zeroExtensionFn a f x := by
  by_cases hx : x ∈ LegendreScaledL2.Interval a
  · let y : LegendreScaledL2.Interval a := ⟨x, hx⟩
    have hy := IntervalZeroExtension.zeroExtensionFn_coe a f y
    change conj (IntervalZeroExtension.zeroExtensionFn a f y.val) =
      IntervalZeroExtension.zeroExtensionFn a f y.val
    rw [hy]
    simp
  · rw [IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem a f hx]
    simp

theorem conj_bilateralLaplaceFn (a : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) :
    conj (bilateralLaplaceFn a f s) =
      bilateralLaplaceFn a f (conj s) := by
  unfold bilateralLaplaceFn
  rw [← integral_conj]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  rw [map_mul, conj_zeroExtensionFn]
  rw [← Complex.exp_conj]
  congr 2
  simp [Complex.conj_ofReal]

theorem fourier_weightedZeroExtensionFn_eq_bilateralLaplaceFn
    (a b xi : ℝ) (f : GeneralZetaWeilForm.TestSpace a) :
    FourierTransform.fourier (weightedZeroExtensionFn a b f) xi =
      bilateralLaplaceFn a f (b - 2 * Real.pi * xi * Complex.I) := by
  rw [Real.fourier_eq']
  unfold weightedZeroExtensionFn bilateralLaplaceFn
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  simp only [RCLike.inner_apply, conj_trivial, smul_eq_mul]
  rw [Complex.ofReal_exp]
  have hexp :
      Complex.exp (↑(-2 * Real.pi * (xi * x)) * Complex.I) *
          Complex.exp (b * x) =
        Complex.exp ((b - 2 * Real.pi * xi * Complex.I) * x) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  have hbcast : ((b * x : ℝ) : ℂ) = (b : ℂ) * (x : ℂ) := by norm_cast
  rw [hbcast, ← mul_assoc, hexp]
  ring

theorem weightedZeroExtensionFn_memLp {p : ℝ≥0∞}
    (a b : ℝ) (f : GeneralZetaWeilForm.TestSpace a)
    (hf : MeasureTheory.MemLp
      (IntervalZeroExtension.zeroExtensionFn a f) p
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)) :
    MeasureTheory.MemLp (weightedZeroExtensionFn a b f) p
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  apply hf.of_le_mul (c := Real.exp (|b| * |a|))
  · have hc : Continuous (fun x : ℝ ↦ (Real.exp (b * x) : ℂ)) :=
      Complex.continuous_ofReal.comp (Real.continuous_exp.comp
        (continuous_const.mul continuous_id))
    exact hc.aestronglyMeasurable.mul hf.1
  · filter_upwards [] with x
    by_cases hx : x ∈ LegendreScaledL2.Interval a
    · have hxa : |x| ≤ |a| := by
        rcases hx with ⟨hx₁, hx₂⟩
        have ha : 0 ≤ a := by linarith
        rw [abs_of_nonneg ha, abs_le]
        exact ⟨by linarith, hx₂⟩
      have hbx : b * x ≤ |b| * |a| := by
        calc
          b * x ≤ |b * x| := le_abs_self _
          _ = |b| * |x| := abs_mul b x
          _ ≤ |b| * |a| := mul_le_mul_of_nonneg_left hxa (abs_nonneg b)
      unfold weightedZeroExtensionFn
      rw [norm_mul, Complex.norm_real, Real.norm_eq_abs,
        abs_of_pos (Real.exp_pos _)]
      exact mul_le_mul_of_nonneg_right (Real.exp_le_exp.mpr hbx) (norm_nonneg _)
    · rw [weightedZeroExtensionFn,
        IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem a f hx]
      simp

theorem weightedZeroExtensionFn_memLp_one (a b : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) :
    MeasureTheory.MemLp (weightedZeroExtensionFn a b f) 1
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
  weightedZeroExtensionFn_memLp a b f
    (IntervalZeroExtension.zeroExtensionFn_memLp_one a f)

theorem weightedZeroExtensionFn_memLp_two (a b : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) :
    MeasureTheory.MemLp (weightedZeroExtensionFn a b f) 2
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
  weightedZeroExtensionFn_memLp a b f
    (IntervalZeroExtension.zeroExtensionFn_memLp a f)

theorem coe_fourier_weightedZeroExtensionL2_ae_eq_bilateralLaplaceFn
    (a b : ℝ) (f : GeneralZetaWeilForm.TestSpace a) :
    (FourierTransform.fourier
      (AutocorrelationPlancherel.toFullLineL2
        (weightedZeroExtensionFn a b f)
        (weightedZeroExtensionFn_memLp_two a b f)) : ℝ → ℂ) =ᵐ[
          (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      fun xi ↦ bilateralLaplaceFn a f
        (b - 2 * Real.pi * xi * Complex.I) := by
  have h := AutocorrelationPlancherel.coe_fourier_toFullLineL2_ae_eq_fourierFn
    (weightedZeroExtensionFn a b f)
    (weightedZeroExtensionFn_memLp_one a b f)
    (weightedZeroExtensionFn_memLp_two a b f)
  filter_upwards [h] with xi hxi
  rw [hxi, fourier_weightedZeroExtensionFn_eq_bilateralLaplaceFn]

/-- Opposite exponential weights cancel in the translated time-domain
cross-product, leaving only the scalar `exp (b*u)`. -/
theorem weighted_cross_inner_cancel (a b u x : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) :
    ⟪weightedZeroExtensionFn a (-b) f x,
        weightedZeroExtensionFn a b f (x + u)⟫_ℂ =
      Real.exp (b * u) *
        ⟪IntervalZeroExtension.zeroExtensionFn a f x,
          IntervalZeroExtension.zeroExtensionFn a f (x + u)⟫_ℂ := by
  unfold weightedZeroExtensionFn
  simp only [RCLike.inner_apply, map_mul, Complex.conj_ofReal]
  push_cast
  have hexp : Complex.exp (b * (x + u)) * Complex.exp (-b * x) =
      Complex.exp (b * u) := by
    rw [← Complex.exp_add]
    congr 1
    ring
  calc
    _ = (Complex.exp (b * (x + u)) * Complex.exp (-b * x)) *
        (IntervalZeroExtension.zeroExtensionFn a f (x + u) *
          (starRingEnd ℂ) (IntervalZeroExtension.zeroExtensionFn a f x)) := by ring
    _ = _ := by rw [hexp]

/-- Weighted cross-Plancherel: opposite exponential weights on the two
Fourier factors cancel in time, leaving the scalar `exp (b*u)` times the
unweighted translated correlation. -/
theorem weighted_crossPlancherel (a b u : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) :
    (∫ xi, ⟪(FourierTransform.fourier
          (AutocorrelationPlancherel.toFullLineL2
            (weightedZeroExtensionFn a (-b) f)
            (weightedZeroExtensionFn_memLp_two a (-b) f)) : ℝ → ℂ) xi,
        Real.fourierChar (u * xi) •
          (FourierTransform.fourier
            (AutocorrelationPlancherel.toFullLineL2
              (weightedZeroExtensionFn a b f)
              (weightedZeroExtensionFn_memLp_two a b f)) : ℝ → ℂ) xi⟫_ℂ) =
      Real.exp (b * u) *
        ∫ x, ⟪IntervalZeroExtension.zeroExtensionFn a f x,
          IntervalZeroExtension.zeroExtensionFn a f (x + u)⟫_ℂ := by
  rw [← AutocorrelationPlancherel.crossCorrelation_eq_fourier u
    (weightedZeroExtensionFn a (-b) f) (weightedZeroExtensionFn a b f)
    (weightedZeroExtensionFn_memLp_two a (-b) f)
    (weightedZeroExtensionFn_memLp_one a b f)
    (weightedZeroExtensionFn_memLp_two a b f)]
  rw [AutocorrelationPlancherel.crossCorrelation_eq_integral]
  rw [← MeasureTheory.integral_const_mul]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  exact weighted_cross_inner_cancel a b u x f

/-- The weighted cross-Plancherel identity written directly as a centered
vertical-line transform.  In particular, the two Fourier factors are exactly
`F(s-1/2)` and `F(1/2-s)` at
`s = 1/2 + b - 2π i ξ`; no informal conjugation or sign convention remains. -/
theorem centered_verticalLine_eq_weighted_autocorrelation
    (a b u : ℝ) (f : GeneralZetaWeilForm.TestSpace a) :
    (∫ xi : ℝ, Real.fourierChar (u * xi) *
        centeredTestTransformFn a f
          (1 / 2 + b - 2 * Real.pi * xi * Complex.I)) =
      Real.exp (b * u) *
        ∫ x : ℝ, ⟪IntervalZeroExtension.zeroExtensionFn a f x,
          IntervalZeroExtension.zeroExtensionFn a f (x + u)⟫_ℂ := by
  rw [← weighted_crossPlancherel a b u f]
  apply MeasureTheory.integral_congr_ae
  have hneg := coe_fourier_weightedZeroExtensionL2_ae_eq_bilateralLaplaceFn
    a (-b) f
  have hpos := coe_fourier_weightedZeroExtensionL2_ae_eq_bilateralLaplaceFn
    a b f
  filter_upwards [hneg, hpos] with xi hnegxi hposxi
  rw [hnegxi, hposxi]
  simp only [RCLike.inner_apply, Circle.smul_def]
  rw [conj_bilateralLaplaceFn]
  unfold centeredTestTransformFn
  simp only [map_sub, map_mul, Complex.conj_ofReal, map_ofNat, Complex.conj_I]
  have h₁ :
      ((1 / 2 + b - 2 * Real.pi * xi * Complex.I : ℂ) - 1 / 2) =
        b - 2 * Real.pi * xi * Complex.I := by
    push_cast
    ring
  have h₂ :
      (1 / 2 - (1 / 2 + b - 2 * Real.pi * xi * Complex.I : ℂ)) =
        (-b : ℂ) + 2 * Real.pi * xi * Complex.I := by
    push_cast
    ring
  rw [h₁, h₂]
  simp only [smul_eq_mul]
  have hcast : ((-b : ℝ) : ℂ) = -(b : ℂ) := by norm_cast
  rw [hcast]
  ring

/-- The centered transform occurring at a zero `ρ`, namely
`F(ρ-1/2) F(1/2-ρ)`, with analytic multiplicity. -/
def zeroSummand (a : ℝ) (f : GeneralZetaWeilForm.TestSpace a)
    (ρ : NontrivialZetaZero) : ℂ :=
  zeroMultiplicity ρ *
    (bilateralLaplace a f (ρ.val - 1 / 2) *
      bilateralLaplace a f (1 / 2 - ρ.val))

/-- The centered entire test transform appearing in the contour proof. -/
def centeredTestTransform (a : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) : ℂ :=
  bilateralLaplace a f (s - 1 / 2) *
    bilateralLaplace a f (1 / 2 - s)

/-- On the right half-plane, the contour integrand is exactly the absolutely
convergent von Mangoldt Dirichlet series, multiplied termwise by the centered
test transform. -/
theorem hasSum_rightContour_vonMangoldt
    (a : ℝ) (f : GeneralZetaWeilForm.TestSpace a)
    {s : ℂ} (hs : 1 < s.re) :
    HasSum
      (fun n ↦ centeredTestTransform a f s *
        LSeries.term (fun k : ℕ ↦ (Λ k : ℂ)) s n)
      (centeredTestTransform a f s * (-logDeriv riemannZeta s)) := by
  have hsum := (ArithmeticFunction.LSeriesSummable_vonMangoldt hs).LSeriesHasSum
  have hvalue := ArithmeticFunction.LSeries_vonMangoldt_eq_deriv_riemannZeta_div hs
  have hlog : LSeries (fun n : ℕ ↦ (Λ n : ℂ)) s =
      -logDeriv riemannZeta s := by
    rw [hvalue]
    unfold logDeriv
    simp only [Pi.div_apply]
    ring
  simpa [hlog] using hsum.mul_left (centeredTestTransform a f s)

/-- On the right of the critical strip, the logarithmic derivative of the
completed zeta function splits into its archimedean and prime factors.  This
is the pointwise factorization used to identify the right vertical edge. -/
theorem logDeriv_completedRiemannZeta_eq_gammaR_add_zeta
    {s : ℂ} (hs : 1 < s.re) :
    logDeriv completedRiemannZeta s =
      logDeriv Complex.Gammaℝ s + logDeriv riemannZeta s := by
  have hs0 : s ≠ 0 := by
    intro h
    subst s
    norm_num at hs
  have hΓ : Complex.Gammaℝ s ≠ 0 :=
    Complex.Gammaℝ_ne_zero_of_re_pos (lt_trans (by norm_num) hs)
  have hζ : riemannZeta s ≠ 0 := riemannZeta_ne_zero_of_one_lt_re hs
  have hΓdiff : DifferentiableAt ℂ Complex.Gammaℝ s := by
    change DifferentiableAt ℂ
      (fun z : ℂ ↦ (Real.pi : ℂ) ^ (-z / 2) * Complex.Gamma (z / 2)) s
    apply DifferentiableAt.mul
    · exact (differentiableAt_id.neg.div_const 2).const_cpow
        (Or.inl (Complex.ofReal_ne_zero.mpr Real.pi_ne_zero))
    · have harg : ∀ m : ℕ, s / 2 ≠ -(m : ℂ) := by
        intro m hm
        have hre := congrArg Complex.re hm
        norm_num at hre
        have hspos : 0 < s.re := lt_trans (by norm_num) hs
        linarith
      exact (Complex.differentiableAt_Gamma (s / 2) harg).comp s
        (differentiableAt_id.div_const 2)
  have hζdiff : DifferentiableAt ℂ riemannZeta s :=
    differentiableAt_riemannZeta (by
      intro h
      have := congrArg Complex.re h
      norm_num at this
      linarith)
  have heq : completedRiemannZeta =ᶠ[𝓝 s]
      fun z ↦ Complex.Gammaℝ z * riemannZeta z := by
    have hpos : {z : ℂ | 0 < z.re} ∈ 𝓝 s :=
      (isOpen_lt continuous_const Complex.continuous_re).mem_nhds
        (lt_trans (by norm_num) hs)
    filter_upwards [hpos] with z hz
    have hz0 : z ≠ 0 := by
      intro h
      subst z
      norm_num at hz
    have hΓz := Complex.Gammaℝ_ne_zero_of_re_pos hz
    rw [riemannZeta_def_of_ne_zero hz0]
    field_simp
  have hlog : logDeriv completedRiemannZeta s =
      logDeriv (fun z ↦ Complex.Gammaℝ z * riemannZeta z) s := by
    unfold logDeriv
    simp only [Pi.div_apply]
    rw [heq.deriv_eq, heq.self_of_nhds]
  rw [hlog, logDeriv_mul s hΓ hζ hΓdiff hζdiff]

/-- The archimedean logarithmic derivative in the conventional digamma
normalization. -/
theorem logDeriv_gammaR_eq_digamma {s : ℂ} (hs : 0 < s.re) :
    logDeriv Complex.Gammaℝ s =
      -(Complex.log (Real.pi : ℂ)) / 2 + Complex.digamma (s / 2) / 2 := by
  let A : ℂ → ℂ := fun z ↦ (Real.pi : ℂ) ^ (-z / (2 : ℂ))
  let B : ℂ → ℂ := Complex.Gamma ∘ fun z ↦ z / (2 : ℂ)
  have hπ : (Real.pi : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr Real.pi_ne_zero
  have hA : HasDerivAt A
      (A s * Complex.log (Real.pi : ℂ) * (-1 / (2 : ℂ))) s := by
    dsimp [A]
    exact ((hasDerivAt_id s).neg.div_const 2).const_cpow (Or.inl hπ)
  have harg : ∀ m : ℕ, s / (2 : ℂ) ≠ -(m : ℂ) := by
    intro m hm
    have hre := congrArg Complex.re hm
    norm_num at hre
    linarith
  have hB : HasDerivAt B (deriv Complex.Gamma (s / (2 : ℂ)) / (2 : ℂ)) s := by
    dsimp [B]
    simpa only [Function.comp_apply, id_eq, div_eq_mul_inv, one_mul, mul_comm] using
      (Complex.differentiableAt_Gamma (s / 2) harg).hasDerivAt.comp s
        ((hasDerivAt_id s).div_const 2)
  have hA0 : A s ≠ 0 := by simp [A, hπ]
  have hB0 : B s ≠ 0 := by
    dsimp [B]
    exact Complex.Gamma_ne_zero harg
  rw [show Complex.Gammaℝ = fun z ↦ A z * B z by
    funext z; rfl]
  rw [logDeriv_mul s hA0 hB0 hA.differentiableAt hB.differentiableAt]
  unfold logDeriv Complex.digamma
  simp only [Pi.div_apply, hA.deriv, hB.deriv]
  rw [logDeriv_apply]
  dsimp [B] at hB0 ⊢
  field_simp

/-- Fully identified logarithmic derivative on the right contour: the first
two terms are archimedean and the last term is the von Mangoldt Dirichlet
series through `hasSum_rightContour_vonMangoldt`. -/
theorem logDeriv_completedRiemannZeta_rightContour {s : ℂ} (hs : 1 < s.re) :
    logDeriv completedRiemannZeta s =
      -(Complex.log (Real.pi : ℂ)) / 2 +
        Complex.digamma (s / 2) / 2 + logDeriv riemannZeta s := by
  rw [logDeriv_completedRiemannZeta_eq_gammaR_add_zeta hs,
    logDeriv_gammaR_eq_digamma (lt_trans (by norm_num) hs)]

theorem rightContour_vonMangoldt_term {s : ℂ} {n : ℕ} (hn : n ≠ 0) :
    LSeries.term (fun k : ℕ ↦ (Λ k : ℂ)) s n = Λ n / (n : ℂ) ^ s := by
  simp [LSeries.term, hn]

/-- Logarithmic-derivative form of the completed-zeta functional equation.
The minus sign is the derivative of `s ↦ 1 - s`.  This is the exact symmetry
used to turn the left vertical side of the Guinand--Weil rectangle into a
second right-side integral. -/
theorem logDeriv_completedRiemannZeta_one_sub
    {s : ℂ} (hs0 : s ≠ 0) (hs1 : s ≠ 1) :
    logDeriv completedRiemannZeta (1 - s) =
      -logDeriv completedRiemannZeta s := by
  have h1s0 : 1 - s ≠ 0 := sub_ne_zero.mpr hs1.symm
  have h1s1 : 1 - s ≠ 1 := by
    intro h
    apply hs0
    linear_combination -h
  have hleft : HasDerivAt
      (completedRiemannZeta ∘ fun z : ℂ ↦ 1 - z)
      (-deriv completedRiemannZeta (1 - s)) s := by
    simpa only [zero_sub, mul_neg, mul_one] using
      (differentiableAt_completedZeta h1s0 h1s1).hasDerivAt.comp s
        ((hasDerivAt_const s (1 : ℂ)).sub (hasDerivAt_id s))
  have hright : HasDerivAt completedRiemannZeta
      (deriv completedRiemannZeta s) s :=
    (differentiableAt_completedZeta hs0 hs1).hasDerivAt
  have hderiv : -deriv completedRiemannZeta (1 - s) =
      deriv completedRiemannZeta s := by
    exact (hleft.congr_of_eventuallyEq
      (Filter.Eventually.of_forall fun z ↦
        (completedRiemannZeta_one_sub z).symm)).unique hright
  unfold logDeriv
  simp only [Pi.div_apply]
  rw [completedRiemannZeta_one_sub, ← hderiv]
  ring

private theorem zerosInClosedBall_finite (R : ℝ) :
    (Metric.closedBall (0 : ℂ) R ∩ riemannZetaZeros).Finite :=
  (isCompact_closedBall (0 : ℂ) R).inter_riemannZetaZeros_finite

/-- Nontrivial zeros in a closed disk, as a finite set. -/
def nontrivialZerosInDisk (R : ℝ) : Finset NontrivialZetaZero :=
  ((zerosInClosedBall_finite R).preimage
    (f := fun ρ : NontrivialZetaZero ↦ ρ.val)
    Subtype.val_injective.injOn).toFinset

/-- Multiplicity-weighted zero sum in a closed disk. -/
def zeroSumInDisk (R a : ℝ) (f : GeneralZetaWeilForm.TestSpace a) : ℂ :=
  ∑ ρ ∈ nontrivialZerosInDisk R, zeroSummand a f ρ

/-- The convergence convention used by the classical Guinand--Weil formula:
zeros are exhausted symmetrically by expanding closed disks.  Unlike
`Summable`, this does not silently assert unconditional (hence absolute, for
scalar series) convergence of a zero sum at low test-function regularity. -/
def DiskHolds (a : ℝ) (f : GeneralZetaWeilForm.TestSpace a) : Prop :=
  Tendsto (fun R : ℝ ↦ zeroSumInDisk R a f) atTop
    (𝓝 (GeneralZetaWeilForm.weilForm a f : ℂ))

/-- Quantitative transform decay sufficient for the horizontal sides of the
standard Guinand--Weil rectangle to vanish.  This is deliberately separated
from the ambient compactly supported `L²` space: compact support plus `L²`
alone does not supply such a pointwise bound. -/
def HasContourDecay (a : ℝ) (f : GeneralZetaWeilForm.TestSpace a) : Prop :=
  ∃ C : ℝ, 0 ≤ C ∧ ∀ (sigma : Set.Icc (-1 : ℝ) 2) (t : ℝ),
    ‖centeredTestTransformFn a f (sigma.val + t * Complex.I)‖ ≤
      C / (1 + |t|) ^ 2

/-- The smooth compact-support class used by the classical (absolutely
convergent) explicit formula.  The global regularity requirement includes
the endpoint matching conditions forced by extension by zero. -/
def IsSmoothCompactSupportTest (a : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) : Prop :=
  ContDiff ℝ 2 (IntervalZeroExtension.zeroExtensionFn a f)

namespace SmoothCompactSupportData

def intervalContinuousMap {a : ℝ} (φ : SmoothCompactSupportData a) :
    C(LegendreScaledL2.Interval a, ℝ) where
  toFun x := φ x.val
  continuous_toFun := φ.smooth.continuous.comp continuous_subtype_val

/-- Map an explicit smooth representative into the interval `L²` quotient. -/
noncomputable def toTestSpace {a : ℝ} (φ : SmoothCompactSupportData a) :
    GeneralZetaWeilForm.TestSpace a :=
  ContinuousMap.toLp 2 (LegendreScaledL2.intervalMeasure a) ℝ
    φ.intervalContinuousMap

theorem coe_toTestSpace_ae {a : ℝ} (φ : SmoothCompactSupportData a) :
    (φ.toTestSpace : LegendreScaledL2.Interval a → ℝ) =ᵐ[
      LegendreScaledL2.intervalMeasure a] fun x ↦ φ x.val := by
  exact ContinuousMap.coeFn_toLp
    (LegendreScaledL2.intervalMeasure a) φ.intervalContinuousMap

theorem hasCompactSupport {a : ℝ} (φ : SmoothCompactSupportData a) :
    HasCompactSupport φ.toFun :=
  HasCompactSupport.of_support_subset_isCompact isCompact_Icc φ.support_subset

theorem hasCompactSupport_ofReal {a : ℝ} (φ : SmoothCompactSupportData a) :
    HasCompactSupport (fun x : ℝ ↦ (φ x : ℂ)) := by
  apply HasCompactSupport.of_support_subset_isCompact isCompact_Icc
  intro x hx
  apply φ.support_subset
  intro hzero
  exact hx (by simp [hzero])

/-- Bilateral Laplace transform before passage to the `L²` quotient. -/
noncomputable def bilateralLaplace {a : ℝ} (φ : SmoothCompactSupportData a)
    (s : ℂ) : ℂ :=
  ∫ x : ℝ, Complex.exp (s * x) * (φ x : ℂ)

theorem integrable_bilateralLaplace {a : ℝ}
    (φ : SmoothCompactSupportData a) (s : ℂ) :
    MeasureTheory.Integrable
      (fun x : ℝ ↦ Complex.exp (s * x) * (φ x : ℂ)) := by
  apply Continuous.integrable_of_hasCompactSupport
  · exact (Complex.continuous_exp.comp (continuous_const.mul
        Complex.continuous_ofReal)).mul
      (Complex.continuous_ofReal.comp φ.smooth.continuous)
  · exact φ.hasCompactSupport_ofReal.mul_left

theorem integrable_bilateralLaplace_deriv {a : ℝ}
    (φ : SmoothCompactSupportData a) (s : ℂ) :
    MeasureTheory.Integrable
      (fun x : ℝ ↦ (x : ℂ) *
        (Complex.exp (s * x) * (φ x : ℂ))) := by
  apply Continuous.integrable_of_hasCompactSupport
  · exact Complex.continuous_ofReal.mul
      ((Complex.continuous_exp.comp (continuous_const.mul
          Complex.continuous_ofReal)).mul
        (Complex.continuous_ofReal.comp φ.smooth.continuous))
  · exact φ.hasCompactSupport_ofReal.mul_left.mul_left

/-- An integrable majorant, uniform for the transform derivative on the unit
ball about `s`. -/
def localDerivativeMajorant {a : ℝ} (φ : SmoothCompactSupportData a)
    (s : ℂ) (x : ℝ) : ℝ :=
  |φ x| * |x| * Real.exp ((‖s‖ + 1) * |x|)

theorem integrable_localDerivativeMajorant {a : ℝ}
    (φ : SmoothCompactSupportData a) (s : ℂ) :
    MeasureTheory.Integrable (φ.localDerivativeMajorant s) := by
  apply Continuous.integrable_of_hasCompactSupport
  · exact ((φ.smooth.continuous.abs.mul continuous_abs).mul
      (Real.continuous_exp.comp
        (continuous_const.mul continuous_abs)))
  · apply HasCompactSupport.of_support_subset_isCompact isCompact_Icc
    intro x hx
    apply φ.support_subset
    intro hzero
    exact hx (by simp [localDerivativeMajorant, hzero])

end SmoothCompactSupportData

/-- The chosen full-line representative really is supported in `[-a,a]`.
This fact is independent of any smoothness assumption. -/
theorem support_zeroExtensionFn_subset (a : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) :
    Function.support (IntervalZeroExtension.zeroExtensionFn a f) ⊆
      LegendreScaledL2.Interval a := by
  intro x hx
  by_contra hxa
  exact hx (IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem a f hxa)

theorem hasCompactSupport_zeroExtensionFn (a : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) :
    HasCompactSupport (IntervalZeroExtension.zeroExtensionFn a f) :=
  HasCompactSupport.of_support_subset_isCompact
    isCompact_Icc (support_zeroExtensionFn_subset a f)

/-- Exponential weighting preserves both global `C²` regularity and compact
support.  These are the functions to which Fourier integration by parts is
applied on the two vertical lines. -/
theorem smooth_weightedZeroExtensionFn {a b : ℝ}
    {f : GeneralZetaWeilForm.TestSpace a}
    (hf : IsSmoothCompactSupportTest a f) :
    ContDiff ℝ 2 (weightedZeroExtensionFn a b f) := by
  unfold IsSmoothCompactSupportTest at hf
  unfold weightedZeroExtensionFn
  have heR : ContDiff ℝ 2 (fun x : ℝ ↦ Real.exp (b * x)) := by fun_prop
  have heC : ContDiff ℝ 2 (fun x : ℝ ↦ (Real.exp (b * x) : ℂ)) :=
    Complex.ofRealCLM.contDiff.comp heR
  exact heC.mul hf

theorem hasCompactSupport_weightedZeroExtensionFn (a b : ℝ)
    (f : GeneralZetaWeilForm.TestSpace a) :
    HasCompactSupport (weightedZeroExtensionFn a b f) := by
  apply HasCompactSupport.of_support_subset_isCompact
    (K := LegendreScaledL2.Interval a) isCompact_Icc
  intro x hx
  by_contra hxa
  apply hx
  simp [weightedZeroExtensionFn,
    IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem a f hxa]

/-- Every derivative through order two of a smooth compactly-supported test
function is integrable.  This is the analytic input needed by Mathlib's
Fourier integration-by-parts theorem. -/
theorem integrable_iteratedFDeriv_weightedZeroExtensionFn
    {a b : ℝ} {f : GeneralZetaWeilForm.TestSpace a}
    (hf : IsSmoothCompactSupportTest a f) {n : ℕ} (hn : n ≤ 2) :
    MeasureTheory.Integrable
      (iteratedFDeriv ℝ n (weightedZeroExtensionFn a b f)) := by
  have hs := smooth_weightedZeroExtensionFn (b := b) hf
  have hc : Continuous
      (iteratedFDeriv ℝ n (weightedZeroExtensionFn a b f)) :=
    (hs.continuous_iteratedFDeriv (by exact_mod_cast hn))
  apply hc.integrable_of_hasCompactSupport
  exact (hasCompactSupport_weightedZeroExtensionFn a b f).iteratedFDeriv n

theorem integrable_pow_mul_iteratedFDeriv_weightedZeroExtensionFn
    {a b : ℝ} {f : GeneralZetaWeilForm.TestSpace a}
    (hf : IsSmoothCompactSupportTest a f) {k n : ℕ} (hn : n ≤ 2) :
    MeasureTheory.Integrable (fun x : ℝ ↦
      ‖x‖ ^ k * ‖iteratedFDeriv ℝ n (weightedZeroExtensionFn a b f) x‖) := by
  have hs := smooth_weightedZeroExtensionFn (b := b) hf
  have hc : Continuous (fun x : ℝ ↦
      ‖x‖ ^ k * ‖iteratedFDeriv ℝ n (weightedZeroExtensionFn a b f) x‖) :=
    (continuous_norm.pow k).mul
      ((hs.continuous_iteratedFDeriv (by exact_mod_cast hn)).norm)
  apply hc.integrable_of_hasCompactSupport
  exact (hasCompactSupport_weightedZeroExtensionFn a b f).iteratedFDeriv n |>.norm.mul_left

/-- Two integrations by parts, packaged as the uniform polynomial Fourier
bound needed on a vertical contour. -/
theorem exists_fourier_decay_constant_weighted
    {a b : ℝ} {f : GeneralZetaWeilForm.TestSpace a}
    (hf : IsSmoothCompactSupportTest a f) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ ξ : ℝ,
      ‖ξ‖ ^ 2 *
          ‖FourierTransform.fourier (weightedZeroExtensionFn a b f) ξ‖ ≤ C := by
  let C : ℝ := 2 ^ 2 *
    ∑ p ∈ Finset.range 1 ×ˢ Finset.range 3,
      ∫ x : ℝ, ‖x‖ ^ p.1 *
        ‖iteratedFDeriv ℝ p.2 (weightedZeroExtensionFn a b f) x‖
  refine ⟨C, ?_, ?_⟩
  · dsimp [C]
    apply mul_nonneg (by norm_num)
    apply Finset.sum_nonneg
    intro p _hp
    exact MeasureTheory.integral_nonneg fun x ↦
      mul_nonneg (pow_nonneg (norm_nonneg x) _) (norm_nonneg _)
  · intro ξ
    have h := Real.pow_mul_norm_iteratedFDeriv_fourier_le
      (K := (0 : ℕ∞)) (N := (2 : ℕ∞))
      (f := weightedZeroExtensionFn a b f)
      (smooth_weightedZeroExtensionFn (b := b) hf)
      (fun k n _hk hn ↦
        integrable_pow_mul_iteratedFDeriv_weightedZeroExtensionFn hf
          (by exact_mod_cast hn))
      (k := 0) (n := 2) (by simp) (by simp) ξ
    simpa [C] using h

/-- Absolutely convergent version of the Guinand--Weil assertion.

This version is appropriate for a sufficiently smooth contour-admissible test
vector.  It is intentionally stronger than `DiskHolds` and must not be used
as the general compactly supported `L²` formulation.
-/
def Holds (a : ℝ) (f : GeneralZetaWeilForm.TestSpace a) : Prop :=
  Summable (zeroSummand a f) ∧
    (∑' ρ : NontrivialZetaZero, zeroSummand a f ρ) =
      GeneralZetaWeilForm.weilForm a f

theorem holds_implies_zero_sum_real {a : ℝ}
    {f : GeneralZetaWeilForm.TestSpace a} (h : Holds a f) :
    (∑' ρ : NontrivialZetaZero, zeroSummand a f ρ).im = 0 := by
  rw [h.2]
  simp

end

end RHP2Bridge.GuinandWeilFormula
