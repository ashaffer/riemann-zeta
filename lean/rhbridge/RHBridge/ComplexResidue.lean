/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.SimplePole
import Mathlib.Analysis.Complex.HasPrimitives
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-!
# Rectangle formulas for finite simple poles

This file develops the rectangle-boundary machinery used to express the
integral of finitely many Cauchy kernels as a residue sum.  The standalone
principal-part removal and circle-integral API lives in `RHBridge.SimplePole`,
which this module imports so existing `RHBridge.ComplexResidue` clients retain
their declarations unchanged.
-/

namespace RHBridge.ComplexResidue

open Complex Metric Set
open Filter
open scoped Interval Topology

noncomputable section

/-- Signed integral over the boundary of the axis-aligned rectangle with
opposite corners `z` and `w`, in Mathlib's established interval convention.
It is positively oriented when `z.re < w.re` and `z.im < w.im`; reversing one
coordinate reverses the corresponding signed interval. -/
def rectBoundaryIntegral (f : ℂ → ℂ) (z w : ℂ) : ℂ :=
  (∫ x : ℝ in z.re..w.re, f (x + z.im * I)) -
    (∫ x : ℝ in z.re..w.re, f (x + w.im * I)) +
      I * (∫ y : ℝ in z.im..w.im, f (w.re + y * I)) -
        I * ∫ y : ℝ in z.im..w.im, f (z.re + y * I)

/-- `rectBoundaryIntegral` is the closed rectangle integral already represented
in Mathlib by the sum of the two opposite wedge integrals. This bridge lets
clients use the native `Complex.wedgeIntegral` API. -/
theorem rectBoundaryIntegral_eq_wedgeIntegral_add
    (f : ℂ → ℂ) (z w : ℂ) :
    rectBoundaryIntegral f z w =
      Complex.wedgeIntegral z w f + Complex.wedgeIntegral w z f := by
  simpa only [rectBoundaryIntegral, smul_eq_mul] using
    (Complex.wedgeIntegral_add_wedgeIntegral_eq z w f).symm

/-- Cauchy--Goursat for `rectBoundaryIntegral`. -/
theorem rectBoundaryIntegral_eq_zero_of_differentiableOn
    (f : ℂ → ℂ) (z w : ℂ)
    (hf : DifferentiableOn ℂ f
      ([[z.re, w.re]] ×ℂ [[z.im, w.im]])) :
    rectBoundaryIntegral f z w = 0 := by
  unfold rectBoundaryIntegral
  simpa only [smul_eq_mul] using
    Complex.integral_boundary_rect_eq_zero_of_differentiableOn f z w hf

/-- Integrability on each of the four parametrized rectangle edges. -/
def RectIntegrable (f : ℂ → ℂ) (z w : ℂ) : Prop :=
  IntervalIntegrable (fun x : ℝ ↦ f (x + z.im * I)) MeasureTheory.volume z.re w.re ∧
  IntervalIntegrable (fun x : ℝ ↦ f (x + w.im * I)) MeasureTheory.volume z.re w.re ∧
  IntervalIntegrable (fun y : ℝ ↦ f (w.re + y * I)) MeasureTheory.volume z.im w.im ∧
  IntervalIntegrable (fun y : ℝ ↦ f (z.re + y * I)) MeasureTheory.volume z.im w.im

/-- Continuity on the closed rectangle supplies integrability on all four
edges. -/
theorem rectIntegrable_of_continuousOn {f : ℂ → ℂ} {z w : ℂ}
    (hf : ContinuousOn f ([[z.re, w.re]] ×ℂ [[z.im, w.im]])) :
    RectIntegrable f z w := by
  unfold RectIntegrable
  constructor
  · apply (hf.comp (by fun_prop) ?_).intervalIntegrable
    intro x hx
    constructor
    · simpa [Complex.add_re, Complex.mul_re] using hx
    · norm_num [Complex.add_im, Complex.mul_im]
  constructor
  · apply (hf.comp (by fun_prop) ?_).intervalIntegrable
    intro x hx
    constructor
    · simpa [Complex.add_re, Complex.mul_re] using hx
    · norm_num [Complex.add_im, Complex.mul_im]
  constructor
  · apply (hf.comp (by fun_prop) ?_).intervalIntegrable
    intro y hy
    constructor
    · norm_num [Complex.add_re, Complex.mul_re]
    · simpa [Complex.add_im, Complex.mul_im] using hy
  · apply (hf.comp (by fun_prop) ?_).intervalIntegrable
    intro y hy
    constructor
    · norm_num [Complex.add_re, Complex.mul_re]
    · simpa [Complex.add_im, Complex.mul_im] using hy

/-- A Cauchy kernel whose pole lies strictly inside a rectangle is integrable
on all four boundary edges. -/
theorem sub_inv_rectIntegrable_of_mem_openRectangle
    (p : ℂ) {x₀ x₃ y₀ y₃ : ℝ}
    (hx₀ : x₀ < p.re) (hx₃ : p.re < x₃)
    (hy₀ : y₀ < p.im) (hy₃ : p.im < y₃) :
    RectIntegrable (fun z : ℂ ↦ (z - p)⁻¹)
      (x₀ + y₀ * I) (x₃ + y₃ * I) := by
  unfold RectIntegrable
  norm_num [Complex.mul_re, Complex.mul_im]
  constructor
  · apply Continuous.intervalIntegrable
    apply Continuous.inv₀
    · fun_prop
    · intro x h
      have him := congrArg Complex.im h
      norm_num [Complex.mul_im] at him
      linarith
  constructor
  · apply Continuous.intervalIntegrable
    apply Continuous.inv₀
    · fun_prop
    · intro x h
      have him := congrArg Complex.im h
      norm_num [Complex.mul_im] at him
      linarith
  constructor
  · apply Continuous.intervalIntegrable
    apply Continuous.inv₀
    · fun_prop
    · intro y h
      have hre := congrArg Complex.re h
      norm_num [Complex.mul_re] at hre
      linarith
  · apply Continuous.intervalIntegrable
    apply Continuous.inv₀
    · fun_prop
    · intro y h
      have hre := congrArg Complex.re h
      norm_num [Complex.mul_re] at hre
      linarith

