/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2CanonicalDense
import RHBridge.P2RoundedPolynomial

/-!
# Fixed-grid expression for the canonical `p = 2` panel polynomials

`DenseRatPoly` is an executable exact model, but evaluating a complete panel
with it creates rational denominators that grow at every convolution.  This
module first records the very same calculation as a small expression tree.
Its exact denotation is proved equal to the canonical dense polynomial.  A
separate evaluator below can therefore round after every node without making
generated floating-point data part of the trusted proof.

Panels are ultimately composed with `t ↦ h*t`, so all stored polynomial
enclosures live on the fixed domain `|t| ≤ 1`.
-/

namespace RHP2Bridge

namespace P2RoundedCanonical

open DenseRatPoly
open RoundedRatPoly

/-! ## A sharing-friendly polynomial expression -/

/-- Operations occurring in the canonical dense formulas.  Powers and finite
geometric sums are primitive nodes so that a rounded evaluator can compute
them iteratively rather than expanding a quadratic-size syntax tree. -/
inductive Expr where
  | atom (p : DenseRatPoly.Poly)
  | add (p q : Expr)
  | scale (c : ℚ) (p : Expr)
  | mul (p q : Expr)
  | comp (p q : Expr)
  | pow (p : Expr) (n : ℕ)
  | geometricReciprocal (p : Expr) (n : ℕ)
  deriving Repr

/-- Exact executable denotation.  This definition is used only by semantic
proofs; the rounded evaluator never constructs the resulting exact dense
polynomial. -/
def Expr.denote : Expr → DenseRatPoly.Poly
  | .atom p => p
  | .add p q => DenseRatPoly.add p.denote q.denote
  | .scale c p => DenseRatPoly.scale c p.denote
  | .mul p q => DenseRatPoly.mul p.denote q.denote
  | .comp p q => DenseRatPoly.comp p.denote q.denote
  | .pow p n => DenseRatPoly.pow p.denote n
  | .geometricReciprocal p n =>
      DenseRatPoly.geometricReciprocal p.denote n

namespace Expr

def zero : Expr := .atom DenseRatPoly.zero
def one : Expr := .atom DenseRatPoly.one
def const (q : ℚ) : Expr := .atom (DenseRatPoly.const q)
def X : Expr := .atom DenseRatPoly.X
def neg (p : Expr) : Expr := .scale (-1) p
def sub (p q : Expr) : Expr := .add p (.neg q)

def sumRange : (N : ℕ) → (ℕ → Expr) → Expr
  | 0, _ => zero
  | N + 1, f => .add (sumRange N f) (f N)

def affine (p : Expr) (c s : ℚ) : Expr :=
  .comp p (.atom [c, s])

def shift (p : Expr) (c : ℚ) : Expr := affine p c 1

@[simp] theorem denote_atom (p : DenseRatPoly.Poly) :
    (atom p).denote = p := rfl

@[simp] theorem denote_add (p q : Expr) :
    (add p q).denote = DenseRatPoly.add p.denote q.denote := rfl

@[simp] theorem denote_scale (c : ℚ) (p : Expr) :
    (scale c p).denote = DenseRatPoly.scale c p.denote := rfl

@[simp] theorem denote_mul (p q : Expr) :
    (mul p q).denote = DenseRatPoly.mul p.denote q.denote := rfl

@[simp] theorem denote_comp (p q : Expr) :
    (comp p q).denote = DenseRatPoly.comp p.denote q.denote := rfl

@[simp] theorem denote_pow (p : Expr) (n : ℕ) :
    (pow p n).denote = DenseRatPoly.pow p.denote n := rfl

@[simp] theorem denote_geometricReciprocal (p : Expr) (n : ℕ) :
    (geometricReciprocal p n).denote =
      DenseRatPoly.geometricReciprocal p.denote n := rfl

@[simp] theorem denote_zero : zero.denote = DenseRatPoly.zero := rfl
@[simp] theorem denote_one : one.denote = DenseRatPoly.one := rfl
@[simp] theorem denote_const (q : ℚ) :
    (const q).denote = DenseRatPoly.const q := rfl
@[simp] theorem denote_X : X.denote = DenseRatPoly.X := rfl

@[simp] theorem denote_neg (p : Expr) :
    (neg p).denote = DenseRatPoly.neg p.denote := by
  simp [neg, DenseRatPoly.neg, DenseRatPoly.scale]

