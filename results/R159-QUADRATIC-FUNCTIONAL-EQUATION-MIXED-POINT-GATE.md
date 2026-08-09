# R159 quadratic functional-equation mixed-point gate

## Status

R156 leaves one genuinely arithmetic loophole: its cutoff-complete
polynomial countermodel does not have the Euler coefficients of the
quadratic head quotient

```text
F_d(s)=zeta(s)/L(s,chi_d).                                  (0.1)
```

For a positive fundamental discriminant `d`, this quotient has the exact
functional equation

```text
F_d(s)=d^(s-1/2)F_d(1-s).                                  (0.2)
```

This report tests whether (0.2), together with the positive deleted Euler
head, gives a signed invariant for the forced `F_d=2` packet.  It does not.
There are three exact conclusions.

1. On the critical line, `F_d=2` is possible only on a lattice of spacing
   `2 pi/log d`.  Its density in a fixed-height window is nevertheless
   `asymp log d`, exactly the existing conductor ledger.  Off the critical
   line, an `F_d=2` point reflects to a moving value, not to another
   `F_d=2` point.
2. Reflecting the positive `H^q`-supported two-value response splits it
   exactly into the old target-bearing linear logarithmic derivative and a
   conductor-delayed term which is analytic at the target.  The delayed
   channel begins at Dirichlet index `d`, but it has lost the zeta zero.
3. On a localization disc lying strictly to the right of `1/2`, exact
   functional-equation functions can approximate arbitrary holomorphic
   data.  An explicit reflection projection exports the price to an
   `O(log d)` critical-line pole lattice.  Thus the functional equation
   alone cannot exclude the R156 local mixed-point packet.

```text
quadratic quotient functional equation                    EXACT
critical-line F=2 phase lattice                            EXACT
off-line F=2 quartet                                       FALSE
reflected two-value response decomposition                 EXACT
target-bearing delayed reflected channel                   IMPOSSIBLE
reflection-invariant paired mixed factor                   ONLY H-SUPPORT
right-local functional-equation freedom                    THEOREM
functional-equation projection cost                        O(log d)
gamma-factor gain                                          NONE; CANCELS EXACTLY
actual Euler-coefficient mixed-packet correlation          OPEN
fixed uniform zeta zero-free strip                         NOT PROVED
zeros approaching one                                      NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md`](R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md)
and
[`R158-CONDITIONED-MIXED-POINT-FAMILY-AND-SKELETON-GATE.md`](R158-CONDITIONED-MIXED-POINT-FAMILY-AND-SKELETON-GATE.md).

## 1. Exact functional equation and right-half geometry

Let `chi_d` be the primitive even real character of a positive fundamental
discriminant `d`.  The completed functions are

```text
pi^(-s/2) Gamma(s/2) zeta(s),
(d/pi)^(s/2) Gamma(s/2) L(s,chi_d).                         (1.1)
```

Their Gamma factors are identical.  Dividing their functional equations
gives

```text
d^(-s/2)F_d(s)=d^(-(1-s)/2)F_d(1-s),                       (1.2)
```

which is (0.2).  Put

```text
ell=log d,
a(s)=d^(s-1/2)=exp[ell(s-1/2)].                            (1.3)
```

Then

```text
F_d(s)=a(s)F_d(1-s),
a(1-s)=a(s)^(-1).                                          (1.4)
```

The localization geometry in R153--R158 is

```text
z_*=1+r+i gamma,
|s-z_*|<=R,
R<r+eta,
eta<1/2.                                                    (1.5)
```

Consequently every point of the closed localization disc satisfies

```text
Re(s)-1/2 >= 1/2+r-R > 1/2-eta=:epsilon>0.                 (1.6)
```

The disc and its reflection under `s ->1-s` are disjoint.  On the right
disc,

```text
|a(s)^(-1)|<=d^(-epsilon)=exp(-epsilon ell).                (1.7)
```

At the known family scale `ell asymp H`, reflected corrections carrying a
factor `a^(-1)` are exponentially smaller than every fixed negative power
of `H`.  The issue below is that this delayed channel does not retain the
target zero.

## 2. Critical-line phase quantization

Real coefficients give

```text
F_d(conj(s))=conj(F_d(s)).                                  (2.1)
```

At `s=1/2+it`, (1.4) therefore says

```text
F_d(1/2+it)=d^(it)conj(F_d(1/2+it)).                        (2.2)
```

### Theorem 2.1 -- exact critical-line `2`-point lattice

Define

```text
Z_d(t)=exp(-it ell/2)F_d(1/2+it).                          (2.3)
```

Where it is finite, `Z_d(t)` is real.  Moreover,

