/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedMomentRefinement

/-!
# Tight value-bounded triple-factor ledger for canonical `p = 2` panels

The coefficient `ℓ¹` majorants of late-panel polynomials are intentionally
very large even though the represented functions remain uniformly bounded.
This module proves those function-value bounds from the existing analytic
panel lemmas and uses them in a three-factor error ledger.  The exact dense
product center is unchanged.
-/

namespace RHP2Bridge

namespace P2RoundedBoundedTriple

open P2RoundedSharedEvaluator
open P2RoundedTripleMoment
open P2RoundedMomentRefinement
open P2RoundedPanelRefinement

/-- Common rational value bound for every normalized exact defect factor. -/
def defectValueBoundQ : ℚ := 7447 / 1000 + 21 / 10 ^ 15

/-- Common rational value bound for every normalized exact component. -/
def componentValueBoundQ : ℚ := 1 + 2 / 10 ^ 18

@[simp] theorem defectValueBoundQ_cast :
    (defectValueBoundQ : ℝ) =
      7447 / 1000 + p2PanelDefectErrorBound := by
  norm_num [defectValueBoundQ, p2PanelDefectErrorBound]

@[simp] theorem componentValueBoundQ_cast :
    (componentValueBoundQ : ℝ) =
      1 + p2PanelComponentErrorBound := by
  norm_num [componentValueBoundQ, p2PanelComponentErrorBound]

theorem evalReal_exactNormalizedDefect_eq_panelPolynomial
    (k : Fin 32) (t : ℝ) :
    RoundedRatPoly.evalReal (exactNormalizedDefect k) t =
      (p2DefectPanelPolynomial (p2PanelCenter k.val) 32).eval
        (p2PanelHalfWidth k.val * t) := by
  simp [exactNormalizedDefect, RoundedRatPoly.evalReal,
    DenseRatPoly.realize_affine,
    DenseRatPoly.realize_p2DefectPanelPolynomial,
    RatPoly.toReal_comp, RatPoly.toReal_p2DefectPanelPolynomialQ,
    p2PanelCenter, p2PanelHalfWidth]

theorem evalReal_exactNormalizedComponent_eq_panelPolynomial
    (kind : P2SelectedKind) (i : Fin 24) (k : Fin 32) (t : ℝ) :
    RoundedRatPoly.evalReal (exactNormalizedComponent kind i k) t =
      (p2SelectedComponent100ScaleCenterPolynomial kind i
        (p2PanelCenter k.val)).eval
          (p2PanelHalfWidth k.val * t) := by
  simp [exactNormalizedComponent, RoundedRatPoly.evalReal,
    DenseRatPoly.realize_affine,
    DenseRatPoly.realize_p2SelectedComponent100ScaleCenterPolynomial,
    RatPoly.toReal_comp,
    RatPoly.toReal_p2SelectedComponent100ScaleCenterPolynomialQ,
    p2PanelCenter, p2PanelHalfWidth]

/-- Uniform value bound on the exact rational defect polynomial after affine
normalization to `[-1,1]`. -/
theorem abs_evalReal_exactNormalizedDefect_le
    (k : Fin 32) {t : ℝ} (ht : |t| ≤ 1) :
    |RoundedRatPoly.evalReal (exactNormalizedDefect k) t| ≤
      (defectValueBoundQ : ℝ) := by
  have hh := p2PanelHalfWidth_nonneg k
  have hlocal :
      |p2PanelHalfWidth k.val * t| ≤ p2PanelHalfWidth k.val := by
    rw [abs_mul, abs_of_nonneg hh]
    exact (mul_le_mul_of_nonneg_left ht hh).trans_eq (mul_one _)
  have hbound := p2DefectPanelPolynomial_polyBound
    (p2PanelCenter k.val) (p2PanelHalfWidth k.val) 32 hh
    (p2Panel_band k) (p2Panel_prefixRho_lt_one k)
  rw [evalReal_exactNormalizedDefect_eq_panelPolynomial]
  calc
    |(p2DefectPanelPolynomial (p2PanelCenter k.val) 32).eval
        (p2PanelHalfWidth k.val * t)| ≤
        7447 / 1000 +
          p2DefectPanelError (p2PanelCenter k.val)
            (p2PanelHalfWidth k.val) 32 :=
      hbound _ hlocal
    _ ≤ 7447 / 1000 + p2PanelDefectErrorBound := by
      gcongr
      exact p2Panel_defectError_le k
    _ = (defectValueBoundQ : ℝ) := defectValueBoundQ_cast.symm

