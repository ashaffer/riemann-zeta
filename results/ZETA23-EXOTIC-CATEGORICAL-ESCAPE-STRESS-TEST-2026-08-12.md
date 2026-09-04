# Exotic categorical escape stress test

Status: hostile scope expansion beyond the finite dagger/CPM four-lemma
grammar, 2026-08-12.  This note tests operator systems, sheaf and cosheaf
descent, derived and triangulated categories, Tannakian reconstruction,
noncommutative motives, index/K-theory, topoi, and enriched limits.  It gives
exact counterexamples to generic shortcuts and a ranked list of constructions
which could become real only after a new zeta-specific theorem.  It proves no
uniform zero-free strip, no failure of one, and no independence statement.

## 1. Verdict

No tested categorical formalism supplies order merely from its categorical
structure.  The genuinely different possibilities are narrower than their
vocabularies suggest.

```text
operator-system matrix amplification             SAME NEGATIVE LINE;
complete order embedding                         ORDER-EQUIVALENT;
nonfaithful CP quotient or relaxation             CAN FORGET THE MIRROR;

ordinary sheaf/cosheaf descent on support         MISSES CROSS RECTANGLES;
cross-aware descent on the pair groupoid          RETAINS THE OPEN CROSS TERM;
derived/hyperdescent of the same local data        CANNOT RECOVER OMITTED DATA;

bare derived or triangulated category             ORDER IS NOT INVARIANT;
dagger/weighted/polarized enhancement              REINTRODUCES THE SIGN GATE;

rigid/Tannakian duality and determinant one        DOES NOT IMPLY PURITY;
independent positive polarization                  REAL BUT RH-STRENGTH INPUT;

Morita/localizing/noncommutative motives           GENERICALLY ORDER-BLIND;
K-class of the negative spectral projection        EXACT BUT SPECTRAL-PROJECTION GATE;
Fredholm index or net spectral flow                TOO COARSE GENERICALLY;

topos/internal local positivity                    DOES NOT GIVE A UNIFORM CONSTANT;
forcing or internal truth alone                    NO STANDARD-ARITHMETIC TRANSFER;

strong/weak/trace limits                           CAN LOSE A MOVING NEGATIVE LINE;
Hilbert/C-star ultraproduct                        RETAINS IT;
norm-coherent corona or ultraproduct estimate      REAL, REQUIRES UNIFORM ARITHMETIC.
                                                               (1.1)
```

The strongest new structural observation is the descent diagnosis.  A
Hermitian kernel is data on ordered pairs, or on a pair groupoid.  A cover of
the one-variable support does not cover all cross rectangles.  Ordinary
local positivity can therefore glue perfectly while a remote cross morphism
carries the whole negative direction.  A factorization algebra, bisheaf, or
pair-groupoid sheaf which retains those rectangles is honest, but its missing
descent estimate is exactly the actual prime/collateral cross-term theorem.

The second genuinely different observation concerns asymptotic limits.
Strong and trace limits can discard a negative vector which moves with the
height.  A Hilbert ultraproduct retains that vector exactly.  This makes
ultraproduct/corona language a legitimate way to state the uniform problem,
but it does not sign the ultraproduct prime operator.  A transfer back to a
fixed strip needs the same uniform carrier-normalized estimate which is open
at finite height.

No construction below is a demonstrated escape.  The whitelist in Section
12 ranks research interfaces, not completed arguments.

## 2. Admission test for an exotic categorical proposal

A categorical reformulation is potentially substantive only if it specifies
all five of the following.

1. **Actual object.**  The object or morphism contains the actual completed
   finite-stage Weil/von-Mangoldt operator, not an abstract matrix sharing a
   few traces.
2. **Order interface.**  It either reflects positivity or identifies a
   quantitative defect whose sign is proved independently.
3. **Cross-place fidelity.**  Prime--prime, prime--pole, selected--collateral,
   and inter-scale products created by the construction are retained or
   bounded.
4. **Uniformity.**  The relevant norm, degree, cohomological amplitude,
   descent constant, or index pairing is uniform in height and support.
