# QP combined phase-jet sieve and coherence inverse attack

**Date:** 2026-08-25  
**Verdict:** the combination has a rigorous analytic half and a rigorous
exact-arithmetic half, but the quantitative physical interface between them
is still open.  Consequently the sharp `D^(1+o(1))` four-cycle bound is not
proved, and the best unconditional project bound remains `D^(9/8+o(1))`.

The progress is nevertheless structural.  On the analytic side, a finite
phase-jet theorem turns every failure of the desired Bessel estimate into a
large cluster of packets coherent modulo the integer Newton lattice.  On the
arithmetic side, completion-action jets recover the full stationary mode up
to exact physical reflection, all exact affine-height collision branches are
classified and counted, and the genuinely transverse residual has an exact
lifted fingerprint with no other collisions.  The one missing theorem is now
a sampled-to-lifted transference estimate for *near* coherence.

## 1. Finite phase-jet Bessel/inverse theorem

Let `u_nu` be normalized packets on an integer interval of length `N`, and
join two packets when no supplied first-, second-, or third-difference test
proves correlation at most `eta`.  If the resulting major-arc graph has
maximum degree `Delta_eta`, finite Abel summation and Schur's test give, for
arbitrary complex coefficients,

```text
||sum_nu c_nu*u_nu||_2^2
 <=[1+Delta_eta+eta*(K-1-Delta_eta)]*sum_nu|c_nu|^2. (1.1)
```

Conversely, a squared Bessel quotient `L` forces

```text
Delta_eta >=[L-1-eta*(K-1)]/(1-eta).                (1.2)
```

The phase jets must be taken modulo integer-valued Newton polynomials:

```text
sum_(0<=r<=3) m_r*binom(S-S_0,r),       m_r in Z.   (1.3)
```

This quotient is compulsory.  In particular, integral affine Poisson labels
give identical sampled exponentials and cannot be separated by a fictitious
Fourier variable.

At the worst endpoint,

```text
N=q^(1/3)=D^(11/16),          K<=D^(7/6+o(1)).      (1.4)
```

The cubic finite-difference envelope optimizes at

```text
eta_cubic=D^(-11/64).                               (1.5)
```

This exceeds the pair saving for the full anisotropic theorem,
`D^(-1/6)`, by `D^(-1/192)`.  It exceeds the saving needed merely to repair
the current `D^(7/96)` operator deficit, `D^(-7/48)`, by `D^(-5/192)`.
Equivalently:

```text
full sqrt(A/B) target: eta=D^(-1/6),   Delta<<D^(1+o(1));
close current gap:     eta=D^(-7/48),  Delta<<D^(49/48+o(1)). (1.6)
```

Thus third-order oscillation is numerically strong enough.  The margins are
small, so the physical stationary partition must retain essentially a full
`q^(1/3)` block.

## 2. Stationary actions are rigid in the correct quotient

For

```text
F(a,S)=-m*a+C*h/a+C*k/(S-a),                        (2.1)
```

let `J(S)` be its critical value on a regular interior branch.  The lifted
jet `(J',J'',J''')` has an explicit rational inverse off

```text
h=0,          k=0,          m=0,          or the cubic fold. (2.2)
```

More importantly, there is an inverse that does not use the affinely aliased
first derivative.  Put

```text
t=a/S,       u=da/dS,
A=-S*J'''/(3J''),       B=S^2*J''''/(3J''),
R=u*(1-u)/(t*(1-t)).                                (2.3)
```

Then exactly

```text
A=1+(u-t)^2/[t*(1-t)],
B=4*A^2-5*R*(A-1).                                  (2.4)
```

Off `m=0`, `(J'',J''',J'''')` recovers the stationary mode up to

```text
(a,h,k,m) -> (S-a,k,h,-m).                          (2.5)
```

The reflected actions differ by exactly `m*S`, so (2.5) is the genuine
physical affine alias on integer `S`.  The inverse Jacobian degenerates only
as `m->0` in a compact interior collar.  The fourth derivative is used to
track/classify a resonant cubic jet across the block; no fourth-derivative
exponential-sum estimate is required.

## 3. Exact coherence branches are completely classified

In scaled-cusp coordinates, let

```text
U=2d*y-g*(p^2-d^2),
H=2d^2*Q-g*p*(p^2-d^2)-2p*U,
j_-=H-dU,                  j_+=H+dU.                (3.1)
```

The two affine-intercept defects from the rational tangent are exactly

```text
delta alpha=j_-/[2(p+d)^2],
delta beta =j_+/[2(p-d)^2].                         (3.2)
```

Four distinguished stationary normals detect

```text
j_-=0,       j_+=0,       H=0,       H-pU=0.        (3.3)
```

The first three are precisely the already peeled axes
`z=-dv,z=dv,z=0`.  Simultaneous left and right collision forces `d^2|g`.
The fourth branch is new: it is a cubic-fold affine-height collision and is
equivalent to `z=-pv`.  It does not force square content.

The new branch is nevertheless affordable.  On `H-pU=0`, write

```text
Q=pL,       g=da,
a*(p^2-d^2)+3w=2dL,
4e=w*(a*(p-d)^2-w),
4f=w*(a*(p+d)^2-w).                                 (3.4)
```

For signed `d`, set `x=p-d>0`, `z=p+d>0`, and
`eta=a*x^2-w`.  Exact elimination gives

