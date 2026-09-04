# A dagger-categorical collapse of the completed-mirror escape census

Status: exact finite-dimensional operator lemmas and a categorical
reorganization of the current Zeta23 obstruction, 2026-08-12.  The results
below compress many existing no-go arguments into a small set of reusable
principles.
They do not prove a zero-free strip, its failure, or RH.  The categorical
language is organizational: the proofs are elementary finite-dimensional
Hilbert-space arguments.

## 1. Headline: one obstruction class and one trichotomy

Work in the dagger category `FHilb` of finite-dimensional complex Hilbert
spaces.  Positive-row nulling splits a dagger idempotent `p`, hence produces
an object `(H,p)` in the dagger Karoubi envelope.  On that object, let

```text
a_bar=p*a,                 g_bar=p*g                       (1.1)
```

be respectively the selected negative row and the completed aggregate row.
Their basic invariant is the exterior class

```text
Omega=a_bar wedge g_bar in exterior^2(pH).                (1.2)
```

For one isolated reflected pair, completion gives

```text
g_bar=lambda*a_bar,       hence Omega=0.                  (1.3)
```

This is the categorical content of the augmented-row obstruction.  It is
also the exact content of the natural `2 x 2` **quotient-row Gram**
detector, because

```text
norm(Omega)^2
 =det [[norm(a_bar)^2, <a_bar,g_bar>],
       [<g_bar,a_bar>, norm(g_bar)^2]].                    (1.4)
```

Thus the transverse-state proposal and its quotient-row Gram-determinant
presentation are not two independent escapes.  They ask for the same
nonzero class in the positive-row quotient.  This statement does not
identify every determinant of a completed Hermitian compression with
`Omega`; those signed determinants are treated separately in Section 6.
If the full actual aggregate is

```text
g_actual=g_pair+e,
```

then

```text
Omega=a_bar wedge p*e.                                    (1.5)
```

Only the non-aligned actual completion remainder--including any
actual-prime, collateral, pole/main, or inter-scale component not already
proved negligible--can create the missing class.

The rest of the escape census falls under the following trichotomy.

```text
order-conservative dagger operation     the original sign is equivalent;
information-losing positive operation   the negative direction can be hidden;
genuinely nonlinear operation           mixed place-correlations are created.
                                                               (1.6)
```

Invertible preconditioning, honest Schur reduction, and Birman--Schwinger
belong to the first line.  Compression, dephasing, random averaging, and
local gluing belong to the second unless supplemented by an order-reflection
or observability theorem.  Determinants, exterior powers, resolvents, and
nonlinear functional calculus belong to the third unless they erase or
merely preserve the original sign.

Positive multi-witnesses fit into the `CPM(FHilb)` completion.  They do not
form a fourth case: after positive rows are nulled, the aligned mirror
inequality is stable under every mixed state and every purification.  Exact
aggregate cancellation retaining a carrier therefore requires a
carrier-sized positive transverse remainder.

Sections 3--6 state and prove these claims precisely.

## 2. The categorical dictionary

For a Hilbert space `H`, write

```text
Herm(H)={A:H->H : A^*=A},
Pos(H) ={R^*R : R:H->K for some K}.                       (2.1)
```

A state is a morphism `z:C->H`, and its evaluation on a form is
`z^* A z`.  A row map `X:H->Y` has a dagger kernel

```text
i:S=ker X -> H,
i^*i=I_S,                    p=i*i^*.                       (2.2)
```

The self-adjoint idempotent `p` is the Karoubi object representing the
feasible subspace.  Two ket rows `a,g:C->H` have the same restriction to
all homogeneous feasible corrections exactly when

```text
p*a=p*g,
```

or, equivalently, when their difference lies in `im X^*`.  Thus the usual
orthogonal quotient

```text
H/im X^*  isometrically isomorphic to ker X                 (2.3)
```

is not extra structure: it is the dagger-kernel splitting.

A positive ensemble

```text
Gamma=sum_j w_j z_j z_j^*,          w_j>=0,                (2.4)
```

