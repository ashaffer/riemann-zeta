# QP self-orbit adversarial lab: total support, false order laws, and scattered cycles

**Date:** 2026-08-26  
**Verdict:** the strongest finite pattern found is that the **entire short
self-orbit support** has only `O(D)` edges.  No tested hard-window or actual
prime fixture violates this, and every dense example is an affine packet.
This is evidence, not a proof.  Simple substitutes for the missing theorem
(Monge order, interval neighbourhoods, or absence of scattered cycles at all
fixed cutoffs) are false.

The most important scale distinction is:

```text
q=25013 critical hard D = 135;
first genuine all-distinct prime C6 found at literal hard D = 8344.
```

Thus the new C6 is a real obstruction to an unrestricted cycle-to-line
classification, but it is **not** a counterexample at the critical window.

---

## 1. Kernel audited

Fix a primitive anchor and write its physical centre orbit as

```text
P_t=(b_t,B_t),                 |t|<=D.
```

The endpoint associated with `P_j` is its exact reflection `(B_j,b_j)`.  On
the actual selected row set `A`, the symmetric non-tangent kernel is

```text
X(t,j)=1  iff  there is x in A with
 |8 x b_t B_j-q^3|<=qD,
 |8 x B_t b_j-q^3|<=qD,
 b_t B_j != B_t b_j.                              (1.1)
```

Pair uniqueness makes the row, when it exists, unique.  Define

```text
E=sum_(t,j) X(t,j),
W(0)=sum_(t:X(t,0)=1) sum_j X(t,j).                (1.2)
```

Here “entire kernel” means all physical orbit tokens in the theorem's short
label range `|t|<=D`, not the irrelevant `q^2`-sized unrestricted orbit.

### Exact complete scans

| carrier / anchor | `D` | physical tokens | incident | `E` | `E/D` | `W(0)` | largest incident line |
|---|---:|---:|---:|---:|---:|---:|---:|
| integer `q=200000`, `(100000,100001)` | 371 | 743 | 144 | 432 | 1.16442 | 271 | 144 |
| integer `q=200000`, `(108551,111297)` | 371 | 256 | 10 | 16 | 0.04313 | 7 | 3 |
| integer bad strip `(92519,87756)` | 371 | 289 | 25 | 32 | 0.08625 | 1 | 4 |
| integer bad `b`-order `(116417,118578)` | 371 | 245 | 22 | 26 | 0.07008 | 5 | 3 |
| actual prime powers `q=10604226`, `(5302109,5302103)` | 2548 | 14 | 5 | 14 | 0.00549 | 10 | 5 |

The richest total support is wholly collinear: all 144 incident vertices of
the central integer example lie on one physical affine line.  The broad and
bad-digital-strip anchors have many available orbit tokens but very few
actual hard-window edges.  This is the empirical invariant which survived
the hostile scan:

```text
large total E  =>  affine coherence                       (finite evidence),
scattered support => E much smaller than D                (finite evidence).
```

The root mask correlates strongly with degree in these examples.  The
central root selects 18 neighbours whose degrees sum to 271; the broad root
selects four whose degrees sum to seven.  This is not promoted to an
asymptotic statement.

### Multilevel tangent obstruction in one fixed chart

The old multilevel full-integer construction does not falsify the stronger
total-edge conjecture.  Fix its step `h` and use anchor

```text
gamma=(m,m-h).
```

For translations `t` and levels `ell`, the centre and reflected-source
labels are exactly

```text
h(h+t),                         0,-h ell.           (1.3)
```

At `m=20000000,L=10,h=11,D=2048L^2=204800`, all eleven centres and eleven
sources remain in `[-D,D]`, and all `11^2=121` edges of their biclique obey
the literal product windows.  Symmetry therefore gives the rigorous lower
bound

```text
E >= 242 = 0.00118164 D.                            (1.4)
```

This is a coherent tangent packet of linear-or-smaller size, not a
superlinear total-support example.  Varying `h` in the multilevel
construction changes the anchor slope and hence changes the self-orbit
chart; those patches cannot be charged to one fixed-anchor `E`.

---

## 2. The rooted ratio rises above `0.73`, but stays coherent

For the full integer shell and central primitive root
`(q/2,q/2+1)`, exact rooted scans give:

| `q` | `D=floor(q^(16/33))` | root degree | max neighbour degree | `W` | `W/D` |
|---:|---:|---:|---:|---:|---:|
| 200000 | 371 | 18 | 18 | 271 | 0.73046 |
| 300000 | 452 | 20 | 20 | 344 | 0.76106 |
| 500000 | 579 | 23 | 23 | 437 | 0.75475 |
| 1000000 | 811 | 27 | 27 | 631 | 0.77805 |
| 2000000 | 1135 | 32 | 32 | 890 | 0.78414 |
| 3000000 | 1381 | 36 | 36 | 1100 | **0.79652** |
| 4000000 | 1588 | 38 | 38 | 1241 | 0.78149 |
| 6000000 | 1933 | 42 | 42 | 1537 | 0.79514 |

So the previous `0.73` was not a limiting constant.  No growth beyond a
constant multiple of `D` appeared, and the entire rooted mass in this
family lies on the two parallel reflected token lines.  The data therefore
strengthen the need to prove “excess implies packet”; they do not suggest a
scattered extremizer.

---

## 3. Exact counterexamples to easy order laws

For the legal full-integer root

```text
q=200000, D=371, gamma=(108551,111297),
```

the anchored adjacency rows are

```text
-162 : {-77,0}
-150 : {0}
-135 : {-235,0}
 -77 : {-162,0}.                                   (3.1)
```

With rows and columns in numerical order, (3.1) violates both possible
orientations of the binary Monge inequality:

```text
A(-162,-77)+A(-150,0)=2 > 1
  =A(-162,0)+A(-150,-77),

A(-162,-235)+A(-150,-77)=0 < 1
  =A(-162,-77)+A(-150,-235).                       (3.2)
```

Interval-neighbourhood replacements also fail.

* At `q=3500,D=52,gamma=(1681,1689)`, the numerical token order is
  `[0,1,8,10,16]`, while row `1` has neighbours `{0,8,16}`: three runs.
* At `q=200000,gamma=(116417,118578)`, sorting physical orbit vertices by
  first coordinate gives `[-85,143,-185,-179,-222,0]`; row `-179` has
  neighbours `{0,-222,-185,-85}`: again three runs.

Thus neither convex bipartite adjacency, Monge/anti-Monge structure, nor a
two-interval theorem is available without extra peeling.

In a deterministic 3927-root broad sample at `q=200000`, 3926 supports were
both `C4`-free and `C6`-free; the largest rectangle-free rooted value was
only `W=7`.  Sparse broad masks are common, but the finite exceptions above
show that bounded alternation is not an exact law.

---

## 4. High-girth route: what survives and what fails

The cycle search imposed all of the following:

1. every coordinate value on the cycle is distinct;
2. all carrier rows are distinct and disjoint from the vertex coordinates;
3. tangent edges are removed;
4. no three reflected pair-points are affine-collinear.

### Critical full-integer searches

Exhaustive searches of the relevant two-cores found no qualifying `C6`:

| `q` | graph vertices | two-core vertices | qualifying `C6` |
|---:|---:|---:|---:|
| 3500 | 38066 | 538 | 0 |
| 6000 | 102986 | 996 | 0 |
| 10000 | 308982 | 3176 | 0 |
| 15000 | 693922 | 6036 | 0 |
| 20000 | 1213218 | 9174 | 0 |

The analogous `C8` search also returned zero for `q=3500,6000,10000,15000`.
These are finite exhaustive statements inside the displayed graphs, not a
high-girth theorem.

### Actual prime cycles beyond the critical window

For the actual prime-power shell at `q=25013`, the older smooth-cutoff graph
at `U=12` has no qualifying `C6` or `C8`.  In the edge filtration through
`U=22`, exhaustive double-precision search found its first qualifying C6 at
bottleneck

```text
U = 21.518440849497075.                             (4.1)
```

Its alternating reflected pair-points are

```text
(10501,10631), (12281,12433), (11953,12101),
(12119,12269), (12601,12757), (14561,14741),        (4.2)
```

and its carriers are

```text
14983, 13163, 13339, 12653, 10531, 12637.          (4.3)
```

All 18 displayed integers are distinct primes.  No three points in (4.2)
are collinear, and its six edges have six distinct primitive directions.
The exact largest cubic residual is