```text
F_d(1/2+it)=2

iff

t=2 pi n/ell  and  Z_d(t)=2(-1)^n                         (2.4)
```

for some integer `n`.

#### Proof

Equation (2.2) makes (2.3) equal to its complex conjugate.  If `F_d=2`,
then (2.2) gives `d^(it)=1`, hence `t ell in 2 pi Z`.  At such a point,
`exp(-it ell/2)=(-1)^n`, which gives the displayed real value.  The converse
is immediate.  QED.

In a fixed interval of length `T`, the lattice in (2.4) has

```text
O(1+T ell)                                                  (2.5)
```

sites.  When `ell asymp H`, phase quantization therefore reproduces the
`O(H)` completed-divisor scale.  It is not a sparsity theorem, and it gives
no information about which sites satisfy the real scalar condition in
(2.4).

### Corollary 2.2 -- no off-line fixed-value quartet

If `F_d(b)=2`, then

```text
F_d(1-b)=2d^(1/2-b).                                       (2.6)
```

Together with conjugation this produces moving values at `1-b` and
`1-conj(b)`, not additional `F_d=2` points.  Only on the critical-line
lattice (2.4) does the moving value return to `2`.

Thus zero quartets do not become mixed-`2`-point quartets.  In particular,
the functional equation does not constrain the off-line `F_d=2` points
which can cancel a target reciprocal-power jet.

## 3. The linear logarithmic derivative under reflection

Set

```text
A_d(s)=-F_d'(s)/F_d(s).                                    (3.1)
```

Logarithmically differentiating (1.4) gives

```text
A_d(s)+A_d(1-s)=-ell.                                      (3.2)
```

For every `k>=1`, differentiating again gives

```text
A_d^(k)(s)+(-1)^k A_d^(k)(1-s)=0.                          (3.3)
```

Thus a reflected high-jet evaluation is algebraically dependent on the
original evaluation.  It is not an independent upper bound.

In `Re(s)>1`, write

```text
F_d=1+U_d.                                                  (3.4)
```

If `chi_d(p)=1` for every `p<=H`, then `U_d` has nonnegative Dirichlet
coefficients and support beyond `H`.  Hence `A_d` has the corresponding
positive deleted Euler head.  Equation (3.3) shows that reflection preserves
this linear detector; it does not amplify its support.

## 4. Exact reflected two-value response

For an integer `q>=1`, define

```text
C_q(s)=-2 U_d(s)^(q-1)U_d'(s)/[1-U_d(s)^2].                (4.1)
```

In the right half-plane of absolute convergence,

```text
C_q=2[-U_d']U_d^(q-1)sum_(j>=0)U_d^(2j),                  (4.2)
```

so its Dirichlet coefficients are nonnegative and its support begins beyond
`H^q`.  Its only displayed finite value poles are `F_d=0` and `F_d=2`.
The residue at `F_d=2` is `+1`; the target residue is `+1` for even `q` and
`-1` for odd `q`.

The following identity is the coefficient-specific reflection gate.

### Theorem 4.1 -- target/reflected-delay conservation

Put

```text
v(s)=F_d(1-s)=a(s)^(-1)F_d(s),
K_q(v)=2(v-1)^(q-1)/(2-v).                                 (4.3)
```

Then, wherever both sides are finite,

```text
C_q(1-s)=K_q(v(s))[F_d'(s)/F_d(s)-ell].                    (4.4)
```

Since `K_q(0)=(-1)^(q-1)`, this has the exact decomposition

```text
C_q(1-s)
 =(-1)^(q-1)[F_d'/F_d-ell]
  +v H_q(v)[F_d'/F_d-ell],                                 (4.5)

H_q(v)=[K_q(v)-K_q(0)]/v.                                  (4.6)
```

The function `H_q` is holomorphic at zero.  Its only displayed finite pole
comes from `v=2`.

#### Proof

At `t=1-s`, write

```text
F_d(t)=v,
U_d(t)=v-1.                                                 (4.7)
```

Because `dt/ds=-1`,

```text
d v/dt=-d v/ds.
```

Also

```text
v'(s)/v(s)=F_d'(s)/F_d(s)-ell.                             (4.8)
```

Substitution into (4.1) gives

```text
C_q(1-s)
 =2(v-1)^(q-1)v'(s)/[v(2-v)]
 =K_q(v)[F_d'/F_d-ell],                                    (4.9)
```

which proves (4.4).  Subtracting the value of `K_q` at zero proves
(4.5)--(4.6).  QED.

### 4.1 Divisor meaning

The first term in (4.5) contains the full target pole.  For `k>=1`, its
`k`th derivative is just a signed derivative of `F_d'/F_d`; the constant
`ell` disappears.  Its Euler support is therefore only the original support
beyond `H`.

