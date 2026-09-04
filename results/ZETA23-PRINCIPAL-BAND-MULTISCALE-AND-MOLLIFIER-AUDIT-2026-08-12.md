# Principal-band iteration: multiscale, prime-dilation, and mollifier audit

Status: exact reduction and scoped no-go theorem, 2026-08-12.  No fixed-power
Mertens estimate and no zero-free strip is proved here.  This iteration tests
the remaining principal band against multiplicative large sieves, bilinear
identities, pretentious/entropy inputs, multiscale high-pass energies, and a
long mollifier which retains the principal character.

The main new result is an exact multiscale rigidity theorem.  A fixed-power
bound for even a dilation *difference* of the Mertens function already proves
a fixed zero-free strip.  Moreover, exact Mobius prime-dilation identities
do not remove the dangerous mode: their Euler-factor multiplier cancels and
reconstructs `1/zeta` identically.  In the all-prime limit this is precisely
the previously isolated `mu*Lambda` recompletion.

Thus the nonstandard multiscale route does not currently close the strip,
but it gives a second, sharply formulated target which has no stationary
linear-density mode:

```text
integral_X^(2X) |M(x)-2M(x/2)|^2 dx << X^(2.98).
```

Proving this for all large `X` would exclude zeros with real part greater
than `0.99`.  No audited coefficient-blind, sieve, entropy, or mollifier
input supplies the required `X^(-0.02)` saving.

## 1. The principal-band requirement remains rank one

For

```text
S_n=M(n+H)-M(n),       1<=n<=N=X-H,
J(X,H)=sum_(n<=N)|S_n|^2,
T=sum_(n<=N)S_n,
```

the exact trapezoidal window and ANOVA identity give

```text
|T-HM(X)|<=H^2,
J(X,H)=|T|^2/N+sum_(n<=N)|S_n-T/N|^2,              (1.1)

J(X,H)>=[H^2/(X-H)] (|M(X)|-H)_+^2.                (1.2)
```

At

```text
H=X^(49/50),       eta=1/49,
```

the desired estimate

```text
J(X,H)<<X H^(2-eta)=X^2.94                         (1.3)
```

implies `M(X)<<X^0.99`.  The Fourier complement of

```text
||alpha||<X^0.01/H
```

is already at the scale (1.3) by the coefficient-blind Dirichlet-kernel
bound.  Hence every proposed principal-band argument must control the mean
projection in (1.1), not merely the centered variance.

This has two immediate consequences which are used below.

1. A large sieve after deleting its principal character controls only the
   second term in (1.1).
2. A zero-density or mollified-mean theorem which permits one exceptional
   ordinate cannot prove (1.3): one zero with `beta>0.99` forces violations
   of (1.3) along an unbounded sequence.

## 2. A high-pass Mellin rigidity theorem

Extend `M(x)=sum_(n<=x)mu(n)` by zero for `0<x<1`.  Fix `r>1` and a real
number `a`, and define the dilation difference

```text
F_(r,a)(x)=M(x)-r^a M(x/r).                         (2.1)
```

The choices `a=0` and `a=1` are both useful.  The first has a zero-free
Mellin multiplier throughout `Re(s)>0`; the second is a genuine normalized
high-pass, since it annihilates the model `M(x)=c x`.

### Theorem 2.1 (dyadic high-pass energy already has strip strength)

Let `0<q<1`.  Suppose that, for every sufficiently large `X`,

```text
integral_X^(2X) |F_(r,a)(x)|^2 dx << X^(1+2q).      (2.2)
```

Then `zeta` has no zero `rho` with `Re(rho)>q` at which

```text
1-r^(a-rho) != 0.                                  (2.3)
```

In particular:

- with `a=0`, (2.2) proves `zeta(s)!=0` throughout `Re(s)>q`;
- with `a=1`, (2.2), together with the classical zero-free line
  `Re(s)=1`, excludes every zero in `Re(s)>q`.

#### Proof

