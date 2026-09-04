# QP sharp four-cycle attack: the regularized two-index spectral gate

**Date:** 2026-08-24  
**Status:** the sharp `D^(1+o(1))` fourth-trace bound is **not proved**.
The attack eliminated several false proof architectures and produced two
precise surviving routes: a regularized two-index square function and a later,
more elementary Walsh/defect-fan Carleson theorem.

## 1. Target

After the already proved repeated-node, parabolic, tangent-packet, and
prime-power chart estimates, the unresolved sector is the balanced broad
two-star operator.  In its physical form, for a shell-supported coefficient
set `A`, put

```text
T_(b,c)=sum_(a in shell) 1_(|8*a*b*c-q^3| <= q*D),
T^o=T-kappa*J.
```

The sharp input for the remaining balanced broad face is the selected-shell
BDH estimate

```text
||T^o z||_2^2 << D*q^o(1)*||z||_2^2.                 (1.1)
```

At the critical flat support `M=D^(15/8)`, (1.1) supplies exactly the
missing `D^(1/8)` occupancy saving on that face.  A promotion of the *entire*
fourth trace also needs a written compatibility bridge to the pair-incidence
peeling used for the remaining parabolic `71/64` and singleton `137/128`
terms.  That bridge is not proved in the reports cited here.

## 2. What the attack proved

### 2.1 Moving Farey congruences are not the obstruction

On every coprime gcd stratum, multiplicative character Fourier transform
diagonalizes the moving fan congruence isometrically.  Mellin inversion then
removes the remaining smooth `c`-dependence.  The resulting modulus character
is exactly the nebentypus in the opposite-cusp formula of Kiral--Young.
Oldclass transport is unitary, and every nonzero lower DFI block lies above
the local-constancy threshold of the DFI mismatch weight.

Thus the dependence of the fan permutation on the delta modulus can be
removed without a power loss.

### 2.2 The short Hecke fold is false

After complete double Poisson, the native coefficient is

```text
g(t)=sum_(u*v=t) p_u*q_v,
B_Delta=sum_t g(t+Delta)*conj(g(t)).                  (2.1)
```

This is an additive autocorrelation of a product convolution, not the
product of two short Hecke polynomials.  The two-spike choice

```text
p=delta_1+delta_Y,       q=delta_1-delta_Y
```

produces the forbidden Hecke index `Y^2-1`.  More strongly, flat data have

```text
sum_(Delta != 0)|B_Delta|^2 >> D^3,                 (2.2)
```

against the desired coefficient scale `D^2`.  Complete Kloosterman
Parseval preserves this loss.

### 2.3 The excess is genuinely broad

A separated nonzero fan packet places normalized energy `>>D` on

```text
|Delta| asymp D,
Delta=2*(r*s-r'*s')
```

after an exact completed physical pullback.  It avoids both coordinate
axes, `Delta=0`, low differences, and the tangent determinant class.
Therefore the excess cannot simply be assigned to the existing affine or
Hankel packet merger.

The fixture is not an actual-prime counterexample: simultaneous
prime-power/product-window realization with one coefficient vector through
all moving DFI moduli is not known.

### 2.4 Finite polar subtraction is insufficient

There is an explicit Fourier frame of modulated separated packets for which
any fixed polar space giving tensor-scale control must have rank

```text
d >= L-O(L^(5/6)).                                  (2.3)
```

Hence deleting the zero mode, the coordinate axes, finitely many Weyl
residues, or any subpower-rank list of classical main profiles cannot prove
the local lift.  A full coefficient-dependent Eisenstein continuum is not
refuted, but constructing it with the correct norm is already the missing
theorem.

### 2.5 The common carrier has a real `GL(3)` coordinate

The two-index torus point

```text
(m,n)=(b,a*c)
```

corresponds to `diag(a*b*c,b,1)`.  Thus `GL(3)` can retain the carrier
geometrically.  A single spherical or maximal-parabolic Hecke eigenvector
cannot encode arbitrary shell weights `z`: its coefficients obey the
standard Hecke separability relations.  Treating the mask as external
two-index Poincare data is possible, but then the required spectral norm is
exactly (1.1), not a consequence of scalar reciprocity.

## 3. The surviving automorphic theorem

The only automorphic repair not ruled out is the following.

### Mask-sensitive regularized two-index Motohashi square function

For each character--Mellin component of the actual QP mask, construct a
two-index `GL(3)` Whittaker/Poincare vector `F(b,n)` such that:

1. its physical norm is the original common-carrier `ell^2_b` norm;
2. automorphic regularization identifies a vector-dependent polar term
   `T_Delta(F)` containing **all** singular, maximal-Eisenstein,
   Weyl-degenerate, and opposite-degenerate channels;
3. the regular remainder satisfies

   ```text
   sum_(Delta != 0)
     ||B_Delta(F)-T_Delta(F)||_(ell^2_b)^2
       << D^(2+o(1))*||F||_phys^2;                   (3.1)
   ```

4. the physical pullback of `T(F)` is bounded by the already proved
   diagonal/tangent/chart estimates, rather than contributing another
   `D^(9/8)` main term.

Equation (3.1) has no polynomial slack: it saves the exact factor `D` in
squared coefficient norm, hence `sqrt(D)` after spectral Cauchy.  It would
imply (1.1).  To infer the full sharp four-cycle bound one must additionally
show that the same regularized operator estimate is compatible with the
post-peeling pair-incidence masks in every remaining sector.

