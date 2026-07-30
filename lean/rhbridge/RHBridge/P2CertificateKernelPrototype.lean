/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2CanonicalRational
import RHBridge.P2PanelPartition
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-!
# Kernel arithmetic prototype for the canonical `p = 2` certificate

This temporary module measures viable exact-rational certificate encodings.
It intentionally contains only tiny representative checks until the selected
encoding has been shown to scale.
-/

namespace RHP2Bridge

namespace P2CertificateKernelPrototype

open Polynomial
open scoped BigOperators

/-- A tiny exact integral check through the rational-polynomial backend. -/
example :
    RatPoly.exactIntegral (X ^ 2 + C (3 / 5 : ℚ)) (-1) 1 = 28 / 15 := by
  norm_num [RatPoly.exactIntegral, Finset.sum_range_succ]

/-! ## Executable dense polynomials

`Polynomial ℚ` uses a noncomputable finitely-supported-map multiplication.
Generated certificates therefore cannot evaluate the canonical expression
with `native_decide` directly.  Ascending dense coefficient lists provide an
executable mirror.  The subsequent bridge lemmas ensure that this is only an
implementation choice, not a new trusted mathematical model.
-/

namespace Dense

/-- Ascending coefficients: `[a₀, a₁, ...]` denotes `∑ aᵢ Xⁱ`.
Trailing zeroes are allowed. -/
abbrev Poly := List ℚ

def add : Poly → Poly → Poly
  | [], q => q
  | p, [] => p
  | a :: p, b :: q => (a + b) :: add p q

def neg : Poly → Poly := List.map (-·)

def sub (p q : Poly) : Poly := add p (neg q)

def scale (a : ℚ) : Poly → Poly := List.map (a * ·)

/-- Schoolbook convolution, arranged recursively by the low coefficient. -/
def mul : Poly → Poly → Poly
  | [], _ => []
  | _ :: _, [] => []
  | a :: p, q => add (scale a q) (0 :: mul p q)

def pow (p : Poly) : ℕ → Poly
  | 0 => [1]
  | n + 1 => mul (pow p n) p

/-- Horner composition in ascending order. -/
def comp : Poly → Poly → Poly
  | [], _ => []
  | a :: p, q => add [a] (mul q (comp p q))

def monomial : ℕ → ℚ → Poly
  | 0, a => [a]
  | n + 1, a => 0 :: monomial n a

def sumRange : ℕ → (ℕ → Poly) → Poly
  | 0, _ => []
  | n + 1, f => add (sumRange n f) (f n)

def exactIntegralAux (a b : ℚ) : ℕ → Poly → ℚ
  | _, [] => 0
  | k, c :: p =>
      c * ((b ^ (k + 1) - a ^ (k + 1)) / ((k : ℚ) + 1)) +
        exactIntegralAux a b (k + 1) p

def exactIntegral (p : Poly) (a b : ℚ) : ℚ :=
  exactIntegralAux a b 0 p

/-- Mathematical interpretation used only at the proof boundary. -/
noncomputable def toPolynomial : Poly → Polynomial ℚ
  | [] => 0
  | a :: p => C a + X * toPolynomial p

@[simp] theorem toPolynomial_nil : toPolynomial [] = 0 := rfl

@[simp] theorem toPolynomial_cons (a : ℚ) (p : Poly) :
    toPolynomial (a :: p) = C a + X * toPolynomial p := rfl

@[simp] theorem toPolynomial_add (p q : Poly) :
    toPolynomial (add p q) = toPolynomial p + toPolynomial q := by
  induction p generalizing q with
  | nil => simp [add]
  | cons a p ih =>
      cases q with
      | nil => simp [add]
      | cons b q =>
          simp only [add, toPolynomial_cons, ih]
          simp
          ring

@[simp] theorem toPolynomial_neg (p : Poly) :
    toPolynomial (neg p) = -toPolynomial p := by
  induction p with
  | nil => simp [neg]
  | cons a p ih =>
      change toPolynomial ((-a) :: neg p) = _
      rw [toPolynomial_cons, ih]
      simp
      ring

