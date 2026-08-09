# R91 Newton smooth/rough joint gate

Status: the exact normalization, signed Buchstab renewal, fixed-power
truncation, parity-conditioned saddle, complex-resonance obstruction,
orthogonality audit, and growing-arity audit are complete.  They do not prove
a fixed zero-free strip and they do not prove that no fixed strip exists.

The main new conclusion is sharper than the informal survivor left by R90.
Write

```text
X=sqrt(t),                 y=t^kappa=X^theta,
theta=2 kappa in (0,1).                                  (0.1)
```

At the accuracy needed for a strip of width `eta`, the rough cofactor may be
truncated at `b<=X^(1+eta)` with an `O(X^(-1-eta))` error.  It consequently
has at most

```text
(1+eta)/theta                                                (0.2)
```

prime factors.  Thus a fixed-power cutoff does **not** put growing arity on
the rough side.  All unbounded arity remains in the smooth factor.

The smooth factor cannot be estimated independently on a fixed line to the
left of `1`.  If

```text
A_y(s)=product_(p<=y)(1-p^(-s)),                            (0.3)
```

then, for every fixed `eta in (0,1/2)`,

```text
|A_y(1-eta+i pi/log y)|
   >= exp{c_eta y^eta/log y}.                               (0.4)
```

This is a genuine parity resonance, at a frequency tending to zero.  The
gamma weight in the Newton/Riesz Mellin integral is of constant size there.
The complementary rough factor has to cancel (0.4) before absolute values.
In the half-plane of convergence that cancellation is exactly

```text
A_y(s) B_y(s)=1/zeta(s).                                    (0.5)
```

Continuing it to a fixed line on the left is the desired zero-free-strip
problem.  Standard Buchstab, fundamental-lemma, entropy, independent-prime,
and orthogonality estimates either separate the two factors and encounter
(0.4), or retain only logarithmic parity mixing.

There remains one honest promotion gate: prove a uniform pointwise power for
the **complete signed joint form**, including the `b=1` smooth axis and all
bounded rough-factor sectors, without taking an absolute value in either
variable.  No such estimate is proved here.

Date: 2026-08-07.

## 1. Put the target on its natural `X` scale

Set

```text
W(v)=v^(-2) exp(-v^(-2)).                                 (1.1)
```

The Poissonized Newton coefficient from R90 satisfies the exact identity

```text
F(X^2)
 =sum_n mu(n)n^(-2)exp(-X^2/n^2)
 =X^(-2) S_W(X),                                         (1.2)

S_W(X)=sum_n mu(n)W(n/X).                                (1.3)
```

The unsigned normalization is

```text
Z_W(X)=sum_n mu(n)^2 W(n/X)
       ~(6/pi^2)X integral_0^infinity W(v)dv
       =3/pi^(3/2) X,                                    (1.4)
```

because

```text
integral_0^infinity v^(-2)e^(-v^(-2))dv=sqrt(pi)/2.       (1.5)
```

Consequently a fixed strip of width `eta` is promoted by

```text
F(X^2)<<X^(-1-eta),                                      (1.6)
```

or equivalently

```text
S_W(X)<<X^(1-eta).                                       (1.7)
```

Relative to the positive squarefree measure in (1.4), the missing assertion
is a conditional parity bias of size `O(X^(-eta))`.  This is a power, not a
logarithmic saving.

The Mellin transform of `W` is

```text
W_hat(s)=integral_0^infinity W(v)v^(s-1)dv
        =(1/2)Gamma(1-s/2),             Re(s)<2.         (1.8)
```

Thus, initially on `Re(s)>1`,

```text
S_W(X)=(1/(2 pi i)) integral_(c-i infinity)^(c+i infinity)
       (1/2)Gamma(1-s/2) X^s/zeta(s) ds.                 (1.9)
```

This is the same fixed-strip detector as R90, expressed in the endpoint
variable `X` rather than the heat variable `t`.

## 2. Exact smooth/rough factorization and its joint probability meaning

