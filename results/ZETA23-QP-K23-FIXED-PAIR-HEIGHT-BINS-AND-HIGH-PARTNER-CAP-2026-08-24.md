# QP `K_(3,2)`: fixed-pair height bins and the high-partner cap

**Date:** 2026-08-24  
**Verdict:** the proposed fixed-pair refinement is correct.  For two fixed
primitive row pairs `p_y,p_z`, the number of third rows whose primitive
cross-product height lies in `[R,2R)` is

```text
<<R*tau(|det(p_y,p_z)|).                              (0.1)
```

Combining (0.1) with the proved triple-codegree bound gives

```text
sum_w t_3(y,z,w)<<D*q^o(1).                          (0.2)
```

Consequently, if `m(y,z)` lies in `[H,2H)`, every anchor `y` has at most

```text
L_y(H)<<D^2/H^2*q^o(1)                              (0.3)
```

such partners.  On a flat coefficient bin this gives the new dyadic
weighted bounds

```text
W_H<<D^2/H^2*q^o(1)||z||_2^4,
H*W_H<<D^2/H*q^o(1)||z||_2^4.                       (0.4)
```

At `H=D^(7/8)`, (0.4) is respectively `D^(1/4)` and `D^(9/8)`.  This
improves the older high-completion profile `D^(3/8)` and `D^(5/4)` by
`D^(1/8)`, but it does **not** improve the current global fourth-trace
exponent: `D^(9/8)` was already known from the diffuse randomized budget
`D^(1/8)` times the maximal physical fan `D`.  The sharp targets are
`D^(1/8)` and `D`, so the new route still misses by `D^(1/8)` at the
critical threshold.

No sharp four-cycle theorem is proved.

The orientation is legitimate.  The binary incidence may be transposed so
that the pair vertices carrying the coefficient weights are the “rows.”
The product equations are symmetric in the row-pair and color-pair
factors, while the common carrier remains on the incidence edge.  Thus the
same primitive-shell determinant argument applies on the weighted side.

## 1. Exact fixed-pair height-bin theorem

Write the primitive shell rows as

```text
p_y=(a,A),        p_z=(b,B),        p_w=(c,C).
```

The raw cross product of the two coordinate triples is exactly

```text
(a,b,c) cross (A,B,C)
 =(b*C-c*B, c*A-a*C, a*B-b*A)
 =(det(p_z,p_w),det(p_w,p_y),det(p_y,p_z)).          (1.1)
```

Put

```text
delta=det(p_y,p_z) !=0,
g=content((a,b,c) cross (A,B,C)),
mathcal H=max(|three minors|)/g.                     (1.2)
```

The determinant `delta` is nonzero: proportional primitive positive shell
pairs are equal.  If

```text
R<=mathcal H<2R,                                     (1.3)
```

then

```text
g divides delta,
|det(p_z,p_w)/g|<2R.                                 (1.4)
```

For one fixed positive divisor `g|delta`, the second quantity in (1.4) has
fewer than `4R` signed integral values.  A fixed value of
`det(p_z,p_w)` determines `p_w`.  Indeed, two solutions differ by an
integral multiple of the primitive vector `p_z`; a nonzero multiple is
larger than the shell diameter in at least one coordinate.  Therefore

```text
#{w:R<=mathcal H(y,z,w)<2R}
 <=(4R-1)*tau(|delta|).                              (1.5)
```

This proves (0.1).  In an actual slope block `|delta|<<D`, so the divisor
factor is `q^o(1)`.

The order `R` is sharp before the actual mask is used.  Put

```text
p_t=(m+3t,m+3t+1).
```

For the fixed pair `(p_0,p_1)` and `t>=1`, the common factor three cancels
from (1.1), leaving primitive height exactly `t`.  Thus the third rows
`p_R,...,p_(2R-1)` give `R` points in one height bin.  The step three makes
all displayed coordinates distinct.  These are primitive narrow-shell
integer pairs, not an actual-prime QP construction.

## 2. Summing the triple codegrees

The proved three-pivot theorem says

```text
t_3(y,z,w)<<1+D/mathcal H(y,z,w).                    (2.1)
```

Dyadically sum (2.1).  On the height bin `[R,2R)`, equations (1.5)--(2.1)
give

```text
sum_(w in bin)t_3(y,z,w)
 <<R*tau(delta)*(1+D/R)
 <<(R+D)*tau(delta).                                 (2.2)
```

