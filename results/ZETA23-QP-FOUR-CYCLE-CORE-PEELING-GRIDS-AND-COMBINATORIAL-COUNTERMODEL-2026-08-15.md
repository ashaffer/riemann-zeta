# QP four-cycle: core peeling, completed grids, and a combinatorial countermodel

**Date:** 2026-08-15  
**Verdict:** the largest-degree actual stars often peel before the deepest
core, but the surviving cores are not classifiable as tangent or
fixed-residual stars.  Completed `3x3` row-column grids are absent throughout
the project `U=12` data and remain rare at `U=24`; they neither explain the
positive fourth-cycle candidates nor occur inside the smallest 3- and
4-core witnesses.

There is also an exact abstract construction realizing an arbitrary
regular high-girth bipartite graph as the all-five-distinct `H` graph of a
linear 3-uniform hypergraph, with carrier degree two and no completed `3x3`.
Thus pair uniqueness, mean sparsity, shift-layer matching, and dependent
random choice cannot prove the required core bound by themselves.  The
smallest live target is an arithmetic compatibility theorem for the exact
carrier/residual labels around a core.

No four-cycle bound is proved here.

---

## 1. Peeling diagnostics

For a vertex `x` of `H`, write

```text
d(x)=degree(x),                residual degree of y=d(y)-1.       (1.1)
```

The latter measures how much of a neighbor remains after the edge back to
`x` is peeled.  For each incident edge, record the two exact cubic residuals
and the two tangent sums `b+c,b+c'`.  Call a vertex fully residual-anchored
if one coordinate residual is constant on all its edges, and fully tangent
if the pair of tangent sums is constant.

### Actual `q=200003,U=12`

| degree | vertices | in 2-core | fully residual-anchored | fully tangent | mean neighbor residual degree | maximum |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 58,656 | 5,884 | 6,300 | 52 | .222 | 4 |
| 3 | 1,728 | 412 | 0 | 0 | .376 | 4 |
| 4 | 84 | 40 | 0 | 0 | .667 | 3 |
| 5 | 4 | 4 | 0 | 0 | 1.000 | 2 |

All four maximum-degree vertices survive in the 2-core.  Thus “every
maximum-degree star peels” is already false, even though their neighbors
have residual degree at most two.

### Actual `q=25013,U=24`

| degree | vertices | in 3-core | fully residual-anchored | fully tangent | mean neighbor residual degree | maximum |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 9,200 | 8 | 0 | 8 | .816 | 5 |
| 4 | 1,592 | 4 | 0 | 0 | .937 | 5 |
| 5 | 212 | 4 | 0 | 0 | 1.219 | 5 |
| 6 | 32 | 0 | 0 | 0 | 1.083 | 5 |

Every maximum-degree vertex peels, but a 3-core remains on sixteen vertices.
The degree-six pair gaps range from `6` to `1050`, with median `382`; high
degree is biased toward a short/major-arc range, but not one exact tangent
block.

### Actual `q=100003,U=24`

| degree | vertices | in 3-core | fully residual-anchored | fully tangent | mean neighbor residual degree | maximum |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 35,384 | 12 | 0 | 4 | .554 | 6 |
| 4 | 4,084 | 20 | 0 | 0 | .654 | 5 |
| 5 | 412 | 4 | 0 | 4 | .736 | 5 |
| 6 | 48 | 8 | 0 | 0 | 1.153 | 5 |
| 7 | 4 | 0 | 0 | 0 | .286 | 2 |

The four degree-seven centers all peel and every one of their neighbors has
degree at most three.  Nevertheless, the surviving 3-core has 44 vertices,
including eight of degree six.  None is fully residual-anchored.

These tables support a quantitative neighbor-peeling strategy, but refute
the simple versions:

```text
all high-degree vertices are tangent:                   FALSE FINITELY;
all high-degree vertices have a fixed cubic residual:  FALSE FINITELY;
all maximum-degree vertices peel:                       FALSE FINITELY. (1.2)
```

No uniform implication `d(x) large => neighbors have q^o residual degree`
is proved.

---

## 2. Completed `3x3` row-column grids

A completed grid consists of three rows and three carriers for which all
nine carry triples exist.  Equivalently, the row-column support contains a
`K_(3,3)`.  The exact enumeration gives:

| `q,U` | completed grids | grids with 9 distinct unordered hyperedges | max common carriers of a row triple |
|:---|---:|---:|---:|
| 12,853, 12 | 0 | 0 | 2 |
| 25,013, 12 | 0 | 0 | 2 |
| 50,021, 12 | 0 | 0 | 2 |
| 100,003, 12 | 0 | 0 | 2 |
| 25,013, 24 | 26 | 12 | 3 |
| 50,021, 24 | 44 | 18 | 3 |
| 100,003, 24 | 18 | 8 | 3 |

At `q=25013,U=40` there are 2,956 grids.  Thus completed grids appear as the
cutoff widens, but they are not present at the project smooth core despite
its many nondegenerate rectangles and cycles.

If “rank-two pattern” is interpreted literally as vanishing determinant of
the `3x3` integer color matrix, the counts are:

```text
q,U:             25013,24   50021,24   100003,24   25013,40
grids:                  26          44           18        2956
det(color)=0:            2           0            0          54. (2.1)
```

One exact rank-two example at `q=25013,U=24` has rows

```text
(12641,12647,15053),
```

columns

```text
(12119,12263,12613),
```

and color matrix

```text
[12769 12619 12269]
[12763 12613 12263]
[10723 10597 10303],                                  (2.2)
```

