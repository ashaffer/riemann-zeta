# QP reciprocal curve: stationary-amplitude Fourier transference and the caustic derivative loss

**Date:** 2026-08-25  
**Verdict:** a frequency-dependent stationary amplitude can be inserted into
the exact cyclic Fejer normal-lattice identity.  On a finite two-dimensional
frequency torus, its DFT expresses the weighted sum exactly as a superposition
of the same cyclic Fejer orbit with shifted affine intercepts.

For a uniformly regular stationary symbol, the DFT is concentrated at shifts
of size `O(1/H)`, so affine-height suppression survives.  Near the cubic fold,
the symbol varies on the curvature scale `d`; its DFT spreads to intercept
shifts of size `1/d`.  At the Airy transition this enlarges the major arc by
`H/J=D^(25/24)` and leaves an amplitude loss `D^(25/48)` over the target.
Fourier-algebra transference alone does not remove that loss.

This proves an exact identity and a regular-symbol sector, not the aggregate
stationary large sieve, (RSR), or the sharp four-cycle bound.

## 1. Finite-torus transference identity

Let `c_h` be supported on ordinary integer representatives `|h|<N`, and
choose `M>2*N`.  Fix a rational tangent normal-lattice congruence

```text
k*K_0-h*P_0==0 (mod R).                              (1.1)
```

Let `A` be any complex function on `(Z/MZ)^2`, periodically evaluated at
the integer pair `(h,k)`.  Define

```text
S_A(alpha,beta)
 =sum_((h,k) satisfying (1.1))
   c_h*c_k*A(h,k)*e(h*alpha+k*beta).                 (1.2)
```

Use the normalized finite DFT

```text
Ahat(u,v)=M^(-2) sum_(x,y mod M)
 A(x,y)*e_M(-u*x-v*y),                               (1.3)
A(h,k)=sum_(u,v mod M) Ahat(u,v)*e_M(u*h+v*k).       (1.4)
```

For `P_c(theta)=sum_h c_h e(h*theta)`, the congruence detector gives the
exact identity

```text
S_A(alpha,beta)
 =sum_(u,v mod M) Ahat(u,v) * O_c(alpha+u/M,beta+v/M), (1.5)

O_c(a,b)
 =1/R sum_(j mod R)
   P_c(a-j*P_0/R)*P_c(b+j*K_0/R).                    (1.6)
```

Thus the stationary symbol does not destroy the cyclic orbit.  Each of its
Fourier coefficients translates the two affine intercepts and multiplies
one copy of the original orbit sum.  No approximation or stationary-phase
argument is used in (1.5).

For an actual fixed rational tangent, restrict the Poisson modes to its
stationary normal lattice and put the corresponding stationary main
amplitude, including its constant Maslov factor and smooth cutoff, into
`A(h,k)`.  Its stationary phase at the tangent is affine-linear in `(h,k)`,
so that phase is already represented by `(alpha,beta)`; the nonconstant
symbol is precisely the factor transferred by (1.5).

## 2. Exact shifted-height Fourier-algebra bound

For shifted intercepts define

```text
eta_(u,v)
 =min_(j mod R) max(
   ||alpha+u/M-j*P_0/R||,
   ||beta +v/M+j*K_0/R||).                           (2.1)
```

Take the height-one normalized Fejer polynomial

```text
P_N(theta)=N^(-2)|sum_(0<=r<N)e(r*theta)|^2.         (2.2)
```

Its triangular coefficients satisfy

```text
0<=P_N(theta)<=min(1,1/(4*N^2*||theta||^2)).         (2.3)
```

Every point of the orbit in (1.6) has at least one coordinate at distance
`eta_(u,v)` from an integer.  Consequently (1.5) gives

```text
|S_A(alpha,beta)|
 <=sum_(u,v mod M) |Ahat(u,v)|*w_N(eta_(u,v)),       (2.4)

w_N(eta)=min(1,1/(4*N^2*eta^2)),                    (2.5)
```

with `w_N(0)=1`.  This is stronger than the unweighted Fourier-algebra bound

```text
|S_A|<=||A||_A:=sum_(u,v)|Ahat(u,v)|.                (2.6)
```

It records exactly how much Fourier mass of the stationary symbol lands on
each shifted approximate affine-height character.

