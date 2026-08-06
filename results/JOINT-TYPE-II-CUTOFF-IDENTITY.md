# Joint Type-II cutoff identity

Status: exact analytic identity and fail-fast checkpoint, 2026-08-06.  This
note does **not** prove RH.

## 1. Verdict

There is an exact arithmetic identity coupling the full cofactor sum, every
moving cutoff quadrant, and the explicit centering from R68.

* The four cutoff quadrants form an outer-product `2 x 2` table, of rank at
  most one, whose sum is
  `-zeta'/zeta`.
* The balanced entry is a weighted logarithmic derivative of a truncated
  Euler product.
* Simultaneous movement of the two cutoffs obeys an exact
  row/column/intersection product rule and is path-independent.
* Applying the exact Type-I centering makes the centered observable exactly
  cutoff-independent.
* Entrywise ramp evaluation destroys rank one, but its resulting exterior-
  square determinant has no fixed sign; Arb certifies an actual-arithmetic
  sign change at two small moving cutoffs.

This is the requested joint conservation law, but it supplies no new bound.
Its coefficient form is Vaughan's identity, its all-mode form is the complete
Volterra--Hankel expansion from R69, and its natural sign-reversing involution
leaves the same coherent semiprime block.  Algebra couples all the pieces but
provides neither sign nor contraction.

## 2. Outer-product cutoff table

For `Re(s)>1` and an integer cutoff `Y`, put

```text
K(s)=-zeta'(s)/zeta(s),
M_Y(s)=sum_(d<=Y)mu(d)d^(-s),
A_Y(s)=1/zeta(s)-M_Y(s),
L_Y(s)=sum_(b<=Y)Lambda(b)b^(-s),
C_Y(s)=K(s)-L_Y(s),
F_Y(s)=zeta(s)A_Y(s)=1-zeta(s)M_Y(s).                     (2.1)
```

The full cofactor-balanced series is

```text
D_Y(s)=zeta(s)A_Y(s)C_Y(s)=F_Y(s)C_Y(s).                 (2.2)
```

All four cutoff sectors occur in the outer-product table

```text
              [ M_Y L_Y    M_Y C_Y ]
T_Y(s)=zeta(s)[ A_Y L_Y    A_Y C_Y ].                     (2.3)
```

Consequently,

```text
sum_(i,j)(T_Y)_(i,j)=K(s),
det T_Y(s)=0.                                             (2.4)
```

The lower-right entry is `D_Y`.  The other three entries combine to the exact
Type-I complement

```text
I_Y(s):=K(s)-D_Y(s)
       =L_Y(s)-M_Y(s)zeta'(s)-zeta(s)M_Y(s)L_Y(s).         (2.5)
```

Coefficientwise, (2.4)--(2.5) are precisely

```text
mu_(>Y)*Lambda_(>Y)*1
 =Lambda-mu_(<=Y)*log-Lambda_(<=Y)
   +mu_(<=Y)*Lambda_(<=Y)*1.                              (2.6)
```

Thus the table retains every cofactor and both cutoff tails, but its
conservation law is exactly Vaughan's identity in outer-product form.

## 3. Weighted logarithmic derivative

The table has a natural Euler-product interpretation.  Define

```text
P_Y(s)=exp(sum_(2<=n<=Y) Lambda(n)/[(log n)n^s])
      =exp(sum_(p^j<=Y) p^(-js)/j),
R_Y(s)=zeta(s)/P_Y(s).                                    (3.1)
```

In the declared half-plane `Re(s)>1`, use the canonical zero-free logarithm
of `R_Y`.  Since `(log P_Y)'=-L_Y`, one has

```text
C_Y(s)=-(log R_Y(s))',
D_Y(s)=-F_Y(s)(log R_Y(s))'.                              (3.2)
```

This packages the complete cofactor cancellation and the large-prime
logarithmic derivative in one formula.  It is not a pure Euler-product
logarithmic derivative.  If

```text
Q_Y(s)=exp(F_Y(s)log R_Y(s)),
```

then the product rule leaves the exact commutator

```text
D_Y=-(log Q_Y)'+F_Y'log R_Y.                              (3.3)
```