For a threshold `y`, every squarefree `n` has a unique factorization

```text
n=ab,       P^+(a)<=y<P^-(b).                            (2.1)
```

Define

```text
F_<=y(u)=sum_(P^+(a)<=y) mu(a)a^(-2)exp(-u/a^2).         (2.2)
```

Then

```text
F(t)=sum_(P^-(b)>y) mu(b)b^(-2)F_<=y(t/b^2).             (2.3)
```

No approximation and no discarded gcd condition is present: the prime
supports of `a` and `b` are disjoint by construction.

On the `X` scale, (2.3) is

```text
S_W(X)=sum_(P^+(a)<=y<P^-(b))
       mu(a)mu(b) W(ab/X).                               (2.4)
```

Let `Q_(X,y)` be the positive probability measure on these pairs whose mass
is proportional to

```text
mu(a)^2 mu(b)^2 W(ab/X).                                 (2.5)
```

Uniqueness of (2.1) and (1.4) give

```text
E_Q[(-1)^(Omega(a)+Omega(b))]
 =S_W(X)/Z_W(X).                                         (2.6)
```

Therefore the exact microcanonical promotion gate is

```text
|E_Q[(-1)^(Omega(a)+Omega(b))]|<<X^(-eta).               (2.7)
```

It is important that (2.7) is a statement about the joint conditional law.
A bound on either marginal parity, or a covariance bound which does not also
cancel the product of the marginal biases, is insufficient.

### 2.1 Mellin diagonalization

For `Re(z)>0`, the finite smooth sum has

```text
integral_0^infinity F_<=y(u)u^(z-1)du
 =Gamma(z) product_(p<=y)(1-p^(2z-2)).                   (2.8)
```

In the common `s` variable of (1.9), put

```text
A_y(s)=product_(p<=y)(1-p^(-s)),
B_y(s)=product_(p>y)(1-p^(-s)),       Re(s)>1.           (2.9)
```

Then

```text
A_y(s)B_y(s)=1/zeta(s).                                  (2.10)
```

The endpoint kernel couples `a` and `b` in physical space, but every
dilation-invariant transform diagonalizes that coupling and returns (2.10).
This is useful bookkeeping and also a warning: a transform proof must obtain
new control of the product, not merely rediscover its factorization.

## 3. An explicit sufficient joint estimate

There are two convenient precise forms of the surviving estimate.

### Gate J1: conditional parity

For some fixed `theta,eta>0`, with `y=X^theta`, prove (2.7) for every
sufficiently large `X`.  By (1.2), (1.4), and R90 Theorem 2.1, this proves

```text
zeta(s)!=0 for Re(s)>1-eta.                              (3.1)
```

### Gate J2: dyadic signed bilinear form

Let `psi` be a fixed smooth dyadic partition of unity, with an initial block
at `1`, and define

```text
J_(A,B)(X;y)
 =sum_(P^+(a)<=y<P^-(b)) mu(a)mu(b)
   psi(a/A)psi(b/B)W(ab/X).                              (3.2)
```

It is sufficient to prove, for one `theta,eta>0`, uniformly over all blocks
which meet `a,b<=X^(1+2eta)`,

```text
|J_(A,B)(X;X^theta)|
 << X^(1-eta)(log X)^(-3).                               (3.3)
```

There are only `O((log X)^2)` such blocks.  Section 4 shows that the omitted
tails are smaller than the target.  The initial `B=1` block must be included;
discarding it removes the positive-density smooth sector which killed the
R89 local-flow proposal.

Gate J2 is deliberately stronger than necessary, but unlike a bound for the
whole right side written tautologically, it identifies an actionable family
of signed Type-I/II endpoint estimates.  Absolute values may be placed
outside each complete block, but not between the `a` and `b` sums.

## 4. Fixed-power truncation makes the rough arity bounded

The smooth profile is uniformly bounded by

