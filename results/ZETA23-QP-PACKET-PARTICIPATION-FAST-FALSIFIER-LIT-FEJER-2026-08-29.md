# QP packet-participation fast falsifier

**Date:** 2026-08-29

**Scope:** exact/certified evaluation of the packet-overlap potential on
packetizations already recoverable from repository fixtures.  This is not an
A2 packet extractor and does not prove A4 or the sharp four-cycle bound.

## 0. Verdict

No existing legal fixture falsifies

```text
inf_x Phi(x) <= 2 log D + o(log q).
```

Two actual-prime-power data sets admit a conservative **abstract operator**
instantiation, and both pass their finite target without any extra factor:

1. grouping the actual ordered-pair incidence graph by its stored carrier;
2. treating each actual `q^2` short residual matching block as one symmetric
   norm-two packet.

The densest audited carrier fixture, `q=25013,U=40`, has the following exact
optimizer value conditional on the materialized support (for the safe
amplitudes `a_t=1`):

```text
exp(inf Phi)=100,
inf Phi=log 100,
D_0=floor(q^(16/33))=135,
100/D_0^2=4/729=0.0054869684....
```

Thus it is very far from a participation counterexample.  The abstract
Latin and Sidon-Cayley controls saturate the natural threshold exactly, so
the mechanism has no general improvement beyond the stated scale.

The important negative finding is that the repository still contains no
literal output of the proposed A2 extractor with all of the data needed to
instantiate A4 on the positive factorial form.  In particular, the dynamic
affine components do not carry `L_t,R_t,a_t`, and the tangent and `q^2`
fixtures carry norms for different operators.

## 1. Exact certificate, not a floating-point optimizer

Let

```text
L(lambda)=max_u sum_(t:u in L_t) lambda_t,
R(lambda)=max_v sum_(t:v in R_t) a_t^2/lambda_t.
```

For any probability measures `alpha,beta` on the left and right vertices,
put

```text
p_t=sum_(u in L_t) alpha_u,
r_t=sum_(v in R_t) beta_v.
```

Then Cauchy--Schwarz gives the reusable dual lower certificate

```text
L(lambda)R(lambda)
 >=(sum_t a_t sqrt(p_t r_t))^2.                       (1.1)
```

All evaluated actual fixtures have `L_t=R_t=S_t` and one constant certified
amplitude `a`.  If

```text
Delta=max_v #{t:v in S_t},
```

take `alpha=beta` to be the point mass at a vertex attaining `Delta` in
`(1.1)`.  This gives the lower bound `a^2 Delta^2`.  The choice
`lambda_t=a` gives both maximum loads equal to `a Delta`.  Therefore

```text
exp(inf Phi)=(a Delta)^2                              (1.2)
```

exactly.  No numerical convex-solver tolerance enters the reported values.

## 2. Actual-prime-power operator-level fixtures

### 2.1 Carrier packets in the ordered-pair incidence graph

`PairIncidenceGraph` stores the ordered left/right pair codes, the weighted
matrix, and the carrier of every edge.  For a fixed carrier `b`, product
uniqueness maps an ordered row pair to one ordered color pair and conversely.
The resulting packet matrix is a weighted partial permutation.  Its entries
are products of two averages of unit-modulus phases, so

```text
||T_b||_(2->2)<=1.                                   (2.1)
```

On both audited `q=25013` smooth fixtures, the finite product symmetry check gives
literal set equality `L_b=R_b`.  With the safe amplitude `a_b=1`, `(1.2)`
therefore applies.

| fixture | packets | ordered-pair edges | `Delta` | `exp(inf Phi)` | `D_0^2` | ratio |
|---|---:|---:|---:|---:|---:|---:|
| actual `q=25013,U=12` | 462 | 30,920 | 4 | 16 | 18,225 | `16/18225` |
| hostile actual `q=25013,U=40` | 535 | 372,536 | 10 | 100 | 18,225 | `4/729` |

Here `D_0=floor(q^(16/33))=135`.  The smooth-core geometric parameter
includes the fixed cutoff constant and is larger (`15509.94...` at `U=40`),
so comparison with `D_0` is the stricter finite normalization.  It is not an
asymptotic statement about participation growth.

The smooth-core builder uses floating-point nearest-integer and logarithmic
cutoff decisions.  Hence these two rows are exact convex certificates for
the materialized finite graphs, but retain the source fixture's diagnostic
support-selection trust boundary.  The exact-integer `q^2` builder removes
that boundary.  Grouping its hard-window generic atoms by carrier gives:

| exact fixture | packets | ordered-pair edges | `Delta` | `exp(inf Phi)` | `D_0^2` | ratio |
|---|---:|---:|---:|---:|---:|---:|
| hard-window `q=4751` | 3 | 24 | 1 | 1 | 3,600 | `1/3600` |
| hard-window `q=25013` | 1 | 8 | 1 | 1 | 18,225 | `1/18225` |

These two rows are proof-grade finite integer-support certificates.  Their
extreme sparsity means they are not useful asymptotic stress tests.

This is an instance of the abstract full-operator lemma only.  Carrier
packets decompose the incidence matrix `H`; they are not the affine/Hankel
packets output by the proposed A2 stopping time, and they do not partition
the nonnegative factorial cell pieces `P_t` required in A4.

