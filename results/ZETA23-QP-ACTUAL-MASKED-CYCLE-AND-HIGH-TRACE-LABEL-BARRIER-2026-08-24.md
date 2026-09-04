# QP sharp four-cycle: actual masked cycle and the high-trace label barrier

**Date:** 2026-08-24  
**Verdict:** a centred singular value above `sqrt(D)` can only be converted
by an ordinary nonbacktracking trace into cycles in the unlabelled
carrier--colour graph.  The arithmetic cancellation supplied by
`q>D^2` starts only after the two alternating products of the hidden row
labels agree.  An unlabelled trace does not impose that agreement.

This is a genuine logical gap, not merely a missing estimate.  There is a
literal actual-prime-power/product-window four-cycle with `q>D^2` and a
nonzero label determinant.  At the incidence level, disjoint projective
plane graphs have critical-scale degrees, pair-unique labels, centred
singular value `D`, and no four-cycles at all.  The latter construction does
not obey the cubic mask, so it does not disprove the desired theorem; it
proves that the mask must enter before the trace-to-cycle step.

No sharp four-cycle bound is proved here.

---

## 1. The exact identity carried by an actual cycle

Put `Q=q^3`.  Let a projected `2k`-cycle have carrier vertices `b_i`,
colour vertices `c_i`, and its two edges at `b_i`

```text
Q+r_i  =8*a_i *b_i*c_i,
Q+r'_i =8*a'_i*b_i*c_(i+1),             |r_i|,|r'_i|<=C*q*D.   (1.1)
```

Multiplication around the cycle cancels every `b_i` and every `c_i`:

```text
(prod_i a'_i)*(prod_i(Q+r_i))
 =(prod_i a_i)*(prod_i(Q+r'_i)).                         (1.2)
```

Since all labels are comparable to `q`, (1.2) gives

```text
|prod_i a_i-prod_i a'_i| <<_(C,k) D*q^(k-2).             (1.3)
```

This is a near-product identity, not equality.  The inequality `q>D^2`
does not change that conclusion.

There is a stronger exact consequence if a separate combinatorial input
has already produced a **label-balanced** cycle,

```text
prod_i a_i=prod_i a'_i.                                  (1.4)
```

Then (1.2), expanded in powers of `Q`, gives

```text
Q^(k-1)*(sum_i r_i-sum_i r'_i)=O_(C,k)(Q^(k-2)*(qD)^2).
```

The expression in parentheses is an integer.  Hence, for fixed `C,k` and
sufficiently large `q/D^2`,

```text
sum_i r_i=sum_i r'_i.                                    (1.5)
```

This is the useful `q>D^2` rigidity.  Its hypothesis is (1.4), which is a
Latin-trade/linked-cycle condition on the hidden labels.  A trace of the
binary carrier--colour adjacency matrix records neither side of (1.4).

## 2. A literal actual masked cycle with nonzero determinant

Take

```text
q=200003,                  D=q^(16/33)>371,
b_0=83777,                 b_1=101411,
c_0=101411,                c_1=117709,

(a_ij)=((117709,101411),(97241,83777)).                    (2.1)
```

Every displayed number is prime and lies in the logarithmic width-`.2`
shell about `q/2`.  In row-major order, the four exact residuals

```text
r_ij=8*a_ij*b_i*c_j-q^3
```

are

```text
(-58791843,-58791843,69391661,-58791843).                 (2.2)
```

Their maximum absolute value is `69391661`, whereas

```text
371*q=74201113<q*D.                                       (2.3)
```

Thus all four edges belong to the actual product-window graph at the sharp
asymptotic scale.  Also `D^2=q^(32/33)<q`.  Nevertheless

```text
a_00*a_11-a_01*a_10
 =117709*83777-101411*97241
 =-158.                                                   (2.4)
```

So even an actual masked cycle in the `q>D^2` regime need not have balanced
labels or zero determinant.  Equation (1.2) holds exactly; in this example
its two label products differ by `158`, and the residual sums do not agree.

This fixture has cross-role repetitions (`b_1=c_0`, among others).  It is
therefore not a counterexample in the all-eight-distinct balanced broad
sector.  Its exact role is narrower: it disproves the proposed local lemma
“actual cycle plus `q>D^2` implies tangent/label-balanced.”

## 3. Why high trace does not manufacture the missing labels

The graph-theoretic obstruction can be made exact at the critical scales.
Let `p` be prime and take the point--line incidence graph of `PG(2,p)`.
It has

