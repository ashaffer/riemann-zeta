# QP four-cycle: exact residual rigidity and the surviving carrier gate

**Date:** 2026-08-15  
**Verdict:** the completed four-cycle bound `(FC)` is **not proved**.  One
entire sector is, however, now closed: at the active scale the actual
prime-power shell has no nondegenerate four-cycle whose color determinant is
zero.  Every surviving cycle has

```text
1 <= |c11*c22-c12*c21| << D.                       (0.1)
```

For each nonzero determinant the alternating residual sum is fixed by the
colors up to an error `O(D^2/q)=O(q^(-1/33+o(1)))`; hence it is the nearest
integer to one explicit rational.  The uncompleted arbitrary-weight color
sum over all the determinant layers in (0.1) already has the desired
`D q^o(1)` bound by a divisor argument.

The remaining loss is therefore not color near-energy.  It is the number of
actual `(a,b)` carrier completions of a color rectangle.  Exact row/column
differences reduce that completion problem to `O(D)` integral shifts.  At
the active aperture those shifts form a modular/reciprocal sample of length

```text
D=q^(16/33+o(1))=q^(1/2-1/66+o(1)),                (0.2)
```

just below the square-root length of its modulus.  The elementary argument
gives `O(D)`, while the suggested spectral closure needs a genuinely smaller
bound (for example `D^(1/2)q^o(1)` in the corresponding local-degree
formulation).  Proving that is a new joint affine-permutation/short-carrier
estimate, not a consequence of the residual identities.

No estimate below the existing `sqrt(R)` tensor norm, no QP theorem, and no
strip theorem is asserted here.

---

## 1. Setup and four exact identities

Let

```text
q be an odd prime,                   Q=q^3,
Y=q/2,
S={p^j:Y exp(-w)<p^j<Y exp(w)},
0<w<(log 2)/3.                                      (1.1)
```

In the truncated core write

```text
r_ij=8 a_i b_j c_ij-Q,              |r_ij|<=H,
H=qD,                               D=q^(16/33+o(1)), (1.2)
```

where harmless fixed shell and cutoff constants can be inserted.  A
nondegenerate rectangle has `a1!=a2` and `b1!=b2`.  Put

```text
S_r=r11+r22-r12-r21,
T_r=r11*r22-r12*r21,
k=c11*c22-c12*c21,
P=a1*a2*b1*b2.                                      (1.3)
```

The matrix identity

```text
Q*ones+r = 8 diag(a1,a2) (c_ij) diag(b1,b2)         (1.4)
```

gives, on taking determinants,

```text
Q*S_r+T_r=64*k*P.                                  (1.5)
```

Multiplying opposite corners instead gives

```text
(c12*c21)(Q+r11)(Q+r22)
 =(c11*c22)(Q+r12)(Q+r21),                         (1.6)
```

and therefore

```text
(c12*c21)(Q*S_r+T_r)
 =k(Q+r12)(Q+r21).                                 (1.7)
```

Finally define the four integral shifts

```text
u1=b1*c11-b2*c12,          u2=b1*c21-b2*c22,
v1=a1*c11-a2*c21,          v2=a1*c12-a2*c22.       (1.8)
```

Their residual identities are

```text
r11-r12=8*a1*u1,           r21-r22=8*a2*u2,
r11-r21=8*b1*v1,           r12-r22=8*b2*v2.        (1.9)
```

If `m=min S`, (1.2) and (1.9) imply

```text
|u_i|,|v_j|<=H/(4m)<<D.                             (1.10)
```

These formulas retain the completed coordinates; no unsigned projection has
been taken.

---

## 2. The zero color-determinant sector is empty

### Lemma 2.1 (short multiplicative interval)

Let `|x_i|<=H`, suppose `2H^2<Q`, and suppose

```text
(Q+x1)(Q+x4)=(Q+x2)(Q+x3).                          (2.1)
```

Then

```text
{x1,x4}={x2,x3}                                    (2.2)
```

as multisets.

Indeed, expansion of (2.1) gives

```text
Q(x1+x4-x2-x3)=x2*x3-x1*x4.                        (2.3)
```

