# QP high-completion tail: the common partial-Beatty graph and the reciprocal-carrier gate

**Date:** 2026-08-22  
**Verdict:** in the exact unimodular chart, the row quotient `m(e)` and the
partner quotient `n(k)` are not two independent rounding functions.  Before
the carrier masks are imposed, they are restrictions of one and the same
partial Beatty graph `R(t)`.  More precisely,

```text
m(e)=R(e),                 n(k)=R(k),
R(t)-(u/d)t=a_t/d in [L/d,U/d],                    (0.1)
f=e*R(k)-k*R(e)=(e*a_k-k*a_e)/d.                  (0.2)
```

Consequently the project-size condition `|f|<<D` has no large-sieve
content by itself.  In a one-sign label interval `1<=e,k<=T`, `U=d`, one
always has `|f|<=T`.  There is an asymptotic exact-integer family at
`T=d^(16/33)` with

```text
asymp T occupied rounding points;
at most O(sqrt(T)) points on every affine line;
|e*R(k)-k*R(e)|<=T for every occupied e,k.         (0.3)
```

Thus deleting every `T^(1-o(1))`-rich affine packet still leaves a complete
high-degree determinant graph.  Beatty discrepancy, continued fractions,
or a determinant large sieve applied only to `(0.2)` cannot prove a power
tail, even in the endpoint `e,k~D` range.

The actual carry problem has an additional, genuinely restrictive layer.
For every retained `e`, the anchor carrier is the unique integer in an
intersection of two reciprocal intervals of length `O(D/q)<1`; it must be
an actual prime power.  For every pair `(e,k)`, the second carrier is the
unique integer in a second such intersection and must again be an actual
prime power.  This nested reciprocal-prime mask is absent from `(0.2)` and
from the countermodel.  A successful high-tail theorem must use it.

No uniform four-cycle bound is claimed.

---

## 1. Canonical unimodular coordinates

Fix an actual ordered color pair `gamma=(c,d)` and put

```text
g=(d,c),                   gcd(c,d)=1.              (1.1)
```

Choose the canonical positive Bezout complement

```text
s=(u,v),
0<u<d,                    0<v<c,
d*v-c*u=1.                                          (1.2)
```

Equivalently,

```text
c*u == -1 (mod d),        v=(1+c*u)/d.              (1.3)
```

Let the common shell be the integer interval `[L,U]`, with

```text
U-L<min(c,d),                                       (1.4)
```

as in the project shell.  An ordered shell pair `x=(a,A)` with determinant

```text
t=a*c-A*d                                           (1.5)
```

has the unique expansion

```text
x=R*g-t*s,
a=d*R-t*u,                A=c*R-t*v.                (1.6)
```

The shell inequalities are exactly

```text
ell_t <= R <= r_t,                                  (1.7)

ell_t=max((L+t*u)/d,(L+t*v)/c),
r_t  =min((U+t*u)/d,(U+t*v)/c).
```

The interval in `(1.7)` has length less than one.  Hence a shell point of
label `t` exists precisely when

```text
ceil(ell_t)<=r_t,                                   (1.8)
```

and then

```text
R(t)=ceil(ell_t).                                   (1.9)
```

This is the exact partial Beatty graph.  There is no asymptotic or
floating-point rounding in `(1.7)--(1.9)`.

The determinant-one identity also gives

```text
v/c=u/d+1/(c*d).                                    (1.10)
```

Thus the two lower endpoints in `(1.7)` have slopes differing by only
`1/(cd)`, while the graph itself lies in the fixed-width strip

```text
R(t)-(u/d)t=a_t/d in [L/d,U/d].                    (1.11)
```

Requiring `a_t,A_t` to be actual prime powers merely restricts the domain
of this graph; it does not change its value `R(t)`.

---

## 2. The row and color graphs coincide

For an anchor row write, as in the anchor-GCD theorem,

```text
x=(a,A)=m(e)*g-e*s,
e=a*c-A*d.                                         (2.1)
```

For a partner color pair `gamma'=(c',d')`, put

```text
g'=(d',c')=n(k)*g-k*s,
k=c*d'-c'*d.                                       (2.2)
```

Both `x` and `g'` are ordered pairs in the same shell.  Applying Section 1
twice proves the exact identity

```text
m(e)=R(e),                 n(k)=R(k).               (2.3)
```

The domains differ: `e` must survive the anchor-carrier mask, whereas `k`
initially needs only to make `(d',c')` an actual shell pair.  But there are
not two independent rounding phases to average.

