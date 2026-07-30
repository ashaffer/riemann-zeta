/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Centered-panel polynomial enclosures

This module provides a reusable algebra for exact, generated centered-panel
certificates.  Nothing here relies on trusted numerical computation:
generated proofs can instantiate rational polynomials and discharge the
remaining scalar inequalities in the Lean kernel.

The main ingredients are uniform polynomial enclosures closed under arithmetic,
exact coefficientwise panel integration, and finite-geometric reciprocal
enclosures under an explicit perturbation bound below one.
-/

namespace PolyEnclosure

open Polynomial

/-- `p`, evaluated in the local coordinate `x`, encloses `f` on the panel
`[c-h,c+h]` with uniform absolute error `e`. -/
def CenteredEncloses (c h : ℝ) (f : ℝ → ℝ) (p : ℝ[X]) (e : ℝ) : Prop :=
  ∀ x : ℝ, |x| ≤ h → |f (c + x) - p.eval x| ≤ e

/-- Uniform absolute bound for a polynomial in the local panel coordinate. -/
def PolyBound (h : ℝ) (p : ℝ[X]) (M : ℝ) : Prop :=
  ∀ x : ℝ, |x| ≤ h → |p.eval x| ≤ M

/-- Rewrite a global-coordinate polynomial in the local coordinate `x`
around the center `c`. -/
noncomputable def shiftPolynomial (p : ℝ[X]) (c : ℝ) : ℝ[X] :=
  p.comp (Polynomial.C c + Polynomial.X)

@[simp] theorem eval_shiftPolynomial (p : ℝ[X]) (c x : ℝ) :
    (shiftPolynomial p c).eval x = p.eval (c + x) := by
  simp [shiftPolynomial]

theorem centeredEncloses_shiftPolynomial_of_pointwise
    {c h e : ℝ} {f : ℝ → ℝ} {p : ℝ[X]}
    (hpoint : ∀ x : ℝ, |x| ≤ h → |f (c + x) - p.eval (c + x)| ≤ e) :
    CenteredEncloses c h f (shiftPolynomial p c) e := by
  intro x hx
  simpa using hpoint x hx

theorem CenteredEncloses.mono_error {c h e E : ℝ} {f : ℝ → ℝ} {p : ℝ[X]}
    (hencl : CenteredEncloses c h f p e) (heE : e ≤ E) :
    CenteredEncloses c h f p E := by
  intro x hx
  exact (hencl x hx).trans heE

/-- Turn an analytic bound on the enclosed function into a polynomial bound.
This avoids unstable coefficient majorants for high-degree local models. -/
theorem CenteredEncloses.polyBound_of_functionBound
    {c h e F : ℝ} {f : ℝ → ℝ} {p : ℝ[X]}
    (hencl : CenteredEncloses c h f p e)
    (hbound : ∀ y : ℝ, |y - c| ≤ h → |f y| ≤ F) :
    PolyBound h p (F + e) := by
  intro x hx
  calc
    |p.eval x| = |f (c + x) - (f (c + x) - p.eval x)| := by ring_nf
    _ ≤ |f (c + x)| + |f (c + x) - p.eval x| := abs_sub _ _
    _ ≤ F + e := by
      exact add_le_add (hbound (c + x) (by simpa using hx)) (hencl x hx)

theorem centeredEncloses_exact (c h : ℝ) (p : ℝ[X]) :
    CenteredEncloses c h (fun y ↦ p.eval (y - c)) p 0 := by
  intro x hx
  simp

theorem CenteredEncloses.add {c h e d : ℝ} {f g : ℝ → ℝ} {p q : ℝ[X]}
    (hf : CenteredEncloses c h f p e)
    (hg : CenteredEncloses c h g q d) :
    CenteredEncloses c h (fun y ↦ f y + g y) (p + q) (e + d) := by
  intro x hx
  rw [Polynomial.eval_add]
  have hrewrite :
      f (c + x) + g (c + x) - (p.eval x + q.eval x) =
        (f (c + x) - p.eval x) + (g (c + x) - q.eval x) := by ring
  rw [hrewrite]
  exact (abs_add_le _ _).trans (add_le_add (hf x hx) (hg x hx))

