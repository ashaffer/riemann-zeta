# A categorical search grammar for the uniform-strip program

Status: exact finite-dimensional lemmas, asymptotic bookkeeping under stated
boundedness hypotheses, and a scoped search-space classification, 2026-08-12.
This note refines the four-lemma categorical consolidation into a decision
procedure for future proposals.  It proves neither a uniform zero-free strip,
its failure, nor an impossibility theorem for RH.

## 1. Verdict: what the second categorical pass adds

The earlier consolidation showed that the current completed Weil/Gabor
obstruction is controlled by an aligned carrier class and that most attempted
adapters are conservative, forgetful, or nonlinear.  A second pass yields five
sharper conclusions which materially change the search strategy.

1. **Probe generation should be tested relative to the actual operator
   system.**  Local probes need not generate the whole matrix positive cone.
   They need generate the same positive functionals as all states only after
   restriction to the carrier-grade space of completed zeta operators.  This
   is a strictly weaker and exactly testable target.  Ordinary interval probes
   already fail on a Toeplitz envelope, but a smaller coefficient-specific
   operator system remains a legitimate place to seek an order-reflection
   theorem.
2. **Uniformly filtered functors cannot create carrier-grade
   transversality.**  A uniformly bounded change of representation induces a
   functor on the carrier associated grade and sends an aligned class to an
   aligned class.  An inverse uniformly bounded on the relevant range also
   reflects the class.  An unbounded adapter can promote a subcarrier error,
   but the required norm or condition-number growth is then the new
   quantitative theorem; the gain is not categorical.
3. **Derived positivity has a precise shift obstruction.**  An additive
   invariant which factors through the Grothendieck group of a triangulated
   category and assigns every object to a proper positive cone must vanish:
   the shift represents the negative class.  Thus a supertrace, Euler
   characteristic, or derived decategorification cannot itself be the positive
   polarization.  A viable cohomological search must work in a heart or pure
   weight piece and construct a separate positive dagger there.
4. **Nonlinear methods have an exact cross-effect budget.**  The failure of a
   nonlinear functor to preserve the place sum is not an informal warning.  By
   finite-difference polarization, its value on the completed sum is the sum
   of its one-place values and all nonzero mixed cross-effects.  A degree-`d`
   polynomial method asks for correlations through order `d`.  This makes a
   target-adaptive quadratic cross-effect the cheapest nonlinear survivor;
   moving to higher degree without a structural vanishing theorem expands the
   arithmetic burden.
5. **Bulk information and a sparse exceptional carrier live in different
   quotients.**  Normalized traces and any fixed collection of bounded-degree
   moments are asymptotically insensitive to uniformly bounded `o(N)`-rank
   perturbations.  A one-pair uniform-strip obstruction can lie in that
   negligible ideal.  Density or bulk-moment improvements must therefore be
   paired with a rank-one-sensitive norm, leverage, index, or carrier-state
   theorem; more bulk information of the same kind is not the missing arrow.

These points expand two directions and prune many others.  The expanded
directions are:

- a **relative probe-cone theorem** on the actual carrier-grade operator
  system;
- an **actual transverse-class computation** in the bounded corona or the
  correct larger Rees grade;
- a **minimal quadratic cross-effect theorem** for actual von Mangoldt
  coefficients;
- a **heart-level, independently polarized global object** rather than a
  derived/supertrace reconstruction; and
- a **sparse-defect-sensitive relative index** in a topology which retains one
  remote carrier.

Everything below explains exactly why these are the surviving categories.

## 2. The ordered and filtered categorical container

### 2.1 Finite stage

Let `FHilb` be the dagger category of finite-dimensional complex Hilbert
spaces.  Over `H` retain

```text
Herm(H)={A:H->H : A*=A},        Pos(H)={A:A>=0}.       (2.1)
```

A morphism `S:E->H` acts contravariantly by dagger pullback

```text
S^!A=S* A S.                                          (2.2)
```

Positive states are matrices `Gamma>=0`, paired with Hermitian effects by

```text
<A,Gamma>=Tr(A Gamma).                                (2.3)
```

This is an ordered Hermitian fibration over `FHilb`, not merely the bare
dagger category.  The `CPM` completion adds positive states, channels,
purifications, and discarding.  The dagger Karoubi envelope splits projections
and hence represents positive-null feasible faces.

At a finite admissible packet stage, after invoking the relevant explicit
formula or declared literature interface, the completed identity is an
equality of Hermitian effects

```text
K_comp=sum_v epsilon_v K_v=K_divisor.                (2.4)
```

The label `v` includes pole/main, gamma, rational, prime, selected-zero, and
collateral pieces.  Every functorial pullback preserves (2.4).  Positivity is
an additional order statement and does not follow from preservation of the
equality.

### 2.2 The marked carrier and its feasible object

Let `X_T:H_T->E_T` collect positive rows and let

```text
i_T:S_T=ker X_T -> H_T,       p_T=i_T i_T*.           (2.5)
```

On `S_T`, write `a_T` for the selected target row, `g_T` for the aggregate
row, and `K_T>0` for the selected carrier scale.  The exact isolated-pair
identity has

```text
[g_T]=lambda_T [a_T]                                  (2.6)
```

