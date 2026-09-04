# Rough first-return weights: exact automaton, rank barrier, and Bazin gate

**Date:** 2026-08-13  
**Status:** exact combinatorial reduction and fail-fast theorem-class audit;
the weighted residue-dispersion target remains open.

## Verdict

The neighboring-gap weight does have an unexpectedly small exact
representation, but not in the notion of rank accepted by the available
dispersion theorems.

For the indicator `rho_z(n)` of the `z`-rough integers, the forward
first-return distance is exactly a two-dimensional weighted-automaton matrix
product.  Thus the
truncated symmetrized Voronoi weight has constant **tensor-train / automaton
bond dimension**.  This is the cleanest new structural fact in this audit.

Converting that matrix product into ordinary shifted arithmetic
coefficients is expensive:

* the layer-cake form has `G` distinct empty-prefix conditions;
* exact inclusion--exclusion has `2^(G-1)` shifted monomials and correlation
  order up to `G`;
* the universal prefix kernel has exact separated rank `G`;
* even constant-error polynomial approximation of the empty-prefix Boolean
  law has degree `Theta(sqrt(G))`.

The proved Matomaki rough-gap square estimate makes the discarded tail small
only after taking

```text
G >= Y^(kappa+delta+o(1)),       kappa=.01974048259....       (0.1)
```

Consequently ordinary separation requires polynomially growing complexity;
fixed-order tuple sieves and Type-I/II decompositions do not result from the
truncation.  This is a definitive obstruction to the class of arguments that
expands the automaton into boundedly many shifted scalar coefficients and
then applies triangle or Cauchy.  It is **not** a no-go theorem for the actual
rough-Voronoi coefficient: a matrix-valued dispersion theorem could in
principle use the constant bond dimension without expanding it.  A fail-fast
calculation below shows, however, that the matrices are a nonsemisimple
triangular pair: their Jordan cocycle is the full first-return sum.  Ordinary
Hilbert-space large sieves see only its coefficient energy and gain nothing
from the dimension two.

Bazin's July 2026 Bombieri--Vinogradov theorem for exponential sums over
products of `k` primes does not provide that theorem.  Its printed Theorem 2
records a logarithmic-error corollary, but raw Proposition 4 plus the
additive-character reduction really gives a fixed-power **global-scale**
bound for one selected modulus.  This is an important correction.  On the
live companion blocks, its additive-twist range reaches the low-denominator
wedge `b<=h/3`, and the raw saving clears `kappa` once
`h>3b+2kappa`.  Nevertheless the resulting bound has scale `Y^(1-delta)`,
not the local scale `H Y^(-kappa)`; it is trivial even against the support
length throughout `h<=.5797`.  Repeated block selectors and, most decisively,
the shifted first-return coefficient remain outside the theorem.

## 1. Exact nearest-site and empty-prefix formulas

Let `S` be a locally finite subset of the integers, put `rho=1_S`, and anchor
at `n in S`.  Write

```text
g_+(n)=min{d>=1:rho(n+d)=1}.
```

For

```text
E_h^+(n)=prod_(1<=j<h)(1-rho(n+j)),
```

with the empty product equal to one, one has the exact layer cake

```text
g_+(n)=sum_(h>=1) E_h^+(n),                           (1.1)
```

where the sum terminates at the next point of `S`.  At a cutoff `G`,

```text
g_+(n)=sum_(1<=h<=G) E_h^+(n)+(g_+(n)-G)_+.          (1.2)
```

There is also a nearest-site pushforward form.  If `L_S(x)` is the last
point of `S` not exceeding `x`, then the forward endpoint measure is

```text
sum_(n in S) g_+(n) delta_n = sum_x delta_(L_S(x)).  (1.3)
```

The reverse form uses the next-site map.  Their arithmetic mean is the
symmetrized Voronoi/trapezoid measure with weight

```text
w_S(n)=[g_-(n)+g_+(n)]/2.                            (1.4)
```

Equations (1.1)--(1.4) are exact away from the already explicit shell
barriers.

### 1.1 Exact bond-dimension-two representation

Let `b_h=rho(n+h)` and evolve the column state `(alive,total)` by

```text
             [1-b_h  0]
M(b_h) =     [  1    1].                             (1.5)
```

Starting from `(1,0)`, after the inputs `b_1,...,b_G` the second coordinate
is exactly

```text
min(g_+(n),G).                                       (1.6)
```