There is a useful coarse form.  Write `|u|_M=min(u,M-u)`, and let

```text
A_low(L)=sum_(max(|u|_M,|v|_M)<=L)|Ahat(u,v)|,
A_tail(L)=sum_(max(|u|_M,|v|_M)> L)|Ahat(u,v)|.      (2.7)
```

The orbit distance is one-Lipschitz in the two intercepts.  If
`eta_0=eta_(0,0)`, then

```text
|S_A|
 <=A_low(L)*w_N(max(0,eta_0-L/M))+A_tail(L).         (2.8)
```

Equations (2.4) and (2.8) are the precise transference estimates.  Merely
bounding `||A||_A` discards the arithmetic location of the shifted orbit and
cannot distinguish a Fourier translate which hits a packet character.

## 3. Uniformly regular symbols are genuinely localized

Work in the critical top dyadic block

```text
|h|+|k| asymp K,       K asymp H,       M asymp H.   (3.1)
```

At a fixed interior tangent, introduce the curvature frequency `d` by

```text
|F''(x_*)| asymp d/q.                                (3.2)
```

Away from the fold, `d asymp K`, ordinary stationary phase has amplitude

```text
A_0 asymp sqrt(q/K).                                 (3.3)
```

After a smooth top-block cutoff, the normalized symbol is a periodic smooth
function of `(h/M,k/M)` with bounded derivatives.  Finite summation by parts
therefore gives, for every fixed `B`,

```text
|Ahat(u,v)|
 <<_B A_0*(1+|u|_M+|v|_M)^(-B),
||A||_A<<A_0.                                        (3.4)
```

Choose `L=q^epsilon` and `B` large.  Equations (2.8) and (3.4) show that if

```text
eta_0>=2*q^epsilon/H,                                (3.5)
```

then

```text
|S_A|
 <<sqrt(q/K)*min(1,(N*eta_0)^(-2))+q^(-A)           (3.6)
```

for any prescribed fixed `A`, after changing derivative order.  At
`K,N asymp H=q/D`, the unsuppressed amplitude in (3.6) is exactly

```text
sqrt(q/H)=sqrt(D).                                   (3.7)
```

Hence stationary-amplitude insertion is harmless on a fixed normal lattice
in the uniformly curved, quantitatively nontrivial affine-height sector.
This is a real sector theorem for the stationary main symbol.  It does not
sum over all rational tangent locations, and the stationary expansion's
standard remainder must still be summed in the full Poisson decomposition.

If `eta_0` is only a constant multiple of `1/H`, even the `O(1)` low Fourier
modes can translate an orbit point onto the major arc.  Formula (2.4), not a
claim of automatic suppression, is then the correct statement.

## 4. Curvature layers and Fourier spread

For an intermediate dyadic curvature layer

```text
d<<K,                                                (4.1)
```

quadratic stationary phase has size

```text
A_d asymp sqrt(q/d).                                 (4.2)
```

Its `j`th derivative in the normal frequency direction is of size
`A_d*d^(-j)`.  A smooth cutoff to a layer of width `asymp d` therefore has
the model finite-DFT envelope

```text
|Ahat_d(u_perp,u_parallel)|
 <<_B A_d*(d/M)
       *(1+d*|u_perp|/M)^(-B)
       *(1+|u_parallel|)^(-B).                       (4.3)
```

Here the coordinates are the primitive normal and tangent frequency
coordinates in one fixed rational chart.  Smooth shell cutoffs convolve
(4.3) with a rapidly decaying `O(1)`-scale sequence.  In particular,

```text
||A_d||_A<<A_d,                                      (4.4)
```

so derivative growth does not by itself create an extra power in the Wiener
norm.  The loss is localization: the significant normal Fourier indices
reach

```text
|u_perp|<<M/d,                                       (4.5)
```

and therefore translate affine intercepts by as much as

```text
|u_perp|/M<<1/d.                                     (4.6)
```

Accordingly, (2.8) preserves affine-height suppression only when

```text
eta_0>>1/d,                                          (4.7)
```

not merely when `eta_0>>1/H`.  In the entire intermediate zone

```text
1/H<<eta_0<=1/d,                                     (4.8)
```

