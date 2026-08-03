# Boundary Weyl inertia checkpoint

Status: the collapsing relative Poincaré margin has been replaced by robust
signature data; the analytic sign theorem remains open, 2026-08-01.

## 1. Constrained Euler--Lagrange equation

Let `T_a` be the pole-free completed incidence operator and let

`M_a : R^2 -> H_a`

have columns `exp(x/2)` and `exp(-x/2)`.  A normalized critical point on the
relative subspace `ker(M_a^*)` satisfies

`T_a f = lambda f + M_a eta`, `M_a^* f = 0`.

At `lambda=0`, if `T_a` is invertible, then

`f=T_a^(-1) M_a eta`

and the moment constraint becomes

`K_a(0) eta=0`,

where

`K_a(z)=M_a^* (T_a-z)^(-1) M_a`

is the `2 x 2` boundary Weyl matrix.  Hence a relative zero mode is equivalent
to singularity of `K_a(0)`.  Both directions of this Schur reduction are now
kernel-checked abstractly in `RHBridge.BoundaryWeylReduction`.

Reflection symmetry changes the boundary coordinates to

`c=cosh(x/2)`, `s=sinh(x/2)`

and gives exactly

`K_a(0)=diag(k_even(a),k_odd(a))`.

## 2. Inertia reduction

Haynsworth inertia additivity gives, in every finite Galerkin compression,

`inertia(T_a) = inertia(T_a restricted to ker M_a^*) + inertia(K_a(0))`.

Therefore the two statements

1. `T_a` has exactly one negative direction and no kernel;
2. `k_even(a)<0<k_odd(a)`;

imply strict positivity of the relative restriction.  Conversely, given the
observed one-negative-direction property of `T_a`, relative positivity forces
the same boundary signature.

This replaces control of a tiny lowest eigenvalue by integer-valued inertia
and two order-one scalar signs.

## 3. Separation from the knife edge

The absolute pole-completed parity blocks are

`Q_even=T_even+2 c c^*`,

`Q_odd =T_odd -2 s s^*`.

Their rank-one thresholds are

`k_even=-1/2`, `k_odd=1/2`.

Thus the tiny unrestricted Weil margins measure distance to these stronger
thresholds.  Relative positivity needs only

`k_even<0<k_odd`,

which leaves an order-one buffer.  This explains how the restricted Weil
criterion can be numerically well conditioned at the signature level even
though the absolute form sits almost on the boundary of positivity.

## 4. Stress test

`src/boundary_weyl_inertia.py` independently computes all three inertias and
the parity Weyl scalars.  Across the principal supports, dimensions `12--20`,
and additional points straddling prime activations, every tested matrix has

`inertia(T)        = (1 negative, 0 zero, m-1 positive)`,

`inertia(K)        = (1 negative, 0 zero, 1 positive)`,

`inertia(relative) = (0 negative, 0 zero, m-2 positive)`.

At dimension `12`:

| support | `k_even` | `k_odd` | `det K` |
|---:|---:|---:|---:|
| 1.750 | `-0.500013` | `0.406163` | `-0.203087` |
| 2.485 | `-0.500000` | `0.499887` | `-0.249943` |
| 2.996 | `-0.500000` | `0.499997` | `-0.249999` |
| 3.555 | `-0.500000` | `0.499999` | `-0.250000` |
| 4.040 | `-0.500000` | `0.500000` | `-0.250000` |

The cross entry is below `3e-16`, as parity predicts.  The same signatures
survive scans immediately before and after the activations near supports
`2.2`, `2.8`, and `3.2`.

These are diagnostics, not proofs.  The approach of the scalars to
`(-1/2,1/2)` is the same knife-edge phenomenon already seen in the absolute
form; it must not be mistaken for an exact unconditional identity.

## 5. Bayesian meaning

This checkpoint validates the boundary-Weyl reformulation as a proof target:
it removes numerical ill-conditioning from the proposition that must be
proved.  It does not yet make the signs automatic.  A continuous family can
change inertia only when `T_a` or `K_a(0)` becomes singular, so a bare
continuity argument would again ask for the nondegeneracy being sought.

The next analytic target is now sharply scalar:

> Prove that the even boundary response is negative and the odd boundary
> response is positive for every support, while the pole-free incidence
> operator has negative index one.

Poisson summation is useful only if it determines these signs before invoking
the completed Weil form.  Deriving merely the stronger near-equalities to
`+/-1/2` from positivity would be circular.

The promising route is to express `k_even` and `k_odd` as Dirichlet-to-Neumann
data of the relative Poisson/Sonin problem.  A sign follows from orientation
of the boundary flux, whereas its distance to `+/-1/2` is allowed to collapse.
This is the precise boundary-Wronskian theorem to attempt next.