at the relevant carrier grade.  Its exterior obstruction is

```text
Omega_T=(p_T a_T) wedge (p_T g_T).                    (2.7)
```

For the isolated pair, `Omega_T=0`.  If the actual aggregate is

```text
g_T=lambda_T a_T+r_T,                                (2.8)
```

then `Omega_T=(p_Ta_T) wedge (p_Tr_T)`.  The actual remainder, not a change of
coordinates, is the only linear source of transversality.

### 2.3 Carrier filtration

For Hermitian families define

```text
F_K={A_T:||A_T||=O(K_T)},
F_<K={A_T:||A_T||=o(K_T)},
gr_K Herm=F_K/F_<K.                                  (2.9)
```

For uniformly bounded normalized morphisms one may instead work in the
corona C-star category

```text
Qcat=prod_T^bounded Hom(H_T,G_T) / c_0 Hom(H_T,G_T). (2.10)
```

The class

```text
tau=[p_T R_T p_T/K_T]                                (2.11)
```

is defined in (2.10) only if the normalized actual remainder is uniformly
bounded.  If it is not, it belongs to a larger filtered grade or to a
specified bornological/Rees completion.  The boundedness decision must come
before claims about `tau`.

### 2.4 The construction grammar

The audited grammar is generated by the following constructors.

```text
L  dagger-linear:
   pullback/congruence, dagger kernel, Karoubi retract,
   biproduct, tensoring with a finite positive ancilla;

C  completely positive:
   positive mixture, purification, channel, conditional expectation,
   partial trace, randomization, dephasing;

P  probe/localization:
   compression to local subobjects, translated packets, finite test banks,
   adaptive or predetermined minors;

M  monoidal/trace:
   tensor/Euler assembly, trace, supertrace, connected character,
   cumulant or logarithmic decategorification;

D  derived/homological:
   complexes, cones, higher differentials, passage to cohomology or K_0;

N  nonlinear/polynomial:
   determinant, exterior or symmetric power, polynomial functional
   calculus, resolvent, Schur/Feshbach, spectral projection;

Q  asymptotic/quotient:
   filtered colimit, strong or compact-open limit, Calkin/corona quotient,
   associated grade, completion in a chosen topology.                 (2.12)
```

A new method outside this grammar is not classified by this note.  Inside
the grammar, a selector depending on a bad zero, negative eigenvector, or
fitted metric is treated as an **external oracle** until it is constructed
from arithmetic data independently of the desired conclusion.

## 3. Information and order signatures

A construction should be assessed relative to the actual admissible class,
not only on all matrices.  Let `W_T subset Herm(H_T)` be a real operator
system containing the carrier-grade completed forms under consideration.
For a map `F_T` define four separate properties.

1. **Equality naturality:** it sends the two sides of (2.4) to equal outputs.
2. **Relative order reflection:** for `A in W_T`,

   ```text
   F_T(A)>=0  implies  A>=0.                          (3.1)
   ```

3. **Carrier faithfulness:** a normalized marked carrier does not become
   zero or subcarrier under `F_T`.
4. **Place additivity:** the value on `sum_v epsilon_v K_v` is determined by
   the separate one-place values without mixed cross-effects.

These properties are independent.  A pullback always has equality
naturality, but a proper compression need not reflect order.  A conditional
expectation is positive, but may kill the carrier.  A determinant detects
inertia in a selected block, but is not place-additive.

This leads to the following cost labels.

```text
O  relative order-reflection/observability theorem is owed;
R  carrier-grade transverse remainder theorem is owed;
X_d  mixed cross-effects through degree d are owed;
P  independent positive polarization is owed;
L  carrier-conservative limit/tightness theorem is owed.              (3.2)
```

The purpose of the grammar is not to ban a constructor.  It is to prevent a
constructor from being counted as payment of its own cost label.

## 4. Exact refinements of the four master lemmas

### 4.1 Relative probe-cone theorem

Let `W subset Herm(H)` be a finite-dimensional real subspace.  For probes
`j_i:E_i->H`, put

```text
C_J=closure cone{j_i Gamma_i j_i*:Gamma_i>=0}.       (4.1)
```

Let `r_W:Herm(H)->W*` be restriction of a state to `W`:

```text
r_W(Gamma)(A)=Tr(A Gamma).                           (4.2)
```

Then the following are equivalent.

1. For every `A in W`,

   ```text
   j_i* A j_i>=0 for every i  implies  A>=0.         (4.3)
   ```

2. The local and global state cones have the same closed image on `W`:

   ```text
   closure r_W(C_J)=closure r_W(Pos(H)).             (4.4)
   ```

Equivalently,

```text
W intersect C_J^*=W intersect Pos(H).                (4.5)
```

Here the last `Pos(H)` is identified with its self-dual cone.

#### Proof

For `A in W`, condition (4.3) on the probes is equivalent to

```text
Tr(A Gamma)>=0 for every Gamma in C_J.               (4.6)
```

Global positivity is equivalent to the same inequality for every
`Gamma>=0`, because the matrix positive cone is self-dual.  Thus (4.3) for
all `A in W` is equality of the two dual cones inside `W`, which is (4.5).
The bipolar theorem on `W*` makes this equivalent to (4.4).  QED

#### Why this changes the search

