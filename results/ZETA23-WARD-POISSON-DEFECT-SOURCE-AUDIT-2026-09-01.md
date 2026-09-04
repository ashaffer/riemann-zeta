# Ward source audit and Poisson-defect reformulation

Date: 2026-09-01

## Verdict

The harmonic residual Ward theorem (`HRW`), uniform adjacent-support
propagation, a uniform zero-free strip, and RH remain **open**.

The source-resolved audit did produce a useful exact reformulation and a
substantially sharper research target.  If

\[
 Q=\begin{pmatrix}A&X\\X^*&D\end{pmatrix},\qquad
 h=\begin{pmatrix}H&Y\\Y^*&Z\end{pmatrix},
\]

after the literal old/collar `L2` split, define the two Poisson maps

\[
 P_Q=A^{-1}X,\qquad P_h=H^{-1}Y.
\]

Then the harmonic residual cross block is exactly

\[
 B=X-AP_h=A(P_Q-P_h).                         \tag{1}
\]

Consequently,

\[
 B^*A^{-1}B=(P_Q-P_h)^*A(P_Q-P_h).           \tag{2}
\]

Thus `HRW` is not best viewed as six separate estimates for the
archimedean, pole, and prime-power sources.  It is a square-root-range bound
for the mismatch between the actual-zeta and reference Poisson extensions.

The matched finite data support this formulation: while the old Ritz floor
falls from `8.88e-7` to `1.33e-8`, the basis-invariant Poisson-defect ratio
stays in `[0.9044,1.1471]`.  This is high-precision non-interval Galerkin
evidence, not a continuum bound.

## 1. Exact variational structure

Let

\[
 J_Qv=(-P_Qv,v),\qquad J_hv=(-P_hv,v).
\]

The first vector is `Q`-orthogonal to the old space and the second is
`h`-orthogonal to it.  Their difference is old-supported:

\[
 J_hv-J_Qv=((P_Q-P_h)v,0).
\]

Since `J_Qv` is `Q`-orthogonal to every old vector,

\[
 \begin{aligned}
 v^*B^*A^{-1}Bv
 &=Q(J_hv-J_Qv,J_hv-J_Qv)\\
 &=Q(J_hv,J_hv)-Q(J_Qv,J_Qv).                \tag{3}
 \end{aligned}
\]

Writing

\[
 \Lambda_Q=D-X^*A^{-1}X
\]

for the finite `Q` Dirichlet-to-Neumann/Schur form, (3) becomes

\[
 B^*A^{-1}B=Q[J_h]-\Lambda_Q.                \tag{4}
\]

The correct continuum theorem target on a compact support slab is therefore

\[
 \boxed{
 \|A_L^{1/2}(P_{Q,L,\delta}-P_{h,L,\delta})v\|_2^2
 \le C_R\,\|J_{h,L,\delta}v\|_{L^2}^2 .
 }                                                   \tag{PD_R}
\]

This is exactly `HRW`, expressed as stability of Poisson maps.

Equivalently, in variational language,

\[
 Q(J_hv)-\inf_{u\in O_L}Q(u+J_hv)
 \le C_R\|J_hv\|_2^2.                       \tag{5}
\]

No enlarged-support positivity is assumed in this formulation.

## 2. What the source cancellation did and did not show

The residual was split exactly as

\[
 R=R_\infty+R_{\rm pole}+R_2+R_3+R_4+R_5,
\]

where

\[
 R_\infty=\operatorname{Arch}-(1+\log\pi)G-W_+
\]

and every prime-power term has its actual negative von Mangoldt weight.

At `M=40`, individual fixed-old-metric Ward ratios range from about `28` to
`1.76e6`, while their physical sum has ratio `1.05946`.  At `M=128`, the
largest isolated ratio is `4.61e7`, while the physical sum has ratio
`0.90443`.  Termwise absolute-value estimates are therefore unusable.

However, the most dramatic source statistic is largely tautological.  For a
`G`-normalized old eigenmode

\[
 A\phi_k=\lambda_kG\phi_k,
\]

(1) gives

\[
 \phi_k^*Bv
 =\lambda_k\langle\phi_k,(P_Q-P_h)v\rangle_G. \tag{6}
\]

This explains why the physical all-ones source vector is the near-null
direction of the low-mode source-scaling matrix.  The archimedean residual
was also defined by exact reconstruction of `Q-h`.  Hence:

- all-ones alignment `0.9997--0.9999` is primarily a consistency check;
- physical rank `1` among the 32 sign patterns mainly confirms signs and
  assembly;
- opposite-parity zero couplings are reflection symmetry;
- fixed-`A` source flips are not coherent modified zeta forms.

The non-tautological datum is that the right side of (6) displays the precise
square-root behavior needed by (2).  In representative lowest active-parity
modes, `|beta|/lambda` grows from roughly `136` to `223`, whereas
`|beta|/sqrt(lambda)` remains around `0.12--0.21`.  A coefficientwise or old
`G`-norm bound on `P_Q-P_h` is therefore likely overstrong; its `A`-energy is
the natural scale.

## 3. Matched finite evidence

Here `q` means collar modes per side, not conductor.  Every row keeps the old
and collar mesh scales comparable.

| `M` | `q` | `delta` | old Ritz floor | even ratio | odd ratio | Ward/Poisson ratio |
|---:|---:|---:|---:|---:|---:|---:|
| 40 | 1 | .32 | 8.878e-7 | 1.0595 | .7199 | **1.0595** |
| 48 | 2 | .40 | 5.672e-7 | 1.0380 | .8939 | **1.0380** |
| 80 | 1 | .16 | 8.918e-8 | .8113 | .9779 | **.9779** |
| 96 | 2 | .20 | 4.408e-8 | .9525 | 1.1471 | **1.1471** |
| 128 | 1 | .10 | 1.330e-8 | .9044 | .8894 | **.9044** |