theorem CenteredEncloses.sub {c h e d : ℝ} {f g : ℝ → ℝ} {p q : ℝ[X]}
    (hf : CenteredEncloses c h f p e)
    (hg : CenteredEncloses c h g q d) :
    CenteredEncloses c h (fun y ↦ f y - g y) (p - q) (e + d) := by
  intro x hx
  rw [Polynomial.eval_sub]
  have hrewrite :
      f (c + x) - g (c + x) - (p.eval x - q.eval x) =
        (f (c + x) - p.eval x) - (g (c + x) - q.eval x) := by ring
  rw [hrewrite]
  exact (abs_sub _ _).trans (add_le_add (hf x hx) (hg x hx))

theorem CenteredEncloses.neg {c h e : ℝ} {f : ℝ → ℝ} {p : ℝ[X]}
    (hf : CenteredEncloses c h f p e) :
    CenteredEncloses c h (fun y ↦ -f y) (-p) e := by
  intro x hx
  simpa only [Polynomial.eval_neg, neg_sub_neg, abs_sub_comm] using hf x hx

theorem CenteredEncloses.const_mul {c h e : ℝ} {f : ℝ → ℝ} {p : ℝ[X]}
    (a : ℝ) (hf : CenteredEncloses c h f p e) :
    CenteredEncloses c h (fun y ↦ a * f y) (C a * p) (|a| * e) := by
  intro x hx
  rw [Polynomial.eval_mul, Polynomial.eval_C]
  rw [show a * f (c + x) - a * p.eval x =
      a * (f (c + x) - p.eval x) by ring, abs_mul]
  exact mul_le_mul_of_nonneg_left (hf x hx) (abs_nonneg a)

/-- Product enclosure.  The error includes the second-order `e*d` term;
`P,Q` are independently certified polynomial sup bounds on the panel. -/
theorem CenteredEncloses.mul {c h e d P Q : ℝ}
    {f g : ℝ → ℝ} {p q : ℝ[X]}
    (hf : CenteredEncloses c h f p e)
    (hg : CenteredEncloses c h g q d)
    (hp : PolyBound h p P) (hq : PolyBound h q Q)
    (he : 0 ≤ e) (hP : 0 ≤ P) :
    CenteredEncloses c h (fun y ↦ f y * g y) (p * q)
      (e * d + e * Q + P * d) := by
  intro x hx
  rw [Polynomial.eval_mul]
  let ef := f (c + x) - p.eval x
  let eg := g (c + x) - q.eval x
  have hef : |ef| ≤ e := hf x hx
  have heg : |eg| ≤ d := hg x hx
  have hp' : |p.eval x| ≤ P := hp x hx
  have hq' : |q.eval x| ≤ Q := hq x hx
  have hrewrite :
      f (c + x) * g (c + x) - p.eval x * q.eval x =
        ef * eg + ef * q.eval x + p.eval x * eg := by
    dsimp [ef, eg]
    ring
  rw [hrewrite]
  calc
    |ef * eg + ef * q.eval x + p.eval x * eg| ≤
        |ef * eg| + |ef * q.eval x| + |p.eval x * eg| := by
      exact (abs_add_le _ _).trans
        (add_le_add (abs_add_le _ _) (le_refl _))
    _ = |ef| * |eg| + |ef| * |q.eval x| + |p.eval x| * |eg| := by
      rw [abs_mul, abs_mul, abs_mul]
    _ ≤ e * d + e * Q + P * d := by
      gcongr

/-- A rational expression for the exact integral of a polynomial. -/
noncomputable def exactIntegral (p : ℝ[X]) (a b : ℝ) : ℝ :=
  ∑ k ∈ Finset.range (p.natDegree + 1),
    p.coeff k * ((b ^ (k + 1) - a ^ (k + 1)) / ((k : ℝ) + 1))

