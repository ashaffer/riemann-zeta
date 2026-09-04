# Operator preconditioning and functional calculus preserve or erase the mirror obstruction

Status: exact inertia, Schur-complement, Birman--Schwinger, nonlinear
additivity, resolvent, and heat-flow classification for the normalized
mirror block, 2026-08-12.  Generic operator transformations do not create a
new uniform-strip mechanism.  A zeta-specific transformed inequality could
still be substantive, but it must control the same completed
prime/collateral block.  No zero-free strip is proved or disproved.

## 1. Verdict

For the current completed Weil/Gabor route, the common operator
transformations divide into three exact classes.

```text
invertible congruence / nonunitary metric change       SAME INERTIA;
positive-block Schur elimination                       SAME LAST PIVOT;
Birman--Schwinger / shifted resolvent                   EQUIVALENT CROSSING;

square, absolute value, positive heat kernel            ERASES THE SIGN;

sign-preserving nonlinear functional calculus           SAME SIGN PROBLEM,
                                                        NONADDITIVE PRIME SIDE. (1.1)
```

The normalized mirror block makes each statement explicit.  A nonunitary
coordinate change can make an unnormalized negative entry arbitrarily
large, but the transported norm pays the inverse condition number.
Eliminating one positive lobe produces a Schur pivot of apparent size
`m*C^2`, but its harmonic extension has squared norm `1+C^2`; the normalized
edge is only `O(m)` and the original exponential carrier is lost.  Eliminating
the true positive eigenmode simply leaves the original negative eigenvalue.

Squaring or applying a positive heat kernel makes every eigenvalue
nonnegative and forgets which one was negative.  The matrix sign and
sign-preserving resolvents retain the negative index, but constructing them
requires the full completed spectral projection.  They have no additive
pole + archimedean - prime decomposition.  In fact, a continuous scalar
functional calculus preserves a universal additive place decomposition only
when it is affine.

Thus these operations may repackage the actual-prime transverse theorem,
and some may be useful numerically, but none supplies it.  A successful
revival must prove a new coefficient-specific bound for a transformed
mixed operator; calling the transform a preconditioner, Green function,
heat flow, or sign operator does not provide that bound.

## 2. Exact normalized mirror block

Retain the exact two-packet compression

```text
M=m*[[1,C],[C,1]]=m*(I+C*sigma_x),
m>0,                 C=cosh(alpha*D)>1.             (2.1)
```

With

```text
e_+=(1,1)/sqrt(2),       e_-=(1,-1)/sqrt(2),        (2.2)
```

the eigenvalues are

```text
p=m*(1+C)>0,
-n=m*(1-C)<0,            n=m*(C-1).                 (2.3)
```

The negative carrier has size `n=X^(alpha*d-o(1))/L`.  The completed
explicit formula is an operator identity

```text
K_comp=K_zero.                                       (2.4)
```

Therefore every transformation applied honestly to the **full** completed
operator gives the same transformed operator on the arithmetic and zero
sides.  The question is whether the transform preserves a tractable
arithmetic decomposition while improving the sign.  The sections below
show the exact obstruction.

## 3. Invertible metric changes preserve the problem

Let `S` be any invertible matrix and set

```text
M_S=S^* M S.                                         (3.1)
```

Sylvester inertia and the determinant give

```text
inertia(M_S)=inertia(M)=(1,1),
det(M_S)=abs(det S)^2*det(M)<0.                      (3.2)
```

Thus no invertible preconditioner removes the negative direction.  It may
appear to amplify it if `M_S` is measured against the old Euclidean norm.
The physical coordinate is `z=S*y`, however, so the transported metric is

```text
G_S=S^*S.                                            (3.3)
```

The generalized quotient is exactly unchanged:

```text
(y^*M_S y)/(y^*G_S y)=(z^*M z)/(z^*z).              (3.4)
```

Any apparent gain in the numerator alone is a condition-number debt in
(3.3).  A similarity `S^(-1)MS` preserves the spectrum; if it is not
Hermitian in the Euclidean metric, it is self-adjoint in the transported
metric and again gives (3.4).

For example, whitening the positive diagonal `mI` gives

```text
m^(-1/2) M m^(-1/2)=I+C*sigma_x,                    (3.5)
```

whose negative eigenvalue is still `1-C`.  Since (2.4) also gives

```text
S^*K_comp S=S^*K_zero S,                            (3.6)
```

the prime, pole, zero, and collateral rows are all transformed by the same
congruence.  A target-adaptive `S` can be useful only if one independently
controls its condition number and the transformed actual-prime remainder.

## 4. Positive-block elimination and the normalization debt

For a general Hermitian block

```text
K=[[A,B],[B^*,D]],                D>0,               (4.1)
```

the exact Schur complement is

```text
S_D=A-B*D^(-1)*B^*.                                  (4.2)
```