The earlier full-space criterion `C_J=Pos(H)` is sufficient but often much
too strong.  A zeta-specific local-to-global theorem only needs (4.4) for the
actual carrier-grade operator system `W_T`.  This suggests a concrete
program:

1. define `W_T` from the exact completed prime/gamma/pole displacement
   structure, before inserting the zero divisor;
2. project both the global state cone and the proposed probe cone to `W_T*`;
3. prove equality, or produce a separating element of `W_T`.

The triangular `3 x 3` example shows that ordinary interval/modulation probes
fail even on a nontrivial Toeplitz envelope.  It does not prove failure on the
smaller actual-coefficient operator system.  The latter is now a sharply
posed GO/STOP test rather than a vague gluing hope.

### 4.2 Karoubi completion, positive ancillas, and CPM rank

#### Karoubi completion does not manufacture a transverse arrow

In the dagger Karoubi envelope, a morphism

```text
(H,p)->(G,q)
```

has the form `q f p` for an already existing morphism `f:H->G`.  Therefore,
if

```text
p g=lambda p a,                                      (4.7)
```

then every further retract or pullback preserves this relation.  Splitting
the positive-null projection exposes the feasible object, but cannot create
`Omega!=0` from `Omega=0`.

#### A positive ancilla is conservative; discarding need not be

For Hermitian `A` and nonzero `B>=0`,

```text
A tensor B>=0  iff  A>=0.                            (4.8)
```

One direction is standard.  If `A` has a negative vector and `B` has a
positive eigenvector, their tensor has negative expectation.  Thus finite
positive stabilization is order-reflecting.

Partial trace is not.  Let `C=C*` be traceless and nonzero.  For sufficiently
large `t`,

```text
Z=I tensor I+t*(A tensor C)                          (4.9)
```

is indefinite for a suitable nonzero Hermitian `A`, while its partial trace
over the second factor is a positive scalar multiple of `I`.  Discarding an
ancilla may erase precisely the correlation which carried the sign.

#### Bounded-constraint CPM rank lemma

Consider the spectrahedron

```text
Gamma>=0,
Tr(B_j Gamma)=b_j,             j=0,...,m,            (4.10)
```

where one equation may be normalization.  If `Gamma` is extreme and has
rank `r`, then

```text
r^2<=m+1.                                             (4.11)
```

Indeed, Hermitian perturbations supported on `range Gamma` have real
dimension `r^2`.  If `r^2>m+1`, a nonzero perturbation annihilates every
constraint in (4.10), and sufficiently small positive and negative multiples
preserve positivity, contradicting extremality.

For trace normalization plus one real aggregate condition, `r=1`.  Therefore,
for a linear objective on this compact trace-normalized feasible set, an
optimum is attained at a rank-one state: a larger positive ensemble using the
same observables cannot improve that optimum.  Without compact normalization,
attainment, or linearity of the objective, this last optimization conclusion
does not follow from the rank bound alone.  An ensemble becomes a genuinely
new route only by introducing new independently controlled effects; the
number of labels or random seeds is not new information.

### 4.3 Filtered-functor rigidity

Let `F_T` be linear maps between normed morphism spaces and suppose

```text
sup_T ||F_T||<infinity.                              (4.12)
```

Then

```text
x_T=o(K_T)  implies  F_T x_T=o(K_T).                 (4.13)
```

Consequently `F=(F_T)` induces a map on `gr_K` and on the bounded corona
whenever it respects source and target composition.  If

```text
g_T-lambda_T a_T=o(K_T)                              (4.14)
```

with bounded `lambda_T`, then

```text
F_Tg_T-lambda_TF_Ta_T=o(K_T).                        (4.15)
```

Thus strict bounded filtered functors preserve carrier-grade alignment.

If, on the relevant range, there are left inverses `G_T` with

```text
sup_T ||G_T||<infinity,                              (4.16)
```

then the induced grade map is conservative: a nonzero carrier class cannot
map to zero.  Uniformly conditioned congruences are the primary example.

An adapter with `||F_T||->infinity` can promote a subcarrier term, but only
under the quantitative inequality

```text
||F_T|| ||x_T|| comparable to K_T.                   (4.17)
```

For a congruence, the transported metric or inverse carries the matching
condition-number cost.  Equation (4.17), together with control of every other
completed term, is a new estimate.  An unbounded functor is therefore a
possible coordinate for a breakthrough, but not a free escape from the
associated-grade obstruction.

This gives a practical first test for every preconditioner, scale filter, or
renormalization: compute its degree on the Rees filtration before computing
large matrices.  Degree-zero strict functors cannot create `tau`; positive
degree functors must pay and control the amplification ledger.

### 4.4 Cross-effect accounting theorem

Let `F` be any map from an additive real vector space to another, and first
replace it by the reduced map `F_0(x)=F(x)-F(0)`.  For a nonempty set
`S subset {1,...,n}`, define the mixed cross-effect

```text
cr_S F(x_i:i in S)
 =sum_(J subset S) (-1)^(|S|-|J|)
      F_0(sum_(j in J)x_j).                           (4.18)
```

Möbius inversion on the Boolean lattice gives the exact identity

