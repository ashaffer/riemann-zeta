# ZETA23 Mertens quadratic-energy strip gate

Status: an independent fixed-strip criterion is proved.  It uses only the
Lipschitz property of the Mertens function, elementary Hilbert-space
inequalities, and the Mellin formula for `1/zeta`; it does not use the
Pick/prime-null carrier construction.  A power saving in one quadratic
Mertens energy gives an explicit fixed zero-free strip.  The criterion can
be rewritten either as a power-saving averaged two-point Chowla estimate or
as a power-saving mean-square estimate for Mobius sums in short intervals.
This is presented as an elementary synthesis and research gate; no claim of
literature novelty is made.
Known averaged-Chowla and almost-all-short-interval theorems reach the same
ledger only with an `o(1)` (quantitatively, typically logarithmic or
subpower) saving, so they recover qualitative cancellation but no fixed
strip through this route.

Date: 2026-08-12.

**Subsequent strengthening.**  The route through the global quadratic
energy is not the sharp deterministic transfer for short increments.  The
anchored step-Poincare inequality

```text
|M(X)|<=2H+sqrt(X*J(X,H))/H
```

improves the strip width derived from (1.5).  The corrected exponent appears
below and is proved in
[`ZETA23-MERTENS-INCREMENT-POINCARE-AND-ZERO-MODE-GATE-2026-08-12.md`](ZETA23-MERTENS-INCREMENT-POINCARE-AND-ZERO-MODE-GATE-2026-08-12.md).

## 1. Verdict

Put

```text
M(x)=sum_(n<=x) mu(n),
S(X)=sum_(n<=X) |M(n)|^2.                            (1.1)
```

The basic exponent transfer is

```text
S(X) << X^(3-kappa)
       => M(X) << X^(1-kappa/3)
       => zeta(s) != 0 for Re(s)>1-kappa/3.          (1.2)
```

The loss of `3` in (1.2) is exact for the elementary argument: a spike of
height `H` in `M` must persist for length comparable with `H`, so it costs
quadratic energy comparable with `H^3`.

There are two useful sufficient inputs.

First, if

```text
sum_(t<=X) sum_(1<=h<t)
  |sum_(a<=t-h) mu(a)mu(a+h)| << X^(3-eta),          (1.3)
```

then (1.2) holds with `kappa=min(eta,1)`.

Second, define the short-increment energy

```text
J(X,H)=sum_(n<=X-H) |M(n+H)-M(n)|^2
      =sum_(n<=X-H) |sum_(n<k<=n+H) mu(k)|^2.        (1.4)
```

If, for one fixed `0<theta<1` and `eta>0`, with `H` comparable with
`X^theta`,

```text
J(X,H) << X H^(2-eta),                               (1.5)
```

then

```text
M(X)<<X^theta+X^(1-theta*eta/2),

zeta(s) != 0 for
Re(s)>1-min(1-theta,theta*eta/2).                    (1.6)
```

Thus any fixed power saving over the trivial mean square of short Mobius
sums would prove a fixed strip.  The earlier block-energy argument gives the
valid but weaker width `(1/3)min(2-2theta,theta*eta)`.  Merely

```text
J(X,H)=o(XH^2)                                       (1.7)
```

gives only `S(X)=o(X^3)` and `M(X)=o(X)`; the unspecified `o(1)` cannot be
converted into a fixed exponent.  This is the precise obstruction met by
the strongest currently imported almost-all-short-interval results.

No fixed strip, and no failure of every fixed strip, is proved here.  The
new content is the exact independent gate (1.5)--(1.6) and its correlation
and Fourier diagnostics.

## 2. Spike persistence and the cubic transfer

### Theorem 2.1 -- quadratic energy implies a zero-free half-plane

Let `0<kappa<=3`.  If

```text
S(X) << X^(3-kappa),                                 (2.1)
```

then

```text
M(X) << X^(1-kappa/3),                               (2.2)
```

and `zeta(s)` has no zero in

```text
Re(s)>1-kappa/3.                                     (2.3)
```

**Proof.**  Since

```text
|M(n+1)-M(n)|=|mu(n+1)|<=1,                          (2.4)
```

a value `|M(N)|=H` forces

```text
|M(n)|>=H/2
```

at every integer `n` in the last `floor(H/2)` positions before `N`.
Consequently, with an absolute harmless adjustment when `H<2`,

```text
H^3 <= 16 S(N).                                      (2.5)
```

Equations (2.1) and (2.5) give (2.2).  Initially for `Re(s)>1`, partial
summation gives

```text
1/zeta(s)=s int_1^infinity M(x)x^(-s-1) dx.          (2.6)
```

By (2.2), the integral on the right converges and is analytic throughout
`Re(s)>1-kappa/3`; call it `F(s)`.  On `Re(s)>1` one has
`zeta(s)F(s)=1`.  The identity theorem, applied to the meromorphic function
`zeta(s)F(s)` on the connected half-plane (with the pole at `s=1` removed),
therefore gives the same identity throughout its domain.  A zero of zeta
there would make the left side zero, a contradiction.  This proves (2.3).
QED.

