# Common-height maximal incidence: fail-fast audit

**Date:** 2026-08-13

## Verdict

The fact that all curvature blocks come from one height `t` does not turn the
available large-sieve, fourth-moment, derivative, or rational-cell estimates
into a pointwise bound.  There are two exact reasons.

1. On a curvature block of length `H=Y/sqrt(t)`, the target threshold must be
   scaled by the block mass `H/Y`.  That normalization exactly consumes the
   apparent gain from applying the large sieve blockwise.  At every dyadic
   denominator scale, the resulting Markov allowance is at least one bad
   selected fraction in every block.  At the first surviving scale, the
   excess exponent is

   ```text
   theta+2*kappa=.1954606468.                         (0.1)
   ```

2. Rational cells selected by one height can have completely coincident bad
   incidences.  A rigorous odd-integer model below has one global logarithmic
   phase, one common height

   ```text
   t_0=2*pi*Y^.844,                                   (0.2)
   ```

   and retained one-turn gaps of size `Y^.156`.  The same `t_0` aligns their
   symmetrized Voronoi errors to total size `Y^(-kappa+o(1))`.  The model
   satisfies the optimized low-denominator excision, the full audited
   Gafni--Tao gap-tail envelope, Stadlmann's gap-square ledger, the cached
   truncated third-gap moment, the additive large sieve, bounded derivative
   estimates, and the coefficient-sensitive integer-product fourth moment.

This is a definitive no-go for the package

```text
common height + rational-cell geometry + current unsigned gap ledgers
+ coefficient-blind large sieve/large values + derivative regularity.    (0.3)
```

It is **not** an actual-prime counterexample.  In particular, it does not
satisfy an unproved actual-prime theorem for the symmetric successor-gap
character statistic.  The actual-prime selected-frequency theorem remains
open, but common-height incidence by itself is no longer a live source of the
missing power.

No zero-free strip is claimed.

---

## 1. The blockwise large-sieve gain cancels exactly

Put

```text
t=Y^a,                    H=Y^h=Y/sqrt(t),
h=1-a/2,                  K=Y/H=Y^(a/2),
theta=797/5000=.1594,     kappa=.0180303234.          (1.1)
```

There are `K` curvature blocks.  On an interior block `I`, its normalized
Voronoi mass is

```text
m_I asyp H/Y=Y^(-a/2).                                (1.2)
```

After deleting gaps above `Y^theta`, the global coefficient square sum is

```text
sum_n |a_n|^2 <<Y^(theta-1+o(1)).                     (1.3)
```

For a fixed height, absorb the exact nonlinear remainder of `t log n` on
each block into unit-modulus coefficients.  At denominators `q asyp Q=Y^r`,
the additive large sieve, applied separately on every block and then summed,
gives

```text
sum_I sum_(q asyp Q) sum_((s,q)=1)
 |sum_(n in I) a_(I,n)(t)e_q(sn)|^2
 <<(H+Q^2)Y^(theta-1+o(1)).                           (1.4)
```

The selected local value must be below `m_I Y^(-kappa)` on essentially all
blocks in order that triangle summation prove a global `Y^(-kappa)` bound.
If `Q^2<=H`, Markov applied to (1.4) permits

```text
N_bad(Q,t)
 <<Y^(theta-a/2) / Y^(-a-2*kappa)
 =Y^(theta+a/2+2*kappa)
 =K Y^(theta+2*kappa).                               (1.5)
```

The factor after `K` is the positive power in (0.1).  Thus (1.5) does not
even rule out one bad selected fraction on every block.

When `Q^2>=H`, the corresponding allowance relative to the number of blocks
has exponent

```text
2r+theta-1+a/2+2*kappa.                              (1.6)
```

At the transition `2r=h`, (1.6) again equals
`theta+2*kappa`; it only increases with `r`.  No dyadic denominator range
improves the conclusion.

This calculation also catches a tempting but invalid averaging step.  The
root-mean-square over the `asymp Q^2` rational fractions is small, but the
phase selects only one fraction on each block.  Dividing (1.5) by `Q^2`
would estimate an average number of bad *fractions*, not the number of blocks
having at least one selected bad fraction.

