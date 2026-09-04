# QP four-cycle: dominant tangent packets have the sharp high-completion tail

**Date:** 2026-08-22  
**Verdict:** the proposed high-completion tail is true, with the sharp
`D/K` strength, for every parabolic color whose completion multiplicity is
carried by one dominant affine/Hankel line.  More quantitatively, if the
largest occupied line contains at least a `1/J` fraction of the completions,
then

```text
sum_(C in the K-tail) w_z(C)
 <<J*D/K*q^o(1)*||z||_2^4.                         (0.1)
```

Thus `J=q^o(1)` gives exactly the desired tail, and its direct fourth-trace
contribution is `D q^o(1)||z||_2^4` after dyadic summation in `K`.

The same conclusion holds under the more invariant hypothesis that one
rational completion plane contains a `1/J` fraction of the completions.
The fixed-plane conic dichotomy makes a power-rich plane parabolic and
splits it into only `q^o(1)` affine lines, reducing it to the theorem above.
Thus all genuinely plane-coherent high-completion colors are closed.

This is a genuine packet-merger theorem, but it also identifies its exact
scope boundary.  A high-multiplicity color may occupy `asymp K` distinct
one- or two-point affine lines.  Such a color has no dominant line, and the
curvature argument below says nothing.  After all rich fixed-direction
packets have been merged, this varying-secants family is the sole residual
high-completion obstruction.

No uniform four-cycle bound is claimed here.

---

## 1. Setup and the two existing inputs

Normalize `||z||_2=1` and write

```text
w_z(C)=|z_x z_y z_u z_v|
```

for a nonzero-determinant color matrix `C=(x,y;u,v)`.  In the parabolic
branch, let

```text
e_C=r_C s_C^T,       h_C=max_(i,j)|(e_C)_ij|       (1.1)
```

be its assigned primitive rank-one direction.  The gap-token aggregation
theorem proves, uniformly for every dyadic `H`,

```text
sum_(C assigned, H<=h_C<2H) w_z(C)
 <<sqrt(D*H)*q^o(1).                               (1.2)
```

The estimate is coefficient-uniform and already includes the bounded chart,
sign, and dyadic multiplicities.

Every maximal occupied affine carrier line has a primitive parametrization

```text
a(t)=a_0+t*A*r_C,       b(t)=b_0+t*B*s_C,
gcd(A,B)=1.                                             (1.3)
```

Put `n=|A*B|>=1`.  The exact quadratic coefficient of the product-matrix
line is `A*B*e_C`.  Comparing any entry on which
`|(e_C)_ij|=h_C` at three occupied parameters in the common product window
gives the established curvature bound

```text
n*h_C*(T-1)^2 <<D,                                  (1.4)
```

where `T` is the number of occupied integer parameters on the line.  In
particular, for `T>=2`,

```text
h_C <<D/T^2.                                        (1.5)
```

Notice that discarding `n` in (1.4) only weakens the estimate, so no
direction summation or normalized-GCD hypothesis is hidden here.

---

## 2. The dominant-packet tail theorem

Fix dyadic `K>=2` and `J>=1`.  Let `F(K,J)` be any family of assigned
parabolic colors such that

```text
K<=m(C)<2K                                             (2.1)
```

and some one maximal affine line of `C` contains

```text
T_C>=K/J                                             (2.2)
```

occupied parameters.  Assume `K/J>=2`; the complementary bounded range is
absorbed by the already closed repeated sectors.

Equations (1.5) and (2.2) imply

```text
h_C <<D*J^2/K^2.                                    (2.3)
```

Sum (1.2) over the logarithmically many dyadic heights below the right side
of (2.3).  Since the geometric series `sum_(H<=H_0) sqrt(H)` is
`O(sqrt(H_0))`,

```text
sum_(C in F(K,J)) w_z(C)
 <<sqrt(D)*sqrt(D*J^2/K^2)*q^o(1)
 <<J*D/K*q^o(1).                                    (2.4)
```

Restoring the norm proves (0.1).  Multiplying by `m(C)<2K` gives

```text
sum_(C in F(K,J)) m(C)w_z(C)
 <<J*D*q^o(1)||z||_2^4.                             (2.5)
```

There are only `O(log q)` multiplicity bins.  Consequently every family in
which the largest line carries a `q^(-o(1))` fraction of each color's
completions contributes

```text
<<D*q^o(1)||z||_2^4                                (2.6)
```

to the direct fourth trace.

The argument also proves the literal tail formulation requested in the
packet strategy:

```text
T_C>=K*q^(-o(1))
  ==> sum_(C: K<=m(C)<2K) w_z(C)
      <<D/K*q^o(1)||z||_2^4.                        (2.7)
```

