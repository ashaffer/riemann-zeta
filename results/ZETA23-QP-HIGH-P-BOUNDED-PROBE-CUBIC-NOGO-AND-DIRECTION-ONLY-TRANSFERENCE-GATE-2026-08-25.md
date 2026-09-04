# QP high-primitive phase jets: bounded-probe cubic no-go and a direction-only transference gate

**Date:** 2026-08-25  
**Verdict:** the missing sampled-to-lifted theorem cannot be proved by
extracting the canonical cubic character from a bounded number of physically
supported characters.  Any exact integer extraction costs at least
`p^3/H` up to an absolute constant, which is already `D^(61/160)` at the
residual primitive floor.

There is a useful replacement target.  The phase-jet cluster argument does
not need to recover the signed cubic invariant, the carrier, or the content.
It is enough for the sampled physical jet to recover the primitive tangent
direction `(p,d)` up to reflection.  A fixed direction contains only
`O(1+B/p)` residual points, namely `D^(329/480+o(1))` at the worst endpoint.
This is below both the full `D` cluster ceiling and the weaker
`D^(49/48)` ceiling needed to repair the current bound.

The physical packet-to-direction implication is still unproved.  Thus this
report removes one impossible route and weakens the remaining theorem; it
does not prove RSR, the physical Bessel intertwining, or the sharp
four-cycle bound.

## 1. The exact cubic support obstruction

For an integral frequency `xi=(-m,h,k)`, put

```text
phi_xi(t)=(-m)*t+h/(4t)+k/(4(1-t)).                 (1.1)
```

Let `(p,d)=1`, `p>|d|`, and define

```text
chi=gcd(p+d,p-d) in {1,2},
a=(p+d)/chi,       b=(p-d)/chi,       N=a+b,
t_0=a/N,           c_0=gcd(4,N^3).                  (1.2)
```

The equations for a cubic stationary phase are

```text
phi_xi'(t_0)=0,             phi_xi''(t_0)=0.         (1.3)
```

The second equation is

```text
h*b^3+k*a^3=0.                                      (1.4)
```

Since `(a,b)=1`, it gives `h=c*a^3`, `k=-c*b^3`.
Substitution in the first equation gives `-m=c*N^3/4`.  Integrality forces
`c` to be a multiple of `4/c_0`.  Consequently all integral solutions of
(1.3) form the primitive rank-one lattice

```text
Z*xi_3,
xi_3=(N^3/c_0, 4a^3/c_0, -4b^3/c_0).               (1.5)
```

Primitivity follows from

```text
gcd(N^3,4a^3,4b^3)=gcd(N^3,4)=c_0.                 (1.6)
```

Moreover, using only the two Fejer coordinates,

```text
max(|h_3|,|k_3|)>=p^3/2.                            (1.7)
```

Indeed, if `chi=1`, then `a+b=2p` and
`max(a^3,b^3)>=p^3`; if `chi=2`, then `a+b=p` and
`4max(a^3,b^3)>=p^3/2`.  In a fixed interior collar this is comparable to
`p^3`.  This formulation does not require a separate support cutoff on the
Poisson coordinate.

Now let `xi_j=(-m_j,h_j,k_j)` be physical frequencies with
`max(|h_j|,|k_j|)<=H`, and suppose integers `c_j` synthesize a nonzero cubic
phase:

```text
sum_j c_j*xi_j=q*xi_3,             q!=0.            (1.8)
```

The triangle inequality in the two Fejer coordinates gives the exact lower
bound

```text
sum_j |c_j|
 >=|q|*max(|h_3|,|k_3|)/H
 >=p^3/(2H).                                        (1.9)
```

Pointwise products, character ratios, integer determinants, and exterior
constructions that remain well-defined in the sampled Newton quotient all
produce integer combinations of their input characters.  Therefore (1.9)
is also their tensor-degree/coefficient-mass gate.  Rationally dividing the
result is not legitimate in the quotient: it requires a noncanonical root
of a sampled character and loses the integer-Newton alias invariance.

At the residual endpoint,

```text
p>=D^(77/160),                 H=D^(17/16),
p^3/H>=D^(61/160).                                  (1.10)
```

This rules out any `D^o(1)`-degree exact synthesis of the canonical cubic
probe.  Applying finite differences in the completion variable can expose
higher derivatives of one supported nonlinear action, but it does not
invalidate (1.9): whenever the construction claims to have produced the
actual cubic character (1.5), its combined integral dual frequency must lie
on this ray and pays the same support cost.

Equation (1.9) is a no-go only for **exact bounded-probe cubic extraction**.
It does not rule out a genuinely nonlinear inverse theorem which recovers a
direction without synthesizing `xi_3`.

## 2. A full fingerprint is unnecessary

For a residual point the exact identities are

