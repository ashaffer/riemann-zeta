/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2CanonicalRational
import RHBridge.P2DenseRationalPolynomial
import RHBridge.P2PanelEntry

/-!
# Executable canonical `p = 2` panel polynomials

These definitions duplicate the exact rational formulas from
`P2CanonicalRational` in the executable dense backend.  The realization
theorems are generic proofs, not generated coefficient identities.  Hence a
native evaluator can compute panel integrals while the kernel checks once
that those computations denote the analytic real polynomials.
-/

namespace RHP2Bridge

namespace DenseRatPoly

open Polynomial
open scoped BigOperators

/-! ## Defect polynomial -/

def prefixDenominatorPerturbation
    (n : ℕ) (c : ℚ) : Poly :=
  add
    (mul (const (c / (2 * RatPoly.prefixDenominatorBaseQ n c))) X)
    (mul (const (1 / (4 * RatPoly.prefixDenominatorBaseQ n c)))
      (pow X 2))

def quarterPrefixTermPolynomial
    (n : ℕ) (c : ℚ) (M : ℕ) : Poly :=
  sub
    (const (RatPoly.prefixAQ n / (RatPoly.prefixAQ n ^ 2 + 625)))
    (mul (const (RatPoly.prefixAQ n))
      (mul (const (RatPoly.prefixDenominatorBaseQ n c)⁻¹)
        (geometricReciprocal
          (prefixDenominatorPerturbation n c) M)))

def quarterDifferenceFinitePrefixPolynomial
    (c : ℚ) (M : ℕ) : Poly :=
  sumRange 64 (fun n => quarterPrefixTermPolynomial n c M)

def p2RationalQuarterTailPoly : Poly :=
  sumRange 16 fun k =>
    sub
      (const ((-1 : ℚ) ^ k * 625 ^ k *
        RatPoly.p2ShiftedPowerTailCenterQ (2 * k + 1)))
      (mul
        (const ((-1 : ℚ) ^ k *
          RatPoly.p2ShiftedPowerTailCenterQ (2 * k + 1) /
            2 ^ (2 * k)))
        (pow X (2 * k)))

def cosTaylorPolynomial (N : ℕ) (L : ℚ) : Poly :=
  sumRange N fun m =>
    mul
      (const (RatPoly.iPowReQ m * L ^ m / (m.factorial : ℚ)))
      (pow X m)

def p2RationalNonPrefixPoly : Poly :=
  add p2RationalQuarterTailPoly
    (mul (const RatPoly.p2PrimeAmplitudeCenterQ)
      (sub one
        (cosTaylorPolynomial 128 RatPoly.p2LogTwoCenterQ)))

def p2DefectPanelPolynomial (c : ℚ) (M : ℕ) : Poly :=
  add (quarterDifferenceFinitePrefixPolynomial c M)
    (shift p2RationalNonPrefixPoly c)

theorem realize_prefixDenominatorPerturbation
    (n : ℕ) (c : ℚ) :
    realize (prefixDenominatorPerturbation n c) =
      RatPoly.prefixDenominatorPerturbationQ n c := by
  unfold prefixDenominatorPerturbation
    RatPoly.prefixDenominatorPerturbationQ
  rw [realize_add, realize_mul, realize_const, realize_X,
    realize_mul, realize_const, realize_pow, realize_X]

theorem realize_quarterPrefixTermPolynomial
    (n : ℕ) (c : ℚ) (M : ℕ) :
    realize (quarterPrefixTermPolynomial n c M) =
      RatPoly.quarterPrefixTermPolynomialQ n c M := by
  unfold quarterPrefixTermPolynomial RatPoly.quarterPrefixTermPolynomialQ
  rw [realize_sub, realize_const, realize_mul, realize_const,
    realize_mul, realize_const, realize_geometricReciprocal,
    realize_prefixDenominatorPerturbation]
  rfl

theorem realize_quarterDifferenceFinitePrefixPolynomial
    (c : ℚ) (M : ℕ) :
    realize (quarterDifferenceFinitePrefixPolynomial c M) =
      RatPoly.quarterDifferenceFinitePrefixPolynomialQ c M := by
  unfold quarterDifferenceFinitePrefixPolynomial
    RatPoly.quarterDifferenceFinitePrefixPolynomialQ
  rw [realize_sumRange]
  apply Finset.sum_congr rfl
  intro n _hn
  exact realize_quarterPrefixTermPolynomial n c M

