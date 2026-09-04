# QP pair-state Schatten and Smith spectral probe

**Date:** 2026-08-22  
**Verdict:** the diagonal-tensor representation is exact and computationally
cheap on the actual prime-power cores, but its unmasked leading spectrum is
not the open pair energy.  At `q=25013`, identical completions contribute
`63.56%` of the fourth mass, repeated-row/column pairs contribute `36.39%`,
and genuine off-diagonal completion pairs contribute only `0.0499%`.

After that exact subtraction, the genuine flat-weight mass is small in all
four audited cores and has no rank-one secants.  It is not concentrated in
one tangent or Smith class.  The first exact additive-tangent pair occurs at
`q=200003`, but supplies only `2.84%` of the genuine mass.  These are finite
diagnostics, not an asymptotic estimate or an arbitrary-coefficient theorem.

---

## 1. Exact diagonal-tensor identity

For each color `c`, let

```text
A_c(a,b)=kappa(a,b,c).
```

Two-coordinate uniqueness makes every `A_c` a partial-permutation matrix:
each row and each column contains at most one supported entry.  For a real
dephased kernel and nonnegative color magnitudes put

```text
B_z=sum_c |z_c| (A_c tensor A_c).                   (1.1)
```

The implementation compresses zero pair states, without changing any
nonzero singular value.

A directed completion is

```text
X=(a1,a2,b1,b2)
```

whose four supported cells have oriented color matrix

```text
C(X)=(c11,c12;c21,c22).                             (1.2)
```

Write

```text
rho(X)=prod_ij kappa(ai,bj,cij).                    (1.3)
```

Direct expansion of `tr((B_z* B_z)^2)` gives the finite identity

```text
||B_z||_S4^4
 =sum_C |sum_{X:C(X)=C} rho(X)|^2
        |z_c11 z_c12 z_c21 z_c22|.                 (1.4)
```

This is an algebraic identity for every finite real pair-unique triple
system; it does not depend on residual pinning or asymptotics.  The code
assembles the two sides independently: the left from a sparse Gram product,
the right by directed grid enumeration.

### Exhaustive Latin fixture

For the order-three cyclic Latin system, `z=(1,2,3)`, and unit kernel:

```text
pair-state matrix                         9 by 9
tensor entries                                27
directed completions                           81
oriented color matrices                        27
S4 mass from sparse Gram                     3942
S4 mass from completion squares              3942
discrepancy                                      0.       (1.5)
```

Thus the identity is checked with exactly representable integer data before
being applied to the smooth actual cores.

---

## 2. Swap-sector decomposition

Simultaneous factor swap commutes with every `A_c tensor A_c`.  Moreover,
the equal-coordinate pair states are invariant.  Hence `B_z` splits into
three orthogonal blocks:

```text
diagonal pair states,
symmetric off-diagonal pair states,
antisymmetric off-diagonal pair states.             (2.1)
```

Consequently

```text
||B_z||_S4^4
 =||B_diag||_S4^4+||B_sym||_S4^4+||B_alt||_S4^4.   (2.2)
```

This is theorem-grade finite linear algebra, not a numerical observation.
On the Latin fixture, each of the three summands is exactly `1314`, with
singular values

```text
6, sqrt(3), sqrt(3).                                (2.3)
```

In every actual fixture below, the symmetric and alternating blocks are
real diagonal-sign gauge equivalent:

```text
B_alt=diag(epsilon_row) B_sym diag(epsilon_col),
epsilon in {+1,-1}.                                 (2.4)
```

The probe certifies (2.4) by a bipartite sign traversal with zero conflicts
and zero edge-ratio error.  This equivalence is fixture-specific; it is not
asserted for every partial-permutation family.  It does show that the
exterior sector supplies no cancellation gain on these cores.

---

## 3. Actual `q=25013` identity and the diagonal warning

The actual prime-power fixture uses shell width `0.2`, cutoff `U=12`, and
quadrature order `32`.  There are

```text
nodes                                      535
triples                                   4002
live colors                                518
compressed tensor entries                39052
directed completions                     79778
oriented color matrices                  70906.       (3.1)
```

