# Tailored discrete Pick problem: separated representatives and the jet obstruction

Status: exact positive theorem for separated representatives, exact five-row
confluent Pick obstruction, and a general finite high-jet obstruction,
2026-08-12.  The unrestricted half-line problem is settled only in these
scopes.  Multiplication of the local obstruction across `Theta(L)` cells and
compact Paley--Wiener realization remain open.  No zero-free strip is proved.

## 1. Binary verdict

There are two different statements which had been conflated.

1. If an occupied phase cell is represented by just one node, the half-disk
   Pick problem has an exact one-product solution.  There is no hidden extra
   Pick exponent in the separated-representative problem.
2. One arbitrary cluster cannot always be replaced by one analytic degree.
   Five rows in one shrinking phase cell can force an approximate *double*
   zero.  Their exact Pick optimum is at most the square of the
   one-representative Blaschke attenuation, up to `O(1/L)`.

Thus the phrase "one condition per occupied phase cell" is false for
arbitrary analytic node configurations.  It could still be true for actual
zeta clusters because of arithmetic restrictions on their scaled depths, or
after a genuinely global construction which couples different cells.  Neither
fact follows from Riemann--von Mangoldt and Bellotti--Wong counts alone.

The five-row obstruction does **not** by itself destroy the current carrier
margin.  A theorem multiplying such local losses across a growing list is
still missing.  This is the first remaining global quantifier.

## 2. Exact positive result for separated representatives

Let `z_1,...,z_M` be distinct right-half-plane representatives and put

```text
b_z(s)=(s-z)/(s+conj(z)),

B(s)=exp(-i*arg(product_j b_(z_j)(alpha)))
     *product_j b_(z_j)(s).                         (2.1)
```

Then `B` is Schur, `B(alpha)>0`, and

```text
B(z_j)=0,

B(alpha)=product_j
 |(alpha-z_j)/(alpha+conj(z_j))|.                  (2.2)
```

Zero belongs to every favorable half-disk

```text
C_j={w: |w|<=1, Re[exp(-i*D*delta_j)w]>=0}.        (2.3)
```

Consequently (2.1) is feasible for the exact half-disk Pick matrix and has
precisely the one-product target value.  Moreover, among Schur functions
subject to the stronger equations `U(z_j)=0`, this value is maximal: division
by the inner product in (2.1), followed by the maximum-modulus principle,
gives

```text
|U(alpha)|<=|B(alpha)|.                            (2.4)
```

This is valid for every finite list, with no separation assumption actually
needed.  Identical nodes are grouped as one value condition; they are not
silently charged as higher-order confluent conditions.  In the exact-zero
architecture, the already-proved balanced bipartite coloring theorem for the
two endpoint legs then restores the one-product same-state carrier bill.
That last statement concerns factor allocation after exact annihilation; it
does not supply the missing compact realization or a global multiplication
theorem for the approximate jet obstructions below.

Equation (2.2) proves that no dual certificate can impose an extra exponent
on a list containing only one effective row per occupied cell.  Any extra
Pick loss must use residual rows in at least one cell.  Compact support is a
separate restriction and is not asserted here.

## 3. The equal-depth center-zero lemma and its limit

Write a phase cell in scaled coordinates as

```text
D*delta=(2m+1)*pi+x,       -pi<=x<=pi.             (3.1)
```

At a common real depth, put one simple zero at the cell center.  After the
harmless phase normalization, the leading local response is

```text
x*sin(x)>=0,       -pi<=x<=pi.                     (3.2)
```

This explains why a centered simple factor groups an equal-depth cell.  A
scaled depth displacement contributes a `lambda*cos(x)` term, which changes
sign between the center and the cell boundary.  The following theorem shows
that this is not merely a defect of the centered choice: arbitrary motion of
one zero and an arbitrary background phase cannot handle every varying-depth
cluster.

## 4. An exact five-row positive dual

Fix

```text
d=2/3,       D=d*L,       alpha>0.                 (4.1)
```

Choose an integer `m_L`, set

```text
delta_c=(2*m_L+1)*pi/D,
z_c=alpha-i*delta_c,                               (4.2)
```

and take five nodes

