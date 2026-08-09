# R94 prime--pole phase transport gate

Status: exact cumulative-flux identity, exact finite-cutoff optimal-transport
sandwich for the complex Mellin phase, a capacitated Hall equivalence, an
Euler quasi-infinite-divisibility barrier, and a fixed-height twist
equivalence.  Positive or phase-aware transport does not yet prove a fixed
zero-free strip.  The only surviving version is a genuinely signed global
prime-discrepancy estimate; its fixed-power form is itself equivalent to a
fixed strip.

Date: 2026-08-07.

## 1. Verdict

Write, on the logarithmic half-line,

```text
M = sum_(n>=2) Lambda(n) delta_(log n),
P = exp(u)du,
nu = M-P.                                                   (1.1)
```

The cumulative mismatch is

```text
D(U)=nu([0,U])=psi(exp(U))-(exp(U)-1).                       (1.2)
```

This quantity is the unavoidable queue in every positive transport from
the pole continuum to the prime-power atoms.  The main conclusions are as
follows.

1. After equalizing the two masses at a finite endpoint `U`, ordinary
   logarithmic Wasserstein transport has the exact cost

   ```text
   W_1 = integral_0^U abs(D(v))dv.                           (1.3)
   ```

2. Let `s=sigma+it`, `sigma>0`, and use the genuinely phase-sensitive cost

   ```text
   d_s(u,v)=abs(exp(-su)-exp(-sv)).                          (1.4)
   ```

   If `W_s(U)` is its optimal transport cost, then exactly

   ```text
   sigma integral_0^U exp(-sigma v)abs(D(v))dv
       <= W_s(U)
       <= abs(s) integral_0^U exp(-sigma v)abs(D(v))dv.      (1.5)
   ```

   Thus winding around the Mellin spiral can change a constant depending on
   the height, but cannot change the convergence exponent.  In fact, if
   `Theta=sup Re(rho)` over nontrivial zeta zeros, then for every fixed `t`

   ```text
   Theta
    = inf {sigma>0: sup_U W_(sigma+it)(U)<infinity}.         (1.6)
   ```

   Equation (1.6) is an exact characterization, not a new bound on `Theta`.

3. A power-local capacitated matching between `d psi(x)` and `dx` is already
   a power-saving prime number theorem.  A matching radius
   `O(x^(1-eta))` forces

   ```text
   psi(x)-x=O(x^(1-eta)log x),                              (1.7)
   ```

   and hence a fixed zero-free strip with an arbitrarily small endpoint
   loss.  Conversely a bound without the logarithm constructs such a
   matching by monotone quantiles.  Prime-gap information checks proximity
   of the support, but not the prefix capacity condition in (1.7).

4. For `sigma>1`, the tilted positive R92 carrier has an explicit
   quasi-Levy representation.  Its continuous negative part is

   ```text
   -exp(-(sigma-1)u)du/u.                                  (1.8)
   ```

   At and below `sigma=1` this is not an admissible quasi-Levy measure; the
   positive prime-power part also has infinite total variation there.
   Finite rational corrections do not alter the growing tail.  This closes
   the direct continuation of the Euler quasi-infinite-divisibility
   certificate.  It does not prove that an isolated tilted carrier below
   one cannot possess some unrelated quasi-Levy representation.

5. Twisting by `n^(-it)` does not make a fixed power easier.  For each fixed
   `t`, a power bound for the twisted prime--pole discrepancy is equivalent,
   by two elementary partial summations, to the same power bound for
   `psi(x)-x`.  Exponent-pair estimates in a moving range can control a
   finite prefix, but their fixed-height far tail is exactly the original
   PNT remainder.  A zero at height `t` is demodulated into a nonoscillatory
   `X^beta` term.

The useful survivor is therefore not a positive Wasserstein, Hall, or Levy
certificate.  It is a signed, scale-global bound for the twisted queue,
retaining cancellation across cuts.  No such fixed-power bound is proved
here, and neither alternative in the fixed-strip dichotomy is settled.

## 2. The exact prime--pole flux

For `Re(s)>1`,

