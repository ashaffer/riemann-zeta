# Two-lobe prime nulling and the local interpolation gate

Status: exact dimension and exponent ledger, a conditional strip theorem,
and an explicit local-conditioning obstruction, 2026-08-11.  No zero-free
strip is proved here.

## 1. Verdict

There is a promising way to combine the Anthropic simple-zero density with
exact prime-translate nulling.  Its raw count and power exponents work.
Write

```text
C_0=3/2-(1/sqrt(2))*cot(1/sqrt(2))
   =0.672500703679...,

r_0=(1-C_0)/2=0.163749648160... .                    (1.1)
```

The simple-line theorem implies that the number of off-line hyperbolic
**positive rows** in a dyadic carrier is at most

```text
p_T<=(r_0+o(1))*N(T,2T).                              (1.2)
```

An endpoint lobe of relative physical length `a` has Shannon dimension
`(a+o(1))*N(T,2T)`.  Endpoint jets, a standard collar, both pole rows, and
all cross-prime-power translates together cost only `o(N(T,2T))`
additional conditions.  Thus the algebraic budget has fixed positive slack
whenever

```text
a>r_0.                                               (1.3)
```

For two endpoint lobes of length `aL`, the same-lobe prime term is at most
`X^(a/2+o(1))`, while a retained cross-lobe response to a pair of depth
`alpha` at the lobe-center separation has scale

```text
X^(alpha*(1-a)-o(1)).                                 (1.4)
```

Consequently a simultaneous interpolation theorem with only `X^o(1)` loss
would close whenever

```text
alpha*(1-a)>a/2.                                     (1.5)
```

Optimizing at `a` decreasing to `r_0` gives

```text
alpha>alpha_0
     =r_0/[2*(1-r_0)]
     =(1-C_0)/[2*(1+C_0)]
     =0.0979071... .                                  (1.6)
```

It would therefore prove the nontrivial uniform strip

```text
Re rho <= 1/2+alpha_0+epsilon
       =0.5979071...+epsilon                         (1.7)
```

for every fixed positive `epsilon`.

That optimized interpolation statement is **false on the current abstract
zero-side inputs**.  The moment-compatible sparse tapered `k=3` island has

```text
K<=X^(2*alpha/3+o(1)).                               (1.8)
```

If the two-lobe construction killed every positive hyperbolic row and
retained (1.4), the other negative rows could only help and the on-line
operator costs only `L^O(1)`, so it would force
`K>=X^(alpha*(1-a)-o(1))`.  Whenever the prime-side power gate (1.5) also
holds, this contradicts (1.8) for every `a<1/3`.
Therefore the `a` decreasing to `r_0` optimization can hold only after using
new zeta-specific information which rules out the sparse island geometry.

The first lobe width not contradicted by that model is `a>=1/3`.  Combining
this with (1.5) gives the weaker countermodel-safe conditional threshold

```text
a downarrow 1/3,
alpha>1/4,
Re rho<=3/4+epsilon.                                  (1.9)
```

No interpolation theorem at `a>1/3` is proved here either.

The missing theorem is not a routine consequence of the dimension count.
The constant `C_0` is a **global dyadic density**, not a local density or a
lower frame bound.  All permitted off-line rows may occur in one locally
saturated block.  For every `a<1/2`, the corresponding one-lobe
interpolation map can have an exponentially small singular value.  The
explicit binomial proof is in Section 6.  This rules out deriving the
needed `X^o(1)` right inverse from (1.2) alone.

The prime translates themselves are not the density obstruction: they are
far below the lobe's Nyquist count, and even their worst elementary local
occupancy is only `X^o(1)`.  The exact remaining problem is a **joint,
target-conditioned grouped Paley--Wiener interpolation theorem for the
off-line positive rows and the prime translates**, or a direct signed
argument which avoids that right inverse.

## 2. Exact time geometry

Put

```text
L=ell_1+eta,                 X=exp(L),
I_+=[(1/2-a)*L,L/2],         I_-=-I_+,
0<a<1/2.                                             (2.1)
```

Each lobe has length `aL`.  Its same-lobe differences satisfy

```text
I_+-I_+ subset [-aL,aL],
I_--I_- subset [-aL,aL],                             (2.2)
```

whereas the positive cross-lobe differences satisfy

```text
I_+-I_-=[(1-2a)*L,L].                                (2.3)
```

The lobe centers are separated by