## 3A. Later physical audit: the exact surviving covariance

The subsequent carrier-preserving audit gives a more elementary statement
of the surviving theorem.  For the full symmetric physical edge matrix `T`,
let `P` project off constants, let `d` be the degree vector,
`dbar=mean(d)`, and `delta=d-dbar*1`.  Then

```text
T-(dbar/n)J = PTP + u*w^* + w*u^*,
||w||^2     = n^(-1) sum_b |d_b-dbar|^2,
(PTP)^2     = P*T^2*P-delta*delta^*/n.               (3A.1)
```

Thus the sharp centered norm for this full physical matrix is equivalent,
up to absolute constants, to the selected-degree BDH bound and the centered
common-neighbour covariance bound

```text
n^(-1) sum_b |d_b-dbar|^2 << D*q^o(1),
||P*T^2*P-delta*delta^*/n|| << D*q^o(1).             (3A.2)
```

Both estimates are open.  This equivalence does not automatically apply to
an arbitrary pair-incidence mask left by tangent peeling, and replacing the
empirical mean by a prescribed analytic main term requires a separate scalar
main-term estimate.

The same audit decomposes `T^*T` into actual physical defect rays
`h=ac-a'c'`.  This extraction is exact, but a `q^o(1)` bound for every raw
ray is too strong: fixed-ray stars naturally have norm `sqrt(D)`.  What is
needed is a centered **vector-valued square function across all defects**.
Ordinary high trace and `SL_2` Balog--Szemeredi--Gowers do not produce it,
because scalar defect moments control total quotient mass rather than the
quotient collisions required by BSG.

Conductor lowering to `q^2` is also exact after a coarse archimedean cutoff.
It splits the fine window into `q/D` Mellin packets of individual width `q`,
but their centres fill the original bandwidth `q^2/D`; their cross-Gram is
again (3A.2).  Hence this reorganization proves no new exponent by itself.

## 3B. Later Walsh audit: the critical tail is much narrower

The residual width-`q` blocks are triangle matchings.  For absolute
coefficients, their fourth form has the exact Walsh decomposition

```text
F=sum_(x,y) (sum_sigma C_(x,y,sigma))^2,
R=sum_(x,y,sigma) C_(x,y,sigma)^2.                  (3B.1)
```

Here `R` is the Rademacher square and the effective fibre multiplicity is
`m_(x,y)=F_(x,y)/R_(x,y)`.  On a factor-two coefficient bin of support `M`,
the maximum hyperedge degree and flatness give the proved bound

```text
R<<D*min(1,D/M)*q^o(1)*||z||_2^4.                  (3B.2)
```

The Carleson target on the dyadic layer `m_(x,y)~H` is `R_H<<D/H`.
Consequently it is automatic for `H<=M/D`.  At the critical support

```text
M=D^(15/8),       R<<D^(1/8),       H<=D^(7/8)     (3B.3)
```

is already closed.  Effective Walsh multiplicity is at most literal
selected-support codegree, so only physical endpoint fans of size
`H>D^(7/8)` remain.  This is the source of the present `D^(9/8)` bound:
the maximal physical fan factor `D` multiplies the random budget `D^(1/8)`.

For endpoints `x<y`, with gap `g=y-x`, carrier `v`, completions `a,b`,
residuals `r,s`, defect `k=xa-yb`, and completion gap `j=a-b`, one has

```text
r-s=8*v*k,
y*r-x*s=8*x*y*v*j-g*q^3.                            (3B.4)
```

The existing close-row theorem closes `g<=D^(3/8)`.  There is now a second
proved pointwise sector.  If `w_x,w_y` are the least absolute modular-inverse
steps in the two defect-lift charts and `w=min(w_x,w_y)`, a free-degree
Selberg majorant plus the second-derivative estimate gives

```text
deg(x,y)
 <<D^2/q+D*(w^2/q)^(1/3)+(q/w^2)^(1/3),             (3B.5)
```

closing `w<=D^(27/32)`.  Applying the third-derivative test on the same
affine defect branches, including the `1+wD/q` wrap transition, extends this
to

```text
w<=D^(13/12)   =>   deg(x,y)<<D^(7/8)*q^o(1).       (3B.6)
```

The wrapped range admits a sharper use of Bourgain's local exponential-sum
growth function.  A natural branch has length `N=q/w`, Fourier parameter
`T_h asymp hq`, and there are `J<<wD/q` branches.  With Selberg degree
`K=D^(1/8)`, the endpoint `w=D^(73/64)` has

```text
N=D^(59/64),      J=D^(5/64),      T_K=D^(35/16),
alpha=log(N)/log(T_K)=59/140.                       (3B.7)
```

Bourgain's local line `beta(alpha)<=1/12+(2/3)alpha` gives
`beta(59/140)=51/140`, so the top dyadic block is exactly
`D^(5/64+51/64)=D^(7/8)`.  All lower blocks are smaller.  Therefore the
proved range is actually

```text
w<=D^(73/64)   =>   deg(x,y)<<D^(7/8)*q^o(1).       (3B.8)
```

The first-level inverse-step argument leaves

```text
g>D^(3/8),       w_x>D^(73/64),      w_y>D^(73/64)  (3B.9)
```

as a residual superset.  The simple uniform theorem

```text
deg(x,y)<<D^(7/8)*q^o(1)   in the sector (3B.9)      (3B.10)
```

