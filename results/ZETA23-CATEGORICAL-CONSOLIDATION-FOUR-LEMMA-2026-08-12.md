# A categorical consolidation of the completed Weil/Gabor program

Status: rigorous finite-dimensional and asymptotic categorical synthesis,
2026-08-12.  This note reorganizes the existing detector, trace,
multi-witness, localization, and operator-transformation audits into four
master lemmas.  It proves no zero-free strip, no failure of a zero-free strip,
and no statement about ZFC independence.

## 1. Verdict

The category-theoretic viewpoint does produce a real compression of the
repository's conclusions.  It does not create a new positivity theorem.
Almost all audited mechanisms fall under four exact facts.

1. **Dagger-kernel/associated-grade carrier lemma.**  Positive constraints
   factor a state through a dagger kernel.  At the selected carrier grade, the
   normalized mirror form is the aggregate cross observable; positive
   diagonal and subcarrier terms vanish in the associated graded object.  A
   state which cancels that cross class cannot retain a negative carrier unless
   a transverse remainder survives at the carrier grade or above it.
2. **Functorial-adapter trilemma.**  A linear dagger pullback transports the
   same completed identity and the same order obstruction; an invertible one
   reflects the original inertia, while a nonfaithful one can lose the bad
   direction.  A nonlinear spectral transform can preserve the sign or erase
   it, but it preserves the additive prime--pole--archimedean decomposition
   only when it is affine.  Thus a transformed detector is not an exclusion
   engine unless a new arithmetic law is added.
3. **Non-descent/nonconservativity lemma.**  Positivity is not determined by a
   finite proper family of local compressions, nor by the first two categorical
   traces.  These decategorifications forget precisely the cross terms in which
   a remote defect can live.
4. **Trace--polarization separation lemma.**  Trace and supertrace forget
   extension or parity-balanced sectors, while functional-equation duality is
   nonpositive.  A positive polarization is extra dagger structure; in finite
   dimension, imposing the desired adjoint law after constructing the
   generator is already equivalent to putting its spectrum on the critical
   line.

When the carrier-normalized compressed remainder is uniformly bounded, the
genuinely unresolved datum in the current Weil/Gabor route can be represented
by one **asymptotic transverse class**

```text
tau=[P_S R_T P_S/K_T]                                (1.1)
```

in a corona C-star category.  Here `S` is the positive-null subobject, `K_T`
is the selected carrier scale, and `R_T` is what remains after the aligned
mirror cross is removed.  Definition (1.1) requires

```text
sup_T ||P_S R_T P_S||/K_T<infinity.                 (1.2)
```

Under the audited packet geometry and proved norm estimates, rational,
archimedean, shallow-collateral, and other subcarrier families are zero in
this quotient.  A nearly equally deep collateral zero or a genuinely
target-transverse actual-prime state need not be zero.  The present estimates
do not prove (1.2) for the full open actual remainder.  If (1.2) fails, that
remainder is a carrier-or-larger object outside this bounded C-star corona; the
finite inequalities of master lemma I still apply, but its asymptotics require
a larger filtered or bornological category.  Computing which case occurs, and
the order and target pairing in it, is the missing engine; changing coordinates
does not compute it.

## 2. The categorical dictionary

Work first in the dagger symmetric monoidal category `FHilb` of
finite-dimensional complex Hilbert spaces.

- The dagger is the Hilbert adjoint `S -> S^*`.
- The tensor product is the monoidal product and `C` is the tensor unit.
- Orthogonal direct sum is a dagger biproduct.  Labelled packets, support
  scales, and witness families use this biproduct.
- For an object `H`, `Herm(H)` is the real ordered vector space of Hermitian
  endomorphisms, with positive cone `End(H)_+`.
- A test morphism `S:E->H` pulls a form back by

```text
Herm(S)(A)=S^* A S.                                  (2.1)
```

This defines a contravariant functor from finite Hilbert spaces and linear
maps to ordered real vector spaces: composition and daggers give

```text
(S T)^* A (S T)=T^*(S^* A S)T,                      (2.2)
```

and positivity is preserved.

The `CPM` construction supplies the correct category for positive ensembles.
In finite-dimensional language, an unnormalized state is a matrix
`Gamma>=0`; a normalized state has `Tr Gamma=1`.  A pure state is `z z^*`, and
the state--observable pairing is

```text
<A,Gamma>=Tr(A Gamma).                               (2.3)
```

Thus

```text
Gamma=sum_j w_j z_j z_j^*,       w_j>=0,             (2.4)
```

is not an analogy: it is exactly a mixed `CPM(FHilb)` state.  Averaging,
dephasing, compression, and discarding labels are completely positive maps.
Signed witness weights are not states in this category.

After invoking the relevant Guinand--Weil theorem or declared literature
interface at a finite packet stage, the explicit formula is an equality of
Hermitian morphisms

```text
K_arithmetic=K_divisor.                              (2.5)
```