5. **Noncircular polarization.**  Any positive metric, unitary Frobenius,
   pure weight, or spectral projection is constructed from arithmetic data
   rather than postulated with the desired spectral consequence.

Failure of item 2 makes the functor forgetful.  Failure of item 3 makes it an
incomplete use of the explicit formula.  Failure of item 4 proves at most a
finite-height or moving-strip result.  Failure of item 5 hides RH or the
desired strip inside the categorical input.

## 3. Operator systems and complete matrix order

### 3.1 Matrix amplification does not dilute the mirror

For the normalized mirror, put

```text
M=m*(I+C*J),               m>0, C>1,
J=[[0,1],[1,0]].                                          (3.1)
```

At matrix level `q`, the operator-system amplification is

```text
M^(q)=M tensor I_q.                                      (3.2)
```

Its eigenvalues are

```text
m*(1+C),       m*(1-C),                                  (3.3)
```

each with multiplicity `q`.  Thus complete positivity does not average or
dilute the negative line; it repeats it.  A negative vector `e_-` gives the
negative vector `e_- tensor u` at every level.

More generally, for a self-adjoint element of a concrete operator system,
level-one positivity is already its usual operator positivity.  Requiring
positivity at all matrix levels becomes stronger for maps between operator
systems, not for the fixed scalar-level element `M` itself.

### 3.2 Complete-order dichotomy

Let `Phi:S->T` be unital completely positive.

* If `Phi` is a complete order embedding on the operator system containing
  the completed form, then

  ```text
  Phi(M)>=0 iff M>=0.                                    (3.4)
  ```

  It is an exact representation change.
* If `Phi` is not order-reflecting, output positivity does not prove input
  positivity.  The diagonal conditional expectation gives the mirror
  counterexample

  ```text
  Phi(M)=m*I>=0,          M not >=0.                     (3.5)
  ```

Matrix convex lifts and free spectrahedral relaxations have the same
boundary.  An exact lift whose projection reflects positivity is equivalent
to the original sign problem.  A relaxation can contain the mirror.  A
noncommutative Positivstellensatz would be genuine only if the **actual**
translation/prime relations supplied a uniform-degree sum-of-squares
certificate with a uniform margin.  Neither complete positivity nor the
abstract operator-system axioms supply such a certificate.

### 3.3 Matrix-level separation returns a vector state

The finite PSD cone is self-dual.  If `M` is not PSD, a rank-one state
`z z^*` separates it:

```text
Tr(M z z^*)=z^*Mz<0.                                   (3.6)
```

Allowing matrix-valued states does not improve existence of a negative
witness for one Hermitian element; purification returns to an ordinary
vector in a larger tensor product, and (3.3) retains the same negative
factor.  Operator-system language can organize relations among several
noncommuting prime translations, but any gain must come from those actual
relations, not from matrix amplification.

## 4. Sheaves, cosheaves, and factorization descent

### 4.1 Exact failure of ordinary local descent

Let

```text
E_12=span(e_1,e_2),              E_23=span(e_2,e_3),
A_0=I_3,
A_c=I_3+c*(e_1 e_3^*+e_3 e_1^*),       c>1.              (4.1)
```

The restrictions to the two-set cover agree exactly:

```text
A_0|E_12=A_c|E_12=I_2,
A_0|E_23=A_c|E_23=I_2,                                  (4.2)
```

and their restrictions to the overlap `span(e_2)` also agree.  Nevertheless

```text
spec(A_0)={1,1,1},
spec(A_c)={1+c,1,1-c}.                                  (4.3)
```

Thus one global lift is positive and the other is not PSD, although every
ordinary local object and every overlap datum is identical.  The forgotten
morphism is the cross term between the disjoint pieces `e_1` and `e_3`.

This example is the sheaf-theoretic core of the triangular-packet no-go.  It
is stronger than saying that a particular partition of unity has a large
error: the restriction functor itself is not faithful on Hermitian kernels.

### 4.2 A quadratic form lives on the pair groupoid

For a support space `X`, a kernel `K(x,y)` is data on `X x X`.  If
`X=U union V`, then

```text
X x X=(U x U) union (U x V) union (V x U) union (V x V).  (4.4)
```