Block Gaussian congruence gives Haynsworth additivity

```text
inertia(K)=inertia(D)+inertia(S_D).                 (4.3)
```

Consequently the sign of the Schur complement is exactly the unresolved
sign of the full operator after a known positive sector is removed.  It is
a valuable reduction, not an independent inequality.

The normalization issue is visible in (2.1).  Eliminate the second lobe,
whose diagonal block is `D=m`.  Then

```text
S_D=m*(1-C^2).                                       (4.4)
```

This looks larger than the original carrier by a factor `C`.  But the
harmonic lift of a scalar `x` is

```text
J*x=(x,-C*x),
(J*x)^*M(J*x)=m*(1-C^2)*abs(x)^2,
norm(J*x)^2=(1+C^2)*abs(x)^2.                       (4.5)
```

Hence its normalized quotient is

```text
m*(1-C^2)/(1+C^2) -> -m,                            (4.6)
```

not the carrier `-m*C`.  The large Schur pivot is paid by a harmonic
extension of norm `C`.  If instead one eliminates the true positive
eigenmode `e_+`, the Schur complement is simply `-n`, the original negative
eigenvalue.

In (4.1), the general effective norm is

```text
J^*J=I+B*D^(-2)*B^*.                                 (4.7)
```

Dropping (4.7) is exactly the normalization error illustrated by
(4.4)--(4.6).

There is also no componentwise Schur formula:

```text
Schur(K_1+K_2) != Schur(K_1)+Schur(K_2)              (4.8)
```

in general, even for small matrices.  The inverse in (4.2) contains the
complete prime--pole--archimedean--zero block and generates mixed products.
Taking the Schur complement of (2.4) preserves equality, but it does not
turn the prime part into a separate positive or small term.

## 5. Birman--Schwinger and resolvent reformulations

Suppose

```text
K=P-R,                         P>0.                  (5.1)
```

Then exactly

```text
K>=0
 iff I-P^(-1/2) R P^(-1/2)>=0
 iff lambda_max(P^(-1/2) R P^(-1/2))<=1.           (5.2)
```

This is the Birman--Schwinger crossing criterion.  For the mirror block,
take

```text
P=mI,                   R=-m*C*sigma_x.             (5.3)
```

The Birman--Schwinger matrix is `-C*sigma_x`, with largest eigenvalue `C>1`.
It records the same negative direction in dimensionless coordinates.

Adding an arbitrary positive shift changes the numerical distance from one
but not the equivalence.  A Neumann or resolvent estimate proving

```text
norm(P^(-1/2) R P^(-1/2))<1                         (5.4)
```

already proves the desired positivity.  The generic log-elliptic
preconditioner tested in the repository tracks the original ground vector
and its margin; no independent interlacing or prime-event sign was found.

If `K` is invertible, `K^(-1)` has the same inertia and replaces each
eigenvalue by its reciprocal.  It suppresses the large mirror carrier
`-n` to `-1/n`.  Shifted resolvents can recover the negative spectral
projection only through a contour enclosing the negative spectrum:

```text
P_-=(1/(2*pi*i))*integral_Gamma (z-K)^(-1)dz.       (5.5)
```

Computing or signing (5.5) is the original negative-subspace problem.
Resolvent expansions around a tractable `P` converge under conditions such
as (5.4); without them, all mixed prime/collateral products return.

## 6. Exact functional-calculus dichotomy

Let `f:R->R` be real Borel and apply the spectral calculus to a finite
Hermitian `K`; continuity will be imposed for the additive theorem below.

### 6.1 Sign-erasing maps

The maps

```text
K^2,       abs(K),       exp(-t*K^2)                (6.1)
```

are positive semidefinite for every `K`.  They cannot distinguish the
mirror block from a positive operator.  For (2.1), squaring sends the two
eigenvalues to `p^2,n^2` and deletes which spectral line carried the minus
sign.

### 6.2 Sign-preserving maps

If

```text
f(0)=0,
sign(f(x))=sign(x)             for every x!=0,       (6.2)
```

then the spectral theorem gives

```text
negative_index(f(K))=negative_index(K),
f(K)>=0 iff K>=0.                                    (6.3)
```

Such a map may rescale the carrier but cannot make proving its absence
easier by order theory alone.  Examples include

```text
K*exp(-t*K^2),
K*(K^2+eta^2)^(-1/2),
sign(K).                                             (6.4)
```

For the isolated mirror block,

```text
sign(M)=sigma_x.                                     (6.5)
```

This is an exact amplitude-independent detector.  For the full completed
operator, however, `sign(K)=P_+-P_-` (and `I-2P_-` when `K` is invertible);
constructing it is exactly constructing the forbidden spectral projection
(5.5).

### 6.3 Nonlinear maps destroy additive completion

Equation (2.4) implies

```text
f(K_comp)=f(K_zero).                                 (6.6)
```