whose determinant is zero.

---

## 3. Deep cores do not contain local completed grids

Take the triples supporting one smallest deepest-core component.  The local
row-column incidence has:

| `q,U` | core | core component `(V,E)` | supporting triples | completed local `3x3` |
|:---|:---|:---|---:|---:|
| 25,013, 24 | 3-core | (8,12) | 23 | 0 |
| 50,021, 24 | 3-core | (8,12) | 23 | 0 |
| 100,003, 24 | 3-core | (10,16) | 32 | 0 |
| 25,013, 40 | 4-core | (12,24) | 42 | 0 |

Therefore even an actual min-degree-three or min-degree-four `H` component
does not force a completed `3x3` among its supporting hyperedges.  This is a
finite counterexample to the most direct dependent-random-choice closure.

All deepest cores in this table have girth four.  No actual min-degree-three
high-girth component was found in these instances.  At `U=12`, however, the
explicit `C6` from the H-graph report is a genuine all-actual high-girth
2-core component.

Uniform color weight on that `C6`'s six colors gives

```text
Q_nd=0.2574897529                                      (3.1)
```

at `q=25013,U=12`, while the entire row-column support has no completed
`3x3`.  Thus even positive concentrated fourth-cycle mass does not require a
grid.

---

## 4. Grid density does not explain the projected high-Q candidates

At `U=12`, grid density is identically zero, while the already recorded
projected finite lower bounds for `Q_nd` are `.6074,.8151,.6120,.3957` at
`q=25013,50021,100003,200003`.

At `U=24`, let `g_c` count completed grids containing color `c`.  A replay of
the same projected nonnegative ascent gives:

| `q` | grids | grid colors | best projected `Q_nd` | active colors | optimizer mass on grid colors | Spearman `(z_c^2,g_c)` | uniform-grid-color `Q_nd` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 25,013 | 26 | 98 | .9925 | 20 | .462 | .167 | .0310 |
| 50,021 | 44 | 171 | .8151 | 9 | .112 | -.017 | .0165 |

The corresponding full-uniform values are `.0590` and `.0391`.  These are
diagnostics, not optimized certificates.  They show no robust positive
correlation between grid participation and the high-Q candidates.

---

## 5. Exact high-girth combinatorial countermodel

The following construction shows why the proved combinatorial inputs cannot
by themselves bound the core number.

Let `G=(L,R,E)` be any simple `k`-regular bipartite graph, of arbitrarily
large girth if desired.  Give each `i in L` a private ordered pair

```text
(a_i^0,a_i^1),
```

each `j in R` a private ordered pair

```text
(c_j^0,c_j^1),
```

and every edge `e=(i,j)` a private carrier `b_e`.  Take all these nodes
distinct and insert exactly the two unordered triples

```text
{a_i^0,b_e,c_j^0},             {a_i^1,b_e,c_j^1}.       (5.1)
```

Then:

1. The resulting 3-uniform hypergraph is linear: two nodes occur together
   in at most one hyperedge.
2. Every carrier has degree two.
3. Every `H` edge is all-five-distinct and compares two distinct unordered
   hyperedges.
4. `H` is the disjoint union of `G` on the displayed orientations and its
   reverse copy.  Hence its degeneracy is exactly `k` and its girth is that
   of `G`.
5. There is no completed row-column `3x3`, because every carrier sees only
   two rows.
6. Padding the node universe with isolated nodes makes the global mean
   degree arbitrarily small.

By Konig's line-coloring theorem, the edges of `G` can additionally be
properly colored with `k` formal shift labels.  Thus every fixed shift layer
is a matching and every vertex sees distinct shifts, while the core number
remains `k`.

This is not an integer-shell realization: it deliberately omits the cubic
carry equations.  Its exact conclusion is narrower and important:

```text
linearity + pair uniqueness + mean sparsity + carrier degree two
+ all-five genericity + fixed-shift matchings + no completed 3x3
do not imply subpolynomial degeneracy.                         (5.2)
```

Any proof must use joint arithmetic compatibility of the carrier, shift,
and residual labels around cycles, not only their separate local bounds.

---

## 6. Smallest live target

The remaining structural target can be stated without max-degree language.

> **Arithmetic core-label theorem.**  In every induced subgraph of the
> actual all-five-distinct `H`, if every vertex has degree at least `k`, then
> `k<<q^o(1)`.

Together with the already proved `Delta(H)<<D`, the orientation inequality

```text
||H||<=2 sqrt(k*Delta(H))                              (6.1)
```

would prove the required spectral bound.

The finite data suggest two narrower ways to attack it:

1. prove that a `k`-core with large `k` must contain many `H` four-cycles,
   then use the exact residual/determinant identities to bound those cycles;
2. prove a quantitative neighbor-peeling statement after excluding the
   finitely classifiable residual-anchor and tangent sectors.

Neither statement is presently proved.  The abstract construction in
Section 5 shows that the arithmetic label compatibility is indispensable.

---

## 7. Binary status

```text
maximum-degree vertices always peel:                  REFUTED FINITELY;
tangent/fixed-residual classification of deep cores:  REFUTED FINITELY;
completed 3x3 at U=12 in tested actual supports:       ABSENT FINITELY;
deep core => local completed 3x3:                      REFUTED FINITELY;
high-Q/grid-density correlation:                       NOT OBSERVED;
combinatorial q^o core theorem from current inputs:    FALSE ABSTRACTLY;
arithmetic core-label theorem:                         OPEN;
four-cycle bound (FC):                                 OPEN.
```

