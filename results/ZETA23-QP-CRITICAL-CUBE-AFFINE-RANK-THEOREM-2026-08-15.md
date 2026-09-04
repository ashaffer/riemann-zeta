# QP four-cycle: critical-cube affine-rank theorem

**Date:** 2026-08-15  
**Verdict:** at the critical side length

```text
R=sqrt(D)=q^(8/33+o(1)),                            (0.1)
```

all active integer triples in any one `R by R by R` coordinate cube lie in
one rational affine plane.  This is an exact rank theorem, not a heuristic
linearization.  Each cube is therefore a legitimate local affine/Hankel
patch and has arbitrary-complex fourth trace `O(D)`.

The result does not by itself sum different cubes.  The remaining broad
problem is to control rectangles whose four corners couple several distinct
cube-planes.

---

## 1. Taylor identity with an integral determinant gap

Let `p0=(A,B,C)` be one active triple in a cube and put

```text
nabla=(BC,AC,AB).                                  (1.1)
```

For another point `p=p0+d`, `d=(x,y,z)`, exact expansion gives

```text
abc-ABC
 =d dot nabla+Cxy+Bxz+Ayz+xyz.                    (1.2)
```

Assume all shell coordinates are between fixed positive multiples of `q`,
the cube has side `R`, and

```text
|8abc-Q|<=H,          H<<qR^2.                     (1.3)
```

The difference of two active products is `O(H)`, while the nonlinear terms
in (1.2) are `O(qR^2+R^3)`.  Since `R=o(q)`, every active difference obeys

```text
|d dot nabla|<<qR^2.                               (1.4)
```

Suppose three active differences `d1,d2,d3` were linearly independent, and
let `V` be the integral matrix with these rows.  Then `det V` is a nonzero
integer, so `|det V|>=1`.  The system

```text
V nabla=e,              ||e||_infinity<<qR^2       (1.5)
```

and Cramer's rule give

```text
||nabla||_infinity<<qR^4.                          (1.6)
```

Indeed, each replaced-column determinant has one column of size `qR^2` and
two columns of size `R`, with only six determinant terms.

But every component of `nabla` is bounded below by a fixed multiple of
`q^2`.  At (0.1),

```text
qR^4=q^(65/33+o(1))=o(q^2),                        (1.7)
```

because `R^4/q=q^(-1/33+o(1))`.  Equations (1.6)--(1.7) contradict (1.1).
Thus no three active differences are independent.

### Theorem 1.1 (critical-cube affine rank)

For all sufficiently large `q`, every active point set in one critical cube
has affine rank at most two.  Since its differences are integral, its affine
hull is a rational plane (or a rational line or point in the lower-rank
cases).

---

## 2. Local fourth-trace consequence

Inside one cube there are at most `R+1` possible integer colors.  Pair
uniqueness makes every fixed-color slice a partial matching, and the row
interval contains at most `R+1` integers.  The affine coherence-patch theorem
therefore gives

```text
tr((A_cube A_cube*)^2)
 <=(R+1)^2 ||z_cube||_2^4
 <<D ||z_cube||_2^4.                               (2.1)
```

Writing a primitive normal as `(u,v,w)`, one can sharpen the fixed-color
matching length.  With `g=gcd(u,v)`, a fixed-color line advances by

```text
(Delta a,Delta b)=(v/g,-u/g),                      (2.2)
```

so

```text
L_cube<=1+min(Rg/|v|,Rg/|u|)
       <=1+Rg/max(|u|,|v|)                         (2.3)
```

when `uv!=0`, with the obvious one-coordinate interpretation otherwise.
Large primitive normals therefore give a stronger broad-cube coefficient

```text
M_cube L_cube<<R+D*g/max(|u|,|v|).                 (2.4)
```

Small normals are precisely the locally coherent/Hankel regime.

---

## 3. What remains

Partitioning the entire shell into critical cubes produces many rational
planes.  Fourth trace is not additive under an arbitrary sum of their
matrices, and a rectangle can place its four triples in four different
cubes.  A global proof still needs either:

1. almost orthogonality for distinct large-normal cube-planes;
2. a merger/packing theorem for overlapping small-normal planes; or
3. a broad incidence bound for cross-cube rectangles.

```text
critical-cube affine rank at most two:              PROVED;
local cube fourth trace O(D):                       PROVED;
primitive-normal local gain (2.4):                 PROVED;
cross-cube plane summation:                         OPEN;
global four-cycle bound:                            OPEN.
```

The exact Taylor identity, affine-rank ledger, and Cramer comparison are in
`src/qp_four_cycle_critical_cube.py` and
`src/test_qp_four_cycle_critical_cube.py`.

