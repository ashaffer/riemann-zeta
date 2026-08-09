# R95 signed multiscale queue and complex-cycle gate

Status: exact flat scale-cocycle theorem, complex-flow Hodge dichotomy,
finite-filter recurrence obstruction, an explicit nonlattice Volterra
filter with a bounded one-sign-change prime kernel, and a one-sided Landau
criterion for a fixed strip.  The one-sided criterion is a genuine
reduction of the missing signed estimate, but it is not proved for the
actual von Mangoldt coefficients.  No fixed strip and no failure of every
fixed strip is proved.

Date: 2026-08-07.

## 1. Verdict

R94 showed that every positive phase-aware transport norm sees the absolute
Chebyshev queue.  This report gives up positivity *inside the queue* and
tests signed scale cycles, complex electrical flows, and nonlattice
high-pass filters.

There are four exact conclusions.

1. Normalized logarithmic scale shifts form a commuting semigroup.  Their
   prime--pole differences obey an exact cocycle identity, and every closed
   scale rectangle has zero holonomy.  A cycle therefore contributes no
   Mellin work; only the source and the boundary flux survive.

2. In any Hermitian or sectorial complex-flow certificate, Hodge
   decomposition removes cycles from the minimizer.  Complex circulations
   can only increase the positive energy.  If the conjugation is removed so
   that cycles can cancel, a two-parallel-edge example has nonzero source
   and exactly zero quadratic energy.  Such a form is not a certificate.

3. A finite pole-killing scale filter has arbitrarily high near-blind
   vertical frequencies by simultaneous recurrence.  A continuous
   nonlattice delay avoids that obstruction.  The exponential delay with
   rate `lambda>1` has the explicit multiplier

   ```text
   B_lambda(s)=(s-1)/(s+lambda-1).                         (1.1)
   ```

   For `lambda=2`, the cumulative filtered queue is the unusually simple
   signed ramp

   ```text
   R_2(log x)
    =sum_(n<=x)Lambda(n)(2n/x-1)-1+x^(-1).                (1.2)
   ```

   Every coefficient in the prime sum lies in `[-1,1]`, there is only one
   sign change, the continuum pole cancels exactly, and `B_2` is uniformly
   nonzero at every nontrivial zeta zero.  This is the cleanest surviving
   signed queue found in this branch.

4. It is enough to bound only **one side** of (1.2).  If, for some `a<1`,
   either

   ```text
   R_2(log x)>=-C x^a                                    (1.3)
   ```

   or

   ```text
   R_2(log x)<= C x^a,                                   (1.4)
   ```

   for all sufficiently large `x`, then `zeta(s)` has no zero in
   `Re(s)>a`.  The proof uses Landau's theorem for the Laplace transform of
   an eventually nonnegative function.  Conversely a zero-free half-plane,
   with an endpoint epsilon, gives both bounds.  Thus the rightmost-zero
   exponent is already encoded in either one-sided envelope of this bounded
   signed ramp.

The reduction from a two-sided prime number theorem to one signed side is
real.  However positivity of `Lambda`, flat scale algebra, and the standard
Selberg-size remainder do not imply (1.3) or (1.4).  An explicit positive
prime-like continuous countermodel passes all those generic tests and has
off-line Mellin poles.

The remaining target is coefficient-specific: prove a fixed-power
one-sided barycenter inequality for the actual von Mangoldt measure, or
construct a genuinely non-flat arithmetic transport whose cycle holonomy
contains new information.  Ordinary scale cycles are exactly flat.

## 2. Normalized scale shifts are flat

Retain the logarithmic prime and pole measures

```text
M=sum_(n>=2)Lambda(n)delta_(log n),
P=exp(u)du,
nu=M-P.                                                    (2.1)
```

For `h>=0`, let `tau_h` translate a measure to the right by `h`, and define
the pole-normalized shift

```text
S_h=exp(h)tau_h.                                           (2.2)
```

Its Laplace action is

```text
L(S_h mu)(s)=exp((1-s)h)L(mu)(s).                         (2.3)
```

On the pole measure,

