# QP four-cycle: odd-prime recentered reciprocal-alias barrier

**Date:** 2026-08-22  
**Verdict:** there is an exact rational recentering at infinitely many odd
prime moduli which recreates the critical tangent alias in the full integer
shell.  It is coherent for `sqrt(D)` translations and for polynomially many
color levels.  After all cross-level rectangles are merged, the whole
**direct** Schatten-four mass is `O(D)` by a sharp Hankel/Young inequality.
The deliberately displayed fixed-color rectangles have mass only
`D^(3/4+o(1))`; the larger `D^(5/4+o(1))` quantity is the
pair-of-completions energy `m(C)(m(C)-1)`.  Thus this is not a counterexample
to `(FC)`.

The exact anchor is never a prime power.  Removing that obstruction requires
a growing-denominator near-rational alias, not a parity or local-curvature
argument.  Standard `abc` does not exclude such aliases: after elimination,
the error term has generic radical at least as large as the main height.

---

## 1. An exact rational point at prime `q`

Let

```text
q ==2591 (mod 3168),
A=3*(2q-1)/11,
C=121*(q+1)/288.                                  (1.1)
```

The congruence is equivalent to

```text
q==287 (mod 288),             q==6 (mod 11).       (1.2)
```

Since `gcd(2591,3168)=1`, Dirichlet's theorem supplies infinitely many prime
values of `q` in (1.1).  For every one of them, `A,C` are integers and

```text
8*A^2*C=(q-1/2)^2*(q+1)=q^3-(3q-1)/4,             (1.3)
1728*C-1331*A=1089.                                (1.4)
```

The limiting shell ratios are

```text
A/(q/2)=12/11=1.0909...,
C/(q/2)=121/144=.84027...,                         (1.5)
```

both strictly inside the project shell of logarithmic half-width `.2`.
Equation (1.3) is much stronger than the required `O(qD)` product window.
Equation (1.4) is the nonzero, bounded slope defect.

The smallest convenient replay is the prime `q=15263`, for which

```text
A=8325,                 C=6413=11^2*53.            (1.6)
```

---

## 2. Multilevel tangent grid with bounded slope defect

Put

```text
R=1728,                 S=1331,       delta=RC-SA=1089.
```

For positive steps `h,l`, a translation `t`, and `i,j in {0,1}`, define

```text
a_i(t)=A+R*i*h+t,
b_j(t)=A+R*j*l-t,
c_ij=C-S*(i*h+j*l).                                (2.1)
```

Write `u=ih`, `v=jl`, `sigma=u+v`, and

```text
P=R^2*u*v+R*(v-u)*t-t^2.                           (2.2)
```

Direct expansion gives the exact identity

```text
a_i(t)b_j(t)c_ij-A^2*C
 =A*delta*sigma+C*P-A*R*S*sigma^2-S*sigma*P.       (2.3)
```

There is no uncancelled term of size `q^2 h`.  If

```text
|Rh|+|Rl|+|t| <=epsilon*sqrt(D),                   (2.4)
```

then (1.3) and (2.3) give

```text
|8*a_i(t)b_j(t)c_ij-q^3|<<_(R,S) epsilon*qD+q.     (2.5)
```

For a sufficiently small fixed `epsilon`, every displayed corner therefore
lies in the retained product window for all large prime `q` in (1.1).
All coordinates remain in the shell because `sqrt(D)=o(q)`.

The top-left corner already displays the reciprocal alias transparently:

```text
(A+t)(A-t)C=A^2*C-C*t^2.                           (2.6)
```

At `|t|<=sqrt(D)`, the quadratic drift is exactly `O(qD)`.  Hence a
one-dimensional Poisson or van der Corput argument cannot save a power on
this fan; its curvature is at the critical coherent scale.

### Same-base tangent directions merge uniquely

There is a useful uniform consequence of the exponent `D^(3/2)<q`.  Let
`L=sqrt(D)` and fix one ordered base pair `(A,C)` with `A,C asymp q`.
Suppose two certified affine tangent packets have primitive directions
`(R,S)` and `(R',S')`, occupied lengths `H,H'>=1`, and satisfy

```text
max(|R|,|S|)*H <=C_1*L,
max(|R'|,|S'|)*H'<=C_1*L,                          (2.7)
|C*R-A*S| <=C_2*D/H,
|C*R'-A*S'|<=C_2*D/H'.                             (2.8)
```

The determinant of the directions obeys the exact estimate

```text
C*|R*S'-R'*S|
 <=|S'|*|C*R-A*S|+|S|*|C*R'-A*S'|
 <<D*L/(H*H').                                     (2.9)
```

Therefore

```text
|R*S'-R'*S| <<D^(3/2)/q
              =q^(-3/11+o(1))<1.                 (2.10)
```

The determinant is integral, so it vanishes.  Primitivity makes the two
directions equal up to sign.  Thus **all certified critical affine packets
based at the same ordered `(A,C)` merge into one direction**, with no
logarithmic or polynomial direction multiplicity.

This is a genuine slope-block improvement, but not the global cover: a fixed
anchor color can still occur with varying row/carrier base pairs, and sparse
one- or two-point packets need not satisfy the tangent hypotheses (2.8).

---

## 3. Merged direct mass versus pair-completion energy

Let `L asymp sqrt(D)` be the number of translations and let

```text
H asymp L/R                                                 (3.1)
```

be the number of legal step values.  Take `h,l` in one interval of length
`H`, with `h!=l`.  There are `asymp H^2` distinct color matrices, each with
`asymp L` translations.  Their combined color support is

```text
{C} union {C-S*s: s in an interval of length asymp 3H}.     (3.2)
```

Give the anchor squared mass `1/4` and distribute squared mass `3/4`
uniformly over the nonanchor colors.  Every color rectangle then has weight

