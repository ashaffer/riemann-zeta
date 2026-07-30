/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedSharedEvaluator

/-!
# Shared moment evaluator for rounded `p = 2` panel certificates

For one normalized panel, all matrix entries share the same rounded defect
polynomial `d`.  This file rewrites the exact integral of

`d * (a * b)`

as a Hankel bilinear form.  Its rows can be emitted and checked separately,
so generated certificates need not normalize a fresh three-factor dense
convolution for every matrix entry.

No approximation occurs in this identity.  Rounding errors remain governed
by `P2RoundedSharedEvaluator.tripleFactorError`; this module only provides an
executable center and a proof that it is the same exact rational integral.
-/

namespace RHP2Bridge

namespace P2RoundedTripleMoment

open scoped BigOperators

abbrev Poly := DenseRatPoly.Poly

/-- The exact integral of `x^n` over `[-1,1]`, retained in a form matching
the dense exact-integral definition. -/
def intervalMoment (n : ℕ) : ℚ :=
  ((1 : ℚ) ^ (n + 1) - (-1 : ℚ) ^ (n + 1)) /
    ((n : ℚ) + 1)

/-- Dot a dense polynomial with the moment sequence beginning at `shift`. -/
def momentDot : ℕ → Poly → ℚ
  | _, [] => 0
  | shift, c :: cs =>
      c * intervalMoment shift + momentDot (shift + 1) cs

theorem momentDot_add (shift : ℕ) (p q : Poly) :
    momentDot shift (DenseRatPoly.add p q) =
      momentDot shift p + momentDot shift q := by
  induction p generalizing q shift with
  | nil => simp [DenseRatPoly.add, momentDot]
  | cons a p ih =>
      cases q with
      | nil => simp [DenseRatPoly.add, momentDot]
      | cons b q =>
          simp only [DenseRatPoly.add, momentDot]
          rw [ih]
          ring

theorem momentDot_scale (shift : ℕ) (c : ℚ) (p : Poly) :
    momentDot shift (DenseRatPoly.scale c p) =
      c * momentDot shift p := by
  induction p generalizing shift with
  | nil => simp [DenseRatPoly.scale, momentDot]
  | cons a p ih =>
      simp only [DenseRatPoly.scale, List.map_cons, momentDot]
      have htail := ih (shift + 1)
      simp only [DenseRatPoly.scale] at htail
      rw [htail]
      ring

@[simp] theorem momentDot_xmul (shift : ℕ) (p : Poly) :
    momentDot shift (DenseRatPoly.xmul p) =
      momentDot (shift + 1) p := by
  simp [DenseRatPoly.xmul, momentDot]

/-- Finite-sum specification of `momentDot`.  The explicit `shift` is what
makes cons-induction track polynomial degrees correctly. -/
theorem momentDot_eq_sum (shift : ℕ) (p : Poly) :
    momentDot shift p =
      ∑ i : Fin p.length,
        p.get i * intervalMoment (shift + i.val) := by
  induction p generalizing shift with
  | nil => simp [momentDot]
  | cons c p ih =>
      simp only [momentDot, List.length_cons, Fin.sum_univ_succ,
        List.get_cons_zero, List.get_cons_succ', Fin.val_zero,
        Nat.add_zero]
      rw [ih]
      simp only [Fin.val_succ]
      congr 1
      apply Finset.sum_congr rfl
      intro i hi
      congr 2
      omega

/-- The executable dense integrator on `[-1,1]` is exactly a moment dot
product. -/
theorem exactIntegral_neg_one_one_eq_momentDot (p : Poly) :
    DenseRatPoly.exactIntegral p (-1) 1 = momentDot 0 p := by
  rw [momentDot_eq_sum]
  simp [DenseRatPoly.exactIntegral, RatPoly.exactIntegralCoeffs,
    intervalMoment]

/-- One row of the Hankel moment matrix for `d`, multiplied by `b`.

At row `shift` this is `Σ_j b_j Σ_r d_r μ_(shift+j+r)`. -/
def hankelMatVecAt (d : Poly) : Poly → ℕ → ℚ
  | [], _ => 0
  | c :: cs, shift =>
      c * momentDot shift d + hankelMatVecAt d cs (shift + 1)

/-- A finite prefix of the shared matvec.  Generated certificates can prove
its rows in independent checkpoint modules. -/
def hankelMatVec (d b : Poly) (rows : ℕ) : Vector ℚ rows :=
  Vector.ofFn fun i => hankelMatVecAt d b i.val

@[simp] theorem hankelMatVec_get
    (d b : Poly) (rows : ℕ) (i : Fin rows) :
    (hankelMatVec d b rows).get i = hankelMatVecAt d b i.val := by
  simp [hankelMatVec]