### Exact chirp reduction

For a block centered at `x_I`, write

```text
exp(i t log n)
 =exp(i t log x_I)
  exp(2*pi*i*alpha_I*(n-x_I)) W_(I,t)(n),
alpha_I=t/(2*pi*x_I),       |W_(I,t)(n)|=1.           (1.7)
```

Dirichlet approximation gives a reduced `s/q`, `q<=H`, with

```text
|alpha_I-s/q|<=1/(qH).                                (1.8)
```

Replacing `alpha_I` by `s/q` costs at most `O(m_I/q)`, because
`|n-x_I|<<H`.  Since every retained `q` is above `Y^.1537`, this error is
far below `m_I Y^(-kappa)`.  The unit-modulus chirp in (1.7) changes neither
the coefficient square sum nor (1.4).  It therefore cannot repair (1.5).

---

## 2. The one-parameter rational-cell geometry does not force emptiness

At a fixed physical center `x asyp Y`, the curvature cell for `s/q` is

```text
|t/(2*pi*x)-s/q|<=sqrt(t)/(Yq).                       (2.1)
```

For `t=Y^a`, its height radius is

```text
Delta t asyp sqrt(t)/q=Y^(a/2-r).                    (2.2)
```

In the companion range, `q<=H=Y^(1-a/2)`, so the smallest possible radius
in (2.2) is

```text
Y^(a-1).                                             (2.3)
```

The cells are not points, but their positive width is not the decisive fact.
What is missing is an incidence theorem preventing the bad cells attached to
different blocks from sharing one height.  Neither (1.4) nor a moment in `t`
contains such a cross-block transversality statement.  The model in Section
4 makes all relevant incidences share `t_0`.

A union bound over a height mesh cannot prove emptiness either.  For the
diffuse actual-prime quadrature, the exact fourth moment gives only

```text
measure{|P(t)|>Y^(-kappa)} <<Y^(4*kappa+o(1))
                           =Y^(.0721212936+o(1)).      (2.4)
```

Bounded second derivative says a peak at a local extremum occupies an
interval of length `gg Y^(-kappa/2)`.  Thus (2.4) permits

```text
Y^((9/2)*kappa+o(1))=Y^(.0811364553+o(1))             (2.5)
```

large components, and in particular permits one.  Guth--Maynard large-value
bounds likewise count separated large values; their structural first term
does not force that count to be zero.

There is also a quantifier issue.  The `Y^o(1)` fourth moment in the diffuse
quadrature report concerns its deliberately flattened coarse-cell weights.
The consecutive-gap route uses the positive Voronoi weights.  One cannot
combine the low-band property of the first vector with the rational-gap
structure of the second vector without proving a new coefficient-transfer
theorem.

---

## 3. An integer-product fourth moment for the countermodel

The fourth-moment mechanism itself is not prime-exclusive.  Let `X` be any
set of integers in a fixed multiplicative shell around `Y`, and put

```text
F_lambda(s)=sum_(n in X) lambda_n exp(i*s*log(n/Y)),
S_2=sum_n |lambda_n|^2.                               (3.1)
```

For every interval `J` of length `L`,

```text
integral_J |F_lambda(s)|^4 ds
 <<(L+Y^2)Y^o(1) S_2^2.                               (3.2)
```

Indeed, square (3.1) and group by the integer product `mn`.  Distinct
products have logarithmic spacing `gg Y^-2`.  Each product has at most
`d(mn)=Y^o(1)` ordered representations in the shell.  Cauchy--Schwarz in
each product fiber followed by the Montgomery--Vaughan mean-value inequality
proves (3.2).

This observation lets the common-height witness below retain integrality
and still satisfy the coefficient-sensitive moment ledger.

---

## 4. Common-height exact-log countermodel

Set

```text
beta=1537/10000=.1537,
b=39/250=.156,
theta=797/5000=.1594,
a=1-b=211/250=.844,
h=1-a/2=289/500=.578,
t_0=2*pi*Y^a.                                         (4.1)
```

Work in a fixed interior physical subshell on which `phi(log(x/Y))` is
positive.  Define the one global phase

