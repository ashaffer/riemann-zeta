/-
Canonical zero extension of the real interval `L²` space to complex
full-line `L²`, with exact norm preservation.
-/
import IntervalFourierL2
import Mathlib.Analysis.Fourier.LpSpace

namespace IntervalZeroExtension

open scoped ENNReal InnerProductSpace FourierTransform

/-- Complex `L²` on the real line with Lebesgue measure. -/
noncomputable abbrev FullLineComplexL2 :=
  MeasureTheory.Lp ℂ 2 (MeasureTheory.volume : MeasureTheory.Measure ℝ)

/-- The selected interval representative, embedded in `ℂ` and extended by
zero off `[-a,a]`.  Passing this function to `MemLp.toLp` makes the resulting
full-line vector independent of all representative choices. -/
noncomputable def zeroExtensionFn
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) : ℝ → ℂ :=
  Function.extend
    (fun x : LegendreScaledL2.Interval a ↦ (x : ℝ))
    (fun x ↦ ((w x : ℝ) : ℂ))
    (fun _ ↦ 0)

@[simp] theorem zeroExtensionFn_coe
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a)
    (x : LegendreScaledL2.Interval a) :
    zeroExtensionFn a w (x : ℝ) = ((w x : ℝ) : ℂ) := by
  simp [zeroExtensionFn, Subtype.val_injective]

theorem zeroExtensionFn_eq_zero_of_not_mem
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) {x : ℝ}
    (hx : x ∉ LegendreScaledL2.Interval a) :
    zeroExtensionFn a w x = 0 := by
  rw [zeroExtensionFn, Function.extend_apply']
  rintro ⟨y, rfl⟩
  exact hx y.property

theorem indicator_zeroExtensionFn
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    (LegendreScaledL2.Interval a).indicator (zeroExtensionFn a w) =
      zeroExtensionFn a w := by
  funext x
  by_cases hx : x ∈ LegendreScaledL2.Interval a
  · simp [hx]
  · simp [hx, zeroExtensionFn_eq_zero_of_not_mem a w hx]

/-- Zero extension preserves membership in every `Lᵖ` class. -/
theorem zeroExtensionFn_memLp_of_memLp
    {p : ℝ≥0∞} (a : ℝ) (w : LegendreScaledL2.IntervalL2 a)
    (hw : MeasureTheory.MemLp
      (w : LegendreScaledL2.Interval a → ℝ) p
      (LegendreScaledL2.intervalMeasure a)) :
    MeasureTheory.MemLp (zeroExtensionFn a w) p
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  let s : Set ℝ := LegendreScaledL2.Interval a
  have hs : MeasurableSet s := measurableSet_Icc
  have hcoe : MeasurableEmbedding
      (fun x : s ↦ (x : ℝ)) :=
    MeasurableEmbedding.subtype_coe hs
  have hrestrict : MeasureTheory.MemLp (zeroExtensionFn a w) p
      ((MeasureTheory.volume : MeasureTheory.Measure ℝ).restrict s) := by
    rw [← map_comap_subtype_coe hs]
    rw [hcoe.memLp_map_measure_iff]
    have hwC : MeasureTheory.MemLp
        (fun x : LegendreScaledL2.Interval a ↦ ((w x : ℝ) : ℂ)) p
        (LegendreScaledL2.intervalMeasure a) :=
      hw.ofReal
    simpa [s, Function.comp_def, LegendreScaledL2.intervalMeasure] using hwC
  have hindicator : MeasureTheory.MemLp
      (s.indicator (zeroExtensionFn a w)) p
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    (MeasureTheory.memLp_indicator_iff_restrict hs).2 hrestrict
  simpa [s, indicator_zeroExtensionFn] using hindicator

/-- The zero extension is square-integrable on the real line. -/
theorem zeroExtensionFn_memLp
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    MeasureTheory.MemLp (zeroExtensionFn a w) 2
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
  zeroExtensionFn_memLp_of_memLp a w (MeasureTheory.Lp.memLp w)

/-- Compact support upgrades the interval `L²` vector's zero extension to
`L¹(ℝ)`. -/
theorem zeroExtensionFn_memLp_one
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    MeasureTheory.MemLp (zeroExtensionFn a w) 1
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  apply zeroExtensionFn_memLp_of_memLp a w
  rw [MeasureTheory.memLp_one_iff_integrable]
  exact (MeasureTheory.Lp.memLp w).integrable (by norm_num)

/-- The canonical full-line complex `L²` vector represented by the zero
extension. -/
noncomputable def zeroExtension
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) : FullLineComplexL2 :=
  (zeroExtensionFn_memLp a w).toLp (zeroExtensionFn a w)