All primitive heights are `O(D)` in a slope block.  Summing the
`O(log D)` bins and absorbing the divisor and logarithmic factors proves

```text
sum_(w distinct from y,z)t_3(y,z,w)<<D*q^o(1).       (2.3)
```

This is a genuinely stronger **local** statement than the earlier
fixed-pair estimate `D*R/delta` in small determinant layers.  Globally,
summing (1.5) over `O(D^2)` row pairs still gives the old
`O(D^2 R q^o(1))` triple count.  Hence the former unrestricted
reciprocal-height and `K_(3,2)` operator exponents do not improve merely by
resumming all pairs.

## 3. Convexity gives the high-partner cap

Fix `y` and let

```text
Z={z:H<=m(y,z)<2H},                  L=|Z|,
S_z=N(y) intersect N(z).
```

For `x in N(y)`, put

```text
d_x=#{z in Z:x in N(z)},             E=sum_x d_x.
```

Then

```text
L*H<=E<2L*H,
sum_x d_x(d_x-1)
 =sum_(z!=w in Z)t_3(y,z,w).                         (3.1)
```

By (2.3), the right side is at most `L*D*q^o(1)`.  On the other hand,
`|N(y)|<=D` and Cauchy give

```text
sum_x d_x(d_x-1)>=E^2/D-E.                          (3.2)
```

If `E<=2D`, then `L<=2D/H`, which is already at most `2D^2/H^2`.  If
`E>2D`, (3.2) is at least `E^2/(2D)`.  Comparing with the upper bound and
using `E>=LH` gives

```text
L<<D^2/H^2*q^o(1).                                  (3.3)
```

This proves (0.3).

## 4. Exact weighted and operator consequences

Let `A_H` be the adjacency matrix of the dyadic partner graph
`H<=m(y,z)<2H`.  Equation (3.3) gives

```text
||A_H||_(2->2)<=max degree(A_H)<<D^2/H^2*q^o(1).    (4.1)
```

For the pair-weight vector `u_(c,d)=|z_c z_d|`,

```text
||u||_2^2<=||z||_2^4.
```

Thus the uncompleted color mass and its completed contribution obey (0.4).
The Gram layer with entries `m(y,z)1_(m~H)` likewise has operator norm

```text
<<H*||A_H||<<D^2/H.                                  (4.2)
```

In exponent notation, for `H=D^tau`, the new uncompleted and completed
exponents are

```text
2-2tau,                 2-tau.                      (4.3)
```

The previous uniform direct theorem gives `5/4-tau` and `5/4`, so (4.3)
is better precisely when `tau>3/4`.  At the critical high-Walsh endpoint,

```text
tau=7/8:
new uncompleted mass       D^(1/4),
new completed trace        D^(9/8),
sharp targets              D^(1/8), D.              (4.4)
```

The factorial kernel has row sum only

```text
H^2*L<<D^2,                                        (4.5)
```

not the desired `D`.  Therefore the new local lemma does not by itself
close the positive quartic either.

### 4.1 The exact square-root-degree spectral gate

The partner cap has one important sharp consequence at the level of a
*possible* packet-free spectral theorem:

```text
H*sqrt(L_H)
 <<H*sqrt(D^2/H^2)*q^o(1)
 <<D*q^o(1).                                         (4.6)
```

Thus the following statement would close every dyadic high-codegree layer
at the sharp scale.

> **Packet-free inverse-expander theorem (open).**  Let
> `G_H(y,z)=m(y,z)1_(H<=m(y,z)<2H)`.  After decomposing and removing the
> coherent low-height affine/Hankel packet modes (including their local
> degree/polar vectors), the residual matrix satisfies
>
> ```text
> ||G_H,res||_(2->2)
>   <<H*sqrt(L_H)*q^o(1)
>   <<D*q^o(1).                                      (4.7)
> ```
>
> Equivalently, if a centered residual layer has norm polynomially larger
> than `H*sqrt(L_H)`, one can recover a low-height packet carrying a
> comparable portion of that spectral mass.

Here “residual” must be literal at the incidence-edge level.  One must
write an honest residual incidence `B_res`, recompute its codegrees and
dyadic bins, and bound the packet--residual mixed completions separately.
Subtracting a convenient rank-one matrix directly from the already formed
positive Gram layer does not define a valid packet decomposition and would
not prove the original weighted trace estimate.

