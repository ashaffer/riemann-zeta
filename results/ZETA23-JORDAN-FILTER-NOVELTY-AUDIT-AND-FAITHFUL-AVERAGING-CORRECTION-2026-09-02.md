# Jordan/filter novelty audit and faithful-averaging correction

Date: 2026-09-02  
Status: corrected classifier theorems and route audit; no zero-free strip or RH  
Passport:
[zeta23_jordan_filter_radical_preflight_v1.json](context/zeta23_jordan_filter_radical_preflight_v1.json)

> **Later same-day provenance correction.**  The abstract causal-box
> multiplier calculation below is classical, and the zeta fixed-box
> specialization has explicit local predecessors in R67
> (`FIXED-BOX-PRIME-TRANSFER-CHECKPOINT.md`) and R68
> (`ACTUAL-PRIME-REFLECTION-TRANSFER-CHECKPOINT.md`).  The primitive
> hierarchy remains useful project synthesis, but the fixed-box zeta
> coordinate must not be described as an immediate new application of this
> report.

## 0. Outcome

The endpoint-flat theorem survives, but two claims about its significance do
not.

1. The equality of the two unit-block Jordan exponents with the rightmost
   singularity abscissa is a direct Landau-oscillation corollary, not credible
   literature-level novelty.  In the zeta specialization it is another exact
   coordinate for the already classical PNT-error/zero-free-region
   equivalence and the repository's earlier R95 and R103 spectrometers.
2. The complete adaptive-mask cone is minimal only if the task is to recover
   the Jordan mass of the *same raw response*.  It is not the minimal scalar
   strip socket.  A causal box average, a fixed primitive, or many other
   faithful fixed filters retain every nontrivial zeta-zero pole and admit a
   one-sided strip criterion without reconstructing the raw Jordan mass.

The audit proves a corrected theorem suite:

- sharp bilateral inequalities between the two Jordan abscissae;
- a multiplicity-sensitive pole-valuation theorem for filter banks;
- generic collapse of every finite bank to one fixed scalar projection;
- fixed-box and fixed-primitive strip criteria forming a strict hierarchy,
  which refutes global minimality of the raw Jordan premise;
- exact Lipschitz grid compression for the raw adaptive mask, at a quantified
  and generally exponential resolution cost;
- partition, subcritical-perturbation, and variable-order scope theorems; and
- countermodels for adaptive orientation, moving windows, blind positive
  smoothing, and unnormalized growing order.

These are useful project-level corrections and organization.  No
literature-level new theorem is claimed.  The only potentially distinctive
package left by the bounded search is the tailored positive ordinary-prime
Euler product in the predecessor report.  Its controlled label is
`NOVELTY_UNRESOLVED`, so it is not promoted as new.

## 1. Claim map

| statement | mathematical status | controlled novelty label | note |
|---|---|---|---|
| positive block exponent equals Laplace abscissa | proved | `IMPORTED` | classical root test/Landau setting |
| bilateral Jordan inequalities, Theorem 2.1 | proved | `PROJECT_SYNTHESIS` | elementary Landau packaging |
| endpoint-flat exponents equal `Theta` | proved from standard explicit-formula upper bound | `LOCAL_PREDECESSOR` | classical corollary; closely preceded by R95/R103 |
| multiplier pole valuation | proved | `PROJECT_SYNTHESIS` | elementary local meromorphic algebra |
| finite-bank generic scalar projection | proved | `PROJECT_SYNTHESIS` | Baire/linear-algebra packaging |
| causal-box and primitive criteria | proved | `LOCAL_PREDECESSOR / PROJECT_SYNTHESIS` | box calculus is classical and the zeta fixed-box coordinate is in R67/R68; the primitive hierarchy is project synthesis |
| Lipschitz grid-mask compression | proved | `PROJECT_SYNTHESIS` | elementary approximation applied to the project response |
| growing-order attenuation | proved | `PROJECT_SYNTHESIS` | Stirling scope correction |
| positive Euler-product falsifier with an arbitrarily long genuine zeta head | algebra proved in predecessor | `NOVELTY_UNRESOLVED` | plausibly distinctive packaging; not promoted |
| subcritical actual-prime one-sided estimate | open | -- | no claim exists yet; this would be real new arithmetic |
| uniform zero-free strip | open | `IMPORTED` | famous open target; unchanged |
| RH | open | `IMPORTED` | famous open target; unchanged |

