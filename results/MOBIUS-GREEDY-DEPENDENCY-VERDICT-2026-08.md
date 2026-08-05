# Value-ordered Mobius greedy: dependency-forest verdict

Status: blocker-forest route pruned as an independent RH mechanism,
2026-08-04.  The exact greedy rule is well defined and its extra allocation
defect is shallow in every audited collar.  However, that defect separates
algebraically from the Mobius imbalance.  Eliminating it leaves exactly
`|M(N)|`; ordering, expansion, terminality, and augmenting paths do not bound
the majority residual.  No RH claim is made.

## 1. Exact rule

Let

```text
S_N={m:N/2<m<=N, m odd and squarefree}.
```

Write `E_N` for the vertices with even `omega(m)` and `O_N` for those with
odd `omega(m)`.  The collar identity is

```text
|E_N|-|O_N|=sum_(m in S_N) mu(m)=M(N).              (1)
```

The graph joins two factor sets when one is obtained from the other by a
one-prime-for-two-primes exchange.  The value-ordered greedy processes
`E_N` in increasing integer value and matches each vertex to its smallest
currently unused odd neighbor.

The implementation is exactly this serial dictatorship.  Collar vertices
and all common-core buckets inherit increasing value order.  For each core,
`first_available` returns the least live eligible entry; the outer minimum
selects the least live neighbor over all cores.  Its pointer skips only an
already-used prefix and never skips a forbidden live entry.

## 2. The decisive decomposition

Let

```text
E=|E_N|, O=|O_N|, nu_g=number of greedy pairs,
U_E=E-nu_g, U_O=O-nu_g, R_g=U_E+U_O.
```

Then, without any graph hypothesis,

```text
U_E-U_O=E-O=M(N),                                  (2)
R_g=|M(N)|+2D_g,   D_g=min(U_E,U_O).                (3)
```

If `nu_*` is the maximum matching size, define the Hall loss and greedy loss
by

```text
h_N=min(E,O)-nu_*,       d_N=nu_*-nu_g.
```

Then

```text
D_g=h_N+d_N,
R_g=|M(N)|+2h_N+2d_N.                              (4)
```

Alternating paths can reduce `d_N`; graph expansion can rule out `h_N`.
Neither operation changes `E-O`.  Even a theorem that the greedy is maximum
and saturates the smaller side gives only

```text
R_g=|M(N)|.                                         (5)
```

Thus the proposed dependency-forest analysis naturally attacks the easy
additive term in (3), not the Mertens term.

## 3. Polynomial compression: the matching and fugacity paths coincide

Let the collar rank enumerator be

```text
Q_N(z)=sum_(m in S_N) z^omega(m).
```

For any exchange matching `A`, a matched edge whose lower rank is `r`
contributes

```text
z^r+z^(r+1)=(1+z)z^r.
```

Consequently there is an exact positive-coefficient decomposition

```text
Q_N(z)=(1+z) A_N(z)+U_N(z),                         (6)
```

where `A_N(z)` enumerates matched edges by lower rank and `U_N(z)` enumerates
the unmatched vertices.  Evaluation at the two relevant points gives

```text
U_N(-1)=Q_N(-1)=M(N),
U_N(1)=R_A(N).                                      (7)
```

The inequality `|M(N)|<=R_A(N)` is therefore just
`|U_N(-1)|<=U_N(1)` for a polynomial with nonnegative coefficients.
Augmenting a matching extracts one more positive multiple of `1+z`; it does
not alter the singular endpoint value.

Equivalently, let `n_r` and `u_r` count all and unmatched collar vertices of
rank `r`, and let `x_k` count matched edges with a common core of rank `k`.
Every such edge consumes one rank-`k+1` and one rank-`k+2` vertex, so

```text
u_r=n_r-x_(r-1)-x_(r-2),                            (8)
```

with negative subscripts interpreted as zero.  The two flow terms cancel in
the alternating sum.  Rank transport can redistribute the residual but
cannot change its signed mass.

