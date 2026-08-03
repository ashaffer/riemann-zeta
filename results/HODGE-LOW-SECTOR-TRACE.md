# Hodge low-sector boundary trace checkpoint

**Superseded verdict (2026-08-02):** the selected hat-space low contraction is
not a viable full-domain target.  Cutoff-free piecewise Legendre functions
with admissible endpoint jumps give a stable negative numerical value for the
complete strengthened Hodge form; see
`PLAIN-LEGENDRE-HODGE-FALSIFIER.md`.  The algebraic two-mode reduction below
remains correct for its chosen finite split, but the propagation route it was
meant to close is pruned.

Status: the Hodge return row now has an exact eigenmode formula, and the
hardest residual has been reduced to one explicit `2 x 2` principal-minor
inequality in the odd low sector.  The reduction is noncircular, but the
remaining determinant has not been proved.  Numerically it is positive and
drifts toward zero under refinement.  Thus no RH or all-event positivity
claim follows from this checkpoint.

## 1. Continuum incidence normalization

Let

`I=[-r,r]`, `J=(-R,-r) union (r,R)`

be the old interval and the consecutive-event collar.  For an active prime
power `m`, put

`ell_m=log(m)`, `c_m=2 Lambda(m)/sqrt(m)`.

The archimedean jump density in the present Fourier convention is

`nu(t)=exp(-t/2)/(1-exp(-2t))`, `t>0`.

On the relative space, where both exponential moments vanish, the completed
old incidence energy is

`E_a(f,g)`

` = integral_(t>0) nu(t) <f-T_t f,g-T_t g> dt`

`   + sum_(old m) (c_m/2)<f-T_(ell_m)f,g-T_(ell_m)g>`.

If `D_a` is its scalar degree, the old Weil operator is

`Q_a=S-D_a I`, `S=E_a|_I`.

For the unique new event `N`, write `d=c_N=q^2` and `ell=log N`.  The event
incidence form is the single positive difference square with coefficient
`d/2`.

## 2. Explicit old--collar trace

Extend an old vector `v` by zero.  Against a collar vector, the old-place and
event cross rows have the following representatives on `J`:

`a_v(x) = - integral_I nu(|x-y|) v(y) dy`

`         - (1/2) sum_(old m) c_m`

`             [v(x-ell_m)+v(x+ell_m)]`,

`e_v(x) = -(d/2)[v(x-ell)+v(x+ell)]`.

The combined arithmetic boundary row is

`r_v=a_v+e_v`.

The pole cross row is exactly zero here, not estimated: every old and
moment-corrected collar vector separately annihilates both pole moments.  The
pole is nevertheless essential in selecting this codimension-two relative
space.

There is one useful exact smoothing cancellation.  For `x>r`,

`nu(x-y)=sum_(k>=0) exp(-(2k+1/2)x) exp((2k+1/2)y)`.

The `k=0` term vanishes because

`integral_I exp(y/2)v(y)dy=0`.

The analogous leading term on the left vanishes by the other moment.  This
removes the longest-range gamma tail, but it does not remove the near-boundary
singularity or the shifted prime traces.

## 3. Exact Hodge eigenmode identity

Let

`Q_a v_i=lambda_i v_i`, `s_i=D_a+lambda_i`,

and put

`tau_i=sqrt(s_i/(s_i+d))`.

The return construction gives the Hodge trace row

`t_i = tau_i(1-tau_i)`

`      * [q^-1 e_i-q s_i^-1 a_i]`.

Algebraically this is exactly

`t_i = (1-tau_i)/(q tau_i)`

`      * [e_i-d(s_i+d)^-1 r_i]`.                 (H)

Lean proves (H) from only `q^2=d`,
`tau_i^2(s_i+d)=s_i`, and `r_i=a_i+e_i`.  There is no sign or Weil-positivity
hypothesis.  Formula (H) is informative: in the low sector, Hodge smoothing
adds a small event-trace correction to the same combined boundary row whose
ordinary Schur cost already controls the problem.  It does not create the
observed prime--gamma cancellation.

## 4. Exact residual after high-sector elimination

Start with the modified enlarged block

`[[Q_a,X],[X*,C-T*T]]`.

Assume a chosen high old sector has been Schur-eliminated, and spend the
complete Hodge trace cost in the collar block.  Let `Dhat_o>0` be the remaining
odd collar form.  In the hard-event Galerkin sections below, the first four old
modes contain two odd modes, indexed `1` and `3`.  Define

`h_ij=<r_i,Dhat_o^-1 r_j>`.