The converse scale is also the expected one.  The standard
Perron/reciprocal-zeta implication from a zero-free half-plane
`Re(s)>Theta` gives, for every `epsilon>0`,

```text
M(X) <<_epsilon X^(Theta+epsilon),
S(X) <<_epsilon X^(2Theta+1+epsilon).                (2.7)
```

Thus a fixed power saving in `S(X)` is, at the level of exponents, not an
artificially stronger target than a fixed strip.  The forward implication
in Theorem 2.1 is the only direction used below.

## 3. Exact two-point correlation ledger

For `1<=h<t`, write

```text
C_t(h)=sum_(a<=t-h) mu(a)mu(a+h).                    (3.1)
```

### Proposition 3.1 -- integrated Chowla identity

For every positive integer `X`,

```text
S(X)
 =sum_(a<=X) mu(a)^2 (X-a+1)
  +2 sum_(h=1)^(X-1) sum_(t=h+1)^X C_t(h).           (3.2)
```

**Proof.**  Expanding the square and reversing summation gives

```text
S(X)=sum_(a,b<=X) mu(a)mu(b)(X-max(a,b)+1).          (3.3)
```

The diagonal is the first term of (3.2).  In the half `b=a+h>a`, use

```text
X-b+1=sum_(t=b)^X 1                                 (3.4)
```

and reverse the `a,t` sums.  The other half is equal by symmetry.  QED.

In particular, (1.3) and (3.2) imply

```text
S(X) << X^2+X^(3-eta).                               (3.5)
```

Theorem 2.1 then yields the strip with
`kappa=min(eta,1)`.  Notice the quantifier in (1.3): cancellation must
survive an absolute-value sum over the two-dimensional `(t,h)` triangle,
with a fixed power saving.  Cancellation only after summing in `h` is not
enough for this sufficient criterion.

Matomaki--Radziwill--Tao prove the averaged Chowla estimate

```text
sum_(h_1,...,h_k<=H)
 |sum_(n<=X) lambda(n+h_1)...lambda(n+h_k)|
 =o(H^k X)                                           (3.6)
```

