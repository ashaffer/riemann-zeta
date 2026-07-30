/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedSharedEvaluator

/-!
# Semantically truncated spherical outers for canonical `p = 2`

A global spherical enclosure is much longer than most normalized panels
need.  We retain the first `L` low-degree coefficients and add the Horner
absolute bound of the padded dropped tail to the error.  The resulting
enclosure is proved in ordinary Lean before it is composed with the panel's
affine spherical argument.
-/

namespace RHP2Bridge

namespace P2RoundedTruncatedOuter

open P2RoundedSharedEvaluator
open P2RoundedCanonical

abbrev Approx := RoundedRatPoly.Approx

/-- The high-degree tail, padded so its coefficients retain their original
degrees. -/
def droppedTail (L : ℕ) (coeffs : DenseRatPoly.Poly) : DenseRatPoly.Poly :=
  List.replicate L 0 ++ coeffs.drop L

/-- Keep the first `L` coefficients and account for every omitted term on
`[-H,H]` in the error. -/
def truncateOuter (H : ℚ) (L : ℕ) (outer : Approx) : Approx where
  coeffs := outer.coeffs.take L
  error := outer.error + RoundedRatPoly.absBound (droppedTail L outer.coeffs) H

@[simp] theorem evalReal_nil (x : ℝ) :
    RoundedRatPoly.evalReal ([] : DenseRatPoly.Poly) x = 0 := by
  simpa [DenseRatPoly.zero] using RoundedRatPoly.evalReal_zero x

@[simp] theorem evalReal_replicate_zero (L : ℕ) (x : ℝ) :
    RoundedRatPoly.evalReal (List.replicate L (0 : ℚ)) x = 0 := by
  induction L with
  | zero =>
      simp [RoundedRatPoly.evalReal, DenseRatPoly.realize]
  | succ L ih =>
      simp [List.replicate_succ, RoundedRatPoly.evalReal_cons, ih]

/-- Pointwise decomposition into the retained prefix and degree-preserving
dropped tail. -/
theorem evalReal_take_add_droppedTail
    (coeffs : DenseRatPoly.Poly) (L : ℕ) (x : ℝ) :
    RoundedRatPoly.evalReal coeffs x =
      RoundedRatPoly.evalReal (coeffs.take L) x +
        RoundedRatPoly.evalReal (droppedTail L coeffs) x := by
  induction L generalizing coeffs with
  | zero =>
      simp [droppedTail]
  | succ L ih =>
      cases coeffs with
      | nil =>
          simp [droppedTail]
      | cons a coeffs =>
          rw [RoundedRatPoly.evalReal_cons,
            List.take_succ_cons, RoundedRatPoly.evalReal_cons]
          rw [show droppedTail (L + 1) (a :: coeffs) =
              0 :: droppedTail L coeffs by
            simp [droppedTail, List.replicate_succ]]
          rw [RoundedRatPoly.evalReal_cons, ih]
          ring

/-- Truncation preserves an enclosure after restricting its domain.  The
tail contribution is verified by `absBound`; no numerical tail estimate is
trusted. -/
theorem truncateOuter_encloses
    {D H : ℚ} {f : ℝ → ℝ} (outer : Approx) (L : ℕ)
    (hH : 0 ≤ H) (hHD : H ≤ D)
    (hOuter : RoundedRatPoly.Encloses D f outer) :
    RoundedRatPoly.Encloses H f (truncateOuter H L outer) := by
  have hRestricted : RoundedRatPoly.Encloses H f outer :=
    hOuter.mono_domain hHD
  intro x hx
  have hOuterAt := hRestricted x hx
  have hTail := RoundedRatPoly.abs_evalReal_le_absBound
    (droppedTail L outer.coeffs) hH hx
  change
    |f x - RoundedRatPoly.evalReal (outer.coeffs.take L) x| ≤
      ((outer.error + RoundedRatPoly.absBound
        (droppedTail L outer.coeffs) H : ℚ) : ℝ)
  rw [show
      f x - RoundedRatPoly.evalReal (outer.coeffs.take L) x =
        (f x - RoundedRatPoly.evalReal outer.coeffs x) +
          RoundedRatPoly.evalReal (droppedTail L outer.coeffs) x by
    rw [evalReal_take_add_droppedTail outer.coeffs L x]
    ring]
  calc
    |(f x - RoundedRatPoly.evalReal outer.coeffs x) +
        RoundedRatPoly.evalReal (droppedTail L outer.coeffs) x| ≤
      |f x - RoundedRatPoly.evalReal outer.coeffs x| +
        |RoundedRatPoly.evalReal (droppedTail L outer.coeffs) x| :=
          abs_add_le _ _
    _ ≤ (outer.error : ℝ) +
        (RoundedRatPoly.absBound
          (droppedTail L outer.coeffs) H : ℝ) :=
      add_le_add hOuterAt hTail
    _ = ((outer.error + RoundedRatPoly.absBound
        (droppedTail L outer.coeffs) H : ℚ) : ℝ) := by
      push_cast
      ring