@[simp] theorem toPolynomial_sub (p q : Poly) :
    toPolynomial (sub p q) = toPolynomial p - toPolynomial q := by
  rw [sub, toPolynomial_add, toPolynomial_neg, sub_eq_add_neg]

@[simp] theorem toPolynomial_scale (a : ℚ) (p : Poly) :
    toPolynomial (scale a p) = C a * toPolynomial p := by
  induction p with
  | nil => simp [scale]
  | cons b p ih =>
      change toPolynomial ((a * b) :: scale a p) = _
      rw [toPolynomial_cons, ih]
      simp
      ring

@[simp] theorem toPolynomial_mul (p q : Poly) :
    toPolynomial (mul p q) = toPolynomial p * toPolynomial q := by
  induction p with
  | nil => simp [mul]
  | cons a p ih =>
      cases q with
      | nil => simp [mul]
      | cons b q =>
          simp only [mul, toPolynomial_add, toPolynomial_scale,
            toPolynomial_cons, ih]
          simp
          ring

@[simp] theorem toPolynomial_pow (p : Poly) (n : ℕ) :
    toPolynomial (pow p n) = toPolynomial p ^ n := by
  induction n with
  | zero => simp [pow]
  | succ n ih => simp [pow, ih, pow_succ]

@[simp] theorem toPolynomial_comp (p q : Poly) :
    toPolynomial (comp p q) = (toPolynomial p).comp (toPolynomial q) := by
  induction p with
  | nil => simp [comp]
  | cons a p ih =>
      simp only [comp, toPolynomial_add, toPolynomial_cons,
        toPolynomial_mul, ih]
      simp

@[simp] theorem toPolynomial_monomial (n : ℕ) (a : ℚ) :
    toPolynomial (monomial n a) = Polynomial.monomial n a := by
  induction n with
  | zero => simp [monomial]
  | succ n ih =>
      simp only [monomial, toPolynomial_cons, ih]
      simp [Polynomial.X_mul_monomial]

@[simp] theorem toPolynomial_sumRange (n : ℕ) (f : ℕ → Poly) :
    toPolynomial (sumRange n f) =
      ∑ k ∈ Finset.range n, toPolynomial (f k) := by
  induction n with
  | zero => simp [sumRange]
  | succ n ih => simp [sumRange, ih, Finset.sum_range_succ]

/-- Real evaluation with an explicit initial exponent. -/
noncomputable def evalAuxReal : ℕ → Poly → ℝ → ℝ
  | _, [], _ => 0
  | k, a :: p, x => (a : ℝ) * x ^ k + evalAuxReal (k + 1) p x

theorem continuous_evalAuxReal (k : ℕ) (p : Poly) :
    Continuous (evalAuxReal k p) := by
  induction p generalizing k with
  | nil => exact continuous_const
  | cons a p ih => exact (continuous_const.mul (continuous_id.pow k)).add (ih (k + 1))

theorem evalAuxReal_eq_pow_mul_eval_toReal
    (k : ℕ) (p : Poly) (x : ℝ) :
    evalAuxReal k p x =
      x ^ k * (RatPoly.toReal (toPolynomial p)).eval x := by
  induction p generalizing k with
  | nil => simp [evalAuxReal]
  | cons a p ih =>
      simp only [evalAuxReal, toPolynomial_cons, RatPoly.toReal_add,
        RatPoly.toReal_C, RatPoly.toReal_mul, RatPoly.toReal_X,
        Polynomial.eval_add, Polynomial.eval_C, Polynomial.eval_mul,
        Polynomial.eval_X, ih]
      rw [pow_succ]
      ring

theorem evalAuxReal_zero_eq_eval_toReal (p : Poly) (x : ℝ) :
    evalAuxReal 0 p x = (RatPoly.toReal (toPolynomial p)).eval x := by
  simpa using evalAuxReal_eq_pow_mul_eval_toReal 0 p x

