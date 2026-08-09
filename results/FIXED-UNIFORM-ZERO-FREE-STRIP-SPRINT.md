# Fixed uniform zero-free strip sprint

Status: exact fourth-moment-to-strip theorem, complete four-shift reduction,
center-annihilator audit, and finite short-orbit falsification; 2026-08-06.
No fixed uniform zero-free strip is proved here.  The one remaining arithmetic
input is isolated below.

## 1. Verdict

The sprint did not produce a new zero-free strip.  It did produce a clean,
quantitative theorem saying exactly what would produce one.

Let `R=log X`.  On every admissible regular frozen-cutoff block `I`, retain
the complete R71 field

```text
g_I(R)=chi_I(R)G_I(R),
F_I(t)=Fourier[g_I](t),                                  (1.1)
```

including every boundary-intersecting grouped product and the whole
rank-two or exact Type-I center.  Fix a derivative order `q>=1`.  If, for
some fixed `kappa>0`,

```text
integral_R abs(F_I(t))^4 dt
 <=exp((2-kappa+o(1))R)                                 (1.2)
```

uniformly on every sufficiently large regular block, then

```text
Delta<=1/2-kappa/4,
Re(rho)<=1-kappa/4.                                     (1.3)
```

This sharp implication uses the whole real-frequency moment in (1.2).  If
the fourth moment is controlled only on an optimized finite height window,
the fixed-order Sobolev fallback below gives the weaker width
`eta=qkappa/(4q+1)`.

This is a real graduated target.  Any `kappa>0` gives a genuine fixed strip.
For the finite-height fallback, the conversion is

| derivative order `q` | height exponent `tau` | strip width `eta` |
|---:|---:|---:|
| 1 | `kappa/5` | `kappa/5` |
| 2 | `kappa/9` | `2kappa/9` |
| 4 | `kappa/17` | `4kappa/17` |

The formal fixed-order ceiling as `q` becomes large is `eta=kappa/4`.  The
Euler constants are now uniform by the imported fixed-step lemma; a
varying-order argument would still require uniform Sobolev/localization and
blockwise-converse estimates.

Three candidate shortcuts were tested.

1. The independent-phase and exact-product Haar comparators do not dominate
   the completed short-orbit moment, even in a faithful finite block.
2. A second difference which exactly kills the rank-two center is elliptic
   and boundedly invertible on the real Fourier axis.  It changes
   coordinates but creates no power saving.
3. Exact product grouping makes the pair diagonal only `X^o(1)`, but the
   unresolved near-product terms still cost `X^(2+o(1))` under known generic
   mean-value estimates.

Thus the surviving statement is not “bound the diagonal.”  It is a signed,
coefficient-specific local equidistribution theorem for near-products,
including their cross terms with the center.

## 2. Exact fourth-moment-to-strip theorem

### Theorem 2.1

Let `G` be the fixed-order exact completed coboundary detector, and fix a
nonzero `chi` in `C_c^infinity`.  For its continuous translates put

```text
g_R(u)=chi(u)G(R+u),
F_R(t)=Fourier[g_R](t),
U_p(R)=integral_R abs(F_R(t))^pdt,       2<=p<infinity.  (2.1)
```

Subject to the same absolutely convergent fixed-window explicit formula as
the R71 energy theorem,

```text
limsup_(R->infinity) log(1+U_p(R))/R=p Delta.            (2.2)
```

For an expanding regular-block partition the same exponent holds provided
the blocks cover every sufficiently large translate, have a fixed-width
core on which their weights are bounded below, and have only `exp(o(R))`
support and weight losses.  In particular, a uniform every-block estimate

```text
U_4(I)<=exp((2-kappa+o(1))R_I)                           (2.3)
```

implies (1.3).  More generally,

```text
U_(2m)(I)<=exp((m-kappa+o(1))R_I)
 => Re(rho)<=1-kappa/(2m).                               (2.4)
```

#### Proof

The fixed-window zero expansion gives, for every `epsilon>0`,

```text
G(R+u)=O_(chi,epsilon)(exp((Delta+epsilon)R))             (2.5)
```

uniformly for `u` in the support of `chi`.  Hausdorff--Young therefore gives

```text
norm(F_R)_p<=C_(p,chi)norm(g_R)_(p')
            <=exp((Delta+epsilon)R),                     (2.6)
```

so the limsup in (2.2) is at most `p Delta`.

For the reverse inequality, fix a zero carrier
`lambda_0=rho-1/2` with `delta=Re(lambda_0)>0`.  Choose
`phi` smooth and supported where `chi` is nonzero such that

