/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.PolyEnclosure

/-!
# Exact rational-polynomial backend for canonical `p = 2` panels

Generated panel certificates should perform polynomial arithmetic and exact
integration in `ℚ`, not normalize large expressions in `ℝ`.  This module
provides that backend and proves that the single final coefficient cast agrees
exactly with `PolyEnclosure.exactIntegral`.

The dense `ofCoeffs` constructor lets a generator emit coefficient functions
directly.  Addition, multiplication, powers, finite sums/products, composition,
and affine changes of variable all commute with the coefficient cast.
-/

namespace RHP2Bridge

namespace RatPoly

open Polynomial

/-- Exact rational polynomial used by generated panel witnesses. -/
abbrev QPoly := Polynomial ℚ

/-- Coefficientwise embedding of a rational polynomial into `ℝ[X]`. -/
noncomputable def toReal (p : QPoly) : ℝ[X] :=
  p.map (algebraMap ℚ ℝ)

@[simp] theorem toReal_zero : toReal 0 = 0 := by
  simp [toReal]

@[simp] theorem toReal_one : toReal 1 = 1 := by
  simp [toReal]

@[simp] theorem toReal_C (q : ℚ) : toReal (C q) = C (q : ℝ) := by
  simp [toReal]

@[simp] theorem toReal_X : toReal (X : QPoly) = X := by
  simp [toReal]

@[simp] theorem toReal_monomial (n : ℕ) (q : ℚ) :
    toReal (monomial n q) = monomial n (q : ℝ) := by
  simp [toReal]

@[simp] theorem toReal_add (p q : QPoly) :
    toReal (p + q) = toReal p + toReal q := by
  simp [toReal]

@[simp] theorem toReal_sub (p q : QPoly) :
    toReal (p - q) = toReal p - toReal q := by
  simp [toReal]

@[simp] theorem toReal_neg (p : QPoly) :
    toReal (-p) = -toReal p := by
  simp [toReal]

@[simp] theorem toReal_mul (p q : QPoly) :
    toReal (p * q) = toReal p * toReal q := by
  simp [toReal]

@[simp] theorem toReal_pow (p : QPoly) (n : ℕ) :
    toReal (p ^ n) = toReal p ^ n := by
  simp [toReal]

@[simp] theorem toReal_smul (q : ℚ) (p : QPoly) :
    toReal (q • p) = (q : ℝ) • toReal p := by
  simp [toReal]

theorem toReal_finset_sum {ι : Type*} (s : Finset ι) (p : ι → QPoly) :
    toReal (∑ i ∈ s, p i) = ∑ i ∈ s, toReal (p i) := by
  exact Polynomial.map_sum (algebraMap ℚ ℝ) p s

theorem toReal_finset_prod {ι : Type*} (s : Finset ι) (p : ι → QPoly) :
    toReal (∏ i ∈ s, p i) = ∏ i ∈ s, toReal (p i) := by
  exact Polynomial.map_prod (algebraMap ℚ ℝ) p s

theorem toReal_comp (p q : QPoly) :
    toReal (p.comp q) = (toReal p).comp (toReal q) := by
  simp [toReal, Polynomial.map_comp]

/-- Evaluation of the real polynomial is `eval₂` of its rational source. -/
theorem eval_toReal (p : QPoly) (x : ℝ) :
    (toReal p).eval x = p.eval₂ (algebraMap ℚ ℝ) x := by
  exact Polynomial.eval_map _ _

/-- At a rational point, evaluation itself commutes with the cast. -/
@[simp] theorem eval_toReal_atRat (p : QPoly) (x : ℚ) :
    (toReal p).eval (x : ℝ) = ((p.eval x : ℚ) : ℝ) := by
  rw [eval_toReal]
  exact Polynomial.eval₂_at_apply (p := p) (algebraMap ℚ ℝ) x

/-- Dense coefficient constructor used by generated certificate tables. -/
noncomputable def ofCoeffs {n : ℕ} (v : Fin n → ℚ) : QPoly :=
  Polynomial.ofFn n v

@[simp] theorem coeff_ofCoeffs_of_lt {n k : ℕ} (v : Fin n → ℚ)
    (hk : k < n) :
    (ofCoeffs v).coeff k = v ⟨k, hk⟩ := by
  exact Polynomial.ofFn_coeff_eq_val_of_lt v hk

