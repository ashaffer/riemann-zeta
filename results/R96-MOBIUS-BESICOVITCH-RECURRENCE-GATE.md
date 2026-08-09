# R96 Mobius--Besicovitch recurrence and the exceptional-character gate

Status: the strongest square-mean recurrence of the reciprocal-zeta
Dirichlet series is proved in the abstract `B^2`/Bohr model.  It does **not**
copy the simple zero of `1/zeta` at `s=1` to a high translate.  There are two
sharp obstructions.

1. Evaluation at a fixed height, or fixed-window local `L^2` control, is an
   unbounded operation in the Besicovitch norm.  The standard Dirichlet
   `H^2` embedding repairs this only after moving right by `1/2`, which puts
   the entire argument back in `Re(s)>1`.
2. Finite-prime recurrence conditions the Bohr lift at the exceptional unit
   character.  In the resulting conditional Haar/`B^2` ensemble, on every
   real line `1/2<sigma<1`, the full series tends to the *finite Euler
   product*, hence to zero, while natural integer cutoffs tend
   hypothetically to `1/zeta(sigma) != 0`.  The conditionally typical tail
   therefore tends to `-1/zeta(sigma)` and exactly repays the recurring
   finite head.

This identifies the noncommuting limits left open in
`R94-RECIPROCAL-ZETA-VERTICAL-RECURRENCE-GATE.md`.  It neither proves a fixed
zero-free strip nor proves that no fixed strip exists.

Date: 2026-08-07.

## 1. Hypothetical setup and the desired contradiction

Assume, solely for this audit, that

```text
zeta(s) != 0                    for Re(s)>theta<1.            (1.1)
```

Put

```text
F(s)=1/zeta(s),
P_N(s)=sum_(n<=N) mu(n)n^(-s),
R_N(s)=F(s)-P_N(s).                                         (1.2)
```

Give `F(1)` its removable value zero.  Then `F` is holomorphic in the
half-plane in (1.1), has a simple zero at `1`, and has no other zero there.
As established in R94, the fixed-strip hypothesis gives

```text
P_N -> F
```

uniformly on each fixed compact subset of `Re(s)>theta`.  It does not give
uniform convergence after an `N`-dependent vertical translation.

Choose

```text
0<r<min(1-theta,1/2),
D_r={s:|s-1|<r}.                                             (1.3)
```

If one could find `tau_k -> infinity` such that

```text
F(s+i tau_k) -> F(s)              locally uniformly on D_r, (1.4)
```

Hurwitz or Rouche would give a high zero of `F`, hence a second pole of
`zeta`, which is impossible.  The question is whether square-mean
almost-periodicity can supply (1.4).

## 2. The strongest formal `B^2` recurrence really is available

Fix a real

```text
sigma>1/2.                                                   (2.1)
```

The weighted Mobius coefficients are square summable:

```text
sum_n mu(n)^2 n^(-2sigma)
 =product_p(1+p^(-2sigma))
 =zeta(2sigma)/zeta(4sigma)<infinity.                        (2.2)
```

Hence they define a Besicovitch Fourier series

```text
f_sigma(t)=sum_n mu(n)n^(-sigma)n^(-it)                      (2.3)
```

as an element of `B^2`, regardless of pointwise convergence.  Its norm is
given exactly by Parseval:

```text
||f_sigma||_(B^2)^2=sum_n mu(n)^2n^(-2sigma).                (2.4)
```

For a vertical translation,

```text
||f_sigma(.+tau)-f_sigma||_(B^2)^2
 =sum_n mu(n)^2n^(-2sigma)|n^(-i tau)-1|^2.                 (2.5)
```

**Proposition 2.1 (diagonal `B^2` recurrence).**  There are arbitrarily
large `tau_k` such that, for every `sigma>1/2`,

```text
||f_sigma(.+tau_k)-f_sigma||_(B^2) -> 0.                    (2.6)
```

### Proof

By Kronecker recurrence, choose `tau_k>k` so that

```text
|p_j^(-i tau_k)-1|<1/k              (j<=k).                 (2.7)
```

For each fixed integer `n`, unique factorization gives
`n^(-i tau_k)->1`.  The summands in (2.5) are bounded by
`4 mu(n)^2n^(-2sigma)`, which is summable by (2.2).  Dominated convergence
proves (2.6).  QED.

This grants the proposed route its strongest natural mean-square premise.
It still does not imply recurrence at `t=0`, where the zero `F(1)=0` is
anchored.