would close the critical Walsh tail.  In Fourier language (3B.10) is a
mask-sensitive vector-valued two-inverse large sieve; scalar reciprocal-sum
estimates do not yield it.

The adjective "two-inverse" does not mean two independent rotations.  If
`g=y-x` and `g*s+1=m*x`, then every defect lift has the exact common
parametrization

```text
a=(s+m)k+y*n,       b=s*k+x*n,       m*x-g*s=1,      (3B.11)
```

and

```text
T/(xa)-T/(yb)=-T*k/(x*y*a*b)<<D/q.                  (3B.12)
```

Thus the two window phases agree to the physical tolerance throughout the
defect range.  Treating them with independent scalar large sieves cannot
give a square-root gain; the remaining estimate must exploit cancellation
between wrap branches, the selected mask, or packet structure.

The Euclidean algorithm nevertheless closes two additional sectors inside
`(3B.9)`.  For either signed completion chart, let `rho` be the least
absolute remainder of its host modulus modulo its inverse step `w`.  A
second-derivative rebranch proves the target if

```text
w>=D^(21/16),      rho<=D^(27/32),      w*rho>=D^(27/16),
```

and a third-derivative rebranch proves it if

```text
w>=D^(25/16),      rho<=D^(13/12),      w*rho>=D^(7/3).
```

The coordinate change is exact: writing the host as `L*w+r` and the old
lift as `a=w*k-host*n`, the variables `t=k-L*n` give
`k=t+L*n` and `a=w*t-r*n`.  It replaces the large step by `rho=|r|` and
allows the derivative estimates to be rerun on the rebranched fibres.

This descent extends exactly to every primitive direction in the defect
lattice, not only the first remainder.  If `gcd(p,m)=1` and
`r=w*p-Q*m!=0`, then the direction `(p,r)` is saturated and its fibres obey

```text
B<<min(D,1+|p|+|r|D/q),             sum_ell |I_ell|<<D.
```

Writing `|p|=D^u`, `|r|=D^v`, and using the fibre-budget exponent
`b=min(1,max(0,u,v+1-33/16))`, gives the exact feasibility polytopes for
these derivative estimates

```text
C_2: v<=27/32, b<=3/4, b-v<=3/8;
C_3: v<=13/12, b<=1/2, v-b>=13/48.
```

The local-`beta` bound extends to the same vector, with dyadic contribution
`B*(H/K)*(Hq)^(beta(log(q/|r|)/log(Hq))+o(1))`.  This is a strict improvement:
there are later convergents with `(u,v,b)=(3/5,4/5,3/5)` in `C_2` even
though both the original and first Euclidean remainders are of order `q`.

Iteration does not cover everything.  For bounded-partial-quotient
rotations, every useful primitive vector lies above `u+v=33/16`; the most
favourable lower envelope has equality and
`b>=min(1,max(u,1-u))`.  This misses `C_2`, `C_3`, and the full current
local-`beta` complex.  Its best top-block certificate is only
`D^(6535/6624)=D^(7/8+739/6624)`.  Consecutive Fibonacci endpoints put both
inverse charts on this trajectory (as a coprime lattice fixture, not an
actual-prime counterexample).  Thus repeated one-dimensional Euclidean
rebranching is genuinely stronger, but cannot by itself prove the global
bound.

Termwise estimation and an unstructured large sieve across the original wraps
are not enough.  Exact Poisson summation exposes a sparse determinant strip
with `h` aliases of every residue; at top Selberg frequency, ordinary
stationary phase stops at `sqrt(hq)=D^(35/32)`, while an unstructured additive
large sieve is worse.
There are coherent low-frequency fixtures saturating termwise absolute
summation, although their actual window count is only tangent scale.  Thus
the still-open sector is the part of `(3B.9)` for which no primitive vector
in either chart enters the derivative or current local-`beta` polytopes.
The bounded-partial-quotient fixture shows that further descent alone cannot
remove it; it needs signed frequency averaging or mask/packet structure.

The dense-defect route now has an exact inverse formulation.  For a fixed
endpoint fan `K` of size `H`, the map from the defect to the paired completion
vector `(a_k,b_k)` is a Freiman two-isomorphism.  Because all defects lie in
an `O(D)` interval, projection to either completion coordinate is itself an
exact Freiman two-isomorphism: a spurious collision would be a nonzero multiple
of `x` or `y` of size `O(D)`.  Hence

```text
E^+({a_k})=E^+(K)>>H^4/D.                              (3B.13)
```

At `H=D^(7/8)` this is exactly `D^(5/2)`.  Every genuine three-point
affine/Hankel packet in that fan has primitive direction
`(d,p_a,p_b,-p_v)` with `|d|<<D` and
`|p_a|+|p_b|+|p_v|<<sqrt(D)`.  The pairs `(d,p_a)` lie in the determinant-`y`
lattice `p_a==x^(-1)d (mod y)`.  The determinant of two candidate packet
directions is therefore a multiple of `y`, but has size `O(D^(3/2))=o(q)`;
it vanishes.  Thus all actual tangent packets in one endpoint fan share one
primitive continued-fraction completion ray and can be labeled before
forming the Gram layer.

