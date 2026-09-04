# Prime-hat transition and the semiprime `CA4` gate

Date: 2026-08-31

Preflight: [`zeta23_hat_transition_ca4_preflight_v1.json`](context/zeta23_hat_transition_ca4_preflight_v1.json)
Exact exponent verifier: [`hat_transition_ca4_gate.py`](../src/hat_transition_ca4_gate.py)

## Verdict

There is a new proved transition theorem for the exact frozen `HT-HAT`
candidate.  Retuning the published Gafni--Tao exceptional-gap envelope and
using the cellwise interpolation identity gives

\[
  |P_Y(t)-b(t)|
  \ll_\varepsilon Y^{-309/16250+\varepsilon}
  \quad (|t|\le Y^{1049/1250}),
\]

where

\[
 \frac{309}{16250}=.0190153846\ldots,
 \qquad
 \frac{1049}{1250}=.8392.
\]

This extends the proved range for the exact nodal-hat vector from
`Y^.4655` to `Y^.8392`, with strict exponent slack over `.019`.  More
generally, the endpoint for a requested saving `c` is every fixed

\[
 a<1-\left(\frac{2}{15}+\frac{13c}{9}\right).
\]

For `c=.01895` this is `a<.839294444...`.

The full aperture still ends at `Y^(50/33)=Y^1.51515...`; hence the theorem
does **not** prove `HT-HAT`, `DPA_P`, a zero-free strip, or RH.  It shortens
the genuinely open band to

\[
 Y^{.8392}\lesssim |t|\le Y^{50/33}.
\]

The initially proposed remaining sufficient input is the fixed-weight,
translated-window fourth moment `CA4(163/1000,1/10)`.  It is open.  The
proof attempt recorded in Sections 4--5 shows that it is equivalent at this
height to a raw atomic moment, not to cancellation against the continuum,
and that it is stronger than the one-sided floor strictly requires.  Its
first open term is a translated gap-weighted balanced-semiprime covariance,
not the project's arbitrary-coefficient sharp four-cycle theorem.

---

## 1. Exact candidate and cell identity

Put

\[
 w=\frac15,\qquad \alpha=\frac{49}{100},\qquad
 \phi(u)=\left(1-\frac{|u|}{w}\right)e^{\alpha u}.
\]

For the complete ordinary-prime shell `Ye^{-w}<=p<=Ye^w`, write

\[
 v_j=\log(p_j/Y),\qquad \Delta_j=v_{j+1}-v_j.
\]

Let `I_V` be linear interpolation on these nodes.  The raw nodal-hat
definition gives the exact identity

\[
 A_Y P_Y^{\mathbb C}(t)
   =\int_{v_1}^{v_J}\phi(u)I_V[e^{it\cdot}](u)\,du,
 \qquad
 A_Y=\int_{v_1}^{v_J}\phi(u)\,du.                    \tag{1.1}
\]

On an interval of length `Delta`, linear interpolation has

\[
 \left|I_V[e^{it\cdot}](u)-e^{itu}\right|
 \le \frac{t^2\Delta^2}{8}.                          \tag{1.2}
\]

This applies directly to the frozen hats.  No conversion to natural
von-Mangoldt weights, no random-prime model, and no coefficient optimization
is used.

---

## 2. Published gap input and a direct transition proof

On the locally audited branch of the Gafni--Tao theorem, for
`2/15<=gamma<=353/1445`, the physical prime gaps `g_j=p_{j+1}-p_j` satisfy

\[
 \sum_{p_j\asymp Y,\ g_j>Y^\gamma}g_j
 \ll_\varepsilon Y^{1-s(\gamma)+\varepsilon},
 \qquad
 s(\gamma)=\frac{45\gamma-6}{65}.                   \tag{2.1}
\]