@[simp] theorem coeff_ofCoeffs_of_ge {n k : ℕ} (v : Fin n → ℚ)
    (hk : n ≤ k) :
    (ofCoeffs v).coeff k = 0 := by
  exact Polynomial.ofFn_coeff_eq_zero_of_ge v hk

/-- Dense coefficient construction also commutes with the final cast. -/
theorem toReal_ofCoeffs {n : ℕ} (v : Fin n → ℚ) :
    toReal (ofCoeffs v) =
      Polynomial.ofFn n (fun i => (v i : ℝ)) := by
  ext k
  by_cases hk : k < n
  · simp [toReal, ofCoeffs, hk]
  · have hnk : n ≤ k := Nat.le_of_not_gt hk
    simp [toReal, ofCoeffs, hnk]

/-- A kernel-checked rational coefficient identity transfers to `ℝ[X]`. -/
theorem toReal_eq_of_eq {p q : QPoly} (h : p = q) :
    toReal p = toReal q := by
  rw [h]

/-- Transfer a generated dense-vector sum witness without expanding it over
the reals. -/
theorem toReal_ofCoeffs_eq_add_of_eq
    {m n l : ℕ} {u : Fin l → ℚ} {v : Fin m → ℚ} {w : Fin n → ℚ}
    (h : ofCoeffs u = ofCoeffs v + ofCoeffs w) :
    toReal (ofCoeffs u) =
      toReal (ofCoeffs v) + toReal (ofCoeffs w) := by
  rw [h, toReal_add]

/-- Transfer a generated dense-vector product witness without real
coefficient convolution. -/
theorem toReal_ofCoeffs_eq_mul_of_eq
    {m n l : ℕ} {u : Fin l → ℚ} {v : Fin m → ℚ} {w : Fin n → ℚ}
    (h : ofCoeffs u = ofCoeffs v * ofCoeffs w) :
    toReal (ofCoeffs u) =
      toReal (ofCoeffs v) * toReal (ofCoeffs w) := by
  rw [h, toReal_mul]

/-- Rewrite a rational global polynomial in the local coordinate `x` around
the rational center `c`. -/
noncomputable def shift (p : QPoly) (c : ℚ) : QPoly :=
  p.comp (C c + X)

@[simp] theorem eval_shift (p : QPoly) (c x : ℚ) :
    (shift p c).eval x = p.eval (c + x) := by
  simp [shift]

/-- The rational shift is exactly `PolyEnclosure.shiftPolynomial` after the
single coefficient cast. -/
theorem toReal_shift (p : QPoly) (c : ℚ) :
    toReal (shift p c) =
      PolyEnclosure.shiftPolynomial (toReal p) (c : ℝ) := by
  simp [shift, toReal, PolyEnclosure.shiftPolynomial,
    Polynomial.map_comp]

/-- Transfer a generated dense-vector shift witness. -/
theorem toReal_ofCoeffs_eq_shift_of_eq
    {m n : ℕ} {u : Fin m → ℚ} {v : Fin n → ℚ} {c : ℚ}
    (h : ofCoeffs u = shift (ofCoeffs v) c) :
    toReal (ofCoeffs u) =
      PolyEnclosure.shiftPolynomial (toReal (ofCoeffs v)) (c : ℝ) := by
  rw [h, toReal_shift]

/-- General rational affine substitution `x ↦ c + s*x`. -/
noncomputable def affine (p : QPoly) (c s : ℚ) : QPoly :=
  p.comp (C c + C s * X)

@[simp] theorem eval_affine (p : QPoly) (c s x : ℚ) :
    (affine p c s).eval x = p.eval (c + s * x) := by
  simp [affine]

theorem toReal_affine (p : QPoly) (c s : ℚ) :
    toReal (affine p c s) =
      (toReal p).comp (C (c : ℝ) + C (s : ℝ) * X) := by
  simp [affine, toReal, Polynomial.map_comp]

/-! ## Compositional rational witnesses for real polynomials -/

/-- Evidence that a real polynomial is obtained by coefficientwise casting
an exact rational polynomial. -/
structure CastWitness (p : ℝ[X]) where
  rational : QPoly
  eq_toReal : p = toReal rational

namespace CastWitness

