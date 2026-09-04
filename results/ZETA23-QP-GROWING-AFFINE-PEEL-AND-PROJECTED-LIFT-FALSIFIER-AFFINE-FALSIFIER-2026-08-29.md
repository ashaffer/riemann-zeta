# Growing affine-peel and projected-lift falsifier

Date: 2026-08-29

## Scope

This is a finite diagnostic, not an asymptotic theorem.  Every modulus `q`
below is prime and every shell mask consists of actual prime powers.  The
support inherits the documented floating nearest-integer trust boundary of
`build_four_cycle_core`; after the support is materialized, the affine ranks,
partitions, graph incidences, component invariants, A4 ledgers, and displayed
certificates use exact integer or rational arithmetic.

Two independent tests were run:

1. A completion-consistent pre-factorial peel, separately in each oriented
   four-color fibre.  It repeatedly takes the largest lex-first affine line
   with at least three unassigned completion points, then the largest
   lex-first affine plane pinned by three noncollinear unassigned points.
   Remaining fibres have size at most two and alone are serialized into A2.
2. An all-five-distinct ordered-pair graph audit.  At every left and right
   anchor it extracts all projected neighbor lines with at least three points,
   tests the carrier/witness sequence, tests the forced product lift, and
   performs a deterministic local line peel on both graph sides.

The replay scripts are:

- `results/verify_zeta23_qp_growing_affine_peel_adversarial_affine_falsifier.py`
- `results/verify_zeta23_qp_projected_neighbor_lift_conflict_affine_falsifier.py`

## Pre-factorial peel ledger

Here `direct` is the number of physical completions before factorialization,
`aff` is the number peeled directly, `atoms` counts ordered distinct
completion pairs before and after the peel, and `Haff` is the exact affine
Carleson load.  `dirs` gives the maximum number of distinct primitive
completion directions incident to one color before/after peeling.

| q | U | D | direct | aff | source/residual atoms | Haff/D | patch reuse | dirs source/residual | max residual component (V,E) | degree product | A4 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11801 | 35 | 94 | 42310 | 174 | 3228 / 2880 | 72/94 | 8 | 131 / 107 | 3,2 | 2 | 4 |
| 11801 | 36 | 94 | 48206 | 210 | 3964 / 3544 | 108/94 | 12 | 157 / 122 | 3,2 | 2 | 4 |
| 11801 | 44 | 94 | 87116 | 798 | 10992 / 9336 | 288/94 | 32 | 352 / 259 | 5,4 | 4 | 12 |
| 25013 | 40 | 135 | 129848 | 126 | 5604 / 5340 | 36/135 | 4 | 90 / 84 | 3,2 | 2 | 4 |
| 50021 | 40 | 189 | 274534 | 84 | 6328 / 6148 | 36/189 | 4 | 64 / 56 | 3,2 | 2 | 4 |
| 100003 | 40 | 265 | 682894 | 42 | 8588 / 8492 | 18/265 | 2 | 58 / 58 | 3,2 | 2 | 4 |

At the requested `q=25013,U=40` fixture there are no rich completion lines.
There are 42 three-point planes: they peel 126 of 129848 direct completions
(0.0970%) and remove 264 of 5604 ordered factorial atoms (4.71%).  The
residual has 5340 atoms in 298 A2 cells and 5290 components.  Its components
are forests, the maximum component has three vertices and two atom-edges,
the maximum left-degree/right-degree product is 2, and its exact unit A4
upper ledger is 4 versus `D^2=18225`.

The resonant `q=11801,U=44` fixture is the hostile color-reuse example.  All
266 selected patches are three-point planes and none is a line.  They peel
798 of 87116 direct completions (0.916%) and remove 1656 of 10992 factorial
atoms (15.07%).  Color 5981 lies in 32 different selected plane geometries.
Each three-point/four-color plane charges it 9, giving

```
H_aff(5981) = 32 * 9 = 288 > D = 94.
```

The same color has 352 distinct primitive source directions.  Thus a literal
constant-one claim `H_aff <= D`, or a proof that silently treats one color as
belonging to only one affine direction, is false for this canonical peel.
This is not an asymptotic disproof of `H_aff << D`: at fixed `U=40`, the
observed ratio falls from the resonant small-q range to `36/135`, `36/189`,
and `18/265` as q grows.  The residual remains extremely sparse throughout:
no tested residual component has a cycle, no component degree product exceeds
4, and A4 never exceeds 12; in particular no `D^2` kill test fired.