This is the exact envelope already checked in
[`ZETA23-HIGH-DENOMINATOR-GAP-EXCEPTIONAL-TAIL-GATE-2026-08-13.md`](ZETA23-HIGH-DENOMINATOR-GAP-EXCEPTIONAL-TAIL-GATE-2026-08-13.md).
The source is Gafni--Tao,
[*On the number of exceptional intervals to the prime number theorem in
short intervals*](https://arxiv.org/abs/2505.24017), now published in
*Essential Number Theory* 5 (2026), 221--241.

Split the interpolation cells at `g_j<=Y^gamma`.

For the long cells, positivity and `Delta_j<<g_j/Y` give

\[
 \sum_{g_j>Y^\gamma}\int_{v_j}^{v_{j+1}}\phi(u)\,du
 \ll_\varepsilon Y^{-s(\gamma)+\varepsilon}.         \tag{2.2}
\]

For retained gaps, dyadic summation in (2.1) gives

\[
 \sum_{g_j\le Y^\gamma}g_j^3
 \ll_\varepsilon
 Y^{1+2\gamma-s(\gamma)+\varepsilon}.                \tag{2.3}
\]

Indeed a bin `g about Y^beta` contributes at most
`Y^(2 beta) sum_(g>Y^beta)g`, and the resulting exponent has positive slope
`2-9/13=17/13`, so the last bin dominates.  Gaps below `Y^(2/15)` are
handled separately by
`sum g^3 <= Y^(4/15) sum g << Y^(19/15)`; this is no larger than the
right side of (2.3).  Equations (1.2) and (2.3) yield

\[
 \sum_{g_j\le Y^\gamma}
 \left|\int_{v_j}^{v_{j+1}}
 \phi(u)(I_V[e^{it\cdot}](u)-e^{itu})\,du\right|
 \ll_\varepsilon
 t^2Y^{-[2-2\gamma+s(\gamma)]+\varepsilon}.          \tag{2.4}
\]

The Baker--Harman--Pintz maximal-gap theorem puts the two extreme prime
nodes within `O(Y^(-19/40))` in logarithmic distance of the tent endpoints.
Since `phi` vanishes linearly there, the omitted endpoint mass is
`O(Y^(-19/20))`.  The published source is
[*The Difference Between Consecutive Primes, II*](https://doi.org/10.1112/plms/83.3.532).
After probability normalization, (2.2)--(2.4) prove

\[
 |P_Y^{\mathbb C}(t)-\widehat\nu(t)|
 \ll_\varepsilon
 Y^{-19/20}
 +Y^{-s(\gamma)+\varepsilon}
 +t^2Y^{-[2-2\gamma+s(\gamma)]+\varepsilon}.         \tag{2.5}
\]

At `|t|<=Y^(1-gamma)`, the last term has saving exactly `s(gamma)`.
Taking

\[
 \gamma=\frac{201}{1250}=.1608
\]

gives

\[
 s(\gamma)=\frac{309}{16250}=.0190153846\ldots,
 \qquad 1-\gamma=\frac{1049}{1250}=.8392.            \tag{2.6}
\]

The continuous transform is `O((1+t^2)^(-1))`.  Thus on the high side of
the carrier band it is smaller than `Y^-.02`, and the strict
`1/65000` exponent margin in (2.6) absorbs constants and a sufficiently
small epsilon.  This proves the stated `.019` floor through `Y^.8392`.

### Trust and novelty label

The input (2.1) and the BHP endpoint theorem are published.  The deductions
(2.2)--(2.6) are elementary and exact.  The retuning to the frozen hat
candidate is new within this repository.  No claim of literature-level
novelty is made without external peer review.

---

## 3. Independent hat--Voronoi transfer

There is also an exact comparison with the older logarithmic Voronoi
antenna.  On one edge `[a,b]`, `d=b-a`, the left hat mass and the left
nearest-node half-cell mass differ by

\[
 \delta=\int_a^b\phi(u)k(u)\,du,
\]

where `k` has integral zero and is odd about `(a+b)/2`.  Consequently

\[
 |\delta|
 \le \operatorname{Lip}(\phi)
       \int_a^b|u-(a+b)/2|\,|k(u)|\,du
 =\frac{\operatorname{Lip}(\phi)}{24}d^2.            \tag{3.1}
\]

The right discrepancy is `-delta`, so the raw coefficient-vector distance
is at most

\[
 \frac{\operatorname{Lip}(\phi)}{12}\sum_j\Delta_j^2. \tag{3.2}
\]

After adding endpoint mass and normalizing, Stadlmann's announced
mean-square gap bound gives

\[
 \|\lambda^{\rm hat}-\lambda^{\rm Vor}\|_1
 \ll_\varepsilon Y^{-.77+\varepsilon}.              \tag{3.3}
\]

Thus every full-Voronoi Fourier estimate transfers uniformly to the exact
hat vector.  This comparison uses Julia Stadlmann's
[*On the mean square gap between primes*](https://arxiv.org/abs/2212.10867),
which the literature search still found as an arXiv preprint rather than a
published paper.  Equation (3.3) is therefore a preprint-dependent companion;
the main transition theorem in Section 2 does not depend on it.

---

## 4. A passport-complete high-tail sufficient lemma

For the residual band, fix

\[
 \theta=\frac{163}{1000}.
\]

Delete, before looking at `t`, the contributions of every nodal-hat edge
whose physical prime gap exceeds `Y^theta`, and renormalize the remaining
positive vector.  Call the resulting probability `mu_(Y,theta)` and let
`nu` be the continuous tent probability.  Set

\[
 R_Y(t)=\widehat\mu_{Y,\theta}(t)-\widehat\nu(t).      \tag{4.1}
\]

The deleted mass has the strict saving

\[
 s(\theta)=\frac{267}{13000}=.02053846\ldots>.019.   \tag{4.2}
\]

The same dyadic tail estimate, now with one rather than two extra powers of
the gap, gives

\[
 \sum_{g_j\le Y^\theta}g_j^2
 \ll_\varepsilon
 Y^{1+(20\theta+6)/65+\varepsilon}.
\]

As above, the gaps below `Y^(2/15)` are bounded by
`sum g^2<=Y^(2/15)sum g`; they do not dominate at the chosen `theta`.

Hence the normalized retained coefficients obey

\[
 \sum_p\lambda_p^2
 \ll_\varepsilon Y^{-q+\varepsilon},
 \qquad
 q=\frac{59-20\theta}{65}
  =\frac{2787}{3250}=.85753846\ldots .               \tag{4.3}
\]

The proposed open statement is:

> **`CA4(163/1000,1/10)`.** Uniformly on overlapping dyadic windows covering
> `Y^(1049/1250)<=T<=Y^(50/33)`,
> \[
>  \int_T^{2T}|R_Y(t)|^4\,dt
>  \ll T\,Y^{-2q+1/10+o(1)}.                         \tag{4.4}
> \]

This permits a full factor `Y^.1` above the atomic diagonal scale; exact
diagonal scale is not requested.

### High-band reduction to the raw atomic moment

There is an important simplification, and a correction to the original
motivation for (4.4).  On every residual window,

\[
 |\widehat\nu(t)|\ll T^{-2}\qquad(T\leq t\leq2T).
\]

Writing `M_Y=muhat_(Y,theta)`, the elementary inequalities
`|x+y|^4<=8(|x|^4+|y|^4)` in both directions give

\[
 \int_T^{2T}|M_Y-\widehat\nu|^4
 \ll \int_T^{2T}|M_Y|^4+T^{-7},
 \qquad
 \int_T^{2T}|M_Y|^4
 \ll \int_T^{2T}|M_Y-\widehat\nu|^4+T^{-7}.         \tag{4.4a}
\]

The remainder is far below the right side of (4.4).  Thus `CA4` is
quantitatively equivalent to the **raw atomic** fourth moment

\[
 \int_T^{2T}|M_Y(t)|^4dt
 \ll T Y^{-2q+1/10+o(1)}.                            \tag{4.4b}
\]

In particular, continuum centering cannot cancel an excessive high-band
atomic moment.  The required cancellation is among the unequal atomic
products under the translated time kernel.

### Exact adapter to the floor

Both probabilities in (4.1) live in `[-w,w]`, so `|R_Y'(t)|<=2w`.  If
`|R_Y(t_0)|>=delta`, then on at least a one-sided interval of length
`Omega(delta)` inside a containing dyadic window,
`|R_Y|>=delta/2`.  Therefore one bad point costs

\[
 \int|R_Y(t)|^4dt\gg\delta^5.                        \tag{4.5}
\]

Combining (4.4)--(4.5), and paying the largest legal window
`T<<Y^(50/33)`, gives the uniform exponent

\[
 c_{\rm out}
 =\frac{2(2787/3250)-50/33-1/10}{5}
 =\frac{10717}{536250}
 =.01998508\ldots>.019.                              \tag{4.6}
\]

The tail in (4.2), the normalization change, the full-hat comparison, and
the continuous transform are all smaller than `Y^-.019`.  Thus (4.4) would
close the entire `HT-HAT(.019)` aperture.  It would then provide the
positive-antenna sibling `DPA_P(c)` for every fixed `c<.019`; the independent
`LTRAD_P(.0189,.001)` sibling would remain open.

---

## 5. What `CA4` really is

Put

\[
 \sigma_Y=\mu_{Y,\theta}-\nu,
 \qquad
 \tau_Y=\sigma_Y*\sigma_Y.
\]

Then

\[
 \widehat\tau_Y(t)=R_Y(t)^2,
 \qquad
 |\widehat\tau_Y(t)|^2=|R_Y(t)|^4.                  \tag{5.1}
\]

A smooth dyadic majorant and Plancherel turn (4.4) into a band-pass `L2`
estimate for

\[
 \tau_Y
 =\mu_{Y,\theta}*\mu_{Y,\theta}
  -2\mu_{Y,\theta}*\nu+\nu*\nu.                    \tag{5.2}
\]

The atomic part of the first term is supported at

\[
 \log(p_1p_2/Y^2).
\]

Logarithmic resolution `1/T` corresponds to physical product resolution

\[
 H\asymp \frac{Y^2}{T}.
\]

At the top of the aperture this is

\[
 H=Y^{2-50/33}=Y^{16/33}.                           \tag{5.3}
\]

Thus the new arithmetic is a translated Selberg-variance theorem for
**balanced products of two primes**, with the actual adjacent-gap hat
weights.  Formula (5.2) is a valid physical representation, but (4.4a)
shows that its continuum terms are negligible on the target band.  The
essential signs come instead from the translated band-pass kernel applied
to unequal atomic products.  Bounding those near-product quadruples
absolutely deletes that cancellation.

More explicitly, take a nonnegative smooth `psi` supported in `(1/2,3)` and
equal to at least one on `[1,2]`, and put

\[
 K(\xi)=\int\psi(u)e^{iu\xi}\,du,
 \qquad
 a_n=\sum_{p_1p_2=n}\lambda_{p_1}\lambda_{p_2}.
\]

Then, exactly,

\[
 \int\psi(t/T)|M_Y(t)|^4dt
 =T\sum_{m,n}a_ma_nK\!\left(T\log\frac mn\right).   \tag{5.3a}
\]

Unique factorization gives

\[
 \sum_na_n^2
 =2\left(\sum_p\lambda_p^2\right)^2-\sum_p\lambda_p^4,
                                                                    \tag{5.3b}
\]

so the diagonal is affordable.  The first open term is the signed
four-distinct covariance in (5.3a).  Standard absolute or Hilbert treatment
gives `Y^2(sum lambda_p^2)^2`, while (4.4b) permits only
`T Y^.1(sum lambda_p^2)^2`.  The exact miss is

\[
 Y^{2-a-.1},
 \]

namely `Y^1.0608` at `a=.8392` and `Y^(127/330)` at `a=50/33`.

This also explains why unique factorization alone is insufficient.  It
identifies the exact atomic diagonal

\[
 2\left(\sum_p\lambda_p^2\right)^2-\sum_p\lambda_p^4,
\]

but ordinary mean-value theory gives

\[
 \frac1T\int_T^{2T}|R_Y(t)|^4dt
 \lesssim (1+Y^2/T)\left(\sum_p\lambda_p^2\right)^2.
                                                                    \tag{5.4}
\]

The conductor loss in (5.4) ranges from `Y^1.1608` at the start of the
residual band to `Y^(16/33)` at its end, whereas (4.4) permits only `Y^.1`.
The exact missing improvement is therefore at least `Y^(16/33-.1)` even at
the easiest endpoint.

---

## 6. Hostile audit

The following possible shortcuts were eliminated.

1. **Gap geometry.** Snapping the log nodes to an odd half-grid moves each
   physical node by less than one at the top aperture, preserves local gap
   geometry asymptotically, and forces `P_Y(B)=-1`.  Ordinary `L2` energy can
   remain diagonal-scale.  Local gaps, density, and large sieve alone cannot
   prove (4.4).
2. **Exact log curvature plus integrality.** The existing odd-integer
   phase-selected construction has `O(log Y)` gaps, no exceptional long-gap
   mass, and exact logarithmic curvature, yet has a constant-width antipodal
   peak.  Exact primality must enter.
3. **More local Peano steps.** The current cell defect already has zero mass
   and first moment.  Its next primitive has one sign.  Another absolute
   summation-by-parts step cannot create cross-gap cancellation.
4. **Cumulative fourth moments.** Integrating from zero includes the coherent
   low carrier and is useless.  The target must be translated dyadically.
5. **Natural prime-polynomial estimates.** Results for `Lambda/log` weights
   do not transfer to adjacent-gap hats.  A coefficient-blind Vaughan or
   Heath--Brown decomposition absorbs `n^(it)` into arbitrary Type-II
   coefficients and loses the one-variable curvature.

`CA4` is not target renaming: a polynomial can satisfy the one-sided floor
while having large positive peaks and failing (4.4).  But the hostile models
also show that `CA4` contains the entire missing actual-prime anti-alias
content.  It is a genuine new theorem, not a soft consequence of the proved
gap packages.

---

## 7. A second, stronger analytic interface

There is a useful fallback formulation.  With the separate fixed cutoff
`theta=161/1000`, define the global retained symmetric trapezoid defect

\[
 \mathcal R_\theta(z)=
 \sum_{g_n\le p_n^\theta}
 \left\{
 \frac{\Delta_n}{2}(p_n^{-z}+p_{n+1}^{-z})
 -\int_{\log p_n}^{\log p_{n+1}}e^{-zu}\,du
 \right\}.                                          \tag{7.1}
\]

The third-moment estimate proves normal convergence in

\[
 \Re z>-r_3,
 \qquad
 r_3=2-2\theta+s(\theta)
     =\frac{22063}{13000}=1.697153846\ldots .        \tag{7.2}
\]

On every interior line `Re z=-r_3+eta`, the absolute estimate is
`O_eta((1+|Im z|)^2)` and merely reproduces the transition frontier.  A new
actual-prime estimate

\[
 \mathcal R_\theta(-r_3+\eta+i\tau)
 \ll_{\eta,\delta}(1+|\tau|)^{1-\delta+\eta}         \tag{7.3}
\]

would, after choosing `eta<delta` and Mellin-localizing by the tent, give

\[
 Y^{-r_3+\eta}t^{1-\delta+\eta}.                    \tag{7.4}
\]

Even the formal `delta=0` exponent leaves `.182...` before the tail charge at
`t=Y^(50/33)`.  The strict exponent below one in (7.3) is used because the
piecewise-linear tent has only quadratic Mellin decay.

This boundary theorem has stronger pointwise and global quantifiers, but it
is not logically ordered with the quantitatively smaller shell-average asked
for by `CA4`: neither displayed estimate implies the other.  It is retained
as a structurally distinct fallback, not promoted over (4.4).

---

## 8. Literature applicability

The closest established results do not match the passport.

- Matomaki--Shao--Tao--Teravainen,
  [*Higher uniformity of arithmetic functions in short intervals I. All
  intervals*](https://arxiv.org/abs/2204.03754), gives arbitrarily strong
  logarithmic bounds for certain natural prime Dirichlet polynomials in a
  relevant height range.  It gives no fixed power and no adjacent-gap mask.
- Matomaki--Teravainen,
  [*Almost primes in almost all short intervals II*](https://arxiv.org/abs/2207.05038),
  proves strong almost-all short-interval results for naturally weighted
  `E_2` numbers using sparse Dirichlet-polynomial mean values.  Its improved
  mean-value lemma still contains the absolute close-pair term

  ```text
  T sum_{0<|h|<=N/T} sum_n |a_n a_{n+h}|,
  ```

  which discards precisely the translated-kernel cancellation needed in
  (5.3a).  It therefore does not state the balanced, gap-weighted band-pass
  variance.
- Matomaki--Radziwill--Tao,
  [*Correlations of the von Mangoldt and higher divisor functions I. Long
  shift ranges*](https://arxiv.org/abs/1707.01315), reaches almost all shifts
  from `H >= M^(8/33+epsilon)` for natural von-Mangoldt/divisor correlations.
  At the top of our range, `M=Y^2` and `H=Y^(16/33)=M^(8/33)`: the exponents
  meet exactly, but their theorem has an epsilon margin, logarithmic rather
  than fixed-power savings, and neither the adaptive adjacent-gap weights nor
  our adaptive weighted convolution.  This exact exponent contact is useful evidence
  for the method, not an importable proof.
- Evans,
  [*Correlations of Almost Primes*](https://arxiv.org/abs/2102.12297), proves
  asymptotics for almost all shifts under factor-range restrictions.  It does
  not control the actual consecutive-gap coefficients or the one common
  translated Mellin height required by `CA4`.
- Matomaki--Shao--Tao--Teravainen,
  [*Higher uniformity of arithmetic functions in short intervals II. Almost
  all intervals*](https://arxiv.org/abs/2411.05770), obtains power savings for
  dense modelled divisor correlations.  Its dense `d_2` structure does not
  transfer to the selected prime-prime convolution with adaptive gap weights;
  even the nominal saving is below the power required by (4.4).

The literature therefore supplies a plausible toolkit--sparse mean values,
Type-II decomposition, and almost-prime correlations--but not the theorem.
The first non-imported edge is exactly the translated, selector-dependent
balanced-semiprime covariance in (5.3a).

---

## 9. Decision-tree update

The earlier `.4655` stopping point was not intrinsic.  It used only the
largest individual gap and missed the combination

```text
exceptional long-gap mass + truncated third gap moment + exact hat cells.
```

That is the important corrected choice, and it yields the theorem in Section
2.  Above `.8392`, the same absolute mechanism is exhausted: a hostile
integer set can align with the phase while satisfying all of its inputs.

The highest-information next proof target exposed by this card is therefore
the atomic form (4.4b), with these nonnegotiable features:

```text
actual consecutive primes;
actual adjacent-gap hat weights;
long edges removed before t is known;
all dyadic bands combined before absolute values;
the signs of the one translated kernel retained across unequal products;
an allowed Y^.1 loss, not an unnecessarily sharp diagonal theorem.
```

The exact state is:

| Statement | Status |
|---|---|
| Exact frozen-hat floor through `Y^.8392` | **PROVED** |
| Hat--Voronoi `l1` transfer | **PROVED conditional on Stadlmann preprint input** |
| `CA4(163/1000,1/10)` | **OPEN** |
| Renewal boundary estimate (7.3) | **OPEN** |
| Full `HT-HAT(.019)` / `DPA_P(.019)` | **OPEN** |
| `LTRAD_P(.0189,.001)` | **OPEN** |
| Uniform zero-free strip / RH | **OPEN** |