The right side has magnitude at most `2H^2<Q`; hence both sides vanish.
Equality of the sums and products proves (2.2).

### Lemma 2.2 (multiplicative Sidonicity of the shell)

Distinct members of `S` are coprime.  If two were powers of the same prime,
their ratio would be at least two, whereas

```text
max(S)/min(S)<exp(2w)<2^(2/3)<2.                    (2.4)
```

Consequently

```text
x*y=u*v,                 x,y,u,v in S              (2.5)
```

forces equality of the unordered pairs `{x,y}={u,v}`.

### Theorem 2.3 (zero-determinant exclusion)

Assume

```text
2H^2<Q,                   2H<8(min S)^2.            (2.6)
```

There is no nondegenerate actual-shell rectangle with `k=0`.

**Proof.**  When `k=0`, (1.6) and Lemma 2.1 give one of two pairings.

For the row pairing,

```text
r11=r12,                 r22=r21.                  (2.7)
```

The first equality says `b1*c11=b2*c12`.  Since `b1!=b2`, Lemma 2.2 forces

```text
c11=b2,                  c12=b1.                   (2.8)
```

The second equality similarly gives `c21=b2,c22=b1`.  It follows that

```text
|r11-r21|=8*b1*b2*|a1-a2|.                         (2.9)
```

The left side is at most `2H`; the right side is at least
`8(min S)^2` unless `a1=a2`.  Condition (2.6) therefore makes the rectangle
degenerate.

For the column pairing the same argument interchanges `a` and `b` and forces
`b1=b2`.  This proves the theorem.  QED

At the active scale,

```text
H^2/Q=D^2/q=q^(-1/33+o(1)),                        (2.10)
```

so both inequalities in (2.6) hold after taking the Schwartz truncation
exponent sufficiently small.  The conclusion concerns the truncated core;
the already proved Schwartz-tail estimate remains separate.

---

## 3. Nonzero determinant: size and residual-sum pinning

Equation (1.5) immediately gives

```text
|k| <= (4QH+2H^2)/(64(min S)^4) << D.              (3.1)
```

Together with Theorem 2.3 this proves (0.1).

Let `C_off=c12*c21`.  Expanding (1.7) and dividing by `C_off*Q` yields the
exact formula

```text
S_r-kQ/C_off
 =k(r12+r21)/C_off
  +k*r12*r21/(C_off*Q)-T_r/Q.                      (3.2)
```

Thus

```text
|S_r-kQ/C_off|
 <=2|k|H/C_off+|k|H^2/(C_off*Q)+2H^2/Q
 <<D^2/q.                                          (3.3)
```

For large `q`, the right side is below `1/2`, and therefore

```text
S_r=nearest_integer(kQ/(c12*c21)).                 (3.4)
```

This is a genuine restriction on the colors.  It does not bound the number
of carrier completions by itself.

There is no determinant gap stronger than (0.1).  The exact all-prime
rectangle recorded in `qp_four_cycle_hostile_lab.py` has

```text
q=50021,                    k=6,
(u1,u2)=(-10,-16),          (v1,v2)=(42,36),
S_r=1208688,
S_r-6q^3/(c12*c21)=-0.039718... .                  (3.5)
```

All its normalized residuals lie inside the smooth inner core.  Hence an
argument requiring `|k|>=q^eta` is false even for actual primes.

---

## 4. The color determinant sum is already affordable

For an arbitrary complex vector `z`, define the absolute fixed layer

```text
E_k(z)=sum_(c11*c22-c12*c21=k)
       |z_c11 z_c12 z_c21 z_c22|.                 (4.1)
```

### Proposition 4.1

Uniformly in `k`,

```text
E_k(z)<=tau_max(q^2+|k|)*||z||_2^4
      <=q^o(1)||z||_2^4.                           (4.2)
```

Indeed, put `A=|z_c11 z_c22|`, `B=|z_c12 z_c21|` and use
`AB<=(A^2+B^2)/2`.  After fixing `c11,c22`, the complementary product is