noncomputable def ofRational (p : QPoly) : CastWitness (toReal p) :=
  ⟨p, rfl⟩

noncomputable def const (q : ℚ) : CastWitness (C (q : ℝ)) :=
  ⟨C q, (toReal_C q).symm⟩

noncomputable def X' : CastWitness (X : ℝ[X]) :=
  ⟨X, toReal_X.symm⟩

noncomputable def add {p q : ℝ[X]}
    (hp : CastWitness p) (hq : CastWitness q) : CastWitness (p + q) :=
  ⟨hp.rational + hq.rational, by
    rw [toReal_add, ← hp.eq_toReal, ← hq.eq_toReal]⟩

noncomputable def sub {p q : ℝ[X]}
    (hp : CastWitness p) (hq : CastWitness q) : CastWitness (p - q) :=
  ⟨hp.rational - hq.rational, by
    rw [toReal_sub, ← hp.eq_toReal, ← hq.eq_toReal]⟩

noncomputable def neg {p : ℝ[X]}
    (hp : CastWitness p) : CastWitness (-p) :=
  ⟨-hp.rational, by rw [toReal_neg, ← hp.eq_toReal]⟩

noncomputable def mul {p q : ℝ[X]}
    (hp : CastWitness p) (hq : CastWitness q) : CastWitness (p * q) :=
  ⟨hp.rational * hq.rational, by
    rw [toReal_mul, ← hp.eq_toReal, ← hq.eq_toReal]⟩

noncomputable def pow {p : ℝ[X]}
    (hp : CastWitness p) (n : ℕ) : CastWitness (p ^ n) :=
  ⟨hp.rational ^ n, by rw [toReal_pow, ← hp.eq_toReal]⟩

noncomputable def comp {p q : ℝ[X]}
    (hp : CastWitness p) (hq : CastWitness q) :
    CastWitness (p.comp q) :=
  ⟨hp.rational.comp hq.rational, by
    rw [toReal_comp, ← hp.eq_toReal, ← hq.eq_toReal]⟩

noncomputable def shift {p : ℝ[X]}
    (hp : CastWitness p) (c : ℚ) :
    CastWitness (PolyEnclosure.shiftPolynomial p (c : ℝ)) :=
  ⟨RatPoly.shift hp.rational c, by
    rw [toReal_shift, ← hp.eq_toReal]⟩

noncomputable def affine {p : ℝ[X]}
    (hp : CastWitness p) (c s : ℚ) :
    CastWitness (p.comp (C (c : ℝ) + C (s : ℝ) * X)) :=
  ⟨RatPoly.affine hp.rational c s, by
    rw [toReal_affine, ← hp.eq_toReal]⟩

noncomputable def ofCoeffs {n : ℕ} (v : Fin n → ℚ) :
    CastWitness (toReal (RatPoly.ofCoeffs v)) :=
  ofRational (RatPoly.ofCoeffs v)

end CastWitness

/-- Exact rational expression for the oriented integral of a rational
polynomial on rational endpoints. -/
def exactIntegral (p : QPoly) (a b : ℚ) : ℚ :=
  ∑ k ∈ Finset.range (p.natDegree + 1),
    p.coeff k * ((b ^ (k + 1) - a ^ (k + 1)) / ((k : ℚ) + 1))

/-- A supplied strict degree cap may replace `natDegree + 1` in the exact
rational integral.  This is useful for dense generated coefficient vectors. -/
theorem exactIntegral_eq_sum_range_of_natDegree_lt
    (p : QPoly) (a b : ℚ) {N : ℕ} (hdeg : p.natDegree < N) :
    exactIntegral p a b =
      ∑ k ∈ Finset.range N,
        p.coeff k * ((b ^ (k + 1) - a ^ (k + 1)) / ((k : ℚ) + 1)) := by
  unfold exactIntegral
  apply Finset.sum_subset
  · exact Finset.range_mono (Nat.succ_le_iff.mpr hdeg)
  · intro k hkN hkSmall
    have hkdeg : p.natDegree < k := by
      have hkNot : ¬k < p.natDegree + 1 := by
        simpa only [Finset.mem_range] using hkSmall
      omega
    rw [Polynomial.coeff_eq_zero_of_natDegree_lt hkdeg, zero_mul]

