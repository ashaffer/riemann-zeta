# ZETA23 R71 completion-preserving minor-arc triage

Date: 2026-09-03  
Registry: R187  
Status: two completion-preserving localization theorems proved; the global
fixed-power arithmetic estimate, a uniform zero-free strip, and RH remain open

Preflight:
[`zeta23_r71_minor_arc_triage_preflight_v1.json`](context/zeta23_r71_minor_arc_triage_preflight_v1.json)

Literature log:
[`zeta23_r71_minor_arc_literature_search_2026-09-03.json`](context/zeta23_r71_minor_arc_literature_search_2026-09-03.json)

## 0. Verdict

The requested minor-arc pass succeeds analytically and fails arithmetically in
a precise sense.

Two exact localizations are now available.

1. After representing the affine R71 center inside the same signed additive
   measure as the frozen Vaughan tail, the order-four compact B-spline makes
   the field selected by the complementary smooth multiplier
   `1-m(X^(99/100)xi)`

   \[
      m(X^{99/100}\xi)
   \]

   contribute only `X^(0.96+o(1))` to the complete energy, including its cross
   term with the retained principal band.  This is not a hard additive cutoff:
   the fixed transition lies between radii `X^(-99/100)` and
   `2X^(-99/100)`.
2. After localizing the *whole* completed field, a compact Gevrey-`s` block
   weight makes the Mellin two-frequency difference sector

   \[
      |u-t|>K R^s,\qquad s>1,
   \]

   smaller than any prescribed fixed exponential power when `K` is chosen
   once and for all.

For the frozen target `eta=1/100`, the desired energy exponent is

\[
  1-2\eta=\frac{49}{50}=0.98.                         \tag{0.1}
\]

Both localization errors lie strictly below `0.98`.  Consequently the full
R71 bound is equivalent, at exponent scale, to the bound for the completed
additive principal band, and also to its polylogarithmic Mellin-difference
near part.

This does **not** prove that principal-band bound.  It shows that the phrase
“prove the minor arcs first” had conflated three different objects.  The
analytic window tails are now controlled.  Primitive nonzero reciprocal
kernel response was already controlled in R87.  What remains is the signed
aggregation of high-denominator/high-determinant packets together with the
reducible faces, low-character projector, exact center, and all cross terms.
That remaining completed estimate is still uniform-strip strength.

No zero-free strip has been proved.

## 1. Frozen theorem passport

Fix

```text
eta=1/100,       ell=1,       k=4,       h=ell/k=1/4,
theta=theta_k=1/2-1/[4(k+1)]=9/20,
U_R=V_R=floor(exp(theta R)),       X=exp(R).            (1.1)
```

One may replace these numerical fixed-window choices by any fixed admissible
order at least four.  They are frozen here so that every exponent and
quantifier has one meaning.

Let

\[
 a=a_{U_R,V_R}=\mu_{>U_R}*\Lambda_{>V_R}*1,
 \qquad a+h=\Lambda,                                  \tag{1.2}
\]

and normalize

\[
 V=W_{h,k}/\lVert W_{h,k}\rVert_2.
\]

On a fixed translate about `R`, retain the complete field

\[
 G_R(r)=\sum_n\frac{a(n)}{\sqrt n}V(r-\log n)
       -z_R(r),
 \qquad
 z_R(r)=\frac{e^{r/2}(\alpha_R+\beta_Rr)}
                   {\lVert W_{h,k}\rVert_2}.          \tag{1.3}
\]

The exact Type-I head can be used instead.  Passing to (1.3) costs only the
already proved `X^o(1)` Euler defect at the endpoint; its induced energy and
cross terms are still power-below the `X^.98` target.  Every assertion below concerns all
sufficiently large translates of one fixed window; no almost-all, selected,
or subsequential replacement is licensed.

The target is

\[
 E_R=\int\psi_R(r)|G_R(r)|^2\,dr
       \le X^{49/50+o(1)}.                             \tag{1.4}
\]

By the audited fixed-window converse, (1.4) implies
`Delta<=49/100` and therefore

\[
  1/100\le\Re\rho\le99/100.                            \tag{1.5}
\]

It does not imply RH without a separate amplifier.

## 2. The affine center belongs to one additive measure

Put `N=||W_(h,k)||_2` and

\[
 J_0=\int V(v)e^{-v/2}\,dv,
 \qquad J_1=\int vV(v)e^{-v/2}\,dv.                   \tag{2.1}
\]

Here `J_0>0`.  Define