is a mixed state in `CPM(FHilb)`.  Conversely every `Gamma>=0` has such a
spectral decomposition, or a purification `Gamma=V V^*`.  Every quadratic
observable remains linear at this level:

```text
Tr(A Gamma)=sum_j w_j z_j^* A z_j=Tr(V^* A V).             (2.5)
```

This explains why the covariance SDP is the natural categorical completion
of the single-witness problem rather than a different proof architecture.

Finally, the completed explicit formula is an additive identity in the
real vector space `Herm(H)`:

```text
K_completed=sum_v epsilon_v K_v=K_zero.                    (2.6)
```

Here the `v` label denotes prime, pole, archimedean, rational, selected-zero,
and collateral-zero pieces.  A construction which is not additive on
`Herm(H)` does not preserve this place decomposition componentwise.

## 3. Lemma I: dagger-Karoubi alignment

### Lemma 3.1 (alignment is natural on the feasible object)

Let `i:S->H` be the dagger kernel of a row map `X:H->Y`, and let
`a,g:C->H`.  Suppose

```text
i^*g=lambda*i^*a.                                        (3.1)
```

Then for every morphism `V:K->S`,

```text
V^*i^*g=lambda*V^*i^*a.                                 (3.2)
```

If `lambda!=0`, no complex aggregate-null vector in the image of `iV` can
retain the corresponding target amplitude.  In particular,

```text
g^*iVh=0  implies  a^*iVh=0.                             (3.3)
```

The same relation survives dagger pullback, direct sums with a common
scalar `lambda`, tensoring by an ancilla identity, and every linear functor
on morphisms.

#### Proof

Equation (3.2) is obtained by left-composing (3.1) with `V^*`.  Equation
(3.3) is its adjoint scalar evaluation.  Direct sums, tensor products, and
linear pullbacks preserve equality.  QED

This elementary naturality is the reason that a change of coordinates or a
larger supply of homogeneous corrections cannot manufacture transversality
from an exactly aligned quotient row.

There is an intrinsic dagger-kernel formulation.  Put

```text
a_bar=i^*a:C->S,             g_bar=i^*g:C->S,
k_g:T=ker(g_bar^*) -> S.                                  (3.4)
```

The exact carrier which survives both the positive rows and the complex
aggregate row is the morphism

```text
a_bar^* k_g:T->C.                                         (3.5)
```

For the two-step filtration `0 subset im X^* subset H`, the top associated
grade is `H/im X^*`.  Equation (3.1) says that its quotient classes obey

```text
[g]=lambda*[a] in H/im X^*,                              (3.6)
```

and then `a_bar^* k_g=0`.  This is the master alignment lemma in categorical
form: the second dagger kernel kills the desired carrier because the two
rows have the same class in the first quotient.

### Lemma 3.2 (one reflected pair is aligned after the positive-row quotient)

Let

```text
H=H_- direct_sum H_+,
x=x_-+x_+,              y=y_-+y_+,
K_pair=2*(x*x^*-y*y^*).                               (3.7)
```

Fix `r in H_+`.  On `H_-`, put

```text
X=x_-^*,             S=ker X,
a=y_-,               g=P_- K_pair r.                   (3.8)
```

If `i:S->H_-` is the dagger kernel of `X`, then exactly

```text
i^*g=-2*(y_+^*r)*i^*a.                                 (3.9)
```

#### Proof

Direct expansion gives

```text
g=2*x_-*(x_+^*r)-2*y_-*(y_+^*r).                      (3.10)
```

Because `i^*x_-=0`, applying `i^*` proves (3.9).  QED

Equation (3.9) is the invariant form of the projected-row identity in the
augmented-row audit.  It does not depend on a coordinate choice or on equal
packet norms.

If the full aggregate contains a remainder `e`, define the transverse
defect morphism

```text
tau=i^*e,
i^*g_actual=lambda*i^*a+tau,
lambda=-2*y_+^*r.                                     (3.11)
```

