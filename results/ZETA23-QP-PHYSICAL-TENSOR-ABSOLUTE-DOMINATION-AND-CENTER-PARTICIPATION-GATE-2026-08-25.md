# QP physical tensors: absolute mask domination and the first center-participation obstruction

**Date:** 2026-08-25  
**Erratum / superseding audit:** Section 3's center-convolution expression is
a valid positive upper relaxation, but it is **not** the corrected exact
target and need not satisfy the desired bound.  The later finite and abstract
audit in
`ZETA23-QP-CENTER-FOURIER-TIGHT-FRAME-IDENTITY-AND-CONVOLUTION-RELAXATION-NOGO-2026-08-25.md`
shows that grouping by additive center creates false cross-row coherence.
The exact remaining target is instead

```text
||H(conj(z) tensor z)||_2^2 << D q^o(1) ||z||_2^4,
```

equivalently the ungrouped row-pair frame potential.  Every statement below
about absolute domination of literal deletion masks remains valid; claims
that the grouped center-vector convolution is the remaining theorem are
superseded by this erratum.

**Verdict:** every literal physical or post-peeling **deletion** in the
fourth-trace expansion is harmless under entrywise absolute values.  The
color-pair coefficient remains

```text
xi_(c,c')=conj(z_c)*z_(c'),
||xi||_2^2=||z||_2^4.                                 (0.1)
```

Thus a completely bounded factorization theorem for the deletion mask is
not needed if one proves the full positive majorant.  This includes the
local broad/error-labelled mask and the dyadic high-completion masks.

Scalar self-RSR still does not automatically prove that positive majorant.
The first exact obstruction is the common-carrier selector which appears
when the second physical tensor is unfolded into completion pairs.  It
turns one scalar rank-one coefficient into

```text
W_(i,j)=1_(b(i)=b(j))*x_i*x_j
       =sum_b x_i*1_(b(i)=b) x_j*1_(b(j)=b).         (0.2)
```

This is a sum of rank-one center blocks, not one globally factorable scalar
pair weight.  Equivalently, restoring the physical completion label repeats
`xi_gamma` once for every incidence `(alpha,gamma)` and changes its norm by
the exact color-pair participation degree.  A fixed-center scalar self-RSR
does not control the coherent sum over centers.

This identifies why the scalar-convolution route is not lossless.  It does
not make the resulting center-vector convolution the correct remaining
theorem: the erratum above supersedes that conclusion.  The faithful target
keeps the ungrouped row-pair output and the rank-one colour tensor.

## 1. First tensor: the raw fourth trace

Write

```text
A_z(a,b)=sum_c z_c*kappa(a,b,c),
kappa(a,b,c)=1_(|8abc-q^3|<=qD).                     (1.1)
```

The fourth Schatten mass is

```text
sum_(a1,a2,b1,b2) sum_(c11,c12,c21,c22)
 kappa_11*kappa_12*kappa_21*kappa_22
 conj(z_c11)*z_c12*z_c21*conj(z_c22).               (1.2)
```

Let `M` be any physical sector or post-peeling deletion depending jointly
on all row, carrier, color, residual, determinant, tangent, and block
labels.  Its only relevant property here is

```text
|M|<=1.                                               (1.3)
```

Taking absolute values term by term in (1.2) gives

```text
|Q_M(z)|
 <=sum kappa_11*kappa_12*kappa_21*kappa_22
       |z_c11 z_c12 z_c21 z_c22|
 =tr((A_|z|^* A_|z|)^2).                             (1.4)
```

The coefficient norm has not changed:

```text
|| |z| ||_2=||z||_2.                                 (1.5)
```

Therefore every literal rectangle deletion is dominated before any
harmonic, stationary, or ANOVA transformation.  Non-positive-definiteness
of `M` is irrelevant to (1.4).

This observation is useful only if the full positive expression on the
right of (1.4) can be bounded sharply.  It cannot be combined for free with
cancellation proved only after a transform: taking (1.4) first deliberately
forgets all cancellation among the deleted pieces.

## 2. Second tensor: exact row-pair/color-pair factorization

Let

```text
alpha=(a_1,a_2),       gamma=(c_1,c_2),              (2.1)
```

