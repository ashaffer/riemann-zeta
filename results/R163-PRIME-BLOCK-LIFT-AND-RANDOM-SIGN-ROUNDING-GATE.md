# R163 prime-block lift and random-sign rounding gate

## Status

There is a clean arithmetic lift from a **strictly slack** continuous prime
control to coefficients on the actual primes.  Let `K` be compact in
`Re(s)>=sigma_0`, let `Y<=H^kappa`, and suppose a real control `b_H` on
`[H,Y]` satisfies

```text
|b_H(x)|<=1-eta                                             (0.1)
```

for one fixed `eta>0`.  If

```text
theta>7/12,             theta<sigma_0,                     (0.2)
```

then there are real coefficients `c_p in [-1,1]`, supported on
`H<p<=Y`, such that

```text
sup_(s in K)
 |sum_(H<p<=Y)c_p p^(-s)
   -integral_H^Y b_H(x)x^(-s)dx/log x|
       << H^(theta-sigma_0)/log H.                         (0.3)
```

The same statement holds with `p^(-s)` and `x^(-s)` replaced by
`Log(1-p^(-s))` and `Log(1-x^(-s))`.  The proof partitions the prime range
into intervals of length `x^theta` and normalizes each coefficient by the
**actual number of primes in its block**.  Consequently no PNT remainder is
left in (0.3).  Only the variation of the analytic kernel inside a block
remains.  At scale `X` that error is

```text
X^(1-sigma_0) X^(theta-1)
   =X^(theta-sigma_0).                                    (0.4)
```

The condition `theta<sigma_0` is exactly the favorable condition

```text
delta+theta<1,       delta=1-sigma_0.                     (0.5)
```

Thus the classical all-interval exponent `theta>7/12` gives a power saving
precisely when `delta<5/12`.

There is also no probabilistic obstruction to replacing the fractional
coefficients by one sign at each prime.  If `K` lies compactly inside a
bounded domain in `Re(s)>sigma_1>1/2`, independent biased signs give, for at
least one outcome,

```text
sup_(s in K)
 |sum_(H<p<=Y)(epsilon_p-c_p)p^(-s)|
       << H^(1/2-sigma_1)/sqrt(log H),                    (0.6)
```

and again the logarithmic Euler kernel obeys the same bound.  Since
`theta>7/12>1/2`, the block-variation exponent in (0.3), not random
rounding, is the worse of these two losses.

There is a real issue with the particular R162 Poisson control.  It has
`a_N(0)=1` and is exponentially close to `1` through a long initial range;
it has no slack comparable to the relative error in a short-interval PNT.
Normalizing its desired block mass by an actual prime deficit can therefore
produce a coefficient greater than `1`.  Clipping or globally shrinking it
leaves the PNT relative error times a prime sum of size `H^(1-sigma_0)`,
which is not a power-small remainder.  Moreover R162 controls the unweighted
Laplace density `dv`, while the exact prime continuum has weight
`dv/(log H+v)` over a horizon `v=O(log H)`.  That weight cannot simply be
frozen at `1/log H` to power accuracy.

Sections 9--11 repair both defects **locally on a filled pair of sufficiently
small conjugate discs**.  A high-degree-only real polynomial in
`q=exp(h lambda)` gives a late-supported causal control whose approximation
error and coefficient norm both decay exponentially.  Dividing that small
control by the exact logarithmic-density weight repairs the factor
`log H/(log H+v)` without approaching saturation.  The target may be any
uniformly bounded conjugation-symmetric analytic family on slightly larger
filled discs; in particular it may be the normalized **exact prime head**.

Combining this strict-slack control with (0.3) and (0.6) gives a fully
discrete theorem: near any fixed nonreal frequency with
`0<delta<5/12`, on a sufficiently small filled conjugate neighborhood,
one can choose one sign at every prime in `H<p<=H^kappa` so that the signed
tail cancels `sum_(p<=H)p^(-s)` by a fixed negative power of `H`.

