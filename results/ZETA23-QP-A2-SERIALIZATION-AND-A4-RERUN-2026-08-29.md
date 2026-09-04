# QP A2 serialization and A4 rerun

**Date:** 2026-08-29

**Status:** the missing A2 data contract is implemented and A4 has been
rerun on the literal positive factorial form.  The fixed-secant baseline
passes exactly.  This is not the open affine/Hankel A2 inverse theorem and
does not prove the sharp four-cycle bound.

## 0. Verdict

The previous A4 audit used operator surrogates because no object retained
the positive completion-pair terms, packet membership, physical ordered
supports, certified local bounds, overlap, remainder, and four masks at the
same time.  The new serializer retains all of them and rejects incomplete or
tampered data.

On the full materialized `q=25013`, cutoff `U=40` actual-prime-power core:

```text
generic ordered completion-pair atoms:       5,604
signed (A,B) cells:                            308
exact-secant packets:                        5,596
largest packet:                                  2 atoms
remainder inside the declared generic sector:    0
maximum left packet load:                         2
maximum right packet load:                        2
max_cell inf_lambda L(lambda)R(lambda):            4
strict normalized target D0^2:               18,225
ratio:                                        4/18,225
```

The value four is exact, not merely a feasible upper bound: `lambda_t=1`
gives the upper bound, while a point-mass dual certificate on two common
packets gives the matching lower bound in a worst cell.

Thus A4 passes this legal finite baseline overwhelmingly.  The important
qualification is that the packetization is almost singleton: 5,596 packets
for 5,604 atoms.  It validates serialization, fixed-layer reconstruction,
and participation bookkeeping.  It is not evidence that the still-unknown
affine extractor compresses a genuinely dense dangerous core.

## 1. What is serialized

For a fixed oriented color matrix

```text
C=(c11,c12;c21,c22)
```

and two distinct physical carrier completions

```text
X=(a1,a2,b1,b2),  X'=(a1',a2',b1',b2'),
```

one source atom records

```text
term id,
C, X, X',
A=a1*a2'-a2*a1',
B=b1*b2'-b2*b1',
exact nonnegative source weight.
```

No D4 canonicalization is applied: the orientation that determines

```text
left vertex =(c11,c12),
right vertex=(c21,c22)
```

is retained.

Each serialized cell additionally records:

1. schema version, source identity, and a SHA-256 source-manifest digest;
2. `q`, the exact literal hard-window radius, and the exponent-normalized
   A4 degree parameter;
3. the signed dyadic `(A,B)` cell and the four positional Cartesian masks;
4. exact rational allocations from every source atom to its packets;
5. explicit remainder allocations and their reasons;
6. the number of packets containing each atom, so overlaps cannot be
   silently erased;
7. every packet's physical `L_t,R_t`, Schur row/column sums, and certified
   `a_t^2`.

JSON rationals are normalized numerator/denominator pairs.  The entire JSON
payload has a second SHA-256 hash.  Deserialization verifies both hashes and
then replays all arithmetic certificates.

## 2. Completeness and certificate checks

The validator enforces the following identities exactly.

```text
source_weight(term)
 =sum_packet allocated_weight(term)
  +remainder_weight(term).
```

It also checks:

- unique occurrence ids and unique packet ids;
- off-diagonal completions and recomputed nonzero secants;
- membership in the declared signed cell and all four masks;
- eight-distinct genericity for each displayed rectangle;
- the literal integer inequalities
  `|8abc-q^3| <= q*hard_window_radius`;
- packet supports equal the projections of their allocated terms;
- declared overlap multiplicities equal the actual allocation counts;
- weighted sparse row and column sums reproduce the declared Schur bound;
- exact-secant packets do not mix secants or repeat either ordered-pair
  vertex.

A4 refuses a cell with positive remainder.  Fractional allocations and
overlapping candidate packets are supported, but their allocations must sum
back to every source coefficient exactly.

## 3. The first legal packetization

Inside each signed dyadic cell, source atoms are grouped by their exact
carrier secant `(A,B)`.  For one such packet, the color-pair relation is
replayed as a weighted partial matching.  If `K_t` is its coefficient
matrix, the serializer computes

```text
a_t^2
 =max_left sum_right |K_t|
  *max_right sum_left |K_t|.
```

Every packet in the full fixture has `a_t^2=1`.  This imports only the
already proved fixed-secant matching structure.  It does not assume the
unproved aggregation over varying secants.