## 2. Bilateral Jordan-abscissa rigidity

Let `mu` be a real locally finite signed Radon measure on `[0,infinity)`,
with Jordan decomposition

\[
 \mu=\mu_+-\mu_-.
\]

For `I_n=[n,n+1)`, put

\[
 \alpha_\pm(\mu)
 =\limsup_{n\to\infty}\frac1n\log\mu_\pm(I_n),
 \qquad \log0=-\infty,
 \tag{2.1}
\]

and

\[
 \alpha_{|\cdot|}(\mu)=\max\{\alpha_+(\mu),\alpha_-(\mu)\}.
\]

Assume this last number is finite.  Its Laplace transform is initially

\[
 F_0(s)=\int_{[0,\infty)}e^{-st}\,d\mu(t),
 \qquad \Re s>\alpha_{|\cdot|}(\mu).
 \tag{2.2}
\]

### Lemma 2.1: block exponent

For every nonnegative locally finite measure `nu`, the abscissa of convergence
of its Laplace transform is

\[
 \alpha(\nu)=
 \limsup_{n\to\infty}\frac1n\log\nu(I_n).
 \tag{2.3}
\]

Indeed, on `I_n` the factor `e^{-sigma t}` differs from `e^{-sigma n}`
by a constant depending only on `sigma`.  Convergence is therefore equivalent
to convergence of

\[
 \sum_ne^{-\sigma n}\nu(I_n),
\]

and (2.3) is the root test.  Landau's positive-transform theorem says that a
finite abscissa in (2.3) is a singular point of the defining transform.

### Theorem 2.1: sharp bilateral inequalities

Suppose `F_0` has a single-valued meromorphic continuation `F` to

\[
 \mathbb H_c=\{s:\Re s>c\}
\]

and `F` is holomorphic at every real `s>c`.  Then

\[
 \boxed{
 \alpha_+(\mu)\le\max\{\alpha_-(\mu),c\},\qquad
 \alpha_-(\mu)\le\max\{\alpha_+(\mu),c\}.}
 \tag{2.4}
\]

In particular,

\[
 \alpha_{|\cdot|}(\mu)>c
 \quad\Longrightarrow\quad
 \alpha_+(\mu)=\alpha_-(\mu)=\alpha_{|\cdot|}(\mu).
 \tag{2.5}
\]

If

\[
 \vartheta(F;c)=
 \sup\{\Re\rho:\rho\in\mathbb H_c
       \text{ is a nonremovable singularity of }F\}>c,
 \tag{2.6}
\]

then

\[
 \alpha_+(\mu)=\alpha_-(\mu)\ge\vartheta(F;c).
 \tag{2.7}
\]

If also, for every `epsilon>0`,

\[
 |\mu|(I_n)\ll_\varepsilon
 e^{(\vartheta(F;c)+\varepsilon)n},
 \tag{2.8}
\]

then both exponents in (2.7) equal `vartheta(F;c)`.

#### Proof

Write `a_+=alpha_+(mu)` and `a_-=alpha_-(mu)`.  In the initial half-plane,

\[
 {\cal L}\mu_+=F+{\cal L}\mu_-.
 \tag{2.9}
\]

The right side continues the positive transform to
`Re(s)>max(c,a_-)` and is holomorphic at every real point there.  If
`a_+>max(c,a_-)`, it would be holomorphic at its positive-transform
abscissa, contradicting Landau.  This proves the first inequality in (2.4).
Apply the same argument to `-mu` for the second.

The defining integral (2.2) is holomorphic for
`Re(s)>alpha_|.|(mu)`.  Hence every continued nonremovable singularity has
real part at most `alpha_|.|(mu)`.  Equations (2.5), (2.7), and the upper
bound (2.8) follow.

### Corollary 2.2: one part suffices

If `F` is meromorphic and real-axis clean in `Re(s)>a`, and either

\[
 \alpha_+(\mu)\le a
 \quad\hbox{or}\quad
 \alpha_-(\mu)\le a,
\]

then `F` is holomorphic throughout `Re(s)>a`.

This is the correct abstract content of Theorem 4.1 in the endpoint-flat
report.  It is an immediate use of Landau's theorem, not new oscillation
theory.

## 3. Zeta specialization and provenance correction

For the endpoint-flat response, write

