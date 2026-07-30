/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2CanonicalRounded

/-!
# Kernel-checkable decomposition of the canonical `p = 2` defect factor

The complete exact normalized defect is cheap for compiled evaluation but
too large for a single kernel `decide` reduction.  This module instead rounds
each of the 64 reciprocal-prefix terms separately, rounds the nonprefix term
separately, and combines the resulting enclosures with bounded-denominator
rounded addition.  A generated certificate can checkpoint four prefix terms
per small kernel module and still obtain one semantic enclosure of the exact
canonical defect.
-/

namespace RHP2Bridge

namespace P2RoundedFactorDecomposition

open scoped BigOperators
open P2RoundedCanonical
open RoundedRatPoly

/-- Exact normalized polynomial for one of the 64 finite-prefix terms. -/
def normalizedPrefixTermPoly (n : ℕ) (k : Fin 32) : DenseRatPoly.Poly :=
  DenseRatPoly.affine
    (DenseRatPoly.quarterPrefixTermPolynomial
      n (p2PanelCenterQ k.val) 32)
    0 (p2PanelHalfWidthQ k.val)

/-- One independently rounded prefix term. -/
def normalizedPrefixTermApprox (n : ℕ) (k : Fin 32) : Approx :=
  rounded gridCells 1 (normalizedPrefixTermPoly n k)

/-- Exact normalized nonprefix summand, including the panel shift. -/
def normalizedNonPrefixPoly (k : Fin 32) : DenseRatPoly.Poly :=
  DenseRatPoly.affine
    DenseRatPoly.p2RationalNonPrefixPoly
    (p2PanelCenterQ k.val) (p2PanelHalfWidthQ k.val)

def normalizedNonPrefixApprox (k : Fin 32) : Approx :=
  rounded gridCells 1 (normalizedNonPrefixPoly k)

/-- Rounded sum of the 64 independently checkpointable prefix terms. -/
def normalizedPrefixSumApprox (k : Fin 32) : Approx :=
  sumRangeRounded gridCells 1 64 fun n =>
    normalizedPrefixTermApprox n k

/-- Replacement for the monolithic rounded defect.  Every intermediate
error is ceiling-compressed to the common `10^-200` grid. -/
def decomposedDefectApprox (k : Fin 32) : Approx :=
  add gridCells 1 (normalizedPrefixSumApprox k)
    (normalizedNonPrefixApprox k)

theorem evalReal_sumRange
    (N : ℕ) (f : ℕ → DenseRatPoly.Poly) (x : ℝ) :
    evalReal (DenseRatPoly.sumRange N f) x =
      ∑ n ∈ Finset.range N, evalReal (f n) x := by
  induction N with
  | zero => simp [DenseRatPoly.sumRange, DenseRatPoly.zero]
  | succ N ih =>
      rw [DenseRatPoly.sumRange, evalReal_add, ih,
        Finset.sum_range_succ]

theorem evalReal_normalizedDefect_eq_decomposition
    (k : Fin 32) (x : ℝ) :
    evalReal (normalizedDefectExpr k).denote x =
      (∑ n ∈ Finset.range 64,
          evalReal (normalizedPrefixTermPoly n k) x) +
        evalReal (normalizedNonPrefixPoly k) x := by
  rw [evalReal_normalizedDefectExpr_eq_canonical]
  simp [DenseRatPoly.p2DefectPanelPolynomial,
    DenseRatPoly.quarterDifferenceFinitePrefixPolynomial,
    normalizedPrefixTermPoly, normalizedNonPrefixPoly,
    DenseRatPoly.affine, DenseRatPoly.shift,
    evalReal_add, evalReal_comp, evalReal_sumRange,
    evalReal_cons, P2RoundedCanonical.evalReal_dense_nil]

theorem normalizedPrefixTermApprox_encloses (n : ℕ) (k : Fin 32) :
    Encloses 1 (evalReal (normalizedPrefixTermPoly n k))
      (normalizedPrefixTermApprox n k) := by
  exact rounded_encloses gridCells (by norm_num) _

theorem normalizedNonPrefixApprox_encloses (k : Fin 32) :
    Encloses 1 (evalReal (normalizedNonPrefixPoly k))
      (normalizedNonPrefixApprox k) := by
  exact rounded_encloses gridCells (by norm_num) _

theorem normalizedPrefixSumApprox_encloses (k : Fin 32) :
    Encloses 1
      (fun x => ∑ n ∈ Finset.range 64,
        evalReal (normalizedPrefixTermPoly n k) x)
      (normalizedPrefixSumApprox k) := by
  exact sumRangeRounded_encloses gridCells (by norm_num)
    (fun n => normalizedPrefixTermApprox n k)
    (fun n => normalizedPrefixTermApprox_encloses n k) 64

/-- The decomposed, checkpoint-friendly computation encloses the same exact
canonical normalized defect as the monolithic definition. -/
theorem decomposedDefectApprox_encloses (k : Fin 32) :
    Encloses 1 (evalReal (normalizedDefectExpr k).denote)
      (decomposedDefectApprox k) := by
  have hAdd := add_encloses gridCells (h := (1 : ℚ)) (by norm_num)
    (normalizedPrefixSumApprox k) (normalizedNonPrefixApprox k)
    (normalizedPrefixSumApprox_encloses k)
    (normalizedNonPrefixApprox_encloses k)
  intro x hx
  rw [evalReal_normalizedDefect_eq_decomposition]
  simpa [decomposedDefectApprox] using hAdd x hx

end P2RoundedFactorDecomposition

end RHP2Bridge