The commuting-square defect `tau` is the only linear source of an escape.
Every dagger-linear transformation sends `tau` to its image; it cannot turn
`tau=0` into a nonzero morphism.

### Lemma 3.3 (the exterior class is the exact complex-null leverage)

Let `a_bar,g_bar in S`, with `g_bar!=0`.  Then

```text
norm(a_bar^* k_g)^2
 =sup_{h in S, norm(h)=1, <g_bar,h>=0} |<a_bar,h>|^2
 =norm(a_bar)^2-|<a_bar,g_bar>|^2/norm(g_bar)^2
 =norm(a_bar wedge g_bar)^2/norm(g_bar)^2.            (3.12)
```

If `g_bar=lambda*a_bar+tau`, `lambda!=0`, then

```text
norm(P_(g_bar^perp) a_bar)
 =dist(a_bar,span(g_bar))
 <=norm(tau)/abs(lambda).                             (3.13)
```

#### Proof

The first equality is orthogonal projection onto `g_bar^perp`.  The Gram
determinant identity for the exterior product gives the second.  Finally,

```text
a_bar-(1/lambda)*g_bar=-(1/lambda)*tau,               (3.14)
```

and distance to `span(g_bar)` is no larger than the norm of this particular
difference.  QED

Two consequences are worth isolating.

1. The adaptive `2 x 2` quotient-row Gram determinant is exactly
   `norm(Omega)^2`.  It measures the same transverse defect as the linear
   aggregate-row problem; it does not create a new direction.
2. For the isolated pair, (3.9) gives `Omega=0`.  For the actual completed
   problem, (1.5) says that a nonzero quotient-row Gram determinant must be
   paid for entirely by an actual-prime, collateral, pole/main, or
   inter-scale remainder.

There is an important real-affine nuance.  A single *homogeneous* constraint
`Re <g_bar,h>=0` does not lose modulus-valued target leverage, because one
may phase-rotate `h`.  The balanced mirror fails the one-real equation for
an affine reason: the positive-row datum leaves no homogeneous correction
with which to cancel its nonzero completed cross scalar.  Lemma II treats
that real quadratic formulation without replacing it by complex
orthogonality.

## 4. Lemma II: the aligned cone is stable in `CPM(FHilb)`

### Lemma 4.1 (mixed-state aligned-cone lemma)

Let `p` be a dagger idempotent, let `N>=0`, and suppose the compressed
Hermitian aggregate observable `B` obeys

```text
p B p <= -c*p N p,             c>0.                  (4.1)
```

Then every mixed state `Gamma>=0` supported by `p` satisfies

```text
Tr(B Gamma)<=-c*Tr(N Gamma).                          (4.2)
```

Consequently

```text
Tr(B Gamma)=0  implies  Tr(N Gamma)=0.                (4.3)
```

More generally, if `B_actual=B+R` and
`Tr(B_actual Gamma)=0`, then

```text
c*Tr(N Gamma)
 <=Tr(R Gamma)
 <=norm((p R p)_+)*Tr(Gamma).                         (4.4)
```

#### Proof

Write `Gamma=V V^*`.  Pulling (4.1) back by `V` gives

```text
V^* B V<=-c*V^* N V.                                 (4.5)
```

Taking traces proves (4.2).  Equation (4.3) follows because both
`Tr(N Gamma)` and `-Tr(B Gamma)` are nonnegative.  Aggregate cancellation
gives `Tr(R Gamma)=-Tr(B Gamma)`, while the last bound in (4.4) is the
variational bound for the positive part of `pRp`.  QED

This is stable not merely under a listed collection of witnesses but under
every purification and ancilla in `CPM(FHilb)`.  Positive ensembles,
real/imaginary quadratures, and positive random mixtures are therefore one
case of the same lemma.

Positive-row nulling is itself stable under passage to mixed states.  If
`P=X^*X`, then

```text
Tr(P Gamma)=norm(X Gamma^(1/2))_HS^2=0
 iff range(Gamma) subset ker X.                       (4.6)
```