```text
integral_[0,infinity) exp(-su)dnu(u)
 =sum_(n>=2) Lambda(n)n^(-s)-integral_0^infinity exp(-(s-1)u)du
 =-zeta'(s)/zeta(s)-1/(s-1).                              (2.1)
```

The pole at `s=1` cancels in (2.1).  At every nontrivial zero, the right
side has the logarithmic-derivative pole with the corresponding
multiplicity.

Stieltjes integration by parts gives the finite-cutoff identity

```text
integral_[0,U] exp(-su)dnu(u)
 =exp(-sU)D(U)+s integral_0^U exp(-su)D(u)du.              (2.2)
```

For `Re(s)>1`, the endpoint term tends to zero and (2.1) is

```text
-zeta'(s)/zeta(s)-1/(s-1)
 =s integral_0^infinity exp(-su)D(u)du.                    (2.3)
```

This is also the one-dimensional flux equation.  If a local flow `J`
transports `P` into `M`, then distributionally

```text
dJ=dnu,
J(U)=D(U)+constant.                                       (2.4)
```

Cycles or complex reroutings do not change the net flux across a cut.  A
positive norm sees `abs(D)`; a signed pairing sees the oscillatory integral
in (2.2).

The finite rational corrections in R93 append densities such as
`exp(-a u)du`, `a>0`, and possibly `du`.  Their cumulative contribution is
`O(1+U)`.  Consequently they change neither a positive exponential growth
exponent nor any of the fixed-power equivalences below.  We suppress them
until Section 7.

## 3. The rightmost zero is the discrepancy exponent

Let

```text
Theta=sup {Re(rho): zeta(rho)=0, 0<Re(rho)<1}.             (3.1)
```

The standard explicit formula and the Mellin identity (2.3) give

**Theorem 3.1 (fixed-power PNT equivalence).**

```text
Theta
 =inf {a: for every epsilon>0,
            D(U)=O_epsilon(exp((a+epsilon)U))}.            (3.2)
```

### Proof

The explicit formula, truncated at height comparable with `x`, gives

```text
psi(x)-x=O_epsilon(x^(Theta+epsilon)).                     (3.3)
```

Logarithmic factors can be absorbed into `x^epsilon`; the harmless `+1` in
(1.2) makes no difference.  This proves the upper implication in (3.2).

Conversely, if `D(U)=O(exp(aU))`, then the right side of (2.3) converges and
is holomorphic for `Re(s)>a`.  It agrees with the logarithmic derivative in
the overlap `Re(s)>1`, so analytic continuation excludes every zeta zero in
`Re(s)>a`.  Applying this with endpoint epsilons proves the reverse
implication.  QED.

An absolute weighted version will be convenient.  Put

```text
I_sigma=limit_(U->infinity)
        integral_0^U exp(-sigma u)abs(D(u))du.             (3.4)
```

The integrals are monotone, so this is simply an improper integral, possibly
infinite.

**Corollary 3.2.**

```text
Theta=inf {sigma>0:I_sigma<infinity}.                      (3.5)
```

Indeed, `sigma>Theta` permits an exponent strictly between `Theta` and
`sigma` in (3.3), proving convergence.  If `I_sigma<infinity`, then

```text
s integral_0^infinity exp(-su)D(u)du                       (3.6)
```

is holomorphic in `Re(s)>sigma` and continues (2.1), so `Theta<=sigma`.
This proof needs no assertion about convergence on the boundary line.

Thus even a weighted *absolute* transport theorem at one fixed exponent
below one would already prove a fixed strip.

## 4. Exact optimal transport for the Mellin spiral

We now give phase-aware transport every finite-cutoff advantage.  Restrict
`M` and `P` to `[0,U]`.  Their masses differ by `D(U)`.  If `D(U)>0`, append
`D(U)delta_U` to `P`; if `D(U)<0`, append `-D(U)delta_U` to `M`.  Denote the
equalized positive measures by `M_U^*` and `P_U^*`.  For every `v<U`, their
cumulative difference is still exactly `D(v)`.

For a metric `d`, let `W_d` denote the Kantorovich transport cost between
these two equal-mass measures.

**Theorem 4.1 (logarithmic transport identity).**

```text
W_(abs(u-v))(M_U^*,P_U^*)
 =integral_0^U abs(D(v))dv.                               (4.1)
```