Ordinary positivity on `U` and `V` sees only `U x U` and `V x V`.
The cross rectangles `U x V` and `V x U` contain the coherent translations
and selected/collateral interactions.  They are not intersections in the
ordinary cover of `X`; no sheaf axiom reconstructs them from diagonal
restrictions.

A faithful categorical object must therefore be one of the following:

* a sheaf or operator-valued kernel on the pair groupoid;
* a bisheaf on `X x X`;
* a factorization algebra with explicit structure maps for disjoint pieces;
* an enriched cosheaf whose gluing data include every cross pairing.

Each is legitimate.  None signs the cross rectangles automatically.  For
the completed Weil kernel, bounding their operator norm or proving their
orientation is precisely the nonlocal prime/collateral gate.

### 4.3 Derived descent does not recover omitted cross data

Applying Cech cohomology, hyperdescent, or a derived functor to the local
diagram in (4.2) cannot distinguish `A_0` from `A_c`: their input diagrams
are literally equal.  A derived enhancement can store the missing cross term
only after it is inserted as an extension or higher cochain.  Computing the
sign of that extension is then new input.

This leaves one real sheaf-theoretic lead: find a zeta-specific decay,
nuclearity, or positivity theorem for the cross-rectangle structure maps.
That would be a substantive proof of the open transverse estimate, not a
formal consequence of descent.

## 5. Derived and triangulated categories

### 5.1 Positivity is not a derived invariant without extra structure

Let

```text
C: 0 -> C --1--> C -> 0                               (5.1)
```

be the two-term contractible complex.  It is isomorphic to the zero object
in the ordinary derived category.  Every chain endomorphism of `C`, including
the degreewise negative identity, therefore becomes the zero morphism after
passing to the derived category.  Chain-level negative order has disappeared.

Even more simply, the forgetful functor from Hermitian complexes to
`D^b(Vec_C)` sends

```text
(C^2,I_2)       and       (C^2,diag(1,-1))             (5.2)
```

to the same one-term underlying complex.  Any invariant factoring through
that forgetful functor cannot decide positivity.

### 5.2 What an honest enhancement must retain

A dagger dg-category, a category with duality, or a weighted/polarized
t-structure may retain chain-level forms.  Then there are two possibilities.

1. Quasi-isomorphism or homological reduction is order-reflecting.  The
   negative class persists and the construction is conservative.
2. Contractible or extension sectors are discarded.  A negative carrier can
   live in such a sector, as (5.1) shows, and an observability theorem is
   needed.

Mapping cones of positive rows can encode the quotient constraint elegantly,
but the induced Hodge reduction is the same positive-block Schur complement.
Distinguished triangles make Euler characteristics additive; they do not make
the signature positive.

### 5.3 Stable Witt information is too coarse

Let `H=<1> direct_sum <-1>` be a hyperbolic Hermitian plane.  In the Witt
group,

```text
[<1>]=[<1> direct_sum H],                              (5.3)
```

although the first representative is positive and the second is indefinite.
Witt stabilization deliberately forgets hyperbolic positive/negative pairs.
If one supplements the Witt class by exact rank, signature, and nullity in
finite dimension, one recovers the inertia and hence the original sign
problem.  There is no intermediate free positivity theorem.

A hypothetical motivic weight structure plus an independently positive
polarization remains a real conceptual route; it belongs with the
Tannakian discussion below, not with bare triangulated formalism.

## 6. Tannakian reconstruction and polarization

### 6.1 Exact rigid-duality counterexample

Fix `r>1` and put

```text
F_r=diag(r,r^(-1)),            J=[[0,1],[1,0]].         (6.1)
```

Then

```text
det(F_r)=1,
F_r^T J F_r=J.                                          (6.2)
```

Thus `F_r` has determinant one, reciprocal eigenvalue symmetry, a rigid
self-duality, and an invariant nondegenerate bilinear form.  Its eigenvalues
are nevertheless off the unit circle.

This is the finite tensor-category model of the familiar warning that
functional-equation duality is not purity.  A rigid tensor category and a
fiber functor can reconstruct the symmetry group and reciprocal spectrum;
they do not turn the indefinite form `J` into a positive polarization.