This does not force a dense fan to occupy that ray.  Density only forces an
`a`-chord of scale `q/H=D^(19/16)` at the threshold, whereas the genuine
continued-fraction scale is `q/D=D^(17/16)`, another exact `D^(1/8)` gap.
There is a useful low-step converse: for suitable shell constants `C,c>0`,
no occupied completion three-progression has
`C*sqrt(D)<|s|<=c*sqrt(q)`.  Below the upper cutoff it would be a genuine
carrier packet, and product curvature would force `|s|<<sqrt(D)`.

The same calculation works for every additive-energy rectangle.  Write its
completion coordinates as `a,a+r,a+s,a+r+s`.  The integral carrier mixed
difference satisfies

```text
Box(v)=C_x*r*s*(2*a+r+s)/[a*(a+r)*(a+s)*(a+r+s)]+O(D/q).              (3B.14)
```

If `|r*s|<=c*q`, integrality forces `Box(v)=0`, and the lower shell bound in
`(3B.14)` then forces `|r*s|<<D`.  Consequently the annulus
`D<<|r*s|<<q` is empty.  The whole narrow contribution is only
`O(H*D*log q+H^2)<<D^2 log q`; every still-dangerous energy rectangle has
the genuinely broad side product `|r*s|>>q`.  This reduction does not require
packet peeling, but it gives no cancellation among those broad rectangles.

One more reciprocal derivative gives a real but nonclosing rigidity.  If two
broad rectangles have the same directions `(r,s)` and the same integer label
`t=Box(v)`, their base completions differ by at most

```text
O(D*q/|r*s|)=O(D/|t|).
```

Also, for each fixed nonzero completion-determinant label `Delta`, there are
only `D^(3/2+o(1))` direction pairs.  Summing `t` restores the lost base
factor, however, and `Delta=0` remains a full primitive-ray sector.  An exact
packet-free quadratic lattice fixture has `D^(3-o(1))` broad rectangles with
`Delta=0` and `t asymp r*s/q`, proving that these two labels alone cannot
close the energy bound.  The fixture deliberately violates the individual
product bands, so it is a proof-method obstruction, not a physical
counterexample; the surviving theorem must couple those bands across bases.

After peeling the unique low-height ray, the minimal open theorem is

```text
E^+({a_k: k in the packet-free remainder})
   <<D^(5/2)*q^o(1).                                   (3B.15)
```

Together with `(3B.13)`, this would give `H<<D^(7/8)q^o(1)`.  The theorem
in `(3B.15)` is not proved: broad isolated two-point reciprocal secants can
carry the completion energy without creating a three-point line.  The
detailed determinant, popular-chord, mixed-difference, and branch ledgers are
in the dedicated dense-defect and reciprocal mixed-difference audits.

The higher-order audits narrow, but do not remove, this gate.  Three fixed
pivots with primitive completion-relation height `J` have at most

```text
t_3<<1+D/J                                             (3B.16)
```

common endpoints.  The global `K_(3,2)` exchange is exact, but its raw
reciprocal-height aggregation is worse than the elementary first moment by
`D^(1/4)`.  A sharper fixed-pair height-bin summation recovers the
`D^(9/8)` high-tail frontier, but still misses the sharp layer by `D^(1/8)`.
Thus higher trace has exposed a projective-design/packet-packing obstruction;
it has not proved (3B.10).

The fixed-pair theorem is nevertheless aligned exactly with a sharp spectral
argument.  On the dyadic `H`-codegree layer, every endpoint has at most

```text
L_H<<D^2/H^2*q^o(1)                                 (3B.17)
```

high partners.  Hence its square-root-degree scale is

```text
H*sqrt(L_H)<<D*q^o(1).                              (3B.18)
```

The remaining loss is the passage from square-root degree to the all-plus
Schur scale `H*L_H`.  A sharp replacement for the pointwise route is therefore
an **inverse-expander packet theorem**: after locally extracting all coherent
low-height affine/Hankel modes, the residual high-partner matrix has norm
`O(H*sqrt(L_H)q^o(1))`; conversely, any larger norm recovers another packet
carrying comparable spectral mass.  Uniform-subset designs show that this is
false without local packet extraction, while their excessive eigenvectors are
exactly coherent low-height modes.  This is the most economical current
formulation of the final `D^(1/8)` gain.

There is also genuine recurrence.  A fan of size `H` forces one completion
translation `Omega(H^2/D)` times and `Omega(H^4/D)` equal-determinant
four-walk collisions.  A polynomial global excess forces recurrent color
matrices and four distinct completions.  Their exact volume-plane index has

```text
|t|<<D^3/q=D^(15/16+o(1)).                          (3B.19)
```

The open fan threshold is `D^(7/8)`, so the scalar plane-label family is
larger by exactly `D^(1/16)`.  This is not merely a loose pigeonhole: a Farey
split-quadric fixture has divisor-sized occupancy in every fixed plane but a
polynomial all-plus/random-sign ratio.  It is not an actual-prime QP
counterexample, but it proves that scalar `t` orthogonality plus fixed-plane
conic bounds cannot supply the missing saving.

The elementary surviving route therefore needs one of the following
sufficient repairs on the actual selected mask:

```text
transverse two-inverse codegree (3B.10),
or a full-label (anchor normal,plane index) Carleson square function,
or the inverse-expander packet theorem above.                            (3B.20)
```

Any such result must retain the carrier and selected coefficient mask.  A
scalar frequency estimate, a fixed-plane divisor bound, or an unlabelled
graph trace is insufficient.