The arithmetic side has an additive place decomposition into pole/main,
archimedean, rational, and prime terms.  Equation (2.5) is an equality datum.
The assertion `K_arithmetic>=0` is an order datum.  A functor preserves (2.5)
automatically; it preserves or reflects its order only when its positive
structure says so.  All categorical algebra below is exact conditional on
this finite-stage identification; this wording does not promote the full
zero-side Guinand--Weil equality to an unconditional Lean theorem.

The role of the other familiar categorical structures is now precise.

- Tensor/Euler composition organizes independent places.
- Trace, supertrace, connected character, and moment maps decategorify
  endomorphisms to scalars.
- Exterior powers are polynomial functors; the total exterior algebra is
  multiplicative for direct sums.  Taking traces of the fixed-degree pieces
  decategorifies them again.
- A positive polarization chooses a dagger or positive metric.  It is not
  determined by an additive or alternating trace.
- Passing to compact support, a packet subspace, or a finite test bank is a
  pullback along a subobject.  Such a pullback preserves positivity but need
  not reflect it.

## 3. Master lemma I: dagger-kernel lifting in the carrier grade

### 3.1 Exact positive-state lemma

Let `H` be a finite Hilbert space, let `X:H->E`, and put

```text
P=X^*X>=0,                  S=ker X.                 (3.1)
```

Let all observables below be compressed to `S`.  Suppose

```text
Q=D+B+E_0,                 D>=0,                    (3.2)
```

where `B` is the aligned aggregate-cross observable and `E_0` is an error.
Let `R=R^*` be a proposed transverse reservoir.  If `Gamma>=0`,
`Tr Gamma=1`, and

```text
abs(Tr((B+R)Gamma))<=epsilon,                       (3.3)
Tr(Q Gamma)<=-kappa,                                (3.4)
```

then

```text
Tr(R Gamma)>=kappa-epsilon-||E_0||,                 (3.5)
||(R)_+||>=kappa-epsilon-||E_0||.                   (3.6)
```

There is a second useful form.  If `N>=0` is a carrier effect and

```text
B<=-c N,                         c>0,               (3.7)
```

then (3.3) implies

```text
||(R)_+||>=c Tr(N Gamma)-epsilon.                   (3.8)
```

In particular, if `R=E_0=0` and the aggregate is cancelled exactly, no
negative state exists.  If a fixed fraction of a carrier of size `K` is
retained, the positive part of the transverse reservoir has norm comparable
to `K`.

#### Proof

From (3.2)--(3.4),

```text
Tr(B Gamma)
 =Tr(Q Gamma)-Tr(D Gamma)-Tr(E_0 Gamma)
 <=-kappa+||E_0||,                                (3.9)
```

because `D>=0` and a state has `Tr(E_0 Gamma)>=-||E_0||`.  Subtract (3.9)
from (3.3), with the unfavorable sign for its error, to obtain (3.5).  For a
Hermitian `R`,

```text
Tr(R Gamma)<=Tr(R_+ Gamma)<=||R_+||,                (3.10)
```

which proves (3.6).  Under (3.7), positivity of `Gamma` gives

```text
Tr(B Gamma)<=-c Tr(N Gamma);                        (3.11)
```

subtracting this from (3.3) gives (3.8).  QED

The positive-null condition has not been hidden.  If a state on `H` obeys

```text
Tr(P Gamma)=0,                                      (3.12)
```

then

```text
0=Tr(X^*X Gamma)=||X Gamma^(1/2)||_HS^2,            (3.13)
```

so `range Gamma` lies in `S`.  Positive-row cancellation therefore really is
factorization through the kernel subobject; different phases cannot cancel a
positive effect.

For homogeneous **complex linear** rows, this factorization has a second exact
form.  Let `a,g:H->C` be the target and aggregate rows, let `i:S->H` be the
dagger-kernel inclusion for `X`, and let

```text
j:K=ker(g i)->S.                                    (3.14)
```

If `g i` is nonzero, the squared target leverage which survives both kernels
is

```text
||(a i)|K||^2
 =||a i||^2-abs(<(a i)^*,(g i)^*>)^2/||g i||^2.     (3.15)
```

Indeed, the orthogonal projector onto `K` is

```text
j j^*=I-(g i)^*(g i)/||g i||^2,                    (3.16)
```

and (3.15) follows by applying it to the Riesz vector `(a i)^*`.  The target
lift vanishes exactly when `(a i)^*` lies in the one-dimensional image of
`(g i)^*`.  Thus the isolated completed pair is not merely “short of
dimension”: its target and aggregate arrows become the same arrow in the
dagger quotient by the positive rows.

Equivalently, put

```text
alpha=(a i)^*,              gamma=(g i)^*,
Omega=alpha wedge gamma in Lambda^2 S.              (3.16a)
```

The Gram identity gives

```text
||Omega||^2=||alpha||^2||gamma||^2-abs(<alpha,gamma>)^2,
||(a i)|K||^2=||Omega||^2/||gamma||^2.              (3.16b)
```