theorem integral_eval_eq_exactIntegral (p : ℝ[X]) (a b : ℝ) :
    (∫ x in a..b, p.eval x) = exactIntegral p a b := by
  simp_rw [Polynomial.eval_eq_sum_range]
  rw [intervalIntegral.integral_finsetSum (μ := MeasureTheory.volume)]
  · simp_rw [intervalIntegral.integral_const_mul, integral_pow]
    rfl
  · intro k hk
    exact Continuous.intervalIntegrable (μ := MeasureTheory.volume)
      (continuous_const.mul (continuous_id.pow k)) a b

/-- Integrating a panel enclosure costs exactly panel length times the
uniform error.  The polynomial term is reduced to rational arithmetic by
`exactIntegral`. -/
theorem integral_centered_sub_exactIntegral_le
    {c h e : ℝ} {f : ℝ → ℝ} {p : ℝ[X]}
    (hh : 0 ≤ h)
    (hencl : CenteredEncloses c h f p e)
    (hf : IntervalIntegrable (fun x ↦ f (c + x)) MeasureTheory.volume (-h) h) :
    |(∫ x in -h..h, f (c + x)) - exactIntegral p (-h) h| ≤ 2 * h * e := by
  have hp : IntervalIntegrable (fun x ↦ p.eval x) MeasureTheory.volume (-h) h :=
    Continuous.intervalIntegrable (μ := MeasureTheory.volume)
      p.continuous (-h) h
  rw [← integral_eval_eq_exactIntegral]
  rw [← intervalIntegral.integral_sub hf hp]
  change ‖∫ x in -h..h, f (c + x) - p.eval x‖ ≤ _
  calc
    ‖∫ x in -h..h, f (c + x) - p.eval x‖ ≤ e * |h - (-h)| := by
      apply intervalIntegral.norm_integral_le_of_norm_le_const
      intro x hx
      rw [Real.norm_eq_abs]
      exact hencl x (by
        have hxu : x ∈ Set.uIcc (-h) h := Set.uIoc_subset_uIcc hx
        rw [Set.uIcc_of_le (by linarith)] at hxu
        rw [abs_le]
        exact hxu)
    _ = 2 * h * e := by
      rw [show |h - (-h)| = 2 * h by rw [abs_of_nonneg] <;> linarith]
      ring

/-- The same enclosure on the original (rather than centered-coordinate)
panel. -/
theorem integral_panel_sub_exactIntegral_le
    {c h e : ℝ} {f : ℝ → ℝ} {p : ℝ[X]}
    (hh : 0 ≤ h)
    (hencl : CenteredEncloses c h f p e)
    (hf : IntervalIntegrable f MeasureTheory.volume (c - h) (c + h)) :
    |(∫ y in c-h..c+h, f y) - exactIntegral p (-h) h| ≤ 2 * h * e := by
  have hfc : IntervalIntegrable (fun x ↦ f (c + x))
      MeasureTheory.volume (-h) h := by
    simpa [add_comm] using hf.comp_add_right c
  have h := integral_centered_sub_exactIntegral_le hh hencl hfc
  rw [intervalIntegral.integral_comp_add_left] at h
  simpa only [sub_eq_add_neg] using h

/-- An interval integral is the sum over any finite chain of adjacent
subintervals.  No monotonicity is needed here; oriented interval integrals
make the identity purely algebraic. -/
theorem intervalIntegral_eq_sum_range_adjacent
    (f : ℝ → ℝ) (b : ℕ → ℝ) (N : ℕ) (hf : Continuous f) :
    (∫ x in b 0..b N, f x) =
      ∑ k ∈ Finset.range N, ∫ x in b k..b (k + 1), f x := by
  induction N with
  | zero => simp
  | succ N ih =>
      rw [Finset.sum_range_succ, ← ih]
      exact (intervalIntegral.integral_add_adjacent_intervals
        (hf.intervalIntegrable (b 0) (b N))
        (hf.intervalIntegrable (b N) (b (N + 1)))).symm