/-- On a rectangle not containing `p`, the Cauchy kernel is integrable on the
boundary and its boundary integral vanishes. -/
theorem sub_inv_rectIntegrable_and_boundaryIntegral_eq_zero
    (p z w : ℂ)
    (hp : p ∉ ([[z.re, w.re]] ×ℂ [[z.im, w.im]])) :
    RectIntegrable (fun q : ℂ ↦ (q - p)⁻¹) z w ∧
      rectBoundaryIntegral (fun q : ℂ ↦ (q - p)⁻¹) z w = 0 := by
  have hne : ∀ q ∈ ([[z.re, w.re]] ×ℂ [[z.im, w.im]]), q - p ≠ 0 := by
    intro q hq hzero
    apply hp
    have : q = p := sub_eq_zero.mp hzero
    simpa [this] using hq
  have hc : ContinuousOn (fun q : ℂ ↦ (q - p)⁻¹)
      ([[z.re, w.re]] ×ℂ [[z.im, w.im]]) :=
    (continuousOn_id.sub continuousOn_const).inv₀ hne
  refine ⟨rectIntegrable_of_continuousOn hc, ?_⟩
  apply rectBoundaryIntegral_eq_zero_of_differentiableOn
  intro q hq
  have hd : DifferentiableAt ℂ (fun u : ℂ ↦ u - p) q := by fun_prop
  exact (hd.inv (hne q hq)).differentiableWithinAt

theorem RectIntegrable.add {f g : ℂ → ℂ} {z w : ℂ}
    (hf : RectIntegrable f z w) (hg : RectIntegrable g z w) :
    RectIntegrable (fun x ↦ f x + g x) z w :=
  ⟨hf.1.add hg.1, hf.2.1.add hg.2.1,
    hf.2.2.1.add hg.2.2.1, hf.2.2.2.add hg.2.2.2⟩

theorem RectIntegrable.const_mul {f : ℂ → ℂ} {z w : ℂ}
    (hf : RectIntegrable f z w) (a : ℂ) :
    RectIntegrable (fun q ↦ a * f q) z w :=
  ⟨hf.1.const_mul a, hf.2.1.const_mul a,
    hf.2.2.1.const_mul a, hf.2.2.2.const_mul a⟩

protected theorem RectIntegrable.fun_sum {ι : Type*} (s : Finset ι)
    {F : ι → ℂ → ℂ} {z w : ℂ}
    (hF : ∀ i ∈ s, RectIntegrable (F i) z w) :
    RectIntegrable (fun q ↦ ∑ i ∈ s, F i q) z w := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [RectIntegrable]
  | @insert a s ha ih =>
      simp only [Finset.sum_insert ha]
      exact (hF a (Finset.mem_insert_self a s)).add
        (ih fun i hi ↦ hF i (Finset.mem_insert_of_mem hi))

/-- Linearity of the rectangle boundary integral. -/
theorem rectBoundaryIntegral_add {f g : ℂ → ℂ} {z w : ℂ}
    (hf : RectIntegrable f z w) (hg : RectIntegrable g z w) :
    rectBoundaryIntegral (fun x ↦ f x + g x) z w =
      rectBoundaryIntegral f z w + rectBoundaryIntegral g z w := by
  unfold rectBoundaryIntegral
  rw [intervalIntegral.integral_add hf.1 hg.1,
    intervalIntegral.integral_add hf.2.1 hg.2.1,
    intervalIntegral.integral_add hf.2.2.1 hg.2.2.1,
    intervalIntegral.integral_add hf.2.2.2 hg.2.2.2]
  ring

theorem rectBoundaryIntegral_const_mul (a : ℂ) (f : ℂ → ℂ) (z w : ℂ) :
    rectBoundaryIntegral (fun q ↦ a * f q) z w =
      a * rectBoundaryIntegral f z w := by
  unfold rectBoundaryIntegral
  simp only [intervalIntegral.integral_const_mul]
  ring

theorem rectBoundaryIntegral_fun_sum {ι : Type*} (s : Finset ι)
    (F : ι → ℂ → ℂ) (z w : ℂ)
    (hF : ∀ i ∈ s, RectIntegrable (F i) z w) :
    rectBoundaryIntegral (fun q ↦ ∑ i ∈ s, F i q) z w =
      ∑ i ∈ s, rectBoundaryIntegral (F i) z w := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [rectBoundaryIntegral]
  | @insert a s ha ih =>
      simp only [Finset.sum_insert ha]
      rw [rectBoundaryIntegral_add
        (hF a (Finset.mem_insert_self a s))
        (RectIntegrable.fun_sum s fun i hi ↦
          hF i (Finset.mem_insert_of_mem hi))]
      rw [ih fun i hi ↦ hF i (Finset.mem_insert_of_mem hi)]

/-- Splitting a rectangle by a vertical line: the new internal vertical edges
occur with opposite orientations and cancel. -/
theorem rectBoundaryIntegral_split_vertical
    (f : ℂ → ℂ) (z w : ℂ) (m : ℝ)
    (hleft : RectIntegrable f z (m + w.im * I))
    (hright : RectIntegrable f (m + z.im * I) w) :
    rectBoundaryIntegral f z w =
      rectBoundaryIntegral f z (m + w.im * I) +
        rectBoundaryIntegral f (m + z.im * I) w := by
  unfold rectBoundaryIntegral
  norm_num [RectIntegrable, Complex.mul_re, Complex.mul_im] at hleft hright ⊢
  rw [← intervalIntegral.integral_add_adjacent_intervals
      hleft.1 hright.1,
    ← intervalIntegral.integral_add_adjacent_intervals
      hleft.2.1 hright.2.1]
  ring

/-- Splitting a rectangle by a horizontal line. -/
theorem rectBoundaryIntegral_split_horizontal
    (f : ℂ → ℂ) (z w : ℂ) (n : ℝ)
    (hbottom : RectIntegrable f z (w.re + n * I))
    (htop : RectIntegrable f (z.re + n * I) w) :
    rectBoundaryIntegral f z w =
      rectBoundaryIntegral f z (w.re + n * I) +
        rectBoundaryIntegral f (z.re + n * I) w := by
  unfold rectBoundaryIntegral
  norm_num [RectIntegrable, Complex.mul_re, Complex.mul_im] at hbottom htop ⊢
  rw [← intervalIntegral.integral_add_adjacent_intervals
      hbottom.2.2.1 htop.2.2.1,
    ← intervalIntegral.integral_add_adjacent_intervals
      hbottom.2.2.2 htop.2.2.2]
  ring

