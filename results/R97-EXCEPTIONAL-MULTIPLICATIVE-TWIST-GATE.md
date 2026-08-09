# R97 exceptional multiplicative twists: the pretentiousness--normality gate

Status: the exceptional-character route has a sharp dichotomy.  Every
unimodular completely multiplicative phase occurs in the vertical Bohr
closure of the ordinary Mobius series.  However:

1. no such phase improves the abscissa of uniform vertical convergence;
   exact Kronecker alignment still makes every finite twisted Mobius block
   attain its `l^1` norm;
2. a twist oscillatory enough to give the usual random/Hardy regularization
   destroys the zero at `s=1`;
3. if a twisted reciprocal Euler product really does continue through
   `s=1` with a simple zero there, then the twist is automatically
   **power-pretentious** to the unit character.  Its quotient by `1/zeta`
   is an absolutely and normally convergent, nonvanishing Euler product in
   a fixed half-plane extending left of `1`.

Thus an exceptional twist cannot simultaneously retain the pole-cancelling
zero and supply a genuinely new source of local normality.  Under a
hypothetical fixed zero-free strip, every twist which retains the zero
forces a nonnormal family of return translates by Hurwitz.  This proves a
pretentiousness-versus-normality barrier, not the existence or
nonexistence of a fixed strip.

Date: 2026-08-07.

## 1. Setup

Let `chi:N -> T` be completely multiplicative, with

```text
|chi(n)|=1.
```

For `Re(s)>1`, put

```text
F_chi(s)=sum_n mu(n)chi(n)n^(-s)
        =product_p (1-chi(p)p^(-s)),                       (1.1)

F(s)=F_1(s)=1/zeta(s).                                    (1.2)
```

The desired exceptional phase would have two conflicting properties:

* `F_chi` should retain the removable simple zero of `F` at `1`;
* the oscillation of `chi` should make the twisted series, or the
  corresponding vertical return family, locally normal across `Re(s)=1`.

The sections below show that these two requirements cannot be obtained
from one completely multiplicative phase.

## 2. Every phase is in the vertical Bohr closure

**Proposition 2.1.**  For every unimodular completely multiplicative
`chi`, there are arbitrarily large real `tau_j` such that

```text
p^(-i tau_j) -> chi(p)                 for every prime p,   (2.1)

n^(-i tau_j) -> chi(n)                 for every n.         (2.2)
```

Consequently, on every compact subset of `Re(s)>1`,

```text
F(s+i tau_j) -> F_chi(s).                                  (2.3)
```

### Proof

For any finite set of primes, the numbers `log p` are rationally
independent: an integer relation would contradict unique factorization.
Kronecker's theorem therefore makes the one-parameter flow

```text
tau -> (p^(-i tau))_p
```

dense in the corresponding finite torus.  A diagonal choice gives (2.1),
with arbitrarily large return times.  Complete multiplicativity gives
(2.2).  In `Re(s)>1`, dominated convergence in the absolutely convergent
Dirichlet series gives (2.3).  QED.

Thus allowing exceptional characters genuinely enlarges the set of
possible vertical limits.  The issue is what analytic behavior those
limits can possess at `s=1`.

## 3. Twisting never improves uniform vertical convergence

The exact sign-alignment obstruction of R94 survives every twist.

**Theorem 3.1 (twisted exact alignment).**  For every real `sigma` and
integers `1<=N<M`,

```text
sup_(t in R)
 |sum_(N<n<=M) mu(n)chi(n)n^(-sigma-it)|
 =sum_(N<n<=M) mu(n)^2 n^(-sigma).                         (3.1)
```

The supremum is approached along arbitrarily large values of `|t|`.

### Proof

The right side is the triangle-inequality upper bound.  By Kronecker's
theorem choose arbitrarily large `t` such that, simultaneously for all
primes `p<=M`,

```text
p^(-it) -> -conj(chi(p)).                                  (3.2)
```

For squarefree `n`,

```text
mu(n)chi(n)n^(-it)
 =product_(p|n) [-chi(p)p^(-it)] -> 1.                     (3.3)
```

