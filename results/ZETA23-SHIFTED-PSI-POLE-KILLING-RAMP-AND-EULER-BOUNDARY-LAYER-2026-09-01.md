# ZETA23 shifted-Psi / pole-killing ramp execution

Date: 2026-09-01  
Target: compare Suzuki's shifted screw function with the R95/R96 signed ramp
and look for an independently provable one-sided margin  
Preflight:
[`zeta23_shifted_psi_ramp_comparison_preflight_v1.json`](context/zeta23_shifted_psi_ramp_comparison_preflight_v1.json)

## Verdict

The comparison is complete, but it does **not** prove a uniform zero-free
strip.

What is proved in this execution is:

1. an exact common Laplace-transform representation of Suzuki's
   `Psi_omega`, a pole-centered triangular von-Mangoldt ramp, and, for every
   prescribed power `r`, the unique normalized pole killer inside the
   two-power ansatz `a y^r+b`;
2. an exact positive but exponentially unstable inverse bridge between the
   triangular and bounded ramps;
3. a method obstruction: a nonzero positivity-preserving causal convolution
   cannot kill the pole, because its Laplace transform cannot vanish at a
   positive real frequency;
4. an unconditional Euler-constant boundary-layer expansion for the entire
   fixed-ratio ramp family;
5. a precise explanation of why small-`delta` finite computations can display
   an apparently clean sign transition without supplying evidence for an
   eventual sign or a zero-free strip.

The sought independent margin is absent from the transform comparison.  A
one-sided bound for the new ramp is a valid sufficient criterion for a strip
and would exclude every forbidden zero mode, but no converse or easier proof
of that bound is obtained here.

## Claim ledger

| Claim | Status | Trust |
|---|---|---|
| Suzuki eventual-positivity criterion | imported theorem | primary literature |
| exact transforms and operator bridges below | project-proved | analytic manuscript, rational identities replayed |
| uniqueness within `a y^r+b` for each prescribed `r` | project-proved | Lean kernel check of scalar algebra |
| one-sided ramp bound implies a zero-free half-plane | project-proved from Landau's theorem | analytic manuscript |
| fixed-ratio Euler boundary expansion | project-proved | analytic manuscript; finite diagnostic agrees |
| exact literature novelty of the boundary expansion | not established | targeted search found no exact match |
| uniform strip or RH | open | no promotion |

The Lean files certify only the stated scalar rational identities.  They do
not formalize the zeta-function continuation, Suzuki's theorem, the prime
number theorem, or Landau's theorem.

## 1. Normalization

Fix

\[
 \frac12<\alpha<1,\qquad
 \delta=1-\alpha\in(0,\tfrac12),\qquad
 \omega=\alpha-\frac12,
\]

and put

