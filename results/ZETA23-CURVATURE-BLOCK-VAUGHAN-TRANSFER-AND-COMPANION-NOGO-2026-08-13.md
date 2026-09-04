# Curvature blocks: Vaughan transfer ledger and companion-band no-go

**Date:** 2026-08-13

## Verdict

No theorem-grade actual-prime saving is obtained.  Freezing the logarithmic
phase on its natural curvature block gives the exact range

```text
H=Y/sqrt(t)=Y^h,       1/2<=h<=5797/10000,
Y^(1537/10000)<q<=H.                                  (0.1)
```

The quadratic part of `t log x` has only bounded variation on this block.
It can be absorbed into a smooth weight, but supplies no extra power with
which to regularize the consecutive-gap coefficients.

For the ordinary von Mangoldt coefficient, global Vaughan cancellation has
ample exponent: its worst relative saving on (0.1) is `.07685`.  It cannot be
localized by differencing prefix bounds: the resulting absolute bound is
`Y^.92315`, whereas `H<=Y^.5797`.  The best all-interval short-interval
theorems begin at `H>Y^(5/8+epsilon)`.  The newer almost-all theorem reaches
`H>Y^(1/3+epsilon)`, but has only logarithmic saving and a logarithmic-size
exceptional set.  Neither statement transfers to a fixed power on every
block, and neither has the successor-gap coefficient.

There is also a rigorous, deliberately **non-prime** obstruction within the
companion band.  At

```text
b=39/250=.156,        t=2*pi*Y^(1-b)=2*pi*Y^.844,
one-period gap asyp Y^b,  H asyp Y^(.578),            (0.2)
```

one can make odd-integer, prime-density-shaped nodes with exact logarithmic
curvature and symmetrized Voronoi weights whose retained antenna has size
`asymp Y^(-kappa)`.  The nodes obey the full audited Gafni--Tao gap-tail
envelope, Stadlmann's gap-square budget, the `Y^.1594` retained-gap cutoff,
and the `q<=Y^.1537` rational deletion.  Thus curvature, integrality, those
gap budgets, and blockwise completion do not imply the target for arbitrary
nodes.

This is **not an actual-prime counterexample and not an actual-prime no-go
theorem**.  It leaves exactly the coefficient-specific possibility requested
by the project: cancellation forced by actual primality jointly with the
symmetrized preceding/following consecutive gaps.

---

## 1. Exact curvature-block normal form

Write

```text
f(x)=t log(x)/(2*pi),          alpha_x=t/(2*pi*x),
H=Y/sqrt(t).
```

Uniformly for `x asyp Y` and `|u|<=H`, Taylor's theorem gives

```text
f(x+u)
 =f(x)+alpha_x u-t u^2/(4*pi*x^2)+O(t H^3/Y^3)
 =f(x)+alpha_x u+O(1)+O(t^(-1/2)).                   (1.1)
```

More precisely, the quadratic term has order one across the block and the
cubic remainder is `O(t^(-1/2))`.  Dirichlet approximation supplies coprime
`r,q` with

```text
1<=q<=H,            |alpha_x-r/q|<=1/(qH).           (1.2)
```

The width in (1.2) is exactly the cached deletion width
`sqrt(t)/(Yq)`.  Hence a retained block forces

```text
Q<q<=H,             Q=Y^beta, beta=1537/10000.       (1.3)
```

On the proved-transition complement `Y^.8406<=t<=Y`,

```text
h=1-(log_Y t)/2 lies in [1/2,5797/10000].            (1.4)
```

Multiplication by the quadratic chirp in (1.1) is multiplication by a smooth
function whose `j`th block derivative is `O_j(H^(-j))`.  Completion of a
smooth unweighted sum can exploit this.  For arbitrary coefficients it does
not create cancellation: after residue decomposition it merely changes each
residue sum by a bounded-variation weight.

---

## 2. The exact Vaughan localization loss

For `alpha=r/q+O(q^-2)`, the classical global estimate is

```text
sum_(n<=Y) Lambda(n)e(alpha n)
 <<(Y/sqrt(q)+Y^(4/5)+sqrt(Yq)) log^4 Y.              (2.1)
```

If `q=Y^c`, its relative power saving is

```text
d_V(c)=min(c/2,1/5,(1-c)/2).                         (2.2)
```

For every denominator in (1.3), throughout the companion band,

```text
d_V(c)>=beta/2=1537/20000=.07685.                    (2.3)
```

But differencing two global prefix estimates to bound a block gives only

```text
Y^(1-beta/2+o(1))=Y^(.92315+o(1)).                   (2.4)
```

At the longest live block this exceeds its length by

```text
.92315-.5797=.34345.                                 (2.5)
```

It is therefore not merely short of the target exponent: it is trivial after
localization.

Applying Vaughan's identity afresh does not transfer to the actual target.
For a balanced Type-II factorization `mn asyp Y`, the product restriction
`x<mn<=x+H` leaves fibers of length at most

```text
H/Y^(1/2)<=Y^(.0797),                                (2.6)
```