/-- Panel specialization of `truncateOuter`. -/
def panelOuterDomain (k : Fin 32) : ℚ :=
  let inner := normalizedSphericalArgumentApprox k
  RoundedRatPoly.absBound inner.coeffs 1 + inner.error

def componentApproxFromTruncatedOuter
    (outer : Approx) (L : ℕ) (kind : P2SelectedKind)
    (i : Fin 24) (k : Fin 32) : Approx :=
  componentApproxFromOuter
    (truncateOuter (panelOuterDomain k) L outer) kind i k

/-- A global outer enclosure yields a shortened canonical component on any
panel; both the tail loss and all composition/rounding losses are included
in the resulting `Approx.error`. -/
theorem componentApproxFromTruncatedOuter_encloses
    (outer : Approx) (L : ℕ) (kind : P2SelectedKind)
    (i : Fin 24) (k : Fin 32)
    (hOuter : RoundedRatPoly.Encloses 22
      (RoundedRatPoly.evalReal
        (DenseRatPoly.sphericalJRealPolynomial
          (p2SelectedDegree kind i.val) 100)) outer) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent kind i k))
      (componentApproxFromTruncatedOuter outer L kind i k) := by
  let inner := normalizedSphericalArgumentApprox k
  let H := RoundedRatPoly.absBound inner.coeffs 1 + inner.error
  have hH0 : 0 ≤ H := by
    dsimp [H]
    exact add_nonneg
      (RoundedRatPoly.absBound_nonneg _ (by norm_num)) (by
        simp [inner, normalizedSphericalArgumentApprox,
          RoundedRatPoly.exact])
  have hH22 : H ≤ 22 := by
    simpa [H, inner, panelOuterDomain] using
      normalizedSphericalArgumentDomain_le_22 k
  have hTruncated : RoundedRatPoly.Encloses H
      (RoundedRatPoly.evalReal
        (DenseRatPoly.sphericalJRealPolynomial
          (p2SelectedDegree kind i.val) 100))
      (truncateOuter H L outer) :=
    truncateOuter_encloses outer L hH0 hH22 hOuter
  have hInner : RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (normalizedSphericalArgumentPoly k)) inner := by
    simpa [inner, normalizedSphericalArgumentApprox] using
      RoundedRatPoly.exact_encloses 1
        (normalizedSphericalArgumentPoly k)
  have hComp := RoundedRatPoly.compRounded_encloses gridCells
    (h := (1 : ℚ)) (by norm_num)
    (truncateOuter H L outer) inner hTruncated hInner
  have hScale := RoundedRatPoly.scale_encloses gridCells
    (h := (1 : ℚ)) (by norm_num)
    (RatPoly.p2SelectedPhaseQ kind i.val *
      p2SelectedScaleCenterQ kind i)
    (RoundedRatPoly.compRounded gridCells 1
      (truncateOuter H L outer) inner) hComp
  intro t ht
  rw [evalReal_exactNormalizedComponent_eq_outer]
  simpa [componentApproxFromTruncatedOuter, componentApproxFromOuter,
    panelOuterDomain, H, inner] using hScale t ht

/-- Build all 24 selected components from a shared outer vector and a small
per-panel/per-mode length table. -/
def componentVectorFromTruncatedOuters
    (outers : Vector Approx 48)
    (outerLength : Fin 32 → Fin 48 → ℕ)
    (kind : P2SelectedKind) (k : Fin 32) : Vector Approx 24 :=
  Vector.ofFn fun i =>
    let n := selectedDegreeFin kind i
    componentApproxFromTruncatedOuter (outers.get n)
      (outerLength k n) kind i k

theorem componentVectorFromTruncatedOuters_encloses
    {outers : Vector Approx 48}
    (hOuters : SphericalOutersEnclose outers)
    (outerLength : Fin 32 → Fin 48 → ℕ)
    (kind : P2SelectedKind) (k : Fin 32) (i : Fin 24) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent kind i k))
      ((componentVectorFromTruncatedOuters
        outers outerLength kind k).get i) := by
  simpa [componentVectorFromTruncatedOuters, sphericalOuterExact,
      selectedDegreeFin] using
    componentApproxFromTruncatedOuter_encloses
      (outers.get (selectedDegreeFin kind i))
      (outerLength k (selectedDegreeFin kind i)) kind i k
      (hOuters.encloses (selectedDegreeFin kind i))

end P2RoundedTruncatedOuter

end RHP2Bridge