\[
 B_R=\frac{\beta_R}{NJ_0},\qquad
 A_R=\frac{\alpha_R}{NJ_0}
       +\frac{\beta_RJ_1}{NJ_0^2}.                    \tag{2.2}
\]

Then substitution `v=r-log t` proves the exact identity

\[
 z_R(r)=\int_0^\infty t^{-1/2}V(r-\log t)
                     (A_R+B_R\log t)\,dt.             \tag{2.3}
\]

Indeed, the right side equals

\[
 e^{r/2}\{A_RJ_0+B_RrJ_0-B_RJ_1\}
 =e^{r/2}(\alpha_R+\beta_Rr)/N.                       \tag{2.4}
\]

Thus, on the common active shell,

\[
 d\mu_R(t)=\sum_n a(n)\delta_n
            -(A_R+B_R\log t)\,dt,                    \tag{2.5}
\]

and with `f_r(t)=t^(-1/2)V(r-log t)`,

\[
             G_R(r)=\int f_r(t)\,d\mu_R(t).           \tag{2.6}
\]

This is completion-preserving: the hard Möbius--von Mangoldt coefficient and
the full affine Type-I center are one signed measure before Fourier inversion,
absolute values, or Cauchy--Schwarz.

## 3. Additive principal-band theorem

Choose one smooth shell cutoff `chi_0(t/X)` equal to one wherever any `f_r`
in the fixed block is supported, and replace (2.5) by its restriction through
that cutoff.  This does not change (2.6).  Put

\[
 P_R(\xi)=\int e(-\xi t)\,d\mu_R(t),
 \qquad e(x)=e^{2\pi ix}.                              \tag{3.1}
\]

Fourier inversion gives

\[
 G_R(r)=\int_{\mathbb R}\widehat f_r(\xi)P_R(-\xi)\,d\xi. \tag{3.2}
\]

Let `m` be a fixed even smooth function equal to one on `[-1,1]` and zero
outside `[-2,2]`.  With `nu=1/100`, split

\[
\begin{aligned}
 G_R^{\rm pri}(r)
   &=\int m(X^{1-\nu}\xi)\widehat f_r(\xi)P_R(-\xi)\,d\xi,\\
 G_R^{\rm tail}(r)&=G_R(r)-G_R^{\rm pri}(r).          \tag{3.3}
\end{aligned}
\]

### Theorem 3.1

Uniformly on every frozen fixed window,

\[
 \lVert G_R^{\rm tail}\rVert_\infty
       \le X^{1/2-4\nu+o(1)}=X^{0.46+o(1)},           \tag{3.4}
\]

and hence

\[
 \int\psi_R|G_R^{\rm tail}|^2\ll X^{0.92+o(1)},      \tag{3.5}
\]

while

\[
 \left|2\Re\int\psi_R G_R^{\rm pri}
                  \overline{G_R^{\rm tail}}\right|
       \ll X^{0.96+o(1)}.                             \tag{3.6}
\]

Consequently

\[
 E_R=\int\psi_R|G_R^{\rm pri}|^2
             +O(X^{0.96+o(1)}),                       \tag{3.7}
\]

so (1.4) holds if and only if

\[
 \int\psi_R|G_R^{\rm pri}|^2\,dr
       \le X^{0.98+o(1)}.                             \tag{3.8}
\]

#### Proof

The elementary coefficient and center bounds give

\[
 \sup_\xi|P_R(\xi)|
 \le\lVert\mu_R\rVert_{\rm TV}
 \le X^{1+o(1)}.                                     \tag{3.9}
\]

For the discrete part use
`|a(n)|<=tau_3(n)log n`; the continuum density in (2.5) is `R^O(1)` on a
shell of length `O(X)`.

Write `r=R+s` with `s` in a fixed compact interval and

\[
 f_r(Xy)=X^{-1/2}F_s(y),\qquad
 F_s(y)=y^{-1/2}V(s-\log y).                           \tag{3.10}
\]

The order-four compact window has a uniformly finite fifth distributional
derivative after this smooth change of variables.  Therefore

\[
 |\widehat F_s(\zeta)|\ll(1+|\zeta|)^{-5}.            \tag{3.11}
\]

Scaling and integration outside `|xi|>=X^(-1+nu)` give

\[
\begin{aligned}
 \int_{|\xi|\ge X^{-1+\nu}}|\widehat f_r(\xi)|\,d\xi
 &=X^{-1/2}\int_{|\zeta|\ge X^\nu}
             |\widehat F_s(\zeta)|\,d\zeta\\
 &\ll X^{-1/2-4\nu}.                                 \tag{3.12}
\end{aligned}
\]