@[simp] theorem denote_sub (p q : Expr) :
    (sub p q).denote = DenseRatPoly.sub p.denote q.denote := by
  simp [sub, DenseRatPoly.sub]

@[simp] theorem denote_sumRange (N : ℕ) (f : ℕ → Expr) :
    (sumRange N f).denote =
      DenseRatPoly.sumRange N (fun k => (f k).denote) := by
  induction N with
  | zero => rfl
  | succ N ih => simp [sumRange, DenseRatPoly.sumRange, ih]

@[simp] theorem denote_affine (p : Expr) (c s : ℚ) :
    (affine p c s).denote = DenseRatPoly.affine p.denote c s := by
  rfl

@[simp] theorem denote_shift (p : Expr) (c : ℚ) :
    (shift p c).denote = DenseRatPoly.shift p.denote c := by
  rfl

end Expr

/-! ## Canonical formula in the expression language -/

open Expr

def prefixDenominatorPerturbationExpr (n : ℕ) (c : ℚ) : Expr :=
  .add
    (.mul
      (.const (c / (2 * RatPoly.prefixDenominatorBaseQ n c))) .X)
    (.mul
      (.const (1 / (4 * RatPoly.prefixDenominatorBaseQ n c)))
      (.pow .X 2))

def quarterPrefixTermExpr (n : ℕ) (c : ℚ) (M : ℕ) : Expr :=
  .sub
    (.const (RatPoly.prefixAQ n / (RatPoly.prefixAQ n ^ 2 + 625)))
    (.mul (.const (RatPoly.prefixAQ n))
      (.mul (.const (RatPoly.prefixDenominatorBaseQ n c)⁻¹)
        (.geometricReciprocal
          (prefixDenominatorPerturbationExpr n c) M)))

def quarterDifferenceFinitePrefixExpr (c : ℚ) (M : ℕ) : Expr :=
  .sumRange 64 (fun n => quarterPrefixTermExpr n c M)

def p2RationalQuarterTailExpr : Expr :=
  .atom DenseRatPoly.p2RationalQuarterTailPoly

def cosTaylorExpr (N : ℕ) (L : ℚ) : Expr :=
  .atom (DenseRatPoly.cosTaylorPolynomial N L)

def p2RationalNonPrefixExpr : Expr :=
  .add p2RationalQuarterTailExpr
    (.mul (.const RatPoly.p2PrimeAmplitudeCenterQ)
      (.sub .one
        (cosTaylorExpr 128 RatPoly.p2LogTwoCenterQ)))

def p2DefectPanelExpr (c : ℚ) (M : ℕ) : Expr :=
  .add (quarterDifferenceFinitePrefixExpr c M)
    (.shift p2RationalNonPrefixExpr c)

def sphericalJRealExpr (n N : ℕ) : Expr :=
  .atom (DenseRatPoly.sphericalJRealPolynomial n N)

def p2SphericalRealExpr (n N : ℕ) : Expr :=
  .comp (sphericalJRealExpr n N)
    (.mul (.const (7 / 16)) .X)

def p2Spherical100PanelExpr (n : ℕ) (c : ℚ) : Expr :=
  .shift (p2SphericalRealExpr n 100) c

def p2SelectedComponent100ScaleCenterExpr
    (kind : P2SelectedKind) (k : Fin 24) (c : ℚ) : Expr :=
  .mul (.const (RatPoly.p2SelectedPhaseQ kind k.val))
    (.mul (.const (p2SelectedScaleCenterQ kind k))
      (p2Spherical100PanelExpr
        (p2SelectedDegree kind k.val) c))

def p2ScaleCenteredPanelIntegrandExpr
    (kind : P2SelectedKind) (i j : Fin 24)
    (c : ℚ) (M : ℕ) : Expr :=
  .mul (p2DefectPanelExpr c M)
    (.mul
      (p2SelectedComponent100ScaleCenterExpr kind j c)
      (p2SelectedComponent100ScaleCenterExpr kind i c))

/-- Normalize a centered panel from `x ∈ [-h,h]` to `t ∈ [-1,1]`. -/
def p2NormalizedPanelIntegrandExpr
    (kind : P2SelectedKind) (i j : Fin 24)
    (c h : ℚ) (M : ℕ) : Expr :=
  .affine (p2ScaleCenteredPanelIntegrandExpr kind i j c M) 0 h

/-! ## Exact-denotation audit -/

