# QP sharp four-cycle: two-sided closeout of the phase-jet route

**Date:** 2026-08-25  
**Binary verdict:** the sharp four-cycle bound has **not** been proved and
has **not** been disproved.  The best unconditional project estimate remains

```text
tr((A_z^* A_z)^2) << D^(9/8+o(1)) ||z||_2^4.
```

The attempted scalar phase-jet completion can nevertheless be closed
decisively: its unrestricted full-threshold maximum-degree assertion is
false, and exact bounded-probe recovery of the virtual cubic fingerprint is
impossible in the high primitive tail.  Neither obstruction violates the
desired Bessel bound.  Both point to the same surviving theorem: a
mask-preserving **vector-valued** supported-harmonic intertwining estimate at
the weaker threshold `eta=D^(-7/48)`.

That theorem is not proved here.  Consequently there is no honest route from
the present lemmas to the sharp four-cycle conclusion.

## 1. The two exact no-go results

### 1.1 The virtual cubic cannot be synthesized at bounded cost

At a primitive tangent `(p,d)`, the integral phases satisfying

```text
Phi'(t_0)=Phi''(t_0)=0
```

form one primitive cubic ray.  Its two Fejer coordinates have size at least
`p^3/2`.  Therefore any integer synthesis from physically supported
characters `|h|,|k|<=H` which produces a nonzero cubic character has

```text
coefficient mass >= p^3/(2H).
```

At the residual floor this is

```text
p^3/H >= D^(61/160).
```

Thus products, determinants, exterior powers, or finite differences cannot
extract the canonical cubic character with `D^o(1)` tensor degree while
remaining well defined modulo the integer Newton lattice.  The lifted cubic
fingerprint is an inverse invariant, not a physically available bounded
probe.

### 1.2 The unrestricted full-threshold degree theorem is false

At `C=Q^2`, `S_0=2Q`, take

```text
h=(p+d)^2*t,       k=(p-d)^2*(t+1),       m=p^2.
```

These are regular interior stationary modes at
`a_0=Q(p+d)/p`.  Their action and first completion derivative are integers,
so both disappear in the physical Newton quotient.  Their first visible
coordinate is

```text
R=Q*J''=2*p^3*t*(t+1)/(2*p*t+p+d).
```

With

```text
D^(77/160)<=p<=sqrt(H/64),
p/8<=d<=p/4,
t=floor(H/(16p^2)),
```

all frequencies are physically supported and all saddles stay in a compact
collar.  There are `D^(17/16+o(1))` distinct nonreflection tangents.  A
pigeonhole bin of `R`-width

```text
W=D^(1+epsilon),       0<epsilon<1/48,
```

contains `D^(1+epsilon-o(1))` modes whose second and third differences are
too small to give correlation `D^(-1/6)`.  Hence the unrestricted assertion

```text
full-threshold major-arc degree <<D^(1+o(1))
```

is false even away from endpoints, the exact zero-dual locus, folds, and
reflection.

This is a dual-mode theorem.  It does not assert that every tangent in the
bin is populated by a primal off-axis product-band point, so it does not
refute a mask-restricted theorem or the four-cycle conjecture.

## 2. Why neither no-go is a counterexample to the bound

The near-zero-dual cloud retains quantitative quadratic separation.  If
`r=|R-R_0|`, its local density and normalized pair correlation satisfy

```text
#{nu: |R_nu-R_0|<=r} <<D^o(1)*(sqrt(H)+r),
rho(r)<<sqrt(r/Q)+sqrt(Q)/(N*sqrt(r)).
```

Dyadic summation gives the absolute Gram-row bound

```text
max_nu sum_mu |<u_nu,u_mu>| <<D^(7/8+o(1)).
```

This is below the desired squared Bessel scale `D` by `D^(1/8)`.  The cloud
defeats only the coarse rule which charges every correlation above one fixed
threshold by one.

No scalable primal four-cycle family above `D^(1+o(1))` was obtained.  The
exact residual fingerprint remains injective up to reflection, and the
finite residual scan still has no nonreflection lifted collision.  These are
evidence, not a proof of the sharp estimate.

## 3. The weaker gap-closing ledger survives every new obstruction

The sharp global estimate does not require the full pair threshold in this
local ledger.  It is enough to repair the current operator deficit using

```text
eta_close=D^(-7/48),
K<=D^(7/6+o(1)),
Delta_close<=D^(49/48+o(1)).
```

