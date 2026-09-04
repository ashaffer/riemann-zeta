# Semilocal Hankel-to-Poisson gate

> **Superseded localization status (2026-09-01).**  The stable-right-inverse
> issue identified below is resolved qualitatively on every support slab
> bounded away from zero: a fixed interior two-moment retraction proves the
> required form-core density, and compact embedding gives norm-continuous
> relative resolvents.  A quantitative rate remains open.  General uniform
> `RSW_R` is also stronger than necessary; at a semidefinite contact only
> exact residual charge on the finite-dimensional kernel remains.  See
> [the recursive fixed-point report](ZETA23-RECURSIVE-CONSOLIDATION-FIXED-POINT-2026-09-01.md).

Date: 2026-09-01

## Verdict

The normalization-exact bridge exists, but the hoped-for positive compact
Hankel square does not.

The Connes--Consani semilocal phase gives exactly the pole-free Weil source,
and the existing Ward cross block is exactly its quantized-differential trace
pairing plus the rank-two zeta pole.  However, the full two-sided Hardy defect
contains a noncompact reverse/Sonin channel and is signed.  Consequently the
published quasi-inner theorem does not imply the harmonic residual Ward bound.

A narrower branch survives.  On the two-moment relative space

\[
 \mathcal R_L=\{f:\operatorname{supp}f\subset I_L,
                 \ell_+(f)=\ell_-(f)=0\},
 \qquad
 \ell_\pm(f)=\int f(x)e^{\pm x/2}\,dx,
\]

the zeta pole vanishes algebraically.  A new five-rung diagnostic on the
correct nested relative complement gives Ward ratios between `0.8977` and
`1.0961` while the old relative Ritz floor drops by a factor about `62.4`.
This keeps a **relative signed-cancellation theorem** alive; it is not a proof
of that theorem.  Global positivity on this relative space is still
RH-equivalent, so the branch has not reduced the logical strength of the
problem.

`HRW`, uniform propagation, a uniform zero-free strip, and RH remain open.

## 1. Exact local-factor bridge

Use the repository Fourier convention

\[
 \widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx.
\]

For `F={infinity,2,3,5}`, the Connes--Consani orientation is

\[
 u_F(t)=\pi^{-it}
 \frac{\Gamma(\frac14+\frac{it}{2})}
      {\Gamma(\frac14-\frac{it}{2})}
 \prod_{p=2,3,5}
 \frac{1-p^{-1/2+it}}{1-p^{-1/2-it}},
 \qquad |u_F(t)|=1.
\]

Direct differentiation gives

\[
 -i\overline{u_F}u_F'
 =\Re\psi\!\left(\frac14+\frac{it}{2}\right)-\log\pi
 -2\sum_{p=2,3,5}\sum_{k\ge1}
   \log p\,p^{-k/2}\cos(kt\log p).                 \tag{1}
\]

This is exactly the pole-free semilocal Weil multiplier.  The full local
factors are differentiated before support compression; at the first `p=5`
window only `2,3,4,5` survive in a licensed test pairing.  The reciprocal
phase used in an older helper reverses the sign.

