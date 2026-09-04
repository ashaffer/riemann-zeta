# Fixed-`S` packet-or-dispersion: hostile stability audit

**Date:** 2026-08-25  
**Verdict:** a constant-threshold packet inverse theorem is false, even in
the exact integer product strip.  There is an explicit shell-faithful,
fully off-resonant example with

```text
8>sqrt(26)
```

distinct carrier-sum levels, no level containing more than the two ordered
swaps, no three-term progression in either the completion coordinates or the
carrier-sum labels, and no three collinear occupied points.  Thus neither a
tangent packet nor a rank-one/AP packet is forced at a constant multiple of
`sqrt(D)`.

This does **not** give a power counterexample.  The stable formulation is
exponent-level:

```text
R(S)>D^(1/2+epsilon)
  => D^(1/2+epsilon-o(1)) genuinely scattered carrier sums U.       (0.1)
```

The implication `(0.1)` follows from the proved fixed-`U` geometry.  Bounding
those scattered levels by `D^(1/2)q^o(1)` is the still-open two-inverse or
shifted-divisor dispersion theorem.  It cannot be replaced by a purely
combinatorial assertion that one packet must occur.

The fixture below uses arbitrary shell integers, not the narrower actual
prime-power QP support.  It is therefore a counterexample to any proposed
inverse theorem using only the shell and individual product bands, not an
actual-prime counterexample to the final QP theorem.

## 1. Exact gcd and shifted-divisor normal form

Take an integer centre `N` and write

```text
a+b=S,
a*v=N+e=:n,       b*w=N+f=:m,       |e|,|f|<=D.       (1.1)
```

Replacing a real centre by a nearest integer enlarges `D` by at most one, so
this normalization has no exponent cost.  Put

```text
g=gcd(a,b)=gcd(a,S),
a=g*A,       b=g*B,       A+B=T=S/g.                  (1.2)
```

Then, exactly,

```text
(A,B)=1,
g | S,n,m,
A | n/g,
B=T-A | m/g.                                         (1.3)
```

Conversely, every tuple in `(1.3)` reconstructs one representation by

```text
v=(n/g)/A,       w=(m/g)/B.                           (1.4)
```

Since `g` is the exact gcd, there is no overcount.  Consequently the ordered
fixed-sum count has the exact complementary shifted-divisor form

```text
R(S)=sum_(|e|,|f|<=D)
     sum_(g | gcd(S,N+e,N+f))
     #{A:
         A | (N+e)/g,
         S/g-A | (N+f)/g,
         gcd(A,S/g)=1,
         reconstructed a,b,v,w lie in the shell}.     (1.5)
```

In the off-resonant sector `e!=f`, one gains the necessary restriction

```text
g | e-f,       hence g<=2D.                           (1.6)
```

This is useful bookkeeping, but it is not a packet theorem.  The fixture in
Section 3 has `g=1` everywhere, so `(1.6)` can be completely generic.
For fixed `(e,f,g)`, divisor enumeration gives `q^o(1)` possibilities; the
unresolved issue is the aggregate over the short two-dimensional label box.
Termwise summation restores a much larger bound.

The diagonal `e=f` is the exact common-product resonance `a*v=b*w`.  The
separate gcd argument already proves that whole slice is

```text
O(sqrt(D)q^o(1)).                                     (1.7)
```

Thus a corrected arithmetic target may be stated solely off resonance:

```text
R_off(S):=sum_(e!=f) [the sum in (1.5)]
          <<sqrt(D)q^o(1).                            (1.8)
```

No estimate `(1.8)` is proved here.

## 2. Exact one-point and pairwise identities

Let `U=v+w`.  Every representation satisfies

```text
a*b*U=N*S+b*e+a*f.                                   (2.1)
```

For two representations indexed by `i,j`, the common centre cancels:

```text
a_i*b_i*U_i-a_j*b_j*U_j
 =b_i*e_i+a_i*f_i-b_j*e_j-a_j*f_j.                  (2.2)
```

The right side is `O(qD)`.  In centred coordinates

```text
h=(a-b)/2
```

the exact version is

```text
S*U/4-N-(U/S)*h^2
 =(e+f)/2-(e-f)*h/S.                                 (2.3)
```

Equation `(2.3)` proves the local multiplicity dichotomy.  There is at most
one exceptional `U` whose `h^2` interval lies within the first `asymp q`
range; it supports `O(sqrt(D))` points.  Every later `U` has its square
interval centred at least `cq` from zero.  Since

```text
sqrt(q)>D       at q=D^(33/16),                       (2.4)
```

consecutive squares are farther apart than the error width, and every such
level supports `O(1)` points.  Hence the rigorous stable inverse statement is

```text
R(S)<<sqrt(D)+#{occupied noncentral U}.               (2.5)
```

It follows that a power excess over `sqrt(D)` creates a power number of
distinct `U` labels.  Nothing in `(2.1)--(2.3)` forces those labels back into
one packet.

## 3. Exact off-resonant counterfixture

Take