Thus an ensemble cannot average away a positive evaluation row; it really
descends to the Karoubi object `p`.

This also locates the exact boundary between Lemmas I and II.  If every
constituent witness is required to satisfy the complex aggregate row, or if
the mixed constraint is the positive energy

```text
Tr(g_bar*g_bar^* Gamma)=0.                           (4.6a)
```

then (4.6), applied once more, forces the mixed state through the second
dagger kernel `k_g`; the surviving carrier is precisely
`a_bar^*k_g` from (3.5).  The minimal aggregate condition used in the
multi-witness audit is weaker and signed:

```text
Tr(B Gamma)=0.                                       (4.6b)
```

It does not put each purification component in `ker(g_bar^*)`.  That is why
the correct CPM statement for the minimal one-real equation is the
order inequality (4.1), rather than a mistaken componentwise row null.

### Corollary 4.2 (exact constants for the normalized mirror)

For one normalized pair, write

```text
M=m*[[1,C],[C,1]]=m*(I+C*J),
m>0,                  C=cosh(alpha*D)>1,
J=[[0,1],[1,0]],                                      (4.7)

e_+=(1,1)/sqrt(2),      e_-=(1,-1)/sqrt(2),
P=m*(1+C)*e_+e_+^*,     N=m*(C-1)*e_-e_-^*,
B=m*C*J,                M=P-N=m*I+B.                 (4.8)
```

Nulling the positive row splits `p_-=e_-e_-^*`.  On that object,

```text
p_- B p_-=-m*C*p_-
          =-[C/(C-1)]*N
          <=-N.                                      (4.9)
```

The factor `C/(C-1)` is the optimal blockwise aligned-cone constant.  For a
direct sum of normalized mirrors,

```text
p B p=-sum_j m_j*C_j*p_(j,-),
p N p= sum_j m_j*(C_j-1)*p_(j,-).                   (4.10)
```

Hence a positive ensemble can cancel the completed cross scalar only after
all retained mirror carriers vanish, unless a remainder `R` satisfies the
carrier-scale lower bound (4.4).

The normalizations in the current Gabor realization are

```text
m=2*A_alpha^2/L,
C=cosh(alpha*D),
K=(m/2)*C.                                           (4.11)
```

For the positive-null vector `z=(s,-s)`, exact evaluation gives

```text
norm(z)^2=2*|s|^2,
aggregate half-cross =-m*C*|s|^2=-2*K*|s|^2,
full cross           =-2*m*C*|s|^2=-4*K*|s|^2,
z^*M z               =2*m*(1-C)*|s|^2
                     =-4*K*|s|^2+2*m*|s|^2.         (4.12)
```

These factors agree with the normalized mirror and augmented-row audits.

There is also a no-leakage identity before positive-row nulling.  For every
positive covariance on the full direct sum,

```text
Tr(B Gamma)=0
 implies Tr(M Gamma)=sum_j m_j*Tr(Gamma_j)>=0.        (4.13)
```

Thus allowing positive-mode leakage cannot preserve a negative mirror value
while canceling its completed cross scalar.

### Corollary 4.3 (one real aggregate row has a pure-state optimum)

On one common feasible space, consider

```text
Gamma>=0,       Tr(Gamma)=1,       Tr(B Gamma)=0.     (4.14)
```

Every extreme point has rank one.  Indeed, if an extreme point had rank
`r>=2`, Hermitian perturbations on its range would have real dimension
`r^2>=4`; the two real equations in (4.14) leave a nonzero perturbation, and
small positive and negative multiples preserve positivity.  This
contradicts extremality.

Therefore any linear objective over (4.14) has a single coherent witness as
an optimizer.  Multi-witness convexification is useful bookkeeping, but it
does not improve the optimum.  The direct-sum aligned inequality (4.10),
not this rank statement, handles separately labelled support scales.

## 5. Lemma III: positive observations are conservative or forgetful

### Lemma 5.1 (order-reflection dichotomy)

Let

```text
Phi:Herm(H)->Herm(K)                                  (5.1)
```