For nonsquarefree `n` the Mobius coefficient vanishes.  The finite sum
therefore approaches its triangle-inequality upper bound.  QED.

Since squarefree integers have density `6/pi^2`,

```text
sum_(N<n<=2N) mu(n)^2/n -> (6/pi^2)log 2,                  (3.4)
```

and for fixed `sigma<1`,

```text
sum_(N<n<=2N) mu(n)^2 n^(-sigma) asymp_sigma N^(1-sigma). (3.5)
```

It follows that the abscissa of uniform convergence of (1.1), uniformly
in height, is exactly `1` for **every** `chi`.  Coefficient-specific
oscillation does not repair the generic vertical-tail obstruction.

## 4. The finite-scale pretentiousness diagnostic

Define the usual distance from the unit character by

```text
D_chi(x)^2=sum_(p<=x) [1-Re chi(p)]/p.                      (4.1)
```

At `s=1`, the finite twisted Euler product

```text
A_chi,P(1)=product_(p<=P)(1-chi(p)/p)                       (4.2)
```

satisfies the exact logarithmic-scale relation

```text
log |A_chi,P(1)|
 =-sum_(p<=P) Re chi(p)/p+O(1)
 =-log log P+D_chi(P)^2+O(1).                              (4.3)
```

Here the `O(1)` is absolute, because all quadratic and higher logarithmic
terms are bounded by `sum_p O(p^(-2))`, and Mertens' prime theorem gives
`sum_(p<=P)1/p=log log P+O(1)`.

Equivalently,

```text
|A_chi,P(1)| asymp exp(D_chi(P)^2)/log P.                  (4.4)
```

This is only a finite-scale diagnostic; by itself it does not prove an
analytic order of vanishing.  It does show the basic tradeoff:

* bounded `D_chi(P)^2` has the same `1/log P` simple-zero scale as the
  unit character;
* `D_chi(P)^2=log log P+O(1)`, the scale of a Steinhaus-random phase, makes
  the product order one rather than zero;
* more generally, `D_chi(P)^2~alpha log log P` gives size
  `(log P)^(alpha-1)`.

The next theorem upgrades this diagnostic to a rigorous analytic barrier.

## 5. A simple zero forces power-pretentiousness

**Theorem 5.1 (power-pretentiousness theorem).**  Suppose `F_chi`, initially
defined by (1.1), has a holomorphic continuation to a neighborhood of
`s=1` and has a simple zero at `1`.  Then there is an `alpha<1` such that

```text
sum_p [1-Re chi(p)]/p^alpha < infinity.                    (5.1)
```

Consequently, for some `beta<1`, with `beta>1/2`,

```text
sum_p |1-chi(p)|/p^beta < infinity.                        (5.2)
```

### Proof

Both `F_chi` and `F=1/zeta` have a simple zero at `1`, so

```text
G_chi(s)=F_chi(s)/F(s)                                     (5.3)
```

extends holomorphically and is nonzero in a neighborhood of `1`.
Reflection gives the same conclusion for

```text
G_conj(chi)(s)=conj(G_chi(conj(s))).                        (5.4)
```

Choose analytic logarithms near `1`, matched to their Euler-product
branches in `Re(s)>1`, and set

```text
Q_chi(s)=[log G_chi(s)+log G_conj(chi)(s)]/2.               (5.5)
```

For `Re(s)>1`, expanding the two Euler products gives

```text
Q_chi(s)
 =sum_p sum_(k>=1)
   [1-Re(chi(p)^k)]/(k p^(ks)).                            (5.6)
```

This is an ordinary Dirichlet series supported on prime powers, and every
coefficient is nonnegative.  It is holomorphic at the real point `s=1`.
Landau's theorem for Dirichlet series with nonnegative coefficients says
that the real point at the abscissa of convergence is singular.  Since
(5.6) converges for `Re(s)>1` but is regular at `1`, its abscissa of
convergence is strictly less than `1`.  Choose `alpha<1` to the right of
that abscissa.  The `k=1` subseries then gives (5.1).