```text
Phi(lambda_0)=integral phi(u)exp(lambda_0 u)du !=0.      (2.7)
```

A sufficiently small bump always does this.  Set
`conjugate(h)=phi/chi`.  Fourier duality and Holder give

```text
abs(integral phi(u)G(R+u)du)
 <=(1/(2pi))norm(hat(h))_(p') U_p(R)^(1/p).              (2.8)
```

If the limsup in (2.2) were below `p delta`, the scalar on the left of
(2.8) would have exponential growth strictly below `delta`.  Its one-sided
Laplace transform would consequently be holomorphic across
`lambda_0`.  But the fixed-window explicit formula gives there a genuine
pole with residue equal to the nonzero zero-carrier coefficient times
`Phi(lambda_0)`.  Archimedean and pole-center corrections are holomorphic at
that point.  This is a contradiction.  Taking the supremum over zero
displacements proves (2.2); a rightmost zero is not required.

On a regular block, use `phi` inside its fixed-width core in (2.8).  The
Fourier norm of `h` is translation invariant and uniform.  The block support
and weight losses are subexponential, so (2.6) is unchanged at exponent
scale.  This proves the block statement.  The exact Type-I head makes the
identity cutoff independent; the fixed-order explicit-center Euler defect
is `exp(o(R))` and does not affect a positive saving.

### Theorem 2.2 (finite-height fallback)

Assume that, for some fixed positive integers `q,k` with `k>=q+2`, every
sufficiently large admissible regular block satisfies

```text
norm(g_I^(q))_2^2<=exp((1+o(1))R).                      (2.9)
```

Suppose there is a fixed `0<kappa<2` such that

```text
U_4(I;abs(t)<=T_R)
      <=exp((2-kappa+o(1))R)                            (2.10)
```

uniformly on those blocks at the optimized height below.  Then
`Re(rho)<=1-qkappa/(4q+1)`.

#### Proof

Put

```text
T_R=exp((tau+o(1))R).                                   (2.11)
```

Hölder on the inner frequency window gives

```text
integral_(abs(t)<=T_R) abs(F_I(t))^2dt
 <=(2T_R)^(1/2)U_4(I)^(1/2)
 <=exp((1-kappa/2+tau/2+o(1))R).                        (2.12)
```

The fixed-order Sobolev tail and (2.9) give

```text
integral_(abs(t)>T_R) abs(F_I(t))^2dt
 <=2pi T_R^(-2q)norm(g_I^(q))_2^2
 <=exp((1-2q tau+o(1))R).                               (2.13)
```

Balance the two exponents:

```text
tau=kappa/(4q+1).                                       (2.14)
```

Plancherel now yields the completed block-energy estimate

```text
norm(g_I)_2^2
 <=exp((1-2q kappa/(4q+1)+o(1))R)
 = exp((1-2eta+o(1))R),
eta=qkappa/(4q+1).                                      (2.15)
```

There are only `exp(o(R))` regular blocks in the R71 extraction.  Summing
(2.15), and using the fixed-order exact-head transfer already required by
R71, gives the same exponent for the cumulative scale energy.  The exact
R71 energy law

```text
limsup log(1+energy up to R)/(2R)=Delta                 (2.16)
```

then gives `Delta<=1/2-eta`.  Since a zero
`rho=1/2+delta+i gamma` has `delta<=Delta`, symmetry gives
`Re(rho)<=1-eta`.  This proves the theorem.

### Even-moment variant

The same calculation is not special to four.  If, for a fixed integer
`m>=2`,

```text
integral_(abs(t)<=T_R) abs(F_I)^(2m)
 <=exp((m-kappa+o(1))R),                                (2.17)
```

then Hölder and the same Sobolev tail balance at

```text
tau=kappa/[m(2q+1)-1],
eta=q kappa/[m(2q+1)-1].                                (2.18)
```

For the sixth moment this denominator is `6q+2`.  This is included because
the finite probe audits moments four and six.  It does not make the sixth
moment an easier arithmetic target; its complete expansion contains still
more unresolved product relations.

### Quantifier warning

The fourth-moment bound must hold on every regular block, not merely almost
all blocks.  A hypothetical off-line carrier is extracted only along a
subsequence.  For the finite-height fallback, a fixed bounded `t` interval
is also insufficient: (2.10) must hold at least out to (2.11) with (2.14).

## 3. Alternative minimum exceptional-set gate

The R75 width analysis gives a second exact formulation.  To target
`Re(rho)<=1-eta`, put

