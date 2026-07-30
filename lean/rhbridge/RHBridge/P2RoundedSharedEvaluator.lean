/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedIntegralBridge
import RHBridge.P2PoleCanonicalDense
import RHBridge.P2EntryTable
import Batteries.Data.Vector.Lemmas

/-!
# Shared rounded evaluator for the canonical `p = 2` matrix

The direct rounded formula rebuilds a large defect expression and two
component expressions for every matrix entry.  Here each panel instead owns
one rounded defect and 48 rounded selected components.  An eager panel vector
uses that cache to produce all 600 upper-triangular integral balls, and a
streaming fold aggregates the 32 panel vectors.

The semantic statements remain independent of this evaluation strategy:
they prove that every cache-based entry ball encloses the exact canonical
rational panel integral.  Closed predicates are exposed separately so a
certificate can be split into kernel-manageable rows or chunks.
-/

namespace RHP2Bridge

namespace P2RoundedSharedEvaluator

open scoped BigOperators
open P2RoundedCanonical

abbrev Approx := RoundedRatPoly.Approx

/-- One normalized panel's shared rounded factors. -/
structure PanelCache where
  defect : Approx
  evenComponents : Vector Approx 24
  oddComponents : Vector Approx 24
  deriving Repr, DecidableEq

def componentVector
    (kind : P2SelectedKind) (k : Fin 32) : Vector Approx 24 :=
  Vector.ofFn fun i => normalizedComponentApprox kind i k

def buildPanelCache (k : Fin 32) : PanelCache where
  defect := normalizedDefectApprox k
  evenComponents := componentVector .even k
  oddComponents := componentVector .odd k

def PanelCache.component
    (cache : PanelCache) (kind : P2SelectedKind) (i : Fin 24) : Approx :=
  match kind with
  | .even => cache.evenComponents.get i
  | .odd => cache.oddComponents.get i

/-- Factorwise correctness boundary for an explicit generated cache.  It is
deliberately not a single structure equality: generated modules can prove
the 49 component equalities in small opaque kernel checks. -/
structure PanelCache.CorrectFor
    (cache : PanelCache) (k : Fin 32) : Prop where
  defect_eq : cache.defect = normalizedDefectApprox k
  even_eq : ∀ i : Fin 24,
    cache.evenComponents.get i = normalizedComponentApprox .even i k
  odd_eq : ∀ i : Fin 24,
    cache.oddComponents.get i = normalizedComponentApprox .odd i k

@[simp] theorem componentVector_get
    (kind : P2SelectedKind) (k : Fin 32) (i : Fin 24) :
    (componentVector kind k).get i =
      normalizedComponentApprox kind i k := by
  simp [componentVector]

@[simp] theorem buildPanelCache_defect (k : Fin 32) :
    (buildPanelCache k).defect = normalizedDefectApprox k := rfl

@[simp] theorem buildPanelCache_component
    (kind : P2SelectedKind) (k : Fin 32) (i : Fin 24) :
    (buildPanelCache k).component kind i =
      normalizedComponentApprox kind i k := by
  cases kind <;>
    simp [buildPanelCache, PanelCache.component, componentVector]

theorem buildPanelCache_correctFor (k : Fin 32) :
    (buildPanelCache k).CorrectFor k := by
  constructor
  · rfl
  · intro i
    exact componentVector_get .even k i
  · intro i
    exact componentVector_get .odd k i

theorem PanelCache.component_eq_of_correct
    {cache : PanelCache} {k : Fin 32} (hcache : cache.CorrectFor k)
    (kind : P2SelectedKind) (i : Fin 24) :
    cache.component kind i = normalizedComponentApprox kind i k := by
  cases kind with
  | even => exact hcache.even_eq i
  | odd => exact hcache.odd_eq i

/-- Exact normalized factors used by the semantic cache interface. -/
def exactNormalizedDefect (k : Fin 32) : DenseRatPoly.Poly :=
  DenseRatPoly.affine
    (DenseRatPoly.p2DefectPanelPolynomial
      (p2PanelCenterQ k.val) 32)
    0 (p2PanelHalfWidthQ k.val)

def exactNormalizedComponent
    (kind : P2SelectedKind) (i : Fin 24) (k : Fin 32) :
    DenseRatPoly.Poly :=
  DenseRatPoly.affine
    (DenseRatPoly.p2SelectedComponent100ScaleCenterPolynomial
      kind i (p2PanelCenterQ k.val))
    0 (p2PanelHalfWidthQ k.val)

/-! ### Shared global spherical checkpoints -/

/-- The global spherical outer approximations use a finer grid because each
of the 48 values is checked only once and reused on all 32 panels.  The
`10^-220` grid leaves ample margin after evaluation on `[-22,22]`. -/
def sphericalOuterCells : ℕ := 10 ^ 220 - 1

def sphericalOuterExact (n : Fin 48) : DenseRatPoly.Poly :=
  DenseRatPoly.sphericalJRealPolynomial n.val 100

def sphericalOuterApprox (n : Fin 48) : Approx :=
  RoundedRatPoly.rounded sphericalOuterCells 22 (sphericalOuterExact n)

theorem sphericalOuterApprox_encloses (n : Fin 48) :
    RoundedRatPoly.Encloses 22
      (RoundedRatPoly.evalReal (sphericalOuterExact n))
      (sphericalOuterApprox n) := by
  exact RoundedRatPoly.rounded_encloses sphericalOuterCells
    (by norm_num) _

def normalizedSphericalArgumentPoly (k : Fin 32) : DenseRatPoly.Poly :=
  [(7 / 16) * p2PanelCenterQ k.val,
    (7 / 16) * p2PanelHalfWidthQ k.val]

def normalizedSphericalArgumentApprox (k : Fin 32) : Approx :=
  RoundedRatPoly.exact (normalizedSphericalArgumentPoly k)

/-- Every normalized affine spherical argument lies in the common rational
outer domain `[-22,22]`. -/
theorem normalizedSphericalArgumentDomain_le_22 (k : Fin 32) :
    RoundedRatPoly.absBound
        (normalizedSphericalArgumentApprox k).coeffs 1 +
      (normalizedSphericalArgumentApprox k).error ≤ 22 := by
  fin_cases k <;>
    norm_num [normalizedSphericalArgumentApprox,
      normalizedSphericalArgumentPoly, RoundedRatPoly.exact,
      RoundedRatPoly.absBound, p2PanelCenterQ, p2PanelHalfWidthQ,
      p2PanelEndpointQ, abs_of_nonneg, abs_of_pos]

theorem abs_normalizedSphericalArgument_le_22
    (k : Fin 32) {t : ℝ} (ht : |t| ≤ 1) :
    |(7 / 16 : ℝ) *
        ((p2PanelCenterQ k.val : ℝ) +
          (p2PanelHalfWidthQ k.val : ℝ) * t)| ≤ 22 := by
  have hbound := RoundedRatPoly.abs_evalReal_le_absBound
    (normalizedSphericalArgumentPoly k) (h := (1 : ℚ))
    (by norm_num) (by simpa using ht)
  calc
    |(7 / 16 : ℝ) *
        ((p2PanelCenterQ k.val : ℝ) +
          (p2PanelHalfWidthQ k.val : ℝ) * t)| =
        |RoundedRatPoly.evalReal
          (normalizedSphericalArgumentPoly k) t| := by
      congr 1
      simp [normalizedSphericalArgumentPoly,
        RoundedRatPoly.evalReal_cons]
      ring
    _ ≤ (RoundedRatPoly.absBound
          (normalizedSphericalArgumentPoly k) 1 : ℝ) := hbound
    _ ≤ 22 := by
      have hdomain : RoundedRatPoly.absBound
          (normalizedSphericalArgumentPoly k) 1 ≤ 22 := by
        simpa [normalizedSphericalArgumentApprox,
          RoundedRatPoly.exact] using
            normalizedSphericalArgumentDomain_le_22 k
      exact_mod_cast hdomain

def componentApproxFromOuter
    (outer : Approx) (kind : P2SelectedKind)
    (i : Fin 24) (k : Fin 32) : Approx :=
  RoundedRatPoly.scale gridCells 1
    (RatPoly.p2SelectedPhaseQ kind i.val *
      p2SelectedScaleCenterQ kind i)
    (RoundedRatPoly.compRounded gridCells 1 outer
      (normalizedSphericalArgumentApprox k))

theorem evalReal_exactNormalizedComponent_eq_outer
    (kind : P2SelectedKind) (i : Fin 24) (k : Fin 32) (t : ℝ) :
    RoundedRatPoly.evalReal (exactNormalizedComponent kind i k) t =
      ((RatPoly.p2SelectedPhaseQ kind i.val *
          p2SelectedScaleCenterQ kind i : ℚ) : ℝ) *
        RoundedRatPoly.evalReal
          (DenseRatPoly.sphericalJRealPolynomial
            (p2SelectedDegree kind i.val) 100)
          (RoundedRatPoly.evalReal
            (normalizedSphericalArgumentPoly k) t) := by
  simp [exactNormalizedComponent,
    DenseRatPoly.p2SelectedComponent100ScaleCenterPolynomial,
    DenseRatPoly.p2Spherical100PanelPolynomial,
    DenseRatPoly.p2SphericalRealPolynomial,
    DenseRatPoly.shift, DenseRatPoly.affine,
    normalizedSphericalArgumentPoly,
    RoundedRatPoly.evalReal_mul, RoundedRatPoly.evalReal_comp,
    RoundedRatPoly.evalReal_cons]
  ring_nf