Indeed, `alive` remains one precisely until the first survivor and `total`
adds its old value at every step.  The left-return rule is the reversed
copy.  A direct sum therefore represents both cutoffs `P,2P` and both
directions with bounded matrix dimension.

This is a weighted automaton (a finite-dimensional linear representation of
a rational series), not a two-state deterministic automaton: the second
coordinate stores an unbounded integer.  That distinction is essential.

This is real low rank, but it is tensor-train rank along the physical shifts.
Bazin, BFI/Maynard dispersion, and the ordinary large sieve require scalar
Dirichlet-convolution or product separation.  No surveyed theorem accepts
(1.5) as an input coefficient.

### 1.2 Triangularization is exact but does not simplify the arithmetic

Put `M_0=M(0),M_1=M(1)`.  Direct multiplication gives

```text
M(b_G)...M(b_1)
 =[ prod_(j<=G)(1-b_j)                         0 ]
  [ sum_(h=0)^(G-1) prod_(j=1)^h(1-b_j)       1 ].   (1.7)
```

The lower-left entry is exactly the truncated first return.  Thus the common
triangular flag reduces the product to two scalar entries, but the hard one
is the whole empty-prefix sum rather than an ordinary rough count.

The failure of semisimplicity is explicit:

```text
M_0^r=[1 0; r 1],
M_0 M_1-M_1 M_0=[0 0; -1 0].                         (1.8)
```

Hence the generators do not commute or diagonalize simultaneously, and the
unit eigenvalue of `M_0` has a Jordan cocycle growing exactly like the gap.
Words with the same number of survivor bits can have outputs `1` and `G`
depending on the first survivor's position.  No reduction to the one-point
rough count, or to a bounded collection of symmetric bit statistics, is
possible.

This is the promised fail-fast result for triangularization: dimension two
does not turn the target into two standard scalar rough sums.  The usual
Hilbert-space large-sieve inequality remains valid for matrix coefficients,
but its right side is their Hilbert--Schmidt energy.  It is therefore exactly
the coefficient-blind estimate already known to miss by a fixed power; the
internal dimension changes only a constant.  A single selected mode cannot
gain from dimension alone, since scalar coefficients embed as rank-one
matrix coefficients.

There is also a sharp finite countermodel to reduction to unweighted scalar
sums.  Periodically repeat the node residues

```text
S={0,1,3,4} mod 8,       consecutive gaps 1,2,1,4.  (1.8a)
```

At the parity character the unweighted node sum per period is zero, while
the twice-normalized symmetrized Voronoi sum is

```text
(4+1)-(1+2)-(2+1)+(1+4)=4.                          (1.8b)
```

The gap-square cost is only `1+4+1+16=22` per period, hence linear in the
ambient length.  Thus one-point additive cancellation plus a near-linear gap
second moment still does not control the weighted-automaton output.  This is
a non-prime, low-modulus method countermodel, not a counterexample to the
actual selected rough coefficient.

### 1.3 Exact marked-prime Duhamel/Buchstab identity

There is nevertheless a useful exact cutoff recursion.  Let

```text
b_h^0=rho_P(n+h),       b_h^1=rho_(2P)(n+h)<=b_h^0,
Pi_i=M(b_G^i)...M(b_1^i).
```

Telescoping matrix products gives

```text
Pi_1-Pi_0
 =sum_(h=1)^G
   [prod_(j=G)^(h+1) M(b_j^1)]
   [M(b_h^1)-M(b_h^0)]
   [prod_(j=h-1)^1 M(b_j^0)],                        (1.9)
```

and every insertion has rank one:

```text
M(b_h^1)-M(b_h^0)
 =(b_h^0-b_h^1)[1 0;0 0].                           (1.10)
```

The marked scalar has the exact SPF expansion

```text
b_h^0-b_h^1
 =sum_(P<p<=2P) 1_(n+h=pm, P^-(m)>=p).              (1.11)
```

Including the change of the anchored centre supplies the identical marked
term at `h=0`.  Equations (1.9)--(1.11) are an exact matrix-valued Buchstab
identity for the truncated band increment.  They isolate one `p,m,h` mark,
but the matrices on its two sides still contain the full first-survivor laws
of the surrounding shifts.  Opening those products recovers (3.1), while
taking norms before summing `h` loses the cross-`h` covariance.  Thus this
recursion sharpens the open interface but does not satisfy Bazin's separated
Dirichlet-convolution hypotheses.

