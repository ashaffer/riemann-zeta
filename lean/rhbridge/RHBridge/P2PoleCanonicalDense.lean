/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2CanonicalDense
import RHBridge.P2PoleRationalCenter

/-!
# Executable rational source of the canonical `p = 2` pole center

This is the pole analogue of `P2CanonicalDense`: finite Taylor and Legendre
polynomials are evaluated using executable coefficient lists, then proved to
realize the exact rational cores used by the analytic pole enclosure.
-/

namespace RHP2Bridge

namespace DenseRatPoly

open Polynomial
open scoped BigOperators

def poleTaylorPolynomial (s : ℚ) (m : ℕ) : Poly :=
  sumRange m fun k =>
    monomial k ((s / 2) ^ k / k.factorial)

/-- The integer shifted-Legendre formula, evaluated directly in `ℚ`. -/
def shiftedLegendre (n : ℕ) : Poly :=
  sumRange (n + 1) fun k =>
    monomial k
      ((-1 : ℚ) ^ k * (n.choose k : ℚ) * ((n + k).choose n : ℚ))

def plainLegendre (n : ℕ) : Poly :=
  comp (shiftedLegendre n) [1 / 2, -(1 / 2)]

def p2PoleTaylorRationalCorePolynomial (n : ℕ) : Poly :=
  mul
    (comp (poleTaylorPolynomial 1 48)
      (mul (const (7 / 16)) X))
    (plainLegendre n)

def p2PoleTaylorRationalCoreQ (n : ℕ) : ℚ :=
  exactIntegral (p2PoleTaylorRationalCorePolynomial n) (-1) 1

def p2PoleTaylorCoeffScaleCenterQ (n : Fin 48) : ℚ :=
  p2ScaleCenterQ n.val / 2 * p2PoleTaylorRationalCoreQ n.val

def p2EntryTaylorPoleCenterQ (e : P2EntryIndex) : ℚ :=
  2 * p2PoleTaylorCoeffScaleCenterQ
      (p2EntryPoleMode e.block e.col) *
    p2PoleTaylorCoeffScaleCenterQ
      (p2EntryPoleMode e.block e.row)

theorem realize_poleTaylorPolynomial (s : ℚ) (m : ℕ) :
    realize (poleTaylorPolynomial s m) =
      RatPoly.poleTaylorPolynomialQ s m := by
  unfold poleTaylorPolynomial RatPoly.poleTaylorPolynomialQ
  rw [realize_sumRange]
  apply Finset.sum_congr rfl
  intro k _hk
  rw [realize_monomial]

theorem realize_shiftedLegendre (n : ℕ) :
    realize (shiftedLegendre n) = RatPoly.shiftedLegendreQ n := by
  unfold shiftedLegendre RatPoly.shiftedLegendreQ
    Polynomial.shiftedLegendre
  rw [realize_sumRange]
  rw [Polynomial.map_sum]
  apply Finset.sum_congr rfl
  intro k _hk
  rw [realize_monomial]
  simp
  calc
    Polynomial.monomial k
        ((-1 : ℚ) ^ k * (n.choose k : ℚ) *
          ((n + k).choose n : ℚ)) =
        C ((-1 : ℚ) ^ k * (n.choose k : ℚ) *
          ((n + k).choose n : ℚ)) * Polynomial.X ^ k :=
      (Polynomial.C_mul_X_pow_eq_monomial
        (a := ((-1 : ℚ) ^ k * (n.choose k : ℚ) *
          ((n + k).choose n : ℚ))) (n := k)).symm
    _ = (-1 : ℚ[X]) ^ k * (n.choose k : ℚ[X]) *
        ((n + k).choose n : ℚ[X]) * Polynomial.X ^ k := by
      simp

theorem realize_plainLegendre (n : ℕ) :
    realize (plainLegendre n) = RatPoly.plainLegendreQ n := by
  unfold plainLegendre RatPoly.plainLegendreQ
  rw [realize_comp, realize_shiftedLegendre]
  simp [realize]
  congr 1
  ring

theorem realize_p2PoleTaylorRationalCorePolynomial (n : ℕ) :
    realize (p2PoleTaylorRationalCorePolynomial n) =
      RatPoly.p2PoleTaylorRationalCorePolynomialQ n := by
  unfold p2PoleTaylorRationalCorePolynomial
    RatPoly.p2PoleTaylorRationalCorePolynomialQ
  rw [realize_mul, realize_comp, realize_poleTaylorPolynomial,
    realize_mul, realize_const, realize_X, realize_plainLegendre]

theorem p2PoleTaylorRationalCoreQ_eq (n : ℕ) :
    p2PoleTaylorRationalCoreQ n =
      RatPoly.p2PoleTaylorRationalCoreQ n := by
  unfold p2PoleTaylorRationalCoreQ
    RatPoly.p2PoleTaylorRationalCoreQ exactIntegral
  rw [← RatPoly.exactIntegral_ofCoeffs]
  apply congrArg (fun p : RatPoly.QPoly =>
    RatPoly.exactIntegral p (-1) 1)
  exact (realize_eq_ofCoeffs
    (p2PoleTaylorRationalCorePolynomial n)).symm.trans
      (realize_p2PoleTaylorRationalCorePolynomial n)

