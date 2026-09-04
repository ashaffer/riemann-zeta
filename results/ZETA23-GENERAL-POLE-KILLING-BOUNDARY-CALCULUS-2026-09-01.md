# ZETA23 general pole-killing boundary calculus

Date: 2026-09-01  
Target: generalize the shifted-Psi pole-killing boundary layer as far as the
current argument permits  
Preflight:
[`zeta23_general_pole_killing_boundary_calculus_preflight_v1.json`](context/zeta23_general_pole_killing_boundary_calculus_preflight_v1.json)

Post-audit route revalidation:
[`ZETA23-POLE-KILLING-CORRECTION-REVALIDATION-AND-ROUTE-AUDIT-2026-09-01.md`](ZETA23-POLE-KILLING-CORRECTION-REVALIDATION-AND-ROUTE-AUDIT-2026-09-01.md)

## Verdict

The generalization succeeds as a reusable theorem suite, but it does **not**
prove a uniform zero-free strip or RH.

The broadest proved object is a dilation calculus for Stieltjes discrepancy
measures.  Its consequences include:

1. a universal boundary-localization theorem requiring only convergence of a
   centered cumulative discrepancy;
2. a distributional delta-jet expansion whose coefficients are all moments
   of that discrepancy;
3. a complete two-index classification for prescribed distinct real
   exponential rates: pole-notch order and endpoint-flatness order, together
   with integer and fractional associated-Laguerre confluent limits;
4. sharp alternation and inverse-instability costs for real continuous scalar
   causal pole killers under the stated moment and Laplace-germ hypotheses;
5. a canonical confluent normal form in terms of Laguerre polynomials;
6. a functional calculus showing that every algebraic boundary coefficient
   is determined by the regular Laurent germ at the pole;
7. a regular-variation calculus covering fractional and logarithmic boundary
   layers;
8. transfer to general Dirichlet series, logarithmic derivatives of
   `L`-functions, higher-order poles, Beurling-type counting measures,
   Banach-valued measures, and multivariate distributional tangents;
9. a local converse Volterra theorem, with a nonzero endpoint diagonal,
   showing that the boundary profile near the origin identifies the original
   limiting discrepancy after rescaling; and
10. a spectral tradeoff theorem: endpoint-normalized filters with a uniform
    `1/s` high-frequency symbol do not attenuate fixed singularities, while
    endpoint-flat filters attenuate them algebraically and pay an exactly
    quantified differentiating loss if one reconstructs the original
    observable; and
11. a compact-support Chebyshev calculus with continuous left/right endpoint
    orders and an arbitrary finite divisor of real pole notches, whose
    far-edge layer is a fractional Volterra transform of the discrepancy
    tail.

The last two points locate the real strip problem.  Every finite collection of
perturbative boundary coefficients sees only finitely many Taylor coefficients
of the Laurent germ at `s=1`.  The complete germ does encode singularities
through its coefficient growth and analytic continuation.  In the
uniform-symbol interior branch, the direct hard-cutoff transient of each fixed
left singularity is beyond all algebraic orders; compact support can
demodulate it at the far edge, but only as a Volterra transform of the unknown
tail.  A uniform strip therefore needs **global or vertically translated
all-order germ control, an exponential-remainder theorem uniform into the
fixed-`epsilon` eventual regime, or a fixed-delta eventual one-sided
`O(exp(eta*t))` envelope theorem**;
another fixed finite jet is insufficient.
All fixed-singularity multiplier statements here are pointwise in a fixed
offset `omega`; they do not supply the joint uniformity needed for sequences
approaching `Re(s)=1` at unbounded height.

## Claim ledger

| Claim | Status | Trust |
|---|---|---|
| exact Stieltjes boundary identity and leading limit | project-proved | analytic manuscript |
| delta-jet and regular-variation expansions | project-proved | analytic manuscript; endpoint counterexample included |
| fixed-rate exponential filter classification | project-proved | exact rational replay; low-order Lean certificates |
| fractional and compact-support extensions | project-proved under the stated branch, sector, and tail hypotheses | analytic manuscript; high-precision replay for explicit examples |
| alternation and inverse-instability theorem | project-proved | analytic proof using standard Chebyshev-system facts |
| Laguerre confluent normal form | project-proved | exact transform replay; classical special-function identities |
| finite-dimensional Laurent-germ functional calculus | project-proved for fixed filters under the stated moment, endpoint, and remainder hypotheses | analytic manuscript and numerical/symbolic replay |
| infinite-dimensional semigroup calculus or global germ-to-strip propagation | conditional/open | domains, uniform constants, and vertical continuation are not supplied by the finite calculus |
| Dirichlet-series transfer | project-proved under stated PNT/error hypotheses | analytic manuscript; imported PNT inputs separated |
| Landau singularity-exclusion adapter | project-proved from imported Landau theorem | hypotheses stated explicitly |
| exact literature novelty of the combined calculus | not established | targeted search found close ingredients, not the full synthesis |
| uniform zero-free strip or RH | open | no promotion |

The Lean development certifies selected scalar rational identities only.  It
does not formalize Stieltjes integration, the prime number theorem, Landau's
theorem, analytic continuation, or any zero-free region.

## 1. Universal scaled-measure theorem

Let `nu` be a signed or complex measure on `(0,infinity)` whose total
variation is finite on every `(0,T]`, and use the right-continuous cumulative

\[
 A(t)=\nu((0,t]),\qquad A(0)=0.
\]

Assume

\[
 A(t)=-C+E(t),\qquad E(t)\longrightarrow0.
\tag{1.1}
\]

For `c,epsilon>0` and `Phi_c in C^1([0,c])`, put

\[
 R_\epsilon(c)=
 \int_{(0,c/\epsilon]}\Phi_c(\epsilon u)\,dA(u).
\tag{1.2}
\]

Stieltjes integration by parts gives the exact identity

