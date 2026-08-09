# Proportional-order detector bank and centered major-arc gate

Status: tilted-edge and zero-temperature theorems proved analytically for the
full von Mangoldt field; a retreated-cutoff transfer to the evaluated
rank-two center proved from the existing uniform Euler lemma; current
Type-II/dispersion literature audited through 2026-08-07.  The bank removes
the nonattained-edge obstruction, but the arithmetic fixed-power gap still
vanishes at zero slope.  This report does **not** prove a new zero-free strip
or the Riemann Hypothesis.

## 1. Verdict

Three questions left by R78--R79 can now be separated cleanly.

1. **Can a moving record zero evade every growing detector?**  No, after
   replacing one sublinear-order schedule by a dyadic bank of
   proportional-order schedules.  At slope `lambda>0`, the vertical zero
   spectrum is compact and its largest tilted modulus is attained.  Sending
   `lambda` to zero recovers the exact horizontal width

```text
Delta=sup_rho abs(Re(rho)-1/2).                          (1.1)
```

   This supplies the previously missing moving-edge converse.
2. **Do current zero-free estimates give a fixed power for these tests?**
   Yes at each fixed positive slope.  Vinogradov--Korobov gives

```text
A_h(lambda)
 <=1/2-c_h lambda^(2/5)[log(1/lambda)]^(-1/5)+O_h(lambda),
                                                               (1.2)
```

   where `A_h(lambda)` is the amplitude exponent in the tilted metric.  But
   the saving tends to zero as `lambda->0`.  Optimizing (1.2) for a zero of
   height `gamma` reproduces exactly the Vinogradov--Korobov strip; it does
   not give a fixed horizontal strip.
3. **Can the newest Type-II or dispersion theorems supply the missing
   uniform gap?**  Not as a black-box import.  The R71 tail coefficient has
   the elementary size hypotheses of an MRSTT Type-II sum, and Wright's 2026
   fixed-denominator Kloosterman theorem has a nominal `x^(-1/40+o(1))` gain
   for its own balanced trilinear form.  MRSTT does not directly control the
   completed tail--head--center square.  R81 derives Wright's exact phase on
   the off-axis mode lattice, but its punctured axes and conditional
   all-cofactor tail are not covered.  Exact Mellin completion is

```text
-zeta'(s)/zeta(s)-1/(s-1),                              (1.3)
```

   whose remaining poles are precisely the nontrivial zeta zeros.  The
   additive-mode audit now gives an exact cofactorwise nonzero-mode expansion.
   It also shows that every individual zero residue persists through a
   universal shell-normalized band for the actual proportional B-splines and
   has a nonzero Gamma limit at each fixed nonzero scaled frequency.
   Total-zero-sum noncancellation and a completed reciprocal-phase
   reorganization remain open.

The new useful target is therefore not another recurrence theorem and not a
generic Type-`I_2` estimate.  The exact additive mode reduction is now done;
the targets are a completion-preserving **reciprocal-phase reorganization**
and then a centered joint rational--Archimedean major-arc estimate with a
power uniform as `lambda->0`.  Such a power theorem would give a fixed
zero-free strip.  No surveyed source proves those remaining steps.  The
correction is developed
in
[`COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md`](COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md).

## 2. Exact proportional-order factorization

Fix `h>0`.  With the notation of
[`FULL-FIELD-VK-SUBPOWER-BOUND.md`](FULL-FIELD-VK-SUBPOWER-BOUND.md), let

```text
Phi_(h,k)(t)
 =h^(-k)vol{u in [0,h]^k:u_1+...+u_k<t},

W_(h,k)(t)=Phi_(h,k)(t+hk)-Phi_(h,k)(t),
N_(h,k)=norm(W_(h,k))_2,
V_(h,k)=W_(h,k)/N_(h,k).                                (2.1)
```

The full pole-subtracted field is

```text
D_(h,k)^full(r)
 =sum_n Lambda(n)n^(-1/2)V_(h,k)(r-log n)
  -exp(r/2)Vhat_(h,k)(1/2).                             (2.2)
```

Put

```text
alpha_h(s)=(exp(hs)-1)/(hs)=integral_0^1 exp(hst)dt,
beta_h(s) =(1-exp(-hs))/(hs)=exp(-hs)alpha_h(s).         (2.3)
```

The exact unnormalized window multiplier has the elementary factorization