There is an additional identification issue.  Carlson's classical theorem
identifies a vertical mean with the coefficient norm when a Dirichlet
series converges in a half-plane and is bounded in every smaller
half-plane.  A fixed zero-free strip gives compact-local convergence and
height-dependent bounds for `1/zeta`, not the required vertical
boundedness.  Thus direct invocation of Carlson at the new convergence
boundary is not automatic.  We will grant even this identification below;
the recurrence-to-zero argument still fails.

## 3. Same-line point evaluation is unbounded

The `B^2` seminorm averages over all heights.  It assigns zero cost to a
fixed compact interval after division by the averaging length.  Analyticity
does not change this fact.

For an explicit witness, put

```text
K_N(t)=N^(-1/2) sum_(n<=N)n^(-it).                           (3.1)
```

These are entire Dirichlet polynomials, and orthogonality of the distinct
frequencies `log n` gives

```text
||K_N||_(B^2)=1,              K_N(0)=sqrt(N).                (3.2)
```

Moreover, if `|t|<=1/(3 log N)`, then

```text
Re(n^(-it))>=cos(1/3)                 (n<=N),                (3.3)
```

so

```text
integral_(-1/(3logN))^(1/(3logN)) |K_N(t)|^2 dt
 >=[2 cos(1/3)^2/3] N/log N.                                (3.4)
```

Scaling (3.1) by `sqrt(log N/N)` produces entire Dirichlet polynomials
whose `B^2` norms tend to zero while their local `L^2` mass in a fixed
window stays bounded below.  Scaling by `1/sqrt(N)` gives `B^2` norm
tending to zero while the value at zero remains one.

Therefore no inequality of either form

```text
|g(0)| <= C ||g||_(B^2),

integral_(-h)^h |g(t)|^2dt <= C_h ||g||_(B^2)^2             (3.5)
```

can hold for Dirichlet polynomials.  Subharmonic or Cauchy estimates need a
*local* area or boundary norm first; (2.6) supplies only a global-density
seminorm.

## 4. The sharp half-unit tax in Dirichlet `H^2`

For a square-summable Dirichlet series

```text
g(w)=sum_n a_n n^(-w),          sum_n|a_n|^2<infinity,       (4.1)
```

Cauchy--Schwarz gives

```text
|g(w)|
 <=(sum_n|a_n|^2)^(1/2) zeta(2Re(w))^(1/2).                 (4.2)
```

The right side is finite exactly when `Re(w)>1/2`, and this point-evaluation
threshold is sharp in the Hardy space of Dirichlet series.  Corresponding
fixed-window `L^2` embeddings also occur on the line `Re(w)=1/2`, not on
the coefficient boundary `Re(w)=0`.

Apply this to the difference in (2.5), using a coefficient line `sigma`.
The `H^2` theory can turn `B^2` recurrence into compact or local recurrence
only at

```text
Re(s)>sigma+1/2.                                            (4.3)
```

Since square summability itself requires `sigma>1/2`, (4.3) lies strictly
in

```text
Re(s)>1.                                                     (4.4)
```

That is exactly the half-plane where absolute convergence already gives
ordinary Bohr almost-periodicity.  No circle enclosing `s=1` fits there.

The same loss appears in finite-interval mean-value estimates.  Their
off-diagonal term is controlled by a weight comparable to `n`, leading to

```text
sum_n n |mu(n)n^(-sigma)|^2
 =sum_n mu(n)^2n^(1-2sigma),                                (4.5)
```

which converges only for `sigma>1`.  Thus generic analytic local-`L^2`
machinery cannot upgrade (2.6) in the desired region.

## 5. The Bohr lift exposes the exact conditional tail

The failure is not merely an abstract warning about sparse spikes.  The
coefficient-specific prime structure identifies the term that defeats the
recurrence.

Let `T^infinity` have one coordinate `z_p` for each prime.  If

```text
n=product_p p^(alpha_p(n)),
z^alpha(n)=product_p z_p^(alpha_p(n)),                       (5.1)
```

the Bohr lift of (2.3) is the `L^2` function

```text
mathcal F_sigma(z)
 =sum_n mu(n)n^(-sigma)z^alpha(n)
 =product_p(1-p^(-sigma)z_p).                               (5.2)
```

The product equality holds in `L^2` by (2.2).

Fix a prime cutoff `P` and condition the first coordinates to be the unit
phase.  Write

```text
A_P(s)=product_(p<=P)(1-p^(-s)),
H_P(s,z)=product_(p>P)(1-p^(-s)z_p).                        (5.3)
```