### 6.2 Positive polarization is exactly the nonformal input

Suppose instead there were a positive definite `H` with

```text
F_r^* H F_r=H.                                         (6.3)
```

For an eigenvector `v` of eigenvalue `lambda`,

```text
(abs(lambda)^2-1)*v^*Hv=0,                             (6.4)
```

so every eigenvalue would have modulus one.  Equation (6.3) is impossible
for (6.1).

Consequently a Tannakian route to RH, or to an annular bound corresponding
to a fixed strip, must construct a positive polarization or a quantitative
replacement from the actual arithmetic category.  Postulating it is
circular at the spectral level.  This is exactly what makes the Weil
cohomological proof over finite fields powerful: purity comes from additional
geometric positivity, not from tensor rigidity alone.

For the Riemann zeta function, no accepted neutral Tannakian category with
the required global Frobenius, trace formula, and positive polarization is
currently part of this project.  Constructing one would be a genuine new
architecture and could transcend the finite Gabor obstruction.  It is also
far more than a categorical repackaging of the existing proof.

## 7. Noncommutative motives, Morita invariance, and traces

### 7.1 Morita/localizing invariants do not remember an element's order

Algebraic K-theory, cyclic-type invariants, and noncommutative motives are
typically stable or Morita invariant.  The positive cone of a selected
self-adjoint element is not determined by the ambient algebra's Morita class.

For an exact finite example, both

```text
U_+=I_3,                 U_-=diag(-1,-1,1)              (7.1)
```

have determinant one.  Hence they define the same algebraic class under
`K_1^alg(C) isomorphic to C^*`; both are also trivial in topological
`K_1^top(C)=0`.  Yet `U_+` is positive and `U_-` is not PSD.  The ordinary
Fredholm index is zero for both as well.

Similarly, trace information alone is not order-reflecting:

```text
Tr(I_2)=Tr(diag(3,-1))=2,                              (7.2)
```

while only the first matrix is PSD.  The repository's flat-defect theorem
strengthens this from one trace to the exact first two Zeta23 moments while
hiding the negative line from a long range of principal subobjects.

### 7.2 Categorical trace limits can lose finite-rank defects

Let

```text
A_N=I_N-2*e_N e_N^*.                                   (7.3)
```

Every `A_N` has a negative eigenvalue `-1`.  With normalized trace `tau_N`,

```text
tau_N(A_N^k)=1                     for even k,
tau_N(A_N^k)=1-2/N ->1             for odd k.          (7.4)
```

Thus the full limiting noncommutative moment distribution is the positive
point mass at `1`, despite a negative line at every stage.  Fixed-degree
categorical characters, cyclic traces, or limiting free distributions do not
control a moving spectral edge.

### 7.3 The negative spectral K-class is exact but not free

For an invertible finite Hermitian `A`, let

```text
P_-(A)=1_((-infinity,0))(A).                            (7.5)
```

The class `[P_-(A)] in K_0(C)=Z` is its negative index, and it vanishes
exactly when `A>0`.  This is a faithful invariant.  Constructing (7.5),
however, uses sign functional calculus, which is continuous only while a gap
at zero is retained, or a resolvent contour around the negative spectrum.  It
is the original spectral-projection-and-gap gate.

A genuinely new index route would need an arithmetic Fredholm module and an
index pairing computable directly from primes which equals the negative
spectral class without first constructing `P_-`.  No such pairing is supplied
by Morita invariance alone.

### 7.4 Net spectral flow is too coarse without a protected path

The scalar loop

```text
A_t=cos(2*pi*t),                 0<=t<=1              (7.6)
```

starts and ends positive, has total spectral flow zero, and is negative at
`t=1/2`: the two zero crossings cancel.  Hence a vanishing net index does not
exclude an intermediate negative sector.  If one proves a path stays
invertible and begins positive, its inertia is constant, but path
invertibility is then the desired exclusion theorem.

## 8. Topoi, internal logic, and the uniform quantifier

### 8.1 Stalkwise strict positivity is not uniform coercivity

Over the base `T in [1,infinity)`, consider the continuous family

```text
A_T=diag(1,T^(-1)).                                    (8.1)
```

