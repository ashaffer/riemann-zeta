import RHBridge.GuinandWeilFormula

open scoped ENNReal InnerProductSpace RealInnerProductSpace Topology
open MeasureTheory

namespace RHP2Bridge.GuinandWeilFormula

noncomputable section

theorem test_integrable_bilateralLaplaceFn
    (a : ℝ) (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) :
    Integrable (fun x : ℝ ↦
      IntervalZeroExtension.zeroExtensionFn a f x * Complex.exp (s * x)) := by
  let C : ℝ := Real.exp (‖s‖ * |a|)
  have hmajorant : Integrable (fun x : ℝ ↦
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

theorem test_integrable_bilateralLaplace
    (a : ℝ) (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) :
    Integrable (fun x : ℝ ↦
      (IntervalZeroExtension.zeroExtension a f : ℝ → ℂ) x *
        Complex.exp (s * x)) := by
  apply (test_integrable_bilateralLaplaceFn a f s).congr
  filter_upwards [IntervalZeroExtension.coeFn_zeroExtension a f] with x hx
  rw [hx]

theorem test_bilateralLaplace_add
    (a : ℝ) (f g : GeneralZetaWeilForm.TestSpace a) (s : ℂ) :
    bilateralLaplace a (f + g) s =
      bilateralLaplace a f s + bilateralLaplace a g s := by
  unfold bilateralLaplace
  have hcoe :
      (IntervalZeroExtension.zeroExtension a (f + g) : ℝ → ℂ) =ᵐ[volume]
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
            apply integral_congr_ae
            filter_upwards [hcoe] with x hx
            rw [hx]
            ring
    _ = _ := integral_add (test_integrable_bilateralLaplace a f s)
      (test_integrable_bilateralLaplace a g s)

theorem test_bilateralLaplace_smul
    (a c : ℝ) (f : GeneralZetaWeilForm.TestSpace a) (s : ℂ) :
    bilateralLaplace a (c • f) s = c * bilateralLaplace a f s := by
  unfold bilateralLaplace
  have hcoe :
      (IntervalZeroExtension.zeroExtension a (c • f) : ℝ → ℂ) =ᵐ[volume]
        fun x ↦ c • (IntervalZeroExtension.zeroExtension a f : ℝ → ℂ) x := by
    rw [IntervalZeroExtension.zeroExtension_smul]
    exact MeasureTheory.Lp.coeFn_smul c _
  calc
    (∫ x : ℝ, (IntervalZeroExtension.zeroExtension a (c • f) : ℝ → ℂ) x *
        Complex.exp (s * x)) =
      ∫ x : ℝ, c * ((IntervalZeroExtension.zeroExtension a f : ℝ → ℂ) x *
        Complex.exp (s * x)) := by
          apply integral_congr_ae
          filter_upwards [hcoe] with x hx
          rw [hx, Complex.real_smul]
          ring
    _ = _ := by rw [integral_const_mul]

def testZeroCrossSummand (a : ℝ)
    (f g : GeneralZetaWeilForm.TestSpace a)
    (ρ : NontrivialZetaZero) : ℂ :=
  (zeroSummand a (f + g) ρ - zeroSummand a f ρ -
    zeroSummand a g ρ) / 2

theorem testZeroCrossSummand_smul
    (a c : ℝ) (f g : GeneralZetaWeilForm.TestSpace a)
    (ρ : NontrivialZetaZero) :
    testZeroCrossSummand a f (c • g) ρ =
      c * testZeroCrossSummand a f g ρ := by
  simp only [testZeroCrossSummand, zeroSummand,
    test_bilateralLaplace_add, test_bilateralLaplace_smul]
  push_cast
  ring

def testZeroCrossInDisk (R a : ℝ)
    (f g : GeneralZetaWeilForm.TestSpace a) : ℂ :=
  ∑ ρ ∈ nontrivialZerosInDisk R, testZeroCrossSummand a f g ρ

theorem testZeroCrossInDisk_eq (R a : ℝ)
    (f g : GeneralZetaWeilForm.TestSpace a) :
    testZeroCrossInDisk R a f g =
      (zeroSumInDisk R a (f + g) - zeroSumInDisk R a f -
        zeroSumInDisk R a g) / 2 := by
  unfold testZeroCrossInDisk testZeroCrossSummand zeroSumInDisk
  simp_rw [div_eq_mul_inv]
  rw [← Finset.sum_mul]
  simp only [Finset.sum_sub_distrib]

theorem testZeroCrossInDisk_smul (R a c : ℝ)
    (f g : GeneralZetaWeilForm.TestSpace a) :
    testZeroCrossInDisk R a f (c • g) =
      c * testZeroCrossInDisk R a f g := by
  unfold testZeroCrossInDisk
  simp_rw [testZeroCrossSummand_smul]
  rw [Finset.mul_sum]

end

end RHP2Bridge.GuinandWeilFormula