/-- Aggregate centered polynomial enclosures over a finite adjacent
partition.  Generated certificates need only provide rational endpoints,
local centers/half-widths, and one local enclosure per panel. -/
theorem integral_partition_sub_sum_exactIntegral_le
    (f : ℝ → ℝ) (b c h e : ℕ → ℝ) (p : ℕ → ℝ[X]) (N : ℕ)
    (hf : Continuous f)
    (hh : ∀ k ∈ Finset.range N, 0 ≤ h k)
    (hends : ∀ k ∈ Finset.range N,
      c k - h k = b k ∧ c k + h k = b (k + 1))
    (hencl : ∀ k ∈ Finset.range N,
      CenteredEncloses (c k) (h k) f (p k) (e k)) :
    |(∫ x in b 0..b N, f x) -
        ∑ k ∈ Finset.range N, exactIntegral (p k) (-h k) (h k)| ≤
      ∑ k ∈ Finset.range N, 2 * h k * e k := by
  rw [intervalIntegral_eq_sum_range_adjacent f b N hf,
    ← Finset.sum_sub_distrib]
  calc
    |∑ k ∈ Finset.range N,
        ((∫ x in b k..b (k + 1), f x) -
          exactIntegral (p k) (-h k) (h k))| ≤
      ∑ k ∈ Finset.range N,
        |(∫ x in b k..b (k + 1), f x) -
          exactIntegral (p k) (-h k) (h k)| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ k ∈ Finset.range N, 2 * h k * e k := by
      apply Finset.sum_le_sum
      intro k hk
      have hpanel := integral_panel_sub_exactIntegral_le
        (hh k hk) (hencl k hk)
        (hf.intervalIntegrable (c k - h k) (c k + h k))
      rw [(hends k hk).1, (hends k hk).2] at hpanel
      exact hpanel

/-- Finite geometric-series polynomial approximating `1/(1+r)`. -/
noncomputable def geometricReciprocal (r : ℝ[X]) (N : ℕ) : ℝ[X] :=
  ∑ k ∈ Finset.range N, (-r) ^ k

@[simp] theorem eval_geometricReciprocal (r : ℝ[X]) (N : ℕ) (x : ℝ) :
    (geometricReciprocal r N).eval x =
      ∑ k ∈ Finset.range N, (-r.eval x) ^ k := by
  simp only [geometricReciprocal, eval_finsetSum, eval_pow, eval_neg]

theorem scalar_geometric_reciprocal_identity (u : ℝ) (N : ℕ)
    (hu : 1 + u ≠ 0) :
    (1 + u)⁻¹ - (∑ k ∈ Finset.range N, (-u) ^ k) =
      (-u) ^ N / (1 + u) := by
  have hgeom := geom_sum_mul_neg (-u) N
  simp only [sub_neg_eq_add] at hgeom
  apply (mul_right_cancel₀ hu)
  rw [sub_mul, inv_mul_cancel₀ hu]
  rw [hgeom]
  field_simp [hu] <;> ring

/-- Directed finite-geometric reciprocal remainder. -/
theorem abs_inv_one_add_sub_geometric_le
    (u ρ : ℝ) (N : ℕ) (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1)
    (huρ : |u| ≤ ρ) :
    |(1 + u)⁻¹ - (∑ k ∈ Finset.range N, (-u) ^ k)| ≤
      ρ ^ N / (1 - ρ) := by
  have huLower : -ρ ≤ u := (abs_le.mp huρ).1
  have hdenPos : 0 < 1 + u := by linarith
  have hbasePos : 0 < 1 - ρ := by linarith
  have hden : 1 + u ≠ 0 := ne_of_gt hdenPos
  rw [scalar_geometric_reciprocal_identity u N hden, abs_div,
    abs_pow, abs_neg, abs_of_pos hdenPos]
  have hpow : |u| ^ N ≤ ρ ^ N := by gcongr
  exact div_le_div₀ (pow_nonneg hρ0 N) hpow hbasePos (by linarith)