The remaining odd contraction is exactly the positivity of

`[[lambda_1-h_11, -h_13],[-h_13,lambda_3-h_33]]`.

Since the first diagonal is strictly positive in the diagnostics, this is
equivalent to the two scalar conditions

`lambda_1-h_11>0`,

`Delta_odd := (lambda_1-h_11)(lambda_3-h_33)-h_13^2 >= 0`.       (O)

Lean proves the general equivalence between the two-mode contraction and
(O).  It does **not** assert (O) for the zeta traces.  Proving `Delta_odd>=0`
from the explicit functions in Section 2 is the precise remaining low-sector
theorem.

## 5. Hard-event data

The table uses the collar metric after eliminating old modes `j>=4`; the
omitted low Hodge trace changes the largest eigenvalue only in approximately
the ninth decimal place.  Put

`G_ij=h_ij/sqrt(lambda_i lambda_j)`.

| old degree | odd eigenvalues | `G` | `lambda_max(G)` | `det(I-G)` |
|---:|---:|:---|---:|---:|
| `121` | `1.28545e-6`, `3.04158e-3` | `[[.0882543,-.0347203],[-.0347203,.9923887]]` | `.99372005` | `.00573408` |
| `181` | `3.42180e-7`, `2.89616e-3` | `[[.3248655,.0169649],[.0169649,.9953450]]` | `.99577399` | `.00285494` |
| `241` | `1.82318e-7`, `2.81730e-3` | `[[.5964163,.0119493],[.0119493,.9958589]]` | `.99621609` | `.00152848` |

At degree `121`, the normalized Hodge-trace Gram has largest scale about
`1.87e-5`, whereas the combined-cross contraction is `.99372005`.  The
decisive entry is therefore the boundary dual norm of mode `3`, not the
Hodge loss.

The determinant decreases roughly like the inverse square of the displayed
Galerkin degree (`N^2 det(I-G)` is approximately `84, 94, 89`).  This is
evidence for a saturated non-strict continuum contraction, not for a uniform
strict gap.  A proof therefore cannot spend a resolution-independent epsilon
in this block.

For that mode, in the same high-eliminated collar dual metric,

| component | dual norm |
|:---|---:|
| archimedean | `.985149` |
| old-prime adjacency | `.980392` |
| new event adjacency | `.0627924` |
| combined `arch-oldPrime-event` | `.0549403` |
| `sqrt(lambda_3)` | `.0551505` |

The archimedean and old-prime rows have correlation `.996825`.  Their large
near-parallel pieces cancel, leaving a combined trace almost exactly as large
as the old eigenvalue budget permits.  This is genuine event-specific
structure, but it is an approximate eigenmode continuation phenomenon rather
than a pointwise kernel identity.

## 6. Euler--Lagrange boundary and circularity audit

The weak old eigen-equation says, on `I`,

`L_a v_i=lambda_i v_i+alpha_i exp(x/2)+beta_i exp(-x/2)`.

It determines the compressed residual modulo the two moment directions.  It
does not determine the exterior row `r_i|_J`.  The gamma part of that row is a
nonlocal integral, while the prime parts are shifted traces with kink
locations.  They cannot be equated pointwise by algebra; their observed
alignment uses the special old eigenfunction.

Consequently none of the following proves (O):

1. the old weak Euler--Lagrange equation alone;
2. the functional-calculus bound on `1-tau`;
3. positivity of the unshifted incidence squares;
4. collar positivity before old-variable minimization.

Assuming an exterior continuation inequality strong enough to imply (O)
would assume precisely the remaining mixed positivity.  A noncircular proof
must estimate the explicit prime--gamma trace in Section 2 and establish the
displayed two-mode determinant with a reserve large enough to absorb (H).

## 7. Formal artifacts

Lean files:

- `RHBridge/HodgeLowSector.lean`;
- `RHBridge/HodgeLowSectorAudit.lean`.

The audit reports only the standard foundational axioms
`propext`, `Classical.choice`, and `Quot.sound` for:

- `scalar_eigenmode_hodge_trace_identity`;
- `two_mode_psd_iff_determinant`;
- `two_mode_contraction_iff_principal_minor`.

Finite-section diagnostics are produced by `src/hodge_sector_scan.py`; they
are not premises of the Lean theorems.

The generic high-tail theorem does not prove that the continuum low sector is
four-dimensional.  With only raw operator norms it may leave many more modes;
the two-mode reduction above is exact inside the selected finite Galerkin
split and guides the continuum target, but it is not a spectral-dimension
theorem.