theorem RectIntegrable.glue_vertical
    {f : ℂ → ℂ} {z w : ℂ} {m : ℝ}
    (hleft : RectIntegrable f z (m + w.im * I))
    (hright : RectIntegrable f (m + z.im * I) w) :
    RectIntegrable f z w := by
  norm_num [RectIntegrable, Complex.mul_re, Complex.mul_im] at hleft hright ⊢
  exact ⟨hleft.1.trans hright.1, hleft.2.1.trans hright.2.1,
    hright.2.2.1, hleft.2.2.2⟩

theorem RectIntegrable.glue_horizontal
    {f : ℂ → ℂ} {z w : ℂ} {n : ℝ}
    (hbottom : RectIntegrable f z (w.re + n * I))
    (htop : RectIntegrable f (z.re + n * I) w) :
    RectIntegrable f z w := by
  norm_num [RectIntegrable, Complex.mul_re, Complex.mul_im] at hbottom htop ⊢
  exact ⟨hbottom.1, htop.2.1, hbottom.2.2.1.trans htop.2.2.1,
    hbottom.2.2.2.trans htop.2.2.2⟩

/-- Three-cell vertical subdivision. -/
theorem rectBoundaryIntegral_split_vertical_three
    (f : ℂ → ℂ) (z w : ℂ) (m n : ℝ)
    (h₁ : RectIntegrable f z (m + w.im * I))
    (h₂ : RectIntegrable f (m + z.im * I) (n + w.im * I))
    (h₃ : RectIntegrable f (n + z.im * I) w) :
    rectBoundaryIntegral f z w =
      rectBoundaryIntegral f z (m + w.im * I) +
      rectBoundaryIntegral f (m + z.im * I) (n + w.im * I) +
      rectBoundaryIntegral f (n + z.im * I) w := by
  have h₁₂ : RectIntegrable f z (n + w.im * I) :=
    RectIntegrable.glue_vertical (z := z) (w := n + w.im * I)
      (m := m) (by simpa [Complex.mul_re, Complex.mul_im] using h₁)
      (by simpa [Complex.mul_re, Complex.mul_im] using h₂)
  rw [rectBoundaryIntegral_split_vertical f z w n h₁₂ h₃]
  rw [rectBoundaryIntegral_split_vertical f z (n + w.im * I) m]
  · norm_num [Complex.mul_re, Complex.mul_im]
  · simpa [Complex.mul_re, Complex.mul_im] using h₁
  · simpa [Complex.mul_re, Complex.mul_im] using h₂

/-- Three-cell horizontal subdivision. -/
theorem rectBoundaryIntegral_split_horizontal_three
    (f : ℂ → ℂ) (z w : ℂ) (m n : ℝ)
    (h₁ : RectIntegrable f z (w.re + m * I))
    (h₂ : RectIntegrable f (z.re + m * I) (w.re + n * I))
    (h₃ : RectIntegrable f (z.re + n * I) w) :
    rectBoundaryIntegral f z w =
      rectBoundaryIntegral f z (w.re + m * I) +
      rectBoundaryIntegral f (z.re + m * I) (w.re + n * I) +
      rectBoundaryIntegral f (z.re + n * I) w := by
  have h₁₂ : RectIntegrable f z (w.re + n * I) :=
    RectIntegrable.glue_horizontal (z := z) (w := w.re + n * I)
      (n := m) (by simpa [Complex.mul_re, Complex.mul_im] using h₁)
      (by simpa [Complex.mul_re, Complex.mul_im] using h₂)
  rw [rectBoundaryIntegral_split_horizontal f z w n h₁₂ h₃]
  rw [rectBoundaryIntegral_split_horizontal f z (w.re + n * I) m]
  · norm_num [Complex.mul_re, Complex.mul_im]
  · simpa [Complex.mul_re, Complex.mul_im] using h₁
  · simpa [Complex.mul_re, Complex.mul_im] using h₂

