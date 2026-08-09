# R137 exceptional high-jet resonance gate

## Status

This report pursues the one survivor left by R133: perhaps the actual
one-parameter prime-log orbit produces exceptionally early large values of the
high Euler jet, even though a Haar-random prime torus predicts none before
Cauchy localization expires.

The main result is a fail-fast theorem for resonance.  It is stronger than a
no-go for coefficient-positive Euler products.  Every resonator whose useful
main term is a Haar/diagonal average, including resonators with signed or
complex coefficients, must concentrate by a factor

```text
exp{exp[(G+o(1))k]},

G=min{2 log((r+1/2)/d), log((r+1)/d)}.                (0.1)
```

For localization into `Re(s)>1-eta`, with `eta<1/2`, this rate is strictly
larger than the Cauchy height rate

```text
L=log(R/d),                 d<R<r+eta.                (0.2)
```

Consequently a finite Haar/diagonal resonator needs more than `T^A` monomials
for every fixed `A`, at every height allowed by Cauchy.  Standard short
resonators, finite long resonators, positive Euler-product resonators, hard
phase cylinders, and soft weighted phase alignment therefore do not prove even
one usable copied jet in this window, much less the polynomially many copies
needed by zero density.

This is not an upper bound for the actual vertical orbit.  A resonator whose
main term comes from exceptional *finite-height off-diagonal arithmetic*, or a
direct theorem that the prime-log orbit visits this Haar-tiny set anomalously
early and often, remains open.  No such result was found in the primary
literature audited below.

```text
exact large-jet threshold from R133                    YES
exact zero-density copy count required                 YES
Soundararajan/Haar-diagonal resonance                  CLOSED
positive Euler-product resonance                       CLOSED
hard and soft natural-scale phase alignment            CLOSED
known quantitative Kronecker guarantees                TOO LATE
known finite-height moment upper bounds                 TOO WEAK
exceptional finite-height off-diagonal resonator        OPEN
fixed zero-free strip                                   NOT PROVED
zeros approaching one                                   NOT PROVED
```

Date: 2026-08-08.

Predecessor: [`R133-HIGH-JET-EULER-RECURRENCE-GATE.md`](R133-HIGH-JET-EULER-RECURRENCE-GATE.md).

## 1. The exact theorem an exceptional-value mechanism must supply

Use the normalization from R133,

```text
D(s)=-zeta'(s)/zeta(s),
J_k(s)=(-1)^k D^(k)(s)/k!
      =sum_(n>=2) Lambda(n)(log n)^k/[k! n^s].         (1.1)
```

Suppose a source zero produces, at

```text
z_*=1+r+i gamma,                    r>0,               (1.2)
```

a nearest-pole distance

```text
d=r+delta_*.                                             (1.3)
```

For a bounded-gap sequence of orders `k`, R133 proves

```text
abs(J_k(z_*))>=c_* d^(-k-1).                            (1.4)
```

Fix a proposed strip width `eta` with

```text
delta_*<eta<13/30,                                      (1.5)
```

and choose

```text
d<R<r+eta.                                              (1.6)
```

The upper endpoint `13/30` is only the range in which the imported
Guth--Maynard density exponent is smaller than one; in particular it is below
`1/2`, which will be decisive below.

The zero-free-disc Cauchy estimate says that a value of size

```text
V_k=c_0 d^(-k-1)=d^(-k+o(k))                            (1.7)
```

at height `t` forces a zero within radius `R`, provided

```text
log t <= c_1 (R/d)^k.
```

At exponential-rate level, the full height ceiling is therefore

```text
log log T <=(L+o(1))k,
L=log(R/d)>0.                                           (1.8)
```

Let

```text
theta_eta=(30/13)eta<1.                                 (1.9)
```

The density argument would close if, for infinitely many useful orders, one
could find a height `T_k` satisfying (1.8) and a set of shifts with

```text
# {1-separated t in [T_k,2T_k]: abs(J_k(1+r+it))>=V_k}
    >=T_k^(theta_eta+epsilon).                         (1.10)
```

Indeed the fixed-radius zero discs have bounded overlap, while

