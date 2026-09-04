# Global mixed-depth Pick attack and the Carleson quantifier wall

Status: exact global affine-screen theorem, exact reflected-pair Poisson
functional, reproducible four-parameter optimization, positive-convolution
diagnostic, and primary-literature audit, 2026-08-13.  The global compact
Pick gate remains **open**.  No zero-free strip or RH statement is proved.

## 1. Binary verdict

The one-cell growing-Taylor-jet construction is already excluded by its
`4^(r-o(r))` capacity defect.  This note therefore tests a genuinely global
mixed-depth alternative: two exact finite-difference chains running through
`Theta(L)` phase cells along a segment whose physical horizontal depth varies
by `Theta(1)`.

For every such affine segment the forced Schur attenuation and its complete
pointwise reflected-pair Poisson load have closed formulas.  A reproducible
four-parameter search over segment depth, ordinate width, slope, and ordinate
offset gives

```text
largest attenuation found       .013984923822840388 L,
available GP surcharge           .0253912552074952   L,
gap below surcharge              .011406331384654812 L.       (1.1)
```

The optimizer is, to numerical precision,

```text
center depth b                   .4709446178315,
ordinate width H                 .0377065906692,
depth slope s                    0,
ordinate center v0               0,
pointwise Poisson load           .5000000000000.               (1.2)
```

Thus allowing an `O(1)` depth drift does **not** revive the binomial
obstruction: five independent global searches return the old centered,
equal-depth endpoint.  The formulas below are theorem-grade; (1.1)--(1.2)
are a floating global-search result, not an interval proof that no other
affine point exists.  In particular, an obstruction below the surcharge is
not an upper construction and does not prove GP.

The literature audit also isolates a precise missing theorem.  Classical
Carleson, Paley--Wiener, divided-difference, and Beurling--Malliavin results do
not convert the present Poisson cap into the needed compact Schur state.  They
require separation, a fixed `N`-Carleson cluster bound, a Muckenhoupt
condition, or merely decide qualitative Toeplitz-kernel nontriviality.  The
actual triangular array permits `N_L=Theta(L)` rows in one microscopic cell,
and GP needs an exponentially calibrated target value and a compact causal
two-leg realization.

## 2. A global sloped finite-difference screen

Fix

```text
alpha=.49,       d=.66,       D=dL,
K/L -> c>0,      H=pi*c/d.                              (2.1)
```

Let `b` be the center depth, `s` the horizontal slope per unit ordinate, and
`v0` the center ordinate.  Put

```text
z(x)=b+s*H*(x-1/2)-i*[v0+H*(x-1/2)],     0<=x<=1.       (2.2)
```

Take the two interlaced chains `x=n/K` and `x=(n+1/2)/K`.  The phase increase
between consecutive points is exactly `pi+o(1)`; harmless endpoint rounding
can make it exact for every `L`.  The physical depth range is

```text
b-sH/2 <= Re z <= b+sH/2.                              (2.3)
```

Unlike the retired growing-jet fixture, this screen spans a fixed ordinate
interval and may span a fixed horizontal-depth interval.  It is not confined
to one microscopic Taylor cell.

Write

```text
w=H*(s-i),
t_*=1/2+(alpha-b+i*v0)/w,
R=max{|z(0)-alpha|,|z(1)-alpha|}.                     (2.4)
```

Then `z(x)-alpha=w*(x-t_*)`.  The target parameter `t_*` is off `[0,1]`
whenever the target is not on the segment.

## 3. Exact affine-screen attenuation

Define

```text
J(t)=1+integral_0^1 log|t-x| dx
    =Re{t Log t-(t-1)Log(t-1)}.                       (3.1)
```

### Proposition 3.1

Assume the whole segment lies in the right half-plane, its depths lie in the
live interval `[alpha*d,alpha]`, and `R<alpha`.  If a right-half-plane Schur
function `U` satisfies all half-disk signs on the two interlaced chains, then

```text
limsup_(L->infinity) L^(-1)log|U(alpha)| <=-F,

F=(dH/pi)*{log[alpha/(2R)]-J(t_*)}.                  (3.2)
```

#### Proof

Taylor-expand `U` at `alpha` through degree `K-1`.  Since the segment is in a
disk of radius `R<r<alpha`, the uniform remainder is

```text
epsilon_L <=[R/r+o(1)]^K/[1-R/r+o(1)].              (3.3)
```

Along either chain the node is affine in `n`, while its half-disk normal
alternates by `(-1)^n`.  Therefore the positive binomial sum of the real row
margins vanishes for the Taylor polynomial.  Every exact row margin is
nonnegative, so the polynomial margins obey

```text
|q_n| <=2^K*epsilon_L/binom(K,n).                    (3.4)
```

The first chain controls one real projection and the half-step chain controls
the orthogonal projection.  Lagrange interpolation back to `t_*` gives

```text
|U(alpha)|
 <=K^C*2^K*epsilon_L*exp{K*J(t_*)+o(K)}.            (3.5)
```