be positive and real-linear.

* If `Phi` is order-reflecting, meaning

  ```text
  Phi(A)>=0 implies A>=0,                             (5.2)
  ```

  then positivity of `Phi(A)` is equivalent to positivity of `A`.  The
  transformation may simplify coordinates, but it does not weaken the
  theorem to be proved.
* If `Phi` is not order-reflecting, positivity of `Phi(A)` cannot by itself
  certify positivity of `A`.  One needs an additional theorem restricting
  the allowed operators to a subclass on which `Phi` becomes
  order-reflecting.

If `Phi` has a nonzero self-adjoint kernel element `X`, the failure can be
made explicit: fix `mu>0`; for a suitable sign of `X` and sufficiently large
`t`,

```text
A=mu*I+t*X                                             (5.3)
```

is not positive semidefinite while `Phi(A)=mu*Phi(I)>=0`.

This is formally elementary, but it is the precise categorical distinction
between a faithful proof transform and a lossy observation.

### Lemma 5.2 (dagger pullback is order-reflecting exactly when it sees all
directions)

For a morphism `S:K->H`, put

```text
Phi_S(A)=S^* A S.                                     (5.4)
```

Then `Phi_S` is order-reflecting on all Hermitian forms if and only if `S`
is surjective.

#### Proof

If `S` is surjective and `S^*AS>=0`, every `h in H` equals `Sk` for some
`k`, and

```text
h^*Ah=k^*S^*ASk>=0.                                  (5.5)
```

Conversely, if `S` is not surjective, choose a unit vector
`w perpendicular to range(S)` and `t>1`.  Then

```text
A=I-t*w*w^*                                           (5.6)
```

has eigenvalue `1-t<0`, while `S^*AS=S^*S>=0`.  QED

An invertible preconditioner is therefore an order isomorphism; Sylvester
inertia gives the stronger equality of negative indices.  A singular heat
limit or proper compression can lose the mirror only by ceasing to see its
negative direction.  Recovering the original conclusion then requires the
missing inverse or observability estimate.

### Lemma 5.3 (no finite family of proper local subobjects is universally
order-reflecting)

Let `E_1,...,E_q` be finitely many proper subspaces of `H`.  There exists an
Hermitian `A` which is not positive semidefinite, while its compression to
every `E_j` is positive semidefinite.  If `dim H>=2`, the construction may be
taken indefinite.

#### Proof

Choose a unit vector `w` outside the finite union of the `E_j`, and let

```text
q_0=max_j norm(P_(E_j) w)^2<1.                       (5.7)
```

Choose `1<t<=1/q_0` when `q_0>0`, and any `t>1` when `q_0=0`.  Put

```text
A=I-t*w*w^*.                                         (5.8)
```

For `v in E_j`,

```text
v^*Av=norm(v)^2-t*|<w,v>|^2
     >=(1-t*q_0)*norm(v)^2>=0,                       (5.9)
```

whereas `w^*Aw=1-t<0`.  QED

This single lemma contains the qualitative obstruction behind fixed test
banks and finite local-gluing schemes.  The repository's `3 x 3` Toeplitz
and continuous triangular-packet countermodels strengthen it by preserving
the relevant translation structure and by handling an infinite parametric
family of interval packets.

### Schur and Birman--Schwinger are conservative pullbacks

For

```text
K=[[A,B],[B^*,D]],             D>0,                  (5.10)
```

the harmonic graph morphism

```text
J_D x=(x,-D^(-1)B^*x)                                  (5.11)
```

satisfies

```text
J_D^* K J_D=A-B D^(-1)B^*,
J_D^*J_D=I+B D^(-2)B^*.                              (5.12)
```

An invertible block Gaussian congruence identifies `K` with the direct sum
of `D` and this Schur complement.  Consequently, once `D>0`, Schur
positivity is exactly the unresolved last pivot; dropping the graph metric
in (5.12) creates a false amplification.

For the mirror, the scalar pivot and graph metric are

```text
m*(1-C^2),                    1+C^2,                 (5.13)
```

