# QP sector combination: sharp dominance gains and the balanced-cross remainder

**Date:** 2026-08-15  
**Verdict:** the central-packet and one-sided Burgess theorems do not cover
every full-shell dual direction.  They combine into a quantitative
dominance classification, and at the active aperture every power-dominant
direction improves the `49/66` exponent.  A nonempty residual sector remains: vectors with two
power-comparable components, in particular balanced upper/lower far-tail
vectors.

The exact arithmetic tensor left in that sector is

```text
K_cross(a,b,c)=hat psi(B log(abc/Y^3)),             (0.1)
a,b>Y+H,                   c<Y-H.
```

It is supported on

```text
|8abc-q^3|<<q^3/B=qR,       q=2Y, R=q^(2-A+o(1)), (0.2)
```

and, for fixed `c`, confines `ab` only to a window of length `O(R)`.
The currently proved coefficient-uniform norm is therefore `O(sqrt(R))`,
exactly the old cubic scale.  The prime-modulus Burgess argument does not
apply: the residual interval in (0.2) spans `asymp R` complete residue
systems modulo `q`, rather than one short interval.

Thus no exponent below `49/66` for the unrestricted full shell follows
from sector combination alone.  This report does not assert that (0.1)
saturates `sqrt(R)` on actual prime powers; it identifies the exact
uncontrolled rank-one tensor.  No QP, QP equivalence, or strip is proved.

---

## 1. Three-component decomposition

Let `q` be an odd prime, `Y=q/2`, `B=Y^A`, and use a fixed shell width
`w<log 2`.  Put

```text
h=2-A,                  R=q^(h+o(1)),
kappa=h/4+3/32.                                      (1.1)
```

At the active aperture `A=50/33`,

```text
h=16/33,       h/2=8/33,       kappa=227/1056.     (1.2)
```

Fix

```text
H=q^alpha,                 alpha<=1/2-epsilon,      (1.3)
```

and split a full-shell coefficient vector and its centered time function as

```text
y=y_C+y_++y_-,             Z=Z_C+Z_++Z_-.          (1.4)
```

Here `C` is `|n-Y|<=H`, while `+` and `-` are the upper and lower far
tails.  Define the component standard deviations

```text
sigma_C=||Z_C||_(L2(rho_B)),
sigma_+=||Z_+||_(L2(rho_B)),
sigma_-=||Z_-||_(L2(rho_B)).                        (1.5)
```

The central divided-difference frame and one-sided separated frames give

```text
point-evaluation cost on C:       q^(alpha/2+o(1)) sigma_C,
point-evaluation cost on either tail:
                                  q^(1/2+o(1)) sigma_+/- .  (1.6)
```

The proved pure cubic constants are

```text
K_C=o(1),                  K_+=K_-=q^(kappa+o(1)). (1.7)
```

Polarizing the proved full-shell clustered cubic estimate gives, for any
three component inputs,

```text
|T(Z_i,Z_j,Z_k)|
 <=q^(h/2+o(1)) sigma_i sigma_j sigma_k.            (1.8)
```

Equation (1.8) is the only input used on mixed component triples.

## 2. General dominance lemma

For `j` in `{C,+,-}`, let

```text
delta_j=(sum_(i!=j)sigma_i)/sigma_j.                (2.1)
```

Assume `delta_j<=1/2`.  The reverse triangle inequality gives

```text
||Z||_2>=(1-delta_j)sigma_j.                        (2.2)
```

Expanding the centered cubic, using the pure estimate for `j`, and using
(1.8) on every term containing another component gives

```text
|E Z^3|/||Z||_2^3
 <=C {K_j+q^(h/2+o(1))delta_j}.                    (2.3)
```

The point-evaluation or calibrated leverage is at most

```text
C {sqrt(M_j)+delta_j sqrt(M_max)}sigma_j,
M_max<=q^(1+o(1)).                                  (2.4)
```

The smooth means of all three components are smaller than any prescribed
fixed power after choosing the fixed Fourier-decay order, and under
`delta_j<=1/2` they are negligible relative to the right side of (2.2).
The cubic endpoint inequality and (2.2)--(2.4) therefore give the
directional support ratio

```text
h_Y(y)/[-y dot v]_+
 >>1/{[sqrt(M_j)+delta_j sqrt(M_max)]
       [1+K_j+q^(h/2+o(1))delta_j]}.                (2.5)
```

This is the sharp combination statement furnished by the current inputs.
It becomes a transverse lower bound only for a ray whose every separating
dual lies in the stated sector.  A support-function infimum over all duals
cannot discard the residual sector below.

## 3. Side-dominant classification

Suppose one far side is dominant with

```text
delta_+<=q^(-theta+o(1))                            (3.1)
```

or the analogous lower-side condition, where `theta>0` is fixed.  Since
the dominant tail already has dimension `q^(1+o(1))`, (2.5) has exponent

```text
e_side(theta)
 =1/2+max(kappa,h/2-theta).                         (3.2)
```

At `A=50/33`, this is

```text
e_side(theta)
 =49/66-min(theta,29/1056).                         (3.3)
```

