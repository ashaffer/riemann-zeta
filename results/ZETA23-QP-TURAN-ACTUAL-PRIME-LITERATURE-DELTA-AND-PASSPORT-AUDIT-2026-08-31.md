# QP/Turan actual-prime literature delta and passport audit

Date: 2026-08-31

Literature cutoff: 2026-08-31

Trust: primary papers and author/publisher records were checked directly.
Project exponent specializations are derived below.  A cited theorem is not
treated as an application unless its complete passport matches.

## Verdict

No checked theorem proves `DPA_P(.019)`, averaged or pointwise `GCG4`,
`CA4(163/1000,1/10)`, or `LTRAD_P(.0189,.001)`.

Two previously unrecorded August 2026 papers are genuinely relevant, but both
fail decisive tests.

1. Maynard--Pandey--Radziwill prove a new pointwise additive exponential-sum
   estimate for the natural von Mangoldt sequence.  Its phase, coefficient
   class, and quantifiers do not match a prime-log antenna.  On the most
   optimistic generic-minor-arc specialization to the semiprime covariance,
   it gives normalized square size only `Y^(-5/12+o(1))`, whereas `CA4`
   requires `Y^(-5249/3250+o(1))`.  The exponent deficit is

   \[
      \frac{5249}{3250}-\frac5{12}
      =\frac{23369}{19500}=1.198410\ldots .
   \]

2. Wright's new subdyadic trilinear Kloosterman-fraction theorem recognizes
   short intervals in both denominator variables.  This is a real method
   contact, but not a near miss.  At the exact `CA4` scale, its unchanged
   first term caps even an ideal, lossless global reconstruction at the
   formal conductor saving `Y^(-1/8)`.  `CA4` needs
   `Y^(-127/330)`, leaving

   \[
      \frac{127}{330}-\frac18
      =\frac{343}{1320}=.259848\ldots .
   \]

   The scalar blockwise use is worse: it also pays up to
   `Y^(1-theta)` when the blocks are recombined.  Independently of this
   numerical failure, Wright has three separated coefficient slots and a
   nonzero reciprocal phase; `CA4` has four adaptive adjacent-gap weights,
   a translated signed kernel, and a zero/main sector which has not been
   separated with a fixed-power error.

A live-source check also changes one apparent import: Olivier Ramare's
2026 preprint *The weighted large sieve through Parseval* is **withdrawn**;
the author records an important miscalculation.  It is not admissible input.

Alpoge--Furman's new critical-line density theorem was also rechecked at the
exact prime-side theorem, rather than inferred from its headline.  It is a
major result, but it is already imported in this repository and is
deliberately insensitive to a sparse off-line set.  Its prime-side input is a
second moment for the fixed natural `Lambda(n)/sqrt(n)` sequence at length
`X<=T`; a Montgomery--Vaughan second-moment treatment of the masked
semiprime replacement would have length `Y^2` at time `Y^(50/33)`, exceeding
the diagonal range by `Y^(16/33)`.  It therefore reproduces, rather than
removes, the exact conductor obstruction behind `CA4`.  Its Section 7.2
conditional `k=4` discussion does land on the exact shift resolution
`Y^(16/33)`, but for the natural `Lambda*Lambda` mask and without an
unconditional estimate.

Thus the literature reframe is negative but useful.  Short-block recognition
alone cannot close the conductor gap.  Any viable `CA4/GCG4` theorem must
improve the Kloosterman first term as well as preserve the four masks and
collective signed reconstruction.  The independent `LTRAD` lock is untouched.

## 1. Exact passports used in this audit

The routing state is
[`ZETA23-UNIFORM-STRIP-CONSOLIDATED-STATE-AND-INTUITION-PUMPS-2026-08-30.md`](ZETA23-UNIFORM-STRIP-CONSOLIDATED-STATE-AND-INTUITION-PUMPS-2026-08-30.md).
The exact high-tail targets are recorded in
[`ZETA23-HAT-TRANSITION-AND-CENTERED-SEMIPRIME-CA4-GATE-2026-08-31.md`](ZETA23-HAT-TRANSITION-AND-CENTERED-SEMIPRIME-CA4-GATE-2026-08-31.md)
and
[`ZETA23-GLOBAL-CONDUCTOR-L4-INFORMATION-GAIN-SPRINT-2026-08-31.md`](ZETA23-GLOBAL-CONDUCTOR-L4-INFORMATION-GAIN-SPRINT-2026-08-31.md).

### 1.1 `DPA_P(.019)`

For every sufficiently large legal `Y`, one needs a real, signed,
prime-supported vector satisfying

\[
 \sum_p y_p=1,
 \qquad
 \inf_{t\in[Y^{.01},Y^{50/33}]}
       \sum_p y_p\cos(t|\log(p/Y)|)\ge -Y^{-.019}.
\]

The fixed retained-hat branch is stronger because its vector is nonnegative
and fixed before `t` is seen.  Its low band is proved only through
`Y^.8392`; the rest is open.

### 1.2 `CA4` and global `GCG4`

For `theta=163/1000`, let `lambda_p` be the normalized positive nodal-hat
weights after all edges with physical gap above `Y^theta` are deleted before
`t` is seen, and put

