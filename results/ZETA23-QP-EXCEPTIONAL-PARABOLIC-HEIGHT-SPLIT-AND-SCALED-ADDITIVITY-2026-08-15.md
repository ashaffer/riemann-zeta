# QP four-cycle: exceptional parabolic height split and scaled additivity

**Date:** 2026-08-15  
**Verdict:** the exceptional rank-two-plane sector admits a stronger global
weighted bound than the pointwise `sqrt(D)` estimate.  Its completed
all-distinct color mass satisfies

```text
Q_exceptional(z)<<D^(11/8)q^o(1)||z||_2^4.        (0.1)
```

The proof measures the primitive rank-one direction at infinity of each
parabolic chart.  A direction of height `h` supports at most
`sqrt(D/h)q^o(1)` completions of one color, while there are only
`H^2q^o(1)` primitive rank-one directions of height at most `H`.

This is an exceptional-sector theorem only.  Generic rank-three difference
lattices are not parabolic and are not covered.  They can still have the
currently proved multiplicity `D^(15/32+o(1))`, larger than the splitting
threshold `D^(3/8)`.  Therefore (0.1) does **not** prove a global
`D^(11/32)` carry operator or transverse exponent `2/3`.

The exact algebra also corrects a tempting overstatement.  A parabolic chart
does not force the raw colors to form an additive rectangle.  It forces only
diagonally scaled additivity:

```text
r1*s1*c11+r2*s2*c22=r1*s2*c12+r2*s1*c21.          (0.2)
```

Accordingly the color determinant still factors, but with the slope-height
factor attached.  An explicit long active integer chart below has
`det C=-250` and raw additive defect `-5`; thus ordinary additive-grid
closure is false without extra prime-power input.

---

## 1. Prior exceptional-plane classification

For one all-distinct color matrix `C`, let `m(C)` be its number of product-
matrix completions and let

```text
w_z(C)=|z_c11 z_c12 z_c21 z_c22|,       ||z||_2=1.
```

The successive-minima theorem divides the fixed-color problem into a
generic rank-three difference-lattice branch and an exceptional branch in
which every product matrix lies in one rational affine two-plane.  The
parabolic inverse theorem then gives the following dichotomy inside the
exceptional branch:

```text
nonparabolic plane conic:    m(C)<<q^o(1);
parabolic plane conic:       q^o(1) rational affine-carrier charts. (1.1)
```

The determinant-layer theorem supplies, for all colors and hence for the
exceptional subset,

```text
sum_C w_z(C)<<Dq^o(1).                            (1.2)
```

Finally, for every primitive rank-one integral relation `e`, the fixed-
relation theorem gives

```text
sum_(C:e kills C) w_z(C)<<sqrt(D)q^o(1).           (1.3)
```

---

## 2. Denominators and the primitive quadratic direction

Take one rational parabolic chart in (1.1).  After fixing its denominator,
carrier-gcd class, and parameter congruence, and then replacing the
parameter by the integer coordinate on that progression, its product
matrices have the form

```text
M(n)=M0+nM1+n^2 M2,                 n in Z,         (2.1)
```

and are integral at every admissible integer `n`.  The matrix `M2` is a
nonzero rational scalar multiple of one primitive rank-one integer matrix

```text
e,                     h=||e||_infinity.           (2.2)
```

There is no denominator loss in the lower bound for the quadratic
coefficient.  Since an integer-valued quadratic polynomial has integral
second difference,

```text
2M2=Delta^2 M(n) in Mat_2(Z).                      (2.3)
```

Primitivity of `e` therefore implies

```text
2M2=g e                 for some nonzero g in Z,
||M2||_infinity>=h/2.                              (2.4)
```

This is also why passing to a sparse parameter congruence is harmless: its
step is already included in (2.1), and can only enlarge the quadratic
coefficient.

For every completion, each entry of `M(n)` lies in its fixed product window
of length `O(D)`.  Choose an entry where (2.4) is attained.  A real quadratic
with leading coefficient of magnitude at least `h/2` takes values in an
interval of length `O(D)` at only

```text
O(1+sqrt(D/h))                                       (2.5)
```

integer arguments: complete the square and split at its vertex.  Actual
completion parameters form a subset of those arguments.

### Proposition 2.1 (height versus chart multiplicity)

If `m_ch(C)` is the number of completions assigned to one parabolic chart
of primitive direction height `h`, then

```text
m_ch(C)<<1+sqrt(D/h).                              (2.6)
```

For a chart with at least three points, the common-level identity is a
polynomial identity in `n`.  Its quadratic coefficient gives

```text
e11*c11+e22*c22-e12*c12-e21*c21=0.                (2.7)
```

Thus `e` is exactly a rank-one color relation to which (1.3) applies.

---

## 3. Weighted high/low chart split

Fix a threshold `M>=3`.  Assign every exceptional parabolic completion to
one of the `q^o(1)` charts supplied by (1.1).

For charts with `m_ch(C)<=M`, equations (1.1)--(1.2) give

```text
Q_low
 =sum_C sum_(low ch) m_ch(C)w_z(C)
 <<M Dq^o(1).                                      (3.1)
```

If `m_ch(C)>M`, Proposition 2.1 forces

```text
h<<H:=D/M^2.                                       (3.2)
```

There are `O(X^2q^o(1))` primitive rank-one two-by-two matrix directions of
height at most `X`.  This follows by the primitive factorization
`e=r s^T` and the divisor sum

```text
sum_(||r||~R, R||s||<=X) 1<<X^2 log(2X).           (3.3)
```