```text
F_0(sum_(i=1)^n x_i)
 =sum_(nonempty S subset {1,...,n}) cr_S F(x_i:i in S). (4.19)
```

The second cross-effect is

```text
cr_2F(A,B)=F(A+B)-F(A)-F(B)+F(0).                    (4.20)
```

It vanishes for all pairs exactly when `F_0` is additive.  For scalar
functional calculus `F(A)=f(A)`, the dimension-one case then makes
`f-f(0)` additive; continuity makes `f` affine.  For a polynomial **map** of
total degree at most `d`, cross-effects of order greater than `d` vanish; the
lower mixed effects remain.  (A categorical functor called "polynomial" needs
its own degree definition before this finite-difference conclusion is used.)

For example,

```text
(A+B)^d-A^d-B^d
```

is the sum of noncommutative words containing both letters.  Exterior and
symmetric powers have the corresponding mixed polarization summands, and
determinant coefficients are their scalar traces.  Resolvents and Schur
maps have infinite or rational mixed expansions wherever defined.

Applied to (2.4), equation (4.19) is an exact arithmetic ledger.  A nonlinear
certificate has only three possibilities.

1. Its cross-effects vanish for a formal structural reason; then it reduces
   to a lower-degree or block-local construction and must still reflect the
   carrier.
2. It erases sign, as with square or absolute value; then it is forgetful.
3. Its nonzero cross-effects must be evaluated on actual prime, gamma, pole,
   and collateral pieces.  Their signs are new mixed arithmetic theorems.

This does not make nonlinear methods unpromising.  It ranks them by cost.
The target-adaptive `2 x 2` quotient Gram or completed determinant is the
minimal nontrivial degree and asks for a two-correlation theorem.  A method
of degree `d>2` should be pursued only when a symmetry kills most lower mixed
effects or known arithmetic estimates genuinely improve at that degree.

### 4.5 The derived shift obstruction and the trace-zero boundary lemma

#### Shift-positive K_0 invariants vanish

Let `T` be a triangulated category and let

```text
I:K_0(T)->V                                           (4.21)
```

be an additive invariant into a real vector space with a proper cone `C`, so
`C intersect (-C)={0}`.  Suppose

```text
I([X]) in C for every object X of T.                 (4.22)
```

Then `I=0` on all object classes.

Indeed, `X[1]` is also an object and

```text
[X[1]]=-[X] in K_0(T).                               (4.23)
```

Thus both `I([X])` and `-I([X])` lie in `C`, forcing `I([X])=0`.

This is the exact categorical obstruction behind attempts to obtain a
positive polarization from an Euler characteristic or supertrace.  A viable
cohomological construction must break the shift symmetry by selecting a
heart, a pure-weight sector, or a harmonic object, and then add a positive
metric not determined by the alternating trace.  The signed explicit formula
and the positive polarization should be modeled by different functors linked
by a separately proved compatibility theorem.

#### Positive trace-zero boundaries are trivial

In a finite C-star algebra with faithful positive trace `tr_f`,

```text
Z>=0 and tr_f(Z)=0  imply  Z=0.                      (4.24)
```

Every commutator has trace zero.  Therefore a positive commutator in this
setting is zero, and no strict positive-commutator estimate can arise from a
pure categorical boundary.  A nontrivial virial, Ward, or anomaly route must
identify an explicit boundary/leakage term, a failure of trace class, or an
infinite-volume anomaly and prove its sign.  Compression which hides the
compensating channel is a forgetful map, not such a proof.

Together, (4.23) and (4.24) prune broad searches for positivity inside
derived cancellation itself.  They positively redirect the search toward a
heart-level polarization or a controlled singular boundary term.

### 4.6 The sparse-defect quotient lemma

Let `dim H_N=N`, and let `A_N,R_N` be uniformly norm-bounded Hermitian
families with

```text
rank R_N=o(N).                                        (4.25)
```

For every fixed integer `k>=1`,

```text
(1/N)Tr((A_N+R_N)^k)-(1/N)Tr(A_N^k)->0.              (4.26)
```

#### Proof

Expand the difference into the finitely many noncommutative words containing
at least one `R_N`.  Each word has uniformly bounded norm and rank at most
`rank R_N`; hence its trace is `O(rank R_N)`.  Divide by `N`.  QED

Thus every fixed collection of normalized moments factors asymptotically
through the quotient by the low-rank negligible ideal.  There can exist a
positive `A_N` and an indefinite `A_N+R_N` with the same limiting data.  The
same information-loss statement applies to any invariant constant on a
defect ideal `J`: if `F(A+R)=F(A)` for `R in J`, no downstream function of
`F(A)` can exclude an indefinite perturbation in `J`.

The hypotheses of (4.25) are a model statement, not a claim that every
normalized Zeta23 block has uniformly bounded norm.  The project-specific
trace/Frobenius ledgers already establish the corresponding invisibility of
one or `o(N)` exceptional blocks at their actual normalization.  The
categorical conclusion is the same: bulk density lives in a quotient which
can forget the sparse carrier.

The escape is explicit.  Add a functor which is sensitive to the ideal:

- operator norm or least edge;
- selected leverage `u*A^dagger*u`;
- a carrier-state pairing;
- a relative Fredholm/index class with a proven gap; or
- moments whose order grows sufficiently fast, together with the resulting
  high-order arithmetic estimates.