Fourier coefficients of a perfectly smooth stationary symbol can shift the
orbit onto an approximate packet character.  An unweighted Fourier-algebra
argument then gives only

```text
|S_(A_d)|<<sqrt(q/d)
          =sqrt(D)*sqrt(H/d)                         (4.9)
```

at the critical top block.  The exact missing gain on this layer is
`sqrt(H/d)`.

Estimate (4.3) is a local smooth-symbol statement.  Making it uniform while
the rational tangent denominator varies requires tracking the chart and
shell cutoffs.  The torus identity (1.5) itself is uniform and has no such
qualification.

## 5. The Airy transition gives the precise worst derivative loss

At frequency size `K`, one has

```text
|F'''(x_*)|asymp K/q^2.                              (5.1)
```

On the quadratic stationary length `(q/d)^(1/2)`, the cubic phase is small
exactly when

```text
(K/q^2)*(q/d)^(3/2)<<1.
```

Thus the quadratic-to-Airy transition occurs at

```text
J=(K^2/q)^(1/3).                                     (5.2)
```

At `d=J`, (4.2) equals the uniform cubic amplitude

```text
A_Airy=q^(2/3)*K^(-1/3).                             (5.3)
```

The Airy symbol is smooth only on the normal frequency scale `J`; its DFT
therefore spreads through `M/J` modes and shifts intercepts by `1/J`.

At the critical values

```text
q=D^(33/16),       K=M=H=D^(17/16),                 (5.4)
```

the exact exponent ledger is

```text
J                         =D^(1/48),
A_Airy                    =D^(49/48),
target sqrt(D)            =D^(24/48),
amplitude loss            =D^(25/48),
Fourier spread M/J        =D^(25/24).                (5.5)
```

The spread exponent is twice the amplitude-loss exponent, as predicted by
square-root cancellation.  A uniform Airy treatment prevents the false
quadratic blow-up below `J`; it does not supply the missing `D^(25/48)` gain.
In (2.4), the near-fold Fourier mass may land on shifts with
`eta_(u,v)<=1/H`, and triangle inequality permits all of that mass to count
as major arc.

## 6. What remains after transference

The exact identity reduces amplitude insertion to the following weighted
problem:

```text
sum_(u,v)|Ahat(u,v)|*w_H(eta_(u,v)).                 (6.1)
```

Three possible new inputs could improve (6.1):

1. prove that at most a `sqrt(d/H)` fraction of the curvature-layer Fourier
   algebra mass can land on shifted affine-height major arcs (the model in
   which only one of the `H/d` comparable Fourier shifts lands there gives
   the stronger fraction `d/H`);
2. square-sum the shifted orbit values before summing the DFT coefficients,
   gaining the predicted `sqrt(H/d)`;
3. classify every concentration of shifted characters as one physical
   approximate tangent packet and charge it to the packet-pair restriction
   theorem.

None follows from the Fourier-algebra norm alone.  The near-fold layer is
exactly where the varying amplitude and affine-height arithmetic must be
treated together.  The separate facts that exact cubic pairs are sparse and
that one physical tangent packet has length `O(sqrt(D))` do not control all
regular normal-lattice Fourier translates.

The transference therefore validates the proposed architecture on regular
symbols while locating its exact remaining loss:

```text
finite DFT superposition of shifted cyclic orbits:    EXACT;
shifted-eta Fourier-algebra bound (2.4):               PROVED;
uniformly curved symbol localized at scale 1/H:       PROVED;
regular high-height fixed-lattice sector:             CLOSED;
intermediate curvature effective height scale:        1/d;
Airy transition curvature J:                          D^(1/48);
near-fold amplitude loss over sqrt(D):                 D^(25/48);
near-fold Fourier-spread count:                        D^(25/24);
weighted shifted-character square function:           OPEN;
aggregate stationary large sieve / RSR:               OPEN;
sharp four-cycle bound:                                NOT PROVED.
```

## Reproducibility

The finite DFT identity, shifted orbit bound, and transition exponents are
implemented in

```text
src/qp_stationary_amplitude_transference.py
src/test_qp_stationary_amplitude_transference.py
```

Six focused tests verify DFT reconstruction, the unweighted congruence
detector, the amplitude-weighted transference identity, Fejer positivity,
the shifted-eta bound, and the exact critical exponent ledger.
