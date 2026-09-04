/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.RelativeCrossNecessity
import RHBridge.SemilocalWardDistillation
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-!
# Algebraic schemas from recursive consolidation

This module records assumption-transparent lemmas which recur in the
fixed-point audit: zero-energy kernel charge, quantitative decoder stability,
finite-channel reserve completion, and the maximal-frontier continuation
contradiction.  None of these statements contains zeta-specific analytic
input.
-/

namespace RHBridge.RecursiveConsolidation

open RHP2Bridge.RelativeCrossNecessity
open SemilocalWardDistillation
open scoped BigOperators

noncomputable section

/-! ## Kernel charge -/

/-- `KernelNullChargeOn pairing oldKernel directions` says that every old
nullvector is uncharged against every licensed new direction.  The definition
is deliberately set-level: analytic applications may supply subspaces,
support germs, or harmonic slices as the two sets. -/
def KernelNullChargeOn {N W R : Type*} [Zero R]
    (pairing : N → W → R) (oldKernel : Set N) (directions : Set W) : Prop :=
  ∀ n ∈ oldKernel, ∀ w ∈ directions, pairing n w = 0

/-- Null-charge against a larger direction set automatically restricts to
every intermediate direction set. -/
theorem kernelNullChargeOn_of_directions_subset
    {N W R : Type*} [Zero R] {pairing : N → W → R}
    {oldKernel : Set N} {intermediate larger : Set W}
    (hKNC : KernelNullChargeOn pairing oldKernel larger)
    (hsub : intermediate ⊆ larger) :
    KernelNullChargeOn pairing oldKernel intermediate := by
  intro n hn w hw
  exact hKNC n hn w (hsub hw)

/-- Along an antitone family of direction sets, KNC at one index propagates
to every later (hence smaller) member. -/
theorem kernelNullChargeOn_antitone_family
    {N W R ι : Type*} [Zero R] [Preorder ι]
    {pairing : N → W → R} {oldKernel : Set N}
    (directions : ι → Set W) (hanti : Antitone directions)
    {i j : ι} (hij : i ≤ j)
    (hKNC : KernelNullChargeOn pairing oldKernel (directions i)) :
    KernelNullChargeOn pairing oldKernel (directions j) :=
  kernelNullChargeOn_of_directions_subset hKNC (hanti hij)

/-- In particular, KNC on the zeroth member of a decreasing sequence holds
on every member of that sequence. -/
theorem kernelNullChargeOn_antitone_nat
    {N W R : Type*} [Zero R] {pairing : N → W → R}
    {oldKernel : Set N} (directions : ℕ → Set W)
    (hanti : Antitone directions)
    (hKNC : KernelNullChargeOn pairing oldKernel (directions 0)) :
    ∀ k, KernelNullChargeOn pairing oldKernel (directions k) := by
  intro k
  exact kernelNullChargeOn_antitone_family directions hanti (Nat.zero_le k) hKNC

/-- If a globally nonnegative two-by-two mixed quadratic form has zero old
diagonal energy, its cross coefficient must vanish.  This is the scalar core
of kernel-null-charge necessity at a semidefinite first contact. -/
theorem cross_eq_zero_of_zero_oldEnergy_mixed_nonnegative
    {A B D : ℝ} (hA : A = 0)
    (hmixed : ∀ x y : ℝ, 0 ≤ mixedQuadratic A B D x y) :
    B = 0 := by
  subst A
  have hD : 0 ≤ D := by
    simpa [mixedQuadratic] using hmixed 0 1
  have hline : ∀ t : ℝ, 0 ≤ 0 + 2 * t * B + t ^ 2 * D := by
    intro t
    simpa [mixedQuadratic, mul_comm, mul_left_comm] using hmixed 1 t
  have hdet : B ^ 2 ≤ 0 * D :=
    cross_sq_le_of_quadratic_nonneg (A := 0) (C := B) (D := D)
      (by norm_num) hD hline
  nlinarith [sq_nonneg B]

/-- Every nonzero charge at a zero-energy contact produces an explicit
negative direction, independently of the new diagonal coefficient. -/
theorem chargedContact_has_negative_direction
    {B D : ℝ} (hB : B ≠ 0) :
    ∃ x y : ℝ, mixedQuadratic 0 B D x y < 0 := by
  refine ⟨-(D + 1) / (2 * B), 1, ?_⟩
  have hden : 2 * B ≠ 0 := mul_ne_zero (by norm_num) hB
  have hvalue :
      mixedQuadratic 0 B D (-(D + 1) / (2 * B)) 1 = -1 := by
    simp only [mixedQuadratic, zero_mul, zero_add, mul_one, one_pow]
    field_simp [hden]
    ring
  rw [hvalue]
  norm_num