theorem coeFn_zeroExtension
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    (zeroExtension a w : ℝ → ℂ) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      zeroExtensionFn a w :=
  (zeroExtensionFn_memLp a w).coeFn_toLp

/-- Exact norm preservation for zero extension (including the real-to-complex
scalar embedding). -/
theorem norm_zeroExtension
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    ‖zeroExtension a w‖ = ‖w‖ := by
  rw [zeroExtension, MeasureTheory.Lp.norm_toLp,
    MeasureTheory.Lp.norm_def]
  congr 1
  let s : Set ℝ := LegendreScaledL2.Interval a
  have hs : MeasurableSet s := measurableSet_Icc
  have hcoe : MeasurableEmbedding
      (fun x : s ↦ (x : ℝ)) :=
    MeasurableEmbedding.subtype_coe hs
  calc
    MeasureTheory.eLpNorm (zeroExtensionFn a w) 2
        (MeasureTheory.volume : MeasureTheory.Measure ℝ) =
        MeasureTheory.eLpNorm
          (s.indicator (zeroExtensionFn a w)) 2
          (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
      rw [indicator_zeroExtensionFn a w]
    _ = MeasureTheory.eLpNorm (zeroExtensionFn a w) 2
          ((MeasureTheory.volume : MeasureTheory.Measure ℝ).restrict s) :=
      MeasureTheory.eLpNorm_indicator_eq_eLpNorm_restrict hs
    _ = MeasureTheory.eLpNorm (zeroExtensionFn a w) 2
          (MeasureTheory.Measure.map (fun x : s ↦ (x : ℝ))
            (MeasureTheory.Measure.comap (fun x : s ↦ (x : ℝ))
              (MeasureTheory.volume : MeasureTheory.Measure ℝ))) := by
      rw [map_comap_subtype_coe hs]
    _ = MeasureTheory.eLpNorm
          (zeroExtensionFn a w ∘ (fun x : s ↦ (x : ℝ))) 2
          (MeasureTheory.Measure.comap (fun x : s ↦ (x : ℝ))
            (MeasureTheory.volume : MeasureTheory.Measure ℝ)) :=
      hcoe.eLpNorm_map_measure
    _ = MeasureTheory.eLpNorm (fun x : s ↦ (w x : ℝ)) 2
          (LegendreScaledL2.intervalMeasure a) := by
      apply MeasureTheory.eLpNorm_congr_norm_ae
      filter_upwards [] with x
      simp [s, LegendreScaledL2.intervalMeasure]
    _ = MeasureTheory.eLpNorm (w : s → ℝ) 2
          (LegendreScaledL2.intervalMeasure a) := rfl

private theorem zeroExtensionFn_add_ae
    (a : ℝ) (w v : LegendreScaledL2.IntervalL2 a) :
    zeroExtensionFn a (w + v) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      zeroExtensionFn a w + zeroExtensionFn a v := by
  let s : Set ℝ := LegendreScaledL2.Interval a
  have hs : MeasurableSet s := measurableSet_Icc
  apply MeasureTheory.ae_of_ae_restrict_of_ae_restrict_compl s
  · rw [ae_restrict_iff_subtype hs]
    filter_upwards [MeasureTheory.Lp.coeFn_add w v] with x hx
    simp only [zeroExtensionFn_coe, Pi.add_apply]
    rw [hx]
    simp
  · apply (MeasureTheory.ae_restrict_iff' hs.compl).2
    filter_upwards [] with x hx
    have hx' : x ∉ LegendreScaledL2.Interval a := hx
    simp [zeroExtensionFn_eq_zero_of_not_mem a (w + v) hx',
      zeroExtensionFn_eq_zero_of_not_mem a w hx',
      zeroExtensionFn_eq_zero_of_not_mem a v hx']

private theorem zeroExtensionFn_smul_ae
    (a c : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    zeroExtensionFn a (c • w) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      c • zeroExtensionFn a w := by
  let s : Set ℝ := LegendreScaledL2.Interval a
  have hs : MeasurableSet s := measurableSet_Icc
  apply MeasureTheory.ae_of_ae_restrict_of_ae_restrict_compl s
  · rw [ae_restrict_iff_subtype hs]
    filter_upwards [MeasureTheory.Lp.coeFn_smul c w] with x hx
    simp only [zeroExtensionFn_coe, Pi.smul_apply]
    rw [hx]
    simp
  · apply (MeasureTheory.ae_restrict_iff' hs.compl).2
    filter_upwards [] with x hx
    have hx' : x ∉ LegendreScaledL2.Interval a := hx
    simp [zeroExtensionFn_eq_zero_of_not_mem a (c • w) hx',
      zeroExtensionFn_eq_zero_of_not_mem a w hx']

theorem zeroExtension_add
    (a : ℝ) (w v : LegendreScaledL2.IntervalL2 a) :
    zeroExtension a (w + v) = zeroExtension a w + zeroExtension a v := by
  apply MeasureTheory.Lp.ext
  exact (coeFn_zeroExtension a (w + v)).trans <|
    (zeroExtensionFn_add_ae a w v).trans <|
      ((coeFn_zeroExtension a w).symm.add
        (coeFn_zeroExtension a v).symm).trans
          (MeasureTheory.Lp.coeFn_add (zeroExtension a w)
            (zeroExtension a v)).symm

theorem zeroExtension_smul
    (a c : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    zeroExtension a (c • w) = c • zeroExtension a w := by
  apply MeasureTheory.Lp.ext
  exact (coeFn_zeroExtension a (c • w)).trans <|
    (zeroExtensionFn_smul_ae a c w).trans <|
      ((coeFn_zeroExtension a w).symm.const_smul c).trans
        (MeasureTheory.Lp.coeFn_smul c (zeroExtension a w)).symm

/-- Zero extension as a real-linear map. -/
noncomputable def zeroExtensionLinearMap (a : ℝ) :
    LegendreScaledL2.IntervalL2 a →ₗ[ℝ] FullLineComplexL2 where
  toFun := zeroExtension a
  map_add' := zeroExtension_add a
  map_smul' := zeroExtension_smul a

@[simp] theorem zeroExtensionLinearMap_apply
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    zeroExtensionLinearMap a w = zeroExtension a w := rfl

/-- Canonical norm-preserving real-linear zero extension from interval `L²`
to complex `L²(ℝ)`. -/
noncomputable def zeroExtensionLI (a : ℝ) :
    LegendreScaledL2.IntervalL2 a →ₗᵢ[ℝ] FullLineComplexL2 where
  toLinearMap := zeroExtensionLinearMap a
  norm_map' := norm_zeroExtension a

@[simp] theorem zeroExtensionLI_apply
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    zeroExtensionLI a w = zeroExtension a w := rfl

/-! ## The pointwise `L¹` Fourier transform -/

/-- The same compactly supported function as a full-line `L¹` vector. -/
noncomputable def zeroExtensionL1
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    MeasureTheory.Lp ℂ 1 (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
  (zeroExtensionFn_memLp_one a w).toLp (zeroExtensionFn a w)

/-- Exact pointwise normalization bridge: the interval coefficient at angular
frequency `z` is Mathlib's `L¹` Fourier transform at ordinary frequency
`z / (2π)`. -/
theorem intervalFourierCoeff_eq_fourier_zeroExtensionFn
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (z : ℝ) :
    IntervalFourierL2.intervalFourierCoeff a w z =
      FourierTransform.fourier (zeroExtensionFn a w)
        (z / (2 * Real.pi)) := by
  rw [IntervalFourierL2.intervalFourierCoeff_eq_integral,
    Real.fourier_eq]
  let s : Set ℝ := LegendreScaledL2.Interval a
  have hs : MeasurableSet s := measurableSet_Icc
  calc
    (∫ x : LegendreScaledL2.Interval a,
        ((w x : ℝ) : ℂ) * LegendrePlaneWave.fourierPhase z (x : ℝ)
        ∂(LegendreScaledL2.intervalMeasure a)) =
        ∫ x : LegendreScaledL2.Interval a,
          zeroExtensionFn a w (x : ℝ) *
            LegendrePlaneWave.fourierPhase z (x : ℝ)
          ∂(LegendreScaledL2.intervalMeasure a) := by
      apply MeasureTheory.integral_congr_ae
      filter_upwards [] with x
      rw [zeroExtensionFn_coe]
    _ = ∫ x in s, zeroExtensionFn a w x *
          LegendrePlaneWave.fourierPhase z x := by
      rw [LegendreScaledL2.intervalMeasure]
      exact MeasureTheory.integral_subtype_comap
        (s := s) (μ := MeasureTheory.volume) hs
        (fun x : ℝ ↦ zeroExtensionFn a w x *
          LegendrePlaneWave.fourierPhase z x)
    _ = ∫ v : ℝ, Real.fourierChar
          (-inner ℝ v (z / (2 * Real.pi))) • zeroExtensionFn a w v := by
      rw [← MeasureTheory.integral_indicator hs]
      apply MeasureTheory.integral_congr_ae
      filter_upwards [] with x
      by_cases hx : x ∈ s
      · rw [Set.indicator_of_mem hx, Circle.smul_def,
          Real.fourierChar_apply, Real.inner_apply]
        unfold LegendrePlaneWave.fourierPhase
        have hpi : 2 * Real.pi ≠ 0 := by positivity
        have hscalar :
            2 * Real.pi * (-(x * (z / (2 * Real.pi)))) = -(z * x) := by
          field_simp
        have hexp :
            ((2 * Real.pi * (-(x * (z / (2 * Real.pi))) : ℝ) : ℝ) : ℂ) *
                Complex.I =
              (-((z : ℂ) * Complex.I)) * (x : ℂ) := by
          rw [hscalar]
          push_cast
          ring
        rw [hexp]
        ring
      · rw [Set.indicator_of_notMem hx,
          zeroExtensionFn_eq_zero_of_not_mem a w hx]
        simp

/-- The bounded-continuous `L¹` Fourier transform has the same exact
pointwise coefficient formula. -/
theorem intervalFourierCoeff_eq_fourierTransformL1
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (z : ℝ) :
    IntervalFourierL2.intervalFourierCoeff a w z =
      Real.Lp.fourierTransform (zeroExtensionL1 a w)
        (z / (2 * Real.pi)) := by
  rw [intervalFourierCoeff_eq_fourier_zeroExtensionFn]
  exact congrFun
    (Real.fourierTransform_toLp (zeroExtensionFn_memLp_one a w)).symm
    (z / (2 * Real.pi))

/-! ## The full-line `L²` Fourier transform -/

/-- Mathlib's Plancherel Fourier transform of the zero extension. -/
noncomputable def fourierZeroExtensionL2
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) : FullLineComplexL2 :=
  FourierTransform.fourier (zeroExtension a w)

/-- Plancherel plus zero-extension isometry: the full-line Fourier transform
has exactly the original interval norm. -/
theorem norm_fourierZeroExtensionL2
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    ‖fourierZeroExtensionL2 a w‖ = ‖w‖ := by
  rw [fourierZeroExtensionL2, MeasureTheory.Lp.norm_fourier_eq,
    norm_zeroExtension]

/-- The Plancherel `L²` transform agrees almost everywhere with the
pointwise `L¹` Fourier integral.  This is the standard `L¹ ∩ L²`
compatibility theorem, proved here from Mathlib's tempered-distribution
compatibility and Fourier--Fubini identity. -/
theorem coeFn_fourierZeroExtensionL2_ae_eq_fourierFn
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    (fourierZeroExtensionL2 a w : ℝ → ℂ) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      FourierTransform.fourier (zeroExtensionFn a w) := by
  apply ae_eq_of_integral_contDiff_smul_eq
  · exact (MeasureTheory.Lp.memLp (fourierZeroExtensionL2 a w)).locallyIntegrable
      (by norm_num)
  · have htop : MeasureTheory.MemLp
        (FourierTransform.fourier (zeroExtensionFn a w)) ∞
        (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
      rw [← Real.fourierTransform_toLp (zeroExtensionFn_memLp_one a w)]
      exact (Real.Lp.fourierTransform (zeroExtensionL1 a w)).memLp_top
    exact htop.locallyIntegrable le_top
  · intro g hg hsupp
    let gc : ℝ → ℂ := Complex.ofRealCLM ∘ g
    have hgcSupp : HasCompactSupport (Complex.ofRealCLM ∘ g) :=
      hsupp.comp_left rfl
    have hgcDiff : ContDiff ℝ ((⊤ : ℕ∞) : WithTop ℕ∞)
        (Complex.ofRealCLM ∘ g) := by
      have horder : ((⊤ : ℕ∞) : WithTop ℕ∞) ≤ ⊤ := le_top
      exact (Complex.ofRealCLM.contDiff.of_le horder).comp hg
    let φ : SchwartzMap ℝ ℂ := hgcSupp.toSchwartzMap hgcDiff
    have hdist := congrArg (fun T : SchwartzMap ℝ ℂ →L[ℂ] ℂ ↦ T φ)
      (MeasureTheory.Lp.fourier_toTemperedDistribution_eq (zeroExtension a w))
    have hdist' :
        (∫ x : ℝ, (FourierTransform.fourier φ) x •
            (zeroExtension a w : ℝ → ℂ) x) =
          ∫ x : ℝ, φ x • (fourierZeroExtensionL2 a w : ℝ → ℂ) x := by
      change
        (MeasureTheory.Lp.toTemperedDistribution (zeroExtension a w))
            (FourierTransform.fourier φ) =
          (MeasureTheory.Lp.toTemperedDistribution
            (FourierTransform.fourier (zeroExtension a w))) φ at hdist
      rw [MeasureTheory.Lp.toTemperedDistribution_apply,
        MeasureTheory.Lp.toTemperedDistribution_apply] at hdist
      simpa only [fourierZeroExtensionL2] using hdist
    have hdistFn :
        (∫ x : ℝ, (FourierTransform.fourier φ) x •
            zeroExtensionFn a w x) =
          ∫ x : ℝ, φ x • (fourierZeroExtensionL2 a w : ℝ → ℂ) x := by
      calc
        _ = ∫ x : ℝ, (FourierTransform.fourier φ) x •
              (zeroExtension a w : ℝ → ℂ) x := by
          apply MeasureTheory.integral_congr_ae
          filter_upwards [coeFn_zeroExtension a w] with x hx
          rw [hx]
        _ = _ := hdist'
    have hfub := VectorFourier.integral_fourierIntegral_smul_eq_flip
      (e := Real.fourierChar)
      (L := innerₗ ℝ)
      (μ := (MeasureTheory.volume : MeasureTheory.Measure ℝ))
      (ν := (MeasureTheory.volume : MeasureTheory.Measure ℝ))
      Real.continuous_fourierChar continuous_inner
      (MeasureTheory.memLp_one_iff_integrable.mp
        (zeroExtensionFn_memLp_one a w)) φ.integrable
    have hinnerFlip : (innerₗ ℝ).flip = innerₗ ℝ := by
      apply LinearMap.ext
      intro x
      apply LinearMap.ext
      intro y
      exact real_inner_comm x y
    rw [hinnerFlip] at hfub
    change
      (∫ ξ : ℝ, FourierTransform.fourier (zeroExtensionFn a w) ξ • φ ξ) =
        ∫ x : ℝ, zeroExtensionFn a w x •
          FourierTransform.fourier (φ : ℝ → ℂ) x at hfub
    have hfub' :
        (∫ x : ℝ, φ x •
            FourierTransform.fourier (zeroExtensionFn a w) x) =
          ∫ x : ℝ, (FourierTransform.fourier φ) x •
            zeroExtensionFn a w x := by
      simpa only [SchwartzMap.fourier_coe, smul_eq_mul, mul_comm] using hfub
    calc
      (∫ x : ℝ, g x • (fourierZeroExtensionL2 a w : ℝ → ℂ) x) =
          ∫ x : ℝ, φ x • (fourierZeroExtensionL2 a w : ℝ → ℂ) x := by
        apply MeasureTheory.integral_congr_ae
        filter_upwards [] with x
        rfl
      _ = ∫ x : ℝ, φ x •
            FourierTransform.fourier (zeroExtensionFn a w) x := by
        exact hdistFn.symm.trans hfub'.symm
      _ = ∫ x : ℝ, g x •
            FourierTransform.fourier (zeroExtensionFn a w) x := by
        apply MeasureTheory.integral_congr_ae
        filter_upwards [] with x
        rfl

/-- Almost-everywhere coefficient formula for Mathlib's `L²` transform in
ordinary frequency: `ξ` corresponds exactly to angular frequency `2πξ`. -/
theorem coeFn_fourierZeroExtensionL2_ae_eq_intervalFourierCoeff
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    (fourierZeroExtensionL2 a w : ℝ → ℂ) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      fun ξ ↦ IntervalFourierL2.intervalFourierCoeff a w
        (2 * Real.pi * ξ) := by
  filter_upwards [coeFn_fourierZeroExtensionL2_ae_eq_fourierFn a w] with ξ hξ
  rw [hξ]
  have hnorm : (2 * Real.pi * ξ) / (2 * Real.pi) = ξ := by
    field_simp [Real.pi_ne_zero]
  calc
    FourierTransform.fourier (zeroExtensionFn a w) ξ =
        FourierTransform.fourier (zeroExtensionFn a w)
          ((2 * Real.pi * ξ) / (2 * Real.pi)) := by rw [hnorm]
    _ = IntervalFourierL2.intervalFourierCoeff a w (2 * Real.pi * ξ) :=
      (intervalFourierCoeff_eq_fourier_zeroExtensionFn
        a w (2 * Real.pi * ξ)).symm

/-- The squared `L²` norm is the integral of the squared pointwise norm of
the selected representative. -/
theorem norm_sq_eq_integral_norm_sq (f : FullLineComplexL2) :
    ‖f‖ ^ 2 = ∫ x : ℝ, ‖(f : ℝ → ℂ) x‖ ^ 2 := by
  calc
    ‖f‖ ^ 2 = (inner ℂ f f).re := by
      exact @InnerProductSpace.norm_sq_eq_re_inner ℂ _ _ _ _ f
    _ = (∫ x : ℝ, inner ℂ ((f : ℝ → ℂ) x) ((f : ℝ → ℂ) x)).re := by
      rw [MeasureTheory.L2.inner_def]
    _ = ∫ x : ℝ,
          (inner ℂ ((f : ℝ → ℂ) x) ((f : ℝ → ℂ) x)).re := by
      exact (integral_re (𝕜 := ℂ)
        (MeasureTheory.L2.integrable_inner f f)).symm
    _ = ∫ x : ℝ, ‖(f : ℝ → ℂ) x‖ ^ 2 := by
      apply MeasureTheory.integral_congr_ae
      filter_upwards [] with x
      exact inner_self_eq_norm_sq (𝕜 := ℂ) ((f : ℝ → ℂ) x)

/-- Restrict a full-line `L²` vector to a symmetric ordinary-frequency
band. -/
noncomputable def restrictToBand
    (B : ℝ) (f : FullLineComplexL2) : FullLineComplexL2 :=
  (MeasureTheory.MemLp.indicator measurableSet_Icc
      (MeasureTheory.Lp.memLp f)).toLp
    ((Set.Icc (-B) B).indicator (fun ξ : ℝ ↦ f ξ))

theorem coeFn_restrictToBand
    (B : ℝ) (f : FullLineComplexL2) :
    (restrictToBand B f : ℝ → ℂ) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      (Set.Icc (-B) B).indicator (fun ξ : ℝ ↦ f ξ) :=
  (MeasureTheory.MemLp.indicator measurableSet_Icc
    (MeasureTheory.Lp.memLp f)).coeFn_toLp

/-- Restricting to a band cannot increase the `L²` norm. -/
theorem norm_restrictToBand_le
    (B : ℝ) (f : FullLineComplexL2) :
    ‖restrictToBand B f‖ ≤ ‖f‖ := by
  rw [restrictToBand, MeasureTheory.Lp.norm_toLp,
    MeasureTheory.Lp.norm_def]
  apply ENNReal.toReal_mono (MeasureTheory.Lp.eLpNorm_ne_top f)
  exact MeasureTheory.eLpNorm_indicator_le (f : ℝ → ℂ)

/-- For a nonnegative radius, the squared norm of band restriction is
exactly the interval integral of the squared pointwise norm. -/
theorem norm_restrictToBand_sq_eq_intervalIntegral
    (B : ℝ) (hB : 0 ≤ B) (f : FullLineComplexL2) :
    ‖restrictToBand B f‖ ^ 2 =
      ∫ ξ in -B..B, ‖(f : ℝ → ℂ) ξ‖ ^ 2 := by
  rw [norm_sq_eq_integral_norm_sq]
  calc
    (∫ ξ : ℝ, ‖(restrictToBand B f : ℝ → ℂ) ξ‖ ^ 2) =
        ∫ ξ : ℝ,
          ‖(Set.Icc (-B) B).indicator (fun x : ℝ ↦ f x) ξ‖ ^ 2 := by
      apply MeasureTheory.integral_congr_ae
      filter_upwards [coeFn_restrictToBand B f] with ξ hξ
      rw [hξ]
    _ = ∫ ξ in Set.Icc (-B) B, ‖(f : ℝ → ℂ) ξ‖ ^ 2 := by
      rw [← MeasureTheory.integral_indicator measurableSet_Icc]
      apply MeasureTheory.integral_congr_ae
      filter_upwards [] with ξ
      by_cases hξ : ξ ∈ Set.Icc (-B) B <;> simp [hξ]
    _ = ∫ ξ in -B..B, ‖(f : ℝ → ℂ) ξ‖ ^ 2 := by
      rw [intervalIntegral.integral_of_le (by linarith),
        ← MeasureTheory.integral_Icc_eq_integral_Ioc]

private theorem restrictToBand_add
    (B : ℝ) (f g : FullLineComplexL2) :
    restrictToBand B (f + g) = restrictToBand B f + restrictToBand B g := by
  apply MeasureTheory.Lp.ext
  filter_upwards [coeFn_restrictToBand B (f + g),
    coeFn_restrictToBand B f, coeFn_restrictToBand B g,
    MeasureTheory.Lp.coeFn_add f g,
    MeasureTheory.Lp.coeFn_add (restrictToBand B f) (restrictToBand B g)]
      with x hleft hf hg hfg hright
  rw [hleft, hright]
  by_cases hx : x ∈ Set.Icc (-B) B
  · simp only [Set.indicator_of_mem hx, Pi.add_apply]
    rw [hfg, hf, hg]
    simp [hx]
  · simp only [Set.indicator_of_notMem hx, Pi.add_apply]
    rw [hf, hg]
    simp [hx]

private theorem restrictToBand_smul
    (B : ℝ) (c : ℂ) (f : FullLineComplexL2) :
    restrictToBand B (c • f) = c • restrictToBand B f := by
  apply MeasureTheory.Lp.ext
  filter_upwards [coeFn_restrictToBand B (c • f),
    coeFn_restrictToBand B f,
    MeasureTheory.Lp.coeFn_smul c f,
    MeasureTheory.Lp.coeFn_smul c (restrictToBand B f)]
      with x hleft hf hcf hright
  rw [hleft, hright]
  by_cases hx : x ∈ Set.Icc (-B) B
  · simp only [Set.indicator_of_mem hx, Pi.smul_apply]
    rw [hcf, hf]
    simp [hx]
  · simp only [Set.indicator_of_notMem hx, Pi.smul_apply]
    rw [hf]
    simp [hx]

/-- Symmetric band restriction as a complex-linear contraction. -/
noncomputable def restrictToBandLinearMap (B : ℝ) :
    FullLineComplexL2 →ₗ[ℂ] FullLineComplexL2 where
  toFun := restrictToBand B
  map_add' := restrictToBand_add B
  map_smul' := restrictToBand_smul B

@[simp] theorem restrictToBandLinearMap_apply
    (B : ℝ) (f : FullLineComplexL2) :
    restrictToBandLinearMap B f = restrictToBand B f := rfl

/-- Symmetric band restriction as a continuous complex-linear contraction. -/
noncomputable def restrictToBandCLM (B : ℝ) :
    FullLineComplexL2 →L[ℂ] FullLineComplexL2 :=
  LinearMap.mkContinuous (restrictToBandLinearMap B) 1 (fun f ↦ by
    simpa using norm_restrictToBand_le B f)

@[simp] theorem restrictToBandCLM_apply
    (B : ℝ) (f : FullLineComplexL2) :
    restrictToBandCLM B f = restrictToBand B f := rfl

/-- The Plancherel Fourier transform of the zero extension, restricted to
the ordinary-frequency band corresponding to angular frequencies `[-b,b]`.
The radius is exactly `b / (2π)`. -/
noncomputable def angularFourierBandL2
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (b : ℝ) :
    FullLineComplexL2 :=
  restrictToBand (b / (2 * Real.pi)) (fourierZeroExtensionL2 a w)

/-- The interval-to-band operator itself, as a continuous real-linear map.
It is the composition of canonical zero extension, Mathlib's Plancherel
Fourier transform, and ordinary-frequency restriction to
`[-b/(2π),b/(2π)]`. -/
noncomputable def angularFourierBandCLM (a b : ℝ) :
    LegendreScaledL2.IntervalL2 a →L[ℝ] FullLineComplexL2 :=
  ((restrictToBandCLM (b / (2 * Real.pi))).restrictScalars ℝ).comp <|
    ((FourierTransform.fourierCLM ℂ FullLineComplexL2).restrictScalars ℝ).comp <|
      (zeroExtensionLI a).toContinuousLinearMap

@[simp] theorem angularFourierBandCLM_apply
    (a b : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    angularFourierBandCLM a b w = angularFourierBandL2 a w b := rfl

/-- Exact identification of the Hilbert norm of the Plancherel band
operator with the angular-frequency energy used by the Legendre leakage
ledger.  This includes both the `2π` change of variables and the
`L¹ ∩ L²` compatibility theorem above. -/
theorem norm_angularFourierBandL2_sq_eq_normalizedIntervalFourierBandEnergy
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a)
    (b : ℝ) (hb : 0 ≤ b) :
    ‖angularFourierBandL2 a w b‖ ^ 2 =
      IntervalFourierL2.normalizedIntervalFourierBandEnergy a w b := by
  have htwoPi : 2 * Real.pi ≠ 0 := by positivity
  have hB : 0 ≤ b / (2 * Real.pi) := div_nonneg hb (by positivity)
  rw [angularFourierBandL2,
    norm_restrictToBand_sq_eq_intervalIntegral _ hB]
  calc
    (∫ ξ in -(b / (2 * Real.pi))..b / (2 * Real.pi),
        ‖(fourierZeroExtensionL2 a w : ℝ → ℂ) ξ‖ ^ 2) =
        ∫ ξ in -(b / (2 * Real.pi))..b / (2 * Real.pi),
          ‖IntervalFourierL2.intervalFourierCoeff a w
            (2 * Real.pi * ξ)‖ ^ 2 := by
      apply intervalIntegral.integral_congr_ae
      filter_upwards [
        coeFn_fourierZeroExtensionL2_ae_eq_intervalFourierCoeff a w]
          with ξ hξ
      intro _hmem
      rw [hξ]
    _ = (1 / (2 * Real.pi)) *
        ∫ z in -b..b,
          ‖IntervalFourierL2.intervalFourierCoeff a w z‖ ^ 2 := by
      rw [intervalIntegral.integral_comp_mul_left
        (fun z : ℝ ↦ ‖IntervalFourierL2.intervalFourierCoeff a w z‖ ^ 2)
        htwoPi]
      congr 1
      · field_simp
      · field_simp
    _ = IntervalFourierL2.normalizedIntervalFourierBandEnergy a w b := rfl

theorem norm_angularFourierBandCLM_apply_sq_eq_normalizedIntervalFourierBandEnergy
    (a b : ℝ) (hb : 0 ≤ b)
    (w : LegendreScaledL2.IntervalL2 a) :
    ‖angularFourierBandCLM a b w‖ ^ 2 =
      IntervalFourierL2.normalizedIntervalFourierBandEnergy a w b := by
  rw [angularFourierBandCLM_apply]
  exact norm_angularFourierBandL2_sq_eq_normalizedIntervalFourierBandEnergy
    a w b hb

/-- The integrated Legendre estimate, transferred without loss to the
actual Plancherel band operator. -/
theorem norm_angularFourierBandCLM_apply_sq_le_of_mem_orthogonal
    (a : ℝ) (ha : 0 < a) (b : ℝ) (hb : 0 ≤ b) (m : ℕ)
    (w : LegendreScaledL2.IntervalL2 a)
    (hw : w ∈ (LegendreScaledL2.finiteLegendreSubspace a m)ᗮ)
    (hq : (a * b) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    ‖angularFourierBandCLM a b w‖ ^ 2 ≤
      ‖w‖ ^ 2 *
        LegendrePlaneWaveBand.fourierNormalizedBandLeakageMajorant a b m := by
  rw [norm_angularFourierBandCLM_apply_sq_eq_normalizedIntervalFourierBandEnergy
    a b hb w]
  exact
    IntervalFourierL2.normalizedIntervalFourierBandEnergy_le_of_mem_orthogonal
      a ha b hb m w hw hq

/-- The exact band-norm consequence of zero-extension isometry and
Plancherel. -/
theorem norm_angularFourierBandL2_le
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (b : ℝ) :
    ‖angularFourierBandL2 a w b‖ ≤ ‖w‖ := by
  exact (norm_restrictToBand_le _ _).trans_eq
    (norm_fourierZeroExtensionL2 a w)

theorem norm_angularFourierBandCLM_apply_le
    (a b : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    ‖angularFourierBandCLM a b w‖ ≤ ‖w‖ := by
  rw [angularFourierBandCLM_apply]
  exact norm_angularFourierBandL2_le a w b

theorem norm_angularFourierBandL2_sq_le
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (b : ℝ) :
    ‖angularFourierBandL2 a w b‖ ^ 2 ≤ ‖w‖ ^ 2 := by
  exact pow_le_pow_left₀ (norm_nonneg _) (norm_angularFourierBandL2_le a w b) 2

end IntervalZeroExtension