Thus every fixed-power side imbalance improves `49/66`.  Once

```text
theta>=h/2-kappa=29/1056,                           (3.4)
```

one recovers the full one-sided Burgess exponent `755/1056`.  Squaring
the amplitude ratio in (3.4) gives the previously proved minority-energy
threshold `q^(-29/528+o(1))`.

For density-one prime centers, replace `kappa` by

```text
kappa_dens=h/4+1/16=97/528.                         (3.5)
```

The plateau is then `361/528`, reached at amplitude imbalance
`theta>=31/528`, equivalently minority energy `q^(-31/264+o(1))`.

## 4. Central-dominant classification

Suppose instead

```text
delta_C<=q^(-theta+o(1)).                           (4.1)
```

The central point-evaluation dimension and the far-tail leverage must both
be retained.  Equations (1.6), (1.7), and (2.5) give

```text
e_C(theta)
 =max(alpha/2,1/2-theta)+max(0,h/2-theta).          (4.2)
```

For the maximal packet `alpha=1/2-epsilon` at the active aperture,

```text
e_C(theta)=
  49/66-2theta,                0<theta<=8/33;
  1/2-theta,                   8/33<=theta<=1/4+epsilon/2;
  1/4-epsilon/2,               theta>=1/4+epsilon/2. (4.3)
```

The last line is exactly the central restricted depth
`M_C^(-1/2)` at the exponent level.  The extra condition on `theta` is not
cosmetic: a tiny far-tail coefficient vector can still cost
`sqrt(M_tail)` in the calibrated point evaluation.

Again every fixed `theta>0` improves `49/66`, but constant-factor central
dominance alone does not: the mixed term in (2.3) then remains at
`q^(h/2)`.

## 5. Exact residual sector

Fix any `theta>0`.  If no component satisfies

```text
delta_j<=q^(-theta),                               (5.1)
```

then the second-largest component standard deviation is at least a fixed
multiple of `q^(-theta)` times the largest.  At least two components are
therefore power-comparable.  This residual sector is nonempty.  The
simplest subfamily is

```text
sigma_C=0,                  sigma_+=sigma_->0.      (5.2)
```

Changing `H` within the parity range cannot remove (5.2): its coefficients
may be supported in fixed multiplicative cells a positive distance from
`Y`.

To see the surviving arithmetic, use the exact identity

```text
F_y(t)=Re P_y(t),
P_y(t)=Y^(-it)sum_n y_n n^(it).                    (5.3)
```

For two upper nodes `a,b` and one lower node `c`, the `P_y^3` expansion
contains

```text
hat psi(B log(abc/Y^3)) y_a y_b y_c.               (5.4)
```

This term is Schwartz-negligible on a pure side and parity-separated when
all three nodes lie in the central packet.  Neither mechanism applies to
the balanced far-tail assignment.  Its near-resonance condition is (0.2).

For fixed `c`, (0.2) puts the product `ab` in an integer interval of length
`O(R)`.  Bounded prime-power product multiplicity and Schur's test give

```text
||K_cross||<=C_w sqrt(R)=q^(h/2+o(1)).             (5.5)
```

Unlike `|2ab-qc|<=R`, reducing (0.2) modulo `q` does not produce a short
residual character sum: its residual length is `qR>q`.  A saving in (5.5)
would require a new rank-one triple-product estimate, a higher-modulus
character argument retaining all three arbitrary coefficient slots, or a
calibration-sensitive leverage--skew theorem.  None is presently proved.

## 6. Why component support bounds cannot be glued abstractly

There is also an exact abstract obstruction to any argument using only the
three separate positive-range theorems.  On a probability space take the
symmetric two-point variable `X in {-1,1}` and set

```text
Z_+=X,                       Z_-=-X.                (6.1)
```

Each component separately has the same variance and a valid cubic endpoint
bound, while `Z_++Z_-=0`.  Thus lower bounds for `sup Z_+` and `sup Z_-`
cannot be added: their favorable points need not coincide, and cross
covariance can cancel them.  The actual clustered frame prevents replacing
this model by an exact equality without paying divided-difference energy,
but it does not eliminate the mixed cubic tensor (5.4).

This abstract example is not asserted to be an actual-prime extremizer.  It
proves only that component theorems, without a mixed estimate, cannot imply
a full-shell support theorem.

## 7. Disposition

```text
every fixed-power pure-sector direction improves 49/66
at A=50/33:                                           PROVED;
side-dominant exponent formula (3.2):                  PROVED;
central-dominant exponent formula (4.2):               PROVED;
all full-shell vectors enter a pure sector:             FALSE;
balanced far-tail triple-product tensor (5.4):          REMAINS;
power saving for (5.5) on actual prime powers:           OPEN;
unrestricted full-shell exponent below 49/66:            NOT PROVED;
QP, QP equivalence, or uniform strip:                    NOT PROVED.
```

The rational exponent ledger is replayed in

```text
src/qp_sector_combination_gate.py
src/test_qp_sector_combination_gate.py
```

with current result `5 passed`.