theorem p2PoleTaylorCoeffScaleCenterQ_eq (n : Fin 48) :
    p2PoleTaylorCoeffScaleCenterQ n =
      RatPoly.p2PoleTaylorCoeffScaleCenterQ n := by
  unfold p2PoleTaylorCoeffScaleCenterQ
    RatPoly.p2PoleTaylorCoeffScaleCenterQ
  rw [p2PoleTaylorRationalCoreQ_eq]

theorem p2EntryTaylorPoleCenterQ_eq (e : P2EntryIndex) :
    p2EntryTaylorPoleCenterQ e =
      RatPoly.p2EntryTaylorPoleCenterQ e := by
  unfold p2EntryTaylorPoleCenterQ RatPoly.p2EntryTaylorPoleCenterQ
  rw [p2PoleTaylorCoeffScaleCenterQ_eq,
    p2PoleTaylorCoeffScaleCenterQ_eq]

theorem p2EntryTaylorPoleCenter_eq_cast_dense (e : P2EntryIndex) :
    RHP2Bridge.p2EntryTaylorPoleCenter e =
      (p2EntryTaylorPoleCenterQ e : ℝ) := by
  rw [p2EntryTaylorPoleCenterQ_eq]
  exact RatPoly.p2EntryTaylorPoleCenter_eq_cast e

/-! ## Complete executable entry center -/

def p2AlphaCenterQ : ℚ := 10938711277167 / 10 ^ 13

def p2InvTwoPiCenterQ : ℚ :=
  15915494309189533576 / 10 ^ 20

def p2EntryDiagonalIndicatorQ (e : P2EntryIndex) : ℚ :=
  if e.row = e.col then 1 else 0

def p2EntryPoleSignQ (block : P2EntryBlock) : ℚ :=
  match block with
  | .even => 1
  | .odd => -1

def p2StoredCenterQ (e : P2EntryIndex) : ℚ :=
  (p2StoredCenterNumerator e : ℚ) / 10 ^ 18 +
    if e.row = e.col then 227 / 10 ^ 7 else 0

def p2EntryApproxCenterQ (e : P2EntryIndex) : ℚ :=
  p2AlphaCenterQ * p2EntryDiagonalIndicatorQ e +
    p2InvTwoPiCenterQ * (2 * p2EntryPanelSumQ e) +
    p2EntryPoleSignQ e.block * p2EntryTaylorPoleCenterQ e

def p2EntryCenterFits (e : P2EntryIndex) : Prop :=
  |p2EntryApproxCenterQ e - p2StoredCenterQ e| ≤ 1 / 10 ^ 13

@[simp] theorem p2AlphaCenterQ_cast :
    (p2AlphaCenterQ : ℝ) = RHP2Bridge.p2AlphaCenter := by
  norm_num [p2AlphaCenterQ, RHP2Bridge.p2AlphaCenter]

@[simp] theorem p2InvTwoPiCenterQ_cast :
    (p2InvTwoPiCenterQ : ℝ) = RHP2Bridge.p2InvTwoPiCenter := by
  norm_num [p2InvTwoPiCenterQ, RHP2Bridge.p2InvTwoPiCenter]

@[simp] theorem p2EntryDiagonalIndicatorQ_cast (e : P2EntryIndex) :
    (p2EntryDiagonalIndicatorQ e : ℝ) =
      RHP2Bridge.p2EntryDiagonalIndicator e := by
  unfold p2EntryDiagonalIndicatorQ
    RHP2Bridge.p2EntryDiagonalIndicator
  split <;> simp

@[simp] theorem p2EntryPoleSignQ_cast (block : P2EntryBlock) :
    (p2EntryPoleSignQ block : ℝ) =
      RHP2Bridge.p2EntryPoleSign block := by
  cases block <;>
    simp [p2EntryPoleSignQ, RHP2Bridge.p2EntryPoleSign]

theorem p2StoredCenter_eq_cast_dense (e : P2EntryIndex) :
    RHP2Bridge.p2StoredCenter e = (p2StoredCenterQ e : ℝ) := by
  rw [RHP2Bridge.p2StoredCenter_eq_integer_table]
  unfold p2StoredCenterQ
  push_cast
  split <;> simp_all <;> norm_num

theorem p2EntryApproxCenter_eq_cast_dense (e : P2EntryIndex) :
    RHP2Bridge.p2AlphaCenter *
          RHP2Bridge.p2EntryDiagonalIndicator e +
        RHP2Bridge.p2InvTwoPiCenter *
          (2 * RHP2Bridge.p2EntryPanelSum e) +
        RHP2Bridge.p2EntryPoleSign e.block *
          RHP2Bridge.p2EntryTaylorPoleCenter e =
      (p2EntryApproxCenterQ e : ℝ) := by
  unfold p2EntryApproxCenterQ
  push_cast
  rw [p2EntryPanelSum_eq_cast_dense,
    p2EntryTaylorPoleCenter_eq_cast_dense]
  simp

end DenseRatPoly

end RHP2Bridge