```text
z_j=alpha-lambda_j/L
    -i*(delta_c+x_j/D),                            (4.3)

(x_1,...,x_5)=(-pi,-pi/2,0,pi/2,pi),
(lambda_1,...,lambda_5)=(1,1,1,1,8).              (4.4)
```

All five nodes lie in one closed phase cell and have real part below
`alpha`.  The two boundary phases may be moved a sufficiently small fixed
amount into the cell; every conclusion below persists by continuity.

Since

```text
D*delta_j=(2*m_L+1)*pi+x_j,                        (4.5)
```

the original favorable inequalities become, after writing `V=-U`,

```text
Re[exp(-i*x_j)*V(z_j)]>=0.                         (4.6)
```

Put

```text
h_j=-lambda_j-i*x_j/d,
z_j=z_c+h_j/L.                                    (4.7)
```

For a complex affine jet `P+C*h`, the left side of (4.6) is

```text
f_j=Re[exp(-i*x_j)*(P+C*h_j)]
   =n_j dot (Re P, Im P, Re C, Im C),              (4.8)
```

where

```text
n_j=( cos(x_j),
      sin(x_j),
     -lambda_j*cos(x_j)-(x_j/d)*sin(x_j),
      (x_j/d)*cos(x_j)-lambda_j*sin(x_j) ).        (4.9)
```

These five normals have the exact positive dependence

```text
sum_j w_j*n_j=0,

(w_1,...,w_5)
 =(1,14/(3*pi),2,14/(3*pi),1),                    (4.10)
```

and the determinant of the first four rows is

```text
det(n_1,n_2,n_3,n_4)=9*pi^2/4.                    (4.11)
```

Therefore

```text
f_j>=0 for every j     implies     P=C=0.          (4.12)
```

This is the desired local Pick dual certificate.  It is exact algebra, not a
numerical observation.

There cannot be an analogous obstruction with at most four rows at the
affine-jet level.  Four homogeneous half-spaces in `R^4` always have a
nonzero common point: if their normals have rank below four, take a common
orthogonal vector; if they have full rank, solve `n_j dot X=1`.  Thus five is
the sharp first cardinality for a one-analytic-degree obstruction.

## 5. Exact Schur consequence: a second Blaschke factor

Assume that `delta_c` remains in a fixed bounded ordinate interval and let
`U_L` be any right-half-plane Schur function satisfying (4.6).  Taylor's
formula at `z_c` gives

```text
V(z_j)=V(z_c)+V'(z_c)*h_j/L+O_alpha(L^(-2)).       (5.1)
```

The remainder is uniform because a fixed disk about `z_c` remains in the
right half-plane and every Schur function is bounded there.  Apply the
positive relation (4.10) and the invertibility (4.11) to the five inequalities
with their `O(L^-2)` errors.  One obtains

```text
V(z_c)=O_alpha(L^(-2)),
V'(z_c)=O_alpha(L^(-1)).                           (5.2)
```

Here is a direct two-step Schur proof of the target loss.  Define

```text
b_c(s)=(s-z_c)/(s+conj(z_c)),
rho_c=|b_c(alpha)|
     =|delta_c|/sqrt(4*alpha^2+delta_c^2).         (5.3)
```

First remove the value `a=V(z_c)` by a disk automorphism and divide by
`b_c`.  The result is Schur and its value at `z_c` is

```text
2*alpha*V'(z_c)/(1-|a|^2)=O_alpha(L^(-1)).         (5.4)
```

Remove this second small value and divide once more by `b_c`.  Schwarz--Pick
at `alpha` then gives

```text
|U_L(alpha)|=|V(alpha)|
 <=rho_c^2+O_alpha(L^(-1)).                        (5.5)
```

If `delta_c` tends to a fixed nonzero `delta_0`, then `rho_c` tends to a
constant strictly between zero and one.  Every one of the five possible
representative nodes has one-factor attenuation

```text
|b_(z_j)(alpha)|=rho_c+O_alpha(L^(-1)).            (5.6)
```

Thus the exact half-disk Pick optimum for this cluster pays at least a second
fixed Blaschke attenuation.  Prescribing one exact zero per cell is not a
valid universal compression rule.

## 6. Arbitrarily high local jet obstructions

The five-row fixture is the first member of a general convex-geometric
phenomenon.  For fixed `r>=0`, let

```text
h(lambda,x)=-lambda-i*x/d                         (6.1)
```