For the flat vector on the 518 live colors, the two sides of (1.4) are

```text
0.2268108837303188,
0.2268108837303169,                        (3.2)
```

with discrepancy `1.9e-15`.

The completion-pair decomposition is

| class | mass | fraction of full S4 |
|---|---:|---:|
| identical completion | `0.1441717866` | `63.5648%` |
| off-diagonal, but a repeated row or column | `0.0825258979` | `36.3853%` |
| genuine off-diagonal pair | `0.0001131992` | `0.049909%` |

Thus the leading singular value of the full `B_z` belongs to the diagonal
block.  It says almost nothing about the open genuine pair term.

The block ledger is

| block | S4 mass | top singular value |
|---|---:|---:|
| diagonal | `0.1441717866` | `0.35757598` |
| symmetric off-diagonal | `0.0413195486` | `0.09203830` |
| alternating off-diagonal | `0.0413195486` | `0.09203830` |

The two exterior matrices have `17525` supported entries and `14943`
nontrivial sign-gauge components.  Most components are tiny.  Their combined
fourth mass contains both the easy repeated-row/column mass and the small
genuine residue; merely deleting diagonal pair *states* does not isolate the
open term.

---

## 4. Four-modulus scaling scan

The following table uses the same cutoff, shell, flat-live-color
normalization, and quadrature order.  `genuine` is the exact positive mass
after deleting identical completions and every pair in which either
completion repeats a row or column.  Counts include directed orientations.

| `q` | `D` | live colors | full S4 | genuine | genuine/full | ordered genuine pairs | secant Smith classes |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 25013 | 4652.98 | 518 | `2.26811e-1` | `1.13199e-4` | `4.99091e-4` | 96 | 6 |
| 50021 | 6511.25 | 988 | `1.87776e-1` | `2.75050e-5` | `1.46478e-4` | 72 | 6 |
| 100003 | 9110.37 | 1863 | `1.34013e-1` | `2.24002e-5` | `1.67149e-4` | 168 | 12 |
| 200003 | 12749.31 | 3492 | `1.06960e-1` | `1.19076e-5` | `1.11328e-4` | 288 | 20 |

A four-point log-log fit labels the normalized genuine mass as approximately
`q^-1.00`, but the successive doubling ratios are

```text
0.243, 0.814, 0.532.                                (4.1)
```

That variation is too large to treat the fitted exponent as a law.  The
normalization also changes with the number of live colors.  The unnormalized
positive genuine mass, obtained by multiplying by the square of that count,
has fitted exponent about `+0.83`, again with large local variation.  Neither
fit is evidence for a uniform coefficient theorem.

The top block singular values are:

| `q` | diagonal top | symmetric top | alternating top | all-five `H` top |
|---:|---:|---:|---:|---:|
| 25013 | `0.357576` | `0.0920383` | `0.0920383` | `2.094756` |
| 50021 | `0.324472` | `0.0680335` | `0.0680335` | `2.138461` |
| 100003 | `0.271123` | `0.0578214` | `0.0578214` | `2.347666` |
| 200003 | `0.239002` | `0.0424897` | `0.0424897` | `2.389839` |

Descriptive four-point fits give exponents `-0.20`, `-0.36`, and `+0.07`,
respectively.  The `H` norm remains order one in this scan, far below its
available degree bound; its top modes live on small components rather than a
growing bulk mode.

---

## 5. Tangent and Smith classification

### 5.1 Completion secants

For two completions of the same color matrix, put

```text
E=M(X)-M(X'),
M(a1,a2,b1,b2)=(a1*b1,a1*b2;a2*b1,a2*b2).          (5.1)
```

The probe records the Smith pair

```text
d1=gcd(E11,E12,E21,E22),
d2=|det E|/d1.                                      (5.2)
```

At `q=25013`, the 96 directed genuine pairs occupy six classes:

```text
(2,709884),
(4,137812), (4,172776), (4,267240), (4,536520),
(6,104328).                                         (5.3)
```

Each class contains 16 directed pairs.  No rank-one secant occurs.  Across
the four moduli, the class counts are `6,6,12,20`, and the rank-one count is
zero throughout.  The residue is therefore becoming more, not less,
Smith-dispersed in this small scan.

