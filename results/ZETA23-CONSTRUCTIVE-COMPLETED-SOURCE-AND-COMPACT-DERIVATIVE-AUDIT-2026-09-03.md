# Constructive completed-source search and compact derivative audit

Date: 2026-09-03.

Status: the requested construction was attempted directly.  We obtained an
explicit inverse-free completed-source *candidate hierarchy*, its exact
uncancelled remainder, a finite-state obstruction, and an exact four-Cauchy
continuum grammar which remains credible.  We did **not** obtain an operator
`T^src` satisfying `Gamma=T^src A`, a uniform zero-free strip, or RH.

Novelty status: **IMPORTED + LOCAL_PREDECESSOR + PROJECT_SYNTHESIS**.  No claim
below is labeled `CANDIDATE_NEW`.

## 1. Passport and typing

Work in one fixed outer form Hilbert space.  With `V_a` the old space and
`W_(a,b)` its collar, write

\[
 K_a=P_a^hG|_{V_a},\qquad A_a=I+K_a,\qquad
 \Gamma_{a,b}=P_{W_{a,b}}^hG|_{V_a}.                 \tag{1.1}
\]

Thus `A_a:V_a -> V_a` and `Gamma_(a,b):V_a -> W_(a,b)`.  The target is a
displayed operator `T^src_(a,b):V_a -> W_(a,b)` such that

\[
 \Gamma_{a,b}=T^{\rm src}_{a,b}A_a,                  \tag{1.2}
\]

constructed without `A_a^{-1}`, a pseudoinverse, KNC, later positivity, RH,
or a topology chosen to make division bounded.  A core formula counts only
with independently proved boundedness or closability.

The preflight and allowed operation grammar are recorded in
[`zeta23_completed_source_constructive_search_preflight_v1.json`](context/zeta23_completed_source_constructive_search_preflight_v1.json).

## 2. The canonical finite source word and its exact remainder

For every integer `m>=1`, the most direct inverse-free completed-source word
is

\[
 T_m=\Gamma_{a,b}\sum_{j=0}^{m-1}(-K_a)^j.           \tag{2.1}
\]

It uses only the completed source and support projections.  Finite geometric
division gives the exact identity

\[
 \boxed{\Gamma_{a,b}=T_mA_a+\Gamma_{a,b}(-K_a)^m.}   \tag{2.2}
\]

At a contact `A_an=0`, one has `K_an=-n`; consequently

\[
 \Gamma_{a,b}(-K_a)^mn=\Gamma_{a,b}n               \tag{2.3}
\]

for every finite depth.  Iteration does not make the dangerous charge small:
it returns the entire charge.

More generally, a regular commuting candidate `T=Gamma p(K_a)` has residual

\[
 \Gamma\{1-(1+K_a)p(K_a)\}.                         \tag{2.4}
\]

At the contact spectral value `K=-1`, the multiplier in braces equals one
for every polynomial, or every scalar functional calculus regular there.
The scalar function which removes it is `1/(1+z)`, precisely the forbidden
inverse.  This prunes the regular commuting/Krylov hierarchy, not
boundary-localized identities among the separate pole, Lerch, and
prime-dilation pieces.

## 3. Why the xi annihilator does not divide the charge

Let `S=-g''*` be the completed source and `M=eta'*` Suzuki's mean-periodic
annihilator.  The unconditional global identity gives

\[
 MS=0.                                                \tag{3.1}
\]

Splitting the source output into its old and full-exterior parts yields

\[
 M\Gamma_{\rm ext}\phi=-ME_aA_{\rm dist}\phi.       \tag{3.2}
\]

For any regular convolution parametrix `L`, this becomes only

\[
 \Gamma_{\rm ext}
 =-LME_aA_{\rm dist}+(I-LM)\Gamma_{\rm ext}.         \tag{3.3}
\]

The Fourier multiplier of `eta'` is proportional to
`z xi(1/2-iz)`.  Hence `1-LM` equals the identity at every xi zero whenever
`L` is regular.  Killing this remainder requires `1/xi`-type poles and imports
the divisor that the construction was supposed to prove.  Restricting (3.2)
to a collar adds a far-exterior remainder because `eta'` is bilateral and
noncompactly supported.  At contact, (3.2) says only
`M Gamma_ext n=0`, not `Gamma_ext n=0`.