so the normalized quotient tends to `-m`, not to the exponential carrier
`-m*C`.

Likewise, if `P>0`,

```text
P-R=P^(1/2)*[I-P^(-1/2)R P^(-1/2)]*P^(1/2).         (5.14)
```

The Birman--Schwinger crossing is an invertible dagger congruence and hence
an equivalent sign statement.  Resolvent reconstruction of the negative
projection is an order-conservative reformulation only after one proves the
very norm/crossing estimate at issue.

### Dephasing and local gluing are forgetful observations

The diagonal conditional expectation `E` gives the exact mirror example

```text
E(m*(I+C*J))=m*I>=0,
m*(I+C*J) has eigenvalue m*(1-C)<0.                  (5.15)
```

It kills the off-diagonal carrier `J`.  Random phase averaging and block
dephasing have the same structure.  A local-gluing map

```text
A |-> direct_sum_j V_j^* A V_j                       (5.16)
```

is useful only if it is order-reflecting on the completed zeta operator
class.  The triangular-packet countermodels prove that the current local
family is not.  An IMS or observability estimate capable of repairing
(5.16) must therefore control exactly the nonlocal cross term that the map
forgets.

## 6. Lemma IV: an additive nonlinear escape is linear

The first three sections cover dagger-linear and positive constructions.
The remaining possibility is to apply a determinant, exterior power,
resolvent, Schur map, or spectral nonlinearity to the completed identity.
The following elementary lemma explains the unavoidable arithmetic cost.

### Lemma 6.1 (only affine scalar calculus preserves every additive place
decomposition)

Let `f:R->R` be continuous and suppose

```text
f(A+B)=f(A)+f(B)-f(0)                                (6.1)
```

for all commuting finite Hermitian `A,B`.  Then

```text
f(t)=f(0)+c*t                                        (6.2)
```

for a real constant `c`.

#### Proof

Apply (6.1) to `1 x 1` matrices.  The continuous function
`h(t)=f(t)-f(0)` satisfies Cauchy's equation `h(s+t)=h(s)+h(t)`, hence is
linear.  QED

Therefore a continuous spectral calculus has only three relevant outcomes.

1. If it is affine and sign-preserving, it retains the original negative
   index.
2. If it sends every scalar to a nonnegative scalar, as do `t^2`, `|t|`,
   and `exp(-u*t^2)`, it erases the sign.
3. If it is genuinely nonlinear and retains sign information, it does not
   preserve (2.6) term by term.  Its arithmetic side contains mixed-place
   expressions.

For a polynomial this is completely explicit:

```text
(A+B)^k-A^k-B^k
 =sum of all noncommutative words containing both A and B.   (6.3)
```

Taking traces turns these words into mixed correlations.  Newton identities
show that determinant coefficients have the same cost.  Exterior powers of
`A+B` contain polarized mixed discriminants, and a Schur complement or
resolvent contains mixed inverse products.  Applying the nonlinearity
separately to each place avoids the mixed terms only by ceasing to be the
nonlinearity of the completed operator.

This is the categorical point: a genuinely nonlinear functional calculus
is not an enrichment-preserving map of the additive hom-space
`Herm(H)`.  It cannot be both a nonlinear amplifier and a functorial
preserver of the prime + pole + archimedean - zero decomposition.

### Corollary 6.2 (low-order nonlinear certificates do not bypass the
mixed-correlation gate)

On the selected two-packet zero block,

```text
det M=-m^2*sinh(alpha*D)^2<0.                        (6.4)
```

This signed determinant correctly detects the mirror.  It is not the
positive Gram determinant (1.4): indeed, (6.4) is negative while every Gram
determinant is nonnegative.  The two constructions nevertheless expose two
faces of the same research gate.  After positive-row quotienting, the
quotient-row Gram determinant is (1.4), and by (1.5) its nonzero part comes
entirely from the actual transverse remainder.  For the distinct completed
Hermitian determinant (6.4), continuous Cauchy--Binet/Andreief expands the
arithmetic side into signed prime--prime, pole--prime, and collateral
two-correlations.  Neither quantity follows from the global first two
moments; each needs target-specific actual arithmetic information.