```text
Phi(x)=t_0 log(x/Y).                                  (4.2)
```

The consecutive crossings of one fixed phase `xi modulo 2*pi` are separated
by

```text
ell(x)=x[exp(2*pi/t_0)-1]=Y^(b+o(1)).                 (4.3)
```

Select every `ceil(Y^kappa)`-th crossing.  At every selected crossing, round
the crossing and the next crossing to odd integers and leave the interval
between them empty.  These selected gaps are disjoint.  Fill every
complementary interval by odd integers with even gaps comparable with
`log Y`, retaining the selected endpoints.

The resulting ordered node set `X_Y` has

```text
#X_Y asyp Y/log Y,
#(X_Y intersect J)<<1+|J|/log Y,                      (4.4)
```

and its selected long gaps have

```text
g=Y^(b+o(1)),
N_L=Y^(1-b-kappa+o(1))=Y^(.8259696766...+o(1)).       (4.5)
```

Rounding changes each endpoint phase by only

```text
O(t_0/Y)=O(Y^-b).                                     (4.6)
```

Hence both endpoints of every selected gap have phase
`xi+o(1)`, and the phase makes one full turn across its logarithmic interval.

### 4.1 Critical retained Voronoi error

Let `Delta=log((x+g)/x)`.  On a selected gap,

```text
t_0 Delta=2*pi+O(Y^-b),       Delta=Y^(b-1+o(1)).    (4.7)
```

The two endpoint half-cell masses therefore point in the same direction,
while the constant-amplitude continuum integral over the full turn is zero.
Smooth variation of `phi` and the rounding error contribute `o(Delta)`.
Thus every selected gap contributes

```text
(c_phi+o(1))g/Y                                      (4.8)
```

after one common rotation, with `c_phi>0`, and all contributions align.
Using (4.5), their total is

```text
N_L Y^(b-1+o(1))=Y^(-kappa+o(1)).                    (4.9)
```

Globally, the small-gap mesh contributes only

```text
O(log Y/Y)+O(t_0^2 log^2(Y)/Y^2)
 =Y^(-2b+o(1))=o(Y^-kappa),                           (4.10)
```

by the exact half-cell/trapezoid comparison and the trapezoid Peano
remainder.  Smooth-amplitude errors of size `O(Delta^2)` on the long gaps
total

```text
Y^(b-1-kappa+o(1)).                                  (4.10a)
```

Rounding is larger than (4.10a), and must be recorded separately.  The
phase error `O(Y^-b)` in (4.6), multiplied by the interval mass
`Delta=Y^(b-1+o(1))`, gives `O(Y^-1)` per long gap.  Its total is

```text
Y^(-b-kappa+o(1))=o(Y^-kappa).                       (4.10b)
```

Consequently the exact retained logarithmic Voronoi error at the **single
common height** `t_0` has modulus

```text
asymp Y^(-kappa).                                     (4.11)
```

This coherence is blockwise, not merely a global concentration in one
exceptional block.  Every curvature block contains

```text
Y^(h-b-kappa+o(1))=Y^(.4039696766...+o(1))            (4.11a)
```

selected gaps.  Their aligned mass on that block is

```text
Y^(h-b-kappa)Y^(b-1)=Y^(h-1-kappa)
 =(H/Y)Y^(-kappa).                                    (4.11b)
```

The smooth continuum integral over one block is `O(t_0^-1)` after one
integration by parts, which is `o((H/Y)Y^-kappa)` at these exponents.  On
one block, the Peano part of the small-mesh error is

```text
t_0^2 (H/log Y)(log Y/Y)^3
 =Y^(h-1-2b+o(1)),                                   (4.11c)
```

and the half-cell correction is `Y^(h-2+o(1))`.  Both are
`o(Y^(h-1-kappa))`.  Thus
(4.11b) is also the size of the local node sum after its continuum
comparator is restored; it is not an artifact of subtracting two large
uncontrolled block terms.

Thus the model realizes exactly the relative block threshold used in
(1.5), on essentially every block, and all block contributions share the
same final complex direction.

### 4.2 Every selected rational comes from that same height

On the whole fixed shell,

