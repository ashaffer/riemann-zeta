# Late Buchstab semiprime dispersion gate

**Date:** 2026-08-13  
**Status:** exact late-band reduction and separated-surrogate power theorem;
short-block selected rough-Voronoi transfer remains open.

## Verdict

The range `p>Y^(1/3)` is algebraically the cleanest part of the post-`q`
SPF tail.  Every composite in the active `p`-rough set is a product of two
primes, so a dyadic transition deletes only balanced semiprimes.  For a
**separated, unweighted** prime-product coefficient, Bazin's 2026
generalized Vaughan estimate gives a genuine fixed-power Bombieri--Vinogradov
surrogate throughout the selected denominator range.  If

```text
p=Y^u,       q=Y^b,       1/3<=u<=1/2,
.1537<=b<=33/133,
```

the global exact-rational modulus-average saving is

```text
delta_sep(u,b)
 =min{b/2,(u-b)/2,(1-3b)/2} >=17/399
 =.04260651629....                                  (0.1)
```

This exceeds the hostile carrier bill
`kappa=.01974048259...` by `.02286603370...`.  Thus ordinary semiprime
dispersion does have enough raw exponent; the old claim that every available
input saves only logarithms would be too pessimistic in this late,
separated surrogate.

It still does **not** prove the rough-Voronoi increment theorem.  There are
two independent defects.

1. Bazin's theorem is a whole-prefix average over moduli.  A curvature block
   has length `H=Y^h`, and Fourier localization to that block needs additive
   twists up to `1/H`.  Bazin's twist term then gives

   ```text
   Y Q^(3/2) H^(-1/2).                               (0.2)
   ```

   At `b=h=33/133`, (0.2) is `Y^(166/133)`, not a
   short-interval saving.  Differencing two global prefixes is also trivial
   on a block.  The common-height selector may reuse a denominator on many
   blocks, whereas the theorem averages each modulus only once and already
   maximizes over its numerator.

2. Globally, the actual coefficient is a joint nearest-survivor matrix, not
   a fixed product `alpha_p beta_r`.  On a block with `H<=r`, however, the
   complete endpoint transport can be anchored at each deleted source `pr`;
   each `r` then occurs with at most one `p`, so the first-return weight is
   absorbed exactly into one sequence `beta_I(r)`.  This does not make
   Bazin local: `beta_I` depends on the block, selected modulus, and
   numerator, while his estimate retains the global parameter `Y`.

The exact late-band semiprime identity, (0.1), and this unique-fiber
separation are proved.  The negative
conclusion is scoped: the **published separated/global estimates do not
imply** the selected short-block weighted theorem.  This is not a no-go
theorem against a new short-interval, gap-aware dispersion argument.

## 1. Exact Buchstab simplification after `Y^(1/3)`

Let `A_z` be the integers in the shell with no prime factor at most `z`,
with the terminal prime endpoints retained as barriers.  If `z>Y^(1/3)`
and `n asyp Y` is composite in `A_z`, then

```text
n=r s,       r,s primes,       z<r<=s.               (1.1)
```

Indeed, three prime factors at least `z` would have product greater than
`Y`.  Consequently

```text
A_z={shell primes} union {r s: z<r<=s primes}.       (1.2)
```

For a dyadic band `P<p<=2P`, `P>Y^(1/3)`, the exact transport from the
companion weighted-rough report is

```text
nu_(2P)-nu_P,                                        (1.3)
```

and its deleted centres are precisely the semiprimes `pr` whose smaller
prime factor lies in `(P,2P]`.  Formula (1.3) is an identity of signed
Voronoi measures, not merely an identity of centre sets.

For a maximal deleted component

```text
l<x_1<...<x_k<r,
```

its twice-normalized coefficient is

```text
(r-x_1)delta_l+(x_k-l)delta_r
 -sum_j (x_(j+1)-x_(j-1))delta_(x_j).                (1.4)
```

Thus even in the semiprime range the negative coefficient at `x_j=p_jr_j`
depends on the adjacent active nodes, and the two positive coefficients
depend on the whole deleted run.

## 2. What Bazin actually proves for a separated surrogate

