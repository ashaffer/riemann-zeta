# Referee audit: categorical search pruning and positive routes

Status: **PASS AFTER PATCHES**, 2026-08-12.

This is a hostile mathematical audit of:

- `ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md`;
- `ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md`; and
- `ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md`.

The verdict applies to the exact finite-dimensional lemmas and to the stated
conditional asymptotic claims.  It is not a certification of a zero-free
strip, RH, a no-go theorem for all possible methods, or any ZFC-independence
claim.

## Audited exact claims

The following claims pass after the corrections recorded below.

1. **Relative probe-cone duality.**  For a real Hermitian subspace `V`, local
   compression positivity reflects global positivity on `V` exactly when the
   restricted local and global state cones have the same closed image.  The
   equivalent formulation

   ```text
   closure(C_J+V_perp)=closure(Pos(H)+V_perp)
   ```

   follows from cone polarity and the finite-dimensional bipolar theorem.
2. **CPM extreme-rank bound.**  For a complex Hermitian spectrahedron with
   `m+1` real affine equalities, an extreme point of rank `r` satisfies
   `r^2<=m+1`.  The perturbation space on its support has real dimension
   `r^2`.
3. **Filtered-functor rigidity.**  Uniformly bounded linear maps preserve
   `o(K_T)` families and therefore induce associated-grade maps.  Uniformly
   bounded left inverses reflect nonzero grade classes on their stated range.
4. **Cross-effect identity.**  Boolean-lattice Möbius inversion gives the
   exact expansion into all mixed cross-effects.  Cross-effects above degree
   `d` vanish for polynomial maps of total degree at most `d`.
5. **Shift-positive `K_0` obstruction.**  An additive `K_0` invariant placing
   every object of a triangulated category in a pointed cone vanishes, since
   `[X[1]]=-[X]` and both signs must lie in the cone.
6. **Sparse-moment invisibility.**  A uniformly bounded `o(N)`-rank
   perturbation changes each fixed normalized moment by `o(1)`; every mixed
   word containing the perturbation has rank `o(N)` and uniformly bounded
   norm.
7. **Operator-system order claims.**  Complete order embeddings reflect
   positivity; non-order-reflecting CP maps can erase the mirror; positive
   recovery is sufficient for level-one order reflection, and CP recovery is
   sufficient at all matrix levels.
8. **Stinespring covariance.**  For a unital CP map,

   ```text
   [Phi(a_i* a_j)-Phi(a_i*)Phi(a_j)]_(i,j)>=0.
   ```

   This is the Gram matrix of the Stinespring defect.  It is a multiplicative
   Kadison--Schwarz defect, not an additive cross-effect of the linear map.
9. **Quotient-row obstruction.**  Projection modulo
   `im(X*)+C a` gives the exact exterior transversality class, and the leverage
   formula is the standard Gram-determinant identity.
10. **Carrier-slice support bound.**  A positive state cancelling an aligned
    negative carrier forces a positive remainder pairing of carrier size; the
    support functional over the specified compact convex slice is an SDP and
    is bounded by the positive-part norm of the compressed remainder.
11. **Mosco claims.**  Vanishing lower-bound defects transfer positivity to a
    Mosco limit via a strong recovery sequence.  A weakly escaping sequence
    with uniformly negative form value violates the Mosco liminf condition.
12. **Approximate polarization.**  The Loewner defect

    ```text
    -epsilon G <= A*G+GA-G <= epsilon G
    ```

    implies `abs(Re(lambda)-1/2)<=epsilon/2` for every eigenvalue.  The
    multiplicative analogue gives the stated annular bound.
13. **K-theory and limits.**  The finite negative spectral projection records
    the exact negative index but requires a gap-dependent spectral
    projection.  A Hilbert ultraproduct retains the moving negative vector,
    whereas strong and normalized-trace limits can lose it.

## Corrections made during audit

### Search grammar report

- Qualified the CPM optimization conclusion: rank-one attainment requires a
  compact trace-normalized feasible set and a linear objective.
- Replaced the ambiguous “polynomial functor” assertion by the exact
  polynomial-map statement and made the affine functional-calculus argument
  explicit.
- Qualified the fitted equation `A*G+GA=G`: existence of `G>0` is equivalent
  in finite dimension to critical-line spectrum **and diagonalizability**, so
  it also contains a semisimplicity condition.
- Clarified the tensor expression in the partial-trace counterexample.

### Exotic escape report

- Corrected the sign-functional-calculus wording: continuity is retained only
  while the gap at zero remains open.
- Corrected the ultraproduct quantifier.  A standard margin in one fixed
  ultraproduct transfers only to an ultrafilter-large set of stages.  Eventual
  uniformity needs an all-ultrafilter theorem or a contradiction for every
  arbitrary bad subsequence.
- Added this quantifier requirement to the ultraproduct whitelist entry.

### Positive-routes report

- Distinguished Stinespring covariance from additive cross-effects throughout.
- Corrected the operator-system formulation: order reflection on an arbitrary
  `V` is not automatically order reflection on the larger unital operator
  system generated by `V`; one must first enlarge and retest `V+R I`.
- Qualified the restricted-cone computation: non-PSD separation is not one
  unconditional SDP.  It becomes an SDP after fixing a candidate negative
  vector, or requires an equivalent certified cone-containment procedure.
- Replaced `||h||=1` by `||h||<=1` in the leverage supremum, making the exact
  identity valid in the one-dimensional degenerate case as well.
- Added the missing Hermitian, positivity, and support hypotheses to the
  carrier cancellation bound.
- Renamed the feasible “carrier face” a **carrier slice**; the inequality-cut
  spectrahedron is not generally a face in the convex-geometric sense.
- Expanded the Mosco recovery proof and qualified the fitted-metric statement
  for nonnormal matrices.

## Scope and residual obligations

The reports pass only with the following boundaries.

- The first-nonformal-node theorem is a bookkeeping theorem for its declared
  construction grammar.  It is not an impossibility theorem for mathematics
  outside that grammar.
- `GO` and `STOP` mean “pursue” or “stop as a free categorical shortcut.”  A
  construction can be revived by a genuinely new arithmetic estimate,
  polarization, order-reflection theorem, or conservative limit theorem.
- CP recovery is a sufficient constructive certificate, not a necessary
  condition for level-one order reflection.  Failure of its Choi SDP prunes
  CP recovery, not all positive or cone-duality arguments.
- Positive Stinespring covariance does not enter the completed Weil identity
  automatically.  The separate signed arithmetic identity labeled `(5.5)` is
  indispensable.
- Mosco, corona, and ultraproduct formalisms retain information only under
  their explicit boundedness, compatibility, gap, and transfer hypotheses.
- Approximate polarization proves a strip only after a zero-independent
  arithmetic generator, correct spectral identification, and uniformly
  controlled positive metric have been constructed.
- None of the three reports computes the actual transverse von Mangoldt class,
  excludes equally deep collateral cancellation, or proves a uniform strip.

## Final referee verdict

**PASS AFTER PATCHES.**  The exact lemmas are mathematically sound under their
now-explicit hypotheses, and the search-pruning recommendations are defensible
as scoped research triage.  Their publishable value remains methodological
until at least one zeta-specific recovery, transverse remainder, covariance
identity, independent polarization, or stable index theorem is proved.
