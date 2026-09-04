# QP four-cycle: exact covolume of a degenerate short plane

**Date:** 2026-08-15  
**Verdict:** the repeated rank-one direction in a degenerate short plane has
height at most the plane covolume, hence at most the product of its first two
successive minima.  The exact formula also shows that a proposed lower bound
`lambda1*lambda2 >> q*h/|det C|` is false.

## 1. Exact normal form

Let `K` be the signed color matrix, `det K=k!=0`, and suppose the degenerate
plane has primitive null direction

```text
e=r*s^T,          gcd(r1,r2)=gcd(s1,s2)=1,
r^T K s=0.                                             (1.1)
```

Write `r_perp=(r2,-r1)` and `s_perp=(s2,-s1)`.  There are nonzero integers
`eta,theta` such that

```text
K s=eta r_perp,             K^T r=theta s_perp.       (1.2)
```

Unimodular changes sending `r,s` to the first coordinate transform `K` to

```text
K'=(0,theta;eta,gamma).                               (1.3)
```

Consequently

```text
eta*theta=-k.                                         (1.4)
```

The second primitive normal of the plane is

```text
n=adj(e)^T=r_perp*s_perp^T.                           (1.5)
```

The content of the six Pluecker coordinates of `K wedge n` is invariant
under the same unimodular change.  In (1.3) it is visibly

```text
delta=gcd(eta,theta).                                 (1.6)
```

Thus the saturated integral plane

```text
Gamma={X in Mat_2(Z): <K,X>=<n,X>=0}                 (1.7)
```

has covolume

```text
det Gamma=||K wedge n||/delta.                        (1.8)
```

## 2. Exact metric identity and the null-height bound

Put `R2=||r||_2^2`, `S2=||s||_2^2`.  The four orthogonal rank-one tensors
formed from `r,r_perp,s,s_perp` give

```text
||K wedge n||^2=eta^2 R2^2+theta^2 S2^2.             (2.1)
```

After dividing by `delta^2`, both coefficients remain nonzero integers.
Therefore

```text
(det Gamma)^2>=max(R2^2,S2^2)>=R2*S2=||e||_2^2.      (2.2)
```

In particular

```text
||e||_infinity<=det Gamma.                            (2.3)
```

If `Gamma` is the saturated plane spanned by first and second successive-
minimum vectors `V1,V2`, then

```text
det Gamma<=||V1 wedge V2||<=lambda1*lambda2.          (2.4)
```

This gives the clean middle-slice height bound

```text
h(e)<=lambda1*lambda2.                                (2.5)
```

It is stronger and more invariant than extracting the repeated root from
the binary discriminant coefficients.

## 3. The suggested `q*h/|k|` lower bound is false

Take the additive color matrix

```text
C=(A,A-a;A-b,A-a-b),       k=-ab,                   (3.1)
```

with coprime `a,b` of order `sqrt(D)` and `A` of order `q`.  Its tangent
direction is `e=(1,1;1,1)`.  Equations (1.2) have

```text
eta=a,             theta=b,             delta=1,   (3.2)
```

and (2.1) gives

```text
det Gamma=2*sqrt(a^2+b^2) asymp sqrt(D).            (3.3)
```

On the other hand

```text
q*h/|k| asymp q/D=q^(17/33+o(1)),                  (3.4)
```

which is polynomially larger than `sqrt(D)=q^(8/33+o(1))`.  Thus no bound
of the proposed shape follows even from the exact tangent geometry.  The
large `q` component of `K` is nearly parallel to `adj(e)^T` and cancels
from the wedge; the surviving covolume measures the two additive gaps.

```text
Pluecker content gcd(eta,theta):                     PROVED;
exact covolume formula (2.1):                        PROVED;
null height h(e)<=lambda1*lambda2:                   PROVED;
lower bound lambda1*lambda2 >> qh/|k|:               FALSE;
multi-slice parabolic point bound:                   PREVIOUSLY PROVED;
full four-cycle bound:                               OPEN.
```

The identities are replayed in
`src/qp_four_cycle_degenerate_plane_covolume.py` and its tests.
