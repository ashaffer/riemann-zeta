# Full reciprocal strip: local tangent packets and the projection gate

**Date:** 2026-08-24  
**Verdict:** the full product strip has a rigorous local structure theorem.
Every three occupied lattice points in a sufficiently short completion arc
of length `c*q^(1/3)` are exactly collinear, and each resulting affine packet
contains `O(1+sqrt(D/(P*Q)))` points.  At the critical scale this is at most
`O(sqrt(D))`.

This does not prove the global projected-energy estimate

```text
E^+(A_C) << D^(5/2+o(1)),
A_C={a asymp q: some integer v asymp q has |a*v-C|<=D}.       (0.1)
```

After local packets are removed, points separated by more than `q^(1/3)`
are invisible to the determinant argument.  An abstract scaled Behrend set
shows that the local theorem plus the reciprocal 3AP gap cannot by themselves
give any power saving over cubic energy.  The recent Jing--Wu algebraic-
surface energy theorem controls equality of all lifted coordinates, not the
energy of the first-coordinate projection; a concrete moment-curve example
rules out that inference.

## 1. The exact three-point determinant

Fix

```text
C asymp q^2,      q=D^(33/16),
P_C={(a,v) in Z^2:a,v asymp q, |a*v-C|<=D}.          (1.1)
```

For `a_1<a_2<a_3`, the reciprocal curve has the exact determinant

```text
det [1 a_i C/a_i]_(i=1)^3
 =C*(a_2-a_1)*(a_3-a_1)*(a_3-a_2)/(a_1*a_2*a_3).   (1.2)
```

Write an occupied carrier as

```text
v_i=C/a_i+theta_i,                 |theta_i|<=D/a_i. (1.3)
```

If `L=a_3-a_1` and `a_min=a_1`, multilinearity of the determinant gives

```text
|det [1 a_i v_i]|
 <= C*L^3/a_min^3 + 2*L*D/a_min.                    (1.4)
```

The determinant on the left is an integer.  Hence, whenever the right side
of `(1.4)` is less than one, all three lattice points are collinear.

On a fixed shell, `(1.4)` is

```text
O(L^3/q + L*D/q).                                   (1.5)
```

Choose a sufficiently small shell-dependent constant `c>0`.  For

```text
L<=c*q^(1/3),                                       (1.6)
```

the first term is below (say) `1/2`, while the second is

```text
D*q^(-2/3)=D^(-3/8).                                (1.7)
```

It follows that every triple of occupied points in such an arc is exactly
collinear.  If the arc contains at least two points, choosing those two as
anchors shows that all its occupied points lie on one affine line.

## 2. Each local line is a short tangent packet

Write the primitive direction of a decreasing nonhorizontal integer line as

```text
(Q,-P),                   P,Q>=1, gcd(P,Q)=1.        (2.1)
```

Along this line,

```text
(a_0+Q*k)*(v_0-P*k)
 =a_0*v_0+(Q*v_0-P*a_0)*k-P*Q*k^2.                  (2.2)
```

Thus the product has constant second difference `-2*P*Q`.  The preimage of
an interval of width `2D` under the quadratic in `(2.2)` is the union of at
most two intervals, of total length at most

```text
2*sqrt(2D/(P*Q)).                                   (2.3)
```

Consequently

```text
#(P_C intersect line) <=2+2*ceil(sqrt(2D/(P*Q)))
                       <<1+sqrt(D/(P*Q)).            (2.4)
```

A horizontal line has at most one occupied point once `D=o(q)`, since one
horizontal lattice step changes the product by `asymp q`.  In particular,
every local packet has `O(sqrt(D))` points.  This recovers the tangent-packet
scale without assuming that `C` is an integer or that a point has a fixed
product-error label.

## 3. A cubic finite-difference exclusion

For four completions in an arithmetic progression, direct subtraction gives

```text
Delta_r^3(C/a)
 =-6*C*r^3/[a(a+r)(a+2r)(a+3r)].                    (3.1)
```

The carrier third difference is integral and the four rounding errors add
`O(D/q)`.  If `|r|^3<<q^2`, integrality first forces that third difference to
vanish.  Substitution into `(3.1)` then forces

```text
|r|^3<<D*q.                                         (3.2)
```

There is therefore a forbidden cubic annulus

```text
(D*q)^(1/3)<<|r|<<q^(2/3).                          (3.3)
```

At `q=D^(33/16)`, its endpoints are

```text
D^(49/48)  and  D^(11/8).                           (3.4)
```

The macroscopic step `q/D=D^(17/16)` lies strictly inside this gap, with
margins `D^(1/24)` and `D^(5/16)` at the exponent level.  Hence a completely
occupied macroscopic arithmetic progression is impossible.  This is useful
rigidity, but it is still a finite-pattern statement.

The corresponding three-direction identity is

```text
Delta_r Delta_s Delta_u(C/a)
 =-6*C*r*s*u* integral_[0,1]^3
   (a+t_1*r+t_2*s+t_3*u)^(-4) dt_1 dt_2 dt_3.       (3.5)
```

It gives the same forbidden volume annulus

```text
D*q<<|r*s*u|<<q^2.                                  (3.6)
```

## 4. Why the `q^(1/3)` partition does not close energy

The preceding results control every occupied triple that fits inside one
short arc.  They do not constrain an isolated family with mutual completion
spacing greater than `q^(1/3)`.