theorem realize_p2RationalQuarterTailPoly :
    realize p2RationalQuarterTailPoly =
      RatPoly.p2RationalQuarterTailPolyQ := by
  unfold p2RationalQuarterTailPoly RatPoly.p2RationalQuarterTailPolyQ
  rw [realize_sumRange]
  apply Finset.sum_congr rfl
  intro k _hk
  rw [realize_sub, realize_const, realize_mul, realize_const,
    realize_pow, realize_X]

theorem realize_cosTaylorPolynomial (N : ℕ) (L : ℚ) :
    realize (cosTaylorPolynomial N L) =
      RatPoly.cosTaylorPolynomialQ N L := by
  unfold cosTaylorPolynomial RatPoly.cosTaylorPolynomialQ
  rw [realize_sumRange]
  apply Finset.sum_congr rfl
  intro m _hm
  rw [realize_mul, realize_const, realize_pow, realize_X]

theorem realize_p2RationalNonPrefixPoly :
    realize p2RationalNonPrefixPoly =
      RatPoly.p2RationalNonPrefixPolyQ := by
  unfold p2RationalNonPrefixPoly RatPoly.p2RationalNonPrefixPolyQ
  rw [realize_add, realize_p2RationalQuarterTailPoly, realize_mul,
    realize_const, realize_sub, realize_one,
    realize_cosTaylorPolynomial]

theorem realize_p2DefectPanelPolynomial (c : ℚ) (M : ℕ) :
    realize (p2DefectPanelPolynomial c M) =
      RatPoly.p2DefectPanelPolynomialQ c M := by
  unfold p2DefectPanelPolynomial RatPoly.p2DefectPanelPolynomialQ
  rw [realize_add, realize_quarterDifferenceFinitePrefixPolynomial,
    realize_shift, realize_p2RationalNonPrefixPoly]

/-! ## Spherical and selected-component polynomials -/

def sphericalJRealPolynomial (n N : ℕ) : Poly :=
  mul
    (mul
      (const (1 / (2 ^ (n + 1) * (n.factorial : ℚ))))
      (pow X n))
    (sumRange N fun m =>
      mul
        (const (RatPoly.iPowReQ m * RatPoly.weightMomentQ n m /
          (m.factorial : ℚ)))
        (pow X m))

def p2SphericalRealPolynomial (n N : ℕ) : Poly :=
  comp (sphericalJRealPolynomial n N)
    (mul (const (7 / 16)) X)

def p2Spherical100PanelPolynomial (n : ℕ) (c : ℚ) : Poly :=
  shift (p2SphericalRealPolynomial n 100) c

def p2SelectedComponent100ScaleCenterPolynomial
    (kind : P2SelectedKind) (k : Fin 24) (c : ℚ) : Poly :=
  mul (const (RatPoly.p2SelectedPhaseQ kind k.val))
    (mul (const (p2SelectedScaleCenterQ kind k))
      (p2Spherical100PanelPolynomial
        (p2SelectedDegree kind k.val) c))

def p2ScaleCenteredPanelIntegrandPolynomial
    (kind : P2SelectedKind) (i j : Fin 24)
    (c : ℚ) (M : ℕ) : Poly :=
  mul (p2DefectPanelPolynomial c M)
    (mul
      (p2SelectedComponent100ScaleCenterPolynomial kind j c)
      (p2SelectedComponent100ScaleCenterPolynomial kind i c))

theorem realize_sphericalJRealPolynomial (n N : ℕ) :
    realize (sphericalJRealPolynomial n N) =
      RatPoly.sphericalJRealPolynomialQ n N := by
  unfold sphericalJRealPolynomial RatPoly.sphericalJRealPolynomialQ
  rw [realize_mul, realize_mul, realize_const, realize_pow, realize_X,
    realize_sumRange]
  apply congrArg (fun p : ℚ[X] =>
    C (1 / (2 ^ (n + 1) * (n.factorial : ℚ))) *
      Polynomial.X ^ n * p)
  apply Finset.sum_congr rfl
  intro m _hm
  rw [realize_mul, realize_const, realize_pow, realize_X]

theorem realize_p2SphericalRealPolynomial (n N : ℕ) :
    realize (p2SphericalRealPolynomial n N) =
      RatPoly.p2SphericalRealPolynomialQ n N := by
  unfold p2SphericalRealPolynomial
    RatPoly.p2SphericalRealPolynomialQ
  rw [realize_comp, realize_sphericalJRealPolynomial, realize_mul,
    realize_const, realize_X]