```text
N(1-eta,2T)<=T^(theta_eta+o(1)).                        (1.11)
```

The same conclusion follows from a measurable set of size
`T^(theta_eta+epsilon)`, since a single zero can account for only a bounded
length of centers `t`.

Thus existence of one large value is not the requested replication theorem.
The actual target is the polynomial count (1.10), below the double-exponential
Cauchy ceiling (1.8).

## 2. The prime-torus model of the high jet

Put

```text
a_k(p^v)=(log p)(v log p)^k/[k! p^(v(1+r))].            (2.1)
```

On the infinite prime torus `Omega=product_p S^1`, with Haar probability
`mu`, define

```text
calJ_k(z)=sum_p sum_(v>=1) a_k(p^v) z_p^v.              (2.2)
```

The series is absolutely convergent.  For an arbitrary phase `phi`, write

```text
X_k(z)=Re(e^(-i phi) calJ_k(z))=sum_p X_(p,k)(z_p).     (2.3)
```

The prime blocks are independent and centered.  Define

```text
B_k=max_p ||X_(p,k)||_infinity,
S_k^2=sum_p E_mu X_(p,k)^2.                             (2.4)
```

### Lemma 2.1 -- the two scales of an Euler jet

For fixed `r>0`,

```text
B_k=(r+1)^(-k+o(k)),
S_k=(r+1/2)^(-k+o(k)).                                 (2.5)
```

#### Proof

For one prime,

```text
||X_(p,k)||_infinity
 <=sum_(v>=1) (log p)(v log p)^k
                    exp[-(1+r)v log p]/k!.             (2.6)
```

The saddle in `u=v log p` is `u=k/(1+r)`.  Stirling's
formula, with the sum over `v` contributing only a subexponential factor,
gives the first assertion uniformly in `p`; primes near the saddle give the
matching lower exponential rate.

Orthogonality of the powers of `z_p` gives

```text
S_k^2=(1/2)sum_p sum_(v>=1) a_k(p^v)^2.                (2.7)
```

The `v=1` prime sum has, by the prime number theorem, the same exponential
rate as

```text
1/(k!)^2 int_0^infinity u^(2k+1)exp[-(1+2r)u]du.       (2.8)
```

Stirling gives the `2/(1+2r)=1/(r+1/2)` base in (2.5).
The proper prime powers have a strictly smaller base.  QED.

Relative to the source threshold (1.7), set

```text
H=log((r+1/2)/d),
E=log((r+1)/d),
G=min(2H,E).                                           (2.9)
```

Since `d<R<r+eta` and `eta<1/2`, both `H` and `E` are
positive.

## 3. An entropy lower bound for every Haar resonator

The next theorem is the central gate.  It turns the random-torus rarity noted
in R133 into a lower bound on the concentration of *any* resonance weight.

### Theorem 3.1 -- high-jet resonance entropy

Let `w>=0` satisfy

```text
int_Omega w dmu=1                                      (3.1)
```

and suppose that, after a suitable rotation `phi`,

```text
int_Omega X_k(z)w(z)dmu(z)>=V_k.                       (3.2)
```

Then

```text
Ent_mu(w):=int w log w dmu
 >=c min(V_k^2/S_k^2,V_k/B_k)
 =exp[(G+o(1))k].                                      (3.3)
```

Consequently

```text
||w||_infinity>=exp{exp[(G+o(1))k]}.                   (3.4)
```

#### Proof

The independent centered blocks in (2.3), bounded by `B_k` and with total
variance `S_k^2`, obey the elementary Bernstein moment-generating estimate

```text
log E_mu exp(lambda X_k)
 <=lambda^2 S_k^2/[2(1-lambda B_k/3)]                  (3.5)
```

for `0<=lambda<3/B_k`.  This follows first for finitely many primes from the
power-series bound for each centered bounded variable, and then for (2.3) by
absolute convergence.

The Gibbs variational inequality gives, for every such `lambda`,

```text
Ent_mu(w)
 >=lambda int X_k w dmu-log E_mu exp(lambda X_k).      (3.6)
```

Choose `lambda` of size

```text
min(V_k/S_k^2,1/B_k).                                  (3.7)
```