Thus `Omega` is a basis-free transversality invariant: it vanishes precisely
when the complex aggregate kernel kills all target leverage.  It is not the
signed determinant of the completed Weil form.  The former measures the angle
between two constraint rows; the latter detects operator inertia.  Conflating
them would again turn a detector into an engine.  A fuller Karoubi-envelope
operator treatment is in
[`ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md`](ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md).

The minimal one-real aggregate condition is affine/quadratic rather than the
complex kernel (3.14).  It must not be replaced by (3.15).  The state/effect
lemma (3.2)--(3.8) is the version valid for that actual minimal condition and
gives the same no-lift conclusion on the affine mirror block.

### 3.2 Why multiple witnesses add no hidden degree of freedom

On one common admissible object, consider states satisfying only

```text
Gamma>=0,       Tr Gamma=1,       Tr(B Gamma)=0.     (3.17)
```

Every extreme point of this spectrahedron has rank one.  If an extreme state
had rank `r>=2`, Hermitian perturbations on its range would have real dimension
`r^2>=4`.  The two real equations

```text
Tr Delta=Tr(B Delta)=0                              (3.18)
```

leave a nonzero perturbation, and small `Gamma+-t Delta` remain positive.
This contradicts extremality.  A linear objective therefore has a pure-state
optimizer.  Convexifying witnesses is useful bookkeeping, but with the one
minimal real aggregate equation it cannot improve the optimum over a coherent
witness.

More generally, positive maps preserve the aligned inequality.  If
`Psi` is positive and (3.7) holds, then

```text
Psi(B)<=-c Psi(N).                                  (3.19)
```

An invertible dagger pullback is order-reflecting.  A conditional expectation
or dephasing may send `Psi(N)` to zero, but then it has erased the detector;
it has not made the cross transverse.

### 3.3 The carrier associated grade

The depth/exponent ledger is a filtration, not just a list of estimates.  For
an asymptotic object `H=(H_T)` and selected carrier scale `K_T`, define the
dagger-stable Hermitian filtration spaces

```text
F_K={A_T=A_T^*: ||A_T||=O(K_T)},
F_<K={A_T=A_T^*: ||A_T||=o(K_T)}.                   (3.20)
```

Their quotient

```text
gr_K Herm(H)=F_K/F_<K                               (3.21)
```

is the associated Hermitian vector space at the carrier grade.  Its
C-star-ordered realization for uniformly bounded normalized families is given
in Section 3.4.  If one filters all morphism spaces by powers of `X_T`,
composition adds exponents and these spaces are the corresponding Hermitian
parts of the associated graded dagger category.  Families larger than `O(K_T)`
belong to a higher filtered piece and are not elements of (3.21).

Let `i_T:S_T->H_T` be the positive-row dagger kernel.  Pullback to `S_T`
commutes with passage to the grade.  For the mirror,

```text
i_T^*M_T i_T=i_T^*B_T i_T+D_T+o(K_T),
D_T>=0,                                              (3.22)
```

and in the isolated normalized pair `D_T=m_T I=o(K_T)`.  Hence the completed
form class and aggregate-cross class coincide in `gr_K`.  Cancelling the
aggregate asks for a lift through the kernel of that grade-class; retaining a
negative carrier asks for the same state to pair negatively with the identical
class.  Master lemma I says these demands are incompatible unless a new
arrow `R_T` has a nonzero carrier-grade component.  If `R_T/K_T` is unbounded,
it lies above this bounded grade rather than defining a class inside it; in
either case it is not a subcarrier escape.

This is the promised **dagger-kernel/associated-grade obstruction**:

```text
constraints -> dagger kernel S
            -> carrier associated grade
            -> mirror class = aggregate class
            -> no negative constrained lift without transverse
               carrier-or-larger R_T.                                    (3.23)
```

### 3.4 The asymptotic quotient category

The subcarrier language can be made exact.  Let an object be a sequence
`H=(H_T)` of finite Hilbert spaces.  Define

```text
Hom_b(H,G)={ (S_T): sup_T ||S_T||<infinity }.       (3.24)
```

The families with `||S_T||->0` form a closed dagger operator ideal `I_0`,
because uniformly bounded pre- and post-composition preserve norm convergence
to zero.  The quotient

```text
Qcat=Hom_b/I_0                                      (3.25)
```

is a C-star category, the finite-matrix analogue of a corona category.

Normalize every uniformly carrier-bounded observable by `K_T`.  For the exact
mirror block,

```text
M_T=m_T I+B_T,              m_T/K_T->0,             (3.26)
```

and hence in `Qcat`

```text
[M_T/K_T]=[B_T/K_T].                                (3.27)
```

A family of density matrices and a free ultrafilter define a state on the
endomorphism algebra of the quotient by

```text
phi([A_T])=lim_U Tr(A_T Gamma_T).                   (3.28)
```

This is well-defined because every `I_0` family has vanishing expectation.
If the aggregate cancellation makes `phi([B/K])=0`, (3.27) forces
`phi([M/K])=0`; it cannot simultaneously be at most `-eta<0`.  If
`R_T/K_T` is also uniformly bounded, it defines a morphism in `Qcat`, and the
exact relation is instead