```text
n=p^2+p+1 vertices on each side,
d=p+1 degree,
girth 6, hence no four-cycles.                            (3.1)
```

Take at least two disjoint copies.  The vector which is constant on one
component, the negative constant on another, and zero elsewhere is killed
by the global all-ones matrix.  The centred adjacency therefore has the
exact singular value

```text
sigma_centred=d,                                         (3.2)
```

not `sqrt(d)`.

This can also respect all three abstract pair-uniqueness and degree ledgers.
A `d`-regular bipartite graph is a union of `d` perfect matchings.  Split
each matching into pieces of at most `d` edges and give every piece a fresh
row label.  Then each label is a matching of size at most `d`, so every two
coordinate projections are injective.  The number of labels per component
is

```text
d*ceil(n/d)=p^2+O(p),                                    (3.3)
```

the same order as the vertices.  Taking `ceil(d^(1/16))` components gives

```text
q=d^(33/16+o(1)),                                        (3.4)
```

exactly the project exponent relation.  Yet the centred singular value is
`d` and there is no projected four-cycle to which the four-shift rigidity
could be applied.

There is an even cleaner obstruction for the small power violations which
a `q^o(1)` theorem must exclude.  Fix `0<epsilon<3/32`, let the ambient
degree cap be `D`, and choose

```text
d=D^(1/2+2*epsilon+o(1)).                            (3.5)
```

Use two projective-plane components of degree `d` and make all other
ambient vertices isolated.  Their total number of edges is

```text
2*d^3=D^(3/2+6*epsilon+o(1))<D^(33/16)=q.           (3.6)
```

Consequently every edge can receive its own one-use label from an ambient
label set of size `q`.  All three pair projections are injective and **no
cycle of any length is label-balanced**, because the alternating edge-label
sets are disjoint.  Nonetheless the centred component singular value is

```text
d>sqrt(D)*D^epsilon.                                (3.7)
```

Thus even a power spectral violation need not produce a linked/Latin-trade
cycle from graph trace and pair uniqueness.  The cubic arithmetic mask is
the only remaining possible source of such a conclusion.

This is an incidence countermodel, not an actual QP countermodel: no
integers have been assigned to its abstract vertices and it does not impose
(1.1).  It proves the precise methodological point.  Nonbacktracking trace,
degree bounds, pair uniqueness, and critical cardinalities cannot by
themselves turn spectral excess into the **label-balanced** linked cycles
needed by (1.5).  Such a theorem would already be the missing
mask-sensitive reciprocal restriction theorem.

## 4. The GL(3) reformulation does not retain the common carrier

The scalar three-factor coefficient

```text
alpha_n=sum_(abc=n) 1_S(a)1_S(b)z_c                       (4.1)
```

is compatible with a minimal-parabolic `GL(3)` Eisenstein/divisor
coefficient.  It is not the two-star object.  Squaring (4.1) allows the two
copies to use different carriers, whereas the required energy is

```text
sum_b |sum_(a,c,r: 8abc=Q+r) z_c|^2.                      (4.2)
```

Keeping (4.2) requires the Hilbert-valued coefficient

```text
alpha_n(b)=1_S(b)*sum_(ac=n/b)1_S(a)z_c.                  (4.3)
```

The external selected-shell projector in `b` is not a scalar Hecke
coefficient and is not restored by polarization in `z`.  Thus a scalar
`GL(3)` Whittaker/Motohashi identity aggregates away exactly the carrier
fibre whose equality defines the two-star count.  A vector-valued
cross-cusp theorem accepting (4.3) would be a new theorem equivalent in
strength to the desired restriction estimate, not an existing automatic
reformulation.

## 5. Binary status

```text
actual projected-cycle product identity (1.2):       PROVED;
cycle gives only near label product (1.3):            PROVED;
label-balanced cycle plus q>D^2 gives (1.5):          PROVED;
actual q>D^2 masked cycle forces label balance:       FALSE (2.1)--(2.4);
counterfixture is all-eight-distinct broad:            NO;
high trace plus pair uniqueness forces 4-cycles:      FALSE (PG(2,p));
high trace plus the full cubic mask forces trades:    OPEN / TARGET THEOREM;
scalar GL(3) coefficient retains common b:            NO;
sharp four-cycle theorem from this route:             NOT PROVED.
```

Exact replay code and tests:

```text
src/qp_actual_masked_cycle_high_trace_barrier.py
src/test_qp_actual_masked_cycle_high_trace_barrier.py
```
