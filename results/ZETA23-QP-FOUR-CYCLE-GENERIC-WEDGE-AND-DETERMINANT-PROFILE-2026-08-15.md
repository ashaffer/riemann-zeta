# QP four-cycle: generic wedge and color-determinant profile

**Date:** 2026-08-15  
**Verdict:** the repeated-node/permutation sector is not the remaining
four-cycle obstruction.  After deleting every `H` edge made from the same
unordered hyperedge, the observed actual-prime core numbers are unchanged.
At the rectangle level, all four unordered hyperedges are distinct in a
growing majority of the finite data, reaching 87% at `q=100003,U=24`.

The color-determinant layers show no `1/|k|` decay.  On the other hand, the
number of actual carrier completions of a fixed color rectangle is at most
three in oriented form and six modulo the natural rectangle symmetries in
all tested `U=12` instances through `q=200003`.  This is strong diagnostic
support for a subpolynomial completion theorem, but no such theorem is
proved here.

---

## 1. Unordered linear-hypergraph split

The dephased carry support can be regarded as an unordered 3-uniform
hypergraph

```text
T={{a,b,c}: |B log(8abc/q^3)|<=U}.                       (1.1)
```

The narrow carry window makes it linear: two coordinate values determine at
most one third value.  An `H` edge compares two triples

```text
(a,b,c),                    (a',b,c')                  (1.2)
```

sharing the carrier `b`.  They are the same unordered hyperedge exactly when

```text
(c,c')=(a',a).                                           (1.3)
```

Call (1.3) a permutation edge.  There are two increasingly strong generic
filters:

```text
distinct-hyperedge:     delete only (1.3);
all-five-distinct:      retain only edges with a,a',b,c,c' all distinct.
                                                                    (1.4)
```

The first is the exact sector left after the proved identical-unordered-edge
geometry.  The second is a hostile stronger deletion.

---

## 2. Cores survive the exact distinct-hyperedge deletion

### Project smooth core `U=12`

| `q` | all `H` edges | distinct-hyperedge edges | removed | degeneracy | cycle rank | `C4` |
|---:|---:|---:|---:|---:|---:|---:|
| 25,013 | 35,050 | 31,052 | 3,998 | 2 | 162 | 0 |
| 50,021 | 107,094 | 97,424 | 9,670 | 2 | 326 | 8 |
| 100,003 | 282,978 | 261,248 | 21,730 | 2 | 478 | 16 |
| 200,003 | 805,294 | 755,012 | 50,282 | 2 | 1,074 | 24 |

### Wider actual cores

| `q,U` | all edges | distinct-hyperedge edges | degeneracy | cycle rank | `C4` |
|:---|---:|---:|---:|---:|---:|
| 25,013, 24 | 142,652 | 134,312 | 3 | 1,898 | 356 |
| 50,021, 24 | 385,382 | 366,616 | 3 | 3,114 | 376 |
| 100,003, 24 | 1,093,470 | 1,050,004 | 3 | 5,148 | 516 |
| 25,013, 40 | 389,418 | 375,480 | 4 | 31,170 | 7,640 |

Thus all tested `3`- and `4`-cores survive after identical unordered
hyperedges are removed.

The stronger all-five-distinct deletion gives:

| `q,U` | retained fraction | degeneracy | cycle rank | `C4` |
|:---|---:|---:|---:|---:|
| 25,013, 12 | .882 | 2 | 162 | 0 |
| 50,021, 12 | .907 | 2 | 324 | 8 |
| 100,003, 12 | .920 | 2 | 474 | 16 |
| 200,003, 12 | .937 | 2 | 1,074 | 24 |
| 25,013, 24 | .936 | 2 | 1,872 | 344 |
| 50,021, 24 | .947 | 2 | 3,098 | 368 |
| 100,003, 24 | .958 | 3 | 5,134 | 516 |
| 25,013, 40 | .957 | 4 | 30,254 | 7,316 |

Even the strongest deletion therefore retains a genuine actual-prime
3-core and 4-core.  Repeated coordinates are not necessary for high core
number.

### Exact pattern of the first `U=24` core

At `q=25013,U=24`, one orientation of the smallest 3-core has left pairs

```text
L1=(10559,11443), L2=(11443,12401),
L3=(11897,12893), L4=(13259,14369)
```

and right pairs