This normalization and the quasi-inner result are from Connes--Consani,
[Quasi-inner functions and local factors](https://arxiv.org/html/2008.10974v1).

## 2. The Weil functional is a trace anomaly

Let `P` be the Hardy projection and `U_F=M_{u_F}`.  Define

\[
 D_{U_F}=P-U_F^*PU_F=-\frac12U_F^*[2P-I,U_F].       \tag{2}
\]

The continuum kernel has analytic diagonal

\[
 K_{D_U}(s,t)=-\frac{i}{2\pi}
 \frac{1-\overline{U(s)}U(t)}{s-t},
 \qquad
 K_{D_U}(t,t)=\frac{\Theta_U'(t)}{2\pi}.            \tag{3}
\]

Thus the phase derivative in (1) appears only after taking the regularized
trace diagonal:

\[
 \tau_g(D_{U_F})
 =\operatorname{Tr}(M_gD_{U_F})
 =\frac1{2\pi}\int g(t)(-i\overline{u_F}u_F')(t)\,dt.\tag{4}
\]

It is incorrect to identify `D_U` itself with the multiplication operator in
(1).  This distinction is explicit in Connes--Consani,
[Weil positivity and the trace formula](https://arxiv.org/html/2006.13771v1).

For the reference-harmonic lift `J_h`, `h(phi,J_h v)=0`.  Therefore the
current Ward block has the exact representation

\[
 \boxed{
 B_{ij}=Q_W(\phi_i,J_he_j)
 =\tau_{\widehat\phi_i\overline{\widehat{J_he_j}}}(D_{U_F})
  +P_{\rm pole}(\phi_i,J_he_j),
 }
                                                               \tag{5}
\]

where

\[
 P_{\rm pole}(v,w)
 =\ell_+(v)\overline{\ell_-(w)}
  +\ell_-(v)\overline{\ell_+(w)}.                \tag{6}
\]

Suzuki's screw-function realization gives the independent equality

\[
 Q_W(v,w)=\langle G_aDv,Dw\rangle,
\]

so (5) is also the exact Hardy-to-screw-to-Poisson socket.  Positivity or a
square root of `G_a` cannot be used unconditionally; that would import the RH
criterion being sought.  See Suzuki,
[Weil's quadratic form via the screw function](https://arxiv.org/html/2606.09096).

## 3. Why the compact square-root proposal fails

In Hardy blocks write

\[
 U_F=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

Then exactly

\[
 D_{U_F}=
 \begin{pmatrix}
 c^*c&-a^*b\\
 -b^*a&-b^*b
 \end{pmatrix},
 \qquad
 D_{U_F}^2=\operatorname{diag}(c^*c,b^*b).         \tag{7}
\]

Connes--Consani control `c=(I-P)U_FP`: for three finite primes it is an
infinitesimal of order `1/6`.  This is only one oriented half-line leakage.
Their Sonin theorem also gives an infinite-dimensional `ker d`; unitarity
implies `b` is an isometry there.  Hence the reverse leakage is noncompact.
The two physical collar edges have opposite orientations and encounter both
blocks.  Taking an absolute value necessarily sees the noncompact channel and
also destroys the signed source cancellation.

Two moment constraints cannot repair this abstractly.  If `S=ker d` is
infinite-dimensional and `E=ker ell_+ intersect ker ell_-`, then `S intersect
E` is still infinite-dimensional and `b` remains an isometry there.  More
generally restriction to a finite-codimensional subspace does not change the
essential norm of `b`.  Reflection only splits `S` into parities; at least one
infinite parity sector remains.

There is an exact relative countermodel.  Let a projection difference `D`
have orthonormal eigenvectors `t_n,s_n` with eigenvalues `delta_n,-1`, where
`delta_n` comes from compact rotation blocks and tends to zero, while `s_n`
lies in the isometric Sonin channel.  Put `epsilon_n=delta_n^2` and

\[
 u_n=A_nt_n+B_ns_n,\qquad w_n=-B_nt_n+A_ns_n,
\]

\[
 A_n^2=\frac{1+\epsilon_n}{1+\delta_n},\qquad
 B_n^2=\frac{\delta_n-\epsilon_n}{1+\delta_n}.
\]

The vectors are orthonormal, so with `h=I`, `w_n` is exactly h-harmonic
relative to `old=span(u_n)`.  They can all be placed in the joint two-moment
kernel and one reflection parity.  Nevertheless

\[
 D(u_n,u_n)=\epsilon_n,
 \qquad |D(u_n,w_n)|^2=(1+\epsilon_n)(\delta_n-\epsilon_n),
\]

and the Ward ratio is

\[
 (1+\delta_n^2)(\delta_n^{-1}-1)\longrightarrow\infty. \tag{10}
\]

Thus reflection, moments, h-harmonicity, bounded residual, and one-sided
compactness together still do not imply the desired estimate.

The generator has an exact layer-cake form

\[
 q_F=\operatorname{qf-lim}_{R\to\infty}
 \int_{-R}^{R}(P_a-U_F^*P_aU_F)\,da,               \tag{8}
\]

but this is a clipped quadratic-form limit, not an absolutely convergent
positive operator integral.  Each fiber is a signed difference of
projections.

There is also a mask/gauge obstruction.  Adding a prime whose powers lie
outside the support window leaves every licensed logarithmic-derivative
pairing unchanged, while changing the Hankel block, its singular subspaces,
and its quasi-inner order.  A `c`-only reconstruction is therefore not
determined by the localized Ward form.  The minimal active mask must be fixed.

Finally, smooth quasi-inner structure is generically insufficient.  On the
circle take `N=-i d/dtheta` and `U=exp(i b sin(theta))`.  The Hankel block is
rapidly compact, but

\[
 N-U^*NU=-b\cos\theta.
\]

With one old and one collar mode and reference old floor `epsilon`, the Ward
response is `b^2/(4 epsilon)`, which diverges as the floor collapses.

## 4. Pole mismatch

The zeta pole in (6) is universal rank two.  It is not the finite-rank polar
piece called `E_0` in the quasi-inner analysis.  For `m` finite primes, the
local-factor product has a pole of order `m+1` at `s=0`; its polar Hankel part
has rank `m+1`.  Thus the present product has rank four, and adjoining an
inactive prime changes that rank while leaving the Ward target fixed.

This rules out a canonical identification of the two corrections.  It also
explains the earlier source audit: removing or isolating the true pole gave
Ward ratios from `1.76e6` to `4.61e7`, whereas the completed source stayed near
one.  Separate norm estimates are structurally unusable.

## 5. Finite trace no-go

An exactly unitary finite cyclic collocation erases the anomaly.  For finite
matrices, if `M_g U=U M_g`, then cyclicity gives

\[
 \operatorname{Tr}\bigl(M_g(P-U^*PU)\bigr)=0.       \tag{9}
\]

This was checked numerically and proved in Lean.  Valid finite approximations
must instead use either the point-split kernel (3), with its diagonal supplied
analytically, or padded noncyclic Laurent/Toeplitz sections whose boundary
nonunitarity retains the anomaly.  Singular vectors from a cyclic DFT model
have no evidentiary value here.

The first noncyclic reconstruction was also run on the actual `M=40,q=1`
relative Ward extremizer.  Direct Cayley/Jacobian quadrature of the analytic
diagonal converges to the x-space value `1.096028...` (error `1.61e-6` at
`2^20` points), validating the convention.  Smooth-symbol and unit-shift
controls reconstruct exactly.  But hard Laurent block sums do not stabilize:
for example, `(N,L)=(4,32)` gives

\[
 (++,+-,-+,--)= (1.1933,.4971,.4201,-1.0585),
\]

while `(8,64)` gives `(1.6789,.1432,.0835,-1.4297)`, and further padding is
nonconvergent.  The reverse block is order one in every tested truncation and
its Frobenius mass exceeds the compact block's, so these data do not support
Sonin suppression.  Since the separate traces are conditional, no continuum
block percentage is claimed.  A common Abel/heat regularization or the
point-split kernel is required before further block attribution.

## 6. Surviving two-moment branch

The full relative nullspace is formed first.  The old relative nullspace is
embedded and G-orthonormalized, and its G-orthogonal complement inside the
full relative space supplies the corrected collar.  Thus the collar has
dimension `2q` but generally includes an old-supported correction; it is not
the literal exterior collar.

On these coordinates (6) vanishes exactly.  The pole-free semilocal form and
the completed form therefore give the same Ward response up to floating-point
error.

| old `M` | `q`/side | `delta` | old relative floor | relative Ward ratio |
|---:|---:|---:|---:|---:|
| 40 | 1 | .32 | `2.635e-5` | **1.0960** |
| 48 | 2 | .40 | `1.209e-5` | **1.0898** |
| 80 | 1 | .16 | `1.940e-6` | **.8977** |
| 96 | 2 | .20 | `1.081e-6` | **1.0174** |
| 128 | 1 | .10 | `4.222e-7` | **.9468** |

Moment and G-orthogonality residuals are below `1e-14`.  In the independently
rerun `M=40` row, the compressed pole norm is `1.61e-16` and completed versus
pole-free ratios differ by `8.53e-14`.

This is not a fresh RH criterion: two-moment relative spaces already occur in
the project's relative incidence and boundary-Weyl programs.  It also does
not revive the previously falsified strengthened Hodge inequality.  The new
information is narrower: the semilocal anomaly has an exact socket into the
ordinary relative Ward problem, and eliminating the pole does not destroy the
observed five-rung stability.

Connes--Consani's finite-vanishing-set form of Weil's criterion shows that
requiring the Mellin transform to vanish at `0` and `1` remains equivalent to
RH; in the additive convention these are the two moments above.  Therefore a
cofinal proof of relative positivity would prove RH directly.  At a fixed
support it is weaker than completed positivity, and its corrected collar has
old-supported components.  The existing literal-collar `HRW` and `NR_log`
adapter consequently do not transfer without a new quantitative theorem.

## 7. The theorem that is actually missing

Let `A_L` be the pole-free Weil form on the old relative space and let
`J_{h,L,delta}^{rel}` be the reference-harmonic lift into the corrected
relative collar.  Put `R_F=q_F-h`; its multiplier is bounded because the
logarithmic growth cancels between `q_F` and `h`.  The surviving target is

\[
 \boxed{
 (B_L^{rel})^*A_L^{-1}B_L^{rel}
 \preceq C_R (J_{h,L,\delta}^{rel})^*GJ_{h,L,\delta}^{rel},
 \qquad
 B_L^{rel}=E_LR_FJ_{h,L,\delta}^{rel}.
 }                                                       \tag{RSW_R}
\]

Boundedness of `R_F` on `L2` does not prove `(RSW_R)`, because the old
`A_L` floor still collapses.  Douglas factorization shows that factoring
`B_L^{rel}` through `A_L^{1/2}` with a uniform norm is exactly the missing
Ward theorem, not a shortcut around it.

Propagation would additionally require a relative reference-localization
estimate for the moment-corrected collar, with a modulus tending to zero as
`delta` tends to zero, and the residual diagonal estimate.  Controlling the
old-supported moment correction is a stable-right-inverse problem not covered
by the literal-collar `NR_log` calculation.  Directly proving the complete
relative Schur complement nonnegative would simply restate one-step relative
positivity; the factorized Ward-plus-localization route is stronger but is the
only presently identified noncircular mechanism.

Finally, `F={infinity,2,3,5}` is licensed only on the present support slab.
Every fixed finite place set becomes indefinite on sufficiently large
moment-null supports, so a cofinal argument must grow the place mask at each
prime event while controlling its constants.

The anomaly-preserving hard-Toeplitz falsifier has now been attempted and is
regularization-indeterminate.  The next licensed finite test is a common
Abel/heat regularization of `c^*c`, both cross terms, and `-b^*b`, proved first
to recover the analytic trace diagonal.  Independently of that experiment,
the exact abstract countermodel means that only an arithmetic cancellation or
alignment theorem—not qualitative compactness—can prove the Ward bound.

There is one sharp positive conditional identity.  If the actual support
geometry could be shown to align so that `A=c^*c` and `B=c^*d`, then

\[
 |\langle x,c^*dy\rangle|^2
 \le \langle x,c^*cx\rangle\,\|y\|^2,              \tag{11}
\]

giving Ward constant one without division by the collapsing floor.  But
Paley--Wiener reflection activates both Hardy directions: for convolution by
`v`,

\[
 \|P_+C_vP_-\|_{HS}^2=\int_0^\infty x|v(x)|^2dx,
 \quad
 \|P_-C_vP_+\|_{HS}^2=\int_{-\infty}^0|x||v(x)|^2dx.
\]

For nonzero even or odd `v` the two values are equal and nonzero.  Hence (11)
would require a genuinely zeta-specific contamination-cancellation identity;
it cannot follow from symmetry or the moment constraints alone.

## Claim ledger

- equations (1)--(9), block identities, pole rank, and finite cyclic no-go:
  exact algebra/analysis in the stated conventions;
- Lean trace theorem: machine checked;
- five relative rows: cutoff-free high-precision assembly followed by
  ordinary double-precision linear algebra, not interval certified;
- literature-level novelty of the identities: not claimed;
- `(RSW_R)`, `HRW`, propagation, a uniform zero-free strip, and RH: open.

## Artifacts

- exact gates: [`semilocal_hankel_poisson_gate.py`](../src/semilocal_hankel_poisson_gate.py)
- relative diagnostic: [`semilocal_relative_ward_probe.py`](../src/semilocal_relative_ward_probe.py)
- anomaly finite sections: [`semilocal_toeplitz_anomaly_probe.py`](../src/semilocal_toeplitz_anomaly_probe.py)
- tests: [`test_semilocal_hankel_poisson_gate.py`](../src/test_semilocal_hankel_poisson_gate.py),
  [`test_semilocal_relative_ward_probe.py`](../src/test_semilocal_relative_ward_probe.py),
  [`test_semilocal_toeplitz_anomaly_probe.py`](../src/test_semilocal_toeplitz_anomaly_probe.py)
- Lean theorem: [`SemilocalHankelTraceNoGo.lean`](../lean/rhbridge/RHBridge/SemilocalHankelTraceNoGo.lean)
- Toeplitz reconstruction report: [`ZETA23-SEMILOCAL-TOEPLITZ-ANOMALY-PRELIMINARY-2026-09-01.md`](ZETA23-SEMILOCAL-TOEPLITZ-ANOMALY-PRELIMINARY-2026-09-01.md)
- finite data: [`zeta23_semilocal_relative_ward_summary_2026_09_01.json`](zeta23_semilocal_relative_ward_summary_2026_09_01.json)
- exact-gate output: [`zeta23_semilocal_hankel_poisson_gate_2026_09_01.json`](zeta23_semilocal_hankel_poisson_gate_2026_09_01.json)
- preflight/postflight: [`zeta23_semilocal_hankel_poisson_preflight_v1.json`](context/zeta23_semilocal_hankel_poisson_preflight_v1.json),
  [`zeta23_semilocal_hankel_poisson_postflight_v1.json`](context/zeta23_semilocal_hankel_poisson_postflight_v1.json)