```text
N_(h,k)Vhat_(h,k)(s)
 =[alpha_h(s)^k-beta_h(s)^k]/s.                         (2.4)
```

Indeed, if

```text
q_h(s)=sinh(hs/2)/(hs/2),
```

then `alpha_h=exp(hs/2)q_h`, `beta_h=exp(-hs/2)q_h`, and
(2.4) is exactly the multiplier in R79.

Fix a slope

```text
0<lambda<1/h,
R_n=n/lambda,
z_lambda(s)=exp(s/lambda)alpha_h(s),
w_lambda(s)=exp(s/lambda)beta_h(s).                     (2.5)
```

For `s_rho=rho-1/2`, the distributional explicit formula gives, on every
fixed compact `u` interval,

```text
F_(lambda,n)(u)
 :=N_(h,n)D_(h,n)^full(R_n+u)

 =-sum_rho m_rho exp(s_rho u)/s_rho
       [z_lambda(s_rho)^n-w_lambda(s_rho)^n]
  +the corresponding trivial-zero sum.                 (2.6)
```

Equation (2.6) is the key change of coordinates: proportional smoothing
turns every zero contribution into a difference of two pure powers.

## 3. Tilted-edge theorem

### Theorem 3.1 (attained tilted spectral radius)

Let `q` be a bounded, nonnegative, nonzero weight supported on a fixed
compact interval and positive almost everywhere on a nondegenerate interval.
Include the bases in (2.5)
for every nontrivial zero with multiplicity and the analogous bases for the
trivial zeros.  Define

```text
r_h(lambda)
 =max_{s, epsilon in {z,w}} abs(epsilon_lambda(s)),
A_h(lambda)=lambda log r_h(lambda).                     (3.1)
```

Then the maximum is attained by a finite nonempty set and

```text
limsup_(n->infinity)
 [N_(h,n)^2 integral q(u)
      abs(D_(h,n)^full(R_n+u))^2du]^(1/(2n))
 =r_h(lambda).                                          (3.2)
```

Moreover, for some `c_lambda>0`, the set of integers on which

```text
N_(h,n)^2 integral q(u)abs(D_(h,n)^full(R_n+u))^2du
 >=c_lambda r_h(lambda)^(2n)                            (3.3)
```

has positive lower Banach density.

#### Evidence class and trust base

This is an analytic theorem.  Its inputs are the exact explicit formula
(2.6), Riemann--von Mangoldt local counting, elementary uniqueness of finite
exponential sums, and the uniform-mean theorem for finite trigonometric
polynomials.  It is not formalized in Lean.  The algebraic factorization is
exercised by
[`proportional_order_detector_bank.py`](../src/proportional_order_detector_bank.py).

#### Exact scope

The theorem applies to the cutoff-independent full field.  Corollary 7.2
below transfers it to a different frozen-cutoff schedule with the evaluated
rank-two center.  It does not apply to the old near-square cutoff schedule at
`k` proportional to `R`.

#### Proof

For nontrivial zeros in the critical strip,

```text
abs(alpha_h(s))+abs(beta_h(s))
 <<_h(1+abs(Im(s)))^(-1).                               (3.4)
```

Thus both base families tend to zero as the ordinate tends to infinity.
For a trivial zero `s=-2m-1/2`, the `z` base tends to zero, and the `w` base
does too exactly because `1/lambda-h>0`.  Hence the set of nonzero bases has
only zero as an accumulation point.  Its largest modulus is attained by a
finite set.

Possible collisions between bases do not damage the block norm.  Group an
equal base `b` in (2.6).  Its coefficient is the `L2(q du)` vector

```text
C_b(u)=
 -sum_(z_lambda(s)=b)m_s exp(su)/s
 +sum_(w_lambda(s)=b)m_s exp(su)/s.                     (3.5)
```

Distinct exponentials are linearly independent on an interval.  Also
`z_lambda(s)=w_lambda(s)!=0` is impossible, since it would force
`exp(-hs)=1` and then `alpha_h(s)=beta_h(s)=0`.  Therefore every grouped
nonzero base has a nonzero coefficient vector.