```text
c12*c21=c11*c22-k,                                 (4.3)
```

which has at most the divisor-majorant number of ordered factorizations.
The second square is identical with the two diagonals interchanged.

Consequently

```text
sum_(0<|k|<<D) E_k(z)<<D q^o(1)||z||_2^4.          (4.4)
```

This is exactly the scale requested in `(FC)`, but (4.4) counts every color
rectangle once.  The completed four-cycle counts it once for each actual
`(a1,a2,b1,b2)` completion.  That multiplicity is the remaining issue.

---

## 5. Exact parametrization of the completion multiplicity

For `k!=0`, Cramer's rule applied to (1.8) gives

```text
b1=(c22*u1-c12*u2)/k,
b2=(c21*u1-c11*u2)/k,
a1=(c22*v1-c21*v2)/k,
a2=(c12*v1-c11*v2)/k.                              (5.1)
```

The compatibility identity is

```text
a1*u1-a2*u2=b1*v1-b2*v2=S_r/8.                    (5.2)
```

The quotient is integral because the four copies of `-Q` cancel in `S_r`.
Writing `L=S_r/8`, direct multiplication also gives

```text
v1*u1=c11*L-k*a2*b2,
v2*u2=c22*L-k*a1*b1.                              (5.3)
```

Equations (3.4), (5.1), and (5.3) are the promised exact residual
parametrization.  They separate the already controlled determinant layer
from the short carrier variables.

### 5.1 The fixed-cross-product conic

Fix the two diagonal colors

```text
c=c11,                    d=c22,
n=c12*c21,                k=c*d-n,                 (5.4)
```

and put

```text
s=a1*b1,                  t=a2*b2,
X=c12*a1*b2,              Y=c21*a2*b1.             (5.5)
```

Then

```text
X+Y=c*s+d*t-L,            X*Y=n*s*t.               (5.6)
```

Consequently `w=X-Y` lies on the exact conic

```text
w^2=(c*s+d*t-L)^2-4*n*s*t.                         (5.7)
```

For fixed `(c,d,n,s)`, view (5.7) as a quadratic in `t`.  If

```text
B_s=2*d*(c*s-L)-4*n*s,
```

then

```text
(2*d^2*t+B_s-2*d*w)(2*d^2*t+B_s+2*d*w)
 =16*n*s*(d*L-k*s).                                (5.8)
```

This factorization retains, rather than removes, the carrier shifts.  With
`e=c12` and `f=c21`, its two factors are exactly

```text
2*d^2*t+B_s-2*d*w = -4*f*b1*v2,
2*d^2*t+B_s+2*d*w = -4*e*a1*u2.                   (5.8a)
```

Thus applying the divisor bound separately at (5.8) cannot manufacture a
second saving: it simply refactors the two free nonzero shifts.

When the right side is nonzero, its divisor count gives `q^o(1)` possible
`(t,w)` for each `s`.  It vanishes exactly on the tangent equation

```text
k*s=d*L.                                           (5.9)
```

For each resulting `(s,t,w)`, the unordered pair `{X,Y}` is fixed by
(5.6).  Factoring `n`, `s`, and `t` and checking the shared row/column
factors costs at most a product of ordinary divisor functions, hence still
`q^o(1)`; it cannot increase the count.

Thus, for fixed `(c,d,n)`, summing the `O(D)` possible values of `s` gives
`O(D q^o(1))` completions.  This is rigorous but not enough: `n` itself
ranges over `O(D)` near-product values, so summing it separately returns the
old `D^2 q^o(1)` scale.  There is no injective map obtained merely by
summing the determinant before the carriers.

### 5.2 The exact tangent is affordable

The tangent in (5.9) is not a mysterious conic degeneration.  The second
identity in (5.3) says

```text
d*L-k*s=v2*u2.                                     (5.10)
```

Hence (5.9) is precisely `v2*u2=0`.

If `v2=0`, then `r12=r22`.  Lemma 2.2 and nondegeneracy force

```text
c12=a2,                   c22=a1.                  (5.11)
```

Moreover

```text
k=a1*c11-a2*c21=v1,       L=b1*k.                 (5.12)
```