```text
q=800,       D=26,       S=2027,       N=986978.      (3.1)
```

All coordinates in the following table lie in `[q,2q]` and both product
errors lie in `[-D,D]`.

| `a` | `b` | `v` | `w` | `U` | `e` | `f` | `X=e-f` | `eta=e+f` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 807 | 1220 | 1223 | 809 | 2032 | -17 | 2 | -19 | -15 |
| 835 | 1192 | 1182 | 828 | 2010 | -8 | -2 | -6 | -10 |
| 859 | 1168 | 1149 | 845 | 1994 | 13 | -18 | 31 | -5 |
| 882 | 1145 | 1119 | 862 | 1981 | -20 | 12 | -32 | -8 |
| 886 | 1141 | 1114 | 865 | 1979 | 26 | -13 | 39 | 13 |
| 908 | 1119 | 1087 | 882 | 1969 | 18 | -20 | 38 | -2 |
| 940 | 1087 | 1050 | 908 | 1958 | 22 | 18 | 4 | 40 |
| 987 | 1040 | 1000 | 949 | 1949 | 22 | -18 | 40 | 4 |

Adjoin the swaps `(b,a,w,v)`.  The result has sixteen ordered points and
exactly two on each of eight distinct `U` levels.  Direct exact checks give

```text
8>sqrt(26);
all eight levels are off resonance: X!=0;
all gcd(a,b)=1;
all eight (X,eta) labels are distinct;
the 16 completion a-coordinates contain no nontrivial 3AP;
the eight U labels contain no nontrivial 3AP;
the 16 points (a,v) contain no collinear triple.       (3.2)
```

Thus this is not a hidden common-product slice, a gcd stratum of unusual
size, a tangent line, or a short affine/AP packet.  It is a genuinely
scattered finite configuration.

## 4. Scaling scan

An exact interval sweep was used: for each sampled `S`, every solution of

```text
|a*v-b*w|<=2D
```

was converted to its exact common-centre interval, and those intervals were
swept while tracking the number of occupied `U` cells of multiplicity at
most two.  The table reports the largest value found among the sampled sums,
not a global maximum.

| `q` | `D=round(q^(16/33))` | sampled `S` values | best scattered `U` | ratio to `sqrt(D)` |
|---:|---:|---:|---:|---:|
| 300 | 16 | 25 | 8 | 2.00 |
| 500 | 20 | 25 | 8 | 1.79 |
| 800 | 26 | 25 | 11 | 2.16 |
| 1200 | 31 | 25 | 9 | 1.62 |
| 1800 | 38 | 25 | 10 | 1.62 |
| 2500 | 44 | 25 | 10 | 1.51 |
| 4000 | 56 | 6 | 9 | 1.20 |
| 6000 | 68 | 6 | 12 | 1.46 |
| 10000 | 87 | 14 | 10 | 1.07 |
| 16000 | 109 | 3 | 10 | 0.96 |
| 25000 | 136 | 3 | 11 | 0.94 |

These data rule out neither `D^o(1)` nor `sqrt(D)q^o(1)` growth.  The larger
rows are much too sparsely sampled, and the entire range is far too small to
distinguish logarithmic growth from a small power.  In particular, the table
must **not** be cited as asymptotic evidence for an exponent.  It does show
that constant-factor overshoots and progression-free selections are routine,
so a constant-threshold packet assertion is unstable.

No asymptotic Behrend-type construction inside the physical strip was found.
The usual CRT attempt makes the common centre at least the product of the
chosen moduli and leaves the `C asymp q^2` shell.  Thus there is currently no
example with `D^(1/2+epsilon)` scattered levels for any fixed `epsilon>0`.

A separate exhaustive **prime-only** sweep over every admissible `S` and
every exact common-centre interval gave best scattered-level counts

```text
q:                 50, 100, 200, 400, 800, 1200
best prime-only U:  1,   2,   2,   2,   2,    2.
```

This does not include higher prime powers and is much too small to support a
positive conjectural exponent.  It only confirms that the explicit fixture
in Section 3 should not be advertised as an actual-prime example.

## 5. Corrected target

The weakest true packet-or-dispersion theorem is `(2.5)`, not a packet
conclusion:

```text
central/tangent level:          O(sqrt(D));
every noncentral level:         O(1);
power excess in R(S):           power-many distinct U levels.          (5.1)
```

The missing theorem is one of the equivalent exponent-level statements

```text
#{occupied noncentral U} <<sqrt(D)q^o(1),
R_off(S) in (1.8)       <<sqrt(D)q^o(1),
nonzero-dual aggregate  <<sqrt(D)q^o(1).             (5.2)
```

Calling `(5.2)` a consequence of packet-freeness would be circular.  It is a
new short shifted-divisor/two-inverse dispersion estimate.  The finite
fixture proves that its proof must tolerate generic gcd one, distinct error
labels, and AP-free masks.

The exact fixture and identities are machine-checked in
`src/qp_fixed_s_packet_dispersion_audit.py`; focused tests are in
`src/test_qp_fixed_s_packet_dispersion_audit.py`.