Every stalk is strictly positive and locally has a positive lower bound.
Nevertheless

```text
inf_(T>=1) lambda_min(A_T)=0.                          (8.2)
```

Thus an internal or local statement

```text
for each T, locally there exists delta(T)>0             (8.3)
```

does not produce the external constant

```text
there exists delta_0>0 for every T.                     (8.4)
```

A uniform zero-free strip has the quantifier pattern (8.4), not (8.3).
Sheaf semantics can encode the varying bound honestly, but it does not
compactify a noncompact height parameter for free.

### 8.2 Enough points versus a forgetful site

For a continuous field of full C-star algebras over a space with enough
points, positivity is fiberwise.  Such a topos is conservative and returns
the original family of inequalities.  A site whose probes contain only
local packet subspaces can validate all local restrictions while missing the
cross term in (4.1).  The distinction is again order reflection, now at the
level of points/probes.

Forcing, Booleanization, or a proof in a nonstandard/internal complex field
does not automatically yield a theorem about the standard Riemann zeta
function.  One needs an absoluteness or transfer theorem for the fully
quantified analytic statement.  No such theorem here proves a strip or its
failure, and no ZFC-independence result is known.

Topos language may be useful for keeping the uniform quantifiers honest.  It
does not change them.

## 9. Enriched limits, ind/pro objects, coronas, and ultraproducts

### 9.1 Strong limits can lose the moving negative line

On `ell^2(N)`, let

```text
A_n=I-2*e_n e_n^*.                                      (9.1)
```

Each `A_n` has eigenvalue `-1` with eigenvector `e_n`.  For every fixed
`x in ell^2`, however,

```text
norm((A_n-I)x)=2*abs(x_n) ->0.                          (9.2)
```

Hence

```text
A_n -> I strongly,                                     (9.3)
```

and the positive strong limit has forgotten the negative state.  Weak,
strong-resolvent, fixed-vector, and normalized-trace convergence can all have
this defect.  This is an exact model for a bad packet whose direction changes
with height and dimension.

A norm limit behaves differently.  If `A_n->A` in operator norm and
`A>=delta I`, then `A_n>0` eventually.  Proving the required norm convergence
and a fixed `delta` is precisely a cofinal quantitative estimate, not a
formal property of the limit category.

### 9.2 A Hilbert ultraproduct retains the defect

Let `U` be a free ultrafilter.  In the Hilbert ultraproduct, the vector

```text
e=[(e_n)]_U                                             (9.4)
```

has norm one, and the ultraproduct operator satisfies

```text
[(A_n)]_U e=-e.                                        (9.5)
```

Thus the ultraproduct sees the moving negative line which the strong limit
loses.  This is a genuine advantage of the construction.

It is not yet an arithmetic escape.  To use (9.5) for the completed zeta
operators one must:

1. normalize every operator by the carrier scale;
2. prove uniform boundedness so the ultraproduct element exists;
3. identify the ultraproduct of the actual prime/pole/collateral decomposition;
4. prove a positive or transverse estimate there; and
5. establish a transfer principle with the required finite-stage
   quantifier.

Items 2--4 are the carrier-normalized actual remainder theorem in a different
language.  A strict standard margin in one fixed ultraproduct transfers only
to a set of stages belonging to its ultrafilter, not automatically to every
sufficiently large stage.  Eventual uniformity follows only if the argument
works for every free ultrafilter, or if an arbitrary hypothetical bad
subsequence can be placed in an ultraproduct and contradicted.  Without that
quantifier upgrade—or without a standard margin—the construction may prove
only an ultrafilter-large, infinitesimal, or subsequential statement.

### 9.3 Corona and asymptotic C-star categories

For uniformly bounded normalized operators, the quotient

```text
product_T B(H_T) / direct_sum_T B(H_T)                 (9.6)
```

removes norm-vanishing families while retaining a persistent carrier.  The
transverse class of the four-lemma consolidation belongs here only if

```text
sup_T norm(R_T)/K_T<infinity.                           (9.7)
```

