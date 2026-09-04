# QP four-cycle: pair-completion energy and common-modulus audit

**Date:** 2026-08-15  
**Verdict:** the pair-of-completions identities give a sharper exact target,
but they do **not** prove the four-cycle bound.  The useful target is the
off-diagonal weighted pair estimate

```text
sum_C m(C)(m(C)-1) w_z(C) << D q^o(1) ||z||_2^4.       (0.1)
```

It is enough to close the full bound by a quadratic bootstrap.  For two
completions of the same color matrix, their product difference `E` lies in
a length-`D` box and satisfies an exact color hyperplane; its determinant
factors into two independently short row and carrier determinants.  These
facts expose the missing joint energy theorem precisely.

Two tempting shortcuts fail:

* Fourier expansion of the color hyperplane is completely coherent,
  because residual pinning puts every completion of `C` on the same level;
* the common-modulus relation in the two short shifts `u,v` is the reduction
  of a stronger integer equality.  It does not supply a new complete
  Kloosterman variable, and direct Fourier completion again puts the short
  physical masks into unrestricted dual frequencies.

An `O(D)` top/bottom color-pair fibre would also close the estimate, but it
does not follow from linearity or degree caps: an explicit symmetric linear
3-graph has such a fibre of order `D^3`.  Thus any proof of (0.1) must use
the cubic carry equation and actual prime-power support in an essential
way.

No QP, strip, or full four-cycle theorem is asserted here.

---

## 1. Exact pair identities

Write

```text
C=(c11,c12;c21,c22),       k=det C,
K=( c11 -c12; -c21 c22 ).                            (1.1)
```

A completion is `X=(a1,a2,b1,b2)`, with column vectors `a,b`, product
matrix `M=a b^T`, and alternating level

```text
F_C(X)=a^T K b
      =c11*a1*b1+c22*a2*b2-c12*a1*b2-c21*a2*b1.     (1.2)
```

Since the four copies of `q^3` cancel,

```text
S_r(X)=8 F_C(X).                                     (1.3)
```

At the active scale the residual pinning theorem therefore says that all
completions of one fixed `C` have one common integral level

```text
F_C(X)=L(C).                                         (1.4)
```

Take two such completions `X=(a,b)` and `X'=(a',b')`.  Put

```text
E=M-M',
A=a1*a2'-a2*a1',       B=b1*b2'-b2*b1'.             (1.5)
```

The residual window gives `|e_ij|<<D`.  Subtracting (1.4) gives the exact
hyperplane

```text
c11*e11+c22*e22-c12*e12-c21*e21=0.                  (1.6)
```

Both product matrices have rank one, hence

```text
det E=-A*B.                                          (1.7)
```

The two factors are individually short, not merely their product.  For
example,

```text
A*b1=a2'*e11-a1'*e21,       A*b2=a2'*e12-a1'*e22,
B*a1=b2'*e11-b1'*e12,       B*a2=b2'*e21-b1'*e22.   (1.8)
```

All shell variables are comparable with `q`, so (1.8) proves

```text
|A|+|B|<<D.                                          (1.9)
```

This is a genuine strengthening of the bare `|det E|<<D^2` statement.

There is also an exact Lagrange identity.  Define the two cross levels

```text
X=a^T K b',                  Y=a'^T K b.             (1.10)
```

Taking the determinant of

```text
[a a']^T K [b b'] = (L X;Y L)
```

gives

```text
L^2-X*Y=k*A*B.                                      (1.11)
```

Finally let

```text
e=e11,
u2=b1*c21-b2*c22,           v2=a1*c12-a2*c22.       (1.12)
```

Direct elimination, with `a1',b1'` denoting the first coordinates of the
second completion, gives

```text
e*L+A*b1'*u2+B*a1'*v2-c22*A*B=0.                   (1.13)
```

Before imposing equal levels, the left side of (1.13) is exactly
`a1*b1*(F_C(X)-F_C(X'))`.  Thus (1.13) contains no discarded error term.

---

## 2. The off-diagonal bootstrap

Let

```text
w(C)=|z_c11 z_c12 z_c21 z_c22|,
S=sum_C m(C)w(C),
W=sum_C w(C),
P=sum_C m(C)(m(C)-1)w(C).                           (2.1)
```

The proved determinant-layer energy gives

```text
W<<D q^o(1)||z||_2^4.                               (2.2)
```

Normalize `||z||_2=1`.  Weighted Cauchy--Schwarz says

```text
S^2 <= W sum_C m(C)^2w(C)=W(S+P).                  (2.3)
```

Consequently (0.1) makes `S` satisfy

```text
S^2<<D q^o(1)(S+D q^o(1)),                          (2.4)
```