This is also the exact connection to the earlier squarefree fugacity
polynomial

```text
P_N(z)=sum_(n<=N) mu(n)^2 z^omega(n).
```

Pair every odd squarefree `m<=N/2` with `2m`.  Their contributions are
`z^omega(m)(1+z)`, leaving precisely the odd collar:

```text
P_N(z)=(1+z) B_N(z)+Q_N(z),                         (9)
```

where `B_N` has nonnegative coefficients.  Hence

```text
P_N(-1)=Q_N(-1)=U_N(-1)=M(N).                      (10)
```

The fugacity-displacement and exchange-matching paths are not orthogonal.
Both try to control the same singular `z=-1` remainder after removing
manifest positive multiples of `1+z`.

## 4. What the blocker forest proves

Let `c(e)` be the odd vertex selected by an even vertex `e`, and let
`owner(o)` be the even vertex matched to `o`.

The greedy order gives the following exact certificates.

1. If `e` is unmatched, every `o` in its neighborhood has
   `owner(o)<e`.
2. If `c(e)=t`, every neighboring odd `o<t` has `owner(o)<e`.
3. If an odd vertex `f` is free after the algorithm, every even neighbor `e`
   is matched and satisfies `c(e)<f`.

Direct an even vertex through a neighbor certified to have been used before
that vertex was processed--every neighbor for an unmatched vertex, or a
neighbor below `c(e)` for a matched vertex.  Every such causal arc decreases
the even integer, so these arcs form a directed acyclic graph.  For a
nonisolated even vertex, let `ell(e)` be its least odd neighbor.  If `ell(e)`
was already used, the canonical parent

```text
parent(e)=owner(ell(e))
```

is earlier than `e`.  Along a nonterminal parent chain, both even values and
least-neighbor labels decrease strictly.

An augmenting path can reach a free odd only by leaving this decreasing
causal structure through a preference ascent.  In particular, a length-three
path

```text
e_0 -- o_1 -- e_1 -- f
```

with unmatched endpoints satisfies

```text
e_1<e_0,       o_1=c(e_1)<f.                       (11)
```

This is a precise description of the greedy allocation defect `d_N`.  It is
not a mechanism for the majority term in (3).

## 5. Why injective charging fails

For every common factor core `C`, the admissible vertices

```text
{C p in S_N}             and             {C q r in S_N}
```

form a complete bipartite fiber.  Disjointness of the extra primes is
automatic: if `p=q` or `p=r`, the two endpoint values have ratio equal to an
odd prime, at least `3`, and cannot both lie in one factor-two collar.

The empty-core fiber is especially transparent.  Every collar prime is
adjacent to every collar semiprime.  Thus the greedy consumes any selected
primes in increasing order; unused primes form a terminal suffix.  An
unmatched prime implies that every semiprime was matched, while an unmatched
semiprime implies that every collar prime was consumed.  This large biclique
is a routing hub, not a sparse exceptional structure.

More generally, one owned odd vertex can block unboundedly many later evens.
The census found extreme core reuse: at `N=20000,50000,100000`, only
`43,70,104` chosen common cores supported `2010,5053,10102` matches.  Cores
of rank at most one supported respectively `92.7%,89.8%,87.9%` of them.
Individual owners blocked as many as `24` unmatched evens, and individual
chosen odds blocked as many as `32` unmatched odds.  No bounded-congestion
charge follows from the core geometry.

The obvious attempt to reverse this fanout into a rigid primorial-core
obstruction also fails.  If `m=C a b` lies in `[alpha N,N]` with
`alpha>1/2`, then every prime

```text
a b/(2 alpha)<p<=a b,       p not dividing C,
```

gives another collar vertex `C p`.  Indeed
`C p>m/(2 alpha)>=N/2` and `C p<=m<=N`.  For `a b` tending to infinity, the
prime number theorem supplies

```text
(1-1/(2 alpha)+o(1)) a b/log(a b)-omega(C)
```