This is not yet a zero-free-strip theorem.  The control theorem applies to
single-valued analytic targets on **filled** discs.  The logarithm of a zeta
factor on a contour enclosing a retained zero has monodromy and is not such a
target.  In the nonlinear program the common zeta divisor remains, together
with the collective cofactor whose extra zeros R153--R161 were built to
control.  R163 supplies a new coefficient-specific local shaping mechanism;
it does not prove that the shaped collective cofactor is zero-free.

Date: 2026-08-08.

Predecessor:
[`R162-BOUNDED-CAUSAL-LAPLACE-CONTROLLABILITY.md`](R162-BOUNDED-CAUSAL-LAPLACE-CONTROLLABILITY.md).

## 1. The all-interval prime input

Fix

```text
7/12<theta<1.                                             (1.1)
```

The classical all-interval prime number theorem gives, uniformly as
`x->infinity`,

```text
pi(x+x^theta)-pi(x)
       =(1+o(1)) x^theta/log x.                           (1.2)
```

Only (1.2) is used below.  In particular, the argument does not replace an
exact prime sum by its PNT main term after the coefficients have been
chosen.  The main term in (1.2) is used only to verify the box constraint
`|c_p|<=1`.

For reference, the `7/12` all-interval threshold is the classical Huxley
short-interval exponent; it is distinct from results which merely locate
one prime in a shorter interval.

## 2. Exact block-normalization theorem

### Theorem 2.1 (slack continuum to actual primes)

Let `K` be a compact subset of the complex plane and put

```text
sigma_0=inf_(s in K) Re(s),       M=1+sup_(s in K)|s|.    (2.1)
```

Fix `kappa>1`, `eta>0`, and `theta` such that

```text
7/12<theta<sigma_0.                                      (2.2)
```

For every sufficiently large `H`, every `Y` with
`H<=Y<=H^kappa`, and every real measurable `b_H` on `[H,Y]` satisfying
(0.1), there are real `c_p in [-1,1]`, for primes `H<p<=Y`, for which
(0.3) holds.  The implied constant is uniform in `b_H`, `H`, and `Y`.

### Proof

Set `x_0=H`.  As long as

```text
x_j+x_j^theta<=Y,                                        (2.3)
```

put

```text
h_j=x_j^theta,       I_j=[x_j,x_j+h_j),
x_(j+1)=x_j+h_j.                                         (2.4)
```

Let

```text
N_j=#{p in I_j},
L_j=integral_(I_j) dx/log x,
B_j=integral_(I_j) b_H(x)dx/log x.                        (2.5)
```

By (1.2), uniformly over all these blocks,

```text
N_j=(1+o(1))L_j.                                         (2.6)
```

For large enough `H`, (0.1) and (2.6) imply

```text
|B_j|<= (1-eta)L_j<N_j.                                  (2.7)
```

Define

```text
c_p=B_j/N_j       if p in I_j,                           (2.8)
```

and put `c_p=0` on the final incomplete interval.  Equation (2.7) gives
the exact box constraint.

Fix `s in K`.  For `x<=t<=x+x^theta`, the fundamental theorem of calculus
and (2.1) give

```text
|t^(-s)-x^(-s)|<<_K x^theta x^(-sigma_0-1).              (2.9)
```

The constant parts of the discrete and continuous block contributions
agree exactly:

```text
sum_(p in I_j)c_p x_j^(-s)
       =B_j x_j^(-s)
       =integral_(I_j)b_H(t)x_j^(-s)dt/log t.             (2.10)
```

Using (1.2), (2.9), and `|c_p|<=1`, the difference on block `I_j` is at
most

```text
O_K(h_j^2 x_j^(-sigma_0-1)/log x_j).                     (2.11)
```

Since successive `x_j` are spaced by `h_j`, summing (2.11) is bounded by

```text
integral_H^Y x^(theta-sigma_0-1) dx/log x
       << H^(theta-sigma_0)/log H.                        (2.12)
```

Here `theta<sigma_0` is decisive.  The unfilled terminal interval has
length less than `x_J^theta`; its continuous contribution satisfies the
same bound.  This proves (0.3), uniformly on `K`.  QED.

