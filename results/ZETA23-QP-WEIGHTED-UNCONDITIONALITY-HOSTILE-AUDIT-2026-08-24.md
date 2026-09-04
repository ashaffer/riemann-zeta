# QP weighted residual-block unconditionality: hostile audit

**Date:** 2026-08-24  
**Verdict:** the weighted Rademacher theorem and its `O(D)` normalization
pass.  Raw all-plus/Rademacher unconditionality is the wrong theorem: an
exact product-window tangent packet loses a factor `D^(1/2)` at the intended
QP exponents.  The excess is exactly a block-odd part of the nonzero color-
determinant four-cycle sector.  The literal packet cannot occur on the
actual prime-power shell at polynomial length, but extending that fact from
exact arithmetic progressions to general approximate packets is open.

No sharp four-cycle theorem is proved here.

## 1. Audit of the randomized theorem

For a linear triple system partitioned into vertex-matching classes, put

```text
M_e(i,j)=z_k,  M_e(i,k)=z_j,  M_e(j,k)=z_i,
A_I=sum_(e in I) M_e.                                  (1.1)
```

The within-class cross products vanish, so

```text
sum_I A_I^*A_I=sum_e M_e^*M_e.                         (1.2)
```

The landed proof of

```text
||sum_I A_I^*A_I||HS^2,
||sum_I A_I A_I^*||HS^2 <=14 Delta ||z||2^4            (1.3)
```

is valid for complex `z`.  For fixed shared vertex `p`, global linearity
makes all other vertices in the incident triples distinct; this is the
point which closes the cross terms in (1.3).

There is also an exact three-pairing identity.  With
`S_epsilon=sum_I epsilon_I A_I`, write

```text
R=||sum_I A_I^*A_I||HS^2,
L=||sum_I A_I A_I^*||HS^2,
C=sum_(I,J) tr(A_I^*A_J A_I^*A_J),
U=sum_I ||A_I||S4^4.
```

Then

```text
E_epsilon ||S_epsilon||S4^4=R+L+C-2U <=R+2L.          (1.4)
```

The inequality uses

```text
|tr((A_I^*A_J)^2)|
 <=tr((A_I^*A_J)^*(A_I^*A_J)),                        (1.5)
```

whose sum is `L`.  Hence

```text
E_epsilon ||S_epsilon||S4^4
 <=42 Delta ||z||2^4.                                 (1.6)
```

At the physical scale `Delta<<D q^o(1)`, this is sharp.  The same argument
allows a common edge scalar `omega_e` with `|omega_e|<=1`, as required for
a bounded smooth product kernel.

There is a useful stronger form on one factor-comparable coefficient bin.
Suppose `z` has support `M`, norm `s`, and

```text
||z||infinity^2 <=K*s^2/M.                              (1.7)
```

For a vertex `p`, put

```text
D_p=sum_(e contains p) sum_(u in e, u!=p)|z_u|^2.       (1.8)
```

Global linearity and the degree cap give both

```text
D_p<=s^2,                 D_p<=2K*Delta*s^2/M,          (1.9)
```

while the complete incidence sum is

```text
sum_p D_p=2 sum_v deg(v)|z_v|^2<=2Delta*s^2.           (1.10)
```

Therefore the cross part of either square function is

```text
<=2Delta*min(1,2K*Delta/M)*s^4.                        (1.11)
```

The self part is at most `12K*Delta*s^4/M`.  Applying (1.4) gives

```text
E_epsilon ||S_epsilon||S4^4
 <<_K Delta*min(1,Delta/M)*s^4.                        (1.12)
```

This is valid in both orientations.  Vertices `p` outside `supp(z)` cause
no loss; they are already included in the exact identity (1.10).

At the critical diffuse support

```text
Delta~D,                  M=D^(15/8),                  (1.13)
```

the random-sign budget is only

```text
D^2/M=D^(1/8),                                        (1.14)
```

