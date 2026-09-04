# QP product-error cubes: exact rigidity and the remaining recurrence gate

**Date:** 2026-08-24  
**Verdict:** the product errors do more than control the mixed carrier label.
They give an exact cube-separation theorem and exclude every balanced broad
`3 x 2` occupied strip.  A sufficiently short four-term completion AP also
has affine carrier and is therefore a true packet.  These statements are
fully proved below.

They do **not** yet prove packet-free reciprocal energy `D^(5/2+o(1))`.
The unproved step is a combinatorial recurrence theorem saying that excess
broad-rectangle energy in the physical product bands forces one of the
forbidden strips/APs.  Additive energy alone cannot supply that recurrence.

Throughout, `E=C_0 D`, the positive shell is

```text
lambda*q <= a,b,v <= Lambda*q,
q=D^(33/16),
```

and every occupied point satisfies

```text
e^a=a*v-C_a,       e^b=b*v-C_b,
|e^a|,|e^b|<=E.                                      (0.1)
```

All constants below may depend on the fixed shell and `C_0`, but not on
`D`.  The second product coordinate is needed only for the determinant
eliminations; the recurrence exclusions already follow from `e^a`.

## 1. Exact rectangle algebra

Let a completion rectangle have base `P=(a,b)` and directions

```text
U=(r,p),       V=(s,ell).
```

Write

```text
rho   = Delta_U v,
sigma = Delta_V v,
tau   = Delta_U Delta_V v,
A     = Delta_U Delta_V e^a,
B     = Delta_U Delta_V e^b.                         (1.1)
```

Direct expansion, with no approximation, gives

```text
A=s*rho+r*sigma+(a+r+s)*tau,
B=ell*rho+p*sigma+(b+p+ell)*tau.                     (1.2)
```

In particular `|A|,|B|<=4E`.  Put

```text
alpha=det(P,U)=a*p-b*r,
beta =det(P,V)=a*ell-b*s,
Delta=det(U,V)=r*ell-p*s.                            (1.3)
```

Eliminating one first carrier difference at a time gives the two exact
wedge laws

```text
p*A-r*B   =-Delta*rho+(alpha-Delta)*tau,
ell*A-s*B = Delta*sigma+(beta+Delta)*tau.            (1.4)
```

For completeness, let

```text
kappa=x*a-y*b,
d_U=x*r-y*p,
d_V=x*s-y*ell.
```

Then the determinant coordinates obey

```text
y*alpha=r*kappa-a*d_U,
y*beta =s*kappa-a*d_V,
y*Delta=s*d_U-r*d_V,                                 (1.5)
kappa*Delta-d_U*beta+d_V*alpha=0.                    (1.6)
```

Thus `alpha,beta,Delta=O(D)` under the physical defect bounds.  If the two
centres come from one product target, so `x*C_a=y*C_b`, the pointwise error
relation is also exact:

```text
y*e^b=x*e^a-kappa*v.                                 (1.7)
```

Equations `(1.2)--(1.7)` are the complete two-dimensional product-error,
carrier, and defect-determinant algebra.

## 2. Exact cube algebra and its determinant eliminations

Add a third completion direction `H=(h,g)` and suppose all eight cube
vertices are occupied.  Define

```text
tau_UV=Delta_U Delta_V v,
tau_UH=Delta_U Delta_H v,
tau_VH=Delta_V Delta_H v,
omega =Delta_U Delta_V Delta_H v,
A_3   =Delta_U Delta_V Delta_H e^a,
B_3   =Delta_U Delta_V Delta_H e^b.                  (2.1)
```

The exact third-order Leibniz laws are

```text
A_3=(a+r+s+h)*omega
      +h*tau_UV+r*tau_VH+s*tau_UH,
B_3=(b+p+ell+g)*omega
      +g*tau_UV+p*tau_VH+ell*tau_UH.                 (2.2)
```

Here `|A_3|,|B_3|<=8E`.  More generally, for completion increments
`h_1,...,h_m` in the `a` coordinate,

```text
Delta_1...Delta_m(a*v)
 =(a+sum_i h_i)*Delta_1...Delta_m v
  +sum_i h_i*product_(j!=i) Delta_j v.               (2.3)
```

This formula remains valid with repeated directions.

There are three exact cube wedge laws.  Set

```text
gamma   =det(P,H)=a*g-b*h,
Delta_HU=det(H,U)=h*p-g*r,
Delta_HV=det(H,V)=h*ell-g*s.                         (2.4)
```

Then

```text
p*A_3-r*B_3
 =Delta_HU*tau_UV-Delta*tau_UH
   +(alpha-Delta+Delta_HU)*omega,

ell*A_3-s*B_3
 =Delta_HV*tau_UV+Delta*tau_VH
   +(beta+Delta+Delta_HV)*omega,

g*A_3-h*B_3
 =-Delta_HU*tau_VH-Delta_HV*tau_UH
   +(gamma-Delta_HU-Delta_HV)*omega.                 (2.5)
```