On the exact recurrence slice `z_p=1` for `p<=P`,

```text
mathcal F_s=A_P(s)H_P(s,z).                                 (5.4)
```

For real `sigma>1/2`, independence gives

```text
E H_P(sigma,z)=1,
E |H_P(sigma,z)|^2=product_(p>P)(1+p^(-2sigma)),

E |H_P(sigma,z)-1|^2
 =product_(p>P)(1+p^(-2sigma))-1 ->0.                       (5.5)
```

Hence the uncontrolled high-prime factor tends to one in conditional
`L^2`.  The low-prime Euler factor decides the result.

Now take the left real point of the Rouche disc,

```text
sigma_-=1-r,             theta<sigma_-<1.                    (5.6)
```

Since `sum_p p^(-sigma_-)` diverges,

```text
0<A_P(sigma_-)
 <=exp(-sum_(p<=P)p^(-sigma_-)) ->0.                         (5.7)
```

Equations (5.4)--(5.7) prove the exact conditional collapse

```text
A_P(sigma_-)H_P(sigma_-,z) ->0
                   in L^2 over the high-prime phases.       (5.8)
```

But the fixed-strip premise gives natural-order convergence

```text
S_P(sigma_-):=sum_(n<=P)mu(n)n^(-sigma_-)
 ->F(sigma_-)=1/zeta(sigma_-) !=0.                           (5.9)
```

Subtracting the recurring natural head from the conditional full series
gives

```text
A_P(sigma_-)H_P(sigma_-,z)-S_P(sigma_-)
 ->-F(sigma_-)                  in conditional L^2.          (5.10)
```

Equation (5.10) is the requested signed joint estimate--with the wrong
sign for the proposed contradiction.  On the prime-phase recurrence set,
the growing tail is generically order one and cancels the recurring finite
head.

This conditional claim has a direct finite-dimensional interpretation.
Truncate (5.2) to primes `p<=Q`.  Kronecker equidistribution on the finite
torus says that averaging those vertical phases subject to

```text
|p^(-i tau)-1|<delta                 (p<=P)                  (5.11)
```

converges to Haar measure conditioned on the corresponding low-prime arcs.
One may then let `Q` tend to infinity in `L^2`, and finally let `delta` tend
to zero, obtaining (5.4)--(5.10).  In particular, for every fixed `c>0`,

```text
Prob_high(|A_P(sigma_-)H_P(sigma_-,z)|>=c)
 <=c^(-2) A_P(sigma_-)^2
       product_(p>P)(1+p^(-2sigma_-))
 ->0.                                                        (5.12)
```

Thus a return whose full tail copies the natural value would be an
increasingly exceptional high-prime configuration, not something supplied
by mean square.

At `sigma=1`, both summation procedures tend to zero:

```text
product_(p<=P)(1-1/p)->0,
sum_(n<=P)mu(n)/n->0.                                      (5.13)
```

That agreement at the single zero hides the obstruction.  Every closed
contour enclosing `1` contains points with real part below `1`, where
(5.8) and (5.9) disagree.

For `sigma>1`, by contrast,

```text
A_P(sigma)->product_p(1-p^(-sigma))=F(sigma),                (5.14)
```

which is why ordinary prime-phase recurrence works perfectly in the
absolute-convergence half-plane.

### 5.1 The Euler boundary layer has an explicit local spike

The collapse at the real point does not make the conditioned analytic
family locally bounded.  The same finite Euler factor becomes exponentially
large after an imaginary displacement of order `1/log P`.

Fix `0<a<1/2` and put `sigma=1-a`.  Then, for suitable constants depending
only on `a`,

```text
|A_P(sigma)| <= exp(-c_a P^a/log P),                         (5.15)
```

whereas uniformly for

```text
I_P=[pi/log P, 1.05 pi/log P],                              (5.16)
```

one has

```text
|A_P(sigma+it)| >= exp(c_a P^a/log P)       (t in I_P)      (5.17)
```

once `P` is large.

To prove this, use the uniform expansion

```text
log|1-p^(-sigma-it)|
 =-p^(-sigma)cos(t log p)+O_a(p^(-2sigma)).                 (5.18)
```

The quadratic errors sum to `O_a(1)` because `2sigma>1`.  If
`P^(9/10)<p<=P` and `t` lies in (5.16), then

```text
0.9 pi <= t log p <=1.05 pi,
cos(t log p)<=-1/2.                                         (5.19)
```