This logical gap is real even in three dimensions.  On `R^3`, set

\[
 S(x,y,z)=(y,x+z,y),\qquad P(x,y,z)=(x,0,0),          \tag{3.4}
\]

and let `M` project onto `span(1,0,-1)`.  Then `MS=0` and `PSP=0`, while

\[
 (I-P)SP(1,0,0)=(0,1,0)\ne0.                         \tag{3.5}
\]

Thus an annihilator identity plus the old equation does not generically
propagate vanishing.

## 4. What finite/local grammars are actually ruled out

Suzuki's current expansion, on a prime-free edge interval, is

\[
 g(t)=\tfrac12|t|\log|t|+A|t|+r(t),\qquad r\in C^2,
                                                               \tag{4.1}
\]

so for `t>0`

\[
 g'(t)=\tfrac12\log t+(A+\tfrac12)+O(t),\qquad
 g''(t)=\frac1{2t}+O(1).                               \tag{4.2}
\]

A purely local differential operator cannot move zero-extended old data into
an open collar.  A finite-rank scalar boundary-state/sampler/jet model also
cannot reproduce the near-edge Hankel family `g''(r+s)`: for any distinct
positive `x_i,y_j`,

\[
 \det[g''(\varepsilon(x_i+y_j))]_{i,j=1}^N
 =(2\varepsilon)^{-N}
   \det[(x_i+y_j)^{-1}]_{i,j=1}^N+O(\varepsilon^{-N+1}),          \tag{4.3}
\]

and the Cauchy determinant is nonzero.  For example, for
`x=(1,2,3,4)`, `y=(5,6,7,8)`, it is exactly
`1/9958443264000`.  Hence the actual near-edge kernel has arbitrarily large
rank.  Equivalently, the imported continuous Kronecker theorem says a
finite-rank Hankel kernel must be exponential-polynomial, which a logarithmic
edge is not.

The scope matters.  Equation (4.3) rules out finite-rank scalar interface
state.  It does not rule out continuum integration, distributed memory,
matrix Riemann--Hilbert systems, or every possible finite composition which
uses source translations.  Full exterior rows can also meet finitely many
prime interfaces, so a claim that they are globally smooth would be false.

Mean-periodicity is not a Volterra substitute.  If `U=0` on `(-a,a)`, then at
`x=a+r` the equation `U*eta'=0` contains both the unknown right future and the
unknown left exterior.  The smooth bilateral kernel has no delta pivot.
Truncation gives an approximation, whereas a contact needs exact zero.

## 5. The exact continuum grammar which survives

The logarithmic obstruction does not merely say “use an infinite operator.”
The archimedean term has a concrete four-channel Cauchy form.  For `t>0`, put

\[
 L(t)=e^{-t/2}\Phi(e^{-2t},1,\tfrac14),\quad
 x=e^{-t/2},\quad q=e^{t/2}.                            \tag{5.1}
\]

Termwise summation gives

\[
 L(t)=4\sum_{n\ge0}\frac{x^{4n+1}}{4n+1}
 =\log\frac{1+x}{1-x}+2\arctan x,                     \tag{5.2}
\]

and therefore

\[
 L'(t)=-\frac12\sum_{\zeta^4=1}\frac1{q-\zeta}.
                                                               \tag{5.3}
\]

The Lerch part of `g'` is `-L/2`.  With `X=e^(x/2)` and
`Y=e^(y/2)`, its off-diagonal contribution to `g''(x-y)`, for `x>y`, is

\[
\boxed{\frac{Y}{4}\sum_{\zeta^4=1}\frac1{X-\zeta Y}.}        \tag{5.4}
\]

At the diagonal this must be read as a finite-part distribution.  If
`F_2(t)=e^(-t/2)Phi(e^(-2t),2,1/4)`, then `F_2'=-2L` and