But a nonlinear `f` does not preserve the arithmetic decomposition.  This
has a sharp universal form.

### Theorem 6.1 (only affine functional calculus is place-additive)

Suppose a continuous `f:R->R` satisfies

```text
f(A+B)=f(A)+f(B)-f(0)                               (6.7)
```

for all commuting finite Hermitian `A,B`.  Then

```text
f(x)=f(0)+c*x                                       (6.8)
```

for one real constant `c`.

#### Proof

Apply (6.7) to `1 x 1` matrices and put `g(x)=f(x)-f(0)`.  Then
`g(x+y)=g(x)+g(y)`.  Continuity makes the additive function linear.  QED

Thus every genuinely nonlinear amplifier introduces mixed
prime--prime, prime--archimedean, pole--prime, and collateral products.  If
one instead applies `f` separately to the place pieces, the result is not
`f(K_comp)` and no longer equals the transformed zero operator.  Controlling
the mixed products is a new arithmetic theorem, not a consequence of
functional calculus.

## 7. Heat smoothing and singular limits

Let `T_t` be a prescribed smoothing operator and consider

```text
K_t=T_t^* K T_t.                                     (7.1)
```

In every finite Gabor space, an invertible `T_t` gives a congruence and
preserves inertia by Section 3.  Both sides of completion receive the same
smoothing:

```text
T_t^*K_comp T_t=T_t^*K_zero T_t.                    (7.2)
```

If `T_t` becomes noninvertible, a negative direction can disappear only by
leaving its range or collapsing into its kernel.  Recovering it uniformly
as `t` changes requires an inverse/observability estimate whose condition
number is exactly the lost carrier cost.  In infinite dimension, a compact
heat semigroup has an unbounded inverse; passing to its range without paying
that inverse can silently discard the mirror packet.

Heat flow generated by `K` itself returns to Section 6.  The positive heat
operator `exp(-tK^2)` erases sign, while `K exp(-tK^2)` preserves sign and
the original negative index.  The elementary maximum-principle route for
the associated theta/Laguerre density also has an indefinite forcing term;
there is no generic no-collision inequality.

## 8. Hodge lifts and commutators

A Hodge lift or auxiliary positive square can enlarge the operator, but
eliminating that positive sector returns its Schur complement.  Haynsworth
additivity shows that the last negative pivot has not disappeared.  The
repository's exact Dirichlet-to-Neumann audit reaches precisely

```text
lambda-<r,D^(-1)r>,                                  (8.1)
```

whose sign is the unresolved enlarged-window positivity statement.
Analytic continuation or renaming (8.1) a boundary response does not sign
it.

Regular virial/Mourre commutators also do not amplify the carrier.  If
`K psi=lambda psi` and the products are defined, then

```text
<psi,[K,G]psi>=0.                                    (8.2)
```

A strict positive commutator on the negative spectral subspace can hold only
when that subspace is already empty.  Compression can manufacture a
positive commutator only by dropping the compensating boundary leakage.
Singular or support-moving generators remain outside the regular theorem,
but their exact defect is the existing endpoint/collar and completed-flux
problem, not a free commutator gain.

## 9. Exact classification and scope

The following routes are closed as generic transformations of the current
mirror/explicit-formula problem:

1. an invertible nonunitary basis or metric change;
2. eliminating a positive block while dropping its harmonic-extension norm;
3. Birman--Schwinger or resolvent reformulation without a new crossing bound;
4. squaring, absolute value, or a positive heat kernel as a sign detector;
5. a fixed sign-preserving scalar calculus treated as easier positivity;
6. applying a nonlinear map separately to prime, pole, and archimedean
   pieces; and
7. a regular commutator whose strict estimate is tested on the spectral
   subspace it is meant to exclude.

Not closed is a genuinely new **zeta-specific** transformed estimate: for
example, an arithmetically canonical preconditioner with a uniformly bounded
condition number and an independently signed prime-event law, or a nonlocal
mixed resolvent inequality which controls every term generated by Theorem
6.1.  Proving such a statement would be real progress.  It is not supplied
by the transformation itself and remains another formulation of the actual
prime/collateral gate.

Exact cross-links:
[`BIRMAN-SCHWINGER-CHECKPOINT.md`](BIRMAN-SCHWINGER-CHECKPOINT.md),
[`HODGE-LOW-SECTOR-DTN-NOGO.md`](HODGE-LOW-SECTOR-DTN-NOGO.md),
[`COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md`](COMPLETED-WEIL-VIRIAL-COMMUTATOR-NOGO.md),
[`THETA-HEAT-EVOLUTION-AUDIT.md`](THETA-HEAT-EVOLUTION-AUDIT.md),
[`NEVANLINNA-NEGATIVE-SQUARE-GATE.md`](NEVANLINNA-NEGATIVE-SQUARE-GATE.md),
and
[`ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md`](ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md).