```text
phi([M/K])=-phi([R/K])                              (3.29)
```

up to the stated aggregate sign convention.  Thus a retained negative class
forces `[R/K]` to be nonzero and to have the required positive state pairing.

No boundedness estimate of this strength is currently proved for the full
actual-prime/collateral remainder.  If

```text
sup_T ||P_S R_T P_S||/K_T=infinity,                 (3.30)
```

then `[R/K]` is not a morphism of `Qcat`; it must not be silently placed in
the corona.  It is instead a larger-grade case in the filtration of Section
3.3, or an object for a separately specified bornological category.  This
does not weaken the finite conclusion (3.6): every retained negative witness
still forces a carrier-sized positive part of `R_T`.  It only prevents the
unproved assertion that the whole open remainder has a bounded corona class.

This quotient statement consolidates the following repository results.

- Positive multi-witnesses, phases, real/imaginary quadratures, and labelled
  support scales are states and dagger biproducts covered by (3.5)--(3.19).
- Soft positive-row leakage is the exact special case `M=mI+B`.
- Randomization and dephasing are positive maps; they preserve alignment or
  erase the off-diagonal carrier.
- Under the audited packet geometry and its proved norm estimates, rational
  and archimedean remainders, and collateral pairs a fixed depth below the
  selected pair, are zero morphisms in (3.25) after carrier normalization.
- The pole/main term cancels its matching continuum-prime term before the
  quotient is taken.  Critical pole resonance does not manufacture a second
  class.
- A nearly equally deep collateral pair, a nonorthogonal inter-scale term, or
  a coefficient-specific actual-prime state can survive as `[R/K]` when its
  normalized norm is bounded, or occupy a larger filtered grade when it is
  not.  This is exactly the open transverse case, not an additional witness
  parameter.

The principal source statements are
[`ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md`](ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md),
[`ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md`](ZETA23-COLLATERAL-RESERVOIR-DICHOTOMY-2026-08-12.md), and
[`ZETA23-CRITICAL-POLE-MAIN-AND-MELLIN-SCALE-ESCAPE-AUDIT-2026-08-12.md`](ZETA23-CRITICAL-POLE-MAIN-AND-MELLIN-SCALE-ESCAPE-AUDIT-2026-08-12.md).

## 4. Master lemma II: the functorial-adapter trilemma

### 4.1 Dagger pullbacks transport the same obstruction

Let (2.5) hold and let `S:E->H`.  Functoriality gives

```text
S^*K_arithmetic S=S^*K_divisor S.                  (4.1)
```

The place decomposition is transported term by term.  If `S` is invertible,
Sylvester inertia gives

```text
inertia(S^*KS)=inertia(K),                          (4.2)
```

and the transported metric is `S^*S`; the generalized Rayleigh quotient is
unchanged.  If `S` has proper range, positivity of `S^*KS` does not reflect
positivity of `K`: a negative direction outside `range S` is invisible.

Several apparently nonlinear constructions are dagger pullbacks once their
normalization is retained.  For

```text
K=[[A,B],[B^*,D]],                  D>0,             (4.3)
```

the harmonic lift

```text
Jx=(x,-D^(-1)B^*x)                                  (4.4)
```

satisfies

```text
J^*KJ=A-BD^(-1)B^*,
J^*J=I+BD^(-2)B^*.                                  (4.5)
```

The Schur complement is therefore a pulled-back form.  Dropping `J^*J` is the
normalization error which creates an apparent carrier gain.  Birman--Schwinger
whitening and finite heat smoothing are likewise congruences; resolvent
crossings are equivalent spectral tests.  None adds an order law.

### 4.2 Only affine spectral calculus is place-additive

Let a unitarily natural spectral transformation be

```text
F_H(A)=f(A)                                          (4.6)
```

for one continuous real function `f`.  Suppose it respects additive place
decomposition in the universal sense

```text
F_H(A+B)=F_H(A)+F_H(B)-f(0)I                        (4.7)
```

for all commuting finite Hermitian `A,B`.  Then

```text
f(x)=f(0)+c x                                       (4.8)
```

for a real constant `c`.

Indeed, apply (4.7) to one-dimensional objects and put
`g(x)=f(x)-f(0)`.  Then `g(x+y)=g(x)+g(y)`, and continuity makes `g` linear.

This gives an exact trilemma.

1. If a spectral map makes every output positive, as with the square or
   absolute value, it erases the sign.
2. If `f(0)=0` and `sign f(x)=sign x`, it preserves the negative index and the
   original positivity problem.
3. If it is genuinely nonlinear, it does not universally transport the
   additive arithmetic decomposition term by term.  Its expansion introduces
   mixed prime--prime, prime--archimedean, and pole--prime terms; an
   operator-specific cancellation of those terms would itself be a new
   arithmetic law.

The same distinction applies to scale filters.  A coherent filtered witness
is a test morphism and retains all cross-scale terms.  At the residue level,
the Mellin multiplier acts naturally on the selected zero and its matching
completed arithmetic term.  A formal signed average can cancel these classes,
but it is not a positive `CPM` state and gives no negative-witness inference.