There is no smaller uniform recursive norm hidden here.  On the old word
`b_h^0=1` and new word `b_h^1=0` for every `h<=G`, the lower-left entry of
`Pi_1-Pi_0` is `G-1`.  Hence any norm estimate based only on the matrix
recursion must pay a linear `G` in the worst case.  Arithmetic restrictions
could exclude or cancel this word, but that would be precisely the new input
being sought.

## 2. What the rough-gap moment buys

Let the consecutive `z`-rough gaps in the retained shell be `d_i`, including
the explicit boundary gaps, and define the weight-truncated measure by
replacing both neighboring gaps by their minima with `G`.  Then positivity
and the fact that every gap is used once in each direction give

```text
||nu_z-nu_(z,G)||_TV
 =sum_i (d_i-G)_+
 <=G^(-1) sum_i d_i^2.                               (2.1)
```

Consequently

```text
||(nu_(2P)-nu_P)-(nu_(2P,G)-nu_(P,G))||_TV
 <=G^(-1)[G_2(Y;P)+G_2(Y;2P)].                      (2.2)
```

In the interior of the range where both cutoffs satisfy

```text
Y^.1537 <= P,2P <= Y^.16,
```

the proved Matomaki--Iwaniec estimate gives

```text
G_2(Y;P)+G_2(Y;2P) <<Y(log Y)^2.                    (2.3)
```

To make (2.2) at most `Y^(1-kappa-delta+o(1))`, it is therefore enough and,
for this coefficient-blind use of (2.3), necessary to take

```text
G=Y^(kappa+delta+o(1)).                              (2.4)
```

This is useful but sharply scoped.  A post-`q` band starts at `P>=q`, so the
proved moment theorem can help only for selector exponents

```text
.1537 <= log q/log Y <= .16,
```

a width of exactly `.0063`.  For `q>Y^.16` it does not touch even the first
post-`q` band.  The terminal-prime edge cap supplies a weaker gap square for
the later bands, but it is not near-linear and cannot make (2.2) power-small
at any cutoff below the edge cap.

## 3. Why scalar separation expands again

For Boolean inputs `b_1,...,b_(G-1)`, expanding (1.2) gives

```text
sum_(h<=G) prod_(j<h)(1-b_j)
 =G+sum_(empty != A subset {1,...,G-1})
       (-1)^|A| (G-max A) prod_(j in A)b_j.           (3.1)
```

After multiplication by `rho_z(n)`, a term indexed by `A` is a shifted
rough correlation of order `|A|+1`.  Formula (3.1) has `2^(G-1)` terms and
uses every order through `G`.  The cancellations between these terms are the
first-return condition; taking absolute values destroys them.

There is a smaller exact layer representation, but it still cannot have
bounded universal rank.  The gap/prefix matrix

```text
K(d,h)=1_(h<=d),             1<=d,h<=G,              (3.2)
```

is triangular with determinant one.  Hence every exact decomposition

```text
K(d,h)=sum_(j<=R) A_j(d)B_j(h)                       (3.3)
```

valid for the full first-return functional has `R>=G`.  Restricting to even
gaps merely gives the same statement with rank `floor(G/2)`.

There is an approximation-theoretic version of the same warning.  Empty
prefix is the NOR function of `G-1` bits.  Paturi's theorem gives constant
error approximate degree `Theta(sqrt(G))`.  At the minimal cutoff (2.4),
even this very lenient scalar polynomial interface has degree at least

```text
Y^(kappa/2+o(1))=Y^(.009870241295...+o(1)).           (3.4)
```

This does not contradict the dimension-two weighted automaton: polynomial degree and
tensor-train bond dimension are different notions of complexity.

### 3.1 Dyadic gap layers do not give power accuracy

Rounding each retained gap to a dyadic value uses only `O(log G)` thresholds,
but has constant relative error.  Since the sum of the gaps is the physical
length, its coefficient-blind total error is `asymp Y`, not
`Y^(1-kappa)`.

Using multiplicative bins of ratio `1+eta` gives total mass error at most
`eta Y`.  Uniform power accuracy therefore requires

```text
eta<=Y^(-kappa-delta),
# thresholds >>Y^(kappa+delta) log G.                (3.5)
```

Thus deterministic threshold compression returns to the same polynomial
complexity.  An approximation adapted to the *actual joint distribution* of
gap length, residue, and selected numerator is not ruled out; the rough-gap
second moment alone contains none of that joint information.