Equations (3.9) and (3.12) prove (3.4).  Squaring proves (3.5).  The trivial
complete bound `G_R=O(X^(1/2+o(1)))` also gives that bound for the principal
part.  Cauchy--Schwarz now proves (3.6), and (3.7)--(3.8) follow.

For general fixed order `k`, the exponents in (3.5) and (3.6) are
`1-2k nu` and `1-k nu`.  The strict condition needed to preserve a target
`1-2eta` is `k nu>2eta`.

## 4. Mellin-difference localization theorem

This is a different Fourier coordinate.  Let `psi_R` be a translate of a
fixed real compact Gevrey-`s` plateau, `s>1`.  Choose a larger compact
plateau `chi_R=1` on `supp(psi_R)` and put

\[
 H_R=\chi_RG_R.                                       \tag{4.1}
\]

With the radian convention
`fhat(t)=integral f(r)exp(-itr)dr`, the complete energy is exactly

\[
 E_R=\frac1{(2\pi)^2}\iint
   \widehat\psi_R(u-t)\widehat H_R(t)
   \overline{\widehat H_R(u)}\,dt\,du.                \tag{4.2}
\]

Let `E_near(Omega)` and `E_far(Omega)` be the restrictions of (4.2) to
`|u-t|<=Omega` and its complement.

### Theorem 4.1

The split is exact and both terms are real.  Moreover,

\[
 |E_R^{\rm far}(\Omega)|
 \le\frac1{2\pi}
 \left\{\int_{|v|>\Omega}|\widehat\psi_R(v)|\,dv\right\}
 \lVert H_R\rVert_2^2.                                \tag{4.3}
\]

If

\[
 \lVert\psi_R^{(j)}\rVert_1
 \le C_0C_1^j(j!)^s,                                 \tag{4.4}
\]

then

\[
 \int_{|v|>\Omega}|\widehat\psi_R(v)|\,dv
 \ll \operatorname{poly}(\Omega)e^{-c\Omega^{1/s}}. \tag{4.5}
\]

Since the crude completed-field bound is

\[
 \lVert H_R\rVert_2^2\le e^{R+o(R)},                 \tag{4.6}
\]

taking `Omega=K R^s` gives

\[
 |E_R^{\rm far}|\le
 e^{(1-cK^{1/s}+o(1))R}.                              \tag{4.7}
\]

In particular, choose `K` so that `cK^(1/s)>4/100`; then the exponent in
(4.7) is below `0.96`, and the `0.98` target is equivalent to the same bound
for `E_near`.

#### Proof

Put
`k_far(v)=1_(|v|>Omega) psihat_R(v)`.  Treating (4.2) as the quadratic form
of convolution by `k_far`, Cauchy--Schwarz, Young's inequality, and
Plancherel give

\[
 \frac1{(2\pi)^2}\lVert\widehat H_R\rVert_2
 \lVert k_{\rm far}*\widehat H_R\rVert_2
 \le\frac1{2\pi}\lVert k_{\rm far}\rVert_1
                    \lVert H_R\rVert_2^2,             \tag{4.8}
\]

which is (4.3).  Integrating by parts `j` times gives

\[
 |\widehat\psi_R(v)|
 \le C_0C_1^j(j!)^s|v|^{-j}.                          \tag{4.9}
\]

Optimizing at `j` comparable with `|v|^(1/s)` proves (4.5).  Finally,
the same divisor bound used in (3.9), together with the affine center, gives
(4.6).

The exact near term depends on the auxiliary plateau `chi_R`.  This is
harmless but must be stated: for two admissible extensions,

\[
 |E_{{\rm near},1}-E_{{\rm near},2}|
 \le |E_{{\rm far},1}|+|E_{{\rm far},2}|.             \tag{4.10}
\]

Thus the near form is asymptotically canonical modulo the proved negligible
error, not literally canonical.  Without `chi_R`, the affine center is not a
global `L2` function and (4.2) is not a licensed completed split.

Compact Gevrey cutoffs exist for every fixed `s>1`, so the band can be
`R^(1+epsilon)` for any fixed positive `epsilon`.  One cannot set `s=1`
using a nonzero compactly supported analytic cutoff.  This is the ordinary
compact-support uncertainty boundary, not an arithmetic obstruction.

## 5. Hostile sign and completion audit

The hard difference split in Section 4 is Hermitian but not positive.  The
completed finite R71 diagnostic at

```text
X=127, Y=8, h=0.04, k=1, Omega=17.09975946676696       (5.1)
```