The second defect becomes

```text
f=e*n(k)-m(e)*k
 =e*R(k)-k*R(e)
 =(e*d'_k-k*a_e)/d
 =(e*c'_k-k*A_e)/c.                                (2.4)
```

Divisibility in the last two expressions is automatic.  Writing

```text
rho_t=R(t)-(u/d)t=a_t/d                            (2.5)
```

gives the especially transparent form

```text
f=e*rho_k-k*rho_e.                                 (2.6)
```

At the project scale `|e|,|k|<<D` and `rho_t=O(1)`, so `(2.6)` is already
`O(D)`.  In a one-sign interval `0<=e,k<=T`, if `U=d`, then

```text
0<=e*rho_k<=T,            0<=k*rho_e<=T,
|f|<=T.                                             (2.7)
```

The determinant window is therefore at its natural full diameter, not at
a large-sieve scale smaller than the diameter.

---

## 3. A scattered asymptotic integer obstruction

The preceding loss is not confined to a rich exact line.  Let

```text
M=(3 1; 2 1),              det M=1,
M^j=(d_j u_j; c_j v_j).                             (3.1)
```

Then

```text
d_j*v_j-c_j*u_j=1,
c_j/d_j -> sqrt(3)-1,
u_j/d_j -> alpha=(sqrt(3)-1)/2.                    (3.2)
```

The quadratic irrational `alpha` is badly approximable.  Put

```text
lambda=exp(-0.4),
L_j=ceil(lambda*d_j),       U_j=d_j,
T_j=floor(d_j^(16/33)).                              (3.3)
```

Since

```text
lambda < sqrt(3)-1 < 1,                             (3.4)
```

both anchor coordinates lie in `[L_j,U_j]` for large `j`, and the shell
has exactly the project endpoint ratio.  For `1<=t<=T_j`, Section 1 reduces
to

```text
R_j(t)=ceil((u_j/d_j)t),                            (3.5)
```

provided

```text
{(u_j/d_j)t}
 <=1-L_j/c_j-t/(c_j*d_j).                          (3.6)
```

The right side tends to the positive constant

```text
omega=1-lambda/(sqrt(3)-1)>0.                      (3.7)
```

The ratios `u_j/d_j` converge to `alpha` with error `O(d_j^(-2))`.
Bounded-type rotation discrepancy, or the elementary Ostrowski expansion
for this quadratic irrational, therefore gives

```text
#{1<=t<=T_j:(3.6)}=omega*T_j+O(log T_j).            (3.8)
```

The moving endpoint `t/(c_jd_j)`, the endpoint rounding in `L_j`, and the
replacement of `alpha` by `u_j/d_j` change the count by `O(1)`: their total
boundary displacement is
`O(1/d_j+T_j/d_j^2)=o(1/T_j)`, while bad approximability separates the
first `T_j` rotation points by `>>1/T_j`.

Every two occupied labels satisfy

```text
|e*R_j(k)-k*R_j(e)|<=T_j                           (3.9)
```

by `(2.7)`.  This remains true after restricting both labels to the endpoint
dyadic interval `[T_j/2,T_j]`, which still contains `asymp T_j` occupied
points.

It remains to verify that this is not a hidden rich-line packet.  If an
affine line through integer points has primitive direction `(s,r)`, then
along that line

```text
a_t=d_j*R_j(t)-u_j*t
```

changes in nonzero multiples of

```text
Delta=d_j*r-u_j*s.                                  (3.10)
```

For `s<=T_j`, bad approximability and the `O(d_j^(-2))` convergent error
give

```text
|Delta|>>d_j/s.                                    (3.11)
```

All `a_t` lie in an interval of length `O(d_j)`, so the line contains at
most `O(s)` occupied points.  Its horizontal span also gives at most
`O(T_j/s)` points.  Hence

```text
#(one line)<=O(min(s,T_j/s))<=O(sqrt(T_j)).         (3.12)
```

Equations `(3.8)`, `(3.9)`, and `(3.12)` prove `(0.3)`.  In particular, for
every `J=T_j^o(1)`, no line contains the `T_j/J` points required by the
dominant-tangent packet theorem, while the determinant graph has degree
`asymp T_j`.

This is an unrestricted-integer shell construction.  It deliberately does
not assert that its coordinates or carriers are actual prime powers.

---

## 4. The exact actual-carrier thinning

Let