theorem denote_prefixDenominatorPerturbationExpr (n : ℕ) (c : ℚ) :
    (prefixDenominatorPerturbationExpr n c).denote =
      DenseRatPoly.prefixDenominatorPerturbation n c := by
  simp [prefixDenominatorPerturbationExpr,
    DenseRatPoly.prefixDenominatorPerturbation]

theorem denote_quarterPrefixTermExpr (n : ℕ) (c : ℚ) (M : ℕ) :
    (quarterPrefixTermExpr n c M).denote =
      DenseRatPoly.quarterPrefixTermPolynomial n c M := by
  simp [quarterPrefixTermExpr, DenseRatPoly.quarterPrefixTermPolynomial,
    denote_prefixDenominatorPerturbationExpr]

theorem denote_quarterDifferenceFinitePrefixExpr (c : ℚ) (M : ℕ) :
    (quarterDifferenceFinitePrefixExpr c M).denote =
      DenseRatPoly.quarterDifferenceFinitePrefixPolynomial c M := by
  simp [quarterDifferenceFinitePrefixExpr,
    DenseRatPoly.quarterDifferenceFinitePrefixPolynomial,
    denote_quarterPrefixTermExpr]

theorem denote_p2RationalQuarterTailExpr :
    p2RationalQuarterTailExpr.denote =
      DenseRatPoly.p2RationalQuarterTailPoly := by
  rfl

theorem denote_cosTaylorExpr (N : ℕ) (L : ℚ) :
    (cosTaylorExpr N L).denote =
      DenseRatPoly.cosTaylorPolynomial N L := by
  rfl

theorem denote_p2RationalNonPrefixExpr :
    p2RationalNonPrefixExpr.denote =
      DenseRatPoly.p2RationalNonPrefixPoly := by
  simp [p2RationalNonPrefixExpr, DenseRatPoly.p2RationalNonPrefixPoly,
    denote_p2RationalQuarterTailExpr, denote_cosTaylorExpr]

theorem denote_p2DefectPanelExpr (c : ℚ) (M : ℕ) :
    (p2DefectPanelExpr c M).denote =
      DenseRatPoly.p2DefectPanelPolynomial c M := by
  simp [p2DefectPanelExpr, DenseRatPoly.p2DefectPanelPolynomial,
    denote_quarterDifferenceFinitePrefixExpr,
    denote_p2RationalNonPrefixExpr]

theorem denote_sphericalJRealExpr (n N : ℕ) :
    (sphericalJRealExpr n N).denote =
      DenseRatPoly.sphericalJRealPolynomial n N := by
  rfl

theorem denote_p2SphericalRealExpr (n N : ℕ) :
    (p2SphericalRealExpr n N).denote =
      DenseRatPoly.p2SphericalRealPolynomial n N := by
  simp [p2SphericalRealExpr, DenseRatPoly.p2SphericalRealPolynomial,
    denote_sphericalJRealExpr]

theorem denote_p2Spherical100PanelExpr (n : ℕ) (c : ℚ) :
    (p2Spherical100PanelExpr n c).denote =
      DenseRatPoly.p2Spherical100PanelPolynomial n c := by
  simp [p2Spherical100PanelExpr,
    DenseRatPoly.p2Spherical100PanelPolynomial,
    denote_p2SphericalRealExpr]

theorem denote_p2SelectedComponent100ScaleCenterExpr
    (kind : P2SelectedKind) (k : Fin 24) (c : ℚ) :
    (p2SelectedComponent100ScaleCenterExpr kind k c).denote =
      DenseRatPoly.p2SelectedComponent100ScaleCenterPolynomial kind k c := by
  simp [p2SelectedComponent100ScaleCenterExpr,
    DenseRatPoly.p2SelectedComponent100ScaleCenterPolynomial,
    denote_p2Spherical100PanelExpr]

theorem denote_p2ScaleCenteredPanelIntegrandExpr
    (kind : P2SelectedKind) (i j : Fin 24) (c : ℚ) (M : ℕ) :
    (p2ScaleCenteredPanelIntegrandExpr kind i j c M).denote =
      DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial kind i j c M := by
  simp [p2ScaleCenteredPanelIntegrandExpr,
    DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial,
    denote_p2DefectPanelExpr,
    denote_p2SelectedComponent100ScaleCenterExpr]