### 4.3 Detector versus engine as a categorical distinction

An exact detector is a functor or invariant `D` for which a forbidden zero
produces a nontrivial object, scalar, kernel vector, or index.  Li powers,
Nyman--Beurling kernels, shifted de Branges kernels, Weil inertia, and winding
all provide versions of this second arrow:

```text
forbidden zero  ---->  nonzero detector.             (4.9)
```

A functor applied to the completed equality only rewrites (4.9).  An
exclusion engine requires a separate first arrow

```text
arithmetic/geometric law  ---->  detector must vanish. (4.10)
```

Categorically, (4.10) must be one of the following additional structures:

- an order-reflecting positive functor or natural polarization;
- an independently computed monotone/contractive effect;
- a homotopy- or limit-stable index whose arithmetic representative is
  defined without the zero divisor;
- a coefficient-specific theorem which computes the bounded transverse class
  (1.1), or proves and controls a larger filtered-grade remainder.

Equality-producing monoidal, duality, trace, or transform structure alone
does not supply any of these.

The operator instances are proved in
[`ZETA23-OPERATOR-PRECONDITIONING-FUNCTIONAL-CALCULUS-AUDIT-2026-08-12.md`](ZETA23-OPERATOR-PRECONDITIONING-FUNCTIONAL-CALCULUS-AUDIT-2026-08-12.md).

## 5. Master lemma III: positivity does not descend through the audited decategorifications

### 5.1 Exact probe-cone criterion

Let `J={j_i:E_i->H}` be any finite or infinite family of bounded probe
morphisms into a finite Hilbert space `H`.  Define its closed probe cone

```text
C_J=closure cone{j_i Gamma_i j_i^*:
                 i in J, Gamma_i>=0}.               (5.1)
```

Define the cone of forms which look positive to every probe by

```text
L_J={A=A^*: j_i^* A j_i>=0 for every i}.            (5.2)
```

With respect to the Hilbert--Schmidt pairing, these cones obey the exact
duality

```text
L_J=(C_J)^*.                                        (5.3)
```

Consequently, local positivity reflects global positivity for **every**
Hermitian form,

```text
L_J=Pos(H),                                         (5.4)
```

if and only if

```text
C_J=Pos(H).                                         (5.5)
```

#### Proof

For Hermitian `A`, cyclicity of trace gives

```text
Tr(A j_i Gamma_i j_i^*)=Tr((j_i^* A j_i)Gamma_i).  (5.6)
```

The right side is nonnegative for every `Gamma_i>=0` exactly when
`j_i^*Aj_i>=0`.  This proves (5.3), including closure by continuity.  The
positive cone of a matrix algebra is self-dual.  Since every positive `A`
has positive pullbacks, `Pos(H)` is contained in `L_J`; dualizing (5.3) now
gives (5.4) iff (5.5).  QED

This is the precise categorical descent criterion.  A collection of probes
need not cover only vectors; its pushed-forward positive states must generate
the entire global positive cone.  It therefore applies equally to infinitely
many translations, modulations, packet windows, or randomized probes.  A
successful coherent probe theorem is exactly a proof of (5.5) for the
operator system actually occupied by the completed form.

There is a sharp finite-family corollary.  Let `E_1,...,E_m` be subspaces and
let `j_i` be their isometric inclusions.  Then the restrictions reflect
positivity for every Hermitian `A` if and only if

```text
union_i E_i=H.                                      (5.7)
```

For a finite family over `C`, this forces one `E_i=H`.  To prove the converse
failure directly, choose a unit vector `x` outside the union and put

```text
c=max_i ||P_(E_i)x||^2<1.                           (5.8)
```

Choose `1<lambda<=1/c` when `c>0`, and any `lambda>1` when `c=0`.  Then

```text
A=I-lambda x x^*                                   (5.9)
```

is negative on `x`, while for `y in E_i`,

```text
<y,Ay>
 >=(1-lambda ||P_(E_i)x||^2)||y||^2
 >=0.                                               (5.10)
```

This contains the `3 x 3` triangular-packet counterexample.  Partition
gluing, short translated windows, and a predetermined finite test bank cannot
imply global positivity without generating the missing coherent rank-one
states in (5.1).  An adaptive subobject containing the negative vector does
detect it, but its arithmetic compression is then a target-specific theorem.

### 5.2 First two traces are not order-conservative

The moment decategorification

```text
A |-> (Tr A,Tr(A^2))                                (5.11)
```

does not reflect positivity, even with the exact Zeta23-scale values.  For
every even `N>=26`, put

```text
a_N^2=(N/3-8)/(N-2),        b^2=1/3,                (5.12)

A_N=diag(-1,3,
         (1+a_N) repeated (N-2)/2 times,
         (1-a_N) repeated (N-2)/2 times),           (5.13)

B_N=diag((1+b) repeated N/2 times,
         (1-b) repeated N/2 times).                 (5.14)
```