/-- Main reciprocal closure used by generated certificates: if the local
polynomial perturbation is bounded by `ρ<1`, its finite geometric reciprocal
has a fully rational uniform error. -/
theorem centeredEncloses_geometricReciprocal
    (c h ρ : ℝ) (r : ℝ[X]) (N : ℕ)
    (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1) (hr : PolyBound h r ρ) :
    CenteredEncloses c h
      (fun y ↦ (1 + r.eval (y - c))⁻¹)
      (geometricReciprocal r N) (ρ ^ N / (1 - ρ)) := by
  intro x hx
  simp only [add_sub_cancel_left]
  rw [eval_geometricReciprocal]
  exact abs_inv_one_add_sub_geometric_le (r.eval x) ρ N hρ0 hρ1 (hr x hx)

/-- Reciprocal after factoring a nonzero constant `a` from a denominator. -/
theorem centeredEncloses_scaledGeometricReciprocal
    (c h ρ a : ℝ) (r : ℝ[X]) (N : ℕ)
    (ha : a ≠ 0) (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1)
    (hr : PolyBound h r ρ) :
    CenteredEncloses c h
      (fun y ↦ (a * (1 + r.eval (y - c)))⁻¹)
      (C a⁻¹ * geometricReciprocal r N)
      (|a⁻¹| * (ρ ^ N / (1 - ρ))) := by
  have hbase := centeredEncloses_geometricReciprocal c h ρ r N hρ0 hρ1 hr
  have hscaled := hbase.const_mul a⁻¹
  intro x hx
  have := hscaled x hx
  convert this using 1 <;> field_simp

/-- Stability of reciprocal under an enclosed perturbation.  This is the
piece needed when the denominator itself has already been constructed by the
enclosure algebra. -/
theorem abs_inv_one_add_sub_inv_one_add_le
    (u v ρ e : ℝ) (hρ0 : 0 ≤ ρ) (hρ1 : ρ < 1) (he : 0 ≤ e)
    (hu : |u| ≤ ρ) (hv : |v| ≤ ρ) (huv : |u - v| ≤ e) :
    |(1 + u)⁻¹ - (1 + v)⁻¹| ≤ e / (1 - ρ) ^ 2 := by
  have huLower : -ρ ≤ u := (abs_le.mp hu).1
  have hvLower : -ρ ≤ v := (abs_le.mp hv).1
  have hbase : 0 < 1 - ρ := by linarith
  have huPos : 0 < 1 + u := by linarith
  have hvPos : 0 < 1 + v := by linarith
  have huNe : 1 + u ≠ 0 := ne_of_gt huPos
  have hvNe : 1 + v ≠ 0 := ne_of_gt hvPos
  have hid :
      (1 + u)⁻¹ - (1 + v)⁻¹ =
        (v - u) / ((1 + u) * (1 + v)) := by
    field_simp [huNe, hvNe]
    ring
  rw [hid, abs_div, abs_mul, abs_of_pos huPos, abs_of_pos hvPos]
  have hnum : |v - u| ≤ e := by simpa [abs_sub_comm] using huv
  have hden : (1 - ρ) ^ 2 ≤ (1 + u) * (1 + v) := by
    rw [pow_two]
    exact mul_le_mul (by linarith) (by linarith) hbase.le (by positivity)
  exact div_le_div₀ he hnum (sq_pos_of_pos hbase) hden