Predetermined low-order minors are lossy observations in the sense of
Lemma 5.1.  Quantitatively, the flat-defect moment countermodel in
`ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md` has the exact
first two Zeta23 moments, one eigenvalue `-kappa`, and every coordinate
compression through order

```text
r<=N/(1+3*kappa)                                     (6.5)
```

positive semidefinite.  An adaptive minor can find the defect only by
depending on the negative spectral data.  Its arithmetic realization is
then the new mixed-correlation theorem, not a consequence of the global
moments.

## 7. The categorical escape theorem

The preceding lemmas can be packaged as one scoped theorem.

### Theorem 7.1 (conservative--forgetful--nonlinear trichotomy)

Assume a finite completed Weil compression contains a normalized mirror
subquotient (4.7), and let positive evaluation rows be split by a dagger
idempotent `p`.  Consider a certificate assembled by finitely many of the
following operations:

1. dagger pullback/congruence, biproduct, Karoubi splitting, or tensoring by
   a finite ancilla;
2. positive mixtures/covariances and positive linear observations;
3. Schur, resolvent, determinant, exterior-power, or continuous spectral
   operations, while retaining the completed arithmetic identity.

Then every such certificate is in at least one of the following classes.

```text
(A) Conservative:
    it is order-reflecting on the completed operator class and hence proves
    a sign statement equivalent to the original one.

(B) Forgetful:
    it is not order-reflecting and needs an independent zeta-specific
    observability/cross-term theorem to recover the discarded direction.

(C) Nonlinear:
    it introduces mixed prime/pole/archimedean/collateral products whose
    control is a new arithmetic correlation theorem.                 (7.1)
```

Moreover, on the positive-null mirror face, every aggregate-null positive
state retaining carrier `Tr(N Gamma)` forces

```text
norm((p R p)_+)*Tr(Gamma)>=Tr(N Gamma),              (7.2)
```

where `R` is the non-aligned actual remainder.  In the single-seed complex
row formulation, the same missing content is measured by

```text
Omega=(p*a) wedge (p*g_actual)
     =(p*a) wedge (p*e).                              (7.3)
```

#### Proof

Operations in item 1 are dagger-linear.  If their pullback is
order-reflecting, Lemma 5.2 puts them in (A); otherwise Lemmas 5.1--5.3 put
them in (B).  Karoubi restriction preserves the alignment relation by
Lemma 3.1.

Positive mixtures in item 2 are mixed states in `CPM(FHilb)`.  Lemma 4.1
gives (7.2); positive observations again obey Lemma 5.1.  Thus they belong
to (A) or (B) and cannot generate a transverse remainder from zero.

Schur and Birman--Schwinger operations are conservative congruences when
their stated positive/invertible hypotheses hold.  A sign-erasing spectral
map is forgetful.  Continuous scalar spectral maps fail universal place
additivity by Lemma 6.1; determinant, exterior, polynomial, Schur, and
resolvent operations have the mixed expansions described in Section 6.
An operator-specific identity making those mixed terms cancel would be a new
arithmetic law, not a consequence of the formal operation classified here.
Finally, (7.3) is Lemmas 3.2--3.3.  QED

The classes can overlap: a Schur map, for example, is conservative for the
full block but nonlinear with respect to its separate place summands.  The
theorem says that at least one cost is unavoidable; it does not claim a
unique label.

## 8. Collapse table for the existing escape census