Then `B_N>0`, `A_N` has one negative eigenvalue, and exactly

```text
Tr A_N=Tr B_N=N,
Tr(A_N^2)=Tr(B_N^2)=4N/3.                           (5.15)
```

Hence even agreement of the first two categorical traces does not determine
the order object.  The stronger flat-defect construction in the low-order
nonlinear audit additionally makes every coordinate principal compression up
to order `N/(1+3 kappa)` positive while retaining a carrier-scale negative
eigenvalue.

Exterior powers clarify rather than evade this issue.  The full functor
`Lambda^r` retains wedges containing the negative eigenvector, but the scalar
`Tr(Lambda^r A)` and a predetermined family of coordinate minors are further
decategorifications.  They are not jointly order-reflecting at bounded or
currently tractable order.  A target-adaptive `2 x 2` determinant is an exact
detector; its completed arithmetic sign is the missing two-correlation
engine.

### 5.3 Higher arrows can be invisible to the relevant degree

For a dagger complex

```text
H_0 --d_0--> H_1 --d_1--> H_2,                     (5.16)
```

the degree-zero Hodge energy is exactly

```text
Delta_0=d_0^*d_0.                                  (5.17)
```

Changing `d_1` or adding later categorical structure cannot repair degree-zero
positivity unless it changes `d_0`, the degree containing the Weil object, or
the dagger itself.

### 5.4 Limits are another nonconservative functor unless tightness is proved

A limit topology is part of the mathematical functor, not cleanup.  A
compact-open or fixed-resolution limit in which one remote normalized quartet
tends to the identity makes every continuous integer invariant blind to that
quartet.  A uniform-symbol topology preserves winding but the relevant finite
Euler products do not converge there below `Re(s)=1`.  A divisor/contour limit
detects the quartet because it has imported zero counting.  This is the same
nonconservativity issue at the pro-object level: the chosen colimit either
kills the defect, fails to exist in the order/index category, or carries the
missing theorem as an additional hypothesis.

The source audits are
[`TRIANGULAR-PACKET-CONE-NOGO.md`](TRIANGULAR-PACKET-CONE-NOGO.md),
[`ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md`](ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md),
[`QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`](QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md).

## 6. Master lemma IV: decategorified trace and duality do not supply polarization

### 6.1 Supertrace forgets contractible glue

Let a two-term Hilbert complex have

```text
C^0=V,             C^1=V,             d=I.          (6.1)
```

If an endomorphism `W` acts by the same matrix on both degrees and commutes
with `d`, then

```text
Str(W)=Tr(W|C^0)-Tr(W|C^1)=0.                       (6.2)
```

The whole contractible summand is invisible to every such signed trace even
when `W` encodes nontrivial chain-level coupling.  Consequently a
parity-balanced mixed-place sector can cancel virtually without providing a
positive harmonic polarization.  This is not a numerical accident; the
supertrace factors through the homotopy category and is designed to forget
contractible objects.

### 6.2 Honest characters split under an invariant dagger

Let a finite Hilbert object carry a unitary action of an independent compact
place torus.  Its invariant dagger gives an orthogonal weight decomposition

```text
H=direct_sum_chi H_chi.                              (6.3)
```

Indeed, if `v,w` have distinct characters `chi,eta`, invariance gives

```text
<v,w>=chi(t) conjugate(eta(t)) <v,w>                (6.4)
```

for every `t`, and some `t` forces the scalar factor to differ from one.

The independent compact-place action is a model hypothesis here; it has not
been derived for the multiplicatively coupled adelic quotient.  The splitting
conclusion is conditional on that action and its invariant dagger.

If an **honest** connected character has no mixed weights, the corresponding
nonnegative weight multiplicities vanish and the finite object splits
placewise.  There is then no cross-place positive mechanism.  If the trace is
instead a supercharacter, mixed even and odd sectors may cancel, but (6.1)--
(6.2) show why that cancellation has no positive meaning.  Taking a connected
logarithm, cumulant, or alternating trace can reproduce the explicit formula;
it does not reconstruct a dagger polarization forgotten by decategorification.

### 6.3 A faithful positive trace forces trivial block locality

Let `tr_f` be a faithful finite trace on a finite-dimensional C-star algebra,
and suppose

```text
0<=P,Q<=I,
tr_f(P)=tr_f(P^2),       tr_f(Q)=tr_f(Q^2),
tr_f(PQ)=0.                                          (6.5)
```

Then `P` and `Q` are orthogonal projections.

Indeed, `P-P^2>=0` and `Q-Q^2>=0`.  Faithfulness and (6.5) force
`P=P^2` and `Q=Q^2`.  Traciality gives

```text
tr_f(PQP)=tr_f(PQ)=0.                               (6.6)
```

Since `PQP=(QP)^*(QP)>=0`, faithfulness gives `QP=0`, hence `PQ=0`.

This is the positive-trace fork complementary to supertrace invisibility.  A
single faithful positive trace which saturates the first two pure Euler
moments and kills the first mixed moment separates the local sectors
orthogonally; it cannot also encode nontrivial cross-place polarization.  A
supertrace can hide a mixed bridge, but then its cancellation is virtual and
does not define an order.  The signed explicit-formula trace and the positive
polarization must therefore be distinct structures.