\[
 \langle g_L'',\varphi\rangle
 =\lim_{\varepsilon\downarrow0}\left[
 \int_{|t|>\varepsilon}\frac{e^{3|t|/2}}{e^{2|t|}-1}\varphi(t)\,dt
 -L(\varepsilon)\varphi(0)\right].                    \tag{5.5}
\]

Thus the diagonal counterterm cannot be discarded when turning (5.4) into
an operator.

The other continuous exponential terms have rank two; the diagonal
`|t|` term supplies a local distribution; and every prime ramp differentiates
to the dilation atoms `X=sqrt(m)Y` and `Y=sqrt(m)X`, with weight
`Lambda(m)/sqrt(m)`.  Thus a serious direct construction must retain:

- all four root-of-unity Cauchy channels;
- the diagonal and rank-two completion data;
- every active prime-power dilation; and
- both interval boundaries.

This gives a completely explicit exterior source normal form.  Put

\[
 J_a=(\alpha,\beta)=(e^{-a/2},e^{a/2}),\quad
 f(Y)=n(2\log Y),\quad
 C_f(z)=\frac1{2\pi i}\int_\alpha^\beta\frac{f(Y)}{Y-z}\,dY,  \tag{5.6}
\]

and `M_minus=integral e^(-y/2)n(y)dy`,
`M_plus=integral e^(y/2)n(y)dy`.  For `X>beta`, the full distributional
source `A_full=-g''*` is

\[
\begin{aligned}
 A_{\rm full}n(2\log X)
 ={}&XM_-+X^{-1}M_+\\
 &-\sum_{m:\,X/\sqrt m\in J_a}\frac{\Lambda(m)}{\sqrt m}
       f(X/\sqrt m)\\
 &+\pi i\sum_{\zeta^4=1}\zeta^{-1}C_f(\zeta^{-1}X).
\end{aligned}                                                    \tag{5.7}
\]

The reflected formula gives the left exterior.  In derivative coordinates,
`H_n'=-i A_full n`; integrating (5.7) from the old boundary and projecting
off the outer constant gives the previously certified collar charge
`Gamma_(a,b)n`.  This is the explicit completed pole--Lerch--prime source we
were looking for at the *normal-form* level.

This is an explicit inverse-free *grammar*, not yet an operator satisfying
(1.2).  The Cauchy transform has Plemelj jump `C_(f,+)-C_(f,-)=f`.  Its
homogeneous triangular lift has jump

\[
 \begin{pmatrix}1&f\\0&1\end{pmatrix},\qquad\det=1,             \tag{5.8}
\]

and the four rotated local jumps also have determinant one.  This proves
pointwise invertibility of the displayed triangular jumps, not Fredholmness
or global propagation: the completed old equation couples
the traces by the prime dilations, so the full problem is operator-valued and
nonlocal.

Let `U n` denote the admissible Cauchy state and write

\[
 \mathcal B_a\mathcal U n=A_an,\qquad
 \mathcal E_{a,b}\mathcal U n=\Gamma_{a,b}n.                    \tag{5.9}
\]

Defining an exterior readout by “choose `F` with `B_a F=h` and return
`E_(a,b)F`” is independent of the chosen solution if and only if

\[
 \mathcal E_{a,b}\ker\mathcal B_a=0,                            \tag{5.10}
\]

which on the genuine state range is exactly
`Gamma_(a,b)(ker A_a)=0`: KNC.

More explicitly, any local parametrix `P` has residual
`R=I-P B_a` in the Cauchy-state notation.  Its finite reconstruction
hierarchy obeys

\[
 T_m^{P}=\mathcal E_{a,b}\sum_{j=0}^{m-1}R^jP,\qquad
 \boxed{\mathcal E_{a,b}-T_m^{P}\mathcal B_a
       =\mathcal E_{a,b}R^m.}                                  \tag{5.11}
\]

On a homogeneous state `F=U n` with `A_an=0`, `RF=F`; the remainder in
(5.11) is the entire charge `Gamma_(a,b)n` at every depth.  Thus the local
jump determinant is harmless, while the global operator has a homogeneous
state at contact and removability of its exterior readout is precisely KNC.
No Fredholm determinant for this state system is asserted here.  Replacing
the remainder by a global inverse would merely rename the target.

