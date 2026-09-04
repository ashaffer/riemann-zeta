# QP four-cycle: actual-shell H graph core and cycle lab

**Date:** 2026-08-15  
**Verdict:** at the project truncation `U=12`, every tested actual-prime-power
row-pair/color-pair graph is 2-degenerate and has arboricity exactly two.
Its components stay tiny and its norm stays below three through `q=200003`.
This is strong finite evidence for a hereditary-sparsity route to `(FC)`, but
it is not an asymptotic theorem.  Constant 2-degeneracy, planarity, endpoint
coprimality, and outerplanarity are all false as general structural claims.

---

## 1. The graph and why degeneracy would prove FC

For truncated triples `(a,b,c)`, let the left vertices be ordered distinct
row pairs `(a,a')`, the right vertices ordered color pairs `(c,c')`, and put
an edge

```text
(a,a') -- (c,c')
```

when one carrier `b` supports both triples `(a,b,c)` and `(a',b,c')`.
Pair uniqueness makes this a simple bipartite graph.  The weighted incidence
coefficient is

```text
conjugate(kappa(a,b,c))*kappa(a',b,c'),              |coefficient|<=1.
```

This is the support graph of the matrix `H` in the simultaneous-divisor
spectral reduction.

There is a useful rigorous implication.  If this graph is `k`-degenerate and
has maximum degree `Delta`, orient it along a degeneracy ordering, with at
most `k` outgoing edges per vertex.  For the Hermitian dilation of the
weighted `H`, write

```text
M=R+R*,             ||R||_infinity<=k,       ||R||_1<=Delta.
```

Schur's bound gives

```text
||H||=||M|| <=2 sqrt(k*Delta).                         (1.1)
```

The proved arithmetic degree bound is `Delta<<D`.  Therefore the hereditary
theorem

```text
degeneracy(H)<<q^o(1)                                  (1.2)
```

would imply `||H||<<sqrt(D)q^o(1)` and hence `(FC)`, including concentrated
coefficient vectors.  This bypasses the intermediate-support gap left by a
dyadic decomposition of `z`.

Equation (1.1) is a theorem.  Equation (1.2) is only the new target suggested
by the finite data below.

---

## 2. Actual-prime-power data at the hard core

For the exact finite support `|B log(8abc/q^3)|<=1`:

| `q` | shell nodes | triples | `H` edges | max degree | max component `(V,E)` | cycle rank | degeneracy | arboricity | `||H_support||` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 25,013 | 535 | 306 | 490 | 1 | (2,1) | 0 | 1 | 1 | 1.0000 |
| 50,021 | 996 | 699 | 1,378 | 2 | (3,2) | 0 | 1 | 1 | 1.4142 |
| 100,003 | 1,875 | 1,944 | 3,976 | 1 | (2,1) | 0 | 1 | 1 | 1.0000 |
| 200,003 | 3,496 | 4,473 | 10,568 | 2 | (4,3) | 0 | 1 | 1 | 1.6180 |

Every one of these graphs is a forest.  This is a finite statement, not a
claim that the hard graph is always acyclic.

---

## 3. Actual-prime-power data at the smooth core `U=12`

| `q` | shell nodes | triples | `H` edges | max degree | cyclic components | total cycle rank | max `(V,E,excess)` | `C4` count | degeneracy | arboricity |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 25,013 | 535 | 4,002 | 35,050 | 4 | 162 | 176 | (12,11,2) | 24 | 2 | 2 |
| 50,021 | 996 | 9,675 | 107,094 | 4 | 326 | 338 | (14,14,3) | 18 | 2 | 2 |
| 100,003 | 1,875 | 21,741 | 282,978 | 4 | 476 | 496 | (18,20,3) | 42 | 2 | 2 |
| 200,003 | 3,496 | 50,292 | 805,294 | 5 | 1,052 | 1,102 | (18,18,4) | 72 | 2 | 2 |

Here `excess=E-V+1` on a connected component.  The `3`-core is empty in all
four cases.  Since cycles exist, 2-degeneracy certifies that the arboricity
is exactly two.

The support and actual smooth-weight norms are:

| `q` | `||H_support||` | `||H_weighted||` |
|---:|---:|---:|
| 25,013 | 2.414214 | 2.094756 |
| 50,021 | 2.561553 | 2.138461 |
| 100,003 | 2.618034 | 2.495716 |
| 200,003 | 2.935432 | 2.510852 |

These are deterministic finite power-iteration values.  Entrywise
domination also makes the unweighted support norm a rigorous upper bound for
the weighted norm; no asymptotic inference is made from their small size.

Only `976,1956,2840,6340` vertices lie in the respective 2-cores, out of
`64760,200324,539296,1548208` incident vertices.  Thus even the cyclic part
is a small fraction of the finite graph.

### A labeled actual cycle

At `q=25013,U=12`, the smallest cyclic component is the `C6` with left
vertices

```text
L1=(10259,10313),  L2=(12511,12577),  L3=(15161,15241)
```

and right vertices

```text
R1=(10313,10259),  R2=(12577,12511),  R3=(15241,15161).
```

Writing `v=a2*c2-a1*c1`, its six edges `(L,R;b;v)` are

```text
(L1,R2;15161;-1500)       (L1,R3;12511;-2026)
(L2,R1;15161; 1500)       (L2,R3;10259; -254)
(L3,R1;12511; 2026)       (L3,R2;10259;  254).          (3.1)
```

The two cubic residuals on each edge are selected from exactly

```text
{-89102613, 92829387, 113675675}.
```

