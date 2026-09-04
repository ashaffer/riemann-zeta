# Generic GACCT is not necessary in the abstract directed-pair class

Date: 2026-08-29

## Verdict

Cardinal `(GACCT_R)/(GP_R)` is a clean sufficient theorem, but it is not
necessary for the rank-one four-cycle estimate at the level of masked
directed-pair incidence.  An exact scalable model has generic-like
line-free, all-distinct-secant rich fibers and

```text
max W / D asymp sqrt(D),
R*P_gamma(R)/D=sqrt(D),
```

while its exact rank-one energy norm is only `D/4`.  The separation comes
from color geometry: every row neighborhood is a partial directed matching.

This is not an actual-prime QP counterexample.  It proves that the main
target should be stated in weighted `(AF_2)/(AF_3)` or `(SRH_R)` form;
cardinal `(GP_R)` should be retained as a stronger fallback unless physical
completion constraints are proved to make the two comparable.

## 1. Directed-parabola construction

Let `p` be an odd prime and put `D=p^2`.  Take the left rows to be
`L=F_p^2`.  On the right take one anchor `gamma_*` and `p^2` partners
`eta_(a,b)`, `(a,b) in F_p^2`.  Join the anchor to every row and put

```text
(x,y) ~ eta_(a,b)  iff  y=x^2+a*x+b  in F_p.       (1.1)
```

The exact incidence counts are

```text
# rows                         =p^2=D,
# partners                     =p^2=D,
deg(gamma_*)                   =p^2=D,
deg(eta_(a,b))                 =p=sqrt(D),
degree of every left row       =p+1.
```

Two distinct translated parabolas meet in at most one point.  A line meets
one parabola in at most two points.  Moreover its ordered secants are all
different: for `t!=s`,

```text
(t-s, f(t)-f(s))=(h,h(t+s+a)),
```

and `h` together with the second coordinate recovers ordered `(t,s)` because
`2` is invertible.  Thus every anchor-partner common-neighbor fiber has
line occupancy two and exactly `p(p-1)` distinct ordered secants.

There is also a shell-comparable rank-one matrix realization of the same
local secant signature.  Put `M=p+1`, take `t=M+1,...,M+p`, and let

```text
u_t=(M^2+t^2,Mt),        v_t=(M^2,Mt),
X_t=u_t v_t^T.
```

All four factors are comparable.  The matrices obey

```text
det X_t=0,                  (X_t)_11-(X_t)_22=M^4.
```

They span the full three-dimensional pinned hyperplane: after constants are
removed their coordinates contain `t,t^2,t^3`.  For `t!=s`,

```text
det(X_t-X_s)=M^4(t-s)^2(ts-M^2)!=0.                (1.2)
```

The secant itself recovers `t-s` and `t+s`, so all ordered matrix secants
are distinct.  This strengthens “no rich line” to the generic fixed-pair
signature that defeats every fixed-secant multiplicity estimate.  It does
not assert that the matrices satisfy the QP hard completion map or that a
physical successive-minima ledger would certify them as generic.

## 2. Cardinal failure

For every partner,

```text
r_(gamma_*)(eta_(a,b))=p.
```

Consequently the scale `R=p` has

```text
P_(gamma_*)(p)=p^2=D,
R*P_(gamma_*)(R)=p^3=D^(3/2).                      (2.1)
```

The complete anchored degree sum is

```text
W(gamma_*)=sum_(row~gamma_*) deg(row)
          =p^2(p+1)=D(sqrt(D)+1).                  (2.2)
```

Both `(GP_R)` and `(NDS)` therefore fail by a square-root power.

## 3. Exact rank-one energy remains sharp-safe

Assign every right vertex, including the anchor, a different directed color
pair `(u_j,v_j)`.  All `u_j` lie in one mask, all `v_j` in a disjoint mask,
and no color is reused.  For a coefficient vector `z`, the transition form
on a row `ell` is

```text
T(z)(ell)=sum_(j:ell~j) conjugate(z_(u_j))*z_(v_j).
```

Since each row sees a subset of one global directed matching, Cauchy and
AM--GM give

```text
|T(z)(ell)|^2
 <=(sum_(j~ell)|z_(u_j)|^2)(sum_(j~ell)|z_(v_j)|^2)
 <=||z||_2^4/4.
```

There are `D` rows, hence