\[
 A_\zeta(s)=-\frac{\zeta'}{\zeta}(s),\qquad
 F(s)=A_\zeta(s)-\frac1{s-1}.
\]

The pole at `s=1` is removable in `F`; with the standard Stieltjes convention,

\[
 F(1)=-\gamma,
 \qquad
 F'(1)=\gamma^2+2\gamma_1.
\]

All arithmetic sums below contain the full von Mangoldt function, including
proper prime powers.

## 2. Suzuki's shifted function in centered arithmetic coordinates

Suzuki proves

\[
 \mathcal L\Psi_\omega(q)
 =\frac1{q^2}\frac{\xi'}{\xi}(\alpha+q)
\]

and, more importantly,

\[
 \xi(s)\ne0\quad(\Re s>\alpha)
 \quad\Longleftrightarrow\quad
 \Psi_\omega(t)\ge0\quad\hbox{for every sufficiently large }t.
\tag{2.1}
\]

Define the triangular prime ramp and its pole-centered version by

\[
 W_\alpha(t)=
 \sum_{n\le e^t}\Lambda(n)n^{-\alpha}(t-\log n),
\]

\[
 J_\alpha(t)=W_\alpha(t)
 -\frac{e^{\delta t}-1-\delta t}{\delta^2}.
\]

Termwise Laplace transformation first in `Re(q)>delta`, followed by
continuation, gives

\[
 \widehat J_\alpha(q)=\frac{F(\alpha+q)}{q^2}.
\tag{2.2}
\]

Set

\[
 C_\infty(s)=\frac1s-\frac12\log\pi
 +\frac12\psi\!\left(\frac s2\right).
\]

An exact collection of Suzuki's second pole and gamma terms is

\[
 \begin{aligned}
 H_\alpha(t)={}&C_\infty(\alpha)t+C_\infty'(\alpha)\\
 &+e^{-\alpha t}\left[
 \frac1{\alpha^2}
 -\frac14\Phi\!\left(e^{-2t},2,\frac\alpha2\right)
 \right].
 \end{aligned}
\tag{2.3}
\]

Direct transformation gives

\[
 \widehat H_\alpha(q)=\frac{C_\infty(\alpha+q)}{q^2},
 \qquad
 \frac{\xi'}{\xi}(s)=C_\infty(s)-F(s).
\]

Then

\[
 \boxed{\Psi_\omega(t)=H_\alpha(t)-J_\alpha(t).}
\tag{2.4}
\]

This is not an approximation.  It also gives

\[
 H_\alpha(t)=C_\infty(\alpha)t+C_\infty'(\alpha)
 +O(e^{-(\alpha+2)t}).
\]

For orientation, `C_infinity(alpha)<0` throughout this interval.  Indeed,

\[
 C_\infty'(\alpha)
 =\sum_{m\ge1}\frac1{(\alpha+2m)^2}>0
\]

and `C_infinity(1)<0`.  Thus (2.1) asks the centered arithmetic ramp
`J_alpha` to stay below an explicit asymptotically negative affine function.
This restates the strip target exactly; it does not make it weaker.

## 3. Classification of the two-scale pole-killing ramps

Let `r>0`.  Consider a two-power cutoff `w(y)=a y^r+b`.  Require

1. endpoint normalization `w(1)=1`; and
2. annihilation of the pole frequency `q=delta`.

The two linear equations are

\[
 a+b=1,
 \qquad
 \frac a{\delta+r}+\frac b\delta=0.
\]

They have the unique solution

\[
 a=\frac{r+\delta}{r},\qquad b=-\frac\delta r.
\tag{3.1}
\]

This gives the general normalized ramp

\[
 \begin{aligned}
 \mathcal B_{\delta,r}(t)
 ={}&\sum_{n\le e^t}\Lambda(n)n^{-(1-\delta)}
 \left[
 \frac{r+\delta}{r}(ne^{-t})^r-\frac\delta r
 \right]\\
 &-\frac{1-e^{-rt}}r.
 \end{aligned}
\tag{3.2}
\]

The continuum subtraction in (3.2) is exact:

\[
 \int_0^t e^{\delta u}
 \left[
 \frac{r+\delta}{r}e^{-r(t-u)}-\frac\delta r
 \right]du
 =\frac{1-e^{-rt}}r.
\]

Its Laplace transform is

\[
 \boxed{
 \widehat{\mathcal B}_{\delta,r}(q)
 =\frac{q-\delta}{q(q+r)}F(q+1-\delta).
 }
\tag{3.3}
\]

The symmetric choice `r=delta` is

\[
 B_\delta(t)=
 \sum_{n\le e^t}\Lambda(n)n^{-(1-\delta)}
 \bigl[2(ne^{-t})^\delta-1\bigr]
 -\frac{1-e^{-\delta t}}\delta.
\tag{3.4}
\]

It is the common deformation sought in this execution.  Under the algebraic
endpoint extension `delta=1` (outside the Suzuki range `0<delta<1/2`),

\[
 B_1(\log x)
 =\sum_{n\le x}\Lambda(n)(2n/x-1)-1+x^{-1},
\]

is the R95/R96 ramp, while for each fixed `x`,

\[
 \lim_{\delta\downarrow0}B_\delta(\log x)
 =\sum_{n\le x}\frac{\Lambda(n)}n-\log x.
\tag{3.5}
\]

### One-sided strip criterion

For fixed `delta` and `r`, either of the eventual estimates

\[
 \mathcal B_{\delta,r}(t)\le C
 \quad\hbox{or}\quad
 \mathcal B_{\delta,r}(t)\ge-C
\tag{3.6}
\]

implies

\[
 \zeta(s)\ne0\qquad(\Re s>1-\delta).
\tag{3.7}
\]

The ramp is locally integrable and of finite exponential order.  After adding
a compactly supported correction, one side of (3.6) gives a nonnegative
function with a finite Laplace abscissa.  Formula (3.3), initially an identity
in its absolute-convergence half-plane, gives its meromorphic continuation.
If the abscissa were positive, Landau's theorem would force a singularity at
that positive real point.  The continuation has no such singularity: zeta has
no real zero in `(0,1)`, and the pole at `q=delta` was removed.  Hence the
abscissa is at most zero, and only at this point may one conclude that the
Laplace integral converges throughout `Re(q)>0`.  A zero `rho` with
`Re(rho)>1-delta` would now produce a pole at `q=rho-(1-delta)`; the factor
`q-delta` cannot cancel it, since that would mean `rho=1`.  This is a
contradiction.

This criterion is mathematically valid but is not an independently available
estimate.  A positive oscillatory density with a Mellin pole to the right of
`1-delta` makes the ramp oscillate without a one-sided bound, exactly as the
criterion requires.

### Prime powers

For the symmetric ramp and `alpha=1-delta>1/2`, deleting proper prime powers
changes the ramp by at most

\[
 \sum_p\frac{(\log p)p^{-2\alpha}}{1-p^{-\alpha}}<\infty.
\tag{3.8}
\]

Thus a one-sided criterion can be formulated with primes alone up to a fixed
`O_alpha(1)` correction.  This does **not** license dropping that correction
in finite comparisons; numerically it is large.

## 4. Exact bridge to Suzuki's triangular ramp

From (2.2) and (3.3),

\[
 \mathcal B_{\delta,r}=T_{\delta,r}J_\alpha,
 \qquad
 \widehat T_{\delta,r}(q)=\frac{q(q-\delta)}{q+r}.
\tag{4.1}
\]

The inverse multiplier has the elementary decomposition

\[
 \frac{q+r}{q(q-\delta)}
 =-\frac r{\delta q}
 +\frac{r+\delta}{\delta(q-\delta)}.
\]

Consequently

\[
 J_\alpha(t)=\int_0^t
 \left[
 \frac{r+\delta}{\delta}e^{\delta(t-u)}-\frac r\delta
 \right]\mathcal B_{\delta,r}(u)\,du.
\tag{4.2}
\]

The inverse kernel is positive on the forward cone, but grows like
`exp(delta t)`.  The corrected weighted-Mertens estimate (7.1) makes the
following integral absolutely convergent; evaluation of (3.3) at `q=delta`
then gives the exact moment

\[
 \int_0^\infty e^{-\delta u}\mathcal B_{\delta,r}(u)\,du=0.
\tag{4.3}
\]

Using (4.3) in (4.2) gives

\[
 \begin{aligned}
 J_\alpha(t)={}&-\frac r\delta\int_0^t
 \mathcal B_{\delta,r}(u)\,du\\
 &-\frac{r+\delta}{\delta}e^{\delta t}
 \int_t^\infty e^{-\delta u}\mathcal B_{\delta,r}(u)\,du.
 \end{aligned}
\tag{4.4}
\]

For the symmetric ramp this becomes the clean common representation

\[
 \boxed{
 \Psi_\omega(t)=H_\alpha(t)
 +\int_0^tB_\delta(u)\,du
 +2e^{\delta t}\int_t^\infty e^{-\delta u}B_\delta(u)\,du.
 }
\tag{4.5}
\]

Equation (4.5) is the exact answer to the transform-comparison part of the
preflight.

## 5. Why the bridge supplies no free positivity margin

The obstruction occurs before any delicate estimate.

Every convolution multiplier which removes the main pole by annihilating its
exponential mode must vanish at the positive frequency `q=delta`.  If a
nonzero causal convolution kernel `k` were nonnegative and its Laplace
transform converged there, then

\[
 \widehat k(\delta)=\int_0^\infty k(t)e^{-\delta t}\,dt>0.
\]

It therefore cannot be a pole killer.  Some sign change or distributional
differentiation is unavoidable in the forward map.  Conversely, the exact
inverse (4.2) is positive but contains the unstable mode `exp(delta t)`.

This proves the following scoped no-go statement (where convergence at
`q=delta` is the relevant stability requirement):

> No nonzero nonnegative ordinary causal convolution kernel whose Laplace
> integral converges at `q=delta` can itself realize an exact pole-killing
> multiplier.  For the fixed exact map (4.1), the inverse kernel is positive
> but exponentially unbounded.

It does not rule out an affine correction, a nonlinear or noncausal argument,
or an argument using a genuinely special property of the primes.  It does
rule out the direct ordinary-convolution margin proposed in this comparison.

Increasing `r` does not evade the obstruction.  It attenuates a forbidden
zero mode through the same denominator `q+r` that makes the negative part of
the physical kernel look smaller.  Allowing `r` to depend on `t` destroys the
single fixed Laplace transform needed by the Landau argument.

## 6. Exact weighted-Mertens representation

Define

\[
 A(t)=\sum_{n\le e^t}\frac{\Lambda(n)}n-t,
 \qquad E(t)=A(t)+\gamma.
\tag{6.1}
\]

Let `dA` denote the Stieltjes measure

\[
 dA(u)=\sum_n\frac{\Lambda(n)}n\,\delta_{\log n}(du)-du.
\]

For the general ramp, put

\[
 K_{\delta,r}(t,u)=
 \frac{r+\delta}{r}e^{-rt+(r+\delta)u}
 -\frac\delta r e^{\delta u}.
\]

Then exactly

\[
 \mathcal B_{\delta,r}(t)=\int_{(0,t]}K_{\delta,r}(t,u)\,dA(u).
\tag{6.2}
\]

Since `A(0)=0`, Stieltjes integration by parts and `A=-gamma+E` give

\[
 \boxed{
 \begin{aligned}
 \mathcal B_{\delta,r}(t)
 ={}&\frac\gamma r\bigl[\delta-(r+\delta)e^{-rt}\bigr]
 +e^{\delta t}E(t)\\
 &-\frac1r\int_0^t
 \left[
 (r+\delta)^2e^{-rt+(r+\delta)u}
 -\delta^2e^{\delta u}
 \right]E(u)\,du.
 \end{aligned}}
\tag{6.3}
\]

For `r=delta`, this is

\[
 \boxed{
 \begin{aligned}
 B_\delta(t)={}&\gamma(1-2e^{-\delta t})+e^{\delta t}E(t)\\
 &-\delta\int_0^t
 \left[4e^{-\delta t+2\delta u}-e^{\delta u}\right]E(u)\,du.
 \end{aligned}}
\tag{6.4}
\]

The factor `e^(delta t)` multiplying `E(t)` is essential.  Omitting it gives
an incorrect identity.

## 7. Euler boundary-layer theorem

Fix `a>0`, take `r=a delta`, and examine the double scale

\[
 t=\frac c\delta,
 \qquad c\in(0,\infty)\ \hbox{fixed}.
\]

Ramaré's corrected explicit estimate gives

\[
 |E(t)|\le\frac{1.833}{t^2}\qquad(t>0),
\tag{7.1}
\]

in the corresponding `x=e^t` notation.  In particular `E` is integrable and
`E(c/delta)=O(delta^2)` uniformly when `c` stays in a compact subset of
`(0,infinity)`.

Define

\[
 K_0=\int_0^\infty E(u)\,du.
\]

The Laplace identity

\[
 \int_0^\infty E(t)e^{-qt}\,dt
 =\frac{F(1+q)+\gamma}{q}
\]

shows that

\[
 K_0=F'(1)=\gamma^2+2\gamma_1
 =0.1875462328403652245972033846\ldots.
\tag{7.2}
\]

Substitution into (6.3), followed by dominated convergence, proves the
uniform compact-`c` expansion

\[
 \boxed{
 \begin{aligned}
 \mathcal B_{\delta,a\delta}(c/\delta)
 ={}&\frac\gamma a\bigl[1-(a+1)e^{-ac}\bigr]\\
 &-\frac\delta a
 \bigl[(a+1)^2e^{-ac}-1\bigr]K_0+o(\delta).
 \end{aligned}}
\tag{7.3}
\]

This is unconditional.

The standard zero-free-region PNT remainder gives stretched-exponential
decay of `E`, hence all moments

\[
 K_m=\int_0^\infty u^mE(u)\,du
 =\frac{(-1)^m}{m+1}F^{(m+1)}(1).
\tag{7.4}
\]

Expanding the exponentials in (6.3) then upgrades (7.3), for each fixed `N`,
to

\[
 \boxed{
 \begin{aligned}
 \mathcal B_{\delta,a\delta}(c/\delta)
 ={}&\frac\gamma a[1-(a+1)e^{-ac}]\\
 &-\sum_{m=0}^{N-1}
 \frac{\delta^{m+1}}{a\,m!}
 \bigl[(a+1)^{m+2}e^{-ac}-1\bigr]K_m
 +O_{a,c,N}(\delta^{N+1}).
 \end{aligned}}
\tag{7.5}
\]

The remainder is uniform for `a` and `c` in compact subsets of
`(0,infinity)`.

### The universal transition

The leading profile in (7.3) vanishes at

\[
 c_a=\frac{\log(a+1)}a.
\tag{7.6}
\]

This is exactly the logarithmic age at which the physical kernel changes
sign:

\[
 \frac{(a+1)e^{-a\delta v}-1}{a}=0
 \quad\Longleftrightarrow\quad
 \delta v=c_a.
\]

At `c=c_a`, the coefficient of `-delta K_0` and the derivative of the leading
profile simplify to `1` and `gamma`, respectively.  Therefore the local zero
of the two-term profile is

\[
 c=c_a+\frac{K_0}{\gamma}\delta+o(\delta),
 \qquad
 \frac{K_0}{\gamma}=0.3249153553\ldots.
\tag{7.7}
\]

For the symmetric ramp `a=1`,

\[
 B_\delta(c/\delta)
 =\gamma(1-2e^{-c})
 -\delta(4e^{-c}-1)K_0+o(\delta).
\tag{7.8}
\]

At the project value `delta=10^-6`, (7.7) places the local profile transition
at

\[
 \log x=693147.505475\ldots,
 \qquad
 \log_{10}x=301030.136773\ldots.
\]

This is roughly `1.37 * 10^301030`.  It is a local zero of the asymptotic
profile, not a theorem about the first sign change of the discontinuous
arithmetic ramp.

## 8. What the finite data mean

At `x=10^7`, the full-von-Mangoldt values compare with (7.8) as follows.

| `delta` | `delta log x` | actual `B_delta` | one term | two terms |
|---:|---:|---:|---:|---:|
| 0.001 | 0.016118 | -0.559454 | -0.558758 | -0.559308 |
| 0.01 | 0.161181 | -0.410073 | -0.405365 | -0.409874 |
| 0.05 | 0.805905 | 0.053507 | 0.061550 | 0.054173 |
| 0.1 | 1.611810 | 0.349597 | 0.346876 | 0.350663 |

The agreement is explained by the unconditional boundary theorem.  It is not
evidence for (3.6).

Dropping proper prime powers at the same cutoff gives, respectively,
`-1.297314`, `-1.000144`, `-0.000256`, and `0.785518`.  Although (3.8) makes
the correction asymptotically bounded for fixed `delta`, it is plainly not a
negligible finite perturbation.

The replayable diagnostic is
[`ZETA23-SHIFTED-PSI-RAMP-DIAGNOSTIC-2026-09-01.json`](ZETA23-SHIFTED-PSI-RAMP-DIAGNOSTIC-2026-09-01.json).

## 9. Fast falsifiers and retired inferences

The following possible shortcuts fail.

1. **Continuity from `delta=0`.**  Equation (3.5) is pointwise at fixed `x`.
   The relevant transition lives at `log x` of order `1/delta`, so the limit
   is singular.  Equations (7.3)--(7.8) quantify the failure.
2. **Finite positivity or negativity.**  A computation through any ordinary
   cutoff samples only the early side of the boundary layer when `delta` is
   tiny.
3. **Prime-only finite margins.**  Proper prime powers are bounded but large
   enough to reverse apparent finite margins.
4. **A larger decay parameter.**  It suppresses the forbidden mode along with
   the negative kernel tail; it creates no uncompensated gain.
5. **A variable decay parameter.**  It no longer defines the fixed transform
   needed for Landau's theorem.
6. **Positivity and density alone.**  Positive oscillatory pseudo-prime
   densities can carry a conjugate Mellin pole to the right of `1-delta` and
   reproduce the forbidden growing oscillation.
7. **Positive-kernel transfer from Suzuki.**  Pole annihilation forces a zero
   of the multiplier at a positive frequency, which a nonzero nonnegative
   convolution kernel cannot have.

## 10. Literature placement

- Masatoshi Suzuki, [Section 11 of *Aspects of the screw function
  corresponding to the Riemann zeta-function*](https://arxiv.org/html/2206.03682v4#S11),
  supplies the shifted transform and theorem (2.1).
- Olivier Ramaré, [*Explicit estimates for the summatory function of
  Lambda(n)/n from the one of Lambda(n)*](https://doi.org/10.4064/aa159-2-2),
  together with the [mandatory
  corrigendum](https://ramare-olivier.github.io/Maths/Corrigendum-PsiTildeSimple-Acta-02.pdf),
  supplies (7.1).  The corrigendum fixes signs and finite computations while
  retaining the `1.833/log^2(x)` bound.
- Murty and Pathak, [*Relations between certain power series and functions
  involving zeros of zeta functions*](https://mast.queensu.ca/~murty/Zeta_Relations_Revised.pdf),
  give explicit formulas for arbitrary finite combinations of
  `x^a sum_{n<=x} Lambda(n)n^{-a}`.  Indeed

  \[
  x^{1-\delta}B_\delta(\log x)
  =2x^{1-2\delta}S_{1-2\delta}(x)
   -x^{1-\delta}S_{1-\delta}(x)
   -\frac{x^{1-\delta}-x^{1-2\delta}}\delta,
  \]

  where `S_s(x)=sum Lambda(n)n^{-s}`.  Thus the two-weight arithmetic
  combination is already contained in a general explicit-formula framework.
  At a prime-power cutoff their theorem uses the usual half-weight endpoint
  convention, which must be converted to the right-continuous `n<=x`
  convention used here.
- Johnston and Yang, [Theorem 1.4](https://arxiv.org/html/2204.01980), give an
  explicit Vinogradov--Korobov PNT error more than sufficient for the
  all-moment expansion (7.5).

The exact pole-centered Laplace packaging, operator bridge, and Euler
boundary profile were not found verbatim in the targeted search.  They should
be described conservatively as apparently unrecorded project lemmas pending a
broader independent novelty review.  The boundary law is a short Abelian
consequence of known weighted-Mertens estimates, not a zero-free-strip
breakthrough.

## 11. Decision-tree update

Within the class of fixed exact linear causal convolution transfers, the
proposed branch

\[
 \text{Suzuki positivity}
 \longrightarrow
 \text{stable positive ramp transfer}
 \longrightarrow
 \text{easy one-sided bound}
\]

is closed at its first arrow.  In that class, the pole-killing zero and
unstable inverse are structural, not artifacts of the symmetric kernel.

The exact ramps remain useful as **spectrometers**: they put the strip target
in a compact signed cutoff family and make scale mistakes visible.  They do
not currently reduce the strip to an easier theorem.  Further work on this
branch is justified only if it introduces a property of the actual
von-Mangoldt sequence not shared by positive oscillatory densities.  Merely
optimizing `r`, extending finite scans, or reproving eventual one-sidedness in
new notation should be rejected as target renaming.

The honest global state after this execution is unchanged:

\[
 \boxed{\text{uniform zero-free strip open; RH open.}}
\]

## 12. Reproducibility

Code and certificates:

- `src/shifted_psi_ramp_bridge.py`
- `src/test_shifted_psi_ramp_bridge.py`
- `lean/rhbridge/RHBridge/ShiftedPsiRampBridge.lean`
- `lean/rhbridge/RHBridge/ShiftedPsiRampBridgeAudit.lean`

Verification commands:

```bash
PYTHONPATH=src python3 -m pytest -q src/test_shifted_psi_ramp_bridge.py
cd lean/rhbridge
lake env lean RHBridge/ShiftedPsiRampBridge.lean
lake env lean RHBridge/ShiftedPsiRampBridgeAudit.lean
```