/-- Direct exact integration of a dense rational coefficient vector. -/
def exactIntegralCoeffs {n : ℕ} (v : Fin n → ℚ) (a b : ℚ) : ℚ :=
  ∑ k : Fin n,
    v k * ((b ^ (k.val + 1) - a ^ (k.val + 1)) /
      ((k.val : ℚ) + 1))

/-- The dense coefficient-vector integrator agrees with the polynomial
integrator, including the empty-vector case. -/
theorem exactIntegral_ofCoeffs {n : ℕ} (v : Fin n → ℚ) (a b : ℚ) :
    exactIntegral (ofCoeffs v) a b = exactIntegralCoeffs v a b := by
  by_cases hn : n = 0
  · subst n
    simp [exactIntegral, exactIntegralCoeffs, ofCoeffs]
  · have hdeg : (ofCoeffs v).natDegree < n :=
      Polynomial.ofFn_natDegree_lt (Nat.one_le_iff_ne_zero.mpr hn) v
    rw [exactIntegral_eq_sum_range_of_natDegree_lt _ _ _ hdeg]
    rw [← Fin.sum_univ_eq_sum_range]
    simp [exactIntegralCoeffs, ofCoeffs]

private theorem natDegree_toReal (p : QPoly) :
    (toReal p).natDegree = p.natDegree := by
  unfold toReal
  exact Polynomial.natDegree_map_eq_of_injective
    (Rat.cast_injective (α := ℝ)) p

/-- Central compatibility theorem: exact integration in `ℚ`, followed by one
cast, is definitionally the same mathematical quantity as the existing real
polynomial integrator. -/
theorem cast_exactIntegral (p : QPoly) (a b : ℚ) :
    (exactIntegral p a b : ℝ) =
      PolyEnclosure.exactIntegral (toReal p) (a : ℝ) (b : ℝ) := by
  unfold exactIntegral PolyEnclosure.exactIntegral
  rw [natDegree_toReal]
  push_cast
  apply Finset.sum_congr rfl
  intro k hk
  simp [toReal]

/-- Dense coefficient-vector compatibility with
`PolyEnclosure.exactIntegral`. -/
theorem cast_exactIntegralCoeffs {n : ℕ} (v : Fin n → ℚ) (a b : ℚ) :
    (exactIntegralCoeffs v a b : ℝ) =
      PolyEnclosure.exactIntegral
        (toReal (ofCoeffs v)) (a : ℝ) (b : ℝ) := by
  rw [← exactIntegral_ofCoeffs, cast_exactIntegral]

/-- A rational equality for a dense coefficient vector identifies its real
exact integral immediately. -/
theorem real_exactIntegral_ofCoeffs_eq_of_eq
    {n : ℕ} {v : Fin n → ℚ} {a b value : ℚ}
    (h : exactIntegralCoeffs v a b = value) :
    PolyEnclosure.exactIntegral
        (toReal (ofCoeffs v)) (a : ℝ) (b : ℝ) = (value : ℝ) := by
  rw [← cast_exactIntegralCoeffs, h]

/-- Compatibility with the actual oriented interval integral. -/
theorem intervalIntegral_eval_toReal (p : QPoly) (a b : ℚ) :
    (∫ x in (a : ℝ)..(b : ℝ), (toReal p).eval x) =
      (exactIntegral p a b : ℝ) := by
  rw [PolyEnclosure.integral_eval_eq_exactIntegral]
  exact (cast_exactIntegral p a b).symm

/-- Exact rational change of variables for an affine substitution.  This
includes `s = 0` and therefore needs no side condition. -/
theorem exactIntegral_affine (p : QPoly) (c s a b : ℚ) :
    exactIntegral p (c + s * a) (c + s * b) =
      s * exactIntegral (affine p c s) a b := by
  apply Rat.cast_injective (α := ℝ)
  push_cast
  rw [cast_exactIntegral, cast_exactIntegral]
  rw [← PolyEnclosure.integral_eval_eq_exactIntegral,
    ← PolyEnclosure.integral_eval_eq_exactIntegral]
  have hchange := intervalIntegral.smul_integral_comp_add_mul
    (a := (a : ℝ)) (b := (b : ℝ))
    (fun x : ℝ => (toReal p).eval x) (s : ℝ) (c : ℝ)
  rw [toReal_affine]
  simp only [Polynomial.eval_comp, Polynomial.eval_add,
    Polynomial.eval_C, Polynomial.eval_mul, Polynomial.eval_X,
    smul_eq_mul] at hchange ⊢
  simpa [add_comm] using hchange.symm