This explains why the positive-density theorem is valuable but cannot be
iterated to a uniform strip merely by improving constants in the same bulk
moments.

### 4.7 Limit conservativity

Qualitative positivity on an algebraic filtered union is stagewise: if
forms and embeddings are exactly compatible and every vector belongs to a
stage, the colimit form is positive if and only if all stage forms are
positive.  This fact does not provide a uniform margin and does not turn a
finite list of stages into a cofinal proof.

Weaker analytic limits can lose a moving carrier.  On `ell^2`, put

```text
A_n=I-2 e_n e_n*.                                    (4.27)
```

Every `A_n` has eigenvalue `-1`, but `A_n` converges strongly to `I`.  Thus
strong-resolvent, compact-open, fixed-window, and weak-state limits require a
separate tightness or observability theorem.  Norm convergence with a uniform
gap is carrier-conservative; strong convergence alone is not.

A proposed index limit must therefore specify:

1. the topology or operator ideal;
2. the class representing one remote normalized carrier;
3. why that class is nonzero in the quotient;
4. convergence of the all-place arithmetic object in the same topology; and
5. gap/continuity hypotheses under which the index is stable.

Changing to a topology which sees the quartet but in which the Euler product
does not converge merely exchanges one unpaid `L` obligation for another.

## 5. Scoped categorical pruning theorem

### Theorem 5.1 (first nonformal node)

Fix a finite-stage completed identity (2.4), a feasible Karoubi object
`(H_T,p_T)`, a carrier scale `K_T`, and a real operator system `W_T` containing
the admissible carrier-grade forms.  Consider a certificate represented by a
finite syntax tree whose internal nodes are constructors from (2.12), and
whose leaves contain only:

- the completed equality;
- already proved positive rows and subcarrier estimates; and
- formal dagger, monoidal, trace, or homological structure.

Assume no leaf already contains the desired zero exclusion, a fitted negative
spectral projection, or a polarization constructed from the forbidden
divisor.  If the certificate excludes a marked carrier defect, then along
some branch of its syntax tree there is a first node which supplies at least
one of the following genuinely additional inputs:

```text
(O) relative order reflection on W_T or its carrier grade;
(R) a signed carrier-or-larger actual transverse remainder;
(X) control of a nonzero mixed cross-effect of a nonlinear constructor;
(P) an independently constructed positive polarization/heart;
(L) a carrier-conservative cofinal limit or stable relative index.     (5.1)
```

In particular, the constructors alone do not discharge (5.1).

#### Proof

Proceed upward through the syntax tree.

- Dagger pullbacks, uniformly filtered linear maps, biproducts, positive
  ancillas, and Karoubi retracts preserve the completed equality and the
  carrier alignment.  If they are relatively order-reflecting, the original
  order problem remains and label `(O)` is owed; if they are not, recovering
  the discarded direction requires `(O)` or `(L)`.  A nonstrict filtered map
  requires the quantitative remainder input `(R)`.
- Positive mixtures are states in `CPM(FHilb)`.  The aligned-face inequality
  survives purification and mixing, and the rank lemma shows that repeated
  copies of the same constraints add no information.  Cancellation retaining
  a carrier requires `(R)`.  A positive channel which discards the carrier
  requires relative order reflection `(O)` to recover it.
- Probe families reflect order exactly under the relative cone equality
  (4.4), which is `(O)`.
- A nonlinear node decomposes by (4.19).  If its cross-effects vanish, it
  reduces to lower-degree formal nodes.  If it erases sign, it cannot prove
  the antecedent order statement.  Otherwise a nonzero mixed term must be
  signed, which is `(X)`.
- A trace or derived node factors through a nonconservative
  decategorification.  The shift lemma prevents that signed invariant from
  being an objectwise positive polarization.  A successful lift therefore
  supplies `(P)` or returns to `(O)`.
- A limit or quotient node can lose a moving carrier as in (4.27).  Stability
  of order or index is precisely `(L)`.

Since the leaves contain none of these new inputs, a successful root must
have a first node at which one is added.  QED

### Scope

The theorem classifies a grammar, not all mathematics.  A new dynamical
inequality, arithmetic inverse theorem, geometric motive, probabilistic
rigidity theorem, or other structure may enter as a new leaf and lie outside
the grammar.  The theorem then asks the useful question: which item in (5.1)
does that structure actually supply?

## 6. Decision tree for new proposals

Use the following decision tree before investing in computation or Lean
formalization.

