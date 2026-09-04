# Selector-stable truncated rough-gap energy

**Date:** 2026-08-13  
**Status:** analytic capped-energy theorem proved from the same published
Matomaki input; blockwise charge consequence proved for the edgewise
Gafni--Tao truncation.

**Update:** the exact universal-base reorder in
`ZETA23-UNIVERSAL-ROUGH-BASE-SELECTOR-Q-GROUP-2026-08-13.md` supersedes the
charge exponent below: it combines the full `D=1/3` gap-square theorem with
`B_q=R_(Y^(4/25)) union q Z` and gives the stronger selector-stable saving
`.0799`.  The present report remains the direct theorem for varying
traditional rough cutoffs and records the independent `D=5/9` frontier.

## Verdict

The full-square estimate `G_2(Y;z)<<Y log^2 Y` already proved for
`z<=Y^.16` does not by itself aggregate when a curvature block chooses a
different rational denominator: truncated square energy is not monotone
under deleting rough points.  There is, however, a selector-stable
replacement which also handles composite denominators exactly.

Put

```text
Z=Y^(8/33),       G=C_w Y^theta,   theta=797/5000,
Phi_G(R_z)=sum_(gaps g of R_z) g min(g,G).
```

Here `C_w` is the fixed shell constant in the audited Gafni--Tao long-gap
cutoff.  It has no effect on any exponent below.

At the one maximal cutoff `Z`,

```text
Phi_G(R_Z) << Y^(1+1468/16875+epsilon),              (0.1)
1468/16875=.08699259259....
```

For a reduced rational denominator `q_I<Y`, put

```text
B_(q_I)=R_Z union {composite multiples of q_I}.
```

If disjoint curvature blocks `I` choose arbitrary such denominators, the
total square energy of their `G`-short local `B_(q_I)` gaps obeys

```text
sum_I sum_(g in B_(q_I), g meets I, g<=G) g^2
 <<Y^(1+1468/16875+epsilon),                          (0.2)
```

provided every block has length at least `Y^(8/33)`.  Thus the estimate is
stable under the height-selected denominator.  No union bound over
denominators and no regularity of `I -> q_I` is used.  Only the maximal
set `R_Z` needs an analytic variance bound.  In particular (0.2) is valid
past `q_I=Z`; it covers every curvature denominator below `Y`.

For resonant `q_I`-multiple groups with `q_I>=Y^beta`,
`beta=799/5000`, the
blockwise Cauchy inequality now aggregates to

```text
Y^-1 sum_I |D_(q_I,I)|
 <<Y^(-(beta-1468/16875)/2+epsilon)
 =Y^(-9829/270000+epsilon),                           (0.3)
```

where `9829/270000=.03640370370...`.  This clears the largest current
carrier bill `.01974048259...` by `.01666322111...`.

Equations (0.2)--(0.3) apply to the exact **short-terminal-edge part** of
the deletion telescope.  Gafni--Tao permits the complementary long prime
edges to be discarded by the already audited positive mass estimate.  The
result does not control the pre-`q` rough Fourier mode or the post-`q` SPF
tail.

## 1. The broader lower-sieve variance range

Use Matomaki's lower vector-sieve minorant with

```text
d=5/9,       e=1/1000,       L=d+e=5009/9000,
D=Y^d,       E=Y^e.
```

At the largest allowed roughness cutoff,

```text
d/(8/33)=55/24>2,                                   (1.1)
```

so the dimension-one lower-sieve function has a fixed positive margin and
the minorant mean is `>>1/log Y`, uniformly over the whole cutoff range.

Factor the level-`D` well-factorable weight at

```text
m=2L/3,             d-m,
```

and join the beta factor `e` to the second piece.  Since

```text
d-m+e=L/3,
```

the parameters in raw Lemma 5.4 are

```text
M<=Y^(2L/3),       N<=Y^(L/3),       Q<=Y^L.         (1.2)
```

For physical interval length `H=Y^eta`, the endpoint of the valid range is

```text
eta_* = 1-5L/3 = 391/5400=.0724074074....            (1.3)
```

At `eta=eta_*`, the nodes in the fourth-power bracket of Lemma 5.4 are

