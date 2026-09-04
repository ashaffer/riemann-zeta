# Multi-witness aggregate cancellation is an exact semidefinite problem

Status: exact positive-ensemble reduction, exact one-real-row SDP and dual,
an aligned direct-sum no-go, and an exact transverse-reservoir escape
criterion, 2026-08-12.  The isolated completed mirror blocks admit no
multi-witness or multi-scale cancellation.  Whether the **actual** raw-prime
operator supplies the required opposite-sign reservoir is not proved.  No
zero-free strip is proved or disproved.

## 1. Verdict

Using two or more witnesses is logically legitimate only with
**nonnegative** weights.  If

```text
sum_j w_j Q(f_j)<0,             w_j>=0,             (1.1)
```

then at least one `f_j` is a negative Weil direction.  Such an ensemble is
represented exactly by one positive-semidefinite covariance matrix.  Its
combined real aggregate-prime cancellation is one linear trace equation.

This observation does not evade the completed one-pair alignment:

1. On one common admissible witness space, an SDP with normalization and
   one real aggregate equation always has a rank-one optimum.  Multiple
   witnesses cannot improve any linear carrier or full-form objective over
   one coherently chosen witness.
2. On a direct sum of normalized asymmetric mirror blocks, nulling the
   positive rows makes every completed cross block negative semidefinite.
   All selected carriers therefore have the same real sign, independently
   of seed phase, real/imaginary quadrature, support length, or positive
   ensemble weight.  Their aggregate can vanish only when every selected
   carrier vanishes.  More strongly, even without positive-row nulling,
   canceling the completed cross scalar makes the total mirror-pair form
   nonnegative.
3. Signed weights can cancel those rows algebraically, but a negative signed
   sum does not imply that any constituent Weil form is negative.

There is one genuine abstract escape.  The actual raw-prime cross operator,
after compression to the positive-null face, could have an opposite-sign,
target-neutral state.  Mixing that reservoir state with the selected
carrier state cancels the one real row while retaining a fixed carrier
fraction exactly when the reservoir trace is carrier-sized.  The explicit
formula then forces that opposite sign to come from pole/archimedean terms,
collateral zero rows, or nonorthogonal inter-scale cross terms of the same
size as the selected carrier.  None of the current count or moment inputs
proves such a reservoir for the actual zeta/von Mangoldt operators.

Thus multi-witness cancellation is not a free escape and is not a new
dimension argument.  Its exact unresolved content is the sign and size of
one compressed actual-prime operator.

## 2. Positive ensembles are PSD covariances

Let the finite admissible packet space, after support and endpoint
conditions, be

```text
H=H_- direct_sum H_+,
z_j=ell_j direct_sum r_j.                            (2.1)
```

For nonnegative weights define

```text
Gamma=sum_j w_j z_j z_j^* >=0.                      (2.2)
```

Every positive-semidefinite `Gamma` has such a decomposition, by its
spectral theorem.  For every Hermitian observable `A`,

```text
Tr(A Gamma)=sum_j w_j z_j^* A z_j.                  (2.3)
```

Let the minimal real aggregate cross observable be

```text
B_G=[[0,G],[G^*,0]],
z^* B_G z=2*Re(ell^* G r).                          (2.4)
```

Then aggregate cancellation across all witnesses is exactly

```text
Tr(B_G Gamma)=0.                                    (2.5)
```

It is one real equation.  It does not require any constituent in (2.2) to
be individually prime-null.

Let `X` collect every positive evaluation row that is to be nulled and put

```text
P=X^*X>=0.                                          (2.6)
```

There is no ensemble relaxation of these positive nulls:

```text
Tr(P Gamma)=sum_j w_j norm(X z_j)^2=0
 iff range(Gamma) subset ker X
 iff X z_j=0 for every j with w_j>0.                (2.7)
```

Equivalently, `P Gamma=Gamma P=0`.  In particular, averaging cannot cancel
positive-zero energy by phase.

Finally, if `Q=Q^*` is the complete finite Weil operator, then

```text
Tr(Q Gamma)<0                                       (2.8)
```