### 3.2 Exact loss for expand-then-Cauchy methods

The optimistic coefficient-blind `L2` baseline is already of order
`Y^(1+o(1))`, whereas selector closure asks for `Y^(1-2kappa-delta)`.
If an exact `R`-piece expansion is recombined only through

```text
||sum_(j<=R)c_j||_2^2 <= R sum_(j<=R)||c_j||_2^2,   (3.6)
```

the forced `R>=G=Y^(kappa+o(1))` consumes another `kappa`.  Even granting the
unrealistically favorable collective baseline `sum_j||c_j||_2^2=Y^(1+o(1))`,
this proof class lands at exponent `1+kappa`, missing the target by

```text
3 kappa=.05922144777....                             (3.7)
```

This is a no-go for (3.6), not for a proof that preserves matrix-product or
cross-layer cancellation.

## 4. Bazin 2026: exact scope audit

Bazin's [Theorem 2](https://arxiv.org/abs/2607.15137) proves, for
`f_k(n)=1_(Omega(n)=k)`, a rational-additive Bombieri--Vinogradov theorem
summed over `q<=Q`, with

```text
Q<=x^(1/3)(log x)^(-B),
|lambda|<=Q^(-3)(log x)^(-B),                       (4.1)
```

and total error `x/(log x)^C`.  Stopping at that corollary is too
pessimistic.  Proposition 4 gives the explicit character-sum estimate

```text
Xi(f_k;x,Q,theta)
 <<[x^(1/2)Q^2+x^(5/6)Q+x+xQ^2 theta^(1/2)]x^o(1). (4.2)
```

For a separated coefficient supported on units modulo every `q asyp Q`
(for example, a late semiprime rectangle whose two factors exceed `2Q`),
combining (4.2) with Bazin's additive-character Lemma 6 on one dyadic
modulus range, and bounding one selected `q` by the complete average, gives
the global-scale error

```text
x^(1/2)Q^(3/2)+x^(5/6)Q^(1/2)+xQ^(-1/2)
  +xQ^(3/2)theta^(1/2),                              (4.3)
```

up to divisor logarithms and the explicit principal term.  Unit support is
what gives the `Q^(-1/2)` conversion; unrestricted `f_k` has additional
`t|n` sectors in Lemma 6, so (4.3) is not being asserted for an arbitrary
coefficient by title-level analogy.  For a smooth
window of physical length `H=Y^h`, Fourier inversion has `L1` norm
`Y^o(1)` and requires `theta=Y^o(1)/H`; the ambient variable remains `x=Y`,
not `H`, because translating `f_k(Y_0+m)` destroys multiplicativity.  With
`q=Y^b`, the raw relative saving in (4.3) is

```text
delta_B(b,h)
 =min{b/2,(1-3b)/6,(h-3b)/2}.                       (4.4)
```

There are two genuine points of contact.

1. On the shallow `h=33/133` slice, the selected moduli
   `q<=Y^(33/133)` lie below `Y^(1/3)` with exponent margin

   ```text
   1/3-33/133=34/399=.0852130....                    (4.5)
   ```

2. A `P`-rough integer near `Y`, with `P>=Y^.1537`, has only boundedly many
   prime factors.  Splitting unweighted rough-centre counts by `Omega` is
   therefore compatible in spirit with Bazin's `k` range.  In the late
   semiprime band, Bazin's sharper Lemma 10 gives still better raw power for
   a separated rectangular prime convolution.

Neither point reaches the target.

* Bazin treats unrestricted `f_k`, not the condition that every factor exceed
  `P`, and not the shifted products in (3.1).
* The printed theorem sums each modulus once, while (4.3) bounds a selected
  modulus by the entire dyadic average.  A selected denominator may repeat
  on polynomially many independently weighted curvature blocks; neither
  statement supplies that block multiplicity.
* On the shallow `h=33/133` slice, Fourier localization really is outside
  (4.1): `H>=q^3` fails for every legal `b>=.1537`, with margin

  ```text
  33/133-3(1537/10000)
     =-283263/1330000=-.2129796992....                (4.6)
  ```

