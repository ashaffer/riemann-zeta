# Full incidence-kernel cycle audit

Status: globally closed cycles alone and the named boundary-ray and orthogonal
return-free families are pruned; admitting the complete cycle space recovers
exactly the Weil Schur condition.  Mixed tilted proper subspaces remain open,
2026-08-01.

## 1. Exact three-channel decomposition

In the finite-dimensional model, at one support enlargement write

`B_U h=(A h,q V h)`, `B_W k=(X k,Y k)`,

where `V*V=I`, `q^2=D_b-D_a>0`, `S=A*A`, and `S_0=S+q^2 I`.
The old Weil operator is `Q_a=S_0-D_b I`.

Assuming the displayed Gram operators are invertible, the kernel of the old
divergence splits orthogonally into

`ker(B_U*) = return cycles + ker(A*) + ker(V*)`.

One return parametrization is

`R z=(A z,-q^-1 V S z)`, `R*R=q^-2 S S_0`.

The corresponding collar-response capacities are

`G_return=(q A*X-S V*Y)* (S S_0)^-1 (q A*X-S V*Y)`,

`G_old=X* P_(ker A*) X`,

`G_shell=Y* P_(ker V*) Y`.

Their sum is exactly

`G_full=B_W* P_(ker B_U*) B_W`

`      =B_W*B_W-B_W*B_U S_0^-1 B_U*B_W`.

This identity is verified numerically to operator-norm error below `4.2e-15`.
An infinite-dimensional version requires the corresponding closed-range or
Moore--Penrose hypotheses; no such continuum assertion is being smuggled into
this finite decomposition.

Put `L=S_0^-1 B_U*B_W`.  For any selected orthogonal cycle family with
capacity `G_J`, the exact contractive-dual requirement is

`G_J >= H := D_b [I+L* S_0 Q_a^-1 L]`.

The inverse-old-gap term is forced by the off-diagonal blocks of `C*C`; a raw
test against `D_b I` is insufficient.  With all three channels, `G_full>=H`
is algebraically exactly the Schur complement of the new Weil form.  This is
the point where the construction becomes circular.

## 2. Global translation cycles have no response

Let `nabla_h=T_h-I`.  Commutativity gives the plaquette cycle

`(K_(h,k) phi)_h=c_h^-1/2 nabla_k* phi`,

`(K_(h,k) phi)_k=-c_k^-1/2 nabla_h* phi`,

and hence

`B* K_(h,k) phi`

` =nabla_h* nabla_k* phi-nabla_k* nabla_h* phi=0`.

Antisymmetrically smeared continuum plaquettes and prime/Mobius closed chains
obey the same identity.  Because they are closed for the full divergence,
they pair to zero with collar gradients as well as old gradients.  They add no
dual-frame capacity when used alone.

That last qualification matters.  A zero-response vector can improve a
responsive family after tilting by cancelling an inefficient norm component.
For example, if the response vector is `e_1`, the line spanned by
`e_1+e_2` has capacity `1/2`, while adjoining the invisible vector `e_2`
produces a span containing `e_1` and hence capacity `1`.  The closure identity
therefore rules out plaquettes as standalone responders, not every mixed
plaquette--boundary construction.

Lean formalizes this commuting-cycle closure and the resulting invisibility in
`RHP2Bridge.IncidenceCycleObstruction`.

## 3. Explicit boundary-relative cycles are too small

For collar width `ell=b-a`, delay `h>=ell`, and right/left collar pieces
`y_+,y_-`, the outward ray

`K_h y=T_h y_+-y_-`

has old divergence zero and collar response `sqrt(c_h) I`.  Summing all such
channels gives the explicit capacity

`A_ray = integral_(2 ell)^infinity`

`          exp(-t/4)/(2(1-exp(-t))) dt`

`        + sum_(n old, log n>=ell) Lambda(n)/sqrt(n)`.

Across the four principal transitions, `A_ray/D_b` is approximately

`0.364, 0.433, 0.400, 0.418`.

Even an optimistic opposite-boundary chain raises these only to about
`0.593--0.661`.  Thus direct escape paths miss the unamplified threshold by a
large factor.  Globally closed plaquettes supply no response on their own;
plaquette-assisted tilted spans are not decided by this ray estimate.

The larger exterior-edge family is bounded above by `G_old`.  Consequently
every construction contained in the orthogonal old-fresh plus shell-fresh
summand is bounded by `G_old+G_shell`.  A subspace tilted through the return
channel need not obey that bound even if it is still a proper subspace of the
full kernel.

## 4. The maximal return-free family crosses below threshold

Raw degree floors initially looked favorable: at coarse resolution
`(G_old+G_shell)/D_b` lies between `1.025` and `1.074`.  The amplified test
changes the result.

For the transition `2.485 -> 2.996`:

| old/collar hats | cutoff | `lambda_min(H^-1/2 (G_old+G_shell) H^-1/2)` | full-cycle ratio |
|---:|---:|---:|---:|
| `21/6` | `600` | `1.010479` | `1.011072` |
| `31/10` | `1200` | `1.004062` | `1.004684` |
| `61/20` | `1200` | `1.001722` | `1.002397` |
| `121/40` | `1600` | `1.000170` | `1.000764` |
| `181/60` | `1600` | `0.999819` | `1.000420` |
| `181/60` | `2000` | `0.999828` | `1.000430` |

