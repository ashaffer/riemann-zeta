# Universal rough base makes the resonant denominator group selector-stable

**Date:** 2026-08-13  
**Status:** exact deletion reordering plus the proved Matomaki rough-gap
square theorem; valid, but superseded for the resonant group by the
integer-base `q`-first reorder.

## Verdict

Fix once and for all

```text
Z_0=Y^(4/25).
```

The already proved estimate

```text
G_2(Y;Z_0)=sum_(consecutive R_(Z_0) gaps) g^2
           <<Y(log Y)^2                              (0.1)
```

controls the resonant deletion group for **every** block-selected reduced
denominator

```text
Y^beta<=q_I<Y,             beta=799/5000,            (0.2)
```

including arbitrary composite denominators.  The denominator need not equal
the roughness cutoff.

After deleting the terminal prime edges longer than
`G=Y^(797/5000)` and the `O(1)` short edges crossing each curvature-block
boundary, one has the selector-stable aggregate

```text
Y^-1 sum_I |D~_(q_I,I)| <<Y^(-beta/2+o(1))
                       =Y^(-799/10000+o(1)).         (0.3)
```

Thus the resonant group saves `.0799`, uniformly over the common-height
selector.  This is stronger than the `.0364037` saving obtained from the
broader `D=5/9` truncated-energy argument, and it clears the current maximum
carrier bill `.01974049` by more than `.0601`.

This conclusion is correct in its stated short-edge scope.  The later
integer-base theorem
`ZETA23-Q-FIRST-INTEGER-BASE-RESONANT-GROUP-2026-08-13.md` deletes the
blockwise union of selected multiples directly from the integer lattice and
gives the stronger saving `beta=.1598`.  It therefore supersedes (0.3) for
the resonant group.  The present theorem remains a valid independent
square-refinement corollary of the rough-gap estimate.

The tilde matters: `D~_q` is the resonant group in a newly reordered, but
exact, deletion telescope.  The early and late remainders change with this
order and remain open.  Equation (0.3) is not by itself a bound for the full
prime antenna.

## 1. Exact universal-base reorder

Work edge by edge between two consecutive terminal primes retained by the
Gafni--Tao short-edge truncation.  The prime endpoints are never deleted and
are permanent barriers.  For the denominator `q=q_I`, define the pre-group
active set

```text
B_q=R_(Z_0) union {n: q|n and n is composite}.       (1.1)
```

Starting from all integer nodes on the edge, use the following order.

1. Delete every composite `n notin R_(Z_0)` for which `q` does not divide
   `n`.  The active set is then exactly `B_q`.
2. Delete every `q`-multiple simultaneously.  Since `q<Y`, all such nodes
   in the `Y`-shell are composite.  At every deleted center,
   `e_q(a n)=1`.
3. Delete every remaining composite in `R_(Z_0)`.

The initial integer trapezoid rule and final prime trapezoid rule are
unchanged.  Finite deletion telescopes are order-independent, so this is an
exact decomposition, not a model.  It also shows why pre-sieving merely to
`P^-(q)` would be wrong: a multiple `qm` can have a smaller prime factor
coming from `m` and disappear before the intended group.  Step 1 retains
all `q`-multiples by construction.

Let `D~_(q,I)` denote step 2 on the short terminal edges wholly contained in
block `I`.  The simultaneous positive-transport identity gives

```text
|D~_(q,I)| <<sqrt(N_I E_I),                          (1.2)
```

where `N_I` is the number of deleted `q`-multiples and `E_I` is the sum of
the squares of the incident pre-group `B_q` gaps.  This is the same
order-free Cauchy argument as for the traditional prime stage: every gap is
incident to at most two deleted centers.

## 2. Selector-stable square monotonicity

The decisive inclusion is

```text
R_(Z_0) subset B_q                                  (2.1)
```

for every `q`.  Hence every `B_q` gap is a subinterval of one
`R_(Z_0)` gap.  No arithmetic relation between different selected
denominators is needed.

After boundary-edge disposal, the terminal edges belonging to distinct
curvature blocks are disjoint.  Therefore all selected local `B_(q_I)` gaps
are disjoint intervals.  Inside any fixed coarse gap of length `g`, their
lengths `g_j` satisfy `sum_j g_j<=g`, and

```text
sum_j g_j^2 <=(sum_j g_j)^2<=g^2.                   (2.2)
```

Sum (2.2) over the coarse gaps and use (0.1):

```text
sum_I E_I <<Y(log Y)^2.                              (2.3)
```

This proves the precise selector-stable monotonicity step that fails if
every block imports its full boundary gaps.  It works here because the
terminal edges crossing block boundaries are disposed of first.

## 3. Count and global Cauchy

The blocks are disjoint and each denominator satisfies (0.2), so trivially

```text
sum_I N_I
 <=sum_I (|I|/q_I+O(1))
 <<Y^(1-beta)+K.                                     (3.1)
```

At the top aperture every block has length at least `Y^(8/33)`, whence

```text
K<<Y^(1-8/33)=o(Y^(1-beta)).                         (3.2)
```

Apply Cauchy to (1.2) across the blocks and insert (2.3)--(3.2):

```text
sum_I |D~_(q_I,I)|
 <=sqrt((sum_I N_I)(sum_I E_I))
 <<Y^(1-beta/2)(log Y).                              (3.3)
```

Division by `Y` proves (0.3).

## 4. Boundary and long-edge scope

The separately audited Gafni--Tao estimate controls removal of terminal
prime gaps longer than

```text
G=Y^theta,              theta=797/5000.
```

Among the retained edges, at most `O(K)` cross curvature-block boundaries.
Discarding them costs normalized positive mass at most

```text
KG/Y <<Y^(-(8/33-theta))
     =Y^(-13699/165000)=Y^(-.0830242...).            (4.1)
```

This is smaller than (0.3).  Every remaining terminal edge lies wholly in
one block, so it has one selected denominator and its entire deletion
telescope is componentwise.  The surviving prime endpoints ensure that no
pre-group gap crosses out of that edge.

There are two different savings here and they must not be conflated.  The
boundary-edge cost in (4.1) saves `.0830242...`, whereas the Gafni--Tao
long-edge tail at this cutoff saves only
`1173/65000=.0180461538...`.  Thus (0.3) clears the maximum carrier bill for
the *retained resonant group*, but this report does not show that the
long-edge disposal clears the maximum bill `.01974049`.  The global
integer-base `q`-first transport needs neither disposal for its resonant
group bound.

The exact value in (4.1) is
`8/33-797/5000=13699/165000`; fixed shell constants are absorbed in
`Y^o(1)`.

## 5. Truth boundary

```text
universal-base exact deletion reorder:               PROVED
arbitrary composite denominator q<Y:                 PROVED
selector-stable aggregate pre-group gap square:      PROVED
normalized resonant-group saving beta/2=.0799:       PROVED
cross-block boundary disposal:                       PROVED
superseded by global integer-base q-first saving:     YES
traditional SPF order required for the telescope:    FALSE
early reordered remainder:                           OPEN
late reordered remainder:                            OPEN
full prime antenna / zero-free strip from this alone: NOT CLAIMED
```

## 6. Reproduction

```bash
python3 results/verify_zeta23_universal_base_q_group.py
python3 results/verify_zeta23_matomaki_rough_gap_gate.py
```

The first checker verifies the selector/count/boundary exponent ledger and
square-refinement inequality.  The second replays the exact published-input
parameters proving (0.1).