\[
 U(s)=-\frac{\zeta'}{\zeta}(s)-\frac1{s-1},
 \qquad
 H_r(s)=\frac{s-1}{s(s+1)\cdots(s+r+1)}.
 \tag{3.1}
\]

Then the transform of `b_r(t)=B_r(e^t)` is `H_r(s)U(s)`.  At every
nontrivial zeta zero `rho`, `U` has a *simple* pole, even if `rho` is a
multiple zero of zeta, and

\[
 H_r(\rho)\ne0.
\]

The standard explicit-formula estimate gives

\[
 |b_r(t)|\ll_{r,\varepsilon}e^{(\Theta+\varepsilon)t},
 \qquad
 \Theta=\sup_\rho\Re\rho.
 \tag{3.2}
\]

Theorem 2.1 therefore gives

\[
 \alpha_+(b_r)=\alpha_-(b_r)=\Theta.
 \tag{3.3}
\]

Equation (3.3) is sound.  Its corrected provenance is:

- Landau's theorem already turns a real-axis-clean nonreal Mellin
  singularity into two-sided oscillation;
- Kaczorowski--Pintz prove much more about frequency and size of such
  oscillations;
- Mahatab--Mukhopadhyay explicitly develop positive/negative and
  measure-theoretic versions;
- Han's 2025 smooth-weighted PNT paper proves closely related
  zero-spectrum/max/mean-absolute-error equivalences; and
- locally, R95 already gives a faithful fixed one-sided ramp criterion and
  R103 already gives an exact `Theta` sign spectrometer.

Thus (3.3) is best described as a clean endpoint-flat specialization and
coordinate, not a new theorem of oscillation theory.

The same correction applies to the fixed-box specialization in Section 5:
R67 already derived the fixed-box prime-transfer coordinate, and R68 gave
its complete centered actual-prime Type-II form.  Section 5 supplies a more
general filter classification, not a first zeta fixed-box reduction.

## 4. Correct filter invariant: local valuation, not only radical

Let `U` be meromorphic and let

\[
 F_j(s)=H_j(s)U(s)+E_j(s),\qquad 1\le j\le m,
 \tag{4.1}
\]

where the `H_j` and `E_j` are holomorphic near a source pole `rho`.  If `U`
has pole order `m_rho` and `H_j` has zero order `nu_j(rho)`, then `F_j` has
pole order

\[
 d_j(\rho)=(m_\rho-\nu_j(\rho))_+.
 \tag{4.2}
\]

The bank's surviving pole order is therefore

\[
 d_{\cal H}(\rho)
 =\max_j d_j(\rho)
 =\left(m_\rho-\min_j\nu_j(\rho)\right)_+.
 \tag{4.3}
\]

For simple source poles, (4.3) reduces to the common-zero radical criterion.
For higher-order poles it does not.  If

\[
 U(s)=(s-\rho)^{-2},\qquad H_1(s)=H_2(s)=s-\rho,
\]

the filters have a common zero, but both outputs retain a simple pole.

### Theorem 4.1: a finite bank has a fixed generic scalarization

There is a fixed real coefficient vector `a=(a_1,...,a_m)`, selectable in
any prescribed nonempty cone open in the full space `R^m`, such that

\[
 H_a=\sum_ja_jH_j
 \tag{4.4}
\]

retains every source pole retained by the bank, with the largest bank-visible
order at that pole.

#### Proof

At a retained pole, take the coefficient of the highest surviving principal
part in `sum a_jH_jU`.  Its cancellation is one proper real linear subspace
of coefficient space.  A meromorphic function has only countably many poles
in the half-plane.  A countable union of proper closed subspaces cannot cover
an open set, by Baire category.  Choose `a` outside that union.

This is a local divisor statement.  It is not a Wiener inversion theorem and
does not provide a quantitative Bezout/corona norm.  In particular, absence
of common zeros does not by itself preserve a fixed exponential *inverse*
bound.  Weighted Wiener theory needs additional regularity/nonquasianalytic
hypotheses, and pure exponential weights are exactly a delicate boundary.

### Componentwise one-sided consequence

Suppose each `f_j` is a real signed locally finite measure or function of
finite absolute block exponent, its Laplace transform continues as `F_j` in
(4.1), and one orientation is fixed for each response with

\[
 \alpha_{\varepsilon_j}(f_j)\le a
\]

for every `j`, where each continued `F_j` is real-axis clean in `Re(s)>a`.
Corollary 2.2 makes every `F_j` holomorphic there.  Consequently every source
pole to the right of `a` must be killed to its full multiplicity by every
filter.  A jointly faithful bank excludes all such source poles.

Equality between a bank Jordan exponent and its surviving spectral abscissa
still needs an absolute block-growth upper bound.  Singularities alone give
the lower bound, not equality.

## 5. Faithful averaging: the minimality correction

### Theorem 5.1: causal box criterion

Let `f` be locally integrable of finite exponential order on `[0,infinity)`,
extended by zero to the negative axis.  For `L>0`, define

\[
 g_L(t)=\int_{\max(0,t-L)}^tf(u)\,du.
 \tag{5.1}
\]

Then

\[
 {\cal L}g_L(s)=K_L(s){\cal L}f(s),
 \qquad
 K_L(s)=\frac{1-e^{-Ls}}s,\qquad K_L(0)=L.
 \tag{5.2}
\]

The nonzero roots of `K_L` are `2*pi*i*k/L`; in particular it is zero-free
in `Re(s)>0`.

More generally, the positive compact kernel
`e^(a v) 1_[0,L](v)` has multiplier
`(1-e^(-L(s-a)))/(s-a)`, whose zeros lie on `Re(s)=a`.  Its convolution
powers are compact exponential B-splines.  This filter algebra is classical;
the strip corollary below is an immediate application, not a novelty claim.

For every fixed endpoint order `r` and fixed `L>0`, put

\[
 g_{r,L}(t)=\int_{\max(0,t-L)}^tb_r(u)\,du.
\]

Then

\[
 \alpha_+(g_{r,L})=\alpha_-(g_{r,L})=\Theta.
 \tag{5.3}
\]

For `0<a<1`, either pointwise estimate

\[
 g_{r,L}(t)\ge-Ce^{at}
 \quad\hbox{or}\quad
 g_{r,L}(t)\le Ce^{at}
 \tag{5.4}
\]

implies \(\zeta(s)\ne0\) in \(\Re s>a\).

The proof is (5.2), noncancellation, the upper bound inherited from (3.2),
and Corollary 2.2.  Unlike the raw Jordan support function, (5.4) uses one
fixed translated test.

Raw Jordan control implies the corresponding box lower bound, since

\[
 (g_L(t))_-
 \le\int_{t-L}^t f_-(u)\,du.
\]

The converse fails.  Let

\[
 h(t)=e^{at}\sin(e^{ct}),\qquad f=h',\qquad c>0.
\]

Every fixed box integral of `f` is `h(t)-h(t-L)=O(e^{at})`, while both raw
Jordan masses of `f` have exponent `a+c`.  Thus the fixed-box premise is
strictly weaker on the ambient function class.

### Theorem 5.2: a strict hierarchy of faithful scalar premises

For a fixed integer `m>=1`, let

\[
 I^mf(t)=\frac1{(m-1)!}\int_0^t(t-u)^{m-1}f(u)\,du.
 \tag{5.5}
\]

Its multiplier is `s^{-m}`, which is nonzero in `Re(s)>0`.  Hence

\[
 \alpha_+(I^mb_r)=\alpha_-(I^mb_r)=\Theta
 \tag{5.6}
\]

for every fixed `m`, and either one-sided `O(e^{at})` bound for `I^mb_r`
implies the strip `Re(s)>a`.

Moreover, for `a>0`,

\[
 I^mf(t)\ge-Ce^{at}
 \quad\Longrightarrow\quad
 I^{m+1}f(t)\ge-\frac Ca e^{at}+O(1),
 \tag{5.7}
\]

and similarly for the upper orientation.  These sufficient premises form a
descending chain.  Each implication is strict for general functions: apply
successive derivatives to the chirp `h` above.  Explicitly, with
`f=h^(m+1)`, repeated integration gives `I^(m+1)f=h+P_m` but
`I^m f=h'+P_(m-1)` for fixed polynomials `P_j`; the former is
`O(e^(at))`, while both orientations of the latter have exponent `a+c`.
Thus no member of this
primitive hierarchy is minimal, and in particular the raw Jordan premise is
not globally minimal across faithful filters.  This does not assert that the
partially ordered class of every conceivable sufficient predicate has, or
lacks, an artificial least element.

The endpoint-flat report's minimality statement remains valid only in its
literal scope: among nonnegative additive corrections `q` for which
`f+q>=0`, the smallest is `q=f_-`.  It cannot be promoted to a comparison
between different filters.

This also corrects the stop rule.  A faithful fixed filter cannot improve the
spectral exponent, but it may still change arithmetic proof complexity.
Filter design is worthwhile only when accompanied by a concrete arithmetic
advantage, not when sold as spectral contraction.

## 6. Raw masks versus detector filters

For the raw response on one block,

\[
 \int f_-
 =\sup_{0\le h\le1}-\int hf.
 \tag{6.1}
\]

This is an exact support-function identity.  It creates a *reconstruction*
socket, denoted `J`.  A fixed translated mask instead creates a convolution
output with its own multiplier; that is a distinct *filter* socket, denoted
`F`.  Confusing `J` and `F` caused the earlier route overclaim.

### Theorem 6.1: Lipschitz grid compression

Let `f` be `L`-Lipschitz on an interval of length one, and let `Pi` be a
partition of mesh at most `delta`.  Define

\[
 S_\Pi^-(f)=\sum_{I\in\Pi}\left(-\int_If\right)_+.
 \tag{6.2}
\]

Then

\[
 0\le\int f_- -S_\Pi^-(f)\le\frac{L\delta}{2}.
 \tag{6.3}
\]

On a cell which does not change sign, equality holds.  On a changing cell of
length `ell`, the defect is

\[
 \min\left(\int_If_+,\int_If_-\right).
\]

A zero in the cell and Lipschitz continuity give
`integral_I |f| <= L ell^2/2`.  Summing and using
`sum ell^2<=delta` proves (6.3).

The order `L*delta` is sharp.  Alternating centered ramps of slopes `+L` and
`-L` on equal cells form a globally continuous `L`-Lipschitz triangular
wave with zero cell integrals and total negative mass `L*delta/8`; a smooth
sine version gives `L*delta/(2*pi^2)`.

For `r>=1`, the endpoint-flat response obeys

\[
 \operatorname{Lip}(b_r;[T,T+1])\ll_re^T.
 \tag{6.4}
\]

Consequently a target exponent `a<1` can use a grid with

\[
 \delta_T\le e^{-(1-a+\kappa)T},
 \tag{6.5}
\]

whose approximation error is `O(e^{(a-kappa)T})`.  Complete measurable masks
are therefore not literally necessary under the available regularity.  But
the grid has about

\[
 e^{(1-a+\kappa)T}=x^{1-a+\kappa}
\]

cells and an unstructured binary cone of twice-exponential cardinality in
`T`.  Lipschitz compression exposes a mask-entropy gate; it does not solve it.

### Bounded-variation reconstruction barrier

If `0<=h<=1`, `Var(h)<=V`, and `Omega=2*pi*m`, integration by parts gives

\[
 \left|\int_0^1h(u)e^{i\Omega u}\,du\right|
 \le\frac{V+2}{\Omega}.
 \tag{6.6}
\]

But

\[
 \int_0^1(\cos\Omega u)_-\,du=\frac1\pi.
\]

Thus fixed-fraction reconstruction of the raw Jordan mass at frequency
`Omega` needs variation of order `Omega`.  This says nothing against a fixed
low-variation filter whose multiplier is merely nonzero at that frequency:
however small its fixed coefficient, it preserves the horizontal exponent.

## 7. Which window changes preserve the exponent?

Let `nu>=0` and let

\[
 0=t_0<t_1<t_2<\cdots,
 \qquad
 0<\ell_-\le t_{n+1}-t_n\le\ell_+<\infty.
 \tag{7.1}
\]

Then the Laplace abscissa is also

\[
 \limsup_{n\to\infty}
 \frac1{t_n}\log\nu([t_n,t_{n+1})).
 \tag{7.2}
\]

Indeed, the bounded upper width makes the exponential weight uniformly
comparable to its left-endpoint value, while the lower width gives
`t_n>=n ell_-`, so the usual root-test comparison converges.

Both density controls matter for the left-endpoint coordinate:

- for `t_n=log(n+1)` and `dnu=e^{theta t}dt`, exponentially shrinking cells
  give exponent `theta-1`, not `theta`;
- for `t_n=2^n` and `theta>0`, unbounded cells give exponent `2 theta`, not
  `theta`.

Thus “bounded-width covering partition” must include an upper cell-density
condition.  More generally, the replacement “at most `e^{o(T)}` cells per
unit interval” is valid here only while retaining uniformly bounded cell
diameter (or another explicit sublinear-diameter hypothesis).
Existential moving or shrinking windows are not substitutes for a fixed
covering coordinate.

## 8. Stable and unstable changes

### 8.1 Subcritical perturbations are stable

If

\[
 \alpha_+(f)=\alpha_-(f)=\vartheta
\]

and the absolute block exponent of `g` is strictly smaller than `vartheta`,
then

\[
 \alpha_+(f+g)=\alpha_-(f+g)=\vartheta.
 \tag{8.1}
\]

This follows from

\[
 (f+g)_\pm\le f_\pm+|g|,
 \qquad
 f_\pm\le(f+g)_\pm+|g|.
\]

Strict inequality is essential: `g=-f` cancels an equal-exponent response.

### 8.2 Growing endpoint order can fake a saving

For fixed `z` outside `{1,0,-1,-2,...}`, the endpoint-flat multiplier is

\[
 H_r(z)=\frac{(z-1)\Gamma(z)}{\Gamma(z+r+2)}.
 \tag{8.2}
\]

Stirling gives

\[
 \log|H_r(z)|
 =-r\log r+r-\left(\Re z+\frac32\right)\log r+O_z(1).
 \tag{8.3}
\]

If `r_N~cN/log N`, then

\[
 |H_{r_N}(z)|=e^{-cN+o(N)}.
 \tag{8.4}
\]

A blockwise variable-order filtered mode can therefore display an exponent
smaller by `c` even though the source singularity did not move.  Removing the
explicit factorial does not eliminate the issue:

\[
 (r+1)!H_r(z)
 =(z-1)\Gamma(z)r^{-z}(1+O_z(r^{-1})),
 \tag{8.5}
\]

so, when `Re(z)>0` as for nontrivial zeta zeros, `r_N=e^{cN}` again creates
exponential attenuation.  More fundamentally,
`r=r_N` produces no single fixed Laplace transform.  A Landau argument fixes
the filter before height tends to infinity; a variable family needs a new
uniform reconstruction theorem and a subexponential nondegeneracy ledger.

### 8.3 Exact quantifier countermodels

1. **Real-axis regularity.**  For `f(t)=e^{theta t}`, the transform has a real
   pole at `theta`, `alpha_+=theta`, and `alpha_-=-infinity`.
2. **Absolute upper bound.**  Add
   `e^{lambda t}sin(e^t)`, `lambda>theta`, to a mode with poles on
   `Re(s)=theta`.  The chirp has an entire continued transform but both Jordan
   exponents `lambda`; visible poles give only a lower bound.
3. **Adaptive block orientation.**  For
   `f(t)=(-1)^floor(t)e^{theta t}`,

   \[
    F(s)=\frac{\tanh((s-\theta)/2)}{s-\theta}.
   \]

   It is real-axis clean and has nonreal poles on `Re(s)=theta`.  Both fixed
   Jordan exponents are `theta`, but a sign chosen after seeing each block
   selects zero mass every time.
4. **Moving empty windows.**  Fix `0<delta<1` and let `p` be `4`-periodic, equal to `1` on
   `[0,delta]`, `-1` on `[2,2+delta]`, and zero elsewhere in a period.  It
   has zero mean and a nonzero odd Fourier coefficient.  Hence

   \[
    f(t)=e^{\theta t}p(t),\qquad
    F(s)=\frac{\int_0^4p(u)e^{-(s-\theta)u}\,du}
                  {1-e^{-4(s-\theta)}}
   \]

   is real-axis clean at `s=theta`, retains nonreal poles on
   `Re(s)=theta`, and has a unit empty interval in every period.
5. **Positive smoothing can be blind.**  For `z=theta+i gamma`, take a
   compactly supported `phi>=0` on `[0,infinity)`, extend it by zero to the
   negative axis, take `L=pi/|gamma|`, and put

   \[
    k(u)=\phi(u)+e^{\theta L}\phi(u-L).
   \]

   Then `k>=0` but its Laplace multiplier vanishes at `z`.
6. **Infinite/adaptive banks.**  Collective pole coverage can migrate with
   height so no fixed member attains the edge.  Finite-bank Baire
   scalarization does not extend to an unstructured height-adaptive choice.

## 9. Literature frontier audit

The primary-source audit changes the novelty and route assessment as follows.

| literature result | exact overlap | consequence here |
|---|---|---|
| [Landau, 1905](https://eudml.org/doc/158244), as stated in [Kaczorowski--Pintz, 1986](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1986.Kaczorowski_1.pdf) | a real-axis-clean boundary of a Mellin transform forces sign changes; Kaczorowski--Pintz add frequency and size | Theorem 2.1 is a corollary/package, not new oscillation theory |
| [Mahatab--Mukhopadhyay, Theorems 3.1--3.5](https://arxiv.org/html/1512.03144v4#S3) | explicitly splits positive and negative excursions and proves measure/L2 lower bounds from nonreal singularities | strongly overlaps the Jordan-mass motivation |
| [Han, Theorem 1.1 and Proposition 2.5](https://arxiv.org/html/2505.23795v1#S2) | smooth weighted PNT error versus zero-free regions; zero scale equivalent to max and mean absolute error scales | broad smooth-detector/ZFR framing is already current literature; Han does not state the fixed-sign unit-log-block identity |
| [Révész, 2022](https://arxiv.org/abs/2202.01837) and [Schlage-Puchta, 2019](https://arxiv.org/abs/1912.00853) | a given zero forces large, localized PNT oscillation; Révész obtains near-sharp constants in Beurling systems | much stronger zero-to-oscillation information is known than mere exponent equality |
| [Broucke, 2025](https://arxiv.org/abs/2507.13780) | refines zero-free-region/PNT-error transfer and constructs near-sharp Beurling examples with prescribed zero contours | generic Tauberian improvement cannot be mistaken for zeta-specific arithmetic progress |
| [Hardy--Littlewood, 1916](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1916.Hardy.pdf) | classical Riesz smoothing has nonzero gamma-ratio zero coefficients | endpoint/Riesz smoothing is established technology |
| [Unser--Blu, 2005](https://bigwww.epfl.ch/publications/unser0503.pdf) | compact exponential boxes, their convolution splines, and product Fourier multipliers | the box/B-spline transfer calculus in Section 5 is classical |
| [Wiener, 1932](https://doi.org/10.2307/1968102) and [Bingham--Inoue, Theorem 4.1](https://eprints.lib.hokudai.ac.jp/repo/huscap/all/18902/JMAA250-2.pdf) | systems of Mellin kernels and absence of common zeros | common-zero bank language is classical; our local multiplicity valuation is not a new Wiener theorem |
| [Dales--Hayman, 1981](https://www.numdam.org/articles/10.5802/aif.852/) | weighted Beurling-algebra Tauberian theory and its nonquasianalytic hypotheses | qualitative coverage must not be advertised as fixed-exponential quantitative inversion |
| [Broucke--Debruyne--Vindas, 2020](https://arxiv.org/abs/2001.01635) and [Debruyne, 2024](https://arxiv.org/abs/2411.03809) | entire pole-subtracted transforms can coexist with arbitrarily slow remainders; quantitative Tauberian remainders require width and growth hypotheses | continuation or smoothing alone supplies no exponential upper bound |
| [Ramakrishnan](https://www.its.caltech.edu/~dinakar/papers/mildTcheb-JNT.pdf), [Grosswald--Schnitzer](https://msp.org/pjm/1978/74-2/pjm-v74-n2-p09-s.pdf), and [Bochkov--Romanov](https://arxiv.org/abs/2106.15949) | positive-type Euler methods, modified prime Euler products, and Helson zetas with flexible zeros | close but nonidentical antecedents to the tailored ordinary-prime falsifier |
| [Bellotti, 2025](https://arxiv.org/abs/2508.02041) | an absolute-constant zero-density estimate near the left edge of the Korobov--Vinogradov region and the corresponding optimal PNT error | substantially sharpens near-edge counting/error transfer but does not exclude a single fixed-right zero |
| [Bellotti--Trudgian--Yang, 2026](https://arxiv.org/abs/2603.21490) | an explicit region `sigma >= 1-1/(4.896 log t)` for `t>=3` | updates the explicit baseline, but the width still tends to zero and gives no uniform strip |
| [Guth--Maynard, 2024/2026](https://arxiv.org/abs/2405.20552) | frontier zero-density and large-value estimates | important for global counts, but such density estimates still permit a single exceptional rightmost zero; already imported elsewhere in the repository |

Bounded, non-exhaustive searches on 2026-09-02 of arXiv, journal
repositories, GitHub, and public AI-assisted RH repositories found no exact
public match for the complete
Jordan/filter classifier package or for the falsifier's exact bundle of
ordinary prime nodes, an arbitrarily long genuine zeta head, a prescribed
off-axis zero pair, and positivity of both coefficient cones.
That is **not** an absence proof: search cannot cover private, unpublished,
unindexed, or differently phrased human/AI work.  Therefore the controlled
label for that bundle is `NOVELTY_UNRESOLVED`, never `CANDIDATE_NEW`, until
specialist review.  It is plausibly distinctive project packaging, but its
ingredients are elementary, so even a positive novelty verdict would make it
a useful falsifier rather than deep strip mathematics.  The dated databases,
representative queries, identifiers, and labels are recorded in the
[machine-readable novelty audit](context/zeta23_jordan_filter_novelty_audit_v1.json).

## 10. Corrected decision tree

```text
uniform zero-free strip
|
+-- fixed faithful scalar response
|   |
|   +-- R95 bounded one-front ramp          already present
|   +-- raw endpoint Jordan mass
|   |   +-- exact adaptive masks            reconstruction identity
|   |   `-- fine grid masks                 same target, quantified entropy
|   +-- causal box / B-spline average       fixed-test alternative
|   `-- fixed primitive hierarchy           strict descending family
|
+-- finite fixed filter bank
|   +-- pole valuation coverage             qualitative classifier
|   `-- quantitative inverse                needs a corona/conditioning theorem
|
+-- blind or growing/adaptive filters
|   +-- fixed multiplier zero               detects only surviving poles
|   `-- sign/order/window chosen with T      no fixed-transform Landau socket
|
+-- zeta-specific arithmetic engine
|   +-- exact all-prime nonlinear identity
|   +-- functional equation / zero correlation
|   `-- coefficient-sensitive one-sided inequality
|
+-- independent architectures
    +-- QP/Turan: DPA_P(.019) AND LTRAD_P(.0189,.001)
    `-- Weil: zeta-specific adjacent-support propagation
```

The box and primitive observations correct the endpoint branch but do not yet
outrank R95: R95 already supplies a bounded, one-front, uniformly faithful
fixed response.  The correct next comparison is arithmetic, not spectral.
The fixed-box row also does not outrank R67/R68, which already contain its
zeta-specific prime and Type-II transfer.
For each fixed faithful filter, require an explicit passport recording:

1. exact prime-power weights and continuum term;
2. coefficient range, number of fronts, and variation;
3. exact identities or integrality unavailable to the positive Euler
   countermodel;
4. the one-sided estimate to be proved from known inputs; and
5. an honest delta against R95, R103, Han, and classical Riesz means.

Unless a candidate wins one of those arithmetic columns, it is duplicate
detector engineering and should stop.

## 11. What genuinely remains at the frontier

The project does not currently possess a literature-new theorem that advances
the strip.  The frontier statement is narrower:

> Find a fixed faithful actual-prime response whose one-sided subcritical
> estimate follows from a zeta-specific source law not retained by the smooth
> positive-density and positive Euler-product countermodels.

The new law must use something such as exact all-prime local factors in a
nonlinear way, the functional equation coupled to arithmetic coefficients, or
a target-conditioned zero/prime correlation.  Positivity, PNT, moments,
arbitrarily long finite zeta Euler heads, generic smoothing, and qualitative no-common-zero
coverage have all been separated from that task.

The highest-information immediate experiment is a head-to-head passport for
the already faithful R95 ramp, the R67/R68 causal-box coordinate, and the
first fixed primitive.  It should be terminated immediately unless the new weight
exposes an exact arithmetic identity absent from R95/R103.  Parallel effort
should remain on the independent QP/Turan and Weil first-open edges rather
than treating another equivalent detector as progress.

## 12. Replay and trust

Finite witnesses and algebraic scope checks are replayed by

```text
python3 -m pytest -q \
  src/test_jordan_detector_calculus.py \
  src/test_endpoint_flat_riesz_landau.py \
  src/test_pole_killing_boundary_calculus.py \
  src/test_shifted_psi_ramp_bridge.py
```

This replay passes all 69 tests in the current workspace.

The new module verifies the box multiplier, adaptive-orientation transform,
grid-mask bound, higher-pole survival, and endpoint-order attenuation.  The
analytic theorems in this report are manuscript proofs, not Lean-formalized
claims.  Literature results are imported at the cited scope.  No finite
calculation is used as asymptotic evidence for a strip.