Equations (3.5)--(3.7) prove the first inequality in (3.3).  Lemma 2.1 and
(1.7) give its exponential rate.  Finally,

```text
Ent_mu(w)<=log ||w||_infinity,                         (3.8)
```

which proves (3.4).  QED.

The associated Haar upper tail is

```text
mu{X_k>=V_k}
 <=exp{-c min(V_k^2/S_k^2,V_k/B_k)}
 <=exp{-exp[(G+o(1))k]}.                               (3.9)
```

The theorem is more useful than (3.9): it says that changing the torus measure
to make the large value typical costs the same entropy, no matter how cleverly
the phases are weighted.

### The strict rate separation

Because `R<r+eta<r+1/2`,

```text
H=log((r+1/2)/d)>log(R/d)=L.                           (3.10)
```

Also `E>L`, since `R<r+1`.  Hence

```text
G=min(2H,E)>L.                                         (3.11)
```

At the Cauchy ceiling, (1.8) and (3.9) imply

```text
T mu{X_k>=V_k}
 <=exp{exp[(L+o(1))k]-exp[(G+o(1))k]}=o(1).            (3.12)
```

Thus even an ideally mixed orbit is predicted to see no target value before
localization expires.

## 4. Soundararajan-style finite resonators

Let

```text
P(z)=sum_(m in M) c_m z^alpha(m)                       (4.1)
```

be any prime-torus polynomial with `M=#M` monomials; the coefficients may be
positive, signed, or complex.  Its normalized resonance density is

```text
w_P=|P|^2/||P||_2^2.                                  (4.2)
```

The peak-to-mean ratio satisfies

```text
K(P)=||P||_infinity^2/||P||_2^2<=M                    (4.3)
```

by Cauchy--Schwarz.  If its Haar/diagonal resonance quotient reaches `V_k`,
Theorem 3.1 gives

```text
log M>=log K(P)>=exp[(G+o(1))k],
M>=exp{exp[(G+o(1))k]}.                               (4.4)
```

But (1.8) and (3.11) imply, for every fixed `A>0`,

```text
M>T^A                                                   (4.5)
```

for all sufficiently large useful `k`.  This rules out the normal resonance
regime `M<=T^kappa`, regardless of the signs of the coefficients and regardless
of how large the integers indexing the monomials are.

For a conventional short Dirichlet-polynomial resonator, one also needs its
length below a fixed power of the averaging length in order to make the
diagonal dominate.  Its number of monomials is then at most a fixed power of
`T`, so (4.5) already rules it out.

This explains why merely importing a more efficient GCD-sum resonator cannot
repair R133.  Such a resonator can greatly improve a subexponential extremal
constant on the critical line, but here the required number of monomials is
super-polynomial in the *entire Cauchy-allowed height*.

## 5. Infinite positive Euler-product resonators

The long positive resonator used for logarithmic derivatives has the model

```text
P(z)=product_p (1-u_p z_p)^(-1),       0<=u_p<1.       (5.1)
```

For finite prime support its exact peak-to-mean ratio is

```text
K(P)=product_p (1+u_p)/(1-u_p).                        (5.2)
```

The diagonal high-jet quotient is

```text
Q_k=sum_p sum_(v>=1) a_k(p^v)u_p^v.                   (5.3)
```

Let

```text
b_(p,k)=sum_(v>=1)a_k(p^v),
max_p b_(p,k)=(r+1)^(-k+o(k)).                         (5.4)
```

If `Q_k>=V_k`, then

```text
V_k<=sum_p u_p b_(p,k),
sum_p u_p>=V_k/max_p b_(p,k)=exp[(E+o(1))k].           (5.5)
```

Therefore

```text
log K(P)
 =sum_p log((1+u_p)/(1-u_p))
 >=2sum_p u_p
 >=exp[(E+o(1))k].                                    (5.6)
```

Since `E>L`, the resonator peak is larger than `T^A` times its mean for every
fixed `A` at the Cauchy ceiling.  The usual long-resonator proof integrates an
even weight centered at zero, uses positivity of its Fourier transform, and
then discards the low-height portion using an upper bound for `|P|^2`.
Equation (5.6) makes that discarded portion larger than the whole available
high-height mass.  The same inequality prevents extraction of the polynomial
measure required in (1.10).