### Corollary 2.2 (arbitrary exact analytic head)

Let `A_H(s)` be any analytic target on a neighborhood of `K`.  If a
control satisfying (0.1) obeys

```text
sup_(s in K)
 |A_H(s)+integral_H^Y b_H(x)x^(-s)dx/log x|<=E_H,         (2.13)
```

then the coefficients in Theorem 2.1 satisfy

```text
sup_(s in K)|A_H(s)+sum_(H<p<=Y)c_p p^(-s)|
 << E_H+H^(theta-sigma_0)/log H.                          (2.14)
```

In particular one may take the **exact** head

```text
A_H(s)=S_H(s)=sum_(p<=H)p^(-s).                           (2.15)
```

The theorem does not assert the existence of the slack control in (2.13);
it says that once such a control is found, passage to the actual tail
primes costs only the explicit power in (2.14).

## 3. The exact logarithmic-Euler version

For `x` sufficiently large and `s in K`, use the analytic branch

```text
ell_s(x)=Log(1-x^(-s)).                                  (3.1)
```

If `sigma_0>0`, then

```text
|d ell_s(x)/dx|
 =|s x^(-s-1)/(1-x^(-s))|
 <<_K x^(-sigma_0-1).                                    (3.2)
```

Repeating the proof of Theorem 2.1 verbatim gives

```text
sup_(s in K)
 |sum_(H<p<=Y)c_p Log(1-p^(-s))
  -integral_H^Y b_H(x)Log(1-x^(-s))dx/log x|
 << H^(theta-sigma_0)/log H.                             (3.3)
```

Thus block normalization respects the exact optional-prime Euler factors;
there is no need to discard their prime-square and higher terms after the
lift.

## 4. Randomized rounding in Bergman norm

### Theorem 4.1 (one sign per actual prime)

Let `Omega` be a bounded plane domain with

```text
closure(Omega) subset {Re(s)>sigma_1},    sigma_1>1/2,    (4.1)
```

and let `K` be compactly contained in `Omega`.  For every finite set of
primes `P subset (H,infinity)` and every choice `c_p in [-1,1]`, there are
signs `epsilon_p in {+1,-1}` such that

```text
sup_(s in K)
 |sum_(p in P)(epsilon_p-c_p)p^(-s)|
 <<_(K,Omega,sigma_1) H^(1/2-sigma_1)/sqrt(log H).        (4.2)
```

The same conclusion holds with `p^(-s)` replaced by
`Log(1-p^(-s))`.

### Proof

Choose the signs independently with

```text
Prob(epsilon_p=1)=(1+c_p)/2.                             (4.3)
```

Then `E(epsilon_p-c_p)=0` and

```text
E|epsilon_p-c_p|^2=1-c_p^2<=1.                           (4.4)
```

For

```text
R(s)=sum_(p in P)(epsilon_p-c_p)p^(-s),                  (4.5)
```

independence and Fubini give

```text
E ||R||_(A^2(Omega))^2
 <=area(Omega) sum_(p>H)p^(-2sigma_1)
 << H^(1-2sigma_1)/log H.                                (4.6)
```

The last estimate follows already from the standard Chebyshev upper bound
for primes, by a dyadic decomposition.  Hence one outcome has Bergman norm
at most the square root of the right side.  The interior Bergman evaluation
bound

```text
sup_K |R|<<_(K,Omega)||R||_(A^2(Omega))                  (4.7)
```

proves (4.2).

For the logarithmic kernel,

```text
|Log(1-p^(-s))|<<p^(-Re(s))                              (4.8)
```

uniformly on `Omega` once `H` is large.  Equations (4.6)--(4.7) therefore
apply without change.  QED.

The same argument simultaneously rounds any fixed number of channels or
derivatives, at the cost of changing the implied constant.  Real signs also
preserve conjugation symmetry automatically.

## 5. Combined exponent ledger

Assume a slack exact-head control (2.13), and choose

```text
7/12<theta<sigma_0.                                      (5.1)
```