```text
d_a=(1-a)*L.                                         (2.4)
```

Let `f=r+ell`, with `r` in the right lobe and `ell` in the left lobe.  Fixing
`r` makes every cross-correlation value

```text
<ell,T_y r>,             y in [(1-2a)L,L],            (2.5)
```

linear in `ell`.  Thus every cross-prime-power term can, in the polarized
complex space, be imposed as a linear null condition.  The same
linearization applies to the two pole cross terms.

For an off-line pair `j`, write its hyperbolic contribution as

```text
2*(x_j*x_j^*-y_j*y_j^*).                              (2.6)
```

Imposing

```text
<f,x_j>=0                                             (2.7)
```

kills its positive row.  The remaining `-2*abs(<f,y_j>)^2` is favorable.
All simple on-line rows may be left in place: the unit-count sampling bound
puts their entire positive Gram operator at `L^O(1)`.  Hence one need not
spend a condition on each on-line zero.

The real-admissibility point is exact finite-dimensional linear algebra.  If
`A` is the real symmetric completed matrix and `f=x+i*y`, then

```text
conj(f)^T*A*f=x^T*A*x+y^T*A*y.                       (2.8)
```

Consequently a negative **total** Hermitian form for the independently
polarized complex lobes gives a negative admissible real Rayleigh vector,
either `x` or `y`.  The prime nulls and individual carrier sign need not
descend term by term.  This validates complex linearization without doubling
the condition count.  The endpoint-jet and two-lobe spaces used here are
complexifications of real, conjugation-stable spaces, so `x` and `y` retain
their support, jet, and remote-leakage admissibility.  This argument does not
supply the target leverage missing below.

## 3. Dimension ledger

Let

```text
N=N(T,2T)=(1+o(1))*T*L/(2*pi).                       (3.1)
```

The ambient sharp Gabor coordinate count is `(1+o(1))*N`.  A stable
time--frequency concentration space for one lobe of length `aL` and
frequency aperture `T` has the expected complex dimension

```text
dim E_a=(a+o(1))*T*L/(2*pi)=(a+o(1))*N.              (3.2)
```

The following are the conditions to be paid from this lobe.

### 3.1 Endpoint jets and collar

For mesoscopic padding, the endpoint-tail construction uses

```text
m+O(D*L)<=c*eta*T,                                   (3.3)
```

where `m` is the jet order and `D` is the ordinate collar width.  Since
`eta=o(L)`, this is `o(N)`.  All positive off-line rows in the collar may be
included in the `O(DL)` term; no density theorem in the collar is needed.

### 3.2 Off-line positive rows

Anthropic proves at least `(C_0-o(1))*N` simple on-line zero points.  Every
off-line hyperbolic block consumes two zero points and supplies one positive
row.  Therefore

```text
p_T<=(1-C_0+o(1))*N/2=(r_0+o(1))*N.                 (3.4)
```

The selected pair's own positive mate changes this by only one.

### 3.3 Cross-prime-power rows

The active cross-prime powers obey (2.3), so their number is

```text
q_pr
 <=#{n=p^k: X^(1-2a)<=n<=X}
 =(1+o(1))*X/L.                                      (3.5)
```

At the additive edge `X asymp T*exp(eta)`.  Hence

```text
q_pr/N=O(exp(eta)/L^2)=o(1),                         (3.6)
```

using the admissible raw-prime condition

```text
exp(eta)*log L/L ->0.                                (3.7)
```

The two pole rows and the retained-target condition cost `O(1)`.

Combining (3.2)--(3.6), the formal dimension surplus is

```text
dim E_a-p_T-m-O(DL)-q_pr-O(1)
 >=(a-r_0-o(1))*N.                                  (3.8)
```

This proves that the proposal is not blocked by rank or time--bandwidth
when `a>r_0`.  It does **not** prove that the inhomogeneous system is
surjective, well-conditioned, or target-retaining.

## 4. Power ledger

Let `R_f` denote the zero-extended autocorrelation.  From (2.2), the
same-lobe arithmetic term contains only `n<=X^a`.  Cauchy--Schwarz gives
`abs(R_f(y))<=norm(f)_2^2`, and Chebyshev plus partial summation gives

```text
sum_(n<=X^a) Lambda(n)/sqrt(n)*abs(R_f(log n))
 <<X^(a/2)*norm(f)_2^2.                              (4.1)
```

