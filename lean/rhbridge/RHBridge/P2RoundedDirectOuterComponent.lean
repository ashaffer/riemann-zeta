/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedTruncatedOuter

/-!
# Directly composed spherical components for canonical `p = 2`

This module provides an alternative to the rounded-Horner component evaluator.
It first forms the exact rational coefficient composition, rounds that result
once, and then applies the selected scale with one final rounding barrier.
The grid is an explicit parameter so certificate scouts can compare smaller
grids without changing the production evaluator.
-/

namespace RHP2Bridge

namespace P2RoundedDirectOuterComponent

open P2RoundedCanonical
open P2RoundedSharedEvaluator
open P2RoundedTruncatedOuter

abbrev Approx := RoundedRatPoly.Approx

/-- Compose a spherical outer with the exact normalized panel argument in one
coefficient operation, then apply the canonical selected-mode scale. -/
def componentApproxFromOuter
    (cells : Nat) (outer : Approx) (kind : P2SelectedKind)
    (i : Fin 24) (k : Fin 32) : Approx :=
  RoundedRatPoly.scale cells 1
    (RatPoly.p2SelectedPhaseQ kind i.val *
      p2SelectedScaleCenterQ kind i)
    (RoundedRatPoly.comp cells 1 outer
      (normalizedSphericalArgumentApprox k))

/-- Direct composition is semantically valid whenever the supplied outer is
already known on the exact domain of this panel. -/
theorem componentApproxFromOuter_encloses_on_panel
    (cells : Nat) (_hCells : 0 < cells)
    (outer : Approx) (kind : P2SelectedKind)
    (i : Fin 24) (k : Fin 32)
    (hOuter : RoundedRatPoly.Encloses (panelOuterDomain k)
      (RoundedRatPoly.evalReal
        (DenseRatPoly.sphericalJRealPolynomial
          (p2SelectedDegree kind i.val) 100)) outer) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent kind i k))
      (componentApproxFromOuter cells outer kind i k) := by
  let inner := normalizedSphericalArgumentApprox k
  have hInner : RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (normalizedSphericalArgumentPoly k)) inner := by
    simpa [inner, normalizedSphericalArgumentApprox] using
      RoundedRatPoly.exact_encloses 1
        (normalizedSphericalArgumentPoly k)
  have hComp := RoundedRatPoly.comp_encloses cells
    (h := (1 : ℚ)) (by norm_num) outer inner
    (by simpa [panelOuterDomain, inner] using hOuter) hInner
  have hScale := RoundedRatPoly.scale_encloses cells
    (h := (1 : ℚ)) (by norm_num)
    (RatPoly.p2SelectedPhaseQ kind i.val *
      p2SelectedScaleCenterQ kind i)
    (RoundedRatPoly.comp cells 1 outer inner) hComp
  intro t ht
  rw [evalReal_exactNormalizedComponent_eq_outer]
  simpa [componentApproxFromOuter, inner] using hScale t ht

/-- A global spherical enclosure restricts to the panel domain and therefore
certifies the direct component evaluator. -/
theorem componentApproxFromOuter_encloses
    (cells : Nat) (hCells : 0 < cells)
    (outer : Approx) (kind : P2SelectedKind)
    (i : Fin 24) (k : Fin 32)
    (hOuter : RoundedRatPoly.Encloses 22
      (RoundedRatPoly.evalReal
        (DenseRatPoly.sphericalJRealPolynomial
          (p2SelectedDegree kind i.val) 100)) outer) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent kind i k))
      (componentApproxFromOuter cells outer kind i k) := by
  have hDomain : panelOuterDomain k ≤ 22 := by
    simpa [panelOuterDomain] using
      normalizedSphericalArgumentDomain_le_22 k
  exact componentApproxFromOuter_encloses_on_panel cells hCells outer kind i k
    (hOuter.mono_domain hDomain)

/-- Direct composition after the independently verified coefficient-prefix
truncation of a global spherical outer. -/
def componentApproxFromTruncatedOuter
    (cells : Nat) (outer : Approx) (L : Nat)
    (kind : P2SelectedKind) (i : Fin 24) (k : Fin 32) : Approx :=
  componentApproxFromOuter cells
    (truncateOuter (panelOuterDomain k) L outer) kind i k

theorem componentApproxFromTruncatedOuter_encloses
    (cells : Nat) (hCells : 0 < cells)
    (outer : Approx) (L : Nat) (kind : P2SelectedKind)
    (i : Fin 24) (k : Fin 32)
    (hOuter : RoundedRatPoly.Encloses 22
      (RoundedRatPoly.evalReal
        (DenseRatPoly.sphericalJRealPolynomial
          (p2SelectedDegree kind i.val) 100)) outer) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent kind i k))
      (componentApproxFromTruncatedOuter cells outer L kind i k) := by
  have hDomain0 : 0 ≤ panelOuterDomain k := by
    unfold panelOuterDomain
    exact add_nonneg
      (RoundedRatPoly.absBound_nonneg _ (by norm_num)) (by
        simp [normalizedSphericalArgumentApprox, RoundedRatPoly.exact])
  have hDomain22 : panelOuterDomain k ≤ 22 := by
    simpa [panelOuterDomain] using
      normalizedSphericalArgumentDomain_le_22 k
  have hTruncated := truncateOuter_encloses outer L
    hDomain0 hDomain22 hOuter
  exact componentApproxFromOuter_encloses_on_panel cells hCells
    (truncateOuter (panelOuterDomain k) L outer) kind i k hTruncated

/-- All 24 parity-selected components using per-panel/per-mode truncation
lengths and the direct coefficient-composition evaluator. -/
def componentVectorFromTruncatedOuters
    (cells : Nat) (outers : Vector Approx 48)
    (outerLength : Fin 32 → Fin 48 → Nat)
    (kind : P2SelectedKind) (k : Fin 32) : Vector Approx 24 :=
  Vector.ofFn fun i =>
    let n := selectedDegreeFin kind i
    componentApproxFromTruncatedOuter cells (outers.get n)
      (outerLength k n) kind i k

theorem componentVectorFromTruncatedOuters_encloses
    (cells : Nat) (hCells : 0 < cells)
    {outers : Vector Approx 48}
    (hOuters : SphericalOutersEnclose outers)
    (outerLength : Fin 32 → Fin 48 → Nat)
    (kind : P2SelectedKind) (k : Fin 32) (i : Fin 24) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent kind i k))
      ((componentVectorFromTruncatedOuters
        cells outers outerLength kind k).get i) := by
  simpa [componentVectorFromTruncatedOuters, sphericalOuterExact,
      selectedDegreeFin] using
    componentApproxFromTruncatedOuter_encloses cells hCells
      (outers.get (selectedDegreeFin kind i))
      (outerLength k (selectedDegreeFin kind i)) kind i k
      (hOuters.encloses (selectedDegreeFin kind i))

end P2RoundedDirectOuterComponent

end RHP2Bridge
