# QP four-cycle: residual cores after dyadic gap projection

**Date:** 2026-08-15  
**Verdict:** the dyadic gap-projection theorem removes a large structured
sector, but its finite complement is not a forest and is not uniformly
two-degenerate at the scanned scales.  An explicit actual-prime residual
`K5` survives at `q=100003`, cutoff `U=24`, even after deleting all
repeated-coordinate rectangles and applying projection constant `C=100`.

This is a finite hostile diagnostic.  It does not contradict the proven
sector theorem and makes no asymptotic assertion.

---

## 1. Exact filter

For rows `(a1,a2)` and columns `(b1,b2)`, put

```text
A=|a2-a1|, B=|b2-b1|, rho_ij=1+|ai-bj|.            (1.1)
```

The three squared projection scales are

```text
(1+A)^2 min(rho11,rho12) min(rho21,rho22),
(1+B)^2 min(rho11,rho21) min(rho12,rho22),
min(1+A,1+B)^2 min(rho11,rho22) min(rho12,rho21).   (1.2)
```

A rectangle is filtered at constant `C` when the smallest square root in
(1.2) is at most `C D`.  Before this test, the ledger below retains only
rectangles with all eight displayed coordinates distinct and all four
unordered hyperedges distinct.

The theorem controls every fixed/dyadic sector with an `O_C(D)` weighted
bound; summing its logarithmically many sectors costs only `q^o(1)`.  A
finite residual at one selected constant is not evidence against that
statement.

---

## 2. Residual pair-incidence graph

The first graph keeps the prior H vertices and retains an H incidence if it
participates in at least one uncovered generic rectangle.  At `C=100`:

| `q,U` | uncovered rectangles | residual H edges | 2-core vertices | degeneracy |
|---|---:|---:|---:|---:|
| 25013,24 | 3396 | 12016 | 116 | 2 |
| 50021,24 | 19048 | 65662 | 854 | 2 |
| 100003,24 | 66876 | 229256 | 2842 | 3 |
| 25013,40 | 9580 | 30666 | 870 | 2 |

The full generic H degeneracies in the same order are `2,2,3,4`; for
`q=25013,U=40` the filter lowers degeneracy to 3 at `C=1` and to 2 by
`C=64`.

---

## 3. Completion-interaction graph

The more faithful local graph fixes the ordered row pair.  Its vertices are

```text
(a1,a2,b,c1,c2),                                    (3.1)
```

and an uncovered original rectangle joins its two column completions.  The
exact degeneracies are:

| `q,U` | `C=1` | `4` | `10` | `16` | `64` | `100` |
|---|---:|---:|---:|---:|---:|---:|
| 25013,24 | 5 | 5 | 4 | 4 | 3 | 2 |
| 50021,24 | 5 | 5 | 5 | 5 | 4 | 4 |
| 100003,24 | 6 | 6 | 5 | 5 | 4 | 4 |
| 25013,40 | 8 | 8 | 7 | 7 | 5 | 4 |

Thus the currently proved anisotropic/near-square sectors do not leave a
uniformly forest-like interaction graph at these scales.

---

## 4. Explicit clean residual `K5`

At `q=100003,U=24,C=100`, fix the rows

```text
(43391,44537).                                      (4.1)
```

The following five H incidences form a complete graph under column-pair
completion:

```text
carrier 47279, colors (60937,59369)
carrier 47951, colors (60083,58537)
carrier 50503, colors (57047,55579)
carrier 53951, colors (53401,52027)
carrier 60757, colors (47419,46199).                (4.2)
```

All 17 displayed labels are prime.  Every one of the ten rectangles has all
eight coordinates distinct and four distinct unordered hyperedges.  Their
best projection-scale ratios range from

```text
113.0465 D to 627.7115 D,                           (4.3)
```

so every edge survives the `C=100` filter.  This gives residual degeneracy
at least four with no repeated-node explanation.

---

## 5. Consequence

The gap-projection theorem is a real sector theorem, but a direct argument
that its complement is acyclic, two-degenerate, or supported only on
permutation/repeated-coordinate wedges is false at finite scale.  Any core
peeling closure must use another arithmetic invariant on the residual
completion graph, or prove that fixed positive degeneracy has sufficiently
small weighted mass after dyadic summation.

Exact replay code:

```text
src/qp_four_cycle_gap_residual_lab.py
src/test_qp_four_cycle_gap_residual_lab.py
```