```text
w_z(C_matrix) asymp H^(-3/2).                      (3.3)
```

The deliberately displayed fixed-color rectangles are counted once in the
direct form.  Their contribution is

```text
sum_C m(C) w_z(C)
  asymp H^2*L*H^(-3/2)
  =L*sqrt(H)
  <<D^(3/4).                                       (3.4)
```

This is not the full direct form of the union: triples belonging to different
levels create additional cross-level rectangles.  Those rectangles merge
rather than accumulate independently.  Put

```text
x=a-A=t+R*i*h,             y=b-A=-t+R*j*l.         (3.5)
```

Then every retained entry obeys

```text
x+y=R*(i*h+j*l),
c=C-(S/R)*(x+y).                                   (3.6)
```

After harmless affine reindexing and deletion of unused entries, the entire
matrix is a submatrix of a compressed Hankel matrix

```text
H_(x,y)=z_(C-S*(x+y)/R).                            (3.7)
```

The row and column intervals have length `O(L)`, each color anti-diagonal has
multiplicity `O(L)`, and only `O(H)` colors occur.  Therefore

```text
||H||_F^2 <<L*||z||_2^2,
||H||_op^2 <=||z||_1^2 <<H*||z||_2^2.              (3.8)
```

Young's convolution inequality gives the operator estimate in (3.8).
Consequently the **whole merged direct patch**, including every cross-level
rectangle, satisfies

```text
||H||_S4^4 <=||H||_op^2*||H||_F^2
             <<L*H*||z||_2^4
             <=L^2*||z||_2^4
             <<D*||z||_2^4.                        (3.9)
```

By contrast, a Cauchy--Schwarz route which first asks for the factorial
pair energy sees

```text
sum_C m(C)(m(C)-1) w_z(C)
  asymp H^2*L^2*H^(-3/2)
  =L^2*sqrt(H)
  asymp_R D^(5/4).                                (3.10)
```

Equations (3.4), (3.9), and (3.10) locate an exact loss of one translation
factor.  They explain why the recentered alias defeats a common-neighbor
second moment but does not defeat the direct zero-modulation/Schatten-four
target.

---

## 4. Why the exact alias is not an actual-prime-power family

From (1.1),

```text
C=11^2*k,                 k=(q+1)/288.             (4.1)
```

The two congruences in (1.2) imply `11` does not divide `k`.  For all large
`q`, `k>1`, so `C` has at least two distinct prime divisors.  In particular,
the shared anchor is never a prime power.

This is the exact rational-slope obstruction in a slightly different form.
It does not survive the actual mask.  But replacing `C` by a nearby prime
changes `8A^2C` by `asymp q^2`, much larger than `qD`.  The base point,
modulus, and slope must all be retuned simultaneously.  Therefore the
remaining actual problem is a shrinking-target, growing-denominator
problem; it is not removed by simply sieving the exact grid.

For a general primitive tangent direction `(R,S)`, coherence over a fan of
length `H` with physical width `RH<=sqrt(D)` permits

```text
|RC-SA| <<D/H,
|C/A-S/R| <<D/(q*R*H).                             (4.2)
```

For a maximally extended fan `RH asymp sqrt(D)`, the last accuracy is
`sqrt(D)/q`.  The generic denominator needed to approximate a shell ratio
to that accuracy is

```text
R_generic asymp sqrt(q/sqrt(D))=q^(25/66),         (4.3)
```

whereas a coherent direction has `R<=sqrt(D)=q^(16/66)`.  Thus a dangerous
fan is precisely an exceptional rational alias across the gap
`q^(9/66)=q^(3/22)`.

---

## 5. Standard `abc` does not close the alias

Let a prospective near alias satisfy

```text
epsilon=8A^2C-q^3,              delta=RC-SA.       (5.1)
```

Eliminating `C` gives the exact shifted-cubic equation

```text
8S*A^3-R*q^3=R*epsilon-8*delta*A^2.                (5.2)
```

In the active range, `A,C,q asymp q`, `|epsilon|<<qD`, and a nonzero
determinant defect already makes the right side generically as large as
`|delta|q^2`.  After division by the common gcd, the radical in the standard
`abc` application can be bounded only by

```text
rad(8S*A^3 * R*q^3 * (R*epsilon-8*delta*A^2))
 <<rad(RS)*q^2*|R*epsilon-8*delta*A^2|.             (5.3)
```

For a generic `q^2` error, the available radical upper bound is of order
`q^4`, while the main height in (5.2) is only `Rq^3`.  It therefore gives
no quality-above-one contradiction.  The same failure occurs in the simpler determinant equation
`RC-SA=delta`, whose radical contains both shell-scale factors `A,C`.

Consequently standard `abc`, even if assumed, supplies no uniform exclusion
of the nonzero near-rational aliases relevant to the direct problem.

---

## 6. Consequence for the reciprocal/common-neighbor route

```text
odd-prime-q exact recentering:                    PROVED;
critical sqrt(D) reciprocal fan:                  PROVED;
same-base certified tangent-direction uniqueness: PROVED;
displayed fixed-color direct submass:              O(D^(3/4));
whole merged direct Schatten-four mass:            O(D);
pair-completion energy of this family:             Theta(D^(5/4));
actual-prime-power embedding of exact family:      IMPOSSIBLE;
standard abc exclusion of near aliases:            NO;
outer-fan / actual-mask aggregation:               OPEN;
uniform FC from this route:                        NOT PROVED.
```

The exact identities and mass ledger are replayed by

```text
src/qp_odd_prime_reciprocal_alias.py
src/test_qp_odd_prime_reciprocal_alias.py
```

with

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_odd_prime_reciprocal_alias.py
```