gives, stably at Gaussian quadrature orders `8` through `32`,

```text
complete energy       0.1277499014525
near contribution     0.1575199385126
far contribution     -0.02977003706009.                (5.2)
```

At order `24`, the far contribution decomposes as

```text
tail--tail            -0.0258842431099
tail--center          -0.00385966246150
center--center        -0.0000261314886710.              (5.3)
```

This is D-rated finite numerical evidence, not an asymptotic theorem.  It is
enough to falsify any proof which calls the far term a positive minor-arc
energy or allocates the center only after the split.

The executable audit also replays the exact cyclic finite-DFT identity and
checks its discrete Young bound before running (5.2).  See
[`r71_minor_arc_triage.py`](../src/r71_minor_arc_triage.py) and
[`test_r71_minor_arc_triage.py`](../src/test_r71_minor_arc_triage.py).

## 6. Why this does not close the arithmetic minor arcs

There are now three distinct ledgers.

| coordinate | controlled statement | unresolved statement |
|---|---|---|
| Mellin difference `u-t` | `|u-t|>K R^s` is negligible | the near form contains every zero self-pair |
| additive frequency `xi` | the complementary smooth multiplier `1-m(X^(99/100)xi)` contributes only `X^(.96+o(1))` including cross terms | the completed principal band |
| reciprocal/cofactor packets | primitive balanced kernel response is power-small in R87 | signed accumulation, axes, reducible faces, high determinants, and cross-cofactor completion |

A hypothetical off-line zero contributes a self-pair with `u` approximately
equal to `t`, so Theorem 4.1 deliberately leaves its carrier in the near
form.  In additive coordinates, the surviving band contains the zero axis
and rationals whose relevant denominators are at least `X^(99/100)`.

R87's pointwise reciprocal response bound cannot simply be summed.  The
cofactor expansion has a prescribed rectangular limiting order, its
coefficients are signed, and pointwise packet smallness has no aggregation
content: `N` packets of size `1/N` can sum to one.  The all-sector
recombination is exactly the original positive R71 energy.

The reducible face cannot be called an elementary major term either.  Its
Dirichlet series contains `1/zeta` and `zeta'/zeta^2`; a fixed-power tail
bound for that face alone already excludes zeros in the corresponding
strip.  Any successful cancellation must therefore keep it coupled to the
other sectors and the exact center.

## 7. Primary-literature comparison

The local novelty firewall changes the attribution before any external
comparison.  Two earlier project reports already contained the broad
architecture:

- [`COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md`](COMPLETION-PRESERVING-ADDITIVE-MODE-AUDIT.md)
  constructed the full-von-Mangoldt prime-minus-continuum measure, required
  the continuum term at every additive frequency, identified the
  zero-carrying principal band, and isolated the zero/reducible sectors left
  outside the favorable Wright packets.
- [`ZETA23-MERTENS-TYPEII-PRINCIPAL-BAND-GATE-2026-08-12.md`](ZETA23-MERTENS-TYPEII-PRINCIPAL-BAND-GATE-2026-08-12.md)
  had already shown, in the Mertens short-increment coordinate, that generic
  nonprincipal-frequency saving leaves a strip-strength principal carrier.

Thus neither “put the center in the same signed measure” nor “the principal
band contains the obstruction” is new to R187.  The actual R187 delta is
narrower: the exact two-moment affine center for the frozen Vaughan tail;
the explicit order-four cutoff `|xi|<=X^(-99/100)` with field, tail-energy,
and cross-term exponents `.46`, `.92`, and `.96`; the Gevrey
Mellin-difference localization of the whole completed field; and the finite
negative far-piece fixture.  Its local classification is therefore
**LOCAL PREDECESSOR + SHARPENED PROJECT SYNTHESIS**, not a new architecture.

No audited primary theorem has the complete passport.

