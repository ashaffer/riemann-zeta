/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2Containment

/-!
# Finite entry-certificate interface for the canonical `p = 2` blocks

The exact finite certificate stores two symmetric `24 × 24` interval
matrices.  Consequently only the `300 + 300` upper-triangular entries need
analytic enclosure proofs.  This module packages those 600 obligations as a
single finite type, exposes their exact integer centers and common radius,
and lifts either center-distance or interval certificates to the canonical
matrix-containment endpoint.

No numerical computation is trusted here.  Symmetry of the two stored
integer tables is checked by kernel reduction with `decide`; symmetry of the
analytic scalar entries follows from their exact integral formulas.
-/

namespace RHP2Bridge

open scoped ENNReal InnerProductSpace RealInnerProductSpace

noncomputable section

/-- The two parity blocks in the canonical 48-dimensional certificate. -/
inductive P2EntryBlock
  | even
  | odd
  deriving DecidableEq, Fintype

/-- A parity-tagged ordered entry of one canonical `24 × 24` block. -/
structure P2EntryIndex where
  block : P2EntryBlock
  row : Fin 24
  col : Fin 24
  deriving DecidableEq, Fintype

/-- The analytic certificate need only cover upper-triangular entries. -/
abbrev P2UpperEntryIndex := {e : P2EntryIndex // e.row ≤ e.col}

set_option maxRecDepth 4096 in
-- Kernel evaluation of the 1,152 candidate tagged pairs needs deeper recursion.
/-- There are exactly `2 * (24 * 25 / 2) = 600` analytic entry obligations. -/
theorem card_p2UpperEntryIndex : Fintype.card P2UpperEntryIndex = 600 := by
  decide

/-- Exact scalar expression for an even-block entry. -/
noncomputable def p2EvenScalarEntry (i j : Fin 24) : ℝ :=
  GlideKernel.p2Alpha * (if i = j then 1 else 0) +
    (1 / (2 * Real.pi)) *
      (∫ r in (-50 : ℝ)..50, p2EvenBandIntegrand i.val j.val r) +
    2 * p2PoleCoeff (2 * j.val) * p2PoleCoeff (2 * i.val)

/-- Exact scalar expression for an odd-block entry. -/
noncomputable def p2OddScalarEntry (i j : Fin 24) : ℝ :=
  GlideKernel.p2Alpha * (if i = j then 1 else 0) +
    (1 / (2 * Real.pi)) *
      (∫ r in (-50 : ℝ)..50, p2OddBandIntegrand i.val j.val r) -
    2 * p2PoleCoeff (2 * j.val + 1) * p2PoleCoeff (2 * i.val + 1)

/-- The parity-tagged scalar entry consumed by a generated certificate. -/
noncomputable def p2ScalarEntry (e : P2EntryIndex) : ℝ :=
  match e.block with
  | .even => p2EvenScalarEntry e.row e.col
  | .odd => p2OddScalarEntry e.row e.col

/-- Integer numerator of the stored `10⁻¹⁸` center before restoring the
diagonal `beta` shift. -/
def p2StoredCenterNumerator (e : P2EntryIndex) : ℤ :=
  match e.block with
  | .even => FullInfClipped48.evenAFun e.row.val e.col.val
  | .odd => FullInfClipped48.oddAFun e.row.val e.col.val

/-- Exact center of the stored interval for a tagged entry. -/
noncomputable def p2StoredCenter (e : P2EntryIndex) : ℝ :=
  match e.block with
  | .even => FullInfClipped48Real.evenMidReal e.row e.col
  | .odd => FullInfClipped48Real.oddMidReal e.row e.col

/-- Every stored entry has this exact rational radius. -/
noncomputable def p2StoredRadius : ℝ :=
  (FullInfClipped48.delta : ℝ)

/-- Lower endpoint of the stored interval for a tagged entry. -/
noncomputable def p2StoredLower (e : P2EntryIndex) : ℝ :=
  match e.block with
  | .even => FullInfClipped48Real.evenLowerReal e.row e.col
  | .odd => FullInfClipped48Real.oddLowerReal e.row e.col

/-- Upper endpoint of the stored interval for a tagged entry. -/
noncomputable def p2StoredUpper (e : P2EntryIndex) : ℝ :=
  match e.block with
  | .even => FullInfClipped48Real.evenUpperReal e.row e.col
  | .odd => FullInfClipped48Real.oddUpperReal e.row e.col

/-- The center is literally the stored integer divided by `10¹⁸`, plus the
diagonal shift.  This is the normalization used by certificate generators. -/
theorem p2StoredCenter_eq_integer_table (e : P2EntryIndex) :
    p2StoredCenter e =
      (p2StoredCenterNumerator e : ℝ) / 10 ^ 18 +
        if e.row = e.col then (227 : ℝ) / 10 ^ 7 else 0 := by
  rcases e with ⟨block, i, j⟩
  cases block <;>
    simp [p2StoredCenter, p2StoredCenterNumerator,
      FullInfClipped48Real.evenMidReal,
      FullInfClipped48Real.oddMidReal,
      FullInfClipped48Real.evenAReal,
      FullInfClipped48Real.oddAReal,
      FullInfClipped48.evenAQ, FullInfClipped48.oddAQ,
      FullInfClipped48.evenAInt, FullInfClipped48.oddAInt,
      FullInfClipped48.scale, FullInfClipped48.beta]

theorem p2StoredRadius_eq : p2StoredRadius = (1 : ℝ) / 10 ^ 12 := by
  norm_num [p2StoredRadius, FullInfClipped48.delta]

theorem p2StoredLower_eq_center_sub_radius (e : P2EntryIndex) :
    p2StoredLower e = p2StoredCenter e - p2StoredRadius := by
  rcases e with ⟨block, i, j⟩
  cases block <;>
    rfl

theorem p2StoredUpper_eq_center_add_radius (e : P2EntryIndex) :
    p2StoredUpper e = p2StoredCenter e + p2StoredRadius := by
  rcases e with ⟨block, i, j⟩
  cases block <;>
    rfl

/-- Direct interval form of the 600 upper-triangular analytic obligations. -/
def P2UpperEntryEnclosures : Prop :=
  ∀ e : P2UpperEntryIndex,
    p2StoredLower e.val ≤ p2ScalarEntry e.val ∧
      p2ScalarEntry e.val ≤ p2StoredUpper e.val

/-- Center-radius form of the same 600 obligations.  This is often the most
convenient target for generated panel certificates. -/
def P2UpperEntryCenterCertificate : Prop :=
  ∀ e : P2UpperEntryIndex,
    |p2ScalarEntry e.val - p2StoredCenter e.val| ≤ p2StoredRadius

/-- Build the unified 600-entry interval certificate from the two natural
upper-triangular block families emitted by a certificate generator. -/
theorem p2UpperEntryEnclosures_of_blocks
    (he : ∀ i j : Fin 24, i ≤ j →
      FullInfClipped48Real.evenLowerReal i j ≤ p2EvenScalarEntry i j ∧
        p2EvenScalarEntry i j ≤ FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j : Fin 24, i ≤ j →
      FullInfClipped48Real.oddLowerReal i j ≤ p2OddScalarEntry i j ∧
        p2OddScalarEntry i j ≤ FullInfClipped48Real.oddUpperReal i j) :
    P2UpperEntryEnclosures := by
  rintro ⟨⟨block, i, j⟩, hij⟩
  cases block
  · simpa [p2StoredLower, p2StoredUpper, p2ScalarEntry] using he i j hij
  · simpa [p2StoredLower, p2StoredUpper, p2ScalarEntry] using ho i j hij

/-- Center-radius analogue of `p2UpperEntryEnclosures_of_blocks`. -/
theorem p2UpperEntryCenterCertificate_of_blocks
    (he : ∀ i j : Fin 24, i ≤ j →
      |p2EvenScalarEntry i j -
        FullInfClipped48Real.evenMidReal i j| ≤ p2StoredRadius)
    (ho : ∀ i j : Fin 24, i ≤ j →
      |p2OddScalarEntry i j -
        FullInfClipped48Real.oddMidReal i j| ≤ p2StoredRadius) :
    P2UpperEntryCenterCertificate := by
  rintro ⟨⟨block, i, j⟩, hij⟩
  cases block
  · simpa [p2ScalarEntry, p2StoredCenter] using he i j hij
  · simpa [p2ScalarEntry, p2StoredCenter] using ho i j hij

/-- A center-radius certificate implies the exact stored interval bounds. -/
theorem p2UpperEntryEnclosures_of_centerCertificate
    (h : P2UpperEntryCenterCertificate) :
    P2UpperEntryEnclosures := by
  intro e
  have he := h e
  rw [abs_le] at he
  rw [p2StoredLower_eq_center_sub_radius,
    p2StoredUpper_eq_center_add_radius]
  constructor <;> linarith [he.1, he.2]

theorem p2EvenMatrix_entry_eq_scalarEntry (i j : Fin 24) :
    FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j =
      p2EvenScalarEntry i j := by
  exact p2EvenMatrix_entry_eq_scalar_integral i j

theorem p2OddMatrix_entry_eq_scalarEntry (i j : Fin 24) :
    FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j =
      p2OddScalarEntry i j := by
  exact p2OddMatrix_entry_eq_scalar_integral i j

theorem p2EvenScalarEntry_symmetric (i j : Fin 24) :
    p2EvenScalarEntry i j = p2EvenScalarEntry j i := by
  have hint :
      (∫ r in (-50 : ℝ)..50, p2EvenBandIntegrand i.val j.val r) =
        ∫ r in (-50 : ℝ)..50, p2EvenBandIntegrand j.val i.val r := by
    apply intervalIntegral.integral_congr
    intro r _
    unfold p2EvenBandIntegrand
    ring
  unfold p2EvenScalarEntry
  rw [hint]
  simp only [eq_comm]
  ring

theorem p2OddScalarEntry_symmetric (i j : Fin 24) :
    p2OddScalarEntry i j = p2OddScalarEntry j i := by
  have hint :
      (∫ r in (-50 : ℝ)..50, p2OddBandIntegrand i.val j.val r) =
        ∫ r in (-50 : ℝ)..50, p2OddBandIntegrand j.val i.val r := by
    apply intervalIntegral.integral_congr
    intro r _
    unfold p2OddBandIntegrand
    ring
  unfold p2OddScalarEntry
  rw [hint]
  simp only [eq_comm]
  ring

theorem p2EvenMatrix_symmetric (i j : Fin 24) :
    FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j =
      FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm j i := by
  rw [p2EvenMatrix_entry_eq_scalarEntry,
    p2EvenMatrix_entry_eq_scalarEntry, p2EvenScalarEntry_symmetric]

theorem p2OddMatrix_symmetric (i j : Fin 24) :
    FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j =
      FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm j i := by
  rw [p2OddMatrix_entry_eq_scalarEntry,
    p2OddMatrix_entry_eq_scalarEntry, p2OddScalarEntry_symmetric]

private theorem evenAFun_symmetric : ∀ i j : Fin 24,
    FullInfClipped48.evenAFun i.val j.val =
      FullInfClipped48.evenAFun j.val i.val := by
  decide

private theorem oddAFun_symmetric : ∀ i j : Fin 24,
    FullInfClipped48.oddAFun i.val j.val =
      FullInfClipped48.oddAFun j.val i.val := by
  decide

private theorem evenAReal_symmetric (i j : Fin 24) :
    FullInfClipped48Real.evenAReal i j =
      FullInfClipped48Real.evenAReal j i := by
  change ((FullInfClipped48.evenAFun i.val j.val : ℤ) : ℝ) =
    ((FullInfClipped48.evenAFun j.val i.val : ℤ) : ℝ)
  rw [evenAFun_symmetric]

private theorem oddAReal_symmetric (i j : Fin 24) :
    FullInfClipped48Real.oddAReal i j =
      FullInfClipped48Real.oddAReal j i := by
  change ((FullInfClipped48.oddAFun i.val j.val : ℤ) : ℝ) =
    ((FullInfClipped48.oddAFun j.val i.val : ℤ) : ℝ)
  rw [oddAFun_symmetric]

theorem evenLowerReal_symmetric (i j : Fin 24) :
    FullInfClipped48Real.evenLowerReal i j =
      FullInfClipped48Real.evenLowerReal j i := by
  simp only [FullInfClipped48Real.evenLowerReal,
    FullInfClipped48Real.evenMidReal, Matrix.of_apply]
  rw [evenAReal_symmetric]
  simp only [eq_comm]

theorem evenUpperReal_symmetric (i j : Fin 24) :
    FullInfClipped48Real.evenUpperReal i j =
      FullInfClipped48Real.evenUpperReal j i := by
  simp only [FullInfClipped48Real.evenUpperReal,
    FullInfClipped48Real.evenMidReal, Matrix.of_apply]
  rw [evenAReal_symmetric]
  simp only [eq_comm]

theorem oddLowerReal_symmetric (i j : Fin 24) :
    FullInfClipped48Real.oddLowerReal i j =
      FullInfClipped48Real.oddLowerReal j i := by
  simp only [FullInfClipped48Real.oddLowerReal,
    FullInfClipped48Real.oddMidReal, Matrix.of_apply]
  rw [oddAReal_symmetric]
  simp only [eq_comm]

theorem oddUpperReal_symmetric (i j : Fin 24) :
    FullInfClipped48Real.oddUpperReal i j =
      FullInfClipped48Real.oddUpperReal j i := by
  simp only [FullInfClipped48Real.oddUpperReal,
    FullInfClipped48Real.oddMidReal, Matrix.of_apply]
  rw [oddAReal_symmetric]
  simp only [eq_comm]

private theorem even_upper_containment
    (h : P2UpperEntryEnclosures) (i j : Fin 24) (hij : i ≤ j) :
    FullInfClipped48Real.evenLowerReal i j ≤
        FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ∧
      FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ≤
        FullInfClipped48Real.evenUpperReal i j := by
  have he := h ⟨⟨.even, i, j⟩, hij⟩
  simpa [p2StoredLower, p2StoredUpper, p2ScalarEntry,
    ← p2EvenMatrix_entry_eq_scalarEntry] using he

private theorem odd_upper_containment
    (h : P2UpperEntryEnclosures) (i j : Fin 24) (hij : i ≤ j) :
    FullInfClipped48Real.oddLowerReal i j ≤
        FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ∧
      FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ≤
        FullInfClipped48Real.oddUpperReal i j := by
  have he := h ⟨⟨.odd, i, j⟩, hij⟩
  simpa [p2StoredLower, p2StoredUpper, p2ScalarEntry,
    ← p2OddMatrix_entry_eq_scalarEntry] using he

/-- The 600 upper-triangular scalar enclosures imply the two full ordered
`24 × 24` matrix-containment statements required by the endpoint. -/
theorem p2_matrix_containment_of_upper_entry_enclosures
    (h : P2UpperEntryEnclosures) :
    (∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.evenUpperReal i j) ∧
    (∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.oddUpperReal i j) := by
  constructor
  · intro i j
    by_cases hij : i ≤ j
    · exact even_upper_containment h i j hij
    · have hji : j ≤ i := by omega
      have h' := even_upper_containment h j i hji
      rwa [evenLowerReal_symmetric, evenUpperReal_symmetric,
        p2EvenMatrix_symmetric]
  · intro i j
    by_cases hij : i ≤ j
    · exact odd_upper_containment h i j hij
    · have hji : j ≤ i := by omega
      have h' := odd_upper_containment h j i hji
      rwa [oddLowerReal_symmetric, oddUpperReal_symmetric,
        p2OddMatrix_symmetric]

/-- Canonical clipped endpoint consuming exactly the 600 finite scalar
entry enclosures, with parity and lower-triangle entries discharged here. -/
theorem p2_clipped_endpoint_of_upper_entry_enclosures
    (h : P2UpperEntryEnclosures)
    {f : FullInfP2Endpoint.P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2ClippedForm f f := by
  obtain ⟨he, ho⟩ := p2_matrix_containment_of_upper_entry_enclosures h
  exact p2_clipped_endpoint_of_matrix_containment_no_parity he ho hf

/-- Center-radius version of the canonical finite endpoint. -/
theorem p2_clipped_endpoint_of_upper_center_certificate
    (h : P2UpperEntryCenterCertificate)
    {f : FullInfP2Endpoint.P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2ClippedForm f f := by
  exact p2_clipped_endpoint_of_upper_entry_enclosures
    (p2UpperEntryEnclosures_of_centerCertificate h) hf

end

end RHP2Bridge