```text
d_0=1/2-eta,
alpha_0=d_0-eta/(2q).                                   (3.1)
```

Choose a fixed `q` for which `alpha_0>0`.  It is enough to prove, for every
small fixed `epsilon>0`,

```text
measure{abs(t)<=exp((eta/q+epsilon)R):
        abs(F_I(t))>=exp((alpha_0-epsilon)R)}
 =o(1/H_I)                                              (3.2)
```

uniformly on every sufficiently large regular block.  Indeed a zero with
displacement greater than `d_0` produces, after fixing a displacement
strictly between them, an exceptional set of size `gg 1/H_I` above the
threshold in (3.2).

This formulation is useful for importing a future large-values theorem.
Markov turns a sufficiently strong `U_4` estimate into (3.2); at the displayed
threshold it requires `kappa>4eta+2eta/q`.  The sharper conversion in
Theorem 2.1 instead uses Hölder on the whole inner `L2` mass and requires
only `kappa=eta(4q+1)/q`.  Neither estimate is currently known for the
completed coefficient.

## 4. The exact complete four-shift form

Write the grouped tail transform as

```text
T(t)=sum_n c_n Phi_n(t),
Phi_n(t)=integral_I chi_I(R)V(R-log n)exp(-itR)dR
        =n^(-it)K_n(t),                                 (4.1)
```

where

```text
K_n(t)=integral chi_I(log n+u)V(u)exp(-itu)du.           (4.2)
```

Boundary profiles are retained through the `n` dependence of `K_n`.  Let

```text
Z(t)=[alpha J_chi(1/2-it)+beta J_chi'(1/2-it)]/norm(W)_2,
F_I=T-Z.                                                (4.3)
```

Augment the index set by the center channels and write
`F_I=sum_a d_a Phi_a`.  Then, on any frequency interval `J`,

```text
U_4(I;J)
 =sum_(a,b,c,d)d_a conjugate(d_b)d_c conjugate(d_d)
   Q_((a,c),(b,d)),                                     (4.4)

Q_((a,c),(b,d))
 =integral_J Phi_a(t)Phi_c(t)
             conjugate(Phi_b(t)Phi_d(t))dt.             (4.5)
```

Thus `Q` is a positive semidefinite pair Gram matrix, while its individual
tail, boundary, and center sectors have no useful sign.

There is an even cleaner exact physical-space form.  With `g=g_I`,

```text
integral_R abs(F_I(t))^4dt=2pi norm(g*g)_2^2.            (4.6)
```

Consequently the desired theorem is precisely an `L2` power saving for the
self-convolution of the completed prime discrepancy.  It is not a moment
of a tail polynomial with the center appended later.

For a finite window `J=[t_0-T,t_0+T]`, put `q_I=g*g`.  Then

```text
U_4(I;J)
 =double_integral q_I(u)conjugate(q_I(v))
   exp(-it_0(u-v)) 2sin(T(u-v))/(u-v) du dv,             (4.7)
```

with the diagonal value interpreted by continuity.  Formula (4.7) displays
the near-product resolution barrier directly.

## 5. Product grouping localizes the obstruction

Squaring only the tail gives the exact grouping

```text
T(t)^2=sum_m m^(-it)B_m(t),
B_m(t)=sum_(uv=m)c_u c_v K_u(t)K_v(t).                  (5.1)
```

Hence

```text
integral_J abs(T(t))^4dt
 =sum_(m,l)integral_J B_m(t)conjugate(B_l(t))
                    (m/l)^(-it)dt.                     (5.2)
```

On the safe interior, the profile is common.  The pair coefficient becomes

```text
b_m=m^(-1/2)sum_(uv=m)a_Y(u)a_Y(v).                     (5.3)
```

The divisor bound `abs(a_Y(n))<=tau_3(n)log n` gives

```text
sum_m abs(b_m)^2=X^o(1).                                (5.4)
```

The same divisor estimate keeps the boundary pair diagonal
subexponential.  This is a useful simplification: exact multiplicative
collisions are not the exponential obstruction.

The off-diagonal is different.  The pair labels have size about `X^2`, so
adjacent log frequencies can be spaced at scale `X^(-2)`.  The required
height is only `T=X^tau`, with `tau<1/2` in Theorem 2.1.  Approximately
`X^2/T` pair labels remain unresolved inside one Fourier cell.  The ordinary
mean-value or large-sieve estimate therefore has the shape

```text
(T+X^2)sum_m abs(b_m)^2=X^(2+o(1)),                     (5.5)
```

