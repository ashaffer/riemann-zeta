# QP affine compression: literal candidate and falsifier audit

**Date:** 2026-08-29  
**Source:** materialized `q=25013`, `U=40` positive-factorial A2 data  
**Verdict:** no uniform affine-compression theorem is proved.  Natural exact
affine packet classes capture at most `1.071%` of this source.  A rigorous
finite packet-or-sparse-remainder split does pass A4, but the fixture has no
certified A2 excess and therefore does not test the desired conditional
inverse theorem.

## 1. Exact geometry before factorialization

The source has

```text
repeated oriented color fibres:             2,712
completion occurrences in those fibres:    5,468
multiplicity 2 / 3 / 4:              2,670 / 40 / 2
ordered off-diagonal factorial atoms:       5,604
```

Exact rational Gaussian elimination gives

```text
2-point fibres of affine rank 1:            2,670
3-point fibres of affine rank 2:               40
4-point fibres of affine rank 3:                2
fibres with >=3 collinear completions:           0
```

After reversal is identified, the `5,604` ordered atoms give `2,802`
unoriented secants.  Their canonical affine-line Pluecker keys are all
different.  Thus two distinct unoriented atoms never lie on the same exact
completion line in this fixture.

This immediately falsifies an unconditional theorem that asks rich affine
lines to retain a positive fraction of all repeated-completion mass.  If
two-point lines are declared packets instead, every atom is captured but
there is one line per unoriented atom, so there is no compression.

## 2. Candidate direction extractors

Candidates were intersected with the signed `(A,B)` cells before replaying
their Schur and A4 loads.  A group of size one is counted as uncompressed
remainder.

| packet key | all cell pieces | nontrivial pieces | retained atoms | singleton remainder | max piece | unit-balance A4 |
|---|---:|---:|---:|---:|---:|---:|
| exact primitive four-carrier direction | 5,580 | 8 | 32 | 5,572 | 10 | 4 |
| primitive row and column directions, relative scale forgotten | 5,556 | 12 | 60 | 5,544 | 10 | 4 |
| sign cone, non-affine control | 490 | 370 | 5,484 | 120 | 102 | 6 |
| one packet per whole cell, non-affine control | 308 | 240 | 5,536 | 68 | 186 | 4 |

The target is

```text
D0=floor(q^(16/33))=135,             D0^2=18,225.
```

For the optimistic row/column-direction extractor, the twelve genuinely
nontrivial packets retain

```text
60/5,604 = 1.0706638... of the mass,
compression inside the retained part = 60/12 = 5,
maximum overlap = 1,
largest packet = 10 atoms,
maximum squared Schur amplitude = 2,
exact worst extracted-packet A4 value = 2.
```

The largest raw cell has `186>D0` atoms but splits into `177` optimistic
direction pieces; its largest piece has only ten atoms, a fraction `5/93`.
Raw cardinality above `D0` therefore does not imply a dominant affine
direction, even on this literal source.  It is not the normalized A2 excess
hypothesis.

The two non-affine controls are important falsifiers of the *test*.  A
data-fitted sign cone or even the entire cell compresses dramatically and
still passes A4 because this finite support has tiny row and column degrees.
Consequently A4 plus a Schur certificate cannot decide that a packet is
genuinely affine; the admissible packet geometry must be fixed in advance.

## 3. Maximal planes before ordered pairs

A nontrivial affine two-plane is required to contain three noncollinear
completion points.  The forty rank-two triples give forty planes.  Each
rank-three four-point fibre gives four distinct triangle planes.  Hence

```text
pinned plane candidates:                         48
direct completion incidences in them:           144
unique direct completion mass:                  128 / 5,468
unique factorial mass in their union:           264 / 5,604
maximum direct/factorial overlap:                  3 / 2
```

Thus the union of every pinned plane sees all multiplicity-three and
multiplicity-four fibres, but only `4.7109%` of the factorial mass.  Giving
the four triangle planes in a rank-three fibre half of each common ordered
pair is an exact positive allocation.

A disjoint stopping rule that chooses one maximal plane in each fibre of
multiplicity at least three retains

```text
direct mass:                         126 / 5,468
factorial mass:                      252 / 5,604
factorial remainder:                      5,352.
```

If a plane pinned by only two points is admitted, one plane per fibre retains
`5,466/5,468` direct occurrences.  That apparently strong answer is
tautological: it uses `2,712` planes and does not aggregate the two-point
sector.

## 4. Strongest literal packet-or-remainder split

Combine:

1. all pinned planes, using half allocations in each rank-three four-point
   fibre; and
2. every nontrivial parallel primitive row/column direction in the remaining
   multiplicity-two sector.

The exact result is

```text
structured unique atoms:                         316
pre-fragment labels:             48 planes + 12 direction-cell groups
signed-cell packet fragments:                    292
packet allocations:                              340
overlap histogram:                     292 once, 24 twice
maximum packet size / squared amplitude:        10 / 2
unit-balance structured A4:                      9/2
final singleton-direction residual:            5,288
unit-balance residual A4:                           4
```

The large residual is still `94.36%` of the source.  Its largest cell has
`176>D0` atoms, but the finite A4 certificate is only `4`, versus the target
`18,225`.  Equivalently the resulting positive-form coefficient is at most
`2`, versus the required scale `D0=135`.  It is therefore a raw-cardinality
core, not a dangerous core in the relevant finite factorial norm.

This is a rigorous finite **packet-or-dispersive-remainder** certificate.  It
is not an affine compression theorem: almost all atoms go to the harmless
remainder, and no uniform estimate for future `q` follows.

## 5. What the actual theorem must say

The literal audit rules out unconditional mass capture as the target.  A
credible uniform theorem must instead be conditional on the true post-A1
operator excess:

```text
V(R,Y)=||R^*Y||op / sqrt(D) >= q^delta.
```

The current `qp-a2-packet-cell/v1` object stores positive factorial atoms,
masks, allocations, and A4 supports.  It stores neither the residual map
`R`, the common dual test `Y`, nor `V(R,Y)`.  It also cannot record how much
of `||R*Y||op` a candidate packet captures.  Therefore this source cannot
verify or falsify the stopping-time assertion `(6.0b)` in the joint research
program.

The next schema/theorem iteration needs:

1. `R`, `Y`, and an exactly replayable normalized excess;
2. a predeclared proof type for each packet (rich line/plane, or a genuinely
   new parallel two-point merger), rather than an arbitrary Schur grouping;
3. captured dual operator mass, not merely captured atom count; and
4. a packet-free alternative for a direction-diverse residual.

The finite evidence favors a dichotomy of that form.  It does not support a
theorem saying that all or a fixed fraction of the factorial mass must be
affinely compressed.

## 6. Replay

All counts, affine ranks, Pluecker line keys, allocations, overlaps, Schur
bounds, and A4 loads are checked by

```text
results/verify_zeta23_qp_affine_compression_falsifier_affine_falsifier.py
```

Run with

```bash
PYTHONPATH=src python3 \
  results/verify_zeta23_qp_affine_compression_falsifier_affine_falsifier.py
```

The verifier reports `PASS`.