There is no mismatch between `m(C)` and line occupancy: it is precisely the
explicit dominance hypothesis (2.2).  The proof never silently replaces
the total completion count by a line length.

---

## 3. Packet interpretation

A literal long line is the coherent tangent/Hankel object.  Merging its
colors before taking the fourth trace already gives the local `O(D)` packet
bound.  The theorem above adds a global weighted fact: even when the color
matrices and packet bases vary, colors supporting a line of length `T` have
total determinant-band mass `O(D/T)`.  Thus coherent packets cannot create
the missing `D^(1/4)` loss.

This is stronger than summing an `O(D)` estimate over packet labels.  It
uses the packet length to force the relation height down to `D/T^2`, then
uses the square-root height law (1.2).  The two square roots cancel exactly.

### Plane-coherent corollary

Let `F_plane(K,J)` consist of color matrices with `m(C)~K` for which one
rational affine two-plane contains at least `K/J` of the actual completion
product matrices.  The plane includes the fixed integral level and one
independent secant relation.

Its intersection with `det M=0` is a binary conic.  The proved conic
dichotomy says

```text
nonparabolic plane:   q^o(1) actual points;
parabolic plane:      q^o(1) affine rational-tangent charts. (3.1)
```

Reducible sections contain only `O(1)` actual completions unless they are
already affine-line cases.  If `K/J` is a fixed power of `q`, the selected
plane is consequently parabolic, and one of its charts has

```text
T_C >=K/(J*q^o(1)).                                  (3.2)
```

Assign that chart's primitive rank-one direction to `C` and apply Section
2.  The gap-token theorem permits an arbitrary deterministic assignment of
one occupied relation to each color, so this selection creates no overlap
loss.  We obtain

```text
sum_(C in F_plane(K,J)) w_z(C)
 <<J*D/K*q^o(1)||z||_2^4,                           (3.3)

sum_(C in F_plane(K,J)) m(C)w_z(C)
 <<J*D*q^o(1)||z||_2^4.                             (3.4)
```

If `K/J=q^o(1)`, the ordinary determinant-layer mass gives (3.3), because
its right side is then `Dq^o(1)`.  Multiplication by `m(C)<2K` gives (3.4)
since `K/J=q^o(1)`.  Thus the corollary, with the usual absorption of
subpowers, covers every range.

This proves the packet strategy's coherent half: high completion
multiplicity cannot remain expensive inside one rational tangent plane.
The remaining colors must distribute their completions over polynomially
many genuinely different secant planes.

---

## 4. Exact residual family

For a color with no dominant line, write its occupied maximal lines as
`L_1,...,L_R`.  The unresolved case has

```text
m(C)~K,       max_nu |L_nu|=K*q^(-Omega(1)),        (4.1)
```

and at the sharp endpoint it may have `R~K` lines containing only one or
two actual parameters each.  Three points expose the quadratic curvature
and enter the fixed-direction merger; one- and two-point secants do not pin
their intercepts.

Within the parabolic remainder, the exact mask-preserving labels are the wedge tokens

```text
(r_C, alpha),       alpha=det(r_C,a),
(s_C, beta),        beta=det(s_C,b).                (4.2)
```

Together with the normalized primitive multiplier data they retain the
actual carrier pairs and do not complete the prime-power mask to a
rectangle.  The known normalized-GCD identity gives the correct
`ell^2` kernel between the two token axes.  What is not known is the Bessel
estimate saying that a fixed color-gap token has only `q^o(1)` total energy
over its varying actual wedge lifts.  Equivalently, the remaining theorem is
a square-function bound for the varying one-/two-point secants in (4.2).

Ordinary Cotlar orthogonality cannot provide it: at fixed color determinant
all secant layers are restrictions of the same partial permutation, so a
single common color makes their cross norm one.  The wedge coordinate must
remain present until after the actual-mask energy estimate.

```text
dominant-line D/K color-mass tail:                  PROVED;
dominant-line direct FC contribution:               PROVED;
arbitrary complex coefficient vector:               INCLUDED;
fixed-direction rich-line merger:                   PROVED PREVIOUSLY;
plane-coherent D/K tail and direct FC:               PROVED;
mask-preserving wedge-token coordinates:            EXACT;
varying one-/two-point wedge-lift Bessel bound:       OPEN;
uniform high-completion tail:                        OPEN;
uniform four-cycle bound:                            OPEN.
```

The scale cancellation and finite quadratic identity are replayed in
`src/qp_dominant_tangent_packet_tail.py` and its test module.

---

## 5. Exact defect-plane form of the wedge label

There is a particularly clean actual-mask-preserving realization of (4.2).
For one completion put