## 3C. Product-error cubes: a proved rigidity theorem, but on the wrong side

The individual product errors sharpen the reciprocal mixed-difference
calculus.  On a completion rectangle with positive directions `r,s`, put

```text
rho=Delta_r v,       sigma=Delta_s v,       tau=Delta_r Delta_s v,
A=Delta_r Delta_s(a*v-C).
```

Then the exact Leibniz identity is

```text
A=s*rho+r*sigma+(a+r+s)*tau.                         (3C.1)
```

On an eight-vertex cube with third positive direction `h`, write
`omega=Delta_h Delta_r Delta_s v` and
`A_3=Delta_h Delta_r Delta_s(a*v-C)`.  Exactly,

```text
A_3=(a+h+r+s)*omega
      +h*tau_rs+r*tau_sh+s*tau_rh.                  (3C.2)
```

Reciprocal rounding makes every pair curvature nonnegative and kills
`omega` when `hrs<<q^2`.  Consequently, if all three faces are broad,

```text
|rs|,|rh|,|sh|>>q,
```

then an occupied cube must satisfy

```text
|rsh|>>q^2.                                          (3C.3)
```

Indeed the three broad inequalities first give `|rsh|>>q^(3/2)`, while
`omega=0` in the lower-volume branch makes (3C.2) force
`|rsh|<<Dq`; these are incompatible because `sqrt(q)/D=D^(1/32)`.
The same algebra proves two concrete recurrence exclusions:

```text
packet-free occupied four-AP:
    r=O(D) or r>>q^(2/3)=D^(11/8);

occupied broad 3 x 2 strip with r^2*s<<q^2:
    r=O(D),                                           (3C.4)
```

and symmetrically for a `2 x 3` strip.  Thus balanced broad rectangles at
`r,s~sqrt(q)` cannot concatenate in either of their own directions.

This does not close packet-free energy.  If `E>D^(5/2+epsilon)`, the exact
Freiman map and `U^2<=U^3` force

```text
>>D^(3+2*epsilon)
```

all-broad additive cubes after the narrow faces are removed.  The theorem
above sends every survivor to (3C.3), where the raw base/direction capacity
is still `O(H*D^3)`.  Standard BSG, dependent random choice, and cube
pigeonholing therefore cannot finish the proof.  A physical-band theorem
counting the high-volume cubes would finish it, but that theorem remains
open.

## 3D. The exact error-coherence square-root gate

There is a sharper spectral formulation of the same missing cancellation.
For each retained point label the integer product error by

```text
epsilon(a,v)=a*v-N_0,             |epsilon|<<D.
```

For ordered pairs put

```text
n=a_i+a_j,             eta=epsilon_i+epsilon_j,
B(n,eta)=#{(i,j) with these two labels}.              (3D.1)
```

The completion energy and the fully error-tagged energy are exactly

```text
E_a  =sum_n (sum_eta B(n,eta))^2,
E_tag=sum_(n,eta) B(n,eta)^2.                         (3D.2)
```

If `G_(eta,eta')=<B(.,eta),B(.,eta')>`, then

```text
E_a=1^*G1,       E_tag=tr(G),       C_err=E_a/E_tag. (3D.3)
```

Thus the formerly vague cross-wrap loss is the concrete zero
error-frequency coherence quotient `C_err`.  With

```text
mu_2=max_(n,eta) B(n,eta),
```

one has

```text
E_a<=C_err*mu_2*H^2.                                 (3D.4)
```

The precise sufficient theorem is therefore

```text
C_err*mu_2 <<D^(1/2)*q^o(1)                          (3D.5)
```

on the physical post-peeling broad kernel.  Cotlar summation, ordinary
nonbacktracking trace, entropy collision, and the graph-weighted Yao
identity all reproduce the off-diagonal part of (3D.3); none bounds it.

The exponent in (3D.5) is sharp.  At the genuine tangent centre `C=Q^2`,

```text
a=Q+h,       v=Q-h,       epsilon=-h^2,
|h|<=sqrt(D),                                           (3D.6)
```

and the effective coherence has order `sqrt(D)`.  This packet is already
eligible for the affine/Hankel peel, but it proves that a valid global
trace theorem cannot improve the square-root merely by retagging errors.
No physical-shell example with a larger power has been found.

Equivalently, the stronger shell-only conjecture

```text
A(C,D)={a~q:there is v~q with |a*v-C|<=D},
E^+(A(C,D))<<D^(5/2)*q^o(1)                           (3D.7)
```

would imply the packet-free theorem.  It remains plausible and open.  A
CRT construction shows that (3D.5) is false if the common-shell condition
`a~v~q`, `C~q^2` is discarded, so any proof must use precisely that
physical geometry.

## 3E. Full-strip local packets and the nonzero-saddle gate

Two further audits show exactly how much of (3D.7) follows from existing
near-curve technology.  For three strip points `a_1<a_2<a_3` of completion
diameter `L`, one has the exact reciprocal determinant

```text
det[1,a_i,C/a_i]
 =C*(a_2-a_1)*(a_3-a_1)*(a_3-a_2)/(a_1*a_2*a_3),

|det[1,a_i,v_i]|
 <=C*L^3/a_min^3+2*L*D/a_min.                       (3E.1)
```

The second determinant is integral.  Hence every three occupied points in
an arc `L<=c*q^(1/3)` are exactly collinear.  On a primitive decreasing
line of direction `(Q,-P)`, the product is a quadratic with second
difference `-2PQ`, giving