implies `z_j^*Qz_j<0` for some `j`.  This is why positive-ensemble
bookkeeping is a valid route to one negative direction, even though that
particular constituent need not satisfy (2.5) separately.

By contrast, signed coefficients do not have this implication.  For
example, `Q(z_1)=Q(z_2)=1` but

```text
2*Q(z_1)-3*Q(z_2)=-1.                               (2.9)
```

Consequently a signed finite difference in the support length is not a
Weil counterexample.  It must first be realized as one actual test function,
with all coherent cross terms retained.

## 3. Exact multi-seed geometry

In the lobe decomposition, write the covariance as

```text
Gamma=[[L,C],[C^*,R]],

L=sum_j w_j ell_j ell_j^*,
R=sum_j w_j r_j r_j^*,
C=sum_j w_j ell_j r_j^*.                            (3.1)
```

The complete finite-dimensional positivity criterion is

```text
C=L^(1/2) W R^(1/2),       norm(W)_op<=1,            (3.2)
```

on the supports of `L` and `R` (with the usual Moore--Penrose formulation
when either is singular).  Thus every possible collection of seed phases
and free-lobe phases is already encoded by one contraction `W`.

Both the actual-prime cross and a selected cross target are linear
functionals of this same matrix:

```text
Tr(B_G Gamma)=2*Re Tr(G^* C),
Tr(B_Y Gamma)=2*Re Tr(Y^* C).                       (3.3)
```

For a positive row `x=x_- direct_sum x_+`, condition (2.7) gives the two
exact matrix equations

```text
L*x_-+C*x_+=0,
C^*x_-+R*x_+=0.                                    (3.4)
```

These are the covariance version of the affine single-seed matching
equation.  Multiple seed phases do not create an unrecorded degree of
freedom: they change `C`, subject to (3.2)--(3.4).

If several fixed seed moments or normalizations are prescribed, they are
additional linear constraints on `R` and `C`.  They can make the feasible
set smaller and can raise the rank of an extremizer, but they do not alter
the aligned sign theorem in Section 5.

## 4. The exact SDP and dual

Let

```text
H_0=ker P,
B_0=P_(H_0) B_G P_(H_0),
N_0=P_(H_0) N P_(H_0),                              (4.1)
```

where `N>=0` measures the selected negative carrier.  Normalize by
`Tr(Gamma)=1`; another norm budget is obtained by scaling.  The exact
carrier-survival problem for positive ensembles is

```text
C_* = max Tr(N_0 Gamma)
      subject to Gamma>=0,
                 Tr(Gamma)=1,
                 Tr(B_0 Gamma)=0.                  (4.2)
```

Its dual is

```text
C_* = min lambda
      subject to lambda*I_0+nu*B_0-N_0>=0,
                 lambda,nu real.                   (4.3)
```

The dual is strictly feasible for large `lambda`, so finite-dimensional
strong duality holds whenever the primal is feasible.

The one-real-row feasibility condition itself is simply

```text
lambda_min(B_0)<=0<=lambda_max(B_0).                (4.4)
```

If `B_0<=0`, every feasible covariance is supported in `ker B_0`; a carrier
survives precisely when `N_0` is nonzero on that kernel.

For the complete proof objective, put

```text
q_* = min Tr(Q_0 Gamma)
      subject to the constraints in (4.2).          (4.5)
```

Then a positive aggregate proof of a negative direction exists exactly
when `q_*<0`.  The dual form is

```text
q_* = max lambda
      subject to Q_0-lambda*I_0-nu*B_0>=0.          (4.6)
```

Equations (4.2)--(4.6), with the actual finite Gabor matrices inserted, are
the exact finite computation.  No prime-by-prime equations occur.

There is also a useful rank fact.  On one common witness space, every
extreme point of (4.2) has rank one.  Indeed, if an extreme `Gamma` had rank
`r>=2`, Hermitian perturbations on its range would have real dimension
`r^2>=4` in the complex case (and `r(r+1)/2>=3` in the real case).  The two
real equations

```text
Tr(Delta)=Tr(B_0 Delta)=0                           (4.7)
```

