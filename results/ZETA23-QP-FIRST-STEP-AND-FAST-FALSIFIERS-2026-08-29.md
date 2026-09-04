# QP first step and fast falsifiers

**Date:** 2026-08-29

**Question:** Does the first concrete Blomer--Pascadi (BP) interface, or the
packet-participation alternative, survive contact with a literal QP cell?

**Status:** This audit neither proves nor disproves the sharp four-cycle
bound.  It closes the currently specified **scalar black-box BP adapter**,
leaves a genuinely mask-sensitive vector BP theorem open, and finds no
counterexample to packet participation on the operator-level fixtures that
can presently be constructed.

## 0. Outcome

The first step produced three decisive facts.

1. A literal all-prime four-completion cell has a joint off-axis mask of
   exact rank three.  It cannot be represented by one product
   `alpha(left) beta(right)`.
2. Even after passing to exact reciprocal coordinates, the two columns of
   one literal rectangle have different multipliers `lambda`.  Thus the
   rectangle is not one fixed-`(modulus,lambda)` Kloosterman matrix, the
   input accepted by the scalar BP theorem.
3. Conditional on freezing one scalar layer, the published proof removes
   coefficient identities at its first spectral-norm step, before the
   discriminant is formed.  Its later correlation weights are correlations
   of analytic cutoffs, not the four physical QP masks.

Consequently, “import BP and preserve the masks when the discriminant
appears” starts too late.  Any viable BP route needs a new vector/masked
estimate at the spectral step itself.

The packet fast falsifier went the other way: every available exact
operator-level instance satisfies the proposed participation scale, often
by a large margin.  But no existing A2 extractor emits all the data needed
to evaluate the A4 potential on the actual positive factorial pieces.

## 1. Frozen literal cell

The exact all-prime fixture has

```text
q=5,868,182, D=1,912,
14 completion chains, 10 off-axis chains.
```

In its Bezout coordinates the four center tokens and partner tokens are

```text
centers  =((-216,35),(-180,29),(-72,11),(-36,5)),
partners =((216,-35),(180,-29),(72,-11),(36,-5)).
```

The exact support matrix is

```text
0 0 1 1
0 0 1 1
1 1 0 1
1 1 1 0.
```

Its rank is exactly three: the first two rows agree, while the bottom-right
`3 x 3` minor has determinant two.  Its nuclear-to-Hilbert--Schmidt ratio is

```text
(sqrt(17)+1)/sqrt(10)=1.620068247057....
```

This finite constant is not an asymptotic obstruction.  It is a rigorous
falsifier of the claim that the literal cell is already one separable
scalar coefficient pair.

An independent mixed-remainder fixture has `delta*h=-2592` and `D^2<q`.
For its two columns the exact reciprocal conversion gives, at the same
prime modulus `m=2,934,079`,

```text
(v_1,lambda_1)=(180,2160),
(v_2,lambda_2)=(144,2592).
```

Both shifts are units and both congruences hold, but
`lambda_1 != lambda_2`.  A completion pair generally creates four such
layers at two moving row moduli.  Hence there is no legal map from one QP
rectangle to one scalar BP kernel without conditioning and then paying for
reconstruction.

For a single frozen unit layer the Fourier identity is exact:

```text
T_lambda(f,g)
 = m^(-2) sum_(u,w mod m) g_hat(u) f_hat(w) S(lambda*u,w;m).
```

This identifies the BP variables, but it does not reconstruct the coupled
four-mask cell after the layers have been separated.

## 2. Where the published BP proof loses the masks