```text
# packet <<1+sqrt(D/(P*Q))<=1+sqrt(D).               (3E.2)
```

This is a genuine local random-or-packet theorem, but a scaled Behrend set
can have one abstract point per such arc and cubic projected energy.  The
local statement alone therefore cannot prove (3D.7).

The product band does exclude the cleanest physical version of that
fixture.  On one progression

```text
a=a_0+R*k,       R>=q/D,       M<=q/R,
f(k)=C/(a_0+R*k),       delta=D/q,
```

the `k=4` Huxley--Sargos near-curve theorem gives

```text
# {k:||f(k)||<=delta}
 <<M*(R^4/q^3)^(1/10)
   +M*(D/q)^(1/6)
   +D^(1/4)*q^(1/2)/R+1.                            (3E.3)
```

At the worst endpoint `R=q/D`, `M=D`, the three exponents are

```text
129/160,       79/96,       7/32.
```

Thus every macroscopic rank-one progression contains at most

```text
D^(79/96+o(1))=D^(5/6-1/96+o(1)).                   (3E.4)
```

physical strip points.  What is missing is an inverse theorem forcing a
supercritical-energy set to put more than `D^(5/6)` points on one such
rank-one progression; ordinary BSG may return a smaller, higher-rank core.

There is also a direct two-inverse formulation of the remaining analytic
piece.  For a fixed completion pair sum `S`, let `delta=D/q`, `H=q/D` and
use a degree-`H` Selberg majorant with coefficients `|c_h|<<delta`.  Then

```text
R(S)
 <=sum_(|h|,|k|<=H)c_h*c_k*T(h,k),
T(h,k)=sum_a W(a)
 e(C*(h/a+k/(S-a))).                                (3E.5)
```

After Poisson summation in `a`, the zero-dual saddle is characterized by

```text
h*k>0,       a/(S-a)=sqrt(h/k).                     (3E.6)
```

This is the same-sign tangent saddle family.  Its stationary amplitude is

```text
<<sqrt(q)*(h*k)^(1/4)/(sqrt(h)+sqrt(k))^2,
```

and absolute summation already gives the sharp total

```text
delta^2*sqrt(q)*H^(3/2)=sqrt(D).                    (3E.7)
```

The one-zero-frequency terms obey the same bound.  Therefore tangent
stationarity is no longer the analytic obstruction.  Opposite-sign nonzero
modes can have cubic caustics: at `C=Q^2`, `S=2Q`,

```text
(h,k,m,a)=(t,-t,-2t,Q)
```

is an exact example.  For the physical rational centre `C/S^2 in Q`, the
caustic classification shows that exact integer cubics form only `O(H)`
pairs and their total Airy cost is
`D^(-1/24+o(1))`; allowing one near-Airy mode for every pair gives the
smaller ledger `D^(49/48)`.  The regular nondegenerate ledger is
`D^(25/16)`, a factor `H=D^(17/16)` above the target.  A fully uniform
analytic decomposition is not used here; these ledgers only show that the
cubic exception is not the missing power.

The minimal remaining estimate is a signed large-sieve bound of size
`sqrt(D)*q^o(1)` for the **nonzero** Poisson saddles in (3E.5).  Their
collective cancellation is the unresolved two-inverse theorem.

## 3F. The carrier-projection gate and one sharp resonant slice

The same fixed-sum problem has an exact arithmetic formulation.  Write

```text
e=a*v-N_0,       f=b*w-N_0,
S=a+b,           eta=e+f,          U=v+w,
x=a-b,           y=v-w,            P=2*N_0+eta.
```

Then

```text
S*U+x*y=2*P.                                      (3F.1)
```

Consequently, after fixing `(S,eta,U)`, the pair cell has at most
`2*tau(|2P-SU|)=q^o(1)` elements (the zero case is the unique diagonal).
This is a genuine three-label codegree theorem.  It does not survive
projection for free: the required two-label multiplicity sums over all
carrier sums `U`, and bounding the number of occupied `U` remains open.
The Jing--Wu surface-energy theorem controls the full `(S,U,eta)` energy,
not this projected energy.

One resonant slice does close sharply.  If `a*v=b*w`, write

```text
a=g*A,       b=g*B,       (A,B)=1,
v=B*ell,     w=A*ell,     A+B=S/g.
```

For fixed `g|S`, fixing `ell` gives `O(g+sqrt(D))` possibilities after
summation, while fixing `ell*A*(S/g-A)` gives
`O((1+D/g)*q^o(1))`.  Splitting at `g=sqrt(D)` and summing over `g|S`
proves

```text
#{a+b=S, |a*v-C|<=D, |b*w-C|<=D, a*v=b*w}
  <<sqrt(D)*q^o(1).                                  (3F.2)
```

For the full slice, centered coordinates reduce the count further to

```text
R(S)<<sqrt(D)+#{occupied noncentral carrier sums U}. (3F.3)
```

The exceptional `U` contains the quadratic tangent packet and is already
sharp.  Each later `U` contains only `O(1)` points because consecutive
relevant squares are separated by `sqrt(q)>D`.  Thus the outstanding
arithmetic problem is no longer local multiplicity; it is to control how
many scattered carrier sums are occupied.  Analytically, this corresponds to
the required collective nonzero-dual cancellation.

## 4. Why existing theorems do not yet prove (3.1)