```text
S_hP=1_(u>=h)exp(u)du,
(I-S_h)P=1_(0<=u<h)exp(u)du.                              (2.4)
```

Thus `I-S_h` kills the *tail* of the pole exactly, leaving only a compact
boundary correction.

The normalized shifts form an exact semigroup:

```text
S_hS_k=S_(h+k)=S_kS_h.                                    (2.5)
```

Put

```text
C_h=(I-S_h)nu.                                            (2.6)
```

**Theorem 2.1 (flat scale cocycle).**  For every `h,k>=0`,

```text
C_(h+k)=C_h+S_hC_k=C_k+S_kC_h,                            (2.7)

C_h+S_hC_k-C_k-S_kC_h=0.                                 (2.8)
```

### Proof

The first equality is the operator identity

```text
I-S_hS_k=(I-S_h)+S_h(I-S_k).                              (2.9)
```

Interchanging `h` and `k` and using (2.5) gives the second equality and
(2.8).  QED.

Equation (2.8) is the exact closed rectangular cycle.  It vanishes for
every measure, not just the primes.  Multiplying `S_h` by a scalar character
`exp(i alpha h)` still gives a commuting semigroup and does not create
curvature.

In the transform variable,

```text
L(C_h)(s)
 =[1-exp((1-s)h)]
  [-zeta'(s)/zeta(s)-1/(s-1)].                            (2.10)
```

At a nontrivial zero `rho` and for every `h>0`, the bracket has a pole and

```text
1-exp((1-rho)h)!=0                                       (2.11)
```

because `Re(rho)<1`.  A single scale coboundary faithfully retains every
fixed zero.  Closing several such paths into a scale cycle gives (2.8), not
an additional relation.

For an infinite path, a purported cycle can close only by sending flux to
infinity.  Discrete integration by parts then leaves the endpoint term

```text
exp(-sU)D(U),
D(U)=psi(exp(U))-(exp(U)-1),                              (2.12)
```

which is exactly the boundary queue in R94.  Calling it a circulation at
infinity does not remove it.

## 3. Complex flow: the Hodge dichotomy

The preceding flatness has a graph-theoretic version that covers nonlocal
edges and arbitrary complex phases.

Let `G=(V,E)` be a finite oriented graph, let `partial` be its incidence
operator, and let a complex flow `J` satisfy

```text
partial J=b,                                               (3.1)
```

where the total source `b` is zero.  For a complex vertex potential `f`,

```text
<b,f>=<J,partial^*f>.                                     (3.2)
```

Here the brackets use the usual Hermitian pairing.

**Theorem 3.1 (cycles do no work).**  If `Z` is any complex circulation,
`partial Z=0`, then

```text
<J+Z,partial^*f>=<J,partial^*f>=<b,f>.                    (3.3)
```

Consequently a cycle cannot alter the Mellin work of a flow with fixed
marginals.

Now assign positive conductances `c_e` and use the Hermitian Thomson energy

```text
E(J)=sum_e abs(J_e)^2/c_e.                                (3.4)
```

The affine space `{J:partial J=b}` is a translate of `ker(partial)`.  Its
minimum-energy member is orthogonal, in the conductance metric, to every
cycle.  Therefore

```text
E(J+Z)=E(J)+E(Z)                                          (3.5)
```

at the minimizer.  Allowing complex flows changes no part of this Hilbert
projection.

Every cut retains the same obstruction.  If `A` is a set of vertices, then

```text
sum_(v in A)b_v=sum_(e crosses boundary A) epsilon_e J_e. (3.6)
```

Cauchy--Schwarz gives

```text
abs(sum_(v in A)b_v)^2
 <=[sum_(e crosses boundary A)c_e]
   [sum_(e crosses boundary A)abs(J_e)^2/c_e].             (3.7)
```

For consecutive scale vertices, the source on a prefix is precisely the
twisted or untwisted cumulative prime--pole queue.  Parallel and nonlocal
edges may enlarge cut capacity, but they cannot change its net flux.

The only apparent escape is to remove complex conjugation.  It is false as
a certificate in the smallest possible example.  Take two parallel edges
with source constraint