* This last statement is **not** true throughout the live companion band.
  There

  ```text
  1/2<=h<=.5797,       .1537<=b<=h,                  (4.7)
  ```

  and the twist hypothesis reaches the nonempty wedge `b<=h/3`.  At the
  lowest point `(b,h)=(.1537,.5)`, its twist saving is

  ```text
  (h-3b)/2=.01945,
  (h-3b)/2-kappa=-.00029048259....                   (4.8)
  ```

  It clears the global hostile bill exactly when

  ```text
  h>3b+2kappa;
  at b=.1537 the threshold is .50058096518....       (4.9)
  ```

  Thus Bazin exposes a real low-`q` global-power subrange.
* It still does not give a useful **local block** estimate.  For the twist
  term in (4.3) to be at most the required `H Y^(-kappa)`, one needs

  ```text
  h>=2/3+b+(2/3)kappa.                               (4.10)
  ```

  Even at the most favorable `b=.1537`, the right side is
  `.833526988...`, above the companion maximum `.5797` by
  `.253826988...`.  Endpoint differencing has the same ambient-`Y` scale.
* Most fundamentally, the coefficient

  ```text
  rho_P(n) prod_(j<s)(1-rho_P(n+j))                  (4.11)
  ```

  is a shifted joint first-return law, not a one-variable multiplicative
  function or one of Bazin's separated convolutions.  The bond-dimension-two
  form
  (1.5) does not change that hypothesis.

Therefore Bazin supplies neither the localized primitive `L2/L4` theorem nor
a no-go against it.  Its strongest useful lesson here is architectural: a
future matrix-valued analogue of Proposition 4 would have the correct
rational-additive interface, and the raw theorem is not exponent-starved in
the low-`q` companion wedge.  What is missing is an estimate at the local
`H` scale which accepts the first-return matrix product and repeated selected
block weights.

## 5. Other primary literature checked