/-- A `3 × 3` rectangular frame decomposition.  If the boundary integrals on
the eight frame cells vanish, the outer boundary integral equals the central
cell boundary integral. -/
theorem rectBoundaryIntegral_eq_center_of_three_by_three_frame
    (f : ℂ → ℂ) (x₀ x₁ x₂ x₃ y₀ y₁ y₂ y₃ : ℝ)
    (h00 : RectIntegrable f (x₀ + y₀ * I) (x₁ + y₁ * I))
    (h10 : RectIntegrable f (x₁ + y₀ * I) (x₂ + y₁ * I))
    (h20 : RectIntegrable f (x₂ + y₀ * I) (x₃ + y₁ * I))
    (h01 : RectIntegrable f (x₀ + y₁ * I) (x₁ + y₂ * I))
    (h11 : RectIntegrable f (x₁ + y₁ * I) (x₂ + y₂ * I))
    (h21 : RectIntegrable f (x₂ + y₁ * I) (x₃ + y₂ * I))
    (h02 : RectIntegrable f (x₀ + y₂ * I) (x₁ + y₃ * I))
    (h12 : RectIntegrable f (x₁ + y₂ * I) (x₂ + y₃ * I))
    (h22 : RectIntegrable f (x₂ + y₂ * I) (x₃ + y₃ * I))
    (hz00 : rectBoundaryIntegral f (x₀ + y₀ * I) (x₁ + y₁ * I) = 0)
    (hz10 : rectBoundaryIntegral f (x₁ + y₀ * I) (x₂ + y₁ * I) = 0)
    (hz20 : rectBoundaryIntegral f (x₂ + y₀ * I) (x₃ + y₁ * I) = 0)
    (hz01 : rectBoundaryIntegral f (x₀ + y₁ * I) (x₁ + y₂ * I) = 0)
    (hz21 : rectBoundaryIntegral f (x₂ + y₁ * I) (x₃ + y₂ * I) = 0)
    (hz02 : rectBoundaryIntegral f (x₀ + y₂ * I) (x₁ + y₃ * I) = 0)
    (hz12 : rectBoundaryIntegral f (x₁ + y₂ * I) (x₂ + y₃ * I) = 0)
    (hz22 : rectBoundaryIntegral f (x₂ + y₂ * I) (x₃ + y₃ * I) = 0) :
    rectBoundaryIntegral f (x₀ + y₀ * I) (x₃ + y₃ * I) =
      rectBoundaryIntegral f (x₁ + y₁ * I) (x₂ + y₂ * I) := by
  have hb := rectBoundaryIntegral_split_vertical_three f
    (x₀ + y₀ * I) (x₃ + y₁ * I) x₁ x₂
      (by simpa [Complex.mul_re, Complex.mul_im] using h00)
      (by simpa [Complex.mul_re, Complex.mul_im] using h10)
      (by simpa [Complex.mul_re, Complex.mul_im] using h20)
  have hm := rectBoundaryIntegral_split_vertical_three f
    (x₀ + y₁ * I) (x₃ + y₂ * I) x₁ x₂
      (by simpa [Complex.mul_re, Complex.mul_im] using h01)
      (by simpa [Complex.mul_re, Complex.mul_im] using h11)
      (by simpa [Complex.mul_re, Complex.mul_im] using h21)
  have ht := rectBoundaryIntegral_split_vertical_three f
    (x₀ + y₂ * I) (x₃ + y₃ * I) x₁ x₂
      (by simpa [Complex.mul_re, Complex.mul_im] using h02)
      (by simpa [Complex.mul_re, Complex.mul_im] using h12)
      (by simpa [Complex.mul_re, Complex.mul_im] using h22)
  have hb01 : RectIntegrable f (x₀ + y₀ * I) (x₂ + y₁ * I) :=
    RectIntegrable.glue_vertical (z := x₀ + y₀ * I)
      (w := x₂ + y₁ * I) (m := x₁)
      (by simpa [Complex.mul_re, Complex.mul_im] using h00)
      (by simpa [Complex.mul_re, Complex.mul_im] using h10)
  have hbInt : RectIntegrable f (x₀ + y₀ * I) (x₃ + y₁ * I) :=
    RectIntegrable.glue_vertical (z := x₀ + y₀ * I)
      (w := x₃ + y₁ * I) (m := x₂)
      (by simpa [Complex.mul_re, Complex.mul_im] using hb01)
      (by simpa [Complex.mul_re, Complex.mul_im] using h20)
  have hm01 : RectIntegrable f (x₀ + y₁ * I) (x₂ + y₂ * I) :=
    RectIntegrable.glue_vertical (z := x₀ + y₁ * I)
      (w := x₂ + y₂ * I) (m := x₁)
      (by simpa [Complex.mul_re, Complex.mul_im] using h01)
      (by simpa [Complex.mul_re, Complex.mul_im] using h11)
  have hmInt : RectIntegrable f (x₀ + y₁ * I) (x₃ + y₂ * I) :=
    RectIntegrable.glue_vertical (z := x₀ + y₁ * I)
      (w := x₃ + y₂ * I) (m := x₂)
      (by simpa [Complex.mul_re, Complex.mul_im] using hm01)
      (by simpa [Complex.mul_re, Complex.mul_im] using h21)
  have ht01 : RectIntegrable f (x₀ + y₂ * I) (x₂ + y₃ * I) :=
    RectIntegrable.glue_vertical (z := x₀ + y₂ * I)
      (w := x₂ + y₃ * I) (m := x₁)
      (by simpa [Complex.mul_re, Complex.mul_im] using h02)
      (by simpa [Complex.mul_re, Complex.mul_im] using h12)
  have htInt : RectIntegrable f (x₀ + y₂ * I) (x₃ + y₃ * I) :=
    RectIntegrable.glue_vertical (z := x₀ + y₂ * I)
      (w := x₃ + y₃ * I) (m := x₂)
      (by simpa [Complex.mul_re, Complex.mul_im] using ht01)
      (by simpa [Complex.mul_re, Complex.mul_im] using h22)
  have hall := rectBoundaryIntegral_split_horizontal_three f
    (x₀ + y₀ * I) (x₃ + y₃ * I) y₁ y₂
      (by simpa [Complex.mul_re, Complex.mul_im] using hbInt)
      (by simpa [Complex.mul_re, Complex.mul_im] using hmInt)
      (by simpa [Complex.mul_re, Complex.mul_im] using htInt)
  norm_num [Complex.mul_re, Complex.mul_im] at hb hm ht hall
  rw [hall, hb, hm, ht, hz00, hz10, hz20, hz01, hz21, hz02, hz12, hz22]
  ring

/-- Translation invariance of the rectangle boundary integral. -/
theorem rectBoundaryIntegral_comp_sub_translation
    (f : ℂ → ℂ) (z w p : ℂ) :
    rectBoundaryIntegral (fun q ↦ f (q - p)) (z + p) (w + p) =
      rectBoundaryIntegral f z w := by
  unfold rectBoundaryIntegral
  norm_num [Complex.add_re, Complex.add_im, Complex.mul_re, Complex.mul_im]
  have hb : (fun x : ℝ ↦ f (x + (z.im + p.im) * I - p)) =
      fun x ↦ f (((x - p.re : ℝ) : ℂ) + z.im * I) := by
    funext x
    congr 1
    apply Complex.ext <;> norm_num [Complex.mul_re, Complex.mul_im]
  have ht : (fun x : ℝ ↦ f (x + (w.im + p.im) * I - p)) =
      fun x ↦ f (((x - p.re : ℝ) : ℂ) + w.im * I) := by
    funext x
    congr 1
    apply Complex.ext <;> norm_num [Complex.mul_re, Complex.mul_im]
  have hr : (fun y : ℝ ↦ f (w.re + p.re + y * I - p)) =
      fun y ↦ f (w.re + ((y - p.im : ℝ) : ℂ) * I) := by
    funext y
    congr 1
    apply Complex.ext <;> norm_num [Complex.mul_re, Complex.mul_im]
  have hl : (fun y : ℝ ↦ f (z.re + p.re + y * I - p)) =
      fun y ↦ f (z.re + ((y - p.im : ℝ) : ℂ) * I) := by
    funext y
    congr 1
    apply Complex.ext <;> norm_num [Complex.mul_re, Complex.mul_im]
  rw [hb, ht, hr, hl]
  have ib : (∫ x : ℝ in z.re + p.re..w.re + p.re,
      f (((x - p.re : ℝ) : ℂ) + z.im * I)) =
      ∫ x : ℝ in z.re..w.re, f (x + z.im * I) := by
    convert intervalIntegral.integral_comp_sub_right
      (fun x : ℝ ↦ f (x + z.im * I)) p.re using 1
    all_goals ring_nf
  have it : (∫ x : ℝ in z.re + p.re..w.re + p.re,
      f (((x - p.re : ℝ) : ℂ) + w.im * I)) =
      ∫ x : ℝ in z.re..w.re, f (x + w.im * I) := by
    convert intervalIntegral.integral_comp_sub_right
      (fun x : ℝ ↦ f (x + w.im * I)) p.re using 1
    all_goals ring_nf
  have ir : (∫ y : ℝ in z.im + p.im..w.im + p.im,
      f (w.re + ((y - p.im : ℝ) : ℂ) * I)) =
      ∫ y : ℝ in z.im..w.im, f (w.re + y * I) := by
    convert intervalIntegral.integral_comp_sub_right
      (fun y : ℝ ↦ f (w.re + y * I)) p.im using 1
    all_goals ring_nf
  have il : (∫ y : ℝ in z.im + p.im..w.im + p.im,
      f (z.re + ((y - p.im : ℝ) : ℂ) * I)) =
      ∫ y : ℝ in z.im..w.im, f (z.re + y * I) := by
    convert intervalIntegral.integral_comp_sub_right
      (fun y : ℝ ↦ f (z.re + y * I)) p.im using 1
    all_goals ring_nf
  rw [ib, it, ir, il]