\[
 \boxed{
 R_\epsilon(c)=
 -C\Phi_c(0)+\Phi_c(c)E(c/\epsilon)
 -\epsilon\int_0^{c/\epsilon}\Phi_c'(\epsilon u)E(u)\,du.}
\tag{1.3}
\]

Consequently, if the endpoint values and first derivatives of the test family
are uniformly bounded, then

\[
 \boxed{R_\epsilon(c)\longrightarrow-C\Phi_c(0)}
\tag{1.4}
\]

uniformly for `c` in compact subsets of `(0,infinity)`.  No moment or rate for
`E` is required.  The proof of the integral limit is just a compact-tail
split, or dominated convergence after `z=epsilon*u`.

Uniformity cannot include `c=0`: the response there is zero, while the
iterated interior limit is generally `-C Phi_0(0)`.

### Causal-kernel specialization

For `sigma>0` and a differentiable causal kernel `k`, take

\[
 \Phi_c(z)=e^{\sigma z}k(c-z).
\]

Then

\[
 \begin{aligned}
 B_{\epsilon,k}(c/\epsilon)
 ={}&-Ck(c)+e^{\sigma c}k(0)E(c/\epsilon)\\
 &-\epsilon\int_0^{c/\epsilon}e^{\sigma\epsilon u}
 (\sigma-\partial_c)k(c-\epsilon u)E(u)\,du,
 \end{aligned}
\tag{1.5}
\]

and hence

\[
 \boxed{B_{\epsilon,k}(c/\epsilon)\longrightarrow-Ck(c).}
\tag{1.6}
\]

The Euler-constant ramp is the case `C=gamma`, `sigma=1`, and
`k(c)=2e^{-c}-1`.

## 2. Delta jets and the maximal integer-power expansion

Define discrepancy moments

\[
 K_m=\int_0^\infty u^mE(u)\,du.
\tag{2.1}
\]

Fix `N>=1`.  Suppose, uniformly for `c` in a compact positive interval,

- the tests form a bounded `C^(N+1)` family;
- `int_0^infinity (1+u^N)|E(u)|du<infinity`; and
- the hard endpoint satisfies
  `sup_c |E(c/epsilon)|=O(epsilon^(N+1))`.

Taylor expansion in (1.3) then gives

\[
 \boxed{
 R_\epsilon(c)=
 -C\Phi_c(0)-
 \sum_{m=0}^{N-1}\frac{\epsilon^{m+1}}{m!}
 \Phi_c^{(m+1)}(0)K_m+O(\epsilon^{N+1}).}
\tag{2.2}
\]

For causal kernels this is

\[
 \boxed{
 B_{\epsilon,k}(c/\epsilon)=
 -Ck(c)-
 \sum_{m=0}^{N-1}\frac{\epsilon^{m+1}}{m!}K_m
 (\sigma-\partial_c)^{m+1}k(c)
 +O(\epsilon^{N+1}).}
\tag{2.3}
\]

This is the maximal fixed-order Laurent-jet dictionary under ordinary moment
hypotheses.

### Distributional form

Let `nu_epsilon=(u -> epsilon*u)_# nu`.  Against smooth compactly supported
tests there is no moving hard endpoint, and (2.2) becomes

\[
 \boxed{
 \nu_\epsilon\sim-C\delta_0+
 \sum_{m\ge0}\frac{(-1)^m\epsilon^{m+1}K_m}{m!}
 \delta_0^{(m+1)}.}
\tag{2.4}
\]

Thus the boundary calculus is literally a multipole expansion at the origin.
The limiting prime discrepancy becomes a monopole; its integrated moments
become dipole, quadrupole, and higher delta jets.

### The hard-endpoint hypothesis is necessary

All absolute moments do not control a sampled endpoint.  Let `T_j=2^j` and
take `E` to be a decaying baseline plus disjoint triangular bumps centered at
`T_j`, with height `T_j^(-1/2)` and width `exp(-T_j)`.  Then

\[
 E(t)\to0,\qquad
 \int_0^\infty t^m|E(t)|dt<\infty
 \quad\hbox{for every }m,
\]

but for `epsilon_j=c/T_j`,

\[
 E(c/\epsilon_j)=T_j^{-1/2}\gg\epsilon_j.
\]

If `Phi_c(c)` is nonzero, the endpoint term in (1.3) destroys even the
first-order expansion.  Endpoint-zero smoothing, smooth compact support, or
averaging in `c` removes this obstruction.

## 3. Scaling tangents and regular variation

The constant boundary law is one member of a larger tangent calculus.  Let
`T=1/epsilon`, let `b(T)>0`, and suppose

\[
 \frac{A(Tz)}{b(T)}\longrightarrow G(z)
\tag{3.1}
\]

almost everywhere on compact `z`-intervals, with a uniform local majorant and
endpoint convergence at the chosen `c`.  Retain the inherited convention
`G(0)=0`, since `A(0)=0`.  Then

\[
 \boxed{
 \frac{R_{1/T}(c)}{b(T)}\longrightarrow
 \Phi_c(c)G(c)-\int_0^c\Phi_c'(z)G(z)\,dz.}
\tag{3.2}
\]

When the zero-extended `G` has bounded variation, the right side is
`int_[0,c] Phi_c dG`; the closed left endpoint retains a tangent atom created
by a jump from the zero extension.  In particular, if

\[
 A(t)\sim D t^\rho L(t),\qquad \rho>0,
\]

regular variation yields

\[
 \boxed{
 R_\epsilon(c)\sim
 D\epsilon^{-\rho}L(1/\epsilon)\rho
 \int_0^c\Phi_c(z)z^{\rho-1}\,dz.}
\tag{3.3}
\]

### Complete noninteger tail hierarchy

Suppose

\[
 E(t)\sim D t^{-\beta}L(t),
 \qquad n<\beta<n+1,
\tag{3.4}
\]

where `n>=0` is an integer and `L` is slowly varying.  Put

\[
 P_{n-1}(z)=
 \sum_{r=0}^{n-1}\frac{\Phi_c^{(r+1)}(0)}{r!}z^r,
\]

with an empty sum for `n=0`.  Under the usual uniform regular-variation
bounds,

\[
 \begin{aligned}
 R_\epsilon(c)={}&-C\Phi_c(0)
 -\sum_{r=0}^{n-1}\frac{\epsilon^{r+1}}{r!}
 \Phi_c^{(r+1)}(0)K_r\\
 &+D\epsilon^\beta L(1/\epsilon)\mathcal H_{\beta,c}[\Phi_c]
 +o(\epsilon^\beta L(1/\epsilon)),
 \end{aligned}
\tag{3.5}
\]

where

\[
 \begin{aligned}
 \mathcal H_{\beta,c}[\Phi]
 ={}&\Phi(c)c^{-\beta}
 -\int_0^c(\Phi'(z)-P_{n-1}(z))z^{-\beta}\,dz\\
 &+\sum_{r=0}^{n-1}
 \frac{\Phi^{(r+1)}(0)}{r!}
 \frac{c^{r+1-\beta}}{\beta-r-1}.
 \end{aligned}
\tag{3.6}
\]

At an integer threshold `beta=n+1`, if the truncated borderline moment

\[
 J(T)=\int^T\frac{L(u)}u\,du
\]

diverges and `L(T)=o(J(T))`, the next term is governed by

\[
 -\frac{D\epsilon^{n+1}\Phi^{(n+1)}(0)}{n!}
 \int^{1/\epsilon}\frac{L(u)}u\,du.
\tag{3.7}
\]

It becomes the familiar `epsilon^(n+1)L(1/epsilon)log(1/epsilon)` only when
the final integral has that asymptotic.  This caveat matters for arbitrary
slowly varying `L`.  If the borderline integral converges, the next absolute
moment exists and the ordinary moment expansion resumes instead.

## 4. Transform algebra and arbitrary-order pole killers

Let

\[
 \widehat k(s)=\int_0^\infty e^{-sv}k(v)\,dv.
\]

For the full causal response

\[
 B_{\epsilon,k}(t)=
 \int_{(0,t]}e^{\sigma\epsilon u}
 k(\epsilon(t-u))\,dA(u),
\]

Laplace transformation gives

\[
 \boxed{
 \widehat B_{\epsilon,k}(q)=
 \epsilon^{-1}\widehat k(q/\epsilon)
 \mathcal D(q-\sigma\epsilon),}
\tag{4.1}
\]

where `mathcal D(q)=int exp(-qu)dA(u)` in a common convergence half-plane.

An order-`m` notch at the shifted pole is exactly

\[
 \widehat k^{(j)}(\sigma)=0,
 \qquad 0\le j<m,
\tag{4.2}
\]

or equivalently

\[
 \boxed{
 \int_0^\infty v^j e^{-\sigma v}k(v)\,dv=0,
 \qquad0\le j<m.}
\tag{4.3}
\]

Conditions (4.2)--(4.3) mean order at least `m`; exact order additionally
requires `widehat k^(m)(sigma)!=0`.

### Alternation-instability theorem

Assume `k` is real, nonzero, continuous, and the absolute moments in (4.3)
exist.

- The `m` orthogonality conditions force at least `m` sign changes.  If there
  were fewer, a polynomial of degree below `m` could be chosen with the same
  sign pattern as `k`, contradicting its orthogonality.
- If
  `hat k(s)=a_m(s-sigma)^m+O((s-sigma)^(m+1))`, then the causal inverse of the
  scaled multiplier necessarily contains

  \[
   \boxed{
   \frac{\epsilon^{m+1}}{a_m(m-1)!}
   t^{m-1}e^{\sigma\epsilon t}.}
   \tag{4.4}
  \]

Thus every additional cancellation order costs another alternating lobe and
another polynomial degree multiplying the same exponential instability.

A nonzero nonnegative scalar kernel cannot kill a positive frequency at all,
because `hat k(sigma)>0`.  In the local algebra of analytic Laplace germs,
the pole killers form the maximal ideal at evaluation `sigma`; order is its
valuation, cascade adds valuations, and inversion changes a zero of order `m`
into a pole of order `m`.  This local-algebra statement should not be confused
with an unqualified spectral-synthesis claim for every global convolution
algebra.

## 5. Complete finite-mode classification

Take `N` distinct stable rates `a_j>=0` and

\[
 k(v)=\sum_{j=0}^{N-1}c_je^{-a_jv},
 \qquad k(0)=\sum_jc_j=1.
\]

Then endpoint normalization and a zero of order `m<=N-1` at `sigma` are
equivalent to

\[
 \boxed{
 \widehat k(s)=
 \frac{(s-\sigma)^mQ(s)}{\prod_{j=0}^{N-1}(s+a_j)},}
\tag{5.1}
\]

where `Q` is monic of degree `N-1-m`.  For an exact order-`m` zero require
`Q(sigma)!=0`; without that condition (5.1) means order at least `m`.  This
classifies all extra-mode freedom.

The minimal case `N=m+1` is unique:

\[
 \boxed{
 \widehat k(s)=\frac{(s-\sigma)^m}{\prod_{j=0}^m(s+a_j)},
 \qquad
 c_j=\frac{(\sigma+a_j)^m}
 {\prod_{\ell\ne j}(a_j-a_\ell)}.}
\tag{5.2}
\]

These are Lagrange/divided-difference weights.  Ordered rates give alternating
coefficient signs.  Exponentials with distinct real rates form a Chebyshev
system, so an `(m+1)`-term combination has at most `m` zeros.  Section 4 forces
at least `m` sign changes.  Therefore the minimal kernel has exactly `m`
simple positive crossings.

### Cascade normal form

The same transfer factors as

\[
 \widehat k_m(s)=\frac1{s+a_0}
 \prod_{j=1}^m\frac{s-\sigma}{s+a_j}.
\tag{5.3}
\]

Each first-order notch has impulse

\[
 \delta_0-(\sigma+a_j)e^{-a_jv},
\]

so cascading adds one zero order and one forced alternation per stage.  The
inverse stage is

\[
 \delta_0+(\sigma+a_j)\epsilon e^{\sigma\epsilon t},
\]

which is positive but unstable.

For the bridge from this filtered response back to the triangular response,

\[
 \frac{\prod_{j=0}^m(q+a_j\epsilon)}
 {q^2(q-\sigma\epsilon)^m}
\]

is a convolution of nonnegative causal factors, yet contains the unavoidable
tail

\[
 \boxed{
 \frac{\epsilon^{m-1}\prod_j(\sigma+a_j)}
 {\sigma^2(m-1)!}
 t^{m-1}e^{\sigma\epsilon t}.}
\tag{5.4}
\]

Positivity of this inverse uses scalar real `sigma>0` and `a_j>=0`; it need
not survive complex rates or an arbitrary extra factor `Q`.

## 6. The confluent Laguerre normal form

Coalescing all stable rates at `a>=0` gives

\[
 \boxed{
 k_{m,a}(v)=e^{-av}L_m((a+\sigma)v),
 \qquad
 \widehat k_{m,a}(s)=
 \frac{(s-\sigma)^m}{(s+a)^{m+1}}.}
\tag{6.1}
\]

It is the unique kernel of the form `e^(-av)P_m(v)`, with `P_m(0)=1`, having
an order-`m` notch.  Its `m` fronts are the positive Laguerre zeros divided by
`a+sigma`.  It is therefore canonical in three precise senses:

- minimal dimension;
- the minimum possible number of sign changes; and
- a single repeated stable pole, hence a Jordan/confluent normal form.

It is not proved optimal for a zero-free strip or under a bounded-cutoff norm.
For example, `a=0` minimizes one formal inverse coefficient but makes
`L_m(sigma*v)` unbounded as a cutoff.

If `lambda_(m,j)` is a Laguerre zero and
`c_j=lambda_(m,j)/(a+sigma)`, then the leading inverse-tail coefficient `A`
satisfies the exact localization law

\[
 \boxed{
 A c_j^{m+1}=
 \frac{\epsilon^{m-1}\lambda_{m,j}^{m+1}}
 {\sigma^2(m-1)!}.}
\tag{6.2}
\]

Moving a front toward the origin therefore forces its unstable coefficient to
grow like `c_j^(-(m+1))` within this family.

## 6A. The full two-index finite-state normal form

The endpoint normalization `k(0)=1` is not forced by pole cancellation.  It is
one corner of a larger bidegree theory.  Fix integers `m,r>=0` and require

\[
 \widehat k^{(j)}(\sigma)=0\quad(0\le j<m),
\tag{6A.1}
\]

and

\[
 k^{(\ell)}(0)=0\quad(0\le\ell<r),
 \qquad k^{(r)}(0)=1.
\tag{6A.2}
\]

Here `m` is the finite pole-notch order, while `r+1` is the relative degree at
infinity.  For `N` prescribed distinct rates, the complete classification is

\[
 \boxed{
 \widehat k(s)=
 \frac{(s-\sigma)^mQ(s)}{\prod_{j=0}^{N-1}(s+a_j)},
 \qquad
 \deg Q=N-m-r-1,}
\tag{6A.3}
\]

where `Q` is monic and `Q(sigma)!=0` for exact notch order.  Hence

\[
 \boxed{N\ge m+r+1.}
\tag{6A.4}
\]

The unique minimal filter has `N=m+r+1`, `Q=1`, and

\[
 \boxed{
 c_j=(-1)^r
 \frac{(\sigma+a_j)^m}{\prod_{\ell\ne j}(a_j-a_\ell)}.}
\tag{6A.5}
\]

It has a zero of multiplicity `r` at the endpoint and exactly `m` simple
positive crossings.  Indeed, pole orthogonality forces `m` sign changes, and
the endpoint zero plus those crossings saturate the `N-1=m+r` zero bound for
an `N`-term exponential Chebyshev system.

The scaled multiplier is

\[
 \boxed{
 G_{\epsilon,m,r}(q)=
 \epsilon^r\frac{(q-\sigma\epsilon)^m}
 {\prod_{j=0}^{m+r}(q+a_j\epsilon)}.}
\tag{6A.6}
\]

For `r>=1`, `k(0)=0`, so the moving hard-endpoint term in (1.5) vanishes
**exactly**.  The leading boundary law is then uniform down to `c=0`, and on
compact positive `c`-windows the moment expansion needs no separately sampled
endpoint rate.  Absolute moment tails control the truncation.  Higher-jet
uniformity at `c=0` itself requires enough endpoint derivatives to vanish.

At a fixed singularity offset `omega!=0`,

\[
 \boxed{
 G_{\epsilon,m,r}(\omega+\sigma\epsilon)
 =\epsilon^r\frac{\omega^m}
 {\prod_j(\omega+(\sigma+a_j)\epsilon)}
 \sim\frac{\epsilon^r}{\omega^{r+1}}.}
\tag{6A.7}
\]

Thus endpoint flatness really does attenuate a fixed zero residue by an
algebraic factor.  It does not cancel the singularity for any fixed positive
`epsilon` and does not change its exponential time action.  The exact inverse
tax is the high-frequency behavior

\[
 \boxed{G_{\epsilon,m,r}(q)^{-1}
 \sim\epsilon^{-r}q^{r+1}.}
\tag{6A.8}
\]

The inverse therefore contains differentiating/Dirac-derivative terms and an
`epsilon^(-r)` loss.  Relative to the triangular `q^(-2)` target, the bridge
has high-frequency degree `r-1`: it is an ordinary smoothing kernel at `r=0`,
has feedthrough at `r=1`, and contains derivatives of a point mass for
`r>=2`.

This gives a geometric summary: `m` is the vanishing divisor at the finite
point `s=sigma`; `r+1` is the vanishing divisor at infinity in coordinate
`1/s`.  Minimal filters solve a two-point Hermite interpolation problem on the
Riemann sphere.  Dimension pays for the sum of the two prescribed divisors.

### Associated-Laguerre confluence

Coalescing the stable rates gives the integer two-index normal form

\[
 \boxed{
 k_{m,r,a}(v)=
 \frac{m!}{(m+r)!}v^r e^{-av}
 L_m^{(r)}((a+\sigma)v),
 \qquad
 \widehat k_{m,r,a}(s)=
 \frac{(s-\sigma)^m}{(s+a)^{m+r+1}}.}
\tag{6A.9}
\]

Ordinary Laguerre is precisely the endpoint-normalized slice `r=0`.

### Positive smoothing hierarchy

If the endpoint-normalized order-`m` filter uses the first `m+1` rates and
the order-`r` endpoint-flat filter appends `r` further rates, then exactly

\[
 \boxed{
 G_{\epsilon,m,r}(q)=G_{\epsilon,m,0}(q)
 \prod_{\ell=m+1}^{m+r}
 \frac{\epsilon}{q+a_\ell\epsilon}.}
\tag{6A.10}
\]

For `a_ell>0`, each extra factor has the nonnegative stable impulse
`epsilon*exp(-a_ell*epsilon*t)`.  Endpoint flatness is therefore a one-way
positive smoothing hierarchy.  A same-exponent one-sided estimate
`O(exp(eta*t))` transfers through this factor when
`eta+a_ell*epsilon>0`; equality introduces `t*exp(eta*t)`, and if the sum is
negative the slower kernel tail remains.  Transferring an estimate backward
incurs the differentiating `epsilon^(-r)` inverse.  If `a_ell=0`, the factor
is an integrator and the corresponding rate qualification is essential.  In
particular, inverse instability does not refute a direct Landau argument
performed on the smoothed endpoint-flat response.  Since the implication is
one-way, the smoothed eventual-order premise may be strictly weaker; whether
it is easier for the actual prime measure is open.

## 6B. Fractional endpoint order

The confluence continues beyond finite-state rational filters.  For every
real `alpha>=0`, define

\[
 \boxed{
 k_{m,\alpha,a}(v)=
 \frac{m!}{\Gamma(m+\alpha+1)}v^\alpha e^{-av}
 L_m^{(\alpha)}((a+\sigma)v).}
\tag{6B.1}
\]

Then

\[
 \boxed{
 \widehat k_{m,\alpha,a}(s)=
 \frac{(s-\sigma)^m}{(s+a)^{m+\alpha+1}},
 \qquad
 k(v)\sim\frac{v^\alpha}{\Gamma(\alpha+1)}.}
\tag{6B.2}
\]

For `alpha>0` the hard endpoint again vanishes exactly.  Generalized Laguerre
theory gives exactly `m` positive simple fronts.  Its scaled and fixed-mode
laws are

\[
 G_{\epsilon,m,\alpha}(q)=
 \epsilon^\alpha
 \frac{(q-\sigma\epsilon)^m}
 {(q+a\epsilon)^{m+\alpha+1}},
 \qquad
 G(\omega+\sigma\epsilon)
 \sim\frac{\epsilon^\alpha}{\omega^{\alpha+1}}.
\tag{6B.3}
\]

For noninteger powers, use the branch inherited from
`(q+a*epsilon)^(m+alpha+1)`.  When `0<alpha<1`, the kernel is absolutely
continuous but not `C^1` at zero.  The boundary proof uses (1.3) with
`k' in L^1_loc` and a uniform integrable envelope for its
`v^(alpha-1)` edge singularity; it does not invoke the bounded-derivative
version of Section 1 verbatim.

For noninteger `alpha`, the stable pole becomes a branch point and the filter
is no longer finite-state.  The positivity story can still be retained after
changing the comparison target to a fractional primitive.  Relative to
`H(q)/q^(alpha+2)`, the inverse bridge factors into the usual positive notch
stages and the base factor

\[
 \frac{(q+a\epsilon)^{\alpha+1}}{q^{\alpha+2}},
\]

whose inverse is
`M(-alpha-1,1,-a*epsilon*t)
=exp(-a*epsilon*t)M(alpha+2,1,a*epsilon*t)>0`.
This preserves causal positivity but changes the downstream observable; it
does not supply the missing fixed-delta one-sided exponential-envelope
theorem.

## 6C. Compact support and the two-edge calculus

The rational high-frequency law is not universal among causal kernels.
Compact support creates a second endpoint whose symbol dominates analytic
continuation into the left half-plane.

Fix `T>0`, integers `r_0,r_T>=0`, and let `P_m` be the degree-`m` orthogonal
polynomial on `[0,T]` for the positive weight

\[
 v^{r_0}(T-v)^{r_T}e^{-(a+\sigma)v}dv.
\]

After normalizing the first nonzero left jet (equivalently,
`r_0! kappa_0=1` in the notation below), set

\[
 \boxed{
 k(v)=v^{r_0}(T-v)^{r_T}e^{-av}P_m(v)1_{[0,T)}(v).}
\tag{6C.1}
\]

The half-open convention matters only when `r_T=0`: it sets `k(T)=0` and
therefore excludes an atom exactly at the moving far edge.  With the closed
convention the corresponding formula below contains the left limit `E(x-)`
instead of `E(x)`.

Orthogonality gives an order-`m` zero of `widehat k` at `sigma`, and standard
orthogonal-polynomial theory gives exactly `m` simple roots in `(0,T)`.  Thus
compact pole killers have three independent design indices:

- left endpoint order `r_0`, controlling the ordinary large-positive-`s`
  symbol;
- notch order `m`, controlling cancellation at `s=sigma`; and
- right endpoint order `r_T`, controlling large-negative-`s` continuation.

If

\[
 k(v)\sim\kappa_0v^{r_0}\quad(v\downarrow0),
 \qquad
 k(T-y)\sim\kappa_Ty^{r_T}\quad(y\downarrow0),
\]

then Watson integration at the two edges gives, as `|s|->infinity` in a
closed sector about the positive real ray,

\[
 \widehat k(s)\sim
 \frac{\kappa_0\Gamma(r_0+1)}{s^{r_0+1}}
 \quad(\Re s\to+\infty),
\tag{6C.2}
\]

whereas, as `|s|->infinity` in a closed sector about the negative real ray,

\[
 \boxed{
 \widehat k(s)\sim
 \frac{\kappa_T\Gamma(r_T+1)e^{-sT}}
 {(-s)^{r_T+1}}}
 \quad(\Re s\to-\infty).
\tag{6C.3}
\]

Consequently a fixed left singularity `omega` has multiplier

\[
 \epsilon^{-1}\widehat k(\sigma+\omega/\epsilon)
 \sim
 \frac{\kappa_T\Gamma(r_T+1)\epsilon^{r_T}
 e^{-\sigma T}e^{-\omega T/\epsilon}}
 {(-\omega)^{r_T+1}}.
\tag{6C.4}
\]

This is a Paley--Wiener-type edge escape from the rational `1/omega` law.  In
particular (6C.3) applies along the fixed ray
`s=sigma+omega/epsilon` when `Re(omega)<0`.  At the
support-edge scale

\[
 t=T/\epsilon+x,
\]

the exponential `e^{-omega*T/epsilon}` in (6C.4) cancels the time evolution
of the zero mode.  The remaining contribution is algebraic in `epsilon` and
retains `e^{omega*x}`.  Compact support therefore demodulates the direct flat
zero transient at its far edge.

There is an equally concrete time-side theorem.  For `r_T=0`, assume only the
baseline `E(t)->0` and the compact-kernel regularity used above.  For
`r_T>=1`, assume

\[
 \int_x^\infty (u-x)^{r_T-1}|E(u)|\,du<\infty,
\tag{6C.5a}
\]

and also impose the hard-endpoint condition

\[
 t^{r_T}E(t)\longrightarrow0.
\tag{6C.5b}
\]

When `k(0)!=0`, this condition kills the literal upper endpoint in integration
by parts.  When `k(0)=0`, it is still needed for (6C.5) to denote an ordinary
improper Stieltjes integral.  If instead (6C.6) is taken as the primary
renormalized/distributional definition, it can be omitted in that
endpoint-flat case.  Under the displayed hypotheses, for `x>=0`,

\[
 \boxed{
 \epsilon^{-r_T}B_{\epsilon,k}(T/\epsilon+x)
 \longrightarrow
 \kappa_T\int_{(x,\infty)}(u-x)^{r_T}\,dE(u).}
\tag{6C.5}
\]

For `r_T=0` this is `-kappa_T E(x)` with the half-open convention in (6C.1).
For `r_T>=1`, integration by parts gives

\[
 \boxed{
 -\kappa_T r_T\int_x^\infty
 (u-x)^{r_T-1}E(u)\,du.}
\tag{6C.6}
\]

Condition (6C.5b) is not a consequence of the absolute moment in (6C.5a):
narrow endpoint spikes give counterexamples, exactly as in Section 2.

Thus the far-edge layer reconstructs tail primitives of the discrepancy.  It
really does expose the beyond-all-orders remainder, but the new target is a
Volterra transform of that same unknown tail.  The full profile is injective:
for `r_T>=1`, differentiating (6C.6) `r_T` times in the distributional sense
recovers

\[
 \frac{d^{r_T}}{dx^{r_T}}F_{r_T}(x)
 =(-1)^{r_T+1}\kappa_T r_T!E(x).
\]

This does **not** mean that a one-sided or exponential bound for one primitive
automatically gives the same bound for `E`; differentiation needs additional
regularity or a Tauberian input.  The compact-support construction therefore
rephrases, rather than solves, the arithmetic tail problem.

There is also a decisive quantifier boundary: (6C.5)--(6C.6) take
`epsilon->0` for each fixed `x` (locally uniformly only under uniform
hypotheses on bounded `x`-windows).  Landau fixes `epsilon` and then sends
`t`, equivalently `x`, to infinity.  Injectivity of the family of fixed-`x`
limits is not a stable two-parameter reconstruction theorem.  In particular,
the `r_T=0` identity merely returns `E(x)`; it supplies no decay estimate.

A simple replayable first-order example is

\[
 k(v)=(1-v/T)(1-\lambda v)1_{[0,T]}(v),
 \qquad
 \lambda=
 \frac{\int_0^T e^{-\sigma v}(1-v/T)dv}
 {\int_0^T ve^{-\sigma v}(1-v/T)dv}.
\tag{6C.7}
\]

It has `k(0)=1`, `k(T)=0`, one interior sign change, and
`widehat k(sigma)=0`.  Since `k'(T)!=0`, its left-half-plane symbol is the
`r_T=1` case of (6C.3).

## 6D. Fractional two-edge and multiple-notch compact synthesis

The compact construction admits both continuous endpoint orders and several
real anchors.  Fix `alpha_0,alpha_T>=0`, distinct positive anchors `sigma_h`
with multiplicities `m_h`, and put `M=sum_h m_h`.  The exponential-polynomial
space

\[
 \mathcal U=
 \operatorname{span}\{v^j e^{-\sigma_hv}:0\le j<m_h\}
\tag{6D.1}
\]

is an `M`-dimensional extended Chebyshev system on `(0,T)`.  For the positive
interior weight

\[
 W(v)=v^{\alpha_0}(T-v)^{\alpha_T}e^{-av},
\]

there is a unique monic polynomial `P_M` of degree `M` such that

\[
 \boxed{\int_0^T W(v)P_M(v)u(v)\,dv=0
 \quad\hbox{for every }u\in\mathcal U.}
\tag{6D.2}
\]

Indeed, singularity of the mixed moment matrix would produce a nonzero
polynomial of degree at most `M-1` orthogonal to the Chebyshev space.  The
standard sign-change argument would force at least `M` sign changes, a
contradiction.  The same argument applied to `P_M` shows that all of its `M`
zeros are simple and lie in `(0,T)`.

Normalize `N` by

\[
 N T^{\alpha_T}P_M(0)=\Gamma(\alpha_0+1)^{-1}
\]

and define

\[
 \boxed{k(v)=N W(v)P_M(v)1_{[0,T)}(v).}
\tag{6D.3}
\]

Then every requested notch is exact:

\[
 \boxed{\widehat k^{(j)}(\sigma_h)=0
 \quad(0\le j<m_h),\qquad
 \widehat k^{(m_h)}(\sigma_h)\ne0.}
\tag{6D.4}
\]

The nonvanishing follows because adding the next confluent exponential to
(6D.1) again gives a Chebyshev system; one extra orthogonality condition would
force `M+1` sign changes.  Thus (6D.3) is a canonical compact multi-notch
filter with exactly the information-theoretic minimum `M` interior fronts.
For a single anchor it reduces to the Jacobi-weighted orthogonal-polynomial
construction in Section 6C, now with fractional endpoint orders.

If `k(T-y)~kappa_T y^(alpha_T)`, the two symbol laws become

\[
 \widehat k(s)\sim s^{-\alpha_0-1},
 \qquad
 \widehat k(s)\sim
 \frac{\kappa_T\Gamma(\alpha_T+1)e^{-sT}}
 {(-s)^{\alpha_T+1}}
\tag{6D.5}
\]

in the positive- and negative-ray sectors, respectively.  At a fixed left
singularity the far-edge multiplier is therefore proportional to
`epsilon^(alpha_T) exp(-omega*T/epsilon)/(-omega)^(alpha_T+1)`.
The powers use the continuous branches selected inside those sectors; no
uniform assertion is made through their Stokes boundaries.

The time-side result also continues fractionally.  For `alpha_T>0`, assume

\[
 \int_x^\infty (u-x)^{\alpha_T-1}|E(u)|\,du<\infty
\]

and impose the safe moving-current-edge condition

\[
 t^{\alpha_T}E(t)\longrightarrow0
\tag{6D.5a}
\]

regardless of the left endpoint order.  (For a sufficiently regular
left-edge taper this can be weakened to a uniform concentration condition,
but pointwise moments alone do not suffice when `0<alpha_0<1`.)  Then, for
each fixed `x`,

\[
 \boxed{
 \epsilon^{-\alpha_T}B_{\epsilon,k}(T/\epsilon+x)
 \longrightarrow
 -\kappa_T\alpha_T\int_x^\infty
 (u-x)^{\alpha_T-1}E(u)\,du.}
\tag{6D.6}
\]

This is a right-sided Riemann--Liouville fractional integral.  It is inverted
by the corresponding fractional derivative only under its usual domain and
regularity hypotheses.  Formula (6C.6) is the integer slice.  For
`alpha_T=0`, use the open-tail value `-kappa_T E(x)`.

The proof of (6D.6) must split the two kernel edges.  The far edge is handled
by the displayed weighted tail integral; the current edge uses (6D.5a) and
local integrability of `k'`.  A single global dominated-convergence envelope
is false for a fractional left taper, and narrow moving spikes expose the
failure.  Local uniformity in `x` requires the corresponding tail and
current-edge hypotheses uniformly on the chosen `x`-interval.

For nonreal anchors, the linear moment construction may still exist, but the
real Chebyshev, exact-front, and scalar sign conclusions do not follow.  This
is the same complex-anchor boundary already exposed in Section 7.

## 7. Multiple notches and multiple fronts

For positive frequencies `sigma_h` with multiplicities `m_h`, let
`M=sum_h m_h`.  The unique minimal `(M+1)`-rate transfer is

\[
 \boxed{
 \widehat k(s)=
 \frac{\prod_h(s-\sigma_h)^{m_h}}
 {\prod_{j=0}^{M}(s+a_j)},
 \qquad
 c_j=
 \frac{\prod_h(a_j+\sigma_h)^{m_h}}
 {\prod_{\ell\ne j}(a_j-a_\ell)}.}
\tag{7.1}
\]

The confluent exponential system
`{v^r exp(-sigma_h*v):0<=r<m_h}` is a Chebyshev system.  Orthogonality forces
`M` crossings; the `(M+1)`-rate output has at most `M`, so it has exactly `M`
simple crossings.  Its inverse contains every unstable family

\[
 P_h(t)e^{\sigma_h\epsilon t},
 \qquad \deg P_h=m_h-1,
\]

with nonzero leading coefficient.  Particular lower coefficients of `P_h`
may vanish.

This extension can cancel a finite prescribed constellation.  It cannot
cancel an unknown infinite zero set with fixed finite dimension.

The residue formula (7.1) is algebraic and continues to complex anchors and
stable poles, provided no numerator and denominator node collides.  A
conjugation-invariant anchor multiset with real stable rates produces a real
oscillatory kernel.  At an anchor of multiplicity `m_h`, its inverse contains
a nonzero degree-`m_h-1` polynomial times
`exp(sigma_h*epsilon*t)` and is unstable whenever
`Re(sigma_h)>0`.  The exact `M`-sign-change conclusion is licensed only for
positive real anchors, where the confluent exponential functions form a real
Chebyshev system; it is not asserted for general complex notches.

If a boundary kernel itself has a zero of multiplicity `m` at `c_0`, assume
the absolute-moment and Taylor-remainder hypotheses of Section 2 through
`K_(m-1)`, `C^(m+1)` regularity, and an endpoint remainder `o(epsilon^m)`
near `c_0`.  Writing `c=c_0+d*epsilon`, every bounded real displacement limit
must be a real root of

\[
 \boxed{
 C d^m+m\sum_{r=0}^{m-1}(-1)^{r+1}
 {m-1\choose r}K_r d^{m-1-r}=0.}
\tag{7.2}
\]

The polynomial need not have `m` real roots, so an `m`-fold real front need
not split into `m` real crossings.  If
`K_0=...=K_(m-2)=0`, the equation reduces to

\[
 d^m=(-1)^{m+1}\frac{mK_{m-1}}C.
\]

## 8. Universal motion of simple fronts

Let `C!=0`, let `K_0` exist, and let `c_*` be a simple zero of `k`.  The zero
of the first-order smooth/formal asymptotic profile satisfies

\[
 \boxed{
 c_\epsilon=c_*+\frac{K_0}{C}\epsilon+o(\epsilon).}
\tag{8.1}
\]

The first motion is independent of the kernel, notch order, rates, and
`sigma`.  If the second moment data exist, its next coefficient is

\[
 \boxed{
 \left(\frac{K_0^2}{2C^2}-\frac{K_1}{C}\right)
 \left(\frac{k''(c_*)}{k'(c_*)}-2\sigma\right).}
\tag{8.2}
\]

For an atomic arithmetic ramp, an exact equality `B=0` need not occur at a
jump.  To transfer (8.1) to the actual hard-cutoff sign bracket requires
`E(c/epsilon)=o(epsilon)` uniformly near `c_*`; (8.2) requires
`o(epsilon^2)`, `K_1`, and the corresponding derivatives.  Endpoint-zero
smoothing is an alternative.  In zeta applications the strong PNT remainder
and the mesoscopic jump size meet these conditions, so (8.1)--(8.2) locate a
sign-transition bracket to every algebraic order.

More generally, for a finite-dimensional derivative-invariant `k`, or for an
analytic vector with a controlled convergent functional calculus, the
implicit function theorem applied to
`H(-epsilon*(sigma-partial_c))k` produces a unique analytic surrogate front
through every simple zero.  All of its coefficients are recursive
Bell/Faa-di-Bruno polynomials in the Laurent coefficients and the jet of `k`
at the front.  For a generic analytic `k` without derivative-growth control,
this is only a formal implicit series.  Equations (8.1)--(8.2) are the first
two terms.  Under a rapid discrepancy remainder in the controlled cases, the
arithmetic sign-transition bracket has this same expansion to every fixed
order, with only a flat error left.

## 9. Dirichlet-series transfer

Let

\[
 D(s)=\sum_{n\ge1}b_nn^{-s},\qquad
 D(\sigma_0+w)=\frac r w+H(w),
 \qquad H(w)=\sum_{j\ge0}\kappa_jw^j.
\tag{9.1}
\]

Remove an atom at `n=1` if necessary and define

\[
 A(t)=\sum_{\log n\le t}b_nn^{-\sigma_0}-rt
 =\kappa_0+E(t).
\tag{9.2}
\]

The convergence in (9.2) is a separate weighted-PNT hypothesis; meromorphic
continuation alone does not imply it.  With `C=-kappa_0`, define

\[
 \begin{aligned}
 B_{\epsilon,k}(t)={}&
 \sum_{n\le e^t}b_nn^{-(\sigma_0-\sigma\epsilon)}
 k(\epsilon(t-\log n))\\
 &-r\int_0^t e^{\sigma\epsilon u}
 k(\epsilon(t-u))\,du.
 \end{aligned}
\tag{9.3}
\]

Then

\[
 \boxed{
 \widehat B_{\epsilon,k}(q)=
 \epsilon^{-1}\widehat k(q/\epsilon)
 H(q-\sigma\epsilon),}
\tag{9.4}
\]

initially in a common convergence half-plane, followed by continuation.
Moreover,

\[
 \boxed{
 B_{\epsilon,k}(c/\epsilon)\longrightarrow\kappa_0k(c).}
\tag{9.5}
\]

The theorem depends only on the weighted-Mertens limit (9.2), so it also
applies to abstract and Beurling counting measures once that limit is known.

### Higher principal parts

If

\[
 D(\sigma_0+w)=\sum_{j=1}^p r_{-j}w^{-j}+H(w),
\]

the time-side principal density is

\[
 \sum_{j=1}^p\frac{r_{-j}}{(j-1)!}u^{j-1}.
\]

For a bounded universal boundary profile one must subtract this whole
polynomial.  An order-`p` notch cancels the corresponding pole in the
continued `q`-transform, but that is not the same as boundary centering: the
hard cutoff leaves a large transient.  Indeed an uncentered term
`r_(-j)w^(-j)` contributes exactly

\[
 \boxed{
 \frac{r_{-j}\epsilon^{-j}}{(j-1)!}
 \int_0^c e^{\sigma v}k(c-v)v^{j-1}\,dv.}
\tag{9.6}
\]

The full infinite-range moment may vanish after pole killing while this
truncated integral does not.  For the symmetric first-order kernel and a
simple pole, (9.6) is `r(1-e^(-c))/epsilon`.

For `-L'/L`, even an order-`r` pole or zero of `L` produces only a simple pole
with residue `+r` or `-r`; the ordinary first-order notch remains the relevant
one.  A genuine example with `p>1` is `D(s)=zeta(s)^p`: after subtracting its
full Laurent polynomial, the regular remainder gives a divisor-function
boundary calculus.  An order-`p` notch may additionally regularize the
uncentered transform, but cannot replace that subtraction on the boundary
scale.

## 10. Laurent-germ functional calculus

Let

\[
 \mathcal L=\sigma-\partial_c.
\]

Whenever the relevant ordinary moments exist (for example, absolutely), the
moment/Laurent relation following from (9.1)--(9.2) is

\[
 K_m=(-1)^m m!\kappa_{m+1}.
\tag{10.1}
\]

Therefore, to every order licensed by those moments and the endpoint bound,
the boundary expansion is

\[
 \boxed{
 B_{\epsilon,k}(c/\epsilon)
 \sim[H(-\epsilon\mathcal L)k](c).}
\tag{10.2}
\]

Under rapid `E`, all moments and endpoint bounds are available, and for a
finite exponential kernel the all-orders surrogate resums to

\[
 \boxed{
 \mathcal S_\epsilon(c)=
 \sum_jc_je^{-a_jc}H(-\epsilon(\sigma+a_j)).}
\tag{10.3}
\]

If `E` has a rapid, for example stretched-exponential, remainder, then for
every fixed `N`, fixed filter dimension, compact positive `c`-window, and
compact rate set,

\[
 B_{\epsilon,k}(c/\epsilon)-\mathcal S_\epsilon(c)
 =O_N(\epsilon^N).
\tag{10.4}
\]

This is an all-orders asymptotic statement, not an exact identity and not a
claim that the formal series converges.

For the confluent Laguerre kernel, put `b=a+sigma`.  Nilpotence of the
derivative on degree-`m` polynomials gives the finite Jordan formula

\[
 \boxed{
 \mathcal S_\epsilon(c)=e^{-ac}
 \sum_{r=0}^m\frac{(-\epsilon b)^r}{r!}
 H^{(r)}(-\epsilon b)L_{m-r}^{(r)}(bc).}
\tag{10.5}
\]

Equations (10.2)--(10.5) are Laurent-jet tomography: changing the kernel
changes how the same regular germ is sampled.  A finite jet contains only
finite local data.  The complete infinite germ can encode its singularities
through coefficient growth and analytic continuation, but exploiting that
requires quantitative all-order information not supplied by a finite
boundary expansion.

### Invariant-module and semigroup formulation

The exponential and confluent cases are instances of one finite-dimensional
theorem.  Let `V` be any finite-dimensional space of kernels invariant under
`partial_c`, let `L=sigma-partial_c` on `V`, and let `H` be holomorphic on a
neighborhood of `-epsilon*spec(L)`.  Then the perturbative surrogate is the
ordinary matrix functional calculus

\[
 \boxed{\mathcal S_\epsilon=H(-\epsilon L)k.}
\tag{10.6}
\]

Diagonalizing `L` gives (10.3); its Jordan blocks give derivatives of `H` and
associated Laguerre/exponential-polynomial formulas such as (10.5).  The map

\[
 H\longmapsto H(-\epsilon L)
\]

is an algebra homomorphism from regular germs to endomorphisms of `V`.  Every
finite-dimensional derivative-invariant kernel space consists of
exponential polynomials, so this includes ordinary impulse responses of
finite-dimensional constant-coefficient systems, not only sums with simple
real rates.  Direct-feedthrough distributions require separate bookkeeping.

On an infinite-dimensional function space the same statement is available
for analytic vectors of the translation generator, or through a holomorphic
semigroup functional calculus, provided the spectrum, domains, and remainder
bounds are controlled.  Those hypotheses are substantive; the notation
`H(-epsilon*L)` alone does not establish them.

## 11. Endpoint-normalized uniform-symbol filters do not attenuate fixed singularities

Suppose `D` has a non-pole singularity at

\[
 \rho=\sigma_0+\omega,\qquad\omega\ne0.
\]

It appears in (9.4) at `q_rho=omega+sigma*epsilon`.  For the minimal order-`m`
filter, its exact multiplier there is

\[
 \boxed{
 G_\epsilon(q_\rho)=
 \frac{\omega^m}
 {\prod_{j=0}^m(\omega+(\sigma+a_j)\epsilon)}.}
\tag{11.1}
\]

Hence

\[
 \boxed{
 G_\epsilon(q_\rho)\longrightarrow\frac1\omega,}
\tag{11.2}
\]

independently of `m` and of all stable rates.  Endpoint normalization forces
this common high-frequency response.

The limit is not special to the minimal formula.  Any epsilon-independent,
ordinary continuous rational impulse kernel with strictly proper transfer and
`k(0+)=1` satisfies

\[
 \widehat k(s)=\frac1s+O(s^{-2})
 \quad(s\to\infty),
\]

and therefore, along every fixed nonzero rational-continuation direction,

\[
 \epsilon^{-1}\widehat k(\sigma+\omega/\epsilon)
 =\frac1\omega+O(\epsilon).
\tag{11.3}
\]

So no fixed-dimensional normalized exponential-polynomial filter with a
uniform high-frequency expansion attenuates a fixed singularity at leading
order, regardless of its extra modes or notch order.  A merely proper transfer
may contain a Dirac feedthrough and is outside this assertion.  This extension
uses rational continuation; it is not an asymptotic claim for an arbitrary
Laplace transform deep in its left half-plane.

The same high-frequency law is matrix-valued.  If an epsilon-independent
strictly proper rational matrix impulse kernel has `K(0+)=I`, then

\[
 \epsilon^{-1}\widehat K(\sigma+\omega/\epsilon)
 =\frac I\omega+
 \frac{\epsilon(K'(0+)-\sigma I)}{\omega^2}+O(\epsilon^2).
\tag{11.3a}
\]

Changing the leading response to a fixed singularity therefore requires an
endpoint jet or generator of size at least `1/epsilon`, loss of uniform
meromorphic-at-infinity control, or endpoint flatness as in Section 6A.

There is a stronger modulus statement that permits growing order.  Write
`b_j=sigma+a_j>0`.  Exactly,

\[
 G_\epsilon(q_\rho)=\frac1\omega
 \prod_{j=0}^m\left(1+\frac{b_j\epsilon}{\omega}\right)^{-1}.
\tag{11.4}
\]

If `Re(omega)<0` and

\[
 0<b_j\epsilon<-2\Re\omega
 \quad\hbox{for every }j,
\]

then

\[
 \left|1+\frac{b_j\epsilon}{\omega}\right|<1,
 \qquad
 \boxed{|G_\epsilon(q_\rho)|>|\omega|^{-1}.}
 \tag{11.5}
\]

Thus even an order `m=m(epsilon)` that grows cannot attenuate a fixed
left-half-plane singularity while all physical notch scales
`b_j*epsilon` remain below its distance-to-boundary threshold.  If additionally
`max_j b_j*epsilon->0`, `sum_j b_j*epsilon->Lambda`, and the quadratic sum
tends to zero, then

\[
 G_\epsilon(q_\rho)\longrightarrow
 \frac1\omega e^{-\Lambda/\omega},
\tag{11.6}
\]

whose modulus is larger than `1/|omega|` when `Lambda>0`.

For zeta, `omega=rho-1`.  A fixed zero contributes a direct hard-cutoff mode on the boundary
scale proportional to

\[
 \exp((\rho-1)c/\epsilon),
\]

up to algebraic and bounded exponential factors.  It is therefore beyond all
orders in `epsilon` when `Re(rho)<1`.  Higher pole cancellation reshapes only
an `O(epsilon)` neighborhood of `s=1`; on the endpoint-normalized slice it
neither moves nor attenuates a fixed zero at leading order.  Endpoint-flat
order `r` supplies the genuine algebraic attenuation `epsilon^r`, but still
does not change the exponent or remove the transform singularity.

This is the decisive no-improvement theorem for the fixed-order,
endpoint-normalized higher-filter route.  Section 6A gives its exact escape
tax rather than pretending no escape exists.

This conclusion is pointwise for fixed `omega`.  Failure of a uniform strip
would involve a sequence `omega_n=-d_n+i*gamma_n` with `d_n->0` and
`|gamma_n|->infinity`.  No statement above is uniform in that joint regime;
such a use requires a separate zero-height and `(omega,epsilon)` growth
ledger.
Rates with `b_j*epsilon` comparable to or larger than the fixed spectral gap
can attenuate that one mode algebraically, but they place stable poles at a
physical rather than boundary scale and make the rate/derivative constants,
and sometimes the coefficients, singular.  They no longer inherit the
boundary theorem uniformly.  Complex/matrix filters and noncausal filters lie
outside the scalar alternation theorem; normalized fixed matrix filters still
obey (11.3a), while genuine cross-channel or future-data cancellation requires
a new downstream order structure.

## 12. Where the strip information lives

For zeta, classical zero-free information gives a stretched-exponentially
small weighted-PNT error.  For rational or, more generally, uniform-symbol
kernels on `t=c/epsilon`, the direct hard-cutoff transient of every fixed left
zero, and the difference between the response and its germ surrogate, are
flat in `epsilon`.  Every fixed finite delta jet in that interior branch
therefore misses the direct transient.

Compact support is the explicit edge exception.  For a support length `T`,
the isolated residue factor is proportional to
`exp(omega*(c-T)/epsilon)`: it is flat for `c>T`, algebraic at `c=T`, and
exponentially large before the far edge.  In the last regime it must be
combined with the causal endpoint terms and is not an independently
controlled signal.  At `c=T`, Section 6C identifies the complete edge profile
with a Volterra tail transform rather than with a finite Laurent jet.

The **complete** Laurent germ does not forget the zeros: a singular term
`1/(w+a)` contributes
`(-1)^j a^(-j-1)` to every Taylor coefficient, and singularity locations are
encoded in coefficient growth and analytic continuation.  But coefficient
growth at the single center `w=0` directly controls only a Euclidean disk up
to the nearest singularity, not an unbounded vertical half-plane.  What is
absent is a quantitative **global or vertically translated** continuation
theorem with uniform constants.  Abstract uniqueness of analytic
continuation is not a stable strip estimate.

In an explicit formula, a zero `rho` heuristically/conditionally contributes
the exponential scale displayed in Section 11.  Making that statement
termwise requires the usual contour-shift and zero-sum controls; it is not
promoted here to an unconditional transseries identity.

A uniform zero-free strip would correspond to a true exponential envelope

\[
 |E(t)|\lesssim e^{-\eta t}
 \quad\Longleftrightarrow\quad
 |E(c/\epsilon)|\lesssim e^{-\eta c/\epsilon}
\]

up to standard epsilon losses and growth hypotheses.  Thus the remaining
mathematics is one of the following:

1. prove a global/translated-germ propagation theorem, with high-order bounds
   uniform in height, strong enough to continue through a fixed half-plane;
2. prove an exponential remainder after subtracting the Laurent-germ
   surrogate, uniformly for unbounded `c/t` strongly enough to reach the
   fixed-`epsilon` eventual regime;
3. prove a fixed-`epsilon`, eventual one-sided inequality strong enough for
   Landau's theorem; or
4. introduce a genuinely nonperturbative amplifier that converts the flat
   zero contribution into a controlled algebraic signal without importing an
   equivalent strip estimate.

Adding only finitely many further Laurent jets is not another route.  Even a
one-center `j->infinity` radius theorem yields only a disk; the logically open
route requires height-uniform propagation or equivalent global analytic
control.

## 13. Exact Landau adapter and its limits

Let a fixed-`epsilon` filtered response be real, locally integrable, and known
to have some finite initial Laplace convergence abscissa, as in the
Dirichlet-series setting of Section 9.  If, for some `eta`, it is eventually
bounded on either side by `C exp(eta*t)`, add the corresponding exponential
and a compact correction to obtain a globally nonnegative function.  Landau's
theorem says that a finite Laplace abscissa is a singularity on the real axis.

If the continued transform has no real-axis singularity at any `q>eta`, its
Laplace integral therefore converges and is holomorphic in `Re(q)>eta`.  Formula
(9.4) then excludes every uncanceled singularity of `D` in

\[
 \Re s>\sigma_0-\sigma\epsilon+\eta.
\]

This improves on the original line `Re(s)=sigma_0` only when
`eta<sigma*epsilon`; the certified strip width is exactly
`sigma*epsilon-eta`.

The qualifications are essential:

- coefficient positivity is not enough; the **filtered function** needs a
  real one-sided order;
- a real exceptional zero supplies exactly the real singularity Landau
  permits and must be excluded separately;
- the minimal rational endpoint-flat multiplier has no zeros beyond its
  intended pole notch, but a compact transform can have additional complex
  zeros; a compact-filter strip argument therefore needs a multiplier
  zero-free on the target region or a jointly coprime separating family;
- the diagonal limit `epsilon->0`, `t=c/epsilon` does not imply an eventual
  inequality as `t->infinity` for each fixed `epsilon`; and
- a complex-valued response has no scalar one-sided order.

For the Riemann zeta function there is no real zero in `(0,1)`, but the needed
fixed-delta ramp inequality remains unproved.

## 14. Converse, vector, and multivariate extensions

### Volterra identifiability

For a general product kernel `Phi_c(z)=p(z)k(c-z)`, (1.2) can be written

\[
 R_{1/T}(c)=p(c)k(0)A(Tc)-
 \int_0^c\partial_z[p(z)k(c-z)]A(Tz)\,dz.
\tag{14.1}
\]

Assume `p(0)k(0)!=0`, with `p,k` continuously differentiable.  Then the
diagonal coefficient stays uniformly away from zero on some sufficiently
short interval, and there this is a Volterra equation of the second kind,
injective and stably invertible.  Stability on a prescribed interval `[0,C]`
requires the stronger condition
`inf_(0<=c<=C)|p(c)k(0)|>0` (or a separate resolvent hypothesis).

A local Gronwall argument shows that if bounded `A` has the locally uniform
limiting response associated with a constant `D` near the origin, then
`A(Tc)->D` there.  Fixing one such `c>0` and writing `T=t/c` gives
`A(t)->D`.  The condition at zero cannot be weakened merely to nonvanishing
for `c>0`:
with `p(z)=z` and `k=1`, every constant limiting discrepancy is annihilated in
the leading response.

So a local boundary profile with nonzero diagonal identifies the limiting
discrepancy even though global causal inversion of a pole-killing filter is
exponentially unstable.  Local identifiability and global stability are
different questions.

### Banach and operator values

Equations (1.3)--(3.3) extend componentwise to Banach-valued measures under
norm bounded variation and Bochner moment hypotheses.  There is also a
positive-operator no-go.  If `K(t)` is positive semidefinite and

\[
 \widehat K(\sigma)v=0,
\]

then

\[
 0=\int_0^\infty e^{-\sigma t}
 \langle K(t)v,v\rangle dt
\]

forces `K(t)v=0` almost everywhere.  A positive operator filter can notch a
direction only by being pointwise blind to it; vectorization alone does not
create positive cancellation.

There is also a semigroup version of the boundary calculus.  Let `T(z)=e^{zG}`
be a strongly continuous semigroup and let `K(c)` be an operator kernel.  On
vectors in the required generator domains, replace the scalar test by

\[
 \Phi_c(z)x=T(z)K(c-z)x.
\]

Then (1.3) remains exact with

\[
 \Phi_c'(z)x=T(z)[GK(c-z)-K'(c-z)]x,
\]

and the moment jets are

\[
 (G-\partial_c)^{n+1}K(c)x.
\]

Thus the germ surrogate is `H(-epsilon*(G-partial_c))K`.  A bounded fixed
generator cannot evade the uniform principal-symbol law.  Evasion requires
`epsilon*G=O(1)` on the selected vectors, exploding graph norms, or a
nonuniform endpoint jet—the operator version of the same inverse tax.

### Several scaling variables

If a multivariate cumulative `A(T_1z_1,...,T_dz_d)/b(T)` converges in local
`L^1` to `G`, then its mixed distributional derivative converges to
`partial_1...partial_d G`.  A constant interior tangent on the positive
orthant produces a corner delta at the origin.

Hard boxes are subtler: every face, edge, and corner contributes its own
endpoint term.  Diagonal information `A(T,...,T)` is insufficient.  A full
multivariate all-orders calculus requires the face/Mobius hierarchy, not one
bulk discrepancy function.

More explicitly, for a smooth test on the box `[0,c_1]x...x[0,c_d]`, repeated
integration by parts gives

\[
 \boxed{
 R_{\boldsymbol\epsilon}(\mathbf c)=
 \sum_{S\subseteq[d]}(-1)^{|S|}
 \int_{[0,\mathbf c]_S}
 \partial_S\Phi(\mathbf z_S,\mathbf c_{S^c})
 A(\mathbf z_S/\boldsymbol\epsilon_S,
   \mathbf c_{S^c}/\boldsymbol\epsilon_{S^c})
 \,d\mathbf z_S.}
\tag{14.2}
\]

This is the exact face/Mobius expansion.  For product causal kernels,
`k_i(0)=0` kills every proper upper-face term in the corresponding coordinate;
partial endpoint flatness removes the associated sublattice of faces.  Product
relative orders `r_i` yield fixed-mode factors
`prod_i epsilon_i^(r_i)/omega_i^(r_i+1)`.  They smooth face artifacts but do
not replace the full anisotropic tangent data.

## 15. Arithmetic instances

### Riemann zeta

With

\[
 F(s)=-\frac{\zeta'}{\zeta}(s)-\frac1{s-1},
 \qquad F(1)=-\gamma,
\]

the weighted-Mertens discrepancy has `C=gamma`, and (10.2) becomes

\[
 B_{\epsilon,k}(c/\epsilon)
 \sim[F(1-\epsilon(\sigma-\partial_c))k](c).
\]

For `k(c)=2e^{-c}-1`, this recovers the previously proved Euler boundary
profile and all of its Stieltjes-constant jets.

### Dedekind zeta functions

For a fixed number field `K`,

\[
 -\frac{\zeta_K'}{\zeta_K}(1+w)
 =\frac1w-\gamma_K+O(w).
\]

The fixed-field prime-ideal theorem supplies the required decay, giving for
the symmetric kernel

\[
 B_{K,\epsilon}(c/\epsilon)
 =\gamma_K(1-2e^{-c})+O_{K,[a,b]}(\epsilon).
\]

Uniformity over a family of fields would need uniform PNT errors and separate
control of exceptional real zeros.

### Automorphic and Selberg-class examples

The algebra applies to regularized logarithmic derivatives in the Selberg
class.  A weighted PNT and real-valued response must be added as hypotheses;
they are not automatic from the axioms.  A safe imported PNT instance is a
unitary cuspidal self-contragredient Rankin--Selberg setting covered by
Liu--Ye.  Their PNT remainder supplies all moments for the boundary theorem.

The finite Euler-product `L`-function is intended.  Passing to a completed
`L`-function adds explicit archimedean terms and changes the discrete ramp.

## 16. Literature and novelty assessment

The closest ingredients found are:

- Dixit--Murty's Proposition 2.1 gives a general Laurent-constant/PNT-error
  identity, a direct ancestor of the moment dictionary:
  [Acta Arithmetica paper](https://www.imsc.res.in/~anupdixit/IharaConjecture.pdf).
- Ghosh studies higher Euler--Kronecker Laurent coefficients, so the
  coefficients themselves are not new:
  [arXiv:2411.17946](https://arxiv.org/abs/2411.17946).
- Liu--Ye prove the automorphic Rankin--Selberg PNT used above:
  [PAMQ paper](https://intlpress.com/site/pub/files/_fulltext/journals/pamq/2007/0003/0002/PAMQ-2007-0003-0002-a004.pdf).
- Kaczorowski--Perelli show that the Selberg-class PNT is tied to
  nonvanishing on the line `Re(s)=1`:
  [DOI](https://doi.org/10.1007/s00013-003-0032-9).
- Landau's original positivity/singularity theorem is the external input to
  Section 13:
  [EuDML](https://eudml.org/doc/158244).
- Laguerre functions and repeated-pole filters are classical in system
  identification and inverse Laplace analysis:
  [Wahlberg 1982](https://doi.org/10.1016/0016-0032(82)90070-9),
  [Abate--Choudhury--Whitt 1996](https://doi.org/10.1287/ijoc.8.4.413).
- Positivity and location of Laguerre zeros are standard orthogonal-polynomial
  facts:
  [DLMF Section 18.16](https://dlmf.nist.gov/18.16).

No source was found stating the full combined package: scaled discrepancy
delta jets, the two-index pole-notch/endpoint classification, universal front
motion, associated-Laguerre confluence, germ functional calculus, the
uniform-symbol obstruction, and its endpoint-flat and compact-edge escapes.

The conservative novelty assessment is:

- the individual transform and interpolation identities are elementary or
  classical;
- the boundary theorem and jet package are apparently unrecorded but short
  Abelian consequences of known weighted-Mertens theory;
- the strongest reusable synthesis is the delta-jet/germ calculus together
  with the exact alternation-instability theorem and the three-way spectral
  tradeoff between normalized rational, endpoint-flat, and compact-edge
  filters;
- this is low-to-moderate theorem-suite novelty, not a major number-theory
  breakthrough; and
- it supplies no new zero-free strip without a nonperturbative arithmetic
  estimate.

One citation warning survived the audit: the displayed constant in Liu--Ye
Corollary 2.4 appears shifted by `-1` relative to direct partial summation and
Dixit--Murty Proposition 2.1.  This report uses Liu--Ye only for the PNT
remainder and identifies constants independently from Laurent expansion.

## 17. Replay and formal certificates

Exact rational and high-precision replay is in
[`pole_killing_boundary_calculus.py`](../src/pole_killing_boundary_calculus.py)
with tests in
[`test_pole_killing_boundary_calculus.py`](../src/test_pole_killing_boundary_calculus.py).

The replay covers:

- arbitrary fixed order and rational rates;
- arbitrary positive rational anchor;
- multiple anchors and multiplicities;
- the full notch/endpoint-flat bidegree classification;
- associated and fractional Laguerre normal forms;
- compactly supported fractional two-edge, multi-anchor synthesis;
- scaled multipliers and fixed-singularity response;
- Laguerre confluence;
- boundary jets and germ functional calculus;
- inverse unstable coefficients; and
- multiple-front splitting polynomials.

Selected low-order algebra is kernel-checked in
[`HigherPoleKillingFilters.lean`](../lean/rhbridge/RHBridge/HigherPoleKillingFilters.lean)
and its axiom audit
[`HigherPoleKillingFiltersAudit.lean`](../lean/rhbridge/RHBridge/HigherPoleKillingFiltersAudit.lean).

Replay commands:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_pole_killing_boundary_calculus.py

cd lean/rhbridge
lake build RHBridge.HigherPoleKillingFilters
lake env lean RHBridge/HigherPoleKillingFiltersAudit.lean
```

Final replay on 2026-09-01: `35` general-calculus tests plus `17` legacy
shifted-ramp tests passed (`52` total).  The compact Chebyshev solver uses the
scale-free coordinate `v/T`, closed beta--hypergeometric moments, guarded
precision, and explicit relative-notch residual checks.  The Lean module and
axiom audit also passed; the selected identities use only Lean's standard
`propext`, `Classical.choice`, and `Quot.sound` axioms.

## 18. Decision-tree update

This execution maps the fixed-order perturbative branch as follows.

\[
 \text{weighted PNT limit}
 \Longrightarrow
 \text{universal leading boundary profile},
\]

\[
 \text{limit + moments + endpoint control}
 \Longrightarrow
 \text{finite Laurent jets},
\]

and

\[
 \text{rapid error}
 \Longrightarrow
 \text{all-orders germ surrogate},
\]

while independently

\[
 \text{order-}m\text{ pole notch}
 \Longrightarrow
 m\text{ sign changes}
 +t^{m-1}e^{\sigma\epsilon t}\text{ inverse instability}.
\]

The two chains meet in the scoped no-improvement theorem (11.2): fixed-order,
endpoint-normalized rational filters reorganize the local pole germ but do
not attenuate a fixed zeta-zero mode at leading order.  Endpoint-flat filters
evade that narrow statement by a factor `epsilon^r`.  Their inverse pays the
matching differentiating loss `epsilon^(-r)` when reconstructing the original
observable, but a direct Landau argument on the filtered response does not
perform that inversion and therefore remains logically open.  Compactly supported
filters evade the rational symbol law through their far edge, but the edge
profile is precisely a Volterra transform of the still-uncontrolled
discrepancy tail.

The compact far-edge asymptotic is sectorial.  A sequence of zeros capable of
defeating every fixed strip approaches an imaginary/Stokes direction after
the `1/epsilon` rescaling, where both compact-kernel endpoints contribute and
may interfere.  No uniform high-height amplification follows from the
negative-ray formula alone.

Accordingly, **within this calculus**, the best next target is not a
still-higher pole killer.  The genuine open edges are: a fixed-`epsilon`
eventual one-sided `O(exp(eta*t))` envelope theorem for a rational
endpoint-flat or compact response, with multiplier noncancellation; or
global/vertically translated germ
propagation.  If one tries to derive the compact response's fixed-`epsilon`
sign from the far-edge limit, that derivation additionally needs a uniform
vertical/Stokes two-parameter estimate and Tauberian stability.  Those are
not assumptions of direct Landau once the envelope theorem is independently
known.  Any successful version must use explicit prime-specific input absent
from generic Mellin-pole models.  Globally, this calculus does not displace
the independent QP/Turan locks or the Weil adjacent-support edge, and no
unique best route is established.

Durable status: RH open; uniform strip open; the sharp four-cycle bound open
and not a direct gate to this calculus.