* Matomaki's [*Almost primes in almost all very short
  intervals*](https://arxiv.org/abs/2012.11565) supplies the vector-sieve
  localization behind (2.3), but not residue classes of first-return mass.
* Gorodetsky's [rough-number short-interval variance
  theorem](https://link.springer.com/article/10.1007/s00209-024-03601-w)
  analyzes unweighted two-point variance.  Its main asymptotic condition does
  not allow both roughness `y=Y^u` and interval length `H=Y^gamma` with fixed
  positive `u,gamma`: its left side grows like `log Y/loglog Y`, while its
  right side stays bounded.  The paper's tuple fundamental lemma has constants
  depending on fixed tuple order and does not cover (3.4).
* Ford--Konyagin--Maynard--Pomerance--Tao's [*Long gaps in sieved
  sets*](https://ems.press/journals/jems/articles/17283) constructs long gaps
  in very general sifted sets.  It neither distributes nearest-site weights
  in growing residue classes nor forbids such distribution in this specific
  rough flow.
* Paturi's [symmetric-Boolean approximation
  theorem](https://doi.org/10.1145/129712.129758) gives the scalar polynomial
  barrier (3.4).  It is a complexity statement for arbitrary Boolean inputs,
  not an arithmetic lower bound for the actual rough sequence.
* Berstel--Reutenauer's [theory of noncommutative rational
  series](https://www-igm.univ-mlv.fr/~berstel/LivreSeries/LivreSeries.html)
  identifies finite-dimensional linear representations with weighted
  automata and finite Hankel rank.  It explains why (1.5) has bond dimension
  two.  It supplies representation/minimization theorems, not cancellation
  for an arithmetic source word; finite Hankel rank does not make the Jordan
  semigroup (1.8) contractive or mixing.

No primary theorem was located that combines a matrix-valued weighted-automaton
local weight, fixed-power roughness, polynomial selected moduli, and
short-block Bombieri--Vinogradov dispersion.

## 6. Independent audit: the arbitrary-selector `L2` target is false

The newly proposed selector-uniform `L2` closure theorem is too strong even
though its deterministic implication is correct.  At

```text
h=33/133,       q=floor(Y^h),       H=q+O(1),        (6.1)
```

partition the shell into half-open blocks of `q` consecutive integer sites
and discard the already-budgeted terminal edges crossing a block boundary.
Reduction modulo `q` is injective in every retained block.  In a simultaneous
band deletion, a deleted centre occurs only as a negative atom of
`nu_(2P)-nu_P`; all positive transport atoms lie on surviving sites.  Hence

```text
sum_(I,P)||Delta_(I,P)||_2^2
 >=#{retained post-q deleted centres}.               (6.2)
```

There are `>>Y/log Y` usable centres already among semiprimes `pr` with

```text
Y^.30<p<=Y^.31,       Y<pr<=2Y,       r prime.       (6.3)
```

Both factors exceed `q`, `p` is the unique SPF label, and each centre occurs
in one dyadic band.  The deleted long-edge region has length
`Y^(.981954...+o(1))`, and all crossing edges have total length
`Y^(.911280...+o(1))`; both are `o(Y/log Y)`.  Since `q/H=1+o(1)`, the left
side of the proposed weighted `L2` theorem is `>>Y/log Y`, contradicting its
allowed `Y^(1-2kappa+o(1))=Y^(.960519...+o(1))`.

This falsifies uniformity over arbitrary legal block selectors.  It does
**not** yet falsify a theorem restricted to the denominators produced by one
fixed common height: no common height has been shown to choose the same
injective `q` on these blocks.

The same diagonal does not kill the `L4` route.  If `N_(I,P)` centres are
deleted, then `C_Delta(0)^2>=N_(I,P)^2`.  Cauchy over `Y/H` blocks and
`Y^o(1)` bands forces only

```text
sum_(I,P) q/H^3 sum_s|C_Delta(s)|^2
 >>Y/H times a polylogarithmic loss
 =Y^(1-h-o(1)).                                      (6.4)
```

At `h=33/133` this exponent is `.751879...`, safely below the allowed
`1-4kappa=.921038...`.  Other correlations could still violate the theorem,
but physical diagonal mass alone does not.  The common-height selected `L4`
coefficient is therefore the honest surviving moment target.

## 7. Strongest continuation exposed by the audit

The low-rank object worth attacking is not a `p,m,h` CP decomposition.  It is
the matrix-valued character/additive sum

```text
sum_(n in I) rho_z(n) e_q(a n)
  u^T [prod_(1<=j<=G) M(rho_z(n+j))] v,              (7.1)
```

and its left-return and `z=P,2P` direct-sum variants, with
`G=Y^(kappa+delta)`.  A selector-stable dispersion theorem for (7.1) would
preserve the exact weighted-automaton cancellation that every scalar
expansion loses.

Two possible interfaces remain live:

1. a matrix-valued Selberg/Buchstab dispersion argument that averages over
   the marked band prime before opening the physical-shift product;
2. a short-interval pseudorandomness theorem saying that the divisibility
   word `rho_z(n+1),...,rho_z(n+G)` fools this particular dimension-two
   weighted automaton even after a primitive additive twist.

Neither theorem presently exists in the surveyed literature.  They are
strictly stronger than a rough-gap second moment but more structured than an
arbitrary high-order tuple theorem.  This is a live reformulation, not a
claimed advance toward a strip by itself.

## 8. Truth boundary

```text
empty-prefix / nearest-site formulas:                 PROVED
dimension-two weighted-automaton representation:      PROVED
triangular Jordan closed form:                        PROVED
rank-one marked-prime Duhamel recursion:               PROVED
gap-square truncation inequality:                     PROVED
minimal moment-based cutoff exponent kappa:           PROVED
exact universal prefix rank G:                        PROVED
constant-error polynomial degree Theta(sqrt G):       PUBLISHED / APPLIED
dyadic threshold compression gives power accuracy:    FALSE COEFFICIENT-BLIND
Matomaki G2 touches the entire post-q tail:            FALSE
Bazin shallow-slice lambda range:                     DISJOINT
Bazin companion low-q lambda wedge:                   NONEMPTY
Bazin raw global saving clears kappa:                 YES ON A SUBRANGE
Bazin bound reaches local H*Y^-kappa scale:            FALSE
Bazin coefficient contains first-return weight:       FALSE
arbitrary-selector L2 closure theorem:                FALSE
common-height-restricted L2 theorem:                  NOT FALSIFIED HERE
diagonal mass falsifies L4 closure theorem:           FALSE
bounded scalar p,m,h separation from current inputs:  NOT OBTAINED
matrix-valued selected-modulus dispersion theorem:    OPEN
common-height weighted rough-Voronoi L4 theorem:       OPEN
post-q tail / zero-free strip:                        NOT CLAIMED
```

## 9. Reproduction

```bash
PYTHONPATH=src python3 -m unittest -v \
  src/test_rough_first_return_rank_gate.py
python3 results/verify_zeta23_rough_first_return_rank_gate.py
```

The verifier checks the exact empty-prefix, inclusion--exclusion,
weighted-automaton product, triangular closed form, rank-one Duhamel identity,
commutator, tail-square, rational-rank, and exponent ledgers.