After exact-prime lifting and sign rounding, the total error on a slightly
smaller compact set is

```text
E_H
 +O(H^(-(sigma_0-theta))/log H)
 +O(H^(-(sigma_1-1/2))/sqrt(log H)).                     (5.2)
```

Because `theta>1/2`, the first exponent is smaller.  Taking `theta` as
close to `7/12` as allowed yields every exponent

```text
c<sigma_0-7/12.                                          (5.3)
```

Equivalently, writing `sigma_0=1-delta`, the lift has a fixed power exactly
for

```text
delta<5/12.                                               (5.4)
```

This is a genuine fixed-power arithmetic theorem.  Sections 9--11 verify its
slack-control hypothesis for bounded analytic exact heads on a sufficiently
small filled conjugate-disc pair.  It is not a zero-free-strip theorem because
the retained zeta divisor and the nonlinear collective cofactor remain.

## 6. Why saturation is not a bookkeeping issue

Suppose only `|b_H|<=1`.  In a block `I_j`, the normalization (2.8) asks
for

```text
|c_p|=|B_j|/N_j.                                         (6.1)
```

If `b_H` is essentially `1` there and the actual block contains fewer
primes than its logarithmic-integral main term, (6.1) exceeds `1`.  The
two-sided asymptotic (1.2) does not prevent this.  Clipping changes the
block mass by the prime-count discrepancy.  Summed against a kernel whose
natural size is `H^(1-sigma_0)`, a merely `o(1)` relative discrepancy is
not the `H^(-c)` remainder required here.

The Poisson-tail control of R162 is maximally exposed to this issue:

```text
a_N(0)=1,
1-a_N(v)=exp(-alpha v)sum_(n>N)(alpha v)^n/n!,            (6.2)
```

so its deficit from `1` is vastly smaller than the known relative PNT
error throughout its saturated initial range.  Exact block counts remove
the PNT error only after a feasible mass `|B_j|<=N_j` has been prescribed;
they cannot create missing coefficient capacity.

At this point there are two honest ways forward:

1. Prove a weighted causal-Laplace control with fixed slack
   `|b_H|<=1-eta` and target the exact prime head in (2.13).
2. Prove a bounded overflow-redistribution theorem which moves the excess
   mass of saturated deficit blocks into later prime blocks while retaining
   uniform analytic accuracy.

Neither statement is contained in the ordinary short-interval PNT.  Section
9 proves the first statement locally by replacing the saturated Poisson
profile with a late-supported high-degree polynomial control.

## 7. The logarithmic-density correction left by R162

With `x=H exp(v)` and `lambda=1-s`, the exact continuum prime density is

```text
x^(-s)dx/log x
 =H^lambda exp(lambda v)dv/(log H+v).                    (7.1)
```

R162 controls

```text
1/lambda+integral a_H(v)exp(lambda v)dv.                 (7.2)
```

On its required horizon `v=O(log H)`, the ratio

```text
log H/(log H+v)                                          (7.3)
```

varies by a fixed amount.  It cannot be absorbed into an `o(1)`, much less
a power-small error.  Multiplying the R162 profile by
`1+v/log H` repairs the density algebraically, but generally violates the
coefficient bound and aggravates saturation.  The late-supported control in
Section 9 has exponentially small amplitude, so Section 10 can make exactly
this multiplication without spending its slack.

## 8. Reality check

```text
continuous slack control -> actual fractional primes      THEOREM
PNT discrepancy after block normalization                 ZERO
block variation for delta<5/12                            POWER-SMALL
fractional coefficients -> one sign per prime             THEOREM
rounding scale in Re(s)>1/2                               POWER-SMALL
R162 Poisson profile has usable slack                      NO
R162 unweighted profile handles exact prime density        NO
late-supported exact-head weighted slack control           THEOREM LOCAL
exact signed prime-head cancellation for delta<5/12        THEOREM LOCAL
zeta-log control on a filled disc containing a zeta zero   BLOCKED BY MONODROMY
nonlinear collective cofactor zero-free                    OPEN
fixed uniform zeta zero-free strip                         NOT PROVED
zeros approaching Re(s)=1                                  NOT PROVED
```