By partial summation and the prime number theorem,

```text
sum_(P^(9/10)<p<=P)p^(-sigma) asymp_a P^a/log P,             (5.20)

sum_(p<=P^(9/10))p^(-sigma)
 =O_a(P^(0.9a)/log P).                                      (5.21)
```

The positive contribution from (5.19) therefore dominates every possible
negative low-prime contribution, proving (5.17).  At `t=0`, the elementary
bound `log(1-x)<=-x` and (5.20) prove (5.15).

Take `a=r/2`.  For all large `P`, the segment

```text
{1-a+it:t in I_P}
```

lies inside the disc `D_r`.  Equations (5.16)--(5.17) imply

```text
integral_(I_P)|A_P(1-a+it)|^2dt
 >=(0.05 pi/log P) exp(2c_a P^a/log P)
 ->infinity.                                                (5.22)
```

The high-prime factor does not remove this in conditional mean square:

```text
E_high |A_P(s)H_P(s,z)|^2
 =|A_P(s)|^2 product_(p>P)(1+p^(-2Re(s))).                  (5.23)
```

Thus the natural recurrence-conditioned ensemble has exploding local
`L^2` inside every Rouche disc even while its value at the left real point
collapses to zero.  This is an explicit version of the sparse analytic
spike that the global Besicovitch norm cannot see.

## 6. The exceptional unit character

Conditional expectation of the Bohr lift onto the first prime coordinates
is

```text
E(mathcal F_sigma | z_p, p<=P)
 =product_(p<=P)(1-p^(-sigma)z_p).                           (6.1)
```

These martingales converge to `mathcal F_sigma(z)` for Haar-almost every
`z`.  At the unit character

```text
z=(1,1,1,...),                                               (6.2)
```

their values tend to zero for every `sigma<=1`.  Under (1.1), however, the
natural integer ordering at this same character is assigned the analytic
value `F(sigma)!=0` for `theta<sigma<1`.

There is no contradiction.  An `L^2(T^infinity)` function is defined only
up to a Haar-null set, and the point (6.2), as well as the one-dimensional
Kronecker orbit through it, is Haar-null.  The natural-order boundary value
is extra information not encoded by the `L^2` equivalence class.

This is exactly the setting in which boundary versions of Carlson's theorem
are delicate or false.  Ergodicity controls almost every starting
character for an `L^1` observable, while the reciprocal-zeta argument needs
the exceptional starting character (6.2) and a prescribed return to it.

## 7. The three limits that do not commute

The proposed proof silently interchanges three operations:

```text
N -> infinity       natural integer cutoff,
T -> infinity       vertical Besicovitch/Carlson mean,
P -> infinity       dimension of the prime-phase return.    (7.1)
```

For each fixed `N`, Kronecker recurrence copies `P_N` uniformly on a fixed
disc.  For each fixed translation, the hypothetical strip lets `N` tend to
infinity.  For each fixed `P`, an infinite-height mean equidistributes the
remaining prime phases.  None of these statements is uniform in the other
two parameters.

The exact noncommutation at `sigma_-` is

```text
lim_(N->infinity) sum_(n<=N)mu(n)n^(-sigma_-)
 =F(sigma_-) !=0,                                           (7.2)

lim_(P->infinity)
 sum_(all n whose prime factors are <=P)mu(n)n^(-sigma_-)
 =lim_(P->infinity)A_P(sigma_-)=0.                          (7.3)
```

Both exhaust every integer coefficientwise.  The series is only
conditionally convergent, and finite-prime recurrence selects the smooth
Euler ordering (7.3), not the natural ordering (7.2).

There is a corresponding density obstruction.  Requiring the first
`pi(P)` prime phases to lie in arcs of angular width `delta` defines a Bohr
set of asymptotic density on the scale

```text
delta^(pi(P)).                                               (7.4)
```

An unconditioned square tail on a line `sigma>1/2` decays only polynomially:

```text
sum_(n>P)mu(n)^2n^(-2sigma) asymp_sigma P^(1-2sigma).        (7.5)
```

Markov's inequality applied to (7.5) cannot guarantee one good tail value
inside the exponentially thinner set (7.4).  Equation (5.10) shows that
this is not just weak bookkeeping: the tail is systematically correlated
with the recurrence condition.

Finally, the compact-convergence estimate from R94 has the form

```text
|R_N(s+i tau)|
 <<(1+|tau|) N^(alpha-Re(s)),       theta<alpha<Re(s).       (7.6)
```