theorem realize_p2Spherical100PanelPolynomial (n : ℕ) (c : ℚ) :
    realize (p2Spherical100PanelPolynomial n c) =
      RatPoly.p2Spherical100PanelPolynomialQ n c := by
  unfold p2Spherical100PanelPolynomial
    RatPoly.p2Spherical100PanelPolynomialQ
  rw [realize_shift, realize_p2SphericalRealPolynomial]

theorem realize_p2SelectedComponent100ScaleCenterPolynomial
    (kind : P2SelectedKind) (k : Fin 24) (c : ℚ) :
    realize (p2SelectedComponent100ScaleCenterPolynomial kind k c) =
      RatPoly.p2SelectedComponent100ScaleCenterPolynomialQ kind k c := by
  unfold p2SelectedComponent100ScaleCenterPolynomial
    RatPoly.p2SelectedComponent100ScaleCenterPolynomialQ
  rw [realize_mul, realize_const, realize_mul, realize_const,
    realize_p2Spherical100PanelPolynomial]

theorem realize_p2ScaleCenteredPanelIntegrandPolynomial
    (kind : P2SelectedKind) (i j : Fin 24)
    (c : ℚ) (M : ℕ) :
    realize (p2ScaleCenteredPanelIntegrandPolynomial kind i j c M) =
      RatPoly.p2ScaleCenteredPanelIntegrandPolynomialQ kind i j c M := by
  unfold p2ScaleCenteredPanelIntegrandPolynomial
    RatPoly.p2ScaleCenteredPanelIntegrandPolynomialQ
  rw [realize_mul, realize_p2DefectPanelPolynomial, realize_mul,
    realize_p2SelectedComponent100ScaleCenterPolynomial,
    realize_p2SelectedComponent100ScaleCenterPolynomial]

/-! ## Executable exact panel and entry sums -/

def p2ScaleCenteredPanelIntegralQ
    (kind : P2SelectedKind) (i j : Fin 24)
    (c h : ℚ) (M : ℕ) : ℚ :=
  exactIntegral
    (p2ScaleCenteredPanelIntegrandPolynomial kind i j c M) (-h) h

def p2PanelIntegralQ
    (kind : P2SelectedKind) (i j : Fin 24) (k : ℕ) : ℚ :=
  p2ScaleCenteredPanelIntegralQ kind i j
    (p2PanelCenterQ k) (p2PanelHalfWidthQ k) 32

def p2EntryPanelSumQ (e : P2EntryIndex) : ℚ :=
  ∑ k ∈ Finset.range 32,
    p2PanelIntegralQ (p2EntrySelectedKind e.block) e.row e.col k

theorem p2ScaleCenteredPanel_exactIntegral_eq_cast_dense
    (kind : P2SelectedKind) (i j : Fin 24)
    (c h : ℚ) (M : ℕ) :
    PolyEnclosure.exactIntegral
        (RHP2Bridge.p2ScaleCenteredPanelIntegrandPolynomial
          kind i j (c : ℝ) M)
        (-h : ℝ) (h : ℝ) =
      (p2ScaleCenteredPanelIntegralQ kind i j c h M : ℝ) := by
  unfold p2ScaleCenteredPanelIntegralQ
  rw [← RatPoly.toReal_p2ScaleCenteredPanelIntegrandPolynomialQ]
  rw [← realize_p2ScaleCenteredPanelIntegrandPolynomial]
  simpa using (cast_exactIntegral
    (p2ScaleCenteredPanelIntegrandPolynomial kind i j c M)
    (-h) h).symm

theorem p2EntryPanelSum_eq_cast_dense (e : P2EntryIndex) :
    RHP2Bridge.p2EntryPanelSum e = (p2EntryPanelSumQ e : ℝ) := by
  unfold RHP2Bridge.p2EntryPanelSum p2EntryPanelSumQ p2PanelIntegralQ
  push_cast
  apply Finset.sum_congr rfl
  intro k _hk
  simpa [p2PanelCenter, p2PanelHalfWidth] using
    p2ScaleCenteredPanel_exactIntegral_eq_cast_dense
      (p2EntrySelectedKind e.block) e.row e.col
      (p2PanelCenterQ k) (p2PanelHalfWidthQ k) 32

end DenseRatPoly

end RHP2Bridge
