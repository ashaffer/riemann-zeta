# QP canonical self-orbit DRPLS: adversarial finite audit

**Date:** 2026-08-27  
**Verdict:** no all-one complete-integer self-orbit tested here violates, or
shows polynomial growth relative to, the scale `q^2/K`.  In the actual
Selberg-truncated range the largest observed normalized moment was
`2.2207082`; it was a single adjacent affine orbit.  The exact critical
balanced tower with `Theta(F)` parallel lanes and `Theta(F^2)` points stayed
below `0.301` through `q=3,234,304`, while its observed translate-aggregation
factor stayed bounded.  These are finite data, not a proof of DRPLS.

## 1. Scope and the frequency cutoff

For the complete integer-shell canonical orbit

```text
P_t=(b_t,B_t),  c*b_t-C*B_t=t,  |t|<=D,
S(h)=sum_(t,j) exp(2 pi i h q^3/(8 b_t B_j)),
M(K)=sum_(K<h<=2K)|S(h)|^2,
rho(K)=M(K)/(q^2/K),
```

there are two ranges in the tables:

```text
actual Selberg-truncated:  2K<=q/D;
strong diagnostic:        K<=q/D, so its final block reaches 2q/D.
```

This distinction matters.  The adjacent family has `rho about 2` in the
actual range and `rho about 8` in the stronger range.  The latter is useful
hostile evidence but is not the actual truncated top block.

The audit concerns the all-one **complete integer** orbit.  It makes no
claim about a theorem uniform in arbitrary masks.

## 2. Exact-residue algorithm and checks

The implementation does not evaluate a large floating phase.  It first
groups equal products,

```text
c(n)=#{(t,j): b_t B_j=n},
S(h)=sum_n c(n) exp(2 pi i h (q^3 mod 8n)/(8n)),
```

and only then converts the exact rational residue to a complex root.  It
additionally reduces every residue fraction and groups products whose
reciprocal phases are exactly equal modulo one.  This separates three
nonoscillatory ledgers in the expanded moment:

```text
strict diagonal = K * (#orbit)^2,
equal-product aliases = K * sum_n c(n)^2,
all exact phase aliases = K * sum_theta (sum_(phase(n)=theta)c(n))^2,
signed nonalias remainder = M(K)-(all exact phase aliases).
```

For `N` orbit points, `P` distinct products, and maximum frequency `H`, the
cost is `O(N^2 log N+HP)` arithmetic with `O(N^2)` memory.  Exact graph
comparisons use `K ||v-w||_infinity^2<=q`, so no rounded radius enters the
small-small classification.

Independent `complex128` and `clongdouble` runs agreed as follows:

| fixture | normalized-mass difference |
|---|---:|
| adjacent, `q=200000,D=371,K=539` | `2.31e-14` |
| balanced tower, `F=16,R=5793,K=362` | `2.20e-15` |

## 3. Adjacent orbit: the finite extremizer

For `q=2m` and `gamma=(m,m+1)`, the exact orbit is

```text
P_t=(m+1-t,m-t),   -D<=t<=D.
```

Scanning every integral `K`, rather than powers of two only, gives:

| `q` | `D=floor(q^(16/33))` | actual worst `K` | actual `rho` | exact-alias part | signed remainder | strong worst `rho` |
|---:|---:|---:|---:|---:|---:|---:|
| 2,000 | 39 | 25 | 1.4871 | 1.9214 | -0.4343 | 6.7704 |
| 5,000 | 62 | 40 | 2.0007 | 1.9830 | 0.0177 | 7.8984 |
| 10,000 | 86 | 58 | 1.8152 | 1.9997 | -0.1845 | 8.2227 |
| 20,000 | 121 | 82 | 2.1870 | 1.9756 | 0.2114 | 7.6351 |
| 50,000 | 189 | 132 | 1.9045 | 1.9956 | -0.0911 | 7.2691 |
| 100,000 | 265 | 188 | 2.0574 | 1.9884 | 0.0690 | 7.6537 |
| 200,000 | 371 | 269 | 2.1213 | 1.9941 | 0.1273 | 7.3212 |
| 500,000 | 579 | 431 | 2.1588 | 1.9940 | 0.1648 | 7.9588 |
| 1,000,000 | 811 | 616 | 2.0467 | 1.9974 | 0.0493 | 7.3435 |

A 151-position scan of adjacent anchors at `q=20000,D=121` found the
largest actual value

```text
gamma=(8512,8513), K=82:
rho=2.2207081689,
packet-square ratio=1.0172635278,
translate aggregation rho/PS=2.1830215163.
```

The large constant has a precise explanation.  The two coordinate sets are
overlapping integer intervals of length `2D+1`.  Their intersection has
length `2D`, so factor swapping supplies at least

```text
(2D+1)^2 + (2D)(2D-1)
```

exact-alias quadruples.  At `K about q/(2D)` this is asymptotically two
normalized target units; at `K about q/D` it is eight.  Thus most of the
observed adjacent mass is the already divisor-controlled exact-alias
sector, not an unidentified positive near-collision cloud.

## 4. Other hostile scans