Subcarrier rational, archimedean, and shallow-collateral terms vanish in the
quotient when their proved bounds apply.  A nearly equally deep collateral
pair or an actual-prime transverse component can remain.  If (9.7) fails,
the proposed class is not even an element of this bounded corona and a
bornological/filtered enlargement is required.

The corona therefore gives a clean *location* for the obstruction.  Its
order is not computed by passage to the quotient.

### 9.4 Ind/pro coherence

An inductive system of nested compressions can reflect positivity when every
vector is eventually represented and the forms are compatible.  The current
height-dependent Gabor operators are not compressions of one fixed bounded
operator with one fixed bad vector.  A pro-object which retains every stage
also retains every unresolved sign.  A colimit which identifies only fixed
vectors can lose the moving line as in (9.1).

Thus the useful question is not “limit or no limit,” but which states and
which norm enrichment the limit functor preserves.

## 10. Enriched Yoneda and probe completeness

The full Yoneda philosophy provides a final cross-check.

If one retains every vector-state probe `z:C->H`, then

```text
A>=0 iff z^*Az>=0 for every z.                         (10.1)
```

The full order-enriched probe functor is conservative, but (10.1) is exactly
the original positivity theorem.  Restricting to a smaller probe category can
make the arithmetic manageable, but it is valid only if the cone generated
by its rank-one effects is the full PSD cone or if a zeta-specific
observability theorem repairs the loss.

This describes the exotic constructions above uniformly:

```text
all probes/cross morphisms retained       conservative but not easier;
some probes/cross morphisms discarded     exact countermodels exist;
new higher invariant retained             its arithmetic value needs proof.
                                                               (10.2)
```

The third line is the only possible true escape from the finite four-lemma
grammar.  Tannakian polarization, an index pairing, or an ultraproduct margin
would qualify, but none is presently constructed for the actual zeta data.

## 11. What is genuinely outside the four-lemma grammar?

Most exotic operations reduce to the existing conservative/forgetful/
nonlinear classification once order and norm are made explicit.  Four
interfaces are genuinely additional rather than mere vocabulary.

1. **Positive polarization from external geometry.**  A new cohomology or
   Tannakian category could supply positivity not derivable from the finite
   completed operator.  The Lorentz example (6.1) shows exactly what must be
   added.
2. **Topological index pairing.**  A negative spectral class might be paired
   with an arithmetic cycle and computed without estimating every matrix
   coefficient.  This requires a Fredholm module and a nontrivial pairing;
   ordinary index/K-theory does not provide them.
3. **Cross-aware descent.**  A product-site or factorization object could
   exploit genuine arithmetic locality of the cross rectangles.  It must
   prove a quantitative sign/decay theorem for those structure maps.
4. **Compactness retaining moving states.**  Ultraproduct or corona methods
   can turn a height-dependent bad direction into one limiting state.  A
   uniform arithmetic law in that limit could be new; weak or trace limits
   are insufficient.

These are logical interfaces for breakthroughs, not evidence that a
breakthrough is already present.

Relative to the existing three-way frontier, item 1 is the independent
polarization route and item 3 is the transverse arithmetic route.  Item 4
is a stronger uniformity container, not a source of order by itself.  Thus
item 2--a genuinely computable arithmetic index pairing--is the only
potential **fourth engine** found in this stress test.  It is presently only
an interface: no nontrivial Fredholm cycle or prime-side index computation
has been constructed here.

## 12. Ranked whitelist

No item is green.  “Whitelisted” means structurally capable of adding new
information if its explicit entry ticket is proved.

### Rank 1: cross-aware operator-system or pair-groupoid descent

**Why it is closest:** it attacks the exact actual-prime/collateral remainder
without first asking for a new global cohomology theory.

**Entry ticket:** construct a faithful kernel/factorization object containing
all `U x V` cross rectangles and prove a carrier-scale sign, nuclearity, or
decay estimate uniform in height and target geometry.

**Failure mode:** omitting cross rectangles returns the exact matrices
(4.1)--(4.3); retaining them without estimating them merely renames the open
gate.

### Rank 2: carrier-normalized ultraproduct/corona compactness

**Why it is real:** (9.5) proves that it retains moving negative directions
which ordinary asymptotics lose.