This is the standard one-dimensional formula for `W_1`: the optimal cost is
the integral of the absolute difference of the cumulative distribution
functions.  Endpoint atoms do not affect the integral.

The phase-sensitive version is almost as exact.

**Theorem 4.2 (Mellin-spiral sandwich).**  Let
`s=sigma+it`, `sigma>0`, and

```text
d_s(u,v)=abs(exp(-su)-exp(-sv)).                           (4.2)
```

Then

```text
sigma integral_0^U exp(-sigma v)abs(D(v))dv
 <=W_(d_s)(M_U^*,P_U^*)
 <=abs(s) integral_0^U exp(-sigma v)abs(D(v))dv.           (4.3)
```

### Proof

The radial projection `z -> abs(z)` is one-Lipschitz.  Therefore

```text
d_s(u,v)>=abs(exp(-sigma u)-exp(-sigma v)).                (4.4)
```

Push both measures forward by `r=exp(-sigma u)`.  Since this map reverses
order, the cumulative discrepancy at `r=exp(-sigma v)` is the negative of
the prefix discrepancy `D(v)`.  The one-dimensional transport formula and
`abs(dr)=sigma exp(-sigma v)dv` give

```text
W_(abs(r-r'))
 =sigma integral_0^U exp(-sigma v)abs(D(v))dv.             (4.5)
```

Contraction under the radial projection proves the lower bound.

For the upper bound, use the arc-length metric on the logarithmic spiral:

```text
ell_s(u,v)
 =integral_(min(u,v))^(max(u,v)) abs(s)exp(-sigma w)dw
 =(abs(s)/sigma)
   abs(exp(-sigma u)-exp(-sigma v)).                       (4.6)
```

Chord length is at most arc length, so `d_s<=ell_s`.  Monotone transport in
the radial coordinate and (4.5) now give

```text
W_(d_s)<=W_(ell_s)
 =abs(s) integral_0^U exp(-sigma v)abs(D(v))dv.            (4.7)
```

QED.

Combining Theorem 4.2 with Corollary 3.2 proves the characterization (1.6).
It also explains why matching equal phases modulo a logarithmic period does
not help asymptotically.  If `h=2pi/abs(t)`, then

```text
exp(-s(u+kh))=exp(-sigma kh)exp(-su),                      (4.8)
```

up to the orientation of `t`.  A same-phase jump through `k` periods still
pays the radial difference

```text
exp(-sigma u)abs(1-exp(-sigma kh)).                        (4.9)
```

Routing it through adjacent periods telescopes to the same radial cost.
High frequency shortens one period, but the number of crossed periods grows
in the inverse proportion.  The prefix queue remains.

There is also no hidden optimization before taking an absolute value.  For
every coupling `Pi` of the equalized marginals,

```text
integral [exp(-su)-exp(-sv)]dPi(u,v)
 =integral exp(-su)dM_U^*(u)-integral exp(-sv)dP_U^*(v).    (4.10)
```

The complex work is determined entirely by the marginals.  Transport cycles
contribute zero.  The standard stable estimate takes the modulus inside,

```text
abs(integral [exp(-su)-exp(-sv)]dPi)
 <=integral d_s(u,v)dPi,                                  (4.11)
```

and optimization gives Theorem 4.2.  If the modulus is not taken inside,
one has simply renamed the signed prime--pole transform; if it is taken
inside, the radial lower bound restores `abs(D)`.

There is a second cutoff cost which must not be hidden.  Equalization added
the boundary reservoir `abs(D(U))delta_U`.  Recovering the original
prime--pole transform introduces the endpoint term

```text
exp(-sU)D(U)                                                (4.12)
```

from (2.2).  Finite rational corrections cannot absorb a power-sized
sequence of such reservoirs.  Working with a small rightward margin and
(3.6) handles the endpoint exactly; dropping it does not.

## 5. Capacitated local matching and Hall prefixes

Return to the ordinary `x` coordinate.  Let

```text
dM_x=sum_(n>=2)Lambda(n)delta_n,
dP_x=dx on [1,infinity).                                  (5.1)
```

The cumulative discrepancy is