All entries below used every integral `K` in the stated range.

| family | tests | largest actual `rho` | largest strong `rho` |
|---|---:|---:|---:|
| random primitive anchors, `q=20000` | 500 | 1.4085 | 5.7367 |
| random primitive anchors, `q=50000` | 200 | 0.9156 | 3.8040 |
| random primitive anchors, `q=100000` | 60 | 0.1835 | 0.7401 |
| designed `1<=p,P<=13`, 12 signed small `r`, `q=50000` | 306 | 1.9088 | 7.2724 |

The designed scan solves `c*p-C*P=r` exactly before building the orbit.  Its
worst actual case was again `U=(1,1),r=1`.  No many-translate or
continued-fraction design beat the adjacent orbit.

At `q=200000,D=371,K=269`, representative exact fixtures give:

| anchor | orbit points | full `rho` | small-small points | small-small `rho` | packet-square ratio | aggregation |
|---|---:|---:|---:|---:|---:|---:|
| `(100000,100001)` | 743 | 2.1213 | 743 | 2.1213 | 1.0963 | 1.9351 |
| `(106319,106348)` | 281 | 0.1408 | 281 | 0.1408 | 0.1382 | 1.0187 |
| `(104467,111006)` | 233 | 0.1047 | 0 | 0 | 0 | -- |
| `(118951,95146)` | 121 | 0.0283 | 121 | 0.0283 | 0.0264 | 1.0734 |
| `(92519,87756)` | 289 | 0.1754 | 0 | 0 | 0 | -- |

The 49-translate direction `(17,16)` in the third row is outside the
constant-one small-step cutoff at the actual top block; this is why its
small-small column is empty rather than evidence of cancellation.

## 5. Exact critical balanced tower

The geometry hostile family is

```text
q=2FR,  D=F^2,
gamma=(F(R+1)-1,FR-1),
z(m,n)=(mR-n,m(R+1)-n),
t(z)=m-Fn.
```

The implementation verifies the identities for every orbit point.  It also
constructs an exact rectangle with `0<=n<F`: every admissible lane `m`
contributes all `F` points.  The number of such lanes is `Theta(F)` for the
fixed shell (the finite counts are displayed as `lanes x F`).

With `F=N^8,R=N^25`, one has

```text
q=2N^33, D=N^16, K=q/(2D)=R/F=N^17,
R_K=sqrt(q/K)=sqrt(2)F,
U=(1,1), r=F.
```

Hence this is genuinely in the small-remainder/small-step sector:
`F << D^2/R_K^2` and `1 << D/R_K`.  It is not an easy-sector surrogate.

For the feasible analogues `R=ceil(F^(25/8))` at the actual top block:

| `F` | `q` | orbit points | guaranteed rectangle | full `rho` | alias | signed remainder | PS ratio | aggregation |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | 3,252 | 37 | `3 x 6` | 0.3986 | 0.3318 | 0.0668 | 0.2658 | 1.4996 |
| 10 | 26,680 | 81 | `4 x 10` | 0.2578 | 0.2024 | 0.0555 | 0.1912 | 1.3483 |
| 12 | 56,592 | 121 | `5 x 12` | 0.2661 | 0.2210 | 0.0451 | 0.2040 | 1.3045 |
| 16 | 185,376 | 193 | `6 x 16` | 0.2080 | 0.1761 | 0.0319 | 0.1838 | 1.1320 |
| 20 | 465,360 | 321 | `8 x 20` | 0.2324 | 0.1999 | 0.0325 | 0.2040 | 1.1390 |
| 24 | 987,216 | 481 | `10 x 24` | 0.2808 | 0.2168 | 0.0640 | 0.2270 | 1.2369 |
| 28 | 1,864,520 | 673 | `12 x 28` | 0.3009 | 0.2295 | 0.0714 | 0.2374 | 1.2672 |
| 32 | 3,234,304 | 833 | `13 x 32` | 0.2680 | 0.2049 | 0.0631 | 0.2222 | 1.2060 |

The more strongly separated analogues `R=F^4`, tested through `F=16`, also
showed no growth: full `rho<=1.408` and aggregation `<=1.930` (both small-`F`
maxima).

## 6. Binary conclusion

```text
polynomial growth relative to q^2/K found:       NO;
finite DRPLS counterexample found:                NO;
balanced F-by-F-scale tower present exactly:      YES;
balanced tower violates packet square sum:        NO;
balanced tower violates translate aggregation:    NO;
largest actual normalized mass observed:          2.2207082;
largest actual aggregation factor observed:       2.1830216;
evidence upgrades DRPLS to a theorem:              NO.
```

The remaining gap is analytic: prove signed aggregation uniformly for the
canonical orbit.  The experiments specifically remove the leading concern
that the exact critical many-lane small-small tower is a hidden polynomial
obstruction.

Reproduction and regression tests:

```text
PYTHONPATH=src pytest -q src/test_qp_canonical_self_orbit_drpls_lab.py
```

Implementation:

```text
src/qp_canonical_self_orbit_drpls_lab.py
src/test_qp_canonical_self_orbit_drpls_lab.py
```