The commutator cannot be deleted from this natural prime-local product
representation.  For distinct primes `p,q>Y`, the coefficient of `D_Y` at
`pq` is `-log(pq)`.  A prime-local Euler-product logarithmic derivative is
supported on prime powers, so any such representation of `D_Y` would need
cross-prime factors and would merely encode the same balanced convolution
nonlocally.  This does not exclude the tautological nonlocal construction
`exp(-integral D_Y)`.

## 4. Exact cutoff transport

Increase the common cutoff from `Y=n-1` to `Y=n`.  With the old values of
`F_Y,C_Y`, write

```text
alpha=mu(n),   lambda=Lambda(n),   z=n^(-s).
```

Then

```text
F^+=F-alpha z zeta,
C^+=C-lambda z,

Delta D
 =-alpha z zeta C-lambda z F+alpha lambda z^2 zeta.       (4.1)
```

These are respectively row removal, column removal, and restoration of the
double-counted intersection.  Updating the Möbius and von Mangoldt cutoffs
in either order gives the same mixed difference.  The cutoff transport is
therefore flat and path-independent.

For any scalar arithmetic weight `W_x(n)`, coefficient evaluation of (4.1)
gives

```text
Delta B
 =-mu(n) sum_(b>=n,m) Lambda(b)W_x(nbm)
  -Lambda(n) sum_(d>=n,m) mu(d)W_x(dnm)
  +mu(n)Lambda(n) sum_m W_x(n^2m).                         (4.2)
```

This is the exact moving row/column/intersection identity found in R69.

## 5. Coupling the moving centering

Let `mathcal L_x` apply the R68 ramp weight to the coefficients of a
Dirichlet series.  Write

```text
S(x)=mathcal L_x(K),
B_Y(x)=mathcal L_x(D_Y),
T_Y(x)=mathcal L_x(I_Y).                                  (5.1)
```

Equations (2.4)--(2.5) give the exact identity

```text
B_Y(x)+T_Y(x)=S(x).                                       (5.2)
```

If `J sqrt(x)` is the pole main term, define the exact moving centering

```text
Z_Y^exact(x)=J sqrt(x)-T_Y(x).                             (5.3)
```

Then

```text
B_Y(x)-Z_Y^exact(x)=S(x)-J sqrt(x)=C_full(x),              (5.4)
```

independently of `Y`.  In particular,

```text
Delta T_Y=-Delta B_Y,
Delta Z_Y^exact=Delta B_Y.                                (5.5)
```

This `Z_Y^exact` contains the complete unevaluated Type-I sum.  It is a
tautological exact coordinate, not an effective closed centering.

The explicit R68 centering replaces the exact Type-I evaluation by

```text
T_Y^app(x)=I_pol(x;Y,Y)+I_0(Y,Y),
Z_Y(x)=J sqrt(x)-T_Y^app(x).                              (5.6)
```

Define its signed Euler-evaluation defect by

```text
E_Y(x)=T_Y^app(x)-T_Y(x).                                 (5.7)
```

The complete joint identity is therefore

```text
B_Y(x)-Z_Y(x)=C_full(x)+E_Y(x),
Delta(B_Y-Z_Y)=Delta E_Y.                                 (5.8)
```

For fixed smoothing order `k`, `Y=floor(x^theta)`, and the support hypotheses
of R68, one has `E_Y=o(1)` when `0<theta<theta_k` and `E_Y=O(1)` at
`theta=theta_k`.  This validates the moving centering and explains every
cutoff jump, but it does not bound `C_full`.  It only moves the same unknown
scalar between the balanced and Type-I coordinates.

## 6. Every singular mode

For the sharp hyperbola assume `log(x/Y^2)>ell` and put

```text
T=log(x/Y^2),
omega_j=(2j-1)pi/(2T),
e_j(u)=sqrt(2/T)cos(omega_j u),
lambda_j=(-1)^(j-1)/omega_j.                              (6.1)
```

The sharp triangular kernel has the Cesaro singular expansion

```text
1_(u+v<T)=Cesaro-sum_j lambda_j e_j(u)e_j(v).              (6.2)
```

Away from the boundary `dr=x`, finite coefficient evaluation gives exactly

```text
B_Y^sharp(x)=Cesaro-sum_j lambda_j M_j(x)B_j(x),           (6.3)

M_j=sum_(Y<d<=x/Y) mu(d)d^(-1/2)e_j(log(d/Y)),
B_j=sum_(Y<r<=x/Y) beta_Y(r)r^(-1/2)e_j(log(r/Y)).         (6.4)
```