## 9. Late-supported strict-slack causal control

The saturation in Section 6 is a property of the Poisson profile, not of
bounded causal Laplace control.  The following theorem gives a control whose
supremum norm tends to zero.

### Theorem 9.1 (filled conjugate-disc strict slack)

Fix

```text
lambda_0=delta+i gamma,       delta>0,       gamma!=0.    (9.1)
```

There are radii `0<r_0<r_1`, a cell length `h>0`, and constants
`C,c>0`, depending only on `lambda_0`, with the following property.  Put

```text
Lambda_j={|lambda-lambda_0|<=r_j}
         union {|lambda-conjugate(lambda_0)|<=r_j}.       (9.2)
```

Let `f_N` be any family of functions holomorphic on a neighborhood of
`Lambda_1`, satisfying

```text
f_N(conjugate(lambda))=conjugate(f_N(lambda)),
sup_(Lambda_1)|f_N|<=1.                                  (9.3)
```

For every integer `N>=1` there is a real step function `a_N` such that

```text
support(a_N) subset [Nh,CNh],
||a_N||_infinity<=C exp(-cN),                             (9.4)

sup_(lambda in Lambda_0)
 |f_N(lambda)+integral_0^infinity
                  a_N(v)exp(lambda v)dv|
       <=C exp(-cN).                                     (9.5)
```

The steps of `a_N` have length `h`.  Thus its Laplace transform is an exact
finite exponential polynomial, not a continuum heuristic.

### Proof

Choose a phase `phi` strictly between `0` and `pi`.  Along the arithmetic
progression

```text
h=(2 pi m+phi)/|gamma|,                                  (9.6)
```

the two central images under

```text
q=exp(h lambda)                                          (9.7)
```

are conjugate points `z` and `conjugate(z)`, while
`|z|=exp(h delta)` can be made arbitrarily large.  First choose `m` so that
this modulus is larger than the fixed constants below, and then choose
`r_1` small enough that (9.7) is biholomorphic on both discs and their
images are disjoint compact neighborhoods of the two centers, outside the
unit circle.

Set

```text
W(q)=(q-z)(q-conjugate(z)).                              (9.8)
```

This polynomial has real coefficients.  Shrinking `r_1` once more gives
two nested polynomial lemniscates

```text
L_0 subset interior(L_1),
L_j={q:|W(q)|<=rho_j},       0<rho_0<rho_1,               (9.9)
```

whose two components lie in the two exponential images.  On `L_1`, every
holomorphic conjugation-symmetric function `g` has the exact two-sheet
decomposition

```text
g(q)=G_0(W(q))+q G_1(W(q)),                              (9.10)
```

where `G_0,G_1` are holomorphic for `|W|<=rho_1` and have real Taylor
coefficients.  Indeed, if `q_+(w),q_-(w)` are the two inverse roots of
`W(q)=w`, then

```text
G_1(w)=[g(q_+(w))-g(q_-(w))]/[q_+(w)-q_-(w)],
G_0(w)=[q_+(w)g(q_-(w))-q_-(w)g(q_+(w))]
       /[q_+(w)-q_-(w)].                                (9.11)
```

The denominators stay away from zero on the chosen lemniscate.  Conjugation
in (9.11) proves the reality assertion.

Apply (9.10) to `q^(-N)g(q)` and truncate the two Taylor series in `W` at
degree `dN`, where `d` is a fixed sufficiently large integer.  Call the
resulting real polynomial `Q_N(q)`.  Cauchy's estimate on the nested
`W`-discs gives

```text
sup_(L_0)|q^(-N)g(q)-Q_N(q)|
 << R_-^(-N)(rho_0/rho_1)^(dN),                          (9.12)
```

where `R_-=min_(L_1)|q|>1`.  Multiplication by `q^N` gives a polynomial

```text
P_N(q)=q^N Q_N(q)                                        (9.13)
```

