# Weighted rough transition and gap-four hostile audit

**Date:** 2026-08-13  
**Status:** both exact reductions pass; the remaining negative conclusions are
method-scoped, not no-go theorems for the actual arithmetic coefficients.

## Verdict

The dyadic post-`q` reduction in
[`ZETA23-WEIGHTED-ROUGH-TRANSITION-RESIDUE-DISPERSION-GATE-2026-08-13.md`](ZETA23-WEIGHTED-ROUGH-TRANSITION-RESIDUE-DISPERSION-GATE-2026-08-13.md)
is exact with the cutoff convention currently stated there:

```text
Delta_(I,P)
 =nu_(I,max(2P,q_I))-nu_(I,max(P,q_I)).              (0.1)
```

In particular, (0.1) vanishes when `q_I>=2P`; there is no unrecorded first
stage at `q_I`, and the identity holds for composite denominators.  The
finite-group `L2` and `L4` hypotheses in that report have the correct block
weights and close at the claimed exponent.

The near-quarter gap-four reduction in
[`ZETA23-SELECTED-TRANSITION-FINITE-GROUP-AND-FIXED-GAP-GATE-2026-08-13.md`](ZETA23-SELECTED-TRANSITION-FINITE-GROUP-AND-FIXED-GAP-GATE-2026-08-13.md)
also passes.  Its exact output is a twisted *actual cousin-prime* sum, not a
sieve majorant.  The published literature checked below does not prove the
required pointwise power cancellation.  Conversely, none of the cited
parity or sieve results proves that this cancellation is impossible.

No zero-free strip follows from either reduction alone.

## 1. Dyadic rough-Voronoi increment

Let `nu_z` be the trapezoid/Voronoi measure after every prime at most the
real cutoff `z` has been deleted.  Once `p>q`, deleting the `q`-multiples
first cannot change the active set: every `q`-multiple has a prime divisor
at most `q<p` and was already deleted in the ordinary SPF flow.  Therefore

```text
sum_(P<p<=2P, p>q_I) (nu_p-nu_(p-))
 =nu_(max(2P,q_I))-nu_(max(P,q_I)).                  (1.1)
```

This checks all cutoff cases:

```text
q_I<=P:       nu_(2P)-nu_P,
P<q_I<2P:    nu_(2P)-nu_(q_I),
q_I>=2P:     0.                                      (1.2)
```

Both endpoint measures have total mass equal to the retained physical
length, so the increment has mass zero.  Both cutoffs in a nonzero
increment are at least `q_I`; consequently every atom is a unit modulo
`q_I`.  Reducing (1.1) modulo `q_I` therefore loses no selected-character
information.

### Selector and block normalization

For

```text
D_(I,P)(a)=sum_(r mod q_I) Delta_(I,P)(r)e_(q_I)(ar),
```

unnormalized finite Parseval gives

```text
sum_(a mod q_I)|D_(I,P)(a)|^2
 =q_I||Delta_(I,P)||_2^2.                            (1.3)
```

There are only `Y^o(1)` dyadic bands.  Thus Cauchy first across bands and
then with physical weights `H_I` gives

```text
sum_I |R_(>q_I,I)|
 <<Y^(1/2+o(1))
   [sum_(I,P) q_I/H_I ||Delta_(I,P)||_2^2]^(1/2).    (1.4)
```

Accordingly the sufficient input exponent `1-2kappa-2delta` gives the
output exponent `1-kappa-delta`.  The fourth-moment calculation is likewise
exact:

```text
sum_a |D_(I,P)(a)|^4
 =q_I sum_s |C_(Delta_(I,P))(s)|^2,                  (1.5)
```

and band recombination costs only the cube of the number of bands.  Holder
with `H_I` then gives the stated hypothesis

```text
sum_(I,P) q_I/H_I^3 sum_s|C_(Delta_(I,P))(s)|^2
 <<Y^(1-4kappa-4delta+o(1)).                         (1.6)
```

No assumption that the selector uses distinct denominators or numerators
enters (1.3)--(1.6).

### Boundary and frozen-amplitude scope

Equations (1.1)--(1.6) are exact on retained terminal-prime edges lying
wholly inside one curvature block, for the frozen additive character and
constant-amplitude trapezoid rule.  A terminal edge crossing a block
boundary has no unambiguous single selector and is not part of
`Delta_(I,P)` under this convention.  The companion selector-stable rough
gap ledger disposes of those edges separately; their known cost is not
being re-proved or silently charged to (1.4).