/-- Uniform value bound on every exact rational selected-component
polynomial after affine normalization to `[-1,1]`. -/
theorem abs_evalReal_exactNormalizedComponent_le
    (kind : P2SelectedKind) (i : Fin 24) (k : Fin 32)
    {t : ℝ} (ht : |t| ≤ 1) :
    |RoundedRatPoly.evalReal (exactNormalizedComponent kind i k) t| ≤
      (componentValueBoundQ : ℝ) := by
  have hh := p2PanelHalfWidth_nonneg k
  have hlocal :
      |p2PanelHalfWidth k.val * t| ≤ p2PanelHalfWidth k.val := by
    rw [abs_mul, abs_of_nonneg hh]
    exact (mul_le_mul_of_nonneg_left ht hh).trans_eq (mul_one _)
  have hbound :=
    p2SelectedComponent100ScaleCenterPolynomial_polyBound
      kind i (p2PanelCenter k.val) (p2PanelHalfWidth k.val)
      (p2Panel_band k)
  rw [evalReal_exactNormalizedComponent_eq_panelPolynomial]
  calc
    |(p2SelectedComponent100ScaleCenterPolynomial kind i
        (p2PanelCenter k.val)).eval
          (p2PanelHalfWidth k.val * t)| ≤
        1 + p2SelectedComponent100ScaleCenterError kind i :=
      hbound _ hlocal
    _ ≤ 1 + p2PanelComponentErrorBound := by
      gcongr
      exact p2Panel_componentError_le kind i
    _ = (componentValueBoundQ : ℝ) := componentValueBoundQ_cast.symm

/-! ### Bounded three-factor error ledger -/

/-- Tight executable error ledger.  In particular, it never inspects a
coefficient majorant of any of the three stored polynomials. -/
def boundedTripleError (d a b : Approx) : ℚ :=
  d.error * (componentValueBoundQ + a.error) *
      (componentValueBoundQ + b.error) +
    defectValueBoundQ * a.error *
      (componentValueBoundQ + b.error) +
    defectValueBoundQ * componentValueBoundQ * b.error

/-- The same exact dense product center as the direct triple-factor ledger,
equipped with the bounded-value radius. -/
def boundedTripleProductApprox (d a b : Approx) : Approx where
  coeffs := DenseRatPoly.mul d.coeffs
    (DenseRatPoly.mul a.coeffs b.coeffs)
  error := boundedTripleError d a b

@[simp] theorem boundedTripleProductApprox_coeffs_eq_unrounded
    (d a b : Approx) :
    (boundedTripleProductApprox d a b).coeffs =
      (unroundedTripleProductApprox d a b).coeffs := rfl