/-- Positivity of a real symmetric bilinear form on the enlarged space forces
an old zero-energy vector to have zero mixed pairing with every enlarged
direction. -/
theorem symmetricBilinForm_cross_eq_zero_of_nonnegative
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    (Q : LinearMap.BilinForm ℝ V) (hsymm : Q.IsSymm)
    (hnonneg : ∀ v, 0 ≤ Q v v) {n w : V}
    (hn : Q n n = 0) :
    Q n w = 0 := by
  apply cross_eq_zero_of_zero_oldEnergy_mixed_nonnegative hn
  intro x y
  have hxy := hnonneg (x • n + y • w)
  have hexpand :
      Q (x • n + y • w) (x • n + y • w) =
        mixedQuadratic (Q n n) (Q n w) (Q w w) x y := by
    simp only [map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply,
      smul_eq_mul, mixedQuadratic]
    rw [hsymm.eq w n]
    ring
  rwa [hexpand] at hxy

/-- The preceding pointwise statement gives KNC against any licensed set of
new directions, once the old-kernel set consists of zero-energy vectors. -/
theorem symmetricBilinForm_kernelNullChargeOn
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    (Q : LinearMap.BilinForm ℝ V) (hsymm : Q.IsSymm)
    (hnonneg : ∀ v, 0 ≤ Q v v) {oldKernel directions : Set V}
    (hkernel : ∀ n ∈ oldKernel, Q n n = 0) :
    KernelNullChargeOn (fun n w ↦ Q n w) oldKernel directions := by
  intro n hn w _
  exact symmetricBilinForm_cross_eq_zero_of_nonnegative Q hsymm hnonneg
    (hkernel n hn)

/-! ## Provenance and decoder stability -/

