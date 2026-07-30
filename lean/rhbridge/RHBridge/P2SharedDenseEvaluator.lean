/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2PoleCanonicalDense
import RHBridge.P2EntryTable
import Batteries.Data.Vector.Lemmas

/-!
# Shared executable evaluator for the canonical `p = 2` matrix

The direct dense formula rebuilds the common defect and component
polynomials for every matrix entry.  This evaluator instead streams through
the 32 panels.  On each panel it constructs one defect polynomial and the 48
selected-component polynomials, uses that cache to update all 600
upper-triangular sums, and then discards the cache.

All arrays have fixed sizes.  The semantic theorems below prove that their
entries equal the independently defined canonical rational panel sums.
-/

namespace RHP2Bridge

namespace DenseRatPoly

/-- The 24 component polynomials of each parity on one panel. -/
structure P2PanelCache where
  defect : Poly
  evenComponents : Vector Poly 24
  oddComponents : Vector Poly 24

def p2ComponentVector
    (kind : P2SelectedKind) (c : ℚ) : Vector Poly 24 :=
  Vector.ofFn fun k =>
    p2SelectedComponent100ScaleCenterPolynomial kind k c

def p2BuildPanelCache (k : ℕ) : P2PanelCache where
  defect := p2DefectPanelPolynomial (p2PanelCenterQ k) 32
  evenComponents := p2ComponentVector .even (p2PanelCenterQ k)
  oddComponents := p2ComponentVector .odd (p2PanelCenterQ k)

def P2PanelCache.component
    (cache : P2PanelCache) (kind : P2SelectedKind) (i : Fin 24) : Poly :=
  match kind with
  | .even => cache.evenComponents.get i
  | .odd => cache.oddComponents.get i

@[simp] theorem p2ComponentVector_get
    (kind : P2SelectedKind) (c : ℚ) (i : Fin 24) :
    (p2ComponentVector kind c).get i =
      p2SelectedComponent100ScaleCenterPolynomial kind i c := by
  simp [p2ComponentVector]

@[simp] theorem p2BuildPanelCache_component
    (kind : P2SelectedKind) (k : ℕ) (i : Fin 24) :
    (p2BuildPanelCache k).component kind i =
      p2SelectedComponent100ScaleCenterPolynomial
        kind i (p2PanelCenterQ k) := by
  cases kind <;> simp [p2BuildPanelCache, P2PanelCache.component]

/-- One exact panel integral using a shared panel cache. -/
def p2PanelIntegralFromCache
    (cache : P2PanelCache) (h : ℚ)
    (kind : P2SelectedKind) (i j : Fin 24) : ℚ :=
  exactIntegral
    (mul cache.defect
      (mul (cache.component kind j) (cache.component kind i)))
    (-h) h

theorem p2PanelIntegralFromCache_eq
    (kind : P2SelectedKind) (i j : Fin 24) (k : ℕ) :
    p2PanelIntegralFromCache (p2BuildPanelCache k)
        (p2PanelHalfWidthQ k) kind i j =
      p2PanelIntegralQ kind i j k := by
  cases kind <;>
    simp [p2PanelIntegralFromCache, p2BuildPanelCache,
      P2PanelCache.component, p2PanelIntegralQ,
      p2ScaleCenteredPanelIntegralQ,
      p2ScaleCenteredPanelIntegrandPolynomial]

/-- Upper-triangular entry attached to a generated row. -/
def p2GeneratedEntryAt (r : Fin 600) : P2EntryIndex :=
  (p2UpperEntryAt r).val

/-- Update all 600 exact sums with a single shared panel cache. -/
def p2AddPanelToSums
    (sums : Vector ℚ 600) (k : ℕ) : Vector ℚ 600 :=
  let cache := p2BuildPanelCache k
  Vector.ofFn fun r =>
    let e := p2GeneratedEntryAt r
    sums.get r +
      p2PanelIntegralFromCache cache (p2PanelHalfWidthQ k)
        (p2EntrySelectedKind e.block) e.row e.col

/-- Stream the first `N` panels into all 600 upper-triangular sums. -/
def p2SharedPanelSums : ℕ → Vector ℚ 600
  | 0 => Vector.replicate 600 0
  | N + 1 => p2AddPanelToSums (p2SharedPanelSums N) N