```text
||T(conjugate(z) tensor z)||_2^2 <=D/4 ||z||_2^4. (3.1)
```

This constant is exact: support `z` only on the anchor's two colors with
equal squared masses.  The anchor occurs in every row, and equality holds
in `(3.1)`.

There is no contradiction with the proved equivalence of `(WNDS)` and
`(NDS)`.  `(WNDS)` bounds the **positive Schur majorant**
`sum_gamma W(gamma)x_c x_C`; it is not a necessary lower bound for the
actual squared row sums.  In this model the majorant loses the matching
orthogonality by precisely the power seen in `(2.2)`.

## 4. Relation to the existing countermodels

* The directed-matching double star separates edgewise `(RDP)` from NDS,
  but its NDS value is `O(D)`.  It does not test necessity of `(GP_R)`.
* The Paley difference mask has degree and codegree of order `p`; at the
  physical normalization `D asymp p^2`, its anchored mass is of order `D`.
  It saturates rather than violates the cardinal target.  Its hard-window
  embedding uses ordinary integers, not actual prime powers, and was built
  to expose scalar projective loss.
* The Latin and Sidon--Cayley fixtures concern packet participation and
  attain their `D^2` A4 target.  They do not separate NDS from rank-one
  energy.
* The tagged product-of-parabolas example is the closest precursor: it has
  line-free fibers and excessive zero-tag factorial mass.  The construction
  above adds the missing original-color directed-pair labels and shows that
  their matching geometry can make the actual rank-one form small.

## 5. What a physical lift would still have to satisfy

The model deliberately respects several known scalar ceilings:

```text
anchor degree D, partner count D, codegree sqrt(D),
one point per prospective anchor determinant layer,
pairwise partner codegree <=1,
line occupancy 2 and R^2 distinct full-rank secants.
```

Thus determinant-layer injectivity, the pointwise `sqrt(D)` theorem, and
fixed-secant divisor bounds alone cannot establish necessity of `(GP_R)`.

It omits the genuinely physical constraints:

1. its finite-field selector is not generated by the unique hard completion
   map, and it provides no common actual-prime-power witnesses;
2. it does not impose the shell cubic windows, pairwise prime-power
   coprimality, or the physical signed relation matrix;
3. it does not include all cyclic/permutation edges forced by one physical
   triple--extra positive rows could destroy the matching certificate;
4. around every high-degree physical edge, the six-product identity and
   CDLS theorem force projected rich-line mass.  The present abstract labels
   only the common-neighbor fibers and supply no compatible projected-arm
   coordinates;
5. its disjoint color matching is combinatorially legal but has not been
   shown compatible with `p^3` simultaneous completion incidences.

The Paley hard-window fixture warns against claiming that product windows
alone automatically destroy arbitrary selectors.  At present the actual
prime/witness mask and cyclic closure, not a proved abstract incidence law,
are the credible obstructions to a lift.

## 6. The finite experiment that separates weighted from cardinal routes

The two routes must be evaluated on the **same** growing physical generic
dyadic block.  For each anchor and power-rich scale `R`:

1. serialize every common-completion chain with its original ordered color
   pair, witnesses, product-matrix secant, pinned tag, reciprocal height,
   and exact positive factorial weight;
2. remove only the already certified coherent/parabolic weighted part;
3. record the cardinal quantity
   `C_card=R*P_gamma^gen(R)/D`;
4. on the identical residual terms, certify the rank-one/weighted quantity
   using `(AF_2)/(AF_3)`, `(SRH_R)`, or an A4-style exact packet
   primal--dual bracket;
5. freeze the incidence and geometry and compare three color-label controls:
   the actual labels, an injective directed-matching relabel, and a
   maximal-reuse relabel.

The relabel controls leave `C_card` unchanged.  A large separation in the
weighted certificates measures exactly the information discarded by
`(GP_R)`.  The decisive physical outcome is one of:

```text
C_card grows, weighted actual-label constant stays O(1): GP_R unnecessary;
weighted and cardinal constants track each other: physical labels restore GP_R;
both grow: a genuine obstruction to the sharp bound/weighted route.
```

Current materialized graphs, whose generic codegrees are at most six, cannot
run this test in the unresolved power-rich range.  Another cardinal cover or
line-count scan would not distinguish the alternatives.

Replay:

```text
python3 results/verify_zeta23_qp_gacct_nonnecessity_directed_parabola_affine_falsifier.py
```