[BP Theorem 1.1 and Proposition 3.1](https://arxiv.org/html/2607.24311)
apply to a fixed modulus, a fixed scalar Kloosterman multiplier, two scalar
coefficient vectors, and interval cutoffs.  In equation (3.4), the proof
uses

```text
|alpha^T K beta| <= ||alpha||_2 ||beta||_2 ||K||.
```

That operation forgets which entries came from each of the four QP masks.
The later `z_i(h_i)` are autocorrelations of BP's cutoff weights.  They are
not transforms of `S_11,S_12,S_21,S_22`.  The trace discriminant is therefore
available only after the physical mask structure has already disappeared.

There are two distinct obstructions, in order:

1. before BP, the QP columns do not share a fixed `lambda`;
2. inside a frozen BP layer, equation (3.4) scalarizes away the masks.

This corrects the earlier program: the proposed new theorem must begin
before the discriminant, rather than modifying only the character-sum end
of the proof.

## 3. Fast scalar-conversion falsifiers

At the QP exponent `D=q^(16/33)`, BP's dominant black-box saving is

```text
q^(-19/1056).
```

The local four-cycle ledger requires `q^(-1/66)`, leaving only

```text
q^(1/352)=q^(3/1056)
```

for all conversions.  The following positive exponents are the factors by
which the listed adapter still misses the required target.

| scalar adapter | best certified miss |
|---|---:|
| direct length-`D` block triangle inequality, one unrestricted Fourier side | `q^(269/1056)` |
| balanced BP with optimized padded block length `H=q^(29/51)` | `q^(265/1122)` |
| asymmetric BP Theorem 5.5 plus block triangle inequality | `q^(2/9)` |
| full-length opened-kernel Parseval | `q^(1/33)` |

For the first line, the exact factorization infimum for a flat Fourier
point mass is `sqrt(q/D)=q^(17/66)`.  The lower bound allows arbitrary
overlapping or signed length-`D` interval decompositions, by
`l1 <= sqrt(D) l2`; it is not an artifact of consecutive blocks.  On the
literal finite cell the conversion cost is `39.1783...`, while the entire
allowed BP conversion factor is only `1.04527...`.

The optimized balanced calculation permits a common padded length
`H=q^alpha`.  The exact objective is minimized at `alpha=29/51`; it still
misses by `q^(265/1122)`.  The asymmetric theorem improves that black-box
miss to `q^(2/9)`.  Elementary full-length Parseval is substantially better
than either, but it still fails by `q^(1/33)`.

A separate Paley four-hard-window integer fixture forces projective/HS loss
`D^(1/4)=q^(128/1056)`, exceeding the conversion budget by
`q^(125/1056)`.  This is a method-level obstruction from the hard-window
and Bezout identities alone; it is not an actual-prime counterexample.

These tests close scalar intervalization, scalar rank-one triangle
decomposition, and their balanced/asymmetric BP optimizations.  They do
**not** lower-bound the loss of every possible actual-prime hybrid or a
proof-level vector theorem.  The global A1 infimum is therefore not known
to have a positive-power loss.

## 4. Packet-participation falsifier

For packet supports `L_t,R_t`, amplitudes `a_t`, and positive weights
`lambda_t`, put

```text
L=max_u sum_(t:u in L_t) lambda_t,
R=max_v sum_(t:v in R_t) a_t^2/lambda_t.
```

For probability weights `alpha,beta` on the two vertex sets, set

```text
p_t=sum_(u in L_t) alpha_u,
r_t=sum_(v in R_t) beta_v.
```

Cauchy--Schwarz gives the exact dual certificate

```text
L R >= (sum_t a_t sqrt(p_t r_t))^2.
```

When `L_t=R_t` and the amplitudes are constant, concentration at a vertex
of maximum participation `Delta`, together with `lambda_t=a_t`, proves

```text
exp(inf Phi)=(a Delta)^2
```

exactly.  No numerical optimizer tolerance is involved.

The densest available actual-prime operator abstraction has

```text
q=25,013, D_0=135, 535 carrier packets,
372,536 incidences, Delta=10, a=1,
exp(inf Phi)=100, D_0^2=18,225.
```

Thus its ratio is `4/729`.  Exact-integer `q^2` carrier and residual-matching
fixtures also pass.  Conversely, scalable Latin and Sidon-Cayley controls
attain `D^2` exactly, so the proposed threshold is sharp for the abstract
mechanism.

The qualification is decisive: no repository fixture currently supplies a
literal A2 output containing all of

1. packet id and term membership in the nonnegative cell decomposition;
2. oriented ordered-pair supports `L_t,R_t`;
3. a certified local amplitude `a_t` for the same positive factorial form;
4. overlap multiplicities and the unpacketized remainder;
5. the associated `q,D`, signed cell, and four retained masks.

Therefore the available packet tests are rigorous operator-level stress
tests, not a legal evaluation of A4 on the proposed A2 decomposition.  A4
remains open.

See the full [packet-participation audit](ZETA23-QP-PACKET-PARTICIPATION-FAST-FALSIFIER-LIT-FEJER-2026-08-29.md).

## 5. Decision-tree update

The scalar BP branch should be demoted.  More block-length optimization is
not the next experiment: even the best elementary scalar adapter misses by
`q^(1/33)`, and the literal cell also has moving multipliers and joint masks
that those exponent calculations omit.

Two credible branches remain:

1. **Vector BP:** formulate a centered direct-sum/square-function estimate
   at the analogue of BP equation (3.4), jointly retaining the four masks,
   moving `(modulus,lambda)` layers, Fourier axes, and conductor sectors.
   This is genuinely new mathematics, not a black-box corollary of BP.
2. **Packet route:** make A2 emit the five-field schema above, then run the
   exact A4 primal/dual optimizer on growing literal cells.  The present
   evidence is favorable, and a counterexample would be cheap and decisive.

The highest-information next step is branch 2: implement the literal A2
serialization and immediately rerun A4.  It is a finite, falsifiable gate.
The vector BP theorem remains the analytic fallback if the packet route
fails or saturates for a structurally interpretable reason.

## 6. Reproduction and verification

The A1 replay is

```text
results/verify_zeta23_qp_a1_fast_falsifiers.py
```

and the packet replay is

```text
results/verify_zeta23_qp_packet_participation_fast_falsifier_lit_fejer.py
```

Both run cleanly.  The focused QP/BP regression suite reports

```text
38 passed.
```