/-- Scalar three-factor telescoping estimate used by the polynomial
enclosure theorem below. -/
theorem abs_triple_sub_le
    {fd fa fb dh ah bh ed ea eb Bd Bc : ℝ}
    (hfd : |fd| ≤ Bd) (hfa : |fa| ≤ Bc) (hfb : |fb| ≤ Bc)
    (hd : |fd - dh| ≤ ed) (ha : |fa - ah| ≤ ea)
    (hb : |fb - bh| ≤ eb)
    (hed : 0 ≤ ed) (hea : 0 ≤ ea)
    (hBd : 0 ≤ Bd) (hBc : 0 ≤ Bc) :
    |fd * (fa * fb) - dh * (ah * bh)| ≤
      ed * (Bc + ea) * (Bc + eb) +
        Bd * ea * (Bc + eb) + Bd * Bc * eb := by
  have hah : |ah| ≤ Bc + ea := by
    calc
      |ah| = |fa - (fa - ah)| := by congr 1; ring
      _ ≤ |fa| + |fa - ah| := abs_sub _ _
      _ ≤ Bc + ea := add_le_add hfa ha
  have hbh : |bh| ≤ Bc + eb := by
    calc
      |bh| = |fb - (fb - bh)| := by congr 1; ring
      _ ≤ |fb| + |fb - bh| := abs_sub _ _
      _ ≤ Bc + eb := add_le_add hfb hb
  have hterm1 :
      |(fd - dh) * (ah * bh)| ≤
        ed * (Bc + ea) * (Bc + eb) := by
    rw [abs_mul, abs_mul]
    calc
      |fd - dh| * (|ah| * |bh|) ≤
          ed * (|ah| * |bh|) :=
        mul_le_mul_of_nonneg_right hd
          (mul_nonneg (abs_nonneg _) (abs_nonneg _))
      _ ≤ ed * ((Bc + ea) * |bh|) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_right hah (abs_nonneg _)) hed
      _ ≤ ed * ((Bc + ea) * (Bc + eb)) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_left hbh (add_nonneg hBc hea)) hed
      _ = ed * (Bc + ea) * (Bc + eb) := by ring
  have hterm2 :
      |fd * ((fa - ah) * bh)| ≤ Bd * ea * (Bc + eb) := by
    rw [abs_mul, abs_mul]
    calc
      |fd| * (|fa - ah| * |bh|) ≤
          Bd * (|fa - ah| * |bh|) :=
        mul_le_mul_of_nonneg_right hfd
          (mul_nonneg (abs_nonneg _) (abs_nonneg _))
      _ ≤ Bd * (ea * |bh|) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_right ha (abs_nonneg _)) hBd
      _ ≤ Bd * (ea * (Bc + eb)) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_left hbh hea) hBd
      _ = Bd * ea * (Bc + eb) := by ring
  have hterm3 :
      |fd * (fa * (fb - bh))| ≤ Bd * Bc * eb := by
    rw [abs_mul, abs_mul]
    calc
      |fd| * (|fa| * |fb - bh|) ≤
          Bd * (|fa| * |fb - bh|) :=
        mul_le_mul_of_nonneg_right hfd
          (mul_nonneg (abs_nonneg _) (abs_nonneg _))
      _ ≤ Bd * (Bc * |fb - bh|) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_right hfa (abs_nonneg _)) hBd
      _ ≤ Bd * (Bc * eb) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_left hb hBc) hBd
      _ = Bd * Bc * eb := by ring
  rw [show fd * (fa * fb) - dh * (ah * bh) =
      (fd - dh) * (ah * bh) +
        fd * ((fa - ah) * bh) +
        fd * (fa * (fb - bh)) by ring]
  calc
    |(fd - dh) * (ah * bh) + fd * ((fa - ah) * bh) +
        fd * (fa * (fb - bh))| ≤
      |(fd - dh) * (ah * bh)| + |fd * ((fa - ah) * bh)| +
        |fd * (fa * (fb - bh))| := by
      exact (abs_add_le _ _).trans
        (add_le_add (abs_add_le _ _) le_rfl)
    _ ≤ ed * (Bc + ea) * (Bc + eb) +
        Bd * ea * (Bc + eb) + Bd * Bc * eb :=
      add_le_add (add_le_add hterm1 hterm2) hterm3

