# Balanced-tower exact-alias Gram audit (2026-08-27)

## Verdict

The exact guaranteed balanced-tower rectangle does **not** show polynomial
growth, or a violation of the `q^2/K` target, in the actual truncated top
band through `F=52` (`q=23,963,160`).  After exact cross-packet phase aliases
are removed, the signed all-one Gram/diagonal ratio remains between `0.868`
and `1.339` over the whole scan, and between `1.001` and `1.214` for
`20<=F<=52`.

This does not prove the desired dispersion inequality.  It does falsify the
naive premise that unequal exact phases make every packet pair weakly
correlated: a nonalias normalized packet-pair correlation reaches `0.880`.
The maximum
absolute row sum of the whitened residual Gram reaches `7.261`, while its
spectral radius reaches `2.126`.  Thus positivity/Schur summation loses a
visible factor even though the signed all-one vector continues to cancel.
The finite range cannot distinguish a polylogarithm from a small power.

A follow-up packet-level quotient merges `P=(a,b)` with its exact
transpose involute `P^T=(b,a)`, using the column `G_P+G_(P^T)` and counting
`G_(a,a)` once.  This absorbs most of the hostile Gram mass: through `F=52`
the residual spectral radius is at most `0.860`, the maximum absolute row
sum is at most `3.509`, and the largest pair correlation is `0.509`.
Persistent nonzero correlations nevertheless remain in rational
three-lane hinges, so transposition does not yield pairwise `o(1)`.

## Exact setup and quotient

For the scaled critical family put

```text
R = ceil(F^(25/8)),  q=2FR,  D=F^2,
gamma=(F(R+1)-1,FR-1),
z(m,n)=(mR-n,m(R+1)-n),  t=m-Fn.
```

Only the guaranteed rectangle consisting of every admissible lane `m` and
`0<=n<F` is used.  A lane is one packet.  The frequency scale is

```text
K=floor(q/(2D))=floor(R/F),  K<h<=2K.
```

This is the actual top band in the truncated Selberg reduction.  It is not
the stronger formal endpoint `K=q/D` used in some earlier exploratory
scans.

For an ordered lane pair `P=(a,b)`, define

```text
G_P(h) = sum_{n,n'<F} exp(2 pi i h q^3 /
                           (8 (aR-n)(b(R+1)-n'))).
M  = sum_h |sum_P G_P(h)|^2,
PS = sum_P sum_h |G_P(h)|^2.
```

Alias equality is decided without floating point.  For every cell product
`N=(aR-n)(b(R+1)-n')`, the code computes and reduces the integer pair

```text
(q^3 mod 8N, 8N).
```

If `a[P,theta]` is the number of cells in `P` with that reduced phase, the
exact cross-packet alias mass is the integer

```text
A = K sum_theta ((sum_P a[P,theta])^2 - sum_P a[P,theta]^2).
```

The signed genuinely nonalias cross term is `E=M-PS-A`.  The all-one
alias-quotiented ratio reported below is `1+E/PS`.  For the stronger hostile
test, the off-diagonal matrix

```text
H[P,Q] = (<G_P,G_Q> - K sum_theta a[P,theta]a[Q,theta])
         / sqrt(<G_P,G_P><G_Q,G_Q>)
```

is evaluated numerically after exact range reduction; `H[P,P]=0`.

## Critical-family scan

`T=q^2/K`, `rho` is the spectral radius of `H`, and `row1` is its maximum
absolute row sum.

