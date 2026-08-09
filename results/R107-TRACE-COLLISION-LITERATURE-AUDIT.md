# R107 trace-collision literature audit

Status: targeted primary-literature audit and exact trilinear-hypersurface
import.  The imported theorem recovers the existing `H^(2+o(1))` fixed-trace
fiber bound, but gives no fixed power beyond it.  No source surveyed here
proves `N_8(H)<<H^(6-delta)`, a fixed zeta zero-free strip, or the
nonexistence of such a strip.

Date: 2026-08-07.

## 1. Target and verdict

Write

```text
Tr_a(h_1,h_2,h_3,h_4)
 =a^2 h_1h_2h_3h_4-a(h_1+h_3)(h_2+h_4)+2,            (1.1)

r_T(H)=#{h in Z^4: abs(h_i)<=H, Tr_a(h)=T},
N_8(H)=sum_T r_T(H)^2.                                 (1.2)
```

Here `a` is a nonzero integer of polynomial height in `H`.  R100 proves

```text
r_T(H)<<H^(2+o(1))        for T!=plusminus2,
N_8(H)<<H^(6+o(1))        after the corresponding trace grouping.  (1.3)
```

The requested new input would be either

```text
sup_(T!=plusminus2) r_T(H)<<H^(2-delta)                (1.4)
```

or, more directly,

```text
N_8(H)<<H^(6-delta)                                  (1.5)
```

for a fixed `delta>0`.  A targeted search of cyclic continuants,
trilinear hypersurfaces, Markoff--Hurwitz varieties, bilinear-form energy,
integer determinant equations, additive-divisor estimates, and matrix
product counts found one theorem which matches (1.1) exactly after
homogenization: Theorem 9 of Thomas Reuss.  Its application is rigorous and
useful as a baseline, but its two boundary terms sum to exactly `H^2` in
(1.4), or `H^6` in (1.5).  The other sources below either give structural
identities without box counts, treat a geometrically different variety, or
also stop at the `H^6` incidence scale.

This is a targeted survey, not an exhaustive proof that no applicable
theorem exists.

## 2. Exact import: Reuss's trilinear hypersurface theorem