As one rigidity consequence, suppose translation by `H` preserves the
three labels `tau_UV,A,B`.  Then `omega=A_3=B_3=0`, and `(2.2)` gives

```text
Delta*tau_VH=-tau_UV*det(H,V),
Delta*tau_UH= tau_UV*det(H,U).                       (2.6)
```

If `Delta=0` and `tau_UV!=0`, the translation `H` is completion-collinear
with both `U` and `V`.  For `Delta!=0`, both new curvatures are locked to
determinant ratios.  This is an exact controlled-error recurrence theorem,
not a pigeonhole assertion that the labels must recur.

## 3. Reciprocal rounding with signs

From the first product band,

```text
v(a)=C_a/a+zeta(a),        |zeta(a)|<=E/(lambda*q).  (3.1)
```

For positive increments `t_1,...,t_m`, repeated integration gives

```text
Delta_(t_1)...Delta_(t_m)(C_a/a)
 =(-1)^m*m!*C_a*product_i(t_i)
   * integral_[0,1]^m
       (a+sum_i theta_i*t_i)^(-m-1) dtheta.          (3.2)
```

Its magnitude is comparable to

```text
product_i(t_i)/q^(m-1),                              (3.3)
```

and the error finite difference is at most `2^m E/(lambda*q)`.
At the present scale

```text
E/q << D/q = D^(-17/16).                             (3.4)
```

Consequently every integer second carrier difference in positive
directions is nonnegative for large `D`.  Also, for a sufficiently small
fixed `c_3>0`,

```text
h*r*s<=c_3*q^2
   => Delta_H Delta_U Delta_V v=0                   (3.5)
```

whenever `h,r,s>0` and all eight vertices are occupied.  Notice that
`(3.5)` uses the full error size `8E/q`; there is no silent rounding of an
`O(1)` quantity.

## 4. Cube-separation theorem for a broad rectangle

Assume `h,r,s>0` and let the bottom rectangle have

```text
tau=tau_UV>=1.                                       (4.1)
```

If `hrs<=c_3q^2`, equation `(3.5)` makes `omega=0`.  All three pair
curvatures in `(2.2)` are nonnegative, so

```text
8E>=|A_3|=A_3
   =h*tau+r*tau_VH+s*tau_UH
   >=h*tau.                                          (4.2)
```

This proves the exact dichotomy

```text
h<=8E/tau        or        h*r*s>c_3*q^2.            (4.3)
```

If `r*s>=Bq` for a sufficiently large fixed broadness constant `B`, the
second reciprocal identity gives `tau asymp rs/q`.  Thus `(4.3)` becomes

```text
h << D/tau       or        h >> q/tau.               (4.4)
```

There is a forbidden translated-base annulus between these alternatives.
Its scale ratio is

```text
(q/tau)/(D/tau)=q/D=D^(17/16).                       (4.5)
```

No equality of the top and bottom mixed labels was assumed: in the low
volume branch it follows automatically from `omega=0`.

### Corollary 4.1 (three broad faces force large cube volume)

Suppose all three direction pairs are broad, in the fixed-constant sense

```text
r*s, r*h, s*h >=b_0*q,       b_0>0 fixed.            (4.6)
```

After independently reversing cube directions, one may take `r,s,h>0`;
the same eight vertices remain occupied.  Formula `(3.2)`, the `o(1)`
rounding error, and `(4.6)` give

```text
tau_UV asymp r*s/q,
tau_UH asymp r*h/q,
tau_VH asymp s*h/q,                                  (4.7)
```

with all three integers positive.  If `r*s*h<=c_3q^2`, then `omega=0`,
and `(2.2)` yields

```text
8E>=A_3
 >=c*(h*r*s/q+r*s*h/q+s*r*h/q)
 >=c*r*s*h/q.                                        (4.8)
```

Thus `r*s*h<<Eq`.  On the other hand, multiplication of the three
inequalities in `(4.6)` gives

```text
r*s*h>=b_0^(3/2)*q^(3/2).                            (4.9)
```

At `q=D^(33/16)` these bounds are incompatible for large `D`, because

```text
q^(3/2)/(D*q)=sqrt(q)/D=D^(1/32).                   (4.10)
```

Consequently every occupied cube with three broad direction-pairs obeys

```text
r*s*h>c_3*q^2.                                       (4.11)
```

All eight `a`-coordinates lying in the fixed positive shell are enough for
this proof: after the sign reversals, the integration box in `(3.2)` lies
between its minimum and maximum occupied vertices and hence stays in the
same shell.  No monotonicity of the `b`-coordinate is needed.

A related monotonicity statement is useful.  If several rectangles have
the same full positive directions `U=(r,p)`, `V=(s,ell)` and the same
`tau`, order their bases by increasing `a`.  For two bases separated by
`H=(h,g)` with `h>0`,

```text
A(top)-A(bottom)
 =h*tau+r*tau_VH+s*tau_UH >=h*tau.                  (4.12)
```

Since every `A` lies in `[-4E,4E]`, there are at most