The second term is analytic at every zero of `F_d`.  Indeed, if `F_d` has a
zero of order `m`, then

```text
v F_d'/F_d=O((s-rho)^(m-1)).                               (4.10)
```

Thus the factor `v` cancels the target logarithmic pole.  Its value pole
`v=2` is

```text
F_d(s)=2a(s),                                               (4.11)
```

the reflection of an `F_d=2` point, not the local mixed value itself.

### 4.2 Dirichlet-support meaning

In `Re(s)>1`, if

```text
F_d(s)=sum_n f_d(n)n^(-s),       f_d(1)=1,                 (4.12)
```

then

```text
v(s)=sqrt(d) sum_n f_d(n)(dn)^(-s).                        (4.13)
```

Every term in the second line of (4.5), expanded at `v=0`, therefore has
Dirichlet support at an integer at least `d`.  At `log d asymp H`, this is
an exponentially delayed channel.  Equation (4.10) shows exactly why that
gain is unavailable: the delayed channel has no target divisor.

### Corollary 4.2 -- reflection cannot amplify a retained target

Any fixed nonzero use of the target-bearing first term in (4.5) restores
the `H`-supported linear logarithmic derivative.  Subtracting that first
term isolates a response supported beyond `d`, but cancels the target pole
identically.

Consequently the functional equation does not turn the `H^q` response into
a target-bearing conductor-delayed response.  It splits target retention
and conductor delay into complementary terms.

## 5. Reflection-invariant value factors

The same obstruction appears without differentiating (4.1).

### 5.1 The paired mixed-value factor

The fixed value `F_d=2` and its reflected moving value are packaged by

```text
M_2(s)=a(s)^(-1)[F_d(s)-2][F_d(s)-2a(s)].                  (5.1)
```

A direct substitution gives

```text
M_2(1-s)=M_2(s).                                           (5.2)
```

Its logarithmic derivative is

```text
M_2'/M_2
 =-ell+F_d'/(F_d-2)+(F_d'-2ell a)/(F_d-2a).                (5.3)
```

On the right localization disc, whenever the displayed denominators stay
separated,

```text
(F_d'-2ell a)/(F_d-2a)
 =ell+O[a^(-1)(ell|F_d|+|F_d'|)].                          (5.4)
```

Therefore

```text
M_2'/M_2
 =F_d'/(F_d-2)+O[a^(-1)(ell|F_d|+|F_d'|)]
 =[-U_d']/(1-U_d)+O(a^(-1)...) .                           (5.5)
```

The principal right-hand response in (5.5) has nonnegative coefficients,
but begins beyond only `H`.  Reflection completion has removed neither its
linear head nor its mixed divisor.

### 5.2 The paired target factor

The simplest reflection-invariant target factor is

```text
M_0(s)=a(s)^(-1)F_d(s)^2,                                  (5.6)
```

for which

```text
M_0(1-s)=M_0(s),
M_0'/M_0=2F_d'/F_d-ell.                                    (5.7)
```

Pairing the target zero therefore starts with the linear logarithmic
derivative.  Cancelling its Taylor terms about `F_d=1` requires the same
additional value divisors or exact polynomial-at-infinity germ audited in
R153--R156.  Functional symmetry does not change that conservation law.

## 6. Exact functional-equation projection

The preceding identities close the natural reflected responses.  There is
also a local approximation theorem showing why no invariant can follow from
the functional equation alone.

Let

```text
(T_ell f)(s)=a(s)f(1-s).                                   (6.1)
```

Then `T_ell^2=1`, and the functional equation is `T_ell F=F`.

For an integer `J>=2`, define

```text
P_(ell,J)f(s)
 =[a(s)^J f(s)+a(s)f(1-s)]/[1+a(s)^J].                    (6.2)
```

### Theorem 6.1 -- right-local functional-equation freedom

The function in (6.2) satisfies

```text
P_(ell,J)f(s)=a(s)P_(ell,J)f(1-s)                          (6.3)
```

identically.  On a compact set `K` contained in
`Re(s)>=1/2+epsilon`,

```text
|P_(ell,J)f(s)-f(s)|
 <=2[|a(s)|^(1-J)|f(1-s)|+|a(s)|^(-J)|f(s)|]               (6.4)
```

for all sufficiently large `ell`.  Its possible projection poles lie on
the exact critical-line lattice

```text
Re(s)=1/2,
Im(s)=(2n+1)pi/(J ell).                                    (6.5)
```

#### Proof

At `1-s`, replace `a` by `a^(-1)` in (6.2) and multiply numerator and
denominator by `a^J`.  Multiplication by `a` gives exactly (6.2), proving
(6.3).  Subtracting `f(s)` gives