| F | q | K | points | M/T | PS/T | M/PS | A/PS | E/PS | rho | row1 | max pair |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | 3,252 | 45 | 18 | .07395 | .05437 | 1.3602 | .02113 | .3390 | .675 | 1.308 | .249 |
| 8 | 10,624 | 83 | 24 | .02862 | .03257 | .8788 | .01124 | -.1324 | .484 | .884 | .257 |
| 10 | 26,680 | 133 | 40 | .04292 | .03809 | 1.1269 | .02218 | .1047 | .756 | 1.876 | .327 |
| 12 | 56,592 | 196 | 60 | .04767 | .04439 | 1.0740 | .01243 | .0615 | .703 | 1.750 | .209 |
| 16 | 185,376 | 362 | 96 | .04121 | .04037 | 1.0207 | .00680 | .0139 | .804 | 2.206 | .347 |
| 20 | 465,360 | 581 | 160 | .04955 | .04482 | 1.1055 | .00779 | .0977 | 1.085 | 3.214 | .610 |
| 24 | 987,216 | 856 | 240 | .05627 | .05058 | 1.1126 | .00722 | .1054 | 1.247 | 4.136 | .821 |
| 28 | 1,864,520 | 1,189 | 336 | .05337 | .05303 | 1.0066 | .00594 | .0006 | 1.042 | 4.112 | .669 |
| 32 | 3,234,304 | 1,579 | 416 | .05185 | .04921 | 1.0536 | .00485 | .0487 | 1.034 | 4.371 | .671 |
| 36 | 5,257,512 | 2,028 | 504 | .05432 | .04613 | 1.1775 | .00594 | .1716 | 1.424 | 5.302 | .783 |
| 40 | 8,119,520 | 2,537 | 640 | .05714 | .04830 | 1.1831 | .00640 | .1767 | 2.126 | 6.140 | .847 |
| 44 | 12,030,216 | 3,106 | 748 | .04895 | .04637 | 1.0558 | .00319 | .0526 | 1.123 | 5.183 | .790 |
| 48 | 17,224,704 | 3,738 | 912 | .06055 | .04967 | 1.2191 | .00490 | .2142 | 2.063 | 7.261 | .849 |
| 52 | 23,963,160 | 4,431 | 1,092 | .05461 | .05039 | 1.0839 | .00446 | .0794 | 1.274 | 6.316 | .880 |

There is no monotone growth in `M/T`, `PS/T`, the signed quotient, or the
residual spectral radius.  The absolute row sum has an upward envelope but
is highly nonmonotone; these data do not justify fitting a power law.

## Exact near-alias mechanism

The worst nonalias correlations are usually transposed lane pairs.  For
example, witnesses include `(20,24)~(24,20)` at `F=20`,
`(40,48)~(48,40)` at `F=48`, and `(56,63)~(63,56)` at `F=52`.
This is explained by the exact identity

```text
X=(aR-n)(b(R+1)-n'),
Y=(bR-n')(a(R+1)-n),
X-Y=a n'-b n.
```

Writing `Q=q^3/8=F^3 R^3`, the corresponding unwrapped phase difference is

```text
Q(1/X-1/Y) = Q(b n-a n')/(XY).
```

For `a,b` of order `F`, `n,n'<F`, and `h` of order `R/F`, the multiplied
difference `hQ(1/X-1/Y)` is of order one, not a growing separation
parameter.  Thus exact aliases are sparse (`A/PS` is below `0.8%` from
`F=16` onward), but near-transpose aliases survive the top scale.  Any proof
that first takes absolute values of all cross-packet correlations therefore
misses the cancellation visible in the all-one sum.

## Transpose-involution quotient

Let an unordered lane pair index the merged column

```text
H_{a,b}=G_(a,b)+G_(b,a)  if a<b,
H_{a,a}=G_(a,a).
```

Then `sum H=sum G`, so the full all-one mass `M` is exactly unchanged.
The diagonal, exact cross-alias mass, and residual Gram are recomputed from
the merged cell classes rather than inferred from the ordered diagnostics.
In particular, an exact alias between `G_(a,b)` and `G_(b,a)` becomes an
internal diagonal contribution, as it should.

