# QP signed discrepancy: the affine-carrier gate

**Date:** 2026-08-15

**Verdict:** signed vector balancing does not presently prove fixed-power QP.
The continuum discretization is cheap enough: if a signing has the required
carrier, a polynomial grid of size

```text
Y^(50/33+1/2+o(1))=Y^(133/66+o(1))                  (0.1)
```

certifies the complete band.  The failure is instead exact and affine.
Spencer/Banaszczyk-type discrepancy controls the carrier row on the same
square-root scale as every spectral row, while QP requires the carrier to be
`Y^c` square-root scales larger.  Translating or biasing a rounding scheme
does not remove this tax: the fractional centre must already be a Delsarte
antenna, up to the rounding error.

There are three precise results.

1. The symmetric signed-discrepancy problem is polar to minimum-TV signed
   carrier synthesis on the same actual cosine curve.  It is a stronger form
   of the existing one-sided Delsarte kill, not a relaxation.
2. Conditioning random signs to have the exceptional carrier needed by QP
   reproduces the uniform actual-node antenna in conditional expectation;
   its normalized fluctuations are of QP size.  Thus biased signing rounds
   the unknown natural antenna rather than replacing it.
3. An odd-half-period grid defeats **arbitrary signed coefficients**, not
   only positive weights.  After an arbitrarily small rationally independent
   perturbation it still defeats every coefficient vector of polynomial
   normalized total variation.  Hence count, mesh, rational independence,
   and generic vector-balancing norms cannot imply the desired theorem.

The half-grid is not the actual prime-log set, and exceptional deterministic
signings are not ruled out by the conditional-probability calculation.
Accordingly no QP-KILL, QP-PROMOTE, or zero-free strip is claimed.  The live
statement remains an actual-prime affine residual/Delsarte theorem.

---

## 1. The exact signed target

Let the distinct nonzero actual nodes be

```text
u_1,...,u_M in (0,w],              w=1/5,
a(t)=(cos(tu_j))_(j<=M),           q=(1,...,1),
H=[T,B]=[Y^.01,Y^(50/33)].                         (1.1)
```

The project one-sided signed antenna asks for `y` such that

```text
q^T y=1,
inf_(t in H) y^T a(t)>=-epsilon,                    (1.2)
```

with `epsilon=Y^(-c)` and the required fixed `c`.  The symmetric discrepancy

```text
Delta_H=inf_(q^T y=1) sup_(t in H)|y^T a(t)|         (1.3)
```

is stronger: `Delta_H<=epsilon` implies (1.2).

Define the signed synthesis cost

```text
C_H=inf {||nu||_TV:
          nu a finite signed measure on H,
          integral_H a(t)dnu(t)=q}.                 (1.4)
```

### Theorem 1.1 (symmetric discrepancy/TV reciprocity)

For the distinct cosine nodes in (1.1),

```text
Delta_H C_H=1.                                      (1.5)
```

#### Proof

The vectors `a(t)`, `t in H`, span `R^M`.  Otherwise a nonzero vector `z`
would make

```text
sum_j z_j cos(tu_j)=0
```

on an interval.  Analytic continuation and linear independence of the
distinct exponentials `exp(+/- i u_j t)` force every `z_j=0`.

The finite-dimensional dual of (1.4) is

```text
C_H=sup {q^T z:sup_(t in H)|z^T a(t)|<=1}.           (1.6)
```

This is the standard total-variation/moment duality; it also follows
directly by separating the image of the TV unit ball under
`nu -> integral a dnu`.  Scaling `z` in (1.6) shows that its supremum is
exactly `1/Delta_H`, proving (1.5).  QED

Thus a symmetric discrepancy proof at level `Y^-c` is exactly a proof that
every signed representation of the carrier by legal high-band atoms costs
at least `Y^c`.  The coefficient signs have not weakened the arithmetic
statement.  The existing one-sided Delsarte value can be smaller than
`Delta_H`; (1.5) must not be advertised as an equivalence for the one-sided
problem.

---

## 2. The continuum grid is not the obstruction

For arbitrary real coefficients `c_j`, write

```text
F_c(t)=sum_j c_j cos(tu_j),
S=q^T c>0,                     N=||c||_1.             (2.1)
```

Then

```text
|F_c'(t)|<=wN.                                       (2.2)
```

### Lemma 2.1 (norm-sensitive grid transfer)

Take a grid containing both endpoints of `H` and having mesh at most

```text
h=epsilon S/(2wN).                                  (2.3)
```

If