Here `beta_Y(r)=sum_(b|r,b>Y)Lambda(b)`, so every cofactor is already
included.
These projections are real parts of finite Dirichlet polynomials at
`1/2-i omega_j`.  The finite hyperbola truncation prevents a modewise Euler
factorization.  Summing every mode recovers `B_Y^sharp`; passage back to its
Dirichlet series then recovers (2.2).  The full cofactor sum was already
retained inside `beta_Y` in every `B_j`.

Fixed-order smoothing does not create a preferred common basis.  If
`S=s_1+...+s_k`, with the `s_i` independent uniform variables on `[0,h]`,
then, with the arithmetic cutoffs held fixed,

```text
B_Y^(k)(x)=Expectation_S B_Y^sharp(x exp(-S)),
Z_(Y,star)^(k)(x)=Expectation_S Z_(Y,star)^sharp(x exp(-S)), (6.5)
```

where `star` may mean the exact or the R68 approximate centering, provided
the same choice is made on both sides.  For the approximate sharp centering,
use `J_0=2`, `K_0=-4`, the same fixed `Y`, and the unchanged `I_0`.
Each sharp summand has length `T-S` and hence different singular vectors.
Moreover `Z_Y` is made from Type-I head moments outside the tail operator;
there is no canonical modewise allocation of it.  Any such allocation is a
gauge choice.  Summing the full expansion gives (5.8), not an additional
Parseval, Wronskian, or Ward conservation law.

## 7. The exact divisor involution

There is also a full-cofactor-sum, product-preserving sign-reversing
involution.  Let `W` have finite support, as the ramp does, or enough absolute
convergence to justify regrouping, and define

```text
B_y(W)=sum_(d>y,b>y,m>=1)mu(d)Lambda(b)W(dbm).
```

Group `q=dm` and set

```text
M_y(q)=sum_(d|q,d>y)mu(d).                                (7.1)
```

For `q>1`, choose a canonical prime `p(q)|q`.  Pair each squarefree divisor
`e` not divisible by `p(q)` with `e p(q)`, moving `p(q)` between the Möbius
divisor and its cofactor.  All pairs cancel except those crossing the cutoff,
giving

```text
M_y(q)
 =-sum_(e|q, p(q) not| e, y/p(q)<e<=y)mu(e).              (7.2)
```

Consequently,

```text
B_y(W)
 =-sum_(b>y,q>1) Lambda(b)W(bq)
    sum_(e|q,p(q) not| e,y/p(q)<e<=y)mu(e).               (7.3)
```

This is a genuine divisor-boundary identity, but the boundary is not thin.
If `q` is prime and exceeds `y`, then `e=1` remains.  For products of two
distinct primes above `y`, all admissible terms in the product fiber are
negative, and (7.3) gives `-log(pq)`; at `p^2` the coefficient is `-log p`.
Hence no product-fiber-preserving, termwise sign reversal can remove that
block.  A useful pairing would have to cross distinct products, though not
necessarily distinct scales.

## 8. Exterior-square sign test

The determinant-zero identity does have one nontrivial descendant.  If a
linear functional has a justified representation

```text
mathcal L(H)=integral H(s)dnu(s)
```

and `T(s)=zeta(s)u(s)v(s)^T`, then the `2 x 2` Cauchy--Binet identity gives

```text
det mathcal L(T)
 =1/2 integral integral zeta(s)zeta(t)
   det[u(s),u(t)]det[v(s),v(t)]dnu(s)dnu(t).               (8.1)
```

For `u=(M_Y,A_Y)` and `v=(L_Y,C_Y)`, this simplifies to

```text
det mathcal L(T)
 =1/2 (mathcal L tensor mathcal L)[
   (F_Y(t)-F_Y(s))
   (L_Y(s)K(t)-K(s)L_Y(t))].                              (8.2)
```

This exterior square measures exactly how entrywise smoothing destroys rank
one.  It would be useful if the two wedge factors had a common orientation.
They do not have a fixed arithmetic sign.