For `Re(s)>1`, partial summation gives

```text
integral_1^infinity M(x)x^(-s-1) dx=1/[s zeta(s)]. (2.4)
```

Changing variables in the dilated term gives the exact identity

```text
integral_1^infinity F_(r,a)(x)x^(-s-1) dx
  =[1-r^(a-s)]/[s zeta(s)].                         (2.5)
```

For `sigma=Re(s)>q`, Cauchy--Schwarz and (2.2) bound the contribution of a
dyadic block by

```text
(integral_X^(2X)|F_(r,a)(x)|^2 dx)^(1/2)
(integral_X^(2X)x^(-2sigma-2) dx)^(1/2)
 << X^(q-sigma).                                    (2.6)
```

The dyadic series therefore converges locally uniformly in `Re(s)>q`.
The left side of (2.5) is holomorphic there, so (2.5), initially proved in
`Re(s)>1`, continues there.  A zero of `zeta` satisfying (2.3) would give a
pole on the right, a contradiction.  For `a=0`,
`|r^(-rho)|<1` in `Re(rho)>0`, so (2.3) always holds.  For `a=1`, equality
can occur only on `Re(rho)=1`; the classical theorem handles that line.
QED

For the requested line, the genuinely high-pass target is therefore

```text
integral_X^(2X)|M(x)-2M(x/2)|^2 dx << X^2.98.       (2.7)
```

The trivial scale is `X^3`.  Thus (2.7) asks for exactly a fixed
`X^(-0.02)` energy gain, just like the principal-band target.  It removes a
literal linear-density signal but not a hypothetical `x^rho` zero mode:
the latter is multiplied by `1-2^(1-rho)`, which is nonzero off the line
`Re(rho)=1`.

### 2.2 Exact odd-block form and a local-parity obstruction

Put

```text
O(x)=sum_(n<=x, n odd)mu(n).
```

The local Mobius rule at 2 gives

```text
M(x)=O(x)-O(x/2).                                   (2.8)
```

Consequently the high-pass in (2.7) is exactly

```text
D(x):=M(x)-2M(x/2)
 =O(x)-3O(x/2)+2O(x/4)                              (2.9)

 =sum_(x/2<n<=x, n odd)mu(n)
  -2 sum_(x/4<n<=x/2, n odd)mu(n).                 (2.10)
```

Thus (2.7) asks for decorrelation between two adjacent odd Mobius blocks.
It is natural to hope that the exact sign reversal `mu(2n)=-mu(n)` supplies
this decorrelation.  It does not: that one-prime parity rule is compatible
with full `X^3` energy.

#### Lemma 2.2 (one-prime parity cannot save the high-pass)

For every sufficiently large dyadic `X`, there are coefficients `b(n)`
with `|b(n)|<=1` satisfying

```text
b(2m)=-b(m)  for m odd,       b(n)=0 if 4|n,        (2.11)
```

such that, with `B(x)=sum_(n<=x)b(n)`,

```text
integral_X^(5X/4)|B(x)-2B(x/2)|^2 dx >> X^3.       (2.12)
```

To prove this, choose odd coefficients `c(n)=-1` on `(X/4,X/2]`,
`c(n)=1` on `(X/2,5X/4]`, and zero elsewhere.  Extend them by

```text
b(n)=c(n) if n is odd,
b(2n)=-c(n) if n is odd,
b(n)=0 if 4|n.
```

Then (2.8)--(2.10) hold with `b,c` in place of `mu,O`.  For
`X<=x<=5X/4`, the first block in (2.10) consists entirely of `+1`
coefficients and has sum `x/4+O(1)`.  The second has sum

```text
3x/8-X/2+O(1)<=-X/32+O(1).                         (2.13)
```

It follows that `|B(x)-2B(x/2)|>>X` throughout an interval of length
`X/4`, proving (2.12).