```text
HMNQ/Y = N,                 Q+N^2 = Y^L,
(MQ)^2 exponent             =10L/3,
MQ*N*(Q+N^2) exponent       =3L,
H*(MN)^3*Q/Y exponent       =7L/3,
full bracket exponent       =10L/3.                  (1.4)
```

Hence, for every fixed `delta>0` and `eta=eta_*-delta`, the correlation
exponent is

```text
1/2+eta/2+5L/6 = 1-delta/2.                          (1.5)
```

The `S_1^-`, `S_3^-`, and `H^3` estimates transfer exactly as in the
lower-level audit.  Therefore

```text
integral |E_Z(x;H)|^2 dx << YH/log Y,                (1.6)
meas{x:(x-H,x] contains no Z-rough integer}
                         <<Y log Y/H                 (1.7)
```

uniformly for `H<=Y^(eta_*-delta)`.  This is the only analytic roughness
cutoff needed below.  Smaller selector-dependent cutoffs enter solely
through deterministic nesting.

### A caught boundary error

The tempting moving split

```text
n=eta+2L-1,        m=1-L-eta                         (1.8)
```

does not prove (1.5).  Its `(MQ)^2` branch makes the total Lemma 5.4
exponent identically

```text
1/2+eta/2+[2(m+L)]/4=1.                              (1.9)
```

It is exactly on the no-saving boundary.  The fixed balanced split (1.2),
with `eta<eta_*`, is essential.

## 2. One empty-window scale controls a capped energy

Let

```text
T_Z(H)=sum_(gaps of R_Z) (g-H)_+.
```

Equation (1.7) gives `T_Z(H)<<Y log Y/H`.  Define

```text
phi_G(g)=g min(g,G).
```

At `H=Y^(eta_*-delta)`, split the gaps at `2H`.  The gaps below `2H`
contribute at most `2HY`.  For `g>2H`, one has `g<=2(g-H)`, hence

```text
sum_g phi_G(g)
 <=2HY+2G T_Z(H)
 <<YH+YG log Y/H.                                    (2.1)
```

Since `theta>2eta_*`, the second term dominates.  Letting `delta` tend to
zero in the usual epsilon formulation proves (0.1), because

```text
theta-eta_*=1468/16875=.08699259259....              (2.2)
```

Iwaniec's `J(Z)<<Z^2=o(Y)` is used only to keep shell-boundary gaps in a
fixed multiplicative enlargement; the variance need not reach the maximum
gap scale.

## 3. Why the capped energy is selector-stable

The elementary fact that makes the extension work is

```text
phi_G(a)+phi_G(b)<=phi_G(a+b),       a,b>=0.          (3.1)
```

If `a+b<=G`, this is `a^2+b^2<=(a+b)^2`.  If `a+b>=G`, each summand is at
most `Ga` or `Gb`, while the right side is `G(a+b)`.  Thus `phi_G` is
superadditive: merging gaps can only increase its total.

By definition `R_Z` is a subset of every `B_(q_I)`.  Every selected local
gap therefore lies inside one `R_Z` gap.  Gaps wholly contained in disjoint blocks have
disjoint interiors.  Grouping them by the containing `R_Z` gap and applying
(3.1) proves that their total `phi_G` energy is at most `Phi_G(R_Z)`.

There are at most two local gaps crossing each block boundary.  On the
Gafni--Tao short-edge part they have length at most `G`, so their total
extra square energy is

```text
O(KG^2),       K<=Y^(1-8/33).                        (3.2)
```

Its excess exponent is

```text
2theta-8/33=6301/82500=.07637575758...,              (3.3)
```

strictly below (2.2).  This proves (0.2).  Notice that ordinary truncated
energy `sum_(g<=G)g^2` is not monotone: one long coarse gap can split into
many short gaps.  The linear continuation `phi_G(g)=Gg` above the cap is
what repairs that defect.

Two naive alternatives are genuinely invalid.

1. Fixed-cutoff truncated energy is not monotone under refinement: a gap
   longer than `G` contributes zero to `sum_(g<=G)g^2`, while splitting it
   can create many positive `G`-short squares.