```text
208700629,
ceil(208700629/25013)=8344.                         (4.4)
```

Consequently (4.2)--(4.3) is an exact literal hard-window C6 at the minimal
integer threshold `D=8344`, but

```text
8344 / floor(25013^(16/33)) = 8344/135 > 61.8.     (4.5)
```

A similarly all-distinct prime `C8` was found by `U=40`; it has eight
distinct directions and exact literal threshold `D=13964`.  These fixtures
disprove the unconditional claim that every short prime cycle is forced by
role repetition or one affine line.  They leave the critical-window
cycle-to-packet route alive.

The numerical threshold (4.1) belongs to the logarithmic smooth diagnostic.
Primality, distinctness, collinearity, directions, residual (4.4), and the
literal `D` statement are all checked by integer arithmetic.

---

## 5. Exact Fourier expansion and why Parseval does not close it

There is an exact character expansion which retains every mask.  Let `T` be
the finite physical token set, `A` the actual selected rows, and choose an
integer modulus `M>2R_*`, where `R_*` bounds the absolute values of both
cubic residuals on `A x T x T`.  Put

```text
I=[-qD,qD],  L=2qD+1,
Ihat(h)=sum_(r in I) e_M(-hr).                     (5.1)
```

Then, exactly,

```text
X(t,j)=1/M^2 sum_(h,k mod M) Ihat(h) Ihat(k)
 e_M(-(h+k)q^3)
 sum_(x in A) e_M(8x(h b_t B_j+k B_t b_j)).        (5.2)
```

Token and row masks have not been completed to ambient boxes.  The zero
frequency contributes

```text
|A| L^2/M^2                                      (5.3)
```

per masked pair, or `|T|^2` times (5.3) to the total sum.  With a natural
`M` of order `q^3`, this is tiny; zero frequency is not the obstruction.

Parseval gives the valid identities

```text
sum_h |Ihat(h)|^2 = M L,
sum_u |sum_(x in A)e_M(ux)|^2 = M |A|.             (5.4)
```

But the sampled frequency

```text
u=8(h b_t B_j+k B_t b_j)                           (5.5)
```

is bilinear in `(t,j)` and has large collision families on the principal
affine packet.  Standard separated-frequency large-sieve hypotheses are
therefore absent.  Cauchy--Parseval alone pays the same radial square-root
loss which underlies the existing `D^(3/2)` ceiling; it gives no strict
exponent gain.

Nor does fixed-row residue inversion remove that loss.  For fixed `x~q`,

```text
r=8xp-q^3,                 r == -q^3 (mod 8x).      (5.6)
```

The interval `[-qD,qD]` contains `Theta(D)` representatives of this one
class because its length is `2qD` while `8x` is of order `q`.  Retaining the
radial quotient leaves a `D`-component vector; discarding it loses the hard
cutoff.  Thus a legal BP normalization does not by itself prove the desired
total-edge theorem.  A genuinely new mask-sensitive collision or
radial-quotient estimate is still required.

---

## 6. Status

```text
exact orbit reflection and one-orbit cross-products:       PROVED;
exact masked Fourier expansion (5.2):                      PROVED;
zero mode harmless at natural exact modulus:               PROVED;
Monge / anti-Monge adjacency:                              FALSE;
two-interval neighbourhood theorem:                       FALSE;
all fixed-cutoff prime cycles peel to repetitions/lines:   FALSE;
critical-window scattered C6/C8 in tested fixtures:        NOT FOUND;
total short-kernel E << D q^o(1):                          OPEN;
sharp four-cycle theorem:                                  NOT PROVED.
```

Reproduction:

```text
PYTHONPATH=src pytest -q \
  src/test_qp_self_orbit_adversarial_lab.py \
  src/test_qp_scattered_token_search.py

cd lean/weilcert
lake env lean QPScatteredTokenOrbitReflection.lean
```

The recorded run passed **10 Python tests** and the Lean file's **4 exact
theorems**.

Implementation:

```text
src/qp_self_orbit_adversarial_lab.py
src/test_qp_self_orbit_adversarial_lab.py
src/qp_scattered_token_search.py
lean/weilcert/QPScatteredTokenOrbitReflection.lean
```