For completeness, the needed form of Landau's theorem is short.  If
`H(s)=sum_n a_n n^(-s)` with `a_n>=0` were analytic in a disc around its
finite abscissa `sigma_c`, choose a real `s_0>sigma_c` inside that disc.
At `s_0`, termwise differentiation gives

```text
(-1)^m H^(m)(s_0)=sum_n a_n(log n)^m n^(-s_0)>=0.          (5.7)
```

Evaluating the Taylor series a little to the left of `sigma_c`, all terms
have the same sign.  Tonelli's theorem then identifies it with

```text
sum_n a_n n^(-(s_0-delta)),
```

and its finiteness gives convergence to the left of `sigma_c`, a
contradiction.  Hence regularity at `1` forces `sigma_c<1` as claimed.

Finally,

```text
|1-chi(p)|^2=2[1-Re chi(p)].                               (5.8)
```

For any

```text
beta>max(1/2,(1+alpha)/2),                                (5.9)
```

Cauchy--Schwarz gives

```text
sum_p |1-chi(p)|/p^beta
 <=(2 sum_p [1-Re chi(p)]/p^alpha)^(1/2)
   (sum_p 1/p^(2beta-alpha))^(1/2)<infinity.              (5.10)
```

Because `alpha<1`, such a `beta<1` exists.  QED.

The use of Landau's theorem is decisive: mere convergence of the finite
product at the single point `1` would not imply (5.1).  Holomorphic
continuation of a genuine simple zero does.

## 6. The twist is only a normal nonvanishing multiplier

With `beta<1` as in Theorem 5.1, consider

```text
G_chi(s)
 =product_p (1-chi(p)p^(-s))/(1-p^(-s)).                   (6.1)
```

Its logarithm is

```text
log G_chi(s)
 =sum_p sum_(k>=1) [1-chi(p)^k]/(k p^(ks)).                (6.2)
```

The `k=1` terms converge absolutely and normally on closed half-planes to
the right of `beta`, by (5.2).  The terms `k>=2` do so on every closed
half-plane in `Re(s)>1/2`.  Therefore (6.1) is a normally convergent,
holomorphic, nonvanishing Euler product in

```text
Re(s)>beta                                                    (6.3)
```

after increasing `beta` slightly if desired.  It agrees with (5.3) in
`Re(s)>1` and hence by continuation wherever both sides are defined.

This is the main no-go conclusion.  Any twist which genuinely retains the
simple zero factors as

```text
F_chi(s)=G_chi(s)/zeta(s),                                 (6.4)
```

where `G_chi` is already harmless and nonzero in a fixed left
neighborhood of `1`.  Such a twist cannot cancel, regularize, or relocate
the difficult behavior of `1/zeta`; it inherits it unchanged up to a
normal unit.

There is also a useful converse.  If (5.2) holds for some `beta<1`, then
(6.1) is normal and nonzero near `1`, so (6.4) gives `F_chi` a holomorphic
simple zero at `1`.  Thus power-closeness is precisely the stable class of
zero-retaining twists, up to the small exponent loss between (5.1) and
(5.2).

## 7. The finite Euler approximants must be nonnormal

There is an unconditional Hurwitz formulation of the same barrier.

**Proposition 7.1.**  Under the hypothesis of Theorem 5.1, let

```text
A_chi,P(s)=product_(p<=P)(1-chi(p)p^(-s)).                  (7.1)
```

On every sufficiently small disc `D` centered at `1` to which `F_chi`
continues with its isolated simple zero, the family `{A_chi,P}` is not
locally bounded.

### Proof

Choose `D subset {Re(s)>0}`.  Every zero of a factor in (7.1) lies on
`Re(s)=0`, since

```text
1-chi(p)p^(-s)=0  implies  |p^(-s)|=1.                     (7.2)
```

Thus every `A_chi,P` is zero-free on `D`.  If the family were locally
bounded, Montel would give a locally uniformly convergent subsequence.
On the nonempty region `D intersect {Re(s)>1}`, the full sequence already
converges to `F_chi` by absolute Euler-product convergence.  The identity
theorem makes the subsequential limit equal to the continued `F_chi` on
all of `D`.  Hurwitz says a locally uniform limit of zero-free functions
is zero-free or identically zero, contradicting the isolated simple zero
of `F_chi` at `1`.  QED.