**Entry ticket:** uniform boundedness of the normalized actual operator,
identification of its ultraproduct place decomposition, a strict standard
positive/transverse margin, and either an all-ultrafilter argument or an
arbitrary-bad-subsequence contradiction that yields eventual finite-stage
uniformity.

**Failure mode:** fixed-vector or normalized-trace convergence loses the
carrier; an infinitesimal ultraproduct margin gives no fixed strip.

### Rank 3: arithmetically polarized Tannakian/cohomological category

**Why it is transformative:** an independently positive polarization could
force spectral purity by (6.4) and bypass witness engineering entirely.

**Entry ticket:** an actual category for the Riemann zeta divisor, a trace
formula matching primes and zeros, and a noncircular positive polarization or
quantitative annular analogue.

**Failure mode:** rigid duality, determinant one, and functional symmetry
alone admit (6.1).

### Rank 4: nontrivial arithmetic index pairing

**Why it is logically distinct:** an index theorem can sometimes replace
pointwise spectral estimates by topology.

**Entry ticket:** a Fredholm module whose pairing detects the off-line
negative spectral class and whose prime-side value is computable and forced
to vanish or have the opposite sign.

**Failure mode:** ordinary `K_1`, Fredholm index, net spectral flow, or the
class of `P_-` itself is respectively blind, too coarse, or equivalent to the
original spectral projection.

### Rank 5: weighted/derived enhancement with genuine purity

**Why it remains possible:** a weight structure plus hard-Lefschetz-type
positivity could supply new geometry.

**Entry ticket:** the same noncircular weight and polarization data required
in Rank 3, together with an actual realization of the explicit formula.

**Failure mode:** bare derived localization kills contractible negative
sectors as in (5.1).

## 13. Ranked blacklist as free shortcuts

These constructions may remain useful organizationally or computationally.
They are blacklisted only as sources of a strip **without** an additional
arithmetic/order theorem.

```text
1. ordinary operator-system matrix amplification;
2. CP dephasing, matrix-convex relaxation, or nonfaithful quotient;
3. ordinary sheaf descent on one-variable support;
4. Cech/derived descent applied after cross data were omitted;
5. bare derived, triangulated, or stable-equivalence formalism;
6. Witt class without full inertia;
7. rigid/Tannakian duality without a positive polarization;
8. Morita-invariant motive, algebraic K-theory, or ordinary Fredholm index;
9. categorical trace, supertrace, or any fixed collection of normalized moments;
10. zero net spectral flow without a protected invertible path;
11. stalkwise/internal positivity without a uniform external constant;
12. forcing or nonstandard truth without a standard transfer theorem;
13. strong, weak, strong-resolvent, or trace-only asymptotic limits;
14. a corona class asserted without the boundedness in (9.7);
15. full Yoneda testing, which is exact but is the original positivity problem.
                                                               (13.1)
```

## 14. Consolidated recommendation

The category-theoretic search should not branch equally among all exotic
frameworks.  The most concrete next iteration is to place the completed
kernel on a product site or operator system which keeps separated packet
interactions as named morphisms, then ask for one quantitative theorem about
those morphisms.  In parallel, the carrier-normalized finite matrices can be
formulated in a C-star ultraproduct to verify that every proposed asymptotic
estimate actually controls moving bad states rather than only fixed vectors
or traces.

The polarized Tannakian and index routes are conceptually real but currently
architectural research programs, not near-term lemmas.  Bare sheaf, derived,
motivic, K-theoretic, topos, or limit language should not be counted as an
escape until it passes the five-item admission test in Section 2.

## 15. Cross-links

This stress test extends rather than replaces:

- `ZETA23-CATEGORICAL-CONSOLIDATION-FOUR-LEMMA-2026-08-12.md`;
- `ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md`;
- `ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md`;
- `ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md`;
- `CATEGORY-THEORETIC-SEARCH-PRUNING-REFEREE-AUDIT-2026-08-12.md`;
- `CATEGORY-THEORETIC-CONSOLIDATION-REFEREE-AUDIT-2026-08-12.md`;
- `ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md`;
- `TRIANGULAR-PACKET-CONE-NOGO.md`;
- `ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md`.