theorem denote_p2NormalizedPanelIntegrandExpr
    (kind : P2SelectedKind) (i j : Fin 24)
    (c h : ℚ) (M : ℕ) :
    (p2NormalizedPanelIntegrandExpr kind i j c h M).denote =
      DenseRatPoly.affine
        (DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial kind i j c M)
        0 h := by
  simp [p2NormalizedPanelIntegrandExpr,
    denote_p2ScaleCenteredPanelIntegrandExpr]

/-! ## Exact normalization of dense integrals -/

/-- The executable dense integral is literally the rational-polynomial
integral of its proof-only realization. -/
theorem dense_exactIntegral_eq_realize
    (p : DenseRatPoly.Poly) (a b : ℚ) :
    DenseRatPoly.exactIntegral p a b =
      RatPoly.exactIntegral (DenseRatPoly.realize p) a b := by
  unfold DenseRatPoly.exactIntegral
  rw [← RatPoly.exactIntegral_ofCoeffs]
  rw [← DenseRatPoly.realize_eq_ofCoeffs]

/-- Dense form of the exact rational substitution `x = h*t`. -/
theorem dense_exactIntegral_centered_eq_scale_normalized
    (p : DenseRatPoly.Poly) (h : ℚ) :
    DenseRatPoly.exactIntegral p (-h) h =
      h * DenseRatPoly.exactIntegral (DenseRatPoly.affine p 0 h) (-1) 1 := by
  rw [dense_exactIntegral_eq_realize, dense_exactIntegral_eq_realize,
    DenseRatPoly.realize_affine]
  exact RatPoly.exactIntegral_centered_eq_scale_normalized
    (DenseRatPoly.realize p) h

/-! ## Bounded-denominator evaluator -/

/-- `10^-40` fixed grid for normalized defect factors and directly composed
panel components.  Direct composition rounds the final coefficient vector
once, avoiding the late-panel error amplification of rounded Horner. -/
def gridCells : ℕ := 10 ^ 40 - 1

/-- Evaluate an expression with an outward-rounding barrier at every node.
For composition, the outer expression is evaluated on the domain inferred
from the already rounded inner enclosure. -/
def Expr.run (cells : ℕ) : (h : ℚ) → Expr → RoundedRatPoly.Approx
  | h, .atom p => RoundedRatPoly.rounded cells h p
  | h, .add p q =>
      RoundedRatPoly.add cells h (p.run cells h) (q.run cells h)
  | h, .scale c p =>
      RoundedRatPoly.scale cells h c (p.run cells h)
  | h, .mul p q =>
      RoundedRatPoly.mul cells h (p.run cells h) (q.run cells h)
  | h, .comp outer inner =>
      let innerApprox := inner.run cells h
      let outerDomain :=
        RoundedRatPoly.absBound innerApprox.coeffs h + innerApprox.error
      RoundedRatPoly.compRounded cells h
        (outer.run cells outerDomain) innerApprox
  | h, .pow p n =>
      RoundedRatPoly.powRounded cells h (p.run cells h) n
  | h, .geometricReciprocal p n =>
      RoundedRatPoly.geometricReciprocalRounded cells h (p.run cells h) n

theorem evalReal_dense_pow
    (p : DenseRatPoly.Poly) (n : ℕ) (x : ℝ) :
    RoundedRatPoly.evalReal (DenseRatPoly.pow p n) x =
      RoundedRatPoly.evalReal p x ^ n := by
  simp [RoundedRatPoly.evalReal, DenseRatPoly.realize_pow]

@[simp] theorem evalReal_dense_nil (x : ℝ) :
    RoundedRatPoly.evalReal ([] : DenseRatPoly.Poly) x = 0 := by
  simpa [DenseRatPoly.zero] using RoundedRatPoly.evalReal_zero x

@[simp] theorem evalReal_dense_X (x : ℝ) :
    RoundedRatPoly.evalReal DenseRatPoly.X x = x := by
  simp [DenseRatPoly.X, RoundedRatPoly.evalReal_cons]

theorem evalReal_dense_geometricReciprocal
    (p : DenseRatPoly.Poly) (N : ℕ) (x : ℝ) :
    RoundedRatPoly.evalReal
        (DenseRatPoly.geometricReciprocal p N) x =
      ∑ k ∈ Finset.range N, (-RoundedRatPoly.evalReal p x) ^ k := by
  rw [RoundedRatPoly.evalReal,
    DenseRatPoly.realize_geometricReciprocal,
    RatPoly.toReal_finset_sum,
    Polynomial.eval_finsetSum]
  simp [RoundedRatPoly.evalReal]