So even the specially twisted finite Euler objects necessarily develop a
boundary layer near the retained zero.  The twist does not remove the
mechanism seen in R94--R96.

## 8. Fixed-strip consequence for vertical return families

Now assume, only for this section, a fixed zero-free strip

```text
zeta(s) != 0                       for Re(s)>theta<1.        (8.1)
```

Then `F=1/zeta` is holomorphic there, with its unique zero at `s=1`.
Choose a disc

```text
D={s:|s-1|<r},   0<r<min(1-theta,1),                       (8.2)
```

and let `tau_j` realize `chi` as in Proposition 2.1.  Suppose `F_chi`
continues to `D` with a simple zero at `1`.

**Proposition 8.1.**  The return family

```text
{s -> F(s+i tau_j)}_j                                      (8.3)
```

is not locally bounded on `D`.

### Proof

If it were locally bounded, Montel would give a locally uniformly
convergent subsequence.  In `D intersect {Re(s)>1}`, Proposition 2.1 and
absolute convergence identify its limit as `F_chi`.  The identity theorem
identifies the limit with the continuation of `F_chi` on `D`.

For large `j`, every function `F(s+i tau_j)` is zero-free on `D`.  Indeed,
in the half-plane (8.1), a zero of `1/zeta` can only come from the unique
pole of zeta at `1`, which would occur here at `s=1-i tau_j`, outside `D`.
Hurwitz now contradicts the isolated zero of the limiting `F_chi` at `1`.
QED.

This gives an exact conditional target: proving local boundedness of one
such return family by an independent estimate would disprove every fixed
strip.  Theorems 3.1 and 5.1 explain why a multiplicative twist alone
cannot supply that estimate.

## 9. Why random and hybrid phases do not escape

For independent Steinhaus phases `chi(p)`, the random series

```text
sum_p chi(p)p^(-s)                                          (9.1)
```

converges almost surely, locally in `Re(s)>1/2`; its variance is controlled
by `sum_p p^(-2sigma)`.  The quadratic and higher parts of the logarithm
also converge there.  Hence the random Euler product in (1.1) is almost
surely holomorphic and nonzero in `Re(s)>1/2`.

At the same time,

```text
D_chi(P)^2=log log P+O(1)                 almost surely,   (9.2)
```

because `sum_p Re chi(p)/p` converges almost surely.  Formula (4.4) then
predicts, correctly, a nonzero value rather than a zero at `1`.

A harmonic-density hybrid behaves similarly.  If `chi(p)=1` on a set of
primes carrying proportion `delta` of `sum 1/p`, and is unbiased on the
remainder, then at logarithmic scale

```text
D_chi(P)^2~(1-delta)log log P,
|A_chi,P(1)|=(log P)^(-delta+o(1)).                         (9.3)
```

Any positive harmonic proportion of random primes weakens the zero;
full simple-zero scale requires `delta=1`.  More pathological sparse
hybrids may preserve the pointwise scale, but Theorem 5.1 says that if
they preserve an *analytic simple zero*, their exceptional primes must be
power-sparse and the quotient Euler product is normal.  There is no
analytic middle regime missed by the density heuristic.

## 10. Disposition and surviving target

The proposed exceptional-character construction is killed in its natural
form:

```text
enough phase entropy for new normality
             => no zero at 1;

analytic simple zero at 1
             => power-pretentious phase
             => normal nonzero multiplier of 1/zeta
             => original boundary layer survives.         (10.1)
```

What would still settle the fixed-strip question by this line is no longer
a clever choice of a single completely multiplicative phase.  It would
have to be a genuinely joint estimate proving local boundedness of the
return translates in Proposition 8.1 despite the exact finite-block
alignment in Theorem 3.1.  Equivalently, it must control the cutoff/height
boundary layer rather than encode it into another Euler product.

This round therefore establishes a sharp structural barrier.  It does
**not** prove that a fixed zero-free strip exists, and it does **not** prove
that one cannot exist.