Likewise, a smooth amplitude changes the atomic coefficients and phase
freezing replaces the logarithmic phase only after a separate approximation
argument.  Finite Parseval continues to hold for the resulting complex
weights, but the numerical size of their transition vectors is not a
consequence of the constant-amplitude theorem.  Thus even a proof of the
open rough-increment estimate must be reattached to the existing boundary,
long-edge, taper, and phase-freezing ledgers before it can be called an
antenna estimate.

## 2. Exact coefficient-blind deficit

Let `c_(I,P)(n)` be the atomic increment before reduction modulo `q_I`.
Cauchy inside residue classes, using `q_I<=H_I`, proves

```text
q_I||Delta_(I,P)||_2^2
 <=(H_I+q_I)||c_(I,P)||_2^2
 <=2H_I||c_(I,P)||_2^2.                              (2.1)
```

With the retained terminal-gap cap

```text
G=Y^theta,                  theta=.1594,
```

the atomic mass and total mass on an edge of length `g<=G` give, after the
dyadic logarithm is absorbed,

```text
sum_(I,P)||c_(I,P)||_2^2 <<Y^(1+theta+o(1)).          (2.2)
```

The same exponent bounds the coefficient-blind `L4` input because
`||c_(I,P)||_1<=2H_I`.  At

```text
kappa=.01974048259...,
```

the exact baseline gaps between (2.2) and the closing inputs are

```text
L2: theta+2kappa=.19888096518...,
L4: theta+4kappa=.23836193036....                    (2.3)
```

Even if a future gap theorem improved (2.2) optimistically to
`Y^(1+o(1))` throughout the full tail, (2.1) would still miss by

```text
2kappa=.03948096518...   and   4kappa=.07896193036.... (2.4)
```

Equations (2.3)--(2.4) are a deficit for the **coefficient-blind proof
class**.  They are not a counterexample built from the actual rough sets.
The actual vectors may have residue cancellation invisible to (2.1).

## 3. Literature boundary for the rough increment

The theorem statements, rather than title-level analogies, give the
following quantifier mismatch.