```text
J_1+J_2=b!=0                                              (3.8)
```

and the complex-bilinear form

```text
Q(J)=J_1^2+J_2^2.                                         (3.9)
```

The feasible flow

```text
J_1=(1+i)b/2,
J_2=(1-i)b/2                                              (3.10)
```

has

```text
Q(J)=0.                                                    (3.11)
```

Thus an indefinite complex energy can certify zero cost for a nonzero
source.  If instead a non-Hermitian form is sectorial,

```text
Re Q(J)>=c sum_e abs(J_e)^2/c_e,       c>0,               (3.12)
```

then it is comparable with (3.4) and returns to the cut bound (3.7).  This
is the exact dichotomy:

```text
coercive complex flow      cycles cannot help;
noncoercive complex flow   false zero-energy sources exist.             (3.13)
```

## 4. Finite signed scale filters have recurrent blind spots

A finite scale filter has the form

```text
A=sum_(j=0)^m a_j S_(h_j),                               (4.1)

Ahat(s)=sum_(j=0)^m a_j exp((1-s)h_j).                    (4.2)
```

To kill the pole tail it must satisfy

```text
Ahat(1)=sum_j a_j=0.                                      (4.3)
```

At a zeta zero `rho`, the filtered logarithmic derivative retains its pole
exactly when

```text
Ahat(rho)!=0.                                             (4.4)
```

If (4.4) fails, the filter has hidden the target rather than excluded it.

**Theorem 4.1 (finite-filter recurrence).**  Every finite filter satisfying
(4.3) has a sequence `abs(t_n)->infinity` such that

```text
Ahat(1+it_n)->0.                                          (4.5)
```

Consequently, for every `eta>0`,

```text
inf_(1-eta<sigma<=1, t in R) abs(Ahat(sigma+it))=0.        (4.6)
```

### Proof

Simultaneous Diophantine approximation supplies `t_n` for which

```text
exp(-it_n h_j)->1                                         (4.7)
```

for every `j`.  Substitution in (4.2) and (4.3) proves (4.5).  Letting
`sigma` tend to one slowly along the same sequence proves (4.6).  QED.

This is an obstruction to a *uniformly invertible* finite cyclic filter,
not a claim that an actual zeta zero occurs at a blind frequency.

There is also a general growth ledger.  Suppose a scale-dependent filter
`A_U` acts on an exponential mode `exp(rho U)` and is faithful at that mode
in the sense that

```text
exp(-o(U))<=abs(Ahat_U(rho))<=exp(o(U)).                   (4.8)
```

Then

```text
abs(A_U exp(rho U))=exp(Re(rho)U+o(U)).                   (4.9)
```

Thus every fixed filter, and every `o(U)`-fold iteration with
subexponential coefficient norm and nonvanishing target response, preserves
the real growth exponent.  If the response is exponentially small instead,
the inverse condition number is exponentially large and the filter has
suppressed the evidence it was meant to detect.

## 5. A faithful nonlattice filter and its exact prime ramp

Continuous delays can avoid Theorem 4.1.  For `lambda>1`, average the
normalized shifts against an exponential law:

```text
K_lambda
 =integral_0^infinity S_h lambda exp(-lambda h)dh.         (5.1)
```

Its transform multiplier is

```text
Khat_lambda(s)
 =integral_0^infinity lambda exp(-(lambda+s-1)h)dh
 =lambda/(s+lambda-1),                                    (5.2)

B_lambda(s):=1-Khat_lambda(s)
 =(s-1)/(s+lambda-1).                                     (5.3)
```

The only zero of `B_lambda` in `Re(s)>0` is `s=1`, where it kills the pole
tail.  It has no vertical recurrence.

Let

```text
R_lambda(U)=((I-K_lambda)nu)([0,U]).                       (5.4)
```

Since

```text
(K_lambda nu)([0,U])
 =integral_0^U lambda exp(-(lambda-1)h)D(U-h)dh,           (5.5)
```

one has the exact Volterra high-pass formula

```text
R_lambda(U)
 =D(U)-integral_0^U lambda exp(-(lambda-1)h)D(U-h)dh.      (5.6)
```