supported in degrees from `N` through `N+2dN+1` and

```text
sup_(L_0)|g-P_N|<<exp(-c_1N).                            (9.14)
```

after `d` is chosen so that the geometric Taylor gain beats
`max_(L_0)|q|/R_-`.

It remains to check coefficient size; this is why the centers were moved
far outside the unit circle before the discs were fixed.  If
`B=||W||_(ell^1)` denotes the sum of the absolute values of the three
coefficients in (9.8), the coefficient norm of a degree-`dN` Taylor
polynomial in `W` is at most

```text
O(R_-^(-N))(1+B/rho_1)^(dN).                             (9.15)
```

Choose the relative lemniscate radii fixed as `|z|` grows.  Then
`B/rho_1=O(1)`, whereas `R_-` is a fixed positive multiple of `|z|`.
Taking `m` still larger if necessary makes the right side of (9.15)
`O(exp(-c_2N))`.  Multiplication by `q^N` only shifts coefficient indices.
Thus, writing

```text
P_N(q)=sum_n c_(n,N)q^n,                                (9.16)
```

all `c_(n,N)` are real and

```text
max_n |c_(n,N)|<<exp(-c_2N).                             (9.17)
```

For the target in (9.5), define on the two exponential images

```text
g(q)=-lambda(q)f_N(lambda(q))/(q-1).                     (9.18)
```

The two inverse branches are used separately.  Equation (9.3) makes (9.18)
conjugation-symmetric, and `q=1` is outside `L_1`.  Let `P_N` be the
polynomial just constructed and put

```text
a_N(v)=c_(n,N)       for nh<=v<(n+1)h.                  (9.19)
```

Then, exactly,

```text
integral_0^infinity a_N(v)exp(lambda v)dv
   =[q-1]P_N(q)/lambda.                                 (9.20)
```

Equations (9.14), (9.17), and (9.18)--(9.20) prove
(9.4)--(9.5), after changing the constants.  QED.

The filled-disc hypothesis is substantive.  The proof approximates a
holomorphic target on the whole lemniscate component, not merely on its
boundary.

## 10. Exact logarithmic weight and exact analytic heads

Put

```text
T=log H,       lambda=1-s.                              (10.1)
```

Let `A_H(s)` be analytic on the `s`-images of `Lambda_1` and suppose its
normalized family

```text
f_H(lambda)=T H^(-lambda)A_H(1-lambda)                  (10.2)
```

is uniformly bounded there and respects conjugation.  Apply Theorem 9.1
with `N=ceil(BT)`, after dividing by that uniform bound.  The constant `B`
may be chosen as large as any prescribed power accuracy requires.  Define

```text
b_H(v)=(T+v)a_N(v)/T.                                   (10.3)
```

Since the support length in (9.4) is `O(N)=O(T)`, while
`||a_N||_infinity=O(exp(-cN))`, one has, for large `H`,

```text
support(b_H) subset [0,C_B log H],
||b_H||_infinity<=1/2.                                  (10.4)
```

Set `Y=H exp(C_B log H)=H^kappa`.  The logarithmic weight is now repaired
by an exact identity:

```text
integral_H^Y b_H(log(x/H))x^(-s)dx/log x

 =H^lambda/T integral_0^(C_B log H)
                     a_N(v)exp(lambda v)dv.             (10.5)
```

Combining (9.5), (10.2), and (10.5), and increasing `B`, gives, for every
fixed `A>0`,

```text
sup_(s in 1-Lambda_0)
 |A_H(s)+integral_H^Y b_H(log(x/H))x^(-s)dx/log x|
       <=H^(-A).                                        (10.6)
```

Thus the strict-slack weighted control required by Corollary 2.2 exists for
every target satisfying the explicit boundedness condition (10.2).

### The exact prime head satisfies the hypothesis

Take

```text
A_H(s)=S_H(s)=sum_(p<=H)p^(-s).                          (10.7)
```

On the slightly larger frequency discs, `Re(lambda)` is bounded below by a
positive constant.  Chebyshev's upper bound and partial summation give,
uniformly there,