```text
positive multi-witness / covariance       Lemma 4.1, CPM stability;
real-imaginary quadrature                  the same mixed-state lemma;
positive multiscale direct sum             exact block inequality (4.10);
signed scale sum                           not a positive CPM state;
positive-row nulling                       dagger Karoubi object (H,p);
augmented complex aggregate row            quotient alignment, Lemma 3.2;
actual target-transverse state             nonzero Omega / positive part of R;
adaptive quotient-row Gram test             norm(Omega)^2;
completed 2x2 determinant or Pick test      signed mixed two-correlations;
fixed minor/test bank                       non-order-reflecting observation;
invertible preconditioning                 order-isomorphic pullback;
singular smoothing/compression             forgetful pullback;
Schur/Hodge/Dirichlet-to-Neumann            harmonic graph congruence;
Birman--Schwinger                           invertible congruence;
resolvent or spectral projection           equivalent sign, or mixed products;
randomization/dephasing                     non-order-reflecting CP observation;
local positivity gluing                     non-order-reflecting observation;
square/absolute value/positive heat         sign-forgetting calculus;
sign-preserving functional calculus         same index, mixed arithmetic side;
determinant/exterior/higher moments          mixed-place correlations.       (8.1)
```

The table replaces many route-specific slogans with a small set of proofs.  It also
clarifies which transformations can still be useful computationally: an
order-conservative transform may greatly improve numerical conditioning,
and a nonlinear transform may expose an estimable correlation.  What it
cannot do is supply the missing estimate merely by being a transformation.

## 9. The consolidated research target

There are two equivalent-looking but differently useful presentations of
the remaining zeta-specific content.

### Operator-cone presentation

Decompose the compressed actual aggregate on the positive-null face as

```text
B_actual=B_align+R,
B_align<=-N.                                         (9.1)
```

One must prove either

```text
norm((p R p)_+)=o(K)                                 (9.2)
```

uniformly, which closes every positive-ensemble escape at carrier scale
`K`, or construct a positive state for which the positive part of `R` is
carrier-sized and its full completed-form cost is smaller than the retained
negative carrier.

### Exterior-class presentation

For a fixed seed, prove either

```text
p*g_actual=lambda*p*a+o_carrier                     (9.3)
```

uniformly, which collapses the complex target leverage by (3.13), or, when
`p*g_actual!=0`, prove a uniform lower bound for

```text
norm((p*a) wedge (p*g_actual))/norm(p*g_actual).     (9.4)
```

The latter is simultaneously a transverse-row theorem and an adaptive
`2 x 2` quotient-Gram theorem; using it for a negative-witness construction
also requires control of the full completed-form cost.  A signed
completed-Weil or Pick determinant remains a different nonlinear
certificate, but Section 6 shows that its arithmetic proof must control
corresponding mixed correlations.

These presentations are not identical for every affine real SDP, but they
locate the same source of new information: the component of the actual
completion remainder transverse to the isolated reflected-pair class.  No
basis change, positive ancilla, quotient, or nonlinear renaming creates that
component.

## 10. Novelty and scope assessment

The strongest new project-level insight is (1.2)--(1.5): the quotient-row
Gram presentation and the target-transverse row escape are the same exterior
class in the dagger positive-row quotient.  This should not be conflated
with the distinct signed determinant of the completed Weil compression.
The exact optimal
mirror constant `C/(C-1)` in (4.9) and the unified trichotomy (7.1) make the
existing collection of no-go results substantially easier to reuse.

The underlying abstract ingredients--dagger kernels, purification of
positive matrices, order reflection, Sylvester/Haynsworth inertia, and the
continuous Cauchy equation--are standard and elementary.  The categorical
packaging should therefore be presented as a synthesis theorem for this
specific completed-Weil architecture, not as a novel theorem of category
theory.  It becomes mathematically substantive for the zeta problem only
when paired with a new estimate for (9.2) or (9.4).

## 11. Source cross-links

The exact inputs consolidated here are:

- `ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md`;
- `ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md`;
- `ZETA23-LOW-ORDER-NONLINEAR-CERTIFICATE-NOGO-2026-08-12.md`;
- `ZETA23-OPERATOR-PRECONDITIONING-FUNCTIONAL-CALCULUS-AUDIT-2026-08-12.md`;
- `TRIANGULAR-PACKET-CONE-NOGO.md`;
- `ZETA23-LESS-OBVIOUS-ESCAPES-MASTER-AUDIT-2026-08-12.md`.
