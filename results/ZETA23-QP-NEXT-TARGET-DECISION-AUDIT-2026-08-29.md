# QP next-target decision audit

**Date:** 2026-08-29

> **Superseded at the operator level.**  The later direct rank-one audit in
> `ZETA23-QP-WEIGHTED-GENERIC-DYADIC-RANK-ONE-AND-TAGGED-TRACE-TARGET-2026-08-29.md`
> shows that even generic `GACCT` is stronger than necessary: it is the
> maximum-row theorem created by rowwise Cauchy.  The minimal positive target
> is instead the global rank-one weighted dyadic tail `(WGDT_R)`, equivalently
> its globally weighted factorial/tagged-trace form.  The comparisons below
> remain valid only among the unweighted positive routes.

**Corrected verdict:** whole-star physical RDP is logically sufficient but
is not the right next project node.  It bundles two independent missing
assertions and is strictly stronger than the anchored row-sum theorem needed
by the operator.  The coefficient-large line theorem remains a useful local
classification lemma, but it does not transfer to the weighted anchored
tail without the very overlap/Carleson estimate still missing.  The best
next node is therefore the remaining-range generic anchored Carleson tail,
after the already closed coherent packet contribution is removed.

## 1. Three routes

### A. Small-coefficient selected-divisor theorem

This is the residual local problem after the coefficient-large theorem.
For a null-dual line pair it asks for

```text
N_U(p,gamma,mu)*N_V(p,eta,lambda) <<D q^o(1)
```

in the regime where all four integer coefficients have size below
`sqrt(D)q^o(1)` and one or both witness graphs are remote/non-affine.

* **Logical sufficiency:** not sufficient alone.  It controls every selected
  null line pair, but an arm may occupy many lines.
* **Tractability:** best of the three.  It is an exact, fixed-center
  simultaneous-divisor problem on two affine error planes.  Coefficient-large,
  affine-witness, transverse, and zero-height branches are already removed.
* **Falsifiability:** best.  Exact line populations, witness defects, heights,
  and product windows can all be scanned.  Literal remote examples exist
  (`4 x 3` at `q=809`), and the largest current actual-mask example is
  `10 x 8`; neither violates `O(D)`.

### B. Physical line cover or dominant-fan inverse

Together with A, either a `q^o(1)` line-pair cover or

```text
|U||V| <<q^o(1)*(D+M_null)
```

proves edgewise RDP and bypasses packet allocation.

* **Logical sufficiency:** sufficient only together with A.  A whole-star
  RDP theorem packages A and B and is sufficient by itself.
* **Tractability:** intermediate but substantially worse than A.  The
  determinant strip and all pointwise line-pair bounds do not imply it;
  transformed shell grids give `|U||V|~D^2` with `M_null=O(D)`.  The proof
  must aggregate the physical completion mask across many directions.
* **Falsifiability:** good for concrete cover rules and polynomial claims,
  weaker for an existential `q^o` theorem.  Current exact covers are at most
  six and the worst whole-star ratio is `1.26`, but bounded finite degrees
  provide little asymptotic evidence.

This is not literally the global affine allocation problem: it has one
central edge, scalar cardinalities, and no color reuse or integral host
rounding.  It is nevertheless another aggregation theorem, now internal to
one star.  Thus whole-star RDP bypasses global allocation logically while
repackaging a comparably essential local concentration gate mathematically.

### C. Mask-sensitive Carleson allocation

A joint host-extraction/allocation theorem can close the affine route
without RDP.

* **Logical sufficiency:** highest if it includes physical fan hosts,
  completion-consistent assignment, the mask dual inequalities, and integral
  rounding.  Allocation given unproved hosts is not sufficient.
* **Tractability:** lowest.  It is vector-valued over all colors and all
  completion items.  Canonical local peels already double-assign edges, and
  locally bounded packets can accumulate unbounded common-color load.