theorem integral_evalAuxReal (k : ℕ) (p : Poly) (a b : ℚ) :
    (∫ x in (a : ℝ)..(b : ℝ), evalAuxReal k p x) =
      (exactIntegralAux a b k p : ℝ) := by
  induction p generalizing k with
  | nil => simp [evalAuxReal, exactIntegralAux]
  | cons c p ih =>
      rw [show evalAuxReal k (c :: p) =
          (fun x : ℝ => (c : ℝ) * x ^ k) + evalAuxReal (k + 1) p by
        funext x
        simp [evalAuxReal]]
      have hc : IntervalIntegrable (fun x : ℝ => (c : ℝ) * x ^ k)
          MeasureTheory.volume (a : ℝ) (b : ℝ) :=
        (continuous_const.mul (continuous_id.pow k)).intervalIntegrable _ _
      have hp : IntervalIntegrable (evalAuxReal (k + 1) p)
          MeasureTheory.volume (a : ℝ) (b : ℝ) :=
        (continuous_evalAuxReal (k + 1) p).intervalIntegrable _ _
      change (∫ x in (a : ℝ)..(b : ℝ),
        (c : ℝ) * x ^ k + evalAuxReal (k + 1) p x) = _
      rw [intervalIntegral.integral_add hc hp]
      rw [intervalIntegral.integral_const_mul, integral_pow,
        ih]
      simp only [exactIntegralAux]
      push_cast
      rfl

theorem real_exactIntegral_eq (p : Poly) (a b : ℚ) :
    PolyEnclosure.exactIntegral (RatPoly.toReal (toPolynomial p))
        (a : ℝ) (b : ℝ) = (exactIntegral p a b : ℝ) := by
  rw [← PolyEnclosure.integral_eval_eq_exactIntegral]
  calc
    (∫ x in (a : ℝ)..(b : ℝ),
        (RatPoly.toReal (toPolynomial p)).eval x) =
        ∫ x in (a : ℝ)..(b : ℝ), evalAuxReal 0 p x := by
      apply intervalIntegral.integral_congr
      intro x hx
      exact (evalAuxReal_zero_eq_eval_toReal p x).symm
    _ = (exactIntegral p a b : ℝ) := integral_evalAuxReal 0 p a b

end Dense

/-! ## Executable mirror of the canonical band expression -/

namespace CanonicalDense

open Dense

def prefixDenominatorPerturbation
    (n : ℕ) (c : ℚ) : Dense.Poly :=
  [0,
    c / (2 * RatPoly.prefixDenominatorBaseQ n c),
    1 / (4 * RatPoly.prefixDenominatorBaseQ n c)]

/-- Simultaneously accumulate `∑ k < N, (-r)^k` and `(-r)^N`.
This avoids recomputing every power from scratch. -/
def geometricReciprocalState (r : Dense.Poly) :
    ℕ → Dense.Poly × Dense.Poly
  | 0 => ([], [1])
  | N + 1 =>
      let previous := geometricReciprocalState r N
      (Dense.add previous.1 previous.2,
        Dense.mul previous.2 (Dense.neg r))

def geometricReciprocal (r : Dense.Poly) (N : ℕ) : Dense.Poly :=
  (geometricReciprocalState r N).1

def quarterPrefixTermPolynomial
    (n : ℕ) (c : ℚ) (M : ℕ) : Dense.Poly :=
  Dense.sub
    [RatPoly.prefixAQ n / (RatPoly.prefixAQ n ^ 2 + 625)]
    (Dense.scale (RatPoly.prefixAQ n)
      (Dense.scale (RatPoly.prefixDenominatorBaseQ n c)⁻¹
        (geometricReciprocal (prefixDenominatorPerturbation n c) M)))

def quarterDifferenceFinitePrefixPolynomial
    (c : ℚ) (M : ℕ) : Dense.Poly :=
  Dense.sumRange 64 (fun n => quarterPrefixTermPolynomial n c M)

def rationalQuarterTailPolynomial : Dense.Poly :=
  Dense.sumRange 16 (fun k =>
    let tail := RatPoly.p2ShiftedPowerTailCenterQ (2 * k + 1)
    Dense.sub
      [(-1 : ℚ) ^ k * 625 ^ k * tail]
      (Dense.monomial (2 * k)
        (((-1 : ℚ) ^ k * tail) / 2 ^ (2 * k))))