would leave a nonzero perturbation `Delta`, and sufficiently small
`Gamma+-epsilon*Delta` would remain positive semidefinite.  This contradicts
extremality.

Therefore every linear objective in (4.2) has a rank-one optimizer.  With
only the minimal real aggregate equation, multi-witness convexification
cannot beat a single coherent witness **when all candidates inhabit the
same admissible space with the same operators**.  A labelled direct sum of
genuinely different support normalizations is discussed in Section 7.

## 5. Aligned-row no-go theorem

The following operator inequality is the exact extension of the one-pair
alignment obstruction.

### Theorem 5.1 (positive ensembles cannot cancel an aligned row)

Suppose on the positive-null space `H_0` that

```text
B_align<=-c*N_0,             c>0.                  (5.1)
```

Then every `Gamma>=0` supported in `H_0` satisfies

```text
Tr(B_align Gamma)<=-c*Tr(N_0 Gamma).                (5.2)
```

Consequently

```text
Tr(B_align Gamma)=0  implies  Tr(N_0 Gamma)=0.      (5.3)
```

This conclusion includes arbitrarily many witnesses, seeds, phases, and
positive weights.  It uses only positivity of `Gamma`.

### Robust form

Let the actual row be

```text
B_actual=B_align+R.                                 (5.4)
```

Aggregate cancellation gives the necessary inequality

```text
c*Tr(N_0 Gamma)
 <=Tr(R Gamma)
 <=norm((R_0)_+)_op*Tr(Gamma),                      (5.5)
```

where `R_0` is the compression of `R` to `H_0` and `(R_0)_+` its positive
part.  Hence a normalized ensemble retaining carrier `K` requires

```text
norm((R_0)_+)_op>=c*K.                              (5.6)
```

With a subpower norm budget, an `X^o(1)` remainder cannot cancel a
carrier of size `X^theta`, `theta>0`.  More generally, (5.5) measures the
exact carrier loss rather than merely counting the dimension of a putative
reservoir.

## 6. Exact direct sum of asymmetric mirror blocks

For each packet or scale `j`, use orthonormal lobe coordinates `u_j,v_j`
and the exact normalized mirror compression

```text
M_j=m_j*[[1,C_j],[C_j,1]],
m_j>0,                  C_j=cosh(alpha_j D_j)>1.    (6.1)
```

Put

```text
e_(j,+)=(u_j+v_j)/sqrt(2),
e_(j,-)=(u_j-v_j)/sqrt(2).                          (6.2)
```

The positive and negative spectral pieces and the completed lobe-cross
observable are

```text
P_j=m_j*(1+C_j)*e_(j,+)e_(j,+)^*,
N_j=m_j*(C_j-1)*e_(j,-)e_(j,-)^*,
B_j=m_j*C_j*(u_j v_j^*+v_j u_j^*).                 (6.3)
```

Let `P=direct_sum_j P_j`, `N=direct_sum_j N_j`, and
`B=direct_sum_j B_j`.  By (2.7), `Tr(P Gamma)=0` puts the covariance in the
direct sum of the negative modes and any neutral coordinates.  Therefore

```text
Tr(B Gamma)
 =-sum_j m_j*C_j*<e_(j,-),Gamma e_(j,-)>,           (6.4)

Tr(N Gamma)
 = sum_j m_j*(C_j-1)*<e_(j,-),Gamma e_(j,-)>.       (6.5)
```

Off-diagonal covariance between different `j` does not enter either trace.
Since every diagonal weight in (6.4) is nonnegative,

```text
Tr(B Gamma)<=-Tr(N Gamma).                          (6.6)
```

This is (5.1) with `c=1`.  Thus two, one hundred, or a continuum of
orthogonal mirror blocks cannot cancel their completed aggregate cross
rows while their negative carriers add.  Different seed phases do not
help: after the positive null, every block contributes a negative multiple
of an absolute square.

The same conclusion holds for the carrier-scale pure block

```text
2*k_j*(u_j v_j^*+v_j u_j^*).                       (6.7)
```

