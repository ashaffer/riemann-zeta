/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedMomentRefinement

/-!
# Generic assembly helpers for generated canonical `p = 2` certificates

Generated files should contain only explicit data and small kernel-checked
equalities.  This module turns whole-vector equalities into the semantic
moment interface and combines contiguous finite ranges without depending on
any particular generated certificate.
-/

namespace RHP2Bridge

open P2RoundedSharedEvaluator
open P2RoundedTripleMoment

namespace P2RoundedMomentRefinement

namespace PanelMomentData.CorrectFor

/-- Whole-vector checkpoints imply the pointwise semantic interface consumed
by the staged and bounded triple-factor ledgers. -/
theorem of_vector_eq
    {data : PanelMomentData} {cache : PanelCache}
    (hmoments : data.moments = defectMoments cache.defect.coeffs)
    (hlength : ∀ (kind : P2SelectedKind) (i : Fin 24),
      (cache.component kind i).coeffs.length ≤ 149)
    (hmatvecs : ∀ (kind : P2SelectedKind) (i : Fin 24),
      data.matvecs kind i =
        hankelMatVecFromMoments data.moments
          (cache.component kind i).coeffs) :
    data.CorrectFor cache := by
  constructor
  · rw [hmoments]
    exact defectMoments_correct cache.defect.coeffs
  · exact hlength
  · intro kind i row
    rw [hmatvecs kind i]

end PanelMomentData.CorrectFor

end P2RoundedMomentRefinement

namespace P2RoundedGeneratedCertificate

/-- The canonical parity/index dispatch into the 48 selected modes. -/
abbrev selectedMode
    (kind : P2SelectedKind) (i : Fin 24) : Fin 48 :=
  p2SelectedModeFin kind i

@[simp] theorem selectedMode_val
    (kind : P2SelectedKind) (i : Fin 24) :
    (selectedMode kind i).val = p2SelectedDegree kind i.val :=
  p2SelectedModeFin_val kind i

/-- `FinRangeAll P lo hi` asserts `P` on the half-open value interval
`[lo, hi)` inside `Fin n`.  Bounds may be arbitrary naturals, which lets
generated modules state uniform fixed-size chunks even at an endpoint. -/
def FinRangeAll {n : Nat} (P : Fin n → Prop) (lo hi : Nat) : Prop :=
  ∀ i : Fin n, lo ≤ i.val → i.val < hi → P i

namespace FinRangeAll

theorem of_forall
    {n lo hi : Nat} {P : Fin n → Prop}
    (h : ∀ i, P i) : FinRangeAll P lo hi := by
  intro i _ _
  exact h i

/-- Combine two chunks sharing an endpoint. -/
theorem combine
    {n a b c : Nat} {P : Fin n → Prop}
    (hab : FinRangeAll P a b) (hbc : FinRangeAll P b c) :
    FinRangeAll P a c := by
  intro i hai hic
  by_cases hib : i.val < b
  · exact hab i hai hib
  · exact hbc i (Nat.le_of_not_gt hib) hic

/-- A chunk spanning all possible `Fin n` values proves the unrestricted
finite proposition. -/
theorem to_forall
    {n : Nat} {P : Fin n → Prop}
    (h : FinRangeAll P 0 n) : ∀ i, P i := by
  intro i
  exact h i (Nat.zero_le i.val) i.isLt

theorem zero_card_iff
    {n : Nat} {P : Fin n → Prop} :
    FinRangeAll P 0 n ↔ ∀ i, P i := by
  constructor
  · exact to_forall
  · exact of_forall

end FinRangeAll

end P2RoundedGeneratedCertificate

end RHP2Bridge