Summing (4.7) over dyadic `H` costs only `q^o(1)`.  Since the pair-weight
vector has squared norm at most `||z||_2^4`, (4.7), together with the
already proved bounds for the extracted packets, would give the desired
`O(Dq^o(1))` weighted fourth trace on this incidence sector.

This theorem is **not** a consequence of (0.3).  For a nonnegative
`L`-regular support graph, the constant vector has eigenvalue `H*L`, not
`H*sqrt(L)`.  A global constant subtraction is also insufficient for a
disjoint union of dense components: every component contributes its own
constant mode.  The inverse assertion must identify and peel those local
modes arithmetically.

The subset design in Section 5 is an exact hostile test.  Its high-partner
graph is complete, so

```text
G_H=H*(J-I),
||G_H||=H*L,
||G_H||/(H*sqrt(L))=sqrt(L).                         (4.8)
```

At the same time its primitive rows are the affine family
`p_i=(m+i,m+i+1)`.  Hence the excessive eigenvector is precisely a
coherent low-height packet mode which (4.7) is required to extract.  The
example refutes a raw expander estimate but is consistent with the stated
inverse theorem.  Disjoint copies show why the extraction must be local,
not merely one global rank-one polar subtraction.

Most importantly, the current critical-bin theorem already has

```text
randomized mass D^(1/8) times maximum fan D =D^(9/8). (4.9)
```

So (4.4) supplies a new dyadic structural profile, while (4.7) isolates a
new sharp conditional gate, but neither is a new best global theorem.
Without (4.7), there is no new best global
fourth-trace or operator exponent.  It becomes sharp only in the extreme
range `H=D*q^(-o(1))`.

## 5. Hostile saturation of the derived inequalities

The convexity exponent cannot be improved from (2.3), maximum degree, and
the height cap alone.  Let `s>=3`, put

```text
n=s^2,
```

and form the incidence graph between `n` rows and all `s`-subsets of those
rows.  Membership is incidence.  Its exact parameters are

```text
D_0=binom(n-1,s-1),
H_0=binom(n-2,s-2),
t_0=binom(n-3,s-3).                                  (5.1)
```

Every row has all other `n-1` rows as `H_0`-codegree partners.  Assign row
`i` the primitive shell pair

```text
p_i=(m+3i,m+3i+1).
```

For `i<j<k`, its primitive height is

```text
mathcal H(i,j,k)
 =(k-i)/gcd(j-i,k-j)<=n-1.                           (5.2)
```

Since `(s-1)(s-2)<=n-2`, equations (5.1)--(5.2) give

```text
t_0<=D_0/(n-1)<=D_0/mathcal H(i,j,k),
sum_(w!=y,z)t_3(y,z,w)=(n-2)t_0<=D_0.               (5.3)
```

Thus both the arithmetic height cap and the fixed-pair budget are obeyed.
But

```text
L=n-1=s^2-1,
D_0^2/H_0^2=(s+1)^2,
L/(D_0^2/H_0^2)=(s-1)/(s+1) ->1.                   (5.4)
```

The high-partner graph is complete, so the constant vector also saturates
the adjacency operator bound.  This construction uses primitive narrow
integer row pairs, but its subset incidence is not realized by the QP
product window and its coordinates are not actual prime powers.  It is a
method countermodel: any improvement over (0.3)--(0.4) must use additional
actual-mask structure.

## 6. Status

```text
fixed-pair height-bin count R*tau(delta):          PROVED;
fixed-pair triple-codegree sum O(D q^o):           PROVED;
dyadic high-partner cap D^2/H^2:                  PROVED;
flat weighted tail D^2/H^2:                       PROVED;
completed/Gram high-layer bound D^2/H:            PROVED;
identity H*sqrt(L_H)<=D:                           PROVED;
packet-free residual norm <=H*sqrt(L_H):           OPEN INVERSE THEOREM;
critical high layer improves old D^(5/4):         TO D^(9/8);
new best global fourth-trace exponent:             NO (already D^(9/8));
sharp critical trace D:                            NOT PROVED;
partner/Schur exponent from present inputs:        SHARP (method model);
actual-prime/product-window saturation:            NOT OBTAINED.
```

Executable replay:

```text
src/qp_support_graph_k23_gate.py
src/test_qp_support_graph_k23_gate.py
```