/-- Generic semantic theorem for the bounded ledger.  Its only factor-bound
premises concern the exact represented functions, not stored coefficients. -/
theorem boundedTripleProductApprox_encloses
    {fd fa fb : ℝ → ℝ} (d a b : Approx)
    (hd : RoundedRatPoly.Encloses 1 fd d)
    (ha : RoundedRatPoly.Encloses 1 fa a)
    (hb : RoundedRatPoly.Encloses 1 fb b)
    (hfd : ∀ x : ℝ, |x| ≤ 1 → |fd x| ≤ (defectValueBoundQ : ℝ))
    (hfa : ∀ x : ℝ, |x| ≤ 1 → |fa x| ≤ (componentValueBoundQ : ℝ))
    (hfb : ∀ x : ℝ, |x| ≤ 1 → |fb x| ≤ (componentValueBoundQ : ℝ)) :
    RoundedRatPoly.Encloses 1
      (fun x => fd x * (fa x * fb x))
      (boundedTripleProductApprox d a b) := by
  intro x hx
  have hdAt := hd x hx
  have haAt := ha x hx
  have hbAt := hb x hx
  have hdError0Q := RoundedRatPoly.error_nonneg_of_encloses
    (h := (1 : ℚ)) (by norm_num) hd
  have haError0Q := RoundedRatPoly.error_nonneg_of_encloses
    (h := (1 : ℚ)) (by norm_num) ha
  have hdError0 : (0 : ℝ) ≤ (d.error : ℝ) := by
    exact_mod_cast hdError0Q
  have haError0 : (0 : ℝ) ≤ (a.error : ℝ) := by
    exact_mod_cast haError0Q
  have hBd0 : (0 : ℝ) ≤ (defectValueBoundQ : ℝ) := by
    norm_num [defectValueBoundQ]
  have hBc0 : (0 : ℝ) ≤ (componentValueBoundQ : ℝ) := by
    norm_num [componentValueBoundQ]
  have hx1 : |x| ≤ (1 : ℝ) := by
    simpa using hx
  change
    |fd x * (fa x * fb x) -
        RoundedRatPoly.evalReal
          (DenseRatPoly.mul d.coeffs
            (DenseRatPoly.mul a.coeffs b.coeffs)) x| ≤
      (boundedTripleError d a b : ℝ)
  rw [RoundedRatPoly.evalReal_mul, RoundedRatPoly.evalReal_mul]
  calc
    |fd x * (fa x * fb x) -
        RoundedRatPoly.evalReal d.coeffs x *
          (RoundedRatPoly.evalReal a.coeffs x *
            RoundedRatPoly.evalReal b.coeffs x)| ≤
      (d.error : ℝ) *
          ((componentValueBoundQ : ℝ) + (a.error : ℝ)) *
          ((componentValueBoundQ : ℝ) + (b.error : ℝ)) +
        (defectValueBoundQ : ℝ) * (a.error : ℝ) *
          ((componentValueBoundQ : ℝ) + (b.error : ℝ)) +
        (defectValueBoundQ : ℝ) * (componentValueBoundQ : ℝ) *
          (b.error : ℝ) :=
      abs_triple_sub_le (hfd x hx1) (hfa x hx1) (hfb x hx1)
        hdAt haAt hbAt hdError0 haError0 hBd0 hBc0
    _ = (boundedTripleError d a b : ℝ) := by
      simp [boundedTripleError]

/-- Canonical specialization for an arbitrary semantically certified panel
cache. -/
theorem boundedTripleProductApprox_encloses_canonical
    {cache : PanelCache} {k : Fin 32}
    (hcache : cache.EnclosesCanonical k)
    (kind : P2SelectedKind) (i j : Fin 24) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedIntegrand kind i j k))
      (boundedTripleProductApprox cache.defect
        (cache.component kind j) (cache.component kind i)) := by
  have hproduct := boundedTripleProductApprox_encloses
    cache.defect (cache.component kind j) (cache.component kind i)
    hcache.defect_encloses
    (hcache.component_encloses kind j)
    (hcache.component_encloses kind i)
    (fun x hx => abs_evalReal_exactNormalizedDefect_le k hx)
    (fun x hx => abs_evalReal_exactNormalizedComponent_le kind j k hx)
    (fun x hx => abs_evalReal_exactNormalizedComponent_le kind i k hx)
  intro x hx
  rw [evalReal_exactNormalizedIntegrand_eq_canonicalFactors]
  exact hproduct x hx

/-! ### Tight integral balls -/

/-- Original-coordinate integral ball with the unchanged exact convolution
center and the new bounded-value radius. -/
def boundedTripleIntegralBall
    (halfWidth : ℚ) (d a b : Approx) : QBall :=
  ⟨halfWidth * DenseRatPoly.exactIntegral
      (DenseRatPoly.mul d.coeffs
        (DenseRatPoly.mul a.coeffs b.coeffs)) (-1) 1,
    2 * halfWidth * boundedTripleError d a b⟩

/-- Formal record that changing the ledger did not change the rational
center. -/
@[simp] theorem boundedTripleIntegralBall_center_eq_tripleFactor
    (halfWidth : ℚ) (d a b : Approx) :
    (boundedTripleIntegralBall halfWidth d a b).center =
      (tripleFactorIntegralBall halfWidth d a b).center := rfl

/-- Tight direct-factor ball for one canonical cache entry. -/
def boundedTripleEntryBall
    (k : Fin 32) (cache : PanelCache)
    (kind : P2SelectedKind) (i j : Fin 24) : QBall :=
  boundedTripleIntegralBall (p2PanelHalfWidthQ k.val)
    cache.defect (cache.component kind j) (cache.component kind i)