```text
omega_(t_0)(x)=t_0/(2*pi*x) asyp Y^-b,
eta_(t_0)=sqrt(t_0)/Y=Y^(-h+o(1)).                   (4.12)
```

Because

```text
beta<b<h,                                             (4.13)
```

one has `eta<<omega<<1/Y^beta`.  The rational `0/1` is farther than its
curvature width.  Every positive reduced rational with denominator at most
`Y^beta` is at least `Y^-beta`, also farther than its width.  Across a
selected gap, `omega` changes by only `O(Y^-1)`, so the entire Voronoi cell
has the same margins.  No node in the construction is removed by the
optimized low-denominator deletion.

For each curvature block, Dirichlet's theorem now selects a reduced
`s_I/q_I` satisfying

```text
Y^beta<q_I<=H=Y^h,
|omega_(t_0)(x_I)-s_I/q_I|<=1/(q_I H).               (4.14)
```

All pairs `(s_I,q_I)` in (4.14) are therefore selected by the same `t_0`;
they are not arbitrary independently chosen numerators.  Nevertheless the
coherence (4.11) survives.  Combining the exact chirp identity (1.7) with
(4.11b), the rational value at `(s_I,q_I)` differs from this critical local
value by only

```text
O((H/Y)/q_I)=o((H/Y)Y^-kappa).                        (4.14a)
```

In particular, this construction explicitly realizes one common-height
selected bad rational value per curvature block, within the allowance of
(1.5).

### 4.3 Every current unsigned gap ledger holds

The long-gap mass and square mass are

```text
sum_L g=Y^(1-kappa+o(1)),
sum_L g^2=Y^(1+b-kappa+o(1))
         =Y^(1.1379696766...+o(1)).                   (4.15)
```

The small mesh adds only `Y log Y` to the square mass.  Thus the model is
well inside the `Y^(1.23+epsilon)` gap-square budget, and `b<theta` means no
gap is removed by the `Y^theta` cutoff.

On the audited Gafni--Tao branch, the allowed tail saving at threshold
`Y^gamma` is

```text
c_GT(gamma)=(9/13)(gamma-2/15).
```

At the model scale,

```text
c_GT(b)=51/3250=.01569230769...<kappa.                (4.16)
```

For `2/15<=gamma<=b`, (4.15) is below the allowed
`Y^(1-c_GT(gamma)+o(1))`; above `b` there are no long gaps.  Thus the full
audited tail envelope holds.

The selected contribution to the truncated third moment is

```text
sum_L g^3=Y^(1+2b-kappa+o(1))
         =Y^(1.2939696766...+o(1)),                   (4.17)
```

strictly below the cached actual-prime allowance
`Y^(84549/65000+epsilon)=Y^(1.300753846...+epsilon)`.

### 4.4 Large sieve, moment, derivative, and large-value ledgers

The normalized Voronoi coefficient square sum in this model is

```text
S_2
 <<N_L(Y^(b-1))^2+Y^(-1+o(1))
 =Y^(b-1-kappa+o(1))
 =Y^(-.8620303234...+o(1)),                           (4.18)
```

which is smaller than the generic truncated bound `Y^(theta-1)`.
The additive large sieve is an unconditional inequality for these integer
coefficients, so the model satisfies (1.4).

Applying (3.2) on the complete legal aperture `B=Y^(50/33)<Y^2` gives

```text
integral_0^B |F_lambda(s)|^4 ds
 <<Y^(2b-2*kappa+o(1))
 =Y^(.2759393532...+o(1)).                            (4.19)
```

Chebyshev at level `Y^-kappa` allows exceptional length

```text
Y^(2b+2*kappa+o(1))
 =Y^(.3480606468...+o(1)),                            (4.20)
```

so (4.11) is fully compatible with the fourth moment.  Since the logarithmic
frequencies lie in a fixed compact interval and the weights have bounded
total mass,

```text
sup_s |F_lambda^(j)(s)|=O_j(1).                       (4.21)
```

A single critical peak is therefore also compatible with all derivative and
large-value packet counts.  Those theorems never assert that the exceptional
set is empty.

### Scope of the model