Polynomial factors in `L` are harmless here.  Conditions (2.5) delete the
cross-lobe prime terms exactly.  The cross-lobe archimedean kernel is
exponentially decreasing, and the same-lobe archimedean part is only
subpower after the standard normalization.

For a selected pair of depth `alpha`, a nonnegligible signed cross
correlation at the center displacement (2.4) has hyperbolic weight

```text
exp(alpha*d_a)=X^(alpha*(1-a)).                      (4.2)
```

This is a safe center-scale target; endpoint concentration can make the raw
Laplace response larger.  A quantitative interpolation statement must
guarantee that normalization, jets, and the positive-row constraints lose
only `X^o(1)` from (4.2).  Under precisely that hypothesis, the target
dominates (4.1) when (1.5) holds.  The on-line `L^O(1)` operator, poles,
archimedean term, and endpoint-jet remote tail are then smaller as well.

This proves the conditional implication (1.6)--(1.7), not its hypothesis.

## 5. Exact projection/right-inverse criterion

Fix a normalized right-lobe seed `r`.  Let `E_-` be the allowed left-lobe
space after endpoint jets and leakage control.  Restrict every off-line
positive row to the two lobes and write it as `x_j^-+x_j^+`.  For every
active cross-prime shift put

```text
v_n=P_(E_-) T_(log n)r.                               (5.1)
```

Include the projected pole rows.  Define

```text
A_T ell
 =((<ell,x_j^->)_j,
   (<ell,v_n>)_n,
   pole coordinates),                                (5.2)

b_T
 =(-(<r,x_j^+>)_j,
   0,
   required pole data).                              (5.3)
```

Let `a_0^-` be the selected negative row on the left and let `a_0^+` be its
right-lobe value.  The exact feasible set is

```text
F_T={ell in E_-: A_T ell=b_T}.                       (5.4)
```

If it is nonempty, its minimum norm is controlled by `A_T^dagger b_T`, and
the homogeneous freedom which can retain the target is

```text
P_(ker A_T) a_0^-.                                   (5.5)
```

Thus a sufficient quantitative statement is

```text
norm(A_T^dagger b_T)<=X^o(1),

sup_(ell in F_T, norm(ell)<=X^o(1))
 abs(<ell,a_0^->+<r,a_0^+>)
 >=X^(alpha*(1-a)/2-o(1)),                           (5.6)
```

with the square in the second line producing (4.2).  Equivalent formulations
may use a lower singular value of the augmented map `(A_T,a_0^-)` or a
distance of `a_0^-` from `range(A_T^*)`.

Equation (3.8) only says that a kernel should have large algebraic
dimension if the listed rows are independent.  It gives neither line of
(5.6).

## 6. A local block has exponentially bad conditioning

The following elementary lemma isolates the failure of the global count.

### Lemma 6.1 (locally supercritical lobe block)

Let

```text
ell=log(T/(2*pi)),        I_a=[-aL/2,aL/2],
Delta=4*pi/ell,           0<a<1/2,       q>=1,         (6.1)
```

and define the synthesis map

```text
S_q b(t)=sum_(j=0)^q b_j*exp(i*j*Delta*t),
            t in I_a.                                (6.2)
```

Then its least singular value satisfies

```text
sigma_min(S_q)
 <=C*sqrt(aL)*q^(1/4)*sin(pi*a*L/ell)^q.             (6.3)
```

The same upper bound holds for the least nonzero singular value of the
adjoint sampling map.  In particular, any right inverse for arbitrary data
on this block has norm at least

```text
c*(aL)^(-1/2)*q^(-1/4)*sin(pi*a*L/ell)^(-q).         (6.4)
```

Here `T` is sufficiently large depending on the fixed `a`; since
`L/ell=1+o(1)`, the sine in (6.3) is then strictly smaller than one.

#### Proof

Take

```text
b_j=(-1)^(q-j)*binom(q,j).
```

Then

```text
S_q b(t)=(exp(i*Delta*t)-1)^q.                       (6.5)
```

For `t in I_a`,

```text
abs(exp(i*Delta*t)-1)<=2*sin(pi*a*L/ell),            (6.6)
```

whereas

```text
norm(b)_2^2=sum_j binom(q,j)^2=binom(2q,q)
            >=c*4^q/sqrt(q).                         (6.7)
```

Taking the `L2(I_a)` norm in (6.5), dividing by (6.7), and using equality of
the nonzero singular values of a map and its adjoint proves (6.3)--(6.4).
QED