not `D`.  This strengthens the randomized theorem, but it also makes clear
that a raw `q^o(1)` comparison is far stronger than FC on diffuse bins.  A
packet inverse theorem must compare the coherent contribution to its own
merged-packet budget, not insist that it be comparable to (1.14).

The direct implication is precise but slightly narrower than “the whole
FC theorem”: it treats the all-distinct hard/smooth carry after the scalar
kernel is included.  The already proved repeated-node and permutation
sectors and the standard smooth recombination must still be appended.

## 2. Exact expansion of the missing all-plus excess

Let

```text
r_ij=8 a_i b_j c_ij-q^3,
lambda_ij=floor(r_ij/q).                               (2.1)
```

In the fourth-trace expansion a rectangle contributes the coefficient

```text
conj(z_c11) z_c12 conj(z_c22) z_c21                   (2.2)
```

to the all-plus operator.  Its sign expectation is retained exactly when
every value among

```text
(lambda_11,lambda_12,lambda_21,lambda_22)             (2.3)
```

has even multiplicity.  Thus

```text
all-plus - random-sign
 =sum_rectangles (2.2) * 1_(some block label is odd),  (2.4)
```

with the evident scalar kernel factors.  Formula (2.4) is an exact complex
identity, not a positive sum.

Put

```text
Q=q^3,
S=r11+r22-r12-r21,
T=r11*r22-r12*r21,
k=c11*c22-c12*c21.                                    (2.5)
```

Cancellation of the two carrier rows and columns gives

```text
Q*S+T=64 k a1*a2*b1*b2.                               (2.6)
```

If `|r_ij|<=H`, `2H^2<Q`, and `k=0`, then (2.6) forces
`S=T=0`.  Therefore

```text
{r11,r22}={r12,r21},                                  (2.7)
```

so the block labels pair and the rectangle survives the random signs.
Consequently

```text
every term in (2.4) has 0<|k|<<D.                     (2.8)
```

The upper bound follows from (2.6), the shell sizes, and `H<<qD`.
Therefore raw sign removal is not a shortcut around the hard four-cycle
problem: it asks for a mask-stable estimate on a selected part of exactly
the nonzero small-determinant sector.

An actual all-prime rectangle at `q=50021` has determinant `k=6` and four
distinct width-`q` block labels, so (2.4) is genuinely populated on the
physical mask.

## 3. The tangent no-go is exact and critically scaled

For the integer fixture

```text
a_i=m+i,
b_j=m+2L+j,
c_ij=m-2L-i-j,            0<=i,j<L,
q=2m,                     D=100L^2,                  (3.1)
```

take `m>64L^3` and put normalized flat weight on the `2L-1` color nodes.
All other coefficients vanish.  The full symmetric carry matrix is exactly
the self-adjoint dilation of the constant `L x L` matrix with entry
`(2L-1)^(-1/2)`.  Hence

```text
||A_z||S4^4=2L^4/(2L-1)^2.                             (3.2)
```

This factor `2` is essential: it comes from the two singular-value copies
in the symmetric dilation.

The exact residual label is

```text
lambda_ij=-4[i^2+i(2L+j)+(2L+j)^2]-1_(i>0).           (3.3)
```

The labels are injective on each row and column.  Equal-label triples are
also disjoint in their color vertices: this follows either directly on the
anti-diagonals `i+j=s`, or from the short-block lemma since
`q<8 min{a_i,b_j,c_ij}`.  Thus the classes really are triangle matchings,
not merely proper matrix colors.

There is no nondegenerate alternating two-label rectangle.  If the two
diagonal labels and the two off-diagonal labels paired, row-sum subtraction
would give

```text
4(i-i')[2(i+i')+4L+j+j']
 +2(1_(i>0)-1_(i'>0))=0,                              (3.4)
```

which is impossible.  Only row/column backtracking survives, and literal
sign enumeration gives

```text
E_epsilon ||sum_I epsilon_I A_I(z)||S4^4
 =2L^2/(2L-1).                                        (3.5)
```