The entropy theorem subsumes (5.6) and also permits signed or complex
coefficients.  The direct calculation is included because it exhibits exactly
where a coefficient-positive Euler product pays: to collect `V_k`, it must
bias at least `exp(Ek)` prime blocks, and the product of those biases costs the
exponential of that number.

## 6. Hard cylinders, soft alignment, and quantitative Kronecker

A hard phase-alignment argument selects an arc for every useful prime phase.
Its inverse Haar volume is the exponential of the number of constrained
coordinates.  A Fejer kernel, von Mises tilt, Euler product, or general
`|P|^2` resonator replaces the hard indicator by a soft weight.
Theorem 3.1 proves that this softening cannot reduce the leading entropy below

```text
exp[(G+o(1))k].                                        (6.1)
```

Thus the distinction between hard and soft alignment is not the surviving
loophole.

Quantitative local Kronecker theorems do give explicit *upper bounds* for the
length of an interval guaranteed to hit a prescribed phase box.  For the
frequencies `log p`, unique factorization supplies rational linear
independence.  The prime-log specialization of Korolev--Rezvyakova gives, for
fixed arc width and primes `p<=N`, a guarantee with

```text
log h <=(3/16+o(1))N^2,                                (6.2)
```

while the sharper Gonek--Montgomery form has essentially

```text
log h <=N log N(1+o(1)).                               (6.3)
```

For a packet with effective entropy dimension `exp[(G+o(1))k]`, the interval
lengths supplied by these theorems have `log log h=(G+o(1))k`, later than the
Cauchy rate `Lk`.  This comparison concerns what the published bounds
*certify*; it is not a lower bound for the true first return.

More importantly, (6.2)--(6.3) are hitting-time *upper* bounds.  They certify a
return by a late scale; they do not prove that the actual prime-log orbit has no
exceptional earlier return.  Linear-form lower bounds are not a substitute:
after eliminating the continuous parameter `t`, their constants deteriorate
with the dimension and prime sizes, and they do not yield a lower hitting-time
bound comparable with (3.9).  The audited primary literature contains no
growing-dimensional discrepancy theorem for

```text
t ->(t log p/(2pi))_p                                  (6.4)
```

which rules out, or supplies in bulk, the exceptional visits required by
(1.10).

## 7. Why known large-value and moment theorems do not fill the gap

There are two very different order ranges in the literature.

* Soundararajan's resonance method and its Bondarenko--Seip refinement create
  large values through weighted Dirichlet-polynomial averages.  Their finite
  resonators have at most `T^kappa` terms, and so fall under (4.5).
* Li--Zhao use a positive infinite Euler-product resonator for `zeta'/zeta`
  near the `1`-line.  That is an order-zero result; its peak-cost ledger is
  compatible at that scale but becomes (5.6) for the orders needed here.
* Yang proves large values of `zeta^(ell)(1+it)` uniformly only for
  `ell<=log_3 T/log_4 T`.  R133 needs

  ```text
  k>=(1/L+o(1))log_2 T,                                (7.1)
  ```

  and concerns derivatives of `-zeta'/zeta`, not derivatives of `zeta`.
  The order gap is therefore asymptotic, not a missing logarithmic factor.

The deterministic second moment for the Euler jet yields only

```text
meas{t<=T:abs(J_k)>=V_k}
 <<T exp[-(2H+o(1))k],                                 (7.2)
```

which still permits `T^(1-o(1))` heights when `k` is a multiple of
`log log T`.  It cannot disprove the exceptional set.

To recover the Haar rarity (3.9) by a `2q`th moment requires

```text
q>=exp[(G+o(1))k].                                     (7.3)
```

An Euler head has length `X=exp(O(k/r))`; diagonal finite-height control of
the `2q`th moment requires roughly

```text
q log X<=log T.                                        (7.4)
```