```text
sum_(p<=H)p^(Re(lambda)-1)
       << H^(Re(lambda))/log H.                          (10.8)
```

Hence (10.2) is uniformly bounded.  This use of the PNT is only a norm
bound for the exact analytic target; the block construction in Theorem 2.1
still normalizes by the actual prime counts.

## 11. Fully discrete signed prime cancellation

### Theorem 11.1

Let `lambda_0=delta+i gamma`, where

```text
0<delta<5/12,       gamma!=0.                            (11.1)
```

There is a sufficiently small filled conjugate-disc pair `Lambda_0` around
`lambda_0` and its conjugate, and constants `kappa>1`, `c>0`, such that for
every sufficiently large `H` there are signs

```text
epsilon_p in {+1,-1},       H<p<=H^kappa,                (11.2)
```

with

```text
sup_(lambda in Lambda_0)
 |sum_(p<=H)p^(lambda-1)
   +sum_(H<p<=H^kappa)epsilon_p p^(lambda-1)|
       <<H^(-c).                                         (11.3)
```

### Proof

Shrink the discs so that

```text
sigma_0=inf_(lambda in Lambda_0) Re(1-lambda)>7/12.      (11.4)
```

Choose `theta` strictly between `7/12` and `sigma_0`.
Equations (10.6) and (10.7), followed by Theorem 2.1, give fractional actual
prime coefficients with error

```text
O(H^(-(sigma_0-theta))/log H).                           (11.5)
```

Theorem 4.1 rounds them to signs with the smaller error

```text
O(H^(-(sigma_1-1/2))/sqrt(log H))                        (11.6)
```

on a slightly smaller disc, where `sigma_1>1/2`.  The continuum error in
(10.6) can be made smaller than both.  Since `theta>1/2`, (11.5) is the
limiting term.  Any

```text
c<sigma_0-7/12                                           (11.7)
```

is available after choosing the radii and `theta`.  QED.

There is an Euler-factor corollary.  The finite head

```text
L_H(s)=sum_(p<=H)Log(1-p^(-s))                           (11.8)
```

is analytic on these discs and satisfies the normalized boundedness
hypothesis.  Apply the same construction to the target `-L_H`, so that the
signed linear tail approximates `L_H`, and use

```text
Log(1-p^(-s))=-p^(-s)+O(p^(-2 Re(s))).                   (11.9)
```

The tail of the error in (11.9) is
`O(H^(1-2sigma_0)/log H)`.  Consequently the signs may also be chosen so
that

```text
sum_(p<=H)Log(1-p^(-s))
 +sum_(H<p<=H^kappa)epsilon_p Log(1-p^(-s))
       =O(H^(-c'))                                       (11.10)
```

uniformly on a slightly smaller disc, for some `c'>0`.

Equation (11.10) is a genuine coefficient-specific local shaping theorem
for the optional-prime Euler family left open by R160.  It makes the finite
Euler multiplier locally `1+O(H^(-c'))` while retaining its exact head
deletion and the common zeta divisor.

## 12. The remaining nonlinear and topological gate

Theorem 11.1 does not cancel a retained zeta zero.  It shapes a
single-valued analytic finite Euler multiplier.  If a contour encloses a
zeta zero, `Log zeta` has nonzero monodromy and cannot satisfy the
filled-disc hypothesis (9.3).  Approximating only the contour would not
repair this: a zero-free analytic exponential inside has winding zero.

In the collective amplifier, every shaped channel still has the common
zeta factor.  The desired scalar therefore factors as

```text
zeta(s) times a collective cofactor.                     (12.1)
```

R160 closes the fixed finite full-cutoff version by forcing cofactor zeros.
Theorem 11.1 lies outside that no-go because it uses independently signed,
growing optional-prime controls, but it does not prove the new cofactor
zero-free.  The next theorem must use the available local Euler shaping to
construct a collective cofactor with a quantitative lower bound on the
whole target contour, while respecting its winding.  That is the remaining
place where a fixed zero-free strip could enter.