1. Wolke's Bombieri--Vinogradov theorem, as recorded in Xuan's
   [*Integers free of small prime factors in arithmetic progressions*](https://doi.org/10.1017/S0027763000007212),
   averages the modulus and gives arbitrary logarithmic savings for
   **unweighted counts** of sifted integers.  It has neither the selected
   pointwise modulus nor the nearest-neighbor Voronoi weight in (0.1).
2. Xuan's individual fixed-modulus results at a fixed-power roughness
   cutoff reach only subpolynomial moduli and retain a possible exceptional
   real-character contribution before specialization.  They do not reach
   `q_I=Y^b`, `.1537<=b<=33/133`.
3. Bombieri--Friedlander--Iwaniec and Maynard well-factorable dispersion
   estimates average moduli after a separated bilinear coefficient has
   been produced.  The coefficient assigning a deleted centre to its two
   first surviving rough neighbors is a joint coefficient, and no cited
   theorem supplies the required separation with a power-small error.
4. The classical and restricted-support large sieves average frequencies
   or moduli.  Their presently available gain is at most logarithmic here;
   a blockwise height selector may choose an exceptional frequency.

Thus no published result located proves (1.4) or (1.6) with a fixed power.
There is also no published theorem located that rules out such an estimate
for the actual rough-Voronoi increments.

## 4. Gap-four algebra and puncture audit

Take `q>4`, `q=3 (mod 4)`, `a=(q+1)/4`, and

```text
z=e_q(a)=i e(1/(4q)).                                (4.1)
```

On an unpunctured terminal edge `[p,p+4]`, the prime trapezoid minus the
integer trapezoid is

```text
z^p K_4(z),
K_4(z)=3/2(1+z^4)-(z+z^2+z^3).                      (4.2)
```

Writing

```text
B_4(z)=1/2(1+z^4)+z+z^2+z^3,
```

one has `K_4=2(1+z^4)-B_4`, `B_4(i)=0`, and
`|B_4'(z)|<=8` on the unit circle.  Since
`|z-i|<=pi/(2q)`, the accumulated analytic error is `O(H/q)`.

There is at most one interior `q`-multiple on a length-four edge.  Removing
one unit-lattice node changes its local unit-modulus trapezoid by at most
`2`, and only `O(H/q+1)` disjoint terminal edges are punctured.  Hence the
total puncture error is indeed `O(H/q+1)`.

If `p,p+4>3` are prime, then `p+2` is divisible by `3`; the endpoints are
therefore automatically consecutive.  Finally

```text
z^p=i chi_4(p)e(p/(4q)),       z^4=e(1/q),
```

which proves the exact sector reduction

```text
R_(I,4)(a/q)
 =2i(1+e(1/q))
   sum_(p,p+4 prime in I) chi_4(p)e(p/(4q))
  +O(H/q+1).                                          (4.3)
```

The multiplier has modulus `4|cos(pi/q)|`, so it introduces no power loss.
Since `q>=Y^.1537` and `.1537>kappa`, the puncture error is below the local
`HY^(-kappa)` bill.

## 5. Fixed-gap threshold and literature boundary

A bound of the form

```text
|sum_(p,p+4 prime in I) chi_4(p)e(p/(4q))|
 <<Hq^(-delta)Y^o(1)                                 (5.1)
```

beats the local bill uniformly only if

```text
delta>kappa/.1537=.1284351502....                    (5.2)
```

Thus `q^(-1/8)` misses by the exact `Y`-exponent

```text
kappa-.1537/8=.00052798259....                       (5.3)
```

The primary-source scope check is:

1. Green--Tao restriction gives an `L^p`, `p>2`, frequency estimate for
   prime-tuple exponential sums.  It permits exceptional individual
   frequencies and does not imply (5.1) for the selected numerator.
2. Mikawa's 1992 theorem in
   [*On prime twins in arithmetic progressions*](https://tsukuba.repo.nii.ac.jp/record/16157/files/8.pdf)
   proves, in his notation,

   ```text
   sum_(q<=x^(1/2)(log x)^(-B)) max_((a,q)=1)
     sum_(0<|2k|<=x) |E(x;q,a,2k)|
       <<x^2(log x)^(-A).                            (5.4)
   ```

   It averages both the modulus and the shift.  Formula (5.4) allows the
   single shift `2k=4` and a height-selected modulus to be exceptional.
3. Matomaki--Radziwill--Tao prove the expected von-Mangoldt correlation for
   almost all shifts in ranges of length at least `X^(8/33+epsilon)`, with
   logarithmic average saving.  This neither retains the fixed shift `4`
   nor supplies the selected additive twist.
4. Murty--Vatwani explicitly add a conjectural shifted-prime/Mobius
   equidistribution input, together with Elliott--Halberstam, to cross the
   parity barrier.  It is not an unconditional source for (5.1).
5. Ford--Maynard prove optimal results and construct obstructions for
   arbitrary **nonnegative** sequences satisfying specified Type-I/II
   axioms.  Their theorem is not a no-go result for the particular signed
   actual-prime coefficient in (5.1).

The literature therefore supports the stated fail-fast boundary: standard
sieve, restriction, or averaged dispersion does not establish (5.1), but
no cited result eliminates (5.1).

## 6. Reproduction and truth boundary

Run:

```bash
PYTHONPATH=src python3 -m unittest -v \
  src/test_weighted_rough_transition_gate.py
python3 results/verify_zeta23_weighted_rough_transition_gate.py

PYTHONPATH=src python3 -m unittest -v \
  src/test_universal_q_reorder_transport.py \
  src/test_spf_residue_transport.py
python3 results/verify_zeta23_selected_transition_fixed_gap_gate.py
```

On 2026-08-13 these ran `6/6` and `9/9` unit tests respectively, and both
verifiers returned `PASS`.

```text
cutoff-clipped dyadic telescope:                      EXACT
q-first invariance for p>q:                          EXACT
selector/block L2 and L4 normalization:              EXACT
coefficient-blind deficits (2.3):                    EXACT
coefficient-blind bounds disprove actual dispersion: NO
published actual weighted-increment theorem:         NOT FOUND
gap-four K_4 algebra and puncture order:              EXACT
cousin pairs automatically consecutive:              EXACT
q-decay threshold and q^(-1/8) deficit:               EXACT
published fixed-shift selected-q power theorem:       NOT FOUND
published no-go theorem against either live input:    NOT FOUND
post-q tail / whole nonresonant transition:           OPEN
zero-free strip:                                      NOT CLAIMED
```