/-- `ProvenanceBound U T r c` says that target values differ by at most `c`
whenever their observed representations under `U` differ by at most `r`. -/
def ProvenanceBound {X Y Z : Type*} [PseudoMetricSpace Y] [PseudoMetricSpace Z]
    (U : X → Y) (T : X → Z) (radius bound : ℝ) : Prop :=
  ∀ x x' : X, dist (U x) (U x') ≤ radius →
    dist (T x) (T x') ≤ bound

/-- A decoder with uniform target error `epsilon` transfers its pointwise
modulus to the underlying target with the sharp triangle loss `2*epsilon`. -/
theorem provenanceBound_of_uniform_decoder_error
    {X Y Z : Type*} [PseudoMetricSpace Y] [PseudoMetricSpace Z]
    (U : X → Y) (T : X → Z) (decoder : Y → Z)
    {radius decoderBound epsilon : ℝ}
    (herror : ∀ x, dist (T x) (decoder (U x)) ≤ epsilon)
    (hdecoder : ∀ y y', dist y y' ≤ radius →
      dist (decoder y) (decoder y') ≤ decoderBound) :
    ProvenanceBound U T radius (2 * epsilon + decoderBound) := by
  intro x x' hxx'
  have hmiddle :
      dist (decoder (U x)) (decoder (U x')) ≤ decoderBound :=
    hdecoder (U x) (U x') hxx'
  calc
    dist (T x) (T x') ≤
        dist (T x) (decoder (U x)) + dist (decoder (U x)) (T x') :=
      dist_triangle _ _ _
    _ ≤ dist (T x) (decoder (U x)) +
        (dist (decoder (U x)) (decoder (U x')) +
          dist (decoder (U x')) (T x')) := by
      gcongr
      exact dist_triangle _ _ _
    _ ≤ epsilon + (decoderBound + epsilon) := by
      exact add_le_add (herror x)
        (add_le_add hmiddle (by simpa [dist_comm] using herror x'))
    _ = 2 * epsilon + decoderBound := by ring

/-- Postcomposition by an `L`-Lipschitz representation map transports a
composite provenance bound back to radius `r/L`. -/
theorem provenanceBound_of_postcompose_lipschitz
    {X Y W Z : Type*} [PseudoMetricSpace Y] [PseudoMetricSpace W]
    [PseudoMetricSpace Z]
    (U : X → Y) (T : X → Z) (V : Y → W)
    {L radius bound : ℝ} (hL : 0 < L)
    (hV : ∀ y y', dist (V y) (V y') ≤ L * dist y y')
    (hcomposite : ProvenanceBound (fun x ↦ V (U x)) T radius bound) :
    ProvenanceBound U T (radius / L) bound := by
  intro x x' hxx'
  apply hcomposite
  calc
    dist (V (U x)) (V (U x')) ≤ L * dist (U x) (U x') :=
      hV (U x) (U x')
    _ ≤ L * (radius / L) :=
      mul_le_mul_of_nonneg_left hxx' hL.le
    _ = radius := by field_simp [ne_of_gt hL]

/-- If `V` has an `M`-Lipschitz inverse on the observed range, a provenance
bound before the coordinate change controls the postcomposed representation
at the correspondingly enlarged radius. -/
theorem provenanceBound_of_postcompose_inverseLipschitz
    {X Y W Z : Type*} [PseudoMetricSpace Y] [PseudoMetricSpace W]
    [PseudoMetricSpace Z]
    (U : X → Y) (T : X → Z) (V : Y → W)
    {M radius bound : ℝ} (hM : 0 ≤ M)
    (hinverse : ∀ x x',
      dist (U x) (U x') ≤ M * dist (V (U x)) (V (U x')))
    (hbase : ProvenanceBound U T (M * radius) bound) :
    ProvenanceBound (fun x ↦ V (U x)) T radius bound := by
  intro x x' hxx'
  apply hbase
  exact (hinverse x x').trans (mul_le_mul_of_nonneg_left hxx' hM)

/-! ## Multichannel reserve completion -/

/-- Sharp finite-channel square completion from componentwise cross budgets.
If channel `i` costs at most
`charge i * sqrt A * sqrt S`, their worst-case aligned charge is the sum of
the individual charges.  A collar reserve closes the block precisely when
the squared total charge plus the diagonal loss is at most one. -/
theorem finiteChannel_reserve_square_completion
    {I : Type*} [Fintype I]
    (cross charge : I → ℝ) {A S D loss : ℝ}
    (hA : 0 ≤ A) (hS : 0 ≤ S)
    (hcharge : ∀ i, 0 ≤ charge i)
    (hcross : ∀ i, |cross i| ≤
      charge i * Real.sqrt A * Real.sqrt S)
    (hdiagonal : (1 - loss) * S ≤ D)
    (hbudget : (∑ i, charge i) ^ 2 + loss ≤ 1) :
    0 ≤ A + 2 * (∑ i, cross i) + D := by
  let totalCharge : ℝ := ∑ i, charge i
  have htotalCharge : 0 ≤ totalCharge := by
    exact Finset.sum_nonneg fun i _ ↦ hcharge i
  have hsqrtA : (Real.sqrt A) ^ 2 = A := Real.sq_sqrt hA
  have hsqrtS : (Real.sqrt S) ^ 2 = S := Real.sq_sqrt hS
  have habs :
      |∑ i, cross i| ≤ totalCharge * Real.sqrt A * Real.sqrt S := by
    calc
      |∑ i, cross i| ≤ ∑ i, |cross i| :=
        Finset.abs_sum_le_sum_abs cross Finset.univ
      _ ≤ ∑ i, charge i * Real.sqrt A * Real.sqrt S :=
        Finset.sum_le_sum fun i _ ↦ hcross i
      _ = totalCharge * Real.sqrt A * Real.sqrt S := by
        dsimp [totalCharge]
        rw [← Finset.sum_mul, ← Finset.sum_mul]
  have hcrossLower :
      -(totalCharge * Real.sqrt A * Real.sqrt S) ≤ ∑ i, cross i :=
    (abs_le.mp habs).1
  have hremainder : 0 ≤ 1 - loss - totalCharge ^ 2 := by
    dsimp [totalCharge] at hbudget ⊢
    linarith
  have hsquare :
      0 ≤ (Real.sqrt A - totalCharge * Real.sqrt S) ^ 2 +
        (1 - loss - totalCharge ^ 2) * S :=
    add_nonneg (sq_nonneg _ ) (mul_nonneg hremainder hS)
  have hbase :
      0 ≤ A - 2 * totalCharge * Real.sqrt A * Real.sqrt S +
        (1 - loss) * S := by
    nlinarith [hsqrtA, hsqrtS]
  nlinarith

/-! ## Maximal-frontier continuation -/

/-- A bounded reachable set cannot both contain its supremal frontier and
admit a strict right extension from every reachable point.  This is the
order-theoretic contradiction at the core of maximal-support continuation. -/
theorem not_bddAbove_of_frontier_mem_of_rightExtension
    {reachable : Set ℝ}
    (hfrontier : BddAbove reachable → sSup reachable ∈ reachable)
    (hright : ∀ x ∈ reachable, ∃ y ∈ reachable, x < y) :
    ¬ BddAbove reachable := by
  intro hbounded
  have hsup : sSup reachable ∈ reachable := hfrontier hbounded
  obtain ⟨y, hy, hsupy⟩ := hright (sSup reachable) hsup
  exact (not_lt_of_ge (le_csSup hbounded hy)) hsupy

end

end RHBridge.RecursiveConsolidation