### 6.4 A fitted positive dagger is equivalent to the spectral conclusion

A positive metric `G>0` defines a dagger by

```text
A^(dagger_G)=G^(-1)A^*G.                            (6.7)
```

For a finite generator `A`, the following are equivalent.

1. There is `G>0` such that `A^(dagger_G)=I-A`.
2. There is `G>0` such that `A^*G+GA=G`.
3. `A-(1/2)I` is similar to a skew-Hermitian matrix.
4. `A` is diagonalizable and every eigenvalue has real part `1/2`.

For `2 => 3`, set `S=G^(1/2)`.  The equation says that
`SAS^(-1)-(1/2)I` is skew-Hermitian.  Conversely, transport the standard
metric back along a similarity in item 3.  The spectral theorem gives
`3 iff 4`.

Thus a positive dagger which turns functional-equation reflection into an
adjoint is already the desired finite spectral theorem.  Computing `G` from
the eigenvectors or a Cholesky factor of the desired Weil form is a detector
factorization, not an independent engine.

### 6.5 Rigid duality is strictly weaker than positive polarization

For real `a!=0`, put

```text
A_a=diag(1/2+a,1/2-a),
J_symp=[[0,1],[-1,0]].                               (6.8)
```

Then

```text
A_a^T J_symp+J_symp A_a=J_symp,                     (6.9)
```

although the eigenvalues lie off the critical line.  A nondegenerate
symplectic duality can encode `rho <-> 1-rho`; it does not carry an order cone.
The functional equation therefore supplies a rigid reflection datum, while a
positive polarization remains genuinely extra structure.

Master lemma IV is the categorical form of the detector-versus-engine and
global-trace lessons: an alternating trace can give the exact explicit
formula, and a duality can give the exact symmetry, while neither determines
the positive dagger needed for zero exclusion.  In the function-field model,
the Rosati/Hodge polarization is independent geometric input; that is exactly
the kind of second arrow absent here.

The finite trace and polarization audit is
[`GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`](GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md).

## 7. Scoped master corollary for the audited grammar

Consider the proof grammar generated by dagger pullbacks and dagger-kernel or
Karoubi subobjects, dagger biproducts, completely positive mixtures and
conditional expectations, local probe families, categorical
trace/supertrace and continuous spectral calculus, and bounded filtered or
cofinal limits of these constructions.

Within this audited grammar, exclusion of a carrier-grade mirror defect must
add at least one of the following data not generated by the completed equality
alone:

1. an order-reflecting coherent probe family, equivalently the relevant
   probe cone generates the positive cone;
2. a bounded same-grade transverse arithmetic class such as `tau` whose sign
   and target pairing are computed from actual coefficients, or a controlled
   carrier-or-larger remainder in a specified filtered category;
3. an independent positive polarization or dagger, constructed without the
   forbidden divisor or the desired spectral factorization;
4. a conservative cofinal-limit/tightness theorem which cannot lose one
   arbitrarily remote carrier defect.

This follows directly from master lemmas I--IV: I forces item 2 at the carrier
grade, II shows that the allowed adapters do not create order, III forces item
1 or 4 when passing through probes or limits, and IV forces item 3 when trace
or duality is asked to control spectrum.

This corollary is deliberately scoped.  It is not an exhaustion of all
possible methods for RH or for a uniform zero-free strip.  A new arithmetic
inverse theorem, dynamical inequality, geometric construction, or other
mechanism outside this grammar may supply a genuinely different engine.

## 8. Collapse table

| Audited route | Categorical form | Governing lemma |
|---|---|---|
| positive multi-witness / multi-seed | one mixed `CPM` state | I |
| phases and real/imaginary quadrature | unitary dagger automorphisms | I, II |
| labelled support scales | dagger biproduct | I |
| positive-row nulls | state factors through a kernel subobject | I |
| soft aggregate leakage | `Q=D+B` with `D>=0` | I |
| shallow collateral, rational, archimedean | zero class under the audited packet estimates | I |
| actual-prime or deep collateral reservoir | bounded class `tau`, or a larger filtered-grade remainder | I |
| randomization / dephasing | completely positive map | I, II |
| invertible preconditioning | order-reflecting dagger congruence | II |
| Schur / Birman--Schwinger / heat pullback | same form under a transported metric | II |
| square / absolute value | sign-erasing spectral functor | II |
| sign-preserving functional calculus | order-equivalent but nonadditive unless linear | II |
| Mellin/support filters | natural common residue multiplier or non-state signed sum | II |
| shifted de Branges, Li, Nyman, winding | sensitive detector without first arrow | II |
| translated local positivity / partition gluing | non-order-reflecting subobject family | III |
| low minors / trace and Frobenius moments | nonconservative decategorification | III |
| exterior coefficients | trace after a polynomial functor | III |
| connected trace / supertrace gluing | forgets extensions or parity-balanced sectors | IV |
| functional-equation/symplectic duality | rigid reflection without an order cone | IV |
| fitted global positive metric | equivalent to the critical-line spectral law | IV |
| higher incidence differentials | invisible to the degree-zero energy functor | III |
| finite computation and finite windows | proper restriction plus nonconservative limit | III |