The newly audited exceptional sizes are all below that ceiling:

```text
near-zero-dual unresolved R-window:       D^(47/48+o(1));
one oriented primitive-direction fiber:   D^(329/480+o(1));
fixed-Q full-harmonic signature fiber:     D^(41/48+o(1));
off-cluster Schur term eta_close*K:         D^(49/48+o(1)).
```

The full-harmonic statement uses the elementary implication

```text
||j*theta||_T<=eta for every 1<=j<=cH
       => ||theta||_T<<eta/H.
```

After the bounded reciprocal wrap branches are split, a fixed-Q signature
cell has physical carrier width

```text
Q*eta/H+B/P
 <<D^(41/48)+D^(329/480).
```

There are only `O(1)` product-error choices over each carrier.  Thus the
arithmetic information in the supported harmonic vector is sufficient in
principle, even though one scalar jet is not.

## 4. The exact theorem still missing

What remains is not another fingerprint calculation.  It is the following
analytic statement.

> **Mask-preserving vector harmonic intertwining.**  Decompose every retained
> physical completion block into supported harmonic bundles without losing
> the original coefficient `l2` normalization.  For arbitrary selected
> product-band coefficients, the cross-bundle Gram form must be dominated by
> the nonuniform quadratic kernel on the near-zero-dual cloud, or else expose
> the complete supported harmonic signature of the associated primal packet.
> Stationary cross-amplitudes must retain bounded normalized Abel variation,
> including the near-fold transition.  At `eta=D^(-7/48)`, the resulting
> maximum physical fiber must be `D^(49/48+o(1))` or smaller.

The existing results prove the finite scalar Schur theorem, the exact
stationary-action inverse, the affine-height branch counts, the direction
and full-signature fiber bounds, and the nonuniform cloud row sum.  They do
not prove this intertwining.  In particular:

1. a large scalar packet correlation does not automatically reveal every
   supported harmonic;
2. the physical completion Fourier variable is not the reduced error
   difference `(e-f)/g`;
3. the Airy-scale stationary amplitude spreads through many harmonic shifts;
4. the original carrier/colour coefficients have not been transferred to
   the proposed vector bundles with a lossless `l2` identity;
5. the fixed-centre estimate has not been assembled across all centres and
   the remaining nonfactorable physical tensors.

Any one of these gaps prevents a sharp four-cycle claim.

## 5. Closeout and priors

The scalar bounded-probe architecture is closed negatively:

```text
bounded physical synthesis of cubic fingerprint:     IMPOSSIBLE;
unrestricted full-threshold max-degree theorem:       FALSE;
near-zero cloud violates the Bessel target:           NO;
weaker D^(-7/48) threshold survives the cloud:        YES;
full supported vector signature has small fibers:     PROVED;
physical vector harmonic intertwining:                OPEN;
global sharp four-cycle assembly:                     OPEN;
sharp four-cycle bound:                               NOT PROVED/DISPROVED;
best unconditional exponent:                          9/8.
```

Updated subjective probabilities after this audit:

```text
the sharp four-cycle bound is true:                    about 90%;
the scalar phase-jet/fingerprint route closes it:      below 5%;
the vector-harmonic/nonuniform route can close it
without another major idea:                            about 20%;
a genuinely new mask-sensitive restriction theorem
eventually closes it:                                  about 50%.
```

The closeout is therefore negative as a proof claim but positive as a
diagnosis: the remaining difficulty is no longer algebraic injectivity.  It
is a single coefficient-uniform vector restriction/intertwining problem,
followed by a still nontrivial global assembly.

## 6. Reproducibility

The new exact audits are in:

```text
results/ZETA23-QP-HIGH-P-BOUNDED-PROBE-CUBIC-NOGO-AND-DIRECTION-ONLY-TRANSFERENCE-GATE-2026-08-25.md
results/ZETA23-QP-HIGH-P-SUPPORTED-NEWTON-INFORMATION-AND-NOISE-ALIAS-THEOREM-2026-08-25.md
results/ZETA23-QP-SUPPORTED-NEAR-ZERO-DUAL-JET-CLOUD-NO-GO-AND-NONUNIFORM-REPAIR-2026-08-25.md

src/qp_high_p_jet_transference_gate.py
src/test_qp_high_p_jet_transference_gate.py
src/qp_high_p_newton_information.py
src/test_qp_high_p_newton_information.py
src/qp_near_zero_dual_cloud.py
src/test_qp_near_zero_dual_cloud.py
```