```text
e-f=g*n,                  n=p*y-Q*d.                (2.1)
```

Fix `Q` and one oriented primitive direction `(p,d)`.  If
`|e|<=A<=B` and `g>=G`, then

```text
|n|<=2B/g<=2B/G.                                    (2.2)
```

As the integral carrier `y` varies, `n=p*y-Q*d` runs through one arithmetic
progression of step `p`.  An interval of length `4B/G` therefore contains
at most

```text
1+floor(4B/(G*p))                                   (2.3)
```

possible carriers.

There is no hidden content multiplicity in the high primitive compact
collar.  Changing `g` by one changes the narrow left error by
`(p-d)(Q+y)/2`; after allowing reflection, the sufficient condition

```text
(p-|d|)*(Q-|y|)>4A                                  (2.4)
```

gives at most one admissible content for a fixed `y`.  It holds with a
large power margin in the residual energy core.  Hence, after summing
dyadic content cells, one oriented direction has

```text
#fiber <<(1+B/p)*D^o(1).                             (2.5)
```

Reflection costs only a factor two.

At the worst endpoint,

```text
B=D^(7/6),          p>=D^(77/160),
B/p<=D^(329/480).                                  (2.6)
```

This is dramatically below the available cluster budgets.

## 3. Exact phase-jet ledger under direction transference

For the full anisotropic theorem the off-cluster correlation threshold is

```text
eta_full=D^(-1/6).                                  (3.1)
```

Since the total wide multiplicity is `K<=D^(7/6+o(1))`, Schur's bound has
off-cluster contribution

```text
eta_full*K<=D^(1+o(1)).                             (3.2)
```

The permitted major-arc degree is therefore `D^(1+o(1))`.  The
direction-fiber exponent (2.6) has margin

```text
1-329/480=151/480.                                  (3.3)
```

To repair only the present `D^(7/96)` operator deficit, take

```text
eta_close=D^(-7/48).                                (3.4)
```

Then

```text
eta_close*K<=D^(49/48+o(1)),                        (3.5)
```

and the direction fiber has the still larger margin

```text
49/48-329/480=161/480.                              (3.6)
```

Thus the arithmetic inverse target can be weakened from

```text
sampled jet -> (chi,K_2,J_2,J_3)                   (3.7)
```

to

```text
sampled jet -> (p,d), modulo reflection.            (3.8)
```

No recovery of `n` is needed: its entire fiber fits comfortably inside the
major-arc allowance.

## 4. The precise theorem still missing

A sufficient physical statement is the following.

> **Direction-only sampled-jet transference.**  On every retained
> completion block of length `q^(1/3-o(1))`, after quotienting by the
> integer Newton lattice, the jet-major-arc neighborhood of any regular
> residual packet at threshold `eta` is supported on `D^o(1)` primitive
> tangent directions `(p,d)`, up to the exact reflection involution.
> Cross-amplitudes have uniformly bounded normalized Abel variation.

For `eta=D^(-1/6)`, equations (2.5), (3.2), and (3.3) would give the full
anisotropic Bessel target.  For `eta=D^(-7/48)`, equations (2.5), (3.5), and
(3.6) would close the current numerical deficit.

The proved curvature-jet inverse does not establish this statement.  It
recovers a **dual stationary mode and its saddle**.  The missing physical
step must show that a large quotient-jet cluster forces those recovered
dual saddles to select only `D^o(1)` of the primal rational tangents attached
to the product-band packets.  Approximate stationary localization, integer
Newton wraps, near-fold modes, and the varying stationary amplitude must all
be retained.  Merely observing that a dual saddle is near one packet is not
a coefficient-uniform Bessel intertwining.

This direction-only statement is strictly weaker than virtual-cubic
transference and avoids the support obstruction (1.10).  It remains genuine
new mathematics rather than a consequence of the existing exact inverse
formulas.

## 5. Reproducibility and status

The primitive cubic ray, synthesis lower bound, direction progression count,
content spacing gate, and exponent ledger are implemented in

```text
src/qp_high_p_jet_transference_gate.py
src/test_qp_high_p_jet_transference_gate.py
```

```text
primitive integral cubic ray:                         CLASSIFIED;
bounded supported cubic extraction cost >=p^3/(2H):  PROVED;
cost at the residual floor D^(61/160):                PROVED;
fixed-direction residual fiber O(1+B/p):              PROVED;
endpoint fiber exponent D^(329/480):                  PROVED;
fiber below the full D cluster ceiling:               PROVED;
fiber below the closing D^(49/48) ceiling:            PROVED;
sampled quotient jet -> primitive direction:           OPEN;
physical mask-sensitive Bessel theorem:                OPEN;
RSR / global fourth-trace assembly:                    OPEN;
sharp four-cycle bound:                                NOT PROVED.
```