def cosTaylorPolynomial (N : ℕ) (L : ℚ) : Dense.Poly :=
  Dense.sumRange N (fun m =>
    Dense.monomial m
      (RatPoly.iPowReQ m * L ^ m / (m.factorial : ℚ)))

def rationalNonPrefixPolynomial : Dense.Poly :=
  Dense.add rationalQuarterTailPolynomial
    (Dense.scale RatPoly.p2PrimeAmplitudeCenterQ
      (Dense.sub [1]
        (cosTaylorPolynomial 128 RatPoly.p2LogTwoCenterQ)))

def defectPanelPolynomial (c : ℚ) (M : ℕ) : Dense.Poly :=
  Dense.add (quarterDifferenceFinitePrefixPolynomial c M)
    (Dense.comp rationalNonPrefixPolynomial [c, 1])

def sphericalJRealPolynomial (n N : ℕ) : Dense.Poly :=
  Dense.scale (1 / (2 ^ (n + 1) * (n.factorial : ℚ)))
    (Dense.mul (Dense.monomial n 1)
      (Dense.sumRange N (fun m =>
        Dense.monomial m
          (RatPoly.iPowReQ m * RatPoly.weightMomentQ n m /
            (m.factorial : ℚ)))))

def p2SphericalRealPolynomial (n N : ℕ) : Dense.Poly :=
  Dense.comp (sphericalJRealPolynomial n N) [0, 7 / 16]

def p2Spherical100PanelPolynomial (n : ℕ) (c : ℚ) : Dense.Poly :=
  Dense.comp (p2SphericalRealPolynomial n 100) [c, 1]

def selectedComponent100ScaleCenterPolynomial
    (kind : P2SelectedKind) (k : Fin 24) (c : ℚ) : Dense.Poly :=
  Dense.scale
    (RatPoly.p2SelectedPhaseQ kind k.val *
      p2SelectedScaleCenterQ kind k)
    (p2Spherical100PanelPolynomial
      (p2SelectedDegree kind k.val) c)

def panelIntegrandPolynomial
    (kind : P2SelectedKind) (i j : Fin 24) (c : ℚ) (M : ℕ) :
    Dense.Poly :=
  Dense.mul (defectPanelPolynomial c M)
    (Dense.mul
      (selectedComponent100ScaleCenterPolynomial kind j c)
      (selectedComponent100ScaleCenterPolynomial kind i c))

theorem toPolynomial_prefixDenominatorPerturbation
    (n : ℕ) (c : ℚ) :
    Dense.toPolynomial (prefixDenominatorPerturbation n c) =
      RatPoly.prefixDenominatorPerturbationQ n c := by
  simp [prefixDenominatorPerturbation,
    RatPoly.prefixDenominatorPerturbationQ]
  ring

theorem toPolynomial_geometricReciprocal
    (r : Dense.Poly) (N : ℕ) :
    Dense.toPolynomial (geometricReciprocal r N) =
      RatPoly.geometricReciprocalQ (Dense.toPolynomial r) N := by
  have hstate :
      Dense.toPolynomial (geometricReciprocalState r N).1 =
          ∑ k ∈ Finset.range N, (-Dense.toPolynomial r) ^ k ∧
        Dense.toPolynomial (geometricReciprocalState r N).2 =
          (-Dense.toPolynomial r) ^ N := by
    induction N with
    | zero => simp [geometricReciprocalState]
    | succ N ih =>
        simp only [geometricReciprocalState, Dense.toPolynomial_add,
          Dense.toPolynomial_mul, Dense.toPolynomial_neg, ih.1, ih.2]
        constructor
        · rw [Finset.sum_range_succ]
        · rw [pow_succ]
  simpa [geometricReciprocal, RatPoly.geometricReciprocalQ] using hstate.1