\[
 M_Y(t)=\sum_p\lambda_p e^{it\log(p/Y)},
 \qquad q=\frac{2787}{3250}.
\]

Uniformly on every translated dyadic window
`Y^(1049/1250)<=T<=Y^(50/33)`, `CA4` asks for

\[
 \int_T^{2T}|M_Y(t)|^4dt
 \ll T Y^{-2q+1/10+o(1)}.                           \tag{1.1}
\]

At the top scale, with product variable `X=Y^2`,

\[
 T=Y^{50/33}=X^{25/33},\qquad
 H=Y^2/T=Y^{16/33}=X^{8/33}.                       \tag{1.2}
\]

Ordinary fourth-moment theory loses `Y^2/T=Y^(16/33)` over the diagonal
scale, while (1.1) permits `Y^.1`.  The required conductor improvement is

\[
 Y^{16/33-1/10}=Y^{127/330}.                       \tag{1.3}
\]

The alternative global target uses `theta=161/1000`,
`q=2789/3250`, and requires

\[
 \int_{Y^{839/1000}}^{2Y^{50/33}}|F_{Y,\theta}(t)|^4dt
 \ll Y^{-1187/13000+o(1)}.                         \tag{1.4}
\]

The selected conductor gain is `3/8`; the exact minimum is
`9599/26000=.369192...`.

The center-averaged version asks, on a fixed-factor block of half-integer
centers, for