and define the ordered wedge incidence

```text
H_(alpha,gamma)
 =sum_b kappa(a_1,b,c_1) kappa(a_2,b,c_2).           (2.2)
```

Physical pair uniqueness makes (2.2) a `0/1` entry and makes its carrier
`b` unique when it is one.  Put

```text
xi_gamma=conj(z_c1)*z_c2.                            (2.3)
```

Then direct expansion gives the exact row-Gram identity

```text
G_alpha
 :=sum_b conj(A_z(a_1,b))*A_z(a_2,b)
 =(H xi)_alpha.                                      (2.4)
```

On the full ordered color-pair space,

```text
sum_gamma |xi_gamma|^2
 =(sum_c |z_c|^2)^2=||z||_2^4.                      (2.5)
```

This is the second occurrence of the same rank-one factorization.  It is
not destroyed by passing from the raw trace to the physical incidence
operator.

Now allow a mask before the common row-pair is summed:

```text
N_(alpha,gamma,gamma'),       |N|<=1.                (2.6)
```

It includes:

* broad/narrow rectangle deletion;
* tangent-packet peeling;
* all-distinct and orientation restrictions;
* residual-block deletion; and
* dyadic restrictions on the common-completion multiplicity after these
  are pulled back to their common row-pair witnesses.

Termwise absolute values prove

```text
|sum_(alpha,gamma,gamma')
  conj(xi_gamma) N_(alpha,gamma,gamma')
  H_(alpha,gamma)H_(alpha,gamma') xi_gamma'|

 <=sum_alpha (sum_gamma H_(alpha,gamma)|xi_gamma|)^2
 =||H |xi|||_2^2.                                    (2.7)
```

If a dyadic mask is stated only on

```text
m(gamma,gamma')=(H^*H)_(gamma,gamma'),              (2.8)
```

then its kernel is

```text
1_(K<=m<2K)*m(gamma,gamma')<=m(gamma,gamma'),        (2.9)
```

and (2.7) applies directly.  Hence the thresholded `H^*H` need not be
positive semidefinite: it is absolutely dominated by the unthresholded
positive kernel while the coefficient (2.3) remains factorable.

The same proof is equation (8.3) of the prior RSR bridge in literal
indices.  For the local error-labelled operator, pair states
`pi=(i,j),rho=(k,l)` have

```text
w_pi=z_i z_j,
K_br(pi,rho)
 =1_(n(pi)=n(rho))*1_(broad and unpeeled).           (2.10)
```

Thus

```text
|<w,K_br w>|
 <=sum_S (sum_(n(i,j)=S)|z_i z_j|)^2.               (2.11)
```

At one fixed center this is exactly an absolute scalar self-convolution
energy.  No cb mask theorem is needed there.

## 3. Where scalar factorization first fails

Formula (2.7) is not yet a scalar convolution with the original input norm.
For each physical carrier `b`, define

```text
f_b(a)=sum_c kappa(a,b,c)*|z_c|.                    (3.1)
```

Pair uniqueness makes the sum in (3.1) contain at most one color in each
cell.  Equations (2.2)--(2.7) give

```text
||H|xi|||_2^2
 =sum_(a_1,a_2)
    (sum_b f_b(a_1)f_b(a_2))^2.                     (3.2)
```

All terms are nonnegative.  Grouping ordered row pairs by the additive
completion `S=a_1+a_2` therefore gives the valid relaxation

```text
||H|xi|||_2^2
 <=sum_S (sum_b (f_b*f_b)(S))^2
 =||sum_b f_b*f_b||_2^2.                            (3.3)
```

The right side of (3.3) is **not** the self-convolution of one scalar
sequence.  On edge-expanded point indices `i=(a,b,c)`, its pair coefficient
is exactly

```text
W_(i,j)
 =1_(b_i=b_j)*|z_(c_i)z_(c_j)|.                     (3.4)
```

For one fixed `b`, (3.4) is rank one and scalar self-RSR applies.  Globally,

```text
W=sum_b x_b tensor x_b,                              (3.5)
```