/-- Normalization of a centered panel to `[-1,1]`. -/
theorem exactIntegral_centered_eq_scale_normalized
    (p : QPoly) (h : ℚ) :
    exactIntegral p (-h) h =
      h * exactIntegral (affine p 0 h) (-1) 1 := by
  simpa using exactIntegral_affine p 0 h (-1) 1

/-- A generated rational equality is sufficient to identify a real exact
panel integral, with no real symbolic normalization. -/
theorem real_exactIntegral_eq_of_eq {p : QPoly} {a b value : ℚ}
    (h : exactIntegral p a b = value) :
    PolyEnclosure.exactIntegral (toReal p) (a : ℝ) (b : ℝ) =
      (value : ℝ) := by
  rw [← cast_exactIntegral, h]

/-- Bridge an arbitrary real panel polynomial to a rational witness.  The
potentially large polynomial identity is checked over `ℚ`; the real exact
integral then follows by one rewrite. -/
theorem real_exactIntegral_eq_of_poly_eq
    {pReal : ℝ[X]} {p : QPoly} {a b value : ℚ}
    (hpoly : pReal = toReal p)
    (hvalue : exactIntegral p a b = value) :
    PolyEnclosure.exactIntegral pReal (a : ℝ) (b : ℝ) = (value : ℝ) := by
  rw [hpoly]
  exact real_exactIntegral_eq_of_eq hvalue

/-- Exact-integral bridge packaged through a compositional cast witness. -/
theorem CastWitness.real_exactIntegral_eq
    {pReal : ℝ[X]} (hp : CastWitness pReal) (a b : ℚ) :
    PolyEnclosure.exactIntegral pReal (a : ℝ) (b : ℝ) =
      (exactIntegral hp.rational a b : ℝ) := by
  calc
    PolyEnclosure.exactIntegral pReal (a : ℝ) (b : ℝ) =
        PolyEnclosure.exactIntegral (toReal hp.rational) (a : ℝ) (b : ℝ) :=
      congrArg (fun p : ℝ[X] =>
        PolyEnclosure.exactIntegral p (a : ℝ) (b : ℝ)) hp.eq_toReal
    _ = (exactIntegral hp.rational a b : ℝ) :=
      (cast_exactIntegral hp.rational a b).symm

/-- A generated rational value equality closes the exact real integral of a
compositional witness. -/
theorem CastWitness.real_exactIntegral_eq_of_eq
    {pReal : ℝ[X]} (hp : CastWitness pReal) {a b value : ℚ}
    (hvalue : exactIntegral hp.rational a b = value) :
    PolyEnclosure.exactIntegral pReal (a : ℝ) (b : ℝ) = (value : ℝ) := by
  rw [hp.real_exactIntegral_eq, hvalue]

/-- Finite sums of panel integrals can likewise be normalized entirely in
`ℚ` and cast only once. -/
theorem sum_real_exactIntegral_eq_cast
    {ι : Type*} (s : Finset ι) (p : ι → QPoly)
    (a b : ι → ℚ) :
    ∑ i ∈ s, PolyEnclosure.exactIntegral
        (toReal (p i)) (a i : ℝ) (b i : ℝ) =
      ((∑ i ∈ s, exactIntegral (p i) (a i) (b i) : ℚ) : ℝ) := by
  push_cast
  apply Finset.sum_congr rfl
  intro i hi
  exact (cast_exactIntegral (p i) (a i) (b i)).symm

/-- A single rational witness proves a whole generated sum of exact panel
integrals. -/
theorem sum_real_exactIntegral_eq_of_rational_eq
    {ι : Type*} {s : Finset ι} {p : ι → QPoly}
    {a b : ι → ℚ} {value : ℚ}
    (h : ∑ i ∈ s, exactIntegral (p i) (a i) (b i) = value) :
    ∑ i ∈ s, PolyEnclosure.exactIntegral
        (toReal (p i)) (a i : ℝ) (b i : ℝ) = (value : ℝ) := by
  rw [sum_real_exactIntegral_eq_cast, h]

end RatPoly

end RHP2Bridge
