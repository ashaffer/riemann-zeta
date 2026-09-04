# Singular weighted common-regulator anomaly theorem

Date: 2026-09-01

## Status

This note proves a general common-regulator theorem for Hardy projection
defects with singular phase points.  Heat is one member of a larger regulator
class: uniformly `L1`-bounded trace-class convolution approximate identities
with absolute tails tending to zero all give the same interior total pairing.
The kernels may be signed or complex.  Spectral positivity is needed only
when one additionally wants a common square-root sandwich.  The note also
identifies the boundary anomaly that can appear when the test weight does not
vanish at a phase jump.

The theorem rigorously validates the **total** heat-regularized semilocal Weil
trace used in the zeta project.  It does not prove convergence of the four
Hardy block traces separately, a Ward inequality, a zero-free strip, or RH.

Claim status: project-proved analytic theorem, unrefereed.  Literature-level
novelty has not been established.

## 1. Setup

Put normalized measure `dmu(theta)=dtheta/(2 pi)` on the circle.  Let

\[
 Pe_n=\mathbf 1_{n\le0}e_n,
 \qquad Ne_n=ne_n,
 \qquad R_\epsilon=e^{-\epsilon N^2/2}.              \tag{1.1}
\]

For a measurable unimodular phase `u`, let `U=M_u` and

\[
 D_u=P-U^*PU.                                        \tag{1.2}
\]

The singular statements below take `Sigma` to be a nonempty finite subset of
the circle.  If `Sigma` is empty, assume instead that `u` is globally `C1`
(or use the corresponding global Sobolev hypotheses); that is the separate
ordinary nonsingular approximate-identity theorem.  For nonempty `Sigma`,
write

\[
 \delta(x)=\operatorname{dist}(x,\Sigma).
\]

Assume that `u` is `C^1` off `Sigma`.  Define the local derivative envelope

\[
 \Lambda_u(x)=
 \sup_{d(x,y)<\delta(x)/2}|u'(y)|.                  \tag{1.3}
\]

## 2. Main theorem

### Theorem 1: weighted punctured-circle heat recovery

Let `g` be bounded and suppose

\[
 |g(x)|\bigl(1+\Lambda_u(x)+\delta(x)^{-1}\bigr)
 \in L^1(\mathbb T).                                \tag{2.1}
\]

Then `R_epsilon M_g D_u R_epsilon` is trace class for every
`epsilon>0`, the weighted phase derivative is integrable, and