/-- The normalized kernel integral on a centered square. -/
theorem rectBoundaryIntegral_inv_centeredSquare
    {r : ℝ} (hr : 0 < r) :
    rectBoundaryIntegral (fun z : ℂ ↦ z⁻¹)
      ((-r : ℂ) - r * I) (r + r * I) = 2 * Real.pi * I := by
  unfold rectBoundaryIntegral
  norm_num [Complex.mul_re, Complex.mul_im]
  have hminus : IntervalIntegrable
      (fun x : ℝ ↦ ((x : ℂ) + -(r * I))⁻¹) MeasureTheory.volume (-r) r := by
    apply Continuous.intervalIntegrable
    apply Continuous.inv₀
    · fun_prop
    · intro x hx
      have him := congrArg Complex.im hx
      norm_num [Complex.mul_im] at him
      linarith
  have hplus : IntervalIntegrable
      (fun x : ℝ ↦ ((x : ℂ) + r * I)⁻¹) MeasureTheory.volume (-r) r := by
    apply Continuous.intervalIntegrable
    apply Continuous.inv₀
    · fun_prop
    · intro x hx
      have him := congrArg Complex.im hx
      norm_num [Complex.mul_im] at him
      linarith
  have hright : IntervalIntegrable
      (fun y : ℝ ↦ ((r : ℂ) + y * I)⁻¹) MeasureTheory.volume (-r) r := by
    apply Continuous.intervalIntegrable
    apply Continuous.inv₀
    · fun_prop
    · intro y hy
      have hre := congrArg Complex.re hy
      norm_num [Complex.mul_re] at hre
      linarith
  have hleft : IntervalIntegrable
      (fun y : ℝ ↦ (-(r : ℂ) + y * I)⁻¹) MeasureTheory.volume (-r) r := by
    apply Continuous.intervalIntegrable
    apply Continuous.inv₀
    · fun_prop
    · intro y hy
      have hre := congrArg Complex.re hy
      norm_num [Complex.mul_re] at hre
      linarith
  rw [← intervalIntegral.integral_sub hminus hplus]
  rw [sub_eq_add_neg, add_assoc]
  rw [← sub_eq_add_neg
    (I * (∫ y : ℝ in -r..r, ((r : ℂ) + y * I)⁻¹))
    (I * (∫ y : ℝ in -r..r, (-(r : ℂ) + y * I)⁻¹))]
  rw [← mul_sub]
  rw [← intervalIntegral.integral_sub hright hleft]
  have hhorizontal : (fun x : ℝ ↦
      ((x : ℂ) + -(r * I))⁻¹ - ((x : ℂ) + r * I)⁻¹) =
      fun x ↦ (2 * r * I) * ((r ^ 2 + x ^ 2 : ℝ)⁻¹ : ℂ) := by
    funext x
    have hd : (r ^ 2 + x ^ 2 : ℝ) ≠ 0 := by nlinarith [sq_nonneg x]
    have hdc : ((r ^ 2 + x ^ 2 : ℝ) : ℂ) ≠ 0 := by exact_mod_cast hd
    have hm : (x : ℂ) - r * I ≠ 0 := by
      intro h
      have hi := congrArg Complex.im h
      norm_num [Complex.mul_im] at hi
      linarith
    have hp : (x : ℂ) + r * I ≠ 0 := by
      intro h
      have hi := congrArg Complex.im h
      norm_num [Complex.mul_im] at hi
      linarith
    push_cast
    change ((x : ℂ) - r * I)⁻¹ - ((x : ℂ) + r * I)⁻¹ = _
    rw [inv_sub_inv hm hp]
    field_simp [hdc]
    ring_nf
    simp only [show I ^ 3 = -I by norm_num]
    have hsum : (r : ℂ) ^ 2 + (x : ℂ) ^ 2 ≠ 0 := by
      exact_mod_cast hd
    symm
    calc
      _ = ((r : ℂ) * I * 2) * ((r : ℂ) ^ 2 + (x : ℂ) ^ 2) *
          ((r : ℂ) ^ 2 + (x : ℂ) ^ 2)⁻¹ := by ring
      _ = (r : ℂ) * I * 2 := by
        rw [mul_assoc, mul_inv_cancel₀ hsum, mul_one]
  have hvertical : (fun y : ℝ ↦
      ((r : ℂ) + y * I)⁻¹ - (-(r : ℂ) + y * I)⁻¹) =
      fun y ↦ (2 * r : ℂ) * ((r ^ 2 + y ^ 2 : ℝ)⁻¹ : ℂ) := by
    funext y
    have hd : (r ^ 2 + y ^ 2 : ℝ) ≠ 0 := by nlinarith [sq_nonneg y]
    have hdc : ((r ^ 2 + y ^ 2 : ℝ) : ℂ) ≠ 0 := by exact_mod_cast hd
    have hp : (r : ℂ) + y * I ≠ 0 := by
      intro h
      have hre := congrArg Complex.re h
      norm_num [Complex.mul_re] at hre
      linarith
    have hm : -(r : ℂ) + y * I ≠ 0 := by
      intro h
      have hre := congrArg Complex.re h
      norm_num [Complex.mul_re] at hre
      linarith
    push_cast
    rw [inv_sub_inv hp hm]
    field_simp [hdc]
    ring_nf
    rw [Complex.I_sq]
    have hsum : (r : ℂ) ^ 2 + (y : ℂ) ^ 2 ≠ 0 := by
      exact_mod_cast hd
    field_simp [hsum]
    ring
  rw [hhorizontal, hvertical]
  have hJ : (∫ x : ℝ in -r..r, (r ^ 2 + x ^ 2)⁻¹) =
      Real.pi / (2 * r) := by
    rw [integral_inv_sq_add_sq hr.ne']
    rw [div_self hr.ne', neg_div, div_self hr.ne', Real.arctan_one,
      Real.arctan_neg, Real.arctan_one]
    field_simp
    ring
  simp_rw [show ∀ x : ℝ,
      ((r ^ 2 + x ^ 2 : ℝ) : ℂ)⁻¹ =
        (((r ^ 2 + x ^ 2)⁻¹ : ℝ) : ℂ) by
      intro x
      exact (Complex.ofReal_inv _).symm]
  rw [intervalIntegral.integral_const_mul,
    intervalIntegral.integral_const_mul]
  rw [intervalIntegral.integral_ofReal]
  rw [hJ]
  push_cast
  have hrc : (r : ℂ) ≠ 0 := by exact_mod_cast hr.ne'
  field_simp [hrc]
  ring

/-- The kernel integral on a square centered at an arbitrary pole. -/
theorem rectBoundaryIntegral_sub_inv_centeredSquare
    (p : ℂ) {r : ℝ} (hr : 0 < r) :
    rectBoundaryIntegral (fun z : ℂ ↦ (z - p)⁻¹)
      (p + ((-r : ℂ) - r * I)) (p + (r + r * I)) =
        2 * Real.pi * I := by
  calc
    _ = rectBoundaryIntegral (fun z : ℂ ↦ z⁻¹)
        ((-r : ℂ) - r * I) (r + r * I) := by
      simpa only [add_comm] using
        rectBoundaryIntegral_comp_sub_translation (fun z : ℂ ↦ z⁻¹)
          ((-r : ℂ) - r * I) (r + r * I) p
    _ = _ := rectBoundaryIntegral_inv_centeredSquare hr

/-- Rectangle residue theorem for one simple Cauchy kernel.  The positive
number `r` selects a square around the pole lying strictly inside the outer
rectangle. -/
theorem rectBoundaryIntegral_sub_inv
    (p : ℂ) {x₀ x₃ y₀ y₃ r : ℝ} (hr : 0 < r)
    (hx₀ : x₀ < p.re - r) (hx₃ : p.re + r < x₃)
    (hy₀ : y₀ < p.im - r) (hy₃ : p.im + r < y₃) :
    rectBoundaryIntegral (fun z : ℂ ↦ (z - p)⁻¹)
      (x₀ + y₀ * I) (x₃ + y₃ * I) = 2 * Real.pi * I := by
  let k : ℂ → ℂ := fun z ↦ (z - p)⁻¹
  let x₁ := p.re - r
  let x₂ := p.re + r
  let y₁ := p.im - r
  let y₂ := p.im + r
  have hx01 : x₀ ≤ x₁ := hx₀.le
  have hx12 : x₁ ≤ x₂ := by dsimp [x₁, x₂]; linarith
  have hx23 : x₂ ≤ x₃ := hx₃.le
  have hy01 : y₀ ≤ y₁ := hy₀.le
  have hy12 : y₁ ≤ y₂ := by dsimp [y₁, y₂]; linarith
  have hy23 : y₂ ≤ y₃ := hy₃.le
  have bottom (a b : ℝ) (hab : a ≤ b) :
      RectIntegrable k (a + y₀ * I) (b + y₁ * I) ∧
        rectBoundaryIntegral k (a + y₀ * I) (b + y₁ * I) = 0 := by
    apply sub_inv_rectIntegrable_and_boundaryIntegral_eq_zero
    intro hmem
    norm_num [Complex.mul_re, Complex.mul_im] at hmem
    rw [uIcc_of_le hy01] at hmem
    exact (not_le_of_gt (by dsimp [y₁]; linarith)) hmem.2.2
  have top (a b : ℝ) (hab : a ≤ b) :
      RectIntegrable k (a + y₂ * I) (b + y₃ * I) ∧
        rectBoundaryIntegral k (a + y₂ * I) (b + y₃ * I) = 0 := by
    apply sub_inv_rectIntegrable_and_boundaryIntegral_eq_zero
    intro hmem
    norm_num [Complex.mul_re, Complex.mul_im] at hmem
    rw [uIcc_of_le hy23] at hmem
    exact (not_le_of_gt (by dsimp [y₂]; linarith)) hmem.2.1
  have left : RectIntegrable k (x₀ + y₁ * I) (x₁ + y₂ * I) ∧
      rectBoundaryIntegral k (x₀ + y₁ * I) (x₁ + y₂ * I) = 0 := by
    apply sub_inv_rectIntegrable_and_boundaryIntegral_eq_zero
    intro hmem
    norm_num [Complex.mul_re, Complex.mul_im] at hmem
    rw [uIcc_of_le hx01] at hmem
    exact (not_le_of_gt (by dsimp [x₁]; linarith)) hmem.1.2
  have right : RectIntegrable k (x₂ + y₁ * I) (x₃ + y₂ * I) ∧
      rectBoundaryIntegral k (x₂ + y₁ * I) (x₃ + y₂ * I) = 0 := by
    apply sub_inv_rectIntegrable_and_boundaryIntegral_eq_zero
    intro hmem
    norm_num [Complex.mul_re, Complex.mul_im] at hmem
    rw [uIcc_of_le hx23] at hmem
    exact (not_le_of_gt (by dsimp [x₂]; linarith)) hmem.1.1
  have d00 := bottom x₀ x₁ hx01
  have d10 := bottom x₁ x₂ hx12
  have d20 := bottom x₂ x₃ hx23
  have d02 := top x₀ x₁ hx01
  have d12 := top x₁ x₂ hx12
  have d22 := top x₂ x₃ hx23
  have hcenter : RectIntegrable k (x₁ + y₁ * I) (x₂ + y₂ * I) := by
    norm_num [RectIntegrable, Complex.mul_re, Complex.mul_im] at d10 d12 right left ⊢
    exact ⟨d10.1.2.1, d12.1.1, right.1.2.2.2, left.1.2.2.1⟩
  have hframe := rectBoundaryIntegral_eq_center_of_three_by_three_frame
    k x₀ x₁ x₂ x₃ y₀ y₁ y₂ y₃
    d00.1 d10.1 d20.1 left.1 hcenter right.1 d02.1 d12.1 d22.1
    d00.2 d10.2 d20.2 left.2 right.2 d02.2 d12.2 d22.2
  rw [hframe]
  have hsq := rectBoundaryIntegral_sub_inv_centeredSquare p hr
  change rectBoundaryIntegral (fun z : ℂ ↦ (z - p)⁻¹)
    (x₁ + y₁ * I) (x₂ + y₂ * I) = 2 * Real.pi * I
  have hc₁ : (x₁ + y₁ * I : ℂ) = p + ((-r : ℂ) - r * I) := by
    apply Complex.ext <;>
      norm_num [x₁, y₁, Complex.mul_re, Complex.mul_im] <;> ring
  have hc₂ : (x₂ + y₂ * I : ℂ) = p + ((r : ℂ) + r * I) := by
    apply Complex.ext <;>
      norm_num [x₂, y₂, Complex.mul_re, Complex.mul_im]
  rw [hc₁, hc₂]
  exact hsq

/-- Public finite-simple-pole rectangle residue theorem.  The radii select
disjointness-free local squares around the poles; only containment in the
outer rectangle is required. -/
theorem rectBoundaryIntegral_finite_simplePoles
    {ι : Type*} (poles : Finset ι) (pole residue : ι → ℂ)
    (radius : ι → ℝ) {x₀ x₃ y₀ y₃ : ℝ} (g : ℂ → ℂ)
    (hg : DifferentiableOn ℂ g
      ([[x₀, x₃]] ×ℂ [[y₀, y₃]]))
    (hr : ∀ i ∈ poles, 0 < radius i)
    (hx₀ : ∀ i ∈ poles, x₀ < (pole i).re - radius i)
    (hx₃ : ∀ i ∈ poles, (pole i).re + radius i < x₃)
    (hy₀ : ∀ i ∈ poles, y₀ < (pole i).im - radius i)
    (hy₃ : ∀ i ∈ poles, (pole i).im + radius i < y₃)
    (hInt : ∀ i ∈ poles, RectIntegrable
      (fun z : ℂ ↦ (z - pole i)⁻¹) (x₀ + y₀ * I) (x₃ + y₃ * I)) :
    rectBoundaryIntegral
      (fun z ↦ g z + ∑ i ∈ poles, residue i * (z - pole i)⁻¹)
      (x₀ + y₀ * I) (x₃ + y₃ * I) =
        2 * Real.pi * I * ∑ i ∈ poles, residue i := by
  classical
  let z : ℂ := x₀ + y₀ * I
  let w : ℂ := x₃ + y₃ * I
  have hgInt : RectIntegrable g z w := by
    apply rectIntegrable_of_continuousOn
    norm_num [z, w, Complex.mul_re, Complex.mul_im]
    exact hg.continuousOn
  have hgZero : rectBoundaryIntegral g z w = 0 := by
    apply rectBoundaryIntegral_eq_zero_of_differentiableOn
    norm_num [z, w, Complex.mul_re, Complex.mul_im]
    exact hg
  let F : ι → ℂ → ℂ := fun i q ↦ residue i * (q - pole i)⁻¹
  have hFInt : ∀ i ∈ poles, RectIntegrable (F i) z w := by
    intro i hi
    exact (hInt i hi).const_mul (residue i)
  rw [rectBoundaryIntegral_add hgInt (RectIntegrable.fun_sum poles hFInt)]
  rw [hgZero, zero_add, rectBoundaryIntegral_fun_sum poles F z w hFInt]
  apply Eq.trans ?_ (Finset.mul_sum _ _ _).symm
  apply Finset.sum_congr rfl
  intro i hi
  rw [show F i = fun q ↦ residue i * (q - pole i)⁻¹ by rfl]
  rw [rectBoundaryIntegral_const_mul]
  rw [rectBoundaryIntegral_sub_inv (pole i) (hr i hi)
    (hx₀ i hi) (hx₃ i hi) (hy₀ i hi) (hy₃ i hi)]
  ring

/-- Finite-simple-pole rectangle residue theorem without a separate boundary
integrability hypothesis. Strict containment of each local square already
implies that the pole misses all four outer edges. -/
theorem rectBoundaryIntegral_finite_simplePoles_of_radii
    {ι : Type*} (poles : Finset ι) (pole residue : ι → ℂ)
    (radius : ι → ℝ) {x₀ x₃ y₀ y₃ : ℝ} (g : ℂ → ℂ)
    (hg : DifferentiableOn ℂ g
      ([[x₀, x₃]] ×ℂ [[y₀, y₃]]))
    (hr : ∀ i ∈ poles, 0 < radius i)
    (hx₀ : ∀ i ∈ poles, x₀ < (pole i).re - radius i)
    (hx₃ : ∀ i ∈ poles, (pole i).re + radius i < x₃)
    (hy₀ : ∀ i ∈ poles, y₀ < (pole i).im - radius i)
    (hy₃ : ∀ i ∈ poles, (pole i).im + radius i < y₃) :
    rectBoundaryIntegral
      (fun z ↦ g z + ∑ i ∈ poles, residue i * (z - pole i)⁻¹)
      (x₀ + y₀ * I) (x₃ + y₃ * I) =
        2 * Real.pi * I * ∑ i ∈ poles, residue i := by
  apply rectBoundaryIntegral_finite_simplePoles poles pole residue radius g hg
    hr hx₀ hx₃ hy₀ hy₃
  intro i hi
  apply sub_inv_rectIntegrable_of_mem_openRectangle
  · linarith [hx₀ i hi, hr i hi]
  · linarith [hx₃ i hi, hr i hi]
  · linarith [hy₀ i hi, hr i hi]
  · linarith [hy₃ i hi, hr i hi]

/-- Human-facing finite-simple-pole rectangle residue theorem. The only
geometric hypothesis is that every pole lies strictly inside the rectangle;
the local radii used by the subdivision proof are chosen internally. -/
theorem rectBoundaryIntegral_finite_simplePoles_of_mem_openRectangle
    {ι : Type*} (poles : Finset ι) (pole residue : ι → ℂ)
    {x₀ x₃ y₀ y₃ : ℝ} (g : ℂ → ℂ)
    (hg : DifferentiableOn ℂ g
      ([[x₀, x₃]] ×ℂ [[y₀, y₃]]))
    (hx₀ : ∀ i ∈ poles, x₀ < (pole i).re)
    (hx₃ : ∀ i ∈ poles, (pole i).re < x₃)
    (hy₀ : ∀ i ∈ poles, y₀ < (pole i).im)
    (hy₃ : ∀ i ∈ poles, (pole i).im < y₃) :
    rectBoundaryIntegral
      (fun z ↦ g z + ∑ i ∈ poles, residue i * (z - pole i)⁻¹)
      (x₀ + y₀ * I) (x₃ + y₃ * I) =
        2 * Real.pi * I * ∑ i ∈ poles, residue i := by
  let radius : ι → ℝ := fun i ↦
    min (min ((pole i).re - x₀) (x₃ - (pole i).re))
      (min ((pole i).im - y₀) (y₃ - (pole i).im)) / 2
  apply rectBoundaryIntegral_finite_simplePoles_of_radii
    poles pole residue radius g hg
  · intro i hi
    dsimp [radius]
    apply div_pos
    · rw [lt_min_iff]
      constructor
      · rw [lt_min_iff]
        exact ⟨sub_pos.mpr (hx₀ i hi), sub_pos.mpr (hx₃ i hi)⟩
      · rw [lt_min_iff]
        exact ⟨sub_pos.mpr (hy₀ i hi), sub_pos.mpr (hy₃ i hi)⟩
    · norm_num
  · intro i hi
    have hpos : 0 < (pole i).re - x₀ := sub_pos.mpr (hx₀ i hi)
    have hle :
        min (min ((pole i).re - x₀) (x₃ - (pole i).re))
          (min ((pole i).im - y₀) (y₃ - (pole i).im)) ≤
            (pole i).re - x₀ :=
      (min_le_left _ _).trans (min_le_left _ _)
    dsimp [radius]
    linarith
  · intro i hi
    have hpos : 0 < x₃ - (pole i).re := sub_pos.mpr (hx₃ i hi)
    have hle :
        min (min ((pole i).re - x₀) (x₃ - (pole i).re))
          (min ((pole i).im - y₀) (y₃ - (pole i).im)) ≤
            x₃ - (pole i).re :=
      (min_le_left _ _).trans (min_le_right _ _)
    dsimp [radius]
    linarith
  · intro i hi
    have hpos : 0 < (pole i).im - y₀ := sub_pos.mpr (hy₀ i hi)
    have hle :
        min (min ((pole i).re - x₀) (x₃ - (pole i).re))
          (min ((pole i).im - y₀) (y₃ - (pole i).im)) ≤
            (pole i).im - y₀ :=
      (min_le_right _ _).trans (min_le_left _ _)
    dsimp [radius]
    linarith
  · intro i hi
    have hpos : 0 < y₃ - (pole i).im := sub_pos.mpr (hy₃ i hi)
    have hle :
        min (min ((pole i).re - x₀) (x₃ - (pole i).re))
          (min ((pole i).im - y₀) (y₃ - (pole i).im)) ≤
            y₃ - (pole i).im :=
      (min_le_right _ _).trans (min_le_right _ _)
    dsimp [radius]
    linarith

/-- Native `wedgeIntegral` form of the finite-simple-pole rectangle residue
theorem. -/
theorem wedgeIntegral_add_wedgeIntegral_finite_simplePoles_of_radii
    {ι : Type*} (poles : Finset ι) (pole residue : ι → ℂ)
    (radius : ι → ℝ) {x₀ x₃ y₀ y₃ : ℝ} (g : ℂ → ℂ)
    (hg : DifferentiableOn ℂ g
      ([[x₀, x₃]] ×ℂ [[y₀, y₃]]))
    (hr : ∀ i ∈ poles, 0 < radius i)
    (hx₀ : ∀ i ∈ poles, x₀ < (pole i).re - radius i)
    (hx₃ : ∀ i ∈ poles, (pole i).re + radius i < x₃)
    (hy₀ : ∀ i ∈ poles, y₀ < (pole i).im - radius i)
    (hy₃ : ∀ i ∈ poles, (pole i).im + radius i < y₃) :
    let z := x₀ + y₀ * I
    let w := x₃ + y₃ * I
    let f := fun q ↦ g q + ∑ i ∈ poles, residue i * (q - pole i)⁻¹
    Complex.wedgeIntegral z w f + Complex.wedgeIntegral w z f =
      2 * Real.pi * I * ∑ i ∈ poles, residue i := by
  dsimp only
  rw [← rectBoundaryIntegral_eq_wedgeIntegral_add]
  exact rectBoundaryIntegral_finite_simplePoles_of_radii poles pole residue
    radius g hg hr hx₀ hx₃ hy₀ hy₃

/-- Native `wedgeIntegral` form with only strict interior containment as its
geometric hypothesis. -/
theorem wedgeIntegral_add_wedgeIntegral_finite_simplePoles_of_mem_openRectangle
    {ι : Type*} (poles : Finset ι) (pole residue : ι → ℂ)
    {x₀ x₃ y₀ y₃ : ℝ} (g : ℂ → ℂ)
    (hg : DifferentiableOn ℂ g
      ([[x₀, x₃]] ×ℂ [[y₀, y₃]]))
    (hx₀ : ∀ i ∈ poles, x₀ < (pole i).re)
    (hx₃ : ∀ i ∈ poles, (pole i).re < x₃)
    (hy₀ : ∀ i ∈ poles, y₀ < (pole i).im)
    (hy₃ : ∀ i ∈ poles, (pole i).im < y₃) :
    let z := x₀ + y₀ * I
    let w := x₃ + y₃ * I
    let f := fun q ↦ g q + ∑ i ∈ poles, residue i * (q - pole i)⁻¹
    Complex.wedgeIntegral z w f + Complex.wedgeIntegral w z f =
      2 * Real.pi * I * ∑ i ∈ poles, residue i := by
  dsimp only
  rw [← rectBoundaryIntegral_eq_wedgeIntegral_add]
  exact rectBoundaryIntegral_finite_simplePoles_of_mem_openRectangle
    poles pole residue g hg hx₀ hx₃ hy₀ hy₃

end

end RHBridge.ComplexResidue