/-! ### Two-stage shared evaluation

The canonical rounded factors have at most 149 stored coefficients.  Thus
149 matvec rows need the 297 defect moments numbered `0` through `296`.
The following two vectors are explicit kernel-checkpoint boundaries.
-/

/-- A generated or computed moment vector has the intended mathematical
meaning.  This pointwise predicate permits one Lean proof per row. -/
def DefectMomentsCorrect
    (d : Poly) (moments : Vector ℚ 297) : Prop :=
  ∀ i : Fin 297, moments.get i = momentDot i.val d

/-- All defect moments needed by two degree-at-most-148 component factors. -/
def defectMoments (d : Poly) : Vector ℚ 297 :=
  Vector.ofFn fun i => momentDot i.val d

@[simp] theorem defectMoments_get (d : Poly) (i : Fin 297) :
    (defectMoments d).get i = momentDot i.val d := by
  simp [defectMoments]

theorem defectMoments_correct (d : Poly) :
    DefectMomentsCorrect d (defectMoments d) := by
  intro i
  exact defectMoments_get d i

/-- Total vector lookup used by the executable staged kernel.  Correctness
theorems below prove that the zero-padding branch is unreachable. -/
def vectorGetD {n : ℕ} (v : Vector ℚ n) (i : ℕ) : ℚ :=
  if h : i < n then v.get ⟨i, h⟩ else 0

@[simp] theorem vectorGetD_of_lt
    {n i : ℕ} (v : Vector ℚ n) (h : i < n) :
    vectorGetD v i = v.get ⟨i, h⟩ := by
  simp [vectorGetD, h]

/-- One component row evaluated from a supplied defect-moment checkpoint. -/
def hankelRowFromMoments
    (moments : Vector ℚ 297) : Poly → ℕ → ℚ
  | [], _ => 0
  | c :: cs, shift =>
      c * vectorGetD moments shift +
        hankelRowFromMoments moments cs (shift + 1)

/-- The 149 canonical Hankel matvec rows obtained from shared moments. -/
def hankelMatVecFromMoments
    (moments : Vector ℚ 297) (b : Poly) : Vector ℚ 149 :=
  Vector.ofFn fun i => hankelRowFromMoments moments b i.val

/-- A supplied matvec, of any length, agrees with the mathematical rows. -/
def HankelMatVecCorrect
    (d b : Poly) {rows : ℕ} (v : Vector ℚ rows) : Prop :=
  ∀ i : Fin rows, v.get i = hankelMatVecAt d b i.val

theorem hankelRowFromMoments_eq_hankelMatVecAt
    {d : Poly} {moments : Vector ℚ 297}
    (hmoments : DefectMomentsCorrect d moments)
    (b : Poly) (shift : ℕ) (hfit : shift + b.length ≤ 297) :
    hankelRowFromMoments moments b shift =
      hankelMatVecAt d b shift := by
  induction b generalizing shift with
  | nil => simp [hankelRowFromMoments, hankelMatVecAt]
  | cons c b ih =>
      simp only [List.length_cons] at hfit
      have hshift : shift < 297 := by omega
      simp only [hankelRowFromMoments, hankelMatVecAt]
      rw [vectorGetD_of_lt moments hshift]
      rw [hmoments ⟨shift, hshift⟩]
      rw [ih (shift + 1) (by omega)]

theorem hankelMatVecFromMoments_correct
    {d : Poly} {moments : Vector ℚ 297}
    (hmoments : DefectMomentsCorrect d moments)
    (b : Poly) (hlength : b.length ≤ 149) :
    HankelMatVecCorrect d b
      (hankelMatVecFromMoments moments b) := by
  intro i
  simp only [hankelMatVecFromMoments, Vector.get_ofFn]
  apply hankelRowFromMoments_eq_hankelMatVecAt hmoments
  omega

theorem hankelMatVecFromMoments_get_eq_hankelMatVec_get
    {d : Poly} {moments : Vector ℚ 297}
    (hmoments : DefectMomentsCorrect d moments)
    (b : Poly) (hlength : b.length ≤ 149) (i : Fin 149) :
    (hankelMatVecFromMoments moments b).get i =
      (hankelMatVec d b 149).get i := by
  rw [hankelMatVec_get]
  exact hankelMatVecFromMoments_correct hmoments b hlength i

theorem hankelMatVecFromDefectMoments_get_eq
    (d b : Poly) (hlength : b.length ≤ 149) (i : Fin 149) :
    (hankelMatVecFromMoments (defectMoments d) b).get i =
      (hankelMatVec d b 149).get i :=
  hankelMatVecFromMoments_get_eq_hankelMatVec_get
    (defectMoments_correct d) b hlength i