The `m_j I` same-lobe remainder in (6.1) changes the carrier by only the
displayed `C_j-1` versus `C_j`; it does not change the sign.

This theorem is intentionally limited to the orthogonal/aligned block
regime.  Overlapping packets, collateral zeros, or prime-side cross-scale
terms can create off-block entries.  Those entries belong to the remainder
`R` in (5.4) and must satisfy the quantitative requirement (5.5).

There is a stronger identity which does not assume the positive rows were
nulled.  From (6.1) and (6.3), on the full two-coordinate block,

```text
M_j=m_j*I_j+B_j.                                    (6.8)
```

Therefore every positive covariance, with arbitrary mass in both spectral
modes, satisfies

```text
Tr((direct_sum_j M_j)Gamma)
 =sum_j m_j*Tr(Gamma_(j,j))+Tr(B Gamma).             (6.9)
```

If the **completed** aggregate cross scalar is canceled, the last term is
zero and the first is nonnegative, strictly positive on every nonzero
mirror block.  Hence allowing positive-row leakage cannot make the selected
mirror contribution negative while using cross cancellation.  The
positive spectral energy pays more than the nominal negative carriers.
Only an off-block/actual-prime remainder can alter (6.9).

## 7. Multiple support lengths

There are three mathematically different operations that can be called a
multi-scale construction.

### 7.1 Positive sum of separate explicit formulas

If scale `L_j` has its own packet space and normalization, label the spaces
and form their direct sum.  The block-diagonal covariance gives exactly

```text
sum_j w_j Q_(L_j)(f_j),        w_j>=0.              (7.1)
```

This is a valid proof device because a negative value of (7.1) forces one
negative constituent.  For isolated normalized mirror blocks, (6.4) shows
that their completed cross rows all have the same sign.  Support length
does not supply cancellation.

The rank-one statement in Section 4 now produces a rank-one vector in the
**labelled direct sum**.  If the `Q_(L_j)` genuinely use different
normalizations, that formal vector need not be one physical test function;
it is another representation of the positive sum (7.1).  The direct-sum
sign theorem, not the rank statement, is what rules out the aligned escape.

### 7.2 Signed scale differences

A combination with some `w_j<0` can cancel prime polynomials, but it does
not imply a negative Weil direction, by (2.9).  No conclusion about RH
follows unless the signed combination is independently realized as one
admissible quadratic form.

### 7.3 One coherent multi-scale test function

If all packets are embedded in one largest support and

```text
f=sum_j a_j f_j,                                    (7.2)
```

then `Q(f)` contains every inter-scale cross term.  This is a rank-one
covariance in the common physical space, not (7.1).  Such a construction is
legitimate and is already covered by the one-real-row SDP.  It can escape
the block no-go only if the newly retained off-block operator supplies the
positive remainder required by (5.5).  Dropping those coherent terms while
using their phases for cancellation is inconsistent.

The completed explicit formula makes the same point without matrices.  At
every scale,

```text
B_pole+B_arch-B_prime=B_selected+B_collateral.      (7.3)
```

After a positive weighted sum, raw-prime cancellation gives

```text
sum_j w_j B_selected,j
 =sum_j w_j*(B_pole,j+B_arch,j-B_collateral,j).     (7.4)
```

If the selected left side has one sign and magnitude `K`, the combined
pole/archimedean/collateral right side must also have magnitude at least
`K`.  Thus different prime phases at different heights or support lengths
cannot by themselves provide a free cancellation: exact completion charges
the cancellation to a carrier-sized omitted term.

## 8. Real quadrature does not change the sign theorem

For real-symmetric operators and a complex packet `z=x+i*y`,

```text
z^*A z=x^T A x+y^T A y.                             (8.1)
```

Thus complex polarization is exactly a positive two-real-witness ensemble.
It is legitimate to have

```text
x^T B x+y^T B y=0                                  (8.2)
```

without either real packet being separately prime-null, provided the total
full form is estimated before descent.  If the total full form is negative,
one of `x,y` is negative.

In the aligned mirror face, however,

```text
x^T B x<=-c*x^T N x,
y^T B y<=-c*y^T N y.                               (8.3)
```

