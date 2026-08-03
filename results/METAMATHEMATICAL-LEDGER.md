# RH metamathematical branch: assumption ledger

This track studies provability status. It supplies no analytic evidence for or
against RH and does not treat “independent” as a third truth value.

## Three distinct levels

1. **Standard truth:** RH is true or false in the standard natural numbers.
2. **Formal sentence:** a particular arithmetic sentence `RH_F` is proved, in
   a specified base theory, equivalent to the chosen analytic statement.
3. **Provability:** ZFC proves `RH_F`, proves its negation, or proves neither.

Moving between these levels requires an explicit interpretation. It cannot be
done merely by calling the analytic statement “Pi-1.”

## Conditional finite-witness argument

Fix a theory `T` and a formal presentation satisfying both:

- semantically, `not RH_F` holds exactly when some natural number `n` passes a
  decidable counterexample checker `C(n)`;
- for each actual `n` with `C(n)`, `T` verifies the finite computation and
  proves `not RH_F`.

Then, in the ambient metatheory,

    T does not prove `not RH_F`  ==>  RH_F is true.

Thus, if `RH_F` is independent of `T`, it is true but unprovable in `T`. This
does not prove independence, and it does not follow from consistency alone.
The kernel-checked abstract result is `true_of_independent` in
`RHBridge.MetamathematicalLedger`.

## Assumptions that must remain visible

- **Formalization bridge:** the arithmetic sentence is equivalent to analytic
  RH in the intended model.
- **Checker correctness:** the finite predicate represents a genuine
  counterexample, including bounds on transcendental constants.
- **Internal verification:** the theory proves checker-to-negation for each
  witness (normally uniformly in a weak arithmetic theory).
- **Metatheory/model:** “truth” refers to the ambient standard model.
- **Soundness, when used:** consistency, 1-consistency, omega-consistency, and
  arithmetic soundness are distinct hypotheses.

## Candidate routes, not completed bridges

Robin-type inequalities and other finite-check criteria make a Pi-1-style
arithmetization plausible: falsity would be witnessed by an integer. But a
publication-grade argument must encode divisor sums, logarithms, Euler's
constant, strict inequalities, certified rational bounds, and then prove the
equivalence in a named base theory. This repository has not completed that
work, so it does not currently claim “RH is Pi-1” as a formal theorem.

## Useful next lemmas

1. Choose one exact finite criterion and give a primitive-recursive rational
   certificate format for all real inequalities.
2. Formalize its checker and prove checker soundness.
3. Identify a weak arithmetic base theory supporting the equivalence proof.
4. Only then encode ZFC proof predicates and investigate nonprovability or
   relative consistency. Numerical Weil-form work does not address these.