and associate to `(lambda,x)` the real normal in `R^(2*r+2)` for the
functional

```text
(C_0,...,C_r)
  -> Re[exp(-i*x)*sum_(k=0)^r C_k*h(lambda,x)^k].  (6.2)
```

### Lemma 6.1 (finite positive spanning fixture)

For every fixed `r`, there is a finite set of points with

```text
lambda_j>0,       -pi<x_j<pi,                      (6.3)
```

whose normals in (6.2) positively span `R^(2*r+2)`.  The set may be chosen
with at most

```text
4*r+4                                                (6.4)
```

points.

#### Proof

If all normals lay in one closed half-space through zero, there would be a
nonzero polynomial `P` of degree at most `r` such that

```text
Re[exp(-i*x)*P(-lambda-i*x/d)]>=0                  (6.5)
```

for every `lambda>0` and `-pi<x<pi`.  If `a_m` is the leading nonzero
coefficient, division by `lambda^m` and passage to infinity would give

```text
Re[(-1)^m*a_m*exp(-i*x)]>=0                        (6.6)
```

through a full `2*pi` range of `x`, which is impossible.  For each coefficient
vector on the unit sphere there is therefore a normal having strictly
negative pairing with it.  Those strict-negative sets form an open cover of
the compact unit sphere, so a finite subcover exists.  The corresponding
finite normals have trivial polar cone and hence positively span the whole
space by finite-dimensional separation.  Extracting a minimal positive basis
leaves at most `2*N` members; here `N=2*r+2`, proving (6.4).  All normals used
already have parameters in the strict ranges (6.3).  QED

The sharper minimal-size guess is `2*r+3`.  It is exact for `r=1` by Section
4 and small numerical probes find such simplices for `r=2,3,4,5`; no proof
for every `r` is claimed here.

Apply a fixed fixture from Lemma 6.1 in one shrinking phase cell.  Taylor
expansion through order `r`, positive spanning, and a uniform Cauchy
remainder imply

```text
U_L^(k)(z_c)=O_(alpha,r)(L^(k-r-1)),
0<=k<=r.                                           (6.7)
```

Indeed, with `V=-U` put

```text
Y_(k,L)=V^(k)(z_c)/(k!*L^k).
```

The finite positive-spanning fixture has a constant `kappa_r>0` such that
some row pairs with every nonzero real jet vector `Y` by at most
`-kappa_r*||Y||`.  Each favorable inequality, while the Taylor remainder is
`O_(alpha,r)(L^(-r-1))`, therefore forces
`||Y||=O_(alpha,r)(L^(-r-1))`, which is exactly (6.7).

Iterating the Schur step in Section 5 `r+1` times gives

```text
|U_L(alpha)|
 <=rho_c^(r+1)+O_(alpha,r)(L^(-1)).                (6.8)
```

More explicitly, the successive Schur parameters at `z_c` are
`O(L^(-r-1)),O(L^(-r)),...,O(L^(-1))`; undoing the disk automorphisms at
`alpha` contributes one factor of modulus `rho_c` at each step and a total
`O(L^(-1))` error.

Thus arbitrary zero-count-compatible clusters can require arbitrarily high
local analytic order.  The constants in (6.7)--(6.8) depend on the fixed
fixture and on `r`; no assertion uniform in growing `r` is made.

## 7. Conditional repetition ledger

The local theorem does not automatically multiply over nearby cells.
Nevertheless it is useful to record exactly what a hypothetical global
factor-count theorem would cost.

Suppose every occupied cell contains `m` actual pair rows and a global
construction pays `c` effective Blaschke factors for that cell.  With

```text
p=1/(4*pi),       q=d/(2*pi),       a=0.10076,     (7.1)
```

the Riemann--von Mangoldt plus Bellotti--Wong envelope becomes

```text
p_eff=(c/m)*p,
a_eff=(c/m)*a,
q_eff=c*q.                                         (7.2)
```

For the even decreasing target potential

```text
V_alpha(delta)=(1/2)*log(1+(2*alpha/delta)^2),     (7.3)
```

the same rearrangement calculation as in the one-product report gives