Group high charts dyadically by `h` and then by their direction `e`.  On a
height-`h` block, (2.6) contributes at most `sqrt(D/h)`, while (1.3)
contributes at most `sqrt(D)` of color mass per direction.  Equations
(3.2)--(3.3) yield

```text
Q_high
 <<D sum_(dyadic J<=H) J^(3/2)q^o(1)
 <<D H^(3/2)q^o(1)
 =D^(5/2)M^(-3)q^o(1).                            (3.4)
```

The `q^o(1)` number of charts per color absorbs assignment overlaps.  The
nonparabolic part of (1.1) contributes only `Dq^o(1)` by (1.2).

Balancing (3.1) and (3.4),

```text
M D=D^(5/2)/M^3,
M=D^(3/8),                                         (3.5)
```

proves (0.1).

At this threshold, `H=D^(1/4)=q^(4/33+o(1))`, safely below the shell
minimum.  Thus every use of the fixed short-relation theorem is within its
proved height range.

---

## 4. Exact scaled additivity

Write the signed color matrix as

```text
K=(c11,-c12;-c21,c22).                             (4.1)
```

Over a parabolic chart, factor

```text
M(t)=(u0+t r)(v0+t s)^T.                           (4.2)
```

The coefficient of `t^2` in the constant-level identity is

```text
r^T K s=0.                                         (4.3)
```

When all four slope components are nonzero, put

```text
d_ij=r_i s_j c_ij.                                 (4.4)
```

Equation (4.3) is exactly

```text
d11+d22=d12+d21.                                   (4.5)
```

Set

```text
A=d11-d12,                 B=d11-d21.              (4.6)
```

Then

```text
(r1 r2 s1 s2)det C=det(d_ij)=-A B.                (4.7)
```

Thus the determinant does factor into two additive steps, but in four
different dilates of the color variable.  Raw additivity is the special
case in which the two tangent slope vectors are constant across their
coordinates, as in the ordinary translation grid.  It is not a consequence
of parabolicity.

If a tangent component vanishes, (4.3) degenerates further and (4.7) is not
available.  Proposition 2.1 remains valid because it uses an entry attaining
the nonzero direction height, not division by all four components.

---

## 5. A long active integer counterexample to raw additivity

Let `T` be a large integer with `T=1 mod 6`, put `q=10T`, and choose an
integer parameter `t`.  Define

```text
a1(t)=6(T+t),                  a2(t)=5(T+2+t),
b1(t)=5(T+1-t),                b2(t)=5(T+7-t),       (5.1)

C=( 25(T-1)/6, 25(T-7)/6;
    5(T-3),     5(T-9) ).                            (5.2)
```

All entries are integral.  For `20L<=t<=21L` with `L=o(T)`, every displayed
row, column, and color label lies in the project width-`0.2` shell centered
at `q/2=5T`:
the limiting extreme ratio is

```text
6/(25/6)=36/25<exp(0.4).                           (5.3)
```

Use

```text
r=(6,5),       s=(5,5),
P=(0,2),       Q=(1,7),       B0=125.              (5.4)
```

Each cell has the exact product identity

```text
a_i(t)b_j(t)c_ij
 =B0(T+P_i+t)(T+Q_j-t)(T-P_i-Q_j).                (5.5)
```

Writing `X=P_i+t`, `Y=Q_j-t`, and `S=X+Y`,

```text
(T+X)(T+Y)(T-S)-T^3
 =T(XY-S^2)-SXY.                                   (5.6)
```

Since `q^3/8=125T^3`, equations (5.5)--(5.6) give

```text
|8a_i(t)b_j(t)c_ij-q^3|<<qL^2                     (5.7)
```

throughout the displayed length-`L` parameter interval.  This is a genuine
long parabolic product-window family at `D=O(L^2)`.  For sufficiently large
`L`, all eight labels in each rectangle are distinct.  The induced triple
system is pair-unique: each color fixes its cell, the row and column
coordinates are injective in `t`, and the two row ranges are separated by
order `T` (a possible overlap of the two column progressions cannot also
preserve a row).

Nevertheless direct calculation gives

```text
det C=-250,
c11+c22-c12-c21=-5.                                (5.8)
```

The four colors are distinct for large `T`.  Scaled colors do obey (4.5):

```text
(d11,d12;d21,d22)
 =125*(T-1,T-7;T-3,T-9),                           (5.9)
```

and their two steps are `A=750`, `B=250`, so (4.7) reads

```text
750*(-250)=-750*250.                               (5.10)
```

This full-integer example is not an actual-prime-power counterexample to
the QP four-cycle bound.  It proves that the passage from a parabolic
fixed-color chart to an ordinary additive color rectangle is algebraically
invalid.  Any prime-power closure must handle the dilated relation (0.2),
or prove additional slope alignment from actual-prime arithmetic.

---

## 6. Exact scope

The fourth-root of (0.1) is `D^(11/32)`, and if it were a bound for the full
all-distinct trace it would produce transverse exponent

```text
1/2+(11/32)*(16/33)=2/3.                           (6.1)
```

It is not currently a full-trace bound.  The generic branch has no rational
parabolic direction to which (2.6)--(3.4) can be assigned.  Closing or
matching that branch requires a new weighted count on the rank-one quadric
surface inside the generic rank-three common-level lattice.

```text
parabolic chart multiplicity sqrt(D/h):             PROVED;
exceptional-sector mass D^(11/8+o):                 PROVED;
raw additive colors from parabolicity:               FALSE;
diagonally scaled additivity and determinant factor: PROVED;
global fourth trace D^(11/8+o):                     OPEN;
global operator D^(11/32+o), transverse 2/3:        NOT CLAIMED;
full four-cycle bound:                               OPEN.
```
