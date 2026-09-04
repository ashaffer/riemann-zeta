# Endpoint-flat Jordan mass and the Riesz-variation gate

Date: 2026-09-01  
Status: corrected exact reduction; no zero-free strip proved  
Passport:
[zeta23_endpoint_flat_jordan_mass_preflight_v1.json](context/zeta23_endpoint_flat_jordan_mass_preflight_v1.json)

> **Correction notice (2026-09-02).**  Theorem 5.1 remains valid, but it is
> a classical Landau consequence in an endpoint-flat coordinate, not a
> literature-new oscillation theorem.  The adaptive-mask cone is minimal
> only for reconstructing the Jordan mass of this same raw response.  It is
> not the minimal strip socket: one fixed causal box average or any fixed
> primitive is also faithful and gives a strictly weaker sufficient premise
> on the ambient function class.  See the
> [full novelty and faithful-averaging correction](ZETA23-JORDAN-FILTER-NOVELTY-AUDIT-AND-FAITHFUL-AVERAGING-CORRECTION-2026-09-02.md).

## 0. Outcome

Pursuing the endpoint-flat Landau branch produced one sound exact coordinate
and a useful, but narrower than first stated, route correction.

For every fixed endpoint order, the displayed normalization of the unique
(up to nonzero scalar) minimal consecutive-rate filter is an explicit
beta/Riesz weight.  The exponential growth exponent of either one
of its two Jordan parts is exactly