```text
Q=q^3,                    E=C*q*D*q^o(1),           (4.1)
```

denote the additive form of the retained product window.  For an occupied
row point

```text
x_e=(a_e,A_e),                                    (4.2)
```

an anchor carrier must belong to

```text
J_gamma(e)=[L,U]
 intersect [(Q-E)/(8*a_e*c),(Q+E)/(8*a_e*c)]
 intersect [(Q-E)/(8*A_e*d),(Q+E)/(8*A_e*d)].      (4.3)
```

Each of the last two intervals has length

```text
O(E/q^2)=O(D/q)*q^o(1)=o(1).                       (4.4)
```

Thus `(4.3)` contains at most one integer, denoted `b_e`, and the actual
anchor domain is precisely the subset on which

```text
b_e exists and a_e,A_e,b_e are actual prime powers. (4.5)
```

For a partner label `k`, put

```text
g'_k=(d'_k,c'_k)=R(k)g-k*s.                        (4.6)
```

A shared completion additionally requires the unique integer in

```text
J_k(e)=[L,U]
 intersect [(Q-E)/(8*a_e*c'_k),(Q+E)/(8*a_e*c'_k)]
 intersect [(Q-E)/(8*A_e*d'_k),(Q+E)/(8*A_e*d'_k)] (4.7)
```

to exist and be an actual prime power `b'_(e,k)`.  Therefore the exact
residual incidence is

```text
I(e,k)=1_{a_e,A_e,d'_k,c'_k,b_e,b'_(e,k) actual}
       *1_{b_e in J_gamma(e)}*1_{b'_(e,k) in J_k(e)},  (4.8)
```

with the usual all-distinct deletions.

The first pair of carry equations implies `|e|<<D`, and the second implies
`|f|<<D`; but Section 3 shows that the latter inequality is not the sparse
part of `(4.8)`.  The sparse part is the simultaneous reciprocal rounding
and actual-prime-power requirement.

There is an equivalent carrier chord form.  The two equations sharing the
top row give

```text
|b_e*c-b'_(e,k)*c'_k|<<D,                          (4.9)
```

and the bottom row gives

```text
|b_e*d-b'_(e,k)*d'_k|<<D.                          (4.10)
```

For fixed colors, every short chord label determines the carrier pair
uniquely.  This is another exact partial matching, not an independent box.

---

## 5. Consequence for the high-tail search

The exact chart gives the following audit.

* The low determinant range `|k|<=D/K` remains closed by partner uniqueness
  and the second factorial estimate, as in the anchor-GCD theorem.
* The common Beatty graph does not extend that closure into `|k|~D`.
  The model in Section 3 is supported entirely in an endpoint dyadic label
  range, has no dominant affine line, and still has full determinant degree.
* Standard one-dimensional rotation discrepancy gives distribution, not
  sparsity, at the threshold `|f|~D`; its main term is the full pair count.
* A determinant large sieve could only gain when its window is `o(T)` for
  labels of diameter `T`.  Here `T<=D` and the available window is `D`.
* Any power improvement must therefore estimate the nested actual mask
  `(4.8)`, or an equivalent cross-partner interaction of the reciprocal
  carriers.  Dropping either carrier or replacing actual prime powers by all
  integers admits the obstruction in Section 3.

The finite replay

```text
d=6089, c=5179, [L,U]=[4098,6112], T=1000
```

has exactly

```text
212 occupied rounding points,
maximum affine-line occupancy 15,
maximum |eR(k)-kR(e)| 974,
minimum degree at threshold 1000 equal to 212.      (5.1)
```

Both anchor coordinates are prime, but the other coordinates are left as
integers; `(5.1)` is a hostile algebraic diagnostic, not an actual-QP
counterexample.  The actual `q=25013` six-cycle is also replayed and verifies
the quotient identity and uniqueness of the reciprocal carrier.

```text
canonical shell interval for R(t):                 PROVED;
m(e)=R(e), n(k)=R(k):                              PROVED;
exact determinant identity (2.4):                  PROVED;
project-scale f-window is non-sparse:              PROVED;
scattered asymptotic integer obstruction:          PROVED;
unique reciprocal carrier intervals:              PROVED;
Beatty/continued-fraction endpoint tail alone:     FALSE;
power bound for the nested actual carrier mask:    OPEN;
uniform four-cycle bound:                          OPEN.
```

Exact arithmetic and the finite diagnostics are in
`src/qp_sl2_rounding_graph.py` and its test module.