/-- A single global spherical outer enclosure yields a canonical normalized
component enclosure on any of the 32 panels. -/
theorem componentApproxFromOuter_encloses
    (outer : Approx) (kind : P2SelectedKind)
    (i : Fin 24) (k : Fin 32)
    (hOuter : RoundedRatPoly.Encloses 22
      (RoundedRatPoly.evalReal
        (DenseRatPoly.sphericalJRealPolynomial
          (p2SelectedDegree kind i.val) 100)) outer) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent kind i k))
      (componentApproxFromOuter outer kind i k) := by
  let inner := normalizedSphericalArgumentApprox k
  let H := RoundedRatPoly.absBound inner.coeffs 1 + inner.error
  have hH22 : H ≤ 22 := by
    simpa [H, inner] using normalizedSphericalArgumentDomain_le_22 k
  have hOuterH : RoundedRatPoly.Encloses H
      (RoundedRatPoly.evalReal
        (DenseRatPoly.sphericalJRealPolynomial
          (p2SelectedDegree kind i.val) 100)) outer :=
    hOuter.mono_domain hH22
  have hInner : RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (normalizedSphericalArgumentPoly k)) inner := by
    simpa [inner, normalizedSphericalArgumentApprox] using
      RoundedRatPoly.exact_encloses 1
        (normalizedSphericalArgumentPoly k)
  have hComp := RoundedRatPoly.compRounded_encloses gridCells
    (h := (1 : ℚ)) (by norm_num) outer inner
    (by simpa [H] using hOuterH) hInner
  have hScale := RoundedRatPoly.scale_encloses gridCells
    (h := (1 : ℚ)) (by norm_num)
    (RatPoly.p2SelectedPhaseQ kind i.val *
      p2SelectedScaleCenterQ kind i)
    (RoundedRatPoly.compRounded gridCells 1 outer inner) hComp
  intro t ht
  rw [evalReal_exactNormalizedComponent_eq_outer]
  simpa [componentApproxFromOuter, inner] using hScale t ht

def selectedDegreeFin
    (kind : P2SelectedKind) (i : Fin 24) : Fin 48 :=
  ⟨p2SelectedDegree kind i.val, by
    cases kind <;> simp [p2SelectedDegree] <;> omega⟩

def componentVectorFromOuters
    (outers : Vector Approx 48)
    (kind : P2SelectedKind) (k : Fin 32) : Vector Approx 24 :=
  Vector.ofFn fun i =>
    componentApproxFromOuter (outers.get (selectedDegreeFin kind i))
      kind i k

structure SphericalOutersEnclose (outers : Vector Approx 48) : Prop where
  encloses : ∀ n : Fin 48, RoundedRatPoly.Encloses 22
    (RoundedRatPoly.evalReal (sphericalOuterExact n)) (outers.get n)

/-- Reference outer vector computed by the trusted rounded kernel.  Generated
literal certificates can replace this vector while proving the same semantic
predicate one coordinate at a time. -/
def computedSphericalOuters : Vector Approx 48 :=
  Vector.ofFn sphericalOuterApprox

theorem computedSphericalOuters_enclose :
    SphericalOutersEnclose computedSphericalOuters := by
  constructor
  intro n
  simpa [computedSphericalOuters] using sphericalOuterApprox_encloses n

theorem componentVectorFromOuters_encloses
    {outers : Vector Approx 48} (hOuters : SphericalOutersEnclose outers)
    (kind : P2SelectedKind) (k : Fin 32) (i : Fin 24) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent kind i k))
      ((componentVectorFromOuters outers kind k).get i) := by
  simpa [componentVectorFromOuters, sphericalOuterExact,
      selectedDegreeFin] using
    componentApproxFromOuter_encloses
      (outers.get (selectedDegreeFin kind i)) kind i k
      (hOuters.encloses (selectedDegreeFin kind i))

def exactNormalizedPrefixTerm (n : ℕ) (k : Fin 32) :
    DenseRatPoly.Poly :=
  DenseRatPoly.affine
    (DenseRatPoly.quarterPrefixTermPolynomial
      n (p2PanelCenterQ k.val) 32)
    0 (p2PanelHalfWidthQ k.val)

def exactNormalizedNonprefix (k : Fin 32) : DenseRatPoly.Poly :=
  DenseRatPoly.affine DenseRatPoly.p2RationalNonPrefixPoly
    (p2PanelCenterQ k.val) (p2PanelHalfWidthQ k.val)

/-- Small rounded expression used as the checkpoint target for one prefix
term. -/
def normalizedPrefixTermExpr (n : Fin 64) (k : Fin 32) : Expr :=
  .affine
    (quarterPrefixTermExpr n.val (p2PanelCenterQ k.val) 32)
    0 (p2PanelHalfWidthQ k.val)

def normalizedPrefixTermApprox (n : Fin 64) (k : Fin 32) : Approx :=
  (normalizedPrefixTermExpr n k).run gridCells 1

def normalizedNonprefixExpr (k : Fin 32) : Expr :=
  .affine p2RationalNonPrefixExpr
    (p2PanelCenterQ k.val) (p2PanelHalfWidthQ k.val)

def normalizedNonprefixApprox (k : Fin 32) : Approx :=
  (normalizedNonprefixExpr k).run gridCells 1

/-- One-shot atom targets matching generated fixed-grid coefficient data. -/
def normalizedPrefixTermAtomApprox (n : Fin 64) (k : Fin 32) : Approx :=
  RoundedRatPoly.rounded gridCells 1
    (exactNormalizedPrefixTerm n.val k)

def normalizedNonprefixAtomApprox (k : Fin 32) : Approx :=
  RoundedRatPoly.rounded gridCells 1 (exactNormalizedNonprefix k)

theorem normalizedPrefixTermApprox_encloses
    (n : Fin 64) (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedPrefixTerm n.val k))
      (normalizedPrefixTermApprox n k) := by
  simpa [normalizedPrefixTermExpr, normalizedPrefixTermApprox,
      exactNormalizedPrefixTerm,
      P2RoundedCanonical.denote_quarterPrefixTermExpr] using
    Expr.run_encloses gridCells (by norm_num)
      (normalizedPrefixTermExpr n k)

theorem normalizedNonprefixApprox_encloses (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedNonprefix k))
      (normalizedNonprefixApprox k) := by
  simpa [normalizedNonprefixExpr, normalizedNonprefixApprox,
      exactNormalizedNonprefix,
      P2RoundedCanonical.denote_p2RationalNonPrefixExpr] using
    Expr.run_encloses gridCells (by norm_num) (normalizedNonprefixExpr k)

theorem normalizedPrefixTermAtomApprox_encloses
    (n : Fin 64) (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedPrefixTerm n.val k))
      (normalizedPrefixTermAtomApprox n k) := by
  exact RoundedRatPoly.rounded_encloses gridCells (by norm_num) _

theorem normalizedNonprefixAtomApprox_encloses (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedNonprefix k))
      (normalizedNonprefixAtomApprox k) := by
  exact RoundedRatPoly.rounded_encloses gridCells (by norm_num) _

/-- Algebraic decomposition used to certify the large defect factor in 65
small pieces rather than by one monolithic equality. -/
def exactNormalizedDefectPieces (k : Fin 32) : DenseRatPoly.Poly :=
  DenseRatPoly.add
    (DenseRatPoly.sumRange 64
      (fun n => exactNormalizedPrefixTerm n k))
    (exactNormalizedNonprefix k)

theorem realize_exactNormalizedDefectPieces (k : Fin 32) :
    DenseRatPoly.realize (exactNormalizedDefectPieces k) =
      DenseRatPoly.realize (exactNormalizedDefect k) := by
  simp [exactNormalizedDefectPieces, exactNormalizedPrefixTerm,
    exactNormalizedNonprefix, exactNormalizedDefect,
    DenseRatPoly.p2DefectPanelPolynomial,
    DenseRatPoly.quarterDifferenceFinitePrefixPolynomial,
    DenseRatPoly.shift, DenseRatPoly.realize_add,
    DenseRatPoly.realize_sumRange, DenseRatPoly.realize_affine,
    Polynomial.comp_assoc, Polynomial.add_comp,
    Polynomial.C_comp, Polynomial.X_comp, Polynomial.sum_comp]

theorem evalReal_dense_sumRange
    (N : ℕ) (f : ℕ → DenseRatPoly.Poly) (t : ℝ) :
    RoundedRatPoly.evalReal (DenseRatPoly.sumRange N f) t =
      ∑ n ∈ Finset.range N, RoundedRatPoly.evalReal (f n) t := by
  rw [RoundedRatPoly.evalReal, DenseRatPoly.realize_sumRange,
    RatPoly.toReal_finset_sum, Polynomial.eval_finsetSum]
  simp [RoundedRatPoly.evalReal]

theorem evalReal_exactNormalizedDefect_eq_pieceSum
    (k : Fin 32) (t : ℝ) :
    RoundedRatPoly.evalReal (exactNormalizedDefect k) t =
      (∑ n ∈ Finset.range 64,
        RoundedRatPoly.evalReal (exactNormalizedPrefixTerm n k) t) +
      RoundedRatPoly.evalReal (exactNormalizedNonprefix k) t := by
  have hrealize := realize_exactNormalizedDefectPieces k
  rw [show RoundedRatPoly.evalReal (exactNormalizedDefect k) t =
      RoundedRatPoly.evalReal (exactNormalizedDefectPieces k) t by
    simp [RoundedRatPoly.evalReal, hrealize]]
  simp [exactNormalizedDefectPieces, RoundedRatPoly.evalReal_add,
    evalReal_dense_sumRange]

/-- Explicit small-piece representation of the normalized defect. -/
structure DefectPieces where
  prefixTerms : Vector Approx 64
  nonprefix : Approx
  deriving Repr, DecidableEq

def computedDefectPieces (k : Fin 32) : DefectPieces where
  prefixTerms := Vector.ofFn fun n => normalizedPrefixTermApprox n k
  nonprefix := normalizedNonprefixApprox k

def computedDefectAtomPieces (k : Fin 32) : DefectPieces where
  prefixTerms := Vector.ofFn fun n => normalizedPrefixTermAtomApprox n k
  nonprefix := normalizedNonprefixAtomApprox k

def DefectPieces.prefixAt (pieces : DefectPieces) (n : ℕ) : Approx :=
  pieces.prefixTerms.get ⟨n % 64, Nat.mod_lt n (by norm_num)⟩

def DefectPieces.assemble (pieces : DefectPieces) : Approx :=
  RoundedRatPoly.add gridCells 1
    (RoundedRatPoly.sumRangeRounded gridCells 1 64 pieces.prefixAt)
    pieces.nonprefix