The crossing is about seventeen times the observed cutoff drift.  The old and
full Weil gaps remain positive and of the expected scale in both final runs.
This is strong numerical falsification of the maximal return-free criterion,
not a certified continuum counterexample.

By capacity monotonicity this simultaneously prunes rays, exterior edges,
selected old-edge cycles, and every smaller family contained in that
orthogonal return-free summand in this finite section.  Adding the return
channel is essential for the final roughly
`6e-4` crossing, but adding all of it gives `G_full`, the exact Weil Schur
condition.

The first refined crossing at `2.485 -> 2.996` had only one negative
generalized mode, and that individual finite section does admit a
noncircular scalar Schur certificate.  In an `H`-orthonormal generalized
eigenbasis, put

`mu=1-lambda_1=1.715433075e-4`,

`gamma=lambda_2-1=1.283707232e-3`.

On the negative mode the return block has diagonal
`r=6.017467205e-4`, while its operator-norm cross block into the positive
sector is `c=1.164247996e-4`.  Discarding the positive--positive return block
still leaves the scalar Schur reserve

`(r-mu)-c^2/gamma = 4.196443590e-4 > 0`.

Thus return repairs this representative index-one defect without appealing
to the exact full-cycle ratio or to any quantitative lower bound from the
positive--positive return block.  This is a genuine local certificate, but
not a uniform path: the index-one feature does not persist across the later
transitions.

| transition | old/collar hats | negative modes of `G_old+G_shell-H` | two lowest generalized ratios | full ratio |
|---:|---:|---:|---:|---:|
| `2.485 -> 2.996` | `181/60` | `1` | `0.999828, 1.001284` | `1.000430` |
| `2.996 -> 3.555` | `121/40` | `2` | `0.997973, 0.999828` | `1.000123` |
| `2.996 -> 3.555` | `181/60` | `3` | `0.997762, 0.999528` | `1.000081` |
| `3.555 -> 4.040` | `121/40` | `2` | `0.999029, 0.999478` | `1.000167` |
| `3.555 -> 4.040` | `181/60` | `2` | `0.998834, 0.999358` | `1.000061` |

At `121/40` the first two negative modes have opposite parities.  The defect
index can therefore grow under refinement and is not confined to one parity.
An index-one Feshbach reduction is not a uniform surviving target.

## 5. Translation geometry alone cannot force the stronger target

There is also an exact finite countermodel on `Z/4`.  With shifts `2` and `1`
and normalized vectors

`u=(-2,1,-1,2)/sqrt(10)`,

`v=(-1,-2,2,1)/sqrt(10)`,

the full shifted block is

`[[3/10,3/5],[3/5,19/10]]`,

which is strictly positive (`det=21/100`).  Its return-free fresh capacity is
`40/19`, below the amplified threshold `351/70`; the full capacity `40/7`
passes.  Thus commuting translations, shell isometry, and strict positivity
do not make the proper-cycle inequality automatic.

Lean proves the scalar amplified criterion, positivity of this block, and both
capacity comparisons in `RHP2Bridge.IncidenceCycleObstruction`.

Nor is low defect index forced abstractly.  A reflection-preserving model on
`Z/6` has a strictly positive full block but a negative return-free defect in
an even, mean-zero sector.  Orthogonal direct sums give arbitrarily many
negative directions while preserving commuting translations, parity, shell
isometry, strict positivity, and an ambient codimension-two moment subspace.
Thus the observed defect index must be quantitatively zeta-specific; parity
and the two moments provide no uniform rank bound.

The only general inertia statement is the rank bound.  If
`M=G_old+G_shell-H`, `R=G_return`, and `M+R>=0`, then
`n_-(M)<=rank(R)`: otherwise a negative subspace of dimension greater than
`rank(R)` would meet `ker(R)` nontrivially, contradicting positivity of
`M+R`.  The direct-sum countermodel makes this sharp at arbitrary rank.  This
does not determine the zeta-specific defect index; it only explains why
parity and moment codimension cannot force it to be one.

## 6. Verdict

The named cycle families have reached a sharp boundary:

1. globally closed arithmetic cycles are invisible when used alone;
2. explicit boundary rays are much too weak on their own;
3. the maximal orthogonal old-fresh plus shell-fresh reservoir fails after
   amplification in stable but uncertified finite Galerkin sections;
4. its negative index grows with support/refinement, so it does not leave a
   scalar residual theorem;
5. the full three-channel reservoir succeeds exactly when the Weil Schur
   complement succeeds.

The unrestricted cycle space therefore renames, rather than solves, Weil
positivity.  But the audit does **not** rule out a mixed tilted proper
subspace.  For an orthogonal proper family `J`, its exact remaining condition
is

`E_J := G_full-G_J <= G_full-H`.

The right side is tiny on the critical modes, so a viable family must preserve
those directions very accurately; it may still discard large capacity on
surplus modes or use invisible cycles to cancel norm.  Constructing or
falsifying such a zeta-specific tilted family is the sole surviving version of
this pathway.  The exact countermodels show only that commuting translations,
parity, shell isometry, moment codimension, and full positivity do not force
it automatically.
