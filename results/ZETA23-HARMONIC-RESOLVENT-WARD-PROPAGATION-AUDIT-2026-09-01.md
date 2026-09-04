# Harmonic resolvent/Ward propagation audit

Date: 2026-09-01

> **Superseded propagation status (same date).**  The quantitative
> `NR_log` estimate isolated below remains open as a rate theorem, but it is
> no longer a logical prerequisite for existence-only propagation.  Compact
> embedding of the bounded-support logarithmic form domain gives an optimal
> qualitative norm-resolvent modulus.  At a semidefinite support, Fredholm
> theory supplies the Ward estimate off the finite-dimensional kernel; the
> exact remaining condition is zero residual charge from that kernel into
> arbitrarily thin reference-harmonic collars.  A maximal-support argument
> also removes the separate non-Zeno hypothesis.  See
> [the recursive fixed-point report](ZETA23-RECURSIVE-CONSOLIDATION-FIXED-POINT-2026-09-01.md)
> and its dedicated localization proof.  The numerical and quantitative-rate
> analyses below remain valid in their stated scope.

## Verdict

The uniform zero-free strip, global Weil positivity, and RH have **not** been
proved.

The audit did, however, change the live propagation target in a substantive
way.  The previously proposed dyadic spectral-Carleson allocation is not a
consequence of boundary capacity, bounded residuals, or positivity, and is
strictly stronger than the estimate needed by the Schur complement.  It
should not remain the default target.

The credible replacement is a two-lemma factorization:

1. a reference-form norm-resolvent estimate for adding a thin support collar;
2. a zeta-specific, division-free harmonic residual Ward inequality.

The new high-precision finite diagnostic supports both factors through the
tested resolution range.  Its basis-invariant Ward ratio is `1.05946` for one
collar mode per side, `1.03802` for two modes per side at `delta=0.4`, and
`1.14708` after shrinking the two-mode collar to `delta=0.2`.  This is
evidence, not a continuum or interval-certified theorem.

## 1. Exact block reduction

Write project support as `L=4a`, so the physical interval is

\[
 I_L=[-L/4,L/4].
\]

The first certified endpoint is

\[
 L_5=2\log 5.
\]

Use the positive reference form

\[
 \mathfrak h(f)=\|f\|_2^2+
 \frac1{2\pi}\int_{\mathbb R}|\widehat f(t)|^2
       \frac12\log(1+4t^2)\,dt.
\]

After making the old and literal-collar bases orthogonal in `L2`, write

\[
 Q=\begin{pmatrix}A&X\\X^*&D\end{pmatrix},\qquad
 \mathfrak h=\begin{pmatrix}H&Y\\Y^*&Z\end{pmatrix}.
\]

Set

\[
 K=H^{-1}Y,\qquad J=\binom{-K}{I},\qquad
 S=Z-Y^*H^{-1}Y.
\]

The congruence `(u,v) -> (u-Kv,v)` gives the exact identity

\[
 T^*QT=
 \begin{pmatrix}
 A&\widetilde X\\
 \widetilde X^*&\widetilde D
 \end{pmatrix},
\]

where, for `R=Q-h`,

\[
 \widetilde X=X-AK=R_{oc}-R_{oo}K=P_oRJ,
 \qquad
 \widetilde D=S+J^*RJ.
\]

Thus, when `A>0`, the exact remaining condition is

\[
 S+J^*RJ-J^*RP_o^*A^{-1}P_oRJ\succeq0.       \tag{1}
\]

No estimate through the smallest eigenvalue of `A` has yet been made.

## 2. What logarithmic collar capacity proves

Let `E` have length `delta <= exp(-1)`.  Splitting at
`T=delta^(-1/2)` proves

\[
 \|1_Ef\|_2^2\le
 \frac{8}{\log(e/\delta)}\,\mathfrak h(f).     \tag{2}
\]

Indeed, the low-frequency piece obeys

\[
 \|f_{\le T}\|_\infty^2\le (T/\pi)\|f\|_2^2,
\]