whereas every retained denominator is `>Y^.1537`.  A naive completion that
requires one full period of the original denominator inside each balanced
fiber is therefore unavailable.  This comparison is not a no-go for a
bilinear Type-II argument: after one variable is frozen, gcd reduction may
change the effective denominator.  More fundamentally, the Voronoi coefficient

```text
(g_(j-1)+g_j)/2
```

has no Vaughan/Heath--Brown convolution identity.  Expanding
consecutiveness introduces prime correlations of unbounded order.

The prefix comparison with the natural prime weight is also not a repair.
At Voronoi boundaries it is exactly `x-vartheta(x)`.  A uniform fixed-power
prefix transfer would already be a fixed-power PNT and hence strip-strength.
This does not exclude a frequency-specific transfer; it identifies that
transfer as new arithmetic input.

---

## 3. Why the standard oscillatory tools stop

### 3.1 Van der Corput and exponent pairs

With the coefficient extended by zero to the integers, the first
van-der-Corput step produces correlations

```text
sum_n a_(n+h) conjugate(a_n)
 e(f(n+h)-f(n)).                                     (3.1)
```

For the gap antenna, (3.1) is a weighted correlation between endpoints of
consecutive-prime cells.  Gap moments control `sum |a_n|^2`; they do not
control (3.1) with its sign.  Exponent-pair bounds for a smooth phase assume
an unweighted or suitably factored coefficient and therefore cannot be
inserted coefficient-blindly.

### 3.2 Completion and characters

At the frozen rational, completion gives the already audited exact statistic

```text
1/phi(q) sum_(chi mod q) tau_q(chibar;r) C_q^sym(chi), (3.2)
```

where `C_q^sym(chi)` weights `chi(p)` by the preceding and following gaps.
The principal character is harmless.  No fixed-modulus variance or selected
Gauss-weighted bound for the nonprincipal part is known.  The quadratic
factor in (1.1) changes (3.2) only by smooth block weights.

### 3.3 Dispersion

The additive large sieve gives an RMS saving `.074` at the bottom
denominator after gap truncation.  It still permits one exceptional numerator
for every selected modulus.  Since the logarithmic phase selects one such
numerator and modulus, an average-frequency result is not pointwise closure.

---

## 4. Companion-band one-period-gap countermodel

Put

```text
kappa=.0180303234,
beta=1537/10000=.1537,
theta=797/5000=.1594,
b=39/250=.156,
a=1-b=211/250=.844,
h=(1+b)/2=289/500=.578.                              (4.1)
```

The Gafni--Tao tail-saving envelope on this range is

```text
c_GT(gamma)=(9/13)(gamma-2/15).
```

At `b`,

```text
c_GT(b)=51/3250=.01569230769...<kappa.               (4.2)
```

Take `t=2*pi*Y^a` and work in a fixed interior multiplicative sub-shell on
which the amplitude `phi` is positive.  The phase

```text
Phi(x)=t log(x/Y)                                    (4.3)
```

makes one turn over the physical distance

```text
ell(x)=x(exp(2*pi/t)-1) asyp Y^b.                    (4.4)
```

There are `asymp Y^(1-b)` phase crossings in the sub-shell.  Select every
`Y^(kappa+o(1))`th crossing.  Round its location `x_j` and the location one
turn later to odd integers.  The resulting selected gaps satisfy

```text
g_j=Y^(b+o(1)),
Phi(x_j)=xi+O(Y^-b) mod 2*pi,
Phi(x_j+g_j)=xi+O(Y^-b) mod 2*pi,                    (4.5)
```

for one fixed `xi`, and their number is

```text
N_L=Y^(1-b-kappa+o(1)).                              (4.6)
```

They are disjoint because successive selected crossings are separated by
`Y^(b+kappa+o(1))`.  Fill every complementary interval by odd integer nodes
with even gaps comparable to `log Y`, retaining the selected endpoints and
putting no node inside a selected gap.  This gives

```text
#nodes asyp Y/log Y,
#(nodes in J)<<1+|J|/log Y.                          (4.7)
```

### 4.1 All audited gap budgets hold

The selected long-gap mass and square mass are

```text
sum_L g_j=Y^(1-kappa+o(1)),
sum_L g_j^2=Y^(1+b-kappa+o(1))=Y^(1.1379696766...+o(1)). (4.8)
```

The small mesh contributes `O(Y log Y)` to the square mass.  Hence the total
is `o(Y^1.23)`.  Also `b<theta`, so no gap reaches the retained-gap deletion
threshold `Y^.1594`.

For every `2/15<=gamma<=b`, the Gafni--Tao-style allowed mass is
`Y^(1-c_GT(gamma)+o(1))`.  Since `c_GT(gamma)<=c_GT(b)<kappa`, (4.8) obeys
the full envelope.  Above `b` there are no long gaps.  Thus the construction
does not cheat by violating an already collected gap-tail input.

### 4.2 The optimized rational deletion misses it

On this shell,

```text
omega_t(x)=t/(2*pi*x) asyp Y^-b,
eta_t=sqrt(t)/Y asyp Y^-h.                           (4.9)
```

Because

```text
beta<b<h,
```