```text
|F_<=y(u)|
 <=sum_(P^+(a)<=y)a^(-2)
 =product_(p<=y)(1+p^(-2))
 <=zeta(2)/zeta(4)=15/pi^2.                              (4.1)
```

It follows directly from (2.3) that

```text
|sum_(b>B, P^-(b)>y) mu(b)b^(-2)F_<=y(X^2/b^2)|
 <<sum_(b>B)b^(-2)<<B^(-1).                              (4.2)
```

The symmetric absolute truncation in `a` has the same bound, since the
positive `b^(-2)` Euler product is bounded.  Hence:

### Lemma 4.1 (fixed-power arity bound)

For a target `F(X^2)=O(X^(-1-eta))`, truncation at

```text
a,b<=X^(1+eta)                                           (4.3)
```

costs only `O(X^(-1-eta))`.  A safe truncation at
`X^(1+2eta)` makes the error strictly smaller than the target.  If
`y=X^theta`, every retained rough cofactor satisfies

```text
Omega(b)<=log b/log y<=(1+2eta)/theta.                   (4.4)
```

In particular, its arity is bounded independently of `X`.

This changes the interpretation of the R90 survivor.  The rough sector can
make long multiplicative jumps, but it cannot carry an unbounded number of
prime bits at a fixed power threshold.  The required growing arity is wholly
inside the smooth factor, or in a global coupling among many distinct
factorizations rather than inside one rough cofactor.

If

```text
R=floor((1+2eta)/theta),                                 (4.5)
```

then (2.3) becomes, up to `O(X^(-1-2eta))`, the finite parity expansion

```text
sum_(0<=j<=R) (-1)^j
 sum_(y<p_1<...<p_j, p_1...p_j<=X^(1+2eta))
 (p_1...p_j)^(-2)
 F_<=y(X^2/(p_1...p_j)^2).                               (4.6)
```

The issue is not convergence of an infinite rough cascade.  It is exact
cancellation among finitely many rough sectors and the internally signed
smooth profile.

## 5. The signed Buchstab renewal and the fundamental-lemma barrier

For a test function `phi`, define the rough dilation operator

```text
(R_y phi)(u)=sum_(P^-(b)>y)mu(b)b^(-2)phi(u/b^2).         (5.1)
```

If `b>1`, write `p=P^-(b)` and `b=pc`.  Then
`P^-(c)>p` and `mu(b)=-mu(c)`.  Therefore the exact signed Buchstab identity
is

```text
R_y phi(u)
 =phi(u)-sum_(p>y)p^(-2) R_(p^+)phi(u/p^2),              (5.2)
```

where `R_(p^+)` restricts every prime factor of `c` to be strictly greater
than `p`.  Equation (2.3) is simply

```text
F=R_y F_<=y.                                             (5.3)
```

Iterating (5.2) through the fixed depth (4.5) gives (4.6).  Taking absolute
values at any level changes the alternating renewal into its positive
counterpart and yields exactly

```text
|F(X^2)|
 <=sum_n mu(n)^2n^(-2)e^(-X^2/n^2)
 ~3/pi^(3/2)X^(-1).                                     (5.4)
```

Thus the unsigned Buchstab renewal closes at the elementary exponent with
the sharp constant.  No slack is hidden in this calculation.

### 5.1 Why the standard fundamental lemma cannot supply the power

In a conventional combinatorial sieve, a level `D` and threshold `y` give
the parameter

```text
u=log D/log y.                                           (5.5)
```

The fundamental-lemma relative remainder has the qualitative best-case
shape

```text
exp{-u log u+O(u)}.                                      (5.6)
```

Constants and the choice of upper or lower sieve do not matter for the
following scale calculation.  With `y=X^theta` and every evaluable divisor
bounded by a fixed power `D<=X^L`, one has

```text
u<=L/theta=O_(L,theta)(1).                               (5.7)
```

The remainder in (5.6) is then only a fixed constant, not `X^(-eta)`.  For
(5.6) to be at most `X^(-eta)`, it is necessary that