- Suvitie's shifted-divisor mean square concerns fixed divisor/Hecke
  coefficients and also averages an additive translation; it has no
  arbitrary common-carrier fibre.
- Yang's noncuspidal `GL(3)` reciprocity starts with one already constructed
  Whittaker vector.  It does not provide the norm-preserving synthesis map
  from an arbitrary QP mask, and it retains additional degenerate and
  residual channels.
- The standard `GL(3)` large sieve's bad long-coefficient term is generated
  by maximal Eisenstein spectrum.  This makes full regularization plausible,
  but it does not supply the required two-index, mask-preserving theorem.
- The recent Hou--Pan cuspidal `GL(3)` sieve does not match the arithmetic
  kernel.  Its long-Weyl factorization has two independent coprime moduli
  and one boundary index, whereas the QP transform has one modulus and the
  joint index `S(-h,-u*Delta;c)`.  CRT does not separate `h` from `Delta`.
  Even a fantasy extension loses the required power on prime/rough delta
  moduli, and the uploaded preprint does not presently include a proof of
  its stated bilinear Theorem 1.3.
- Yao Zhi's five-term theorem (arXiv:2608.15458, Theorem 1.1) is a sharp
  numerical near-miss: for full Cartesian ratio data it gives a centered
  fourth moment of scale `p*D^6` above `D=p^(14/29+o(1))`, while
  `16/33-14/29=2/957`.  The physical fan is instead the selected graph
  `m=m(k)` cut out by arbitrary carriers.  Its packet-free energy relation
  has four terms with arbitrary denominators `v_i`, not the theorem's fifth
  free summand, so the result does not apply to `(3B.15)`.  The exact
  graph-supported centering identity can be proved, but Young's inequality
  gives only `D^3`, and this is sharp for the matching `m(k)=k^2`, whose
  carrier phases are the interval `v_k=k` and whose graph has no three
  collinear points.  Thus mask-blind graph centering still misses
  `D^(5/2)` by `D^(1/2)`; Cartesian completion is worse at `D^6`.
- High graph trace cannot recover the missing labels: actual masked cycles
  need not be tangent, and abstract high-girth regular components can have a
  large centered singular value without any linked cycle.

## 5. Binary outcome

```text
sharp fourth trace D^(1+o(1)):                     NOT PROVED;
best unconditional fourth trace:                  D^(9/8+o(1));
moving-modulus fan obstruction:                    REMOVED;
short Hecke fold:                                  REFUTED;
coefficient-blind local Plancherel lift:            REFUTED;
finite/subpower-rank polar repair:                  REFUTED;
blanket tangent interpretation of the excess:      REFUTED;
actual-prime counterexample:                        NOT FOUND;
two-index carrier geometry:                        EXACT;
regularized mask-sensitive square function (3.1): OPEN;
(3.1) implies balanced broad closure:               CONDITIONAL;
full post-peeling compatibility bridge:             OPEN;
exact residual Walsh decomposition:                 PROVED;
flat-bin random budget D*min(1,D/M):                 PROVED;
automatic critical range H<=D^(7/8):                PROVED;
close endpoint gaps <=D^(3/8):                      CLOSED;
inverse-step sectors min(w_x,w_y)<=D^(73/64):       CLOSED;
shared Bezout/two-window phase coherence:            PROVED;
second/third Euclidean remainder sectors:             CLOSED;
all-primitive Euclidean derivative/beta polytopes:      PROVED;
later-convergent strict sector enlargement:             PROVED;
bounded-partial-quotient two-chart method obstruction:  PROVED;
Euclidean iteration alone as global closure:            INSUFFICIENT;
termwise/unstructured cross-wrap Poisson repair:       REFUTED;
unique CF completion ray for true packets in a fan:   PROVED;
low-step reciprocal 3AP / forbidden middle band:      PROVED;
mixed-difference annulus D<<|r*s|<<q:                 EMPTY;
narrow reciprocal energy O(D^2 log q):                PROVED;
broad reciprocal rectangles |r*s|>>q:                 OPEN;
packet-free reciprocal energy D^(5/2):               OPEN;
fixed-(r,s,t) base diameter O(D/t):                    PROVED;
fixed nonzero-Delta direction bound D^(3/2+o(1)):      PROVED;
two-label t,Delta counting as global closure:           INSUFFICIENT;
Yao graph-centering bound D^3:                         PROVED SHARP;
graph-centering gap to packet-free target:              D^(1/2);
three-pivot height theorem t_3<<1+D/J:               PROVED;
global K_(3,2) aggregation:                          FAILS BY D^(1/4);
high-partner cap L_H<<D^2/H^2:                       PROVED;
square-root layer scale H*sqrt(L_H)<<D:              EXACT;
inverse-expander packet theorem:                     OPEN;
scalar volume-label orthogonality repair:            REFUTED;
transverse codegree D^(7/8):                         OPEN;
full-label plane/packet Carleson theorem:             OPEN.
exact rectangle/cube product-error Leibniz laws:      PROVED;
three-broad-face cube volume |rsh|>>q^2:              PROVED;
packet-free middle-scale four-AP exclusion:           PROVED;
balanced broad 3 x 2 recurrence exclusion:            PROVED;
supercritical energy => D^(3+2eps) broad cubes:        PROVED;
high-volume broad-cube count D^(3+o(1)):              OPEN;
BSG/DRC/raw cube recurrence as global closure:         INSUFFICIENT;
error-tagged two-frequency identity:                  PROVED;
exact surviving quotient C_err=E_a/E_tag:             PROVED;
C_err*mu_2<<D^(1/2+o(1)):                             OPEN;
full reciprocal-strip energy D^(5/2+o(1)):            OPEN.
q^(1/3) local reciprocal arcs are affine packets:     PROVED;
primitive local packet size O(1+sqrt(D/(PQ))):        PROVED;
macroscopic rank-one occupancy D^(79/96+o(1)):        PROVED;
energy inverse => D^(5/6) on one macroscopic AP:      OPEN;
two-inverse zero-dual/tangent contribution sqrt(D):   PROVED;
exact cubic-caustic classification, rational centre:   PROVED;
exact cubic cost D^(-1/24+o(1)), rational centre:       PROVED;
fixed-(S,eta,U) pair-cell multiplicity q^o(1):         PROVED;
projection over occupied carrier sums U:               OPEN;
fixed-S common-product slice sqrt(D)*q^o(1):           PROVED;
full fixed-S count sqrt(D)*q^o(1):                     OPEN;
nonzero Poisson-saddle aggregate sqrt(D):              OPEN.
```