```text
x*(2L+a*z)=2Q-3w,
4e=w*eta,
2x*(a*(p+x)+L)=2Q+3eta.                             (3.5)
```

If `|w|<=sqrt(A)`, sum over `w` and divisors of `2Q-3w`.  Otherwise the
narrow mask gives `|eta|<4sqrt(A)`, and one sums over `eta` and divisors of
`2Q+3eta`.  This proves, with arbitrary packet deletion and asymmetric
`A<=B`,

```text
# {H-pU=0, |e|<=A, |f|<=B} <<sqrt(A)*Q^o(1).        (3.6)
```

Thus no exact affine-height branch exceeds the packet budget.

## 4. The transverse residual has an exact lifted fingerprint

For a primitive residual direction, put

```text
chi=gcd(p+d,p-d) in {1,2},
a=(p+d)/chi,       b=(p-d)/chi,       N=a+b,
n=p*y-Q*d.                                            (4.1)
```

The canonical regular and cubic action defects are

```text
J_2=2Q*n^2/[chi^2*(Q^2-y^2)],
J_3=-8n^3/[c_0*chi^3*(Q^2-y^2)],
c_0=gcd(4,N^3),
J_3/(chi*J_2)=-n/Q.                                 (4.2)
```

The regular tangent curvature is

```text
K_2=8p^4/[chi^2*(p^2-d^2)].                         (4.3)
```

Because `p^4/(p^2-d^2)` is reduced, `(chi,K_2)` recovers `(p,|d|)`.
The ratio in (4.2) recovers `n`; then `J_2` recovers `|y|`, and
`d=(py-n)/Q` fixes the orientation.  The narrow product band makes the
content `g` unique.  Hence

```text
(chi,K_2,J_2,J_3)                                   (4.4)
```

recovers the entire residual point, while replacing `J_3` by `|J_3|`
leaves exactly the physical reflection orbit.  This holds on the genuine
`(z+dv)(z-dv)!=0`, nonsquare-content residual; it is not an axis theorem.

At the worst energy endpoint,

```text
J_2 has at most D^(13/48+o(1)) integral lifts,
|J_3|<<D^(-5/8).                                    (4.5)
```

So the cubic defect is automatically unwrapped, and the total possible lift
multiplicity is far below both cluster ceilings in (1.6).  A scan of 238,640
oriented residual points for `101<=Q<=4000` found no nonreflection collision
of the lifted fingerprint.  The proof of injectivity is exact and does not
depend on the scan.

## 5. The precise support/transference obstruction

The fingerprint in Section 4 is not automatically a physical Bessel label.
Its canonical regular normal has frequency size `p^2`; after the proved
residual floor it is supported only in

```text
D^(77/160)<<p<<D^(17/32),                           (5.1)
```

a strip of exponent width `1/20`.  The canonical cubic normal has size
`p^3` and already exceeds the Fejer cutoff at the residual floor by

```text
D^(61/160).                                         (5.2)
```

It is therefore a virtual inverse invariant, not a Fourier column that may
be inserted into the original sum.  Meanwhile, the quotient curvature jet
of Section 2 recovers a *dual stationary mode*, whereas (4.4) also recovers
the *primal affine packet and content*.  Neither theorem alone supplies the
missing identification.

The remaining theorem can now be stated without metaphor.

> **Mask-sensitive sampled-to-lifted jet transference.**  On every physical
> completion block of length `q^(1/3-o(1))`, a pair of regular residual
> packets must either satisfy a first-, second-, or third-difference estimate
> at the correlation threshold in (1.6), or its sampled action jet modulo
> the integer Newton lattice must determine the lifted fingerprint (4.4) up
> to `Q^o(1)` distortion and the lift count (4.5).  Cross-amplitudes must have
> uniformly bounded normalized Abel variation.

If this theorem is proved at `eta=D^(-7/48)`, (1.1), (3.6), and (4.5) give
the missing `D^(-7/96)` operator saving.  At `eta=D^(-1/6)` they give the
full `sqrt(A/B)` anisotropic saving.  The remaining difficulties are:

```text
lifting quadratic/cubic Newton wraps from sampled data;
uniform stability at the smallest nonzero slope defect |n|=1;
retaining full q^(1/3) blocks through stationary partitions;
transferring the varying stationary amplitude without an l^1 fold loss;
realizing the virtual residual fingerprint past the p^2 support plateau. (5.3)
```

## 6. Binary status

```text
finite phase-jet correlation tests:                 PROVED;
coefficient-uniform Bessel/inverse dichotomy:        PROVED;
endpoint cubic saving sufficient numerically:        PROVED;
lifted regular stationary-action inverse:            PROVED;
affine-quotient q2--q4 inverse up to reflection:      PROVED;
scaled cusp axes as affine-height collisions:        PROVED;
new fold-height branch classification:               PROVED;
fold-height O(sqrt(A)Q^o(1)) count:                  PROVED;
transverse residual lifted fingerprint inverse:       PROVED;
only exact residual symmetry is reflection:           PROVED;
residual cubic probe physically supported:            FALSE;
sampled-to-lifted quantitative transference:          OPEN;
physical mask-sensitive phase-jet Bessel theorem:     OPEN;
sharp four-cycle bound:                               NOT PROVED.
```

The focused proofs, implementations, and tests are recorded in the phase-jet
Bessel, affine-height inverse, fold-height divisor, stationary-action
rigidity, and residual-fingerprint companion reports dated 2026-08-25.