Therefore

```text
all-plus/random =L^2/(2L-1) asymp L asymp D^(1/2).    (3.6)
```

This obstruction is on the intended exponent scale, not an artifact of an
unrelated choice of `q`.  On the exact subsequence

```text
L=t^8,                 m=t^33,
q=2t^33,               D=100t^16,                    (3.7)
```

we have `D=(100/2^(16/33))q^(16/33)` and
`L=2^(-8/33)q^(8/33)`.  For large `t`, also `q>D^2`.

The fixture uses consecutive integers rather than actual prime powers.  It
refutes raw unconditionality as a consequence of product geometry,
matching classes, linearity, and residual ordering alone.  It does not
refute an actual-prime theorem.

## 4. A genuine actual-mask escape for exact affine packets

There is a simple reason the literal packet (3.1) cannot be transferred to
the actual shell at polynomial length.

### Prime-power progression lemma

Let

```text
x_i=A+i*d,                  0<=i<L,                   (4.1)
```

be positive prime powers with pairwise distinct prime bases.  For every
prime `p<=L/2`, one must have `p|d`.

Indeed, if `p` did not divide `d`, the `L` indices contain at least two
solutions of `x_i=0 (mod p)`.  Both corresponding prime powers would have
base `p`, contradicting distinctness.  Hence

```text
prod_(p<=L/2) p | d.                                  (4.2)
```

The project shell contains at most one power of each prime base.  Also its
diameter is `O(q)`, so `(L-1)|d|<<q`.  Chebyshev's estimate in (4.2) yields

```text
L<<log q.                                             (4.3)
```

Thus an exact affine/Hankel grid whose rows, columns, or colors form a
polynomial-length arithmetic progression is excluded by the actual mask.
Its possible loss is only `q^o(1)`.

This helps only **complete exact** packets.  A rich sparse packet can retain
prime nodes on subsets of the three progressions.  A packet of side `L`
and density only inverse-polylogarithmic still has `q^o(1)` of the complete
edges and can retain the same polynomial all-plus/random ratio.  Elementary
upper-bound sieve estimates naturally permit about `L/log L` prime-power
nodes in a progression interval; they do not force the step to contain the
full primorial in (4.2).  Thus (4.3) neither rules out a rich sparse actual-
prime packet nor supplies a power saving.

More generally, a coherent family can be approximately affine, can split
among rational charts, and can use irregular prime samples.  What remains
is to prove that any polynomial excess in (2.4) contains a quantitatively
large controlled rational packet, and then prove a mask-preserving Carleson
packing estimate for those sparse packets.  The exact AP lemma is a useful
endpoint check, not that inverse theorem.

## 5. Correct remaining theorem

The viable statement is:

```text
polynomial all-plus excess
  => Carleson-packed affine/Hankel packets
     + a packet-free remainder satisfying block S4 unconditionality.    (5.1)
```

The coherent packets are bounded by the existing merged-packet theorem;
the remainder is bounded by (1.6).  Neither the global packet packing nor
the packet-free implication in (5.1) is proved.

```text
weighted Rademacher O(D):                         PROVED;
flat-bin randomized refinement D min(1,D/M):      PROVED;
critical flat-bin random budget D^(1/8):          PROVED;
full symmetric tangent normalization:            AUDITED/PASS;
raw block unconditionality:                      FALSE in integer model;
critical QP scaling of the no-go:                 VERIFIED;
all-plus excess lies in nonzero determinant:      PROVED;
complete exact prime-power AP packets O(log q):   PROVED;
rich sparse actual-prime packet exclusion:        OPEN;
excess-implies-packet theorem:                    OPEN;
sharp four-cycle bound:                           NOT PROVED.
```

Executable replay:

```text
src/qp_weighted_unconditionality_audit.py
src/test_qp_weighted_unconditionality_audit.py
src/qp_weighted_triangle_packet_inverse.py
src/test_qp_weighted_triangle_packet_inverse.py
```