\[
 \Theta=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

Thus a subcritical estimate for either fixed sign part is equivalent to a
uniform zero-free strip.  Within the fixed raw response, its unit-block
Jordan mass is the least nonnegative additive correction that makes the
response one-signed.  This is not a global minimality statement across
filters.  A fixed causal box average or fixed primitive retains the same
rightmost-zero abscissa and gives another one-sided strip criterion without
reconstructing the raw Jordan mass.  For the raw endpoint-flat response,
elementary regularity still converts any subcritical mass exponent back to a
subcritical pointwise exponent, with a reduced margin.

The branch therefore yields a better coordinate on the strip obstruction,
not an easier proof of it.  Increasing endpoint order only attenuates high
zeros polynomially and delays their numerical visibility.  It never removes
one.

The exact scalar strip coordinate is:

\[
 \text{for some fixed }r\ge 1,\ \varepsilon\in\{-1,+1\},\ a<1,\qquad
 \int_N^{N+1}[\varepsilon B_r(e^t)]_+\,dt
 \ll_{a'}e^{a'N}\quad(a'>a).
\]

The sign \(\varepsilon\) must be selected once before \(N\to\infty\).
Proving this statement proves the strip \(\Re s>a\).  Nothing in this report
proves the displayed estimate.

## 1. Exact endpoint-flat family

For an integer \(r\ge0\), define

\[
 w_r(y)=\frac{((r+2)y-1)(1-y)^r}{(r+1)!},
 \qquad 0\le y\le1.
 \tag{1.1}
\]

Its polynomial coefficients are

\[
 w_r(y)=\sum_{j=0}^{r+1}c_{r,j}y^j,\qquad
 c_{r,j}=\frac{(-1)^{j+1}(j+1)}
 {j!\,(r+1-j)!}.
 \tag{1.2}
\]

With the normalization in (1.1), this is the unique (up to nonzero scalar)
minimal consecutive-rate filter with rates
\(0,1,\ldots,r+1\), notch order one, and endpoint-flatness order \(r\).
It has:

- one interior front at \(y=1/(r+2)\);
- a zero of exact order \(r\) at \(y=1\);
- negative sign before the front and positive sign after it; and
- Mellin transform

\[
 {\cal M}w_r(s)
 =\int_0^1w_r(y)y^{s-1}\,dy
 =\frac{s-1}{s(s+1)\cdots(s+r+1)}.
 \tag{1.3}
\]

For \(r=0\), this is the original ramp \(w_0(y)=2y-1\).  The first genuinely
endpoint-flat member is

\[
 w_1(y)=-\frac12+2y-\frac32y^2.
 \tag{1.4}
\]

### Proof

Expanding the two factors in (1.1) gives (1.2).  The beta integrals give

\[
 \frac1{(r+1)!}
 \left((r+2)B(s+1,r+1)-B(s,r+1)\right),
\]

which simplifies to (1.3).  The numerator supplies the unique interior zero;
the factor \((1-y)^r\) supplies the endpoint order.  The rational function
in (1.3) is, up to nonzero scalar, the unique minimal bidegree-one transfer
with these consecutive stable poles and the notch at \(s=1\); (1.3) fixes
the scalar normalization.

## 2. Exact actual-prime response

Define the centered von Mangoldt response

\[
 B_r(x)=
 \sum_{n\le x}\Lambda(n)w_r(n/x)
 -\frac{(1-x^{-1})^{r+1}}{(r+1)!},
 \qquad x\ge1,
 \tag{2.1}
\]

and put \(b_r(t)=B_r(e^t)\).

For \(\Re s>1\), absolute Fubini gives

\[
 \begin{aligned}
 \int_1^\infty B_r(x)x^{-s-1}\,dx
 &=
 \frac{s-1}{s(s+1)\cdots(s+r+1)}
 \left(
 -\frac{\zeta'}{\zeta}(s)-\frac1{s-1}
 \right).
 \end{aligned}
 \tag{2.2}
\]

The pole at \(s=1\) is removed.  At a nontrivial zero \(\rho\), however,

\[
 \frac{\rho-1}{\rho(\rho+1)\cdots(\rho+r+1)}\ne0.
 \tag{2.3}
\]

Consequently every nontrivial zeta zero remains a singularity of (2.2).
The coefficient at height \(\gamma\) is only attenuated at the polynomial
rate \(O_r(|\gamma|^{-r-1})\).

The pole at \(s=0\) contributes the positive constant

\[
 \frac{\log(2\pi)-1}{(r+1)!}.
 \tag{2.4}
\]

This small deterministic offset is important when interpreting finite
experiments at high endpoint order.

### Proof of the transform

For one prime-power atom, the substitution \(y=n/x\) gives

\[
 \int_n^\infty w_r(n/x)x^{-s-1}\,dx
 =n^{-s}{\cal M}w_r(s).
\]

The continuum subtraction has transform

\[
 \int_1^\infty
 \frac{(1-x^{-1})^{r+1}}{(r+1)!}x^{-s-1}\,dx
 =\frac1{s(s+1)\cdots(s+r+1)}.
\]

Combining these with
\(\sum\Lambda(n)n^{-s}=-\zeta'(s)/\zeta(s)\) proves (2.2).
Since \(\zeta'(0)/\zeta(0)=\log(2\pi)\), its residue at zero is (2.4).

## 3. Riesz-variation identity

Define the normalized Riesz error

\[
 C_r(x)=
 \frac1x\sum_{n\le x}\Lambda(n)(1-n/x)^{r+1}
 -\frac{(1-x^{-1})^{r+2}}{r+2}.
 \tag{3.1}
\]

Then, everywhere in the ordinary derivative sense away from entry points
and globally in the locally absolutely continuous sense,

\[
 B_r(x)=\frac{x^2}{(r+1)!}\,C_r'(x).
 \tag{3.2}
\]

The cutoff term vanishes when a new integer enters, so \(C_r\) has no jump.
Differentiating (3.1), writing \(y=n/x\), and using

\[
 (r+1)y(1-y)^r-(1-y)^{r+1}
 =((r+2)y-1)(1-y)^r
\]

proves (3.2).

The negative Jordan-mass target can therefore be written as a one-sided
weighted variation theorem:

\[
 \int_1^\infty (B_r(x))_-x^{-s-1}\,dx
 =
 \frac1{(r+1)!}
 \int_1^\infty(C_r'(x))_-x^{1-s}\,dx.
 \tag{3.3}
\]

Here derivatives and sign parts are understood almost everywhere, and the
identity holds for real \(s\) as an equality of extended nonnegative
integrals, or for complex \(s\) in any common absolute-convergence
half-plane.

So this route is equivalently asking for a subcritical bound on one
direction of the total variation of an actual-prime Riesz error.

## 4. Jordan-part Landau theorem in the raw-response ordering

Let \(f\) be real, locally integrable, and of finite exponential order.  Put
\(f_+=\max(f,0)\), \(f_-=\max(-f,0)\), and define

\[
 \alpha_\pm(f)=
 \limsup_{N\to\infty}\frac1N
 \log\int_N^{N+1}f_\pm(t)\,dt,
 \tag{4.1}
\]

with \(\log0=-\infty\).

For a nonnegative locally integrable function, (4.1) is exactly the abscissa
of convergence of its Laplace transform.  This unit-block definition is
essential: the cumulative mass \(\int_0^T f_\pm\) incorrectly truncates every
negative abscissa at zero.

### Theorem 4.1: one Jordan part suffices

Suppose the Laplace transform of \(f\), initially convergent in a right
half-plane, continues meromorphically to \(\Re s>a\) and is analytic at
every real \(s>a\).  If either

\[
 \alpha_-(f)\le a
 \quad\text{or}\quad
 \alpha_+(f)\le a,
 \tag{4.2}
\]

then the continued transform of \(f\) is holomorphic in \(\Re s>a\).

### Proof

Assume the first alternative.  The transform of \(f_-\) is holomorphic for
\(\Re s>a\).  On the initial convergence half-plane,

\[
 {\cal L}f_+={\cal L}f+{\cal L}f_-.
\]

The right side analytically continues across every real point
larger than \(a\).  If the convergence abscissa of the nonnegative function
\(f_+\) were some real number \(>a\), Landau's theorem would force a
singularity at that real abscissa, a contradiction.  Hence both Jordan-part
transforms converge in \(\Re s>a\), and their difference is holomorphic
there.  The other orientation is identical after replacing \(f\) by \(-f\).

This is the weakest possible nonnegative additive correction to this same
raw response.  If \(g\ge0\) and
\(f+g\ge0\), then \(g\ge f_-\) almost everywhere.  Thus the smallest
possible Laplace abscissa among all such corrections is attained by
\(g=f_-\) itself.  It does not follow that this premise is weakest after
changing the response by a faithful filter.

The block formulation of \(\alpha_-(f)\le a\) is

\[
 \int_N^{N+1}f_-(t)\,dt
 \ll_{a'}e^{a'N}
 \quad\text{for every }a'>a.
 \tag{4.3}
\]

This permits arbitrarily deep excursions if their widths are sufficiently
small.  It is strictly weaker as a statement about arbitrary functions than
a pointwise lower envelope.

## 5. Exact rightmost-zero spectrometer

Let \(\Theta\) be the supremum of the real parts of the nontrivial zeros of
\(\zeta\).

### Theorem 5.1

For every fixed integer \(r\ge0\),

\[
 \boxed{\alpha_+(b_r)=\alpha_-(b_r)=\Theta.}
 \tag{5.1}
\]

In particular, for either one globally fixed orientation,

\[
 \alpha_\pm(b_r)<1
 \quad\Longleftrightarrow\quad
 \Theta<1.
 \tag{5.2}
\]

The right side is exactly the existence of a uniform zero-free strip.

### Proof

The standard explicit-formula consequence

\[
 \psi(x)-x=O_\varepsilon(x^{\Theta+\varepsilon})
 \tag{5.3}
\]

and partial summation in the finite polynomial expansion (1.2) give

\[
 B_r(x)=O_{r,\varepsilon}(x^{\Theta+\varepsilon}).
 \tag{5.4}
\]

The continuum term in (2.1) is exactly the contribution of the unit density,
so no uncancelled \(x\)-term remains.  Equation (5.4) implies both upper
bounds in (5.1).

If, for example, \(\alpha_-(b_r)<\Theta\), choose
\[
 \max\{\alpha_-(b_r),0\}<a<\Theta;
\]
this is possible because \(\Theta\ge1/2\).  Formula (2.2) is analytic at every real
\(s>a\): zeta has no real zero in \(0<s<1\), the pole at one is centered,
and the displayed rational denominator has no positive-real pole.  Theorem
4.1 would make (2.2) holomorphic throughout \(\Re s>a\).  But by the
definition of \(\Theta\), there is a nontrivial zero \(\rho\) with
\(\Re\rho>a\), and (2.3) says it is not cancelled.  This is a contradiction.
The same argument applied to \(-b_r\) proves the lower bound for
\(\alpha_+(b_r)\).

The theorem is an endpoint-flat specialization of the classical Landau
positive-transform argument.  It is a useful project coordinate, but no
claim of literature-level novelty is made; locally, R95 and R103 already
contain closely related faithful-filter and exact-spectrometer statements.

## 6. The exact raw-Jordan adaptive-mask target

For a fixed unit block \(I_T=[T,T+1]\),

\[
 \int_{I_T}(b_r(t))_-\,dt
 =
 \sup_{0\le h\le1}
 \left(-\int_{I_T}h(t)b_r(t)\,dt\right),
 \tag{6.1}
\]

where the supremum is over measurable masks.  The maximizing mask is the
indicator of the negative set.

Substituting (2.1) and interchanging a finite sum and integral gives

\[
 \begin{aligned}
 \int_{I_T}h(t)b_r(t)\,dt
 &=
 \sum_{n\le e^{T+1}}\Lambda(n)W_{T,h,r}(n)
 -V_{T,h,r},\\
 W_{T,h,r}(n)
 &=
 \int_{\max(T,\log n)}^{T+1}
 h(t)w_r(ne^{-t})\,dt,\\
 V_{T,h,r}
 &=
 \int_T^{T+1}
 h(t)\frac{(1-e^{-t})^{r+1}}{(r+1)!}\,dt.
 \end{aligned}
 \tag{6.2}
\]

Therefore an exact arithmetic lemma for the *raw Jordan mass* is a uniform
one-sided actual-\(\Lambda\) discrepancy estimate over the complete affine family

\[
 \{(W_{T,h,r},V_{T,h,r}):0\le h\le1\}.
 \tag{6.3}
\]

This is more demanding than a fixed-test mean value because it reconstructs
the raw response's complete Jordan mass.  A mask can select
every adverse half-cycle inside the block, including cycles at scale
\(1/|\gamma|\) for arbitrarily high zeta zeros.  Averaging over \(t\) without
retaining this adaptive quantifier does not control that Jordan mass.
However, controlling the raw Jordan mass is not necessary for a strip proof:
the fixed causal box output has multiplier
\((1-e^{-Ls})/s\), which is zero-free in \(\Re s>0\), and its one-sided
subcritical bound is already a faithful strip criterion.

The theorem passport is consequently:

| field | retained object |
|---|---|
| nodes | every ordinary prime power |
| weights | exact \(\Lambda(p^k)=\log p\) |
| mask | all measurable \(0\le h\le1\) on one unit log block |
| continuum | exact affine term \(V_{T,h,r}\), not discarded |
| sign | one orientation chosen once, before height |
| resolution | all within-block sign changes |
| exponent | one fixed \(a<1\) |
| socket | raw-Jordan reconstruction plus Theorem 4.1 and (2.3) |

## 7. Why the raw Jordan target is still qualitatively strip-strength

For \(r\ge1\), the endpoint value \(w_r(1)=0\), so new prime powers enter
continuously.  Chebyshev's elementary bound and differentiation between
entry points give, on each unit block,

\[
 \|b_r\|_{L^\infty[T-1,T+2]}\ll_r e^T,\qquad
 \operatorname{Lip}(b_r;[T-1,T+2])
 \ll_r e^T.
 \tag{7.1}
\]

Suppose, for one fixed orientation and every \(a'>a<1\),

\[
 \int_N^{N+1}[\varepsilon b_r(t)]_+\,dt
 \ll_{a'}e^{a'N}.
 \tag{7.2}
\]

An adverse excursion of depth \(H\) persists, by (7.1), over length
\(\gg\min\{H/e^T,1\}\).  If the minimum is one, (7.2) directly gives the
stronger bound \(H\ll e^{a'T}\).  Otherwise, applying (7.2) to one of the at
most three neighboring unit blocks yields

\[
 H^2\ll_{r,a'}e^{(1+a')T}.
\]

Hence

\[
 [\varepsilon b_r(T)]_+
 \ll_{r,a'} e^{((1+a')/2)T}.
 \tag{7.3}
\]

The exponent in (7.3) remains strictly below one.  Thus the Jordan-mass
condition is minimal in the raw-response additive-correction ordering, but
on this regular response it cannot be
proved by a mechanism that only wins through arbitrarily narrow spikes:
any subcritical mass theorem already contains a subcritical pointwise
theorem with a reduced margin.

## 8. Spectral persistence under further smoothing

Every additional stable convolution whose multiplier is nonzero at the
mode—including each exponential stage in the beta hierarchy—multiplies an
oscillatory mode

\[
 e^{\lambda t}\cos(\gamma t)
\]

by a nonzero complex scalar such as

\[
 \frac{1}{\lambda+a+i\gamma}.
\]

It changes amplitude and phase, not \(\lambda\).  Therefore both sign-part
block exponents remain \(\lambda\).  In the beta family this is already
encoded by (2.3) and (5.1).

Positive compact kernels can have complex Laplace zeros, so an arbitrary
kernel family still needs a no-common-zero audit.  Increasing \(r\) in the
present nonvanishing hierarchy can make a finite interval look one-signed for a very long
time.  It cannot create a smaller asymptotic Jordan exponent.  This rules out
spectral contraction as a reason to search over larger fixed endpoint
orders; a different fixed filter could still be useful if it exposes a
genuine arithmetic simplification.

## 9. Two hostile countermodels

### 9.1 Smooth positive-density model

Let \(z=-d+i\gamma\), with \(0<d<1\), and let

\[
 E(t)=\Re(c e^{zt})=c e^{-dt}\cos(\gamma t),\qquad
 A(t)=-c+E(t).
\]

If \(c\sqrt{d^2+\gamma^2}<1\), then

\[
 dM(t)=dt+dA(t)
\]

is a positive smooth measure, asymptotic to unit density, with bounded
discrepancy converging exponentially to a constant and all polynomial
moments of its decaying density perturbation.  To put it on the same
prime scale as (2.1), tilt and push it forward under \(u\mapsto e^u\):

\[
 d\Psi(e^u)=e^u\,dM(u).
\]

The centered response of this positive source then contains

\[
 \Re\!\left(
 c z\,{\cal M}w_r(1+z)e^{(1+z)t}
 \right)+O(1).
 \tag{9.1a}
\]

The multiplier is nonzero for \(\gamma\ne0\), so both Jordan exponents are
\(1-d\).  Choosing \(1-d\) larger than the claimed bound makes both masses
supercritical.

Thus positivity, smoothness, PNT-level convergence, all moments, and endpoint
flatness cannot prove the desired estimate on a generic measure class.

### 9.2 Positive Euler-product model on the actual prime-power nodes

The sharper falsifier retains the exact node geometry.  Fix \(d>0\), choose
\(\gamma\ne0\) outside the countable set of ordinates of zeta zeros, and
choose \(P>2^{1/d}\).  Put

\[
 L_{P,d,\gamma}(s)=
 \prod_{p\le P}(1-p^{-s})^{-1}
 \prod_{p>P}
 \frac{(1-p^{-(s+d+i\gamma)})
       (1-p^{-(s+d-i\gamma)})}
      {1-p^{-s}}.
 \tag{9.1}
\]

For \(p>P\), write \(r_p=p^{-d}<1/2\) and
\(\theta_p=\gamma\log p\).  The local Dirichlet coefficients are

\[
 1,\quad
 1-2r_p\cos\theta_p,\quad
 1-2r_p\cos\theta_p+r_p^2,\ldots,
\]

and are positive.  Its generalized von Mangoldt coefficients are

\[
 \Lambda_L(p^k)
 =\log p\,[1-2p^{-kd}\cos(k\gamma\log p)]>0.
 \tag{9.2}
\]

Up to finitely many explicit Euler factors, (9.1) is

\[
 \frac{\zeta(s)}
 {\zeta(s+d+i\gamma)\zeta(s+d-i\gamma)}.
\]

It has a pole at \(s=1\) and exact zeros at
\(1-d\pm i\gamma\).  It also:

- uses precisely the ordinary prime-power nodes;
- has positive Dirichlet coefficients and positive coefficients of
  \(-L'/L\);
- agrees exactly with zeta on any prescribed finite zeta Euler head; and
- has a PNT-type main term.

This eliminates every proof based only on positivity, the prime-power node
set, PNT, positive Euler products, asymptotically zeta-like tail weights, or
an arbitrarily long initial segment of zeta's Euler data.

The model fails the exact unit Euler factors at all large primes.  Equivalently,
it fails zeta's exact divisor identity

\[
 \Lambda*1=\log.
 \tag{9.3}
\]

But (9.3) alone is not a linear coercive estimate: Dirichlet aggregation
multiplies \(-\zeta'/\zeta\) by \(\zeta\) and cancels precisely the pole
created by a zero of \(\zeta\).  Reversing that aggregation divides by
\(\zeta\), which imports the target stability.  An escape from this
countermodel must use some structure it does not retain: possibilities
include exact all-prime structure used nonlinearly, the functional equation,
zero-side correlations, or a separate prime inequality controlling the
adaptive mask cone.

## 10. Finite actual-prime diagnostic

A double-precision scan at every integer \(100\le x\le2{,}000{,}000\)
gave:

| \(r\) | minimum \(B_r(x)\) | argmin | maximum \(B_r(x)\) | argmax |
|---:|---:|---:|---:|---:|
| 0 | -687.808614 | 1,772,200 | 717.597576 | 1,513,751 |
| 1 | -22.368545 | 1,855,951 | 16.648539 | 948,641 |
| 2 | -1.035372 | 2,000,000 | 1.016601 | 1,665,318 |
| 3 | -0.015883 | 918,285 | 0.103041 | 1,811,522 |
| 4 | 0.003547 | 988,617 | 0.011622 | 1,944,133 |
| 5 | 0.000930 | 1,694,840 | 0.001398 | 2,000,000 |

The apparent positivity for \(r=4,5\) is a falsifier of naive numerical
intuition, not evidence for eventual positivity.  The positive residue
(2.4) is then comparable with the displayed values, while the zero
coefficients have been divided by roughly \(|\gamma|^{r+1}\).  Theorem 5.1
proves that the asymptotic sign-part exponent has not changed.

Machine-readable record:
[ZETA23-ENDPOINT-FLAT-RIESZ-DIAGNOSTIC-2M-2026-09-01.json](ZETA23-ENDPOINT-FLAT-RIESZ-DIAGNOSTIC-2M-2026-09-01.json).

## 11. Literature cross-check

The literature supports the obstruction diagnosis.  This section records
the sources used in the original pass; the 2026-09-02 correction linked at
the top imports the more directly overlapping Landau--Pólya oscillation,
positive/negative Mellin-part, systems-of-kernels, exponential-spline, and
current weighted-PNT literature.

- Hardy and Littlewood's classical Riesz means attach to a zero \(\rho\) a
  gamma-ratio coefficient.  It is nonzero and decays only polynomially with
  height.  This is the same spectral behavior as (2.2).
  [Hardy--Littlewood, 1916](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1916.Hardy.pdf)
- Debruyne's quantified one-sided Ingham--Karamata theorem derives a
  remainder from an already available inverse-width function \(M\) together
  with vertical-growth control \(K\).  Fixed exponential decay requires
  bounded \(M\), so one necessary input is already a fixed analytic strip;
  that strip alone does not automatically verify every growth and
  monotonicity hypothesis.
  [Debruyne, Theorems 1.3--1.4](https://arxiv.org/html/2411.03809v1#S1.SSx4)
- Johnston's zero-free-region-to-PNT theorem, together with the cited Pintz
  converse, explains why the known narrowing region produces
  subexponential rather than fixed-exponential decay for the raw PNT
  errors.  This is scale evidence, not an optimality theorem for the
  adaptive Jordan mass.
  [Johnston, Theorem 2.1](https://arxiv.org/html/2411.13791v2#S2.Thmtheorem1)
- Ramaré's corrected weighted explicit formula supplies rigorous smoothing
  adapters, but its zero terms again retain nonzero polynomially decaying
  coefficients.
  [Ramaré, corrected Lemma 2.1](https://ramare-olivier.github.io/Maths/Corrigendum-PsiTildeSimple-Acta-02.pdf)

In the scoped literature search, no imported Tauberian, Riesz-mean,
finite-difference, or complete-monotonicity theorem was found that supplies
the subcritical Jordan-mass estimate from known prime information.  Endpoint
flatness improves vertical convergence; it does not enlarge the domain of
analyticity.

## 12. Claim and trust ledger

| claim | status | trust |
|---|---|---|
| beta/consecutive-rate formula (1.1)--(1.3) | project proved | exact rational and symbolic replay |
| actual-prime Mellin formula (2.2) | project proved | analytic manuscript plus numerical unit tests |
| Riesz derivative identity (3.2) | project proved | algebraic derivation plus finite-difference replay |
| one-Jordan-part Landau theorem | classical Landau corollary in stated scope | analytic manuscript, classical Landau imported |
| exact exponent identity (5.1) | classical corollary/project specialization, conditional only on standard explicit-formula bound (5.3) | analytic manuscript plus classical input; locally preceded by R95/R103 |
| adaptive-mask identity (6.2) | project proved | finite Fubini identity |
| claim that adaptive masks are the minimal strip socket | refuted | fixed causal-box and primitive criteria |
| regularity collapse (7.3) | project proved for integer \(r\ge1\) | elementary Chebyshev/Lipschitz argument |
| smooth and Euler-product countermodels | project proved | direct algebra |
| finite \(2\)M sign ranges | diagnostic only | double precision |
| subcritical actual-prime Jordan mass | open | no evidence promoted |
| uniform zero-free strip | open | unchanged |
| RH | open | unchanged |

Replay:

    python3 -m pytest -q \
      src/test_endpoint_flat_riesz_landau.py \
      src/test_pole_killing_boundary_calculus.py \
      src/test_shifted_psi_ramp_bridge.py

passes all 61 combined tests, including 9 new endpoint-flat/Riesz tests.

## 13. Route decision

The endpoint-flat branch should remain in the theorem library but should not
remain the active discovery priority in its present scalar form.

What was gained is exact, with the corrected scope:

1. the cleanest fixed-order response is now an explicit beta/Riesz
   derivative;
2. the pointwise premise has been reduced to the least raw-response additive
   Jordan correction, not to a globally minimal strip premise;
3. that raw premise has been proved to have exponent exactly \(\Theta\);
4. its arithmetic quantifier is exposed as an adaptive-mask cone, while
   fixed causal boxes and primitives supply separate faithful sockets; and
5. countermodels expose exact all-prime multiplicative rigidity as one first
   discriminator; the functional equation, zero correlations, and other
   zeta-specific global identities remain distinct possibilities.

What was not gained is an exponent saving.  Further nonvanishing stable
smoothing or higher fixed endpoint order cannot provide one spectrally.
Fixed-test averaging does not control the *raw* adaptive-mask socket, but a
fixed average with a zero-free multiplier is itself a valid strip detector.
Finite Euler matching or generic positivity is still insufficient.  Signed
kernel families with possible complex zeros require a separate multiplier
zero audit.

Within this beta/Riesz arithmetic-response architecture, a new nonlinear
all-prime inequality controlling (6.3) remains one possible continuation,
not the uniquely preferred one.  It must now compete head-to-head with the
R95 ramp, a causal-box response, and a fixed primitive on arithmetic proof
complexity.  A zero-side theorem, a direct complex-analytic argument, or
another zeta-specific correlation mechanism could instead enter through a
different socket.  The portfolio recommendation—not a theorem—is to retain
these detector statements as classifiers while keeping effort on the
independent QP/Turan and Weil first-open edges.