The one-mode ladder decreases; the two-mode width refinement increases from
`1.0380` to `1.1471`.  The full tested range is modest, but the upward `q=2`
drift prevents any claim of asymptotic convergence or a uniform constant.
At `M=128` the two parity eigenvalues are close and the relative top eigengap
is only `1.66%`; individual extremizer morphology should not be extrapolated.

An independent `M=40` replay at 85 decimal digits agrees with the 55-digit
run in all 20 serialized digits of the principal invariants.  Algebraic,
Poisson, source reconstruction, and reflection errors are between roughly
`1e-64` and `1e-103` in the main runs.

## 4. The clean p=5 contact test

At `L5=2 log(5)`, the `n=5` old-old block is analytically zero.  Therefore
changing only the newly active `p=5` cross translation leaves the old metric
`A` unchanged and is cleaner than the other source ablations.

Replacing the contact atom by an equal-mass outward smear over
`[log(5),log(5)+delta/4]` changes the Ward ratio as follows:

| case | actual p5 atom | outward smear |
|---|---:|---:|
| M40/q1/.32 | 1.059 | 19.52 |
| M48/q2/.40 | 1.038 | 69.03 |
| M80/q1/.16 | .978 | 3.60 |
| M96/q2/.20 | 1.147 | 12.26 |
| M128/q1/.10 | .904 | 1.87 |

This is evidence that the exact threshold contact cancels a boundary-flux
singularity.  It is not a theorem that the arithmetic coefficient is an
optimizer; on some finite rungs a nearby coefficient gives a slightly smaller
ratio.

## 5. Literature synthesis and the most promising square root

The closest literature does not contain `(PD_R)`.

Connes--Consani prove that the **product** of the archimedean and finitely many
nonarchimedean local-factor ratios is quasi-inner, equivalently that its Hardy
off-diagonal/Hankel block is compact; no individual finite-prime ratio has
this property.  This is unusually well matched to the present evidence that
the completed source must be kept intact:
[Quasi-inner functions and local factors](https://arxiv.org/abs/2008.10974).

The resulting high-information candidate is to construct the semilocal
product

\[
 u_F=\rho_\infty\rho_2\rho_3\rho_5
\]

before logarithmically differentiating it into explicit-form sources, and
compare its compressed Hankel defect with the Poisson mismatch in (2).  A
successful bridge would expose an actual square root.  Qualitative compactness
is not enough: its norm must remain controlled as the old floor collapses.

Krein accelerant theory supplies another relevant shape.  The
Krein--Sobolev evolution of a truncated resolvent kernel is a rank-one
boundary law, making it a natural model for support propagation:
[Krein systems](https://arxiv.org/abs/0903.4778).

Suzuki's screw-function work connects the zeta Weil distribution to
continuous/nonlocal finite-interval operator realizations, unconditionally;
this is the most direct socket for translating the Poisson/DtN formulation
into an established zeta operator framework:
[Aspects of the screw function](https://arxiv.org/abs/2206.03682),
[Weil's quadratic form via the screw function](https://arxiv.org/abs/2606.09096).

For the independent reference side, the multiplier defining `h` is a complete
Bernstein function of `-Delta`.  Kwaśnicki--Mucha therefore provide a local
Dirichlet-to-Neumann extension and energy minimization principle, a concrete
tool for `NR_log` but not for the zeta arithmetic defect:
[Extension technique for complete Bernstein functions](https://arxiv.org/abs/1707.02475).

## 6. Next theorem/falsifier

The next action should not be another sourcewise inequality.  It should be a
normalization-exact **semilocal Hankel-to-Poisson bridge test**:

1. construct `u_F` for `F={infinity,2,3,5}` with the exact local-factor
   normalization;
2. form its Hardy/Sonin Hankel defect before taking logarithmic derivatives;
3. compress it to the old/collar geometry used here;
4. test whether `A^(1/2)(P_Q-P_h)` is a bounded boundary derivative or
   compression of that defect, modulo explicit pole/reference terms;
5. reject the route immediately if the finite matrices fail exact symmetry,
   source, or singular-subspace matching;
6. if they match, seek a quantitative compact-defect estimate uniform on a
   compact support slab.

The alternative analytic route is a completed-zeta Green/DtN kernel or Krein
accelerant identity proving `(PD_R)` directly.  Any route that first takes
absolute values of the individual pole, archimedean, or prime-power pieces is
ruled out by the finite data.

## Claim ledger

- source decomposition and equations (1)--(4): exact finite block algebra;
- Poisson/modal identity (6): exact finite generalized-eigenvector algebra;
- active mask `{2,3,4,5}`, weights, pole, parity, and transformations:
  independently audited against the existing assembler;
- five matched rows and the p5 perturbations: cutoff-free ordinary-`mpmath`
  Galerkin evidence, not interval-certified;
- 55/85-digit agreement at `M=40`: verified;
- `(PD_R)` / `HRW`: open;
- `NR_log`: open and logically independent;
- uniform propagation, a uniform zero-free strip, and RH: open.

## Artifacts

- driver: [`ward_source_extremizer_probe.py`](../src/ward_source_extremizer_probe.py)
- tests: [`test_ward_source_extremizer_probe.py`](../src/test_ward_source_extremizer_probe.py)
- consolidated data: [`zeta23_ward_poisson_defect_summary_2026_09_01.json`](zeta23_ward_poisson_defect_summary_2026_09_01.json)
- preflight: [`zeta23_hrw_source_audit_preflight_v1.json`](context/zeta23_hrw_source_audit_preflight_v1.json)