Writing `x=exp(U)` and summing the Stieltjes integral by prime powers gives

**Theorem 5.1 (bounded signed Riesz kernel).**

```text
R_lambda(log x)
 =sum_(n<=x)Lambda(n)
    [lambda(n/x)^(lambda-1)-1]/(lambda-1)
  -(1-x^(1-lambda))/(lambda-1).                           (5.7)
```

### Proof

Under `y=x exp(-h)`, the prime cumulative part of (5.5) is

```text
lambda x^(1-lambda)
 integral_1^x psi(y)y^(lambda-2)dy.                       (5.8)
```

Expanding `psi(y)` and integrating from each prime power `n` to `x` gives

```text
sum_(n<=x)Lambda(n)
 [lambda/(lambda-1)]
 [1-(n/x)^(lambda-1)].                                    (5.9)
```

Subtracting (5.9) from `psi(x)` gives the prime coefficient in (5.7).  The
same calculation on `-(x-1)` gives the final elementary correction.  QED.

At `lambda=2`, (5.7) becomes (1.2).  This filter has several unusually good
properties:

```text
prime weights                  2n/x-1 in [-1,1]
number of sign changes         one
continuum main term            exactly zero
delay law                      absolutely continuous
multiplier zeros in Re(s)>0    only s=1.                  (5.10)
```

It is also uniformly faithful on the zeta divisor.  Let

```text
gamma_* = inf {abs(Im(rho)): zeta(rho)=0, 0<Re(rho)<1}.    (5.11)
```

There are no real nontrivial zeros and zeros are discrete, so
`gamma_*>0`.  For `rho=beta+i gamma`,

```text
abs(B_2(rho))^2
 =[(1-beta)^2+gamma^2]/[(1+beta)^2+gamma^2]
 >=gamma_*^2/(gamma_*^2+4)>0.                             (5.12)
```

Thus the nonlattice filter neither creates artificial zeros nor approaches
zero along the actual zeta divisor.

The measure-side smoothing is explicit too:

```text
(K_lambda M)(du)
 =lambda sum_(log n<=u)Lambda(n)
   exp(-(lambda-1)(u-log n))du,                           (5.13)

(I-K_lambda)P=exp(-(lambda-1)u)du.                        (5.14)
```

Hence `(I-K_lambda)nu` still contains every original positive prime-power
atom, opposed by a smooth signed history.  Its total variation has not
improved; the gain in (5.7) exists only before absolute values.

## 6. A one-sided fixed-power bound is enough

The signed ramp allows a sharper target than a two-sided PNT estimate.

For `Re(s)>1`, (2.1), (5.3), and integration of a cumulative measure give

```text
L_lambda(s)
 :=integral_0^infinity R_lambda(U)exp(-sU)dU
 ={B_lambda(s)/s}
   [-zeta'(s)/zeta(s)-1/(s-1)].                           (6.1)
```

The right side is meromorphic in `Re(s)>0`.  It is analytic at every
positive real `s`: zeta has no real zero in `(0,1)`, the singularity at one
inside the square brackets is removable, and `B_lambda(1)=0`.  At every
nontrivial zero `rho`, however, (5.3) is nonzero and (6.1) has a pole.

We use the classical Landau principle.

**Lemma 6.1 (Landau).**  If a locally integrable function `g(U)` is
nonnegative for all sufficiently large `U`, is of exponential order, and
has finite Laplace abscissa `sigma_c`, then its Laplace transform has a
singularity at the real point `s=sigma_c`.

The same statement follows for an eventually nonnegative function after a
compact modification.  Positivity is essential: it prevents cancellation
of the moments that would otherwise continue the transform through its
real convergence boundary.

**Theorem 6.2 (one-sided ramp criterion).**  Fix `lambda>1` and `0<a<1`.
If either

```text
R_lambda(U)>=-C exp(aU)                                   (6.2)
```

or

```text
R_lambda(U)<= C exp(aU)                                   (6.3)
```

for all sufficiently large `U`, then