structure DefectPieces.EnclosesCanonical
    (pieces : DefectPieces) (k : Fin 32) : Prop where
  prefix_encloses : ∀ i : Fin 64,
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal
        (exactNormalizedPrefixTerm i.val k))
      (pieces.prefixTerms.get i)
  nonprefix_encloses : RoundedRatPoly.Encloses 1
    (RoundedRatPoly.evalReal (exactNormalizedNonprefix k))
    pieces.nonprefix

theorem computedDefectPieces_enclosesCanonical (k : Fin 32) :
    (computedDefectPieces k).EnclosesCanonical k := by
  constructor
  · intro i
    simpa [computedDefectPieces] using
      normalizedPrefixTermApprox_encloses i k
  · exact normalizedNonprefixApprox_encloses k

theorem computedDefectAtomPieces_enclosesCanonical (k : Fin 32) :
    (computedDefectAtomPieces k).EnclosesCanonical k := by
  constructor
  · intro i
    simpa [computedDefectAtomPieces] using
      normalizedPrefixTermAtomApprox_encloses i k
  · exact normalizedNonprefixAtomApprox_encloses k

/-- Assemble a semantic defect certificate from 64 independently checked
prefix terms and one nonprefix term. -/
theorem DefectPieces.assemble_encloses
    {pieces : DefectPieces} {k : Fin 32}
    (hpieces : pieces.EnclosesCanonical k) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedDefect k))
      pieces.assemble := by
  have hprefix : ∀ n : ℕ,
      RoundedRatPoly.Encloses 1
        (RoundedRatPoly.evalReal
          (exactNormalizedPrefixTerm (n % 64) k))
        (pieces.prefixAt n) := by
    intro n
    exact hpieces.prefix_encloses
      ⟨n % 64, Nat.mod_lt n (by norm_num)⟩
  have hsum := RoundedRatPoly.sumRangeRounded_encloses gridCells
    (h := (1 : ℚ)) (by norm_num)
    (f := fun n t => RoundedRatPoly.evalReal
      (exactNormalizedPrefixTerm (n % 64) k) t)
    (p := pieces.prefixAt) hprefix 64
  have hadd := RoundedRatPoly.add_encloses gridCells
    (h := (1 : ℚ)) (by norm_num)
    (RoundedRatPoly.sumRangeRounded gridCells 1 64 pieces.prefixAt)
    pieces.nonprefix hsum hpieces.nonprefix_encloses
  intro t ht
  rw [evalReal_exactNormalizedDefect_eq_pieceSum]
  have hmod :
      (∑ n ∈ Finset.range 64,
          RoundedRatPoly.evalReal
            (exactNormalizedPrefixTerm (n % 64) k) t) =
        ∑ n ∈ Finset.range 64,
          RoundedRatPoly.evalReal (exactNormalizedPrefixTerm n k) t := by
    apply Finset.sum_congr rfl
    intro n hn
    rw [Nat.mod_eq_of_lt (Finset.mem_range.mp hn)]
  rw [← hmod]
  simpa [DefectPieces.assemble] using hadd t ht

def panelCacheOfPieces
    (pieces : DefectPieces)
    (evenComponents oddComponents : Vector Approx 24) : PanelCache where
  defect := pieces.assemble
  evenComponents := evenComponents
  oddComponents := oddComponents

/-- Build a panel cache from independently certified defect pieces and the
48 shared global spherical outer approximations. -/
def panelCacheFromPiecesAndOuters
    (pieces : DefectPieces) (outers : Vector Approx 48)
    (k : Fin 32) : PanelCache :=
  panelCacheOfPieces pieces
    (componentVectorFromOuters outers .even k)
    (componentVectorFromOuters outers .odd k)

/-- The exact affine normalization of the canonical panel integrand. -/
def exactNormalizedIntegrand
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) :
    DenseRatPoly.Poly :=
  DenseRatPoly.affine
    (DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial
      kind i j (p2PanelCenterQ k.val) 32)
    0 (p2PanelHalfWidthQ k.val)

/-- Pointwise bridge from the optimized separately normalized factors to
the canonical affine-normalized product. -/
theorem evalReal_exactNormalizedIntegrand_eq_factors
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) (t : ℝ) :
    RoundedRatPoly.evalReal (exactNormalizedIntegrand kind i j k) t =
      RoundedRatPoly.evalReal (normalizedDefectExpr k).denote t *
        (RoundedRatPoly.evalReal
            (normalizedComponentExpr kind j k).denote t *
          RoundedRatPoly.evalReal
            (normalizedComponentExpr kind i k).denote t) := by
  rw [evalReal_normalizedDefectExpr_eq_canonical,
    evalReal_normalizedComponentExpr_eq_canonical,
    evalReal_normalizedComponentExpr_eq_canonical]
  simp [exactNormalizedIntegrand,
    DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial,
    DenseRatPoly.affine, RoundedRatPoly.evalReal_comp,
    RoundedRatPoly.evalReal_mul]

theorem evalReal_exactNormalizedIntegrand_eq_canonicalFactors
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) (t : ℝ) :
    RoundedRatPoly.evalReal (exactNormalizedIntegrand kind i j k) t =
      RoundedRatPoly.evalReal (exactNormalizedDefect k) t *
        (RoundedRatPoly.evalReal
            (exactNormalizedComponent kind j k) t *
          RoundedRatPoly.evalReal
            (exactNormalizedComponent kind i k) t) := by
  rw [evalReal_exactNormalizedIntegrand_eq_factors,
    evalReal_normalizedDefectExpr_eq_canonical,
    evalReal_normalizedComponentExpr_eq_canonical,
    evalReal_normalizedComponentExpr_eq_canonical]
  rfl

theorem normalizedDefectApprox_encloses_exact (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedDefect k))
      (normalizedDefectApprox k) := by
  intro t ht
  rw [show RoundedRatPoly.evalReal (exactNormalizedDefect k) t =
      RoundedRatPoly.evalReal (normalizedDefectExpr k).denote t by
    exact (evalReal_normalizedDefectExpr_eq_canonical k t).symm]
  exact normalizedDefectApprox_encloses k t ht

theorem normalizedComponentApprox_encloses_exact
    (kind : P2SelectedKind) (i : Fin 24) (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent kind i k))
      (normalizedComponentApprox kind i k) := by
  intro t ht
  rw [show
      RoundedRatPoly.evalReal (exactNormalizedComponent kind i k) t =
        RoundedRatPoly.evalReal
          (normalizedComponentExpr kind i k).denote t by
    exact (evalReal_normalizedComponentExpr_eq_canonical
      kind i k t).symm]
  exact normalizedComponentApprox_encloses kind i k t ht

/-- Purely semantic correctness for an explicit factor cache.  Unlike
`CorrectFor`, this interface can be assembled from many small enclosure
theorems without reducing a monolithic defect equality. -/
structure PanelCache.EnclosesCanonical
    (cache : PanelCache) (k : Fin 32) : Prop where
  defect_encloses : RoundedRatPoly.Encloses 1
    (RoundedRatPoly.evalReal (exactNormalizedDefect k)) cache.defect
  even_encloses : ∀ i : Fin 24, RoundedRatPoly.Encloses 1
    (RoundedRatPoly.evalReal (exactNormalizedComponent .even i k))
    (cache.component .even i)
  odd_encloses : ∀ i : Fin 24, RoundedRatPoly.Encloses 1
    (RoundedRatPoly.evalReal (exactNormalizedComponent .odd i k))
    (cache.component .odd i)

theorem PanelCache.EnclosesCanonical.component_encloses
    {cache : PanelCache} {k : Fin 32}
    (hcache : cache.EnclosesCanonical k)
    (kind : P2SelectedKind) (i : Fin 24) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent kind i k))
      (cache.component kind i) := by
  cases kind with
  | even => exact hcache.even_encloses i
  | odd => exact hcache.odd_encloses i

theorem PanelCache.CorrectFor.enclosesCanonical
    {cache : PanelCache} {k : Fin 32} (hcache : cache.CorrectFor k) :
    cache.EnclosesCanonical k := by
  constructor
  · rw [hcache.defect_eq]
    exact normalizedDefectApprox_encloses_exact k
  · intro i
    rw [PanelCache.component_eq_of_correct hcache]
    exact normalizedComponentApprox_encloses_exact .even i k
  · intro i
    rw [PanelCache.component_eq_of_correct hcache]
    exact normalizedComponentApprox_encloses_exact .odd i k

theorem panelCacheOfPieces_enclosesCanonical
    {pieces : DefectPieces} {k : Fin 32}
    {evenComponents oddComponents : Vector Approx 24}
    (hpieces : pieces.EnclosesCanonical k)
    (heven : ∀ i : Fin 24, RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent .even i k))
      (evenComponents.get i))
    (hodd : ∀ i : Fin 24, RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedComponent .odd i k))
      (oddComponents.get i)) :
    (panelCacheOfPieces pieces evenComponents oddComponents).EnclosesCanonical k := by
  constructor
  · exact DefectPieces.assemble_encloses hpieces
  · exact heven
  · exact hodd

theorem panelCacheFromPiecesAndOuters_enclosesCanonical
    {pieces : DefectPieces} {outers : Vector Approx 48} {k : Fin 32}
    (hpieces : pieces.EnclosesCanonical k)
    (hOuters : SphericalOutersEnclose outers) :
    (panelCacheFromPiecesAndOuters pieces outers k).EnclosesCanonical k := by
  apply panelCacheOfPieces_enclosesCanonical hpieces
  · exact componentVectorFromOuters_encloses hOuters .even k
  · exact componentVectorFromOuters_encloses hOuters .odd k

/-- Build one entry's normalized rounded integrand from a shared cache. -/
def entryApprox
    (cache : PanelCache) (kind : P2SelectedKind) (i j : Fin 24) : Approx :=
  RoundedRatPoly.mul gridCells 1 cache.defect
    (RoundedRatPoly.mul gridCells 1
      (cache.component kind j) (cache.component kind i))