- [Drappeau's Theorem 5.1](https://arxiv.org/abs/1504.05549) is the closest
  structural model: it keeps a low-conductor character projector inside a
  signed dispersion sum and gains `R^(-1)`.  At `Q~x^(1/2)`, however, its
  hypothesis `N<=Q^(2/3-eta)` restricts `N` to roughly `x^(1/3)`, not the
  balanced R71 scale `x^(1/2)`.  Its removed low-conductor projector is also
  not the R71 continuum/Type-I center and contains the zero-carrying part.
- [Wright's 2026 Theorems 2.1--2.2](https://arxiv.org/abs/2608.27732) give a
  fixed-power improvement for subdyadic, nonzero-phase trilinear
  Kloosterman-fraction form.  The phase is assumed nonzero, while the proof
  treats its native determinant-zero contribution separately.  It does not
  supply the R71 reducible/zero-phase/center completion; the convolution
  application gives a logarithmic aggregate after absolute values.  This is
  useful on individual nondegenerate packets, not on their completed R71 sum.
- [Blomer--Pascadi](https://arxiv.org/abs/2607.24311) gain `c^(-1/32)` for
  critical native short Kloosterman boxes.  The exact R71 support has not been
  serialized into those boxes with subpower projective cost while retaining
  the `k`-dependent phase and completion.
- [Maynard--Pandey--Radziwill](https://arxiv.org/abs/2608.14777) exhibit the
  scalar rational-major-arc term `N/sqrt(B)`.  Their absolute-value estimate
  diagnoses exactly why the rational projector cannot be discarded, but it
  does not estimate its cancellation with the R71 center.
- [MRSTT](https://arxiv.org/abs/2411.05770) prove logarithmic higher
  uniformity outside exceptional short intervals, relative to a sieve
  approximant.  Neither the every-window quantifier nor the exact R71
  quadratic cross terms survive that transfer.
- The Montgomery--Vaughan mean-value theorem is coefficient-blind and leaves
  the length term `X`, hence only `X^(1+o(1))` here.

The external-literature verdict is `NO MATCH LOCATED`, not proof of novelty.
The two localization theorems are classical Fourier/Gevrey analysis applied
to a locally pre-existing completion architecture and are classified as
**LOCAL PREDECESSOR + IMPORTED CLASSICAL ANALYSIS + SHARPENED PROJECT
SYNTHESIS**, not candidate-new mathematics.

## 8. Corrected next theorem

The strongest exact endpoint left after Sections 3--4 is

\[
 \boxed{
 \int\psi_R(r)\left|
   \int m(X^{99/100}\xi)\widehat f_r(\xi)P_R(-\xi)\,d\xi
 \right|^2dr
 \le X^{49/50+o(1)}.}                                 \tag{8.1}
\]

By (3.7), (8.1) is equivalent to the desired `eta=1/100` R71 estimate and
hence to the corresponding uniform strip.  It is a cleaner target, not an
easier theorem.

The next *falsifiable adapter*, before attempting (8.1) head-on, is narrower:

> Serialize the completed principal band as a signed cofactor/determinant
> sum in which (i) the nonzero high-determinant packets meet the Wright/R87
> hypotheses, (ii) the low-character/reducible sector is retained jointly
> with the exact affine center in (2.5), with their coupling explicitly
> exhibited, and (iii) the total projective decomposition cost is `X^o(1)`
> before any absolute value.

If such a serialization fails, the current Kloosterman-import route is
closed.  If it succeeds, the genuinely new analytic input is a **balanced,
completed projector-coupled dispersion theorem** with saving `X^(-1/50)`.
There are two parallel first-open edges: signed accumulation of the
nondegenerate packets, and joint cancellation of the reducible/low-character
projector with the exact center.  Improving only one does not prove a strip.

## 9. Formal and executable scope

Lean proves the affine two-moment identity, every rational exponent in the
`eta=1/100` ledger, the signed near/far transfer in both directions,
asymptotic extension independence at the error level, a negative far-piece
countermodel, and the failure of pointwise packet estimates to aggregate.
It does not formalize the analytic Fourier or number-theoretic inputs.

The Python replay checks the complete finite Fourier identity, all
tail/center sectors, the discrete Young bound, the finite negative far
fixture, the Gevrey exponent budget, the additive-band exponents, and the
affine-center moment equations.

No fixed-power arithmetic bound, uniform zero-free strip, sharp four-cycle
bound, or RH theorem is claimed.

## 10. Verification

The hostile referee found no fatal transform, affine-normalization,
spline-regularity, or exponent error after the scope corrections recorded
above.  The executable checks and synchronized corpus replay give:

```text
pytest -q src/test_r71_minor_arc_triage.py                 7 passed
focused synchronized Python suite                       129 passed
full Python suite                                      2421 passed in 67.62s
lake build RHBridge.R71MinorArcTriage                    8655 jobs
lake build RHBridge                                    13469 jobs
```

`R71MinorArcTriageAudit.lean` reports only Lean/mathlib's standard
`propext`, `Classical.choice`, and `Quot.sound`.  As stated in Section 9,
these machine checks certify the finite algebraic guards and replay the
numerical fixture; they do not formalize the analytic localization theorem.