Thus a diagonal proof needs the natural cutoff to outrun a positive power
of the return height.  Kronecker recurrence chooses the height only after
the growing prime dimension and requested accuracy are fixed, and supplies
no compatible bound.  Mean-square convergence removes the height from an
average only by allowing precisely the sparse exceptional values needed to
defeat (1.4).

## 8. Why analytic local `L^2` would be decisive--and must fail

Suppose, along a full prime-phase return sequence, one could prove for every
compact `K` in a slightly larger disc

```text
sup_k integral_K |F(s+i tau_k)|^2 dA(s)<infinity.            (8.1)
```

The analytic mean-value inequality would give local boundedness.  Montel,
agreement with `F` on the part of the disc in `Re(s)>1`, and the identity
theorem would then yield (1.4); Hurwitz would give the contradiction.  R94
proved conversely that, under a fixed strip, every full diagonal
prime-phase return sequence must fail such local boundedness.

The `B^2` norm cannot supply (8.1): Sections 3--4 show that it lacks both
same-line point evaluation and same-line fixed-window control.  Any theorem
that did supply (8.1) for these Mobius twists would therefore be genuinely
coefficient-specific and strong enough by itself to disprove (1.1).  It is
not a consequence of Carlson, Besicovitch recurrence, or generic analytic
continuation.

## 9. Literature check

The functional-analytic conclusions above agree with the primary
literature.

1. [Hedenmalm--Lindqvist--Seip, *A Hilbert space of Dirichlet series and
   systems of dilated functions in L2(0,1)* (1997)](https://arxiv.org/abs/math/9512211)
   identifies square-summable Dirichlet series with `H^2` on the
   infinite-dimensional polytorus, characterizes their vertical limits,
   and places compact convergence of those limits in a half-plane shifted
   right by `1/2`.
2. [Saksman--Seip, *Integral means and boundary limits of Dirichlet series*
   (2007)](https://arxiv.org/abs/0712.0492) states Carlson's interior mean
   theorem with its boundedness hypotheses and proves that no general
   Lebesgue boundary version exists, even for bounded Dirichlet-series
   functions.  This directly warns against identifying a polytorus
   `L^2` representative with values on the exceptional unit orbit.
3. [Nakamura, *The generalized strong recurrence for non-zero rational
   parameters* (2010)](https://arxiv.org/abs/1006.1778) records Bagchi's
   theorem that positive-density local-uniform self-recurrence of `zeta` in
   the critical strip is equivalent to RH.  This is consistent with the
   present gate: local-uniform recurrence is far stronger than `B^2`
   recurrence.

No result in these papers converts (2.6) into recurrence at a prescribed
Haar-null character on a contour crossing `Re(s)=1`.

## 10. Exact surviving target

The route would become decisive if one could prove any one of the following
for a diagonal prime-phase return sequence `tau_k`:

```text
F(s+i tau_k)-F(s) ->0          in local area L2 on D_r;      (10.1)

sup_k ||F(.+i tau_k)||_(L2(K))<infinity
                               for every compact K in D_r;   (10.2)

R_(N_k)(s+i tau_k)->0          uniformly on boundary D_r,   (10.3)
```

with `N_k` also large enough that the finite head recurs.  Each condition
would contradict a fixed strip by the R94 normal-family/Rouche theorem.

Generic `B^2` theory supplies none of them.  More sharply, (5.10) says that
the natural candidate for (10.3) has an order-one conditional defect at the
left real point.  A survivor must select an extraordinarily atypical
high-prime phase configuration or prove a new signed small-ball theorem for
the recurrence-conditioned Mobius tail.  Treating the tail by total
mean-square mass loses exactly the correlation that matters.

## 11. Disposition

The attempted chain is now resolved as follows:

```text
fixed strip
 -> compact-local Mobius series convergence                VALID

square-summable coefficients for sigma>1/2
 -> abstract B^2 recurrence                                VALID

B^2 recurrence
 -> recurrence at F(1)=0 or local L2 on a Rouche disc      FALSE

finite-prime recurrence
 -> small shifted Mobius tail                              FALSE GENERICALLY;
                                                            exact defect -F
```

The mechanism is a prime-coordinate boundary layer.  At `s=1` it mimics
the zero of `1/zeta`; immediately to the left it chooses a different
summation order and cancels the naturally convergent value.  The resulting
sparse analytic spikes are invisible to Besicovitch mean square and are
precisely what a hypothetical fixed strip would force.

No fixed-strip/no-fixed-strip conclusion is claimed.