This residual-permutation pattern is a concrete clue for a structural core
theorem, but no classification of all components is proved here.

---

## 4. Hostile cutoff ladder: constant degeneracy is false

The degeneracy changes when the fixed smooth cutoff is widened:

| `q` | cutoff ranges and observed degeneracy |
|---:|:---|
| 25,013 | `1,2 -> 1`; `4,8,12,16,20 -> 2`; `24,32,36 -> 3`; `40,48 -> 4` |
| 50,021 | `12,16 -> 2`; `24,32,40 -> 3`; `48,64 -> 4` |
| 100,003 | `12,16 -> 2`; `24,32,40,48 -> 3` |

At `q=25013,U=24`, the smallest 3-core consists of two reverse components,
each isomorphic to `K_(4,4)` minus a perfect matching.  One orientation has
left pairs

```text
(10559,11443), (11443,12401), (11897,12893), (13259,14369)
```

and the reversed pairs on the right.  Every vertex has degree three.  The
twelve edge labels `(left index,right index;b;v)` are replayed by
`smallest_core_component` in the finite module.

Thus “actual `H` is always 2-degenerate” is false.  The data do not refute
the weaker target (1.2): the observed core number grows slowly with the
cutoff, and every cutoff used here is fixed independently of `q`.

---

## 5. Integer and coprimality controls

### Full integer hard shell

| `q` | 101 | 211 | 401 | 809 | 1,601 |
|---:|---:|---:|---:|---:|---:|
| degeneracy | 2 | 2 | 3 | 4 | 3 |
| max degree | 5 | 6 | 8 | 10 | 10 |
| cycle rank | 52 | 90 | 408 | 1,348 | 4,088 |

Nonplanar components already occur at `q=211`.  Hence low core number is not
a consequence of the monotone convex carrier geometry alone.

Restricting both row-pair and color-pair vertices to gcd one does not repair
this.  At `q=809,U=1`, its smallest 3-core orientation has left vertices

```text
(345,349), (349,353), (432,437), (433,438), (434,439)
```

and right vertices

```text
(349,345), (353,349), (437,432), (438,433), (439,434).
```

It is a nonplanar 3-regular bipartite graph on ten vertices.  Its fifteen
carrier/shift labels are:

```text
(345,349):  (437,432;439;3),   (438,433;438;7),
            (439,434;437;11)
(349,353):  (437,432;434;-17), (438,433;433;-13),
            (439,434;432;-9)
(432,437):  (349,345;439;-3),  (353,349;434;17),
            (439,434;349;10)
(433,438):  (349,345;438;-7),  (353,349;433;13),
            (438,433;349;0)
(434,439):  (349,345;437;-11), (353,349;432;9),
            (437,432;349;-10).                              (5.1)
```

### Globally pairwise-coprime synthetic shell

A stronger control takes every shell prime and greedily adds composites
whose prime factors are disjoint from all previously selected nodes.  The
resulting node set is globally pairwise coprime, not merely pairwise on each
vertex.

Most tested selections at `q=12853,25013,50021,U=12` were 2-degenerate.
However, the deterministic ordering by decreasing least prime factor at
`q=25013` selects 529 primes and 30 composites and has a 3-core.  Its
smallest component is again `K_(4,4)` minus a perfect matching, with left
pairs

```text
(11467,12041), (11987,12587), (12587,13217), (12907,13553),
```

and reversed right pairs.  The only composite in this witness is

```text
12587=41*307.
```

All displayed nodes are pairwise coprime.  Therefore global pairwise
coprimality still does not force 2-degeneracy.  Primality, or a subtler
prime-power restriction, matters in the `U=12` finite data.

---

## 6. Planarity and outerplanarity audit

At `U=12`, every actual component tested through `q=200003` is planar.
Outerplanarity already fails: at `q=12853`, eight cyclic components are not
outerplanar, and failures persist at all larger tested values.

Planarity is also not stable under widening the actual cutoff.  At
`q=25013,U=24`, two components on 16 vertices and 22 edges are nonplanar.
One contains the following explicit subdivision of `K_(3,3)`; its six branch
vertices are

```text
R(14731,12653), L(10729,12491), R(12377,10631),
R(13327,11447), L(11447,13327), L(12653,14731).
```

The three subdivided paths are completed by the degree-two pairs

```text
L(10631,12377)-R(12491,10729),
L(12421,14461)-R(14503,12457),
L(12457,14503)-R(14461,12421).
```

Thus neither planarity nor outerplanarity can be the general proof.  A
quantitative core/arboricity theorem such as (1.2) survives every hostile
test performed here.

---

## 7. Binary status

```text
finite H builder with carrier and smooth weights:      IMPLEMENTED;
hard-core forest property for listed q:                VERIFIED FINITELY;
U=12 degeneracy/arboricity two for listed q:           VERIFIED FINITELY;
explicit actual C6 residual-permutation component:     VERIFIED FINITELY;
constant 2-degeneracy for actual H:                    REFUTED FINITELY;
planarity for general actual H:                        REFUTED FINITELY;
2-degeneracy from endpoint/global coprimality:          REFUTED FINITELY;
hereditary q^o(1) degeneracy/arboricity:                OPEN;
four-cycle bound (FC):                                  OPEN.
```

Executable finite replay:

```bash
PYTHONPATH=src python3 -m pytest -q src/test_qp_four_cycle_h_graph_lab.py
```

The graph builder, exact component/core/cycle ledgers, carrier labels, and
smallest-core witness extractor are in
`src/qp_four_cycle_h_graph_lab.py`.