Theorem 9 of [Reuss, *Counting points on bilinear and trilinear
hypersurfaces*](https://arxiv.org/abs/1502.07594) concerns an integral
trilinear form

```text
f(x,y,z),       x,y,z in P^1(Z),
```

with nonzero Cayley hyperdeterminant `D`.  If `f` is irreducible and

```text
s(x,y,z)=Delta_xy(z) Delta_yz(x) Delta_zx(y)!=0,       (2.1)
```

then the number of primitive representatives in the box

```text
abs(x_i)<=X_i,  abs(y_i)<=Y_i,  abs(z_i)<=Z_i
```

is

```text
N_f << mathcalT^epsilon [
       (X_1X_2Y_1Y_2Z_1Z_2)^(1/2)/abs(D)^(1/4)
       +(X_1X_2Y_1Y_2)^(1/2)+Z_1Z_2],                 (2.2)

mathcalT=norm(f)X_1X_2Y_1Y_2Z_1Z_2.                  (2.3)
```

The variables may be permuted before taking the best bound.  The absolute
value in (2.2) is the natural interpretation of the source's
`D^(1/4)` notation.  The theorem is coefficient-uniform up to the displayed
`mathcalT^epsilon` factor.

### 2.1 Homogenizing the canonical trace

Fix `h_1=u`, put

```text
x=(h_2,1),       y=(h_3,1),       z=(h_4,1),
```

and homogenize `Tr_a(h)=T` separately in the three pairs.  The resulting
form is

```text
f_(u,T)(x,y,z)
 = a^2u x_0y_0z_0
   -a x_0y_0z_1-a u x_0y_1z_1
   -a x_1y_0z_0-a u x_1y_1z_0
   +(2-T)x_1y_1z_1.                                   (2.4)
```

A direct Cayley-hyperdeterminant expansion gives the exact identity

```text
D(f_(u,T))=a^4u^2(T^2-4).                             (2.5)
```

Thus `D!=0` whenever `u!=0` and `T!=plusminus2`.  A factorized trilinear
form has zero hyperdeterminant in Reuss's setup, so (2.5) also verifies the
irreducibility hypothesis.

The exclusion (2.1) does not discard any rational point on our affine
chart.  On putting the second coordinate of each pair equal to `1`, the
three determinant forms are

```text
Delta_xy(h_4)
 =-a[a^2u^2h_4^2+a u(T-2)h_4-(T-2)],

Delta_yz(h_2)
 =-a[a^2u^2h_2^2+a u(T-2)h_2-(T-2)],

Delta_zx(h_3)
 =-a^2[u^2+T u h_3+h_3^2].                            (2.6)
```

Every quadratic in (2.6) has discriminant equal to a rational square
multiple of `T^2-4`.  If one had a rational root, `T^2-4` would be a
rational square and hence an integer square.  But

```text
T^2-y^2=4
```

has integral solutions only at `T=plusminus2`, `y=0`.  Therefore `s!=0`
for every affine rational point under the current hypotheses.  This check
is important: Reuss explicitly warns that his omitted `s=0` locus can be
as large as a boundary term for a general trilinear form, but that locus is
empty here.

### 2.2 The exact bound obtained

Use

```text
X_1=Y_1=Z_1=H,       X_2=Y_2=Z_2=1.
```

The affine pairs `(h_i,1)` are primitive.  Equations (2.2) and (2.5) give,
uniformly for `u!=0` and `T!=plusminus2`,

```text
#{(h_2,h_3,h_4): abs(h_i)<=H, Tr_a(u,h_2,h_3,h_4)=T}

 <<H^epsilon [
   H^(3/2)/(abs(a)abs(u)^(1/2)abs(T^2-4)^(1/4))+H].   (2.7)
```

Summing `1<=abs(u)<=H` yields

```text
r_T(H)
 <<H^(2+epsilon)[1+1/(abs(a)abs(T^2-4)^(1/4))].       (2.8)
```

The slice `u=0` is smaller.  There

```text
T=2-a h_3(h_2+h_4),                                  (2.9)
```

so for `T!=2` there are divisor-many choices of `h_3` and `O(H)` choices
of `(h_2,h_4)`, giving `H^(1+o(1))`.  Consequently (2.8) rigorously
recovers R100's `H^(2+o(1))` nonparabolic fiber estimate by a completely
different theorem.

It does not prove (1.4).  The `+H` term in (2.7), repeated over the `H`
choices of `u`, is already `H^2`.  The hyperdeterminant gain improves the
first term when `abs(u)` or `abs(T)` is large, but it does not affect this
boundary term.

For collisions, fix `h_1=u` in one copy and all four variables of the other
copy.  Equation `Tr_a(h)=Tr_a(h')` is then (2.4) in the remaining three
variables.  There are `O(H^5)` fixed choices, and the `+H` term in (2.7)
therefore gives

```text
N_8(H)<<H^(6+epsilon)                                 (2.10)
```

for the nonparabolic, nonzero-`u` part.  The omitted axis and parabolic
strata are elementary and do not exceed this endpoint (the `T=2` fiber has
a genuine `H^2` subfamily when `h_1=h_3=0`).  Reuss thus identifies the
nonparabolic obstruction unusually cleanly: an improvement needs a theorem
which uses the coefficient-specific affine chart to beat or average his
boundary terms; nonzero hyperdeterminant alone is insufficient.

### 2.3 Primitive same-residue reduction and divisor-AP audit

There is an additional exact reduction which Reuss's general theorem does
not see.  In the `a=1`, nonzero-opposite-coordinate case, write

```text
h_1=v r,       h_3=v s,       (r,s)=1,       v>0.     (2.11)
```

Dividing R100's opposite-pair factorization by `v^2` gives

```text
(vrs h_2-(r+s))(vrs h_4-(r+s))
 =r^2+T rs+s^2.                                      (2.12)
```

Reducing (2.12) modulo `q=vrs` proves the necessary condition

```text
v divides T-2.                                        (2.13)
```

Indeed the right side differs from `(r+s)^2` by `(T-2)rs`.
Consequently every solution corresponds to a factorization

```text
A B=N_(r,s):=r^2+T rs+s^2,
A congruent B congruent -(r+s) (mod q),       q=vrs,   (2.14)
```

with the two affine quotients bounded by `H`.  For general integral `a`,
replace `q` by `a vrs`; the necessary condition becomes `a v|(T-2)`.

This is more restrictive than an ordinary divisor bound, but the closest
divisor-in-progressions theorems do not match its quantifiers:

* [Shparlinski, *On the Restricted Divisor Function in Arithmetic
  Progressions*](https://arxiv.org/abs/1003.5347), Theorems 5 and 6,
  controls second moments over residue classes, or averages of
  `tau_(M,N)(k)` as `k` runs through families of progressions, with a fixed
  modulus (the strongest displayed two-parameter result is stated first for
  prime modulus).  In (2.14), there is only one correlated value
  `k=N_(r,s)`, while the modulus and residue move with the same `(r,s)`.
* [Nguyen, *Generalized divisor functions in arithmetic progressions:
  I*](https://arxiv.org/abs/2308.06839) obtains power-saving discrepancy
  bounds after summing `tau_k(n)` over `n<=X` and averaging over constrained,
  well-factorable moduli.  It does not estimate an individual binary
  quadratic value with a modulus made from its variables.
* [Grimmelt--Merikoski, *The divisor function along arithmetic
  progressions and binary cubic
  polynomials*](https://arxiv.org/abs/2508.17979), Theorems 1.1 and 1.3,
  reaches almost all moduli near `X^(2/3)` and factorable moduli under
  explicit size hierarchies, for primitive fixed residue classes and after
  a long `n`-sum.  The moving class `-(r+s) mod vrs` and single value
  `r^2+Trs+s^2` are outside that setup.

The key missing theorem is therefore not ordinary equidistribution of
`tau(n)` in progressions.  It is an average, over primitive `(r,s)`, of the
*same-residue factor-pair count* in (2.14), uniform in the moving
discriminant `T^2-4`.  None of the checked divisor-AP results removes the
`+1` per `(r,s)` which becomes Reuss's repeated boundary term.

## 3. Exact cyclic-continuant identification

For `a=1`, (1.1) is exactly the length-four rotundus of
[Conley--Ovsienko, *Rotundus: triangulations, Chebyshev polynomials, and
Pfaffians*](https://arxiv.org/abs/1707.09106):

```text
R_4(h_1,h_2,h_3,h_4)
 =h_1h_2h_3h_4-h_1h_2-h_2h_3-h_3h_4-h_4h_1+2.        (3.1)
```

This is not just an analogy; (3.1) equals `Tr_1(h)` term by term.  Their
Theorem 2 classifies *totally positive* integer solutions of a special
rotundus equation using centrally symmetric triangulations.  The paper
states that after total positivity is dropped, even classification of
positive solutions is open in the relevant lengths.  It supplies no
uniform signed-box estimate for arbitrary levels `R_4=T`.

[Ovsienko, *Partitions of unity in SL(2,Z), negative continued fractions,
and dissections of polygons*](https://arxiv.org/abs/1710.02996) similarly
classifies positive sequences for which the full matrix product is
`plusminus I` or a square root of `-I`.  Those are special central or
zero-trace product values, not a count of arbitrary signed trace fibers.

[Badziahin, *Continuant Diophantine
equations*](https://arxiv.org/abs/1607.07212) gives structural chains and
factorizations for reciprocal-quadratic continuant equations.  It supports
the exact adjacent identity already used in R100,

```text
(p h_3-h_1)(p h_4-h_2)=p^2+pT+1,    p=h_1h_2-1,      (3.2)
```

but states no estimate uniform in the varying multiplication-table
parameter `p`, the trace `T`, and a signed box.  These continuant papers are
therefore structural lemmas, not imports of (1.4) or (1.5).

There is also a useful terminology warning.  Badziahin's Theorem 3
classifies the ordinary continuant equation `K_4=1` and includes three
two-parameter integer families.  Thus an `O(H^(1+epsilon))` theorem is false
for an undifferentiated claim about all length-four *ordinary* continuants.
Our polynomial is the cyclic continuant `R_4`, and the target excludes its
parabolic `R_4=2` two-parameter family.  The targeted search found no paper
claiming `O(H^(1+epsilon))` for the signed cyclic fibers
`R_4=T`, `T!=plusminus2`.

## 4. Nearby counting theorems and their hypothesis mismatches

### 4.1 Markoff--Hurwitz integer points

[Gamburd--Magee--Ronan, *An asymptotic formula for integer points on
Markoff--Hurwitz varieties*](https://arxiv.org/abs/1603.06267), Theorem 3,
counts unexceptional solutions of

```text
x_1^2+...+x_n^2=a x_1...x_n+k
```

up to height `R` as `c(log R)^beta+o((log R)^beta)`.  Exceptional families,
when present, can have at least linear growth.  The small count comes from
Vieta involutions, reduction to a compact fundamental set, and an infinite
descent on positive tuples.  Our rotundus is linear, not quadratic, in each
coordinate; its signed level sets have no known height-reducing Vieta
action.  No birational height-preserving transfer of their hypotheses was
found, so their polylogarithmic theorem is not applicable.

### 4.2 Bilinear and point--plane energy

R100's exact invariant form is

```text
Tr_a(h)-2
 =a(a h_1h_3,-h_1-h_3) dot (h_2h_4,h_2+h_4).         (4.1)
```

Each pair invariant has multiplicity at most two, but radial and collinear
multiplicities remain.  [Rudnev, *On the number of incidences between
points and planes in three dimensions*](https://arxiv.org/abs/1407.0426),
Theorems 3 and 14, gives

```text
I(P,Pi)=O(m sqrt(n)+mk)
```

and its weighted analogue.  In the most favorable one-point-per-direction
specialization of the associated bilinear-value collision problem, the
main energy scale is `N^3` for a planar set of `N` points.  Here each
invariant set has `N asymp H^2`, so even that favorable scale is `H^6`.
The weighted/collinear versions are weaker.  Thus generic point--plane or
hyperbolic-paraboloid incidence does not yield (1.5); it would need a new
estimate exploiting the two discriminant-square parametrized subsets in
(4.1).

### 4.3 Shifted products and fixed determinants

The exact off-diagonal adjacent-cell equation is

```text
qUV-pU'V'=(p-q)(pq-1).                                (4.2)
```

[Topacogullari, *On a certain additive divisor
problem*](https://arxiv.org/abs/1512.05770) proves power-saving asymptotics
for smoothed positive-variable sums on

```text
r_1 n_2-r_2 n_1=h
```

with fixed coprime coefficients and controlled shifts.  Taking
`n_1=UV`, `n_2=U'V'` makes (4.2) look similar, but here `p,q` vary over a
near-quadratic multiplication-table set; the factor variables are signed,
affine, residue-restricted, and carry weights depending on `p,q`.
Discarding these restrictions leaves the positive divisor main term rather
than a cancellation estimate.  The cited theorem is not uniform in the
joint regime needed by (4.2).

[Chapman--Mudgal, *Counting 2x2 integer matrices with a given
determinant*](https://arxiv.org/abs/2509.20259), Theorem 1.1, proves for
`1<=h<=2N^2`

```text
#{(x,y,z,w) in [-N,N]^4: xy-zw=h}
 =16/zeta(2) N^2 sum_(d|h)1/d+O_epsilon(N^epsilon(N+h)). (4.3)
```

Equation (4.3) is a warning against a positive majorant of (4.2): the
unrestricted determinant variety genuinely has an `N^2` main term.  The
theorem does not preserve the sparse affine congruences which could create
cancellation in our signed weighted sum.

### 4.4 Full matrix products

[Afifurrahman, *Some counting questions for matrix
products*](https://arxiv.org/abs/2306.04885), Corollary 2.2, bounds solutions
of

```text
A_1...A_m=B_1...B_m
```

in a full `n x n` integer matrix box.  For nonsingular matrices its exponent
is `(2m-1)n^2-(m-1)n+o(1)` in the entry height.  At `n=2,m=2` this is
`H^(10+o(1))`; trace equality is weaker than matrix equality, and the full
matrix box does not exploit our one-parameter `SL_2` factors.  It gives no
competitive bound for (1.5).

## 5. Applicability matrix

| Source | Exact match to our equation? | Quantitative consequence here | Verdict |
|---|---:|---:|---|
| Reuss, Theorem 9 | Yes, after fixing `h_1` and homogenizing | `r_T<<H^(2+epsilon)`, `N_8<<H^(6+epsilon)` | Directly applicable, endpoint only |
| Conley--Ovsienko rotundus | Yes for `a=1` | Exact cyclic-continuant identity | Structural only; positivity/classification hypotheses do not count signed fibers |
| Ovsienko / Badziahin | Special product values or adjacent reciprocal factorization | Recovers (3.2) | No uniform varying-`p,T` box estimate |
| Shparlinski; Nguyen; Grimmelt--Merikoski | No: long divisor sums in fixed/averaged progressions | No bound for (2.14) | Correlated value, modulus, and residue violate the averaging setup |
| Gamburd--Magee--Ronan | No: Markoff--Hurwitz is quadratic in each variable | None without a new descent action | Not directly applicable |
| Rudnev point--plane incidence | Yes at the abstract dot-product level | Favorable generic energy scale `H^6` | Endpoint; special lattice geometry unused |
| Topacogullari additive divisor | Formally resembles (4.2) after multiplying variables | Fixed-coefficient smoothed error terms | Varying coefficients, signs, affine restrictions, and weights violate the needed setup |
| Chapman--Mudgal determinant count | Positive majorant of a fixed `(p,q)` cell | Exhibits an `N^2` main term | Cannot provide signed cancellation |
| Afifurrahman matrix products | Only in a much larger ambient space | Full-box exponent far too large | Not directly applicable |

## 6. What the literature import changes

The survey does not merely repeat the divisor proof.  It gives a precise
geometric diagnosis:

1. The fixed-`u,T` trace equation is a nonsingular trilinear hypersurface
   with hyperdeterminant exactly `a^4u^2(T^2-4)`.
2. Reuss's potentially large excluded singular locus is empty on the
   canonical affine chart for every nonparabolic integer trace.
3. The determinant-sensitive term in the best exact imported theorem is
   already favorable.  The loss is in its coefficient-insensitive boundary
   terms.
4. Generic bilinear incidence also stops at `H^6`, while generic determinant
   counting contains a real main term.  Any gain must use the simultaneous
   sparse parametrizations, not just nondegeneracy of the ambient variety.
5. Primitive reduction further says that the scale variable `v` divides
   `T-2`, but turns the remaining problem into the correlated same-residue
   factor average (2.14).  Existing divisor-in-progressions theorems average
   the wrong independent variables.

The clean next theorem to attack is therefore a coefficient-specific
affine-chart refinement or average of (2.7), for example

```text
sum_(abs(u)<=H)
 #{(h_2,h_3,h_4): Tr_a(u,h_2,h_3,h_4)=T}
 <<H^(2-delta)                                         (6.1)
```

uniformly for `T!=plusminus2`, or its eight-variable weighted analogue.
Such a theorem must beat the repeated `+H` boundary term and control the
small-discriminant traces; merely increasing `abs(D)` or quoting a generic
incidence theorem cannot do it.

No surveyed theorem supplies (6.1).  Conversely, failure of these methods
does not prove that (6.1), a fixed zero-free strip, or RH is false.
