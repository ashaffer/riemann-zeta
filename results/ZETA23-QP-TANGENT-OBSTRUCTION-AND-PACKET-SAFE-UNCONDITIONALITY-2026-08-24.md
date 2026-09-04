# QP four-cycle: tangent obstruction and packet-safe unconditionality

**Date:** 2026-08-24  
**Verdict:** the sharp randomized residual-block theorem is valid, but its
raw all-plus comparison is false in the exact full-integer product-window
model by a factor of order `sqrt(D)`.  The obstruction is precisely a
coherent affine/Hankel packet, whose direct fourth trace is already bounded
sharply by the existing packet merger.  The correct missing theorem is
therefore an **excess-implies-packet inverse theorem**, followed by
unconditionality only on the packet-free remainder.

## 1. Exact tangent fixture

Let `L>=2`, take `m>64L^3`, put `q=2m`, and define

```text
a_i=m+i,                 0<=i<L,
b_j=m+2L+j,              0<=j<L,
c_ij=m-2L-i-j.                                      (1.1)
```

All role intervals are disjoint.  With `x=i` and `y=2L+j`,

```text
(m+x)(m+y)(m-x-y)-m^3
 =-m(x^2+xy+y^2)-xy(x+y).                           (1.2)
```

Thus every triple belongs to the literal window

```text
|8a_i b_j c_ij-q^3| <=qD,             D=100L^2.     (1.3)
```

Give the `2L-1` color nodes `c_ij` the flat coefficient
`z_c=(2L-1)^(-1/2)` and give all other nodes coefficient zero.  The symmetric
carry matrix is the self-adjoint dilation of the constant `L x L` matrix

```text
H_ij=(2L-1)^(-1/2).                                  (1.4)
```

Consequently

```text
||A_z||S4^4=2L^4/(2L-1)^2 asymp L^2 asymp D.         (1.5)
```

This is a sharp but harmless coherent packet.

## 2. Width-`q` residual signs destroy the coherence

Put `F(i,j)=i^2+i(2L+j)+(2L+j)^2`.  From (1.2) and `m>64L^3`,

```text
floor((8a_i b_j c_ij-q^3)/q)
 =-4F(i,j)-1_(i>0).                                  (2.1)
```

These labels are proper in every row and column.  They also contain no
alternating two-label rectangle.  Indeed, the crossed equalities for
`i!=i'`, `j!=j'` would imply

```text
4(i-i')[2(i+i')+4L+j+j']+2(1_(i>0)-1_(i'>0))=0,     (2.2)
```

which is impossible.

Let independent signs be attached to the width-`q` residual blocks.  In
the fourth moment, (2.2) leaves only row and column backtracking.  Direct
counting gives the exact average

```text
E_epsilon ||sum_I epsilon_I A_I(z)||S4^4
 =2L^2/(2L-1) asymp L.                               (2.3)
```

Combining (1.5) and (2.3),

```text
 all-plus / randomized =L^2/(2L-1) asymp L/2
                         asymp sqrt(D).              (2.4)
```

Hence no coefficient-blind estimate comparing the raw all-plus operator to
its residual-block Rademacher average can be proved from the integer product
window.  The example is not an actual-prime counterexample: its nodes are
consecutive integers.  It is an exact obstruction to the proposed proof
mechanism and identifies what must be extracted.

## 3. Correct GPT-7-style theorem

For physical residual blocks `A_I(z)`, one needs a decomposition

```text
A_I=A_I^coh+A_I^gen                                    (3.1)
```

with the following properties.

1. `A^coh` is a union of rational affine/Hankel packets and satisfies a
   global Carleson packing estimate.  The existing merged-packet theorem
   then gives

```text
||sum_I A_I^coh||S4^4 <<D q^o(1)||z||2^4.            (3.2)
```

2. The packet-free remainder obeys

```text
||sum_I A_I^gen||S4^4
 <<q^o(1) E_epsilon||sum_I epsilon_I A_I^gen||S4^4.  (3.3)
```

3. The proved weighted Rademacher theorem bounds the right side of (3.3)
   by `Dq^o(1)||z||2^4`.

Thus the single genuinely new input is the inverse implication

```text
polynomial all-plus excess
       => quantitatively large mergeable affine/Hankel packet.          (3.4)
```

It must retain the actual prime/product mask: resolvable Steiner systems
and Latin block designs show that matching structure and pair uniqueness
alone do not imply (3.4).

## 4. Status

```text
sharp weighted Rademacher fourth moment:         PROVED;
raw all-plus unconditionality:                   FALSE in integer model;
identified obstruction:                          AFFINE/HANKEL PACKET;
direct bound for one merged packet:              PROVED previously;
global packet Carleson packing:                   OPEN;
packet-free arithmetic unconditionality:         OPEN;
sharp uniform four-cycle theorem:                 NOT PROVED.
```

Exact replay:

```text
src/qp_weighted_triangle_packet_inverse.py
src/test_qp_weighted_triangle_packet_inverse.py
```