@[simp] theorem boundedTripleEntryBall_center_eq_tripleFactor
    (k : Fin 32) (cache : PanelCache)
    (kind : P2SelectedKind) (i j : Fin 24) :
    (boundedTripleEntryBall k cache kind i j).center =
      (tripleFactorEntryBall k cache kind i j).center := rfl

/-- The bounded-value ledger encloses the canonical rational panel integral
for every semantically certified cache. -/
theorem abs_p2PanelIntegralQ_sub_boundedTripleEntryBallCenter_le
    {cache : PanelCache} {k : Fin 32}
    (hcache : cache.EnclosesCanonical k)
    (kind : P2SelectedKind) (i j : Fin 24) :
    |DenseRatPoly.p2PanelIntegralQ kind i j k.val -
        (boundedTripleEntryBall k cache kind i j).center| ≤
      (boundedTripleEntryBall k cache kind i j).radius := by
  have happrox := boundedTripleProductApprox_encloses_canonical
    hcache kind i j
  have h := abs_p2PanelIntegralQ_sub_entryBallFromApproxCenter_le
    kind i j k
    (boundedTripleProductApprox cache.defect
      (cache.component kind j) (cache.component kind i)) happrox
  simpa [boundedTripleEntryBall, boundedTripleIntegralBall,
    entryBallFromApprox, boundedTripleProductApprox] using h

/-- Generated-entry wrapper around the tight direct-factor ball. -/
def boundedTriplePanelBall
    (cache : PanelCache) (k : Fin 32) (r : Fin 600) : QBall :=
  let e := generatedEntryAt r
  boundedTripleEntryBall k cache
    (p2EntrySelectedKind e.block) e.row e.col

/-! ### Moment-staged tight centers -/

/-- Tight QBall whose exact center is consumed from a supplied matvec. -/
def boundedMomentEntryBall
    (data : PanelMomentData) (cache : PanelCache) (k : Fin 32)
    (kind : P2SelectedKind) (i j : Fin 24)
    (hrows : (cache.component kind j).coeffs.length ≤ 149) : QBall :=
  ⟨p2PanelHalfWidthQ k.val *
      hankelDotFromVector (cache.component kind j).coeffs
        (data.matvecs kind i) hrows,
    2 * p2PanelHalfWidthQ k.val *
      boundedTripleError cache.defect
        (cache.component kind j) (cache.component kind i)⟩

/-- Correct supplied moments and matvecs identify the staged tight ball with
the direct exact-convolution tight ball. -/
theorem boundedMomentEntryBall_eq_boundedTripleEntryBall
    {data : PanelMomentData} {cache : PanelCache}
    (hdata : data.CorrectFor cache)
    (k : Fin 32) (kind : P2SelectedKind) (i j : Fin 24) :
    boundedMomentEntryBall data cache k kind i j
        (hdata.component_length_le kind j) =
      boundedTripleEntryBall k cache kind i j := by
  have hdot := hankelDotFromVector_eq_hankelBilinear
    cache.defect.coeffs (cache.component kind j).coeffs
    (cache.component kind i).coeffs (data.matvecs kind i)
    (hdata.component_length_le kind j)
    (hdata.matvec_correct kind i)
  simp [boundedMomentEntryBall, boundedTripleEntryBall,
    boundedTripleIntegralBall,
    exactIntegral_triple_eq_hankelBilinear, hdot]

/-- Generated-entry wrapper around the moment-staged tight ball. -/
def boundedMomentPanelBall
    (data : PanelMomentData) (cache : PanelCache) (k : Fin 32)
    (hdata : data.CorrectFor cache) (r : Fin 600) : QBall :=
  let e := generatedEntryAt r
  boundedMomentEntryBall data cache k
    (p2EntrySelectedKind e.block) e.row e.col
    (hdata.component_length_le (p2EntrySelectedKind e.block) e.col)

theorem boundedMomentPanelBall_eq_boundedTriplePanelBall
    {data : PanelMomentData} {cache : PanelCache}
    (hdata : data.CorrectFor cache) (k : Fin 32) (r : Fin 600) :
    boundedMomentPanelBall data cache k hdata r =
      boundedTriplePanelBall cache k r := by
  unfold boundedMomentPanelBall boundedTriplePanelBall
  dsimp only
  exact boundedMomentEntryBall_eq_boundedTripleEntryBall hdata k
    (p2EntrySelectedKind (generatedEntryAt r).block)
    (generatedEntryAt r).row (generatedEntryAt r).col