Equation (8.2) then forces both carrier terms to vanish.  Rotating seed
phases by `i`, or pairing cosine and sine quadratures, cannot reverse an
absolute-square sign.

Imposing a complex aggregate row rather than its necessary real part adds
a second real trace equation.  It can only shrink the feasible covariance
set.  The no-go already holds for the weaker one-real equation.

## 9. The exact surviving two-witness mechanism

The preceding no-go is sharp.  Suppose on `H_0` there are two normalized
positive covariances, a carrier state `Gamma_-` and a reservoir state
`Gamma_+`, such that

```text
b_-=Tr(B_actual Gamma_-)<0,
b_+=Tr(B_actual Gamma_+)>0,
n_-=Tr(N Gamma_-)>0.                                (9.1)
```

Then the positive mixture

```text
Gamma
 =[b_+*Gamma_-+abs(b_-)*Gamma_+]
   /(b_++abs(b_-))                                  (9.2)
```

satisfies `Tr(B_actual Gamma)=0` and retains

```text
Tr(N Gamma)
 =[b_+*n_-+abs(b_-)*n_+]
   /(b_++abs(b_-))
 >=b_+*n_-/(b_++abs(b_-)).                          (9.3)
```

Hence a target-neutral reservoir (`n_+=0`) loses only a fixed carrier
factor precisely when `b_+` is comparable to or larger than `abs(b_-)`.
This is an explicit abstract two-witness escape, not merely a necessary
condition.

It closes a negative-direction proof only if the complete forms also obey

```text
b_+*[-Tr(Q Gamma_-)]
 >abs(b_-)*Tr(Q Gamma_+).                           (9.4)
```

Equation (9.4) is the exact collateral-cost condition for the mixture in
(9.2) to have negative full form.  A reservoir with the correct prime sign
but carrier-sized positive zero energy is useless.

Conversely, decompose

```text
B_actual=B_align+R,
B_align<=-c*N.                                      (9.5)
```

Every aggregate-null positive covariance must satisfy (5.5).  Therefore a
carrier-surviving ensemble exists only if the compressed transverse
remainder has a positive direction of carrier scale which overwhelms the
aligned row and has acceptable full `Q` cost.  Equations (9.1)--(9.4) show
that this strengthened condition is also sufficient once such an
opposite-sign actual-row direction is produced.

This is the exact operator alternative:

```text
aligned face:       no multi-witness escape;

opposite-sign face: two positive witnesses suffice, subject to (9.4).    (9.6)
```

## 10. Scope for the actual zeta problem

The direct-sum no-go applies exactly to the normalized isolated
Paley--Wiener mirror blocks and to any completed compression satisfying
(5.1).  It also shows that the abstract one-pair counterblock cannot be
repaired merely by duplicating it, changing seed phases, or changing its
support scale.

It does **not** prove that the actual raw von Mangoldt cross operator is
sign-definite on the complete positive-null space.  Actual on-line zeros,
other off-line pairs, pole and archimedean rows, nonorthogonal packet
overlaps, and coherent cross-scale terms contribute to `R`.  Existing zero
counts, trace/Frobenius moments, KMT bounds, and ordinary prime mean squares
do not determine the positive spectral edge of this compressed remainder,
nor the full-form cost in (9.4).

The strongest correct next theorem is therefore the following.

### Actual-prime transverse-reservoir theorem card

For every hypothetical deepest off-line pair and an admissible asymmetric
packet geometry, prove one of:

1. **no-go:** on the positive-null face,
   `B_actual<=-c*N+R_small`, with
   `norm((R_small)_+)=o(K)` under the allowed subpower norm budget; or
2. **construction:** produce `Gamma_-,Gamma_+` satisfying
   (9.1)--(9.4), uniformly in ordinate, collision geometry, endpoint jets,
   and support scale.

The first alternative rules out this entire multi-witness escape family.
The second turns it into a genuine surviving mechanism and reduces the
proof to the remaining same-lobe/full-form ledger.  No result currently in
the repository establishes either alternative for the actual zeta data, so
no strip claim follows from this audit.