and the positive quadratic root is `S<<D q^o(1)`.  This closes the desired
four-cycle sum.  In particular, the diagonal pair `E=0` need not be bounded
separately; it is the self-consistent `S` term in (2.3).

Thus the smallest clean remaining theorem is (0.1), restricted to distinct
completions and, after the already proved deletions, to the all-eight-node
sector.

---

## 3. Why additive Fourier on the exact hyperplane gives no gain

Choose an integer modulus `P0` larger than the full range of the levels.
For fixed `C`, Fourier detection of equality gives

```text
sum_(X,X' in Comp(C)) 1_(F_C(X)=F_C(X'))
 =P0^(-1) sum_(t mod P0)
   |sum_(X in Comp(C)) exp(2*pi*i*t*F_C(X)/P0)|^2.  (3.1)
```

But (1.4) makes the inner sum

```text
m(C) exp(2*pi*i*t*L(C)/P0)                          (3.2)
```

for **every** frequency.  Formula (3.1) is therefore exactly `m(C)^2` at
all frequencies; there is no nonprincipal cancellation to estimate.

The determinant can be combined algebraically with the hyperplane.  If
`e22!=0`, then

```text
(e22*c12-e21*c11)(e22*c21-e12*c11)
 =-det(E)*c11^2-e22^2*k.                            (3.3)
```

Rotated versions cover the other pivots.  For fixed `(E,k,c11)` and
nonzero right side, (3.3) gives a divisor-type number of color pairs.  If
the right side vanishes, one of the two factors vanishes and leaves a
linear matching branch.  Neither case is the obstruction.

The obstruction is summing over the many realizable secants `E`.  Equations
(1.6)--(1.9) do not currently prove that the weighted set of actual
prime-power secants has mass `O(D)`.  Treating the four entries of `E` as
independent length-`D` variables loses powers; treating their determinant
layers independently also loses, since `A,B` each range over length `D`.

---

## 4. The two short determinants do not yet give a BP kernel

For a fixed first completion, the second row vector is determined by `A`
through

```text
a1' == -A*inverse(a2) (mod a1),                     (4.1)
```

and the second carrier vector is determined by `B` through

```text
b1' == -B*inverse(b2) (mod b1).                     (4.2)
```

The short shell makes each lift unique, when it exists.  The key point is
that (4.1) and (4.2) live at the two generally distinct moduli `a1` and
`b1`.  Their coupling includes

```text
a1'*b1'=a1*b1-e,             |e|<<D.                (4.3)
```

Thus the admissible pairs `(A,B)` carry a joint coefficient supported on a
thin graph; they are not two independent coefficient sequences.  Combining
the two congruences by the Chinese remainder theorem produces modulus
`a1*b1 asymp q^2`.  At that modulus the physical length is

```text
D=q^(16/33)=(q^2)^(8/33),                            (4.4)
```