### 5.2 Exact additive tangent

The exact additive tangent test is

```text
X-X'=(t,t,-t,-t).                                   (5.4)
```

Its directed-pair counts are

```text
q=25013,50021,100003:       0,
q=200003:                   8.                      (5.5)
```

The `q=200003` packet comes from

```text
C=(113063,113051;113051,113039),       det C=-144,
X=(93997,94007,94099,94109),
X'=(94099,94109,93997,94007),
X-X'=(-102,-102,102,102),
E=(0,-1020;1020,0),
Smith(E)=(1020,1020).                               (5.6)
```

Including all directed orientations, its mass is `3.38124e-7`, or `2.84%`
of the genuine mass at that modulus.  It is also the only pair admitted by
the `5 sqrt(D)` near-square test.  Thus exact tangent extraction identifies
a real coherent packet, but it does not account for the other `97.16%`.

### 5.3 Row-pair/color-pair incidence modes

For an incidence edge from `(a,a')` to `(c,c')`, define

```text
h=a*c-a'*c',
R=(a a'; c' c),             det R=h.                (5.7)
```

The edge Smith invariants are `gcd(a,a',c,c')` and `|h|` divided by that
gcd.  In the top all-five-distinct `H` mode, all material influence has first
Smith invariant one.  The shift profiles are

| `q` | median `|h|` | 90th percentile `|h|` | fraction with `|h|<=D` | dominant Smith class |
|---:|---:|---:|---:|---:|
| 25013 | 432 | 642 | `1.000` | `(1,432)` |
| 50021 | 1160 | 1976 | `1.000` | `(1,1452)` |
| 100003 | 390 | 688 | `1.000` | `(1,546)` |
| 200003 | 288 | 318 | `1.000` | `(1,288)` |

No principal `h=0` edge carries mode influence.  The large finite modes are
primitive, nonprincipal, small-shift packets.  This is compatible with a
spectral treatment which extracts a tangent range, but it supplies no
large-sieve estimate by itself.

---

## 6. What the probe changes

1. **The Schatten representation is real and exact.**  It is not merely an
   analogy for completion energy.

2. **The raw fourth norm has the wrong leading modes.**  Any analytic use
   must include a nonbacktracking/masked subtraction of identical and
   repeated-row/column completion pairs.  Ordinary positive Schatten
   control spends almost all of its budget on terms already known to be
   harmless.

3. **Exterior antisymmetry is gauge-trivial on the audited cores.**  Passing
   from the symmetric to the alternating pair space does not reduce the
   singular spectrum.

4. **The genuine residue is not one tangent class.**  It has no rank-one
   secants, its Smith support grows across the scan, and the first exact
   additive packet is only a small fraction.  A useful trace formula would
   have to average uniformly over Smith levels rather than isolate a single
   exceptional orbit.

5. **The incidence modes remain localized and order one.**  Their Smith
   first invariant is primitive and their shifts lie well inside the `D`
   window.  The finite data show no growing spectral obstruction, but flat
   coefficients cannot test the required worst-case coefficient vector.

The natural next computational step is a genuinely masked pair-state
operator whose trace is exactly the genuine completion-pair mass and whose
Smith layers remain visible.  The present positive `B_z` supplies the
ambient representation and exact subtraction ledger, not that final
operator.

---

## 7. Reproduction and trust boundary

Focused exact and regression tests:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_four_cycle_pair_state_spectral_probe.py
```

Full four-modulus JSON scan:

```bash
PYTHONPATH=src python3 -m qp_four_cycle_pair_state_spectral_probe \
  25013 50021 100003 200003 --quadrature-order 32
```

The implementation is

```text
src/qp_four_cycle_pair_state_spectral_probe.py.
```

Integer supports, completion counts, partial-permutation checks, secant
Smith invariants, tangent identities, sector support, and sign-gauge
consistency are exact.  Smooth kernel values, Schatten totals, singular
values, and eigenvectors use double precision.  The independent S4 identity
errors are at roundoff scale.  No finite scan, fitted exponent, or mode
profile is promoted to an asymptotic claim.