Accordingly the direct lane was narrowed to constructing the full
Cauchy--dilation jump system and computing its global compatibility remainder.
R185 computed the exterior-source half: rotations and positive dilations
commute before localization and one pole mode cancels on each side.  It did
not use the homogeneous old equation, whose Lerch part is a split
finite-part/Carleman operator, so the global compatibility system and its
form-domain state adapter remain open.  Only the particular scalar
root--dilation noncommutativity mechanism is parked.

## 6. A compact scalar coordinate for the uniform strip

The parallel strip lane admits a cleaner exact coordinate.  Fix a real
compact profile `W`, set `h(v)=e^(-v/2)W(v)`, and define

\[
 D_W(t)=\sum_{n\ge2}\Lambda(n)n^{-1/2}W(t-\log n)
        -e^{t/2}\widehat W(1/2),                       \tag{6.1}
\]

\[
 S_h(t)=\sum_{n\ge2}\frac{\Lambda(n)}n h'(t-\log n).  \tag{6.2}
\]

Since `widehat W(1/2)=integral h`, locally finite differentiation gives the
exact source-preserving bridge

\[
 \boxed{S_h(t)=e^{-t/2}(\partial_t-\tfrac12)D_W(t).}   \tag{6.3}
\]

For `0<delta<1/2`, `alpha=1-delta`, and
`V_delta(v)=e^(delta v)h(v)`, the shifted completed sum

\[
 G_{\delta,V}(t)=\sum\Lambda(n)n^{-\alpha}
 V_\delta(t-\log n)-e^{\delta t}\widehat V_\delta(\delta)
                                                               \tag{6.4}
\]

satisfies

\[
 \boxed{(\partial_t-\delta)G_{\delta,V}(t)=e^{\delta t}S_h(t).} \tag{6.5}
\]

Let `F(s)=-zeta'(s)/zeta(s)-1/(s-1)` and let
`b_(delta,r)` be the causal pole-killed ramp with

\[
 \mathcal Lb_{\delta,r}(q)=
 \frac{q-\delta}{q(q+r)}F(\alpha+q).                  \tag{6.6}
\]

In the standard whole-line distribution convention the exact bridge is

\[
 \boxed{V_\delta*\partial(\partial+r)(Hb_{\delta,r})
       =e^{\delta t}S_h-V_\delta.}                    \tag{6.7}
\]

The previously tempting formula without `-V_delta` drops the causal boundary
impulse.  It is valid only in an open-half-line convention which absorbs that
impulse, or pointwise after the fixed support collar of `V_delta`.

With the bilateral convention `widehat h(s)=integral h(u)e^(-su)du`, the
transform is

\[
 \mathcal LS_h(s)=\widehat h(s)+s\widehat h(s)F(1+s). \tag{6.8}
\]

Thus `s widehat h(s)F(1+s)` is the transform of `S_h-h`, not literally of
`S_h`; on a tail the discrepancy is an entire initial-collar term.

### Strip-calibrated one-sided theorem

Fix `0<theta<1/2`.  Assume `h` is real and sufficiently smooth that the
explicit zero sum is absolutely convergent (for example a compact spline
with transform decay `O((1+|tau|)^(-A))`, `A>2`), and assume

\[
 \widehat h(\rho-1)\ne0\quad
 \text{whenever }\Re\rho>1-\theta.                    \tag{6.9}
\]

It is enough to choose `W` whose bilateral transform has zeros only on
`Re z=0`, since `widehat h(s)=widehat W(s+1/2)`.  If one sign
`epsilon_0 in {+1,-1}` and fixed constants `C,T` obey

\[
 \boxed{\epsilon_0S_h(t)\ge-Ce^{-\theta t}
        \quad(t\ge T),}                               \tag{6.10}
\]