```text
R1=(11443,10559), R2=(12401,11443),
R3=(12893,11897), R4=(14369,13259).
```

It is `K_(4,4)` minus the matching `Li--Ri`.  Its edges
`(left,right;carrier;shift v)` are

```text
L1-R2;14939;  90    L1-R3;14369; 184    L1-R4;12893; 466
L2-R1;14939; -90    L2-R3;13259;  98    L2-R4;11897; 392
L3-R1;14369;-184    L3-R2;13259; -98    L3-R4;11443; 294
L4-R1;12893;-466    L4-R2;11897;-392    L4-R3;11443;-294. (2.1)
```

Here `v=a'c'-ac`.  Every edge in (2.1) compares two distinct unordered
hyperedges.  Ten of the twelve edges have all five underlying nodes
distinct; `L1-R2` and `L2-R1` repeat the value `11443`.  Removing those two
edges peels this particular 3-core, explaining why the all-five filter drops
the `q=25013,U=24` core number from three to two.

That explanation is not general.  At `q=100003,U=24`, the all-five graph has
a 3-core with left vertices

```text
(45061,52957), (46499,54647), (47777,56149),
(49409,58067), (50767,59663)                           (2.2)
```

and their reverses on the right; it has 16 edges, every one all-five
distinct.  At `q=25013,U=40`, an all-five 4-core has six vertices on each
side and 24 edges.  These are explicit finite counterexamples to a
permutation-only core classification.

---

## 3. Rectangle wedge audit

For a nondegenerate rectangle, form its four unordered corner hyperedges

```text
{a_i,b_j,c_ij},                 i,j in {1,2}.            (3.1)
```

The counts are:

| `q,U` | rectangles | four distinct hyperedges | fraction | all 8 coordinate values distinct |
|:---|---:|---:|---:|---:|
| 12,853, 12 | 1,176 | 748 | .636 | 728 |
| 25,013, 12 | 1,419 | 904 | .637 | 902 |
| 50,021, 12 | 3,646 | 2,700 | .741 | 2,680 |
| 100,003, 12 | 6,926 | 5,398 | .779 | 5,360 |
| 200,003, 12 | 16,096 | 12,832 | .797 | 12,794 |
| 25,013, 24 | 20,829 | 16,840 | .809 | 16,564 |
| 50,021, 24 | 44,437 | 36,936 | .831 | 36,440 |
| 100,003, 24 | 100,529 | 87,418 | .870 | 86,878 |
| 25,013, 40 | 150,672 | 132,454 | .879 | 129,848 |

At `U=12`, nearly every rectangle also uses four distinct colors:

```text
q:                 25013   50021   100003   200003
four-color count:   1418    3640     6920    16088.       (3.2)
```

Consequently neither a repeated hyperedge nor a repeated color supports the
dominant finite wedge sector.

---

## 4. Color determinant: no reciprocal decay

For colors in matrix order put

```text
k=c11*c22-c12*c21.                                    (4.1)
```

At `U=12`:

| `q` | rectangles | distinct `|k|` | min `|k|` | max `|k|` | `k=0` | max exact completion | max completion modulo D4 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 25,013 | 1,419 | 497 | 6 | 3,824 | 0 | 2 | 4 |
| 50,021 | 3,646 | 1,070 | 4 | 5,682 | 0 | 2 | 4 |
| 100,003 | 6,926 | 1,777 | 2 | 9,118 | 0 | 2 | 4 |
| 200,003 | 16,096 | 3,134 | 2 | 13,574 | 0 | 3 | 6 |

The absence of `k=0` replays the proved zero-determinant exclusion.

For `q=200003`, the dyadic determinant profile is:

| `|k|` range | rectangle count | smooth kernel mass | color orbits | mean orbit completion | max |
|:---|---:|---:|---:|---:|---:|
| [2,4) | 2 | 1.265 | 1 | 2.000 | 2 |
| [4,8) | 12 | 8.471 | 6 | 2.000 | 2 |
| [8,16) | 12 | 8.246 | 6 | 2.000 | 2 |
| [16,32) | 60 | 40.502 | 30 | 2.000 | 2 |
| [32,64) | 106 | 68.876 | 53 | 2.000 | 2 |
| [64,128) | 226 | 159.153 | 113 | 2.000 | 2 |
| [128,256) | 494 | 348.682 | 246 | 2.008 | 4 |
| [256,512) | 936 | 642.922 | 468 | 2.000 | 2 |
| [512,1024) | 1,814 | 1,273.162 | 902 | 2.011 | 4 |
| [1024,2048) | 3,230 | 2,244.867 | 1,614 | 2.001 | 4 |
| [2048,4096) | 5,070 | 3,405.094 | 2,528 | 2.006 | 6 |
| [4096,8192) | 3,792 | 2,343.518 | 1,895 | 2.001 | 4 |
| [8192,16384) | 342 | 176.180 | 171 | 2.000 | 2 |