```text
M_x([1,x])-P_x([1,x])=psi(x)-(x-1).                       (5.2)
```

**Theorem 5.1 (power-local matching implies a strip).**
Suppose that, outside a compact set, there is a locally finite positive
coupling `Pi` of `M_x` and `P_x` supported on

```text
abs(x-y)<=C max(x,y)^(1-eta),       0<eta<1.               (5.3)
```

Then

```text
psi(x)-x=O(x^(1-eta)log x),                               (5.4)
```

and consequently `Theta<=1-eta` after an arbitrarily small endpoint loss.

### Proof

The net excess in the prefix `[1,x]` must cross the cut at `x`.  Condition
(5.3) forces both endpoints of every crossing edge into a collar

```text
[x-C_1 x^(1-eta),x+C_1 x^(1-eta)]                         (5.5)
```

for all sufficiently large `x`.  The continuum mass of this collar is
`O(x^(1-eta))`.  Since `Lambda(n)<=log n`, its prime-power mass is at most

```text
O(x^(1-eta)log x+log x).                                  (5.6)
```

The absolute net crossing flux is no larger than the total crossing mass.
Equations (5.2), (5.5), and (5.6) prove (5.4).  Theorem 3.1 finishes the
proof.  QED.

There is a converse at the same exponent.

**Theorem 5.2 (power PNT constructs the matching).**  If

```text
psi(x)-(x-1)=O(x^(1-eta)),                                (5.7)
```

then the monotone quantile coupling between `M_x` and `P_x` is supported,
for large coordinates, on

```text
abs(x-y)=O(max(x,y)^(1-eta)+log max(x,y)).                 (5.8)
```

### Proof

Use mass `q>=0` as the common quantile.  The continuum coordinate is
`y=q+1`.  If the prime quantile lies at the atom `n`, then

```text
psi(n-)<q<=psi(n).                                        (5.9)
```

Both endpoints in (5.9) differ from `n-1` by
`O(n^(1-eta)+Lambda(n))`.  Hence

```text
q+1=n+O(n^(1-eta)+log n),                                 (5.10)
```

which is (5.8).  QED.

The relevant Hall condition is therefore not merely that every continuum
point lies near a prime.  For a radius `R`, a capacitated coupling requires,
for every Borel set `A`, inequalities of the form

```text
M_x(A)<=P_x(A^R),
P_x(A)<=M_x(A^R).                                         (5.11)
```

Taking `A` to be a prefix recovers (5.4).  A prime-gap theorem controls the
support distance but says nothing about whether the atoms, with their fixed
capacities `Lambda(n)`, can serve all nearby continuum mass.  The cumulative
queue is precisely the missing capacity datum.  Fractional matching and
optimal positive flow do not evade it.