one has `eta_t<<omega_t<<1/Q`.  The rational `0/1` is farther than its
deletion width, and every positive rational with denominator at most `Q` is
at least `1/Q`.  Consequently the selected cells avoid the entire optimized
low-denominator deletion.  This holds for the whole selected Voronoi cell,
not just its node: across a cell of physical length `O(Y^b)`,

```text
|Delta omega_t|<<t Y^b/Y^2<<Y^-1,                   (4.10)
```

which is negligible compared with both margins `omega_t-eta_t` and
`1/Q-omega_t`.  Dirichlet's theorem still supplies a curvature-
resolution approximant, and retention forces its reduced denominator to
satisfy exactly

```text
Q<q<H.                                               (4.11)
```

No claim that this `q` is comparable with the one-period gap is needed.
Rounding a physical period of size `Y^b` to an integer generally controls
the reciprocal approximation only on scale `O(Y^(-2b))`, which need not
reach the Dirichlet width.  The construction is compatible with (4.11) but
does not claim to realize every denominator in that range.

### 4.3 The exact logarithmic Voronoi error is critical-size

For one selected gap let `Delta=log((x+g)/x)`.  Equations (4.4)--(4.5) give

```text
t Delta=2*pi+O(Y^-b),        Delta asyp g/Y.          (4.12)
```

The two half-cell endpoint contributions have the same phase, while the
continuum integral across one full turn is `o(Delta)`.  Smooth variation of
`phi` is also `o(Delta)`.  After a common rotation, each selected gap
therefore contributes

```text
(positive constant+o(1)) g/Y                         (4.13)
```

to `P_Y(t)-b(t)`.  The contributions align by (4.5), so (4.8) yields

```text
|P_Y(t)-b(t)| >=Y^(-kappa+o(1)).                     (4.14)
```

The small gaps contribute at most

```text
O(log(Y)/Y)+O(Y^(-2b)log^2 Y)=o(Y^-kappa)            (4.15)
```

by the exact half-cell-to-trapezoid error and the trapezoid Peano remainder.
This proves the claimed abstract obstruction.

### Scope of the obstruction

The construction uses odd integers chosen by phase.  They are not primes.
It proves only that the following package does not imply a better-than-
`Y^-kappa` pointwise antenna bound for arbitrary nodes:

```text
integrality + exact t log x curvature + positivity + symmetric Voronoi rule
+ prime-shaped density + full audited gap tails + gap-square budget
+ optimized low-q deletion.                          (4.16)
```

It does not rule out an identity or distribution theorem peculiar to the
actual consecutive primes.

---

## 5. Primary-literature boundary

* Vaughan's global natural-weight estimate has the favorable exponent in
  (2.3), but it is a length-`Y` theorem and has the wrong coefficient.
* Matomaki--Shao--Tao--Teravainen,
  [*Higher uniformity of arithmetic functions in short intervals I*](https://arxiv.org/abs/2204.03754),
  treats all intervals for `Lambda` from `H>=X^(5/8+epsilon)`, with
  arbitrary logarithmic saving after subtracting its major-arc approximant.
* Matomaki--Radziwill--Shao--Tao--Teravainen,
  [*Higher uniformity of arithmetic functions in short intervals II*](https://arxiv.org/abs/2411.05770),
  reaches `H>=X^(1/3+epsilon)` for almost all intervals, again with
  logarithmic saving and a logarithmic exceptional set.  It does not imply
  an all-block fixed power.
* Matomaki--Shao,
  [*Discorrelation between primes in short intervals and polynomial phases*](https://arxiv.org/abs/1902.04708),
  gives an all-interval inverse theorem only above `X^(2/3+epsilon)` and at
  logarithmic strength.
* Kim,
  [*Prime Running Functions*](https://doi.org/10.1080/10586458.2020.1786863),
  makes even a fixed-modulus one-sided successor-gap main term conjectural
  for actual primes.  Its fixed-sieve random-model theorems are not
  actual-prime estimates.
* Gafni--Tao,
  [*On the number of exceptional intervals to the prime number theorem in
  short intervals*](https://doi.org/10.2140/ent.2026.5.221), supplies the
  unsigned tail envelope used in (4.2), not a signed gap Fourier theorem.

No primary source located proves a power estimate for the selected
symmetrized gap-character statistic, either with or without the bounded
quadratic chirp.

---

## 6. Exact surviving actual-prime theorem

After the block reduction, a closing input can be stated without ambiguity.
Uniformly for every retained companion block, every reduced approximant in

```text
Y^beta<q<=Y/sqrt(t),       Y^.8406<=t<=Y,             (6.1)
```

prove a fixed-power bound for the smoothly chirped selected statistic

```text
1/phi(q) sum_(chi nonprincipal)
 tau_q(chibar;r) C_(q,H)^sym(chi),                    (6.2)
```

with saving `c>kappa`, or prove an equivalent direct `z=0` consecutive-gap
dispersion theorem.  Vaughan handles the natural `Lambda` comparator;
(6.2) is the unproved transfer interface.

The numerical exponent ledger is checked by

```bash
python3 results/verify_zeta23_curvature_block_transfer.py
```