Therefore an additive or multiplicative large sieve which uses coefficient
size, odd support, and the exact prime-2 sign relation but no joint odd-prime
information cannot prove (2.7).  Imposing a fixed finite set of local prime
rules merely replaces the odd base by a positive-density rough base and a
finite dilation filter, as Section 3 makes exact; cancellation on that base
is still an additional input.  Letting the prime set grow while retaining
all its signs leads to the Euler recompletion in Section 3.

The Mellin transform makes the single-zero imprint explicit.  Since

```text
sum_(n odd)mu(n)n^(-s)=1/[(1-2^(-s))zeta(s)],       (2.14)
```

the multiplier of (2.9) is

```text
[1-3*2^(-s)+2*4^(-s)]/[1-2^(-s)]
 =1-2^(1-s),                                        (2.15)
```

and hence

```text
integral_1^infinity D(x)x^(-s-1)dx
 =[1-2^(1-s)]/[s zeta(s)].                          (2.16)
```

If `rho` is a zero with `0<Re(rho)<1`, the numerator in (2.16) cannot
vanish: its second term has modulus `2^(1-Re(rho))>1`.  By the proof of
Theorem 2.1, for every `q<Re(rho)` the dyadic energy bound
`integral_X^(2X)|D(x)|^2dx<<X^(1+2q)` must fail.  One forbidden zero is
therefore visible in this high-pass energy even though the stationary
linear-density mode has been removed.

### General finite filters

For

```text
F_h(x)=sum_(j=1)^k c_j M(x/r_j),
h(s)=sum_(j=1)^k c_j r_j^(-s),                      (2.17)
```

the same proof gives

```text
integral_1^infinity F_h(x)x^(-s-1)dx=h(s)/[s zeta(s)].
                                                               (2.18)
```

An `L^2` power bound for `F_h` excludes every zero not canceled by `h`.
A finite filter therefore has only two possibilities: if its multiplier is
zero-free in the proposed strip, its power bound is already strip-strength;
if it has multiplier zeros, it simply leaves those spectral modes
uncontrolled.  Choosing many scales does not make a coefficient-blind
Poincare estimate into a bound for `M`.

## 3. Exact prime dilation reconstructs the reciprocal zeta function

The preceding theorem does not yet use multiplicativity.  The exact
prime-dilation calculation shows why multiplicativity does not make (2.7)
automatic.

For a finite set of primes `P`, put

```text
G_P(x)=sum_(n<=x, (n, product_(p in P)p)=1) mu(n),
(S_p f)(x)=f(x/p).                                  (3.1)
```

### Theorem 3.1 (finite Euler-factor recompletion)

One has the coefficientwise identity

```text
M(x)=product_(p in P)(I-S_p) G_P(x).                (3.2)
```

For one prime this says simply

```text
M(x)=G_p(x)-G_p(x/p).                               (3.3)
```

Indeed, the first term supplies integers not divisible by `p`; the second
supplies a coefficient `-mu(m)=mu(pm)` at each squarefree multiple `pm`.
Iteration proves (3.2).  Equivalently, in `Re(s)>1`,

```text
sum_((n,P#)=1) mu(n)n^(-s)
 =1/[zeta(s) product_(p in P)(1-p^(-s))],           (3.4)
```

while the dilation filter in (3.2) multiplies by the missing product.  The
result is exactly `1/zeta(s)`, not a better-behaved remainder.

Thus conditioning away finitely many primes leaves the same reciprocal-
zeta poles.  Applying the corresponding high-pass factors restores those
Euler factors and recovers `M` exactly.  Taking absolute values in (3.2)
loses all parity cancellation; keeping the signs returns the original
problem.

There is also an all-prime infinitesimal form.  For `n>1`,

```text
(mu*Lambda)(n)=-mu(n)log n,
(mu*1)(n)=0,                                        (3.5)
```

and hence, for any finitely supported weight `f`,

```text
sum_(n>=2)mu(n)f(n)
 =-sum_(dm>=2)mu(d)(Lambda(m)-1)f(dm)/log(dm).       (3.6)
```