while the high-frequency piece is bounded by

\[
 \|f_{>T}\|_2^2\le
 \frac{W_+(f)}{\tfrac12\log(1+4T^2)}.
\]

The order `1/log(1/delta)` is sharp under rescaling of a fixed compactly
supported profile.

Applied to the harmonic representative `Jv`, (2) controls only the literal
collar mass:

\[
 G_c\preceq \frac8{\log(e/\delta)}S.
\]

It does **not** control the old-side harmonic tail `K*G_o K`.

The exact missing reference theorem is

\[
 J^*GJ=K^*G_oK+G_c
 \preceq \frac{C_R}{\log(e/\delta)}S.           \tag{NR_log}
\]

Block inversion shows that `NR_log` is equivalent to the norm-resolvent
domain-perturbation estimate

\[
 \|T_{I_{L+\delta}}^{-1}
   -\iota T_{I_L}^{-1}\iota^*\|_{L^2\to L^2}
 \le \frac{C_R}{\log(e/\delta)},               \tag{3}
\]

where `T_I` is the operator associated to `h` on functions supported in `I`.

### Exact abstract obstruction

Capacity alone cannot prove (3).  Let

\[
 G=\operatorname{diag}(1,\eta),\qquad
 \mathfrak h=\begin{pmatrix}3&3\\3&5\end{pmatrix}.
\]

For `eta<=1/2`, `h-G` is positive, `K=1`, and `S=2`.  The raw collar ratio is
`eta/2 -> 0`, but

\[
 \frac{K^*G_oK+G_c}{S}=\frac{1+\eta}{2}\longrightarrow\frac12.
\]

The actual translation-invariant log-Bessel kernel must therefore enter any
proof of `NR_log`.

## 3. Why the dyadic allocation was the wrong target

The former candidate demanded, for the old spectral band
`2^(-m-1)<lambda<=2^(-m)`,

\[
 \rho_m\lesssim
 \frac1{\log(e/\delta)}\frac{2^{-m}}{(m+1)^2}. \tag{4}
\]

There is no abstract route from capacity to (4).  Capacity gives smallness in
the collar scale; old positivity gives smallness in `lambda`.  The two facts
give a minimum, not their product.

An exact positive `2 by 2` countermodel makes the mismatch explicit.  Put

\[
 \delta_m=e^{-m},\quad \eta_m=(m+1)^{-1},\quad
 \lambda_m=2^{-m},\quad b_m^2=\lambda_m\eta_m/2,
\]

and take

\[
 G=\operatorname{diag}(1,\eta_m),\quad
 \mathfrak h=I,\quad
 Q=\begin{pmatrix}\lambda_m&b_m\\b_m&1\end{pmatrix}.
\]

Then `Q>0`, the residual is uniformly `G`-bounded, reference localization is
exactly of order `1/log`, and the full inverse response is

\[
 b_m^2/\lambda_m=\frac1{2(m+1)}.
\]

Nevertheless the weighted quantity in (4) equals `(m+1)/2` before its extra
logarithmic scaling.  Therefore the direct response can have exactly the
desired rate while (4) fails by an unbounded factor.

## 4. The new arithmetic target

The numerical pattern points to

\[
 J^*RP_o^*A^{-1}P_oRJ\preceq C_R J^*GJ.       \tag{HRW}
\]

This has an equivalent, division-free formulation.  If `u` is old-supported
and `w` is reference-harmonic relative to the old space, then