for fixed `k` and every `H=H(X)->infinity`, and their methods extend to
general bounded multiplicative functions.  Their stated quantitative decay
is roughly `(log log H)/(log H)`, rather than `H^(-eta)`.  See
[Matomaki--Radziwill--Tao, *An averaged form of Chowla's conjecture*](https://arxiv.org/abs/1503.05121)
and the [journal version](https://doi.org/10.2140/ant.2015.9.2167).
Conversions of (3.6) into the integrated ledger (3.2) therefore retain a
subpower loss.  They do not supply a fixed `eta` in (1.3).

## 4. Short-interval mean square

### Theorem 4.1 -- deterministic block inequality

For all integers `1<=H<=X`,

```text
S(X) <= 2 X H^2+2 (X/H)^2 J(X,H).                    (4.1)
```

**Proof.**  Partition `1,...,X` into its `H` residue chains.  On the chain
starting at `1<=r<=H`, put

```text
d_(r,j)=M(r+(j+1)H)-M(r+jH).                         (4.2)
```

For `r+kH<=X`, Cauchy--Schwarz gives

```text
|M(r+kH)|^2
 <=2|M(r)|^2+2k sum_(j<k)|d_(r,j)|^2
 <=2H^2+2k sum_(j<k)|d_(r,j)|^2.                    (4.3)
```

Summing the first term over all `X` positions gives `2XH^2`.  Every chain
has at most `X/H` increments.  Reversing the `j,k` sums in the second term
therefore bounds it by

```text
2(X/H)^2 sum_(r,j)|d_(r,j)|^2
 =2(X/H)^2 J(X,H).                                   (4.4)
```

This proves (4.1).  QED.

If `H` is comparable with `X^theta`, (1.5) and (4.1) give

```text
S(X)
 << X^(1+2theta)+X^3 H^(-eta)
 << X^(3-min(2-2theta,theta eta)).                   (4.5)
```

Theorem 2.1 therefore gives the older, valid strip width
`(1/3)min(2-2theta,theta*eta)`.  It is superseded by the following direct
endpoint transfer.

### Theorem 4.2 -- anchored step-Poincare inequality

For `1<=H<=X/2`,

```text
J(X,H)>=(H^2/X)*(|M(X)|-2H)_+^2,                   (4.6)

|M(X)|<=2H+sqrt(X*J(X,H))/H.                       (4.7)
```

For each residue `1<=r<=H`, telescope from `M(r)` along its `H`-step
chain to the last point in `(X-H,X]`.  That endpoint differs from `M(X)`
by at most `H`, while `|M(r)|<=H`.  Cauchy--Schwarz on each chain costs at
most `X/H` increments; summing the `H` disjoint chains proves (4.6).
Equation (4.7) follows.  Under (1.5), it gives exactly (1.6).

The 2016 theorem of Matomaki and Radziwill proves Mobius cancellation in
almost all intervals `[x,x+psi(x)]` for every `psi(x)->infinity`, however
slowly.  In the bounded normalized form, almost-everywhere cancellation
upgrades to a qualitative mean-square statement of the form (1.7), after
the usual dyadic bookkeeping.  See
[Matomaki--Radziwill, *Multiplicative functions in short intervals*](https://annals.math.princeton.edu/2016/183-3/p06).
The later higher-uniformity theorem gives qualitative `o(XH)` average
cancellation, even uniformly over fixed-degree polynomial phases, for
`H>=X^theta` (and polynomial-phase estimates in a wider subpower range); see
[Matomaki--Radziwill--Tao--Teravainen--Ziegler](https://annals.math.princeton.edu/2023/197-2/p03).

A sharper current comparator is Matomaki--Radziwill--Shao--Tao--Teravainen,
[Inventiones Mathematicae 244 (2026), Theorem 1.1(i) and Corollary
1.2(i)](https://doi.org/10.1007/s00222-026-01408-6).  For
`X^(1/3+epsilon)<=H<=X^(1-epsilon)` it gives, for every **fixed** `A>0`, a
bound of size `H/(log X)^A` for the short Mobius sum outside
`O_(A,epsilon)(X/(log X)^A)` starting points.  Squaring on the good set and
using the trivial bound `H` on the exceptional set yields, after renaming
`A`,

```text
J(X,H) <<_(A,epsilon) X*H^2/(log X)^A.              (4.8)
```

This is stronger than a bare qualitative `o(1)`.  But when `H=X^theta` and
`A` is fixed,

```text
(log X)^(-A)=H^(-A log log X/(theta log X))=H^(-o(1)).
```

The cited theorem supplies no uniformity for taking
`A` of order `log X/log log X`, as a fixed `H^(-eta)` saving would require.
It therefore still does not produce a fixed strip through (4.1).

These theorems are much richer structurally than (1.7), but the rate is the
decisive datum for this strip question.  Substituting

```text
J(X,H)<=epsilon(X) XH^2,  epsilon(X)->0,             (4.9)
```

into (4.1) gives only

```text
S(X)<=2XH^2+2epsilon(X)X^3.                         (4.10)
```

For fixed `theta<1`, the second term is `X^(3-o(1))` unless one knows a
fixed power rate for `epsilon(X)`.  No choice of a fixed block exponent
removes this obstruction.

## 5. Fourier localization of the missing estimate

Define

```text
A_X(alpha)=sum_(n=1)^X mu(n)e(n alpha),
B_X(alpha)=sum_(n=1)^X M(n)e(n alpha),
e(u)=exp(2 pi i u).                                  (5.1)
```

Discrete summation by parts gives the exact identity

```text
(1-e(alpha))B_X(alpha)
 =A_X(alpha)-M(X)e((X+1)alpha).                      (5.2)
```

Hence Parseval yields

```text
S(X)=int_0^1
 |A_X(alpha)-M(X)e((X+1)alpha)|^2
 /|1-e(alpha)|^2 d alpha.                            (5.3)
```

The apparent singularity at `alpha=0` is removable because the numerator
vanishes there.  Formula (5.3) identifies `S(X)` as a negative-Sobolev, or
integrated low-frequency, energy of Mobius.

This also isolates the obstruction to importing ordinary Fourier
uniformity.  On every fixed arc separated from `alpha=0`, the denominator
is bounded below and the trivial bounds plus Parseval make its contribution
`O(X^2)`, already a full power below the cubic barrier.  A contribution of
order `X^(3-o(1))` can hide only in an arc shrinking toward the zero
frequency, at the natural resolution around `1/X`.  That central mode is
exactly the Mertens partial sum; estimates uniform over nonzero phases or
minor arcs do not by themselves control it.

Thus higher-order Gowers uniformity, polynomial-phase cancellation, and
large-sieve bounds are not missing a routine summation step.  To prove a
fixed strip through this independent route, one needs a fixed power saving
in the low-frequency norm (5.3), equivalently a fixed-power short-increment
estimate such as (1.5) or an integrated correlation estimate such as
(1.3).

## 6. Research target and pruning rule

The cleanest bounded target exposed by this audit is:

```text
Find fixed theta in (0,1), eta>0 such that

sum_(n<=X-X^theta)
 |sum_(n<k<=n+X^theta) mu(k)|^2
 << X^(1+theta(2-eta)).                              (6.1)
```

It would prove the explicit strip (1.6).  For example, at `theta=1/2`, a
mean-square saving `H^(-eta)` gives width

```text
delta=min(1/2,eta/4).                                (6.2)
```

This target is worth pursuing only if an input has a genuine fixed power
rate.  Results stated as `o(1)`, logarithmic savings, density-one
exceptional-set statements without a power rate, or uniformity away from
the zero Fourier mode cannot close the ledger.  That pruning rule applies
before any further technical elaboration.