theorem toPolynomial_quarterPrefixTermPolynomial
    (n : ℕ) (c : ℚ) (M : ℕ) :
    Dense.toPolynomial (quarterPrefixTermPolynomial n c M) =
      RatPoly.quarterPrefixTermPolynomialQ n c M := by
  simp [quarterPrefixTermPolynomial,
    RatPoly.quarterPrefixTermPolynomialQ,
    toPolynomial_geometricReciprocal,
    toPolynomial_prefixDenominatorPerturbation]

theorem toPolynomial_quarterDifferenceFinitePrefixPolynomial
    (c : ℚ) (M : ℕ) :
    Dense.toPolynomial (quarterDifferenceFinitePrefixPolynomial c M) =
      RatPoly.quarterDifferenceFinitePrefixPolynomialQ c M := by
  simp [quarterDifferenceFinitePrefixPolynomial,
    RatPoly.quarterDifferenceFinitePrefixPolynomialQ,
    toPolynomial_quarterPrefixTermPolynomial]

theorem toPolynomial_rationalQuarterTailPolynomial :
    Dense.toPolynomial rationalQuarterTailPolynomial =
      RatPoly.p2RationalQuarterTailPolyQ := by
  simp only [rationalQuarterTailPolynomial,
    RatPoly.p2RationalQuarterTailPolyQ, Dense.toPolynomial_sumRange,
    Dense.toPolynomial_sub, Dense.toPolynomial_cons,
    Dense.toPolynomial_nil, Dense.toPolynomial_monomial,
    mul_zero, add_zero]
  simp_rw [← Polynomial.C_mul_X_pow_eq_monomial]

theorem toPolynomial_cosTaylorPolynomial (N : ℕ) (L : ℚ) :
    Dense.toPolynomial (cosTaylorPolynomial N L) =
      RatPoly.cosTaylorPolynomialQ N L := by
  simp only [cosTaylorPolynomial, RatPoly.cosTaylorPolynomialQ,
    Dense.toPolynomial_sumRange, Dense.toPolynomial_monomial]
  simp_rw [← Polynomial.C_mul_X_pow_eq_monomial]

set_option maxRecDepth 4096 in
theorem toPolynomial_rationalNonPrefixPolynomial :
    Dense.toPolynomial rationalNonPrefixPolynomial =
      RatPoly.p2RationalNonPrefixPolyQ := by
  unfold rationalNonPrefixPolynomial RatPoly.p2RationalNonPrefixPolyQ
  rw [Dense.toPolynomial_add,
    toPolynomial_rationalQuarterTailPolynomial,
    Dense.toPolynomial_scale, Dense.toPolynomial_sub,
    toPolynomial_cosTaylorPolynomial]
  simp

theorem toPolynomial_defectPanelPolynomial (c : ℚ) (M : ℕ) :
    Dense.toPolynomial (defectPanelPolynomial c M) =
      RatPoly.p2DefectPanelPolynomialQ c M := by
  simp [defectPanelPolynomial, RatPoly.p2DefectPanelPolynomialQ,
    RatPoly.shift, toPolynomial_quarterDifferenceFinitePrefixPolynomial,
    toPolynomial_rationalNonPrefixPolynomial]

theorem toPolynomial_sphericalJRealPolynomial (n N : ℕ) :
    Dense.toPolynomial (sphericalJRealPolynomial n N) =
      RatPoly.sphericalJRealPolynomialQ n N := by
  simp only [sphericalJRealPolynomial,
    RatPoly.sphericalJRealPolynomialQ, Dense.toPolynomial_scale,
    Dense.toPolynomial_mul, Dense.toPolynomial_monomial,
    Dense.toPolynomial_sumRange]
  simp_rw [← Polynomial.C_mul_X_pow_eq_monomial]
  simp
  ring

theorem toPolynomial_p2SphericalRealPolynomial (n N : ℕ) :
    Dense.toPolynomial (p2SphericalRealPolynomial n N) =
      RatPoly.p2SphericalRealPolynomialQ n N := by
  simp [p2SphericalRealPolynomial, RatPoly.p2SphericalRealPolynomialQ,
    toPolynomial_sphericalJRealPolynomial]