| F | merged columns | PS/T | M/PS | A/PS | E/PS | rho | row1 | max pair | witness |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---|
| 6 | 6 | .05712 | 1.2945 | 0 | .2945 | .512 | .876 | .214 | `(5,6)~(6,7)` |
| 8 | 6 | .03342 | .8566 | 0 | -.1434 | .283 | .453 | .138 | `(7,7)~(8,9)` |
| 10 | 10 | .04096 | 1.0480 | 0 | .0480 | .481 | 1.012 | .238 | `(9,11)~(9,12)` |
| 12 | 15 | .04653 | 1.0244 | 0 | .0244 | .526 | 1.119 | .162 | `(11,11)~(11,12)` |
| 16 | 21 | .04264 | .9664 | 0 | -.0336 | .520 | 1.241 | .203 | `(14,18)~(19,19)` |
| 20 | 36 | .04767 | 1.0395 | 0 | .0395 | .486 | 1.505 | .175 | `(19,22)~(23,24)` |
| 24 | 55 | .05377 | 1.0465 | 0 | .0465 | .553 | 1.925 | .282 | `(21,24)~(24,28)` |
| 28 | 78 | .05634 | .9474 | 0 | -.0526 | .503 | 2.184 | .115 | `(28,34)~(31,34)` |
| 32 | 91 | .05250 | .9875 | 0 | -.0125 | .564 | 2.208 | .267 | `(27,38)~(36,38)` |
| 36 | 105 | .04977 | 1.0914 | .00088 | .0905 | .574 | 2.553 | .215 | `(30,36)~(36,40)` |
| 40 | 136 | .05254 | 1.0874 | .00143 | .0860 | .860 | 2.940 | .366 | `(40,45)~(45,48)` |
| 44 | 153 | .04970 | .9849 | 0 | -.0151 | .529 | 2.659 | .176 | `(43,51)~(50,53)` |
| 48 | 190 | .05426 | 1.1160 | .00109 | .1149 | .817 | 3.509 | .509 | `(42,48)~(48,56)` |
| 52 | 231 | .05458 | 1.0007 | .00091 | -.0002 | .509 | 3.177 | .151 | `(51,62)~(56,60)` |

For `F>=20`, the exact-alias-removed all-one ratio is between `0.9474`
and `1.1149`.  Exact cross aliases vanish in ten of the fourteen rows and
never exceed `0.143%` of the merged diagonal.  Relative to the ordered
columns, the maxima fall as follows:

```text
spectral radius:       2.126 -> 0.860
absolute row sum:      7.261 -> 3.509
pair correlation:      0.880 -> 0.509
```

## Residual rational hinges

The remaining correlations are primarily three-lane hinges
`{a,b}~{b,c}`.  Among the ten largest merged correlations at each of
`F=24,40,48`, respectively 6, 7, and 7 pairs share a lane.  Three exactly
scaled families give the following isolated two-column results:

| family | lane triple `(a,b,c)` | first corr. | last corr. | tested F |
|:---|:---|---:|---:|:---|
| A | `(7F/8,F,7F/6)` | .281831 | .537353 | 24,48,72,96,120,144 |
| B | `(F,9F/8,6F/5)` | .366153 | .429686 | 40,80,120,160 |
| C | `(5F/6,F,10F/9)` | .214878 | .242285 | 36,72,108,144 |

Every exact cross-alias mass in this table is zero.  In family A the
correlations at `F=48,72,96,120,144` are respectively
`.509304,.531910,.535329,.536832,.537353`; this is compelling finite
evidence for a nonzero limiting hinge correlation, not a proof of a limit.

The first reciprocal expansion for lanes `a=alpha F`, `b=beta F` is

```text
q^3/[8(aR-n)(b(R+1)-n')]
 = FR/(alpha beta) - F/(alpha beta)
   + n/(alpha^2 beta) + n'/(alpha beta^2) + O(F/R).
```

At `h~R/F`, the multiplied error is still `O(1)`, while rational
`alpha,beta` make the displayed linear frequencies commensurate.  This
explains why a spacing-only argument cannot force hinge correlations to
zero.  A fixed number of constant-size hinge correlations is not itself a
polynomial Gram obstruction; the full merged spectral and row diagnostics
above remain bounded at the tested scales.

## Reproduction

```bash
PYTHONPATH=src pytest -q src/test_qp_canonical_self_orbit_drpls_lab.py
PYTHONPATH=src python3 src/run_qp_balanced_tower_alias_gram.py
PYTHONPATH=src python3 src/run_qp_balanced_tower_alias_gram.py --F-values 48 52
PYTHONPATH=src python3 src/run_qp_balanced_tower_alias_gram.py --transpose-quotient
PYTHONPATH=src python3 src/run_qp_balanced_tower_hinge_scan.py
```

The implementation is in `src/qp_balanced_tower_alias_gram.py`; the scan
driver is `src/run_qp_balanced_tower_alias_gram.py`.  The tests cover exact
integer eighth-root rounding, the actual top scale, the alias ledger, and a
known `F=6` cross-alias mass.  The hinge driver is
`src/run_qp_balanced_tower_hinge_scan.py`; its regression test independently
checks a zero-alias, nonzero-correlation fixture.  All phase decisions are
exact; the displayed Gram values are double-precision evaluations of roots
after exact modular range reduction.  These finite computations are
evidence only.