/-- Generic semantic audit for the bounded-denominator evaluator.  This is
the key trust boundary: every computed error is a rational number, while the
theorem relates it to evaluation of the exact canonical expression over
`ℝ`. -/
theorem Expr.run_encloses
    (cells : ℕ) {h : ℚ} (hh : 0 ≤ h) (e : Expr) :
    RoundedRatPoly.Encloses h
      (RoundedRatPoly.evalReal e.denote) (e.run cells h) := by
  induction e generalizing h with
  | atom p =>
      exact RoundedRatPoly.rounded_encloses cells hh p
  | add p q ihp ihq =>
      simpa [RoundedRatPoly.Encloses, Expr.denote, Expr.run,
          RoundedRatPoly.evalReal_add] using
        RoundedRatPoly.add_encloses cells hh
          (p.run cells h) (q.run cells h) (ihp hh) (ihq hh)
  | scale c p ih =>
      simpa [RoundedRatPoly.Encloses, Expr.denote, Expr.run,
          RoundedRatPoly.evalReal_scale] using
        RoundedRatPoly.scale_encloses cells hh c
          (p.run cells h) (ih hh)
  | mul p q ihp ihq =>
      simpa [RoundedRatPoly.Encloses, Expr.denote, Expr.run,
          RoundedRatPoly.evalReal_mul] using
        RoundedRatPoly.mul_encloses cells hh
          (p.run cells h) (q.run cells h) (ihp hh) (ihq hh)
  | comp outer inner ihOuter ihInner =>
      simp only [Expr.denote, Expr.run]
      let innerApprox := inner.run cells h
      let outerDomain : ℚ :=
        RoundedRatPoly.absBound innerApprox.coeffs h + innerApprox.error
      have hInner : RoundedRatPoly.Encloses h
          (RoundedRatPoly.evalReal inner.denote) innerApprox := by
        exact ihInner hh
      have hInnerError : 0 ≤ innerApprox.error :=
        RoundedRatPoly.error_nonneg_of_encloses hh hInner
      have hOuterDomain : 0 ≤ outerDomain := by
        dsimp [outerDomain]
        exact add_nonneg
          (RoundedRatPoly.absBound_nonneg innerApprox.coeffs hh)
          hInnerError
      have hOuter : RoundedRatPoly.Encloses outerDomain
          (RoundedRatPoly.evalReal outer.denote)
          (outer.run cells outerDomain) := ihOuter hOuterDomain
      simpa [RoundedRatPoly.Encloses, innerApprox, outerDomain,
          RoundedRatPoly.evalReal_comp] using
        RoundedRatPoly.compRounded_encloses cells hh
          (outer.run cells outerDomain) innerApprox hOuter hInner
  | pow p n ih =>
      simpa [RoundedRatPoly.Encloses, Expr.denote, Expr.run,
          evalReal_dense_pow] using
        RoundedRatPoly.powRounded_encloses cells hh
          (p.run cells h) (ih hh) n
  | geometricReciprocal p n ih =>
      simpa [RoundedRatPoly.Encloses, Expr.denote, Expr.run,
          evalReal_dense_geometricReciprocal] using
        RoundedRatPoly.geometricReciprocalRounded_encloses cells hh
          (p.run cells h) (ih hh) n

/-! ### Separately cacheable normalized factors -/

def normalizedDefectExpr (k : Fin 32) : Expr :=
  .atom
    (DenseRatPoly.affine
      (DenseRatPoly.p2DefectPanelPolynomial
        (p2PanelCenterQ k.val) 32)
      0 (p2PanelHalfWidthQ k.val))

def normalizedComponentExpr
    (kind : P2SelectedKind) (i : Fin 24) (k : Fin 32) : Expr :=
  .atom
    (DenseRatPoly.affine
      (DenseRatPoly.p2SelectedComponent100ScaleCenterPolynomial
        kind i (p2PanelCenterQ k.val))
      0 (p2PanelHalfWidthQ k.val))

def normalizedDefectApprox (k : Fin 32) : RoundedRatPoly.Approx :=
  (normalizedDefectExpr k).run gridCells 1

def normalizedComponentApprox
    (kind : P2SelectedKind) (i : Fin 24) (k : Fin 32) :
    RoundedRatPoly.Approx :=
  (normalizedComponentExpr kind i k).run gridCells 1