which is exactly `kappa=0`.

The rank-two center cannot be bounded sectorwise: its separate fourth
moment and its tail cross terms live at the same `X^2` scale.  Any saving
must occur after the atomic pair measure and the continuous center-pair
measure have been combined.

The smallest surviving arithmetic formulation is therefore:

> Prove that the completed pair measure has `L2` mass
> `O(X^(2-kappa+o(1)))` for one fixed `kappa>0`, uniformly on every
> regular frozen-cutoff block, at resolution `1/T` with
> `T=X^(kappa/(4q+1))`.

This is a signed local equidistribution theorem for near-products, not an
exact-product energy theorem.

## 6. Why Haar or independent phases do not transfer

For channel values `z_j(t)`, the independent-phase comparators are exactly

```text
E abs(sum_j exp(i theta_j)z_j)^4
 =2S_2^2-S_4,                                           (6.1)

E abs(sum_j exp(i theta_j)z_j)^6
 =6S_2^3-9S_2S_4+4S_6,                                 (6.2)
```

where `S_r=sum_j abs(z_j)^r`.  A collision-aware comparator additionally
groups every pair or triple monomial with the same integer product.

The faithful finite probe retains every boundary product and the signed
center.  At

```text
X=127, Y=8, T=80,                                       (6.3)
```

it gives

| comparator | fourth-moment ratio | sixth-moment ratio |
|---|---:|---:|
| independent phases | `1.6334823915` | `1.7162258774` |
| exact-product collision aware | `1.5947043586` | `1.6235788308` |

The ratios are completed short-orbit moment divided by comparator moment.
Exact collisions such as

```text
110*143=121*130,
117*154=126*143                                      (6.4)
```

are included.  They do not explain the excess.  The dominant effect is
coherence among unequal but Fourier-unresolved products.

This is D-rated finite evidence, not an asymptotic lower bound.  It is a
valid fail-fast rejection of the proposed universal finite domination
inequalities.  A theorem special to the actual Mobius--Vaughan coefficient
remains logically possible.

There is also an analytic generic obstruction.  On an interior block,
coefficients of the form

```text
c_n=X^(-1/2)f(log(n/X))                                 (6.5)
```

can satisfy any two prescribed center-moment constraints while retaining a
nonzero Mellin value at a real frequency.  Their exact-product Haar energy
is `X^o(1)`, but their short-orbit fourth moment is `gg X^2` on a fixed
frequency neighborhood.  Coefficient size, exact-product energy, and two
center constraints therefore cannot imply the required transfer.

## 7. The center-annihilator is exact but elliptic

For fixed `h>0`, define

```text
(tau_h f)(R)=f(R+h),
c=exp(h/2),
Q_h=(tau_h-c)^2.                                        (7.1)
```

Then

```text
Q_h exp(R/2)=0,
Q_h(R exp(R/2))=0.                                      (7.2)
```

Thus `Q_h` exactly kills the displayed rank-two center.  On an exponential
carrier it acts by

```text
Q_h exp(sR)=q_h(s)exp(sR),
q_h(s)=(exp(hs)-exp(h/2))^2.                            (7.3)
```

For a zero carrier `s=rho-1/2`, this multiplier can vanish only when

```text
rho=1+2pi i m/h.                                        (7.4)
```

The classical zero-free line `Re(rho)=1` excludes (7.4).  Hence `Q_h`
preserves every nontrivial zero carrier and its exponential displacement.

On the real Fourier axis,

```text
(c-1)^2<=abs(q_h(it))<=(c+1)^2.                         (7.5)
```

In particular `Q_h` is boundedly invertible in global `L2`, with

```text
Q_h^(-1)
 =exp(-h)sum_(j>=0)(j+1)exp(-jh/2)tau_h^j.              (7.6)
```

The same series and Minkowski transfer any block fourth-moment power saving
with exponent strictly below `2` back to the original completed field.
Thus `Q_h` cannot manufacture the desired `kappa`; it is a clean
center-free coordinate in which one may try to prove it.

Three bookkeeping qualifications matter.

1. The primitive center contains a bounded constant which `Q_h` does not
   kill.  It is harmless at every positive exponential scale.
2. The exact unevaluated Type-I head is not annihilated.  At fixed order its
   Euler defect is `exp(o(R))`; the R71 transfer is now proved uniformly on
   the regular growing-order schedule as well.
3. Localization must follow the difference.  In general

```text
Q_h(chi G)-chi Q_hG
 =[chi(R+2h)-chi(R)]G(R+2h)
 -2c[chi(R+h)-chi(R)]G(R+h).                            (7.7)
```