```text
u log u >= eta log X,
u >= (eta+o(1))log X/log log X.                          (5.8)
```

But this asks for

```text
D=y^u
 >=exp{(theta eta+o(1))(log X)^2/log log X},             (5.9)
```

far beyond the polynomial endpoint range.  In the actual truncated sum,
(4.4) says more directly that only a fixed number of rough inclusion-
exclusion levels even occur.

The linear-sieve parity barrier is therefore present in its literal scale
form.  Upper/lower or absolute fundamental-lemma estimates cannot resolve
the alternating finite sum (4.6) to a fixed power.

## 6. Dickman/saddle normalization gives only logarithmic parity entropy

The positive and signed smooth Euler partitions at a real exponent `sigma`
are

```text
C_y(sigma)=product_(p<=y)(1+p^(-sigma)),
A_y(sigma)=product_(p<=y)(1-p^(-sigma)).                 (6.1)
```

Under the positive Gibbs measure, the smooth prime bits are independent and

```text
P(p divides a)=p^(-sigma)/(1+p^(-sigma)).                (6.2)
```

Their parity expectation is exactly

```text
A_y(sigma)/C_y(sigma)
 =product_(p<=y)(1-p^(-sigma))/(1+p^(-sigma)).           (6.3)
```

Take the saddle scale

```text
sigma=1+lambda/log y,                                    (6.4)
```

with `lambda` fixed.  Mertens' prime sum gives

```text
sum_(p<=y)p^(-sigma)=log log y+O_lambda(1),               (6.5)
```

while the sum of the squared terms is bounded.  Hence

```text
A_y(sigma)/C_y(sigma)
 asymp_lambda (log y)^(-2).                              (6.6)
```

This agrees with the finite-prime countermodel in R90.  The mean number of
active smooth prime bits is only

```text
E Omega(a)=log log y+O_lambda(1).                         (6.7)
```

Even the ideal Poisson model with mean `m` has parity bias

```text
E[(-1)^N]=e^(-2m).                                       (6.8)
```

Putting `m~log log y` into (6.8) again gives `(log y)^(-2)`, not a power of
`y`.  Canonical independence, entropy, a central limit theorem for
`Omega`, and fixed-strength noise all stop at this logarithmic scale.

Microcanonical conditioning on `ab` near `X` can create additional
cancellation, and the prime number theorem proves that it does.  But that
additional cancellation is not a consequence of the amount of parity
entropy: it comes from oscillation across the endpoint transform.  The next
section identifies the saddle at which a separate smooth estimate loses
that oscillation.

## 7. A low-frequency complex saddle defeats separate smooth estimates

The finite product `A_y(s)` is entire, so it is tempting to shift the smooth
Mellin contour to `Re(s)=1-eta` and bound it there.  The following elementary
calculation kills that approach by absolute values.

### Theorem 7.1 (smooth parity resonance)

Fix `eta in (0,1/2)` and put

```text
sigma=1-eta,             tau_y=pi/log y.                 (7.1)
```

For all sufficiently large `y`,

```text
log |A_y(sigma+i tau_y)|
 >=c_eta y^eta/log y,                                    (7.2)
```

and hence (0.4) holds.

#### Proof

For `p in [y^(2/3),y]`,

```text
tau_y log p in [2pi/3,pi],
cos(tau_y log p)<=-1/2.                                  (7.3)
```

Writing `r=p^(-sigma)`, the Taylor estimate

```text
log|1-r exp(-i tau_y log p)|
 =-r cos(tau_y log p)+O(r^2)                             (7.4)
```

is at least `r/3` for large `p`.  The prime number theorem, at this very
coarse fixed-power scale, gives

```text
sum_(y^(2/3)<=p<=y)p^(-sigma)
 asymp_eta y^(1-sigma)/log y
 =y^eta/log y.                                           (7.5)
```

The primes below `y^(2/3)` can subtract at most
`O(y^(2eta/3)/log y)`, and