```text
START: What new datum is added beyond the completed equality?
  |
  +-- none; only a change of representation
  |     |
  |     +-- uniformly invertible/order-reflecting? --> equivalent problem;
  |     |                                             pursue only if an
  |     |                                             existing estimate fits
  |     |
  |     +-- compression/average/discard? -----------> test relative cone on W
  |                                                   or STOP
  |
  +-- positive witnesses/ancillas/randomness
  |     |
  |     +-- same effects and constraints? ----------> CPM rank bound; STOP
  |     |
  |     +-- new independently signed effect? -------> GO: identify its
  |                                                   carrier-grade class
  |
  +-- nonlinear detector
  |     |
  |     +-- sign-erasing? ---------------------------> STOP
  |     |
  |     +-- sign-preserving on full operator? -------> equivalent sign;
  |     |                                             new estimate required
  |     |
  |     +-- uses place decomposition? --------------> expand cross-effects
  |           |
  |           +-- actual mixed theorem available? --> GO
  |           +-- mixed terms unnamed/uncontrolled? -> STOP
  |
  +-- local/probe/gluing argument
  |     |
  |     +-- projected probe cone equals global cone
  |     |   on actual carrier-grade W? --------------> GO
  |     +-- counterexample inside W? ----------------> STOP
  |     +-- equality not tested? --------------------> make this the next task
  |
  +-- trace/cohomology/derived construction
  |     |
  |     +-- only K_0, Euler, supertrace, duality? ----> cannot supply order;
  |     |                                             STOP as polarization
  |     +-- independent heart/pure positive metric? -> GO; audit adjoint law
  |     +-- metric fitted from zeros/eigenvectors? --> detector only; STOP
  |
  +-- limit/index/completion
        |
        +-- topology kills a moving rank-one defect? -> STOP
        +-- arithmetic object fails to converge? ----> STOP
        +-- carrier survives and index is stable? ---> GO
        +-- either fact unproved? --------------------> that is the next task
                                                                    (6.1)
```

There is a second, scale-specific check for every branch:

```text
Is the proposed new term o(K), O(K), or larger than K?
```

- `o(K)` cannot alter the carrier-grade alignment.
- `O(K)` belongs in `tau` and requires its sign and target angle.
- a larger term moves the problem to a higher Rees grade and requires a
  normalization/sign theorem there.

Calling a term “global” or “categorical” does not answer this scale question.

## 7. Branches to prune or place at low priority

The following are closed as generic shortcuts within the grammar.  They may
still be useful coordinates after a new estimate is supplied.

### 7.1 More conservative adapters without a new estimate

Low priority:

- additional invertible preconditioners or metric changes;
- Schur, Feshbach, Hodge, Dirichlet-to-Neumann, or Birman--Schwinger rewrites;
- resolvent or sign-functional-calculus reformulations;
- finite positive ancillas and Morita/matrix stabilization; and
- further Karoubi splittings of the same feasible rows.

These preserve the order problem or the carrier grade.  A proposal should be
revived only when it exposes a transformed prime estimate that is genuinely
available and includes the transported norm.

### 7.2 More mixtures with the same observables

Stop adding:

- phases, random seeds, real/imaginary quadratures;
- positive direct sums over the same support scales;
- dephased or block-randomized copies; and
- larger positive ensembles constrained by the same aggregate effects.

The `CPM` rank bound and aligned-face inequality already optimize this class.
Signed weights are outside the state cone and do not imply a Weil witness.

### 7.3 Generic local gluing

Do not pursue another partition of unity, translated-window cover, or
diagonal packet family unless the first deliverable is the relative cone
identity (4.4) on a specified zeta operator system.  Ordinary spanning,
density of vectors, and sheaf-like support coverage are insufficient.

### 7.4 Derived glue without a heart-level polarization

Do not add higher differentials, mapping cones, contractible bridges, or
supertrace refinements while leaving the primary map and dagger unchanged.
The degree-zero energy does not change, contractible glue is trace-invisible,
and shift-positive `K_0` invariants vanish.  A concrete positive metric on a
heart or pure sector is required before returning to this branch.

### 7.5 Nonlinear names without a cross-effect ledger

“Take a determinant,” “pass to exterior power,” “use a Pick matrix,” or
“apply a connected logarithm” is not a proposal until (4.19) is written for
the completed place pieces and every carrier-sized mixed term is named.
Higher degree is lower priority than degree two unless it kills rather than
multiplies the uncontrolled correlations.

### 7.6 Bulk invariants aimed at one exception

Normalized trace, Frobenius energy, positive-density counts, and any fixed
bounded set of moments factor through a sparse-defect quotient at the
relevant abstract level.  Improving their constants cannot alone exclude one
off-line pair.  Revive the branch only when coupled to a rank-one-sensitive
edge, leverage, or index theorem.

### 7.7 Weak limits without carrier tightness

Compact-open, strong-resolvent, fixed-window, or average convergence should
not be treated as a global completion unless a moving negative line is shown
not to escape.  Finite certificates are useful base stages; without a
cofinal transfer theorem they are not an asymptotic proof architecture.

## 8. Expanded GO targets, in recommended order

### GO-1: build the actual carrier-grade operator system and test relative
probe generation

Define the smallest practical real space `W_T` containing the exact
prime/gamma/pole completed compressions after positive-row quotient and
carrier normalization.  Retain its Toeplitz/displacement-rank and coefficient
constraints.  Then compute or bound

```text
closure r_(W_T)(C_probe)  versus
closure r_(W_T)(Pos(H_T)).                            (8.1)
```

A proof of equality is an order-reflecting coherent-probe theorem.  A
separating form in `W_T` closes the proposed probe family.  This is likely the
cheapest genuinely new categorical target because it can be falsified at
finite stages and, unlike full PSD generation, exploits arithmetic structure.

Promising probe additions are coherent separated-lobe states and their
polarizations, not more single intervals.  Their purpose is to generate the
missing exposed face of (8.1).