/-- The separately checkpointable inner product of the two selected
components in one entry. -/
def componentPairApprox
    (cache : PanelCache) (kind : P2SelectedKind) (i j : Fin 24) : Approx :=
  RoundedRatPoly.mul gridCells 1
    (cache.component kind j) (cache.component kind i)

/-- Finish an entry approximation from a separately checkpointed component
pair. -/
def entryApproxFromPair (cache : PanelCache) (pair : Approx) : Approx :=
  RoundedRatPoly.mul gridCells 1 cache.defect pair

@[simp] theorem entryApprox_eq_entryApproxFromPair
    (cache : PanelCache) (kind : P2SelectedKind) (i j : Fin 24) :
    entryApprox cache kind i j =
      entryApproxFromPair cache (componentPairApprox cache kind i j) := rfl

/-- A staged ordinary-kernel certificate for a literal entry approximation.
The pair and final product equalities may be checked in separate small
modules, while all analytic meaning continues to come from the certified
factor cache. -/
structure EntryProductCertificate
    (cache : PanelCache) (kind : P2SelectedKind) (i j : Fin 24)
    (literal : Approx) where
  pair : Approx
  pair_eq : pair = componentPairApprox cache kind i j
  entry_eq : literal = entryApproxFromPair cache pair

def EntryProductCertificate.direct
    (cache : PanelCache) (kind : P2SelectedKind) (i j : Fin 24) :
    EntryProductCertificate cache kind i j
      (entryApprox cache kind i j) := by
  refine ⟨componentPairApprox cache kind i j, rfl, ?_⟩
  rfl

def EntryProductCertificate.of_entryApprox_eq
    {cache : PanelCache} {kind : P2SelectedKind} {i j : Fin 24}
    {literal : Approx} (h : literal = entryApprox cache kind i j) :
    EntryProductCertificate cache kind i j literal := by
  refine ⟨componentPairApprox cache kind i j, rfl, ?_⟩
  simpa using h

/-- Direct sup-norm error ledger for three semantically certified factors.
No coefficient multiplication or rounding is used to compute this radius. -/
def tripleFactorError (d a b : Approx) : ℚ :=
  d.error * (RoundedRatPoly.absBound a.coeffs 1 + a.error) *
      (RoundedRatPoly.absBound b.coeffs 1 + b.error) +
    RoundedRatPoly.absBound d.coeffs 1 * a.error *
      (RoundedRatPoly.absBound b.coeffs 1 + b.error) +
    RoundedRatPoly.absBound d.coeffs 1 *
      RoundedRatPoly.absBound a.coeffs 1 * b.error

/-- Exact coefficient convolution equipped with the direct triple-factor
error ledger.  In contrast to `entryApprox`, this performs no coefficient
rounding and introduces no multiplication-rounding error. -/
def unroundedTripleProductApprox (d a b : Approx) : Approx where
  coeffs := DenseRatPoly.mul d.coeffs
    (DenseRatPoly.mul a.coeffs b.coeffs)
  error := tripleFactorError d a b

theorem unroundedTripleProductApprox_encloses
    {fd fa fb : ℝ → ℝ} (d a b : Approx)
    (hd : RoundedRatPoly.Encloses 1 fd d)
    (ha : RoundedRatPoly.Encloses 1 fa a)
    (hb : RoundedRatPoly.Encloses 1 fb b) :
    RoundedRatPoly.Encloses 1
      (fun x => fd x * (fa x * fb x))
      (unroundedTripleProductApprox d a b) := by
  intro x hx
  have hdAt := hd x hx
  have haAt := ha x hx
  have hbAt := hb x hx
  have hdBound := RoundedRatPoly.abs_evalReal_le_absBound
    d.coeffs (h := (1 : ℚ)) (by norm_num) hx
  have haBound := RoundedRatPoly.abs_evalReal_le_absBound
    a.coeffs (h := (1 : ℚ)) (by norm_num) hx
  have hbBound := RoundedRatPoly.abs_evalReal_le_absBound
    b.coeffs (h := (1 : ℚ)) (by norm_num) hx
  have haValue : |fa x| ≤
      ((RoundedRatPoly.absBound a.coeffs 1 + a.error : ℚ) : ℝ) := by
    calc
      |fa x| = |(fa x - RoundedRatPoly.evalReal a.coeffs x) +
          RoundedRatPoly.evalReal a.coeffs x| := by congr 1 <;> ring
      _ ≤ |fa x - RoundedRatPoly.evalReal a.coeffs x| +
          |RoundedRatPoly.evalReal a.coeffs x| := abs_add_le _ _
      _ ≤ (a.error : ℝ) +
          (RoundedRatPoly.absBound a.coeffs 1 : ℝ) :=
        add_le_add haAt haBound
      _ = ((RoundedRatPoly.absBound a.coeffs 1 + a.error : ℚ) : ℝ) := by
        push_cast
        ring
  have hbValue : |fb x| ≤
      ((RoundedRatPoly.absBound b.coeffs 1 + b.error : ℚ) : ℝ) := by
    calc
      |fb x| = |(fb x - RoundedRatPoly.evalReal b.coeffs x) +
          RoundedRatPoly.evalReal b.coeffs x| := by congr 1 <;> ring
      _ ≤ |fb x - RoundedRatPoly.evalReal b.coeffs x| +
          |RoundedRatPoly.evalReal b.coeffs x| := abs_add_le _ _
      _ ≤ (b.error : ℝ) +
          (RoundedRatPoly.absBound b.coeffs 1 : ℝ) :=
        add_le_add hbAt hbBound
      _ = ((RoundedRatPoly.absBound b.coeffs 1 + b.error : ℚ) : ℝ) := by
        push_cast
        ring
  have hdError0Q : 0 ≤ d.error :=
    RoundedRatPoly.error_nonneg_of_encloses (h := (1 : ℚ))
      (by norm_num) hd
  have haError0Q : 0 ≤ a.error :=
    RoundedRatPoly.error_nonneg_of_encloses (h := (1 : ℚ))
      (by norm_num) ha
  have hbError0Q : 0 ≤ b.error :=
    RoundedRatPoly.error_nonneg_of_encloses (h := (1 : ℚ))
      (by norm_num) hb
  have hdAbs0Q : 0 ≤ RoundedRatPoly.absBound d.coeffs 1 :=
    RoundedRatPoly.absBound_nonneg d.coeffs (h := (1 : ℚ))
      (by norm_num)
  have haAbs0Q : 0 ≤ RoundedRatPoly.absBound a.coeffs 1 :=
    RoundedRatPoly.absBound_nonneg a.coeffs (h := (1 : ℚ))
      (by norm_num)
  have hdError0 : (0 : ℝ) ≤ (d.error : ℝ) := by
    exact_mod_cast hdError0Q
  have haError0 : (0 : ℝ) ≤ (a.error : ℝ) := by
    exact_mod_cast haError0Q
  have hdAbs0 : (0 : ℝ) ≤
      (RoundedRatPoly.absBound d.coeffs 1 : ℝ) := by
    exact_mod_cast hdAbs0Q
  have haAbs0 : (0 : ℝ) ≤
      (RoundedRatPoly.absBound a.coeffs 1 : ℝ) := by
    exact_mod_cast haAbs0Q
  have haTotal0 : (0 : ℝ) ≤
      ((RoundedRatPoly.absBound a.coeffs 1 + a.error : ℚ) : ℝ) := by
    exact_mod_cast add_nonneg haAbs0Q haError0Q
  have hterm1 :
      |(fd x - RoundedRatPoly.evalReal d.coeffs x) * (fa x * fb x)| ≤
        (d.error : ℝ) *
          (RoundedRatPoly.absBound a.coeffs 1 + a.error : ℚ) *
          (RoundedRatPoly.absBound b.coeffs 1 + b.error : ℚ) := by
    rw [abs_mul, abs_mul]
    calc
      |fd x - RoundedRatPoly.evalReal d.coeffs x| *
          (|fa x| * |fb x|) ≤
          (d.error : ℝ) * (|fa x| * |fb x|) :=
        mul_le_mul_of_nonneg_right hdAt
          (mul_nonneg (abs_nonneg _) (abs_nonneg _))
      _ ≤ (d.error : ℝ) *
          (((RoundedRatPoly.absBound a.coeffs 1 + a.error : ℚ) : ℝ) *
            |fb x|) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_right haValue (abs_nonneg _)) hdError0
      _ ≤ (d.error : ℝ) *
          (((RoundedRatPoly.absBound a.coeffs 1 + a.error : ℚ) : ℝ) *
            ((RoundedRatPoly.absBound b.coeffs 1 + b.error : ℚ) : ℝ)) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_left hbValue haTotal0) hdError0
      _ = (d.error : ℝ) *
          (RoundedRatPoly.absBound a.coeffs 1 + a.error : ℚ) *
          (RoundedRatPoly.absBound b.coeffs 1 + b.error : ℚ) := by ring
  have hterm2 :
      |RoundedRatPoly.evalReal d.coeffs x *
          ((fa x - RoundedRatPoly.evalReal a.coeffs x) * fb x)| ≤
        (RoundedRatPoly.absBound d.coeffs 1 : ℝ) * a.error *
          (RoundedRatPoly.absBound b.coeffs 1 + b.error : ℚ) := by
    rw [abs_mul, abs_mul]
    calc
      |RoundedRatPoly.evalReal d.coeffs x| *
          (|fa x - RoundedRatPoly.evalReal a.coeffs x| * |fb x|) ≤
        (RoundedRatPoly.absBound d.coeffs 1 : ℝ) *
          (|fa x - RoundedRatPoly.evalReal a.coeffs x| * |fb x|) :=
        mul_le_mul_of_nonneg_right hdBound
          (mul_nonneg (abs_nonneg _) (abs_nonneg _))
      _ ≤ (RoundedRatPoly.absBound d.coeffs 1 : ℝ) *
          ((a.error : ℝ) * |fb x|) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_right haAt (abs_nonneg _)) hdAbs0
      _ ≤ (RoundedRatPoly.absBound d.coeffs 1 : ℝ) *
          ((a.error : ℝ) *
            ((RoundedRatPoly.absBound b.coeffs 1 + b.error : ℚ) : ℝ)) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_left hbValue haError0) hdAbs0
      _ = (RoundedRatPoly.absBound d.coeffs 1 : ℝ) * a.error *
          (RoundedRatPoly.absBound b.coeffs 1 + b.error : ℚ) := by ring
  have hterm3 :
      |RoundedRatPoly.evalReal d.coeffs x *
          (RoundedRatPoly.evalReal a.coeffs x *
            (fb x - RoundedRatPoly.evalReal b.coeffs x))| ≤
        (RoundedRatPoly.absBound d.coeffs 1 : ℝ) *
          (RoundedRatPoly.absBound a.coeffs 1 : ℝ) * b.error := by
    rw [abs_mul, abs_mul]
    calc
      |RoundedRatPoly.evalReal d.coeffs x| *
          (|RoundedRatPoly.evalReal a.coeffs x| *
            |fb x - RoundedRatPoly.evalReal b.coeffs x|) ≤
        (RoundedRatPoly.absBound d.coeffs 1 : ℝ) *
          (|RoundedRatPoly.evalReal a.coeffs x| *
            |fb x - RoundedRatPoly.evalReal b.coeffs x|) :=
        mul_le_mul_of_nonneg_right hdBound
          (mul_nonneg (abs_nonneg _) (abs_nonneg _))
      _ ≤ (RoundedRatPoly.absBound d.coeffs 1 : ℝ) *
          ((RoundedRatPoly.absBound a.coeffs 1 : ℝ) *
            |fb x - RoundedRatPoly.evalReal b.coeffs x|) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_right haBound (abs_nonneg _)) hdAbs0
      _ ≤ (RoundedRatPoly.absBound d.coeffs 1 : ℝ) *
          ((RoundedRatPoly.absBound a.coeffs 1 : ℝ) * (b.error : ℝ)) :=
        mul_le_mul_of_nonneg_left
          (mul_le_mul_of_nonneg_left hbAt haAbs0) hdAbs0
      _ = (RoundedRatPoly.absBound d.coeffs 1 : ℝ) *
          (RoundedRatPoly.absBound a.coeffs 1 : ℝ) * b.error := by ring
  change
    |fd x * (fa x * fb x) -
        RoundedRatPoly.evalReal
          (DenseRatPoly.mul d.coeffs
            (DenseRatPoly.mul a.coeffs b.coeffs)) x| ≤
      (tripleFactorError d a b : ℝ)
  rw [RoundedRatPoly.evalReal_mul, RoundedRatPoly.evalReal_mul]
  rw [show
      fd x * (fa x * fb x) -
          RoundedRatPoly.evalReal d.coeffs x *
            (RoundedRatPoly.evalReal a.coeffs x *
              RoundedRatPoly.evalReal b.coeffs x) =
        (fd x - RoundedRatPoly.evalReal d.coeffs x) *
            (fa x * fb x) +
          RoundedRatPoly.evalReal d.coeffs x *
            ((fa x - RoundedRatPoly.evalReal a.coeffs x) * fb x) +
          RoundedRatPoly.evalReal d.coeffs x *
            (RoundedRatPoly.evalReal a.coeffs x *
              (fb x - RoundedRatPoly.evalReal b.coeffs x)) by ring]
  calc
    |(fd x - RoundedRatPoly.evalReal d.coeffs x) * (fa x * fb x) +
        RoundedRatPoly.evalReal d.coeffs x *
          ((fa x - RoundedRatPoly.evalReal a.coeffs x) * fb x) +
        RoundedRatPoly.evalReal d.coeffs x *
          (RoundedRatPoly.evalReal a.coeffs x *
            (fb x - RoundedRatPoly.evalReal b.coeffs x))| ≤
      |(fd x - RoundedRatPoly.evalReal d.coeffs x) * (fa x * fb x)| +
        |RoundedRatPoly.evalReal d.coeffs x *
          ((fa x - RoundedRatPoly.evalReal a.coeffs x) * fb x)| +
        |RoundedRatPoly.evalReal d.coeffs x *
          (RoundedRatPoly.evalReal a.coeffs x *
            (fb x - RoundedRatPoly.evalReal b.coeffs x))| := by
      exact (abs_add_le _ _).trans
        (add_le_add (abs_add_le _ _) le_rfl)
    _ ≤ (d.error : ℝ) *
          (RoundedRatPoly.absBound a.coeffs 1 + a.error : ℚ) *
          (RoundedRatPoly.absBound b.coeffs 1 + b.error : ℚ) +
        (RoundedRatPoly.absBound d.coeffs 1 : ℝ) * a.error *
          (RoundedRatPoly.absBound b.coeffs 1 + b.error : ℚ) +
        (RoundedRatPoly.absBound d.coeffs 1 : ℝ) *
          (RoundedRatPoly.absBound a.coeffs 1 : ℝ) * b.error :=
      add_le_add (add_le_add hterm1 hterm2) hterm3
    _ = (tripleFactorError d a b : ℝ) := by
      simp [tripleFactorError]