\[
 \boxed{
 \lim_{\epsilon\downarrow0}
 \operatorname{Tr}\bigl(R_\epsilon M_gD_uR_\epsilon\bigr)
 =\int_{\mathbb T}g(x)(-i\overline{u(x)}u'(x))\,d\mu(x).
 }                                                   \tag{2.2}
\]

No one-sided trace of `P` is taken, and no cyclicity is applied after
removing the common heat factors.

### Theorem 2: universality over absolute-tail common regulators

Let `T_epsilon` be convolution by a possibly signed or complex kernel
`h_epsilon` on the circle.  Assume

1. `T_epsilon` is trace class;
2. `integral h_epsilon dmu=1` and
   `sup_epsilon ||h_epsilon||_1<infinity`;
3. for every `eta>0`, the **absolute** tail obeys
   \[
   \int_{d(r,0)>\eta}|h_\epsilon(r)|\,d\mu(r)
   \longrightarrow0.                               \tag{2.3}
   \]

Under (2.1),

\[
 \boxed{
 \lim_{\epsilon\downarrow0}
 \operatorname{Tr}(T_\epsilon M_gD_u)
 =\int_{\mathbb T}g(-i\overline u u')\,d\mu.
 }                                                   \tag{2.4}
\]

If, in addition, `T_epsilon` is a positive operator and
`R_epsilon=T_epsilon^(1/2)`, then `R_epsilon` is Hilbert--Schmidt and

\[
 \operatorname{Tr}(R_\epsilon M_gD_uR_\epsilon)
 =\operatorname{Tr}(T_\epsilon M_gD_u),             \tag{2.5}
\]

so (2.4) is a genuine common two-sided regulator theorem.  Circle heat,
Poisson/Abel, and Fejer convolution operators satisfy these assumptions.
The conclusion is regulator independence of the **total** pairing within
this class; it says nothing about the four signed Hardy blocks separately.

Proof.  In the proof below replace the heat kernel `H_epsilon` by
`h_epsilon`.  The uniform `L1` bound, applied to the absolute value of the
kernel, gives (3.8) with a fixed extra constant.  Unit mass and the absolute
tail condition give convergence to the removable diagonal at every
nonsingular point: on a small neighborhood use continuity of the filled-in
kernel, and on its complement use (2.3).  Dominated convergence using (2.1)
proves (2.4).  For completeness, the kernel trace identity follows by Fourier
truncation: a trace-class convolution operator has summable Fourier
multipliers, so its finite Fourier truncations converge in trace norm and
their kernels converge uniformly.  The finite-rank trace identities therefore
pass to the operator trace, while the kernel integrals pass to the limit by
the domination (2.1).  Under the additional spectral-positivity hypothesis,
the operator has a
Hilbert--Schmidt square root and Hilbert--Schmidt cyclicity gives (2.5).  No
Gaussian estimate, pointwise positivity, or evenness is used for the interior
limit.  Uniform `L1` control is substantive: sign-changing Dirichlet kernels
with diverging `L1` norm are not covered.

### Closed-null-set extension

The same conclusion holds when `Sigma` is any nonempty closed null set, `u`
is locally `W^{1,infinity}` on its complement, and `Lambda_u` is the
corresponding local essential derivative envelope.  The empty set is the
nonsingular case already separated above.  The diagonal formula then holds
almost everywhere off `Sigma`.  Approximate-identity convergence at its
Lebesgue points, the fact that `Sigma` is null, and the same domination (2.1)
prove the claim.  Finiteness is used below only to write the boundary
contribution as a finite sum of jumps.

### Power-law corollary and null-set thickness

Suppose near `Sigma` that

\[
 |u'(x)|\le C\delta(x)^{-\alpha}
   \bigl(1+|\log\delta(x)|\bigr)^k,
 \qquad
 |g(x)|\le C_g\delta(x)^\beta,                      \tag{2.6}
\]

with `alpha,k>=0`.  If `Sigma` is finite, condition (2.1) follows whenever

\[
 \boxed{\beta>\max(\alpha-1,0).}                    \tag{2.7}
\]

The extra requirement `beta>0` cannot be deleted from a phase-uniform
statement: some unmatched one-sided phase limits produce nonzero boundary
flux when the weight does not vanish.

For a general closed null set, nullity alone does **not** imply (2.7): its
metric neighborhoods can shrink more slowly than every power.  Suppose
instead that for some `kappa in (0,1]` and all sufficiently small `r`,

\[
 \mu\{x:\delta(x)<r\}\le C_\Sigma r^\kappa.        \tag{2.8}
\]

Then the sufficient threshold is

\[
 \boxed{\beta>\max(\alpha-\kappa,1-\kappa).}        \tag{2.9}
\]

Indeed, a dyadic-shell sum shows that
`delta^p(1+|log delta|)^k` is integrable whenever `p>-kappa`.
Apply this with `p=beta-alpha` and `p=beta-1`.  A finite set has
`kappa=1`, recovering (2.7).  Without either finiteness or a quantified
neighborhood bound such as (2.8), the primary domination hypothesis (2.1),
not a power-only shortcut, is the valid statement.

## 3. Proof

The lower Hardy distribution is

\[
 p_-(r)=\sum_{n\le0}e^{inr}
 =\frac12\delta_{\mathbb T}(r)+\frac12
  -\frac{i}{2}\operatorname{PV}\cot(r/2).           \tag{3.1}
\]

Away from the punctures, the kernel of (1.2) is

\[
 K_u(x,y)=p_-(x-y)
          \bigl(1-\overline{u(x)}u(y)\bigr).         \tag{3.2}
\]

The delta term vanishes because the second factor is zero on the diagonal.
For fixed nonsingular `x`, the remaining quotient extends continuously to

\[
 K_u(x,x)=-i\overline{u(x)}u'(x).                   \tag{3.3}
\]

Let

\[
 H_\epsilon(r)=\sum_{n\in\mathbb Z}e^{-\epsilon n^2}e^{inr}
\]

be the normalized circle heat approximate identity.  Since `R_epsilon` is
trace class and `M_gD_u` is bounded, fixed-`epsilon` cyclicity is legal and

\[
 \operatorname{Tr}(R_\epsilon M_gD_uR_\epsilon)
 =\operatorname{Tr}(R_\epsilon^2M_gD_u).             \tag{3.4}
\]

Kernel composition expresses (3.4) as

\[
 \int g(x)A_\epsilon(x)\,d\mu(x),
 \qquad
 A_\epsilon(x)=
 \int H_\epsilon(y-x)K_u(x,y)\,d\mu(y).             \tag{3.5}
\]

Split the inner integral into

\[
 d(x,y)<\delta(x)/2
 \quad\hbox{and}\quad
 d(x,y)\ge\delta(x)/2.
\]

On the first region the connecting arc avoids `Sigma`.  The mean-value bound
and the first-order Hardy singularity give

\[
 |K_u(x,y)|\le C(1+\Lambda_u(x)).                    \tag{3.6}
\]

On the complement, use `|1-conj(u(x))u(y)|<=2` and
`|p_-(x-y)|<=C(1+d(x,y)^{-1})` to obtain

\[
 |K_u(x,y)|\le C(1+\delta(x)^{-1}).                 \tag{3.7}
\]

Positivity and unit mass of `H_epsilon` yield the uniform domination

\[
 |A_\epsilon(x)|
 \le C\bigl(1+\Lambda_u(x)+\delta(x)^{-1}\bigr).    \tag{3.8}
\]

For every nonsingular `x`, the heat approximate identity and (3.3) give

\[
 A_\epsilon(x)\longrightarrow-i\overline u(x)u'(x).
\]

Condition (2.1) and dominated convergence prove (2.2).  The same bound
shows absolute integrability of every displayed kernel composition.  For
finite `Sigma`, (2.7) is precisely the pair of one-dimensional integrability
conditions

\[
 \beta-\alpha>-1,
 \qquad \beta-1>-1.
\]

## 4. Sharp boundary anomaly

The condition `beta>0` cannot simply be dropped from a phase-uniform theorem.
On `(0,2 pi)` let

\[
 u(\theta)=e^{ic\theta},\qquad g=1,
\]

where, for a nonzero-flux witness, `c` is not in `(1/2)Z` (for example
`c=1/4`).  The interior phase derivative is `c`, but

\[
 \lim_{\epsilon\downarrow0}
 \operatorname{Tr}(R_\epsilon D_uR_\epsilon)
 =c-\frac{\sin(2\pi c)}{2\pi}.                      \tag{4.1}
\]

The second term is flux across the circular cut.

More generally, suppose at one puncture that `u` is piecewise `C1` up to the
puncture and that bounded `g` is piecewise continuous up to it, with one-sided
limits `u_+,u_-` and `g_+,g_-`.  For every **even** normalized uniformly-`L1`
absolute-tail kernel whose convolution operator is trace class, the additional
boundary contribution is

\[
 \boxed{
 \mathcal B=\frac1{4\pi}
 \left[-ig_+(1-\overline{u_+}u_-)
       +ig_-(1-\overline{u_-}u_+)\right].
 }                                                   \tag{4.2}
\]

For continuous `g`,

\[
 \mathcal B=-\frac{g(0)}{2\pi}
             \Im(\overline{u_+}u_-).                \tag{4.3}
\]

It vanishes when the phase traces match or the weight vanishes at the
puncture.  More generally, in the convolution orientation of (3.5), suppose

\[
 m_\pm=\lim_{\epsilon\downarrow0}
 \int_{\{0<\pm r<\pi\}}h_\epsilon(r)\,d\mu(r),
 \qquad m_++m_-=1.
\]

Then the asymmetric boundary term is

\[
 {1\over2\pi}\left[
 -i m_-g_+(1-\overline{u_+}u_-)
 +i m_+g_-(1-\overline{u_-}u_+)
 \right].                                           \tag{4.2a}
\]

The even case has `m_+=m_-=1/2` and recovers (4.2).  Formula (4.2) follows
from the regulator-independent concentration identity

\[
 \frac1{(2\pi)^2}\int_{0<a,b<r_0}
 \frac{h_\epsilon(a+b)}{a+b}\,da\,db
 \longrightarrow\frac1{4\pi}.                      \tag{4.4}
\]

Here `r_0` is any fixed number in `(0,pi/2)`.  After putting `r=a+b`, the
inner segment has length `r` for `0<r<r_0`; the remaining part lies in the
absolute tail.  Evenness and unit mass leave one half of the concentrated
mass.  The error is controlled by the uniform `L1` bound and absolute tails.
Without convergence of the one-sided masses, only subsequential boundary
formulas, and possibly no full trace limit, are asserted.  Evenness is a
sufficient symmetry; the exact coefficient condition is the balanced limit
`m_+=m_-=1/2`.  Summing (4.2) gives the formula for finitely many
piecewise-`C1` jumps.

This boundary term is the continuum analogue of the finite boundary-defect
account in the anomaly-budget identity.

## 5. Semilocal zeta corollary

Let

\[
 u_F(t)=\rho_\infty(1/2+it)\rho_2(1/2+it)
        \rho_3(1/2+it)\rho_5(1/2+it)
\]

and define

\[
 m_F(t)=-i\overline{u_F(t)}u_F'(t).
\]

Use the Cayley coordinate

\[
 t=-\cot(\theta/2).
\]

The pole-free Weil multiplier obeys

\[
 -i\overline{u_F(t)}u_F'(t)=O(\log(2+|t|)),          \tag{5.1}
\]

while

\[
 \frac{dt}{d\theta}=\frac{1+t^2}{2}.
\]

Thus the Cayley phase satisfies

\[
 |\partial_\theta u_F|=O\!\left(
 |\theta|^{-2}\log(1/|\theta|)\right),              \tag{5.2}
\]

so `(alpha,k)=(2,1)`.

For a unit triangular hat of center `c` and half-width `d`,

\[
 \widehat\phi_{c,d}(t)
 =d e^{-ict}\operatorname{sinc}^2(td/2)=O(t^{-2}).  \tag{5.3}
\]

Hence, when `v` and `w` are triangular hats or elements of their finite
linear span (and likewise for any separately stated smooth class with this
pointwise Fourier decay),

\[
 g(\theta)=\widehat v(t(\theta))
             \overline{\widehat w(t(\theta))}
 =O(|\theta|^4).                                    \tag{5.4}
\]

Here `beta=4>1=alpha-1`, so Theorem 1 applies with ample reserve.  Changing
variables in (2.2) gives the rigorous identity

\[
 \boxed{
 \lim_{\epsilon\downarrow0}
 \operatorname{Tr}(R_\epsilon M_gD_{u_F}R_\epsilon)
 =\frac1{2\pi}\int_{\mathbb R}
   \widehat v(t)\overline{\widehat w(t)}\,m_F(t)\,dt.
 }                                                   \tag{5.5}
\]

Thus common heat regularization recovers the total semilocal anomaly for this
hat trial class despite the infinitely oscillatory Cayley endpoint.
Individual `c^*c`, cross, and `-b^*b` traces may still diverge or depend on
the common removal prescription; (5.5) does not separate them.  No claim is
made here for arbitrary vectors in the logarithmic form domain: such vectors
need not have pointwise `O(t^-2)` Fourier decay, and extending (5.5) to that
domain would require a separate density and uniform-continuity theorem.

## Claim ledger

- weighted heat recovery (2.2), including the uniformly-`L1` absolute-tail
  and closed-null-set extensions: proved by kernel domination and approximate
  identity;
- threshold (2.7): proved and uniformly sharp at the level `beta=0` because
  some unmatched phase traces have nonzero flux for a nonvanishing weight;
  under (2.8) the correct sufficient threshold is (2.9), while arbitrary
  closed null sets have no power-only corollary;
- boundary flux (4.2): proved for the even absolute-tail regulator class;
  asymmetric limits retain their one-sided-mass coefficients;
- semilocal derivative and weight bounds: exact from the local-factor
  derivative and triangular-hat transform, for the hat trial space;
- common total semilocal trace (5.5): proved on that trial space (or an
  explicitly stated smooth class with the same decay);
- regulator-independent individual Hardy block limits: open;
- Ward positivity, propagation, a uniform strip, and RH: open.