theorem evalReal_normalizedDefectExpr_eq_canonical
    (k : Fin 32) (t : ℝ) :
    RoundedRatPoly.evalReal (normalizedDefectExpr k).denote t =
      RoundedRatPoly.evalReal
        (DenseRatPoly.affine
          (DenseRatPoly.p2DefectPanelPolynomial
            (p2PanelCenterQ k.val) 32)
          0 (p2PanelHalfWidthQ k.val)) t := rfl

theorem evalReal_normalizedComponentExpr_eq_canonical
    (kind : P2SelectedKind) (i : Fin 24) (k : Fin 32) (t : ℝ) :
    RoundedRatPoly.evalReal (normalizedComponentExpr kind i k).denote t =
      RoundedRatPoly.evalReal
        (DenseRatPoly.affine
          (DenseRatPoly.p2SelectedComponent100ScaleCenterPolynomial
            kind i (p2PanelCenterQ k.val))
          0 (p2PanelHalfWidthQ k.val)) t := rfl

theorem normalizedDefectApprox_encloses (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (normalizedDefectExpr k).denote)
      (normalizedDefectApprox k) := by
  exact Expr.run_encloses gridCells (by norm_num) _

theorem normalizedComponentApprox_encloses
    (kind : P2SelectedKind) (i : Fin 24) (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (normalizedComponentExpr kind i k).denote)
      (normalizedComponentApprox kind i k) := by
  exact Expr.run_encloses gridCells (by norm_num) _

/-! ### From a uniform enclosure to an exact rational integral interval -/

/-- Integrating a fixed-domain rounded enclosure costs twice its uniform
error.  Both endpoints of the conclusion are executable rationals. -/
theorem abs_dense_exactIntegral_sub_approx_le
    (exactPoly : DenseRatPoly.Poly) (approx : RoundedRatPoly.Approx)
    (hencl : RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal exactPoly) approx) :
    |DenseRatPoly.exactIntegral exactPoly (-1) 1 -
        DenseRatPoly.exactIntegral approx.coeffs (-1) 1| ≤
      2 * approx.error := by
  have hCentered : PolyEnclosure.CenteredEncloses 0 1
      (RoundedRatPoly.evalReal exactPoly)
      (RatPoly.toReal (DenseRatPoly.realize approx.coeffs))
      (approx.error : ℝ) := by
    intro x hx
    have hx' : |x| ≤ (((1 : ℚ) : ℝ)) := by simpa using hx
    simpa [RoundedRatPoly.evalReal] using hencl x hx'
  have hContinuous : Continuous (RoundedRatPoly.evalReal exactPoly) := by
    exact (RatPoly.toReal (DenseRatPoly.realize exactPoly)).continuous
  have hIntegrable :
      IntervalIntegrable
        (fun x : ℝ => RoundedRatPoly.evalReal exactPoly (0 + x))
        MeasureTheory.volume (-1) 1 := by
    simpa using hContinuous.intervalIntegrable (-1) 1
  have h := PolyEnclosure.integral_centered_sub_exactIntegral_le
    (c := (0 : ℝ)) (h := (1 : ℝ)) (e := (approx.error : ℝ))
    (by norm_num) hCentered hIntegrable
  have hExactIntegral :
      (∫ x : ℝ in (-1)..1, RoundedRatPoly.evalReal exactPoly x) =
        (DenseRatPoly.exactIntegral exactPoly (-1) 1 : ℝ) := by
    calc
      (∫ x : ℝ in (-1)..1, RoundedRatPoly.evalReal exactPoly x) =
          PolyEnclosure.exactIntegral
            (RatPoly.toReal (DenseRatPoly.realize exactPoly)) (-1) 1 := by
        exact PolyEnclosure.integral_eval_eq_exactIntegral _ _ _
      _ = (DenseRatPoly.exactIntegral exactPoly (-1) 1 : ℝ) :=
        by simpa using
          (DenseRatPoly.cast_exactIntegral exactPoly (-1) 1).symm
  have hApproxIntegral :
      PolyEnclosure.exactIntegral
          (RatPoly.toReal (DenseRatPoly.realize approx.coeffs)) (-1) 1 =
        (DenseRatPoly.exactIntegral approx.coeffs (-1) 1 : ℝ) := by
    simpa using
      (DenseRatPoly.cast_exactIntegral approx.coeffs (-1) 1).symm
  rw [show (fun x : ℝ => RoundedRatPoly.evalReal exactPoly (0 + x)) =
      RoundedRatPoly.evalReal exactPoly by funext x; simp,
    hExactIntegral,
    hApproxIntegral] at h
  norm_num at h
  exact_mod_cast h