far below the `c^(13/28)` critical range in the Blomer--Pascadi theorem.
Here the cited input is
[Blomer--Pascadi, Theorem 1.1](https://arxiv.org/abs/2607.24311).

Equation (1.13) is an exact bilinear relation in `A,B`, but the coefficients
`a1',b1'` are precisely the two different modular lifts (4.1)--(4.2).
Apparent further congruences obtained from (1.11) reduce to the identities

```text
L=a1*u1-a2*u2=b1*v1-b2*v2,
u2*v2=c22*L-k*a1*b1.                                (4.5)
```

No common-modulus complete variable remains.  A direct application of a
bilinear Kloosterman theorem would have to replace the joint graph weight
by separable weights; coefficient-uniform control of that replacement is
exactly the missing correlation theorem.

---

## 5. The proposed common-modulus `u,v` parametrization

Fix `m=c11` and put

```text
u=m*b1-c12*b2,              v=m*a1-c21*a2.          (5.1)
```

Both are `O(D)`.  In the generic coprime sector,

```text
b2 == -inverse(c12)*u (mod m),
a2 == -inverse(c21)*v (mod m),                      (5.2)
```

with unique shell lifts.  If `n=a2*b2`, the cell-22 product window gives
`n` in an interval of length `O(D)` and

```text
u*v == c12*c21*n (mod m).                           (5.3)
```

However (5.3) is the reduction of the stronger equality

```text
u*v=m*L-k*n.                                        (5.4)
```

Indeed `c12*c21=m*c22-k`.  Thus the modular phase in (5.3) is identically
coherent on actual completions.  The cell-22 window is equivalently a
length-`O(|k|D)` condition on the ordinary integer product `uv`.

For the opposite shifts

```text
u2=c21*b1-c22*b2,           v2=c12*a1-c22*a2,       (5.5)
```

one has

```text
u2*v2=c22*L-k*a1*b1,
m*u2=c21*u-k*b2(u),
m*v2=c12*v-k*a2(v).                                 (5.6)
```

So the cell-11 window is a second product-window condition on the two
modular-lift maps `u->u2` and `v->v2`.  It is not a classical complete
Kloosterman sum in the physical variables `u,v`.

This can also be seen from exact Fourier inversion.  For masks `f,g` and a
length-`D` product mask `h`, the enlarged modular count is

```text
T=sum_(u,v,n) f(u)g(v)h(n) 1_(uv=c12*c21*n mod m).
```

On the unit sector,

```text
T=m^(-2) sum_(r,s,n) fhat(r) ghat(s) h(n)
                   S(r,s*c12*c21*n;m).              (5.7)
```

The Kloosterman arguments in (5.7) are the additive **dual** variables
`r,s`, not the short physical shifts `u,v`.  Actual prime-power lift masks
can have full dual support, while `s*n` is a coupled product rather than a
second separated interval coefficient.  This is the same localization and
nonseparability loss found in the earlier one-edge bridge.

Dropping all arithmetic masks to full intervals makes (5.7) a legitimate
positive local box majorant, but it no longer controls the weighted global
completion-pair energy (0.1), and the second product window (5.6) remains
coupled.

---

## 6. Direct top/bottom projection and its exact limitation

For an ordered color pair `p=(c1,c2)`, let `W_p` be the set of ordered
carrier endpoint pairs `(b1,b2)` for which some center `a` supports

```text
(a,b1,c1),                 (a,b2,c2).               (6.1)
```

Pair uniqueness makes the center unique and the color-degree cap gives

```text
|W_p|<=D.                                              (6.2)
```

For `C` with top pair `p` and bottom pair `q`, every completion belongs to
`W_p intersect W_q`, so

```text
m(p,q)<=|W_p intersect W_q|.                         (6.3)
```

Consequently an `O(D)` row and column bound for the matrix `m(p,q)^2`
would prove the weighted pair estimate by Schur's test.  But expanding one
row gives

```text
sum_q m(p,q)^2
 <=sum_(x,y in W_p) #{q:x,y in W_q}.                 (6.4)
```

Linearity and degree caps alone give only `O(D^3)` in (6.4), and that scale
is sharp abstractly.  Let `r=D-1`.  Take `r` disjoint endpoint pairs, one
top color pair `p`, and `r` bottom color pairs `q_j`.  Give `p` and every
`q_j` all `r` endpoint pairs, using a distinct center for each required
incidence.  In unordered-triple notation the edges are

```text
{a_i,b_i0,p_0},             {a_i,b_i1,p_1},
{x_ij,b_i0,q_j0},           {x_ij,b_i1,q_j1}.        (6.5)
```

This 3-graph is linear.  Every node has degree at most `D`, and symmetrizing
the triples preserves those properties.  Nevertheless

```text
m(p,q_j)=r,                sum_j m(p,q_j)^2=r^3.     (6.6)
```

The construction is not a cubic-carry model.  Its role is exact: it proves
that the desired `O(D)` projection fibre cannot be deduced from pair
uniqueness, symmetry, and degree caps.  The carry hyperplane and actual
prime-power determinants must supply a factor `D^2` beyond the abstract
bound.

---

## 7. Precise remaining theorem

After the proved zero-determinant and repeated-coordinate deletions, it is
enough to establish either of the following genuinely arithmetic statements:

```text
(A) sum_C m(C)(m(C)-1) w_z(C)
      <<D q^o(1)||z||_2^4;

(B) max_p sum_q m(p,q)^2 <<D q^o(1)
    and the transposed bound.                        (7.1)
```

Statement (B) is stronger and is false for general linear carry-free
systems.  Statement (A) is the sharp weighted target.  The exact data now
available for attacking it are (1.6)--(1.13) and (5.4)--(5.6).  What is
still missing is a joint prime-power secant theorem that sums the short
determinants `A,B` or the coupled shift products without replacing their
joint coefficient by arbitrary independent boxes.

```text
pair hyperplane and determinant identities:          PROVED;
individual |A|,|B|<<D:                               PROVED;
off-diagonal D estimate => full FC:                   PROVED CONDITIONALLY;
common-modulus uv congruence => direct BP:            FALSE AS A DIRECT STEP;
O(D) projection fibre from degree/linearity:          FALSE;
actual weighted off-diagonal pair theorem:            OPEN;
full four-cycle bound:                                OPEN.
```

Exact replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_four_cycle_pair_energy_audit.py
```