/-- Dot `a` against successive rows of the shared matvec. -/
def hankelBilinearAux (d b : Poly) : Poly → ℕ → ℚ
  | [], _ => 0
  | c :: cs, shift =>
      c * hankelMatVecAt d b shift +
        hankelBilinearAux d b cs (shift + 1)

/-- Executable shared-defect Hankel bilinear center. -/
def hankelBilinear (d a b : Poly) : ℚ :=
  hankelBilinearAux d b a 0

/-- Finite-sum specification of the recursive bilinear consumer. -/
theorem hankelBilinearAux_eq_sum
    (d b a : Poly) (shift : ℕ) :
    hankelBilinearAux d b a shift =
      ∑ i : Fin a.length,
        a.get i * hankelMatVecAt d b (shift + i.val) := by
  induction a generalizing shift with
  | nil => simp [hankelBilinearAux]
  | cons c a ih =>
      simp only [hankelBilinearAux, List.length_cons,
        Fin.sum_univ_succ, List.get_cons_zero,
        List.get_cons_succ', Fin.val_zero, Nat.add_zero]
      rw [ih]
      simp only [Fin.val_succ]
      congr 1
      apply Finset.sum_congr rfl
      intro i hi
      congr 2
      omega

theorem hankelBilinear_eq_sum (d a b : Poly) :
    hankelBilinear d a b =
      ∑ i : Fin a.length, a.get i * hankelMatVecAt d b i.val := by
  rw [hankelBilinear, hankelBilinearAux_eq_sum]
  simp

/-- Dot a polynomial against a supplied finite matvec.  `hrows` guarantees
that every coefficient has a row; the proof is erased by code generation. -/
def hankelDotFromVector {rows : ℕ}
    (a : Poly) (v : Vector ℚ rows) (hrows : a.length ≤ rows) : ℚ :=
  ∑ i : Fin a.length, a.get i * v.get (Fin.castLE hrows i)

/-- Any checkpointed correct matvec gives exactly the shared Hankel
bilinear value. -/
theorem hankelDotFromVector_eq_hankelBilinear
    {rows : ℕ} (d a b : Poly) (v : Vector ℚ rows)
    (hrows : a.length ≤ rows)
    (hv : HankelMatVecCorrect d b v) :
    hankelDotFromVector a v hrows = hankelBilinear d a b := by
  rw [hankelBilinear_eq_sum]
  unfold hankelDotFromVector
  apply Finset.sum_congr rfl
  intro i hi
  rw [hv (Fin.castLE hrows i)]
  rfl

/-- Convolution followed by a moment dot is the corresponding Hankel
matvec row. -/
theorem momentDot_mul (p q : Poly) (shift : ℕ) :
    momentDot shift (DenseRatPoly.mul p q) =
      hankelMatVecAt q p shift := by
  induction p generalizing shift with
  | nil =>
      simp [DenseRatPoly.mul, DenseRatPoly.zero, momentDot,
        hankelMatVecAt]
  | cons c p ih =>
      rw [DenseRatPoly.mul, momentDot_add, momentDot_scale,
        momentDot_xmul]
      simp only [hankelMatVecAt]
      rw [ih]

theorem hankelMatVecAt_mul (d b a : Poly) (shift : ℕ) :
    hankelMatVecAt (DenseRatPoly.mul b d) a shift =
      hankelBilinearAux d b a shift := by
  induction a generalizing shift with
  | nil => simp [hankelMatVecAt, hankelBilinearAux]
  | cons c a ih =>
      simp only [hankelMatVecAt, hankelBilinearAux]
      rw [momentDot_mul, ih]

theorem momentDot_triple_eq_hankelBilinear
    (d a b : Poly) :
    momentDot 0 (DenseRatPoly.mul a (DenseRatPoly.mul b d)) =
      hankelBilinear d a b := by
  rw [momentDot_mul, hankelMatVecAt_mul]
  rfl

/-- Main exact identity consumed by generated panel certificates. -/
theorem exactIntegral_triple_eq_hankelBilinear (d a b : Poly) :
    DenseRatPoly.exactIntegral
        (DenseRatPoly.mul d (DenseRatPoly.mul a b)) (-1) 1 =
      hankelBilinear d a b := by
  have hreorder :
      DenseRatPoly.exactIntegral
          (DenseRatPoly.mul d (DenseRatPoly.mul a b)) (-1) 1 =
        DenseRatPoly.exactIntegral
          (DenseRatPoly.mul a (DenseRatPoly.mul b d)) (-1) 1 := by
    rw [P2RoundedCanonical.dense_exactIntegral_eq_realize,
      P2RoundedCanonical.dense_exactIntegral_eq_realize]
    simp only [DenseRatPoly.realize_mul]
    congr 1
    ring
  rw [hreorder, exactIntegral_neg_one_one_eq_momentDot]
  exact momentDot_triple_eq_hankelBilinear d a b

/-! ### Connection to the verified analytic error ledger -/

/-- The direct triple-factor ball with its center evaluated through the
shared Hankel moments. -/
def tripleMomentIntegralBall
    (halfWidth : ℚ)
    (d a b : P2RoundedSharedEvaluator.Approx) :
    P2RoundedSharedEvaluator.QBall :=
  ⟨halfWidth * hankelBilinear d.coeffs a.coeffs b.coeffs,
    2 * halfWidth * P2RoundedSharedEvaluator.tripleFactorError d a b⟩

theorem tripleMomentIntegralBall_eq_tripleFactorIntegralBall
    (halfWidth : ℚ)
    (d a b : P2RoundedSharedEvaluator.Approx) :
    tripleMomentIntegralBall halfWidth d a b =
      P2RoundedSharedEvaluator.tripleFactorIntegralBall
        halfWidth d a b := by
  simp [tripleMomentIntegralBall,
    P2RoundedSharedEvaluator.tripleFactorIntegralBall,
    exactIntegral_triple_eq_hankelBilinear]

/-- Canonical panel ball using the staged moment center. -/
def tripleMomentEntryBall
    (k : Fin 32) (cache : P2RoundedSharedEvaluator.PanelCache)
    (kind : P2SelectedKind) (i j : Fin 24) :
    P2RoundedSharedEvaluator.QBall :=
  tripleMomentIntegralBall (p2PanelHalfWidthQ k.val)
    cache.defect (cache.component kind j) (cache.component kind i)

theorem tripleMomentEntryBall_eq_tripleFactorEntryBall
    (k : Fin 32) (cache : P2RoundedSharedEvaluator.PanelCache)
    (kind : P2SelectedKind) (i j : Fin 24) :
    tripleMomentEntryBall k cache kind i j =
      P2RoundedSharedEvaluator.tripleFactorEntryBall
        k cache kind i j := by
  simpa [tripleMomentEntryBall,
    P2RoundedSharedEvaluator.tripleFactorEntryBall] using
      tripleMomentIntegralBall_eq_tripleFactorIntegralBall
        (p2PanelHalfWidthQ k.val) cache.defect
        (cache.component kind j) (cache.component kind i)

/-- Rewrite the verified direct-factor QBall center through an arbitrary
checkpointed matvec.  The QBall radius—and therefore the analytic error
proof—does not change. -/
theorem tripleFactorEntryBall_center_eq_hankelDotFromVector
    {rows : ℕ} (k : Fin 32)
    (cache : P2RoundedSharedEvaluator.PanelCache)
    (kind : P2SelectedKind) (i j : Fin 24)
    (v : Vector ℚ rows)
    (hrows : (cache.component kind j).coeffs.length ≤ rows)
    (hv : HankelMatVecCorrect cache.defect.coeffs
      (cache.component kind i).coeffs v) :
    (P2RoundedSharedEvaluator.tripleFactorEntryBall
        k cache kind i j).center =
      p2PanelHalfWidthQ k.val *
        hankelDotFromVector
          (cache.component kind j).coeffs v hrows := by
  unfold P2RoundedSharedEvaluator.tripleFactorEntryBall
    P2RoundedSharedEvaluator.tripleFactorIntegralBall
  rw [exactIntegral_triple_eq_hankelBilinear]
  rw [hankelDotFromVector_eq_hankelBilinear
    cache.defect.coeffs (cache.component kind j).coeffs
    (cache.component kind i).coeffs v hrows hv]

/-- The previously proved analytic error ledger applies unchanged to the
Hankel-evaluated center. -/
theorem abs_p2PanelIntegralQ_sub_tripleMomentEntryBallCenter_le
    {cache : P2RoundedSharedEvaluator.PanelCache} {k : Fin 32}
    (hcache : cache.EnclosesCanonical k)
    (kind : P2SelectedKind) (i j : Fin 24) :
    |DenseRatPoly.p2PanelIntegralQ kind i j k.val -
        (tripleMomentEntryBall k cache kind i j).center| ≤
      (tripleMomentEntryBall k cache kind i j).radius := by
  rw [tripleMomentEntryBall_eq_tripleFactorEntryBall]
  exact
    P2RoundedSharedEvaluator.abs_p2PanelIntegralQ_sub_tripleFactorEntryBallCenter_le
      hcache kind i j

end P2RoundedTripleMoment

end RHP2Bridge