```text
zeta(s)!=0,                    Re(s)>a.                    (6.4)
```

### Proof

Assume (6.2); the other case follows after replacing `R_lambda` by its
negative.  After a compact modification, the function

```text
g(U)=R_lambda(U)+C exp(aU)                                (6.5)
```

is nonnegative.  Its Laplace transform is

```text
G(s)=L_lambda(s)+C/(s-a)+E(s),                            (6.6)
```

where `E` is entire and accounts for the compact modification.

Suppose `rho=beta+i gamma` were a zeta zero with `beta>a`.  By (5.3),
`L_lambda` and hence `G` have a pole at `rho`.  Therefore the Laplace
abscissa `sigma_c` of the nonnegative function `g` must satisfy

```text
sigma_c>=beta>a;                                          (6.7)
```

otherwise the defining Laplace integral would make `G` holomorphic at
`rho`.  Lemma 6.1 now forces a singularity of `G` at the real point
`sigma_c`.  But (6.1) and (6.6) are analytic at every real point strictly
larger than `a`.  This contradicts (6.7).  QED.

The converse holds with endpoint epsilons.  If `Theta=sup Re(rho)`, the
explicit formula gives

```text
R_lambda(U)=O_epsilon(exp((Theta+epsilon)U)),              (6.8)
```

because `B_lambda` is a fixed rational multiplier.  Consequently

**Corollary 6.3 (one-sided characterization of the right edge).**

```text
Theta
 =inf {a: for every epsilon>0,
          R_lambda(U)>=-O_epsilon(exp((a+epsilon)U))}

 =inf {a: for every epsilon>0,
          R_lambda(U)<= O_epsilon(exp((a+epsilon)U))}.      (6.9)
```

This is the genuine gain of the signed formulation.  R94's positive
transport required an absolute weighted discrepancy.  Here either one
signed envelope suffices.

For `lambda=2`, the two alternatives are the prime-barycenter inequalities

```text
2 sum_(n<=x)n Lambda(n)-x psi(x)
 >=-C x^(a+1)+x-1,                                       (6.10)
```

or the reverse upper inequality.  They compare the von Mangoldt mass in the
upper and lower portions of `[1,x]` without bounding their absolute
discrepancies separately.

## 7. Why the filtered theorem is still not free

The Volterra filter is invertible after the PNT boundary condition, and the
inverse exposes the remaining global cancellation exactly.  Put

```text
E(U)=exp(-U)D(U),
r_lambda(U)=exp(-U)R_lambda(U).                            (7.1)
```

Equation (5.6) becomes

```text
r_lambda(U)
 =E(U)-integral_0^U lambda exp(-lambda h)E(U-h)dh.         (7.2)
```

Taking an elementary resolvent, or differentiating the exponential
convolution, gives

```text
E(U)=r_lambda(U)+lambda integral_0^U r_lambda(v)dv.        (7.3)
```

The ordinary PNT gives `E(U)->0`; the known subexponential PNT bound makes
`r_lambda` integrable.  Hence

```text
integral_0^infinity r_lambda(v)dv=0,                      (7.4)

E(U)=r_lambda(U)-lambda integral_U^infinity r_lambda(v)dv. (7.5)
```

Thus a two-sided power bound for `R_lambda` is exactly equivalent to the
same power bound for `D`.  The one-sided Landau theorem is the only logical
saving; an absolute estimate simply reconstructs the old PNT remainder.

Iteration does not create a free contraction.  In the normalized variable,
the convolution in (7.2) is a Markov operator `K` with

```text
||I-K||_(infinity->infinity)<=2.                          (7.6)
```

Therefore

```text
||(I-K)^m||<=2^m.                                         (7.7)
```

On a zero mode, the response is

```text
[B_lambda(rho)]^m.                                        (7.8)
```

For `lambda=2`, (5.12) prevents blindness, but

```text
sup_(rho) abs(B_2(rho))=1                                 (7.9)
```

