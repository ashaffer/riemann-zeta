# Delete the selected denominator first: the resonant group is elementary

**Date:** 2026-08-13  
**Status:** exact finite deletion reorder.

## Verdict

Delete the blockwise union of all multiples of the selected denominators
directly from the integer lattice **before** deleting any other composite.
Equivalently one may localize this operation to terminal prime edges.  Then,
uniformly for arbitrary blockwise choices

```text
Y^(1537/10000)<=q_I<Y,
```

including composite denominators,

```text
Y^-1 sum_I |D^(first)_(q_I,I)|
 <<Y^(-1537/10000+o(1))=Y^(-.1537+o(1)).             (0.1)
```

This is twice the exponent furnished by the universal rough-base Cauchy
argument and makes no use of a rough-gap theorem.  Consequently the
high-denominator rough-gap square was a sufficient lemma for the resonant
group under a traditional sieve ordering, but it is not a necessary lemma
once arbitrary exact deletion reordering is allowed.

The cost is structural, not logical: after the `q`-first group, the sole
remaining deletion tail contains every other composite, including those
with small least prime factor.  Every remaining center is nonresonant
modulo `q`, but bounding their signed aggregate is still open.  Thus (0.1)
does not prove the full antenna or a zero-free strip.

## 1. Exact global reorder

Partition the shell into half-open curvature blocks `I` and choose one
denominator `q_I` on each block.  Assign a boundary integer to exactly one
of its adjacent blocks, and put

```text
D={interior n in the shell: n belongs to I and q_I|n}. (1.0)
```

Start from the integer lattice, retain the two fixed outer endpoints, delete
all of `D` simultaneously, and then delete every remaining composite.
Because `q_I<Y` while shell integers have size `Y`, every point of `D` is
composite.  Up to the fixed outer-endpoint convention, the final set is the
terminal primes, and

```text
T(primes)-T(integers)=D^(first)+R^(nonq)             (1.1)
```

is an exact finite telescope.  Every later deletion center `n` in block `I`
satisfies `q_I` not dividing `n`, including at a block boundary under the
half-open assignment convention.

The simultaneous transport identity does not require the deleted nodes to
be separated.  Different selected denominators may therefore create
adjacent deleted nodes on opposite sides of a boundary.  Every interior
integer node initially has Voronoi mass one, so

```text
||nu_(Z\D)-nu_Z||_TV=2 #D.                           (1.2)
```

For the piecewise selected test function
`f(n)=e_(q_I)(a_I n)` on `I`, or that phase times a uniformly bounded taper,
(1.2) gives `|D^(first)(f)|<=2||f||_infty #D`.  More precisely, partition
the transported mass of the original integer Voronoi cells according to the
deleted center from which it came.  This gives exact block contributions
`D_I^(first)` even when their destination lies across a block boundary, and

```text
sum_I |D_I^(first)(f)|<=2||f||_infty sum_I #D_I.     (1.2a)
```

Thus the global statement proves the sum of blockwise absolute values in
(0.1), not merely the absolute value after summing the blocks.

For comparison, this global identity may be localized edgewise.  Let
`[p,p']` be any edge between consecutive terminal primes.  Start with every
integer in this interval, retaining `p,p'` forever, and put

```text
D_q={n in (p,p'): q|n}.
```

Because `q<Y` while `p,p'` are in the `Y`-shell, every point of `D_q` is
composite.  Perform two steps:

1. delete all of `D_q` simultaneously;
2. delete every remaining composite, in any order.

The final active set is exactly the prime endpoints, and the initial set is
the integer trapezoid partition.  Therefore

```text
T(primes)-T(integers)=D^(first)_q+R^(nonq)_q         (1.3)
```

is an exact finite telescope.  Every center in `R^(nonq)_q` satisfies
`q` not dividing `n`, since all `q`-multiples disappeared in step 1.

This grouping is valid for composite `q`; it is not an Eratosthenes
prime stage and does not pretend that `q` is prime.

## 2. The resonant group has mass `O(Y/q)`

In the integer trapezoid partition, every interior node has Voronoi mass
exactly one.  The simultaneous positive-transport identity hence gives

```text
||nu_(Z\D_q)-nu_Z||_TV=2 #D_q,                      (2.1)
```

so for every unit-modulus phase, and in particular the selected rational
phase `e_q(a n)`, one has

```text
|D^(first)_q|<=2 #D_q.                               (2.2)
```