\[
 |R(u,w)|^2\le C_R\,Q_L(u,u)\,\|w\|_2^2.      \tag{HRW'}
\]

Because `h(u,w)=0`, the left side can equally be written `|Q(u,w)|^2`.
Taking `u=A^{-1}P_oRw` proves `HRW` from `HRW'`; ordinary Cauchy--Schwarz in
the `A` energy proves the converse.

This is the plausible source-specific Ward/Bessel theorem.  It asks the
combined pole, bounded archimedean remainder, and all actual prime
translations to map a harmonic boundary vector into the square-root range of
the old Weil form.  Componentwise absolute-value estimates are not licensed.

Combining `NR_log`, `HRW`, and the standard compact-support residual bound

\[
 |R|\preceq M_R G
\]

turns (1) into

\[
 \widetilde D-\widetilde X^*A^{-1}\widetilde X
 \succeq
 \left(1-\frac{(M_R+C_R)C_R^{\rm ref}}
                    {\log(e/\delta)}\right)S. \tag{5}
\]

Uniform constants on each finite support slab therefore give a positive
step size without dividing by the old ground floor.  This is the correct
socket for the existing formal cofinal-propagation theorem.

`HRW` remains open and could contain essentially the hard arithmetic content
of the desired strip.  Equation (5) is a reduction, not a proof of that
content.

## 5. Finite diagnostic

The new driver is
[`harmonic_schur_collar_probe.py`](../src/harmonic_schur_collar_probe.py).
It implements:

- arbitrary unequal-width triangular hats;
- literal disjoint collars on both sides of `I_L`;
- exact polynomial hat overlaps;
- cutoff-free x-space formulas for the log-Bessel reference and digamma
  archimedean term;
- all active actual prime powers and the pole rank-two term;
- high-precision generalized eigensolves;
- exact congruence, residual, and inverse-spectral identity checks.

The calculation uses ordinary `mpmath`, not interval balls.  It is
cutoff-free and high precision, but is still a nonrigorous finite Galerkin
diagnostic.

For collar degree `q`, the literal collar mesh is

\[
 h=\frac{\delta}{4(q+1)},
\]

and the old mesh is

\[
 d=\frac{L_5}{2(M+1)}.
\]

The licensed refinement below keeps `d/h` close to one.  Shrinking `delta`
at fixed `M` is underresolved and produces falsely favorable decay.

### Width/refinement ladder, one collar mode per side

| `M` | `delta` | old Ritz floor | `K_ref` | `K_diag` | `K_response` | Schur/S |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 0.40 | 2.240e-6 | 0.4465 | 1.4895 | 0.4253 | 0.0434 |
| 40 | 0.32 | 8.878e-7 | 0.4736 | 1.5822 | 0.5018 | 0.0498 |
| 60 | 0.21 | 2.399e-7 | 0.5173 | 1.7365 | 0.4508 | 0.1477 |
| 80 | 0.16 | 8.918e-8 | 0.5416 | 1.8428 | 0.5198 | 0.1727 |
| 128 | 0.10 | 1.330e-8 | 0.5774 | 2.0051 | 0.5222 | 0.2347 |

Here

\[
 K_{\rm response}=\log(e/\delta)\,
 \lambda_{\max}(\widetilde X^*A^{-1}\widetilde X,S).
\]

It remains in `[0.425,0.523]` while the old Ritz floor drops by a factor of
about 168.

### Collar refinement at fixed `delta=0.4`

| modes/side `q` | matched old `M` | `K_ref` | `K_diag` | `K_response` | old band statistic |
|---:|---:|---:|---:|---:|---:|
| 1 | 32 | 0.4465 | 1.4895 | 0.4253 | 6.33 |
| 2 | 48 | 0.4576 | 1.5167 | 0.4665 | 10.63 |
| 4 | 80 | 0.4702 | 1.5440 | 0.4952 | 28.56 |

The invariant aggregate quantities stabilize as collar resolution increases.
The old dyadic allocation moves in the opposite direction.  This is not a
continuum refutation of (4), but it is strong evidence that (4) is an
unstable and unnecessary coordinatewise target.

The direct generalized Ward ratios currently certified only as numerical
values are

\[
 \Theta_{40,1,0.32}=1.0594574483,
 \qquad
 \Theta_{48,2,0.40}=1.0380181007,
 \qquad
 \Theta_{96,2,0.20}=1.1470826705.
\]

The last two are genuine four-dimensional collar generalized eigenvalues,
not ratios of two separately optimized scalar quantities.  On the matched
`q=2` width refinement from `(M,delta)=(48,0.4)` to `(96,0.2)`, the triples

\[
 (K_{\rm ref},K_{\rm diag},K_{\rm response})
 = (0.458,1.517,0.467),\ (0.533,1.782,0.596)
\]

remain modest, although their upward drift means the present ladder is not a
proof of uniform boundedness.

## 6. Literature positioning

The reference operator is not merely analogous to a logarithmic Laplacian.
After rescaling it is the one-dimensional logarithmic Schrödinger/log-Bessel
operator with symbol `log(1+|xi|^2)`.  Feulefack develops its singular-kernel,
Dirichlet-form, eigenvalue, and Green-function framework and identifies it as
the variance-gamma generator:
[arXiv:2112.08783](https://arxiv.org/abs/2112.08783).

For the homogeneous logarithmic Laplacian, Chen--Weth supply the bounded-domain
Dirichlet framework and boundary regularity:
[arXiv:1710.03416](https://arxiv.org/abs/1710.03416).  The later
Chen--Hauer--Weth extension theorem realizes the logarithmic Laplacian through
a weighted local problem and proves weak unique continuation:
[arXiv:2312.15689](https://arxiv.org/abs/2312.15689).  That extension is the
most concrete imported tool for attacking `NR_log`.  Jarohs--Saldana--Weth
also give explicit Green-operator bounds and domain approximation machinery
for fractional Poisson problems:
[arXiv:1910.12297](https://arxiv.org/abs/1910.12297).

A targeted search of these works and searches for “norm-resolvent/domain
perturbation/Mosco convergence + logarithmic Laplacian” did not locate the
quantitative thin-collar estimate (3), and none of the located papers contains
the completed-zeta Ward inequality `HRW'`.  This establishes a credible
novelty target, not literature-level novelty: absence from this bounded search
is not proof that no equivalent theorem exists.

## 7. Decision-tree corrections

The important mistakes were high in the tree:

1. **Capacity was conflated with harmonic localization.**  Literal sliver
   mass is only the bottom-right part of the norm-resolvent estimate.
2. **Two smallness mechanisms were multiplied without a theorem.**  This
   created the unjustified `lambda/(m+1)^2` spectral allocation.
3. **The first shrinking-collar scout coupled support shrinkage to a changing
   Galerkin complement.**  It was useful for discovering the boundary layer,
   but was not a literal support split.
4. **Fixed-degree shrinkage was initially read too optimistically.**  Once the
   collar scale falls below the old mesh, the apparent response decay is a
   resolution artifact.
5. **A floor-free aggregate inequality was decomposed before it was tested.**
   Testing the invariant Schur response first exposed the Ward structure.

## 8. Next proof program and kill rules

The next mathematics should be theorem-first:

1. prove `NR_log` for the killed one-dimensional log-Bessel operator, most
   likely through its Green kernel or a Wiener--Hopf boundary factorization;
2. prove `HRW'` for the **combined** completed-zeta residual on one compact
   support slab;
3. make the constants uniform in the old support inside that slab and insert
   them into (5);
4. only then build an Arb literal-collar block certificate and the formal
   propagation adapter.

The route should be killed or revised if any of the following occurs:

- the Ward ratio diverges under matched old/collar refinement;
- `K_ref` diverges under the same refinement, falsifying `NR_log`;
- a proposed proof of `HRW'` assumes positivity of the enlarged form;
- the proof works only after replacing actual prime coefficients by absolute
  values or a smooth pseudonode source;
- an interval replay changes the sign or scale of the finite Schur data.

## Claim ledger

- p=5 endpoint positivity and its microscopic first crossing: rigorous,
  pre-existing project result;
- block congruence and the equivalence `HRW <-> HRW'`: exact algebra;
- literal sliver estimate (2): proved above at the analytic-note level;
- the two abstract countermodels: exact;
- finite values in the tables: high-precision, cutoff-free, non-interval
  numerical evidence;
- `NR_log`: open;
- `HRW/HRW'`: open;
- uniform/cofinal propagation, a uniform zero-free strip, and RH: open.