/-- Canonical analytic enclosure stated directly for the staged tight ball. -/
theorem abs_p2PanelIntegralQ_sub_boundedMomentPanelBallCenter_le
    {data : PanelMomentData} {cache : PanelCache}
    (hdata : data.CorrectFor cache) {k : Fin 32}
    (hcache : cache.EnclosesCanonical k) (r : Fin 600) :
    let e := generatedEntryAt r
    |DenseRatPoly.p2PanelIntegralQ
          (p2EntrySelectedKind e.block) e.row e.col k.val -
        (boundedMomentPanelBall data cache k hdata r).center| ≤
      (boundedMomentPanelBall data cache k hdata r).radius := by
  dsimp only
  rw [boundedMomentPanelBall_eq_boundedTriplePanelBall hdata]
  simpa [boundedTriplePanelBall, generatedEntryAt] using
    abs_p2PanelIntegralQ_sub_boundedTripleEntryBallCenter_le
      hcache
      (p2EntrySelectedKind (generatedEntryAt r).block)
      (generatedEntryAt r).row (generatedEntryAt r).col

/-! ### Tight generated-target handoff -/

/-- Finite refinement predicate for the tight staged balls.  This is kept
separate from `PanelTargetRefinements`, whose source balls use the older
coefficient-majorant radius. -/
def BoundedMomentPanelTargetRefinements
    (cache : Fin 32 → PanelCache)
    (data : Fin 32 → PanelMomentData)
    (hdata : ∀ k, (data k).CorrectFor (cache k)) : Prop :=
  ∀ (k : Fin 32) (r : Fin 600),
    (boundedMomentPanelBall
      (data k) (cache k) k (hdata k) r).Refines
        (coarsePanelBall k r)

/-- The 32 tight staged enclosures and their finite target refinements bound
the exact canonical entry sum by the existing coarse aggregate ball. -/
theorem abs_p2EntryPanelSumQ_sub_coarseAggregateCenter_le_of_bounded
    (cache : Fin 32 → PanelCache)
    (data : Fin 32 → PanelMomentData)
    (hdata : ∀ k, (data k).CorrectFor (cache k))
    (hcache : ∀ k, (cache k).EnclosesCanonical k)
    (hrefines : BoundedMomentPanelTargetRefinements cache data hdata)
    (r : Fin 600) :
    |DenseRatPoly.p2EntryPanelSumQ (p2UpperEntryAt r).val -
        (coarseAggregateBall r).center| ≤
      (coarseAggregateBall r).radius := by
  unfold coarseAggregateBall
  unfold DenseRatPoly.p2EntryPanelSumQ
  rw [← Fin.sum_univ_eq_sum_range]
  apply QBall.abs_sum_sub_finSum_center_le
  intro k
  exact QBall.abs_sub_center_le_of_refines
    (by
      simpa [generatedEntryAt] using
        abs_p2PanelIntegralQ_sub_boundedMomentPanelBallCenter_le
          (hdata k) (hcache k) r)
    (hrefines k r)

/-- Complete generic downstream handoff for the tight ledger.  Generated
modules need only provide abstract panel data, its semantic row checks, and
the finite rational refinements. -/
theorem bandSumCertificates_of_boundedMomentTargetRefinements
    (cache : Fin 32 → PanelCache)
    (data : Fin 32 → PanelMomentData)
    (hdata : ∀ k, (data k).CorrectFor (cache k))
    (hcache : ∀ k, (cache k).EnclosesCanonical k)
    (hrefines : BoundedMomentPanelTargetRefinements cache data hdata) :
    P2PanelCertificateAggregate.BandSumCertificates := by
  apply P2RoundedBandCertificate.bandSumCertificates_of_fitsGeneratedBandTable
    (fun r => (coarseAggregateBall r).center)
    (fun r => (coarseAggregateBall r).radius)
  · exact abs_p2EntryPanelSumQ_sub_coarseAggregateCenter_le_of_bounded
      cache data hdata hcache hrefines
  · exact P2RoundedPanelRefinement.fitsGeneratedBandTable_of_allCentersMatch
      P2RoundedPanelTargetAggregate.allCentersMatch

end P2RoundedBoundedTriple

end RHP2Bridge
