import Mathlib

/-!
# Abstract metamathematical ledger for RH

This file deliberately does not assert that an arithmetization of RH has
already been carried out. It records the logical argument available after one
supplies a finite-counterexample encoding and verifies it in a chosen theory.
-/

namespace RHP2Bridge.MetamathematicalLedger

/-- A semantic finite-counterexample presentation. Computability is an
explicit field, not silently inferred from the equivalence. -/
structure FiniteCounterexamplePresentation (P : Prop) where
  counterexample : ℕ → Prop
  decidableCounterexample : DecidablePred counterexample
  false_iff_exists_counterexample : ¬ P ↔ ∃ n, counterexample n

/-- An abstract provability predicate. Instantiating this with ZFC requires
coding formulas, proofs, and the selected arithmetic version of RH. -/
structure Theory where
  Provable : Prop → Prop

/-- The theory verifies every genuine finite counterexample as a proof of
`¬ P`. A concrete application must formalize this verification. -/
def VerifiesCounterexamples {P : Prop} (T : Theory)
    (E : FiniteCounterexamplePresentation P) : Prop :=
  ∀ n, E.counterexample n → T.Provable (¬ P)

/-- Semantic soundness is stronger than consistency and must be named. -/
def Sound (T : Theory) : Prop := ∀ P : Prop, T.Provable P → P

/-- Syntactic independence from the selected theory, not a third truth value. -/
def Independent (T : Theory) (P : Prop) : Prop :=
  ¬ T.Provable P ∧ ¬ T.Provable (¬ P)

/-- If every actual finite counterexample would prove the negation in the
theory, unprovability of that negation implies truth in the metatheory. -/
theorem true_of_negation_unprovable {P : Prop} (T : Theory)
    (E : FiniteCounterexamplePresentation P)
    (hverify : VerifiesCounterexamples T E)
    (hunprovable : ¬ T.Provable (¬ P)) : P := by
  by_contra hP
  obtain ⟨n, hn⟩ := E.false_iff_exists_counterexample.mp hP
  exact hunprovable (hverify n hn)

/-- Hence independence of a finitely refutable proposition forces its truth
in the ambient metatheory. It does not establish independence. -/
theorem true_of_independent {P : Prop} (T : Theory)
    (E : FiniteCounterexamplePresentation P)
    (hverify : VerifiesCounterexamples T E)
    (hindependent : Independent T P) : P :=
  true_of_negation_unprovable T E hverify hindependent.2

theorem true_of_provable_of_sound {P : Prop} (T : Theory)
    (hsound : Sound T) (hproof : T.Provable P) : P :=
  hsound P hproof

end RHP2Bridge.MetamathematicalLedger