```text
sum_p p^(-2sigma)<infinity                               (7.6)
```

because `sigma>1/2`.  Summing (7.4) proves (7.2).  QED.

The resonance has a simple parity interpretation.  For a prime near `y`,

```text
-p^(-i pi/log y) approximately +1.                       (7.7)
```

Thus the endpoint Fourier phase absorbs the Mobius sign of every large
smooth prime.  Conditioning a product to have a given logarithmic size
nearly locks the parity of its large prime factors.  Only the small-prime
bits remain to mix, producing the logarithmic factor in (6.6).

The obstruction is quantitatively severe in the proposed power regime.
With `y=X^theta`, (7.2) reads

```text
|A_y(1-eta+i pi/log y)|
 >=exp{c X^(theta eta)/log X}.                            (7.8)
```

Meanwhile

```text
(1/2)Gamma(1-(sigma+i tau_y)/2)                          (7.9)
```

has size bounded above and below by positive constants.  The gamma kernel
does not suppress the resonance because `tau_y` tends to zero.

The theorem does not say that the smooth endpoint sum is exponentially
large; its Mellin integral contains further cancellation.  It proves the
precise failed inequality:

```text
integral |W_hat(s) A_y(s) X^s| |ds|                     (7.10)
```

cannot be bounded on any fixed line left of `1` by a polynomial target.
Any proof which shifts and takes the modulus of the smooth factor has lost
before it reaches the rough recombination.

In `Re(s)>1`, the rough product cancels the smooth product exactly through
(2.10).  To continue that cancellation to `Re(s)=1-eta`, one needs a
meaningful continuation of `B_y` satisfying

```text
B_y(s)=1/(zeta(s)A_y(s)).                                (7.11)
```

Uniform regularity of the right side is precisely what fails at a zeta
zero.  The complex saddle therefore exposes, rather than resolves, the
fixed-strip-equivalent remainder.

## 8. Orthogonality and random signs: the point evaluation costs the gain

There is an attractive off-wall comparison with independent random prime
phases.  On a dyadic annulus, define the multilinear torus polynomial

```text
H_X((z_p))
 =sum_(X<n<=2X, n squarefree)n^(-2)e^(-X^2/n^2)
   product_(p divides n)z_p.                             (8.1)
```

Haar orthogonality on the full prime torus gives

```text
integral |H_X(z)|^2 dz
 =sum_(X<n<=2X, n squarefree)n^(-4)e^(-2X^2/n^2)
 asymp X^(-3).                                           (8.2)
```

Thus independent random prime signs normally give size `X^(-3/2)`, the
square-root/RH scale.  But Mobius is the single coherent point

```text
z_p=-1 for every p.                                      (8.3)
```

Cauchy--Schwarz evaluation at that point costs the square root of the
`asymp X` effective monomials:

```text
|H_X((-1)_p)|
 <=X^(1/2)(sum_n |coefficient_n|^2)^(1/2)
 <<X^(-1).                                               (8.4)
```

This exactly restores the elementary exponent.  The random-sign comparison
contains no pointwise information at the coherent parity point.

Randomizing the threshold does even less.  When a prime crosses the cutoff,
both

```text
(-1)^Omega(a)   and   (-1)^Omega(b)                      (8.5)
```

flip, so their product is invariant.  The target character lies in the
zero-frequency subspace of the cutoff flow; martingale orthogonality in the
cut position annihilates none of it.

A one-dimensional phase marking only `Omega(n)` groups many integers into
the same Fourier coefficient.  Parseval then retains all cross terms with
equal `Omega`, and the value at phase `pi` is again an uncontrolled boundary
point.  Hypercontractive or influence bounds see only
`Theta(log log X)` active bits and yield powers of `log X`, in agreement
with Section 6.

## 9. Growing-arity couplings do not have enough intrinsic states

Lemma 4.1 leaves only the smooth factor with growing arity.  Under the
canonical endpoint scale, its typical number of prime factors is
`Theta(log log X)`.  Reconfiguring subsets of the primes of a single smooth
integer therefore supplies only