```text
1+8E/tau                                             (4.13)
```

such bases.  Fixing `(U,V,tau,A)` fixes at most one base `a`-coordinate
(and hence at most one physical base by fibre uniqueness).  This statement
does not hold if only the first components `(r,s)` are fixed.  Summing the
possible `A` labels, however, does not by itself prove the desired global
energy bound.

## 5. A four-term AP forces a true packet in the middle range

Suppose four occupied points form a completion AP

```text
P, P+U, P+2U, P+3U,            U=(r,p), r>0.         (5.1)
```

For `e=e^a`, repeated `(2.3)` is

```text
Delta_r^3 e=(a+3r)*Delta_r^3 v+3r*Delta_r^2 v.       (5.2)
```

If `r^3<=c_3q^2`, reciprocal rounding gives `Delta_r^3v=0`.  Since the
left side of `(5.2)` has magnitude at most `8E`,

```text
r>8E/3  =>  Delta_r^2v=0.                            (5.3)
```

Thus all four carrier values are affine and `(5.1)` is a true full affine
packet.  A packet-free completion 4-AP therefore has the dichotomy

```text
r=O(D)       or       r >> q^(2/3)=D^(11/8).         (5.4)
```

More generally, an occupied completion AP of length `m+1` obeys

```text
r^m<=c_m q^(m-1),  r>C_mD
   => Delta_r^2v=...=Delta_r^m v=0.                 (5.5)
```

Indeed rounding first kills `Delta_r^m v`, and the exact identity

```text
Delta_r^j e=(a+jr)*Delta_r^jv+jr*Delta_r^(j-1)v     (5.6)
```

then descends one degree at a time.  This is a proved packet-rigidity
lemma, with no density assumption.

## 6. Balanced broad rectangles cannot form a `3 x 2` strip

Suppose all six points

```text
P+iU+jV,          i=0,1,2,  j=0,1                  (6.1)
```

are occupied, with `r,s>0`.  Assume

```text
tau_UV>=1,       r^2*s<=c_3q^2.                     (6.2)
```

Rounding gives `Delta_U^2 Delta_Vv=0`.  The repeated-direction instance
of `(2.3)` is

```text
Delta_U^2 Delta_V e^a
 =2r*tau_UV+s*Delta_U^2v.                            (6.3)
```

Both carrier differences on the right are nonnegative.  Since the left
has magnitude at most `8E`, `(6.3)` forces

```text
r<=4E.                                               (6.4)
```

Therefore no such broad strip exists when `r>4E`.  Symmetrically, a
`2 x 3` strip with `r*s^2<=c_3q^2` forces `s<=4E`.

At the balanced broad scale,

```text
r,s asymp sqrt(q)=D^(33/32),
r^2*s,s^2*r asymp q^(3/2)<<q^2,
r,s>D,                                               (6.5)
```

so neither extension is possible.  Broad rectangles at this scale are
rigorously isolated from concatenation in their own completion directions.

## 7. Exact stopping point

The proved conclusions are:

```text
rectangle and cube product-error Leibniz laws:       PROVED;
all 2D/3D determinant eliminations:                  PROVED;
broad translated-base forbidden annulus:             PROVED;
middle-range completion AP forces a packet:          PROVED;
balanced broad 3 x 2 and 2 x 3 strips impossible:    PROVED.
```

What is not proved is

```text
more than D^(5/2+o(1)) broad rectangles
   => a forbidden AP or 3 x 2 recurrence.            OPEN.              (7.1)
```

This implication is false for an arbitrary subset of an interval:
three-AP-free Behrend-type sets can still have additive energy
`D^(3-o(1))`.  A valid proof of `(7.1)` must use the individual physical
product bands across many rectangles, not energy or packet-freeness alone.
Accordingly, the packet-free reciprocal-energy theorem and the sharp
four-cycle bound remain open at precisely this recurrence gate.

There is a sharp way to see why Corollary 4.1 alone does not close the
count.  Embed the defect set in a cyclic group of size `N asymp D` without
wraparound.  Gowers--Cauchy--Schwarz gives

```text
#(occupied additive 3-cubes) >= E^+(K)^2/N^2.        (7.2)
```

Thus energy `D^(5/2+epsilon)` produces `D^(3+2epsilon)` cubes.  Cubes with
a narrow direction-pair contribute at most

```text
O(D)*E_narrow=O(D^3 log q),                          (7.3)
```

so an epsilon-power excess does force many cubes with three broad faces.
Corollary 4.1 sends them to the large-volume sector `r*s*h>>q^2`, but the
raw defect parametrization `(base,d,e,f)` still permits `O(D^4)` such
cubes.  No proved estimate reduces that sector to `D^(3+o(1))`.  Such an
upper bound would, through `(7.2)`, prove PFRE immediately; it is a precise
equivalent next gate rather than a consequence of the present cube
algebra.

The exact identities are machine-replayed in
`src/qp_product_error_cube_algebra.py`; focused tests are in
`src/test_qp_product_error_cube_algebra.py`.