For scale, the Baker--Harman--Pintz
[*difference between consecutive primes*](https://doi.org/10.1112/plms/83.3.532)
radius `x^(21/40+epsilon)` would correspond to
`eta=19/40-epsilon`.  It does let one attach each continuum location to a
nearby *support point* after capacities are discarded.  A genuine coupling
with the prescribed `Lambda` capacities at that radius would instead imply

```text
psi(x)-x=O_epsilon(x^(21/40+epsilon)),                     (5.12)
```

and a zero-free half-plane essentially as strong as `Re(s)>21/40`.  The
large gap between these statements is exactly the Hall-prefix obstruction,
not a technical loss in the matching algorithm.

## 6. Quasi-infinite divisibility stops at the pole line

Let the positive R92 carrier transform be

```text
H(s)=[(s-1)/(s(s+1))]zeta(s)
    =integral_0^infinity A(exp(u))exp(-su)du, Re(s)>0.      (6.1)
```

For real `sigma>0`, normalize the tilted positive density to a probability
law.  Its characteristic function is

```text
phi_sigma(t)=H(sigma-it)/H(sigma).                         (6.2)
```

For `sigma>1`, the Euler product and Frullani's identity give the exact
quasi-Levy exponent

```text
log phi_sigma(t)
 =integral_0^infinity (exp(itu)-1)d kappa_sigma(u),         (6.3)

d kappa_sigma(u)
 =sum_(p,k>=1) p^(-k sigma)/k delta_(k log p)(du)
  +[-exp(-(sigma-1)u)+exp(-sigma u)+exp(-(sigma+1)u)]du/u. (6.4)
```

Near zero the continuous density in (6.4) is `1/u+O(1)`, which satisfies
the usual `min(1,u^2)` quasi-Levy integrability condition.  At infinity it
has finite total variation when `sigma>1`, and the prime-power sum is also
finite there.  Thus (6.4) is a valid signed Levy certificate in the Euler
half-plane.

At `sigma=1`, however, the first continuous term is `-du/u` at infinity;
for `sigma<1` it grows as

```text
-exp((1-sigma)u)du/u.                                     (6.5)
```

The prime-power total variation

```text
sum_(p,k>=1)p^(-k sigma)/k                                (6.6)
```

also diverges for `sigma<=1`.  Atomic and absolutely continuous parts are
mutually singular, so they cannot cancel in total variation.  Appending
finitely many rational factors adds only finitely many densities
`plus_or_minus exp(-(sigma+a)u)du/u`; these do not cancel (6.5) without
undoing the pole-cancelling factor itself.

This proves a precise no-go statement: the natural Euler/Frullani
quasi-infinite-divisibility certificate has no continuation through
`sigma=1`, even though the positive carrier itself exists for every
`sigma>0`.

One must not strengthen that statement without proof.  For nonlattice laws,
nonvanishing of the characteristic function is not generally equivalent to
quasi-infinite divisibility; see Lindner, Pan, and Sato,
[*On quasi-infinitely divisible distributions*](https://arxiv.org/abs/1701.02400).
An unrelated quasi-Levy representation for one isolated `sigma<1` is not
excluded by (6.5).  But proving such a representation for every
`sigma>sigma_0` would already imply

```text
H(sigma+it)!=0 for all sigma>sigma_0 and all real t,        (6.7)
```

which is the desired zero-free half-plane.  Quasi-infinite divisibility
therefore supplies neither an automatic certificate nor a weaker
intermediate lemma in the present construction.

## 7. Fixed-height twists and the exponent-pair tail

Define the twisted prime--pole cumulative discrepancy

```text
D_t(X)
 =sum_(n<=X)Lambda(n)n^(-it)-integral_1^X x^(-it)dx.       (7.1)
```

Stieltjes partial summation, with

```text
D_0(X)=psi(X)-(X-1),                                      (7.2)
```

gives the exact pair of inverse identities

```text
D_t(X)
 =X^(-it)D_0(X)
  +it integral_1^X D_0(y)y^(-it-1)dy,                    (7.3)

D_0(X)
 =X^(it)D_t(X)
  -it integral_1^X D_t(y)y^(it-1)dy.                     (7.4)
```

**Theorem 7.1 (fixed-height twist equivalence).**  For every fixed real
`t` and every `a>0`,

```text
D_t(X)=O_t(X^a) if and only if D_0(X)=O_t(X^a).             (7.5)
```

The constants in one direction gain at most a factor depending on
`1+abs(t)/a`.  This follows immediately by inserting either bound into
(7.3) or (7.4).

Consequently, a fixed exponent-pair saving

```text
D_t(X)=O_t(X^(1-eta)) for all X                            (7.6)
```

at even one fixed height is already a fixed-power PNT and proves a
zero-free strip.  The oscillation `n^(-it)` cannot make the far-tail
exponent easier.

The resonance can also be seen directly from the explicit formula.  A zero

```text
rho=beta+i gamma                                           (7.7)
```

contributes a mode proportional to `X^rho` to `D_0(X)`.  In
`D_gamma(X)`, multiplication by `x^(-i gamma)` demodulates its derivative,
producing a nonoscillatory term proportional to

```text
X^beta/beta.                                               (7.8)
```

With a smooth compactly supported weight this is a literal Mellin residue,
so a bound with an exponent below `beta` is impossible.  At the target
height, the hoped-for phase cancellation is exactly neutralized by the
target zero.

Standard exponent-pair and Vaughan-identity estimates remain useful when
the height grows with the summation length.  They can give cancellation in
ranges such as `X<=abs(t)^A`, with the precise `A` depending on the estimate.
But for any fixed target height, this covers only the finite logarithmic
prefix

```text
log X<=A log abs(t).                                       (7.9)
```

The tail `X->infinity` is governed by (7.3)--(7.5).  A saving which is only
a negative power of `abs(t)` but leaves the `X` exponent equal to one also
does not help: after multiplication by `X^(-sigma)`, its dyadic tail
diverges for every fixed `sigma<1`.

For comparison, a classical Vinogradov--Korobov PNT estimate has the shape

```text
abs(D(U))
 <<exp(U-c U^(3/5)(log U)^(-1/5))                         (7.10)
```

with an inessential modification at small `U`.  Substitution into Theorem
4.2 gives, for fixed `0<sigma<1`, only the truncated upper certificate

```text
W_(sigma+it)(U)
 <<_(sigma,t) exp((1-sigma)U
                  -c' U^(3/5)(log U)^(-1/5))              (7.11)
```

up to polynomial factors.  Since the negative term in the exponent is
`o(U)`, (7.11) is not uniform in `U` for fixed `sigma<1`.  It reproduces a
moving approach to the pole line, not a fixed strip.  No fixed-power PNT
remainder has been assumed in this audit.  A modern explicit reference for
the same `3/5` shape is Johnston and Yang,
[*Some explicit estimates for the error term in the prime number theorem*](https://arxiv.org/abs/2204.01980).

## 8. The surviving signed estimate

Positive transport replaces the cut flux by `abs(D)` and is characterized
by Theorem 4.2.  The only way still open inside this formulation is to retain
the sign before summing scales.

One exact target is the twisted queue (7.1).  A theorem of the form

```text
there exists eta>0 such that, for one fixed t_0,
D_(t_0)(X)=O_(t_0)(X^(1-eta)) for every X                 (8.1)
```

would, by Theorem 7.1, prove a fixed zero-free strip.  Requiring polynomial
uniformity in `t` would give useful quantitative control of the logarithmic
derivative, but is not needed for the qualitative strip.

In logarithmic flux form, the same target is to bound the signed expression

```text
exp(-sU)D(U)+s integral_0^U exp(-su)D(u)du                (8.2)
```

without replacing `D` by `abs(D)`, uniformly as `U->infinity` in a fixed
right half-plane.  Any successful phase-sensitive flow must estimate (8.2)
through an arithmetic correlation across many cuts.  A positive coupling,
an absolute transport energy, or a Hall feasibility theorem necessarily
returns to (4.3) and cannot see that cancellation.

A potentially useful multiscale formulation is to retain the signed block

```text
B_t(X)=sum_(X<n<=2X)Lambda(n)n^(-it)
       -integral_X^(2X)x^(-it)dx.                          (8.3)
```

The missing theorem is a coherent cancellation of the normalized blocks
over all sufficiently large scales, not merely a good estimate for scales
below a power of the height.  A zero `beta+it` supplies an eigenmode of size
`X^beta` to this scale evolution, so a strict fixed-power contraction would
exclude it.

This target is honest but not cheaper than the fixed-strip problem.  The
value of the transport audit is the sharp pruning:

* phase wrapping is blocked by radial decay;
* positive local matching is blocked by prefix capacity;
* the natural quasi-Levy certificate loses admissibility at `Re(s)=1`;
* exponent-pair cancellation at moving height does not control the fixed
  far tail;
* finite rational corrections affect none of these exponential thresholds.

## 9. Bottom line

The signed prime--pole measure admits a clean transport geometry, but its
global mass discrepancy is not a nuisance term: it is the arithmetic
content of the zero-free-strip problem.  The complex Mellin phase traces a
spiral whose modulus is strictly monotone, and that radial coordinate gives
the lower bound (4.3).  Consequently even optimal phase-aware positive
transport has convergence threshold exactly `Theta`, the supremum of the
real parts of the zeros.

No fixed strip and no sequence of zeros approaching one is proved.  The
remaining avenue within this model is a non-positive, phase-coherent global
estimate for the signed twisted queue.  Local prime proximity, Wasserstein
cost, Hall expansion, ordinary quasi-infinite divisibility, and finite-range
exponent-pair bounds do not supply it.