The fixed-window fourth-moment and all-sector Type-II proposals sit at the
boundary rather than being disproved by these lemmas.  They are direct
arithmetic engines: their fixed power saving is already exponent-equivalent to
a fixed strip.  Category theory correctly classifies them as new laws, not as
free transformations of the detector.

## 9. The reduced research target

The synthesis leaves one diagram to complete and three genuinely different
ways to supply its missing arrow.

```text
actual primes + completion
          |
          |  independent order/index theorem
          v
bounded class tau, or controlled larger-grade remainder
                         ---->  exclusion of the mirror defect.
```

The first option is an **actual transverse order theorem**: first determine
whether the actual von Mangoldt remainder is uniformly carrier-bounded.  In
the bounded case, determine the sign and target angle of `tau`; in the
unbounded case,
identify its filtered growth and prove the corresponding normalized sign
theorem.  Alternatively, prove a local depth/isolation theorem forcing every
such remainder into the wrong cone for a hypothetical offending zero.

The second option is an **independent polarization or order-reflecting
functor**: construct a positive dagger or coherent probe cone from arithmetic
or geometry without using the zero divisor, a fitted eigenbasis, or the
desired Weil factorization, and prove that it transports the completed object
into an order category conservatively at the carrier scale.

The third option is a **quantized computation**:
construct a completion-native relative index whose arithmetic representative
does not factor through the zero divisor or the negative spectral projection,
and prove its stability in an all-place topology sensitive to one arbitrarily
remote defect.

Every successful proposal must therefore answer four categorical questions
at its start.

1. What is the object before its zeros or bad eigenvectors are known?
2. Which morphism supplies an order, contraction, or index rather than an
   equality?
3. Why is that morphism nonzero on the quotient class (1.1) when defined, or
   on the controlled larger filtered grade, or why does it exclude that
   remainder?
4. Which limit functor is order- or index-conservative for one remote defect?

This is a sharper admission test than “find another equivalent criterion.”
The repository already has many conservative detectors.  Its missing datum is
an arithmetic functor which is conservative for **order at the carrier scale**.

## 10. Novelty and scope assessment

The four master lemmas are elementary consequences of finite-dimensional
operator theory, `CPM(FHilb)`, and C-star-category quotients.  They should not
be advertised individually as new category theory.  Their value is the
zeta-specific consolidation:

- the exact identification of positive witness ensembles with states and of
  the one-pair obstruction with a state/effect alignment problem;
- the conditional carrier-normalized corona class (1.1), together with the
  explicit larger-grade alternative, as a single filtered receptacle for
  genuine transverse escapes;
- the joint explanation of local-gluing, low-moment, supertrace,
  fitted-polarization, and limit failures as nonconservative forgetful
  functors.

That synthesis could support a publishable conceptual or methods section only
when paired with the repository's exact normalized mirror realization and at
least one substantive zeta-specific theorem about the bounded `tau` class or
the larger-grade actual remainder.  On its own it is a
rigorous research reorganization and a collection of reusable no-go lemmas,
not a uniform-strip result or a standalone mathematical breakthrough.

## 11. Main repository sources

- [`ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md`](ZETA23-DAGGER-CATEGORICAL-OPERATOR-COLLAPSE-2026-08-12.md)
- [`ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md`](ZETA23-CATEGORICAL-SEARCH-GRAMMAR-AND-PRUNING-THEOREM-2026-08-12.md)
- [`ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md`](ZETA23-CATEGORICAL-POSITIVE-ROUTES-AND-FAIL-FAST-GATES-2026-08-12.md)
- [`ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md`](ZETA23-EXOTIC-CATEGORICAL-ESCAPE-STRESS-TEST-2026-08-12.md)
- [`CATEGORY-THEORETIC-CONSOLIDATION-REFEREE-AUDIT-2026-08-12.md`](CATEGORY-THEORETIC-CONSOLIDATION-REFEREE-AUDIT-2026-08-12.md)
- [`ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md`](ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md)
- [`CONSOLIDATED-LEDGER-AND-ORTHOGONAL-RESET-2026-08.md`](CONSOLIDATED-LEDGER-AND-ORTHOGONAL-RESET-2026-08.md)
- [`POST-EQUIVALENCE-REGROUP.md`](POST-EQUIVALENCE-REGROUP.md)
- [`GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`](GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md)
- [`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md)
- [`ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md`](ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md)
- [`ZETA23-OPERATOR-PRECONDITIONING-FUNCTIONAL-CALCULUS-AUDIT-2026-08-12.md`](ZETA23-OPERATOR-PRECONDITIONING-FUNCTIONAL-CALCULUS-AUDIT-2026-08-12.md)
- [`ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md`](ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md)
- [`QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`](QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md)