theorem toPolynomial_p2Spherical100PanelPolynomial (n : ℕ) (c : ℚ) :
    Dense.toPolynomial (p2Spherical100PanelPolynomial n c) =
      RatPoly.p2Spherical100PanelPolynomialQ n c := by
  simp [p2Spherical100PanelPolynomial,
    RatPoly.p2Spherical100PanelPolynomialQ, RatPoly.shift,
    toPolynomial_p2SphericalRealPolynomial]

theorem toPolynomial_selectedComponent100ScaleCenterPolynomial
    (kind : P2SelectedKind) (k : Fin 24) (c : ℚ) :
    Dense.toPolynomial
        (selectedComponent100ScaleCenterPolynomial kind k c) =
      RatPoly.p2SelectedComponent100ScaleCenterPolynomialQ kind k c := by
  simp [selectedComponent100ScaleCenterPolynomial,
    RatPoly.p2SelectedComponent100ScaleCenterPolynomialQ,
    toPolynomial_p2Spherical100PanelPolynomial]
  ring

theorem toPolynomial_panelIntegrandPolynomial
    (kind : P2SelectedKind) (i j : Fin 24) (c : ℚ) (M : ℕ) :
    Dense.toPolynomial (panelIntegrandPolynomial kind i j c M) =
      RatPoly.p2ScaleCenteredPanelIntegrandPolynomialQ kind i j c M := by
  simp [panelIntegrandPolynomial,
    RatPoly.p2ScaleCenteredPanelIntegrandPolynomialQ,
    toPolynomial_defectPanelPolynomial,
    toPolynomial_selectedComponent100ScaleCenterPolynomial]

set_option maxHeartbeats 800000
set_option maxRecDepth 4096
/-- Semantic bridge for the executable exact integral of one canonical
panel. -/
theorem real_exactPanelIntegral_eq_dense
    (kind : P2SelectedKind) (i j : Fin 24) (c h : ℚ) (M : ℕ) :
    PolyEnclosure.exactIntegral
        (p2ScaleCenteredPanelIntegrandPolynomial kind i j (c : ℝ) M)
        (-h : ℝ) (h : ℝ) =
      (Dense.exactIntegral (panelIntegrandPolynomial kind i j c M)
        (-h) h : ℝ) := by
  rw [← RatPoly.toReal_p2ScaleCenteredPanelIntegrandPolynomialQ]
  rw [← toPolynomial_panelIntegrandPolynomial]
  simpa only [Rat.cast_neg] using
    Dense.real_exactIntegral_eq
      (panelIntegrandPolynomial kind i j c M) (-h) h

end CanonicalDense

example : Dense.add [1, 2] [3, 4, 5] = [4, 6, 5] := by native_decide

example : Dense.mul [1, 2] [3, 4] = [3, 10, 8] := by native_decide

example : Dense.exactIntegral (Dense.mul [1, 2] [3, 4]) (-1) 1 = 34 / 3 := by
  native_decide

/-! The first generated panel value is checked by recomputing the complete
canonical rational expression inside Lean's native evaluator.  Python merely
supplies the proposed rounded integer. -/

set_option maxRecDepth 4096
set_option maxHeartbeats 20000000

def firstGeneratedPanelNumerator : ℤ :=
  -15614294737720158450729501401719657941893

def generatedPanelScale : ℕ := 10 ^ 40

def generatedPanelRoundingRadius : ℚ := 1 / (2 * generatedPanelScale)

example :
    (CanonicalDense.panelIntegrandPolynomial .even
      (0 : Fin 24) (0 : Fin 24) (p2PanelCenterQ 0) 32).length > 0 := by
  native_decide

example :
    |Dense.exactIntegral
          (CanonicalDense.panelIntegrandPolynomial
            .even (0 : Fin 24) (0 : Fin 24) (p2PanelCenterQ 0) 32)
          (-p2PanelHalfWidthQ 0) (p2PanelHalfWidthQ 0) -
        (firstGeneratedPanelNumerator : ℚ) / generatedPanelScale| ≤
      generatedPanelRoundingRadius := by
  native_decide

end P2CertificateKernelPrototype

end RHP2Bridge