then every nontrivial zero satisfies `Re rho<=1-theta`.  Indeed,
`epsilon_0S_h+Ce^(-theta t)` is nonnegative on the tail.  Landau's theorem
forces its Laplace convergence abscissa to be a real singularity; the
pole-centered continuation is regular at every real point greater than
`-theta`, while a forbidden zero would give an uncancelled nonreal pole at
`s=rho-1`.  Hence the convergence abscissa is at most `-theta`, excluding
such a pole.

Conversely, under the stated zero-sum decay, `Re rho<=1-theta` gives

\[
 |S_h(t)|\ll_h e^{-\theta t}.                          \tag{6.11}
\]

For a generic `C_c^1` profile the lossless converse is not licensed; extra
smoothing or an epsilon/logarithmic loss is required.  The sign in (6.10)
must be chosen once globally, not separately by block or sample.

Equations (6.3) and (6.11) give `D_W(t)=O(e^((1/2-theta)t))`, hence the R71
energy exponent `1-2theta`.  Therefore (6.10) is a cheap scalar falsifier and
an exact strip-strength endpoint coordinate.  It is not an easier contraction
lemma.  The complete R71 energy remains the better discovery surface because
it retains quadratic structure; further fixed-filter optimization is pruned.

## 7. Literature and novelty firewall

The completed screw kernel and localized operator are imported from Suzuki;
mean-periodicity is imported from Suzuki and from Fesenko--Ricotta--Suzuki.
The finite-rank Hankel classification is classical Kronecker theory.  The
compact one-sided criterion is a Landau/Pintz-type consequence and is closely
overlapped by Suzuki's eventual-sign shifted-`Psi` criterion and Han's smooth
weighted PNT/zero-free-region results.  The four-Cauchy rewrite is elementary
algebra applied to Suzuki's Lerch term.

The dated formula-level search is recorded in
[`zeta23_completed_source_constructive_literature_search_2026-09-03.json`](context/zeta23_completed_source_constructive_literature_search_2026-09-03.json).
No indexed source in that bounded search displayed (1.2), but this is not
evidence of absence from private, unpublished, unindexed, or differently
phrased work.

## 8. Decision-tree update

The following branches are now pruned at their stated scope:

1. finite regular polynomial/Krylov source iteration;
2. a regular xi-annihilator parametrix;
3. purely local differential transport into the collar;
4. finite-rank scalar boundary-state compression of the logarithmic edge;
5. bilateral mean-periodicity treated as a Volterra recurrence; and
6. the collar-free causal ramp identity.

Two branches survive:

1. **Direct RH (historical R184 next test):** the continuum four-Cauchy plus
   exact prime-dilation system.  R185 subsequently found globally commuting
   scale covariance and computed both exterior readouts, but did not serialize
   the split old operator or test those readouts on its homogeneous kernel.
2. **Uniform strip:** a new arithmetic argument proving either the complete
   R71 power bound or the globally oriented compact-source inequality
   (6.10).  These are endpoint-strength statements; no current estimate
   establishes them.

The first item was the prescribed next calculation when this report was
written.  R185 showed that its proposed scalar root--dilation mixing is absent
but did not complete orientation-sensitive global compatibility.  The strip
lane remains the primary route and should use `S_h` as a
normalization/falsification coordinate while seeking structure in the complete
energy; the direct lane retains the explicit split-Carleman and domain-adapter
debts.

## 9. Formal and executable scope

[`CompletedSourceConstructiveSearch.lean`](../lean/rhbridge/RHBridge/CompletedSourceConstructiveSearch.lean)
kernel-checks geometric division, persistence of contact charge, regular
parametrix residual, the paired four-Cauchy rational identity, and the
three-dimensional annihilator countermodel.
[`CompactSourceDerivativeBridge.lean`](../lean/rhbridge/RHBridge/CompactSourceDerivativeBridge.lean)
checks the finite derivative/multiplier algebra and the causal collar sign.
Neither file formalizes Suzuki's analytic kernel, Landau's theorem, a strip,
or RH.

[`completed_source_constructive_search.py`](../src/completed_source_constructive_search.py)
replays the same finite identities over exact rationals, including arbitrary
Cauchy determinant ranks.  These fixtures test formulas and scope; they are
not numerical evidence for the missing asymptotic estimate.