@[simp] theorem p2AddPanelToSums_get
    (sums : Vector ℚ 600) (k : ℕ) (r : Fin 600) :
    (p2AddPanelToSums sums k).get r =
      sums.get r +
        p2PanelIntegralQ
          (p2EntrySelectedKind (p2GeneratedEntryAt r).block)
          (p2GeneratedEntryAt r).row (p2GeneratedEntryAt r).col k := by
  simp [p2AddPanelToSums, p2GeneratedEntryAt,
    p2PanelIntegralFromCache_eq]

theorem p2SharedPanelSums_get (N : ℕ) (r : Fin 600) :
    (p2SharedPanelSums N).get r =
      ∑ k ∈ Finset.range N,
        p2PanelIntegralQ
          (p2EntrySelectedKind (p2GeneratedEntryAt r).block)
          (p2GeneratedEntryAt r).row (p2GeneratedEntryAt r).col k := by
  induction N with
  | zero => simp [p2SharedPanelSums]
  | succ N ih =>
      rw [p2SharedPanelSums, p2AddPanelToSums_get, ih,
        Finset.sum_range_succ]

/-- The shared vector agrees entrywise with the canonical dense definition. -/
theorem p2SharedPanelSums_eq_entryPanelSumQ (r : Fin 600) :
    (p2SharedPanelSums 32).get r =
      p2EntryPanelSumQ (p2GeneratedEntryAt r) := by
  rw [p2SharedPanelSums_get]
  rfl

/-! ## Shared pole coefficients and complete centers -/

/-- All 48 finite pole coefficients are computed once. -/
def p2PoleCoeffVector : Vector ℚ 48 :=
  Vector.ofFn p2PoleTaylorCoeffScaleCenterQ

@[simp] theorem p2PoleCoeffVector_get (n : Fin 48) :
    p2PoleCoeffVector.get n = p2PoleTaylorCoeffScaleCenterQ n := by
  simp [p2PoleCoeffVector]

def p2EntryTaylorPoleCenterFromVector
    (coeffs : Vector ℚ 48) (e : P2EntryIndex) : ℚ :=
  2 * coeffs.get (p2EntryPoleMode e.block e.col) *
    coeffs.get (p2EntryPoleMode e.block e.row)

@[simp] theorem p2EntryTaylorPoleCenterFromVector_eq
    (e : P2EntryIndex) :
    p2EntryTaylorPoleCenterFromVector p2PoleCoeffVector e =
      p2EntryTaylorPoleCenterQ e := by
  simp [p2EntryTaylorPoleCenterFromVector,
    p2EntryTaylorPoleCenterQ]

def p2ApproxCenterFromVectors
    (sums : Vector ℚ 600) (poles : Vector ℚ 48)
    (r : Fin 600) : ℚ :=
  let e := p2GeneratedEntryAt r
  p2AlphaCenterQ * p2EntryDiagonalIndicatorQ e +
    p2InvTwoPiCenterQ * (2 * sums.get r) +
    p2EntryPoleSignQ e.block *
      p2EntryTaylorPoleCenterFromVector poles e

/-- Closed finite predicate evaluated with one shared panel-sum vector and
one shared pole vector.  The `let` bindings are intentional: native
evaluation constructs each closed vector once. -/
def P2SharedGeneratedCenterFits : Prop :=
  let sums := p2SharedPanelSums 32
  let poles := p2PoleCoeffVector
  ∀ r : Fin 600,
    |p2ApproxCenterFromVectors sums poles r -
      p2StoredCenterQ (p2GeneratedEntryAt r)| ≤ 1 / 10 ^ 13

theorem p2EntryCenterFits_of_shared
    (h : P2SharedGeneratedCenterFits) (r : Fin 600) :
    p2EntryCenterFits (p2GeneratedEntryAt r) := by
  have hr := h r
  simp only [p2ApproxCenterFromVectors] at hr
  rw [p2SharedPanelSums_eq_entryPanelSumQ,
    p2EntryTaylorPoleCenterFromVector_eq] at hr
  simpa [p2EntryCenterFits, p2EntryApproxCenterQ] using hr

end DenseRatPoly

end RHP2Bridge