/-- Semantic enclosure for the cache-built normalized integrand. -/
theorem entryApprox_encloses_exactNormalized
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal
        (exactNormalizedIntegrand kind i j k))
      (entryApprox (buildPanelCache k) kind i j) := by
  have hPair := RoundedRatPoly.mul_encloses gridCells
    (h := (1 : ℚ)) (by norm_num)
    (normalizedComponentApprox kind j k)
    (normalizedComponentApprox kind i k)
    (normalizedComponentApprox_encloses kind j k)
    (normalizedComponentApprox_encloses kind i k)
  have hTriple := RoundedRatPoly.mul_encloses gridCells
    (h := (1 : ℚ)) (by norm_num)
    (normalizedDefectApprox k)
    (RoundedRatPoly.mul gridCells 1
      (normalizedComponentApprox kind j k)
      (normalizedComponentApprox kind i k))
    (normalizedDefectApprox_encloses k) hPair
  intro x hx
  rw [evalReal_exactNormalizedIntegrand_eq_factors]
  simpa [entryApprox] using hTriple x hx

/-- Semantic enclosure in the exact form consumed by the centered-integral
bridge. -/
theorem entryApprox_encloses_canonicalAffine
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal
        (DenseRatPoly.affine
          (DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial
            kind i j (p2PanelCenterQ k.val) 32)
          0 (p2PanelHalfWidthQ k.val)))
      (entryApprox (buildPanelCache k) kind i j) := by
  exact entryApprox_encloses_exactNormalized kind i j k

theorem entryApprox_eq_of_correct
    {cache : PanelCache} {k : Fin 32} (hcache : cache.CorrectFor k)
    (kind : P2SelectedKind) (i j : Fin 24) :
    entryApprox cache kind i j =
      entryApprox (buildPanelCache k) kind i j := by
  simp [entryApprox, hcache.defect_eq,
    PanelCache.component_eq_of_correct hcache]

/-- Semantic enclosure obtained from split factor-checkpoint equalities. -/
theorem entryApprox_encloses_canonicalAffine_of_correct
    {cache : PanelCache} {k : Fin 32} (hcache : cache.CorrectFor k)
    (kind : P2SelectedKind) (i j : Fin 24) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal
        (DenseRatPoly.affine
          (DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial
            kind i j (p2PanelCenterQ k.val) 32)
          0 (p2PanelHalfWidthQ k.val)))
      (entryApprox cache kind i j) := by
  rw [entryApprox_eq_of_correct hcache]
  exact entryApprox_encloses_canonicalAffine kind i j k

/-- Product semantics from a cache whose factors were certified directly by
enclosures, with no equality to a monolithic computed defect. -/
theorem entryApprox_encloses_canonicalAffine_of_enclosesCanonical
    {cache : PanelCache} {k : Fin 32}
    (hcache : cache.EnclosesCanonical k)
    (kind : P2SelectedKind) (i j : Fin 24) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal
        (exactNormalizedIntegrand kind i j k))
      (entryApprox cache kind i j) := by
  have hPair := RoundedRatPoly.mul_encloses gridCells
    (h := (1 : ℚ)) (by norm_num)
    (cache.component kind j) (cache.component kind i)
    (hcache.component_encloses kind j)
    (hcache.component_encloses kind i)
  have hTriple := RoundedRatPoly.mul_encloses gridCells
    (h := (1 : ℚ)) (by norm_num)
    cache.defect
    (RoundedRatPoly.mul gridCells 1
      (cache.component kind j) (cache.component kind i))
    hcache.defect_encloses hPair
  intro t ht
  rw [evalReal_exactNormalizedIntegrand_eq_canonicalFactors]
  simpa [entryApprox] using hTriple t ht

/-- A staged literal product inherits the exact normalized-integrand
semantics of its certified factor cache.  The equalities in `hproduct` are
purely finite checks; the approximation error is justified by the ordinary
enclosure theorems used in `hcache`. -/
theorem EntryProductCertificate.encloses_of_enclosesCanonical
    {cache : PanelCache} {kind : P2SelectedKind} {i j : Fin 24}
    {literal : Approx}
    (hproduct : EntryProductCertificate cache kind i j literal)
    {k : Fin 32} (hcache : cache.EnclosesCanonical k) :
    RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedIntegrand kind i j k))
      literal := by
  rw [hproduct.entry_eq, hproduct.pair_eq]
  simpa [entryApproxFromPair, componentPairApprox, entryApprox] using
    entryApprox_encloses_canonicalAffine_of_enclosesCanonical
      hcache kind i j

/-- An exact rational center-radius pair. -/
structure QBall where
  center : ℚ
  radius : ℚ
  deriving Repr, DecidableEq

namespace QBall

def zero : QBall := ⟨0, 0⟩

def add (a b : QBall) : QBall :=
  ⟨a.center + b.center, a.radius + b.radius⟩

def sum : List QBall → QBall
  | [] => zero
  | a :: as => add (sum as) a

def finSum {N : ℕ} (balls : Fin N → QBall) : QBall :=
  ⟨∑ k, (balls k).center, ∑ k, (balls k).radius⟩