### 6.2 Why Anthropic's global density permits this block

At maximal local off-line density, place one reflected pair every
`Delta=4*pi/ell` in ordinate.  The two zero points per pair then have total
density `ell/(2*pi)`, which is at most the Riemann--von Mangoldt main density
throughout `[T,2T]`; simple on-line quantile fillers supply the difference.
Taking

```text
q=(r_0+o(1))*N                                       (6.8)
```

uses an ordinate interval of length

```text
q*Delta=(2*r_0+o(1))*T
       =(1-C_0+o(1))*T<T.                            (6.9)
```

Place this block at the upper end of `[T,2T]` and fill the rest of the
carrier with simple on-line points.  It is compatible even with applying
the global density statement at every shifted dyadic window: if the block
has length `(1-C_0)T` and ends at `2T`, the largest fraction of any interval
`[U,2U]` occupied by the isolated block is `1-C_0`, attained at `U=T`.
Putting only simple on-line points outside the block can only decrease that
fraction.  The slowly varying logarithmic density and endpoint rounding
change it by `o(1)`.  Thus the global theorem, not merely one selected
dyadic count, permits the sampling geometry in Lemma 6.1.

For equal pair depths, restriction of the positive `x` rows to the lobe
only multiplies these exponentials by one common nonvanishing hyperbolic
weight.  Its condition ratio is at worst an `X^O(1)` factor.  This cannot
repair the `exp(-c_a*q)` singular value when `q>>log X`.
Projecting the adjoint rows into an endpoint-jet subspace can only decrease
the norm of the bad dual combination; it either preserves the obstruction
or destroys surjectivity altogether.

For every proposed `a` near `r_0`, (6.3) is exponentially small in `q`, far
below `X^-o(1)`.  This does not prove that the particular right-hand side
and target in (5.6) always realize the worst singular direction.  It proves
the precise no-go needed here:

> Global density plus algebraic dimension cannot supply a uniform
> `X^o(1)` right inverse for the joint interpolation problem.

A target-conditioned theorem might still avoid the bad singular vectors.
That would be new structure, not a consequence of (1.2).

If all pairs in this positive-density block are kept at one fixed depth,
classical horizontal zero-density estimates and the evaluated Zeta23 moment
give additional objections.  Accordingly, this block is used only to refute
the inference from the global `C_0` count to a stable right inverse.  It is
not asserted to satisfy every zeta input simultaneously.

## 7. Prime rows are subcritical; zero rows are the gate

The logarithms of prime powers near `X` need not be uniformly separated,
but their elementary local occupancy is small on the natural resolution
scale.  A log interval of length `1/T` near `log X` corresponds to an
ordinary integer interval of length

```text
O(X/T+1)=O(exp(eta)+1)=X^o(1).                       (7.1)
```

It therefore contains at most `X^o(1)` prime powers.  Together with (3.6),
this shows:

```text
prime-translate count       =o(N),
prime local multiplicity    =X^o(1),
off-line-row local block    may have Theta(N) rows.  (7.2)
```

This is not yet a proof of a stable prime-translate interpolation theorem;
one still needs a grouped frame estimate.  It does rule out blaming the
failure of the raw proposal on prime time--bandwidth.  The prime rows are
strictly subcritical in both the global count and elementary local mesh.

## 8. Sparse versus positive-density off-line sets

The conditioning issue survives the word "sparse."  Lemma 6.1 is
exponentially bad whenever `q -> infinity`; it does not require `q` to be a
positive fraction of `N`.  A block with `q=o(N)` but `q>>log X` can therefore
have a right-inverse cost much larger than every power of `X`.

This is consistent with the sparse tapered `k=3` island.  That construction
has `o(N)` off-line rows, matches the first and Frobenius moments up to
`o(N)`, and still reduces the carrier to `X^(2*alpha/3+o(1))`.  It proves
that bulk moments do not automatically turn sparse off-line geometry into
a one-pair carrier.

The conditioning lemma also occurs inside that legal sparse model.  Its
constant-depth terminal rows have spacing `6*pi/L`.  Repeating (6.5) on a
lobe of length `aL` replaces the sine in (6.3) by
`sin(3*pi*a/2)`.  This is exponentially smaller than one for every fixed
`a<1/3`, including all `a` near `r_0`.  A terminal subblock contains
`q asymp H*L -> infinity` such rows.  Thus even a moment-compatible
`p_T=o(N)` family need not have an `X^o(1)` arbitrary-data interpolation
constant.  As before, this does not by itself identify the selected target
with the bad singular direction.