The detailed proofs and executable certificates are in:

- `ZETA23-QP-CHARACTER-MELLIN-HECKE-FOLD-AND-REGULARIZED-MOTOHASHI-GATE-2026-08-24.md`;
- `ZETA23-QP-MASK-PRESERVING-LOCAL-LIFT-AND-GL3-RECIPROCITY-AUDIT-2026-08-24.md`;
- `ZETA23-QP-BULK-PRODUCT-AUTOCORRELATION-AND-KLOOSTERMAN-ISOMETRY-BARRIER-2026-08-24.md`;
- `ZETA23-QP-ACTUAL-MASKED-CYCLE-AND-HIGH-TRACE-LABEL-BARRIER-2026-08-24.md`;
- `ZETA23-QP-SCHUR-CERTIFICATE-ANOVA-AND-CENTERED-COVARIANCE-GATE-2026-08-24.md`;
- `ZETA23-QP-CARRIER-PRESERVING-DEFECT-RAY-INVERSE-GATE-2026-08-24.md`;
- `ZETA23-QP-FIXED-DEFECT-SL2-BSG-QUOTIENT-COLLISION-BARRIER-2026-08-24.md`;
- `ZETA23-QP-Q2-COARSE-LIFT-HYBRID-MELLIN-AND-PRINCIPAL-GATE-2026-08-24.md`;
- `ZETA23-QP-RESIDUAL-WALSH-DEFECT-FAN-INVERSE-AND-CARLESON-GATE-2026-08-24.md`;
- `ZETA23-QP-CRITICAL-WALSH-CLOSE-TRANSVERSE-CODEGREE-AUDIT-2026-08-24.md`;
- `ZETA23-QP-CRITICAL-DEFECT-FAN-RECURRENCE-AND-ENDPOINT-QUADRUPLE-GATE-2026-08-24.md`;
- `ZETA23-QP-SELECTED-SUPPORT-K23-THREE-PIVOT-HEIGHT-AND-QUARTER-GAP-2026-08-24.md`;
- `ZETA23-QP-K23-FIXED-PAIR-HEIGHT-BINS-AND-HIGH-PARTNER-CAP-2026-08-24.md`;
- `ZETA23-QP-TRANSVERSE-TWO-INVERSE-POINTWISE-AND-LITERATURE-AUDIT-2026-08-24.md`;
- `ZETA23-QP-ITERATED-EUCLIDEAN-REBRANCH-AUDIT-2026-08-24.md`;
- `ZETA23-QP-DENSE-DEFECT-CF-RAY-AND-RECIPROCAL-ENERGY-GATE-2026-08-24.md`;
- `ZETA23-QP-PACKET-FREE-RECIPROCAL-MIXED-DIFFERENCE-AND-YAO-AUDIT-2026-08-24.md`;
- `ZETA23-QP-YAO-GRAPH-WEIGHTED-CENTERING-ADDENDUM-2026-08-24.md`;
- `ZETA23-QP-BROAD-RECTANGLE-THIRD-DIFFERENCE-AND-LABEL-FIXTURE-2026-08-24.md`;
- `ZETA23-QP-PRODUCT-ERROR-CUBE-RIGIDITY-AND-RECURRENCE-GATE-2026-08-24.md`;
- `ZETA23-QP-COMBINATORIAL-INVERSE-BSG-DRC-AND-LABEL-DISPERSION-AUDIT-2026-08-24.md`;
- `ZETA23-QP-ERROR-LABELLED-BROAD-SPECTRAL-COHERENCE-GATE-2026-08-24.md`;
- `ZETA23-QP-FULL-RECIPROCAL-STRIP-LOCAL-PACKETS-AND-PROJECTION-GATE-2026-08-24.md`;
- `ZETA23-QP-PAIR-CELL-DISCRIMINANT-AND-SQRT-BLOCK-AUDIT-2026-08-24.md`;
- `ZETA23-QP-FIXED-PAIR-SUM-SELBERG-TANGENT-AND-NONZERO-DUAL-GATE-2026-08-24.md`;
- `ZETA23-QP-NONZERO-POISSON-CUBIC-SADDLE-AND-DYADIC-AUDIT-2026-08-24.md`.