For a fixed denominator away from block and outer endpoints there is even an
exact formula.  A deleted
multiple `x` has integer neighbors `x-1,x+1`, so its simultaneous charge is

```text
{e_q(a(x-1))+e_q(a(x+1))}/2-e_q(ax)
 =cos(2*pi*a/q)-1.                                   (2.2a)
```

Thus a fixed-`q` interior group with no adjacent deletion imported from a
neighboring block equals
`#D_q {cos(2*pi*a/q)-1}`; (2.2) is sharp up to its absolute constant for
adversarial numerators.  Endpoint conventions contribute only `O(1)` per
block and are already present in (2.3).  The global proof uses only total
variation, so this formula is not needed where the denominator changes.

For disjoint curvature blocks,

```text
sum_I #D_(q_I)
 <=sum_I (|I|/q_I+O(1))
 <<Y^(1-1537/10000)+K.                              (2.3)
```

At the shortest block scale `H>=Y^(8/33)`,
`K<<Y^(1-8/33)=o(Y^(1-1537/10000))`.  Equations
(2.2)--(2.3), divided by `Y`, prove (0.1).  No Cauchy inequality and no gap
moment are required.

## 3. Edge and boundary scope

No terminal-gap truncation or boundary-edge discard is needed for (0.1).
Prime nodes are never deleted and automatically act as barriers, including
on long prime gaps, while the global total-variation estimate permits the
test function and selected denominator to change across block boundaries.

If one insists on a componentwise proof in which each retained prime edge
has one fixed selected denominator, the older bookkeeping remains valid:

The Gafni--Tao truncation removes terminal prime edges longer than

```text
G=Y^(797/5000).
```

Discard also the `O(K)` retained edges crossing curvature-block boundaries.
Their normalized positive mass is

```text
KG/Y <<Y^(-(8/33-797/5000))
     =Y^(-13699/165000)=Y^(-.0830242...).            (3.1)
```

Every remaining edge belongs to one block and therefore to one selected
denominator.  Its two prime endpoints are permanent barriers, so the
componentwise deletion identity (1.3) introduces no cross-block charge.
This disposal is optional for the resonant group and is not charged against
the stronger global statement.

## 4. What changed relative to the rough-stage route

The traditional SPF split was

```text
T(primes)=C_(<q)+D_q+R_(>q).
```

It preserved multiplicative stage labels in the tail, but created a dense
pre-`q` mode and made the resonant stage depend on pre-`q` rough gaps.  The
blockwise `q`-first split is instead

```text
T(primes)=T(integers)+D^(first)+R^(nonq)_(q_I).      (4.1)
```

The integer baseline is the existing quadrature baseline.  There is no
pre-group candidate mode, and (0.1) settles the only resonant group.  The
new live arithmetic object is the signed blockwise non-`q_I` composite tail
`R^(nonq)_(q_I)`.  Least-prime-factor labels may still be used **after** the
first deletion, but their local neighbor gaps are those of the
`q`-punctured evolving set.

There is a precise warning against over-interpreting “nonresonant.”  After
step 1 the active rule is the explicit blockwise punctured lattice `Z\D`, so

```text
R^(nonq)_(q_I)=T(primes)-T(Z\D).                    (4.2)
```

On one block with a fixed denominator this specializes to
`R^(nonq)_q=T(primes)-T(Z minus qZ)`.

The second term is periodic and explicit.  Consequently a power estimate
for (4.2) is, up to that known baseline, essentially the original selected
prime statistic.  Pointwise exclusion of phase-one centers is not itself a
cancellation theorem.  The `q`-first reorder definitively removes the
resonant-group obstruction, but it does not automatically simplify the
remaining signed arithmetic.

## 5. Truth boundary

```text
q-first exact deletion identity:                    PROVED
arbitrary composite selected denominator:           PROVED
selector-stable resonant saving q^-1:                PROVED
global selector; adjacent boundary deletions:         PROVED
long-edge or boundary disposal needed for q-group:    NO
rough-gap moment needed for this resonant group:     NO
all remaining centers pointwise nonresonant:         PROVED
signed non-q composite tail:                         OPEN
integer-to-continuum transfer in the full taper:      SEPARATE INPUT
full antenna / zero-free strip from this alone:       NOT CLAIMED
```

## 6. Reproduction

```bash
python3 results/verify_zeta23_q_first_integer_base.py
```