After two powers have been absorbed into the coefficients, the remaining
series is absolutely summable by (3.4) and Riemann--von Mangoldt counting.
The standard spectral-radius argument for a compact Hilbert-valued
exponential series gives the upper half of (3.2).  On the top circle
`abs(b)=r_h(lambda)`, the normalized contribution is a nonzero finite
Hilbert-valued trigonometric polynomial.  Its Cesaro mean square is the sum
of the squared norms of its grouped coefficient vectors and is positive.
It therefore stays above one fixed positive norm threshold on a set of
positive lower Banach density.  Lower-modulus bases are exponentially
negligible, which proves both the lower half of (3.2) and the exact-top-radius
statement (3.3).

#### Sharpness and nonclaims

Vertical compactification persists at the endpoint `lambda h=1`; there the
trivial `w` bases decay only polynomially.  The strict restriction
`lambda h<1` is the support condition `R_n>hn` used by the detector.  For
`lambda h>1`, the negative-trivial-zero `w` bases grow.  A scalar
sample at `u=0` can have accidental base collisions; the block norm is what
removes them without a genericity assumption.  The theorem proves a
converse for this detector family, not an arithmetic upper bound.

## 4. The zero-temperature identity

### Theorem 4.1 (horizontal width as a zero-slope limit)

Choose `h` outside the countable resonance set for one fixed critical-line
zero.  Then

```text
lim_(lambda->0+) A_h(lambda)=Delta.                     (4.1)
```

#### Proof

For `abs(Re(s))<=1/2`, (2.3) gives

```text
abs(alpha_h(s)),abs(beta_h(s))<=exp(h/2).               (4.2)
```

Consequently every nontrivial base satisfies

```text
lambda log abs(epsilon_lambda(s))
 <=Re(s)+h lambda/2<=Delta+h lambda/2.                  (4.3)
```

The trivial bases remain strictly to the left.  This proves the upper
limit.  By functional-equation symmetry, `Delta` is also the supremum of
the right-hand displacements.  Choose such a zero with displacement
`delta>Delta-epsilon`.  Its `alpha_h` factor is nonzero whenever `delta>0`,
and by the harmless choice of `h` also in the `Delta=0` endpoint.  Hence

```text
A_h(lambda)
 >=delta+lambda log abs(alpha_h(delta+i gamma))
 ->delta.                                                (4.4)
```

Letting `epsilon->0` proves (4.1).

This identity is a zero-temperature or tropical limit: the height penalty
`lambda log abs(alpha_h)` makes the spectrum compact at positive
temperature, while the exact horizontal edge returns as the penalty is
removed.

### Corollary 4.2 (an RH-complete dyadic bank)

Fix `0<c<1/h`, let `lambda_j=c 2^(-j)` for `j>=0`, and at a scale `R` retain the
distinct positive orders

```text
k_j(R)=floor(lambda_j R).                               (4.5)
```

There are only `O(log R)` of them, and duplicates are counted once.  Define

```text
B_c(R)=sum_j N_(h,k_j)^2
 integral q(u)abs(D_(h,k_j)^full(R+u))^2du.             (4.6)
```

If RH holds, then

```text
B_c(R)=O_(h,c,q)(1).                                    (4.7)
```

If a zero has displacement `delta>d>0`, then on a set of logarithmic scales
of positive lower Banach density,

```text
B_c(R)>=exp(2dR).                                       (4.8)
```

Indeed, under RH,

```text
abs(alpha_h(i gamma))=abs(beta_h(i gamma))
 =abs(sin(h gamma/2)/(h gamma/2)).                      (4.9)
```

The supremum of (4.9) over zeta ordinates is attained and strictly below
one, so the sum over the distinct orders is geometric.  The negative
trivial-zero contribution is uniformly geometric because `ch<1`.  If
`delta>d`, choose
a fixed `j` so small in slope that

```text
delta+lambda_j log abs(alpha_h(delta+i gamma))>d.       (4.10)
```

Choose `d<d_1<A_h(lambda_j)`.  The exact-top-radius recurrence (3.3) applied
along `R=n/lambda_j` first gives a fixed normalized margin on a positive-
lower-Banach-density set of lattice points.  The finite top spectral
polynomial and the differentiated absolutely summable tail have a uniform
local Lipschitz bound after division by their top exponential rate; explicitly,
after two powers are absorbed,
`sum_b norm(C_b')abs(b)^2<infinity`.  Hence
the lower bound with exponent `d_1`, and therefore (4.8) with exponent `d`,
persists on a fixed one-sided interval
`[n/lambda_j,n/lambda_j+eta]`, with `eta<1/lambda_j` so that the order remains
`k_j(R)=n`.  Since `eta` is independent of `n`, these
thickened lattice points have positive lower Banach density in the real
`R`-axis.