/-- The executable normalized approximation for one canonical panel. -/
def normalizedPanelApprox
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) :
    RoundedRatPoly.Approx :=
  (p2NormalizedPanelIntegrandExpr kind i j
    (p2PanelCenterQ k.val) (p2PanelHalfWidthQ k.val) 32).run
      gridCells 1

/-- Center of the outward-rounded original-coordinate panel integral. -/
def panelIntegralCenterQ
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) : ℚ :=
  p2PanelHalfWidthQ k.val *
    DenseRatPoly.exactIntegral
      (normalizedPanelApprox kind i j k).coeffs (-1) 1

/-- Radius paid for rounding the polynomial computation on one panel. -/
def panelIntegralRadiusQ
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) : ℚ :=
  2 * p2PanelHalfWidthQ k.val *
    (normalizedPanelApprox kind i j k).error

theorem p2PanelHalfWidthQ_nonneg (k : Fin 32) :
    0 ≤ p2PanelHalfWidthQ k.val := by
  have h : (0 : ℝ) ≤ (p2PanelHalfWidthQ k.val : ℝ) := by
    simpa [p2PanelHalfWidth] using p2PanelHalfWidth_nonneg k
  exact_mod_cast h

theorem normalizedPanelApprox_encloses
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal
        (DenseRatPoly.affine
          (DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial
            kind i j (p2PanelCenterQ k.val) 32)
          0 (p2PanelHalfWidthQ k.val)))
      (normalizedPanelApprox kind i j k) := by
  simpa [normalizedPanelApprox,
      denote_p2NormalizedPanelIntegrandExpr] using
    Expr.run_encloses gridCells (by norm_num)
      (p2NormalizedPanelIntegrandExpr kind i j
        (p2PanelCenterQ k.val) (p2PanelHalfWidthQ k.val) 32)

/-- Kernel-checked analytic error bound for one rounded panel integral. -/
theorem abs_p2PanelIntegralQ_sub_roundedCenter_le
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) :
    |DenseRatPoly.p2PanelIntegralQ kind i j k.val -
        panelIntegralCenterQ kind i j k| ≤
      panelIntegralRadiusQ kind i j k := by
  let p := DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial
    kind i j (p2PanelCenterQ k.val) 32
  let q := normalizedPanelApprox kind i j k
  let h := p2PanelHalfWidthQ k.val
  have hh : 0 ≤ h := p2PanelHalfWidthQ_nonneg k
  have hencl : RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (DenseRatPoly.affine p 0 h)) q := by
    simpa [p, q, h] using normalizedPanelApprox_encloses kind i j k
  have hi :
      |DenseRatPoly.exactIntegral (DenseRatPoly.affine p 0 h) (-1) 1 -
          DenseRatPoly.exactIntegral q.coeffs (-1) 1| ≤
        2 * q.error :=
    abs_dense_exactIntegral_sub_approx_le _ _ hencl
  rw [DenseRatPoly.p2PanelIntegralQ,
    DenseRatPoly.p2ScaleCenteredPanelIntegralQ,
    show DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial
        kind i j (p2PanelCenterQ k.val) 32 = p by rfl,
    dense_exactIntegral_centered_eq_scale_normalized]
  change
    |h * DenseRatPoly.exactIntegral (DenseRatPoly.affine p 0 h) (-1) 1 -
        h * DenseRatPoly.exactIntegral q.coeffs (-1) 1| ≤
      2 * h * q.error
  calc
    |h * DenseRatPoly.exactIntegral (DenseRatPoly.affine p 0 h) (-1) 1 -
        h * DenseRatPoly.exactIntegral q.coeffs (-1) 1| =
        h * |DenseRatPoly.exactIntegral (DenseRatPoly.affine p 0 h) (-1) 1 -
          DenseRatPoly.exactIntegral q.coeffs (-1) 1| := by
      rw [← mul_sub, abs_mul, abs_of_nonneg hh]
    _ ≤ h * (2 * q.error) := mul_le_mul_of_nonneg_left hi hh
    _ = 2 * h * q.error := by ring

end P2RoundedCanonical

end RHP2Bridge