```text
2^Omega(a)=(log X)^(O(1))                                (9.1)
```

candidate states.

A generic covering or entropy argument for a power-local pairing at relative
resolution `X^(-eta)` would need at least `X^eta` candidate states.  Its
necessary mesh-counting inequality is

```text
2^Omega(a)>=X^eta,
Omega(a)>=eta log X/log 2.                               (9.2)
```

This is far outside the Hardy--Ramanujan/Erdos--Kac scale
`Omega(a)~log log X`.  Thus the number of intrinsic subset states cannot by
itself guarantee a fixed-power near-isometry for a typical `a`.  A rare
arithmetic alignment could beat the generic mesh count, so this is an
entropy no-go, not a theorem excluding every specially designed
subset-product involution.  It is the growing-arity analogue of the R89
local-spacing warning, but not as absolute as R89's integer-gap obstruction.

What (9.2) does **not** rule out is a global transport among many different
smooth integers, or a signed flow whose long edges cancel collectively.
Such a construction would no longer be an intrinsic prime-subset coupling;
it would be a pointwise power estimate for the smooth Mobius endpoint
distribution.  Gate J2 is the correct test for it.

## 10. Why an all-orders saddle or renewal remainder meets the strip

The product in the exact endpoint transform is independent of the cutoff:

```text
A_y(s)B_y(s)=1/zeta(s).                                  (10.1)
```

Near `s=1`, `1/zeta(s)` has a zero.  Consequently the logarithmic main terms
from the smooth and rough saddle expansions cancel to all fixed orders.
This explains why the full prime number theorem is much smaller than the
individual `(log X)^(-A)` parity scales.  It does not make the remainder a
fixed power.

### 10.1 An extreme cutoff leaves only the smooth axis and one prime

The bounded-arity statement can be sharpened into a useful two-sector
reduction.  Fix a prospective `eta in (0,1/2)` and choose

```text
1/2+eta<theta<1,             y=X^theta.                  (10.2)
```

Every rough squarefree integer with at least two prime factors is then
larger than

```text
y^2>X^(1+2eta).                                          (10.3)
```

Using (4.2) on all such cofactors gives the lossless-at-the-target identity

```text
F(X^2)
 =F_<=y(X^2)
  -sum_(p>y)p^(-2)F_<=y(X^2/p^2)
  +O(X^(-1-2eta)).                                      (10.4)
```

Thus it is enough to cancel a single prime transform against the full
smooth axis.  This is substantially simpler than an unrestricted
growing-arity cascade, but it does not by itself create a saving.

Indeed, writing

```text
g_(X,y)(v)=v^(-2)F_<=y(X^2/v^2),                         (10.5)
```

the second term is the Stieltjes integral

```text
integral_y^infinity g_(X,y)(v)d pi(v).                   (10.6)
```

Replacing `d pi(v)` by `dv/log v` produces the continuous
Buchstab/Dickman renewal and cancels the logarithmic saddle expansion of the
first term.  The remainder is

```text
integral_y^infinity g_(X,y)(v)d(pi(v)-li(v)).             (10.7)
```

after the corresponding endpoint terms are included.  Absolute partial
summation with the classical prime-number-theorem remainder supplies only a
Vinogradov--Korobov subpower.  A uniform power remainder

```text
pi(v)-li(v)<<v^(1-eta_0)                                 (10.8)
```

would supply the desired kind of bound, but (10.8) is itself a fixed
zero-free-strip theorem.  More generally, an exceptional zero contributes
a coherent power mode to (10.7); the finite smooth multiplier `A_y(rho)` is
not zero and cannot erase it.

The two-sector formula is therefore the cleanest remaining physical-space
laboratory.  A successful argument would have to estimate the **signed
combination** in (10.4) more sharply than it estimates the prime discrepancy
in (10.7).  Standard modulus bounds and ordinary PNT partial summation do
not do so.