With `f=w`, (3.6) is exactly the signed all-divisor recompletion of the
trapezoidal Mertens carrier.  Therefore the attempted prime-dilation
multiscale route does not bypass the earlier Type-I/II gate; it derives it.

## 4. Why multiplicative and bilinear large sieves stop at the same mode

The multiplicative large sieve has schematic form

```text
sum_(q<=Q) q/phi(q) sum_(chi mod q)^*
 |sum_(n<=X)a_n chi(n)|^2
 <=(X+Q^2)sum_(n<=X)|a_n|^2.                        (4.1)
```

For `a_n=mu(n)`, the `q=1` term is `|M(X)|^2`.  Since
`sum|mu(n)|^2 asymp X`, the best coefficient-blind consequence of (4.1) is
`|M(X)|^2<<X^2`.  It has no `X^(-0.02)` gain.  Removing the principal
character makes the family estimate stronger but deletes exactly the mode
needed in (1.1).

The same obstruction appears after Vaughan-, Heath--Brown-, or Ramaré-type
decomposition.  At additive frequency zero, a rectangular bilinear block
factorizes:

```text
sum_(d in D)sum_(m in M)a_d b_m
 =(sum_(d in D)a_d)(sum_(m in M)b_m).                (4.2)
```

There is no Type-II phase oscillation.  In the bounded phase
`alpha=t/X`, the kernel `exp(2 pi i tdm/X)` is a smooth, finite-rank limit
of separated moments; its constant Taylor mode is (4.2).  Splitting the
`d=1` term from (3.6) asks for a fixed-power PNT error and is already a
strip theorem.  Retaining cancellation across all `d` gives (3.6), namely
the weighted Mertens carrier itself.

This is a scoped no-go statement: a genuinely new joint signed bilinear
estimate could prove the strip.  Standard large-sieve positivity or
blockwise absolute values cannot.

## 5. Long mollifiers which retain `q=1`

Let

```text
P_N(s)=sum_(n<=N)mu(n)n^(-s).                       (5.1)
```

In `Re(s)>1`, multiplication by zeta gives

```text
zeta(s)P_N(s)=sum_(k>=1)a_N(k)k^(-s),
a_N(k)=sum_(d|k, d<=N)mu(d),                        (5.2)
```

where

```text
a_N(1)=1,       a_N(k)=0 for 2<=k<=N.               (5.3)
```

So a long mollifier moves the entire error beyond its length.  It does not
make that error sign-definite.  At any zero `rho`, the analytic function
`zeta(s)P_N(s)-1` has the exact value `-1`, for every `N`.

Consequently, either of the following would directly prove a strip:

```text
sup_(Re(s)>q) |zeta(s)P_N(s)-1|<1                  (5.4)
```

for a suitable height-dependent mollifier, or local uniform convergence
of `P_N` to `1/zeta` in `Re(s)>q`.  A zero makes either assertion
impossible.  Conversely, an `L^2` mollified estimate over ordinates may
bound the number of exceptions, but it cannot exclude a single exceptional
zero unless its final nonnegative budget is less than one.  The `q=1`
signed remainder which must be bounded to reach that threshold is again a
Mertens/reciprocal-zeta remainder.

Thus keeping the principal character signed is necessary, but it does not
lower the theorem's strength.  Averaging it away proves density; bounding
it uniformly proves the desired zero-free region.

## 6. Pretentious distance, entropy decrement, and positivity

Three further templates have sharp exponent-level ceilings.

### 6.1 Pretentious distance

For every real `t`, the Euler-prime distance satisfies

```text
D(mu,n^(it);X)^2
 =sum_(p<=X)(1+cos(t log p))/p
 <=2 log log X+O(1).                                (6.1)
```

Any gain produced only as `exp(-cD^2)` is therefore a power of `log X`,
not `X^(-0.01)` in amplitude.  A fixed-power result must exploit a signed
relation beyond the standard prime-harmonic metric.

### 6.2 Independent prime conditioning and entropy