```text
P_(ell,J)f(s)-f(s)
 =[a(s)f(1-s)-f(s)]/[1+a(s)^J].                            (6.6)
```

On `K`, `|a|>=exp(epsilon ell)`, so
`|1+a^J|>=|a|^J/2` for large `ell`, which proves (6.4).
Finally, the new denominator vanishes exactly when

```text
exp[J ell(s-1/2)]=-1,
```

which is (6.5).  QED.

In a fixed-height interval the lattice (6.5) has `Theta(J ell)` points, and
for a generic seed these denominator zeros are genuine poles.  Thus this
explicit way of enforcing reflection carries a conductor-scale `ell` bill.
The lattice lies outside the right localization disc by (1.6).

### 6.1 Embedding arbitrary right-local packets

Let `K` be a closed right localization disc and let `K^*=1-K`.  They are
disjoint by (1.6).  Runge approximation with finite Hermite interpolation
allows a seed `f` to approximate arbitrary holomorphic data on `K`, while
being arbitrarily small on `K^*`.  Including the conjugate discs and
symmetrizing the seed preserves real coefficients.

The finite interpolation constraints can retain designated divisors
exactly.  For example:

```text
f(rho)=f(1-rho)=0                                          (6.7)
```

makes `P_(ell,J)f(rho)=0`, while, for a prescribed mixed point `b`,

```text
f(b)=2,
f(1-b)=2/a(b)                                              (6.8)
```

makes `P_(ell,J)f(b)=2`.  Uniform approximation on the boundaries of
small divisor discs and Rouché's theorem preserve the remaining local zero
and mixed-point counts.

Applying this to the R156 polynomial packet produces an exact
functional-equation model with the same right-local target/mixed
cancellation.  The reflection price is exported to the critical-line
lattice (6.5) and to the reflected half-plane.

This projection model is deliberately not claimed to be a quadratic Euler
quotient.  It proves the precise logical statement needed here: functional
symmetry, real symmetry, phase quantization, and quartet pairing do not by
themselves distinguish the actual quotient from the R156 local
countermodel.

## 7. Right-half localization versus the left-half bill

The audit separates the two halves cleanly.

### 7.1 Right half

On the full target disc, `|a^(-1)|<=exp(-epsilon ell)`.  Every genuinely
reflected correction in the second line of (4.5) is therefore delayed to
Dirichlet index at least `d`.  If it is isolated, however, it is target-free.
Every reflected expression which retains the target also retains the first
line of (4.5), and hence the ordinary `H`-supported logarithmic derivative.

### 7.2 Critical line and left half

On `Re(s)=1/2`, `|a|=1`; the exponential right-half gain vanishes.  It is
replaced by the phase lattice (2.4), or by the projection pole lattice
(6.5), both of density `asymp ell`.  Beyond the line, the functional
equation supplies the reflected values exactly, but no independent estimate
for them.

For ordinary derivatives, write `D=d/ds`.  Equation (1.4) gives

```text
(-1)^k F_d^(k)(1-s)
 =a(s)^(-1)(D-ell)^k F_d(s).                               (7.1)
```

The powers of `ell` in (7.1) are the ordinary-derivative form of the
conductor bill.  Logarithmic differentiation compresses them to the constant
in (3.2), but then the target-bearing part is exactly the old linear
detector.

### 7.3 Gamma terms

There is no unaccounted gamma saving in this quadratic quotient.  The two
Gamma factors in (1.1) cancel before (1.2) is formed.  At fixed target
height, separately reintroducing the completed factors only restores terms
which have already canceled.  The scale in this gate is `ell=log d`, not a
missing archimedean contribution.

## 8. Consequence and surviving target

The exact functional equation supplies useful location information, but it
does not sign the local mixed packet.

```text
critical-line phase information
    -> O(log d) possible sites, no off-line confinement;

reflection of the H^q response
    -> target-bearing H-supported term
       + target-free d-supported term;

reflection-invariant value product
    -> unamplified H-supported logarithmic derivative;

symmetric right/left contour
    -> critical-line or conductor-scale bill.              (8.1)
```

In particular, the functional equation cannot defeat the R156 polynomial
countermodel by pairing `F_d=2` points, by critical-line phase quantization,
or by a scalar reflection-symmetric response.

What remains open is narrower and genuinely coefficient-specific: prove a
target-conditioned correlation theorem for the actual quadratic-character
Euler coefficients and the off-line divisor of

```text
zeta(s)-2L(s,chi_d).                                       (8.2)
```

Such a theorem would have to use more than the functional equation and the
coarse `O(log d)` divisor ledger.  No result here proves a fixed zero-free
strip or proves that zeros approach one.