Indeed, (1.9) has gamma decay

```text
|Gamma(1-(sigma+i tau)/2)|
 <<_(sigma) (1+|tau|)^C exp(-pi|tau|/4).                 (10.9)
```

To prove an `X^(1-eta)` bound, heights much larger than a constant multiple
of `log X` may be discarded.  But the required contour shift for the
remaining heights is exactly through the rectangle

```text
Re(s)>1-eta,              |Im(s)|<=C_eta log X.          (10.10)
```

As `X` tends to infinity these rectangles exhaust the fixed half-strip.  A
zero `rho=beta+i gamma` contributes a nonzero local residue proportional to

```text
Gamma(1-rho/2) X^rho/zeta'(rho)                          (10.11)
```

in the simple-zero case, with the usual logarithmic polynomial for higher
multiplicity.  The coefficient may be exponentially small in `|gamma|`, but
it is fixed.  If `beta>1-eta`, its power of `X` eventually violates the
desired bound.

Therefore:

* a finite-height saddle expansion cannot prove a uniform power;
* mean-square or almost-all frequency control cannot discard one exceptional
  pole;
* optimizing the classical moving zero-free region gives the known
  Vinogradov--Korobov subpower saving;
* a fixed-power remainder uniform in (10.10) is already a fixed zero-free
  strip theorem.

This is the exact place where the standard Dickman/Buchstab renewal ceases
to be an asymptotic calculation and becomes the original analytic problem.

## 11. Verdict and surviving theorem shape

The signed smooth/rough decomposition has now been pushed through the main
nonclassical possibilities:

```text
X-scale and positive normalization                    EXACT
joint conditional-parity formulation                 EXACT
fixed-power truncation                                O(X^(-1-eta))
rough arity for y=X^theta                             BOUNDED
signed Buchstab renewal                               EXACT
unsigned renewal                                      sharp X^(-1) only
fundamental lemma at polynomial level                 constant error only
canonical/Dickman parity mixing                       (log y)^(-2)
smooth fixed-left-line modulus bound                  KILLED by (7.2)
random-prime orthogonality                            average only
random cutoff martingale                              target invariant
intrinsic smooth subset coupling                      polylog states only
cutoff theta>1/2+eta                                  smooth + one prime
complete joint pointwise power                        OPEN
fixed zero-free strip                                 NOT PROVED
nonexistence of a fixed strip                         NOT PROVED.       (11.1)
```

The remaining possible theorem is concrete.  For one fixed power cutoff
`y=X^theta`, prove Gate J1 or J2 by a mechanism that simultaneously:

1. retains the `b=1` smooth axis;
2. recombines every one of the finitely many rough parity sectors in (4.6);
3. cancels the low-frequency smooth resonance of Theorem 7.1 before taking
   absolute values;
4. is uniform at every Mellin height, not only on average.

Any such estimate with exponent `eta>0` proves
`zeta(s)!=0` for `Re(s)>1-eta`.  Conversely, the existence of a zero in that
half-strip supplies the residue obstruction (10.11), so the requested joint
estimate is not weaker than the goal.

The most promising remaining interpretation is not “more entropy.”  It is a
zeta-specific cancellation of the parity-locked complex saddles across the
finite rough Buchstab sectors.  The exact resonance frequency
`pi/log y` and the bounded sector count in (4.6) give a sharply testable
setting for such a theorem.  No known positivity, sieve, or generic
orthogonality principle supplies it.

## Internal anchors

* [`R90-NEWTON-COEFFICIENT-CANCELLATION-GATE.md`](R90-NEWTON-COEFFICIENT-CANCELLATION-GATE.md),
  for the Newton fixed-strip equivalence, Poissonization, and finite-prime
  countermodels.
* [`R89-MOBIUS-NEAR-ISOMETRIC-FLOW-GATE.md`](R89-MOBIUS-NEAR-ISOMETRIC-FLOW-GATE.md),
  for the positive-density smooth obstruction to bounded-arity local flow.