Here (3.1) is the Stirling limit of the exact complex Lagrange product; it is
the continuation factor which cannot be omitted when the target is off the
chain.  Let `r` tend to `alpha` and use `K/L->dH/pi` to obtain (3.2).  QED

For `s=v0=0`, (3.1)--(3.2) reduce exactly to the previously audited centered
formula

```text
J(1/2+i*y)
 =(1/2)log(1/4+y^2)+2y*atan(1/(2y)).                 (3.6)
```

Thus the new calculation strictly contains the old equal-depth screen.

## 4. Exact pointwise reflected-pair load

Put

```text
K_b(u)
 =(1/2-b)/[(1/2-b)^2+u^2]
  +(1/2+b)/[(1/2+b)^2+u^2].                         (4.1)
```

The two chains in (2.2) have combined ordinate density `2dL/pi`.  Hence their
leading completed-Poisson load at ordinate `t`, divided by `L`, is

```text
P_(b,H,s)(t)
 =(2d/pi)*integral_(-H/2)^(H/2)
       K_(b+s*v)(t-v) dv.                           (4.2)
```

An abstract screen compatible with the actual reflected-zero Poisson identity
must satisfy

```text
sup_t P_(b,H,s)(t)<=1/2.                            (4.3)
```

The offset `v0` only translates the maximizer of (4.2).  For `s=0`, the
maximum is at the segment center and (4.2) becomes the earlier exact formula

```text
(4d/pi)*{
 atan[H/(2(1/2-b))]+atan[H/(2(1/2+b))]}.            (4.4)
```

Equations (3.2) and (4.2), not a window-count surrogate, are what the
optimizer evaluates.  Both horizontal members of every reflected pair are
charged.

## 5. Optimization and hostile interpretation

The search domain was

```text
alpha*d <= b+s*v <= alpha       (-H/2<=v<=H/2),
R<alpha,
sup_t P(t)<=1/2.                                      (5.1)
```

Differential evolution was run with seeds

```text
1, 17, 313, 230813, 999983,                           (5.2)
```

and the active centered face was optimized independently by one-dimensional
root finding.  Every run returned (1.1)--(1.2).  Sloping the segment has two
competing effects: it changes the complex continuation point `t_*`, but it
also increases the far endpoint radius and moves a portion of the rows toward
the expensive right boundary in (4.1).  In the numerical extremal these
effects favor zero slope.

The logically valid conclusions are deliberately narrow.

1. Proposition 3.1 proves the attenuation formula for every affine mixed-depth
   screen.
2. Equation (4.2) is the exact necessary pointwise Poisson charge.
3. No point found in a reproducible multi-start search exceeds the surcharge.
4. The numerical maximum is not an interval-certified universal maximum.
5. Even a certified maximum below the surcharge would only eliminate this
   lower-obstruction family; it would not construct the GP interpolant.

## 6. Positive-convolution screens do not show a hidden win

The next sparse global family replaces the binomial measure by the positive
convolution

```text
(1+z+z^2)^K,
z=exp(-2*pi*i/3).                                    (6.1)
```

Its moment functional has a zero of order `K`, and its `2K+1` coefficients
give one rotating chain of real half-space rows.  This is attractive because
the number of real rows is close to the `2K` real dimensions of a complex
degree-`K-1` polynomial.

The attraction is illusory in the tested range.  The positive dependence
controls row `n` only by the inverse trinomial probability.  A Chebyshev-basis
linear program computing the resulting target-evaluation norm gives a
continuation charge about `1.9K` near the relevant geometry.  A coarse search
then peaks near

```text
forced attenuation approximately .009 L,             (6.2)
```

below even the affine binomial value.  This is only a floating diagnostic;
it is included to prevent (6.1) from being mistaken for a free factor-of-two
improvement.  No theorem in this note depends on (6.2).

## 7. The Poisson cap does not imply a fixed-`N` Carleson theorem

The quantifier mismatch can be made exact.  Fix a live depth `b=.47`, let

```text
N_L=floor(.01L),
delta_j=(j-(N_L-1)/2)/L^3.                          (7.1)
```

These are distinct nodes in an ordinate interval of width `O(L^-2)`.  Since
every translate of the reflected-pair kernel is at most its centered value,
their complete pointwise load satisfies

```text
L^(-1) sup_t sum_j K_b(t-delta_j)
 <=.01*{1/(.5-.47)+1/(.5+.47)}
 =.3436426116... <1/2.                              (7.2)
```

Thus the triangular array obeys the same necessary Poisson ceiling used by
GP.  Nevertheless, it cannot be partitioned into any fixed number `N0` of
uniformly separated subsequences with constants independent of `L`.  Among
any `N0+1` consecutive nodes, two have the same color; their ordinate gap is
at most `N0/L^3`, and their right-half-plane pseudohyperbolic distance is at
most

```text
[N0/L^3]/sqrt{(2b)^2+(N0/L^3)^2} ->0.              (7.3)
```