/-- `fine.Refines coarse` means every real or rational value enclosed by
`fine` is also enclosed by `coarse`.  This is the small closed predicate used
for generated checkpoint balls. -/
def Refines (fine coarse : QBall) : Prop :=
  |fine.center - coarse.center| + fine.radius ≤ coarse.radius

@[simp] theorem zero_center : zero.center = 0 := rfl
@[simp] theorem zero_radius : zero.radius = 0 := rfl
@[simp] theorem add_center (a b : QBall) :
    (add a b).center = a.center + b.center := rfl
@[simp] theorem add_radius (a b : QBall) :
    (add a b).radius = a.radius + b.radius := rfl

@[simp] theorem sum_nil : (sum []).center = 0 := rfl

theorem sum_center (balls : List QBall) :
    (sum balls).center = (balls.map QBall.center).sum := by
  induction balls with
  | nil => rfl
  | cons a balls ih =>
      simp [sum, ih, add_comm]

theorem sum_radius (balls : List QBall) :
    (sum balls).radius = (balls.map QBall.radius).sum := by
  induction balls with
  | nil => rfl
  | cons a balls ih =>
      simp [sum, ih, add_comm]

@[simp] theorem finSum_center {N : ℕ} (balls : Fin N → QBall) :
    (finSum balls).center = ∑ k, (balls k).center := rfl

@[simp] theorem finSum_radius {N : ℕ} (balls : Fin N → QBall) :
    (finSum balls).radius = ∑ k, (balls k).radius := rfl

theorem abs_sum_sub_finSum_center_le
    {N : ℕ} (x : Fin N → ℚ) (balls : Fin N → QBall)
    (hencl : ∀ k, |x k - (balls k).center| ≤ (balls k).radius) :
    |∑ k, x k - (finSum balls).center| ≤ (finSum balls).radius := by
  rw [finSum_center, finSum_radius, ← Finset.sum_sub_distrib]
  calc
    |∑ k, (x k - (balls k).center)| ≤
        ∑ k, |x k - (balls k).center| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ k, (balls k).radius := by
      exact Finset.sum_le_sum fun k _ => hencl k

theorem abs_sub_center_le_of_refines
    {x : ℚ} {fine coarse : QBall}
    (hx : |x - fine.center| ≤ fine.radius)
    (href : fine.Refines coarse) :
    |x - coarse.center| ≤ coarse.radius := by
  calc
    |x - coarse.center| =
        |(x - fine.center) + (fine.center - coarse.center)| := by
      ring_nf
    _ ≤ |x - fine.center| + |fine.center - coarse.center| :=
      abs_add_le _ _
    _ ≤ fine.radius + |fine.center - coarse.center| :=
      add_le_add hx le_rfl
    _ = |fine.center - coarse.center| + fine.radius := add_comm _ _
    _ ≤ coarse.radius := href

theorem refines_refl (ball : QBall) : ball.Refines ball := by
  simp [Refines]

theorem refines_trans {a b c : QBall}
    (hab : a.Refines b) (hbc : b.Refines c) : a.Refines c := by
  unfold Refines at hab hbc ⊢
  calc
    |a.center - c.center| + a.radius ≤
        (|a.center - b.center| + |b.center - c.center|) + a.radius := by
      gcongr
      rw [show a.center - c.center =
          (a.center - b.center) + (b.center - c.center) by ring]
      exact abs_add_le _ _
    _ = (|a.center - b.center| + a.radius) +
          |b.center - c.center| := by ring
    _ ≤ b.radius + |b.center - c.center| := by gcongr
    _ = |b.center - c.center| + b.radius := add_comm _ _
    _ ≤ c.radius := hbc

theorem add_refines_add {a₁ a₂ b₁ b₂ : QBall}
    (h₁ : a₁.Refines b₁) (h₂ : a₂.Refines b₂) :
    (add a₁ a₂).Refines (add b₁ b₂) := by
  unfold Refines at h₁ h₂ ⊢
  simp only [add_center, add_radius]
  rw [show
    a₁.center + a₂.center - (b₁.center + b₂.center) =
      (a₁.center - b₁.center) +
        (a₂.center - b₂.center) by ring]
  calc
    |(a₁.center - b₁.center) +
        (a₂.center - b₂.center)| +
          (a₁.radius + a₂.radius) ≤
        (|a₁.center - b₁.center| +
          |a₂.center - b₂.center|) +
            (a₁.radius + a₂.radius) := by
      gcongr
      exact abs_add_le _ _
    _ = (|a₁.center - b₁.center| + a₁.radius) +
        (|a₂.center - b₂.center| + a₂.radius) := by ring
    _ ≤ b₁.radius + b₂.radius := add_le_add h₁ h₂

theorem sum_refines_sum
    {fine coarse : List QBall}
    (hlength : fine.length = coarse.length)
    (href : ∀ n (hn : n < fine.length),
      (fine.get ⟨n, hn⟩).Refines
        (coarse.get ⟨n, by simpa [hlength] using hn⟩)) :
    (sum fine).Refines (sum coarse) := by
  induction fine generalizing coarse with
  | nil =>
      have hc : coarse = [] := List.eq_nil_of_length_eq_zero (by simpa using hlength.symm)
      subst hc
      exact refines_refl _
  | cons a fine ih =>
      cases coarse with
      | nil => simp at hlength
      | cons b coarse =>
          simp only [List.length_cons, Nat.succ.injEq] at hlength
          apply add_refines_add
          · apply ih hlength
            intro n hn
            simpa using href (n + 1) (Nat.succ_lt_succ hn)
          · simpa using href 0 (by simp)

end QBall

/-- Original-coordinate integral ball obtained from an arbitrary normalized
rounded approximation.  This is the checkpoint boundary for generated
literal entry polynomials. -/
def entryBallFromApprox (k : Fin 32) (approx : Approx) : QBall :=
  let halfWidth := p2PanelHalfWidthQ k.val
  ⟨halfWidth * DenseRatPoly.exactIntegral approx.coeffs (-1) 1,
    2 * halfWidth * approx.error⟩

/-- Integral ball for three certified factors using exact coefficient
convolution and the direct sup-error ledger. -/
def tripleFactorIntegralBall
    (halfWidth : ℚ) (d a b : Approx) : QBall :=
  ⟨halfWidth * DenseRatPoly.exactIntegral
      (DenseRatPoly.mul d.coeffs
        (DenseRatPoly.mul a.coeffs b.coeffs)) (-1) 1,
    2 * halfWidth * tripleFactorError d a b⟩

/-- Generic exact-integral theorem for three semantically certified factors.
The center contains one exact dense convolution, but there are no rounded
intermediate products and no multiplication-rounding errors. -/
theorem abs_scaledExactIntegral_sub_tripleFactorIntegralBallCenter_le
    {exact : DenseRatPoly.Poly} {fd fa fb : ℝ → ℝ}
    (d a b : Approx)
    (hexact : ∀ x, RoundedRatPoly.evalReal exact x =
      fd x * (fa x * fb x))
    (hd : RoundedRatPoly.Encloses 1 fd d)
    (ha : RoundedRatPoly.Encloses 1 fa a)
    (hb : RoundedRatPoly.Encloses 1 fb b)
    (halfWidth : ℚ) (hhalfWidth : 0 ≤ halfWidth) :
    |halfWidth * DenseRatPoly.exactIntegral exact (-1) 1 -
        (tripleFactorIntegralBall halfWidth d a b).center| ≤
      (tripleFactorIntegralBall halfWidth d a b).radius := by
  have hproduct := unroundedTripleProductApprox_encloses d a b hd ha hb
  have hencl : RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal exact)
      (unroundedTripleProductApprox d a b) := by
    intro x hx
    rw [hexact x]
    exact hproduct x hx
  have h := abs_scaledExactIntegral_sub_approxCenter_le
    hencl halfWidth hhalfWidth
  simpa [tripleFactorIntegralBall,
    unroundedTripleProductApprox] using h

/-- The ordinary analytic enclosure theorem for an arbitrary literal entry
approximation.  No numerical generator is trusted: `happrox` must prove in
Lean that the stored polynomial and error enclose the exact normalized
canonical integrand. -/
theorem abs_p2PanelIntegralQ_sub_entryBallFromApproxCenter_le
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32)
    (approx : Approx)
    (happrox : RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal
        (exactNormalizedIntegrand kind i j k)) approx) :
    |DenseRatPoly.p2PanelIntegralQ kind i j k.val -
        (entryBallFromApprox k approx).center| ≤
      (entryBallFromApprox k approx).radius := by
  have h := abs_centeredExactIntegral_sub_approxCenter_le
    (exact := DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial
      kind i j (p2PanelCenterQ k.val) 32)
    (approx := approx)
    (p2PanelHalfWidthQ k.val) (p2PanelHalfWidthQ_nonneg k)
    (by simpa [exactNormalizedIntegrand] using happrox)
  simpa [DenseRatPoly.p2PanelIntegralQ,
    DenseRatPoly.p2ScaleCenteredPanelIntegralQ,
    entryBallFromApprox] using h

/-- Direct triple-factor ball for one canonical cache entry. -/
def tripleFactorEntryBall
    (k : Fin 32) (cache : PanelCache)
    (kind : P2SelectedKind) (i j : Fin 24) : QBall :=
  tripleFactorIntegralBall (p2PanelHalfWidthQ k.val)
    cache.defect (cache.component kind j) (cache.component kind i)

/-- A semantically certified factor cache encloses the canonical panel
integral using the direct, unrounded triple-product ledger. -/
theorem abs_p2PanelIntegralQ_sub_tripleFactorEntryBallCenter_le
    {cache : PanelCache} {k : Fin 32}
    (hcache : cache.EnclosesCanonical k)
    (kind : P2SelectedKind) (i j : Fin 24) :
    |DenseRatPoly.p2PanelIntegralQ kind i j k.val -
        (tripleFactorEntryBall k cache kind i j).center| ≤
      (tripleFactorEntryBall k cache kind i j).radius := by
  have hproduct := unroundedTripleProductApprox_encloses
    cache.defect (cache.component kind j) (cache.component kind i)
    hcache.defect_encloses
    (hcache.component_encloses kind j)
    (hcache.component_encloses kind i)
  have happrox : RoundedRatPoly.Encloses 1
      (RoundedRatPoly.evalReal (exactNormalizedIntegrand kind i j k))
      (unroundedTripleProductApprox cache.defect
        (cache.component kind j) (cache.component kind i)) := by
    intro x hx
    rw [evalReal_exactNormalizedIntegrand_eq_canonicalFactors]
    exact hproduct x hx
  have h := abs_p2PanelIntegralQ_sub_entryBallFromApproxCenter_le
    kind i j k
    (unroundedTripleProductApprox cache.defect
      (cache.component kind j) (cache.component kind i)) happrox
  simpa [tripleFactorEntryBall, tripleFactorIntegralBall,
    entryBallFromApprox, unroundedTripleProductApprox] using h