such choices.  Large extra factors therefore create many mixed-core escape
edges rather than a trapped positive-density family.

There is also a decisive abstract control.  On the complete bipartite graph
`K_(E,O)` with the same value orders, the greedy has perfect expansion,
depth-one blocker stars, no Hall or allocation loss, and terminal unmatched
vertices.  Nevertheless,

```text
R_g=|E-O|.                                           (12)
```

which can be arbitrarily large in the control model.  Dense blockers,
decreasing dependency chains, and terminality therefore do not imply
cancellation of the color imbalance.

## 6. Exact memory-bounded certificates

The companion script
`src/mobius_greedy_dependency_audit.py` verifies (1)--(4), constructs the
greedy matching without materializing the dense graph, and searches for
vertex-disjoint length-three augmentations.  The selected exact checkpoints
are:

| `N` | `M(N)` | greedy `R_g` | `D_g` | disjoint length-3 paths | residual after paths |
|---:|---:|---:|---:|---:|---:|
| 10,000 | -23 | 23 | 0 | 0 | 23 |
| 20,000 | 26 | 28 | 1 | 1 | 26 |
| 50,000 | 23 | 27 | 2 | 2 | 23 |
| 100,000 | -48 | 56 | 4 | 4 | 48 |
| 200,000 | -1 | 27 | 13 | 13 | 1 |

At every checkpoint, disjoint paths remove all of `D_g` and leave exactly
`|M(N)|`.  For example, at `N=20000` the certified path is

```text
19803 -- 10311 -- 10353 -- 19635,
```

with factor sets

```text
(3,7,23,41) -- (3,7,491) -- (3,7,17,29)
             -- (3,5,7,11,17).
```

The middle edge belongs to the greedy matching; flipping the path increases
its size by one.

Unmatched vertices are not low-degree anomalies.  At `N=20000,50000,100000`
their degree ranges were respectively `73--1530`, `106--3608`, and
`189--8880`.  Multi-source alternating searches found only shallow priority
inversions: all targets were reached in three edges at the first two
checkpoints; at `N=100000`, all but one were reached in three and the last in
five.

Across 400 exact checkpoints at or below `100000`, the largest observed
greedy defect was `12`.  Unmatched vertices appeared near the upper endpoint,
but not as a literal suffix: many matched vertices followed the first
unmatched one.  The largest observed terminal age was `1367` at `N=94460`,
or `4.448 sqrt(N)`.  These are diagnostics, not asymptotic evidence.

Reproduce the retained certificates with

```text
python3 src/mobius_greedy_dependency_audit.py \
  10000 20000 50000 100000 200000 --show-paths

python3 -m pytest -q src/test_mobius_greedy_dependency_audit.py
```

The script caps ordinary runs at `N=200000` and caps the length-three scan,
so failure to find all paths is reported as a failed certificate search, not
misstated as a theorem.  The `N=200000` audit used approximately `49 MB` peak
resident memory on the present machine.

## 7. Verdict

The alternating dependency forest successfully explains and repairs greedy
inefficiency, but that is not the RH-bearing quantity.  The proposed route

```text
blocker expansion -> few unmatched -> Mertens cancellation
```

breaks at its second arrow.  Blocker expansion controls `h_N+d_N`; after it
is exhausted, the unmatched mass is exactly `|M(N)|`.

A direct theorem `R_g(N)=O(N^(1-delta))` would still be valuable and would
give a new zero-free half-plane.  But it now requires an independently
countable arithmetic property containing every *majority-side* residual,
such as a proved power-short clearing interval.  Establishing that property
would itself be the new Mertens cancellation theorem; it does not follow from
the dependency forest, core expansion, or better matching.

Accordingly:

- further augmenting-path optimization and larger scans are parked;
- the exact decomposition and polynomial compression are retained as useful
  structural results;
- the named greedy may be revived only with a new unsigned arithmetic
  invariant for the majority residual, not another matching argument.