Bazin's [*A Bombieri--Vinogradov theorem for exponential sums over products
of k primes*](https://arxiv.org/abs/2607.15137), Theorem 8 and Lemma 10,
apply to a rectangular convolution

```text
F(n)=sum_(m n'=n) alpha_m beta_(n'),                 (2.1)
```

with `m asyp M`, `n' asyp N`, `MN asyp Y`, and the stated logarithmic
square-norm bounds.  Prime indicators on dyadic intervals satisfy those
bounds.  With exact additive twist (`lambda=0`), his character-sum quantity
obeys

```text
Xi(F;Y,Q,0)
 <<[Y+Y^(1/2)Q(M+N)^(1/2)+Y^(1/2)Q^2] log^O(1).     (2.2)
```

Suppose the prime factors in (2.1) exceed `2Q`.  Then every supported
integer is a unit for every modulus `q<=2Q`.  Applying Bazin's additive
character expansion (his Lemma 6) on the dyadic moduli `Q<q<=2Q` costs
`Q^(-1/2)` up to divisor logarithms.  It gives

```text
sum_(Q<q<=2Q) max_((a,q)=1)
 |sum_n F(n)e_q(an)-c_q(a)/phi(q) sum_n F(n)|

 <<[YQ^(-1/2)
    +Y^(1/2)Q^(1/2)(M+N)^(1/2)
    +Y^(1/2)Q^(3/2)] log^O(1).                       (2.3)
```

Here `c_q(a)` is the Ramanujan principal term; for reduced `a` it is
independent of the chosen numerator.  In the signed Voronoi increment the
analogous principal mode vanishes because the transported mass is zero,
but (2.3) is asserted only for the separated surrogate.

Put

```text
M=Y^u,       N=Y^(1-u),       Q=Y^b,
1/3<=u<=1/2.
```

The three terms in (2.3) save, relative to `Y`, respectively

```text
b/2,            (u-b)/2,            (1-3b)/2.       (2.4)
```

This proves (0.1).  The minimum over the legal rectangle occurs at
`u=1/3,b=33/133`, where

```text
(u-b)/2=17/399=.04260651629....                      (2.5)
```

Bazin's published Theorem 2 is stated for the full indicator
`1_(Omega(n)=k)` and records a logarithmic-error corollary.  Equations
(2.2)--(2.5) use the stronger explicit estimate actually stated in his
Theorem 8/Lemma 10.  A dyadic late-semiprime centre set is a logarithmic
sum/integral of rectangular prime convolutions after the standard factor-
ordering separation, so the same power ledger applies to its **unweighted
whole-prefix** surrogate.  It does not apply to (1.4).

## 3. The short-block loss is fatal for direct application

Bazin's Lemma 10 allows `|lambda|<=vartheta`, but adds

```text
Y Q^2 vartheta^(1/2)                                 (3.1)
```

to (2.2), hence

```text
Y Q^(3/2) vartheta^(1/2)                             (3.2)
```

to the additive modulus average (2.3).  A smooth cutoff to an interval of
length `H=Y^h` has Fourier support reaching `vartheta asyp H^(-1)`.
The exponent of (3.2) is then

```text
1+(3b-h)/2.                                          (3.3)
```

At the exact top curvature point `b=h=33/133`, this is

```text
1+b=166/133=1.24812030075....                        (3.4)
```

The small-twist hypothesis in Bazin's Theorem 2,
`vartheta<=Q^(-3)log^(-B)`, is precisely the condition preventing (3.2)
from growing; block localization would require `H>=Q^3`, whereas every
retained top-scale denominator has `q asyp H`.

More decisively, making the twist term (3.2) smaller than the actual
unnormalized block target `H Y^(-kappa)` requires

```text
h>=2/3+b+(2/3)kappa.                                 (3.4a)
```

At the most favorable retained denominator `b=.1537`, the right side is
`.833526988...`, above the entire companion range `h<=.5797`.  Thus the
formal whole-`Y` comparison `(h-3b)/2>kappa` is not a local closure anywhere
in the live block range.

Nor does endpoint differencing repair this.  Even the best global exponent
from (2.5) is

```text
Y^(1-17/399)=Y^(382/399)=Y^.95739348... .            (3.5)
```

The desired local carrier scale at the same endpoint is

```text
H Y^(-kappa)=Y^(.22837981816...).                    (3.6)
```

Thus the direct prefix-difference deficit is `.72901366555...` in the
`Y` exponent.

There is also a selector quantifier mismatch.  At the top aperture there
are

```text
K=Y/H=Y^(100/133+o(1))                               (3.7)
```

blocks but only `O(H)=Y^(33/133+o(1))` possible denominator values.  Some
denominator is reused at least `Y^(67/133+o(1))` times on average under any
assignment.  Bazin averages a modulus once and already takes the maximum
over primitive numerators; it gives no bound for this repeated collection
of disjoint, independently weighted blocks.

## 4. First-return anchoring and the unique-large-factor separation

For a deleted semiprime `x=pr`, its neighboring-gap coefficient is globally
a joint function of `(p,r)`.  Nevertheless the positive endpoint transport
can be anchored at the deleted sources exactly.  Evaluating (1.4) at
`f(n)=e_q(an)`, one component contributes

```text
sum_(j=1)^k e_q(a x_j) W_(q,a)(x_j),                 (4.1)
```

where every `W(x_j)` contains
`-(x_(j+1)-x_(j-1))/2`, `W(x_1)` also contains

```text
(r-x_1)/2 e_q(a(l-x_1)),
```

and `W(x_k)` also contains

```text
(x_k-l)/2 e_q(a(r-x_k)).                             (4.2)
```

For `k=1` both endpoint terms are attached to the same source.  Thus (4.1)
includes all positive survivor mass; no prime endpoint needs a separate
prime-product parametrization.

Fix a block `I` of length `H=Y^h` and a late rectangle

```text
p asyp Y^u,             r asyp R=Y^(1-u).
```

If

```text
H<=R,                   equivalently u<=1-h,         (4.3)
```

then each fixed integer `r` has at most one integer `p` with `pr in I`.
Define `beta_(I,q,a)(r)=W_(q,a)(pr)` for this unique `p`, and zero otherwise,
and let `alpha_P(p)` be the band prime indicator.  On the block,

```text
sum_(pr in I)e_q(apr)W_(q,a)(pr)
 =sum_(pr in I)alpha_P(p)beta_(I,q,a)(r)e_q(apr).    (4.4)
```

This is an exact separated convolution.  At `h=1/2`, it covers the entire
late range `1/3<u<=1/2`, with the balanced endpoint split by factor order.
For `h>1/2`, it covers `u<=1-h`.  Past that boundary one may subdivide into
blocks of length `R`, but a naive recombination pays the power
`H/R=Y^(h+u-1)`.

The coefficient norm is not automatically logarithmic.  On terminal edges
of length at most `G=Y^(797/5000)`, (1.4) and (4.1) give

```text
sum_(x in I)|W_(q,a)(x)|^2 <<H G Y^o(1),
sum_(r asyp R)|beta_(I,q,a)(r)|^2/r
 <<H G/R Y^o(1).                                    (4.5)
```

For the first inequality, the negative two-gap squares and the two endpoint
squares are each at most `G` times the disjoint physical length.

Even granting a logarithmic norm in (4.5), Bazin's localized bound at
`h=1/2,b=.1537` is

```text
Y^(1-(h-3b)/2)=Y^.98055,                             (4.6)
```

whereas the unnormalized block target is

```text
H Y^(-kappa)=Y^(.4802595...).                        (4.7)
```

Thus it is weaker than the trivial `O(H)` estimate on the block.  Comparing
the saving `(h-3b)/2=.01945` only with `kappa` compares both quantities to
the whole-shell scale `Y`; it omits the mandatory factor `H/Y`.

The exact remaining late-band target in the unique-fiber range is a theorem
uniform in the block-dependent sequence in (4.4):

```text
|sum_(pr in I)alpha_P(p)beta_(I,q,a)(r)e_q(apr)
  -principal mode|
 <<H Y^(-kappa-delta),                               (4.8)
```

or a selector-aggregate `L4` analogue.  BFI and Maynard do not state this
short-product-interval estimate.  Bettin--Chandee accepts arbitrary
one-variable factors, but its Kloosterman-fraction/modulus-average theorem
is not (4.8).  Bazin accepts the separated coefficient (4.4), but the global
`Y` terms in Section 3 remain.  The first-return weight is therefore
algebraically removable in (4.3); short localization and selector
uniformity are the exact analytic gap.

## 5. Truth boundary

```text
late active composites are semiprimes:                PROVED
late dyadic band is nu_(2P)-nu_P:                     PROVED
separated global BV power frontier (0.1):             PROVED FROM BAZIN 8/10
frontier uniformly exceeds hostile kappa:             PROVED
source-centred transport formula (4.1):                PROVED
unique-large-factor separation for u<=1-h:             PROVED
Bazin theorem is block-localized at H=Y^h:            FALSE
common-height primitive selector removes q reuse:     FALSE
published theorem supplies short-block (4.8):          NONE FOUND
late weighted rough-Voronoi increment:                 OPEN
post-q SPF tail:                                      OPEN
```

## 6. Reproduction

```bash
python3 results/verify_zeta23_late_buchstab_semiprime_gate.py
```

The checker verifies every rational endpoint and exponent comparison in
(0.1)--(3.7).  It does not assert the missing low-rank or short-interval
dispersion theorem.