There is a completely coefficientwise version.  For a nonnegative arithmetic
weight `W_x`, put `H_x(q)=sum_m W_x(qm)` and let `Q_ij` be the four evaluated
cutoff sectors.  Direct expansion gives

```text
det Q
 =sum_(d<=Y<e, b<=Y<c) mu(d)mu(e)Lambda(b)Lambda(c)
   [H_x(db)H_x(ec)-H_x(dc)H_x(eb)].                       (8.3)
```

Even a fixed-sign Hankel minor would be multiplied by the indefinite factor
`mu(d)mu(e)`.  The failure occurs before asymptotics.  At `Y=2`, if `E(n)` is
the coefficient matrix of `n^(-s)` in (2.3), then

```text
det[E(3)+E(6)]= log(2)log(3)>0,
det[E(2)+E(9)]=-log(2)log(3)<0.                            (8.4)
```

Nor is the determinant coercive for the balanced entry: for any prime
`p>Y`, `det E(p^2)=0` although its balanced coefficient is `-log p`.

The sign failure persists for ordinary positive smoothing.  For any fixed
cutoff `Y`, the one-sided ramp and the prime number theorem give

```text
det Q_Y(x)=J^2 x M_Y(1)L_Y(1)+o_Y(x).                     (8.5)
```

Here `L_Y(1)>0`, while `M_2(1)=1/2>0` and
`M_5(1)=1-1/2-1/3-1/5=-1/30<0`.  Thus the same positive
ramp produces both eventual signs at fixed cutoffs.

For the one-sided unit ramp, apply the coefficient functional entrywise to
(2.3), using the moving cutoff `Y=floor(X^(3/8))`.  Arb interval arithmetic
certifies

```text
det mathcal L_70(T_4)
 =[8.78195851326225429234858644994 +/- 1e-28] >0,

det mathcal L_80(T_5)
 =[-3.63367865689937808594145237569 +/- 1e-28] <0.         (8.6)
```

After deleting every prime-power term except the primes, the corresponding
determinants are respectively
`[6.1632708564811506231 +/- 1e-18]` and
`[-2.6999443933196089697 +/- 1e-18]`.  The sign change is not a prime-power
artifact.

The exact certificate is
[`src/joint_cutoff_determinant_falsifier.py`](../src/joint_cutoff_determinant_falsifier.py),
with a focused regression test.  This refutes a fixed-sign determinant or
total-positivity shortcut for the natural ramp-evaluated cutoff table.  It
does not rule out a different completed matrix, a non-determinantal
invariant, or an inequality using additional arithmetic structure.

## 9. What the identity changes

The construction succeeds algebraically and fails analytically:

* the cutoff connection is exactly flat, so this outer-product transport
  supplies no additional holonomy or index;
* the determinant-zero law is multiplicative, while ramp evaluation is
  linear; its exterior-square defect changes sign on the actual arithmetic
  table;
* singular-mode allocation of the head centering is noncanonical;
* fiberwise Möbius cancellation stops at a large semiprime boundary.

Thus the purely algebraic Euler-product, Vaughan/Buchstab, all-mode, and
product-fiber constructions considered here yield only these identities.  In
this cutoff-involution route, a further advance must add a non-fiberwise
arithmetic estimate that lets the semiprime collar cancel with other
balanced parity/cofactor sectors and possibly the Type-I head **before**
taking absolute values.  The exact transport law (4.1) is the correct ledger
for such an estimate, but supplies no sign by itself.

## 10. Evidence boundary

Sections 2--7 are coefficientwise Dirichlet-convolution identities,
elementary product differentiation, and the classical singular expansion of
the triangular integral kernel.  Section 8 uses the elementary `2 x 2`
Cauchy--Binet identity and a Python FLINT/Arb interval certificate.  The Euler
error quoted after (5.8) is the fixed-order estimate proved in R68.  No step
assumes RH.  None of these identities proves the required bound, Weil
positivity, or RH, and none is formalized in Lean.

The focused reproduction commands are

```text
PYTHONPATH=src python3 -m unittest -v \
  src/test_joint_cutoff_determinant_falsifier.py
python3 src/joint_cutoff_determinant_falsifier.py
```

The 2026-08-06 audit used Python 3.12.3, `python-flint 0.9.0`, FLINT 3.6.0,
and 50 decimal digits.  A release must additionally record a committed source
hash.