### 2.2 Actual `q^2` residual matching blocks

Every selected short residual block is a vertex-disjoint union of
all-distinct triangle atoms.  Its symmetric block matrix is a direct sum of
`K_3` adjacency matrices and hence has norm exactly two.  Its left and right
single-node supports coincide.  Applying `(1.2)` with `a=2` gives:

| `q` | `D_0` | blocks | support incidences | `Delta` | `exp(inf Phi)` | `D_0^2` | ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 151 | 11 | 2 | 6 | 2 | 16 | 121 | `16/121` |
| 4,751 | 60 | 6 | 21 | 2 | 16 | 3,600 | `1/225` |
| 25,013 | 135 | 12 | 39 | 2 | 16 | 18,225 | `16/18225` |

These are genuine prime-power/product-window fixtures, but their vertices
are single shell nodes.  A4 uses ordered-color-pair supports of positive
quartic packet pieces.  Therefore the table is a valid abstract-overlap
stress test, not a literal A4 evaluation.

## 3. Existing abstract/hostile controls

The fixtures in `test_qp_collective_dyadic_gate.py` can be optimized
exactly:

| fixture | exact `exp(inf Phi)` | certificate |
|---|---:|---|
| 100 pairwise-disjoint packets, `a_t=7` | 49 | concentrate `(1.1)` on any packet; take `lambda_t=7` |
| 100 packets with one common left vertex and disjoint right vertices, `a_t=7` | 4,900 | uniform right dual measure; equal `lambda_t` |
| amplitudes 6 and 10, disjoint left vertices and one common right vertex | 136 | optimize the left dual weights proportional to `a_t^2`; take equal `lambda_t` |

The last test's checked choice `(lambda_1,lambda_2)=(3,5)` gives 160, so it
is a valid ledger test but is not the optimum.  The exact optimum is 136.

Two scalable hostile families are especially informative.

* In the cyclic Latin two-star fixture of degree `d`, carrier packets are
  permutation maps, and each ordered pair belongs to all `d` carriers of
  its group.  Thus `exp(inf Phi)=d^2`.  With `D=d`, the target is attained
  exactly.
* In the parabolic Sidon-Cayley fixture over `F_p`, its `p` translation
  layers are permutation packets supported on every vertex.  Thus
  `exp(inf Phi)=p^2`; with `D=p`, this again attains the target exactly.

For the full-integer tangent/Hankel fixture, merging the entire coherent
grid into one packet and using the proved symmetric fourth-trace bound gives
the safe one-packet amplitude `a=2L^2`.  With `D=100L^2`,

```text
exp(inf Phi)=4L^4=D^2/2500.                           (3.1)
```

This confirms that the coherent tangent obstruction is harmless once it is
merged.  It says nothing about global participation among many sparse
actual-prime packets.

## 4. Exact data still missing for literal A4

To run the requested falsifier on an actual A2/A4 packet family, one file
must provide, for a fixed `q`, signed dyadic cell, and four Cartesian masks:

1. a packet id `t` for every extracted piece and exact term membership, with
   nonnegative pieces that cover or partition the relevant cell form;
2. oriented ordered-color-pair supports
   `L_t subset S_11 x S_12` and `R_t subset S_21 x S_22`;
3. a certified `a_t` satisfying
   `P_t(z)<=a_t sqrt(U_t(z) V_t(z))` for every coefficient vector, with the
   same normalization and scalar kernel as the endpoint;
4. overlap/partition multiplicities if one physical term belongs to more
   than one packet, and the exact remainder left for A3/A5;
5. the associated `D,q` and retained joint QP masks.

No current actual packet fixture contains this tuple.  Concretely:

* `DynamicAffineComponent` stores labels, points, direction, determinant
  step, and capacity, but no ordered-pair supports or local amplitude.
* `affine_packet_vertices` returns only the union of left/right vertices
  whose neighborhoods are affinely collinear.  It does not identify packet
  ids, attach each edge to a packet, or certify `a_t`.
* The `q=200003` additive-tangent diagnostic stores completion pairs and
  their mass, but no covering packet family or A4 amplitudes.
* The tangent-grid fixture stores triple matching classes and one coefficient
  vector; its merged global bound does not encode participation among a
  family of extracted packets.
* The Fejer packet-pair square-function test has explicit toy integer
  supports, but its datum is sumset overlap and packet cardinality, not an
  A4 local amplitude or an actual QP packetization.
* The 323-completion translation fixture stores secant-cell occupancy, not
  color-pair supports or amplitudes.

Accordingly, there is no growing legal A2-output fixture on which failure of
`(6.3)` can presently be certified.  The fast falsifier passes every
available abstraction but does not reduce the status `A4: OPEN`.

## 5. Reproduction

The isolated verifier added for this audit is

```text
results/verify_zeta23_qp_packet_participation_fast_falsifier_lit_fejer.py
```

Run:

```bash
PYTHONPATH=src python3 \
  results/verify_zeta23_qp_packet_participation_fast_falsifier_lit_fejer.py
```

It reconstructs all table entries from existing fixture builders, checks
partial-permutation incidence, checks literal left/right support equality,
and prints the exact integer optimum and target before converting their
ratio to decimal.