If counts decayed like `1/|k|`, dyadic totals would remain approximately
flat.  Instead they grow roughly with the bin width throughout the bulk and
fall only at the geometric boundary.  The smooth mass behaves the same way.
Thus reciprocal determinant decay is not supported by these computations.

---

## 5. Fixed-color completion multiplicity

**Subsequent hostile audit.**  The full-integer analogue of a
`(1+D/|k|) polylog(q)` completion bound is false: an exact translation grid
has `m asymp sqrt(D)` and `|k| asymp D`, even with four distinct colors and
all eight coordinates distinct after four deletions.  See
`ZETA23-QP-FOUR-CYCLE-FIXED-COLOR-TRANSLATION-GRID-OBSTRUCTION-2026-08-15.md`.
That grid is arithmetically excluded from prime-power support, so the actual
prime-power statement below remains open.

The mean D4-orbit multiplicity in the last table is essentially two.  This
is the forced transpose symmetry: swapping the row and carrier roles gives
the second completion.  Additional completions are rare.

At `q=200003,U=12`, the maximum orbit multiplicity six occurs for the color
orbit

```text
(101561,103171,109133,110863),             |k|=3600.   (5.1)
```

Its exact oriented maximum is three.  This is a repeated-coordinate
permutation configuration: some colors coincide with rows or columns.

The maximum in the all-eight-distinct sector is only two oriented/four
modulo D4.  One orbit is

```text
(105143,110477,111767,117437),             |k|=4368,  (5.2)
```

with completions including

```text
rows (82223,87403),       columns (103567,108821),
rows (97429,103567),      columns (87403,91837).       (5.3)
```

The gaps in (5.3) are macroscopic, not the close-row tangent block from the
common-neighbor maximum.  Thus a completion theorem cannot be reduced to
the tangent sector alone.

No proof that the completion multiplicity is `q^o(1)` is obtained.  The
finite maximum `3` is a diagnostic, not an asserted uniform bound.

---

## 6. Closed-walk carrier pairing is false

At `q=25013,U=12`, an actual `H` four-cycle has left vertices

```text
L1=(10429,11393),              L2=(11423,12479)
```

and right vertices

```text
R1=(12479,11423),              R2=(15031,13759).
```

In cyclic order

```text
L1-R1-L2-R2-L1
```

the carriers are

```text
15031, 13723, 11393, 12479.                              (6.1)
```

The alternating products are

```text
15031*11393=171248183,
13723*12479=171249317.                                  (6.2)
```

They differ by `-1134`, and the alternating carrier multisets also differ.
Therefore neither exact odd/even carrier-multiset pairing nor equality of
alternating carrier products holds on all closed `H` walks.  The strongest
moment-pairing shortcut is finitely refuted.

---

## 7. Binary status

```text
identical-unordered-hyperedge filter:                  IMPLEMENTED;
all-five-distinct edge filter:                         IMPLEMENTED;
four-distinct-hyperedge wedge countersector:           VERIFIED FINITELY;
constant/planar core from permutation deletion:        REFUTED FINITELY;
1/|k| determinant-layer decay:                         NOT SUPPORTED;
small fixed-color completion multiplicity:             OBSERVED FINITELY;
q^o(1) completion theorem:                             OPEN;
exact carrier pairing on closed H walks:               REFUTED FINITELY;
four-cycle bound (FC):                                  OPEN.
```

Executable routines for both edge filters, rectangle enumeration,
determinants, unordered-hyperedge counts, and completion ledgers are in
`src/qp_four_cycle_h_graph_lab.py`.  Tests:

```bash
PYTHONPATH=src python3 -m pytest -q src/test_qp_four_cycle_h_graph_lab.py
```