* **Falsifiability:** concrete algorithms are highly falsifiable by exact
  ledgers or the fractional dual.  A fully existential theorem is harder to
  kill because the admissible host family is itself part of the theorem.

## 2. Corrected recommended target

The exact operator target is not edgewise RDP.  For a fixed anchor `gamma`,
put

```text
r_gamma(eta)=#{p:p~gamma and p~eta},
P_gamma(R)=#{eta:R<=r_gamma(eta)<2R}.
```

The dyadic estimate

```text
R*P_gamma(R)<<Dq^o(1)                                (ACCT_R)
```

is equivalent, up to logarithms, to the sufficient neighbourhood-degree
sum `NDS`.  It permits harmless double stars on which RDP fails by a power.
Existing arguments already close bounded/subpower `R`, anchors of degree
`H<=D^(1/4)q^o(1)`, and

```text
R >> H^2/sqrt(D)q^o(1).
```

The coherent/parabolic high tail is also closed on the original rank-one
weighted route.  Thus the smallest main target is

```text
R*#{generic residual eta:R<=r_gamma(eta)<2R}
 <<Dq^o(1),                                           (GACCT_R)

H>>D^(1/4),
q^o(1)<<R<<min(sqrt(D),H^2/sqrt(D)).
```

This is strictly weaker than whole-star RDP, a dominant-fan theorem, or a
global affine packet allocation theorem, and it is exactly in the range not
already proved.

The coefficient-large theorem does **not** prove `(GACCT_R)`.  It controls
one selected null line pair inside one edge-star.  The left side of
`(GACCT_R)` sums incidences over many partners and many center neighbors of
one anchor.  Turning the pointwise line bound into this sum requires either
a bounded-overlap assignment or a weighted fan charge; that implication is
the missing Carleson theorem itself.  Consequently the coefficient-large
result should be used to delete/classify easy dyadic incidences inside a
future proof, not cited as an anchored-tail estimate.

## 3. Useful local sublemma, but no longer the main target

The following one-arm theorem is still a clean auxiliary target, strictly
smaller in variables and geometry than A.

> **Small-height selected-divisor line cap.**  Fix pairwise-coprime actual
> shell nodes `a,c,C`, a primitive direction `p=(p_1,p_2)`, put
> `mu=p_2*c-p_1*C`, and fix `gamma` with
> `max(|gamma|,|mu|)<sqrt(D)q^o(1)`.  Count actual-shell
> triples `(x,d,E)` satisfying
>
> ```text
> |x*d-a*c|, |x*E-a*C| <=D q^o(1),
> p_2*d-p_1*E=gamma,
> p_2*(x*d-a*c)-p_1*(x*E-a*C)=gamma*x-a*mu.
> ```
>
> Then the count is `O(sqrt(D)q^o(1))`.

The last displayed equation is redundant algebraically but records the
selected-divisor plane that a proof must retain.  The theorem is sharp on
the affine transition grid.  Applying it once to each arm proves A
immediately.  It proves neither `(ACCT_R)` nor `(GACCT_R)`, so it should be
pursued as a fast falsifier/local input rather than the main project node.

A still more diagnostic intermediate is a **few-bends theorem**: ordered
witness points on such a line can be partitioned into `q^o(1)` affine
witness runs.  The proved quadratic curvature bound then gives the one-arm
cap.  A growing family with polynomially many genuine witness bends would
falsify this route early.

## 4. Ranking

```text
Main-project relevance:          remaining GACCT_R > A > B > global C
Standalone logical economy:      GACCT_R > whole-star RDP > A or B alone
Local tractability:              A > GACCT_R > B >> global C
Fast falsifiability:             A > concrete GACCT_R/B > existential C
```

The full neighbourhood-degree-sum occupied-cell theorem is still broader
than necessary because several of its dyadic ranges and its coherent
weighted contribution are already closed.  The generic remaining-range
tail `(GACCT_R)`, rather than full NDS or RDP, is the corrected next node.