If local Mobius factors are imposed independently for `p<=z`, their exact
mean is

```text
product_(p<=z)(1-1/p)^2 asymp 1/(log z)^2.          (6.2)
```

Likewise, the density of integers avoiding those primes is of logarithmic
order.  Entropy decrement or Ramaré conditioning which ends with
independent small-prime information therefore gives logarithmic savings.
Iterating the signed prime relations rather than declaring independence
leads to (3.2) and (3.6), where the parity mode remains.  This does not rule
out a new cross-scale entropy theorem; it identifies the needed new input
as a fixed-power *dependence* estimate between prime-dilated sums.

### 6.3 Positivity

The exact correlation kernel for `J` is positive semidefinite, but its top
rank-one direction is (1.1).  Centering deletes that direction rather than
bounding it.  Moreover, replacing Mobius correlations by absolute values
has size

```text
sum_(k,l<=X)|mu(k)mu(l)|W_(X,H)(k,l) >> XH^2,       (6.3)
```

by squarefree density and a blockwise Cauchy--Schwarz argument.  Hence a
positive majorant spends the whole `H^eta` budget.  Positivity can control
the variance after the mean is supplied; it cannot manufacture the signed
mean estimate.

## 7. Zero-detecting feedback

If `zeta` has a zero of real part `beta`, then for every `epsilon>0` there
are arbitrarily large `X` with

```text
|M(X)|>=X^(beta-epsilon).                           (7.1)
```

Otherwise the Mellin integral (2.4) would continue through that zero.
Equation (1.2) then forces, along a sequence,

```text
J(X,H)>=X^(2beta-1-2epsilon)H^2.                    (7.2)
```

Thus one zero, not a positive-density family, defeats the target.  A
zero-density estimate which tends to infinity with height cannot close the
argument by integrality.  A long zero detector must either leave a possible
exception or prove a pointwise principal-character estimate; the latter is
the strip input itself.

The multiscale version says the same thing spectrally.  A putative zero mode
`x^rho` is multiplied in (2.1) by `1-r^(a-rho)`.  Prime dilation does not
destroy it; (3.4) shows that the p-free sum contains the same pole with one
Euler factor removed, and (3.2) puts that factor back.

## 8. Exact verdict and genuinely different inputs

No fixed-power estimate is obtained.  The audited routes end as follows.

```text
centered/additive large sieve       controls variance, deletes rank one;
multiplicative large sieve          q=1 term is M(X), no power gain;
blockwise Type I/II                 d=1 is PNT, all-d sum is Mertens;
pretentious distance                logarithmic prime-harmonic budget;
independent entropy conditioning    logarithmic and hits parity;
positive correlation majorant       full X H^2 scale;
zero-density/mollified mean          may leave one forbidden zero;
finite multiscale filter             Mellin multiplier / zeta;
exact prime-dilation filter          reconstructs 1/zeta identically.
```

The two clean fixed-power targets now available are

```text
(A) J(X,X^(49/50)) << X^2.94,

(B) integral_X^(2X)|M(x)-2M(x/2)|^2 dx << X^2.98.  (8.1)
```

Either proves `zeta(s)!=0` for `Re(s)>0.99`.  Target (B) is structurally
different: it kills the stationary linear-density model before estimation.
Theorem 2.1 proves that it still detects every possible off-line zero.

A genuinely new input would therefore have to be one of:

1. a fixed-power covariance theorem between prime-dilated, p-free Mobius
   sums which retains the alternating signs in (3.2);
2. a nonlinear scale-coupling estimate not reducible to a finite Mellin
   multiplier and not based only on independent prime entropy;
3. a uniform signed long-mollifier remainder below one, including its
   principal-character component; or
4. the original signed all-divisor estimate (3.6).

Each item is honestly strip-strength.  The useful pruning is that no
further effort should be spent on centered large sieves, positive
majorants, or independent prime conditioning as if they could later recover
the missing mean at negligible cost.