At the Cauchy ceiling the left side of (7.4) has exponential rate `G`, while
the right side has rate `L<G`.  Hence the moment order needed to prove natural
Haar rarity is unavailable in the same window.  Existing upper bounds neither
produce the copies nor rule out an arithmetically exceptional set of them.

## 8. The precisely delimited survivor

The following routes are now closed at the exponent level:

```text
full phase recurrence                 R133
optimized positive prime head         R133
sparse coefficient-maximizing packet  R133
arbitrary Haar/diagonal resonator      Theorem 3.1
finite signed or complex resonator     (4.4)--(4.5)
positive infinite Euler product        (5.5)--(5.6)
hard or soft natural torus sampling    (3.9), (6.1)
available high moments                 (7.3)--(7.4)
```

What remains is not a conventional improvement of resonance weights.  It is
one of the following genuinely arithmetic theorems.

1. **Exceptional-orbit count.**  For useful `k`, prove (1.10) at some
   `T_k` satisfying (1.8), even though the Haar expected count tends to zero by
   (3.12).
2. **Finite-height off-diagonal resonance.**  Construct a signed/complex
   resonator whose main contribution comes from special relations

   ```text
   abs(log(n/(m p^v)))<=1/T,                            (8.1)
   ```

   rather than the Haar diagonal `n=m p^v`, and control its denominator and
   unweighted output on `[T,2T]`.  Such a construction is not governed by
   Theorem 3.1, but no candidate relation family with the required gain is
   known.

Either theorem would describe a vertical prime-log orbit that is
super-polynomially more concentrated than its Haar model at a dimension growing
like `exp(Gk)`.  This is a concrete and very severe arithmetic requirement.

It is important not to turn the absence of such a theorem into a negative
claim.  The entropy argument proves that Haar-based resonance cannot find the
exceptional values.  It does not prove that the deterministic orbit lacks
them.

## 9. Verdict

No fixed strip and no sequence of zeros approaching one is proved here.  The
exceptional-high-jet idea has, however, been reduced to a much narrower target:

```text
source signal                         V_k=d^(-k+o(k))
Cauchy ceiling                        log T<=exp[(L+o(1))k]
zero-density copy count               T^((30/13)eta+epsilon)
Haar resonator entropy                exp[(G+o(1))k]
resonator peak/mean                    exp{exp[(G+o(1))k]}
geometry                              G>L
finite resonator support required      >T^A for every fixed A
Haar expected useful returns           o(1)
actual exceptional prime-log returns   OPEN
```

The next viable attack must use finite-height arithmetic that is invisible to
the independent-prime torus.  Optimizing a positive packet, changing the soft
phase weight, increasing an ordinary moment, or importing a standard
Soundararajan resonator cannot cross the strict gap `G>L`.

## Primary references

* K. Soundararajan,
  [*Extreme values of zeta and L-functions*](https://arxiv.org/abs/0708.3990),
  for the resonance framework.
* A. Bondarenko and K. Seip,
  [*Large GCD sums and extreme values of the Riemann zeta function*](https://arxiv.org/abs/1507.05840),
  for the finite long-resonator/GCD-sum refinement.
* Z. Li and S. Zhao,
  [*Omega Theorems for Logarithmic Derivatives of Zeta and L-functions Near the 1-line*](https://arxiv.org/abs/2404.17250),
  for a positive Euler-product resonator and a conditional measure extraction
  for the order-zero logarithmic derivative.
* D. Yang,
  [*Extreme values of derivatives of zeta and L-functions*](https://arxiv.org/abs/2204.13826),
  for the proved derivative-order range on the `1`-line.
* S. M. Gonek and H. L. Montgomery,
  [*Kronecker's approximation theorem*](https://doi.org/10.1016/j.indag.2016.01.013),
  for the sharp local quantitative Kronecker framework.
* M. A. Korolev and I. S. Rezvyakova,
  [*On simultaneous approximations to the logarithms of primes*](https://doi.org/10.22405/2226-8383-2022-23-5-87-100),
  for the explicit prime-log specialization.
* L. Guth and J. Maynard,
  [*New large value estimates for Dirichlet polynomials*](https://arxiv.org/abs/2405.20552),
  for the zero-density exponent used in (1.11).