Equivalently, a kernel method may move from an ordinary support cover to a
pair-groupoid or product-site cover.  For `X=U union V`, the object must retain
`U x V` and `V x U` as well as the two diagonal rectangles.  Such cross-aware
descent is faithful enough to avoid the triangular-packet countermodel, but
its descent structure maps must then prove the same carrier-scale
prime/collateral cross estimate encoded by (8.1).  This is a real reformulation
of GO-1, not a separate free source of positivity.

### GO-2: decide the Rees grade of the actual remainder

For

```text
R_T=K_actual,T-K_aligned-pair,T                      (8.2)
```

on the positive-null object, first prove one of

```text
||p_T R_T p_T||=o(K_T),
||p_T R_T p_T||=O(K_T),
||p_T R_T p_T||/K_T->infinity along a subsequence.   (8.3)
```

The first closes every carrier-scale positive-ensemble escape.  The second
defines `tau` and reduces the problem to its positive part and target pairing.
The third identifies a larger-grade object whose sign must be controlled
before carrier cancellation is discussed.  Separating these cases prevents
an unproved bounded corona class from silently entering the argument.

The analytic components of `R_T` should be graded separately: actual centered
von Mangoldt state, almost-equal-depth collateral pairs, inter-scale overlap,
pole/main, rational, and archimedean terms.  Several are already known to be
subcarrier; effort should concentrate on the first two.

### GO-3: cross-effect-first quadratic arithmetic

For the adaptive quotient-row Gram or completed `2 x 2` determinant, derive
the exact `cr_2` arithmetic expression before designing a new witness.  Sort
its terms into

```text
prime--prime,
prime--gamma/pole,
prime--collateral,
collateral--collateral.                              (8.4)
```

Then ask whether coefficient structure, displacement rank, or an existing
Type-II estimate signs the particular polarized combination.  This route is
direct strip-strength, but it is the minimal nonlinear burden.  If the exact
quadratic expression already needs an unavailable fixed power saving, exterior
degrees `3,4,...` should be deprioritized.

### GO-4: a sparse-exception detector coupled to the density theorem

Treat the positive-density result as control of the quotient by a sparse
defect ideal.  Add one invariant which does not factor through that quotient:

- a uniform selected-block leverage lower bound;
- a carrier-state separation theorem;
- an actual least-edge inequality; or
- a relative index with a uniform gap.

The useful research question is not whether another bulk statistic can be
estimated, but whether the quotient map admits a zeta-specific order-reflecting
lift on one exceptional block.

### GO-5: heart-level global polarization

A cohomological/global-trace program should specify:

1. a heart, pure weight piece, or harmonic object on which positivity is not
   annihilated by shift;
2. a canonical positive dagger defined from arithmetic or geometry before
   zeros are known;
3. a separate signed trace functor reproducing the explicit formula;
4. a compatibility natural transformation between trace and polarization;
5. naturality as primes are adjoined; and
6. a carrier-conservative global limit.

The first deliverable must be item 2, not another trace identity.  In the
finite model, existence of some `G>0` solving `A*G+GA=G` is equivalent to
`A` being diagonalizable with spectrum on the critical line.  Thus fitting
such a metric after constructing `A` is at least the critical-line spectral
conclusion (and also encodes semisimplicity), so it is only a detector.

### GO-6: a completion-native relative index

Construct an arithmetic object before its zeros are used, place it in a
corona/Calkin or other operator category where a single remote carrier has a
nonzero class, and prove all-place convergence and index stability there.
The local Euler loops, `B^2` phase limit, and compact-open divisor topology do
not jointly meet these requirements.  A new index is worth pursuing only when
the topology and the nonvanishing class are specified simultaneously.

### GO-7: actual collateral isolation

Prove a zeta-specific theorem excluding a second pair in the same carrier
grade with the orientation needed to cancel the selected pair.  Count,
density, and the first two moments allow a sparse almost-equal-depth exception.
The missing input is a local depth/angle or divided-difference conditioning
theorem, not more abstract categorical structure.

## 9. Stop/go table for the current search space

| Proposal family | Categorical signature | Immediate decision | Required revival theorem |
|---|---|---|---|
| invertible preconditioner | strict filtered, order-conservative | low priority | transformed arithmetic bound with conditioning |
| singular smoothing/compression | carrier-forgetful unless observed | stop | relative order reflection on `W_T` |
| Schur/Feshbach/Birman--Schwinger | conservative; nonlinear by places | low priority | signed last-pivot/cross-effect estimate |
| positive ancilla | order-conservative stabilization | stop as escape | genuinely new coupled effect |
| partial trace/dephasing | positive but nonconservative | stop | recovery/observability theorem |
| positive multi-witness | one `CPM` state; bounded extreme rank | stop with same effects | carrier-grade transverse effect |
| local packet cover | probe cone | test, then go/stop | relative cone equality (4.4) |
| target-adaptive minor | exact detector, nonlinear degree two | go only as arithmetic target | signed actual two-correlation theorem |
| fixed low minors/moments | sparse-defect forgetful | stop for one pair | rank-one-sensitive supplement |
| exterior degree `d` | polynomial with effects through degree `d` | defer for `d>2` | structural vanishing or `d`-point estimate |
| supertrace/K_0 | shift-signed decategorification | stop as polarization | independent heart-level dagger |
| higher differential | leaves degree-zero energy unchanged | stop | change primary map or dagger and rederive formula |
| faithful positive trace with no mixed moment | forces block locality under audited hypotheses | stop as cross-place engine | separate coupled polarization structure |
| commutator/virial | trace-zero boundary | stop in regular finite class | singular boundary/anomaly with signed flux |
| fitted positive metric | equivalent to target spectrum | stop | zero-independent geometric metric |
| bulk density/trace refinement | factors through sparse quotient | useful but insufficient | ideal-sensitive lift |
| compact-open/strong limit | moving carrier can escape | stop | tightness plus arithmetic convergence |
| corona/relative index | potentially carrier-sensitive | go if class is nonzero | stable gap and all-place convergence |
| actual `tau` or higher Rees remainder | new arithmetic object | highest priority | boundedness/grade, sign, target angle |