The nodes are odd integers selected using (4.2), not primes.  The model does
not claim Bombieri--Vinogradov distribution, actual-prime successor laws, or
the missing symmetrized gap-character estimate.  It proves the exact
nonimplication

```text
(0.3) does not imply a better-than-Y^-kappa uniform bound
for arbitrary integral prime-density-shaped nodes.                    (4.22)
```

An actual-prime proof must therefore use an arithmetic fact coupling
primality to the preceding/following gaps (or prove the selected
Gauss-weighted character statistic directly).  Merely observing that the
same height selects all local fractions does not provide that fact.

---

## 5. Literature boundary

* Montgomery--Vaughan's
  [large sieve](https://doi.org/10.1112/S0025579300004708) averages the
  rational frequencies in (1.4).  It contains no maximal incidence theorem
  for one phase-selected fraction on each independently weighted block.
* Guth--Maynard,
  [*New large value estimates for Dirichlet polynomials*](https://arxiv.org/abs/2405.20552v2),
  count separated large values.  Their theorem and examples retain a
  structural first term which permits a singleton exceptional height.
* Gafni--Tao,
  [*On the number of exceptional intervals to the prime number theorem in
  short intervals*](https://arxiv.org/abs/2505.24017), supply the unsigned
  tail envelope used in (4.16), not a signed cross-block incidence theorem.
* Matomaki--Radziwill--Shao--Tao--Teravainen,
  [*Higher uniformity of arithmetic functions in short intervals II*](https://arxiv.org/abs/2411.05770v2),
  prove almost-all-block results for ordinary `Lambda` with logarithmic
  saving and fixed-complexity phases.  Their theorem is neither all-block
  pointwise nor a theorem for consecutive-gap Voronoi weights.
* Chen--Gupta--Li,
  [*Large Value Estimates for Dirichlet Polynomials with Characters and Zero
  Density of Dirichlet L-Functions*](https://arxiv.org/abs/2507.08296v2),
  count large character polynomials.  As already audited, their arbitrary-
  coefficient first term is larger than the entire selected character
  family at this normalization.

No primary source located proves the missing cross-block maximal incidence
statement.  More importantly, the model proves that no such statement can
follow from the coefficient-blind package (0.3); it would have to assume new
actual-prime arithmetic.

---

## 6. Reproduction

The exponent and inequality ledger is checked by

```bash
python3 results/verify_zeta23_common_height_maximal.py
```

The checker audits the algebra.  It does not replace the imported primary
theorems or turn the scoped integer model into an actual-prime theorem.

---

## 7. Hostile re-audit disposition

**Binary verdict: PASS after correction.**  The following points were
independently recomputed.

* In the `Q^2<=H` range, the large-sieve numerator has exponent
  `theta-a/2`, the squared local threshold has exponent `-a-2*kappa`,
  and division by the `K=Y^(a/2)` blocks leaves exactly
  `theta+2*kappa`.  In the `Q^2>=H` range, the relative exponent is (1.6)
  and agrees at `2r=h`.
* The height-cell radius is `sqrt(t)/q`; its exponent is `a/2-r`, ranging
  from `.2683` at `r=beta` to `-b=-.156` at `r=h`.  The construction's
  `alpha asyp Y^-b` lies outside every deleted low-denominator cell, while
  Dirichlet supplies a positive denominator `Y^beta<q<=Y^h` on every block.
* The one-turn gap count, per-block count, square and third moments,
  Gafni--Tao tail endpoint, coefficient square sum, and fourth-moment
  exponents all agree with the checker.
* Every selected gap is generated by the same exact logarithmic phase and
  the same `t_0`; the local rational pairs are approximants to that common
  derivative, not independently prescribed fractions.

The re-audit found two nonfatal error-ledger defects in the earlier text.
Integer rounding gives `Y^(-b-kappa+o(1))`, not the smaller aggregate
`O(sum Delta^2)`, and the small-mesh Peano error on one block is
`Y^(h-1-2b+o(1))`, not the unscaled global error.  Equations
(4.10a)--(4.10b) and (4.11c) now record the corrected bounds.  Both remain
strictly below their required global or local thresholds, so neither alters
the scoped no-go conclusion.