The commutator lives on boundary collars at the raw unknown scale.
Overlapping frozen-cutoff blocks with a `2h` safety margin avoid estimating
it absolutely.

The differential analogue `(D-1/2)^2` has the same defect: its real-axis
multiplier is bounded below, and its localization commutator restores the
raw field.  Neither operator is a real low-frequency wavelet.

## 8. Current literature reality check

The versioned primary-source survey and exact R71 normalization now live in
[`publication/IMPORTED-ANALYTIC-BASELINE.md`](../publication/IMPORTED-ANALYTIC-BASELINE.md).
The comparisons below are retained as the branch-local subset.

The strongest unconditional zero-free regions remain of
Vinogradov--Korobov type: their boundary tends to `1` with height rather
than staying to the left of one fixed vertical line.  For example,
[Bellotti's explicit result](https://arxiv.org/abs/2306.10680) gives the
asymptotic boundary

```text
1-1/[48.0718(log t)^(2/3)(log log t)^(1/3)].            (8.1)
```

A fixed strip `Re(rho)<=1-eta` would therefore be a qualitative
breakthrough, not a small numerical improvement of (8.1).

[Guth--Maynard's large-value theorem](https://arxiv.org/abs/2405.20552)
substantially improves generic Dirichlet-polynomial large values and zero
density.  [Matomaki--Teravainen](https://arxiv.org/abs/2403.13157) show
important implications in the reverse direction between zero density and
large values.  These results do not state the every-block completed
fourth-moment estimate (2.3).

Likewise, current shifted-von-Mangoldt and higher-uniformity theorems give
almost-all-shift or almost-all-interval results with logarithmic or
`o(1)` savings; see
[Matomaki--Radziwill--Tao](https://arxiv.org/abs/1707.01315) and
[Matomaki--Radziwill--Shao--Tao--Teravainen](https://arxiv.org/abs/2411.05770).
After matching their quantifiers and norms to (2.3), they do not furnish a
fixed `kappa>0` uniformly on every carrier block.  This last sentence is the
conclusion of the present reduction audit, not a theorem asserted by those
papers.

## 9. Research disposition

The fourth-moment route survives, but only in its complete form.

* **Proved exactly at exponent scale:** (2.2), hence (2.3) implies the
  explicit strip (1.3).
* **Small diagonal:** exact pair collisions contribute only `X^o(1)`.
* **Closed shortcuts:** independent-phase domination, exact-product Haar
  domination, coefficient-blind restriction, and center annihilation as a
  source of contraction.
* **Open arithmetic theorem:** cancellation among unequal near-products and
  the continuous center at resolution `1/T`, uniformly on every regular
  block.

The best experimental coordinate is `Q_hG`, because its rank-two center is
absent and its inverse is explicit.  The best proof coordinate is still the
exact pair convolution (4.6), because it exposes which atomic--continuous
cross terms must cancel.  A successful proof must use a property of the
actual Mobius--Vaughan coefficient not shared by the generic example (6.5).

## 10. Reproducibility

The D-rated completed-moment scout is
[`src/r71_fixed_strip_moment_probe.py`](../src/r71_fixed_strip_moment_probe.py),
with focused tests in
[`src/test_r71_fixed_strip_moment_probe.py`](../src/test_r71_fixed_strip_moment_probe.py).
It verifies channel closure before computing any moment, retains all
boundary profiles and the signed center, and implements both exact phase
formulas and exact multiplicative collision grouping.

Run

```text
PYTHONPATH=src python3 -m pytest -q \
  src/test_r71_fixed_strip_moment_probe.py

PYTHONPATH=src python3 src/r71_fixed_strip_moment_probe.py \
  --scales 127 --cutoffs 8 \
  --stress-scales 127 --stress-cutoffs 6 8 \
  --heights 40 --long-height 80 --frequency-step 0.5 \
  --gaussian-order 12
```

The calculation falsifies finite domination guesses.  It does not estimate
an asymptotic exponent and is not evidence that a fixed strip is true or
false.

The follow-up
[`FIXED-STRIP-FOURTH-MOMENT-PROOF-ATTEMPT.md`](FIXED-STRIP-FOURTH-MOMENT-PROOF-ATTEMPT.md)
proves the sharper full-moment identity
`limsup log(1+U_p(R))/R=p Delta`, reduces mesoscopic cells to an equivalent
pair-PNT variance, and closes proportional-order scale filtering.  It does
not prove the missing fixed `kappa`.
