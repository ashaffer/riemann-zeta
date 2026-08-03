/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage2DefectCharacterization
import RHBridge.ActivationCancellation
import RHBridge.SupportDecomposition

/-!
# Stage 3: minimal defect and support saturation

The three Stage-2 coordinate descriptions are derived from one radical
functional; they are not independent constraints.  The first new information
comes from the parameter history at the first crossing: the zero mode cannot
already live in any strictly smaller support window.
-/

namespace RHP2Bridge.Stage3SupportSaturation

open GeneralZetaWeilForm SuzukiClosedDomainLiterature
open Stage2DefectCharacterization
open SupportDecomposition

noncomputable section

/-- The parsimonious fixed-window defect is just the first-crossing mode. -/
abbrev MinimalDefect (a : ℝ) := FirstCrossingZeroMode a

/-- Stage-2 synchronization adds coordinate descriptions but no new logical
constraint once the common first-crossing source is retained. -/
theorem stage2_nonempty_iff_minimal_nonempty
    {a shift : ℝ} (hshift : shift < 0) :
    Nonempty (DefectCharacterization a shift) ↔
      Nonempty (MinimalDefect a) := by
  constructor
  · rintro ⟨defect⟩
    exact ⟨defect.source⟩
  · rintro ⟨mode⟩
    exact ⟨characterizeFirstCrossing hshift mode⟩

/-- A first crossing together with strict positivity at every smaller
nonnegative support. -/
structure FirstCrossingWithHistory (a : ℝ) extends FirstCrossingZeroMode a where
  strictlyPositiveBefore : ∀ b : ℝ, 0 ≤ b → b < a →
    ∀ g : LogarithmicFormDomain b, g.val ≠ 0 →
      0 < logarithmicWeilForm b g

/-- Classical first-crossing package with its parameter history. -/
axiom exists_firstCrossingWithHistory_of_not_rh
    (hnot : ¬ RiemannHypothesis) :
    ∃ a : ℝ, 0 < a ∧ Nonempty (FirstCrossingWithHistory a)

/-- Support saturation: a first-crossing mode with positive history cannot be
the nested-support image of a nonzero vector from a smaller window. -/
theorem no_nonzero_smaller_support_preimage
    {a : ℝ} (crossing : FirstCrossingWithHistory a)
    {b : ℝ} (hb : 0 ≤ b) (hba : b < a)
    (g : LogarithmicFormDomain b) (hg : g.val ≠ 0) :
    NestedSupport.nestedLogarithmicSupport (le_of_lt hba) g ≠
      crossing.vector := by
  intro heq
  have heqval := congrArg Subtype.val heq
  have heqval' :
      NestedSupport.nestedSupport b a g.val = crossing.vector.val := by
    simpa only [NestedSupport.nestedLogarithmicSupport_val] using heqval
  have hzeroA : weilForm a crossing.vector.val = 0 :=
    crossing.zero_energy
  have hzeroB : logarithmicWeilForm b g = 0 := by
    rw [← ActivationCancellation.weilForm_nestedSupport_eq
      (le_of_lt hba) g]
    rw [heqval']
    exact hzeroA
  exact (ne_of_gt (crossing.strictlyPositiveBefore b hb hba g hg)) hzeroB

/-- Geometric form of support saturation: every proper boundary collar of a
first-crossing vector is nonzero.  Thus the mode genuinely reaches the moving
boundary at every smaller scale, rather than merely being represented in the
larger ambient space. -/
theorem collarPart_ne_zero
    {a : ℝ} (crossing : FirstCrossingWithHistory a)
    {b : ℝ} (hb : 0 ≤ b) (hba : b < a) :
    collarPart b a hba.le crossing.vector.val ≠ 0 := by
  intro hcollar
  have hold : oldPart b a hba.le crossing.vector.val = crossing.vector.val := by
    have hsum := oldPart_add_collarPart b a hba.le crossing.vector.val
    rw [hcollar, add_zero] at hsum
    exact hsum
  obtain ⟨u, hu, _⟩ :=
    exists_unique_oldPart_preimage b a hba.le crossing.vector.val
  have hnested :
      NestedSupport.nestedSupport b a u = crossing.vector.val :=
    hu.trans hold
  have hudomain : InLogarithmicDomain b u := by
    apply (NestedSupport.inLogarithmicDomain_nestedSupport_iff hba.le u).mp
    rw [hnested]
    exact crossing.vector.property
  let g : LogarithmicFormDomain b := ⟨u, hudomain⟩
  have hg : g.val ≠ 0 := by
    intro hzero
    apply crossing.nonzero
    rw [← hnested]
    change u = 0 at hzero
    rw [hzero]
    exact map_zero (NestedSupport.nestedSupportLI b a hba.le)
  apply no_nonzero_smaller_support_preimage crossing hb hba g hg
  apply Subtype.ext
  exact hnested

/-- Under failure of RH, the first-crossing defect supplied by the literature
is necessarily support-saturating. -/
theorem not_rh_implies_support_saturating_defect
    (hnot : ¬ RiemannHypothesis) :
    ∃ a : ℝ, 0 < a ∧ ∃ crossing : FirstCrossingWithHistory a,
      ∀ (b : ℝ) (_hb : 0 ≤ b) (hba : b < a)
        (g : LogarithmicFormDomain b), g.val ≠ 0 →
          NestedSupport.nestedLogarithmicSupport hba.le g ≠ crossing.vector := by
  obtain ⟨a, ha, ⟨crossing⟩⟩ :=
    exists_firstCrossingWithHistory_of_not_rh hnot
  refine ⟨a, ha, crossing, ?_⟩
  intro b hb hba g hg
  exact no_nonzero_smaller_support_preimage crossing hb hba g hg

end

end RHP2Bridge.Stage3SupportSaturation