\[
 \frac1{\#\mathcal Y_N}\sum_{Y\in\mathcal Y_N}
 \int_{Y^{839/1000}}^{2Y^{50/33}}|F_Y(t)|^4dt
 \ll N^{-1187/13000+o(1)}.                         \tag{1.5}
\]

This averages the shell center `Y`.  It is not an average over characters,
delta-method moduli, determinant offsets, or short-interval starts.

Opening the fourth power gives the actual adjacent-gap-weighted balanced
semiprime covariance

\[
 T\sum_{m,n}a_ma_nK\!\left(T\log\frac mn\right),
 \qquad
 a_n=\sum_{pr=n}\lambda_p\lambda_r.                \tag{1.6}
\]

The diagonal and shared-prime sectors fit.  The first open term is the
signed four-distinct part.  Taking absolute values of the near-product tube
removes exactly the cancellation being requested.

### 1.3 `LTRAD_P(.0189,.001)`

For every legal negative prime event of mean depth
`D>=Y^(-.001+o(1))`, the prime-only radial radius must obey

\[
 r_P(H_Y)\ge Y^{-.0189+o(1)}.
\]

For the recorded one-atom mixing adapter, the transverse form is

\[
 \inf_{y:y\cdot v=-1}\sup_{t\in H_Y}y\cdot a_P(t)
 \ge Y^{-.0179+o(1)}.                              \tag{1.7}
\]

This is a lower-return statement for every source-normalized legal signed
dual vector.  Upper bounds for one natural prime polynomial, density-one
statements, or unsigned moment bounds have the wrong polarity or quantifier.

## 2. Duplicate audit and genuinely new items

The following project imports were checked before searching: the analytic
baseline, the 2026-08-29 frontier survey, the reciprocal/bilinear survey,
the 2026-08-31 breadth synthesis, and the two exact `CA4/GCG4` reports linked
above.  Consequently the following are retained as prior imports, not new
discoveries:

- Montgomery--Vaughan mean values;
- Guth--Maynard large values and zeta zero density;
- Gafni--Tao exceptional short intervals;
- Baker--Harman--Pintz and Stadlmann prime-gap inputs;
- Matomaki--Radziwill--Tao shifted correlations at `X^(8/33+epsilon)`;
- Matomaki--Teravainen sparse almost-prime mean values;
- the two Higher Uniformity papers;
- Bettin--Chandee trilinear Kloosterman fractions;
- Wright's April 2026 Part I;
- Alpoge--Furman's critical-line density theorem and its finite-Gabor
  rank--trace mechanism;
- Jaming--Kellay--Saba and Avdonin--Moran for resolved frequencies and
  clusters;
- the standard and variational large sieves; and
- sharp GCD-sum bounds.

The material additions and requested live-source recheck from the present
pass are:

| Source | Source status on 2026-08-31 | Audit result |
|---|---|---|
| [Maynard--Pandey--Radziwill, *Exponential sums over primes*](https://arxiv.org/abs/2608.14777), v1, 2026-08-14 | primary arXiv preprint | new theorem checked; no gate adapter |
| [Wright, *Trilinear Kloosterman fractions II*](https://arxiv.org/abs/2608.27732), v1, 2026-08-27 | primary arXiv preprint | new theorem checked; exact exponent and passport failures below |
| [Chen--Gupta--Li, character large values and zero density](https://arxiv.org/abs/2507.08296), v2, 2026-07-27 | primary arXiv preprint, materially revised after v1 | q-aspect theorem checked; no gate adapter |
| [Alpoge--Furman, *More than two thirds of the zeros...*](https://arxiv.org/abs/2608.13637), v2, 2026-08-19 | primary arXiv preprint, with official Lean artifact | prior import rechecked at its prime-side theorem; no strip or `CA4` adapter |
| [Li, *Primes in almost all short intervals III*](https://runbolicarey.com/assets/downloads/Primes_in_almost_all_short_intervals_III.pdf) | author-hosted, unrefereed manuscript with no stable version stamp | stronger statement noted, but still only logarithmic exceptional density |
| [Ramare, *The weighted large sieve through Parseval*](https://arxiv.org/abs/2605.29470) | **withdrawn**; “important miscalculation discovered” | inadmissible |

## 3. Wright II: exact `CA4` passport test

### 3.1 The imported theorem

For intervals or consecutive elements of congruence classes
`A subset [A,2A]`, `M subset [M,2M]`, `N subset [N,2N]`, with

\[
 |\mathcal M|\ll MX^{-\eta},\qquad
 |\mathcal N|\ll NX^{-\eta},
\]

Wright's Theorem 2.1 bounds, for nonzero integer `vartheta`,

\[
 \mathcal B=
 \sum_{a\in\mathcal A}\sum_{m\in\mathcal M}
 \sum_{\substack{n\in\mathcal N\\(m,n)=1}}
 \alpha_m\beta_n\gamma_a
 e\!\left(\vartheta\frac{a\bar m}{n}\right)
\]

by

\[
\begin{aligned}
 |\mathcal B|
 &\ll \|\alpha\|_2\|\beta\|_2\|\gamma\|_2 M^\varepsilon
 \left(1+\frac{|\vartheta|A}{NM}\right)^{1/2}\\
 &\quad\times\left[
 A^{1/2}(M^{1/2}N^{3/8}+M^{3/8}N^{1/2})\right.\\
 &\qquad\qquad\left.
 +A^{7/20}(M^{3/5}N^{7/20}+M^{7/20}N^{3/5})X^{-2\eta/5}
 \right].                                           \tag{3.1}
\end{aligned}
\]

For 1-bounded `alpha,beta`, their two norms contribute the additional local
support factor `X^(-eta)` relative to full dyadic support.  Wright notes a
typical `X^(-7eta/5)` local improvement when the second bracketed term is
dominant.  That sentence cannot be extrapolated through our global block
reconstruction, and at our parameters the first term becomes dominant.  As
in the paper's convolution application, `X=MN` in the specialization below.

### 3.2 Exact scale ledger

Give the theorem every friendly identification:

\[
 X=Y^2,\qquad M=N=Y,\qquad A=H=Y^{16/33}.           \tag{3.2}
\]

A physical block of length `Y^theta` has

\[
 Y^\theta=Y X^{-\eta},
 \qquad \eta=\frac{1-\theta}{2}.                   \tag{3.3}
\]

Thus `eta=837/2000` for `CA4` and `eta=839/2000` for global `GCG4`.
The explicit improvement in the second term of (3.1), in `Y` units, is

\[
 X^{-2\eta/5}=Y^{-2(1-\theta)/5}
 =\begin{cases}
   Y^{-837/2500}=Y^{-.3348},&\theta=.163,\\
   Y^{-839/2500}=Y^{-.3356},&\theta=.161.
  \end{cases}                                      \tag{3.4}
\]

This looks large until both bracketed terms are retained.  Before (3.4),
their `Y` exponents are

\[
 \frac12\frac{16}{33}+\frac78=\frac{295}{264},
 \qquad
 \frac7{20}\frac{16}{33}+\frac{19}{20}=\frac{739}{660}.
                                                               \tag{3.5}
\]

The second is larger by exactly `1/440`.  For the original full-dyadic
Bettin--Chandee estimate, the two corresponding relative savings from the
trivial trilinear size are

\[
 \frac18,
 \qquad
 \frac1{20}+\frac3{20}\frac{16}{33}=\frac{27}{220};
                                                               \tag{3.6}
\]

the second term dominates, giving the previously recorded formal saving
`27/220`.

Wright's factor (3.4) makes that second term much smaller, but it does
nothing to the first.  Therefore even a hypothetical **lossless**
vector-valued reconstruction over every short block is capped at

\[
 \min\left(\frac18,
            \frac{27}{220}+\frac{2(1-\theta)}5\right)
 =\frac18.                                         \tag{3.7}
\]

So the new theorem improves the friendly Bettin--Chandee benchmark by only
`1/440`, from `27/220` to `1/8`.  It misses

\[
 \begin{array}{rcl}
 \text{pointwise `CA4`:}&127/330-1/8&=343/1320=.259848\ldots,\\
 \text{selected global `GCG4`:}&3/8-1/8&=1/4,\\
 \text{exact global threshold:}&9599/26000-1/8&=6349/26000=.244192\ldots.
 \end{array}                                       \tag{3.8}
\]

The actual scalar theorem does not offer lossless reconstruction.  There
are `R=Y^(1-theta)` blocks in each prime variable, and

\[
 \sum_i\|\alpha_i\|_2\le R^{1/2}\|\alpha\|_2,
 \qquad
 \sum_j\|\beta_j\|_2\le R^{1/2}\|\beta\|_2.       \tag{3.9}
\]

Termwise absolute recombination can therefore pay another `R`.  The theorem
contains no square-function statement which removes (3.9).  Equation (3.7)
is consequently an optimistic ceiling, not an achieved global estimate.

### 3.3 Passport fields

| Field | Wright II | `CA4/GCG4` | Result |
|---|---|---|---|
| arithmetic geometry | reciprocal phase `a mbar/n` | translated near determinant `pr-qs`, after a still-unproved completion | no literal adapter |
| coefficient slots | three separated arbitrary sequences | four factor weights, each determined by an adjacent-prime gap | grouping creates a joint convolution slot |
| short support | two interval/AP variables can be subdyadic | prime factors can be partitioned into physical short blocks | genuine local contact |
| sign | absolute value of each reciprocal-phase form | cancellation of one signed translated kernel across offsets and windows | termwise use discards target cancellation |
| zero sector | `vartheta` must be a nonzero integer | completion has a zero/main sector; identifying and subtracting it with fixed-power error is open | failed |
| quantifier | one trilinear form | every legal `Y`; every translated window, or one global/center average | reconstruction absent |
| power | ideal ceiling `1/8` at (3.2) | `127/330` pointwise or at least `9599/26000` globally | failed before masks |

Wright's Theorem 2.2 also has a real scale contact.  It proves logarithmic
Bombieri--Vinogradov-type distribution for `alpha*beta` when `beta` is
Siegel--Walfisz, uniformly for

\[
 N^{34}X^{-17+\varepsilon}\le Q\le NX^{-\varepsilon}. \tag{3.10}
\]

At `M=N=Y=X^(1/2)`, the natural `CA4` delta-method modulus

\[
 Q=T^{1/2}=Y^{25/33}=X^{25/66}                    \tag{3.11}
\]

does lie inside (3.10).  This corrects the weaker comparison that looks only
at Wright's showcased `Q=X^(1/2+epsilon)` corollary.  It still does not help:

- neither adjacent-gap sequence is known to be Siegel--Walfisz;
- the conclusion is only `X(log X)^(-A)`, not a fixed power;
- it averages delta-method moduli rather than shell centers `Y`;
- it treats one fixed residue `a`, whereas the translated kernel has many
  determinant offsets/modes; and
- no principal-term identity has been proved for the recomputed hat weights.

Thus both Wright theorems fail, for different reasons.

## 4. Maynard--Pandey--Radziwill: exact passport test

### 4.1 The theorem

Write `alpha=a/r+epsilon`, `(a,r)=1`, `r<=N^(1/2)`,
`|epsilon|<=1/(rN^(1/2))`, and

\[
 \mathfrak B=\max(r,rN|\varepsilon|).
\]

Maynard--Pandey--Radziwill Theorem 1.1 proves

\[
 \left|\sum_{n<N}\Lambda(n)e(n\alpha)\right|
 \le N^{o(1)}\left(\frac{N}{\mathfrak B^{1/2}}
                         +N^{19/24}\right).         \tag{4.1}
\]

It improves Vinogradov's `N^(4/5)` term to `N^(19/24)`.  The proof uses the
Heath--Brown identity, character-aspect large values, and specific allowable
factorizations of the natural von Mangoldt sequence.  Its intermediate
arbitrary coefficients do not turn (4.1) into an arbitrary-coefficient
prime theorem.

### 4.2 `DPA` test

`DPA` has phase `t log(p/Y)`, not `p alpha`.  At top height, Taylor
linearization on a physical interval of length `L` is harmless only while

\[
 tL^2/Y^2\ll1,
 \qquad L\lesssim Y/\sqrt t=Y^{8/33}.              \tag{4.2}
\]

The retained gap blocks `Y^.163` are shorter than (4.2), but (4.1) is a
prefix/dyadic theorem for the natural sequence `Lambda(n)`.  Differencing
two prefixes gives an error of size `Y^(19/24+o(1))`, vastly exceeding a
shifted block of length at most `Y^(8/33)`.  It neither treats
`Lambda(Y+h)` at that length nor the adjacent-gap weight `lambda_p`.

Moreover, `DPA` asks for one vector chosen before `t` and a uniform
one-sided floor on the entire band.  Major arcs in (4.1) retain the first
term `N/B^(1/2)`, and may give no power saving.  Thus the phase,
mask, coefficient cone, and quantifier order all fail.

### 4.3 `CA4/GCG4` test

After (1.6) is linearized on `|m-n|<=H`, an additive Fourier representation
has product phase `e(alpha pr)`.  Fixing one prime `p` leaves an additive
prime sum in `r`, but with coefficient `lambda_r`, not `Lambda(r)`.  The
frequency also depends on the complementary product in the exact kernel.

Even ignoring those failures, assume the most favorable generic
`B=Y^(1/2)` and replace the actual weights by normalized natural
prime weights.  Then (4.1) gives inner normalized amplitude

\[
 Y^{19/24}/Y=Y^{-5/24+o(1)}.                        \tag{4.3}
\]

Triangle summation in the fixed outer prime and then squaring gives at best
`Y^(-5/12+o(1))`.  In contrast, (1.1) asks per unit `T` for

\[
 Y^{-2q+1/10+o(1)}=Y^{-5249/3250+o(1)}.            \tag{4.4}
\]

The deficit is the `23369/19500` displayed in the verdict.  When
`B=O(1)`, (4.1) gives no saving at all.  An average theorem proving
that the tuple-dependent frequencies avoid those major arcs would itself be
a new input.  Finally, (4.3) does not retain the actual `ell^2` scale
`sum lambda_p^2`, so it cannot be multiplied by that scale for free.

The result therefore does not imply pointwise or center-averaged `GCG4`.

### 4.4 Passport fields

| Field | Maynard--Pandey--Radziwill | Project gate | Result |
|---|---|---|---|
| phase | additive `e(n alpha)` after rational approximation | Mellin `e^(it log(p/Y))`, or a translated product determinant after a further completion | no direct phase adapter |
| source/mask | the fixed natural `Lambda(n)` sequence, including prime powers | prime-only adjacent-gap hats, or an arbitrary legal signed source vector | failed |
| coefficient cone | Heath--Brown factors internal to one natural sequence | four externally prescribed adaptive prime coefficients | internal arbitrary slots do not transfer |
| sign/polarity | absolute upper bound for one exponential sum | uniform one-sided DPA floor, lower-return `LTRAD`, or signed covariance cancellation | failed |
| resolution | prefix/dyadic length `Y`; differencing error `Y^(19/24)` | shifted Taylor blocks of length at most `Y^(8/33)` and product resolution `Y^(16/33)` | failed |
| normalization | natural mass of order `Y` | `sum y_p=1` or the actual hat `ell^2` scale | failed |
| quantifier/average | pointwise in one additive frequency; no shell-center average | one vector before every `t`, every translated time window, or average over recomputed centers `Y` | failed |
| exponent | optimistic normalized square `Y^(-5/12)` | `Y^(-5249/3250)` per unit time in `CA4` | deficit `23369/19500` |

### 4.5 Character large values and zero density behind (4.1)

Chen--Gupta--Li Theorem 1.1 treats primitive characters and arbitrary
`|a_n|<=1`, but assumes `N>=(qT)^(2/3)`.  For a prime-factor polynomial at
the top `CA4` height,

\[
 N=Y,\qquad T=Y^{50/33},\qquad T^{2/3}=Y^{100/99}, \tag{4.5}
\]

so the direct factor-length use misses the hypothesis by `Y^(1/99)`.
At product length the hypothesis holds, but the coefficient is the adaptive
semiprime convolution and the already-audited generic large-value terms
remain.

Their Theorem 1.2 gives, among other bounds,

\[
 \sum_{\chi\bmod q}N(\sigma,T,\chi)
 \ll(qT)^{7(1-\sigma)/3+o(1)}
\]

uniformly, with a `30/13` exponent in favorable smooth-modulus regimes.
For `q=1` this is a zeta zero-density theorem, not zero exclusion: it can
still permit one zero in any contemplated fixed strip.  It averages
characters/zeros, not shell centers or legal source vectors.  Hence it does
not prove `DPA`, `LTRAD`, or a uniform strip.

## 5. Alpoge--Furman: density breakthrough, not a strip or mask theorem

### 5.1 Exact imported result and prime-side theorem

[Alpoge--Furman, Theorem A](https://arxiv.org/abs/2608.13637) proves

\[
 N_0^s(T,2T)\ge (2/3-o(1))N(T,2T),\qquad
 N_d(T,2T)\ge (5/6-o(1))N(T,2T).                  \tag{5.1}
\]

For the Montgomery--Taylor window the constants become

\[
 C=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}
   =.6725007\ldots,
 \qquad \frac{1+C}{2}=.8362503\ldots .           \tag{5.2}
\]

Theorem B gives the same statement for each fixed primitive Dirichlet
character; the paper's
[official Lean artifact](https://github.com/anthropics/zeta-23-lean)
formalizes both results.  This is already audited in
[`ANTHROPIC-ZETA23-INTEGRATION.md`](../publication/ANTHROPIC-ZETA23-INTEGRATION.md)
and the analytic baseline, so it is a revalidated prior import rather than a
new project discovery.

The mechanism is important.  A finite Gabor compression of Weil's Hermitian
form writes the zero side as an on-line positive part plus off-line
signature-`(1,1)` blocks.  A rank--trace inequality combines this inertia
information with their prime-side Theorem 5.7,

\[
 \|\widetilde G\|_{\rm HS}^2
   =(R(\psi)+O_\psi((\log T)^{-1}))N(T,2T).        \tag{5.3}
\]

But (5.3) is evaluated from the fixed explicit-formula polynomial

\[
 P_X(\tau)=-\frac1\pi\sum_{n\le X}
          \frac{\Lambda(n)}{\sqrt n}\cos(\tau\log n),
 \qquad X=T/(2\pi),                               \tag{5.4}
\]

including prime powers.  Its arithmetic estimate is Montgomery--Vaughan
orthogonality plus Chebyshev--Mertens for the natural square weights; the
general licensed range is `X<=T`.  It is not a fourth-moment estimate for an
arbitrary prime mask.

### 5.2 Exact conductor, higher-trace, and resolution ledger

There are two possible comparisons, and neither transfers.

1. Treat (5.3) as a theorem for a prime-factor polynomial of length `Y`.
   Since `Y<T=Y^(50/33)`, the ordinary second moment is already in the
   diagonal range.  `CA4`, however, asks for its **fourth** moment.

2. Square the masked prime polynomial first and try to feed its semiprime
   coefficients to the second-moment argument.  Write its product length as
   `N_prod=Y^2`, while the top time length is `T_CA=Y^(50/33)`.  Thus

   \[
      \frac{N_{\rm prod}}{T_{\rm CA}}
       =Y^{2-50/33}=Y^{16/33}.                    \tag{5.5}
   \]

   This is precisely the generic fourth-moment conductor loss.  The target
   permits only `Y^(1/10)`, so the missing improvement remains

   \[
      Y^{16/33-1/10}=Y^{127/330}.                 \tag{5.6}
   \]

   Since (5.3) supplies no masked-semiprime power saving, its formal gain is
   zero.  The corresponding deficits are therefore `127/330` for pointwise
   `CA4`, the selected `3/8` for global `GCG4`, and `9599/26000` for the exact
   global threshold; averaging (5.3) over zero heights does not create the
   shell-center average (1.5).

The nearby product resolution is correspondingly

\[
 H=Y^2/T_{\rm CA}=Y^{16/33}=N_{\rm prod}^{8/33},  \tag{5.7}
\]

whereas (5.3) isolates the natural diagonal through the log-frequency gaps
of individual prime powers.  It has no theorem for the signed translated
`|pr-qs|\lesssim H` tube.

Alpoge--Furman Section 7.2 makes the missing order explicit.  Their diagonal
evaluation of `tr(G_tilde^k)` is available in the Rudnick--Sarnak range

\[
 X^k\le T^{2-\varepsilon};                        \tag{5.8}
\]

apart from the separately evaluated Hilbert--Schmidt endpoint (5.3), at their
full bandwidth `X\asymp T` this general diagonal method permits only `k=1`.
Thus it supplies no unconditional higher-trace ladder.  At the project
specialization
`X=Y`, `T=T_CA=Y^(50/33)`, the needed `k=4` case would require

\[
 Y^4\le Y^{(50/33)(2-\varepsilon)};
\]

it fails by the factor

\[
 \frac{Y^4}{Y^{(50/33)(2-\varepsilon)}}
 =Y^{32/33+(50/33)\varepsilon},                   \tag{5.9}
\]

which is already `Y^(32/33)` before the epsilon loss.

The prime-side exponent range can reach `k=3` here (for sufficiently small
fixed epsilon), but not `k=4`.  Their conditional `k=4` hypothesis instead
encodes Hardy--Littlewood-type asymptotics for

\[
 \sum_m(\Lambda*\Lambda)(m)(\Lambda*\Lambda)(m+h),
 \qquad |h|\le X^2/T.                             \tag{5.10}
\]

The scale in (5.10) is exactly adjacent to `CA4`: set the paper's prime cutoff
`X=Y` and its height `T=T_CA`; then `X^2/T` is exactly (5.7).  But the theorem
status and passport go the wrong way.  Equation (5.10) is explicitly
conditional, uses the natural Dirichlet convolution `Lambda*Lambda`, and asks
for an asymptotic shifted-correlation main term.  `CA4` needs an unconditional
upper bound for a translated signed covariance whose four prime-factor
coefficients are the
recomputed adjacent-gap hats.  Thus Section 7.2 independently identifies
the same open arithmetic correlation; it does not estimate it, and (5.3)
contributes no part of the fixed-power gain (5.6).

### 5.3 Full passport comparison

| Field | Alpoge--Furman | Project gate | Result |
|---|---|---|---|
| source | all prime powers `n<=X` with `Lambda(n)/sqrt(n)`, plus archimedean and pole terms | prime-only shell with weights recomputed from predecessor/successor gaps | failed |
| coefficient cone | one fixed natural explicit-formula sequence | signed source-normalized `y` for `DPA/LTRAD`, or positive adaptive hats and their semiprime convolution for `CA4` | failed |
| moment/order | Hilbert--Schmidt second moment (5.3); higher traces only in (5.8) or conditionally | raw prime fourth moment / semiprime second moment | failed |
| resolution | individual log-frequency diagonal for `X<=T`; conditional natural correlations at `X^2/T` | translated near-products at (5.7), with product length exceeding time | failed by (5.5) |
| sign | global zero-side inertia and an unsigned Hilbert--Schmidt norm | one-sided prime-log floor or signed four-distinct covariance | failed |
| normalization | trace normalized so one isolated on-line zero contributes one; result scaled by `N(T,2T)` | `sum y_p=1`, radial source normalization, or the hat `S_2` scale | failed |
| quantifier | asymptotic dyadic zero census; fixed character in Theorem B, or a character/modulus family in the separate remark | every legal shell `Y`, every frequency/window, or an average over shell centers themselves | failed |
| conclusion | positive proportion simple and on the line | exclude even one off-line zero in a fixed strip | failed categorically |

Numerically, even the optimized certificate leaves an uncontrolled fraction
`1-C=.3274993...` of the zero count.  More decisively, the paper states that
its inputs are insensitive to `o(N)` off-line zeros and also hold for
Davenport--Heilbronn and Epstein zeta functions whose RH analogues fail.
Even a hypothetical `1-o(1)` density conclusion would therefore not imply a
uniform strip.

Their separate Dirichlet-family remark averages primitive characters and
moduli with a smooth modulus weight.  It does not average the physical shell
center `Y`, and it never recomputes the adjacent-gap selector, so it is not an
instance of averaged `GCG4` either.

The rank--inertia idea could only become strip-facing after a new
**spectral-edge** theorem controlling the negative part or least eigenvalue
strongly enough to rule out one off-line block.  Trace and Hilbert--Schmidt
data alone are sharp and cannot do this.  Accordingly Alpoge--Furman proves
none of `DPA`, averaged `GCG4`, `CA4`, or `LTRAD`.

## 6. Category-by-category import matrix

| Area and primary result | Exact useful content | Exact mismatch at the project gate |
|---|---|---|
| [Montgomery--Vaughan mean value](https://doi.org/10.1112/jlms/s2-8.1.73) | `int|sum a_n n^(-it)|^2 << (T+N)sum|a_n|^2`; squaring gives `(T+N^2)` for a length-`N` prime polynomial | gives the `Y^2/T` loss; `CA4` needs its fixed-power removal |
| [Guth--Maynard](https://arxiv.org/abs/2405.20552), Theorem 1.1 | `R << T^o(1)(N^2V^-2+N^(18/5)V^-4+TN^(12/5)V^-4)` | prior exact audit gives a full-vector deficit `.650459...`; favorable bin deficit `.290151...`; counts peaks but does not preserve the selector |
| Maynard--Pandey--Radziwill and Chen--Gupta--Li | (4.1), character large values, and improved density | natural additive `Lambda`, wrong averaging variable, and the failures in Section 4 |
| [Alpoge--Furman](https://arxiv.org/abs/2608.13637), Theorems A, B, 5.7 and Section 7.2 | unconditional `2/3` simple on-line and `5/6` distinct; finite-Gabor inertia plus a natural prime-power second moment | sparse off-line sets are invisible; the semiprime reinterpretation retains the `Y^(127/330)` gap; higher traces are unavailable, and conditional `k=4` has the wrong mask |
| [Gafni--Tao](https://arxiv.org/abs/2505.24017) | polynomial exceptional-interval bounds for `theta>2/15`; the project derives `s(gamma)=(45gamma-6)/65` on the licensed branch | already powers the proved retained-hat transition through `Y^.8392`; gives no high-band signed product cancellation |
| [Stadlmann](https://arxiv.org/abs/2212.10867) and [Baker--Harman--Pintz](https://doi.org/10.1112/plms/83.3.532) | mean squared prime gap `O(x^(.23+epsilon))`; maximal-gap exponent `21/40` | already supports hat/Voronoi transfer and endpoints; local gap control is falsified as a route to high-band `CA4` |
| Li's author-hosted *Almost all short intervals III* | claims primes in `[n-n^(1/24+epsilon),n]` outside `O_B(X log^-B X)` starts | much shorter physical scale, but only logarithmic exceptional density; no `Y^(-.019)` deletion, adjacent weights, or Fourier cancellation |
| [Matomaki--Radziwill--Tao](https://arxiv.org/abs/1707.01315) | natural `Lambda`/divisor shifted correlations for almost all shifts once `H>=X^(8/33+epsilon)` | project has `H=X^(8/33)` exactly; epsilon endpoint, log saving, Type-II factor range, and adaptive coefficient failures |
| [Matomaki--Teravainen](https://arxiv.org/abs/2207.05038) and [Evans](https://arxiv.org/abs/2102.12297) | sparse mean values and almost-all correlations for naturally weighted `E_2` numbers | the absolute close-pair term misses binwise `GCG4` by exactly `Y^(3/8)`; no adjacent-gap convolution |
| [Higher Uniformity II](https://arxiv.org/abs/2411.05770) | power/log cancellation for natural or modelled arithmetic functions for almost all additive starts | coefficients, center variable, and fixed-power size mismatch; an exceptional-start theorem need not control the recomputed `Y`-dependent hats |
| [Bettin--Chandee](https://arxiv.org/abs/1502.00769) and Wright II | trilinear reciprocal phases; Wright recognizes two subdyadic variables | friendly full-shell savings `27/220` and at best `1/8`, versus at least `.369192`; separated-slot and reconstruction failures |
| [Bondarenko--Seip GCD sums](https://arxiv.org/abs/1402.0249) | at the critical kernel, `sum gcd(n_k,n_l)/sqrt(n_kn_l) <= N exp(O(sqrt(log N logloglog N/loglog N)))` | only subpolynomial loss control for a GCD kernel; the aligned product-grid sector is already closed, while scattered Bezout residues and the adjacent mask are not a GCD matrix |
| [Lewko--Lewko variational large sieve](https://arxiv.org/abs/1111.6190) and the classical hybrid sieve | arbitrary coefficients and variation/maximal control, with the usual conductor term | arbitrary-coefficient strength keeps the conductor loss; no prime-mask fixed power or signed determinant-offset main cancellation |
| Ramare 2605.29470 | proposed weighted Parseval large sieve | withdrawn for an important miscalculation; unusable |
| [Hu](https://arxiv.org/abs/2608.18956), [Jing--Wu](https://arxiv.org/abs/2608.14467), and [Cushman--Demeter--Wu](https://arxiv.org/abs/2608.12316) | near-optimal exact additive energy on algebraic varieties/surfaces or three-fold energy on lifted convex curves | lifting primes to `(p,log p)` imposes the extra equation `p1+p2=p3+p4`; `CA4` has only a `1/T`-near log-product relation.  Exact lifted energy does not control its signed tube |
| [Wang shell-type bilinear decoupling](https://arxiv.org/abs/2608.19531) | sharp PDE decoupling for shell/paraboloid Fourier support | no embedding preserving the one-dimensional log-prime phase, adaptive weights, and translated kernel |
| [Tang short twisted second moment](https://arxiv.org/abs/2608.14852) and [Conrey--Kwan--Lin--Turnage-Butterbaugh](https://arxiv.org/abs/2607.00282) | reciprocity for zeta twists on intervals of length `T^delta`, `delta>1/2`; power-saving family mean values in character aspects | zeta/automorphic family moments with fixed arithmetic twists, not the raw adjacent-gap polynomial for every `Y`; family averaging cannot exclude one source event |
| [Jaming--Kellay--Saba](https://arxiv.org/abs/2303.10919) and [Avdonin--Moran](https://matwbn.icm.edu.pl/ksiazki/amc/amc11/amc1143.pdf) | finite-band nonharmonic `L^1` for resolved frequencies; cluster divided-difference `L^2` coordinates | no uniform source-normalized, one-sided lower return for unresolved actual-prime clusters; no `Y^(-.0179)` bound |
| [Bellotti zero density](https://arxiv.org/abs/2508.02041) | `O(1)` zeros sufficiently near the moving Vinogradov--Korobov boundary | `O(1)` is not zero; one exceptional zero is fatal, and the boundary is not a fixed strip |

Modern GCD sums and lifted additive-energy theorems therefore explain or
close already structured sectors, but do not touch the first open
four-distinct covariance.  Decoupling would require adding a curvature
coordinate; that changes the incidence relation rather than estimating it.

## 7. Gate conclusions and research reframe

### 7.1 `DPA_P(.019)`

The only directly productive prime-distribution import remains Gafni--Tao,
already used in the project to prove the exact frozen-hat approximation up
to `Y^.8392`.  Neither the newer additive prime-sum theorem nor shorter
almost-all prime intervals extends the uniform prime-log floor above that
height.  The high band remains an actual-prime signed-covariance problem.

### 7.2 Pointwise and averaged `GCG4/CA4`

Wright II updates the vocabulary but not the feasibility estimate: current
Kloosterman technology can recognize subdyadic blocks, yet its first term
has a `1/8` ceiling in the friendliest serialization.  A black-box
`CA4 -> Wright II` project should therefore be stopped; it fails the
exponent test even before its missing adapter is built.

The theorem one would actually need must do all of the following at once:

```text
improve the unchanged A^(1/2) Kloosterman term;
retain four adjacent-gap-derived factor weights;
keep the translated kernel signs until the global sum;
control the zero/main sector with a fixed-power error;
recombine short blocks and dual modes with a square-function norm;
work for every Y and all time windows, or average in Y itself.
```

That is genuinely new selector-sensitive dispersion, not a routine
serialization of an existing theorem.

The center-averaged target (1.5) receives no special benefit from the
surveyed almost-all results: they average additive starts, characters, or
moduli, while (1.5) recomputes the predecessor/successor mask at every shell
center.  Moreover, the project's hostile inverse-density model shows that
an averaged upper moment does not automatically couple to lower
radialization.

### 7.3 `LTRAD_P(.0189,.001)`

Nothing in the new prime, Kloosterman, density, or decoupling literature has
the lower-return polarity of (1.7).  Jaming--Kellay--Saba plus
Avdonin--Moran remains the closest analytic blueprint, but the missing step
is still a source-weighted, cluster-aware nonharmonic Littlewood theorem for
the actual prime frequencies.  Prime density and gap theorems cannot supply
source normalization, as the project's density-preserving countermodel
already demonstrates.

### 7.4 Durable status

| Statement | Status after this survey |
|---|---|
| frozen-hat floor through `Y^.8392` | **PROJECT-PROVED using prior imports** |
| Wright II direct `CA4/GCG4` import | **REFUTED by exponent and passport tests** |
| Maynard--Pandey--Radziwill direct gate import | **REFUTED by phase/coefficient/quantifier tests** |
| Alpoge--Furman density theorem | **VALID PRIOR IMPORT; direct strip/`CA4` adapter REFUTED** |
| pointwise `CA4` / global `GCG4` | **OPEN** |
| center-averaged actual-prime `GCG4` | **OPEN** |
| signed `DPA_P(.019)` | **OPEN** |
| `LTRAD_P(.0189,.001)` | **OPEN** |
| contemplated uniform zero-free strip | **OPEN** |
| RH | **OPEN** |

No percentage of completion follows from this literature audit.