/-- Original-coordinate integral ball obtained from one cached normalized
integrand. -/
def entryBall
    (k : Fin 32) (cache : PanelCache)
    (kind : P2SelectedKind) (i j : Fin 24) : QBall :=
  let approx := entryApprox cache kind i j
  let halfWidth := p2PanelHalfWidthQ k.val
  ⟨halfWidth * DenseRatPoly.exactIntegral approx.coeffs (-1) 1,
    2 * halfWidth * approx.error⟩

@[simp] theorem entryBall_eq_entryBallFromApprox
    (k : Fin 32) (cache : PanelCache)
    (kind : P2SelectedKind) (i j : Fin 24) :
    entryBall k cache kind i j =
      entryBallFromApprox k (entryApprox cache kind i j) := rfl

/-- Integral semantics specialized to a staged literal product
certificate. -/
theorem abs_p2PanelIntegralQ_sub_entryBallFromApproxCenter_le_of_product
    {cache : PanelCache} {k : Fin 32}
    (hcache : cache.EnclosesCanonical k)
    (kind : P2SelectedKind) (i j : Fin 24) (literal : Approx)
    (hproduct : EntryProductCertificate cache kind i j literal) :
    |DenseRatPoly.p2PanelIntegralQ kind i j k.val -
        (entryBallFromApprox k literal).center| ≤
      (entryBallFromApprox k literal).radius := by
  exact abs_p2PanelIntegralQ_sub_entryBallFromApproxCenter_le
    kind i j k literal
    (hproduct.encloses_of_enclosesCanonical hcache)

/-- Transport a staged literal-entry ball through a small generated coarse
ball refinement predicate. -/
theorem abs_p2PanelIntegralQ_sub_coarseCenter_le_of_product
    {cache : PanelCache} {k : Fin 32}
    (hcache : cache.EnclosesCanonical k)
    (kind : P2SelectedKind) (i j : Fin 24) (literal : Approx)
    (hproduct : EntryProductCertificate cache kind i j literal)
    (coarse : QBall)
    (hrefines : (entryBallFromApprox k literal).Refines coarse) :
    |DenseRatPoly.p2PanelIntegralQ kind i j k.val - coarse.center| ≤
      coarse.radius := by
  exact QBall.abs_sub_center_le_of_refines
    (abs_p2PanelIntegralQ_sub_entryBallFromApproxCenter_le_of_product
      hcache kind i j literal hproduct)
    hrefines

/-- One cache-built ball encloses the canonical exact rational panel
integral. -/
theorem abs_p2PanelIntegralQ_sub_entryBallCenter_le
    (kind : P2SelectedKind) (i j : Fin 24) (k : Fin 32) :
    |DenseRatPoly.p2PanelIntegralQ kind i j k.val -
        (entryBall k (buildPanelCache k) kind i j).center| ≤
      (entryBall k (buildPanelCache k) kind i j).radius := by
  have h := abs_centeredExactIntegral_sub_approxCenter_le
    (exact := DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial
      kind i j (p2PanelCenterQ k.val) 32)
    (approx := entryApprox (buildPanelCache k) kind i j)
    (p2PanelHalfWidthQ k.val) (p2PanelHalfWidthQ_nonneg k)
    (entryApprox_encloses_canonicalAffine kind i j k)
  simpa [DenseRatPoly.p2PanelIntegralQ,
    DenseRatPoly.p2ScaleCenteredPanelIntegralQ, entryBall] using h

/-- Integral semantics for an explicit cache whose 49 factors have been
checkpointed against the canonical rounded evaluator. -/
theorem abs_p2PanelIntegralQ_sub_entryBallCenter_le_of_correct
    {cache : PanelCache} {k : Fin 32} (hcache : cache.CorrectFor k)
    (kind : P2SelectedKind) (i j : Fin 24) :
    |DenseRatPoly.p2PanelIntegralQ kind i j k.val -
        (entryBall k cache kind i j).center| ≤
      (entryBall k cache kind i j).radius := by
  have h := abs_centeredExactIntegral_sub_approxCenter_le
    (exact := DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial
      kind i j (p2PanelCenterQ k.val) 32)
    (approx := entryApprox cache kind i j)
    (p2PanelHalfWidthQ k.val) (p2PanelHalfWidthQ_nonneg k)
    (entryApprox_encloses_canonicalAffine_of_correct hcache kind i j)
  simpa [DenseRatPoly.p2PanelIntegralQ,
    DenseRatPoly.p2ScaleCenteredPanelIntegralQ, entryBall] using h

theorem abs_p2PanelIntegralQ_sub_entryBallCenter_le_of_enclosesCanonical
    {cache : PanelCache} {k : Fin 32}
    (hcache : cache.EnclosesCanonical k)
    (kind : P2SelectedKind) (i j : Fin 24) :
    |DenseRatPoly.p2PanelIntegralQ kind i j k.val -
        (entryBall k cache kind i j).center| ≤
      (entryBall k cache kind i j).radius := by
  have h := abs_centeredExactIntegral_sub_approxCenter_le
    (exact := DenseRatPoly.p2ScaleCenteredPanelIntegrandPolynomial
      kind i j (p2PanelCenterQ k.val) 32)
    (approx := entryApprox cache kind i j)
    (p2PanelHalfWidthQ k.val) (p2PanelHalfWidthQ_nonneg k)
    (entryApprox_encloses_canonicalAffine_of_enclosesCanonical
      hcache kind i j)
  simpa [DenseRatPoly.p2PanelIntegralQ,
    DenseRatPoly.p2ScaleCenteredPanelIntegralQ, entryBall] using h

/-- Upper-triangular entry attached to an eager vector row. -/
def generatedEntryAt (r : Fin 600) : P2EntryIndex :=
  (p2UpperEntryAt r).val

/-- All 600 entry balls from an already materialized panel cache. -/
def panelBallsFromCache
    (k : Fin 32) (cache : PanelCache) : Vector QBall 600 :=
  Vector.ofFn fun r =>
    let e := generatedEntryAt r
    entryBall k cache (p2EntrySelectedKind e.block) e.row e.col

/-- All 600 entry balls for one panel, using one syntactic cache binding. -/
def panelBalls (k : Fin 32) : Vector QBall 600 :=
  panelBallsFromCache k (buildPanelCache k)

def addBallVectors
    (a b : Vector QBall 600) : Vector QBall 600 :=
  Vector.ofFn fun r => QBall.add (a.get r) (b.get r)

/-- Add one panel to a running eager vector and then discard its cache. -/
def addPanelToBalls
    (sums : Vector QBall 600) (k : Fin 32) : Vector QBall 600 :=
  let cache := buildPanelCache k
  Vector.ofFn fun r =>
    let e := generatedEntryAt r
    QBall.add (sums.get r)
      (entryBall k cache (p2EntrySelectedKind e.block) e.row e.col)

/-- Streaming aggregate over an explicitly supplied panel list. -/
def aggregatePanelBalls : List (Fin 32) → Vector QBall 600
  | [] => Vector.replicate 600 QBall.zero
  | k :: ks => addPanelToBalls (aggregatePanelBalls ks) k

def allEntryBalls : Vector QBall 600 :=
  aggregatePanelBalls (List.finRange 32)

/-- Direct single-entry forms are convenient for semantic transfer and for
kernel checks that intentionally avoid normalizing the entire eager vector. -/
def panelEntryBall (e : P2EntryIndex) (k : Fin 32) : QBall :=
  entryBall k (buildPanelCache k)
    (p2EntrySelectedKind e.block) e.row e.col

def entryCenterQ (e : P2EntryIndex) : ℚ :=
  ∑ k : Fin 32, (panelEntryBall e k).center

def entryRadiusQ (e : P2EntryIndex) : ℚ :=
  ∑ k : Fin 32, (panelEntryBall e k).radius

def generatedEntryCenterQ (r : Fin 600) : ℚ :=
  (allEntryBalls.get r).center

def generatedEntryRadiusQ (r : Fin 600) : ℚ :=
  (allEntryBalls.get r).radius

@[simp] theorem panelBalls_get (k : Fin 32) (r : Fin 600) :
    (panelBalls k).get r = panelEntryBall (generatedEntryAt r) k := by
  simp [panelBalls, panelBallsFromCache, panelEntryBall,
    generatedEntryAt]

@[simp] theorem panelBallsFromCache_get
    (k : Fin 32) (cache : PanelCache) (r : Fin 600) :
    (panelBallsFromCache k cache).get r =
      entryBall k cache
        (p2EntrySelectedKind (generatedEntryAt r).block)
        (generatedEntryAt r).row (generatedEntryAt r).col := by
  simp [panelBallsFromCache, generatedEntryAt]

theorem abs_p2PanelIntegralQ_sub_panelBallsFromCacheCenter_le_of_correct
    {k : Fin 32} {cache : PanelCache} (hcache : cache.CorrectFor k)
    (r : Fin 600) :
    |DenseRatPoly.p2PanelIntegralQ
          (p2EntrySelectedKind (generatedEntryAt r).block)
          (generatedEntryAt r).row (generatedEntryAt r).col k.val -
        ((panelBallsFromCache k cache).get r).center| ≤
      ((panelBallsFromCache k cache).get r).radius := by
  rw [panelBallsFromCache_get]
  exact abs_p2PanelIntegralQ_sub_entryBallCenter_le_of_correct hcache
    (p2EntrySelectedKind (generatedEntryAt r).block)
    (generatedEntryAt r).row (generatedEntryAt r).col