This limitation is power-sharp as a matter of method.  Let `M asymp D`, take
a Behrend-type set

```text
B subset [1,M],       |B|=M^(1-o(1)),       B has no 3AP,    (4.1)
```

and form the abstract completion set

```text
A_*=a_0+g*B,                    g asymp q/D.          (4.2)
```

At the critical scale,

```text
g/q^(1/3)=D^(3/8).                              (4.3)
```

Thus every `q^(1/3)` arc contains at most one point of `A_*`, and the 3AP
gap sees nothing.  Nevertheless Cauchy--Schwarz gives

```text
E^+(A_*)=E^+(B)>=|B|^4/|B+B|=D^(3-o(1)).            (4.4)
```

This is deliberately **not** a construction inside the physical product
strip.  It proves exactly that local determinant packets, partitioning, and
3AP exclusion alone cannot establish `(0.1)`.  The missing input must use the
individual product bands on the isolated, macroscopically separated points.

## 5. A genuine global gain on one macroscopic progression

The individual product bands do rule out the abstract fixture `(4.2)` if it
is required to be physical.  This follows from the `k=4` theorem of Huxley
and Sargos for integral points close to a smooth curve; a corrected detailed
proof and the precise bound used here are given in
[Zhao's exposition](https://arxiv.org/abs/2407.01778).

Let

```text
a=a_0+R*k,        1<=k<=M,        M<=q/R,            (5.1)
f(k)=C/(a_0+R*k),              delta=D/q.             (5.2)
```

On a fixed shell,

```text
|f^(4)(k)| asymp R^4/q^3.                            (5.3)
```

The Huxley--Sargos bound with derivative order four gives

```text
# {k: ||f(k)||<=delta}
 << M*(R^4/q^3)^(1/10)
    +M*(D/q)^(1/6)
    +D^(1/4)*q^(1/2)/R+1.                            (5.4)
```

For a macroscopic progression, `R>=q/D` and `M<=q/R`.  Every term decreases
as `R` increases, so it is enough to insert `R=q/D`, `M=D`.  At
`q=D^(33/16)`, the three powers in `(5.4)` are respectively

```text
D^(129/160),       D^(79/96),       D^(7/32).        (5.5)
```

Therefore

```text
#(A_C intersect (a_0+R*[1,M]))
 <<D^(79/96+o(1))=D^(5/6-1/96+o(1)).                (5.6)
```

for `R>=q/D` (the very-large-`R` range is also immediate from `M<=q/R`).
So a physical `q/D`-dilate of the Behrend fixture cannot have the size used
in `(4.4)`.  This is a real use of all the product bands and a useful inverse
test: any proof reducing excessive energy to more than `D^(5/6)` points on
one macroscopic progression would close that branch.

What is not currently available is such a rank-one inverse theorem at the
`D^(5/2)` energy threshold.  Balog--Szemeredi--Gowers can return a structured
core, but its quantitative output may be a higher-rank generalized
progression and may be much smaller than `D^(5/6)`.  Thus `(5.6)` eliminates
the cleanest high-step-AP counterexample without proving `(0.1)`.

## 6. Jing--Wu controls the lift, not its projection

Jing and Wu prove that if a finite set `X` lies on an irreducible algebraic
surface in `R^3`, then its **vector** additive energy is

```text
E_R3(X)<<Lambda_F(X)*|X|^(2+epsilon),                (5.1)
```

where `Lambda_F` is the maximum concentration on an affine line contained in
the surface.  See [Theorem 1.1 of Jing--Wu](https://arxiv.org/abs/2608.14467).

The physical lift

```text
X_C={(a,v,e):a*v=N+e} subset Z(a*v-e-N)              (5.2)
```

does lie on a quadratic surface.  But `(5.1)` counts quadruples whose `a`,
`v`, **and** `e` sums all agree.  The desired energy imposes only equality of
the `a` sums and coherently sums over the other two mismatches.

There can be no general projection step.  On the irreducible quadratic
surface

```text
Z(z-x*y),                                           (5.3)
```

take

```text
X_n={(k,k^2,k^3):1<=k<=n}.                          (5.4)
```

No three moment-curve points are collinear, so `Lambda_F(X_n)<=2`, and
Jing--Wu gives near-quadratic vector energy.  Yet the first projection is the
interval `[1,n]`, whose ordered energy is exactly

```text
E^+([1,n])=(2*n^3+n)/3.                             (5.5)
```

The new surface theorem is therefore inapplicable to `(0.1)` unless it is
supplemented by a genuinely projection-sensitive or mismatch-sensitive
estimate.

## 7. Status

```text
three-point reciprocal determinant identity:       PROVED;
q^(1/3) local arc forces one affine line:            PROVED;
line packet size O(1+sqrt(D/(P*Q))):                 PROVED;
cubic AP / cube-volume forbidden annulus:            PROVED;
partition plus 3AP gap gives global energy saving:   NO (Behrend fixture);
physical macroscopic AP has <=D^(79/96+o(1)) points:  PROVED (Huxley--Sargos);
energy >D^(5/2) forces >D^(5/6) in one such AP:       OPEN;
Jing--Wu surface energy controls first projection:   NO (moment curve);
full-strip energy D^(5/2+o(1)):                      OPEN;
packet-free broad reciprocal energy:                 OPEN.
```

The exact identities and exponent margins are replayed in
`src/qp_full_strip_local_packet_gate.py` and
`src/test_qp_full_strip_local_packet_gate.py`.