## 10. A compact admission checklist

Every future iteration should answer these questions in order.

1. **Object:** What is constructed from primes, gamma data, and support before
   a bad zero or negative eigenvector is known?
2. **Operator system:** On what real space `W_T` must order be reflected?
3. **Grade:** Is the new term subcarrier, carrier, or larger?
4. **Functor signature:** Is the main operation conservative, forgetful, or
   nonlinear on that `W_T` and grade?
5. **Cross-effects:** If nonlinear, what are all carrier-sized mixed terms?
6. **Positivity source:** Which arrow supplies order rather than equality?
7. **Sparse sensitivity:** Can one exceptional rank-one/pair defect survive
   every stated invariant?
8. **Independence:** Is the probe, metric, or index defined without using the
   desired spectral conclusion?
9. **Limit:** In what topology does one remote defect remain nonzero, and does
   the arithmetic object converge there?
10. **Quantitative close:** What exact estimate, with constants and
    normalization, closes the diagram?

Failure at questions 2--5 usually permits a finite countermodel and should be
tested before formalization.  Failure at 6--10 identifies the genuine theorem
to pursue rather than another equivalent detector.

## 11. What category theory still does not decide

The grammar does not determine any of the following.

- whether the full actual remainder in (8.2) is bounded at carrier scale;
- the sign and target angle of the centered von Mangoldt transverse class;
- whether an almost-equally-deep collateral zeta zero exists;
- fixed-power Type-II or prime-polynomial cancellation;
- quantitative endpoint-jet and divided-difference conditioning;
- an exact nonzero intertwiner between shifted de Branges and compact-support
  Weil categories;
- a canonical number-field analogue of a Rosati/Hodge polarization;
- tight all-place convergence in a carrier-sensitive index topology; or
- a uniform zero-free strip.

These are analytic and arithmetic questions.  The category-theoretic gain is
that they are no longer hidden among coordinate choices, witness copies, or
decategorifications.

## 12. Novelty and publication boundary

The individual ingredients used here are standard: cone duality, Karoubi
completion, purification, spectrahedral rank bounds, polynomial
cross-effects, the shift relation in `K_0`, faithful traces, and elementary
operator-topology counterexamples.  They should not be presented as new
category theory.

The potentially publishable project-level contribution is their joint
application to the exact normalized completed-mirror architecture:

- the **relative** operator-system probe criterion as the correct replacement
  for full local-to-global positivity;
- the strict filtered/Rees statement that formal adapters cannot create the
  missing carrier class;
- the cross-effect budget linking nonlinear categorical degree to arithmetic
  correlation order;
- the derived shift theorem as a clean reason to separate signed trace from a
  heart-level polarization; and
- the sparse-defect quotient as the categorical boundary between the density
  theorem and a uniform strip.

This is a rigorous navigation and pruning theorem.  It becomes a substantive
zeta paper only when paired with at least one new zeta-specific result:
relative cone generation, computation/exclusion of `tau`, a signed quadratic
cross-effect estimate, an independent polarization, or a carrier-sensitive
stable index.

## 13. Primary repository anchors

- [`ZETA23-CATEGORICAL-CONSOLIDATION-FOUR-LEMMA-2026-08-12.md`](ZETA23-CATEGORICAL-CONSOLIDATION-FOUR-LEMMA-2026-08-12.md)
- [`ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md`](ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md)
- [`ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md`](ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md)
- [`CATEGORY-THEORETIC-SEARCH-PRUNING-REFEREE-AUDIT-2026-08-12.md`](CATEGORY-THEORETIC-SEARCH-PRUNING-REFEREE-AUDIT-2026-08-12.md)
- [`CATEGORY-THEORETIC-CONSOLIDATION-REFEREE-AUDIT-2026-08-12.md`](CATEGORY-THEORETIC-CONSOLIDATION-REFEREE-AUDIT-2026-08-12.md)
- [`ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md`](ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md)
- [`ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md`](ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md)
- [`GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`](GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md)
- [`TRIANGULAR-PACKET-CONE-NOGO.md`](TRIANGULAR-PACKET-CONE-NOGO.md)
- [`ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md`](ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md)
- [`ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md`](ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md)
- [`../publication/NO-GO-THEOREM-GUIDE.md`](../publication/NO-GO-THEOREM-GUIDE.md)