theorem
    abs_p2PanelIntegralQ_sub_panelBallsFromCacheCenter_le_of_enclosesCanonical
    {k : Fin 32} {cache : PanelCache}
    (hcache : cache.EnclosesCanonical k) (r : Fin 600) :
    |DenseRatPoly.p2PanelIntegralQ
          (p2EntrySelectedKind (generatedEntryAt r).block)
          (generatedEntryAt r).row (generatedEntryAt r).col k.val -
        ((panelBallsFromCache k cache).get r).center| ≤
      ((panelBallsFromCache k cache).get r).radius := by
  rw [panelBallsFromCache_get]
  exact
    abs_p2PanelIntegralQ_sub_entryBallCenter_le_of_enclosesCanonical
      hcache (p2EntrySelectedKind (generatedEntryAt r).block)
      (generatedEntryAt r).row (generatedEntryAt r).col

/-- Transport a canonical panel enclosure through a generated coarse-ball
checkpoint. -/
theorem abs_p2PanelIntegralQ_sub_coarseCenter_le
    {k : Fin 32} {cache : PanelCache} (hcache : cache.CorrectFor k)
    (r : Fin 600) (coarse : QBall)
    (hrefines :
      ((panelBallsFromCache k cache).get r).Refines coarse) :
    |DenseRatPoly.p2PanelIntegralQ
          (p2EntrySelectedKind (generatedEntryAt r).block)
          (generatedEntryAt r).row (generatedEntryAt r).col k.val -
        coarse.center| ≤ coarse.radius := by
  exact QBall.abs_sub_center_le_of_refines
    (abs_p2PanelIntegralQ_sub_panelBallsFromCacheCenter_le_of_correct
      hcache r)
    hrefines

theorem abs_p2PanelIntegralQ_sub_coarseCenter_le_of_enclosesCanonical
    {k : Fin 32} {cache : PanelCache}
    (hcache : cache.EnclosesCanonical k)
    (r : Fin 600) (coarse : QBall)
    (hrefines :
      ((panelBallsFromCache k cache).get r).Refines coarse) :
    |DenseRatPoly.p2PanelIntegralQ
          (p2EntrySelectedKind (generatedEntryAt r).block)
          (generatedEntryAt r).row (generatedEntryAt r).col k.val -
        coarse.center| ≤ coarse.radius := by
  exact QBall.abs_sub_center_le_of_refines
    (abs_p2PanelIntegralQ_sub_panelBallsFromCacheCenter_le_of_enclosesCanonical
      hcache r)
    hrefines

/-- Sum 32 generated coarse panel balls after their factor checkpoints and
refinement predicates have been proved independently. -/
theorem abs_p2EntryPanelSumQ_sub_coarseFinSumCenter_le
    (r : Fin 600) (cache : Fin 32 → PanelCache)
    (coarse : Fin 32 → QBall)
    (hcache : ∀ k, (cache k).CorrectFor k)
    (hrefines : ∀ k,
      ((panelBallsFromCache k (cache k)).get r).Refines (coarse k)) :
    |DenseRatPoly.p2EntryPanelSumQ (generatedEntryAt r) -
        (QBall.finSum coarse).center| ≤
      (QBall.finSum coarse).radius := by
  unfold DenseRatPoly.p2EntryPanelSumQ
  rw [← Fin.sum_univ_eq_sum_range]
  apply QBall.abs_sum_sub_finSum_center_le
  intro k
  exact abs_p2PanelIntegralQ_sub_coarseCenter_le
    (hcache k) r (coarse k) (hrefines k)

theorem
    abs_p2EntryPanelSumQ_sub_coarseFinSumCenter_le_of_enclosesCanonical
    (r : Fin 600) (cache : Fin 32 → PanelCache)
    (coarse : Fin 32 → QBall)
    (hcache : ∀ k, (cache k).EnclosesCanonical k)
    (hrefines : ∀ k,
      ((panelBallsFromCache k (cache k)).get r).Refines (coarse k)) :
    |DenseRatPoly.p2EntryPanelSumQ (generatedEntryAt r) -
        (QBall.finSum coarse).center| ≤
      (QBall.finSum coarse).radius := by
  unfold DenseRatPoly.p2EntryPanelSumQ
  rw [← Fin.sum_univ_eq_sum_range]
  apply QBall.abs_sum_sub_finSum_center_le
  intro k
  exact abs_p2PanelIntegralQ_sub_coarseCenter_le_of_enclosesCanonical
    (hcache k) r (coarse k) (hrefines k)

/-- Per-panel eager-vector form, allowing certificate checks to split before
the 32-panel aggregate if kernel normalization of the latter is too large. -/
theorem abs_p2PanelIntegralQ_sub_panelBallsCenter_le
    (k : Fin 32) (r : Fin 600) :
    |DenseRatPoly.p2PanelIntegralQ
          (p2EntrySelectedKind (generatedEntryAt r).block)
          (generatedEntryAt r).row (generatedEntryAt r).col k.val -
        ((panelBalls k).get r).center| ≤
      ((panelBalls k).get r).radius := by
  rw [panelBalls_get]
  simpa [panelEntryBall] using
    abs_p2PanelIntegralQ_sub_entryBallCenter_le
      (p2EntrySelectedKind (generatedEntryAt r).block)
      (generatedEntryAt r).row (generatedEntryAt r).col k

@[simp] theorem addBallVectors_get
    (a b : Vector QBall 600) (r : Fin 600) :
    (addBallVectors a b).get r = QBall.add (a.get r) (b.get r) := by
  simp [addBallVectors]

@[simp] theorem addPanelToBalls_get
    (sums : Vector QBall 600) (k : Fin 32) (r : Fin 600) :
    (addPanelToBalls sums k).get r =
      QBall.add (sums.get r) (panelEntryBall (generatedEntryAt r) k) := by
  simp [addPanelToBalls, panelEntryBall, generatedEntryAt]

/-- Entrywise semantics of the streaming vector fold. -/
theorem aggregatePanelBalls_get
    (ks : List (Fin 32)) (r : Fin 600) :
    (aggregatePanelBalls ks).get r =
      QBall.sum (ks.map (panelEntryBall (generatedEntryAt r))) := by
  induction ks with
  | nil =>
      simp [aggregatePanelBalls, QBall.sum]
  | cons k ks ih =>
      simp [aggregatePanelBalls, ih, QBall.sum]

theorem allEntryBalls_get_center (r : Fin 600) :
    (allEntryBalls.get r).center =
      entryCenterQ (generatedEntryAt r) := by
  rw [allEntryBalls, aggregatePanelBalls_get, QBall.sum_center]
  simp only [List.map_map, entryCenterQ]
  exact (Fin.sum_univ_def
    (fun k : Fin 32 => (panelEntryBall (generatedEntryAt r) k).center)).symm

theorem allEntryBalls_get_radius (r : Fin 600) :
    (allEntryBalls.get r).radius =
      entryRadiusQ (generatedEntryAt r) := by
  rw [allEntryBalls, aggregatePanelBalls_get, QBall.sum_radius]
  simp only [List.map_map, entryRadiusQ]
  exact (Fin.sum_univ_def
    (fun k : Fin 32 => (panelEntryBall (generatedEntryAt r) k).radius)).symm

@[simp] theorem generatedEntryCenterQ_eq (r : Fin 600) :
    generatedEntryCenterQ r = entryCenterQ (generatedEntryAt r) :=
  allEntryBalls_get_center r

@[simp] theorem generatedEntryRadiusQ_eq (r : Fin 600) :
    generatedEntryRadiusQ r = entryRadiusQ (generatedEntryAt r) :=
  allEntryBalls_get_radius r

/-- The direct cache-based 32-panel aggregate encloses the independently
defined exact canonical rational panel sum. -/
theorem abs_p2EntryPanelSumQ_sub_entryCenterQ_le (e : P2EntryIndex) :
    |DenseRatPoly.p2EntryPanelSumQ e - entryCenterQ e| ≤
      entryRadiusQ e := by
  unfold DenseRatPoly.p2EntryPanelSumQ entryCenterQ entryRadiusQ
  rw [← Fin.sum_univ_eq_sum_range, ← Finset.sum_sub_distrib]
  calc
    |∑ k : Fin 32,
        (DenseRatPoly.p2PanelIntegralQ
          (p2EntrySelectedKind e.block) e.row e.col k.val -
          (panelEntryBall e k).center)| ≤
        ∑ k : Fin 32,
          |DenseRatPoly.p2PanelIntegralQ
            (p2EntrySelectedKind e.block) e.row e.col k.val -
            (panelEntryBall e k).center| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ k : Fin 32, (panelEntryBall e k).radius := by
      apply Finset.sum_le_sum
      intro k hk
      simpa [panelEntryBall] using
        abs_p2PanelIntegralQ_sub_entryBallCenter_le
          (p2EntrySelectedKind e.block) e.row e.col k

/-- Eager-vector form consumed by generated upper-entry certificates. -/
theorem abs_p2EntryPanelSumQ_sub_generatedEntryCenterQ_le (r : Fin 600) :
    |DenseRatPoly.p2EntryPanelSumQ (generatedEntryAt r) -
        generatedEntryCenterQ r| ≤
      generatedEntryRadiusQ r := by
  rw [generatedEntryCenterQ_eq, generatedEntryRadiusQ_eq]
  exact abs_p2EntryPanelSumQ_sub_entryCenterQ_le (generatedEntryAt r)

theorem entryRadiusQ_nonneg (e : P2EntryIndex) : 0 ≤ entryRadiusQ e := by
  exact (abs_nonneg _).trans
    (abs_p2EntryPanelSumQ_sub_entryCenterQ_le e)

theorem generatedEntryRadiusQ_nonneg (r : Fin 600) :
    0 ≤ generatedEntryRadiusQ r := by
  rw [generatedEntryRadiusQ_eq]
  exact entryRadiusQ_nonneg (generatedEntryAt r)

end P2RoundedSharedEvaluator

end RHP2Bridge