The exact A4 primal certificate evaluates

```text
L=max_u sum_(t:u in L_t) lambda_t,
R=max_v sum_(t:v in R_t) a_t^2/lambda_t.
```

For this fixture `lambda_t=1` gives `L<=2`, `R<=2`, hence `LR<=4` in every
cell.  The implemented exact dual check accepts rational probabilities
`alpha,beta` and rational `s_t` satisfying

```text
s_t^2 <= a_t^2 p_t r_t,
p_t=sum_(u in L_t) alpha_u,
r_t=sum_(v in R_t) beta_v,
```

and certifies the lower bound `(sum_t s_t)^2`.  A worst cell has two packets
through the same left/right point; point masses and `s_t=1` on those packets
give the matching lower bound four.

## 4. Literal sources and scale separation

### 4.1 Compact all-prime fibre

The frozen compact fixture is

```text
q=25013,
C=(13103,12659;10799,10433),
X1=(10903,13229,13693,14173),
X2=(11483,13933,13001,13457),
X3=(11681,14173,12781,13229),
X4=(11743,14249,12713,13159).
```

Every node is prime and each `C+Xi` has eight distinct entries.  Its largest
integer residual is `342,803,781`, so the least literal hard-window radius
is `13,706`.  Its twelve ordered atoms occupy eight signed cells.  Exact
serialization gives twelve fixed-secant packets and exact worst A4 value
four.

### 4.2 Full actual-prime-power core

The source pipeline is

```text
build_four_cycle_core
 -> enumerate_rectangles
 -> completion_groups_from_generic_rectangles
 -> ordered X != X' atoms
 -> signed cells
 -> exact-secant packets.
```

The finite counts are

```text
unoriented generic rectangle records:      150,672
oriented color fibres:                     127,092
repeated color fibres:                       2,712
multiplicity 2 / 3 / 4 fibres:       2,670 / 40 / 2
ordered off-diagonal atoms:                  5,604
```

The largest signed cell contains 186 atoms in 185 exact-secant packets.  Its
unit-balance load product is only two.  Across all cells, the exact worst
optimized value is four.

Two different `D`-scales must not be conflated.  The least exact integer
hard-window radius for the materialized `U=40` source is `15,506`.  The A4
stress test uses

```text
D0=floor(q^(16/33))=135
```

and target `D0^2=18,225`, which is the stricter exponent-normalized
comparison used in the prior audits; the fixed cutoff factor is normally
absorbed into `q^epsilon`.  Both values are serialized explicitly.

The core builder uses floating nearest-integer/log-cutoff decisions.  After
the support is materialized, every serialized term, residual inequality,
allocation, mask, Schur bound, primal bound, and dual bound is checked with
exact integer or rational arithmetic.  The large-core conclusion retains
the builder's support-selection trust boundary.  The compact fibre avoids
any ambiguity about the displayed arithmetic.

The existing exact `q^2` residual-matching fixtures induce no rectangles and
hence no positive factorial atoms.  They are not legal A4 sources; they have
not been relabelled as such.

## 5. What changed in the research decision

The earlier statement “A4 cannot be run because A2 emits no legal data” is
now resolved at the interface level.  A4 can consume, validate, hash,
round-trip, and certify an exact positive packet cover.

The rerun finds no fixed-secant participation obstruction.  But it also
shows why this does not close A2: exact secants create almost one packet per
atom.  They do not classify or compress polynomial all-plus excess across
varying secants.

The next mathematical test is therefore precise:

1. attach affine/Hankel packet candidates to these same term ids;
2. allocate a certified positive portion of each term to them;
3. measure retained mass, overlap, and the explicit unpacketized remainder;
4. rerun the unchanged A4 primal/dual verifier;
5. test packet-free unconditionality only on the serialized remainder.

If affine packets leave a polynomial remainder, require polynomial overlap,
or make A4 exceed `D^2`, that route is falsified without changing the target
or the data model.

## 6. Implementation and verification

- A2 schema, extractor, JSON, and validation:
  `src/qp_a2_packet_serialization.py`
- Exact A4 primal/dual certificates and family summary:
  `src/qp_a4_serialized_participation.py`
- Contract and adversarial tests:
  `src/test_qp_a2_packet_serialization.py`
- Full literal replay:
  `results/verify_zeta23_qp_a2_serialized_a4.py`

The focused regression suite reports

```text
100 passed.
```

