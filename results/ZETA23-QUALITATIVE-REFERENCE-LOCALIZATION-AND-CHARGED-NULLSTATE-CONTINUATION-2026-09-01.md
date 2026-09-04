# Qualitative reference localization and charged-nullstate continuation

**Date:** 2026-09-01  
**Architecture:** Weil positivity only  
**Status:** abstract/reference theorems proved below; the completed-zeta
charged-nullstate hypothesis is open; global Weil positivity and RH remain
open

## 0. Verdict

The quantitative estimate previously called `NR_log` is not needed for a
qualitative cofinal-continuation argument.  On bounded support intervals, the
log-Bessel reference form has compact embedding.  Monotone convergence of its
nested support domains therefore upgrades to **operator-norm** convergence of
the embedded resolvents.  The exact modulus is

\[
 \|K_{L'}-K_L\|
 =\sup_{0\ne w\in\mathcal V_{L'}\cap\mathcal V_L^{\perp_{\mathfrak h}}}
   \frac{\|w\|_2^2}{\mathfrak h(w,w)},
 \qquad L<L',                                      \tag{0.1}
\]

and it tends to zero uniformly when `L,L'` remain in a compact positive
support slab and `L'-L` tends to zero.

For a completed Weil form

\[
 q=\mathfrak h+r,
\]

the residual `r` is represented by a bounded `L2` operator on every bounded
support slab.  If `q_L` is nonnegative, compact resolvent gives a positive
spectral gap on the orthogonal complement of its finite-dimensional radical.
Consequently every old spectral direction away from the radical already
satisfies the needed Ward estimate.  The only irreducible continuation input
at a singular support is the exact charge cancellation

\[
 r\bigl(\ker q_L,
   \mathcal V_{L'}\cap\mathcal V_L^{\perp_{\mathfrak h}}\bigr)=0. \tag{0.2}
\]

If (0.2) holds along arbitrarily thin right collars at every hypothetical
singular positive support, a maximal-support argument gives cofinal Weil
positivity.  Conversely, any first failure of positivity must occur through a
nonzero radical vector carrying nonzero completed-source boundary charge.

Condition (0.2) has **not** been proved for the Riemann zeta source.  At one
contact it is strictly smaller than a compact-slab, all-vector uniform `HRW`
theorem.  Universally over every semidefinite completed-zeta contact, however,
it is RH-equivalent under the accepted Weil and support-continuity interfaces;
the quantifier collapse is recorded in the dedicated last-mile audit.  Nothing
in this report proves RH or a uniform zero-free strip.

## 1. Theorem passport and preflight

| Field | Value |
|---|---|
| architecture | Weil positivity; no QP/Turan input or conclusion |
| target | qualitative continuation of localized completed Weil positivity |
| first unproved edge | completed-source charge cancellation (0.2) on the radical of a hypothetical first-contact form |
| support convention | `I_L=[-L/4,L/4]`; all spaces are nested by zero extension |
| source | the exact combined completed-zeta archimedean, prime-power, and pole source; no sourcewise absolute values |
| coefficient cone | arbitrary real form-domain vectors, matching the repository; complex Hermitian analogue noted below |
| normalization | repository Fourier and support normalization below |
| quantifier order | on each finite slab first fix one common residual form; then quantify over every support and every old/harmonic-collar vector |
| full-band floor | no old positive floor is assumed at a singular support; the radical is retained exactly |
| resolution | continuum closed-form domains; no Galerkin truncation |
| rate | qualitative modulus `Omega_B(delta)=o(1)`; no claimed `1/log(1/delta)` rate |
| downstream adapter | maximal-support/open--closed continuation of Weil positivity |
| abstract falsifier | the charged `2 by 2` block in Section 8 proves that (0.2) is necessary and not a consequence of compactness or continuity |
| finite evidence | the certified `p=5` result supplies only the initial local seed; it does not establish (0.2) |
| Fejer / pseudo-node tests | not applicable to this Weil-side compact-form theorem; no QP/Turan inference is made |

## 2. Hilbert spaces, support embeddings, and adjoints

Use the Fourier convention

\[
 \widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx,
 \qquad
 \|f\|_2^2=\frac1{2\pi}\int_{\mathbb R}|\widehat f(t)|^2\,dt.
\]

The physical Hilbert spaces and forms below are real, as in
`GeneralZetaWeilForm`; their Fourier transforms are complex-valued.  The
complex Hermitian version is identical after inserting conjugates.  In any
necessity argument, a complex cross coefficient is killed by testing both
real and imaginary scalar phases, not by a single real line.

Fix a finite outer support `B>0`, and put

\[
 I_L=[-L/4,L/4],\qquad H_L=L^2(I_L),\qquad 0<L\le B.
\]

Every element of `H_L` is identified with its zero extension to `I_B`.  The
corresponding isometry and its Hilbert adjoint are

\[
 \iota_L:H_L\longrightarrow H_B,
 \qquad \iota_L^*:H_B\longrightarrow H_L.           \tag{2.1}
\]

Define

\[
 m(t)=\frac12\log(1+4t^2),                            \tag{2.2}
\]

\[
 \mathcal V_B=
 \left\{f\in H_B:
   \frac1{2\pi}\int_{\mathbb R}m(t)|\widehat f(t)|^2\,dt<\infty
 \right\},                                           \tag{2.3}
\]

where functions are Fourier transformed after zero extension to the line.
Give `V_B` the Hilbert inner product

\[
 \mathfrak h(f,g)=\langle f,g\rangle_{H_B}
 +\frac1{2\pi}\int_{\mathbb R}
     m(t)\widehat f(t)\overline{\widehat g(t)}\,dt.   \tag{2.4}
\]

For `0<L<=B`, let

\[
 \mathcal V_L={f\in\mathcal V_B:\operatorname{supp}f\subset I_L\}.
                                                               \tag{2.5}
\]

It will be proved below that this is exactly the `h`-closure of
`C_c^infty(I_L^circ)`.  In particular `V_L` is a closed subspace of `V_B` and
is dense in `H_L`.

Let

\[
 \mathcal J:\mathcal V_B\longrightarrow H_B            \tag{2.6}
\]

be the inclusion.  Its adjoint is always taken with `h` on the source and the
`L2` inner product on the target:

\[
 \mathfrak h(\mathcal J^*F,v)=\langle F,\mathcal Jv\rangle_{H_B}
 \quad(F\in H_B,\ v\in\mathcal V_B).                  \tag{2.7}
\]

Write

\[
 P_L^{\mathfrak h}:\mathcal V_B\longrightarrow\mathcal V_L \tag{2.8}
\]

for the `h`-orthogonal projection.  Finally, let `T_L` be the positive
self-adjoint operator on `H_L` associated with the closed form
`h|_{V_L}`.  Since `h(f,f)>=||f||_2^2`, one has `T_L>=I`, and the embedded
Dirichlet resolvent is

\[
 K_L=\iota_LT_L^{-1}\iota_L^*:H_B\longrightarrow H_B. \tag{2.9}
\]

The definitions give the exact factorization

\[
 \boxed{K_L=\mathcal J P_L^{\mathfrak h}\mathcal J^*.} \tag{2.10}
\]

Indeed, if `u=P_L^h J^*F`, then for every `v in V_L`,

\[
 \mathfrak h(u,v)=\langle F,v\rangle_{H_B}
 =\langle\iota_L^*F,v\rangle_{H_L},
\]

which is the Lax--Milgram characterization of the right side of (2.9).

## 3. Compact embedding and support-domain continuity

### Lemma 3.1 -- compactness of the form embedding

The inclusion `J:V_B->H_B` is compact.

**Proof.**  For `T>0`, let

\[
 A_Tf=1_{I_B}\mathcal F^{-1}
          (1_{[-T,T]}\widehat f).
\]

As an operator from `L2(I_B)` to itself, `A_T` has a square-integrable kernel
on `I_B x I_B`, hence is Hilbert--Schmidt.  On the unit ball of
`(V_B,h)`, Plancherel gives

\[
 \|f-A_Tf\|_{H_B}^2
 \le \frac1{2\pi}\int_{|t|>T}|\widehat f(t)|^2\,dt
 \le \frac{\mathfrak h(f,f)}{1+m(T)}.                \tag{3.1}
\]

Thus `J` is an operator-norm limit of compact maps.  `square`

### Lemma 3.2 -- exact support core

For every `0<L<=B`,

\[
 \mathcal V_L=
 \overline{C_c^\infty(I_L^\circ)}^{\,\mathfrak h}.     \tag{3.2}
\]

**Proof.**  Only the reverse inclusion needs proof.  If `f in V_B` is
supported in `I_L`, define the normalized inward dilation

\[
 D_rf(x)=r^{-1/2}f(x/r),\qquad 0<r<1.                 \tag{3.3}
\]

Its support lies in `I_{rL}` and

\[
 \widehat{D_rf}(t)=r^{1/2}\widehat f(rt).             \tag{3.4}
\]

For `r` in a fixed neighborhood of one, the weight `1+m` obeys

\[
 1+m(t/r)\le C(1+m(t)).                               \tag{3.5}
\]

Dilations are strongly continuous first on compactly supported Fourier data
and then, by (3.5) and density, on `L2((1+m)dt)`.  Hence
`D_rf -> f` in `h` as `r` increases to one.  Each `D_rf` has a positive
support gap from the boundary of `I_L`.  Convolution with a sufficiently
small smooth compactly supported approximate identity preserves that gap and
converges in `h`, because its Fourier multiplier tends pointwise to one and is
uniformly bounded.  This produces the required interior smooth approximants.
`square`

### Lemma 3.3 -- both monotone domain limits

If `L_n` increases to `L`, then

\[
 \overline{\bigcup_n\mathcal V_{L_n}}^{\,\mathfrak h}
 =\mathcal V_L.                                       \tag{3.6}
\]

If `L_n` decreases to `L`, then

\[
 \bigcap_n\mathcal V_{L_n}=\mathcal V_L.             \tag{3.7}
\]

**Proof.**  For (3.6), first inward-dilate an arbitrary element of `V_L` so
that its support lies in some `I_{L_n}`, and then use the mollification in
Lemma 3.2.  For (3.7), an element of the intersection is in `V_B` and its
`L2` support lies in the intersection of the closed intervals, namely `I_L`;
Lemma 3.2 then identifies it as an element of `V_L`.  `square`

## 4. Exact norm-resolvent localization

### Theorem 4.1 -- compact nested-resolvent localization

The map

\[
 (0,B]\ni L\longmapsto K_L\in\mathcal B(H_B)          \tag{4.1}
\]

is operator-norm continuous.  It is uniformly continuous on every compact
positive slab `[a,b] subset (0,B]`.

For `L<L'`, put

\[
 \mathcal W_{L,L'}=
 \mathcal V_{L'}\cap\mathcal V_L^{\perp_{\mathfrak h}}. \tag{4.2}
\]

Then

\[
 P_{\mathcal W_{L,L'}}^{\mathfrak h}
 =P_{L'}^{\mathfrak h}-P_L^{\mathfrak h},             \tag{4.3}
\]

\[
 \boxed{
 K_{L'}-K_L
 =\mathcal J P_{\mathcal W_{L,L'}}^{\mathfrak h}\mathcal J^*
 \succeq0,}                                           \tag{4.4}
\]

and

\[
 \boxed{
 \|K_{L'}-K_L\|
 =\sup_{0\ne w\in\mathcal W_{L,L'}}
     \frac{\|w\|_{H_B}^2}{\mathfrak h(w,w)}.}        \tag{4.5}
\]

When `W_{L,L'}={0}`, the supremum in (4.5) is defined as zero, in agreement
with the norm of the zero operator.

Consequently, for `0<a<b<=B`,

\[
 \Omega_{[a,b]}(\delta)=
 \sup_{\substack{a\le L\le L'\le b\\L'-L\le\delta}}
 \|K_{L'}-K_L\|                                      \tag{4.6}
\]

satisfies

\[
 \Omega_{[a,b]}(\delta)\longrightarrow0
 \quad(\delta\downarrow0),                           \tag{4.7}
\]

and, whenever `a<=L<=L'<=b`, every `w in W_{L,L'}` obeys

\[
 \|w\|_2^2\le
 \Omega_{[a,b]}(L'-L)\mathfrak h(w,w).               \tag{4.8}
\]

**Proof.**  For increasing closed Hilbert subspaces, orthogonal projections
converge strongly to the projection onto the closure of their union; for
decreasing subspaces, they converge strongly to the projection onto their
intersection.  Lemma 3.3 therefore gives

\[
 P_{L_n}^{\mathfrak h}\longrightarrow P_L^{\mathfrak h}
 \quad\hbox{strongly on }\mathcal V_B                 \tag{4.9}
\]

in both monotone directions.  The projections are uniformly bounded and
`J^*` is compact by Lemma 3.1.  Strong convergence is uniform on the compact
image under `J^*` of the unit ball of `H_B`; hence

\[
 \|\mathcal J(P_{L_n}^{\mathfrak h}-P_L^{\mathfrak h})
       \mathcal J^*\|\longrightarrow0.                \tag{4.10}
\]

Together with (2.10), this proves both one-sided limits, hence norm
continuity.  Uniform continuity on `[a,b]` is Heine--Cantor.

Nested orthogonal projections give (4.3), and (4.4) follows from (2.10).  If
`A=J P_W^h`, then the right side of (4.4) is `AA^*`, so its norm is
`||A||^2`.  Projecting an arbitrary form vector onto `W` can only decrease its
`h` norm, and every `w in W` is its own projection.  This proves (4.5), and
(4.6)--(4.8) follow.  `square`

### Quotient and harmonic-lift typing

No multiplication by a sharp collar indicator is needed.  Define the Hilbert
quotient

\[
 \mathcal X_{L,L'}=\mathcal V_{L'}/\mathcal V_L       \tag{4.11}
\]

with the quotient `h` norm.  Let

\[
 J^\mathfrak h_{L,L'}:\mathcal X_{L,L'}
   \longrightarrow\mathcal V_B                       \tag{4.12}
\]

send each class to its unique minimum-`h` representative, viewed by inclusion
in the fixed outer form space.  It is an isometric embedding with range
`W_{L,L'}`, hence unitary onto that range.  If
`pi:V_L'->X_L,L'` is the quotient map, then the adjoint is correctly typed
as a map on `V_B` and

\[
 (J^\mathfrak h_{L,L'})^*=\pi P_{L'}^{\mathfrak h},
 \qquad
 J^\mathfrak h_{L,L'}(J^\mathfrak h_{L,L'})^*
 =P_{\mathcal W_{L,L'}}^{\mathfrak h}.               \tag{4.13}
\]

Here the adjoint is formed with the quotient inner product and `h`.  Thus

\[
 K_{L'}-K_L
 =(\mathcal J J^\mathfrak h_{L,L'})
  (\mathcal J J^\mathfrak h_{L,L'})^*.               \tag{4.14}
\]

If the quotient energy is denoted by
`S(xi)=||xi||_{X_{L,L'}}^2`, (4.8) is exactly the coordinate-free collar
estimate

\[
 (J^\mathfrak h_{L,L'})^*\mathcal J^*\mathcal J
 J^\mathfrak h_{L,L'}\preceq
 \Omega_{[a,b]}(L'-L)I_{X_{L,L'}}.                   \tag{4.15}
\]

Equivalently,
`||mathcal J J^h_{L,L'} xi||_2^2 <= Omega_[a,b](L'-L) S(xi)`.

This is the qualitative theorem `NR_0`.  It does not supply the conjectured
explicit `C/log(e/delta)` rate.

## 5. Two-moment relative spaces: correct ambient typing

Define bounded functionals on `H_B` by

\[
 \ell_\pm(f)=\int_{I_B}f(x)e^{\pm x/2}\,dx,
 \qquad \ell=(\ell_+,\ell_-).                         \tag{5.1}
\]

For each `L`, the correct relative ambient Hilbert space and form domain are

\[
 H_L^{\rm rel}=H_L\cap\ker\ell,
 \qquad
 \mathcal V_L^{\rm rel}=\mathcal V_L\cap\ker\ell.    \tag{5.2}
\]

The form domain in (5.2) is **not** dense in all of `H_L`; it is dense in
`H_L^rel`.  This distinction is required to define its associated operator.
Zero extension gives an isometry

\[
 \iota_L^{\rm rel}:H_L^{\rm rel}\longrightarrow H_B^{\rm rel}. \tag{5.3}
\]

Its Hilbert adjoint need not be raw restriction: it is the relative
orthogonal projection of the restriction.  All relative resolvents below use
this correctly typed adjoint.

Fix a compact positive slab `[a,b]`.  Choose a nonempty open interval
`J_0` compactly contained in `I_a^circ`.  The restrictions of `e^{x/2}` and
`e^{-x/2}` to `J_0` are linearly independent.  Therefore there are
`psi_1,psi_2 in C_c^infty(J_0)` for which

\[
 \left(\ell_i(\psi_j)\right)_{i\in\{+,-\},\,j\in\{1,2\}}
\]

is invertible.  Equivalently, there is a fixed bounded right inverse

\[
 C:\mathbb R^2\longrightarrow C_c^\infty(J_0)
 \subset\mathcal V_a,
 \qquad \ell C=I_{\mathbb R^2}.                      \tag{5.4}
\]

Set

\[
 \Pi=I-C\ell.                                        \tag{5.5}
\]

Then for every `L in [a,b]`,

\[
 \Pi\mathcal V_L\subset\mathcal V_L^{\rm rel},
 \quad \Pi|_{\mathcal V_L^{\rm rel}}=I,
 \quad
 \|\Pi\|_{\mathcal V_B\to\mathcal V_B}
 \le1+\|C\|\,\|\ell\|.                             \tag{5.6}
\]

The support and norm of the corrector are fixed across the entire slab; in
particular they do not deteriorate at prime-activation thresholds.  Such a
uniform fixed corrector is not asserted as `a` tends to zero.

Applying `Pi` to the approximants from Lemma 3.3 proves

\[
 \overline{\bigcup_n\mathcal V_{L_n}^{\rm rel}}^{\,\mathfrak h}
 =\mathcal V_L^{\rm rel}\quad(L_n\uparrow L),         \tag{5.7}
\]

while

\[
 \bigcap_n\mathcal V_{L_n}^{\rm rel}
 =\mathcal V_L^{\rm rel}\quad(L_n\downarrow L)       \tag{5.8}
\]

follows by intersecting (3.7) with `ker ell`.  The same correction argument,
starting from `L2` approximants, proves that `V_L^rel` is dense in
`H_L^rel`.

Let `T_L^rel` be the operator on `H_L^rel` associated with the restricted
form, let

\[
 \mathcal J_{\rm rel}:\mathcal V_B^{\rm rel}
 \longrightarrow H_B^{\rm rel}
\]

be the compact inclusion, and let `P_L^{h,rel}` be the form-orthogonal
projection.  Then

\[
 K_L^{\rm rel}
 =\iota_L^{\rm rel}(T_L^{\rm rel})^{-1}
  (\iota_L^{\rm rel})^*
 =\mathcal J_{\rm rel}P_L^{\mathfrak h,{\rm rel}}
  \mathcal J_{\rm rel}^*.                            \tag{5.9}
\]

The proof of Theorem 4.1 applies verbatim.  Hence the relative resolvents are
norm-continuous, uniformly so on compact positive slabs, and their harmonic
complements satisfy the exact analogue of (4.5).  The previously open
relative localization issue is therefore closed qualitatively; an explicit
rate remains open.

## 6. Bounded completed-Weil residual on a slab

On a fixed finite slab, choose the completed Weil form once on the outer
space and write

\[
 q_B(f,g)=\mathfrak h(f,g)
          +\langle R_Bf,g\rangle_{H_B},               \tag{6.1}
\]

where `R_B=R_B^*` is bounded and

\[
 M_B=\|R_B\|<\infty.                                  \tag{6.2}
\]

For the completed-zeta source, (6.2) is unconditional on each bounded slab:

1. the archimedean multiplier minus (2.2) is bounded on the real frequency
   line;
2. only finitely many prime-power translations can couple two functions
   supported in `I_B`, and each translation is `L2` bounded;
3. the completed pole contribution is finite rank, with its exponential
   moments bounded on `I_B`.

For `L<=B`, define

\[
 q_L=q_B|_{\mathcal V_L\times\mathcal V_L}.           \tag{6.3}
\]

This restriction convention is essential: `q_L` is not rebuilt with a
discontinuously changing active mask.  Since (6.1) is a bounded perturbation
of `h`, it is a closed semibounded form.  After adding
`c_B||f||_2^2` with `c_B>M_B`, it is uniformly coercive and equivalent to
the `h` norm.  Applying Theorem 4.1 with that common shifted slab form shows
that the embedded shifted `q_L` resolvents are also norm-continuous.

If `q_L>=0`, let `A_L` be its nonnegative self-adjoint operator in `H_L` and
put

\[
 \mathcal N_L=\ker A_L
 =\{n\in\mathcal V_L:q_L(n,v)=0\text{ for all }v\in\mathcal V_L\}. \tag{6.4}
\]

Compactness of `V_L->H_L` implies compact resolvent.  Thus `N_L` is finite
dimensional and

\[
 \gamma_L=
 \inf_{\substack{u\in\mathcal V_L\cap\mathcal N_L^{\perp_{H_L}}\\
                   \|u\|_2=1}}
 q_L(u,u)>0.                                         \tag{6.5}
\]

The same statements hold on the correctly typed relative spaces after
compressing the bounded residual form to `H_B^rel`.

## 7. Semidefinite local continuation

### Theorem 7.1 -- charged-nullstate Schur continuation

Let `0<L<L'<=B`, suppose `q_L>=0`, and put

\[
 \mathcal W=\mathcal W_{L,L'},
 \qquad
 \omega=\|K_{L'}-K_L\|.                              \tag{7.1}
\]

Assume the radical is uncharged into this harmonic collar:

\[
 \boxed{
 \langle R_Bn,w\rangle=0
 \quad(n\in\mathcal N_L,\ w\in\mathcal W).}          \tag{7.2}
\]

Set

\[
 C_L=\frac{M_B^2}{\gamma_L}.                          \tag{7.3}
\]

Then for all `u in V_L` and `w in W`,

\[
 |q_B(u,w)|^2
 \le C_Lq_L(u,u)\|w\|_2^2,                           \tag{7.4}
\]

\[
 q_B(w,w)\ge\mathfrak h(w,w)-M_B\|w\|_2^2,          \tag{7.5}
\]

and

\[
\boxed{
\begin{aligned}
 q_B(u+w,u+w)
 &\ge
 \left(\sqrt{q_L(u,u)}
       -\sqrt{C_L\omega\,\mathfrak h(w,w)}\right)^2\\
 &\quad+
 \left[1-(M_B+C_L)\omega\right]\mathfrak h(w,w).
\end{aligned}}                                      \tag{7.6}
\]

In particular,

\[
 (M_B+C_L)\omega\le1
 \quad\Longrightarrow\quad q_{L'}\succeq0.          \tag{7.7}
\]

**Proof.**  Decompose `u=n+u_perp` in `H_L`, where `n in N_L`.  Positivity of
the form implies the radical identity

\[
 q_L(n,v)=0\quad(v\in\mathcal V_L),                  \tag{7.8}
\]

and (6.5) gives

\[
 \|u_\perp\|_2^2\le\gamma_L^{-1}q_L(u,u).            \tag{7.9}
\]

Because `w` is `h`-orthogonal to `V_L`,

\[
 q_B(u,w)=\langle R_Bu,w\rangle.                     \tag{7.10}
\]

Hypothesis (7.2) removes `n`; boundedness of `R_B` and (7.9) prove (7.4).
Equation (7.5) is immediate from (6.1).  The exact norm identity (4.5) gives

\[
 \|w\|_2^2\le\omega\mathfrak h(w,w).                 \tag{7.11}
\]

Insert (7.4), (7.5), and (7.11) into

\[
 q_B(u+w)=q_L(u)+2q_B(u,w)+q_B(w)
\]

and complete the square to obtain (7.6).  Finally,

\[
 \mathcal V_{L'}=\mathcal V_L
 \oplus_{\mathfrak h}\mathcal W,                     \tag{7.12}
\]

so (7.6) covers every form-domain vector and proves (7.7).  `square`

If `N_L={0}`, condition (7.2) is vacuous.  Therefore strict positivity at a
fixed support always propagates through some nonempty right interval.  At a
singular support, (7.2) is the only part of the all-vector Ward inequality not
already supplied by bounded residuals and compact resolvent.

There is also an exact Euler--Lagrange interpretation.  For
`n in N_L`,

\[
 \langle R_Bn,w\rangle=0\quad(w\in\mathcal W_{L,L'})
 \quad\Longleftrightarrow\quad
 q_B(n,v)=0\quad(v\in\mathcal V_{L'}).                \tag{7.13}
\]

The forward implication uses (7.8), the decomposition (7.12), and
`q_B(n,w)=<R_Bn,w>`; the reverse implication is immediate.  Thus an
uncharged old radical vector is exactly a nullstate whose weak
Euler--Lagrange equation extends to the enlarged support.

There is no claim that `C_L` is uniform in `L`.  It may diverge when a positive
eigenvalue approaches zero.  A compact-slab uniform `HRW` theorem would give
effective uniform steps, but Theorem 7.1 does not prove it and the qualitative
maximal-support argument below does not require it.

## 8. Maximal-support continuation and first-charge dichotomy

### Theorem 8.1 -- open--closed propagation

Suppose a consistent family of forms (6.3) is given on every finite support
slab and that

\[
 q_{L_0}\succeq0                                      \tag{8.1}
\]

for some `L_0>0`.  Assume that whenever `L>=L_0`, `q_L>=0`, and
`N_L` is nonzero, there exists a sequence

\[
 L_j>L,\qquad L_j\downarrow L,                        \tag{8.2}
\]

such that

\[
 \langle R_{B_j}n,w\rangle=0
 \quad
 (n\in\mathcal N_L,
  \ w\in\mathcal W_{L,L_j})                          \tag{8.3}
\]

for any common slab `B_j>=L_j` containing the two supports.  Then

\[
 q_L\succeq0\qquad\text{for every finite }L\ge L_0.  \tag{8.4}
\]

**Proof.**  Let

\[
 \mathcal P=\{L\ge L_0:q_L\succeq0\}.                \tag{8.5}
\]

Restriction makes `P` downward closed.  Suppose it is bounded and put
`A=sup P`.  If `A=L_0`, then `A in P` by (8.1).  If `A>L_0`, every
`L in [L_0,A)` lies in `P`: choose an element of `P` larger than `L` and
restrict.  For arbitrary `f in V_A`, Lemma 3.3 then gives
`f_k in V_{L_k}` with `L_0<=L_k<A`, `L_k` increasing to `A`, and `f_k->f`
in `h`.  On a common finite slab, (6.1) is `h` continuous.  Hence

\[
 q_A(f,f)=\lim_kq_{L_k}(f_k,f_k)\ge0,                 \tag{8.6}
\]

so `A in P` in this case as well.

Fix the single outer slab `B=A+1`.  If `N_A={0}`, Theorem 7.1 and (4.7)
extend positivity past `A`, a contradiction.  If `N_A` is nonzero, select
an uncharged `L_j` from (8.2)--(8.3), with `L_j<B`, so close to `A` that

\[
 (M_B+C_A)\|K_{L_j}-K_A\|\le1.                       \tag{8.7}
\]

Theorem 7.1 again gives `L_j in P`, a contradiction.  Thus `P` is unbounded;
downward closure gives (8.4).  `square`

This proof replaces a quantitative iterative non-Zeno condition by
semidefinite local continuation at the limiting support.  Bare local
openness at strictly positive supports is still insufficient: its step sizes
can shrink to a finite singular endpoint.

### Corollary 8.2 -- exact first-failure obstruction

Under the reference and bounded-residual hypotheses, if (8.1) holds but
global positivity fails, then there is a finite first support

\[
 A=\sup\mathcal P                                     \tag{8.8}
\]

such that `q_A>=0`, `N_A` is nonzero, and for every sufficiently close
`L'>A` there are

\[
 0\ne n\in\mathcal N_A,
 \qquad w\in\mathcal W_{A,L'}                        \tag{8.9}
\]

with

\[
 \langle R_Bn,w\rangle\ne0.                          \tag{8.10}
\]

Indeed, the proof of Theorem 8.1 gives `q_A>=0`.  If the radical were zero,
or if an arbitrarily close collar annihilated it, Theorem 7.1 would cross
`A`.

The charge condition cannot be deduced from continuity, compact embedding,
or bounded residuals.  In the scalar old/collar model

\[
 q=\begin{pmatrix}0&b\\b&d\end{pmatrix},
 \qquad \mathfrak h=I,                               \tag{8.11}
\]

the old restriction is nonnegative and entirely radical, but every `b!=0`
makes the enlarged form indefinite.  This is exactly a charged-nullstate
failure.  More elaborate projection-defect examples in the operator theorem
suite show that compactness, all-Schatten decay, finite moment constraints,
and parity constraints likewise do not force (8.3).

The nesting quantifiers do not weaken this gate.  At a fixed semidefinite
support `A`, cancellation at one `L'>A`, throughout one right neighborhood,
or along an arbitrarily thin sequence are equivalent: cancellation on
`V_{L'}` restricts to every intermediate space.  A basis of the finite
dimensional `N_A` also turns nullvector-dependent germs into one common germ.
Together with Theorem 7.1, germ cancellation is therefore equivalent to
right-extension of positivity at that contact.  Universally over all
completed-zeta contacts, it is RH-equivalent under the accepted global Weil
interface.  This logical classification does not prove the cancellation.

## 9. Prime activations and uniformity audit

### 9.1 No discontinuity at an activation threshold

On a fixed outer interval `I_B`, include every prime-power translation that
can act anywhere on that slab and define `q_L` only by restriction.  A
translation longer than the support diameter has disjoint support and hence
zero matrix element.  At exact contact, the two `L2` supports intersect only
on a null set, so the matrix element is again zero.  Thus the apparent change
in an enumerated active mask is not a jump of the continuum form.

The support-domain limits in Lemma 3.3 and bounded perturbation in (6.1) imply
norm continuity of shifted embedded resolvents across every activation.  No
prime-event-dependent redefinition of `h`, of the support embeddings, or of
the moment corrector occurs.

### 9.2 What is uniform on a compact slab

The following quantities are uniform on each fixed `[a,b]` with `a>0`:

- the reference form and compact embedding;
- the modulus `Omega_[a,b](delta)=o(1)`;
- the fixed relative moment retraction `Pi` and its form norm;
- the residual operator bound `M_b` after all completed sources on the slab
  are combined.

The automatically generated constant

\[
 C_L=M_b^2/\gamma_L                                  \tag{9.1}
\]

is only pointwise.  It need not stay bounded when `L` varies, because the
first positive eigenvalue may approach zero.  Uniform compact-slab `HRW`
therefore remains open.  The maximal-support proof uses only the finite gap on
the complement of the radical at one limiting support and then takes an
arbitrarily thin collar; it bypasses uniform `HRW` rather than proving it.

## 10. Consequences and corrections to the current decision tree

1. The explicit `NR_log` estimate in the harmonic-resolvent audit remains an
   interesting quantitative problem, but the qualitative reference theorem
   needed for an existence-only continuation is already proved by Theorem
   4.1.  The finite-dimensional capacity countermodel there does not satisfy
   a nested compact-resolvent limit and does not refute this theorem.
2. The relative stable-right-inverse/localization problem in the semilocal
   report is closed qualitatively by Section 5.  Only an explicit modulus is
   still missing.
3. Uniform all-vector `HRW` is stronger than necessary for qualitative
   propagation.  Off the radical it follows pointwise from bounded residuals
   and the compact-resolvent gap.  The exact remaining arithmetic target is
   (8.3).
4. The inverse Poisson notation `A_L^{-1}B_L` is not valid at a singular old
   form unless the cross block annihilates the kernel and satisfies the
   corresponding range condition.  At zero floor one must use the
   division-free inequality (7.4), or a Moore--Penrose inverse after proving
   that condition.
5. A separate iterative non-Zeno theorem is unnecessary under the
   semidefinite continuation hypothesis of Theorem 8.1.  The earlier Zeno
   warning remains valid for arguments that establish openness only at
   strictly positive supports and do not control the limiting radical.

## 11. Claim and novelty ledger

| Claim | Status | Novelty assessment |
|---|---|---|
| compact support-core identities, compact embedding, monotone projection convergence | proved here at analytic-note level | standard closed-form/Mosco machinery |
| exact resolvent difference and norm identity (4.4)--(4.5) | proved here | standard Hilbert-space consequence, useful project formulation |
| qualitative relative localization with fixed moment correction | proved here | low abstract novelty; corrects a project typing/gap statement |
| semidefinite continuation Theorem 7.1 | proved abstractly | standard spectral-gap plus Schur argument; project-specific target reduction |
| maximal-support and first-charge dichotomy | proved conditionally on (8.3) | likely a new project synthesis; literature novelty not established |
| compact-slab bounded completed-zeta residual | unconditional standard analysis in the stated normalization | not a positivity theorem |
| certified initial `p=5` seed | pre-existing project theorem under its recorded Arb-plus-analytic trust base | local only |
| completed-zeta charged-nullstate cancellation (8.3) | **open** | sole new arithmetic continuation target identified here |
| uniform `HRW`, global Weil positivity, uniform zero-free strip, RH | **open** | no promotion |

## 12. Source pointers

- reference form, block identities, `NR_log`, `HRW`, and bounded residual:
  `ZETA23-HARMONIC-RESOLVENT-WARD-PROPAGATION-AUDIT-2026-09-01.md`,
  lines 35--159 and 201--242;
- relative moment branch and previously stated localization gap:
  `ZETA23-SEMILOCAL-HANKEL-TO-POISSON-GATE-2026-09-01.md`,
  lines 273--345;
- certified seed and first `p=5` crossing:
  `ZETA23-P5-FIRST-EVENT-PROPAGATION-CERTIFICATION-2026-09-01.md`,
  lines 6--51 and 95--142;
- prior Schur and source-identifying continuation routes:
  `ZETA23-WEIL-GLOBAL-SUPPORT-LITERATURE-PASSPORT-AND-RECENT-CLAIM-AUDIT-2026-08-31.md`,
  lines 759--801;
- projection-defect countermodels:
  `ZETA23-OPERATOR-LEMONADE-THEOREM-SUITE-2026-09-01.md`,
  lines 175--316.