```text
h_m=a/[2*(m*q-p)],                                 (7.4)

I_alpha(h)=integral_(-h)^h V_alpha(delta)d delta
 =h*log(1+(2*alpha/h)^2)
  +4*alpha*atan(h/(2*alpha)),                      (7.5)

C_(m,c)
 =2*pi*alpha*p_eff+(q_eff-p_eff)*I_alpha(h_m).     (7.6)
```

This is a **conditional ledger**, not a theorem that local Pick losses
multiply.

At

```text
alpha=1/2,       d=2/3,       a=0.10076,           (7.7)
```

some representative residual carrier exponents are

```text
(m,c)       alpha*d-C_(m,c)
(1,1)        0.013383432
(3,2)       -0.005503578
(5,2)        0.104609999
(5,3)       -0.009751668
(10,5)       0.008330719
(12,6)      -0.001523735.                          (7.8)
```

Therefore even a hypothetical global rule `c=ceil(m/2)` would not close the
present constants; it already loses for some small odd multiplicities.  The
complex jet dimension must be stated more carefully.  Forcing `c` complex
Taylor coefficients to vanish means positively spanning `R^(2*c)`, which
requires at least `2*c+1` scalar half-space rows.  Thus the dimension ceiling
is

```text
c<=floor((m-1)/2),                                  (7.9)
```

not `floor(m/2)` when `m` is even.  In particular `(m,c)=(12,6)` is a useful
cost diagnostic in (7.8), but it cannot be forced by twelve rows at the jet
level; the dimension-compatible entry `(12,5)` has residual exponent
`0.054285776...`.

The proven high-jet lemma still shows that this is not merely a small-`m`
issue.  Put `c=r+1`.  Its fixture uses some `M<=4*c` rows and may be padded by
additional distinct rows to `m=4*c` without weakening positive spanning.
In the conditional ledger (7.6),

```text
C_(4*c,c)=alpha/8+(a/4)*log(c)+O_(alpha,d,a)(1),   (7.10)
```

so the residual exponent is negative for all sufficiently large fixed `c`.
With the rounded constants (7.7), direct evaluation first becomes negative
at `c=2040`, `m=8160`.  This remains only a conditional repetition ledger:
Lemma 6.1 supplies one fixed local fixture, while no theorem here multiplies
its attenuation over `Theta(L)` cells.

Known zero counts permit, but do not force, repeated fixed-multiplicity
fixtures: `m*K` rows in `K` occupied cells can be placed under both the row
envelope and the phase-cell occupancy cap.  They do not supply the missing
analytic statement that the local attenuations in (6.8) multiply.  Conversely,
they give no anti-confluence theorem excluding the high-depth patterns of
Section 6.

The needed next result is consequently more specific than a generic
factor-two interpolation theorem.  One must prove at least one of:

1. an actual-zeta restriction which forbids positive-spanning depth/phase
   fixtures in the dangerous cells;
2. a global Schur theorem whose cross-cell coupling beats the local
   multiplicity ledger in (7.6); or
3. a compact two-leg construction using structure outside scalar inner
   interpolation.

Riemann--von Mangoldt, Bellotti--Wong, and Huxley bounds by themselves prove
none of these alternatives.

## 8. Scope

Proved here:

* the exact one-product solution for any finite separated representative
  list;
* the exact five-normal dual identity (4.10), its sharp affine cardinality,
  and the Schur bound (5.5);
* existence of fixed finite fixtures forcing every prescribed finite jet
  order, with the explicit `4*r+4` row bound;
* the conditional count/potential ledger (7.6), including the
  dimension-corrected consequence (7.9)--(7.10).

Not proved here:

* the conjecturally sharp `2*r+3` construction for every `r`;
* multiplication of local double- or higher-zero losses across `Theta(L)`
  cells;
* a global factor-two upper construction;
* compact Paley--Wiener transfer for a growing list;
* occurrence or exclusion of the fixtures among actual zeta zeros;
* a zero-free strip.

## 9. Referee audit

**PASS AFTER PATCHES.**  The separated-representative theorem, the five-row
normal identity and Schur double attenuation, and the fixed-order high-jet
existence theorem all survive hostile checking.  The constants in (7.8)
recompute from (7.4)--(7.6).  The patch removes an incorrect even-`m`
dimension inference and makes explicit that neither the local Schur loss nor
the conditional ledger has been multiplied across a growing family of
cells.