For a fixed quadruple `(a1,c11,a2,c21)`, the two carrier coordinates
`b1,b2` are unique because their allowed intervals have length less than
one.  Its coefficient is

```text
|z_a1 z_c11 z_a2 z_c21|,                           (5.13)
```

and (5.12) is exactly a fixed determinant layer in those four actual-shell
variables.  Proposition 4.1 therefore bounds the total `v2=0` contribution
by `D q^o(1)||z||_2^4`.

Similarly, `u2=0` forces

```text
c21=b2,                   c22=b1,
k=b1*c11-b2*c12=u1,       L=a1*k,                 (5.14)
```

and the same weighted determinant argument applies.  Their intersection can
be counted twice harmlessly.  Thus **all exact tangent modes satisfy the
requested four-cycle scale**.

What remains is the generic sector `u2*v2!=0`.  The per-`s` factorization
(5.8) is divisor-sharp, but separately summing both `s` and the cross product
`n` still loses two factors of `D`.  Recovering one of them requires a joint
carrier estimate rather than another pointwise divisor bound.

---

## 6. The precise local theorem which is missing

Fix distinct `a1,a2 in S`, and count triples `(b,c1,c2)` for which

```text
|8*a1*b*c1-Q|<=H,             |8*a2*b*c2-Q|<=H.    (6.1)
```

Subtracting the two residuals gives

```text
v=a1*c1-a2*c2,                |v|<=H/(4 min S)<<D. (6.2)
```

The shell diameter is smaller than `min S`.  Since `gcd(a1,a2)=1`, all
integer solutions of `a1*c1-a2*c2=v` differ by `(a2,a1)`, so each fixed `v`
has at most one lift `(c1,c2)` in the shell.  Once `c1` is known, (6.1)
places `b` in an interval of length

```text
H/(4*a1*c1)<1,                                     (6.3)
```

so `b` is also unique.  This proves the local degree bound

```text
degree(a1,a2)<<D.                                  (6.4)
```

It does not prove the desired square-root improvement.  More explicitly,
(6.2) gives

```text
c1(v) == inverse(a1)*v (mod a2),                   (6.5)
```

with the unique shell lift, and the remaining test is

```text
distance(Q/(8*a1*c1(v)), S)<~D/q.                 (6.6)
```

Thus the live input is cancellation in the joint affine-permutation and
reciprocal carrier `(6.5)--(6.6)` for `|v|<<D`.  Its length is below
`sqrt(q)` by `q^(1/66)`.  Completing a generic modulus-`q` sum reaches a
`sqrt(q)` error, which is worse than the trivial `D` count here.  Separate
prime counts, the divisor bound (4.2), and unsigned residual energy do not
estimate this joint sample.

A theorem of the schematic form

```text
sup_(a1!=a2) degree(a1,a2)<<D^(1/2)q^o(1)          (6.7)
```

(or a suitably weighted averaged substitute compatible with the fourth
trace) is the next exact target.  Statement (6.7) is **open**, not a result
of this note.

---

## 7. Binary ledger

```text
exact residual/determinant identities:              PROVED;
zero color-determinant nondegenerate sector:         EMPTY / PROVED;
surviving determinant range 1<=|k|<<D:              PROVED;
alternating residual sum pinned within O(D^2/q):     PROVED;
fixed-layer weighted color bound q^o(1):            PROVED;
all-layer color-only bound D q^o(1):                PROVED;
exact conic tangent contribution D q^o(1):          PROVED;
fixed (diagonal colors, cross product) completions: O(D q^o(1)) / PROVED;
completed local degree O(D):                         PROVED;
completed local degree D^(1/2)q^o(1):               OPEN;
generic joint (cross product, carrier) saving:       OPEN;
four-cycle bound (FC):                               NOT PROVED;
tensor exponent below the existing sqrt(R) scale:   NOT PROVED;
QP or uniform strip:                                 NOT PROVED.
```

Executable replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_four_cycle_residual_gate.py \
  src/test_qp_four_cycle_hostile_lab.py
```