where the `x_b` have disjoint center labels.  Its rank is the number of
nonempty centers.  Dropping `1_(b_i=b_j)` restores a scalar rank-one weight,
but it also adds every cross-center pair and forces the point coefficient
norm

```text
sum_(a,b,c) kappa(a,b,c)|z_c|^2
 =sum_c deg(c)|z_c|^2,                               (3.6)
```

which can be `D||z||_2^2`.  This is not a lossless transfer.

The same obstruction appears without expanding all edges.  To attach a
completion coordinate to a color pair `gamma`, replace `xi_gamma` by one
copy on every incidence `(alpha,gamma)`.  Its squared norm becomes

```text
sum_(alpha,gamma) H_(alpha,gamma)|xi_gamma|^2
 =sum_gamma deg_H(gamma)|xi_gamma|^2,                (3.7)
```

instead of (2.5).  A one-column star of degree `r` changes the norm by
exactly the factor `r`.  High-completion colors are precisely columns for
which such participation can be polynomial.

Equations (3.4) and (3.7), not the pair-of-pair deletion `N`, are the first
exact nonfactorable/normalization obstruction.

## 4. Why per-center scalar self-RSR does not aggregate

Suppose the hereditary scalar theorem gives, for every fixed center,

```text
||f_b*f_b||_2^2
 <<sqrt(D U_b) q^o(1)||f_b||_2^4.                   (4.1)
```

It controls the diagonal terms in

```text
||sum_b f_b*f_b||_2^2
 =sum_(b,b') <f_b*f_b,f_b'*f_b'>.                   (4.2)
```

It supplies no decay for `b!=b'`.  Identical legal rows repeated at `L`
centers make the left side of (4.2) equal `L^2` times one-center energy,
whereas the diagonal sum is only `L` times that energy.  This is the same
completion-repetition obstruction found after the fixed-lattice Airy
theorem.

One can retain the selector in (3.4) by using the Hilbert feature `e_b`.
Its Gram factorization has norm one, so this particular mask has no
`gamma_2` loss.  What results is a Hilbert-valued/center-vector restriction
problem.  Scalar self-RSR is not stable under that replacement without a
new vector theorem.

## 5. Superseded sufficient relaxation and the exact target

The following is a sufficient but generally stronger positive theorem:

> **Center-coherent self restriction (CCSR).**  Uniformly under the physical
> shell, all admissible product-band deletions, and the Fejer dyadic masks,
>
> ```text
> ||sum_b f_b*f_b||_2^2
>  <<D q^o(1)||z||_2^4,                              (5.1)
> ```
>
> with `f_b` defined by (3.1), with the sharper mask-dependent version when
> needed before the Fejer sum.

By (1.4), (2.7), and (3.3), (5.1) controls every literal pair-of-pair
deletion at once.  It is **not equivalent** to the rank-one color
restriction

```text
||H(conj(z) tensor z)||_2^2
 <<D q^o(1)||z||_2^4.                                (5.2)
```

Equation (5.2), not (5.1), is the exact remaining fourth-trace target.  The
unmasked operator-norm estimate `||H||^2<<D` is stronger than (5.2), because
(5.2) tests only rank-one color-pair tensors.  The later Kraus audit rewrites
(5.2), with no loss, as `Phi:S1->S2` or `Phi^*:S2->Sinf`.

This yields the corrected logical picture:

```text
literal post-peeling deletion mask needs cb control:       NO;
absolute domination retains xi=zbar tensor z:              YES;
fixed-center broad kernel controlled by scalar self-RSR:    YES;
all centers controlled by separate scalar self-RSR bounds: NO;
first obstruction: same-center pair selector/participation: EXACT;
its Hilbert Gram norm:                                      1;
remaining cost: center/output Bessel multiplicity:          OPEN;
CCSR / grouped center convolution used as target:           NO;
ungrouped rank-one H / Kraus dual bound:                    OPEN;
sharp four-cycle bound:                                     NOT PROVED.
```

## 6. Reproducibility

The exact incidence identity, arbitrary bounded-mask domination, rank-one
color-pair norm, participation-star loss, and same-center rank are replayed
in

```text
src/qp_pre_stationary_fejer_completion_bundle.py
src/test_qp_pre_stationary_fejer_completion_bundle.py
```