Thus the bank repairs the exact quantifier failure in R78: neither edge
attainment nor uniform almost-periodicity of a triangular array is needed.
It does not provide (4.7) from primes without RH.

## 5. What Vinogradov--Korobov gives at positive slope

### Theorem 5.1 (fixed-power tilted VK bound)

There are `lambda_0,c_h,C_h>0` such that for every fixed
`0<lambda<lambda_0`, with `R_n=n/lambda`,

```text
integral q(u)abs(D_(h,n)^full(R_n+u))^2du

 <=exp{[1-2c_h lambda^(2/5)
              (log(1/lambda))^(-1/5)+C_h lambda]R_n}
                                                               (5.1)
```

for all sufficiently large `n`.

#### Proof

The zero-shell proof in R79 is valid whenever `R>hk`; its exact-side loss is
`exp(B_h k)`, not `exp(C_h k^2)`.  Set `k=lambda R`.  The shell objective per
unit `R` becomes

```text
a y^(-2/3)(log y)^(-1/3)+lambda y,
y=log abs(gamma).                                      (5.2)
```

Its optimizer and value are

```text
y asymp lambda^(-3/5)[log(1/lambda)]^(-1/5),

S/R asymp
 lambda^(2/5)[log(1/lambda)]^(-1/5).                    (5.3)
```

Reduce `lambda_0` so that the displayed `C_h lambda` loss is smaller than
the main saving.  The finite
low-zero term has a fixed horizontal gap and the trivial-zero term decays
because `lambda h<1`.  Squaring the resulting pointwise bound and integrating
over the fixed `u` interval proves (5.1).

This is a genuine fixed power for every one tilted test.  It is not a fixed
horizontal strip.  If `s=delta+i gamma` with `delta` bounded away from zero,
then

```text
abs(alpha_h(s))>>_(h,delta_0) (1+abs(gamma))^(-1),
       delta>=delta_0>0.                                (5.4)
```

The factor `N_(h,n)^2 asymp_h n` is exponent-negligible.  Combining Theorem
3.1 with (5.1) and taking

```text
lambda asymp
 [log abs(gamma)]^(-5/3)
 [log log abs(gamma)]^(-1/3)                            (5.5)
```

returns

```text
delta<=1/2-c[log abs(gamma)]^(-2/3)
                  [log log abs(gamma)]^(-1/3).          (5.6)
```

Thus the bank plus current literature closes exactly back to the imported
Vinogradov--Korobov region.  The limit in (4.1) needs a saving bounded away
from zero as `lambda->0`; (5.1) supplies a saving tending to zero.

## 6. MRSTT interface audit: Type-II coefficient passes, completed lift open

Let `X=exp(r)` denote the detector scale and decompose its active product
range into dyadic shells `Q=[Y,2Y]`.  On the old sublinear-order R71 schedule,

```text
Y=X^(1+o(1)),
U,V=Y^(1/2+o(1)).                                      (6.1)
```

At fixed proportional slope the wider window instead gives
`Y=X^(1+O_h(lambda))` and
`U,V=Y^(1/2+O_(h,A)(lambda))`.  These errors tend to zero only in the
zero-slope limit.

Write

```text
alpha(d)=mu(d)1_(U<d<=Y exp(O(hk))/V),

beta_V(q)=sum_(b|q,b>V)Lambda(b).                       (6.2)
```

Then the tail coefficient on that shell is exactly

```text
a_(U,V)=alpha*beta_V.                                   (6.3)
```

Since

```text
0<=beta_V(q)<=sum_(b|q)Lambda(b)=log q,                 (6.4)
```

one has

```text
sum_(q<=B)beta_V(q)^2<=B log^2 B,
sum_(q<=B)beta_V(q)^4<=B log^4 B.                       (6.5)
```

Thus (6.3) has the elementary `L2` and `L4` coefficient hypotheses of the
Type-II inverse theorem in
Matomaki--Radziwill--Shao--Tao--Teravainen, with factor-range endpoints
`A_II^+,A_II^-=Y^(1/2+o(1))` on the old schedule and an `O(lambda)` exponent
collar at fixed slope.  An application additionally needs a large
correlation on a sufficiently large set of interval starts; (6.3)--(6.5) do
not supply that input.

The tempting Type-`I_2` representation

```text
mu_(>U)*Lambda_(>V)*1                                  (6.6)
```