```text
F_c(tau)>=-(epsilon/2)S             at every grid point, (2.4)
```

then

```text
F_c(t)>=-epsilon S                  for every t in H. (2.5)
```

The grid may be chosen with at most

```text
2+2w(B-T)N/(epsilon S)                             (2.6)
```

points.

#### Proof

Every point of the interval is within `h` of a grid point.  Equations
(2.2)--(2.3) make the interpolation loss at most `epsilon S/2`; combine it
with (2.4).  The count in (2.6) is immediate.  QED

For a sign vector, `N=M`.  A standard finite-grid discrepancy scale is

```text
D asymp sqrt(M log G),                               (2.7)
```

where `G` is the number of constraints.  To turn this into normalized error
`epsilon`, the carrier must obey

```text
S >= 2D/epsilon
  asymp epsilon^(-1)sqrt(M log G).                   (2.8)
```

Substitution into (2.6) gives the self-consistent bound

```text
G << B sqrt(M/log G).                                (2.9)
```

Since `M=Y^(1+o(1))` and `B=Y^(50/33)`, one can take (0.1).  In particular,
`log G=O(log Y)`, exactly the regime in which ordinary finite discrepancy
bounds operate.  Unbounded real coefficients require the norm-sensitive
grid (2.6), but sign coefficients do **not** suffer a superpolynomial
continuum tax.

This calculation removes a false blocker.  It does not produce the carrier
in (2.8).

---

## 3. Affine rounding preserves the missing debt

Let `A` be the node-by-grid cosine matrix, let `x` be a fractional centre,
and let `e` be a rounding error.  Put

```text
c=x+e,                 S_x=q^T x,
|q^T e|<=delta,        ||A^T e||_infinity<=D.         (3.1)
```

### Theorem 3.1 (rounding conservation law)

If the rounded vector is a grid antenna,

```text
A^T c>=-epsilon(q^T c)q_G,                           (3.2)
```

then its fractional centre already satisfies

```text
A^T x>=-epsilon S_x q_G-(D+epsilon delta)q_G.        (3.3)
```

Conversely, the margin

```text
A^T x>=-epsilon S_x q_G+(D+epsilon delta)q_G         (3.4)
```

is sufficient for (3.2).

#### Proof

Subtract `A^T e` from (3.2), use
`q^T c=S_x+q^T e`, and take the two worst signs in (3.1).  The reverse
calculation proves (3.4).  QED

Consequences:

* If `S_x>>(D+epsilon delta)/epsilon`, rounding changes only a lower-order
  part of the normalized antenna.  The centre `x/S_x` is already the needed
  Delsarte object.
* If `x=0`, the carrier is itself a rounding error.  A symmetric theorem
  bounds it on the same scale as every spectral row.  Appending the carrier
  row therefore gives `|S|=O(D)`, whereas (2.8) requires `S>>D` by the factor
  `epsilon^-1=Y^c`.
* Translating the discrepancy body merely chooses a nonzero `x`; (3.3) is
  the exact debt inherited by that translation.

This is why partial coloring is excellent for discretizing a fractional
antenna already known to exist, but does not manufacture the antenna.

---

## 4. The exceptional-carrier tax and conditional signing

For independent unbiased signs, Hoeffding gives

```text
Pr{|sum_j sigma_j|>=L}<=2 exp[-L^2/(2M)].             (4.1)
```

At (2.8), with `G` polynomial,

```text
L/sqrt(M) asymp epsilon^-1 sqrt(log Y),
L^2/M asymp Y^(2c)log Y.                             (4.2)
```

At `c=.019` this is a `Y^.019 sqrt(log Y)` Gaussian deviation and has tail
`exp[-Y^.038 log Y]`.  This does not prove nonexistence--a deterministic
exceptional signing may exist--but it explains exactly why a centred
Gaussian-measure theorem does not supply the affine target.  A translated
body forcing the last normalized Gaussian coordinate beyond the first
quantity in (4.2) has Gaussian measure far below `1/2`, outside the usual
Banaszczyk hypothesis.

There is a sharper identity.  Condition the uniform sign vector on the
attainable value

```text
sum_j sigma_j=S.                                     (4.3)
```

Exchangeability gives, for every legal height `t`,

```text
E[sum_j sigma_j cos(tu_j) | (4.3)]
 =S M^(-1)sum_j cos(tu_j).                           (4.4)
```

Moreover sampling without replacement and Hoeffding's convex-order lemma
give, for every `x>0`,