For the `k=3` island the target failure follows independently of singular
vectors.  Suppose (5.6) held at a width `a<1/3` and that the power gate
`alpha*(1-a)>a/2` also held.  Killing all positive
hyperbolic rows leaves the selected negative square at scale
`X^(alpha*(1-a)-o(1))`; every other negative square has the same favorable
sign, while the complete on-line Gram operator has norm only `L^O(1)` by
the unit-count sampling bound.  Hence the full configuration would have

```text
K>=X^(alpha*(1-a)-o(1))
  >>X^(2*alpha/3+o(1)),                               (8.1)
```

contradicting the island's proved operator upper bound.  Thus the selected
leverage, not only an unrelated singular direction, collapses somewhere in
this admissible family.

There is a useful refinement for a future proof.  Split the additional
pairs at a depth threshold `epsilon>0`.

```text
depth <=epsilon:  strip sampling should bound the whole positive Gram
                  operator by X^(epsilon+o(1))*L^O(1);

depth > epsilon:  classical horizontal zero density makes the row count
                  o(N), but gives no separation or X^o(1) lower frame
                  bound.                              (8.2)
```

Choosing `epsilon<alpha*(1-a)` would make the shallow population harmless
at the proposed target scale.  The hard interpolation should therefore be
asked only for the deeper sparse rows.  The tapered `k=3` island shows why
`o(N)` rank alone still does not solve that refined problem.

For positive-density **regular fixed-depth** masks, the Zeta23 Frobenius
moment is much more effective: the audited `k=7` mask is impossible, and its
signed edge has been computed exactly.  This does not amount to a theorem
that every positive-density clustered or aperiodic row family has the lower
frame bound required in (5.6).  First and Frobenius moments control average
singular-value statistics; matrices with the same two leading moments may
still have an exponentially small least singular value.

The honest dichotomy is therefore

```text
regular positive-density screens   excluded in important model classes;
sparse/local screens               invisible to bulk moments in general;
uniform target-conditioned frame   open.                            (8.3)
```

## 9. Conditional theorem card and next input

### Conditional theorem 9.1 (optimistic actual-zeta version)

Fix `a` and `alpha` with

```text
r_0<a<1/2,
alpha*(1-a)>a/2.                                     (9.1)
```

Assume, uniformly for every hypothetical depth-`alpha` core pair, that:

1. the endpoint-lobe spaces realizing (3.2) have remote leakage smaller
   than the scale in (4.2);
2. the joint positive-row, cross-prime, and pole system satisfies the
   target-conditioned `X^o(1)` estimate (5.6).

Then the completed explicit formula excludes that pair.  Letting `a`
decrease to `r_0` gives (1.6)--(1.7).

This version necessarily uses information absent from the current
count/density/moment ledger, because the sparse `k=3` island contradicts its
second hypothesis for `a<1/3`.

### Conditional theorem 9.2 (countermodel-safe numerical version)

If the same two hypotheses can instead be proved for every fixed
`a>1/3`, then the completed explicit formula excludes every pair with

```text
alpha>1/4+epsilon,                                   (9.2)
```

and gives a uniform zero-free strip with right edge `3/4+epsilon`.  This is
only a numerically consistent target, not a theorem: the known `k=3` model
does not refute it, but neither the global density nor the first two moments
prove its target-conditioned interpolation hypothesis.

### What would remove the condition

Any one of the following would be sufficient progress:

1. a local off-line-row density bound, on every relevant macroscopic and
   mesoscopic ordinate interval, strong enough to keep the sampling density
   below the lobe type;
2. a grouped Paley--Wiener/Carleson theorem proving (5.6) for the actual zeta
   rows despite the bad general singular directions;
3. a direct signed block theorem which uses the other negative rows and
   bypasses individual positive-row interpolation; or
4. a zeta-specific moment/higher-moment statement controlling the required
   target leverage, rather than only trace and Frobenius averages.

The numerical alternatives are now exact.  New zeta arithmetic ruling out
sparse `k=3`-type screening, plus interpolation for every `a>r_0`, would
give the stronger right edge `0.5979071...`.  Without such an exclusion,
the first two-lobe target consistent with the known countermodel has right
edge `3/4`.  Global Anthropic density and time--bandwidth counting prove
neither interpolation statement.