as the zero ordinates tend to infinity.  There is no uniform spectral
cooling factor below one.  If `m=o(U)`, (7.7)--(7.8) change every fixed
mode by only `exp(o(U))` and preserve its horizontal exponent.  If
`m` is proportional to `U`, the coefficient norm in (7.7) is already
exponential.  A bound obtained from total variation pays that full cost.
Taking `m` still larger can erase every fixed zero mode, but then the filter
has erased the evidence and has no controlled inverse.

## 8. Positivity and flat cycles admit off-line countermodels

The one-sided criterion cannot follow from positivity of the prime-like
measure and scale algebra alone.

Fix

```text
0<beta<1,
gamma!=0.                                                 (8.1)
```

Choose a smooth cutoff `chi` which vanishes near zero and equals one for
`U>=2`, and put

```text
D_(beta,gamma)(U)
 =epsilon chi(U)exp(beta U)cos(gamma U).                   (8.2)
```

Define

```text
dM_(beta,gamma)(U)=exp(U)dU+dD_(beta,gamma)(U).            (8.3)
```

For sufficiently small positive `epsilon`, this is a positive measure.  On
the tail,

```text
abs(D_(beta,gamma)'(U))
 <=epsilon sqrt(beta^2+gamma^2)exp(beta U),                (8.4)
```

which is dominated by `exp(U)`; compact positivity is secured by reducing
`epsilon` once more.

The centered measure

```text
nu_(beta,gamma)=M_(beta,gamma)-P=dD_(beta,gamma)           (8.5)
```

obeys every flat cocycle identity in Section 2 and every complex-flow work
identity in Section 3.  Its Laplace transform has genuine poles at

```text
s=beta+i gamma,
s=beta-i gamma.                                           (8.6)
```

Applying the nonlattice filter multiplies their residues by
`B_lambda(beta plus_or_minus i gamma)`, which is nonzero.  Therefore
`R_lambda` has positive and negative excursions of order `exp(beta U)` and
violates both one-sided bounds at every exponent below `beta`.

This countermodel also passes the generic Selberg-size test.  Expanding the
centered Selberg distribution gives

```text
U nu+2(P*nu)+nu*nu.                                       (8.7)
```

The mixed term is `O(exp(U))`, while the other terms are
`O((1+U)exp(beta U))`.  Thus its cumulative remainder has the standard
`O((1+U)exp(U))` scale.  Positivity, the pole main term, flat transport, and
an ordinary Selberg remainder cannot prove (6.2) or (6.3).  The actual
atomic von Mangoldt structure must enter.

## 9. Surviving target and reality check

The most concrete surviving theorem is now one-sided:

**Signed ramp strip target.**  Prove that there are fixed `eta>0` and `C`
such that at least one of

```text
sum_(n<=x)Lambda(n)(2n/x-1)-1+x^(-1)
 >=-C x^(1-eta),                                          (9.1)
```

or

```text
sum_(n<=x)Lambda(n)(2n/x-1)-1+x^(-1)
 <= C x^(1-eta)                                           (9.2)
```

holds for every sufficiently large `x`.  Theorem 6.2 would then give the
fixed zero-free strip `Re(s)>1-eta`.

This target has advantages over the raw PNT error:

* all prime coefficients are bounded by one;
* the coefficient changes sign only at `x/2`;
* the pole continuum cancels exactly;
* only one side must be controlled;
* the multiplier is uniformly nonzero on the zeta divisor.

It remains a major arithmetic estimate.  Dropping either half of the prime
sum, using absolute values, or estimating the two halves independently
returns an `O(x)` bound.  Standard scale cycles add no identity by Theorem
2.1, and positive complex-flow energies return the prefix queue by Theorem
3.1.

A genuinely new transport would need nonzero arithmetic curvature: two
parallel paths must differ because of coefficient-specific factorization or
prime correlations, not merely because they traverse logarithmic scales in
a different order.  In operator language, it needs noncommuting arithmetic
transports.  Plain translations commute and have zero holonomy.

No fixed strip and no proof that zeros approach one is obtained here.  The
new actionable reduction is (9.1)--(9.2): a fixed-power **one-sided** bound
for a bounded signed von Mangoldt ramp is sufficient and, up to endpoint
epsilons, equivalent to the desired strip.