This is a rigorous no-go for importing a fixed-`N` Carleson interpolation
constant from the Poisson cap alone.  It is **not** a GP counterexample: the
phases and values of these nearly coincident rows are nearly identical and
may be coherently redundant.  A successful theorem must exploit exactly that
compatibility instead of treating the rows as arbitrary interpolation data.

## 8. What the primary literature actually supplies

The most relevant classical machinery does not fill the remaining quantifier.

* Carleson's [bounded interpolation theorem](https://doi.org/10.2307/2372840)
  characterizes `H^infinity` interpolation by uniform separation.  The
  completed Poisson bound is an upper mass bound, not a separation theorem,
  and permits a growing microscopic cluster.
* Lyubarskii and Seip,
  [*Complete interpolating sequences for Paley--Wiener spaces and
  Muckenhoupt's (A_p) condition*](https://arxiv.org/abs/math/9511212),
  characterize complete interpolation using separation/generating-function
  and Muckenhoupt control.  Neither condition follows from (4.3).
* Gaunard,
  [*Divided Differences & Restriction Operator on Paley--Wiener Spaces for
  N-Carleson Sequences*](https://arxiv.org/abs/1104.2141), extends the trace
  theory to finite unions of `N` Carleson sequences and uses divided
  differences inside the groups.  Its hypothesis fixes `N` and still requires
  a generating entire function plus a continuous or discrete Muckenhoupt
  condition.  Here the allowed triangular array has `N_L=Theta(L)` and no
  uniform `A_p` certificate.
* Avdonin and Ivanov,
  [*Exponential Riesz bases of subspaces and divided
  differences*](https://arxiv.org/abs/math/0103160), treat close exponential
  groups through divided differences.  Their Riesz-basis/subspace geometry is
  not a bound for the half-disk target extremal, and it supplies neither the
  `exp(o(L))` triangular-array conditioning nor compact two-leg support.
* Makarov and Poltoratski,
  [*Beurling--Malliavin theory for Toeplitz
  kernels*](https://arxiv.org/abs/math/0702497), compute a critical type for
  qualitative nontriviality of Toeplitz kernels from an effective-density
  condition.  Their theorem decides whether a nonzero Hardy/Smirnov function
  exists after an epsilon type shift.  It does not prescribe the present
  interior half-disks, lower-bound the normalized value at `alpha`, or put the
  inverse transform into the two required compact endpoint layers.
* Sarason,
  [*Generalized interpolation in H-infinity*](https://doi.org/10.1090/S0002-9947-1967-0208383-8),
  gives the exact finite compressed-shift criterion.  It does not bound the
  growing compressed-shift norm from (4.3) alone.

The distinction is structural, not bibliographic.  Density/type theorems say
whether some function exists.  GP needs the much stronger exponential
normalization

```text
-log|U(alpha)| <=(.3234-epsilon)L                   (8.1)
```

together with all interior signs and a compact physical realization.

## 9. Precise surviving lemma

The literature and the new calculation reduce the live gap to the following
triangular-array statement.

> **Growing-multiplicity compact half-disk lemma.**  For every candidate-local
> reflected list satisfying the pointwise completed-Poisson cap, including
> clusters with `N_L=Theta(L)` and mixed depths in `[alpha*d,alpha]`, construct
> one scalar two-leg compact causal Schur state satisfying every phase-tied
> half-disk, with (8.1), uniformly in the list.  The proof must control the
> target normalization, reverse-endpoint leakage, and compact support with the
> same exponent.

It would be enough to prove a representative/divided-difference reduction
whose constants are `exp(o(L))` or whose explicit exponential cost is less
than `.025391255L` after the audited Green base.  A fixed-`N` Carleson theorem,
a qualitative BM type theorem, or an obstruction below the surcharge does not
imply this lemma.

## 10. Truth table

| assertion | verdict |
|---|---|
| affine mixed-depth attenuation formula (3.2) | **proved** |
| exact pointwise reflected-pair load (4.2) | **proved** |
| affine family is global rather than one-cell | **yes** |
| a searched affine mixed-depth obstruction exceeds `.025391255L` | **no** |
| the floating search certifies the global affine maximum | **no** |
| cubic-root positive convolution gives a larger obstruction | **no in the diagnostic; no theorem claimed** |
| classical Carleson/PW/BM theory supplies growing-multiplicity target control | **no** |
| the Poisson cap implies a fixed-`N` Carleson decomposition | **no**, by (7.1)--(7.3) |
| a compact GP upper construction has been proved | **no** |
| an admissible mixed-depth obstruction above the surcharge has been proved | **no** |
| GP or a zero-free strip is closed | **no** |

## 11. Reproduction

```bash
python3 src/test_mixed_depth_pick_screen.py
python3 results/verify_zeta23_mixed_depth_pick_screen.py
```

The verifier intentionally reports `gp_closed=false`.  `PASS` means that the
exact formulas, centered regression, Poisson cap, and stated floating optimum
replay; it does not mean that GP has been proved.