does **not** pass their hypotheses.  The offending rough factor
`Lambda_(>V)` has truncated total variation `>>V` already on `(V,2V]`.  The
Type-`I_2` parameter is therefore forced down
to `delta<=Y^(-1/2+o(1))`; the polynomial inverse-theorem losses make the
result vacuous for a small fixed-strip threshold.

The formal Type-II contagion scales themselves are not the problem.  With
additive interval length `Y^theta`, `theta>1/2`, density `sigma=Y^(-nu)`, and
balanced factor scale `A=Y^(1/2+o(1))`, Proposition 6.6 of the 2026 paper is
compatible with any sufficiently small fixed `nu>0` satisfying

```text
K nu<min(1/2,theta-1/2).                                (6.7)
```

This scale calculation does not manufacture the required power-density set
of R71 starts.  The inverse conclusion is a second obstruction.  In the
abelian case it produces a frequency `T` and a small progression modulus on
which the residual phase after multiplication by `n^(-iT)` has bounded
variation for many starts.  A local model `n^(-it)` lies in this permitted
major-arc class (with `T=-t` in the model case), so the bad Mellin phase is
not excluded.

To obtain a power, the proof's Dirichlet-polynomial input would require a
separate estimate of the form

```text
sup_t abs(sum_(d~Y^(1/2))mu(d)d^(-1-it))
 <<Y^(-c).                                               (6.8)
```

For Mobius and von Mangoldt, current inputs give logarithmic or
Vinogradov--Korobov subpower savings.  A power is available there only for
divisor-type coefficients.  More importantly, (6.8) has already separated
the Mobius factor from the Type-I head and discarded the completion whose
cross terms R71 must retain.

The minimal useful replacement is a vector theorem.  Let

```text
h_(U,V)
 =mu_(<=U)*log+Lambda_(<=V)
  -mu_(<=U)*Lambda_(<=V)*1,

a_(U,V)+h_(U,V)=Lambda.                                 (6.9)
```

Partition `[Y,2Y]` into short additive intervals `J` of length `H_add` with
a bounded-overlap smooth partition of unity `chi_J`.  For the localizer at
scale `r`, use the dimensionless weight

```text
w_(J,r,Y)(u)=sqrt(Y)u^(-1/2)chi_J(u)V_(h,k)(r-log u).   (6.10)
```

For this weight, or its Mellin twist by a frequency `T`, define

```text
S_J(T)=(
 sum_n a_(U,V)(n)w_(J,r,Y)(n)n^(-iT),
 sum_n h_(U,V)(n)w_(J,r,Y)(n)n^(-iT),
 -integral w_(J,r,Y)(u)u^(-iT)du),

ell(z_1,z_2,z_3)=z_1+z_2+z_3.                          (6.11)
```

The open power theorem is

```text
sup_(abs(T)<=Y^o(1)) sum_J abs(ell(S_J(T)))^2
 <<Y H_add Y^(-2eta+o(1)),       eta>0.                 (6.12)
```

No coordinate may be squared separately.  Since the completed shell field is

```text
D_Y(r)=Y^(-1/2)sum_J ell(S_J(0)),                       (6.13)
```

Cauchy over the `O(Y/H_add)` intervals turns (6.12) into
`abs(D_Y(r))^2<<Y^(1-2eta+o(1))`.  Uniformity is required in `r`, shell,
block, slope/order, cutoffs, partition, and the displayed weight family.
Integrating and summing the `exp(o(R))` blocks and shells then gives the
complete fixed-power energy.  At fixed slope an `O(lambda)` exponent loss
remains because `Y=X^(1+O(lambda))`; a power uniform as `lambda->0` gives the
stated strip in the limit.  Existing MRSTT almost-all results do not
directly give even its logarithmic-saving version: they are scalar residual
estimates and do not contain the joint tail--head--pole square, the
deterministic block-bank quantifier, or the displayed uniform `T` supremum.

Primary sources:

- [Higher uniformity I, all intervals](https://doi.org/10.1017/fmp.2023.28),
  especially its Type-`I_2` inverse theorem and hyperbola decomposition;
- [Higher uniformity II, almost all intervals](https://doi.org/10.1007/s00222-026-01408-6),
  especially its nilsequence contagion and Type-II inverse theorems.

## 7. A proportional-order transfer to the explicit R71 center

The old frozen-center transfer chose cutoffs
`U=V=x^(1/2-c/k)` and required `hk^2=o(R)`.  That particular schedule fails
when `k` is proportional to `R`.  The uniform Euler lemma permits a different
schedule.

### Theorem 7.1 (retreated-cutoff Euler transfer)

Let `C_h` be large enough for the uniform Euler error

```text
abs(E_(U,V)(x))
 <<exp[C_h(k^2+k log(k+2))]
   [U^(k+1)log(2x)+(UV)^(k+1)]x^(-k-1/2).               (7.1)
```

Choose constants

```text
1/2<a_0<1,
A>max(C_h,h),
0<c<min(1/h,1/A),                                      (7.2)
```

with a fixed margin in the last inequality.  For `1<=k<=cR`, put

```text
theta_(R,k)=a_0/k+A k/R,

U_(R,k)=V_(R,k)
 =floor(exp[(1-theta_(R,k))R/2]).                       (7.3)
```

For all sufficiently large `R`, freeze these cutoffs on any fixed-width
two-sided block `r in [R-H_0,R+H_0]`.  The support condition holds and the
normalized difference between the full field and the balanced tail plus its
evaluated rank-two center is

```text
norm(D_(h,k)^frozen-D_(h,k)^full)_(L2([R-H_0,R+H_0]))
 <=exp(-kappa R)                                       (7.4)
```

for some `kappa>0`, uniformly in `1<=k<=cR` after reducing `c` if needed.
When `k=lambda R+O(1)`, the stronger quadratic term in the exponent is
negative.

#### Proof

The function `a_0/k+Ak/R` is convex in `k`, so its maximum on
`[1,cR]` occurs at an endpoint.  The fixed gaps `a_0<1` and `Ac<1` show that
`theta_(R,k)<=1-delta` uniformly for some `delta>0`.  Moreover,

```text
theta_(R,k)R=a_0 R/k+A k>=hk,                           (7.5)
```

and the actual support margin
`a_0R/k+(A-h)k-O_h(1)` tends uniformly to infinity.  Hence the support
condition `UV<=exp(r-hk)` holds throughout the two-sided block.  The dominant
`UV` term in (7.1), at the central scale, has logarithm at most

```text
C_h k^2+O_h(k log(k+2))
 +[1/2-(k+1)theta_(R,k)]R

=-(a_0-1/2)R-a_0R/k
  -(A-C_h)k^2-Ak+O_h(k log(k+2)).                       (7.6)
```

This is at most `-kappa R`; for proportional orders it also contains the
negative term `-(A-C_h)lambda^2R^2`.  Moving to the left endpoint costs only
`O_h(kH_0)`.  The one-`U` term is smaller by a term of order `kR`.  Endpoint
differencing, division by

```text
N_(h,k)>=sqrt(hk)/2,                                    (7.7)
```

and integration over a fixed block cost only polynomial factors, proving
(7.4).

### Corollary 7.2 (tilted bank with evaluated center)

For slopes

```text
0<lambda<c<min(1/h,1/A),                               (7.8)
```

Theorems 3.1, 4.1, and 5.1 remain valid if the full field is replaced by the
frozen balanced R71 tail with its complete evaluated rank-two center and the
cutoffs (7.3).  At each fixed slope, the stronger form of (7.6) is

```text
norm(D^frozen-D^full)_2
 <=exp[-(A-C_h)lambda^2R^2
        +O_(lambda,h,a_0,A,H_0)(R log R)].               (7.9)
```

This superexponential defect, rather than (7.4) alone, shows that the
spectral radius and its recurrence are unchanged.

For fixed slope `lambda`, these cutoffs lie at

```text
U,V=x^((1-A lambda+o(1))/2),
central-shell cofactor length=x^(A lambda+o(1)),
full-window cofactor<=x^((A+h)lambda+o(1)).             (7.10)
```

Thus they retreat a fixed `O(lambda)` distance from square root.  They return
to the near-square geometry as the zero-temperature slope tends to zero.
This transfer is bookkeeping, not the missing cancellation estimate.

## 8. New dispersion input and its unproved R71 bridge

Thomas Wright's April 2026 preprint
[Trilinear Kloosterman fractions I](https://arxiv.org/abs/2604.25177),
Theorem 2.1, bounds

```text
B(M,N,A_W;R_0)
 =sum_(a~A_W,m~M,n~N;(m,nR_0)=1)
   alpha_m beta_n nu_a e(vartheta a inverse(m)/(nR_0)),
vartheta in Z-{0}.                                      (8.1)
```

In a compact form sufficient for the exponent audit, its right side is

```text
M^epsilon norm(alpha)norm(beta)norm(nu)(A_WMN)^(1/2)R_0^(1/4)
 *(1+abs(vartheta)A_W/(MN))^(1/4)

 *[N^(-1/8)+R_0^(1/8)N^(1/8)M^(-1/4)
   +M^(1/10)R_0^(-3/20)A_W^(-1/20)N^(-3/20)
   +N^(3/20)A_W^(-3/20)M^(-1/5)
   +N^(3/8)M^(-1/2)].                                  (8.2)
```

At the schematic balanced R71 scale

```text
M=N=x^(1/2+o(1)),
R_0=x^o(1),
abs(vartheta)A_W<=MN x^o(1),                            (8.3)
```

the worst displayed gain is `M^(-1/20+o(1))`, i.e.
`x^(-1/40+o(1))` for Wright's native form relative to its Cauchy baseline.

The original exact R71 formula has the continuous log-ratio kernel
`psihat(u-t)`, not a derived additive equality

```text
d_1b_1m_1-d_2b_2m_2=h_shift.                            (8.4)
```

R81 has since passed the first algebraic gate: using
`Lambda=(-mu log)*1`, it allocates the continuum cofactor by cofactor and
Poisson summation expresses the exact completed field using only direct
nonzero additive modes.  A finite Ramanujan alternative gives exact reduced
rationals with polylogarithmic coefficient norm and one explicit Mertens zero
mode.  The off-axis part of the double lattice produces Wright's inverse phase
after a second Poisson summation.  No theorem yet controls its coupled
amplitude, determinant/dual-zero sectors, punctured-axis corrections, or the
completed zero mode, so the complete square is not in (8.1).  Any usable
derivation must retain those cancellations and verify coprimality, phase
integrality, dyadic ranges, sequence norms, and total mode-summation loss.

There is a second exponent correction.  With the retreated cutoffs at fixed
slope, a central-shell cofactor has length `x^(A lambda+o(1))`, and the upper
edge of the full window can reach `x^((A+h)lambda+o(1))`; neither is `x^o(1)`
at fixed slope.  Under the most favorable hypothetical balanced map, direct
substitution gives the crude full-window budget

```text
eta_W^full(lambda)
 =1/40-[(11A+10h)/40]lambda+o(1),                      (8.5)
```

before phase and mode losses.  Thus the fixed denominator does not
automatically kill the gain at sufficiently small slope, but (8.5) is not an
R71 estimate.

Independently, exact Mellin completion gives

```text
[1/zeta(s)][-zeta'(s)/zeta(s)]zeta(s)
 =-zeta'(s)/zeta(s),                                    (8.6)
```

and the rank-two pole center changes this to (1.3), not to an analytic
function.  The additive-mode audit proves persistence of an individual zero
residue in a universal shell-normalized band for the actual proportional
family, and a nonzero whole-window Gamma limit at every fixed `xi!=0`.
Total-zero-sum noncancellation is still open, fixed rational `a/q` carry
genuine prime main terms, and the carrier has not been identified with only
one exact dual mode.  Wright can potentially bound the off-axis forms already
isolated by the new reduction, but it cannot yet be said to have cleared “the
nonzero modes.”

This boundary is shared by the broader literature audit:

| Input | Fixed power available where? | R71 failure mode |
|---|---|---|
| MRSTT contagion | a translated-partition logarithmic square for the completed scalar on genuine minor arcs | no fixed power or predetermined-bank bound; rational--Archimedean major arcs survive |
| reciprocal/Kloosterman phases | Wright's native nonzero integer phase | off-axis phase derived; amplitude separation, zero sectors, completed zero mode, and net summation remain |
| additive Mobius twists | genuine minor arcs | every fixed rational `a/q` has a singular-series major term; zero is not the only major arc |
| long twisted moments | much shorter polynomial or divisor coefficients | balanced length `x^(1/2)` with `t=x^o(1)` is outside range |
| three-variable Mobius sums | logarithmic saving unconditionally | published power versions assume a fixed zero-free half-plane |

The January 2026 preprint arXiv:2601.00292 must not be used as an improved
Kloosterman input: it was withdrawn after a missing `L^2` factor was found,
and the authors state that the argument no longer yields the claimed
improvement.

The exact correction and exponent ledger are in
[`COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md`](COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md).

## 9. The surviving centered rational-major-arc theorem

The literature-derived proof architecture is now precise.

1. Use the proportional-order bank to make every horizontal record carrier
   an attained tilted carrier.  This closes the recurrence/exceptional-set
   quantifier.
2. Use R81's exact cofactorwise Poisson decomposition of the joint
   prime--continuum field.  This gate is now proved.
3. Extend the derived off-axis Wright phase across its coupled amplitude,
   determinant/dual-zero and punctured-axis sectors, and the conditional or
   finite-basis zero mode, then sum all native forms with positive net power.
   This is currently red.
4. Prove (6.12), or its exact mode-form analogue, on the remaining centered
   rational--Archimedean major arcs, including every cross term and the total
   zero sum.  This is currently red and is the intrinsic fixed-strip-strength
   step.

The last step must retain

```text
balanced tail + complete Type-I head - pole integral                  (9.1)
```

inside one square.  A theorem for the tail, Mobius factor, prime factor,
head, or center separately is not enough.

For a fixed strip `Re(rho)<=1-eta`, it would suffice to establish a bank
bound whose amplitude gap stays below `1/2-eta` uniformly along some slopes
`lambda_j->0`.  For RH itself the limiting amplitude must be zero.  In the
arithmetic field under study, define its half-energy exponent by

```text
A_arith(lambda)
 =limsup_(n->infinity) [1/(2R_n)]
   log[N_(h,n)^2 integral q(u)abs(D_(h,n)(R_n+u))^2du]. (9.2)
```

Theorem 3.1 identifies this with `A_h(lambda)` for the exact full field.  The
thresholds are

```text
fixed strip: limsup_(lambda->0) A_arith(lambda)<=1/2-eta,
RH:          limsup_(lambda->0) A_arith(lambda)<=0.      (9.3)
```

Current VK gives the right side of (1.2), whose limit is `1/2`.  Arbitrary
fixed logarithmic savings also have limit `1/2`.  This is why neither can be
amplified into (9.3) by adding more detector scales.

## 10. Reality check and next experiment

What changed:

- nonattainment is no longer a live obstruction;
- proportional-order fixed powers are legitimate, and the evaluated center
  can be retained after an `O(lambda)` cutoff retreat;
- Type-`I_2` is the wrong MRSTT interface; Type II is the correct one;
- recent Kloosterman technology gives a real native-form candidate gain, and
  its fixed-denominator exponent survives at sufficiently small slope in the
  favorable schematic regime.

What did not change:

- the off-axis Wright phase is exact, but no completion-preserving bound for
  its coupled amplitude, zero sectors, and completed Mertens mode has been
  proved;
- the Poisson decomposition cancels the continuum zero mode cofactorwise, but
  fixed rational modes retain singular-series main terms and total-zero-sum
  noncancellation is unresolved;
- every imported unconditional bound on that component has horizontal
  exponent tending to `1/2`;
- no fixed strip, RH, or ZFC-independence statement follows.

The first completion-preserving additive-mode audit has now been executed in
the linked follow-up, including the direct nonzero-mode expansion, its exact
off-axis reciprocal phase, and a uniform individual-residue band.  The
highest-value next computation is narrower: control the coupled amplitude and
the determinant/dual-zero and punctured-axis sectors while retaining either
the conditional cofactor cancellation or the finite basis's Mertens zero mode.
A separate power bound for that mode already costs the full strip.  Only after
this passes should work be invested in the complete mode sum; the
rational-major-arc theorem remains the unavoidable new cancellation input.

## 11. Reproduction and nonclaims

Run the exact algebraic probe and focused tests with

```text
PYTHONPATH=src python3 src/proportional_order_detector_bank.py
PYTHONPATH=src python3 -m pytest -q \
  src/test_proportional_order_detector_bank.py
```

The probe checks (2.3)--(2.5), vertical compactification on finite nodes, the
dyadic order bank, and the VK exponent scaling.  It does not numerically
evaluate zeta zeros beyond supplied synthetic nodes, certify (5.1), or test
Wright's theorem.

Theorems 3.1, 4.1, 5.1, and 7.1 are conventional analytic arguments, not
Lean theorems.  Their novelty has not been externally assessed.  This report
does not claim a fixed zero-free strip, RH, an every-block proof of (6.12),
or control of the centered principal additive band.