```text
delta_1=x*b_1-y*b_2,       delta_2=u*b_1-v*b_2.    (5.1)
```

The two product windows sharing the first, respectively second, row give

```text
|delta_1|+|delta_2|<<D.                             (5.2)
```

Use the primitive parabolic gap equations

```text
r_1*x-r_2*u=-s_2*theta,
r_1*y-r_2*v=-s_1*theta,                             (5.3)
```

and define the actual column wedge

```text
beta=det(s,b)=s_1*b_2-s_2*b_1.                     (5.4)
```

Direct substitution, with no approximation, gives

```text
r_1*delta_1-r_2*delta_2=theta*beta.                 (5.5)
```

Thus every maximal affine carrier line is sent to an integral line in the
`(delta_1,delta_2)` square.  Its primitive direction is `(r_2,r_1)` (up to
the harmless sign convention), and its intercept is exactly `theta*beta`.
The raw carrier multiplier changes the spacing of occupied points but not
the line label.  The row-side identity is the transpose:

```text
s_1*epsilon_1-s_2*epsilon_2=eta*alpha.              (5.6)
```

Here `epsilon_1,epsilon_2` are the analogous vertical product defects and
`alpha=det(r,a)`.

The defect coordinate itself is lossless.  Fix an ordered pair of distinct
actual colors `(x,y)` and an integer `delta`.  All integer solutions of

```text
x*b_1-y*b_2=delta                                  (5.7)
```

differ by an integral multiple of `(y,x)`, since `gcd(x,y)=1`.  The project
shell has diameter smaller than both `x` and `y`, so at most one solution
lies in the shell.  Reversing colors and carriers proves that, for fixed
`delta`, (5.7) is a partial matching between actual color pairs and actual
carrier pairs.  The common row is then unique because its product interval
has length `O(D/q)<1`.

There is also an exact local coordinate formula.  Freeze primitive `s`, a
top gap token

```text
d=s_1*x-s_2*y !=0,                                 (5.8)
```

and a wedge `beta`.  The transform

```text
(b_1,b_2) -> (beta,delta)
```

has determinant `-d`, and its inverse is

```text
b_1=(y*beta+s_1*delta)/d,
b_2=(x*beta+s_2*delta)/d.                           (5.9)
```

In particular the prime-power mask is simply imposed on the two explicit
integer values in (5.9); no rectangular completion is needed.  Along the
integer line with fixed `beta`,

```text
b(t)=b(0)+t*s,       delta(t)=delta(0)+t*d.         (5.10)
```

The band (5.2) therefore contains at most

```text
1+O(D/|d|)                                           (5.11)
```

actual lifts for a fixed `(s,d,beta)` token.  The case `d=0` is absent in
the active range: primitivity and coprimality would force `s` proportional
to `(y,x)`, whose coordinates have size `asymp q`, whereas `||s||<<D=o(q)`.

Equations (5.5) and (5.9) identify the sought orthogonal label as far as
geometry permits:

```text
(r,theta,beta; delta_1,delta_2),                    (5.12)
```

or its row transpose.  Rich parallel lines merge by the existing
fixed-direction Hankel theorem.  The residual consists of one or two
prime-masked lattice points on each of many intercepts `theta*beta`.

The defect layers are partial matchings, but they are not Cotlar-orthogonal.
If the same carrier pair supports legal paths in two defect layers, the
cross product of the corresponding partial permutations contains a matrix
unit and has operator norm one.  Therefore (5.12) does not, by itself,
prove a square-function estimate.  What would finish the argument is an
actual-mask Bessel theorem for the explicit lattice values (5.9), after
the rich intercepts have been merged.  It must average the varying
intercepts before taking absolute values; a positive completion in
`(beta,delta)` recreates the known false alias.

Outside the parabolic remainder the analogous label is the primitive
secant-triangle normal.  Any color with polynomial multiplicity supplies
many triples of completions.  If a positive proportion of those
completions lay in one rational two-plane, the plane-coherent corollary
would apply.  Thus the final broad family is a weighted aggregation over
varying triangle normals, equivalently over variable-coefficient Pluecker
systems.  Finite actual-prime examples show that these normals really can
vary and need not be parabolic, although every fixed bounded-multiplicity
family is already harmless by the determinant-layer theorem.

```text
small-defect coordinates (5.1)--(5.2):             PROVED;
wedge/intercept identity (5.5):                    PROVED;
fixed-defect partial matching:                     PROVED;
explicit mask-preserving inverse (5.9):            PROVED;
fixed-wedge lift cap (5.11):                       PROVED;
bare cross-defect Cotlar decay:                    FALSE;
scattered-intercept actual-mask Bessel theorem:    OPEN.
```