/-- Full reciprocal closure.  If `δ` is enclosed by polynomial `r` with
error `e`, and `|r|≤R` with `R+e<1`, then a finite geometric polynomial
encloses `1/(1+δ)`.  Every displayed error expression is rational when the
certificate data are rational. -/
theorem CenteredEncloses.invOneAdd_of_polyBound
    {c h R e : ℝ} {δ : ℝ → ℝ} {r : ℝ[X]} (N : ℕ)
    (hδ : CenteredEncloses c h δ r e) (hr : PolyBound h r R)
    (hR : 0 ≤ R) (he : 0 ≤ e) (hsmall : R + e < 1) :
    CenteredEncloses c h (fun y ↦ (1 + δ y)⁻¹)
      (geometricReciprocal r N)
      (e / (1 - (R + e)) ^ 2 + R ^ N / (1 - R)) := by
  intro x hx
  have hrx : |r.eval x| ≤ R := hr x hx
  have hδx : |δ (c + x) - r.eval x| ≤ e := hδ x hx
  have hδbound : |δ (c + x)| ≤ R + e := by
    calc
      |δ (c + x)| = |(δ (c + x) - r.eval x) + r.eval x| := by ring_nf
      _ ≤ |δ (c + x) - r.eval x| + |r.eval x| := abs_add_le _ _
      _ ≤ e + R := add_le_add hδx hrx
      _ = R + e := by ring
  have hrbound : |r.eval x| ≤ R + e := hrx.trans (by linarith)
  have hstable := abs_inv_one_add_sub_inv_one_add_le
    (δ (c + x)) (r.eval x) (R + e) e (by positivity) hsmall he
      hδbound hrbound hδx
  have hgeom := abs_inv_one_add_sub_geometric_le
    (r.eval x) R N hR (by linarith) hrx
  rw [eval_geometricReciprocal]
  calc
    |(1 + δ (c + x))⁻¹ - ∑ k ∈ Finset.range N, (-r.eval x) ^ k| =
        |((1 + δ (c + x))⁻¹ - (1 + r.eval x)⁻¹) +
          ((1 + r.eval x)⁻¹ -
            ∑ k ∈ Finset.range N, (-r.eval x) ^ k)| := by ring_nf
    _ ≤ |(1 + δ (c + x))⁻¹ - (1 + r.eval x)⁻¹| +
        |(1 + r.eval x)⁻¹ -
          ∑ k ∈ Finset.range N, (-r.eval x) ^ k| := abs_add_le _ _
    _ ≤ e / (1 - (R + e)) ^ 2 + R ^ N / (1 - R) :=
      add_le_add hstable hgeom

/-- Coefficient `ℓ¹` majorant, convenient for generated `norm_num` proofs. -/
def coeffMajorant (p : ℝ[X]) (h : ℝ) : ℝ :=
  ∑ k ∈ Finset.range (p.natDegree + 1), |p.coeff k| * h ^ k

theorem abs_eval_le_coeffMajorant (p : ℝ[X]) {h x : ℝ}
    (hh : 0 ≤ h) (hx : |x| ≤ h) :
    |p.eval x| ≤ coeffMajorant p h := by
  rw [Polynomial.eval_eq_sum_range]
  calc
    |∑ k ∈ Finset.range (p.natDegree + 1), p.coeff k * x ^ k| ≤
        ∑ k ∈ Finset.range (p.natDegree + 1), |p.coeff k * x ^ k| :=
      Finset.abs_sum_le_sum_abs _ _
    _ = ∑ k ∈ Finset.range (p.natDegree + 1),
        |p.coeff k| * |x| ^ k := by
      apply Finset.sum_congr rfl
      intro k hk
      rw [abs_mul, abs_pow]
    _ ≤ ∑ k ∈ Finset.range (p.natDegree + 1),
        |p.coeff k| * h ^ k := by
      gcongr with k hk
    _ = coeffMajorant p h := rfl

theorem polyBound_coeffMajorant (p : ℝ[X]) {h : ℝ} (hh : 0 ≤ h) :
    PolyBound h p (coeffMajorant p h) := by
  intro x hx
  exact abs_eval_le_coeffMajorant p hh hx

end PolyEnclosure