```text
Pr{|sum_j sigma_j cos(tu_j)
       -S M^(-1)sum_j cos(tu_j)|>=x | (4.3)}
 <=2 exp[-x^2/(8M)].                                 (4.5)
```

Indeed the `+1` locations form a uniform fixed-cardinality subset; apply
Hoeffding to its sum of numbers in `[-1,1]` and use
`sum sigma_j a_j=2 sum_(sigma_j=1)a_j-sum_j a_j`.

A union bound over `G` grid points shows that, conditional on the carrier
(2.8), the normalized signed polynomial is, with high conditional
probability,

```text
M^(-1)sum_j cos(tu_j)+O(epsilon)                     (4.6)
```

on the grid.  Thus the most direct exceptional-carrier signing does not
replace the unknown uniform prime antenna; it reproduces it to precisely the
QP accuracy.  Nonuniform biases replace the right side of (4.6) by the
corresponding fractional antenna, returning to Theorem 3.1.

Again, (4.5) is not a no-exception theorem.  It rules out claiming that
ordinary biased-random-sign concentration itself proves QP.

---

## 5. A signed half-grid barrier

Let

```text
u_j=(2k_j+1)pi/B.                                    (5.1)
```

Then at the legal top height

```text
a(B)=-q.                                             (5.2)
```

### Theorem 5.1 (common half-period defeats all coefficient signs)

For every real coefficient vector with `S=q^T c>0`,

```text
F_c(B)/S=-1.                                         (5.3)
```

If instead

```text
B u'_j=(2k_j+1)pi+eta_j,       |eta_j|<=eta,         (5.4)
```

then

```text
|F'_c(B)/S+1|<=eta^2 ||c||_1/(2S).                  (5.5)
```

#### Proof

Equation (5.3) is (5.2).  For (5.5), use

```text
cos[(2k+1)pi+eta]=-cos eta,
0<=1-cos eta<=eta^2/2,
```

and the triangle inequality.  QED

The prime-density half-grid from the positive-weight audit has cardinality
`Y^(1-o(1))`, physical mesh `O(log Y)`, and the advertised gap moments.  It
may be perturbed by an arbitrarily small amount outside the countable union
of rational-dependence hyperplanes.  Equation (5.5) shows that such a
perturbation still defeats every vector with prescribed normalized TV

```text
||c||_1/S<=L                                         (5.6)
```

provided `eta^2 L=o(1)`.  For the sign normalization (2.8),

```text
L=M/S << epsilon sqrt(M/log Y)=Y^(1/2-c+o(1)),       (5.7)
```

which is polynomial.  An invisible power-small perturbation therefore keeps
the signed obstruction while adding rational independence.

This is a proof-class countermodel, not an actual-prime counterexample.
Unbounded signed coefficients can magnify a fixed perturbation, which is why
the norm qualifier in (5.5)--(5.6) is essential.

---

## 6. Relation to the projected residual

Suppose a balancing algorithm first selects packet constraints and then
chooses a zero-carrier correction.  Its minimum Euclidean correction is the
projected-Gram solve already proved in the companion report.  The directional
source quotient and off-packet residual are unchanged by calling that solve
"vector balancing."

At the other endpoint, if a deterministic balancing theorem directly
returns `c` with (2.5), then `y=c/S` is already the signed Delsarte
certificate.  There is no intermediate implication to prove.  Thus the
genuinely new theorem would have to be one of:

```text
an actual-prime exceptional-carrier signing satisfying (2.4);
a fractional actual-prime antenna with enough margin to survive (3.1);
an actual-prime carrier-residual theorem controlling the adaptive solve.
                                                               (6.1)
```

Generic discrepancy, coefficient rounding, and continuum entropy do not
supply any item in (6.1).

---

## 7. Disposition

```text
symmetric discrepancy / signed-TV polar identity:       PROVED;
norm-sensitive continuum discretization:                 PROVED;
QP sign-grid cardinality polynomial:                      PROVED;
affine rounding conservation law:                         PROVED;
conditional high-carrier mean identity:                   PROVED;
signed bounded-TV half-grid obstruction:                  PROVED;
actual-prime exceptional-carrier signing:                 OPEN;
actual-prime projected residual estimate:                 OPEN;
fixed-power signed or positive QP-KILL:                    NOT PROVED;
QP-PROMOTE or uniform zero-free strip:                     NOT PROVED.
```

Executable replay:

```bash
PYTHONPATH=src python3 src/qp_signed_discrepancy_gate.py
PYTHONPATH=src python3 -m pytest -q src/test_qp_signed_discrepancy_gate.py
```