## Projected-neighbor audit

Counts below aggregate left and right anchors.  `nonaff` counts rich projected
lines whose unique carrier witnesses are not affine in the primitive line
parameter.  `nonplane` counts lines whose corresponding source triples have
affine rank three.  `dual selected` counts graph edges assigned by both the
left and right deterministic local peels.

| q | U | graph edges | rich lines | nonaff | nonplane | lift failures | same-side crossings | dual selected |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 12853 | 12 | 15112 | 20 | 16 | 16 | 0 | 0 | 0 |
| 25013 | 12 | 30920 | 24 | 24 | 24 | 0 | 0 | 4 |
| 50021 | 12 | 97144 | 52 | 48 | 48 | 0 | 0 | 0 |
| 25013 | 24 | 133512 | 488 | 468 | 472 | 0 | 4 | 20 |
| 11801 | 35 | 110264 | 2712 | 2528 | 2568 | 0 | 44 | 712 |
| 11801 | 44 | 158536 | 5814 | 5458 | 5558 | 0 | 204 | 1602 |
| 25013 | 40 | 372536 | 4748 | 4596 | 4656 | 0 | 44 | 768 |
| 50021 | 40 | 1000840 | 7340 | 7108 | 7200 | 0 | 28 | 928 |

### Exact non-affine-witness certificate

At `q=11801,U=44`, fix the left anchor `(b,B)=(4831,4993)`.
The three projected neighbors and their unique witnesses are

```
t    (d,D)        x
0    (6121,5923)  6947
12   (6481,6271)  6561
22   (6781,6561)  6271
```

They lie on the exact primitive line

```
-29 d + 30 D = 181,
(d,D) = (6121,5923) + t(30,29).
```

The witnesses are not affine in t, since

```
(6561-6947)*22 = -8492 != -8112 = (6271-6947)*12.
```

Nevertheless the multiplicative lifts are

```
(xd,xD,x) =
(42522587,41147081,6947),
(42521841,41144031,6561),
(42523651,41144031,6271),
```

and all obey the forced homogeneous plane equation

```
-29(xd) + 30(xD) - 181x = 0.
```

The six actual source triples are

```
(6947,4831,6121), (6947,4993,5923),
(6561,4831,6481), (6561,4993,6271),
(6271,4831,6781), (6271,4993,6561).
```

They are not contained in one ordinary affine plane: the affine 3-by-3
minor from the first four displayed points is exactly `-750384`.  This is a
concrete counterexample to the implication

```
rich projected neighbor line
    => affine witnesses
    => one ordinary affine source-coordinate patch.
```

It does not counterexample the product-lift statement; that identity held on
all 21198 rich lines in the eight-fixture ladder (zero failures).

### Exact dual-anchor assignment certificate

Still at `q=11801,U=44`, the all-five-distinct graph edge

```
left anchor  = (4861,4871)
right anchor = (6733,6719)
carrier      = 6277
```

is selected by both independent canonical endpoint peels.  Its left packet is

```
line -d+D=-14:
((6733,6719),6277), ((6793,6779),6221), ((6871,6857),6151),
```

while its right packet is

```
line -e+E=10:
((4861,4871),6277), ((5011,5021),6089), ((5041,5051),6053).
```

The packets meet in the displayed central edge but are otherwise different.
There are 1602 such double assignments in this fixture after deterministic
same-anchor peeling, and 1634 edges belong to rich lines at both endpoints
before peeling.  Hence independent local endpoint rules do not define a
completion-consistent partition.  A global orientation or allocation rule is
logically necessary.

## Conclusion for the affine-compression route

The naive sought theorem is false in two distinct places:

1. projected affine geometry does not pull back to affine witness/source
   geometry; and
2. independent local packet selection is not completion-consistent across
   the two graph endpoints.

The surviving credible theorem has to be different: operate in the exact
homogeneous product lift, choose packets with one global edge-allocation rule,
and prove a mask-sensitive Carleson estimate after that allocation.  The
finite residual data are compatible with such a theorem but do not prove it.
The computations give no dangerous residual component or A4 core, while the
single-color direction reuse shows exactly why a per-direction local summation
cannot supply the missing global estimate.

## Replay

```bash
python3 results/verify_zeta23_qp_growing_affine_peel_adversarial_affine_falsifier.py
python3 results/verify_zeta23_qp_projected_neighbor_lift_conflict_affine_falsifier.py
```