2. Giving every block both of its **full** boundary gaps is not summable,
   even when every block chooses the same cutoff.  One long rough gap
   crossing `J` blocks is then charged `J` times as `J g^2`, although the
   global ledger contains only `g^2` once.  Thus the often-invoked formula
   `sum_I G_(2,I)(q_I)<=G_2(Z)` is false with that convention.

The capped functional repairs the first issue; short-edge disposal or the
explicit `KG^2` ledger repairs the second.

For the antenna application there is an even cleaner boundary convention:
discard every terminal prime edge crossing a curvature-block boundary.
There are `O(K)` such edges and their total unnormalized length is `O(KG)`.
After division by `Y` this costs

```text
KG/Y <<Y^(-(8/33-theta))=Y^(-.0830242...),           (3.4)
```

well beyond the carrier requirement.  All remaining short edges lie wholly
inside one block, so their selected denominator is unambiguous and no
transport charge from an adjacent block is present.

## 4. Aggregating the deletion charges

Decompose the short prime rule edge by edge.  If a terminal consecutive
prime gap has length at most `G`, then throughout the Eratosthenes deletion
telescope every intermediate rough subgap inside that edge also has length
at most `G`: the two terminal primes survive and remain barriers.

For a possibly composite selected denominator `q_I`, order this edge's
exact deletion telescope as follows.

1. Delete every composite `n` with `n notin R_Z` and `q_I` not dividing
   `n`.  The active set is exactly
   `B_(q_I)=R_Z union {composite q_I-multiples}`.
2. Delete **all multiples of `q_I` simultaneously**.  They were deliberately
   retained in step 1, and the phase `e_(q_I)(a_I n)` equals one at every
   such center.
3. Delete every remaining composite in `R_Z` in any order.

The start and end rules are unchanged, because a finite deletion telescope
is independent of the chosen order.  This constructs the resonant group for
an arbitrary composite denominator; it is not a fictitious prime sieve
stage.  Since `q_I<Y`, none of its multiples in the `Y`-shell is a terminal
prime.  Long terminal edges were removed before this edgewise telescope and
therefore contribute no charge to the short rule.

The exact simultaneous-deletion transport identity and Cauchy now give on
block `I`

```text
|D_(q_I,I)| <<sqrt(N_I E_I),                         (4.1)
```

where `E_I` is its incident pre-group `B_(q_I)` short-gap square energy.
Each rough gap is incident to at most two deleted centers.

Summing (4.1) and applying Cauchy once more,

```text
sum_I |D_(q_I,I)|
 <<sqrt((sum_I N_I)(sum_I E_I)).                     (4.2)
```

No sieve estimate is needed for the first factor.  Since the blocks are
disjoint and `q_I>=Y^beta`,

```text
sum_I N_I
 <=sum_I (|I|/q_I+O(1))
 <<Y^(1-beta)+K
 <<Y^(1-beta).                                       (4.3)
```

An enlargement by `G` at block edges adds only
`O(K(G/Y^beta+1))`, also smaller.  Insert (0.2) and (4.3) into (4.2) to
obtain (0.3).

## 5. Scope

```text
D=5/9 raw lower-sieve variance through eta<391/5400: PROVED
capped rough-gap energy exponent 1+1468/16875:       PROVED
arbitrary blockwise cutoff selector stability:       PROVED
aggregated short-edge resonant q-group saving .0364: PROVED
ordinary truncated-square monotonicity:               FALSE
moving Type-II split (1.8) gives a power saving:      FALSE
pre-group localized rough Fourier mode:               OPEN
post-q signed SPF-stage aggregate:                    OPEN
full antenna / zero-free strip from this lemma alone: NOT CLAIMED
```

## 6. Reproduction

```bash
python3 results/verify_zeta23_selector_stable_rough_gap_energy.py
```

The checker replays every rational exponent in Sections 1--4, catches the
moving-split equality, and regression-checks (3.1) on a rational grid.  The
analytic input remains Matomaki, *Almost primes in almost all very short
intervals*, Proposition 5.1, Lemma 5.4, and Sections 6.1--6.3, as audited in
the companion rough-gap reports.
